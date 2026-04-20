---
description: Definition — distillation is compression viewed as learning; in KB methodology, directed context compression for a bounded consumer; co-equal learning mechanism alongside constraining
type: kb/types/definition.md
tags: [learning-theory]
status: current
---

# Distillation

Distillation is **compression viewed as learning** — goal-oriented compression whose purpose is the capacity change it produces in the consumer. The source is already-recorded material — a teacher model's outputs, methodology, accumulated reasoning, logged observations — re-compressed for a specific downstream consumer. This distinguishes distillation from general training, which compresses data without a particular consumer in mind. It sits in the task-oriented region of classical compression theory (rate-distortion, information bottleneck, MDL). By Simon's definition of learning — a permanent change in a system's capacity for adaptation — that capacity change *is* the operation's point, not an incidental side effect. In deployed agentic systems, distillation is one of two co-equal learning mechanisms alongside [constraining](./constraining.md); the same structure shows up in distinct substrates (see below).

In KB methodology, distillation is **directed context compression** — compressing knowledge so that a specific consumer can act on it within bounded context. "Directed" because different operational contexts need different extractions from the same source; "context" because the budget is a hard constraint, not a soft guideline. Without distillation, the source material often exceeds the consumer's [effective context](../effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) for the task — making the operation infeasible, not merely slow. Even when source material would technically fit, undistilled methodology crowds out the actual work — consuming tokens and adding navigational complexity. The source can be any already-recorded material — raw observations, methodology, prior reasoning, accumulated understanding — and the target is always an artifact that equips a consumer (agent, collaborator) to perform a task.

[Context engineering](./context-engineering.md) is the architecture — the loading strategy, routing, the `select` function in the [scheduling model](../bounded-context-orchestration-model.md). Distillation is the main operation that architecture performs, though not the only one (routing, scoping, and maintenance are also context engineering operations). Most KB learning is distillation in practice: explore messily, notice patterns, extract insight, write a note.

## Prior work

Distillation draws from two traditions.

**Purposeful compression** — classical information theory already has variants that relax strict message preservation in favor of goal-oriented preservation:

- **Rate-distortion theory** (Shannon, 1959) — lossy compression minimizes rate subject to a bounded distortion function; the distortion function is where the "goal" lives (JPEG's is perceptual, a theory's is "fails to answer queries correctly").
- **Information bottleneck** (Tishby et al., 1999) — compress X into T to maximize I(T;Y) under bounded I(X;T); directed compression for a specific downstream task variable Y.
- **Minimum description length / Kolmogorov complexity** — the shortest program that agrees with observations *is* a theory; theory-building is compression in the formal sense.
- **Simon's definition of learning** — "any change in a system that produces a more or less permanent change in its capacity for adapting to its environment." The compression-viewed-as-learning framing follows: any operative compression changes capacity, so compression ⊆ learning; distillation is the region where that capacity change is the operation's point.

**Audience-aware communication** — applied fields that practice goal-oriented compression on text:

- **Technical writing** — the discipline is built on audience analysis and purpose-driven restructuring. Progressive disclosure is distillation applied to documentation.
- **Pedagogical adaptation** — scaffolding (Vygotsky), curriculum design, and Bloom's taxonomy all address reshaping knowledge for learners at different levels.
- **Library science / abstracting** — professional abstracting and indexing is distillation optimized for retrieval decisions.
- **Knowledge management** — Nonaka & Takeuchi's externalization (tacit → explicit knowledge) describes a similar transformation, though without the context-budget framing.

Three things are specific to the agent context: the context budget is a hard constraint (rate-distortion with a specific rate cap); the query class the consumer will face is open-ended rather than a fixed distribution; and the consumer is itself a reasoner that can fill gaps rather than a passive decoder.

**TODO:** This survey is from the agent's training data, not systematic. Revisit with deep search — technical writing and pedagogy literatures likely have results about what makes distillation effective.

## How distillation works

Content is selected and compressed to fit the consumer's task and context budget. The rhetorical mode may shift if the task demands it — argumentative → procedural when the task is execution, exploratory → assertive when the task is deciding. In the KB application the medium stays constant: unlike [codification](./codification.md), distillation typically stays in natural language consumed by an LLM. Other instances target different substrates (see below).

| Source → Distillate | Target |
|---|---|
| Methodology → Skill | Agent performing a specific workflow |
| Workshop → Note | Future agents needing the insight |
| Research → Design principle | Decision-making in a particular area |
| Accumulated understanding → Narrative | Consumer who needs the current whole picture |
| Caller's knowledge + sub-agent's question → Refined prompt | Sub-agent facing a specific task |
| Domain artifacts (logs, patches, docs) → Detection/analysis skill | Agent diagnosing or investigating a class of problems |
| Many observations → Summary | Agent that can't fit them all in context |

Targeting is information loss — which is why the source persists. Reading only the `/connect` skill, you can connect notes but can't adapt the procedure to a novel situation; the methodology notes handle that.

