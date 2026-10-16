---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Agent-R's shipped trajectory collection, revision-data construction and evaluation at commit 82fcc1ca7873b460949ed49022146dd988c32e31, with the training loop only partly evidenced."
run-id: AAS-2026-10-12-agent-r-216224d4270a-01
result-disposition: complete
target-class: builder or improvement plane
boundary-kind: complete artifact, partial loop
reviewed-boundary: "82fcc1ca7873b460949ed49022146dd988c32e31"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/ByteDance-Seed/Agent-R
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/agent-r-216224d4270a/related-systems/ByteDance-Seed--Agent-R
  revision: "82fcc1ca7873b460949ed49022146dd988c32e31"
  sha256: null
---

# Agent-R boundary

## Boundary and evidence

This run characterizes Agent-R as a model-dependent agent improvement plane: its shipped code collects search trees from environment interactions, reloads them to construct revision-training conversations, and evaluates an actor through environment actions. It includes the shipped drivers, not just the MCTS library. The intended use is to distinguish executable data-construction and agent-control responsibilities from the declared iterative self-training method. The classification is grounded in SRC-1, `README.md`, `mcts_collection.py`, `path_collection.py`, `eval.py` and `mcts_utils/llm_server.py`.

The repository names its three shipped entry points directly (SRC-1, `README.md`):

> - `mcts_collection.py`: Implements the MCTS-based trajectory generation framework.
> - `path_collection.py`: Generates revision trajectories based on model-guided evaluation.
> - `eval.py`: Script for evaluating the agent's performance across specified tasks.
> --- `README.md`

Functional inclusions are task selection and environment-client initialization; conversation initialization; local model inference and the alternative API wrapper; MCTS action generation, environment reset/replay, reward propagation and tree persistence; reloading trees, model-guided action critique and revision-conversation export; and evaluation rollout/result persistence. All three task adapters—WebShop, SciWorld and TextCraft—are included. The revision prompt and revision-thought strings are shipped in `mcts_utils/llm_server.py`, not an external instruction layer. The data-to-consumer edge is visible in the revision driver (SRC-1, `path_collection.py`):

> root = ExtendedMCTS.load(data_path)
> --- `path_collection.py`

> write_to_jsonl(output_dir, output_entry)
> --- `path_collection.py:247-247`

The selected boundary is **complete artifact, partial loop**, not whole-system. It covers the acquired repository artifact but cannot close the advertised iterative model-improvement loop. The README delegates training to Xtuner and names a training configuration and `xtuner_config/` directory that are absent from the tracked tree at this commit. Thus training ingestion, optimization, checkpoint admission and automated iteration back into collection are not implementation-grounded here. This is missing evidence for advertised responsibilities, not exclusion of the shipped collection or evaluation drivers. SRC-1, `README.md`, supplies the training intent:

