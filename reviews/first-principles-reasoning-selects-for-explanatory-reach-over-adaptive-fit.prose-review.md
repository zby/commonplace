=== PROSE REVIEW: first-principles-reasoning-selects-for-explanatory-reach-over-adaptive-fit.md ===

Checks applied: 8

WARN:
- [confidence-miscalibration] The note presents Deutsch's two-category distinction (adaptive vs. explanatory) as a settled binary taxonomy with the assertive framing "David Deutsch distinguishes two kinds of knowledge." In Deutsch's own work (primarily *The Beginning of Infinity*), this is a philosophical argument, not an empirically validated classification — yet the note treats it as established ground truth throughout. More importantly, the three-part "negative test" in the eponymous section ("Can you vary the explanation?" / "Does it reach?" / "Can it be criticized?") is the note's own construction, attributed implicitly to Deutsch by proximity but never flagged as proposed. The phrase "Deutsch's distinction provides a quality check" presents this constructed test as if Deutsch himself supplied it.
  Recommendation: Flag the three-part negative test as the note's own operationalization of Deutsch's ideas ("One way to operationalize this for KB writing..."). Consider a brief hedge on the binary framing — Deutsch argues for this distinction; the note adopts it.

- [proportion-mismatch] The core claim is in the title: first-principles reasoning selects for explanatory reach over adaptive fit. The section that most directly carries this claim is "Why this matters for the KB" (roughly one paragraph plus an example). The "negative test" section and "programming fast-pass" section together are longer and are supporting/derivative material. The load-bearing argument — *why* first-principles filtering is equivalent to selecting for reach — gets compressed into a single sentence: "the derivation is explanatory — it says *why* the pattern works, which means it predicts where the pattern will fail." That sentence is doing almost all of the work for the title claim, and it is underdeveloped relative to the downstream test and application sections.
  Recommendation: Expand the "Why this matters for the KB" section to develop the core equivalence claim more fully. Consider whether the negative test section (which is already distilled into a recurring task) could be shortened here to rebalance.

INFO:
- [source-residue] The note is pitched at the level of epistemology and KB methodology. The computational-model paragraph in "Why this matters for the KB" introduces domain-specific terms ("scoping," "partial evaluation," "scheduling," "compilers," "dynamic scoping," "lexically scoped sub-frames") without explicit example framing. These are arguably the note's *subject matter* rather than residue, since the KB itself is about agent/context engineering. However, a reader encountering this note as an epistemology piece (which the title and opening suggest) might find the density of programming-language terms unmarked and surprising.
  Recommendation: No action required if the intended audience is KB contributors who already know the computational-model area. Worth checking whether a reader coming from the learning-theory tag would have enough context.

- [redundant-restatement] The "programming fast-pass" section's opening sentence ("The design methodology gives programming patterns a 'fast pass.'") restates a point already made in the "Why this matters" section (where the computational-model area is presented as exemplifying reach). The section then adds only one new element (the Thalo convergent-evolution reference) before pointing back to the methodology note. The section is short enough that the restatement cost is low, but it is structurally a re-entry into already-covered ground.
  Recommendation: Consider folding the Thalo reference into the "Why this matters" section and removing the "programming fast-pass" section, or trimming the restating opener to a single transition sentence.

CLEAN:
- [pseudo-formalism] No formal notation, equations, or symbolic apparatus appears in the note. The numbered test items in "The negative test" section are a checklist, not pseudo-formal decomposition. Clean.

- [orphan-references] All specific claims are attributed. Deutsch is named as the source. Links to other KB notes (design methodology, discovery, mechanistic constraints, computational-model, Thalo) provide the context chain. No floating data points or uncited empirical claims. Clean.

- [unbridged-cross-domain-evidence] The note draws from Deutsch's epistemology (philosophy) and applies it to KB design (engineering). The bridge is explicit: "The KB's first-principles methodology is, in Deutsch's terms, a filter that selects for explanatory reach over adaptive fit." The genome/neural-network examples in the opening are used as illustrations of Deutsch's own categories, not as cross-domain evidence claims. The Thalo reference is handled by deferring to the methodology note for the full argument. Clean.

- [anthropomorphic-framing] The note uses "A gene 'knows' how to build an eye" with scare quotes, signaling deliberate metaphorical use rather than literal attribution. No other anthropomorphic language applied to models or systems. Clean.

Overall: 2 warnings, 2 info
===
