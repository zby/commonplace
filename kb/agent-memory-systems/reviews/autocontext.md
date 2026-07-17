---
description: "Autocontext review: iterative evaluation harness with trace-learning playbooks, hints, skills, tools, validators, runtime traces, and optional model distillation"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
tags: [trace-learning]
---

# Autocontext

Autocontext, by greyhaven-ai, is a Python and TypeScript control plane for running iterative agent/scenario evaluations and carrying forward what worked. Its memory system is not a standalone recall database: it is a run/knowledge/artifact substrate that turns scored generations, role outputs, runtime sessions, and production traces into playbooks, hints, operational lessons, generated tools, harness validators, exported skills, datasets, and optional local model artifacts.

**Repository:** https://github.com/greyhaven-ai/autocontext

**Reviewed commit:** [d381f21e17e405885aab4ff3a4e6475402bae8db](https://github.com/greyhaven-ai/autocontext/commit/d381f21e17e405885aab4ff3a4e6475402bae8db)

**Last checked:** 2026-06-04

## Core Ideas

**Memory is organized around evaluated runs, not free-form recall.** A run records generations, matches, role outputs, validation results, replays, reports, and traces, while the scenario knowledge directory accumulates the playbook, hints, lessons, dead ends, tools, harness files, mutation state, snapshots, and exported packages that should influence later generations ([README.md](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/README.md), [autocontext/src/autocontext/storage/artifacts.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/storage/artifacts.py), [autocontext/src/autocontext/storage/sqlite_store.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/storage/sqlite_store.py)). The source-of-truth rhythm is "try, score, gate, persist, feed forward."

**Trace-derived curation is first-class.** The coach prompt is explicitly asked to produce a replacement playbook, operational lessons, and competitor hints from prior generation evidence; optional curator passes can accept, reject, merge, or consolidate those lessons; rollback paths append dead ends; architects can create tools, validators, and harness mutations ([autocontext/src/autocontext/prompts/templates.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/prompts/templates.py), [autocontext/src/autocontext/agents/curator.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/agents/curator.py), [autocontext/src/autocontext/loop/stage_helpers/persistence_helpers.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/loop/stage_helpers/persistence_helpers.py), [autocontext/src/autocontext/harness/mutations/store.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/harness/mutations/store.py)).

**Context efficiency is handled by component compaction, budgets, and progressive surfaces.** Prompt assembly separates playbook, trajectory, lessons, tools, analysis, hints, dead ends, notebooks, reports, evidence manifests, and session history before compacting and trimming them. Component caps, deduplication, role-scoped exclusions, protected hints/dead ends, and compaction ledgers make the prompt budget observable, though token estimation is a char/4 heuristic rather than tokenizer-accurate ([autocontext/src/autocontext/prompts/context_budget.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/prompts/context_budget.py), [autocontext/src/autocontext/knowledge/compaction.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/knowledge/compaction.py), [autocontext/src/autocontext/storage/context_selection_store.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/storage/context_selection_store.py)).

**The same learned state is served through multiple adoption surfaces.** Autocontext exposes CLI, SDK, HTTP, MCP, Pi, Hermes, Claude Code skill export, and TypeScript surfaces. The MCP tools read playbooks, trajectories, analyses, hints, generated tools, skills, solved packages, feedback, and runtime sessions; exported packages turn accumulated scenario knowledge into portable agent skills ([autocontext/src/autocontext/mcp/knowledge_tools.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/mcp/knowledge_tools.py), [ts/src/mcp/knowledge-readback-tools.ts](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/ts/src/mcp/knowledge-readback-tools.ts), [autocontext/src/autocontext/knowledge/export.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/knowledge/export.py), [autocontext/docs/agent-integration.md](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/docs/agent-integration.md)).

**It can cross from prose memory into symbolic policy and parametric state.** Learned playbooks and hints are prose, but generated validators, tools, mutation specs, strategy packages, context-selection decisions, production-trace manifests, and distillation manifests are symbolic. Training export and the autoresearch training runner can turn trace-derived records into model artifacts registered for cheaper local runtimes ([autocontext/src/autocontext/training/export.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/training/export.py), [autocontext/src/autocontext/training/runner.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/training/runner.py), [ts/src/traces/distillation-pipeline.ts](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/ts/src/traces/distillation-pipeline.ts)).

## Artifact analysis

- **Storage substrate:** `files` — The primary retained store is the file tree: `runs/<run_id>/`, `knowledge/<scenario>/`, `skills/`, `.autocontext/production-traces/`, compaction ledgers, generated tools, harness files, packages, and optional training workspaces. SQLite stores run/generation/match/role metrics, feedback, task queues, runtime-session indexes, and analytics support state; model checkpoints and blob mirrors are secondary substrates rather than the canonical knowledge surface.
- **Representational form:** `prose` `symbolic` `parametric` — Playbooks, analyses, hints, reports, lessons, exported skills, and curator outputs are prose; JSON/JSONL records, SQLite rows, metrics, manifests, context-selection records, mutation specs, validators, tools, and schemas are symbolic; optional training outputs and model registry entries add a parametric layer.
- **Lineage:** `authored` `imported` `trace-extracted` — Scenarios, tasks, policies, hooks, and operator feedback can be authored or imported; run events, role outputs, score trajectories, production traces, session logs, compaction entries, credit assignments, lessons, dead ends, and training datasets are derived from execution traces.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — Playbooks, analyses, traces, reports, and packages provide evidence/context; generated skills, prompt fragments, role prompts, and context policies instruct; scenario contracts, staged validators, mutation gates, and harness files enforce or validate; family routing, role routing, search, and context-selection records route and rank; training and distillation surfaces provide learning input.

**Scenario knowledge.** `knowledge/<scenario>/playbook.md`, `hints.md`, `hint_state.json`, `lessons.json`, `dead_ends.md`, `analysis/`, `coach_history.md`, `architect/changelog.md`, `tools/`, `harness/`, `mutations.json`, and snapshots are the central behavior-shaping artifacts. Their authority varies: a playbook is advisory context for the competitor, a harness validator can block a candidate, and a mutation can become a prompt or context policy after gating.

**Run artifacts.** `runs/<run_id>/generations/gen_<n>/` holds metrics, replay JSON, role Markdown, curator outputs, and compaction artifacts. SQLite stores generation metrics, matches, role outputs, staged validation results, consultations, and feedback. These are raw and derived traces; they become future knowledge when coach, curator, export, or training flows select from them.

**Context-selection and compaction records.** Context budgeting produces decision records with candidate/selected hashes, token estimates, selection reasons, dedupe and trim counts, useful-candidate recall fields, and compaction cache metrics ([autocontext/src/autocontext/knowledge/context_selection.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/knowledge/context_selection.py)). These records audit serving behavior, but they do not prove the model used the selected memory.

**Production traces and distillation datasets.** The production trace SDK writes validated JSONL batches under `.autocontext/production-traces/incoming/`; the TypeScript ingest path validates, deduplicates, redacts, moves accepted traces, writes receipts/errors, and enforces retention under a lock ([autocontext/src/autocontext/production_traces/emit.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/production_traces/emit.py), [ts/src/production-traces/ingest/scan-workflow.ts](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/ts/src/production-traces/ingest/scan-workflow.ts)). The distillation pipeline filters those traces into train, held-out, eval-only, and contrastive JSONL plus a manifest.

**Promotion path.** The strongest path is trace -> scored generation -> coach/curator judgment -> playbook/hints/lessons/skill/tool/harness mutation -> next prompt or validator. A second path is production/run traces -> curated dataset -> training workspace -> model registry artifact. The system has several gates, but semantic provenance for individual prose claims depends on the agent output; not every lesson is forced to cite the exact run event that justified it.

## Comparison with Our System

Autocontext and Commonplace both preserve inspectable file artifacts and make generated views subordinate to canonical knowledge. The divergence is purpose and authority. Commonplace is a durable methodology KB: collection contracts, type specs, link semantics, validation, and review gates govern artifacts before they become trusted future context. Autocontext is an experimental control loop: scored traces and role prompts generate candidate knowledge quickly, then scenario evaluation decides whether it helped.

Autocontext is stronger as an online learning harness. It has a concrete loop for producing playbooks, hints, lessons, tools, validators, datasets, and model artifacts from evaluated attempts. Commonplace is stronger as a long-lived epistemic library: it can say why an artifact is valid, how it links to other artifacts, and what review status it carries, but it does not automatically run a scored optimization loop around every note.

The most relevant design tradeoff is authority escalation. Autocontext can move from prose advice to symbolic validators, prompt mutations, and trained model artifacts, but the evidence for a particular memory's semantic truth is often the score trajectory rather than an explicit source citation. Commonplace should borrow the escalation ladder without relaxing its source and review expectations.

### Borrowable Ideas

**Context-selection telemetry.** Commonplace could record which notes, sources, indexes, warnings, and review findings were candidates, selected, trimmed, or omitted for a command. Ready for review bundles and validation-assisted workflows.

**Trace-derived maintenance records before silent edits.** Autocontext's pending/generated artifacts make learning auditable: a coach output, curator decision, mutation record, or distillation manifest can be inspected before stronger authority is granted. Ready for stale-note, duplicate-note, and review-warning workflows.

**Promotion from prose insight to symbolic gate.** A repeated review failure could first become a note, then a validator rule or review gate once evidence accumulates. Worth borrowing when a concrete warning recurs across several artifacts.

**Portable skill export.** Commonplace already has skills, but Autocontext's package/export path suggests a way to make a solved local workflow portable without making the exported skill the canonical source. Useful when a KB workflow should be handed to another agent environment.

**Do not borrow score-only truth.** Autocontext can accept knowledge because downstream score improved. Commonplace library artifacts need explicit lineage, citations, and review because their use outlives the original benchmark.

## Write side

**Write agency:** `manual` `automatic` — Operators can author scenarios, policies, feedback, packages, hooks, and imported traces; the system automatically writes run artifacts, SQLite rows, role outputs, playbooks, hints, lessons, skill files, dead ends, context-selection decisions, compaction ledgers, tool and validator files, mutation records, datasets, and training/model artifacts.

**Curation operations:** `consolidate` `dedup` `synthesize` `invalidate` `promote` — Coach and curator flows synthesize playbooks, hints, and lessons; curator consolidation deduplicates and caps lessons; playbook guards reject destructive shrinkage; rollback paths record dead ends; hint managers rank and rotate hints; mutation gates promote approved prompt/context/tool/completion changes into active harness state.

### Trace-learning

**Trace source:** `session-logs` `tool-traces` `event-streams` `trajectories` — Autocontext consumes generation records, role outputs, scores, matches, replay JSON, staged validation results, runtime-session prompt/tool/command events, production traces, feedback rows, context-selection telemetry, and compaction events.

**Extraction.** Extraction is a mixed human/LLM/system loop. Coaches extract replacement playbooks, operational lessons, and competitor hints from prior context; curators judge or merge playbook changes and consolidate lessons; deterministic gates check marker presence, shrinkage, mutation shape, validator syntax, retention/redaction policy, and dataset curation rules. The oracle is usually downstream score plus role/curator judgment, with deterministic checks around artifact shape and safety.

**Learning scope:** `per-project` `cross-task` — Scenario knowledge is rooted in a project/workspace and usually scenario-scoped, but exported skills, packages, production-trace datasets, training outputs, and model registry artifacts can carry lessons across tasks or runtimes.

**Learning timing:** `online` `staged` — Playbooks, hints, role outputs, telemetry, dead ends, and context-selection records update during runs; production-trace ingest, distillation, exports, and training are staged workflows.

**Distilled form:** `prose` `symbolic` `parametric` — Distillation outputs include Markdown playbooks/skills/reports, JSON/JSONL records, validators, tools, mutation specs, manifests, datasets, and optional model checkpoints.

Autocontext strengthens the trace-learning survey's claim that learning can be useful before fine-tuning: most behavior change comes from prose and symbolic artifacts re-entering prompts or gates. It also shows the governance hazard: fast trace-to-playbook learning needs explicit provenance if the result is meant to become durable knowledge rather than run-local optimization state.

## Read-back

**Read-back:** `both` — Agents and operators can pull retained knowledge through CLI/MCP/API/search/export readers, while the generation loop automatically injects scenario-scoped playbook, lessons, hints, analyses, tools, trajectories, dead ends, reports, notebooks, and attribution context into role prompts.

**Read-back signal:** `coarse` `identifier` `inferred / lexical` — Prompt assembly pushes a fixed set of knowledge components for the current scenario/run/generation, which is coarse within that selected scenario but targeted by identifiers such as scenario name, run id, generation, role, component name, skill name, and cwd. MCP strategy search is lexical keyword search over solved-scenario fields rather than embeddings or LLM judgment ([autocontext/src/autocontext/knowledge/search.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/knowledge/search.py), [autocontext/src/autocontext/session/runtime_context.py](https://github.com/greyhaven-ai/autocontext/blob/d381f21e17e405885aab4ff3a4e6475402bae8db/autocontext/src/autocontext/session/runtime_context.py)).

**Faithfulness tested:** `no` — Autocontext records selected context, score trajectories, component credit estimates, and downstream evaluation results, but the inspected code does not run a with/without ablation that proves a specific injected memory artifact changed the model's behavior.

The main push injection point is prompt assembly before role invocation. `build_prompt_bundle` assembles the current playbook and related components into competitor, analyst, coach, and architect prompts; runtime context assembly separately layers system policy, repo instructions, role instructions, scenario context, knowledge, runtime skills, tool affordances, and session history. After a turn, writes such as role-output capture, compaction, playbook updates, and metrics persistence are maintenance, not read-back.

Selection complexity is controlled by component boundaries, semantic compaction, budget trimming, role-scoped components, protected hints/dead ends, manifest-first skill discovery, and lexical search. It is not a vector store or learned retriever in the inspected code. Effective precision, context dilution, and whether the receiving model obeys the injected memory remain runtime-quality questions.

Other consumers matter. Human operators inspect run status, reports, trace timelines, context-selection reports, and exported packages. Curators consume playbooks and analyses. Training and distillation pipelines consume traces and datasets. Validators and mutation gates consume symbolic artifacts with stronger authority than ordinary prose memory.

## Curiosity Pass

Autocontext's strongest memory mechanism is not the production-trace SDK or optional local training; it is the repeated score-conditioned production of mundane artifacts: playbooks, hints, dead ends, tools, validators, and prompt mutations.

The system is unusually explicit about context efficiency for a learning harness. Component caps, compaction entries, selection telemetry, and role-scoped context make budget decisions reviewable, even though the final policy is still simple deterministic trimming.

"Learning" spans very different authority levels. A hint rotated by impact score, a curator-merged playbook, an approved harness mutation, and a fine-tuned checkpoint should not be treated as the same kind of memory merely because each came from traces.

The most fragile layer is prose lineage. Scores can show that a run improved after a change, but unless the coach or curator writes evidence into the lesson, a later reader cannot always tell which trace event justified the claim.

## What to Watch

- Whether context-selection telemetry grows into a true faithfulness test with controlled prompt ablations; that would change the read-back trust story.
- Whether generated lessons and playbooks gain required source-event citations; that would make trace-derived prose more portable outside a single scenario loop.
- Whether approved harness mutations become richer policy objects with invalidation and rollback metadata; that would strengthen the promotion path from advice to system-definition artifact.
- Whether production-trace distillation becomes the dominant learning route or remains a secondary export/training workflow behind prompt-level playbooks and validators.
- Whether embeddings or LLM relevance judgments enter strategy search or prompt context selection; that would change the read-back signal classification.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes Autocontext's retained run/knowledge artifacts from the prompt, MCP, API, and export paths that serve them.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - supports separating playbooks, run traces, generated tools, validators, mutations, datasets, and model artifacts by substrate, form, lineage, and authority.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - frames Autocontext's score-conditioned coach/curator/dataset/training loops.
- [Context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - frames Autocontext's component budgets, compaction, and selection telemetry.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies generated validators, prompt mutations, context policies, exported skills, and trained-model surfaces.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies playbooks, analyses, traces, reports, hints, and exported packages when they serve as evidence or advice.
