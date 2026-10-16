---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "PrimeScientist's shipped research-search workflow and benchmark integrations at commit 29971beac6f4f4b41309b1326762e1b83ceece98."
run-id: AAS-2026-10-14-primescientist-f880686cf98a-01
result-disposition: complete
target-class: workflow
boundary-kind: whole-system
reviewed-boundary: "29971beac6f4f4b41309b1326762e1b83ceece98"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/henri-xyu02/PrimeScientist
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/primescientist-f880686cf98a/related-systems/henri-xyu02--PrimeScientist
  revision: "29971beac6f4f4b41309b1326762e1b83ceece98"
  sha256: null
---

# PrimeScientist boundary

## Boundary and evidence

This analysis covers PrimeScientist as a model-dependent research-search **workflow**, not as the implementation of its underlying coding-agent runtime. Its intended use is budgeted research-paper replication and code optimization. The shipped driver initializes plans through a reflector, selects filesystem-backed tree nodes, launches an agent through a benchmark adapter, evaluates results, retains artifacts and scores, and uses them for subsequent selection and proposals. The boundary includes both tree search and the shipped linear baseline. SRC-1, `README.md`, `run_search.py`, `run_vanilla.py`, `search/tree.py`, `search/reflector.py`.

The target's own description establishes the intended division of labor:

> Code for **PrimeScientist**, a budget-adaptive tree-search framework for
> autonomous research agents. Each tree node is an *experimental plan*
> executed by a coding agent (Codex); a *reflector agent* reads each result and
> proposes child plans.
> --- `README.md`

The shipped driver is part of the target, not an excluded application using a library. It owns state reloading, budget checks, selection, benchmark calls, score admission, pruning and reflection. The benchmark adapters and their runners are likewise included: they stage retained plans for agent consumption, create or inherit sandboxes and return evaluation packets. The following executable call sequence grounds the workflow classification. SRC-1, `run_search.py`:

>         run_id = benchmark.run_agent(task, agent, model, run_env,
>                                      env_override=env_override,
>                                      node_dir=node.path)
>         if run_id is None:
>             continue
>         packet  = benchmark.evaluate(task, run_id)
>         primary = benchmark.primary_score(packet)
> --- `run_search.py`

The boundary is **whole-system** for the shipped PrimeScientist workflow. It includes state production and persistence in tree files and ledgers, plan and workspace inheritance, reflector prompt templates and session bookkeeping, later state reload and consumption, benchmark evaluators, task assets and launchers. This is not a claim that every task dataset or vendored evaluator internal has already been inspected. The initial inspection traces the material control paths; the coverage table distinguishes included but not-yet-inspected supporting material from unavailable evidence. SRC-1, `search/tree.py`, `search/reflector.py`, `run_search.py`, `run_vanilla.py`, `benchmarks/base.py`, `benchmarks/registry.py`.

Filesystem state is substantively inside the boundary. Tree nodes persist plans, packets, statistics and priors; the driver resumes an existing tree. The baseline reloads prior packets and stages history before further agent calls. FIRE-Bench runners consume staged task plans and any available cross-task insights, and the inheritance runner copies a parent sandbox before replacing its staged plan. These are inspected consumer paths, not merely declarations in an API. Their presence does not establish that cross-task insight production forms a functioning closed loop. SRC-1, `search/tree.py`, `run_search.py`, `run_vanilla.py`, `benchmarks/fire_bench/agents/codex/run.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`.

>     root_path = tree_dir / "root"
>     if root_path.exists() and (root_path / STATS_FILE).exists():
>         return TreeNode(root_path, task)
>     return None
> --- `search/tree.py`

