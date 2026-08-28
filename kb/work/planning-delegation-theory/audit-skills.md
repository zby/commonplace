# Skill audit: planning and delegation

## Audit boundary

This audit covers every `SKILL.md` under `kb/instructions/`, the runtime
projections of those skills, and the instructions and type contracts that
directly govern their dispatches or outputs. It evaluates current behavior
against the mechanisms established or synthesized in the
[research report](./research-report.md). It does not amend any operative
artifact.

The audit asks six questions at each decision surface:

1. What must the parent or instruction author fix before delegation?
2. What may the executor choose from live state?
3. Is a future or consequential choice intentionally deferred, or merely
   omitted?
4. If deferred, what later observation can change it, will the option remain
   available, and how does the work converge or escalate?
5. Could a bounded probe buy the missing information more cheaply than either
   waiting or committing fully?
6. Does the procedure state its mechanism, or rely on a compact methodology
   name to activate an unspecified model prior?

## Source-derived theory and Commonplace synthesis

The distinction in this section is load-bearing. The external sources support
the mechanisms in the first table. The final audit rule is a Commonplace
synthesis; no source states it as a unit, and the current source set does not
establish that applying it improves LLM-agent outcomes.

### Mechanisms supported by the external sources

| Method family | Source-derived mechanism | Boundary relevant to this audit |
|---|---|---|
| Mission tactics | The senior supplies task and purpose, intent, support, and coordination-essential guidance; a competent subordinate chooses means from local conditions, with feedback and retained upstream responsibility. | Delegation is not an outcome-only prompt. The parent may hold purpose, cross-task coupling, privileged facts, risk limits, and external commitments that the worker cannot reconstruct. |
| Rolling-wave planning | Detail near work while retaining later work at a coarser level; elaborate it when its premises improve. | A coarse future is not an unowned placeholder. It needs a replanning or relearning point. The method does not itself require delegation. |
| Real options | Preserve a costly-to-reverse choice only when later observation can change it, commitment would destroy a valuable alternative, the opportunity will remain available, and the value preserved exceeds delay cost. | Uncertainty by itself does not justify deferral. A bounded information-producing action may dominate both passive waiting and full commitment. |
| Dynamic Adaptive Policy Pathways | Couple a stable objective and near-term action to monitored signposts, response-triggering thresholds, and enough lead time to change course. | “Decide later” is governable only when the observation, consequential condition, viable response, and response horizon are named. |
| Set-based design | Retain an evaluable feasible set, actively produce discriminating evidence, eliminate weak alternatives, and converge by a latest safe commitment boundary. | Multiple candidates are justified only when an evaluation surface and convergence rule earn their carrying cost. |

### Commonplace synthesis used as the target-side audit rule

Fix upstream the intent, constraints, privileged facts, arbitrary conventions,
and coordination boundaries that execution cannot safely reconstruct. Leave
to execution decisions whose premises depend on live state or evidence the run
will produce. Preserve alternatives only while later observation or a bounded
probe can discriminate among them, the opportunity remains available, and the
value of waiting exceeds its cost. A planned deferral names how it re-enters
the decision process and how it converges or escalates.

This rule does **not** imply a planning form, a real-options calculation, a
DAPP pathway diagram, or a set-based tournament for every task. The theory is
a decision test. It should become extra workflow machinery only where a
recurring consequential choice needs that machinery.

## Inventory and projection status

### Skill sources

The ten `cp-skill-*` rows marked **promoted** are the exact entries in
`src/commonplace/scaffold_manifest.py::MANIFEST.promoted_skills`. Installed
projects receive real copied directories. This source checkout uses the exact
symlink projections shown below.

