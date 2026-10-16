---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Prime Agent's shipped Rust runtime, Python kernel, continual harness and bundled skills at commit 33da15a2c15c4e903c372f69ae8e1156d77d53da."
run-id: AAS-2026-10-14-prime-agent-8ec59ae12476-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "33da15a2c15c4e903c372f69ae8e1156d77d53da"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/PrimeIntellect-ai/prime-agent
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/prime-agent-8ec59ae12476/related-systems/PrimeIntellect-ai--prime-agent
  revision: "33da15a2c15c4e903c372f69ae8e1156d77d53da"
  sha256: null
---

# Prime Agent boundary

## Boundary and evidence

This run analyses Prime Agent as the shipped coding and research agent, not just its Python harness-state API. Intended use is to explain how its runtime conducts model-driven work, retains operating state, refines that state and makes it available to later work. The target is in scope as an **enclosing runtime**: the repository ships the model/tool loop and the callers that construct, persist, reload and serve sessions. Its continual harness is a subsystem of that runtime, not the entire target. The boundary kind is **whole-system**, covering the shipped Rust application, Python kernel package, bundled instructions and skills, and their shipped consumers and evaluation seams. [SRC-1: `README.md`, `crates/pa-cli/src/main.rs`, `crates/pa-cli/src/print_runtime.rs`, `crates/pa-agent/src/agent_loop/run.rs`]

The entry-point trace starts at `crates/pa-cli/src/main.rs`, which invokes `pa_cli::main_with_runtime` with `PrintRuntime`. That runtime dispatches interactive, print/JSON, daemon, ACP and RPC modes. ACP creates a daemon session; interactive code connects to the daemon; print mode has its own engine and inline child-agent host. These are included product paths, not excluded applications that happen to consume a library. The separate daemon binary also dispatches supervisor and worker entry points. Worker creation opens or creates session files and seeds the hosted engine. The hosted engine constructs the shared core session with the provider stream, Python kernel and daemon child host. [SRC-1: `crates/pa-cli/src/main.rs`, `crates/pa-cli/src/lib.rs`, `crates/pa-cli/src/print_runtime.rs`, `crates/pa-cli/src/print_rlm.rs`, `crates/pa-cli/src/interactive_mode/daemon.rs`, `crates/pa-tui/src/interactive/run.rs`, `crates/pa-daemon/src/main.rs`, `crates/pa-daemon/src/worker/create.rs`, `crates/pa-daemon/src/agent_engine/lifecycle.rs`]

> let code = pa_cli::main_with_runtime(&args, &pa_cli::PrintRuntime);
> --- `crates/pa-cli/src/main.rs`

The agent loop issues assistant requests, executes returned tool calls, admits their results into context and checks turn-boundary hooks. This establishes runtime ownership of the model-dependent loop, rather than a returning computation that supplies a value to an unrelated host. [SRC-1: `crates/pa-agent/src/agent_loop/run.rs`]

> let message =
>     stream_assistant_response(current_context, config, signal, emit, stream_fn).await?;
> new_messages.push(AgentMessage::from(message.clone()));
> --- `crates/pa-agent/src/agent_loop/run.rs`

Functional inclusions cover session admission and queues; provider/model selection and streaming adapters; tool execution and kernel lifecycle; recursion, agent messaging and factory workflows; local/global harness state, refinement planning and application, rollback records and digest delivery; skills and prompt assembly; compaction and session reload; goals, autonomous gates, schedules and heartbeats; session storage, archive, recovery and reattachment; configuration, resource packages, export, telemetry and trace delivery; and shipped installation/update seams. Initial inspection traced the principal runtime and retained-state loop. It is not an exhaustive audit of every included file or proof that all advertised modes behave identically. [SRC-1: `crates/pa-core/README.md`, `crates/pa-daemon/README.md`, `crates/pa-cli/src/print_runtime.rs`, `prime-agent-runtime/src/rlm/factory.py`, `skills/factory/SKILL.md`]

