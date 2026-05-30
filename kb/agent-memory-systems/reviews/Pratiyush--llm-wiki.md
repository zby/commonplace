---
description: "Trace-derived local wiki builder that converts coding-agent session logs into raw markdown, synthesized wiki pages, static exports, MCP tools, and agent workflows"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# Pratiyush/llm-wiki

Pratiyush's `llm-wiki` is a Python package and agent prompt system for turning local coding-agent session histories into a Karpathy-style three-layer wiki: immutable raw transcript markdown, LLM- or agent-maintained wiki pages, and generated static/AI-consumable exports. Unlike MehmetGoekce's promptware-only `llm-wiki`, this repository contains a substantial implemented CLI, session-store adapters, renderer, synthesis pipeline, lint/governance surfaces, MCP server, and Claude/Codex-facing workflow files.

**Repository:** https://github.com/Pratiyush/llm-wiki

**Reviewed commit:** [834998747ec5368f4a4f3ffa450995048ac7c4af](https://github.com/Pratiyush/llm-wiki/commit/834998747ec5368f4a4f3ffa450995048ac7c4af)

**Last checked:** 2026-05-16

## Core Ideas

**The implemented storage model is layered files, not a memory service.** The architecture document names `raw/`, `wiki/`, and `site/` as the conceptual layers, while the code implements them as repo-local directories plus state files such as `.llmwiki-state.json`, `.llmwiki-synth-state.json`, and `.llmwiki-queue.json` ([docs/architecture.md](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/docs/architecture.md), [llmwiki/convert.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/convert.py), [llmwiki/synth/pipeline.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/synth/pipeline.py), [llmwiki/ingest_queue.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/ingest_queue.py)). The storage substrate is mostly markdown and JSON files; optional graph and export layers are derived files, not authoritative stores.

**Raw transcript conversion is real trace ingestion.** `llmwiki sync` discovers local session JSONL files through adapters for Claude Code, Codex CLI, Cursor, Gemini, Copilot, OpenCode, ChatGPT, and Obsidian-related inputs, normalizes records into a shared shape, redacts secrets, skips live sessions by default, enforces raw-file immutability unless `--force` is passed, and writes frontmatter-rich transcript markdown under `raw/sessions/` ([llmwiki/adapters/base.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/adapters/base.py), [llmwiki/adapters/claude_code.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/adapters/claude_code.py), [llmwiki/adapters/codex_cli.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/adapters/codex_cli.py), [llmwiki/convert.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/convert.py)). The raw transcript is a knowledge artifact: source evidence for later summaries, queries, audits, visualizations, and exports.

**Synthesis is split between code backends and agent prompts.** `llmwiki synthesize` scans raw markdown, calls a configured synthesizer backend, writes `wiki/sources/<project>/<date>-<slug>.md`, preserves curated tags on re-synthesis, updates synthesis state, appends to `wiki/log.md`, and rebuilds the `## Sources` section of `wiki/index.md` ([llmwiki/synth/pipeline.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/synth/pipeline.py)). The backend options are revealing: dummy synthesis is deterministic test output; Ollama is a local LLM backend; agent-delegate writes pending prompts under `.llmwiki-pending-prompts/` so a running coding agent can complete the page without an API call ([llmwiki/synth/base.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/synth/base.py), [llmwiki/synth/agent_delegate.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/synth/agent_delegate.py), [llmwiki/synth/prompts/source_page.md](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/synth/prompts/source_page.md)).

**Agent instructions carry much of the wiki-maintenance authority.** `CLAUDE.md`, `AGENTS.md`, slash commands, and skills define how an agent should ingest sources, query the wiki, lint pages, extract entities/concepts, record contradictions, update indexes, and preserve raw immutability ([CLAUDE.md](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/CLAUDE.md), [AGENTS.md](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/AGENTS.md), [.claude/commands/wiki-ingest.md](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/.claude/commands/wiki-ingest.md), [.claude/skills/self-learn/SKILL.md](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/.claude/skills/self-learn/SKILL.md)). These files are system-definition artifacts: their representational form is prose instruction, and their behavioral authority is instruction/routing/governance when consumed by Claude Code, Codex, or another agent.

**The build/export layer turns memory into many derived consumption surfaces.** `llmwiki build` renders raw and wiki pages into a static site, writes per-session HTML plus `.txt` and `.json` siblings, emits `search-index.json`, copies raw markdown into `site/sources/`, creates AI-consumable exports, writes a manifest, and copies an interactive graph viewer into the site ([llmwiki/build.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/build.py), [llmwiki/exporters.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/exporters.py), [llmwiki/graph.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/graph.py), [llmwiki/manifest.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/manifest.py)). These generated exports have knowledge-artifact authority when used as evidence or context by humans and agents, but their lineage should be treated as derived: raw/session and wiki files are the sources of truth.

**Governance is partly deterministic and partly aspirational.** The code implements confidence scoring, a lifecycle state machine, candidate promotion/merge/discard/archive operations, lint rule registration, structural linting, optional LLM lint hooks, freshness checks, tags, backlinks, and scheduled build/lint policy ([llmwiki/confidence.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/confidence.py), [llmwiki/lifecycle.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/lifecycle.py), [llmwiki/candidates.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/candidates.py), [llmwiki/lint/__init__.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/lint/__init__.py), [llmwiki/config_schedule.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/config_schedule.py)). The README advertises `MEMORY.md` Auto Dream consolidation, and `cmd_init` seeds `wiki/MEMORY.md`, `SOUL.md`, `CRITICAL_FACTS.md`, `hints.md`, and hot-cache files, but the inspected CLI parser has no `dream` or memory-consolidation command path; at this commit, that advertised consolidation should be treated as planned/prompted surface rather than implemented code ([README.md](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/README.md), [llmwiki/cli.py](https://github.com/Pratiyush/llm-wiki/blob/834998747ec5368f4a4f3ffa450995048ac7c4af/llmwiki/cli.py)).

## Comparison with Our System

| Dimension | Pratiyush/llm-wiki | Commonplace |
|---|---|---|
| Primary purpose | Personal/team coding-agent history wiki and static site | Methodology KB for agent-operated knowledge systems |
| Storage substrate | Local markdown/JSON directories: `raw/`, `wiki/`, `site/`, graph/export/state files | Git-tracked typed markdown collections, source snapshots, generated indexes, review artifacts |
| Representational form | Mixed: transcript prose, markdown frontmatter, JSON exports, prompt instructions, lint/lifecycle code | Prose plus structured frontmatter, path-valued type specs, authored links, CLI validators/review gates |
| Lineage | Raw session markdown is source of truth; synthesized wiki pages and exports are derived; state files track mtimes, not source-span provenance | Source snapshots, commit-pinned citations, replacement archives, validation, semantic review, explicit status metadata |
| Activation | Static search, MCP query/search/read tools, graph/query CLI, agent commands/skills, generated AI exports | `rg`, indexes, links, skills, type contracts, instructions, validation/review workflows |
| Behavioral authority | Raw pages advise; wiki pages explain; prompts/skills instruct; lint/lifecycle/candidates validate and govern; MCP/search rank and expose | Artifact types explicitly distinguish knowledge artifacts from system-definition artifacts and their consumers |

The strongest alignment is file-first context engineering. Both systems keep retained artifacts inspectable, editable, greppable, and regenerable. `llm-wiki` is more productized around installation, static browsing, adapters, search UI, and MCP consumption. Commonplace is stronger on type contracts, collection-local conventions, link semantics, and review lineage.

The main difference is that `llm-wiki` starts from traces. Its raw layer treats agent session history as the privileged evidence source, then builds derived knowledge and UI surfaces around it. Commonplace can review trace-derived systems and store source snapshots, but its primary library artifacts are intentionally authored claims, definitions, ADRs, instructions, and reviews rather than automatic transcript compilations.

The artifact-authority split is less explicit in `llm-wiki` than in commonplace. Raw transcript files and generated source pages are mostly knowledge artifacts when consumed as evidence, reference, or context. `CLAUDE.md`, `AGENTS.md`, slash commands, skills, lint rules, lifecycle rules, candidate commands, and schedule/config helpers are system-definition artifacts because they instruct, validate, route, or govern agent behavior. Static HTML, `.txt`, `.json`, `llms.txt`, `graph.jsonld`, RSS, sitemap, manifest, and MCP query responses are derived consumer surfaces; their authority depends on the underlying raw/wiki files and the build/export pipeline.

Lineage is the place where commonplace's stricter habits matter. `llm-wiki` preserves raw transcripts and frontmatter, uses state files to avoid repeated conversion/synthesis, and makes generated site artifacts disposable. But synthesized wiki claims do not carry source-span citations, review decisions, invalidation rules, or stable pointers from each distilled claim back to transcript turns. A later agent can inspect the raw session, but it may need to redo the evidence audit.

## Borrowable Ideas

**Adapter-first trace intake.** Ready to borrow for workshop layers. The adapter pattern cleanly separates session-store discovery from shared parsing, redaction, rendering, and state tracking.

**Raw immutable transcripts plus derived wiki pages.** Ready as a design pattern. Keeping traces immutable while letting synthesized pages evolve is a useful lineage boundary, provided the distilled pages preserve enough source pointers.

**Agent-delegate synthesis.** Worth borrowing selectively. Writing pending prompts to disk and letting the active coding agent complete them avoids extra API surfaces while keeping the pipeline inspectable.

**AI-consumable siblings for every rendered page.** Ready for consuming projects. `.txt`, `.json`, `llms.txt`, `llms-full.txt`, and `graph.jsonld` are practical compiled views for downstream agents.

**Do not borrow advertised memory consolidation without implementation.** The `MEMORY.md`/Auto Dream idea is relevant, but commonplace should require a concrete consolidation command, trigger policy, review record, and retirement path before treating it as an implemented memory mechanism.

## Trace-derived learning placement

**Trace source.** The trace source is local coding-agent history: JSONL session records from Claude Code, Codex CLI, Cursor, Gemini CLI, Copilot, OpenCode, ChatGPT exports, and related inputs. The primary trigger boundary is one discovered session file; `sync` filters live sessions, dropped record types, ignored projects/files, and unchanged mtimes before writing raw markdown.

**Extraction.** Extraction has two levels. First, code deterministically normalizes records, redacts sensitive material, counts turns/tools/tokens, derives metadata, and renders the conversation into markdown. Second, synthesis backends or agent workflows produce source summaries, claims, quotes, tags, connections, entity/concept pages, contradictions, and overview/index updates. The extraction oracle is mixed: deterministic Python for conversion and metadata; LLM/agent judgement for summaries, links, contradictions, and reusable lessons.

**Storage substrate.** Raw trace-derived artifacts live under `raw/sessions/`. Distilled wiki/source artifacts live under `wiki/`, including `wiki/sources/`, `wiki/entities/`, `wiki/concepts/`, `wiki/syntheses/`, `wiki/log.md`, and seeded navigation files. Derived exports live under `site/`, graph files, and machine-readable siblings. Operational lineage and idempotency live in JSON state files such as `.llmwiki-state.json`, `.llmwiki-synth-state.json`, `.llmwiki-queue.json`, and `.llmwiki-pending-prompts/`.

**Representational form.** Raw transcripts are prose/symbolic mixed artifacts: markdown conversation text plus structured frontmatter and metrics. Synthesized wiki pages are mostly prose with symbolic frontmatter and wikilinks. Static exports and MCP responses are structured JSON/text/HTML derived views. Prompts, slash commands, and skills are prose system-definition artifacts. Lint, lifecycle, candidate, adapter, and build code are symbolic system-definition artifacts. There is no implemented distributed-parametric memory state in the inspected code.

**Lineage.** The strongest lineage is raw session to converted markdown to generated site/export files. Synthesis adds a raw-file-to-wiki-source path using source frontmatter, state-file mtimes, and project/date/slug naming. That lineage is useful for regeneration, but it is not claim-level provenance: distilled claims, entity facts, and concepts do not store transcript-turn IDs or source spans by default. Static exports are derived views that can be deleted and regenerated from `raw/` and `wiki/`.

**Behavioral authority.** Raw transcript files are knowledge artifacts. Synthesized wiki pages are knowledge artifacts unless an agent consumes them as instructions. `CLAUDE.md`, `AGENTS.md`, slash commands, skills, config schedules, lint rules, lifecycle transitions, and candidate operations are system-definition artifacts with instruction, validation, routing, or governance authority. MCP search/query/read tools have activation and retrieval authority: they decide which retained artifacts enter an agent's context, but they do not by themselves verify or promote claims.

**Scope.** Scope is local-project or local-corpus learning. The system can summarize and expose a user's accumulated session history across projects, but it does not train a cross-project model or enforce a curated promotion path from repeated trace patterns into stronger rules without agent/human action.

**Timing.** Conversion can run on demand or on schedule; `sync` can auto-build and auto-lint according to config. Synthesis is staged and stateful, with optional agent-delegate completion. Static exports are batch-compiled. The advertised Auto Dream consolidation is not a demonstrated code path at this commit.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Pratiyush/llm-wiki is a trace-compilation and trace-distillation system. It strengthens the survey's distinction between raw trace artifacts and distilled behavior-shaping artifacts: the raw layer is evidentiary, while prompts, skills, lint rules, and synthesized pages can shape future agent behavior through different authority channels.

## Curiosity Pass

The repository has a lot of shipped surface area, but the strongest memory mechanism remains simple: find local traces, redact/normalize them, put them in markdown, then compile indexes and query/export views. This is a feature, not a weakness, because it preserves inspectability.

The docs and implementation disagree in a few important places. The README advertises 16 lint rules and Auto Dream consolidation; the CLI computes lint count from the live registry, and the inspected parser exposes no memory-consolidation command. Reviews should privilege the implemented CLI and modules over feature-list language.

The candidate workflow is a useful trust boundary, but it is not wired into every synthesis path as a mandatory promotion gate. `synthesize_new_sessions` writes source pages directly into `wiki/sources/`; candidate promotion is available for pages that land in `wiki/candidates/`, but the trust model depends on which workflow created the page.

The MCP server is a practical activation surface, but its ranking is keyword/token based over wiki pages and raw sessions, not semantic memory or audited retrieval. That keeps it cheap and inspectable; it also means a relevant lesson can stay inactive if the terms do not match.

## Takeaways

**Trace-derived does apply.** The code consumes agent session traces and creates durable raw and distilled retained artifacts that can shape future behavior through search, MCP, agent prompts, exports, and wiki pages.

**The system's best idea is lineage by layer.** Treat `raw/` as immutable evidence, `wiki/` as agent-maintained distillation, and `site/`/exports as disposable compiled views. This is a clean substrate split even when individual distilled claims need stronger provenance.

**Prompt files are not just documentation.** `CLAUDE.md`, `AGENTS.md`, slash commands, and skills are behavior-shaping system-definition artifacts. They deserve the same review attention as Python modules.

**Exports are activation infrastructure.** `llms.txt`, `.txt` siblings, `.json` siblings, graph exports, and MCP tools make the wiki consumable by other agents without scraping the UI.

**Advertised memory consolidation should not be credited as implemented memory.** The seeded `MEMORY.md` and documentation point toward cross-session consolidation, but implementation evidence at this commit supports scaffolding and instructions more than an autonomous consolidation loop.

## Open Questions

- Should synthesized claims carry stable pointers to raw transcript turns, tool calls, or source spans?
- Should candidate review become mandatory for LLM-created entity/concept pages, not just an optional workflow?
- Should `MEMORY.md` consolidation be implemented as a deterministic/agent command with review records, or removed from the advertised feature set until it exists?
- How should the system distinguish user-authored wiki pages from LLM-generated pages in frontmatter and lifecycle policy?
- Should MCP query results expose lineage and confidence fields alongside snippets so agents can decide whether to trust them?
- How should stale raw transcripts, redaction policy changes, and adapter schema changes invalidate downstream synthesized pages and exports?

## What to Watch

- Whether Auto Dream or equivalent `MEMORY.md` consolidation gains an executable command path and tests.
- Whether synthesis gains source-span provenance and claim-level audit metadata.
- Whether MCP query/search grows from keyword ranking into a lineage-aware activation layer.
- Whether lifecycle/confidence values become enforced gates for generated page consumption.
- Whether adapter support remains accurate as upstream session formats change.

## Bottom Line

Pratiyush/llm-wiki is a real trace-derived agent-memory system, not just a wiki scaffold. Its implemented contribution is the end-to-end file pipeline from local coding-agent sessions to raw markdown, distilled wiki pages, static/AI exports, and MCP/query surfaces. For commonplace, the main lesson is to borrow the layered trace substrate and compiled consumer views while keeping stricter claim lineage, explicit artifact authority, and validation gates before distilled trace knowledge becomes trusted memory.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: `llm-wiki` is trace compilation plus optional trace distillation into wiki/source artifacts and agent-facing compiled views.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: raw transcripts, synthesized pages, exports, MCP tools, prompts, skills, and validators need separate storage/form/lineage/authority treatment.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: raw transcripts, synthesized source pages, entity/concept pages, graph exports, and `.txt`/`.json` siblings mostly serve as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: `CLAUDE.md`, `AGENTS.md`, slash commands, skills, lint rules, lifecycle rules, and candidate workflows instruct or govern agents.
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - aligns: raw transcripts and pending prompts behave like a work-in-flight layer before durable distilled pages are trusted.
