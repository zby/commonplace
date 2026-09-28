---
type: types/type-spec.md
name: generated-review
description: "Compact public projection of one complete agentic-system analysis run, generated from and pinning the run's retained overview"
schema: ./generated-review.schema.yaml
---

# Generated agentic-system review

The compact public projection of one complete run, published under
`kb/agentic-systems/reviews/<system-slug>.md`. It is generated from the
run's retained set and pins the set's overview, so a reader can verify
and open the exact analysis from a clean checkout. It is not hand-edited:
a correction goes through the method and a new run. Its frontmatter is
what publication checks, with the pin on the overview.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-systems/types/generated-review.md` |
| `description` | Yes | One-sentence retrieval description of the system's mechanism and limits |
| `generated-by` | Yes | `analyse-agentic-system` |
| `analysis-run` | Yes | The producing run ID |
| `source-identity` | Yes | The stable source identity the set's Source register declares |
| `reviewed-revision` | Yes | The set's `reviewed-boundary` |
| `analysis-overview` | Yes | `kb/reports/retained/agentic-system-analysis/<run-id>/overview.md` |
| `analysis-overview-sha256` | Yes | SHA-256 of the retained overview's bytes |

## Body

The body opens with one **evidence basis** line: what the analysis is
grounded in and when the evidence was captured, with the reviewed
revision. It then gives, in prose organized by the system's operation,
the discriminating mechanisms, the memory and epistemic findings that
change how the system should be read, and the limits, citing set records
by ID and linking the overview. Every claim it makes is present in the
set; it introduces no finding of its own. Quote blocks, where used, follow
the set's quotation contract and repeat passages the set holds, since the
review is a projection, not a member. It gives no product ranking,
adoption advice, or system-wide grade, and no transfer recommendation.

## Template

```markdown
---
type: agentic-systems/types/generated-review.md
description: "{one-sentence description}"
generated-by: analyse-agentic-system
analysis-run: AAS-YYYY-MM-DD-system-slug-nn
source-identity: {stable identity}
reviewed-revision: "{revision or capture label}"
analysis-overview: kb/reports/retained/agentic-system-analysis/{run-id}/overview.md
analysis-overview-sha256: "{sha256}"
---

# {System}

Evidence basis: {sources and capture date} at {revision}.

{Sections as the system's operation warrants.}
```
