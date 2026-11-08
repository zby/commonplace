---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Antinomia's shipped Obsidian knowledge-management plugin and model-assisted workflows at frozen commit 6fafd01082fbecb2a18803500a1abe70a2bdc9f4."
run-id: AAS-2026-11-08-antinomia-19694628edc2-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "6fafd01082fbecb2a18803500a1abe70a2bdc9f4"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/demartinogiuseppe/antinomia
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/antinomia-df91b67b26b3/related-systems/demartinogiuseppe--antinomia
  revision: "6fafd01082fbecb2a18803500a1abe70a2bdc9f4"
  sha256: null
---

# Antinomia boundary

## Boundary and evidence

Antinomia is in scope as a **memory/knowledge/context-engineering system**: an Obsidian plugin that retains typed notes and uses model calls to classify input, extract material, propose transformations and identify contradictions. Its intended use is reflective personal knowledge work, not an autonomous enclosing agent runtime. The source calls this Personal Tension Management and cautions against treating Hunter proposals as decision-support truths (SRC-1, `README.md`).

> **Antinomia** is an Obsidian plugin for **Personal Tension Management (PTM)** — the in-tension counterpart of Personal Knowledge Management.
> --- `README.md`

The **whole-system** boundary is the shipped plugin, including its interactive drivers, prompts, admission interfaces, note persistence, maintenance, subsequent note consumers and evaluation material. It is not merely the AI transport library. The build enters through `main.ts`; its plugin class loads settings, registers views and commands, and exposes creation and modification operations. Shipped views, modals and helpers are internal callers, not excluded host applications (SRC-1, `esbuild.config.mjs`, `main.ts`).

The initial trace follows the loop across these responsibilities:

- **Produce and admit:** command registration in `main.ts` reaches free input, guided note creation, PDF/YouTube ingestion, elevation and presupposition mapping. Search traced model calls and note writes in all shipped flow files. The presupposition confirmation modal collects new/link/skip decisions before `applyPresuppositionDecisions` creates notes and updates both directions of retained links (SRC-1, `main.ts`, `flows/freeInput.ts`, `flows/pdfIngest.ts`, `flows/youtubeFetch.ts`, `modals/PresuppositionMapModal.ts`, `flows/presuppositionMap.ts`).
- **Persist and maintain:** `createNote` writes Markdown through the vault API; settings use plugin `loadData`/`saveData`. Elevation, resolution, defeated archiving, link maintenance, schema migration/backup/restore and presupposition delete synchronization belong to the target (SRC-1, `main.ts`, `flows/elevation.ts`, `flows/migration.ts`, `flows/presuppositionMap.ts`).
- **Reload and consume:** the frontmatter helper reads Obsidian's metadata cache. Hunter reads retained Markdown bodies and typed metadata, selects open tensions and substrates, constructs a bounded prompt and calls the configured backend. Previously dismissed pairs are read from note frontmatter and filtered from later results. Graph, list, dashboard, audit and dependency-map views are additional shipped consumers (SRC-1, `core/frontmatter.ts`, `flows/hunter.ts`, `views/AntinomiaGraphView.ts`, `views/DashboardView.ts`, `views/AuditVaultView.ts`, `views/PresuppositionsMapView.ts`).
- **Evaluate:** the example-vault flow writes seeded contradictions, noise and a human-readable Hunter measurement key. Tests cover parsers, model detection, frontmatter and selected maintenance flows, including mock-vault presupposition integration. These are evaluation designs and assertions, not evidence that a live run passed (SRC-1, `flows/exampleVault.ts`, `tests/README.md`, `tests/flows/presuppositionMap-integration.test.ts`).

Minimum implementation passages supporting the retained-state loop:

> const file = await this.app.vault.create(path, content);
> --- `main.ts`

> return app.metadataCache.getFileCache(file)?.frontmatter;
> --- `core/frontmatter.ts`

> const isOpenTension = t === TYPE.tension && fm?.status === "open";
> const isSubstrate = t === TYPE.substrate;
> if (isOpenTension || isSubstrate) candidates.push(f);
> --- `flows/hunter.ts`

> fm.presupposes = toWikilinks(mergeUnique(prev, uBasenames), titleMap);
> --- `flows/presuppositionMap.ts`

