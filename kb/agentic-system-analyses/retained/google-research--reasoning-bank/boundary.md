---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ReasoningBank's shipped WebArena and SWE-Bench memory loops at commit ed80611788292ea739f1effd31f16c53823b8a0d."
run-id: AAS-2026-10-14-reasoning-bank-f0bedcab086c-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: ed80611788292ea739f1effd31f16c53823b8a0d
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  kind: git
  identity: https://github.com/google-research/reasoning-bank
  revision: ed80611788292ea739f1effd31f16c53823b8a0d
  path: /home/zby/llm/commonplace/.commonplace/worktrees/reasoning-bank-f0bedcab086c/related-systems/google-research--reasoning-bank
  sha256: null
---

# ReasoningBank boundary

## Boundary and evidence

ReasoningBank is in scope as a model-dependent memory system. This run covers the repository's shipped implementation, not just its retrieval API or the conceptual memory-item format. Its intended use is to derive reusable reasoning from agent trajectories and supply it to subsequent web-navigation and software-engineering tasks. The source describes that intent directly (SRC-1, `README.md`):

> We introduce ReasoningBank, a memory mechanism for agents that learns from both
> successful and failed trajectories, with reasoning stored as memory content.
> --- `README.md`

The target class is **memory/knowledge/context-engineering system**, with a **whole-system** boundary. This includes the shipped callers, agents, induction prompts, retrieval and embedding-cache maintenance, trajectory persistence, feedback evaluators, and scaling variant. The WebArena driver and modified mini-swe-agent batch runner are inside the target: they own persistence and subsequent consumption, rather than being unspecified external callers. Whole-system denotes functional coverage of the shipped memory loops; it does not assert that all entry points work or that every dependency is frozen.

The initial entry-point trace establishes both sides of the memory loop:

- WebArena: `WebArena/pipeline_memory.py` invokes `WebArena/run.py`, `WebArena/autoeval/evaluate_trajectory.py`, and `WebArena/induce_memory.py` in task order. The runner reloads the JSONL bank, selects records through `WebArena/memory_management.py`, and writes selected content to the text file passed into the shipped agent. `WebArena/agents/legacy/agent.py` reads that file into the system message. Induction uses success/failure instructions and appends new records to the bank (SRC-1, these paths).
- SWE-Bench: `SWE-Bench/run.sh` enters `third_party/` and calls `mini-extra swebench`. The script registration in `third_party/pyproject.toml` and dispatch in `third_party/src/minisweagent/run/mini_extra.py` lead to `third_party/src/minisweagent/run/extra/swebench.py`. Its `process_instance` reloads the bank, retrieves prior records, calls the agent with selected memory, saves a trajectory, judges that trajectory with a model, induces new items, and appends them. `third_party/src/minisweagent/agents/default.py` places the selected content in its system message (SRC-1, these paths).
- The WebArena scaling path is also included: `WebArena/pipeline_scaling.py` launches trials and invokes `WebArena/induce_scaling.py`, whose instructions come from `WebArena/prompts/memory_instruction.py`. Inclusion is not a claim that its sampling, feedback interpretation or client wiring is correct; those require mechanism-level review (SRC-1, these paths).

Minimum implementation passages supporting inclusion of the shipped producers and consumers follow. In the WebArena induction path:

>     # write memory to jsonl file
>     with open(args.output_path, 'a') as f:
>         f.write(json.dumps({
>             "task_id": args.task.split(".")[-1],
>             "query": ex["query"],
>             "think_list": ex["think_list"],
>             "action_list": ex["action_list"],
>             "status": ex["status"],
>             "memory_items": generated_memory_item.split("\n\n"),
>             "template_id": ex["template_id"]
>         }) + '\n')
> --- `WebArena/induce_memory.py`

In the modified SWE-Bench runner, retained records are reloaded before retrieval:

>     with open(f"./memory/{model.config.model_name}.jsonl", "r") as f:
>         memory_bank = [json.loads(line) for line in f.readlines()]
> --- `third_party/src/minisweagent/run/extra/swebench.py`

The same runner subsequently persists induced content:

>         with open(f"./memory/{model.config.model_name}.jsonl", "a") as f:
>             f.write(json.dumps({
>                 "task_id": instance_id,
>                 "query": task,
>                 "memory_items": generated_memory_item,
>                 "status": "success" if status else "fail",
>             }) + "\n")
> --- `third_party/src/minisweagent/run/extra/swebench.py`

The frozen evidence is the acquired Git repository at **ed80611788292ea739f1effd31f16c53823b8a0d**, with applicability cutoff **2026-10-14**. HEAD matched that pin on inspection; the checkout reported no working-tree changes. The overall evidence tier is **code-grounded**. Source reading establishes implementation structure and declared instructions, not successful execution, measured improvement, or causal effectiveness. No target execution, provider call, dependency installation or experiment was performed.

### Repository coverage

Every top-level tracked file or directory is classified below. “Included” makes the material available for analysis within this boundary; initial inspection is distinguished from exhaustive auditing. Paths in this table are SRC-1 commit-relative anchors.

