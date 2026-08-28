# Audit: planning and delegation instructions and contracts

## Scope and conclusion

This audit covers non-skill surfaces that an agent, planner, or instruction author
actually consumes when planning work, delegating a bounded task, waiting for a
condition, or running parallel writes. It does not audit the promoted skill
bodies, and it makes no behavior-determining change.

The current system has two different maturity levels:

- Review, ingest, compression, and full-pass workflows already model delegation
  as a controlled boundary: the parent owns scheduling and integration, a fresh
  worker receives one bounded contract, outputs are isolated, and completion is
  verified.
- The general contracts do not state that invariant. `AGENTS.md` governs mailbox
  authority but not delegation; the instruction collection prefers clean-context
  invocation without specifying a handoff contract; the workshop contract and
  instruction type inherit an overly one-directional planner/executor rule; and
  the task-planning subsystem is scaffolded without a collection contract or
  shipped task types.

The highest-value planning change is local, not universal: revise
`kb/instructions/invert-solution-shaped-requests.md` so its “least-committing”
rule distinguishes committing now, passively waiting for an exogenous
observation, and taking a bounded action that produces information. Ask for the
cost of delay only after establishing that commitment would destroy a meaningful
alternative or create costly dependencies. Do not add a delay-cost field to
every plan, backlog item, workshop, or use of the word “deferred.”

## Evidence boundary: source theory versus Commonplace recommendation

### Source-grounded mechanisms, as retained in the research report

- Mission tactics allocates choice of means to a competent executor while the
  planner supplies purpose, intent, support, resources, information flow,
  coordination, feedback, and retained responsibility
  (`research-report.md:71-105`, **Source methodology** and **Shared mechanism**).
- Rolling-wave planning keeps future work visible at a coarser resolution and
  increases detail as information improves (`research-report.md:126-145`).
- Real-options theory makes preservation of choice conditional. Commitment must
  destroy an alternative or create costly dependencies; later observation or a
  bounded experiment must be capable of changing the choice; the opportunity
  must remain; and present benefit, coordination value, or expiry lost by
  waiting must be counted (`research-report.md:160-191`). It also recognizes
  early information-producing action (`research-report.md:164-175`).
- DAPP separates a monitored signpost, a trigger threshold, a tipping point, and
  response lead time (`research-report.md:215-245`).
- Set-based design maintains several candidates only with tests, evidence-based
  elimination, compatibility constraints, and a latest safe commitment boundary
  (`research-report.md:251-287`).

These sources do not establish the report's starting claim that codification
selects the remaining work for unpredictability (`research-report.md:48-67`),
and they do not establish that the combined method improves LLM-agent outcomes
(`research-report.md:454-456`).

### Commonplace synthesis and recommendations

The integrated rule at `research-report.md:36-44` is explicitly a Commonplace
synthesis, not a source quotation or a unit stated by any source. The report's
three operative postures—commit now, wait, and stage a probe—are a Commonplace
application of the option mechanism (`research-report.md:193-213`). The nine
machinery obligations at `research-report.md:464-487` are audit candidates, not
already-binding requirements.

For Commonplace machinery, use this decision order:

1. First ask whether committing now would materially destroy a viable
   alternative or create costly-to-reverse dependencies. If not, ordinary
   evidence, scope, and verification rules decide the task; do not demand option
   accounting.
2. If it would, distinguish:
   - **commit now** — act on current evidence, including when waiting loses more
     current benefit, coordination value, or opportunity than it preserves;
   - **passive waiting** — take no information-producing action because a named
     exogenous observation will discriminate, the opportunity will remain, and
     delay is cheap enough;
   - **bounded probe** — perform active work with a bounded cost, output, stop
     condition, and named decision it can change;
   - **multiple live alternatives** — pay carrying cost only when an evaluation
     surface and convergence boundary justify it.
3. Treat capacity queueing, a blocked dependency, a review finding disposition,
   and “do nothing” as separate states. They are not automatically real options.

## Candidate-obligation disposition

