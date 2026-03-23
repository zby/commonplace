=== SEMANTIC REVIEW: decomposition-rules-for-bounded-context-scheduling.md ===

Claims identified: 19

**Step 1: Extracted claims**

1. "These rules follow from the symbolic scheduling model" (opening sentence) — dependency claim
2. The optimisation problem is: "Choose a decomposition, a prompt-construction strategy, and a schedule of state transformations that maximises expected task utility while respecting the per-call bound M" — definition/scope claim
3. Five objective terms are listed (token traffic, number of calls, peak prompt size, information loss, preservation of cross-item interactions) — enumeration
4. "This makes the problem different from ordinary knapsack-style context packing" — causal/scope claim
5. Four trade-offs are listed (early filtering vs discarding, aggressive summarisation vs destroying interactions, many narrow calls vs overhead, loading raw vs saving task-shaped intermediates) — enumeration
6. "The first two are about optionality... The latter two are about cost structure" — classification claim
7. Rule: "Separate selection from joint reasoning" — prescriptive claim
8. Rule: "Use symbolic operations wherever exactness is available" — prescriptive claim
9. Rule: "Save reusable intermediate items in scheduler state" — prescriptive claim with condition ("when they are much cheaper to reuse than reconstructing the originals")
10. Rule: "Delay expensive co-loading until interactions justify it" — prescriptive claim with condition
11. Rule: "Commit low-degree-of-freedom choices first" — prescriptive claim
12. Rule: "Do not compress away needed interfaces" — prescriptive claim
13. Rule: "Choose representations, not just subsets" — prescriptive claim
14. Rule: "Exploit clean frames recursively" — prescriptive claim
15. ConvexBench "validates two rules directly" — grounding claim
16. "scoped recursion... recovers F1=1.0 at all depths from F1~0.2 under flat accumulation" — empirical attribution
17. "finer decomposition (10-character sub-functions) consistently outperforms coarser decomposition confirms 'exploit clean frames recursively'" — empirical attribution + causal claim
18. "Both results hold despite trivial token counts (5,331 tokens at depth 100), confirming that the rules respond to compositional complexity, not volume" — causal/scope claim
19. MAKER "demonstrates the extreme case: maximal decomposition to m=1... achieves O(s ln s) cost scaling and solves a 1,048,575-step task with zero errors" — empirical attribution

**Step 2: Completeness and boundary cases**

The note's implicit space is "practical rules for decomposing work across bounded LLM calls." The eight rules claim to cover the scheduling decisions an orchestrator must make when tasks exceed a single context window.

Boundary cases tested:

(a) **Tasks requiring global coherence across all items (e.g., writing a unified narrative from 50 sources).** The rules say "delay expensive co-loading until interactions justify it" and "do not compress away needed interfaces." But when the task *is* global synthesis — where essentially every item interacts with every other — the delay strategy has no room to operate, and saving interfaces for everything approaches loading everything. The rules do not address the case where the relevant set is irreducibly large relative to M and interactions are dense, not sparse. The "exploit clean frames recursively" rule gestures at tree-structured merging, but the note does not discuss how to handle synthesis quality loss from hierarchical merging when global coherence matters.

(b) **Single-item tasks that fit in one window.** The simplest instance — a task where the full input fits within M — trivially satisfies all rules (no decomposition needed). The rules do not explicitly address when *not* to decompose. This is a minor gap; the rules are framed as applicable "when needed," but the note never states the precondition.

(c) **Tasks where the decomposition structure is unknown upfront.** Both empirical sources (ConvexBench, MAKER) have known decomposition structures (recursive function composition, recursive Hanoi). The rules assume the orchestrator knows how to decompose — "separate selection from joint reasoning," "exploit clean frames recursively" — but do not address the meta-problem of *discovering* the right decomposition. The parent model note acknowledges this in its open questions ("How much selection judgment should the scheduler perform..."), but the rules note does not flag that the rules presuppose a decomposition strategy is already available.

(d) **Tasks where symbolic operations are not available for any sub-step.** The rule "use symbolic operations wherever exactness is available" has the escape hatch "wherever... available," but some tasks (e.g., open-ended brainstorming, creative writing) may have no sub-step amenable to symbolic operations. In such cases, most of the eight rules still apply, but the note's framing — especially the empirical grounding — leans heavily toward tasks with significant symbolic structure.

