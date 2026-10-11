---
type: reference/types/design-proposal.md
description: "Proposal: cover systems such as Ars Umbris across a finite set of pinned repositories while preserving analysis roles, source IDs and path-only quotations"
---

# Multi-repository agentic-system analysis

## Goal

Allow one analysis to cover a system whose consequential mechanisms span several
repositories, such as Ars Umbris. Preserve the current analytical workflow and
quotation authoring experience rather than require a full run per repository.

The [retained scope comparison](../../reports/retained/multi-repository-analysis-scope-2026-10-11/multi-repository-scope-comparison.md)
provides the component pins, option comparison, source-consumer audit and limits
behind this proposal. Its Ars Umbris overwrite question is a bounded test case,
not an exhaustive system boundary.

## Current state (as of 2026-10-11)

The current roles can investigate cross-component mechanisms, and the `SRC-*`
register can distinguish several sources and their evidence layers. Acquisition,
frozen-boundary checks and quotation resolution nevertheless bind one Git or
capture object. Declaring another source ID does not authorize its repository or
route quotations to it. Separate component accounts do not establish integration
without additional composition assessment.

## Candidate design and alternatives

**Preferred candidate: one frozen source tree with repository directories.**
Approve a finite set of repository identities and full commits before the run.
Present each repository as a top-level directory. A quotation path such as
`au-mcp/src/daemon/broker.ts` is an ordinary path with an additional directory;
the frozen manifest supplies its provenance. Retain source IDs, evidence-layer
and inspected-scope information, and existing analyst record IDs. Do not require
per-quotation source selection or repeated revisions.

Acquisition, boundary validation and publication would consume the approved
manifest as a binding input. Analysts and report verification would consume the
source tree through the existing boundary input. Source lookup would resolve only
approved component paths. These multi-repository consumers must be built; the
source register alone does not implement them. Keep existing roles, independent
verification, correction ownership and exact-byte publication.

Alternatives remain available: a single-component run can answer a deliberately
narrower question; separate runs can produce independently reusable component
accounts, at the cost of repeated workflow work and a separate composition
assessment. Neither answers the same cross-component question merely by accepting
its component reports.

## Forces and open choices

Coverage must justify source-preparation, verification and operator-reading cost.
The operator reports recurrent quotation friction; directory prefixes are acceptable,
but a richer quotation grammar or substantial additional repair work is not the
intended trade-off. Costs and reliability improvements remain unmeasured.

Leave physical tree construction and minimal shared-code changes open. Approve
membership and a stable system identity explicitly; discovering another repository
produces a limit or a request to revise the boundary, never recursive acquisition.
Full Ars Umbris coverage needs a separately scoped component set. Dependency
installation, target execution, source-ID removal and new analytical roles are
outside this proposal.

## Adoption criteria

Before adoption, demonstrate with offline fixtures that:

- Every approved component is available at its exact pin; partial preparation,
  changed pins or ambiguous directory names prevent live acceptance/publication.
- Existing path-only quotations work through repository directories without extra
  attribution fields. Wrong revisions, missing components and escaping paths fail
  safely; existing single-repository and capture behavior still works.
- The source register remains bound to approved provenance, and publication binds
  exact member bytes to the whole frozen boundary under a stable system identity.
- Existing retained analyses validate without rewriting. The implementation and
  observed quotation-repair burden are acceptable to the operator.

These deterministic checks are warranted by approved pins and exact file bytes.
They establish provenance, addressing and quotation occurrence, not claim support,
release compatibility or runtime safety. Adoption and implementation require a
separate commission; this proposal does not launch an analysis.
