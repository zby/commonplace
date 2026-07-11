---
description: "WUPHF review: local multi-agent office with git-backed markdown wiki, per-agent notebooks, fact extraction, learning logs, lint, and cited lookup"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
tags: [trace-derived]
---

# WUPHF

WUPHF, from `nex-crm/wuphf`, is a local multi-agent "office" that runs headless Claude/Codex-style teammates through a broker, scoped MCP tools, per-agent worktrees, and a shared UI. Its memory system is the markdown backend: a local git wiki at `~/.wuphf/wiki/`, per-agent notebooks, append-only fact and learning logs, derived SQLite/Bleve indexes, extraction/synthesis prompts, lint, and review/promotion workflows.

**Repository:** https://github.com/nex-crm/wuphf

**Reviewed commit:** [fa7449550ce42c8f163a5f78388751a92937bfc6](https://github.com/nex-crm/wuphf/commit/fa7449550ce42c8f163a5f78388751a92937bfc6)

**Last checked:** 2026-06-05

## Core Ideas

**The office is push-driven but model sessions are fresh.** The architecture doc says the broker wakes agents on messages, builds a per-agent prompt plus scoped MCP manifest, and runs a fresh headless provider process per turn instead of resuming a growing chat session ([ARCHITECTURE.md](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/ARCHITECTURE.md), [internal/team/launcher.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/launcher.go)). Persistent behavior therefore lives in channel/task state, worktrees, prompts, tools, and memory artifacts, not in provider-side conversation history.

**The default memory substrate is a git-native markdown wiki.** The README presents every agent notebook and the shared wiki as local markdown in `~/.wuphf/wiki/`; the schema makes markdown the source of truth and treats SQLite, Bleve, and other indexes as rebuildable caches ([README.md](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/README.md), [docs/specs/WIKI-SCHEMA.md](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/docs/specs/WIKI-SCHEMA.md), [internal/team/wiki_index.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_index.go)).

**Writes are serialized through a single wiki worker.** Wiki articles, notebook entries, raw artifacts, fact logs, learnings, lint reports, playbook executions, and archive sweeps all route through the `WikiWorker` queue, preserving the single-writer invariant for one git repository and surfacing queue saturation instead of silently retrying ([internal/team/wiki_worker.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_worker.go), [internal/team/notebook_worker.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/notebook_worker.go)).

**Notebook-to-wiki promotion is reviewed.** Agents can write draft entries only under their own notebook path, but any agent can read/search notebooks. Durable shared knowledge is supposed to move through `notebook_promote`, review state, and `Repo.ApplyPromotion`, which copies the notebook body into `team/...` and stamps the source entry with promotion metadata ([internal/teammcp/notebook_tools.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/teammcp/notebook_tools.go), [internal/team/promotion_commit.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/promotion_commit.go)).

**Context efficiency comes from fresh turns, scoped tools, retrieval caps, and compiled indexes.** WUPHF avoids session-history growth, registers a smaller MCP surface by mode and backend, defaults to explicit memory lookups/searches, and caps `/lookup` retrieval with top-k facts before a cited-answer prompt ([internal/teammcp/server.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/teammcp/server.go), [internal/team/wiki_query.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_query.go), [internal/team/wiki_query_retrieve.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_query_retrieve.go)). It reduces context volume but still relies on agent behavior and prompt instructions to decide when to search.

**Governance is layered rather than purely retrieval-based.** Direct wiki writes require a verified recent human request unless an admin bypass is enabled; lint detects contradictions and lets users mark winners; read logs support archival; team learnings validate type/source/confidence and reject instruction-like insights ([internal/teammcp/server_wiki_tools.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/teammcp/server_wiki_tools.go), [internal/team/wiki_lint.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_lint.go), [internal/team/wiki_archiver.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_archiver.go), [internal/team/learnings.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/learnings.go)).

## Artifact analysis

- **Storage substrate:** `repo` `files` `sqlite` — The canonical markdown backend is a git repository rooted at `~/.wuphf/wiki/`; notebooks, wiki pages, artifacts, fact JSONL, learning JSONL, lint reports, read telemetry, backups, and generated pages live as files, while `NewPersistentWikiIndex` can store derived facts in SQLite and text search in Bleve under `.wuphf/index/` ([internal/team/wiki_git.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_git.go), [internal/team/wiki_index.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_index.go)).
- **Representational form:** `prose` `symbolic` `parametric` — Wiki articles, notebooks, prompts, briefs, skills, lint reports, and learning prose are prose; YAML frontmatter, JSONL facts/learnings, triplets, indexes, redirects, queues, review state, MCP schemas, and git commits are symbolic; notebook clustering can use embeddings, and legacy GBrain/Nex or optional index code may add vector-like retrieval state ([internal/team/wiki_query.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_query.go), [internal/team/notebook_signal_scanner.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/notebook_signal_scanner.go), [internal/team/notebook_signal_scanner_embeddings.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/notebook_signal_scanner_embeddings.go)).
- **Lineage:** `authored` `imported` `trace-extracted` — Users and agents author notebooks, wiki pages, learnings, playbooks, and skills; onboarding and artifact paths import source material into the wiki; raw artifacts and repeated notebook/self-heal signals can be extracted into facts, briefs, learning rows, and skill proposals ([internal/team/artifact_commit.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/artifact_commit.go), [internal/team/wiki_extractor.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_extractor.go), [internal/team/skill_synthesizer.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/skill_synthesizer.go)).
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Wiki pages, facts, notebooks, artifacts, and read results are knowledge context; prompt blocks, compiled skills, playbooks, and MCP tool descriptions instruct agents; delegation checks, path validators, review states, task memory workflow, lint resolution, safety guards, and queue limits enforce; query classes, graph walks, slug signals, launch targeting, and tool registration route behavior; BM25, typed retrieval, demand scores, confidence, trust, read stats, and clusters rank; extraction, synthesis, learnings, and skill proposals learn from retained material.

**Wiki articles and fact logs.** The schema's three-layer model separates immutable raw artifacts from LLM-owned wiki pages, append-only fact logs, lint reports, redirects, graph logs, playbooks, and the schema itself ([docs/specs/WIKI-SCHEMA.md](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/docs/specs/WIKI-SCHEMA.md)). The index can be rebuilt from markdown and JSONL, so the derived search layer is an access structure, not the source of truth.

**Notebooks.** Notebook entries are per-agent draft memory under `agents/{slug}/notebook/...` for `notebook_write`, while reads/searches are cross-agent. They have weak authority until promoted, but they feed demand, review, context workflow, and possibly skill-synthesis surfaces ([internal/team/notebook_worker.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/notebook_worker.go), [internal/team/broker_notebook_review.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/broker_notebook_review.go)).

**Learning log.** `team_learning_record` appends validated JSONL and regenerates a human-readable `team/learnings/index.md`; search deduplicates, filters, computes effective confidence, and returns evidence-like learning records ([internal/teammcp/learning_tools.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/teammcp/learning_tools.go), [internal/team/learnings.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/learnings.go)).

**Promotion path.** WUPHF has several promotion ladders: notebook draft -> review candidate -> team wiki article; artifact -> extracted fact/entity -> fact log and brief; wiki/playbook article -> compiled skill; repeated notebook/self-heal signals -> skill candidate -> LLM-synthesized skill proposal. These are meaningful authority transitions, but they are unevenly governed: notebook promotion has explicit review, while artifact extraction and Stage B skill synthesis rely more on prompts, guards, and proposal status.

## Comparison with Our System

WUPHF and Commonplace both treat a git-backed markdown knowledge base as agent-operable memory, but they optimize for different loops. Commonplace is a methodology KB with typed notes, collection contracts, validation, and review gates. WUPHF is an operational multi-agent workplace where memory is one subsystem among broker routing, worktrees, UI, MCP tools, tasks, integrations, and skill compilation.

The strongest alignment is the substrate choice: markdown remains inspectable, git history matters, indexes are rebuildable, and artifacts are separated by authority. WUPHF's divergence is that it tries to make the KB active inside an office product: agents get scoped memory tools, humans get a wiki UI and maintenance suggestions, and background loops can extract facts, synthesize briefs, lint contradictions, promote notebooks, and propose skills.

The main risk is authority drift. WUPHF has many paths that can turn notes into behavior-shaping objects, but not all paths preserve the same level of provenance and review. Commonplace would treat that as a collection/type-contract issue first; WUPHF often encodes the contract in code comments, prompts, handler validation, and workflow state.

### Borrowable Ideas

**Single queue for all git-backed writes.** Commonplace could borrow the explicit single-writer queue for any future UI or agent service that writes notes, generated indexes, reviews, and telemetry into one repository. Ready now if Commonplace grows a long-running server.

**Notebook as weak-authority draft memory.** WUPHF's notebook/write/read/promote split is a useful operational pattern: private-by-convention scratch can be searchable without becoming canonical. Ready as a design pattern; implementation should wait for a concrete multi-agent workflow.

**Human-request token for direct canonical writes.** Requiring a recent human message ID for direct wiki writes is a practical guard against agents bypassing review. Commonplace could adapt this for any external UI that lets agents write canonical notes.

**Learning records separate from wiki claims.** `team_learning_record` keeps compact lessons in a typed log instead of letting every lesson become a full wiki page or instruction. Commonplace could use a similar low-friction log for repeated operational learnings that are not yet notes.

**Cited-answer lookup as a wiki reader.** WUPHF's `/lookup` path gives an answer plus citations over top-k indexed facts. Commonplace could borrow this as a read tool only after source/citation contracts are strict enough to avoid answer-shaped hallucination.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents manually write notebooks, wiki articles, learnings, playbooks, visual artifacts, and promotion requests through MCP/UI/HTTP tools; automatic paths initialize/recover the wiki repo, regenerate catalogs, reconcile indexes, extract facts from artifacts, synthesize briefs and skills, run lint, archive stale pages, record reads, and update fact/log state.

**Curation operations:** `dedup` `consolidate` `evolve` `synthesize` `invalidate` `decay` `promote` — Entity resolution and fact reinforcement dedup repeated extracted facts; entity synthesis and generated learning pages consolidate records into readable surfaces; fact mutation, brief synthesis, skill enhancement, and index reconciliation evolve existing artifacts; Stage B skill synthesis and entity briefs synthesize new prose from stored signals; lint resolution, `valid_until`, supersedes, archive tombstones, DLQ retirement, and review state invalidate stale or failed records; archival and effective-confidence scoring decay low-value memory; notebook promotion, skill proposal writing, and playbook compilation promote lower-authority material into stronger artifacts.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` — Qualifying traces include raw wiki artifacts such as chat/meeting/email/manual records, agent-authored notebook captures, playbook execution records, task/self-heal incidents, and repeated cross-agent notebook patterns. The old automatic fan-out from every message/task transition is explicitly disabled, so not every office event becomes durable memory automatically ([internal/team/auto_notebook_writer.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/auto_notebook_writer.go), [internal/team/artifact_commit.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/artifact_commit.go)).

**Extraction.** Raw artifacts trigger `ExtractFromArtifact`, which reads the committed artifact, renders `extract_entities_lite`, asks the configured provider for JSON, resolves entities, computes deterministic fact IDs, merges reinforcement, updates the index, persists JSONL fact logs, and creates ghost briefs. Notebook clusters and self-heal incidents feed `SkillCandidate` values into Stage B, where an LLM synthesizes or enhances skills subject to dedup and safety guard checks ([internal/team/wiki_extractor.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_extractor.go), [internal/team/stage_b_signals.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/stage_b_signals.go), [internal/team/skill_synthesizer.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/skill_synthesizer.go)).

**Learning scope:** `per-project` `cross-task` — The wiki and learning log are local-office/project memory, and learnings can be scoped by repo, file, playbook, task, entity, or global-like keys.

**Learning timing:** `online` `offline` `staged` — Artifact extraction runs asynchronously after artifact commits; `/lookup`, learning search, and notebook search happen during use; lint, archive, skill compile, promotion sweep, and boot reconcile are cron/event/reconcile-style maintenance.

**Distilled form:** `prose` `symbolic` `parametric` — Distilled artifacts include prose briefs, wiki pages, learning descriptions, lint reports, and skills; symbolic JSONL facts, triplets, YAML, review state, and compiled skill metadata; and embedding-backed notebook clustering when enabled.

**Survey fit.** WUPHF is a broad trace-to-KB and trace-to-skill system, but its strongest trace-derived claim is not automatic capture of all chat. It is the staged path from explicitly retained artifacts and notebook/workflow signals into facts, briefs, learning records, skill candidates, and reviewable/promotable team knowledge.

## Read-back

**Read-back:** `both` — Agents can explicitly pull memory through notebook, wiki, learning, context, and legacy memory tools; WUPHF also pushes selected memory or memory obligations into agent turns through prompt blocks and broker-built notifications, and `/lookup` pushes retrieved wiki sources into a cited-answer LLM call before the answer is returned.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` `inferred / judgment` — Coarse prompt blocks tell agents that markdown memory is active and how to use it; identifier signals include backend, channel, slug, task_id, path, scope, file, playbook, and entity filters; lexical search covers notebook/wiki/learning queries and BM25; judgment appears in query classification, cited-answer generation, extraction, lint contradiction judgment, and skill synthesis.

**Faithfulness tested:** `no` — The repository has tests for retrieval routes, prompt parsing, lint, tool registration, workflow state, and evaluation harnesses, but I did not find a with/without-memory ablation or post-action audit proving that pushed or retrieved memory changed an agent's later behavior faithfully.

**Direction edge cases.** MCP `team_wiki_read`, `team_wiki_search`, `notebook_search`, `team_learning_search`, and `wuphf_wiki_lookup` are pull tools from the calling agent's perspective. The broker-side `/lookup` endpoint is push to the answer model because retrieval and prompt assembly occur inside the handler after a human or agent asks a question. For normal headless agent turns, broad memory guidance is push, while specific wiki/notebook facts mostly depend on the agent choosing a tool.

**Selection, scope, and complexity.** `/lookup` defaults to top 20 facts, classifies the query, uses typed graph walks for specific query classes, falls back to BM25, hydrates fact sources, and prompts an answer model with source snippets ([internal/team/wiki_query.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_query.go), [internal/team/wiki_query_retrieve.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/wiki_query_retrieve.go), [prompts/answer_query.tmpl](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/prompts/answer_query.tmpl)). Tool schemas are mode/backend-scoped, which helps prompt size, but actual relevance and context dilution remain runtime qualities rather than code-proven facts.

**Authority at consumption.** Retrieved wiki facts and articles are advisory evidence in answers and agent work. Compiled skills, playbooks, prompt blocks, task workflow gates, and MCP tool descriptions have stronger instruction/routing force. Lint and review surfaces can gate or mutate retained artifacts, but they do not prove downstream model obedience.

**Other consumers.** Humans consume the web wiki, article editor, review UI, lint findings, read history, visual artifacts, and channel messages. The broker consumes the same repo for index reconcile, boot recovery, archives, skill compilation, and UI events.

## Curiosity Pass

**The repo contains a visible path tension around notebooks.** `notebook_write` and promotion code use `agents/{slug}/notebook/...`, while the Stage B notebook scanner's constants describe `team/agents/...`. That may mean the scanner targets a different notebook lineage or a stale path convention; I would not treat notebook-cluster skill synthesis as fully proven end-to-end without a targeted test at this commit ([internal/team/notebook_worker.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/notebook_worker.go), [internal/team/skill_scanner.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/skill_scanner.go), [internal/team/notebook_signal_scanner.go](https://github.com/nex-crm/wuphf/blob/fa7449550ce42c8f163a5f78388751a92937bfc6/internal/team/notebook_signal_scanner.go)).

**The source-of-truth story is stronger than the activation story.** WUPHF works hard to make markdown/git reconstructable and attributable. The code is less able to prove that an agent searched before acting, used the retrieved memory, or changed behavior because of it.

**Direct wiki write is intentionally uncomfortable.** The direct `team_wiki_write` path requires a human-request ID, nudging agents toward notebook capture plus review. That is a good authority boundary for a system with many autonomous agents.

**Extraction failures do not fail artifact commits.** This protects raw evidence, but it also means a user can have an apparently successful capture whose structured facts are delayed in DLQ. The review should treat raw artifact retention and fact availability as separate stages.

## What to Watch

- Whether notebook path conventions converge between `agents/...` and `team/agents/...`; this determines whether notebook-cluster skill synthesis is a live learning path or a partially stale implementation.
- Whether `/lookup` or agent turns gain a memory-use audit, ablation, or post-action citation check; that would change the faithfulness verdict.
- Whether extracted facts gain stronger source-span provenance and prompt-version lineage in every durable output, especially generated briefs and skills.
- Whether direct team learnings remain evidence records rather than becoming prompt-control instructions through later prompt assembly.
- Whether review/promotion state becomes mandatory for all generated skills and wiki claims, not only notebook-originated articles.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: WUPHF stores rich memory, but only tool calls, prompt blocks, `/lookup`, and generated skills make it affect a future action.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: WUPHF's wiki pages, notebooks, fact logs, learning rows, skills, indexes, prompts, and review state carry different substrates, forms, lineage, and authority.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: WUPHF extracts facts and skill candidates from retained artifacts, notebooks, and self-heal traces.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: wiki articles, notebook entries, raw artifacts, citations, facts, and learnings mostly advise until read or promoted.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompt blocks, MCP tool schemas, compiled skills, lint rules, validators, and review workflows instruct, route, validate, rank, or enforce behavior.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains: WUPHF's targeted read-back relies on paths, slugs, task ids, scopes, query classes, and typed predicates being available as symbols or inferred from query text.
