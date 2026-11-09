---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "OpenResearch's shipped local research-agent workspace, orchestration, experiment state and consumers at commit 2c45ff3183b494aac4001bd44eefbe57a3c249ae."
run-id: AAS-2026-10-20-openresearch-62725ad1cd0a-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "2c45ff3183b494aac4001bd44eefbe57a3c249ae"
analysis-cutoff: "2026-10-20"
evidence-tier: code-grounded
source:
  identity: https://github.com/alphaXiv/OpenResearch
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/openresearch-62725ad1cd0a/related-systems/alphaXiv--OpenResearch
  revision: "2c45ff3183b494aac4001bd44eefbe57a3c249ae"
  sha256: null
---

# OpenResearch boundary

## Boundary and evidence

This run examines OpenResearch as the shipped local-first research-agent workspace, not just its CLI tool API or experiment database. The intended use is to explain how its agent sessions, research instructions, experiment branches, compute runs and retained evidence form an operating loop. The frozen source is SRC-1 at `2c45ff3183b494aac4001bd44eefbe57a3c249ae`; the applicability cutoff is 2026-10-20. The overall evidence tier is code-grounded. This is source inspection, not a new execution or effectiveness evaluation.

The target class is **enclosing runtime**: OpenResearch owns the local session/message model, admission and persistence infrastructure, host lifecycle and adapters around separately installed coding-agent runtimes. Those native runtimes remain nested dependencies, not implementations owned by OpenResearch. The boundary kind is **whole-system** for the software shipped in this repository. It includes the desktop/dashboard callers and standalone CLI, not merely the Rust functions they call. SRC-1 `Cargo.toml` declares the `orx` binary at `src/main.rs`; that entry point dispatches CLI commands and desktop-app startup. `src/commands/up.rs` constructs `ChatHost`, reconciles unfinished turns, recovers run supervisors, resumes persisted queues and starts the run-wake watcher.

The inspected session-layer contract makes the enclosing role explicit (SRC-1 `src/local/chat/mod.rs`):

> //! Unified chat layer for `orx up` — one session/message model over
> //! harness adapters (Claude Code, Codex, OpenCode, Cursor, Antigravity), each a local child
> //! process using the user's own login. orx's SQLite is the system of record
> //! for transcripts; each harness keeps its native session for context/resume.
> --- `src/local/chat/mod.rs`

The scope includes both persistent state and its later consumers. `src/local/opencode.rs` loads experiment and run counts from `Store`, renders project state into the bundled playbook and writes it into a session worktree alongside native skills. `src/local/harness/claude.rs` calls `ensure_playbook` on the turn path and looks up a previous native session for resume. `ui/src/queries/chat.ts` reloads session/message snapshots through the local API and merges live updates. Thus the shipped driver and UI are included even though model inference is delegated. SRC-1 `src/local/opencode.rs` provides the implementation anchor:

> let project_state = ProjectState::load(&project.id)?;
> std::fs::write(&playbook, playbook_md(project, &project_state))
> --- `src/local/opencode.rs`

Instructions are also material evidence. The system prompt routes agents to CLI state and focused skills, while result interpretation is an instructed task rather than an inference justified by a successful run status (SRC-1 `SYSTEM_PROMPT.md`, `agent-skills/orx-results/SKILL.md`):

> Never infer a result from run status or memory. Before accepting or reporting a
> run-derived claim, confirm that:
> --- `agent-skills/orx-results/SKILL.md`

Functional inclusions cover project creation/import, private session worktrees, experiment-tree creation and maintenance, run submission/supervision/cancellation/wake-up, logs and artifacts, transcript and native-context persistence/recovery/compaction, permission and invocation bridges, literature retrieval clients, reusable skills/templates, local/remote presentation, telemetry and installation/update controls. Inclusion is permission for later inspection at this same commit, not a claim that every backend or test has already been audited.

### Tracked top-level coverage

The tree and CLI dispatch were inspected to identify shipped responsibilities. “Included; mapped” denotes an included path whose role was located from the tree, manifest, dispatch or embedding references, but whose detailed internals have not yet been inspected. Such material is not an access gap or a deliberate functional exclusion.

