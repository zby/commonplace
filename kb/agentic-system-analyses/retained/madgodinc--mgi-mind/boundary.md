---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "MGI-Mind's shipped memory system, clients, usage protocol and evaluators at a8defc36f7d0bcd5108714763a12625a0eda0868."
run-id: AAS-2026-11-08-mgi-mind-e0f02081480f-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: a8defc36f7d0bcd5108714763a12625a0eda0868
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/madgodinc/mgi-mind
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/mgi-mind-2cc7fc8c894a/related-systems/madgodinc--mgi-mind
  revision: a8defc36f7d0bcd5108714763a12625a0eda0868
  sha256: null
---

# MGI-Mind boundary

## Boundary and evidence

MGI-Mind is in scope as a memory/knowledge/context-engineering system for AI assistants, not as an enclosing assistant runtime. Its intended use is to retain notes, structured facts, procedures, skills and session context, then return relevant material to assistants across sessions. The boundary covers the whole shipped system: Rust executable, CLI, MCP and HTTP surfaces, state admission and maintenance, session/context rendering, Python clients, integration drivers and prompts, deployment wrappers, and evaluators. The classification follows the shipped entry point and its consumers, rather than treating the server API as the entire product (SRC-1, `Cargo.toml`, `src/main.rs`, `src/mcp.rs`, `src/cli.rs`, `docs/integrations/openai_agents.py`).

> Local long-term memory for AI assistants. One Rust binary, a local Qdrant
> vector database, local ONNX models. Speaks MCP, so Claude Code and other
> assistants read and write memory on their own. Also a normal CLI.
> --- `README.md`

This is a `whole-system` boundary relative to MGI-Mind's shipped responsibilities, not a claim to include the internals of every host framework. The examples that construct agents and feed recall results back to models are included. Their third-party framework implementations and model services are external dependencies. In particular, the shipped OpenAI Agents example registers recall/remember functions, constructs an agent with a memory-use instruction and invokes it twice; it is not excluded merely because it calls a client API (SRC-1, `docs/integrations/openai_agents.py`).

> def recall(query: str) -> str:
>     """Search the agent's long-term memory for anything relevant to a query."""
>     return str(mem.search(query, tier=2))
> --- `docs/integrations/openai_agents.py`

> def remember(fact: str) -> str:
>     """Save a durable fact to long-term memory so future runs can recall it."""
>     return str(mem.add(fact))
> --- `docs/integrations/openai_agents.py`

### Frozen evidence and limits

The sole frozen source is `https://github.com/madgodinc/mgi-mind` at full commit `a8defc36f7d0bcd5108714763a12625a0eda0868`; the checkout's HEAD was checked against the acquired revision. This commit is the reviewed boundary. The applicability cutoff is 2026-11-08, the supplied run date. Later commits, mutable links, release downloads, other branches and external repositories are not evidence in this run. The source object above preserves acquisition's identity, kind, path, revision and digest unchanged.

The overall evidence tier is code-grounded. Source inspection establishes wiring and executable mechanisms, not successful operation in an installed environment. No target commands, examples, tests or model calls were executed. Repository-authored benchmark and audit prose is attributable reporting, not independent verification. Retained benchmark files can supply run evidence only after their actual contents and conditions are inspected; their presence alone establishes no score or causal effect (SRC-1, `benchmark/README.md`, `src/bench.rs`, `src/bench_stale.rs`).

External dependencies include Qdrant, ONNX Runtime, embedding/reranking model artifacts, optional llama-server and extractor weights, Python HTTP transport, and the host agent frameworks and their model providers. Their integration code and configuration are included; their upstream implementations, installed versions and live behavior are not. This prevents conclusions about complete host scheduling, actual prompt compliance, production reliability, downloaded artifact behavior, or end-to-end answer quality. The optional extractor is included as a feature-gated path, not assumed active in the default build (SRC-1, `Cargo.toml`, `src/extractor.rs`, `docs/integrations/langgraph.py`, `clients/python/mgimind/_client.py`).

> default = []
> --- `Cargo.toml`

> extractor = []
> --- `Cargo.toml`

### Initial loop trace

The initial inspection covered the repository tree and these material paths. It is boundary establishment, not an exhaustive mechanism review of every function.

