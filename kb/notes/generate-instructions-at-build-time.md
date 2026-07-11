---
description: Template generation pays the flexibility cost once at setup; runtime variables pay it on every use across every substitution site, with occasional LLM misreads
type: kb/types/note.md
traits: []
tags: [architecture]
---

# Generate KB skills at build time, don't parameterise them

Since [indirection is costly in LLM instructions](../notes/indirection-is-costly-in-llm-instructions.md), skills and instructions should be generated from templates rather than parameterised with runtime variables.

Skills hardcode paths dozens of times — in grep commands, script invocations, save targets. Making a KB reusable across projects requires these paths to vary. There are two ways to get that variability:

**Runtime variables** — skills contain placeholders like `$KB_ROOT/notes/` and the LLM substitutes on every invocation. This adds interpretation overhead to every skill use, across every substitution site. Occasionally the LLM gets it wrong — wrong root, wrong slash direction, missing suffix — and the error surfaces only when a tool call fails.

**Build-time generation** — a template contains `{{kb_root}}/notes/`, a setup script resolves it to an absolute path at install time, and the generated skill is literal. The LLM reads and acts directly, with no substitution step.

Build-time generation is the right choice. It's [constraining applied to configuration](./methodology-enforcement-is-constraining.md) — the template is soft, the generated output is hard. You pay the flexibility cost once at setup time, not on every use. The canonical form for any skill is standalone (paths resolved to concrete values); the templating step is the mechanism for producing that canonical form, not a feature that should leak into the runtime artifact.

## Installation-specific inputs

Not all build-time inputs need to be committed to the repo. A second category exists: values that are static within one installation but vary between installations — sibling repo paths, local tool locations, environment-specific endpoints. These pass the same frontloading test ("can this be computed without the LLM's runtime state?") but can't be committed without breaking portability.

The mechanism is identical: templates contain placeholders, a setup or build step resolves them from a local (gitignored) config file, and the generated output is literal. The only difference is the input source. A placeholder like `{{sibling_repos.some_repo}}/kb/notes/` resolves from local config the same way a repo-committed `{{kb_root}}/notes/` resolves from repo config.

For recurring tasks this is especially clean. The task template is a stable runbook — "do not edit per run." Configuration separates the stable procedure ("for each sibling repo, check for changes since last review") from the variable environment ("here are the repos and their paths"), and the build step composes them.

**Injection scope.** Not every task needs every config value. The build step should resolve only what the task declares it needs — the [typed-callable](./instructions-are-typed-callables.md) pattern applied to configuration dependencies.

**Graceful absence.** When a config value is missing, the generated output should state what's unavailable rather than silently omitting it. "Sibling path not configured — skip" is better than the agent discovering the path doesn't exist mid-task.

---

Relevant Notes:

- [instruction-generation](../reference/instruction-generation.md) — current-state: how Commonplace instantiates this argument today through `commonplace-init`, scaffold trees, and the specific substitution points
- [indirection is costly in LLM instructions](../notes/indirection-is-costly-in-llm-instructions.md) — foundation: the general principle this applies; in code indirection is free, in LLM instructions it costs context and interpretation on every read
- [methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — template generation is a point on the constraining gradient
- [instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — motivates: always-loaded context should be slim; variable interpretation adds complexity
- [instructions are typed callables](./instructions-are-typed-callables.md) — enables: typed signatures on tasks/skills can declare configuration dependencies, letting the build step resolve only what's needed
- [scenario-decomposition-drives-architecture](./scenario-decomposition-drives-architecture.md) — motivates: the recurring "review related systems" scenario revealed the need for installation-specific paths