> Before starting the training process, modify the `llama3_8b_instruct_full_alpaca_e3_copy.py` script with the necessary settings, as outlined in the [Xtuner tutorial](https://github.com/InternLM/xtuner/tree/main/docs/en/user_guides).
> --- `README.md`

External dependencies include AgentGym's environment clients and servers, vLLM and Transformers for local inference, FastChat conversation templates, mmengine serialization, and Xtuner for the documented training stage. An alternative wrapper uses OpenAI/Azure configuration. Their implementations and model checkpoints are not frozen sources in this run. Consequently this boundary does not establish environment-transition correctness, model behavior, training semantics or dependency compatibility. Initial task instructions come from `env.conversation_start`, so their externally supplied contents cannot be characterized from this checkout alone (SRC-1, `mcts_collection.py`, `eval.py`, `mcts_utils/llm_server.py`, `requirements.txt`, `README.md`).

The evaluator reads `test_id/{Task}_test.json`, while the tracked test JSON files are under `mcts_utils/`; `test_id/` is not shipped. That missing input prevents concluding that the documented evaluator is runnable unchanged, but does not prevent inspection of its control flow. No target code or tests were executed, and no generated search trees, revision outputs, training artifacts or execution traces were supplied. Source inspection supports implementation and declared design, not observed success or a causal claim that revision training improves performance (SRC-1, `eval.py`, `README.md`).

### Tracked artifact coverage

The table accounts for every top-level tracked entry. Included means within the functional evidence boundary; it does not assert that every byte has already been inspected. Available material not yet inspected remains distinct from missing evidence.

| Top-level entry | Treatment and material paths | Initial inspection and limits |
|---|---|---|
| `README.md` | Included: declared method, entry points, dependency setup, training and evaluation instructions | Fully inspected; design evidence, not proof of execution. |
| `mcts_collection.py` | Included: task dispatch, environment setup, search invocation and persisted tree naming | Fully inspected; producer and persistence driver, not an external host. |
| `path_collection.py` | Included: persisted-tree consumer, path selection, model critique, revision conversations and JSONL export | Fully inspected; does not establish subsequent optimizer ingestion. |
| `eval.py` | Included: test-task driver and evaluation consumer of the configured actor | Fully inspected; its referenced `test_id/` input directory is absent. |
| `mcts_utils/` | Included: `mcts_raw.py`, `llm_server.py`, `webshop/mcts_ws.py`, `textcraft/mcts_tc.py`, `sciworld/mcts_sci.py`, `sciworld/eval_utils_sw.py`, `sciworld/data_utils_sw.py`, and the task test/train JSON files | Core MCTS, wrappers, prompts, rollout/persistence helpers and all three adapters fully inspected. SciWorld action validation inspected in `eval_utils_sw.py` through line 166; remaining helpers, `data_utils_sw.py` and JSON contents available but not yet inspected. No claims about their full data coverage or auxiliary prompting behavior are established here. |
| `requirements.txt` | Included: declared dependency versions | Fully inspected; no installation or compatibility check. |
| `assets/` | Included as available design material: `method.png`, `method.pdf` | Tracked paths established; contents not yet inspected. No diagram-specific conclusions used. |
| `.gitignore` | Excluded from functional analysis: repository housekeeping | Tracked presence inspected, contents not read; no conclusion about ignored artifact retention policy. |
| `LICENSE` | Excluded from functional analysis: legal terms | Tracked presence inspected, contents not read; no legal assessment. |
| `Notice.txt` | Excluded from functional analysis: notice metadata | Tracked presence inspected, contents not read; no attribution-compliance assessment. |

The frozen revision is `82fcc1ca7873b460949ed49022146dd988c32e31`; the checkout HEAD was verified against the acquired pin. The applicability cutoff is 2026-10-12, the supplied run date. It does not imply inspection of later development, live linked documents or the external paper. Overall evidence is code-grounded, with README statements separately treated as doctrine/design.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/ByteDance-Seed/Agent-R` | 82fcc1ca7873b460949ed49022146dd988c32e31 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/agent-r-216224d4270a/related-systems/ByteDance-Seed--Agent-R`. Tracked tree enumerated. Implementation: `mcts_collection.py`, `path_collection.py`, `eval.py`, `mcts_utils/mcts_raw.py`, `mcts_utils/llm_server.py`, all three task MCTS adapters, `mcts_utils/sciworld/eval_utils_sw.py` through line 166, and `requirements.txt`. Doctrine/design: full `README.md`. Other available paths and deliberate exclusions are distinguished in the coverage table. | Implementation: [collection driver](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_collection.py), [revision driver](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/path_collection.py), [evaluation driver](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/eval.py), [model calls, prompts and persistence](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/mcts_utils/llm_server.py), `mcts_utils/mcts_raw.py`, `mcts_utils/webshop/mcts_ws.py`, `mcts_utils/textcraft/mcts_tc.py`, `mcts_utils/sciworld/mcts_sci.py`, `mcts_utils/sciworld/eval_utils_sw.py`, `requirements.txt`. Doctrine/design: [README](https://github.com/ByteDance-Seed/Agent-R/blob/82fcc1ca7873b460949ed49022146dd988c32e31/README.md). | Implementation gaps: documented training configuration and evaluator's `test_id/` are absent; external environments, training software and checkpoints are not captured, preventing end-to-end training and execution conclusions. Design limits: README intent does not establish implementation or efficacy. No observed-run or causal-experiment layer supplied. Available but uninspected material is not an access gap. |
