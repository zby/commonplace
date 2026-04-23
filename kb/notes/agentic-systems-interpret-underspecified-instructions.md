---
description: LLM-based systems have two distinct properties — semantic underspecification of natural language specs (the deeper difference from traditional programming) and execution indeterminism (present in all practical systems) — the spec-to-program projection model captures the first, which indeterminism tends to obscure
type: kb/types/note.md
traits: [has-external-sources]
tags: [learning-theory, computational-model]
status: current
---

# Agentic systems interpret underspecified instructions

*A theoretical framing for LLM-based agentic systems — enough conceptual machinery to clarify why certain design choices make sense.*

## Two Distinct Phenomena

LLM-based systems differ from traditional programs in two ways that are often conflated but are conceptually distinct:

**1. Semantic underspecification.** Natural language specifications don't have precise denotations. "Write a summary" admits a *space* of valid interpretations — different lengths, emphases, structures. This is a property of the specification language itself, not the engine.

**2. Execution indeterminism.** The same prompt can produce different outputs across runs due to sampling (temperature > 0). This is a property of the execution engine — conceptually simpler than semantic underspecification, and largely eliminable via temperature=0, though implementation details (floating-point non-determinism, batching, infrastructure changes) mean true determinism is hard to guarantee in practice. All deployed systems exhibit indeterminism and often benefit from it.

The two are not entirely orthogonal — indeterminism is the mechanism by which different interpretations get surfaced across runs — but they are fundamentally different in kind. The first is semantics; the second is engineering.

### Indeterminism obscures the real difference

Counterintuitively, indeterminism *hides* the deeper issue rather than revealing it. Because outputs vary across runs, people attribute the variation to randomness — "it's stochastic" — and reach for familiar tools: temperature tuning, retries, sampling strategies. This provides a comfortable framework that avoids confronting the real difference from traditional programming.

If LLMs were deterministic, you'd get one stable output for a given prompt — but you'd have to ask: *why this interpretation and not any of the other equally valid ones?* That question forces you to see that the specification language doesn't have the same semantics as a formal programming language. The indeterminism lets you avoid that question by explaining everything as noise.

## Spec-to-Program Projection

A natural-language spec admits multiple valid programs. The LLM picks one:

```
Spec → choose interpretation → execute on input → output
```

The spec-to-program mapping is one-to-many — a semantic property, not a probabilistic one. Even a deterministic LLM would face it: it would always pick the same interpretation, but the user couldn't predict which one from the spec alone.

This makes LLMs different from compilers. A compiler performs a semantics-preserving translation — the source and target represent the same program, just in different languages. An LLM performs a *projection*: it collapses a space of valid interpretations to one concrete program.

The two phenomena layer on top of each other: the projection picks an interpretation (semantic underspecification), then execution of that interpretation may vary across runs (indeterminism). But the more interesting variation comes from the first source — qualitatively different strategies, not noisy executions of the same one.

### Example: "Refactor for Readability"

Ask an LLM coding assistant to refactor a function for readability. Valid interpretations include:

- Extract helper functions
- Rename variables for clarity
- Restructure control flow (loops → comprehensions)
- Add comments explaining intent

These aren't noisy variations of *one* strategy — they're different *interpretations* of "readability." The spec doesn't pick out a unique transformation; the space of valid approaches is genuinely plural.

This reframes prompt engineering: it's about narrowing the space of valid interpretations, not debugging a fixed program.

## Narrowing the Interpretation Space

The usual tools: system prompts, few-shot examples, tool definitions, output schemas, conversation history, temperature. In practice it's hard to determine which phenomenon a given mechanism addresses — a more detailed system prompt might narrow the interpretation space, or it might just make one interpretation more likely without eliminating the others. The line between "disambiguating the spec" and "biasing the engine" is rarely clean.

Temperature is often cited as purely an indeterminism control, but it's subtler than that. Lowering temperature concentrates the sampling distribution — which can change *which interpretation* you see, not just how noisily you see it. At temperature=0 the LLM still picks one interpretation from the space the spec admits; you just get the same one every time. This is why lowering temperature alone doesn't solve the "wrong interpretation" problem — it eliminates variation without ensuring the remaining interpretation is the one you wanted.

