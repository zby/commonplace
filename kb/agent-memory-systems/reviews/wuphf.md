---
description: "WUPHF review: multi-agent office with git-backed wiki, per-agent notebooks, MCP memory tools, trace extraction, and prompt-time memory push"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# WUPHF

WUPHF, from `nex-crm/wuphf`, is a local multi-agent "office" for running AI teammates through Claude Code, Codex, Opencode, OpenAI-compatible providers, or legacy tmux panes. Its memory system is not a standalone vector-store SDK. It is built into the office runtime: per-agent notebooks, a shared git-backed Markdown wiki, wiki search and cited lookup, fact extraction, lint, notebook-to-wiki promotion, playbook compilation, team learning logs, and prompt-time context injection all sit behind broker endpoints and MCP tools.

**Repository:** https://github.com/nex-crm/wuphf

**Reviewed commit:** [83393b2c5e4a66754062fbd2b4cda7e9ec2dd299](https://github.com/nex-crm/wuphf/commit/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299)

**Last checked:** 2026-06-02

## Core Ideas

**The office is push-driven, but agent turns are fresh.** The broker wakes agents on messages, routes by focus/collab mode and mentions, then launches a headless provider turn rather than preserving one growing model session. Claude and Codex runners build a prompt, scoped MCP config, and stdin payload per turn; coding agents can also receive isolated task worktrees ([ARCHITECTURE.md](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/ARCHITECTURE.md), [internal/team/headless_claude.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/team/headless_claude.go), [internal/team/headless_codex.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/team/headless_codex.go)).

**Markdown is the default shared memory substrate.** Fresh installs use a local wiki repository under `~/.wuphf/wiki/`, with team articles, indexes, git commits, backup mirror, wiki UI, and MCP tools. Nex and GBrain remain legacy shared-memory backends, but the README and backend code make Markdown the built-in path for new installs ([README.md](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/README.md), [internal/team/wiki_git.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/team/wiki_git.go), [internal/team/memory_backend.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/team/memory_backend.go)).

**Private notebooks are draft memory, not automatically trusted team memory.** Agents write `agents/{slug}/notebook/*.md` through notebook MCP tools. Other agents may read/search notebooks, but promotion to `team/*.md` goes through `notebook_promote`, reviewer routing, and a retained source entry; the tool response explicitly nudges durable notes toward promotion rather than silently making scratch notes canonical ([internal/teammcp/notebook_tools.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/teammcp/notebook_tools.go), [internal/team/memory_workflow.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/team/memory_workflow.go), [internal/team/memory_workflow_reconciler.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/team/memory_workflow_reconciler.go)).

**The wiki has both plain retrieval and typed retrieval.** Agents can read, list, search, and ask cited questions over the wiki. The cited lookup path uses a `WikiIndex`, query classification, additive typed graph walks over fact records, BM25 fallback, and an LLM answer step that returns source JSON. This is stronger than simple substring wiki search, but still keeps Markdown/fact logs as the source layer ([internal/teammcp/server_wiki_tools.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/teammcp/server_wiki_tools.go), [internal/team/wiki_lookup.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/team/wiki_lookup.go), [internal/team/wiki_query_retrieve.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/team/wiki_query_retrieve.go)).

**Trace and artifact extraction are explicitly operationalized.** Committed artifacts can trigger an extractor that reads artifact Markdown, prompts an LLM for entities and facts, resolves entities, writes typed fact logs, updates the index, and sends failures to a DLQ. Separate tools record durable team learnings and playbook executions, and playbook synthesis can push execution outcomes back into playbook text ([internal/team/wiki_extractor.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/team/wiki_extractor.go), [internal/teammcp/learning_tools.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/teammcp/learning_tools.go), [internal/teammcp/playbook_tools.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/teammcp/playbook_tools.go)).

**Context efficiency is controlled by scoping, not compression alone.** WUPHF avoids persistent model sessions, scopes MCP manifests by agent/mode, searches notebooks and wiki before loading them, caps private memory matches, caps context lookup limits/timeouts, and wraps pushed memory as untrusted background. The system still pays prompt cost for injected snippets and tool schemas; its strongest economy move is that agents see selected, scoped memory and tools rather than every channel, notebook, wiki page, and integration ([internal/team/scoped_memory.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/team/scoped_memory.go), [internal/teammcp/context_tools.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/teammcp/context_tools.go), [internal/teammcp/server.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/teammcp/server.go)).

## Artifact analysis

- **Storage substrate:** `repo` — Local git repository under `~/.wuphf/wiki/team/`, with backup mirror and generated `index/all.md`
- **Representational form:** `mixed` — Prose Markdown with symbolic paths, wikilinks, categories, authorship, and git commits

**Team wiki articles.** Storage substrate: local git repository under `~/.wuphf/wiki/team/`, with backup mirror and generated `index/all.md`. Representational form: prose Markdown with symbolic paths, wikilinks, categories, authorship, and git commits. Lineage: authored by agents or humans, migrated from legacy backends, promoted from notebooks, generated from decision packets, or edited through the web/wiki APIs. Behavioral authority: knowledge artifacts when read or searched; system-definition artifacts when a wiki article is a playbook, decision, process, or source that later tools compile, search, or cite.

**Per-agent notebooks.** Storage substrate: Markdown files under `agents/{slug}/notebook/` in the same wiki repo. Representational form: prose working notes plus symbolic path ownership. Lineage: agent-authored scratch or captured task context; the retained auto-notebook writer type exists but the code comment says production no longer wires it to message/task hooks. Behavioral authority: primarily private or cross-agent knowledge artifacts; they gain stronger authority only through promotion review or when a `context_lookup` / notebook search result is deliberately used in a task.

**Notebook promotion records and memory-workflow state.** Storage substrate: broker state, review log, task `MemoryWorkflow` records, and target wiki files after approval. Representational form: symbolic JSON-like workflow state plus prose rationale and promoted Markdown. Lineage: derived from notebook source paths, task ids, reviewer decisions, and reconciliation checks. Behavioral authority: system-definition artifacts for workflow enforcement and review routing: they decide whether lookup/capture/promote steps are pending, satisfied, missing, or approved.

**Wiki fact logs, entities, graph, and indexes.** Storage substrate: JSONL fact/entity logs, `WikiIndex` stores, text index, typed fact store, and generated catalog/cache state. Representational form: mixed symbolic triples/facts/entities plus indexed text and ranking state. Lineage: extracted from committed artifacts and wiki material, merged/reinforced through resolver logic, invalidated by source edits or extraction/reconcile changes. Behavioral authority: ranking and retrieval system-definition artifacts; facts shape lookup answers, lint checks, typed graph walks, and entity briefs, while the source Markdown remains the human-readable evidence layer.

**MCP tool schemas and broker endpoints.** Storage substrate: Go code in `internal/teammcp/` and broker route handlers. Representational form: symbolic tool definitions with prose descriptions and JSON schemas. Lineage: authored runtime interface over the broker/wiki/notebook/memory systems. Behavioral authority: system-definition artifacts because they constrain which actions agents can take: read, search, write, promote, lint, resolve contradictions, record learnings, compile playbooks, or run context workflow steps.

**Headless prompt and memory brief assembly.** Storage substrate: runtime prompt construction, per-agent MCP config files, broker memory maps, and backend search results. Representational form: prose prompt/context blocks plus symbolic tool manifests and environment variables. Lineage: assembled per turn from the human notification, private notebook matches, shared backend hits, role prompt, active task, and scoped tools. Behavioral authority: system-definition at consumption time: pushed memory can influence the next agent action, while the code explicitly frames it as untrusted background rather than operator instruction.

**Team learnings, playbooks, compiled skills, and execution logs.** Storage substrate: wiki-backed learning log/index, `team/playbooks/*.md`, compiled playbook skill files, and append-only execution logs. Representational form: mixed prose guidance, symbolic metadata, and compiled skill artifacts. Lineage: authored playbooks, recorded executions, explicit team learning records, and synthesis jobs. Behavioral authority: playbooks and compiled skills can become instructions for future agents; execution records and learnings are knowledge artifacts until a future tool or synthesis path reads them back into a task.

**Lint reports and contradiction resolutions.** Storage substrate: daily lint reports, fact-log mutations, and wiki worker commits. Representational form: symbolic findings plus prose summaries. Lineage: derived from fact index checks, LLM contradiction judgments, stale/orphan/cross-reference scans, and human/agent resolution choices. Behavioral authority: validation and governance system-definition artifacts; they do not just describe the wiki, they drive correction paths and supersession/validity updates.

The promotion path is unusually explicit for a product repo: notebook or artifact -> candidate knowledge -> reviewer/promotion or extractor -> wiki/fact/log/playbook surfaces -> retrieval, prompt injection, lint, or compilation. It is not fully Commonplace-like, because type contracts and review status are lighter, but WUPHF does distinguish draft, promoted, generated, indexed, and compiled surfaces.

## Comparison with Our System

| Dimension | WUPHF | Commonplace |
|---|---|---|
| Primary purpose | Multi-agent office for running AI teammates and shared company/project memory | Methodology KB and framework for agent-operated knowledge bases |
| Main retained unit | Wiki article, notebook entry, fact/log row, playbook, broker task/workflow state | Typed Markdown artifact with collection/type contract, links, validation, and review |
| Runtime activation | Broker wakes agents; memory snippets and tools can be pushed into fresh turns | Mostly pull through search/indexes/links unless instructions or skills load context |
| Learning loop | Agents capture/promote notes, extract facts from artifacts, record learnings/executions, synthesize playbooks | Source-grounded artifact writing, semantic review, validation, workshop-to-library promotion |
| Governance | Git commits, reviewer promotion, lint reports, permission gates, path validation, DLQs | Schemas, collection contracts, deterministic validation, semantic review gates, git history |

The strongest alignment is that both systems treat a file-backed knowledge base as operational infrastructure for agents rather than as passive documentation. WUPHF makes this visible in product form: agents are given MCP tools, notebooks, wiki lookup, and promotion flows while they work. Commonplace makes the artifact contract more explicit: type specs, collection-local routing, link vocabulary, and review gates define what each artifact is allowed to mean.

The main divergence is runtime ambition. WUPHF is an office runtime first, so it accepts a broad mix of broker state, tool manifests, per-turn prompt assembly, wiki files, fact logs, generated briefs, playbook compilers, and UI surfaces. Commonplace is slower and more inspectable: it usually keeps durable methodology claims in Markdown with explicit status and validation before making them behavior-shaping.

### Borrowable Ideas

**Notebook-to-wiki promotion as a first-class workflow.** Commonplace already has a workshop/library distinction, but WUPHF's notebook tools make the draft-to-shared-memory transition explicit in the agent's tool surface. Ready to borrow as a pattern for workshop notes: a promote command should preserve source, rationale, reviewer, target path, and state.

**Pushed memory must be fenced as untrusted background.** WUPHF's `composeHeadlessStdinPayload` puts the operator message first and wraps retrieved context in a warning fence. Commonplace should borrow that exact authority discipline anywhere source snapshots, email, web, or chat-derived material are pushed into agent context. Ready now.

**Context workflow state tied to tasks.** WUPHF tracks lookup, capture, and promote as task workflow steps rather than leaving memory hygiene to convention. Commonplace review or ingest tasks could record whether source lookup, durable capture, and promotion decisions happened. Needs a concrete task/workshop substrate before implementation.

**Typed fact extraction with source Markdown preserved.** WUPHF's extractor keeps Markdown as source of truth while generating fact/index rows for retrieval. Commonplace could use the same split for generated indexes or source snapshots: symbolic facts improve lookup, but the cited Markdown remains reviewable evidence. Ready as a design pattern; automation needs stricter validation before broad use.

**Playbook execution logs as learning input.** WUPHF records playbook runs and offers synthesis back into playbook text. Commonplace instructions could benefit from append-only execution notes that later propose revisions, especially for brittle operational procedures. Needs review gates so one failed run does not rewrite durable instructions too quickly.

**Single-writer queue for wiki mutation.** The wiki worker serializes writes, index regeneration, events, and backup mirroring. Commonplace currently relies on git discipline and validation; a queue is unnecessary for local single-agent editing, but the pattern is useful if future MCP write tools or concurrent agents mutate the same KB.

## Trace-derived learning placement

**Trace source.** WUPHF qualifies as trace-derived learning. Its raw signals include agent-authored notebook entries, committed artifacts, task memory workflow events, playbook execution records, team learning records with `source` fields such as observed/execution/synthesis/cross-agent, wiki write history, fact extraction DLQ records, and lint reports. The older auto-notebook writer is explicitly retained but not wired in production, so ordinary chat/task transitions should not be counted as automatic durable trace capture at this commit ([internal/team/auto_notebook_writer.go](https://github.com/nex-crm/wuphf/blob/83393b2c5e4a66754062fbd2b4cda7e9ec2dd299/internal/team/auto_notebook_writer.go)).

**Extraction.** Extraction is mixed. Some paths are agent-initiated and explicit: `notebook_write`, `context_capture`, `notebook_promote`, `team_learning_record`, and `playbook_execution_record`. The more automatic path is `wiki_extractor.go`: after an artifact commit, it reads the artifact, renders an entity-extraction prompt, parses JSON, resolves entities, computes fact IDs, submits facts, and records validation/provider failures in a DLQ. The oracle is therefore a mix of agent judgment, reviewer approval, LLM extraction, resolver gates, lint checks, and execution outcome labels.

**Scope and timing.** Scope is workspace/team oriented, with per-agent notebook shelves and shared wiki paths. Timing is staged rather than purely online: memories are captured during or after work, promoted or extracted after a write, reconciled periodically, and then consumed in future tasks through lookup, search, prompt injection, playbook lists, or compiled skills.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), WUPHF belongs with trace-to-readable-artifact and trace-to-symbolic-index systems. It strengthens the survey's distinction between retained trace evidence and distilled behavior-shaping surfaces: notebook entries and artifacts are evidence/candidates; promoted wiki articles, fact logs, learnings, and compiled playbooks are the durable outputs that can change later behavior.

**Curation policy.** WUPHF is strongest where it requires explicit promotion or validation: notebook promotion has reviewer state, direct wiki writes require human delegation unless bypassed, and lint can resolve contradictions by mutating fact validity. It is weaker where LLM extraction creates typed facts from artifacts: the code has sanitization, resolver gates, DLQ, and source paths, but this review did not find a claim-level human approval gate before extracted facts influence typed retrieval.

## Read-back placement

**Read-back:** `both` — WUPHF has pull through MCP/wiki/notebook/context tools and engineered push through broker-woken agent turns that append scoped memory briefs before the next provider action.

**Direction.** Pull paths include notebook search/read/list, wiki search/read/list/lookup, context lookup, playbook list, team learning search, and legacy Nex/GBrain shared queries. Push exists when broker events wake agents and the headless runner appends scoped memory briefs to the incoming notification before the provider acts. The default Markdown wiki/notebook surface is pull by tool call; the automatic prompt brief uses broker private memory and any active external memory backend rather than pushing the wiki by default.

**Targeting and signal.** Pull triggers are explicit agent/user tool calls and slash commands. Push memory targeting is `instance`: each headless turn's notification text becomes the query for `fetchScopedMemoryBrief`. The private-memory path is `inferred / lexical`, because it matches the notification against the retained note key, title, and content with substring/token scoring and a small top-k cap. The shared external path is backend-dependent: GBrain is `inferred / embedding` when vector search is configured, with keyword/reduced-mode fallback; Nex recall is an opaque external API query, so the review can identify it only as inferred query-based recall from local code. The broker wake itself is also event-keyed by messages, focus/collab mode, mentions, active tasks, and channel membership, but those symbols decide which agent wakes, not which memory snippet is selected.

**Timing relative to action.** Pushed memory arrives before the provider turn performs tool calls or writes output. It is appended to stdin after the operator notification and before the model acts, which means it can change the next action rather than only audit the result.

**Selection, scope, and complexity.** Complexity controls include per-agent private namespaces, shared/private scope switches, literal notebook search, wiki top-k lookup, context lookup limits/timeouts, backend choice, agent-specific MCP manifests, and fresh-session turns. The pushed brief is short, but it is still prose context; precision and context dilution depend on search quality and backend behavior at runtime.

**Authority at consumption.** The code deliberately lowers authority for pushed external memory by wrapping it as background, untrusted data and warning the model not to treat embedded instructions as operator commands. The same retrieved content can still become behavior-shaping advice because it is in the model's prompt; effective authority depends on the model following the wrapper and the surrounding system prompt.

**Faithfulness.** WUPHF has tests and benchmarks for many subsystems, including lookup, MCP tools, wiki behavior, and token/performance claims, but this review did not find a WITH/WITHOUT ablation showing that a particular pushed memory brief changed agent behavior in the intended direction. The `push-activation` tag is therefore structural, not a measured faithfulness claim.

**Other consumers.** Humans consume the wiki UI, notebooks, lint reports, promotion cards, task memory workflow state, and channel messages. Background workers consume queues, indexes, extraction DLQs, playbook execution logs, and wiki events. External agents consume MCP tools.

## Curiosity Pass

**The README promise is more coherent than the implementation surface is small.** WUPHF's memory story is readable in the README, but the actual system spans broker state, wiki git operations, MCP tools, UI, extraction, lint, learning logs, playbooks, and legacy backends. That breadth is useful for an office runtime and hard to review as a single "memory system."

**The auto-notebook comment changes the trace-derived decision.** A superficial scan would treat message/task hooks as automatic trace learning. The current code says that hook is intentionally not wired in production, so trace-derived status rests on explicit capture/promotion/extraction/learning/playbook paths instead.

**The wiki is both source and product UI.** WUPHF leans into Wikipedia-like presentation, but the operational core is still git-backed Markdown. That is an adoption advantage for users who want files, while the UI and MCP tools add enough structure for agents to treat it as memory infrastructure.

**Prompt-injection handling is unusually explicit.** The memory wrapper does not solve all authority problems, but it correctly treats external context as hostile data. That is a concrete improvement over memory systems that push retrieved text without source-authority framing.

**Extracted facts can outrun review.** The fact extractor has useful guardrails, but generated facts can shape typed retrieval. This is the design pressure point: symbolic indexes are powerful because they route future answers, so their trust state matters.

## What to Watch

- Whether extracted facts gain a review/approval state before they influence typed retrieval and contradiction lint; that would make WUPHF's generated symbolic layer safer as system-definition infrastructure.
- Whether pushed memory gets behavioral faithfulness tests, such as perturbing private/wiki hits and measuring downstream action changes; that would turn `push-activation` from structural to evaluated.
- Whether notebook promotion states become visible enough for agents to avoid citing unapproved scratch as team truth; this decides how cleanly draft and canonical authority stay separated.
- Whether playbook execution synthesis automatically edits playbook source or only proposes revisions; automatic synthesis would need stronger evidence thresholds and rollback.
- Whether legacy Nex/GBrain paths continue to shrink behind the Markdown wiki; mixed backends complicate lineage and authority because similar tools can return very different evidence shapes.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: WUPHF needs separate treatment for wiki files, notebooks, facts, indexes, tool schemas, prompts, workflows, playbooks, and lint reports.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - extends: WUPHF does not stop at storage; it pushes scoped memory into fresh agent turns.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: WUPHF turns artifacts, notebook captures, executions, and learnings into durable knowledge/index/playbook surfaces.
- [Activate behavior-changing memory before the mistake](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: WUPHF's memory brief fires before a provider turn, though faithfulness is not proven from code.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: WUPHF's tool schemas, workflow states, fact indexes, playbooks, and lint resolutions shape future behavior with more force than ordinary notes.