| Top-level tracked path | Coverage and role | Initial inspection and limits |
|---|---|---|
| `src/` | Included: executable operating loop. `main.rs`; `commands/{app,up,up_remote,remote_host,agent,create_experiment,exp,supervise,serve,logs,runs,project,projects,skill,library,install_skills,discover,paper}.rs`; `local/{chat,harness,acp,opencode,claude,codex,git,experiments,projects,files,native_store,native_chats,storage,agent_skills,user_skills}.rs` or corresponding module directories; `store/`, `store.rs`, `jobs/`, `plane/`, invocation, configuration, telemetry and updates. | Entry-point dispatch read; startup, playbook generation, state loading, harness contract, Claude turn/resume, native-store roots and experiment helpers sampled. Run launch/supervision, skill embedding and client routes searched. Detailed backend parity, compaction/admission edge cases, remote transport and platform behavior remain to be inspected, not excluded. |
| `ui/` | Included: operator admission and state consumption. `src/main.tsx`, `App.tsx`, routes, `api.ts`, chat/project queries, workspace persistence, events, `components/ChatPanel.tsx`, experiment/log/artifact views; `tests/`, build metadata, translations and committed `dist/`. | API routes and chat snapshot/live-query consumer inspected. Other views, UI tests and emitted assets mapped but not yet inspected in detail. No claim of source/dist equivalence or UI correctness. |
| `SYSTEM_PROMPT.md` | Included: shared injected session playbook. | Read; rendering and project-state substitution traced in `src/local/opencode.rs`. Native channel behavior beyond the sampled adapter remains for analysis. |
| `SKILL.md` | Included: standalone CLI-agent guidance and entry into focused modules. | Cardinal experiment and command contracts inspected. Remaining reference material is included, not yet fully inspected. |
| `agent-skills/` | Included: shipped research/maintenance instructions. Compute and its backend references; experiment tree, create, git, logs, results, reports, figures/assets, paper, literature review, customization, instances, delegation and feedback. | Embedding references searched; results skill read. These are model-facing procedure evidence, not proof of agent compliance. Other skills and figure helpers are mapped for later inspection. |
| `Cargo.toml`, `Cargo.lock` | Included: binary entry point and dependency/build boundary. | Manifest read; lockfile mapped. External dependency internals are not established by declarations. |
| `build.rs`, `dist-workspace.toml` | Included; mapped: platform build and distribution configuration. | No build execution or release-reproducibility conclusion. |
| `tests/` | Included; mapped: compute, invocation-gate, logs and restart integration tests. | Compute test declarations searched; test code can establish asserted contracts after inspection, not a passing result in this run. |
| `scripts/` | Included; mapped: packaging/smoke checks, development slots, compatibility/ACP/SSH/chart/release-note tests, asset generators and demo-evidence generator. | Demo generator input/output references searched. No scripts executed; no compatibility or packaging-success conclusion. |
| `demo/` | Included; mapped: nanochat base/experiment/quick code, recorded output, evidence manifest/metrics/checkpoint metadata/tokenizer, reports and figures. Also consumed by shipped onboarding/demo code under `src/local/demo.rs`. | Evidence README and generation references searched. Not independently reproduced or authenticated; retained training outputs do not by themselves demonstrate general orchestration or research quality. |
| `docs/` | Included; mapped: local-model, rental lifecycle, Linux and Windows contracts. | Backend and deployment context; detailed claims require later reads. |
| `linux/` | Included; mapped: AppRun, desktop registration and icon. | Platform entry into the shipped app; no Linux installation test. |
| `macos/` | Included; mapped: bundle metadata and distribution instructions. | Platform packaging, not evidence of successful signing/notarization. |
| `windows/` | Included; mapped: launcher crate/source, installer and icon. | Companion desktop entry point; no Windows runtime or installer verification. |
| `.github/` | Included; mapped: CI, release/signing/build/telemetry workflows and actions, ownership/template files and readme assets. | Operational and evaluation definitions, not evidence that workflows passed. |
| `README.md`, `README.es.md`, `README.ja.md`, `README.ko.md`, `README.zh.md` | Included: product intent and user entry points. | English README read. Translations mapped, not checked for parity. Product claims remain attributed doctrine unless supported by implementation or supplied run evidence. |
| `release-notes/` | Included; mapped: release instructions and independent-chat behavior account. | Not yet inspected; historical claims cannot substitute for current implementation. |
| `AGENTS.md`, `CLAUDE.md` | Included; mapped: repository-maintainer agent instructions. | Source evidence only, not authority for this analysis; no claim that contributor guidance is injected into user research sessions. |
| `.gitattributes`, `.gitignore`, `.port-workflow.mjs`, `clippy.toml` | Excluded from functional analysis: repository hygiene, port workflow and lint configuration. | Prevents conclusions about contributor workflow completeness and lint policy; no excluded research-session or experiment-state responsibility identified from the tracked tree. |
| `LICENSE` | Excluded from mechanism analysis: licensing text. | No legal interpretation or licensing-compliance conclusion. |