None of these eliminate ambiguity entirely. Natural language specs remain underspecified even under maximum constraint. So real systems don't just manage underspecification within LLM components — they manage the transitions between LLM and code.

## Boundaries

Agentic systems interleave LLM components and code. When execution crosses from LLM to code (or back), both phenomena flip simultaneously: LLM components carry semantic underspecification and indeterminism, code has neither. Each crossing is therefore a natural **checkpoint** — the deterministic side doesn't care how it was reached, only what arguments arrived — which anchors debugging, testing, and refactoring against the mess upstream. See [LLM↔code boundaries are natural checkpoints](./llm-code-boundaries-are-natural-checkpoints.md).

Boundaries aren't fixed. As systems evolve, logic moves across them.

## Constraining and Relaxing

Components exist on a spectrum from underspecified semantics (natural language, LLM-interpreted) to precise semantics (formal language, deterministic code). Logic can move in both directions.

**Constraining**: Replace an LLM component with a deterministic one. This does two things simultaneously: it **resolves semantic underspecification** by choosing one interpretation from the space the spec admits and committing to it in a language with precise semantics, and it **removes execution indeterminism** by eliminating sampling noise. Both matter in practice, but the semantic commitment is the deeper operation.

**Relaxing**: Replace a deterministic component with an LLM-interpreted one. Describe new functionality in natural language; the LLM figures out how to do it.

```
Underspecified (flexible, handles ambiguity)  ——constrain——>  Precise (reliable, testable, cheap)
Underspecified (flexible, handles ambiguity)  <——relax———  Precise (reliable, testable, cheap)
```

### Why constrain?

Constraining a pattern to code has four benefits — three quantitative, one qualitative:

**Cost.** LLM API calls are priced per token. A simple operation like sanitising a filename might cost fractions of a cent, but at scale those fractions compound. The same operation in code costs effectively nothing.

**Latency.** Every LLM call involves network round-trip plus inference time. Even fast models add hundreds of milliseconds. Code executes in microseconds.

**Reliability.** Deterministic code returns the same output for the same input, every time. No hallucination, no refusal, no silent behavior changes when the underlying model is updated.

**Enforcement.** Some properties — scope rules, type rules, contract checks, invariants — only exist if a deterministic interpreter checks them. Prose can describe them but can't enforce them; LLM adherence is always probabilistic. Reliability is about output consistency on typical inputs; enforcement is the binary fact that a constraint holds for *all* inputs. For properties that require enforcement, the constraining move is not optional — the alternative is to go without the guarantee. Scope is one such property ([LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md)); bookkeeping is another ([scheduler-llm-separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)).

The tradeoff: code requires you to commit to one precise interpretation. LLMs let you specify *intent* in natural language and defer the choice of interpretation to runtime. That's why constraining is progressive — you wait until patterns emerge before committing to a specific semantics.

LLM code generation is itself a constraining move, but only a one-shot form — freezing a single projection of the spec into code. Progressively extracting only the patterns that stabilize across many runs is a different mode with different tradeoffs; see [progressive constraining commits only after patterns stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md). For the wider gradient of constraining techniques — from prompt restructuring through evals to deterministic modules — see [codification](./definitions/codification.md). Either way, **version both spec and artifact** — regeneration is a new projection, not a deterministic rebuild.

### Relaxing as extension

The common path for relaxing is **extension**: you need new capability, describe it in natural language, and it becomes callable. The rarer path is **replacement**: rigid code is drowning in edge cases, so you swap it for an LLM call that handles linguistic variation.

Real systems need both directions. A component might start as an LLM call (quick to add), constrain to code as patterns emerge (reliable and fast), then grow new capabilities via relaxing. The system breathes.

## Testing and Debugging

The two phenomena create different challenges for testing and debugging.

**Testing**: Execution indeterminism means you can't rely on assertion equality for LLM outputs — you need to run the same input multiple times and check that outputs fall within acceptable bounds. In practice this looks more like sampling and checking invariants than formal hypothesis testing, but the principle holds: you're characterising a distribution, not verifying a point. Semantic underspecification means you also need to verify that the space of valid interpretations is acceptable, not just that individual outputs look right. Every piece you constrain becomes traditionally testable — because you've committed to one interpretation in a precise language.

