# Writing conventions for kb/agent-memory-systems/

## Register

This collection is **descriptive**: it documents external agent memory, knowledge, and context-engineering systems — how each one is built, what it does, how it compares with commonplace.

The quality goal is **fidelity + economy**: faithful to what the code actually does, in minimum tokens. A review that misrepresents the reviewed system is worse than none — it pollutes the landscape.

## Structure

**`reviews/`** — individual system reviews, one file per system, typed as `kb/agent-memory-systems/types/agent-memory-system-review.md`. The workflow and section rules live in `types/agent-memory-system-review.md`.

**`source-only/`** — lightweight `type: kb/types/note.md` coverage for systems known from papers, READMEs, or articles when no reachable repository has been inspected. These entries keep source-only systems visible without using the repo-required review type.

**Collection root** — navigation (index, README), cross-system analyses (comparative reviews, focused comparisons), and any analysis grounded in multiple reviews. When an analysis makes a claim general enough to transfer beyond this landscape, consider promoting it to `kb/notes/`.

## Title conventions

**Reviews:** the repository name (`napkin.md`, `crewai-memory.md`) unless there is an established house-style variant.

**Root-level analyses:** topical for surveys (`agentic-memory-systems-comparative-review.md`); claim-shaped, with the `title-as-claim` trait, when the analysis makes a specific argument.

## Fidelity discipline

Read code, not marketing. Ground every review in primary sources — README, architecture docs, package manifests, core source files. Do not rely on the README if the implementation clarifies or contradicts it.

When the system's docs say X but the code does Y, the review says Y and notes the divergence.

## Outbound linking conventions

When linking FROM this collection:

| To register | Appropriate relationships |
|---|---|
| Descriptive (same register) | cross-reference / see-also |
| Theoretical (kb/notes/) | grounds / evidence |
| Prescriptive (kb/instructions/) | procedure (rare) |

## Types

- `agent-memory-system-review` -> `kb/agent-memory-systems/types/agent-memory-system-review.md`
  Use for code-grounded reviews of external agent memory or context-engineering systems.
- `note` -> `kb/types/note.md`
  Use for source-only coverage and cross-system descriptive analyses.
- `index` -> `kb/types/index.md`
  Use for navigation hubs and generated directory indexes.

## What does NOT belong here

- Transferable claims about KB methodology → `kb/notes/`
- Procedures and how-to guidance → `kb/instructions/`
- Descriptions of the commonplace system itself → `kb/reference/`
- Raw snapshots of external sources → `kb/sources/`
- Work in progress → `kb/work/`
