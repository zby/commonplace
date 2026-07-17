---
description: "llm-project-wiki review: prompt-only Claude Code workflow that bootstraps an Obsidian project wiki, wiki-first rules, diff ingest, and gap audits"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# llm-project-wiki

`llm-project-wiki`, from `akash-r34/llm-project-wiki`, is a prompt-only Claude Code setup kit for creating an Obsidian "LLM wiki" inside a software project. At the reviewed commit it contains only `README.md` and `SETUP_PROMPT.md`; the shipped behavior is an authored prompt that asks Claude to audit a project, scaffold a vault, build wiki pages, wire future-agent lookup rules, and maintain the wiki through diff-based ingest and gap audits.

**Repository:** https://github.com/akash-r34/llm-project-wiki

**Reviewed commit:** [1fdfba9129a46afd18aa68a83f12d6716ab694c6](https://github.com/akash-r34/llm-project-wiki/commit/1fdfba9129a46afd18aa68a83f12d6716ab694c6)

**Last checked:** 2026-06-04

## Core Ideas

**The system is an agent prompt, not an application runtime.** The repo's file list is just `README.md` and `SETUP_PROMPT.md`; there is no package, executable, tests, or library code. The implementation surface is therefore the setup prompt itself: it instructs a Claude Code session to detect whether an `Obsidian Vault/` exists, then either build a new vault through phases 0-6 or run Phase G as a repair audit ([SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md), [README.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/README.md)).

**It compiles project sources into an Obsidian wiki.** The prompt defines a three-layer vault: `Sources/` for synced originals, `Wiki/` for LLM-maintained compiled pages, and `Templates/` for page creation. It requires `schema.md`, `log.md`, `index.md`, six Templater templates, an Obsidian health page, and eventually 40-100+ interlinked project pages covering architecture, entities, concepts, decisions, status, and references ([SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md), [README.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/README.md)).

**Wiki-first lookup is the behavior hook.** Setup modifies `CLAUDE.md` and optionally `GEMINI.md` so future agent sessions must consult the vault `index.md`, use its Semantic Lookup table, read relevant wiki pages, and only then fall back to existing memory files or source files. That makes the generated wiki a primary context surface for future coding work, but the actual page content is still read through explicit navigation rather than automatically injected into every model call ([SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md)).

**Context efficiency comes from precompilation plus diff refresh.** The intended optimization is to avoid rereading raw code for ordinary questions: future sessions use a semantic index and compiled wiki pages with code excerpts, constraints, and cross-references. Maintenance is scoped by `git diff HEAD~1 --name-only`, path-to-`Sources/` mapping, grep from changed source to affected wiki pages, section-level updates, and stale-page frontmatter ([SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md), [README.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/README.md)).

**Governance is prompt-specified and file-based.** The prompt asks Claude to create Dataview health checks, frontmatter requirements, wikilink density targets, stale status, gap logs, bootstrap/audit logs, sync scripts, slash commands, and protocol wiring checks. Those are inspectable files, but the reviewed repo does not include generated examples or executable validation proving that a resulting vault satisfies them ([SETUP_PROMPT.md](https://github.com/akash-r34/llm-project-wiki/blob/1fdfba9129a46afd18aa68a83f12d6716ab694c6/SETUP_PROMPT.md)).

## Artifact analysis

- **Storage substrate:** `files` `repo` — The shipped system is two Markdown files in a git repository, and the generated target state is an Obsidian vault plus project files such as `CLAUDE.md`, `GEMINI.md`, `.claude/commands/wiki-ingest.md`, `scripts/sync-vault.sh`, `SECOND_BRAIN.md`, and wiki Markdown pages.
- **Representational form:** `prose` `symbolic` — The operative artifact is prose instruction to Claude; symbolic parts include vault directory contracts, command paths, shell snippets, frontmatter schemas, page types, status values, log grammars, Dataview queries, and grep/git workflows.
- **Lineage:** `authored` `imported` `trace-extracted` — The setup prompt and generated schemas/rules are authored; `Sources/` snapshots are imported from project memory, rules, root docs, and design docs; gap entries and query-generated missing-page work are trace-extracted from future tasks where the wiki proves insufficient.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `learning` — Generated wiki pages advise future agents as knowledge; `CLAUDE.md` / `GEMINI.md` wiki-first rules and slash commands instruct; stale marking, sync cadence, and "only if insufficient" fallback rules constrain behavior; `index.md`, Semantic Lookup, wikilinks, and grep path matching route reads and maintenance; frontmatter, health dashboards, orphan checks, broken-link checks, and gap audits validate; gap-to-ingest and diff ingest implement a lightweight learning loop.

**Setup prompt.** `SETUP_PROMPT.md` is the highest-authority retained artifact in the source repo. It does not store project knowledge itself; it causes a future Claude session to create a local knowledge substrate and agent rules in the target project.

**Generated vault.** The intended durable memory is the created Obsidian vault: `Sources/` preserves source snapshots, `Wiki/` stores compiled knowledge pages, `Templates/` constrains future page shape, `index.md` routes questions, `schema.md` governs maintenance, and `log.md` stores bootstrap, ingest, gap, and audit records.

**Generated project rules and commands.** The prompt wires `CLAUDE.md`, `GEMINI.md`, `/wiki-ingest`, `/status`, and `/phase-complete` so future agent sessions treat the wiki as primary context and mark pages stale after code edits. These are system-definition artifacts because they shape future agent workflow, not just human documentation.

**Access structures.** The Semantic Lookup table, full TOC, wikilinks, Dataview stale/old/orphan/schema checks, grep by `source_file`, and `git diff` changed-file lists are symbolic access structures. They reduce search complexity, but the repo does not provide measured retrieval quality.

Promotion path: raw project files are synced into `Sources/`, compiled by Claude into wiki pages, then given stronger future authority through `CLAUDE.md` / `GEMINI.md` wiki-first rules. Gap entries can later promote missing knowledge into new or updated wiki pages through `/wiki-ingest`.

## Comparison with Our System

`llm-project-wiki` and Commonplace both treat Markdown files plus agent instructions as a real context-engineering substrate. The difference is where discipline lives. Commonplace has collection contracts, type specs, validation commands, review workflows, and a repo-wide methodology for durable artifacts. `llm-project-wiki` is a bootstrap prompt that asks an LLM to create an Obsidian vault and maintenance conventions inside another repo.

The strongest overlap is the compiled-source model: source snapshots feed distilled pages, and later agents should prefer the distilled surface before opening raw source. The largest divergence is enforcement. Commonplace validates artifact structure with shipped commands; `llm-project-wiki` relies on Claude following prompt instructions, shell snippets, Dataview queries, and manual commit discipline in the generated project.

### Borrowable Ideas

**Semantic Lookup as a first-class routing table.** Ready now as a navigation pattern. Commonplace indexes could carry more "question / intent -> artifact" rows for recurring agent tasks, not only directory listings and tag hubs.

**Stale marking on source edits.** Ready for workflows where notes describe source files. Commonplace could borrow the explicit "edit source -> mark derived page stale" rule for generated reference pages, while keeping validation separate from the generated wiki.

**Gap-to-log-to-ingest loop.** Useful with a concrete workshop workflow. A failed lookup should leave a small, structured gap entry that the next maintenance pass can promote into a source, note, or index update.

**Do not borrow prompt-only enforcement as sufficient governance.** The setup prompt is practical for bootstrapping, but Commonplace should keep deterministic validators and review gates for artifacts that carry durable authority.

## Write side

**Write agency:** `manual` `automatic` — A human manually starts the setup prompt, sync script, and slash commands, but the instructed Claude workflow automatically scaffolds files, writes pages, updates stale pages, resolves gaps, audits vault wiring, and patches missing infrastructure within that session.

**Curation operations:** `evolve` `synthesize` `invalidate` — Diff ingest evolves existing wiki pages by updating only changed sections; bootstrap and gap resolution synthesize new overview/entity/concept/decision/status/reference pages from multiple project sources; code edits mark affected wiki pages `status: stale`, and Phase G repairs stale or broken vault state. There is no shipped deduplication, decay, recurrence promotion, or contradiction-maintenance implementation beyond prompt-specified link/orphan/gap audits.

### Trace-learning

**Trace source:** `session-logs` — The qualifying trace-learning path is the future-work loop: when a question or task reveals that the wiki is insufficient, Claude appends a `[gap]` entry to `log.md`; the next `/wiki-ingest` reads open gaps and creates or updates the missing pages.

**Learning scope:** `per-project` — The generated wiki, gaps, stale markers, and command rules live in the target software project.

**Learning timing:** `online` `staged` — Gap capture happens during the future task that discovered the missing knowledge; resolution is staged into the next ingest or gap-audit pass.

**Distilled form:** `prose` `symbolic` — Gaps become prose log entries, then wiki pages with frontmatter, wikilinks, source paths, and status metadata.

**Extraction.** The oracle is the acting LLM's judgment that the wiki was insufficient for the current task. The prompt prescribes a one-sentence gap note and later ingest processing, but it does not ship code that parses transcripts or automatically ranks gaps.

**Scope and timing.** Most wiki construction is imported-source distillation, not trace learning. The trace-derived part is narrow: task-time lookup failures become durable gap records and later wiki updates.

**Survey fit.** `llm-project-wiki` is a prompt-level example of trace-derived repair, not a trace-mining platform. It strengthens the distinction between "compile source into a wiki" and "learn from future agent sessions where the compiled wiki fails."

## Read-back

**Read-back:** `pull` — The generated wiki becomes the primary reference, but future agents are instructed to open `index.md`, use the Semantic Lookup table, and read wiki pages explicitly; the reviewed repo does not implement automatic memory injection into the model context.

Wiki-first rules in `CLAUDE.md` and `GEMINI.md` are pushed instructions about *how* to retrieve memory, not automatic delivery of the memory content itself. `/status` similarly starts from a wiki status page by command convention. The read path is therefore deliberate navigation over retained files: index -> wiki page -> fallback memory/source only when insufficient.

Selection and scope are bounded by the authored routing structures: Semantic Lookup entries, TOC groups, wikilinks, `source_file` frontmatter, `grep -rl` affected-page discovery, and changed-file lists from `git diff`. The repo does not include tests or telemetry proving that this selection improves answer quality or prevents stale-source mistakes.

## Curiosity Pass

**The most consequential artifact is not the wiki; it is the rule that makes agents trust the wiki first.** Without the generated `CLAUDE.md` / `GEMINI.md` protocol, the vault is just documentation. With it, the same files gain operational authority over future source-reading behavior.

**The system's portability comes from being prompt-only.** Any Claude Code project can try it without installing a package, but every guarantee depends on the model correctly executing a long prompt and maintaining the generated conventions.

**The stale-marker loop is cheap but fragile.** Grepping `source_file:` frontmatter can work for direct entity pages, but cross-cutting concept, architecture, and decision pages may need updates even when no single `source_file` points at the changed code.

**It intentionally optimizes for LLM retrieval over human documentation.** The prompt explicitly says the wiki is not for humans and should prioritize precision over readability. That is aligned with agent memory, but it may make ordinary project documentation less pleasant if teams conflate the two.

## What to Watch

- Whether the repo gains generated sample vaults or tests; that would make it possible to evaluate whether the long setup prompt reliably produces the promised structure.
- Whether `/wiki-ingest` becomes executable code rather than a Markdown command prompt; that would shift maintenance from model-followed procedure toward deterministic tooling.
- Whether stale propagation expands beyond direct `source_file` grep to dependency-aware updates for concept, architecture, and decision pages.
- Whether the gap log gains status, owner, source, and resolution metadata; that would make the trace-derived repair loop auditable rather than a loose task journal.
- Whether Obsidian Dataview health checks are complemented by CLI validation so non-Obsidian agents can enforce the same constraints.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: the generated wiki is pulled through explicit lookup, even though wiki-first rules push the obligation to look.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: setup prompts, generated wiki pages, source snapshots, rules, logs, and commands differ by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: compiled wiki pages advise future agents as reference context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: setup prompt, `CLAUDE.md` / `GEMINI.md` rules, slash commands, schemas, and health checks shape future behavior.
- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - qualifies narrowly: task-discovered wiki gaps become durable log entries and later page updates.