| Canonical source | Status | Runtime projection paths | Decision-surface relevance |
|---|---|---|---|
| [`kb/instructions/cp-skill-write/SKILL.md`](../../instructions/cp-skill-write/SKILL.md) | Promoted | `.agents/skills/cp-skill-write/SKILL.md`; `.claude/skills/cp-skill-write/SKILL.md` | Resolves intent, chooses ordinary versus multistage writing, delays the first target write until source guards pass. |
| [`kb/instructions/cp-skill-validate/SKILL.md`](../../instructions/cp-skill-validate/SKILL.md) | Promoted | `.agents/skills/cp-skill-validate/SKILL.md`; `.claude/skills/cp-skill-validate/SKILL.md` | Deterministic, non-delegating terminal check. |
| [`kb/instructions/cp-skill-connect/SKILL.md`](../../instructions/cp-skill-connect/SKILL.md) | Promoted | `.agents/skills/cp-skill-connect/SKILL.md`; `.claude/skills/cp-skill-connect/SKILL.md` | Produces regenerable candidates without committing library edges. |
| [`kb/instructions/cp-skill-convert/SKILL.md`](../../instructions/cp-skill-convert/SKILL.md) | Promoted | `.agents/skills/cp-skill-convert/SKILL.md`; `.claude/skills/cp-skill-convert/SKILL.md` | Defers semantic metadata and advertises unimplemented future conversions. |
| [`kb/instructions/cp-skill-health-check/SKILL.md`](../../instructions/cp-skill-health-check/SKILL.md) | Promoted | `.agents/skills/cp-skill-health-check/SKILL.md`; `.claude/skills/cp-skill-health-check/SKILL.md` | Runs ordered diagnostic probes and recommends the smallest repair. |
| [`kb/instructions/cp-skill-ingest/SKILL.md`](../../instructions/cp-skill-ingest/SKILL.md) | Promoted | `.agents/skills/cp-skill-ingest/SKILL.md`; `.claude/skills/cp-skill-ingest/SKILL.md` | Strong parent/worker split, isolated dispatch, bounded repair, incumbent backup and restoration. |
| [`kb/instructions/cp-skill-snapshot-web/SKILL.md`](../../instructions/cp-skill-snapshot-web/SKILL.md) | Promoted | `.agents/skills/cp-skill-snapshot-web/SKILL.md`; `.claude/skills/cp-skill-snapshot-web/SKILL.md` | Adapter routing, bounded metadata reads, explicit stop instead of open-ended fallback search. |
| [`kb/instructions/cp-skill-revise-autoreason/SKILL.md`](../../instructions/cp-skill-revise-autoreason/SKILL.md) | Promoted, experimental | `.agents/skills/cp-skill-revise-autoreason/SKILL.md`; `.claude/skills/cp-skill-revise-autoreason/SKILL.md` | Preserves A/B/AB alternatives, uses evidence gates and blind evaluation, caps passes, retains the incumbent. |
| [`kb/instructions/cp-skill-write-multistage/SKILL.md`](../../instructions/cp-skill-write-multistage/SKILL.md) | Promoted | `.agents/skills/cp-skill-write-multistage/SKILL.md`; `.claude/skills/cp-skill-write-multistage/SKILL.md` | Fixes a task brief, delegates staged evidence work, invalidates downstream stages when premises change, and defers additional artifacts as explicit handoffs. |
| [`kb/instructions/cp-skill-ground/SKILL.md`](../../instructions/cp-skill-ground/SKILL.md) | Promoted | `.agents/skills/cp-skill-ground/SKILL.md`; `.claude/skills/cp-skill-ground/SKILL.md` | Chooses bounded quotes versus a checksum-verified snapshot from the information needed to judge one claim. |
| [`kb/instructions/cp-skill-revise-iterative/SKILL.md`](../../instructions/cp-skill-revise-iterative/SKILL.md) | Packaged but demoted; explicit invocation only | None | Launches a nested `claude -p` process and relies on a short revision cue plus parent fidelity checks. |
| [`kb/instructions/analyse-agentic-system/SKILL.md`](../../instructions/analyse-agentic-system/SKILL.md) | Source-checkout projection; not promoted by the framework manifest | `.agents/skills/analyse-agentic-system/SKILL.md`; `.claude/skills/analyse-agentic-system/SKILL.md` | Orchestrator fixes boundary, revision, records, and lens depth; lens workers inspect execution-dependent detail and return corrections. |
| [`kb/instructions/roughdraft-review/SKILL.md`](../../instructions/roughdraft-review/SKILL.md) | Repo-local projection | `.agents/skills/roughdraft-review/SKILL.md`; `.claude/skills/roughdraft-review/SKILL.md` | Human review loop with an explicit completion signal. |
| [`kb/instructions/write-agent-memory-system-review/SKILL.md`](../../instructions/write-agent-memory-system-review/SKILL.md) | Repo-local projection | `.agents/skills/write-agent-memory-system-review/SKILL.md`; `.claude/skills/write-agent-memory-system-review/SKILL.md` | Parent prepares a frozen checkout and owns QA, but archives the incumbent before worker availability or replacement success and leaves recursive worker authority open. |
| [`kb/instructions/evaluate-scenarios/SKILL.md`](../../instructions/evaluate-scenarios/SKILL.md) | Source-local, not projected | None | Measures context/fork cost; it does not evaluate whether a planning decision was correct. |

