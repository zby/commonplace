---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Exocomp's shipped multi-agent runtime, retained project state and operator clients at commit b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251."
run-id: AAS-2026-10-14-exocomp-692bb27c35f9-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/cookiengineer/exocomp
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/exocomp-692bb27c35f9/related-systems/cookiengineer--exocomp
  revision: b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251
  sha256: null
---

# Exocomp boundary

## Boundary and evidence

This run examines Exocomp as a self-hosted multi-agent environment for software development and related security work. Its intended use includes a human-facing planner, role-specific contractor agents, tool-mediated project work, and retained session and project records. The target is in scope as an **enclosing runtime**: it issues model requests, dispatches returned tool calls, starts contractor processes, and supplies its own operator interfaces. It is not merely a library consumed by an excluded application. SRC-1: `README.md`, `source/cmds/exocomp/main.go`, `source/engine/Session.go`, `source/tools/Agents.go`.

The **whole-system** boundary includes the shipped Go command variants, embedded role prompts, session engine, provider configuration and adapters, tools, filesystem-backed records, recovery/debug driver, terminal/JSONL/web/webview interfaces, authored browser application, packaging scripts, and test/evaluation sources. These paths are available in the frozen repository. Initial inspection traced the main entry points through session setup, model requests, tool execution, persistence, restoration and operator consumption; it is not an exhaustive implementation audit of every helper or tool method.

The decisive runtime path assembles requests from agent messages and tool schemas, then handles assistant tool calls and requests another completion. SRC-1: `source/engine/Session.go`.

> resolved_url := session.Config.ResolveURL(session.Agent.Model, "/chat/completions")
> resolved_model := session.Config.ResolveModel(session.Agent.Model)
> resolved_token := session.Config.ResolveToken(session.Agent.Model)
> --- `source/engine/Session.go`

> session.CallTool(tool_id, tool_name, tool_method, tool_arguments)
> --- `source/engine/Session.go`

Contractor execution belongs inside the target: the agents tool launches an agent-mode executable, defaulting to its own executable unless `EXOCOMP_AGENT` overrides it. The child receives role, prompt and sandbox parameters. SRC-1: `source/tools/Agents.go`, `source/cmds/exocomp-agent/main.go`, `source/ui/jsonl/Client.go`.

> exe, _ := os.Executable()
>
> if os.Getenv("EXOCOMP_AGENT") != "" {
>     exe = os.Getenv("EXOCOMP_AGENT")
> }
> --- `source/tools/Agents.go:512-516`

Retained state is also part of the boundary, not just the inference loop. Recovery serializes sessions and agents; terminal and web setup reload those records. The `agimus` command restores an existing project session into a debug sandbox. Project tools read and write requirements, bugs and changelog records, and skills admit project-local instructions. The browser application sends chat/tool requests and reloads agent state through the shipped web API. SRC-1: `source/engine/Recovery.go`, `source/ui/tty/Client.go`, `source/ui/web/Server.go`, `source/cmds/agimus/main.go`, `source/utils/engine/RestoreSession.go`, `source/tools/readRequirements.go`, `source/tools/writeRequirements.go`, `source/tools/readSkills.go`, `app/engine/Session.go`.

> path := filepath.Join(recovery.Playground, ".exocomp", "session.json")
> err2 := os.MkdirAll(filepath.Dir(path), 0755)
> --- `source/engine/Recovery.go`

Shipped prompts are operational evidence of declared role responsibilities, not proof that models follow them. They are included because they guide the same runtime that executes tools and consumes retained records. SRC-1: `source/agents/planner.yaml`, `source/agents/NewAgent.go`, `source/agents/Roles.go`.

> - Track completed tasks of other agents via "agents.Await"
> - Track created bug reports via "bugs.List"
> - Track created specifications via "requirements.List"
> - Track changes via "changelog.List"
> --- `source/agents/planner.yaml`

### Top-level coverage

Every top-level tracked file or directory is classified below. “Included” establishes functional scope, not that every file was read. Material paths identified by the tree and scoped searches remain available for later inspection under SRC-1. No unavailable material runtime source path was discovered.