The frozen evidence is SRC-1 at commit `6fafd01082fbecb2a18803500a1abe70a2bdc9f4`, with applicability cutoff **2026-11-08**. HEAD was checked against the acquired pin. The overall tier is **code-grounded**, supplemented by the repository's own doctrine/design. No target code, tests, examples or model requests were executed.

### Tracked top-level coverage

“Included” means within the functional evidence boundary; the inspection column distinguishes initial tracing from material available for later detailed inspection. No material shipped state-loop path is deliberately excluded.

| Top-level tracked path | Treatment and role | Initial inspection and limit |
|---|---|---|
| `main.ts` | Included: plugin entry, settings UI, command/view registration, persistence and maintenance drivers | Inspected imports, command and persistence search results, startup, settings reload/save and note creation. Remaining method bodies are available, not an access gap. |
| `ai/` | Included: `callAI.ts`, `detectModel.ts`, `parseResponse.ts`, `pingBackend.ts`, `notifyUsage.ts`, `prompts.ts`; transport, adaptation, parsing, connectivity, feedback and shipped instructions | Read transport API/routing and initial prompt definitions; searched exported operations and call consumers. Remaining internals and prompt bodies are available for later inspection. |
| `core/` | Included: `settings.ts`, `types.ts`, `constants.ts`, `templates.ts`, `frontmatter.ts`, `utils.ts`, `aiFriction.ts`, `hoverBus.ts`; retained schema, templates, controls and UI support | Read settings/defaults and cached-frontmatter reader; searched helpers, template constructors and friction prompt surface. Detailed schemas and remaining helpers are available. |
| `flows/` | Included: `freeInput.ts`, `titleProposal.ts`, `pdfIngest.ts`, `youtubeFetch.ts`, `hunter.ts`, `elevation.ts`, `presupposti.ts`, `presuppositionMap.ts`, `migration.ts`, `exampleVault.ts`; production, maintenance, reuse and seeded evaluation | Traced calls and persistence across all files; read Hunter selection/model/admission/dismissal path, presupposition decision persistence and example evaluation key. Other bodies remain available. |
| `modals/` | Included: guided `NewTensionModal.ts`/`NewSubstrateModal.ts`, `FreeInputModal.ts`, classification/title/elevation confirmation, PDF selectors/progress/`ConceptsPreviewModal.ts`, presupposition mapping/impact, migration, profile/privacy, onboarding/tutorial/guidance and `FrictionCard.ts` | Searched action handlers and inspected presupposition confirmation/acceptance. Other UI and instructional text remains available, not excluded. |
| `views/` | Included: `HunterResultsView.ts`, `DismissedPairsView.ts`, `OpenTensionsView.ts`, substrate/principle/defeated lists, `UnclassifiedNotesView.ts`, `DashboardView.ts`, `AuditVaultView.ts`, `AntinomiaGraphView.ts`, `PresuppositionsMapView.ts`, `OnboardingChecklistView.ts` | Traced retained-note consumers by search; read Hunter result rendering/dismissal and action dispatch surface. Remaining rendering and refresh details remain available. |
| `helpers/` | Included: `renderAntinomiaNav.ts`, `renderNoteCard.ts`, `renderTensionContext.ts`, `withLoadingButton.ts`; shared creation/navigation/context UI | Searched exports, frontmatter reads and navigation-to-flow handlers. Remaining presentation details available. |
| `tests/` | Included: `ai/`, `core/`, `flows/`, fixtures, mocks and setup; regression/evaluation design | Read suite README and presupposition mock-vault integration setup/assertions; enumerated other tests and fixtures. No execution or live efficacy conclusion. |
| `README.md` | Included: intended use, workflow, limitations and installation doctrine | Read completely; source claims are not observed deployment evidence. |
| `BETA-INSTALL.md`, `CHANGELOG.md` | Included: operator/setup instructions and attributed change history | Available, not yet inspected; no version-history or installation-success claim made. |
| `manifest.json`, `package.json` | Included: plugin identity, host compatibility declaration, entry/build/test scripts and dependencies | Read completely; compatibility declaration is not a platform test result. |
| `package-lock.json`, `versions.json` | Included: dependency and release metadata | Available, not yet inspected; no resolved-dependency security or release-history conclusion. |
| `esbuild.config.mjs` | Included: build entry and host externalization | Read entry/build configuration through production-output comments; remaining copy/watch steps available. |
| `eslint.config.js`, `eslint.async.config.js`, `tsconfig.json`, `vitest.config.ts`, `.github/` | Included: static checks, compilation, test runner and `.github/workflows/test.yml` CI specification | Enumerated and available, not yet inspected; no CI-pass or static-check conclusion. |
| `package-release.ps1`, `scripts/` | Included: release packaging and development hooks (`disable-claude-attribution.py`, `install-hook.sh`, `prepare-commit-msg`) | Enumerated and available, not yet inspected; no package reproducibility or hook-behavior conclusion. |
| `.gitignore` | Included: development exclusion metadata | Available, not yet inspected; no claim about ignored local artifacts. |
| `styles.css`, `assets/` | Included: presentation and `assets/nebula.jpg` graph background | Enumerated, available; not visually inspected. No aesthetic, accessibility or rendering-fidelity assessment. |
| `CITATION.cff`, `LICENSE` | Included: attribution and licensing metadata | Enumerated, available; no independent legal assessment. |

