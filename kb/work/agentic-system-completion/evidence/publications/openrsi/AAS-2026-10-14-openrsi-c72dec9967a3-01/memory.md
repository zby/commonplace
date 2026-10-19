---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "OpenRSI memory: evaluated program histories, targeted experience summaries, training-data selection and Gym context construction."
run-id: AAS-2026-10-14-openrsi-c72dec9967a3-01
source-identity: "https://github.com/FrontisAI/OpenRSI"
reviewed-boundary: "71ae803a035d5e3b78c19fa49ed9f67d0550cbaa"
---

# OpenRSI memory report

## Boundary and evidence

This report covers retained program-search experience, its selected model-visible renderings, supervised-training examples and task-building context within the frozen [boundary](boundary.md). SRC-1 is the sole source. All new findings below are implementation readings at commit `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`; prompts additionally show requested behavior, not model compliance. No target code, tests, services or model endpoints were executed. External weights, full corpora, historical runs and the upstream RL trainer are not captured. Consequently persistence and delivery can be established in source, but actual activation, improved capacity and historical checkpoint lineage cannot.

The supplied runtime is a useful route inventory, not proof that every retained artifact reaches every consumer. The following table distinguishes direct inspection from reliance on supplied findings and retains unresolved surfaces. Paths are commit-relative SRC-1 anchors.

