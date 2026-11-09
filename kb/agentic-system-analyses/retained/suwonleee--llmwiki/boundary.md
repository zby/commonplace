---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "llmwiki's shipped project-wiki engine, model-facing maintenance skills, capture and retrieval integrations at commit e6be788bdfd969c3695f839a5d6b5752bb233cfc."
run-id: AAS-2026-11-08-llmwiki-7f7e35008c0f-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "e6be788bdfd969c3695f839a5d6b5752bb233cfc"
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/suwonleee/llmwiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/llmwiki-43812a7c978d/related-systems/suwonleee--llmwiki
  revision: "e6be788bdfd969c3695f839a5d6b5752bb233cfc"
  sha256: null
---

# llmwiki boundary

## Boundary and evidence

This run examines llmwiki as a project-knowledge system that preserves coding-session material in a wiki and supplies it to later model sessions. It includes the Bun/TypeScript engine, its shipped callers, capture daemon, installation and plugin wiring, model-facing skills, optional engine-launched generation, maintenance and evaluation surfaces. It is not just a search library or the API behind its hooks. The intended use is an account of how these shipped components produce, maintain, admit and consume retained knowledge, not a recommendation for Commonplace.

The classification is **memory/knowledge/context-engineering system**, with a **whole-system** functional boundary. The source describes the cross-session purpose explicitly (SRC-1, `README.md`):

> llmwiki turns coding sessions into a wiki in `docs/wiki/`. Claude Code, Codex and OpenCode can share it, retrieve relevant context in later sessions, and quiz you on past decisions.
> --- `README.md`

The boundary includes model-executed instructions as well as deterministic code. In the normal documented workflow, the host model performs substantive wiki authorship under the save/deep skills; the CLI supplies extraction, state transitions and checks. Thus the absence of a default engine model subprocess does not make the target independent of model operation. The source's authorship contract is explicit (SRC-1, `skill/wiki-save.md`):

> - The human doesn't hand-write the wiki. **The LLM writes all categories** — *summarizing* what the human decided/realized, grounded in the transcript. **Never *fabricate***: `decision`/`insight` hold only what *the human expressed*. Test: **useful to the next session?** No filler.
> --- `skill/wiki-save.md`

Initial entry-point tracing covered the package binary into `src/cli.ts`; hook registration through the three shell wrappers into `src/hook-cli.ts`; its enrollment gate and calls to `buildContext`, `buildTurnContext` and edit-rule assembly; daemon routing/materialization into capture enqueue; the canonical save/deep procedures into extract, watermark, indexing and review commands; and OpenCode/OpenClaw callers into CLI context consumption. The plugin manifests point to `skills/`, and `src/plugin/build-assets.ts` renders those assets from `skill/`. These are shipped paths inside the target, not excluded applications merely because they call engine functions (SRC-1, `package.json`, `src/cli.ts`, `hooks/hooks.json`, `hooks/sessionstart-inject.sh`, `hooks/userpromptsubmit-inject.sh`, `hooks/pretooluse-inject.sh`, `src/hook-cli.ts`, `src/daemon/watch.ts`, `skill/wiki-save.md`, `skill/wiki-deep.md`, `.claude-plugin/plugin.json`, `.codex-plugin/plugin.json`, `src/plugin/build-assets.ts`, `adapters/opencode/llmwiki.ts`, `adapters/openclaw/llmwiki.ts`).

Both the ordinary warm maintenance workflow and the optional unattended path remain inside this boundary. `daemon/autoupdate-all.sh` dispatches `autoupdate` over pending repositories; `daemon/autoupdate-schedule.sh` supplies the opt-in scheduling surface. `src/engine/autoupdate.ts` has direction-review routing and gated non-direction publication. These paths must not be erased by treating the ordinary skill's prohibition on unattended backlog extraction as proof that no unattended writer ships. The optional provider boundary is distinct from the host session model (SRC-1, the preceding paths and `src/engine/claude.ts`):

> //   There is NO default. Unset or empty → no subprocess is launched at all, and callers get a
> //   deterministic "unavailable" marker. Generative passes are strictly opt-in because they are
> //   the only thing in this engine that sends your session content to another program.
> --- `src/engine/claude.ts`

The state loop includes Markdown persistence, capture/watermark state, rebuildable SQLite indexes, read-time context and rule eligibility, feedback and subsequent maintenance. Initial implementation inspection reached indexing imports and source classification in `src/engine/db.ts`, cold-start page reads in `src/engine/context.ts`, bounded turn assembly in `src/engine/turncontext.ts`, and the rule eligibility predicate in `src/engine/knowledge-policy.ts`; save/deep instructions specify the associated human/model maintenance procedure. These establish the functional boundary, not an exhaustive audit of each engine module (SRC-1, these paths and `skill/wiki-save.md`, `skill/wiki-deep.md`).

### Tracked top-level coverage

Every tracked top-level file or directory is classified below. **Included** means within the analysis's functional/evidence scope, not that every line has already been inspected. “Tree only” and “not yet inspected” are inspection limits, not unavailable evidence. All rows refer to SRC-1 at the reviewed commit. No material shipped state-loop responsibility is deliberately excluded.