### External dependencies and excluded evidence

Obsidian's vault, metadata cache, workspace and plugin storage APIs are external runtime dependencies. The plugin's calls to them are included; Obsidian implementation and a real user vault are not frozen. This prevents conclusions about host atomicity, cache timing guarantees, synchronization durability or actual user outcomes. `main.ts` and `core/frontmatter.ts` establish the dependency, not those guarantees (SRC-1).

Configured Anthropic/OpenAI-compatible model services, local servers and their model weights are outside the frozen source. `ai/callAI.ts` implements request routing; it does not freeze providers or establish model accuracy, privacy enforcement or operational availability. YouTube/transcript services and PDF host facilities are dependencies reached by the shipped ingest flows, not additional evidence sources (SRC-1, `ai/callAI.ts`, `flows/youtubeFetch.ts`, `flows/pdfIngest.ts`).

Installed dependency implementations, built release binaries, live Obsidian desktop/mobile behavior and actual model execution traces are not supplied as frozen run evidence. This prevents claims of successful installation, end-to-end correctness, measured contradiction-detection quality or causal improvement. Repository tests and response fixtures remain inspectable source material; their existence does not remove these limits. Linked external papers, newsletters, provider documentation and release pages are not registered sources and were not followed. This prevents treating their contents as evidence for this run. Available-but-uninspected repository files in the coverage table are not access gaps and remain eligible for later inspection at this same pin.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/demartinogiuseppe/antinomia` | 6fafd01082fbecb2a18803500a1abe70a2bdc9f4 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/antinomia-df91b67b26b3/related-systems/demartinogiuseppe--antinomia`. Implementation: tracked tree, build entry, `main.ts` startup/settings/createNote and command/persistence searches; `ai/callAI.ts` API/routing; `core/settings.ts`, `core/frontmatter.ts`; flow/view/modal/helper state-loop searches; Hunter flow, presupposition persistence/confirmation, Hunter result UI, presupposition mock integration test. Doctrine/design: complete `README.md`, `tests/README.md`, metadata, initial `ai/prompts.ts` definitions and example-vault evaluation key. | Implementation: [plugin entry](https://github.com/demartinogiuseppe/antinomia/blob/6fafd01082fbecb2a18803500a1abe70a2bdc9f4/main.ts), [Hunter loop](https://github.com/demartinogiuseppe/antinomia/blob/6fafd01082fbecb2a18803500a1abe70a2bdc9f4/flows/hunter.ts), [presupposition persistence](https://github.com/demartinogiuseppe/antinomia/blob/6fafd01082fbecb2a18803500a1abe70a2bdc9f4/flows/presuppositionMap.ts). Doctrine/design: [README](https://github.com/demartinogiuseppe/antinomia/blob/6fafd01082fbecb2a18803500a1abe70a2bdc9f4/README.md), [prompts](https://github.com/demartinogiuseppe/antinomia/blob/6fafd01082fbecb2a18803500a1abe70a2bdc9f4/ai/prompts.ts), [seeded evaluation key](https://github.com/demartinogiuseppe/antinomia/blob/6fafd01082fbecb2a18803500a1abe70a2bdc9f4/flows/exampleVault.ts). | No repository access gap identified. Implementation evidence is static source inspection, not observed execution. Doctrine/design is attributed intent, not efficacy evidence. External host/provider implementations, user vaults, deployment artifacts and live run results are not frozen; this prevents deployment, durability, accuracy and causal-effect conclusions. |
