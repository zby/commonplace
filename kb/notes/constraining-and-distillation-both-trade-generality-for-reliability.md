---
description: Constraining narrows interpretation and distillation extracts focused artifacts; both can trade generality for reliability/speed/cost when task fit is good
type: kb/types/note.md
traits: []
status: current
tags: [learning-theory, constraining, distillation]
---

# Constraining and distillation both trade generality for reliability, speed, and cost

[Capacity decomposes into generality and a reliability/speed/cost compound](./learning-is-not-only-about-generality.md). [Constraining](./definitions/constraining.md) (narrowing the space of valid interpretations) and [distillation](./definitions/distillation.md) (extracting a focused artifact from larger material) both operate on this trade-off, but through different operations.

## The trade-off in action

An LLM can multiply numbers. A calculator can multiply numbers. Within a specified numeric representation and supported input range, the calculator has more reliable, cheaper, and usually faster capacity for multiplication: it will not hallucinate 7×8=54, and it can run without an API call. But the LLM has more generality — it can also translate, summarise, write prose.

This is the trade-off made concrete. Moving from the LLM to the calculator sacrifices generality for a gain in the reliability/speed/cost compound within that operation. These dimensions often improve together when the substrate changes from stochastic generation to deterministic code, but the gain depends on task fit and implementation limits.

## How constraining trades generality for reliability/speed/cost

[Constraining](./definitions/constraining.md) narrows the interpretation space. Each constraint reduces semantic latitude; when it fits the task, it can make the remaining operation more reliable, faster, cheaper, or easier to review.

[Codification](./definitions/codification.md) — the far end of the constraining spectrum — is the clearest high-yield case for the reliability/speed/cost compound. Replacing an LLM validation check with a Python script doesn't change *what* gets checked — it changes how reliably the check runs inside its specified contract, how fast it usually runs, and its marginal cost once written. What you give up is generality: the script handles exactly what it handles, nothing more.

But reliability/speed/cost gains are not exclusive to codification. Constraining short of codification (storing outputs, writing conventions) can also improve reliability and speed, just less dramatically. Across the constraining spectrum, successful constraints spend semantic latitude for narrower behavior — codification is just where the reliability/speed/cost gain can be largest because the medium itself changes.

## How distillation trades generality for reliability/speed/cost

[Distillation](./definitions/distillation.md) extracts from a larger body of reasoning into a focused artifact shaped by a specific use case, context budget, or agent. The extracted artifact is narrower than the source (less generality) but operationally more efficient: less material to load, less selection work, and fewer opportunities for the agent to choose the wrong source fragment.

A skill distilled from many methodology notes can fit in a single context window (speed, cost) and deliver a stable procedure (reliability). Extraction improves reliability by preselecting the relevant premises and ordering the steps; the agent no longer has to reconstruct the procedure from a larger note cluster each time. The methodology notes remain for edge cases — the distilled skill can't handle everything they cover. This is the same trade-off: generality for reliability/speed/cost gains, through extraction rather than constraint.

## The mechanisms differ in operation

| | Constraining | Distillation |
|---|---|---|
| **Operation** | Constrain — narrow the interpretation space | Extract — select and compress from a larger body |
| **What changes** | The same artifact becomes more constrained | A new, focused artifact is produced from a larger source |
| **Medium transition** | Ranges from none (conventions) to full (codification) | Typically none — stays in natural language |
| **Reliability/speed/cost yield** | Highest at codification (substrate change) | Moderate — speed and cost gains from reduced context |

Both directions are [capacity change](./learning-is-not-only-about-generality.md). The reverse — relaxing a constrained component, or loading the full source instead of the distillate — trades reliability/speed/cost gains back for generality.

---

Relevant Notes:

- [learning is not only about generality](./learning-is-not-only-about-generality.md) — grounds: defines the capacity decomposition this note applies
- [fixed artifacts split into exact specs and proxy theories](./fixed-artifacts-split-into-exact-specs-and-proxy-theories.md) — grounds: distinguishes cases where narrowing can harden confidently from cases where relaxing may be needed
