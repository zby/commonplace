---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "OpenWiki's shipped knowledge-generation, maintenance and consumption paths at commit 7c469e59584bfac3f97f5c32a67604de46805999."
run-id: AAS-2026-10-14-openwiki-8f502f680f75-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "7c469e59584bfac3f97f5c32a67604de46805999"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/langchain-ai/openwiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/openwiki-8f502f680f75/related-systems/langchain-ai--openwiki
  revision: 7c469e59584bfac3f97f5c32a67604de46805999
  sha256: null
---

# OpenWiki boundary

## Boundary and evidence

OpenWiki is in scope as a model-dependent knowledge system. Its intended use is to produce and maintain linked Markdown knowledge from repository source or personal knowledge sources, then make retained pages available to humans and coding agents. The target is the shipped OpenWiki system, not just its retrieval API or repository-generation library. The classification is `memory/knowledge/context-engineering system`; the boundary kind is `whole-system`. This includes the native model-driven runtime, host-driven generation protocol, deterministic state management, ingestion, retrieval, scheduling, visualization, instructions and evaluation drivers. SRC-1, `README.md`, `package.json`, `src/agent/index.ts`, `src/integrations/core/session-manager.ts`.

The package declares its CLI and Pi integration as shipped surfaces:

> "bin": {
>     "openwiki": "./dist/cli/cli.js"
>   },
> --- `package.json`

> "pi": {
>     "extensions": [
>       "./dist/integrations/pi/openwiki.js"
>     ],
>     "skills": [
>       "./integrations/openwiki"
>     ]
>   },
> --- `package.json`

The native CLI dispatches ingestion, interactive and print runs, integration/MCP commands, workspace management and visualization. Repository init/update dispatches from `runOpenWikiAgent` to `runNativeRepositoryGeneration`; the latter begins or resumes the repository run, plans it, runs page agents and finishes it. Personal ingestion pulls source data where possible, then invokes an update of the local wiki. These shipped callers are included rather than treated as external applications. SRC-1, `src/cli/cli.tsx`, `src/cli/runners.ts`, `src/agent/index.ts`, `src/agent/repository-runner.ts`, `src/ingestion/ingestion.ts`.

> const isRepositoryGeneration =
>     outputMode === "repository" && (command === "init" || command === "update");
> --- `src/agent/index.ts`

The shared repository lifecycle admits written pages and sparse Claim decisions, persists Claim state before recording page completion, and performs deterministic finalization before removing resumable state. Host integrations call this same lifecycle; the external coding host supplies semantic research, page prose and its own model session. OpenWiki's host-facing instructions and protocol are included, but the host's independent runtime is not attributed to OpenWiki. SRC-1, `src/generation/repository-run.ts`, `src/generation/run-state.ts`, `src/integrations/core/session-manager.ts`, `integrations/openwiki/SKILL.md`.

> OpenWiki owns run state, the page queue, Claims validation/persistence, indexes,
> provenance, and finalization. You own semantic repository research and the prose
> for the single page OpenWiki assigns you.
> --- `integrations/openwiki/SKILL.md`

> await run.claimsRuntime.finalize(run.state.startedAt, otherPendingPages);
>       await assertPageClaimsDurable(run, current.path);
> --- `src/generation/repository-run.ts`

Consumption is part of this boundary. Retrieval discovers retained pages and reads their Markdown, while the integration skill instructs a host to search for concrete uncertainties and read selected sections. Personal chat has a wiki-first prompt. The source also ships managed repository instruction snippets, a visualizer and evaluation callers that generate, preserve, reload or supply wiki artifacts to another agent. SRC-1, `src/retrieval/wiki.ts`, `src/integrations/core/retrieval-tools.ts`, `src/agent/prompts/personal.ts`, `src/ingestion/code-mode.ts`, `evals/ledger/run/runner.ts`, `evals/deepswe/openwiki_codex.py`.

> const store = new ClaimsStore(wiki.root);
>     for (const page of await store.discoverPages()) {
>       if (!isRetrievableWikiPage(page)) continue;
>       const markdown = await store.readMarkdown(page);
>       units.push(...searchUnits(markdown, page, terms, wiki.id));
>     }
> --- `src/retrieval/wiki.ts`

The frozen evidence is the acquired Git checkout at `7c469e59584bfac3f97f5c32a67604de46805999`, with applicability cutoff `2026-10-14`. HEAD was checked against that pin and the tracked tree was enumerated read-only. Overall evidence is `code-grounded`: executable source supports the boundary, with source-native documentation and prompts supplying declared intent. No target, test, example, provider call or evaluation was executed. Evaluator code is evidence of a shipped evaluation mechanism, not an observed experiment result.

### Tracked-tree coverage

The table accounts for every top-level tracked file or directory in SRC-1. Included directories remain available for later inspection at the same pin. “Initial inspection” records what was actually read or traced here; inventory-only material is not presented as inspected behavior. All paths in this table are commit-relative anchors under SRC-1.

