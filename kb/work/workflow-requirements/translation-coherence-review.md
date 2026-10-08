# Analysis translation coherence review

## Decision and scope

The opt-in translation has handlers and declared inputs through assembly and
publication. Keep the live CLI and analysis skill on the legacy workflow. Do not
compact YAML or claim production readiness. The operator requested this review
instead of the planned end-to-end proof. That proof was not run.

Review the contracts and mechanisms, not only test counts. The review covered
worker loading, criterion and member snapshots, correction answers, semantic
gates, historical verdicts, disposition-dependent coverage, provenance,
publication effects, reporting and legacy routing. An independent read-only
coding review supplied findings; the coordinator integrated and checked fixes.
No analytical workers, source acquisition from the network, target execution,
installation or repository retained publication was used.

## Fixed findings

### Criterion inputs were declared but not consumed as pinned bytes

Declaring a schema file did not make the legacy validator use that input. Draft
checks could read installed schema bytes or process caches instead. Publication
initially refused to validate rather than pretend this boundary was sound.

`CriterionSnapshot` now closes type and transitive schema resolution over supplied
bytes. Missing references, unsupported reference mechanisms and cache substitution
fail explicitly. `ValidationRun`, draft checks and whole-set publication consume
that snapshot. Frozen Git inspection reads committed blobs rather than mutable
checkout files. The handlers retain source and before/after method/code guards.
Tests cover differing disk/pinned schemas, inactive transitive references,
cross-run cache isolation, missing dependencies and exact member snapshots.

Technical basis: `src/commonplace/lib/type_resolver.py`,
`src/commonplace/lib/validation.py`, `agentic_job_validation.py`,
`tests/commonplace/lib/test_pinned_validation_contracts.py` and
`tests/commonplace/workflow/test_analysis_pinned_drafts.py`.

### Upstream waits could discard a late completed verdict's application

A verifier immediately ready against changed reports held back its apply job.
Its next completion could replace the latest-completed address before the earlier
verdict's historical judgments were recorded. Exhaustion could hold application
back indefinitely. Order-only test inputs had hidden production scheduling.

A narrow code-only exception now consumes a completed model attempt and its
handed members before that producer's rerun. It requires handed members from
another role and only immutable dependencies on the exempt producer. Current
member/judgment dependencies and own-answered-refusal-only checks keep their
ordinary waits. Model scheduling, exact subjects, installation and scope override
rules do not change. Tests use ordinary currency inputs, an open next attempt and
exhaustion; they retain scenario 17's wait and scenario 21's historical subjects.

Technical basis: `workflow/state.py`,
`tests/commonplace/workflow/test_completed_handed_scheduling.py` and scenario 21.

### Per-run locking did not coordinate publishers

A run lock did not prevent another run's publisher from changing a destination
between recognition and rename/removal. Both publishers now share a repository
publication lock covering incumbent checks, recognition, mutation and rollback.
Non-cooperating writers remain an authority-level exclusion requirement.

Technical basis: `agentic_publication.publication_lock`,
`agentic_job_publication.publish_analysis`, and publication/routing tests.

### Legacy finalization could create a second working set

Legacy manifest creation now rejects engine/mixed directories before writing.
The set type distinguishes legacy `output/` from new-engine `set/`. Assembly
supplies the published exact-byte manifest separately from the engine's type-only
working projection. It does not manufacture legacy state or an `output/` twin.

Technical basis: `agentic_finalize.py`, set type and routing tests.

### Holding historical judgments were easy to misread as current-set verification

A handed basis can remain holding after a canonical peer changes. This is correct
historical evidence, not verification of the new peer. Reporting now exposes
`canonical-peer-drift` separately from address-based stale acceptances. Coverage
still requires current endpoint versions, and stage gates retain all required
subject judgments. No mutable peer is substituted into a historical judgment.

Technical basis: `agentic_engine_report.py`, `workflow/state.py` and the report
regression in `test_completed_handed_scheduling.py`.

### Completion, retries and downstream ordering

The first closure of a model attempt is final within a result batch as well as
across invocations. A later duplicate cannot replace completion with failure.
The latest failed attempt remains retryable even if inputs revert to an earlier
successful baseline; presence, role permission and attempt limits still apply.

