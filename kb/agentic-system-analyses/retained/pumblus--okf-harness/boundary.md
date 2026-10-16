---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "OKF Harness's shipped agent-guided wiki maintenance and retrieval system at commit 0dd4f806c454a68088c5a3e64b4cbebbe2c216be."
run-id: AAS-2026-10-15-okf-harness-6bf5507fbdbf-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "0dd4f806c454a68088c5a3e64b4cbebbe2c216be"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/pumblus/okf-harness
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/okf-harness-6bf5507fbdbf/related-systems/pumblus--okf-harness
  revision: "0dd4f806c454a68088c5a3e64b4cbebbe2c216be"
  sha256: null
---

# OKF Harness boundary

## Boundary and evidence

OKF Harness is in scope as a **memory/knowledge/context-engineering system**, not an enclosing model runtime. Its intended use is local, agent-maintained, OKF-compatible wikis: register source material, synthesize and maintain wiki pages, then supply bounded wiki evidence for later answers. The **whole-system** boundary includes the shipped agent instructions and host integrations as well as the deterministic CLI and core library. It does not stop at the library API. The host agent performs the model-dependent synthesis and judgment specified by the shipped workflows; the CLI supplies persistence, planning, validation and retrieval. SRC-1: `README.md`, `packages/agent-pack/templates/okf-harness/SKILL.md`, `packages/agent-pack/templates/okf-harness/references/ingest.md`, `packages/cli/src/index.ts`.

> The ingest plan is metadata-level guidance. It returns a recommended reference path, candidate concepts, an optional suggested new concept, a next step, and an agent checklist; it does not read source bodies, summarize content, extract claims, or synthesize wiki pages.
> --- `packages/agent-pack/templates/okf-harness/references/ingest.md`

> Otherwise, read the registered source material, update only bounded wiki files, run check, and finish with the registered source ID, changed wiki paths, check status, and unresolved questions.
> --- `packages/agent-pack/templates/okf-harness/references/ingest.md`

### Functional coverage and entry-point trace

The inspected paths establish a shipped production-to-consumption loop, rather than only a returning retrieval function:

- **Host entry and initialization.** Native and portable skills route requests through the setup launcher. The setup implementation resolves a workspace, reads its runtime pin and delegates through `npx` to that runtime. The CLI entry calls `runCli`, whose registered commands include initialization, workspace inspection, source operations, retrieval, recovery and agent guidance installation. Initialization calls `initWorkspace`, optionally installs agent adapters, and initializes Git recovery. These shipped callers are included, not treated as external applications. SRC-1: `packages/native-integration/skills/okf-harness/SKILL.md`, `plugins/agent-plugins/okf-harness/skills/okf-harness/SKILL.md`, `packages/setup/src/index.ts`, `packages/cli/src/main.ts`, `packages/cli/src/index.ts`, `packages/cli/src/commands/init.ts`.
- **Retained state and admission.** Source commands call core registration and ingest planning. Local-file registration reads bytes, hashes them, writes an immutable raw copy with exclusive creation, and appends a manifest entry. URL registration retains metadata rather than downloading the page body. Wiki synthesis is assigned to the agent, not performed by these commands. SRC-1: `packages/cli/src/commands/source.ts`, `packages/core/src/source/index.ts`, `packages/agent-pack/templates/okf-harness/references/ingest.md`.
- **Maintenance and recovery.** Shipped reconciliation instructions require reading both source revisions, editing affected wiki claims, checking the result, then acknowledging the exact revision edge through the CLI. The check pipeline composes lineage, lint, currency and conformance. Recovery code supplies initialization, judgment-bearing checkpoints, history and restoration using Git. These are included maintenance responsibilities, not merely documentation adjacent to retrieval. SRC-1: `packages/agent-pack/templates/okf-harness/references/reconcile.md`, `packages/agent-pack/templates/okf-harness/references/check.md`, `packages/cli/src/commands/source.ts`, `packages/cli/src/commands/workspace.ts`, `packages/core/src/check/index.ts`, `packages/core/src/recovery/index.ts`.
- **Reload and later consumption.** The workspace snapshot reads configuration, wiki concepts, manifest and reconciliation ledger. Retrieval commands call `planEvidenceBrief`, `searchWorkspace`, `readWorkspaceDocument` and graph generation. The evidence implementation selects wiki excerpts and emits limits, candidates, warnings and withheld-evidence information. The answer instructions assign sufficiency and conflict judgment to the agent, with at most one automatic cue-following read. They also allow an explicitly accepted, limited wiki write-back. SRC-1: `packages/core/src/lineage/index.ts`, `packages/cli/src/commands/query.ts`, `packages/core/src/evidence/index.ts`, `packages/agent-pack/templates/okf-harness/references/answer.md`.
- **Evaluation surfaces.** The example workspace supplies synthetic retained sources and wiki pages. The inspected maintenance-loop test scripts source loss, restoration, revision registration, reconciliation and subsequent evidence reads. CI declares tests across operating systems and Node versions. These are source-level fixtures and test assertions, not observed test outcomes or evidence of model compliance. SRC-1: `examples/ai-research-workspace/README.md`, `packages/cli/test/maintenance-loop.test.ts`, `.github/workflows/ci.yml`.

