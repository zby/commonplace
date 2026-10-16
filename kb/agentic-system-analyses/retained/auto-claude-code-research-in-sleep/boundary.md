---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Auto-claude-code-research-in-sleep (ARIS), frozen at 26b95cfa0d8747078e9e43b42e20952709e561b8, with partial-loop inspection of its research workflow and shipped helpers."
run-id: AAS-2026-10-15-auto-claude-code-research-in-sleep-a8abf5f80cbb-01
result-disposition: complete
target-class: workflow
boundary-kind: complete artifact, partial loop
reviewed-boundary: 26b95cfa0d8747078e9e43b42e20952709e561b8
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-auto-claude-code-research-in-sleep/related-systems/wanshuiyin--Auto-claude-code-research-in-sleep
  revision: 26b95cfa0d8747078e9e43b42e20952709e561b8
  sha256: null
---

# Auto-claude-code-research-in-sleep boundary

## Boundary and evidence

ARIS is in scope as a model-dependent research **workflow**, not an enclosing agent runtime. Its intended use is to coordinate literature review, idea selection, experiment implementation, iterative review and optional paper production through host-executed skills. The source-native description is:

> ARIS is a research harness: composable Markdown skills that orchestrate the ML research lifecycle through cross-model adversarial collaboration.
> --- `AGENT_GUIDE.md`

This classification rests on SRC-1, `AGENT_GUIDE.md` and `skills/research-pipeline/SKILL.md`. The latter is a shipped caller, not an external application: it chains `/idea-discovery`, `/experiment-bridge`, `/auto-review-loop` and optional `/paper-writing`, specifying artifact handoffs and per-stage state transitions. Its explicit orchestration contract is:

> It orchestrates up to four major workflows in sequence. Workflow 3 (paper writing) is optional and controlled by `AUTO_WRITE`.
> --- `skills/research-pipeline/SKILL.md`

The functional boundary includes the repository's mainline and host-specific skill prompts, shared contracts, installer/update paths, reviewer bridges, persistence and validation helpers, monitoring, templates and tests. Shipped callers, retention maintenance and evaluators remain inside the target even when their implementation has not yet been inspected. The complete Git artifact is frozen; initial inspection establishes only a **partial loop**, not whole-system coverage.

The traced entry path is the Claude plugin manifest → setup command → registered Codex MCP bridge, alongside the research-pipeline skill → phase-state CLI → persisted JSON → resume selection. The bridge's complete implementation was inspected through request dispatch, subprocess launch, result conversion and saved thread options (SRC-1, `.claude-plugin/plugin.json`, `commands/setup.md`, `mcp-servers/codex-exec/server.py`). The phase helper's complete implementation was inspected through creation, status mutation, acceptance/provisional recording, persistence and resume consumption (SRC-1, `tools/run_state.py`). The caller explicitly requires re-auditing unfinished acceptance:

> A stage left `done` (gate failed/ambiguous, or the run crashed before the gate)
> is re-validated on the next resume — the acceptance obligation is never skipped.
> --- `skills/research-pipeline/SKILL.md`

These are implementation and instruction observations, not evidence that a host followed the instructions or that recorded verdict identities are genuine. The model-family classifier imported by the phase helper has not yet been inspected; its classification accuracy is not established here (SRC-1, `tools/run_state.py`).

### Initial coverage and remaining inspection

The following is an inspection map, not a source allowlist. Uninspected shipped paths remain eligible at the same registered commit. None is an access failure.

| Tracked top-level material | Boundary treatment and initial inspection | Limit on conclusions |
|---|---|---|
| `.claude-plugin/`, `.codex-plugin/`, `commands/` | Included. Read `.claude-plugin/plugin.json` and `commands/setup.md`; other manifests inventoried only. | Does not establish Codex-plugin discovery or all installation routes. |
| `skills/` | Included. Read all of `research-pipeline/SKILL.md` and `shared-references/resumable-runs.md`; read `auto-review-loop/SKILL.md` opening through calling conventions and the start of recovery state, and `research-wiki/SKILL.md` through init. Other skills, mirrors, overlays, references and local scripts inventoried only. | Does not establish full review-stop enforcement, wiki lifecycle, proof/patent workflows or platform equivalence. |
| `tools/` | Included. Read all of `run_state.py`; other files inventoried, including `research_wiki.py`, `provenance.py`, `review_gate.py`, `watchdog.py`, `iteration_log.py`, installers, update scripts, experiment queue and meta-optimization tools. | Does not establish all admission checks, retention updates, stall recovery, corpus improvement or installation correctness. |
| `mcp-servers/` | Included. Read all of `codex-exec/server.py`; other reviewer, consultation, image and Feishu servers inventoried only. | Does not establish alternative transport behavior or integration parity. |
| `templates/` | Included; inventoried, including project instructions, artifact templates and `claude-hooks/` guards/logging. Not yet read. | Does not establish template obligations or enforcement of corpus-write controls. |
| `aris-monitor/` | Included; `run.sh`, scanner, ticker, focus helpers and widget inventoried only. | Does not establish monitoring coverage or session recovery. |
| `tests/`, `.github/` | Included; test files, CI workflows and Copilot reviewer profiles inventoried only. | No test-result or evaluator-quality claim; no Copilot evidence-chain validation. |
| `AGENT_GUIDE.md`, `README.md`, `README_CN.md`, `SETUP_GUIDE.md`, `SETUP_GUIDE_CN.md`, `CONTRIBUTING.md`, `CONTRIBUTING_CN.md`, `docs/` | Included as shipped doctrine/documentation. Read all of `AGENT_GUIDE.md`; other documentation inventoried only. | Routing claims in the guide are not substitutes for unread skill specifications; deployment and recovery documentation has not been verified. |
| `.env.example`, `.gitattributes`, `.gitignore`, `LICENSE` | Included as configuration, packaging and legal context; inventoried only. | No configuration-default, distribution-policy or licensing assessment. |
| `assets/`, `community_papers/`, `xhs_post.md` | Deliberately excluded from operational analysis as presentation/community material; paths inventoried, contents not inspected. | Cannot use screenshots, the community PDF or promotional prose as proof of successful operation or research quality. |

