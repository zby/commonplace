---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Agent-R workflow: WebShop search-tree collection and the separately invoked, threshold-blocked revision-conversation export."
run-id: AAS-2026-10-12-agent-r-216224d4270a-01
reviewed-boundary: "82fcc1ca7873b460949ed49022146dd988c32e31"
---

# Agent-R workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is WebShop task selection → environment-scored search tree → separately invoked revision-data construction. It was selected because the producer and consumer are both shipped, and their filesystem handoff is explicit. It follows [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection) and [RT-RTE-revision-export](runtime.md#rt-rte-revision-export), rather than joining unrelated capabilities. The delivered collection product is a JSON tree. Revision-conversation delivery is a source-defined downstream path, but its threshold comparisons prevent nontrivial exports when reached in the shipped code. The account therefore does not assert a completed training-data workflow.

Evidence is SRC-1 implementation: complete reads of `mcts_collection.py`, `path_collection.py` and `mcts_utils/webshop/mcts_ws.py`, plus the selection, backpropagation and persistence methods in `mcts_utils/mcts_raw.py` and the writer/revision prompts in `mcts_utils/llm_server.py`. These reads revisit paths already registered in [the boundary](boundary.md); they introduce no source or observed-run layer. No target execution, generated tree or exported row was supplied. External environment semantics and model behavior remain uninspected.

### 1. Caller supplies a bounded task and delegates collection

The caller starts `mcts_collection.py`, configuring `TASK=webshop`, the environment server, task-index range, model directory, generation settings and output label. The driver excludes test indices and indices outside the clean-training list. An existing `search_results_{idx}.json` suppresses recollection, without checking its provenance or completeness. This is a bounded curriculum, not an open request or a per-action human approval process (SRC-1, `mcts_collection.py`; [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection)).

For an admitted task, the driver resets the environment, constructs a FastChat conversation from the server's initial instruction, `Ok.` and the initial observation, and passes the conversation, shared client, task index and initially empty recent-action history to `ExtendedMCTS`. The local actor is [RT-CMP-func-call-offline](runtime.md#rt-cmp-func-call-offline); the output label does not guarantee a particular checkpoint or that later verifier weights match it.

### 2. Search delegates proposals, but owns action effects and successors

At an expandable node, `ExtendedMCTS` asks the actor for serial candidate responses. The actor receives a trimmed conversation, not tree statistics. Software parses each response into an action. Before executing it, software resets the shared environment to the task and replays the node's earlier actions. It stores the new response and observation in a child with the full node conversation restored. This reset/replay handoff requires reproducible external transitions and exclusive client use; it is not a separately isolated worker or a saved environment snapshot (SRC-1, `mcts_utils/webshop/mcts_ws.py`; [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection)).