| Top-level path | Classification | Role and initial inspection | Exclusion or inspection limit; conclusion prevented |
|---|---|---|---|
| `.gitignore` | Included | Read build, vendor and generated web-asset exclusions. | Ignore rules do not establish that ignored outputs have been built or deployed. |
| `README.md` | Included | Read intended use, role/tool listings, command variants, configuration and provider requirements. | Documentation claims remain declared intent unless checked against implementation or run evidence. |
| `TODO.md` | Included | Read outstanding runtime, tool, role and UI work as author-reported development status. | Does not establish that every reported defect remains present or that proposed features ship. |
| `app/` | Included | Read `main.go`, `build.sh`, and the request/polling portion of `engine/Session.go`; searched `controllers/Chat.go`, `controllers/Bugs.go`, `controllers/Changelog.go`, `controllers/Requirements.go` for state consumption and actions. Includes `components/`, `views/`, `types/`, `schemas/`, `utils/` and `public/` supporting the authored browser client. | Rendering/helper details not yet inspected. Generated WASM and the external Gooey implementation are not present as frozen target evidence; successful frontend build or deployment is not established. |
| `build/` | Excluded: placeholder | Tracked tree contains only `build/.gitkeep`; build producers are included under `toolchain/`. | No packaged executable is available here to establish released-binary behavior. |
| `docs/` | Included, except decorative image | Read `TESTING.md`; searched `ARCHITECTURE.md` for runtime and tool paths. Includes `API.md`, `USAGE.md`, `SERVERS.md`, `TOOL_CALLS.md`, `TESTING_GUIDE.md` and `docker/` setup sources. These other documents and Docker details are not yet inspected. `exocomp.png` is deliberately excluded as decoration. | Unread documentation is not an access gap and supplies no initial findings. Image exclusion prevents no operational conclusion. Container deployment is not established. |
| `installer/` | Included | Read `cmds/exocomp-installer/main.go` and `actions/InstallExocomp.go`; searched installation actions. Includes `assets/FS.go`, asset placeholders and Go module metadata. | Program installation and platform packaging details need further inspection; placeholder assets are not built distribution evidence. |
| `quickstart-exocomp.sh` | Included | Read the driver that clears the prior source-local session and starts the web-mode planner. | This shipped state-maintenance action is not excluded as an external caller. No execution performed. |
| `quickstart-ollama.sh` | Included | Read model checks, context-size selection and launch of the external inference service. | Does not supply the implementation or measured operation of Ollama or its models. |
| `sessions/` | Included | Searched `questions_incomplete_test/.exocomp/session.json` and `debug/request.json`, `debug/response.json` for stored messages, tool calls and error records; includes the example project's `go.mod`. | Retained artifacts are inspectable but their executing code revision and full provenance are not independently established. They cannot prove current-revision success rates or general reliability. |
| `source/` | Included | Read all four `cmds/*/main.go` entry points; inspected `actions/Webview.go`; searched other `actions/`. Read the model/response path in `engine/Session.go`, persistence/restore paths in `engine/Recovery.go`, agent creation and `agents/planner.yaml`; searched embedded-role loading in `agents/Roles.go`. Read contractor spawning in `tools/Agents.go`, skill discovery in `tools/readSkills.go`, requirement persistence in `tools/readRequirements.go` and `tools/writeRequirements.go`; searched bugs/changelog persistence and tool consumers. Inspected JSONL setup and web recovery; searched terminal recovery, API routing and webview integration. Includes `providers/`, `adapters/`, `types/`, `schemas/`, `parsers/`, `utils/`, all tool schemas and remaining role YAMLs. Read a deterministic agent-lifecycle test and searched live-test gates and session-test cases. | Remaining method, role, parser and helper details are not yet inspected, not unavailable or excluded. Test code is not a test result. Bundled webview headers are available but not an independent audit of native platform behavior. |
| `toolchain/` | Included | Read `test.go` and `actions/BuildExocomps.go`; searched `build.go`, `install.go`, clone/build/install actions and external program identities. Includes `types/` and `utils/` for build/server helpers. | Build and installation success and the unfinished test driver's effectiveness are not established by execution. External repositories named by clone recipes are not frozen by this source pin. |
| `vendor/` | Excluded: placeholder | Tracked tree contains only `vendor/.gitkeep`; clone/build recipes are included under `toolchain/`. | No vendored program implementation is available to support conclusions about those programs' internal behavior. |