The retained-state loop includes both writer sides and later consumption. Python harness helpers serialize entries and refinement events; Rust refinement applies a plan inside a locked state update, then records outcomes. Digest rendering reloads global and local stores and merges them for model-facing context. Worker session storage and engine adoption are included because they own persistence and restore responsibility outside that API. Bundled refinement instructions are evidence of the agent-facing contract, not proof of successful learning. [SRC-1: `prime-agent-runtime/src/rlm/harness.py`, `crates/pa-core/src/refinement/mod.rs`, `crates/pa-core/src/session_engine/refine.rs`, `crates/pa-core/src/session_engine/harness_digest.rs`, `crates/pa-daemon/src/session_store/write.rs`, `crates/pa-daemon/src/agent_engine/lifecycle.rs`, `skills/refine/SKILL.md`]

> let global = load_harness_state(&context.global_dir, HarnessScope::Global);
> let local = context
>     .local_dir
>     .as_ref()
>     .map(|dir| load_harness_state(dir, HarnessScope::Local));
> let merged = merge_harness_states(&global, local.as_ref());
> --- `crates/pa-core/src/session_engine/harness_digest.rs`

The frozen evidence is SRC-1 at full commit `33da15a2c15c4e903c372f69ae8e1156d77d53da`; the read-only checkout's HEAD was checked against the supplied pin. The applicability cutoff is the supplied run date, **2026-10-14**, not a claim about later releases. Overall evidence is **code-grounded**, with documentation used as declared intent. No target code, tests, examples or model services were executed. Test source supports the existence and design of checks, not their passage or measured results.

External dependencies include model-provider APIs and credentials, remote model/MCP catalogs, third-party MCP servers and integrations, package sources, release endpoints, analytics/trace receivers, and the host operating system and Python/IPython environment. Their shipped adapters and configuration are included; their external implementations, live content and service behavior are not frozen here. This prevents conclusions about provider internals, current catalog contents, remote service reliability, end-to-end cloud execution or delivery guarantees. User projects, user-created skills and actual session histories are also outside the evidence set; their absence prevents claims about practical task success or improvement across real sessions. The linked RLM/continual-harness papers, Verifiers and PRIME-RL repositories are not acquired sources; the README's links cannot establish their algorithms or results. [SRC-1: `README.md`, `crates/pa-ai/README.md`, `crates/pa-models/README.md`, `crates/pa-core/README.md`, `crates/pa-telemetry/README.md`, `scripts/release/README.md`]

Historical TypeScript references in code and documentation are attributed migration context, not an independently inspected historical implementation. The boundary covers this commit's shipped Rust/Python product; it cannot establish behavior of an older release from parity comments alone. No source-access failure was encountered. Files not yet read in depth remain available under SRC-1 and are not access gaps.

### Top-level coverage

Every top-level tracked entry is classified below. “Included” defines functional scope, not exhaustive initial reading. Material implementation paths named within included directories remain available to later jobs at the same commit. Deliberately excluded repository administration does not remove any shipped session or harness responsibility.

