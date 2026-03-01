---
description: LLM-based systems have two distinct properties — execution indeterminism (present in all practical systems) and semantic fuzziness of natural language specs (the deeper difference from traditional programming) — the "program sampling" model captures the second, which indeterminism tends to obscure
type: note
traits: [has-external-sources]
areas: [learning-theory]
status: current
---

# Agentic systems interpret fuzzy specifications

*A theoretical framing for LLM-based agentic systems — enough conceptual machinery to clarify why certain design choices make sense.*

## LLMs as virtual machines

An LLM can be viewed as a virtual machine. Give it a sufficiently detailed specification, and it interprets that spec into behavior. This is more than metaphor—projects like [OpenProse](https://github.com/openprose/prose) treat the LLM explicitly as an interpreter: "A long-running AI session is a Turing-complete computer."

The key insight: **simulation with sufficient fidelity is implementation.** When an LLM receives a detailed VM specification, it *becomes* that VM through simulation. The interpreter runs inside the session.

This pure LLM VM approach has limitations:
- Every operation costs tokens (expensive at scale)
- Every step requires API round-trip (high latency)
- Specifications are in natural language (fuzzy semantics, no precise denotation)
- Execution is indeterministic (sampling noise on top of semantic fuzziness)

These limitations motivate hybrid architectures that combine LLM execution (neural) and code execution (symbolic), enabling computation to move between the two as systems evolve—stabilise patterns to code when they emerge, soften rigid code back to LLM when edge cases multiply.

## Two distinct phenomena

LLM-based systems differ from traditional programs in two ways that are often conflated but are conceptually distinct:

**1. Execution indeterminism.** The same prompt can produce different outputs across runs due to sampling (temperature > 0). This is a property of the execution engine—conceptually simpler than semantic fuzziness, and theoretically eliminable (temperature=0), though in practice all deployed systems exhibit it and often benefit from it.

**2. Semantic fuzziness.** Natural language specifications don't have precise denotations. "Refactor for readability" doesn't pick out a unique transformation—it admits a *space* of valid interpretations. This is a property of the specification language itself, not the engine. Even a perfectly deterministic LLM would still face the problem that the spec doesn't uniquely determine the output.

These two phenomena are not entirely orthogonal—indeterminism is the mechanism by which different interpretations get surfaced across runs—but they are fundamentally different in kind. The first is engineering; the second is semantics.

### Indeterminism obscures the real difference

Counterintuitively, indeterminism *hides* the deeper issue rather than revealing it. Because outputs vary across runs, people attribute the variation to randomness—"it's stochastic"—and reach for familiar tools: temperature tuning, retries, sampling strategies. This provides a comfortable framework that avoids confronting the real difference from traditional programming.

If LLMs were deterministic, you'd get one stable output for "refactor for readability"—but you'd have to ask: *why this interpretation and not any of the other equally valid ones?* That question forces you to see that the specification language doesn't have the same semantics as a formal programming language. The indeterminism lets you avoid that question by explaining everything as noise.

## Probabilistic programming as practical model

Both phenomena—fuzzy semantics and execution indeterminism—are captured by a single framework: probabilistic programming. LLM-based agentic systems interleave deterministic computation with components that interpret fuzzy natural-language specs:

```python
x = llm_call(prompt)        # fuzzy semantics + indeterminism
y = f(x)                    # deterministic
z = llm_call(prompt2(y))    # fuzzy semantics + indeterminism
```

The LLM components have two sources of variation—the semantic fuzziness of natural language specs and the execution indeterminism of the engine—while traditional code has neither. The combined distribution is too complex to characterize directly, so we reason about it through simpler mental models.

## A useful mental model: "program sampling"

Programmers often reason about LLMs as if they sample a *program* (or interpretation) from the specification, then execute it:

```
Spec → sample interpretation → execute on input → output
```

This model captures the **semantic fuzziness** phenomenon directly: the spec admits multiple valid programs, and the LLM picks one. It's fundamentally about the spec-to-program mapping being one-to-many—a semantic property, not a probabilistic one. (With indeterminism, different runs may pick different ones; without it, the LLM picks the same one consistently—but the one-to-many mapping remains.)

This makes LLMs fundamentally different from compilers. A traditional compiler performs a semantic-preserving transformation—a homeomorphism between representations where the meaning is invariant. An LLM performs a *projection*: a natural-language spec admits a space of valid interpretations, and the LLM collapses that space to one concrete program. Even a deterministic LLM would do this—it would just always pick the same interpretation, with no principled way for the user to predict which one from the spec alone.

Mathematically, this projection is a mixture model:

```
D(Output | Spec, Input) ≈ Σ Pr[Program | Spec] · D(Output | Program, Input)
```

The mixture over programs captures the semantic fuzziness—multiple valid interpretations of the spec. The `D(Output | Program, Input)` term captures execution indeterminism—variation within a single interpretation. Both are present in practice, but the program-sampling model highlights that the more interesting variation comes from the first source.

### Example: "Refactor for readability"

Ask an LLM coding assistant to refactor a function for readability. Valid interpretations include:

- Extract helper functions
- Rename variables for clarity
- Restructure control flow (loops → comprehensions)
- Add comments explaining intent

These aren't noisy variations of *one* strategy—they're different *interpretations* of "readability." The spec doesn't pick out a unique transformation; the space of valid refactoring approaches is genuinely plural. A deterministic LLM would still have to choose one—but you couldn't predict which from the spec alone, and you'd have no basis to say it chose wrong.

We don't claim this is how LLMs actually work internally. But as a mental model for reasoning about the semantic gap between natural language specs and concrete behavior, it's useful: prompt engineering becomes about narrowing the space of valid interpretations, not debugging a fixed program.

## Narrowing the interpretation space

In probabilistic programming, you shape distributions through priors, conditioning, and constraints. With LLMs, you use different mechanisms—but the goal is the same: **narrowing the space of interpretations the LLM might choose**.

| Mechanism | Effect |
|-----------|--------|
| System prompt | Sets prior expectations, narrows toward intended behavior |
| Few-shot examples | Shifts probability mass toward demonstrated patterns |
| Tool definitions | Biases toward valid actions; can truncate support when tool-only decoding is enforced |
| Output schemas | Constrain structure and sometimes content (enums, ranges, regexes) |
| Conversation history | Dynamic reshaping as context accumulates |
| Temperature | Flattens or sharpens the distribution at sampling time |

Understanding these as **distribution-shaping techniques** clarifies what each can and can't do—and which phenomenon each addresses. Temperature operates on execution indeterminism only; it sharpens or flattens the sampling without changing what the spec means. Examples and detailed instructions operate on semantic fuzziness; they narrow the space of valid interpretations. Schemas and tool definitions do both: they constrain structure (reducing indeterminism) and sometimes eliminate entire classes of interpretation (reducing fuzziness). But none eliminate the ambiguity entirely—natural language specs remain fuzzy even under maximum constraint.

## Semantic boundaries

Agentic systems interleave components with fuzzy semantics (LLM) and precise semantics (code). When an LLM calls a tool, or a tool triggers an LLM, execution crosses a **semantic boundary**.

```
Fuzzy semantics → Precise semantics → Fuzzy semantics
     (LLM)             (tool)              (LLM)
 interpretation      exact function      interpretation
```

At each crossing:
- **Fuzzy → Precise**: The LLM's interpretation is consumed by code that treats it as a concrete value. The code doesn't know or care that the input could have been different under a different interpretation of the spec.
- **Precise → Fuzzy**: A concrete value enters a component that interprets a natural-language spec to decide what to do with it. The spec doesn't uniquely determine the behavior; the LLM resolves the ambiguity.

These boundaries are natural **checkpoints**. The deterministic code doesn't care how it was reached—only what arguments it received. This matters for debugging, testing, and reasoning about the system.

But boundaries aren't fixed. As systems evolve, logic moves across them.

## Stabilising and softening

Components exist on a spectrum from fuzzy semantics (natural language, LLM-interpreted) to precise semantics (formal language, deterministic code). Logic can move in both directions.

**Stabilising**: Replace an LLM component with a deterministic one. This does two things simultaneously: it **resolves semantic fuzziness** by choosing one interpretation from the space the spec admits and committing to it in a language with precise semantics, and it **removes execution indeterminism** by eliminating sampling noise. Both matter in practice, but the semantic commitment is the deeper operation.

**Softening**: Replace a deterministic component with an LLM-interpreted one. Describe new functionality in natural language; the LLM figures out how to do it.

```
Fuzzy (flexible, handles ambiguity)  ——stabilise——>  Precise (reliable, testable, cheap)
Fuzzy (flexible, handles ambiguity)  <——soften———  Precise (reliable, testable, cheap)
```

### Why stabilise?

Stabilising a pattern to code has three practical benefits:

**Cost.** LLM API calls are priced per token. A simple operation like sanitising a filename might cost fractions of a cent, but at scale those fractions compound. The same operation in code costs effectively nothing.

**Latency.** Every LLM call involves network round-trip plus inference time. Even fast models add hundreds of milliseconds. Code executes in microseconds.

**Reliability.** Deterministic code returns the same output for the same input, every time. No hallucination, no refusal, no drift across model versions.

The tradeoff: code requires you to commit to one precise interpretation. LLMs let you specify *intent* in fuzzy natural language and defer the choice of interpretation to runtime. That's why stabilising is progressive—you wait until patterns emerge before committing to a specific semantics.

### One-shot vs progressive stabilising

LLMs can act as compilers: spec in, code out. But as the program-sampling model makes clear, this is projection from a fuzzy spec, not compilation—the LLM resolves the semantic ambiguity, producing one valid implementation from the space the spec admits, with no way to predict which one from the spec alone. This is one-shot stabilising: freeze a single resolution into code.

Alternatively, you can stabilise incrementally. As you observe the LLM's behavior across many runs, you learn which interpretations it consistently chooses—and can extract those stable patterns into deterministic code while keeping the LLM for genuinely ambiguous cases.

Example: a file-renaming agent initially uses LLM judgment for everything. You notice it always lowercases and replaces spaces with underscores—so you extract `sanitize_filename()` to code. The agent still handles ambiguous cases ("is '2024-03' a date or a version?"), but the common path is now deterministic.

Either way, **version both spec and artifact**. Regeneration is a new projection from the same spec—potentially a different resolution of the same ambiguity, not a deterministic rebuild. Don't treat "re-generate later" as a build step.

For the gradient of stabilisation techniques — from prompt restructuring through evals to deterministic modules — see [crystallisation](./crystallisation.md).

### Softening as extension

The common path for softening is **extension**: you need new capability, describe it in natural language, and it becomes callable. The rarer path is **replacement**: rigid code is drowning in edge cases, so you swap it for an LLM call that handles linguistic variation.

Real systems need both directions. A component might start as an LLM call (quick to add), stabilise to code as patterns emerge (reliable and fast), then grow new capabilities via softening. The system breathes.

## Testing and debugging

LLM components require different approaches, and the two phenomena create different challenges.

**Testing**: Execution indeterminism means you run the same input N times and check the distribution of outputs—statistical hypothesis testing, not assertion equality. Semantic fuzziness means you also need to verify that the space of valid interpretations is acceptable, not just that individual outputs look right. Every piece you stabilise becomes traditionally testable—because you've committed to one interpretation in a precise language.

**Debugging**: When a prompt "fails," you need to distinguish between the two phenomena. Is the LLM producing a bad execution of a good interpretation (indeterminism problem—may not reproduce)? Or is it consistently choosing an interpretation you didn't intend (fuzziness problem—the spec admits it, so it will recur)? The fix is different: retry vs. rewrite the spec.

## Design implications

Treating agentic systems as interpreters of fuzzy specifications suggests:

1. **Be explicit about semantic boundaries**—know where you're crossing between precise and fuzzy semantics
2. **Enable bidirectional refactoring**—design interfaces so components can move across the boundary without rewriting call sites
3. **Narrow interpretations where reliability matters**—use schemas, constraints, and deterministic code on critical paths
4. **Preserve ambiguity where it helps**—don't over-constrain creative or genuinely open-ended tasks
5. **Version both spec and artifact**—regeneration is a new projection, not a deterministic rebuild
6. **Design for unpredictable interpretation**—the LLM may resolve ambiguity differently than you expect
7. **Stabilise progressively, soften tactically**—start with fuzzy specs for flexibility, commit to precise semantics as patterns emerge

---

Relevant Notes:
- [learning-theory](./learning-theory.md) — parent index: learning mechanisms, oracle theory, memory architecture
- [stabilisation](./stabilisation.md) — defines the narrowing mechanism this note frames theoretically
- [crystallisation](./crystallisation.md) — the stabilisation gradient from prompt tweaks to deterministic modules
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — applies: typing, testing, and version control transfer to prompting under this framework
- [storing-llm-outputs-is-stabilization](./storing-llm-outputs-is-stabilization.md) — applies: keeping an LLM output resolves fuzziness to a fixed interpretation
- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — applies: type assignment resolves semantic fuzziness in both document and type definition
- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — enables: llm-do implements the movable semantic boundary through unified calling conventions

Topics:
- [learning-theory](./learning-theory.md)
