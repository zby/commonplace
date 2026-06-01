---
description: "Workflow-memory system for web agents that distills WebArena and Mind2Web trajectories into website-scoped prompt files with weak lineage and lifecycle controls"
type: ../types/agent-memory-system-review.md
status: outdated
tags: []
last-checked: "2026-05-16"
---

# Agent Workflow Memory

> Replaced 2026-06-01. See [agent-workflow-memory](./agent-workflow-memory.md) for the current review.

Agent Workflow Memory is the official code release for the AWM paper by Zhiruo Wang, Jiayuan Mao, Daniel Fried, and Graham Neubig. The repo implements a web-agent memory loop for WebArena and Mind2Web: run or collect web-task trajectories, induce reusable workflows from them, store those workflows as plain text files, and inject the files into later task-solving prompts. The important architectural choice is that "memory" is not a database service here. It is a website-scoped workflow prompt artifact produced from benchmark traces and reused by a mostly fixed acting agent.

**Repository:** https://github.com/zorazrw/agent-workflow-memory

**Reviewed revision:** [8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1](https://github.com/zorazrw/agent-workflow-memory/commit/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1)

## Core Ideas

**The durable memory is a workflow text file.** WebArena ships website files such as [`webarena/workflow/shopping.txt`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/workflow/shopping.txt), and the WebArena runner passes one file with `--workflow_path` ([`webarena/README.md`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/README.md), [`webarena/pipeline.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/pipeline.py)). Mind2Web similarly writes `workflow/{website}.txt` in offline mode and reuses that path for inference ([`mind2web/README.md`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/README.md), [`mind2web/offline_induction.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/offline_induction.py)). The representational form is prose plus action snippets, not a typed rule store, graph, or learned weight update.

**Workflow induction has two source regimes: annotated examples and successful trajectories.** Mind2Web offline induction loads training examples, augments candidate-element scores, formats full task/action traces, calls a model to summarize workflows, filters website-specific blocks, and writes a text file ([`mind2web/offline_induction.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/offline_induction.py), [`mind2web/utils/data.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/utils/data.py)). WebArena induction instead parses `experiment.log`, filters invalid actions, selects successful runs by ground-truth reward or autoeval, deduplicates by intent template and abstract action sequence, and either writes concrete examples directly or asks GPT to produce summary workflows ([`webarena/induce_rule.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_rule.py), [`webarena/induce_prompt.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/induce_prompt.py)).

**Online mode is staged between tasks, not live within a trajectory.** WebArena's pipeline runs one task with the current workflow file, evaluates the completed trajectory, then overwrites the website workflow before the next task ([`webarena/pipeline.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/pipeline.py)). Mind2Web's online pipeline runs a batch of examples, then calls `online_induction.py` over accumulated result JSON before continuing ([`mind2web/pipeline.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/pipeline.py), [`mind2web/online_induction.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/online_induction.py)). This is deploy-time artifact learning around a fixed agent, but the update cadence is benchmark-stage, not per-step self-modification.

**Prompt injection gives the workflow system-definition authority.** In WebArena, the legacy agent appends the workflow file directly to the system prompt before each action call ([`webarena/agents/legacy/agent.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/agents/legacy/agent.py), [`webarena/run.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/run.py)). In Mind2Web, `get_exemplars` reads the workflow file and prepends it as a prompt exemplar before sampled concrete examples from `data/memory/exemplars.json` ([`mind2web/memory.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/memory.py)). The raw traces are knowledge artifacts when inspected as evidence, but the induced workflow file becomes a system-definition artifact because it shapes the action policy at prompt time.

**Evidence, exemplars, workflows, and retrieval artifacts are separate surfaces.** WebArena result directories hold `experiment.log`, `summary_info.json`, screenshots, and autoeval JSON; Mind2Web writes per-task conversation JSON with inputs, outputs, predictions, targets, and metrics ([`webarena/autoeval/evaluate_trajectory.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/webarena/autoeval/evaluate_trajectory.py), [`mind2web/memory.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/memory.py)). Mind2Web also ships `data/memory/exemplars.json`, which is sampled separately from the workflow file. There is an optional `mind2web/workflow/retrieve.py` path that parses workflow blocks and tries to build a FAISS index over workflow names and docstrings, but it is not used by the main Mind2Web runner, and the inspected implementation returns metadata from `build_memory` where the semantic branch later expects a FAISS object ([`mind2web/workflow/retrieve.py`](https://github.com/zorazrw/agent-workflow-memory/blob/8c0ff8cd11d648c8fceb99e4e42f37e3b75381b1/mind2web/workflow/retrieve.py)).

**Lineage stops at directory convention.** The generated workflow file does not preserve source task IDs, source run IDs, evaluator model, extraction prompt version, confidence, or supersession metadata. The scripts can regenerate a file from result directories or training data, but the file itself does not carry enough provenance to invalidate or audit one workflow block later. This is the main cost of the deliberately simple text-file substrate.

## Comparison with Our System

| Dimension | Agent Workflow Memory | Commonplace |
|---|---|---|
| Primary memory artifact | Website-scoped workflow `.txt` file | Typed markdown notes, reviews, instructions, indexes, workshop artifacts |
| Source signal | Annotated web-task examples, successful trajectories, autoeval or ground-truth reward | Human and agent-authored artifacts, source snapshots, review traces, validation results |
| Representational form | Prose workflow descriptions plus action syntax | Mostly prose and markdown structure, with symbolic frontmatter, links, schemas, and scripts |
| Behavioral authority | Prompt-time instruction/exemplar for the acting web agent | Advice, instruction, validation, routing, review, and generated index authority split by artifact type |
| Lineage | External result directories and data files; weak provenance inside workflow artifacts | Frontmatter, links, source files, generated indexes, review state, and git history |
| Update style | Whole-file replacement after induction | Targeted file edits, validation, review, and index regeneration |
| Activation | Explicit `--workflow_path`, system prompt append, or Mind2Web exemplar injection | Agent navigation, authored links, skill loading, validation gates, and operator instructions |
| Scope | Website and benchmark family | Cross-project KB methodology |

AWM is stronger than commonplace on the narrow trace-to-procedure path. It demonstrates a compact loop where successful web-task behavior is distilled into a future action guide and immediately measured on the same benchmark family. Commonplace has richer artifact contracts and lifecycle controls, but it does not yet have an equivalent automated procedure-mining loop from task traces into reusable instructions.

Commonplace is stronger on governance. AWM's workflow files are readable and cheap to patch, but they are not addressable below the file level, not source-linked, not validated, and not retired by policy. That is fine for benchmark iteration where the file is a transient learned prompt. It is much weaker for a durable KB where an agent needs to know why a retained procedure exists, when it stopped applying, and who is allowed to change its authority.

**Read-back:** push — the configured workflow file is injected into the acting prompt before web action selection.

## Borrowable Ideas

**Mine procedures, not just facts, from traces.** Ready to borrow as a target shape. AWM's workflow prompt files are evidence that trace-derived extraction can produce procedural context, not only reflections or task summaries. In commonplace this would look like workshop traces producing candidate instructions or skills, with review before promotion.

**Keep the first version as plain text.** Ready to borrow, with governance added. AWM gets leverage because workflow files are ordinary prompt text. Commonplace should not jump straight to a complex workflow database unless a real activation problem demands it.

**Deduplicate traces before induction.** Ready to borrow. WebArena's two-stage deduplication by intent template and abstract action sequence is a small but useful protection against extracting the same routine repeatedly. A commonplace trace-mining workflow should similarly reduce near-duplicate episodes before asking a model to generalize.

**Separate raw trajectories from distilled procedures.** Ready to borrow. AWM keeps logs, evaluator outputs, exemplars, induced workflow files, and optional retrieval/index files distinct. The split is right even though the lineage between the surfaces is weak.

**Do not borrow whole-file replacement as the long-term lifecycle.** The overwrite model is acceptable for a benchmark prompt file. For commonplace, learned workflow blocks need stable IDs or file-per-procedure storage, source pointers, review state, and retirement rules before they become durable instructions.

**Treat workflow retrieval as a later optimization.** Needs a use case and implementation cleanup first. AWM's optional FAISS retrieval script is conceptually useful for selecting a small workflow subset, but the main runners use direct file injection, and the inspected semantic retrieval branch appears incomplete. The borrowable idea is "retrieve workflow blocks by task intent," not this exact implementation.

## Trace-derived learning placement

**Trace source.** AWM qualifies as trace-derived learning. The raw signals are WebArena completed task trajectories in `experiment.log`, autoeval or ground-truth success signals, Mind2Web annotated training examples, and Mind2Web result JSON from prior runs.

**Extraction.** WebArena extraction filters to successful runs, parses thought/action blocks, removes malformed actions, deduplicates by template and abstract trajectory, and either writes concrete examples or prompts GPT to summarize reusable workflows. Mind2Web extraction formats annotated examples or prior run JSON, calls GPT with workflow-induction prompts, and filters generated text to the current website.

**Storage substrate.** Raw traces live in result directories, data JSON, and evaluator outputs. Distilled workflows live in repository-local `.txt` files under `workflow/`. Optional retrieval artifacts can be FAISS indexes saved by `mind2web/workflow/retrieve.py`, but that path is outside the main acting loop at this commit.

**Representational form.** Raw traces are mixed evidence: natural-language thoughts, observations, action strings, screenshots, scores, and JSON metrics. The distilled operative part is prose plus symbolic action syntax. No inspected path updates weights.

**Lineage.** Lineage is external and procedural rather than embedded. A user can infer that `workflow/{website}.txt` came from a particular data directory or result directory used by an induction command, but the workflow file does not record source IDs, extraction model, prompt version, evaluator, timestamp, or source block references. Regeneration is possible by rerunning scripts, but invalidation is not local to the artifact.

**Behavioral authority.** Raw trajectories and evaluator outputs are knowledge artifacts: they are evidence for induction and audit. The workflow file is a system-definition artifact when injected into WebArena's system prompt or Mind2Web's exemplar context, because it directly shapes which actions the agent should take.

**Scope and timing.** Scope is website-local and benchmark-local. Offline Mind2Web induction happens before test inference from training examples. Online Mind2Web induction happens between batches. WebArena induction happens after completed task runs, often one task at a time in the shipped pipeline.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), AWM remains a trajectory-run readable-artifact learner. It strengthens the survey's "workflow prompt files" subtype: traces become reusable action procedures, not just reflections or facts. It also sharpens the maintenance-axis claim because AWM's workflow-file replacement is clearly weaker than ExpeL-style operation verbs or ACE-style counters, despite being more procedure-shaped than Dynamic Cheatsheet's single cheatsheet blob.

## Curiosity Pass

**The word "memory" is doing real work, but narrowly.** The workflow file changes later action selection, so it is memory in the behavioral sense. It is not a general memory system: no write API, no query service, no lifecycle policy, and no durable evidence package inside the artifact.

**The induced artifact is more procedural than many reflection systems.** AWM's workflows are closer to "how to navigate this site" than to "remember this fact." That makes it especially relevant to commonplace instructions and skills, not only notes.

**The strongest oracle is before the artifact, not after it.** WebArena induction can select successful trajectories using ground-truth reward or autoeval, but after a workflow is written there is no block-level test saying which induced procedure helped or hurt. The system measures benchmark success overall, not the validity of individual workflow routines.

**Mind2Web mixes workflow memory with exemplar prompting.** `get_exemplars` injects the workflow file and then samples concrete examples from `exemplars.json`. That makes attribution hard: improvements may come from induced workflows, sampled examples, or both.

**The optional retrieval path is more revealing as a design sketch than as finished machinery.** Loading workflow names and docstrings into a vector index is a reasonable scaling direction. But because the main runner does not depend on it, and because the semantic branch appears inconsistent at the return-value boundary, the reviewed system should be read primarily as file-injection workflow memory.

## What to Watch

- Whether future versions add source IDs, evaluator metadata, extraction prompt versions, or confidence fields to workflow blocks.
- Whether workflow files move from whole-file replacement to addressable workflow units with add/edit/remove operations.
- Whether WebArena and Mind2Web converge on one induction and injection abstraction instead of separate benchmark-specific scripts.
- Whether the optional FAISS workflow retrieval path becomes part of the main inference loop and is repaired enough to evaluate.
- Whether AWM-style workflow induction transfers outside benchmark websites where DOM IDs, site templates, and task distributions are less stable.

---

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - source-inspected instance: AWM distills web-task trajectories and annotated examples into website-scoped workflow prompt files
- [Designing agent memory systems](../../notes/designing-agent-memory-systems.md) - exemplifies: behavior-changing memory is about what later action can change, not whether the substrate is called memory
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - supports: AWM is a readable-artifact trace-extraction loop with weak lineage inside the artifact
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: the workflow artifact matters because it loads before action selection
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - contrasts: AWM's result directories are workshop-like source evidence, while workflow files are promoted action guidance
- [Dynamic Cheatsheet](./dynamic-cheatsheet.md) - contrasts: both learn prompt-state artifacts from benchmark runs, but AWM produces website-scoped workflows from successful web trajectories rather than maintaining one carried-forward cheatsheet blob
- [ExpeL](./expel.md) - contrasts: both mine experience into reusable instructions, but ExpeL has explicit memory-edit operations while AWM overwrites workflow files
- [ReasoningBank](./reasoning-bank.md) - compares-with: ReasoningBank includes AWM as a baseline-style extraction mode, but adds a JSONL memory bank and retrieval pipeline around extracted items
