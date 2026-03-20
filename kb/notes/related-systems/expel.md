---
description: Cross-task experiential learning pipeline that gathers trajectories, maintains natural-language rules, and retrieves past traces at inference; reviewed source promotes artifacts, not weights
type: note
tags: [related-systems]
status: current
last-checked: 2026-03-20
---

# ExpeL

ExpeL is a research codebase for LLM agents that learn from accumulated task experience. The implementation is explicitly staged: first gather trajectories over training tasks, then run a separate insight-extraction pass that turns those trajectories into reusable natural-language rules, then evaluate with both the rules and retrieved prior trajectories available at prompt time. Built by Andrew Zhao and collaborators as the official AAAI 2024 implementation.

**Repository:** https://github.com/LeapLabTHU/ExpeL

## Core Ideas

**Experience is trajectory-shaped, not session-shaped.** The repo does not mine one long interactive session. `train.py` gathers repeated task attempts over benchmark tasks, storing succeeded and failed trial histories. The later extraction stage works over those accumulated trajectories.

**Insight extraction is a distinct pipeline stage.** `insight_extraction.py` loads prior logs with `load_trajectories_log(...)`, reconstructs an `ExpelAgent`, and calls `create_rules(...)` over training folds. That separation matters: ExpeL treats "gather traces" and "generalize from traces" as two different jobs rather than one inline reflection loop.

**The learned artifact is a maintained rule list, not just raw reflections.** In `agent/expel.py`, `create_rules(...)` compares successful and failed trajectories, prompts for critique operations, parses `ADD`, `EDIT`, `REMOVE`, and `AGREE`, then updates `rule_items_with_count` through `update_rules(...)`. Rules gain or lose strength counters, can be edited in place, and disappear when their score falls to zero. This is a real artifact lifecycle, not append-only accumulation.

**ExpeL keeps both generalized and episodic memory.** At evaluation time, `insert_before_task_prompt()` injects the current numbered rule list through `rule_template`. Separately, `update_dynamic_prompt_components()` builds a vectorstore over prior successful trajectories and fewshots, then retrieves examples by task, thought, step, action, or rotation strategies. The agent therefore reuses both generalized rules and concrete past traces.

**Reflection is a precursor, not the final learned object.** `agent/reflect.py` still runs short natural-language reflection between failed attempts, but ExpeL's distinctive step is what happens afterward: those per-trial reflections and trajectories are later consolidated into a benchmark-level rule set. Relative to Reflexion, the repo is much more explicit about maintenance and cross-task generalization.

**Promotion stays in inspectable text artifacts.** In the reviewed source, learned results remain textual: reflections, trajectories, retrieved fewshots, and the numbered rule list. I did not find a path from ExpeL's gathered experience into model-weight updates.

## Comparison with Our System

ExpeL is closer to our trace-derived survey than most earlier reflection systems because it separates trace gathering from later consolidation and gives the learned artifact an explicit maintenance protocol. But it is still optimizing benchmark task performance, not curating an open-ended knowledge base.

| Dimension | ExpeL | Commonplace |
|---|---|---|
| Trace source | Repeated task trajectories across training tasks | Human+agent editing traces, notes, links, workshop artifacts |
| Learned substrate | Numbered natural-language rules plus retrievable prior trajectories | Notes, links, instructions, workshop artifacts |
| Promotion target | Inspectable prompt-time artifacts only | Inspectable text artifacts only |
| Update style | LLM-proposed `ADD/EDIT/REMOVE/AGREE` over a ranked rule list | Manual curation and targeted file edits |
| Oracle strength | Benchmark success/failure and task outcomes | Mostly human judgment and local validation |
| Scope | Cross-task within one benchmark family | Cross-domain KB |

ExpeL is stronger than our current system on automatic consolidation from repeated runs. It does the thing our survey keeps pointing at: mine trajectories, compare successes against failures, and maintain a reusable artifact with explicit operations instead of freeform rewrites.

Commonplace is stronger on compositional knowledge structure. ExpeL's learned rules are flat and benchmark-scoped. There is no equivalent of explicit semantic links, note types, or cross-domain maturation. A rule can be promoted, edited, or removed, but it cannot become part of a richer graph of explanations.

