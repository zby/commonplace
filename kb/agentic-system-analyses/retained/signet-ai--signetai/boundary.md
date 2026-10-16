---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Signet's shipped memory, identity, maintenance and context-delivery system at frozen Git revision 12dba1ce753babda735f2ba7b6f150c6c0b7f95e."
run-id: AAS-2026-10-14-signetai-64f703d83203-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "12dba1ce753babda735f2ba7b6f150c6c0b7f95e"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/signet-ai/signetai
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/signetai-64f703d83203/related-systems/signet-ai--signetai
  revision: "12dba1ce753babda735f2ba7b6f150c6c0b7f95e"
  sha256: null
---

# Signet boundary

## Boundary and evidence

This run analyses Signet as the shipped memory, identity and context-delivery system, not merely its library API or its Dreaming worker. The intended use is to explain how captured evidence becomes retained state, how model-driven maintenance changes that state, and how later agents receive it. The target is in scope as a **memory/knowledge/context-engineering system**. Its own background maintenance issues model calls, and its shipped adapters serve retained context to model-using hosts (SRC-1, `platform/daemon/src/pipeline/dreaming-worker.ts`, `integrations/pi/extension/src/index.ts`).

The source's declared purpose is:

> Signet gives your AI agents a shared memory. You can use it to store, sync, and share memories, system prompts, transcripts, institutional knowledge, and secrets across all the AI tools and models you use.
> --- `README.md`

The boundary is **whole-system**: it includes evidence capture and imports; agent-scoped persistence and authorization; indexing, recall and context construction; Dreaming prompts, tools and audited mutations; identity and generated harness configuration; shipped CLI, SDK, integrations, browser and desktop clients; backup, recovery, maintenance and evaluation paths. These same-repository callers are part of the target, not external applications. The table below distinguishes boundary inclusion from inspection depth. Inclusion does not imply every implementation file has already been read.

### Initial entry-point and loop trace

The npm launcher calls `launchSignet`, whose implementation resolves and spawns a platform binary (SRC-1, `dist/signetai/bin/signet.js`, `dist/signetai/bin/launch.js`). The root workspace scripts identify CLI, daemon, native, connector and extension build surfaces (SRC-1, `package.json`). The CLI registers memory, sources and Dreaming commands; the daemon registers memory, hook, source, import, transcript-import, knowledge, ontology and pipeline routes (SRC-1, `surfaces/cli/src/cli.ts`, `platform/daemon/src/daemon.ts`). Memory routes import the transactional ingest and mutation functions together with recall and database-owner facilities (SRC-1, `platform/daemon/src/routes/memory-routes.ts`). The ingest implementation inserts memory content, source identity, agent scope and evidence metadata into SQLite (SRC-1, `platform/daemon/src/transactions.ts`).

The daemon starts a transcript-capture worker and a Dreaming worker through its pipeline startup path. The inspected startup explicitly distinguishes current semantic maintenance from legacy extraction:

> logger.info("dreaming", "Dreaming owns all semantic writes; legacy extraction is retired");
> --- `platform/daemon/src/daemon.ts`

Dreaming's executor calls the inference router with a prompt and tools; this establishes model-dependent operation rather than a passive storage library (SRC-1, `platform/daemon/src/pipeline/dreaming-worker.ts`). Shipped maintenance instructions are also in scope. Their mutation contract is declared, not treated here as proof that every handler enforces it:

> Do not rewrite raw transcript/source artifacts or edit SQLite directly.
> --- `skills/dreaming/SKILL.md`

The consumer side is shipped too. The Pi lifecycle implementation posts session-start and session-end payloads, reads session-file snapshots, and retains returned startup context. Its extension registers prompt, context and compaction handlers (SRC-1, `integrations/pi/extension-base/src/lifecycle.ts`, `integrations/pi/extension/src/index.ts`). The context handler returns hidden injected messages alongside the host's messages:

> messages: [...event.messages, ...hiddenMessages],
> --- `integrations/pi/extension/src/index.ts`

