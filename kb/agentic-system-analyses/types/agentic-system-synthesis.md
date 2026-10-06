---
type: types/type-spec.md
name: agentic-system-synthesis
description: "The synthesizer's public account of one analysis run: the retrieval description, the bounded synthesis and the limitations that code assembles into the overview"
schema: ./agentic-system-synthesis.schema.yaml
---

# Agentic system synthesis

The public account of one analysis run, written after the records have
passed independent verification. Code copies its parts into the
[overview](./agentic-system-analysis-overview.md): the frontmatter
`description` becomes the overview's description, and `## Bounded synthesis`
and `## Limitations` become the overview's sections of those names. The
overview type fixes what those sections must contain and how they read; this
type fixes the document the synthesizer writes and the verifier judges.

## Frontmatter

| Field | Required | Use |
|---|---:|---|
| `type` | Yes | `agentic-system-analyses/types/agentic-system-synthesis.md` |
| `description` | Yes | One sentence on the system's mechanism and limits, 50 to 250 characters; it is the overview's retrieval description |
| `run-id` | Yes | The run's ID |
| `reviewed-boundary` | Yes | The run's immutable revision or capture identity |

## Body

`## Bounded synthesis` and `## Limitations`, in that order and nothing else,
with the content the overview type requires of them. Every record ID resolves
in the accepted set, and relative links are written as they will resolve from
`overview.md` in the set directory.

## Template

```markdown
---
type: agentic-system-analyses/types/agentic-system-synthesis.md
description: "{one sentence on the system's mechanism and limits}"
run-id: AAS-YYYY-MM-DD-system-slug-token-nn
reviewed-boundary: "{immutable revision or capture identity}"
---

# {System} synthesis

## Bounded synthesis

## Limitations
```