## Trace-derived learning placement

On axis 1 of [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md), ExpeL fits the **trajectory-run pattern**. It learns from completed task trajectories gathered across many benchmark tasks and folds, not from one live session log.

On axis 2, ExpeL is a strong **trace-derived artifact-learning** system. The promoted result is an inspectable rule list with an explicit lifecycle, plus prompt-time retrieval over prior successful traces. That places it closer to [Autocontext](./autocontext.md) and the [trajectory-informed memory generation ingest](../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) than to weight-learning systems like [OpenClaw-RL](../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md).

The interesting subtype signal is this: ExpeL does not just summarize trajectories into tips. It maintains a rule set with explicit mutation verbs and counters. Within the artifact-learning branch, that makes it one of the clearest examples of trajectory-to-rule consolidation rather than trajectory-to-summary compression.

## Borrowable Ideas

**Separate gathering from consolidation.** Ready now as a workshop pattern. ExpeL makes the boundary explicit: first collect traces, then run a later pass that generalizes across them. That is cleaner than trying to decide permanence inline during every run.

**Use explicit mutation verbs for learned artifacts.** Ready now as a design pattern. `ADD`, `EDIT`, `REMOVE`, and `AGREE` give the maintenance loop a visible contract and make artifact drift easier to reason about than whole-document rewrites.

**Keep a strength counter on learned rules.** Ready now as a lightweight ranking mechanism. ExpeL's counters are simple, but they create real lifecycle behavior: recurring rules harden, weak ones decay out.

**Retrieve past traces through multiple query slices.** Needs a use case first. The task/thought/step/action retrieval split is a useful reminder that "similarity" is not one thing. Different query surfaces may matter at different points in a run.

## Curiosity Pass

The strongest idea in ExpeL is not reflection by itself. Reflexion already showed that failed attempts can become verbal guidance. ExpeL's stronger move is to turn many such attempts into a maintained shared rule set and to keep the maintenance operations explicit in the code.

That makes ExpeL a better reference for durable artifact learning than most early trajectory-learning papers. It preserves inspectability, but it does not stay at the level of "retry with a better note to self." It tries to consolidate recurring patterns into something benchmark-level.

The ceiling is that its generalization target is still relatively flat. A ranked rule list is more durable than a reflection buffer, but it is still not a typed knowledge system. The repo shows how to stabilize tactical lessons, not how to build a linked body of explanatory knowledge.

## What to Watch

- Whether later descendants keep ExpeL's explicit rule operations or collapse back to whole-document synthesis
- Whether the counter-based rule lifecycle stays robust outside benchmark settings with clean success signals
- Whether the retrieval surface diversity actually matters, or is mostly benchmark-specific tuning
- Whether a future line bridges ExpeL-style artifact consolidation into weight updates, as Autocontext and OpenClaw-RL do on different paths
- Whether rule lists eventually need richer structure than flat numbered guidance

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: ExpeL is a clean trajectory-run artifact-learning case and sharpens the artifact side of the survey
- [Autocontext](./autocontext.md) — compares: both learn from repeated runs into inspectable artifacts, but Autocontext spans into optional weight distillation while ExpeL stays in rules and retrieved traces
- [Reflexion](./reflexion.md) — sharpens: ExpeL inherits the verbal reflection idea but adds a later consolidation stage with explicit rule maintenance
- [trajectory-informed-memory-generation-self-improving-agents ingest](../../sources/trajectory-informed-memory-generation-self-improving-agents.ingest.md) — compares: both extract guidance from trajectories, but ExpeL's code shows a more explicit rule-maintenance lifecycle
- [deploy-time learning](../deploy-time-learning-the-missing-middle.md) — sharpens: ExpeL shows the same artifact-learning mechanism through prompt-visible rules and retrieved traces, even though the repo packages it as a benchmark-loop research pipeline rather than a production deployment system
- [memory management policy is learnable but oracle-dependent](../memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: ExpeL also depends on the strength of its task oracle, but keeps the learned result inspectable instead of training it into weights
