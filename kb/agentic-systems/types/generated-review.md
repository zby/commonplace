---
type: types/type-spec.md
name: generated-review
description: "Compact public projection of one complete agentic-system analysis run, generated from and pinning the run's retained manifest"
schema: ./generated-review.schema.yaml
---

# Generated agentic-system review

The compact public projection of one complete run, published under
`kb/agentic-systems/reviews/<system-slug>.md`. It is generated from the
run's retained set and pins the set’s manifest, so a reader can verify
and open the exact analysis from a clean checkout. It is not hand-edited:
a correction goes through the method and a new run. Its frontmatter is
what publication checks, with the pin on the manifest.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-systems/types/generated-review.md` |
| `description` | Yes | The overview's `description`: the synthesizer's one-sentence retrieval description of the system's mechanism and limits |
| `generated-by` | Yes | `analyse-agentic-system` |
| `analysis-run` | Yes | The producing run ID |
| `source-identity` | Yes | The stable source identity the set's Source register declares |
| `reviewed-revision` | Yes | The set's `reviewed-boundary` |
| `analysis-artifact` | Yes | `kb/agentic-systems/reports/retained/<run-id>/ARTIFACT.yaml` |
| `analysis-artifact-sha256` | Yes | SHA-256 of the retained manifest's bytes |

## Body

Code renders the body from the verified overview; no job writes it. It
has four parts, in order:

1. `# <System>`, the run's `system` parameter.
2. One **evidence basis** line, built from the overview's boundary fields:
   the evidence tier, the source identity, the reviewed revision and the
   analysis cutoff.
3. The overview's Bounded synthesis, unchanged except for its links.
4. `## Limitations` with the overview's Limitations.

Relative links in the overview resolve inside the set directory, so code
rewrites them to resolve from the review into the retained set under
`kb/agentic-systems/reports/retained/<run-id>/`. Absolute URLs and
anchor-only links stay as they are. The review therefore makes no claim
the set does not make, and the overview's contract for the Bounded
synthesis (no ranking, adoption advice, system-wide grade or transfer
recommendation) holds for the review too.

## Template

```markdown
---
type: agentic-systems/types/generated-review.md
description: "{one-sentence description}"
generated-by: analyse-agentic-system
analysis-run: AAS-YYYY-MM-DD-system-slug-nn
source-identity: {stable identity}
reviewed-revision: "{revision or capture label}"
analysis-artifact: kb/agentic-systems/reports/retained/{run-id}/ARTIFACT.yaml
analysis-artifact-sha256: "{sha256}"
---

# {System}

Evidence basis: {evidence-tier} analysis of `{source identity}` at `{reviewed-boundary}`, with an analysis cutoff of {analysis-cutoff}.

{The overview's Bounded synthesis, with its links rewritten.}

## Limitations

{The overview's Limitations.}
```
