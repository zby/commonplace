---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Sage-wiki's shipped knowledge-state production, maintenance and consumption paths at commit d3ef3a1346405c82eac01b4d7c493c94c1c59169."
run-id: AAS-2026-10-15-sage-wiki-cc43456fb833-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: d3ef3a1346405c82eac01b4d7c493c94c1c59169
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/xoai/sage-wiki
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/sage-wiki-cc43456fb833/related-systems/xoai--sage-wiki
  revision: d3ef3a1346405c82eac01b4d7c493c94c1c59169
  sha256: null
---

# Sage-wiki boundary

## Boundary and evidence

This run examines Sage-wiki as a shipped memory/knowledge/context-engineering system, not merely its embedding API or MCP tools. Its intended use is to retain source documents and agent-produced knowledge, compile them into a wiki and graph, and supply that retained state to later searches and model answers. The target issues model calls for compilation, conversation extraction and question answering. Its enclosing agents are consumers, not a runtime implemented by Sage-wiki. SRC-1: `README.md`, `internal/compiler/fullpipeline.go`, `internal/scribe/session.go`, `internal/query/query.go`.

The author's declared system identity is:

> **sage-wiki** is a graph memory and knowledge base that AI agents and humans build and query together.
> --- `README.md`

Executable scope includes source ingestion, text capture, transcript scribing, tiered compilation, retained markdown and database state, indexing, ontology construction, output admission and removal, search/context assembly, and answer filing. It also includes shipped CLI, MCP, REST, embedded Go, browser and terminal callers, background workers, prompt/skill generation, packs, federation and durability paths. These are parts of the target even where they invoke internal APIs rather than own a model loop. SRC-1: `cmd/sage-wiki/main.go`, `pkg/engine/methods.go`, `internal/mcp/tools_write.go`, `internal/serve/deps.go`, `internal/query/query.go`, `internal/trust/promote.go`, `README.md`.

Initial tracing establishes production, maintenance, admission and later consumption rather than stopping at a library facade:

- Reader capture writes into `raw/captures`; the compiler loads configuration, prompts and manifest, computes a diff, runs tiers and saves the manifest. The full pipeline supplies summarize/extract/write passes. SRC-1: `pkg/engine/methods.go`, `internal/compiler/pipeline.go`, `internal/compiler/fullpipeline.go`.
- Session scribing is a separate producer: the shipped command reads a transcript, opens the configured database and invokes extraction that adds or updates ontology entities. It is included rather than attributed to an excluded agent host. SRC-1: `cmd/sage-wiki/main.go`, `internal/scribe/session.go`.
- Answer filing delegates to the trust path when the configured mode is not unrestricted inclusion. Promotion moves retained answers into outputs and indexes them; demotion removes retrieval entries. Compilation can check source changes that invalidate confirmed outputs. SRC-1: `internal/query/query.go`, `internal/trust/promote.go`, `internal/compiler/pipeline.go`.
- Later question answering creates stores over the database, retrieves chunks or documents and builds context with the configured output-inclusion policy. MCP's compound query calls this same question-answer path; browser and terminal query callers reference streaming and saving paths. SRC-1: `internal/query/query.go`, `internal/mcp/tools_compound.go`, `internal/web/server.go`, `internal/tui/query/model.go`.
- Generated instructions prescribe search before work and capture afterward. The LangGraph example searches, conditionally compiles, retrieves again and captures; its generation step is a stub. The Go example captures, compiles and searches; the Vercel example exposes retrieval tools but directly invokes them rather than demonstrating autonomous model tool selection. SRC-1: `internal/skill/packs/base.md.tmpl`, `examples/langgraph/main.py`, `examples/embed/main.go`, `examples/vercel-ai-sdk/main.ts`.
- Evaluators are shipped consumers, not excluded hosts: the memory-benchmark backend persists session markdown, compiles projects, checks resumed state and searches it; the LOCOMO driver supplies separate answerer/judge calls. Its scores therefore cannot automatically be attributed to Sage-wiki's native answer-generation path. SRC-1: `eval/benchmarks/common/sagewiki.py`, `eval/benchmarks/locomo/run.py`.

The retained-answer admission boundary is explicit in implementation:

> // Move file from under_review/ to outputs/ BEFORE marking confirmed
> --- `internal/trust/promote.go`

The shipped instruction closes the intended consumer-to-producer loop:

> After completing work that produced new knowledge:
>
> - A decision or tradeoff → `wiki_learn` with type "decision"
> - A non-obvious finding or gotcha → `wiki_learn` with type "gotcha"
> - A pattern or convention → `wiki_learn` with type "convention"
> - Rich context from a conversation → `wiki_capture` to extract and index it
> --- `internal/skill/packs/base.md.tmpl`

