# Directory artifacts workshop

## Commission

Posed by the operator on 2026-09-28. Extend Commonplace validation so a
set of documents in one directory can have its own type and set-wide
checks. The first production instance is the agentic-system analysis set.
The operator required an architectural design before implementation.

The [ADR draft](./adr-draft.md) is the authoritative record of the agreed
design, alternatives, open choices and acceptance checks. This README
records the work's scope, inputs, coordination and closure conditions.

## Remaining work

Resolve the draft's [open choices](./adr-draft.md#open-choices-before-implementation),
then demonstrate the proposed format on the real analysis set and the
[acceptance cases](./adr-draft.md#acceptance-checks-before-promotion) before
implementing it. These examples must expose the loading and schema
contracts concretely; they are not additional production types.

Implement the validator model and integrate the analysis consumers, with
tests for the acceptance cases. If the examples require disproportionate
machinery, revisit the design here before changing the shipped model.
Promote the draft only after implementation and verification.

The evaluation boundary is the analysis set plus fixtures for the generic
language. Skill directories and existing sidecar pairs may supply later
instances, but no additional production type is required. Add one only
if it already exists in the repository. The separate review of analysis
code size and redundant checks may use these findings; this workshop does
not own that review.

## Inputs

- The [output transition plan](../agentic-analysis-output-documents/transition-plan.md),
  including its revised-layering section, and the
  [consumer inventory](../agentic-analysis-output-documents/consumer-inventory-20260928.md).
- The analysis member type specs under `kb/types/`, the
  [type-spec contract](../../types/type-spec.md), and the
  [validation contract](../../reference/validation-contract.md).
- Candidate implementation `6d8d9fd0` ("Check the analysis set through a
  type rule on the overview"), reverted in `597055b5`. Its tests and
  changes to validation, path resolution, discovery and consumers show
  what the integration touches. Its overview-based recognition and
  manifest are superseded by the draft; it is implementation evidence,
  not the design to restore.

## Coordination

The [output-documents workshop](../agentic-analysis-output-documents/README.md)
owns the analysis set design and producer transition. Its
[relaxed run-state verification](../agentic-analysis-output-documents/transition-plan.md#relaxed-run-state-verification-2026-09-28-operator-decision)
retains member schemas, the existing pin chain, source and quote anchors,
committed-input checks and run identity agreement. Cross-member record
resolution and the profile-against-union check are deferred to this
workshop. Restoring those checks is distinct from preserving the checks
that still run. The transition also drops exact finalization derivation
and the set-level quote minimum; moving the manifest does not reinstate
them.

The operator confirmed the integration choices on 2026-09-28: membership
is the Markdown files directly beside `ARTIFACT.yaml`; the analysis
manifest stores every member's hash and is pinned externally; explicit
member validation checks the file and directory validation checks the set.
The draft retains a TODO to reconsider simpler integrity bookkeeping after
deployment.

The [workflow deployment plan](../agentic-analysis-output-documents/transition-plan.md#directory-artifact-deployment-2026-09-28-operator-decision)
owns moving analysis output into a dedicated directory and updating the
producer, publication and readers. That integration replaces the
overview's `members` metadata with schema-owned membership and the new
manifest, then changes the external pins. The generic feature does not
special-case analysis filenames or working files. Apply the workflow
changes when adopting the feature, not in advance. The refresh batch in
`kb/work/agentic-memory-refresh/batch-01-handoff.md` waits on the
output-documents transition, not on this workshop.

## Closure

Close when the numbered ADR records the implemented model, its acceptance
checks pass, the analysis set validates from a clean checkout, and the
equivalent checks it replaces in run-state verification, publication and
comparison loading have been removed. Then delete the workshop and remove
its entry from `kb/work/README.md`.

If the operator revises the decision to keep set checks outside the
validator, record that outcome and close without implementation.