### External dependencies and evidence limits

Installed harness executables and their provider/model services are outside this repository's implementation boundary. Their OpenResearch adapters, native-state location and resume bridges are inside it. The checkout therefore supports conclusions about calls, settings, persistence and recovery designed by OpenResearch, not the internals or guaranteed behavior of Claude Code, Codex, OpenCode, Cursor, Antigravity or ACP peers. SRC-1 `src/local/harness/mod.rs` defines the adapter interface; `src/local/native_store.rs` distinguishes isolated and legacy provider stores.

Compute providers and schedulers, SSH hosts/containers, local operating-system facilities, literature services, GitHub and Overleaf, account/managed-compute services and update/download endpoints are external dependencies. Their shipped clients and backend controllers remain included (`src/main.rs`, `src/commands/`, `src/jobs/`, `src/local/`). No external service implementation, credentials, moving web documentation or provider execution was acquired. This prevents claims about remote reliability, billing correctness, corpus coverage, deployment security or external API conformity beyond the code's declared/requested behavior.

No required repository source was found inaccessible. Uninspected included files are explicitly distinguished above from unavailable dependencies. The run performed no target execution, dependency installation, test run or model call. Shipped fixtures, tests and the demo can be inspected later under SRC-1, but they do not establish a new observed run or causal experiment by this analysis.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/alphaXiv/OpenResearch` | 2c45ff3183b494aac4001bd44eefbe57a3c249ae | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/openresearch-62725ad1cd0a/related-systems/alphaXiv--OpenResearch`. Implementation: tracked tree and full `src/main.rs` dispatch; `Cargo.toml`; bounded startup reads in `src/commands/up.rs`; `src/local/chat/mod.rs` session contract; `src/local/harness/mod.rs` adapter contract; `src/local/harness/claude.rs` turn/resume path; `src/local/opencode.rs` state load/render/write; `src/local/native_store.rs` provider roots; `src/local/experiments.rs` experiment helpers; `ui/src/queries/chat.ts` consumer. Searches: `src/store.rs`, `src/commands/{agent,exp,supervise}.rs`, `src/local/agent_skills.rs`, `ui/src/api.ts`, demo evidence/generator and test declarations. Doctrine/design: `README.md`, `SYSTEM_PROMPT.md`, opening/cardinal and command sections of `SKILL.md`, complete `agent-skills/orx-results/SKILL.md`. | Implementation: [entry point](https://github.com/alphaXiv/OpenResearch/blob/2c45ff3183b494aac4001bd44eefbe57a3c249ae/src/main.rs), [startup](https://github.com/alphaXiv/OpenResearch/blob/2c45ff3183b494aac4001bd44eefbe57a3c249ae/src/commands/up.rs), [playbook/state](https://github.com/alphaXiv/OpenResearch/blob/2c45ff3183b494aac4001bd44eefbe57a3c249ae/src/local/opencode.rs), [chat](https://github.com/alphaXiv/OpenResearch/blob/2c45ff3183b494aac4001bd44eefbe57a3c249ae/src/local/chat/mod.rs), [UI consumer](https://github.com/alphaXiv/OpenResearch/blob/2c45ff3183b494aac4001bd44eefbe57a3c249ae/ui/src/queries/chat.ts). Doctrine/design: [prompt](https://github.com/alphaXiv/OpenResearch/blob/2c45ff3183b494aac4001bd44eefbe57a3c249ae/SYSTEM_PROMPT.md), [result instructions](https://github.com/alphaXiv/OpenResearch/blob/2c45ff3183b494aac4001bd44eefbe57a3c249ae/agent-skills/orx-results/SKILL.md), [README](https://github.com/alphaXiv/OpenResearch/blob/2c45ff3183b494aac4001bd44eefbe57a3c249ae/README.md). | No repository access gap identified. Initial inspection is not exhaustive and is not an allowlist. External harness/service internals and authenticated deployments unavailable; no fresh execution evidence, so runtime success, agent compliance and research effectiveness remain unestablished. Demo evidence is mapped but not assessed here as an observed-run layer. |
