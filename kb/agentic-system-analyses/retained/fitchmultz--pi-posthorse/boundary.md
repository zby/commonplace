---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Pi Posthorse's complete extension and retained-state loop at commit 307ef6bf05bc8bd8d718725761ffdf2f2ef72539, excluding the external Pi host implementation."
run-id: AAS-2026-10-14-pi-posthorse-58b9647d2f29-01
result-disposition: complete
target-class: extension or tool mechanism
boundary-kind: whole-system
reviewed-boundary: "307ef6bf05bc8bd8d718725761ffdf2f2ef72539"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/fitchmultz/pi-posthorse
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/pi-posthorse-58b9647d2f29/related-systems/fitchmultz--pi-posthorse
  revision: "307ef6bf05bc8bd8d718725761ffdf2f2ef72539"
  sha256: null
---

# Pi Posthorse boundary

## Boundary and evidence

This run analyses Posthorse as a complete Pi extension, not as an enclosing agent runtime. Its intended use is to continue long model-driven tasks across fresh context windows while keeping notes and earlier conversation recoverable. It qualifies as an agentic mechanism because its shipped entry point installs model-callable tools, request guidance and turn/compaction hooks into Pi's model execution loop (SRC-1, `package.json`, `index.ts`, `src/rollover.ts`, `src/context-tools.ts`). The target class is **extension or tool mechanism**; the boundary kind is **whole-system**, relative to this extension, not the external host.

The package declares the loading path directly (SRC-1, `package.json`):

