---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "kgai's shipped decision-memory engine, agent capture instructions, host hooks and retained-state readers at commit 0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b."
run-id: AAS-2026-10-14-kgai-54bcae52e039-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/kgaidev/kgai
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/kgai-54bcae52e039/related-systems/kgaidev--kgai
  revision: 0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b
  sha256: null
---

# kgai boundary

## Boundary and evidence

This run analyses kgai as a shipped decision-memory system for AI-assisted development, not merely its Go library or CLI. Its intended use is to retain structural engineering choices and their reasons, recall them before later changes, and share their history across installations. The boundary includes the engine, model-facing skill and commands, lifecycle hooks, configuration approval, synchronization clients, optional model-fork capture mod, and editor reader. These responsibilities are shipped in the same repository and are not excluded as enclosing applications (SRC-1: `README.md`, `skills/knowledge-graph/SKILL.md`, `hooks/hooks.json`, `mods/kgai-mod/hooks/register.tsx`, `editors/vscode/src/extension.ts`).

The target class is **memory/knowledge/context-engineering system**. The boundary kind is **whole-system**: the initial inspection traces shipped producers, admission and persistence, maintenance, reload and later consumption, including the optional capture caller and evaluation harness. This does not mean every implementation branch has already been inspected. Remaining files in the frozen repository remain eligible evidence for later jobs.

The memory loop depends on a host model interpreting task work and retained decisions. The default engine does not own that enclosing model runtime: its skill prescribes recall and capture, and its hooks supply a capture nudge. The optional mod does issue a side-model request through the host API and submits the resulting proposal to the same engine. Both paths belong to this analysis (SRC-1: `skills/knowledge-graph/SKILL.md`, `hooks/auto-capture-stop.sh`, `mods/kgai-mod/hooks/register.tsx`). Minimum passages establishing this scope:

> ALSO invoke it BEFORE a non-trivial change to read prior decisions you must respect,
> and to answer "why is X like this", "how does X relate to Y", "what changed and when".
> --- `skills/knowledge-graph/SKILL.md`

> const reply = await $.model.fork({ prompt: CAPTURE_PROMPT })
> --- `mods/kgai-mod/hooks/register.tsx`

The shipped CLI dispatches ingest, recall, history, conflicts, synchronization, configuration and repair commands. Ingest decodes a constrained input, calls the engine, appends an event and applies it to the graph. Store append writes to a per-install shard. The editor's shipped `kgread` entry point reloads that retained log through `internal/view` and `internal/replay`; it is a consumer within the target rather than an external example application (SRC-1: `src/main.go`, `src/internal/engine/engine.go`, `src/internal/store/store.go`, `src/cmd/kgread/main.go`, `src/internal/view/model.go`, `editors/vscode/src/extension.ts`).

> if err := e.S.Append(&ev); err != nil {
> return res, err
> }
> if err := g.ApplyEvent(ev); err != nil {
> return res, fmt.Errorf("event appended but projection failed (run `kg rebuild`): %w", err)
> }
> --- `src/internal/engine/engine.go`

> m.Proj = replay.Build(evs)
> m.Stats = m.Proj.Stats()
> --- `src/internal/view/model.go`

### Frozen evidence and limits

Evidence is the acquired Git repository at **0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b**, with an applicability cutoff of **2026-10-14**. The checkout HEAD was verified against the acquisition pin. Overall evidence tier is **code-grounded**: executable entry points and their producer/consumer connections were inspected as source, alongside shipped doctrine. No target code, tests, examples or providers were executed.

External dependencies include the Claude Code, Codex CLI and Gemini CLI hosts and their model/tool/hook interfaces; the optional mod's `claude-code` API; VS Code extension APIs; the native Kuzu binding/library; Git; and AWS/S3 or cloud-broker services used by configured sync transports. The repository contains host wiring and synchronization clients, not those hosts, model services or broker implementation (SRC-1: `hosts/README.md`, `mods/kgai-mod/hooks/register.tsx`, `editors/vscode/src/extension.ts`, `src/go.mod`, `src/internal/remote/cloud.go`, `docs/ARCHITECTURE.md`). Their exclusion prevents conclusions about host scheduler internals, actual model compliance, remote service guarantees or end-to-end deployed availability.

Live websites, release binaries, downloaded native libraries, the separate Gemini distribution repository and external benchmark archives are not frozen evidence. This prevents verification of their current contents or reported scale results. Repository documentation's statements about successful host runs and performance are reported operation, not observed runs in this analysis. The inspected smoke-test harness establishes what a shipped evaluator measures, not that its expectations passed. The demo store is explicitly fictional, not production experience (SRC-1: `README.md`, `hosts/README.md`, `tests/host-smoke.sh`, `examples/acme-shop/README.md`). No access gap was encountered for tracked repository text; uninspected files are not unavailable evidence.

### Top-level tracked coverage

The tracked tree was enumerated at the frozen commit. “Included” means within the functional evidence boundary; initial inspection is stated separately. Every top-level tracked file or directory is accounted for below. All rows concern SRC-1.

