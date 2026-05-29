# Workshop: Tool-loop Control

Rewrite workspace for the note currently captured in `kb/notes/tool-loop-index.md`.

The main framing change is deliberate: start from the normal application architecture where a framework-owned tool loop is a genuinely useful convenience layer, then argue that strong frameworks should keep that loop optional so application code can reclaim control when orchestration becomes part of the product logic.

## Source notes

- `kb/notes/tool-loop-index.md` — current note whose opening jumps too quickly to expressivity loss
- `kb/notes/bounded-context-orchestration-model.md` — the scheduler model underneath the argument
- `kb/notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md` — why hidden progression tends to move bookkeeping back into the conversational medium
- `kb/notes/session-history-should-not-be-the-default-next-context.md` — why framework-owned progression also tends to make history inheritance the default
- `kb/notes/apparent-success-is-an-unreliable-health-signal-in-framework-owned.md` — one practical consequence once the framework owns progression and fallback policy

## Promoted notes

- `kb/notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent.md` — capability-surface changes and recursive decomposition
- `kb/notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md` — context-bound semantic subgoals that require partitioning and staged aggregation
- `kb/notes/codified-scheduling-patterns-can-turn-tools-into-hidden-schedulers.md` — codified next-step policy as hidden scheduling
- `kb/notes/stateful-tools-recover-control-by-becoming-hidden-schedulers.md` — supporting concession note showing what the strongest stateful-tool recovery actually buys

## Workshop scaffolding

- `llm-frameworks-should-keep-the-tool-loop-optional.md` — broad framing draft for the eventual top-level replacement note
- `the-practical-scheduler-is-the-host-language.md` — the bridge note: the simplest practical library demotes the tool loop to a returning, per-call-parameterized function and lets host-language code play `select`/`K`; minimal surface is one primitive plus one hook
- `orchestration-strategies-and-run-state-have-opposite-persistence.md` — follow-on: `K` (run-state) stays ephemeral, but recurring `select`-strategies are the high-value promotion target; reframes "RLM + a tested orchestrator library" as a test-gated cache that makes the host-language scheduler self-populating

## Retired scaffolding (distilled, deleted 2026-05-29)

Two early drafts were spent — every durable claim now lives in a published note or in the framing draft above, with no library links depending on them, so they were deleted (recoverable via git):

- `anatomy-of-an-llm-application.md` — tool-loop-first decomposition. Distilled into: `llm-frameworks-should-keep-the-tool-loop-optional.md` (convenience case + programmer's dilemma), the promoted `subtasks-that-need-different-tools...` (capability-surface boundary, now more complete), and the promoted `codified-scheduling-patterns...` (temporal codification).
- `a-framework-owned-tool-loop-can-simulate-explicit-orchestration-by.md` — constructive counterexample (singleton-runtime recovery). Distilled into the promoted `stateful-tools-recover-control-by-becoming-hidden-schedulers.md` (the concession claim) and the promoted `subtasks-that-need-different-tools...` (where the construction strains). The remaining `ControlRuntime` code was illustrative scratch, not preserved.

## New inputs (2026-05-29 session)

Folded into `llm-frameworks-should-keep-the-tool-loop-optional.md` ahead of promotion:

- **Frozen-`select` framing** — the framework-owned tool loop is the [bounded-context](../../notes/bounded-context-orchestration-model.md) `select` hardcoded to "append result, re-ask with same tools." "Keep the loop optional" = let the application own `select`. This is the one substantive new *idea* (vs. grounding), grounded in the bounded-context model note.
- **Lifecycle hooks convergence** — the [agent-harness survey](../../sources/agent-harness-large-language-model-agents-survey.md) independently makes lifecycle hooks first-class, corroborating the proposed middle layer.
- **iii production evidence** — [iii](../../sources/how-to-build-your-own-agent-harness-2060069083878408689.md) ships the loop as one swappable layer on a bus; "slider not a fork" reframes the programmer's dilemma. (Cite the replaceability/layering half only — independent versioning is a deployment property, not a tool-loop property.)

Decision (2026-05-29): develop this workshop independently of, and ahead of, the `harness-fundamentals` brainstorm. The drafts no longer link out to `harness-boundary.md`; the frozen-`select` argument stands on its own, grounded in the bounded-context model note and the agent-harness survey / iii sources. The wider "what is the harness" candidate set — including Candidate D (harness = `select`), the general case of this workshop's frozen-`select` argument — stays in `kb/work/harness-fundamentals/` and is not a dependency here. Any argument once carried by the cross-workshop link is inlined in the drafts and cited to its underlying source.

## Open decisions

- Whether the promoted note should keep the old title family (`...expose the loop`) or use the sharper formulation here (`...keep the tool loop optional`)
