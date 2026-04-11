# Security Audit Checklist

Use this reference when the audit scope is broad, the repo is unfamiliar, or
you need search starters before targeted reading.

## 1. Scope Triage

Prefer the narrowest honest mode:

- `diff` when there is a live change set
- `surface` when the concern is one subsystem or trust boundary
- `dependency` when the pressure is package or install/update risk
- `repo` only for a lightweight broad pass, not a fake full penetration test

State what you did not review.

## 2. Trust-Boundary Questions

Start by asking:

- What untrusted inputs enter the system?
- Where are auth, role, or capability gates enforced?
- What secrets or tokens exist, and where do they flow?
- What can execute commands, start subprocesses, write files, or call the
  network?
- What data is logged, persisted, or exported?
- What automation runs without an explicit human checkpoint?
- If the repo is agentic, what tools can the model invoke and on what inputs?

## 3. Hotspot Search Starters

Use targeted `rg` searches before opening files. Tune them per language.

```bash
rg -n "API_KEY|SECRET|TOKEN|PASSWORD|PRIVATE_KEY|BEGIN (RSA|OPENSSH|PRIVATE)" .
rg -n "eval\\(|exec\\(|subprocess|shell=True|os\\.system|spawn\\(|child_process|pickle\\.loads|yaml\\.load\\(" .
rg -n "innerHTML|dangerouslySetInnerHTML|render_template_string|Markup\\(" .
rg -n "jwt|session|cookie|csrf|authorize|permission|role|admin|allow_origins|CORS" .
rg -n "open\\(|Path\\(|unlink\\(|rmtree|rm -rf|upload|download|tempfile|mktemp" .
rg -n "fetch\\(|axios\\(|requests\\.|httpx\\.|urllib|webhook|callback" .
rg -n "system prompt|tool call|function call|allowed_tools|approval|sandbox" .
```

These are search starters, not evidence. Read the matched code before drawing a
conclusion.

## 4. Audit Lenses

### Secrets and Credential Handling

- Hard-coded secrets or local secrets copied into committed files
- Tokens echoed to logs, artifacts, traces, or browser output
- Secrets loaded broadly when a narrower scope would work

### AuthN, AuthZ, and Capability Boundaries

- Missing checks on write, admin, or destructive actions
- Role checks happening in the UI but not on the server or tool boundary
- Capability gates that rely on caller convention rather than enforcement

### Untrusted Content and Injection

- String-built SQL or command execution
- Path construction from user-controlled input
- Template or HTML injection
- Deserialization of untrusted data into executable objects

### File, Network, and Process Safety

- Over-broad file writes or deletes
- Shell or subprocess execution with user-controlled fragments
- SSRF-style fetch surfaces or unbounded external callbacks
- Download, upload, and archive extraction without path or type controls

### Dependency and Supply-Chain Behavior

- Install/update scripts with broad execution privileges
- Runtime fetching of code or mutable remote assets
- Dependency bump flows without validation or rollback shape
- Large dependency additions with no reason or trust note

### Logging, Persistence, and Export

- Sensitive payloads or model context stored longer than needed
- Logs that expose prompts, credentials, or private user data
- Export surfaces that bypass existing visibility or approval rules

### Agent and Automation Safety

- Tool permissions broader than the task requires
- Untrusted text routed directly into high-impact tool calls
- Automation that changes code, infra, or data without a clear gate
- Prompt-injection exposure at document, browser, or email boundaries

## 5. Severity Guidance

Use this to order findings, not to dramatize them.

- `Critical` — active path to credential exposure, auth bypass, destructive
  action, or remote code/data compromise with weak preconditions
- `High` — strong likely exploit or serious control gap on a real path, but
  with narrower conditions or impact
- `Medium` — credible weakness, unsafe default, or missing guardrail that is
  worth fixing but not obviously urgent
- `Low` — hardening, cleanup, or a risk worth documenting without immediate
  pressure

When unsure, lower the severity and explain the uncertainty.

## 6. Follow-Up Routing

- `fix now` when the issue is clear, local, and safely patchable
- `create story` when remediation is real work across files or behavior
- `add guardrail` when the bug is one example of a recurring failure mode
- `document accepted risk` when the tradeoff is known and intentional
- `no finding` when the audit did not surface meaningful issues

The skill should prefer the smallest honest next action over a broad security
program.
