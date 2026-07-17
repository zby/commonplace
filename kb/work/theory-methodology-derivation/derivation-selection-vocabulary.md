# Vocabulary: derivation, selection, and what happens to distillation

The vocabulary thread. Two moves are on the table, the second strictly stronger than the first.

## Move 1: derivation as a named subtype of distillation

The current [distillation definition](../../notes/definitions/distillation.md) is deliberately silent on the logical relation between source and distillate — it requires only provenance and use-shaping. **Derivation** is the subtype where the source *entails* the distillate: the theory is a generator, not a reservoir. That one added property buys three operational consequences, which is what makes it worth naming:

1. **Fidelity becomes checkable.** A generic distillate can only be judged consumer-facing ("does it serve the use?" — semantic judgment). A derived distillate has an agreement condition: re-derive and compare (physics' matching). Derivation moves distillate verification up the [oracle-strength spectrum](../../notes/oracle-strength-spectrum.md) — derived content can be gated, not just critiqued.
2. **Fallback is licensed.** Only a generator source can answer questions the distillate lacks. Re-deriving a corner case from a theory is computation from principles; going back to a pile of ingested sources is retrieval plus fresh reasoning. The whole [two-layer architecture](./two-layer-theory-methodology.md) is only available for the derivation subtype — and only derivation forces the source to stay shipped rather than archived.
3. **Cache semantics.** A derived distillate is recomputable, hence in principle never load-bearing — exactly the semantics the KB already gives **marks** in `kb/types/tag-readme.md` ("recomputable, so never load-bearing; enforced-or-omitted, because a stale trusted cache is a trap"). A derived methodology is a mark writ large. On theory revision, derived content is invalidated-but-recomputable, which plugs into [make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) differently than ordinary distillate staleness does.

Caveat: in prose media, entailment is checked by an LLM judge, so derivation is *graded* — the payoffs arrive in proportion to source coherence and entailment checkability. The definition should state entailment as the ideal that checkability degrades away from, or it overclaims.

## Move 2: decompose distillation into selection + derivation

Proposal (current position): for economy of terms, most uses of "distillation" could be replaced. Distillation becomes **consumer-directed selection, then derivation**. Selection is the simple part; derivation carries the logical relation.

Pressure-testing against the distillation definition's own instances table:

| Instance | Decomposes? |
|---|---|
| source article → claim summary | yes: claim-level selection + paraphrase (degenerate derivation — mutual entailment, register change) |
| methodology → skill | yes: select the workflow, derive the procedure given the consumer's goal as a premise |
| workshop → note | only when the note adds no claims; where synthesis posits a new general claim, that step is ampliative |
| repeated review failures → gate instruction | **no**: particulars → rule is induction; no amount of selection makes the rule entailed |

The failures of decomposition are the interesting result: the current "distillation" quietly bundles truth-preserving reshaping with **ampliative generalization**. The decomposition forces the ampliative cases out — and the KB already has the receiving concept: [discovery](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md). Failures→gate becomes: *select* the failures, *discover* the pattern, *derive* the rule. Three primitives with distinct verification semantics: selection checkable by provenance, derivation by matching, discovery only by subsequent testing.

**The workshop→note case in practice** (operator position): the decomposition could be kept clean by forcing the inductive step to happen inside the workshop — so that writing the note from the workshop is pure selection + derivation. In practice we mostly just skip that separation; the induction happens implicitly wherever it happens. Worth deciding whether "discovery happens in the workshop, the note is derived from it" becomes an actual convention in the `kb/work/` contract or stays a descriptive observation.

## What needs settling before migration

1. **Where consumer-directedness lives.** It is the load-bearing part of the current definition, and neither primitive carries it by default. Derivation from a theory is promiscuous — infinitely many things are entailed. Proposal: selection is always *selection-for* — the consumer's need is the criterion, applied both to source material and to which consequences are worth deriving. If so, selection is "simple" but doing real work and needs its own half-page definition.
2. **Whether "distillation" keeps a job.** The composite (consumer-directed selection + derivation) is the KB's most common operation; common composites usually earn a one-word name. But the name could be a defined phrase inside the primitives' notes rather than a primitive of its own.
3. **Churn inventory.** The term is in the CLAUDE.md vocabulary, a definition note, the `distillation` tag (in learning-theory's `covered_by`, with its own tag-README), and note titles. `skills-derive-from-methodology-through-distillation.md` becomes *cleaner* under the new scheme; other usages need classification.
4. **Loss of the ML bridge.** The definition currently rides on the resonance with Hinton-style knowledge distillation (teacher→student is statistical fit, not entailment — it would classify as selection-heavy, derivation-poor). Renaming weakens that bridge; the definition already flags the ML sense as distinct, so the cost may be small.

## Next action: usage audit

Per the KB's worked-case-first norms (and Carnap explication, which is on the [philosophy-borrowing](../philosophy-borrowing/README.md) candidate list — sharpening the loose existing "derive" usage into a technical term *is* explication): sweep actual `distillation`/`distill` usage across `kb/`, classify each instance as selection / derivation / ampliative(discovery), and let the tallies show whether the word retains a job. The audit output lands in this directory and is the evidence the eventual definition rewrite or ADR cites.

---

Working links:

- [distillation](../../notes/definitions/distillation.md) — tests: the definition whose instance table the decomposition is checked against
- [constraining](../../notes/definitions/constraining.md) — depends-on: constraining stays orthogonal under the new scheme (a derived methodology can still be prose)
- [discovery is seeing the particular as an instance of the general](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — mechanism: receives the ampliative residue the decomposition forces out of distillation
- [skills derive from methodology through distillation](../../notes/skills-derive-from-methodology-through-distillation.md) — tests: existing loose use of "derive"; first worked example or naming collision to resolve
- [oracle strength spectrum](../../notes/oracle-strength-spectrum.md) — grounds: what "fidelity becomes checkable" means
- [make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — extends: derived-content staleness is invalidate-and-recompute
