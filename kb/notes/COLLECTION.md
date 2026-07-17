# Writing conventions for kb/notes/ (theoretical profile)

## Text contract and reach

Theoretical [profile](./definitions/text-contract.md): transferable claims about what is true — mechanisms, principles, arguments that should hold across systems.

Quality goal is **reach** — the most general formulation the argument supports, with boundaries mapped. A note with reach compresses many situations into one explanation.

Tests for reach:
- Change one premise — can you predict the change in the conclusion?
- Would the insight apply in a different domain?
- Could someone say exactly how it's wrong, not just that it's incomplete?
- Does it account for where the pattern actually works and fails, not just why it should?

Notes that only record "X works" are adaptive — useful but brittle. Explaining *why* X works gives reach. Reach is a direction, not a gate.

Apply reach to claim formulation:
- State the claim under the weakest assumptions the argument actually uses.
- Treat qualifiers in the title, description, opening claim, and main proof as obligations. If a qualifier does not change the reasoning when removed, drop it from the claim or move it to an application, corollary, or scope note.
- Keep real boundaries explicit. A boundary belongs in the claim when the argument depends on it; otherwise it belongs in `## Scope`, `## Caveats`, or a nearby narrower application note.
- Prefer a general lemma plus narrower consequences over a narrow lemma whose extra assumptions are only needed by one downstream use.

**Don't defend against objections you've already closed.** A clause that pre-empts a misreading the previous clause already ruled out doesn't add rigor, it pads: "a hypothesis to be tested, not a definitional truth" — being a hypothesis to be tested already means it isn't one. State the claim once; let review catch what still needs defending.

**Admit real gaps instead of hedging around them.** Precision means an agent can't misread the claim — it does not mean stacking qualifications against every conceivable pushback. When the argument has an actual gap — an assumption you can't yet defend, a case you haven't worked through — name it plainly in `## Scope` or `## Open Questions` as an opening for later investigation. A named gap is more useful than one padded shut with defensive language, and it's what review and later notes are for.

**Formulation constraint.** Title and opening argument must be statable in general terms, even when derived from a specific system.

**Theory-independence constraint.** The claim must stand if any single cited description is removed — otherwise it's still a description.

**Existential recast for designs.** A design idea is not a weak claim — its free parameters make it evaluable by usefulness, not truth (rationale: [design proposals differ from claims in kind, not confidence](./design-proposals-differ-from-claims-in-kind-not-confidence.md)). It may stay here only recast as an existential claim: the title carries the truth-apt part, and the construction appears as a witness with its free choices explicitly marked. The requirements must be substantive enough that exhibiting any witness is informative; otherwise the design belongs in `kb/reference/proposals/` (ADR 028).

**Hypotheses stay recognizable in prose.** State the conjectural force in the title, description, opening, or a clearly named hypotheses/open-questions section. `user-verified: true` may attest that a note responsibly presents a conjecture; it does not turn the conjecture into established fact.

## Title and body composability

**Claim titles by default.** Name the note like a claim, not a topic — something that could be true or false.

- *Composability test:* `since [title](./title.md)` or `because [title](./title.md)` reads naturally as prose.
- *Strength test:* the claim is contestable. "Continuous learning can happen outside of weights" passes; "continuous learning is substrate-independent" fails — nobody pushes back.

Add the `title-as-claim` trait when using one, so review gates check the promise.

**Body composability.** Another note should be able to cite this one as a premise without inheriting unrelated claims or examples. If a second cluster would poison imports, split it off or move it to `kb/work/`.

Exception: notes with the `synthesis` trait weave multiple cited claims into a single argument and are cited as a unit. Component claims that need to stand as citable premises should be extracted into their own notes.

Exceptions to claim titles: multi-claim specs, definitions, indexes, and exploratory drafts not ready to assert.

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
| `evidence` | asym | reference, agent-memory, agentic-systems, sources | this observation corroborates the claim |
| `derived-from` | asym | reference, agent-memory, agentic-systems, sources | claim is worked out from this source, adding nothing beyond it — see the lineage semantics in `kb/reference/link-vocabulary.md` |
| `abstracted-from` | asym | reference, agent-memory, agentic-systems, sources | claim generalizes beyond this source; the source is evidence, authority is earned by testing |
| `see-also` | asym | reference, agent-memory, agentic-systems, sources, instructions | adjacent companion; use sparingly |

## Types

| type | file | use for |
|---|---|---|
| `note` | `kb/types/note.md` | transferable theoretical notes |
| `structured-claim` | `./types/structured-claim.md` | developed arguments with explicit evidence and reasoning sections |
| `definition` | `kb/types/definition.md` | KB vocabulary under `kb/notes/definitions/` |
| `tag-readme` | `kb/types/tag-readme.md` | a tag's curated head (`<tag>-README.md`); weight-gated, with optional validator-enforced `complete`/`covered_by` marks |
| `index` | `kb/types/index.md` | build-time generated listings only — do not author new committed indexes |

## What does NOT belong here

- Unadopted system designs → `kb/reference/proposals/` (`design-proposal` trait), unless recast as an existential claim per above
- Descriptions of how a specific system works → `kb/reference/` or `kb/agent-memory-systems/`
- Procedures and how-to guidance → `kb/instructions/`
- Raw captures without frontmatter → `text` type, any collection
- Work in progress → `kb/work/` (workshops)
