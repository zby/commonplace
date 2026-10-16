---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Quicky Wiki's shipped knowledge-production, persistence, maintenance and consumption paths at commit cfeecbffce5b6d0f16533b258a1e88edd86f731e."
run-id: AAS-2026-10-15-quicky-wiki-628f7d7cc628-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: cfeecbffce5b6d0f16533b258a1e88edd86f731e
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/anzal1/quicky-wiki
  kind: git
  path: /media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-quicky-wiki/related-systems/anzal1--quicky-wiki
  revision: cfeecbffce5b6d0f16533b258a1e88edd86f731e
  sha256: null
---

# Quicky Wiki boundary

## Boundary and evidence

Quicky Wiki is in scope as a **memory/knowledge/context-engineering system**. Its intended use is to turn source documents into a retained, confidence-scored knowledge base that people and agent clients can query. This is not merely a library API or an MCP tool: the repository ships the callers that initialize local state, ingest documents, maintain claims, render pages, and later reload and consume them. The boundary is **whole-system**, covering these shipped paths, their embedded prompts and their user-facing entry points. This classification rests on SRC-1, `package.json`, `src/cli.ts`, `src/lib.ts`, `src/cli/context.ts`, `src/compiler/ingest.ts`, `src/graph/store.ts`, `src/graph/query.ts` and `src/mcp/server.ts`.

The declared purpose is explicit (SRC-1, `README.md`):

> **Turn any collection of documents into a living, confidence-scored knowledge base — powered by LLMs.**
> --- `README.md`

The implementation reads source content, extracts claims through a model, compares them with retained knowledge and resolves the result into the graph. Its extraction instructions are shipped source, not external agent policy (SRC-1, `src/compiler/ingest.ts`):

