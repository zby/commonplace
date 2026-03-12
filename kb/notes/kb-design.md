---
description: Index of notes about agent-operated KB architecture, operations, and evaluation — how agent-operated knowledge bases are built, installed, and assessed
type: index
status: current
---

# KB design

How agent-operated knowledge bases are built, installed, and evaluated. Architecture decisions, skill design, and the evaluation loop for the knowledge system itself. For document structure and types, see [document-system](./document-system.md). For the learning theory knowledge bases draw on, see [learning-theory](./learning-theory.md).

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

## Related Areas

- [document-system](./document-system.md) — types, writing conventions, and validation that the KB's documents follow
- [learning-theory](./learning-theory.md) — the learning mechanisms (constraining, codification, distillation) that KB operations instantiate
- [computational-model](./computational-model.md) — PL concepts (scheduling, partial evaluation, scoping) that inform KB architecture; the scheduling notes moved here
- [links](./links.md) — linking methodology, navigation, and link contracts
- [maintenance](./kb-maintenance.md) — detection, operations, and dynamics that keep the KB healthy over time
- [related-systems](./related-systems/related-systems-index.md) — external system comparisons