**Debugging**: the two phenomena suggest different fixes — retry for indeterminism failures, rewrite the spec for underspecification failures. Mistaking one for the other wastes effort. See [LLM debugging starts with retry-versus-rewrite triage](./llm-debugging-starts-with-retry-versus-rewrite-triage.md).

## Design Implications

Treating agentic systems as interpreters of underspecified instructions suggests:

1. **Be explicit about semantic boundaries** — know where you're crossing between precise and underspecified semantics
2. **Enable bidirectional refactoring** — design interfaces so components can move across the boundary without rewriting call sites
3. **Narrow interpretations where reliability matters** — use schemas, constraints, and deterministic code on critical paths
4. **Preserve ambiguity where it helps** — don't over-constrain creative or genuinely open-ended tasks
5. **Version both spec and artifact** — regeneration is a new projection, not a deterministic rebuild
6. **Design for unpredictable interpretation** — the LLM may resolve ambiguity differently than you expect
7. **Constrain progressively, relax tactically** — start with underspecified for flexibility, commit to precise semantics as patterns emerge

---

Relevant Notes:

- [learning-theory](./learning-theory-index.md) — parent index: learning mechanisms, oracle theory, memory architecture
- [llm-code-boundaries-are-natural-checkpoints](./llm-code-boundaries-are-natural-checkpoints.md) — splits from this note: the boundary-as-checkpoint argument expanded with debugging, testing, and refactoring applications
- [progressive-constraining-commits-only-after-patterns-stabilize](./progressive-constraining-commits-only-after-patterns-stabilize.md) — splits from this note: the one-shot vs progressive distinction for LLM code generation as a constraining mode
- [llm-debugging-starts-with-retry-versus-rewrite-triage](./llm-debugging-starts-with-retry-versus-rewrite-triage.md) — splits from this note: the debugging heuristic derived from the two-phenomena model
- [constraining](./definitions/constraining.md) — defines the narrowing mechanism this note frames theoretically
- [codification](./definitions/codification.md) — the constraining gradient from prompt tweaks to deterministic modules
- [programming-practices-apply-to-prompting](./underspecification-and-indeterminism-complicate-programming-for-prompts-in-distinct-ways.md) — applies: typing, testing, and version control transfer to prompting under this framework
- [storing-llm-outputs-is-constraining](./storing-llm-outputs-is-constraining.md) — applies: keeping an LLM output resolves underspecification to a fixed interpretation
- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — applies: type assignment resolves semantic underspecification in both document and type definition
- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — enables: llm-do implements the movable semantic boundary through unified calling conventions
- [writing styles are strategies for managing underspecification](./writing-styles-are-strategies-for-managing-underspecification.md) — applies: the five empirically observed context-file writing styles map to different strategies for narrowing the interpretation space
- [context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — intensified by: underspecification means extra context distorts interpretation, not just wastes space — making context scarcity qualitatively worse than traditional resource constraints
- [ABC: Agent Behavioral Contracts](https://arxiv.org/html/2602.22302v1) — grounds: contracts resolve semantic underspecification with formal YAML DSL; probabilistic compliance model (p,δ,k) quantifies how tightly a contract narrows the interpretation space
- [interpretation errors are failures of the interpreter not the spec](./interpretation-errors-are-failures-of-the-interpreter.md) — bounded by: the two-phenomena model assumes a perfect interpreter; real LLMs add a third failure mode with different remedies
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — applies: scoping is one interpreter-enforced property that has to be imposed via the constraining move; sub-agents are that move for scope
- [scheduler-llm-separation exploits an error-correction asymmetry](./scheduler-llm-separation-exploits-an-error-correction-asymmetry.md) — applies: bookkeeping is another interpreter-enforced property; symbolic substrates enforce it for free while prose accumulates correction cost

Sources:

- Ma et al. (2026). [Prompt Stability in Code LLMs](https://arxiv.org/pdf/2509.13680) — strongest empirical evidence for the two-phenomena separation: emotion/personality prompt variations change code output while holding task spec constant, isolating underspecification (which interpretation?) from indeterminism (which run?)
