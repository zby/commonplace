---
description: "Planner-executor research agent that turns benchmark answer traces into JSONL case memory and a trained case selector for planner prompt reuse"
type: ../types/agent-memory-system-review.md
tags: [related-systems, trace-derived]
status: current
last-checked: "2026-04-27"
---

# AgentFly

AgentFly is the GitHub repository for the system its README presents as Memento: a planner-executor research agent that improves benchmark performance by storing prior question plans as cases, retrieving similar cases for new questions, and optionally training a neural case selector over accumulated successes and failures. The code combines a meta-planner, an executor connected to MCP tool servers, JSONL case memory, an LLM-based answer judge, and parametric or non-parametric retrieval. Built by Huichi Zhou, Yihang Chen, Siyuan Guo, Xue Yan, Kin Hei Lee, Zihan Wang, Ka Yiu Lee, Guchun Zhang, Kun Shao, Linyi Yang, and Jun Wang according to the README citation.

**Repository:** https://github.com/Agent-on-the-Fly/AgentFly

**Reviewed revision:** 42fbbcac63dd58ed6856c0761357345a58e4f032

**Commit:** https://github.com/Agent-on-the-Fly/AgentFly/commit/42fbbcac63dd58ed6856c0761357345a58e4f032

## Core Ideas

**A hierarchical planner-executor loop is the base agent.** The plain client keeps a short `shared_history`, asks a meta-planner for JSON subtasks, and runs each subtask through an executor that can call MCP tools before feeding task results back to the planner. That loop is implemented in `client/agent.py`, while the README frames it as a Meta-Planner plus Executor architecture for high-level questions and tool-mediated subtasks. Sources: [client/agent.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/agent.py), [README.md](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/README.md).

**Case memory is planner-level in-context learning, not a general knowledge base.** The durable memory item is a prior question plus the planner's JSON plan plus a label. Non-parametric mode reads `memory/dummy_memo.jsonl`, embeds question keys with SimCSE, retrieves top-k similar cases, splits them into positive and negative examples by reward, and injects a formatted "provide a plan for the current task" prompt before planning. Parametric mode reads `memory/memory.jsonl`, retrieves cases with a classifier, and injects the same positive/negative plan examples. Sources: [client/no_parametric_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/no_parametric_cbr.py), [client/parametric_memory_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/parametric_memory_cbr.py), [memory/memory.jsonl](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/memory.jsonl).

**The non-parametric retriever is simple embedding search rebuilt at query time.** `memory/np_memory.py` loads JSONL records, extracts key/value pairs, embeds all keys and the incoming task with `transformers` models, computes dot-product similarity, and returns ranked cases with line indexes. There is no vector database, metadata schema, or lifecycle layer beyond appending JSONL rows and reloading them after each new run. Source: [memory/np_memory.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/np_memory.py).

**The parametric retriever trains a binary selector over query-case pairs.** `train_memory_retriever.py` builds `PairJsonlDataset` rows from `query`, `case`, `plan`, and `truth_label`, encodes the current query and candidate case text with a sentence-transformer backbone, concatenates the two embeddings, and trains a two-class classifier. `memory/parametric_memory.py` loads the trained weights, scores every case in the pool against the new prompt, sorts by probability, and returns the highest scoring cases. Sources: [memory/train_memory_retriever.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/train_memory_retriever.py), [memory/parametric_memory.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/parametric_memory.py).

**Learning is driven by an answer judge over benchmark data.** Both CBR scripts load `data/deepresearcher.jsonl`, run tasks, judge the final answer against ground truth with `gpt-4o-mini`, write detailed result traces, and append new memory rows. Non-parametric mode appends `{question, plan, reward}`; parametric mode appends `{case, plan, case_label}` and also writes training pairs for every retrieved case with a `truth_label` derived from whether the current answer was judged correct. Sources: [client/no_parametric_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/no_parametric_cbr.py), [client/parametric_memory_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/parametric_memory_cbr.py), [memory/training_data.jsonl](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/training_data.jsonl).

**The MCP tool layer is broad but mostly orthogonal to memory.** The server directory supplies code execution, search, crawling, document, image, video, spreadsheet, and math tools through FastMCP scripts. The memory system does not store tool-specific artifacts as reusable skills; tool calls are captured in result records, while the durable case memory keeps the planner's plan text. Sources: [server/](https://github.com/Agent-on-the-Fly/AgentFly/tree/42fbbcac63dd58ed6856c0761357345a58e4f032/server), [server/code_agent.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/server/code_agent.py).

## Comparison with Our System

AgentFly and commonplace both treat memory as an artifact-level intervention rather than a model-weight update. The overlap ends quickly: AgentFly optimizes planner prompt examples for benchmark QA tasks, while commonplace maintains a typed, inspectable methodology library for future agent work.

| Dimension | AgentFly | Commonplace |
|---|---|---|
| Trace source | Benchmark question runs, plans, answers, judge labels, retrieved cases | Human and agent edits, notes, sources, reviews, workshop artifacts |
| Durable unit | JSONL case rows and retriever training pairs | Typed markdown notes, links, ADRs, instructions, generated indexes |
| Retrieval | SimCSE embedding search or trained binary case selector | Grep over titles/frontmatter plus authored links and indexes |
| Promotion target | Planner prompt examples; optionally retriever weights | Library notes, instructions, scripts, validation rules, indexes |
| Oracle | LLM judge against benchmark ground truth | Human judgment plus validation and review bundles |
| Lifecycle | Append rows; retrain selector; no retirement or provenance per case | Status fields, backlinks, review, validation, archival patterns |
| Consumer | The meta-planner only | Acting agents, maintainers, reviewers, navigation surfaces |

