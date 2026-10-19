---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ACE's playbook adaptation framework and shipped evaluation callers at commit 82709de050e1db6e6ef2f07bcb0393560b94992a, with the AppWorld submodule unavailable."
run-id: AAS-2026-10-18-ace-007571102a54-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "82709de050e1db6e6ef2f07bcb0393560b94992a"
analysis-cutoff: "2026-10-18"
evidence-tier: code-grounded
source:
  identity: https://github.com/ace-agent/ace
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-ace/related-systems/ace-agent--ace
  revision: 82709de050e1db6e6ef2f07bcb0393560b94992a
  sha256: null
---

# ACE boundary

## Boundary and evidence

This run analyses how ACE produces, updates, persists, reloads and consumes a playbook of task-solving knowledge. The intended use is an implementation-grounded account of that adaptation loop, including its shipped evaluation callers, rather than an audit of benchmark performance. ACE qualifies as a memory/knowledge/context-engineering system: its generator consumes playbook text, its reflector supplies feedback, and its curator issues model-mediated changes to retained context (SRC-1, `ace/ace.py`, `ace/core/generator.py`, `ace/core/curator.py`).

> prompt = GENERATOR_PROMPT.format(playbook, reflection, question, context)
> --- `ace/core/generator.py`

> self.playbook, self.next_global_id, operations, _ = self.curator.curate(
> --- `ace/ace.py`

The boundary includes both sequential `ACE` and batched `ACEBatch`, their model prompts, the optional bulletpoint analyzer, deterministic playbook operations, model-call and logging utilities, and the Finance and two Mind2Web evaluation paths. These callers are part of the target, not excluded host applications: they select the orchestrator, load initial playbook files, and run training or evaluation (SRC-1, `eval/finance/run.py`, `eval/mind2web/run.py`, `eval/mind2web2/run.py`). Persistence is traced from orchestrator output back to caller input and generator consumption (SRC-1, `ace/ace.py`, `utils.py`, `ace/core/generator.py`).

> final_playbook_path = os.path.join(save_path, f"final_playbook.txt")
>         with open(final_playbook_path, "w") as f:
>             f.write(self.playbook)
> --- `ace/ace.py:818-820`

> def load_initial_playbook(path):
>     """Load initial playbook if provided."""
>     if path and os.path.exists(path):
>         with open(path, 'r') as f:
>             return f.read()
>     return None
> --- `eval/finance/run.py`

The batched path is material, not an interchangeable name for the sequential loop. Its inspected update stage generates grouped curator proposals against a shared base playbook, reduces them, then applies the resulting operations (SRC-1, `ace/ace_batch.py`).

> final_operations, _ = self.curator.aggregate_operations(
> --- `ace/ace_batch.py`

The boundary kind is **complete artifact, partial loop**, not whole-system. The frozen main repository is available, but its `ace-appworld` Gitlink points to a separate repository whose contents are absent from the acquired checkout. The tracked `.gitmodules` identifies that dependency; the tree pins it to `9f3e92155345a9159f3a8b25abc334eeca05b545` (SRC-1, `.gitmodules`, `ace-appworld`). That pointer is not a second frozen source. Its absence prevents implementation conclusions about AppWorld environment interaction, feedback, retained-state consumption and the full AppWorld adaptation loop. The main repository's benchmark claims remain author reports, not verified outcomes (SRC-1, `README.md`). No additional repository is acquired or silently admitted.

> [submodule "ace-appworld"]
> 	path = ace-appworld
> 	url = https://github.com/ace-agent/ace-appworld.git
> --- `.gitmodules`

The applicability cutoff is 2026-10-18. The reviewed boundary is exactly commit `82709de050e1db6e6ef2f07bcb0393560b94992a`; the checkout HEAD was checked against acquisition. No claim covers later revisions. The overall evidence tier is **code-grounded**. Reading implementation is not execution evidence: this run has not executed ACE, tests, examples or model calls. Provider behavior, embedding-model behavior, realized reliability, cost and causal performance gains cannot be established from these inspections. External model services, Python packages and user-supplied data or initial playbooks remain dependencies, not additional evidence sources (SRC-1, `pyproject.toml`, `eval/finance/run.py`, `ace/core/generator.py`).

### Repository coverage and remaining inspection

This inventory records the functional scope and initial inspection, not a claim that every included file has already been read. Included but uninspected files remain available at the registered commit for later jobs. They are not access gaps.

| Top-level path | Status and material paths | Role and conclusion limits |
|---|---|---|
| `ace/` | Included; inspected training and persistence sections of `ace/ace.py`, proposal/reducer stage of `ace/ace_batch.py`, `core/generator.py`, curator application section of `core/curator.py`, and `prompts/generator.py`; searched other component and prompt definitions. | Orchestration, feedback, admission, later consumption and optional maintenance. Remaining reflection, analyzer, prompt and mode details require further inspection before detailed behavioral claims. |
| `eval/` | Included; inspected initial-playbook loading, orchestrator selection and invocation in `finance/run.py`, `mind2web/run.py`, `mind2web2/run.py`; searched processor and preparation entry points. Tracked `finance/data/` and each `data/sample_config.json` remain included but not content-inspected. | Shipped callers, scoring, data preparation and input fixtures. Dataset-level scoring and preparation semantics are not yet established. |
| `utils.py` | Included; inspected parallel test-set evaluation and generator consumption; searched client initialization and extraction definitions. | Shared evaluation and provider setup; remaining details await inspection. |
| `playbook_utils.py` | Included; searched parsing, counter update, operation application and extraction definitions. | Deterministic retained-state manipulation; detailed operation semantics await inspection. |
| `llm.py` | Included; searched entry point and imports. | Model transport, timing and errors; detailed retry and provider semantics await inspection. |
| `logger.py` | Included; searched logging entry points. | LLM, bullet usage, curator differences and failures; detailed log semantics await inspection. |
| `README.md` | Included; inspected. | Declared architecture, usage, persisted outputs and attributed performance reports, not run evidence. |
| `EXTENDING_ACE.md` | Included; not yet content-inspected. | Task-extension instructions; no detailed contract conclusion yet. |
| `tutorials/` | Included; `ExtendingDatasets.md` not yet content-inspected. | Dataset-extension instructions; no detailed contract conclusion yet. |
| `ace-appworld` | Unavailable Gitlink content; pointer and `.gitmodules` inspected. | Prevents AppWorld implementation and full-loop conclusions. |
| `.gitmodules` | Included; inspected. | Submodule identity declaration only. |
| `pyproject.toml` | Included; inspected. | Package requirements and dependencies, not installed behavior. |
| `uv.lock` | Included; not yet content-inspected. | Dependency resolution metadata; no reproducible-environment conclusion yet. |
| `.env.example` | Included; not yet content-inspected. | Provider configuration surface; no detailed configuration conclusion yet. |
| `.python-version` | Included; not yet content-inspected. | Interpreter selection metadata; no compatibility conclusion yet. |
| `.gitignore` | Deliberately excluded from functional analysis. | Repository hygiene; no conclusion about which local runtime outputs Git ignores. |
| `LICENSE.txt` | Deliberately excluded from functional analysis. | Licensing; no legal or redistribution assessment. |
| `assets/` | Deliberately excluded; `images/ace_framework.png` not inspected. | Illustrative diagram; no additional design claims inferred from image content. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/ace-agent/ace` | 82709de050e1db6e6ef2f07bcb0393560b94992a | implementation; doctrine/design; reported operation | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-ace/related-systems/ace-agent--ace`. Implementation: tree and entry-point searches; selected training/update/persistence sections of `ace/ace.py` and `ace/ace_batch.py`; generator and curator application; all three evaluator caller tails; shared test evaluation in `utils.py`. Doctrine/design: `README.md`, `ace/prompts/generator.py`, `.gitmodules`, `pyproject.toml`. Reported operation: benchmark and efficiency claims in `README.md`, attributed only. The coverage table distinguishes full inspection, bounded sections, searches and pending reads. | [Sequential loop](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/ace.py); [batched loop](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/ace/ace_batch.py); [Finance caller](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/eval/finance/run.py); [declared design and results](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/README.md); [submodule declaration](https://github.com/ace-agent/ace/blob/82709de050e1db6e6ef2f07bcb0393560b94992a/.gitmodules). Other initially inspected anchors: `ace/core/generator.py`, `ace/core/curator.py`, `ace/prompts/generator.py`, `eval/mind2web/run.py`, `eval/mind2web2/run.py`, `utils.py`, `pyproject.toml`. | AppWorld submodule contents unavailable: no AppWorld implementation or full adaptation-loop conclusion. No inspected execution trace or intervention: no observed-run or causal-experiment layer and no validation of reported performance. External pages linked by the README were not admitted as evidence. |