### Projection drift check

Both projection trees contain thirteen symlinks. Every symlink resolves to its
corresponding `kb/instructions/<skill>/` directory; none is broken, copied, or
content-divergent. There is therefore no source/projection drift to repair in
this checkout. Future edits belong only in the canonical sources.

The install test at
[`tests/commonplace/cli/test_init_project.py`](../../../tests/commonplace/cli/test_init_project.py)
checks byte identity for only seven of the ten manifest-promoted skills. It
omits `cp-skill-convert`, `cp-skill-ingest`, and
`cp-skill-revise-autoreason`, even though the implementation projects all
three.

### Directly governing contracts and composition siblings

| Path | Why it governs this audit |
|---|---|
| [`kb/instructions/COLLECTION.md`](../../instructions/COLLECTION.md) | Binding precision, composition, and invocation guidance for every skill and instruction. |
| [`kb/types/instruction.md`](../../types/instruction.md) | Binding instruction structure and the current “fix what the executor cannot determine” rule. |
| [`kb/instructions/draft-ingest-report.md`](../../instructions/draft-ingest-report.md) | Complete ingest-worker brief; fixes worker inputs and denies recursive orchestration. |
| [`kb/instructions/run-review-batches.md`](../../instructions/run-review-batches.md) | Complete review-job orchestration and worker dispatch contract. |
| [`kb/instructions/analyse-external-system-epistemic-architecture.md`](../../instructions/analyse-external-system-epistemic-architecture.md) | Method executed by the agentic-system epistemic lens. |
| [`kb/instructions/assess-a-claim-bearing-artifact-against-external-literature.md`](../../instructions/assess-a-claim-bearing-artifact-against-external-literature.md) | Conditional multistage branch whose bilateral-isolation experiment delegates three independent workers. |
| [`kb/instructions/ingest-paper-with-code.md`](../../instructions/ingest-paper-with-code.md) | Conditional ingest branch with code selection, bounded execution, and ordinary-ingest fallback. |
| [`kb/instructions/re-ingest.md`](../../instructions/re-ingest.md) | Caller that depends on ingest backup, replacement, and restoration semantics. |
| [`kb/sources/types/ingest-report.md`](../../sources/types/ingest-report.md) | Governs the substantive choices left to the ingest drafting worker. |
| [`kb/agent-memory-systems/types/agent-memory-system-review.md`](../../agent-memory-systems/types/agent-memory-system-review.md) | Governs the memory-review worker and contains future-facing `Borrowable Ideas` and `What to Watch` sections. |
| [`kb/reports/types/connect-report.md`](../../reports/types/connect-report.md) | Makes connect output explicitly advisory, regenerable candidate evidence rather than a deferred committed plan. |

## Current behavior by decision surface

