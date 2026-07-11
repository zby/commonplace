---
description: Four lenses on the codify-vs-LLM decision — spec completeness, oracle strength, interpretation space, pattern stability — collected from across the KB, with evidence they come apart at the edges
type: kb/types/note.md
traits: []
tags: [learning-theory, constraining]
---

# Codify-versus-LLM decision heuristics

Should this component be deterministic code or an LLM call? The KB has accumulated heuristics for this question from several angles. This note collects them.

## Four lenses on the same decision

The KB offers at least four framings. They often agree in practice but ask different questions, and it's not obvious they reduce to a single criterion.

### 1. Spec completeness — is the spec a definition or a theory?

The [fixed-artifact distinction](./fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) draws the line. **Exact specs** fully capture the problem — the specification of multiplication is multiplication. Deterministic code is pure win. **Proxy theories** approximate the problem — "detect edges" was a plausible theory of what seeing requires, not a definition. The component can satisfy its local spec and still fail to compose into the target capability.

Confidence signals:
- Is correctness fully specifiable? (definition → codify)
- Is the spec a definition or a proxy metric? (proxy → leave for LLM)
- Are failures local or compositional? (compositional → the specs are probably theories)

### 2. Oracle strength — how cheaply can you verify correctness?

The [oracle strength spectrum](./oracle-strength-spectrum.md) turns the binary into a gradient:

| Oracle | Verification | Codification fitness |
|---|---|---|
| Hard | Exact, cheap, deterministic (tests, types, schema) | Natural codification candidate |
| Soft | Proxy score (BLEU, rubrics, heuristic checks) | Partial — codify the proxy, leave the judgment |
| Interactive | Feedback available (user edits, preference pairs) | Extract deterministic rules from the feedback over time ([spec mining](./spec-mining-as-codification.md)) |
| Delayed | Signal arrives later (user churn, bug surfaces) | Resist codification until signal accumulates |
| No oracle | Vibes and anecdotes | Leave for LLM + human review |

### 3. Interpretation space — does the spec admit one valid output or many?

The [underspecification framing](./agentic-systems-interpret-underspecified-instructions.md) asks a different question. "Parse this YAML" has one correct output. "Refactor for readability" admits extract-helpers, rename-variables, restructure-control-flow, add-comments — all valid, qualitatively different.

Under this lens, codification is fundamentally about **committing to one interpretation** from a space the spec admits. [Constraining](./definitions/constraining.md) narrows the space; [codification](./definitions/codification.md) collapses it to a point by crossing into executable code. The risk isn't wrong code — it's wrong commitment. If the problem genuinely has many valid interpretations, codifying one loses the others.

### 4. Pattern stability — has this emerged across enough runs?

The [codification definition](./definitions/codification.md) adds a temporal dimension: "codify when a pattern has emerged across enough runs that you can confidently commit." The [spec mining](./spec-mining-as-codification.md) workflow operationalizes this — watch the system, identify regularities, extract deterministic checks.

This lens treats codification as empirical. You don't decide *a priori* what to codify. You observe what the LLM does repeatedly the same way, and extract that. The agent always lowercases filenames and replaces spaces with underscores, so you extract `sanitize_filename()`. The pattern emerged; the codification followed.

The operational strategy is progressive [constraining](./definitions/constraining.md): start underspecified for flexibility, commit to precise semantics as patterns stabilize.

## Do the lenses reduce to one?

The four correlate but may not share a root:

- **Spec completeness** is about the nature of the problem
- **Oracle strength** is about how you check the output
- **Interpretation space** is about how many valid answers exist
- **Pattern stability** is about temporal evidence

A tempting reduction: spec completeness → single valid interpretation → cheap verification → stable pattern. If the spec fully captures the problem, there's one answer, you can verify cheaply, and the pattern is trivially stable. This makes spec completeness look foundational and the others downstream.

But the chain breaks at the edges. Some problems have cheap verification yet admit multiple valid outputs — sorting has a unique answer, but "good variable names" has several valid options even with a testable rubric. Some problems have stable patterns despite weak oracles — the LLM always formats dates the same way, extractable as code, even though "good formatting" is loosely specified.

