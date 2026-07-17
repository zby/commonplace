---
description: "ExpeL review: trace-learning benchmark agent that distills task trajectories into rules and retrieves prior trials as few-shots"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-learning]
last-checked: "2026-06-04"
---

# ExpeL

ExpeL, from LeapLabTHU's `ExpeL` repository, is the official implementation of the AAAI 2024 paper "ExpeL: LLM Agents are Experiential Learners." It is a benchmark agent pipeline for HotpotQA, ALFWorld, WebShop, and FEVER that gathers task trajectories, distills them into natural-language rules, and evaluates held-out tasks with those rules plus dynamically retrieved prior trajectories.

**Repository:** https://github.com/LeapLabTHU/ExpeL

**Reviewed commit:** [e41ec9a24823e7b560c561ab191441b56d9bcefc](https://github.com/LeapLabTHU/ExpeL/commit/e41ec9a24823e7b560c561ab191441b56d9bcefc)

**Source directory:** `related-systems/ExpeL`

## Core Ideas

**The system is a staged experiential-learning experiment.** The README presents three operational stages: experience gathering with `train.py`, insight extraction with `insight_extraction.py`, and evaluation with `eval.py` ([README.md](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/README.md)). The code follows that split: training saves logs and serializable agent dictionaries, insight extraction reloads training histories and creates fold-specific rules, and evaluation reloads those artifacts before running held-out tasks ([train.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/train.py), [insight_extraction.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/insight_extraction.py), [eval.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/eval.py)).

**Raw experience is retained as trajectories, reflections, and checkpoints.** `ExpelAgent.next_task()` turns each completed training attempt into a `Trajectory` carrying task text, trajectory text, parsed thoughts/actions/observations/steps, and reflections, then stores it in success or failure histories by task ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py), [memory/episode.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/memory/episode.py)). `save_trajectories_log()` persists text logs, true logs, and pickled agent dictionaries under the configured log path ([utils.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/utils.py)).

**Rules are LLM-maintained distillations over stored traces.** `create_rules()` compares successful and failed trajectories for the same training task and also batches successful trajectories alone, asks the LLM for `ADD`, `EDIT`, `REMOVE`, or `AGREE` operations over the existing rule list, parses those operations, updates counted rule items, sorts by counter strength, and renders a numbered rules string ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py)). The critique templates explicitly demand general, concise rules rather than trial-specific narration ([prompts/templates/human.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/templates/human.py)).

**Evaluation receives rules without asking for them.** During evaluation, `insert_before_task_prompt()` appends the benchmark-specific rule template before the task prompt unless `no_rules` is set, and `eval.py` creates or loads the rule set at fold boundaries ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py), [eval.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/eval.py)). The rule templates frame rules as experiences or, for FEVER, mandatory teacher insights ([prompts/templates/human.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/templates/human.py)).

**Successful trajectories are retrieved into the few-shot slot.** In evaluation, `update_dynamic_prompt_components()` builds a FAISS vector store over static few-shots and successful training trajectories, indexes task/thought/action/step/reflection documents with metadata, queries by the configured strategy, filters by environment, current task, duplicate task, and token length, optionally reranks, then replaces the old few-shot examples inside `prompt_history` before the model call ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py), [configs/agent/expel.yaml](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/configs/agent/expel.yaml)).

**Context efficiency is bounded but local.** ExpeL limits few-shot count to the base prompt's example count, filters retrieved examples above `max_fewshot_tokens`, retrieves a buffered candidate set, truncates oversized failed-trial critique batches, truncates reflection scratchpads, and halts long trajectories through the base agent's prompt loop ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py), [agent/reflect.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/reflect.py), [agent/react.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/react.py)). There is no durable global context planner; the controls are benchmark-prompt safeguards around rule and example insertion.

## Artifact analysis