| Top-level entry | Treatment and role | Initial inspection and limits |
| --- | --- | --- |
| `src` | Included: shipped implementation and callers. Material paths include `src/cli/cli.tsx`, `src/cli/runners.ts`, `src/cli/app/app.tsx`; `src/agent/index.ts`, `src/agent/repository-runner.ts`, `src/agent/repository-prompts.ts`, `src/agent/prompts/code.ts`, `src/agent/prompts/personal.ts`, `src/agent/wiki-finalizer.ts`, `src/agent/okf-middleware.ts`, `src/agent/skills.ts`; `src/generation`, `src/claims`, `src/okf`; `src/ingestion`, `src/connectors`; `src/integrations`, `src/retrieval`, `src/linking`; `src/scheduling`, `src/visualize`; setup, auth, config, telemetry, platform and Mermaid support. | Traced CLI dispatch, native generation routing, planner creation, page admission/finalization, persisted run-state read/write, host lifecycle, retained-page retrieval, personal ingestion and managed setup. Read personal and repository planner prompt portions and bundled-skill synchronization. Other support implementations and detailed algorithms remain for later inspection; this boundary does not certify their correctness. |
| `integrations` | Included: shipped host instructions and metadata, particularly `integrations/openwiki/SKILL.md` and `integrations/openwiki/agents`. | Read the complete skill, including generation, Claim reconciliation and later retrieval instructions. Agent metadata inventoried, not yet inspected. |
| `skills` | Included: bundled `skills/mermaid-diagrams/SKILL.md` and `skills/write-connector/SKILL.md`. | Inventoried; delivery traced through `src/agent/skills.ts` and agent skill registration. Individual instruction bodies not yet inspected. |
| `evals` | Included: `evals/ledger` longitudinal generation/evaluation and `evals/deepswe` downstream agent-consumption experiment driver, including their tests and benchmark fixtures. | Read LEDGER/DeepSWE documentation portions, the complete `evals/ledger/system/openwiki-system.ts`, checkpoint loop in `evals/ledger/run/runner.ts`, and generation/cache/copy portions of `evals/deepswe/openwiki_codex.py`. Evaluator internals, benchmark contents and result analysis remain uninspected. No measured benefit or grounding accuracy is established here. |
| `examples` | Included: `examples/openwiki-update.yml`, `examples/openwiki-update-auto-merge.yml`, `examples/openwiki-update.bitbucket-pipelines.yml`, `examples/openwiki-update.gitlab-ci.yml` operational callers. | Inventoried, not yet read. The repository's own scheduled driver was read separately. No cross-platform scheduling equivalence is established here. |
| `openwiki` | Included: shipped self-documentation/artifact example: pages, `openwiki/INSTRUCTIONS.md`, `openwiki/.claims`, `openwiki/.page-manifest.json`, `openwiki/.last-update.json`. | Read only `openwiki/INSTRUCTIONS.md`; inventoried the rest. Generated self-descriptions and sidecars are target-authored artifacts, not independent verification or observed run evidence. |
| `test` | Included: source-native behavior contracts across agent, generation, Claims, ingestion, retrieval, integrations, scheduling and other support subsystems. | Tree inventoried; test bodies not yet inspected or executed. Presence alone establishes neither passing tests nor runtime guarantees. |
| `.github` | Included: CI, release and maintenance drivers; material maintenance path `.github/workflows/openwiki-update.yml`. | Read that scheduled dogfood update/PR workflow completely; other workflows and issue templates inventoried. No hosted execution outcome is available. |
| `AGENTS.md` | Included: managed guidance for subsequent repository-agent consumption. | Read completely; optional just-in-time retrieval and scheduled maintenance policy. |
| `CLAUDE.md` | Included: tracked host instruction surface. | Inventoried as a regular tracked file; body not yet read. Do not assume it is a symlink or identical to `AGENTS.md`. |
| `README.md` | Included: public product, installation and operating contract. | Read opening product, host integration, retrieval, workspaces and visualizer sections; later provider/configuration sections remain uninspected. |
| `CONTRIBUTING.md`, `DEVELOPMENT.md` | Included: source-native development and integration contracts. | Inventoried, not yet read; no contributor procedure or development guarantee is inferred. |
| `package.json` | Included: executable entry points, distributed assets, dependency and evaluation-script declarations. | Read completely. Installed dependency internals and published package bytes are not frozen by this source alone. |
| `pnpm-lock.yaml`, `pnpm-workspace.yaml` | Included: dependency/workspace metadata. | Inventoried, not yet read; exact resolved dependency behavior remains unestablished. |
| `scripts` | Included: build and integration delivery via `scripts/copy-visualize-assets.cjs`, `scripts/install-local-integration.mjs`, `scripts/stamp-build-channel.cjs`. | Inventoried and linked through package scripts; bodies not yet inspected. No built-distribution correctness claim. |
| `eslint.config.js`, `tsconfig.client.json`, `tsconfig.eslint.json`, `tsconfig.json`, `vitest.config.ts` | Included: build, lint and test configuration. | Inventoried; bodies not yet inspected or commands executed. No configuration correctness or suite result claim. |
| `.changeset` | Excluded: release-process metadata (`.changeset/README.md`, `.changeset/config.json`). | Deliberate exclusion prevents conclusions about release bookkeeping, not the knowledge loop. |
| `.claude` | Excluded: checkout-local harness settings (`.claude/settings.local.json`). | Deliberate exclusion prevents conclusions about maintainer-specific host permissions. Product integration implementation remains included. |
| `.gitignore`, `.prettierignore`, `.trivyignore` | Excluded: repository tooling ignore policy. | Deliberate exclusion prevents claims about ignored-file, formatting or vulnerability-scanning coverage. Runtime source filtering remains included in `src/agent/openwiki-ignore.ts`. |
| `CHANGELOG.md` | Excluded: historical release narrative. | Deliberate exclusion prevents historical evolution or release-to-release claims; analysis concerns only the pinned implementation. |
| `LICENSE` | Excluded: legal terms. | Deliberate exclusion prevents legal/licensing analysis. |
| `static` | Excluded: marketing screenshots, diagrams and animations. | Deliberate exclusion prevents treating demonstrations or images as runtime/experimental evidence. Executable visualization remains included under `src/visualize`. |

