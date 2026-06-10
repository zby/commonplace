---
description: ""
type: scenario
frequency: common | occasional | rare
---

# {Scenario name}

{What the user wants and what the agent must do — then how the operation forks into clean contexts.}

## Forks

Every `cp-skill-*` runs `context: fork`, so an operation is a chain of clean-context agents, each paying its loads from scratch. List the forks in execution order (the orchestrating main agent is Fork 1; each skill invocation is a further fork). For each load, classify it:

- **overhead** — read only because the work is inside this framework (AGENTS.md, the collection's COLLECTION.md, a type-spec, a skill body, a curated index / scoped `rg` listing, a validate run). Give a real path so the harness can measure its bytes.
- **content** — task or source material the agent would read regardless of any framework. Usually "variable"; put a byte estimate in Notes.
- **spared** — content this fork does *not* load because the framework gave it a cheaper surface (a description line instead of a note body, a frontloaded answer, a distilled artifact). Record as a credit, not a load.

### Fork N — {name} (orchestrator | cp-skill-X)
| load | kind | source | hops |
|---|---|---|---|
| {what the fork reads} | overhead | `path/to/file` | 1 |
| {task material} | content | variable | 2-4 |
| {avoided bodies} | spared | — | — |

Notes: {what the table can't carry — why a hop count is a range, what an estimate assumes, whether AGENTS.md is re-injected into this fork.}

## Variants

{Environment or workflow differences that change the fork set or the loads — installed project vs Commonplace repo, directory-local types, escalation to methodology, optional steps skipped.}