The SDK, dashboard and browser extension also call daemon memory or hook APIs. The desktop client manages daemon startup rather than being an excluded enclosing application (SRC-1, `libs/sdk/src/client-p2.ts`, `surfaces/dashboard/src/lib/api.ts`, `surfaces/browser-extension/src/shared/api.ts`, `surfaces/desktop/src/daemon-manager.ts`). MemoryBench's Signet provider calls remember, session-end and recall endpoints; its orchestrator includes ingest, indexing, search, answer and evaluation phases. Evaluation is therefore included as a shipped driver, not inferred from the README's reported score (SRC-1, `memorybench/src/providers/signet/index.ts`, `memorybench/src/orchestrator/index.ts`).

### Repository coverage

Every top-level tracked entry is classified below. “Included; mapped” means the tracked tree and entry wiring establish a material responsibility, but detailed implementation remains for later analysis. “Excluded” is a deliberate functional exclusion, not missing evidence. There is no identified unavailable material source path at this pin. All rows refer to SRC-1; listed paths are commit-relative anchors.

| Top-level tracked entry | Coverage and material paths | Role and limit |
| --- | --- | --- |
| `platform/` | Included; initial code inspection of `platform/daemon/src/daemon.ts`, `platform/daemon/src/routes/memory-routes.ts`, `platform/daemon/src/routes/hooks-routes.ts`, `platform/daemon/src/transactions.ts`, `platform/daemon/src/pipeline/dreaming-worker.ts`, `platform/daemon/src/pipeline/dreaming.ts`, `platform/native/src/lib.rs`; mapped `platform/core/src/migrations/`, database, identity, workspace, recall and search modules; daemon source providers, transcript capture/import, DB-owner workers, ontology operations, memory-head publication, maintenance, recovery, inference, auth and MCP paths | State production, admission, storage, semantic maintenance and retrieval. Individual enforcement, scheduling and failure semantics are not yet established by this boundary. |
| `integrations/` | Included; initially inspected `integrations/pi/extension/src/index.ts` and `integrations/pi/extension-base/src/lifecycle.ts`; mapped connectors for Claude Code, Codex, Forge, Gemini, Hermes, Kimi, Muse Code, Oh My Pi, OpenClaw, OpenCode and Pi; Codex plugin skills/hooks, Hermes plugin, OpenClaw memory adapter, OpenCode plugin, Oh My Pi extension and `integrations/unreal/plugin/` | Shipped capture, reload and consumption paths remain inside the system. Pi wiring is not evidence of identical lifecycle behavior across all hosts; those paths need their own inspection. |
| `libs/` | Included; initially searched `libs/sdk/src/client-p2.ts`; mapped generated SDK client, transport, AI/OpenAI helpers, `libs/connector-base/src/` and `libs/lifecycle-proof/src/` | Shared API consumption, integration installation and lifecycle instrumentation. Instrumentation code alone is not an observed trace. |
| `surfaces/` | Included; initially inspected CLI entry registration, dashboard API client, browser API client, desktop daemon manager and tray entry searches; mapped CLI command/features modules, `surfaces/cli/templates/`, dashboard onboarding/settings/chat/graph views, desktop runtime staging and tray controls | Operator admission, persistence requests, retrieval and runtime management. `surfaces/cli/templates/AGENTS.md.template` and `surfaces/cli/templates/DREAMING.md.template` were read; remaining templates and UI details are included but not yet inspected. |
| `dist/` | Included; read launcher and searched `dist/signetai/bin/launch.js`; mapped wrapper installation/runtime helpers, native-platform manifests, `dist/signetai/templates/` and bundled Hermes plugin | Shipping and bootstrap paths, including prompts and consumers. Actual release binaries and installed package contents are not supplied, preventing binary/source equivalence claims. |
| `skills/` | Included; read `skills/dreaming/SKILL.md`; mapped `skills/onboarding/SKILL.md` | Shipped maintenance and setup instructions. Onboarding details not yet inspected; maintenance instructions support doctrine, not observed compliance. |
| `memorybench/` | Included; inspected Signet provider and orchestrator excerpts/searches; mapped benchmark datasets, provider prompts, answer/evaluate/search/ingest phases, judges, checkpoints, server and UI | Shipped evaluation driver and evidence-consuming workflow. No benchmark execution or result verification was performed. Other provider adapters are comparison plumbing, not separate analysed systems. |
| `scripts/` | Included; mapped `scripts/bench-memory.ts`, `scripts/autoresearch-memorybench.ts`, `scripts/claim-trace-eval.ts`, `scripts/observer-belief-eval.ts`, `scripts/evals/`, MCP probes, native/build/staging tools, memory backfill and regression tests | Build, maintenance and evaluation support. Root scripts establish invocation wiring; detailed scripts are not yet inspected and do not establish performance. |
| `tests/` | Included; mapped `tests/integration/acceptance/`, pipeline LLM, search visibility, web-content indexing, stress and import regression paths | Test and acceptance contracts; not executed, so no test-pass claim. |
| `deploy/` | Included; mapped `deploy/docker/` entrypoint, compose, healthcheck/token scripts and `deploy/aur/`, `deploy/channels/` packaging | Deployment and access setup. Detailed deployment behavior not yet inspected; no live deployment assurance. |
| `docs/` | Included; mapped runbooks, architecture diagrams and `docs/specs/` approved/complete/draft contracts | Target-native doctrine and historical design. A spec's status does not establish current implementation. No external analysis is imported. |
| `web/` | Included: read `web/docs/src/content/docs/architecture/packages-data-flow.md`; mapped remaining API, pipeline, hooks, harness, memory, source and benchmark documentation, plus `web/marketing/public/install.sh`, `web/marketing/public/install.ps1`, `web/marketing/public/skill.md`. Excluded: marketing presentation/blog/testimonials, ads and `web/workers/reviews/` | Documentation, installers and operator setup belong to the boundary. Marketing and review-service exclusion prevents conclusions about public-site operation or marketplace reviews, not local memory behavior. Unread installers remain included, not an access gap. |
| `.agents/` | Included; read `.agents/skills/benchmarking/SKILL.md`; mapped benchmarking reference/scripts/results, Dreaming development and other repository-agent instructions | Target-native evaluation and development procedures. Uninspected results are not independently verified evidence. |
| `.claude/` | Included; mapped `.claude/skills` | Instruction projection; projection behavior not yet inspected. |
| `.github/` | Included; mapped build, release, Docker, Dreaming benchmark gate, migration, event-loop, transcript-import and acceptance workflows. Excluded: issue/PR templates and PR screenshots | Shipped CI/evaluation and release wiring. Exclusion prevents conclusions about issue administration and screenshot fidelity. No CI success inferred. |
| `.githooks/` | Included; mapped commit-message and pre-commit hooks | Development gates; enforcement not tested. |
| `package.json`, `bun.lock`, `bunfig.toml`, `biome.json`, `tsconfig.json`, `turbo.json`, `.bump-level`, `.dockerignore`, `.gitignore` | Included; root `package.json` read; remaining configuration mapped | Workspace entry points, dependency/build and packaging contracts. Dependency implementations are not frozen by a lockfile alone. |
| `AGENTS.md`, `CLAUDE.md`, `AI_POLICY.md`, `CONTRIBUTING.md` | Included; mapped | Repository development instructions, not user memory content. Not yet inspected; no claim of development-policy compliance. |
| `README.md`, `README.de.md`, `README.ja.md`, `README.ko.md`, `README.zh-CN.md`, `VISION.md`, `ROADMAP.md`, `CHANGELOG.md`, `repo.map.yaml`, `SECURITY.md` | Included; English README read, remaining documents mapped | Declared purpose, orientation, plans/history and security guidance. Translations and historical statements are not independently corroborated. |
| `CODE_OF_CONDUCT.md`, `LICENSE`, `NOTICE`, `THIRD_PARTY_LICENSES.md` | Excluded; tracked root documents | Community and legal materials; no legal or licensing assessment. |
| `public/`, `screenshots/` | Excluded; image/branding assets and UI illustrations | No conclusions about rendered visual fidelity or screenshot authenticity. |

