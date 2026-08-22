# Writing conventions for kb/notes/

## Text contract and explanatory-reach

This collection retains transferable claims about what is true — mechanisms, principles, and arguments that should hold across systems.

Quality goal is **explanatory-reach** — the most general formulation the argument supports, with boundaries mapped. A note with explanatory-reach compresses many situations into one explanation.

Tests for explanatory-reach:
- Change one premise — can you predict the change in the conclusion?
- Would the insight apply in a different domain?
- Could someone say exactly how it's wrong, not just that it's incomplete?
- Does it account for where the pattern actually works and fails, not just why it should?

Notes that only record "X works" are adaptive — useful but brittle. Explaining *why* X works gives explanatory-reach. Explanatory-reach is a direction, not a gate.

Apply explanatory-reach to claim formulation:
- State the claim under the weakest assumptions the argument actually uses.
- Treat qualifiers in the title, description, opening claim, and main proof as obligations. If a qualifier does not change the reasoning when removed, drop it from the claim or move it to an application, corollary, or scope note.
- Keep real boundaries explicit. A boundary belongs in the claim when the argument depends on it; otherwise it belongs in `## Scope`, `## Caveats`, or a nearby narrower application note.
- Prefer a general lemma plus narrower consequences over a narrow lemma whose extra assumptions are only needed by one downstream use.

**Don't defend against objections you've already closed.** A clause that pre-empts a misreading the previous clause already ruled out doesn't add rigor, it pads: "a hypothesis to be tested, not a definitional truth" — being a hypothesis to be tested already means it isn't one. State the claim once; let review catch what still needs defending.

**Admit real gaps instead of hedging around them.** Precision means an agent can't misread the claim — it does not mean stacking qualifications against every conceivable pushback. When the argument has an actual gap — an assumption you can't yet defend, a case you haven't worked through — name it plainly in `## Scope` or `## Open Questions` as an opening for later investigation. A named gap is more useful than one padded shut with defensive language, and it's what review and later notes are for.

**Formulation constraint.** Title and opening argument must be statable in general terms, even when derived from a specific system.

**Theory-independence constraint.** The claim must stand if any single cited description is removed — otherwise it's still a description.

**Design-shaped artifacts need a theoretical claim.** A construction may stay here when it witnesses a substantive truth-apt existential claim. Mark its [residual selections as choices](./artifact-classification-separates-content-kind-lineage-and-authority.md), not as evidence that the selections are uniquely correct. The requirements must be substantive enough that exhibiting any witness is informative; otherwise the unadopted design belongs in `kb/reference/proposals/` under [ADR 028](../reference/adr/028-design-proposals-live-in-reference-proposals.md). Proposal status is a workflow state, not an information kind.

**Hypotheses stay recognizable in prose.** State the conjectural force in the title, description, opening, or a clearly named hypotheses/open-questions section. `user-verified: true` may attest that a note responsibly presents a conjecture; it does not turn the conjecture into established fact.

**Claim modality (ADR 066).** A claim asserts in one of three modes, and the mode determines what refutes it. **Universal** — one genuine counterexample refutes; the default reading for any claim that does not state otherwise. **Statistical** — the claim states a tendency ("usually", "most", "under conditions C"); a single instance does not refute it, prevalence evidence does — and the claim must still forbid something: state the comparison, conditions, or rate that prevalence evidence could refute, or the tendency is vacuous. This stated-refuter requirement is Popper's treatment of probabilistic claims made per-claim: a frequency claim is strictly unfalsifiable until a refuting prevalence is fixed in advance, and here that decision lives in the claim text rather than in a field-wide convention. **Ideal-type** — the claim states a deliberately simple first-order model whose exceptions are conceded and accounted for; what refutes it is an exception the domain treats as ordinary unmarked practice, or the model losing explanatory dominance — see [domain pricing routes an exception to idealization assessment but does not decide it](./domain-pricing-routes-an-exception-to-idealization-assessment.md). Ideal-type acceptance and refutation are comparative — inference to the best explanation with its virtues (declared use, mechanism, bound, dominance) written as attackable commitments rather than reviewer judgment; the bound is absolute, so "best available" alone never suffices. A priced exception is Lakatos's anomaly rather than a refuter: it earns the claim an idealization assessment, and the adequacy record then decides the verdict. Declare the mode in the claim text itself — title, thesis, or a named section; an ideal-type claim carries its adequacy record (declared use, omitted mechanism, consequence bound, explanatory dominance) in the body, where review attacks it like any content. There is no frontmatter mode field: undeclared text reads as universal. Mode is orthogonal to lifecycle stage — a status-conjecture note may conjecture a universal or a tendency; declare both when both apply. Repair under review is mode-aware and runs in both directions: reframing a defeated universal down to statistical or ideal-type requires meeting the target mode's guard, and a claim hedged below its warrant is reframed up, not left vacuous.

