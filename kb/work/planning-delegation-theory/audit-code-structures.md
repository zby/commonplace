# Planning and delegation: code and structure audit

This audit maps the source-grounded obligations in
[`research-report.md`](./research-report.md) to the behavior Commonplace
actually ships. It covers the Python package, operational store, type and
schema system, validators, workflow instructions, tests, generated structures,
and command/harness boundary. It does not assume that Commonplace is an agent
runtime.

## Executive findings

1. **There is no persisted generic plan consumer.** Commonplace has no planner,
   model launcher, scheduler, lease manager, background trigger monitor, or
   general delegation API. The package exposes deterministic commands; parent
   agents use harness-native workers under instructions.
2. **Two persisted objects are plan-like but deliberately narrow.**
   `ReviewJobPlan` projects queued review pairs and derived artifact paths from
   SQLite. `FullPassReport` is a guarded state packet for one note-improvement
   workflow. Neither represents or consumes general intent, constraints,
   deferred choices, options, probes, triggers, or delegation authority.
3. **The strongest current pattern is workflow-specific control.** Exact inputs,
   immutable captures, bounded retries, deterministic output checks, and
   explicit hand-back are encoded only where a real workflow consumes them.
   This is a better precedent than adding generic planning fields with no
   executor.
4. **The immediate transfer belongs mainly in authored instruction contracts.**
   Commonplace can refine the existing instruction type and the multistage
   brief so consequential deferral is distinguished from omission and worker
   handoffs state the control regime. Semantic sufficiency must remain model or
   user judgment.
5. **A few already-repeated checks can move into code.** The review selector's
   emitted protocol version is not checked by its consumer, and several ingest
   handoff invariants are mechanically checkable from the report and its
   checksum-verified snapshot. These are bounded changes to existing consumers,
   not a reason to build a generic planner.
6. **Behavioral evidence is missing.** `tests/scenarios/` measures context bytes
   and hops, not planning quality. Before codifying option, probe, or convergence
   policy, Commonplace should compare the explicit transfer gloss against its
   current instructions on controlled planning cases.

## Evidence and attribution boundary

The research report supplies source theory; the recommendations below are
target-side Commonplace engineering judgments. The source-backed transfer used
here is:

- preserve stable intent and constraints while delegating execution-time means;
- add detail as information becomes available;
- defer a costly-to-reverse choice only when later evidence can change it, the
  option remains available, and delay is worth its cost;
- distinguish a bounded information-producing probe from passive waiting and
  full commitment;
- make adaptation observable through a signpost or observation, threshold, and
  sufficient lead time; and
- preserve multiple feasible alternatives only with an evaluation surface and
  an explicit convergence boundary.

The set-based formulation is supported here by the later Kennedy, Sobek, and
Kennedy paper recorded in
[`kennedy-sobek-kennedy-set-based-rework.ingest.md`](../../sources/kennedy-sobek-kennedy-set-based-rework.ingest.md).
It substitutes for the inaccessible image-only Sobek, Ward, and Liker (1999)
text. That substitution supports the preserve/test/converge mechanism but not
direct attribution of the 1999 article's canonical three-principle wording.
No Commonplace field name, checklist, or implementation recommendation below
should be presented as the 1999 formulation. The combined theory also has no
current empirical evidence of improving LLM-agent outcomes.

## What Commonplace actually implements

### Package and harness boundary

`pyproject.toml` registers deterministic `commonplace-*` entry points for
validation, snapshots, relocation, freshness, and review bookkeeping. The
package dependencies and `src/commonplace/` contain no model SDK, model-call
adapter, planner, scheduler, or general worker-dispatch implementation.

The operative worker boundary is textual:

- [`run-review-batches.md`](../../instructions/run-review-batches.md) assigns
  selection, job creation, dispatch, finalization, and verification to the
  parent and judgment to fresh workers.
- [`draft-ingest-report.md`](../../instructions/draft-ingest-report.md) accepts a
  fixed input bundle and permits one output.
- [`cp-skill-write-multistage/SKILL.md`](../../instructions/cp-skill-write-multistage/SKILL.md)
  and
  [`cp-skill-revise-autoreason/SKILL.md`](../../instructions/cp-skill-revise-autoreason/SKILL.md)
  tell the parent how to create and close fresh workers.

ADR 035 explicitly rejects a package-owned scheduler because concurrency,
budgets, retries, and model calls belong to the harness. ADR 067 makes a
generated prompt the review worker's sole job-specific contract. Those are
current architectural constraints, not gaps to reverse incidentally.