(e) **Contradictory rule application: aggressive decomposition vs overhead costs.** "Exploit clean frames recursively" pushes toward maximal decomposition, while the trade-off section warns about "many narrow calls against the overhead of orchestration." The rules do not provide guidance on when the overhead of decomposition exceeds its benefit — the stopping condition for recursion is left implicit.

WARN:
- [Completeness] The rules do not address the irreducibly-dense-interaction case — tasks where most items interact with most others and the relevant set cannot be sparsified. The note's trade-off list identifies "preservation of cross-item interactions needed by later synthesis" as an objective term, but none of the eight rules provides guidance for the case where this term dominates. The closest rule ("do not compress away needed interfaces") tells you what not to lose, but not how to proceed when preserving everything exceeds M.

INFO:
- [Completeness] The rules presuppose that a decomposition strategy is available. Both empirical sources have predetermined decomposition structures. The note does not flag that discovering the decomposition is a separate (and potentially harder) problem, though the parent model note's open questions partially cover this.
- [Completeness] No explicit stopping condition for recursive decomposition — "exploit clean frames recursively" and the overhead trade-off pull in opposite directions without resolution criteria.

**Step 3: Grounding alignment**

Sources checked: bounded-context-orchestration-model.md, convexbench-can-llms-recognize-convex-functions.md (source + ingest), meyerson-maker-million-step-llm-zero-errors.md (source + ingest), solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking-better-designs.md.

(A) ConvexBench attribution (claims 15-18):

The note claims ConvexBench "validates two rules directly": (1) "use symbolic operations wherever exactness is available" and (2) "exploit clean frames recursively."

For rule (1), the note says: "expression structure is recovered via deterministic AST parsing (not LLM calls)." The source confirms this — external tools provide explicit ASTs (source, "Proposed Solutions" section). Attribution is accurate.

For rule (1), the note also says: "scoped recursion — pruning history to retain only direct dependencies — recovers F1=1.0 at all depths from F1~0.2 under flat accumulation." The source confirms F1=1.0 recovery via "focused context" that "prunes irrelevant historical context, keeping only direct dependencies for each sub-task" (source, "Proposed Solutions" and "Experimental Results"). However, the F1=1.0 recovery is attributed in the note to scoped recursion as evidence for "use symbolic operations wherever exactness is available." This conflates two interventions: the AST parsing (symbolic operation) and the focused-context recursion (not a symbolic operation — it is an LLM-call scoping strategy). The source clearly separates these as distinct contributions. The note's phrasing "The 'use symbolic operations' rule is confirmed by the design: expression structure is recovered via deterministic AST parsing (not LLM calls), and scoped recursion..." links both under one rule when the source treats them as two separate mechanisms. The F1=1.0 result comes from the full pipeline (AST parsing + agentic recursion + focused context), not from symbolic operations alone.

For rule (2), the note says finer decomposition "confirms 'exploit clean frames recursively.'" The source's ablation studies confirm "finer decomposition (10-character sub-functions) consistently outperforms coarser decomposition." Attribution is accurate.

The claim "both results hold despite trivial token counts (5,331 tokens at depth 100), confirming that the rules respond to compositional complexity, not volume" is supported by the source, which explicitly distinguishes "long-context capability" from "long-horizon reasoning capability."

WARN:
- [Grounding] The note's empirical grounding paragraph for ConvexBench conflates the AST-parsing intervention (symbolic operation) with the focused-context/scoped-recursion intervention (LLM-call scoping) under a single rule ("use symbolic operations wherever exactness is available"). The source separates these as distinct mechanisms contributing to the recovery. The sentence beginning "The 'use symbolic operations wherever exactness is available' rule is confirmed by the design: expression structure is recovered via deterministic AST parsing (not LLM calls), and scoped recursion..." attributes the scoped-recursion result to the symbolic-operations rule, when the source attributes it to the agentic-reasoning-with-focused-context framework. The second half of this sentence (scoped recursion recovering F1=1.0) better supports "exploit clean frames recursively" than "use symbolic operations."

(B) MAKER attribution (claim 19):

