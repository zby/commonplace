---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "MentisDB's shipped memory engine, skill registry, service surfaces, clients and operating instructions at commit 4c9b95041da68c5a26dece9f8776ff54b05b910c."
run-id: AAS-2026-10-14-mentisdb-a8b5903ae3e2-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "4c9b95041da68c5a26dece9f8776ff54b05b910c"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/cloudllm-ai/mentisdb
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/mentisdb-a8b5903ae3e2/related-systems/cloudllm-ai--mentisdb
  revision: "4c9b95041da68c5a26dece9f8776ff54b05b910c"
  sha256: null
---

# MentisDB boundary

## Boundary and evidence

This run analyses MentisDB as a **memory/knowledge/context-engineering system**, not as an enclosing agent runtime. The intended use is to explain how its shipped components retain agent memories and instruction bundles, maintain that state, and return it for later use. The boundary is **whole-system** for the repository's memory system: the Rust library, daemon and CLI, HTTP and stdio MCP surfaces, operator interfaces, integration writers, Python client and LangChain adapter, shipped memory instructions, examples and evaluators all belong to the target. Repository callers are not excluded merely because they call its API.

The declared product supports this classification (SRC-1, `README.md`):

> MentisDB is a **durable semantic memory engine and versioned skill registry** for AI agents — a persistent, hash-chained brain that survives context resets, model swaps, and team turnover.
> --- `README.md`

The initial entry-point trace establishes the following functional coverage. These are implementation and instruction boundaries, not claims that the paths were executed:

- **Produce and admit retained state:** `Cargo.toml` declares the `mentisdb` executable at `src/bin/mentisdb.rs`; its `main` dispatches daemon, headless, stdio, combined and CLI modes. `src/server.rs` maps REST and MCP requests to service operations. Its append operation builds a `ThoughtInput` and calls the chain append path; `src/lib.rs` validates references, constructs the linked record, writes through the storage adapter and updates indexes. The Python client's append method posts to the same REST surface. SRC-1, `Cargo.toml`, `src/bin/mentisdb.rs`, `src/server.rs`, `src/lib.rs`, `pymentisdb/client.py`.
- **Reload and maintain state:** `MentisDb::open_with_storage` loads thoughts and registries and rebuilds indexes and invalidation state. Maintenance includes relation-driven invalidation, optional append deduplication, summary candidate selection, sidecar rebuilding, branch and merge surfaces, skill version persistence, and backup/restore. These are included responsibilities; this boundary does not settle their detailed correctness. SRC-1, `src/lib.rs`, `src/search/mod.rs`, `src/server.rs`, `src/skills.rs`, `src/backup.rs`, `src/cli/mod.rs`.
- **Consume retained state:** ranked search combines available retrieval signals; the service's recent-context operation returns a catch-up prompt. The LangChain adapter retrieves records and formats them into a named prompt variable. The shipped Python example explicitly writes conversation messages and then reloads memory variables. This adapter and example are part of the target, not an excluded host application. SRC-1, `src/lib.rs`, `src/server.rs`, `pymentisdb/langchain.py`, `examples/langchain_memory_example.py`.
- **Guide model-operated memory work:** the daemon embeds `MENTISDB_SKILL.md`, and both the skill and cookbook instruct agents to load prior state, search before appending, distill durable information and checkpoint before session loss. These instructions are included as doctrine/design, not as enforced scheduling or observed compliance. SRC-1, `src/bin/mentisdb.rs`, `src/server.rs`, `MENTISDB_SKILL.md`, `docs/cookbook/cookbook-1-0-operator-playbook.html`, `docs/cookbook/cookbook-2-2-cross-session-continuity.html`.
- **Evaluate the system:** Rust tests and Criterion benchmarks exercise storage, search, transport and skill responsibilities; the shipped LongMemEval, LoCoMo and ConvoMem drivers ingest conversation records and evaluate retrieval against evidence. Evaluator code is included, but no benchmark was run for this analysis. SRC-1, `tests/search_ranked_eval_tests.rs`, `tests/startup_migration_tests.rs`, `benches/search_ranked.rs`, `benches/thought_chain.rs`, `lme-benches/longmemeval_bench.py`, `lme-benches/convomem_bench.py`, `locomo-benches/locomo_bench.py`.

