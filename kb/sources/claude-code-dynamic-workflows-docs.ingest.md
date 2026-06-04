---
description: "Claude Code dynamic-workflows docs — the saveable, script-authored counterpoint to RLM's ephemeral orchestrators; evidence for the orchestration/run-state persistence cluster"
source_snapshot: "claude-code-dynamic-workflows-docs.md"
ingested: "2026-06-03"
type: kb/sources/types/ingest-report.md
source_type: tool-announcement
domains: [orchestration, sub-agents, persistence, context-engineering]
---

# Ingest: Orchestrate subagents at scale with dynamic workflows

Source: claude-code-dynamic-workflows-docs.md
Captured: 2026-06-03
From: https://code.claude.com/docs/en/workflows

## Classification

Type: tool-announcement -- official Anthropic product documentation for a research-preview Claude Code feature ("dynamic workflows"). It announces and specifies a shipping capability, not a study or argument; treat its design framings as vendor-authored.
Domains: orchestration, sub-agents, persistence, context-engineering
Author: Anthropic (first-party docs for Claude Code). High authority on the feature's mechanics and constraints; no independent evaluation of whether the design works better than alternatives.

## Summary

Dynamic workflows are a JavaScript script that Claude writes to orchestrate up to 1,000 subagents per run (16 concurrent), executed by a background runtime in an isolated environment so the session stays responsive. The defining move is that the plan lives "in code": the script holds the loop, branching, and intermediate results in script variables, so Claude's context window receives only the final answer rather than every agent's output. A run can be saved as a reusable `/<name>` command (project or user scope), accept `args` as structured input, and be resumed within a session via cached agent results. The docs position workflows against subagents, skills, and agent teams along five axes (who decides next, where intermediate results live, what's repeatable, scale, interruption), and ship one bundled workflow, `/deep-research`, which fans out searches, has independent agents adversarially cross-check sources, votes on each claim, and filters claims that don't survive. For someone deciding whether to read the full source: read it if you work on agent-orchestration, run-state persistence, or context-window economics — the comparison table and the "where intermediate results live" framing are the load-bearing parts.

## Connections Found

The companion [connect report](../reports/connect/sources/claude-code-dynamic-workflows-docs.connect.md) found no existing note names this feature (`rg` for "dynamic workflow", "ultracode", "deep-research" returned zero hits) — this is fresh source material. The strongest cluster is orchestration / scheduler-persistence. The report records three outbound `evidence` edges for this ingest's eventual authored surface and five reverse-edge candidates (the primary signal for a snapshot), all into that cluster:

- [RLM has the model write ephemeral orchestrators over sub-agents](../notes/rlm-has-the-model-write-ephemeral-orchestrators-over-sub-agents.md) — workflows are a shipped instance of the model writing the orchestrator as code with results in script variables, and the **non-ephemeral counterpoint**: the script is saveable, the exact path RLM opts out of.
- [Orchestration strategies and run-state have opposite persistence economics](../notes/orchestration-strategies-and-run-state-have-opposite-persistence.md) — the save-as-command flow promotes the recurring orchestration to durable library code while per-run results stay ephemeral in script variables — a deployed realization of the note's lifecycle split.
- [The chat-history model trades context efficiency for implementation simplicity](../notes/the-chat-history-model-trades-context-efficiency-for-implementation.md) — workflows keep intermediate agent results out of Claude's context, a concrete design avoiding the chat-history default.
- [Agent orchestration occupies a multi-dimensional design space](../notes/agent-orchestration-occupies-a-multi-dimensional-design-space.md) — the docs' own five-axis comparison table is a practitioner instance of the multi-axis (not single-ladder) framing.
- [Synthesis is not error correction](../notes/synthesis-is-not-error-correction.md) — `/deep-research` votes on each claim and filters claims that fail cross-checking rather than merging everything, exactly the distinction the note draws.

The connect report also flags a **synthesis opportunity**: this docs capture plus the parallel X-article snapshot ([a-harness-for-every-task-dynamic-workflows](../sources/a-harness-for-every-task-dynamic-workflows.md)) together with the RLM cluster could ground a note framing dynamic workflows as the saveable counterpoint to RLM's ephemeral orchestrators — the deployed example the persistence note currently lacks. The connect report notes (non-actionable maintenance context) that a future ingest pass should cross-reference the two snapshots with `compares-with`.

## Extractable Value

1. **The saveable-orchestrator data point that the persistence cluster is missing.** `orchestration-strategies-and-run-state-have-opposite-persistence` predicts a "self-populating host-language scheduler" / test-gated orchestrator cache where the recurring `select`-strategy gets promoted to durable code while run-state stays ephemeral. The `s` → save-as-command flow (`.claude/workflows/` or `~/.claude/workflows/`, runs as `/<name>`) is the concrete deployed instance of exactly that split. Highest reach: it closes a real gap in an existing note with a first-party example. [quick-win]

2. **A first-party axis table for the orchestration design space.** The "who decides next / where results live / what's repeatable / scale / interruption" table is a vendor-authored multi-axis comparison of subagents vs skills vs agent teams vs workflows. It corroborates `agent-orchestration-occupies-a-multi-dimensional-design-space` (orchestration is a space, not a ladder) and supplies named axes worth borrowing for retrieval and discussion. High reach. [quick-win]

3. **"Plan moves into code, so only the final answer lands in context."** A clean statement of the context-economics argument behind run-state persistence: script variables hold intermediate results so the context window is spared. Operationalizes `the-chat-history-model-trades-context-efficiency-for-implementation` and the run-state side of the persistence note. [just-a-reference]

4. **`/deep-research` as a shipped voting/filtering pipeline.** It "votes on each claim" and filters claims that "didn't survive cross-checking" via independent adversarial review — a product choosing filtering over merge-everything synthesis. Evidence for `synthesis-is-not-error-correction`, and an applied (if under-specified) case of decorrelated checks for `error-correction-works-above-chance-oracles-with-decorrelated-checks`. [just-a-reference]

5. **Concrete runtime constraints as design parameters.** 1,000 agents/run, 16 concurrent, no mid-run user input ("for sign-off between stages, run each stage as its own workflow"), no direct filesystem/shell from the script (agents act; the script coordinates), resume-within-session via cached agent results. These are specific bounds a methodology note on bounded-context orchestration could cite when discussing real coordination guarantees and stage boundaries. Context-bound to this product, but precise. [just-a-reference]

6. **`ultracode` as an automatic-orchestration effort level.** `/effort ultracode` makes Claude plan a workflow for every substantive task (one to understand, one to change, one to verify). A data point on deploy-time vs runtime decisions about when to codify orchestration — relevant to `deploy-time-learning-is-the-missing-middle` and the authorship axis of the RLM/persistence cluster. [just-a-reference]

## Limitations (our opinion)

This is vendor documentation, so the usual tool-announcement caveats apply (our opinion). What is not shown:

- **No evaluation or failure modes.** The docs assert workflows yield "a more trustworthy result than a single pass" and that adversarial review improves quality, with zero benchmarks, no TPR/FPR detail, and no reported failure cases. The `error-correction-works-above-chance-oracles-with-decorrelated-checks` note's preconditions (above-chance oracles, decorrelation) are exactly what the docs do not demonstrate — so treat the quality claims as design intent, not evidence.
- **Cost framing is soft.** "Meaningfully more tokens" plus advice to "run on a small slice first" acknowledges expense without quantifying the trade-off where a workflow is or isn't worth it.
- **Research preview, point-in-time.** Version-gated (v2.1.154+, trigger keyword changed at v2.1.160), constraints (1,000-agent cap, 16 concurrent) and surface (`/config` toggles, save locations) may shift; cite mechanics with the captured date in mind.
- **Saveability is described, durability is not.** The docs show how to save and rerun a script but say nothing about lineage, invalidation, or how a saved workflow ages as the codebase it audits changes — the maintenance questions our KB cares about most.

## Recommended Next Action

Write the note flagged in the connect report's synthesis opportunity: **a structured-claim note framing dynamic workflows as the saveable, script-authored counterpoint to RLM's ephemeral orchestrators** — the deployed realization of the promote-recurring-`select` / keep-run-state-ephemeral split that `orchestration-strategies-and-run-state-have-opposite-persistence.md` predicts but currently lacks a real example for. Draft it from both dynamic-workflow snapshots (this docs capture and the X-article harness capture), cite this snapshot and the RLM/chat-history notes as `evidence`, and add the `compares-with` cross-reference between the two snapshots at that time. If a full note is not yet warranted, the minimal alternative is a log entry plus the reverse-edge `evidence` citations into the RLM/persistence cluster.
