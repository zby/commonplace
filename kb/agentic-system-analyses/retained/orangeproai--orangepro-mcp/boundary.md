---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "OrangePro's shipped CLI, MCP tools and evidence-to-test workflow at commit 039cd936e38eb7d52d0e03ded3b3168373d55d77."
run-id: AAS-2026-11-08-orangepro-mcp-4e3d3a22c7c8-01
result-disposition: complete
target-class: extension or tool mechanism
boundary-kind: whole-system
reviewed-boundary: "039cd936e38eb7d52d0e03ded3b3168373d55d77"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/orangeproai/orangepro-mcp
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/orangepro-mcp-ee88f4b60339/related-systems/orangeproai--orangepro-mcp
  revision: "039cd936e38eb7d52d0e03ded3b3168373d55d77"
  sha256: null
---

# OrangePro boundary

## Boundary and evidence

The target is the shipped OrangePro repository: its local evidence graph, test-drafting and proof workflow, CLI and MCP interfaces, agent-facing instructions, platform API adapters and ancillary deployment code. Its intended use is to identify test gaps in a checkout, supply grounded test drafts and distinguish test associations from targeted mutation evidence. This is an **extension or tool mechanism**, not the enclosing coding-agent runtime. Its model-dependent generation and candidate-link lanes qualify it for analysis even though analysis, ranking and proof can operate without a model. SRC-1: `package.json`, `src/local/operations.ts`, `src/local/mcp.ts`.

The boundary is **whole-system** for this shipped artifact, not for OrangePro's remotely hosted platform or the user's coding environment. The package binaries enter `dist/local/cli.js`; the launcher resolves that same engine. The repository also contains a separate platform stdio entry and a remote HTTP worker. These shipped paths remain included rather than being mistaken for external applications. SRC-1: `package.json`, `packages/mcp-server/bin/mcp-server.js`, `src/index.ts`, `src/server.ts`, `packages/mcp-remote/src/index.ts`.

> const cliPath = require.resolve("@orangepro/orangepro-mcp/dist/local/cli.js");
> --- `packages/mcp-server/bin/mcp-server.js`

Initial tracing covers production, retention, admission and later consumption of local state. `opAnalyze` builds a graph from source and enrichers, preserves generated artifacts and candidate flows, and saves it. `opGenerate` reloads that graph, resolves a provider, invokes generation, persists fresh drafts and refreshes reports. The start driver invokes analysis, optional AI linking and flow discovery, automatic proof and gap drafting. Proof results enter a ledger, and traceability/report consumers reload graph and ledger. These are shipped responsibilities, including automatic test execution, not solely responsibilities of an external coding agent. SRC-1: `src/local/operations.ts`, `src/local/workspace.ts`.

> const closed = dynamicProofSucceeded(oracle);
> --- `src/local/operations.ts`

> const result = buildRtm(graph, loadLedger(root), { targetIds, changedFiles, statuses: opts.statuses, limit: opts.limit, scope });
> --- `src/local/operations.ts`

The agent workflow also instructs a host agent to write and run returned drafts and submit proof arguments. This host-driven path coexists with the shipped automatic and assisted paths; it does not justify classifying the repository as only a returning library API. The skill's broad non-execution wording is documentation evidence, not a boundary that removes the executable proof drivers. SRC-1: `src/local/agentWorkflow.ts`, `rules/orangepro.mdc`, `skills/opro/SKILL.md`, `src/local/operations.ts`, `src/local/draftTest.ts`.

> "Write each runnable test body to its `suggested_path`, run its `run_command` from the owning package, then call the returned `prove_run` args after a pass to attempt public Proven. Use `record_run` only for static diagnostics.",
> --- `src/local/agentWorkflow.ts`

The revision is frozen at **039cd936e38eb7d52d0e03ded3b3168373d55d77**, verified as the checkout's HEAD. The applicability cutoff is **2026-11-08**, the supplied run date; it makes no claim about later revisions. The overall evidence tier is **code-grounded**. Inspection is static: no target execution, provider call, test run or service deployment was performed. Test source is evidence of encoded checks, not observed passing results. Documentation and comments supply declared contracts, not independent demonstrations.