The division between executable machinery and delivered agent obligations matters to this boundary:

> Judge sufficiency and conflicts yourself. Evidence sufficiency and conflict judgment belong to the agent, not the CLI.
> --- `packages/agent-pack/templates/okf-harness/references/answer.md`

> Accepted ceiling: an Agent that skips the disclosure or the lineage prose is not caught by anything. Harness can prove the obligation was delivered, never that it was honored.
> --- `packages/agent-pack/templates/okf-harness/references/answer.md`

### Repository coverage

The tracked top-level tree was inventoried at the frozen commit. Every top-level tracked item is classified below. “Included” sets functional scope; it does not assert a line-by-line audit. Material loop entry points and their state-producing and state-consuming callers were inspected as listed above. Additional available files not initially inspected remain available under SRC-1, not access gaps. Deliberate exclusions below concern development, distribution presentation or duplicated prose, not an omitted wiki maintenance responsibility.

| Top-level tracked item | Coverage | Material paths, role and initial inspection | Exclusion or inspection limit and conclusion prevented |
|---|---|---|---|
| `.agents/` | Included | `plugins/marketplace.json`: Codex distribution discovery; tree inventoried, manifest contents not initially inspected. | No claim of marketplace resolution success. |
| `.claude-plugin/` | Included | `marketplace.json`: Claude distribution discovery; tree inventoried, manifest contents not initially inspected. | No claim of marketplace resolution success. |
| `.gitattributes` | Excluded | Repository file handling. | No audit of checkout attribute behavior. |
| `.github/` | Included for evaluation; issue templates excluded | Inspected `workflows/ci.yml`; templates and pull-request form are contribution administration. | CI configuration establishes intended checks, not passing runs; no issue-triage assessment. |
| `.gitignore` | Excluded | Repository ignore rules. | No confidentiality or ignored-file audit. |
| `AGENTS.md`, `CLAUDE.md` | Excluded | Instructions for developing this repository, distinct from shipped workspace guidance under packages and plugins. | No account of the project's own development-agent compliance. |
| `CONTEXT.md`, `CONTRIBUTING.md` | Excluded | Project glossary and contributor process. | No reconstruction of contributor operations from these files. |
| `LICENSE` | Excluded | Legal terms. | No licensing assessment. |
| `README.md` | Included | Inspected product purpose, architecture sketch, supported surfaces and user loop. | Declared operation only where not traced into implementation. |
| `README.zh-CN.md` | Excluded | Alternate-language product introduction. | No translation-parity assessment. |
| `SECURITY.md` | Included | Security contract available but not initially inspected. | No security-policy or security-completeness conclusion at this stage. |
| `biome.json` | Excluded | Development formatting and lint configuration. | No formatter-policy audit. |
| `docs/` | Included for product contracts; contributor and website planning excluded | `CLI.md`, `WORKFLOWS.md`, `AGENT-PLUGIN.md`, `adr/`, `zh-CN/` product counterparts remain in scope. Initially inventoried; operational guidance was inspected at its shipped template and skill paths instead. `agents/` and `website/` concern repository development and site planning. | Product docs not initially read are not access gaps. No history-of-design, translation-parity or contributor-process conclusion. |
| `examples/` | Included | `ai-research-workspace/`: configuration, manifest, raw source, wiki references/topics/index/log and agent pointers; inspected its README and inventoried the state files. | Synthetic example, not evidence of a real user's knowledge or an observed answer. |
| `install.ps1`, `install.sh` | Included | Installer entry surfaces, inventoried but implementation not initially inspected; setup and launcher implementation inspected under `packages/setup/`. | No assertion that installers work on actual hosts. |
| `llms-full.txt`, `llms.txt` | Excluded | Generated documentation presentation. | No generated-document freshness or parity assessment. |
| `package.json` | Included | Inspected package metadata, Node requirement and build/test entry scripts. | Metadata does not establish published artifact behavior. |
| `packages/` | Included | `core/src/` persistence, snapshots, validation, retrieval and recovery; `cli/src/` shipped driver and command consumers; `agent-pack/templates/` maintenance and answer instructions and `src/index.ts` rendering/installation; `setup/src/index.ts` host setup and pinned-runtime launcher; `native-integration/` skill packaging and OpenCode synchronization. Inspected the paths cited in the loop trace, adapter rendering/installation, integration profiles, native package metadata and OpenCode implementation. `*/test/`, golden guidance and fixtures are included evaluation surfaces; inspected the CLI maintenance-loop test. | No package, host, test or model execution was performed. Unread implementation details and tests remain available for later jobs. |
| `plugins/` | Included | `agent-plugins/okf-harness/` portable/Codex artifact and `claude/okf-harness/` native Claude artifact, each with entry skill and setup/discovery/repair references. Inspected both entry skills and inventoried references and manifests. | No assumption that the different host distributions deliver identical guidance or are actually loaded. |
| `pnpm-lock.yaml`, `pnpm-workspace.yaml` | Included | Dependency resolution and workspace package topology, inventoried but not initially read. | No dependency or supply-chain audit. |
| `scripts/` | Included for evaluation/distribution; site presentation excluded | `smoke-marketplace-plugins.mjs`, `smoke-npm-tarballs.mjs` and its declaration file: distribution checks; `build-llms.mjs`: documentation generation; `build-site.mjs`: website build. Inventoried; root script invocations inspected in `package.json`. | No smoke-test result or published-site parity claim. |
| `site/` | Excluded | `src/index.html`, `src/_redirects`: public landing page and routing. | No live-site, deployment or browser-UI conclusion. The local graph report remains included under core/CLI. |
| `skills/` | Included | Inspected `okf-harness/SKILL.md`, the Hermes host entrypoint routing to launcher, maintenance and evidence commands. | Host execution and adherence remain unobserved. |
| `tsconfig.base.json`, `tsconfig.json` | Excluded | Development compiler configuration. | No compiler-configuration audit. |
| `vendor/` | Included | `agent-plugins/1.0.0/SOURCE.md` and `plugin.schema.json`: vendored distribution schema/provenance, inventoried but not initially inspected. | No independent assertion of schema compliance or upstream behavior. |
| `vitest.config.ts` | Included | Evaluation configuration, inventoried but not initially read. | No test-discovery completeness claim. |