The shipped benchmark integrations are AutoLab and FIRE-Bench. AutoLab stages a plan, invokes Codex in a sandbox and runs task verification through Docker or enroot. FIRE-Bench dispatches agent runners and invokes the vendored RAGChecker evaluation entry point; its inspected evaluation path derives a conclusion from a log and uses model-backed extraction/checking. OpenHands also has a shipped FIRE-Bench runner and is included as an alternate integration, despite the README's narrower supported-backend statement. Its prompt injection and Docker dispatch were inspected; operational compatibility is not established. SRC-1, `benchmarks/autolab/__init__.py`, `benchmarks/fire_bench/__init__.py`, `benchmarks/fire_bench/run_agent.py`, `benchmarks/fire_bench/agents/openhands/run.py`, `benchmarks/fire_bench/eval/RAGChecker/eval.py`, `README.md`.

The registry distinguishes shipped integrations from an unavailable optional integration:

> # Shipped in this repo. terminal_bench is dispatched but not vendored here, so
> # it is listed separately and only reported as available once importable.
> _SHIPPED = ("fire_bench", "autolab")
> --- `benchmarks/registry.py`

External dependencies include the Codex CLI and model service, optional OpenHands runtime images, container runtimes, host launch tooling, Python packages and task-specific model/data services. The target includes invocation, prompt/context injection and output handling, not those external runtimes' internal scheduling, tool policy or context management. Their implementation is not frozen here; conclusions about their internal guarantees are prevented. SRC-1, `search/reflector.py`, `benchmarks/autolab/__init__.py`, `benchmarks/fire_bench/agents/codex/run.py`, `benchmarks/fire_bench/agents/openhands/run.py`, `README.md`.

No other repository, paper linked from the README, live webpage or later revision supplies evidence. The frozen checkout is at **29971beac6f4f4b41309b1326762e1b83ceece98**, with an applicability cutoff of **2026-10-14**. HEAD matched the acquired revision and the checkout status was clean. The evidence tier is **code-grounded**: source inspection supports executable paths, while documentation supplies attributed design intent. No target execution, benchmark run or causal experiment was performed. The README reports benchmark evaluation, including MLE-Bench, but the inspected registry does not provide an MLE-Bench integration. This prevents treating that reported evaluation as a shipped, inspected execution path or as observed performance. SRC-1, `README.md`, `benchmarks/registry.py`.

### Top-level coverage

All rows refer to SRC-1 at the frozen commit. “Not yet inspected” is an inspection limit, not an access gap or exclusion from the registered repository.