- **Entry and service ownership.** `Cargo.toml` names `src/main.rs` as the `mgimind` binary; main parses CLI arguments and calls `cli::run`. CLI dispatch selects MCP or HTTP serving, direct writes/reads, session handling, maintenance and benchmarks. MCP initializes configuration and Qdrant access and starts the doubt-window background task; HTTP has its own route allowlist and token/scope state. Do not infer identical service lifecycle behavior merely because both surfaces reach shared storage (SRC-1, `Cargo.toml`, `src/main.rs`, `src/cli.rs`, `src/mcp.rs`, `src/http_api.rs`).
- **Produce and admit.** MCP `mind_add` calls authored storage directly. `mind_ingest` accepts agent-provided candidates or raw text and calls the ingest pipeline. Ingest checks relevance/novelty, handles recoverable quarantine and reassertion, and dispatches memory, fact and procedure writes. The stored-memory path checks library registration, scans for secrets, chunks, embeds and upserts into Qdrant. These are distinct entry paths; the boundary does not assume every write passes the same relevance gate (SRC-1, `src/mcp.rs`, `src/ingest.rs`, `src/storage.rs`).
- **Retain and revise.** The fact core serializes writes, consults prior triple state and uses the validity-model path. Procedure and skill modules expose write/recall/outcome operations over storage; outcome recording writes external signals. Consolidation reads memory metadata and neighbors for deduplication and coldness handling; Markdown reconciliation calls ordinary storage mutations. Transcript ingestion is another shipped input path, not an external application responsibility (SRC-1, `src/knowledge.rs`, `src/procedure.rs`, `src/skill.rs`, `src/outcome.rs`, `src/consolidate.rs`, `src/md_reconcile.rs`, `src/session_ingest.rs`).
- **Optional model extraction.** Accepted ingested memories can enqueue extraction only under the extractor feature and an installed server. The bounded worker calls `extract_facts` and sends resulting triples to the fact API. This path belongs inside the boundary even though default features do not activate it (SRC-1, `src/ingest.rs`, `src/extractor.rs`, `Cargo.toml`).
- **Reload and consume.** Search embeds a query, records recent query activity, runs dense/sparse retrieval and optionally reranks results before rendering. `mind_context` calls `cli::build_context`, which loads prior session text, visible facts, pinned blocks, the skill catalogue, library inventory and quarantine information. Session start/end write local files; last-session retrieval reads them. Python integration drivers turn persisted search results into model-visible tool outputs and offer remember tools for later writes (SRC-1, `src/storage.rs`, `src/mcp.rs`, `src/cli.rs`, `src/session.rs`, `clients/python/mgimind/_client.py`, `docs/integrations/openai_agents.py`, `docs/integrations/langgraph.py`, `docs/integrations/pydantic_ai.py`).
- **Evaluate.** Retrieval benchmarking ingests haystack sessions into a benchmark library, searches them and compares returned session identifiers with gold identifiers. Procedural benchmarking learns fixes and checks recall positions. Retrieval-policy benchmarking consumes saved results rather than observing a real no-policy agent. The pinned STALE adapter describes itself as a scaffold with a working harness on another branch; that branch is not acquired. Tests are source evidence of intended checks, not executed results in this run (SRC-1, `src/bench.rs`, `src/bench_procedural.rs`, `src/bench_policy.rs`, `src/bench_stale.rs`, `tests/cli_integration.rs`, `tests/http_integration.rs`).

The shipped operating manual is part of the memory loop. It asks the assistant to extract durable candidates, search before relying on past information and close sessions with summaries. It also explicitly says the manual is not automatically loaded by clients. Thus repository documentation supplies a consumption protocol, not proof that a deployed assistant follows it (SRC-1, `AI_INSTRUCTIONS.md`).

> AI_INSTRUCTIONS.md is not auto-loaded by any client; wiring in the MCP server
> only gives the tools, not the habit of using them. Before finishing the install,
> append (never overwrite) a short pointer to this file's protocol into whichever
> rules file the client reads every session:
> --- `AI_INSTRUCTIONS.md`

> You are the memory's extractor. As you work, when a few things accrue that are worth
> keeping, send them in one `mind_ingest` call with a `candidates` array.
> --- `AI_INSTRUCTIONS.md`

The integration guide calls its examples illustrations rather than maintained packages. Hermes explicitly labels its host-side registration signatures unverified. These limits prevent claiming tested cross-framework compatibility; they do not justify removing the shipped callers from the boundary (SRC-1, `docs/integrations/README.md`, `docs/integrations/hermes.py`).

> Every example targets the live HTTP server above; it assumes `MGIMIND_URL` and
> `MGIMIND_TOKEN` are set and the agent's own model key (`ANTHROPIC_API_KEY` or
> `OPENAI_API_KEY`) is present. They are illustrations, not a maintained package.
> Copy the dozen lines you need.
> --- `docs/integrations/README.md`

