---
description: Definition — distillation is targeted transformation of recorded material into a use-shaped artifact for a particular downstream consumer; in KB practice this is usually directed context compression
type: kb/types/definition.md
tags: [learning-theory]
status: current
---

# Distillation

Distillation is targeted transformation of already-recorded material into an artifact shaped for a particular downstream consumer. The target artifact preserves what the consumer needs from the source in a form the consumer can use.

In KB practice, distillation is usually directed context compression, because agents, maintainers, collaborators, and artifacts operate under bounded context. Compression is the common pressure, not the definition: a distillate may also reorganize, reframe, change register, make implicit structure explicit, or expand a key point while still being shaped for one use.

## Scope

Use the term distillation when recorded material has been reshaped into an artifact for a particular downstream consumer. The source can be methodology, raw observations, prior reasoning, traces, research, a teacher model's outputs, or accumulated understanding. The resulting distillate can be a note, skill, instruction, prompt, review lens, design principle, summary, or model update.

Common KB instances:

- methodology notes → skill body for an agent executing a workflow;
- workshop material → durable note for future reasoning;
- source article → claim summary for ingestion;
- caller context → refined prompt for a sub-agent;
- repeated review failures → gate instruction or validation rule.

Most KB learning has a distillation phase: explore messily, notice patterns, then write an artifact that future agents can actually use.

## How distillation works

Distillation changes shape. Content may be selected, reorganized, reframed, compressed, expanded, or moved into another register to fit the consumer's task and context budget. Argumentative material can become procedural guidance; exploratory notes can become an assertive claim; a broad workshop can become a narrow note.

| Source → Distillate | Target |
|---|---|
| Methodology → Skill | Agent performing a specific workflow |
| Workshop → Note | Future agents needing the insight |
| Research → Design principle | Decision-making in a particular area |
| Accumulated understanding → Narrative | Consumer who needs the current whole picture |
| Caller's knowledge + sub-agent's question → Refined prompt | Sub-agent facing a specific task |
| Domain artifacts (logs, patches, docs) → Detection/analysis skill | Agent diagnosing or investigating a class of problems |
| Many observations → Summary | Agent that can't fit them all in context |

Targeting usually loses information, so a distillate does not replace its source for every purpose. A skill may preserve the steps needed to run a workflow while omitting the rationale, alternatives, and failed approaches needed to adapt that workflow to a novel situation.

A distillate can also look adequate while quietly losing behavioral influence: compressed experience is often less active than the raw traces it replaced ([Faithful Self-Evolvers](https://arxiv.org/html/2601.22436v2)).

## Exclusions

Distillation is not retrieval. Retrieval selects existing material; distillation rewrites or re-encodes material for use.

Distillation is not all training. General training may produce capacity change without a particular downstream consumer in view; distillation targets a consumer or use.

Distillation is not [constraining](./constraining.md), though the same artifact may be both distilled and constrained.

## Relationship to constraining

[Constraining](./constraining.md) and distillation operate on different dimensions of the same artifacts:

| | Not distilled | Distilled |
|---|---|---|
| **Not constrained** | Raw capture (text file, session notes) | Use-shaped but semantically loose (draft skill, rough note) |
| **Constrained** | Committed but not transformed from a source (stored output, frozen config) | Use-shaped and semantically focused (validated skill, codified script) |

Constraining asks: *how constrained is this artifact?* Distillation asks: *was this artifact transformed from recorded source material for a particular consumer?*

You can distill without constraining (write a task-shaped skill that remains natural language and underspecified), and you can constrain without distilling (store an LLM output, committing to one interpretation without transforming recorded source material). Strong artifacts often combine both.

The distinction is at the artifact level, not the decision level. The choice to impose a constraint can itself be a distillate of observed looseness: the same rate limit has different epistemic status depending on whether it came from measurement or prediction.

## Instances

The same pattern appears in different media.

**KB distillation** is the focus of this note. A workshop, source, trace, or body of methodology is reshaped into a note, skill, instruction, prompt, or review lens for a future agent or collaborator. The consumer's effective context is the main budget, so the result is usually shorter than the source, but the important change is use-shaping: the artifact is written in the form the consumer can act on.

**ML knowledge distillation** (Hinton et al., 2015) has the same structure in a different substrate. A large teacher model's output distribution is transformed into a smaller student model's weights. The consumer is the student model, and the budget is parameter count or deployment cost rather than prompt context.

Both cases transform a source the consumer cannot use directly into a target the consumer can use. They differ in medium and mechanism, not in the role the transformation plays.

[Context engineering](./context-engineering.md) is the architecture that routes, loads, scopes, and maintains knowledge under bounded context. Distillation is the main operation that architecture performs, though not the only one.

---

Relevant Notes:

- [context efficiency is the central design concern](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — foundation: the bounded context that makes distillation a feasibility requirement, not just an optimization
- [agent context is constrained by soft degradation, not hard token limits](../agent-context-is-constrained-by-soft-degradation-not-hard-token-limits.md) — foundation: effective context depends on task complexity, so the same source may be feasible for one task and infeasible for another
- [constraining](./constraining.md) — co-equal mechanism: constraining the interpretation space, orthogonal to distillation
- [codification](./codification.md) — the far end of constraining; sometimes follows distillation (reshape a procedure for use, then commit it to a symbolic artifact)
- [skills derive from methodology through distillation](../skills-derive-from-methodology-through-distillation.md) — the full argument for distillation as the mechanism behind skill creation
- [agent statelessness makes routing architectural](../agent-statelessness-makes-routing-architectural-not-learned.md) — driver: each session starts fresh, so reasoning must be distilled rather than remembered
- [deploy-time learning](../deploy-time-learning-is-the-missing-middle.md) — timing frame for durable artifact updates that distillation can produce
- [learning is not only about generality](../learning-is-not-only-about-generality.md) — foundation: capacity decomposes into generality vs reliability+speed+cost; distillation trades source completeness for operational efficiency
- [information value is observer-relative](../information-value-is-observer-relative.md) — grounds: reframes distillation as bounded information extraction; deterministic transformations create information for bounded observers
- [evolving understanding needs re-distillation not composition](../evolving-understanding-needs-re-distillation-not-composition.md) — exemplifies: when a consumer needs the whole evolving picture, holistic rewrite is re-distillation
- [conversation vs prompt refinement in agent-to-agent coordination](../conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — exemplifies: prompt refinement is distillation of the caller's knowledge for a sub-agent's task
- [Epiplexity (Finzi et al., 2026)](https://arxiv.org/html/2601.03220v1) — grounds: epiplexity measures theoretically what distillation does operationally — quantifies extractable structure for a given observer under computational bounds
- [getsentry/skills](../../agent-memory-systems/reviews/getsentry-skills.md) — production evidence: the skill-writer meta-skill shows that distillation quality depends primarily on source collection breadth ("keep collecting until retrieval passes no longer add new guidance"), not compression technique — a dimension this note underemphasizes
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](https://arxiv.org/html/2601.22436v2) — warning case: compressed experience can remain semantically plausible yet lose behavioral influence relative to the raw traces it distills
