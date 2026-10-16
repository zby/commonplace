---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Tracecraft's shipped bucket-backed agent coordination and session-retention system at commit 97c6b7447f8e696f0116357d9f86bb0ece25e5b1."
run-id: AAS-2026-10-14-tracecraft-9c4af961e8e2-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "97c6b7447f8e696f0116357d9f86bb0ece25e5b1"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  kind: git
  identity: https://github.com/arrmlet/tracecraft
  revision: "97c6b7447f8e696f0116357d9f86bb0ece25e5b1"
  path: /home/zby/llm/commonplace/.commonplace/worktrees/tracecraft-9c4af961e8e2/related-systems/arrmlet--tracecraft
  sha256: null
---

# Tracecraft boundary

## Boundary and evidence

This run analyses Tracecraft as the shipped durable coordination and session-retention system for external agents. Its intended use is to preserve coding-agent transcripts and let agents exchange shared state, messages, task ownership, handoff records and files through a user-controlled bucket. It is in scope as a memory/knowledge/context-engineering system, not as an enclosing model runtime. Its own description explicitly separates retained coordination state from ownership of the model loop (SRC-1, `README.md`):

> Tracecraft owns neither the loop nor the model — just the durable state agents coordinate *through* — so it works across hosts, across clouds, with agents that aren't even running at the same time.
> --- `README.md`

The boundary is **whole-system for the shipped Tracecraft product**, including its CLI callers, Python storage interface, session adapters, shipped agent instructions and evaluators. It is not merely the storage-wrapper API. The package exposes `tracecraft.cli:main`; that entry point registers initialization, shared memory, agents, messages, steps, artifacts, sessions and status. Tracing those registrations reaches the writers, admission checks, later readers and maintenance commands described below (SRC-1, `sdk/pyproject.toml`, `sdk/tracecraft/cli/__init__.py`).

> [project.scripts]
> tracecraft = "tracecraft.cli:main"
> --- `sdk/pyproject.toml`

### Functional coverage

- **Configuration and admission:** initialization writes local configuration, creates or checks the backend bucket and registers an agent. Configuration selects the backend and permits a per-process agent override. Storage keys are project-prefixed. Memory, recipient and step validation, conditional claim writes and completion ownership checks are inside the target, not delegated to an excluded application (SRC-1, `sdk/tracecraft/config.py`, `sdk/tracecraft/store.py`, `sdk/tracecraft/cli/init_cmd.py`, `sdk/tracecraft/cli/memory.py`, `sdk/tracecraft/cli/messages.py`, `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/protocol.py`).
- **Persisted coordination and later consumption:** memory commands write current values and version snapshots, then expose get/list/history; messages expose direct/broadcast writes and full or cursor-based reads; step commands write claims, status and structured handoffs, then expose status and dependency polling; artifacts expose upload/download/list. Agent and status views consume stored registration and aggregate coordination state. The store API is also a shipped direct read/write path (SRC-1, `sdk/tracecraft/cli/memory.py`, `sdk/tracecraft/cli/messages.py`, `sdk/tracecraft/cli/steps.py`, `sdk/tracecraft/cli/artifacts.py`, `sdk/tracecraft/cli/agents.py`, `sdk/tracecraft/cli/status.py`, `sdk/tracecraft/store.py`, `README.md`).
- **Session retention and maintenance:** the mirror driver discovers host sessions through the adapter registry, reads new bytes or SQLite rows, applies optional regex redaction, writes transcript parts and metadata, and advances local mirror state. Its one-shot, follow and follow-all paths are included. List/show later reload retained sessions; compact merges parts and deletes originals; stop clears local state and records an end marker. These are shipped drivers, not external applications (SRC-1, `sdk/tracecraft/cli/session.py`, `sdk/tracecraft/harness/__init__.py`, `sdk/tracecraft/harness/base.py`, `sdk/tracecraft/harness/claude_code.py`, `sdk/tracecraft/harness/codex.py`, `sdk/tracecraft/harness/openclaw.py`, `sdk/tracecraft/harness/hermes.py`, `sdk/tracecraft/redact.py`).
- **Agent-side usage contracts:** the Claude Code project prompt and Hermes skill prescribe checking peers and inboxes, claiming work, sharing progress and leaving handoff context. They also prescribe reads of retained memory and downloaded artifacts. These instructions belong to the product boundary even though the host decides whether to load and follow them (SRC-1, `examples/claude-code/CLAUDE.md`, `examples/hermes-agent/SKILL.md`).
- **Evaluators:** shipped SDK tests cover these CLI and adapter contracts; contention and messaging benchmark drivers call the actual storage wrappers and read durable state back. Evaluators belong to the evidence boundary, but no evaluator was executed in this run (SRC-1, `sdk/tests/test_v025_features.py`, `sdk/tests/test_session_cli.py`, `benchmarks/contention_bench.py`, `benchmarks/messaging_bench.py`).

