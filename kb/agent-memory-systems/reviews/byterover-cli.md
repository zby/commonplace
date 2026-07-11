---
description: "byterover-cli review: local context-tree memory with HTML topic curation, BM25/runtime-signal retrieval, MCP hooks, review logs, dream pruning, and ByteRover cloud sync"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-04"
---

# byterover-cli

byterover-cli is ByteRover's `brv` command-line and daemon implementation for project memory. At the reviewed commit it persists curated knowledge in a project-local `.brv/context-tree`, reads it back through deterministic BM25 retrieval or an agentic query path, lets agents write validated `<bv-topic>` HTML topics through CLI/MCP flows, keeps per-topic runtime ranking signals in a sidecar store, exposes human review logs for curation, and offers a dream pipeline for link/merge/prune/synthesis candidate discovery.

**Repository:** https://github.com/campfirein/byterover-cli

**Reviewed commit:** [faf456d6bb47cb441b61c73051a581f4488868af](https://github.com/campfirein/byterover-cli/commit/faf456d6bb47cb441b61c73051a581f4488868af)

**Last checked:** 2026-06-04

## Core Ideas

**The main retained artifact is a project context tree, not a chat memory table.** The README describes ByteRover as persistent structured memory for coding agents, and the constants put the shared project store at `.brv/context-tree` with sibling project data such as logs, review backups, sessions, archive state, and settings ([README.md](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/README.md), [constants.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/constants.ts)). That makes it closer to a local KB for agents than to a vector-only memory service.

**Curated knowledge is now an HTML vocabulary with a closed schema.** MCP `brv-curate` asks the calling agent to supply one `<bv-topic>` HTML document and embeds the allowed element vocabulary in the tool description; `writeHtmlTopic()` strips fences, parses with parse5, requires one root topic and a safe path, validates every `<bv-*>` element against `ELEMENT_REGISTRY`, refuses to clobber existing topics unless overwrite is explicit, stamps timestamps, and writes atomically under the context tree ([brv-curate-tool.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/infra/mcp/tools/brv-curate-tool.ts), [html-writer.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/infra/render/writer/html-writer.ts)). The older markdown `curate` tool remains in the agent tool layer with ADD/UPDATE/UPSERT/MERGE/DELETE schemas, review metadata, backups, and sidecar updates ([curate-tool.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/agent/infra/tools/implementations/curate-tool.ts)).

**Read-back is mostly deliberate retrieval, but setup hooks push workflow instructions.** MCP `brv-query` dispatches a deterministic `query-tool-mode` task and returns matched topics as markdown sections for the calling agent to synthesize; it explicitly avoids LLM dispatch inside ByteRover ([brv-query-tool.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/infra/mcp/tools/brv-query-tool.ts)). Separately, `hook-prompt-submit` loads the `brv-instructions` template so hosts such as Claude Code can inject mandatory "query first / curate later" guidance before a prompt; that is push of authored workflow instructions, not selected memory content ([hook-prompt-submit.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/oclif/commands/hook-prompt-submit.ts), [brv-instructions.md](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/templates/sections/brv-instructions.md)).

**Search combines lexical retrieval with mutable runtime signals.** `SearchKnowledgeService` indexes HTML and markdown topics with MiniSearch, supports symbolic path queries and subtree scopes, propagates child scores to parent summaries, filters by kind and maturity, and blends normalized BM25 with importance, recency, and maturity tier boosts ([search-knowledge-service.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/agent/infra/tools/implementations/search-knowledge-service.ts), [memory-scoring.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/core/domain/knowledge/memory-scoring.ts)). The ranking signals live in an `IKeyStorage`-backed sidecar so query-time access bumps do not dirty version-controlled topic files ([runtime-signal-store.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/infra/context-tree/runtime-signal-store.ts), [file-key-storage.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/agent/infra/storage/file-key-storage.ts)).

**The write path has human-review affordances without making review mandatory.** Curate operations carry confidence, impact, reason, summary, previous summary, and `needsReview`; high-impact and delete operations become pending review unless review is disabled, while backups make rejection restorable ([curate-tool.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/agent/infra/tools/implementations/curate-tool.ts), [curate-log-handler.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/infra/process/curate-log-handler.ts)). The MCP tool-mode path similarly lets callers attach `meta` so the curation appears in the review pipeline, while omitting metadata still writes a topic ([brv-curate-tool.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/infra/mcp/tools/brv-curate-tool.ts)).

**Dream is a maintenance workflow, not an autonomous rewrite loop.** `brv dream scan` loads topics and sidecar signals, runs deterministic link/merge/prune/synthesize candidate generators, and returns candidates for the calling agent to decide; `finalizeDreamSession()` only archives explicitly named paths, preserving text, mtimes, and signals for undo ([dream-session.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/infra/dream/tool-mode/dream-session.ts), [prune-candidates.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/infra/dream/tool-mode/prune-candidates.ts)).

## Artifact analysis

- **Storage substrate:** `files` — The primary retained memory is the project-local `.brv/context-tree` file tree; secondary file-backed substrates include `.brv` logs, review backups, archive state, a nested context-tree git repository, and global/project data keystore blobs.
- **Representational form:** `prose` `symbolic` — Topic bodies carry prose facts, rules, decisions, flows, and examples, while `<bv-topic>` attributes, element names, paths, relations, runtime-signal records, logs, review statuses, manifests, and command schemas carry symbolic state.
- **Lineage:** `authored` `trace-extracted` — Topics are authored by users or calling agents through curate flows, while task inputs, file references, query hits, curate logs, access counts, mtimes, and dream candidate state are extracted from use traces and persisted as logs or sidecar signals.
- **Behavioral authority:** `knowledge` `instruction` `validation` `ranking` `learning` — Context topics advise later agents as knowledge; hook templates and MCP tool descriptions instruct hosts; the HTML writer validates the artifact grammar; BM25 and sidecar signals rank retrieval; access/update/prune signals feed future maintenance.

**Context-tree topics.** Storage substrate: `.brv/context-tree/<path>.html` in current tool mode, with legacy markdown still read by search and writeable by the older agent tool path. Representational form: prose inside a symbolic HTML vocabulary with root attributes such as path, title, summary, tags, keywords, and related references. Lineage: authored by a user/calling agent or generated by ByteRover's in-daemon curate agent from a task context; validation, timestamps, and overwrite behavior are system-added. Behavioral authority: knowledge artifact when returned by query; system-definition-like instruction when a topic encodes rules or decisions that the calling agent treats as project constraints, though ByteRover itself does not prove compliance.

**Runtime-signal sidecar.** Storage substrate: `FileKeyStorage` entries under a project data keystore, keyed as `["signals", ...pathSegments]`. Representational form: symbolic `importance`, `recency`, `maturity`, `accessCount`, and `updateCount` records. Lineage: trace-extracted from search access hits, curate updates, merges, deletes, archive/restore, and mtimes; invalidated when the corresponding topic is deleted or archived. Behavioral authority: ranking and maintenance input, because search blends the signals with BM25 and dream pruning uses low-importance/staleness thresholds.

**Search indexes and query outputs.** Storage substrate: in-memory MiniSearch cache rebuilt from context-tree files, plus query logs under project data. Representational form: symbolic indexed documents, symbol trees, references, scores, excerpts, and rendered markdown results. Lineage: derived from topic files, summary files, source definitions, mtimes, and runtime-signal reads; caches invalidate on file mtimes, schema version, source changes, and explicit refresh. Behavioral authority: routing/ranking for `brv-query` and agent query tasks; knowledge artifact when matched docs are inserted into the caller's context.

**Curate logs, review backups, and task history.** Storage substrate: project data files and `.brv/review-backups`. Representational form: symbolic operation envelopes plus prose reasons, summaries, previous summaries, responses, and telemetry. Lineage: trace-extracted from task lifecycle events, tool results, curation outputs, and pre-write snapshots. Behavioral authority: review/audit state; backups have restoration authority when a human rejects a change.

**Agent memories blob store.** Storage substrate: file blobs under the agent storage directory, with `memory-{id}` JSON records and optional attachment blobs. Representational form: prose memory content plus symbolic tags, source, pinned flag, timestamps, and attachment metadata. Lineage: authored or system/user/agent-sourced through `MemoryManager` CRUD APIs, not the context-tree curate protocol. Behavioral authority: push-like prompt context when `MemoryContributor` lists recent or pinned memories into `# Agent Memories`, but this is a separate local agent-memory surface from the shared ByteRover context tree ([memory-manager.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/agent/infra/memory/memory-manager.ts), [memory-contributor.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/agent/infra/system-prompt/contributors/memory-contributor.ts)).

**Dream archives and ghost cues.** Storage substrate: `.brv/archive` for tool-mode archives and `_archived/*.stub.md` / `*.full.md` inside the context tree for archive-service mode. Representational form: full preserved prose plus symbolic archive metadata and short ghost-cue summaries. Lineage: derived from existing topics and sidecar signals; tool-mode finalize preserves previous text, mtime, and signals for undo. Behavioral authority: decay/maintenance and search affordance, because archived material is no longer an ordinary topic but may remain discoverable through stubs or undo state.

Promotion path: ByteRover has a practical ladder from task/session evidence to a validated topic file, then to retrieval/ranking, review status, version-control sync, and optional archive/undo. It does not provide a Commonplace-style semantic gate before a topic becomes queryable; validation is mostly grammar/path/metadata correctness, with human review optional by operation metadata.

## Comparison with Our System

| Dimension | byterover-cli | Commonplace |
|---|---|---|
| Primary purpose | Agent-facing project memory for coding workflows | Git-native methodology KB for agent-operated knowledge bases |
| Canonical artifact | `<bv-topic>` HTML topic in `.brv/context-tree` | Typed Markdown note, review, instruction, ADR, or source snapshot |
| Storage substrate | Local files plus keystore sidecars, nested git/VC, logs, optional cloud sync | Repository files plus generated indexes and validation/review reports |
| Write path | Agent/user curation, MCP tool-mode writes, legacy curate tool, dream archive finalization | Authored artifacts, source snapshots, explicit review, validation, index refresh |
| Read-back | Pull retrieval via CLI/MCP/search; push of setup instructions and local pinned memories | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | HTML schema validation, path/overwrite guards, review logs, backups, version-control commands | Collection/type contracts, schema validation, git diffs, semantic gates, review archives |

ByteRover is stronger as a deployable coding-agent memory product. It has installation scripts, MCP tools, a daemon, TUI/web UI, provider management, context-tree search, curation sessions, review UI state, and cloud sync/version-control commands ([package.json](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/package.json), [README.md](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/README.md)). Commonplace is stronger as a methodology corpus: artifacts are typed by collection contracts, source citations are explicit, indexes are generated from files, and semantic review is part of the maintenance story.

The biggest design split is authority. ByteRover deliberately makes the calling agent responsible for synthesis in MCP query mode: ByteRover returns matched topics, not an answer. That is a good adoption tradeoff, but it means the project memory's effective force depends on host instructions, hook installation, and the agent's obedience. Commonplace treats many files as direct system-definition artifacts for agents operating inside the repo.

### Borrowable Ideas

**A closed HTML topic vocabulary for agent-authored memory.** Needs a concrete use case. Commonplace could use a stricter symbolic format for high-volume operational snippets, but Markdown plus type specs is still better for long-form methodology notes.

**Separate shared content from mutable ranking signals.** Ready now as a design principle. ByteRover's sidecar keeps access/importance bumps out of version-controlled topics; Commonplace should do the same if it adds usage-derived ranking.

**Return retrieved topics to the caller rather than answering inside the memory service.** Ready for retrieval tooling. `brv-query` keeps the calling agent responsible for synthesis, which avoids one hidden LLM layer and makes retrieval evidence visible.

**Expose overwrite refusal with prior content in the error.** Ready now. The `path-exists` correction loop is a good pattern for agent write tools: prevent silent clobber, include the existing artifact, and let the agent merge intentionally.

**Borrow review backups as rejection infrastructure, not as semantic review.** Ready now. Commonplace already archives old review files; ByteRover's first-write backup idea is useful for reversible working-tree edits, but grammar validation should not be mistaken for meaning validation.

**Use dream-style candidate generation for workshops.** Needs a bounded workflow. Link/merge/prune/synthesize candidate scans would fit Commonplace work directories, with human/agent review before library promotion.

## Write side

**Write agency:** `manual` `automatic` — Humans and calling agents author topics through CLI/MCP/curate tools; automatic system operations update runtime signals, logs, review backups, generated summaries/manifests, access-hit counts, and archive/undo metadata.

**Curation operations:** `decay` `promote` — Runtime scoring down-weights stale material through recency/importance decay and promotes or demotes maturity tiers from access/update signals. Dream pruning can archive explicitly selected low-importance or stale topics, but link/merge/synthesis are candidate surfaces rather than automatic store-changing writes.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — Query and curate task lifecycles, tool results, MCP calls, access-hit events, file references, task histories, and curation session inputs feed durable logs, sidecar signals, and sometimes generated topic content.

**Learning scope:** `per-project` `cross-task` — Context trees, sidecar signals, logs, and review state are project-scoped and persist across later tasks; cloud/version-control flows can share the topic tree across teammates and machines.

**Learning timing:** `online` `staged` — Search access hits and curate sidecar updates happen during ordinary task execution, while curation sessions, review approval/rejection, dream scans, finalization, and version-control sync are staged workflows.

**Distilled form:** `prose` `symbolic` — Curate transforms task/file/user context into prose topics embedded in symbolic `<bv-topic>` structure; access and update traces become symbolic ranking and maturity signals.

**Trace source.** ByteRover qualifies as trace-derived because task inputs and agent activity become durable retained artifacts. `CurateExecutor` preloads file references, compacts large context, injects task variables and precomputed recon results into an agent session, then writes the agent's final `<bv-topic>` output through the HTML writer ([curate-executor.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/infra/executor/curate-executor.ts)). Query and curation lifecycle hooks persist task-level logs, matched documents, timing, operations, responses, and review metadata ([query-log-handler.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/infra/process/query-log-handler.ts), [curate-log-handler.ts](https://github.com/campfirein/byterover-cli/blob/faf456d6bb47cb441b61c73051a581f4488868af/src/server/infra/process/curate-log-handler.ts)).

**Extraction.** Extraction is mixed. Tool-mode MCP curation has the calling agent author the HTML directly, while ByteRover validates and writes it; in-daemon curation runs an agent session over task context and asks for a final topic document; search access traces are automatically condensed into access counts and importance bumps; dream scans derive maintenance candidates from topic contents, links, mtimes, search results, and sidecar signals.

**Scope and timing.** The durable shared layer is per project/worktree, with optional cloud sync and version-control. Timing is online for access/update sidecar bumps and task logs, staged for `brv curate` sessions, review decisions, dream finalization, and VC push/pull.

**Survey fit.** ByteRover belongs in the trace-to-project-KB and trace-to-ranking-signal families. It strengthens the survey claim that trace-derived learning often has two authority levels: raw task/use traces become logs and signals, while only a curated or agent-authored distillation becomes the memory content that later agents read.

## Read-back

**Read-back:** `both` — Context-tree memory is primarily pull through `brv query`, MCP `brv-query`, `search_knowledge`, `read_file`, and query tasks, but ByteRover also pushes authored workflow instructions through prompt-submit hooks and can push local agent memories through the system-prompt memory contributor.

**Read-back signal:** `coarse` — The implemented push paths found in code are coarse always-load/setup surfaces: mandatory ByteRover workflow instructions and recent or pinned local agent memories. Instance-targeted content-tree topic selection remains pull retrieval.

**Faithfulness tested:** `no` — The repository has command, hook, search, review, telemetry, and validation tests, but I did not find a with/without ablation proving pushed instructions or memories change agent behavior reliably.

**Targeting and signal.** The strong content-tree retrieval path is pull: user/agent query text or symbolic paths drive MiniSearch, scope filters, maturity filters, parent-score propagation, and sidecar-ranked results. The push path is coarse because `hook-prompt-submit` prints a static instruction template for coding-agent hosts, and `MemoryContributor` lists recent or pinned memories without relevance selection. ByteRover does not appear to automatically select context-tree topics by the current user prompt and inject them before every agent call; instead, its hook tells the agent to run `brv query`.

**Injection point.** Hook instructions and `# Agent Memories` are assembled before a model call in the host or ByteRover agent prompt. Query results enter the calling agent's context only when the agent, user, or MCP client invokes retrieval. Search access-hit flushing and curation logging happen after or around retrieval/write operations, so those are write-side maintenance for later calls.

**Selection, scope, and complexity.** Pull selection is relatively rich: exact path matching, natural-language BM25, AND-first/OR fallback, subtree scope, element-hint prefiltering, kind and maturity filters, score-gap filtering, parent propagation, local-source boost, query caches, and sidecar-based compound scoring. Pushed setup instructions are not content-selected and can be heavy-handed; the template repeatedly marks `brv query` and `brv curate` as mandatory for code tasks, so its effective authority depends on host acceptance and agent compliance.

**Authority at consumption.** Retrieved topics are advisory evidence unless the caller treats rules/decisions as project constraints. Hook instructions are higher-authority operational guidance in the host context. MCP `brv-curate` and `brv-query` descriptions also act as system-definition artifacts for external agents by defining exact write/read contracts.

**Faithfulness.** ByteRover tests structural behavior such as hook output, query envelopes, review commands, runtime-signal updates, and validation paths, but behavior change from pushed memory/instructions is not measured. Effective obedience remains runtime-dependent.

**Other consumers.** Humans consume the same memory through CLI, TUI/web UI, `brv review`, `brv curate view`, query logs, review pending/approve/reject commands, version-control commands, and cloud dashboard flows. That human surface is central: ByteRover is as much a collaborative context-management product as an agent memory library.

## Curiosity Pass

**The context tree and local agent-memory blob store should not be collapsed.** Both can enter prompts, but the context tree is shared project knowledge with search, review, and sync; the blob store is a local list of agent memories.

**ByteRover's strongest governance is syntactic.** The closed `<bv-*>` vocabulary, overwrite guard, safe-path checks, and sidecar separation are useful, but they do not by themselves verify that a topic is true or worth retaining.

**The read-back story is intentionally pull-first.** The hook says "query first" instead of silently injecting top-k topics. That avoids hidden context pollution, but it relies on the agent remembering or obeying the instruction.

**Runtime signals are behavior-shaping memory.** Access counts, importance, maturity, and recency may look like metadata, but they affect ranking, pruning, and promotion/demotion. They deserve lineage and undo handling, which the code partially supplies.

**Dream scan separates candidate discovery from action.** That is a good boundary: deterministic scans can surface link/merge/prune/synthesis opportunities without silently rewriting the KB.

## What to Watch

- Whether `brv-query` gains an automatic pre-prompt topic injection hook; that would shift context-tree read-back from pull-only for topics to instance-targeted push.
- Whether review approval becomes mandatory for high-authority `<bv-rule>` or `<bv-decision>` topics, rather than optional metadata supplied by the caller.
- Whether runtime-signal sidecars gain stronger cross-process consistency and orphan pruning; current comments note per-key/process caveats and backlog cleanup.
- Whether dream synthesis begins writing new topics directly; that would change the curation operation from candidate surfacing to automatic synthesis.
- Whether ByteRover adds behavioral faithfulness tests comparing agents with and without pushed instructions or recalled topics.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: ByteRover stores a rich context tree, but topic memory usually affects agents only after explicit query.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: ByteRover requires separating topics, sidecar ranking signals, logs, hook instructions, and archive stubs by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: returned topics, query logs, curate logs, and archive stubs mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: hook templates, MCP tool contracts, HTML validators, path guards, and ranking policies configure future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: ByteRover turns task/file/query traces into curated topics, sidecar signals, and maintenance candidates.
