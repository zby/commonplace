---
description: "SkillNote review: self-hosted skill registry, collection-scoped sync, agent-native hooks, MCP tool exposure, usage analytics, and draft skill capture"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-02"
---

# SkillNote

> Replaced 2026-06-05. See [SkillNote](./skillnote.md) for the current review.

SkillNote, by luna-prompts, is a self-hosted registry and distribution system for `SKILL.md` files used by AI coding agents. The inspected repository ships a Next.js web UI, FastAPI/PostgreSQL backend, npm/Docker lifecycle CLI, Claude Code plugin, OpenClaw skill bundle, MCP server, GitHub import flow, versioned skill publishing, collection scoping, and analytics paths that record which skills agents used.

**Repository:** https://github.com/luna-prompts/skillnote

**Reviewed commit:** [7303ba7ab2098f9675e320fd68296458b4703752](https://github.com/luna-prompts/skillnote/commit/7303ba7ab2098f9675e320fd68296458b4703752)

**Last checked:** 2026-06-02

## Core Ideas

**The retained unit is a native agent skill, not a remote memory record.** SkillNote stores skill name, slug, description, body, collections, extra frontmatter, import origin, and version counters in PostgreSQL, but the agent-facing artifact is still a local `SKILL.md` file written into the host agent's native skill directory ([skill.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/db/models/skill.py), [sync.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/hooks-handlers/sync.sh), [plugin-openclaw/skillnote/sync.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin-openclaw/skillnote/sync.sh)). That gives the registry centralized editing and sharing while preserving Claude Code and OpenClaw's on-disk skill semantics.

**Collections are the primary context-efficiency control.** Claude Code sync reads `.skillnote.json`, filters `/v1/skills?collections=...`, writes only the selected collection into project-local `.claude/skills/`, and removes stale `skillnote-*` directories from the managed set ([sync.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/hooks-handlers/sync.sh)). The backend enforces a 15-skill collection limit in `validate_skill_count`, matching the README's claim that SkillNote addresses Claude Code's shared skill-description budget by scoping active skills ([skill_validator.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/validators/skill_validator.py), [README.md](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/README.md)). Complexity is bounded by collection membership and by native skill progressive disclosure: descriptions are visible up front, full bodies are loaded only through the host skill mechanism.

**Agent integration is mostly hook and filesystem plumbing.** The Claude Code plugin wires `SessionStart`, `FileChanged`, `UserPromptSubmit`, `PostToolUse`, `PostCompact`, and `SubagentStart` hooks; sync is blocking only on startup/resume/compact, while usage tracking and auto-sync paths are async ([hooks.json](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/hooks/hooks.json)). The picker writes `.skillnote.json`, sync materializes the selected skills, compact/subagent hooks re-inject active collection context, and post-tool hooks ask the agent to rate a skill after use ([skillnote-pick](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/bin/skillnote-pick), [compact-context.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/hooks-handlers/compact-context.sh), [subagent-context.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/hooks-handlers/subagent-context.sh), [skill-used-context.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/hooks-handlers/skill-used-context.sh)).

**Skill publishing and imports preserve lineage, but not full proof.** Manual API saves snapshot a `SkillContentVersion` on every create/update/restore; bundle publication validates a ZIP, extracts `SKILL.md` metadata, stores the bundle by slug/version, and verifies checksums on download ([skills.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/skills.py), [publish.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/publish.py), [downloads.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/downloads.py)). GitHub import shallow-clones or sparse-checkouts source repositories, scans `SKILL.md`, records source URL/ref/subpath/SHA/path/content hash, detects upstream drift, and marks edited imported skills as forked ([cloner.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/services/imports/cloner.py), [importer.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/services/imports/importer.py), [refresher.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/services/imports/refresher.py)).

**Analytics are designed to shape future selection.** Claude Code hook events and MCP tool calls write `skill_call_events`; OpenClaw agents post richer `skill_usage_events`; ratings and comments are aggregated into summaries, leaderboards, context-bundle metadata, and staleness flags ([hooks.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/hooks.py), [analytics.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/analytics.py), [openclaw.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/openclaw.py), [comments.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/comments.py)). SkillNote does not automatically rewrite a skill from those traces, but the traces affect future ranking, review attention, and agent self-report.

**MCP is an alternate read-back surface.** The MCP server exposes each database skill as a tool whose description is the skill trigger and whose call returns the full skill body; it listens for PostgreSQL `NOTIFY` events and broadcasts `tools/list_changed` to connected clients after skill changes ([mcp_server.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/mcp_server.py)). This makes the same registry usable by agents that can consume MCP tools instead of on-disk skill folders.

## Artifact analysis

- **Storage substrate:** `rdbms` — PostgreSQL tables `skills` and `skill_content_versions`
- **Representational form:** `prose` `symbolic` — Skill bodies, descriptions, comments, outcomes, and drafts are prose, while slugs, collections, manifests, version counters, import fields, hashes, ratings, events, hooks, and bundle metadata are symbolic control state
- **Lineage:** `authored` `imported` `trace-extracted` — Skills are authored in the web/API, imported from GitHub or bundles, and supplemented by usage events, ratings, comments, session reads, and prompt-derived drafts
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Browseable history and drafts are knowledge artifacts; synced skills and hooks instruct; collection limits, manifests, and checksum/drift paths constrain activation; collections and MCP tools route; validators and import checks govern; analytics rank and trace signals feed later selection

**Registry skill rows and content versions.** Storage substrate: PostgreSQL tables `skills` and `skill_content_versions`. Representational form: mixed prose and symbolic state: `description` and `content_md` are prose instruction bodies, while slug, collections, current version, extra frontmatter, import fields, source hashes, and latest-version flags are symbolic control metadata. Lineage: authored in the web/API, imported from GitHub scans, restored from previous versions, or published from ZIP bundles; create/update/restore snapshots preserve previous content state, but ordinary versions do not embed evidence that the instruction is true. Behavioral authority: system-definition artifacts when rendered as local `SKILL.md` files, MCP tools, or OpenClaw bundle entries; knowledge artifacts when humans browse or compare history.

**Synced local skill files.** Storage substrate: project-local `.claude/skills/skillnote-*/SKILL.md` for Claude Code and `~/.openclaw/skills/sn-*/SKILL.md` for OpenClaw. Representational form: mixed YAML frontmatter and Markdown instructions. Lineage: generated from database rows by sync scripts, with URL placeholder substitution and collection prefixes; stale files are removed according to manifest ownership. Behavioral authority: system-definition artifacts consumed by the host agent's native skill loader, with trigger authority carried mainly by `description` and operative authority carried by the full body.

**Collection selection and manifests.** Storage substrate: `.skillnote.json` in the project, per-plugin `.skillnote-manifest.json`, the backend `collections` table, and arrays on `skills.collections`. Representational form: symbolic JSON/table metadata. Lineage: user picks or creates collections through the picker/API; sync regenerates manifests from current server results. Behavioral authority: routing and scope authority. These artifacts decide which skills are visible to a project before the agent does any task-level reasoning.

**Import-source records and bundle artifacts.** Storage substrate: PostgreSQL `import_sources`, per-skill origin fields, downloaded/uploaded ZIP bundles under configured bundle storage, and transient shallow clones during import. Representational form: symbolic source metadata, hashes, refs, paths, ZIP archives, and copied Markdown bodies. Lineage: imported from external GitHub repositories or uploaded bundles; drift detection compares upstream SHA/content hashes and records forked status after local edits. Behavioral authority: governance and invalidation authority. They do not usually affect the next agent action directly, but they decide whether a skill is treated as upstream-derived, forked, drifted, or safely downloadable.

**Hook, plugin, and sidecar instruction artifacts.** Storage substrate: Claude Code plugin files under `~/.claude/plugins/...`, shell wrapper entries, picker binaries, OpenClaw `skillnote` bundle files, `~/.openclaw/skillnote-agents.md`, and OpenClaw config JSON. Representational form: shell/Python/JSON symbolic machinery plus prose instructions. Lineage: generated or installed from the SkillNote backend/plugin bundle and periodically refreshed. Behavioral authority: strong system-definition authority because these artifacts run before prompts, sync skills, inject additional context, graft instructions into OpenClaw, record usage, and ask for ratings.

**Usage, rating, comment, and connection records.** Storage substrate: PostgreSQL `skill_call_events`, `skill_usage_events`, `skill_ratings`, `comments`, in-memory MCP connection state, and local OpenClaw watcher state JSON. Representational form: symbolic events plus prose outcomes/comments. Lineage: trace-derived from Claude Code `PostToolUse[Skill]`, MCP `tools/call`, OpenClaw session JSONL skill reads, explicit usage posts, agent ratings, and comments. Behavioral authority: ranking, audit, staleness, and curation authority. They shape future OpenClaw context-bundle ordering and human dashboard attention; they are not ordinary evidence that a skill's content is correct.

**Draft skill candidates.** Storage substrate: project-local `.skillnote/drafts/*.md` written by the Claude Code `UserPromptSubmit` hook. Representational form: Markdown draft with YAML metadata and quoted prompt evidence. Lineage: trace-extracted from user prompt text matching convention-signaling regexes such as "from now on", "always", and "never"; explicit save phrases instead inject context that tells the agent to run the `skill-push` workflow. Behavioral authority: weak knowledge-artifact / candidate authority until a human or agent confirms and publishes through the API; the draft alone does not become an active skill ([prompt-watch.sh](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/hooks-handlers/prompt-watch.sh), [skill-push/SKILL.md](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/plugin/skills/skill-push/SKILL.md)).

The promotion path is explicit rather than fully autonomous: prompt or usage traces can become draft candidates, ratings, comments, and ranking signals; a skill becomes behavior-shaping only after publication or sync into the agent's native surface. SkillNote has strong promotion from registry row to active skill, but weak automatic promotion from trace to trusted procedure.

## Comparison with Our System

| Dimension | SkillNote | Commonplace |
|---|---|---|
| Primary purpose | Distribute reusable agent skills across teams and agents | Maintain a typed methodology KB and review corpus for future agents |
| Main substrate | PostgreSQL registry plus generated local `SKILL.md` files, plugin hooks, MCP tools, and ZIP bundles | Git-tracked Markdown artifacts, type specs, validation, indexes, review gates, and source snapshots |
| Context control | Collection scoping, native skill descriptions, OpenClaw bundle caps, MCP tool filtering | `rg`, curated indexes, path/type scoping, frontmatter descriptions, skills, and validation |
| Learning loop | Usage events, ratings, comments, prompt-signal draft files, OpenClaw usage-ranked bundles | Human/agent review, source-grounded notes, validation warnings, semantic gates, workshop promotion |
| Governance | Version snapshots, bundle checksum validation, import lineage, fork/drift flags, self-hosted access boundary | Collection contracts, schemas, link vocabulary, source-pinned citations, review archives, deterministic validation |
| Activation | Hooks, native skill loaders, MCP tools, OpenClaw sidecar/context bundle | Mostly deliberate pull via search/index/link navigation, with prescriptive instructions when invoked |

SkillNote and Commonplace share the premise that behavior-shaping knowledge should remain inspectable and editable. SkillNote packages that premise for adoption: it makes the active artifact a native `SKILL.md`, keeps synchronized copies on disk, and reaches agents through their real startup, hook, and tool surfaces. Commonplace is more conservative about authority: artifacts become durable through type contracts, source-grounding, validation, review, and git lifecycle rather than through usage counts or productized sync.

The main tradeoff is operational reach versus epistemic control. SkillNote can get a team's skills into many agent sessions quickly, and its hook surfaces help prevent skills from being forgotten. But that reach makes authority diffuse: a future action can be affected by collection picks, sync manifests, hook context, MCP tool descriptions, OpenClaw sidecars, ratings, comments, and registry rows. Commonplace keeps fewer activation paths and stronger review semantics, but that makes activation more manual.

**Read-back:** `both` — Registry skills are pull when an agent deliberately invokes an MCP tool or reads a selected local skill; they are push when startup/session hooks sync selected collections, native skill descriptions are made visible to the host agent, and compact/subagent hooks reintroduce active skill metadata. Prompt-hook workflow text and OpenClaw sidecar instructions are shipped baseline scaffolding, not read-back by themselves.

### Borrowable Ideas

**Project-scoped active-skill manifests.** Ready to borrow. Commonplace could keep a small local manifest of currently relevant instructions or notes for a project/workshop, with generated context constrained by that manifest rather than by the whole KB.

**Usage telemetry as navigation pressure, not truth.** Ready with constraints. SkillNote's call counts, ratings, comments, and OpenClaw context-bundle ordering are useful signals for what agents actually touch. Commonplace could use similar local analytics to find neglected or overused instructions, but should not let usage alone promote a claim's epistemic status.

**Draft candidates from convention-signaling prompts.** Needs a use case and review boundary. The `prompt-watch` split is good: explicit "save this" pushes a skill-creation workflow into context, while weaker signals create local drafts. Commonplace could capture candidate notes or instructions from repeated user corrections, but only into a workshop queue, not directly into the library.

**Agent-native distribution over bespoke runtime protocol.** Ready as an adoption lesson. SkillNote syncs to the substrate agents already consume instead of requiring every agent to call a custom service. Commonplace skills and instructions should prefer native harness surfaces where those surfaces preserve the artifact contract.

**Import lineage and fork flags for borrowed instructions.** Ready in principle. SkillNote records source path, source SHA, content hash, imported source, and forked status for imported skills. Commonplace could apply the same model to external instructions or examples that are adapted into local procedures.

**Do not borrow ratings as quality gates.** SkillNote ratings are appropriate for product analytics and selection hints. Commonplace should not treat a 5-star instruction as validated unless a review, test, or source-grounding check supports it.

## Write-side placement

**Write agency:** `automatic` `manual` — the review identifies a trace-derived or rule-driven path that changes retained memory from execution/session evidence; manual surfaces are included where the reviewed prose describes user or operator authoring.

**Curation operations:** `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

### Trace-derived learning
**Trace source:** `session-logs` `tool-traces` `event-streams` — SkillNote consumes OpenClaw session JSONL reads, Claude Code skill-use and MCP tool-call traces, hook events, usage posts, ratings/comments, and prompt text signals.

**Learning scope:** `per-task` `per-project` `cross-task` — Usage is session/task scoped, prompt drafts are project-local, and aggregated usage/rating signals steer later cross-task selection.

**Learning timing:** `online` `staged` — Events, drafts, ratings, and usage posts are written online, while promotion into active skills or context-bundle selection happens through later publish/sync or bundle-selection stages.

**Distilled form:** `prose` `symbolic` — Prompt drafts, comments, and skill bodies are prose; events, counts, ratings, rankings, manifests, and metadata are symbolic.

**Trace source.** SkillNote qualifies as trace-derived under the current rules, but only for specific paths. It consumes Claude Code skill-use hook events, MCP `tools/call` events, OpenClaw session JSONL reads of `sn-*/SKILL.md`, explicit OpenClaw usage posts, agent ratings/comments, and user prompt text that matches convention or "save this as a skill" patterns. It does not mine full coding transcripts into finished skills automatically.

**Extraction.** Extraction is mostly deterministic. Hook code extracts skill slug and session id; the MCP middleware extracts tool-call names and connection metadata; OpenClaw's watcher scans new JSONL lines for `read` calls ending in `/sn-*/SKILL.md`; analytics endpoints aggregate counts and ratings; `prompt-watch.sh` uses regexes to either inject `skill-push` context or write a draft candidate. The oracle for a finished skill remains human/agent confirmation through the `skill-push` workflow, not an automatic judge.

**Scope and timing.** Usage traces are session/task scoped and written online after skill calls or explicit usage posts. OpenClaw context bundles use 30-day usage and rating aggregates at selection time. Draft candidates are project-scoped local files created during `UserPromptSubmit`. Ratings and comments are post-action review signals.

**Survey placement.** SkillNote belongs in the trace-to-operational-signal and trace-to-draft-candidate branches of the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md). It strengthens the survey's distinction between raw trace retention and behavior-shaping distilled artifacts: events and comments steer future selection, while a durable active skill still requires an explicit publish/sync path.

## Read-back placement

**Read-back:** `both` — retained registry skills and skill metadata reach agents by pull when explicitly read or invoked, and by push when hooks or tool surfaces expose selected skills before the agent asks for a specific body.

**Direction.** Both. The strongest memory push paths are startup/session sync of registry skills into `.claude/skills/`, native skill-description exposure, MCP tool-list exposure, OpenClaw `sn-*` skill sync, and compact/subagent context that reintroduces active skill names. Pull remains present when an agent chooses a skill, reads a local `SKILL.md`, calls an MCP skill tool, or asks the registry/API for details. `UserPromptSubmit` explicit-save context and the OpenClaw sidecar's "check SkillNote" instruction are shipped workflow scaffolding; they can cause later read-back, but they are not retained memory read-back themselves.

**Read-back signal:** `coarse` `identifier` `inferred / judgment` — Push paths include coarse skill exposure/sync, collection and skill identifiers, and documented resolver or host-agent judgment over descriptions and task context.

**Faithfulness tested:** `no` — Tests cover mechanics, but the review found no with/without ablation or post-action audit proving pushed skills change downstream behavior.

**Targeting and signal.** Targeting is mixed. Claude Code sync is `instance` / `identifier` at the project-collection level: `.skillnote.json` names collections, the API query filters by those collection identifiers, and the generated skill frontmatter exposes descriptions to the host skill selector. The final choice of which synced skill body to apply is host-mediated from description and task context rather than settled by SkillNote's code. OpenClaw's background sync is `coarse` when it writes all registry skills to `sn-*` directories, while `/v1/openclaw/context-bundle` is mixed: optional `collection_filter` is an `identifier`, the server's usage/rating sort is a trace-derived ranking prior rather than semantic relevance, and the documented resolver subagent performs final `inferred / judgment` selection against `task_summary` ([openclaw.py](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/api/openclaw.py), [openclaw.py schema](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/backend/app/schemas/openclaw.py)). MCP activation is tool-list exposure plus client-side tool choice; the server can narrow by collection identifiers, then the MCP client/agent chooses by tool description.

**Injection point.** SessionStart and OpenClaw sidecar sync happen before task handling. UserPromptSubmit fires before Claude responds to a prompt. PostToolUse, usage posts, comments, and ratings happen after a skill is used and can shape later selection but not the just-completed action. PostCompact and SubagentStart reintroduce collection awareness after context transitions.

**Selection, scope, and complexity.** Code-grounded bounds include the 15-skill collection limit, project `.skillnote.json`, managed manifests, OpenClaw `max_skills` bounds of 1-100, a 4x over-fetch window before usage/rating sort, top-200 analytics caps, and native progressive disclosure from description to full skill body. Effective precision, recall, and context dilution are not verified from code.

**Authority at consumption.** Local `SKILL.md` files and MCP skill tools carry system-definition authority when the host agent applies them. Ratings, comments, usage counts, and context-bundle metadata carry ranking and review authority. Prompt drafts and usage dashboards advise humans and agents but do not become instructions until published or synced as skills.

**Faithfulness.** The repository includes tests for hooks, imports, OpenClaw usage, MCP behavior, and UI flows, but the code does not prove that agents obey pushed skill instructions or that a particular skill changed downstream behavior. SkillNote records calls and ratings; it does not run WITH/WITHOUT ablations or post-action audits for skill adherence.

**Other consumers.** Human users consume the web editor, version history, import workspace, analytics dashboard, comments, and integration pages. CLI setup and bridge jobs consume backend state to install or reconnect agents. The OpenClaw resolver subagent consumes context bundles; MCP clients consume tool-list changes.

## Curiosity Pass

SkillNote is closer to an instruction supply chain than to a memory database. The interesting memory mechanism is not storage alone; it is the path from registry row to host-native skill surface.

The system is deliberately self-hosted and has no default API authentication, so the real access boundary is network reachability. That is coherent for the local/team deployment story, but it means an exposed instance is a direct write path into future agent instructions ([README.md](https://github.com/luna-prompts/skillnote/blob/7303ba7ab2098f9675e320fd68296458b4703752/README.md)).

The most subtle context-efficiency move is collection scoping, not semantic retrieval. SkillNote avoids the 8,000-character skill-description limit by reducing what is active, then lets the host agent perform ordinary skill selection.

The prompt-watcher is intentionally weaker than "learn a skill from chat." It creates draft evidence or pushes a confirmation workflow; that restraint is a design strength because it keeps accidental user phrasing from becoming team-wide instruction.

The OpenClaw bundle says SkillNote is not the ranker, then sorts by usage and rating before handing candidates to a resolver. That is a useful split: cheap operational priors first, semantic judgment later.

## What to Watch

- Whether the planned Codex/Cursor/OpenHands adapters preserve native skill semantics or collapse SkillNote into a generic remote retrieval layer.
- Whether prompt-derived drafts gain a governed review queue in the registry, with source prompt, acceptance, rejection, and publication lineage.
- Whether ratings/comments start affecting Claude Code collection sync, not only dashboards and OpenClaw bundle ordering.
- Whether API authentication or signed skill bundles become default for shared deployments; without that, network reachability is the instruction-write boundary.
- Whether the system adds a faithfulness check that distinguishes "skill was loaded" from "skill changed the agent's behavior."

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - compares: SkillNote turns usage and prompt traces into ranking, review, and draft-candidate signals rather than autonomous finished skills.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: SkillNote invests heavily in hook and native-skill activation, not just storage.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: SkillNote separates registry rows, synced skill files, manifests, hooks, import lineage, and analytics traces by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: synced `SKILL.md` files, plugin hooks, MCP tool definitions, and sidecar instructions directly shape future agent behavior.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: comments, usage logs, import previews, and draft candidates advise later review before they become active instructions.
