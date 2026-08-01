# Case packet

Neutral case identifier: case-5fea6da992bdb6

The possible directed relationship from Artifact A to Artifact B is under review.

## Artifact A

# Specification-level separation recovers scoping before it recovers error correction

OpenProse is a useful tension case for the [scheduler-LLM separation conjecture]. It tries to make an LLM session behave like a symbolic executor without moving the interpreter into code. The repo provides a workflow DSL (`.prose`), an execution specification (`prose.md`), a compile/validation specification (`compiler.md`), and explicit state protocols for files and databases. That is not the clean model. But it is not just flat prompting either.

The important observation is that some benefits of separation arrive *before* the medium boundary. OpenProse names control-flow structure (`parallel`, `retry`, `resume`, loops), makes discretionary judgments explicit via `**...**`, and externalises intermediate state into bindings and agent memory files instead of keeping everything in one conversation. Those are real gains. They reduce prompt ambiguity, create cleaner frame boundaries, and recover some of the scoping benefits described in [LLM context is composed without scoping].

What does **not** arrive yet is the main reliability mechanism from the error-correction note. The parser, validator, scheduler, and branch evaluator are still LLM-mediated. `prose compile` is another natural-language specification interpreted by the model, not a deterministic parser. `**...**` conditions are explicit soft-oracle checkpoints. Even the "VM" is induced behavior inside an existing agent runtime rather than a substrate with discrete-state restoration. The boundary between symbolic bookkeeping and semantic judgment is *named*, but not yet *hardened*.

This creates an intermediate regime:

- **Flat prompting** — no explicit scheduler vocabulary, no stable frame interfaces, state mostly lives in conversation
- **Specification-level separation** — control flow is named, state protocols are externalised, judgment holes are marked, but execution still depends on LLM compliance
- **Architectural separation** — bookkeeping moves to code or another hard-oracle substrate; the LLM handles only the semantic steps

The intermediate regime matters because it explains why systems like OpenProse can feel substantially better than raw prompting without yet earning the full error-correction benefits of symbolic execution. Syntax and file protocols can recover scoping, resumability, and some orchestration discipline before they recover hard reliability. The scheduler note should therefore not read as a binary "either fully separated or worthless." There is a meaningful middle ground.

This ordering — scoping first, error correction second — is specific to specification-level approaches that work by naming structure within the LLM's own execution. Tool-use frameworks (function calling with typed parameters, JSON schema validation) take a different path: they codify the interface contract, giving hard-oracle checks on output format without recovering scoping within the LLM's reasoning. That is mini-codification at the boundary, not specification-level separation — a different route to partial reliability that does not pass through the intermediate regime described here.

The cost of staying in that middle ground is that bookkeeping is still paid for on the stochastic substrate. The system can mark the symbolic/semantic boundary, but it cannot use hard oracles to enforce most of it. This means the asymmetry from [scheduler-LLM separation exploits an error-correction asymmetry] still applies; OpenProse shows where the scoping gains start, not where the error-correction argument stops.

---

Relevant Notes:

- [programming practices apply to prompting] — explains why a DSL and explicit state protocols help before codification

## Artifact B

# LLM context is composed without scoping

An LLM's context is assembled by concatenating system prompts, skill bodies, user messages, and tool outputs into a single token stream. Everything is global: every token is visible to every other token, with no way to say "this binding is local to this skill" or "this tool output should not influence instruction interpretation."

This is not even dynamic scoping (name bindings resolved through the call stack rather than the source structure), which at least maintains a stack with push and pop. Flat concatenation is the [homoiconic medium] (instructions and data share one representation) with no structure imposed on top, yet it produces dynamic scoping's pathologies — and the Lisp analogy still clarifies them:

