---
description: When an agent silently resolves unacknowledged material ambiguity in a spec, final success hides that the contract failed to determine the path — an extension of the tool-fallback observability problem
type: note
traits: [has-external-sources]
tags: [learning-theory, computational-model, observability, llm-interpretation-errors]
status: seedling
---

# Silent disambiguation is the semantic analogue of tool fallback

This note extends [apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) from tool failure to specification failure. When a tool call fails and the agent finds another way, the run succeeds but hides that the intended path broke. The same thing happens with specs when there is **unacknowledged material ambiguity**: the spec leaves an implementation-significant branch unresolved, the agent silently picks one reading, and the run succeeds while hiding that the contract didn't determine the path.

The pattern in both cases: a prescribed path exists, the runtime hits a point where it can't follow it as written, the agent fills the gap with local judgment, and the user gets a useful artifact anyway. With tools the gap is concrete (missing binary, bad path). With specs the gap is semantic (the task needs one branch but the contract doesn't determine which). Either way the run has crossed from primary-path execution into recovery — and nothing reports it.

This excludes specs that explicitly delegate discretion. If the artifact says the choice is open-ended, heuristic, or left to agent judgment, then choosing within that space is still primary-path execution. The degraded case is not "the agent made a choice." It is "the agent had to repair missing contract that the spec did not acknowledge as discretionary."

This is not [interpreter failure](./interpretation-errors-are-failures-of-the-interpreter.md) (the spec was clear and the model violated it). It is the spec leaving room the agent quietly filled. And it is not just restating that [agents interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — underspecification is the background condition; the claim here is that silently resolving it is a recovery event that should be visible, not a neutral implementation detail.

The implication for spec-driven development is that task completion is not evidence that the spec was sufficient. A capable agent compensates for unacknowledged material ambiguity just as it compensates for a broken script. Without reporting — surface assumptions, record directional choices, escalate when guarantees change — "implemented successfully" collapses "the spec was sufficient" and "the agent improvised well enough."

---

Relevant Notes:

- [apparent success is an unreliable health signal in framework-owned tool loops](./apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md) — extended from: this note carries the same observability argument one layer up, from tool failure to unacknowledged semantic underdetermination
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: ambiguity exists because natural-language specs admit multiple valid interpretations
- [changing requirements conflate genuine change with disambiguation failure](./changing-requirements-conflate-genuine-change-with-disambiguation-failure.md) — sharpens: the first silent choice is already a degraded run state, not only a future maintenance problem
- [interpretation errors are failures of the interpreter](./interpretation-errors-are-failures-of-the-interpreter.md) — distinguishes: this note is about insufficient specification, not violating a sufficient one
- [enforcement without structured recovery is incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — applies: ambiguity handling also needs typed recovery and escalation
- [observability](./observability-index.md) — belongs to: semantic recovery must be visible to learn whether contracts are sufficient
- [What Spec-Driven Development Gets Wrong](../sources/what-spec-driven-development-gets-wrong-2025993446633492725.ingest.md) — exemplifies: bidirectional spec updates make semantic recovery visible
