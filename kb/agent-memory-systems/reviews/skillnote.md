---
description: "SkillNote review: self-hosted SKILL.md registry with collections, imports, sync adapters, usage/rating feedback, and prompt-derived draft candidates"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-05"
---

# SkillNote

SkillNote, from `luna-prompts/skillnote`, is a self-hosted registry for `SKILL.md` files. At the reviewed commit it combines a Next.js web UI, FastAPI/PostgreSQL backend, npm CLI, Claude Code plugin, OpenClaw skill bundle, and MCP server so teams can create, import, version, scope, sync, and rate reusable agent skills.

**Repository:** https://github.com/luna-prompts/skillnote

**Reviewed commit:** [7303ba7ab2098f9675e320fd68296458b4703752](https://github.com/luna-prompts/skillnote/commit/7303ba7ab2098f9675e320fd68296458b4703752)

**Last checked:** 2026-06-05

## Core Ideas

**The registry stores skill instructions as database rows, then materializes them back to native agent formats.** The main `skills` row stores name, slug, description, Markdown body, collections, extra frontmatter, import lineage, source path/SHA, and fork status; each browser/API save creates a `skill_content_versions` snapshot. Claude sync writes project-local `.claude/skills/skillnote-*/SKILL.md`, OpenClaw sync writes `~/.openclaw/skills/sn-*/SKILL.md`, and the MCP server exposes each skill row as a live MCP tool whose call returns the full skill body ([backend/app/db/models/skill.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/db/models/skill.py), [backend/app/db/models/skill_content_version.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/db/models/skill_content_version.py), [plugin/hooks-handlers/sync.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/hooks-handlers/sync.sh), [plugin-openclaw/skillnote/sync.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin-openclaw/skillnote/sync.sh), [backend/mcp_server.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/mcp_server.py)).

**Context efficiency is collection scoping plus native skill discovery, not semantic memory retrieval.** The product is explicitly motivated by Claude Code's active skill-description budget and uses per-project collections to keep the active skill set around the expected 12-15 skill range. Filtering is symbolic: `.skillnote.json` names collections, sync fetches `/v1/skills?collections=...`, and the backend filters `skills.collections` arrays case-insensitively ([README.md](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/README.md), [plugin/hooks-handlers/sync.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/hooks-handlers/sync.sh), [backend/app/api/skills.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/skills.py), [plugin/skills/collection/SKILL.md](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/skills/collection/SKILL.md)).

**Imports retain upstream lineage and fork state.** GitHub imports inspect a source, clone and scan `SKILL.md` files, persist an `import_sources` row with owner/repo/ref/SHA/subpath/status, and attach per-skill source path, source SHA, content hash, and `forked_from_source` status. Later manual edits flip `forked_from_source`, so refresh paths can distinguish local divergence from upstream drift ([backend/app/db/models/import_source.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/db/models/import_source.py), [backend/app/services/imports/inspector.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/services/imports/inspector.py), [backend/app/services/imports/importer.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/services/imports/importer.py), [backend/app/api/skills.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/skills.py)).

**Read-back is adapter-specific.** Claude Code gets hooks that sync skills, prompt for collection selection, preserve skill context after compaction, and prompt for ratings after skill use. OpenClaw gets an always-loaded skill plus sidecar instructions that tell the agent to sync, inspect relevant `sn-*` skills before work, and log/rate afterwards. MCP clients get tools whose descriptions are the skill descriptions, plus PostgreSQL `LISTEN/NOTIFY` updates for tool-list refresh ([plugin/hooks/hooks.json](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/hooks/hooks.json), [plugin/hooks-handlers/compact-context.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/hooks-handlers/compact-context.sh), [plugin-openclaw/skillnote/SKILL.md](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin-openclaw/skillnote/SKILL.md), [plugin-openclaw/skillnote/sync.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin-openclaw/skillnote/sync.sh), [backend/mcp_server.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/mcp_server.py)).

**Feedback becomes ranking and review signal, not automatic rewriting.** Skill calls, usage events, comments, and ratings are persisted and surfaced through analytics. The OpenClaw context-bundle endpoint sorts candidates by 30-day usage and rating before handing the bundle to an agent-side resolver, and low ratings or deprecation comments mark a skill as `needs_review`. The inspected code does not automatically rewrite a stored skill from the feedback; it changes visibility, review priority, and operator evidence ([backend/app/db/models/analytics_event.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/db/models/analytics_event.py), [backend/app/db/models/skill_usage_event.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/db/models/skill_usage_event.py), [backend/app/api/analytics.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/analytics.py), [backend/app/api/openclaw.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/openclaw.py), [backend/app/api/comments.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/comments.py)).

**There is a trace-derived draft path, but promotion stays explicit.** The Claude `UserPromptSubmit` hook watches user prompts for explicit save phrases and convention markers. Explicit phrases inject guidance telling Claude to follow the `skill-push` flow; convention markers silently write `.skillnote/drafts/*.md` candidate notes with the matched evidence sentence, signal, timestamp, session id, and next-step instruction. The actual registry push still requires skill-push drafting, collection choice, review, and API write ([plugin/hooks-handlers/prompt-watch.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/hooks-handlers/prompt-watch.sh), [plugin/skills/skill-push/SKILL.md](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/skills/skill-push/SKILL.md)).

## Artifact analysis

- **Storage substrate:** `rdbms` `files` `repo` `in-memory` — The authoritative registry lives in PostgreSQL tables for skills, content versions, published versions, collections, import sources, comments, ratings, usage, and call events; adapters materialize those rows into local `SKILL.md` files, project `.skillnote.json`, manifests, OpenClaw sidecars, and draft files; imported skills retain repo source coordinates; MCP session registries and context-bundle candidate ranking are in-memory request-time surfaces.
- **Representational form:** `prose` `symbolic` — Skill bodies, descriptions, comments, outcomes, sidecar instructions, prompt-derived drafts, and `SKILL.md` files are prose; frontmatter, slugs, collections, content hashes, version/checksum rows, JSON manifests, hook definitions, shell/Python/TypeScript adapters, API schemas, and database models are symbolic. The inspected implementation does not persist embeddings or model weights.
- **Lineage:** `authored` `imported` `trace-extracted` — Users and agents author skills through the web/API/skill-push path; marketplace/GitHub import copies skills from upstream `SKILL.md` files with source SHA/path/hash; prompt-watch drafts and analytics/rating records are extracted from session events, user prompts, tool calls, and agent feedback.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Skill text is consumed as knowledge and instruction by agents; collections, `.skillnote.json`, MCP tool lists, and OpenClaw context bundles route which skills are visible; validators and import guards enforce bundle/name/collection/path rules; usage/rating/comment aggregates rank and flag skills; prompt-watch and skill-push create a learning path from repeated interaction patterns to candidate or published skills.

**Skill rows and content versions.** Storage substrate: PostgreSQL `skills` and `skill_content_versions`. Representational form: prose descriptions/bodies plus symbolic slug, collections, version number, source metadata, and extra frontmatter. Lineage: authored manually or imported from upstream, with every save creating a version snapshot. Behavioral authority: system-definition instruction when synced or exposed as a tool, and knowledge/advice when browsed by a human.

**Local adapter materializations.** Storage substrate: project `.claude/skills/skillnote-*/SKILL.md`, `~/.openclaw/skills/sn-*/SKILL.md`, manifest JSON, sync timestamps, and `~/.openclaw/skillnote-agents.md`. Representational form: `SKILL.md` prose/frontmatter plus shell-generated manifests. Lineage: derived copies from the registry, invalidated by sync interval, collection filter, and manifest comparison. Behavioral authority: instruction and routing because these files determine what the native agent skill system discovers.

**Import-source records.** Storage substrate: PostgreSQL `import_sources` plus per-skill source fields. Representational form: symbolic source type, host, owner, repo, ref, subpath, SHA, status, and hash. Lineage: imported source metadata derived from GitHub/API/clone inspection. Behavioral authority: validation, review, and refresh governance, not direct agent instruction.

**Usage, ratings, and comments.** Storage substrate: PostgreSQL event/comment/rating tables and OpenClaw session watcher state. Representational form: symbolic event fields plus prose outcomes/comments. Lineage: trace-extracted from MCP `tools/call`, Claude `PostToolUse`, OpenClaw JSONL skill reads, explicit usage posts, and agent comments. Behavioral authority: ranking and review signal; these records affect dashboards, context-bundle sorting, `needs_review` status, and operator decisions rather than rewriting skills.

**Prompt-derived drafts.** Storage substrate: project `.skillnote/drafts/*.md` files. Representational form: prose draft notes with symbolic frontmatter fields for trigger, signal, timestamp, session id, and status. Lineage: trace-extracted from `UserPromptSubmit` prompt text. Behavioral authority: knowledge and learning candidate; they are not active skill instructions until an agent/user promotes them through `skill-push` or another write path.

**MCP tool surface.** Storage substrate: PostgreSQL plus live FastMCP provider state. Representational form: symbolic tool schema and prose tool description/content. Lineage: derived from current skill rows on each list/get call; list-change notifications are driven by PostgreSQL `NOTIFY`. Behavioral authority: routing and instruction because the tool list is the agent-facing discovery surface and tool calls return the skill instructions.

Promotion path: SkillNote can move a pattern from prompt evidence to a draft candidate, from draft/manual authoring/import into a registry skill, from registry skill into adapter-local `SKILL.md` or MCP tool instructions, and from usage/ratings/comments into ranking or `needs_review` signals. It does not yet promote low-rated feedback into automatic skill rewrites or a validated repair workflow.

## Comparison with Our System

| Dimension | SkillNote | Commonplace |
|---|---|---|
| Primary purpose | Shared operational skill registry for coding agents | Source-grounded methodology KB for agent-operated knowledge bases |
| Main retained artifact | `SKILL.md` instructions in PostgreSQL, synced files, MCP tools, and plugin bundles | Typed Markdown notes, instructions, reviews, sources, indexes, schemas, and commands |
| Context control | Collection-scoped skill discovery, native agent skill loading, MCP tool filtering | Search/index/link navigation, collection/type contracts, validation, review gates, selective skill loading |
| Write path | Web/API/CLI import, manual editing, version snapshots, prompt-derived draft candidates | File edits, collection contracts, validation, review, generated indexes, source snapshots |
| Read-back | Both pushed catalog/skills and explicit skill/tool reads | Mostly explicit pull, with loaded instructions and skills where selected by the harness |
| Governance | Import validation, content versions, source hash/SHA, checksums, ratings/comments, usage analytics | Type validation, link checks, source citations, semantic review, git history, collection-local contracts |

SkillNote and Commonplace share a local-file adoption bet: agents operate best when durable knowledge can be inspected, edited, diffed, and loaded through the toolchain they already trust. SkillNote differs by making the database the coordination point and materializing to files per agent, while Commonplace treats the repository files as the authoritative store.

The most useful divergence is authority management. SkillNote is comfortable making a registry skill active in an agent's native instruction system once it belongs to a collection. Commonplace usually keeps most knowledge as advisory pull context until a type contract, instruction, validator, or command grants stronger authority.

The trace-derived draft path is also more opportunistic than Commonplace's current review culture. SkillNote detects convention language and writes a draft candidate immediately, but requires explicit user/agent promotion before publication. That is a clean halfway state: cheap capture without pretending the capture is already a reviewed skill.

### Borrowable Ideas

**Per-project skill collections as a first-class context budget.** Ready for a concrete Commonplace skill-loading workflow. Commonplace could keep instruction bundles small by letting a project choose named operational skill sets, with a visible cap and status output.

**Materialize remote or database-backed knowledge into native local files.** Ready as an adapter principle. SkillNote avoids asking Claude Code/OpenClaw to consume a bespoke registry protocol; it writes the files those agents already understand. Commonplace should prefer native harness surfaces when exporting selected KB procedures.

**Prompt-derived draft capture with manual promotion.** Ready for workshop use. A Commonplace hook could capture repeated "from now on" or "our convention" prompts into `kb/work/` drafts, but promotion to `kb/instructions/` should still require review, frontmatter, and validation.

**Feedback as ranking/review signal before auto-rewrite.** Ready now. SkillNote's ratings and comments influence visibility and `needs_review` without mutating the underlying skill text. Commonplace review queues could borrow that separation between use signal and artifact edits.

**Do not borrow database authority without a repo export story.** Needs a stronger use case. SkillNote's database makes live sync and analytics natural, but Commonplace's value depends on repo-native lineage, review, and reproducible diffs. A Commonplace registry would need bidirectional export or source-of-truth clarity before using a database as the canonical store.

## Write side

**Write agency:** `manual` `automatic` — Humans and agents create, edit, import, publish, restore, and delete skills through the web/API/CLI/skill-push paths; automatic hooks sync registry rows to local skill files, record skill calls/usage/ratings, notify MCP clients, and create draft candidates from prompt signals.

**Curation operations:** `promote` — Usage counts, ratings, comments, deprecation warnings, and recent comments do not rewrite skill bodies, but they change salience and review state in analytics and OpenClaw context-bundle sorting. The inspected code does not automatically consolidate, deduplicate, evolve, synthesize, invalidate, or decay existing skill content.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — SkillNote consumes Claude hook events, OpenClaw session JSONL reads, MCP `tools/call` events, explicit OpenClaw usage posts, agent comments/ratings, and `UserPromptSubmit` prompt text.

**Learning scope:** `per-project` `cross-task` — Claude prompt drafts are written under the active project; registry skills, ratings, and usage analytics are reusable across tasks and agents once synced or exposed through the registry.

**Learning timing:** `online` `staged` — Hooks run during sessions and can write draft candidates or log use immediately; publishing a durable skill from those candidates is staged through skill-push/manual review.

**Distilled form:** `prose` `symbolic` — Prompt-watch writes prose candidate notes with symbolic metadata; registry publication produces `SKILL.md` prose plus frontmatter, collection, version, and source fields.

**Trace source.** The strongest trace-derived path is `prompt-watch.sh`: it reads the current user prompt from the Claude hook input, ignores subagent prompts, checks that SkillNote is active for the project, and detects explicit save phrases or convention markers. Separately, MCP middleware logs tool calls, OpenClaw's watcher scans session JSONL files for reads of `sn-*/SKILL.md`, and the plugin hooks prompt agents to rate skills after use.

**Extraction.** Explicit save phrases do not create a registry skill; they inject additional context telling Claude to follow the skill-push workflow. Convention markers create a Markdown draft containing the matched evidence sentence, signal, timestamp, session id, and next step. The oracle is lexical pattern matching, not semantic judgment. Ratings and usage events are extracted from tool calls and agent posts, then used as analytics/ranking evidence.

**Scope and timing.** Prompt-derived candidates are project-local and pending; they become cross-agent only after a deliberate publication step. Usage/rating traces are cross-task registry evidence as soon as they are posted, but they affect ranking/review, not the skill body.

**Survey placement.** SkillNote occupies a conservative trace-derived corner: online event capture produces draft candidates and feedback records, while durable system-definition authority still requires explicit skill publication. It strengthens the survey distinction between trace-derived candidate knowledge and promoted instructions.

## Read-back

**Read-back:** `both` — Registry memory reaches agents by push when active collections are synced into native skill directories, OpenClaw sidecar instructions are loaded, MCP tool lists expose skill descriptions, or hooks re-inject active-skill context; full skill bodies can also be pulled through native skill invocation, explicit file reads, REST/API reads, or MCP tool calls.

**Read-back signal:** `coarse` `identifier` `inferred / judgment` — Coarse push appears as the active collection's whole skill catalog; identifier selection uses collection names, `.skillnote.json`, slug/tool names, and agent adapter choice; the OpenClaw context-bundle and sidecar workflow afford agent-side judgment over descriptions/task summaries, while the server itself does not perform semantic ranking.

**Faithfulness tested:** `no` — The implementation records calls, ratings, comments, outcomes, usage, and dashboards, but I did not find an ablation or audit that proves a pushed or selected skill changed the agent's downstream behavior.

**Direction edge cases.** A user choosing a collection is explicit pull from the user's perspective, but once `.skillnote.json` exists the active collection is pushed to Claude Code through `SessionStart` and 60-second `UserPromptSubmit` syncs. MCP tools are similar: clients may pull a tool body, but the tool list itself is a pushed discovery surface from the registry.

**Targeting and signal.** Claude collection scoping is symbolic and project-local: `.skillnote.json` chooses collections and sync writes only matching skills. OpenClaw's shipped `SKILL.md` tells agents to inspect synced `sn-*` descriptions before work, and the API's context-bundle accepts task summary, channel, workspace, recent skill ids, and collection filters, but its own server-side sort is usage/rating/name rather than semantic relevance. The LLM-side resolver is host behavior, not a server guarantee.

**Injection point.** Claude sync happens at session start, file-change, prompt-submit, post-tool-use, post-compact, and subagent-start hooks. OpenClaw sync runs from the always-loaded SkillNote skill and writes local skills plus the sidecar. MCP read-back happens at tool-list and tool-call time before the model can use the selected instruction.

**Selection, scope, and complexity.** SkillNote controls volume mostly by collections and adapter conventions. Claude sync can fetch all skills or comma-filtered collections; OpenClaw sync fetches all skills but the sidecar instructs the agent to read only relevant `sn-*` files, with a v1 method of frontmatter scan, at most three selected full reads, and a hard cap of five. Effective context dilution is not verified from code.

**Authority at consumption.** Synced `SKILL.md` files and MCP skill tools have instruction authority inside the host agent's native skill system. Usage/rating/comment records have ranking and review authority. Prompt-derived drafts remain advisory candidate knowledge until promoted.

**Faithfulness.** The analytics system can show that a skill was called/read and how an agent rated it, but those are self-report and event logs. SkillNote does not compare with/without a skill, perturb a fired skill, or audit whether the agent followed the instruction.

**Other consumers.** Human operators use the web UI, analytics dashboard, version history, import workspace, comments, ratings, and source/fork metadata. The same retained artifacts therefore serve agents as instructions and humans as governance evidence.

## Curiosity Pass

**The registry is memory infrastructure, but the active memory unit is still a skill description.** Context efficiency depends heavily on authors writing high-signal descriptions and collections staying small; the code enforces some collection/name rules but not semantic trigger quality.

**MCP support shifts SkillNote toward tool-discovery memory.** Unlike local sync, the MCP server can broadcast `tools/list_changed`, so the agent-facing catalog can refresh without file polling. That is a different read-back profile from Claude/OpenClaw native skill folders.

**The strongest trace-derived mechanism is intentionally weak authority.** Prompt-watch captures candidate drafts, not published skills. That restraint matters: lexical convention detection is too noisy to grant instruction authority automatically.

**Ratings are useful but easy to overtrust.** A low rating can mark a skill as needing review, and high usage can raise it in context-bundle sorting, but ratings remain agent self-report unless paired with outcome audits.

**The source-of-truth boundary is split.** PostgreSQL is canonical for registry content, while synced local files are what agents actually consume. That split is operationally useful, but debugging stale behavior requires checking sync state, collection config, local materialization, and database rows.

## What to Watch

- Whether prompt-derived drafts gain a reviewed promotion workflow with source prompt links, duplicates, rejection state, and expiry; that would make trace-derived skill learning more auditable.
- Whether usage/ratings/comments start rewriting or repairing skill bodies automatically; that would change write-side classification from salience promotion toward evolve or synthesize.
- Whether the OpenClaw context-bundle resolver becomes a shipped server-side ranker or embedding retriever; that would add inferred read-back stronger than today's usage/rating pre-sort.
- Whether authentication and per-collection permissions land; without them, database-backed instruction authority is bounded to trusted local/LAN deployments.
- Whether SkillNote adds export/import round-tripping to Git repositories for the registry itself; that would reduce the audit gap between database state and reviewable diffs.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: SkillNote storage becomes behavior-shaping only when adapters sync, expose, or read back active skills.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: registry rows, synced files, import metadata, ratings, comments, prompts, and MCP tools have different forms and authorities.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - relates: prompt-watch turns interaction traces into skill candidates while preserving manual promotion.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: drafts, comments, ratings, and usage records provide evidence or advice before they become instructions.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: published and synced `SKILL.md` files can instruct agents through native skill systems.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - relates: SkillNote's targeting relies on slugs, collections, paths, tool names, and descriptions.
