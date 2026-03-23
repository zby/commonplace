---
description: Definition — distillation compresses knowledge so a consumer can act on it within bounded context, making operations feasible that raw source material would exceed; co-equal learning mechanism alongside constraining
type: note
traits: []
tags: [learning-theory]
status: current
---

# Distillation

One of two co-equal learning mechanisms in deployed agentic systems, alongside [constraining](./constraining.md). Distillation is **compressing knowledge so that a consumer can act on it within bounded context**. Without distillation, the source material often exceeds the consumer's [effective context](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) for the task — making the operation infeasible, not merely slow. Even when source material would technically fit, undistilled methodology crowds out the actual work — both by consuming tokens and by adding navigational complexity. The source can be anything — raw observations, methodology, prior reasoning, accumulated understanding. The target is always an artifact that equips a consumer (agent, collaborator) to perform a task. Different operational contexts need different extractions from the same source, so multiple distillations are normal — each serves a different consumer-task pair.

[Context engineering](./context-engineering.md) is the architecture — the loading strategy, routing, the `select` function in the [scheduling model](./bounded-context-orchestration-model.md). Distillation is the main operation that architecture performs, though not the only one (routing, scoping, and maintenance are also context engineering operations).

Most KB learning is distillation — explore messily, notice patterns, extract insight, write a note.

## Prior work

Compressing knowledge for a specific audience is not new — it's the core of several established fields:

- **Technical writing** — the discipline is built on audience analysis and purpose-driven restructuring. Progressive disclosure is distillation applied to documentation.
- **Pedagogical adaptation** — scaffolding (Vygotsky), curriculum design, and Bloom's taxonomy all address reshaping knowledge for learners at different levels.
- **Library science / abstracting** — professional abstracting and indexing is distillation optimized for retrieval decisions.
- **Knowledge management** — Nonaka & Takeuchi's externalization (tacit → explicit knowledge) describes a similar transformation, though without the context-budget framing.

What's specific to our use is the agent context: the context budget is a hard constraint, not a soft guideline.

**TODO:** This survey is from the agent's training data, not systematic. Revisit with deep search — technical writing and pedagogy literatures likely have results about what makes distillation effective.

## How distillation works

The content is selected and compressed to fit the consumer's task and context budget. The rhetorical mode may shift if the task demands it (argumentative → procedural when the task is execution, exploratory → assertive when the task is deciding). What stays constant is the medium — unlike [codification](./codification.md), distillation typically stays in natural language consumed by an LLM.

| Source → Distillate | Target |
|---|---|
| Methodology → Skill | Agent performing a specific workflow |
| Workshop → Note | Future agents needing the insight |
| Research → Design principle | Decision-making in a particular area |
| Accumulated understanding → Narrative | Consumer who needs the current whole picture |
| Caller's knowledge + sub-agent's question → Refined prompt | Sub-agent facing a specific task |
| Domain artifacts (logs, patches, docs) → Detection/analysis skill | Agent diagnosing or investigating a class of problems |
| Many observations → Summary | Agent that can't fit them all in context |

Targeting is information loss — this is why the source persists. Reading only the `/connect` skill, you can connect notes but can't adapt the procedure to a novel situation. The methodology notes handle that.

Warning: a distillate can look adequate while losing behavioral influence — compressed experience is often less active than the raw traces it replaced ([Faithful Self-Evolvers](../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md)).

## Relationship to constraining

Constraining and distillation are orthogonal — they operate on different dimensions of the same artifacts:

| | Not distilled | Distilled |
|---|---|---|
| **Not constrained** | Raw capture (text file, session notes) | Extracted but loose (draft skill, rough note) |
| **Constrained** | Committed but not extracted (stored output, frozen config) | Extracted AND hardened (validated skill, codified script) |

Constraining asks: *how constrained is this artifact?* Distillation asks: *was this artifact extracted from something larger?*

You can distil without constraining (extract a skill — still natural language, still underspecified). You can constrain without distilling (store an LLM output — no extraction from reasoning involved). The full compound gain comes when both apply.

## Terminology note

ML "knowledge distillation" (Hinton et al., 2015) trains a smaller model to mimic a larger model's output distribution — automated, targets weights, optimizes for reproducing the teacher's behavior. KB distillation involves judgment about what to extract, targets text artifacts, and optimizes for operational effectiveness — the distillate serves a different purpose than the source. Shared intuition: purposeful compression from a larger source into a smaller target for a specific consumer.

---

Relevant Notes:

- [context efficiency is the central design concern](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — foundation: the bounded context that makes distillation a feasibility requirement, not just an optimization
- [effective context is task-relative](./effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) — foundation: effective context depends on task complexity, so the same source may be feasible for one task and infeasible for another
- [constraining](./constraining.md) — co-equal mechanism: constraining the interpretation space, orthogonal to distillation
- [codification](./codification.md) — the far end of constraining; sometimes follows distillation (extract a procedure, then codify it to code)
- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — the full argument for distillation as the mechanism behind skill creation
- [agent statelessness makes routing architectural](./agent-statelessness-makes-routing-architectural-not-learned.md) — driver: each session starts fresh, so reasoning must be distilled rather than remembered
- [deploy-time learning](./deploy-time-learning-the-missing-middle.md) — the substrate (repo artifacts) through which distillation operates
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — foundation: capacity decomposes into generality vs reliability+speed+cost; distillation trades source completeness for operational efficiency
- [information value is observer-relative](./information-value-is-observer-relative.md) — grounds: reframes distillation as bounded information extraction; deterministic transformations create information for bounded observers
- [evolving understanding needs re-distillation not composition](./evolving-understanding-needs-re-distillation-not-composition.md) — exemplifies: when a consumer needs the whole evolving picture, holistic rewrite is re-distillation
- [conversation vs prompt refinement in agent-to-agent coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — exemplifies: prompt refinement is distillation of the caller's knowledge for a sub-agent's task
- [Epiplexity (Finzi et al., 2026)](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — grounds: epiplexity measures theoretically what distillation does operationally — quantifies extractable structure for a given observer under computational bounds
- [getsentry/skills](./related-systems/getsentry-skills.md) — production evidence: the skill-writer meta-skill shows that distillation quality depends primarily on source collection breadth ("keep collecting until retrieval passes no longer add new guidance"), not compression technique — a dimension this note underemphasizes
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md) — warning case: compressed experience can remain semantically plausible yet lose behavioral influence relative to the raw traces it distills