The shipped agent instruction establishes an explicit cross-invocation usage loop, not proof that a real agent followed it (SRC-1, `examples/claude-code/CLAUDE.md`):

> 1. Check `tracecraft agents` to see who else is working
> 2. Check `tracecraft inbox` for messages before starting
> 3. Run `tracecraft claim <your-step>` before starting work
> 4. Share progress via `tracecraft memory set`
> 5. When done, run `tracecraft complete <step> --note "context for next agent"`
> 6. Check `tracecraft inbox` periodically for messages from other agents
> --- `examples/claude-code/CLAUDE.md`

### Repository coverage

Every top-level tracked item at the pin is classified below. “Included” identifies material within the analytical boundary, not a claim that every line has already been inspected. Deferred inspection is distinguished from inaccessible evidence. All rows refer to SRC-1.

| Top-level tracked item | Classification and material paths | Role and inspection status | Exclusion or limit; conclusion prevented |
|---|---|---|---|
| `.env.example` | Included | Inspected credential and harness-location examples; relates to `sdk/tracecraft/cli/init_cmd.py`, configuration and adapters. | Examples do not establish real credential or host configuration. |
| `.github/` | Included: `workflows/ci.yml`, `workflows/release.yml` | Both inspected. CI invokes SDK tests; release builds the SDK, copies root documentation and checks the installed CLI. | Workflow source is not evidence of a successful CI or published package run. |
| `.gitignore` | Included | Inspected development exclusions and credential-file ignore rules. | Ignore rules do not establish absence of leaked credentials. |
| `CLAUDE.md` | Included | Inspected repository-side architecture and contributor instructions. | Declared architecture is checked against executable paths, not accepted as implemented merely because stated. |
| `CONTRIBUTING.md` | Included | Inspected contributor procedure, parallel worktree guidance and test instructions. | Does not establish observed contributor behavior. |
| `LICENSE` | Excluded from operational mechanism | Inspected MIT license; legal metadata. | No legal interpretation or licensing-compliance conclusion. |
| `README.md` | Included | Fully inspected use cases, command reference, API example, backend limits and reported benchmark headlines. | Promotional and benchmark claims remain attributed unless grounded separately. |
| `SECURITY.md` | Included | Inspected security policy for redaction, privacy and credential handling. | Policy does not establish a security audit or runtime guarantee. |
| `benchmarks/` | Included: `contention_bench.py`, `messaging_bench.py`, `test_contention_bench.py`, `build_report.py`, `report_template.py`, `contention_report.html`, `results_*.jsonl`, `README.md` | README inspected; claim trial/preflight and messaging send/readback implementations inspected; Python symbols inventoried. Report-generation internals, raw results and generated report not yet inspected. | No access gap. Numerical results and causal attribution are not independently established by this boundary; raw records remain available for later inspection at the same pin. These evaluators test storage primitives, not model reasoning quality. |
| `docker-compose.dev.yml` | Included as development dependency setup | Inspected MinIO service definition. | Does not establish a running backend, portable latency or deployment security. |
| `docs/` | Included: `session-mirror.md`, `s3-architecture.md`; assets excluded as demonstrations | Both textual documents inspected; `assets/tracecraft-claim-race.gif` and `assets/tracecraft-messaging.gif` inventoried, not viewed. | Documentation is intent, with implementation taking precedence where commands/layout differ. Unviewed demonstration images do not support execution claims. |
| `examples/` | Included: `claude-code/CLAUDE.md`, `hermes-agent/SKILL.md` | Both fully inspected as shipped model-facing coordination instructions and read/write consumption procedures. | Host loading, compliance and downstream reasoning remain unobserved. |
| `plans/` | Excluded from shipped operational implementation: blueprints, research and `server-archive/` | Tree inventoried; `server-archive/README.md` inspected to resolve whether server scaffolding is product code. Other plans not yet inspected. SDK packaging and imports were traced independently. | No conclusion about fulfillment of proposals, historical pivots or a managed-server implementation. Plans can supply attributed design evidence if later inspected, not substitute for shipped behavior. |
| `sdk/` | Included: `pyproject.toml`, `README.md`, all `tracecraft/` modules and `tests/` | Package metadata and every production module inspected, including all CLI drivers, storage backends, protocol, config, redaction and four adapters. Test symbols inventoried; memory/message and session write/read tests sampled as source. Remaining test bodies not yet inspected. | No inaccessible production path. No test execution or exhaustive test-adequacy conclusion. Test source specifies checks, not observed passing results. |

The archived server is deliberately excluded from the shipped mechanism, rather than counted as an uninspected enclosing runtime. Packaging selects `tracecraft*` under `sdk/`; the traced CLI imports reach the bucket-backed SDK. The archive supplies a matching explicit status statement (SRC-1, `sdk/pyproject.toml`, `sdk/tracecraft/cli/__init__.py`, `plans/server-archive/README.md`):