| Top-level tracked item | Decision and role | Initial inspection and limits |
|---|---|---|
| `.gitignore` | Excluded: repository hygiene. | Tree inventoried; content not inspected. No conclusion about which local outputs or credentials Git ignores. |
| `.python-version` | Included: interpreter selection. | Tree inventoried; content not yet inspected. No interpreter-compatibility conclusion. |
| `CONTRIBUTING.md` | Excluded: contribution process, not memory maintenance instructions. | Tree inventoried; content not inspected. No conclusion about contributor governance. Runtime induction instructions are included separately below. |
| `LICENSE` | Excluded: legal terms. | Tree inventoried; content not inspected. No licensing assessment. |
| `README.md` | Included: declared purpose, setup, entry points and dependency boundaries. | Read completely. Its performance framing and setup directions are doctrine/design, not execution evidence. |
| `SWE-Bench/` | Included: shipped launcher and output accounting. | Read `SWE-Bench/run.sh` and `SWE-Bench/compute_stats.py`; traced launcher to the vendored batch runner. External benchmark grading is not thereby observed. |
| `WebArena/` | Included: full web-task memory loop and feedback/scaling variants. | Inspected `WebArena/pipeline_memory.py`, `WebArena/pipeline_scaling.py`, runner reload/selection in `WebArena/run.py`, induction/persistence in `WebArena/induce_memory.py` and `WebArena/induce_scaling.py`, retrieval/cache writes in `WebArena/memory_management.py`, consumer injection in `WebArena/agents/legacy/agent.py`, and success/failure/parallel instructions in `WebArena/prompts/memory_instruction.py`. Traced `WebArena/autoeval/evaluate_trajectory.py` through saved feedback and searched `WebArena/autoeval/evaluator.py`. Also inventoried/searched alternate agents, prompting, client utilities, `WebArena/config_files/generate_config_files.py`, `WebArena/utils/evaluate_trajectory.py`, `WebArena/webarena_patch.py` and `WebArena/reeval_memevol_prompt.py`. These available ancillary paths are included but not yet exhaustively inspected; no claim of compatibility among all alternate entry points. |
| `assets/` | Included: design illustrations referenced by README, `assets/method.png` and `assets/reasoningbank.png`. | Tree inventoried; images not yet inspected. No figure-derived claim or unavailable-image gap. |
| `main.py` | Included: root executable. | Read completely; prints a greeting rather than running the memory loops. The material launchers are the benchmark paths above. |
| `pyproject.toml` | Included: root package metadata and dependencies. | Read completely; records BrowserGym, browser automation and model-client dependencies. Dependency declarations do not establish installed versions or successful setup. |
| `third_party/` | Included: shipped modified runtimes, prompts, environments and evaluation machinery, not an excluded host. | Read script registration in `third_party/pyproject.toml`, CLI dispatch in `third_party/src/minisweagent/run/mini_extra.py`, and material memory lifecycle in `third_party/src/minisweagent/run/extra/swebench.py`. Inspected prompt injection in `third_party/src/minisweagent/agents/default.py`, instructions in `third_party/src/minisweagent/memory/instruction.py`, retrieval/cache maintenance in `third_party/src/minisweagent/memory/memory_management.py`; searched standalone `third_party/src/minisweagent/memory/induce_memory.py`. The tree also includes model/environment adapters, configs, interactive/single-instance runners and trajectory saving/inspection utilities. Vendored `third_party/webarena/agent/`, `third_party/webarena/browser_env/`, `third_party/webarena/llms/`, `third_party/webarena/evaluation_harness/` and `third_party/webarena/test.raw.json` are included; searched evaluator routing and feedback code in `third_party/webarena/evaluation_harness/evaluators.py`. Ancillary adapters, raw fixtures and alternate runners are available but not yet exhaustively inspected, not access gaps. |
| `uv.lock` | Included: dependency-resolution metadata. | Tree inventoried; lock contents not yet inspected. No reproducibility or environment-reconstruction claim. |

### External dependencies and conclusion limits

External provider services, credentials and model weights, BrowserGym's installed experiment runner, hosted benchmark websites/container images, SWE-Bench datasets/task repositories and the external SWE-Bench grading service are outside the frozen source. Their declared use is visible in SRC-1 `README.md`, `pyproject.toml`, `WebArena/run.py` and `SWE-Bench/run.sh`; their live behavior and exact deployment state are not captured. Consequently this analysis cannot establish live provider behavior, environment reproducibility, actual task success, agreement between model feedback and benchmark grading, or measured memory/scaling gains. Shipped adapters and vendored benchmark/evaluator modifications remain inside the boundary; responsibility for those changes is not attributed to an external host.

No external paper, linked upstream repository, live documentation page or new revision is registered. README claims may be treated as attributed design statements, not as independent evidence from its linked paper. No supplied execution trace or causal experiment is registered. Available but initially uninspected files at the frozen commit can be inspected by later analysts under SRC-1; this register is not a path allowlist.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/google-research/reasoning-bank` | ed80611788292ea739f1effd31f16c53823b8a0d | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/reasoning-bank-f0bedcab086c/related-systems/google-research--reasoning-bank`. Implementation: entry-point, retention, reload, retrieval/cache, injection, feedback and scaling paths named in the coverage table. Doctrine/design: README setup/purpose and inspected success/failure/parallel induction prompts. Tracked tree inventoried in full; ancillary inspection limits are stated above. | Implementation: [WebArena pipeline](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/pipeline_memory.py), [WebArena induction](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/induce_memory.py), [SWE-Bench lifecycle](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/run/extra/swebench.py). Doctrine/design: [README](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/README.md), [web memory instructions](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/WebArena/prompts/memory_instruction.py), [coding memory instructions](https://github.com/google-research/reasoning-bank/blob/ed80611788292ea739f1effd31f16c53823b8a0d/third_party/src/minisweagent/memory/instruction.py). | No missing material shipped memory-loop source identified. External environments/services and execution evidence are not captured: implementation and intent do not establish successful operation, benchmark effectiveness or causality. |
