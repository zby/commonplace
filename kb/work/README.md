# Work

Experimental workshop space. Purpose-driven working artifacts that haven't codified into notes yet.

Each workshop is a directory exploring a specific workflow end-to-end: from question through sourcing and extraction to finished notes. The goal is to discover what patterns actually emerge from use, rather than designing structure upfront.

## Active Workshops

- [lineage-mechanisms](./lineage-mechanisms/README.md) — revising lineage mechanisms across sources, generated reports, distillation records, report persistence, and source-to-source/source-to-note relation labels
- [src-architecture-alternatives](./src-architecture-alternatives/README.md) — alternative architectures for `src/commonplace/` from a full code read; active thread is an append-only event log as review-store source of truth with acceptance events that embed their snapshots
- [relocation-move-map-engine](./relocation-move-map-engine/README.md) — collapsing note and directory relocation around one move-map engine for link rewriting, file moves, redirects, and removal of review-store rekeying
- [kb-graph-loader](./kb-graph-loader/README.md) — testing whether validation, generated indexes, docs hooks, and review targeting should share one loaded KB note/graph model
- [epistack-competition](./epistack-competition/README.md) — framework-side pointer to the sibling `epistack-casebooks` repo (FLF competition entry): what it's for and the `backlog-to-commonplace.md` protocol for moving ideas between the two repos
- [agent-note-improvement](./agent-note-improvement/README.md) — testing instructions that help agents improve weak existing notes by comparing an older weak revision against a later accepted revision
- [agent-memory-design](./agent-memory-design/README.md) — continuation workshop for discussing revisions and companion artifacts around `kb/notes/designing-agent-memory-systems.md`
- [bulk-operations](./bulk-operations/README.md) — generalizing deep research, review reruns, connect triage, source refresh, validation sweeps, and corpus migrations into a reusable target-selection, sharding, execution, merge-back, and validation pattern
- [pi-agent-zerostack-comparison](./pi-agent-zerostack-comparison/README.md) — preparing a code-grounded comparison instruction for the two Rust coding-agent CLIs cloned under `related-systems/`
- [vocabulary-governance](./vocabulary-governance/README.md) — deciding how global, collection-local, and type-specific vocabularies should be declared and used by shipped KBs
- [aris-full-trial](./aris-full-trial/README.md) — running a private full-ARIS paper-production trial while keeping only framing and lessons learned in the public KB
- [review-bundle-packing](./review-bundle-packing/README.md) — measuring and deciding whether review prompts must stay bundle-local or may pack multiple bundles into one run
- [validation](./validation/README.md) — making validation a reliable part of the workflow: when, what, and how to validate (hooks, skill upgrades, periodic revalidation)
- [obsidian-affordances](./obsidian-affordances/README.md) — deciding which Obsidian-facing affordances are useful compatibility layers versus representation drift for a repo-native KB
- [philosophy-borrowing](./philosophy-borrowing/README.md) — evaluating Peirce's abduction, Quine's web of belief, speech-act theory, and Carnap's explication as operational borrowings for KB methodology
- [agent-complexity-theory](./agent-complexity-theory/README.md) — formal consequences of the bounded-context orchestration model; candidate theorem sketches for academic collaboration
- [semantic-search-replacement](./semantic-search-replacement/README.md) — evaluating whether to replace qmd as the semantic-search layer, and with what
- [latent-space-generation-without-training](./latent-space-generation-without-training/README.md) — exploring whether embedding-guided novelty-generation papers can become a practical no-large-training workflow
- [review-revise-gated](./review-revise-gated/README.md) — finding review/revise arrangements that reliably produce the manual-edit quality bar, then codifying as reusable instructions
- [auditable-llm-editing](./auditable-llm-editing/README.md) — testing whether sparse, anchored writing state prevents accidental claim drift across repeated LLM editing passes
- [distributing-built-kbs](./distributing-built-kbs/README.md) — downstream counterpart to ADR 021's Commonplace-library shipping model: most hassle-free way to distribute a domain KB someone built, by separating the lightweight consumer path from the authoring machinery
- [lifecycle-management](./lifecycle-management/README.md) — mapping the full artifact life-cycle (intake, promotion, maturation, retirement); the `agent-memory-design` test case landed as a `note + synthesis` trait in `kb/notes/designing-agent-memory-systems.md`
- [derivative-report-uniformity](./derivative-report-uniformity/README.md) — unifying frontmatter, directory structure, and (deliberately fuzzy) validation/staleness across the three source-derived reports: reviews, connect reports, critiques
- [scaffolding-relaxation](./scaffolding-relaxation/README.md) — preserving the unresolved theory question from the Fable/workstream and vertical-agent ingests: which scaffolding recedes with stronger models, and which persists because it supplies state, authority, verification, lifecycle, or context economy
- [condensation-faithfulness-experiment](./condensation-faithfulness-experiment/README.md) — designing an experiment to test whether our condensation methodology (write conventions + gate suite) produces more behaviorally faithful memory than naive auto-summary, using the Faithful Self-Evolvers perturbation protocol