| Top-level tracked path | Classification | Material paths and role | Initial inspection and conclusion limit |
|---|---|---|---|
| `.codex/` | Included configuration | `.codex/auth.json.example`: credential setup template for the agent integration | Tree inspected; template contents not yet inspected. No claim about actual credentials or authentication success. |
| `.env.example` | Included configuration | Model keys, state roots and execution-mode configuration example | Configuration role inspected through `README.md`; example contents not yet inspected. Exact variable semantics require code/example inspection. |
| `.gitignore` | Included state convention | Runtime artifacts and secret-file tracking exclusions | Tree inspected; contents not yet inspected. No exhaustive claim about ignored state. |
| `LICENSE` | Excluded legal text | Project license | Deliberate analytical exclusion; no legal interpretation or license-compliance conclusion. |
| `NOTICE` | Included provenance | Vendored-component provenance and licensing notices | Tree and README references inspected; notice contents not yet inspected. No independent provenance verification. |
| `README.md` | Included doctrine/design and reported operation | Intended research-search loop, setup, repository map and reported evaluations | Fully inspected. Claims of evaluation are attributed reports, not observed runs. |
| `benchmarks/` | Included integration, context and evaluation plane | `base.py`, `registry.py`, `utils.py`; `autolab/__init__.py` and `tasks/*/{instruction.md,task.toml,environment/,tests/,solution/}`; `fire_bench/__init__.py`, `run_agent.py`, `agents/{codex,openhands}/`, `benchmark/papers/`, `benchmark/{plan_generator.py,tree_parser.py,reflect_program.md}`, `utils/`, and `eval/RAGChecker/` | Inspected base/registry, adapter setup/run/evaluation paths, FIRE-Bench dispatcher, Codex plan-loading and inheritance paths, OpenHands instruction injection/dispatch, and RAGChecker `eval.py` scoring entry. Searched shared cost/skill helpers and preparation-tool entry points. Per-task assets, preparation-tool bodies, alternate container-helper bodies and most vendored evaluator internals remain not yet inspected; no exhaustive task correctness, preparation behavior or evaluator reliability conclusion. |
| `requirements.txt` | Included dependency declaration | Python dependency specification | Tree inspected; contents not yet inspected. No dependency-resolution or reproducibility guarantee. |
| `run_search.py` | Included enclosing workflow driver | Initialization/reload, node execution, evaluation admission, budgets, pruning, expansion and final reporting | Main loop and node runner inspected; helper call sites searched. CLI and remaining helper bodies require further inspection for exact option/retry guarantees. |
| `run_vanilla.py` | Included baseline workflow | Packet replay, history staging, best-workspace reuse, scoring and keep/revert decisions | Main loop inspected; helper call sites searched. No empirical baseline comparison. |
| `scripts/` | Included shipped callers | `run_{autolab,firebench}.sh`, matching `_vanilla.sh` launchers and `README.md` | AutoLab tree launcher fully inspected; all four launcher entry-point calls searched. Remaining launcher bodies and flag reference not yet inspected. No suite-launch compatibility guarantee. |
| `search/` | Included retained-state and reflector mechanism | `tree.py`, `reflector.py`, empty `__init__.py`; selection/statistics, plan/proposal prompts, session persistence and reflection | `tree.py` fully inspected; initialization and reflection prompts, Codex invocation/session accounting and initialization consumer inspected. Remaining proposal/admission and log-brief helper bodies not yet inspected; their exact validation guarantees require further inspection. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/henri-xyu02/PrimeScientist` | 29971beac6f4f4b41309b1326762e1b83ceece98 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/primescientist-f880686cf98a/related-systems/henri-xyu02--PrimeScientist`. Implementation: tracked tree, `search/tree.py`, `run_search.py` main loop/node runner, `run_vanilla.py` main loop, `search/reflector.py` prompts and Codex/init paths, `benchmarks/base.py`, `benchmarks/registry.py`, AutoLab and FIRE-Bench adapter paths, FIRE-Bench dispatcher, selected Codex/OpenHands runner paths, RAGChecker scoring entry and AutoLab launcher. Search-only inspection: shared cost/skill helpers, preparation-tool entry points and other launcher calls. Doctrine/design: `README.md`, interface contracts and reflector prompts. Reported operation: README evaluation/reproducibility statements; not independently checked. | Implementation: [search driver](https://github.com/henri-xyu02/PrimeScientist/blob/29971beac6f4f4b41309b1326762e1b83ceece98/run_search.py), [tree state](https://github.com/henri-xyu02/PrimeScientist/blob/29971beac6f4f4b41309b1326762e1b83ceece98/search/tree.py), [reflector](https://github.com/henri-xyu02/PrimeScientist/blob/29971beac6f4f4b41309b1326762e1b83ceece98/search/reflector.py), `run_vanilla.py`, `benchmarks/autolab/__init__.py`, `benchmarks/fire_bench/__init__.py`, `benchmarks/fire_bench/run_agent.py`, `benchmarks/fire_bench/agents/codex/run.py`, `benchmarks/fire_bench/agents/codex/run_inherit.py`, `benchmarks/fire_bench/agents/openhands/run.py`, `benchmarks/fire_bench/eval/RAGChecker/eval.py`. Doctrine/design and reported operation: [README](https://github.com/henri-xyu02/PrimeScientist/blob/29971beac6f4f4b41309b1326762e1b83ceece98/README.md), `benchmarks/base.py`, `search/reflector.py`. | No material shipped control-path access gap identified. External agent/model internals and non-shipped benchmark integrations are unavailable within this source, preventing internal-runtime and missing-integration conclusions. No supplied or generated execution evidence supports observed success, reported benchmark numbers or causal effectiveness. Included supporting files not yet inspected are listed in the coverage table. |
