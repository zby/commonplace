---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "OpenRSI memory: program journals, execution-derived experience, rollout databases and training/context handoffs."
run-id: AAS-2026-10-19-openrsi-4f870183cadd-01
source-identity: "https://github.com/FrontisAI/OpenRSI"
reviewed-boundary: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
---

# OpenRSI memory report

## Boundary and evidence

The subject is the shipped OpenMLE improvement stack at SRC-1, commit `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`, under the supplied [boundary](boundary.md). Memory scope follows Gym construction/retry, Evo generation and asynchronous search, NatureBench's shared solver handoff, SFT collection/selection/training and RL generation/reward routes. It includes retained program content, evaluation traces, derived experience, checkpoint recovery, static guidance and model-visible selection. Static instructions are context inputs, not themselves read-back of experience accumulated through use.

Direct source reads below add implementation coverage within SRC-1; they do not register another source. Supplied runtime findings are identified separately. No target code, tests, provider, sandbox or trainer was executed. Source wiring establishes neither successful use nor benefit. External corpora, weights, deployed endpoint mappings and external RL SLIME remain outside the frozen evidence. Exact initial model lineage and an exercised training-to-Evo deployment chain cannot be established.

| Entry point or memory operation | Source path in SRC-1 | Coverage and limits |
| --- | --- | --- |
| Gym CLI, bound perception tools, preparation retries, package output and raw-data cleanup | `OpenMLE-Gym/openmle_gym/cli.py`; `OpenMLE-Gym/builder_core/design.py`; `OpenMLE-Gym/builder_core/utils/nodes.py` | Supplied [RT-RTE-gym-build](runtime.md#rt-rte-gym-build); annotation below. Full metadata maintenance and downstream package quality checks remain uninspected; no complete package lifecycle claim. |
| Evo journal save/load and raw/display output | `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/utils/journal.py` | Direct reads: [MEM-OBJ-journal](#mem-obj-journal), [MEM-RTE-experience-cycle](#mem-rte-experience-cycle). |
| Experience admission, per-step cards, strategy board, resume reattachment | `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py` | Direct reads: [MEM-OBJ-experience-card](#mem-obj-experience-card), [MEM-OBJ-strategy-board](#mem-obj-strategy-board). Both successful and failed experience can contribute. |
| Base memory processors and targeted operator selection | `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/memory.py`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/improve.py`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py` | Direct reads: [MEM-RTE-operator-context](#mem-rte-operator-context). Debug/crossover selector and summary preparation inspected; their complete final templates not inspected. No identical final-prompt guarantee across all operators. |
| Rich summary generation and cache alternatives | `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py` | Direct reads: [MEM-OBJ-rich-summary](#mem-obj-rich-summary). Separate node/card/cache restoration alternatives, not journal-only persistence. |
| Async commits, final export and NatureBench workspace feedback | `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`; `OpenMLE-Evo/third_party/aira-evo/examples/nature_bench/base_task.py` | Supplied [RT-RTE-evo-async](runtime.md#rt-rte-evo-async), [RT-RTE-final-submit](runtime.md#rt-rte-final-submit), [RT-RTE-naturebench-execution](runtime.md#rt-rte-naturebench-execution). Complete cancellation, workspace expiry and final-statistics consumers not inspected. |
| Optional task-skill injection and authored synthesis materials | `OpenMLE-Evo/tts_search/task_skill_guidance.py`; `OpenMLE-Evo/skills/README.md`; `OpenMLE-Evo/scripts/evaluate_airaevo.py` | Injector and README directly read; driver call sites searched. [MEM-OBJ-task-skills](#mem-obj-task-skills). Full driver normalization, individual playbook/skill content and historical synthesis provenance not inspected; no guarantee bundled filenames match task keys. |
| SFT SQLite admission, greedy read-back and checkpoint preload | `OpenMLE-ERL/SFT/tts_search/program_database.py`; `OpenMLE-ERL/SFT/tts_search/greedy.py`; `OpenMLE-ERL/SFT/tts_search/prompt_builder.py`; `OpenMLE-ERL/SFT/tts_search/services/scheduler.py` | Direct reads: [MEM-OBJ-sft-programs](#mem-obj-sft-programs), [MEM-RTE-sft-reuse](#mem-rte-sft-reuse). Evolutionary/parallel scheduler variants not fully inspected; no universal gate or lossless resume claim. |
| SFT durable logs, selection and token-budget admission to loss | `OpenMLE-ERL/SFT/tts_search/services/result_persistence.py`; `OpenMLE-ERL/SFT/tts_search/data_produce/pipeline.py`; `OpenMLE-ERL/SFT/scripts/sft_data_selection/finalize_messages.py`; `OpenMLE-ERL/SFT/slime/slime/rollout/sft_rollout.py` | Persistence primitives directly read; selection and training supplied in [RT-RTE-sft-training](runtime.md#rt-rte-sft-training). [MEM-OBJ-sft-messages](#mem-obj-sft-messages). All corpus transformations and actual corpus contents uninspected. |
| RL database construction, insertion, pruning, summary update and later prompt selection | `OpenMLE-ERL/RL/generate_mle.py`; `OpenMLE-ERL/RL/program_database.py`; `OpenMLE-ERL/RL/prompt_builder.py`; `OpenMLE-ERL/RL/airaevo_experience.py` | Database, update and AIRA inference selection directly read; helper function inventory and prompt call sites searched, not full helper body. [MEM-OBJ-rl-programs](#mem-obj-rl-programs), [MEM-RTE-rl-reuse](#mem-rte-rl-reuse). Complete helper formatting, lifecycle hooks, reward-bound caches and snapshot restore callers uninspected; no full RL state inventory/restart-fidelity claim. |
| Evo-local alternate SQLite API | `OpenMLE-Evo/tts_search/program_database.py` | Identified by source enumeration; body and callers not inspected. Must not equate it to the SFT or RL implementation. Admission, pruning and live read-back remain unresolved for this available alternative. |
| Opaque parameter memory and subsequent serving | `OpenMLE-ERL/SFT/slime_scripts/common/run_slime_sft.sh`; `OpenMLE-ERL/RL/train_with_patch.py` | Supplied [RT-CMP-sft-model](runtime.md#rt-cmp-sft-model), [RT-CMP-rl-model](runtime.md#rt-cmp-rl-model), [RT-BAP-training-parameters](runtime.md#rt-bap-training-parameters). External assets/optimizer prevent a full numerical lineage account. |

## Core ideas

1. **Executable attempts remain distinct from experience about them.** The journal retains code, plans, raw terminal output, metrics and links. Cards derive family/error/delta metadata from those attempts; a strategy board aggregates them; optional model summaries express reusable comparisons. The actual later consumer sees selected and shortened fields, not the complete archive. These distinctions are established by [MEM-OBJ-journal](#mem-obj-journal), [MEM-OBJ-experience-card](#mem-obj-experience-card), [MEM-OBJ-strategy-board](#mem-obj-strategy-board) and [MEM-OBJ-rich-summary](#mem-obj-rich-summary).
2. **Read-back is mostly software-initiated prompt construction.** Parent identity, ancestry, sibling utility or error signature target prior material before a model call. It is not a model issuing a general retrieval query. Base journal summaries are a configurable alternative, not an always-present layer. [MEM-RTE-operator-context](#mem-rte-operator-context) traces this distinction.
3. **Retention is not endorsement.** RL deliberately stores some invalid categories. SFT tree-search insertion in the inspected callback is not conditional on the rejection policy's accepted Boolean. Pruning and later selection are separate gates. A failure can be retained for debugging without authority as a successful solution: [MEM-RTE-sft-reuse](#mem-rte-sft-reuse), [MEM-RTE-rl-reuse](#mem-rte-rl-reuse).
4. **Training consumes a transformed representation.** Stored conversations become token IDs and loss masks, while reward metadata goes to a different numerical update path. Neither a JSONL file nor a checkpoint proves that later Evo operators use its result. See [RT-RTE-sft-training](runtime.md#rt-rte-sft-training) and [RT-BAP-training-parameters](runtime.md#rt-bap-training-parameters).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-journal
Label: Evo Journal and Nodes

Source-native identity: `Journal` containing `Node` objects, SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/utils/journal.py`. Storage: in-process objects and checkpoint `journal.jsonl`, written/read by `Evolutionary` in `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`. This is a retained part of the search, not a duplicate search route.
Part of: [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation)

Operative parts differ: symbolic executable code, parent/child/step identifiers, numerical metrics and flags; natural-language plan, analysis and terminal text; operator metrics can also retain prompt/completion traces. Identifiers support graph traversal and recovery; they are not equivalent to content summaries. `_term_out` holds raw output while `term_out` returns a trimmed readable view. Selected code later becomes an action through [RT-BAP-candidate-execution](runtime.md#rt-bap-candidate-execution); textual feedback reaches model interpretation through [MEM-RTE-operator-context](#mem-rte-operator-context).

> def term_out(self) -> str:
>         """Get the terminal output of the code execution (after truncating it)."""
>         if self._term_out:
>             return trim_long_string("".join(self._term_out))
>         return ""
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/utils/journal.py`

Checkpoint export enumerates fields rather than serializing arbitrary dynamic node attributes. Experience cards and rich summaries therefore require their separate paths below. Export writes `metric_info` as a nested dictionary, whereas `from_export_data` reconstructs information from keys starting `metric_info/`; exact metric-metadata recovery from this save/load pair is not established and appears lossy for the direct nested export. It does restore code, raw output, analysis, metric value/direction and graph references in the inspected implementation. Source: SRC-1, same journal path; [MEM-RTE-experience-cycle](#mem-rte-experience-cycle).

#### MEM-OBJ-experience-card
Label: Evo execution-derived experience card

Source-native identity: `build_experience_card` and `node.experience_card`; SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py` and `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`. Storage: attached dictionaries, per-step `experience_card.json`, aggregate `experience_cards.jsonl`. Symbolic fields include node/parent IDs, score/fitness/status, timings, usage, imports, method-family label, novelty, parent delta, error signature and selection diagnostics; plan/analysis and optional rich summary are natural language. These are derived records, not full logs or model weights.
Part of: [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation)

Software derives metadata from candidate code, execution/parser results, history and operator usage. Auto-detected family and inverse-square-root frequency novelty are heuristics, not established semantic novelty. Original task/data/model provenance remains external or only partially represented. Later consumers include board computation, parent utility and operator-memory construction. No per-card human approval is shown. The record is distinct from the enclosing route and from raw journal content.

> "delta_vs_parent": delta_vs_parent,
>         "error_signature": detect_error_signature(status, status_code, raw_run_log, clear_run_log),
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`

#### MEM-OBJ-strategy-board
Label: Evo aggregate strategy board

Source-native identity: `build_strategy_board`; SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`. Symbolic derived dictionary, persisted as `strategy_board.json` by `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`. It aggregates best/rank, family counts and failure rates, repeated errors, recent deltas, parent graph, score history and runtime. It is not an independently authored scientific account. Source cards supply its lineage. Prompt construction recomputes a board from attached cards; the persisted board file is not thereby proven to be the prompt reader's input.
Part of: [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation)

> "recent_delta_trend": sum(deltas[-5:]) / len(deltas[-5:]) if deltas else None,
>         "status_count": status_count,
>         "operator_counts": operator_counts,
>         "parent_graph": parent_graph,
>         "score_history": score_history,
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`

The board supplies weak/global context through operator formatting, not a trustworthy causal explanation of why a method works. Distinct from cards by aggregation scope and consumer representation; no counterpart object is declared in runtime.

#### MEM-OBJ-rich-summary
Label: Evo rich memory summary and cache

Source-native identity: `node.rich_summary`, card `rich_summary`, and `rich_summaries/<node.id>.json`; SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`. Storage: node/card dictionaries and filesystem cache adjacent to the checkpoint directory. Natural-language `method_overview` and `parent_comparison_experience` are wrapped by symbolic node/parent IDs and JSON keys. This separately maintained object belongs to the generation route, not a new inference-model component.
Part of: [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation)

Producer: optional summary model from [RT-CMP-generic-llm](runtime.md#rt-cmp-generic-llm). Inputs include current/first-parent code, plans, selected metric/card facts and sanitized readable execution output. The summary is requested to retain comparative reasons, but successful causal reasoning and faithful retention are unobserved. Its later operator display truncates each rich field to 420 characters and falls back to legacy analysis, so even generated reasons need not reach the next model intact. Source: SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py` and `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`.

> if not method_overview or not parent_experience:
>             return None
>         return {
>             "method_overview": method_overview,
>             "parent_comparison_experience": parent_experience,
>         }
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

This admission checks usable fields, not factual truth. A node-level lock avoids duplicate concurrent summary work for that node in this process. Existing node value, attached-card value, disk cache and new model generation are distinct recovery alternatives. Node-ID lookup does not establish content-hash freshness after external editing. No general cache invalidation or human editing protocol is established by these methods.

#### MEM-OBJ-task-skills
Label: Task skill guidance files

Source-native identity: task-specific Markdown loaded by `load_task_skill_map` and `TaskSkillGuidanceInjector`; SRC-1, `OpenMLE-Evo/tts_search/task_skill_guidance.py`. Filesystem natural-language guidance, keyed by filename stem in a symbolic map. The authored collection includes descriptions, category playbooks and a synthesis prompt according to `OpenMLE-Evo/skills/README.md`; individual contents and historical authorship were not traced. This is distinct from [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation): static input guidance, not accumulated episode memory or another model.

> skill_text = self.skill_map.get(task_name)
> --- `OpenMLE-Evo/tts_search/task_skill_guidance.py`

> if self.heading in public_user_prompt:
>             return public_user_prompt, TaskSkillGuidanceResult(
> --- `OpenMLE-Evo/tts_search/task_skill_guidance.py`

Consumer: configured evaluation-data patching and subsequently model-visible public user guidance. Injection is optional guidance, preserves benchmark instructions in its introduction, skips an existing heading and either reports missing or raises in strict mode. No semantic quality check or trace-fed update is shown in the injector. The supplied skill filenames include `SKILL_` prefixes; whether driver normalization maps actual task names correctly requires its full patch path, not an assumption from directory labels. Reading static files alone does not establish per-content human approval or an exercised synthesis cycle.

#### MEM-OBJ-sft-programs
Label: SFT rollout ProgramDatabase

Source-native identity: `ProgramDatabase` / `Program` in SRC-1, `OpenMLE-ERL/SFT/tts_search/program_database.py`. SQLite rows hold symbolic code, parent IDs, scores/reward/fitness, generation mode and metadata; natural-language feedback, run logs and raw model text are separate columns. Derivation combines model generations and evaluator output. `clear_run_log` in metadata can replace the reconstructed run-log display. This is a different implementation and schema from the RL database.
Part of: [RT-RTE-sft-training](runtime.md#rt-rte-sft-training)

> if self.max_per_task is not None and count > self.max_per_task:
> --- `OpenMLE-ERL/SFT/tts_search/program_database.py`

Retention is task-name top-k by fitness when configured, with `None` disabling pruning; `clear` deletes by task or all rows. A callable storage API alone is not a read-back route: [MEM-RTE-sft-reuse](#mem-rte-sft-reuse) identifies the scheduler and greedy consumer. Checkpoint preload constructs reduced rows with empty feedback/run_log and parent_code. It preserves rejection metadata and code/raw response where available, not every prior prompt input. These facts qualify lossless-resume interpretations of [RT-RTE-sft-training](runtime.md#rt-rte-sft-training).

#### MEM-OBJ-sft-messages
Label: SFT demonstration messages and training representation

Source-native identity: finalized message datasets accepted by the SFT launcher and `sft_rollout`; supplied [RT-RTE-sft-training](runtime.md#rt-rte-sft-training) provides the executable passages and SRC-1 paths. Storage: caller-selected JSONL/Parquet and in-memory training samples; message content is natural language plus symbolic code, message roles/tool schemas are symbolic, token IDs/masks are symbolic training encodings, not themselves distributed weights. Output checkpoints are the separate distributed-parametric component [RT-CMP-sft-model](runtime.md#rt-cmp-sft-model).
Part of: [RT-RTE-sft-training](runtime.md#rt-rte-sft-training)

Lineage is path-dependent: collection/score filters, evolutionary segmentation, deduplication and token-length filtering can intervene. The launcher accepts another caller-supplied dataset, so successful launch is not proof of those semantic gates or historical rollout ancestry. The training consumer receives messages/tools for mask generation and then tokens/masks; it does not freshly re-evaluate code. Exact corpus contents, retained reasons and later endpoint deployment remain uninspected. This is an operative part, not a duplicate of the training route.

#### MEM-OBJ-rl-programs
Label: RL ProgramDatabase and derived experience metadata

Source-native identity: `ProgramDatabase` / `Program` in SRC-1, `OpenMLE-ERL/RL/program_database.py`; producer/updater in `OpenMLE-ERL/RL/generate_mle.py`. SQLite persists symbolic code, payload/status, scores, reward/fitness, parent links, visit/exploit/explore/cooling statistics and metadata. Natural-language raw response/log content and optional `airaevo_rich_summary` are not equivalent to those selection counters. `airaevo_experience_card` is structured derived metadata, distinct from the original execution payload and from Evo's card file schema. The same database contains these separately consumed parts; their original task/model/data provenance is not fully supplied.
Part of: [RT-RTE-rl-training](runtime.md#rt-rte-rl-training)

> # Recompute task fitness after each insertion.
>             self._recompute_task_fitness(program.task_name, conn, cursor)
> --- `OpenMLE-ERL/RL/program_database.py`

The class docstring's top-k-by-reward wording is weaker evidence than its implementation: pruning orders by `fitness DESC`. Nonpositive max disables this prune branch. Clear/snapshot methods exist, but full lifecycle/restore wiring is not inspected. A just-inserted row can already be gone when `get_by_id` is called; the producer only builds experience metadata when the row survives. Later consumers are concrete selectors in [MEM-RTE-rl-reuse](#mem-rte-rl-reuse), not inferred solely from database availability.

### Routes

#### MEM-RTE-experience-cycle
Label: Evo trace-to-experience persistence and resume

Part of: [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation)

Trigger/owner: the per-task runner records a completed step; software builds a card and board from candidate/result/history, attaches the card and writes three experience outputs. Resume loads journal plus separately loaded cards filtered to recognized written steps, then matches cards by node ID. This is narrower than the full search route and also serves its async variant. Admission is configured experience enablement and software derivation, not per-step human approval. Failed material can remain as diagnostic history; board validity filtering and population admission are separate decisions. Metric trust is inherited from the task/parser, including alternatives in runtime; no new expected-answer oracle is added.

- Immediate return: attached card and task/step output paths, plus recomputed aggregate files.
- Later read-back: later operator and parent selectors consume attached cards; restart explicitly reattaches loaded cards to reconstructed journal nodes.
- Delegated visibility: cards expose selected execution/history fields; raw logs remain separate, and summary-model inputs use readable/sanitized output.
- Selection predicate: experience must be enabled; resume excludes cards with recognized step indexes not in written_steps; node-ID equality controls attachment.
- Invalidation or expiry: aggregate JSONL and board are rewritten; run/step filtering bounds resume. Cross-file crash atomicity and stale-summary invalidation are not established.
- Activation or effect: implementation makes trace-derived state available to later sampling/prompt construction; actual changed model behavior is unobserved.
- Evidence limits: no run artifacts, independent metric verification or exact complete recovery proof; journal metadata mismatch and separate summary caches qualify resume.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Sources: SRC-1, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`.

> for journal_node in solver.journal.nodes:
>             card = cards_by_node_id.get(str(getattr(journal_node, "id", "")))
>             if card is not None:
>                 journal_node.experience_card = card
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`

#### MEM-RTE-operator-context
Label: Evo selected memory delivery to operator calls

Part of: [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation)

The automatic trigger is an impending improve/debug/crossover call. Software selects retained nodes from parent IDs, ancestry, siblings and journal/card metadata, ensures rich summaries where configured, and formats memory before dispatch. Models propose new code; software selects/adopts the work product; caller launch/configuration is not a per-item human veto. Mode is bounded search; evaluator and parser supply outcome facts, while summary/model prose is not an answer oracle. Proposed change targets candidate code rather than operator parameters. Guidance includes selected parent code/output, task/data information, budgets and experience.

- Immediate return: selected text is inserted into operator query data; improve dispatches to GenericLLM, which renders messages or accepts explicit-message alternatives.
- Later read-back: previous nodes' summary/card facts and optionally base journal summaries reach a new operator invocation; not the entire journal archive.
- Delegated visibility: improve receives parent code and readable sanitized output separately from selected memory; summary generation receives current and first-parent material, not all ancestors' raw traces.
- Selection predicate: targeted memory requires experience.enabled and prompt_memory.enabled; base memory is used instead when targeted memory is off, or additionally when use_base_memory is true. Improve defaults to three ancestors/three horizontal siblings; crossover defaults to two each per parent. Debug prioritizes same error signature then recent nodes, with configured cap.
- Invalidation or expiry: selection is rebuilt per call; simple base memory can keep only the final max_length characters. Raw journal remains reachable to code even when omitted from this model call. No global token-fit guarantee was established.
- Activation or effect: delivery is wired; natural-language guidance depends on model interpretation, while symbolic utility calculations can change selection policy. Reliable compliance and benefit are unobserved.
- Evidence limits: item caps and 420-character rich fields are not full-prompt token budgets; complete debug/crossover final templates and provider truncation remain uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/memory.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/improve.py` and `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/llm_helpers/generic_llm.py`.

> if memory:
>         improve_data["memory"] = memory
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/improve.py`

> if max_length and summary:
>         if len(summary) > max_length:
>             summary = f"...(truncated) {summary[-max_length:]}"
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/memory.py`

Base processors also support whole-journal summaries with buggy/code/plan inclusion switches, first-parent ancestral traversal stopping at success, sibling summaries and no memory. These are format/selection alternatives, not evidence that every invocation gets all four. Selected call inputs resemble a bounded frame: the next model receives values, not live pointers into the journal. Source-native node IDs let host code traverse retained state; the model cannot dereference them without a separate exposed tool. The inspected GenericLLM API supplies no such journal-dereference operation.

#### MEM-RTE-sft-reuse
Label: SFT program admission, checkpoint reconstruction and greedy reuse

Part of: [RT-RTE-sft-training](runtime.md#rt-rte-sft-training)

The scheduler's inspected tree-search callback stores a program when search/database/generation prerequisites hold, regardless of whether rejection-policy acceptance was true. Rejection and selection metadata persist. Greedy selection subsequently chooses fresh drafts, optionally zero-fitness debug parents, or the best-fitness parent; prompt_builder inserts that parent's code and feedback. Computational policy owns selection and insertion; model owns proposed code. Caller-selected launch/data paths are not evidence of per-content human approval. Operating mode is bounded rollout collection; evaluator outcomes guide selection, not a fresh expected-answer check at prompt assembly.

- Immediate return: database ID and scheduler progress updates; on generation, a newly constructed request message list.
- Later read-back: GreedySearch retrieves retained same-task programs; checkpoint preload joins generation/evaluation records and reconstructs database rows for later search.
- Delegated visibility: new request receives a system message and freshly built user prompt; improve includes selected parent code/feedback, not every prior conversation or database row.
- Selection predicate: empty database/draft quota/probabilities decide draft; debug tries fitness zero, then falls back to best. Pruning uses task-name fitness top-k. Checkpoint rows need matching generation request and deduplicate program IDs.
- Invalidation or expiry: configured pruning and clear delete rows; preload leaves feedback/run_log/parent_code empty, so not all original context survives this alternative. Complete scheduler lifecycle and other search variants remain uninspected.
- Activation or effect: code wires prior work into later model requests and makes reduced checkpoint state reusable; changed outputs and benefit are unobserved.
- Evidence limits: callback admission is not corpus acceptance; no universal promise all retained rows reach training, no lossless feedback recovery, and no complete parallel/evolutionary variant coverage.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `OpenMLE-ERL/SFT/tts_search/services/scheduler.py`, `OpenMLE-ERL/SFT/tts_search/greedy.py`, `OpenMLE-ERL/SFT/tts_search/prompt_builder.py`, `OpenMLE-ERL/SFT/tts_search/program_database.py`.

> run_log="",
>                 feedback="",
>                 parent_id=parent_db_id,
>                 parent_code="",
> --- `OpenMLE-ERL/SFT/tts_search/services/scheduler.py`

The durable result writer separately appends/flushed/fsyncs JSONL under a file lock and atomically replaces JSON snapshots (SRC-1, `OpenMLE-ERL/SFT/tts_search/services/result_persistence.py`). Those are per-file persistence primitives, not proof of a crash-atomic database/dataset transaction or equivalent reconstructed prompt content.

#### MEM-RTE-rl-reuse
Label: RL database admission and later parent/experience prompt selection

Part of: [RT-RTE-rl-training](runtime.md#rt-rte-rl-training)

Trigger/producer: reward processing constructs a Program, applies the runtime's insertion predicate, adds it, then conditionally updates experience on the surviving row. `get_program_database` opens the configured SQLite path. `get_search_algorithm` selects different consumer implementations: greedy, evo, or airaevo. The airaevo option instantiates AIRAInferenceEvoSearch, not AIRAEvoSearch. This distinction prevents attributing every rich-memory path to every evolutionary label. Summary inputs come from the retained program/current card/parent; model writes two requested fields; software checks parseability/nonempty strings and merges metadata. No semantic veto or human approval of summary content is shown.

- Immediate return: insertion ID, optional experience metadata on sample/row, and reward to training; later select returns prompt, parents and mode.
- Later read-back: AIRAInferenceEvoSearch reads same-task programs, constructs operator-specific memory and passes it with parent code/results to build_airaevo_prompt; AIRAEvoSearch instead calls build_prompt with selected parents. Evaluation returns raw public prompts/draft without those parent-memory additions in the inspected selectors.
- Delegated visibility: generation receives constructed prompts, not SQLite or full global state. Rich summary service receives its assembled experiment prompt; payload/status and selection metadata remain distinct.
- Selection predicate: insertion accepts HTTP 200 or explicit hack/no_verify/hack_verify categories; pruning keeps fitness top-k when positive max configured. AIRA inference selection filters active successes/debug candidates, caps populations, chooses policy/mode and utilities; debug related-memory cap is eight versus three for other modes at its call site.
- Invalidation or expiry: pruning/clear can remove programs; summary generation is skipped if the inserted row is already absent. Snapshot API exists, but complete snapshot restore/lifecycle hooks and grouped prompt-cache expiry are uninspected.
- Activation or effect: source wires retained programs/derived summaries into later SGLang prompt construction and reward into training. Exercised weight changes, model compliance and improvement remain unobserved.
- Evidence limits: full airaevo_experience formatting/lineage and all reward/history caches not inspected; external trainer prevents complete training and restart conclusions. No blanket all-modes memory guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

SRC-1, `OpenMLE-ERL/RL/generate_mle.py`, `OpenMLE-ERL/RL/program_database.py`, `OpenMLE-ERL/RL/prompt_builder.py`. Closest supplied route is the parent above; this is its retained-state subroute, not a replacement.

> memory = build_operator_experience_memory(
>             mode,
>             parents,
>             all_programs=programs,
>             current_program=parent_program if mode == "debug" else None,
>             lower_is_better=False,
>             max_related_cards=8 if mode == "debug" else 3,
>         )
> --- `OpenMLE-ERL/RL/program_database.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-experience-guidance
Label: Retained experience as operator guidance

Consumer: later Evo operator models and configured RL AIRA-inference prompt consumer. Channel: selected formatted card/summary/parent text in model messages. Force: natural-language interpretation influencing proposed code; symbolic metadata separately feeds host selection. Horizon: later rounds on the task and recoverable subsequent invocations where the retained files/database and corresponding loader are used. This is distinct from [RT-BAP-candidate-execution](runtime.md#rt-bap-candidate-execution), which concerns executing generated code, and [RT-BAP-training-parameters](runtime.md#rt-bap-training-parameters), which concerns numerical training. Sources and minimum delivery passages are in [MEM-RTE-operator-context](#mem-rte-operator-context) and [MEM-RTE-rl-reuse](#mem-rte-rl-reuse). Wiring supports a behavioral channel, not activated benefit or reliable causal explanations.

## Annotations

#### On [RT-RTE-gym-build](runtime.md#rt-rte-gym-build)

The supplied route establishes a concrete same-run read-back: preparation selects the last two retained `prepares` messages between the system and current request. Software chooses the tail on retry; prior code/failure traces persist separately rather than remaining automatically model-visible. Trigger is failed preparation with retries remaining. This is selected working context, not an external retrieval service. Natural-language feedback and symbolic generated code have different consumers; Python reaches execution under the route's separate admission checks. The task package persists for evaluation/input preparation; complete downstream consumer tracing remains outside this member's direct inspection. Raw-data deletion requires the success/fileinfo condition recorded by runtime; it is not withdrawal of all derived package artifacts. No per-generated-file human approval follows from --execute. The supplied verbatim query/compile passages support these limits (SRC-1, `OpenMLE-Gym/builder_core/utils/nodes.py`).

#### On [RT-RTE-sft-training](runtime.md#rt-rte-sft-training)

Stored message read-back is explicit at the SFT rollout consumer, whereas selected-score and token-length gates belong to producer paths and are not universal launcher admission. Whole-example token rejection is context/data filtering, not compaction into a retained summary. Samples become token IDs and masks with reward zero in SFT; full raw output is not passed as an execution object to the optimizer. Numerical checkpoints can have longer persistence than any prompt but require separately established later serving. See its supplied executable passages and [MEM-OBJ-sft-messages](#mem-obj-sft-messages).

## Write side

Acquisition and admission are path-specific. Gym model authoring plus compile/write/retry checks differs from Evo's execution-derived card construction, from optional model summary generation, and from caller-selected training datasets. Launch/configuration supplies authority to run a workflow; it does not show a human editing or approving each retained item. Initial model/corpus provenance remains unresolved alongside these known subsequent transformations.

The Evo chain is raw candidate/plan/execution → parsed journal facts → deterministic card/board → optional comparative natural-language summary → selected later operator guidance. [MEM-RTE-experience-cycle](#mem-rte-experience-cycle) and [MEM-RTE-operator-context](#mem-rte-operator-context) distinguish trace retention from a derived result with an actual later consumer. Cards/boards retain provenance IDs and selected evidence fields, not complete reasons. Summary fields request reasons; structural acceptance cannot verify them, and display shortening can remove them. Separate journal, card file and rich-summary cache are materially different checkpoint forms. A summary may be recovered from node, card or cache before any new model call. None implies an immutable evidence/versioned semantic curation system.

SFT and RL retain failure evidence without necessarily admitting it as successful work. SFT's inspected callback stores acceptance as metadata; dataset gates operate later. RL's invalid-category retention precedes consumer filtering, and top-k fitness pruning is a separate withdrawal mechanism. Pruned database rows are no longer selected through those database methods, but this does not prove erasure from result logs, snapshots or already-constructed prompts. Explicit clear APIs establish deletion capability, not an observed maintenance schedule. [MEM-RTE-sft-reuse](#mem-rte-sft-reuse) and [MEM-RTE-rl-reuse](#mem-rte-rl-reuse) bound these conclusions.

Static task skills have a file-edit/synthesis surface but no demonstrated automatic trace-fed maintenance path in the inspected injector. Full content quality and historical synthesis remain unresolved. Training datasets similarly have caller-controlled replacement surfaces. These are not automatically human curation, and automatic transformations are not automatically epistemically warranted.

## Read-back

The concrete consumers are the next preparation invocation, later search operators, SFT greedy/tree-search generation, SFT token/mask generation, and configured RL prompt selection. Their requests are triggered by code-owned retries, search iterations or training reads. Selection is predominantly automatic supply into a new call, not an unsolicited independent agent or foreground model deciding to fetch a remembered fact. Parent/task/error targeting is supported; semantic-vector retrieval is not established by these inspected paths.

Budgets operate at different units. Gym selects two messages. Base Evo memory can keep a character suffix or exclude code/buggy nodes; targeted memory caps nodes and truncates summary fields. SFT token filtering excludes examples instead of summarizing them; its scheduler can bound how many new generations happen. None establishes a common context-token budget across the complete system. Current frames retain only selected values; host journals/databases remain separately accessible to host code. Popping a model call's local frame does not delete retained search state, and IDs shown in text are not automatically dereferenceable model pointers.

Stored knowledge and behavioral authority are consumer-relative. Code in a parent prompt is evidence/example material interpreted by a model; chosen code sent to the executor has executable force. Reward/fitness metadata can directly determine software selection, while prose summary claims cannot compel compliance. Message datasets influence numerical training through token masks, not through ordinary prompt obedience. Exact trained checkpoint adoption remains unresolved rather than inferred from persistence.

## Integration issues

- **Journal metadata recovery qualification.** [MEM-OBJ-journal](#mem-obj-journal) identifies nested `metric_info` export versus flattened-key reconstruction in SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/utils/journal.py`. The generic checkpoint statements in [RT-RTE-evo-generation](runtime.md#rt-rte-evo-generation) should not be read as complete recovery of evaluator metadata. Consequence: recovered metric value alone need not preserve every status/official-score predicate used by experience selection. No correction of a demonstrated runtime result is claimed.
- **Separate restore surfaces.** [MEM-OBJ-rich-summary](#mem-obj-rich-summary) and [MEM-RTE-experience-cycle](#mem-rte-experience-cycle) supplement the runtime journal account with card reattachment and summary cache alternatives. Exact cross-file consistency/freshness remains unresolved; neither journal-only completeness nor total loss of summaries is justified.
- **SFT rejection is not tree-database exclusion.** [MEM-RTE-sft-reuse](#mem-rte-sft-reuse) supplements [RT-RTE-sft-training](runtime.md#rt-rte-sft-training): the inspected scheduler callback persists accepted/rejected metadata while storing the generated evaluated program. Its reduced checkpoint preload can omit previously model-visible feedback. Consequence: corpus admission, search admission and checkpoint context equivalence must stay separate.
- **RL policy labels and pruning.** [MEM-RTE-rl-reuse](#mem-rte-rl-reuse) distinguishes `evo` from `airaevo` consumer classes; [MEM-OBJ-rl-programs](#mem-obj-rl-programs) qualifies the class docstring's reward-pruning label with executable fitness ordering. This supplements rather than contradicts [RT-RTE-rl-training](runtime.md#rt-rte-rl-training). Full helper formatting, caches and snapshot/lifecycle callers remain uninspected, preventing a complete RL-state/restart claim.
- **Unresolved alternate and static-input coverage.** Evo-local SQLite API callers and exact skill filename/task normalization remain unresolved in the coverage table. Available source is not an access gap or evidenced absence. No common semantics across three ProgramDatabase files, exercised skill injection, or complete automatic skill-maintenance claim is made.
- **Identity/overlap.** All new route/object parts name their closest supplied container explicitly. No new declaration is proposed as a duplicate replacement of a supplied record; [MEM-BAP-experience-guidance](#mem-bap-experience-guidance) is distinct from executable-code and parameter-update authority. The async route shares these memory objects rather than introducing a second store. Other analysts were not supplied, so cross-specialist identity remains for reconciliation.

## Limitations and checks

HEAD was rechecked directly as the frozen commit. Source identity matches boundary and invocation; all new implementation findings remain SRC-1. Method/type/collection/worker/record inputs were read, including bounded continuations. Source reads were static; failed exploratory path searches did not supply evidence and were followed by reads at actual paths. No source or engine metadata was modified.

The inventory retains unresolved included mechanisms rather than claiming whole-system coverage: metadata/evaluation maintenance, full debug/crossover templates, individual authored skills/playbooks, Evo-local SQLite callers, all SFT parallel/evolutionary variants, RL helper formatting/history caches/lifecycle restore and external optimizer/provider internals. These limits prevent completeness, exact training provenance, crash-consistent semantic recovery and exercised-improvement conclusions, not the positive routes documented above. No observed or causally supported operation is claimed. Persistence and delivery alone establish neither improved capacity nor a theory-builder or self-improvement result.

Deterministic output validation passed: `commonplace-run validate-output` reported “Member content check passes; invocation residue not checked.” This establishes form/quotation checks only, not claim support or job acceptance.
