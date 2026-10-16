---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Prove2Me_workspace's agent-facing formalization workflow and Lean extraction helpers at commit 38e12f9d215cb103a0f9173ec230a614fcd93b61, without the enclosing agent harness or platform implementation."
run-id: AAS-2026-10-14-prove2me-workspace-187ef30582c9-01
result-disposition: complete
target-class: workflow
boundary-kind: complete artifact, partial loop
reviewed-boundary: "38e12f9d215cb103a0f9173ec230a614fcd93b61"
analysis-cutoff: "2026-10-14"
evidence-tier: doc-grounded
source:
  identity: https://github.com/prove2me/Prove2Me_workspace
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/prove2me-workspace-187ef30582c9/related-systems/prove2me--Prove2Me_workspace
  revision: 38e12f9d215cb103a0f9173ec230a614fcd93b61
  sha256: null
---

# Prove2Me_workspace boundary

## Boundary and evidence

This run examines the shipped agent skill, persistent workspace conventions, solver and captain procedures, independent statement read-back instructions, and full-project upload helpers. Its intended use is to explain how this artifact directs an external model-driven agent to discover, formalize, verify, publish, revisit and reuse mathematical work. It does not review the entire Prove2me service. The target class is **workflow**, not an enclosing runtime: the repository supplies agent instructions and two Lean extraction programs, while the agent's harness supplies execution and model calls. SRC-1, `README.md`, `SKILL.md`, `references/mission_solver.md`, `references/mission_captain.md`, `references/mission_auditor.md`.

> This repository contains both the **agent skill** ([SKILL.md](SKILL.md) + [references/](references/)) and the **working workspace** agents operate in.
> --- `README.md`

The boundary kind is **complete artifact, partial loop**. All tracked repository content is eligible evidence, including shipped drivers and consumers in the reference playbooks. The artifact prescribes the loop but does not supply its enclosing model runtime, platform backend, live shared library or actual agent execution traces. The repository tree and entry-point tracing established that `SKILL.md` routes operators to solver/captain playbooks; the solver reads earlier attempts and writes new proofs and explanations; the captain maintains proposals and milestones; and the upload playbook consumes both shipped extractors. These callers are included, not dismissed as external merely because they direct API calls. SRC-1, `SKILL.md`, `references/mission_solver.md`, `references/mission_captain.md`, `references/upload_full_project.md`.

> The orchestration code (a few Python scripts: planner, generator, uploader) is ordinary engineering you write yourself — this playbook gives you the design rules and the failure modes that are expensive to rediscover.
> --- `references/upload_full_project.md`

Functional inclusions cover credential/workspace reuse, local Lean environment setup, theorem/definition mirrors, proof and reduction submissions, verdict polling, contribution publication, proposal auditing, milestone maintenance, discussions/backlinks, and extraction-driven project conversion. The retained-state consumption paths matter: the solver is instructed to read milestone history, discussions, backlinks and prior submissions before attempting a target; the upload procedure prescribes a resumable uploader state file. These are workflow contracts, not inspected backend persistence or a shipped uploader implementation. SRC-1, `references/setup.md`, `references/lean-setup.md`, `references/mission_solver.md`, `references/communicate.md`, `references/upload_full_project.md`.

> - Before attempting an open milestone, read its edit history (`GET /milestones/:id/history`) — an event that removed or replaced a `theorem_id` marks a rejected formalization path, and the captain's `reason` tells you why. Do NOT retry an approach the captain already rejected ([missions.md](missions.md)).
> --- `references/mission_solver.md`

The frozen evidence is solely SRC-1 at full commit `38e12f9d215cb103a0f9173ec230a614fcd93b61`; the cutoff is **2026-10-14**, the supplied run date. HEAD was checked against that pin, and the tracked tree and working-tree status were inspected read-only. The overall evidence tier is **doc-grounded** because the agent loop and service contracts are instructions, not an implemented agent controller. The Lean helper programs separately support implementation-level findings about extraction. Their presence does not establish execution of the whole workflow. SRC-1, `scripts/extract_decl_graph.lean`, `scripts/extract_sketch_info.lean`.

### Repository coverage and initial inspection

This table records eligibility and initial inspection, not a whole-system coverage claim. No tracked top-level path is deliberately excluded. Files listed as not yet read remain available at the same pin; they are not access gaps and cannot yet support detailed findings.

