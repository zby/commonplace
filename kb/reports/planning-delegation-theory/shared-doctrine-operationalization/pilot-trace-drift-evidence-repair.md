# Multistage pilot: drift, evidence, and repair forward trace

> Historical first-candidate trace. Its state-machine findings remain valid,
> but its overall failure depended on then-unverified native Claude doctrine
> delivery. The later direct probe and lean-candidate comparison supersede that
> consumption-path judgment. See [the final pilot
> decision](./multistage-pilot.md).

## Result

The doctrine-compressed candidate preserves the committed workflow on the
verified Codex consumption path. It does not preserve the baseline's
self-contained control boundary on every canonical consumption path. The same
canonical skill is projected to Claude Code, where root-doctrine delivery to a
fresh worker remains unverified. On that path the candidate silently relies on
four removed rules: the parent schedules workers, integrates returns, handles
recovery, and silence grants no nested delegation.

The operational state machine, evidence invalidation, digest binding, repair
limit, and drift stop are unchanged. The regression is interpretive and
authority-path dependent, not a changed branch in the happy Codex trace. Revise
the candidate by restoring the removed parent-control and no-delegation rules
while retaining its useful doctrine-delta framing and explicit ownership of
user-owned decisions.

## Compared bytes and consumption assumptions

- **Committed baseline:**
  `git show 0acef622:kb/instructions/cp-skill-write-multistage/SKILL.md`,
  SHA-256
  `ccb0f2ceeb984b41c5ab11706a2160a4ccbdc9ed8bec57e80513ce0f25aef812`.
- **Working-tree candidate:**
  `kb/instructions/cp-skill-write-multistage/SKILL.md`, SHA-256
  `30b646c2d05bab982a7f2e7b960b4c1fd94ff6c2a59ad0ded380ec253a674792`.
- **Shared promotion reference:**
  `kb/instructions/cp-skill-write-multistage/references/promotion.md`,
  SHA-256
  `6e950a138fe1283b208c3dd0c323410f76093ae9cee8c00fd55a1d3d8065758c`.
  It has no diff from `0acef622`.
- The only baseline-to-candidate change is in `Execute now`. The candidate
  introduces the doctrine-delta framing and explicit parent ownership of
  user-owned decisions. It removes explicit parent scheduling, integration,
  and recovery and removes the blanket worker no-delegation rule. Every state,
  invalidation, digest, repair, grounding, review, and promotion clause is
  byte-identical.
- This Codex task received root `AGENTS.md` as binding repository instruction.
  The workshop's delivery probe independently records the same result for
  Codex-spawned workers, including review workers. The candidate may therefore
  inherit the root Delegation defaults on this path.
- The canonical source is also a promoted `.claude/skills/` skill. The
  workshop records Claude Code delivery as documented but not successfully
  probed and requires Claude packets to remain self-contained until delivery is
  verified. The candidate's compression therefore cannot be assumed safe for
  that canonical path.

The symbolic state used below is:

- `O` — the SHA-256 of byte-exact `original.md`;
- `H1` — the SHA-256 of candidate v1;
- `H2` — the SHA-256 of the corrected candidate, with `H2 != H1` in this
  scenario;
- `R1(H1, block)` — immutable, well-formed `review-01.md` bound to `H1`;
- `R2(H2, accept)` — immutable, well-formed `review-02.md` bound to `H2`.

"Live mutation" below distinguishes the live target from the grounding
subroutine's explicitly delegated source-side Quotes mutation. The parent owns
all target mutation, integration, and recovery. `cp-skill-ground` alone owns
its permitted ingest resolution and Quotes mutation. That is a named
conditional exception in both versions, not an authority leak.

## Delegation-control source ledger

