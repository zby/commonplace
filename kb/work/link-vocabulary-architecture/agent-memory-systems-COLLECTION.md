# PROPOSED: Writing conventions for kb/agent-memory-systems/

> Workshop draft. Delta from current `kb/agent-memory-systems/COLLECTION.md`:
> - Outbound linking section reorganised **per destination collection** rather than by register. Each destination block declares when the connect skill should search it and which labels writers may use.
> - Intra-collection labels import the common descriptive-shaped set plus `compares-with` as a collection extension — comparisons between reviewed systems are the load-bearing work here, and no other label names the "parallel design-axis analysis" reader-need.
> - `cross-reference` and `describes` dropped per [`label-audit.md`](./label-audit.md) — neither names a specific reader-need.
> - Cross-collection labels selected from the shared catalogue in [`link-vocabulary.md`](./link-vocabulary.md). This `COLLECTION.md` is authoritative for writers; `link-vocabulary.md` is a resource for `COLLECTION.md` authors.
> - `grounds` (an intra-theoretical label) replaced with `rationale`.
> - All other sections unchanged.

## Register

This collection operates in the **descriptive [register](../../notes/definitions/register.md)** (one of three content modes — theoretical, descriptive, prescriptive — determining quality goal, title conventions, and linking rules). It documents external agent memory, knowledge, and context-engineering systems — how each one is built, what it does, how it compares with commonplace.

The quality goal is **fidelity + economy**: faithful to what the code actually does, in minimum tokens. A review that misrepresents the reviewed system is worse than none — it pollutes the landscape.

## Structure

**`reviews/`** — individual system reviews, one file per system, typed as `kb/agent-memory-systems/types/agent-memory-system-review.md`. The workflow and section rules live in `types/agent-memory-system-review.md`.

**`source-only/`** — lightweight `type: kb/types/note.md` coverage for systems known from papers, READMEs, or articles when no reachable repository has been inspected. These entries keep source-only systems visible without using the repo-required review type.

**Collection root** — navigation (index, README), cross-system analyses (comparative reviews, focused comparisons), and any analysis grounded in multiple reviews. When an analysis makes a claim general enough to transfer beyond this landscape, consider promoting it to `kb/notes/`.

## Title conventions

**Reviews:** the repository name (`napkin.md`, `crewai-memory.md`) unless there is an established house-style variant.

**Root-level analyses.** Two cases:

- **Surveys and overviews** — use a topical title naming the subject (e.g., `agentic-memory-systems-comparative-review.md`).
- **Argumentative analyses** — analyses asserting a specific claim — use a claim-shaped title and add the `title-as-claim` trait, following the same conventions as `kb/notes/` (see `kb/notes/COLLECTION.md`).

## Fidelity discipline

Read code, not marketing. Ground every review in primary sources — README, architecture docs, package manifests, core source files. Do not rely on the README if the implementation clarifies or contradicts it.

When the system's docs say X but the code does Y, the review says Y and notes the divergence.

## Outbound linking conventions

Outbound rules are organised by destination collection. Each block declares when to search the destination for link targets and which labels writers may use.

### → `kb/agent-memory-systems/` (within this collection)

**Search:** when a review describes a component of a larger reviewed system, realizes an abstract contract named in another review, or can be compared to another system on a specific design axis (the comparative work is the collection's core).

**Labels:**

| label | reader-need |
|---|---|
| `part-of` / `contains` | wants to situate this in the larger system |
| `implements` / `implemented-by` | wants the concrete realization or the abstract contract |
| `compares-with` | wants a specific design-axis comparison with another system (collection extension) |
| `see-also` | might benefit but no specific need; use sparingly |

**`compares-with` vs `contrasts`.** `contrasts` (theoretical) names a difference in *claims*; `compares-with` names a difference in *systems* on a design axis. Use `compares-with` here; reserve `contrasts` for theoretical notes.

### → `kb/reference/`

**Search:** uncommon but worth a scan — commonplace and external systems are mostly described independently, but thematic analogues turn up. Search when a review's design element has a direct analogue in the commonplace system, or when the topic area overlaps a commonplace subsystem. Let the agent filter.

**Labels:**

| label | reader-need |
|---|---|
| `see-also` | the commonplace component is an instructive adjacent reference |

### → `kb/notes/`

**Search:** when a reviewed system's design rests on a theoretical claim. Note the asymmetry: theoretical notes more often link *into* this collection via `evidence` / `derived-from`; a review promoting a novel claim should promote it to `kb/notes/` and let the theory link back, rather than authoring a new theoretical claim from within the review.

**Labels:**

| label | reader-need |
|---|---|
| `rationale` | this system's design rests on this claim |
| `evidence` | rare; this system corroborates the claim |
| `defined-in` | reader may not know a term; target is under `kb/notes/definitions/` |
| `see-also` | might benefit but no specific need; use sparingly |

### → `kb/instructions/`

**Search:** uncommon. Reviews don't typically cite commonplace procedures, but scan when a review describes an operational workflow that has a commonplace counterpart.

**Labels:**

| label | reader-need |
|---|---|
| `see-also` | directly relevant adjacent reference |

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
