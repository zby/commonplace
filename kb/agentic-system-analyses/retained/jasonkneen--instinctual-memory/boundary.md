---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Instinctual Memory's shipped memory loop and agent integrations at Git revision 6acb13dc35765bf5ccfc87e445dd09c480f1c28a."
run-id: AAS-2026-10-12-instinctual-memory-af48437aa60c-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "6acb13dc35765bf5ccfc87e445dd09c480f1c28a"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/jasonkneen/instinctual-memory
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/instinctual-memory-workflow-af48437aa60c/related-systems/jasonkneen--instinctual-memory
  revision: 6acb13dc35765bf5ccfc87e445dd09c480f1c28a
  sha256: null
---

# Instinctual Memory boundary

## Boundary and evidence

The target is the shipped Rust `mem` product, including its library, executable, integrations and agent skill. Its intended use is durable memory from agent sessions and project instruction files, with later retrieval and changes by agents. This is an in-scope memory/knowledge/context-engineering system, not an enclosing agent runtime. It issues model calls for fact extraction and maintenance and serves retained context to host agents. The whole-system boundary includes the shipped callers that produce, persist, reload, maintain and consume that state (SRC-1, `Cargo.toml`, `src/main.rs`, `src/cli.rs`, `src/consolidate.rs`, `src/tidy.rs`, `src/ops.rs`, `src/hook.rs`, `skills/mem/SKILL.md`).

The declared product loop is:

> `mem` reads the conversations you have already had with Claude Code, Codex, and OpenCode, plus your `AGENTS.md`/`CLAUDE.md`/`README.md` files, and turns them into a small set of curated, sourced facts stored in a plain Git repository. Agents search that memory (facts and raw sessions together), read it over MCP, change it through a validated path, and get it written back into each project's `AGENTS.md`.
> --- `README.md`

Initial implementation inspection traces `src/main.rs` into CLI store resolution and dispatch. Ingest and backfill append adapter output to the journal. The CLI consolidation loop invokes `Consolidator::run_batch`, which reloads the checkpoint, entities and controls, extracts facts and publishes changed state. Direct changes use `change::apply`; its publisher validates a candidate before a compare-and-swap update. Retrieval reloads the published Git state and journal through `ops::combined_search`. MCP, HTTP and shell dispatch to the shared operation layer. Writeback reads entity facts and writes a managed block into a project instruction file. These shipped drivers are included rather than attributed to an external caller (SRC-1, `src/main.rs`, `src/cli.rs`, `src/journal.rs`, `src/consolidate.rs`, `src/change.rs`, `src/repo.rs`, `src/ops.rs`, `src/mcp.rs`, `src/http_serve.rs`, `src/shell.rs`).

The agent-facing loop also belongs to the target. Setup embeds and installs the skill and registers hooks and MCP configuration. Hooks reload preferences or matching facts as host context; session-end sync launches the shipped backfill and consolidation commands. The skill instructs an agent to sync, search, change, write back and review proposed cleanup. Extraction and cleanup prompts embedded in Rust are included as instructions governing retained content (SRC-1, `src/setup.rs`, `src/hook.rs`, `skills/mem/SKILL.md`, `src/consolidate.rs`, `src/tidy.rs`).

> /// The `/mem` skill, shipped inside the binary.
> const SKILL: &str = include_str!("../skills/mem/SKILL.md");
> --- `src/setup.rs`

> The test for every candidate: would a new teammate, starting fresh next month, need to know this? If it only describes what was happening in that session, it is not a fact.
> --- `src/consolidate.rs`

The boundary freezes only repository revision `6acb13dc35765bf5ccfc87e445dd09c480f1c28a`, verified against checkout HEAD. The applicability cutoff is 2026-10-12, not a claim that this revision reflects every change through that date. The overall tier is code-grounded: inspected source establishes implemented paths and shipped instructions, not successful deployment or model quality.

External dependencies are Git and the Rust dependency stack; configurable OpenAI-compatible model endpoints for extraction and cleanup; OpenRouter Decisions for JEV reranking; cached fastembed cross-encoder weights for local reranking; and host agents supplying transcripts, hook payloads, instruction-file consumption and MCP clients (SRC-1, `Cargo.toml`, `src/consolidate.rs`, `src/jev.rs`, `src/search/rerank.rs`, `src/setup.rs`, `src/hook.rs`). Their implementations, service versions, model weights and live behavior are not frozen here. This prevents conclusions about provider internals, host scheduling guarantees, actual host compliance with the skill, and end-to-end answer improvements. The target's adapters and host configuration writers remain included.

### Tracked top-level coverage

Every top-level tracked item is classified below. Included means within the analysis boundary, not every line already inspected. Named inspection is initial boundary tracing; the entire registered Git revision remains available to later jobs.