| Operation / entry point | Inspected source or supplied evidence | Coverage and conclusion limit |
| --- | --- | --- |
| Evo runner checkpoint and experience attachment | Direct: `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`; `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/utils/journal.py` | [MEM-OBJ-journal](#mem-obj-journal), [MEM-OBJ-experience-card](#mem-obj-experience-card); journal, cards and summary cache are separate persistence forms, not one complete checkpoint. |
| Evo Draft/Improve/Debug/Crossover context, legacy alternatives | Direct: `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/memory.py`; searched call sites in operator files; directly inspected targeted selector and renderer in `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py` | [MEM-RTE-targeted-memory](#mem-rte-targeted-memory); default counts and clipping, not a universal token budget. |
| Rich-summary production and cache reload | Direct: `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py`; solver summary methods | [MEM-OBJ-rich-summary](#mem-obj-rich-summary), [MEM-RTE-summary-cache](#mem-rte-summary-cache). Model truthfulness and cache invalidation after content edits are not established. |
| RL generation/reward hooks and database APIs | Direct bounded reads/searches: `OpenMLE-ERL/RL/generate_mle.py`, `OpenMLE-ERL/RL/program_database.py`, `OpenMLE-ERL/RL/airaevo_experience.py` | [MEM-OBJ-rl-program](#mem-obj-rl-program); annotation on [RT-RTE-rl-training](runtime.md#rt-rte-rl-training). AIRAInferenceEvoSearch traced; other search classes inventoried but not all prompt branches audited. No uniform selector claim. |
| SFT tree-search collection and checkpoint preload | Direct: `OpenMLE-ERL/SFT/tts_search/services/scheduler.py`, `OpenMLE-ERL/SFT/tts_search/greedy.py`, `OpenMLE-ERL/SFT/tts_search/program_database.py` | [MEM-OBJ-sft-program](#mem-obj-sft-program), [MEM-RTE-sft-search](#mem-rte-sft-search). Preload omits feedback even when original row retained it. Other scheduler modes not exhaustively inspected. |
| SFT selection and training consumer | Direct collection and alignment: `OpenMLE-ERL/SFT/tts_search/data_produce/collect.py`, `OpenMLE-ERL/SFT/tts_search/data_produce/alignment.py`; supplied filter/trainer wiring: [RT-RTE-sft-training](runtime.md#rt-rte-sft-training) | [MEM-OBJ-alignment-dataset](#mem-obj-alignment-dataset). Corpus-specific selection and numerical updates unobserved. |
| Gym graph, bound tools, description and preparation feedback | Direct: `OpenMLE-Gym/builder_core/design.py`, `OpenMLE-Gym/builder_core/utils/state.py`, bounded `OpenMLE-Gym/builder_core/utils/nodes.py`; supplied CLI dispatch: [RT-RTE-gym-build](runtime.md#rt-rte-gym-build) | Annotation below; explicit query construction is established, graph-state erasure is not. Tool implementation/edit validation and every metadata-pipeline branch remain uninspected. |
| Gym executable task packages and sandbox evaluation | Supplied: [RT-OBJ-metric](runtime.md#rt-obj-metric), [RT-RTE-sandbox-evaluation](runtime.md#rt-rte-sandbox-evaluation) | Executable authority is distinct from prose experience. Sandbox SQL/idempotency/session records are operational persistence, not established later model-context consumers; their cleanup and authorization were not audited here. |
| NatureBench/local adapters and async commits | Supplied: [RT-RTE-naturebench-execution](runtime.md#rt-rte-naturebench-execution), [RT-RTE-async-search](runtime.md#rt-rte-async-search) | Shared journal delivery does not establish an additional memory store. NatureBench-specific prompt differences and all remote infrastructure remain uninspected. |
| Other vendored/search and static guidance surfaces | Tree/search inventory: `OpenMLE-Evo/tts_search/program_database.py`, `OpenMLE-ERL/SFT/third_party/aira-evo/src/dojo/core/solvers/operators/memory.py`; shipped skills/prompts named in boundary | Included but not traced end to end here. These are distinct copies, not proved identical to Evo's rich-memory path. Cannot claim exhaustive memory equivalence across stages, or that every shipped skill is automatically loaded. |

Initial database contents and operator-supplied prompt/data provenance remain local unknowns. No human per-content approval follows merely from launching these stages. Available but uninspected branches above are not absences.

## Core ideas

1. **The program history and the active population are different.** A failed or displaced candidate can remain in Evo's journal and become failure context even when it cannot be an active solution. Code, logs and scores are records of attempts; cards and summaries are derived products. [MEM-OBJ-journal](#mem-obj-journal), [MEM-OBJ-experience-card](#mem-obj-experience-card), [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search).
2. **Context is assembled around an operator, not recovered as a full conversation.** Improve selects ancestry and neighboring attempts; Debug prioritizes matching errors. The summary model can turn code and execution records into reusable prose, cached by node ID. The later model receives clipped display fields, not all evidence the summary producer saw. [MEM-RTE-targeted-memory](#mem-rte-targeted-memory), [MEM-RTE-summary-cache](#mem-rte-summary-cache).
3. **Training retains a different projection of experience.** SFT keeps conversation examples after score-based selection, while separate manifests retain selection metadata. RL stores programs, including some invalid categories, for later parent/context selection. Neither database membership nor the word “experience” certifies correctness. [MEM-OBJ-alignment-dataset](#mem-obj-alignment-dataset), [MEM-OBJ-rl-program](#mem-obj-rl-program).
4. **Working-context isolation can exist without erasing stored state.** Gym constructs each model query explicitly. Its graph nodes returning an empty message list do not themselves establish deletion under an append/merge reducer. Preparation retries retain a code-and-feedback tail rather than the entire attempt rationale. Annotation on [RT-RTE-gym-build](runtime.md#rt-rte-gym-build).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-journal
Label: Evo Journal and Node history

Part of: [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search)

The object is retained state within that route, not a duplicate of the whole search route. Source-native identity: `Journal.nodes` and `Node` fields for code, plan, parents/children, execution output, analysis, metrics and operator usage. Substrate: Python objects and checkpoint `journal.jsonl`. Form: symbolic Python and graph/score metadata, natural-language plans/analysis/log text. Logs are raw task feedback; analysis is derived and may be model-generated. Content and access/link metadata remain distinct. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/utils/journal.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`.

The solver writes every exported node then reconstructs nodes and relations at reload. Later consumers are parent selection and model-context construction. Numeric metrics influence code selection directly; prose affects proposals only through model interpretation. Horizon: rounds and continuation on the same task. This is not cross-task retrieval by itself. Island eviction is not journal erasure; see [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search).

> journal_sd = self.journal.node_list()
> journal_path = Path(self.cfg.checkpoint_path) / "journal.jsonl"
> with open(journal_path, "w") as f:
>     for node in journal_sd:
>         f.write(json.dumps(node) + "\n")
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

Checkpoint fidelity is limited. Export writes a nested `metric_info`; reload instead gathers flattened keys starting `metric_info/`. Thus nested score provenance/status can be lost even when the scalar metric survives. Dynamic experience-card and rich-summary attributes are not in this explicit journal export. Separate files compensate for some omissions, not a lossless journal round trip. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/utils/journal.py`.

> "metric_info": node.metric.info if node.metric else None,
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/utils/journal.py:285-305`

> metric_info = {
>     k[len("metric_info/") :]: v for k, v in node_data.items() if k.startswith("metric_info/")
> }
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/utils/journal.py`

#### MEM-OBJ-experience-card
Label: Experience cards and strategy board

Part of: [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search)

These are derived parts of search state, not another name for the route. Source-native identity: per-step `experience_card.json`, aggregate `experience_cards.jsonl`, `strategy_board.json`, and attached `node.experience_card`. Storage is filesystem JSON and Python dictionaries. The card's IDs, lineage, scores, rank, timing, detected family, novelty and error signature are symbolic fields. Its plan/analysis and optional summary are natural-language content. A board aggregates cards; neither a family label nor novelty score is a verified explanation of why a method succeeds. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`, `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`.

The runner's step callback derives cards from evaluated nodes and raw/clear logs, computes the board and writes files when experience is enabled. No per-card human approval occurs there. On continuation, it reads cards, filters against retained written steps and attaches by node ID. Later consumers include prompt rendering and optional experience-based parent utilities. This retention is trace-fed transformation, not merely raw logging. Rationale survives as plan/analysis where present, but those are not all delivered in targeted display. [MEM-RTE-targeted-memory](#mem-rte-targeted-memory).

> for journal_node in solver.journal.nodes:
>     card = cards_by_node_id.get(str(getattr(journal_node, "id", "")))
>     if card is not None:
>         journal_node.experience_card = card
> --- `OpenMLE-Evo/third_party/aira-evo/examples/mle_bench/single_task_runner.py`

> "novelty_score": novelty_score,
> "delta_vs_parent": delta_vs_parent,
> "error_signature": detect_error_signature(status, status_code, raw_run_log, clear_run_log),
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`

#### MEM-OBJ-rich-summary
Label: Rich memory summary

Part of: [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search)

Source-native identity: two fields, `method_overview` and `parent_comparison_experience`, on a node/card and in `rich_summaries/<node.id>.json`. Form: natural-language method and comparative experience inside symbolic JSON; node/parent IDs are lineage/access metadata, not the explanation. Storage is cache files plus Python objects, separate from the journal. No counterpart object was declared in runtime; [RT-CMP-generic-llm](runtime.md#rt-cmp-generic-llm) is its producer component, not this artifact. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py`.

Producer inputs include current and first-parent code, plan, execution output, task description, score/status, runtime and card fields. The output requests comparative reasons rather than only success labels. Later operator displays can carry those reasons, clipped to 420 characters per field; their correctness and full preservation are not guaranteed. [MEM-RTE-summary-cache](#mem-rte-summary-cache), [MEM-RTE-targeted-memory](#mem-rte-targeted-memory).

> "description": "2-5 concise sentences comparing the current node against its parent and extracting reusable success or failure experience."
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py`

#### MEM-OBJ-rl-program
Label: RL ProgramDatabase program and metadata

Part of: [RT-RTE-rl-training](runtime.md#rt-rte-rl-training)

Source-native identity: RL `Program` SQL rows, including executable code, raw generated text, evaluator `payload`, scores/rewards, parent code/ID, category/hack flags and JSON metadata. Substrate: SQLite plus snapshots. Form is mixed: symbolic executable code, numeric/control metadata and natural-language generation/feedback/summary content. A payload dictionary is not interchangeable with the brief rich-summary display. Initial DB provenance is operator/deployment-dependent; subsequent generation/evaluation lineage is explicitly retained. SRC-1, `OpenMLE-ERL/RL/program_database.py`, `OpenMLE-ERL/RL/generate_mle.py`.

Runtime already establishes admission of status 200 and the `hack`, `no_verify`, `hack_verify` categories. The database then recomputes task fitness and, if capped, physically deletes rows outside top-k fitness. This is separate from reward sign and active-success eligibility. `clear(task_name)`/global clear are exposed deletion capabilities, not proof of an automatic withdrawal schedule. `save_snapshot` commits then copies the database file; no inspected automatic restoration into serving is established. SRC-1, `OpenMLE-ERL/RL/program_database.py`; [RT-RTE-rl-training](runtime.md#rt-rte-rl-training).

> # Maintain top k programs per task when max_per_task > 0.
> --- `OpenMLE-ERL/RL/program_database.py`

> ORDER BY fitness DESC
> LIMIT ?
> --- `OpenMLE-ERL/RL/program_database.py:457-470`

Later consumers include task-local parent selection, context construction, fitness recomputation and reward-baseline queries. Those channels have different trust rules: `get_all_base_rewards(include_hack=False)` excludes hacks by default, whereas `get_all(task_name)` returns rows without that exclusion. Retention therefore does not give every row the same behavioral authority. SRC-1, `OpenMLE-ERL/RL/program_database.py`.

#### MEM-OBJ-sft-program
Label: SFT rollout ProgramDatabase rows

Part of: [RT-RTE-sft-training](runtime.md#rt-rte-sft-training)

The object belongs to the experience-production side of that broader route. It is distinct from RL's database: separate source file, row schema, fitness handling and consumers. Source-native identity: `OpenMLE-ERL/SFT/tts_search/program_database.py` `Program` rows, with code, run log, feedback, raw text, parent fields, score/reward/fitness and metadata. Substrate: SQLite. Form: executable symbolic code and numerical/link fields alongside natural-language feedback and generation text. Admission, pruning and later read-back are in [MEM-RTE-sft-search](#mem-rte-sft-search). SRC-1, `OpenMLE-ERL/SFT/tts_search/program_database.py`.

The schema preserves feedback separately from logs; metadata can preserve model request messages, reasoning and rejection reasons in the scheduler. This supports local lineage, not verified original dataset provenance. The source-native Evo `tts_search` database is another copy, not silently identified with this one. SRC-1, `OpenMLE-ERL/SFT/tts_search/services/scheduler.py`, `OpenMLE-ERL/SFT/tts_search/program_database.py`.

#### MEM-OBJ-alignment-dataset
Label: SFT alignment conversations and manifest

Part of: [RT-RTE-sft-training](runtime.md#rt-rte-sft-training)

Source-native identity: output JSONL/Parquet training rows plus optional CSV manifest. Storage: filesystem datasets. Representational form: natural-language system/user/assistant content containing symbolic Python, then token/loss-mask representation at training; weights are a distinct distributed-parametric result described by [RT-CMP-training-models](runtime.md#rt-cmp-training-models). SRC-1, `OpenMLE-ERL/SFT/tts_search/data_produce/collect.py`, `OpenMLE-ERL/SFT/tts_search/data_produce/alignment.py`.

Lineage is a reconstructed conversation, not necessarily a verbatim complete rollout: source system text can be transformed to a pass-k draft system prompt; user text comes from retained `user_prompt.md` or source fallback; assistant content is rebuilt from reasoning/code/response files. Evaluator feedback is used to admit examples and kept as metadata/paths, not automatically appended as an assistant justification. The training frame deliberately drops all but ID/messages. A separate manifest retains score, reward, feedback status and paths. Thus selection reasons can survive beside the examples without reaching the training loss consumer as reasons. Exact contents of external source Parquet remain unknown. SRC-1, `OpenMLE-ERL/SFT/tts_search/data_produce/collect.py`, `OpenMLE-ERL/SFT/tts_search/data_produce/alignment.py`.

> return pd.DataFrame(
>     [{"id": row["id"], "messages": row["messages"]} for row in rows]
> )
> --- `OpenMLE-ERL/SFT/tts_search/data_produce/alignment.py`

### Routes

#### MEM-RTE-summary-cache
Label: Rich summary derivation and cache reuse

Part of: [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search)

Trigger and progression: before an Improve/Debug/Crossover call, solver-selected related nodes → existing node/card summary → disk cache → otherwise optional summary model → structural normalization → node/card/cache → later targeted prompt. Owner: solver code selects and admits; model authors prose. This is the write/reuse part of the runtime's broader search route, not a second declaration of the whole route. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/rich_memory_summary.py`.

- Immediate return: summary fields attached to node and card; disk write is attempted, with warning on I/O failure.
- Later read-back: same-task later operator calls and continuation can load the node-ID cache; selected summaries reach the model through targeted display.
- Delegated visibility: summary model sees selected current/first-parent code, plans, output and metadata, not every prior conversation; proposal model sees a shorter rendering.
- Selection predicate: prompt-memory enabled; related-node selector; existing nonempty two-field dictionaries take precedence over a new model call. Normalization admits nonempty strings, not semantic correctness.
- Invalidation or expiry: malformed/missing cache is bypassed; exceptions/invalid JSON do not admit new summary; existing valid-shaped entries are reused. No content-hash comparison is made in the inspected cache-loading method.
- Activation or effect: implements trace-fed prose that can shape later proposals; actual reliance or benefit is unobserved.
- Evidence limits: source wiring only; cached IDs do not verify content freshness, summary truth or successful disk persistence.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is software validation of model-authored content, not human approval. The operator can configure/disable the mechanism; no per-summary veto or quality oracle is shown. Task feedback guides bounded experiment summarization. Recovery is reuse or retry on a later call; no inspected semantic rejection/rollback loop updates a misleading but well-shaped summary. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`.

> cached_summary = self._load_cached_rich_summary(node)
> if cached_summary is not None:
>     self._store_rich_summary(node, cached_summary)
>     return
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

> if not method_overview or not parent_experience:
>     return None
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/evo.py`

#### MEM-RTE-targeted-memory
Label: Evo targeted operator memory

Part of: [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search)

Endpoints: accumulated nodes/cards → code selector and board rendering → operator query data → GenericLLM system/user messages → next program proposal. Owner: solver/operator code, not a foreground model issuing a retrieval tool request. Distinct part: context selection within the larger evolution route; [RT-BAP-operator-guidance](runtime.md#rt-bap-operator-guidance) supplies the downstream authority channel. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/improve.py`.

- Immediate return: formatted memory string attached to operator query data when nonempty.
- Later read-back: later proposal invocations receive accumulated experiment evidence selected from journal/card state; cache reload extends the horizon across task continuation.
- Delegated visibility: selected parent, recent ancestors and ranked related attempts, plus aggregate board stats and clipped summaries; not full raw logs or all plans from every node.
- Selection predicate: Improve defaults to parent plus three ancestors and three horizontal siblings sharing a parent; Crossover defaults to two ancestors/two siblings for each of two parents. Siblings rank by utilities. Debug prioritizes error-signature matches, then recent nodes, capped by configuration.
- Invalidation or expiry: context is rebuilt per call; omitted nodes remain reachable in journal/files. Rich summaries clip to 420 characters per field, fallback legacy analysis to 360. Count caps are not a total token ceiling.
- Activation or effect: rendered experience is advisory model-interpreted input; numeric utility can separately influence parent sampling. Delivery is wired, behavioral activation and benefit unobserved.
- Evidence limits: current inspected Evo implementation; alternate prompts must actually reference the memory field. No cross-system equivalence or universal context-budget guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Code automatically supplies selected evidence as part of a proposal call: this is push into the operator context, not independent unsolicited execution or model-directed retrieval. The candidate model authors new code; solver/task code retains veto over admission using task evaluation. No per-memory human approval or truth oracle intervenes. Source prompts request using experience and avoiding repeated failures; the method/family labels and comparative narratives are fallible guidance. [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search), [RT-RTE-sandbox-evaluation](runtime.md#rt-rte-sandbox-evaluation).

> if parent_ids.intersection(candidate_parent_ids):
>     siblings.append(candidate)
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`

> method_overview = _compact_text(rich_summary.get("method_overview"), max_chars=420)
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/solvers/evo/experience.py`

Legacy alternatives remain material: factory-registered `simple_memory`, `ancestral_memory`, `sibling_memory`, `no_memory` operate on the journal. Simple memory can select good-only or buggy-inclusive nodes, plans-only or code/analysis, and retain only a character-limited suffix. Ancestral memory follows the first parent and can stop at a successful parent; sibling memory renders children of the supplied node. Draft uses its base memory operator; Improve/Debug/Crossover can omit base memory when targeted memory is enabled, or append it when configured. Thus targeted memory is not the sole read-back route. SRC-1, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/memory.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/draft.py`, `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/improve.py`.

> summary = f"...(truncated) {summary[-max_length:]}"
> --- `OpenMLE-Evo/third_party/aira-evo/src/dojo/core/solvers/operators/memory.py`

#### MEM-RTE-sft-search
Label: SFT tree-search retention and replay

Part of: [RT-RTE-sft-training](runtime.md#rt-rte-sft-training)

Endpoints: generated/evaluated rollout → scheduler Program construction → SQLite insert/prune → GreedySearch parent selection → prompt builder → next generation. Owner: scheduler/database/search code. A separate checkpoint preload rebuilds rows from generation/evaluation result records. This is experience production within the supplied training route, distinct from numerical SFT optimization. SRC-1, `OpenMLE-ERL/SFT/tts_search/services/scheduler.py`, `OpenMLE-ERL/SFT/tts_search/greedy.py`, `OpenMLE-ERL/SFT/tts_search/program_database.py`.

- Immediate return: persisted row ID and updated task progression; selected prompt/parent on the next search request.
- Later read-back: GreedySearch reads task-local best or zero-fitness debugging parent; checkpoint preload repopulates code, scores and parent links for continued generation.
- Delegated visibility: prompt builder receives selected parent and task description, not the whole SQL store; preloaded rows can lack original execution feedback.
- Selection predicate: empty DB forces Draft; otherwise configured draft/debug probabilities and draft count, with best-fitness fallback. Database pruning keeps top-k by fitness, unless max_per_task is None.
- Invalidation or expiry: SQL deletion prunes rows; clear API supports task/global deletion. Rejected evaluations can still be stored with acceptance/rejection metadata; retention is not dataset admission.
- Activation or effect: retained programs feed subsequent context; no actual rollout or model response was observed.
- Evidence limits: selected tree-search and preload branches, not every scheduler mode or all reconstructed prompt text. Replay preserves less context than original row construction.
- implementation conclusion status: wired
- operation conclusion status: uninspected

The model proposes programs; code decides acceptance labels, row persistence and later selection. No human per-program approval is shown. Rejection policy/task feedback supplies the bounded experiment's selection evidence, not a guarantee that admitted text is true. Recovery reconstructs from checkpoints rather than restoring all original messages. The preload explicitly writes blank log, feedback and parent code, while retaining IDs and code. SRC-1, `OpenMLE-ERL/SFT/tts_search/services/scheduler.py`.

> run_log="",
> feedback="",
> parent_id=parent_db_id,
> parent_code="",
> --- `OpenMLE-ERL/SFT/tts_search/services/scheduler.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-rl-training](runtime.md#rt-rte-rl-training)

Memory-specific retention and curation: [MEM-OBJ-rl-program](#mem-obj-rl-program) persists raw program/evaluation material plus derived card/summary metadata. For the `airaevo` algorithm, `_maybe_update_airaevo_program_metadata` derives a card after insertion, optionally asks a summary endpoint for two prose fields, and merges metadata. Admission only checks nonempty fields; failures retain an error category rather than a validated summary. The summary endpoint is `AIRAEVO_MEMORY_LLM_URL` or the current SGLang router, not a pinned weight identity. Its parameters are not updated by this helper; a mutable endpoint can resolve to different weights. Training mutability remains as described by [RT-CMP-training-models](runtime.md#rt-cmp-training-models). SRC-1, `OpenMLE-ERL/RL/generate_mle.py`.

> url = os.getenv("AIRAEVO_MEMORY_LLM_URL", "").strip()
> if not url:
>     url = f"http://{args.sglang_router_ip}:{args.sglang_router_port}/generate"
> --- `OpenMLE-ERL/RL/generate_mle.py`

Read-back: AIRAInferenceEvoSearch reads task rows, filters an active-success population, chooses mode/parents and automatically builds experience memory into system/user prompts. Evaluation mode returns the original public prompts without that selected-parent path. RL's Draft can receive best/recent prior memories; Improve's “horizontal sibling” renderer actually selects children of the current parent, unlike Evo's shared-parent siblings. Debug uses signature matches then recency; Crossover displays parents and ancestry. There is no single shared selector semantics merely because labels match. Rich prose is clipped to 420 characters in this RL renderer. SRC-1, `OpenMLE-ERL/RL/program_database.py`, `OpenMLE-ERL/RL/airaevo_experience.py`.

> siblings = _sort_programs(_children_of(parent, programs), lower_is_better)[: 3 if sibling_k is None else max(0, int(sibling_k))]
> --- `OpenMLE-ERL/RL/airaevo_experience.py`

Group selection caching temporarily shares selected prompt/parent data across samples; it deletes the entry after expected accesses. That is working-context coordination, not durable experience curation. Database snapshots persist a different horizon. Source trust is task/evaluator-dependent, especially for retained invalid categories; actual reuse, parameter effects and summary reliability remain unobserved. SRC-1, `OpenMLE-ERL/RL/generate_mle.py`, `OpenMLE-ERL/RL/program_database.py`.

#### On [RT-RTE-sft-training](runtime.md#rt-rte-sft-training)

The filtered training result is [MEM-OBJ-alignment-dataset](#mem-obj-alignment-dataset); SQL production history is [MEM-OBJ-sft-program](#mem-obj-sft-program). Those are not interchangeable with trained parameters. Collection rejects nonmatching status, insufficient reward, rejection-policy failure and, when required, nonsuccess feedback; supplied runtime further traces token, validation/test-gap, top-k and dedup filters. The operator configures inputs/thresholds, but software admits each row. Source files and manifests keep provenance that minimal training messages omit. SRC-1, `OpenMLE-ERL/SFT/tts_search/data_produce/collect.py`; supplied [RT-RTE-sft-training](runtime.md#rt-rte-sft-training).

> if require_feedback_success and not feedback_is_success(feedback):
>     counters["dropped_feedback_not_success"] += 1
>     continue
> --- `OpenMLE-ERL/SFT/tts_search/data_produce/collect.py`

The later training consumer requests the selected dataset, tokenizes messages and loss masks, and updates weights. This is a trace-fed numerical update path, not evidence that every selection reason is presented to the trained model or that the resulting weights improved future work. The full historical corpora and deployed model handoff remain unavailable. [RT-RTE-sft-training](runtime.md#rt-rte-sft-training), [RT-CMP-training-models](runtime.md#rt-cmp-training-models).

#### On [RT-RTE-gym-build](runtime.md#rt-rte-gym-build)

Working-context control is explicit query construction. Perception selects tool-message content, a fresh system prompt and file-tree request; Describe loads web info, raw tree and saved file inventory into a new query. Tool-bound `save` material crosses into `fileinfo.txt`, then Describe consumes it to author `description.txt`; Prepare reloads that description and a shipped sample. The graph's tool inventory includes listing, CSV summary, text/Markdown read and save. Saved inventory and generated description are derived material; raw web/tree files and prepared data are distinct evidence/input artifacts. Tool implementation admission checks remain uninspected. SRC-1, `OpenMLE-Gym/builder_core/design.py`, `OpenMLE-Gym/builder_core/utils/nodes.py`.

> response = self.llm_provider_tools.query(
>     [query[0]] +
>     tool_messages +
>     [query[1]]
> )
> --- `OpenMLE-Gym/builder_core/utils/nodes.py`

Correction/limit on graph-state reset interpretation: graph R nodes return `messages: []`, but AgentState uses `add_messages`. An empty returned list does not itself prove erasure under this reducer; framework execution is not inspected here. The stronger supported result is that the explicit LLM query omits most accumulated state. The frame analogy fits each selected model call, not an asserted deletion of its caller's graph history. SRC-1, `OpenMLE-Gym/builder_core/utils/state.py`, `OpenMLE-Gym/builder_core/design.py`.

> messages: Annotated[Sequence[BaseMessage], add_messages]
> --- `OpenMLE-Gym/builder_core/utils/state.py`

Preparation retries supply `prepares[-2:]`: after a completed attempt these are code and success/error feedback, not the previous description and extracted thought. The full four-field attempt groups are written to `prepares.json` at Next. No later automatic reload of that JSON is established here; within-run retry read-back is established. Source raw deletion is conditional on success and nonempty file inventory, preserving that inventory as a raw placeholder, not a lossless replacement of the dataset. Admission is code/model controlled under operator-selected options, not per-content human editing. SRC-1, `OpenMLE-Gym/builder_core/utils/nodes.py`; minimum tail-selection passage already retained by [RT-RTE-gym-build](runtime.md#rt-rte-gym-build).

> atomic_write_text(
>     raw_placeholder,
>     fileinfo.read_text(encoding="utf-8"),
> )
> shutil.rmtree(self.structure.raw_dir(comp_id), ignore_errors=True)
> --- `OpenMLE-Gym/builder_core/utils/nodes.py`

## Write side

Acquisition differs by channel. Evo retains generated code, execution records and analysis, then derives cards and optional comparison summaries. Code admits summaries structurally, not by a demonstrated truth check. Optional model summaries can retain comparative reasons; targeted displays shorten those reasons. The cached summary is not a replacement for the raw journal, and journal export is not the complete cache. [MEM-OBJ-journal](#mem-obj-journal), [MEM-OBJ-experience-card](#mem-obj-experience-card), [MEM-RTE-summary-cache](#mem-rte-summary-cache).

RL admits selected status/categories into SQL, recomputes fitness, prunes when configured, and optionally adds summary metadata. SFT tree search can retain rejection records, whereas downstream SFT collection excludes them according to its admission rules. SFT alignment writes conversations separately from provenance manifests. Thus curation can change eligibility, representation and available rationale without proving better knowledge. Physical write agency is software; content authorship is mixed model/task-source/evaluator; the inspected subsequent admissions do not require individual human approval. Unknown initial source-dataset and database provenance does not erase these known transformations. [MEM-OBJ-rl-program](#mem-obj-rl-program), [MEM-RTE-sft-search](#mem-rte-sft-search), [MEM-OBJ-alignment-dataset](#mem-obj-alignment-dataset).

Cleanup/rejection is local, not global forgetting: island eviction can leave journal history; SQL top-k removes database rows; context clipping leaves full text in files; dataset rejection excludes a row without deleting the original rollout; Gym raw deletion keeps only a file-inventory placeholder. No inspected mechanism guarantees that rejecting an artifact withdraws all its descendants or cached summaries. That last conclusion is limited to the mechanisms actually traced, not an asserted system-wide absence. Relevant inspection limits remain in the coverage table. [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search), [MEM-OBJ-rl-program](#mem-obj-rl-program), [MEM-OBJ-alignment-dataset](#mem-obj-alignment-dataset), annotation on [RT-RTE-gym-build](runtime.md#rt-rte-gym-build).

## Read-back

| Retained result | Later consumer and selector | Delivery / budget / authority |
| --- | --- | --- |
| Evo journal and separate card files | Solver continuation, parent utilities, legacy and targeted memory operators | Reload by task checkpoint/node IDs; numeric selection plus model-interpreted context. Reconstruction has metric-info and dynamic-field limitations. [MEM-OBJ-journal](#mem-obj-journal). |
| Evo rich summary | Related-node preparation and operator rendering | Existing node/card/cache precedence; code-selected push on each call, count limits and character clipping, not a guaranteed global token limit. [MEM-RTE-summary-cache](#mem-rte-summary-cache), [MEM-RTE-targeted-memory](#mem-rte-targeted-memory). |
| RL SQL rows and summary metadata | Generation search selector, reward baseline/fitness code | Task query, success/debug predicates, parent selection and best/recent/ancestor/error context; configurable cache lifetime; prose advisory, numeric fields executable selection data. Annotation on [RT-RTE-rl-training](runtime.md#rt-rte-rl-training). |
| SFT SQL rows / checkpoint results | GreedySearch and prompt builder | Best/zero-fitness task-local parent selection; preloaded rows omit feedback/log fields. [MEM-RTE-sft-search](#mem-rte-sft-search). |
| SFT conversations | Trainer sample/token/loss-mask construction | Dataset requested by configured path; messages, not manifest metadata, enter the minimal frame. Update authority acts on weights; deployment back to Evo unresolved. [MEM-OBJ-alignment-dataset](#mem-obj-alignment-dataset). |
| Gym inventory/description and retry tail | Describe, Prepare and retry invocation | Explicit file reads and code-selected last-two-message tail; not full graph history. Saved `prepares.json` has no established later automatic consumer in inspected paths. Annotation on [RT-RTE-gym-build](runtime.md#rt-rte-gym-build). |

Storage APIs alone are not additional consumer routes: RL snapshot/clear and untraced database copies establish capabilities, not observed restore, withdrawal or later model activation. All implemented later-delivery routes above remain operation-uninspected.

## Integration issues

1. **Qualify checkpoint restoration.** [RT-RTE-evolution-search](runtime.md#rt-rte-evolution-search) correctly names journal reload, but must not imply lossless restoration of all memory. Nested metric-info export and flattened-key reload differ; cards and rich summaries require separate files. Evidence and affected source paths are retained in [MEM-OBJ-journal](#mem-obj-journal). This can alter score-source/status availability after continuation; actual resumed behavior was not observed.
2. **Do not equate empty graph updates with context erasure.** Annotation on [RT-RTE-gym-build](runtime.md#rt-rte-gym-build) identifies `add_messages` and explicit query selection. The runtime's literal statement that reset nodes return empty messages is correct; any stronger erasure inference needs correction. Actual graph-state semantics depend on the unexecuted framework; the source establishes bounded LLM inputs independently.
3. **Keep similarly named selectors separate.** RL's Improve “siblings” are children of the selected parent, unlike Evo's shared-parent siblings. The annotation on [RT-RTE-rl-training](runtime.md#rt-rte-rl-training) and [MEM-RTE-targeted-memory](#mem-rte-targeted-memory) preserve the difference; shared names do not establish identical memory operations.
4. **No duplicate declaration proposed.** Every new object/route is a material part of exactly one supplied route and declares that relation. [MEM-OBJ-journal](#mem-obj-journal), [MEM-OBJ-experience-card](#mem-obj-experience-card), [MEM-OBJ-rich-summary](#mem-obj-rich-summary), [MEM-RTE-summary-cache](#mem-rte-summary-cache), [MEM-RTE-targeted-memory](#mem-rte-targeted-memory) refine search; [MEM-OBJ-rl-program](#mem-obj-rl-program) refines RL; [MEM-OBJ-sft-program](#mem-obj-sft-program), [MEM-OBJ-alignment-dataset](#mem-obj-alignment-dataset), [MEM-RTE-sft-search](#mem-rte-sft-search) refine the broad SFT production/training route. Runtime model components and authority paths retain their identities.
5. **Unresolved included surfaces.** The coverage table retains separate vendored memory/database copies, other RL search algorithms, metadata/task-quality branches, skill loading, sandbox operational stores and NatureBench-specific context paths. Their exact consumers, edit/admission rules or replay fidelity remain partly uninspected. This prevents exhaustive whole-release equivalence/coverage claims, not the positive mechanisms established here. External corpus/checkpoint provenance and deployment additionally prevent a historical trace-to-trained-model-to-serving causal chain. [RT-CLM-meta-evolution](runtime.md#rt-clm-meta-evolution), [RT-CMP-training-models](runtime.md#rt-cmp-training-models).

## Limitations and checks

The frozen checkout HEAD was rechecked as `71ae803a035d5e3b78c19fa49ed9f67d0550cbaa`; the source identity and run ID match supplied inputs. The complete invocation, member/type inputs and records contract were read, including bounded continuation reads. No prior analyses or peer workspaces were used. Added inspection consists of the direct paths in the coverage table, not new source registrations.

This is source-level evidence of retention, automatic derivation, selection and configured delivery. Actual memory reliance, semantic summary correctness, causal benefits, cross-task transfer and historical training lineage remain unestablished. The report does not infer theory criticism from comparative summaries, or improved capacity from trace-fed writes. It does not establish an exercised self-improvement loop from the separately runnable stages.

Deterministic validation: the invocation-specific `commonplace-run validate-output` check passed with “Member content check passes; invocation residue not checked.” Its complete result was inspected. This establishes form and quotation occurrence, not semantic completeness, claim support or job acceptance.
