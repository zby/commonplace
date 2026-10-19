---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Agent Skills for Context Engineering, including its shipped research-to-skill workflow and examples, frozen at commit 9ff0c99108b36d3b886defd825d8ac1f47dba374."
run-id: AAS-2026-10-19-agent-skills-for-context-engineering-7e663338370b-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "9ff0c99108b36d3b886defd825d8ac1f47dba374"
analysis-cutoff: "2026-10-19"
evidence-tier: code-grounded
source:
  identity: https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-agent-skills-for-context-engineering/related-systems/muratcankoylan--Agent-Skills-for-Context-Engineering
  revision: "9ff0c99108b36d3b886defd825d8ac1f47dba374"
  sha256: null
---

# Agent Skills for Context Engineering boundary

## Boundary and evidence

### Target and intended use

The target is the repository's context-engineering skill system, including the researcher operating system that maintains it and the shipped examples that produce or consume persistent context. Its intended use is to guide agents building, optimizing and evaluating agent systems, while retaining research, mechanisms and claims for later skill revisions. This is an in-scope **memory/knowledge/context-engineering system**, with a substantial builder or improvement plane. It is not classified as an enclosing agent runtime merely because some shipped examples and benchmarks issue model calls. SRC-1, `SKILL.md`, `README.md`, `researcher/README.md`, `.plugin/plugin.json`.

The target declares both a consumption path and a maintenance path:

> At startup, agents load only skill names and descriptions. Full content loads only when a skill is activated for relevant tasks.
> --- `README.md`

> This directory defines the repo-native workflow for turning external research into skill changes. It is intentionally file-based so agents can inspect, resume, and audit work without requiring a hosted scheduler.
> --- `researcher/README.md`

These are doctrine/design statements, not evidence that any particular external host follows that loading policy. The manifests supply the shipped entry points: the Open Plugins manifest points to `./skills/`; the Claude marketplace manifest bundles explicit skill directories under one plugin. SRC-1, `.plugin/plugin.json`, `.claude-plugin/marketplace.json`.

### Frozen evidence and boundary kind

The evidence is SRC-1 at full commit `9ff0c99108b36d3b886defd825d8ac1f47dba374`, with applicability cutoff **2026-10-19**. The acquired checkout's HEAD matches that revision and its working tree reported no changes. The source object above preserves the acquisition object unchanged. No additional repositories, live websites or external documents are registered. External research cited by the target is available here only as repository-contained representations, not as independently verified external evidence.

The boundary kind is **complete artifact, partial loop**. The whole Git artifact is frozen and available, including examples and maintenance tooling; this boundary does not narrow the target to a skill API or to the researcher scripts alone. Initial inspection traces plugin discovery, research-state advancement, mechanism promotion, a retained-data consumer, and the router benchmark. It does not trace every example, artifact/export implementation, validator or skill helper end to end. Those files are available but not yet inspected, not access gaps. This prevents a whole-system coverage claim at this stage. Later analysis may inspect them under SRC-1 at the same commit without adding sources.

The overall tier is **code-grounded**, because executable shipped consumers and state transitions were inspected. Skill-loading promises, research procedure and human review policies remain doctrine/design unless separately supported by implementation. No target execution, tests or provider calls were performed. No observed-run or causal-experiment layer is established by this boundary; stored reports or traces require their own inspection before supporting operational claims.

### Functional inclusions and initial trace

**Published instruction surface.** Include root collection guidance, both plugin manifests, all published `skills/` bodies, references and helper scripts, and the authoring template. The manifests and root skill map were read; individual published skill bodies and helper implementations were not yet traced. Their inclusion does not make every described algorithm an implemented runtime feature. SRC-1, `SKILL.md`, `.plugin/plugin.json`, `.claude-plugin/marketplace.json`, `README.md`.