| Report obligation | Actual consumer and evidence | Authority path and disposition | Minimal result |
|---|---|---|---|
| 1. Separate fixed intent/constraints from open choices | Workshop framings (`kb/work/COLLECTION.md:13-17`) and authored instructions (`kb/types/instruction.md:20-27`) | Theory note first; then binding contracts — **change** | Qualify the executor-information rule with planner-held intent, coupling, authority, and coordination facts. |
| 2. Explain consequential deferral or delegate non-enumerable choice | Workshop plans and active-work state; `task-active` currently has status, decision record, and future steps (`kb/tasks/types/task-active.md:14-20, 39-68`) | Workshop contract — **change**; task subsystem — **proposal** | A deliberately coarse consequential item names a replanning/evidence/trigger/convergence path or explicit executor authority. |
| 3. Record preserved alternative and delay cost where commitment is costly | The commitment decision in solution inversion (`kb/instructions/invert-solution-shaped-requests.md:115-146`) | Local instruction plus real-options theory — **change** | Make this a conditional branch after costly-to-reverse commitment is established, not a universal plan field. |
| 4. Consider a bounded probe separately from waiting and commitment | Solution inversion already asks for “Cheapest validation” (`invert-solution-shaped-requests.md:91-101`) | Local instruction — **change**; active-task representation — **proposal** | Name a probe as active work with an output and decision consequence; do not label it deferral. |
| 5. Give intentionally coarse future work a convergence path | Workshop framing currently says not to pre-commit method or first targets (`kb/work/COLLECTION.md:15`); active tasks allow an unqualified “future step” (`task-active.md:62-65`) | Workshop contract — **change**; task subsystem — **proposal** | Require a control form only when future work is intentionally coarse and consequential. |
| 6. Give adaptation triggers observation, threshold, and lead time | Backlog tasks already carry `Why Not Now` and `Trigger to Activate` (`task-backlog.md:14-18, 46-50`) | Task subsystem — **proposal**; ordinary recurring work — **deliberate non-change** | Strengthen only state-conditioned adaptive triggers; cadence and simple dependency waiting do not need DAPP machinery. |
| 7. Carry alternatives only with evaluation and convergence | Solution inversion generates alternative framings (`invert-solution-shaped-requests.md:103-113`); proposals hold live options and adoption criteria (`kb/reference/proposals/README.md:3-14`) | Solution inversion — **change** only at costly commitment; proposal contract — **deliberate non-change** | Analytical alternatives may be generated and discarded in one pass. Require carrying-cost justification only when several remain live across work. |
| 8. Make delegation state intent, constraints, authority, context/resources, coordination, feedback, and recovery | Always-loaded control plane, instruction authoring contract, and every procedure that dispatches a worker | `AGENTS.md`/template and instruction contracts — **change**; sparse local procedures — **change** | One worker-facing contract per boundary; parent retains scheduling, integration, verification, and recovery. |
| 9. Use compact methodology cues only with activation fidelity | Frontloading and instruction authoring; a scoped search found no non-skill behavior surface using `Auftragstaktik`, “mission tactics,” or “mission command” | Theory plus scenario test — **experiment**; current instructions — **deliberate non-change** | Test bare cue versus explicit gloss before deployment; do not add a dormant general rule to every instruction. |

## Findings by behavior-determining surface

### 1. Add one portable delegation invariant to the control plane

**Disposition: change. Priority: high.**

Evidence:

- `AGENTS.md:136-142` says mailbox messages do not grant mutation authority or
  launch an agent. It does not state what a real delegation must carry or who
  retains orchestration responsibility.
- `AGENTS.md.template:62-85` supplies version-control and collection-routing
  defaults but no collaboration invariant.
- The control-plane theory assigns universal collaboration constraints to the
  concise always-loaded invariant layer (`kb/notes/agents-md-should-be-organized-as-a-control-plane.md:21-44`) and excludes long task-specific procedures and bulk-operation checklists (`:84-95`).
- `kb/reference/control-plane-goals.md:13-19` says `AGENTS.md` is loaded on every
  invocation, including forked contexts; `:38-46` inventories what the shipped
  template carries.
- The mailbox contract already supplies two parts of the rule for that channel:
  a self-contained request with exact paths and edit/report authority
  (`kb/messages/README.md:25-27`), while messages do not expand authority or
  guarantee delivery (`:36-38`). Posting is not the delegation mechanism.

