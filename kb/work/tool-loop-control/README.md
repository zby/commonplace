# Workshop: Tool-loop Control

Rewrite workspace for the note currently captured in `kb/notes/tool-loop-index.md`.

The main framing change is deliberate: start from the normal application architecture where a framework-owned tool loop is a genuinely useful convenience layer, then argue that strong frameworks should keep that loop optional so application code can reclaim control when orchestration becomes part of the product logic.

## Source notes

- `kb/notes/tool-loop-index.md` — current note whose opening jumps too quickly to expressivity loss
- `kb/notes/bounded-context-orchestration-model.md` — the scheduler model underneath the argument
- `kb/notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md` — why hidden progression tends to move bookkeeping back into the conversational medium
- `kb/notes/session-history-should-not-be-the-default-next-context.md` — why framework-owned progression also tends to make history inheritance the default
- `kb/notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned-tool-loops.md` — one practical consequence once the framework owns progression and fallback policy

## Promoted notes

- `kb/notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent-frameworks.md` — capability-surface changes and recursive decomposition
- `kb/notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling-problems.md` — context-bound semantic subgoals that require partitioning and staged aggregation
- `kb/notes/codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md` — codified next-step policy as hidden scheduling
- `kb/notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md` — supporting concession note showing what the strongest stateful-tool recovery actually buys

## Workshop scaffolding

- `llm-frameworks-should-keep-the-tool-loop-optional.md` — broad framing draft for the eventual top-level replacement note
- `anatomy-of-an-llm-application.md` — tool-loop-first decomposition of the normal LLM application shape
- `a-framework-owned-tool-loop-can-simulate-explicit-orchestration-by-externalizing-control-state.md` — detailed constructive counterexample showing how stacks, branching, and recursive decomposition could be encoded inside a framework-owned loop

## Open decisions

- Whether the promoted note should keep the old title family (`...expose the loop`) or use the sharper formulation here (`...keep the tool loop optional`)
