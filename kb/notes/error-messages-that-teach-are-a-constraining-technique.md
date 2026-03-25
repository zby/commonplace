---
description: In agent systems the error channel is an instruction channel — making errors teach the fix is nearly free and eliminates the agent's need to diagnose, an orthogonal axis to enforcement strength
type: note
traits: [has-external-sources]
tags: [learning-theory]
status: seedling
---

# Error messages that teach are a constraining technique

In agent systems, every error message the agent sees — linter output, test failures, hook warnings — is context that shapes its next action. A human seeing `null pointer exception` brings decades of debugging experience. An agent's only knowledge of what went wrong is what appears in context. The error channel is an instruction channel.

This means the difference between `FAIL` and `FAIL: description must be under 200 chars, yours is 247 — trim the last sentence` is not cosmetic. The first forces the agent to spend context diagnosing the problem. The second [frontloads](./frontloading-spares-execution-context.md) the answer. The cost difference is negligible — same hook, better message. The reliability difference is large.

Lopopolo's report on [OpenAI's Codex team](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) puts it directly: "Linter error messages double as remediation instructions — every failure message teaches the agent the fix." And: "every mistake is a harness bug" — when an agent makes an error the system could have prevented through a better message, the system is at fault.

## Orthogonal to enforcement strength

The [constraining gradient](./methodology-enforcement-is-constraining.md) moves from instructions through skills and hooks to scripts, trading flexibility for reliability. But there's a second axis: **how much the enforcement artifact teaches when it fires**. A blocking hook that says `FAIL` constrains maximally but informs minimally. A blocking hook that explains the fix constrains equally but informs maximally. Moving along this axis is cheap — it requires no change in trigger mechanism or enforcement strength, only better messages.

This is available at every layer. An instruction can say "check descriptions" or "descriptions must discriminate — if it paraphrases the title, rewrite it." A script can silently correct or log what it changed and why. The inform axis is orthogonal to the enforcement axis, and nearly free to improve.

---

Relevant Notes:

- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — extends: adds the inform axis orthogonal to the enforcement gradient
- [constraining](./definitions/constraining.md) — instance: teaching errors constrain interpretation by simultaneously blocking wrong outputs and demonstrating correct ones
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: teaching errors frontload the fix instead of leaving the agent to derive it
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — primary evidence: linter messages as remediation instructions in a 1M LOC agent-generated codebase
- [enforcement without structured recovery is incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — extends: teaching messages are the inform axis of recovery; structured recovery adds follow-through (corrective → fallback → escalation)
