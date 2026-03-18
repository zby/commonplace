# Connection Report: Why AI systems don't learn and what to do about it

**Source:** [why-ai-systems-dont-learn-and-what-to-do-about-it](kb/sources/why-ai-systems-dont-learn-and-what-to-do-about-it.md)
**Date:** 2026-03-18
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read [kb/notes/index.md](kb/notes/index.md) — flagged candidates:
  - [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — strongest description-level tension: source says deployed AI does not learn; note says deployed systems do learn via repo artifacts
  - [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md) — direct overlap on "continuous learning" but opposite substrate assumptions
  - [llm-learning-phases-fall-between-human-learning-modes](kb/notes/llm-learning-phases-fall-between-human-learning-modes.md) — source leans heavily on human/animal cognition; note warns against literal human-LLM learning-mode mapping
  - [in-context-learning-presupposes-context-engineering](kb/notes/in-context-learning-presupposes-context-engineering.md) — source's System M looks like a broader meta-control version of context engineering
  - [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) — source asks for autonomous learning architectures; this note names oracle/evaluation as the missing bottleneck
  - [agent-statelessness-makes-routing-architectural-not-learned](kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md) — possible contrast: current KB agents are runtimes, not learners
  - [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md) — shared control-plane vocabulary; needed verification that this was more than metaphor overlap

**Topic indexes:**
- Read [kb/notes/tags-index.md](kb/notes/tags-index.md) — routed to [kb/notes/learning-theory-index.md](kb/notes/learning-theory-index.md)
- Read [kb/notes/learning-theory-index.md](kb/notes/learning-theory-index.md) — reinforced:
  - [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md)
  - [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md)
  - [llm-learning-phases-fall-between-human-learning-modes](kb/notes/llm-learning-phases-fall-between-human-learning-modes.md)
  - [in-context-learning-presupposes-context-engineering](kb/notes/in-context-learning-presupposes-context-engineering.md)
  - [context-engineering](kb/notes/context-engineering.md)

**Semantic search:** (via qmd, with grep fallback after partial qmd failure)
- query `"autonomous learning meta-control lifelong adaptation learning from observation and action"` — top hits:
  - [trace-derived-learning-techniques-in-related-systems](kb/notes/trace-derived-learning-techniques-in-related-systems.md) (88%) — strong lexical/semantic overlap on autonomous learning loops, but the note's real focus is trace ingestion and promotion targets, not the source's A/B/M architecture
  - [learning-is-not-only-about-generality](kb/notes/learning-is-not-only-about-generality.md) (50%) — useful foundation but too general for a direct source link
  - [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) (38%) — genuine mechanism overlap on what blocks autonomous learning
  - [context-engineering](kb/notes/context-engineering.md) (32%) — moderate match through the control-plane/routing frame
- query `"continuous learning during deployment through artifacts versus weight updates"` — top hits:
  - [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md) (93%) — strongest direct connection
  - [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) (43%) — same dispute over where learning happens
  - [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) (43%) — names the remaining bottleneck once artifact-based learning is accepted
  - [in-context-learning-presupposes-context-engineering](kb/notes/in-context-learning-presupposes-context-engineering.md) (41%) — relocates learning to the system layer
  - [agent-statelessness-makes-routing-architectural-not-learned](kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md) (34%) — possible contrast, needed manual check
- query `"control plane meta-control routing data selection context engineering"` — qmd failed with `InsufficientMemoryError`; fell back to keyword search
- query over `sources` for autonomous learning — qmd failed with the same VRAM error; fell back to existing linked ingests and grep results

**Keyword search:**
- `rg -n "autonomous learning|meta-control|MLOps|lifelong|deployment|continual learning|learn after deployment|learning from action|learning from observation" kb/notes kb/sources --glob '*.md'`
  - found [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md) — explicit continuous-learning contrast
  - found [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — explicit training/in-context/deploy-time distinction
  - found [in-context-learning-presupposes-context-engineering](kb/notes/in-context-learning-presupposes-context-engineering.md) — explicit "continual learning may be unnecessary" rebuttal pattern
  - found [llm-learning-phases-fall-between-human-learning-modes](kb/notes/llm-learning-phases-fall-between-human-learning-modes.md) — explicit human-learning comparison
  - found [openclaw-rl-train-any-agent-simply-by-talking.ingest.md](kb/sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) — concrete counterexample where deployed agents do learn via weights
  - found [dario-amodei-we-are-near-the-end-of-the-exponential.ingest.md](kb/sources/dario-amodei-we-are-near-the-end-of-the-exponential.ingest.md) — adjacent debate about whether continual learning is needed
- `rg -n "control plane|meta-control|autonomous learning|continuous learning|deploy-time learning|learning modes|stateless|learner" kb/notes --glob '*.md'`
  - confirmed [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md) is only a vocabulary match
  - confirmed [agent-statelessness-makes-routing-architectural-not-learned](kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md) is a present-day design note, not a direct argument about autonomous learning architectures

**Link following:**
- From [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md): followed links to [in-context-learning-presupposes-context-engineering](kb/notes/in-context-learning-presupposes-context-engineering.md) and [openclaw-rl-train-any-agent-simply-by-talking.ingest.md](kb/sources/openclaw-rl-train-any-agent-simply-by-talking.ingest.md) — clarified that the KB already distinguishes artifact learning from live weight learning
- From [llm-learning-phases-fall-between-human-learning-modes](kb/notes/llm-learning-phases-fall-between-human-learning-modes.md): followed the Amodei connection implicitly via [dario-amodei-we-are-near-the-end-of-the-exponential.ingest.md](kb/sources/dario-amodei-we-are-near-the-end-of-the-exponential.ingest.md) — confirmed existing KB skepticism about literal human-learning analogies
- From [in-context-learning-presupposes-context-engineering](kb/notes/in-context-learning-presupposes-context-engineering.md): link structure already points back to deploy-time learning and continuous-learning notes; no new neighborhood emerged beyond the core cluster

## Connections Found

- [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — **contradicts**: the source's headline claim is that current AI systems do not learn after deployment because learning has been externalized into human-run MLOps. This note makes the opposite system-level claim: deployed systems can learn through durable repo artifacts even when weights stay fixed. The tension is productive rather than total: the source is correct at the model-weight level, while the note argues the system boundary should include artifacts.
- [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md) — **extends**: once Simon's "capacity change" definition is adopted, the source's diagnosis becomes too narrow. This note provides the missing definitional move: prompts, schemas, evals, tools, and code updates are genuine learning if they durably improve adaptation. The source identifies a real gap, but this note narrows it from "AI doesn't learn" to "current models don't autonomously self-improve through integrated observation/action/meta-control."
- [in-context-learning-presupposes-context-engineering](kb/notes/in-context-learning-presupposes-context-engineering.md) — **extends**: the source's System M is a general meta-control layer that selects what to learn from, how to route information, and when to switch modes. This note is the KB's present-day, narrower analogue: before a model can adapt in context, a context-engineering layer must decide what enters the window and how it is framed. Following the link gives a concrete modern instantiation of "meta-control" on today's stacks.
- [llm-learning-phases-fall-between-human-learning-modes](kb/notes/llm-learning-phases-fall-between-human-learning-modes.md) — **contradicts**: the source leans on child/animal cognition as a direct architectural guide. This note pushes back on literal mapping: LLM learning phases do not line up cleanly with human learning modes, so analogies are suggestive but not structurally reliable. The connection is useful because it turns the paper's strongest rhetorical move into an explicit methodological caution.
- [automating-kb-learning-is-an-open-problem](kb/notes/automating-kb-learning-is-an-open-problem.md) — **extends**: the source offers a broad architectural roadmap for autonomous learning but leaves the evaluation problem underspecified. This note sharpens the bottleneck: the hard part is not naming A/B/M components, but manufacturing oracles for judgment-heavy learning operations. It helps explain why the source remains a conceptual roadmap rather than an actionable engineering recipe.

**Bidirectional candidates** (reverse link also worth adding):
- [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) ↔ source — **contradicts**: the note would benefit from this paper as a clean statement of the model-centric view it is rebutting
- [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md) ↔ source — **extends/contradicts**: the note would benefit from this paper as a high-status example of the default ML framing it is revising
- [llm-learning-phases-fall-between-human-learning-modes](kb/notes/llm-learning-phases-fall-between-human-learning-modes.md) ↔ source — **contradicts**: the note should link to a more explicit cognitive-science roadmap than the current Amodei-only support

## Rejected Candidates

- [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md) — shared "control plane" vocabulary only; the note is about repository instruction placement, not learning-mode arbitration
- [agent-statelessness-makes-routing-architectural-not-learned](kb/notes/agent-statelessness-makes-routing-architectural-not-learned.md) — interesting contrast, but too present-day and KB-specific to be a useful direct link from this source; it would read as "future learning systems differ from today's runtimes," which is true but too obvious
- [context-engineering](kb/notes/context-engineering.md) — real overlap exists, but [in-context-learning-presupposes-context-engineering](kb/notes/in-context-learning-presupposes-context-engineering.md) captures the specific connection more cleanly
- [trace-derived-learning-techniques-in-related-systems](kb/notes/trace-derived-learning-techniques-in-related-systems.md) — high semantic similarity because both discuss learning loops, but the note is a taxonomy of implementation substrates rather than a response to the source's thesis
- [learning-is-not-only-about-generality](kb/notes/learning-is-not-only-about-generality.md) — useful background foundation, but too abstract to justify a direct link from this source

## Index Membership

- No strong case for direct index membership — this is a source snapshot, not a note
- If ingested, the resulting analysis belongs primarily in the learning-theory neighborhood, with secondary relevance to computational-model notes through the control-plane analogy

## Synthesis Opportunities

- **Autonomous learning is substrate-relative.** [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md), [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md), and this source imply a higher-order claim not yet named cleanly: "AI systems don't learn" is only true if the system boundary stops at model weights. Once repo artifacts count as part of the adaptive system, present-day agents already exhibit a partial form of autonomous learning.
- **Meta-control may be context engineering generalized beyond prompts.** [in-context-learning-presupposes-context-engineering](kb/notes/in-context-learning-presupposes-context-engineering.md), [context-engineering](kb/notes/context-engineering.md), and this source suggest a broader abstraction: routing/loading/scoping/maintenance may be one instance of a more general meta-control function that also chooses observation, action, and reward channels.
- **Control-plane abstractions recur at multiple levels.** [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md), [context-engineering](kb/notes/context-engineering.md), and this source all use control-plane language for different substrates (repo guidance, prompt assembly, learning-mode arbitration). There may be a real shared structure, but it is not yet articulated well enough to link directly.

## Flags

- Tension: [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) vs source — disagreement over whether deployed AI already learns depends on whether the system boundary includes artifacts
- Tension: [llm-learning-phases-fall-between-human-learning-modes](kb/notes/llm-learning-phases-fall-between-human-learning-modes.md) vs source — disagreement over how literally cognitive-science learning analogies should guide AI architecture