The boundary kind is **whole-system**: all material shipped state-loop paths remain included, including examples and evaluators. This does not claim exhaustive implementation inspection. The table distinguishes initial source reading/search tracing from inventory-only material still available for later inspection. No material path is excluded merely because it is a caller.

### Tracked top-level coverage

All entries below belong to SRC-1 at the frozen commit. Directory scopes name material paths, not just directory labels. “Included” means within the functional/evidence boundary; inspection status describes work performed for this declaration. Inventory-only material is available, not an access gap.

| Top-level entry | Classification | Role, material paths and initial inspection | Exclusion limit |
|---|---|---|---|
| `.dockerignore` | Excluded | Packaging filter; inventoried | No assessment of container build-context completeness |
| `.gitattributes` | Excluded | Repository attributes; inventoried | No assessment of checkout/export transformations |
| `.github/` | Included | `workflows/ci.yml`, `clients.yml`, release/publish/fuzz workflows and templates; inventory-only | None; workflow execution is not established |
| `.gitignore` | Excluded | Repository ignore policy; inventoried | No assessment of accidentally untracked deployment artifacts |
| `.golangci.yml` | Included | Static-check configuration; inventory-only | None; no lint result established |
| `CHANGELOG.md` | Included | Shipped release history; inventory-only | None; history is not implementation proof |
| `CONTRIBUTING.md` | Included | Pack/parser authoring contract, referenced by README; inventory-only | None; detailed contract not yet inspected |
| `Dockerfile` | Included | Shipped deployment entry; inventory-only | None; container behavior not tested |
| `LICENSE` | Excluded | Legal terms; inventoried | No licensing conclusion |
| `Makefile` | Included | Build/test/generation drivers; inventory-only | None; no build result established |
| `README.md` | Included | Full read: intended system, workspace layout, commands, interfaces, packs, mirror and evaluation declarations | None; performance declarations remain attributed |
| `api/` | Included | `openapi.yaml`: REST contract; inventoried and located through README and server wiring | None; endpoint contract details need inspection |
| `assets/` | Included | Architecture, compiler, graph and interface diagrams plus UI image; inventoried, not visually inspected | None; diagrams do not establish executable behavior |
| `ci/` | Included | Ownership, qualification, platform/service contracts and standards; inventory-only | None; qualification has not been verified |
| `clients/` | Included | Python `src/sagewiki/client.py`, `jobs.py`, models/tests; TypeScript `src/client.ts`, `jobs.ts`, types/tests; client search tracing and shipped examples | None; client transport details not exhaustively inspected |
| `cmd/` | Included | `sage-wiki/main.go` command routing and scribe read; `capture.go`, `learn.go`, `write_cmd.go`, `trust_cmd.go`, `ontology_resolve.go`, pack/hub/mirror/hydrate commands inventoried | None; secondary command implementations remain available |
| `docs/` | Included | `guides/agent-memory-layer.md`, configuration, prompts, graph, output-trust, storage, serve, search and remote-mirror guides; security/determinism/webhooks docs and translations inventoried | None; only README's referenced declarations used initially |
| `eval/` | Included | `benchmarks/common/sagewiki.py` fully read; `locomo/run.py` searched through retrieval, answer/judge and result persistence; `longmemeval/run.py`, `beam/run.py`, prompts/results, `retrieval_ab.py`, `eval.py`/tests inventoried | None; benchmark results and other driver details not yet assessed |
| `examples/` | Included | Full reads of `embed/main.go`, `langgraph/main.py`, `vercel-ai-sdk/main.ts`: retained-state consumers and capture/compile callers | None; stubs are not real agent execution evidence |
| `go.mod` | Included | Module dependency declaration; inventory-only | None; dependency internals remain outside frozen source |
| `go.sum` | Included | Dependency checksums; inventory-only | None; no dependency integrity audit performed |
| `integration_test.go` | Included | Root integration test; inventoried, not read or run | None; passing integration behavior not established |
| `internal/` | Included | Read/search traced `compiler/pipeline.go`, `fullpipeline.go`, `mcp/tools_write.go`, `tools_compound.go`, `serve/deps.go`, `query/query.go`, `trust/promote.go`, `hooks.go`, `scribe/session.go`, `linter/runner.go`, `app/app.go`, `web/server.go`, `tui/query/model.go`, `skill/packs/base.md.tmpl`. Inventory also covers compiler workers/watch/batch/curation, extract, prompts/templates, pack/bundled, ontology, search, memory, vectors, manifest, storage/postgres, mirror, auth, hub, wiki and API implementations/tests | None; detailed subpasses, store backends, federation and restore implementation remain available for later source inspection |
| `pkg/` | Included | `engine/doc.go` read; `engine/methods.go` capture read and compile routing searched; engine search/manager, sagewiki facade, provider/fake, events and mirror inventoried | None; facade isolation and backend guarantees not exhaustively assessed |
| `scripts/` | Included | CI checks, determinism scripts, `p4-fixture-server.sh` and warmcheck; inventoried | None; fixture setup is not observed target execution |
| `skills/` | Included | `sage-wiki/SKILL.md` fully read; `sage-wiki-integrate/SKILL.md` inventoried | None; instructions describe intended agent behavior, not compliance |
| `testdata/` | Included | OpenAI fixtures, golden corpus including adversarial/contradiction/multihop cases, golden state/search/events; inventoried | None; fixtures have not been validated as run evidence |
| `tests/` | Included | `pathological/generator.go`, `pathological_test.go`; inventory-only | None; no scale or pathological-case result established |
| `tools/` | Included | `skillgen` generator/templates plus CI evidence/check/summary tools and tests; inventory-only | None; generated-contract freshness not independently checked |
| `web/` | Included | `src/lib/api.ts`, `app.tsx`, ArticleView/GraphView/QAPanel and reload/SSE support inventoried; server-side query/save consumers searched under `internal/` | None; client rendering and browser execution not assessed |

