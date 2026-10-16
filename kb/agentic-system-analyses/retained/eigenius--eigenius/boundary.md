---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Eigenius's typed knowledge platform at commit 836498ebd99733067d45aa6f7b09d4ff5035dd99, with its repository frozen and its operational loop only partly traced."
run-id: AAS-2026-10-15-eigenius-fe68ed89519b-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: complete artifact, partial loop
reviewed-boundary: "836498ebd99733067d45aa6f7b09d4ff5035dd99"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/eigenius/eigenius
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-eigenius/related-systems/eigenius--eigenius
  revision: "836498ebd99733067d45aa6f7b09d4ff5035dd99"
  sha256: null
---

# Eigenius boundary

## Boundary and evidence

Eigenius is in scope as a **memory/knowledge/context-engineering system**: a typed knowledge platform with model-assisted prose formalization and an agent-facing tool surface. It is not classified here as an enclosing autonomous agent runtime. Its declared intended use is verifiable AI in science and engineering, built on a typed, versioned knowledge graph (SRC-1, `README.md`). That statement is intent, not evidence of scientific reliability:

> An open-source platform for **verifiable AI in science and engineering**, built on a typed, versioned knowledge graph.
> --- `README.md`

The executable source supports the knowledge-system classification. The shipped CLI constructs `EncodingFormalizer`, supplies a persistent RocksDB backend when `--db` is set, and injects the formalizer into the kernel server (SRC-1, `cli/src/main.rs`). The formalizer reloads a document branch, obtains recorded model decisions or live decision arms, runs the encoding pipeline, emits an artifact, and commits recorded draws. Thus retained content can influence a later formalization; this is not merely a stateless returning computation (SRC-1, `crates/eigenius-encoding/src/formalize.rs`):

> let branch = doc_branch_head(&backend, &req.doc_id)?;
> --- `crates/eigenius-encoding/src/formalize.rs`

> let draws_committed = commit_draws(&backend, &req.doc_id, doc_layer, draw_resources_all)?;
> --- `crates/eigenius-encoding/src/formalize.rs`

Model calls are part of the shipped implementation, not just an external agent's possible usage. The kernel's Anthropic client constructs a model request containing a user prompt and schema-constrained output, then sends it to the provider. Separately, the Deno entry point registers real or mock `CompleteText` and `CompleteJson` components (SRC-1, `kernel/src/dcg/anthropic_client.rs`, `orchestration/src/main.ts`). The provider call itself is inspectable:

> let resp = reqwest::Client::new()
>         .post(API_URL)
>         .header("x-api-key", api_key)
>         .header("anthropic-version", ANTHROPIC_VERSION)
>         .header("content-type", "application/json")
>         .json(&body)
>         .send()
>         .await
>         .map_err(|e| format!("anthropic request failed: {e}"))?;
> --- `kernel/src/dcg/anthropic_client.rs`

### Functional inclusions and inspection extent

The target is the Eigenius platform shipped in this repository, not just its Rust library interface. The CLI, MCP server, SDK, browser notebook, drivers, ontologies, maintenance machinery and evaluators remain in the functional boundary. A shipped caller is not treated as an external host. The entire Git repository at the registered revision is available for later source inspection; the paths below record initial coverage, not an evidence allowlist.

The boundary kind is **complete artifact, partial loop**. The complete tracked tree was inventoried, and material entry points were traced into formalization, persistence/replay and caller-controlled admission. However, the initial inspection has not traced every maintenance, retrieval, institution and evaluation path. These are uninspected available sources, not access gaps or deliberate functional exclusions. Consequently this boundary does not certify whole-system operational coverage.

| Responsibility | Initial inspection and remaining limit |
|---|---|
| Product intent and entry surfaces | SRC-1, `README.md` introduction, capability and architecture sections; tracked-tree inventory. Documentation declarations are not treated as execution results. |
| CLI host and persistence selection | SRC-1, `cli/src/main.rs` local commit helpers and `cmd_serve`: RocksDB selection, in-process Lean/Statistics registration, configuration loading and formalizer injection. Other CLI verbs were located by search, not traced end to end. |
| Prose formalization and decision retention | SRC-1, `kernel/src/server/formalize.rs` request setup; `crates/eigenius-encoding/src/formalize.rs` served formalizer, branch reload, replay selection, emission and draw commitment. `kernel/src/dcg/anthropic_client.rs` request construction and send inspected; `kernel/src/dcg/reading_ranker.rs` prompt/provider locations searched. Full prompt contracts, grammar, decision gating and all provider alternatives still require inspection before claiming their guarantees. |
| Agent-facing production and admission | SRC-1, `orchestration/src/mcp/server.ts` load, program execution and formalization/result tools. The formalization tool returns a task and exposes a separate artifact fetch; loading is a separate operation. External agents' reasoning, scheduling and decision to trust an artifact are not attributed to Eigenius. |
| Shipped notebook consumer | SRC-1, `notebooks/src/runtime/notebookStore.ts` formalization-cell execution: task polling, artifact retrieval, and optional explicit load. `notebooks/src/components/cells/FormalizeCell.tsx` and `clients/eigenius-ts/src/notebook.ts` were searched for caller/persistence responsibilities. Browser persistence, notebook publication/reopening and every SDK method have not been fully traced. |
| Admission and startup seams | SRC-1, `kernel/src/server/load.rs` commit-orchestrator invocation and outcome handling; `kernel/src/server/lifecycle.rs` startup backend and component setup. Resume locations were searched, but crash recovery, branch consistency and lower-level durable writes are not established by this inspection. |
| Alternate computation and external runtimes | SRC-1, `orchestration/src/main.ts` component registration and runtime configuration declarations; tree inventory of `crates/runtime-substrate/`, Julia, Lean and R workers, and institution crates. The native dispatch/verification loops remain to be traced; no conclusion about proof soundness, sandbox isolation or numerical correctness follows from these entry seams. |
| State maintenance and retrieval | Tree inventory includes `kernel/src/task/`, `kernel/src/layer/`, `kernel/src/query/`, `kernel/src/commit/`, `storage/rocksdb/`, `storage/tikv/`, `scripts/`, `ontologies/` and provisioning/import crates. Apart from the seams above, consolidation, garbage collection, indexing, retrieval, bootstrap schemas and external-data provisioning remain uninspected. Their completeness and consistency cannot yet be assessed. |
| Instructions, demos and evaluators | Tree inventory includes `CLAUDE.md`, `docs/method/`, design/guides, `demo/`, `experiments/`, tests under kernel/storage/crates/orchestration, and notebook E2E tests. Initial evaluator inspection is limited to the opening of `crates/eigenius-encoding/tests/served_formalization.rs`, which declares a replay-based served/CLI artifact comparison requiring a DB snapshot. Instructions, demo loops, benchmark validity and test outcomes are not established. |
| Packaging and presentation | Tree inventory includes workspace/build manifests, `.cargo/`, `.github/`, `deploy/`, Compose files, `justfile`, `patches/`, `proto/`, `data/`, `references/` and `website/`. No deployment, release or website behavior is claimed from inventory alone. |

