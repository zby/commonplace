---
description: "Conjecture: discovery-verification asymmetry means discriminating, boundary-exposing examples can retain value across model upgrades even as stronger models absorb familiar abstract principles."
type: types/note.md
traits: [title-as-claim, has-comparison]
tags: [learning-theory, document-system, curation]
---

# Discriminating examples may outlast principles across upgrades

*Conjecture expanding the preserved-search-work thread in [model upgrades obsolete notes by function rather than uniformly](./model-upgrades-obsolete-notes-by-function-rather-than-uniformly.md).*

Across model upgrades, well-chosen concrete examples may retain their value better than standalone abstract principles. Stronger models can often reproduce and apply familiar principles unaided, eroding the marginal value of prose restating those principles. By contrast, a discriminating example can preserve substantial search work that an upgrade does not automatically nullify.

## Discovery–verification asymmetry resists model upgrades

The mechanism behind this conjecture is an **asymmetry between discovery and verification**. Finding a crisp case that separates competing explanations, refutes an attractive generalization, or exposes an unexpected boundary requires open-ended search across a large design space. Checking that case once it is written down is cheap: any reader can inspect its conditions, re-derive the conflict or decision flip, and see where the boundary sits. [ADR 091](../reference/adr/091-refutation-needs-a-checkable-counterexample-corroboration-a-test.md) relies on the same property when treating a specified counterexample as reproducible because any reader can re-derive the conflict.

Retaining a high-asymmetry example caches the expensive discovery step and hands the cheap verification step to every future reader:

- **Bounded sessions still miss edge cases.** Even a stronger model does not automatically search out every non-obvious counterexample or subtle failure mode during routine work unless something brings that case to mind.
- **Stronger readers verify and exploit good cases better.** Once a discriminating case is supplied, a stronger model can check the inference, avoid the trap, and generalize from the boundary more reliably than a weaker model could.
- **Good cases survive revision of the principle itself.** If a stronger model replaces a flawed or over-general rule with a better explanation, a well-chosen case or recorded failure still stands as an adequacy constraint that the successor theory must handle ([retaining episode evidence keeps a distilled rule open to re-examination](./retaining-episode-evidence-keeps-a-distilled-rule-open-to.md)).

## What the asymmetry separates

The asymmetry does not favor concreteness in general or make abstract principles obsolete. It separates which examples and which principles stay durable:

- **Durable examples are hard to find, locally plausible, and cheap to verify.** Three kinds fit best:
  - *Minimal decision pairs* where changing one condition flips the verdict, such as the two-commute veto table in [a veto can block outranking without deciding the reverse](./a-veto-can-block-outranking-without-deciding-the-reverse.md).
  - *Discriminating contrasts between competing mechanisms*, such as the intervention separating two observationally equivalent causal models in [competing causal theories can guide distinguishing experiments](./competing-causal-theories-can-guide-distinguishing-experiments.md), or temperature masking versus repair in [LLM output deviation requires three-way diagnosis](./llm-output-deviation-requires-three-way-diagnosis.md).
  - *Recorded empirical surprises* whose local facts cannot be derived from model priors alone.
  To keep probing real boundaries rather than straw-men, a boundary example should be *locally defensible*—carrying the same surface alibi that actually fools a reader or reviewer ([calibrating semantic gates against labelled fixtures](../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md)). Whereas [abstracting an experience only when you can state its boundary](./abstract-an-experience-only-when-you-can-state-the-boundary.md) keeps an instance when its boundary is not yet statable, this conjecture keeps a discriminating example *even after* the boundary is stated because rediscovering that case stays costly.