> Not imported by the shipped SDK at any point;
> moved here so reviewers don't mistake it for the product.
> --- `plans/server-archive/README.md`

### Dependencies, exclusions and evidence limits

External dependencies are Python, Click, boto3/botocore and an S3-compatible endpoint, or the optional HuggingFace Hub client and bucket service; the Hermes adapter additionally uses Python's SQLite reader. Backend implementation, authentication policy, service durability and conditional-write semantics are outside the registered repository. The target's wrapper calls and fallback behavior are inspectable, but this boundary cannot establish guarantees for every advertised backend or deployed service (SRC-1, `sdk/pyproject.toml`, `sdk/tracecraft/s3.py`, `sdk/tracecraft/hf.py`, `sdk/tracecraft/harness/hermes.py`).

Claude Code, Codex, OpenClaw and Hermes are external model hosts. Their transcript production, pruning, tool selection, prompt assembly and use of returned content are excluded. Tracecraft's adapters and shipped usage instructions are included. This distinction prevents attributing host reasoning, automatic context injection, or actual agent uptake to Tracecraft merely because it preserves and displays host outputs. No external-host source or real agent-session trace has been supplied (SRC-1, `sdk/tracecraft/harness/base.py`, the four adapter paths above, `examples/claude-code/CLAUDE.md`, `examples/hermes-agent/SKILL.md`).

There is no identified inaccessible shipped production path. Available files deferred in the coverage table are not access gaps. The evidence tier is **code-grounded**: implementation and source-native doctrine are inspectable, while README benchmark results are reported operation until their frozen records and conditions are assessed. No target code, tests, examples or provider calls were executed. The complete disposition means the boundary and source register were established, not that system correctness or performance was experimentally verified.

The frozen source is the acquired Git object at **97c6b7447f8e696f0116357d9f86bb0ece25e5b1**. The checkout's HEAD matches that pin and its working tree was clean when inspected. The applicability cutoff is **2026-10-14**, the opening run date; this is not a claim about the commit's author date or the live repository at that date. Later commits, issue pages, package releases and external documents are outside this evidence boundary. The source register covers the entire repository at the pin: initial inspection paths are not an allowlist for later jobs.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/arrmlet/tracecraft` | 97c6b7447f8e696f0116357d9f86bb0ece25e5b1 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/tracecraft-9c4af961e8e2/related-systems/arrmlet--tracecraft`. Implementation: tracked tree, `sdk/pyproject.toml`, all `sdk/tracecraft/` modules, CI/release workflows, MinIO setup, selected memory/message and session test bodies, benchmark preflight/trial and messaging readback paths. Doctrine/design: `README.md`, `sdk/README.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `SECURITY.md`, `.env.example`, `.gitignore`, `docs/session-mirror.md`, `docs/s3-architecture.md`, both shipped example instructions, archive status README. Reported operation: README and benchmark README claims only; raw benchmark records and report not yet inspected. | Implementation: [package/CLI entry point](https://github.com/arrmlet/tracecraft/blob/97c6b7447f8e696f0116357d9f86bb0ece25e5b1/sdk/pyproject.toml), [session driver](https://github.com/arrmlet/tracecraft/blob/97c6b7447f8e696f0116357d9f86bb0ece25e5b1/sdk/tracecraft/cli/session.py), [bucket protocol](https://github.com/arrmlet/tracecraft/blob/97c6b7447f8e696f0116357d9f86bb0ece25e5b1/sdk/tracecraft/protocol.py), [contention evaluator](https://github.com/arrmlet/tracecraft/blob/97c6b7447f8e696f0116357d9f86bb0ece25e5b1/benchmarks/contention_bench.py). Doctrine/design: [agent usage prompt](https://github.com/arrmlet/tracecraft/blob/97c6b7447f8e696f0116357d9f86bb0ece25e5b1/examples/claude-code/CLAUDE.md), [session contract](https://github.com/arrmlet/tracecraft/blob/97c6b7447f8e696f0116357d9f86bb0ece25e5b1/docs/session-mirror.md). Reported operation: [benchmark claims and limits](https://github.com/arrmlet/tracecraft/blob/97c6b7447f8e696f0116357d9f86bb0ece25e5b1/benchmarks/README.md), [product claims](https://github.com/arrmlet/tracecraft/blob/97c6b7447f8e696f0116357d9f86bb0ece25e5b1/README.md). | No checkout access gap. External hosts, service implementations and deployment evidence are not registered; prevents host-loop and universal backend guarantees. No run executed; tests and benchmark code do not establish passing results. Uninspected frozen benchmark outputs prevent independent numerical or causal conclusions here. |
