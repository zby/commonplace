---
description: "ExpeL review: staged trajectory gathering, rule mutation, and prompt-time trajectory retrieval for benchmark agent learning"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# ExpeL

ExpeL is LeapLabTHU's AAAI 2024 research implementation of an LLM agent that learns from benchmark experience. The code is organized as a three-stage pipeline: `train.py` gathers ReAct/Reflexion-style trajectories, `insight_extraction.py` distills those trajectories into a maintained natural-language rule list, and `eval.py` evaluates with both rules and retrieved trajectory examples available in the prompt. The reviewed system is therefore not a general repository-backed memory system; it is a benchmark-oriented trace-to-prompt-artifact learning loop.

**Repository:** https://github.com/LeapLabTHU/ExpeL

**Reviewed commit:** [e41ec9a24823e7b560c561ab191441b56d9bcefc](https://github.com/LeapLabTHU/ExpeL/commit/e41ec9a24823e7b560c561ab191441b56d9bcefc)

**Last checked:** 2026-05-16

## Core Ideas

**Learning is staged around persisted run logs.** `train.py` creates an `ExpelAgent`, runs each benchmark task, records prompt-visible history and fuller history, then writes `.txt`, `_true.txt`, and `.pkl` files under `logs/<benchmark>/expel/<run_name>` through `save_trajectories_log(...)` ([train.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/train.py), [utils.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/utils.py)). `insight_extraction.py` loads the saved pickle, reconstructs the agent state, splits tasks into folds, and calls `create_rules(...)` over each training fold ([insight_extraction.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/insight_extraction.py)). `eval.py` then loads an extracted-insights run and either recreates rules per fold or loads cached fold rules before evaluation ([eval.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/eval.py)). The storage substrate is local files, not a service or database.

**Raw traces are kept separately from distilled rules.** During training, `ExpelAgent.next_task()` converts the current prompt log into a `Trajectory` object and appends it to `succeeded_trial_history` or `failed_trial_history`; failed task indexes are tracked separately ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py), [memory/episode.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/memory/episode.py)). `Trajectory` parses the retained text into observations, actions, thoughts, steps, optional reflections, and optional embedding keys. These traces are knowledge artifacts when reused as examples or evidence: they show what happened, but they do not by themselves instruct later behavior.

**The distinctive learned artifact is a scored flat rule list.** `create_rules(...)` compares successful and failed trajectories, chunks successful trajectories, prompts a critique model with the current rule list, parses `ADD`, `EDIT`, `REMOVE`, and `AGREE` operations, and applies them to `rule_items_with_count` ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py), [prompts/templates/human.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/templates/human.py)). `update_rules(...)` gives added rules an initial count, increments agreed or edited rules, decrements removed rules, drops rules at zero, and sorts by count. This is a symbolic system-definition artifact: at evaluation time it is injected ahead of the task as an instruction or strong guidance surface through benchmark-specific `RULE_TEMPLATE`s.

**The rule mutation protocol is deliberately narrow.** The prompt asks for at most four operations, bans trial-specific wording, and frames rules as generally applicable tips for future Thought and Action ([prompts/templates/human.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/templates/human.py)). The parser only accepts operation lines matching a simple regex and ending in a period; the updater drops malformed edits, additions that duplicate existing rules, and operations targeting nonexistent rules ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py)). This is lightweight governance, but it is real governance: the LLM proposes mutations and code applies a constrained state transition.

**Prompt-time trajectory retrieval remains separate from rule learning.** For evaluation, `setup_vectorstore()` turns successful trajectories and static fewshots into LangChain `Document`s typed as `task`, `thought`, `step`, `action`, or `reflection`, with environment metadata. `update_dynamic_prompt_components()` builds a FAISS store over one selected slice, retrieves candidates by the current task or step context, optionally reranks them, filters overlong/self/duplicate examples, and replaces the fewshot block already present in the prompt ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py), [memory/__init__.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/memory/__init__.py), [configs/agent/expel.yaml](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/configs/agent/expel.yaml)). The behavior-shaping mechanism is mixed: prose exemplars are the operative knowledge artifacts, while embeddings and FAISS are a transient ranking surface.

**Reflexion is embedded as an inner loop, not the final memory.** `ReflectAgent` can reflect between failed attempts on the same task, keeps `reflections`, and inserts formatted reflections before retrying ([agent/reflect.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/reflect.py)). ExpeL's distinctive step is later: those reflections and trajectories become source material for fold-level rule extraction and trajectory retrieval.

## Comparison with Our System

