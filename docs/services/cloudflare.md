# Cloudflare

The checked projects use Cloudflare as authoritative DNS for `copper-dog.com`.
This catalog has **no copied Cloudflare credential**. An environment-variable
scan found none; a token in CI, another machine or a remote secret store remains
possible. Do not infer account/zone IDs or access from the domain name.

## Existing recipes

Local references under `/Users/cam/Documents/Projects`:

- `roborally-web/docs/runbooks/deploy.md`: DNS-only app CNAME, Fly ACME CNAME
  and Fly ownership TXT. Fly terminates TLS for `roborally.copper-dog.com`.
- `escape-rooms-calgary/docs/research/hosting.md`: DreamHost hosting with
  Cloudflare DNS-only A record and DreamHost TLS.
- `ultima-iv-web/docs/research/story-013-private-deployment.md`: same DNS/host
  boundary for `u4.copper-dog.com`.

These examples do not establish a reusable Cloudflare Tunnel, Worker, Pages,
R2 or proxy configuration. A tunnel connector token is not a general DNS API
credential; do not reuse it as one.

## Bootstrap access and a new domain

1. Use the existing Cloudflare dashboard login to identify the account and
   zone. If using a new domain, confirm registrar delegation/nameservers and
   existing DNS/mail records before changing anything.
2. For automation, create a custom API token with only the permissions and
   resources the task needs; DNS changes typically need zone DNS edit and zone
   read only if the client discovers the zone. Restrict to the selected zone
   and set expiry where practical. Avoid the global API key.
3. Save `CLOUDFLARE_API_TOKEN` in a private local environment file, import it
   into a named profile using the [helper](../services.md), and record its real
   resource scope. Account/zone IDs can accompany it. Never paste the token.
4. Verify token status and the intended zone via read-only API calls with the
   token in an Authorization header; suppress response bodies containing
   sensitive metadata. Valid-token status alone does not prove DNS permissions.
5. Add only the records required by the target host. Existing DNS-only examples
   leave TLS to DreamHost/Fly. Proxying is a separate choice requiring compatible
   TLS and application behavior. Preserve mail and unrelated records.

The scoped-token mechanism, permissions and verification flow were checked
against [Cloudflare's token guide](https://developers.cloudflare.com/fundamentals/api/get-started/create-token/)
on 2026-10-28. Account permissions and DNS state were not checked or changed.
