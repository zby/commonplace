---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Exo's shipped runtime, harness integrations and persistent-agent experiment at commit 423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e."
run-id: AAS-2026-10-15-exo-f0905e2cf44b-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/exoharness/exo
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-exo/related-systems/exoharness--exo
  revision: "423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e"
  sha256: null
---

# Exo boundary

## Boundary and evidence

This run analyses Exo as shipped in the registered repository, not just its Rust library API or its older personal-agent harness. The intended use is to explain how Exo hosts model-driven agents, retains their state and reconnects clients and background work to that state. The target is in scope as an **enclosing runtime**: it admits agent definitions and turns, supplies durable infrastructure, and invokes interchangeable harnesses. The harnesses own model/context semantics. This classification does not mean Exo implements the internals of every hosted coding agent. SRC-1: `crates/cli/src/main.rs`, `crates/cli/src/managed_agents.rs`, `crates/executor/src/native/managed_executor.rs`, `website/docs-src/architecture/harnesses.md`.

The source-native architectural distinction is explicit:

> The harness decides how to call the
> model, build context, compact history, plan, and use tools. The runtime
> provides durable state, sandboxes, credentials, and network controls.
> --- `website/docs-src/architecture/harnesses.md`

The boundary kind is **whole-system**. It includes the native CLI and HTTP service; agent-definition parsing and resource preparation; turn admission, execution and recovery interfaces; stored events and versioned artifacts; credentials, egress, MCP and sandbox implementations; TypeScript harnesses and native-agent bridges; the Cloudflare host; shipped clients and examples; and the persistent-agent experiment under `exo/`. The last is a shipped caller with additional state and maintenance responsibilities, not an excluded application. Tests and evaluators are included as descriptions of checks, not as evidence that those checks passed.

Initial tracing establishes both infrastructure and consumption paths. `exo run` opens or resumes a managed thread and dispatches to a prompt, TUI or REPL; `--serve` enters the service path. Managed execution delegates turns and resumption to the resolved executor. The Basic implementation reloads events from storage and writes artifact metadata and byte versions. The Responses loop materializes prompt messages, calls a model runtime, appends model events, executes tools and appends results. SRC-1: `crates/cli/src/main.rs`, `crates/cli/src/managed_agents.rs`, `crates/executor/src/native/managed_executor.rs`, `crates/exoharness/src/basic.rs`, `exoharness/typescript/model-runtime/turn-loop.ts`.

The model loop consumes the retained conversation, rather than treating storage as an unused export:

> const messages = await materializePromptMessages(
>       conversation,
>       options.instructions
>         ? await options.instructions(context)
>         : basicHarnessInstructions(context),
>     );
> --- `exoharness/typescript/model-runtime/turn-loop.ts`

The persistent-agent harness registers tools through profiles, reads identity and local instructions, and adds memory, todos and skills to its instructions. Memory tools write an agent artifact and reload its latest version for prompt injection. Scheduling and adapters feed later inputs back through conversation wakeups; the guardian builds binaries and requests service/REPL restarts. These paths remain inside the boundary even though the current root README presents `exo/` as an earlier experiment. SRC-1: `exo/harness.ts`, `exo/profiles/practical.ts`, `exo/profiles/bootstrap.ts`, `exo/tools/memory-tools.ts`, `exo/scheduler-runner/src/main.rs`, `crates/executor/src/native/scheduler_runtime.rs`, `crates/executor/src/native/adapter/runtime.rs`, `crates/executor/src/native/conversation_wakeup.rs`, `exo/scripts/exo-service-guardian`, `exo.sh`, `README.md`.

> const memory = await memoryInstruction(context);
>   if (memory !== null) {
>     instructions.push(memory);
>   }
> --- `exo/harness.ts`

### Repository coverage

Every top-level tracked entry is classified below. “Included” means within the functional evidence boundary, not that every file or implementation branch has already been read. Material entry and state paths have been inspected as identified above; additional available files remain eligible for later jobs at this same pin. Tree inspection and scoped searches supply the path inventory (SRC-1). No available but unread file is classified as inaccessible.

