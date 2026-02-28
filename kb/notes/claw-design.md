---
description: Index of notes about claw architecture, operations, and evaluation — how claws are built, installed, operated, and assessed
type: index
status: current
---

# Claw design

How claws are built, installed, operated, and evaluated. Architecture decisions, skill design, and the evaluation loop for the knowledge system itself. For document structure and types, see [document-system](./document-system.md). For the learning theory claws draw on, see [learning-theory](./learning-theory.md).

## Architecture

- [files-not-database](./files-not-database.md) — files with git beat a database for agent KBs: universal interface, free versioning, zero infrastructure; derived indexes solve scale without replacing the source of truth
- [commonplace-architecture](./commonplace-architecture.md) — the commonplace repo structure: kb/, skills/, scripts/, and how they compose
- [commonplace-installation-architecture](../commonplace-installation-architecture.md) — how commonplace installs into projects: symlinks, CLAUDE.md generation, directory layout
- [context-loading-strategy](./context-loading-strategy.md) — CLAUDE.md should be a slim router, not a manual; match instruction specificity to loading frequency
- [scenario-decomposition-drives-architecture](./scenario-decomposition-drives-architecture.md) — deriving architectural requirements from concrete user stories decomposed into step-by-step context needs; confirms the loading hierarchy
- [scenarios](./scenarios.md) — concrete use cases the knowledge system must serve
- [generate-instructions-at-build-time](./generate-instructions-at-build-time.md) — generate CLAUDE.md and routing tables at build time rather than maintaining them by hand
- [extract-kb-as-standalone-project](./extract-kb-as-standalone-project.md) — extracting the KB framework as a reusable project
- [indirection-is-costly-in-llm-instructions](./indirection-is-costly-in-llm-instructions.md) — in LLM instructions, every layer of indirection costs context and interpretation overhead on every read, unlike code where indirection is nearly free at runtime

## Skills & Methodology

- [agent-statelessness-makes-skill-layers-architectural-not-pedagogical](./agent-statelessness-makes-skill-layers-architectural-not-pedagogical.md) — the methodology-to-skill relationship is permanent infrastructure for LLM agents, not a learning progression; lossy compilation creates systematic blind spots
- [skills-derive-from-methodology-through-distillation](./skills-derive-from-methodology-through-distillation.md) — methodology-to-skill derivation is distillation (extracting procedures from reasoning in the same medium), distinct from crystallisation and stabilisation
- [methodology-enforcement-is-stabilisation](./methodology-enforcement-is-stabilisation.md) — instructions, skills, hooks, and scripts form a stabilisation gradient for methodology; practices start stochastic and harden as they prove out
- [instructions-are-typed-callables](./instructions-are-typed-callables.md) — skills and tasks are typed callables: they accept document types as input and produce types as output, and should declare their signatures
- [design-methodology-borrow-widely-filter-by-first-principles](./design-methodology-borrow-widely-filter-by-first-principles.md) — borrow from software engineering, library science, knowledge management — but filter through first principles before adopting
- [agent-statelessness-means-harness-should-inject-context-automatically](./agent-statelessness-means-harness-should-inject-context-automatically.md) — since agents never internalize, the harness should inject context automatically rather than relying on agent initiative

## Evaluation

- [what-works](./what-works.md) — proven patterns: prose-as-title, template nudges, frontmatter queries, discovery-first
- [what-doesnt-work](./what-doesnt-work.md) — anti-patterns and insufficient evidence: auto-commits, queue overhead
- [needs-testing](./needs-testing.md) — promising but unconfirmed: extract/connect/review cycle, input classification
- [what-cludebot-teaches-us](./what-cludebot-teaches-us.md) — techniques from cludebot worth borrowing, what we already cover, and what to watch for at scale

## Gaps

- [automating-kb-learning-is-an-open-problem](./automating-kb-learning-is-an-open-problem.md) — the KB already learns through manual human+agent work; the open problem is automating the judgment-heavy mutations (connections, groupings, synthesis)
- [claw-learning-is-broader-than-retrieval](./claw-learning-is-broader-than-retrieval.md) — a claw's learning must improve action capacity (classification, planning, communication), not just retrieval; needs different knowledge types and evaluation criteria
- [quality-signals-for-kb-evaluation](./quality-signals-for-kb-evaluation.md) — proposes a composite oracle from graph-topology, content-proxy, and LLM-hybrid signals to address the learning loop's quality gates problem
- [notes-need-quality-scores-to-scale-curation](./notes-need-quality-scores-to-scale-curation.md) — as the KB grows, /connect retrieves too many candidates; composite note scores filter and rank before agent evaluation
- [a-functioning-claw-needs-a-workshop-layer-not-just-a-library](./a-functioning-claw-needs-a-workshop-layer-not-just-a-library.md) — the library type system models durable knowledge but not work-in-motion with state machines, dependencies, and expiration
- [deep-search-is-connection-methodology-applied-to-temporarily-expanded-corpus](./deep-search-is-connection-methodology-applied-to-temporarily-expanded-corpus.md) — /connect's dual discovery and articulation testing are corpus-agnostic, so deep search means temporarily expanding the corpus with web results

## Decisions

- [001-generate-topic-links-from-frontmatter](./001-generate-topic-links-from-frontmatter.md) — replace LLM-generated Topics footers with deterministic script

## Reference material

- [Toulmin argument](../sources/purdue-owl-toulmin-argument.md) — formal argumentation model (claim/grounds/warrant/qualifier/rebuttal/backing) that grounds claim-title conventions and the `structured-claim` type
- [Agentic Note-Taking 23: Notes Without Reasons](../sources/agentic-note-taking-23-notes-without-reasons-2026894188516696435.working.md) — practitioner validation of propositional links over embedding-based adjacency; confirms the Goodhart risk in quality signals

## Related Areas

- [document-system](./document-system.md) — types, writing conventions, and validation that the claw's documents follow
- [learning-theory](./learning-theory.md) — the learning mechanisms (stabilisation, crystallisation, distillation) that claw operations instantiate
- [links](./links.md) — linking methodology, navigation, and link contracts
- [related-systems](./related-systems/related-systems-index.md) — external system comparisons