### Review selection and jobs

The review pipeline is the only shipped surface that uses an object named a
plan:

- `src/commonplace/review/review_target_selector.py::StaleCriterion` and
  `render_json()` emit target paths, reasons, changed inputs, optional baseline
  revision, result kind, and `schema = commonplace-review-targets/2`.
- `src/commonplace/cli/review/create_review_jobs.py::_selector_pairs()` consumes
  only model partition, target/criterion identity, and result kind. It ignores
  `schema`, `reasons`, `changed_inputs`, and `baseline_revision`; it then
  rechecks path existence, criterion identity, result kind, applicability, and
  duplicates.
- `_note_groups()`, `_criterion_groups()`, `_chunks()`, and `_group_pairs()`
  implement fixed packing. Criterion packing defaults to five notes. There is
  no cost-aware or adaptive sharder.
- `src/commonplace/review/batch.py::prepare_grouped_review_job()` captures exact
  note and criterion snapshots, creates DB rows, derives artifact paths, and
  renders the prompt.
- `src/commonplace/review/review_db.py::ReviewJobPlan` is a read model over one
  `review_jobs` row, ordered `review_pairs`, and paths derived from the job id.
  `create_job_with_pairs()`, `load_review_job_plan()`, and
  `list_review_job_plans()` are its persistence boundary.
- `src/commonplace/review/protocol/prompt.py::render_pairs_prompt()` embeds the
  captured notes and criteria, permitted reading scope, exact output path,
  isolation rules, and result protocol. Judgment-bearing requirements live in
  hashed criterion text, not the mechanical prompt wrapper.
- `src/commonplace/review/finalization.py::finalize_review_job_from_owned_output()`
  requires exact pair coverage and result-kind grammar, writes evidence, and
  advances freshness all-or-nothing.

The SQLite shape in `src/commonplace/store-schema.sql` is intentionally small.
`review_jobs.status` is only `queued | completed | failed`; there is no running
state, lease, owner, heartbeat, retry counter, deadline, trigger, or escalation
field. `review_pairs.expected_baseline_revision` and
`expected_generation_next_revision`, enforced through
`src/commonplace/freshness/baselines.py`, provide compare-and-swap protection
against stale finalization. That is real state convergence, but only for a
review pair's accepted freshness baseline.

`src/commonplace/review/telemetry.py` records deterministic link availability
and soft worker-reported consumption. The prompt permits `stop_reason = budget`
or `sufficiency`, but no budget value is supplied or enforced. The offline
`scripts/review_link_consumption.py` summarizes observations; it does not feed
them back into grouping, dispatch, or retry policy.

Relevant existing tests include:

- `tests/commonplace/review/test_review_batch.py::test_finalize_review_job_fails_partial_output_without_salvage`;
- `tests/commonplace/review/test_review_store.py::test_job_cannot_complete_until_every_pair_completes`;
- `tests/commonplace/freshness/test_transitions.py::test_upsert_observation_rejects_mismatched_expected_revision`;
- `tests/commonplace/review/test_review_jobs_live_and_direct.py::test_create_review_jobs_selector_criterion_grouping_chunks_and_lists`; and
- `tests/commonplace/docs/test_review_worker_contract.py::test_review_worker_dispatch_requires_fresh_context_and_only_the_prompt_path`.

**Finding:** the selector JSON is a disposable target list and `ReviewJobPlan`
is an execution manifest for a fixed assay. Neither is a general intent-bearing
plan. Persisting selector rationales in review jobs would not make them so, and
would duplicate diagnostics that do not affect review judgment.

### Full-improvement pass state

The closest implemented precedent for a persisted workflow state machine is the
full-pass packet:

- [`full-pass-report.schema.yaml`](../../reports/types/full-pass-report.schema.yaml)
  constrains `phase`, `closing_status`, `closing_repair_attempted`, disposition,
  captures, resolution, authority, and allowed conditional combinations.
- `src/commonplace/lib/full_pass.py::FullPassReport`,
  `parse_full_pass_report()`, and `guard_full_pass_report()` parse the packet and
  compare current files with immutable captured bytes.
- `src/commonplace/lib/validation.py::validate_full_pass_report()` verifies
  capture hashes and the canonical rendered resolution projection.
- `commonplace-guard-full-pass-report` is a parent-invoked pre-transition guard.