| Top-level tracked entry | Treatment and material paths or role | Inspection status and limits |
|---|---|---|
| `crates/` | Included: `cli/src/main.rs`, `managed_agents.rs`, service/TUI callers; `managed-agents/src/` definitions; `executor/src/native/` execution, scheduler and adapter runtimes; `exoharness/src/` storage, events, artifacts, queues, sandbox, vault and egress substrate; `worker-runtime/src/` hosted execution; `mcp/src/`, `cost/src/`, `firecracker-protocol/src/`, `firecracker-guest/src/` support. | CLI dispatch, managed executor, Basic event reads/artifact writes, stored queue interface, wakeups, scheduler and adapter delivery inspected; remaining backends and policy branches not exhaustively inspected. No parity or security guarantee follows from this coverage. |
| `exoharness/` | Included: `typescript/harness/` runtime contract and tool surfaces; `typescript/model-runtime/turn-loop.ts`; `typescript/codex/`, `typescript/cursor/`; `examples/typescript/` bundled and example harnesses; managed-agent examples; containers; `cloudflare/src/` host/provider/thread/sandbox code and its tests. | Responses loop, Pi launch/history bridge, Codex wrapper and Cloudflare request routing inspected; Claude bridge searched; SDK internals and individual backend behavior not established by those reads. |
| `exo/` | Included: `harness.ts`, `prompts/me.md`, `profiles/`, `tools/`, `adapters/` workers and setup prompts, `scheduler-runner/`, guardian and other `scripts/`, `SELF.md` and `docs/` maintenance instructions. | Harness, profiles, memory read/write/injection, scheduler entry point and guardian build path inspected. Other tool implementations, protocol workers and prompt bodies remain available, not access gaps. |
| `exo.sh` | Included: launcher, profile setup, state creation/reuse, environment persistence, setup-prompt submission and runner supervision. | Read completely; actual deployment success not observed. |
| `eval/` | Included: `harbor/src/exo_harbor/agent.py`, CLI client, trajectory export, plugin, tests and task datasets. This is a shipped evaluator/consumer, not external application code. | Driver read: creates per-trial conversation, attaches Harbor-owned container, sends task and exports trajectory even after failure. No benchmark result or measured improvement established. |
| `examples/` | Included: `tutorial/1_ticket_triage/agent.md` agent-definition example. | Inventoried; example content not yet inspected and no task outcome inferred. |
| `website/` | Included: `src/chat.jsx`, reconnecting WebSocket client, UI components, `src/worker.js`, deployment configuration; `docs-src/` current and archived docs, architecture, tutorials and build-time event documentation. | Static asset worker read, chat client searched, current harness/data-model docs read. UI and all reconnect branches not exhaustively inspected; no deployed-service behavior inferred. |
| `docs/` | Included: providers, resources, egress, `RSI.md`, `SELF-CONTROL.md` and diagrams as source-authored design material. | Inventoried, not yet read; declarations must not be substituted for implementation. Image assets do not establish execution. |
| `support/` | Included: CI sandbox setup and Firecracker build, administrative and egress smoke scripts. | Inventoried; host-specific provisioning and smoke-test outcomes not observed. |
| `fuzz/` | Included: Firecracker protocol fuzz target, corpus and manifests. | Inventoried; no fuzzing results claimed. |
| `scripts/` | Included: website development, hook setup and precommit helpers. | Inventoried through tree and package-script consumers; not yet inspected in detail. |
| `.github/` | Included: CI and sandbox-image publication workflows. | CI validation/test configuration initially inspected; no workflow execution evidence. |
| `.githooks/` | Included: pre-commit and pre-push checks. | Inventoried; enforcement and successful checks not established. |
| `README.md` | Included: current positioning, quickstart, architecture and identification of the earlier experiment. | Read; third-party comparisons are source claims, not independent evidence. |
| `AGENTS.md` | Included as target-authored development instructions, not instructions binding this analysis. | Inventoried; not yet read. |
| `Cargo.toml`, `Cargo.lock` | Included: Rust workspace membership and dependency pins. | Manifest read; external dependency implementations are not captured by their lock entries. |
| `package.json`, `pnpm-lock.yaml`, `pnpm-workspace.yaml` | Included: JS dependencies, scripts and workspace wiring. | Package manifest read; lock/workspace files inventoried. No installed dependency behavior inferred. |
| `Makefile`, `setup.sh`, `mise.toml` | Included: build/setup entry points and toolchain configuration. | Inventoried; installation not attempted. |
| `tsconfig.json`, `vitest.config.ts`, `clippy.toml`, `.oxfmtrc.json`, `.oxlintrc.json` | Included: resolution, tests, lint and formatting configuration. | Inventoried; not evidence that configuration checks pass. |
| `.env.example`, `.gitignore` | Included: configuration template and local-state tracking boundaries. | Inventoried; actual local credentials or deployment state are not frozen evidence. |
| `LICENSE` | Excluded from behavioral analysis: legal terms only. | Prevents legal/licensing conclusions; does not remove a runtime path. |

