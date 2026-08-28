# Planning and delegation machinery: implementation handoff

## Status

The source-grounding and two machinery-revision passes are complete. This file
records what landed, what was deliberately not built, and which unresolved
items still have a reason to exist. The comparative argument remains in the
[research report](./research-report.md); the ordered possibility space remains
in the [machinery revision plan](./machinery-revision-plan.md).

## Source and theory outputs

Eight authoritative source ingests now retain enough verbatim material for the
claims promoted in this pass: three mission-tactics or *Auftragstaktik*
sources, two rolling-wave or progressive-elaboration sources, and one source
each for real options, DAPP, and set-based design. All eight validate; the PMI
lexicon's open-vocabulary `reference-lexicon` genre produces the one deliberate
warning documented in the research report.

The pass promoted:

- [Productive deferral requires a preserved option, discriminating evidence,
  and a convergence rule](../../notes/productive-deferral-requires-option-evidence-and-convergence.md).
- [Intent-framed delegation is a control regime, not a short prompt](../../notes/intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md).

It revised:

- [Current-task fit alone does not warrant costly structural entrenchment](../../notes/current-task-fit-alone-does-not-warrant-costly-entrenchment.md)
  with the real-options conditions, delay costs, and bounded-probe alternative.
- [An author should fix what the executor can't determine, not what it will](../../notes/fix-what-the-executor-cant-determine-not-what-it-will.md)
  to make information allocation bidirectional and distinguish timing,
  evidence production, and actor ownership.
- [Solve low-degree-of-freedom subproblems first](../../notes/solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md)
  to stop equating temporal deferral with delegation.
- [Capable agents need methodology selection](../../notes/capable-agents-need-methodology-selection.md),
  [weight-resident methodologies compress behavior in context](../../notes/weight-resident-methodologies-compress-behavior-in-context.md),
  and [borrowing can operate through retained artifacts or weight activation](../../notes/borrowing-can-operate-through-retained-artifacts-or-weight-activation.md)
  with an activation-fidelity condition for ambiguous cues.

The first two filenames in that three-note activation-fidelity item were shortened through
`commonplace-relocate-note` after the edits exposed pre-existing 70-character
contract failures. Their titles did not change, backlinks were rewritten, and
`properdocs.yml` now carries the redirects.

## Machinery changes that landed

### Delegation safety seam

The root and scaffolded control-plane instructions, instruction collection and
type contracts, instruction-writing procedure, workshop contract, and control-
plane reference now agree on a small portable delegation contract:

- delegation does not expand the task's authority;
- consequential worker packets name intended result, constraints, owned output
  or write scope, accessible inputs, coordination boundary, verification or
  feedback, and stop or escalation conditions;
- the parent retains scheduling, integration, and recovery;
- parallel mutation requires disjoint ownership or an explicit coordination
  rule; and
- nested delegation requires explicit authorization.

These rules landed in `AGENTS.md`, `AGENTS.md.template`,
`kb/reference/control-plane-goals.md`, `kb/types/instruction.md`,
`kb/instructions/COLLECTION.md`, `kb/instructions/write-instruction.md`, and
`kb/work/COLLECTION.md`.

The instruction type and workshop collection also now consume the revised
information-allocation rule. They retain privileged facts, external or cross-
work coupling, and coordination-bearing selections; they leave decoupled
arbitrary choices and situation-dependent means open. A workshop execution
plan that deliberately leaves consequential future work coarse must name how
that item returns to decision, while non-plan workshops incur no such protocol.

### Existing decision consumers

- [Invert solution-shaped requests](../../instructions/invert-solution-shaped-requests.md)
  now enters a commit/wait/probe/decline comparison only when action would
  destroy a meaningful alternative or create a costly-to-reverse dependency.
  It requires a named later observation or bounded probe and accounts for
  current benefit, coordination value, expiry, and alternative-maintenance
  cost.
- `kb/instructions/cp-skill-convert/SKILL.md` no longer assigns speculative
  tags during conversion or treats connect reports as mutation authority, and
  it no longer carries an unowned catalogue of future conversions.

### Deterministic code and tests

- `create_review_jobs` now rejects selector payloads whose `schema` is missing
  or differs from the emitted `commonplace-review-targets/2` constant before it
  consumes targets or model selection.
- The scaffold skill-projection test now derives its expected promoted skills
  from `MANIFEST.promoted_skills`, so additions cannot silently escape copy
  coverage.
- Focused review and scaffold tests passed before this handoff. The final
  integrated result is recorded below.

## Second delegated-authoring pass

The promoted multistage writer now uses one isolated reconstruction worker,
one staged-reveal disposition/candidate author, and one digest-bound independent
reviewer. The parent retains evidence, authority, invalidation, integration,
promotion, validation, and recovery. Separate skeleton, draft-only, mutable
audit, and redundant acceptance stages were removed. The exact accepted target
digest and audit account are in the [delegated authoring surface
sweep](./delegated-authoring-surface-sweep.md).

The same pass repaired bounded consumers that shared the mechanism:

- instruction type, authoring, and collection rules now distinguish a complete
  worker handoff from consequential temporal deferral and no longer prefer a
  fresh context merely for reset;
- mailbox requests, warning deferrals, prose deferrals, and retained log work
  now name the choice, evidence, return, and stop boundaries they actually need;
- warning sweeps and tag follow-up no longer delegate automatically without an
  information or disjoint-capacity advantage;
- AutoReason actors, the full-pass copyeditor, and the memory-review drafter
  have complete anti-recursion and no-grandchild boundaries; and
- generated report-job prompts now permit the parser's existing `ERROR`
  escalation route and forbid nested delegation instead of forcing a guess.

## Commit / wait / probe assay

The [behavioral assay](./commit-wait-probe-assay/report.md) compared the current
real-options wording with the preceding least-commitment wording. Its 8/8
treatment versus 7/8 control result was below the preregistered threshold and
is not decision-useful. The evidence is retained for redesign; no machinery
change follows from it.

## Deliberate non-changes

The pass did not build a generic planner, persisted plan type, scheduler,
option schema, trigger monitor, or runtime model runner. The audits found no
second consumer or target-side evidence that would justify those structures.
It also did not put a bare *Auftragstaktik* cue into operative instructions:
the explicit gloss is the current reliable compact form until activation-
fidelity trials show that the name alone preserves the intended mechanism.

The following items remain proposals or experiment-backed work, not unfinished
parts of the changes above:

- ingest handoff validation against name-paired snapshots;
- memory-system review staging, recovery, and failure-path tests;
- retirement or harness-native replacement of the legacy nested-CLI iterative
  revision skill;
- static nested-delegation and agent-CLI authority checks;
- the methodology-cue behavioral assay and any redesigned replication of the
  inconclusive commit/wait/probe assay;
- a decision on the unconsumed task subsystem; and
- any generic persisted plan, only after two real workflows need the same state
  and a named consumer exists.

## Remaining theory and source handoffs

- The costly-entrenchment workshop retains one proposed, unconfirmed note on
  cheap adoption plus weak retirement accumulating cost. Do not create it
  without maintainer confirmation.
- The known-feasible-set boundary in the low-degree-of-freedom ordering claim
  and a possible rolling-wave/set-based refinement of specification strategy
  remain plausible but were not required for the repaired delegation theory.
- Revisit PMI Lexicon Version 5, Sobek/Ward/Liker (1999), an untouched 2012
  ADRP 6-0, or Pindyck's published JEL pagination only under the exact
  conditions in the research report's source-revisit queue.
- No current source warrants an empirical claim that the combined methodology
  improves LLM-agent outcomes. That remains a target-side experiment.

## Validation record

The integrated pass completed on 2026-08-28:

- all 43 changed or newly created Markdown artifacts passed
  `commonplace-validate`; the PMI ingest retained its one deliberate
  open-vocabulary genre warning;
- focused `ruff` checks passed for the changed runtime and test files;
- `git diff --check` passed; and
- `uv run pytest` passed all 598 tests in 37.41 seconds.

The second delegated-authoring pass also completed on 2026-08-28:

- all 17 changed or newly created Markdown artifacts passed their explicit
  `commonplace-validate` calls without warnings or failures;
- focused `ruff` checks passed for the review-prompt code and test;
- focused review-protocol tests passed all 26 cases, and the scaffold projection
  test passed all 18 cases;
- `git diff --check` passed; and
- `uv run pytest` passed all 599 tests in 44.24 seconds.
