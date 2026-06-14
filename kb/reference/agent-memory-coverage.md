---
description: "How Commonplace's shipped surfaces realize agent-memory requirements: control plane, contracts, storage roles, validation, review, activation, promotion, lifecycle, and current gaps"
type: kb/types/note.md
tags: []
status: current
---

# Agent memory coverage

Commonplace realizes agent memory as a file-backed knowledge base with a small command and skill surface. Its durable memory is not a single store. It is the combined system of authored artifacts, generated views, validation commands, review state, and always-loaded routing context that future agents can use inside bounded context.

The requirements come from [Designing a Memory System for LLM-Based Agents](../notes/designing-agent-memory-systems.md). This page maps those requirements to the shipped Commonplace system and names the main remaining limits.

## Coverage map

| Memory requirement | Commonplace realization | Current limit |
|---|---|---|
| Control-plane memory | `AGENTS.md` keeps KB goals, scope, routing, vocabulary, commands, skills, and git conventions in always-loaded context. See [control-plane goals](./control-plane-goals.md). | There is no typed on-situation cue index yet. |
| Direct memory creation | Agents and maintainers write notes, reference docs, ADRs, instructions, skills, source ingests, workshop artifacts, validators, and indexes as ordinary files. Commonplace implements direct-authored memory strongly through typed notes, indexes, instructions, skills, validation scripts, review gates, and explicit collection/type contracts. | Promotion decisions are still mostly manual. |
| Artifact contracts | `COLLECTION.md` defines each collection's register, quality goal, scope, and outbound-linking rules. The `type:` field points to a type-spec doc with structure, prose guidance, and schema. See [collections and types](./collections-and-types.md) and [type loading](./type-loading.md). | Project-specific collections still depend on users defining good contracts. |
| Import external knowledge | Source snapshots, ingest reports, conversion tooling, and staged workshops preserve external material and convert it toward Commonplace artifacts. | There is no mature graph-first or bulk-reingest pipeline. |
| Preserve evidence | Source snapshots and ingests preserve evidence for external sources. | Broad session-trace capture, redaction, retention, and replay are not shipped as a memory substrate. |
| Trace-derived extraction | `kb/log.md` can serve as a manual observation inbox between raw traces and durable artifacts. The current system is strongest once an agent or maintainer already understands what should be written. | Automated session-trace extraction is not implemented. |
| Discoverability | Titles, descriptions, tags, directory indexes, generated indexes, key-index pointers, `rg`, file paths, and skill metadata provide progressive routing surfaces. | Ranking and quality scoring remain underdeveloped. |
| Composability | Link prose, collection-owned link labels, claim titles, definitions, and indexes preserve relationships among artifacts. | Automated connection discovery is report-based, not continuously maintained. |
| Trust | Script validation checks frontmatter, links, enum values, required sections, and template headings. Review gates add semantic checks with stored acceptance state. See [review system architecture](./review-architecture.md). | Behavioral faithfulness and activation effects are not measured as first-class metrics. |
| Multiple consumer surfaces | Notes, reference docs, instructions, sources, reports, workshops, commands, skills, and control-plane files serve different agent, maintainer, reviewer, and workflow needs. | Retrospective episodes and typed cue indexes remain underdeveloped. |
| Storage roles | Authored markdown is the source of truth; generated indexes are rebuildable; reports are operational artifacts; review state lives in SQLite. See [storage](./storage-architecture.md). | Compiled behavior-facing views need stronger source-of-truth and regeneration rules. |
| Activation | Always-loaded `AGENTS.md`, on-demand file reads, and on-invoke skills load relevant memory into agent work. | Situation-triggered activation and behavioral faithfulness tests for activated memory remain future work. |
| Prose-to-code promotion | Repeated procedures and stable rules can become instructions, skills, type specs, schemas, review gates, validators, scripts, or commands. Manual promotion from log entries, notes, and workshops into stronger artifacts is supported. | There is no mature candidate queue that scores future value against maintenance cost. |
| Lifecycle | Status fields, validation failures, review staleness, generated-index refresh, workshop closure, and log review provide partial lifecycle handling. | Retirement, supersession, relaxation, recurrence tracking, and scheduled lifecycle work are incomplete. |
| Authority | Explicit files, git review, deterministic validation, and semantic review gates provide the current authority model for durable memory changes. | Authority for automatic extraction, promotion, activation, and retirement is not fully specified. |
| Evaluation | Structural validation and semantic review evaluate artifact quality. | Activation, behavioral uptake, context efficiency, source-alignment health, and promotion economics are not first-class metrics. |
| Native work environment | Markdown, git, shell commands, `.claude/skills/`, `.agents/skills/`, and package commands let Claude Code, Codex, and similar agents inspect and edit memory where they already work. See [architecture](./architecture.md) and [instruction generation](./instruction-generation.md). | Harness-specific execution policy differs across tools. |
| Reusable memory distribution | `commonplace-init` installs reusable methodology under `kb/commonplace/` while leaving user collections project-owned. Shared types stay in `kb/types/`; promoted skills are linked into harness skill directories. | Local project authority and shipped-library upgrades still require operator judgment. |

## Boundary

Commonplace is strongest today as a directly authored, quality-controlled, IDE-compatible memory substrate. It covers artifact contracts, discoverability, composability, validation, review, and source-of-truth boundaries well.

It is weaker as an autonomous learning system. Automated session-trace extraction, candidate promotion queues, on-situation cue activation, behavioral uptake tests, and mature lifecycle scheduling remain design work, not shipped capability.

## Related implementation references

- [Commonplace architecture](./architecture.md) — contains: installed layout, shipped library, user collections, and skill discovery surfaces
- [Storage](./storage-architecture.md) — contains: authored markdown, generated indexes, reports, and review SQLite state
- [Control-plane goals](./control-plane-goals.md) — contains: always-loaded KB goals and routing context in `AGENTS.md`
- [Collections and types](./collections-and-types.md) — implements: collection contracts plus type contracts
- [Type loading](./type-loading.md) — implements: path-valued type pointers and authoring-time contract loading
- [Review system architecture](./review-architecture.md) — implements: semantic review, provenance, acceptance, and stale-pair detection
- [Instruction generation](./instruction-generation.md) — implements: scaffold generation and multi-harness skill installation

---

Relevant Notes:

- [Designing a Memory System for LLM-Based Agents](../notes/designing-agent-memory-systems.md) — rationale: the requirements this shipped-system coverage map implements and partially leaves open
