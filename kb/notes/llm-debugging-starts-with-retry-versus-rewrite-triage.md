---
description: "Uses execution-versus-interpretation failure to choose the first debugging move: retry a bad execution of a sound reading, or rewrite a specification that reliably induces the wrong reading"
type: kb/types/note.md
traits: [title-as-claim]
tags: [learning-theory, computational-model, llm-reliability]
---

# LLM debugging starts with retry-versus-rewrite triage

LLM components exhibit two distinct phenomena — semantic underspecification of the spec, and execution indeterminism during sampling. See [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) for the framing this note depends on. When a prompt "fails," the first diagnostic question follows directly: which phenomenon is responsible?

- **Indeterminism failure** — the LLM produced a bad execution of a good interpretation. The spec was fine; the sample was unlucky. Retries may not reproduce the failure, and the fix is operational: retry, lower temperature, or accept the sampling variance.
- **Underspecification failure** — the LLM is consistently choosing an interpretation you didn't intend. The spec admits it, so the failure will recur on every run that lands on the same interpretation. The fix is semantic: rewrite the spec to exclude the bad interpretation, or narrow the interpretation space with examples, schemas, or constraints.

The two have different remedies because they have different causes, and the remedies do not substitute. Treating an underspecification failure as noise — more retries, more temperature tuning — wastes effort: the spec still admits the bad interpretation, so the LLM will land on it again. Treating an indeterminism failure as a spec problem — rewriting when the original was fine — overcommits: the new spec narrows interpretations that never caused trouble, and may exclude good ones.

The triage test: run the same input several times. If the failure is intermittent, suspect indeterminism. If it reproduces, suspect underspecification — the spec is consistently picking out behavior you didn't intend, and retrying won't change that.

Edge case: the two can blend. Lowering temperature concentrates the sampling distribution, which can *change which interpretation you see* — not just how noisily you see it. A failure that appeared intermittent at high temperature may become consistent at low temperature, or vice versa. That's a signal the interpretation space matters, not just the sampling — so the fix lives in the spec, not the engine.

The triage is usually best performed at the nearest [LLM↔code boundary](./llm-code-boundaries-are-natural-checkpoints.md): inspect what arrived at the code side, and ask whether a different-but-valid interpretation would have produced the same argument. If yes, the failure is upstream in the projection; if no, it's downstream in the code.

---

Relevant Notes:

- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: the two-phenomena model that motivates the triage
- [llm-code-boundaries-are-natural-checkpoints](./llm-code-boundaries-are-natural-checkpoints.md) — related: checkpoints are where you bisect to decide which side of the crossing the failure came from
- [out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec](./out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — bounded by: real LLMs also add interpreter failures beyond the two phenomena, which this triage does not cover