The state machine admits one bounded closing repair, then either readiness or
hand-back. User authority controls destructive or alternative dispositions; a
version guard can mark a packet superseded. Tests in
`tests/commonplace/test_full_pass_validation.py`,
`tests/commonplace/lib/test_full_pass.py`, and
`tests/commonplace/cli/test_guard_full_pass_report.py` cover illegal state
combinations, capture corruption, version drift, the one-repair boundary, and
hand-back.

**Finding:** this is evidence that schema plus a workflow-specific parser and
guard can enforce state safely. It is not a generic plan consumer: the parent
still interprets and performs transitions under
[`run-full-improvement-pass-on-note.md`](../../instructions/run-full-improvement-pass-on-note.md),
and the fields are specific to one note-improvement transaction.

### Task and workshop artifacts

The apparent plan types under `kb/tasks/types/` are not an implemented plan
system:

- [`task-active.md`](../../tasks/types/task-active.md),
  [`task-backlog.md`](../../tasks/types/task-backlog.md), and
  [`task-recurring.md`](../../tasks/types/task-recurring.md) all declare
  `schema: null`.
- The active template has Goal, Prerequisites, Decision Record, Tasks, and
  Current State; the backlog template has Why Not Now and Trigger to Activate.
  These are prose resume aids with no parser or transition consumer.
- `src/commonplace/scaffold_manifest.py::MANIFEST` creates the task lifecycle
  directories but does not ship `kb/tasks/types/` into installed projects.
- `tests/commonplace/lib/test_type_resolver.py::test_schema_null_skips_schema_validation`
  confirms that schema-null types receive no schema validation.

The multistage writer has richer manual state. Its workshop `README.md`
checklist, `brief.md`, reconstruction, disposition, skeleton, audit, and
candidate files are consumed by the parent instruction. It fixes governing
intent and user-reserved decisions, invalidates downstream stages after an
upstream change, and stops for missing authority. It deliberately has no stage
frontmatter and no parser. This makes it the best existing place to test richer
planning language, but not evidence for a generic plan schema.

### Delegated ingest and experimental AutoReason

The ingest workflow already demonstrates intent-preserving delegation:

- the parent resolves the target, immutable snapshot checksum, connection
  report, exact retained Quotes block, output path, and repair policy;
- the fresh drafting worker chooses analysis and prose within those fixed
  inputs;
- the parent verifies the handoff and permits at most one fresh replacement;
  and
- a failed refresh restores a checksum-verified incumbent.

The ingest type schema and
`src/commonplace/lib/validation.py::validate_ingest_snapshot_pairing()` and
`validate_ingest_quotes()` already enforce much of the durable artifact
contract. The parent still manually checks capture-metadata projection, Quotes
adjacency and byte preservation, forbidden snapshot/connect-report references,
and code-grounding parity. Some of those checks are deterministic and repeated
on both primary and replacement attempts.

AutoReason is explicitly experimental. Its instruction hard-codes at most five
passes, fresh role workers, three parallel blind judges, Borda aggregation,
conservative ties, two consecutive incumbent wins as convergence, bounded role
reruns, and a claim-revision sidecar as escalation. Its state, ranking parser,
and retry accounting live in prose and files; no package consumer enforces
them. That is appropriate while the workflow is an experiment, but means a
partially executed bundle cannot be treated as machine-verified state.

### Generated and bulk structures

The generated surfaces are specialized derivations, not plan execution:

- `src/commonplace/lib/index_generated.py::generated_section_for_index()` and
  `src/commonplace/lib/index_directory.py::collect_index_pages()` build
  deterministic in-memory publication pages. They do not persist intentions or
  schedule work.
- `src/commonplace/lib/systems_matrix.py::parse_review_text()` and
  `scripts/build_systems_matrix.py` parse controlled review tokens, preserve
  hand-classified columns through an identity join, flag omissions rather than
  guess, and regenerate `kb/agent-memory-systems/systems.csv`. This is an
  implicit document-set implementation for one domain.
- `src/commonplace/lib/relocation.py::relocate_note()` and
  `relocate_directory()` compute an in-memory move/update map for dry-run or
  immediate apply. Apply recomputes from live files; no persisted, version-bound
  move plan is later consumed.
