---
description: In code, indirection (variables, config, abstraction layers) is nearly free at runtime — in LLM instructions, every layer of indirection costs context and interpretation overhead on every read
type: note
traits: []
areas: [claw-design]
status: seedling
---

# Indirection is costly in LLM instructions

In traditional programming, a variable lookup or config reference costs essentially nothing at runtime. The CPU reads from memory either way — `project_claw/notes/` and `CONFIG["root"] + "/notes/"` are equally cheap. Indirection is so free that we use it everywhere: environment variables, config files, dependency injection, abstraction layers. The cost of adding a level of indirection is architectural complexity, not runtime performance.

In LLM instructions, the cost model is fundamentally different. Every token competes for context. A variable like `{{claw_root}}` doesn't just occupy the tokens for its name — it requires the LLM to maintain the mapping in working memory, recognise substitution sites, perform the replacement mentally, and act on the result. That's interpretive overhead on every read. And unlike a CPU, the LLM occasionally gets it wrong: forgetting to substitute, mangling a path, or applying the wrong value.

This means indirection patterns that are free in code become expensive in prompts:
- **Config variables** in instructions add per-read interpretation cost
- **Abstraction layers** ("use the appropriate search command" vs "run `grep -r term project_claw/notes/`") force the LLM to resolve the abstraction before acting
- **Conditional paths** ("if X, do A; if Y, do B" where X is always true) waste context on dead branches

The fix is the same as in compiled languages: **resolve at build time what you can**. If a value is known when the instructions are authored (or can be determined at setup time), bake it in. Generate concrete instructions from templates. The flexibility cost is paid once; the resulting instructions are literal and direct.

## Where the boundary is

Not all indirection should be eliminated. The principle applies when:
- The value is **known at setup time** and stable during operation (paths, project names, tool versions)
- The instruction is **read frequently** (always-loaded context, commonly invoked skills)
- The LLM must **act on the value** in commands or paths, not just understand it conceptually

Runtime parameters remain parameters — the current file being processed, a URL being ingested, a user's query. These genuinely vary and must stay variable.

The test: if you could do a find-and-replace before the LLM ever sees the text, and the result would always be the same, then do the find-and-replace. That's build-time resolution.

## Example: claw skill portability

This principle surfaced during claw extraction planning. Skills in `project_claw/skills/` hardcode `project_claw/` paths dozens of times — in grep commands, script invocations, save targets. Making the claw reusable requires either runtime variables (`$CLAW_ROOT/notes/`) or build-time generation (template → concrete skill). Runtime variables would add interpretation overhead to every skill invocation. [Generating instructions at build time](../claw-design/generate-instructions-at-build-time.md) is the [stabilisation](../claw-design/methodology-enforcement-is-stabilisation.md) move: resolve the variable once, load the literal result every time.

---

Relevant Notes:
- [programming practices apply to prompting](./programming-practices-apply-to-prompting.md) — context: indirection cost is another case where a programming practice (abstraction via variables) transfers to prompting but with a different cost model
- [methodology enforcement is stabilisation](../claw-design/methodology-enforcement-is-stabilisation.md) — foundation: build-time generation is a point on the stabilisation gradient — moving from stochastic interpretation to deterministic resolution
- [CLAUDE.md is a router, not a manual](../claw-design/context-loading-strategy.md) — motivates: always-loaded context is expensive; indirection mechanics make it more so

Topics:
- [claw-design](./claw-design.md)
