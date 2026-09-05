# Eigenius contact points: a whole-system witness for the verification-locus theory

Working note. Eigenius (local clone at `related-systems/eigenius/`, gitignored) is an open-source typed knowledge-graph platform for verifiable AI in science. It combines content-addressed immutable layers, four declared epistemic categories (Declared / Observed / Derived / Verified), path-specific commit gates, trace-bearing derivations, justification certificates, and Lean 4 proof checking. Its method docs (`docs/method/reasoning.md`, `docs/method/grounding.md`) and design docs (D39 justification logic, D54 lemma citation, D58 obligation graphs, D61 grounding discovery, D62 encoding pipeline) run this workshop's problem list from the far end of the constraining axis. It belongs beside Build Systems à la Carte, PROV, and in-toto as a literature anchor, but not as those systems already unified without gaps: the [code-grounded whole-system review](../../agentic-systems/reviews/eigenius.md) shows incomplete cache identity, task recovery, ordinary runtime provenance, and proof-to-claim correspondence.

Clone paths below are repo-local pointers, not durable links. The `kb/agentic-systems/` review now owns present-tense implementation claims; this file maps the case into lineage theory and distinguishes implemented controls, host-agent method, and intended design.

## Against the kernel: both bridges, with path-specific guarantees

The verification-locus kernel names two bridges from history to checkable state: records (attestation) and re-derivability (reproducibility). Eigenius's ontology and reasoning method try to operate both simultaneously, with the epistemic category naming the intended warrant:

- **Re-derivability bridge** — Derived and Verified in the design vocabulary. A deterministic program over fully pinned semantic inputs can support the D54 meaning "true relative to the content-addressed data + deterministic method." The current runtime does not make that condition universal: ordinary successful program outputs are stamped Derived, positional replay checks only task position, deterministic cache identity omits component arguments/layer/component version, and ordinary runtime handlers discard their partial `RuntimeInvocation`. Derived therefore records an executed derivation path; stronger reproducibility or factivity depends on the path actually pinning every relevant input.
- **Checked-warrant bridge** — a committed `ReasoningSentence` has a proposition, justification, and certificate checked against `JustifiedBy`; D54 makes the sentence a citable Verified witness. Lean supplies a second verification modality for proof terms, but graph-claim correspondence is conditional on optional anchors. These are checked warrants relative to admitted witnesses and axioms, not unqualified truth about the source world.
- **Record bridge** — Declared and Observed. Declared is intended as explicitly non-factive; Observed is defeasible measurement-with-provenance. Both ultimately require trust in the recorder and the admission path.

The four categories remain a useful **graded factivity vocabulary for the checkable/credence witness split**—finer than our binary regime and attached to claims rather than witness fields—but the category name alone does not enforce its trust condition on every commit path. Candidate borrow for the carried-witness family: a witness can name a factivity grade, provided the producer and validator establish the conditions that grade assumes.

## Trace vs warrant — a distinction our ladder mixes

D39 §12: "reasoning traces describe *what happened* … justification terms describe *with what warrant*." The implementation supports the distinction. A `ProgramTrace` reifies effectful execution; a `ReasoningSentence` carries the proposition, justification term, and checked certificate; the gate's `Verdict` records that the gate ran but is not the proposition-bearer. In our terms, a trace is reified history (an L1 record; journal entry, non-recomputable), while a justification term is a carried witness that makes a state check bounded. Worth naming when the ladder notes are extracted: L1 records answer *what happened*; carried witnesses answer *why believe it*—different consumers, different invalidation.

## They exercise both flagged gaps, but do not close both globally

The two gaps in [verification-locus-and-provenance-theory.md](./verification-locus-and-provenance-theory.md) ("write down, don't build") both have concrete Eigenius counterparts:

- **Gap: radius-1 assay results have unhashed inputs.** Content-addressed layers and explicit proposition/witness keys show how many dependencies can become queryable ("This is a query, not a meeting"—`docs/design/vision.md`). But dependency invalidation is not total in the current implementation: cache identity omits semantic inputs, task replay is positional, and ordinary runtime provenance is incomplete. Eigenius corroborates the value of factored watched edges while also showing that codifying artifacts is insufficient unless execution identities cover every meaning-changing input.
- **Gap: link text is a checkable witness that nothing checks.** Implemented D54 lemma citation is title-as-claim traversal-as-reasoning with a mechanical drift guard: a committed sentence is cited by typed proposition, and a wrong restatement fails to type-check rather than becoming silently unsound. This confirms the gap is real and the fix checks the *carried claim*, not merely pointer health; our cheap-join validator candidate is the natural-language analogue.

Also on citation semantics: "cite the proposition-bearer, never the Verdict" (D54 §4.3) — their verdicts attest "the gate ran and reached this verdict," not the proposition. Independent confirmation of our result-kind stance that review outcomes are execution state, not citable knowledge.

## Against the ladder: an intended no-L0 method, enforced at named boundaries

