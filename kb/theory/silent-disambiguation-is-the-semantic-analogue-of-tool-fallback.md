---
description: When an agent silently resolves unacknowledged material ambiguity in a spec, final success hides that the contract failed to determine the path — an extension of the tool-fallback observability problem
type: types/note.md
traits: [has-external-sources, title-as-claim]
tags: [learning-theory, computational-model, observability, llm-reliability]
---

# Silent disambiguation is the semantic analogue of tool fallback

When a tool call fails and the agent silently works around it, [final task success does not establish intended-path health](./final-task-success-does-not-establish-intended-path-health.md) unless an independent execution signal preserves the deviation. The same thing happens one layer up: when a spec leaves an implementation-significant branch unresolved and the agent silently picks one reading, success hides that the contract didn't determine the path. The gap is semantic instead of operational, but the observability failure is identical — the run crossed into recovery and nothing reported it.

This is not [interpreter failure](./out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) (spec was clear, model violated it), and it excludes specs that explicitly delegate discretion. It is the agent repairing a contract gap the spec didn't acknowledge — which means task completion alone cannot distinguish "the spec was sufficient" from "the agent improvised well enough."

An unrequested guard is a common instance. Sean Goedecke reports, in [What requirements don't you have?](../sources/sean-goedecke-what-requirements-dont-you-have.ingest.md), agents adding a mutex or a mid-flight re-check the task never asked for. Whether to guard was a branch the spec left open; the agent resolved it toward guarding, and a passing diff hides that the resolution was the agent's rather than the spec's.

---

Relevant Notes:

- [What requirements don't you have?](../sources/sean-goedecke-what-requirements-dont-you-have.ingest.md) — evidenced-by: illustrates silent resolution of an open branch toward an unrequested guard; practitioner observation, not a test of the claim
- [Final task success does not establish intended-path health](./final-task-success-does-not-establish-intended-path-health.md) — extends: this note carries the same non-identifiability argument one layer up, from tool failure to unacknowledged semantic underdetermination
- [agentic systems interpret underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md) — foundation: ambiguity exists because natural-language specs admit multiple valid interpretations
- [changing requirements conflate genuine change with disambiguation failure](./changing-requirements-conflate-genuine-change-with-disambiguation.md) — sharpens: the first silent choice is already a degraded run state, not only a future maintenance problem
- [out-of-spec output is a failure of the interpreter, not the spec](./out-of-spec-output-is-a-failure-of-the-interpreter-not-the-spec.md) — distinguishes: this note is about insufficient specification, not violating a sufficient one
- [enforcement without structured recovery is incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — applies: ambiguity handling also needs typed recovery and escalation
- [observability](../tags/observability-README.md) — belongs to: semantic recovery must be visible to learn whether contracts are sufficient
- [What Spec-Driven Development Gets Wrong](https://x.com/augmentcode/status/2025993446633492725) — exemplifies: bidirectional spec updates make semantic recovery visible
