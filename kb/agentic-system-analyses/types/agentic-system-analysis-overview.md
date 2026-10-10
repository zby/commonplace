---
type: types/type-spec.md
name: agentic-system-analysis-overview
description: "Code-written entry member of an analysis set: identity, disposition, links to every member, amendment index and deterministic validation"
schema: ./agentic-system-analysis-overview.schema.yaml
---

# Agentic system analysis overview

The code-written reading entry point of one `analyse-agentic-system` run's
retained set. It holds identity and disposition, links to every member, the
amendment index and the deterministic validation account. It copies no
member's account. The sibling `ARTIFACT.yaml` selects the
[analysis set type](./agentic-system-analysis-set.md) and pins every member,
including this overview.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-analysis-overview.md` |
| `description` | Yes | For a complete run, the synthesizer's retrieval description; otherwise a code-written sentence naming the system, boundary and disposition |
| `run-id` | Yes | Canonical `AAS-YYYY-MM-DD-system-slug-token-nn` identity |
| `system` | Yes | Source-native system name or the caller's unambiguous identifier |
| `run-date` | Yes | Date the run opened |
| `result-disposition` | Yes | `complete`, `blocked`, or `out-of-scope` |
| `target-class` | Yes | Target class under the [boundary type](./agentic-system-boundary.md); `null` before classification |
| `boundary-kind` | Yes | Extent of the selected target; `null` before establishment |
| `reviewed-boundary` | Yes | Immutable revision or capture identity, or `null` before establishment |
| `analysis-cutoff` | Yes | Applicability cutoff, or `null` before establishment |
| `evidence-tier` | Yes | `code-grounded`, `doc-grounded`, or `null` before establishment |
| `inputs-commit` | Yes | Full repository commit supplying the method; publication requires the method unchanged |

## Members

`## Members` links every other member by its declared path and role. Boundary,
reports, profile, synthesis and independent judgments remain inspectable in
their own bytes. A blocked or out-of-scope entry states its stopping condition
and links the boundary; it does not imply that later stages were reached.

## Amendment index

`## Amendment index` contains `Amended or superseded records: <IDs or none>`
and links `reconciliation.md` when present. It lists that member's
supersessions, not rewritten report text. Where reconciliation was not
reached, it says so.

## Deterministic validation

`## Deterministic validation` names the exact targets and results for every
member. It reports deterministic checks, not semantic verification or job
acceptance. The overview's digest never appears inside its own bytes.

## Template

```markdown
---
type: agentic-system-analyses/types/agentic-system-analysis-overview.md
description: "{the synthesizer's description, or the stopping disposition}"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
system: "{source-native system name}"
run-date: "YYYY-MM-DD"
result-disposition: complete
target-class: "{selected target class}"
boundary-kind: whole-system
reviewed-boundary: "{immutable revision or capture identity}"
analysis-cutoff: "YYYY-MM-DD"
evidence-tier: code-grounded
inputs-commit: "{full commit at run start}"
---

# {System} agentic-system analysis

## Members

## Amendment index

## Deterministic validation
```