The note claims MAKER "demonstrates the extreme case: maximal decomposition to m=1 (one step per bounded call) achieves O(s ln s) cost scaling and solves a 1,048,575-step task with zero errors."

The source confirms: maximal decomposition (m=1), O(s ln s) cost, 1,048,575 steps, zero errors. Attribution is accurate.

The note then claims this "validates 'delay expensive co-loading until interactions justify it' — each step depends only on the current disk configuration, so independent calls dominate joint reasoning." This is a reasonable inference. The MAKER source confirms each agent gets "the minimal context it needs to perform its single step: the overall strategy and the current state of the problem." However, MAKER's success also critically depends on voting-based error correction (first-to-ahead-by-k), which the note does not mention. The O(s ln s) cost scaling is not achievable through decomposition alone — it requires the voting mechanism to maintain the per-step success probability. The note attributes the scaling result to decomposition rules without noting the error-correction dependency.

The note also claims MAKER "confirms 'exploit clean frames recursively' at the limit: when every sub-task is atomic, the recursive pattern degenerates to a flat sequence of maximally focused calls." The source does describe this maximal decomposition. However, calling a flat sequence a degenerate case of recursion is the note's own framing — MAKER's architecture is not recursive (it is a linear sequence of identical micro-steps), and the source does not describe it as recursive. The characterization is not inaccurate but imposes a frame the source does not use.

INFO:
- [Grounding] The MAKER attribution omits that O(s ln s) cost scaling depends on the voting/error-correction mechanism, not decomposition alone. The source's scaling law derivation (Section 3.2) requires first-to-ahead-by-k voting to achieve the target success probability. The note presents the scaling result as validating decomposition rules, but the source shows it is a joint result of decomposition + error correction.
- [Grounding] Characterizing MAKER's flat sequence of micro-steps as "the recursive pattern degenerates to a flat sequence" is the note's own framing. The source does not describe MAKER as recursive or as a degenerate case of recursion. This is a minor vocabulary mismatch — the inference is reasonable but could mislead a reader into thinking the source frames it this way.

(C) Domain coverage:

The note claims eight general rules for bounded-context scheduling. Both empirical sources operate in the hard-oracle regime (mechanically verifiable correctness at each step). The note does not restrict its scope to hard-oracle tasks — the rules are presented as general. The ingest files for both sources note this limitation explicitly: ConvexBench ingest says "Only tested in the hard-oracle regime"; MAKER ingest says "The insights/execution boundary is acknowledged but underexplored." The note's rules may well apply beyond this regime, but the empirical grounding covers only one end of the oracle-strength spectrum.

INFO:
- [Grounding/Domain] Both empirical sources operate exclusively in the hard-oracle regime (deterministic per-step correctness). The note presents its rules as general-purpose scheduling guidance without flagging that all empirical validation comes from tasks with mechanically verifiable sub-steps. The rules may apply more broadly, but the grounding does not cover soft-oracle tasks (synthesis, creative work, ambiguous judgment).

(D) Parent model reference:

The note claims rules "follow from the symbolic scheduling model." The parent model note (bounded-context-orchestration-model.md) reciprocally links to this note as "consequence: practical rules that follow from the model." The derivation relationship is consistent across both notes. However, the derivation is informal — the rules are stated as practical guidance, not formally derived from the model's definitions. This is appropriate for a seedling note and not a grounding problem.

PASS:
- [Grounding] Parent-model reference is reciprocal and consistent. The bounded-context-orchestration-model.md links to this note as "consequence" and this note links back as "foundation."
- [Grounding] The low-degree-of-freedom note (solve-low-degree-of-freedom-subproblems-first.md) and the "commit low-degree-of-freedom choices first" rule are well-aligned. The linked note describes the general heuristic; the rule applies it to scheduling. The link semantics ("extends") are accurate.

**Step 4: Internal consistency**

(A) The trade-off section identifies "early filtering against the risk of discarding something that matters later" and then the rules section says "separate selection from joint reasoning — first use cheap narrow calls to discover sparsity." These are consistent — the rule addresses the trade-off by making the filtering call cheap rather than eliminating the risk.