Minimum passages distinguish the shipped memory loop from an API-only boundary. The core skill prescribes later-session consumption (SRC-1):

> 5. `mentisdb_recent_context` → load where you left off
> 6. Write `Summary` with `role: Checkpoint`
> --- `MENTISDB_SKILL.md`

The Python adapter converts retrieved state into a prompt variable (SRC-1):

> formatted = self._format_messages(messages)
> return {self.memory_key: formatted}
> --- `pymentisdb/langchain.py`

The implementation also serves model calls for optional extraction. This does not make MentisDB the enclosing task agent. Extraction produces candidate records, while the separate append surface admits durable state (SRC-1, `src/llm.rs`, `src/server.rs`):

> //! LLM output is **untrusted**. The returned [`ExtractionResult`] contains
> //! [`ThoughtInput`] records that callers must review, validate, and
> //! optionally sign before appending to a chain.
> --- `src/llm.rs`

The preceding passage is a module-level contract, not evidence that a caller actually reviews the output. The inspected extraction service returns the extracted records without calling its append operation. External hosts remain responsible for task execution, deciding when to call memory tools, and using returned context in their own model conversations. The integration writers configure host MCP connections; they are included, but the implementations of Codex, Claude Code, OpenCode and other hosts are not frozen here. That exclusion prevents conclusions about host scheduling, automatic memory-tool use, instruction obedience or end-to-end task improvement. SRC-1, `src/server.rs`, `src/integrations/targets/codex.rs`, `src/integrations/targets/claude_code.rs`, `src/integrations/targets/opencode.rs`, `docs/cookbook/cookbook-1-0-operator-playbook.html`.

External dependencies include Rust and Python packages, OpenAI-compatible extraction services, embedding implementations/model assets, host MCP clients and webhook destinations. Package declarations and MentisDB's adapters are evidence; dependency implementations, provider behavior and remote services are not separate frozen sources. This prevents verification of provider quality, remote delivery reliability or dependency internals from this source alone. SRC-1, `Cargo.toml`, `src/llm.rs`, `src/search/fastembed_provider.rs`, `src/webhooks.rs`, `pymentisdb/langchain.py`.

### Repository coverage

The inventory is the tracked top-level tree at the reviewed commit. Every top-level file or directory is classified below. **Included** means eligible evidence within the functional boundary, not a claim of exhaustive inspection. Initial inspection used full reads for short contracts and adapters, bounded reads for large modules, and searches for entry points and responsibility paths. Files not yet read are not access gaps. No material shipped memory path is deliberately omitted from the functional boundary.

All rows refer to SRC-1. Directory rows name material paths; remaining detail can be inspected at the same commit without creating another source identity.

