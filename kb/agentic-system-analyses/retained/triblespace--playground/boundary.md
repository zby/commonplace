---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Playground's shipped sandbox MCP provider and optional native-worker gateway at de28ac8fdda30c7a5c2ee099de089e65a685195f."
run-id: AAS-2026-10-14-playground-88ee8a292f9b-01
result-disposition: complete
target-class: extension or tool mechanism
boundary-kind: whole-system
reviewed-boundary: de28ac8fdda30c7a5c2ee099de089e65a685195f
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/triblespace/playground
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/playground-88ee8a292f9b/related-systems/triblespace--playground
  revision: de28ac8fdda30c7a5c2ee099de089e65a685195f
  sha256: null
---

# Playground boundary

## Boundary and evidence

This analysis covers the shipped Playground executable as an agent-facing sandbox MCP provider, including its optional authenticated gateway to native Faculties workers. Its intended use is to expose isolated shell execution and file exchange to an enclosing agent client. It qualifies as an **extension or tool mechanism**, not an enclosing model runtime: MCP clients supply commands, and the optional worker route serves a separately configured native MCP process. The provider need not issue model calls itself to fall within this analysis. SRC-1: `README.md`, `src/main.rs`, `src/mcp.rs`, `src/mcp_http/workers.rs`.

> `playground` provisions isolated, stateful shells and exposes them over the
> [Model Context Protocol](https://modelcontextprotocol.io/). It is the exec
> transport an MCP client (e.g. an agent runtime) calls to run shell commands in
> an isolated sandbox. This crate is only the provider.
> --- `README.md`

The boundary is **whole-system for that shipped provider**, rather than a library-only view. It includes operator provisioning and credential commands, sandbox construction and reattachment, persistent tenant storage and identity setup, model-facing session/file/execution tools, bounded job retention and consumption, authentication and session admission, shutdown and destruction, and the optional worker gateway and shipped worker supervisor. These responsibilities occur in the same repository and are not excluded merely because a CLI or service script drives an API. SRC-1: `src/main.rs`, `src/mcp.rs`, `src/jobs.rs`, `src/sandbox/mod.rs`, `deploy/freebsd/playground_mcp`, `deploy/freebsd/playground_faculties`.

The executable dispatch was traced from `main` to stdio serving, HTTP serving, and user provisioning. In sandbox mode, these construct a `SandboxProvider` with a backend; its session registry calls the backend and its execution path uses `JobManager`. HTTP startup selects either backend reattachment or the worker route. The FreeBSD worker service calls `user attach` and launches an externally supplied Faculties binary with fixed tenant storage, key, persona, and internal bearer. That service is included; the binary it launches is an external dependency. SRC-1: `src/main.rs`, `src/mcp.rs`, `src/sandbox/mod.rs`, `src/mcp_http/workers.rs`, `deploy/freebsd/playground_faculties`.

>     let server = if args.faculties_workers.is_some() {
>         None
>     } else {
> --- `src/main.rs`

> 	    PILE=/pile/self.pile TRIBLESPACE_KEY=/pile/self.key PERSONA="$worker_persona" \
> 	    /opt/faculties/faculties mcp --pile /pile/self.pile --key /pile/self.key \
> 	    --http-listen "$worker_address" --http-token-file /var/run/faculties-mcp/token
> --- `deploy/freebsd/playground_faculties`

Repository documents also describe a cognition/model-worker loop and hierarchical memory assembly. Those are retained design evidence, not proof that this executable implements that loop. The current command enum and module graph expose provider, account, invite, and cleanup commands; they do not expose the `run`/`exec` model-loop commands described by older design material. Shipped prompts and archive importer fragments remain visible in coverage below, but are not attributed as executable provider behavior. This boundary cannot establish the external runtime's memory-cover algorithm, model scheduling, reflection, or archive ingestion behavior. SRC-1: `src/main.rs`, `Cargo.toml`, `design.md`, `docs/playground_memory_architecture.md`, `prompts/system_prompt.md`, `importers/archive_import_chatgpt.rs`.

> Playground is a minimal, deterministic loop that turns LLM output into execution
> requests and feeds results back into the cognition graph. The core stays
> small: **LLM result → exec request → exec result → new prompt**. Any external
> messaging (Teams, email, etc.) is treated as a separate faculty and not part of
> the core.
> --- `design.md`

### Tracked top-level coverage

The table accounts for every tracked root entry at the frozen commit. “Included” grants later inspection at this same pin; it does not mean every line has already been inspected. Initial inspection traced entry points and responsibilities, not exhaustive correctness. Deliberately excluded material is distinguished from unavailable external implementations and from included files not yet read in detail.

| Root entry | Treatment and material paths | Role and limits |
|---|---|---|
| `.gitignore` | Included as build housekeeping; contents not yet inspected | No executable responsibility inferred from ignore rules. |
| `Cargo.lock` | Included as dependency pinning; contents not yet inspected | No dependency implementation or supply-chain correctness established. |
| `Cargo.toml` | Included; inspected | Package, features, and executable dependency graph. No external crate behavior established. |
| `README.md` | Included; inspected | Current provider contract, tools, lifecycle, backends, worker route, and installation intent. Not a deployment receipt. |
| `deploy/` | Included: `freebsd/playground_mcp`, `playground_faculties`, service examples, `Caddyfile`, `README.md`, `native-workers.md`, `smoke.sh`, and `tests/` | Shipped host integration, tenant-worker supervision, proxy/configuration, operational procedures, and checks. Both service launch paths inspected; guides, proxy, examples, and check bodies remain for detailed inspection. No actual host configuration or successful rollout is established. |
| `design.md` | Included as doctrine/design; opening model-loop description inspected | Alternate/older loop intent must be distinguished from the current provider entry points. Cannot prove a shipped model loop. |
| `docs/` | Included as doctrine/design: `playground.md`, `playground_event_model.md`, `playground_memory_architecture.md`, `memory_temporal_redesign.md`, `teams.md`, `teams_scopes.md`, `linux-sandbox-backend.md` | Memory architecture inspected; other documents initially inventoried or title-searched, not read in detail. Described memory, Teams, model-worker, and proposed backend behavior cannot substitute for implementation inspection. |
| `faculties` | Excluded external implementation; tracked symlink target `../faculties` inspected without following it | Native tools and worker implementation live outside this Git source. Prevents conclusions about their memory/knowledge semantics, model calls, and tool execution beyond the provider's integration contract. |
| `iki-874a-fixed.md` | Excluded; empty file | Supplies no substantive evidence or executable responsibility. |
| `importers/` | Deliberately excluded from executable provider behavior: `archive_import_chatgpt.rs`, `archive_import_claude_code.rs`, `archive_import_codex.rs`, `archive_import_copilot.rs`, `archive_import_gemini.rs` | Tracked archive fragments are outside the current main module graph; ChatGPT fragment inspected initially. Prevents an account of functioning archive persistence, reload, and later memory consumption; these are not silently treated as a shipped provider loop. |
| `prompts/` | Included as doctrine/design: `system_prompt.md`, `system_prompt_corpo.md` | Base prompt read; corporate variant initially inventoried. Model-shell conduct and memory-maintenance instructions are authored here, but no current provider prompt-loading path was established. Prevents claims of their actual enforcement or consumption by an external model. |
| `rust-toolchain.toml` | Included as build configuration; contents not yet inspected | No build success or platform portability established. |
| `scripts/` | Included: `lima-session.yaml.tmpl`, fallback `lima.yaml.tmpl`, `migrate_timestamps.rs`, `rewrite-links.sh`, `view_telemetry.rs` | Session template and fallback selection traced through `src/sandbox/lima.rs`; auxiliary maintenance scripts inventoried by source comments. The fallback template is not excluded despite its older model-loop prose. Detailed script behavior remains uninspected; no migration outcome or autonomous memory maintenance is established. |
| `src/` | Included: `main.rs`, `mcp.rs`, `mcp_http.rs`, `mcp_http/workers.rs` and its test modules, `oauth.rs`, `jobs.rs`, `user_attach_tests.rs`, and `sandbox/{mod,faculties,jail,lima,policy,proc,runner}.rs` | Complete provider responsibility surface: state production, persistence/reattachment, admission, execution, result consumption, and lifecycle. Initial entry-point, trait, routing, and backend-policy inspection; detailed implementations and test bodies are not all read. No target execution, isolation proof, or exhaustive security assessment is implied. |
| `tests/` | Included: `cli_smoke.rs`, `cli_gateway.rs` | Shipped executable-facing checks for serving and gateway integration; headers and gateway setup inspected. Tests were not run. Source assertions are not observed successful operations. |

All source-dependent coverage classifications refer to SRC-1 at the paths named in the table.

### Dependencies and evidence limits

External dependencies include MCP clients and their model providers, Faculties source/binaries and their storage libraries, Lima and its guest environment, FreeBSD jail/ZFS/process facilities, SSH where selected, operator-created templates and shared storage, credentials, and reverse-proxy/network configuration. Playground's own provisioning, mounts, environment setup, credential authority, forwarding, and supervision glue are included. Implementations and deployed state outside this repository are not frozen evidence. Their exclusion prevents end-to-end claims about agent decision-making, native memory correctness, host isolation, egress containment, and public availability. SRC-1: `README.md`, `src/sandbox/faculties.rs`, `src/sandbox/jail.rs`, `src/sandbox/lima.rs`, `deploy/freebsd/playground_faculties`.

The frozen source is the acquired Git checkout at **de28ac8fdda30c7a5c2ee099de089e65a685195f**; its HEAD was verified at that revision. The applicability cutoff is **2026-10-14**, the supplied run date, not a claim about the commit's timestamp. Overall evidence is **code-grounded**, supplemented by source-native design and contract prose. No target, test, example, provider service, or model was executed. No independent run trace or causal experiment was supplied. Later jobs may inspect additional blobs in this registered repository at this commit, but may not add external dependencies or newer revisions as evidence.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/triblespace/playground` | de28ac8fdda30c7a5c2ee099de089e65a685195f | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/playground-88ee8a292f9b/related-systems/triblespace--playground`. Implementation: tracked tree, manifest, main dispatch/server construction/provisioning, provider/session registry, backend trait, worker manifest/admission, Lima template selection, service launch/attachment, and gateway test setup. Doctrine/design: README, design opening, full base prompt and memory-architecture document, and bounded backend/script/test comment searches. Remaining included paths are registered but not all inspected in detail. | Implementation: [entry points](https://github.com/triblespace/playground/blob/de28ac8fdda30c7a5c2ee099de089e65a685195f/src/main.rs), [provider](https://github.com/triblespace/playground/blob/de28ac8fdda30c7a5c2ee099de089e65a685195f/src/mcp.rs), [worker routing](https://github.com/triblespace/playground/blob/de28ac8fdda30c7a5c2ee099de089e65a685195f/src/mcp_http/workers.rs), [worker service](https://github.com/triblespace/playground/blob/de28ac8fdda30c7a5c2ee099de089e65a685195f/deploy/freebsd/playground_faculties). Doctrine/design: [provider contract](https://github.com/triblespace/playground/blob/de28ac8fdda30c7a5c2ee099de089e65a685195f/README.md), [memory description](https://github.com/triblespace/playground/blob/de28ac8fdda30c7a5c2ee099de089e65a685195f/docs/playground_memory_architecture.md), [prompt](https://github.com/triblespace/playground/blob/de28ac8fdda30c7a5c2ee099de089e65a685195f/prompts/system_prompt.md). Other initial paths are named above. | Repository code is available, not an access gap. External Faculties implementation, enclosing agent/model runtime, operator host state, and actual execution evidence are outside the frozen set. Implementation supports source-level provider behavior, not successful deployed operation; doctrine/design supports declared intent, not current model-loop implementation. |
