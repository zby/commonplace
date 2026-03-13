# Connection Report: ConvexBench: Can LLMs Recognize Convex Functions?

**Source:** [ConvexBench: Can LLMs Recognize Convex Functions?](../../sources/convexbench-can-llms-recognize-convex-functions.md)
**Date:** 2026-03-09
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md (141 entries) — flagged candidates:
  - [symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration](../../notes/symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) — agentic divide-and-conquer is an instance of this model
  - [decomposition-rules-for-bounded-context-scheduling](../../notes/decomposition-rules-for-bounded-context-scheduling.md) — paper's decomposition strategies relate to these rules
  - [the-frontloading-loop-is-an-iterative-optimisation-over-bounded-context](../../notes/the-frontloading-loop-is-an-iterative-optimisation-over-bounded-context.md) — recursive agentic loop pattern
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — paper demonstrates context is the bottleneck
  - [frontloading-spares-execution-context](../../notes/frontloading-spares-execution-context.md) — external AST parsing is frontloading
  - [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) — convexity is a calculator problem
  - [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — DCP rules as hard oracle
  - [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) — focused context = clean scoped frames
  - [codification](../../notes/codification.md) — external parsing tool is codification
  - [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — oracle theory
  - [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — one-shot is the degraded variant
  - [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — lazy reasoning as a human-like failure mode

**Topic indexes:**
- Read [computational-model](../../notes/computational-model-index.md) — confirmed: scheduling, scoping, and frontloading notes are the core cluster. Additional candidate: [synthesis-is-not-error-correction](../../notes/synthesis-is-not-error-correction.md) (aggregation methodology).
- Read [learning-theory index](../../notes/learning-theory-index.md) — confirmed oracle-strength and codification connections.

**Semantic search (via qmd):**

- Query 1: `"compositional reasoning failure LLM depth decomposition agentic recursive scaffolding"` in notes (n=15)
  - [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) (56%) — strong match, already cites ConvexBench
  - [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) (45%) — failure mode overlap concept
  - [computational-model](../../notes/computational-model-index.md) (41%) — index, already covered
  - [synthesis-is-not-error-correction](../../notes/synthesis-is-not-error-correction.md) (39%) — aggregation vs voting
  - [symbolic-scheduling-over-bounded-llm-calls](../../notes/symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) (38%) — strong match
  - [decomposition-rules-for-bounded-context-scheduling](../../notes/decomposition-rules-for-bounded-context-scheduling.md) (36%) — strong match
  - [llm-mediated-schedulers-are-a-degraded-variant](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) (35%) — one-shot as degraded variant

- Query 1 in sources (n=10):
  - [convexbench source itself](../../sources/convexbench-can-llms-recognize-convex-functions.md) (93%) — self
  - [convexbench ingest](../../sources/convexbench-can-llms-recognize-convex-functions.ingest.md) (56%) — companion
  - [agentic-code-reasoning ingest](../../sources/agentic-code-reasoning.ingest.md) (44%) — already cites ConvexBench as synthesis partner
  - [meyerson-maker ingest](../../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) (40%) — decomposition at scale
  - [towards-a-science-of-scaling-agent-systems](../../sources/towards-a-science-of-scaling-agent-systems.md) (37%) — multi-agent scaling

- Query 2: `"long-horizon reasoning context window bounded verification step-by-step"` in notes (n=15)
  - [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) (89%) — already identified
  - [the-frontloading-loop-is-an-iterative-optimisation](../../notes/the-frontloading-loop-is-an-iterative-optimisation-over-bounded-context.md) (37%) — already identified
  - [symbolic-scheduling](../../notes/symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) (35%) — already identified

- Query 3: `"deterministic tools parsing external offload symbolic"` in notes (n=10)
  - [decomposition-rules](../../notes/decomposition-rules-for-bounded-context-scheduling.md) (50%) — already identified
  - [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) (34%) — weak match, different domain

**Keyword search:**
- `rg "convexbench|ConvexBench" kb/` — found 6 files: the source, its ingest, the agentic-code-reasoning ingest (cites ConvexBench as synthesis partner), context-efficiency note (already cites), scoping note (already cites), sources/index.md
- `rg "lazy reasoning|compositional reasoning" kb/notes/` — found 2 files: frontloading-loop (mentions "compositional reasoning gap"), scoping note

**Link following:**
- From [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md): already cites ConvexBench as empirical validation. Links to homoiconic medium, codification, unified calling conventions. No new candidates.
- From [context-efficiency-is-the-central-design-concern](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md): already cites ConvexBench. Links to frontloading, indirection, sub-agent isolation. No new candidates.
- From [agentic-code-reasoning ingest](../../sources/agentic-code-reasoning.ingest.md): explicitly identifies ConvexBench as a synthesis partner ("both sources independently show that explicit process structure outperforms free-form reasoning on deep reasoning tasks").

## Connections Found

### Notes that already cite ConvexBench (bidirectional candidates)

These notes already reference ConvexBench. The reverse links (from ConvexBench back to these notes) are worth adding:

- [context-efficiency-is-the-central-design-concern-in-agent-systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **grounds**: ConvexBench provides direct empirical evidence for the "attention degradation under load" property. Performance degrades at 5,331 tokens (trivially below context limits), proving degradation is about reasoning complexity, not token volume. The note already cites ConvexBench.

- [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) — **grounds**: ConvexBench experimentally validates the "recursion with clean frames" prediction. Focused context (giving each recursive step only its direct dependencies) recovers F1=1.0 from 0.2, confirming that flat accumulation — not the reasoning task itself — causes the collapse. The note already cites ConvexBench as its primary empirical evidence for the clean-frames concept.

### New connections (not yet linked from any note to the ConvexBench source)

- [symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration](../../notes/symbolic-scheduling-over-bounded-llm-calls-is-the-right-model-for-agent-orchestration.md) — **exemplifies**: ConvexBench's agentic framework is a concrete instance of the scheduling model. A symbolic scheduler manages the recursion stack and sub-expression tracking (bookkeeping), while bounded LLM calls handle the semantic judgment (is this sub-function convex?). The paper's key finding — that offloading bookkeeping to deterministic tools and giving each LLM call a minimal focused context recovers full performance — is exactly the prediction the scheduling model makes.

- [decomposition-rules-for-bounded-context-scheduling](../../notes/decomposition-rules-for-bounded-context-scheduling.md) — **exemplifies**: The paper demonstrates several of these rules empirically: "separate selection from joint reasoning" (parse the expression deterministically, then ask the LLM about convexity), "use symbolic operations wherever exactness is available" (deterministic AST parsing), and "exploit clean frames recursively" (recursive verification with focused context outperforms flat context). The ablation finding that finer decomposition (10-character sub-functions) consistently outperforms coarser decomposition provides quantitative evidence for aggressive decomposition into narrow calls.

- [frontloading-spares-execution-context](../../notes/frontloading-spares-execution-context.md) — **exemplifies**: The paper's first improvement — offloading expression parsing to an external tool that provides explicit ASTs — is textbook frontloading. A deterministic parser resolves structural ambiguity before the LLM reasons about content, removing parsing from bounded context and freeing attention for the actual convexity analysis. This directly instantiates the note's mechanism: replacing derivation with insertion.

- [bitter-lesson-boundary](../../notes/bitter-lesson-boundary.md) — **exemplifies**: Convexity verification via DCP rules is a pure calculator problem (spec IS the problem, correctness is mechanically verifiable). Yet frontier LLMs fail at depth. The paper shows that scale alone does not solve calculator problems requiring compositional reasoning — engineering scaffolding (deterministic parsing, recursive verification, scoped context) is necessary. A clean datapoint: even in the calculator regime, LLMs need architectural support for compositional depth.

- [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) — **exemplifies**: ConvexBench has a perfect hard oracle: DCP composition rules mechanically verify labels with zero judgment. This hard oracle is what makes the benchmark rigorous and the agentic improvements precisely measurable. Exemplifies the hard-oracle end of the spectrum.

- [the-frontloading-loop-is-an-iterative-optimisation-over-bounded-context](../../notes/the-frontloading-loop-is-an-iterative-optimisation-over-bounded-context.md) — **exemplifies**: The paper's agentic framework with focused context is a concrete instance of the iterative frontloading loop. Each recursive step selects what to include (only direct dependencies), executes in a clean sub-agent frame, absorbs the result (convex/concave/neither for that sub-expression), and feeds it to the next step. The paper's finding that pruning history to direct dependencies recovers full performance validates the note's claim that the loop works because of clean frame isolation.

- [codification](../../notes/codification.md) — **exemplifies**: The external AST parsing tool is codification — a deterministic code solution replacing LLM interpretation for the structural parsing sub-problem. The parsing specification IS the problem (parenthesis matching, operator scope), making it a natural codification candidate. The paper shows the concrete benefit: offloading parsing to code frees the LLM to focus on the semantic judgment (convexity analysis) it is uniquely needed for.

- [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](../../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — **exemplifies**: The paper's one-shot baseline — where the LLM handles both bookkeeping (tracking sub-expressions, managing the recursion) and semantic judgment (assessing convexity) in a single flat context — is the degraded variant. Performance collapse from F1=1.0 to F1=0.2 demonstrates the degradation. The agentic framework with external parsing and focused context recovers the clean separation, achieving F1=1.0.

**Bidirectional candidates** (reverse link also worth adding):
- [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md) <-> source — **grounds**: The return path is already present (note cites ConvexBench). The forward path (source citing note) would be in the ingest file, which already captures this connection.
- [context-efficiency-is-the-central-design-concern](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) <-> source — **grounds**: Same situation — note already cites ConvexBench; forward path is in the ingest.

### Source-to-source connections

- [agentic-code-reasoning ingest](../../sources/agentic-code-reasoning.ingest.md) — **synthesizes**: The ingest already identifies the connection explicitly: "both sources independently show that explicit process structure outperforms free-form reasoning on deep reasoning tasks." ConvexBench shows this for symbolic reasoning (convexity); agentic code reasoning shows it for code semantics (patch equivalence, fault localization). The shared mechanism is: structured templates/frameworks that constrain the reasoning process recover performance that free-form approaches lose.

- [meyerson-maker-million-step-llm-zero-errors ingest](../../sources/meyerson-maker-million-step-llm-zero-errors.ingest.md) — **complements**: Both papers demonstrate that decomposition + focused context solves problems one-shot approaches cannot. MAKER goes to the extreme (one step per agent, voting for reliability); ConvexBench shows recursive decomposition with focused context. Both operate in the hard-oracle regime (Towers of Hanoi, DCP rules). Key difference: MAKER uses redundancy (voting) to handle errors; ConvexBench uses focused context to prevent errors.

- [induction-bias-sequence-models-ebrahimi-2026 ingest](../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md) — **complements**: Ebrahimi et al. explain WHY transformers fail at compositional reasoning (kappa near 1 means length-isolated learning, no transfer across depths). ConvexBench demonstrates WHAT that failure looks like in practice (F1 collapse with depth) and HOW to work around it (recursive decomposition with clean frames). The two papers bracket the problem from opposite directions — mechanism vs manifestation+mitigation.

## Rejected Candidates

- [human-writing-structures-transfer-to-llms-because-failure-modes-overlap](../../notes/human-writing-structures-transfer-to-llms-because-failure-modes-overlap.md) — While ConvexBench's "lazy reasoning" (falling back to shallow heuristics) is a human-like failure mode, the connection is too thin. The failure-mode-overlap note is about writing structures specifically, not about computational reasoning failures. The overlap is at the level of "LLMs have human-like biases" which is too generic.

- [error-correction-works-above-chance-oracles-with-decorrelated-checks](../../notes/error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — ConvexBench does not use error correction or voting. Its solution is about preventing errors through focused context, not correcting them through redundancy. The hard oracle (DCP rules) is present but not used for error correction — only for benchmark verification. The connection would be forced.

- [synthesis-is-not-error-correction](../../notes/synthesis-is-not-error-correction.md) — ConvexBench's recursive aggregation of sub-expression results is not synthesis in the sense this note discusses (merging multiple agent perspectives). Each recursive step has a single correct answer determined by the DCP rules. No genuine semantic connection.

- [methodology-enforcement-is-constraining](../../notes/methodology-enforcement-is-constraining.md) — Only surface-level vocabulary overlap (both discuss "enforcement" mechanisms). The note is about KB methodology enforcement; ConvexBench is about mathematical reasoning. Different domains, different mechanisms.

## Index Membership

- [computational-model](../../notes/computational-model-index.md) — ConvexBench provides empirical evidence for multiple notes in this area (scoping, scheduling, decomposition, frontloading). The source could be added to a "Key empirical evidence" section if the index were to track source evidence.
- [learning-theory](../../notes/learning-theory-index.md) — ConvexBench's hard-oracle benchmark design and the codification of parsing exemplify concepts in this area, but less centrally.

## Synthesis Opportunities

**1. "Compositional depth is the binding constraint, not context length"**
Multiple notes and sources converge on this claim but it has not been explicitly named:
- ConvexBench: F1 collapse at depth 100 despite 5k tokens
- [context-efficiency](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md): complexity dimension of context cost
- [llm-context-is-composed-without-scoping](../../notes/llm-context-is-composed-without-scoping.md): flat accumulation destroys reasoning
- [induction-bias-sequence-models](../../sources/induction-bias-sequence-models-ebrahimi-2026.ingest.md): kappa near 1 means transformers isolate learning by length
- The synthesis would argue: **long-context capability and long-horizon reasoning capability are architecturally independent**, and the field's focus on context-length scaling obscures the compositional-depth bottleneck that requires recursive frame isolation.

**2. "Structured decomposition consistently outperforms free-form reasoning"**
Cross-source pattern (flagged by agentic-code-reasoning ingest):
- ConvexBench: agentic framework with focused context recovers F1=1.0
- Agentic code reasoning: semi-formal templates improve patch verification to 93%
- MAKER: maximal decomposition achieves zero errors over 1M steps
- The synthesis would argue: **across symbolic, code, and execution domains, imposing structured decomposition on the reasoning process consistently recovers performance that free-form approaches lose** — the mechanism is constraining attention to relevant dependencies at each step.

## Flags

- The ConvexBench ingest file already captures all five primary connections to KB notes (context-efficiency, scoping, bitter-lesson-boundary, frontloading, oracle-strength-spectrum) and recommends updating the scoping note's "Undeveloped directions" section. That recommendation has already been partially implemented (the scoping note now cites ConvexBench in the "Recursion with clean frames" paragraph).
- The context-efficiency note also already cites ConvexBench in its complexity section. These are the two notes where the ingest's recommendations have been acted on.
- Seven new note connections identified above have NOT been established yet (symbolic-scheduling, decomposition-rules, frontloading, bitter-lesson-boundary, oracle-strength-spectrum, frontloading-loop, codification, llm-mediated-schedulers).