A distillate can also look adequate while quietly losing behavioral influence: compressed experience is often less active than the raw traces it replaced ([Faithful Self-Evolvers](../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md)).

## Relationship to constraining

[Constraining](./constraining.md) and distillation are orthogonal — they operate on different dimensions of the same artifacts:

| | Not distilled | Distilled |
|---|---|---|
| **Not constrained** | Raw capture (text file, session notes) | Extracted but loose (draft skill, rough note) |
| **Constrained** | Committed but not extracted (stored output, frozen config) | Extracted AND hardened (validated skill, codified script) |

Constraining asks: *how constrained is this artifact?* Distillation asks: *was this artifact extracted from something larger?*

You can distill without constraining (extract a skill — still natural language, still underspecified), and you can constrain without distilling (store an LLM output — no extraction from reasoning involved). The full compound gain comes when both apply.

The orthogonality is at the artifact level, not the decision level. The choice to impose a given constraint is often itself a distillate of observed looseness — a rate limit of "100 req/s" encodes different provenance depending on whether it came from measurement or prediction. Evidence-driven constraining carries distilled understanding into the rule without leaving a visible trace in the rule itself; predictive constraining does not. Same artifact, different epistemic status.

## Instances

The general definition — goal-oriented compression whose purpose is capacity change in a bounded consumer — is realized in distinct substrates:

**KB distillation** (the focus of this note) — source: methodology, raw observations, prior reasoning, accumulated understanding. Target: text artifact. Consumer: a reasoning agent or collaborator. Capacity budget: the consumer's effective context for the task. Extraction mechanism: human or LLM judgment about what to preserve.

**ML knowledge distillation** (Hinton et al., 2015) — source: a large teacher model's output distribution (contrast general training, whose source is raw data). Target: a smaller student model's weights. Consumer: the student itself, deployed where the teacher won't fit. Capacity budget: parameter count. Extraction mechanism: gradient descent on a distillation loss.

Both satisfy the general definition. They differ in substrate and extraction mechanism, not in categorical structure. General ML training is the parent category — also compression producing capacity change, but without a specific downstream consumer; distillation is the subregion where compression targets a particular consumer that can't handle the source directly. Other instances are possible (task-oriented lossy codecs, human teaching) and would decompose along the same five dimensions.

---

Relevant Notes:

- [context efficiency is the central design concern](../context-efficiency-is-the-central-design-concern-in-agent-systems.md) — foundation: the bounded context that makes distillation a feasibility requirement, not just an optimization
- [effective context is task-relative](../effective-context-is-task-relative-and-complexity-relative-not-a-fixed-model-constant.md) — foundation: effective context depends on task complexity, so the same source may be feasible for one task and infeasible for another
- [constraining](./constraining.md) — co-equal mechanism: constraining the interpretation space, orthogonal to distillation
- [codification](./codification.md) — the far end of constraining; sometimes follows distillation (extract a procedure, then codify it to code)
- [skills derive from methodology through distillation](../skills-derive-from-methodology-through-distillation.md) — the full argument for distillation as the mechanism behind skill creation
- [agent statelessness makes routing architectural](../agent-statelessness-makes-routing-architectural-not-learned.md) — driver: each session starts fresh, so reasoning must be distilled rather than remembered
- [deploy-time learning](../deploy-time-learning-is-the-missing-middle.md) — the substrate (repo artifacts) through which distillation operates
- [learning is not only about generality](../learning-is-not-only-about-generality.md) — foundation: capacity decomposes into generality vs reliability+speed+cost; distillation trades source completeness for operational efficiency
- [information value is observer-relative](../information-value-is-observer-relative.md) — grounds: reframes distillation as bounded information extraction; deterministic transformations create information for bounded observers
- [evolving understanding needs re-distillation not composition](../evolving-understanding-needs-re-distillation-not-composition.md) — exemplifies: when a consumer needs the whole evolving picture, holistic rewrite is re-distillation
- [conversation vs prompt refinement in agent-to-agent coordination](../conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — exemplifies: prompt refinement is distillation of the caller's knowledge for a sub-agent's task
- [Epiplexity (Finzi et al., 2026)](../../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — grounds: epiplexity measures theoretically what distillation does operationally — quantifies extractable structure for a given observer under computational bounds
- [getsentry/skills](../../agent-memory-systems/reviews/getsentry-skills.md) — production evidence: the skill-writer meta-skill shows that distillation quality depends primarily on source collection breadth ("keep collecting until retrieval passes no longer add new guidance"), not compression technique — a dimension this note underemphasizes
- [Ingest: Large Language Model Agents Are Not Always Faithful Self-Evolvers](../../sources/large-language-model-agents-are-not-always-faithful-self-evolvers.ingest.md) — warning case: compressed experience can remain semantically plausible yet lose behavioral influence relative to the raw traces it distills