### Frozen revision and limits

The sole source is Git commit `423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e`, with applicability cutoff **2026-10-15**. The acquired checkout's HEAD matches the supplied revision and its working tree was clean on inspection. No other revision, website response, dependency checkout or execution capture is admitted. The evidence tier is **code-grounded**, supplemented by source-authored doctrine/design. This is static source inspection; the target, tests, examples and evaluators were not executed.

External dependencies include model providers; the actual Codex, Claude Code, Pi and Cursor runtimes/SDKs; Lingua and other libraries; container/VM engines and cloud sandbox providers; Cloudflare services; Harbor; and messaging services used by adapters. Their checked-in integration code is included, but external implementations, remote deployments, user data and service-side state are not. This prevents conclusions about provider model quality, native-agent internal context algorithms, deployed availability, end-to-end isolation or empirical performance. The Pi bridge explicitly starts a sandbox process; it is not evidence that Pi's own loop is implemented in this repository. SRC-1: `package.json`, `Cargo.toml`, `exoharness/examples/typescript/pi-harness.ts`, `exoharness/cloudflare/src/index.ts`, `eval/harbor/src/exo_harbor/agent.py`, `exo/README.md`.

There is no known source-access gap within the frozen checkout. Uninspected files listed above are remaining analytical work, not missing evidence. No supplied observed run or causal experiment supports claims of successful recovery, useful self-improvement or retained-memory effectiveness.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/exoharness/exo` | 423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-exo/related-systems/exoharness--exo`. Implementation: CLI dispatch and managed-thread opening; managed executor delegation; Basic event retrieval, artifact persistence and stored queue interface; Responses loop; Pi launch/history bridge; Exo harness/profile/memory paths; launcher, guardian build path, scheduler and adapter wakeups; Harbor driver; Cloudflare routing and website asset worker. Doctrine/design: root and Exo READMEs, Cargo/JS manifests, current harness and data-model docs; initial CI configuration. Tracked tree and scoped searches cover the repository inventory, not exhaustive behavior. | Implementation: [CLI dispatch](https://github.com/exoharness/exo/blob/423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e/crates/cli/src/main.rs), [Basic storage consumer](https://github.com/exoharness/exo/blob/423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e/crates/exoharness/src/basic.rs), [model loop](https://github.com/exoharness/exo/blob/423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e/exoharness/typescript/model-runtime/turn-loop.ts), [persistent-agent harness](https://github.com/exoharness/exo/blob/423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e/exo/harness.ts), [Harbor driver](https://github.com/exoharness/exo/blob/423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e/eval/harbor/src/exo_harbor/agent.py). Doctrine/design: [harness architecture](https://github.com/exoharness/exo/blob/423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e/website/docs-src/architecture/harnesses.md), [data model](https://github.com/exoharness/exo/blob/423d7d0f4394a1ddc9955d13c73c9f8a9c4d4e7e/website/docs-src/architecture/data-model.md). Other initially inspected paths appear in the coverage account above. | No known checkout access gap. External dependency internals and deployed service state are outside this source. No observed-run or experimental layer: execution success, security guarantees, recovery reliability and causal improvement remain unestablished. |