Minimal delta:

- Add a short, harness-neutral delegation invariant to both `AGENTS.md` and
  `AGENTS.md.template`: delegation does not expand task authority; one
  worker-facing contract must identify the intended result, non-negotiable
  constraints, owned outputs/write scope, accessible inputs/resources,
  coordination boundary, verification/feedback route, and stop/escalation
  condition; the parent retains scheduling, integration, and recovery.
- Add one sentence that parallel work needs disjoint ownership or an explicit
  coordination rule; otherwise it is queued.
- Update the template inventory in
  `kb/reference/control-plane-goals.md` when the stock section changes. No
  scaffold-manifest change is needed: the template is already the resolved
  scaffold input (`src/commonplace/scaffold_manifest.py:76-79`).

Do not put rolling-wave, DAPP, set-based, or option-analysis checklists in
`AGENTS.md`. Those are task-specific and would violate the control-plane loading
test. Do not prescribe a particular harness call or context-fork argument in the
portable template.

Over-application risk: an elaborate handoff template on every small same-context
subroutine would spend more context than it protects. The invariant applies when
authority or work crosses an agent boundary; workflow-specific generated prompts
may already satisfy it. In particular, it must not cause a dispatch wrapper to
repeat a generated prompt: ADR 067 makes the generated review prompt the sole
worker contract (`kb/reference/adr/067-review-workers-read-one-prompt-and-write-one-output.md:34-57`).

### 2. Refine the instruction collection and instruction type together

**Disposition: change. Priority: high, after the theory owner is revised.**

Evidence:

- The instruction type explicitly covers “work packets handed to sub-agents”
  (`kb/types/instruction.md:10-12`). It requires goal, first-read executability,
  prerequisites, scope, decisions, and verification (`:20-26`).
- Its detail rule says to fix only what the executor cannot determine and leave
  everything live-determinable to the executor (`kb/types/instruction.md:26`).
  The linked theory currently says a plan executor is “guaranteed to know more”
  and conflates temporal deferral with delegation
  (`kb/notes/fix-what-the-executor-cant-determine-not-what-it-will.md:10-20`).
  The research report instead establishes bidirectional information positions:
  the planner may hold purpose, cross-task coupling, privileged facts, risk
  limits, and external commitments (`research-report.md:94-105, 301-314`).
- The instruction collection requires cold executability and explicit decision
  and scope boundaries (`kb/instructions/COLLECTION.md:5-17`). It treats an
  `invokes` link as a clean-context sub-agent call (`:35-55`) but does not state
  the caller/worker authority or return contract.
- `kb/instructions/write-instruction.md:10-16, 20-40` is the actual authoring
  procedure: it frontloads a cold instruction and checks decisions,
  verification, exclusions, and boundaries, but not delegated ownership or
  recovery.

Minimal delta:

- Revise the theory note first so it distinguishes planner-held and
  executor-held information, coordination commitments, passive deferral, active
  information acquisition, and delegation. Then make `kb/types/instruction.md`
  say that upstream also fixes global coupling, authority, externally binding
  commitments, and verification requirements the executor cannot safely infer.
- Add a conditional **Delegated steps** clause to
  `kb/instructions/COLLECTION.md`: an instruction that dispatches a worker must
  make caller and worker ownership, the single worker contract, output,
  verification, escalation, and recovery visible. Require clean context only
  where independence or context isolation is part of the method, not as a
  universal synonym for delegation.
- Add one conditional bullet to `write-instruction.md`'s draft checklist so the
  authoring procedure consumes the new collection rule. Do not copy the full
  theory or a fixed handoff form into every instruction.

Authority path: this is a natural-language content contract, not a schema rule.
The properties are conditional and semantic. `kb/types/type-spec.md:21-34`
assigns such content to the type contract and semantic conformance, while the
schema handles mechanically visible shape. The current review system is opt-in
and documented around notes (`kb/reference/README-REVIEW-SYSTEM.md:7-16`), so
the contract should not pretend automatic assay coverage exists for every
instruction.

Over-application risk: “provide accessible context” does not mean inherit the
parent transcript or dump every discovered file. It means resolve and package
what the worker needs and cannot cheaply or safely recover. Existing complete
generated contracts remain single authorities.

