# Report collection split drafts

## Commission and status

On 2026-10-03 the operator requested draft files for the split described in
[the proposal](../report-collection-split-proposal.md). These files stage the
split case for review. They adopt no decision and authorize no relocation,
publication, method edit or analysis run. Proposed choices below are agent
recommendations, including the publication-reference format and migration scope.

The drafts remain under the workshop contract. Contract candidates use descriptive
filenames: placing an actual COLLECTION.md here would create an invalid nested
collection. Links in these drafts resolve from the workshop; promotion must
rewrite them for their destinations. Future paths are literal code spans.

## Drafts and intended destinations

| Draft | Intended destination or use |
|---|---|
| [Analysis collection contract](./analysis-collection-contract.md) | `kb/agentic-system-analyses/COLLECTION.md` |
| [Existing collection contract](./agentic-systems-contract.md) | Replace `kb/agentic-systems/COLLECTION.md` |
| [Analysis landing](./analysis-landing.md) | `kb/agentic-system-analyses/README.md` |
| [Analysis reference type](./analysis-reference-type.md) | `kb/agentic-systems/types/analysis-reference.md` |
| [Reference schema](./analysis-reference.schema.yaml) | Its schema sidecar |
| [Method maintenance](./method-maintenance.md) | Maintenance instruction in the new collection, which owns the method; mandatory for method authors only |
| [Publication contract](./publication-contract.md) | Collection-owned publication instruction, explicitly loaded by maintainers and reflected in workflow checks |
| [Decision draft](./decision-draft.md) | Material for an ADR revising ADR 099 after adoption and implementation |
| [Implementation plan](./implementation-plan.md) | Migration dispositions, consumer changes and acceptance |
| [Coverage check](./contract-coverage-check.md) | Clause audit, repairs and verified/proposed loading paths |
| [Shortening alternative](./shortened-agentic-systems-contract.md) | Reduced existing contract without relocation or publication changes |
| [Input comparison](./input-coverage.md) | Same-role and saved-packet comparison of both alternatives |
| [Measurement data](./input-measurements.json) | Exact file paths, byte counts and hashes |

The reference type is new. Existing analysis member types and schemas move with
mechanical identity/path changes; the implementation plan specifies those changes
instead of duplicating their full text here. Job packets keep their role contracts.

## Superseded by later decisions

On 2026-10-03 the operator decided that the new collection is self-contained
and that publication is an update of one current-analyses list; see the parent
proposal. These drafts predate that and need redrafting before use: the
analysis reference type and its schema (replaced by the list), the publication
contract (list update, owned by the new collection), the analysis landing,
and the existing-collection contract. The decision draft was rewritten to
these decisions and carries their revisit conditions as `TODO` items.

## Check result

The operator commissioned coverage and shortening checks after the first draft.
The [audit](./contract-coverage-check.md) repairs scope, title, link and loading
gaps. The [comparison](./input-coverage.md) shows that shortening obtains most
of the measured reduction. Both candidates still require promoting their
conditional authoring routes and supplying the collection contract as a job
dependency. Choose the ownership boundary before implementation; publication
by reference is a separate decision. No live method has changed.

## Closure

Close this draft set when the operator chooses the split or the shortening
alternative, and the chosen design has measured sufficient role inputs and a
concrete migration/publication contract. Implementation closure remains the
parent proposal's closure condition. A live run is separately commissioned.
