---
description: "ExpeL review: benchmark agent that distills training trajectories into rules and retrieves prior trajectories as prompt few-shots"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-01"
---

# ExpeL

ExpeL, from LeapLabTHU's `ExpeL` repository, is the official implementation of the AAAI 2024 paper "ExpeL: LLM Agents are Experiential Learners." It is an experimental benchmark agent for HotpotQA, ALFWorld, WebShop, and FEVER that first gathers task trajectories, then extracts natural-language rules from those traces, and finally evaluates with extracted rules plus retrieved prior trajectories.

**Repository:** https://github.com/LeapLabTHU/ExpeL

**Reviewed commit:** [e41ec9a24823e7b560c561ab191441b56d9bcefc](https://github.com/LeapLabTHU/ExpeL/commit/e41ec9a24823e7b560c561ab191441b56d9bcefc)

**Last checked:** 2026-06-01

## Core Ideas

**The system is a three-stage experiment pipeline.** The README names three stages: experience gathering with `train.py`, insights extraction with `insight_extraction.py`, and evaluation with `eval.py` (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/README.md). The code follows that split: training saves agent checkpoints and text logs, insight extraction loads those checkpoints and creates rules per evaluation fold, and evaluation reloads the extracted insights before running held-out tasks (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/train.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/insight_extraction.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/eval.py).

**Raw experience is retained as task trajectories and checkpoints.** During training, `ExpelAgent.next_task` records each completed attempt as a `Trajectory` with task text, full trajectory text, parsed steps, and reflections, then separates successful and failed histories by task (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/memory/episode.py). `train.py` persists a plain log, a true log, and pickled agent dictionaries under the configured `logs/<benchmark>/expel/<run_name>` path using `save_trajectories_log` (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/train.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/utils.py).

**Rules are trace-distilled natural-language system advice.** `create_rules` compares successful and failed trajectories for the same task, also batches successful trajectories alone, prompts an LLM to emit `ADD`, `EDIT`, `REMOVE`, or `AGREE` operations, parses those operations, updates counters, sorts rules by counter strength, and stores a numbered `self.rules` string (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py). The prompt templates require generally applicable concise rules rather than trial-specific narration (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/templates/human.py). This is the central trace-derived learning mechanism.

**Evaluation pushes rules before the task prompt.** In evaluation mode, `insert_before_task_prompt` inserts the formatted rule template unless `no_rules` is set (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/eval.py). The rule templates describe the rules as experience or mandatory teacher insights, depending on benchmark (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/templates/human.py). From the acting agent's perspective, this is push read-back: the harness places memory in context before the next task action.

**Prior trajectories are retrieved into the few-shot slot.** During evaluation, `update_dynamic_prompt_components` builds a FAISS vector store over successful training trajectories and static few-shot examples, indexing tasks, thoughts, actions, steps, and reflections as `Document` objects (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py). It queries by task, thought, action, step, or rotating strategies, filters by environment, excludes the current task and overlong examples, optionally reranks by length or thought/task cosine similarity, and replaces the old few-shot examples in `prompt_history` with retrieved trajectories. This is engineered push activation because relevance-gated selection happens before an LLM call; the acting agent does not request the memory.

**Context efficiency is local and benchmark-oriented.** ExpeL manages context by limiting the number of few-shots to the current prompt's example count, filtering examples above `max_fewshot_tokens`, retrieving `num_fewshots * buffer_retrieve_ratio` candidates before filtering, truncating large failed-trial critique batches above 13,000 tokens, truncating reflection scratchpads above 12,000 tokens, and stopping trajectories when total history exceeds about 15,800 tokens (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/reflect.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/base.py). There is no global context budget or provenance-aware compaction layer; the controls are pragmatic safeguards around benchmark prompts.

## Artifact analysis

- **Storage substrate:** `files` — Local files under `logs/<benchmark>/expel/`: `.txt` logs, `_true.txt` full logs, and `.pkl` lists of serializable agent dictionaries (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/utils.py)
- **Representational form:** `mixed` — Mixed: prose trajectories in logs, symbolic Python dictionaries in pickle, and embedded prose fields for task histories and reflections

**Training logs and pickled checkpoints.** The storage substrate is local files under `logs/<benchmark>/expel/`: `.txt` logs, `_true.txt` full logs, and `.pkl` lists of serializable agent dictionaries (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/utils.py). The representational form is mixed: prose trajectories in logs, symbolic Python dictionaries in pickle, and embedded prose fields for task histories and reflections. Lineage is raw or lightly structured runtime trace capture from training tasks. Behavioral authority is mostly knowledge artifact authority until later scripts reload the checkpoint; once loaded by insight extraction or evaluation, the same records become learning input and retrieval substrate.

**`Trajectory` objects and in-agent histories.** The storage substrate is in-memory `succeeded_trial_history`, `failed_trial_history`, `past_reflections`, and checkpointed agent dictionaries (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py). The representational form is mixed prose and symbolic parsing: full trajectory text plus parsed thoughts, actions, observations, steps, and optional reflections (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/memory/episode.py). Lineage is direct task execution trace, split by success or failure. Behavioral authority is learning input for rule extraction and ranking input for few-shot retrieval; it is not itself a curated durable rule.

**Extracted rules.** The storage substrate is `rule_items`, `rule_items_with_count`, `cache_rules`, and the serialized agent dictionaries/logs saved by `insight_extraction.py` under `logs/<benchmark>/expel/extracted_insights` (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/insight_extraction.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py). The representational form is prose rules plus symbolic counters and fold cache keys. Lineage is trace-derived: successful-vs-failed comparisons and all-success batches are judged by an LLM, parsed into operations, and accumulated with counter updates. Behavioral authority becomes system-definition artifact authority when `RULE_TEMPLATE` pushes the numbered rules into the evaluation prompt as advice or mandatory insight.

**Few-shot retrieval index.** The storage substrate is an ephemeral FAISS vector store rebuilt inside `update_dynamic_prompt_components`, backed by LangChain `Document` objects created from static few-shots and successful trial histories (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py). The representational form is mixed: prose examples, symbolic metadata (`type`, `task`, `env_name`), and distributed-vector embeddings from the configured embedder (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/memory/__init__.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/configs/agent/expel.yaml). Lineage derives from static benchmark examples and successful training traces. Behavioral authority is ranking and selection influence: the index chooses which trajectories become prompt examples, but the examples carry the actual advisory force.

**Prompt templates and benchmark adapters.** The storage substrate is Python prompt modules under `prompts/` and Hydra YAML configs under `configs/` (https://github.com/LeapLabTHU/ExpeL/tree/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts, https://github.com/LeapLabTHU/ExpeL/tree/e41ec9a24823e7b560c561ab191441b56d9bcefc/configs). The representational form is authored prose instructions, few-shot examples, parser functions, and symbolic config. Lineage is authored benchmark harness code. Behavioral authority is system-definition authority over the base ReAct prompt, reflection prompt, critique prompt, rule read-back wording, action parsing, and retrieval settings.

**Promotion path.** ExpeL promotes runtime traces into behavior-shaping artifacts in two ways: failed/successful trajectories -> LLM critique operations -> counted rules -> rule prompt injection, and successful trajectories/reflections -> vector-indexed documents -> selected few-shot examples -> prompt replacement. The first path crosses from knowledge artifact evidence to prose system-definition advice. The second path keeps the raw trajectory form but adds ranking authority through embeddings and metadata filters.

## Comparison with Our System

| Dimension | ExpeL | Commonplace |
|---|---|---|
| Primary purpose | Benchmark experiential learning for task agents | Typed, agent-operated methodology knowledge base |
| Main substrate | Local logs, pickled checkpoints, prompt modules, ephemeral FAISS indexes | Git-tracked Markdown collections, type specs, source snapshots, generated indexes, review reports |
| Memory unit | Trajectories, reflections, extracted rules, retrieved few-shot examples | Notes, reviews, instructions, sources, ADRs, indexes |
| Learning path | Automatic LLM critique of traces into rules; successful traces retrieved as examples | Agent-authored artifacts under collection/type contracts, validation, review, and git lifecycle |
| Activation | Prompt-time rule push and relevance-gated few-shot push | Mostly explicit pull through `rg`, indexes, links, skills, and review workflows |
| Governance | Counter updates, fold splits, token filters, benchmark evaluation | Frontmatter schemas, collection contracts, validation, semantic review gates, citations |

ExpeL is much narrower than Commonplace but sharper on the experimental memory loop. Its artifacts are not a long-lived knowledge library; they are training-run outputs that exist to improve benchmark performance on related held-out tasks. That lets ExpeL make aggressive automatic promotions that would be too weakly governed for Commonplace methodology claims.

Commonplace is stronger on provenance, reviewability, and durable authority boundaries. ExpeL stores logs and checkpoints, but extracted rules do not carry item-level citations back to the exact trajectory pair or LLM judgment once they enter the prompt. Commonplace would normally keep source snapshots, type contracts, review state, and explicit promotion steps before turning a lesson into an instruction.

ExpeL is stronger on pre-action activation. It does not rely on the agent deciding to search memory: rules are inserted before the task prompt, and retrieved few-shots are selected and swapped into the prompt before LLM calls. That is exactly the storage-to-context step Commonplace often delegates to agent discipline.

**Read-back:** `both` — With static rule push and relevance-gated push activation for retrieved few-shot trajectories; script-level checkpoint loading is a non-agent pull path

### Borrowable Ideas

**Separate trace evidence from distilled rules.** Commonplace could keep workshop run traces as evidence artifacts and promote only concise, reviewed rules into instructions. Ready now as a workflow pattern; automatic promotion needs gates.

**Use operation-coded rule editing.** ExpeL's `ADD`, `EDIT`, `REMOVE`, `AGREE` interface is a compact way to ask an LLM to maintain a bounded rule set. Commonplace review sweeps could use this as an intermediate proposal format, with human or semantic-gate acceptance before durable writes.

**Retrieve examples into an existing prompt slot.** Instead of inventing a new memory pane, ExpeL replaces the few-shot examples the base agent already expects. Commonplace could apply this to review workers by swapping a small set of prior analogous reviews into a fixed "examples" slot. Ready for a narrow experiment.

**Keep activation budgets visible at the selection point.** ExpeL filters retrieved few-shots by token count before insertion. Commonplace should attach explicit budgets to any push-memory injector, preferably with source path and expiry included in each selected item.

**Do not borrow pickle checkpoints as durable knowledge.** They are practical for experiments but poor as a reviewable memory substrate. Commonplace should preserve inspectable Markdown, JSON, or SQLite records with schema and provenance if it adopts similar trace loops.

## Trace-derived learning placement

**Trace source.** ExpeL qualifies as trace-derived learning. Raw traces are task trajectories from benchmark interactions: prompts, thoughts, actions, observations, success/failure outcomes, reflections, and serialized agent state saved by `train.py` (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/train.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py).

**Extraction.** The extraction oracle is an LLM critique prompt. For paired successful and failed trials, the prompt asks for general high-level critiques that avoid similar failures; for successful-trial batches, it asks for generally applicable tips. The LLM must emit bounded operations over the existing rule list, and `parse_rules` plus `update_rules` turns those operations into a counted, sorted rule set (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/templates/human.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py).

**Four fields.** The raw stage persists in local log and pickle files; its representational form is prose trajectories plus symbolic checkpoint fields; lineage is direct task execution; behavioral authority is evidence and learning input. The distilled stage persists as rule lists, counters, fold caches, and extracted-insight checkpoints; its representational form is prose with symbolic counters; lineage is LLM-derived from selected traces; behavioral authority is prompt-level system-definition advice during evaluation. The retrieval stage keeps successful trajectories in their raw prose form but adds vector and metadata ranking authority.

**Scope and timing.** Scope is per benchmark run and per evaluation fold. Training accumulates traces online during task execution; insight extraction is an offline/staged distillation pass; evaluation performs online read-back before and during held-out task execution.

**Survey placement.** ExpeL is a clean example of trace-to-natural-language-rule learning plus trace-to-example retrieval. It strengthens the survey distinction between raw trace retention and distilled behavioral artifacts: the rules are new system-definition artifacts, while retrieved trajectories are still knowledge artifacts selected into a high-authority prompt channel.

## Read-back placement

**Direction.** Read-back is both push and script-level pull. Acting agents receive rules and retrieved few-shots by push during prompt construction; scripts pull checkpoints and extracted-insight runs from disk through `load_trajectories_log` (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/eval.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/utils.py).

**Trigger and relevance signal.** Rule read-back is fold-scoped and unconditional unless `no_rules` is set. Few-shot read-back is relevance-gated: the system builds a FAISS index over candidate documents filtered by environment and document type, queries by task/thought/action/step depending on `fewshot_strategy`, retrieves a buffered top-k, excludes current-task and overlong trajectories, and optionally reranks by length or cosine similarity over thoughts/tasks (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/configs/agent/expel.yaml). This justifies `push-activation`.

**Timing relative to action.** Rules are inserted before the task prompt when the evaluation agent resets. Few-shots can be replaced before an LLM call because `prompt_agent` calls `update_dynamic_prompt_components` before invoking the model (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/react.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py). Reflections during training are also pushed before retrying the same task, but those are per-task recovery memory rather than the main cross-task ExpeL artifact.

**Selection, scope, and complexity.** Selection is bounded by the number of base few-shots, `buffer_retrieve_ratio`, `max_fewshot_tokens`, environment filters, duplicate-task filters, and optional reranking. Complexity can still be high because whole trajectories are inserted as examples rather than compressed into smaller cited fragments.

**Authority at consumption.** Rules have advisory-to-instructional system-definition authority because they are inserted through benchmark rule templates before task work. Retrieved trajectories have example authority: they do not state rules directly, but they shape behavior as demonstrations in the prompt. The vector store has ranking authority rather than direct instruction authority.

**Faithfulness.** The repository evaluates task success with and without configurable rule loading, but I did not find item-level ablations proving that a specific extracted rule or retrieved trajectory caused a specific behavioral change. Structural activation is implemented; effective per-memory influence is not verified from code.

**Other consumers.** Humans can inspect text logs and visualizations, and scripts reload pickled checkpoints. These are experiment-consumer surfaces, not an interactive memory API for a deployed assistant.

## Curiosity Pass

**The durable "memory" is mostly run artifacts.** ExpeL's retained state lives in logs and pickled agent dictionaries, not in a service, database, or versioned knowledge library. That matches its benchmark reproduction role but limits independent inspection and governance.

**The configured retriever class is not the read-back path I found.** The config exposes `retriever_type: knn`, and the constructor accepts `retriever_cls`, but `update_dynamic_prompt_components` builds a FAISS vector store directly (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/configs/agent/expel.yaml, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py). The implemented mechanism is FAISS-based retrieval, not a configurable LangChain retriever swap.

**Rule limits are softer than the name suggests.** `max_num_rules` affects the critique suffix and `list_full` behavior at `max_num_rules + 5`, but the code does not simply cap the final list at that number (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py). It is a pressure mechanism, not a hard schema.

**Evaluation may regenerate rules or load cached fold rules.** `eval.py` calls `create_rules` at fold boundaries, with `load_cache_rules` deciding whether to load cached rules by fold (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/eval.py). That makes lineage dependent on how the run is invoked.

**FEVER looks less complete than the other benchmark paths.** The prompt registry has `None` or a misspelled key in some FEVER critique/reflection entries, while the README examples focus on ALFWorld, WebShop, and HotpotQA (https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/__init__.py, https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/README.md). I would treat FEVER support as less code-confirmed for the full ExpeL rule-extraction path.

## What to Watch

- Whether future ExpeL-style systems preserve item-level provenance from each rule back to the exact trajectory pair, LLM output, and fold. That is the missing bridge from benchmark learning to auditable memory.
- Whether trajectory retrieval moves from whole-example insertion to cited snippet selection or summaries. That would reduce context complexity while preserving relevance-gated activation.
- Whether rule extraction gains validation before prompt authority, such as contradiction checks, held-out ablations, or human acceptance. That determines whether trace-derived rules can safely become durable instructions.
- Whether checkpoint storage moves from pickle to structured, inspectable artifacts. That matters if this design is adapted beyond reproducible experiments.
- Whether the retrieval path uses one persistent index per fold instead of rebuilding FAISS during prompt updates. That would change the artifact analysis from ephemeral ranking state to a durable retrieval artifact.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: ExpeL turns task trajectories into natural-language rules and retrieval-selected examples.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: ExpeL actively inserts rules and retrieved examples before action.
- [Activate Behavior-Changing Memory Before The Mistake](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: evaluation read-back happens before task decisions.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: ExpeL separates logs, trajectories, rules, vector indexes, and prompt templates by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes: raw trajectories and logs serve as evidence, examples, and learning input.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: extracted rules, prompt templates, parser code, and retrieval settings shape future behavior.
