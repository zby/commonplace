=== SEMANTIC REVIEW: constraining-during-deployment-is-continuous-learning.md ===

Claims identified: 11

1. AI labs frame "continuous learning" as a weight-update problem (para 1)
2. Constraining — accumulating symbolic artifacts — adapts deployed systems through a different mechanism entirely (para 1)
3. Each constraining step trades generality for compound gains in reliability, speed, and cost (para 2)
4. Constraining gains "produce the same narrowing of the behavior distribution that fine-tuning targets" (para 2)
5. Herbert Simon defines learning as any change that produces a more or less permanent change in a system's capacity for adapting to its environment (para 3)
6. Constraining during deployment meets every part of Simon's definition (para 3)
7. This is a subset claim — constraining is one concrete way continuous learning happens outside weights (para 4)
8. DSPy and ProTeGi automate one slice of constraining and the ML community recognizes this as learning (para 5)
9. Developer research shows the same pattern in manual form: iterative refinement of prompts, tools, and workflows (para 5)
10. Weight-based learning captures distributional knowledge that doesn't reduce to explicit artifacts (para 6)
11. "The extractable, testable subset that constraining handles covers most of what deployed systems need" (para 6)

---

WARN:
- [Completeness] "The extractable, testable subset that constraining handles covers most of what deployed systems need" (para 6) is a strong quantitative claim ("most") with no grounding. No cited source supports a proportion estimate. The developer study (Huang et al.) documents control strategies but says nothing about what fraction of deployed-system needs those strategies cover. The note's own prior paragraph acknowledges weight-based learning handles "distributional knowledge (style, tone, world knowledge)" — it is not obvious this is the minority case. For a style-sensitive application (marketing copy, creative writing, brand voice), distributional knowledge may be the majority of what the deployed system needs. This claim would benefit from either qualification ("covers a substantial share") or evidence.

- [Completeness] The note lists the artifact forms that constitute constraining during deployment as "prompts, schemas, evals, tools, and deterministic code" (para 1), and later adds "agent memory systems (Claude's memory files, Cursor rules, AGENTS.md conventions)" (para 5). Boundary case: **retrieval-augmented generation (RAG) knowledge bases** — adding documents to a retrieval corpus durably changes the system's behavior distribution during deployment, is inspectable and rollbackable, and is arguably the most widespread form of deploy-time adaptation. RAG document curation does not clearly map to "constraining" as defined in the constraining.md foundation note (which defines constraining as narrowing the interpretation space). Adding a new document to a RAG corpus *expands* what the system can answer — it is accumulation, not narrowing. If RAG is excluded, the note's claim that constraining covers "most of what deployed systems need" becomes harder to sustain, since RAG-based adaptation is extremely common. If RAG is included, the note's use of "constraining" drifts from the foundation note's definition.

- [Grounding – domain coverage] The note claims that developer behaviors documented in the Huang et al. study — "developers iteratively refine prompts, tools, and workflows based on deployment experience" — constitute "continuous learning through constraining." But the ingest note for that source explicitly warns: "Strategies described, not evaluated" and "Single 45-minute observation window." The study captures cross-sectional snapshots of developer practices, not longitudinal evidence of durable capacity change accumulating over time. Simon's definition requires "more or less permanent change in capacity" — a single observation session cannot establish permanence. The note treats "developers do X" as evidence for "X is continuous learning," but the cited source does not actually show the accumulation or persistence of the artifacts it describes. The inference from observed behavior to continuous learning is plausible but unsupported by the cited evidence specifically.

INFO:
- [Completeness] The note frames the comparison as "symbolic artifacts vs weight updates" but does not address a third category: **architectural/infrastructure changes** to deployed systems (adding a new tool endpoint, changing the retrieval pipeline, modifying the agent's allowed action space). These are durable, inspectable changes to the system's capacity — and they may or may not count as "constraining" depending on whether they narrow or broaden interpretation. The note's binary framing (weights vs artifacts) may undercount the mechanisms of deploy-time adaptation.

- [Grounding – vocabulary mismatch] The note states DSPy and ProTeGi "automate one slice of constraining — searching over prompt components to optimize against an objective — and the ML community recognizes this as learning." DSPy's self-description uses "compiling" and "optimizing," not "constraining." The ML community recognizes prompt optimization as optimization/search, not necessarily as "learning" in Simon's sense. The note is making an inference (prompt optimization = constraining = learning) that is reasonable but attributes to the ML community a recognition it may not hold. The note could be more precise: the ML community recognizes DSPy as automated optimization; *the note* argues this constitutes learning under Simon's definition.

- [Internal consistency] The note carefully states it is "a subset claim, not the umbrella claim" (para 4) — constraining is one way continuous learning happens outside weights. But the final paragraph's "covers most of what deployed systems need" pulls toward an umbrella-adjacent claim: if constraining handles "most" of what's needed, it is de facto the dominant mechanism, not merely one subset. The subset framing and the "most" claim create a tension — the note modestly scopes itself in paragraph 4 but makes an expansive claim in paragraph 6.

- [Grounding – inference validity] The note argues: (a) constraining changes the system, (b) the change is permanent (versioned, committed), (c) the capacity for adaptation improves, therefore (d) constraining meets Simon's definition of learning. Step (c) contains a subtle gap: not all constraining improves adaptive capacity. A poorly chosen constraint (an overly restrictive schema, a wrong convention) durably *reduces* the system's capacity. The note implicitly assumes constraining is done well. Simon's definition is symmetric — maladaptive permanent changes are also "learning" under some readings, or they fail the definition under others. The note could acknowledge that constraining-as-learning assumes the constraining is adaptive, not arbitrary.

PASS:
- [Internal consistency] The note's self-scoping as "a subset claim, not the umbrella claim" (para 4) is faithfully maintained in the surrounding structure — the durability-focused foundation note (continuous-learning-requires-durability-not-weight-updates.md) makes the general claim, and this note correctly positions itself as one concrete instance. The Relevant Notes section accurately reflects this relationship ("this note is one concrete non-weight case, not the general claim").

- [Grounding alignment] The Simon citation checks out against the foundation note (learning-is-not-only-about-generality.md), which quotes Simon: "learning is any change in a system that produces a more or less permanent change in its capacity for adapting to its environment." The note's use of this definition is accurate.

- [Grounding alignment] The link to constraining-and-distillation-both-trade-generality-for-reliability-speed-and-cost.md accurately supports the claim about the generality-for-compound trade-off. The foundation note explicitly states: "Each constraint narrows what the system can do (less generality) but makes what it does do more reliable, faster, and cheaper." The attribution is faithful.

- [Grounding alignment] The note's characterization of the developer study ("developers iteratively refine prompts, tools, and workflows based on deployment experience") accurately reflects the source's content. The ingest summary confirms: "professionals carefully control agents through planning, explicit prompting with rich context, step-by-step supervision, and established software engineering practices." The vocabulary and scope of the attribution are aligned — the concern (noted in WARN above) is about what the source can prove about durability, not about whether the behavioral description is accurate.

- [Internal consistency] The note's acknowledgment that "not all continuous learning is constraining" (para 6) and its explicit subset framing (para 4) are consistent with each other and with the broader KB structure. No definition drift was detected — "constraining" is used consistently throughout as narrowing the interpretation space through symbolic artifacts.

Overall: 3 warnings, 4 info
===