### 3. Qualify the workshop framing rule without turning every workshop into a plan

**Disposition: change. Priority: high, after the executor-boundary theory.**

Evidence:

- The work collection allows a framing or plan and says the frame should retain
  the goal, poser/role, closure, evaluation boundary, and bookkeeping
  (`kb/work/COLLECTION.md:13-15`).
- The same paragraph categorically says not to pre-commit method, first targets,
  or interpretation because live work will determine them (`:15`). It inherits
  the current theory's one-directional information premise.
- Active-work theory says live state needs the goal, next action, blockers,
  still-binding decisions, open evidence gates, and closure criteria, and places
  that state in the workshop layer first
  (`kb/notes/active-work-state-is-not-retrospective-memory-or-chat-history.md:10-18`).

Minimal delta:

- Preserve the low-friction rule for ordinary workshops.
- Replace the categorical non-commitment sentence with a conditional rule:
  do not freeze situation-dependent means merely because they can be chosen at
  framing time, but do retain planner-held intent, constraints, cross-work
  coupling, external commitments, and any coordination/evaluation premise a
  later session cannot reconstruct.
- When a framing actually contains an execution plan and intentionally leaves a
  consequential future item coarse, name one convergence form: replanning
  horizon, discriminating evidence or probe, observable trigger, latest safe
  decision point, or bounded executor authority.

Do not require an option ledger, delay cost, signpost, or threshold in every
workshop. A draft, scratch investigation, and migration trace are not all
adaptive plans; the collection's quality goal remains “move the work forward”
(`kb/work/COLLECTION.md:5-9`).

### 4. Put real-options discipline in the instruction that actually chooses commitment

**Disposition: change. Priority: highest planning delta.**

Evidence:

- `invert-solution-shaped-requests.md` exists to stop premature implementation
  (`:8-10`) and excludes already-scoped, reversible, validated, and emergency
  work (`:25-30`).
- It already elicits cheap local validations (`:91-101`) and alternative
  framings that imply different solution classes (`:103-113`).
- Its decision rule is nevertheless “Prefer the least-committing route that
  preserves learning” (`:115-130`), and its single-action examples include
  “defer with the reason stated” (`:132-146`). This can prefer delay without
  establishing a preserved option, later discriminating observation,
  opportunity availability, or delay cost.

Minimal delta:

- Keep the seven-section short report and the requirement to recommend exactly
  one next move. Add a conditional commitment check inside `Recommended next
  move`, not a universal eighth section.
- Trigger the check only when the proposed solution would destroy a meaningful
  alternative or create costly dependencies. Compare internally, then select
  one of: commit now; passively wait for a named exogenous observation; run a
  bounded information-producing probe; or decline/do nothing.
- In that branch, name the preserved alternative, what observation or probe can
  change the choice, whether the opportunity will remain, and the current
  benefit, coordination value, or expiry cost lost by waiting.
- Replace the unconditional “least-committing” preference with the smallest
  sufficient action whose commitment, delay, information, and maintenance costs
  are justified. Clarify that a probe is active work, while passive deferral
  needs a named observation or trigger.

The instruction may still generate three to five alternative framings while
recommending one action. Those framings are comparison inputs discarded within
the pass, not automatically several maintained options. Do not require
set-based carrying-cost machinery unless the workflow keeps them live after the
report.

Over-application risk: forcing this branch on every mechanical or reversible
request would create “options theatre,” delay obvious work, and violate the
instruction's exclusions. Delay cost is required here only after consequential
commitment is established.

### 5. Resolve the task subsystem before changing its planning types

**Disposition: proposal now; deliberate non-change to task type files until the proposal resolves. Priority: medium.**

Evidence:

- `task-backlog` models passive retention through `Why Not Now` and `Trigger to
  Activate` (`kb/tasks/types/task-backlog.md:12-18, 30-50`).
- `task-active` models status, prerequisites, goal, context, a decision record,
  next and future steps, and resumable current state
  (`kb/tasks/types/task-active.md:12-20, 34-72`). Its status currently collapses
  information gathering and dependency waiting into one small vocabulary
  (`:39-45`).
