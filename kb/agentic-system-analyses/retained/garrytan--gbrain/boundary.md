---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "GBrain's shipped memory and context artifact at da434385572e0dc0d825649179aabed4107d6e60, with partial initial loop inspection."
run-id: AAS-2026-10-11-gbrain-9de8e3c225d3-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: da434385572e0dc0d825649179aabed4107d6e60
analysis-cutoff: "2026-10-11"
evidence-tier: code-grounded
source:
  identity: https://github.com/garrytan/gbrain
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/gbrain-9de8e3c225d3/related-systems/garrytan--gbrain
  revision: da434385572e0dc0d825649179aabed4107d6e60
  sha256: null
---

# GBrain boundary

## Boundary and evidence

This run analyses GBrain as a memory/knowledge/context-engineering system serving existing agents. Its intended use is explicit memory with provenance, retrieval, correction and withdrawal, with optional synthesis and background enrichment. The target is the shipped repository artifact, not just its exported engine API or one MCP tool. The CLI, MCP transports, shipped agent instructions, context integration, maintenance and evaluation paths belong to the target. SRC-1 `README.md`, `package.json`, `src/core/operations.ts`.

> **Give the agent you already use a memory you control.** GBrain stores explicit facts with their sources, supports corrections and withdrawal, and makes the same memory available across your agents. Start with keyless memory and keyword retrieval; add semantic search, synthesis, and background enrichment when you need them.
> --- `README.md`

The boundary kind is **complete artifact, partial loop**, not whole-system. Initial inspection establishes shipped entry points and representative admission, read, context-consumption, maintenance and evaluator paths. It does not exhaustively trace every state producer, persistence owner, background driver, host adapter or evaluator. Those available but uninspected paths are not access gaps or excluded applications. They remain part of the registered artifact and may supply later evidence at the same commit. This boundary prevents an initial claim of complete loop coverage; it does not restrict later inspection to the paths listed in the source register.

### Entry points and initial responsibility trace

- **CLI and library:** `package.json` exposes `src/cli.ts` as the executable and `src/core/index.ts` as the library entry, with additional engine, operations, search, synthesis, ingestion, AI and optimizer exports. The executable dynamically loads `src/cli/main.ts`. The inspected operation registry assembles page, search, graph, memory, job, skill, extraction and other handlers. Same-repository command drivers are included, not treated as external library consumers. SRC-1 `package.json`, `src/cli.ts`, `src/core/operations.ts`.
- **Capture and admission:** the CLI capture branch chooses remote MCP, local-owner delegation or an in-process operation handler. The registered `capture` handler submits a page mutation. The inspected admission function prepares a request, calls `admitWrite`, and waits for a receipt. This establishes a shipped state-admission path, not proof that every publication or crash-recovery path succeeds. SRC-1 `src/commands/capture.ts`, `src/core/ops/pages.ts`, `src/core/persistence/page-mutations.ts`.

> return submitPageMutation(ctx, { operation: 'capture', params: p });
> --- `src/core/ops/pages.ts`

> const response = throwIfHeld(pendingAwareResponse(ctx, await waitForWrite(ctx.engine, row, ctx.config, waitMs())), false);
> --- `src/core/persistence/page-mutations.ts`

- **Retained-memory reads:** `recall` is registered as a read operation with entity, question, query, source and token-budget parameters. Its inspected handler resolves source scope and local-versus-remote visibility before reading eligible facts; bounded searches also identify its engine fact-query call sites. The full packing and retrieval implementation has not yet been inspected. SRC-1 `src/core/ops/facts.ts`.
- **Model-facing consumption:** the shipped query skill instructs an agent to retrieve, read, synthesize and cite stored content. This is an instruction contract, not evidence of compliance. The OpenClaw plugin is explicitly shipped in `package.json`; its registration creates the repository's context engine. The inspected assembly branch combines live context, core-memory additions, checkpoint information and resolved entity pointers into `systemPromptAddition`. The host still owns the enclosing conversation runtime. SRC-1 `skills/query/SKILL.md`, `package.json`, `src/openclaw-context-engine.ts`, `src/core/context-engine.ts`.