(B) The trade-off "many narrow calls against the overhead of orchestration" is acknowledged, but the rules section includes "exploit clean frames recursively" without a balancing rule about when to stop decomposing. This creates a tension: the trade-offs section acknowledges overhead, but the rules section provides no guidance on it. This is not a contradiction — the trade-offs section is descriptive and the rules section is prescriptive — but the asymmetry could mislead a reader into thinking maximal decomposition is always preferred.

(C) The claim "Both kinds of trade-off are present in every scheduling decision" (referring to optionality and cost-structure trade-offs) is a strong universality claim. A scheduling decision that is purely about representation choice (e.g., "send summaries instead of full text") involves cost structure but arguably not optionality in the sense described. This is a minor definitional stretch.

(D) The compressed description ("Practical rules for symbolic scheduling over bounded LLM calls — separate selection from joint reasoning, choose representations not just subsets, save reusable intermediates in scheduler state") highlights three of the eight rules. It omits the five others, including "commit low-degree-of-freedom choices first" and "exploit clean frames recursively." This is normal compression, not misrepresentation — the description serves as a retrieval filter, not a summary.

PASS:
- [Consistency] The trade-off section and rules section are internally consistent. Each rule can be read as a response to one or more of the identified trade-offs.
- [Consistency] No definition drift detected. Terms like "scheduler state," "bounded call," "clean frames," and "interactions" are used consistently throughout.
- [Consistency] The description field is a subset of the rules, not a distortion. Acceptable compression for retrieval purposes.

INFO:
- [Consistency] The universality claim "both kinds of trade-off are present in every scheduling decision" is strong. Pure representation-choice decisions (e.g., "send summaries instead of full text") clearly involve cost structure but the optionality dimension is less obvious — the trade-off is between current-call quality and future flexibility, which is optionality only under a generous reading.

---

WARN:
- [Completeness] The rules do not address the irreducibly-dense-interaction case — when most items interact with most others and sparsification is not available. The trade-off section names "preservation of cross-item interactions" as an objective, but no rule provides guidance when this term dominates and the relevant set exceeds M.
- [Grounding] The ConvexBench paragraph conflates two distinct source mechanisms (AST parsing and focused-context recursion) under a single rule ("use symbolic operations wherever exactness is available"). The scoped-recursion result (F1=1.0 recovery) is attributed to the symbolic-operations rule, but the source attributes it to the agentic-reasoning-with-focused-context framework. The second half of the sentence better supports "exploit clean frames recursively."

INFO:
- [Completeness] The rules presuppose an available decomposition strategy. Both empirical sources have predetermined decomposition structures. Discovering the right decomposition is a separate problem not addressed by the rules, though the parent model note's open questions partially cover it.
- [Completeness] No stopping condition for recursive decomposition — "exploit clean frames recursively" and the overhead trade-off pull in opposite directions without resolution criteria.
- [Grounding] MAKER's O(s ln s) scaling depends on voting-based error correction, not decomposition alone. The note presents the scaling result as validating decomposition rules without noting this dependency.
- [Grounding] Characterizing MAKER's flat micro-step sequence as a degenerate case of recursion is the note's framing, not the source's. Reasonable inference but could mislead.
- [Grounding/Domain] Both empirical sources operate exclusively in the hard-oracle regime. The rules are presented as general scheduling guidance without flagging that all empirical validation comes from mechanically-verifiable-sub-step tasks.
- [Consistency] The universality claim "both kinds of trade-off are present in every scheduling decision" is strong and may not hold for pure representation-choice decisions.

PASS:
- [Grounding] Parent-model link is reciprocal and semantically accurate ("foundation" / "consequence").
- [Grounding] Low-degree-of-freedom link is accurate — the rule applies the general heuristic to scheduling contexts.
- [Grounding] ConvexBench ablation result (finer decomposition outperforms coarser) is accurately attributed.
- [Grounding] MAKER empirical facts (m=1, O(s ln s), 1,048,575 steps, zero errors) are accurately reported.
- [Grounding] ConvexBench token-count claim (5,331 at depth 100, compositional complexity not volume) is accurately attributed.
- [Consistency] Trade-off section and rules section are internally consistent; rules respond to identified trade-offs.
- [Consistency] No definition drift across sections.
- [Consistency] Description field is acceptable compression, not distortion.

Overall: 2 warnings, 6 info
===
