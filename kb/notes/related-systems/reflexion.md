---
description: Verbal reinforcement loop that converts failed attempts into short natural-language reflections reused on later tries — early trajectory-based artifact learning without weight updates
type: note
tags: [related-systems]
status: current
last-checked: 2026-03-18
---

# Reflexion

Reflexion is a research codebase for language agents that improve through verbal self-critique. Across reasoning, programming, and environment tasks, the core loop is: attempt a task, observe failure feedback, generate a short natural-language reflection, then feed that reflection into the next attempt. Built by Noah Shinn and collaborators as a NeurIPS 2023 research repo.

**Repository:** https://github.com/noahshinn/reflexion

## Core Ideas

**Feedback becomes natural-language memory, not weights.** Reflexion does not update model parameters in the reviewed repo. It turns failure feedback into short textual reflections or plans that are reused in later attempts.

**The stored unit is deliberately small.** In ALFWorld, failed runs become concise "New plan" strings and only the last few memories are carried forward. In the programming runs, each failed implementation can produce a self-reflection string that conditions the next implementation attempt. This is memory as a bounded hint buffer, not a growing knowledge base.

**The trace substrate is repeated task attempts with explicit failure feedback.** For programming, the signal is unit-test feedback and execution results. For ALFWorld, it is the failed trial log for a specific environment task. Reflexion is not mining long-lived sessions; it is mining bounded trial history.

**Reinjection is prompt-time only.** Reflections are appended into the next prompt through task-specific prompt builders like `EnvironmentHistory`. The repo does not export training data or define a weight-learning path.

**The implementation is thin and domain-specific.** The repo is closer to experiment scaffolding than to a general memory framework. Much of the mechanism is duplicated across task directories, and the persistent memory structure is usually just a list of recent reflection strings.

## Comparison with Our System

Reflexion is an early and important artifact-learning reference, but it is much narrower than the workshop-memory systems in our KB. It learns from trajectories, yet the learned artifact is a tiny rolling buffer of self-advice rather than a maintained body of durable knowledge.

| Dimension | Reflexion | Commonplace |
|---|---|---|
| Trace source | Failed task attempts plus feedback or execution results | Human+agent editing traces, notes, links, workshop artifacts |
| Learned substrate | Short natural-language reflections/plans | Notes, links, instructions, workshop artifacts |
| Promotion target | Prompt-time text only | Inspectable text artifacts only |
| Update style | Append reflection, retry, keep a few recent memories | Manual curation and targeted file edits |
| Oracle strength | Strong local oracle: tests, rewards, success/failure | Weak, mostly human judgment |
| Scope | Per-task and per-benchmark loop | Cross-domain KB |

**Trace-derived learning placement.** On axis 1 of the survey, Reflexion fits the **trajectory-run pattern**: it learns from repeated bounded attempts at the same task family. On axis 2, it is a narrow **trace-derived artifact-learning** system: the promoted result is textual reflection, but usually only as short prompt memory rather than a rich artifact store. It belongs in the survey as a historical precedent and as a lower-structure comparison point.

Relative to [OpenClaw-RL ingest](../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md), Reflexion preserves inspectable verbal feedback but gives up the possibility of parameter adaptation. Relative to [ClawVault](./clawvault.md), it has a much weaker artifact lifecycle: hints are reused, but not matured into typed durable documents.

## Borrowable Ideas

**Failure-to-plan conversion.** Ready now as a workshop pattern. The ALFWorld loop is extremely simple: failed trajectory in, concise new plan out, next attempt conditioned on that plan. That is a clean minimal reflection skill.

**Keep only the recent memory tail.** Ready now as a constraint. Reflexion's "last few reflections only" rule is a useful reminder that not every artifact-learning loop should accumulate indefinitely.

**Task-local reflection before global promotion.** Needs a use case first. Reflexion suggests a two-stage lifecycle: first produce a cheap task-local hint, then only later decide whether it deserves durable promotion.

## Curiosity Pass

Reflexion's main contribution is conceptual economy. It shows that a learning loop can exist without embeddings, vector stores, or training pipelines: just use failure feedback to produce a better hint for the next try.

The trade-off is that the learned artifact has low reach. Most stored reflections are tightly bound to a task, environment, or failing implementation. That makes the system a good ancestor for the survey, but not yet a strong model of durable memory.

So Reflexion is best read as an early trajectory-to-artifact loop with minimal structure. It is closer to "retry with a better note to self" than to a full memory system.

## What to Watch

- Whether later descendants add stronger artifact structure on top of Reflexion's verbal loop
- Whether the small-memory-tail pattern remains competitive against larger artifact stores
- Whether weight-learning systems keep the same feedback decomposition while changing only the promotion target
- Whether prompt-only verbal reinforcement scales beyond benchmark-local retries

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Reflexion is an early artifact-learning precedent for trajectory-based verbal memory
- [ClawVault](./clawvault.md) — contrasts: both preserve inspectable text, but ClawVault has a richer artifact lifecycle and typed promotion path
- [memory management policy is learnable but oracle-dependent](../memory-management-policy-is-learnable-but-oracle-dependent.md) — sharpens: Reflexion also depends on strong local oracles, but keeps the result in prompt-visible text rather than weights
- [OpenClaw-RL: Train Any Agent Simply by Talking](../../sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) — contrasts: same broad idea of learning from ongoing interaction, different promotion target and much weaker training machinery
- [deploy-time learning](../deploy-time-learning-the-missing-middle.md) — sharpens: Reflexion sits in the deploy-time artifact-update space, where learning happens by changing prompt-visible text rather than training weights