| Control | Committed baseline | Candidate on verified Codex | Candidate where root delivery is unverified |
|---|---|---|---|
| Parent schedules workers | Explicit in baseline `Execute now` | Root `AGENTS.md` Delegation default; the skill's launch instructions specialize it | Removed source is unavailable; launch imperatives suggest but do not establish the standing ownership rule |
| Parent integrates returns | Explicit in baseline `Execute now`; stage-specific parent verification also applies | Root Delegation default plus stage-specific verification/freezing | Stage checks cover this scenario locally, but the general integration owner is now an implicit inference |
| Parent handles recovery | Explicit in baseline `Execute now`; promotion reference gives the exact mutation recovery | Root Delegation default plus exact promotion recovery | Promotion recovery remains explicit, but setup and worker-failure recovery no longer have an explicit general owner |
| Workers may not delegate | Explicit: workers do not delegate; conditional procedures are the only role additions | Root rule: nested delegation requires explicit authority and silence means no; conditional procedures remain the only explicit exceptions | Not established. The three-role topology and owned-output clauses constrain results, but do not unequivocally prohibit a worker from creating a nested worker |
| Delegation does not expand authority | Enforced by each role's owned output and mutation exclusions | Same task-specific clauses; root doctrine supplies the general interpretation | The task-specific clauses remain sufficient for the named roles in this trace |
| Worker discretion over means | Explicit in `Execute now` and each role's commission | Same | Same |
| Parent owns live-target mutation | Explicit in `Execute now`, author exclusions, review exclusions, and promotion reference | Same | Same |
| User owns reserved contribution, rebase, overwrite, retitle, and artifact-set choices | Explicit at the relevant returns and promotion gates | Also summarized at the top as parent ownership of routing user-owned decisions | Same task-specific gates remain explicit; no inherited rule is needed |
| Unstated-choice classification | Not needed to close a consequential choice in this fixed scenario | Root doctrine classifies inherited, deliberately delegated, irrelevant, and gap cases | Candidate names doctrine but does not supply the classifier; this matters if a worker encounters a route choice outside the enumerated scenario |

The baseline is therefore self-contained for every delegation default this
scenario exercises. The candidate is context-complete only when the root
Delegation section is actually delivered with binding force.

## Baseline trace

### B0 — Freeze setup and intent

- **Actor and permitted inputs:** The parent reads the settled user direction,
  live Markdown target, target collection contract, and type contract. It may
  inspect backlinks. The target identity, edit mode, contracts, contribution,
  and acceptance condition are already settled by the scenario.
- **Owned outputs and transition:** The parent writes `brief.md`, byte-exact
  `original.md`, `O`, the backlinks query, and the run `README.md`. State becomes
  `setup-frozen(O)`.
- **Invalidation, digest, and repair:** A later identity, mode, collection, or
  type change would restart setup. No candidate or review digest exists. The
  post-review repair allowance is unused and not yet active.
- **Mutation and recovery:** Workshop writes are permitted; the live target is
  read but untouched. Ambiguous or malformed matching-run state is a recovery
  stop. The parent owns that stop and recovery.
- **Delegation source:** Parent commission, scheduling, integration, mutation,
  and recovery are explicit in baseline `Execute now`. User authority over
  replacement-like choices is explicit in section 1.

### B1 — Source-only reconstruction v1

- **Actor and permitted inputs:** A fresh source reconstructor receives only
  `brief.md`, authorized source-only paths, and the exact collection/type
  contracts it needs. It cannot receive the target, `original.md`,
  incumbent-derived material, prior interpretations, candidates, or reviews.
- **Owned outputs and transition:** It owns only `reconstruction.md`. The parent
  verifies that the reconstruction answers the brief from authorized sources
  and freezes it. State becomes `reconstruction-v1-frozen`.
- **Invalidation, digest, and repair:** A changed governing premise or
  substantive evidence invalidates this state and every dependent state. No
  candidate digest or repair is involved.
- **Mutation and recovery:** The worker cannot mutate live sources or target
  state. A failed or unacceptable return stops with the parent rather than
  broadening worker authority.
- **Delegation source:** The packet states inputs, evidence boundary, sole
  output, acceptance, and worker-chosen means. Baseline `Execute now` explicitly
  prohibits worker delegation and assigns scheduling, integration, and recovery
  to the parent.

### B2 — Author v1, source-first reveal

- **Actor and permitted inputs:** One fresh consolidated author receives
  `brief.md`, frozen reconstruction v1, exact target contracts, source-only
  assessments, and any bounded duplicate/premise search. It cannot receive the
  target, `original.md`, incumbent-aware comparisons, earlier candidates, or
  reviews.
