---
description: "Memex review: isolated Claude Code runtime that maintains a markdown wiki through queued ingest, query, and lint jobs"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
---

# Memex

Memex, from `wastedcode/memex`, is a Node/TypeScript CLI and privileged daemon that wraps `claude -p` so each user wiki gets isolated filesystem access, a serial job queue, and prompt-directed maintenance of a markdown knowledge base. Its memory substrate is not embeddings or a vector database; it is a per-wiki file tree where Claude reads raw sources, writes wiki pages, maintains schema/index/log files, and answers later questions by searching those files.

**Repository:** https://github.com/wastedcode/memex

**Reviewed commit:** [1e223b6045be31b70b1ab9e4b28dd403150d29e7](https://github.com/wastedcode/memex/commit/1e223b6045be31b70b1ab9e4b28dd403150d29e7)

**Source directory:** `related-systems/wastedcode--memex`

## Core Ideas

**The wiki is the durable memory.** Creating a wiki registers it in SQLite and scaffolds `.claude.md`, `.claude/`, `.tools/`, `wiki/raw/`, `wiki/_schema.md`, `wiki/_index.md`, and `wiki/_log.md` under the Memex data directory ([src/daemon/scaffold.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/scaffold.ts), [src/lib/constants.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/constants.ts)). SQLite stores wiki registration, queue jobs, and audit logs, but it does not store the wiki's semantic content; the behavior-shaping knowledge lives in markdown files.

**Claude Code is the write engine.** The daemon builds prompts for `ingest`, `query`, and `lint` jobs, wraps the command in a per-job mount namespace, and runs `claude -p` with file tools restricted to `Read`, `Write`, `Edit`, `Glob`, and `Grep` unless a wiki opts into a small whitelist ([src/daemon/runner.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/runner.ts), [src/lib/constants.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/constants.ts)). The project explicitly treats prompts as product logic: the shared wiki prompt makes `_schema.md` institutional memory, `_index.md` the table of contents, `_log.md` the activity ledger, and `## Related` links the connection contract ([src/lib/prompts/wiki.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/wiki.ts), [docs/prompts.md](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/docs/prompts.md)).

**Context efficiency comes from file-native pull and compiled summaries.** Memex has no vector index, embedding budget, or reranker. Query jobs tell Claude to read `_index.md`, search with grep/glob, read relevant pages, and synthesize an answer grounded in file paths ([src/lib/prompts/query.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/query.ts)). Efficiency depends on the maintained index, schema, links, page focus, and Claude's own file search, so the system lowers repeated rediscovery when the wiki is well maintained but does not enforce a hard token budget or top-k selection policy.

**Writes are serialized per wiki.** Each wiki has a FIFO queue backed by SQLite, and only one job runs per wiki at a time; independent wikis can drain in parallel ([src/daemon/queue.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/queue.ts), [src/daemon/db.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/db.ts)). This is a simple but important governance choice: it prevents two Claude processes from concurrently editing the same wiki files.

**Isolation is filesystem-oriented.** The daemon requires mount namespace capability, bind-mounts the wiki directory to `/workspace`, remounts the workspace with `nosuid,nodev`, remounts `wiki/raw/` read-only, and sets `HOME=/workspace` for the child process ([src/daemon/namespace.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/namespace.ts), [src/daemon/runner.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/runner.ts)). The Unix socket is world-writable, but requests are authorized by kernel peer credentials and per-wiki `owner_uid` checks ([src/daemon/server.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/server.ts), [src/daemon/routes.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/routes.ts)).

## Artifact analysis

- **Storage substrate:** `files` `sqlite` — The durable wiki corpus, raw source archive, wiki prompt customization, tool configuration, and Claude credentials are files under each wiki directory; SQLite stores wiki registry rows, queue jobs, job results, and audit logs.
- **Representational form:** `prose` `symbolic` — Wiki pages, `_schema.md`, `_index.md`, `_log.md`, `.claude.md`, prompt text, and query/lint reports are prose; queue rows, API routes, job types, JSON payloads/results, owner UIDs, tool whitelists, mount commands, and CLI command definitions are symbolic. I did not find vector, embedding, or model-weight state owned by Memex.
- **Lineage:** `authored` `imported` — Users author conventions, configuration, prompts, and direct file edits; raw sources are imported into `wiki/raw/`; Claude-derived wiki pages, schema updates, links, index entries, log entries, query answers, and lint reports are derived from imported sources and existing wiki files. I did not find durable extraction from agent/session/tool traces as a standing learning path.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` — Wiki pages and query answers advise as knowledge; prompts, `.claude.md`, `_schema.md`, and tool lists instruct future Claude jobs; namespace isolation, read-only raw mounts, owner checks, job serialization, timeouts, and tool restrictions enforce boundaries; CLI/API routes, job types, index/search conventions, and schema categories route work; lint prompts and reports validate wiki health, though judgment-heavy issues are left for review.

**Wiki files.** The wiki file tree is the central retained artifact. `raw/` files are source material, while all other wiki pages are LLM-maintained knowledge artifacts with source references and related links. `_schema.md` has stronger system-definition authority because the baseline prompt names it "institutional memory" and tells Claude to update conventions, filing heuristics, templates, lifecycle patterns, and vocabulary there ([src/lib/prompts/wiki.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/wiki.ts)).

**Prompt package.** The shared wiki prompt and job prompts are authored system-definition artifacts. They decide that ingest jobs must read sources, read schema/index, search existing pages, update or create pages, maintain bidirectional links, update the index, append to the log, and reflect on schema drift ([src/lib/prompts/ingest.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/ingest.ts)). Query and lint jobs are similarly constrained by prompts rather than by a separate retrieval or validation engine.

**Daemon database and queue.** SQLite tables for `wikis`, `queue_jobs`, and `audit_log` are operational memory rather than semantic wiki memory. They retain ownership, model choice, job payloads/results, retry state, and audit entries, and they control what work runs next ([src/daemon/db.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/db.ts), [src/daemon/queue.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/queue.ts)). That state is system-definition authority for scheduling and accountability, not the main knowledge surface.

**Access and isolation contracts.** The Unix-socket API, peer-credential checks, owner UID field, mount namespace wrapper, read-only raw mount, tool whitelist, and per-wiki credential resolution are behavior-shaping artifacts that define who can mutate a wiki and what Claude can touch ([src/daemon/routes.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/routes.ts), [src/daemon/auth.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/auth.ts), [src/daemon/namespace.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/namespace.ts)).

**Promotion path.** Memex promotes uploaded or existing source files into wiki pages, index entries, links, schema conventions, and log entries. It also lets lint promote observed drift into direct fixes for links, related sections, index entries, and schema text. There is no implemented path from wiki prose into stronger symbolic validators, embeddings, or enforced type schemas.

## Comparison with Our System

| Dimension | Memex | Commonplace |
|---|---|---|
| Primary purpose | Run isolated Claude jobs that build and maintain a personal markdown wiki | Maintain a typed methodology KB for agents and maintainers |
| Canonical substrate | Per-wiki markdown files plus raw source archive | Git-tracked `kb/` collections, type specs, source snapshots, reviews, and generated indexes |
| Retrieval | Claude reads `_index.md`, searches files with grep/glob, and reads pages | Agents use `rg`, authored/generated indexes, links, collection contracts, and review artifacts |
| Write path | Prompt-directed Claude jobs mutate wiki files through file tools | Agents edit repo artifacts under type contracts, validation, semantic review, and git lifecycle |
| Governance | Mount namespace, raw read-only mount, owner UID checks, serial queue, tool whitelist, lint prompt | Collection routing, frontmatter schemas, deterministic validation, review gates, citation discipline |

Memex and Commonplace both bet on ordinary files as durable agent memory. The key difference is authority. Memex delegates knowledge-base maintenance to a running Claude job and relies on prompts, isolation, and serialization to keep the wiki coherent. Commonplace keeps more semantics outside the model: collection contracts, type specs, validation commands, source snapshots, and review processes make many constraints inspectable before and after an agent writes.

Memex is stronger as an adoption layer for personal or project wikis. It gives the user a simple CLI, a daemon queue, per-wiki credentials, filesystem isolation, and prompt defaults that encourage compounding knowledge. Commonplace is stronger where retained artifacts need reviewable methodological authority: claims, source lineage, link semantics, and artifact types are explicit repo objects rather than emergent conventions in a mutable wiki.

### Borrowable Ideas

**Per-workspace job serialization.** Commonplace could use explicit per-workshop or per-artifact queues for high-risk automated maintenance. Ready as an operational pattern when multiple agents may write related files.

**Raw source immutability by mount or permission boundary.** Memex's read-only `raw/` mount is a concrete enforcement version of a source-snapshot rule. Ready conceptually, but Commonplace would need a repo-local equivalent that works without a privileged daemon.

**Schema as prompt-visible institutional memory.** Commonplace already uses collection contracts; Memex's wording around `_schema.md` reinforces that such files should be treated as active behavior-shaping memory, not passive docs. Ready as an authoring emphasis rather than a new feature.

**Prompt-level maintenance checklists are useful but weak alone.** Memex's lint prompt is a compact maintenance spec. Commonplace can borrow the checklist shape, but should keep deterministic validators and review gates for durable claims.

**Do not borrow privilege as a default dependency.** Memex's namespace isolation is useful, but requiring `CAP_SYS_ADMIN` or root is a large operational cost for a methodology KB. Commonplace should prefer user-space constraints unless a concrete threat model requires stronger isolation.

## Write side

**Write agency:** `manual` `automatic` — Users manually create wikis, configure conventions/tools/models, upload sources, and submit ingest/query/lint jobs. Claude jobs automatically create and update wiki pages, schema/index/log files, links, and lint fixes according to prompts; the daemon also writes queue, result, and audit records.

**Curation operations:** `evolve` `synthesize` — Ingest jobs update existing pages, cross-references, index entries, and schema conventions in light of new sources and prior wiki content. The prompts also ask Claude to notice emerging patterns and create synthesis/topic pages when the accumulated wiki warrants them. Lint can repair index/link/schema drift, but duplicate merges, contradictions, and stale claims are generally reported for human judgment rather than automatically consolidated or invalidated.

## Read-back

**Read-back:** `pull` — Retained wiki memory reaches Claude when the job prompt tells it to read `_schema.md`, `_index.md`, search with grep/glob, and read relevant files. The daemon does not pre-load wiki pages, source snippets, schema text, or prior memory into every model invocation; it supplies instructions and lets the agent perform explicit file lookup.

The pull surface is narrow but practical: query jobs read the index, search files, and cite page paths; ingest jobs read schema/index and search existing pages before writing; lint jobs glob all markdown files outside `raw/` and report or repair wiki-health issues ([src/lib/prompts/query.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/query.ts), [src/lib/prompts/ingest.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/ingest.ts), [src/lib/prompts/lint.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/lint.ts)). Actual selection quality depends on Claude's file-search behavior and the maintained quality of `_index.md`, `_schema.md`, page names, and links; Memex does not test whether read wiki memory changes downstream behavior.

## Curiosity Pass

**The README is more ambitious than the current implementation.** The README says good query answers can be filed back as new pages, but the query prompt only says a synthesis "could be saved" and the CLI submits a `query` job without a save flag ([README.md](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/README.md), [src/lib/prompts/query.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/query.ts), [src/cli/commands/query.ts](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/cli/commands/query.ts)).

**The security model is unusually concrete for a wiki tool.** The system does not merely tell Claude to stay in the wiki; it remounts the wiki as `/workspace`, remounts raw sources read-only, filters environment variables, and restricts tools. That gives the prompt discipline a real boundary, though it also makes Linux capability setup part of the product.

**The strongest learned artifact is still prose.** Schema conventions can evolve with every ingest, and that is genuine behavior-shaping memory for future jobs. But it remains prompt-followed prose, not a checked schema, validator, router table, or retrieval index.

**Audit state is not semantic lineage.** Queue jobs and audit logs record that work happened and preserve outputs/results, but the wiki pages themselves do not have enforced source-span lineage beyond prompt-required source references.

## What to Watch

- Whether query jobs gain an explicit "save this synthesis" path. That would turn query results from answers into durable wiki writes.
- Whether lint grows deterministic checks or structured issue files instead of relying only on a Claude prompt and markdown report.
- Whether `_schema.md` conventions become machine-checkable enough to validate drift rather than only describe it.
- Whether wiki pages gain stronger provenance metadata for which raw files and prior pages caused each update.
- Whether the daemon adds diff-before-apply or rollback support for high-impact Claude edits.
- Whether host setup can preserve isolation without requiring root or broad mount namespace capability.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Memex stores a durable wiki, but retained memory enters jobs through explicit file lookup rather than automatic context injection.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: wiki prose, prompt instructions, queue rows, owner checks, and namespace wrappers carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: wiki pages, raw source references, query answers, and lint reports mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: prompts, schema conventions, CLI/API routes, queue policy, tool restrictions, and namespace boundaries govern future behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Memex's main design problem is routing file-backed wiki memory into bounded Claude jobs through prompts and file tools.