- [`bulk-operations/README.md`](../bulk-operations/README.md) and
  [`generative-bulk-operations.md`](../bulk-operations/generative-bulk-operations.md)
  describe select/classify/shard/execute/integrate/validate/close and a possible
  document-set spec. They are workshop theory, not shipped orchestration. The
  document-set spec remains an explicit prerequisite and open design choice.

`tests/scenarios/*.md` plus
[`evaluate-scenarios/SKILL.md`](../../instructions/evaluate-scenarios/SKILL.md)
measure per-fork instruction bytes and hops. They can measure the context cost
of a planning-contract change, but not whether an agent placed decisions,
selected a useful probe, or converged correctly.

## Can current machinery enforce the research obligations?

| Obligation | Current enforcement | Deterministic boundary | Judgment boundary | Disposition |
|---|---|---|---|---|
| Separate fixed intent/constraints from deferred choices | Multistage `brief.md` records intent, constraints, uncertainty, and user-reserved decisions, but not this explicit classification | A future consumed plan type could require the categories and unique decision IDs | Whether a fact is stable, privileged, consequential, or execution-dependent | **change** the instruction contract; no generic schema yet |
| Explain consequential deferral | Blockers and decision markers exist, but ordinary coarse items need no reason | Schema could require a non-empty reason for an explicitly deferred record | Whether later information can actually change the decision | **change** multistage brief/skeleton guidance; **experiment** before broader rollout |
| Record preserved option and delay/reversal cost | No current field or consumer | Presence and allowed qualitative shape could be checked after a real plan type exists | Identifying the real option and comparing delay with commitment cost | **experiment**; do not encode financial valuation |
| Consider a bounded probe separately from waiting and commitment | No generic representation; workflow-specific validation/review steps sometimes act as probes | A plan consumer could require a probe output, budget, and follow-up decision point | Whether the probe is cheap, discriminating, and safe | **experiment**, then workflow-specific instruction if useful |
| Give every coarse item a horizon, evidence condition, trigger, convergence rule, or delegated authority | AutoReason and full-pass have fixed convergence; backlog tasks have unvalidated activation prose | Conditional schema can require at least one control form; a guard can reject an expired or unresolved item at a named checkpoint | Choosing the appropriate control form and a credible boundary | **proposal** only with a named consumer |
| Define trigger observation, threshold, and lead time | Backlog tasks have only free-text Trigger to Activate; no monitor exists | Shape can be validated; a checkpoint consumer can compare an observed value with a typed threshold | Selecting a valid signpost and enough lead time | **proposal**; external automation owns background monitoring |
| Carry alternatives only with evaluation and convergence | AutoReason has one hard-coded candidate set and Borda convergence; set-level generator work is domain-specific | Candidate IDs, test outputs, elimination status, and latest checkpoint can be checked | Whether candidates are genuinely different, tests discriminate, and carrying cost is justified | keep AutoReason as **experiment**; generic support is a **proposal** |
| Delegation states intent, constraints, authority, context/resources, coordination, feedback, escalation/recovery | Ingest and review prompts cover most fields; multistage roles are bounded but the shared instruction type does not name the complete contract | Prompt builders can require exact paths, output ownership, result protocol, retry limits, and guard state | Sufficiency of intent/context, safe authority, useful feedback, and when escalation is warranted | **change** the shared instruction authoring contract and selected workflows |
| Use methodology names only with demonstrated activation fidelity or an explicit gloss | No activation-fidelity assay; current instruction type links the executor-boundary note | A lint rule could only find words, not establish activation | Whether a compact cue activates the intended mechanism | use the explicit gloss in instructions; **experiment** with compact cues; no lint |

## Recommended changes and experiments

### 1. Refine the consumed instruction contract

**Disposition: change.** The smallest operative surface is
[`kb/types/instruction.md`](../../types/instruction.md), especially `## Structure`,
plus the `Step 3 - Write The Brief` and claim-skeleton requirements in the
multistage writer. These texts already have consumers: instruction authors,
type-conformance reviewers, and the multistage parent.

Add the explicit transfer gloss, not a methodology label: preserve intent and
constraints; delegate execution-time choice of means. For instructions that
delegate consequential work, require the author to make clear:

- goal and done condition;
- constraints and authority boundary;
- fixed paths, facts, conventions, and accessible context/resources;
- choices intentionally left to the executor;
- coordination or output ownership;
- feedback/checkpoint surface; and
- recovery or escalation condition.