- **Owned outputs and transition:** It owns `claim-disposition.md` and later
  `candidate.md`; at this reveal it accounts for every reconstructed material
  commitment. The parent verifies and freezes the source-first disposition.
  State becomes `disposition-v1-source-frozen`.
- **Invalidation, digest, and repair:** A new material commitment returns to
  disposition. New substantive evidence would invalidate this disposition
  through its reconstruction dependency. No digest exists yet.
- **Mutation and recovery:** The author cannot change live target, sources,
  ingests, indexes, lineage, siblings, or run control.
- **Delegation source:** Inputs, outputs, mutation exclusions, acceptance, and
  discretionary representational means are explicit in section 3. Parent
  integration and no nested delegation are explicit in baseline `Execute now`.

### B3 — Author v1, incumbent reveal and candidate v1

- **Actor and permitted inputs:** The same author now additionally receives
  `original.md` and any authorized incumbent-aware assessment. The incumbent is
  a reconciliation input and supplies no warrant.
- **Owned outputs and transition:** It completes incumbent reconciliation and
  writes exact candidate v1 bytes. The parent hashes those bytes as `H1`. State
  becomes `candidate-v1(H1)`.
- **Invalidation, digest, and repair:** The candidate depends on brief,
  reconstruction v1, disposition v1, original, contracts, and grounding. Any
  change to candidate bytes requires a fresh review once review begins. Repair
  remains unused.
- **Mutation and recovery:** Only run files change. A user-owned contribution or
  mutation choice returns to the user with an exact decision and resume point;
  the author cannot decide it or touch the live target.
- **Delegation source:** Section 3 supplies staged inputs, owned outputs,
  incumbent status, acceptance shape, and user return. Baseline `Execute now`
  supplies parent integration/recovery and no nested delegation.

### B4 — Reviewer 1 blocks exact candidate v1

- **Actor and permitted inputs:** A fresh reviewer who did not author or revise
  v1 receives candidate v1 and `H1`, brief, reconstruction v1, disposition v1,
  original, contracts, grounding results, and authorized literature records. It
  cannot receive the live target, parent conversation, scratch, or prior
  reviews.
- **Owned outputs and transition:** It writes only immutable
  `review-01.md = R1(H1, block)`. The missing evidence finding names its anchor,
  basis, required byte change, and return to reconstruction. The parent verifies
  the review grammar and recomputes `H1`. State becomes
  `review-01-blocked(H1)`.
- **Invalidation, digest, and repair:** `R1` remains permanently bound to `H1`
  and cannot authorize other bytes. A well-formed block activates the one-repair
  route, but the allowance is not consumed until candidate bytes change.
- **Mutation and recovery:** The reviewer edits nothing and chooses no repair.
  A malformed or digest-mismatched review would be a parent-owned worker-failure
  stop; that branch is not taken.
- **Delegation source:** Reviewer inputs, sole immutable output, acceptance
  grammar, independence, return information, and no-mutation boundary are all
  explicit in section 5. Parent verification, integration, and recovery are
  also explicit in baseline `Execute now`.

### B5 — Ground the missing source claim and invalidate dependents

- **Actor and permitted inputs:** The parent invokes `cp-skill-ground` with
  exactly the authorized ingest/source target and the needed source-side
  proposition. Target prose and target-specific transfer reasoning are not
  permitted. No new URL authority is needed in the stipulated named-source
  case.
- **Owned outputs and transition:** The grounding subroutine alone may add the
  permitted Quotes evidence. The parent verifies the complete Quotes section,
  applies grounding alignment, records `quotes added`, and retains the exact
  appended text. State becomes `new-substantive-evidence`.
- **Invalidation, digest, and repair:** The substantive evidence invalidates
  reconstruction v1 and all dependent disposition/candidate states. `R1`
  remains an immutable historical block on `H1`, but neither `H1` nor its old
  evidence basis is review-reusable. Evidence addition alone has not changed
  candidate bytes, so the repair allowance remains unused.
- **Mutation and recovery:** This is the explicit exception to ordinary worker
  run-only ownership: `cp-skill-ground` owns the permitted source ingest Quotes
  mutation. It has no target mutation authority. Any grounding blocker would
  retain and stop the run; that branch is not taken.
