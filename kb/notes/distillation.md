---
description: Definition — distillation is compressing knowledge for a specific task under a context budget — the operation that context engineering machinery exists to perform; one of two co-equal learning mechanisms alongside constraining
type: note
traits: []
tags: [learning-theory]
status: current
---

# Distillation

One of two co-equal learning mechanisms in deployed agentic systems, alongside [constraining](./constraining.md). Distillation is **compressing knowledge for a specific task under a context budget**. The source can be anything — raw observations, methodology, prior reasoning, accumulated understanding. The target is always an artifact that equips a consumer (agent, collaborator) to perform a task.

[Context engineering](./context-engineering.md) is the architecture — the loading strategy, routing, the `select` function in the [scheduling model](./bounded-context-orchestration-model.md). Distillation is the main operation that architecture performs, though not the only one (routing, scoping, and maintenance are also context engineering operations).

## Why distillation exists

Different operational contexts need different things from the same body of knowledge. An agent connecting notes needs a step-by-step procedure — not fifteen methodology notes about Toulmin argument structure, link contracts, and title-as-claim conventions. An agent validating notes needs a different extraction from the same methodology. A smaller-context agent needs a more compressed version of either.

[Agent statelessness](./agent-statelessness-makes-routing-architectural-not-learned.md) makes this architectural rather than convenient. Each session starts fresh, so the reasoning that produced a procedure can't be "remembered" — it must either be loaded (expensive) or distilled into something that fits the context budget.

## How distillation works

The content is selected and compressed to fit the consumer's task and context budget. The rhetorical mode may shift if the task demands it (argumentative → procedural when the task is execution, exploratory → assertive when the task is deciding), but mode shift is incidental, not defining. What stays constant is the medium — unlike [codification](./codification.md), distillation typically stays in natural language consumed by an LLM.

| Source → Distillate | Target |
|---|---|
| Methodology → Skill | Agent performing a specific workflow |
| Workshop → Note | Future agents needing the insight |
| Research → Design principle | Decision-making in a particular area |
| Accumulated understanding → Campaign narrative | Collaborator joining the campaign now |
| Caller's knowledge + sub-agent's question → Refined prompt | Sub-agent facing a specific task |
| Many observations → Summary | Agent that can't fit them all in context |

Targeting is itself information loss — selecting what's relevant to one context means discarding what's relevant to others. This is why the source persists: it serves many targets, and each distillation chooses a different subset. Multiple distillations of the same source are normal. Reading only the `/connect` skill, you can connect notes but can't adapt the procedure to a novel situation. The methodology notes handle that.

A [campaign narrative](./active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes.md) is distillation of accumulated understanding for a collaborator who needs the current strategic picture, not the history. A [refined prompt](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) is distillation of the caller's knowledge for a sub-agent that needs a clean, self-contained task description. In both cases, "holistic rewrite" is what distillation looks like when the target artifact already exists — you re-distil rather than append, because appending accumulates rather than extracts.

## The dominant mechanism in knowledge work

Most KB learning is distillation. The typical cycle: explore messily → notice patterns → extract insight → write a note. The resulting note might then get [constrained](./constraining.md) (better description, structured sections, eventually code), but the initial learning act — the one that creates new knowledge — is extraction from a larger body of reasoning.

Constraining constrains what already exists. Distillation creates something new from something larger. In a knowledge system, creation matters more than hardening — you need something worth hardening first.

## Relationship to constraining

Constraining and distillation are orthogonal — they operate on different dimensions of the same artifacts:

| | Not distilled | Distilled |
|---|---|---|
| **Not constrained** | Raw capture (text file, session notes) | Extracted but loose (draft skill, rough note) |
| **Constrained** | Committed but not extracted (stored output, frozen config) | Extracted AND hardened (validated skill, codified script) |

Constraining asks: *how constrained is this artifact?* Distillation asks: *was this artifact extracted from something larger?*

You can distil without constraining (extract a skill — still natural language, still underspecified). You can constrain without distilling (store an LLM output — no extraction from reasoning involved). The full compound gain comes when both apply.

Not distillation: moving a validation check to code (codification — the operation is commitment, not extraction); storing an LLM output (constraining — commitment, no extraction from reasoning).

## Terminology note

ML "knowledge distillation" (Hinton et al., 2015) means training a smaller model to mimic a larger model's output distribution. The term here shares the core intuition — a larger source is compressed into a smaller target optimized for a specific consumer — but differs in important ways. ML distillation is automated (gradient descent), targets model weights, and optimizes for faithfully reproducing the teacher's behavior. KB distillation involves judgment about what to extract, targets text artifacts, and optimizes for operational effectiveness in a context — the distillate doesn't try to reproduce the source, it serves a different purpose. The closest ML analogy would be task-specific distillation (fine-tuning the student for a downstream task rather than matching the teacher's full distribution), but even that is more mechanical than what happens here. The term is worth keeping for the shared intuition of purposeful compression, but readers from an ML background should note the divergence.

---

Relevant Notes:

- [constraining](./constraining.md) — co-equal mechanism: constraining the interpretation space, orthogonal to distillation
- [codification](./codification.md) — the far end of constraining; sometimes follows distillation (extract a procedure, then codify it to code)
- [skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — the full argument for distillation as the mechanism behind skill creation
- [agent statelessness makes routing architectural](./agent-statelessness-makes-routing-architectural-not-learned.md) — why distillation is architecturally necessary: context budget constraints
- [deploy-time learning](./deploy-time-learning-the-missing-middle.md) — the substrate (repo artifacts) through which distillation operates
- [learning is not only about generality](./learning-is-not-only-about-generality.md) — foundation: capacity decomposes into generality vs reliability+speed+cost; distillation trades source completeness for operational efficiency
- [information value is observer-relative](./information-value-is-observer-relative-because-extraction-requires-computation.md) — grounds: reframes distillation as bounded information extraction; deterministic transformations create information for bounded observers
- [active-campaign understanding needs a single coherent narrative](./active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes.md) — exemplifies: campaign narratives are distillation of accumulated understanding for a specific consumer; holistic rewrite is re-distillation
- [conversation vs prompt refinement in agent-to-agent coordination](./conversation-vs-prompt-refinement-in-agent-to-agent-coordination.md) — exemplifies: prompt refinement is distillation of the caller's knowledge for a sub-agent's task
- [Epiplexity (Finzi et al., 2026)](../sources/from-entropy-to-epiplexity-rethinking-information-computationally-bounded.ingest.md) — grounds: epiplexity measures theoretically what distillation does operationally — quantifies extractable structure for a given observer under computational bounds
- [getsentry/skills](./related-systems/getsentry-skills.md) — production evidence: the skill-writer meta-skill shows that distillation quality depends primarily on source collection breadth ("keep collecting until retrieval passes no longer add new guidance"), not compression technique — a dimension this note underemphasizes