- `task-recurring` is a stable runbook whose individual run state belongs in an
  output log (`kb/tasks/types/task-recurring.md:10-17, 29-54`). Recurrence is not
  evidence that a run is state-adaptive.
- The scaffold creates `kb/tasks/{backlog,active,completed}` directories
  (`src/commonplace/scaffold_manifest.py:41-50`; described at
  `kb/reference/instruction-generation.md:29-41`) but ships no tasks tree,
  `COLLECTION.md`, README, or task type files
  (`scaffold_manifest.py:52-79`; `instruction-generation.md:43-68`).
- `AGENTS.md:120-134` and `AGENTS.md.template:70-85` route `kb/work/` but not
  `kb/tasks/`. The collection definition's current top-level inventory also
  excludes tasks (`kb/reference/definitions/collection.md:37-45`).
- Existing theory calls tasks an early workshop-like subsystem outside the KB
  and says its ad hoc conventions are adequate for now
  (`kb/notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md:57-75`),
  while newer active-work theory places active state in `kb/work/` first
  (`active-work-state-is-not-retrospective-memory-or-chat-history.md:16-18`).

Proposal question: either consolidate task state into workshops, or establish
`kb/tasks/` as an operative temporal subsystem with a local contract, landing,
shipped types, scaffold files, and AGENTS/template route. Editing source-only
task types before that decision creates a second planning contract that installed
projects do not receive.

If tasks remain distinct, the eventual minimal type deltas are:

- Backlog: ordinary capacity/priority waiting may keep the existing fields. Only
  when deferral preserves a costly-to-reverse consequential choice should it
  name the preserved alternative, exogenous discriminating observation,
  availability/expiry, and cost of waiting. If the missing information can be
  produced cheaply, route a bounded probe to active work instead of calling it
  backlog waiting.
- Active: distinguish `probing <decision>` from `waiting for <observable
  dependency/condition>` and require an intentionally coarse consequential
  future step to name its evidence, replan point, trigger, convergence boundary,
  or executor authority.
- Recurring: no generic DAPP fields. Add observation/threshold/lead-time only to
  a particular runbook that actually adapts to monitored state; external cadence
  is a different control form.

Over-application risk: a schema or mandatory option fields would add ceremony to
cheap task capture and falsely price simple priority waits as irreversible
investment decisions.

### 6. Preserve strong local delegation contracts; patch only the sparse mutating ones

#### Deliberate non-changes

| Procedure | Evidence | Finding |
|---|---|---|
| `run-review-batches.md` | Parent owns selection through reporting (`:8-33`); jobs are not invented/reordered (`:71-84`); work is queued under capacity, fresh, and single-use (`:86-102`); generated prompt is the sole contract and finalization is all-or-nothing (`:94-119`). | **Deliberate non-change.** This is the reference implementation. Do not add a duplicate wrapper or ask the worker to plan the batch. |
| `run-full-improvement-pass-on-note.md` | Exclusive ownership precondition (`:19`); parent/worker roles, no recursion, queueing, and single use (`:23-27`); re-entry guards (`:43-54`); one bounded recovery or rollback/hand-back (`:129-141`). | **Deliberate non-change.** It already binds authority, observation, convergence, and recovery to the workflow's risk. |
| `run-compression-bundle-on-note.md` | Orchestrator/reviewer roles and no recursive dispatch (`:30-33`); exact packet inputs, one output, and verification (`:34-46`); report-only authority (`:98-103`). | **Deliberate non-change.** No option analysis is at issue. |
| `draft-ingest-report.md` | Caller owns capture/checksum/discovery and handoff; worker owns one analysis/report and cannot orchestrate (`:8-29`); missing inputs stop and the supplied snapshot/connect report bound evidence (`:42-53`). | **Deliberate non-change.** The caller has already resolved what should be frontloaded. |
| `composition-friction-gate.md`, `premise-decomposition-gate.md`, `critique-note.md` | Fresh, single-use checker; caller owns lifecycle; reports mutate no target (`composition-friction-gate.md:8-16, 30-32`; `premise-decomposition-gate.md:8-18, 61-63`; `critique-note.md:8-24`). | **Deliberate non-change.** These are isolated report roles, not delegated consequential action. |
| `assess-a-claim-bearing-artifact-against-external-literature.md` | Explicit composition ownership (`:12-18`); bilateral isolation only on named triggers and specifically not generalized from one case (`:22-42`); mutation remains behind disposition and verification (`:60-80`). | **Deliberate non-change.** It is already an anti-overapplication precedent. |
| `re-ingest.md` | Delegated drafting is owned by the ingest skill with exact backup/restore semantics (`:54-59`); post-success audit cannot dispatch another drafting pass (`:63-74`); multiple re-ingests must not be batched because each changes the next input state (`:118-125`). | **Deliberate non-change.** Sequentiality is a dependency constraint, not missed parallelism. |