| Top-level item | Classification and material paths | Initial inspection and role | Limit or conclusion prevented |
|---|---|---|---|
| `.github/` | Included: `.github/workflows/ci.yml` | Read CI definition: lint and tests on Linux/macOS, reranking disabled. | CI configuration is not a retained successful CI run. |
| `.gitignore` | Included | Read exclusions for runtime journal/store, model cache, build output and credentials. | Ignored contents are not frozen evidence; no inference about a real user's stored memory or credentials. |
| `AGENTS.md` | Included | Read repository maintenance instructions and writeback convention. | Its referenced PRD is absent from the tracked tree; detailed requirements in that document cannot be established. |
| `Cargo.toml` | Included | Read binary/library entry points, dependencies and declared Rust requirement. | Dependency declarations do not establish dependency internals. |
| `Cargo.lock` | Included | Located as the dependency pin record; contents not yet inspected. | No initial claim about exact transitive versions or their behavior. This is available evidence, not an access gap. |
| `LICENSE` | Excluded from functional analysis | Legal license artifact, located but not inspected. | No independent legal/license interpretation. No memory-loop responsibility is excluded. |
| `README.md` | Included | Read product flow, commands, host setup, trust claims, configurations and evaluator contract. | Documentation claims remain declared intent unless separately traced in implementation. Referenced PRD is unavailable. |
| `skills/` | Included: `skills/mem/SKILL.md` | Read complete agent procedure for readiness, syncing, answering, changes, writeback and cleanup confirmation. Traced embedding/install in `src/setup.rs`. | No host-agent execution trace or compliance measurement supplied. |
| `src/` — drivers and integrations | Included: `main.rs`, `lib.rs`, `cli.rs`, `setup.rs`, `hook.rs`, `mcp.rs`, `http_serve.rs`, `shell.rs` | Read executable entry, CLI dispatch and selected producer/writeback/consolidation handlers; setup and hook implementations; transport-to-operation dispatch; library export surface searched. | Additional handler details remain available for analysis. Host applications themselves are external; their responsibility is not assigned to `mem`. |
| `src/` — production and retention | Included: `ingest.rs`, `journal.rs`, `consolidate.rs`, `change.rs`, `repo.rs`, `git.rs`, `paths.rs`, `fact.rs`, `entity.rs`, `controls.rs`, `checkpoint.rs`, `index.rs`, `validate.rs`, `error.rs` | Inspected Markdown adapter, journal bulk append/flush, batch consolidation and extractor prompt/input handling, immediate change and publisher, candidate validation; searched public journal/repository entry points. Remaining supporting type, path, Git wrapper, index and error details not yet inspected directly. | No execution, crash or concurrency experiment supplied. Coverage traces retention responsibilities but does not establish all advertised safety claims. |
| `src/` — maintenance | Included: `tidy.rs`, `erasure.rs` | Read cleanup prompt and selection/apply flow; erasure's current-state, journal, history and intent stages. | No observed cleanup or irreversible-erasure result supplied. |
| `src/` — consumption and model services | Included: `ops.rs`, `search/mod.rs`, `search/lexical.rs`, `search/journal.rs`, `search/rerank.rs`, `search/laya.rs`, `jev.rs` | Read shared operation dispatch, combined search/reload, task operation handlers and reranker fallback; searched search-module public surfaces; read JEV configuration/declared request boundary. Detailed scoring, local inference and task-file helpers remain available but not yet inspected. | No inference about real retrieval accuracy, latency, model weights or external service internals. |
| `src/` — evaluation | Included: `evaluation.rs`; CLI `evaluate` and `bench` dispatch in `cli.rs` | Read evaluator's rubric loading, lexical/reranked comparison and pass scoring. Located benchmark driver; its timing details not yet inspected. | No benchmark or rubric result is supplied; evaluator existence is not evidence of effectiveness. |
| `tests/` | Included: `tests/cli.rs`, `tests/recorded_search.rs`; inline source tests remain included | Read lifecycle fixture and assertions; searched store/writeback/hook tests; read recorded-search fixture and local-reranker checks. | Tests were not run. Recorded-search comments report a past session, but executable fixtures are not a complete observed session trace; local-model tests are marked ignored. |

No material shipped responsibility has been deliberately excluded. The missing PRD and unfrozen runtime stores, transcripts, provider responses, model weights and execution results limit conclusions, not access to the shipped memory loop. Uninspected available support files are identified separately from these gaps.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/jasonkneen/instinctual-memory` | 6acb13dc35765bf5ccfc87e445dd09c480f1c28a | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/instinctual-memory-workflow-af48437aa60c/related-systems/jasonkneen--instinctual-memory`. Implementation: repository tree, manifest, executable and CLI dispatch; selected backfill/ingest/consolidate/writeback handlers; journal append/flush, consolidation publication and extraction, validated immediate change, Git publication, shared retrieval/task operations, transport dispatch, setup/hooks, maintenance and evaluator. Doctrine/design: complete `README.md`, `AGENTS.md`, `skills/mem/SKILL.md`, extraction and cleanup prompts, CI definition. Reported operation: past-session framing in `tests/recorded_search.rs`, bounded by its retained fixtures. | Implementation: [entry](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/src/main.rs), [CLI](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/src/cli.rs), [consolidation](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/src/consolidate.rs), [operations](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/src/ops.rs), [hooks](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/src/hook.rs), [evaluation](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/src/evaluation.rs). Doctrine/design: [README](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/README.md), [skill](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/skills/mem/SKILL.md). Reported operation: [recorded checks](https://github.com/jasonkneen/instinctual-memory/blob/6acb13dc35765bf5ccfc87e445dd09c480f1c28a/tests/recorded_search.rs). Other initial paths are named in the coverage table above. | No checkout access gap. Referenced `PRD-portable-agent-memory.md` absent; prevents reading its requirements. No frozen host, provider, real store, model weights, successful test outputs or complete execution trace; prevents deployment, accuracy and causal-effect conclusions. Documentation and fixtures support intent/contracts or attributed operation, not observed-run or causal-experiment evidence. |
