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

## Usage audit — done

Per the KB's worked-case-first norms (and Carnap explication, which is on the [philosophy-borrowing](../philosophy-borrowing/README.md) candidate list — sharpening the loose existing "derive" usage into a technical term *is* explication), the sweep ran on 2026-07-17: see [distillation-usage-audit.md](./distillation-usage-audit.md). Headline: 464 instances; excluding META, library usage is derivation-dominant (DER 48 / AMP 24 / SEL 12 in notes+reference+instructions) but the agent-memory-systems collection's substantive usage is ampliative-dominant (62 AMP / 39 DER), the distillation definition's own instance list spans the DER/AMP boundary, and the trace→rule oracle-theory cluster — the KB's most load-bearing "distill" usage — is exactly the ampliative traffic that would route to discovery. The audit also found a component with no slot in the two-primitive decomposition: authored judgment ("ad-hoc distillation" = selection + packaged judgment), and confirmed derivation must be defined as graded (even DER distillates are re-verified by judgment, per `a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`).

## Sequencing (post-audit)

Operator direction: **split the ampliative cases out first, without a full rename.** The boundary fix is independently correct whatever happens to the word "distillation", and once the ampliative traffic is out, the remaining rename (derivation/selection) becomes near-mechanical.

One design question inside the split — where does the ampliative traffic go? [Discovery's definition](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) is insight-shaped: a dual structure of positing a general *and* recognizing existing particulars as its instances, with recognition as the hard problem. Much of the audited AMP traffic is routine induction (repeated failures → gate rule; one verified episode → bounded rule per [abstract-an-experience](../../notes/abstract-an-experience-only-when-you-can-state-the-boundary.md)), not co-arising insight. Options: (a) extend discovery to own the routine end explicitly; (b) name the ampliative operation itself (abstraction / induction — "abstraction" is already in KB use for the trace→rule move) and position discovery as its high-reach end. Routing everything to "discovery" unmodified risks overloading that term the way distillation is currently overloaded.

**The bet doctrine for judgment cases** (assistant proposal — not to be confused with the operator's *coverage* bet, which is about whether creating a derived layer is warranted at all and lives in the [two-layer thread](./two-layer-theory-methodology.md#the-derivation-bet-operator-position)): mixed and judgment-heavy instances do not get a hybrid category. Where a pipeline has separable stages, split and name the stages (the audit's two-stage pattern: DER stage feeding an AMP stage). Where one artifact is entangled, classify it by the regime bet to be *dominant* — an explicit, falsifiable commitment that fixes the artifact's maintenance and verification semantics (derivation-dominant → matching/recompute discipline; ampliative-dominant → discovery-style testing). A wrong bet has a detection signature: a "derived" artifact that keeps asserting claims the source can't back was ampliative; an "ampliative" rule that turns out entailed is a cheap upgrade to derivation. This is the same shape as "every codification is a bet" (and the promotion bets in the [inductive-bias thread](./methodology-as-inductive-bias.md)) — classification bets and promotion bets are adjudicated the same way, by later behavior. The bet also covers the authored-judgment gap pragmatically: the bet is about the artifact's dominant maintenance regime, not a claim that no foreign content is present.

Order of work: (1) boundary split — rewrite the distillation definition to exclude ampliative steps, move its AMP instances out, settle the discovery-vs-abstraction routing question, relabel or annotate the trace→rule ladder's "Distill" rung; (2) ship the bet doctrine with the split as its classification rule; (3) only then revisit the derivation/selection rename over what remains.

## Discovery is a lifecycle, not an act (operator refinement of the routing)

Routing the ampliative traffic to "discovery" is awkward in one respect: formulating a hypothesis is only *part* of a discovery — it still needs testing. Sometimes the examples are already at hand and promotion is effectively instant (the discovery note's co-arising structure: positing the general and recognizing the instances happen together, because the instances were pre-accumulated). But often it is a long process: conjecture now, evidence later.

Peirce — already the abduction candidate in [philosophy-borrowing](../philosophy-borrowing/README.md) — dissolves this cleanly, because his full inference scheme is a pipeline: **abduction** (posit the hypothesis) → **deduction** (derive its testable consequences) → **induction** (test them against cases). Two things follow:

1. The ampliative *act* is abduction/conjecture; "discovery" properly names the lifecycle's success state, reached only after testing. The instant-promotion case is the degenerate lifecycle where conjecture and test collapse because the evidence pre-exists.
2. The middle stage of Peirce's pipeline is *derivation* — this workshop's term. Testing a conjecture requires deriving its consequences. So the vocabulary's two operations aren't just siblings; they compose: discovery consumes derivation as its verification step.

The KB already implements the lifecycle view operationally: [trace-derived memory earns authority per operation, not at capture](../../notes/trace-derived-memory-earns-authority-per-operation-not-at-capture.md) — the hypothesis is captured immediately, its discovery-status is earned later, per test. And the bet doctrine generalizes: all three bets in this workshop (correctness, coverage, classification) are conjectures with named adjudicators — discoveries-in-progress with different test harnesses.

Implication for Wave 0 of the [migration plan](./migration-plan.md): the discovery amendment should define discovery as a staged lifecycle (conjecture → derived consequences → test → acceptance), with the polation axis grading the conjecture's distance and the instant case as pre-accumulated evidence. AMP traffic routes to the *conjecture stage*, not to the honorific.

## Ord's polation triple grades the ampliative side

Split out to its own thread: [the polation structure of generalization](./polation-structure-of-generalization.md). Upshot for this thread: derivation ≈ interpolation, routine induction ≈ extrapolation, discovery proper ≈ hyperpolation; the carving settles the routing question toward extending discovery (the polation axis is its internal grading, routine induction its shallow end) and formalizes the bet doctrine (classification is a bet about where an artifact's claims sit relative to its source, with verification burden scaling off-manifold).

---

Working links:

- [distillation](../../notes/definitions/distillation.md) — tests: the definition whose instance table the decomposition is checked against
- [constraining](../../notes/definitions/constraining.md) — depends-on: constraining stays orthogonal under the new scheme (a derived methodology can still be prose)
- [discovery is seeing the particular as an instance of the general](../../notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md) — mechanism: receives the ampliative residue the decomposition forces out of distillation
- [skills derive from methodology through distillation](../../notes/skills-derive-from-methodology-through-distillation.md) — tests: existing loose use of "derive"; first worked example or naming collision to resolve
- [oracle strength spectrum](../../notes/oracle-strength-spectrum.md) — grounds: what "fidelity becomes checkable" means
- [make-like staleness detection](../../notes/link-graph-plus-timestamps-enables-make-like-staleness-detection.md) — extends: derived-content staleness is invalidate-and-recompute