#### Sparse mutating procedures

**`fix-warnings/fix-review-warnings-sweep.md` — disposition: change; priority:
high.** It launches one mutating worker per note and asserts independence
(`:31-37`), but it does not define the parent role, concurrency queue, clean
context/no-recursion boundary, pre-existing ownership collision check, or failed
worker recovery. Its sibling summary repeats the same abbreviated rule
(`kb/instructions/FIX-SYSTEM.md:87-94`).

Minimal delta: state that the orchestrator owns selection, capacity queueing,
collision checks, integration, and failure handling; assign one exact note and
its exact fix-report path per fresh single-use worker; forbid recursive
delegation; verify the target diff, report, and relevant validation before
releasing the worker. Do not dispatch a note or report path concurrently owned
or being edited. On missing/partial output or an expanded substantive decision,
stop and report rather than silently launching a repair worker. Update the
`FIX-SYSTEM.md` composition summary in the same change. Leave a general retry,
rollback, and bulk-run-record design to the active bulk-operations workshop,
which already frames sharding as explicit inputs, outputs, authority, collision
boundaries, integration, and validation (`kb/work/bulk-operations/README.md:13-27,
53-65`).

Over-application risk: findings classified `Deferred` by the per-note fixer mean
“requires a substantive human decision” (`fix-review-warnings.md:35-43`). That
is a disposition, not passive option-preserving waiting. Do not require a delay
cost or activation trigger in those reports.

**`revise-note.md` tag follow-up — disposition: change; priority: medium.** The
main pass is correctly limited to one note (`:14-18, 33-48`), but the tag-change
worker is told to inspect nearby notes, indexes, and workflows and directly make
minimal external edits (`:48`). The parent should pass the exact old/new tags and
final note path, define the allowed external artifact class, and make broader
taxonomy or authored-note changes report-only. The worker may discover live
impacts, but discovery does not itself expand mutation authority. Preserve the
existing single-use and parent-verification requirements.

### 7. Do not add a planning schema, validator, or catalog gate yet

**Disposition: deliberate non-change.**

Evidence:

- The candidate obligations are conditional semantic judgments: whether a
  commitment is consequential, an observation discriminates, a probe is bounded,
  or an executor has an information advantage. A schema can inspect an
  intra-document shape but not judge those meanings
  (`kb/reference/validation-contract.md:23-33, 49-55`).
- A type spec should state checkable content properties; production process that
  is invisible from the finished artifact belongs in an instruction
  (`kb/types/type-spec.md:19-34`).
- A catalog gate must own one sharper named failure mode, while conformance to a
  type contract as a whole belongs to the type-conformance pair
  (`kb/types/review-gate.md:28-40`). Gates are uncalibrated problem-noticing, not
  reject authority (`:35-40`).
- The current review system is experimental, opt-in, and snapshot-anchors a note
  against criterion text (`kb/reference/README-REVIEW-SYSTEM.md:7-16, 18-45`).
  It has no registered plan or delegation-packet target kind.

Do not create required fields merely because the theory can name them. First
establish an operative plan/task artifact and stable content contract. If such a
type is adopted, use its type-conformance criterion for the whole contract. Add
a catalog gate only for a separately recurring failure that remains meaningful
across types and has been calibrated. Deterministic validation becomes justified
only for a stable symbolic invariant, such as a required output-owner field in a
future typed delegation packet—not for whether the owner assignment is wise.

### 8. Run two bounded experiments instead of deploying compact methodology cues

**Disposition: experiment. Priority: after theory promotion, before cue use or
stronger enforcement.**