| Surface | Fixed before delegation or execution | Left to execution-time judgment | Deferral, probes, and convergence |
|---|---|---|---|
| Instruction contracts | Goal, constraints, done, privileged facts, paths, names, templates, and valid-interpretation choices are fixed. | Anything the executor “can determine from the live system.” | The rule does not yet distinguish live information advantage from mere postponement, and the collection contract generically prefers sub-agent invocation for an `invokes` edge. |
| Ordinary write | Target contract, intended contribution, named sources, and source-use guard. | Candidate wording, authorized links already in hand, and live filename details. | Ambiguous contribution escalates to the user; complex grounding escalates to multistage. One targeted duplicate search is a bounded probe. The target is not written until its source guard passes. |
| Multistage write | `brief.md` fixes question, audience, target, constraints, evidence paths, retained intent, and user-reserved decisions. Parent owns workshop state, invalidation, promotion, and restoration. | Reconstruction, claim architecture, argument skeleton, draft expression, and audit findings, each in a later-informed fresh context. | Stage outputs are explicit evidence gates. Changed premises invalidate dependent work. Missing intent/evidence has a blocker rule; additional artifacts become authorized handoffs that converge through user acceptance, completion, or decline. The exact paragraph plan may be more detailed than the later writer needs. |
| Ingest | Parent fixes source identity, snapshot bytes, checksum, output path, retained quotes, discovery report, worker count, repair count, and acceptance checks. | Worker chooses genre, source role, settled connections, value, limitations, and one next action from the snapshot and current connection context. | Incumbent bytes are verified before dispatch and restored after failure. One replacement worker gets exact failures. This is the strongest current example of preserved option + bounded retry + explicit convergence. |
| Source grounding and snapshotting | Exact source identity, paired file, checksum, adapter route, and output shape. | Minimum sufficient excerpt, metadata judgment from bounded reads, or determination that broad source context is necessary. | Grounding distinguishes `quotes sufficient`, `quotes added`, and `snapshot required`; snapshotting uses bounded inspection and intentionally stops instead of trying an unbounded converter/tool search. |
| AutoReason revision | Parent fixes roles, candidate set, information isolation, hard constraints, evaluator protocol, pass budget, and apply authority. | Critics identify problems, authors choose wording, auditors assess viability, and judges rank blind candidates. | The incumbent remains live as A; no-problem and invalid-candidate probes stop work early; Borda count, two A wins, five passes, or escalation converge the run. Claim-level work is kept outside the prose tournament. |
| Demoted iterative revision | Parent checks fidelity and retains the original. | A nested shell-launched agent receives a compact “revise for flow” task. | Five-pass cap and significance check converge, but the launch bypasses harness worker authority, isolation, and lifecycle controls. |
| Agentic-system analysis | Orchestrator fixes system boundary, revision, source register, canonical IDs, runtime baseline, and warranted lens depth. | Lenses inspect route-specific details, request targeted reads, propose local records, and return corrections. | Thin evidence produces brief rather than absent lenses. Targeted reads and corrections invalidate only affected work. Both lenses always run, but their depth is proportional. |
| Memory-system review | Parent fixes repository identity, checkout, commit, citation format, artifact contract, QA, and publication surfaces. | Worker chooses which implementation files establish the mechanisms, writes the review, and classifies trace learning. | The incumbent is archived before worker-capacity preflight and before the replacement passes. The worker may recursively delegate without a parent-set role or budget. Later QA may change the candidate, but the old live alternative has already been displaced. |
| Review batches | Parent fixes note/criterion pairs, result kind, model partition, grouping, job paths, worker scheduling, and finalization. | Worker performs only the judgment encoded in the generated prompt. | Jobs are transactional and single-use; malformed output advances no baseline. Capacity failure stops or uses an explicitly authorized local fallback. |
| Connect and conversion | Connect fixes a standard search workflow and writes only a regenerable report. Convert fixes a mechanical text-to-note transformation. | A future authorized writer decides whether to author connection candidates; convert leaves traits and tags empty. | Connect candidates are advisory evidence, not planned commitments. Convert incorrectly says `cp-skill-connect` will later assign tags and retains a catalogue of unimplemented conversions with no adoption condition. |
| Health check, validate, scenario evaluation, Roughdraft | These do not delegate substantive judgment. Health check fixes an ordered diagnostic tree; validation reports deterministic state; scenario evaluation measures fork overhead; Roughdraft waits on a human completion event. | Live diagnostic interpretation, measurement, or human comments. | Health checks are bounded probes; Roughdraft has a `Done Reviewing` convergence signal. Scenario evaluation measures bureaucracy cost but not planning quality. |

## Findings and dispositions

### 1. Qualify the global executor-boundary rule

**Disposition: change.**

**Target evidence.** [`kb/types/instruction.md`](../../types/instruction.md)
currently says to leave anything the executor can determine from the live
system to the executor. This is directionally sound but incomplete. It does
not say that the planner may hold cross-task coupling, privileged facts, or
external commitments; nor does it distinguish an execution-dependent decision
from an arbitrary decision merely postponed until execution.

**Mechanism.** Mission tactics supplies the bidirectional information split.
Real options makes deferral conditional on discriminating later information,
continued availability, costly commitment, and delay cost.