| Top-level tracked path | Treatment and role | Initial inspection and limit |
|---|---|---|
| `.gitignore` | Included: credentials and local build-state retention boundary | Read fully; ignores credentials, toolchain/Lake configuration and build artifacts. SRC-1, `.gitignore`. |
| `README.md` | Included: artifact purpose and entry point | Read fully; directs the user to the skill and identifies workspace/server layout correspondence. SRC-1, `README.md`. |
| `SKILL.md` | Included: main agent prompt, role routing, loop and API index | Read fully; instructions are evidence of intended behavior, not agent compliance. SRC-1, `SKILL.md`. |
| `Definitions/` | Included: persistent definition-module destination | Tracked content is only `.gitkeep`; no actual retained library is supplied. SRC-1, `Definitions/.gitkeep`. |
| `Theorems/` | Included: local statement/stub destination | Tracked content is only `.gitkeep`; mirror producers/consumers were traced in the Lean setup and proving playbooks. SRC-1, `Theorems/.gitkeep`, `references/lean-setup.md`, `references/prove.md`. |
| `Solutions/` | Included: solution destination and local smoke evaluator | `.gitkeep` inventoried; `SmokeTest.lean` read fully. No test was executed. SRC-1, `Solutions/SmokeTest.lean`. |
| `references/` | Included: shipped agent procedures and state-producing/consuming API contracts | Fully read: `mission_solver.md`, `mission_captain.md`, `mission_auditor.md`, `setup.md`, `lean-setup.md`, `prove.md`, `communicate.md`, `upload_full_project.md`. Heading inventory and skill routing inspected for `campaigns.md`, `collections.md`, `contribute.md`, `curate.md`, `discover.md`, `mission_description.md`, `missions.md`; their detailed bodies are not yet inspected. No detailed claims about those unread contracts are established here. SRC-1, `SKILL.md`, `references/mission_solver.md`, `references/mission_captain.md`. |
| `scripts/` | Included: executable project-upload fact extractors | Both `extract_decl_graph.lean` and `extract_sketch_info.lean` read fully, including output generation and consumer instructions. Neither was run. SRC-1, `scripts/extract_decl_graph.lean`, `scripts/extract_sketch_info.lean`, `references/upload_full_project.md`. |
| `examples/` | Included: source-only SumSquares project and expected extraction/platform artifacts | Tree inventoried and `upload_full_project/README.md` read fully; individual Lean and JSONL artifact bodies not yet inspected. The README reports compilation, but this is not an independently inspected execution trace. SRC-1, `examples/upload_full_project/README.md`. |

### External dependencies and prevented conclusions

- **Prove2me API and website:** authentication, job queues, publication, persistent library/discussions/history, verification verdicts, reduction resolution and human/moderator launch actions are documented interfaces. Their backend implementation and live state are not in the frozen source. This prevents claims that their enforcement, persistence, isolation or automatic resolution were independently verified. SRC-1, `references/setup.md`, `references/prove.md`, `references/mission_captain.md`, `references/communicate.md`.
- **Enclosing agent harness and model provider:** the artifact asks the agent to execute commands, write orchestration code and launch blind auditors, but does not ship that runtime or its model-call policy. This prevents conclusions about scheduling, context isolation in practice, model selection, retries or actual compliance. SRC-1, `references/mission_auditor.md`, `references/upload_full_project.md`.
- **Lean, Lake, Mathlib and user-supplied source projects:** external toolchains and imports are prerequisites; project/environment scaffolding is instructed rather than bundled as an installed build. This prevents independent claims of successful compilation or environment equivalence. SRC-1, `references/lean-setup.md`, `references/upload_full_project.md`, `examples/upload_full_project/README.md`.
- **Execution evidence:** this job reads source only. No service was contacted, helper or smoke test executed, or agent episode reproduced. Expected example outputs and documentation may support bounded source-native accounts when inspected, not measured reliability, performance or causal effectiveness.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/prove2me/Prove2Me_workspace` | 38e12f9d215cb103a0f9173ec230a614fcd93b61 | doctrine/design; implementation; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/prove2me-workspace-187ef30582c9/related-systems/prove2me--Prove2Me_workspace`. Doctrine/design: `README.md`, `SKILL.md`, eight fully read playbooks named above, heading inventory of remaining references, `.gitignore`. Implementation: both `scripts/` Lean extractors and `Solutions/SmokeTest.lean`. Reported operation: worked-example README's attributed compilation account. Full tracked-tree inventory; unread example bodies and remaining reference bodies are available, not missing. | Doctrine/design: [skill](https://github.com/prove2me/Prove2Me_workspace/blob/38e12f9d215cb103a0f9173ec230a614fcd93b61/SKILL.md), [solver](https://github.com/prove2me/Prove2Me_workspace/blob/38e12f9d215cb103a0f9173ec230a614fcd93b61/references/mission_solver.md), [upload consumer](https://github.com/prove2me/Prove2Me_workspace/blob/38e12f9d215cb103a0f9173ec230a614fcd93b61/references/upload_full_project.md). Implementation: [declaration extractor](https://github.com/prove2me/Prove2Me_workspace/blob/38e12f9d215cb103a0f9173ec230a614fcd93b61/scripts/extract_decl_graph.lean), [sketch extractor](https://github.com/prove2me/Prove2Me_workspace/blob/38e12f9d215cb103a0f9173ec230a614fcd93b61/scripts/extract_sketch_info.lean). Reported operation: [example account](https://github.com/prove2me/Prove2Me_workspace/blob/38e12f9d215cb103a0f9173ec230a614fcd93b61/examples/upload_full_project/README.md). | No checkout access gap. Backend, enclosing model runtime, installed dependencies and live retained state are outside the frozen evidence; service implementation and end-to-end behavior remain unverified. No observed-run or causal-experiment layer is established. |