### External dependencies and limits

External model/embedding providers, imported Go/Python/JavaScript packages, optional PostgreSQL/pgvector, S3-compatible services, external parsers, remote pack registries, user workspaces and enclosing agent runtimes are outside this single-repository frozen source. Their in-repository adapters, configuration, prompts and shipped callers remain included. This prevents conclusions about provider internals, remote-service guarantees, unseen user content, third-party parser behavior and end-to-end compliance by real agents. SRC-1: `README.md`, `pkg/engine/doc.go`, `examples/langgraph/main.py`, `examples/vercel-ai-sdk/main.ts`, `eval/benchmarks/common/sagewiki.py`.

The acquired checkout's HEAD matches the supplied full commit and its status is clean. The evidence cutoff is 2026-10-15, the opening run date; no later upstream revision or live documentation is admitted. The overall tier is **code-grounded**, with doctrine/design separately attributed. No target execution, tests, dependency installation or model calls were performed. Initially inspected code supports implementation analysis, not observed success, benchmark validity or causal effectiveness. No required source-access gap was encountered. Available files not yet read are explicitly not access gaps.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/xoai/sage-wiki` | d3ef3a1346405c82eac01b4d7c493c94c1c59169 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/sage-wiki-cc43456fb833/related-systems/xoai--sage-wiki`. Implementation: tracked tree inventory; shipped CLI/engine/serve routing, compiler lifecycle, capture, scribe, answer filing/admission/retrieval, linter and UI callers, examples and evaluator consumer tracing listed above. Doctrine/design: full `README.md`, `pkg/engine/doc.go`, `skills/sage-wiki/SKILL.md`, `internal/skill/packs/base.md.tmpl`; source comments and example declarations attributed in place. Listed paths record initial inspection, not an allowlist. | Implementation: [compiler](https://github.com/xoai/sage-wiki/blob/d3ef3a1346405c82eac01b4d7c493c94c1c59169/internal/compiler/pipeline.go), [query](https://github.com/xoai/sage-wiki/blob/d3ef3a1346405c82eac01b4d7c493c94c1c59169/internal/query/query.go), [admission](https://github.com/xoai/sage-wiki/blob/d3ef3a1346405c82eac01b4d7c493c94c1c59169/internal/trust/promote.go), [benchmark backend](https://github.com/xoai/sage-wiki/blob/d3ef3a1346405c82eac01b4d7c493c94c1c59169/eval/benchmarks/common/sagewiki.py). Doctrine/design: [README](https://github.com/xoai/sage-wiki/blob/d3ef3a1346405c82eac01b4d7c493c94c1c59169/README.md), [behavioral template](https://github.com/xoai/sage-wiki/blob/d3ef3a1346405c82eac01b4d7c493c94c1c59169/internal/skill/packs/base.md.tmpl). | No source-access gap identified. Implementation and doctrine/design only at initial inspection: no observed run or causal experiment established. External dependencies and user/host behavior are not frozen here; benchmark artifacts and uninspected paths cannot support conclusions until examined under this pin. |