### Frozen evidence and external limits

The only frozen source is the acquired repository at full commit **12dba1ce753babda735f2ba7b6f150c6c0b7f95e**; checkout HEAD was checked against that pin. The applicability cutoff is **2026-10-14**, the supplied run date. This fixes source applicability, not the date of a deployment or a measured execution. Evidence tier is **code-grounded**, with target-native documentation separately labelled as doctrine/design.

External agent harness implementations, model providers and model weights, remote source services, OS/keyring behavior, downloaded release assets and dependency internals are outside the frozen source. Signet's adapters and provider/service routing remain included. These limits prevent conclusions about an external host's complete agent loop, provider reliability or answer quality, actual remote-service behavior, and cross-platform deployment correctness. The Bun/Node/Rust/native and embedding/search dependencies are visible as manifests and interfaces, not independent implementation sources (SRC-1, `package.json`, `platform/native/src/lib.rs`, `dist/signetai/bin/launch.js`).

No target execution, tests, model calls or live-service inspection was performed. Code supports an account of executable paths; documentation supports attributed intent. Neither supplies observed operation or a causal experiment. The reported benchmark score in the README is not adopted as a verified result. No live documentation page or unpinned repository is additional evidence.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/signet-ai/signetai` | 12dba1ce753babda735f2ba7b6f150c6c0b7f95e | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/signetai-64f703d83203/related-systems/signet-ai--signetai`. Implementation: tracked tree and root workspace scripts; launcher; daemon route/startup wiring; memory transaction and route excerpts; Dreaming executor and state/prompt searches; Pi extension/context and shared lifecycle excerpts; SDK, dashboard/browser API and desktop/tray entry searches; MemoryBench Signet provider and orchestrator searches; native module entry. Doctrine/design: English README, Dreaming skill, benchmarking skill, CLI AGENTS/DREAMING templates and package/data-flow architecture page. These are initial inspected paths, not an allowlist; all included paths at this commit may supply later evidence. | Implementation: [daemon](https://github.com/signet-ai/signetai/blob/12dba1ce753babda735f2ba7b6f150c6c0b7f95e/platform/daemon/src/daemon.ts), [Dreaming executor](https://github.com/signet-ai/signetai/blob/12dba1ce753babda735f2ba7b6f150c6c0b7f95e/platform/daemon/src/pipeline/dreaming-worker.ts), [Pi consumer](https://github.com/signet-ai/signetai/blob/12dba1ce753babda735f2ba7b6f150c6c0b7f95e/integrations/pi/extension/src/index.ts), [evaluation provider](https://github.com/signet-ai/signetai/blob/12dba1ce753babda735f2ba7b6f150c6c0b7f95e/memorybench/src/providers/signet/index.ts). Doctrine/design: [README](https://github.com/signet-ai/signetai/blob/12dba1ce753babda735f2ba7b6f150c6c0b7f95e/README.md), [maintenance instruction](https://github.com/signet-ai/signetai/blob/12dba1ce753babda735f2ba7b6f150c6c0b7f95e/skills/dreaming/SKILL.md), [data-flow contract](https://github.com/signet-ai/signetai/blob/12dba1ce753babda735f2ba7b6f150c6c0b7f95e/web/docs/src/content/docs/architecture/packages-data-flow.md). Additional local anchors appear in the trace and coverage table. | No identified inaccessible material checkout paths. External dependencies and release binaries are not captured. No observed-run or causal-experiment layer established; runtime correctness, benchmark scores, deployment equivalence and provider outcomes cannot be concluded from this initial inspection. Mapped-but-unread files are inspection work remaining, not missing access. |