| Top-level tracked entry | Classification and role | Initial inspection and limits / conclusion prevented |
|---|---|---|
| `.cargo/` | Included build configuration: `config.toml`. | Tree inspected; configuration not yet read in depth. No build-performance or compilation-success conclusion. |
| `.changes/` | Excluded release-note fragments. | Tree inspected, fragments not read. No reconstruction of release history from these notes. Current implementation remains included. |
| `.cursor/` | Excluded contributor review configuration: `BUGBOT.md`. | Not read; no claim about contributor review-agent behavior. |
| `.github/` | Included shipped build/release/evaluation support: `workflows/ci.yml`, `release.yml`, `nightly.yml`, `continuous.yml`, `windows-runtime-triage.yml`, dependency audit action and helper scripts; contributor/social automation excluded. | Tree inspected and release-publication contract read through `scripts/release/README.md`; workflow internals not yet inspected. No assertion that CI or publication passed. Excluded social/review workflows cannot support runtime claims. |
| `.gitignore` | Excluded repository ignore policy. | No claim about completeness of ignored developer artifacts. |
| `AGENTS.md` | Excluded repository contributor instructions, not runtime prompt layers. | Not read as operational authority or agent product behavior; runtime prompts are included under `crates/` and `skills/`. No characterization of repository-development workflow. |
| `CONTRIBUTING.md` | Excluded contribution process. | Not read; no contribution-governance assessment. |
| `Cargo.lock` | Included dependency pin manifest. | Tree inspected, dependency graph not audited. No dependency-security conclusion. |
| `Cargo.toml` | Included workspace membership, dependency and release-profile configuration. | Read; establishes the nine shipped crates and vendored crossterm patch. No successful-build claim. |
| `LICENSE` | Excluded legal text. | No independent license-compliance assessment. |
| `Makefile` | Included build/test support, not a separate external application. | Not yet inspected beyond tree inventory; no make-target or benchmark-result claim. |
| `README.md` | Included product doctrine/design, commands and risk disclosure. | Read completely; links to external works remain unfrozen and excluded as evidence. |
| `crates/` | Included Rust runtime and callers: `pa-cli/src/{main.rs,lib.rs,print_runtime.rs,print_rlm.rs,interactive_mode/,update_flow/}`; `pa-daemon/src/{main.rs,worker/,supervisor/,agent_engine/,session_store/,rlm_children/,scheduled_jobs.rs,acp/,rpc/}`; `pa-agent/src/agent_loop/`; `pa-core/src/{session_engine/,session/,kernel/,refinement/,prompts/,skills/,tools/,cron/,autonomous/,settings/,packages/,mcp/,models/,agent_traces/,export_html/,workspace_snapshot/,update/}`; `pa-ai/src/providers/`; `pa-models/`; `pa-tui/src/{interactive/,daemon_client.rs,session_ui/,factory_view/}`; `pa-types/`; `pa-telemetry/`; associated assets, tests and examples. | Inspected entry points, dispatch, loop, runtime wiring, worker creation/engine construction and restore seams, session writes, refinement writes and digest reload, prompt layer, selected crate contracts and headless evaluator source. Remaining module internals, recovery variants and tests are not yet inspected in depth, not unavailable. Tests are included as implementation/design evidence; no test run, UI performance or provider-success claim. |
| `deny.toml` | Included dependency-audit policy support. | Not yet read; no dependency audit conclusion. |
| `docs/` | Included supporting operation/migration evidence: `daily-stats.md`, `legacy-upgrade-contract.md`, `legacy-upgrade-evidence.md`, `legacy-release-inventory.json`. | Tree inspected; contents not yet read. No historic upgrade or usage-statistics claim. |
| `install-rust.sh` | Included Unix installer/product launcher. | Inventoried, not yet read; cannot yet assert installer behavior. |
| `install.ps1` | Included Windows installer. | Inventoried, not yet read; cannot yet assert Windows installation behavior. |
| `packaging/` | Included Homebrew install/update surfaces: `homebrew/Casks/prime-agent.rb`, `homebrew/Formula/prime-agent.rb`. | Tree inspected, recipes not yet read; no packaging-parity claim. |
| `prime-agent-runtime/` | Included Python kernel: `src/rlm/{__init__.py,repl.py,repl.md,harness.py,factory.py,bash.py,mcp.py,mcp_base.py,skill.py,_winjob.py,machines/}`; `pyproject.toml`, lock and `test/`. | Inspected host-request/recursion API searches, harness schema and saving, factory contract and execution ownership. Factory machines `builder`, `pr-manager`, `review-sweep` and remaining kernel internals/tests not yet read in depth. They remain included, especially as consumers of stored specifications; no execution or restart-recovery result inferred from inventory. |
| `scripts/` | Included evaluation, statistics, build and release support: `ci_test_shard*.py`, `review_*_parity.py`, `daily_stats.py`, `package_release.py`, and `release/{assemble_source.py,assemble_artifacts.py,bundle_catalog.py,native_compat.py,npm_bridge.py,native-compat/,npm_bridge_assets/,verify_*.py,test_*.py}`. | Inventory and `release/README.md` inspected; evaluation and packaging implementations not yet read. No independent parity, publication, usage or causal-improvement claim. Native compatibility export/theme/wasm assets remain part of the shipped artifact scope. |
| `skills/` | Included bundled prompts and executable packages: `agent-message`, `agent-observe`, `attach-image`, `compact`, `edit`, `factory`, `goal`, `mcp`, `prime-intellect`, `refine`, `rlm-heartbeat`, `skill-creator`, `websearch`; each shipped `SKILL.md`, Python package and reference where present. | Full `refine/SKILL.md` and `factory/SKILL.md` inspected; other skill contents not yet read in depth. Included as shipped operating instructions and tool bridges, not merely incidental documentation. No uninspected skill behavior asserted. |
| `vendor/` | Included terminal dependency: `crossterm/` parser/input/terminal implementation and `PRIME_AGENT_PATCH.md`. | Tree and workspace patch declaration inspected; vendor internals not yet read. No terminal compatibility or latency guarantee. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/PrimeIntellect-ai/prime-agent` | 33da15a2c15c4e903c372f69ae8e1156d77d53da | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/prime-agent-8ec59ae12476/related-systems/PrimeIntellect-ai--prime-agent`. Implementation: tracked tree; `Cargo.toml`; CLI entry/dispatch and mode construction (`crates/pa-cli/src/main.rs`, `lib.rs`, `print_runtime.rs`, `print_rlm.rs`, `interactive_mode/daemon.rs`); `crates/pa-agent/src/agent_loop/run.rs`; core session runtime wiring, harness digest, refinement and storage (`crates/pa-core/src/session_engine/runtime_wiring.rs`, `harness_digest.rs`, `refine.rs`, `crates/pa-core/src/refinement/mod.rs`, `executor.rs`, `crates/pa-core/src/session/manager/persist.rs`); daemon entry, worker create, engine lifecycle and store writes (`crates/pa-daemon/src/main.rs`, `worker/create.rs`, `agent_engine/lifecycle.rs`, `session_store/write.rs`); TUI interactive-route searches (`crates/pa-tui/src/interactive/run.rs`); Python host API searches, harness save and factory contract (`prime-agent-runtime/src/rlm/__init__.py`, `harness.py`, `factory.py`); headless evaluator source (`crates/pa-cli/tests/eval_composition_e2e.rs`). Doctrine/design: full `README.md`, `crates/pa-core/README.md`, `crates/pa-daemon/README.md`, `crates/pa-ai/README.md`, `crates/pa-models/README.md`, `crates/pa-telemetry/README.md`, `scripts/release/README.md`, `skills/refine/SKILL.md`, `skills/factory/SKILL.md`; selected `crates/pa-core/src/prompts/layers/core.md`. These paths describe initial inspection, not a source allowlist. | Implementation: [CLI entry](https://github.com/PrimeIntellect-ai/prime-agent/blob/33da15a2c15c4e903c372f69ae8e1156d77d53da/crates/pa-cli/src/main.rs), [model/tool loop](https://github.com/PrimeIntellect-ai/prime-agent/blob/33da15a2c15c4e903c372f69ae8e1156d77d53da/crates/pa-agent/src/agent_loop/run.rs), [retained-state consumer](https://github.com/PrimeIntellect-ai/prime-agent/blob/33da15a2c15c4e903c372f69ae8e1156d77d53da/crates/pa-core/src/session_engine/harness_digest.rs), [refinement apply](https://github.com/PrimeIntellect-ai/prime-agent/blob/33da15a2c15c4e903c372f69ae8e1156d77d53da/crates/pa-core/src/session_engine/refine.rs), [worker engine](https://github.com/PrimeIntellect-ai/prime-agent/blob/33da15a2c15c4e903c372f69ae8e1156d77d53da/crates/pa-daemon/src/agent_engine/lifecycle.rs). Doctrine/design: [product](https://github.com/PrimeIntellect-ai/prime-agent/blob/33da15a2c15c4e903c372f69ae8e1156d77d53da/README.md), [bundled refinement instruction](https://github.com/PrimeIntellect-ai/prime-agent/blob/33da15a2c15c4e903c372f69ae8e1156d77d53da/skills/refine/SKILL.md). | No checkout access gap. Inspection is selective. No observed run or causal experiment is established; source tests are not executed results. External services, catalog revisions, user workloads, linked papers and other repositories are not frozen, preventing conclusions about their internals, live availability, practical learning efficacy and cross-release parity. |