### External dependencies and evidence limits

The enclosing agents, model providers and their context/session machinery are external. OKF Harness ships host-specific skills and integration code, which are included; it does not thereby own those hosts' model calls, scheduling, permissions or instruction adherence. The supported integration profiles name Claude Code, Codex, OpenCode, Pi, Hermes and OpenClaw. SRC-1: `packages/agent-pack/src/integrations.ts`, `packages/native-integration/package.json`, `packages/native-integration/src/opencode.ts`, `skills/okf-harness/SKILL.md`. No host or provider source or execution trace was frozen, so conclusions about actual host behavior, effective prompt loading and answer quality are prevented.

Node, npm/npx and downloaded packages are execution dependencies; Git provides the recovery substrate. Their implementation and the moving registry contents are not frozen sources. The source shows intended runtime-pin delegation, not proof that a registry-served artifact matches this checkout. SRC-1: `package.json`, `packages/setup/src/index.ts`, `packages/core/src/recovery/index.ts`. Upstream LLM Wiki and OKF materials linked by the README are design attributions, not separately acquired evidence. No independent upstream-specification conformance conclusion follows from those links. SRC-1: `README.md`.

The cutoff is **2026-10-15**, the supplied run date. The sole frozen source is repository commit **0dd4f806c454a68088c5a3e64b4cbebbe2c216be**; its checkout HEAD was verified and its status was clean. The overall tier is **code-grounded** because executable entry points and persistence/reload/consumption paths were inspected alongside agent instructions. No target code, tests, examples, installers or model services were executed. There are no established source-access gaps; uninspected available files are inspection limits, and absent execution evidence prevents claims about observed success or causal effects.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/pumblus/okf-harness` | 0dd4f806c454a68088c5a3e64b4cbebbe2c216be | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/okf-harness-6bf5507fbdbf/related-systems/pumblus--okf-harness`. Implementation: tracked-tree inventory; `package.json`; CLI `src/main.ts`, `src/index.ts`, command source/init/workspace handlers and query registration; core workspace initialization/status, source registration, snapshot loading, check pipeline, evidence planning and recovery; agent-pack rendering/installation and integration profiles; setup/launcher delegation; native package metadata and OpenCode skill synchronization; CLI maintenance-loop test and CI workflow as executable evaluation definitions. Doctrine/design: `README.md`; agent-pack workspace skill and ingest/reconcile/check/answer references; portable and Claude plugin entry skills; native and Hermes entry skills; example workspace README. | Implementation: [CLI driver](https://github.com/pumblus/okf-harness/blob/0dd4f806c454a68088c5a3e64b4cbebbe2c216be/packages/cli/src/index.ts), [source persistence](https://github.com/pumblus/okf-harness/blob/0dd4f806c454a68088c5a3e64b4cbebbe2c216be/packages/core/src/source/index.ts), [snapshot reload](https://github.com/pumblus/okf-harness/blob/0dd4f806c454a68088c5a3e64b4cbebbe2c216be/packages/core/src/lineage/index.ts), [evidence consumption](https://github.com/pumblus/okf-harness/blob/0dd4f806c454a68088c5a3e64b4cbebbe2c216be/packages/core/src/evidence/index.ts), [launcher](https://github.com/pumblus/okf-harness/blob/0dd4f806c454a68088c5a3e64b4cbebbe2c216be/packages/setup/src/index.ts). Doctrine/design: [ingest obligations](https://github.com/pumblus/okf-harness/blob/0dd4f806c454a68088c5a3e64b4cbebbe2c216be/packages/agent-pack/templates/okf-harness/references/ingest.md), [answer obligations](https://github.com/pumblus/okf-harness/blob/0dd4f806c454a68088c5a3e64b4cbebbe2c216be/packages/agent-pack/templates/okf-harness/references/answer.md). | No known access gap in the frozen repository. Initial inspection is selective, not an allowlist. Tests and examples supply implementation and intended checks, not observed runs. External hosts, providers, registry artifacts and upstream specifications were not acquired; actual execution, model adherence, answer quality and causal improvement are not established. |
