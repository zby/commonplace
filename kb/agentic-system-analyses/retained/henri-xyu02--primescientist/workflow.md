---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "PrimeScientist workflow account: AutoLab tree search from task delegation through verification, rejection, recovery and retained delivery."
run-id: AAS-2026-10-14-primescientist-f880686cf98a-01
reviewed-boundary: "29971beac6f4f4b41309b1326762e1b83ceece98"
---

# PrimeScientist workflow report

## Workflow account

### Selected workflow and evidence limits

This account selects the AutoLab tree-search workflow because it joins the shipped driver, reflector, coding worker and task verifier in one control path. It exposes both plan rejection before execution and score rejection after execution. It is not a constructed combination of unrelated capabilities. The operator selects AutoLab and a task through `run_search.py`; Python then owns progression without per-plan human approval. The linear baseline and FIRE-Bench remain distinct alternatives, described in the supplied runtime rather than folded into this example. See [RT-RTE-search-execution](runtime.md#rt-rte-search-execution), [RT-RTE-vanilla-retention](runtime.md#rt-rte-vanilla-retention) and [boundary](boundary.md#boundary-and-evidence).

All evidence is SRC-1 implementation or shipped prompt intent at the frozen revision. No successful run, generated plan or delivered optimization was observed. This member additionally inspected `run_search.py` bootstrap, pruning, expansion, node-runner and main-loop bodies; `benchmarks/autolab/__init__.py` setup, worker invocation and evaluation bodies; and `search/reflector.py` AutoLab prompt, initialization, log-brief and proposal-call bodies. These reads confirm the handoffs, not task-test correctness, external Codex behavior or actual reflector diagnosis. Per-task test bodies and alternate enroot verifier internals were not inspected here.

### Request, initialization and selection

The operator supplies task identity, model choices and search limits. The driver loads the adapter and existing filesystem tree, or creates a root and delegates initial plan authorship to the reflector. Initialization supplies a copied task instruction, available other-task insight files and a tree working directory. The reflector is asked to write `root/skill.md`; its successful process return alone does not establish that the file exists. AutoLab checks existence at node setup. A failed initialization returns before the final summary. SRC-1, `run_search.py`, `search/reflector.py`, `benchmarks/autolab/__init__.py`; [RT-OBJ-skill](runtime.md#rt-obj-skill), [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission).

Python selects a node using the source's stochastic BAVT implementation. An unrun node proceeds to execution; a node with a packet proceeds to expansion. Selection depends on persisted priors, visits and aggregate Q, not the worker's recommendation about what to do next. Q can include descendant results, so it is not simply the selected node's own measured reward. [RT-OBJ-stats](runtime.md#rt-obj-stats), [RT-BAP-score-selector](runtime.md#rt-bap-score-selector), SRC-1, `search/tree.py`, `run_search.py`.

### Driver to worker to verifier

AutoLab stages the chosen plan and copies task code into a new workspace. If the parent has positive Q and a retained sandbox, the driver instead supplies that workspace as the seed and adds an inheritance preamble to the staged plan. The adapter excludes prior reward output, injected agent configuration and `target` from the copy. It installs the plan as a native optimization skill, supplies the task instruction as the Codex request, prebuilds a verifier image and may write a build-check helper. The handoff contains executable workspace state and natural-language guidance, not the reflector's whole model context. Skill delivery does not establish compliance. SRC-1, `benchmarks/autolab/__init__.py`, `run_search.py`; [RT-OBJ-sandbox](runtime.md#rt-obj-sandbox), [RT-BAP-plan-worker](runtime.md#rt-bap-plan-worker).

Codex runs with the workspace as its working directory. The host invocation requests `danger-full-access` and no approval; the later verifier container is not the coding worker's confinement boundary. The adapter does not require a zero worker exit status before returning a run ID. A failed worker process that returns can therefore still yield a workspace for evaluation. This is distinct from a setup failure that returns no run ID. SRC-1, `benchmarks/autolab/__init__.py`:

> subprocess.run(
>     cmd, cwd=str(sandbox), env=agent_env,
>     stdout=f, stderr=subprocess.STDOUT,
> )
> --- `benchmarks/autolab/__init__.py`

> return timestamp
> --- `benchmarks/autolab/__init__.py`

The driver calls the adapter evaluator for each available run ID. AutoLab builds the task image, invokes task tests against the submitted workspace, and returns reward, diagnostic detail, artifact pointers and estimated cost. Image-build failure produces zero reward with an error detail. The driver's answer oracle is adapter reward, not the worker's success narrative. Task-test validity remains uninspected, so reward admission is not a guarantee of correctness or scientific truth. With repeated attempts, the driver retains the strict maximum primary score and separately accounts for nonwinning run costs. [RT-RTE-score-evaluation](runtime.md#rt-rte-score-evaluation), [RT-RTE-search-execution](runtime.md#rt-rte-search-execution), SRC-1, `run_search.py`, `benchmarks/autolab/__init__.py`.

### Result admission and successor handoff

The driver moves winning artifacts into the node, stores the packet and backpropagates the score unless score pruning applies. It appends result/cost ledgers. These writes make outcomes available to subsequent selection and reflection; they do not install code into production. Optional pruning compares a child's primary score to positive parent Q minus the threshold. It preserves the packet and artifacts, hides the branch by renaming it, and does not backpropagate that rejected score. Since the worker has already executed, this gate rejects future branch selection rather than undoing past actions. [RT-RTE-search-execution](runtime.md#rt-rte-search-execution), SRC-1, `run_search.py`.

When selection reaches a completed node, the driver asks the reflector for successors. The reflector receives the selected node path, packet/plan/workspace pointers, tree access and possibly a resumed session. Code writes a head-and-tail log brief, preferentially omitting middle trajectory lines; the full hidden log remains reachable. The AutoLab prompt asks for verifier-grounded diagnosis, targeted diff/code inspection and competing hypotheses. These are requests, not evidence of exercised criticism. SRC-1, `search/reflector.py`; [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission):

> Ground your analysis in what the verifier actually reported, not just the score
>    or the agent's own claims.
> --- `search/reflector.py`

The reflector writes successor directories; Python admits them through plan-existence and prior normalization checks. Missing or malformed priors default to 0.5; numerical priors are clamped. A present plan is not checked for semantic quality or requested provenance. Existing raw directories are processed before another model call. Later BAVT selection, rather than immediate reflector execution, decides which admitted successor receives a worker invocation. The supplied runtime establishes this admission mechanism and its theory-assessment limits. [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission), SRC-1, `run_search.py`, `search/reflector.py`.

### Failure, rejection and recovery

There are three consequential recovery owners in this selected path:

- **Driver, failed execution:** setup failure or no usable run packet leaves the node without a packet. The loop prints a failure and continues without incrementing its evaluation counter. It can select the same failed node again; the evaluation budget alone therefore does not cap these failures. Token/time/cost limits are between-operation checks, not worker preemption. [RT-RTE-search-execution](runtime.md#rt-rte-search-execution), [RT-CLM-budget-stop](runtime.md#rt-clm-budget-stop), SRC-1, `run_search.py`.
- **Driver, malformed proposal:** a missing plan causes the proposal directory to be archived with a bootstrap error. Reflection/bootstrapping retries at most twice; no ready children then stops the search. A subprocess success that writes no proposals is also insufficient. [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission), SRC-1, `run_search.py`.
- **Driver plus reflector, low-scoring branch:** code hides the child and writes `pruned_children.md`, retaining structured hypothesis/rationale/changes/risks when available, otherwise a plan excerpt, plus a short verifier tail. If all children are pruned, the driver re-expands the parent with an explicit rejection-context prompt. Code supplies the history; the reflector is asked to avoid repeating approaches, but compliance is unobserved. SRC-1, `run_search.py`, `search/reflector.py`:

> if n_pruned > 0 and n_existing == 0:
> --- `run_search.py`

> is_reexpand = (n_pruned > 0 and n_existing == 0)
> --- `run_search.py`

Filesystem resume loads prior tree state; it is not a transaction spanning packets, moves, statistics and ledgers. Reflector session continuation supplies another continuity path, with failed resume clearing saved session state. Neither establishes recovery of all model context or exact uninterrupted execution. [RT-RTE-search-execution](runtime.md#rt-rte-search-execution), [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission), SRC-1, `run_search.py`, `search/reflector.py`, `search/tree.py`.

### What counts as delivery

Normal loop termination occurs at an evaluation/resource limit, exhausted explored path or failed expansion. The driver prints a best-Q node summary and ledger location. The delivered result is the retained task tree, evaluated packets, winning node workspaces/logs and accounting records, not an automatically exported patch or independently established research conclusion. Best Q is an aggregate search statistic; no additional final verification of the printed best node occurs in the inspected termination block. The worker and reflector do not own delivery acceptance. SRC-1, `run_search.py`; [RT-RTE-search-execution](runtime.md#rt-rte-search-execution):

> bq, best  = best_node(root)
> --- `run_search.py`

> # Search tree is the source of truth — no writes back to benchmark folder.
> --- `run_search.py`

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

#### On [RT-RTE-search-execution](runtime.md#rt-rte-search-execution)

Workflow delivery boundary: AutoLab worker completion is an intermediate handoff, not delivery acceptance. Evaluation packets permit persistence/pruning; final loop termination exposes retained state through the printed best-Q summary. No extra final verification is wired in the inspected termination block. Failure recovery remains driver-owned and can retry an unrun node without consuming the evaluation count. SRC-1, `run_search.py`, `benchmarks/autolab/__init__.py`.

#### On [RT-RTE-plan-admission](runtime.md#rt-rte-plan-admission)

Workflow rejection handoff: score pruning produces a parent rejection digest before possible re-expansion. The driver supplies this context when all children are pruned; model-directed avoidance of those approaches remains requested rather than observed. Failure to produce ready proposals after two attempts stops progression to further worker delegation. SRC-1, `run_search.py`, `search/reflector.py`.