### External dependencies and evidence limits

Native model execution depends on DeepAgents, LangChain/provider adapters and SQLite checkpoint support; host integrations additionally depend on external coding-agent runtimes and MCP transport. Connector ingestion depends on remote services or source repositories. These dependency implementations, live APIs, credentials, generated user wikis and external hosts are outside the frozen repository evidence. The package declares these dependencies, and included code identifies the boundaries; their internals, provider guarantees, live-service availability and host compliance cannot be concluded from this run. SRC-1, `package.json`, `src/agent/index.ts`, `src/ingestion/ingestion.ts`, `src/integrations/core/session-manager.ts`.

The source ships evaluation drivers that use external DeepSWE/Harbor/Codex and model services; those external revisions and executions are not added as sources merely because the driver names them. Their absence prevents empirical conclusions about task performance, longitudinal accuracy, costs and causal effects. It does not prevent inspection of OpenWiki's own driver and artifact-transfer responsibilities. SRC-1, `evals/deepswe/README.md`, `evals/deepswe/openwiki_codex.py`, `evals/ledger/README.md`, `evals/ledger/run/runner.ts`.

No material shipped path was inaccessible during boundary establishment. Uninspected files in included directories are pending source inspection, not access gaps. The whole-system boundary denotes functional scope across production, maintenance, admission and consumption; it is not a claim that every tracked file has been exhaustively reviewed.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/langchain-ai/openwiki` | 7c469e59584bfac3f97f5c32a67604de46805999 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/openwiki-8f502f680f75/related-systems/langchain-ai--openwiki`. Tracked-tree enumeration and HEAD verification. Implementation: package entry points; CLI dispatch; generation routing and planner; page submission and finalization; run-state persistence; host session lifecycle; read-only retrieval and Markdown reload; personal ingestion; managed setup and skill synchronization; LEDGER checkpoint caller and DeepSWE generation/cache/transfer driver. Doctrine/design: opening README sections, complete integration skill, personal prompt portion, repository planner prompt portion, root managed agent instructions, wiki instructions, evaluation README portions and complete scheduled update workflow. | Implementation: [package](https://github.com/langchain-ai/openwiki/blob/7c469e59584bfac3f97f5c32a67604de46805999/package.json), `src/cli/cli.tsx`, `src/agent/index.ts`, `src/agent/repository-runner.ts`, `src/generation/repository-run.ts`, `src/generation/run-state.ts`, `src/integrations/core/session-manager.ts`, `src/integrations/core/retrieval-tools.ts`, `src/retrieval/wiki.ts`, `src/ingestion/ingestion.ts`, `src/ingestion/code-mode.ts`, `src/agent/skills.ts`, `evals/ledger/system/openwiki-system.ts`, `evals/ledger/run/runner.ts`, `evals/deepswe/openwiki_codex.py`. Doctrine/design: [README](https://github.com/langchain-ai/openwiki/blob/7c469e59584bfac3f97f5c32a67604de46805999/README.md), `integrations/openwiki/SKILL.md`, `src/agent/prompts/personal.ts`, `src/agent/repository-prompts.ts`, `AGENTS.md`, `openwiki/INSTRUCTIONS.md`, `evals/ledger/README.md`, `evals/deepswe/README.md`, `.github/workflows/openwiki-update.yml`. | No checkout access gap. Implementation supports source-level operation, not observed execution. Doctrine/design supports intent and contracts, not adherence. External host, dependency and service implementations are not captured; no execution traces or causal experiment results were inspected. Their absence prevents end-to-end reliability, provider/host behavior and empirical benefit claims. Deliberate exclusions and pending inspection are separated in the coverage table. |