External dependencies include the coding-agent/MCP host, Node and package dependencies, customer checkout and its runners, configured model endpoints, Docker for the containerized verification lane, GitHub for delivery, and the OrangePro backend for platform tools. Host planning, host context management and user authorization are not attributed to this target. The backend implementation is not in the frozen source: adapter inspection cannot establish backend scheduling, model prompts, knowledge-graph persistence or tenant isolation. Provider service internals and customer runs are likewise unavailable, preventing conclusions about actual model quality, live reliability, cost and end-to-end effectiveness. SRC-1: `package.json`, `src/local/generate/providers.ts`, `src/local/actionsRun.ts`, `src/local/publishTests.ts`, `packages/mcp-remote/src/index.ts`.

### Shipped-path coverage

Included means within the functional analysis boundary, not exhaustively read. The initial inspection follows the material entry points and state loop above. Remaining helpers, release prose and fixtures are available at this same pin for later inspection; they are not access gaps. All rows refer to SRC-1.

| Top-level tracked path | Treatment and material paths or role | Inspection and conclusion limit |
|---|---|---|
| `.agents/` | Included: `plugins/marketplace.json`, agent distribution metadata. | Tree inventoried; metadata not yet read. No claim about installation behavior. |
| `.claude-plugin/` | Included: `marketplace.json`, plugin discovery. | Tree inventoried; not yet read. No claim about marketplace operation. |
| `.github/` | Included: `workflows/ci.yml`, repository CI. | Tree inventoried; CI configuration not yet read or run. No passing-CI conclusion. |
| `.gitignore` | Included: source-control exclusions. | Inventoried, not yet read. |
| `.npmignore` | Included: packaging exclusions. | Inventoried, not yet read; packaging intent initially traced through `package.json`. |
| `CLAUDE.md` | Included: repository contributor/agent instructions. | Inventoried, not yet read; not adopted as worker instructions. |
| `Dockerfile` | Included: container packaging. | Inventoried, not yet read; no image-build claim. |
| `LICENSE` | Included: licensing metadata. | Inventoried, not yet read; no legal assessment. |
| `QUICKSTART.md` | Included: user onboarding. | Available, not yet read. |
| `README.md` | Included: intended workflow, reports and configuration. | Opening product description and workflow inspected; remaining sections available. |
| `docs/` | Included: `agent-workflow.md`, `agents/*.md`, `local-proof-kit.md`, `reproducibility.md`, maintenance and release documents; images and example HTML are presentation material. | Paths inventoried. Detailed prose and rendered examples not yet inspected; no historical release or screenshot-result finding established. |
| `examples/` | Included: requirements Markdown and CSV inputs. | Inventoried, not yet read; no example execution. |
| `glama.json` | Included: integration metadata. | Inventoried, not yet read. |
| `infra/` | Included: `telemetry-worker/src/index.ts`, schema and deployment configuration. Excluded from evidence extraction: tracked `.wrangler/` cache/database binaries. | Worker notification/storage code initially inspected. Cached deployment state deliberately not decoded, preventing claims about actual telemetry traffic or deployed database contents. No current CLI telemetry connection inferred from this directory's existence. |
| `package-lock.json` | Included: dependency resolution. | Available, not yet read; no dependency-security assessment. |
| `package.json` | Included: binaries, package file list, build and test entry points. | Inspected completely; scripts not executed. |
| `packages/` | Included: `mcp-server/bin/mcp-server.js` engine launcher and `mcp-remote/src/index.ts` HTTP platform adapter, with package/deployment configuration. | Launcher and remote implementation inspected. Backend service behavior remains outside the source. |
| `plugins/` | Included: OrangePro plugin manifests, `.mcp.json`, `rules/orangepro.mdc`, `skills/opro/SKILL.md`. | MCP configuration inspected; plugin instruction copies and manifests inventoried, not yet compared with root instructions. |
| `rules/` | Included: `orangepro.mdc`, host-agent gap/generation/proof procedure. | Inspected completely as doctrine. |
| `scripts/` | Included: packaged JS/TS, Go, Java and Python proof runners/mutators/reporters under `spikes/`; smoke, validation, build and release drivers. | Inventory and package shipping references inspected; runner internals not yet read. No claim about mutation correctness or measured coverage. |
| `server.json` | Included: MCP registry metadata. | Inventoried, not yet read. |
| `skills/` | Included: `opro/SKILL.md`, host-driven test workflow. | Inspected completely as doctrine; not assumed to override newer executable paths. |
| `src/` | Included: local `cli.ts` and `mcp.ts`; `operations.ts`, `workspace.ts`, generation/providers/prompts, graph/analyzer, freshness/reuse, ledger/proof/traceability/reports; assisted `draftTest.ts`, Actions verification and `publishTests.ts`; platform `index.ts`, `server.ts`, API and QA handlers. | Entry-point wiring, state save/reload, generation, start, certificate construction and traceability consumer inspected in bounded ranges; assisted/delivery modules initially inspected through interfaces and declared contracts. Algorithm and security details remain for later tracing, not established by this boundary. |
| `tests/` | Included: API adapter tests, `local/` state/generation/proof/security/integration suites and fixtures. | Inventory inspected; `local/pinnedDrafts.test.ts` initially inspected for retained-draft test design. No tests executed, no pass-rate or effectiveness claim. |
| `tsconfig.build.json` | Included: build selection. | Inventoried, not yet read. |
| `tsconfig.json` | Included: compiler configuration. | Inventoried, not yet read. |
| `vitest.config.ts` | Included: test harness configuration. | Inventoried, not yet read; no execution evidence. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/orangeproai/orangepro-mcp` | 039cd936e38eb7d52d0e03ded3b3168373d55d77 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/orangepro-mcp-ee88f4b60339/related-systems/orangeproai--orangepro-mcp`. Full tracked tree inventoried. Implementation: package binaries and launcher; platform stdio server and complete remote worker; local CLI dispatch search and MCP entry; bounded `operations.ts` analysis/start/generation/proof/RTM ranges; graph persistence; provider HTTP and OpenAI Responses adapter; assisted draft/Actions/delivery interfaces; telemetry worker opening; pinned-draft test opening. Doctrine/design: README opening, root skill/rule, workflow-pack instructions and implementation comments. Listed paths are initial coverage, not an allowlist. | Implementation: [package entry points](https://github.com/orangeproai/orangepro-mcp/blob/039cd936e38eb7d52d0e03ded3b3168373d55d77/package.json), [local operations](https://github.com/orangeproai/orangepro-mcp/blob/039cd936e38eb7d52d0e03ded3b3168373d55d77/src/local/operations.ts), [remote adapter](https://github.com/orangeproai/orangepro-mcp/blob/039cd936e38eb7d52d0e03ded3b3168373d55d77/packages/mcp-remote/src/index.ts). Doctrine/design: [agent workflow](https://github.com/orangeproai/orangepro-mcp/blob/039cd936e38eb7d52d0e03ded3b3168373d55d77/src/local/agentWorkflow.ts), [skill](https://github.com/orangeproai/orangepro-mcp/blob/039cd936e38eb7d52d0e03ded3b3168373d55d77/skills/opro/SKILL.md), [rule](https://github.com/orangeproai/orangepro-mcp/blob/039cd936e38eb7d52d0e03ded3b3168373d55d77/rules/orangepro.mdc). | No checkout access gap identified. External hosted backend, provider internals and customer/host execution are not supplied: no inference about their internal policies or observed end-to-end performance. Tests and reported examples are not observed runs in this analysis. Tracked binary infrastructure cache is deliberately excluded as above. |