> "pi": {
> 		"extensions": [
> 			"./index.ts"
> 		],
> --- `package.json`

That entry point exports `createPosthorse(getPolicy)` and a default extension factory. It registers rollover policy, notes, history and renderers together. The boundary includes this factory and its same-repository consumers; it is not restricted to the exported library API (SRC-1, `index.ts`, `test/official.test.mjs`, `test/native.test.mjs`, `test/harness.ts`). The implementation declares the responsibility split (SRC-1, `index.ts`):

> * Pi owns persisted retain-none context boundaries. Posthorse owns reminder and
> * rollover policy, bounded recovery, durable notes, and history retrieval.
> --- `index.ts`

### Included functional loop

- **Produce and maintain retained state:** the notes tool creates, replaces and appends text files; storage helpers choose shared Git-worktree or agent-package locations and migrate notes out of agent-installed checkouts. Request guidance tells the model how to keep current-state notes, including edits through other available tools. Those external editors are not implemented by Posthorse (SRC-1, `src/notes.ts`, `src/files.ts`, `src/budget.ts`).
- **Admit a fresh window:** `new_context` checks handoff capacity and records its successful callback ID. Turn-end handling checks foreground results, abort conditions and current handoff capacity before drafting a retain-none compaction. Automatic compaction hooks construct recovery text from branch entries and projected content; a narrower turn-end threshold fallback handles eligible fresh-window spans. Manual compaction remains host-owned (SRC-1, `src/context-tools.ts`, `src/rollover.ts`, `src/recovery.ts`, `src/recovery-results.ts`).
- **Reload and consume:** notes reads/searches return stored text; history searches/read pages consume the current branch or project-scoped session files, including nested subagent journals. History normalization and recovery processing account for context edits and legacy window data. Notes/history share page reservations. Request-local guidance tells the continuing model to restore state and verify it before further work (SRC-1, `src/history.ts`, `src/history-search.ts`, `src/session-files.ts`, `src/history-entries.ts`, `src/history-pages.ts`, `src/paging.ts`, `src/budget.ts`).
- **Evaluate the loop:** shipped SDK test drivers load the factory or file extension, create sessions with a faux provider, and exercise retention, rollover, retrieval and reopening. These are included source consumers, not excluded enclosing applications. Their source establishes intended assertions, not observed passing runs (SRC-1, `test/official.test.mjs`, `test/native.test.mjs`, `test/host.test.mjs`, `test/pi-loader.ts`).

The request guidance explicitly connects retention to later consumption (SRC-1, `src/budget.ts`):

> After a rollover, earlier conversation stays in history. Restore notes and todos, then verify live state before stateful or external work; automatic handoffs record inputs, not progress.
> Keep one concise current-state note per task. Preserve decisions and safety constraints; link fuller evidence and history instead of copying them. Edit changed sections rather than resending unchanged content.
> --- `src/budget.ts`

A same-repository test driver includes reopening the persisted journal (SRC-1, `test/official.test.mjs`):

> const reopened = SessionManager.open(h.sessionManager.getSessionFile());
> 	assert.deepEqual(
> 		reopened.buildSessionContext().messages,
> 		JSON.parse(JSON.stringify(h.sessionManager.buildSessionContext().messages)),
> 	);
> --- `test/official.test.mjs:269-273`

### Repository coverage

The tracked tree and shipped imports were inspected before selecting whole-system scope. All production TypeScript files were read. Test inspection covered driver setup, the explicit-reset/notes/history/resume scenario, and a bounded inventory of test declarations; it was not a full assertion audit. The following table accounts for every top-level tracked file or directory. “Excluded” means deliberately outside functional analysis, not inaccessible. Unread support-file contents are distinguished from evidence gaps.

| Top-level tracked path | Treatment and material paths | Role and limit on conclusions |
| --- | --- | --- |
| `index.ts` | Included; read completely | Package entry point and SDK factory; installs all functional components (SRC-1). |
| `ui.ts` | Included; read completely | Registers historical-window/reminder renderers and exports tool cards (SRC-1). |
| `src` — policy/admission | Included; `src/budget.ts`, `src/context-tools.ts`, `src/rollover.ts`, `src/reminders.ts`, `src/contracts.ts`; read completely | Guidance, capacity estimates, reset admission, automatic recovery hooks and reminder state (SRC-1). |
| `src` — durable state/recovery | Included; `src/notes.ts`, `src/files.ts`, `src/recovery.ts`, `src/recovery-results.ts`; read completely | Note persistence, storage migration and bounded recovery records (SRC-1). |
| `src` — retrieval/presentation | Included; `src/history.ts`, `src/history-entries.ts`, `src/history-search.ts`, `src/history-pages.ts`, `src/session-files.ts`, `src/message-text.ts`, `src/paging.ts`, `src/ui/cards.ts`, `src/ui/display.ts`, `src/ui/text.ts`; read completely | Retained-content selection, normalization, paging and operator display (SRC-1). |
| `test` | Included as evaluator source; driver reads: `test/harness.ts`, `test/pi-loader.ts`, `test/host.test.mjs`, fixture setup in `test/native.test.mjs`, fixture and reset/resume scenario in `test/official.test.mjs`; declaration scans in `test/posthorse.test.ts`, `test/renderers.test.ts`, `test/native.test.mjs` | SDK consumers and intended runtime/storage/rendering checks. Remaining assertion bodies, `test/results.ts`, `test/quality-*.ts` and `test/quality-support.ts` were inventoried but not audited. No execution, suite-pass or exhaustive evaluator-coverage conclusion (SRC-1). |
| `README.md` | Included; read completely | User-facing purpose, tools, installation and limits; declared contract, not independent operation evidence (SRC-1). |
| `docs` | Included: `docs/reference.md`, `docs/development.md`, `docs/performance.md`; read completely. Excluded: `docs/quality.md`, `docs/quality-engine.md`; inventoried, contents not inspected | Runtime/storage instructions, host-qualification contract and attributed performance report. Excluding quality-engine internals prevents checker-correctness conclusions; performance data is not reproduced (SRC-1). |
| `ARTIFACTS` | Included: `ARTIFACTS/investigation-report.md`; read completely | Source-native cost investigation, explicitly historical and without inspected production journals/invoices. Does not establish current production cost or incident causation (SRC-1). |
| `package.json` | Included; read completely | Published file list, loading path, peer dependencies and verification entry points (SRC-1). |
| `package-lock.json` | Included as dependency-pin evidence; inventoried, contents not yet inspected | Available to later source inspection; no resolved dependency-graph audit claimed. |
| `.github` | Included evaluator wiring: `.github/workflows/ci.yml`, read completely. Excluded: `.github/workflows/npm-release.yml`, `.github/actionlint.yaml`, `.github/readme/context-rollover.png`, `.github/readme/context-rollover.svg`; inventoried | CI selects host qualification and retains evidence; release automation, action linting and illustrative assets are outside the functional loop. No publication or release-success conclusion (SRC-1, `package.json`, `.github/workflows/ci.yml`). |
| `scripts` | Excluded development checker plane; symbol/import scan of `scripts/quality-policy.ts`, `scripts/quality-prepare.ts`, `scripts/quality-source.ts`, `scripts/setup-oxlint-engine.ts`, `scripts/setup-quality-engine.ts` | Package scripts invoke these for quality preparation, not extension loading. No checker implementation or build-success conclusion (SRC-1, `package.json`). |
| `patches` | Excluded; inventoried `patches/oxlint-import-cycles.patch`, `patches/tsgolint-readonly-flatmap.patch`, `patches/tsgolint-readonly.patch`, `patches/tsgolint-safe-call.patch` | Development checker modifications referenced by setup tooling; no patch-correctness conclusion (SRC-1, `scripts/setup-oxlint-engine.ts`, `scripts/setup-quality-engine.ts`). |
| `AGENTS.md` | Excluded maintainer instruction; read completely | Code-quality and verification procedure, not the model's task-state guidance. No compliance assessment (SRC-1). |
| `CHANGELOG.md` | Excluded; inventoried, contents not inspected | Release history; no historical behavior reconstruction. |
| `LICENSE` | Excluded; inventoried, contents not inspected | Legal terms; no licensing assessment. |
| `diagram.png`, `diagram.svg` | Excluded; inventoried, contents not inspected | Illustrative assets; no diagram-derived mechanism claims. |
| `.gitattributes`, `.gitignore` | Excluded; inventoried, contents not inspected | Repository metadata; no checkout/ignore-policy assessment. |
| `.oxfmtrc.json`, `.oxlintrc.json` | Excluded; inventoried, contents not inspected | Development formatter/linter configuration; no enforcement assessment. |
| `.vscode` | Excluded; inventoried `.vscode/extensions.json`, `.vscode/settings.json` | Editor configuration; no editor-integration assessment. |
| `renovate.json`, `tsconfig.json` | Excluded; inventoried, contents not inspected | Dependency-maintenance and compiler configuration; no updater or typecheck-success assessment. |

### External responsibilities and evidence limits

Pi's SDK, session manager, model/provider execution, compaction preparation and persistence, scheduling, built-in editors and physical request sizing are external dependencies, not Posthorse responsibilities. TUI components and TypeBox schemas are imported dependencies; Node/filesystem/Git metadata and optional local ripgrep support storage and archive retrieval. No external dependency implementation is frozen in this run. This prevents independent certification of host persistence, provider-boundary safety, host-version compatibility, external editor behavior or third-party component correctness (SRC-1, `package.json`, `index.ts`, `src/rollover.ts`, `src/files.ts`, `src/session-files.ts`, `docs/reference.md`). Background work outside the foreground tool batch and application-specific task execution are excluded; the boundary cannot establish their synchronization or task correctness (SRC-1, `src/context-tools.ts`, `docs/reference.md`).

The immutable evidence is repository commit **307ef6bf05bc8bd8d718725761ffdf2f2ef72539**, with applicability cutoff **2026-10-14**. The supplied checkout's HEAD matched this commit and its tracked diff was clean. The overall tier is **code-grounded**. Source-native documentation supplies intent and attributed reports, not independent verification. No target code, tests or examples were executed; no provider calls, production session traces, qualification artifacts or controlled experiment were supplied. Those missing evidence layers prevent measured effectiveness, runtime success, production cost and causal-improvement conclusions. Available but unread files above are not access gaps.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/fitchmultz/pi-posthorse` | 307ef6bf05bc8bd8d718725761ffdf2f2ef72539 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/pi-posthorse-58b9647d2f29/related-systems/fitchmultz--pi-posthorse`. Implementation: complete `index.ts`, `ui.ts` and all `src` files; test-driver/scenario reads and evaluator scans as listed above; CI workflow and development-script symbol scans. Doctrine/design: `README.md`, `docs/reference.md`, `docs/development.md`, `package.json`; maintainer `AGENTS.md` inspected only to distinguish its role. Reported operation: `docs/performance.md`, `ARTIFACTS/investigation-report.md`, with their stated historical and measurement limits. | Implementation: [entry point](https://github.com/fitchmultz/pi-posthorse/blob/307ef6bf05bc8bd8d718725761ffdf2f2ef72539/index.ts), [rollover](https://github.com/fitchmultz/pi-posthorse/blob/307ef6bf05bc8bd8d718725761ffdf2f2ef72539/src/rollover.ts), [notes](https://github.com/fitchmultz/pi-posthorse/blob/307ef6bf05bc8bd8d718725761ffdf2f2ef72539/src/notes.ts), [history](https://github.com/fitchmultz/pi-posthorse/blob/307ef6bf05bc8bd8d718725761ffdf2f2ef72539/src/history.ts), [SDK evaluator](https://github.com/fitchmultz/pi-posthorse/blob/307ef6bf05bc8bd8d718725761ffdf2f2ef72539/test/official.test.mjs). Doctrine/design: [reference](https://github.com/fitchmultz/pi-posthorse/blob/307ef6bf05bc8bd8d718725761ffdf2f2ef72539/docs/reference.md). Reported operation: [performance](https://github.com/fitchmultz/pi-posthorse/blob/307ef6bf05bc8bd8d718725761ffdf2f2ef72539/docs/performance.md), [investigation](https://github.com/fitchmultz/pi-posthorse/blob/307ef6bf05bc8bd8d718725761ffdf2f2ef72539/ARTIFACTS/investigation-report.md). | No repository access gap found. External Pi/provider/automation implementations and actual execution/qualification/production artifacts are outside the frozen source set; this prevents independent host qualification, observed runtime outcomes and causal or production-cost conclusions. Unread repository support files remain available, not inaccessible. |