### Frozen revision and limits

The evidence boundary is repository `https://github.com/cookiengineer/exocomp` at full commit `b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251`, with applicability cutoff **2026-10-14**. The acquired checkout's HEAD matches this pin and its working tree was clean when checked. The source object is preserved unchanged. No later commits, moving web pages or linked external repositories are included.

The overall evidence tier is **code-grounded**. Source inspection supports implemented control and state paths; role prompts and documentation supply doctrine/design. The stored session/debug artifacts may support narrowly scoped observed-run findings once examined in detail, but do not connect their historical execution to this commit. No target commands, examples, tests, providers or services were executed in this run. No causal experiment or measured efficacy evidence has been established.

External dependencies include OpenAI-compatible inference services and model behavior; operator project files, installed programs and project-local skills; Go and host operating-system/process facilities; and Gooey/native browser facilities for the UI. Exocomp's integration code is included, while these dependencies' implementations and arbitrary consuming projects are excluded. This prevents attribution of model quality, external tool correctness, operating-system isolation or external GUI behavior to Exocomp itself. The authored UI path is available, but generated web assets are absent from the tracked tree and `app/go.mod` replaces Gooey with a sibling checkout. That gap prevents claims that this frozen checkout alone is a complete runnable browser distribution; it does not remove the shipped UI caller from the functional boundary. SRC-1: `README.md`, `source/engine/Session.go`, `source/tools/readSkills.go`, `app/go.mod`, `app/build.sh`, `.gitignore`, `source/ui/web/Server.go`.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/cookiengineer/exocomp` | b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251 | implementation; doctrine/design; observed run (retained artifacts only) | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/exocomp-692bb27c35f9/related-systems/cookiengineer--exocomp`. Implementation: command entry points, session inference/response path, recovery, contractor spawning, skill discovery, requirement read/write, UI setup and browser API consumption, build/install/test drivers and lifecycle test source; additional scoped searches listed in coverage table. Doctrine/design: `README.md`, `TODO.md`, `docs/TESTING.md`, scoped `docs/ARCHITECTURE.md` search, `source/agents/planner.yaml`. Observed run: scoped inspection of stored `sessions/questions_incomplete_test/.exocomp/` JSON artifacts, not execution in this analysis. | Implementation: [session engine](https://github.com/cookiengineer/exocomp/blob/b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251/source/engine/Session.go), [recovery](https://github.com/cookiengineer/exocomp/blob/b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251/source/engine/Recovery.go), [contractors](https://github.com/cookiengineer/exocomp/blob/b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251/source/tools/Agents.go), [browser client](https://github.com/cookiengineer/exocomp/blob/b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251/app/engine/Session.go). Doctrine/design: [README](https://github.com/cookiengineer/exocomp/blob/b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251/README.md), [planner prompt](https://github.com/cookiengineer/exocomp/blob/b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251/source/agents/planner.yaml), [testing contract](https://github.com/cookiengineer/exocomp/blob/b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251/docs/TESTING.md). Observed run: [stored session](https://github.com/cookiengineer/exocomp/blob/b36f7ba1f3e2eee25bbcd2711db7d2d5d4824251/sessions/questions_incomplete_test/.exocomp/session.json). | No discovered missing material target source. Generated binaries/web assets and sibling Gooey dependency are not frozen here, preventing distribution/build-success conclusions. External providers, models and tools are excluded implementations. Tests were not run; stored artifacts lack independently verified execution-revision provenance. No efficacy, comprehensive runtime reliability or causal attribution follows from this boundary. |
