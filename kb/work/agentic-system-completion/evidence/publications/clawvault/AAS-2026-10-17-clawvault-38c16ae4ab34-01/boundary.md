---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "ClawVault's shipped memory system and integrations at commit bd702e9cce436bc3065827714cd576e8be20c375."
run-id: AAS-2026-10-17-clawvault-38c16ae4ab34-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: bd702e9cce436bc3065827714cd576e8be20c375
analysis-cutoff: "2026-10-17"
evidence-tier: code-grounded
source:
  identity: https://github.com/Versatly/clawvault
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-clawvault/related-systems/Versatly--clawvault
  revision: bd702e9cce436bc3065827714cd576e8be20c375
  sha256: null
---

# ClawVault boundary

## Boundary and evidence

ClawVault is in scope as a memory/knowledge/context-engineering system. Its intended use is persistent, typed agent memory with later retrieval and session continuity. The boundary is the whole shipped system, not just the exported vault API. It includes the Node CLI, TypeScript library, OpenClaw plugin and memory slot, Python SDK, dashboard, shipped observation drivers, maintenance workers, prompts, templates and evaluation machinery. Package entry points establish distinct CLI, library and plugin consumers (SRC-1, `package.json`, `bin/clawvault.js`, `src/index.ts`, `src/openclaw-plugin.ts`).

The source declares the intended storage medium:

> ClawVault is a structured persistent memory system for AI agents. It stores memories as Obsidian-compatible markdown files.
> --- `AGENTS.md`

The classification is also implementation-grounded. Vault storage writes Markdown, reloads the document and updates search and graph state; loading a vault reads its configuration and reindexes its documents. Retrieval delegates to the search engine (SRC-1, `src/lib/vault.ts`). The observer retains raw messages, compresses them against existing observations, writes observation Markdown and routes it into categories (SRC-1, `src/observer/observer.ts`). Its shipped compression prompt explicitly serves subsequent memory use:

> 'You are an observer that compresses raw AI session messages into durable, human-meaningful observations.',
> --- `src/observer/compressor.ts`

The enclosing agent runtime is not ClawVault. However, ClawVault's own host-facing drivers are included, not dismissed as external callers. The memory slot exposes capture, store, search and recall; capture applies quality checks before storing accepted candidates. The actual OpenClaw plugin registers memory tools and lifecycle, prompt-build and outbound-message hooks. Its prompt-build handler retrieves vault content and returns system-context additions. These are shipped consumption and admission responsibilities (SRC-1, `src/plugin/slot.ts`, `src/capture/service.ts`, `src/openclaw-plugin.ts`, `src/plugin/hooks/before-prompt-build.ts`, `src/plugin/vault-context-injector.ts`). The recall mandate is authored guidance, not evidence that a host model obeys it:

> "- Before answering anything about prior work, people, decisions, preferences, todos, or historical context, call memory_search first.",
> --- `src/plugin/hooks/before-prompt-build.ts`

The loop also includes non-plugin operation. Sleep writes a handoff and can process a session transcript and run reflection; wake reloads the vault, builds a recap and reads recent observations. Scheduled shell drivers invoke the observation CLI. Maintenance dispatches curator, janitor, distiller and surveyor workers and persists maintenance state; the inspected curator classifies inbox items with LLM routes or a heuristic fallback and writes category documents. The Python SDK independently implements Markdown storage, search, checkpoints and a wake-context string (SRC-1, `src/commands/sleep.ts`, `src/commands/wake.ts`, `scripts/observe-active-sessions.sh`, `scripts/observe-stale-sessions.sh`, `src/commands/maintain.ts`, `src/lib/maintenance/curator-worker.ts`, `python/src/clawvault/vault.py`).

The frozen evidence is repository `https://github.com/Versatly/clawvault` at full commit `bd702e9cce436bc3065827714cd576e8be20c375`, verified as the checkout HEAD. The applicability cutoff is 2026-10-17. No other revision, external page, installed package or dependency implementation supplies evidence. The overall tier is code-grounded: implementation and authored contracts were inspected without running the target, its tests, examples or provider calls. `complete` means a boundary and source were established; it does not claim exhaustive code review or successful operation.

### Coverage of the frozen repository

All top-level tracked entries are classified below. “Included” makes a path eligible within this whole-system boundary; it does not assert that every file was inspected. Named traces identify the initial inspection. Inventory-only material remains available for later analysis and is not an access gap. All rows refer to SRC-1.

