# Machinery revision plan

## Decision

Revise Commonplace through existing, consumed authority surfaces. Do not build a
generic planner, persisted plan type, agent scheduler, or universal option
schema on current evidence.

The three machinery audits agree that the research has two different kinds of
consequence:

1. **Immediate safety and coherence changes** belong in existing theory,
   instruction contracts, worker packets, workflow ordering, and validators.
2. **New planning machinery** requires target-side experiments or a proposal
   with a named consumer before implementation.

The detailed evidence is in the [skill audit](./audit-skills.md),
[instruction and contract audit](./audit-instructions-contracts.md), and
[code and structure audit](./audit-code-structures.md).

## Governing implementation rule

Move a decision into code or schema only when its truth is mechanically
inferable from existing authoritative state and a current consumer can act on
it. Keep semantic questions—whether information discriminates, a commitment is
consequential, a probe is worthwhile, or delegated authority is safe—in theory
and instructions until repeated outcomes justify a sharper representation.

Real-options reasoning is conditional. Invoke its commit/wait/probe comparison
only after establishing that the current act would destroy a meaningful
alternative or create costly-to-reverse dependencies. Capacity queueing,
ordinary priority deferral, review-finding disposition, and reversible local
edits do not automatically enter that branch.

## Phase 1: promote the theory owners

### 1. Productive deferral

Create one atomic note:

> **Productive deferral requires a preserved option, discriminating evidence,
> and a convergence rule.**

Its mechanism should distinguish commit now, passive waiting, a bounded
information-producing probe, and maintenance of several live alternatives.
The Pindyck ingest supplies the option-value conditions; rolling-wave planning,
DAPP, and set-based design supply distinct convergence forms. Target-side
operational recommendations must remain Commonplace inferences.

### 2. Intent-framed delegation

Create one atomic note:

> **Intent-framed delegation is a control regime, not a short prompt.**

It should retain planner-held intent, authority, coupling, privileged facts,
resources, feedback, integration, recovery, and accountability while assigning
execution-dependent means to the worker.

### 3. Revise existing owners

- Refine `fix-what-the-executor-cant-determine-not-what-it-will.md` so the
  information asymmetry is bidirectional and temporal deferral, active learning,
  and delegation are not conflated.
- Add the real-options conditions and delay-cost term to
  `current-task-fit-alone-does-not-warrant-costly-entrenchment.md`.
- Bound `solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md` by
  whether the feasible set is sufficiently known.
- Add activation-fidelity limits to the methodology-selection and
  weight-resident-methodology notes.

Use separate multistage writing runs because these artifacts have independent
claims and revision boundaries. Promote source-dependent claims only through
the normal grounding guard.

## Phase 2: deploy the universal delegation safety seam

Apply one composition-aware change across:

- `AGENTS.md` and `src/commonplace/scaffold/AGENTS.md.template`;
- `kb/reference/control-plane-goals.md`;
- `kb/types/instruction.md`;
- `kb/instructions/COLLECTION.md`;
- `kb/instructions/write-instruction.md`; and
- `kb/work/COLLECTION.md`.

The always-loaded rule stays short:

- delegation does not expand task authority;
- the worker contract fixes intended result, non-negotiable constraints,
  owned outputs or write scope, accessible inputs, coordination boundary,
  verification or feedback, and stop or escalation condition;
- the parent retains scheduling, integration, and recovery; and
- parallel writes need disjoint ownership or an explicit coordination rule.

The collection and type contracts add the conditional authoring detail. A
delegated packet must state whether nested delegation is authorized; silence
means no. Clean context is chosen when isolation, later evidence, or independent
parallel judgment creates a concrete benefit—not as a universal reason to pay
handoff cost.

Do not paste rolling-wave, real-options, DAPP, or set-based checklists into
`AGENTS.md`.

## Phase 3: change actual decision consumers

### Solution inversion

Revise `kb/instructions/invert-solution-shaped-requests.md`. Replace its
unconditional preference for the least-committing route with the smallest
sufficient action whose commitment, delay, information, and maintenance costs
are justified.

When the requested solution would create costly-to-reverse commitment, compare:

- commit now on current evidence;
- passively wait for a named exogenous observation;
- run a bounded information-producing probe; or
- decline or do nothing.

The branch names the preserved alternative, what later observation or probe can
change, whether the opportunity will remain, and the current benefit,
coordination value, or expiry cost lost by waiting. It does not become a new
mandatory report section for reversible work.

### Memory-system review promotion

Revise `write-agent-memory-system-review` so the incumbent remains live until a
replacement has passed worker validation, taxonomy QA, semantic QA disposition,
and final validation. Preflight worker capacity before incumbent mutation.
Stage the candidate outside the live path or keep a verified byte-exact backup
with a specified restoration branch. Archive and promote only at convergence.

Add failure-path coverage for unavailable worker capacity, missing output,
invalid output, semantic blocker, promotion failure, restoration, and successful
single archive.

### Sparse mutating delegation