**Smallest justified delta.** Replace the single structure bullet with two
compact rules:

- fix intent, constraints, done, privileged facts, arbitrary conventions, and
  coordination boundaries the executor cannot safely reconstruct;
- leave a consequential choice to execution only when live state or evidence
  produced by the run can change it, and name a re-entry/convergence condition
  when it survives beyond the immediate executor decision.

Do not add frontmatter fields or a universal planning checklist. The type rule
should remain short and should link the eventual durable theory note for
rationale.

**Likely validation.** Run `commonplace-validate kb/types/instruction.md`, then
the type- and collection-conformance review pairs for the type spec. Add a
small semantic assay with premature-commitment, justified-deferral, and
unowned-placeholder counterexamples; prose review alone cannot establish that
the new rule changes execution.

### 2. Make delegation selection conditional rather than generically preferred

**Disposition: change.**

**Target evidence.** The `invokes` row in
[`kb/instructions/COLLECTION.md`](../../instructions/COLLECTION.md) says to
prefer sub-agent invocation so context resets. Context isolation is a real
benefit, but this sentence treats it as sufficient to allocate authority and
pay handoff cost.

**Mechanism.** Delegation is justified when the worker has a useful
information position, independence requirement, or bounded parallel role and
the parent can transmit its complementary information. It is not justified by
uncertainty alone. A same-context procedure is better when the decision is
deterministic, cheap, tightly coupled to parent state, or smaller than the
handoff.

**Smallest justified delta.** Keep `invokes` as the link label, but replace the
generic preference with a conditional choice: use a fresh worker when
isolation, later-acquired evidence, or parallel independence creates a concrete
advantage; otherwise invoke in the current context. Require the caller, not the
callee, to retain the goal, coordination boundary, and acceptance authority.

**Likely validation.** Validate the collection contract and run its
collection-conformance pair. Re-run `evaluate-scenarios` after edits to expose
added or removed fork cost. Do not judge success from lower bytes alone.

### 3. Make recursive delegation an explicit authority boundary

**Disposition: change.**

**Target evidence.** Ingest's worker brief and `draft-ingest-report.md`
explicitly prohibit another agent. The generated review-job prompt similarly
owns one isolated output. In contrast:

- the memory-review worker may spawn further agents if a harness tool is
  available, but receives no nested role, budget, output, or convergence rule;
- multistage writer roles and AutoReason actor prompts do not state whether
  their single-use workers may delegate again;
- agentic-system lens workers are subordinate to one canonical register, but
  their nested authority is implicit.

Spawning another worker changes resource use, information flow, write
ownership, and coordination. It is not merely a choice of local means.

**Smallest justified delta.** Add one default to
`kb/types/instruction.md`: a delegated work packet states whether nested
delegation is authorized; silence means no. Then:

- change the memory-review dispatch to `Do not spawn further agents`;
- add the same boundary to multistage, AutoReason, bilateral-isolation, and
  agentic-lens worker packets;
- authorize nested delegation only in a future workflow that also fixes its
  purpose, maximum scope or budget, writes, return protocol, and escalation.

The worker should still choose tools, reads, ordering, and prose from live
state inside its assigned role.

**Likely validation.** Add a static contract test over delegation-heavy
worker packets. It should assert an explicit nested-delegation value, not a
particular phrase. Retain the existing review-worker one-prompt test and add
negative fixtures where a worker recursively launches an orchestration skill.

### 4. Preserve the incumbent memory review until a replacement converges

**Disposition: change.**

**Target evidence.** `write-agent-memory-system-review` archives and edits the
incumbent in Step 7. Only Step 8 checks whether a fresh worker is available.
The worker then writes directly to the live `note_path`; taxonomy QA, semantic
QA, and final validation happen later. A capacity failure can therefore leave
the current review archived without any candidate, and a later failure has no
specified restoration branch.

**Real-options test.** This is a load-bearing application, not an analogy:

1. Early archiving displaces the current live alternative and substantively
   mutates the archived copy's tags, attestation, and banner.
2. Worker completion and QA can change whether the replacement should land.
3. The opportunity to archive remains available after the candidate passes.
4. There is no material benefit identified for archiving before dispatch.

