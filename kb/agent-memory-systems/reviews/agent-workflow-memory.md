---
description: "Agent Workflow Memory review: workflow text files induced from web-task traces, optional FAISS retrieval, and prompt-time workflow injection"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-04"
---

# Agent Workflow Memory

Agent Workflow Memory, from Zhiruo Wang's `zorazrw/agent-workflow-memory` repository, is a research implementation for web-navigation agents on WebArena and Mind2Web. It stores reusable website workflows as text files, induces those workflows from annotated examples or previous agent trajectories, and injects selected workflows into the acting agent's prompt.

**Repository:** https://github.com/zorazrw/agent-workflow-memory

**Reviewed commit:** [8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1](https://github.com/zorazrw/agent-workflow-memory/commit/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1)

**Last checked:** 2026-06-04

## Core Ideas

**The memory unit is a workflow, not a fact or document.** The README defines a workflow as a common sub-routine with example-specific context abstracted out, and the prompt templates ask the induction model to extract reusable action subsets with variable placeholders and at least two steps ([README.md](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/README.md), [webarena/prompt/instruction.txt](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/prompt/instruction.txt), [mind2web/prompt/instruction_action.txt](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/prompt/instruction_action.txt)). The retained material is therefore procedural: it changes future action selection by showing a recurrent path through a website or task family.

**Offline and online induction share the same write target.** The top-level README distinguishes offline induction from training examples and online induction from past experience ([README.md](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/README.md)). In Mind2Web, offline induction groups examples by domain/subdomain/website, formats action representations, prompts GPT, filters the generated workflows, and writes `workflow/{website}.txt`; online induction reads previous result JSON, turns each recorded step into environment/action pairs, prompts GPT, and overwrites the same workflow file ([mind2web/offline_induction.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/offline_induction.py), [mind2web/online_induction.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/online_induction.py), [mind2web/pipeline.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/pipeline.py)).

**WebArena uses evaluation-gated trajectory integration.** The WebArena path runs a task with a website workflow file, evaluates the generated trajectory, then induces updated memory from successful trajectories. `induce_rule.py` can select trajectories by ground-truth reward or model-based autoeval, deduplicate by template id and abstract action trajectory, optionally require manual acceptance, and write concrete examples into a workflow file; `induce_prompt.py` instead prompts GPT to summarize selected successful trajectories into workflows ([webarena/README.md](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/README.md), [webarena/pipeline.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/pipeline.py), [webarena/induce_rule.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_rule.py), [webarena/induce_prompt.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_prompt.py), [webarena/autoeval/evaluate_trajectory.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/autoeval/evaluate_trajectory.py)).

**Read-back is mostly prompt injection from a selected file.** WebArena appends `workflow_path` contents to the system prompt before each action, while Mind2Web loads workflow text into exemplar messages and then appends as many exemplars as fit the model token budget ([webarena/agents/legacy/agent.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/agents/legacy/agent.py), [mind2web/memory.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/memory.py), [mind2web/run_mind2web.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/run_mind2web.py)). The agent does not search the memory at action time; the harness selects and loads it.

**Context efficiency is coarse but explicit.** The default path is bounded by website-scoped files, `retrieve_top_k` concrete examples, model token checks, and per-step observation truncation rather than a rich memory graph. Mind2Web also includes an optional FAISS/OpenAI-embedding retriever that ranks workflow blocks by workflow name and docstring against test-query text, then writes the top workflows to an output file for later injection ([mind2web/workflow/retrieve.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/workflow/retrieve.py)). Volume is controlled; complexity is not deeply managed because loaded workflows remain full procedural traces or summaries.

**The repository is an experiment harness, not a maintained memory product.** There is no durable schema, migration system, provenance ledger, review gate, or user-facing memory API. Trust comes from benchmark reward/autoeval filtering, manual inspection in one WebArena path, and the fact that workflow files stay inspectable as plain text.

## Artifact analysis

- **Storage substrate:** `files` `vector` — The central retained artifacts are workflow `.txt` files, result JSON/log directories, dataset/config files, and optional FAISS vector indexes over workflow blocks.
- **Representational form:** `prose` `symbolic` `parametric` — Workflows are prose-plus-action templates, trajectories/results are symbolic JSON/log records, and optional semantic retrieval uses embedding vectors.
- **Lineage:** `imported` `trace-extracted` `authored` — Offline Mind2Web workflows derive from imported annotated training examples; online Mind2Web and WebArena workflows derive from previous agent traces; WebArena rule induction can add manual acceptance.
- **Behavioral authority:** `knowledge` `instruction` `ranking` `learning` — Workflow files advise and instruct acting agents when injected, FAISS ranks workflow candidates, and traces/examples feed future workflow induction.

**Workflow text files.** Storage substrate: files under `workflow/` paths, including shipped WebArena examples such as `webarena/workflow/shopping.txt` and generated Mind2Web files named by website ([webarena/workflow/shopping.txt](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/workflow/shopping.txt), [mind2web/README.md](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/README.md)). Representational form: prose task descriptions, thought/action examples, and symbolic action calls or Mind2Web action lines. Lineage: authored examples, imported annotated examples, or generated summaries of successful trajectories. Behavioral authority: system-definition artifacts when appended to system prompts or exemplar messages, because they directly shape next action generation.

**Trajectory and evaluation records.** Storage substrate: WebArena `results/` directories with experiment logs, summary info, and autoeval JSON; Mind2Web result JSON written per task id under `results/{model}/{benchmark}/{website}/{suffix}` ([webarena/induce_rule.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_rule.py), [mind2web/memory.py](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/memory.py)). Representational form: symbolic JSON/log traces plus prose thoughts and outputs. Lineage: trace-extracted from agent runs, then filtered by reward, autoeval, website, task interval, or benchmark split. Behavioral authority: knowledge artifacts as evidence until induction scripts convert them into prompt-active workflow memory.

**Induction prompts and scripts.** Storage substrate: repo Python scripts and prompt text files in both benchmark directories. Representational form: symbolic code plus prose task instructions and one-shot examples. Lineage: authored by the repository. Behavioral authority: learning authority: they decide which examples are formatted, which outputs are filtered, how workflows are deduplicated, and where the resulting memory is written.

**Workflow retrieval index.** Storage substrate: optional FAISS local index saved by `mind2web/workflow/retrieve.py`. Representational form: parametric embeddings plus symbolic metadata ids. Lineage: derived from parsed workflow blocks and invalidated by changing workflow file content, embedding model, top-k policy, or retrieval input set. Behavioral authority: ranking and selection authority because it decides which workflow blocks are written to the output file that later enters the agent context.

**Prompt-assembly paths.** Storage substrate: in-memory message lists assembled during `run.py` or `run_mind2web.py`. Representational form: prose/system messages plus symbolic action-space instructions. Lineage: assembled from static agent prompts, current observation/history, workflow files, and selected exemplars. Behavioral authority: instruction and knowledge authority at consumption time; WebArena gives workflow text system-prompt adjacency, while Mind2Web gives it exemplar-message authority.

**Promotion path.** AWM's promotion path is trace/example -> formatted prompt evidence -> generated or selected workflow text -> website-scoped memory file -> injected prompt context. The system has light quality gates (reward/autoeval, template/action deduplication, optional manual inspection, token checks), but no review state or provenance-preserving workflow version history.

## Comparison with Our System

| Dimension | Agent Workflow Memory | Commonplace |
|---|---|---|
| Primary purpose | Improve web-navigation agents by carrying reusable workflows across tasks | Maintain a typed methodology KB for agents and maintainers |
| Main retained unit | Website workflow text file or selected workflow block | Git-tracked note, review, source snapshot, instruction, type spec, or index |
| Write path | LLM induction from examples/traces, rule selection, manual acceptance in one path | Source-grounded writing, validation, semantic review, curated links, replacement archives |
| Read-back | Harness-selected workflow text is pushed into the acting prompt | Mostly pull through search, indexes, links, and explicit instructions |
| Governance | Benchmark reward/autoeval, deduplication, optional manual acceptance, token checks | Collection contracts, schemas, deterministic validation, semantic gates, git history |

AWM is much narrower than Commonplace. Its memory is not a general knowledge substrate; it is a procedural cache for a specific agent/task family. That narrowness is also its strength. The retained artifact is close to the behavior it should change: a future web-navigation agent sees a reusable workflow before choosing the next action.

The main divergence is authority control. Commonplace treats artifacts as typed library objects and separates evidence, notes, instructions, and validation gates. AWM crosses from trace evidence to prompt-active instruction with relatively little intermediate governance. That is acceptable for a benchmark loop where success rates are the evaluation target, but it would be too coarse for durable methodology claims or repo-level agent rules.

**Read-back:** `push` — AWM's memory path is host-mediated prompt injection: selected workflow files or exemplar messages are loaded into the acting agent before it chooses actions, rather than retrieved by the agent through a deliberate memory tool.

### Borrowable Ideas

**Store reusable procedures at the action-template level.** A Commonplace analogue would be a typed operational-lesson artifact that records a repeated workflow with placeholders, source traces, and applicability conditions. Ready for tightly scoped agent operations; too narrow for ordinary theory notes.

**Keep trace-to-rule promotion visibly staged.** AWM's trajectory -> induced workflow -> injected prompt path is easy to understand. Commonplace could preserve the same staging for agent failures or successful review runs, but with explicit source citations, review status, and retirement rules. Ready as a workshop convention before any automatic write path.

**Use task-family scoping before semantic retrieval.** Website/domain/subdomain selection is crude, but it avoids loading a global memory pile. Commonplace should prefer known collection, type, workshop, and task identifiers before adding embedding retrieval. Ready now as routing discipline.

**Treat benchmark reward as a candidate filter, not proof of correctness.** AWM uses reward/autoeval to select traces for workflow induction. Commonplace can borrow that as a weak promotion signal for operational lessons, but it should not replace semantic review or source-grounding.

**Do not borrow overwrite-only workflow files.** AWM frequently writes the current workflow output to one path. Commonplace needs lineage, replacement archives, and reviewable invalidation when generated operational memory becomes durable.

## Write-side placement

**Write agency:** `automatic` `manual` — Offline scripts, online induction scripts, GPT calls, evaluation filters, retrievers, and pipelines write or overwrite workflow memory automatically, while WebArena rule induction can require manual acceptance before adding selected trajectories.

**Curation operations:** `consolidate` `dedup` `synthesize` `promote` — AWM consolidates many examples or trajectories into compact workflow text, deduplicates WebArena candidates by template and abstract action trajectory, synthesizes new workflow summaries with GPT, and promotes successful or selected traces into prompt-active workflow files.

### Trace-derived learning

**Trace source:** `session-logs` `trajectories` — WebArena experiment logs and Mind2Web result JSON supply the online trace evidence; offline Mind2Web uses annotated example trajectories.

**Learning scope:** `per-task` `per-project` `cross-task` — Traces are produced by individual tasks, scoped by website/domain/subdomain, and reused across later tasks in that website or task family.

**Learning timing:** `online` `offline` `staged` — Offline induction uses training examples before test inference, while online pipelines alternate between inference, evaluation or result capture, and workflow regeneration.

**Distilled form:** `prose` `symbolic` — Distilled workflows are natural-language procedural summaries plus action templates/calls; optional embeddings are a retrieval index over them, not the main learned artifact.

**Trace source.** AWM qualifies as trace-derived learning. WebArena parses `experiment.log` files into thoughts and action lists, filters by ground-truth reward or autoeval reward-model output, and then either writes concrete examples or asks GPT to summarize workflows. Mind2Web online induction reads previous result JSON, extracts the last user observation and model output for each step, and induces a workflow from those past experiences.

**Extraction.** The extraction oracle differs by path. Offline Mind2Web relies on ground-truth annotated examples and candidate-rank data. WebArena can use benchmark reward, model-based autoeval, template deduplication, abstract action deduplication, and optional manual acceptance. GPT is the abstraction engine for neural induction; rule induction can preserve concrete trajectories instead of summarizing them.

**Scope and timing.** The practical scope is website or domain/subdomain/website. Online Mind2Web runs inference over a slice of examples, then induces a new workflow file from accumulated results before later examples. WebArena's pipeline does the same loop around task execution, trajectory evaluation, and workflow update.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), AWM is a clean trace-to-procedure system. It strengthens the survey claim that raw traces and behavior-shaping artifacts must be separated: the logs/results are evidence, while the workflow file is the operative artifact that reaches the next prompt.

## Read-back placement

**Direction.** Push only, for retained workflow memory. The acting WebArena agent receives the workflow file through `workflow_path` appended to the system prompt; Mind2Web receives workflow text and selected concrete examples as prompt messages. The repository has a workflow retriever, but it writes a selected workflow file before inference rather than giving the acting agent a memory-search tool.

**Read-back signal:** `identifier` `inferred / embedding` — The normal selection signal is website/domain/subdomain or an explicit `workflow_path`; the optional Mind2Web retrieval path can select workflow blocks by embedding similarity to task text before writing the prompt-active file.

**Faithfulness tested:** `no` — The paper/repo reports benchmark improvements, but the code does not implement a per-fired-workflow ablation or post-action audit proving a particular loaded workflow changed behavior correctly.

**Targeting and signal.** The default read-back is instance-targeted by declared identifiers: website name, domain/subdomain/website tags, benchmark split, configured result range, and the CLI-supplied `workflow_path`. Optional Mind2Web retrieval adds inferred embedding selection over workflow name and docstring, but that selection is still outside the acting loop.

**Selection, scope, and complexity.** Scope controls are simple: one workflow file per website, domain/subdomain filtering for concrete examples, `retrieve_top_k` exemplars, FAISS `top_k` in the retrieval utility, per-step top-k HTML candidates, and token-limit checks that stop adding exemplars once the prompt would exceed the model budget. This bounds volume, but loaded workflows can still be long concrete trajectories, so complexity is only partly constrained.

**Authority at consumption.** WebArena workflow memory has strong prompt authority because it is appended to the system message before action generation. Mind2Web workflow memory has exemplar authority: it is loaded as user-message demonstrations ahead of the current task trajectory. Neither path is an enforcement gate; the model may ignore or misuse the workflow.

**Faithfulness.** AWM evaluates task success, element accuracy, action F1, and step success, and WebArena uses autoeval or ground-truth reward as write-side filters. Those metrics show aggregate performance and trace eligibility, not whether a specific workflow fired, was used, or caused the next action.

**Other consumers.** The human experimenter consumes workflow files, result logs, and induced outputs when running pipelines or inspecting candidates. That adoption surface is useful for research, but it is not a separate agent read-back path.

## Curiosity Pass

**The "memory" is deliberately small.** AWM does not try to remember arbitrary user facts or conversation history. It remembers action procedures for websites, which makes the write/read contract unusually direct.

**Some paths preserve examples instead of abstracting them.** WebArena `induce_rule.py` can write concrete successful trajectories after filtering and optional manual inspection. That is trace-derived memory, but its abstraction is weaker than the README's workflow definition suggests.

**The optional FAISS retriever is pre-selection, not runtime memory.** It can rank workflow blocks by semantic similarity, but the acting agent still receives the selected text through prompt injection. This matters for read-back: the agent is pushed memory; it is not doing pull RAG.

**The quality gate is empirical but shallow.** Reward/autoeval selects successful traces, and deduplication reduces repetition, but there is no provenance-rich review of whether an induced workflow is generally valid, stale, or overfit to page ids.

**Website-specific ids are both useful and fragile.** Keeping invariant element ids can help WebArena-style tasks, but it makes a workflow brittle when page structure or benchmark configuration changes. That is an acceptable benchmark tradeoff and a weak general-memory design.

## What to Watch

- Whether workflow files gain versioned provenance from source trajectories. That would make induced procedures auditable instead of overwrite-only memory.
- Whether the embedding retriever moves into the acting loop. That would change AWM from identifier-scoped prompt push to prompt-instance semantic activation.
- Whether evaluation changes from aggregate success to per-workflow contribution tests. That would make read-back faithfulness measurable rather than inferred from benchmark deltas.
- Whether workflows become typed artifacts with applicability conditions, invalidation rules, and stale-page detection. That would make them more transferable to Commonplace-style operational lessons.
- Whether online induction keeps concrete trajectories or consistently abstracts them into reusable workflows. The design claim depends on abstraction, not mere successful-example replay.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: AWM makes activation explicit by injecting workflow memory into the prompt before action.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: AWM distills past web-navigation traces into reusable procedural memory.
- [Preserve evidence without loading history](../../notes/agent-memory-requirements/preserve-evidence-without-loading-history.md) - applies inversely: AWM stores traces as evidence but should load distilled workflows, not raw history, when possible.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: workflow files, traces, induction scripts, retrieval indexes, and prompt assemblies carry different substrates, forms, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: injected workflows act as prompt instructions, not merely passive knowledge, once loaded into the system or exemplar context.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - applies: AWM's strongest routing uses available symbols such as website, domain, benchmark, and workflow path.
