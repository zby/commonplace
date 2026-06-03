---
description: "AgentFly review: planner-executor agent with case-bank planning memory, trace-derived plan labels, and retriever-gated prompt injection"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# AgentFly

AgentFly, from the `Agent-on-the-Fly/AgentFly` repository, is published in the README as Memento: a planner-executor research agent that uses case-based reasoning to improve future task planning without fine-tuning the base planner or executor LLMs. The core memory implementation is not a general user-memory substrate. It is a benchmark-oriented case bank of prior questions, generated plans, and correctness labels, read back into the meta-planner before it decomposes the next task.

**Repository:** https://github.com/Agent-on-the-Fly/AgentFly

**Reviewed commit:** [42fbbcac63dd58ed6856c0761357345a58e4f032](https://github.com/Agent-on-the-Fly/AgentFly/commit/42fbbcac63dd58ed6856c0761357345a58e4f032)

**Last checked:** 2026-06-01

## Core Ideas

**The base agent is a hierarchical planner-executor.** `client/agent.py` runs a meta-planner that emits JSON subtasks, then an executor sub-agent that can call MCP tools and returns concise results to the planner. Its only in-run memory is `shared_history`, trimmed by token budget; it does not persist cases or learn across runs ([client/agent.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/agent.py)).

**Case memory stores plans, not full trajectories.** The memory pool is JSONL. In the parametric path, each row has `case`, `plan`, and `case_label`; the non-parametric path uses `question`, `plan`, and `reward` fields. The bundled `memory/memory.jsonl` shows short natural-language questions paired with serialized planner JSON and positive/negative labels, not observations, tool calls, source evidence, or final answers ([memory/memory.jsonl](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/memory.jsonl), [memory/np_memory.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/np_memory.py), [memory/parametric_memory.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/parametric_memory.py)).

**Non-parametric CBR retrieves by embedding similarity.** `client/no_parametric_cbr.py` loads `MEMORY_JSONL_PATH`, extracts question-plan pairs, embeds case keys with a SimCSE model, retrieves top-k similar cases for the current query, separates them into positive and negative examples using the original row's reward, and injects a prompt that asks the planner to imitate positives and avoid negatives ([client/no_parametric_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/no_parametric_cbr.py), [memory/np_memory.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/np_memory.py)).

**Parametric memory trains a case selector, not the agent itself.** `memory/train_memory_retriever.py` trains a classifier over current query and candidate in-context case text, saving `best.pt` or `last.pt`. `memory/parametric_memory.py` loads that checkpoint and scores each pool entry for the current query. The README frames this as learning without LLM weight updates: the trained retriever changes which examples reach the planner, while the planner and executor models remain external LLM calls ([memory/train_memory_retriever.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/train_memory_retriever.py), [memory/parametric_memory.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/parametric_memory.py), [README.md](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/README.md)).

**The online loop writes new cases from judged runs.** Both CBR clients run benchmark questions from `data/deepresearcher.jsonl`, call an LLM judge over predicted answer and ground truth, write result records under `../result/`, and append memory entries for later runs. The parametric path also writes `training_data.jsonl` rows linking the current query, each retrieved case, the case label, and whether the current answer was correct ([client/no_parametric_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/no_parametric_cbr.py), [client/parametric_memory_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/parametric_memory_cbr.py), [memory/training_data.jsonl](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/training_data.jsonl)).

**Tool use is broad, but memory only steers planning.** The executor can call MCP-style servers for code execution, crawling, documents, search, images, math, video, and related tools. The case memory is injected into planner messages before task decomposition; it does not select tools directly, validate tool outputs, rewrite executor prompts per subtask, or constrain final-answer generation ([client/agent.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/agent.py), [client/parametric_memory_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/parametric_memory_cbr.py), [server](https://github.com/Agent-on-the-Fly/AgentFly/tree/42fbbcac63dd58ed6856c0761357345a58e4f032/server)).

## Artifact analysis

- **Storage substrate:** `files` — Filesystem JSONL files such as `memory/memory.jsonl` or the configured `MEMORY_JSONL_PATH`
- **Representational form:** `mixed` — Symbolic JSON records containing prose questions, serialized planner JSON, and positive/negative labels or rewards

**Case-bank JSONL.** Storage substrate: filesystem JSONL files such as `memory/memory.jsonl` or the configured `MEMORY_JSONL_PATH`. Representational form: symbolic JSON records containing prose questions, serialized planner JSON, and positive/negative labels or rewards. Lineage: seeded examples plus trace-derived rows appended after judged benchmark runs. Behavioral authority: knowledge artifacts when inspected as examples; system-definition artifacts at read-back time because selected rows are transformed into planner context that biases the next decomposition.

**Result and trace records.** Storage substrate: JSONL result files written under `../result/` by the CBR clients. Representational form: mixed symbolic/prose records containing query, model output, plan JSON, meta-planner trace, executor trace, tool history, judge rationale, and reward or correctness. Lineage: generated from benchmark questions, planner/executor calls, MCP tool results, and an LLM judge over ground truth. Behavioral authority: knowledge artifacts as audit/evaluation evidence; system-definition artifacts only when compressed into memory rows or pairwise training rows.

**Retriever-training JSONL.** Storage substrate: `memory/training_data.jsonl` or `TRAINING_DATA_PATH`. Representational form: symbolic pair records with current query, retrieved case, case label, plan, and `truth_label`. Lineage: derived from parametric CBR runs by pairing the current judged outcome with every case that was retrieved for that query. Behavioral authority: system-definition artifact for learning because the trainer uses these rows to decide which query-case pairs should be selected later.

**Non-parametric embedding retriever.** Storage substrate: no persistent index in the inspected code; embeddings are computed at retrieval time from the JSONL pool. Representational form: distributed-parametric SimCSE embeddings plus symbolic top-k scores. Lineage: derived from the case-bank key text and the current query under the chosen pretrained encoder. Behavioral authority: ranking system-definition artifact because similarity decides which cases are converted into planner prompt examples.

**Parametric retriever checkpoint.** Storage substrate: PyTorch checkpoint path such as `memory/ckpts/retriever/best.pt`, supplied through `RETRIEVER_MODEL_PATH`. Representational form: distributed-parametric classifier weights on top of a transformer backbone. Lineage: trained from `training_data.jsonl`, tokenizer/backbone choice, split policy, class weighting, and optimizer settings in `train_memory_retriever.py`. Behavioral authority: ranking system-definition artifact because its scores determine which positive and negative cases reach the planner.

**Prompt templates and planner/executor system prompts.** Storage substrate: Python string constants in the client files. Representational form: prose instructions embedded in code. Lineage: authored framework code. Behavioral authority: system-definition artifacts because they define planner JSON shape, executor tool-use behavior, final-answer format, judge criteria, and the meaning of injected positive/negative cases.

The promotion path is benchmark run -> result trace -> judged plan memory row -> retrieved prompt example, with an optional second path through pairwise training data -> retriever checkpoint -> better case selection. It promotes traces into case-selection and prompt-conditioning artifacts, not into durable prose lessons, validators, route tables, or changed planner/executor weights. The main governance gap is lineage: appended memory rows and training rows do not preserve source result-file id, judge model version, prompt version, retrieval scores, or acceptance status.

## Comparison with Our System

| Dimension | AgentFly | Commonplace |
|---|---|---|
| Primary purpose | Improve benchmark task planning through retrieved prior cases | Maintain a typed methodology KB for future agents and maintainers |
| Canonical retained unit | JSONL case with question, plan, and label; optional retriever checkpoint | Git-tracked markdown artifacts, schemas, links, indexes, reviews, and reports |
| Learning loop | Online judged runs append memory; optional offline retriever training | Source-grounded writing, review, validation, and workshop-to-library promotion |
| Read-back | Retrieved cases are pushed into the planner prompt before decomposition | Mostly pull through search/indexes/links, plus explicit instructions and generated context where configured |
| Governance | LLM judge, labels, top-k retrieval, training metrics | Collection contracts, schemas, deterministic validation, semantic review, git history |

AgentFly is closer to Commonplace than systems that only fine-tune a model, because the main behavior-shaping artifacts remain inspectable as files. But its retained unit is narrower: a task and a plan label, rather than a source-grounded note with frontmatter, links, type contract, review state, and explicit evidence. It optimizes for fast few-shot reuse, not durable explanation.

The strongest alignment is the separation between raw evidence and loaded context. AgentFly stores result traces and memory rows, but only a small retrieved subset reaches the planner. Commonplace already makes the same bet with search, indexes, and scoped note loading. The difference is activation: AgentFly automates selection and prompt insertion for every benchmark query, while Commonplace usually leaves search and linking as deliberate agent actions unless an instruction or workflow frontloads context.

The tradeoff is auditability versus immediacy. AgentFly can improve the next run by appending a few JSONL rows, but the row itself carries little support for source review or invalidation. Commonplace makes promotion slower because the artifact must explain itself, but that friction is what lets future agents inspect why a rule or note should still have authority.

**Read-back:** `push` — With instance-targeted inferred selection. From the acting planner's perspective, retrieved case memory arrives before it asks for it; non-parametric CBR gates by SimCSE embedding similarity over the current query and case question, and parametric CBR gates by a trained neural query-case classifier.

### Borrowable Ideas

**Inject negative examples as first-class memory.** A Commonplace analogue would preserve failed plans or invalid review moves alongside successful procedures, then load them as "avoid this pattern" evidence when the current task matches. Ready for workshop reports; promotion to standing instructions needs review gates.

**Train a selector without changing the consuming agent.** AgentFly's parametric retriever changes activation, not the planner model. Commonplace could use a learned or scored selector for context packets while keeping the KB artifacts readable and versioned. Needs a larger supervised corpus of retrieval decisions.

**Keep plan memory separate from execution trace memory.** AgentFly stores compact planning cases even when result records contain fuller traces. Commonplace could similarly distill long agent runs into small plan-shaping cards while retaining the trace as evidence. Ready as a trace-review convention.

**Use retrieval outcomes to generate selector-training examples.** The parametric path records which retrieved cases preceded a correct or incorrect answer. A Commonplace analogue would log which notes were loaded for a task and whether the outcome passed validation, then use that as weak supervision for retrieval ranking. Needs careful controls so "loaded during success" does not become false credit.

**Make activation policy explicit in environment variables.** `MEMORY_TOP_K`, `MEMORY_MAX_POS_EXAMPLES`, and `MEMORY_MAX_NEG_EXAMPLES` make read-back volume tunable. Commonplace generated context workflows could expose similar per-task budgets for positive evidence, counterexamples, and hard instructions. Ready where context packets are generated mechanically.

## Trace-derived learning placement

**Trace source.** AgentFly qualifies as trace-derived learning. The raw signals are benchmark question runs: planner outputs, executor results, tool-call history, final answers, ground-truth comparisons, and LLM-judge rationales in the CBR clients' result records. The memory rows keep only a smaller slice: question, generated plan, and reward or case label.

**Extraction.** Extraction is simple and mostly automatic. After each run, the non-parametric path appends the current question and plan to the memory pool with reward 1 or 0. The parametric path appends a positive or negative case row for the current query, and also writes training pairs connecting each retrieved case to whether the current answer was correct. A separate training script turns those pair records into a classifier checkpoint.

**Scope and timing.** Scope is benchmark-level, especially DeepResearcher-style question answering in the inspected code. Memory accumulation is online during batch processing. Parametric retriever improvement is staged: collect pair data, train the checkpoint offline, then use that checkpoint for later retrieval. The loop does not mine arbitrary user sessions or multi-project histories.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), AgentFly sits between trace-to-prose-case and trace-to-ranker systems. It strengthens the survey split between retained evidence and activation machinery: the JSONL cases are readable, but much of the behavior change comes from which cases the retriever chooses to push into the planner.

## Read-back placement

**Direction.** AgentFly uses push from the planner's perspective. The agent does not issue a memory query as an action; the host client retrieves cases from the current user query and inserts the resulting examples into `shared_history` before the planner call.

**Targeting and signal.** Targeting is `instance`: the client selects cases for the current benchmark query, not a generic always-load bundle. The signal is `inferred`, keyed on content rather than an assigned identifier: the non-parametric path uses SimCSE embedding similarity over case questions, and the parametric path uses a trained neural classifier over the current query and candidate case text, then sorts by predicted relevance score. Precision and recall are not established by code alone.

**Timing relative to action.** Read-back happens before task decomposition, not after execution. It can change the planner's first emitted subtask list, which then changes which tools the executor calls.

**Selection, scope, and complexity.** Selection is top-k by similarity or classifier score. Context volume is bounded by `MEMORY_TOP_K`, `MEMORY_MAX_POS_EXAMPLES`, and `MEMORY_MAX_NEG_EXAMPLES`; the global message history is also trimmed to a token ceiling before planner/executor calls. The loaded material is shallow: question plus plan, grouped as positive and negative examples. It does not recursively load source traces behind a case.

**Authority at consumption.** Memory arrives as advisory prompt context, phrased as examples to follow or avoid. It is not a hard validator, route table, or enforced planner constraint. Effective authority depends on the planner following the examples, which the code does not test at the individual case level.

**Faithfulness.** The repository has benchmark result logging and retriever training/evaluation metrics, but I did not find a faithfulness test that ablates a specific retrieved case, perturbs it, or verifies that the planner used the injected example.

**Other consumers.** Humans can inspect and edit the JSONL memory pool, training data, result logs, and retriever checkpoints. The same files serve as research evidence, selector-training material, and operational read-back state.

## Curiosity Pass

**The README says no fine-tuning, but the parametric path fine-tunes the selector.** The claim is accurate for the planner/executor LLMs; the memory subsystem itself can learn a neural retriever checkpoint.

**The positive/negative labels are answer-level, not plan-step-level.** A plan from a correct answer is treated as positive, and a plan from an incorrect answer is treated as negative. That is cheap supervision, but it can mislabel useful plans that failed because of execution, retrieval, tool, or final-answer issues.

**The memory rows are more compact than the traces that produced them.** That keeps read-back cheap, but it also drops the evidence needed to understand why a plan succeeded or failed.

**Parametric training credit assignment is weak.** `training_data.jsonl` labels retrieved cases by whether the current query was answered correctly, not by whether the individual retrieved case actually helped. The trained selector can still be useful, but the label semantics are noisy.

**Tool traces do not become tool policies.** The executor has a large MCP surface, yet the memory mechanism only conditions the planner. There is no retained rule like "for this task class, prefer search before crawling" except insofar as that pattern appears in remembered plans.

## What to Watch

- Whether memory rows gain provenance fields such as source result path, judge model, prompt version, retrieval score, and acceptance status; that would make trace-derived cases auditable rather than just reusable.
- Whether the system adds plan-step or tool-call-level credit assignment; that would distinguish bad plans from bad execution and make negative memory less noisy.
- Whether retriever training becomes part of the online loop rather than an external staged command; that would turn AgentFly into a tighter continual-learning system.
- Whether memory compression or pruning is implemented as the README TODO suggests; that would reveal whether the case bank remains an inspectable library or becomes a managed activation substrate.
- Whether personal/user memory appears in code; that would move the system beyond benchmark case replay into a broader agent-memory design.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - compares: AgentFly turns judged task runs into reusable cases and selector-training data.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: AgentFly separates JSONL cases, result traces, training pairs, prompt templates, and retriever weights by substrate, form, lineage, and authority.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: AgentFly's memory matters because the client actively retrieves and pushes cases into the planner prompt.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: AgentFly extracts future planning context from prior judged runs.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: selected cases and retriever checkpoints shape later planning even though the original JSONL rows are readable evidence.