**Research maintenance and admission.** Include researcher discovery, source retrieval, evaluations, proposals, run state, novelty checks, readiness checks, mechanism registry and ledgers, claim provenance, corpus inventory, governance, schema/artifact contracts, public export and continuous-operation drivers. These are shipped responsibilities, not an excluded enclosing application. The inspected `loop_step.py` invokes `research_loop.py` to initialize runs and record retrieval, reloads run state, and parks judgment-requiring states. In the inspected `research_loop.py` section, evaluation and proposal commands record paths and state, validation delegates to validators, and promotion appends registry and ledger records. This establishes the source-level connections, not that validators are sound or approval identities authenticated. SRC-1, `researcher/scripts/loop_step.py`, `researcher/scripts/research_loop.py`, `researcher/runbooks/autonomous-research-loop.md`.

> park_run(run_id, "needs source evaluation by human or judge agent")
> --- `researcher/scripts/loop_step.py`

The maintenance loop therefore cannot be treated as a demonstrated autonomous model-driven researcher solely from its scheduler. Its shipped instructions assign judgment and drafting work to an agent or human. SRC-1, `researcher/runbooks/autonomous-research-loop.md`, `researcher/scripts/loop_step.py`.

**Shipped consumers and evaluators.** Include all example projects and benchmark runners. The digital-brain instruction surface specifies staged loading, retained JSONL data and later reuse. Its `idea_to_draft.py` actually reloads ideas, bookmarks and past posts and prints a draft scaffold; it does not itself persist that draft or generate it through a model. The interleaved-thinking CLI's inspected optimization path calls an optimization loop, optionally writes its final prompt, and can generate a skill; the generator and internal optimization loop still require inspection. Neither shipped caller is excluded as an external host. SRC-1, `examples/digital-brain-skill/SKILL.md`, `examples/digital-brain-skill/agents/scripts/idea_to_draft.py`, `examples/interleaved-thinking/reasoning_trace_optimizer/cli.py`.

The router benchmark loads descriptions through the corpus index, sends rendered prompts through `Agent.prompt` with `settingSources: []`, and writes per-item results and a summary. It is a model-calling evaluation path distinct from the conservative continuous loop. The effectiveness runner was read in full and explicitly lacks its execution stage; a plan or dry-run is not evidence of skill-body effectiveness. SRC-1, `researcher/benchmarks/sdk-runner/src/common.ts`, `researcher/benchmarks/sdk-runner/src/runRouter.ts`, `researcher/benchmarks/sdk-runner/src/runEffectiveness.ts`.

> "Stage 3 executor not yet wired in v2.2.x scaffold. See researcher/benchmarks/PLAN.md for the v2.4.0 implementation contract. " +
> "Use --dry-run to validate task and config shape today.",
> --- `researcher/benchmarks/sdk-runner/src/runEffectiveness.ts`

### Repository coverage inventory

This inventory records initial coverage, not a whole-system completion assertion. All rows refer to SRC-1 and the tracked tree at its frozen commit.

