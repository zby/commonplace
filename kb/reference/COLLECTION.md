# Writing conventions for kb/reference/ (descriptive profile)

## Text contract and fidelity

Descriptive [profile](../notes/definitions/text-contract.md): accounts of what exists in the shipped Commonplace system — architecture, type system, operator surface, decision history. Aim at faithful representation of the system as built, not transferable theory.

Quality goal is **fidelity + economy** — say what the system actually does in minimum tokens, without omitting load-bearing details. An agent loading these docs is usually trying to act; every extra token competes with the task.

Tests for economy:
- Could this section be cut without losing information the reader needs to act?
- Is the same fact stated in two places? Deduplicate or link.
- Would a table or list say this more compactly than prose?

**Fidelity constraint.** Describe the system as built, even when the implementation deviates from the theory that inspired it. If the system does X but the theory says Y, describe X and note the deviation — the `rationale` link may carry the qualifier.

**Proposal exception.** Design proposals — finished but unadopted designs — live only under `proposals/` and carry the `design-proposal` trait. A proposal describes a design object faithfully (problem, option space, forces, free choices marked), not shipped behavior; its description leads with "Proposal:" so a reader acting on reference docs never mistakes proposed for shipped. Conventions: [proposals/README.md](./proposals/README.md).

## Title and description conventions

**Topical titles by default.** Answer "what is this about?" — "Type loading", "Storage architecture". A link like `see [type loading](./type-loading.md) for how types are resolved` reads naturally.

Exceptions: ADRs use numbered-decision format (`012-types-for-structure-traits-for-review.md`); definitions use the term as title.

**Description** (frontmatter) should name the specific system aspect covered — "how Commonplace resolves a note's type contract at authoring and validation time" beats "type loading in Commonplace".

## Outbound links

Forward-authored; backlinks are computed. Inline for strongest commitment, with a connective word that fits the argument (e.g. `implements [title](path)`, `rests on [title](path)`, `defined in [title](path)`). Footer for labelled — `- [title](path) — label: context phrase`.

Scan `kb/reference/`, `kb/notes/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/` for link targets. Do not link into `kb/work/` (workshop layer — value is consumed, not imported). The `rationale` edge to `kb/notes/` is the primary theory-ward edge; outbound edges to `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/` are uncommon (use them when a design choice was informed by a specific external system or source).

**Labels:**

| label | destinations | reader-need |
|---|---|---|
| `part-of` / `contains` | reference | situate this in the larger system |
| `implements` / `implemented-by` | reference | concrete realization ↔ abstract contract |
| `supersedes` / `superseded-by` | reference (ADR chains) | current or prior version |
| `rationale` | notes | this design rests on this claim |
| `defined-in` | notes/definitions | reader may not know the term |
| `derived-from` | sources, agent-memory, agentic-systems | this design choice is worked out from this external source/system, adding nothing beyond it — see the lineage semantics in `link-vocabulary.md` |
| `abstracted-from` | sources, agent-memory, agentic-systems | this design choice generalizes beyond this external source/system; the source is evidence, not a generator |
| `evidence` | sources, agent-memory, agentic-systems | this external source/system corroborates the description |
| `procedure` | instructions | for how to do this, see this instruction |
| `see-also` | any | adjacent companion; use sparingly |

## Types

| type | file | use for |
|---|---|---|
| `note` | `kb/types/note.md` | general shipped-system reference documents; design proposals under `proposals/` (trait `design-proposal`) |
| `adr` | `./types/adr.md` | architecture decision records |
| `definition` | `kb/types/definition.md` | shipped-system vocabulary terms |
| `index` | `kb/types/index.md` | reference navigation hubs and generated directory indexes |

## What does NOT belong here

- Transferable claims about KB methodology → `kb/notes/`
- Procedures and how-to guidance → `kb/instructions/`
- Descriptions of external systems → `kb/agent-memory-systems/reviews/` for memory/context-engineering systems, or `kb/agentic-systems/` for whole agentic systems and harnesses
- Work in progress → `kb/work/` (workshops)
- Generated operational artifacts → `kb/reports/`
