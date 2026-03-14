---
description: Values static within an installation but variable across installations — sibling repo paths, local tool locations — are frontloadable through configuration the orchestrator resolves and injects into sub-agent frames; the context savings depend on sub-agent isolation since injection into the main context just adds tokens
type: note
traits: []
tags: []
status: seedling
---

# Injectable configuration extends frontloading to installation-specific values

[Frontloading](./frontloading-spares-execution-context.md) says: pre-compute static parts of instructions and insert results. It lists "variable resolution — paths, project names, configuration values known at setup time" as a frontloadable category. But the current frontloading channels — [build-time generation](./generate-instructions-at-build-time.md) and hardcoded values in CLAUDE.md — only handle values that are the same across all installations. A third category exists: values that are static within one installation but vary between installations.

Crucially, injectable configuration only spares execution context when the orchestrator dispatches tasks to [sub-agents](./llm-context-is-composed-without-scoping.md). The orchestrator constructs a fresh frame containing the task runbook plus resolved config values — and nothing else from the parent context. If the task runs in the main context instead, the injected values just add tokens to the same flat window. The context savings come from frame isolation, not from the injection itself.

## The category

Examples:
- **Sibling repo paths.** Related systems (arscontexta, thalo, clawvault) checked out in adjacent directories. The paths are stable locally but don't exist for other users.
- **Local tool paths.** Custom scripts, language runtimes, or CLI tools installed in non-standard locations.
- **Environment-specific endpoints.** Local services, staging URLs, API keys that differ per machine.

These values share two properties:
1. **Static at runtime** — they don't change during a session or between runs. They pass the frontloading test: "can this be computed without the LLM's runtime state?"
2. **Variable at install time** — they can't be committed to the repo without breaking portability.

The combination means they need a configuration file that is local (gitignored), read by the orchestrator, and injected into sub-agent context before the agent sees the task.

## The mechanism

The orchestrator reads configuration at session start. When it dispatches a recurring task to a sub-agent, it constructs the sub-agent's frame by combining the task runbook with the resolved config values. This is the same partial evaluation the frontloading note describes — the orchestrator is the specialiser, configuration values are the static inputs, and the residual is a task with concrete paths instead of placeholders.

For [recurring tasks](../tasks/types/task-recurring.md) this is especially clean. The recurring task template is a stable runbook — "do not edit per run." Configuration separates the stable procedure ("for each sibling repo, check for changes since last review") from the variable environment ("here are the repos and their paths"). The orchestrator composes them when constructing the sub-agent frame.

## Relationship to auto-injection

[Auto-injection](./agent-statelessness-means-harness-should-inject-context-automatically.md) proposes that the harness inject KB content (definitions, ADRs) based on document references. Injectable configuration is a parallel but distinct channel:

| | Auto-injection | Injectable configuration |
|---|---|---|
| **Source** | KB content (notes, definitions) | Local environment (paths, endpoints) |
| **Trigger** | Document reference encountered during reading | Task/skill loaded by orchestrator |
| **Varies by** | What the agent is reading | What machine it's running on |
| **Lifetime** | Session (definition valid for duration) | Installation (path valid until repo moves) |

Both are instances of the harness resolving information the agent can't or shouldn't resolve itself. Both spare execution context — but only when the harness constructs isolated frames rather than appending to the main context.

## Design considerations

**Implementation spectrum.** The principle is "resolve installation-specific values before they reach the agent." How that resolution happens is an implementation choice:

- **Instructions.** The orchestrator reads a config file and includes resolved values as natural language in the sub-agent's prompt: "The arscontexta repo is at ../arscontexta." Simplest to build, no tooling beyond what exists.
- **Code templates.** A build step expands `{{sibling_repos.arscontexta}}` in task templates before the orchestrator sees them. This is the [build-time generation](./generate-instructions-at-build-time.md) pattern applied to local config — produces committed-looking artifacts from gitignored inputs.
- **Runtime resolution.** The orchestrator passes config as structured data that the sub-agent's tools can reference programmatically.

These aren't mutually exclusive. The instruction path works today; templates and runtime resolution become worthwhile as the number of config-dependent tasks grows.

**Injection scope.** Not every task needs every config value. The orchestrator should inject only what the task declares it needs — the [typed-callable](./instructions-are-typed-callables.md) pattern applied to configuration dependencies. A recurring review task declares it needs `sibling_repos`; the orchestrator provides them in the sub-agent frame.

**Graceful absence.** When a config value is missing, the orchestrator should tell the sub-agent what's unavailable rather than silently omitting it. "arscontexta path not configured — skip" is better than the agent discovering the path doesn't exist mid-task.

**Not a general settings system.** This is specifically for values consumed by specific tasks in sub-agent frames. User preferences that affect agent behaviour globally (like "never auto-commit") belong in CLAUDE.md or `.claude/settings.json` where they're already handled.

---

Relevant Notes:

- [frontloading spares execution context](./frontloading-spares-execution-context.md) — foundation: injectable configuration is a specific frontloading channel for installation-variable values
- [LLM context is composed without scoping](./llm-context-is-composed-without-scoping.md) — mechanism: the context savings depend on sub-agent frame isolation; without it, injected config just adds to the flat window
- [agent statelessness means harness should inject context automatically](./agent-statelessness-means-harness-should-inject-context-automatically.md) — parallel: auto-injection resolves KB references, injectable configuration resolves environment values; both spare execution context through harness-side resolution
- [instructions are typed callables](./instructions-are-typed-callables.md) — enables: typed signatures on tasks/skills can declare configuration dependencies, letting the orchestrator inject only what's needed
- [generate instructions at build time](./generate-instructions-at-build-time.md) — contrast: build-time generation handles values stable across all installations; injectable configuration handles values stable within one installation
- [scenario-decomposition-drives-architecture](./scenario-decomposition-drives-architecture.md) — motivates: the recurring "review related systems" scenario revealed the need for installation-specific paths