### Top-level tracked coverage

Every top-level tracked file or directory is classified below. “Included” makes a path available for later analysis at this commit; it does not claim every byte was inspected. “Not yet inspected” describes available evidence, never an access gap. The material state loop above was traced before selecting `whole-system`. All source-dependent roles in this table refer to SRC-1.

| Top-level path | Classification and role | Initial inspection and limits / conclusion prevented |
|---|---|---|
| `src/` | Included: executable and all state-producing, admission, maintenance and consumption mechanisms. | Read `main.rs`; bounded executable sections of `cli.rs`, `mcp.rs`, `http_api.rs`, `storage.rs`, `ingest.rs`, `knowledge.rs`, `session.rs`, `consolidate.rs`, `extractor.rs`, `bench.rs`, `bench_procedural.rs`; searched `procedure.rs`, `skill.rs`, `outcome.rs`, `md_reconcile.rs`, `session_ingest.rs`, `doubt.rs`. `activity.rs`, `access.rs`, `audit.rs`, `config.rs`, `confidence.rs`, `duel.rs`, `embedder.rs`, `reranker.rs`, `relevance.rs`, `retrieval_policy.rs`, `provenance.rs`, `relibrary.rs`, migration/install modules, secrets/vault, viewer/pulse/frontend and remaining helper bodies remain included but need detailed inspection for mechanism claims. No unavailable shipped path identified. |
| `clients/` | Included: Python synchronous/asynchronous HTTP callers, package and tests. | Inspected `clients/python/mgimind/_client.py` response/transport setup; `__init__.py`, package metadata and `tests/test_client.py` enumerated but not yet read. No claim of tested SDK correctness. |
| `docs/` | Included: shipped integration drivers, prompts, design records, demo and historical design context. | Read `integrations/README.md`, all five Python examples and `openclaude.md`; source-native `design/`, ADRs, `PHASE_D2_D6.md`, blog posts and demo files remain available but not yet inspected. Host implementations are external, not the shipped examples. |
| `benchmark/` | Included: evaluator corpora and retained results. | Read `README.md`; enumerated `datasets/procedural-*.jsonl` and dated `results/` logs/raw JSON, including the partial STALE result directory. Raw result contents not yet inspected: no score or current-revision efficacy is established here. |
| `tests/` | Included: CLI/MCP/storage and HTTP integration evaluators. | Read setup/gating portions of `cli_integration.rs` and `http_integration.rs`; assertions require further inspection. Tests were not run. |
| `scripts/` | Included: evaluator preparation and reproduction tooling. | Read headers/setup of `local-bench-gpu.sh` and `scrape_procedural_dataset.py`; remaining bodies not yet inspected. No successful reproduction claim. |
| `docker/` | Included: deployment/service lifecycle and optional CUDA packaging. | Read `entrypoint.sh`, including persistent-volume seeding, Qdrant child startup and HTTP launch; `cuda/Dockerfile` and `cuda/README.md` remain uninspected. |
| `packaging/` | Included: npm install/launch path. | Read `npm/bin/mgimind.js`, which forwards arguments and stdio to the binary; `npm/lib/install.js`, `package.json` and README remain uninspected. No installer supply-chain assessment. |
| `.github/` | Included: CI/release evaluators and distribution configuration; issue templates are ancillary. | Enumerated `workflows/ci.yml`, `workflows/release.yml` and `ISSUE_TEMPLATE/`; contents not yet inspected, so no claim that CI passed or covers every path. |
| `Cargo.toml` | Included: binary, dependencies and feature contract. | Read completely, including default-off extractor feature and CUDA feature. |
| `Cargo.lock` | Included: dependency resolution. | Enumerated, not yet inspected; no upstream dependency audit. |
| `Dockerfile` | Included: main image build recipe. | Enumerated; deployment behavior initially traced through `docker/entrypoint.sh`, not verified by building the image. |
| `install.sh`, `install.ps1` | Included: native installation and setup. | Enumerated, not yet inspected; manual's installer claims remain attributed documentation until code checked. |
| `server.json`, `glama.json` | Included: server registry/discovery metadata. | Read completely; `server.json` declares npm stdio transport with `mcp` argument. No live registry verification. |
| `AI_INSTRUCTIONS.md` | Included: install, recall/write, session and maintenance protocol for host assistants. | Read completely as target doctrine, not instructions binding this analysis. |
| `AGENTS.md` | Included: repository-agent guidance and concise memory-use protocol. | Read completely as target doctrine. |
| `llms-install.md` | Included: agent-facing installation pointer. | Read completely; routes readers to `AI_INSTRUCTIONS.md`. |
| `README.md` | Included: intended product boundary, commands, storage and operator responsibilities. | Read completely; documentation assertions are not substituted for implementation checks. |
| `README.ru.md`, `README.zh.md` | Included: translated product doctrine. | Enumerated, not yet inspected; no translation-consistency claim. |
| `BENCHMARKS.md`, `AUDIT_STATUS.md` | Included: source-native evaluation and audit reporting. | Enumerated, not yet inspected; reporting is not accepted as independent evidence of correctness. |
| `CHANGELOG.md`, `CHANGELOG-ARCHIVE.md`, `ROADMAP.md` | Included: version history and plans. | Enumerated, not yet inspected; future or historical statements cannot establish behavior at this commit without code evidence. |
| `PROCESS.md`, `CONTRIBUTING.md`, `SECURITY.md` | Included: maintenance, contribution and security doctrine. | Enumerated, not yet inspected; no governance or security-process effectiveness claim. |
| `.dockerignore`, `.editorconfig`, `.gitignore` | Excluded from functional mechanism analysis: build-context/editor/tracking housekeeping. | Enumerated, not inspected. Exclusion prevents asserting packaging completeness or hygiene from these files; it removes no traced memory-loop responsibility. |
| `LICENSE`, `NOTICE`, `CODE_OF_CONDUCT.md` | Excluded from functional mechanism analysis: legal/community artifacts. | Enumerated, not inspected. No licensing-compliance or community-governance conclusion. |

