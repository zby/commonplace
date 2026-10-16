---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Stash's self-hosted persistent-memory system at Git commit d34ed430c4348ef741ef95146b488aea8616f4fb."
run-id: AAS-2026-10-15-stash-7ac5612837a0-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: d34ed430c4348ef741ef95146b488aea8616f4fb
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/alash3al/stash
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/stash-7ac5612837a0/related-systems/alash3al--stash
  revision: d34ed430c4348ef741ef95146b488aea8616f4fb
  sha256: null
---

# Stash boundary

## Boundary and evidence

This run analyses the self-hosted Stash repository as a persistent-memory system for agents. Its intended use is to retain observations across sessions, derive structured knowledge, and return retained content to a caller. It is in scope because it both serves memory to model-driven clients and issues its own model calls during consolidation. The classification is **memory/knowledge/context-engineering system**, not an enclosing agent runtime. The boundary kind is **whole-system**: it includes the shipped CLI, MCP server, maintenance drivers, model adapters, persistence and query layer, and instructions supplied to consuming agents. These are parts of the target, not excluded applications merely because they call the Brain API. [SRC-1: `cmd/cli/main.go`, `cmd/cli/commands.go`, `cmd/cli/mcp.go`, `internal/bootstrap/bootstrap.go`, `internal/reasoner/openai.go`]

The model-dependent maintenance responsibility is explicit in executable code: consolidation passes episode contents to the reasoner, embeds the resulting summary, and inserts a fact and source associations. The reasoner itself calls a chat-completions API. This establishes a model-dependent memory mechanism without requiring Stash to own a general-purpose agent execution loop. [SRC-1: `internal/brain/consolidate.go`, `internal/reasoner/openai.go`]

> sf, err := b.reasoner.ReasonStructured(ctx, texts)
> --- `internal/brain/consolidate.go`

