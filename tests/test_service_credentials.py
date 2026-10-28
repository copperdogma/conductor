"""Credential boundary tests use synthetic values, never the real vault."""
import contextlib
import io
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import service_credentials as s


class ServiceCredentialTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.source = self.root / ".env"
        self.source.write_text('GOOGLE_CLIENT_ID="sample-id"\nGOOGLE_CLIENT_SECRET=\'literal-$(touch forbidden)\'\nOTHER_SECRET=excluded\n')

    def test_selected_only_and_literal_without_shell_execution(self):
        data = {"version": 1, "profiles": {}}
        s.import_profile(data, "test", "google", self.source,
                         {"GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET"}, "test scope")
        values = data["profiles"]["test"]["values"]
        self.assertEqual(set(values), {"GOOGLE_CLIENT_ID", "GOOGLE_CLIENT_SECRET"})
        self.assertEqual(values["GOOGLE_CLIENT_SECRET"], "literal-$(touch forbidden)")
        self.assertFalse((self.root / "forbidden").exists())
        with self.assertRaises(s.CredentialError):
            s.import_profile(data, "test", "google", self.source, {"GOOGLE_CLIENT_ID"}, "scope")

    def test_bad_keys_duplicates_missing_and_multiline_fail_closed(self):
        for text in ['GOOGLE_CLIENT_ID=a\nGOOGLE_CLIENT_ID=b', 'GOOGLE_CLIENT_ID="unterminated',
                     'GOOGLE_CLIENT_ID=', 'GOOGLE_CLIENT_ID=your_client_id', 'GOOGLE_CLIENT_ID="line\nnext"']:
            with self.subTest(text=text):
                self.source.write_text(text)
                with self.assertRaises(s.CredentialError):
                    s.read_selected(self.source, {"GOOGLE_CLIENT_ID"})
        with self.assertRaises(s.CredentialError):
            s.import_profile({"profiles": {}}, "bad", "google", self.source, {"OTHER_SECRET"}, "scope")

    def test_vault_permissions_and_symlinks(self):
        vault = self.root / "private/vault.json"
        data = {"version": 1, "profiles": {}}
        s.save(data, vault)
        self.assertEqual(stat.S_IMODE(vault.stat().st_mode), 0o600)
        self.assertEqual(stat.S_IMODE(vault.parent.stat().st_mode), 0o700)
        self.assertEqual(s.load(vault), data)
        vault.chmod(0o644)
        with self.assertRaises(s.CredentialError):
            s.load(vault)
        link = self.root / "link"
        link.symlink_to(vault.parent, target_is_directory=True)
        with self.assertRaises(s.CredentialError):
            s.save(data, link / "new.json")

    def test_export_only_new_ignored_untracked_file(self):
        subprocess.run(["git", "init", "-q", str(self.root)], check=True)
        (self.root / ".gitignore").write_text("credentials*.json\n")
        profile = {"values": {"GOOGLE_CLIENT_ID": "id", "GOOGLE_CLIENT_SECRET": "private"}}
        target = self.root / "credentials.json"
        s.export_profile(profile, {"GOOGLE_CLIENT_ID"}, target)
        self.assertEqual(json.loads(target.read_text()), {"GOOGLE_CLIENT_ID": "id"})
        self.assertEqual(stat.S_IMODE(target.stat().st_mode), 0o600)
        with self.assertRaises(FileExistsError):
            s.export_profile(profile, {"GOOGLE_CLIENT_ID"}, target)
        with self.assertRaises(s.CredentialError):
            s.export_profile(profile, {"GOOGLE_CLIENT_ID"}, self.root / "visible.json")
        tracked = self.root / "credentials-tracked.json"
        tracked.write_text("existing")
        subprocess.run(["git", "-C", str(self.root), "add", "-f", tracked.name], check=True)
        tracked.unlink()
        with self.assertRaises(s.CredentialError):
            s.export_profile(profile, {"GOOGLE_CLIENT_ID"}, tracked)

    def test_fly_only_access_token(self):
        self.source.write_text('access_token: "test-fly-session"\nmetrics_token: do-not-copy\n')
        self.assertEqual(s.read_selected(self.source, {"FLY_API_TOKEN"}, True),
                         {"FLY_API_TOKEN": "test-fly-session"})

    def test_hash_backslash_and_comments_preserve_literal_values(self):
        for raw, expected in [("abc#def", "abc#def"), (r"abc\def", r"abc\def"),
                              ("abc # comment", "abc"), ('"abc#def" # comment', "abc#def"),
                              (r'"abc\def"', r"abc\def"), ('"abc"junk', None)]:
            with self.subTest(raw=raw):
                if expected is None:
                    with self.assertRaises(s.CredentialError):
                        s.parse_literal(raw)
                else:
                    self.assertEqual(s.parse_literal(raw), expected)

    def test_list_and_error_do_not_expose_values(self):
        from unittest.mock import patch
        sentinel = "SECRET-SENTINEL-PRIVATE"
        data = {"version": 1, "profiles": {"test": {"service": "google", "values": {"GOOGLE_CLIENT_SECRET": sentinel}}}}
        output = io.StringIO()
        with patch.object(sys, "argv", ["helper", "list"]), patch.object(s, "load", return_value=data), contextlib.redirect_stdout(output):
            self.assertEqual(s.main(), 0)
        self.assertNotIn(sentinel, output.getvalue())
        with patch.object(sys, "argv", ["helper", "list"]), patch.object(s, "load", side_effect=ValueError(sentinel)), contextlib.redirect_stderr(output):
            self.assertEqual(s.main(), 1)
        self.assertNotIn(sentinel, output.getvalue())


if __name__ == "__main__":
    unittest.main()
