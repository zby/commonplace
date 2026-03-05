---
description: The most effective stabilisation artifacts simultaneously constrain (block wrong output) and inform (teach the fix) — because in agent systems the error channel is an instruction channel; fills the gap between the stabilisation gradient's layers and the context they deliver
type: note
traits: [has-external-sources]
areas: [learning-theory, kb-design]
status: seedling
---

# Error messages that teach are a stabilisation technique

The [stabilisation gradient](./methodology-enforcement-is-stabilisation.md) describes how practices move from instructions through skills and hooks to scripts, trading flexibility for reliability. But the gradient treats enforcement and instruction as separate concerns: instructions inform, hooks and scripts constrain. The most effective stabilisation artifacts do both simultaneously — they block the wrong output *and* teach the agent the correct one in the same interaction.

Lopopolo's report on [OpenAI's Codex team](../sources/harness-engineering-leveraging-codex-agent-first-world.md) provides the clearest example: "Linter error messages double as remediation instructions — every failure message teaches the agent the fix." A linter that rejects a file and says `error: missing license header` constrains. A linter that says `error: missing license header — add "// SPDX-License-Identifier: MIT" as the first line` constrains *and* informs. The cost difference is negligible; the reliability difference is large, because the agent does not need to search for or infer the fix.

## Why this works in agent systems

In traditional systems, error messages are read by humans who bring external knowledge — a developer seeing `null pointer exception` knows how to debug it. The error message is a signal; the fix comes from the human's training and experience. In agent systems, the error message *is* the training for that interaction. The agent's only knowledge of what went wrong and how to fix it is what appears in its [context window](./context-efficiency-is-the-central-design-concern-in-agent-systems.md). A terse error forces the agent to spend context on diagnosis; a teaching error frontloads the answer.

This is why the error channel is an instruction channel: every verification output the agent sees — linter messages, test failures, hook warnings, CI output — functions as context that shapes its next action. The distinction between "enforcement" and "guidance" collapses. A blocking hook that exits non-zero with a helpful message is simultaneously at the deterministic end of the [stabilisation spectrum](./stabilisation.md) (it blocks the operation) and at the informative end (it teaches the fix).

## The dual-function property

The [methodology enforcement gradient](./methodology-enforcement-is-stabilisation.md) has five layers: instruction, skill, hook (warn), hook (block), script. Each layer is characterised by its trigger reliability and response determinism. But there is an orthogonal axis: **how much context the enforcement artifact delivers to the agent when it fires**. A hook that says `FAIL` constrains maximally but informs minimally. A hook that says `FAIL: description must be under 200 chars, yours is 247 — trim the last sentence` constrains equally but informs maximally.

This dual-function property — constrain + inform — is available at every layer of the gradient:

| Layer | Constrain-only | Constrain + inform |
|-------|---------------|-------------------|
| Instruction | "check descriptions" | "descriptions must discriminate this note from similar ones — if it paraphrases the title, rewrite it" |
| Skill | `/validate` reports pass/fail | `/validate` reports the violation and suggests a fix |
| Hook (warn) | `WARN: bad description` | `WARN: description paraphrases the title — a good description answers 'why THIS note?' not 'what is this about?'` |
| Hook (block) | `exit 1` | `exit 1` with stderr explaining the fix |
| Script | silently corrects | corrects and logs what it changed and why |

The insight is that **moving right on this axis is cheap stabilisation** — it requires no change in trigger mechanism or enforcement strength, only better error messages. Yet the reliability gain is substantial because it eliminates the agent's need to search for or infer the correct response.

## Connection to context efficiency

Teaching error messages are a form of [frontloading](./frontloading-spares-execution-context.md). Instead of giving the agent a procedure ("figure out what's wrong, find the relevant rule, determine the fix"), the error message gives the answer directly. This reduces the [complexity dimension of context cost](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — the agent receives the fix instead of instructions to derive the fix.

Lopopolo's phrase captures it: "every mistake is a harness bug." When an agent makes an error that the system could have prevented or corrected through a better message, the system is wasting context on a problem it already knows how to solve.

---

Relevant Notes:
- [methodology enforcement is stabilisation](./methodology-enforcement-is-stabilisation.md) — extends: adds the inform axis orthogonal to the trigger/response gradient; the gradient captures enforcement reliability but not the context quality of enforcement output
- [stabilisation](./stabilisation.md) — instance: teaching error messages are a stabilisation technique that constrains interpretation space by simultaneously blocking wrong outputs and demonstrating correct ones
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — mechanism: teaching errors are frontloading applied to the error channel — pre-computing the fix instead of leaving it for the agent to derive
- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — motivates: terse errors waste context on diagnosis; teaching errors respond to the complexity dimension by eliminating interpretation overhead
- [Harness Engineering (Lopopolo, 2026)](../sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) — primary evidence: linter messages as remediation instructions in a 1M LOC agent-generated codebase

Topics:
- [learning-theory](./learning-theory.md)
- [kb-design](./kb-design.md)