| Top-level path | Coverage | Role, material paths and initial inspection | Exclusion limit or remaining inspection |
|---|---|---|---|
| `.claude-plugin/` | Included | `plugin.json` inspected for plugin identity; `marketplace.json` enumerated as packaging for the primary plugin and mod. | Marketplace details remain for later inspection; no runtime conclusions from manifest alone. |
| `.github/` | Included | Searches inspected `workflows/build.yml`, `test.yml`, `vscode.yml` for engine/native-library builds, hook tests and bundled `kgread`. | Workflow definitions are not CI run results. |
| `.gitignore` | Excluded | Repository housekeeping, enumerated. | No conclusion about development-checkout ignore hygiene. Store scaffold rules in `src/internal/store/` remain included. |
| `CHANGELOG.md` | Included | Release documentation, enumerated. | Not initially inspected; no release-history claims established. |
| `LICENSE` | Excluded | Legal license text, enumerated. | No licensing-compliance assessment. |
| `README.md` | Included | Fully inspected intended use, integration surfaces, reported operation and external dependencies. | Descriptions of success are attributed claims. |
| `bin/` | Included | `kg` fully inspected: launcher, bootstrap and engine execution. | Actual installation behavior was not exercised. |
| `commands/` | Included | Eight `kg-*.md` prompts enumerated; `kg-review.md` fully inspected; searches trace skill references. Covers ask, decision, history, query, conflicts, sync and trust procedures. | Other command bodies remain for later inspection. |
| `docs/` | Included | `ARCHITECTURE.md` fully inspected; `CONFIGURATION.md` and `SHARED-STORE.md` identified as configuration/approval and shared-store contracts. `demo.gif` is illustrative media. | Remaining contract bodies and media not initially inspected; no observed operation inferred from illustration. |
| `editors/` | Included | `vscode/src/extension.ts` activation and reader startup inspected; `src/reader.ts`, trees, detail, graph panels, webview, package/build metadata and tests enumerated. | Downstream UI and reader protocol details remain for later inspection. The retained-state consumer is not excluded. |
| `examples/` | Included | `acme-shop/README.md` fully inspected; `.kgai/store/log/`, config, application stubs and admin/web paths enumerated as fictional demonstration fixtures. | Fixture payloads not initially inspected; no claim about real decisions or real team use. |
| `hooks/` | Included | `hooks.json`, `session-start.sh`, `inject-prompt.sh`, `turn-state.sh`, `auto-capture-stop.sh`, `auto-sync.sh` fully inspected. Routes install/config context, edit markers, model capture nudge and detached sync. | Host event delivery and model responses were not observed. |
| `hosts/` | Included | `README.md` and `gemini/GEMINI.md` fully inspected; Gemini manifest and hook mapping searched. | Built external Gemini package is not captured; native host implementations are excluded dependencies. |
| `mods/` | Included | `kgai-mod/hooks/register.tsx` fully inspected: side-model call, proposal parsing, dry-run then ingest, classic-nudge suppression and confirmation UI. `rows.ts`, manifests, types and tests enumerated. | Rendering helpers and tests remain for later inspection; mod compatibility was not exercised. |
| `scripts/` | Included | `install.sh` and `build-host-pkg.sh` searched for release/build installation, copied hooks and command conversion; `fetch-libs.sh` and `publish-gemini.sh` enumerated. | Full installation, dependency capture and publishing branches remain for later inspection; no download or build was run. |
| `skills/` | Included | `knowledge-graph/SKILL.md` fully inspected: recall-before-change, lexical reformulation, capture selection, mutations, conflict resolution and approval instructions. | Instructions do not establish model adherence. |
| `src/` | Included | `main.go` dispatch/admission and `engine/engine.go` ingest/sync ranges inspected; `store/store.go` append inspected; `view/model.go` load and `cmd/kgread/main.go` inspected. Searches and tree inspection account for `event`, `graph`, `replay`, `engine/reads.go`, `engine/search.go`, store settings/trust/locks, remote transports, turn markers, view/server, tests, `pretty.go`, `go.mod`, `go.sum`, and `tools/genlog`/`tools/warmbench`. | Detailed identity, retrieval, replay equivalence, transport validation, repair and benchmark branches remain for later source tracing. No subsystem here is excluded. |
| `tests/` | Included | `host-smoke.sh` fully inspected through store-based verdict; `run.sh` searched; hook contract/parse, install-flow/path/rc-safety, host and repository-hygiene suites plus helpers enumerated. | Test source supplies evaluator design only; no retained execution results were established. |

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/kgaidev/kgai` | 0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/kgai-54bcae52e039/related-systems/kgaidev--kgai`. Implementation: tree, primary launcher/hook wiring, CLI dispatch/admission, engine ingest/sync, store append, view load, reader entry point, editor activation and complete optional capture mod; scoped searches of build/host mappings, retrieval/settings/trust/transport interfaces and evaluation tooling. Doctrine/design: complete `README.md`, `docs/ARCHITECTURE.md`, `skills/knowledge-graph/SKILL.md`, `commands/kg-review.md`, `hosts/README.md`, `hosts/gemini/GEMINI.md`, `examples/acme-shop/README.md`. Reported operation: host success and scale assertions in README/host/architecture documentation only. | Implementation: [CLI](https://github.com/kgaidev/kgai/blob/0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b/src/main.go), [engine](https://github.com/kgaidev/kgai/blob/0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b/src/internal/engine/engine.go), [capture mod](https://github.com/kgaidev/kgai/blob/0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b/mods/kgai-mod/hooks/register.tsx), [reader load](https://github.com/kgaidev/kgai/blob/0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b/src/internal/view/model.go), [evaluator](https://github.com/kgaidev/kgai/blob/0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b/tests/host-smoke.sh). Doctrine/design: [skill](https://github.com/kgaidev/kgai/blob/0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b/skills/knowledge-graph/SKILL.md), [architecture](https://github.com/kgaidev/kgai/blob/0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b/docs/ARCHITECTURE.md). Reported operation: [README](https://github.com/kgaidev/kgai/blob/0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b/README.md), [host report](https://github.com/kgaidev/kgai/blob/0ac7f1fae4528805c1d5f504c1bfd6cc34ac953b/hosts/README.md). | No tracked-source access gap established. External hosts/providers, native binaries and broker implementation are outside this source. No observed-run or causal-experiment layer was established; reported model compliance, deployment reliability and performance cannot be independently verified from the initial evidence. |
