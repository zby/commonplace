---
description: "Echel review: project-owned Markdown product memory, deterministic graph/report generation, evidence gates, and task-scoped agent packets"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
---

# Echel

Echel, from `alirezabbasi/echel`, is a local product-creation scaffold for AI-assisted software projects. It keeps product intent, scope, architecture, tasks, decisions, risks, evidence, logs, governance policy, and generated reports in a project-owned wiki plus `.echel` control files, then derives graph-backed work packets, reviews, readiness reports, proof packs, and cockpit views for the next product-owner or coding-agent action.

**Repository:** https://github.com/alirezabbasi/echel

**Reviewed commit:** [70edcf63f0625c7878a1829ff6ab9e3c9b529ae4](https://github.com/alirezabbasi/echel/commit/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4)

**Source directory:** `related-systems/alirezabbasi--echel`

## Core Ideas

**Product memory is file-native and project-owned.** The README frames Echel as a way to move product intelligence out of temporary AI conversations and into a living project memory, while `project.echel` maps symbolic roots such as `$WIKI_ROOT`, `$MEMORY_ROOT`, and governance files ([README.md](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/README.md), [project.echel](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/project.echel)). `ensure_product_pages()` scaffolds the wiki pages and folders that become the durable product surface: project, problem, users, solution, scope, roadmap, architecture, workflows, knowledge, decisions, work, and reports ([tools/echel/product.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/product.py)).

**The graph is deterministic extraction over the wiki.** `build_graph()` reads fixed pages and folders, extracts sections and bullets, adds product/problem/user/need/feature/requirement/component/workflow/task/decision/evidence/risk/milestone nodes, consumes manual graph extensions, and writes `wiki/graph.json` through `write_graph()` ([tools/echel/graph.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/graph.py)). The graph is not a vector index or graph database; it is a generated symbolic view over authored Markdown plus registered evidence.

**Context efficiency comes from bounded packets and bootstraps.** `session_bootstrap.py` prints a fixed startup bundle and truncates `wiki/log.md` to the most recent 120 lines, while `generate_work_packet()` assembles product context, graph context, task objective, acceptance criteria, evidence obligations, likely files, constraints, verification commands, required memory updates, and agent instructions for one task ([tools/session_bootstrap.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/session_bootstrap.py), [tools/echel/product.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/product.py), [schema/work-packet.schema.md](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/schema/work-packet.schema.md)). The efficiency mechanism is scaffolded selection and compact section rendering, not learned semantic retrieval.

**Governance is wired into the retained artifacts.** `doctor` validates primitive task/decision structure, evidence registry shape, evidence links, drift, and gates; `close-task` refuses completion unless the task references a known evidence ID ([tools/echel.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel.py), [tools/echel/evidence.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/evidence.py), [tools/echel/gates.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/gates.py)). Readiness and proof-pack generation carry the same design into milestone/release artifacts by combining graph validation, clarification gaps, task status, evidence registry state, risks, and review reports ([tools/echel/readiness.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/readiness.py)).

**The cockpit is an operator read surface with an allowlisted command bridge.** The FastAPI platform exposes dashboard snapshots over product memory, graph, tasks, packets, reviews, readiness, risks, decisions, contradictions, and logs, while `SAFE_COMMANDS` restricts cockpit actions to named Echel commands ([tools/echel/platform/cockpit.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/platform/cockpit.py), [tools/echel/platform/app.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/platform/app.py)). Platform chat messages persist in SQLite, but the inspected code does not mine chat transcripts into wiki edits, graph edges, rules, validators, or packets ([tools/echel/platform/storage.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/platform/storage.py)).

## Artifact analysis

- **Storage substrate:** `files` — The central retained behavior-shaping state is project-local Markdown and JSON under `wiki/`, `.echel`, `schema/`, `ruleset.md`, `docs/development/state/`, and generated report directories. The cockpit can also create `.echel/platform/platform.db`, but SQLite stores provider/thread/message UI state rather than the main product-memory substrate.
- **Representational form:** `prose` `symbolic` — Markdown pages, rules, packets, reviews, readiness reports, proof packs, logs, and task descriptions are prose; graph JSON, evidence registry JSON, gate policy, memory records, IDs, schemas, command contracts, validation results, and platform rows are symbolic. I did not find persisted embeddings, learned weights, or another parametric memory surface.
- **Lineage:** `authored` `imported` — Product pages are scaffolded, then authored by domain experts, operators, and agents; existing-source setup can import initial source material into the workspace; generated graph, packets, reports, readiness files, proof packs, and cockpit snapshots are derived from the current wiki, registry, gates, and validation state. Operational logs, memory records, and chat messages exist, but I did not find a trace-extraction pipeline that distills session or tool traces into durable product instructions.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` — Wiki pages, logs, cockpit views, and memory records provide knowledge; rules, schemas, packets, and agent instructions direct future work; `close-task`, gates, and readiness blockers enforce progress constraints; graph context and `next_task()` route work; doctor, primitive checks, evidence validation, graph validation, and readiness evaluate artifacts; graph-scored task selection ranks the next open task.

**Product wiki and development state.** `wiki/*.md`, `wiki/work/TASK-*.md`, `wiki/decisions/ADR-*.md`, `wiki/risks.md`, `wiki/log.md`, and development state files are the primary knowledge artifacts. They are human-readable source-of-truth surfaces until commands derive a graph, packet, review, readiness, or proof artifact from them ([tools/echel/product.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/product.py), [project.echel](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/project.echel)).

**Product graph.** `wiki/graph.json` and `wiki/reports/product-graph-report.md` are symbolic/prose derived views. They are regenerated from wiki sections, task files, ADR files, the evidence registry, risks, milestones, and manual graph declarations, then consumed by graph status, graph validation, next-task selection, work packets, reviews, readiness, and cockpit snapshots ([tools/echel/graph.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/graph.py), [schema/product-graph.schema.md](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/schema/product-graph.schema.md)).

**Work packets and review reports.** Generated packets and reviews are the strongest agent-facing artifacts. Packets translate product memory into task-scoped instructions before implementation; reviews check acceptance criteria, definition of done, verification commands, graph integrity, and evidence references after or around implementation ([tools/echel/product.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/product.py), [schema/review.schema.md](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/schema/review.schema.md)).

**Evidence, gates, readiness, and proof packs.** `.echel/evidence_registry.json`, `.echel/gates.json`, `doctor`, readiness reports, proof packs, and release summaries form the governance layer. Their authority is stronger than ordinary product context because they can block task closure, mark readiness blockers, and require registered evidence before a task or release advances ([tools/echel.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel.py), [tools/echel/readiness.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/readiness.py), [schema/proof-pack.schema.md](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/schema/proof-pack.schema.md)).

**Memory records and cockpit state.** `.echel/memory_records.jsonl` supports manual typed records, contradiction flags, links, payloads, and lexical query; the cockpit SQLite store keeps provider, thread, and chat-message state ([tools/echel/memory_kernel.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/memory_kernel.py), [tools/echel/platform/storage.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/platform/storage.py)). These are side lanes today: useful for operator recall and dashboard display, but not the main product-memory derivation path.

**Promotion path.** Echel promotes authored product memory into a generated graph, graph-plus-task state into work packets and review reports, and evidence/review/graph/risk state into readiness and proof artifacts. The authority increase stays inspectable because each promoted artifact is another file rather than an opaque service state.

## Comparison with Our System

| Dimension | Echel | Commonplace |
|---|---|---|
| Primary purpose | Product operating memory for AI-assisted software creation | Methodology KB and framework for agent-operated knowledge bases |
| Main substrate | Project-owned `wiki/`, `.echel` control files, schemas, generated reports, optional cockpit SQLite | Git-tracked `kb/` collections, type specs, validators, source snapshots, generated indexes, review artifacts |
| Context strategy | Session bootstrap, graph-backed task packets, cockpit snapshots, readiness/proof reports | `rg`, indexes, authored links, collection contracts, skills, validation and review reports |
| Governance | Evidence registry, close-task enforcement, gates, graph validation, readiness blockers | Frontmatter schemas, collection/type contracts, validation, semantic reviews, archive/replacement lifecycle |
| Learning loop | Manual/agent-authored product memory plus deterministic derived artifacts | Manual/agent-authored KB artifacts plus validation, review, source snapshots, and promotion workflows |

Echel is close to Commonplace in its file-native premise: durable project intelligence belongs in inspectable artifacts, and future agents should start from governed state rather than chat history. The difference is scope. Echel narrows the system around product creation, task execution, evidence, and release readiness. Commonplace is a general methodology KB framework with stronger collection/type discipline and broader cross-artifact linking.

The most useful divergence is Echel's generated handoff layer. Commonplace already has instructions, reports, indexes, and validation, but many workflows still require the agent to assemble the working context manually. Echel shows a narrower pattern: generate the packet that a specific agent action should consume, including the task, relevant graph context, likely files, evidence obligations, verification, and required memory updates.

Echel's weaker point is semantic fragility. Its graph extractor keys on fixed headings, bullets, filenames, and IDs. That works because the scaffold controls the wiki shape, but it is less portable than Commonplace's type-aware parsing, authored links, and collection contracts.

### Borrowable Ideas

**Task-scoped generated handoffs.** Ready for repeated Commonplace workflows. A review, ingest, or migration command could generate one Markdown packet containing target artifact, collection contract, type contract, recent validation/review findings, relevant notes, required evidence, and post-work surfaces.

**Evidence IDs as closure currency.** Ready for high-authority workflows, not ordinary note writing. Echel's `close-task` gate is blunt but useful: implementation work cannot close until registered evidence exists and is linked from the task.

**Generated readiness as a durable artifact.** Ready as a reporting convention. Echel writes readiness, proof-pack, and release-summary files instead of making readiness a dashboard-only state, which fits Commonplace's preference for reviewable repo artifacts.

**Allowlisted cockpit commands.** Ready as an implementation constraint if Commonplace gains a local UI. Echel's cockpit exposes memory and safe actions without exposing arbitrary shell execution.

**Do not borrow heading-fragile graph extraction as the core semantic layer.** Needs a stronger parser if transplanted. Commonplace should keep using typed frontmatter, collection contracts, links, and validators before deriving graph views with behavioral authority.

## Write side

**Write agency:** `manual` `automatic` — Users and agents manually author product pages, tasks, decisions, risks, memory records, evidence registry entries, and steering updates; Echel automatically writes generated graph files, work packets, review reports, readiness reports, proof packs, release summaries, log entries, status changes, gate reports, and cockpit/platform state through its commands.

**Curation operations:** `consolidate` `synthesize` `promote` — Work packets consolidate product pages, graph context, task criteria, likely files, and evidence duties into a compact handoff; graph reports, review reports, readiness reports, proof packs, and release summaries synthesize new derived artifacts across multiple stored entries; task closure and readiness/proof generation promote task/evidence/review state into stronger progress and release-decision artifacts. I did not find automatic deduplication, decay, in-place evolution, or trace-mined learning.

## Read-back

**Read-back:** `both` — Echel supports pull through file reads, CLI commands, `memory query`, graph/status/review/readiness commands, and cockpit dashboard APIs; it also pushes retained memory when session bootstrap and generated work packets place selected product memory into an agent's starting or task-specific context.

**Read-back signal:** `coarse` `identifier` — Session bootstrap is a coarse fixed bundle. Work packets, review reports, graph context, and next-task selection are instance-targeted by task IDs, fixed wiki paths, graph node IDs, evidence IDs, configured roots, and status fields rather than embedding or LLM relevance.

**Faithfulness tested:** `no` — The repository validates artifact shape, evidence links, graph integrity, gates, and readiness, but I did not find a with/without test proving that bootstrap context or generated packets improve downstream agent behavior.

**Direction edge cases.** Static rules, schemas, and prompt files are baseline instruction and do not by themselves count as memory read-back. The memory-specific push is in the generated or printed surfaces that include current project state: `session_bootstrap.py` and `generate_work_packet()`.

**Targeting and signal.** Pull paths are explicit operator or host calls. Push paths are either coarse fixed-file inclusion or identifier-selected packet/report generation. `next_task()` can choose the graph-preferred open task by task node, requirement/risk edges, and `TBD` penalties, but the signal is still symbolic/identifier-based rather than semantic inference ([tools/echel/product.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/product.py)).

**Injection point.** Bootstrap and packets are pre-invocation context: they are meant to be read before the next implementation or review action. Review, readiness, and proof-pack reports can also become future pre-invocation constraints when handed to an agent for follow-up, but their generation immediately after work is write-side maintenance.

**Selection, scope, and complexity.** Selection is bounded by fixed startup files, recent-log slicing, one task, graph-neighborhood formatting, compact product sections, evidence obligations, likely-file lists, and status/gate summaries. Complexity remains moderate because a packet mixes strategy, graph nodes, task criteria, file hints, verification, and memory-update instructions in one document; there is no token-budgeted top-k memory selector.

**Authority at consumption.** Work packets, schemas, rules, and closure gates carry instruction, validation, and enforcement force when an agent follows the Echel workflow. Cockpit/status views are mostly advisory until the operator triggers a safe command that writes or gates artifacts. Effective uptake by a model agent is not verified from code.

**Other consumers.** Product owners consume the same retained state through cockpit snapshots, readiness reports, proof packs, release summaries, graph reports, risks, decisions, and logs. Echel treats the human steering surface as part of the memory system rather than an afterthought.

## Curiosity Pass

**The "typed graph" is intentionally ordinary.** The graph has authority because downstream commands consume it, not because it is a learned index or database-backed reasoning layer. That makes it easy to inspect and easy to break if the wiki shape drifts.

**The smallest explicit memory kernel is not the main memory system.** `.echel/memory_records.jsonl` supports typed records and contradiction queries, but most memory behavior flows through the wiki, graph, reports, gates, and packets.

**Cockpit chat is storage, not trace learning.** Chat messages persist and `/echel` commands can run allowlisted actions, but there is no inspected path from chat messages to proposed wiki edits, task creation, graph changes, rules, or validators.

**The work packet is the highest-leverage artifact.** The wiki is the source of truth, but the packet is where retained product state becomes immediate next-action guidance for a coding agent.

**The system is more scaffold than package.** The reviewed checkout has local scripts, Make targets, schemas, docs, prompts, wiki files, and tools, but no package manifest. That favors copyable project scaffolding over a clean reusable library boundary.

## What to Watch

- Whether cockpit chat starts proposing or applying wiki edits, tasks, decisions, evidence entries, or memory records. That would change the trace-learning verdict.
- Whether graph extraction moves from fixed headings and bullets to typed frontmatter, schemas, or richer authored links. That would make graph-derived authority less fragile.
- Whether work packets gain token budgets, provenance per included claim, or freshness checks. That would strengthen context efficiency and auditability.
- Whether `.echel/memory_records.jsonl` starts feeding graph generation, packet assembly, contradiction handling, or readiness. That would turn it from a side query store into a central retained-artifact lane.
- Whether readiness gates become configurable enough for project-specific policies without editing Python.
- Whether a packaged installation boundary appears. That would change Echel from a copied scaffold into a more maintainable framework component.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes Echel's stored wiki from bootstrap and packet surfaces that actually re-enter agent context.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies to Echel's wiki pages, graph, packets, reports, gates, evidence registry, memory records, and cockpit state.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies product pages, logs, memory records, graph reports, cockpit views, and proof evidence before they gain stronger action force.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies rules, schemas, work packets, closure gates, validation, readiness blockers, and allowlisted cockpit commands.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames Echel's main mechanism: routing bounded product memory into the next agent session or task.
