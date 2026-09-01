# Mission order — agent operability second slice

This plan uses the transferable mechanism behind *Auftragstaktik*: upstream
fixes intent, boundaries, acceptance, authority, and coordination; execution
chooses means from live evidence. The label alone supplies no control regime.
The governing Commonplace accounts are
[intent-framed delegation](../../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md)
and the rule to
[fix what the executor cannot determine](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md).

## Situation

The first operability slice made status compact, added stable action IDs, and
mechanically exposed workshop and task contradictions. It did not make copied
framework inputs identifiable in an installed project. The active command can
report its package version, but it cannot prove which doctrine, library files,
scaffold files, or projected skills govern the project. Rerunning
`commonplace-init` compares the project with current upstream bytes and
preserves differences, but cannot distinguish a local customization from an
upstream change because it has no prior baseline.

The [baseline](./baseline.md) identifies the known implementation surfaces and
the questions live evidence must answer. The executor should update it when an
observation changes the available alternatives; it is evidence, not an order.

## Intent

### Purpose

Let an agent inspect and safely prepare changes to an installed Commonplace
project without guessing which framework inputs produced it or treating local
customization as accidental drift.

### Desired end state

A newly installed project carries one trustworthy, versioned provenance record.
The active command can use it to distinguish current, locally customized,
upstream-changed, conflicted, incompatible, and genuinely unknown states. An
operator can request a reproducible, non-mutating three-way upgrade plan that
preserves local work and exposes the evidence, effects, risks, verification,
and recovery path for every proposed change. Normal status remains compact and
read-only, and review-system state remains opt-in.

The round is successful when a later agent can answer “what produced this
project, what differs, why, and what safe change is available?” from bounded
machine-readable evidence and drill-downs rather than repository archaeology.

## Key tasks

These are required effects, not a prescribed implementation sequence. Source
identity must be trustworthy before it is allowed to support an upgrade plan;
other investigation, prototyping, testing, and documentation may be ordered or
combined as live evidence suggests.

- **Establish project provenance.** Give copied framework surfaces and
  projected skills an inspectable relationship to the canonical inputs from
  which the project was created or last reconciled.
- **Distinguish operationally different states.** Make the six states in the
  desired end state deterministic, with stable evidence and a useful next
  action for each state that requires one.
- **Prepare change without applying it.** Produce a three-way upgrade plan
  that separates safe upstream changes, local-only edits, convergent edits, and
  conflicts while leaving the project untouched.
- **Prove the interface improves operation.** Exercise controlled fixtures,
  including a local customization and a real conflict; compare output size,
  elapsed time, tool calls, and decision burden with the first-slice baseline;
  and retain the result.
- **Leave shipped authority coherent.** If the solution changes architecture
  or creates load-bearing state, land the corresponding ADR, reference and
  command documentation, tests, package data, and recovery instructions.

## Boundaries

- Preserve every differing project file unless an explicitly authorized apply
  operation later names it. This round's upgrade plan does not mutate projects.
- Keep `commonplace-status` read-only and compact. Per-file evidence belongs in
  structured output or an explicit drill-down.
- Keep review warnings, jobs, and freshness behind `commonplace-status
  --review`; stale review pairs remain normal state for now.
- Treat `commonplace.scaffold_manifest` and its resolved package inputs as the
  shipped inventory. Do not create a second authored scaffold inventory.
- Do not turn `commonplace-init` into an upgrade operation.
- Do not identify user-authored project content as framework-owned merely
  because it sits beside copied framework content.
- Do not generalize operation packets, receipts, overrides, or lifecycle state
  machines without a second worked consumer that needs the abstraction.
- Follow the repository's existing authority, Git, validation, test, package,
  and workshop-closure rules.

## Executor's decision authority

Within an authorized execution of this workshop, the executor may choose the
investigation order, fixtures, internal representations, module boundaries,
command names, and test decomposition. It may reject a candidate design when
worked evidence shows that it cannot distinguish the required states, creates
duplicate authority, loses offline recovery, or costs more than the operational
problem warrants. It may run bounded probes and preserve more than one design
briefly when a named test can discriminate among them.

The executor may decide ordinary implementation details from the live code and
tests. It may not infer permission to apply an upgrade to a real external
project, change the review-status default, promote a generic framework from one
consumer, overwrite authored customization, or broaden this workshop into the
audit's later slices.

When alternatives remain equivalent after inspection, choose the simplest one
consistent with current architecture. When a choice changes authority,
retention, compatibility, or recovery semantics, capture it in an ADR rather
than burying it in code.

## Resources and coordination

The executor inherits Commonplace doctrine from `AGENTS.md`. The primary
starting points are:

- [the retained audit](../../reports/retained/agent-operability-audit-2026-08-31.md)
  for the operator problem and dependency order;
- [the first-slice result](../../reports/retained/agent-operability-first-slice-20260831/README.md)
  for the status baseline and the review-default constraint;
- [instruction generation](../../reference/instruction-generation.md),
  `src/commonplace/scaffold_manifest.py`, and
  `src/commonplace/cli/init_project.py` for current creation authority; and
- `src/commonplace/lib/project_status.py` and its tests for the existing
  situation projection.

This workshop owns integration of this slice. The
[lifecycle-management workshop](../lifecycle-management/README.md) retains
broader artifact-lifecycle questions, and the
[agent-runtime design workshop](../agent-runtime-design/README.md) retains
runtime approval and suspension. Do not edit their scope to make this task
appear complete. If concurrent work changes a shared surface, reconcile with
its owner or return the conflict before overwriting it.

## Execution plan

