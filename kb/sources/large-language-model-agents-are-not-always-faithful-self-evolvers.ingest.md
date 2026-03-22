---
description: Causal-intervention paper showing compressed agent memories can improve systems yet fail faithfulness tests, making behavioral dependence the missing metric for self-evolving agents
source_snapshot: large-language-model-agents-are-not-always-faithful-self-evolvers.md
ingested: 2026-03-22
type: scientific-paper
domains: [agent-memory, distillation, verification, llm-agents]
---

# Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers

Source: large-language-model-agents-are-not-always-faithful-self-evolvers.md
Captured: 2026-03-22
From: https://arxiv.org/html/2601.22436v2

## Classification
Type: scientific-paper — arXiv/ICML-style paper with explicit methodology, controlled interventions, multiple frameworks/models/environments, and a concrete empirical claim about agent behavior.
Domains: agent-memory, distillation, verification, llm-agents
Author: Multi-author research team working directly on self-evolving-agent benchmarks; worth attending to here because they evaluate several established frameworks (ExpeL, Dynamic Cheatsheet, ReasoningBank, G-Memory) rather than proposing only a new memory design.

## Summary
This paper asks whether self-evolving LLM agents actually use the experience they store, or merely carry it around. It defines **experience faithfulness** as causal dependence of behavior on the provided experience, then tests that by intervening on two memory forms: raw trajectories and condensed summaries. Across four representative frameworks, 10 LLM backbones, and 9 environments, the main result is a strong asymmetry: agents reliably depend on raw experience, but often ignore or misread condensed experience, even when condensed memory is the only guidance available. The authors attribute this to three factors: condensed summaries often lack actionable specificity, model internals overweight local/current context relative to retrieved summaries, and some task regimes can be solved well enough from pretrained priors that external experience never becomes causally necessary.

## Connections Found
`/connect` found two strong fit clusters. In learning theory, the source connects to [distillation](../notes/distillation.md) because condensed experience is a distilled artifact whose failure mode is now empirical rather than hypothetical, and to [deploy-time learning](../notes/deploy-time-learning-the-missing-middle.md) because the paper studies symbolic cross-session adaptation but shows that artifact presence is not enough — artifacts must remain behaviorally active. In the trace-derived / related-systems cluster, it connects to [trace-derived learning techniques in related systems](../notes/trace-derived-learning-techniques-in-related-systems.md) by adding a missing evaluation axis (faithfulness at inference time), to [the fundamental split in agent memory is not storage format but who decides what to remember](../notes/related-systems/agentic-memory-systems-comparative-review.md) by suggesting a new “use-time faithfulness” dimension for memory systems, and directly grounds the nearby framework notes [ExpeL](../notes/related-systems/expel.md) and [Dynamic Cheatsheet](../notes/related-systems/dynamic-cheatsheet.md), which the paper evaluates explicitly.

## Extractable Value
1. [experiment] Add **faithfulness-by-intervention** as a standard evaluation for artifact-learning systems: perturb stored memory and measure whether downstream behavior changes. This has high reach because it tests whether a learned artifact is causally operative, not just present.
2. [quick-win] Treat **behavioral faithfulness** as a missing quality criterion for [distillation](../notes/distillation.md): a summary is not good just because it is concise or semantically plausible; it must preserve enough structure to steer later behavior.
3. [deep-dive] Extend [the fundamental split in agent memory is not storage format but who decides what to remember](../notes/related-systems/agentic-memory-systems-comparative-review.md) with a seventh dimension: **use-time faithfulness**. This paper shows that storage unit, agency, and link structure are still incomplete without asking whether the agent actually depends on the stored artifact.
4. [experiment] Preserve both **raw traces and condensed summaries** in learning loops, then choose by task. The paper suggests compressed guidance is not a drop-in substitute for raw episodic detail; some tasks may need replayable traces while others can tolerate distillation.
5. [experiment] Design condensation methods to optimize for **actionable specificity and causal uptake**, not just brevity. The paper’s strongest mechanism claim is that many summaries are too semantically weak to win against local context or pretrained priors.
6. [just-a-reference] Use the paper as empirical support in [trace-derived learning techniques in related systems](../notes/trace-derived-learning-techniques-in-related-systems.md): the survey already compares trace sources and promotion targets, and this source adds evidence that promoted artifacts can differ sharply in causal influence even within the same family of systems.

## Limitations (our opinion)
The strongest result here is the raw-vs-condensed asymmetry; the strongest *narrative* result is the three-cause explanation, and those are not equally well supported. The paper does not test many alternate condensation strategies designed explicitly for behavioral actionability, so its conclusion is best read as “current summary forms often fail” rather than “compression as such fails.” The benchmark mix is also tilted toward research environments and knowledge-intensive QA, which matters because the task-dependence story partly reduces to “the model already knows enough”; that may transfer unevenly to software, KB curation, or other domains where pretrained priors are weaker and raw traces are costlier to carry. The internal-bias evidence relies on attribution analysis, which is suggestive rather than definitive, and the task-dependence section narrows to a small set of additional QA benchmarks under specific model/framework conditions. Finally, the paper measures whether memory is **used**, not whether it is **good**: an unfaithful summary can still raise scores, and a faithful memory can still be wrong. In KB terms, this is a missing complement to the verification/oracle notes — faithfulness is a necessary test for memory quality, not a sufficient one.

## Recommended Next Action
Write a note titled **“Behavioral faithfulness is the missing evaluation criterion for distillation”** connecting to [distillation](../notes/distillation.md) and [deploy-time learning](../notes/deploy-time-learning-the-missing-middle.md) — it would argue that compressed artifacts should be judged by whether perturbing them changes downstream behavior, not just by semantic plausibility or task score.