All four conditions favor waiting. The ingest workflow already demonstrates
the local pattern: preserve verified incumbent bytes, bound repair, accept only
after checks, and restore after failure.

**Smallest justified delta.** Move worker-capacity preflight before any
incumbent mutation. Draft a candidate under a target-compatible workshop
staging path, or at minimum retain and verify a byte-exact backup with a
specified restoration branch. Archive the incumbent and promote the candidate
only after worker validation, taxonomy QA, semantic QA disposition, and final
target validation can complete as one promotion sequence. Keep the worker
blind to the incumbent by an explicit read exclusion; early archival is not
required for epistemic independence.

**Likely validation.** Add failure-path tests or executable fixtures for:
no worker slot, worker returns no file, worker validation failure, semantic-QA
blocker, promotion failure, and same-day archive collision. Each must leave the
incumbent byte-identical and at its original path. A success fixture must
create exactly one archive and one validated current review.

### 5. Remove unowned future decisions from conversion

**Disposition: change.**

**Target evidence.** `cp-skill-convert` says tag assignment is done later by
`cp-skill-connect` or a human, but connect is discovery-only and has no
authority to edit tags. The skill also carries five “Future conversions” as
directions despite having no trigger evidence, owner, experiment, or adoption
boundary.

**Mechanism.** A deferred choice needs a capable later actor and a way back
into the decision. A speculative feature list with neither is omission
presented as flexibility. The repository's YAGNI rule already supplies the
proper route: record a recurring design gap in a proposal when it becomes
real.

**Smallest justified delta.** State that traits and tags remain empty until a
separately authorized semantic editing task assigns them; explicitly say that
connect only reports candidate links. Remove the unimplemented conversion
catalogue and retain one unsupported-conversion stop that points to a proposal
only when the requested need warrants one.

**Likely validation.** Extend
`tests/commonplace/docs/test_type_contract_integrity.py` to reject wording that
assigns tag mutation to connect. Validate the skill and run the current
text-promotion contract tests.

### 6. Turn review “watch” items into observations, not latent plans

**Disposition: change.**

**Target evidence.** The memory-review type asks whether each borrowable idea
is “ready now or needs a concrete use case first” and asks `What to Watch` for
a pending change plus its design consequence. The first names a broad
information need without saying what evidence would discriminate; the second
names a signpost but not whether any action is actually planned.

**Mechanism.** DAPP distinguishes a monitored signpost from a trigger, and
real options requires later information capable of changing a decision. A
review should not silently create an adaptation plan.

**Smallest justified delta.** For a not-ready borrowable idea, require the
specific missing use case or observation that could change readiness, or omit
the idea. For `What to Watch`, require an observable pending event and its
decision consequence; add a response threshold only when a separate adopted
plan actually commits to one. Keep both sections advisory.

**Likely validation.** Validate the type spec and representative reviews. Use
a semantic conformance case that rejects “needs a use case” without naming the
missing discriminating condition, but do not add schema fields for signposts
or triggers.

### 7. Retire or migrate the shell-launched iterative revision path

**Disposition: change.**

**Target evidence.** The demoted `cp-skill-revise-iterative` remains an
operative explicit-invocation instruction and launches `claude -p` from the
shell. It cannot use the parent harness's worker slots, context-isolation
contract, lifecycle close, or execution metadata. Its short “revise for flow”
cue leaves the revision mechanism largely weight-resident; the parent only
checks the result after the work has run.

**Mechanism.** Intent-framed delegation requires a real authority and feedback
regime. Demotion reduces exposure but does not make the remaining execution
path well-governed.

**Smallest justified delta.** Prefer retirement: replace the operative body
with a short explicit pointer to `cp-skill-revise-autoreason` or ordinary
human-reviewed editing. If a distinct iterative path is still needed, migrate
it to a harness worker with an exact work packet, no recursive delegation,
bounded output path, and the existing fidelity/application gates. Do not keep
the shell agent launch as a fallback.

**Likely validation.** Add a repository test rejecting `claude -p`, `codex
exec`, and equivalent agent-CLI launches in active instruction and skill
sources. If the directory is retired or removed, update its packaging entry
and the AutoReason cross-reference, then run init/scaffold tests.

### 8. Keep the current context-specific probe and convergence mechanisms

**Disposition: deliberate non-change.**