**Spooky action at a distance.** An early turn subtly biases a later response. The LLM has no mechanism to mark a binding as out of scope — once something enters the log, it influences everything downstream. This is the [three-space memory claim's] "operational debris pollutes search" failure mode, restated as a scoping problem.

**Name collision.** "Table" meant an HTML element in turn 3 but a database table in turn 12, and the model conflates them. A flat log has no scope boundaries to disambiguate — every use of a term sits in one namespace.

**Inability to reason locally.** You cannot predict what a sub-task will do by reading its prompt alone; its behavior depends on the entire accumulated history. This is the defining problem of dynamic scope: the meaning of a name depends on the call stack, not the definition site.

## The capture problem

Flat concatenation creates a composition-specific problem: **capture**. A skill says "summarize the document." The document contains "don't summarize this section, skip it." The data-level use of "summarize" captures the instruction-level meaning. This is a hygiene failure that leads to prompt injection — the same problem Scheme's hygienic macros (macros that rewrite code without accidentally capturing names from the call site) solve for code generation.

## Within-frame hygiene

Within a single context, the only scoping mechanisms available are weak conventions:

- **Role markers** (system/user/assistant/tool in chat APIs) — primitive structural separation, but the LLM still sees all roles in one attention pass
- **Delimiters and quoting** — XML tags, markdown fences, explicit "the following is data, not instructions" markers — conventional, not enforced
- **Ordering conventions** — system prompt first, then context, then user message — exploits primacy/recency effects but provides no isolation

These are the LLM equivalent of coding conventions in a language without a module system. They help, but they cannot prevent capture — and they cannot disable **non-selective semantic integration**: prompt semantics the task contract does not license still steer generation, because every token shares one global attention field.

## Non-selective semantic integration

"Spooky action at a distance" is measurable, not only architectural. [GSM-DC] varies synthetic distractor count in math word problems and finds power-law error growth — the clean control where irrelevant material is semantically inert noise. [Gonen et al.] varies injected concepts in completion prompts and finds Leak-Rate well above chance even when the concept is task-irrelevant (**semantic leakage**). [Lampinen et al.] varies belief-congruence on logic tasks. These studies are not independent interference axes; they stress the same flat-context failure under different doses and task grains. Benchmark labels (noise, association, content bias) describe what each experiment varied, not separate mechanisms requiring separate mitigations.

The realistic case — semantically linked material that should not govern the task — is what agent workflows encounter. [Context contamination below compliance reasoning] is that failure at agent dose: fine-grained stance drift despite expressed refusal. Counter-instructions can bias against integration; they cannot remove tokens from the window or make a scope boundary binding.

## What flat context buys

Flat logs have a real upside: implicit communication. When a user says "use a more formal tone" in turn 5, the effect propagates to later turns without re-parameterizing. This ambient influence is what makes flat context ergonomic at single-call granularity. The design question is not whether to have the upside, but where to contain it.

## The architectural response

The scoping problem is specific to natural-language content. Symbolic artifacts (code, schemas, types) inherit scoping from their interpreter; distributed-parametric artifacts do not expose this kind of local natural-language scope question. Natural-language content has nothing to inherit: no modules, no lexical scope, no interpreter-enforced boundaries. Scope can only be imposed architecturally.

At invocation time this surfaces as a design choice — **flat (parent context)** or **bounded (sub-agent frame)** — same representational form, same substrate, same authority path, different context-efficiency profile. Flat pays the full volume and complexity cost and risks contamination; bounded trades an interface cost for isolation.

**Sub-agents** are the canonical architectural move: code outside the LLM constructs a fresh flat context, the LLM sees only that, and the scope lives in the orchestration code rather than in the LLM itself.

This is one specialization of the general constraining argument in [agentic systems interpret underspecified instructions] — enforcement is the qualitative reason to move a property to code, distinct from the quantitative reasons (cost, latency, reliability). The error-profile version is [scheduler-llm-separation exploits an error-correction asymmetry]: bookkeeping has catastrophic error cost on the semantic substrate (the LLM) and zero error cost on the symbolic substrate (the surrounding code). Scope is bookkeeping, so it belongs on the symbolic side.

Empirical validation comes from ConvexBench ([Liu et al., 2026]), a benchmark for recognizing convexity in deeply composed symbolic functions: LLMs collapse from F1=1.0 to F1≈0.2 at depth 100, even though the total token count (~5,331) is trivial relative to the context window. The failure is compositional reasoning depth, not token capacity — each recursive step conditions on an expanding history that dilutes attention on the current step. Pruning to retain only direct dependencies at each sub-step (one clean frame per call) recovers F1=1.0 at all depths.

---

Sources:
- Anthropic (2025). [Effective context engineering for AI agents] — recommends sub-agents return 1,000–2,000 token summaries; the tens of thousands of tokens each sub-agent explores stay out of the caller's window. Validates the lexically scoped frames pattern.
- Yang et al. (2025). [GSM-DC] — power-law reasoning degradation under synthetic distractor count; the inert-noise control regime for non-selective integration.
- Gonen et al. (2024/2025). [Semantic leakage in language models] — control/test Leak-Rate metric; instruction-tuned models leak more.
- Lampinen et al. (2024). [Content effects on reasoning tasks] — belief-congruent content shifts logic-task accuracy across model families.

Relevant Notes:

- [unified calling conventions enable bidirectional refactoring] — existing approximation: llm-do's per-agent system prompts and arguments are frame-local context

## Under-review context phrase

the main gains OpenProse gets early are scoping gains, not hard reliability gains