> 3. **Read top results.** Read the top 3-5 pages from gbrain to get full context.
> 4. **Synthesize answer** with citations. Every claim traces back to a specific page slug.
> --- `skills/query/SKILL.md`

> systemPromptAddition: parts.join('\n\n'),
> --- `src/core/context-engine.ts`

- **Maintenance:** `runMaintain` reads health and doctor reports, invokes stale extraction and source-cycle maintenance, then emits before/action/after results. Dream-cycle internals and scheduled drivers remain to be traced. The separate capture skill is included as shipped ingestion doctrine; its explanatory text does not override the current executable admission path. SRC-1 `src/commands/maintain.ts`, `skills/capture/SKILL.md`.
- **Evaluation:** the inspected BrainBench command loads a corpus, refuses an empty fixture set, and calls `runBrainBench` with harness, suite, holdout, model-use and budget settings. The harness internals and adapters are available but not yet inspected; this establishes an evaluator entry point, not validated quality scores. SRC-1 `src/commands/eval-brainbench.ts`.

### Functional inclusions and inspection limits

The tracked-tree inventory was inspected at the frozen HEAD. The following is an artifact map, not a whole-system coverage claim. Grouped rows account for every top-level tracked entry; inspection status distinguishes initial source reading from inventory-only visibility.

| Tracked area | Boundary treatment and role | Initial inspection and conclusion limit |
|---|---|---|
| `src/` | Included: CLI, commands, core state machinery, model gateway, MCP, context plugin, evaluators, assets and types | Representative paths above inspected. Most implementation branches remain uninspected; no exhaustive lifecycle or authority guarantee. |
| `skills/`, `plugin/`, `plugin-variants/`, `.agents/`, `.claude-plugin/`, `.codex-plugin/`, `openclaw.plugin.json` | Included: ingestion, retrieval, maintenance, migration and host-facing skill distribution | Capture/query skills and package wiring inspected; other prompts and distribution copies inventoried only. No claim that every installed host receives or obeys the intended protocol. |
| `templates/`, `recipes/`, `examples/`, `gbrain.yml` | Included: bootstrap material, integration procedures, example skillpacks and repository configuration | Inventory only. No end-to-end bootstrap, connector or example-workflow conclusion. |
| `admin/` | Included: shipped administration UI and its supporting build configuration | Inventory only. No UI authority or client-management safety conclusion. |
| `evals/`, `.gbrain-evals`, `test/`, `tests/` | Included as evaluator, fixture and test evidence where inspected | Inventory plus BrainBench command inspection. No tests executed, no fixture/adaptor completeness or measured-quality conclusion. |
| `scripts/`, `native/`, `patches/`, `vendor/`, `third-party/`, `tools/` | Included where they implement shipped build, installation, storage, maintenance or evaluation responsibilities | Inventory and package-script declarations only. No native lock, patched dependency, install or release correctness conclusion. |
| `README.md`, `AGENTS.md`, `CLAUDE.md`, `BOOTSTRAP_FOR_AGENTS.md`, `INSTALL_FOR_AGENTS.md`, `DESIGN.md`, `docs/`, `llms.txt`, `llms-full.txt` | Included as shipped operational and design doctrine | README inspected completely; other documents inventoried only. No doctrine-to-code consistency conclusion beyond cited passages. |
| `package.json`, `bun.lock`, `bunfig.toml`, `tsconfig.json`, `VERSION`, `.env.testing.example` | Included as entry-point, dependency, runtime and build metadata | Package inspected; other metadata inventoried only. No dependency reproducibility or supported-environment verification. |
| `.github/`, `.gstack`, `.gitattributes`, `.gitignore`, `.gitleaks.toml`, `.gitleaksignore`, `CONTRIBUTING.md`, `SECURITY.md`, `CHANGELOG.md`, `TODOS.md`, `LICENSE`, `docker-compose.ci.yml`, `docker-compose.test.yml`, `dbg-tmp.ts` | Available repository governance, history, security/build support and development material; not evidence of deployed behavior merely by being tracked | Inventory only. No audit of project governance, historical fixes, CI, security posture or debugging behavior. Material shipped responsibilities found here remain within the artifact boundary. |

