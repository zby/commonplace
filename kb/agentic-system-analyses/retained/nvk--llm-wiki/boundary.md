---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "llm-wiki's shipped multi-runtime knowledge workflows, deterministic helpers and evaluation surfaces at commit 95a042c68998559305bc69ac8c482c4e1a415ad3."
run-id: AAS-2026-10-17-llm-wiki-a93f86f698d7-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "95a042c68998559305bc69ac8c482c4e1a415ad3"
analysis-cutoff: "2026-10-17"
evidence-tier: code-grounded
source:
  identity: https://github.com/nvk/llm-wiki
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-nvk--llm-wiki/related-systems/nvk--llm-wiki
  revision: 95a042c68998559305bc69ac8c482c4e1a415ad3
  sha256: null
---

# llm-wiki boundary

## Boundary and evidence

This run covers llm-wiki as a **memory/knowledge/context-engineering system**, not as an enclosing agent runtime. Its intended use is to ingest sources, retain synthesized knowledge, retrieve it for later questions, and maintain operational memory across agent sessions. The shipped instructions assign the semantic compilation and query work to the host model (SRC-1, `claude-plugin/skills/wiki-manager/SKILL.md`):

> You manage an LLM-compiled knowledge base. Source documents are ingested into `raw/`, then incrementally compiled into a wiki of interconnected markdown articles. Claude Code is both the compiler and the query engine — no Obsidian, no external tools.
> --- `claude-plugin/skills/wiki-manager/SKILL.md`

The boundary is **whole-system** for the repository's shipped knowledge-system responsibilities. It includes prompt-driven workflows, portable and runtime-specific entry points, local deterministic helpers, session capture and rehydration, state admission and export controls, package generation, and evaluation drivers. It does not reduce the target to its CLI helper. That helper explicitly distinguishes itself from the model-operated workflows (SRC-1, `scripts/llm-wiki`):

> This is not a replacement for the agentic /wiki workflows. It gives agents and
> humans a local command for the checks that can be done without an LLM.
> --- `scripts/llm-wiki`

### State-loop and entry-point trace

- **Produce and persist:** Claude's ingest command resolves a hub or local wiki, routes collections and datasets separately, and directs writes into the raw layer; the compile command reads sources, plans and updates articles, links them, and updates indexes. The shared compilation protocol specifies how retained raw sources become synthesized articles. These are model instructions, not proof that a host follows them (SRC-1, `claude-plugin/commands/ingest.md`, `claude-plugin/commands/compile.md`, `claude-plugin/skills/wiki-manager/references/compilation.md`).
- **Maintain and admit:** the full skill exposes lint, librarian, audit, archive, retraction, specialist, adapter, checkpoint, inventory and dataset workflows. The deterministic helper's parser dispatches local operations; its `run_lint` reads documents and applies structure, placement, source, index, link, coverage and freshness checks. These paths belong to the target even when a host supplies arguments and filesystem access (SRC-1, `claude-plugin/skills/wiki-manager/SKILL.md`, `scripts/llm-wiki`).
- **Reload and consume:** the full skill's query workflow reads indexes, exact articles and links and supports resume. Query-lite provides a separate read-only, index-first evidence route. Codex and OpenCode ship their own full-skill entry points; the generic Pi launcher loads the compact profile into an external Pi process with read/search tools. The DS4 launcher additionally supplies provider settings and a shipped extension that modifies the prompt and provider request (SRC-1, `claude-plugin/skills/wiki-manager/SKILL.md`, `claude-plugin/skills/wiki-manager/references/query-lite.md`, `plugins/llm-wiki/skills/wiki/SKILL.md`, `plugins/llm-wiki-opencode/skills/wiki-manager/SKILL.md`, `scripts/pi-wiki-query`, `scripts/pi-ds4-wiki-query`, `profiles/ds4/pi-query-tools.ts`).
- **Retain session context:** Codex hook declarations invoke the bundled session helper. Its hook path normalizes and queues events, updates state, optionally writes a digest, rebuilds indexes and can return rehydration context. `build_rehydrate_context` selects retained states with digests; `run_promote` reads a digest and writes an explicit topic raw note. The canonical and bundled session helpers have identical byte hashes at inspection, as do the canonical CLI and its three packaged copies (SRC-1, `plugins/llm-wiki/hooks/hooks.json`, `scripts/llm-wiki-session`, `plugins/llm-wiki/hooks/llm_wiki_session.py`, `claude-plugin/bin/llm-wiki`, `plugins/llm-wiki/bin/llm-wiki`, `plugins/llm-wiki-opencode/bin/llm-wiki`).

