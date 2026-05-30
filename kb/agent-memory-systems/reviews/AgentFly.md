---
description: "Memento planner-executor agent that learns from judged benchmark runs by appending plan cases to JSONL memory and optionally training a neural case selector"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# AgentFly

AgentFly is the Agent-on-the-Fly team's research codebase for Memento, a planner-executor web/research agent that treats continual improvement as case-based memory rather than LLM fine-tuning. The checked-out implementation runs a meta-planner over user questions, delegates subtasks to an MCP-tool executor, judges benchmark answers against ground truth, appends the resulting plans into JSONL case memory, and offers both non-parametric and trained parametric case retrieval paths.

**Repository:** https://github.com/Agent-on-the-Fly/AgentFly

**Reviewed commit:** [42fbbcac63dd58ed6856c0761357345a58e4f032](https://github.com/Agent-on-the-Fly/AgentFly/commit/42fbbcac63dd58ed6856c0761357345a58e4f032)

## Core Ideas

**Planner-executor is the stable runtime boundary.** The base client asks a meta-planner to emit a JSON plan, then runs each step through an executor that can call MCP tools over stdio; completed task results are appended to shared history and fed back into the planner for up to three cycles ([client/agent.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/agent.py)). The tool layer is ordinary MCP packaging around search, crawling, documents, code execution, math, images, and video ([server/](https://github.com/Agent-on-the-Fly/AgentFly/tree/42fbbcac63dd58ed6856c0761357345a58e4f032/server)).

**Case memory is planner prompt conditioning, not a separate reasoning store.** The memory-bearing clients load JSONL cases, retrieve top-k similar cases for the current question, split them into positive and negative examples, then inject a generated prompt telling the planner to follow positive patterns and avoid negative ones ([client/no_parametric_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/no_parametric_cbr.py), [client/parametric_memory_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/parametric_memory_cbr.py)). The retained artifact is a question/case plus a plan string and label, not a note, tool, rule, or structured workflow.

**The non-parametric path recomputes embedding similarity over JSONL.** `memory/np_memory.py` loads JSONL, extracts key/value pairs, embeds every stored key and the query with a SimCSE-style transformer, ranks by dot product, and returns the original question/plan plus line index ([memory/np_memory.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/np_memory.py)). There is no persistent vector index; the storage substrate remains the JSONL file, with transformer embeddings as transient retrieval machinery.

**The parametric path trains a case selector, not the agent model.** `train_memory_retriever.py` builds a `MemoryRetrieverClassifier` over a transformer backbone by concatenating case text and natural query embeddings, training a binary classifier on `query`, `case`, `plan`, and `truth_label` records, and saving weights such as `best.pt` ([memory/train_memory_retriever.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/train_memory_retriever.py)). Runtime `CaseRetriever` loads those weights and scores each case for the current query ([memory/parametric_memory.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/parametric_memory.py)). This is distributed-parametric state, but only for retrieval/ranking; the planner and executor LLM weights are unchanged.

**Benchmark runs become both logs and future cases.** The benchmark clients read DeepResearcher questions, run the agent, ask an LLM judge to compare the final answer with ground truth, write a full result record under `../result/`, and append a smaller memory entry containing the question, plan, and reward or positive/negative case label ([client/no_parametric_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/no_parametric_cbr.py), [client/parametric_memory_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/parametric_memory_cbr.py)). The repo includes populated `memory.jsonl`, `dummy_memo.jsonl`, and `training_data.jsonl` files showing the expected case formats ([memory/](https://github.com/Agent-on-the-Fly/AgentFly/tree/42fbbcac63dd58ed6856c0761357345a58e4f032/memory)).

**Lifecycle is append-and-reload.** After each judged task, the non-parametric client appends to the configured memory JSONL and reloads it in process; the parametric client appends both a case-memory row and, when there were retrieved cases, training rows for later retriever training ([client/no_parametric_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/no_parametric_cbr.py), [client/parametric_memory_cbr.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/parametric_memory_cbr.py)). There is no deduplication, supersession, source invalidation, confidence decay, or automatic retraining trigger.

## Comparison with Our System

AgentFly and commonplace both keep behavior-shaping material outside the base LLM, but they choose different units and authority paths. AgentFly's storage substrate is JSONL plus optional PyTorch weights; commonplace's substrate is git-tracked markdown plus generated indexes. AgentFly's representational form is mixed: prose plan examples in JSONL and distributed-parametric retriever weights. Commonplace mostly uses prose and symbolic validation contracts.

The biggest alignment is that AgentFly treats prior work as prompt-time context, not as hidden model state. A future planner can act differently because prior benchmark attempts are retrieved and inserted before planning. That is a real memory system, but its addressable unit is the whole case row. There are no local titles, descriptions, links, statuses, or review states that a later agent can inspect independently.

The biggest divergence is lineage. AgentFly's full result records preserve rich traces, including planner outputs, executor steps, tool calls, judged answer, rationale, and reward; the active memory row keeps only the question and plan, plus a reward or case label. Commonplace spends much more machinery preserving why a retained artifact exists and how it should be invalidated. AgentFly's active case bank is cheaper, but a future agent cannot tell whether a useful-looking plan came from a robust success, a lucky answer, or a stale benchmark condition without consulting external result logs.

Behavioral authority also differs. The stored case row is a knowledge artifact when read as an example of past behavior. The generated memory prompt gives those examples stronger system-definition-artifact authority because it explicitly instructs the planner to follow positives and avoid negatives. The parametric retriever weights have ranking authority: they decide which examples enter that prompt, but they do not directly instruct or execute.

Where AgentFly is stronger is the closed benchmark loop. It can run many tasks, judge outcomes, append memory, and immediately reuse the enlarged case bank. Commonplace is stronger at durable curation: typed notes, link semantics, validation, archive status, and human-readable lifecycle controls. AgentFly is learning-oriented but thin on maintainability; commonplace is maintainable but does not yet have a comparable automated benchmark-to-memory ingestion loop.

**Read-back:** push — runtime retrieves similar case rows for the current question and injects them into the planner prompt.

## Borrowable Ideas

**Case rows as a workshop substrate.** Ready as a framing. A commonplace workshop could keep a JSONL or markdown table of task, attempted plan, outcome, and judge signal before deciding whether anything deserves promotion into a note or instruction.

**Positive/negative example prompting.** Ready for narrow eval loops. AgentFly's planner prompt uses both successful and failed cases, which is more useful than only retrieving "similar successes". For commonplace, this belongs in benchmarked workshop automation, not in the general library layer.

**Separate active memory from full trace logs.** Needs stronger lineage before adoption. AgentFly's split is useful: result logs are large, memory cases are compact. The missing piece for commonplace would be a stable pointer from each compact case back to the full trace, so the case can be audited before promotion.

**Train a retriever on observed retrieval usefulness.** Needs a use case first. The parametric path turns judged query/case outcomes into a learned case selector, which is a plausible future layer for large review corpora. Commonplace should not add this until lexical and structural navigation stop being enough.

**Keep planner memories at the plan level.** Ready as a constraint. AgentFly does not store whole answers as examples; it stores decompositions. For agent-operated KB work, retaining "how the task was broken down" may be a better reusable artifact than retaining a final response.

## Trace-derived learning placement

**Trace source.** AgentFly consumes benchmark task traces from DeepResearcher-style runs: the input question, planner JSON, executor task outputs, tool call records, final answer, ground truth, LLM-judge rationale, and correctness judgement. The trigger boundary is one completed benchmark question in `client/no_parametric_cbr.py` or `client/parametric_memory_cbr.py`.

**Extraction.** Extraction is intentionally narrow. From the full trace, the active case memory keeps the question and planner JSON, plus either a numeric reward in the non-parametric path or a positive/negative `case_label` in the parametric path. The oracle is an LLM judge comparing the predicted answer to stored ground truth. The parametric path also saves query/case/truth-label rows when retrieved cases were present, using the judged answer as training signal for future case ranking.

**Storage substrate.** Raw run records are JSONL result files outside the repo paths used by the scripts. Distilled active memory is JSONL under `memory/`. Parametric learning data is another JSONL file, and trained retriever state is a PyTorch model checkpoint written by `train_memory_retriever.py`. There is no database, graph store, or persistent vector store in the inspected code.

**Representational form.** The raw trace is mixed prose and symbolic JSON. The active case memory is prose/symbolic mixed form: natural-language questions and plan-step descriptions wrapped in JSON. The trained retriever is distributed-parametric state. The operative part for planner behavior is still prose examples in the prompt; the weights only rank which examples appear.

**Lineage.** The implemented lineage is run trace to judged result row to compact memory case, and optionally retrieved-case judgement rows to retriever checkpoint. That lineage is implicit in file conventions, not in stable IDs. A compact memory row does not carry a pointer to the result record that produced it, and retriever checkpoints do not encode which training-data snapshot produced them.

**Behavioral authority.** Result rows have knowledge-artifact authority: they are evidence and audit logs. Case rows have knowledge-artifact authority when stored, then system-definition-artifact authority once `build_prompt_from_cases` wraps them in planner guidance. Retriever weights have ranking authority because they select which cases shape the planner's next prompt.

**Scope.** The scope is benchmark and project local. Cases can generalize across questions in the same task distribution, but the code does not model projects, domains, source freshness, or cross-benchmark transfer boundaries.

**Timing.** Non-parametric memory updates online after each judged task and is reloaded immediately. Parametric retriever training is offline or staged: the run script appends training examples, while `train_memory_retriever.py` must be invoked separately to produce new weights.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), AgentFly is a trajectory-run artifact-learning system with an optional weight-learning ranking layer. It strengthens the survey's split between artifact learning and weight learning because both appear in one codebase: JSONL plans remain the prompt-visible learned artifact, while classifier weights only improve activation. It also weakens any simple "no fine-tuning" framing: the base LLM is not fine-tuned, but the memory selector can be.

## Curiosity Pass

**The README's "memory-based online reinforcement learning" language is stronger than the code path.** The implementation does append judged experiences and reuse them, but policy improvement is mostly retrieval-conditioned prompting. The only trained policy-like component is the optional case selector, and retraining is a manual script path rather than an online update in the main loop ([README.md](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/README.md), [memory/train_memory_retriever.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/train_memory_retriever.py)).

**The non-parametric retriever is simpler than the architecture language suggests.** It has no case bank service or index maintenance layer; it opens a JSONL file, embeds all keys, embeds the query, and ranks by similarity ([memory/np_memory.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/memory/np_memory.py)). That makes the mechanism inspectable, but it will scale poorly without a derived index.

**The memory artifact may be too lossy for audit.** The full result record contains enough evidence to debug a run, but the active memory row keeps only the plan and label. If a negative plan failed because an executor tool broke, the memory still treats that plan as a negative example. If a positive answer was lucky, the case still becomes positive. The system has no stored distinction between plan quality, execution quality, tool quality, and judge quality.

**The learned retriever's target is retrieval usefulness, not case truth.** `training_data.jsonl` rows label whether the overall answer was correct after using the retrieved cases, not whether an individual retrieved case was intrinsically relevant. This is pragmatic credit assignment, but noisy: all retrieved cases for a successful run get the same positive truth label, and all retrieved cases for a failed run get the same negative truth label.

**The local-server client is a separate deployment affordance, not a memory mechanism.** `agent_local_server.py` adds an OpenAI-compatible direct backend and tool-name patching for local models, but it does not implement the CBR memory loop ([client/agent_local_server.py](https://github.com/Agent-on-the-Fly/AgentFly/blob/42fbbcac63dd58ed6856c0761357345a58e4f032/client/agent_local_server.py)). It matters for adoption, not for retained-artifact design.

## What to Watch

- Whether the project adds stable lineage from compact memory cases back to full run records.
- Whether parametric retriever retraining becomes part of the run loop, with checkpoint versioning and evaluation gates.
- Whether memory entries start distinguishing planner failure from executor/tool failure.
- Whether the JSONL case bank gains deduplication, stale-case retirement, or domain scoping as it grows.
- Whether the repo adds a real persistent index for non-parametric retrieval or keeps recomputing embeddings over the whole case bank.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: AgentFly combines prompt-visible JSONL case artifacts with optional trained ranking weights from judged trajectories
- [deploy-time learning is the missing middle](../../notes/deploy-time-learning-is-the-missing-middle.md) - exemplifies: benchmark outcomes mutate a prompt-time memory substrate without changing the base LLM
- [oracle-strength spectrum](../../notes/oracle-strength-spectrum.md) - exemplifies: the LLM judge over ground-truth answers is stronger than self-report but weaker than deterministic task verification
- [axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - exemplifies: AgentFly separates storage substrate, representational form, lineage, and behavioral authority across JSONL cases, result traces, and retriever weights
- [a functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) - contrasts: AgentFly has an active workshop-like benchmark memory but no curated library promotion path