No source-access gap was encountered. Available-but-uninspected sections above remain within the same frozen Git source for subsequent jobs. Missing host execution evidence and the non-acquired STALE branch are real evidence limits, not invitations to run the target or acquire another revision.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/madgodinc/mgi-mind` | a8defc36f7d0bcd5108714763a12625a0eda0868 | implementation; doctrine/design; reported operation | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/mgi-mind-2cc7fc8c894a/related-systems/madgodinc--mgi-mind`. Implementation: tree, entry dispatch, MCP/HTTP, memory storage/search, ingest/quarantine, fact core, sessions/context, consolidation, optional extractor worker, evaluator code and shipped integration callers as detailed above. Doctrine/design: README, AI instructions, repository-agent guidance and integration guide. Reported operation: benchmark README and source-native evaluator commentary only; raw result contents not yet inspected. | Implementation: [entry](https://github.com/madgodinc/mgi-mind/blob/a8defc36f7d0bcd5108714763a12625a0eda0868/src/main.rs), [dispatch/context](https://github.com/madgodinc/mgi-mind/blob/a8defc36f7d0bcd5108714763a12625a0eda0868/src/cli.rs), [MCP](https://github.com/madgodinc/mgi-mind/blob/a8defc36f7d0bcd5108714763a12625a0eda0868/src/mcp.rs), [storage](https://github.com/madgodinc/mgi-mind/blob/a8defc36f7d0bcd5108714763a12625a0eda0868/src/storage.rs), [consumer](https://github.com/madgodinc/mgi-mind/blob/a8defc36f7d0bcd5108714763a12625a0eda0868/docs/integrations/openai_agents.py), [evaluator](https://github.com/madgodinc/mgi-mind/blob/a8defc36f7d0bcd5108714763a12625a0eda0868/src/bench.rs). Doctrine: [manual](https://github.com/madgodinc/mgi-mind/blob/a8defc36f7d0bcd5108714763a12625a0eda0868/AI_INSTRUCTIONS.md), [integration contract](https://github.com/madgodinc/mgi-mind/blob/a8defc36f7d0bcd5108714763a12625a0eda0868/docs/integrations/README.md). Reported operation: [benchmark reporting](https://github.com/madgodinc/mgi-mind/blob/a8defc36f7d0bcd5108714763a12625a0eda0868/benchmark/README.md), [STALE scope](https://github.com/madgodinc/mgi-mind/blob/a8defc36f7d0bcd5108714763a12625a0eda0868/src/bench_stale.rs). | No checkout access gap. External host implementations, installed artifacts, live executions and another branch's STALE harness are outside this pin. No observed run or causal experiment established by this initial inspection; no verified performance, deployment reliability or end-to-end answer-quality conclusion. |
