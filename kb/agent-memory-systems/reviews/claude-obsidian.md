---
description: "claude-obsidian review: Obsidian/Claude Code wiki skills with hot-cache push, pull-first retrieval, locks, modes, and optional BM25/rerank indexes"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-03"
tags: [trace-derived, push-activation]
---

# claude-obsidian

claude-obsidian, from `AgriciDaniel/claude-obsidian`, is a Claude Code plugin and Obsidian vault template for maintaining a persistent LLM-written wiki. At the reviewed commit, its memory system is a plain-file Obsidian vault plus agent skills, slash commands, hooks, and Python/Bash helper scripts: agents ingest sources into `.raw/` and `wiki/`, query by hot-cache/index/page reads or optional chunk retrieval, save conversations as wiki notes, roll up log entries into fold pages, and use locks, mode routing, and metadata files to keep the vault operable under multi-writer workflows.

**Repository:** https://github.com/AgriciDaniel/claude-obsidian

**Reviewed commit:** [cb93ff6d82f9c35a08bf6010e7fac36dfddc827b](https://github.com/AgriciDaniel/claude-obsidian/commit/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b)

**Last checked:** 2026-06-03

## Core Ideas

**The wiki is the memory, not a chat sidecar.** The top-level reference instruction tells the agent it is maintaining a persistent, compounding wiki inside an Obsidian vault, with `.raw/` as immutable source storage, `wiki/` as LLM-generated knowledge, and `WIKI.md`/skills as the schema and operating procedure ([WIKI.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/WIKI.md), [skills/wiki/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki/SKILL.md)). The README positions this as a "knowledge engine" rather than an Obsidian chat interface ([README.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/README.md)).

**The primary context-efficiency ladder is hot cache -> index -> pages, with optional chunk retrieval.** `wiki-query` reads `wiki/hot.md` first, then `wiki/index.md`, then selected pages, with quick/standard/deep modes and explicit token budgets ([skills/wiki-query/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki-query/SKILL.md)). When provisioned, `wiki-retrieve` replaces the page-level drill path for standard/deep queries with contextual chunks, BM25, and cosine rerank ([skills/wiki-retrieve/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki-retrieve/SKILL.md), [scripts/retrieve.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/retrieve.py)). The complexity control is procedural and optional: the base path bounds reads by mode; the retrieval path bounds candidate count and chunk size but depends on manual index provisioning.

**Claude Code skills are behavior-shaping artifacts.** The repository ships skill files for setup, ingest, query, lint, fold, save, autoresearch, retrieval, canvas, Obsidian syntax, and methodology modes ([skills/](https://github.com/AgriciDaniel/claude-obsidian/tree/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills), [.claude-plugin/plugin.json](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/.claude-plugin/plugin.json)). These are not passive documentation once installed: they route slash-command behavior, tell agents which files to read/write, impose frontmatter and wikilink conventions, and define update obligations for index, log, and hot cache.

**The implementation adds symbolic governance around a prose vault.** `wiki-lock.sh` provides per-file advisory locking; `allocate-address.sh` assigns stable `c-NNNNNN` page addresses; `wiki-mode.py` routes content into generic, LYT, PARA, or Zettelkasten layouts; `detect-transport.sh` chooses the Obsidian CLI/MCP/filesystem write path; and lint instructions check links, frontmatter, addresses, stale claims, and duplicate-like pages ([scripts/wiki-lock.sh](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/wiki-lock.sh), [scripts/allocate-address.sh](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/allocate-address.sh), [scripts/wiki-mode.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/wiki-mode.py), [skills/wiki-lint/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki-lint/SKILL.md)). Governance is mostly instruction-plus-helper, not a central validator that blocks all writes.

**The hot cache is the main push surface.** `hooks/hooks.json` loads `wiki/hot.md` on `SessionStart`, re-loads it after compaction, defers auto-commit during locks, and prompts for hot-cache update on stop when wiki files changed ([hooks/hooks.json](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/hooks/hooks.json), [hooks/README.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/hooks/README.md)). That gives the next session a coarse recent-context push; deeper memory still depends on query/retrieve/read workflows.

**Trace-derived memory exists, but as manual/agent-mediated distillation rather than automatic preference learning.** `/save` files the current conversation or insight as a structured wiki note, and `wiki-fold` rolls up `wiki/log.md` entries into extractive fold pages ([skills/save/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/save/SKILL.md), [skills/wiki-fold/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki-fold/SKILL.md)). I found no Synapptic-like loop that mines raw tool transcripts into learned user policy or benchmarked rules. The trace-derived outputs are notes and folds created by invoked skills.

## Artifact analysis

- **Storage substrate:** `files` — The standing memory lives in a repository/vault directory: `.raw/`, `wiki/`, `_templates/`, `.vault-meta/`, `.obsidian/`, skill files, command files, hook config, and helper scripts
- **Representational form:** `prose` `symbolic` `parametric` — Prose Markdown wiki pages and skills dominate, with symbolic JSON/YAML frontmatter, Obsidian canvas/base files, shell/Python scripts, JSON indexes, lockfiles, and optional embedding vectors
- **Lineage:** `authored` `imported` `trace-extracted` — Agent-authored wiki and package artifacts, imported `.raw/` sources, derived indexes, and saved/folded conversation or log traces all appear in the retained surfaces
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Wiki pages and sources provide knowledge; skills, commands, hooks, locks, lint, mode/config files, retrieval indexes, and save/fold workflows instruct, gate, route, validate, rank, and distill retained traces

**Wiki pages under `wiki/`.** Storage substrate: Markdown files in the vault, organized by the selected methodology mode and linked with Obsidian wikilinks. Representational form: prose Markdown plus YAML frontmatter, wikilinks, callouts, and optional addresses. Lineage: authored by the agent during scaffold, ingest, query filing, save, autoresearch, and lint workflows; invalidated by source changes, stale claims, broken links, or later contradictory sources. Behavioral authority: mostly knowledge artifacts when queried or read as evidence; they can become system-definition artifacts when `wiki/hot.md`, a `CLAUDE.md` rule, or a host instruction tells the agent to treat them as standing context.

**`.raw/` source material and manifest.** Storage substrate: files under `.raw/`, plus `.raw/.manifest.json`. Representational form: source prose/assets plus symbolic manifest records. Lineage: imported or fetched source material, treated as immutable except for the manifest and address map ([skills/wiki-ingest/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki-ingest/SKILL.md)). Behavioral authority: source evidence and delta-tracking input; it should not directly instruct future agents.

**`wiki/hot.md`.** Storage substrate: a wiki Markdown file. Representational form: prose summary with simple frontmatter. Lineage: overwritten after ingest, significant query exchanges, saves, and session-end maintenance. Behavioral authority: high-leverage knowledge artifact because hooks push it into future sessions as recent context; it is advisory context, not an enforced gate.

**Skill and command packages.** Storage substrate: `skills/*/SKILL.md`, `commands/*.md`, and plugin manifests. Representational form: prose instructions with small symbolic frontmatter/metadata. Lineage: authored package content shipped by the plugin. Behavioral authority: system-definition artifacts for compatible agents: they route invocations, prescribe workflows, constrain writes, and tell agents which retained artifacts to update.

**Hook configuration.** Storage substrate: `hooks/hooks.json` and documentation. Representational form: symbolic JSON plus embedded shell commands and prompt text. Lineage: authored plugin configuration. Behavioral authority: system-definition artifact with prompt and command force: it injects hot cache, clears stale locks, defers auto-commit while locks exist, and reminds the agent to update hot cache.

**Vault metadata and derived indexes.** Storage substrate: `.vault-meta/transport.json`, `mode.json`, locks, address counter, `chunks/`, `bm25/index.json`, `embed-cache.json`, tiling thresholds, and related runtime files. Representational form: symbolic JSON/text/lockfiles, plus distributed-parametric embedding vectors where rerank or tiling caches are populated. Lineage: derived from vault configuration, wiki page bodies, chunking, contextual-prefix generation, BM25 build, local embeddings, or helper-script state. Behavioral authority: routing, ranking, locking, address allocation, and maintenance authority; these files decide what gets read, where new notes are filed, and whether concurrent writes proceed.

**Retrieval pipeline artifacts.** Storage substrate: chunk JSON under `.vault-meta/chunks/`, BM25 index JSON, and embedding cache JSON ([scripts/contextual-prefix.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/contextual-prefix.py), [scripts/bm25-index.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/bm25-index.py), [scripts/rerank.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/rerank.py)). Representational form: mixed symbolic chunk metadata, prose chunks/prefixes, lexical index state, and optional dense embeddings. Lineage: derived from current wiki pages; the retrieval docs say the index is not auto-refreshed on every page change and must be re-run after substantive ingest sessions ([skills/wiki-retrieve/SKILL.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/skills/wiki-retrieve/SKILL.md)). Behavioral authority: ranking and selection authority over which pages/chunks the agent reads for a query. Precision/recall quality is not verified from static code.

**Trace-derived notes and folds.** Storage substrate: saved wiki notes and `wiki/folds/*.md` when committed. Representational form: prose Markdown with frontmatter and child-entry links. Lineage: `/save` derives from the current conversation; `wiki-fold` derives from selected `wiki/log.md` entries and referenced pages. Behavioral authority: saved notes are knowledge artifacts unless later loaded as instructions; folds are compressed knowledge artifacts for future scanning and query context.

**Promotion path.** The system has a soft promotion path from source -> wiki page -> hot-cache/index exposure -> optional chunk index -> query answer or saved/folded synthesis. It does not have a hard promotion ladder from note to validated rule to enforced gate. Authority increases when hooks, skills, or host instruction files load a note, not because the note itself changes type.

## Comparison with Our System

| Dimension | claude-obsidian | Commonplace |
|---|---|---|
| Primary purpose | Agent-maintained Obsidian/Claude Code wiki for personal/project knowledge | Git-native methodology KB with typed artifacts, validation, review, and generated indexes |
| Main retained artifact | Markdown wiki pages, hot cache, source files, skills, vault metadata, optional retrieval indexes | Typed Markdown notes, instructions, ADRs, reviews, source snapshots, reports, indexes |
| Context strategy | Hot cache push plus pull-first query modes and optional chunk retrieval | Search, collection contracts, type specs, indexes, links, skills, validation/review reports |
| Governance | Skill instructions, locks, mode router, manifest, lint guidance, hook auto-commit | Collection contracts, schemas, deterministic validation, semantic review, git diffs, replacement archives |
| Trace use | Manual `/save` and invoked log folds turn conversation/log traces into wiki artifacts | Workshop/library promotion, source review, review reports, validation, and explicit skill workflows |
| Read-back | Both: hook-pushed hot cache plus explicit query/retrieve/read | Mostly pull through `rg`, indexes, links, skills, and reports |

claude-obsidian is a close cousin to Commonplace on substrate and operator ergonomics. Both systems bet on inspectable files, agent-readable procedures, lexical search, and small helper commands rather than opaque service memory. claude-obsidian is more productized for an Obsidian/Claude Code user: install the plugin, run `/wiki`, get a working vault, and let the hot cache and slash commands carry everyday memory work.

The main divergence is artifact authority. Commonplace makes the collection/type contract central: a note's role, required sections, validation surface, and review lifecycle are part of the artifact. claude-obsidian relies more on broad skill instructions and Obsidian conventions. That lowers adoption friction, but it means high-authority behavior depends on whether the right skill/hook/host loads a prose artifact rather than on a local typed lifecycle.

claude-obsidian's optional retrieval stack is more ambitious than Commonplace's current plain search path, especially contextual prefixing and rerank caches. The tradeoff is lineage drift: if wiki pages change and the chunk/BM25/embed indexes are stale, the derived retrieval authority can point the agent at old or partial views. The code and docs acknowledge manual refresh; Commonplace should treat that as the key governance cost of introducing derived search indexes.

**Read-back:** `both` — `wiki/hot.md` is pushed by session/compaction hooks, while deeper wiki memory is pulled through explicit `wiki-query`, `wiki-retrieve`, page reads, index scans, and save/fold workflows.

### Borrowable Ideas

**Use a bounded hot-cache push for recent context.** Commonplace could borrow a small generated "recent work" context surface for long-running workshops. Ready only if it has an explicit update owner and expiry rule; otherwise it becomes stale high-salience context.

**Treat retrieval indexes as derived artifacts with visible lineage.** claude-obsidian's chunk records carry page path, address, body hash, prefix source, and timestamps. A Commonplace search layer should expose equivalent derivation state rather than hiding retrieval behind a black box. Ready when there is a real search bottleneck.

**Make write concurrency explicit even for file-first systems.** `wiki-lock.sh` is a practical reminder that plain files are not automatically safe under parallel agents. Commonplace already has git discipline, but per-artifact write locks may matter for batch ingest or generated report workflows. Needs a demonstrated concurrent-write use case.

**Keep method modes as routing policy, not separate implementations.** `wiki-mode.py` centralizes generic/LYT/PARA/Zettelkasten routing so skills do not each fork their own path logic. Commonplace's collection routing already serves this role; the borrow is the small executable router when human prose contracts are not enough.

**Do not borrow implicit authority for ordinary notes.** claude-obsidian can make any wiki page behavior-shaping if a skill reads it. Commonplace should preserve stronger distinctions between knowledge artifacts, instructions, validators, and review gates.

## Trace-derived learning placement

- **Trace source:** `session-logs` — `/save` uses the current conversation, and `wiki-fold` uses `wiki/log.md` entries rather than raw Claude Code tool transcripts
- **Learning scope:** `per-project` `cross-task` — Distilled notes and folds are vault-local project/personal memory that can affect later sessions and tasks
- **Learning timing:** `online` `offline` `staged` — `/save` can run during or after a conversation, while `wiki-fold` is invoked over a selected log range and is dry-run by default
- **Distilled form:** `prose` `symbolic` — Outputs are Markdown notes and folds with frontmatter, links, addresses, and child-entry citations

**Trace source.** claude-obsidian qualifies as trace-derived in a limited, agent-mediated sense. `/save` uses the current conversation as source material for a durable note. `wiki-fold` uses `wiki/log.md` entries, and sometimes referenced child pages, as source material for extractive fold pages. These are traces of prior agent/user operations, not raw Claude Code JSONL tool transcripts.

**Extraction.** Extraction is mostly LLM/operator judgment under skill instructions. `/save` asks the agent to identify valuable content, choose a note type, rewrite the conversation into declarative present-tense knowledge, and update index/log/hot cache. `wiki-fold` is stricter: it requires extractive summarization, child-entry citations, bounded reads, duplicate detection, and count checks. The oracle is therefore instruction-constrained agent judgment, with human invocation and review as the main curation policy.

**Scope and timing.** Scope is vault-local. `/save` can operate during or after a conversation; `wiki-fold` is invoked over a selected recent log range and is dry-run by default. Neither path is automatic online learning from every turn. The output can affect later sessions only after it is filed and then read, indexed, folded, or hot-cache summarized.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), claude-obsidian belongs in the manual/agent-mediated trace-to-prose family, not the automatic transcript-mining or weight-learning family. It weakens any claim that trace-derived memory must be autonomous: useful trace distillation can be invoked, extractive, and file-native. It also splits raw traces from distilled artifacts: conversation/log material is source evidence; saved notes and folds are the durable behavior-shaping candidates.

## Read-back placement

**Direction.** Both. `wiki/hot.md` is pushed at session start and after compaction through hooks. The rest of the wiki is primarily pull: the agent invokes query/retrieve/read workflows, scans indexes, or follows wikilinks.

**Read-back signal:** `coarse` — The push side loads `wiki/hot.md` for a vault/session and is not instance-targeted to the current user request.

**Read-back timing:** `pre-action` — Session-start and post-compaction hot-cache read-back arrive before the receiving session or resumed context takes subsequent actions.

**Faithfulness tested:** `no` — The review found no implemented ablation or faithfulness test proving that hot-cache injection or retrieval candidates change final agent behavior.

**Targeting and signal.** The push side is `coarse`: if a session is in a vault with `wiki/hot.md`, the hook loads the recent-context cache. It is not instance-targeted to the current user request. The pull side can be instance-relevant because the agent's query text drives hot/index/page selection or optional BM25/rerank retrieval. That pull signal is inferred lexical/semantic relevance, not symbolic push.

**Timing relative to action.** Hot-cache read-back happens before the agent's session or resumed context acts. PostCompact re-loads after context compaction but before subsequent actions. Save/fold updates happen after a conversation or log range and can only influence future sessions.

**Selection, scope, and complexity.** Hot cache is deliberately small, about 500 words by convention. Query modes bound deeper reads by quick/standard/deep workflows. Optional retrieval uses chunking, BM25 top-k candidates, dedupe by page address, and optional cosine rerank. The strongest context-efficiency risk is derived-index staleness: if the chunk/BM25/embed state is not rebuilt after wiki changes, selection can lag the source.

**Authority at consumption.** Hot-cache push is advisory context. Skill files and commands have stronger instruction authority because the agent executes their workflow. Retrieval indexes have ranking authority over candidate pages. There is no implemented ablation or faithfulness test proving that hot-cache injection or retrieval candidates change final agent behavior.

**Other consumers.** Humans use the same vault through Obsidian, Dataview, graph/canvas views, dashboards, lint reports, and normal file/git tooling. Some memory artifacts, such as canvases and dashboard bases, are primarily human navigation surfaces that also give agents structure to read.

## Curiosity Pass

**The most behavior-shaping artifact may be a hook, not a note.** `wiki/hot.md` is just Markdown, but `hooks/hooks.json` is what turns it into automatic context. The authority lives in the consumption path.

**The optional retrieval layer is more governed than many RAG add-ons, but still manually refreshed.** It records hashes and prefix sources, gates off-machine prefixing behind consent, and degrades gracefully. It does not automatically rebuild after every write at this commit.

**The system explicitly forbids some nested-agent authority but still ships agent definitions.** Parallel ingest agents are documented, but they must not allocate addresses or update shared indexes/log/hot cache; the orchestrator owns those surfaces ([agents/wiki-ingest.md](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/agents/wiki-ingest.md)). That is a useful separation of page-level work from shared-state mutation.

**`contextual-prefix.py` contains a `claude -p` subprocess tier.** It is consent-gated in the reviewed source and not part of normal query execution unless setup/rebuild chooses it, but it is a real nested-agent CLI path inside the project ([scripts/contextual-prefix.py](https://github.com/AgriciDaniel/claude-obsidian/blob/cb93ff6d82f9c35a08bf6010e7fac36dfddc827b/scripts/contextual-prefix.py)). For this review I did not run it.

**The README's autonomous language is mostly agent-procedural.** Ingest, lint, autoresearch, and save can create many pages, but the core mechanism is still an LLM following skill instructions with helper scripts. There is no always-on background knowledge worker except host hooks.

## What to Watch

- Whether `wiki-retrieve` gains automatic index refresh after writes. That would strengthen read-back but raise derived-artifact invalidation and hook-cost questions.
- Whether `wiki-fold` grows fold-of-folds or automatic scheduling. That would turn trace-derived summarization from invoked maintenance into a standing memory compaction layer.
- Whether lint gains hard blocking behavior. That would move governance from advisory reports toward Commonplace-like validation authority.
- Whether hot-cache update becomes verifiable rather than prompt-reminded. A stale pushed cache is more dangerous than a stale pull-only note because it arrives without a query.
- Whether methodology modes get schema-specific validators. That would make LYT/PARA/Zettelkasten more than routing conventions.
- Whether the plugin relies more on external agent CLIs for prefixing or verification. The existing consent gate is important because those paths send vault content off-machine.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - frames: claude-obsidian's hot-cache hook is a concrete storage-to-context activation path, while deeper wiki pages remain pull-dependent.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: the same Markdown file changes authority depending on whether it is source evidence, hot-cache context, skill instruction, or indexed retrieval candidate.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - applies: mode routing, path routing, hooks, and query-time retrieval all depend on symbols or inferred query relevance already available to the agent.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: wiki pages, sources, saved notes, folds, dashboards, and query answers mostly serve as evidence/context/advice.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: skills, commands, hooks, helper scripts, locks, indexes, and mode/config files shape future agent behavior through instruction, routing, ranking, validation, or trigger authority.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: claude-obsidian is primarily a routing/loading system for Obsidian-backed knowledge under bounded context.