| Dimension | ExpeL | Commonplace |
|---|---|---|
| Primary purpose | Improve benchmark agents from repeated task traces | Maintain an agent-operated methodology KB |
| Raw substrate | Local text logs and pickled agent dictionaries | Git-tracked sources, notes, instructions, reviews, indexes |
| Distilled artifact | Scored flat natural-language rule list | Typed notes, ADRs, instructions, schemas, commands, review artifacts |
| Retrieval surface | Runtime FAISS over task/thought/step/action/reflection documents | `rg`, generated indexes, authored links, descriptions, skills |
| Lineage | Fold/run files preserve source traces, but individual rules do not cite source trajectories | Source links, reviewed revisions, frontmatter, archive/replacement lifecycle |
| Behavioral authority | Rules instruct or strongly guide; retrieved trajectories advise by example | Knowledge artifacts advise; system-definition artifacts instruct, validate, route, or enforce |
| Lifecycle | `ADD`/`EDIT`/`REMOVE`/`AGREE` plus counters; no review status or per-rule provenance | Status fields, validation, review gates, archives, curated navigation |

ExpeL is stronger than commonplace at automatic consolidation from repeated executions. Its mutation language and counters give a small, inspectable artifact a lifecycle: rules can be added, strengthened, rewritten, weakened, and removed without whole-document rewriting.

Commonplace is stronger on durable provenance and compositionality. ExpeL's learned rule list is flat text with counts; the source traces remain in run artifacts, but a rule does not carry explicit citations, confidence, review state, invalidation conditions, or links to related rules. That is acceptable for benchmark folds with strong success signals and short artifacts, but weak for a long-lived KB.

The key authority distinction is that ExpeL has two future-behavior channels. Retrieved trajectories are knowledge artifacts: they act as examples and evidence in the prompt. The distilled numbered rules are system-definition artifacts in the eval path: the prompt says to use or follow them, and they are maintained by a rule-update protocol.

## Borrowable Ideas

**Separate trace gathering from consolidation.** Ready now as a workflow pattern. ExpeL makes raw runs first-class, then mines them later. Commonplace's workshop layer should preserve that separation: capture work traces cheaply, then promote only after a separate consolidation pass.

**Use explicit mutation verbs for LLM-maintained artifacts.** Ready for narrow lists. `ADD`/`EDIT`/`REMOVE`/`AGREE` is much easier to audit than asking a model to rewrite a whole artifact. Commonplace could borrow the verb contract for generated candidate lists, warning queues, or review triage, while still requiring human or validation gates before high-authority promotion.

**Keep counters separate from truth.** Useful but needs care. ExpeL's counts measure repeated support in a benchmark extraction loop, not epistemic correctness. The pattern is borrowable as an activation or priority signal, not as proof.

**Index one trace pool by multiple slices.** Needs a concrete use case. ExpeL's task/thought/step/action/reflection split is a good reminder that one retained trace can support several retrieval views. Commonplace could apply the same idea to work logs, but authored notes and links should remain the canonical library layer.

**Do not borrow source-less rule promotion for durable KB claims.** ExpeL's rule list is appropriately lightweight for prompt guidance. It is not enough for methodology notes where a future agent must audit source lineage and scope.

## Trace-derived learning placement

**Trace source.** ExpeL clearly qualifies as trace-derived learning. The source traces are completed benchmark task attempts across HotpotQA, ALFWorld, WebShop, and FEVER: prompt histories, thoughts, actions, observations, reflections, success/failure outcomes, and fold membership. Trigger boundaries are task attempts during `train.py`, fold boundaries during `insight_extraction.py`, and eval folds during `eval.py`.

**Extraction.** Extraction is LLM critique plus code-constrained mutation. Successful and failed trials are compared per task, successful trials are chunked across training IDs, and the LLM proposes operations against the current rule list. The benchmark environment's success signal decides which traces are successful or failed; the LLM acts as the abstraction judge when turning those traces into general rules.

**Storage substrate.** Raw traces and agent state persist as local `.txt`, `_true.txt`, and `.pkl` files under `logs/<benchmark>/expel/`. Extracted-insight runs live under `logs/<benchmark>/expel/extracted_insights/`, with fold subdirectories for resume checkpoints. During evaluation, retrieved trajectory examples are rebuilt into in-memory `Document`s and a FAISS vectorstore; rules live in pickled agent dictionaries and in prompt strings.

**Representational form.** The raw trajectories are prose-plus-symbolic logs: text messages with task, thought, action, observation, and reflection structure. Distilled rules are prose with symbolic operation metadata during mutation and numeric counters during maintenance. Retrieval adds distributed-parametric embeddings, but the learned artifact is not model weights.