## Title and body composability

**Claim titles by default.** Name the note like a claim, not a topic — something that could be true or false.

- *Composability test:* `since [title](./title.md)` or `because [title](./title.md)` reads naturally as prose.
- *Strength test:* the claim is contestable. "Continuous learning can happen outside of weights" passes; "continuous learning is substrate-independent" fails — nobody pushes back.

Add the `title-as-claim` trait when using one, so review gates check the promise.

**Body composability.** Another note should be able to cite this one as a premise without inheriting unrelated claims or examples. If a second cluster would poison imports, split it off or move it to `kb/work/`.

Exception: notes with the `synthesis` trait weave multiple cited claims into a single argument and are cited as a unit. Component claims that need to stand as citable premises should be extracted into their own notes.

Exceptions to claim titles: multi-claim specs, definitions, indexes, and exploratory drafts not ready to assert.

## Outbound links

Author each outbound link from the reader need at its source. A reciprocal link is allowed when the reverse direction independently helps readers; never add one merely to mirror an existing edge. Relationship symmetry describes semantics, not an authoring obligation: `contradicts` and `contrasts` are self-dual, while the other labels are directional. Find inbound links on demand with repository search; no backlink view is currently generated. Inline for strongest commitment, with a connective word that fits the argument (e.g. `since [title](path)`, `because [title](path)`, `but [title](path)`, `as in [title](path)`). Footer for labelled — `- [title](path) — label: context phrase`.

Scan `kb/notes/`, `kb/types/`, `kb/reference/`, `kb/agent-memory-systems/`, `kb/agentic-systems/`, `kb/sources/`, and `kb/instructions/` for link targets. Do not link into `kb/work/` (workshop layer — value is consumed, not imported). Most links land within `kb/notes/` — the densest path. Outbound edges to `kb/instructions/` are rare — the usual direction is inverse (`instruction → note` via `rests-on`) — except `operationalized-from`, recorded as an `Operationalized into:` footer at this collection's methodology note when a procedure in `kb/instructions/` adds ordering, defaults, or stopping conditions the methodology doesn't itself fix; see the lineage semantics in `kb/reference/link-vocabulary.md`. Edges to `kb/sources/` carry the snapshot the claim was abstracted from or that corroborates it.

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
| `evidenced-by` | asym | notes, types, reference, agent-memory, agentic-systems, sources, external | the target observation, case, or source corroborates, qualifies, or bounds this assertion |
| `derived-from` | asym | reference, agent-memory, agentic-systems, sources | claim is worked out from this source, adding nothing beyond it — see the lineage semantics in `kb/reference/link-vocabulary.md` |
| `abstracted-from` | asym | reference, agent-memory, agentic-systems, sources | claim generalizes beyond this source; the source is evidence, authority is earned by testing |
| `operationalized-from` | asym | instructions | procedure adds ordering, defaults, or stopping conditions this methodology note doesn't itself fix; not claim-preserving — see lineage semantics in `kb/reference/link-vocabulary.md` |
| `see-also` | asym | reference, agent-memory, agentic-systems, sources, instructions | adjacent companion; use sparingly |

## Type eligibility

A typed artifact in this collection may use a global type spec under `kb/types/` or a local type spec under this collection's `types/` directory. Its `type:` value is the path to that contract. Frontmatter-free Markdown is implicit `text`.

Definitions of KB vocabulary belong under `kb/notes/definitions/`.

## Evidence placement

Use `kb/notes/evidence/` when a note's primary contribution is what a bounded dataset, experiment, trace cohort, or comparative casebook establishes. These remain theoretical notes under this collection contract: state both the inference the evidence supports and its limit. Put raw captures in `kb/sources/`, descriptions of particular systems or Commonplace episodes in their descriptive collection, and unsettled audits in `kb/work/`.

## What does NOT belong here

- Unadopted system designs → `kb/reference/proposals/` (`design-proposal` type), unless recast as an existential claim per above
- Descriptions of how a specific system works → `kb/reference/` or `kb/agent-memory-systems/`
- Procedures and how-to guidance → `kb/instructions/`
- Raw captures without frontmatter → `text` type, any collection
- Work in progress → `kb/work/` (workshops)