- **Stock, opaque, and environment-brittle examples decay fast.** A predictable toy illustration of a familiar principle has low discovery cost; a stronger model can generate an equivalent one on demand, leaving the retained copy as clutter. An anecdote missing the premises needed to re-derive why it behaves as claimed forfeits cheap verification ([a checked outcome licenses retaining an episode, not abstracting its explanation](./checked-outcome-licenses-episode-retention-not-abstraction.md)). An example tied to volatile repository internals can go stale faster than the principle it illustrates.
- **Abstract principles still do work examples cannot replace.** An example alone does not say which invariant transfers to unseen domains or where its boundary stops. The abstract claim states that boundary, lets a reader vary premises to predict new cases ([first-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md)), and names the shared structure for cheaper lookup ([recognition, not linking, is the hard problem in knowledge systems](./recognition-not-linking-is-the-hard-problem-in-knowledge-systems.md)). Principles carrying unfamiliar mechanisms, local commitments, or contextual recognition cues also resist simple absorption because [knowledge storage does not imply contextual activation](./knowledge-storage-does-not-imply-contextual-activation.md).

## Implications for note selection and authoring

If this conjecture holds, it shifts both how notes are valued and how important abstract ideas should be authored:

- **Value notes by preserved search cost, not abstraction altitude.** A concise worked contrast or boundary case can retain more value across upgrades than an abstract restatement whose claims stronger models already supply. Do not rank concrete notes lower merely because their surface is less general, and do not assume design principles have zero obsolescence ([notes need quality scores to scale curation](./notes-need-quality-scores-to-scale-curation.md)).
- **Screen abstract claims for a concrete discriminator.** An abstract note that cannot name a case where it rules out a rival, changes a decision, or exposes a boundary is weak under both [warranted reader update](./warranted-reader-update-is-the-objective-of-substantive-writing.md) and [generality bought to avoid counterexamples is paid for in precision](./generality-bought-to-avoid-counterexamples-is-paid-for-in.md).
- **Apply the same filter to examples.** Admit or retain an example when it is hard to discover and cheap to verify; reject stock illustrations that merely repeat a principle in longer form.
- **Develop discriminating examples for important abstract ideas.** Pairing a key abstract claim with a minimal pair or checkable counterexample pays twice: at authoring time it stress-tests the claim and catches hidden boundaries before other notes build on it, and across upgrades it preserves the hardest-to-rediscover intellectual work beside the named invariant.
- **Write examples for cheap, durable verification.** State the assumptions, competing predictions, and flipping condition explicitly so a later reader can re-derive the verdict without hidden context. Prefer minimal constructed contrasts, which do not rot with codebase churn, or dated, explicitly scoped empirical records over live-repo details that quietly drift.
- **Preserve composability when placing examples.** Keep short boundary-defining examples inline inside `kb/theory/` notes, where they localize abstraction and earn their space under [detail overhang](../instructions/compression-bundle/detail-overhang.md) by carrying a load-bearing contrast. Place fuller worked comparisons, arithmetic breakdowns, or multi-case testbeds in linked companion notes (such as standalone worked examples in `kb/notes/` or bounded casebooks in `kb/theory/evidence/`) so premise notes preserve body composability under [`COLLECTION.md`](./COLLECTION.md).
- **Target high-leverage ideas instead of blanket quotas.** Requiring an example on every abstract note invites low-asymmetry filler that adds context and maintenance cost. Focus first on high-centrality concepts, contested distinctions, claims with subtle failure boundaries, and principles that agents repeatedly misapply.

## Scope

- This claim is a conjecture, not an established cross-generation trend. Its survival advantage depends on the discovery–verification gap remaining wide enough under stronger models that retaining a case beats rediscovering it in-session.
- The conjecture does not argue for example-only notes. The strongest durable unit is often a concise named claim paired with a checkable discriminating example.
- Guiding examples and held-out test cases play different roles. An example embedded in a note or prompt orients the reader, which spends it as an independent detection test; regression checking across upgrades needs non-leaking held-out fixtures ([calibrating semantic gates against labelled fixtures](../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md)).
- A concrete example that fails to state its scope or assumptions can mislead just as easily as an over-general principle.

## Open Questions