| Top-level tracked entry | Classification | Role and initial coverage | Exclusion limit or inspection limit |
|---|---|---|---|
| `.env.example` | Included | Daemon/provider configuration; searched alongside source configuration surfaces. | Full variable contract not yet inspected. |
| `.github/` | Excluded | Build, clippy, test and publish workflows; funding metadata. | No CI execution or release-pipeline assurance. |
| `.gitignore` | Excluded | Checkout hygiene. | No conclusions about developer-local ignored state. |
| `AGENTS.md` | Included | Read standalone-crate scope and generic memory API design requirements. | Doctrine, not agent compliance evidence. |
| `Cargo.lock` | Included | Dependency revision metadata. | Not yet inspected; dependency internals remain outside this source. |
| `Cargo.toml` | Included | Read crate identity, feature gates, dependencies, binary and benchmark entry points. | Configuration establishes available build surfaces, not a successful build. |
| `LICENSE` | Excluded | Legal licensing. | No licensing assessment. |
| `MENTISDB_SKILL.md` | Included | Read full startup, search-before-write, correction, checkpoint, handoff and skill-registry instructions. Embedded in binary and server. | Prescribed model behavior, not observed operation. |
| `Makefile` | Included | Development and evaluation entry-point support; initial search only. | Detailed recipes not yet inspected. |
| `README.md` | Included | Read product declaration and installation/CLI introduction. | Remaining sections available but not yet inspected; advertised outcomes are not verified outcomes. |
| `ROADMAP.md` | Included | Planned development, distinct from shipped behavior. | Not yet inspected; cannot establish implementation. |
| `WHITEPAPER.md` | Included | Source-native design account. | Not yet inspected; theory cannot substitute for executable behavior. |
| `WHITEPAPER.pdf` | Included | Published rendering of the design account. | Not yet inspected. |
| `WHITEPAPER.tex` | Included | Authored design publication source. | Not yet inspected. |
| `benches/` | Included | `thought_chain.rs`, `search_ranked.rs`, search baselines, HNSW scale/comparison, skill registry and HTTP concurrency benchmarks; entry points searched in the first two. | Code, not fresh measurement; remaining benchmark bodies not yet inspected. |
| `build-whitepaper.sh` | Excluded | Publication build helper. | No reproducibility claim for the paper build. |
| `changelog.txt` | Included | Source-native release history. | Not yet inspected; history alone does not establish present behavior. |
| `code-performance-reviewer.md` | Included | Shipped project-maintenance instruction. | Not yet inspected; not evidence of a completed performance review. |
| `data/` | Included | `longmemeval_oracle.json`, tracked evaluator input referenced by the driver. | Dataset contents not yet inspected; no claim about benchmark representativeness. |
| `docs/` | Included | Read `cookbook/cookbook-1-0-operator-playbook.html` and `cookbook/cookbook-2-2-cross-session-continuity.html`; inventory also includes memory protocol, ingestion, ranked search, integrations, backup, deployment, extraction/federation designs, release reports and source-native evaluations. | Other documents not yet inspected. Native comparisons are attributed claims, not independent cross-system verification. Linked live pages are not additional frozen evidence. |
| `examples/` | Included | Read `langchain_memory_example.py`, which appends conversation messages and loads memory for later use. | Simulated example, not an observed task-agent run. |
| `lme-benches/` | Included | Inspected ingest/evaluate paths in `longmemeval_bench.py` and `convomem_bench.py`; `README.md`, `run_longmemeval.sh` and `full_bench.sh` are supporting evaluator instructions/wrappers. | Wrappers not yet inspected. No execution evidence or independent confirmation of reported scores. |
| `locomo-benches/` | Included | Inspected evaluation in `locomo_bench.py`; `README.md` and `run_locomo.sh` support dataset setup and invocation. | Ingest detail and wrappers not yet inspected; external dataset not acquired. |
| `logo.svg` | Excluded | Branding. | No visual-design assessment. |
| `pymentisdb/` | Included | Read `langchain.py`; inspected `client.py` append/search calls. `types.py`, `__init__.py`, `pyproject.toml`, `README.md` and `tests/test_client.py` support serialization, packaging and contracts. | Remaining client/type/test detail not yet inspected. No conclusion about LangChain runtime compatibility from execution. |
| `scripts/` | Included | `extract_cookbook_examples.py` is the shipped cookbook-example test extraction path; searched its generated-test handling. | Full extractor not yet inspected; no compilation result. |
| `skills/` | Included | Read `README.md`; tracked engineering, concurrency, benchmarking, cookbook-test and release skills belong to repository maintenance. Memory operating instructions also reside in the root core skill and cookbook. | Individual project-maintenance skill bodies not yet inspected. Index references to absent files do not supply their contents. |
| `src/` | Included | Traced `bin/mentisdb.rs`, `cli/mod.rs`, `server.rs`, `lib.rs`, `llm.rs`, `skills.rs`, `backup.rs`, `search/mod.rs`, and integration writers. `search/` contains lexical/vector/graph, sidecar, summary, expansion and provenance paths. Searches covered `dashboard.rs`, `dashboard_static/index.html`, `tui.rs`, `webhooks.rs` and embedding provider entry points; `auth.rs`, `paths.rs`, remaining CLI/integration modules and dashboard login assets remain eligible operational support. | This is initial responsibility coverage, not an exhaustive code audit; security, UI, storage and retrieval details require further inspection. |
| `start_mentisdb` | Included | Read launcher: configuration hints and `cargo run --bin mentisdb`. | Launcher does not prove a successful startup. |
| `tests/` | Included | Searched `search_ranked_eval_tests.rs` and `startup_migration_tests.rs`; inventory covers memory/storage, invalidation, extraction, summary, vector/graph retrieval, server/transport, skills, backup, setup, dashboard and auth tests. | Test specifications are available; no tests executed and remaining test bodies not yet inspected. |