This is the initial route, not a command-by-command prescription. The stages
are ordered where one produces evidence or state needed by the next. Within a
stage, the executor chooses the means and may reorder, combine, or discard
probes when live evidence makes another route better. At each stage boundary,
update [baseline.md](./baseline.md), verify the output, and elaborate only the
next stage with what has become knowable.

### Stage 1 — establish the decision baseline

- [x] Create a disposable, controlled project through the source-checkout and
  packaged-wheel initialization paths.
- [x] Measure the copied inputs, projected skills, hashing cost, and current
  status output using the table in [baseline.md](./baseline.md).
- [x] Demonstrate what current package/project version fields can and cannot
  distinguish.
- [x] Test candidate provenance designs against templates, projected skills,
  offline comparison, legacy projects, and the six required project states.

Stage output: a short evidence-backed design choice, or a returned finding that
no examined design meets the intent. If the chosen record becomes load-bearing
state, record the architectural decision before implementation.

Completed 2026-09-01. [The Stage 1 design choice](./design-choice.md) selects a
tracked content-addressed baseline and requires its load-bearing semantics to
be recorded in an ADR before Stage 2 implementation.

### Stage 2 — make creation provenance-bearing

- [ ] Promote the Stage 1 design choice into an ADR that fixes the record's
  authority, tracked storage, producer, transitions, and recovery behavior.
- [ ] Implement one versioned provenance record with a single producer and
  explicit consumers.
- [ ] Produce it only after successful project creation without changing
  `commonplace-init`'s preservation behavior.
- [ ] Verify source-checkout, packaged-wheel, template-substitution, projected-
  skill, rerun, and incomplete-write cases.

Stage output: a newly initialized fixture project can prove which canonical
inputs produced every tracked framework-owned surface. Replan the classification
work from the record that actually survived these cases, not its earlier
design sketch.

### Stage 3 — expose trustworthy state

- [ ] Classify current, locally customized, upstream-changed, conflicted,
  incompatible, and unknown projects from the recorded and live evidence.
- [ ] Add stable structured evidence and executable drill-down actions while
  keeping the normal status view small.
- [ ] Verify that a legacy or unreadable record degrades honestly and that
  default status still excludes review state and does not create the store.

Stage output: every controlled state has the intended classification and a
useful next action where one exists. Any unclassifiable real case returns to
the provenance decision rather than being forced into the nearest category.

### Stage 4 — prepare a safe upgrade

- [ ] Compare prior baseline, current project, and selected upstream inputs in
  a reproducible, non-mutating plan.
- [ ] Distinguish unchanged, local-only, upstream-only, convergent, and
  conflicting changes in a customized-project fixture.
- [ ] Expose expected effects, authority, risk, verification, and recovery for
  every proposed change.

Stage output: an operator can inspect a complete three-way plan without any
project mutation. Return control at this point on whether a later commission
should add apply and a compact receipt; this plan does not assume that answer.

### Stage 5 — integrate, evaluate, and hand off

- [ ] Update the ADR and current reference, command, installation, and recovery
  documentation required by the shipped design.
- [ ] Run focused tests, the complete suite, Ruff, artifact validation, and
  lifecycle validation in proportion to the changed surfaces.
- [ ] Compare the finished path with the first-slice baseline and retain exact
  inputs, measurements, failures, operator decisions, and deferrals.
- [ ] Extract durable results and close the workshop when its closure conditions
  are satisfied.

Stage output: shipped behavior, authority, tests, documentation, and retained
evidence agree; later work has an explicit input rather than an implicit tail
of this plan.

## Feedback and return of control

Record decision-relevant observations in [baseline.md](./baseline.md). Return
the plan to the operator, or capture an architectural decision where doctrine
authorizes it, at these triggers:

1. **Provenance convergence.** Before making a provenance record load-bearing,
   show that it distinguishes all required states, identifies its sole producer
   and consumers, handles template substitution, and has a recovery story for
   absent or unreadable records. If no candidate does, return the failed cases
   rather than inventing certainty.
2. **Upgrade-plan convergence.** Once one realistic customized-project fixture
   yields a complete three-way plan, decide whether apply plus a compact receipt
   is a bounded, reversible extension. Add it only with explicit operator
   authority or a later commission; otherwise retain the plan as the input to
   the next slice.
3. **Boundary encounter.** Return immediately when success requires overwriting
   customization, changing default review visibility, adopting backward
   compatibility contrary to doctrine, changing an external project, or
   settling a cross-workshop decision this commission does not own.
4. **Unexpected architecture cost.** Reassess scope if provenance requires a
   new durable service, network availability, an unbounded content cache, or a
   second inventory authority. The desired effect remains fixed; the proposed
   means does not.

These are evidence-triggered returns, not approval checkpoints for ordinary
implementation choices.

## Acceptance evidence

The executor selects exact test structure, but closure requires evidence for
all of the following:

- controlled cases for current, customized, upstream-changed, conflicted,
  incompatible, and unknown projects;
- source-checkout and packaged-wheel creation paths, including templates and
  projected skills;
- incomplete writes, reruns, missing baselines, and unsupported record versions
  fail or degrade honestly without masquerading as current;
- the upgrade plan is reproducible and causes no project mutation;
- default status stays compact, excludes review state, and does not create the
  Commonplace store;
- changed Python passes focused and complete tests plus Ruff; changed KB
  artifacts and lifecycle state validate; and
- the retained result records exact inputs, observed effects, operator
  decisions, retries, failures, and deferred work.

## Later horizons

The following are visible so they are not mistaken for omissions, but this
mission does not own them: common operation packets; graph/FTS retrieval and
change-impact projection; general receipts and learning candidates; default
review-state reporting; broader durable-queue state machines; cue activation;
effect evaluation; and calibrated automation. A later commission should select
among them using the evidence this slice produces.
