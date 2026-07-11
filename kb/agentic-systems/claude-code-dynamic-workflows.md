---
description: "How Claude Code's dynamic-workflows API works — a model-authored JS orchestrator over sub-agents — mapped onto the bounded-context orchestration model: what of the tool loop the harness exposes, to whom, and what it withholds"
type: kb/types/note.md
traits: [has-external-sources]
tags: [computational-model, tool-loop]
---

# Claude Code dynamic workflows

**Evidence basis:** the official docs ([snapshot](../sources/claude-code-dynamic-workflows-docs.md), captured 2026-06-03) plus the Workflow tool contract observed first-hand from inside a running Claude Code session (2026-06-12) — the in-harness contract carries API details the docs omit.

## What it is

A dynamic workflow is a JavaScript script that orchestrates sub-agents. The model writes the script for a task the user describes; a background runtime executes it in isolation from the conversation; intermediate results live in script variables and only the final return value lands in the parent's context. Opt-in is conversational — the `ultracode` keyword, a natural-language request, or session-wide ultracode mode — and a finished run's script can be saved as a reusable `/<name>` command.

## The API surface

The script body gets a small primitive set:

- `agent(prompt, opts) -> Promise` — spawn a sub-agent and **return** its result to the caller. Per-call options: `schema` (forces a validated structured-output call — the result is a parsed object, not text), `model`, `agentType` (a registered sub-agent type such as `Explore` or a custom reviewer), `isolation: 'worktree'` (fresh git worktree for parallel mutation), plus display `label`/`phase`.
- `pipeline(items, ...stages)` / `parallel(thunks)` — composition combinators. `pipeline` runs each item through all stages with no barrier between stages; `parallel` is an explicit barrier. The contract pushes pipeline-by-default and treats barriers as a justified exception.
- `workflow(nameOrRef, args)` — invoke a saved or file-based workflow inline; exactly one nesting level.
- `args` — invocation input passed as structured data, so saved workflows are parameterizable without editing the script.
- `budget` — a shared token pool (`total`, `spent()`, `remaining()`) across the main loop and all workflows; a hard ceiling, enforced by making `agent()` throw once exhausted.
- `log()` / `phase()` — progress narration to the user.

Constraints the runtime imposes:

- **Plain sandboxed JS** — no filesystem, shell, or Node APIs. The docs state the division: "Agents read, write, and run commands. The script coordinates the agents."
- **Determinism for resume** — `Date.now()`, `Math.random()`, and argless `new Date()` throw. Each `agent()` result is journaled keyed by its call prefix; resume replays the unchanged prefix from cache and runs only edited or new calls live. The journal is session-local: exiting Claude Code discards it.
- **Caps** — min(16, cores−2) concurrent agents, 1,000 agents per run, one `workflow()` nesting level.
- **No mid-run user input** — only permission prompts can pause a run; staged sign-off means one workflow per stage. Sub-agents always run in `acceptEdits` mode and inherit the session allowlist regardless of the session's permission mode.

## Mapping onto the orchestration model

| [Bounded-context orchestration model](../notes/bounded-context-orchestration-model.md) | Workflows implementation |
|---|---|
| Bounded call | `agent(prompt, opts)` — returning, per-call-parameterized |
| `select` | Ordinary JS control flow plus `pipeline`/`parallel` |
| `K` | Script variables; reified as the resume journal within a session |
| `select` authorship | The model, per run (RLM-style); whole script promotable to a `/command` |
| Stop condition | Model-finished, or `schema`-validated structured output |