| Top-level tracked entry | Treatment and role | Initial inspection and conclusion limits |
|---|---|---|
| `package.json`, `package-lock.json` | Included: package entry points, build and dependency contract. | Manifest inspected; lockfile inventoried, not audited. No claim of installed dependency behavior or published-package equivalence. |
| `bin/` | Included: executable CLI and command registration, runtime helpers and contract tests. | Traced `clawvault.js` registration into core, query, session, maintenance, resilience, task, project, vault, configuration and networking command groups; searched `register-vault-operations-commands.js` dashboard launch. Individual command branches and tests are not all inspected. |
| `src/` | Included: all executable memory paths and colocated tests. | Inspected `index.ts`, `openclaw-plugin.ts`, `plugin/slot.ts`, capture service, prompt/message/observation/session hooks, vault context injector, vault load/store/find, observer persistence, compressor prompt, wake/sleep, maintain dispatcher and curator, recall service and benchmark runner. Searched replay, context, reflection, fact and maintenance wiring, search, hosted embeddings/reranking and WebDAV. Inspected peer-sync transfer loop in `lib/tailscale.ts`. This covers entry points and producers, admission, maintenance and later consumers; finer algorithm branches and remaining tests await analysis, not external evidence. |
| `python/` | Included: separately packaged SDK, its storage/search/semantic helpers and tests. | `src/clawvault/vault.py` inspected in full, including store, search, checkpoint, wake and document reload. Helper implementations and tests inventoried, not fully inspected. API resemblance does not prove parity with TypeScript. |
| `scripts/` | Included: shipped scheduled observation callers. | Both `observe-active-sessions.sh` and `observe-stale-sessions.sh` inspected in full; both route to CLI observation rather than owning an enclosing runtime. Scheduler deployment is not observed. |
| `dashboard/` | Included: retained-memory graph consumer and live display. | `server.js` inspected in full: initial graph load, HTTP/WebSocket delivery and Markdown file watching. `lib/vault-parser.js`, `lib/graph-diff.js`, their tests and `public/` UI inventoried; rendering and graph correctness not established. |
| `SKILL.md` | Included: shipped agent usage and maintenance instructions. | Inspected in full, including wake/checkpoint/sleep checklist, memory typing, linking, recovery and repair guidance. Documentation claims are not substituted for implementation. |
| `templates/` | Included: schemas and text for retained memory and task/session artifacts. | `handoff.md` inspected; checkpoint, daily, decision, lesson, person, project and task templates inventoried. No claim that every producer enforces every template field. |
| `openclaw.plugin.json` | Included: host manifest and feature/configuration contract. | Inspected in full alongside registration code. Host acceptance and runtime compatibility are not observed. |
| `docs/` | Included: installation, OpenClaw usage and security-release procedures. | `getting-started/installation.md`, `openclaw-plugin-usage.md`, `clawhub-security-release-playbook.md` inventoried, not yet inspected. No operational or security conclusion rests on these documents. |
| `README.md`, `CHANGELOG.md`, `SECURITY.md` | Included: source-native usage, release and security doctrine. | Inventoried, not yet inspected; no release-history or security assurance inferred. |
| `autoresearch/` | Included: improvement-plane instructions, scripts and recorded results. | `program.md` and `run.sh` inspected in full; `experiment.sh`, `results.tsv` and saved JSON reports inventoried. The instructions describe an agent-driven modification/benchmark loop; this boundary makes no causal or measured improvement claim from its uninspected reports. |
| `eval/` | Included: shipped evaluation consumer. | Inspected `run_v35_full.py` benchmark loop and searched ingestion, retrieval, reader and scoring entry points. It instantiates its own `ClawVaultV35` adapter per example, ingests sessions and calls `answer`; it is not automatically an end-to-end test of the TypeScript plugin. Dataset and provider execution are outside the supplied evidence. |
| `testdata/` | Included: observer benchmark transcript/config/expected-output fixtures. | Inventoried client-meeting, coding-decisions and low-signal maintenance fixtures; traced their use through `src/observer/benchmark/runner.ts`. Fixture contents and score validity not yet assessed. |
| `tests/` | Included: compatibility fixtures and expected host-wiring cases. | Inventoried `compat-fixtures/`, including healthy and broken package/skill/hook cases. Fixture hooks are test inputs, not proof that production hooks execute. |
| `schemas/` | Included: compatibility artifact/report validation contracts. | Inventoried JSON schemas and bundle manifest; validator completeness and bundle integrity not assessed. |
| `benchmarks/`, `examples/` | Included: shipped benchmark/example deployment callers. | Inventoried `benchmarks/Clawfile`, `benchmarks/claw-pod.yml` and `examples/observer-bench/` recipe, README and pod configuration. Not yet inspected; no deployed-container performance claim. |
| `AGENTS.md`, `AGENT-TASK.md`, `PLAN.md`, `OPENCLAW_REMEDIATION_PLAN.md` | Included as development/design doctrine, not executable authority for this analysis. | `AGENTS.md` inspected; task and plan documents inventoried, not yet inspected. Planned work cannot establish shipped behavior. |
| `.cursor-context/` | Excluded: bundled enclosing-host background. | Tree inventoried, contents not inspected. Its OpenClaw notes/types cannot establish actual host scheduling, event semantics or model behavior. ClawVault's own `src/plugin/` contracts remain included. |
| `.github/` | Included as build/release and development automation context. | Inventoried CI, notification workflow and release template; not yet inspected. No claim that CI ran or a release was published. |
| `.gitignore`, `.npmignore`, `tsconfig.json`, `vitest.config.ts` | Included: repository, distribution, compilation and test configuration. | Inventoried, not yet inspected; no build/test success or precise published file-set claim. |
| `LICENSE` | Excluded: legal text, not memory-loop evidence. | Inventoried, not inspected; this analysis offers no licensing conclusion. |