For a consequential choice intentionally deferred in a multistage brief or
skeleton, require a reason later information can help and one convergence form:
replanning horizon, evidence condition, trigger, bounded delegated authority,
or explicit user decision. Ask for an option/reversal and delay-cost comparison
only when commitment is materially costly; do not turn every prose task into a
planning worksheet.

**Verification:** run `commonplace-validate` on changed Markdown, then run
type-conformance review on a small sample of worker-bearing instructions. Use
the behavioral experiment below to test whether the change improves decision
placement. A source-string unit test would only freeze wording and should not be
added.

**Dependencies and YAGNI boundary:** promote or otherwise make the underlying
theory citable before presenting it as established Commonplace methodology.
Do not add frontmatter fields, a plan database, or the full checklist to
`AGENTS.md.template`; the always-loaded control plane would charge every task
for a method needed only by planning/delegation workflows.

### 2. Enforce the existing review-selector protocol version

**Disposition: change.** `review_target_selector.render_json()` emits
`commonplace-review-targets/2`, but
`create_review_jobs._selector_pairs()` accepts missing or arbitrary `schema`.
The smallest fix is to centralize/import `SELECTOR_SCHEMA` and reject a missing
or unequal version before targets are read.

**Tests:** extend
`tests/commonplace/review/test_review_jobs_live_and_direct.py::test_create_review_jobs_accepts_selector_json_file_and_validates_model`
with accepted-current, missing-version, and wrong-version cases; update helper
fixtures to emit the current schema. Keep existing path, criterion identity,
applicability, grouping, and CAS tests.

**Dependencies and YAGNI boundary:** no SQLite migration and no persistence of
selector reasons or diffs. Job creation already recaptures live inputs and CAS
state; selection diagnostics should not become execution identity without a
separate demonstrated consumer.

### 3. Move inferable ingest handoff checks into validation

**Disposition: change.** Extend the existing ingest validation path rather than
create a planning subsystem. When the name-paired snapshot exists and matches
`snapshot_sha256`, code can compare the ingest's projected capture metadata
with `src/commonplace/lib/snapshot.py::ingest_metadata_from_snapshot()`. A
focused type rule can also check that the single Quotes section immediately
precedes `## Connections Found` and reject local Markdown links into
`.snapshots/` or generated connect reports.

**Tests:** add cases beside the ingest fixtures in
`tests/commonplace/cli/test_validate_notes.py` for metadata drift, Quotes
misordering, and forbidden local targets; retain
`tests/commonplace/lib/test_snapshot.py::test_ingest_metadata_projects_capture_fields_and_excludes_snapshot_fields`
and the existing pairing/quote-resolution coverage.

**Dependencies and YAGNI boundary:** snapshot absence must remain silent where
the current ignored-cache contract requires it. Validation cannot reconstruct
the opaque `retained_quotes` input or prove it is byte-identical to a prior
ingest; the parent must retain that comparison unless a real handoff manifest
is introduced after observed failures. Do not add locks, CAS, crash recovery,
or a generic delegation record to ingest; its instruction explicitly excludes
those semantics.

### 4. Run a planning-placement experiment before adding policy code

**Disposition: experiment.** Build a small, fixed set of planning tasks that
separately exercise:

- a cheap reversible decision that should be made now;
- a costly-to-reverse decision with a later discriminating observation;
- a proposed deferral where no evidence will arrive;
- a cheap bounded probe that dominates passive waiting;
- a recurring condition expressible as observation, threshold, and lead time;
- multiple alternatives with and without a credible evaluation surface; and
- complementary planner/executor information, including one privileged
  upstream fact the executor cannot recover.

Compare at least: current instruction language, a methodology name alone, the
explicit transfer gloss, and the gloss plus the minimum deferral/convergence
questions. Blind-score decision placement, preserved intent, omission versus
productive deferral, probe selection, convergence, and escalation. Record
context cost separately.

**Tests and dependencies:** this is an empirical workshop, not a pytest unit
test. `tests/scenarios/` may measure the byte/hop cost of a winning instruction
variant, but cannot supply the quality verdict. Do not promote a compact name
as a sufficient cue or add trigger/option policy to code until this assay shows
stable activation across task shapes.

### 5. Use review telemetry to test batching, not to control it yet

**Disposition: experiment.** The existing availability and consumption records
can compare note-packed versus criterion-packed jobs and different batch sizes.
Measure malformed/partial outputs, `budget` stops, consumed/offered bytes,
outcomes, and rerun rates. Only after a stable relation appears should a
deterministic recommendation or cap replace the current default of five.

