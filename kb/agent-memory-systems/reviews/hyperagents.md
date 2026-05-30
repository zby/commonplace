---
description: "HyperAgents review: self-editing agent harness where benchmark traces and scores select executable git-diff patches rather than prose memories"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# HyperAgents

HyperAgents is Meta/Facebook Research's self-referential agent-evolution harness. It runs a meta agent inside Docker, lets that agent edit the agent codebase, captures the resulting git diff, evaluates the patched task agent on configured benchmark domains, stores generation metadata and archive membership, and selects future parents from the scored archive. The implementation is an outer-loop self-editing system more than a semantic memory system: durable behavior lives in executable patches and selection records, while traces and reports are evidence used by later meta-agent calls.

**Repository:** https://github.com/facebookresearch/Hyperagents

**Reviewed commit:** [59a68f672dfb92c74aeb7e61535d776fb36e172d](https://github.com/facebookresearch/Hyperagents/commit/59a68f672dfb92c74aeb7e61535d776fb36e172d)

## Core Ideas

**The meta agent edits the codebase, not a memory store.** `MetaAgent.forward(...)` gives the model a blunt instruction to modify any part of the repository path, with all local tools enabled through the repo's JSON tool loop ([meta_agent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/meta_agent.py), [agent/llm_withtools.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/agent/llm_withtools.py), [agent/tools](https://github.com/facebookresearch/Hyperagents/tree/59a68f672dfb92c74aeb7e61535d776fb36e172d/agent/tools)). `run_meta_agent.py` then resets unwanted `domains/` changes and writes the diff against the base commit to `model_patch.diff` ([run_meta_agent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/run_meta_agent.py), [utils/git_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/git_utils.py)). The promoted artifact is a symbolic system-definition artifact: a git patch that changes future agent execution.

**The task agent is intentionally minimal.** `TaskAgent.forward(...)` formats task input, asks the model for a JSON `response`, extracts the response, and returns message history for logging ([task_agent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/task_agent.py)). There is no durable semantic memory, lesson table, vector store, rule library, or retrieved experience layer in the checked-in task agent. Improvement happens when the meta loop edits the code or prompts that define the task agent.

**Archive state is generation-level lineage.** `generate_loop.py` creates `gen_initial/`, `gen_N/`, `metadata.json`, `archive.jsonl`, `agent_output/meta_agent_chat_history.md`, `agent_output/model_patch.diff`, benchmark eval folders, reports, and analysis plots under an output directory ([generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py), [utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py)). `metadata.json` records parent id, previous and current patch files, eval status, validity, optimize mode, and whether the node can select a next parent. `archive.jsonl` appends the evolving list of generation ids. This is good lineage for replaying a node, but not fine-grained provenance from a particular failure trace to a particular patch hunk.

**Docker replay is the activation mechanism.** Each generation builds or starts a Docker container, applies all parent lineage patches, runs the meta agent, copies patch and eval outputs back out, evaluates the produced agent, then resets and cleans the container before cleanup ([generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py), [utils/docker_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/docker_utils.py), [utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py)). Stored diffs are not merely archival records; they become behavior by being applied into a fresh repo copy before the next meta-agent run or evaluation.

**Evaluation and selection are benchmark-mediated.** The generic harness imports `TaskAgent`, runs it over domain datasets or environment tasks, writes predictions and per-task chat histories, and reports scores such as accuracy, progress, fitness, or proof points ([domains/harness.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/harness.py), [domains/report.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/report.py), [utils/domain_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/domain_utils.py)). Generation evaluation supports staged evaluation before fuller evaluation, and some domains have train/val/test splits. Parent selection can be random, latest, best, score-proportional, or score-and-child-count-weighted; an optional path lets the evolved `select_next_parent.py` choose the next parent in a container ([generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py), [select_next_parent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/select_next_parent.py), [utils/run_select_next_parent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/run_select_next_parent.py)).

**The benchmark surface is broad but domain-specific.** The CLI exposes Search Arena, paper review, Balrog variants, Genesis robot-control variants, Polyglot, IMO grading, and IMO proof domains; support is routed through domain-specific harnesses, reports, score keys, staged-eval sample counts, and split rules ([generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py), [utils/domain_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/domain_utils.py), [domains](https://github.com/facebookresearch/Hyperagents/tree/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains)). The system is therefore a reusable evolutionary harness over computable tasks, but each useful evaluation oracle still needs domain plumbing.

## Comparison with Our System

| Dimension | HyperAgents | Commonplace |
|---|---|---|
| Primary retained state | Output directories, `archive.jsonl`, per-generation `metadata.json`, chat histories, reports, `model_patch.diff` files | Typed markdown notes, reviews, instructions, sources, generated indexes, validation and review outputs |
| Behavior-changing artifact | Applied git diffs over agent code and optional parent-selection code | Notes as knowledge artifacts; instructions, schemas, validators, commands, and skills as system-definition artifacts |
| Raw evidence | Meta-agent chat history, task-agent chat histories, predictions, reports, environment outputs | Sources, snapshots, review traces, validation reports, authored links |
| Selection oracle | Benchmark score, staged eval, valid-parent flags, parent-selection policy | Human/agent review, validation, semantic gates, maintainer judgment |
| Lineage | Generation parent id plus ordered patch-file lineage | Git history, frontmatter metadata, source links, archive replacement notes, generated-index provenance |
| Activation | Docker copy plus patch replay, then import/run changed agent code | Agent navigation, skill loading, validation, and instruction loading |

HyperAgents is stronger than commonplace at closing a hard empirical loop. It does not ask whether a lesson is well written; it asks whether the patched agent scores better or remains a valid parent under benchmark feedback. That makes promotion cheap when the benchmark is trustworthy.

Commonplace is stronger at artifact typing and long-lived interpretability. HyperAgents has the artifact families implicitly: chat histories and reports are knowledge artifacts, patches are system-definition artifacts, score reports rank candidates, and selection code configures future search. The implementation does not make those contracts explicit, attach review status to patch hunks, or preserve semantic explanations as first-class retained artifacts.

The deepest contrast is prose memory versus executable heredity. Commonplace usually tries to make future agents better by giving them better inspectable knowledge and stronger operating rules. HyperAgents makes future agents better by replaying code diffs selected by benchmark pressure. That is memory in the retained-artifact sense, but its operative part is executable code, not a note.

**Read-back:** both — meta agents inspect prior eval artifacts, while selected patch lineages are replayed into future agents.

## Borrowable Ideas

**Treat patch replay as a first-class retained artifact.** Ready to borrow for eval-backed tool or skill loops. A patch file with parent metadata, benchmark score, and replay procedure is a system-definition artifact, not just an experiment artifact.

**Keep raw traces distinct from promoted behavior.** Ready to borrow. HyperAgents stores chat histories, predictions, reports, and patches as separate surfaces. Commonplace trace-derived workflows should preserve that split rather than calling every trace-derived file a memory.

**Use parent selection to avoid single-lineage overfitting.** Worth borrowing when commonplace has enough comparable eval history. Score-and-child-count parent selection is a compact way to preserve exploration pressure without adding a heavy novelty model.

**Replay in a disposable container before trusting generated code.** Ready to borrow for self-editing loops that can afford Docker. The container reset/clean cycle gives generated patches a controlled activation path, even though it is not a complete security boundary.

**Do not borrow unrestricted repository editing as the default.** HyperAgents intentionally lets the meta agent edit broadly, then filters only some paths. Commonplace agents usually need tighter file ownership and artifact contracts because note quality, source fidelity, and instruction authority are not reducible to one benchmark score.

## Trace-derived learning placement

**Trace source.** HyperAgents qualifies as trace-derived learning, but not because it writes prose memories. The raw signals are meta-agent chat histories, task-agent chat histories, benchmark predictions, environment or dataset outputs, per-domain report JSON, generation logs, and score summaries produced during each generation ([generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py), [domains/harness.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/harness.py), [domains/report.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/domains/report.py)).

**Extraction.** Extraction is performed by the meta agent reading the previous generation output directory passed as `--evals_folder`, inspecting evaluation artifacts with bash/editor tools, and editing the repo. The benchmark oracle then decides whether the resulting patch is evaluated, valid, and selectable through staged/full evaluation, report scores, `valid_parent`, and parent-selection policy ([run_meta_agent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/run_meta_agent.py), [generate_loop.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/generate_loop.py), [utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py)).

**Storage substrate.** Raw and derived state lives in the filesystem under generation output directories. Raw traces and eval outputs include chat-history markdown, prediction CSVs, report JSON, logs, and domain-specific output folders. Derived behavior lives in patch files under `gen_N/agent_output/model_patch.diff`, plus lineage pointers in `metadata.json` and archive membership in `archive.jsonl`. Docker containers are replay surfaces, not the canonical storage substrate.

**Representational form.** Raw traces are mixed prose and symbolic records: markdown chat logs, CSV predictions, JSON reports, score scalars, and environment files. Promoted behavior is symbolic executable code and prompt text encoded as git diff patches. There is no inspected path that distills traces into embeddings, vector memories, adapters, weights, or natural-language lesson files.

**Lineage.** Lineage is explicit at generation granularity. A node records its parent, previous patch files, current patch files, evaluation status, and validity; replay applies the ordered lineage diffs into a repo copy. Lineage is weak at semantic granularity: a patch hunk does not carry a source trace id, failure label, causal explanation, or invalidation condition beyond later benchmark performance.

**Behavioral authority.** Raw traces, reports, predictions, logs, and chat histories are knowledge artifacts when a later meta agent reads them as evidence or context. `model_patch.diff` files are system-definition artifacts because they are applied to code that later runs. `metadata.json`, `archive.jsonl`, score reports, and parent-selection code have ranking, configuration, and selection authority. Docker replay has activation authority because it turns stored diffs into an executable agent state.

**Scope and timing.** Scope is per experiment output directory and per configured domain set, with transfer experiments supported by `--meta_patch_files`, `--reset_task_agent`, `--reset_meta_agent`, and `--copy_root_dir`. Timing is offline and generational: run a parent, produce a patch, evaluate, archive, select another parent, and repeat.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), HyperAgents belongs with outer-loop artifact-learning systems. It strengthens the survey split between raw trace/eval artifacts and promoted behavior-shaping artifacts: the trace-derived status is supported, but the promoted artifacts are executable system-definition patches selected by benchmark feedback rather than prose memories or semantic lessons.

## Curiosity Pass

The checked-in meta agent is much thinner than the framing suggests. Most of the intelligence is delegated to the model plus bash/editor tools; the surrounding harness supplies replay, capture, evaluation, archive, and selection.

The system has memory in the evolutionary sense, not the semantic-memory sense. It can carry successful behavior forward through patch lineage, but it does not maintain a lesson layer that a future agent can inspect independently of the code diff.

The path reset is asymmetric. `run_meta_agent.py` resets `domains/` before writing the patch, and `apply_diffs_container(...)` filters `domains/` patch blocks, but broad edits elsewhere are allowed ([run_meta_agent.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/run_meta_agent.py), [utils/gl_utils.py](https://github.com/facebookresearch/Hyperagents/blob/59a68f672dfb92c74aeb7e61535d776fb36e172d/utils/gl_utils.py)). That matches a research harness but would be too permissive for most KB maintenance.

The archive stores enough to replay generations, but not enough to explain them. For analysis, a human can read chat histories and diffs; for maintenance, there is no typed manifest saying which benchmark failures a patch targeted or why it should generalize.

Parent selection is both fixed infrastructure and optionally evolvable behavior. The default code has several simple policies, while `--edit_select_parent` lets the selected parent mechanism run from code in the evolving repository. That makes selection itself a possible system-definition artifact under evolution.

## What to Watch

- Whether future versions add structured patch manifests with target failures, expected effect, risk, and source trace references.
- Whether a semantic lesson or reflection layer appears between raw eval outputs and executable patches.
- Whether evolved parent-selection policies become a major behavior surface rather than an optional experiment flag.
- Whether the Docker boundary becomes stronger against destructive generated code, especially for domains needing GPU or host-mounted data.
- Whether published experiment logs include enough archive, patch, and report data for independent replay rather than only aggregate plots.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: HyperAgents turns traces and benchmark feedback into executable system-definition patches rather than prose memories.
- [Meta-Harness](./meta-harness.md) - compares-with: both optimize harness artifacts from traces and benchmark feedback, but HyperAgents emphasizes self-referential patch lineage and parent selection.
- [auto-harness](./auto-harness.md) - compares-with: both use benchmark feedback to promote code changes, with HyperAgents adding archive parent selection and broader domain support.
- [Voyager](./voyager.md) - compares-with: both promote executable artifacts from trial feedback, but Voyager stores callable task skills while HyperAgents stores repo-level diffs.
- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: chat histories, reports, predictions, and logs advise later meta-agent runs.
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: patch files, selection code, metadata gates, and Docker replay configure or execute future behavior.