| Top-level path(s) | Classification | Material paths and role | Initial inspection and conclusion limits |
| --- | --- | --- | --- |
| `.claude-plugin/` | Included | `plugin.json`, `marketplace.json`: Claude distribution and skill discovery | Plugin manifest inspected; marketplace file tree only. No marketplace acceptance established. |
| `.codex-plugin/` | Included | `plugin.json`: Codex skill and interface declaration | Manifest inspected; external loader behavior not established. |
| `hooks/` | Included | `hooks.json`, `sessionstart-inject.sh`, `userpromptsubmit-inject.sh`, `pretooluse-inject.sh`: automatic consumption and edit-rule entry points | Registration read; wrapper dispatch searched; lightweight hook implementation read. No live delivery test. |
| `src/` | Included | `cli.ts`, `hook-cli.ts`, `commands/`; `daemon/watch.ts`, `daemon/wire*.ts`; `engine/sources/`, `capture.ts`, `update.ts`, `extract.ts`; `engine/autoupdate.ts`, `consolidate.ts`, `review.ts`, `repo-write.ts`; `engine/db.ts`, `schema.sql`, `project-state.ts`; `engine/context.ts`, `turncontext.ts`, `edit-rules.ts`, `knowledge-policy.ts`; feedback, quiz, tiering and maintenance modules; `plugin/`, `dev/` | Entry points and representative producer/admission/consumer code inspected as described above; remaining implementation details are available for later inspection, not access gaps. No exhaustive correctness or security claim. |
| `skill/` | Included | `wiki-save.md`, `wiki-deep.md`, `wiki-ask.md`, `wiki-doctor.md`, `wiki-quiz.md`, and `ref/` writing, citation, consolidation, review, distillation and feedback instructions | Save/deep read fully; references and other skills inventoried but not yet read. Their detailed policies are not inferred from filenames. |
| `skills/` | Included | Five `wiki-*/SKILL.md` assets and `agents/openai.yaml` policies: distributed model-facing consumers | Manifest references and generator inspected; generated bodies not independently compared. No drift-free claim. |
| `adapters/` | Included | `opencode/llmwiki.ts`, `openclaw/llmwiki.ts`; Codex hooks example; Hermes/Orca guides; distribution guide and plugin/package examples | OpenClaw code read and OpenCode context/close-out callers traced. Other adapters inventoried, not yet inspected in detail. No uniform cross-host support claim. |
| `daemon/` | Included | `install.sh`, `autoupdate-all.sh`, `autoupdate-schedule.sh`, `README.md`: service installation, queue capture, optional unattended generation | README inspected in part, all-repository runner read, scheduler entry/configuration inspected; setup's installer call traced. No platform installation success inferred. |
| `setup.sh` | Included | Installation/uninstallation caller for daemon, launcher and harness wiring | Dispatch sites searched. Not an observed install or full shell audit. |
| `setup_text.md` | Included | Model-directed setup procedure | Tree only; no claim about its detailed instructions. |
| `configs/` | Included | `default.toml.example`: alternative convention configuration | Tree only; exact option semantics not yet inspected. |
| `llmwiki.config.example.toml` | Included | Project convention example | Tree only; no claim of equivalence with defaults. |
| `evals/` | Included | `okf-consumer/run.ts`, `provenance.ts`, fixtures and aggregate result JSON: retrieval and source-resolution diagnostics | Diagnostic README and retrieval runner read; result files and provenance runner not yet inspected. No new experiment, model-accuracy estimate or causal efficacy conclusion. |
| `tests/` | Included | Capture, state, admission, retrieval, maintenance, wiring and release tests; `fresh-public-harness-loop.test.ts`, fixtures and support helpers | Inventory and harness-loop imports/test declarations searched. Test code is executable specification, not evidence that tests passed. |
| `reference/` | Included | Installation flow, release gates, support contract and usability-study protocol/schema/validator inputs | Tree only; no completed usability or release qualification inferred. |
| `readmes/` | Included | User guides/translations, `OKF-CONSUMPTION.md`, evidence-guidance result JSON | Tree only; no unseen measurements adopted as findings. |
| `examples/` | Included | Sample-wiki pages, current-state, overview, log and example guides | Tree only; illustrative content is not evidence of a real user's retained state. |
| `README.md`, `ARCHITECTURE.md` | Included | Purpose, workflow and architecture doctrine | Read fully; declared contracts remain distinct from implementation and observed operation. |
| `PLUGIN.md`, `PLUGIN_SUBMISSION.md` | Included | Plugin disclosure and distribution contracts | Tree only; no external approval or permission-safety conclusion. |
| `CONTRIBUTING.md`, `SUPPORT.md`, `PRIVACY.md`, `TERMS.md` | Included | Contributor, support and operator-facing contracts | Tree only; no enforcement or legal-compliance claim. |
| `package.json` | Included | CLI binary, scripts, runtime requirement and development dependency declaration | Read fully; no runtime compatibility test. |
| `.github/` | Included | `workflows/ci.yml`: shipped automated checks | Tree only; no CI execution or result inspected. |
| `bun.lock`, `bunfig.toml`, `tsconfig.json` | Included | Dependency resolution, Bun and TypeScript development configuration | Tree only; no complete dependency/configuration audit. |
| `.gitattributes`, `.gitignore` | Included | Repository storage and ignored-state conventions | Tree only; no private-file exclusion guarantee. |
| `assets/` | Excluded | Banner, plugin icons and social-preview artwork | Deliberately excluded non-operational presentation; prevents visual-branding/accessibility assessment, not knowledge-loop analysis. |
| `LICENSE` | Excluded | License text | Deliberately excluded legal assessment; no legal interpretation supplied. |

