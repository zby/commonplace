<!-- REVIEW-METADATA
note-path: kb/notes/short-composable-notes-maximize-combinatorial-discovery.md
last-full-review-note-sha: e7138e3d1859982bf9f64f7ed30a33a1a07b3b78
last-full-review-note-commit: 77b36d90b09b102404f4e2800ecad318640838d0
last-full-review-at: 2026-03-24T12:00:00+00:00
last-accepted-note-sha: e7138e3d1859982bf9f64f7ed30a33a1a07b3b78
last-accepted-note-commit: 77b36d90b09b102404f4e2800ecad318640838d0
last-accepted-at: 2026-03-24T12:00:00+00:00
last-acceptance-kind: full-review
review-type: semantic-review
-->
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
- [Completeness] The title claim "short composable notes maximize combinatorial discovery" and the opening sentence both present shortness and atomicity as sufficient for maximizing discovery surface area. But the note's own second paragraph introduces a different, stronger variable: "what matters is breadth of *independent* perspectives. Notes from distant domains are more likely to reveal shared structure than additional notes within the same topic." These two variables pull apart. A library of 100 short notes all within the same subdomain would have high co-loading capacity but low discovery potential by the note's own criterion. The design rule ("one claim, one note") addresses only the shortness variable; no guidance addresses the independence variable. The note identifies the more important variable but never reconciles it with the title claim or the design rule.

- [Completeness] The counterfactual in the Evidence section — "A single long note synthesizing all of memory theory would have contained the same information but wouldn't have surfaced the cross-cutting structure — it would have pre-committed to one narrative instead of leaving the connections available for discovery" — asserts a mechanism (pre-committed narrative forecloses discovery) without explicit justification. Why would an LLM reading a long synthesis fail to notice cross-cutting structure contained within it? The implicit premise is that discovery requires structure to be *latent and unnamed across separate documents* rather than present within a single narrative under a different organizational frame. This premise may well be correct, but it is never stated, and without it the counterfactual is an assertion rather than an argument.

- [Grounding — domain coverage] The note cites the discovery note for "discovery requires co-presence of multiple particulars." The discovery note actually discusses discovery as a cognitive/creative act: "recognizing that things from different contexts are instances of a structure that nobody had named yet." The discovery note's analysis focuses on recognition cost, naming as cost amortization, and three depths of abstraction — it does not make a claim about co-loading in a token window as the mechanism enabling discovery. The reviewed note silently narrows "recognition across contexts" (an epistemological claim about what discovery *is*) to "co-loading in bounded context" (an engineering constraint about when discovery *can happen*). This is a reasonable engineering inference, but the note presents it as if the discovery note grounds it directly. The inference step — that recognition across contexts requires co-presence in a finite attention window — is the note's own contribution and should be flagged as such.

INFO:
- [Completeness — boundary case] The simplest instance: a library with exactly two notes. The note's combinatorial argument ("the number of notes that fit determines the surface area") applies degenerate at this scale — there is exactly one pair, and the probabilistic framing ("not every pair yields a discovery") means expected discovery is near zero. At this scale, a longer combined document might actually serve better, since the consumer gets the full picture within one read and can reason about internal connections. The note's argument implicitly requires a library large enough that combinatorial breadth outweighs per-pair discovery probability, but states no threshold or scaling relationship.

- [Completeness — boundary case] The most extreme instance: a library with thousands of very short notes. The co-loading advantage saturates because the agent must *select* which notes to co-load, which is a search/navigation problem the note does not address. At this scale, finding the right combination to load becomes a harder bottleneck than fitting more notes into context. The resolution-switching note is cited as complementary, but it addresses zoom-level navigation (broad vs. narrow), not combinatorial selection (which subset to co-load for discovery).

- [Completeness — boundary case] Notes that sit between the enumerated categories: a note whose argument has three sequential, dependent premises (A therefore B therefore C). This is neither a single atomic claim (violating "one claim, one note") nor a full narrative belonging in a workshop. The design rule says "if a note has multiple ## sections making independent claims, that's a signal to decompose," but dependent premises in a chain are not independent claims — decomposing them loses the inferential force. The note's tension section acknowledges that "some arguments genuinely need space" but routes all such cases to workshops, which may over-rotate: a three-premise argument is not a workshop-scale narrative, yet it resists atomic decomposition.

- [Completeness — prior work] The prior work enumeration (Zettelkasten, modular design, faceted classification) is acknowledged as non-systematic. Notable omissions include the **concept mapping** tradition (Novak & Canas), which emphasizes cross-linking of propositions as a learning mechanism, and **transclusion** (Nelson, 1965), which addresses composability from the opposite direction — including fragments inline rather than keeping them separate. Neither invalidates the argument, but both would sharpen the "what's specific to our context" differentiation claim.

- [Grounding — vocabulary] The note says resolution-switching means "claim titles and descriptions give broad surface-level pairing without loading full bodies." The actual resolution-switching note describes a substantially richer set of mechanisms: titles vs. bodies as a resolution pair, indexes vs. notes at different resolutions, link semantics encoding zoom direction ("since" = zoom into foundation, "extends" = zoom out), and progressive disclosure as a resolution gradient. The reviewed note's reduction is accurate but selective — it imports only the aspect supporting the composability argument and omits the evaluative criterion (resolution-switching fluidity) and the symptoms of poor resolution-switching, which could complicate the "shorter is always better" implication.

- [Grounding — contextual-competence note] The footer link says this note "extends" the contextual-competence note, claiming "composability as one of three properties; short notes compose better." The contextual-competence note does identify composability as one of three properties (discoverable, composable, trustworthy), and defines composable as "pieces of knowledge combine into larger arguments and can be used as premises in new reasoning." It does not itself claim that shorter notes compose better — that inference is the reviewed note's contribution. The link semantics ("extends") are appropriate, but worth noting that the extension is the reviewed note's own argument, not something found in the source.

PASS:
- [Internal consistency] The note's four main sections (theory, prior work, design rule, evidence, tension) are mutually consistent. The theory motivates short notes via bounded context; the prior work places the idea in tradition; the design rule operationalizes the theory; the evidence illustrates discovery via co-loading; the tension section acknowledges a genuine limitation. No definition drift detected — "composable," "atomic," "short," and "independent" are used consistently throughout.
- [Internal consistency] The tension section faithfully represents the limitation ("some arguments genuinely need space") and the resolution (workshops for narratives, library for premises and conclusions) is consistent with the workshop note's library/workshop distinction. The workshop note defines workshop documents as consuming value over time with completion as the success state, which matches the reviewed note's characterization of where synthesized views belong.
- [Grounding — context-efficiency note] The claim that "bounded context" makes co-loading capacity the scarce resource is well-grounded. The context-efficiency note establishes context as "the only channel" through which an agent operates and as "the lowest-degree-of-freedom resource," directly supporting the premise that the number of notes that fit in context is the binding constraint.
- [Grounding — workshop note] The claim that "longer synthesized views belong in workshops" aligns accurately with the workshop note's library/workshop distinction table, which defines library documents as accumulating value and workshop documents as consuming value, with different success states (referenced/connected vs. completed/discarded).
- [Grounding — evolving-understanding note] The tension link to "evolving understanding needs re-distillation not composition" is accurately characterized. That note argues fragment reconciliation can exceed effective context when the consumer needs the whole picture, and the reviewed note correctly frames this as a tension (atomicity for discovery vs. coherence for comprehension) rather than a refutation.

Overall: 3 warnings, 6 info
===
