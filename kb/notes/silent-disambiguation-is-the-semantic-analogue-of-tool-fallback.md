---
description: When an agent silently resolves unacknowledged material ambiguity in a spec, final success hides that the contract failed to determine the path — an extension of the tool-fallback observability problem
type: note
traits: [has-external-sources]
tags: [learning-theory, computational-model, observability, llm-interpretation-errors]
status: seedling
---

# Silent disambiguation is the semantic analogue of tool fallback

When a tool call fails and the agent silently works around it, [apparent success hides that the intended path broke](./apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md). The same thing happens one layer up: when a spec leaves an implementation-significant branch unresolved and the agent silently picks one reading, success hides that the contract didn't determine the path. The gap is semantic instead of operational, but the observability failure is identical — the run crossed into recovery and nothing reported it.

This is not [interpreter failure](./interpretation-errors-are-failures-of-the-interpreter.md) (spec was clear, model violated it), and it excludes specs that explicitly delegate discretion. It is the agent repairing a contract gap the spec didn't acknowledge — which means task completion alone cannot distinguish "the spec was sufficient" from "the agent improvised well enough."

---

Relevant Notes:

- [apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) — extended from: this note carries the same observability argument one layer up, from tool failure to unacknowledged semantic underdetermination
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: ambiguity exists because natural-language specs admit multiple valid interpretations
- [changing requirements conflate genuine change with disambiguation failure](./changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) — sharpens: the first silent choice is already a degraded run state, not only a future maintenance problem
- [interpretation errors are failures of the interpreter](./interpretation-errors-are-failures-of-the-interpreter.md) — distinguishes: this note is about insufficient specification, not violating a sufficient one
- [enforcement without structured recovery is incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — applies: ambiguity handling also needs typed recovery and escalation
- [observability](./observability-index.md) — belongs to: semantic recovery must be visible to learn whether contracts are sufficient
- [What Spec-Driven Development Gets Wrong](../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) — exemplifies: bidirectional spec updates make semantic recovery visible