There's also a directionality question. The oracle-strength lens treats verification cost as the driver: you codify *because* you can verify. The interpretation-space lens inverts this: you can verify *because* the spec admits only one output. "2+2=4" is verifiable because arithmetic has one answer, not because we built a test for it. Which is cause and which is consequence?

The KB doesn't yet have a settled answer. This is worth investigating rather than prematurely closing.

## Quick-reference checklist

The lenses above explain *why* these heuristics work. This section distills them into decision prompts.

**Codify when:**
- The spec fully captures the problem — there's one correct answer
- You can write a test that fully specifies correct behavior
- The LLM does the same thing every time — the pattern has stabilized
- The spec describes *what* (output properties) rather than *how* (process steps)
- The operation is being re-discovered by the LLM on every run at token cost

**Leave for LLM when:**
- The spec is a theory about the problem, not a definition of it
- Correctness requires human judgment or proxy scores
- The problem genuinely admits multiple valid interpretations
- The pattern hasn't stabilized — you're still learning what the right behavior is
- The constraint encodes *how* rather than *what* — process rather than outcome

**Reverse a codification ([relax](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md)) when:**
- Brittleness under paraphrase or reordering ([relaxing signals](./operational-signals-that-a-component-is-a-relaxing-candidate.md))
- Isolation-vs-integration gap — unit tests pass but integration fails
- Growing exception lists and special cases
- Distribution shift breaks the codified component
- Composition failure — individually sound components don't compose into the target capability (strongest signal, most expensive to discover)

## The hybrid case

Most real components are hybrids — part exact spec, part proxy theory. The practical move is to extract exact-spec subproblems into code and leave the rest for LLM.

The [deterministic validation note](./deterministic-validation-should-be-a-script.md) is a worked example: most checks in `/validate` are hard-oracle (frontmatter structure, enum matching, link resolution → script) while the remaining few are soft-oracle (description quality, composability → stays in LLM skill).

[AgeMem](./memory-management-policy-is-learnable-but-oracle-dependent.md), an RL-trained memory management agent, shows the same split. Its memory operations (Add, Delete, Retrieve) are exact-spec artifacts: their specs fully capture what they do. But the composition policy (when to use which) is a proxy theory that benefits from RL training.

## Three common mistakes

1. **Over-codifying.** Encoding "always decompose agents into three phases" as a hard rule when it's a theory about what works. Process constraints are [relaxing candidates](./operational-signals-that-a-component-is-a-relaxing-candidate.md) — they encode *how* rather than *what*.

2. **Under-codifying.** Running everything through an LLM, including checks where deterministic code would be faster, cheaper, and perfectly reliable. The validation example costs real tokens for zero gain on the hard-oracle checks.

3. **Static allocation.** Treating the code/LLM split as a one-time design decision rather than a [continuous cycle](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) of codification and relaxing as understanding evolves.

---

Relevant Notes:

- [fixed artifacts split into exact specs and proxy theories](./fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) — foundation: the exact-spec/proxy-theory distinction (lens 1)
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — foundation: verification cost as a gradient (lens 2)
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the interpretation-space framing (lens 3)
- [codification](./definitions/codification.md) — foundation: pattern stability and the phase transition to code (lens 4)
- [the boundary of automation is the boundary of verification](./the-boundary-of-automation-is-the-boundary-of-verification.md) — synthesis: the broader structural claim that verification cost determines automability — not linked in the body
- [constraining and distillation both trade generality for reliability, speed, and cost](./constraining-and-distillation-both-trade-generality-for-reliability.md) — grounds: the trade-off codification enacts — not addressed in the body
- [process structure and output structure are independent levers](./process-structure-and-output-structure-are-independent-levers.md) — sharpens: makes the "codify what, not how" heuristic precise — process constraints encode theories about good reasoning, output constraints encode verifiable properties
- [ephemeral computation prevents accumulation](./ephemeral-computation-prevents-accumulation.md) — grounds: names the structural cost of the "leave for LLM" side — no accumulation, no cross-run learning
- [Eric Evans: AI Components for a Deterministic System](https://www.domainlanguage.com/articles/ai-components-deterministic-system/) — exemplifies: Evans' modeling/classification split is a worked example where all four lenses yield different verdicts on two halves of the same system
