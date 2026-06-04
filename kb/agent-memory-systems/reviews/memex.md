---
description: "Memex review: isolated Claude Code daemon that turns raw sources into a persistent Markdown wiki with SQLite queues, prompts, and pull-only wiki read-back"
type: ../types/agent-memory-system-review.md
status: current
last-checked: "2026-06-03"
---

# Memex

Memex, from wastedcode's `wastedcode/memex` repository, is a TypeScript CLI and privileged daemon for running Claude Code against isolated per-wiki workspaces. At the reviewed commit, its memory system is not vector RAG or an embedding store. It copies user-supplied raw sources into a wiki-local archive, runs `claude -p` inside a Linux mount namespace, and asks Claude to maintain a durable Markdown wiki with schema, index, activity log, cross-links, source references, query answers, and lint fixes.

**Repository:** https://github.com/wastedcode/memex

**Reviewed commit:** [1e223b6045be31b70b1ab9e4b28dd403150d29e7](https://github.com/wastedcode/memex/commit/1e223b6045be31b70b1ab9e4b28dd403150d29e7)

**Last checked:** 2026-06-03

## Core Ideas

**The durable memory is an LLM-maintained Markdown wiki.** `WikiScaffold.create()` seeds each wiki with `.claude.md`, `wiki/_schema.md`, `wiki/_index.md`, `wiki/_log.md`, and `wiki/raw/`; the system prompt then makes `_schema.md` the agent's "institutional memory," `_index.md` the map, `_log.md` the operation record, and ordinary Markdown pages the knowledge layer ([src/daemon/scaffold.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/scaffold.ts), [src/lib/prompts/wiki.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/wiki.ts)). The README's "just files, no RAG" claim is materially true for the central retained knowledge artifact ([README.md](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/README.md)).

**A daemon owns scheduling, isolation, and persistence around Claude Code.** The CLI talks JSON over a Unix socket to `memex serve`; the daemon persists wikis, jobs, and audit rows in SQLite, drains one FIFO queue per wiki, and runs independent wikis in parallel while serializing writes within a wiki ([src/daemon/db.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/db.ts), [src/daemon/queue.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/queue.ts), [src/daemon/routes.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/routes.ts)). This is scheduler state, not semantic memory, but it is what prevents concurrent LLM writes from racing over the same wiki.

**Context efficiency is delegated to filesystem navigation and prompt discipline.** Memex does not precompute embeddings, summaries, or ranked retrieval packs. Ingest prompts tell Claude to read raw files, `_schema.md`, `_index.md`, and then search related pages; query prompts tell Claude to read `_index.md`, grep/glob for relevant files, and read the files that matter ([src/lib/prompts/ingest.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/ingest.ts), [src/lib/prompts/query.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/query.ts)). Volume is bounded mainly by Claude Code's own file-tool choices, job `max_turns`, and timeout settings; complexity is reduced by insisting on a maintained index and schema, but broad grep/read behavior can still expand until the model spends too much context on navigation.

**The prompts are the behavioral core.** The architecture and prompt docs explicitly treat the prompt as product, and the source backs that up: `ClaudeRunner` appends `getWikiSystemPrompt()` on every job while job-specific prompt builders define ingest, query, and lint behavior ([docs/prompts.md](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/docs/prompts.md), [src/daemon/runner.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/runner.ts), [src/lib/prompts/wiki.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/wiki.ts)). The prompt asks the LLM to maintain bidirectional links, update contradictions, preserve source references, keep the index current, and evolve filing conventions.

**Raw sources are preserved separately from synthesized wiki pages.** `memex ingest` uploads each local file to the daemon; `WikiScaffold.writeRawFile()` stores it under `wiki/raw/` with a timestamp prefix; the namespace wrapper bind-mounts `wiki/raw/` read-only inside `/workspace` ([src/cli/commands/ingest.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/cli/commands/ingest.ts), [src/daemon/scaffold.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/scaffold.ts), [src/daemon/namespace.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/namespace.ts)). The intended lineage is clear: raw sources are source material; wiki pages are derived synthesis.

**Safety is architectural but narrow.** The runner executes `claude -p` through `unshare -m`, bind-mounts only the wiki directory at `/workspace`, sets `HOME` to `/workspace`, filters environment variables, and restricts Claude's tools to `Read`, `Write`, `Edit`, `Glob`, and `Grep` plus a small whitelist of optional extras ([src/daemon/namespace.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/namespace.ts), [src/daemon/runner.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/runner.ts), [src/lib/constants.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/constants.ts)). The tradeoff is operational: the daemon needs Linux namespace support and `CAP_SYS_ADMIN`.

## Artifact analysis

- **Storage substrate:** `files` — The central retained knowledge is a per-wiki filesystem tree of Markdown pages and raw source files; SQLite stores registry, queue, and audit metadata around that filesystem.
- **Representational form:** `prose` `symbolic` — Memex combines prose Markdown pages and prompts with symbolic SQLite rows, command schemas, tool allowlists, filesystem layout, and JSON job results.
- **Lineage:** `authored` `imported` — Wiki pages are Claude-authored derivatives of imported raw sources and existing wiki state; prompts, scaffold files, daemon policy, and per-wiki conventions are authored system-definition artifacts.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` — Wiki pages and raw sources provide knowledge context; prompts, schema/index conventions, queues, namespace policy, and tool allowlists instruct, route, schedule, and enforce future Claude runs.

**Wiki Markdown pages.** Storage substrate: files under `/var/lib/memex/wikis/{wikiId}/wiki/` by default, exposed to Claude as `/workspace/wiki/` inside a per-job mount namespace ([src/lib/constants.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/constants.ts), [src/daemon/namespace.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/namespace.ts)). Representational form: prose Markdown with symbolic file paths, headings, source references, and `## Related` links. Lineage: derived by Claude from raw sources, query work, lint maintenance, and existing wiki state; invalidated by source changes, prompt changes, or later contradictions. Behavioral authority: knowledge artifacts when query jobs cite them as evidence; weak system-definition artifacts when `_schema.md`, `_index.md`, or a page convention tells the next Claude run how to file and interpret material.

**Raw source archive.** Storage substrate: files under `wiki/raw/`, named with a timestamp and sanitized basename. Representational form: mixed, because Memex accepts whatever Claude can read: Markdown, PDF, HTML, text, images, and other local documents. Lineage: imported from user-provided files by `memex ingest`; the namespace wrapper remounts this directory read-only for Claude, so raw sources are intended as immutable evidence. Behavioral authority: source evidence for wiki synthesis, not direct instruction unless the prompt and Claude decide to read and interpret a source.

**Schema, index, and log.** Storage substrate: Markdown files seeded in every wiki. Representational form: mixed prose and symbolic conventions: `_schema.md` names categories and filing rules, `_index.md` maps every page to a summary, and `_log.md` records operations. Lineage: initially scaffolded, then maintained by Claude under ingest and lint prompts. Behavioral authority: `_schema.md` and `_index.md` have routing and instruction-like authority because prompts require Claude to consult them before filing or answering; `_log.md` is primarily audit evidence and is not a strong read-back surface in the inspected prompts.

**Prompt files and wiki conventions.** Storage substrate: authored TypeScript prompt builders plus per-wiki `.claude.md`. Representational form: prose instructions embedded in code and editable Markdown. Lineage: package-authored baseline prompt plus user-authored wiki-specific conventions; prompt changes alter all future jobs. Behavioral authority: system-definition artifacts with direct instruction force through `--append-system-prompt`, job prompts, and Claude Code's auto-discovered `.claude.md`.

**SQLite registry, queue, and audit log.** Storage substrate: `better-sqlite3` database at `MEMEX_DATA_DIR/memex.db`, with `wikis`, `queue_jobs`, and `audit_log` tables ([src/daemon/db.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/db.ts)). Representational form: symbolic relational state. Lineage: created and updated by daemon routes and queue manager; running jobs are reset to pending on startup. Behavioral authority: scheduling, ownership, job recovery, and operational audit authority; it decides when Claude runs, for which wiki, under which job payload.

**Namespace, auth, and tool policy.** Storage substrate: TypeScript daemon code, `.claude/` credential files, `.tools/allowed-tools.txt`, and optional `.tools/mcp.json`. Representational form: symbolic executable policy plus JSON/text configuration. Lineage: package-authored policy with per-wiki user edits. Behavioral authority: enforcement and capability authority over what Claude can see, which credentials it uses, and which tools exist in a job.

**Promotion path.** Memex's main promotion path is raw source -> Claude-derived wiki page -> schema/index/log updates -> later query or ingest context. It has no deterministic type validation or review gate for promoting a page from evidence to instruction. Authority increases when the LLM writes a convention into `_schema.md` or a navigation entry into `_index.md`, but that promotion is prompt-governed rather than independently checked.

## Comparison with Our System

| Dimension | Memex | Commonplace |
|---|---|---|
| Primary purpose | Personal/source-fed wiki maintained by Claude Code jobs | Git-native methodology KB with typed artifacts, validation, reviews, and indexes |
| Main retained artifact | Per-wiki Markdown pages, schema, index, log, raw archive | Typed Markdown notes, instructions, ADRs, reviews, source snapshots, reports, indexes |
| Runtime boundary | Privileged daemon, Unix socket, mount namespace, queued `claude -p` jobs | Repo-local command and skill workflows run by agents/operators in the existing worktree |
| Context strategy | Prompted filesystem search/read over `_index.md`, `_schema.md`, and wiki pages | `rg`, collection contracts, authored links/indexes, generated indexes, validation/review reports |
| Governance | Prompt conventions, read-only raw archive, serial queues, lint prompt, tool allowlist | Type specs, schemas, deterministic validation, semantic review, replacement archives, curated navigation |
| Learning loop | LLM integrates external sources into a living wiki | Deliberate source/review/write workflows with explicit validation and review gates |

Memex and Commonplace share the file-first bet: knowledge should remain inspectable as Markdown and should be maintained as a durable artifact outside the chat transcript. Memex pushes that bet further into runtime product design. It wraps Claude Code itself, isolates a workspace, queues jobs, and treats the LLM as the wiki's standing curator.

The main divergence is governance. Memex uses prompts as the control plane: schema ownership, bidirectional links, contradiction handling, source references, and lint fixes are all instructions to Claude. Commonplace codifies more of the lifecycle into collection contracts, type specs, schemas, validation commands, review artifacts, and git history. Memex is simpler to use as a personal compounding wiki, but its strongest quality guarantees are only as reliable as the current prompt and model behavior.

Memex also has a different stance on context efficiency. Commonplace relies on external agents using indexes, `rg`, and type boundaries carefully. Memex gives Claude a smaller sandbox and a maintained `_index.md`, but still asks the same LLM to perform most selection work through filesystem tools. That avoids embedding/index infrastructure, but it makes context quality sensitive to wiki size, prompt compliance, and whether `_index.md` stays useful.

**Read-back:** `pull` — Retained memory reaches Claude when a job prompt tells it to read `_schema.md`, `_index.md`, search with `Grep`/`Glob`, and `Read` selected wiki files; Memex does not implement unsolicited relevance-triggered memory injection into an already-running agent.

### Borrowable Ideas

**Use a raw/source layer with filesystem-enforced immutability.** Commonplace already snapshots sources, but Memex's read-only `raw/` mount is a clean runtime boundary: the agent can cite evidence while being structurally unable to rewrite it. Ready as an architectural pattern for source-facing agent sandboxes, not necessarily for the current repo workflow.

**Serialize writes per knowledge base.** Memex's per-wiki queues solve a real coordination problem: two LLM jobs should not concurrently mutate the same wiki. Commonplace could borrow this for long-running automated maintenance or review sweeps. Needs a concrete concurrent-writer workflow before adding scheduler machinery.

**Treat schema/index maintenance as a first-class job responsibility.** Memex's prompts repeatedly force the LLM to update `_schema.md`, `_index.md`, and links as part of ingest and lint. Commonplace already has generated indexes and collection contracts; the borrowable part is making maintenance obligations explicit in every write workflow. Ready for instruction tuning where gaps appear.

**Keep the LLM inside a narrow filesystem and tool envelope.** The namespace wrapper is heavier than Commonplace needs for normal work, but the design principle transfers: source ingestion and external-system review benefit from making irrelevant files unreachable, not merely undesired. Needs an execution environment that can provide that boundary without privileged daemon cost.

**Do not borrow prompt-only promotion of authority.** In Memex, a convention becomes behavior-shaping when Claude writes it into `_schema.md` and future prompts tell Claude to obey it. Commonplace should keep stronger promotion paths where high-authority instructions and validators are reviewed, typed, and checked.

## Curiosity Pass

**The README says questions can be filed back, but the query prompt is more conservative.** The README says good answers can be filed back as new pages, while `buildQueryPrompt()` only tells Claude to mention that a synthesized answer could be saved; it does not instruct automatic filing ([README.md](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/README.md), [src/lib/prompts/query.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/query.ts)). That is a sensible safety choice, but it narrows the implemented compounding loop.

**The activity log is maintained, but not obviously consumed.** `_log.md` is appended after operations, and SQLite has a separate audit table. In the inspected job prompts, ingest and query orient through `_schema.md` and `_index.md`, not `_log.md`. The log is valuable evidence for humans and lint, but it is not a strong memory read-back mechanism unless future prompts search it.

**"No RAG" mostly means no separate retrieval infrastructure.** Querying still requires retrieval: Claude reads `_index.md`, searches files, and selects pages. The design replaces a vector pipeline with LLM-operated symbolic retrieval over files, not with retrieval-free reasoning.

**The safety model depends on Linux privilege.** Mount namespaces and read-only bind mounts are concrete isolation, but requiring `CAP_SYS_ADMIN` is a meaningful adoption cost. The systemd unit mitigates this operationally, but the architecture is Linux-specific ([docs/operations.md](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/docs/operations.md), [systemd/memex.service](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/systemd/memex.service)).

**Lint is semantic maintenance, not validation.** The lint prompt asks Claude to find contradictions, stale claims, orphans, duplicates, missing cross-references, index drift, and schema drift, then fix confident structural issues ([src/lib/prompts/lint.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/lint.ts)). That is useful, but it is not a deterministic validator and does not prove claims are grounded.

**The README's `Bash` tool example is not in the inspected whitelist.** The README shows `Bash` as an allowed-tools example, but `ALLOWED_TOOLS_WHITELIST` contains `NotebookEdit`, `WebFetch`, and `WebSearch` as extras, not `Bash` ([README.md](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/README.md), [src/lib/constants.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/constants.ts)). The review treats the code as authoritative for tool policy.

## What to Watch

- Whether Memex adds deterministic schema checks or link/index validators alongside the lint prompt. That would move governance from instruction-only to testable system-definition artifacts.
- Whether query jobs ever gain an explicit "save this synthesis" operation with review or confirmation. That would change the compounding loop from source-ingest-only to conversation-derived wiki growth.
- Whether `_log.md` or SQLite audit rows become inputs to future prompts. That would make operational traces part of the read-back and possibly affect the trace-derived classification.
- Whether the daemon adds bounded search helpers, ranked snippets, or context packs. That would reduce the current dependence on Claude's ad hoc grep/read behavior as wiki size grows.
- Whether MCP tools and extra allowed tools become common in real use. They would widen ingestion power but also weaken the clean file-tool safety story.

## Bottom Line

Memex is a serious file-first memory runtime: it turns Claude Code into a queued, isolated wiki curator and stores the resulting knowledge as readable Markdown rather than opaque vectors. Its strongest idea for Commonplace is not the wiki format itself, but the runtime envelope around it: immutable source archive, per-KB serialized mutation, and prompt-enforced maintenance duties. Its weakest point, from a Commonplace perspective, is that artifact authority is mostly prompt-assigned rather than independently typed, validated, and reviewed.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Memex stores and maintains a wiki, but retained content still affects behavior through prompted file lookup rather than automatic relevance activation.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - frames: Memex's design trades vector infrastructure for LLM-operated filesystem selection under bounded job turns and prompts.
- [Bounded context orchestration model](../../notes/bounded-context-orchestration-model.md) - applies: Memex keeps scheduler state in code/SQLite and reserves LLM calls for bounded semantic wiki maintenance jobs.
- [Preserve evidence without making history the next context](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: Memex keeps raw sources in `wiki/raw/` while asking Claude to maintain derived pages and indexes.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Memex separates raw sources, wiki pages, prompt files, SQLite queue state, and namespace/tool policy by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: most wiki pages and raw sources advise future work as evidence, reference, or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompts, `_schema.md`, `_index.md`, queue state, namespace policy, and tool allowlists shape future agent behavior through instruction, routing, scheduling, and enforcement.