A newly completed upstream candidate is checked before a ready downstream model
that requires its role as an order-only input. This narrow exception applies only
to optional peer-member waits and an unconsumed candidate. Open downstream
attempts, required peers and live judgment gates retain their waits. The check
records existing peer bytes and rechecks when they change. It does not judge a
future peer or grant semantic acceptance merely by scheduling the check.

Technical basis: `workflow/engine.py`, `workflow/state.py` and
`tests/commonplace/workflow/test_engine_review_fixes.py`.

### Preliminary guards can prevent publication recovery

An interrupted replacement can leave tracked deletions that the worktree guard
rejects before journal reconciliation. If preliminary publication checks fail
while an effect journal exists, the invocation reports an uncertain effect:
exact-tree reconciliation has not established the outcome. Checks remain enforced
and evidence is preserved. A journal's state label alone does not prove recovery;
a rollback verified by the effect handler retains ordinary-failure semantics.

Technical basis: `agentic_job_publication.py` and actual-handler interruption
regressions in `tests/commonplace/workflow/test_analysis_publication.py`.

### Rejected sources and boundary links

Boundary invocation checks authorize source identity, frozen pins and capture
containment before reading source bytes or invoking Git. A rejected source is
not inspected for additional integrity diagnostics. Boundary members also use
the same relocation-safe link rule as the other published members.

Technical basis: `agentic_boundary.py`, `validation.py` and
`tests/commonplace/lib/test_analysis_boundary_review_fixes.py`.

## Reviewed invariants

- A valid blocker-bearing verifier document is not acceptance of its subject.
  Separate blocker-free subject judgments cover semantic gates. Invalid verdicts
  refuse the verifier candidate only. No automatic scope overrides are issued.
- Apply jobs declare completed verifier attempts and exact handed subjects.
  Identical verdict bytes about different subjects reapply. Historical judgments
  cannot restore an older member or deliver its refusal to a newer output.
- Structural repairs preserve semantic blockers and supplied limits. Answers use
  the previous-output versions delivered at opening, not newly installed members.
  Restoring earlier bytes does not spend another attempt on an already-answered
  refusal. All attempts still count; completion grants no acceptance.
- Assembly/publication enforce permitted and required members by disposition,
  holding current-member acceptances and either-end coverage for all present
  relations. Optional declaration inputs do not weaken handler completeness.
- Producer provenance identifies actual completed primary outputs and
  coordinator-reported model/effort, not an opening-model guess.
- Publication binds exact members and manifest, rechecks source/preparation/code
  and incumbent identity, and recognizes effects by exact trees and archive.
  Partial or changed effects remain uncertain, including when preliminary guards
  block journal reconciliation. Verified rollback remains an ordinary failure.
  Non-complete sets remain local.

## Limits retained rather than hidden

1. No full-pipeline, shipped-contract end-to-end proof was performed. Narrow
   fixtures do not establish every interaction of the complete declaration.
2. Holding handed judgments and canonical-current verification are distinct.
   Drift is reported; graph coverage and all-subject gates enforce current
   endpoints. Do not describe holding alone as whole-set semantic currency.
3. Record-verification code requires at least one routed blocker when set-check
   failed. The verifier's instruction requires every finding to be addressed.
   Free-text semantic correspondence is not deterministically matched; the
   diagnostic now states this narrower code guard. A machine finding-ID contract
   would require a separate design decision.
4. Carried-limit code checks traceability, not faithful consequences or every
   ID-free uncertainty. Independent synthesis verification owns that judgment.
5. Opening pins the incumbent overview digest, not its entire tree. The journal
   pins the exact tree at publication. A whole-tree opening guard is not claimed.
6. Repository locking coordinates cooperating publishers only. Exclude external
   writers and publishers using another checkout/root from the same destination.
7. The bounded adapter deliberately supports the analysis types and supported
   schema-reference dialect. Unsupported tags, briefs, ingests, dynamic references
   and undeclared quotation dependencies fail rather than silently pass.
8. The retained manifest still permits one model/effort identity for a run.
   Heterogeneous-worker publication requires an adopted provenance contract.
9. New reporting is separate from legacy round state and is not a filesystem
   completion audit. The production CLI/skill are intentionally not switched.

The remaining step is an explicitly authorized adoption decision with the
requested verification boundary. This review must not be represented as the
end-to-end proof it replaced.
