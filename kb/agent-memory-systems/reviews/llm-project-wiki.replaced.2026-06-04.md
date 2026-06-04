---
description: "llm-project-wiki review: Claude Code setup prompt that generates an Obsidian project wiki, wiki-first rules, sync script, ingest command, and gap audit"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-03"
---

# llm-project-wiki

> Replaced 2026-06-04. See [llm-project-wiki](./llm-project-wiki.md) for the current review.

llm-project-wiki, by Akash R, is a promptware scaffold for making Claude Code create and maintain an Obsidian wiki for a software project. The repository is intentionally tiny: it contains a README and one setup prompt. The reviewed system is therefore not a runtime package with source modules; it is an instruction artifact that asks Claude Code to generate a project-local vault, wiki maintenance rules, slash commands, and agent-facing lookup policy in the target repository ([README.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/README.md), [SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md)).

**Repository:** https://github.com/akash-r34/llm-project-wiki

**Reviewed commit:** [1fdfba9129a46afd18aa68a83f12d6716ab694c6](https://github.com/akash-r34/llm-project-wiki/commit/1fdfba9129a46afd18aa68a83f12d6716ab694c6)

**Last checked:** 2026-06-03

## Core Ideas

**The product is a bootstrap prompt, not an installed program.** `SETUP_PROMPT.md` tells Claude Code to detect whether an `Obsidian Vault/` exists, then either build a new vault through Phases 0-6 or run an existing-vault gap audit through Phase G ([SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md)). This makes the repository more like an executable procedure in natural language than a library: the durable system appears only after a target-project Claude session follows the prompt.

**The generated wiki has a three-layer contract.** The prompt scaffolds `Sources/`, `Wiki/`, and `Templates/`, with `Sources/` as copied source material, `Wiki/` as LLM-maintained compiled pages, and `Templates/` as page templates ([README.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/README.md), [SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md)). The important design split is raw input versus compiled knowledge: copied project docs and memory are preserved as reference material, while wiki pages are rewritten into navigable entity, concept, decision, overview, status, and reference pages.

**Wiki-first lookup turns the generated wiki into the agent's primary project memory.** The prompt updates `CLAUDE.md` and `GEMINI.md` with a rule that sends future architecture, data-model, component, decision, and project-state questions through `index.md`, semantic lookup, and relevant wiki pages before falling back to memory files or source code ([SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md)). This is the main behavioral-authority move: wiki pages are not just documentation; the generated rules give them precedence in future agent work.

**Context efficiency comes from compilation and stale marking, not retrieval algorithms.** The setup prompt tries to spare future context by making pages contain signatures, schemas, constraints, edge cases, and cross-references, so an agent can answer from the wiki instead of opening raw source. Updates are localized by `git diff`, source-path references, and `status: stale` markers rather than by embeddings, ranking, or a database ([README.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/README.md), [SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md)). The system reduces repeated rereading when the generated wiki is accurate, but it does not provide a token budget, top-k selector, or mechanical context packer.

**Maintenance is prompt-governed and audit-heavy.** The generated `/wiki-ingest` command is specified as a diff-based update path that maps changed files to `Sources/`, finds affected wiki pages, updates only changed sections, resolves open `[gap]` entries, creates new pages for new entities, and logs the ingest. Phase G separately checks infrastructure wiring, source coverage, wiki coverage, link integrity, frontmatter, protocol wiring, and audit logging for an existing vault ([SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md)). The governance model is explicit, but its execution depends on Claude Code following the prompt and generated command text.

**Adoption is deliberately native to the target developer environment.** The prompt uses Obsidian-compatible Markdown, `CLAUDE.md`, optional `GEMINI.md`, Claude Code slash commands, `git diff`, shell sync scripts, and ordinary repo commits ([README.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/README.md), [SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md)). That keeps the memory substrate inspectable and portable, but also means the system's correctness is mostly prompt compliance plus human/git review rather than a tested implementation.

## Artifact analysis

- **Storage substrate:** `repo` — The reviewed repository stores only the bootstrap prompt and README, while the generated memory system stores vault files, command files, scripts, and agent instruction files in the target project repository.
- **Representational form:** `prose` `symbolic` — The central artifact is prose instruction, but it generates symbolic shell scripts, frontmatter schemas, Dataview queries, slash-command procedures, and Markdown page templates.
- **Lineage:** `authored` `imported` — The setup prompt and generated commands are authored scaffolding, while generated vault pages and source layers are derived from copied docs, memory files, agent rules, and source-code reads
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` — Wiki pages advise future agents, while generated rules, commands, schemas, sync scripts, Dataview health checks, and status fields instruct, route, or audit later work

**Bootstrap prompt.** Storage substrate: `SETUP_PROMPT.md` in the source repository. Representational form: prose procedure with embedded shell snippets, directory trees, frontmatter rules, command specs, and audit checklists. Lineage: authored from Karpathy's LLM Wiki pattern and specialized for Claude Code project work. Behavioral authority: system-definition artifact when pasted into Claude Code, because it instructs the agent to create files, edit project rules, scan source code, and run verification passes. Its effective authority is not verified by code tests in this repository.

**Generated vault scaffold.** Storage substrate: target-project repo files under `Obsidian Vault/<ProjectName>/`. Representational form: mixed Markdown prose, frontmatter, Obsidian wikilinks, Dataview query blocks, and Templater templates. Lineage: generated from the target project's source audit, copied docs/memory, and the setup prompt's schema. Behavioral authority: knowledge artifact when wiki pages are read as project reference; system-definition artifact when `schema.md`, templates, health checks, and wiki status fields govern future maintenance.

**Sources layer and sync script.** Storage substrate: target-project `Sources/` files plus `scripts/sync-vault.sh`. Representational form: copied Markdown/source documentation and symbolic shell commands. Lineage: derived snapshots from `.claude/memory`, `.claude/rules`, root agent files, READMEs, and docs paths, with a "not authoritative" header added to copied agent-instruction files. Behavioral authority: mostly knowledge artifact authority as preserved evidence for wiki generation; the sync script has system-definition authority over which project materials enter the source layer.

**Compiled wiki pages and index.** Storage substrate: target-project `Wiki/*.md` files and `index.md`. Representational form: prose pages constrained by page types, frontmatter, code excerpt conventions, source pointers, Semantic Lookup entries, and wikilinks. Lineage: distilled from `Sources/` and source-code reads during bootstrap or ingest; invalidated by source changes, missing coverage, broken links, stale status, or open gap entries. Behavioral authority: knowledge artifacts when consulted for answers; weak system-definition artifacts when the wiki-first rule makes them the primary context before source reads.

**Generated agent rules and commands.** Storage substrate: target-project `CLAUDE.md`, `GEMINI.md`, `.claude/commands/wiki-ingest.md`, and updates to status/phase commands when present. Representational form: prose instructions with shell snippets and procedural checklists. Lineage: generated from the setup prompt and patched into the target project's existing agent-control surface. Behavioral authority: system-definition artifacts. They route future agent work through the wiki, mark pages stale after code edits, run diff-based ingests, and close gap-to-resolution loops.

**Gap log and health/audit surfaces.** Storage substrate: target-project `log.md`, `Wiki/_Health.md`, and Phase G audit outputs. Representational form: structured prose log entries, Dataview queries, and checklist findings. Lineage: generated from bootstrap, ingest, gap discovery, link checks, frontmatter checks, and existing-vault audits. Behavioral authority: knowledge artifact authority as evidence of maintenance history and open gaps; system-definition authority when `/wiki-ingest` or Phase G consumes those records to create or repair wiki pages.

The promotion path is clear but prompt-mediated: raw project docs and source files become copied `Sources/`, then compiled wiki pages, then wiki-first context for later agents. Some generated artifacts cross into stronger symbolic authority, especially `sync-vault.sh`, frontmatter schemas, Dataview health checks, and grep/diff maintenance procedures. The source repository does not include a deterministic implementation or tests that prove those generated artifacts are created correctly.

## Comparison with Our System

| Dimension | llm-project-wiki | Commonplace |
|---|---|---|
| Primary unit | Generated Obsidian project wiki | Typed Markdown artifacts in a methodology KB |
| Bootstrap mechanism | One Claude Code setup prompt | Repository code, collection contracts, skills, validators, and review workflows |
| Source layer | Copied `Sources/` snapshots from project docs/memory | Captured sources, source-grounded reviews, and workshop material |
| Read path | Wiki-first lookup through generated `index.md` and wiki pages | Search, generated indexes, authored links, skills, and type contracts |
| Maintenance | Prompt-defined sync, diff ingest, stale marking, gap audit | Deterministic validation, generated indexes, review bundles, git lifecycle |
| Main risk | Prompt compliance and generated-artifact drift | Methodology overhead and validation/review maintenance cost |

The strongest alignment is the compiled-knowledge bet. Both systems treat raw source material as too expensive and noisy to reread on every task, then create retained Markdown artifacts that make future agent work cheaper. llm-project-wiki applies that pattern to arbitrary software projects; Commonplace applies it to agent-operated KB methodology and external-system reviews.

The main divergence is where authority is codified. llm-project-wiki leaves almost everything inside natural-language setup and generated maintenance prompts. Commonplace moves more of the system into typed frontmatter, schemas, validators, CLI commands, and collection-local contracts. That makes Commonplace heavier, but it also gives maintainers more deterministic ways to detect drift.

llm-project-wiki is more aggressive about making the compiled wiki the first stop for all future project questions. Commonplace usually expects an agent to choose among search, indexes, links, instructions, and validation outputs. The wiki-first rule is attractive because it creates a simple default path, but it is only safe if wiki freshness and coverage are maintained.

**Read-back:** `pull` — For retained memory only, wiki content reaches the agent when the agent follows the generated wiki-first rule, opens `index.md`, and reads selected wiki pages. The always-loaded part is the lookup instruction in `CLAUDE.md` or `GEMINI.md`, not selected retained wiki content.

### Borrowable Ideas

**Make a generated semantic lookup table the first-page contract.** Commonplace has curated and generated indexes, but a compact "question / intent -> artifact" table is a useful affordance for project-specific agents. Ready for scoped indexes where common questions are stable.

**Use stale marking as an explicit source-to-wiki invalidation path.** The prompt's code-edit rule marks wiki pages stale by searching for `source_file:` references. Commonplace already has validation and generated indexes, but source-linked reviews and workshop outputs could benefit from similarly cheap invalidation markers where a source path changes. Needs a concrete source-backed workflow.

**Separate copied source snapshots from compiled wiki pages.** This matches Commonplace's source/review split. The borrowable detail is the explicit "reference copy, not authoritative instruction" header for synced agent files, which reduces accidental instruction leakage from archived context. Ready for source snapshots that copy `AGENTS.md`, `CLAUDE.md`, or similar files.

**Treat gap logs as maintenance inputs, not just notes.** llm-project-wiki's gap-to-log-to-ingest loop gives a lightweight path from failed lookup to future wiki improvement. Commonplace has workshop notes and review findings; a narrower gap-log grammar could help avoid mid-task context switching while preserving improvement signals. Ready as a workshop convention.

**Do not borrow prompt-only generation where deterministic tooling is cheap.** The setup prompt specifies scripts, frontmatter checks, orphan checks, and index completeness checks in prose. Commonplace should keep such checks in executable validators when the rule is stable enough to codify.

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `consolidate` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Curiosity Pass

The repository is a pure prompt artifact. That is not a defect, but it makes the review's code-grounding unusual: there is no parser, CLI, package manifest, test suite, or generated example vault to inspect. The source can prove the intended protocol, not its execution quality in real projects.

The prompt tells Claude to write a wiki "for LLM retrieval" and not for humans ([SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md)). That is a useful corrective against marketing docs, but it can also lead to pages optimized for exhaustive excerpts rather than maintainable abstractions. The quality bar says any question requiring source reads is a gap; that may encourage over-copying unless the wiki has strong page-size and update-cost discipline.

The wiki-first rule improves activation by making the lookup path obvious, but it is still pull from the agent's perspective. Nothing in the repository implements automatic relevance-gated injection of wiki pages into the model context.

The Sources layer copies root instruction files with a "not authoritative" header. That is a small but important safety pattern: archived instructions are evidence for the wiki, not live instructions for the acting agent.

The generated `/wiki-ingest` command is diff-based, but it relies on source references inside wiki pages and grep mappings. That is practical for early adoption, but brittle if generated pages omit `source_file`, cover many sources, or describe cross-cutting concepts whose invalidation does not map cleanly to one file path.

## What to Watch

- Whether the repository adds a worked example vault from a real project; that would make the prompt's generated artifacts reviewable rather than only specified.
- Whether `/wiki-ingest` becomes an executable command with deterministic stale-page discovery, link checks, and frontmatter validation; that would shift part of the system from prose authority into symbolic authority.
- Whether the wiki-first rule gains context-budget policy for page length, excerpt size, and number of pages read before answering.
- Whether gap entries remain manually filed maintenance signals or become true trace-derived extraction from session logs, tool traces, or repeated failed lookups.
- Whether source-to-wiki lineage gets stronger than path references, for example section anchors, symbol ids, commit pins, or generated dependency maps.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - supports: llm-project-wiki tries to close storage-to-context failure with an explicit wiki-first lookup rule.
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) - aligns: compiled wiki pages precompute source understanding so future calls do not repeatedly rediscover project structure.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: the same Markdown wiki pages have different authority when read as reference versus made primary by `CLAUDE.md`.
- [The wikiwiki principle: lowest-friction capture, then progressive refinement in place](../../notes/wikiwiki-principle-lowest-friction-capture-then-progressive-refinement.md) - contrasts: llm-project-wiki bootstraps a structured wiki up front rather than gradually refining low-friction captures.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: copied Sources, wiki pages, and gap logs mostly serve as evidence, reference, or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: the setup prompt, generated rules, sync script, and slash-command procedures carry instruction, routing, and validation force.
