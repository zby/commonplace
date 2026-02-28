---
description: LLM-based systems interleave deterministic and stochastic computation — the "program sampling" model explains why the same prompt produces qualitatively different behaviors, not just noisy variations
type: note
traits: [has-external-sources]
areas: [learning-theory]
status: current
---

# Agentic systems are probabilistic programs

*A theoretical framing for LLM-based agentic systems — enough conceptual machinery to clarify why certain design choices make sense.*

## LLMs as virtual machines

An LLM can be viewed as a virtual machine. Give it a sufficiently detailed specification, and it interprets that spec into behavior. This is more than metaphor—projects like [OpenProse](https://github.com/openprose/prose) treat the LLM explicitly as an interpreter: "A long-running AI session is a Turing-complete computer."

The key insight: **simulation with sufficient fidelity is implementation.** When an LLM receives a detailed VM specification, it *becomes* that VM through simulation. The interpreter runs inside the session.

This pure LLM VM approach has limitations:
- Every operation costs tokens (expensive at scale)
- Every step requires API round-trip (high latency)
- All execution is stochastic (unpredictable)

These limitations motivate hybrid architectures that combine LLM execution (neural) and code execution (symbolic), enabling computation to move between the two as systems evolve—stabilise patterns to code when they emerge, soften rigid code back to LLM when edge cases multiply.

## Probabilistic programming as foundation

LLM-based agentic systems are naturally understood as **probabilistic programs**: programs that interleave deterministic computation with sampling from distributions.

```python
x = sample(distribution)    # stochastic
y = f(x)                    # deterministic
z = sample(another_dist(y)) # stochastic
```

What's distinctive about agentic systems is that some components have **unknown, high-variance distributions** (the LLM) while others have **known, deterministic behavior** (traditional code). The LLM's distribution is shaped by prompts, examples, and context—but we don't have direct access to its parameters or structure. The distribution is too complex to characterize directly, so we reason about it through simpler mental models.

## A useful mental model: "program sampling"

Programmers often reason about LLMs as if they sample a *program* (or interpretation) from the specification, then execute it:

```
Spec → sample interpretation → execute on input → output
```

This captures why the same prompt can produce qualitatively different behaviors, not just noisy variations of the same behavior—the *interpretation* varies, not just the execution.

This makes LLMs fundamentally different from compilers. A traditional compiler performs a semantic-preserving transformation—a homeomorphism between representations where the meaning is invariant. An LLM performs a *stochastic projection*: a natural-language spec admits a space of valid interpretations, and each run collapses that space to one concrete program. The variance is not translation noise—it's the inherent ambiguity of the source being resolved differently each time.

Mathematically, this projection is a mixture model:

```
D(Output | Spec, Input) ≈ Σ Pr[Program | Spec] · D(Output | Program, Input)
```

If you treat `Program` as deterministic, `D(Output | Program, Input)` collapses to a point mass; most of the variance comes from the mixture over programs.

### Example: "Refactor for readability"

Ask an LLM coding assistant to refactor a function for readability. Different runs might:

- Extract helper functions
- Rename variables for clarity
- Restructure control flow (loops → comprehensions)
- Add comments explaining intent

These aren't noisy variations of *one* strategy—they're different *interpretations* of "readability." Each run samples a different program from the space of valid refactoring approaches.

We don't claim this is how LLMs actually work internally. But as a mental model for reasoning about complex, opaque distributions, it's useful: prompt engineering becomes about shaping a distribution over *behaviors*, not debugging a fixed program.

## Shaping the distribution

In probabilistic programming, you shape distributions through priors, conditioning, and constraints. With LLMs, you use different mechanisms—but the goal is the same: **narrowing the distribution toward desired behaviors**.

| Mechanism | Effect |
|-----------|--------|
| System prompt | Sets prior expectations, narrows toward intended behavior |
| Few-shot examples | Shifts probability mass toward demonstrated patterns |
| Tool definitions | Biases toward valid actions; can truncate support when tool-only decoding is enforced |
| Output schemas | Constrain structure and sometimes content (enums, ranges, regexes) |
| Conversation history | Dynamic reshaping as context accumulates |
| Temperature | Flattens or sharpens the distribution at sampling time |

Understanding these as **distribution-shaping techniques** clarifies what each can and can't do. Examples shift the mode; schemas constrain the support; temperature reshapes the distribution without changing the underlying model. Each narrows the projection—reducing the space of interpretations the LLM might sample—but none eliminate the ambiguity entirely.

## Distribution boundaries

Probabilistic programs naturally interleave stochastic and deterministic computation. When an LLM calls a tool, or a tool triggers an LLM, execution crosses a **distribution boundary**.

```
Stochastic → Deterministic → Stochastic
   (LLM)        (tool)         (LLM)
distribution   point mass    distribution
```

At each crossing:
- **Stochastic → Deterministic**: Variance usually collapses. Given the same arguments (and environment), the tool returns the same output regardless of how the arguments were produced.
- **Deterministic → Stochastic**: Variance is introduced. A fixed input enters a component that produces a distribution over outputs.

These boundaries are natural **checkpoints**. The deterministic code doesn't care how it was reached—only what arguments it received. This matters for debugging, testing, and reasoning about the system.

But boundaries aren't fixed. As systems evolve, logic moves across them.

## Stabilising and softening

Components exist on a spectrum from stochastic to deterministic. Logic can move in both directions.

**Stabilising**: Replace a stochastic component with a deterministic one. Choose one interpretation from the space the spec admits and freeze it into code, configuration, or a decision that no longer varies.

**Softening**: Replace a deterministic component with a stochastic one. Describe new functionality in natural language; the LLM figures out how to do it.

```
Stochastic (flexible, handles ambiguity)  ——stabilise——>  Deterministic (reliable, testable, cheap)
Stochastic (flexible, handles ambiguity)  <——soften———  Deterministic (reliable, testable, cheap)
```

### Why stabilise?

Stabilising a pattern to code has three practical benefits:

**Cost.** LLM API calls are priced per token. A simple operation like sanitising a filename might cost fractions of a cent, but at scale those fractions compound. The same operation in code costs effectively nothing.

**Latency.** Every LLM call involves network round-trip plus inference time. Even fast models add hundreds of milliseconds. Code executes in microseconds.

**Reliability.** Deterministic code returns the same output for the same input, every time. No hallucination, no refusal, no drift across model versions.

The tradeoff: code requires you to know the exact behavior upfront. LLMs let you specify *intent* and figure out the details. That's why stabilising is progressive—you wait until patterns emerge before committing to code.

### One-shot vs progressive stabilising

LLMs can act as compilers: spec in, code out. But as the program-sampling model makes clear, this is stochastic projection, not compilation—each run samples a different valid implementation from the space the spec admits. This is one-shot stabilising: freeze a single sample into code.

Alternatively, you can stabilise incrementally. As you observe the LLM's behavior across many runs, you learn which "programs" it tends to sample—and can extract the consistent patterns into deterministic code while keeping the stochastic component for genuinely ambiguous cases.

Example: a file-renaming agent initially uses LLM judgment for everything. You notice it always lowercases and replaces spaces with underscores—so you extract `sanitize_filename()` to code. The agent still handles ambiguous cases ("is '2024-03' a date or a version?"), but the common path is now deterministic.

Either way, **version both spec and artifact**. Regeneration is a new projection from the same spec—a different sample, not a deterministic rebuild. Don't treat "re-generate later" as a build step.

For the gradient of stabilisation techniques — from prompt restructuring through evals to deterministic modules — see [crystallisation](./crystallisation.md).

### Softening as extension

The common path for softening is **extension**: you need new capability, describe it in natural language, and it becomes callable. The rarer path is **replacement**: rigid code is drowning in edge cases, so you swap it for an LLM call that handles linguistic variation.

Real systems need both directions. A component might start as an LLM call (quick to add), stabilise to code as patterns emerge (reliable and fast), then grow new capabilities via softening. The system breathes.

## Testing and debugging

Stochastic components require different approaches.

**Testing**: Run the same input N times. Check that the distribution of outputs meets expectations—statistical hypothesis testing, not assertion equality. Every piece you stabilise becomes traditionally testable.

**Debugging**: When a prompt "fails," you're not tracing execution—you're reshaping a distribution. The failure might not reproduce. This is why prompt engineering is empirical.

## Design implications

Treating agentic systems as probabilistic programs suggests:

1. **Be explicit about boundaries**—know where you're crossing between deterministic and stochastic execution
2. **Enable bidirectional refactoring**—design interfaces so components can move across the boundary without rewriting call sites
3. **Reduce variance where reliability matters**—use schemas, constraints, and deterministic code on critical paths
4. **Preserve variance where it helps**—don't over-constrain creative or ambiguous tasks
5. **Version both spec and artifact**—regeneration is a new projection, not a deterministic rebuild
6. **Design for statistical failure**—expect retries and graceful degradation
7. **Stabilise progressively, soften tactically**—start stochastic for flexibility, extract determinism as patterns emerge

---

Relevant Notes:
- [learning-theory](./learning-theory.md) — parent index: learning mechanisms, oracle theory, memory architecture
- [stabilisation](./stabilisation.md) — defines the narrowing mechanism this note frames theoretically
- [crystallisation](./crystallisation.md) — the stabilisation gradient from prompt tweaks to deterministic modules
- [programming-practices-apply-to-prompting](./programming-practices-apply-to-prompting.md) — applies: typing, testing, and version control transfer to prompting under this probabilistic model
- [storing-llm-outputs-is-stabilization](./storing-llm-outputs-is-stabilization.md) — applies: keeping an LLM output collapses a distribution to a point
- [document-types-should-be-verifiable](./document-types-should-be-verifiable.md) — applies: type assignment is stochastic projection under this framework
- [unified-calling-conventions-enable-bidirectional-refactoring](./unified-calling-conventions-enable-bidirectional-refactoring.md) — enables: llm-do implements the movable boundary through unified calling conventions over a hybrid VM

Topics:
- [learning-theory](./learning-theory.md)
