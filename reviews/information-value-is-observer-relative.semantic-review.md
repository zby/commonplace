=== SEMANTIC REVIEW: information-value-is-observer-relative.md ===

Claims identified: 14

1. [Opening] "What makes information valuable is not a property of the data alone but of the data-observer pair: the observer's prior knowledge, computational capacity, available tools, and goals all determine what they can extract."
2. [Prior work] Relevance theory defines relevance relative to the individual's cognitive environment.
3. [Prior work] In decision theory, information has value only if it changes a decision.
4. [Prior work] Bounded rationality: the value of information depends on processing capacity, not just content.
5. [Prior work] Bayesian decision theory: expected improvement depends on observer's prior beliefs and utility function.
6. [Prior work] Classical information theory (Shannon, Kolmogorov) deliberately abstracts away the observer.
7. [Prior work] "the same content in a different arrangement can teach more, even though nothing changed by classical measures."
8. [What to keep] "an isolated fact is worth less than a design principle that links to five other notes, because the principle creates extraction opportunities across sessions."
9. [How to present] Four KB conventions are listed as "optimizations for the agent observer": title as claim, descriptions as retrieval filters, short composable notes, progressive refinement.
10. [How to present] "distillation creates value by reshaping knowledge for a specific observer."
11. [How to present] "Multiple distillations of the same source aren't redundant -- each targets a different observer."
12. [What observer-relativity doesn't help with] "Discovery cost is observer-relative but not easily optimized."
13. [What observer-relativity doesn't help with] "Reverse-compression is the failure mode -- expanding text without adding extractable structure."
14. [Open Questions] "Observer-relativity applies to both patterns (require computational depth to extract) and facts (require prior knowledge to interpret). Are these the same phenomenon or two phenomena that share a surface shape?"

WARN:
- [Completeness] The four-factor decomposition of observer state (prior knowledge, computational capacity, tools, goals) is presented without explicit grounding and may be incomplete. "Attention" or "time budget" is a plausible fifth factor -- an observer may have the knowledge, capacity, tools, and goals to extract value, but be under time pressure that prevents them from doing so. Time pressure is distinct from computational capacity (a model with a 1M context window under a 5-second latency constraint is a different observer than the same model with unlimited inference time). The note's own cited traditions hint at this: bounded rationality (Simon) is partly about satisficing under time pressure, not just capacity limits. This factor is arguably subsumed by "computational capacity" if read generously, but the note never makes that subsumption explicit.

- [Grounding/Domain coverage] The Epiplexity link claim states that epiplexity "captures the pattern-extraction aspect (learnable structure a bounded model extracts from sequential data) but does not cover fact-level observer-relativity." This is an accurate and honest scoping of the source. However, the note's central claim is about information value in general (patterns AND facts), and the only formal source cited (Epiplexity) covers only the pattern side. The fact side -- that prior knowledge determines whether a fact is interpretable -- is grounded only in the informal Prior Work section (relevance theory, Bayesian decision theory). The note therefore has asymmetric grounding: the pattern half has a formal theoretical anchor; the fact half has only literature gestures. This asymmetry is not acknowledged in the body (only in the Open Questions, obliquely). A reader following the Epiplexity link might overestimate how much of the note's claim is formally grounded.

- [Completeness/Boundary] The four KB conventions listed as "optimizations for the agent observer" (title as claim, descriptions as retrieval filters, short composable notes, progressive refinement) are presented as instances of observer-relative design. Boundary case: **link semantics** (the requirement that every link articulate its relationship) is arguably a fifth convention that optimizes for the agent observer -- it reduces the computational cost of traversal decisions by making relationship type explicit rather than requiring the agent to infer it. The note links to related notes using semantic labels (instance, grounds, etc.) but does not list link semantics itself as an observer-relative optimization, even though the KB's own CLAUDE.md mandates it for exactly this reason. This is a gap in the enumeration rather than an error, but it's notable because the note is practicing the convention it omits from its list.

INFO:
- [Completeness/Boundary] Claim 8 asserts "an isolated fact is worth less than a design principle that links to five other notes, because the principle creates extraction opportunities across sessions." Boundary case: a well-timed isolated fact (e.g., a critical API deprecation notice) can be more valuable than a well-connected design principle if the observer's immediate goal is execution rather than learning. The note's own framework (goals determine value) supports this counterexample. The claim is probably intended as a default-case heuristic for library design rather than a universal ordering, but it reads as a universal statement.

- [Internal consistency] The note says "distillation creates value by reshaping knowledge for a specific observer" and describes this as "lossy compression." Two sentences later it says "the distillate can be more valuable than the source." These are not contradictory but the juxtaposition of "lossy" (implies information loss) with "more valuable" (implies information gain) could confuse a reader who equates "information" with "value." The note's own framework resolves this (value is observer-relative, so loss in absolute terms can be gain for a bounded observer), and the Epiplexity ingest explicitly discusses this resolution ("deterministic transformations create information for bounded observers"). But the note itself does not make the resolution explicit in-line -- it relies on the reader already understanding the framework being argued for.

- [Grounding] The note's Prior Work section cites four traditions (relevance theory, decision theory, bounded rationality, Bayesian decision theory) entirely from training data, with no linked sources. The note honestly flags this with a TODO. The descriptions appear accurate at the level of standard textbook summaries. No misattribution detected, but the claims cannot be verified against linked sources because none are provided.

- [Completeness/Boundary] The Open Questions section asks whether the agent is "the only important reader." This is a genuine open question but it also creates a tension with the body, which is written entirely from the perspective of the agent as primary reader. If humans are important readers too, some of the "optimizations for the agent observer" (e.g., title-as-claim) might trade off against human readability. The note does not explore this tension beyond flagging the question.

PASS:
- [Internal consistency] The note's structure is internally coherent. The opening claim (value depends on the data-observer pair) is consistently applied throughout: Prior Work shows the claim is established; "Why this matters" applies it to KB design; "What observer-relativity doesn't help with" honestly scopes the limits. No definition drift detected -- "observer" means the same thing (an entity with prior knowledge, capacity, tools, goals) throughout.

- [Grounding] The link to distillation.md is accurate. The note claims "distillation creates value by reshaping knowledge for a specific observer" and the distillation note confirms this framing: "compressing knowledge so that a consumer can act on it within bounded context." The distillation note explicitly links back to this note with "reframes distillation as bounded information extraction." The cross-references are mutually consistent.

- [Grounding] The link to discovery-is-seeing-the-particular-as-an-instance-of-the-general.md is accurate. The note claims "discovery cost is observer-relative" and the discovery note confirms: "recognition cost scales with depth" and links back to this note with "the recognition cost hierarchy maps to computational bounds on structure extraction." No vocabulary or scope mismatch.

- [Grounding] The Epiplexity source link is accurately scoped. The note says epiplexity "captures the pattern-extraction aspect... but does not cover fact-level observer-relativity." The ingest confirms epiplexity measures "structural information extractable by computationally bounded observers" -- specifically learnable patterns, not factual interpretation. The note does not overclaim the source's coverage.

- [Grounding] The link to short-composable-notes-maximize-combinatorial-discovery.md accurately represents that note's argument. The claim that "many short notes give more combinatorial coverage than few long ones for a reader with bounded context" matches the target note's thesis that "short, atomic notes maximize [co-loading] surface area."

- [Internal consistency] The compressed description ("Grounds distillation, discovery, and context arrangement as observer-relative operations") faithfully represents the body. The body does ground each of these as observer-relative. No elision of tensions detected in the description.

Overall: 3 warnings, 4 info
===