> const systemPrompt = `You extract atomic, verifiable claims from source material.
> Each claim should be a single factual statement. Be precise and specific.
> Assign an initial confidence based on how well-supported the claim is by the source.
> Tag each claim with relevant topic tags.
> Identify related concepts (potential wiki page titles) for cross-linking.
> --- `src/compiler/ingest.ts`

Local state survives individual commands: the CLI opens the same working-directory database rather than creating an isolated store per request (SRC-1, `src/cli/context.ts`, `src/graph/store.ts`):

> export function openStore(): KnowledgeStore {
>   return new KnowledgeStore(getDbPath());
> }
> --- `src/cli/context.ts`

Later queries retrieve retained material before calling the model (SRC-1, `src/graph/query.ts`):

> const { pages: relevantPages, claims: relevantClaims } = store.search(
>     question,
>     50,
>   );
> --- `src/graph/query.ts`

### Functional inclusions

- **Production and admission:** initialization, local-file and URL ingestion, directory ingestion, watched-file ingestion, claim extraction, comparison, resolution, entity-kind and metadata handling, confidence calculation and page summaries. These include embedded extraction, comparison and assignment prompts (SRC-1, `src/cli/create.ts`, `src/cli/ingest.ts`, `src/cli/fetch-url.ts`, `src/cli/watch.ts`, `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/types.ts`).
- **Retention and maintenance:** SQLite sources, pages, claims, provenance links, dependency and contradiction relations, events and full-text indexes; confidence updates, decay, cascade handling, lint/prune, health reporting, resurfacing, red-team review and discovery. Suggestions and critiques are included without assuming they are automatically applied (SRC-1, `src/graph/store.ts`, `src/graph/temporal.ts`, `src/cli/metabolism.ts`, `src/cli/lint.ts`, `src/metabolism/health.ts`, `src/metabolism/redteam.ts`, `src/metabolism/resurface.ts`, `src/discovery/discover.ts`).
- **Reload and consumption:** CLI queries and consensus queries, browser dashboard and its state-editing/bookmark routes, MCP read/write tools, exported library API and compiled/exported views. The optional query-answer save path writes a raw source file for later ingestion; it is part of the loop, not an excluded host responsibility (SRC-1, `src/cli/query.ts`, `src/cli/save-answer.ts`, `src/compiler/consensus.ts`, `src/cli/serve.ts`, `src/mcp/server.ts`, `src/lib.ts`, `src/cli/compile.ts`, `src/render/markdown.ts`).

The save path makes its later ingestion step explicit (SRC-1, `src/cli/query.ts`):

> `    Run 'qw ingest ${filePath}' to compile it into knowledge`,
> --- `src/cli/query.ts`

### Tracked-tree coverage

The table accounts for every top-level tracked file or directory at SRC-1's commit. Included means inside the functional evidence boundary, not that every line has already received a detailed mechanism review. The initial inspection traced the CLI, library and MCP entry points through production, retention, maintenance and consumption. Bounded reading and symbol/call searches supplemented full reads. No material shipped path was inaccessible.

| Top-level tracked path | Decision | Material paths and role | Inspection status and conclusion prevented |
|---|---|---|---|
| `.github/` | Included: delivery context | `.github/workflows/publish.yml`: version-change gate, build, typecheck and publication steps | Workflow read. Supports declared release process only, not evidence that any release succeeded. |
| `.gitignore` | Included: storage/build context | Ignores generated bundles, local databases, environment files and other local artifacts | Read. Does not establish what an installed deployment actually retained. |
| `LICENSE` | Excluded deliberately | Legal terms, not a state-production or consumption path | Not inspected; no legal or license-compliance conclusion is made. |
| `README.md` | Included: doctrine/design | Usage, maintenance instructions, provider requirements, knowledge concepts, dashboard and MCP descriptions | Read completely. Describes intent; not a run trace. |
| `package.json` | Included: entry points and dependencies | Three CLI aliases, library exports, Node requirement, runtime/build dependencies and scripts | Read completely; trace continued into `src/cli.ts`, `src/lib.ts` and `tsup.config.ts`. Published-bundle equivalence is not established. |
| `package-lock.json` | Included: dependency metadata | Root package metadata and locked dependency graph | Root stanza and initial dependency entries inspected; remaining lock entries not yet reviewed in detail. No transitive-dependency audit is claimed. |
| `src/` — entry points and contracts | Included | `src/cli.ts`, `src/lib.ts`, `src/types.ts`: command routing, embedding exports, configuration and entity contracts | Entry points read completely; configuration/defaults read and type symbols searched. Detailed review of remaining type declarations remains available. |
| `src/` — drivers and retained-content callers | Included | `src/cli/create.ts`, `src/cli/init.ts`, `src/cli/context.ts`; `src/cli/ingest.ts`, `src/cli/fetch-url.ts`, `src/cli/watch.ts`; `src/cli/query.ts`, `src/cli/save-answer.ts`; `src/cli/metabolism.ts`, `src/cli/lint.ts`, `src/cli/discover.ts`, `src/cli/claims.ts`, `src/cli/timeline.ts`, `src/cli/compile.ts`, `src/cli/serve.ts` | Main callers, setup, context, query/save, ingest/watch, maintenance and compilation read. Dashboard server routes read; embedded UI calls searched. Thin listing/discovery/timeline and older init wrappers traced by imports/symbols; remaining wrapper details, HTML/CSS and URL-conversion helpers are not yet fully inspected. They are not excluded or unavailable. |
| `src/` — knowledge compiler and prompts | Included | `src/compiler/ingest.ts`, `src/compiler/diff.ts`, `src/compiler/resolve.ts`, `src/compiler/confidence.ts`, `src/compiler/consensus.ts` | Extraction, diff, resolution and consensus entry paths read; summary helpers and confidence helpers partly traced by callers/search. Remaining helper details remain available, not an access gap. |
| `src/` — persistence and retrieval | Included | `src/graph/store.ts`, `src/graph/query.ts`, `src/graph/temporal.ts`, `src/graph/cascade.ts` | Store schema, opening, source/page writes, claim writes and reinforcement/challenge operations read; remaining store API inventoried by method search. Query and temporal code read; cascade callers traced. No operational durability or causal effectiveness result follows from these static reads. |
| `src/` — maintenance, discovery and evaluation surfaces | Included | `src/metabolism/decay.ts`, `src/metabolism/health.ts`, `src/metabolism/redteam.ts`, `src/metabolism/resurface.ts`, `src/discovery/discover.ts`, plus lint and consensus callers above | Health, adversarial review, resurfacing and discovery read; decay wrapper traced through temporal implementation. These are shipped checks/reviews, not an external benchmark or an observed evaluation result. |
| `src/` — model interfaces | Included | `src/llm/adapter.ts`, `src/llm/detect.ts`, `src/llm/parse-json.ts` | Adapter implementation read completely; detection and parsing interfaces/callers searched. Provider discovery internals and parsing helper remain available for deeper review. Actual provider behavior is outside the capture. |
| `src/` — views and exports | Included | `src/render/markdown.ts`, `src/render/obsidian.ts`, `src/render/anki.ts`, `src/render/marp.ts`, `src/render/graph-viz.ts`, `src/render/timeline.ts` | Markdown persistence read completely; alternative renderers searched and traced from compilation/export callers. Their detailed templates remain available. Consumer application behavior is not established. |
| `src/` — agent integration | Included | `src/mcp/server.ts`: schemas, tool dispatcher, read/write tools and stdio/HTTP JSON-RPC transport | Read completely and traced from CLI setup to shared ingest, store, query and render operations. Protocol interoperability is not demonstrated by source inspection. |
| `tsconfig.json` | Included: build context | TypeScript compilation contract | Read completely; no successful build is inferred. |
| `tsup.config.ts` | Included: build/entry context | Separate CLI and library bundles; external SQLite dependency | Read completely; generated `dist/` bytes are not frozen evidence. |

### Frozen evidence and limits

The applicability cutoff is **2026-10-15**. The reviewed boundary is exactly **cfeecbffce5b6d0f16533b258a1e88edd86f731e**, not a moving branch, npm release or live service. The acquired checkout's HEAD matched that commit and its working tree was clean when inspected. The supplied source identity remains `https://github.com/anzal1/quicky-wiki`; differing homepage/repository strings inside `package.json` are package-authored metadata, not authority to substitute another repository.