| Top-level tracked path | Functional treatment | Initial inspection and limit |
| --- | --- | --- |
| `.claude-plugin/` | Included distribution entry point | `marketplace.json` read; external Claude loader implementation unavailable here. |
| `.plugin/` | Included distribution entry point | `plugin.json` read; external Open Plugins host behavior not established. |
| `README.md`, `SKILL.md` | Included target definition and consumption guidance | Read in full; declarations distinguished from executable guarantees. |
| `AGENTS.md`, `CLAUDE.md` | Included workspace memory and maintenance instructions | Read in full as target evidence, not worker instructions. |
| `skills/` | Included published context instructions and helpers | Tracked paths inventoried; bodies, references and helper implementations not yet inspected. No corpus-wide implementation claim. |
| `researcher/` | Included maintenance, state, admission, storage and evaluation plane | README and autonomous runbook read in full; `loop_step.py` read in full; `research_loop.py` retrieval-through-promotion section inspected; SDK description loader and router call/result section inspected; effectiveness runner read in full. Remaining scripts, schemas, run records, fixtures, inventories, reports and orchestration drivers not yet traced. No complete maintenance-loop assurance. |
| `examples/` | Included shipped production/consumption demonstrations and evaluators | Digital-brain root skill and idea-to-draft consumer read in full; interleaved-thinking CLI optimization/artifact-reload section inspected. Other consumers, generation internals and evaluations remain uninspected. No end-to-end example efficacy claim. |
| `governance/` | Included authority and export policy surface | Paths inventoried; policy and enforcement not yet inspected. No verified authority or privacy guarantee. |
| `docs/` | Included repository-contained design and research representations | Paths inventoried, content not yet inspected. No independent verification of cited research or contract conformance. |
| `template/` | Included skill-production contract | Paths inventoried, content not yet inspected. No verified authoring compliance. |
| `.github/` | Included validation/deployment integration and amendment template | Workflow and template paths inventoried, not yet inspected. No CI or deployment coverage claim. |
| `assets/` | Included potentially relevant release evidence | Release SVG paths inventoried, content not inspected. No chart-derived performance claims. |
| `CHANGELOG.md`, `CONTRIBUTING.md`, `requirements-dev.txt` | Included release, contribution and development dependency context | Paths inventoried, contents not inspected. No release-history or dependency-completeness claim. |
| `.cursorindexingignore`, `.gitignore` | Included indexing and retention configuration | Paths inventoried, contents not inspected. No verified ignored-state or indexing policy. |
| `LICENSE` | Excluded legal analysis | Its contents were not inspected; no licensing conclusion. |

### External dependencies and exclusions

External agent hosts, their skill-discovery implementations, the Cursor SDK implementation and service, model providers, operating-system scheduling services, network sources and human actions are not frozen as separate sources. Their invocation contracts can be studied through the shipped callers, but their internal behavior cannot be attributed to this target. Host loading correctness, provider reliability, scheduler execution and actual human review cannot be established here. SRC-1, `README.md`, `CLAUDE.md`, `researcher/README.md`, `researcher/benchmarks/sdk-runner/src/runRouter.ts`.

Actual private/runtime queues, bindings, live CAS contents and noncommitted benchmark outputs are not supplied as execution evidence. Repository instructions describe local runtime state separately from committed state; this prevents conclusions about current deployed throughput, private-data protection in operation, or reproducibility of published measurements from raw records without further evidence. This is distinct from available but uninspected tracked implementations and examples. SRC-1, `AGENTS.md`, `researcher/README.md`.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering` | 9ff0c99108b36d3b886defd825d8ac1f47dba374 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-agent-skills-for-context-engineering/related-systems/muratcankoylan--Agent-Skills-for-Context-Engineering`. Tracked tree inventoried. Doctrine/design: `README.md`, root `SKILL.md`, `AGENTS.md`, `CLAUDE.md`, `researcher/README.md`, `researcher/runbooks/autonomous-research-loop.md`, `examples/digital-brain-skill/SKILL.md`. Implementation/configuration: `.plugin/plugin.json`, `.claude-plugin/marketplace.json`, full `researcher/scripts/loop_step.py`, retrieval-through-promotion portion of `researcher/scripts/research_loop.py`, description-loading portion of `researcher/benchmarks/sdk-runner/src/common.ts`, call/persistence portion of `researcher/benchmarks/sdk-runner/src/runRouter.ts`, full `researcher/benchmarks/sdk-runner/src/runEffectiveness.ts`, full `examples/digital-brain-skill/agents/scripts/idea_to_draft.py`, optimization and artifact-reload portion of `examples/interleaved-thinking/reasoning_trace_optimizer/cli.py`. | [Collection](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/README.md); [plugin](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/.plugin/plugin.json); [maintenance driver](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/scripts/loop_step.py); [router](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/researcher/benchmarks/sdk-runner/src/runRouter.ts); [retained-data consumer](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering/blob/9ff0c99108b36d3b886defd825d8ac1f47dba374/examples/digital-brain-skill/agents/scripts/idea_to_draft.py). | No checkout access failure. External hosts/services and actual private runtime state are outside supplied evidence, preventing host-internal and deployed-operation conclusions. Available but uninspected material is identified above; neither whole-system coverage nor observed execution nor causal improvement is established. |
