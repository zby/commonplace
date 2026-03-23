=== SEMANTIC REVIEW: short-composable-notes-maximize-combinatorial-discovery.md ===

Claims identified: 12

1. "Discovery ... requires co-presence: you can't find that three notes share unnamed structure if only one fits in context" (opening paragraph) — causal claim
2. "Under bounded context, the number of notes that fit determines the surface area for cross-cutting connections" (opening paragraph) — causal claim
3. "Short, atomic notes maximize that surface area" (opening paragraph) — scope claim ("maximize")
4. "The gain is probabilistic, not mechanical — not every pair yields a discovery" (paragraph 2) — definition/scope
5. "Notes from distant domains are more likely to reveal shared structure than additional notes within the same topic" (paragraph 2) — causal claim
6. "Claim titles and descriptions give broad surface-level pairing without loading full bodies" (paragraph 3, citing resolution-switching) — mechanism claim
7. Prior work enumeration: Zettelkasten, modular design, faceted classification as recurring instances of composable-unit design (Prior work section) — enumeration
8. "What's specific to our context is the bounded-context motivation" (Prior work section) — differentiation claim
9. "One claim, one note" as the design rule (Design rule section) — prescriptive claim
10. "Longer synthesized views belong in workshops or are generated" (Design rule section) — scope/routing claim
11. Evidence: structure emerged from juxtaposition of independent perspectives; "A single long note synthesizing all of memory theory would have contained the same information but wouldn't have surfaced the cross-cutting structure" (Evidence section) — causal counterfactual
12. Tension acknowledged: "Some arguments genuinely need space — the reasoning from premises to conclusion loses force when atomized" (Tension section) — qualifying claim

---

WARN:
- [Completeness] The claim "short, atomic notes maximize that surface area" treats note count as the primary variable, but the note itself says "what matters is breadth of *independent* perspectives." These pull in different directions. A library of 50 short notes from the same domain would have high surface area by count but low discovery potential by the note's own criterion. The maximization claim is really: short notes maximize *potential* surface area, conditional on independence — but the title and opening paragraph present shortness alone as sufficient. The note partially acknowledges this ("Notes from distant domains are more likely to reveal shared structure") but never reconciles the two variables into the design rule, which says only "one claim, one note" with no guidance on domain diversity.

- [Completeness] The counterfactual in the Evidence section — "A single long note synthesizing all of memory theory would have contained the same information but wouldn't have surfaced the cross-cutting structure" — asserts a mechanism without justification. Why would a long note containing the same information fail to surface the same structure? The implicit argument is that pre-committed narrative forecloses alternative readings, but this is never stated. An LLM re-reading a long synthesis could plausibly discover cross-cutting structure within it. The claim needs the missing premise: that discovery requires the structure to be *latent and unnamed* across separate documents, not merely present in one document under a different narrative frame.

- [Grounding — domain coverage] The note cites the discovery note for the claim that "discovery requires co-presence of multiple particulars." The discovery note actually says discovery requires "recognizing that things from different contexts are instances of a structure that nobody had named yet" — a cognitive/creative act, not a co-loading constraint. The discovery note discusses recognition cost and naming as the hard problem, but does not claim that co-presence in a token window is the mechanism. The reviewed note silently narrows "recognition across contexts" (an epistemological claim) to "co-loading in bounded context" (an engineering constraint). This is a reasonable inference but presented as attribution.

INFO:
- [Completeness — boundary case] The simplest instance: a library with exactly two notes. The note's argument (more notes = more surface area) applies, but the probabilistic framing ("not every pair yields a discovery") means a two-note library has essentially zero expected discovery. At this scale, a longer combined document might actually be better — the consumer gets the full picture and can reason about connections within it. The note's argument implicitly assumes a library large enough that combinatorial breadth outweighs per-pair discovery probability, but never states a threshold or scaling relationship.

- [Completeness — boundary case] The most extreme instance: a library with thousands of very short notes. At this scale, the co-loading advantage saturates — you can fit many notes, but the agent must *select* which ones to co-load, which is a search/navigation problem the note doesn't address. The note assumes loading is the bottleneck, but at scale, finding the right combination to load becomes the bottleneck. The resolution-switching note is cited as complementary, but that note addresses zoom-level navigation, not combinatorial selection.

- [Completeness — prior work] The prior work enumeration (Zettelkasten, modular design, faceted classification) is acknowledged as non-systematic ("from the agent's training data"). A notable omission is the **concept mapping** tradition (Novak & Canas) which emphasizes cross-linking of propositions, and **transclusion** (Nelson, 1965) which addresses the composability problem from the opposite direction — including fragments inline rather than keeping them separate. Neither invalidates the note's argument, but both would sharpen the "what's specific" differentiation.

- [Grounding — vocabulary] The note says resolution-switching means "claim titles and descriptions give broad surface-level pairing without loading full bodies." The resolution-switching note actually describes a richer set of mechanisms (titles vs. bodies, indexes vs. notes, link semantics encoding zoom direction, progressive disclosure as gradient). The reviewed note's reduction to "titles give pairing without loading" is accurate but selective — it imports only the aspect that supports the composability argument and omits the evaluative criterion (resolution-switching fluidity) which might complicate the "short notes are always better" framing.

- [Internal consistency] The note says "the library should be optimized for ... many small, independently authored claims" but later acknowledges that "some arguments genuinely need space." The tension section resolves this by routing narratives to workshops. However, the resolution depends on a clean library/workshop separation that may not hold in practice — a note whose argument requires multiple premises presented in sequence is neither a single claim nor a full narrative. The note's own "Design rule" section ("If a note has multiple ## sections making independent claims, that's a signal to decompose") could conflict with arguments that have dependent, sequential premises. This is an edge case in the framework, not a contradiction, but the decomposition heuristic is stated more confidently than the underlying distinction supports.

PASS:
- [Internal consistency] The note's three main sections (theory, design rule, evidence) are mutually consistent. The theory motivates short notes, the design rule operationalizes the theory, and the evidence illustrates the theory in action. No definition drift detected — "composable," "atomic," "short," and "independent" are used consistently throughout.
- [Internal consistency] The tension section faithfully represents the limitation and the resolution (workshops for narratives) is consistent with the workshop note's framing of consumed-value vs. accumulated-value artifacts.
- [Grounding — workshop note] The claim that "longer synthesized views belong in workshops" aligns with the workshop note's library/workshop distinction. The workshop note defines workshop documents as consuming value over time with completion as the success state, which matches the reviewed note's characterization.
- [Grounding — evolving-understanding note] The tension link to "evolving understanding needs re-distillation not composition" is accurately characterized. That note does argue that fragment reconciliation can exceed effective context, and the reviewed note correctly frames this as a tension rather than a refutation.
- [Grounding — context-efficiency note] The claim that "bounded context" makes co-loading capacity the scarce resource is well-grounded. The context-efficiency note establishes context as "the only channel" and "the lowest-degree-of-freedom resource," directly supporting the premise.

Overall: 3 warnings, 5 info
===
