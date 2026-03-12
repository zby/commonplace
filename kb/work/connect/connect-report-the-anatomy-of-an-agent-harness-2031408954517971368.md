# Connection Report: The Anatomy of an Agent Harness

**Source:** [The Anatomy of an Agent Harness](kb/sources/the-anatomy-of-an-agent-harness-2031408954517971368.md)
**Date:** 2026-03-10
**Depth:** standard

## Discovery Trace

**Index scan:**
- Read kb/notes/index.md — scanned all 144 entries. Flagged candidates:
  - [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — "context rot" and "compaction" appear in both
  - [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) — harness components (instructions, skills, hooks, scripts) match the constraining gradient
  - [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — memory via filesystem/git is deploy-time learning
  - [agent-statelessness-means-harness-should-inject-context-automatically](kb/notes/agent-statelessness-means-harness-should-inject-context-automatically.md) — harness context injection
  - [unified-calling-conventions-enable-bidirectional-refactoring](kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md) — model/harness boundary and llm-do harness layer
  - [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — filesystem + git as inspectable substrate
  - [bounded-context-orchestration-model](kb/notes/bounded-context-orchestration-model.md) — orchestration logic is a harness component
  - [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](kb/notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — compaction is a harness recovery strategy
  - [files-not-database](kb/notes/files-not-database.md) — filesystem as foundational harness primitive
  - [entropy-management-must-scale-with-generation-throughput](kb/notes/entropy-management-must-scale-with-generation-throughput.md) — background cleanup agents are a harness feature
  - [codification-and-relaxing-navigate-the-bitter-lesson-boundary](kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — model/harness co-evolution maps to codify/relax
  - [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md) — AGENTS.md memory files are harness-mediated learning
  - [related-systems/agent-skills-for-context-engineering](kb/notes/related-systems/agent-skills-for-context-engineering.md) — progressive disclosure, filesystem-first, context engineering overlap
  - [related-systems/spacebot](kb/notes/related-systems/spacebot.md) — typed process architecture as clean scheduler, a harness implementation

**Topic indexes:**
- Read [kb-design](kb/notes/kb-design.md) — confirmed candidates above; additionally flagged:
  - [context-loading-strategy](kb/notes/context-loading-strategy.md) — CLAUDE.md as router relates to AGENTS.md harness pattern
  - [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md) — AGENTS.md architecture is harness design

**Semantic search:** (via qmd)
- query "agent harness model boundary context engineering tools orchestration" on notes — top hits:
  - kb/notes/index.md (91%) — index, not a connection target
  - [agent-skills-for-context-engineering](kb/notes/related-systems/agent-skills-for-context-engineering.md) (56%) — strong, covers same harness concepts
  - [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](kb/notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) (46%) — compaction as harness recovery
  - [unified-calling-conventions-enable-bidirectional-refactoring](kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md) (46%) — harness layer section directly relevant
  - [research/adaptation-agentic-ai-analysis](kb/notes/research/adaptation-agentic-ai-analysis.md) (44%) — mapped harness signals to constrain/relax; evaluated below
  - [frontloading-spares-execution-context](kb/notes/frontloading-spares-execution-context.md) (44%) — context optimization is a harness technique
  - [spacebot](kb/notes/related-systems/spacebot.md) (44%) — typed process harness implementation
  - [bounded-context-orchestration-model](kb/notes/bounded-context-orchestration-model.md) (35%) — orchestration as harness component
  - [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) (35%) — already flagged
- query same on sources — top hits:
  - [harness-engineering-leveraging-codex-agent-first-world.ingest.md](kb/sources/harness-engineering-leveraging-codex-agent-first-world.ingest.md) (56%) — companion harness engineering source
  - [harness-engineering-is-cybernetics-2030416758138634583](kb/sources/harness-engineering-is-cybernetics-2030416758138634583.md) (45%) — companion cybernetics framing
  - [context-engineering-ai-agents-oss-ingest.md](kb/sources/context-engineering-ai-agents-oss-ingest.md) (43%) — empirical study of AGENTS.md evolution

**Keyword search:**
- grep "harness" in kb/notes/ — 25 files; confirmed all index scan candidates; no new candidates beyond those already flagged
- grep "harness" in kb/sources/ — 13 files; confirmed companion sources
- grep "Ralph Loop|context rot|compaction" — found in bounded-context-orchestration-model, llm-mediated-schedulers, spacebot, context-efficiency (already flagged)
- grep "progressive disclosure" — 31 files; confirmed agent-skills-for-context-engineering and context-loading-strategy (already flagged)

## Connections Found

### Source-to-source connections

- [Harness Engineering: Leveraging Codex in an Agent-First World](kb/sources/harness-engineering-leveraging-codex-agent-first-world.md) — **extends**: Lopopolo's practitioner report on 1M LOC defines harness engineering from the implementation side (constrain/inform/verify/correct); this Vtrivedy10 thread provides the taxonomy of harness components and derives each from model limitations. The two together give practice + anatomy for the same phenomenon.

- [Harness Engineering Is Cybernetics](kb/sources/harness-engineering-is-cybernetics-2030416758138634583.md) — **extends**: The cybernetics thread frames harness engineering as control-loop design (sensors, actuators, feedback loops); this thread provides the component-by-component derivation of what those control loops operate on. The cybernetics source is theory; this source is taxonomy.

### Source-to-note connections

- [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) — **exemplifies**: The source's "Battling Context Rot" section (compaction, tool call offloading, progressive skill disclosure) independently names context as the scarce resource and derives harness features to manage it. The note already cites the Lopopolo companion source; this source adds the component taxonomy that shows why context management is a harness-level concern, not a model-level one.

- [methodology-enforcement-is-constraining](kb/notes/methodology-enforcement-is-constraining.md) — **exemplifies**: The source's harness components (system prompts, tools, hooks/middleware, orchestration logic) map directly onto the note's constraining gradient (instruction -> skill -> hook -> script). The source's "Hooks/Middleware for deterministic execution (compaction, continuation, lint checks)" is the note's hooks layer described in practitioner language.

- [deploy-time-learning-the-missing-middle](kb/notes/deploy-time-learning-the-missing-middle.md) — **exemplifies**: The source's memory section describes AGENTS.md files that persist knowledge across sessions and get injected on agent start — this is deploy-time learning through repo artifacts. The source's "continual learning" framing matches Simon's definition: each AGENTS.md edit changes the system's capacity without weight updates.

- [agent-statelessness-means-harness-should-inject-context-automatically](kb/notes/agent-statelessness-means-harness-should-inject-context-automatically.md) — **exemplifies**: The source explicitly describes harness-side memory file injection: "Harnesses support memory file standards like AGENTS.md which get injected into context on agent start." This is the note's "on reference" injection layer described as a concrete harness primitive. The source also extends the note's scope by describing web search and MCP tools as additional injection mechanisms for real-time knowledge.

- [bounded-context-orchestration-model](kb/notes/bounded-context-orchestration-model.md) — **exemplifies** (target is seedling): The source's "Orchestration Logic (subagent spawning, handoffs, model routing)" is a harness-level implementation of the note's symbolic scheduler. The source's derivation — models can't maintain state or execute code, so the harness must — is a practitioner restatement of why the scheduler must be symbolic. The Ralph Loop pattern (hook intercepts model exit, reinjects prompt in clean context) is a concrete instance of the select/call/absorb loop.

- [llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model](kb/notes/llm-mediated-schedulers-are-a-degraded-variant-of-the-clean-model.md) — **exemplifies** (target is seedling): The source's compaction harness feature ("intelligently offloads and summarizes the existing context window so the agent can continue working") is the note's first recovery strategy (compaction) described as a concrete harness component. The Ralph Loop's clean context reinsertion is the note's externalisation strategy in action.

- [unified-calling-conventions-enable-bidirectional-refactoring](kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md) — **exemplifies**: The source's "The Coupling of Model Training and Harness Design" section describes how useful primitives discovered in harnesses get baked into model training, creating a co-evolution loop. The note's llm-do harness (imperative Python owning control flow, with agents and tools in a shared namespace) is an alternative harness architecture. The source's observation that changing tool logic degrades performance (apply_patch example) is evidence for why unified calling conventions matter — they reduce the coupling between model training and harness structure.

- [codification-and-relaxing-navigate-the-bitter-lesson-boundary](kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — **exemplifies**: The source's "The Coupling of Model Training and Harness Design" describes the codify/relax dynamic in practitioner terms: harness features codify model behaviors into deterministic code, but "as models get more capable, some of what lives in the harness today will get absorbed into the model" — that absorption is relaxing. The co-training feedback loop is the mechanism by which the boundary moves.

- [inspectable-substrate-not-supervision-defeats-the-blackbox-problem](kb/notes/inspectable-substrate-not-supervision-defeats-the-blackbox-problem.md) — **exemplifies**: The source's filesystem + git harness primitives ("Agents get a workspace to read data, code, and documentation... Git adds versioning so agents can track work, rollback errors, and branch experiments") is the inspectable substrate thesis described as foundational harness architecture. The source makes the substrate the first harness primitive derived from model limitations.

- [files-not-database](kb/notes/files-not-database.md) — **exemplifies**: The source argues filesystem is "the most foundational harness primitive" because it unlocks workspace, incremental offloading, cross-session persistence, and multi-agent collaboration. This is independent practitioner convergence on the note's core claim, arriving from a different direction (harness component derivation vs KB architecture).

- [entropy-management-must-scale-with-generation-throughput](kb/notes/entropy-management-must-scale-with-generation-throughput.md) — **extends** (target is seedling): The source discusses the co-evolution of model training and harness design, where each generation's harness primitives inform next-generation training. This creates a compound entropy management challenge: not only must cleanup match generation throughput (the note's claim), but the harness itself evolves, potentially invalidating existing cleanup patterns. The Terminal Bench example (Opus 4.6 scoring differently across harnesses) shows that harness-level changes can shift the entire quality landscape.

- [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md) — **exemplifies**: The source's memory section describes AGENTS.md as a "form of continual learning where agents durably store knowledge from one session and inject that knowledge into future sessions" — the note's exact claim stated in harness engineering vocabulary. The source adds the harness framing: this learning happens because the harness manages the memory file lifecycle (load, update, persist).

**Bidirectional candidates** (reverse link also worth adding):

- [context-efficiency-is-the-central-design-concern-in-agent-systems](kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) <-> source — the note already cites the Lopopolo companion source; this source provides the component taxonomy showing that context management is a cross-cutting harness concern (compaction, tool call offloading, skill progressive disclosure, memory injection), not just a single architectural pattern.

- [unified-calling-conventions-enable-bidirectional-refactoring](kb/notes/unified-calling-conventions-enable-bidirectional-refactoring.md) <-> source — the note's harness layer section describes llm-do's imperative harness as a contrast to graph DSLs; this source provides the industry-standard harness component taxonomy that the note's alternative harness design should be evaluated against.

## Rejected Candidates

- [related-systems/agent-skills-for-context-engineering](kb/notes/related-systems/agent-skills-for-context-engineering.md) — While this note covers context engineering and progressive disclosure, it reviews a specific skill collection. The connection would be "both discuss context engineering," which is too broad to be useful. The note already connects to the KB's context-efficiency and context-loading-strategy notes which are the specific conceptual bridges.

- [related-systems/spacebot](kb/notes/related-systems/spacebot.md) — Spacebot implements a typed process architecture (clean scheduler), which relates to the source's orchestration logic. But the connection is at the level of "both discuss agent orchestration" — too generic. The bounded-context-orchestration-model note already captures the conceptual bridge.

- [frontloading-spares-execution-context](kb/notes/frontloading-spares-execution-context.md) — The source mentions no pre-computation or partial evaluation concepts. The connection would be indirect through context efficiency, already covered.

- [agents-md-should-be-organized-as-a-control-plane](kb/notes/agents-md-should-be-organized-as-a-control-plane.md) — The source mentions system prompts as a harness component, but does not discuss how to structure them. The connection would be "both mention AGENTS.md" — surface vocabulary overlap without semantic depth.

- [context-loading-strategy](kb/notes/context-loading-strategy.md) — Same reasoning as above. The source mentions context management but does not discuss loading hierarchies or router vs manual distinction.

- [research/adaptation-agentic-ai-analysis](kb/notes/research/adaptation-agentic-ai-analysis.md) — The adaptation taxonomy maps agent/tool signals to constrain/relax, which relates to the source's harness components. But the connection is indirect: the adaptation paper is about classifying observed signals, while the source is about designing harness components. The mapping would require an intermediate note to be useful.

## Index Membership

- [kb-design](kb/notes/kb-design.md) — This source provides a practitioner taxonomy of harness components that the KB's architecture notes describe in theory. It should appear in the Reference Material section alongside the existing Lopopolo and cybernetics sources.
- [learning-theory](kb/notes/learning-theory.md) — The source's memory/search section and co-training loop are concrete evidence for deploy-time learning and the constrain/relax cycle. Worth adding to Reference Material.
- [computational-model](kb/notes/computational-model.md) — The source's orchestration logic (subagent spawning, handoffs, model routing) and compaction patterns relate to the bounded-context orchestration notes. Could appear in Reference Material.

## Synthesis Opportunities

**Harness component taxonomy as a map of KB concepts.** The source derives harness components from model limitations: filesystem (durable storage), bash (general-purpose execution), sandboxes (safe environments), memory/search (continual learning), context management (compaction, progressive disclosure), long-horizon execution (Ralph Loops, planning, git). Each of these maps onto one or more KB notes. The KB has the theories (context efficiency, constraining, deploy-time learning, codify/relax) but has not yet produced a note that explicitly maps harness component categories to theoretical concepts. Such a note would argue that the practitioner taxonomy and the KB's theoretical framework describe the same phenomena from different angles, using the convergence across three independent sources (Vtrivedy10, Lopopolo, cybernetics thread) as evidence.

**Model-harness co-evolution as a concrete instance of codify/relax.** The source's "Coupling of Model Training and Harness Design" section describes a feedback loop where harness primitives get baked into model training, then new primitives are discovered and codified, then models absorb them. This is codify/relax operating at the model-training/harness-design boundary rather than at the code/prompt boundary. No existing note names this as an instance of the pattern. The notes [codification-and-relaxing-navigate-the-bitter-lesson-boundary](kb/notes/codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) and [constraining-during-deployment-is-continuous-learning](kb/notes/constraining-during-deployment-is-continuous-learning.md) provide the theoretical grounding; the source provides the practitioner evidence.

## Flags

- No split candidate detected — the source covers many components but makes a single claim (harness = everything not the model) with a unified derivation methodology.
- The source is not yet ingested (no `.ingest.md` file exists). Running `/ingest` would produce a structured analysis, connections, and extractable value evaluation.