The applicability cutoff is **2026-10-14**. Evidence is frozen at commit **4c9b95041da68c5a26dece9f8776ff54b05b910c**, not at a mutable default branch or the latest package release. The acquired checkout's HEAD matched that pin and its tracked working tree was clean. No other repository, live documentation version, installed package or execution trace is registered.

The overall tier is **code-grounded**. Inspected source supports implementation-path explanations; shipped skills and documentation support doctrine/design. No observed-run or causal-experiment evidence was established. Thus the boundary supports an account of mechanisms and intended use, not demonstrated cross-session task success, throughput, benchmark superiority or improved agent behavior. For example, the LongMemEval evaluator describes its metric as retrieval recall rather than generated-answer quality (SRC-1):

> Measures retrieval recall (R@k): for each of 500 questions, does the gold
> evidence turn appear in the top-k thoughts returned by mentisdb ranked-search?
> --- `lme-benches/longmemeval_bench.py`

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/cloudllm-ai/mentisdb` | 4c9b95041da68c5a26dece9f8776ff54b05b910c | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/mentisdb-a8b5903ae3e2/related-systems/cloudllm-ai--mentisdb`. Implementation: initial entry-point and consumer traces through `Cargo.toml`, `src/bin/mentisdb.rs`, `src/cli/mod.rs`, `src/server.rs`, `src/lib.rs`, `src/llm.rs`, `src/search/mod.rs`, `src/skills.rs`, `src/backup.rs`, `src/integrations/targets/codex.rs`, `src/integrations/targets/claude_code.rs`, `src/integrations/targets/opencode.rs`, `pymentisdb/client.py`, `pymentisdb/langchain.py`, `examples/langchain_memory_example.py`, `start_mentisdb`, and evaluator functions in `lme-benches/longmemeval_bench.py`, `lme-benches/convomem_bench.py`, `locomo-benches/locomo_bench.py`; supporting bounded searches listed in the coverage table. Doctrine/design: `README.md` introduction, full `AGENTS.md`, `MENTISDB_SKILL.md`, `skills/README.md`, and the two read cookbook chapters. | Implementation: [binary dispatch](https://github.com/cloudllm-ai/mentisdb/blob/4c9b95041da68c5a26dece9f8776ff54b05b910c/src/bin/mentisdb.rs), [chain state](https://github.com/cloudllm-ai/mentisdb/blob/4c9b95041da68c5a26dece9f8776ff54b05b910c/src/lib.rs), [services](https://github.com/cloudllm-ai/mentisdb/blob/4c9b95041da68c5a26dece9f8776ff54b05b910c/src/server.rs), [prompt-facing adapter](https://github.com/cloudllm-ai/mentisdb/blob/4c9b95041da68c5a26dece9f8776ff54b05b910c/pymentisdb/langchain.py), [retrieval evaluator](https://github.com/cloudllm-ai/mentisdb/blob/4c9b95041da68c5a26dece9f8776ff54b05b910c/lme-benches/longmemeval_bench.py). Doctrine/design: [core skill](https://github.com/cloudllm-ai/mentisdb/blob/4c9b95041da68c5a26dece9f8776ff54b05b910c/MENTISDB_SKILL.md), [operator loop](https://github.com/cloudllm-ai/mentisdb/blob/4c9b95041da68c5a26dece9f8776ff54b05b910c/docs/cookbook/cookbook-1-0-operator-playbook.html). Other cited code spans are commit-relative anchors in this same Git source. | No checkout access gap established. External hosts, dependency implementations, provider/model assets and untracked runtime state are not frozen evidence; external evaluator datasets except the tracked LongMemEval input are not captured. No observed runs or interventions were supplied or performed. These limits prevent host-behavior, provider-quality, measured-performance and end-to-end efficacy conclusions. Available but unread files are inspection limits, not access gaps. |