The `reasoning` method asks a host agent to put every load-bearing claim on the chain with an epistemic grade and warrant, and the manifesto refuses to weaken the type system for adoption. That is an intended no-L0 authoring policy, not a universal property of stored state. `ReasoningSentence` commits through `ValidateJustification` on the institutional load path, while ordinary program outputs skip AutoOnLoad and kernel-emitted follow-up layers can use a lighter pipeline. Several framing and discovery checks are EigenQL queries the host agent must run. Commonplace's graduated ladder makes a different default bet—assign rungs by retroactive reach because total watching is unaffordable over natural-language artifacts—but two parts still transfer:

- **No silent downgrade.** "A derived result can be promoted to verified by attaching a proof, but a verified result cannot be silently downgraded" (`vision.md`). Treat this as a design rule to test before borrowing, not a current global enforcement claim. It remains a candidate rule for freshness baselines and L2 batch decisions: transitions are monotone or recorded, never silent.
- **Production-time enforcement of process contracts.** The Discovered check (D61/D58) is a query-driven step in the host-agent method: it can block the agent from proceeding while a named competency question is ungrounded, but the kernel does not apply it to every commit automatically. This is still Corollary 1's "push out to the skill" exit made concrete—the procedure runs the history-sensitive check when it can matter—rather than proof that history is universally enforced by storage.

## The two-oracle architecture matches the three-layer sieve

D61 and the shipped reasoning method name the limit of codification: "checker-passing ≠ faithful." The certificate checker (oracle #1) establishes that a proposition follows from admitted witnesses under the encoded rules; it does not establish that the formalization captures source intent (oracle #2). The method reports LLM-judge inflation (~97% judge vs ~66% human agreement) and therefore caps mechanized faithfulness checks at Derived, "never auto-Verified." That is a protocol policy. Lean can check a proof term, but correspondence to a graph claim is guaranteed only when the optional mirror/claim/proposition anchors are present and pass. Mapped to the sieve:

| sieve layer | Eigenius counterpart |
|---|---|
| structure → deterministic validator | kernel type/gate checking on the applicable commit path (oracle #1) |
| semantic contract → LLM/human reviewer | faithfulness backstop, grade-capped at Derived unless stronger correspondence is established (oracle #2) |
| process → producer at production time | host-run Discovered query; two-phase vocabulary-first authoring (D39 §4.5) |

The convergence is the finding: a heavily codified system arrives at the same three-way partition from the formal side and still delegates semantic fidelity to judged reading. The method's grade cap is our PASS-verdicts-are-not-endorsements stance stated as an epistemic rule; the code review supplies the additional warning that even deterministic and proof-oriented labels must be interpreted per execution and commit path.

## Non-retrofittability, corroborated

D58: "a separate 'formalize what we built' pass at the end is the anti-pattern—by then the grading is archaeology, not method." And `reasoning.md`: the chain is "the working memory of the reasoning, not a write-up made afterward." Both restate the workshop's one non-deferrable rule—history can only be recorded at the time—as host-agent authoring method rather than a guarantee the runtime can retrofit.

## Model provenance

Their program traces can record the component, output, provider/model identity, token counts, latency, and an input hash on the derivation event. The current component trace does **not** preserve the full prompt or component argument: `argument_hash` is `None`, the deterministic cache key omits the argument, and ordinary runtime handlers discard their partial `RuntimeInvocation`. This supports [model-provenance.md](./model-provenance.md)'s placement—model identity belongs on derivation events, not canonical-artifact frontmatter—while showing that the shipped event record is not yet a complete replay or provenance closure.

## What to take (candidates, for extraction rounds)

1. Add Eigenius to the literature anchors of the verification-locus file when the seedlings grow—it is an agent-operated provenance system rather than a build/supply-chain one, with a manually loaded host-agent method over a typed substrate.
2. Graded factivity as vocabulary for witness regimes (checkable/credence → factive / conditionally factive / defeasible / non-factive), paired with the rule that the grade's assumed conditions must be enforced or evidenced per path.
3. The trace-vs-warrant distinction, named, in the ladder extraction.
4. No-silent-downgrade as an explicit baseline/L2 candidate to validate against the implementation before promotion.
5. The host-run Discovered query as the worked example that some process contracts are enforceable only at production time (strengthens Corollary 1 rather than contradicting it).

---

Relevant notes:

- [Eigenius](../../agentic-systems/reviews/eigenius.md) — see-also: pinned code-grounded authority for the system behavior this workshop maps into lineage theory
- [verification-locus-and-provenance-theory.md](./verification-locus-and-provenance-theory.md) — grounds: the theoretical spine these contact points map onto
- [model-provenance.md](./model-provenance.md) — is-evidence-for: event-side model recording
- [history has one chance to become checkable](../../notes/history-has-one-chance-to-become-checkable.md) — is-evidence-for: their authoring-time chain discipline is the claim practiced as method
- [criteria edits invalidate verdicts; process edits invalidate artifacts](../../notes/criteria-edits-invalidate-verdicts-process-edits-invalidate-artifacts.md) — is-evidence-for: their content-addressed proposition/witness edges show the watched-edge mechanism, while incomplete execution identities expose its boundary
- [a derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — see-also: their drift detectors (D35) enforce the same rule at load time