The session-consumption code supplies a useful boundary on memory authority (SRC-1, `scripts/llm-wiki-session`):

> lines.append("Do not treat session digests as canonical topic knowledge until promoted into a topic wiki.")
> --- `scripts/llm-wiki-session`

### Top-level coverage

The tracked tree was enumerated before classification. Every top-level tracked entry appears below. “Included” establishes functional scope, not a claim that every file or branch has already been read. Initial inspection traces the material state loop above; remaining detail is available at the same frozen commit, not an access gap.

| Top-level entry | Status | Material paths and role | Inspection boundary or conclusion prevented |
|---|---|---|---|
| `.agents/` | Included | `.agents/plugins/marketplace.json` routes installation to the Codex package. | Manifest inspected; no installed-host behavior observed. |
| `.claude-plugin/` | Included | `.claude-plugin/marketplace.json` routes installation to `claude-plugin/`. | Manifest inspected; marketplace availability is not established. |
| `.claude/` | Excluded | `.claude/release-checklist.md` is repository release administration. | Deliberate exclusion; no conclusion about release execution or publishing compliance. |
| `.gitignore` | Excluded | Repository tracking policy. | Deliberate exclusion; no claim about ignored local artifacts or their retention. |
| `AGENTS.md` | Included | Portable single-file knowledge protocol; architecture, raw/article formats and workflows. | Architecture and format sections searched; detailed portable behavior remains to be inspected. |
| `CLAUDE.md` | Excluded | Contributor testing, synchronization and release guidance. | Searched for repository responsibilities; excluded from product behavior. No claim that maintainers followed its development process. |
| `LICENSE` | Excluded | Legal distribution terms. | Deliberate exclusion; no licensing assessment. |
| `README.md` | Included | Installation, runtime architecture and public usage contract. | Installation and architecture inspected; changelog statements are declarations, not observed runs. |
| `benchmarks/` | Included | `benchmarks/README.md`, `cases/wiki-query.jsonl`, `cases/ds4-wiki-query.jsonl`, `helpers/pi-payload-metrics.ts`: query cases and measurement support. | README and tree inspected; case and metric internals not yet read. No measured efficiency or quality conclusion. |
| `claude-plugin/` | Included | `commands/ingest.md`, `commands/compile.md`, remaining `commands/`; `skills/wiki-manager/SKILL.md` and `references/`; `.claude-plugin/plugin.json`; `bin/llm-wiki`. Primary prompt workflows, maintenance/admission instructions and bundled checks. | Full-skill workflow dispatch, ingest/compile entry paths, shared compile/query protocols and helper sections inspected. Other reference bodies remain available for later detailed analysis; they are not excluded. |
| `plugins/` | Included | Codex `llm-wiki/skills/wiki/`, `skills/wiki-query/`, `hooks/hooks.json`, `hooks/llm_wiki_session.py`, `bin/llm-wiki`, `.codex-plugin/plugin.json`; OpenCode `llm-wiki-opencode/skills/`, shared-reference link and `bin/llm-wiki`. Package consumers and operational-memory integration. | Runtime-specific full-skill entries and Codex hook declaration inspected; bundled helper equivalence checked. Package metadata and remaining generated reference detail are not yet inspected. |
| `profiles/` | Included | `query-lite/SKILL.md`, `ds4/README.md`, `ds4/pi-query-tools.ts`: compact retrieval and provider-specific request shaping. | Canonical query protocol and DS4 extension inspected; no external provider run inspected. |
| `scripts/` | Included | `llm-wiki`, `llm-wiki-session`; `pi-wiki-query`, `pi-ds4-wiki-query`; `benchmark-token-efficiency`; bootstrap, sync and verification scripts. Includes state helpers, host launchers, package maintenance and shipped evaluators. | Helper dispatch/lint, session capture/reload/promotion, both Pi launchers, benchmark fixture-reader code and synchronization references inspected. Additional operation internals remain available; no helper execution performed. |
| `tests/` | Included | `README.md`, `promptfooconfig.yaml`, `evals/assertions/`, `fixtures/golden-wiki/`, defect and fake-provider fixtures, `test-*.sh`, `budgets/token-budgets.json`, `ci/plugin-tests.yml`. Structural, behavioral, packaging and query-evaluation surfaces. | Test contract and behavioral configuration sampled; full tree enumerated. Fixtures/assertions and shell bodies not exhaustively inspected or executed; no pass-rate or robustness claim. |

