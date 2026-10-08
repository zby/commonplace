# Publication consumer boundary

Keep the live CLI and skill on the legacy workflow. The opt-in declaration now
binds new-engine assembly and publication, but binding is not adoption evidence.
The operator requested an overall coherence review instead of the end-to-end
proof. That proof and a production switch are not authorized by these fixtures.
See [coherence review](./translation-coherence-review.md) for the remaining limits.
YAML compaction remains deferred.

## Inputs and content checks

`agentic_job_publication.assemble_analysis` and `publish_analysis` require:

- Opening metadata, pinned acquisition result and classified boundary.
- Exact permitted members and holding acceptances of their current versions.
- Either-end holding coverage for every declared relation between present members.
- Completed producer attempts whose primary output identifies each member.
- One consistent coordinator-reported model/effort identity, as required by the
  retained manifest contract. Heterogeneous workers require a separate decision.
- Closed criterion bytes, including collection and validation contracts, relevant
  types, `types/type-spec.md`, and the complete transitive schema closure.

`validate_pinned_analysis_set` checks supplied member names and bytes, the
manifest pins, member/type schemas and whole-set relations. It does not fall back
to schema caches, network or undeclared files. Frozen-source inspection is
explicitly authorized by the boundary's source pin. Stable-method link-existence
and type-eligibility checks remain environment guards. The opening/code/method
checks must still run before and after validation. Publication refuses warnings
because its current generated receipt does not retain their qualifications.

Draft checks use the same closed criterion mechanism without requiring a
published manifest. They do not establish semantic correctness. Independent
verifiers retain that responsibility.

## Canonical paths and reporting

`set/` is the sole new-engine set. Assembly's exact-byte manifest is an engine
output; publication consumes it, not the type-only working projection. No
persistent `output/` twin is created. Legacy manifest consumers reject engine or
mixed directories before writing. Legacy publication is not used as an adapter.

`agentic_engine_report` reports new-engine attempts, failures, stops, exhausted
jobs, holding judgments and canonical peer drift separately from legacy rounds.
Journal states are explicitly unverified. Its logical read-only operation may
create a lock file. `completed` means a current completed bound publication
attempt, not a fresh retained-filesystem audit. Invocation-specific scheduling
stops require the returned `RunStatus`.

## Effects and coordination

Complete dispositions can replace a retained set; other dispositions remain
local. The opening incumbent guard pins the overview digest. Exact whole-tree
identity begins with the publication journal, not opening.

`effects/publish.json` records exact old/new trees and archive intent before
mutation. Exact installed bytes and the exact archive recognize interrupted
completion. Exact old bytes without an archive permit retry. Partial, changed or
mismatched effects remain uncertain; do not clean them blindly. Ordinary failures
restore the old tree. Uncertainty becomes an engine failed attempt and Stop.

Both legacy and new publishers acquire the shared repository publication lock
under the ignored analysis state root, after any per-run lock. It covers incumbent
validation, recognition, mutation and rollback. These guarantees cover
cooperating publishers using the same repository root. Authority must exclude
non-cooperating writers during publication; byte rechecks alone do not eliminate
those races. Rollback never removes unrecognized bytes under that coordination
precondition.

## Verification boundary

Narrow scripted tests cover member/coverage/provenance rejection, exact manifests,
local non-complete results, temporary-tree publication and archives, rollback,
interrupted effects, symlinks, uncertainty propagation, locks and legacy rejection.
Separate tests exercise closed types/schema references and bounded source reads.
Some adapter-isolation fixtures use minimal schemas; they are not shipped-contract
certification. No full-pipeline or real-analysis proof follows from these tests.