1. **Activation fidelity.** Across the supported model partitions, compare the
   same bounded delegation scenarios under no cue, bare `Auftragstaktik`, and the
   explicit gloss “preserve intent and constraints; delegate execution-time
   choice of means.” Blindly assess whether the result preserves intent,
   delegates means, states authority/resources/feedback/recovery, and avoids
   importing irrelevant military machinery. This tests the ambiguity identified
   at `research-report.md:121-124, 398-415`. It is a workshop scenario test, not
   a review-system gate over notes.
2. **Commit/wait/probe discrimination.** Use a small crossed scenario set varying
   reversal cost, existence of a later discriminating observation, opportunity
   expiry/current benefit, and availability of a cheap information-producing
   action. Compare the incumbent and proposed solution-inversion wording. The
   target behavior is choosing the right posture and declining option analysis
   when commitment is cheap—not maximizing deferral.

Do not hold the basic authority-boundary safety changes hostage to these tests.
The experiments decide compact cue fidelity and the least burdensome exact
real-options prompt shape; they do not decide whether parents retain
accountability.

### 9. Keep frontloading, proposal options, and ordinary waiting scoped

**Disposition: deliberate non-change.**

- Frontloading already applies only to values known before the consuming call,
  including caller-resolved inputs (`kb/notes/frontloading-spares-execution-context.md:22-35`),
  and explicitly stops when the executor is better placed to choose (`:35-37`).
  The missing rule is handoff completeness, not “frontload more.”
- The instruction collection and authoring procedure already require cold,
  self-contained execution (`kb/instructions/COLLECTION.md:15-17`;
  `write-instruction.md:10-16`). Add delegation ownership conditionally; do not
  replace self-containment with full conversation inheritance.
- The proposal contract already preserves options without claiming a decision
  and requires forces and adoption criteria
  (`kb/reference/proposals/README.md:3-14`). A proposal is an undecided design
  artifact, not automatically an execution plan. Do not require delay cost in
  every proposal; apply the real-options branch only when adoption would be a
  costly-to-reverse commitment and waiting is itself under consideration.
- Queued review jobs (`run-review-batches.md:77-102`) and a worker waiting for
  capacity are scheduler state. They do not preserve a decision option and need
  no real-options record.

## Dependency and implementation order

1. **Promote/revise theory first.** Refine
   `fix-what-the-executor-cant-determine-not-what-it-will.md`; add or promote the
   atomic claims “intent-framed delegation is a control regime” and “productive
   deferral requires an option, discriminating evidence, and convergence”; add
   the conditional real-options test to
   `current-task-fit-alone-does-not-warrant-costly-entrenchment.md`; and bound the
   low-degree-of-freedom heuristic by whether the feasible set is known. The
   research report assigns those owners at `:352-396`.
2. **Deploy the universal safety seam.** Update `AGENTS.md`,
   `AGENTS.md.template`, and the control-plane reference together. This change is
   independent of the exact real-options experiment wording.
3. **Deploy the authoring contracts atomically.** Update the instruction type,
   instruction collection, `write-instruction.md`, and workshop collection from
   the promoted theory. Inspect direct composition siblings as
   `kb/instructions/COLLECTION.md:21-27` requires.
4. **Change the actual decision consumer.** Revise
   `invert-solution-shaped-requests.md`; run the commit/wait/probe scenarios; keep
   the shortest wording that discriminates the cases.
5. **Patch mutating delegation outliers.** Update the warnings sweep and its
   `FIX-SYSTEM.md` summary, then narrow the tag-change handoff in `revise-note.md`.
   Re-audit other non-skill dispatchers against the collection contract without
   rewriting workflows that already comply.
6. **Decide the task-system proposal.** Only after adoption should task contracts,
   scaffold files, AGENTS routes, schemas, or validators change.
7. **Run activation-fidelity experiments before any compact methodology cue is
   deployed.** If no cue is used, no runtime rule is needed.

For the Markdown instruction and contract deployments, validate each changed
typed artifact and its affected collection. Treat the template as scaffold input
and exercise the scaffold tests if its emitted content changes. No new catalog
gate, schema, validator, or runtime code is warranted by this audit alone.