### External dependencies and evidence limits

The included code depends on Node and package libraries, filesystem state and, by feature, OpenClaw, qmd, model endpoints, embedding/reranking services, Tailscale and remote peers. The package declares qmd an optional peer dependency; inspected vault methods and slot consumers establish an API path independent of attributing qmd's internal behavior. Hosted embedding/reranking modules contain network calls, and peer sync reads, transfers and writes vault files. Consequently a blanket “no network except observation” claim from older usage guidance is not adopted (SRC-1, `package.json`, `src/lib/vault.ts`, `src/plugin/slot.ts`, `src/lib/hosted-embeddings.ts`, `src/lib/hosted-rerank.ts`, `src/lib/tailscale.ts`, `SKILL.md`).

Excluded external implementations prevent conclusions about actual OpenClaw hook delivery, model compliance, provider reliability, qmd internals, remote-peer trust or Obsidian behavior. No live vault, deployed host session, external dataset or independent execution trace was supplied. These are unavailable operational evidence, not uninspected repository files. They prevent claims of real retention quality, successful recovery, deployment security, measured retrieval utility or causal benchmark gains. In-repository evaluation and autoresearch artifacts remain eligible source-native evidence, with their conditions to be assessed before use; this boundary registers no observed-run or causal-experiment layer.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/Versatly/clawvault` | bd702e9cce436bc3065827714cd576e8be20c375 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-clawvault/related-systems/Versatly--clawvault`. Implementation: `package.json`, `bin/clawvault.js`, `src/index.ts`, `src/openclaw-plugin.ts`, `src/plugin/slot.ts`, `src/capture/service.ts`, `src/plugin/hooks/before-prompt-build.ts`, `src/plugin/hooks/message-sending.ts`, `src/plugin/hooks/observation.ts`, `src/plugin/hooks/session-lifecycle.ts`, `src/plugin/vault-context-injector.ts`, `src/lib/vault.ts`, `src/observer/observer.ts`, `src/recall/service.ts`, `src/commands/wake.ts`, `src/commands/sleep.ts`, `src/commands/maintain.ts`, `src/lib/maintenance/curator-worker.ts`, `src/observer/benchmark/runner.ts`, `scripts/observe-active-sessions.sh`, `scripts/observe-stale-sessions.sh`, `dashboard/server.js`, `python/src/clawvault/vault.py`, peer sync in `src/lib/tailscale.ts`, evaluation loop in `eval/run_v35_full.py`, and source searches recorded in the coverage table. Doctrine/design: `AGENTS.md`, `SKILL.md`, `openclaw.plugin.json`, `templates/handoff.md`, compressor prompt in `src/observer/compressor.ts`, maintenance prompts in `src/lib/maintenance/worker-utils.ts`, `autoresearch/program.md`, `autoresearch/run.sh`. | Implementation: [package entry points](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/package.json), [plugin driver](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/openclaw-plugin.ts), [vault](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/lib/vault.ts), [observer](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/observer.ts), [Python SDK](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/python/src/clawvault/vault.py), [benchmark](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/benchmark/runner.ts). Doctrine/design: [skill](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/SKILL.md), [compression prompt](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/src/observer/compressor.ts), [improvement instructions](https://github.com/Versatly/clawvault/blob/bd702e9cce436bc3065827714cd576e8be20c375/autoresearch/program.md). | No repository access failure encountered. External host/provider/dependency implementations and deployed execution evidence are not supplied; actual integration operation, quality and causal efficacy are unestablished. Available but uninspected paths are distinguished in the coverage table. |