- **Delegation source:** Section 4 supplies the exact grounding packet,
  mutation exception, result handling, and stop conditions. Baseline `Execute
  now` supplies parent scheduling/integration/recovery; the conditional
  procedure explicitly supplies its added role.

### B6 — Fresh source-only reconstruction v2

- **Actor and permitted inputs:** Because evidence changed after author v1 saw
  the incumbent, a fresh reconstructor receives the brief, updated authorized
  source-only paths, and exact contracts. It remains blind to the target,
  original, old reconstruction interpretation, dispositions, candidates, and
  reviews.
- **Owned outputs and transition:** It replaces the invalidated reconstruction
  with reconstruction v2 only. The parent verifies and freezes it. State becomes
  `reconstruction-v2-frozen`.
- **Invalidation, digest, and repair:** The new evidence basis starts fresh
  dependent states. `H1/R1` stay historical. Repair remains unspent until new
  candidate bytes exist.
- **Mutation and recovery:** No live mutation is permitted. Failure returns to
  the parent.
- **Delegation source:** Section 5 explicitly requires a fresh source-only
  context in this condition; section 2 supplies the exclusion set and sole
  output. Baseline `Execute now` supplies the parent and no-delegation defaults.

### B7 — Fresh author v2, repeat the source-first reveal

- **Actor and permitted inputs:** A fresh author, not author v1, receives only
  brief, reconstruction v2, exact contracts, and authorized source-only
  assessments/search. It receives neither incumbent material nor old
  candidate/review material.
- **Owned outputs and transition:** It creates a new source-first disposition;
  the parent verifies and freezes it. State becomes
  `disposition-v2-source-frozen`.
- **Invalidation, digest, and repair:** Its work depends on reconstruction v2.
  No candidate bytes have changed yet in the durable state, so repair remains
  unused.
- **Mutation and recovery:** The fresh author has only the two author-owned run
  files and no live mutation authority.
