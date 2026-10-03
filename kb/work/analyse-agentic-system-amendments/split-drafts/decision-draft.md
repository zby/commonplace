# Separate analysis ownership and publish by reference

Draft decision material, not an accepted ADR. Assign the ADR number and adoption
date only after the decision is made and implemented. Revises
[ADR 099](../../../reference/adr/099-agentic-analysis-method-and-reports-belong-to-the-collection.md).

## Context

Analysis workers need a small complete collection contract. Sharing their
mandatory contract with method authors and public comparison writers exposes
them to unrelated rules and future input growth. The selected optimization is
role-specific input reduction; reduced bytes do not establish analytical quality.
The prototype and complete-packet measurements must establish the saving.

## Proposed decision

Create `kb/agentic-system-analyses/` with its own contract, local analysis member
and run-state types, ignored state, accepted retained sets and historical archives.
Keep the method and comparison/public-navigation ownership in agentic-systems.
Its instructions may explicitly govern reports in the new collection.

Public analyses are accepted retained sets entered through their overview.
Workflow-owned references in agentic-systems select and pin them. Do not generate
a second synthesis. Comparison readers use references and manifest pins.

Authorize one bounded migration of the two current retained sets, their required
path/type/link changes and dependent pins. Preserve findings, sources, record/run
identities and historical method/synthesis provenance. Retain a verified hash map.
Move historical archives byte for byte, keeping historical type identities and
validation exclusions; preserve URL navigation through explicit redirects.
Keep the earlier migration report as historical evidence, with its original map
and hashes. This authority applies only to the inventoried migration cohort.

## Considered alternatives

Shortening the existing contract avoids relocation and may achieve comparable
input reduction. Measure it before choosing the split; the split is preferred
only if its sufficient small contract and ownership boundary justify migration.
A worker exemption introduces a special inheritance rule and is not proposed.
Moving only types violates local type eligibility. Continuing duplicate public
synthesis adds a second authored account where an accepted overview can suffice.

## Consequences

Workers receive the new contract explicitly as a job dependency. Local type
resolution and validators enforce membership. Publication and comparison readers
consume reference identities and hash pins. Site allowlists and reference
validation enforce public exposure; projected research skills retain their
canonical method owner. These are the decision's consumption paths.

The split adds cross-collection method dependencies and migration maintenance.
It does not alter analytical definitions, waive acceptance gates, authorize
correction of retained findings, change generic collection rules, or allow old
runs to adopt a new method commit. A live evaluation run is separate authority.