> resp, err := o.client.Chat.Completions.New(ctx, openai.ChatCompletionNewParams{
> --- `internal/reasoner/openai.go:114-203`

The shipped consumption path is also inside the boundary. MCP `remember` calls `Brain.Remember`; MCP `recall` calls `Brain.Recall` and serializes its results as tool text. CLI commands expose the same storage and retrieval operations. `Remember` persists embedded episodes in PostgreSQL; `Recall` queries stored facts and episodes. The MCP server description carries a session protocol telling the external agent when to store, reload and maintain memory. These instructions are evidence of intended use, not evidence that a client follows them. [SRC-1: `cmd/cli/mcp.go`, `cmd/cli/commands.go`, `internal/brain/episode.go`, `internal/brain/recall.go`, `cmd/cli/mcp_prompts.tmpl`]

> Use recall as the primary way to load durable memory. Use context only for short-lived active work in a known namespace.
> --- `cmd/cli/mcp_prompts.tmpl`

Maintenance includes manual consolidation, the standalone consolidation service, the MCP background ticker and the combined service driver. Docker Compose ships the MCP service with background consolidation enabled. The retained state boundary includes namespaces, episodes, facts and their provenance, relationships, patterns, contradictions, causal links, hypotheses, goals, failures, working context, progress checkpoints, settings and the embedding cache. This is a functional scope declaration, not an assertion that every schema field or transition has already been audited. [SRC-1: `cmd/cli/consolidate.go`, `cmd/cli/mcp.go`, `cmd/cli/serve_all.go`, `docker-compose.yml`, `internal/db/db.go`, `internal/models/models.go`, `internal/db/migrations/00020_add_consolidation_checkpoints.sql`]

### Repository coverage

The tracked tree was inspected at the frozen commit. Every top-level tracked file or directory is accounted for below. “Included” denotes the functional evidence boundary; initial inspection can be a targeted source read or structural search rather than an exhaustive correctness review. All paths and roles in this table refer to SRC-1.

| Top-level path | Decision | Material paths and role | Initial inspection and limits |
|---|---|---|---|
| `.env.example` | Included | Environment contract for database, embeddings, reasoner and maintenance. | Configuration-key search; configuration behavior also traced through `internal/bootstrap/bootstrap.go` and `internal/config/config.go`. No credentials or live configuration inspected. |
| `.github/` | Included | `.github/workflows/release.yml` builds CLI binaries and container images. | Workflow read; build and publication success not observed. |
| `.gitignore` | Excluded | Checkout ignore policy, not a shipped memory producer or consumer. | Tracked-tree inventory; exclusion prevents conclusions about ignored local runtime artifacts. |
| `Dockerfile` | Included | Builds `./cmd/cli/` and installs `/stash` as the image entry point. | Full source read; no image built or run. |
| `LICENSE` | Excluded | Legal terms, not memory behavior. | Tracked-tree inventory only; no licensing assessment. |
| `README.md` | Included | Product boundary, client configuration and intended memory workflow; explicitly distinguishes the cloud product. | Full read; promotional claims remain attributed intent. |
| `cmd/` | Included | `cmd/cli/main.go` command registry; `commands.go` storage/retrieval; `mcp.go` tools, serialization, SSE/stdio and ticker; `mcp_prompts.tmpl` agent instructions; `consolidate.go` maintenance; `serve_all.go` combined driver; `server.go` health/metrics; namespace, context, causal, contradiction, hypothesis, goal, failure and environment command adapters. | Entry points, principal handlers and maintenance drivers read; remaining registry and template definitions structurally searched. Individual secondary handlers and tool descriptions remain available for detailed analyst inspection; they are not access gaps or exclusions. |
| `docker-compose.yml` | Included | PostgreSQL/pgvector persistent volume plus MCP service with background consolidation. | Full read; deployment success and persistence across an actual restart not observed. |
| `docs/` | Included, except decorative image | `docs/GETTING_STARTED.md` agent workflow and maintenance; `docs/LOCAL_OLLAMA.md` provider setup; `docs/index.html` published design and setup account. `docs/og-image.png` excluded as a presentation asset. | Markdown guides read in full; HTML configuration passages searched, remaining HTML not yet inspected. No conclusion about visual presentation or image contents. Documentation is not runtime evidence. |
| `go.mod` | Included | Go module/toolchain and dependency declarations. | Module/toolchain search; no dependency implementation audited. |
| `go.sum` | Included | Dependency integrity manifest. | Inventoried, not substantively inspected; no supply-chain integrity conclusion. |
| `internal/` | Included | `bootstrap/bootstrap.go` and `config/config.go` initialization; `brain/episode.go`, `recall.go`, `context.go` persistence and reload; `brain/consolidate.go`, `consolidate_goal.go`, `consolidate_failure.go`, `consolidate_hypothesis.go`, `decay.go` maintenance; fact, namespace, contradiction, causal, goal, failure and hypothesis modules for state operations; `db/db.go` and `db/migrations/*.sql` persistence; `models/models.go` state structures; `queries/*.go` and `queries/*.tmpl` SQL generation; `embedder/*.go` and `reasoner/*.go` model boundaries and internal prompts; `observability/metrics.go` instrumentation; `brain/brain_test.go` shipped tests. | Core persist/reload paths, bootstrap, migration driver, consolidation orchestration and fact-admission segment, reasoner interface and structured-fact model call, embedding adapter, recall SQL and tests read. Other state operations, schema declarations and maintenance/model methods structurally searched. Secondary implementations remain available for later detailed inspection. Tests inspected concern LIKE escaping and descendant patterns, not an observed memory-quality evaluation. |

### External responsibilities and evidence limits

The repository's own CLI, service drivers and agent-facing instructions remain included. External MCP clients and their enclosing agents are dependencies, not part of the shipped implementation. Their decisions about what to remember, whether to obey the session protocol, and how to use retrieved text cannot be attributed to Stash. The shipped protocol and tool responses establish the integration contract, not successful downstream answer improvement. [SRC-1: `README.md`, `cmd/cli/mcp.go`, `cmd/cli/mcp_prompts.tmpl`]

PostgreSQL/pgvector, model servers, Go dependencies and container bases are external implementations. The source boundary covers Stash's configuration, SQL, requests and handling of responses, not those dependencies' internal correctness, availability or privacy guarantees. No external provider documentation or live service was captured. [SRC-1: `docker-compose.yml`, `Dockerfile`, `internal/db/db.go`, `internal/embedder/openai.go`, `internal/reasoner/openai.go`]

The separately hosted Stash Cloud product is excluded. This prevents conclusions about its tenancy, scalability, feature parity or operation. The repository explicitly says it is a separate implementation; a shared name does not extend this source boundary. [SRC-1: `README.md`]

> The cloud version is written from scratch — it shares no code with this repository.
> --- `README.md`

The frozen revision is **d34ed430c4348ef741ef95146b488aea8616f4fb**, and the applicability cutoff is **2026-10-15**, the supplied run date. HEAD matched this revision and the checkout had no reported tracked or untracked changes. Only this commit may supply source evidence; links to hosted products, provider pages and client software are not additional registered sources. The overall evidence tier is **code-grounded**. No target code, tests, examples, models or services were executed. There are no identified inaccessible material shipped paths; uninspected available code remains inspection work, not an access gap. There is no supplied execution trace or causal experiment, so operational reliability, synthesis quality, agent adherence and downstream benefit remain unestablished.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/alash3al/stash` | d34ed430c4348ef741ef95146b488aea8616f4fb | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/stash-7ac5612837a0/related-systems/alash3al--stash`. Implementation: tracked-tree inventory, CLI entry point and storage/retrieval handlers, MCP tool handlers and transports, consolidation drivers, bootstrap, core episode/recall/context behavior, consolidation orchestration and fact admission, structured-fact model call, embedder adapter, DB initializer, recall SQL and shipped test file; structural searches across secondary state modules, model methods, migrations, configuration, metrics and template definitions. Doctrine/design: full README and Markdown setup guides, initial MCP session protocol and selected HTML setup passages. Coverage table distinguishes detailed reads from searches and still-uninspected available material. | Implementation: [CLI](https://github.com/alash3al/stash/blob/d34ed430c4348ef741ef95146b488aea8616f4fb/cmd/cli/main.go), [MCP](https://github.com/alash3al/stash/blob/d34ed430c4348ef741ef95146b488aea8616f4fb/cmd/cli/mcp.go), [consolidation](https://github.com/alash3al/stash/blob/d34ed430c4348ef741ef95146b488aea8616f4fb/internal/brain/consolidate.go), [recall](https://github.com/alash3al/stash/blob/d34ed430c4348ef741ef95146b488aea8616f4fb/internal/brain/recall.go), [reasoner](https://github.com/alash3al/stash/blob/d34ed430c4348ef741ef95146b488aea8616f4fb/internal/reasoner/openai.go). Doctrine/design: [agent protocol](https://github.com/alash3al/stash/blob/d34ed430c4348ef741ef95146b488aea8616f4fb/cmd/cli/mcp_prompts.tmpl), [README](https://github.com/alash3al/stash/blob/d34ed430c4348ef741ef95146b488aea8616f4fb/README.md), [setup](https://github.com/alash3al/stash/blob/d34ed430c4348ef741ef95146b488aea8616f4fb/docs/GETTING_STARTED.md). | No material checkout access gap identified. Implementation establishes source behavior, not observed success; doctrine establishes intended use, not agent compliance. External clients, dependency internals and the separate cloud implementation are outside scope. No observed-run or causal-experiment evidence registered. |