### Dependencies and evidence limits

The frozen source is the acquired Git repository at **e6be788bdfd969c3695f839a5d6b5752bb233cfc**. Its checkout HEAD matched that revision and its working tree was clean at inspection. The cutoff is **2026-11-08**; later changes and moving documentation links are outside the evidence. The overall tier is **code-grounded**, with source-native doctrine separately identified. No target code, tests, examples, provider calls or setup procedures were executed.

External dependencies include Bun and its SQLite implementation, Git, host-agent runtimes and their transcript formats/hook APIs, OS service managers where used, and an optional configured model CLI/provider. Host runtime implementations, provider behavior, actual user transcript stores and project wikis are not captured sources. Consequently this run cannot establish model compliance with the skills, actual task improvement, data retention on a user's machine, live hook compatibility or successful deployment across platforms. The shipped adapters and installation code remain included; their hosts' internal scheduling and permissions are not attributed to llmwiki (SRC-1, `package.json`, `ARCHITECTURE.md`, `src/hook-cli.ts`, `src/daemon/watch.ts`, `src/engine/claude.ts`, `adapters/openclaw/llmwiki.ts`).

Evaluation artifacts are within scope, but their claims retain their conditions. The inspected diagnostic explicitly bounds what it can support (SRC-1, `evals/okf-consumer/README.md`):

> These frozen synthetic inputs check metadata retrieval and source-ID resolution. They do not
> estimate model accuracy, coding success or external-user productivity. Keep fixture labels
> unchanged when comparing engines. Reports include the fixture SHA-256.
> --- `evals/okf-consumer/README.md`

There is no repository access gap identified. Files marked not yet inspected are available evidence, not missing evidence. There is no newly observed run or causal experiment in this boundary declaration; source comments and reported measurements are not upgraded to either.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/suwonleee/llmwiki` | e6be788bdfd969c3695f839a5d6b5752bb233cfc | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/llmwiki-43812a7c978d/related-systems/suwonleee--llmwiki`. Implementation: package/plugin entry points; CLI extraction, watermark and generation dispatch; hook implementation and wrapper dispatch; daemon route/materialization/enqueue; optional unattended runner/scheduler; OpenCode/OpenClaw context callers; asset generator; portions of DB, cold-start/turn context and admission code; retrieval diagnostic runner. Doctrine/design: README, architecture, full canonical save/deep instructions, diagnostic README and part of daemon README. Reported operation: bounded diagnostic results/limits in its README and attributed observations in provider/adapter comments. The coverage table separates these reads from inventory-only paths. | Implementation: [hook dispatch](https://github.com/suwonleee/llmwiki/blob/e6be788bdfd969c3695f839a5d6b5752bb233cfc/src/hook-cli.ts), [capture caller](https://github.com/suwonleee/llmwiki/blob/e6be788bdfd969c3695f839a5d6b5752bb233cfc/src/daemon/watch.ts), [optional writer](https://github.com/suwonleee/llmwiki/blob/e6be788bdfd969c3695f839a5d6b5752bb233cfc/src/engine/autoupdate.ts), [retrieval diagnostic](https://github.com/suwonleee/llmwiki/blob/e6be788bdfd969c3695f839a5d6b5752bb233cfc/evals/okf-consumer/run.ts). Doctrine/design: [architecture](https://github.com/suwonleee/llmwiki/blob/e6be788bdfd969c3695f839a5d6b5752bb233cfc/ARCHITECTURE.md), [save procedure](https://github.com/suwonleee/llmwiki/blob/e6be788bdfd969c3695f839a5d6b5752bb233cfc/skill/wiki-save.md), [deep procedure](https://github.com/suwonleee/llmwiki/blob/e6be788bdfd969c3695f839a5d6b5752bb233cfc/skill/wiki-deep.md). Reported operation: [diagnostic account](https://github.com/suwonleee/llmwiki/blob/e6be788bdfd969c3695f839a5d6b5752bb233cfc/evals/okf-consumer/README.md), [provider commentary](https://github.com/suwonleee/llmwiki/blob/e6be788bdfd969c3695f839a5d6b5752bb233cfc/src/engine/claude.ts). | No checkout access gap. Host/provider internals and live user state are outside the capture, preventing end-to-end deployment, compliance and efficacy conclusions. Initial inspection is selective, not an allowlist; all repository paths at this commit remain registered evidence. Reported observations have not been independently reproduced. |