Overall evidence is **code-grounded**. SRC-1 supplies implementation and doctrine/design. No target code, tests, examples or model calls were executed. The tracked tree has no dedicated test/benchmark directory; `package.json` supplies build and typecheck scripts, while shipped lint, health, red-team and consensus paths provide internal checking/review mechanisms. This is not evidence of their accuracy or efficacy (SRC-1, `package.json`, `.github/workflows/publish.yml`, `src/cli/lint.ts`, `src/metabolism/health.ts`, `src/metabolism/redteam.ts`, `src/compiler/consensus.ts`).

External dependencies are Node.js, SQLite through `better-sqlite3`, SDKs and configured model endpoints, remote URL content, the browser's D3 resource, and downstream MCP clients or embedding applications (SRC-1, `package.json`, `src/llm/adapter.ts`, `src/cli/fetch-url.ts`, `src/cli/serve.ts`, `src/lib.ts`, `src/mcp/server.ts`). Their implementations and operation are deliberately outside this source boundary. This prevents conclusions about model quality, service reliability, dependency internals, fetched-document truth, browser delivery, client interoperability or enclosing-agent planning. Such host responsibilities are not attributed to Quicky Wiki.

User-created `.quicky/` databases, raw corpora, generated `wiki/` and `dist/` outputs, deployed installations, execution traces and controlled experiments are not supplied as frozen evidence. Their absence prevents conclusions about actual retained contents, long-term knowledge improvement, production scale, confidence calibration, runtime safety or performance. Available source portions not yet inspected are follow-on inspection work, not access gaps and not exclusions from the registered Git revision.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/anzal1/quicky-wiki` | cfeecbffce5b6d0f16533b258a1e88edd86f731e | implementation; doctrine/design | Access root: `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-16-quicky-wiki/related-systems/anzal1--quicky-wiki`. Implementation: tracked-tree inventory; package/build/release configuration; CLI and library entry points; setup/context, ingest/watch, query/save, maintenance/lint, compilation callers; extraction/diff/resolution and consensus; store schema and write/update paths; query/temporal implementation; complete MCP server; dashboard server routes and UI-call search; renderer, discovery, provider and helper symbol/call searches as detailed in the coverage table. Doctrine/design: complete `README.md`, extraction/query/review prompts in the inspected implementation, MCP tool descriptions and setup instructions. | Implementation: [CLI](https://github.com/anzal1/quicky-wiki/blob/cfeecbffce5b6d0f16533b258a1e88edd86f731e/src/cli.ts), [store](https://github.com/anzal1/quicky-wiki/blob/cfeecbffce5b6d0f16533b258a1e88edd86f731e/src/graph/store.ts), [ingestion](https://github.com/anzal1/quicky-wiki/blob/cfeecbffce5b6d0f16533b258a1e88edd86f731e/src/compiler/ingest.ts), [retrieval/query](https://github.com/anzal1/quicky-wiki/blob/cfeecbffce5b6d0f16533b258a1e88edd86f731e/src/graph/query.ts), [MCP](https://github.com/anzal1/quicky-wiki/blob/cfeecbffce5b6d0f16533b258a1e88edd86f731e/src/mcp/server.ts), [dashboard](https://github.com/anzal1/quicky-wiki/blob/cfeecbffce5b6d0f16533b258a1e88edd86f731e/src/cli/serve.ts). Doctrine/design: [README](https://github.com/anzal1/quicky-wiki/blob/cfeecbffce5b6d0f16533b258a1e88edd86f731e/README.md), [extraction prompt](https://github.com/anzal1/quicky-wiki/blob/cfeecbffce5b6d0f16533b258a1e88edd86f731e/src/compiler/ingest.ts), [review prompt](https://github.com/anzal1/quicky-wiki/blob/cfeecbffce5b6d0f16533b258a1e88edd86f731e/src/metabolism/redteam.ts). | No checkout access gap encountered. No observed run or causal experiment supplied. Implementation supports static behavior claims only; documentation and prompts support attributed intent. External services, dependencies, hosts and generated/user artifacts are not captured, preventing the operational and efficacy conclusions named above. |
