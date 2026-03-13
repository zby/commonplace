---
description: Index of notes about agent-operated KB architecture, operations, and evaluation — how agent-operated knowledge bases are built, installed, and assessed
type: index
status: current
---

# KB design

How agent-operated knowledge bases are built, installed, and evaluated. Architecture decisions, skill design, and the evaluation loop for the knowledge system itself. For document structure and types, see [document-system](./document-system-index.md). For the learning theory knowledge bases draw on, see [learning-theory](./learning-theory-index.md).

## Architecture

- [context-efficiency-is-the-central-design-concern-in-agent-systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — context is the scarce resource in agent systems; context cost has two dimensions (volume and complexity) and nearly every architectural pattern is a response to one or both
- [areas-exist-because-useful-operations-require-reading-notes-together](./areas-exist-because-useful-operations-require-reading-notes-together.md) — areas are operational scopes for orientation and comparative reading; boundaries should optimize yield-per-context, not taxonomy
- [files-not-database](./files-not-database.md) — files with git beat a database for agent KBs: universal interface, free versioning, zero infrastructure; derived indexes solve scale without replacing the source of truth
- [commonplace-architecture](./commonplace-architecture.md) — the commonplace repo structure: kb/, scripts/, and how they compose
- [commonplace-installation-architecture](./commonplace-installation-architecture.md) — how commonplace installs into projects: symlinks, CLAUDE.md generation, directory layout
- [agents-md-should-be-organized-as-a-control-plane](./agents-md-should-be-organized-as-a-control-plane.md) — theory for AGENTS.md as a control plane: invariants, routing, escalation boundaries, nested topology, and exclusion rules
- [instruction-specificity-should-match-loading-frequency](./instruction-specificity-should-match-loading-frequency.md) — CLAUDE.md should be a slim router, not a manual; match instruction specificity to loading frequency
- [scenario-decomposition-drives-architecture](./scenario-decomposition-drives-architecture.md) — deriving architectural requirements from concrete user stories decomposed into step-by-step context needs; confirms the loading hierarchy
- [scenarios](./scenarios.md) — concrete use cases the knowledge system must serve
- [generate-instructions-at-build-time](./generate-instructions-at-build-time.md) — generate CLAUDE.md and routing tables at build time rather than maintaining them by hand
- [indirection-is-costly-in-llm-instructions](./indirection-is-costly-in-llm-instructions.md) — in LLM instructions, every layer of indirection costs context and interpretation overhead on every read, unlike code where indirection is nearly free at runtime
- [frontloading spares execution context](./frontloading-spares-execution-context.md) — pre-compute static parts of instructions and insert results; the mechanism is partial evaluation; indirection elimination and build-time generation are specific cases
- [injectable configuration extends frontloading to installation-specific values](./injectable-configuration-extends-frontloading-to-installation-specific-values.md) — values static per-installation but variable across installations (sibling repo paths, local tools) are frontloadable through config the orchestrator injects into sub-agent frames

## Skills & Methodology

- [agent-statelessness-makes-routing-architectural-not-learned](./agent-statelessness-makes-routing-architectural-not-learned.md) — all knowledge routing infrastructure (skills, type templates, routing tables, naming conventions) is permanent architecture for LLM agents, not scaffolding that learners outgrow
- [capability-placement-should-follow-autonomy-readiness](./capability-placement-should-follow-autonomy-readiness.md) — capabilities belong in skills only when autonomy-ready; otherwise keep them in instructions or methodology artifacts, not AGENTS inventories
- [skills-derive-from-methodology-through-distillation](./skills-derive-from-methodology-through-distillation.md) — methodology-to-skill derivation is distillation (extracting procedures from reasoning in the same medium), distinct from codification and constraining
- [methodology-enforcement-is-constraining](./methodology-enforcement-is-constraining.md) — instructions, skills, hooks, and scripts form a constraining gradient for methodology; practices start stochastic and harden as they prove out
- [instructions-are-typed-callables](./instructions-are-typed-callables.md) — skills and tasks are typed callables: they accept document types as input and produce types as output, and should declare their signatures
- [ad-hoc-prompts-extend-the-system-without-schema-changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — the other end of the spectrum: ad hoc instructions notes absorb new requirements without any schema change; the collections problem is a concrete example
- [design-methodology-borrow-widely-filter-by-first-principles](./design-methodology-borrow-widely-filter-by-first-principles.md) — borrow from software engineering, library science, knowledge management — but filter through first principles before adopting
- [agent-statelessness-means-harness-should-inject-context-automatically](./agent-statelessness-means-harness-should-inject-context-automatically.md) — since agents never internalize, the harness should inject context automatically rather than relying on agent initiative
- [instructions-are-skills-without-automatic-routing](./instructions-are-skills-without-automatic-routing.md) — reusable distilled procedures in kb/instructions/ — same format as skills but without activation triggers; invoked when a human points the agent at them
- [distillation-status-determines-directory-placement](./distillation-status-determines-directory-placement.md) — (seedling) hunch that procedural artifacts distilled for execution belong in kb/instructions/; the boundary is "distilled into a procedure", not just "compressed"

## Evaluation

- [what-works](./what-works.md) — proven patterns: prose-as-title, template nudges, frontmatter queries, discovery-first
- [what-doesnt-work](./what-doesnt-work.md) — anti-patterns and insufficient evidence: auto-commits, queue overhead
- [needs-testing](./needs-testing.md) — promising but unconfirmed: extract/connect/review cycle, input classification
- [what-cludebot-teaches-us](./what-cludebot-teaches-us.md) — techniques from cludebot worth borrowing, what we already cover, and what to watch for at scale
- [prompt-ablation-converts-human-insight-to-deployable-framing](./prompt-ablation-converts-human-insight-to-deployable-framing.md) — methodology for testing prompt framings: vary only the framing against a known-correct target, analyze mechanisms, deploy the winner as instruction

## Design Principles

- [a good agentic KB maximizes contextual competence through discoverable, composable, trustworthy knowledge](./a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — unifying theory: three properties (discoverable, composable, trustworthy) serve contextual competence under bounded context; three learning operations (constraining, distillation, discovery) improve them; Deutsch's reach criterion measures knowledge quality
- [a-knowledge-base-should-support-fluid-resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — good thinking requires moving between abstraction levels; KB quality should be measured by how fluidly it supports this resolution-switching, not just retrieval accuracy
- [mechanistic constraints make Popperian KB recommendations actionable](./mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — bridges Popperian conjecture-and-refutation with bounded-context mechanics and proposes concrete upgrades (falsifiers, contradiction passes, oracle-aware hardening)
- [Alexander's patterns connect to knowledge system design at multiple levels](./alexander-patterns-and-knowledge-system-design.md) — (speculative) pattern language as document types, generative processes as codification, centers as mutual reinforcement in the note graph

## Workshop Layer

- [a-functioning-kb-needs-a-workshop-layer-not-just-a-library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — the library type system models durable knowledge but not work-in-motion with state machines, dependencies, and expiration
- [active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes](./active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes.md) — working understanding during an active campaign needs holistic rewrite, not graph composition; theorist exemplifies this as a workshop artifact

- [vibe-noting](./vibe-noting.md) — (seedling) vibe coding works because code is inspectable, not just verifiable; a KB adds that same inspectability to knowledge work, enabling a similar flywheel for reasoning

## Gaps

- [automating-kb-learning-is-an-open-problem](./automating-kb-learning-is-an-open-problem.md) — the KB already learns through manual human+agent work; the open problem is automating the judgment-heavy mutations (connections, groupings, synthesis)
- [claw-learning-is-broader-than-retrieval](./claw-learning-is-broader-than-retrieval.md) — a Claw's learning must improve action capacity (classification, planning, communication), not just retrieval; needs different knowledge types and evaluation criteria
- [deep-search-is-connection-methodology-applied-to-temporarily-expanded-corpus](./deep-search-is-connection-methodology-applied-to-temporarily-expanded-corpus.md) — /connect's dual discovery and articulation testing are corpus-agnostic, so deep search means temporarily expanding the corpus with web results

## Decisions

- [001-generate-topic-links-from-frontmatter](./001-generate-topic-links-from-frontmatter.md) — replace LLM-generated Topics footers with deterministic script

## Reference material

- [Toulmin argument](../sources/purdue-owl-toulmin-argument.md) — formal argumentation model (claim/grounds/warrant/qualifier/rebuttal/backing) that grounds claim-title conventions and the `structured-claim` type
- [Agentic Note-Taking 23: Notes Without Reasons](../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.md) — practitioner validation of propositional links over embedding-based adjacency; confirms the Goodhart risk in quality signals
- [A-MEM: Agentic Memory for LLM Agents](../sources/a-mem-agentic-memory-for-llm-agents.md) — academic paper implementing Zettelkasten-inspired automated memory with link generation and memory evolution; provides empirical evidence for boiling cauldron mutations and scaling data for embedding-based linking
- [Context Engineering for AI Agents in OSS](../sources/context-engineering-ai-agents-oss.md) — empirical study of AGENTS.md/CLAUDE.md adoption in 466 OSS projects; validates the loading-frequency principle's content categories, provides evolution data showing constraining maturation in the wild, and confirms the dual-audience split between human READMEs and machine context files

## Related Tags

- [document-system](./document-system-index.md) — types, writing conventions, and validation that the KB's documents follow
- [learning-theory](./learning-theory-index.md) — the learning mechanisms (constraining, codification, distillation) that KB operations instantiate
- [computational-model](./computational-model-index.md) — PL concepts (scheduling, partial evaluation, scoping) that inform KB architecture; the scheduling notes moved here
- [links](./links-index.md) — linking methodology, navigation, and link contracts
- [maintenance](./kb-maintenance-index.md) — detection, operations, and dynamics that keep the KB healthy over time
- [related-systems](./related-systems/related-systems-index.md) — external system comparisons

## All notes <!-- generated -->

- [004-Replace areas with tags](./adr/004-replace-areas-with-tags.md) — Replaces the areas frontmatter field with freeform tags and restructures index pages to have both curated and generated sections, decoupling navigation from comparative reading
- [A functioning knowledge base needs a workshop layer, not just a library](./a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — The current type system models permanent knowledge (library) but not in-flight work with state machines, dependencies, and expiration (workshop) — tasks are a prototype of the missing layer, and a functioning knowledge base needs both plus bridges between them
- [A good agentic KB maximizes contextual competence through discoverable, composable, trustworthy knowledge](./a-good-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trustworthy-knowledge.md) — Theory of why commonplace's arrangements work — three properties (discoverable, composable, trustworthy) serve contextual competence under bounded context; accumulation is the basic learning operation (reach distinguishes facts from theories); constraining, distillation, and discovery transform accumulated knowledge; Deutsch's reach criterion distinguishes knowledge that transfers from knowledge that merely fits
- [A knowledge base should support fluid resolution-switching](./a-knowledge-base-should-support-fluid-resolution-switching.md) — Good thinking requires moving between abstraction levels — broad for context, narrow for mechanism, back out for pattern. A KB's quality should be measured by how fluidly it supports this resolution-switching, not just retrieval accuracy.
- [Active-campaign understanding needs a single coherent narrative, not composed notes](./active-campaign-understanding-needs-a-single-coherent-narrative-not-composed-notes.md) — Why durable-knowledge graph composition (many linked notes) is wrong for tracking understanding during active engineering — a single holistically rewritten narrative maintains the coherence that working memory requires
- [Ad hoc prompts extend the system without schema changes](./ad-hoc-prompts-extend-the-system-without-schema-changes.md) — When a new requirement doesn't fit existing types or skills, writing an ad hoc instructions note absorbs it without any schema change — the collections problem is a concrete example
- [Agent statelessness makes routing architectural, not learned](./agent-statelessness-makes-routing-architectural-not-learned.md) — Agents never develop navigation intuition — every session is day one — so all knowledge routing infrastructure (skills, type templates, routing tables, naming conventions, activation triggers) is permanent architecture, not scaffolding that learners outgrow
- [Agent statelessness means the harness should inject context automatically](./agent-statelessness-means-harness-should-inject-context-automatically.md) — Since agents can't carry vocabulary or decisions between reads, the harness should auto-inject referenced context — definitions once per session, ADRs when relevant. The trigger mechanism (type, link semantics, term detection) is an open question; the need follows directly from statelessness.
- [AGENTS.md should be organized as a control plane](./agents-md-should-be-organized-as-a-control-plane.md) — Theory for deciding what belongs in AGENTS.md using loading frequency and failure cost, with layers, exclusion rules, and migration paths
- [Alexander's patterns connect to knowledge system design at multiple levels](./alexander-patterns-and-knowledge-system-design.md) — Christopher Alexander's pattern language, generative processes, and centers may connect to our knowledge system design at multiple levels — from structured document types to codification to link semantics. Vague but persistent.
- [Always-loaded context has two surfaces with different affordances](./always-loaded-context-has-two-surfaces-with-different-affordances.md) — CLAUDE.md enforces universal constraints (imperative/push); skill descriptions advertise opt-in capabilities (suggestive/pull) — guidance belongs on whichever surface matches its enforcement model
- [Areas exist because useful operations require reading notes together](./areas-exist-because-useful-operations-require-reading-notes-together.md) — Areas are defined by operations that require reading notes together — orientation and comparative reading — which need sets that are both small enough for context and related enough to yield results
- [Automating KB learning is an open problem](./automating-kb-learning-is-an-open-problem.md) — The KB already learns through manual work (every improvement is capacity change per Simon). The open problem is automating the judgment-heavy mutations — connections, groupings, synthesis — which require oracles we can't yet manufacture.
- [Capability placement should follow autonomy readiness](./capability-placement-should-follow-autonomy-readiness.md) — Capability artifacts should be placed by autonomy readiness so AGENTS.md stays free of inventories and only routes or constrains behavior
- [Claw learning is broader than retrieval](./claw-learning-is-broader-than-retrieval.md) — A Claw's learning loop must improve action capacity (classification, planning, communication), not just retrieval — question-answering is one mode among many
- [Commonplace architecture](./commonplace-architecture.md) — The commonplace repo's own internal layout — what exists, what's missing, and the decision to put global types in CLAUDE.md instead of kb/types/
- [Commonplace installation architecture](./commonplace-installation-architecture.md) — Design for how commonplace installs into a project — two trees (user's kb/ and framework's commonplace/), operational artifacts copied for prompt simplicity, methodology referenced for deeper reasoning
- [Context efficiency is the central design concern in agent systems](./context-efficiency-is-the-central-design-concern-in-agent-systems.md) — Context — not compute, memory, or storage — is the scarce resource in agent systems; context cost has two dimensions (volume and complexity) that require different architectural responses, making context efficiency the central design concern analogous to algorithmic complexity in traditional systems
- [Deep search is connection methodology applied to a temporarily expanded corpus](./deep-search-is-connection-methodology-applied-to-temporarily-expanded-corpus.md) — Design exploration for a deep search skill that reuses /connect's dual discovery and articulation testing on web search results, building a temporary research graph before bridging to KB
- [Design methodology — borrow widely, filter by first principles](./design-methodology-borrow-widely-filter-by-first-principles.md) — We borrow from any source but adopt based on first-principles support — except programming patterns, which get a fast pass because the bet is that knowledge bases are a new kind of software system
- [Distillation status determines directory placement](./distillation-status-determines-directory-placement.md) — Hunch that procedural artifacts distilled for execution belong in kb/instructions/ — the directory boundary is "distilled into a procedure", not "compressed" or "frequently loaded"
- [Enforcement without structured recovery is incomplete](./enforcement-without-structured-recovery-is-incomplete.md) — The enforcement gradient covers detection and blocking but has no recovery column — recovery strategies (corrective → fallback → escalation) are the missing layer, and oracle strength determines which are viable at each level
- [Files beat a database for agent-operated knowledge bases](./files-not-database.md) — Files beat a database early on — a schema commits to access patterns before you know them, and files let you constrain incrementally while getting free browsing, versioning, and agent access from day one
- [Frontloading spares execution context](./frontloading-spares-execution-context.md) — Pre-computing static parts of LLM instructions and inserting results spares execution context — the primary bottleneck in instructing LLMs; the mechanism is partial evaluation applied to instructions with underspecified semantics
- [Generate KB skills at build time, don't parameterise them](./generate-instructions-at-build-time.md) — KB skills should be generated from templates at setup time, not parameterised with runtime variables — applying the general principle that indirection is costly in LLM instructions
- [Indirection is costly in LLM instructions](./indirection-is-costly-in-llm-instructions.md) — In code, indirection (variables, config, abstraction layers) is nearly free at runtime — in LLM instructions, every layer of indirection costs context and interpretation overhead on every read
- [Injectable configuration extends frontloading to installation-specific values](./injectable-configuration-extends-frontloading-to-installation-specific-values.md) — Values static within an installation but variable across installations — sibling repo paths, local tool locations — are frontloadable through configuration the orchestrator resolves and injects into sub-agent frames; the context savings depend on sub-agent isolation since injection into the main context just adds tokens
- [Instruction specificity should match loading frequency](./instruction-specificity-should-match-loading-frequency.md) — The loading hierarchy (CLAUDE.md → skill descriptions → skill bodies → task docs) should match instruction specificity to loading frequency — always-loaded context competes for attention every session
- [Instructions are skills without automatic routing](./instructions-are-skills-without-automatic-routing.md) — Reusable distilled procedures that live in kb/instructions/ — same format as skills but without activation triggers or CLAUDE.md routing entries; invoked when a human points the agent at them
- [Instructions are typed callables with document type signatures](./instructions-are-typed-callables.md) — Skills and tasks are typed callables — they accept document types as input and produce types as output, and should declare their signatures like functions declare parameter types.
- [MCP bundles stateless tools with a stateful runtime](./mcp-bundles-stateless-tools-with-stateful-runtime.md) — MCP forces stateless tool operations through a persistent server process — most tools are pure functions that don't need session state, connections, or lifecycle management, but pay the complexity tax anyway
- [Mechanistic constraints make Popperian KB recommendations actionable](./mechanistic-constraints-make-popperian-kb-recommendations-actionable.md) — Bounded context and underspecification don't just permit conjecture-and-refutation — they require it; derives three concrete practices (falsifier blocks, contradiction-first connection, rejected-interpretation capture) from KB mechanics.
- [Methodology enforcement is constraining](./methodology-enforcement-is-constraining.md) — Instructions, skills, hooks, and scripts form a constraining gradient for methodology — from underspecified and indeterministic (LLM interprets and may not follow) to fully deterministic (code always runs), with hooks occupying a middle ground of deterministic triggers with indeterministic responses
- [Needs testing](./needs-testing.md) — Promising ideas without enough evidence — extract/connect/review cycle, input classification before processing
- [Prompt ablation converts human insight into deployable agent framing](./prompt-ablation-converts-human-insight-to-deployable-framing.md) — Methodology for testing prompt framings — uses controlled variation against a human-verified finding to identify which cognitive moves agents can reliably execute, then deploys the winning framing as instruction
- [Scenario decomposition drives architecture](./scenario-decomposition-drives-architecture.md) — Deriving architectural requirements by decomposing concrete user stories into step-by-step context needs — not from abstract read/write operations but from what the agent actually has to load at each stage, in both the commonplace repo and installed projects
- [Scenarios](./scenarios.md) — Concrete use cases for the knowledge system — upstream change analysis and proposing our own changes
- [Skills derive from methodology through distillation](./skills-derive-from-methodology-through-distillation.md) — The methodology→skill relationship is distillation (extracting operational procedures from discursive reasoning in the same medium) — distinct from codification (prompt→code phase transition) and constraining (narrowing output distribution)
- [The fundamental split in agent memory is not storage format but who decides what to remember](./related-systems/agentic-memory-systems-comparative-review.md) — Comparative analysis of eleven agent memory systems across six architectural dimensions — storage unit, agency model, link structure, temporal model, curation operations, and extraction schema — revealing that the agency question (who decides what to remember) is the most consequential design choice and that no system combines high agency, high throughput, and high curation quality.
- [Two context boundaries govern collection operations](./two-context-boundaries-govern-collection-operations.md) — Any note collection faces two context boundaries — a full-text boundary where all bodies can be loaded together, and an index boundary where all titles+descriptions fit — creating three operational regimes that govern areas, /connect, and whole-KB operations differently
- [Vibe-noting](./vibe-noting.md) — Vibe coding works because code is inspectable, not just verifiable — a KB adds that same inspectability to knowledge work, enabling augmentation even where automation is blocked on oracle construction
- [What cludebot teaches us](./what-cludebot-teaches-us.md) — Techniques from cludebot worth borrowing — what we already cover, what to adopt now, and what to watch for as the KB grows
- [What doesn't work](./what-doesnt-work.md) — Anti-patterns and areas with insufficient evidence — auto-commits, queue overhead, validation ceremony, session rhythm
- [What works](./what-works.md) — Patterns proven valuable in practice — prose-as-title, template nudges, frontmatter queries, semantic search via qmd, discovery-first, public/internal boundary
