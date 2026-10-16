---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Wuphf's shipped agent office and routine service at a frozen Git revision, with partial operational-loop inspection."
run-id: AAS-2026-10-15-wuphf-b246722f99c0-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: complete artifact, partial loop
reviewed-boundary: "88023d4dac7491b6e71dbc1e86d274c435b9cb2c"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/nex-crm/wuphf
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/wuphf-b246722f99c0/related-systems/nex-crm--wuphf
  revision: "88023d4dac7491b6e71dbc1e86d274c435b9cb2c"
  sha256: null
---

# Wuphf boundary

## Boundary and evidence

This run examines the shipped agent office, including its state and knowledge mechanisms, for an account of how it coordinates model-dependent work. The source currently calls the product **gawkbot**; this is the content of the acquired repository, not a change to the supplied source identity. The cutoff is 2026-10-15 and the frozen revision is `88023d4dac7491b6e71dbc1e86d274c435b9cb2c`. The acquired checkout's HEAD was verified against that revision. All evidence comes from SRC-1; no live deployment or target execution was inspected.

The target class is **enclosing runtime**: the shipped launcher starts the broker, web server and background dispatch machinery, rather than merely returning a library result. It can delegate model execution to external CLI runtimes and also ships a model-dependent workflow-building service. Calling a CLI does not move the shipped broker and launcher outside this target. SRC-1, `internal/team/launcher_web.go`, `cmd/wuphf/main.go`, `desktop/oswails/main.go`, `agent/src/buildAgent.ts`.

> // LaunchWeb starts the broker, web UI server, and background bots without tmux.
> --- `internal/team/launcher_web.go`

> go l.notifyBotsLoop()
> go l.notifyTaskActionsLoop()
> go l.notifyOfficeChangesLoop()
> go l.watchdogSchedulerLoop()
> --- `internal/team/launcher_web.go`

> const res = await completeFn(model, ctx, {
> apiKey: opts.apiKey ?? apiKeyFor(model),
> signal: deadline.signal,
> } satisfies StreamOptions);
> --- `agent/src/buildAgent.ts`

The boundary kind is **complete artifact, partial loop**. The complete pinned repository supplies evidence, but this boundary's initial tracing does not establish whole-system coverage. In particular, the frontend, MCP admission routes, agent adoption, alternate execution paths, knowledge maintenance and evaluators have not all been traced through their consumers. These are available evidence, not access gaps or excluded enclosing applications. This prevents claiming an exhaustive account of all shipped loops or universal enforcement of the README's approval and knowledge promises. Later analysis may inspect additional paths in the same registered repository and revision without changing the source boundary.

Functional inclusions are the Go office broker and launcher, task dispatch and recovery, provider adapters, MCP tools and approval handling, retained workspace state, private/shared memory and wiki mechanisms, context assembly, app construction, the Bun agent service, persisted tools and routine transcripts, shipped user interfaces and their callers, instructions/prompts, and source-level evaluation machinery. The initial trace confirms that the broker's scheduler and the agent service are parts of one shipped routine path, not unrelated projects. SRC-1, `internal/team/scheduler_operator_routines.go`, `agent/src/service.ts`, `agent/src/routineRunner.ts`.

> req, err := http.NewRequestWithContext(ctx, http.MethodPost, baseURL+"/routines/run", bytes.NewReader(body))
> --- `internal/team/scheduler_operator_routines.go`

> const session = await sessions.ensureRoutineSession(agent, routine.slug, routine.name);
> const at = now().toISOString();
> await sessions.append(agent, session.id, { from: "you", body: `(scheduled) ${routine.prompt}`, at });
> await sessions.append(agent, session.id, { from: "nex", body: outcome, at: now().toISOString() });
> --- `agent/src/routineRunner.ts`

Retained knowledge consumption is also inside the boundary: the inspected context assembler calls learning/wiki search seams and builds a task knowledge packet. Its presence establishes a shipped consumption path, not retrieval quality or complete wiring coverage. SRC-1, `internal/team/context_assembler.go`.

> header := "RELEVANT TEAM KNOWLEDGE (matched to this task — apply it; cite the learning/wiki id when you do):"
> footer := "When you use retrieved context, cite its id in your messages."
> return header + "\n" + strings.Join(lines, "\n") + "\n" + footer, manifest
> --- `internal/team/context_assembler.go`

### Initial coverage and remaining inspection

The tracked repository tree was enumerated. This table distinguishes initial source reading/search from paths only located in that tree; it is not a whole-system coverage claim. Paths listed as untraced remain functionally included unless explicitly excluded below. All rows refer to SRC-1.

