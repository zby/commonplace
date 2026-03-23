=== SEMANTIC REVIEW: scenarios.md ===

Claims identified: 9

**Claims extracted:**

1. [Title/framing] The note claims to present "concrete use cases for the knowledge system" (description) and asks "What do we actually use the knowledge system for?" — implying these are THE use cases, or at least the primary ones.
2. [Upstream change analysis, enumeration] The upstream workflow has four steps: Notice, Analyze, Write comments, Document the comments.
3. [Upstream change analysis, scope] "Step 4 is where the knowledge system earns its keep" — the KB's value in this scenario is concentrated at the documentation/grounding step.
4. [Upstream change analysis, enumeration] Step 4 requires three things: scan relevant code, read existing notes, find prior decisions.
5. [Upstream change analysis, evaluation criterion] "does it make step 4 faster and better than just reading code and grepping?" — this is the evaluation question for the KB.
6. [Upstream change analysis, dependency] "These scenarios are the concrete evaluation criteria a KB learning loop would need to optimise against" — links to automating-kb-learning-is-an-open-problem.md.
7. [Proposing our own changes, enumeration] The proposing workflow has four steps: Have an idea, Build the case, Write the proposal, Ground it in evidence.
8. [Proposing our own changes, equivalence] "Same documentation need as upstream analysis, but the direction is reversed" — claims structural symmetry between the two scenarios.
9. [Proposing our own changes, enumeration] The KB should help assemble the case via three things: what have we already decided, what constraints exist, what prior art is relevant.

---

WARN:
- [Completeness] The note claims to present "concrete use cases for the knowledge system" but enumerates only two: upstream change analysis and proposing our own changes. Both are externally-directed argumentation scenarios (writing comments, writing proposals). This misses several boundary cases that the KB itself already serves:
  - **Onboarding/orientation**: a new agent session loading context about an unfamiliar area of the KB. This is neither responding to an upstream change nor proposing one — it is navigating the knowledge graph to build understanding. The note's two scenarios both assume the user already knows what they're looking for.
  - **Internal maintenance/refactoring**: reorganizing notes, splitting or merging, updating stale indexes. The linked note automating-kb-learning-is-an-open-problem.md lists seven mutation types (Extract, Split, Synthesise, Relink, Reformulate, Regroup, Retire) — these are KB use cases that don't map to either "upstream analysis" or "proposing changes."
  - **Knowledge discovery/synthesis**: reading across notes to discover a pattern or principle that no single note states. This is a use case the KB enables that is neither reactive (upstream) nor propositional (own changes) — it is exploratory.
  - The note from claw-learning-is-broader-than-retrieval.md already flags this gap explicitly: "the current scenario set is retrieval-oriented; an action-oriented framing would add classification, communication, and planning scenarios."

- [Completeness] The note's evaluation question — "does it make step 4 faster and better than just reading code and grepping?" — frames KB value purely as retrieval speed. This excludes value the KB provides through synthesis (combining knowledge from multiple notes to produce an insight neither contains alone) and through structure (the link graph encoding relationships that grepping cannot surface). A boundary case: the KB helps you realize two previously unconnected design decisions are in tension. That is not "faster grepping" — it is a qualitatively different capability.

INFO:
- [Completeness] The two scenarios are structurally symmetric — both are four-step workflows ending in "ground it in evidence." The note acknowledges this ("Same documentation need... but the direction is reversed"). The question is whether this symmetry is genuine or whether important differences are being elided. In upstream analysis, the knowledge need is reactive and scoped by the external change. In proposing changes, the knowledge need is generative and open-ended — you must also argue for the problem's existence, not just ground a solution. The KB's role in "building the case" (step 2 of proposing) may differ qualitatively from its role in "documenting comments" (step 4 of upstream), but the note treats them as equivalent.

- [Completeness] Claim 4 lists three things needed for step 4: "scan the relevant code, read existing notes, find prior decisions." These three could be read as exhaustive, but a boundary case is finding *external* evidence — related systems, academic sources, prior art from outside the project. The note's "proposing" scenario mentions "what prior art is relevant" but the upstream scenario does not, despite upstream comments also benefiting from external grounding.

- [Grounding alignment] The note links to automating-kb-learning-is-an-open-problem.md with the claim that "these scenarios are the concrete evaluation criteria a KB learning loop would need to optimise against." The linked note does reference scenarios.md and says the scenarios are "the closest thing we have to a requirements spec for what this question-answering capacity must serve." The attribution is accurate. However, the linked note also says "we don't yet have enough logged usage of them to design that loop" — which means the scenarios note is positioned as evaluation criteria for a system that cannot yet evaluate against them. This is not a misattribution but it is worth noting: the scenarios' role as "evaluation criteria" is aspirational, not operational.

- [Internal consistency] The note's description says "Concrete use cases for the knowledge system — upstream change analysis and proposing our own changes." The body's framing question is "What do we actually use the knowledge system for? Start here, work backward to what's needed." The phrase "what do we actually use" suggests empirical observation, but the two scenarios read more like designed archetypes than observed usage patterns. The note does not distinguish between "these are the use cases we have observed" and "these are the use cases we designed for." This is a minor ambiguity, not a contradiction.

PASS:
- [Internal consistency] The four-step structure of each scenario is internally consistent. Each step follows logically from the previous one, and the KB's entry point (step 4 in upstream, steps 2-4 in proposing) is correctly identified in each case.
- [Internal consistency] No definition drift detected. Terms like "knowledge system," "ground," and "evidence" are used consistently throughout.
- [Grounding alignment] The link to automating-kb-learning-is-an-open-problem.md is accurately characterized. The linked note does treat these scenarios as the closest available evaluation criteria, and the relationship is bidirectional (each note links to the other with consistent framing).
- [Internal consistency] The compressed framing ("same documentation need, direction reversed") faithfully represents the structural parallel between the two scenarios without overclaiming — it does not say the scenarios are identical, only that the documentation need is the same.

Overall: 2 warnings, 4 info
===