The external server supplies reward and done. Negative reward makes a terminal disaster child with zero score. Software also terminates children beyond the configured depth, deduplicates exact response strings after execution, propagates terminal rewards and selects the next branch using the shared MCTS rules. The actor proposes actions; it neither approves the search successor nor commits a final solution. The computational selector prefers unvisited nonterminal children and otherwise uses accumulated value/exploration, with random tie resolution. These decision and effect boundaries are retained in [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection) and [RT-BAP-model-action](runtime.md#rt-bap-model-action).

A negative-reward child ends that branch, not the whole task. Search can continue through other nonterminal branches under its iteration budget. This is branch exploration, not rollback of an arbitrary external effect. The next candidate is reconstructed by reset/replay. Exceptions in inference or environment calls have no recovery handler in the inspected collection driver/adapter (SRC-1, `mcts_collection.py`, `mcts_utils/webshop/mcts_ws.py`).

### 3. Collection delivers a tree through the filesystem

Only after search returns does the driver save the recursive root and descendants, including conversations, action/observation histories, scores and terminal flags. It does not return a chosen solution trajectory. The filename is the stage-completion handoff, not a correctness certificate or an incremental checkpoint (SRC-1, `mcts_collection.py`, `mcts_utils/mcts_raw.py`).

> mcts_search.search(env, conv, recent_actions)
> dir_path = f"mcts_result/{Task}/{model_name}"
> file_path = f"{dir_path}/search_results_{idx}.json"
> --- `mcts_collection.py`

> def save(self, output_path):
>     state_dict = self.root.to_dict()
>     mmengine.dump(state_dict, output_path, ensure_ascii=False, indent=2)
> --- `mcts_utils/mcts_raw.py`

There is no automatic process launch across the stage boundary in these drivers. The caller separately invokes `path_collection.py` with an input directory and output directory. That script numerically sorts JSON filenames and reloads each tree; its parsed min/max/step options do not restrict this list. The caller thus owns scheduling and batch recovery (SRC-1, `path_collection.py`; [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)).

### 4. Export filtering rejects some trees and fails at numeric thresholds

On reload, a nonpositive root returns without an output row. Positive-root trees supply terminal childless paths, sorted by average score. Paired mode attempts all distinct ordered high/low path combinations satisfying a score gap; same-parent adjacency is not enforced. The environment score is the ranking signal, not a reference answer shown to the verifier (SRC-1, `path_collection.py`; [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)).

> root = ExtendedMCTS.load(data_path)
> if root.value <= 0:
>     return
> --- `path_collection.py`

A substantive failure path occurs before critique: `BETA` is an environment string compared with a float. The later high-path `ALPHA` comparison has the same defect. A standard shell export does not change Python's string-valued environment lookup. Consequently paired mode with distinct paths reaching the gap comparison raises a type error; `good` mode with a leaf reaching its threshold also fails. Nonpositive roots and empty candidate sets can return without reaching these comparisons. Neither bypassing critique with `--revise 0` nor selecting `good` fixes the relevant numeric defect. The exact threshold passages are supplied by [RT-RTE-revision-export](runtime.md#rt-rte-revision-export), SRC-1, `path_collection.py`.

The inspected script has no exception handler around `process_files`/`main`, conversion fallback or automatic retry. Source repair is required before the intended qualifying-row route can execute. A caller restarting the unchanged script does not recover from this defect. The following steps describe the code below the failing comparisons, not an observed successful export or a claim that the defect has been fixed.

### 5. Conditional critique limits a prefix; it does not certify a correction

In paired revision mode, `revise_worst_path` supplies the verifier with a task description extracted from the stored low-path conversation, preceding actions/observations and the current action/observation. It does not supply the high path as an expected answer or the tree's reward statistics. The shipped prompt requests usefulness judgments and reasons, even describing its input as a science task when this WebShop-selected driver uses it (SRC-1, `path_collection.py`, `mcts_utils/llm_server.py`).

> You must give reasons first and then provide the response in the format: Judgement: <Good or Bad or Uncertain>
> --- `mcts_utils/llm_server.py`

Software extracts the suffix after `Judgement:` and keeps extending the low prefix when it contains `good` or `uncertain`; otherwise it includes the current node and stops. This substring rule is not a validated categorical parser. The judgment's authority is to choose a prefix boundary, not to verify successful task completion or approve a checkpoint. The exact decision passage is in [RT-RTE-revision-export](runtime.md#rt-rte-revision-export); its consumer/force is [RT-BAP-verifier-prefix](runtime.md#rt-bap-verifier-prefix). The local `flag` set for a disaster is not returned or used to veto conversation construction (SRC-1, `path_collection.py`).

### 6. Conditional construction delivers a synthetic training conversation

Below the thresholds, software combines the retained initial context, low-prefix responses with loss disabled, a randomly selected stock revision thought plus `Action: wait` with loss enabled, a fabricated `ok.` observation, and the selected high continuation with loss enabled. It omits an initially identical response prefix. This is a splice of stored branches, not an environment-tested recovery rollout from the low branch's final state. The actor does not generate the inserted revision rationale; the verifier's reasons are stored separately as feedback (SRC-1, `path_collection.py`; [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)).

For this stage, delivery would mean appending an output entry containing `revise_log`, high/low logs, task description and critique feedback to the task/data-type JSONL file. There is no per-row human veto, transaction or deduplication in the writer. Partial existing output is not rolled back after a later exception, and repeated successful invocations could duplicate rows (SRC-1, `path_collection.py`, `mcts_utils/llm_server.py`).

> with open(output_file, 'a+', encoding='utf-8') as jsonl_file:
>     jsonl_file.write(json.dumps(data, ensure_ascii=False) + '\n')
> --- `mcts_utils/llm_server.py`

The workflow ends at artifact production, not installed behavioral improvement. External training and later checkpoint admission are not implementation-grounded in this artifact: see [RT-ABS-training-machinery](runtime.md#rt-abs-training-machinery) and the declared intent in [RT-CLM-iterative-training](runtime.md#rt-clm-iterative-training). The separate evaluator does not automatically consume these JSONL rows. Source wiring and a requested critique therefore establish neither successful export, corrected task execution nor improved later model performance.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-tree-collection](runtime.md#rt-rte-tree-collection)

Workflow handoff: the caller supplies task/configuration; the driver supplies initialized context and a shared environment client; search delegates only text proposal to the actor. Collection delivery is the saved recursive tree after search returns. Branch rejection through terminal/disaster marking leaves software free to explore siblings; reset/replay reconstructs their state rather than providing a general external rollback.

#### On [RT-RTE-revision-export](runtime.md#rt-rte-revision-export)

Workflow handoff: a separate caller invocation chooses the tree directory. The numeric threshold defect blocks qualifying exports before model critique. Beneath that defect, verification selects the included low-prefix boundary, while software constructs the revision cue and continuation. Delivery would be append-only conversation export, not an executed corrected trajectory or trained checkpoint. Scheduling, defect repair and output curation remain caller responsibilities.
