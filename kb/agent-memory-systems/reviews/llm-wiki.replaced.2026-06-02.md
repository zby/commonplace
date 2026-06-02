---
description: "LLM Wiki review: promptware knowledge-base protocol with topic-isolated markdown wikis, raw-to-compiled workflows, multi-runtime plugins, and local lint validation"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# LLM Wiki

> Replaced 2026-06-02. See [llm-wiki](./llm-wiki.md) for the current review.

LLM Wiki is nvk's agent-operated wiki protocol for building topic-isolated, markdown knowledge bases. It ships primarily as a Claude Code plugin, mirrors into Codex and OpenCode/Pi packaging, and also exposes a portable `AGENTS.md` idea file for any file-editing agent. The system is mostly promptware: commands, skills, references, and conventions tell the agent how to ingest raw sources, compile wiki articles, run research/thesis/audit workflows, maintain indexes, and optionally validate structure with a local Python helper.

**Repository:** https://github.com/nvk/llm-wiki

**Reviewed commit:** [505b56c50ff75bbf61eedd236b44d192c0e0674c](https://github.com/nvk/llm-wiki/commit/505b56c50ff75bbf61eedd236b44d192c0e0674c)

**Last checked:** 2026-05-16

## Core Ideas

**The behavior layer is a protocol, not an app server.** `claude-plugin/skills/wiki-manager/SKILL.md` is the main behavior contract: it resolves a wiki hub, routes ambient/wiki commands, defines principles, and points workflows to reference files for ingestion, compilation, linting, audit, archive, inventory, datasets, and project handling ([SKILL.md](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/claude-plugin/skills/wiki-manager/SKILL.md)). Claude command files add concrete entry points such as research, ingest, compile, query, audit, librarian, lessons learned, assess, and output ([commands](https://github.com/nvk/llm-wiki/tree/505b56c50ff75bbf61eedd236b44d192c0e0674c/claude-plugin/commands)). These prompt artifacts are system-definition artifacts because they instruct and route the agent runtime.

**The storage substrate is ordinary markdown with topic isolation.** The hub contains only registry/navigation state, while each topic wiki owns `raw/`, `wiki/`, `inventory/`, `datasets/`, `output/`, indexes, config, and logs ([wiki-structure.md](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/claude-plugin/skills/wiki-manager/references/wiki-structure.md)). This keeps unrelated subjects from sharing retrieval context. Raw sources are immutable knowledge artifacts; compiled wiki articles are synthesized knowledge artifacts; indexes are derived navigation surfaces; config, command prompts, lint rules, and plugin manifests carry stronger system-definition authority.

**Raw-to-compiled transformation is the central memory operation.** The compilation protocol reads `raw/_index.md`, maps new sources to existing articles, classifies new articles as concepts/topics/references, writes synthesized pages with source links and confidence, then updates category, wiki, and master indexes ([compilation.md](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/claude-plugin/skills/wiki-manager/references/compilation.md)). Lineage is frontmatter-and-link based: articles list source paths, sources retain ingestion metadata, and indexes cache summaries rather than becoming canonical. The representational form is prose plus YAML frontmatter and markdown links.

**Research and thesis workflows use agent orchestration as the compiler front end.** `/wiki:research` can create a topic, decompose questions, launch parallel research agents, ingest sources, compile articles, and keep multi-round session state in `.research-session.json`, `.session-events.jsonl`, and `.session-checkpoint.json` ([research.md](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/claude-plugin/commands/research.md)). Thesis mode constrains search around a claim, splits evidence-for/evidence-against work, and renders a verdict; the old `/wiki:thesis` command is now a shim into `/wiki:research --mode thesis` ([thesis.md](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/claude-plugin/commands/thesis.md)). These workflows create knowledge artifacts, not executable validators, unless their outputs are later promoted into instructions or code.

**Indexes are both navigation convention and validation target.** The protocol says agents should read indexes first, stale-check them, and rebuild them as derived caches. The local `scripts/llm-wiki` helper implements deterministic lint rules for structure, frontmatter, canonical placement, unknown files, index consistency, link integrity, source provenance, inventory, datasets, archives, and fixable repairs ([scripts/llm-wiki](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/scripts/llm-wiki), [linting.md](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/claude-plugin/skills/wiki-manager/references/linting.md)). Tests exercise both shell-level fixture assertions and the local lint helper ([test-structure.sh](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/tests/test-structure.sh), [test-local-cli-lint.sh](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/tests/test-local-cli-lint.sh)).

**Multi-runtime packaging keeps one source of truth with generated mirrors.** The README and development guide identify `claude-plugin/skills/wiki-manager/` as the behavioral source of truth, with generated Codex packaging under `plugins/llm-wiki/`, OpenCode/Pi packaging under `plugins/llm-wiki-opencode/`, and portable `AGENTS.md` for non-plugin agents ([README.md](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/README.md), [CLAUDE.md](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/CLAUDE.md)). Sync scripts regenerate the mirrors and tests fail if generated plugin copies drift ([sync-codex-plugin.sh](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/scripts/sync-codex-plugin.sh), [sync-opencode-plugin.sh](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/scripts/sync-opencode-plugin.sh)).

## Comparison with Our System

| Dimension | LLM Wiki | Commonplace |
|---|---|---|
| Primary aim | Help an agent build topic wikis from sources and research sessions | Maintain methodology for agent-operated KBs |
| Storage substrate | Markdown topic wikis under a hub or project-local `.wiki/` | Git-tracked typed Markdown collections |
| Type system | Frontmatter conventions for raw/wiki/inventory/datasets/output | Explicit type specs, schemas, collection contracts, validators |
| Runtime surface | Claude commands, skill references, Codex/OpenCode mirrors, portable `AGENTS.md` | Skills, `AGENTS.md`, `commonplace-*` commands, review/fix workflows |
| Derived views | `_index.md` files, reports, outputs, session checkpoints | Directory indexes, review reports, validation outputs, connect reports |
| Validation | Local deterministic `llm-wiki lint`, shell fixture tests, Promptfoo routing evals | `commonplace-validate`, semantic review bundles, typed schemas |
| Authority model | Mostly prompt instruction plus local structural lint | Typed artifact contracts plus deterministic validation and review gates |

LLM Wiki and commonplace share the same broad intuition: durable agent memory should be made of inspectable files, source-backed synthesis, indexes, and operational workflows rather than hidden chat state. LLM Wiki is more adoption-oriented: it fits Claude Code, Codex, OpenCode, Pi, Obsidian, GitHub markdown, and a copyable `AGENTS.md` file with minimal runtime dependencies.

Commonplace is stricter about artifact contracts. LLM Wiki has good file placement, frontmatter, and lint rules, but the semantics of a compiled article, thesis verdict, audit report, or lesson remain mostly prompt-defined. Commonplace makes collection register, type specs, link vocabulary, validation, review lifecycle, and artifact authority more explicit.

The most important contrast is authority. In LLM Wiki, the agent reads prompt instructions and writes wiki files; deterministic code checks whether the resulting wiki is structurally coherent. In commonplace, instructions, type specs, validators, generated indexes, and semantic review reports are themselves part of a more formal system-definition layer.

**Read-back:** both — agents query wiki indexes and articles, while plugin skills and portable instructions can load behavior rules without a wiki query.

## Borrowable Ideas

**One portable protocol file as an adoption bridge.** LLM Wiki's `AGENTS.md` compresses the whole system into a single file for agents that do not support plugins ([AGENTS.md](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/AGENTS.md)). Commonplace already has repo instructions, but a deliberately portable "minimum viable KB protocol" could lower adoption cost for projects that cannot install the full command package.

**Generated runtime mirrors with drift tests.** The Claude-first source plus Codex/OpenCode generated mirrors is a clean packaging pattern. Commonplace could use the same strategy if it needs thinner runtime-specific skill bundles while keeping the behavior contract centralized.

**Topic isolation as a default user-facing shape.** LLM Wiki's hub/topic split is useful for consumer projects where users have multiple unrelated research areas. Commonplace's own methodology KB should stay integrated, but consuming projects could offer topic sub-wikis when cross-topic noise would hurt retrieval.

**Obsidian-compatible dual-linking.** The dual wikilink plus markdown-link convention is a practical bridge for human graph viewing and agent path following. Commonplace has a more controlled link vocabulary, so this is borrowable only where Obsidian compatibility is a first-class requirement.

**Local lint as migration.** The linting reference treats schema evolution as idempotent structural repair rather than one-off migrations. That principle fits commonplace for some mechanical path/frontmatter repairs, while semantic migrations should still go through review.

## Trace-derived learning placement

LLM Wiki qualifies for trace-derived status, but only through a narrow workflow. The ordinary ingest/compile path is source-derived knowledge synthesis, not trace-derived learning. The qualifying loop is `/wiki:ll`: it scans the current session for error-fix patterns, user corrections, discoveries, configuration changes, and gotchas, then writes a durable `raw/notes/YYYY-MM-DD-ll-<slug>.md` lesson artifact and may append rules to relevant wiki articles or suggest AGENTS/CLAUDE rule additions ([ll.md](https://github.com/nvk/llm-wiki/blob/505b56c50ff75bbf61eedd236b44d192c0e0674c/claude-plugin/commands/ll.md)).

**Trace source.** The source trace is the agent's current session context: failures, fixes, corrections, touched files, and discovered patterns. Multi-round research also records `.session-events.jsonl` and `.session-checkpoint.json`, but those are mostly provenance/resume traces unless a later workflow converts them into lessons.

**Extraction.** Extraction is prompt-governed. The command tells the agent to identify lesson-worthy events, deduplicate, generalize each into a rule, write a structured raw note, optionally update matching articles, and optionally suggest instruction-file rules. There is no separate executable judge for lesson quality.

**Storage substrate.** Raw lessons persist as markdown under the target wiki's `raw/notes/`. Article updates persist under `wiki/`. Suggested AGENTS/CLAUDE rules are advisory unless a human or later agent applies them.

**Representational form.** Lessons are prose with YAML frontmatter. Article updates are prose knowledge artifacts. Proposed rule additions are prose system-definition candidates; they become system-definition artifacts only after promotion into an instruction file.

**Lineage.** Lineage is weak-to-moderate. The lesson note records that it came from a session and includes concrete symptoms/fixes, but the reviewed code does not enforce transcript IDs, source excerpts, hashes, or outcome metrics. Research session JSONL/checkpoint files provide better event provenance for research workflows, but they are not automatically tied to `/wiki:ll` lesson derivation.

**Behavioral authority.** Raw lessons are knowledge artifacts when later compiled or queried. Wiki article updates advise future answers. Suggested AGENTS/CLAUDE rule additions have no force until promoted. Once promoted into `AGENTS.md`, `CLAUDE.md`, command prompts, lint rules, or code, they become system-definition artifacts.

**Scope and timing.** The loop is per wiki or local project and runs after a session, not online during every action. It is cross-session memory, not cross-project model learning.

**Survey placement.** LLM Wiki strengthens the trace-derived survey's distinction between trace capture and artifact promotion: it has a promptware session-to-lesson loop, but its durable behavior change depends on later compilation or explicit instruction promotion.

## Curiosity Pass

LLM Wiki looks simple because it is file-first, but much of its complexity lives in prompt contracts. That makes it easy to inspect and install, but harder to guarantee across agent runtimes than an API-backed system.

The local lint helper is more real than the "zero dependencies" framing might suggest. It gives the protocol an executable spine for structure, placement, indexes, and link checks, while leaving synthesis, research quality, and audit truth-seeking to the agent.

The raw/compiled split is strong; the compiled article contract is less strong. Confidence, sources, volatility, and dual-links help, but there is no type-specific semantic validator for whether a thesis verdict or article synthesis faithfully follows its sources.

The plugin mirrors are generated, which is good, but runtime behavior can still diverge because Claude, Codex, OpenCode, Pi, and generic agents expose different context windows, tool permissions, command affordances, and plugin activation rules.

Trace-derived learning is present but not central. The repository is primarily a source-ingestion and compilation system. The lessons-learned command is a memory loop, but its oracle is the current agent's judgment unless paired with human review or deterministic checks.

## What to Watch

- Whether `/wiki:ll` gains stronger provenance: transcript pointers, source excerpts, confidence, and promotion status.
- Whether compiled articles gain executable semantic checks beyond structural lint and Promptfoo routing evals.
- Whether audit reports and thesis verdicts become typed artifacts with enforceable evidence tables.
- Whether generated Codex/OpenCode mirrors remain behaviorally equivalent as runtimes evolve.
- Whether topic wikis accumulate enough cross-topic overlap to need explicit federation rules beyond sibling index peeks.

## Bottom Line

LLM Wiki is best understood as a portable promptware/protocol system for agent-maintained markdown wikis. It separates raw sources, compiled wiki artifacts, derived indexes, command prompts, local lint code, and runtime packaging reasonably well. Its durable memory is mostly knowledge artifacts; its system-definition artifacts are the command prompts, skill references, local lint rules, sync scripts, and plugin manifests that shape agent behavior.

Relevant Notes:

- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw sources, compiled articles, lessons, reports, and query answers when consumed as evidence or context
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: command prompts, skill files, lint rules, plugin manifests, and promoted AGENTS/CLAUDE rules
- [behavioral authority](../../notes/definitions/behavioral-authority.md) - frames: LLM Wiki's distinction between advisory wiki content and instruction/enforcement surfaces
- [lineage](../../notes/definitions/lineage.md) - explains: source references, session checkpoints, and lint-regenerated indexes as derivation support
- [register](../../notes/definitions/register.md) - compares-with: LLM Wiki's topic articles are mostly descriptive knowledge artifacts, while command files are prescriptive system-definition artifacts