Several skills already operationalize the report without extra planning
fields:

- `cp-skill-ground` reads only enough source context to choose bounded quotes
  versus the verified-snapshot route;
- snapshotting inspects bounded metadata and stops rather than exploring an
  unbounded converter set;
- health-check orders cheap diagnostic observations before recommending a
  repair;
- the literature-disposition instruction makes bilateral isolation
  conditional on an explicit independence question or experiment, rather than
  universalizing one observed result;
- the paper-with-code branch permits only a cheap existing test in a ready
  environment and otherwise records static-inspection limits;
- AutoReason uses the critic and post-candidate auditor as early probes before
  paying for blind judging;
- agentic-system analysis runs a baseline and then scales each mandatory lens
  to its trigger evidence.

Do not add a generic `probe:` field or require every workflow to enumerate
wait/act/test branches. A probe is warranted only when it can cheaply produce
decision-relevant evidence without committing the whole course.

### 9. Keep the strong parent/worker splits in ingest, review batches, and agentic analysis

**Disposition: deliberate non-change.**

These workflows correctly fix planner-owned facts and leave live judgment to
the worker:

- ingest fixes immutable identity, bytes, paths, isolation, and acceptance;
  the worker interprets the source and KB connection context;
- review batching fixes persisted pair protocol, model partition, and output
  transaction; the worker performs only the criterion judgment;
- agentic analysis fixes the boundary, revision, shared IDs, and ownership;
  lenses choose route-specific reads and return evidence-bound corrections.

The fixed detail is justified by identity, coordination, or transaction
semantics. It is not premature commitment to execution-time means. Preserve
the local-fallback authorization stops and ingest's incumbent restoration.

### 10. Keep AutoReason experimental; do not generalize its tournament

**Disposition: experiment.**

AutoReason is the clearest set-based workflow in the skill set: A remains a
first-class option, B and AB are evaluable alternatives, the critic and auditor
can eliminate work early, blind judges provide a declared evaluation surface,
and the run converges through a cap, incumbent-win streak, semantic guard, and
human apply decision. It also discloses its carrying cost: normally seven fresh
agents per pass.

No current evidence shows that this cost improves ordinary note revision. Keep
the experimental label and explicit invocation. Before promotion as a default,
compare it with a single-worker and ordinary-editor baseline on semantic
fidelity, accepted editorial gain, calls/tokens, wall time, and rate of “keep
A.” Do not infer benefit from the sophistication of the tournament.

### 11. Test whether the multistage skeleton fixes too much detail

**Disposition: experiment.**

The multistage admission gate already prevents settled local edits from paying
the full workflow cost. Its claim skeleton is valuable as an audit baseline,
but requiring the work of every section or paragraph before the writer runs
may freeze organization that the later-informed writer can safely choose.

Compare the current paragraph-grain skeleton with a claim-and-inference-grain
skeleton that fixes assertions, evidence, scope, and required inferential
moves while leaving paragraph grouping and local order to the writer. Measure
unsupported commitments, audit findings, semantic drift, accepted prose
quality, and context/call cost. Change the skill only if the coarser skeleton
preserves the audit advantage. This is not a reason to remove reconstruction,
claim disposition, or downstream invalidation.

### 12. Add a behavioral planning assay before broad instruction rollout

**Disposition: experiment.**

Deterministic validation can check fields, paths, result literals, and output
protocols. It cannot tell justified deferral from omission. The research
report explicitly lacks target-side effectiveness evidence.

Run a bounded prompt-level assay against the current and proposed instruction
contract. At minimum include cases where:

1. the parent has a global constraint the worker cannot reconstruct;
2. a tool result available only during execution should decide the means;
3. a reversible low-cost choice has no later discriminating observation, so
   waiting has no option value;
4. later evidence would discriminate, but the opportunity expires first;
5. a cheap bounded probe can resolve the choice before full commitment;
6. a coarse future item has a signpost/replanning point and convergence rule;
7. a superficially similar item is only an unowned placeholder; and
8. a worker tries to create another worker without delegated authority.

Score whether the plan transmits parent-only information, places the remaining
decision at the informed stage, applies all four real-options conditions,
selects a probe only when informative, and converges. Include a no-extra-plan
baseline so success cannot be bought by indiscriminate verbosity.

