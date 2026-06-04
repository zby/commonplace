---
description: "Echel review: product-owned Markdown wiki, generated graph/work packets, readiness gates, cockpit views, and task-scoped push read-back for AI coding"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-03"
tags: [push-activation]
---

# Echel

Echel, from `alirezabbasi/echel`, is a product-creation scaffold and local operating system for AI-assisted software work. At the reviewed commit it keeps product intent, requirements, architecture, tasks, decisions, evidence, risks, logs, and reports in a project-owned `wiki/`, derives a typed product graph from that wiki, and generates work packets, review reports, readiness reports, proof packs, and cockpit views so future agents can resume from project state instead of chat history.

**Repository:** https://github.com/alirezabbasi/echel

**Reviewed commit:** [70edcf63f0625c7878a1829ff6ab9e3c9b529ae4](https://github.com/alirezabbasi/echel/commit/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4)

**Last checked:** 2026-06-03

## Core Ideas

**Product memory lives beside the product, not inside the conversation.** The generated workspace separates project-owned `wiki/` from ignored `echel-core/`, and `project.echel` maps symbolic roots such as `$WIKI_ROOT` and `$MEMORY_ROOT` ([project.echel](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/project.echel), [tools/project_init.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/project_init.py)). The important retained state is ordinary Markdown and JSON under the project repository: product pages, tasks, decisions, reports, graph output, logs, rules, schemas, gate policy, evidence registry, and optional memory records.

**The product graph is a generated symbolic view over Markdown.** `build_graph()` reads fixed wiki pages and folders, extracts sections and bullets, adds product/problem/user/need/feature/requirement/component/workflow/task/decision/evidence/risk/milestone nodes, and writes `wiki/graph.json` through `write_graph()` ([tools/echel/graph.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/graph.py)). This is not embedding retrieval or graph-database memory. It is a deterministic index over authored product memory plus registered evidence.

**Context efficiency is packetized and scaffolded rather than semantic.** Echel reduces context volume by asking agents to load selected startup files or a generated work packet instead of the whole wiki. `session_bootstrap.py` prints rules, schema, core index/project/log/state files with a bounded recent-log slice, while `generate_work_packet()` compacts product context, graph context, task objective, acceptance criteria, likely files, verification, and memory-update obligations into one task-scoped handoff ([tools/session_bootstrap.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/session_bootstrap.py), [tools/echel/product.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/product.py), [schema/work-packet.schema.md](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/schema/work-packet.schema.md)). The complexity boundary is coarse but legible: session baseline, task packet, graph report, review report, readiness report.

**Governance is part of the memory model.** Tasks require context, objective, scope, acceptance criteria, definition of done, verification commands, and documentation updates; evidence IDs are validated through `.echel/evidence_registry.json`; `close-task` refuses closure without registered evidence; and `doctor` combines primitive validation, evidence links, coherence drift, and gates ([schema/task.schema.md](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/schema/task.schema.md), [tools/echel/evidence.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/evidence.py), [tools/echel.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel.py), [tools/echel/gates.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/gates.py)). Memory is intended to be actionable and auditable, not just searchable.

**The cockpit is a local read surface and safe command bridge.** The FastAPI platform reads the same wiki, graph, reports, risks, decisions, contradictions, and readiness state into dashboard APIs, while restricting command execution to a fixed safe-action set ([tools/echel/platform/app.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/platform/app.py), [tools/echel/platform/cockpit.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/platform/cockpit.py), [docs/development/phase4-product-cockpit.md](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/docs/development/phase4-product-cockpit.md)). The cockpit can also store chat provider/thread state in a local platform database, but the inspected code does not use those chat records as the source of product-memory learning.

**Trace-like records exist, but trace-derived learning is not implemented.** `wiki/log.md`, `.echel/memory_records.jsonl`, and cockpit chat messages preserve operational traces, and `memory query` can search manually-added memory records ([tools/echel/memory_kernel.py](https://github.com/alirezabbasi/echel/blob/70edcf63f0625c7878a1829ff6ab9e3c9b529ae4/tools/echel/memory_kernel.py)). I did not find a pipeline that ingests session transcripts, tool traces, or repeated trajectories and distills them into durable rules, validators, graph edges, or prompt instructions. The standing learning loop is manual/governed: agents and operators update canonical wiki artifacts, then Echel derives reports and graph views.

## Artifact analysis

- **Storage substrate:** `files` - The central retained state is project-local Markdown/JSON: `wiki/*.md`, `wiki/work/TASK-*.md`, `wiki/decisions/ADR-*.md`, `wiki/reports/**`, `wiki/graph.json`, `ruleset.md`, `schema/*.md`, `project.echel`, `.echel/gates.json`, `.echel/evidence_registry.json`, and `.echel/memory_records.jsonl`. The optional cockpit also uses SQLite under `.echel/platform/`, but that is not the main project-memory substrate.
- **Representational form:** `prose` `symbolic` - Prose Markdown carries product intent, decisions, risks, tasks, reports, rules, and agent instructions; symbolic JSON carries config, graph nodes/edges, evidence registry, gates, memory records, and platform state; Python code and schemas define the generators, validators, and command contracts.
- **Lineage:** `authored` `imported` - Product memory is scaffolded from CLI inputs or existing-source mode, then authored by domain experts and agents; generated graph, packets, reports, and readiness views are derived from the current wiki, evidence registry, gates, and validation state rather than from session traces.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` - Wiki pages and cockpit views provide product context; work packets, rules, schemas, evidence gates, graph validation, readiness reports, and graph-selected tasks instruct, gate, route, validate, and prioritize future work.

**Product wiki pages.** Storage substrate: `wiki/` Markdown files generated and updated by `project_init.py`, `ensure_product_pages()`, `define`, `clarify`, `steer`, and manual/agent edits. Representational form: prose with YAML frontmatter and conventional sections. Lineage: initially scaffolded from CLI inputs or existing-source mode, then authored by domain experts and agents. Behavioral authority: knowledge artifacts when read as product context, and weak system-definition artifacts when rules/prompts require agents to update or obey the pages.

**Tasks, decisions, risks, evidence, and logs.** Storage substrate: `wiki/work/`, `wiki/decisions/`, `wiki/risks.md`, `wiki/log.md`, and `.echel/evidence_registry.json`. Representational form: mixed prose sections plus symbolic IDs such as `TASK-####`, `ADR-####`, and `EVID-*`. Lineage: authored or generated by commands, with evidence links validated against the registry. Behavioral authority: task and evidence artifacts become system-definition constraints for closure, review, readiness, and future work-packet generation.

**Generated product graph.** Storage substrate: `wiki/graph.json` plus generated `wiki/reports/product-graph-report.md`. Representational form: symbolic JSON graph and prose report. Lineage: derived from current wiki sections, bullets, task files, ADRs, evidence registry, risks, milestones, and manual graph extensions. Behavioral authority: routing/ranking-ish system-definition artifact because `next_task()`, work packets, review reports, cockpit views, graph validation, and readiness summaries use the graph to decide what context and issues to surface. It is regenerated, not source of truth.

**Work packets and review reports.** Storage substrate: `wiki/reports/work-packets/{TASK}-packet.md` and `wiki/reports/reviews/{TASK}-review.md`. Representational form: prose Markdown handoffs with symbolic frontmatter and checklists. Lineage: derived from task files, product pages, graph output, evidence IDs, and validation state. Behavioral authority: high-authority system-definition artifacts for agents because they package the next objective, acceptance criteria, likely files, constraints, verification commands, evidence obligations, required memory updates, and review gaps.

**Readiness reports, proof packs, and release summaries.** Storage substrate: generated Markdown under `wiki/reports/readiness/`, `wiki/reports/proof-packs/`, and `wiki/reports/releases/`. Representational form: mixed prose and symbolic status/check summaries. Lineage: derived from graph validation, clarification gaps, task status, evidence registry, risks, and review reports. Behavioral authority: audit and gate artifacts; they do not implement code behavior directly, but they decide whether a milestone or release should advance.

**Rules, schemas, prompts, and command contracts.** Storage substrate: `ruleset.md`, `docs/ruleset.md`, `schema/*.md`, `prompts/{claude-code,codex,cursor}/`, `Makefile`, and `tools/echel.py`. Representational form: mixed prose instruction, symbolic schema requirements, and executable Python/Make targets. Lineage: authored framework artifacts copied into `echel-core/` for new workspaces. Behavioral authority: system-definition artifacts with instruction and enforcement force over agents and commands; they tell agents what to load, what to update, and which gates must pass.

**Cockpit and chat state.** Storage substrate: generated `.echel/platform/config.json`, `.echel/platform/platform.db`, and in-memory/API response objects. Representational form: symbolic SQLite rows plus prose chat messages and dashboard JSON. Lineage: user/provider configuration, cockpit commands, chat messages, and live reads from wiki/graph/report state. Behavioral authority: mostly operator-facing knowledge artifact and command surface; safe cockpit actions can trigger Echel generators, but chat transcripts are not distilled into project memory by the inspected implementation.

**Promotion path.** Echel promotes authored product intent into canonical wiki pages, wiki pages into a generated product graph, graph/task state into work packets and review reports, and evidence/review/readiness state into proof packs. The authority jump is explicit: product notes become task-scoped instructions and closure gates only after passing through generators and validators.

## Comparison with Our System

| Dimension | Echel | Commonplace |
|---|---|---|
| Primary purpose | Product-creation operating system for AI-assisted software projects | Methodology KB and framework for agent-operated knowledge bases |
| Main retained artifact | Product-owned `wiki/` plus generated graph/reports and `.echel` governance state | Typed Markdown collections, sources, reviews, reports, generated indexes, validation state |
| Context strategy | Session bootstrap plus task-scoped work packets and cockpit snapshots | Search, indexes, links, collection contracts, skills, validation/review reports |
| Retrieval/read-back | Pull CLI/cockpit views and push-style task handoffs for agents | Mostly pull by `rg`/indexes/links/skills, with some workflow-specific generated reports |
| Governance | Task schema, evidence registry, close-task checks, graph validation, gates, readiness reports | Type specs, schemas, collection contracts, validation, semantic reviews, archive/replacement workflow |
| Learning loop | Manual project-memory updates plus deterministic derived views | Manual/agent-authored KB artifacts plus validation, review, source snapshots, and promotion workflows |

Echel is close to Commonplace in its belief that durable project intelligence belongs in inspectable files and that future agents need governed handoffs, not only chat summaries. Its strongest design move is narrower than Commonplace's broad KB methodology: for product work, it names the operating loop and generates exactly the artifacts a coding agent or product owner needs next.

The divergence is type discipline and abstraction level. Commonplace treats collection contracts and type specs as the standing semantic layer. Echel uses conventional filenames, headings, schemas, and generators: powerful enough for one product scaffold, less general as a cross-domain knowledge system. Echel's graph extraction is also brittle by design because it keys on specific sections and bullets, while Commonplace usually leaves richer semantics in authored links, frontmatter, and validation rules.

**Read-back:** `both` - Agents and operators can pull memory through CLI/cockpit/status/graph/query commands, but generated work packets, session-bootstrap output, and prompt files also push selected retained product memory into the next agent session or task handoff.

### Borrowable Ideas

**Generate task-scoped handoffs from standing memory.** Commonplace could produce review/write packets that assemble target artifact, relevant collection contract, recent reports, validation requirements, and required update surfaces. Ready for high-repetition workflows, especially reviews and source ingests.

**Treat evidence IDs as closure currency.** Echel's `close-task` gate is simple: a task cannot close without registered evidence. Commonplace could borrow this for high-authority migrations or review sweeps where every accepted change should cite a report, test, or source snapshot. Needs careful scope so ordinary note writing does not become ceremony.

**Expose readiness as a generated artifact, not a dashboard-only status.** Echel writes readiness, proof-pack, and release-summary files that can be reviewed and committed. Commonplace should keep preferring durable reports over ephemeral UI status when a workflow needs auditability. Ready now as a reporting convention.

**Use a safe command bridge for cockpit-like tools.** The cockpit only runs a fixed set of actions. If Commonplace gets a richer local UI, its command bridge should follow the same allowlist pattern rather than exposing arbitrary shell execution. Ready as an implementation constraint.

**Do not borrow section-fragile graph extraction as the primary semantic model.** Echel's graph is useful because the scaffold controls the wiki shape. Commonplace's heterogeneous collections need stronger type-aware parsing and authored semantics before graph output should guide agent behavior.

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Read-back placement

**Direction.** Both. Operators and agents pull retained memory through `status`, `graph show/report`, `memory query`, cockpit dashboard APIs, and file reads. Echel also produces push-style agent handoffs: `session_bootstrap.py` prints the baseline memory bundle, prompt files tell agents what to load, and `build`/`packet` generates a work packet from the active task and graph.

**Read-back signal:** `coarse` `identifier` - Session bootstrap is a coarse baseline bundle, while work packets and review reports select retained product memory by task ids, fixed wiki paths, graph node ids, evidence ids, and configured roots.

**Faithfulness tested:** `no` - Echel validates artifact structure, evidence links, graph integrity, drift, and gates, but the review found no with/without test proving that pushed packets or bootstrap context improve agent behavior.

**Targeting and signal.** Targeting is `instance` for work packets and review reports: a task id, or the graph-selected next open task, determines which product context, graph context, acceptance criteria, likely files, and evidence obligations are assembled. The signal is `identifier`, because selection keys on task ids, fixed wiki paths, graph node ids, evidence ids, and configured root names rather than semantic relevance inference. Session bootstrap is a coarser always-load baseline.

**Injection point.** The push-style surfaces fire before implementation or review: the packet and bootstrap output are meant to be read before the agent writes code. Review reports and readiness reports are post-action audit surfaces unless a future agent receives them as constraints for follow-up work.

**Selection, scope, and complexity.** Context volume is bounded by fixed file lists, recent-log slicing, compacted section summaries, graph-neighborhood formatting, and task-specific packet sections. Complexity remains moderate because a packet mixes product strategy, graph nodes, acceptance criteria, file guesses, verification, and memory-update obligations in one document. There is no token-aware top-k memory selector or semantic deduplication layer.

**Authority at consumption.** Work packets and schema/rules files carry instruction and enforcement authority when handed to an agent: they define what to implement, what evidence to produce, what memory to update, and what gates to respect. Cockpit/status views are mostly advisory knowledge artifacts unless the operator triggers a safe command that regenerates or gates artifacts.

**Faithfulness.** Echel validates artifact structure, evidence links, graph integrity, drift, and gates, but it does not test whether an agent given a work packet behaves better than an agent without it. Effective use of pushed memory is therefore not verified from code.

**Other consumers.** Product owners consume the same memory through the cockpit, readiness reports, proof packs, release summaries, and logs. That human steering surface is part of the design, not an incidental UI: Echel treats the product owner as accountable for keeping intent and quality intact.

## Curiosity Pass

**The README says "typed graph underneath," but the implementation is a deterministic file-derived graph.** That is not a flaw, but it matters. The graph has authority because downstream commands consume it, not because it has independent storage or inference semantics.

**The memory kernel is much smaller than the product wiki.** `.echel/memory_records.jsonl` can record and query manual memory records, including contradictions, but most implemented memory behavior flows through `wiki/`, graph generation, reports, and gates.

**Echel has many governance surfaces with little package boundary.** There is no `pyproject.toml` or installable package metadata in the reviewed checkout; commands run as local scripts copied into `echel-core/`. That favors inspectability and scaffold use, but makes reuse depend on copying the whole method/tools directory.

**The cockpit's chat is not yet a learning loop.** Chat messages persist in the platform store and can call safe Echel commands, but I found no code path that mines those conversations into wiki updates, graph edits, rules, or tasks.

**The strongest agent-memory artifact is the work packet.** The wiki is the source of truth, but the packet is where retained product state becomes immediate next-action guidance.

## What to Watch

- Whether cockpit chat starts creating proposed wiki edits, tasks, decisions, or memory records from conversation. That would change the trace-derived learning decision.
- Whether graph extraction moves from fixed headings/bullets to typed frontmatter or schemas. That would make Echel's derived graph less scaffold-fragile and more portable.
- Whether work packets gain token budgets, source freshness, or explicit provenance per included claim. That would strengthen context efficiency and auditability.
- Whether `memory_records.jsonl` becomes integrated with graph generation, contradiction management, or packet assembly. That would make it a real retained-artifact lane rather than a side query store.
- Whether readiness gates become configurable enough for project-specific release policies without editing Python code.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Echel activates retained product memory through generated packets and bootstrap surfaces, not only by storing wiki pages.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - grounds: Echel separates wiki pages, graph output, reports, rules, gates, evidence registry, cockpit state, and memory records by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: work packets, rules, schemas, evidence gates, and readiness reports carry instruction, validation, audit, or closure force.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: product pages, logs, cockpit views, and source summaries provide evidence/reference/context until promoted into task or gate authority.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Echel's main value is routing product memory into the bounded context of the next agent session or product decision.