### External boundary and evidence limits

Claude Code, Codex, OpenCode, Pi, model providers, web/MCP services, user wiki hubs, private adapters and user-owned specialists are external dependencies. The repository's prompts, launchers, hook declarations and adapter/checkpoint controls remain included. Host scheduling, model inference, permissions enforcement, tool execution and provider transport are not attributed to llm-wiki merely because its instructions request them (SRC-1, `README.md`, `scripts/pi-wiki-query`, `scripts/pi-ds4-wiki-query`, `plugins/llm-wiki/hooks/hooks.json`).

Private adapter implementations, credentials, live data planes and personal specialist packages are not established by this source. Their absence prevents conclusions about provider-specific execution, real data handling and specialist effectiveness, not inspection of the shipped framework contract (SRC-1, `claude-plugin/skills/wiki-manager/SKILL.md`). User hubs and genuine retained session histories are likewise not supplied; synthetic fixtures and evaluation definitions cannot establish real cross-session usefulness or adherence to the prompts (SRC-1, `tests/README.md`, `scripts/llm-wiki-session`).

The overall tier is **code-grounded** because executable helper, launcher, hook and evaluator paths are inspectable. Semantic research, compilation, audit and querying remain primarily **doctrine/design** evidence unless later records establish an executable mechanism. The benchmark's fixture tool serves retained wiki text to its caller; it is an included shipped consumer, not an excluded application (SRC-1, `scripts/benchmark-token-efficiency`). Evaluation code and configured rubrics establish proposed checks, not observed results. No target, tests, examples, model calls or services were executed for this boundary.

The frozen revision is **95a042c68998559305bc69ac8c482c4e1a415ad3**. The applicability cutoff is **2026-10-17**, the supplied run date, not a claim about the commit's publication time. Checkout HEAD matched the acquired pin and its working-tree status was clean. Evidence is limited to this commit; moving README URLs, later releases and external linked repositories are not additional sources.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/nvk/llm-wiki` | 95a042c68998559305bc69ac8c482c4e1a415ad3 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-20-nvk--llm-wiki/related-systems/nvk--llm-wiki`. Implementation: CLI/helper sections, session hook/state/index/rehydration/promotion paths, generic and DS4 launchers, DS4 extension, benchmark fixture reader, packaged-copy hashes and sync-script references. Doctrine/design: README installation/architecture, full-skill workflow contract, ingest/compile commands, compilation/query-lite protocols, runtime-specific skill entries, test README and behavioral-eval configuration. Tree and scoped architecture/reference searches establish initial coverage, not exhaustive reading. | Implementation: [CLI](https://github.com/nvk/llm-wiki/blob/95a042c68998559305bc69ac8c482c4e1a415ad3/scripts/llm-wiki), [session helper](https://github.com/nvk/llm-wiki/blob/95a042c68998559305bc69ac8c482c4e1a415ad3/scripts/llm-wiki-session), [Pi launcher](https://github.com/nvk/llm-wiki/blob/95a042c68998559305bc69ac8c482c4e1a415ad3/scripts/pi-wiki-query), [evaluator](https://github.com/nvk/llm-wiki/blob/95a042c68998559305bc69ac8c482c4e1a415ad3/scripts/benchmark-token-efficiency). Doctrine/design: [full skill](https://github.com/nvk/llm-wiki/blob/95a042c68998559305bc69ac8c482c4e1a415ad3/claude-plugin/skills/wiki-manager/SKILL.md), [compile command](https://github.com/nvk/llm-wiki/blob/95a042c68998559305bc69ac8c482c4e1a415ad3/claude-plugin/commands/compile.md), [query protocol](https://github.com/nvk/llm-wiki/blob/95a042c68998559305bc69ac8c482c4e1a415ad3/claude-plugin/skills/wiki-manager/references/query-lite.md), [test contract](https://github.com/nvk/llm-wiki/blob/95a042c68998559305bc69ac8c482c4e1a415ad3/tests/README.md). | No checkout access gap encountered. External hosts/providers, private integrations, personal hubs and run traces are not supplied. Implementation supports source-level behavior only; doctrine/design supports intended model workflows only. No observed-run or causal-experiment layer is registered; effectiveness, reliability, actual costs and adherence remain unestablished. |