- Harden `fix-warnings/fix-review-warnings-sweep.md` and `FIX-SYSTEM.md` with
  parent scheduling/integration ownership, disjoint paths, clean single-use
  workers, no recursion, diff/report validation, and explicit failure hand-back.
- Narrow the tag-change follow-up in `revise-note.md` to exact old/new tags,
  allowed artifact classes, and report-only handling of broader taxonomy work.
- Correct `cp-skill-convert`: connect discovers candidates but does not assign
  tags; remove the unowned catalogue of future conversions.
- Refine the memory-review type so “needs a use case” names the observation that
  could change readiness, and `What to Watch` distinguishes a signpost from an
  adopted trigger.

### Legacy iterative revision

`cp-skill-revise-iterative` launches a nested agent CLI outside harness worker
authority and lifecycle controls. The preferred disposition is retirement to a
short pointer to AutoReason or ordinary reviewed editing. Migration to a
harness-native iterative worker remains a materially different alternative and
should be selected only if a distinct use case survives the existing options.

## Phase 4: move repeated deterministic checks into code

### Ingest handoff validation

Extend existing ingest validation, when the name-paired snapshot exists and its
checksum matches, to check:

- capture metadata projected from the snapshot;
- exactly one `## Quotes` section immediately before
  `## Connections Found`; and
- absence of local Markdown links into ignored snapshots or generated connect
  reports.

Keep incumbent byte comparison and opaque retained-quote preservation in the
parent workflow until a real handoff manifest exists. Do not add locks, CAS, or
a generic delegation record.

### Review selector protocol

Make `create_review_jobs` reject selector JSON whose `schema` is missing or does
not equal the emitted `commonplace-review-targets/2` protocol constant. Do not
persist selector diagnostics into review jobs.

### Projection and worker-contract tests

- Derive the installed-skill copy test from `MANIFEST.promoted_skills` instead
  of a partial hard-coded tuple.
- Add a static test rejecting active instruction or skill sources that launch
  agent CLIs to bypass the harness.
- Add contract fixtures requiring explicit nested-delegation authority in
  delegation-heavy worker packets.

## Phase 5: experiments before broader machinery

### Commit / wait / probe discrimination

Compare current and proposed instruction wording on crossed cases varying:

- reversal cost;
- existence of a later discriminating observation;
- opportunity expiry or current benefit;
- availability of a cheap information-producing action;
- planner-only information; and
- a legitimate versus unowned coarse future item.

Score decision placement, preserved intent, appropriate option analysis, probe
selection, convergence, escalation, and unnecessary planning overhead.

This assay ran on 2026-08-28 but was not decision-useful. The compact
[evidence record](./commit-wait-probe-assay/report.md) retains the result and
the design changes needed before any replication. No machinery change follows.

### Methodology-cue activation fidelity

Compare no cue, bare *Auftragstaktik*, and the explicit gloss “preserve intent
and constraints; delegate execution-time choice of means” across supported
model partitions. Do not put a compact cue into operative instructions until it
reliably activates the intended mechanism without importing irrelevant military
machinery.

### Existing experimental workflows

- Keep AutoReason experimental until it beats simpler revision baselines on
  semantic fidelity and accepted gain relative to calls, tokens, and time.
- Compare the multistage paragraph-grain skeleton with a claim-and-inference
  skeleton before changing it.
- Use review telemetry to study grouping and batch size offline; do not add an
  adaptive scheduler on soft worker-reported consumption.

## Proposal queue

### Task subsystem

Decide whether to consolidate task state into `kb/work/` or establish
`kb/tasks/` as an operative temporal subsystem with its own collection contract,
landing, shipped types, scaffold files, and control-plane route. The current
schema-null task types are unconsumed and not shipped, so editing them now would
create trusted-looking planning state without an authority path.

### Generic persisted plan

Open a design proposal only after two recurring workflows need the same
cross-run state and a named consumer will load it before dispatch and at
convergence checkpoints. The proposal must choose an authority path before it
chooses representation. `ReviewJobPlan`, `FullPassReport`, and the task templates
must not be generalized merely because they are plan-like.

## Deliberate non-changes

- Do not add a package-owned model runner, scheduler, leases, heartbeats,
  background trigger monitor, or vendor adapter.
- Do not generalize `ReviewJobPlan` or `FullPassReport`.
- Do not require option, trigger, signpost, probe, or delay-cost fields in
  general schemas.
- Do not preserve multiple alternatives without an evaluation surface and
  convergence boundary.
- Do not treat queued work, ordinary backlog priority, or `deferred` review
  findings as real options.
- Preserve the current strong parent/worker contracts in ingest, review
  batching, full-pass improvement, compression review, and agentic-system
  analysis unless a concrete failure appears.

## Validation order

1. Validate every changed Markdown artifact and run affected type/collection
   conformance checks.
2. Exercise scaffold tests after control-plane template or promoted-skill
   changes.
3. Run focused unit tests for selector protocol, ingest validation, skill
   projection, worker authority, and memory-review failure paths.
4. Run the behavioral planning assay separately from deterministic tests.
5. Measure context/fork overhead only after the final instruction wording is
   known; treat cost as a guard, not a quality oracle.
