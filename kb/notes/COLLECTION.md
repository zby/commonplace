# Writing conventions for kb/notes/ (theoretical register)

## Register and reach

Theoretical [register](./definitions/register.md): transferable claims about what is true — mechanisms, principles, arguments that should hold across systems.

Quality goal is **reach** — the most general formulation the argument supports, with boundaries mapped. A note with reach compresses many situations into one explanation.

Tests for reach:
- Change one premise — can you predict the change in the conclusion?
- Would the insight apply in a different domain?
- Could someone say exactly how it's wrong, not just that it's incomplete?

Notes that only record "X works" are adaptive — useful but brittle. Explaining *why* X works gives reach. Reach is a direction, not a gate.

**Formulation constraint.** Title and opening argument must be statable in general terms, even when derived from a specific system.

**Theory-independence constraint.** The claim must stand if any single cited description is removed — otherwise it's still a description.

## Title and body composability

**Claim titles by default.** Name the note like a claim, not a topic — something that could be true or false.

- *Composability test:* `since [title](./title.md)` or `because [title](./title.md)` reads naturally as prose.
- *Strength test:* the claim is contestable. "Continuous learning can happen outside of weights" passes; "continuous learning is substrate-independent" fails — nobody pushes back.

Add the `title-as-claim` trait when using one, so review gates check the promise.

**Body composability.** Another note should be able to cite this one as a premise without inheriting unrelated claims or examples. If a second cluster would poison imports, split it off or move it to `kb/work/`.

Exception: notes with the `synthesis` trait weave multiple cited claims into a single argument and are cited as a unit. Component claims that need to stand as citable premises should be extracted into their own notes.

Exceptions to claim titles: multi-claim specs, definitions, indexes, seedlings not ready to assert.

## Outbound links

Forward-authored, asymmetric unless marked symmetric; backlinks are computed. Inline for strongest commitment, with a connective word that fits the argument (e.g. `since [title](path)`, `because [title](path)`, `but [title](path)`, `as in [title](path)`). Footer for labelled — `- [title](path) — label: context phrase`.

Scan `kb/notes/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/sources/`, and `kb/instructions/` for link targets. Do not link into `kb/work/` (workshop layer — value is consumed, not imported). Most links land within `kb/notes/` — the densest path. Outbound edges to `kb/instructions/` are rare; the usual direction is inverse (`instruction → note` via `rationale`). Edges to `kb/sources/` carry the snapshot the claim was abstracted from or that corroborates it.

**Labels:**

| label | kind | destinations | reader-need |
|---|---|---|---|
| `extends` | asym | notes | wants the argument developed further |
| `grounds` | asym | notes | wants to verify the premise |
| `enables` | asym | notes | wants the operational prerequisite |
| `exemplifies` | asym (instance→general) | notes | wants the general claim this instance falls under |
| `mechanism` | asym | notes | wants to understand how the claim operates |
| `contradicts` | sym | notes | wants to resolve a disagreement |
| `contrasts` | sym | notes | wants the neighbouring-shape distinction |
| `defined-in` | asym | notes/definitions | reader may not know the term |
| `evidence` | asym | reference, agent-memory, sources | this observation corroborates the claim |
| `derived-from` | asym | reference, agent-memory, sources | claim was abstracted from this source |
| `see-also` | asym | reference, agent-memory, sources, instructions | adjacent companion; use sparingly |

## Types

| type | file | use for |
|---|---|---|
| `note` | `kb/types/note.md` | transferable theoretical notes |
| `structured-claim` | `./types/structured-claim.md` | developed arguments with explicit evidence and reasoning sections |
| `definition` | `kb/types/definition.md` | KB vocabulary under `kb/notes/definitions/` |
| `index` | `kb/types/index.md` | curated or generated navigation hubs |

## What does NOT belong here

- Descriptions of how a specific system works → `kb/reference/` or `kb/agent-memory-systems/`
- Procedures and how-to guidance → `kb/instructions/`
- Raw captures without frontmatter → `text` type, any collection
- Work in progress → `kb/work/` (workshops)