One consequential caller distinction is already supported: generation is not identical to assertion into the serving chain. The notebook obtains the emitted artifact and invokes load only when its `land` setting requests it (SRC-1, `notebooks/src/runtime/notebookStore.ts`):

> if (cell.land) {
>     const outcome = await eigen.load(artifact, {
>       contentType: "application/x-esl",
>       autoCommit: true,
>     });
> --- `notebooks/src/runtime/notebookStore.ts`

This optional path and the CLI's construction of the served formalizer are included platform responsibilities. Treating them as excluded applications would incorrectly narrow the target to the kernel API.

### Frozen evidence and exclusions

The frozen evidence is repository `https://github.com/eigenius/eigenius` at **836498ebd99733067d45aa6f7b09d4ff5035dd99**. The acquired checkout's HEAD matched this pin, and `git status --short` reported no changes. The analysis cutoff is **2026-10-15**; later commits, live documentation changes and external linked papers are not evidence in this run. The overall tier is **code-grounded**. Source inspection establishes implemented paths and declared contracts, not their successful execution.

External model services, independently installed agent hosts, scientific libraries, container engines, external datasets, image registries and deployed databases are dependencies, not additional frozen sources. Repository-side adapters, configuration, workers and importers remain included. Provider behavior, external library correctness, actual image contents, live deployment state and real data coverage cannot be established without separately registered evidence. No such evidence was supplied or acquired. The source mentions a lexicon DB snapshot and WordNet dictionary as prerequisites for the inspected comparison test (SRC-1, `crates/eigenius-encoding/tests/served_formalization.rs`); that test's source is evidence of an evaluator contract, not a supplied snapshot or observed passing run. Target code, tests and demos were not executed.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/eigenius/eigenius` | 836498ebd99733067d45aa6f7b09d4ff5035dd99 | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-15-eigenius/related-systems/eigenius--eigenius`. Implementation: initial bounded reads of `cli/src/main.rs`, `orchestration/src/main.ts`, `orchestration/src/mcp/server.ts`, `kernel/src/server/formalize.rs`, `kernel/src/server/load.rs`, `kernel/src/server/lifecycle.rs`, `kernel/src/dcg/anthropic_client.rs`, `crates/eigenius-encoding/src/formalize.rs`, `notebooks/src/runtime/notebookStore.ts`, and `crates/eigenius-encoding/tests/served_formalization.rs`; searches and tree inventory as recorded above. Doctrine/design: `README.md` introduction, capability and architecture sections, plus comments/tool descriptions in those inspected implementation paths. | Implementation: [CLI host](https://github.com/eigenius/eigenius/blob/836498ebd99733067d45aa6f7b09d4ff5035dd99/cli/src/main.rs), [served formalizer](https://github.com/eigenius/eigenius/blob/836498ebd99733067d45aa6f7b09d4ff5035dd99/crates/eigenius-encoding/src/formalize.rs), [MCP](https://github.com/eigenius/eigenius/blob/836498ebd99733067d45aa6f7b09d4ff5035dd99/orchestration/src/mcp/server.ts), [notebook caller](https://github.com/eigenius/eigenius/blob/836498ebd99733067d45aa6f7b09d4ff5035dd99/notebooks/src/runtime/notebookStore.ts). Doctrine/design: [README](https://github.com/eigenius/eigenius/blob/836498ebd99733067d45aa6f7b09d4ff5035dd99/README.md). Other cited commit-relative paths in this member resolve within this same Git source. | No repository-file access failure encountered. Available but uninspected material is identified above and prevents whole-system loop claims. External services, lexicon snapshots and deployment artifacts are not frozen here; no observed run or causal experiment is registered. Implementation does not establish successful operation, and doctrine/design does not establish implementation completeness. |