AgentFly is stronger as an online experimental loop. A completed benchmark run immediately changes future planning because the script appends a new case and reloads memory before the next question. Commonplace is stronger as an audit substrate: its artifacts keep type contracts, explicit links, source evidence, and maintenance status, while AgentFly's cases are unlabeled examples except for positive/negative outcome labels.

The most important divergence is the memory unit. In AgentFly, the learned artifact is not "how to solve this problem" in a richly explained sense; it is a reusable planner demonstration. That is a narrow but behaviorally active unit: reading the case examples can change the next plan. Commonplace's notes are broader and more composable, but activation depends on navigation rather than an automatic per-query case-injection path.

## Borrowable Ideas

**Keep positive and negative examples symmetric in prompt memory.** Ready when we have a bounded workflow with clear pass/fail outcomes. AgentFly's planner prompt shows both successful and unsuccessful prior plans, which is a useful middle ground between "retrieve only successes" and "dump raw traces."

**Train retrieval on usefulness labels, not just similarity.** Needs a use case first. The parametric retriever's `truth_label` is crude, but the design question is right: similar cases are not always useful cases. Commonplace could eventually score retrieval candidates by downstream task-helpfulness rather than lexical or embedding similarity.

**Append-and-reload as the smallest online learning loop.** Ready as a workshop pattern. AgentFly does not require a server, database, or background job for non-parametric memory; it appends a JSONL row and reloads the case pool. That is a useful baseline for any future commonplace experiment in task-local adaptive memory.

**Separate trace records from distilled case rows.** Ready as a framing. AgentFly writes detailed result records with traces, tool history, judge rationale, and final answer, but the consumed memory row is just question/plan/label. Commonplace's workshop-to-library promotion already has this shape; AgentFly is a compact example of the same compression in benchmark-agent form.

**Do not borrow the lifecycle model as-is.** AgentFly has no evidence-preserving case schema, no case retirement, no contradiction handling, and no explicit provenance link from a memory row back to the full run record. Commonplace should only borrow the retrieval-training loop if the artifact contract also keeps source trace identity.

## Trace-derived learning placement

AgentFly qualifies as trace-derived learning. The trace source is benchmark task execution: each run records the query, planner JSON, executor steps, tool calls, final answer, judge rationale, and reward or correctness label in result JSONL. The trigger boundary is one benchmark question; the online scripts update memory after each completed question and skip already finished questions on restart.

Extraction is partly automatic and lossy. The LLM judge decides whether the answer matches ground truth. Non-parametric mode distills the trace to one `{question, plan, reward}` memory row. Parametric mode distills it to `{case, plan, case_label}` and, when retrieved cases existed, appends query-case training pairs labeled by whether the current run succeeded. The oracle is therefore benchmark ground truth mediated by an LLM judge, not a deterministic evaluator.

The substrate is split. The consumed memory is prose/structured text in JSONL case rows: natural-language questions plus JSON planner steps. The parametric retriever adds an opaque substrate, a trained classifier checkpoint, but that checkpoint selects cases rather than encoding the task policy directly. The role is system-definition at planner time: retrieved examples are injected before planning and are intended to change the planner's behavior, not merely answer factual questions.

Scope is per-benchmark or per-memory-pool, not cross-project knowledge. Timing is online for JSONL case accumulation and staged/offline for retriever training. On the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md), AgentFly sits in trajectory-run ingestion on axis 1 and splits axis 2 between prose case memory and opaque selector weights. It strengthens the survey claim that many "fine-tuning without fine-tuning" systems still rely on artifact memory first, with learned parameters used as a retrieval policy around those artifacts rather than as the primary memory.

## Curiosity Pass

The repository name and README title disagree: the GitHub repository is AgentFly, while the README, package metadata, and user-facing docs call the project Memento. The mechanism under review is the code in this checkout, so the note keeps the requested review title while naming the README identity.

The phrase "parametric memory" is easy to overread. The trained model does not store experiences as model knowledge in the sense of being directly prompted or decoded; it scores query-case pairs so the planner can read selected JSONL cases. The durable experiences remain outside the weights.

The reward assignment for parametric training is coarse. If a run succeeds, every retrieved case used for that run is written as useful; if it fails, every retrieved case is written as not useful. That makes the training loop simple, but it cannot distinguish a helpful retrieved plan from an irrelevant one that happened to be present during a successful run.

The implementation is benchmark-shaped rather than product-shaped. It has scripts for DeepResearcher-style batches, result files, and retraining, but not a durable multi-user memory service or a governance surface for inspecting, editing, retiring, or merging cases.

## What to Watch

- Whether the project adds case pruning, deduplication, or provenance links from memory rows back to full result traces.
- Whether the parametric retriever is retrained automatically in a closed loop or remains a manual script around accumulated JSONL files.
- Whether future versions store tool-call traces or successful executor code as reusable artifacts, instead of only planner demonstrations.
- Whether the LLM judge is replaced or backed by deterministic benchmark evaluators where available.
- Whether the planned memory compression and multi-modal memory features become implemented artifact contracts or remain README roadmap items.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: AgentFly splits trace-derived memory between JSONL planner cases and an opaque learned retrieval policy.
- [ExpeL](./expel.md) - compares-with: both learn from benchmark trajectories, but ExpeL promotes maintained rules while AgentFly promotes case examples and retrieval labels.
- [Voyager](./voyager.md) - contrasts: Voyager promotes executable skills from embodied task success; AgentFly promotes planner examples from question-answer benchmark runs.
- [oracle-strength-spectrum](../../notes/oracle-strength-spectrum.md) - exemplifies: AgentFly uses a soft LLM judge over ground-truth answers, stronger than self-report but weaker than deterministic scoring.
- [deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - exemplifies: non-parametric mode changes future behavior during a run by appending and reloading case memory without weight updates.