**Lineage.** The run-level lineage is recoverable through log directories, run names, fold IDs, saved dictionaries, and the `critique_summary_log`. Per-rule lineage is weak: after `update_rules(...)`, a rule is text plus count, not a cited object pointing to the successful/failing trajectories that produced or edited it. The FAISS trajectory retrieval path keeps stronger lineage because each selected fewshot still resolves to a stored task trajectory in `combined_history`.

**Behavioral authority.** Raw trajectories and retrieved fewshots are knowledge artifacts: they advise by example. Reflections are task-local knowledge artifacts while retrying. The rule list is a system-definition artifact in evaluation because `insert_before_task_prompt()` injects it through templates that tell the agent to use or follow the learned insights. Embeddings and FAISS carry ranking authority over which examples enter the prompt, but they do not become canonical memory.

**Scope.** Learning is benchmark-family local. Configs choose a benchmark and rule template, folds are over that benchmark's task set, and there is no code path showing cross-benchmark rule transfer.

**Timing.** The durable learning loop is offline and staged: gather traces, extract insights, evaluate. Within-task Reflexion is online during a task, but it is not the durable cross-task learned artifact.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), ExpeL sits in the trajectory-run ingestion pattern and the symbolic-artifact learning branch. Its artifact subtype is scored flat rules with explicit mutation verbs, plus a separate prompt-time trajectory-exemplar retrieval surface. It strengthens the survey's distinction between raw trace replay, retrieved exemplars, and distilled system-definition artifacts; it does not require a new survey subtype.

## Curiosity Pass

The README describes an agent that recalls extracted insights and past experiences, and the implementation supports that claim, but the recall path is entirely prompt construction. Experience changes what the agent reads; it does not change model weights, tools, environment APIs, or a typed long-term store.

The strongest design element is the rule mutation protocol, not the use of embeddings. The embedding retrieval path is ordinary fewshot selection over traces; `ADD`/`EDIT`/`REMOVE`/`AGREE` with counters is the part that gives a natural-language artifact an inspectable maintenance loop.

The weakest design element is rule lineage. ExpeL keeps enough run artifacts to audit a fold manually, but the rule object itself does not remember why it exists. That makes decay and editing cheap, but makes later trust expensive.

The code has both older standalone critique helpers and the main `create_rules(...)` path. The review treats `create_rules(...)` plus `train.py`/`insight_extraction.py`/`eval.py` as authoritative because that is the staged pipeline documented and wired through the scripts.

## What to Watch

- Whether ExpeL descendants attach per-rule provenance, confidence, or source-trace citations without losing the simple mutation protocol.
- Whether the CRUD-style rule lifecycle works when the oracle is weaker than benchmark success/failure.
- Whether retrieved trajectories remain more behaviorally influential than distilled rules, especially when rules are abstract or under-cited.
- Whether fold-local rule sets can transfer across benchmark families or whether each domain needs its own prompt template and extraction loop.
- Whether future systems combine ExpeL-style rule mutation with stronger typed artifacts such as executable skills, validators, or repository-backed instructions.

## Bottom Line

ExpeL is one of the cleanest code-grounded examples of trace-derived symbolic artifact learning: benchmark trajectories are gathered, compared, distilled into a scored rule list, and combined with retrieved trajectory exemplars at evaluation time. Its lesson for commonplace is not to imitate the flat rule store wholesale, but to borrow the separation between traces and promotion plus the explicit mutation language for narrow, reviewable maintenance loops.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: ExpeL anchors the scored-flat-rule, CRUD-verb branch of trajectory-derived artifact learning.
- [Reflexion](./reflexion.md) - sharpens: ExpeL embeds Reflexion-style task retries but adds cross-task consolidation and rule maintenance.
- [ReasoningBank](./reasoning-bank.md) - compares-with: both extract from successes and failures, but ReasoningBank stores structured append-only memory items while ExpeL mutates a counted rule list.
- [G-Memory](./g-memory.md) - compares-with: both maintain natural-language rules with mutation verbs and prompt injection, while G-Memory adds a multi-agent task graph.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: ExpeL's trajectories and retrieved examples advise by evidence and example.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: ExpeL's injected rules carry instruction-like authority at evaluation time.
- [Memory management policy is learnable but oracle-dependent](../../notes/memory-management-policy-is-learnable-but-oracle-dependent.md) - qualifies: ExpeL's lifecycle depends on a strong benchmark oracle and LLM critique quality.