**Tests and YAGNI boundary:** keep `src/commonplace/review/telemetry.py` soft and
offline during the experiment. Self-reported consumption is not a reliable
runtime trigger, and no current scheduler can act on it. Do not add adaptive
dispatch, automatic retries, or budget fields to `review_jobs` on current
evidence.

### 6. Require a design proposal before any generic persisted plan

**Disposition: proposal.** A generic plan artifact is justified only when at
least two recurring workflows need the same cross-run state and a concrete
consumer will load it before dispatch and at convergence checkpoints. The
proposal must choose one authority: a parent-invoked workflow guard, a package
command, or an external harness integration. Merely persisting prose does not
make a plan operative.

If that trigger is met, the smallest candidate surface is one operational type
and schema, one parser/type rule for cross-reference checks, and one
parent-invoked guard. The layers should divide responsibility as follows:

| Layer | Justified enforcement |
|---|---|
| JSON Schema | required categories, enums, conditional shape, non-empty fields, and trigger subfields (`observation`, `threshold`, `lead_time`) |
| `@type_rule` / parser | unique IDs, reference resolution, dependency cycles, path and capture/hash relationships, and mutually consistent state |
| workflow guard | legal transitions, retry/repair limits, named checkpoint or latest-decision boundary, guarded live versions, and escalation when a deterministic boundary is crossed |
| criterion/instruction/model | whether intent is adequate, a choice is consequential, evidence discriminates, costs justify deferral, alternatives are feasible, and delegated authority is safe |
| user | goals, destructive authority, unresolved value trade-offs, and expansion beyond the accepted task |

The proposal should not preselect Markdown frontmatter versus SQLite, and it
should not reuse `ReviewJobPlan` merely because of its name. It should also
resolve the document-set-spec prerequisite in the bulk-operations workshop if
bulk generation is the first consumer.

**Tests if approved:** schema valid/invalid fixtures for each conditional form;
parser tests for IDs, references, cycles, and hash guards; CLI tests for every
legal and illegal transition; integration tests showing that dispatch is
refused without the plan and convergence/escalation is enforced. A plan file
with no dispatch or close-time consumer fails the acceptance test.

## Deliberate non-changes

- **Do not add a Commonplace model runner or scheduler.** ADR 035's harness
  ownership remains sound, and the research does not create a target-side need
  for leases, heartbeats, background monitoring, or vendor adapters.
- **Do not generalize `ReviewJobPlan` or expand `review_jobs` with planning
  fields.** Its criterion is already the judgment-bearing intent for a fixed
  assay; its convergence boundary is all-or-nothing finalization plus freshness
  CAS. Options, probes, and DAPP-style triggers are out of scope for that job.
- **Do not turn `FullPassReport` into a base class.** Reuse its design pattern—
  conditional schema, immutable captures, a parser, a guard, bounded recovery—
  when another workflow earns it. Do not reuse its workflow-specific fields.
- **Do not make `kb/tasks/types/task-active.md` the generic plan by default.** It
  is schema-null, unconsumed, and not scaffolded as an installed task type.
  Tightening it would create trusted-looking state without enforcement.
- **Do not code numeric option valuation or universal reversal-cost enums.**
  Commonplace needs the qualitative decision premises, not imported financial
  machinery or invented precision.
- **Do not automatically preserve multiple candidates.** AutoReason's three
  versions are an experiment with a fixed evaluation and stop rule. Elsewhere,
  parallel alternatives without discriminating tests and convergence only add
  carrying cost.
- **Do not treat relocation dry-run or generated indexes as persisted plans.**
  They are immediate deterministic previews/materializations. Persist and guard
  them only if approval and apply must genuinely span changing repository
  state.
- **Do not attribute target fields to Sobek, Ward, and Liker (1999).** The
  verified support is the later substitute paper, and the exact 1999
  formulation remains outside the retained evidence boundary.

## Priority order

1. Refine the shared instruction authoring contract and the multistage brief,
   using the explicit transfer gloss.
2. Run the planning-placement experiment; use its results to decide how much of
   the richer deferral checklist earns a durable instruction surface.
3. Land the two bounded deterministic improvements: strict review-selector
   protocol versioning and inferable ingest handoff validation.
4. Keep review batching adaptive only as an offline telemetry experiment.
5. Open a persisted-plan proposal only after a named consumer and a second
   recurring workflow establish the need.