External host runtimes, their user configurations and private brain corpora are excluded unless their behavior is represented in the frozen repository. GBrain's shipped integration code and instructions are included, but OpenClaw, Hermes, Claude Code, Codex and other hosts are not themselves analysed. This prevents attributing host scheduling, conversation persistence, compaction or model compliance to GBrain. SRC-1 `README.md`, `src/openclaw-context-engine.ts`, `src/core/context-engine.ts`.

> ownsCompaction: false,  // delegate to legacy runtime
> --- `src/core/context-engine.ts`

Bun, PGLite/Postgres, model-provider SDKs and services, and optional connector infrastructure are external dependencies; only their shipped declarations and integration code at this pin are evidence here. This prevents independent claims about provider internals, live service availability or deployment compatibility. SRC-1 `package.json`, `README.md`.

The immutable boundary is commit `da434385572e0dc0d825649179aabed4107d6e60` of `https://github.com/garrytan/gbrain`; the local checkout's HEAD matched that commit and its working tree was clean. The applicability cutoff is the opening run date, **2026-10-11**. Later commits and live linked repositories/pages are outside the evidence set. No target execution, service calls or experiments were performed. The overall tier is **code-grounded**, with doctrine separately labelled. There is no inspected observed-run or causal-experiment evidence. Deployment numbers and performance claims in the README are only reported operation, not verified measurements. SRC-1 `README.md`.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/garrytan/gbrain` | da434385572e0dc0d825649179aabed4107d6e60 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/gbrain-9de8e3c225d3/related-systems/garrytan--gbrain`. Implementation: complete `package.json`, `src/cli.ts`, `src/core/operations.ts`, `src/openclaw-context-engine.ts`, `src/commands/maintain.ts`; bounded portions of `src/commands/capture.ts`, `src/core/ops/pages.ts`, `src/core/persistence/page-mutations.ts`, `src/core/ops/facts.ts`, `src/core/context-engine.ts`, `src/commands/eval-brainbench.ts`; bounded entry-point searches in `src/cli/main.ts`, `src/commands/recall.ts`, `src/mcp/dispatch.ts`. Doctrine/design: complete `README.md`, `skills/capture/SKILL.md`, `skills/query/SKILL.md`. Reported operation: README deployment and performance assertions only. Tracked top-level inventory and directory summaries inspected. | Implementation: [package entry points](https://github.com/garrytan/gbrain/blob/da434385572e0dc0d825649179aabed4107d6e60/package.json), [operation registry](https://github.com/garrytan/gbrain/blob/da434385572e0dc0d825649179aabed4107d6e60/src/core/operations.ts), [page admission](https://github.com/garrytan/gbrain/blob/da434385572e0dc0d825649179aabed4107d6e60/src/core/persistence/page-mutations.ts), [context consumer](https://github.com/garrytan/gbrain/blob/da434385572e0dc0d825649179aabed4107d6e60/src/core/context-engine.ts), [maintenance](https://github.com/garrytan/gbrain/blob/da434385572e0dc0d825649179aabed4107d6e60/src/commands/maintain.ts), [evaluator entry](https://github.com/garrytan/gbrain/blob/da434385572e0dc0d825649179aabed4107d6e60/src/commands/eval-brainbench.ts). Doctrine: [query skill](https://github.com/garrytan/gbrain/blob/da434385572e0dc0d825649179aabed4107d6e60/skills/query/SKILL.md). Doctrine and reported operation: [README](https://github.com/garrytan/gbrain/blob/da434385572e0dc0d825649179aabed4107d6e60/README.md). | No repository access gap established. Available but uninspected material is identified above, not classified as unavailable. Private deployments, external host implementations and live evaluation sources were not acquired; no verified deployment, cross-host continuity, causal performance or universal security conclusion follows. No observed run or causal experiment inspected. |
