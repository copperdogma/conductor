from __future__ import annotations

import importlib.util
import io
import os
import stat
import tempfile
import unittest
from argparse import Namespace
from contextlib import redirect_stdout
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
SPEC = importlib.util.spec_from_file_location(
    "eval_credentials", ROOT / "scripts" / "eval_credentials.py"
)
assert SPEC and SPEC.loader
eval_credentials = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(eval_credentials)


class EvalCredentialTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name)
        self.vault = self.root / "vault" / "eval-credentials.env"

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_import_copy_status_and_remove_never_print_secret(self) -> None:
        secret = "secret-test-value"
        source = self.root / "source.env"
        source.write_text(f"SOURCE_KEY={secret}\n")
        output = io.StringIO()
        with redirect_stdout(output):
            eval_credentials.import_credential(
                Namespace(
                    provider="openrouter",
                    source_env=str(source),
                    source_var="SOURCE_KEY",
                    vault=str(self.vault),
                    replace=False,
                )
            )
            target = self.root / "owner" / ".env"
            eval_credentials.copy_credential(
                Namespace(
                    provider="openrouter",
                    target_env=str(target),
                    target_var="OWNER_OPENROUTER_API_KEY",
                    vault=str(self.vault),
                )
            )
            eval_credentials.status(Namespace(vault=str(self.vault), json=False))
            eval_credentials.remove_credential(
                Namespace(target_env=str(target), target_var="OWNER_OPENROUTER_API_KEY")
            )

        self.assertNotIn(secret, output.getvalue())
        self.assertEqual(stat.S_IMODE(self.vault.stat().st_mode), 0o600)
        self.assertEqual(stat.S_IMODE(self.vault.parent.stat().st_mode), 0o700)
        self.assertEqual(stat.S_IMODE(target.stat().st_mode), 0o600)
        self.assertNotIn("OWNER_OPENROUTER_API_KEY", target.read_text())

    def test_copy_preserves_existing_owner_variables(self) -> None:
        self.vault.parent.mkdir(parents=True)
        self.vault.write_text('EVAL_XAI_API_KEY="xai-test"\n')
        os.chmod(self.vault, 0o600)
        target = self.root / ".env.local"
        target.write_text('PRODUCT_KEY="keep-me"\n')

        eval_credentials.copy_credential(
            Namespace(
                provider="xai",
                target_env=str(target),
                target_var="DOSSIER_XAI_API_KEY",
                vault=str(self.vault),
            )
        )

        assignments = eval_credentials.read_assignments(target)
        self.assertEqual(assignments["PRODUCT_KEY"], "keep-me")
        self.assertEqual(assignments["DOSSIER_XAI_API_KEY"], "xai-test")

    def test_copy_refuses_to_overwrite_owner_credential(self) -> None:
        self.vault.parent.mkdir(parents=True)
        self.vault.write_text('EVAL_XAI_API_KEY="central"\n')
        os.chmod(self.vault, 0o600)
        target = self.root / ".env.local"
        target.write_text('DOSSIER_XAI_API_KEY="owner"\n')

        with self.assertRaises(eval_credentials.CredentialError):
            eval_credentials.copy_credential(
                Namespace(
                    provider="xai",
                    target_env=str(target),
                    target_var="DOSSIER_XAI_API_KEY",
                    vault=str(self.vault),
                )
            )
        self.assertEqual(
            eval_credentials.read_assignments(target)["DOSSIER_XAI_API_KEY"],
            "owner",
        )

    def test_rejects_symlink_target(self) -> None:
        real = self.root / "real.env"
        real.write_text("SAFE=value\n")
        link = self.root / "linked.env"
        link.symlink_to(real)
        with self.assertRaises(eval_credentials.CredentialError):
            eval_credentials.ensure_regular_or_missing(link, purpose="test")

    def test_check_rejects_unknown_central_variable(self) -> None:
        self.vault.parent.mkdir(parents=True)
        self.vault.write_text('UNEXPECTED_API_KEY="value"\n')
        os.chmod(self.vault, 0o600)
        with self.assertRaises(eval_credentials.CredentialError):
            eval_credentials.check(Namespace(vault=str(self.vault)))

    def test_import_requires_explicit_rotation(self) -> None:
        source = self.root / "source.env"
        source.write_text("SOURCE_KEY=new-value\n")
        self.vault.parent.mkdir(parents=True)
        self.vault.write_text('EVAL_OPENROUTER_API_KEY="old-value"\n')
        os.chmod(self.vault, 0o600)

        with self.assertRaises(eval_credentials.CredentialError):
            eval_credentials.import_credential(
                Namespace(
                    provider="openrouter",
                    source_env=str(source),
                    source_var="SOURCE_KEY",
                    vault=str(self.vault),
                    replace=False,
                )
            )


if __name__ == "__main__":
    unittest.main()
