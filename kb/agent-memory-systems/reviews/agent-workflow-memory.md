---
description: "Workflow-memory system for web agents that distils successful trajectories into reusable prompt workflows for WebArena and Mind2Web"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-27"
---

# Agent Workflow Memory

Agent Workflow Memory is a research implementation by Zhiruo Wang and collaborators for web-navigation agents. It treats recurring task subroutines as memory: successful or annotated trajectories are abstracted into workflow text files, and those files are injected into later agent prompts on WebArena and Mind2Web. The codebase is benchmark-oriented rather than a general memory platform: it has scripts for two environments, prompt templates for workflow induction, trajectory evaluation helpers, and plain-text workflow artifacts.

**Repository:** https://github.com/zorazrw/agent-workflow-memory

**Reviewed commit:** [8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1](https://github.com/zorazrw/agent-workflow-memory/commit/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1)

## Core Ideas

**Workflow memory is prompt text, not a database.** The durable memory unit is a website-specific `.txt` workflow file such as WebArena's `workflow/shopping.txt` or `workflow/gitlab.txt`. Mind2Web reads the whole workflow file into a user-message exemplar before acting, then adds sampled concrete examples from `data/memory/exemplars.json`; WebArena appends the workflow file directly to the system message when `workflow_path` is set. This makes memory easy to inspect and edit, but gives it no schema, provenance fields, status, or lifecycle beyond file replacement. Sources: [mind2web/memory.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/memory.py), [webarena/agents/legacy/agent.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/agents/legacy/agent.py).

**Induction abstracts trajectories into reusable subroutines.** The induction prompts ask an LLM to find repeated action subsets across web tasks and represent non-fixed values as variables. Mind2Web offline induction formats annotated training examples and writes filtered workflow text; online induction parses prior result JSON into environment/action steps and rewrites the workflow file from those past experiences. Sources: [mind2web/prompt/instruction_action.txt](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/prompt/instruction_action.txt), [mind2web/offline_induction.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/offline_induction.py), [mind2web/online_induction.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/online_induction.py).

**WebArena uses a closed loop around successful trajectories.** The WebArena path runs an agent, evaluates the generated trajectory with either ground-truth reward or an auto-evaluator, extracts thought/action blocks from logs, deduplicates by template and abstract action sequence, then writes a workflow file. A second induction mode asks an LLM to summarize selected successful examples into abstract workflows. Sources: [webarena/README.md](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/README.md), [webarena/autoeval/evaluate_trajectory.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/autoeval/evaluate_trajectory.py), [webarena/induce_rule.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_rule.py), [webarena/induce_prompt.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_prompt.py).

**Retrieval exists, but the main path is coarse-grained loading.** Mind2Web includes a FAISS-based workflow retriever that embeds workflow names and docstrings, selects top workflows for a website's test queries, and can save a local vector index. The main acting path, however, loads a specified workflow file plus sampled concrete examples; the online pipeline rewrites one workflow path per website rather than maintaining a query-addressable memory store. Sources: [mind2web/workflow/retrieve.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/workflow/retrieve.py), [mind2web/run_mind2web.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/run_mind2web.py), [mind2web/pipeline.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/pipeline.py).

**Evaluation is benchmark-specific.** Mind2Web computes element accuracy, action F1, step success, and full task success while logging full conversations. WebArena can use ground-truth reward or an LLM auto-evaluator over trajectory text and screenshots. These are useful task oracles, but they do not evaluate the workflow artifact itself for correctness, scope, redundancy, or drift. Sources: [mind2web/memory.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/memory.py), [webarena/autoeval/evaluator.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/autoeval/evaluator.py).

## Comparison with Our System

Agent Workflow Memory and commonplace share the same high-level bet that agent memory should change future behavior through explicit artifacts. The difference is the artifact contract. AWM's workflow files are operational prompt payloads: they are meant to be read by an acting agent before a similar task. Commonplace notes are typed knowledge artifacts: they are meant to be navigated, linked, reviewed, validated, and reused across future work.

AWM is stronger where the task loop has a crisp benchmark oracle. WebArena reward, auto-eval status, and Mind2Web step metrics give the system a direct signal for which trajectories are worth learning from. Commonplace has weaker oracles because its outputs are methodology claims and operational conventions, not web-task success/failure.

Commonplace is stronger on evidence and lifecycle. AWM does not preserve per-workflow source provenance in the workflow file, does not record which trajectories supported a workflow, does not model supersession, and does not distinguish candidate, accepted, stale, and deprecated workflow units. The workflow text can become useful quickly, but a later agent cannot audit why it should trust a specific routine without re-reading result directories.

The systems also differ on activation. AWM activates by benchmark/site scope: provide the workflow path for the current website, optionally retrieve or sample a small number of exemplars, then run. Commonplace activates through typed files, indexes, backlinks, and instruction loading rules; it is less automatic but more composable across domains.

## Borrowable Ideas

**Trajectory-to-workflow distillation.** Commonplace could use the same pattern for high-repetition operator workflows: collect several successful task traces, induce a short procedural candidate, then review it into an instruction or skill. Ready when the source traces have a clear success oracle; premature for open-ended note-writing where success is mostly judgment.

**Template and action-sequence deduplication.** WebArena's two-stage deduplication by intent template and abstract action sequence is a practical filter before asking an LLM to summarize examples. In commonplace this maps to review or ingest traces: group by task shape and action skeleton before distilling a reusable procedure. Ready as a lightweight pre-processing idea, not as a new KB feature yet.

**Workflow files as disposable prompt payloads.** AWM shows the value of keeping the acting memory as plain text even when generated by an LLM. For commonplace, this supports generated context bundles and workshop handoffs as derived artifacts, provided source-of-truth notes remain elsewhere. Ready now as a design constraint for generated views.

**Benchmark-specific learning loops.** The online Mind2Web and WebArena loops are useful reminders that trace-derived learning is easiest when the environment supplies task boundaries and measurable outcomes. Commonplace should borrow this only for bounded subproblems such as validation repair, review triage, or command-selection heuristics, not for global KB learning.

## Trace-derived learning placement

**Trace source.** AWM consumes web-task trajectories: Mind2Web annotated examples and model result JSON, plus WebArena experiment logs, action histories, screenshots, summary rewards, and optional auto-evaluation results. Trigger boundaries are per website and per benchmark task range, with online Mind2Web inducing every `induce_steps` examples and WebArena updating after each task in the pipeline. Sources: [mind2web/pipeline.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/pipeline.py), [webarena/pipeline.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/pipeline.py).

**Extraction.** Extraction is LLM-mediated for abstract workflows and script-mediated for filtering. The scripts parse trajectory blocks, remove invalid or unhelpful actions, deduplicate by templates or abstract action sequences, and then either write concrete examples or ask an LLM to summarize common workflows. The oracle is benchmark-specific: ground-truth labels and candidate ranks for Mind2Web, ground-truth reward or an LLM auto-evaluator for WebArena.

**Representational form.** The distilled substrate is prose plus lightweight action syntax in plain text workflow files. There is also an optional FAISS index for retrieval over workflow names/docstrings, but the behavior-changing artifact is still prompt text, not vector state.

**Behavioral authority.** The workflows are system-definition artifacts rather than passive knowledge. Reading them changes the acting agent's policy for the next web task because they are injected into the system message or exemplar context before action selection.

**Scope.** Scope is website or benchmark split local. The code expects the operator to match workflow paths to websites and does not implement cross-site promotion, workflow ownership metadata, or general-purpose memory governance.

**Timing.** The repository supports both offline induction from training examples and online staged induction from earlier agent experiences. It is not continuous in-agent memory consolidation; the pipeline runs scripts that rewrite workflow files between task batches.

**Survey placement.** On the [trace-derived learning survey axes](../trace-derived-learning-techniques-in-related-systems.md), AWM is a clear trajectory-ingestion system with prose/symbolic prompt artifacts as the promotion target. It strengthens the survey claim that trace-derived learning becomes tractable when traces have tight task boundaries and an external oracle. It also splits "agent memory" from "memory store": AWM's memory is a behavior-shaping prompt artifact, while durable evidence remains in benchmark logs and result directories.

## Curiosity Pass

**The name overstates the generality.** "Agent Workflow Memory" sounds like a reusable memory architecture, but the implementation is mostly two benchmark pipelines plus workflow text files. That is not a flaw for the paper's goals, but it matters for transfer: the system demonstrates a learning loop more than it ships a memory substrate.

**The workflow file is both the API and the database.** This is refreshingly simple, and it probably helps benchmark iteration. The cost is that overwrite semantics are blunt: a generated workflow file has no internal identities for individual routines, no evidence pointers, no retirement path, and no merge policy.

**The WebArena path appears somewhat stale.** `webarena/run.py` marks the demo runner as deprecated, and `webarena/pipeline.py` calls `run.py` with `--task` while the parser defines `--task_name`. The conceptual loop is clear, but the checked-in runner scripts may need operator repair before direct reuse. Sources: [webarena/run.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/run.py), [webarena/pipeline.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/pipeline.py).

**Semantic retrieval may be an experimental side path.** The retriever builds FAISS memory over workflow summaries, but the primary Mind2Web acting script samples exemplars and loads one workflow path. If the project evolves, the question is whether retrieval becomes central or stays an ablation/selection utility.

## What to Watch

- Whether workflows gain internal structure: stable ids, source trajectory references, confidence, scope tags, or supersession.
- Whether online induction moves from overwriting a website workflow file to accumulating and curating individual workflow units.
- Whether retrieval becomes part of the main acting path rather than a separate workflow-selection script.
- Whether the benchmark loops are maintained against current BrowserGym, LangChain, and OpenAI client versions.
- Whether future work separates memory evidence, memory artifact, and prompt payload instead of storing everything as result logs plus injected text.

Relevant Notes:

- [distillation](../../notes/definitions/distillation.md) - exemplifies: AWM compresses trajectories into reusable workflow text, a direct case of directed context compression.
- [deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - exemplifies: online induction updates behavior from prior task experiences without changing model weights.
- [automating KB learning is an open problem](../../notes/automating-kb-learning-is-an-open-problem.md) - contrasts: AWM automates learning only where benchmark traces and external oracles make extraction tractable.
- [files not database](../../notes/files-not-database.md) - complicates: workflow text files are the behavior-changing memory, while logs and metrics remain in benchmark result directories.
