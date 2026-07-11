---
description: "Compound Engineering review: repo-file workflow memory with generated strategy, brainstorm, plan, solution, pulse, session-history, and review artifacts"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-04"
---

# Compound Engineering Plugin

Compound Engineering, by EveryInc, is a TypeScript-distributed agent workflow plugin for Claude Code, Codex, Cursor, Copilot, Droid, Qwen, OpenCode, Pi, Gemini, and Kiro-style hosts. At the reviewed commit it ships a plugin package of skills and specialized agents, cross-harness converters/installers, and project workflows that generate retained files such as strategy anchors, ideation docs, brainstorm requirements, implementation plans, solution learnings, concept vocabularies, pulse reports, review artifacts, and instruction-file discoverability edits.

**Repository:** https://github.com/EveryInc/compound-engineering-plugin

**Reviewed commit:** [63b6b260c345ba70ce9d9a393eeedefb64e4e0a0](https://github.com/EveryInc/compound-engineering-plugin/commit/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0)

**Last checked:** 2026-06-04

## Core Ideas

**The memory model is a workflow-shaped file system, not a memory database.** The top-level README frames the loop as strategy, ideation, brainstorm, plan, work, review, compound, and pulse, and the plugin README exposes those steps as skills backed by specialized agents ([README.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/README.md), [plugins/compound-engineering/README.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/README.md)). Memory accumulates as ordinary project files: `STRATEGY.md`, `docs/ideation/`, `docs/brainstorms/`, `docs/plans/`, `docs/solutions/`, `CONCEPTS.md`, and `docs/pulse-reports/`, plus temporary review artifacts.

**Skills are the primary context routers.** Each workflow decides which retained files to read and when: `ce-strategy` writes a product anchor read by downstream ideation, brainstorming, and planning; `ce-brainstorm` reads strategy and concepts before requirements; `ce-plan` searches upstream requirements and reads strategy/concepts; `ce-work` treats plans as decision artifacts; `lfg` composes plan -> work -> review -> test -> PR into an enforced sequence ([plugins/compound-engineering/skills/ce-strategy/SKILL.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/skills/ce-strategy/SKILL.md), [plugins/compound-engineering/skills/ce-brainstorm/SKILL.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/skills/ce-brainstorm/SKILL.md), [plugins/compound-engineering/skills/ce-plan/SKILL.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/skills/ce-plan/SKILL.md), [plugins/compound-engineering/skills/ce-work/SKILL.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/skills/ce-work/SKILL.md), [plugins/compound-engineering/skills/lfg/SKILL.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/skills/lfg/SKILL.md)).

**Context efficiency comes from staged disclosure and scoped search, not a learned retriever.** The skills repeatedly defer reference files until the phase that needs them, require grep/glob-first scans, cap session-history deep dives, avoid loading whole session files, and isolate subagents so large review/planning tasks do not all share one context ([plugins/compound-engineering/skills/ce-compound/SKILL.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/skills/ce-compound/SKILL.md), [plugins/compound-engineering/skills/ce-sessions/SKILL.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/skills/ce-sessions/SKILL.md), [plugins/compound-engineering/skills/ce-code-review/SKILL.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/skills/ce-code-review/SKILL.md)). There is no vector index or global learned ranker in the plugin; selection is mostly path, phase, keyword, frontmatter, git diff, PR metadata, and agent judgment.

**The strongest long-term learning surface is `ce-compound`.** `ce-compound` documents solved problems into `docs/solutions/`, cross-checks related learnings, optionally incorporates session history, updates or creates `CONCEPTS.md`, and checks whether `AGENTS.md` or `CLAUDE.md` make the knowledge store discoverable to future agents ([plugins/compound-engineering/skills/ce-compound/SKILL.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/skills/ce-compound/SKILL.md)). `ce-compound-refresh` then maintains those learning docs by keeping, updating, consolidating, replacing, or deleting stale artifacts ([plugins/compound-engineering/skills/ce-compound-refresh/SKILL.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/skills/ce-compound-refresh/SKILL.md)).

**Review is both quality control and memory generation.** `ce-code-review` spawns reviewer personas, merges structured findings, writes run artifacts under `/tmp/compound-engineering/ce-code-review/<run-id>/`, can apply local fixes in default mode, and surfaces prior `docs/solutions/` as known patterns ([plugins/compound-engineering/skills/ce-code-review/SKILL.md](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/skills/ce-code-review/SKILL.md)). The review output is not just chat; it becomes JSON/report metadata that downstream skills such as `lfg` can consume.

**Adoption is cross-harness and mostly file-native.** Native plugin manifests expose the same skill corpus, while the Bun CLI converts and installs agents, skills, prompts, MCP config, hooks, and managed install manifests into Codex/OpenCode/Pi/Gemini/Kiro target homes with cleanup and path-safety guards ([plugins/compound-engineering/.codex-plugin/plugin.json](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/plugins/compound-engineering/.codex-plugin/plugin.json), [src/commands/install.ts](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/src/commands/install.ts), [src/converters/claude-to-codex.ts](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/src/converters/claude-to-codex.ts), [src/targets/codex.ts](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/src/targets/codex.ts), [src/targets/managed-artifacts.ts](https://github.com/EveryInc/compound-engineering-plugin/blob/63b6b260c345ba70ce9d9a393eeedefb64e4e0a0/src/targets/managed-artifacts.ts)).

## Artifact analysis

- **Storage substrate:** `repo` — The primary behavior-shaping retained state is file-backed: plugin skills/agents/manifests in the distributed repository and generated project files in the consuming repository. Secondary substrates include host config directories such as `.codex/`, machine-local `.compound-engineering/config.local.yaml`, OS temp run artifacts, git history, and external session-history files read by `ce-sessions`.
- **Representational form:** `prose` `symbolic` — Skill bodies, agent personas, strategy docs, brainstorms, plans, solutions, concept entries, and pulse reports are prose; frontmatter, plugin manifests, config YAML, schemas, run JSON, task IDs, requirement IDs, file paths, git refs, and install manifests are symbolic. I found no native parametric memory store; any model judgment happens at execution time rather than being retained as embeddings or weights.
- **Lineage:** `authored` `imported` `trace-extracted` — Plugin instructions and agents are authored; installer/converter outputs and generated docs import plugin templates into target environments; solution docs, pulse reports, review reports, and session-history summaries can be extracted from conversation context, git/PR traces, analytics/tracing data, and prior agent session logs.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `enforcement` `learning` — Strategy, plans, solutions, concepts, and pulse reports advise as knowledge; installed skills, agents, generated instruction-file mentions, and prompt/skill conversions instruct future agents; manifests, skill triggers, task phases, and dispatch rules route work; schemas, frontmatter validation, path-safety checks, health checks, review validators, and protected-artifact rules validate; `lfg`, `ce-code-review`, and setup/update flows enforce workflow order or apply/commit local fixes under specified conditions; `ce-compound` and refresh flows convert traces into reusable learning artifacts.

**Plugin corpus.** Storage substrate: repository files under `plugins/compound-engineering/` plus native plugin manifests. Representational form: prose skill/agent instructions and symbolic metadata. Lineage: authored and release-managed. Behavioral authority: instruction and routing for agent workflows, plus validation where skill contracts prescribe checks.

**Project workflow artifacts.** Storage substrate: consuming project repository files including `STRATEGY.md`, `docs/ideation/`, `docs/brainstorms/`, `docs/plans/`, `docs/solutions/`, `CONCEPTS.md`, and `docs/pulse-reports/`. Representational form: prose with symbolic frontmatter, IDs, categories, and links. Lineage: authored collaboratively by user and agent, with trace-extracted material folded in when workflows read conversation, session, git, analytics, or issue data. Behavioral authority: knowledge for future agents, and instruction when a plan or strategy is explicitly loaded by a workflow.

**Session-history and code-review artifacts.** Storage substrate: scratch directories and `/tmp/compound-engineering/ce-code-review/<run-id>/` rather than canonical project memory. Representational form: extracted skeleton text, JSON findings, metadata, and reports. Lineage: trace-extracted from Claude/Codex/Cursor sessions, git diffs, PR metadata, reviewer outputs, and validator passes. Behavioral authority: knowledge and validation for the current or downstream workflow; durable authority appears only when the result is written into project files, PR bodies, commits, or residual-finding records.

**Installer and conversion artifacts.** Storage substrate: target host homes and project-local config directories. Representational form: symbolic TOML/JSON/YAML manifests and generated skill/agent files with prose bodies. Lineage: imported/compiled from Claude-plugin source. Behavioral authority: routing and instruction, because these files decide which skills, agents, prompts, MCP servers, and hooks are available to the host agent.

Promotion path: Compound Engineering has an explicit ladder from weak evidence to stronger authority. Conversation/session/diff traces first become draft findings or generated docs, then solution docs or concept entries, then instruction-file discoverability, and in some workflows review findings can become applied code fixes or PR residual records. The ladder is operationally strong, but the semantic truth of learned docs depends on the agent workflow and human review path, not on a separate standing verifier.

## Comparison with Our System

| Dimension | Compound Engineering | Commonplace |
|---|---|---|
| Primary purpose | Agent workflow plugin for engineering execution and project learning | Git-native methodology KB for agent-operated knowledge bases |
| Canonical artifact | Skill/agent instruction files plus generated project docs | Typed Markdown artifacts with collection/type contracts |
| Source of truth | Consuming repo files and host plugin installs | Repository files, generated indexes, reports, and validation outputs |
| Write path | Skills generate strategy, requirements, plans, learnings, concepts, pulse reports, review artifacts, and instruction-file edits | Authored edits, snapshots, review workflows, validation, index refresh |
| Read-back | Pull skill invocations plus workflow-loaded project docs and instruction-file discoverability | Mostly explicit pull through search, indexes, links, skills, and loaded instructions |
| Governance | Skill-local schemas, health checks, review validators, path-safety, git diffs, host installs | Collection contracts, schemas, git diffs, semantic gates, citation and lineage discipline |

Compound Engineering is closer to a portable operating procedure layer than to a knowledge base framework. It teaches agents how to turn work into retained project artifacts, then makes those artifacts visible to later workflows. Commonplace is more explicit about artifact type, link semantics, validation, and durable review state; Compound Engineering is more explicit about end-to-end engineering workflow and cross-harness adoption.

The biggest tradeoff is authority speed. Compound Engineering can quickly move a solved problem into `docs/solutions/`, add discoverability lines to `AGENTS.md`, and let later agents search or load that learning. Commonplace makes promotion slower and more typed, which is better when the artifact is methodology truth rather than project-specific operational memory.

### Borrowable Ideas

**Run a discoverability check after every learning write.** Ready now as a Commonplace workflow principle. A knowledge artifact that is not surfaced in agent instructions, indexes, or routing contracts has weak practical memory value.

**Use skill-local references for progressive disclosure.** Ready now. Compound Engineering keeps many detailed contracts in `references/` and loads them only at the phase that needs them; Commonplace skills can use the same pattern to preserve execution context.

**Make review outputs machine-readable even when the human view is prose.** Ready now for review infrastructure. `ce-code-review`'s JSON/run-artifact shape is a good analogue for Commonplace semantic gates that need both a report and downstream automation.

**Treat generated prompt/instruction surfaces as compiled views.** Needs a concrete emitting workflow. If Commonplace produces host-specific instruction files, they should carry source lineage and regeneration rules rather than drifting independently.

**Use session-history extraction as supplementary evidence, not primary truth.** Ready as a constraint. Compound Engineering's `ce-compound` labels session and auto-memory sourced content, which is a useful provenance discipline for trace-derived notes.

## Write side

**Write agency:** `manual` `automatic` — Manual writes come from users invoking skills, answering interviews, approving edits, and directly editing retained project files. Automatic writes include generated strategy/ideation/brainstorm/plan/solution/pulse/review files, session-history scratch extraction, solution-doc frontmatter validation, `CONCEPTS.md` updates, instruction-file discoverability edits, installer outputs, managed manifest writes, cleanup of obsolete managed artifacts, and review-fix commits in default review mode.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `promote` — `ce-compound` consolidates solved-problem context into compact solution docs, detects high overlap so an existing doc can be updated instead of duplicating it, and synthesizes new docs from conversation/code/session evidence. `ce-compound-refresh` consolidates overlapping docs, replaces or deletes stale docs, and marks ambiguous cases stale in headless mode. Discoverability edits and workflow loading promote selected artifacts into future agent attention.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` `event-streams` — The system consumes conversation history and auto-memory blocks during compounding, Claude/Codex/Cursor session logs through `ce-sessions`, git diffs and PR metadata during review, issue/Slack/repo research traces in research workflows, and analytics/tracing/payment/database event streams in product pulse.

**Learning scope:** `per-project` `cross-task` — The durable docs live in a consuming project and are meant to improve later work in that project; cross-task reuse happens through `docs/solutions/`, `CONCEPTS.md`, strategy, plans, and instruction-file discoverability.

**Learning timing:** `online` `staged` — Skill runs write artifacts during the current task, but the extraction and maintenance loops are staged workflows: compounding after a solved problem, refresh after drift evidence, product pulse on a time window, and code review after a diff.

**Distilled form:** `prose` `symbolic` — Traces become prose solution docs, strategy sections, pulse reports, review explanations, and concept definitions, with symbolic frontmatter, categories, IDs, JSON findings, file paths, git refs, and validation metadata.

**Extraction.** The clearest trace-derived loop is `ce-compound` plus `ce-sessions`: session files are discovered, metadata-filtered, skeletonized into scratch files, synthesized by a session historian, and folded into the final solution document only when relevant. The workflow treats session history and auto memory as supplementary evidence, while current conversation and verified fixes take priority.

**Scope and timing.** The raw trace unit is a prior agent session, current conversation, git diff, PR discussion, or product telemetry window. The durable unit is a project file such as a solution learning, concept entry, strategy update, plan, pulse report, PR residual section, or instruction-file discoverability line.

**Survey fit.** Compound Engineering supports the survey split between raw trace artifacts and distilled behavior-shaping artifacts. Raw sessions and review outputs are not the main memory; the behavior-shaping outputs are readable files and installed instructions that later workflows can load.

## Read-back

**Read-back:** `both` — Most memory use is pull: a user or workflow invokes a skill, and the skill searches or reads strategy, concepts, brainstorms, plans, solutions, prior sessions, diffs, or pulse reports. It is also push when workflow rules automatically load retained project files once a skill is invoked, and when instruction-file discoverability lines or installed skill/agent definitions enter a host agent's starting context.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` — Installed skills and instruction-file mentions are coarse surfaces; workflow paths such as `STRATEGY.md`, `docs/plans/`, `docs/solutions/`, branch names, changed files, frontmatter fields, plan IDs, PR numbers, and config keys are identifier signals; related-doc search, keyword-filtered sessions, issue/theme analysis, git-history scans, and reviewer/agent judgment use lexical or semantic inference at execution time.

**Faithfulness tested:** `no` — The repository has tests for converters, path safety, manifest handling, plugin artifacts, review contracts, and session scripts, but I did not find a behavioral ablation showing that loaded strategy, solution docs, instruction-file mentions, or session-history summaries reliably change future agent behavior correctly.

**Direction edge cases.** A user typing `/ce-plan docs/brainstorms/foo.md` is pull from the orchestrating agent's perspective. The plan skill then pushing `STRATEGY.md`, `CONCEPTS.md`, and origin requirements into subagent prompts is push for the receiving subagents. A line in `AGENTS.md` that tells agents `docs/solutions/` exists is pushed instruction or awareness; it is not the same as pushing every solution doc.

**Targeting and signal.** The strongest targeting is symbolic: known paths, categories, frontmatter fields, changed files, plan origins, branch names, and PR metadata. Lexical targeting appears in grep-first related-doc searches and session keyword filtering. No embedding recall path is implemented in the reviewed code.

**Injection point.** Read-back happens before the relevant model call or subagent dispatch. For example, a skill reads a plan before executing work, reads strategy before brainstorming, or assembles code-review context before reviewer agents run. Post-action writes such as generated solution docs, review artifacts, or pulse reports are write-side maintenance for later reads.

**Selection, scope, and complexity.** Selection is constrained by workflow phase, explicit file paths, directory conventions, frontmatter fields, git diff scope, PR metadata, session scan windows, deep-dive caps, and per-skill reference loading. Complexity is still high because a single workflow can combine project instructions, strategy, concepts, requirements, plans, prior solutions, current diffs, subagent outputs, and session history.

**Authority at consumption.** A retrieved solution doc advises as knowledge unless a skill or instruction file tells an agent to use it as a workflow input. A plan has stronger authority during `ce-work`; plugin skills and agents have instruction authority; validators and review gates carry validation or enforcement authority. Effective authority depends on host behavior and model compliance, not just file presence.

**Other consumers.** Human maintainers consume the same artifacts through Markdown files, terminal reports, PR bodies, local config examples, plugin docs, and git history. The design is intentionally inspectable by non-agent readers.

## Curiosity Pass

**The name says plugin, but the mechanism is a knowledge-operating loop.** The important memory behavior is not in the TypeScript package manager wrapper; it is in the skill contracts that create and route project artifacts.

**There is no central "memory" API.** The system works because every workflow knows its own retained surfaces. That makes it easy to inspect, but hard to ask one global question like "what memory will this agent receive?"

**The strongest push surface is discoverability, not automatic recall.** Compound Engineering does not automatically inject the top three relevant solution docs into every task. It makes the knowledge store visible, then relies on workflow-specific search and loading.

**Temporary review artifacts are useful but not canonical.** `/tmp/compound-engineering/ce-code-review/` is a strong automation handoff surface, but it is outside the project repo. Long-term authority comes only when findings become commits, PR text, residual files, or solution docs.

**Trace-derived outputs are readable, which helps governance.** The system does not hide learning in embeddings; the cost is that relevance and truth maintenance are mostly procedural rather than computed.

## What to Watch

- Whether Codex native plugins gain custom-agent support; the current README says a separate Bun install is needed for Codex agents, and that gap determines how much conversion machinery remains necessary.
- Whether `ce-sessions` outputs start feeding more workflows automatically; that would increase trace-derived read-back beyond optional compounding support.
- Whether `docs/solutions/` gains stronger schema/index tooling; that would move it closer to Commonplace-style typed knowledge.
- Whether product pulse reports become inputs to strategy or brainstorm by default; that would make operational telemetry a stronger memory source.
- Whether review artifacts outside `/tmp` become first-class retained project files; that would change their authority from ephemeral QA handoff to durable project memory.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Compound Engineering stores many project artifacts, but workflow loading and instruction-file discoverability decide when they enter context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: skills, agents, plans, solution docs, concepts, review JSON, installer manifests, and instruction-file edits carry different lineage and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: strategy, plans, solution docs, concepts, pulse reports, session summaries, and review reports mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: skills, agents, plugin manifests, workflow gates, validators, and instruction-file edits shape later behavior with stronger force.
- [Keep Lineage And Compiled Views From Drifting](../../notes/agent-memory-requirements/keep-compiled-views-aligned.md) - warns: host-specific installed artifacts and instruction-file discoverability lines are compiled views over the plugin/project memory source.
- [Use Trace-Derived Extraction As Meta-Learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Compound Engineering turns session, conversation, diff, review, and telemetry traces into reusable project learnings.