### 13. Close the promoted-skill projection test gap

**Disposition: change.**

Change `test_init_project_installs_skills_as_copies` to derive the expected set
from `MANIFEST.promoted_skills` rather than repeating a partial tuple. This is
not a theory change, but it is the cheapest check that every operative skill
change reaches both installed runtime surfaces byte-for-byte. Keep the test
that preserves an intentionally divergent installed copy.

## Ordering and dependencies

1. Promote the durable planning theory, or at least settle the exact wording
   of its decision-placement and productive-deferral claims. The operative
   contracts should link durable theory rather than this workshop.
2. Change `kb/types/instruction.md` and the `invokes` guidance in
   `kb/instructions/COLLECTION.md`. These are the shared selection and dispatch
   rules; skill-local edits should use one settled vocabulary.
3. Apply the explicit nested-delegation boundary to all worker packets in one
   composition-aware sweep. Read each direct caller/callee again before
   editing; do not change result literals or output ownership accidentally.
4. Repair `write-agent-memory-system-review` promotion ordering and failure
   recovery. Its archive, worker, review-batch, type-contract, and index
   interfaces must move together.
5. Correct the small unowned deferrals in convert and the memory-review type;
   retire or migrate iterative revision.
6. Close the manifest-derived projection test gap and add worker-authority and
   agent-CLI static tests.
7. Run the behavioral planning assay and the multistage skeleton experiment.
   Do not broaden the machinery until results discriminate.
8. Re-run scenario overhead measurement after the final instruction text is
   known. Use it as a cost guard, not a quality oracle.

No current recommendation requires a schema or runtime-code change. If the
memory-review candidate-staging change cannot be represented safely with the
existing workshop/type/validation rules, stop that implementation and write a
design proposal for the missing staging transaction rather than adding an ad
hoc status field.

## Validation matrix for a later implementation pass

| Change class | Minimum checks |
|---|---|
| Shared instruction/type wording | `commonplace-validate` on each changed artifact; type and collection conformance review pairs; behavioral planning assay. |
| Promoted skill text | Validate canonical `SKILL.md`; run `uv run pytest tests/commonplace/cli/test_init_project.py`; initialize a temporary project and verify both runtime copies match every manifest-promoted source. Never edit projections directly. |
| Worker dispatch changes | Existing `tests/commonplace/docs/test_review_worker_contract.py`; new explicit nested-authority contract tests; negative recursive-orchestration cases. |
| Convert wording | `uv run pytest tests/commonplace/docs/test_type_contract_integrity.py`; validate convert and connect skill sources. |
| Memory-review staging | Failure-path fixtures for capacity, no output, invalid output, semantic block, promotion failure, restoration, and successful single archive; validate candidate and final review. |
| Iterative-revision retirement | Static no-agent-CLI test; packaging/init tests if the directory or force-include list changes. |
| Multistage/AutoReason experiments | Predeclared comparison cases, blind outcome review where feasible, semantic-fidelity checks, call/token/wall-time accounting, and incumbent-retention checks. |
| Prompt-size effects | `evaluate-scenarios` with live byte measurements, reported separately from behavioral quality. |

## Anti-bureaucracy guard

Do not paste the nine machinery obligations from the research report into every
skill. In particular:

- do not require a plan file for one-step, reversible, low-coupling work;
- do not require a replanning horizon when the executor will make the choice
  immediately from live state;
- do not maintain multiple alternatives without a credible evaluation surface
  and convergence boundary;
- do not add signpost, trigger, option, delay-cost, or probe fields to general
  artifact schemas;
- do not turn advisory candidates in connect reports or system reviews into
  implicit commitments;
- do not delegate merely to create a clean context when the handoff loses more
  information than it isolates;
- do not use a bare “Auftragstaktik,” “mission tactics,” “rolling wave,” “real
  options,” or “set-based” cue as an operative shortcut.

No current skill relies on a bare planning-methodology name for its mechanism.
AutoReason uses a compact name, but the complete candidate, critic, audit,
judge, aggregation, fallback, and stop rules are written out; the name is not
load-bearing. Preserve that posture. If mission tactics enters an operative
surface, use the explicit gloss “preserve intent and constraints; delegate
execution-time choice of means” and state the surrounding authority,
information, feedback, and recovery regime.