- **Longitudinal counterfactual test.** Across model upgrades, does withholding an abstract principle lose marginal lift faster than withholding its discriminating example? Testing this requires cross-generation ablations (no note, principle alone, example alone, and both) following [a linked note's durable payload](./linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) and [ablation baselines for the declared objective](../reference/proposals/ablation-baselines-for-the-declared-objective.md), while accounting for public-corpus contamination if newer models train on the KB itself.
- **Stronger-model search.** Stronger models also get better at finding counterexamples and edge cases unaided; for which classes of problems does the discovery–verification gap stay wide enough to justify retaining examples?
- **Activation efficiency per token.** When a stronger model already knows a principle in weights, does a terse claim plus recognition condition or a concrete discriminating example activate the distinction more reliably per token in live work?
- **Maintenance cost versus preserved search.** How should a KB prioritize which important abstract ideas warrant dedicated companion examples first, and when does maintaining real-system examples cost more than the search work they preserve?

---

Relevant Notes:

- [Model upgrades obsolete notes by function rather than uniformly](./model-upgrades-obsolete-notes-by-function-rather-than-uniformly.md) — extends: expands the preserved-search-work thread of what survives across model upgrades
- [Retaining episode evidence keeps a distilled rule open to re-examination](./retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) — grounds: explains why retained cases survive revision of the abstracted rule and supports rule-versus-case ablation comparisons
- [Generality bought to avoid counterexamples is paid for in precision](./generality-bought-to-avoid-counterexamples-is-paid-for-in.md) — grounds: argues for stating the general form once and letting scope lines and worked instances carry the range
- [A linked note's durable payload is what its consumption path cannot reliably supply](./linked-note-durable-payload-is-what-consumption-path-cannot-supply.md) — extends: supplies the behavioral ablation test for measuring durable payload across consumer generations
- [Warranted reader update is the objective of substantive writing](./warranted-reader-update-is-the-objective-of-substantive-writing.md) — grounds: defines note value relative to what the intended reader already supplies
- [A checked outcome licenses retaining an episode, not abstracting its explanation](./checked-outcome-licenses-episode-retention-not-abstraction.md) — contrasts: shows why an opaque episode without faithful process premises fails cheap verification
- [First-principles reasoning selects for explanatory-reach over adaptive fit](./first-principles-reasoning-selects-for-explanatory-reach-over.md) — contrasts: explains the transfer and premise-variation work that abstract claims supply and bare examples cannot replace
- [ADR 091: Refutation needs a checkable counterexample, and corroboration needs a test](../reference/adr/091-refutation-needs-a-checkable-counterexample-corroboration-a-test.md) — evidenced-by: treats a specified counterexample as reproducible because any reader can re-derive the conflict
- [Detail overhang](../instructions/compression-bundle/detail-overhang.md) — see-also: compression gate separating load-bearing boundary examples from illustrative over-elaboration
- [Information value is observer-relative](./information-value-is-observer-relative.md) — grounds: note value depends on what the consuming model already supplies from priors and compute, explaining why stronger models absorb familiar principles while still gaining from high-asymmetry examples
- [Choosing what to learn requires both validity and learning-value gates](./choosing-what-to-learn-requires-both-validity-and-learning-value-gates.md) — grounds: separates trustworthiness from model-relative learning value, supplying the gate that ranking by preserved search cost and rejecting stock illustrations operationalize
- [Weight-resident methodologies provide context-efficient behavioral compression](./weight-resident-methodologies-compress-behavior-in-context.md) — contrasts: compact methodological cues activate weight-resident principles at low token cost, sharpening the activation-efficiency comparison against retaining discriminating examples
- [Abstract an experience into a lesson only when you can state where the lesson stops](./abstract-an-experience-only-when-you-can-state-the-boundary.md) — contrasts: preserves an instance when a boundary cannot yet be stated, whereas this conjecture retains a discriminating example even after the boundary is stated because rediscovering the case stays expensive
- [LLM recompute cost shifts the store-vs-recompute balance](./llm-recompute-cost-inverts-the-store-vs-recompute-default.md) — contrasts: prices caching recoverable derivations against recomputation at fixed capability, whereas this conjecture prices caching hard-to-discover boundary cases across model upgrades
- [Ablation baselines for the declared objective](../reference/proposals/ablation-baselines-for-the-declared-objective.md) — see-also: proposed matched-task ablation design comparing curated theory, episodic examples without distilled theory, and a bare stronger model
- [Calibrating semantic gates against labelled fixtures](../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) — see-also: proposal for retaining hand-authored near-miss boundary fixtures to test semantic gates across model changes