- **Delegation source:** The explicit fresh-author and both-reveals rule in
  section 5 combines with section 3's first-reveal packet. Baseline `Execute
  now` supplies parent integration/recovery and no delegation.

### B8 — Fresh author v2, repeat the incumbent reveal and correct bytes

- **Actor and permitted inputs:** After the parent freezes the new source-first
  disposition, the same fresh author receives `original.md` and any authorized
  incumbent-aware assessment.
- **Owned outputs and transition:** It repeats incumbent reconciliation and
  writes corrected candidate bytes. The parent hashes them as `H2`, with
  `H2 != H1`. State becomes `candidate-v2(H2)`.
- **Invalidation, digest, and repair:** The first candidate-byte change after
  well-formed `R1` consumes the single post-review repair. `R1(H1, block)` has no
  force over `H2`. Any further required byte change in this run must stop.
- **Mutation and recovery:** Only author-owned run files change. User-owned
  decisions still return to the user; none is invented to make the correction.
- **Delegation source:** Sections 3 and 5 explicitly require both reveals,
  fresh authorship, digest-sensitive repair accounting, and user returns.
  Baseline `Execute now` supplies the parent-control defaults.

### B9 — Rerun grounding for candidate v2

- **Actor and permitted inputs:** The parent reruns the section 4 grounding
  interface for v2's named-source dependencies. The grounder again receives
  only source identity and source-side claim needed, not target transfer prose.
- **Owned outputs and transition:** In the stipulated trace the now-retained
  evidence is sufficient, so grounding completes without another substantive
  evidence addition or candidate change. State becomes
  `candidate-v2-grounded(H2)`.
- **Invalidation, digest, and repair:** `H2` remains current. Another substantive
  evidence change would return upstream; because any resulting additional byte
  change is forbidden after the repair is used, that route could terminate the
  run. It is not taken here.
- **Mutation and recovery:** Only the grounding skill could make a permitted
  source Quotes mutation. It makes none in this event. The parent integrates
  the result.
- **Delegation source:** Sections 4 and 5 explicitly require grounding to be
  rerun and retain its exact mutation/return boundary. Baseline `Execute now`
  supplies scheduling, integration, and recovery.

### B10 — Different reviewer accepts exact candidate v2

- **Actor and permitted inputs:** A different fresh reviewer receives exact
  candidate v2 plus `H2`, brief, reconstruction v2, disposition v2, original,
  contracts, current grounding results, and authorized literature records. It
  cannot receive the live target, parent conversation, scratch, or `R1`.
- **Owned outputs and transition:** It writes only immutable
  `review-02.md = R2(H2, accept)`. The parent verifies the grammar and
  recomputes `H2`. State becomes `accepted(H2, R2)`.
- **Invalidation, digest, and repair:** Acceptance authorizes only the exact
  `H2` candidate bytes. Any candidate-byte change would need a fresh reviewer,
  but the repair allowance is already used, so it would also stop this run.
- **Mutation and recovery:** Reviewer 2 mutates nothing and cannot promote.
- **Delegation source:** Reviewer independence, input packet, exclusions,
  digest grammar, immutable output, and different-reviewer requirement are
  explicit in section 5. Parent verification/integration are explicit in
  baseline `Execute now`.

### B11 — Promotion preflight finds live-target drift

- **Actor and permitted inputs:** Only the parent loads the unchanged promotion
  reference after acceptance. It checks candidate bytes against `H2`, review
  binding, completed grounding and preflight, then compares the live target to
  byte-exact `original.md`/`O`.
- **Owned outputs and transition:** The live target differs from `O`. The
  compare fails before replacement. State becomes
  `drift-blocked; workshop-retained`.
- **Invalidation, digest, and repair:** `H2/R2` remain an internally exact
  candidate/review pair, but they are insufficient authority to overwrite a
  target with a different incumbent state. Drift requires abandon or an
  authorized rebase. The user supplied neither. Even a later authorized rebase
  cannot return within this run because the only repair was consumed; it needs
  a new run.
- **Mutation and recovery:** No target or lineage mutation occurs, so rollback
  is unnecessary. Automatic overwrite and rebase are forbidden. The parent
  retains the workshop and reports the drift blocker, both final digests,
  source mutation, and used repair.
- **Delegation source:** The main skill's drift invalidation map and section 6
  load the promotion reference. That reference explicitly assigns every
  mutation and recovery step to the parent and requires retention on a blocker.
  Baseline `Execute now` independently supplies the general parent recovery and
  integration default.

## Candidate trace on the verified Codex path

The candidate follows the same event and state sequence. The entries below
repeat the operative details to expose where its authority source changes.

### C0 — Freeze setup and intent

- **Actor, inputs, and output:** The parent uses settled user direction, target,
  contracts, and backlinks to create `brief.md`, `original.md`, `O`, and run
  control state. State is `setup-frozen(O)`.
- **Invalidation/digest/repair:** Setup identity changes restart setup. No
  candidate digest exists; repair is unused.
- **Mutation/recovery:** Target remains untouched. The candidate explicitly
  makes the invoking agent the parent and gives it live-mutation and user-owned
  decision ownership. Root doctrine supplies scheduling, integration, and
  recovery. The run-state recovery stops remain explicit in section 1.

### C1 — Source-only reconstruction v1

- **Actor, inputs, and output:** A fresh reconstructor receives only brief,
  authorized sources, and contracts; all incumbent and prior-run inputs are
  excluded. It owns only reconstruction v1, which the parent verifies and
  freezes.
- **Invalidation/digest/repair:** Substantive evidence or a governing-premise
  change invalidates this state and its dependents. No digest or repair applies.
- **Mutation/recovery:** The worker has no live mutation. The packet explicitly
  fixes evidence, ownership, acceptance, and return. Root doctrine supplies
  parent scheduling/integration/recovery and prohibits nested delegation by
  silence.

### C2 — Author v1, source-first reveal

- **Actor, inputs, and output:** One fresh author receives only brief,
  reconstruction v1, contracts, and bounded source-only assessments/search. It
  owns disposition and candidate run files and first produces the verified,
  frozen source disposition.
- **Invalidation/digest/repair:** Its state depends on reconstruction v1. No
  digest exists; repair is unused.
- **Mutation/recovery:** Explicit section 3 exclusions prohibit all live target,
  source, ingest, index, lineage, sibling, and run-control mutation. Root
  doctrine supplies integration/recovery and the no-nested-delegation rule.

### C3 — Author v1, incumbent reveal and candidate v1

- **Actor, inputs, and output:** The same author additionally receives original
  and authorized incumbent-aware assessment, reconciles without treating the
  incumbent as evidence, and writes v1. The parent records `H1`.
- **Invalidation/digest/repair:** v1 depends on all upstream state. No review has
  yet consumed repair.
- **Mutation/recovery:** Only run files change. User-owned choices explicitly
  return to the user; the candidate also summarizes parent ownership of routing
  those decisions. Root doctrine supplies the general integration/recovery
  defaults and no delegation.

### C4 — Reviewer 1 blocks exact candidate v1

- **Actor, inputs, and output:** A fresh non-author reviewer receives the exact
  bounded review packet and writes only `R1(H1, block)`. The parent verifies
  grammar and recomputes `H1`.
- **Invalidation/digest/repair:** `R1` binds only `H1`; it cannot authorize
  changed bytes. Repair becomes available but remains unused until bytes change.
- **Mutation/recovery:** Reviewer mutation and repair choice are explicitly
  forbidden. Root doctrine supplies the parent scheduling/integration/recovery
  defaults; the review worker's owned output and stop result are explicit.

### C5 — Ground the missing claim and invalidate dependents

- **Actor, inputs, and output:** The parent invokes the exact source-only
  grounding interface. `cp-skill-ground` alone owns its permitted Quotes
  mutation; the parent verifies and records `quotes added` and the exact text.
- **Invalidation/digest/repair:** New substantive evidence invalidates
  reconstruction v1 and every dependent state. `R1/H1` remain historical.
  Candidate bytes have not yet changed, so repair remains unused.
- **Mutation/recovery:** The source mutation exception and blocker stop are
  explicit. The candidate's root reliance concerns parent scheduling,
  integration, and recovery, not the grounder's task-specific authority.

### C6 — Fresh source-only reconstruction v2

- **Actor, inputs, and output:** A fresh reconstructor receives updated
  authorized sources, brief, and contracts only. It remains incumbent-blind and
  owns reconstruction v2 only. The parent verifies/freezes it.
- **Invalidation/digest/repair:** New dependents begin from reconstruction v2;
  old digest/review state is not reused. Repair remains unused.
- **Mutation/recovery:** No live mutation. The fresh-context and source-only
  rule is explicit; root doctrine supplies parent control and no delegation.

### C7 — Fresh author v2, source-first reveal

- **Actor, inputs, and output:** A fresh author receives reconstruction v2 and
  the same bounded first-reveal inputs, without incumbent or old review/candidate
  material. It writes the new source disposition; the parent freezes it.
- **Invalidation/digest/repair:** The state depends on reconstruction v2. Repair
  is still unused.
- **Mutation/recovery:** Author ownership/exclusions are explicit. Root doctrine
  supplies parent integration/recovery and no nested delegation.

### C8 — Fresh author v2, incumbent reveal and corrected bytes

- **Actor, inputs, and output:** The same fresh author receives original only
  after its source-first account is frozen, repeats reconciliation, and writes
  corrected v2. The parent records `H2 != H1`.
- **Invalidation/digest/repair:** The byte change consumes the only post-review
  repair. `R1` cannot bind `H2`; any later required byte change stops.
- **Mutation/recovery:** Only run files change. User decisions remain explicit
  returns. Root doctrine supplies the omitted stable parent controls.

### C9 — Rerun grounding for candidate v2

- **Actor, inputs, and output:** The parent reruns the exact grounding interface
  for v2. Evidence is sufficient, and no further substantive evidence or byte
  change occurs. State is `candidate-v2-grounded(H2)`.
- **Invalidation/digest/repair:** `H2` remains current. A further evidence-driven
  byte change would exceed the allowance and stop.
- **Mutation/recovery:** Grounding mutation authority remains the explicit
  conditional exception. Root doctrine supplies parent integration and
  recovery.

### C10 — Different reviewer accepts exact candidate v2

- **Actor, inputs, and output:** A different fresh reviewer receives candidate
  v2, `H2`, current upstream artifacts and grounding, and the explicit exclusion
  set. It writes only `R2(H2, accept)`; the parent verifies and recomputes `H2`.
- **Invalidation/digest/repair:** Acceptance binds only exact `H2`. No repair
  remains.
- **Mutation/recovery:** Reviewer cannot mutate or promote. Root doctrine
  supplies parent scheduling/integration/recovery and no nested delegation;
  task-specific review controls remain explicit.

### C11 — Promotion preflight finds live-target drift

- **Actor, inputs, and output:** The parent loads the unchanged promotion
  reference, verifies `H2/R2`, and compares the live target with `O`. The target
  differs, so state becomes `drift-blocked; workshop-retained`.
- **Invalidation/digest/repair:** `H2/R2` remain byte-matched but cannot authorize
  overwrite of the drifted target. No user rebase/overwrite authority exists,
  and the repair is already used; a future rebase requires a new run.
- **Mutation/recovery:** The unchanged promotion reference explicitly says the
  parent executes every mutation and recovery step, forbids automatic overwrite
  or rebase, and retains blocked runs. No write occurred, so no rollback runs.
  This terminal behavior does not depend on inherited root doctrine.

## Invariant comparison

| Invariant | Baseline | Candidate, verified Codex | Candidate, unverified root path |
|---|---|---|---|
| Source reconstruction remains incumbent-blind | PASS: both reconstruction passes receive source-only packets | PASS: identical clauses | PASS for the literal packet; no removed rule affects its exclusion set |
| New substantive evidence invalidates dependent stages | PASS: returns to reconstruction | PASS: identical | PASS: identical |
| Evidence added after incumbent reveal causes fresh reconstruction and both author reveals | PASS: fresh reconstructor, fresh author, source reveal then incumbent reveal | PASS: identical | PASS: identical |
| Changed candidate bytes receive a fresh, different reviewer | PASS: `H2` goes only to reviewer 2 | PASS: identical | PASS: identical review protocol; nested delegation uncertainty could weaken actor independence if a worker improvised helpers |
| At most one post-review repair | PASS: `H2 != H1` consumes it; no later byte change allowed | PASS: identical | PASS: exact local rule |
| Review acceptance binds exact bytes | PASS: `R2` names `H2`; parent recomputes it | PASS: identical | PASS: exact local rule |
| Parent alone owns live-target mutation | PASS | PASS: explicit in candidate and promotion reference | PASS: explicit; no inheritance needed |
| Parent owns integration and recovery | PASS: explicit globally and at promotion | PASS: inherited from verified root, specialized by stage checks and promotion | **At risk:** promotion is explicit, but the removed general default is not delivered; non-promotion recovery/integration must be inferred from scattered parent checks |
| User-owned decisions are not invented | PASS: explicit returns/gates | PASS: additionally summarized at top | PASS: explicit task-local returns/gates |
| No unauthorized nested delegation | PASS: explicit | PASS: verified root says silence means no | **FAIL:** the candidate omits the prohibition on a canonical path the workshop requires to be self-contained |
| Live-target drift stops promotion and retains the run | PASS: promotion reference rejects live target not equal to `O` | PASS: identical | PASS: promotion reference is explicitly loaded after acceptance |

## Operational and interpretive complexity

### Same structural cost

Both versions execute the same 12 named control states in this scenario:

1. setup frozen;
2. reconstruction v1 frozen;
3. source-first disposition v1 frozen;
4. candidate v1 hashed;
5. review 1 blocked;
6. substantive evidence added and dependents invalidated;
7. reconstruction v2 frozen;
8. source-first disposition v2 frozen;
9. corrected candidate v2 hashed and repair consumed;
10. grounding v2 complete;
11. review 2 accepted;
12. promotion drift-blocked with workshop retained.

Both require the same ten outbound worker/reveal handoffs: reconstructor v1,
author v1 source reveal, author v1 incumbent reveal, reviewer 1, grounding that
adds evidence, reconstructor v2, author v2 source reveal, author v2 incumbent
reveal, grounding rerun, and reviewer 2. Both take the same triggered branches:
review block to missing evidence, substantive evidence to reconstruction,
post-incumbent invalidation to fresh actors and two reveals, changed bytes to
repair consumption, acceptance to promotion, and drift without authority to a
retained stop. Neither version adds or removes an operational state, handoff,
retry, digest check, mutation, or rollback.

The active exception count is also unchanged. `cp-skill-ground` is the one
explicit source-mutation exception. The bilateral-isolation literature workers
remain a dormant, explicit topology exception and do not run in this scenario.

### Changed interpretive cost

The baseline duplicates four standing root rules in the skill: parent
scheduling, parent integration, parent recovery, and no nested delegation. On
verified Codex this duplication is unnecessary for interpretation. The
candidate consolidates those rules into the root doctrine and makes its
task-specific controls easier to distinguish: evidence boundaries, run-output
ownership, exact acceptance, live mutation, and user returns remain local.
There is no unresolved consequential choice in the fixed Codex trace.

That consolidation does not reduce operational complexity; it exchanges four
explicit local controls for four inherited controls. On Codex the exchange is
neutral-to-positive: one verified ambient surface supplies the defaults, and
the candidate's doctrine-delta sentence tells the parent how to read the stage
commissions.

Across the actual canonical deployment, however, the exchange adds a
consumption-path branch: first determine whether the current worker runtime
delivers root doctrine with binding force. The candidate neither performs that
check nor provides a fallback packet. On the unverified Claude path, four
intended inheritances become implicit assumptions. Scattered stage verbs make
parent scheduling and integration likely, and the promotion reference closes
promotion recovery, but likelihood is not a binding authority path. Nested
delegation remains materially unresolved. That failure is silent and can be
hidden behind a plausible artifact, which is the workshop's highest-cost error
class.

Restoring the stable parent-control and no-delegation sentences adds no state,
branch, handoff, or exception. It merely duplicates a few root defaults on the
verified Codex path while keeping one canonical skill safe on both promoted
runtime surfaces. Creating runtime-specific skill bodies or a runtime probe
branch would be more operational and maintenance complexity than retaining the
explicit controls.

## Consumption-path judgment

For Codex, root-doctrine delivery is verified twice: the operator records that
the harness injects root `AGENTS.md` into every spawned worker, and this pilot
worker actually received the file as binding instruction independently of its
compact task. Candidate commissions can therefore inherit the parent
scheduling/integration/recovery and silence-means-no-delegation rules. The
candidate passes the full scenario on that path.

For Claude Code, the canonical skill is available through `.claude/skills/`,
but the workshop's fresh-worker probe did not verify binding delivery of
`CLAUDE.md`/root `AGENTS.md`. The workshop explicitly says to treat those
packets as self-contained and not compress them against Commonplace doctrine.
Because one canonical source is projected into both runtime skill directories,
the live candidate deploys the compression to the unverified path too. Merely
naming Commonplace doctrine does not load it, and the instruction type contract
forbids inheritance from an unverified baseline.

This is not a reason to reject the doctrine-delta model. It is a reason to keep
the few load-bearing defaults explicit in a cross-runtime canonical skill until
all its worker paths are verified or the projections deliberately diverge.

## Final disposition

**Baseline: PASS.** It preserves every epistemic, digest, repair, authority,
drift, and retention invariant on both verified and unverified root-doctrine
paths because the exercised delegation defaults are explicit in the skill.

**Candidate: FAIL overall (PASS on verified Codex only).** Its state machine is
behaviorally identical on Codex, but it compresses load-bearing delegation
defaults into root doctrine on a canonical Claude path where delivery remains
unverified. The no-nested-delegation invariant is no longer self-contained, and
general parent integration/recovery ownership becomes implicit outside the
exact promotion branch.

**Recommendation: revise.** Keep the candidate's doctrine-delta framing,
per-stage task-specific commissions, and explicit parent routing of user-owned
decisions. Restore explicit text that the parent schedules workers, integrates
returns, and handles recovery, and that workers do not delegate. This repairs
the cross-runtime authority path without changing any state, branch, handoff,
digest, repair, or promotion control.
