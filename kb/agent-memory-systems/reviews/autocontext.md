---
description: "Autocontext review: iterative agent harness with run traces, scenario-scoped playbooks, lessons, mutations, context assembly, datasets, and distilled models"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# Autocontext

Autocontext, from Grey Haven AI's `greyhaven-ai/autocontext` repository, is an agent evaluation and improvement harness rather than a standalone memory database. A run executes a scenario or task through repeated generations, records the trace, scores the outputs, then carries selected knowledge forward as playbooks, hints, lessons, tools, harness mutations, context-selection records, exported packages, datasets, and optional local model checkpoints. The memory system is the control plane around that loop: it decides which retained artifacts enter future prompts, which traces can become durable knowledge, and which generated artifacts are strong enough to influence later agents.

**Repository:** https://github.com/greyhaven-ai/autocontext

**Reviewed commit:** [231be0c3f508d9512f6cca3658dd073df3438863](https://github.com/greyhaven-ai/autocontext/commit/231be0c3f508d9512f6cca3658dd073df3438863)

**Last checked:** 2026-06-01

## Core Ideas

**The canonical loop is run -> trace -> retained knowledge -> next run.** The README describes `runs/<run_id>/` traces and per-generation artifacts alongside `knowledge/<scenario>/playbook.md`, `hints.md`, and generated tools; the implementation backs that with SQLite run/generation/match/agent-output tables, filesystem artifacts, and per-scenario knowledge stores ([README.md](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/README.md), [autocontext/src/autocontext/storage/sqlite_store.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/storage/sqlite_store.py), [autocontext/src/autocontext/storage/artifacts.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/storage/artifacts.py)).

**Memory is assembled as prompt context, not hidden state.** Python and TypeScript both expose the same runtime context layer order: system policy, repo instructions, role instructions, scenario context, knowledge, runtime skills, tool affordances, and session history. The assembly APIs preserve provenance for repo instructions, knowledge components, skill manifests, tools, and session-history entries ([autocontext/src/autocontext/session/runtime_context.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/session/runtime_context.py), [ts/src/session/runtime-context.ts](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/ts/src/session/runtime-context.ts), [docs/concept-model.md](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/docs/concept-model.md)).

**Prompt assembly has an engineered selection and budget layer.** `build_prompt_bundle` compacts long-lived components, applies token caps, records selected prompt components, and emits role-specific prompts for competitor, analyst, coach, and architect. Hints and known dead ends are protected; playbooks, lessons, analysis, trajectories, reports, and evidence manifests can be compacted or trimmed before they reach the model ([autocontext/src/autocontext/prompts/templates.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/prompts/templates.py), [autocontext/src/autocontext/prompts/context_budget.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/prompts/context_budget.py), [autocontext/src/autocontext/knowledge/context_selection.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/knowledge/context_selection.py)).

**The trace-derived artifacts are plural.** Coach output can replace playbooks, emit operational lessons, and refresh competitor hints. Analyst ratings, hint feedback, credit attribution, dead ends, progress reports, session reports, replay narratives, and mutation logs are persisted and later injected into role prompts when relevant to the scenario and generation ([autocontext/src/autocontext/loop/stages.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/loop/stages.py), [autocontext/src/autocontext/loop/stage_helpers/context_loaders.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/loop/stage_helpers/context_loaders.py), [autocontext/src/autocontext/knowledge/lessons.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/knowledge/lessons.py), [autocontext/src/autocontext/knowledge/mutation_log.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/knowledge/mutation_log.py)).

**Architect outputs can mutate the harness itself.** The architect prompt can propose tools, validators, and typed harness mutations. Mutations are parsed from a delimited JSON block, gated for minimal structural validity, persisted as versioned `mutations.json`, and applied to later prompts as role prompt fragments, context policies, completion checks, or tool instructions ([autocontext/src/autocontext/harness/mutations/parser.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/harness/mutations/parser.py), [autocontext/src/autocontext/harness/mutations/gate.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/harness/mutations/gate.py), [autocontext/src/autocontext/loop/stage_helpers/harness_mutations.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/loop/stage_helpers/harness_mutations.py)).

**Runtime traces and production traces are separate evidence channels.** Run-scoped runtime sessions record prompts, assistant messages, shell/tool calls, child-task lineage, and compaction events in SQLite. Production traces are a customer-facing contract and SDK for application LLM calls, with TypeScript ingestion, dataset generation, retention, and export surfaces ([autocontext/src/autocontext/session/runtime_events.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/session/runtime_events.py), [autocontext/src/autocontext/session/runtime_session_recording.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/session/runtime_session_recording.py), [autocontext/src/autocontext/production_traces/emit.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/production_traces/emit.py), [ts/src/production-traces/dataset/pipeline.ts](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/ts/src/production-traces/dataset/pipeline.ts)).

**Distillation can cross into distributed-parametric artifacts.** Strategy-level training export reads run generations, competitor outputs, playbook, hints, and score trajectory into training records; the autoresearch training loop writes model bundles, and the model registry records checkpoint paths, activation state, runtime types, training metrics, and provenance ([autocontext/src/autocontext/training/export.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/training/export.py), [autocontext/src/autocontext/training/autoresearch/train.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/training/autoresearch/train.py), [autocontext/src/autocontext/training/model_registry.py](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/autocontext/src/autocontext/training/model_registry.py)).

## Artifact analysis

- **Storage substrate:** `sqlite` — SQLite tables plus per-run filesystem directories under `runs/`
- **Representational form:** `symbolic` — Symbolic rows and JSON/markdown artifacts containing strategies, scores, validation results, agent outputs, replays, reports, context-selection decisions, and compaction ledgers

**Run, generation, match, and agent-output records.** Storage substrate: SQLite tables plus per-run filesystem directories under `runs/`. Representational form: symbolic rows and JSON/markdown artifacts containing strategies, scores, validation results, agent outputs, replays, reports, context-selection decisions, and compaction ledgers. Lineage: generated from scenario execution, provider calls, verifier results, and prompt assembly during a concrete run. Behavioral authority: knowledge artifacts when inspected as evidence; system-definition artifacts when later export, training, analysis, context selection, or promotion workflows consume them to shape future prompts or models.

**Scenario knowledge files.** Storage substrate: files under `knowledge/<scenario>/`, including `playbook.md`, `hints.md`, `hint_state.json`, `lessons.json`, `dead_ends.md`, `research_protocol.md`, `progress.json`, `mutation_log.jsonl`, generated tools, generated harness validators, and version archives. Representational form: mixed prose markdown, JSON metadata, Python code, and append-only JSONL. Lineage: authored seeds plus coach, analyst, architect, evaluator, and run-output derivations; playbooks and mutations are versioned, while lessons carry generation, score, schema, upstream signature, operation type, supersession, and validation metadata. Behavioral authority: system-definition artifacts when inserted into role prompts, used as validators, or loaded as generated tools; knowledge artifacts when used as audit evidence.

**Prompt and runtime context assembly artifacts.** Storage substrate: in-memory bundles at execution time, context-selection JSON files under a run, compaction ledgers under `runs/<run_id>/`, and shared Python/TypeScript assembly code. Representational form: symbolic layer metadata plus prose prompt components. Lineage: assembled from repo instructions, role templates, scenario/task inputs, selected knowledge, skill manifests, tool affordances, and runtime-session history; component hashes and selection metrics record what survived assembly. Behavioral authority: system-definition artifacts because they decide which retained material reaches each role and with what prompt position and budget priority.

**Harness mutations.** Storage substrate: versioned JSON under `knowledge/<scenario>/mutations.json` plus `mutation_versions/` archives and mutation-log entries. Representational form: symbolic mutation specs with prose content. Lineage: extracted from architect output after a generation, structurally gated, deduplicated, and stamped with generation/run metadata. Behavioral authority: system-definition artifacts with direct prompt authority: prompt fragments alter role prompts, context policies are injected into experiment-log context, tool instructions alter tool context, and completion checks are appended to competitor prompts.

**Runtime-session event logs and production traces.** Storage substrate: runtime-session SQLite tables for provider-backed runs, production trace JSONL under `.autocontext/production-traces/`, and generated dataset directories under `.autocontext/datasets/`. Representational form: symbolic event records with prompt/response/tool previews, production-trace JSON contract documents, dataset manifests, and split JSONL rows. Lineage: runtime sessions come from provider calls and workspace/tool activity; production traces come from instrumented customer applications and are ingested, redacted, clustered, selected, split, and manifested. Behavioral authority: mostly knowledge artifacts as replay/audit/evaluation evidence, becoming system-definition artifacts when dataset builders, training loops, or memory-pack compilers select them for future evaluation or model training.

**Operational memory packs.** Storage substrate: TypeScript control-plane objects and whatever host registry persists them. Representational form: symbolic pack/finding records plus prose reusable behavior. Lineage: packaged findings cite evidence refs and pass integrity, status, leakage, target-family, risk, and quarantine checks before prompt rendering. Behavioral authority: system-definition artifacts when `compileOperationalMemoryContext` renders selected findings into an "Operational memory to apply" prompt block for a target family ([ts/src/control-plane/memory-packs/index.ts](https://github.com/greyhaven-ai/autocontext/blob/231be0c3f508d9512f6cca3658dd073df3438863/ts/src/control-plane/memory-packs/index.ts)).

**Distilled model artifacts.** Storage substrate: model checkpoint bundles, tokenizer/config files, published artifact JSON, and registry records under `model_registry`. Representational form: distributed-parametric weights plus symbolic metadata. Lineage: exported training records or trace-derived datasets feed MLX/CUDA training; registry records preserve run id, scenario, backend, checkpoint path, metrics, data stats, runtime slots, and activation state. Behavioral authority: system-definition artifacts when activated and resolved as a provider/runtime model; candidate or disabled records are knowledge artifacts until promotion.

The promotion path is unusually broad: raw run and production traces become evidence; coach/architect/analysis stages turn evidence into prose, JSON, code, and package artifacts; context assembly pushes selected artifacts into later prompts; training and promotion can further distill selected traces into model checkpoints. The weak point is not lack of retention. It is authority management: several artifacts can become prompt-active after light structural checks, while quality, specificity, and causal usefulness still require runtime evaluation.

### Borrowable Ideas

**Make context assembly an inspectable artifact.** Commonplace could record which notes, instructions, indexes, review findings, and generated summaries were candidates for a task context and which were selected. Ready where prompt-pack generation already exists; avoid adding machinery for ordinary manual `rg` navigation.

**Separate trace evidence from prompt-active knowledge.** Autocontext keeps run records, runtime sessions, playbooks, lessons, hints, and mutations as distinct surfaces. Commonplace should preserve the same distinction when turning review traces or agent failures into instructions: raw logs are evidence, not rules. Ready as a workshop-to-library convention.

**Treat prompt mutations as typed candidates.** Prompt fragments, context policies, completion checks, and tool instructions are more reviewable than one undifferentiated "memory" blob. Commonplace could use typed candidate changes for high-impact agent instructions. Needs stronger gates before becoming durable repo instruction.

**Carry applicability metadata on lessons.** Lesson generation, score, schema version, source signature, supersession, and validation generation are directly useful for deciding when a lesson should stop being loaded. Ready for trace-derived operational lessons; probably overbuilt for ordinary authored notes.

**Use target-family memory packs as a quality boundary.** Operational memory packs select findings by status, integrity, leakage risk, target family, risk tolerance, quarantine, and capacity. Commonplace could adapt this for generated context bundles that must not leak task answers or stale strategy snippets. Needs a concrete bundle consumer.

**Keep model distillation behind activation state.** Autocontext treats checkpoints as candidates before activation. Commonplace does not need local model training now, but the candidate/shadow/active lifecycle is the right pattern for any learned retriever, ranker, or summarizer that might later influence agent context.

## Comparison with Our System

| Dimension | Autocontext | Commonplace |
|---|---|---|
| Primary purpose | Improve agent/task performance through iterative runs, evaluation, retained knowledge, and optional training | Maintain a typed methodology KB for agents and maintainers |
| Canonical retained unit | Run artifacts, scenario knowledge, prompt components, mutations, packages, datasets, checkpoints | Git-tracked notes, reviews, instructions, type specs, indexes, reports |
| Learning loop | Run/evaluate/analyze/coach/architect/curate, then push selected artifacts forward | Source-grounded writing, validation, semantic review, workshop promotion |
| Read-back | Engineered push into role prompts and runtime context; also pull through CLI/MCP/status/read APIs | Mostly pull through search/indexes/links, with instructions and generated context where explicitly configured |
| Governance | Score gates, prompt budgets, structural mutation gates, versioned playbooks/mutations, context-selection telemetry, model activation states | Collection contracts, schemas, validation, curated links, git history, semantic review gates |

Autocontext is closer to an experimental control plane than to a library-style KB. Commonplace's strength is artifact reviewability: source-pinned citations, type contracts, deterministic validation, and git-native change history. Autocontext's strength is the closed loop from execution trace to prompt-active artifact. It can learn operational behavior without a maintainer explicitly writing every instruction, but that also means some behavior-shaping text crosses from "generated suggestion" to "future prompt material" with less human review than Commonplace would normally allow.

The two systems converge on an important design claim: retained state matters only when its consumption path is explicit. Autocontext makes this concrete by tracking context layers, context budgets, selected components, and prompt mutation application. Commonplace is more conservative: notes can be excellent knowledge artifacts while remaining pull-only until an agent searches, follows links, or receives an instruction to load them.

**Read-back:** `both` — With engineered push. The acting role receives scenario-scoped playbooks, hints, lessons, dead ends, reports, active harness mutations, runtime skills, and session history through prompt/context assembly; operators and agents can also pull run status, playbooks, runtime sessions, datasets, and knowledge through CLI, HTTP, MCP, and SDK surfaces

## Trace-derived learning placement

**Trace source.** Autocontext qualifies as trace-derived learning. Qualifying traces include run generations, match results, validation errors, agent role outputs, score trajectories, replay narratives, runtime-session prompt/tool/child-task events, compaction events, production traces, Hermes curator reports, and task/mission artifacts.

**Extraction.** Extraction is staged and heterogeneous. The coach converts generation outcomes into replacement playbooks, operational lessons, and competitor hints. The analyst and curator provide analysis, ratings, and consolidation. The architect proposes tools, validators, and harness mutations. Context-selection code records which prompt components survived budget/compaction. Production trace tooling ingests and clusters application traces into datasets. Training exporters turn run histories plus playbook/hint context into supervised records.

**Scope and timing.** Scope is scenario-, run-, task-, target-family-, and runtime-session-aware. Most learning happens between generations or between runs; runtime-session logging is online during provider calls; production-trace dataset building and local model training are offline or staged control-plane workflows.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), Autocontext spans several families: trace-to-prose procedure, trace-to-symbolic harness mutation, trace-to-dataset, trace-to-model checkpoint, and trace-to-context-selection telemetry. It strengthens the survey's split between evidence retention and behavior-shaping distillation: raw traces are not the memory that acts; selected playbooks, lessons, hints, mutations, prompt bundles, datasets, and activated checkpoints are.

## Read-back placement

**Direction.** Autocontext uses push and pull. Push is the important memory path for acting agents: the harness assembles retained knowledge into role prompts before the role acts. Pull exists through status, replay, runtime-session, knowledge, production-trace, and MCP/API inspection surfaces.

**Trigger and relevance signal.** The main trigger is generation or runtime-context assembly for a scenario/task. Relevance is structural rather than semantic in the core path: scenario name, generation, role, active mutation status, lesson applicability/staleness, hint volume policy, knowledge include/exclude lists, target-family filtering for memory packs, and component budget policy. Precision/recall of those selections is not verified by static code.

**Timing relative to action.** Prompt memory is assembled before competitor, analyst, coach, or architect generation, so it can change the next action. Runtime-session and compaction logs are written during or after execution; they affect future behavior only after a later assembly, analysis, dataset, or training path consumes them.

**Selection, scope, and complexity.** The strongest controls are scenario scoping, role-specific prompt construction, semantic compaction, component token caps, protected hints/dead ends, mutation type checks, context-selection telemetry, memory-pack capacity limits, and dataset selection rules. These reduce volume and make selection observable, but they do not prove that loaded memory is behaviorally faithful or causally useful.

**Authority at consumption.** Playbooks, hints, lessons, dead ends, tool instructions, completion checks, and context policies are advisory prose/system prompt material, but they have system-definition force because the harness places them in role prompts. Generated validators and tools have stronger symbolic authority. Activated model checkpoints have distributed-parametric authority through provider/model resolution. Run logs and production traces remain knowledge artifacts until selected by one of those consumption paths.

**Faithfulness.** Autocontext evaluates run outcomes and has ablation knobs and benchmark surfaces, but I did not find a per-memory faithfulness test like "this specific lesson fired and changed the next action." Context-selection metrics show what was loaded and compacted; they do not establish use by the model.

**Other consumers.** Operators inspect run reports, status, replay, context-selection reports, runtime-session timelines, production-trace datasets, and cockpit/API views. Those human/operator consumers are a separate surface from prompt push, not a second kind of agent read-back.

## Curiosity Pass

**The name hides a broad control plane.** Autocontext is not just automatic context injection. It includes scenario generation, scoring, role orchestration, production trace ingestion, dataset generation, training, model registry, MCP/API surfaces, Pi integration, and TypeScript/Python parity work.

**Some generated artifacts get prompt authority quickly.** Harness mutations are gated for non-empty content, type requirements, length, deduplication, and active status. That is useful but lighter than a semantic or empirical gate, especially for prompt fragments and context policies.

**The context-selection layer is more auditable than many memory systems.** It records candidates, selected components, token estimates, hashes, and budget telemetry. The missing piece is a stronger link from selected artifact to measured behavioral contribution.

**Operational memory packs are the most Commonplace-like abstraction.** They classify findings, evidence references, target families, risk, leakage, and integrity before rendering a bounded prompt. That looks more like a typed review artifact than ordinary prompt memory.

**The system has both readable and learned memory.** Playbooks, hints, lessons, mutations, and packages stay inspectable; model checkpoints intentionally leave the readable substrate. The registry/provenance layer is therefore essential, because the artifact's operative part is no longer directly readable.

## What to Watch

- Whether prompt-active harness mutations gain stronger semantic review, ablation, or rollback criteria before they persist across runs.
- Whether context-selection telemetry becomes a promotion gate rather than only an observability report.
- Whether operational memory packs become wired into the main run loop or remain a TypeScript control-plane capability.
- Whether Python and TypeScript parity keeps the same context-layer semantics as the control plane expands into campaigns, missions, and production traces.
- Whether production-trace datasets and distilled checkpoints get a fully auditable path from trace source to active runtime model.
- Whether per-artifact faithfulness tests appear for playbooks, lessons, hints, and mutations, not just aggregate run-score improvements.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: Autocontext spans trace-to-playbook, trace-to-mutation, trace-to-dataset, and trace-to-checkpoint learning.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: Autocontext requires separating run logs, scenario knowledge files, prompt bundles, mutations, datasets, and model artifacts by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Autocontext makes activation explicit through prompt/context assembly and context-selection records.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: Autocontext extracts future behavior from scored runs, traces, and curator/coach/architect outputs.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - aligns: runtime sessions and production traces remain evidence while compacted or distilled artifacts carry forward.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: active playbooks, hints, mutations, validators, context bundles, and model records can instruct, route, evaluate, or select future behavior.
