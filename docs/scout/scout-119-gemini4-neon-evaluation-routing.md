# Scout 119 — Gemini 4 Neon evaluation

2026-11-18. Stage 1 proposal. Selection pending. Zero inference requests or
provider spend. Exact-name and slug checks found no match in the evaluated-model
ledger. Hydrogen, Carbon and Argon are separate evaluated models.

## API and data handling

- Google released `gemini-4-neon` on the paid Gemini Developer API on November
  18. Owner access is unverified. Use the native foreground `GenerateContent`
  endpoint at `generativelanguage.googleapis.com/v1beta/models/gemini-4-neon:generateContent`
  with the owner's existing paid credentials after selection. Qualify the actual
  schema, media payload and response handling on the first eligible owner case.
  [Release notes](https://aistudio.google.com/docs/changelog#11-18-2026)
- Text, image, audio, video and PDF input with text output. Google documents
  structured output and function calling. The unified window is 1,048,576
  tokens, with 65,536 output tokens per foreground segment. Use the native
  `thinkingConfig.thinkingLevel` field: `LOW`, `MEDIUM`, `HIGH` (default) or
  `XHIGH`. Thinking uses the output allowance and is billed. Omit custom
  sampling and thinking budgets. This proposal uses single foreground segments.
  [Developer model catalog](https://aistudio.google.com/docs/models#gemini-4)
  [Google model contract](https://docs.cloud.google.cn/gemini-enterprise-agent-platform/models/gemini/4-neon)
  [Thinking API](https://aistudio.google.com/docs/thinking)
- Standard USD per million tokens: $3 input, $0.15 implicit-cache reads and $15
  output including thinking. Budget using cold input. Carbon's temporary $2/$10
  price runs through November 30, so compare measured task cost and latency.
  [Pricing](https://aistudio.google.com/docs/pricing#gemini-4-neon)
  [Carbon release notes](https://aistudio.google.com/docs/changelog#11-10-2026)
- Use owner-confirmed public, permissively licensed or authored synthetic
  fixtures. Standard paid inputs and outputs are excluded from product
  improvement and subject to 55-day abuse-monitoring retention. Owner-specific
  zero retention is unverified. [Paid terms](https://aistudio.google.com/docs/terms#data-use-paid)
  [Abuse monitoring](https://aistudio.google.com/docs/usage-policies#how-we-handle-data)

## Numbered proposal

1. **Doc Web, $12 ($4 handwriting, $8 detector).** Start `handwriting` with the
   public LOC Barney page at **HIGH/32,768**, matched to the reviewed Hydrogen
   configuration, then Alverson if the first passes. Require at least .99 on
   each source, source review, and lower measured cost or latency at parity or
   a material source-quality gain. Hydrogen cleared .99 on both in Scout 111
   and fell below .99 on a fresh Barney run. A useful result advances through
   an independently reserved public page and normal SDK recipe replay before
   a proposed replacement of the reviewed OCR recipe. Separately screen the
   assisted detector with Image011 and a portrait discriminator at **HIGH/32,768**
   against the executable Gemini detector. Qualify original-pixel admission
   first, then score the actual final crops with genuine OCR caption hints.
   Require no integral signature, lettering or seal loss and no outside-caption
   inclusion, plus the owner's geometry gates. Recent subjects lost signature
   pixels or could not admit the original. This pool can screen up to four
   pairs and reserve recovery. Full 13-case and independent publication-path
   qualification would require further scope. [Hydrogen results](scout-111-gemini4-hydrogen-evaluation-routing.md)
   [Sol results and table landing](scout-117-gpt62-sol-evaluation-routing.md)

2. **Board Game Ingester, $13 ($4 orientation, $9 contours).** Start
   `physical-outline-retention` on authored source001 at **HIGH/32,768**, with
   fresh Sol6.1. Require zero material or rim loss and zero definite background
   leakage, plus exact component/contact/hole topology. Recent challengers
   reduced loss to 16 and 64 pixels. A pass can unlock the five other authored
   scenes, one independent edge-contact case, and native inverse/materialize/
   export proof for the contour job. Independently screen `asset-orientation`
   at **LOW/8,192** on pub012, pub014 and f24-04 against the executable Sol6.1
   and reviewed Gemini Decision 1 where accessible. Require all mandatory
   holds, zero wrong automatic rotations, and a concrete error reduction or
   at least 30% faster paired p95 at full parity and useful cost. Passing arms
   need independent source anchors and the real orientation consumer before a
   review patch. [Owner comparison history](scout-117-gpt62-sol-evaluation-routing.md)

3. **Storybook, $10.** Start `compromise-C1-chunking`/C2 complete extraction
   and identity linkage with the authored `LC-026-two-sarahs` case at **HIGH/65,536**
   versus fresh maintained Opus 4.7 complete-job control. Evaluate LC001 next
   on a useful first result, then LC016 and LC027 if warranted. Use the fixed
   blind review and full-source adjudication. Require structure and semantics
   at least .90, LC026 linkage F1 at least .90, complete source coverage and
   correct uncertainty. Hydrogen showed a narrow linkage gain with broader
   structure/source failures. This screens the complete extract/link job used
   through Dossier in the product.
   A replacement would need the independent LC041 oracle and connected C2
   consumer. [Earlier complete extraction comparisons](scout-111-gemini4-hydrogen-evaluation-routing.md)
   [Latest scope and maintained controls](scout-117-gpt62-sol-evaluation-routing.md)

4. **Dossier, $5.** Screen `standalone-semantic-value` on two authored
   namesake snapshots at **MEDIUM/8,192** against fresh Sol6.2 medium, the
   strongest recent qualification lead. The Astra reference is historical
   context. Require strict graph compilation, fixed blind Opus 4.6 source
   review, all corrected facts and uncertainty, and zero material unsupported
   claims. Seek a material semantic gain or at least 20% lower task cost at
   parity without slower completion. Full-history continuation is deferred
   while the narrower namesake opportunity remains open. The larger cohort,
   independent repeats and connected consumer proof would follow any positive
   screen before replacing the staged job. [Dossier owner results](scout-117-gpt62-sol-evaluation-routing.md#task-level-decision-table)

5. **CineForge, $7.** Start `video-understanding` on authored v4
   `vfp_active_001`, using five original ordered JPEGs at **MEDIUM/4,096** versus
   fresh Sol6.1 low and Luna low. Inspect grounding of the gradual size
   change and teal detail directly. Use the fixed blind Opus 4.6 judge, exact
   13 keys, structure at least .70, rubric and combined at least .80 and no
   invented source events. Report the 15 s and $0.02 operational targets.
   Advance a useful result to the remaining five cases and a reserved authored
   case within budget. This can update the benchmark reference. Native video,
   audio and any shipped analyzer would require their own qualified consumer.
   [Maintained fixture and comparison](scout-117-gpt62-sol-evaluation-routing.md#5--cineforge-usd7-screeningreference-decision-only)

6. **Echo Forge, $3.** Start `scene-to-soundscape-golden` on authored Tavern
   and Dungeon at **LOW/8,192** versus fresh GPT-5.4 Mini and the reviewed Ember
   job. Require all source-required sounds, grounded search metadata, and
   correct music/negative/default policies at a useful gain and within the
   $0.01 and soft 5 s targets. Hydrogen improved one difficult source while
   still missing the complete contract. Only a passing screen advances to two
   independently reserved excerpts and the actual reviewed generation command.
   [Reviewed job evidence](scout-110-muse-ember-evaluation-routing.md)
   [Hydrogen comparison](scout-111-gemini4-hydrogen-evaluation-routing.md)

## Reservation and progression

Campaign maximum **$50 USD**. Keep independent pools. Use owner worktrees under
`/Users/cam/.codex/worktrees/neon-20261118/<project-key>`. Freeze exact prompt,
source, settings, schema, scorer, control and judge matrix before the first
call. Verify current control prices and actual original-image token admission
before charging a pool. Reserve all thinking and cold input, recovery, controls,
confirmation and applicable judging within the approved pool. The following
candidate bounds are ceilings for admission, with remaining funds available
for those controls and judges.

| Pool | Maximum Neon dispatches and input/output bounds | Neon USD |
|---|---|---:|
| Handwriting | 4 × 106,000/32,768 including one recovery | 3.23808 |
| Detector | 5 × 106,000/32,768 including one recovery | 4.04760 |
| Orientation | 14 × 26,000/8,192 including one recovery | 2.81232 |
| Contours | 8 × 106,000/32,768 including one recovery | 6.47616 |
| Extraction | 5 × 26,000/65,536 including one recovery | 5.30520 |
| Semantic graph | 3 × 16,000/8,192 including one recovery | 0.51264 |
| Ordered frames | 8 × 20,000/4,096 including independent case and recovery | 0.97152 |
| Soundscape | 5 × 16,000/8,192 including one recovery | 0.85440 |

If the final admitted matrix exceeds a pool, preserve the first decision-bearing
pair and admit later cases only with their complete paired reservations. If the
first pair will not fit, stop the affected arm. High targets the documented
source-fidelity misses. Medium tests semantic and frame quality at practical
cost. Low tests short decision and generation economics. Run one semantic
setting per task. A valid gate failure stops its arm. Use the bounded recovery
slot for operational failures and saved outputs for demonstrated judge defects.
Any qualified default-switch and retirement patch remains in the owner worktree
for review. Stage 1 created this routing note and its index entry only.

## Deferred or excluded

- **Echo Forge other lanes:** retain the sole Liquid d1.2-ultra intent classifier.
  Audio generation, STT and execution are separate contracts.
- **Storybook other lanes:** photo input alone at the representative 2,010
  tokens costs $0.00603 against a $0.001/photo ceiling. Keep persona and other
  interactive decisions outside this screen because extraction is the concrete
  unresolved source-binding lead and Luna has a qualified interactive path.
- **Doc Web other lanes:** retain landed Sol6.2 literal tables (56/56 cells and
  both holds). Defer page-safety replacement until a connected consumer and
  independent fail-closed protocol can change a release decision.
- **BGI and CineForge whole pipeline:** defer joint game intake and complete
  project workspace generation pending eligible full inputs and complete owner
  source/consumer oracles.
- **RoboRally — do not evaluate:** the deterministic engine is authoritative
  at millisecond scale. Hydrogen already returned the full 007 events with a
  host-schema failure. Revisit when there is an independent valued offline
  role and an eligible rule/source cohort.
- **Ultima IV Web — defer:** live/adaptive creator evaluation lacks a maintained
  runnable outcome-grounded comparison.
- **Financial Hub / Financial Reporting — defer:** private records and no
  maintained eligible synthetic decision-quality corpus.
- **Financial Monthly Analysis / Financial Data — defer:** synthetic transport
  fixtures cannot establish source reconciliation quality.
- **VLC Thumbs — do not evaluate:** native decode, caching and bookmarks lack
  a maintained model job. **Conductor — defer:** existing deterministic catalog
  collection has no labeled model comparison for an operational decision.

## Selected execution — 2026-11-18

Cam selected all six numbered owner evaluations for a combined $50 USD ceiling.
Each owner is preparing its isolated worktree, first source matrix and budget
guard. The candidate uses the exact paid native Google route. The central
credential helper lists no configured Google provider. Owners are checking
for their existing authorized access by credential name.

All six isolated worktrees were independently verified under
`/Users/cam/.codex/worktrees/neon-20261118/`.

| Owner / directory | Branch | Base |
|---|---|---|
| `doc-web` | `codex/neon-20261118` | `4376bb7eb988eb91a6218ba819e5e99c5c113d6b` |
| `boardgame-ingester` | `codex/neon-20261118` | `155d606a373b7eea24381bb1c3c39a3d72558071` |
| `storybook` | `codex/neon-20261118-storybook` | `35ee76730f026ad849ba9ee41ee9695d52ddfb60` |
| `dossier` | `codex/neon-20261118` | `ec233b08dd617b0b4f0cf8b9070f0337468e3c0e` |
| `cine-forge` | `codex/neon-20261118` | `dd3c5ca27193b601bbff4731932ea52f002e8e86` |
| `echo-forge` | `codex/neon-20261118-echo-forge` | `97677d23eb229deada555e46f86b20d15bdb5eb4` |

Doc Web, Storybook, Dossier, CineForge and Echo Forge reached authenticated
exact model catalog access on their own credentials and passed owner guard
preflight. Their released caps sum to $37. Board Game Ingester's catalog
rejected its configured Google key with `API_KEY_INVALID`. Its two pools
remain reserved within the overall $50, and its provider dispatch is held
pending access. Catalog responses alone establish no inference or quality
result.

### Owner results

- **Doc Web, handwriting and assisted detection:** retain the reviewed
  Hydrogen handwriting recipe and the current assisted detector and manual
  gates. On the public Barney handwriting page, Neon HIGH/32,768 scored
  .988125 in 87.964 s for $0.141825 versus fresh Hydrogen .987415 in 69.337 s
  for $0.0948675. Both missed .99. On the original Image011 through the real
  assisted driver, Neon lost 740 tracked dark signature pixels compared to
  the Flash control's 999 tracked dark pixels across logo, seal and signatures.
  Both lost the same signature endpoints and included the outside caption.
  Neon cost $0.085404 and took 50.643 s versus Flash $0.0200615 and 25.679 s.
  The shared genuine caption call added $0.008523. Five settled calls
  accounted for $0.350681, $0 held. Further pages and portrait remained
  unmeasured. [Owner attempt](https://github.com/copperdogma/doc-web/blob/d211d08b66ab8d686c85114002ccd614d802a98e/docs/evals/attempts/099-neon-source-fidelity.md)
- **Board Game Ingester, orientation and contours:** existing native access
  rejected with `API_KEY_INVALID`. Keep the current orientation and contour
  workflows. Both candidate lanes are unmeasured, and no paid controls ran.
  The 50-wire frozen matrix and independent $4/$9 guards are ready. Reopen
  when a paid native key is authorized for this owner, successfully cataloged
  and then tested through the first guarded case. Zero inference, $0 known and
  $0 held. [Owner attempt](https://github.com/copperdogma/boardgame-ingester/blob/25b9aa865f12fc85c5fc6438348758ee669ffd3b/docs/evals/attempts/20261118-scout119-neon.md)
- **Dossier, namesakes:** keep GPT-6.2 Sol as the qualification lead and
  retain the current staged job. Both fresh arms compiled and passed both
  authored snapshots with all six meanings preserved per snapshot and all
  24 Neon or 25 Sol rows accepted by fixed blind Opus 4.6 review. Neon
  MEDIUM/8,192 took 102.758 s and $0.160971 in aggregate versus Sol's 35.998 s
  and $0.051934. Eight settled inference requests including four reviews
  accounted for $0.528775, $0 held. Full-history continuation and consumer
  qualification were unmeasured. [Owner attempt](https://github.com/copperdogma/dossier/blob/0c8418a13f4dad6fc967dd47f478bc1c7ceeeaaf/docs/evals/attempts/046-scout119-gemini4-neon-20261118.md)
- **Storybook, extract and link:** retain the production Dossier path. On the
  first authored LC026 pair, Neon HIGH/65,536 scored .904481 structure, .95
  semantics and .875 linkage versus Opus 4.7's .958910, .92 and .890. Both
  missed the .90 linkage gate. Neon retained both Sarahs and recovered all
  11 reference claims and 12 reference edges, with eight extra relationship
  edges and source-backed uncertainty and affect errors. Task cost and
  latency were $0.263859 and 115.232 s versus $0.190150 and 60.262 s. Eight
  settled inference requests including fixed blind reviews accounted for
  $0.520039, $0 held. LC001/016/027 and adoption qualification were unmeasured.
  [Owner attempt](https://github.com/copperdogma/storybook/blob/fbfda79f05c7b3f418b993f84397dd6f5213a8ce/docs/evals/attempts/205-gemini4-neon-complete-extraction-screen.md)
- **CineForge, ordered frames:** retain the Sol6.1 and Luna references. On the
  first five-frame authored case, Neon MEDIUM/4,096 scored .61095 combined
  versus .74575 Sol6.1 and .70785 Luna. All missed .80. Neon identified the
  teal detail and incorrectly described a camera push-in and a prop scale
  change. The bounding box stayed fixed in all five frames. Neon was
  $0.059427 and 24.142 s versus Sol6.1 $0.0101035 and 8.121 s and Luna
  $0.000542675 and 6.086 s. Six settled calls including three blind reviews
  accounted for $0.128053175, $0 held. Five other cases and the independent
  case were unmeasured. [Owner attempt](https://github.com/copperdogma/cine-forge/blob/fd0cabc6007a583ae12758116e35ac41c5df65a2/docs/evals/attempts/063-neon-ordered-frame-screen.md)
- **Echo Forge, reviewed soundscape outline:** retain Mini and the reviewed
  Ember configuration. On Tavern, Neon LOW/8,192 passed the frozen semantic
  scorer while both controls missed two criteria. All three retained four
  required sounds. Neon took 22.257 s and cost $0.044061, versus Mini 11.434 s
  and $0.0080355 and Ember 4.180 s and $0.0011001. Neon's cold input alone
  exceeded the $0.01 job target. Stop on economics. Dungeon and confirmation
  were unmeasured. Three settled calls accounted for $0.0531966, $0 held.
  [Owner attempt](https://github.com/copperdogma/echo-forge/blob/689a02df65dd8257cb01fdbbdf1f77932015d316/docs/evals/attempts/scene-to-soundscape-golden/20261118-scout119.md)

### Billing observation

The exact native `countTokens` preflight underpredicted billed input on
structured requests. Storybook received 2,459 at preflight and 4,153 in
generation. Echo Forge received 1,313 and 3,987 for Tavern. CineForge
received 6,725 and 7,534 on the original five images. The observed charges
fit their reservations. Keep the predeclared full input envelope on future
paid structured comparisons until the exact request shape has a proven cost
bound. This is metering evidence, separate from the semantic results.

### Campaign accounting and remaining decision

Five measured owners accounted for 30 physical inference calls and
**$1.580744775 USD known, $0 held** against the $50 cap. Amounts derive from
provider usage and published pricing or router receipts. Invoices remain
unreconciled. Board Game Ingester's $13 remains at $0 with its paid comparison
waiting for authorized access. Keep all six worktrees under the tabled branches
and bases for reproducing results and resuming the remaining owner. No owner
defaults were activated, committed or pushed. The Dossier worker corrected a
transient worktree path typo before use. The intended path and clean primary
checkout were independently verified.

### Board Game Ingester access recovery — 2026-11-18

Cam authorized temporary use of Storybook's paid Google credential for the
existing Board Game Ingester worktree and its unchanged $4 orientation and
$9 contour pools. The coordinator provisioned only the single ignored
`GEMINI_API_KEY` variable for that owner. The original access rejection and
frozen source matrices remain in the attempt history.

The exact native catalog returned HTTP 200 and both Neon lanes qualified for
native generation and scoring. Keep the existing orientation and contour
workflows. The first three orientation fixtures used the same frozen inputs
for all three subjects. Neon LOW/8,192 passed 2/3 versus 1/3 each for Sol6.1
and reviewed Gemini Decision 1. Neon alone correctly rotated the Mahjong
tile 270 degrees, and all three held the ambiguous texture. All three wrongly
auto-kept the rotated download icon. Its source-backed requirement was
90 degrees clockwise. The wrong automatic decision triggered the stop.
The independent panel and consumer qualification remain unmeasured.

On the first contour pair, Neon HIGH/32,768 lost 5,132 material pixels
including 5,120 rim pixels, with zero definite background leakage. Sol6.1
lost 1,550 material and rim pixels and leaked 713 background pixels. Neither
passed. Neon took 144.963 s and cost $0.230565 versus Sol's 10.513 s and
$0.0099635. The coordinator independently recalculated the Neon losses from
hash-verified truth planes and the exported mask. The other five scenes
and independent edge-contact case were unmeasured.

BGI completed 11 physical calls with $0.304212 known and $0 held, including
$0.0636835 for orientation and $0.2405285 for contours. No retries were sent.
The coordinator removed the temporary credential and empty ignored file
after all calls settled and verified their absence. The BGI worktree remains
uncommitted with its owner evidence. [Owner attempt](https://github.com/copperdogma/boardgame-ingester/blob/25b9aa865f12fc85c5fc6438348758ee669ffd3b/docs/evals/attempts/20261118-scout119-neon.md)

**Campaign complete.** All six owner decisions are settled. Total exposure was
41 inference calls, **$1.884956775 USD known and $0 held** against $50, with
no default changes or landings. Retain the reviewed Hydrogen OCR and assisted
detector in Doc Web, current BGI workflows, Dossier extraction in Storybook,
Sol6.2 as the Dossier namesake qualification lead, Sol/Luna ordered-frame
references in CineForge, and Mini/reviewed Ember in Echo Forge. Neon produced
a narrow orientation and outline quality lead without clearing the respective
automation or economic gates. No within-task effort comparison was performed.

### Publication — 2026-11-18

The six owner commits were fast-forwarded to remote `main`. The task branch
and `main` refs were checked against the exact commit in each repo.

| Owner | Verified commit on remote main |
|---|---|
| doc-web | [d211d08b](https://github.com/copperdogma/doc-web/commit/d211d08b66ab8d686c85114002ccd614d802a98e) |
| boardgame-ingester | [25b9aa86](https://github.com/copperdogma/boardgame-ingester/commit/25b9aa865f12fc85c5fc6438348758ee669ffd3b) |
| storybook | [fbfda79f](https://github.com/copperdogma/storybook/commit/fbfda79f05c7b3f418b993f84397dd6f5213a8ce) |
| dossier | [0c8418a1](https://github.com/copperdogma/dossier/commit/0c8418a13f4dad6fc967dd47f478bc1c7ceeeaaf) |
| cine-forge | [fd0cabc6](https://github.com/copperdogma/cine-forge/commit/fd0cabc6007a583ae12758116e35ac41c5df65a2) |
| echo-forge | [689a02df](https://github.com/copperdogma/echo-forge/commit/689a02df65dd8257cb01fdbbdf1f77932015d316) |

Owner close-out reused the applicable evaluation checks and verified the
affected evidence, registry records, and provider-free replays. The owner
records describe the replay inputs, protected original custody, and scope.
CineForge verified the current v40 contract manifest. Its legacy v34 check
still reports historical drift. No new inference or model changes resulted
from publication.

All six owner worktrees remain in the locations above. The Conductor
record was prepared in `/Users/cam/.codex/worktrees/neon-20261118-closeout/conductor`
on `codex/neon-20261118-closeout`, from base
`40d8b9b6d70c75597c84e9249ba44514ac83e2c0`. The Conductor primary checkout
was left in place.
