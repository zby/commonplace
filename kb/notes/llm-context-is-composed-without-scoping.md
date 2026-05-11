---
description: LLM context is flat concatenation — no scoping, everything global, producing dynamic scoping's pathologies (spooky action at a distance, name collision, inability to reason locally) but without even a stack; scoping must be imposed architecturally via code-constructed sub-agent contexts
type: kb/types/note.md
traits: [has-external-sources, title-as-claim]
tags: [computational-model]
status: seedling
---

# LLM context is composed without scoping

An LLM's context is assembled by concatenating system prompts, skill bodies, user messages, and tool outputs into a single token stream. Everything is global: every token is visible to every other token, with no way to say "this binding is local to this skill" or "this tool output should not influence instruction interpretation."

This is not even dynamic scoping (name bindings resolved through the call stack rather than the source structure), which at least maintains a stack with push and pop. Flat concatenation is the [homoiconic medium](./llm-context-is-a-homoiconic-medium.md) (instructions and data share one representation) with no structure imposed on top, yet it produces dynamic scoping's pathologies — and the Lisp analogy still clarifies them:

**Spooky action at a distance.** An early turn subtly biases a later response. The LLM has no mechanism to mark a binding as out of scope — once something enters the log, it influences everything downstream. This is the [three-space memory claim's](./flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable.md) "operational debris pollutes search" failure mode, restated as a scoping problem.

**Name collision.** "Table" meant an HTML element in turn 3 but a database table in turn 12, and the model conflates them. A flat log has no scope boundaries to disambiguate — every use of a term sits in one namespace.

**Inability to reason locally.** You cannot predict what a sub-task will do by reading its prompt alone; its behavior depends on the entire accumulated history. This is the defining problem of dynamic scope: the meaning of a name depends on the call stack, not the definition site.

## The capture problem

Flat concatenation creates a composition-specific problem: **capture**. A skill says "summarize the document." The document contains "don't summarize this section, skip it." The data-level use of "summarize" captures the instruction-level meaning. This is a hygiene failure that leads to prompt injection — the same problem Scheme's hygienic macros (macros that rewrite code without accidentally capturing names from the call site) solve for code generation.

## Within-frame hygiene

Within a single context, the only scoping mechanisms available are weak conventions:

- **Role markers** (system/user/assistant/tool in chat APIs) — primitive structural separation, but the LLM still sees all roles in one attention pass
- **Delimiters and quoting** — XML tags, markdown fences, explicit "the following is data, not instructions" markers — conventional, not enforced
- **Ordering conventions** — system prompt first, then context, then user message — exploits primacy/recency effects but provides no isolation

These are the LLM equivalent of coding conventions in a language without a module system. They help, but they cannot prevent capture.

## What flat context buys

Flat logs have a real upside: implicit communication. When a user says "use a more formal tone" in turn 5, the effect propagates to later turns without re-parameterizing. This ambient influence is what makes flat context ergonomic at single-call granularity. The design question is not whether to have the upside, but where to contain it.

## The architectural response

The scoping problem is prose-specific. Symbolic artifacts (code, schemas, types) inherit scoping from their interpreter; distributed-parametric artifacts do not expose this kind of local prose scope question. Prose has nothing to inherit: no modules, no lexical scope, no interpreter-enforced boundaries. Scope can only be imposed architecturally.

At invocation time this surfaces as a design choice — **flat (parent context)** or **bounded (sub-agent frame)** — same representational form, same substrate, same authority path, different context-efficiency profile. Flat pays the full volume and complexity cost and risks contamination; bounded trades an interface cost for isolation.

**Sub-agents** are the canonical architectural move: code outside the LLM constructs a fresh flat context, the LLM sees only that, and the scope lives in the orchestration code rather than in the LLM itself.

This is one specialization of the general constraining argument in [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — enforcement is the qualitative reason to move a property to code, distinct from the quantitative reasons (cost, latency, reliability). The error-profile version is [scheduler-llm-separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md): bookkeeping has catastrophic error cost on the semantic substrate (the LLM) and zero error cost on the symbolic substrate (the surrounding code). Scope is bookkeeping, so it belongs on the symbolic side.

Empirical validation comes from ConvexBench ([Liu et al., 2026](https://arxiv.org/html/2602.01075v2)), a benchmark for recognizing convexity in deeply composed symbolic functions: LLMs collapse from F1=1.0 to F1≈0.2 at depth 100, even though the total token count (~5,331) is trivial relative to the context window. The failure is compositional reasoning depth, not token capacity — each recursive step conditions on an expanding history that dilutes attention on the current step. Pruning to retain only direct dependencies at each sub-step (one clean frame per call) recovers F1=1.0 at all depths.

---

Sources:
- Anthropic (2025). [Effective context engineering for AI agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) — recommends sub-agents return 1,000–2,000 token summaries; the tens of thousands of tokens each sub-agent explores stay out of the caller's window. Validates the lexically scoped frames pattern.

Relevant Notes:

- [llm context is a homoiconic medium](./llm-context-is-a-homoiconic-medium.md) — amplifies: the medium provides no structural boundaries, so scoping must be imposed by architecture
- [agent orchestration needs coordination guarantees, not just coordination channels](./agent-orchestration-needs-coordination-guarantees-not-just-coordination-channels.md) — extends: scoping is one coordination guarantee family; without it, flat context fails by contamination rather than by inconsistency or amplification
- [three-space memory separation predicts measurable failure modes](./flat-memory-predicts-specific-cross-contamination-failures-that-are-empirically-testable.md) — exemplifies: the failure modes (search pollution, identity scatter, insight trapping) are symptoms of flat scoping applied to memory
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — grounds: prose has no deterministic interpreter, so scope guarantees — like other interpreter-enforced semantics — must be imposed via the constraining move to code; sub-agents are that move applied to scope
- [unified calling conventions enable bidirectional refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — existing approximation: llm-do's per-agent system prompts and arguments are frame-local context
- [codification](./definitions/codification.md) — enables: frame boundaries are interface points where return values can be progressively typed
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — grounds: the loading hierarchy is a form of binding-time analysis for what's in scope
- [agent statelessness makes routing architectural, not learned](./agent-statelessness-makes-routing-architectural-not-learned.md) — exemplifies: the routing tier separation is lexical scoping in practice
- [instructions are typed callables](./instructions-are-typed-callables.md) — enables: type signatures on skills are frame interfaces — declaring what bindings a sub-agent receives
- [agent statelessness means the context engine should inject context automatically](./agent-statelessness-means-the-context-engine-should-inject-context-automatically.md) — mechanism: automatic context injection constructs lexically scoped frames
- [topology, isolation, and verification form a causal chain for reliable agent scaling](./topology-isolation-and-verification-form-a-causal-chain-for-reliable-agent-scaling.md) — extends: argues that scope isolation is the second prerequisite in a dependency chain, manufacturing the atomic units that verification needs
- [axes of artifact analysis](./axes-of-artifact-analysis.md) — refines: the flat/bounded invocation choice is a prose-form refinement, orthogonal to the substrate/form/lineage/authority record but only applicable inside prose
- [scheduler-llm-separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — grounds: scoping is bookkeeping, and bookkeeping belongs in the symbolic substrate — sub-agents are the canonical offload of prose-scoping to code