Inventory is based on SRC-1's tracked tree at the reviewed commit. This table explicitly leaves material loop paths uninspected; consequently the boundary is not `whole-system`. The optional knowledge subsystem is part of ARIS, not a separate frozen source. Its opening specification identifies persistent paper/idea/experiment/claim entities and helper-mediated operations, but the helper and downstream consumers need further inspection before claiming an implemented closed memory loop (SRC-1, `skills/research-wiki/SKILL.md`, `AGENT_GUIDE.md`).

### Dependencies and time boundary

External dependencies include the enclosing agent hosts and their tool/skill dispatch, authenticated model services and CLIs, MCP transport clients, Python and the shell, project working directories, and task-specific compute and literature services. Setup explicitly requires an installed/authenticated Codex CLI and host MCP registration; the shipped bridge starts the external CLI rather than implementing its agent execution engine (SRC-1, `commands/setup.md`, `mcp-servers/codex-exec/server.py`). Host scheduling, context compaction, provider behavior and GPU execution are not attributed to ARIS itself. Their implementations are outside this source set, preventing conclusions about host isolation, model reliability and successful unattended execution.

The only evidence source is the acquired repository at full commit `26b95cfa0d8747078e9e43b42e20952709e561b8`; checkout HEAD was confirmed against that pin. The applicability cutoff is the supplied run date, **2026-10-15**, not a claim about when every upstream feature was deployed. No other repository, branch, live page or later revision is evidence. Overall evidence is **code-grounded**, with Markdown workflow instructions treated as doctrine/design rather than independently observed operation. No target commands, tests or model calls were executed, and no execution trace or causal experiment was supplied. This prevents claims of operational success, measured performance or causal effectiveness.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep` | 26b95cfa0d8747078e9e43b42e20952709e561b8 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-17-auto-claude-code-research-in-sleep/related-systems/wanshuiyin--Auto-claude-code-research-in-sleep`. Tracked tree inventoried. Implementation: all of `tools/run_state.py`, `mcp-servers/codex-exec/server.py`, `.claude-plugin/plugin.json`. Doctrine/design: all of `AGENT_GUIDE.md`, `commands/setup.md`, `skills/research-pipeline/SKILL.md`, `skills/shared-references/resumable-runs.md`; opening portions of `skills/auto-review-loop/SKILL.md` and `skills/research-wiki/SKILL.md` as bounded above. | Implementation: [phase-state helper](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/26b95cfa0d8747078e9e43b42e20952709e561b8/tools/run_state.py), [Codex bridge](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/26b95cfa0d8747078e9e43b42e20952709e561b8/mcp-servers/codex-exec/server.py), [plugin manifest](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/26b95cfa0d8747078e9e43b42e20952709e561b8/.claude-plugin/plugin.json). Doctrine/design: [pipeline](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/26b95cfa0d8747078e9e43b42e20952709e561b8/skills/research-pipeline/SKILL.md), [setup](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/26b95cfa0d8747078e9e43b42e20952709e561b8/commands/setup.md), [routing guide](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/26b95cfa0d8747078e9e43b42e20952709e561b8/AGENT_GUIDE.md), [resumption contract](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/26b95cfa0d8747078e9e43b42e20952709e561b8/skills/shared-references/resumable-runs.md), [review skill](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/26b95cfa0d8747078e9e43b42e20952709e561b8/skills/auto-review-loop/SKILL.md), [wiki skill](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep/blob/26b95cfa0d8747078e9e43b42e20952709e561b8/skills/research-wiki/SKILL.md). | No checkout access gap identified. Uninspected material is distinguished above from deliberate exclusions. External host/provider implementations and run evidence are not supplied: cannot establish host guarantees, end-to-end success or empirical effectiveness. |