| Area | Initial inspection | Remaining limit |
|---|---|---|
| CLI and desktop drivers | Entry-point search in `cmd/wuphf/main.go` and `desktop/oswails/main.go` reaches `NewLauncher`/`LaunchWeb`; read startup in `internal/team/launcher_web.go`; searched `launcher_boot.go`, `launcher_wiring.go`, `launcher_loops.go` | Full CLI command modes, desktop callbacks and shutdown/recovery behavior not traced |
| Office persistence and per-task runtime selection | Read initial definitions and file loading in `internal/team/broker_persistence.go`; read task identity/resolution in `internal/team/headless_runtime.go` | Save/load integration, all alternate runners, task admission and provider execution not fully traced |
| Routine producer and consumer | Read broker HTTP dispatch and run-state handling in `internal/team/scheduler_operator_routines.go`, service routing/setup in `agent/src/service.ts`, and all of `agent/src/routineRunner.ts`; read `agent/src/buildAgent.ts` | Scheduler registration, service supervision, stored-tool execution, session/store implementations and UI consumption still need tracing |
| Knowledge production, maintenance and use | Read queue/request contract in `internal/team/wiki_worker.go`, task knowledge packet in `internal/team/context_assembler.go`; searched `internal/team/memory_backend.go` and `internal/team/task_completion_hook.go` | Full extraction, synthesis, indexing, repair, promotion, backend selection, prompt assembly and MCP admission remain untraced |
| Other shipped application surfaces | Located `web/src/`, `apps/ios/`, `internal/teammcp/`, `internal/agentdetect/`, `internal/action/`, `internal/computer/`, `internal/hostcomputer/`, `internal/workspaces/`, `runner/`, `packages/protocol/`, `templates/`, and `claude-code-plugin/` | Tree presence is not executable-behavior inspection; no end-to-end coverage or safety guarantee follows |
| Prompts, instructions and evaluation | Read `README.md` and `ARCHITECTURE.md`; located `prompts/`, `internal/team/prompts/`, `evals/`, `bench/`, `tests/`, embedded unit tests, and evaluation commands under `cmd/` | Prompt and maintenance contracts and evaluation conditions/results have not been assessed; architecture prose may lag code |

### Exclusions, dependencies and evidence limits

External model providers, installed agent CLIs, Hermes/OpenClaw gateways, GBrain, external action services, operating-system facilities and remote computers are dependencies, not independently frozen implementations in this run. Their adapters and shipped callers remain included. Their internal behavior, service availability, model quality and guarantees cannot be concluded from adapter code. The source describes CLI and gateway choices and external action providers in SRC-1, `README.md`; GBrain client dependencies are visible in `internal/team/memory_backend.go`. None of those external systems receives a separate source ID.

Runtime workspace contents, user credentials, external repositories edited by agents, downloaded releases and moving linked web pages are excluded because they were not captured. This prevents conclusions about actual user data, production outcomes, packaged-binary equivalence or external documentation at the cutoff. The locally tracked `gawkbot` binary is not a substitute for inspected source or a demonstrated deployment.

Branding/media under `assets/` and `brand/`, marketing surfaces under `landing/` and `website/`, and development/release configuration are available repository material but not evidence of successful agent operation. They may support attributed product intent or packaging claims after inspection, not observed behavior. No source access failure was encountered. Available but uninspected material is identified above; it is not called unavailable. No tests, examples, model calls or services were executed. Overall evidence is **code-grounded**, with documentation used only for declared intent. No observed-run or causal-experiment layer is established here.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/nex-crm/wuphf` | 88023d4dac7491b6e71dbc1e86d274c435b9cb2c | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/wuphf-b246722f99c0/related-systems/nex-crm--wuphf`. Implementation: tracked-tree inventory; entry-point searches in `cmd/wuphf/main.go`, `desktop/oswails/main.go`; startup in `internal/team/launcher_web.go`; searches in `internal/team/launcher_boot.go`, `internal/team/launcher_wiring.go`, `internal/team/launcher_loops.go`; portions of `internal/team/broker_persistence.go`, `internal/team/headless_runtime.go`, `internal/team/wiki_worker.go`, `internal/team/context_assembler.go`, `internal/team/scheduler_operator_routines.go`, `agent/src/service.ts`; full `agent/src/buildAgent.ts`, `agent/src/routineRunner.ts`; searches in `internal/team/memory_backend.go`, `internal/team/task_completion_hook.go`. Doctrine/design: `README.md`, `ARCHITECTURE.md`. | Implementation: [launcher](https://github.com/nex-crm/wuphf/blob/88023d4dac7491b6e71dbc1e86d274c435b9cb2c/internal/team/launcher_web.go), [routine dispatch](https://github.com/nex-crm/wuphf/blob/88023d4dac7491b6e71dbc1e86d274c435b9cb2c/internal/team/scheduler_operator_routines.go), [routine execution](https://github.com/nex-crm/wuphf/blob/88023d4dac7491b6e71dbc1e86d274c435b9cb2c/agent/src/routineRunner.ts), [model call](https://github.com/nex-crm/wuphf/blob/88023d4dac7491b6e71dbc1e86d274c435b9cb2c/agent/src/buildAgent.ts), [context assembly](https://github.com/nex-crm/wuphf/blob/88023d4dac7491b6e71dbc1e86d274c435b9cb2c/internal/team/context_assembler.go). Doctrine/design: [README](https://github.com/nex-crm/wuphf/blob/88023d4dac7491b6e71dbc1e86d274c435b9cb2c/README.md), [architecture](https://github.com/nex-crm/wuphf/blob/88023d4dac7491b6e71dbc1e86d274c435b9cb2c/ARCHITECTURE.md). | No encountered checkout access gap. Partial initial inspection prevents whole-system completeness claims. No supplied live trace or experiment establishes deployment success, effectiveness or causal benefit; dependencies outside this repository are not independently pinned. |