The fit with [the practical scheduler is the host language](../notes/the-practical-scheduler-is-the-host-language.md) is close to literal: a returning primitive, host-language control flow playing `select`, live variables holding `K` — and `K` reified (the journal) exactly when within-run durability demands it, the boundary that note draws. The persistence split matches [orchestration strategies and run-state have opposite persistence economics](../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md): `K` dies with the session while the `select`-strategy (the script) is the promotion target. The authorship model is [RLM's](../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — the model writes the orchestrator rather than being it — with the persistence RLM lacks added on top.

## What the runtime withholds

Four restrictions, each a framework-retained decision rather than an incidental limit:

1. **Guest language, not host language.** With no filesystem or shell access, the symbolic scheduler cannot read its own working set. Partitioning a corpus — the canonical case in [semantic sub-goals that exceed one context window](../notes/semantic-sub-goals-that-exceed-one-context-window-become-scheduling.md) — requires either spending an agent on enumeration or having the parent conversation scout the work-list first and pass it via `args` (the tool contract recommends this "hybrid" explicitly). Deterministic transforms (dedupe, rank, filter) operate only on what agents return, never on the corpus directly.
2. **Capability surface by registry, not per call.** `agent()` takes an `agentType`, not a `tools` argument: the next call's action alphabet is *selected* from registered sub-agent types, not *constructed*. The central forcing case of [subtasks that need different tools](../notes/subtasks-that-need-different-tools-force-loop-exposure-in-agent.md) is met through registry indirection, and the permission posture (`acceptEdits`, inherited allowlist) is fixed.
3. **No dispatch hook, no stop predicate.** The script surface has no tool-execution interposition point (harness-level hooks exist in settings, outside the script), and `agent()` accepts no caller-supplied stop predicate — no step cap or per-agent budget; `budget` is run-granular only.
4. **Frozen loop at the seams.** The parent conversation loop stays frozen and is the only glue between workflows: no mid-run input, so multi-stage work with sign-off runs one workflow per stage with inter-workflow `select` happening in the conversational medium — the regime [LLM-mediated schedulers](../notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) describes, relocated one level up.

## Promotion path

Save-as-command promotes the **whole script, manually, with no test gate** — fit and trust collapse into one human decision. Notably, the vendor's own strategy corpus — adversarial verify, judge panels, loop-until-dry, multi-modal sweep, completeness critic — ships as prescriptive prose inside the Workflow tool prompt, re-instantiated by the model in each script, not as importable tested fragments. The strategy library the persistence-economics note calls for exists here as instructions, not code.

## Reading against the tool-loop cluster

Dynamic workflows are the first shipped harness instance of [keeping the tool loop optional](../notes/llm-frameworks-should-keep-the-tool-loop-optional.md): the bounded call exposed beneath the frozen loop, composable in a host-ish language. The qualifications — exposure to the model rather than the application programmer, a deliberately weakened substrate, registry-mediated capability surfaces, whole-script promotion granularity — are what keep the cluster's question ("who decides what the next step *can do*?") open; the argumentative consequences live in the theory notes, not here.

---

Relevant Notes:

- [Claude Code dynamic workflows docs](../sources/claude-code-dynamic-workflows-docs.md) — derived-from: the official docs snapshot this analysis is grounded in
- [A harness for every task — dynamic workflows](../sources/a-harness-for-every-task-dynamic-workflows.md) — see-also: practitioner walkthrough of the same feature
- [the practical scheduler is the host language](../notes/the-practical-scheduler-is-the-host-language.md) — rationale: the minimal surface (returning primitive, host-language `select`/`K`, reify-`K`-when-forced) this API approximates and deviates from
- [LLM frameworks should keep the tool loop optional](../notes/llm-frameworks-should-keep-the-tool-loop-optional.md) — rationale: the design stance this feature partially ships; the analysis feeds back as evidence there
- [any symbolic program with LLM calls is a select/call program](../notes/any-symbolic-program-with-llm-calls-is-a-select-call-program.md) — see-also: the lemma the mapping table instantiates — JS control flow playing `select`, script variables holding `K`
- [agent orchestration occupies a multi-dimensional design space](../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — see-also: the four withholdings read as independent design axes; this note names that independence
- [RLM has the model write ephemeral orchestrators over sub-agents](../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — see-also: the same authorship model with persistence added
- [orchestration strategies and run-state have opposite persistence economics](../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) — see-also: the journal/save split instantiates the predicted asymmetric lifecycle; the promotion machinery remains coarse and manual
- [tool loop](../notes/tool-loop-README.md) — see-also: the cluster this system is read against
