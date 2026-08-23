# Writing conventions for kb/reference/

## Text contract and fidelity

This collection holds the **choices** Commonplace made and faithfully describes the **current or historical state** they produced — architecture, type system, operator surface, and decision history. Content belongs here when its intended contribution is the selected value, adopted contract, implemented interface, exposed behavior, or prior system state rather than a substantive claim about the design space that remains after those choices are bound. Aim at faithful representation of the system as built, not transferable theory.

A reference artifact may contain supporting belief propositions without becoming a note. What decides placement is the artifact's intended contribution, stated by its title, description, and opening.

Quality goal is **fidelity + economy** — say what the system actually does in minimum tokens, without omitting load-bearing details. An agent loading these docs is usually trying to act; every extra token competes with the task.

Tests for economy:
- Could this section be cut without losing information the reader needs to act?
- Is the same fact stated in two places? Deduplicate or link.
- Would a table or list say this more compactly than prose?

**Fidelity constraint.** Describe the system as built, even when the implementation deviates from the theory that inspired it. If the system does X but the theory says Y, describe X and note the deviation — the `rests-on` link may carry the qualifier.

**Proposal exception.** Design proposals — finished but unadopted designs — live only under `proposals/` and carry the collection-local `design-proposal` type. A proposal describes a design object faithfully (problem, option space, forces, free choices marked), not shipped behavior; its description leads with "Proposal:" so a reader acting on reference docs never mistakes proposed for shipped. Once adopted or retired, a proposal is extracted and moved to `proposals/archive/`, which nothing outside it links into (ADR 056). Conventions: [proposals/README.md](./proposals/README.md).

## Title and description conventions

**Topical titles by default.** Answer "what is this about?" — "Collections and types", "Storage architecture". A link like `see [collections and types](./collections-and-types.md) for how types are resolved` reads naturally.

Exceptions: ADRs use numbered-decision format (`012-types-for-structure-traits-for-review.md`); definitions use the term as title.

**Description** (frontmatter) should name the specific system aspect covered — "how Commonplace resolves a note's type contract at authoring and validation time" beats "type loading in Commonplace".

## Outbound links

Author each outbound link from the reader need at its source. A reciprocal link is allowed when the reverse direction independently helps readers; never add one merely to mirror an existing edge. Find inbound links on demand with repository search; no backlink view is currently generated. Inline for strongest commitment, with a connective word that fits the argument (e.g. `implements [title](path)`, `rests on [title](path)`, `defined in [title](path)`). Footer for labelled — `- [title](path) — label: context phrase`.

Scan `kb/reference/`, `kb/notes/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/` for link targets. Do not link into `kb/work/` (workshop layer — value is consumed, not imported). The `rests-on` edge to `kb/notes/` is the primary theory-ward edge; outbound edges to `kb/agent-memory-systems/`, `kb/agentic-systems/`, and `kb/sources/` are uncommon (use them when a design choice was informed by a specific external system or source).

**Labels:**

| label | destinations | reader-need |
|---|---|---|
| `part-of` / `contains` | reference | situate this in the larger system |
| `implements` / `implemented-by` | reference | concrete realization ↔ abstract contract |
| `supersedes` / `superseded-by` | reference (ADR chains) | current or prior version |
| `compares-with` | reference | compare this artifact with a peer on a named design or contract axis |
| `rests-on` | notes | this design, description, or decision depends on this theoretical claim |
| `defined-in` | notes/definitions | reader may not know the term |
| `derived-from` | sources, agent-memory, agentic-systems | this design choice is worked out from this external source/system, adding nothing beyond it — see the lineage semantics in `link-vocabulary.md` |
| `abstracted-from` | sources, agent-memory, agentic-systems | this design choice generalizes beyond this external source/system; the source is evidence, not a generator |
| `evidenced-by` | reference, sources, agent-memory, agentic-systems, external | the target record, source, or system corroborates, qualifies, or bounds this description |
| `procedure` | instructions | for how to do this, see this instruction |
| `see-also` | reference, notes, agent-memory, agentic-systems, sources, instructions, external | adjacent companion; use sparingly |

## Type eligibility

A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract. Frontmatter-free Markdown is implicit `text`.

## What does NOT belong here

- Transferable claims about KB methodology → `kb/notes/`
- Bounded datasets, experiments, traces, or casebooks whose intended contribution states what they establish about the design space and the limit of that inference → `kb/notes/evidence/`
- Procedures and how-to guidance → `kb/instructions/`
- Descriptions of external systems → `kb/agent-memory-systems/reviews/` for memory/context-engineering systems, or `kb/agentic-systems/` for whole agentic systems and harnesses
- Work in progress → `kb/work/` (workshops)
- Generated operational artifacts → `kb/reports/`
