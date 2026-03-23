=== SEMANTIC REVIEW: three-space-agent-memory-maps-to-tulving-taxonomy.md ===

Claims identified: 6

1. Agent memory should be three qualitatively different spaces: knowledge graph, self space, operational space (from source article)
2. These three spaces map to Tulving's semantic/episodic/procedural taxonomy
3. The key insight is different *lifecycles*, not different topics — knowledge accumulates steadily, self-knowledge evolves slowly, operational artifacts churn
4. Conflating spaces produces three failure modes: (a) operational debris polluting search, (b) identity scattering, (c) insights trapped in session state
5. Whether failures manifest at practical scale is an open empirical question
6. The Tulving mapping may be decorative — practical value may reduce to "separate persistent from transient with different retention policies"

WARN:
- [Completeness] The mapping of Tulving's "procedural memory" to "operational space" is a category stretch. Tulving's procedural memory covers implicit, non-declarative skills (how to ride a bike, how to type) — knowledge that cannot be articulated. The note's operational space contains explicit artifacts: "friction observations, methodology, session artifacts." These are all declarable, articulable content. The note maps procedural memory to the space with the *highest explicit content churn*, but Tulving's procedural memory is defined by being *implicit and stable*. The mapping inverts the stability property that defines the source category.
- [Completeness] "Methodology" appears in the operational space column ("high churn"), but methodology can also be durable, accumulating knowledge. The linked deploy-time-learning note treats methodology hardening (constraining, codification) as something that solidifies over time, not something that churns. A methodology note that has been refined across many sessions fits "steady growth" (knowledge space) better than "high churn" (operational space). The framework provides no guidance for where methodology sits after it stabilizes.
- [Grounding] The link annotation for the comparative review says it "validates: evaluates the three-space taxonomy's analytical utility across 11 systems; uses the knowledge/self/operational split as the framework for comparing agency models and retention policies." However, the comparative review organizes its analysis around six architectural dimensions (storage unit, agency model, link structure, temporal model, curation operations, extraction schema) — not the knowledge/self/operational split. The three-space taxonomy does not serve as the primary analytical framework in that review. The "validates" relationship overstates alignment.

INFO:
- [Completeness] The metabolic rate assignments ("steady growth," "slow evolution," "high churn") are presented as properties of the three spaces but are not uniform within each space. The linked quality-scores note assigns *fast* recency decay to source snapshots and *no* decay to design notes — both of which would live in the knowledge space. If metabolic rate varies significantly within a single space, the three-space lifecycle distinction may not be the right cut. The note's own hedge ("may be decorative") partially acknowledges this, but the table presents the rates as definitive.
- [Completeness] Learned heuristics and preferences (e.g., "this user prefers concise responses") sit ambiguously between knowledge space (a fact) and self space (calibration/identity). In Tulving's taxonomy these would likely be episodic (derived from personal experience), but the note's table puts "operational patterns, calibration" in self space and "atomic notes, linked claims" in knowledge space. A learned preference is both a fact and a calibration. The framework doesn't clearly resolve this.
- [Grounding] The link to deploy-time-learning says "the three timescales framework; graduation from operational to knowledge space is a form of codification." Deploy-time-learning describes three *timescales* of system adaptation (training / in-context / deploy-time), not three *memory spaces*. The correspondence between timescales and memory spaces is the review note's own inference, not something the deploy-time-learning note claims. Calling graduation "a form of codification" is a reasonable extension but it is the note's move, not the source's.

PASS:
- [Internal consistency] The note is internally coherent. It presents the three-space framework from the source, then immediately hedges that the Tulving mapping "may be decorative" and "the practical value could reduce to simpler advice." The speculative status is appropriate and the hedging is consistent throughout.
- [Grounding] The link to three-space-memory-separation-predicts-measurable-failure-modes accurately characterizes that note as an "observational protocol for testing whether the separation actually helps." The linked note does exactly this.
- [Grounding] The link to memory-management-policy-is-learnable-but-oracle-dependent is accurately characterized as "challenges" — AgeMem's two-tier (LTM/STM) access-pattern separation and its unified RL-trained management do provide evidence against structural isolation by content type. The relationship is well-described.
- [Completeness] The three failure modes (search pollution, identity scatter, insight trapping) are well-defined and distinct. Each describes a different cross-contamination direction. No obvious fourth failure mode is missing from the framework as stated (given that the framework only claims three spaces, the three pairwise contamination patterns are the natural set).

Overall: 3 warnings, 3 info
===
