---
description: "hyalo review: Rust CLI for structured Markdown KB search, mutation, linting, snapshot indexes, and Claude skill/rule integration"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-02"
---

# hyalo

hyalo, from `ractive/hyalo`, is a Rust CLI for operating Markdown knowledge bases with YAML frontmatter. It is agent-relevant because it turns a file-backed Obsidian/Zettelkasten-style vault into a structured tool surface: agents can search by content, metadata, links, sections, and tasks; mutate frontmatter and task state; rewrite links during moves; lint schema and Markdown rules; and install Claude Code skills/rules that tell the host agent to prefer hyalo over raw file tools.

**Repository:** https://github.com/ractive/hyalo

**Reviewed commit:** [499fa064237041a06e79634cf7dadfaf34fe6b9b](https://github.com/ractive/hyalo/commit/499fa064237041a06e79634cf7dadfaf34fe6b9b)

**Last checked:** 2026-06-02

## Core Ideas

**The memory substrate is the user's Markdown vault, not a service-owned store.** hyalo is explicit that it works with existing `.md` files, YAML frontmatter, tags, wikilinks, Markdown links, and task checkboxes rather than imposing a new note model ([README.md](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/README.md)). Configuration lives in `.hyalo.toml`, and commands resolve paths against the configured vault directory ([crates/hyalo-cli/src/commands/config.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/src/commands/config.rs), [crates/hyalo-cli/src/cli/args.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/src/cli/args.rs)).

**The agent-facing surface is structured CLI output and deterministic operations.** The command parser exposes a broad command set around `find`, `read`, `set`, `append`, `remove`, `mv`, `links`, `lint`, `types`, `views`, `new`, `summary`, `tags`, `properties`, `backlinks`, tasks, and index lifecycle ([crates/hyalo-cli/src/cli/args.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/src/cli/args.rs)). Successful list output is wrapped as `{"results": ..., "total": ..., "hints": [...]}`, and `--jq` is implemented through `jaq` over that envelope ([crates/hyalo-cli/src/output.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/src/output.rs), [crates/hyalo-cli/Cargo.toml](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/Cargo.toml)). That makes hyalo more like a typed shell API over a KB than a retrieval model.

**Context efficiency comes from scoped retrieval, metadata-first filtering, and snapshot indexes.** `find` narrows by file/glob, property filters, tags, task status, sections, title, broken-link/orphan/dead-end state, sort field, and output fields before returning bounded results ([crates/hyalo-cli/src/commands/find/mod.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/src/commands/find/mod.rs)). BM25 ranked search is implemented with boolean query parsing, phrase support, stemming, and document scoring, while regex search remains available for literal matching ([crates/hyalo-core/src/bm25.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-core/src/bm25.rs)). For repeated queries, `create-index` serializes pre-scanned metadata, link graph data, and optional BM25 data to `.hyalo-index`; read-only commands can consume that snapshot rather than walking the filesystem each time ([crates/hyalo-core/src/index.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-core/src/index.rs), [README.md](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/README.md)).

**Mutations are designed to preserve KB structure.** `mv` validates sources and targets, plans link rewrites, supports dry-run output, then applies file moves and link updates when requested ([crates/hyalo-cli/src/commands/mv.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/src/commands/mv.rs)). Shared mutation helpers patch the snapshot index after frontmatter changes, file creation, and moves, which prevents an active agent loop from consulting stale metadata immediately after it changes a file ([crates/hyalo-cli/src/commands/mutation.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/src/commands/mutation.rs)). Link repair uses deterministic candidate strategies before fuzzy matching, and auto-linking scans unlinked title/alias mentions while avoiding ambiguous titles and excluded targets ([crates/hyalo-core/src/link_fix.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-core/src/link_fix.rs), [crates/hyalo-core/src/auto_link.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-core/src/auto_link.rs)).

**Validation is schema-and-rule based rather than model-judged.** `.hyalo.toml` can define default and per-type schemas with required fields, property constraints, defaults, filename templates, and required sections ([crates/hyalo-core/src/schema.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-core/src/schema.rs)). `hyalo lint` checks frontmatter schema violations, can promote certain warnings in strict mode, validates suspicious saved views, and supports autofix paths for selected issues ([crates/hyalo-cli/src/commands/lint.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/src/commands/lint.rs)). `hyalo new` scaffolds a file from a type schema with placeholders and required sections, making "create, fill, lint" an explicit loop ([crates/hyalo-cli/src/commands/new.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/src/commands/new.rs)).

**Claude integration is generated instruction, not a hidden agent runtime.** `hyalo init --claude` writes `.claude/skills/hyalo/SKILL.md`, `.claude/skills/hyalo-tidy/SKILL.md`, `.claude/rules/knowledgebase.md`, and a managed `.claude/CLAUDE.md` section ([crates/hyalo-cli/src/commands/init.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/src/commands/init.rs)). The main skill tells Claude to use the CLI for Markdown with frontmatter; the rule scopes that advice to the configured knowledgebase path; the tidy skill is a manual consolidation workflow that asks Claude to run hyalo, inspect recent git history, optionally inspect Claude memory files, and report or apply conservative fixes ([crates/hyalo-cli/templates/skill-hyalo.md](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/templates/skill-hyalo.md), [crates/hyalo-cli/templates/rule-knowledgebase.md](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/templates/rule-knowledgebase.md), [crates/hyalo-cli/templates/skill-hyalo-tidy.md](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/templates/skill-hyalo-tidy.md)).

## Artifact analysis

- **Storage substrate:** `files` — User-owned filesystem/repository files under the configured vault directory
- **Representational form:** `mixed` — Mostly prose plus symbolic YAML frontmatter, tags, links, headings, and task checkboxes

**Markdown knowledgebase files.** Storage substrate: user-owned filesystem/repository files under the configured vault directory. Representational form: mostly prose plus symbolic YAML frontmatter, tags, links, headings, and task checkboxes. Lineage: authored or imported by humans and agents; hyalo can scaffold, mutate metadata, rewrite links, and lint them, but it does not claim source authority for the prose. Behavioral authority: knowledge artifacts when read as evidence/reference/context; system-definition artifacts when frontmatter, tags, task state, or links drive command selection, validation, routing, or future agent instructions.

**`.hyalo.toml` configuration.** Storage substrate: a TOML file at the project root or active command directory. Representational form: symbolic configuration. Lineage: authored by the user, created/updated by `hyalo init`, and mutated by commands such as `views`, `types`, and `lint-rules`. Behavioral authority: system-definition artifact with configuration force: it sets vault scope, output defaults, link-resolution policy, schemas, saved views, and lint-rule overrides.

**Snapshot index (`.hyalo-index`).** Storage substrate: MessagePack-serialized file, usually under the vault directory. Representational form: symbolic metadata entries, link graph, and optional BM25 inverted index; no LLM embeddings or vector store are present in the inspected implementation. Lineage: derived from a scan of Markdown files, frontmatter, headings, tasks, links, and tokenized text; invalidated by source file changes and patched best-effort by mutation commands. Behavioral authority: ranking/routing system-definition artifact because it determines which files, links, backlinks, task states, and BM25-ranked results reach a later agent command.

**BM25 search index and filters.** Storage substrate: Rust data structures at runtime, optionally persisted inside `.hyalo-index`. Representational form: symbolic query AST plus statistical term indexes and stemmed tokens. Lineage: derived from document title/body text and optional per-document language metadata. Behavioral authority: ranking and selection authority: it decides what content an agent sees when it deliberately asks for a search.

**CLI command outputs and hints.** Storage substrate: transient stdout/stderr data in the agent/tool loop. Representational form: structured JSON envelope or compact text, with concrete follow-up command hints generated from command output and context ([crates/hyalo-cli/src/hints.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/src/hints.rs), [crates/hyalo-cli/src/output.rs](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/crates/hyalo-cli/src/output.rs)). Lineage: derived at command time from source files, config, elapsed time, flags, and result payloads. Behavioral authority: advisory system-definition artifact for the immediate next action; hints can steer an agent toward drill-down commands but do not themselves mutate the KB unless the agent executes them.

**Generated Claude skills, rules, and managed CLAUDE section.** Storage substrate: generated Markdown files under `.claude/skills/`, `.claude/rules/`, and `.claude/CLAUDE.md`. Representational form: prose instructions plus path-scoped rule metadata. Lineage: authored templates embedded in the CLI and parameterized by `hyalo init --claude`; re-running init overwrites/updates them. Behavioral authority: system-definition artifacts consumed by Claude Code through its skill/rule channels. They give instruction force to prefer hyalo commands, but activation and obedience are host-agent behavior outside hyalo's Rust code.

**hyalo's own dogfood knowledgebase.** Storage substrate: repository Markdown under `hyalo-knowledgebase/`. Representational form: prose research, iteration notes, dogfood reports, backlog items, and decision logs. Lineage: authored and dogfooded during development; the repo's `CLAUDE.md` tells agents to use hyalo for those docs ([CLAUDE.md](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/CLAUDE.md), [hyalo-knowledgebase/decision-log.md](https://github.com/ractive/hyalo/blob/499fa064237041a06e79634cf7dadfaf34fe6b9b/hyalo-knowledgebase/decision-log.md)). Behavioral authority: knowledge artifacts for maintainers and agents working on hyalo; selected instructions in `CLAUDE.md` and generated skills/rules are stronger system-definition artifacts. The dogfood reports are not trace-derived learning in this review's taxonomy because the inspected code does not implement an automatic trace-to-durable-artifact extraction loop from those reports.

The promotion path is mostly symbolic, not learned: prose notes can gain stronger authority when frontmatter, schemas, saved views, links, generated rules, or lint checks make them selectable or enforceable. hyalo can scaffold and validate that stronger surface, but the human or host agent decides what content should be promoted.

## Comparison with Our System

| Dimension | hyalo | Commonplace |
|---|---|---|
| Primary purpose | Operate arbitrary Markdown/frontmatter vaults from a CLI | Maintain a typed methodology KB and framework for agent-operated knowledge bases |
| Main substrate | User filesystem plus `.hyalo.toml` and optional `.hyalo-index` | Git-tracked KB collections, type specs, instructions, generated indexes, validation reports |
| Retrieval | Pull commands: BM25, regex, metadata filters, links, sections, tasks, saved views | Pull through `rg`, indexes, links, reports, and collection/type contracts |
| Mutation | CLI-managed frontmatter/task/link/file operations with dry-run and index patching | File edits plus Commonplace commands for validation, indexes, reviews, snapshots, and note operations |
| Governance | TOML schemas, lint rules, safe path/link handling, strict mode, generated Claude guidance | Collection contracts, schemas, deterministic validation, semantic review, review gates, archive/replacement workflow |
| Learning | No implemented trace-derived learning loop found | No automatic trace-learning assumption; workshop/report artifacts can be promoted deliberately |

hyalo is a closer cousin to Commonplace than to most "memory" libraries: both use ordinary files and typed metadata to make agent work inspectable. The main difference is scope. hyalo is a general-purpose CLI that stays intentionally neutral about note organization, while Commonplace is a specific KB methodology with collection-local contracts, artifact types, and review workflows.

The useful comparison is not "which has more memory," but where authority sits. In hyalo, the authority is concentrated in command behavior and config: if the vault has a schema or saved view, hyalo will enforce or recall it; if not, it remains a flexible Markdown operations layer. In Commonplace, the collection contract and type system are part of the content architecture itself, so writing and routing choices carry more built-in semantics.

hyalo's context-efficiency story is strong for tool loops: it returns filtered, field-shaped, machine-readable results and can reuse a snapshot index. It does not perform semantic context assembly, multi-hop reasoning, or LLM summarization. That restraint is a design advantage when the goal is predictable agent tooling over a human-readable KB.

**Read-back:** `pull` — For hyalo's implemented retrieval and mutation machinery. Generated Claude rules/skills and managed instructions add always-loaded or ordinary host-skill instruction surfaces, but I did not find engineered relevance-gated push activation in hyalo's own code, so this review does not carry `push-activation`

I also did not find qualifying trace-derived learning. The tidy skill can ask Claude to inspect git history, recent KB changes, and optional Claude memory files, and the repository contains dogfood reports; those are manual workflow/report artifacts unless an external agent follows the skill. The inspected implementation does not derive durable behavior-shaping artifacts from session/tool traces, so this review does not carry `trace-derived`.

### Borrowable Ideas

**Command hints as agent navigation affordances.** Commonplace could make validation, index, review, and connect commands emit concrete next-command hints derived from result payloads. This is ready where a command already has structured output and a small number of obvious drill-downs.

**Snapshot indexes with mutation patching.** hyalo's `.hyalo-index` is attractive because it amortizes repeated agent queries and mutation commands patch it in place. Commonplace has generated indexes, but a fast query snapshot over frontmatter, links, review status, and note types would reduce repeated `rg` work in long sessions. Ready for exploration; needs a clear invalidation model.

**Schema-driven file scaffolding with intentionally invalid placeholders.** `hyalo new` creates the structural shell and then relies on lint to tell the writer what remains invalid. Commonplace already has type specs and skills; borrowing this would mean a `commonplace new` path that creates type-correct skeletons but leaves semantically required fields visibly incomplete. Ready if paired with validation.

**Safe link-preserving moves as a first-class operation.** Commonplace already has relocation commands, but hyalo's single-file and batch move design is a good reference for dry-run output, conflict handling, link rewrite plans, and index patching. Ready as an implementation comparison when revising relocation UX.

**Generated host-agent integration from the CLI.** `hyalo init --claude` makes the tool teach the host agent how to use it. Commonplace could similarly generate or refresh local agent rules/skills from current type specs and collection contracts. Useful, but it should be treated as generated static instruction rather than as read-back learning.

**Saved views as named retrieval contracts.** `.hyalo.toml` views encode reusable filters in config. Commonplace could borrow named query presets for common review and navigation states, especially "current seedling notes," "stale reviews," or "notes missing outbound links." Ready once the query surface is stable.

## Curiosity Pass

**The "LLM Wiki" framing is mostly operational, not cognitive.** hyalo supports the Karpathy-style pattern by giving an LLM reliable tools for a persistent wiki, but it does not itself decide what to remember, summarize traces, or judge relevance beyond search/filter mechanisms.

**The generated Claude skill is powerful because it changes tool choice.** It does not push memories into task context; it changes the agent's preferred interface to a Markdown KB. That is a behavioral-authority shift even without qualifying as engineered push activation.

**Hints are a small but important agent API.** The hint system is not memory, but it is a behavior-shaping artifact: it turns command output into suggested next actions. For agents, that may matter more than another natural-language help page.

**BM25 is a pragmatic middle ground.** hyalo avoids vector stores and embeddings, but still gives ranked full-text retrieval with boolean/phrase behavior. That makes retrieval cheap, inspectable, and offline, at the cost of semantic matching.

**Dogfooding creates lots of retained evidence without an automatic learning loop.** The repository's dogfood reports, decision log, and iteration files are valuable knowledge artifacts. They only become system-definition artifacts when humans or agents promote their lessons into rules, schema, commands, or generated instructions.

## What to Watch

- Whether hyalo adds a semantic/vector retrieval layer; that would change the retained artifacts from symbolic/statistical indexes to mixed distributed-parametric ranking state.
- Whether `/hyalo-tidy` becomes an implemented CLI subcommand or scheduled workflow that writes durable review artifacts from git/session traces; that would reopen the `trace-derived` decision.
- Whether generated Claude integration expands from static skills/rules into event hooks or relevance-gated activation; that would reopen the `push-activation` decision.
- Whether `.hyalo-index` grows stronger invalidation, locking, or provenance metadata; that would make it more borrowable for Commonplace query acceleration.
- Whether schemas gain richer body-section contracts and cross-file constraints; that would move hyalo closer to Commonplace's collection/type contract model.

Relevant Notes:

- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: hyalo reduces context load through scoped CLI retrieval, field selection, and snapshot indexes.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: hyalo requires separating Markdown files, TOML config, snapshot indexes, generated skills/rules, command outputs, and dogfood reports by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: vault notes, dogfood reports, command outputs, and lint reports become evidence/reference/context when consumed by an agent.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: `.hyalo.toml`, schemas, lint rules, saved views, snapshot indexes, command implementations, and generated Claude rules/skills configure or constrain behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - clarifies: hyalo stores and indexes knowledge, but future use still depends mostly on deliberate pull commands or host-agent static instructions.
