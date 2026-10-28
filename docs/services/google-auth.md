# Google authentication and authorization

Choose the flow before choosing credentials. We have two different working
patterns; copying an OAuth secret is not always needed for Google sign-in.

## Identity-only browser sign-in

Ultima IV uses Google Identity Services ID tokens. The frontend uses a public
client ID; the backend validates signatures/claims and uses the stable Google
subject as account identity. This does **not** require a web OAuth client secret
or delegated access to Google APIs.

Read `/Users/cam/Documents/Projects/ultima-iv-web/web/server/README.md` and
`docs/runbooks/account-saves.md` in that repo. The documented Google project is
`u4-copper-dog`; project name alone does not grant Cloud Console access. Register
the intended browser origins and validate issuer, audience, expiry and relevant
identity claims server-side. Do not trust a client-supplied email as ownership.
See Google's [server-side ID-token verification guide](https://developers.google.com/identity/gsi/web/guides/verify-google-id-token)
(checked 2026-10-28), including CSRF handling appropriate to the integration.

## Server authorization-code login / delegated API access

Storybook uses a confidential Google web client with ID/secret, authorization
code flow, PKCE/state cookies and `openid profile email`. Its documented callback
is `https://storybook.chat/auth/google/callback`. Read
`/Users/cam/Documents/Projects/Storybook/storybook/packages/backend/src/auth.ts`
and its deployment story before adapting it. Application sessions and cookies
are project-owned and are not copied into this catalog.

Available copies: `google-storybook`, `google-next-auth-template`,
`google-calendar-production`, `google-calendar-local`. Each holds only
`GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`. Their current registrations,
ownership, consent configuration, validity and allowed callbacks are unverified.
Calendar API grants and refresh tokens were intentionally excluded.

## New project recipe

1. Select identity-only sign-in or authorization for named Google APIs. Reuse
   the existing Cloud Console account/project if appropriate; create a dedicated
   client for a new application/environment by default. Existing clients are
   useful for maintaining their existing apps, not universal login credentials.
2. In [Google Auth Platform](https://console.cloud.google.com/auth/overview),
   confirm project, branding/audience, consent configuration and needed scopes.
   Register exact production and local origins/callbacks for the chosen flow.
   Do not silently add callbacks or scopes to a production client's registration.
3. Keep confidential client secrets server-side. A browser client ID is public;
   a client secret, refresh token or application session key is not. Use a
   maintained library for token validation/PKCE/state and bind sessions to a
   verified subject. Never copy another app's session signing secret.
4. Test local and production callback/origin behavior, consent and login/logout
   under the owning project's acceptance criteria. Google sign-in configuration
   alone does not implement sessions, account linking or access controls.

[Google's web-server OAuth guide](https://developers.google.com/identity/protocols/oauth2/web-server),
checked 2026-10-28, requires a registered client and exact callback matching.
Local source confirms Ultima's distinct ID-token pattern; no live login,
Cloud Console access or credential rotation occurred during this catalog setup.
