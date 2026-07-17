# Receiving vocabulary draft

Wave 0 draft for the migration away from `distillation`. This is not a library artifact yet. Its job is to make the receiving vocabulary precise enough that the audit's hard cases can be classified before any semantic rewrite begins.

**Status (2026-07-17, direction revised):** no successor term will be defined — "derive" stays ordinary English (see the [migration plan](./migration-plan.md)'s minimality constraint). The "candidate definition" sections below are retained as drafted: the derivation and selection material is now source text for the structure note's theory section and the `link-vocabulary.md` label semantics, not for `kb/notes/definitions/` files. The discovery amendment and the hard-case table remain live as written — the classifications now decide which label or citation each case gets, not which defined term.

## Candidate definition: derivation

**Derivation** is the production of a use-shaped artifact whose substantive claims stay inside the claim closure of a source artifact, given the declared consumer goal and any stated premises.

The source is a generator, not merely a reservoir. A derived artifact may change form, register, medium, order, emphasis, or level of operational detail. Those changes do not make it ampliative as long as the resulting claims can be recovered from the source plus the declared targeting premises.

Derivation is therefore graded in prose systems. The ideal is entailment, but the practical test is matching: re-derive from the source and compare the result. Confidence degrades when the source is incoherent, tacit, incomplete, or judgment-heavy. A derived prose artifact is still checked by judgment; it is not mechanically safe merely because it is called derived.

Operational consequences:

- **Matching:** fidelity can be checked by re-deriving and comparing.
- **Fallback:** the retained source can answer uncovered cases by fresh derivation.
- **Cache semantics:** the derived artifact is a recomputable fast path, not a replacement for its generator.
- **Staleness:** when the source changes, the derived artifact is invalidated until rematched or re-derived.

Exclusions:

- Not selection: choosing what to carry forward is separate from producing a consequence.
- Not discovery: a derived artifact does not add a substantive claim outside the source's claim closure.
- Not authored commitment: prose judgment added by the author must be classified separately unless it is itself recoverable from the source.
- Not all transformation: form distance can be large while content distance is zero; the content relation is the classifier.
- Not the ordinary verb: the technical sense binds only through explicit reflective-layer markers (this definition's noun, `Derived from:` link labels, type-spec fields, classification bets). Ordinary "derive" in prose — object-level content in consuming KBs, and object-level or casual usage here — stays plain English and claims no maintenance semantics. See the migration plan's reserved-word policy.

## Candidate definition: selection

**Selection** is consumer-directed choosing: choosing source material, source cases, a validity region, or which consequences of a source are worth deriving for a particular consumer.

Selection carries the targeting that the old `distillation` definition called use-shaping. Derivation is promiscuous: a rich source entails many possible consequences. Selection supplies the criterion for which consequences matter.

Selection is mechanically simple but not epistemically empty. A selection decision often embeds a claim about future use: that these cases, this region, or this procedure will recur often enough to justify a fast path. In the two-layer theory-methodology structure, this is the coverage bet. The selected content may be derived; the decision that this content is worth deriving is usually a discovery-shaped hypothesis about the query distribution.

Verification:

- Source-material selection is checked by provenance: did the selected material come from the stated source?
- Consequence selection is checked by fit: does the selected consequence serve the declared consumer?
- Region selection is checked by use: does the fallback rate show that the covered region is earning its upkeep?

Exclusions:

- Retrieval can implement selection, but selection is the choosing relation, not the retrieval mechanism.
- Selection alone does not assert a new object-level rule. If a selected trace is packaged with a new rule, classify the rule as discovery, derivation, or authored commitment.

## Discovery amendment

The current discovery note is insight-shaped: it emphasizes positing a general and recognizing known particulars as its instances. The migration needs that note to own routine induction too, without flattening discovery into every generalization.

The phased view is not a new Commonplace coinage. It borrows from established discovery literature, especially the Peircean account of scientific inquiry as a cycle of abduction, deduction, and induction: form a hypothesis, derive consequences, then test them. Contemporary discovery-system literature uses different names but keeps the same operational separation: retrieving existing artifacts, searching within a fixed schema, proposing a regime/schema change, and committing only after gates. Commonplace should borrow the phase distinction, not overfit to one author's labels.

Proposed amendment:

**Discovery lifecycle** is the technical term (decided 2026-07-17, per the naming rule in [prose-has-no-scope](../vocabulary-governance/prose-has-no-scope.md): technical terms are multi-word coinages; bare "discovery" stays ordinary English): the staged process by which an ampliative conjecture becomes accepted — posit a claim not entailed by the source, derive its testable consequences, test those consequences against cases, and promote the claim when the tests justify it.

The instant insight case is the degenerate lifecycle where the evidence is already accumulated, so conjecture and recognition appear to co-arise. Trace-to-rule cases are the slower lifecycle: conjecture now, authority later.

Candidate phase vocabulary for Commonplace:

| Phase | Literature analogue | KB operation |
|---|---|---|
| Observation / anomaly | surprising fact, repeated case, unexplained pattern | capture the case without granting rule authority |
| Conjecture | Peircean abduction | posit the candidate rule, mechanism, or general type |
| Consequence derivation | Peircean deduction | derive what should be seen if the conjecture is right |
| Test / accumulation | Peircean induction | compare consequences with cases; gather support and rivals |
| Acceptance / commitment | gated discovery, regime transition | promote the claim, define its boundary, and record its maintenance regime |
| Integration | evidence transport / vocabulary update | reconnect old evidence under the new concept and update affected artifacts |

The compound does double duty: it names the staged view and it spares the bare word — "discovery" in ordinary prose claims nothing technical, while "the discovery lifecycle" and its phase names carry the load-bearing semantics (and the exact string is greppable, so the uniqueness check stays lexical). The conjecture phase is where most AMP traffic enters; accepted status is reached later, not claimed by any ampliative sentence.

The polation axis grades the conjecture:

| Grade | Migration role | Signature |
|---|---|---|
| interpolation / autopolation | derivation, not discovery | output stays inside the source's claim closure |
| extrapolation | routine induction | output extends along dimensions already present in the cases |
| hyperpolation | discovery proper | output posits a new dimension, mechanism, or generative model |

For migration purposes, AMP traffic routes to the conjecture stage of the discovery lifecycle, not automatically to accepted status. The artifact earns authority only through later testing.

Literature anchors for promotion:

- [Peirce: abduction](../philosophy-borrowing/peirce-abduction.md) - local borrowing candidate for observation -> explanatory hypothesis.
- [Charles Sanders Peirce, Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/peirce/) - external grounding for abduction, deduction, and induction as phases of scientific method.
- [Scientific Discovery, Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/scientific-discovery/) - external grounding for discovery as process/product and for the hypothesis-generation/testable-consequence focus.
- [Ingest: Self-Revising Discovery Systems for Science](../../sources/self-revising-discovery-systems-agentic-ai.ingest.md) - modern agentic-science support for retrieval/search/discovery separation and gated commitment.
- [Ord, Interpolation/Extrapolation/Hyperpolation](../../sources/interpolation-extrapolation-hyperpolation.md) - source for grading the ampliative conjecture by polation distance and connecting hyperpolation to abduction.

## Classification bet

When a pipeline has separable stages, split and name the stages. For example: select traces, discover a rule, derive an instruction body from the accepted rule.

When one artifact is entangled and cannot be cleanly split, classify it by its dominant maintenance regime:

- **Derivation-dominant:** maintain by source retention, matching, recomputation, and staleness checks.
- **Discovery-dominant:** maintain by evidence, boundary statements, later tests, and authority earned through use.
- **Selection-dominant:** maintain by provenance, consumer fit, and coverage/fallback checks.
- **Authored-commitment-dominant:** maintain as accumulation or constraining; do not hide the commitment under derivation.

The classification is a falsifiable bet. A "derived" artifact that repeatedly asserts claims the source cannot support was misclassified. A "discovery" artifact whose content is later shown to be entailed by the source can be downgraded to derivation and maintained more cheaply.

## Distillation control trap

The migration has a control failure mode: a use-shaped artifact feels controlled because it is compact and executable, while the term `distillation` hides which maintenance regime actually controls it. Selection, derivation, discovery, and authored commitment all produce useful downstream artifacts; they do not earn authority through the same checks.

The diagnostic is now split out in [distillation-control-trap.md](./distillation-control-trap.md). Operationally, every former `distillation` case must answer "what controls this artifact?" before it is renamed. Otherwise the migration can recreate the same mistake under a stricter term by letting selection, conjecture, or authored judgment borrow derivation's matching/recompute semantics.

## Hard-case checks

| Case | Classification under this draft | Why |
|---|---|---|
| Source article -> claim summary | selection + derivation | choose claim-relevant material, then preserve it in a consumer-shaped register |
| Methodology notes -> skill body | selection + derivation | choose the workflow and derive executable steps from the methodology plus the agent's task |
| Workshop -> note | mixed | derived if the note preserves an already-settled claim; discovery if the note posits a new general claim |
| Repeated review failures -> gate instruction | selection + discovery + derivation | select failures, conjecture the common failure mode, derive the gate wording from the accepted rule |
| Single verified trace -> preference rule | discovery-dominant | the universal or bounded rule is not entailed by the single trace |
| `write-instruction.md` repeated operations -> stable procedure | selection + discovery, then derivation where methodology exists | the stable core is an extrapolative claim; the final procedure can be derived from that accepted core and any companion methodology |
| `distillation-is-transformation-not-selection.md` | split | anti-mere-selection survives; trace-to-rule examples are discovery evidence, not derivation evidence |
| "Ad-hoc distillation" as source selection plus packaged judgment | authored commitment unless generalized and tested | judgment additions are not entailed by selection itself |
| Two-stage agent-memory pipelines | split stages | summaries and stats can be derivation; lessons, rules, and playbooks are usually discovery |
| ML knowledge distillation | external term, mostly out of migration scope | the external term remains; inside KB vocabulary it is statistical fitting, not entailment-preserving derivation |

## Acceptance test before Wave 1

Do not start semantic rewrites until the promoted vocabulary can satisfy these checks:

1. Every non-META audit class has a receiving home: selection, derivation, discovery, or authored commitment.
2. The trace-to-rule ladder can be rewritten without using `distillation` as a hidden bridge term.
3. `discovery` can receive routine induction without making accepted discovery and untested conjecture indistinguishable.
4. `selection` explicitly carries consumer-directedness and the coverage bet.
5. The definitions explain why a large form change can still be derivation, while a small wording change can be discovery if it adds a claim.
6. Each semantic rewrite names the artifact's control regime rather than treating use-shapedness itself as authority.

## Promotion shape

Likely library outputs (revised under the no-successor-term direction — zero new defined terms):

- the two-layer structure note in `kb/notes/`, carrying the theory as citable claims: graded entailment-preservation, matching, fallback, cache/staleness semantics, plus the selection material (consumer-directedness, the coverage bet) and the classification bet
- the `Derived from:` / `Derived into:` label semantics in `kb/reference/link-vocabulary.md` (no-added-claims assertion; discovery-side label for ampliative lineage), with `cp-skill-write` updated to match
- an amendment to `kb/notes/discovery-is-seeing-the-particular-as-an-instance-of-the-general.md`, or a separate discovery definition note if the existing title-as-claim note should not carry definition load

The structure note and the discovery amendment promote together — the moment the old term stops covering ampliative traffic, discovery must already own it.