- **Storage substrate:** `files` - The durable retained state is local files under the configured run log directory: text logs, true logs, and pickle checkpoint lists. In-memory histories and ephemeral FAISS indexes shape the run, but the persisted memory surface inspected here is file-based.
- **Representational form:** `prose` `symbolic` `parametric` - Trajectories, reflections, examples, prompts, and rules are prose; task histories, counters, cache keys, fold metadata, configs, and pickled dictionaries are symbolic; retrieved examples are selected through embeddings and FAISS similarity during evaluation.
- **Lineage:** `authored` `imported` `trace-extracted` - Prompt templates, configs, parsers, and benchmark adapters are authored; static benchmark few-shots are imported into the candidate pool; trajectories, reflections, extracted rules, counters, and retrieved examples derive from task execution traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` - Logs and trajectories serve as evidence and examples; extracted rules and prompts instruct later agents; Hydra configs and benchmark adapters route behavior; parsers and success functions validate task outcomes; embeddings, filters, rerankers, and counters rank candidate memories; critique prompts learn rules from traces.

**Training artifacts.** `train.py` writes run logs and serializable dictionaries after each task attempt, while `load_trajectories_log()` later reads those files back for resume, insight extraction, or evaluation ([train.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/train.py), [utils.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/utils.py)). The text logs are readable evidence; the pickled dictionaries are pragmatic checkpoints rather than reviewable knowledge artifacts.

**In-agent trajectory histories.** `succeeded_trial_history`, `failed_trial_history`, `past_reflections`, `rule_items`, `rule_items_with_count`, and `cache_rules` are the run-time working memory that gets serialized into dictionaries where the scripts save checkpoints ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py)). These objects are knowledge artifacts while retained as traces and learning inputs when consumed by rule extraction or retrieval.

**Extracted rules.** The strongest behavior-shaping artifact is the numbered `self.rules` string plus its counted source list. Rules are derived from LLM operations over successful and failed training trajectories, cached per fold when requested, and inserted into later evaluation prompts ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py), [insight_extraction.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/insight_extraction.py)). Their authority changes from learned prose advice to prompt-level system-definition instruction when the rule template is appended before a task.

**Few-shot retrieval state.** `setup_vectorstore()` and `update_dynamic_prompt_components()` derive LangChain `Document` objects and a FAISS index from successful trajectories and static examples, but rebuild that index inside the prompt-update path rather than preserving it as a durable index file ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py)). The retained artifact is the source trajectory/example text; the vector store has ranking authority for the current call.

**Prompt templates and adapters.** Python prompt modules and Hydra configs define the base ReAct prompt, reflection prompt, critique prompt, rule-injection wording, parsing functions, retrieval strategy, buffer ratio, reranker, and token bounds ([prompts/templates/human.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/templates/human.py), [prompts/__init__.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/__init__.py), [configs/agent/expel.yaml](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/configs/agent/expel.yaml)). These authored artifacts carry system-definition authority even before any trace-derived memory exists.

Promotion path: task execution -> trajectory/reflection checkpoint -> LLM critique operations -> counted rule list -> prompt insertion; and successful trajectory -> embedded retrieval candidate -> selected few-shot -> prompt replacement. The first path turns trace evidence into distilled instruction. The second keeps raw examples but gives them ranking and prompt-example authority.

## Comparison with Our System

| Dimension | ExpeL | Commonplace |
|---|---|---|
| Primary purpose | Benchmark experiential learning for task agents | Typed methodology KB and framework for agent-operated knowledge bases |
| Main substrate | Local logs, pickle checkpoints, prompt/config files, ephemeral FAISS indexes | Git-tracked Markdown collections, type specs, source snapshots, generated indexes, review reports |
| Memory unit | Trajectories, reflections, extracted rules, retrieved few-shot examples | Notes, reviews, instructions, sources, ADRs, indexes |
| Learning path | Automatic LLM critique of task traces into rules; successful traces retrieved as examples | Agent-authored artifacts under collection/type contracts, validation, semantic review, and git lifecycle |
| Read-back | Prompt-time push plus script-level loading by run/fold | Mostly explicit pull through `rg`, indexes, links, skills, and review workflows |
| Governance | Counter updates, fold splits, token filters, benchmark success metrics | Frontmatter schemas, collection contracts, citations, validation, semantic review gates, archive lifecycle |

ExpeL is narrower than Commonplace but much more direct about the trace-to-action loop. Its artifacts are experiment outputs built to improve held-out benchmark performance, so it can turn traces into prompt advice without a durable editorial lifecycle. Commonplace is slower but more auditable: claims, instructions, and reviews remain inspectable Markdown with type contracts, source links, validation, and replacement history.

The useful divergence is activation. ExpeL does not rely on the acting agent to remember to search: evaluation rules are inserted before the task, and relevant trajectories replace examples before LLM calls. That is exactly the step Commonplace often leaves to agent discipline.

ExpeL is weaker on provenance and durable governance. A rule can be traced to an extraction run in broad terms, but the persisted prompt-facing rule does not carry item-level citations back to exact trajectory pairs, LLM operation text, fold, and acceptance evidence. That is acceptable for a benchmark experiment and risky for a maintained methodology KB.

### Borrowable Ideas

**Separate raw traces from distilled rules.** Commonplace could keep workshop run traces as evidence while promoting only reviewed lessons into instructions. Ready as a workflow pattern; automatic promotion needs validation and review gates.

**Use operation-coded rule maintenance.** ExpeL's `ADD` / `EDIT` / `REMOVE` / `AGREE` interface is a compact intermediate format for maintaining a bounded lesson list. Commonplace could use it for proposal generation in review sweeps, with acceptance handled by semantic QA or a maintainer.

**Retrieve examples into an existing prompt slot.** ExpeL improves context compatibility by replacing the few-shot examples the base agent already expects. Commonplace could test a fixed "analogous prior reviews" slot for review workers rather than inventing another memory pane.

**Keep activation budgets at the insertion point.** ExpeL filters retrieved examples by token count before insertion. Commonplace should attach explicit token budgets, source paths, and expiry to any future push-memory injector.

**Do not borrow pickle checkpoints as durable knowledge.** Pickle is convenient for reproducing experiments, but it is a poor inspectable substrate for a governed KB. Commonplace should prefer Markdown, JSON, SQLite, or other schema-visible records for trace-derived state.

## Write side

**Write agency:** `automatic` `manual` - ExpeL automatically records trajectories during training, extracts and updates rules through LLM critique operations, caches fold rules, and writes logs/checkpoints; manual agency remains in authored prompts, configs, benchmark setup, run selection, and optional operator choices such as `no_rules` or cache loading.

**Curation operations:** `dedup` `evolve` `synthesize` `promote` - Rule maintenance rejects duplicate additions, supports LLM-requested removal of duplicated/similar rules, edits existing rule text, synthesizes new general rules from multiple stored trajectories, and promotes/demotes rules by counters and sorted prompt order. I did not find retained-history invalidation, age-based decay, or automatic consolidation into summaries.

### Trace-learning

**Trace source:** `trajectories` - The raw signal is benchmark task execution: task text, thoughts, actions, observations, success/failure outcome, reflections, and serialized agent state captured during training.

**Learning scope:** `per-task` `cross-task` - Rule extraction compares success and failure trajectories for a training task, then the resulting rules and retrieved examples are used across held-out tasks within benchmark folds.

**Learning timing:** `online` `offline` `staged` - Training accumulates traces online; `insight_extraction.py` performs an offline/staged distillation pass; `eval.py` can create or load fold rules before evaluation and performs prompt-time retrieval during action.

**Distilled form:** `prose` `symbolic` `parametric` - Distillation yields natural-language rules and example trajectories, symbolic counters/cache keys/fold metadata, and embedding-backed retrieval state for selecting examples.

The extraction oracle is an LLM prompted to compare successful and failed trials or inspect successful-trial batches, then emit bounded operations over the rule list ([prompts/templates/human.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/templates/human.py)). `parse_rules()` and `update_rules()` are the symbolic acceptance layer: malformed or duplicate operations are filtered, counters are adjusted, low-count rules can disappear, and surviving rules are sorted for later insertion ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py)).

Survey fit: ExpeL is a clean trace-to-natural-language-rule system with a second trace-to-example retrieval path. It strengthens the distinction between raw trace retention and distilled behavior-shaping artifacts: rules become system-definition advice, while retrieved trajectories remain knowledge artifacts selected into a high-authority prompt position.

## Read-back

**Read-back:** `both` - Scripts explicitly load saved runs, folds, and checkpoints by path/run name, while acting evaluation agents receive retained rules and retrieved trajectories through prompt construction before model calls.

**Read-back signal:** `coarse` `identifier` `inferred / embedding` - Rule insertion is coarse within the current evaluation fold; few-shot retrieval filters by environment and document type metadata, then selects examples by embedding similarity over task, thought, action, step, or reflection content.

**Faithfulness tested:** `no` - The repository supports benchmark evaluation and a `no_rules` switch, but I did not find item-level with/without ablations or post-action audits proving that a specific inserted rule or retrieved trajectory caused a specific behavior.

The push path is pre-invocation. `ReactAgent.prompt_agent()` calls `update_dynamic_prompt_components()` before invoking the LLM, and ExpeL's override can rebuild the retrieval index and replace few-shots at that point ([agent/react.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/react.py), [agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py)). Rule insertion happens when the evaluation prompt is built or reset, before the current task prompt is appended.

Selection is bounded by the base number of few-shots, `buffer_retrieve_ratio`, `max_fewshot_tokens`, environment filters, current-task exclusion, duplicate-task exclusion, and optional reranking. Complexity remains substantial because selected examples are whole trajectories rather than cited fragments or compact summaries.

Authority at consumption differs by artifact. Rules carry advisory-to-instructional system-definition authority because they are placed in the prompt as experience or mandatory insight. Retrieved trajectories carry example authority: they guide behavior as demonstrations, while FAISS and rerankers carry ranking authority rather than direct instruction authority. Effective uptake by the model is not verified from code.

Other consumers are experiment scripts and humans reading logs, visualizations, and checkpoints. Those pull surfaces are useful for reproducing or inspecting runs, but the distinctive memory read-back for an acting agent is prompt assembly.

## Curiosity Pass

**The durable memory is mostly experiment artifact state.** Logs and pickles are enough for reproducing benchmark runs, but they are not a governed knowledge library. That is a design fit for ExpeL and a warning if the mechanism is copied into a long-lived KB.

**The configured retriever class is not the main retrieval path.** The config exposes `retriever_type`, and the constructor accepts `retriever_cls`, but the inspected prompt-update code directly builds a FAISS vector store from documents ([configs/agent/expel.yaml](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/configs/agent/expel.yaml), [agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py)).

**`max_num_rules` is pressure, not a hard cap.** The rule update path changes the prompt suffix and `list_full` behavior around `max_num_rules + 5`, but it does not simply slice the final rule list to `max_num_rules` ([agent/expel.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/agent/expel.py)).

**FEVER support looks less complete than the README's benchmark list.** Some FEVER reflection and critique entries are `None` or have a misspelled key in the prompt registry, so I would treat the full ExpeL extraction path as better code-confirmed for HotpotQA, ALFWorld, and WebShop ([prompts/__init__.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/prompts/__init__.py), [README.md](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/README.md)).

**Cached fold rules make lineage run-dependent.** Evaluation can load cached fold rules or regenerate rules from training histories depending on config, so the exact rule lineage depends on invocation flags and saved checkpoint state ([eval.py](https://github.com/LeapLabTHU/ExpeL/blob/e41ec9a24823e7b560c561ab191441b56d9bcefc/eval.py)).

## What to Watch

- Whether future ExpeL-style systems preserve item-level provenance from each rule back to exact trajectories, LLM operations, folds, and acceptance evidence.
- Whether trajectory retrieval moves from whole-example insertion to cited snippets or compact trajectory summaries, reducing context complexity while keeping relevance.
- Whether rule extraction gains validation before prompt authority, such as contradiction checks, held-out rule ablations, or human approval.
- Whether checkpoint storage moves from pickle to structured, inspectable artifacts suitable for review and migration.
- Whether retrieval becomes a persistent per-fold index rather than an ephemeral FAISS rebuild inside prompt updates.

Relevant Notes:

- [Trace-learning techniques in related systems](../trace-learning-techniques-in-related-systems.md) - places ExpeL's task trajectories, extracted rules, and retrieved examples in the trace-learning landscape.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes ExpeL's stored logs from prompt-time rule and example read-back.
- [Activate Behavior-Changing Memory Before The Mistake](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies pre-action insertion of behavior-shaping memory.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies to ExpeL's logs, checkpoints, trajectories, rules, vector ranking state, and prompt templates.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - distinguishes raw trajectories, logs, and retrieved examples as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes rules, prompt templates, configs, parsers, and retrieval policy as behavior-shaping artifacts.
