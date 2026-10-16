---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Memex's shipped wiki-production, maintenance and query system at commit 1e223b6045be31b70b1ab9e4b28dd403150d29e7."
run-id: AAS-2026-10-14-memex-42ecde52cc05-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "1e223b6045be31b70b1ab9e4b28dd403150d29e7"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/wastedcode/memex
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/memex-42ecde52cc05/related-systems/wastedcode--memex
  revision: "1e223b6045be31b70b1ab9e4b28dd403150d29e7"
  sha256: null
---

# Memex boundary

## Boundary and evidence

This run analyses Memex as a **memory/knowledge/context-engineering system**, not merely its exported client API. Its intended use is a persistent personal wiki built and maintained from supplied sources and consumed by later questions. Memex's daemon delegates model-dependent file work to external Claude Code processes. The source-native declared purpose is supported by the shipped ingest and query prompts (SRC-1, `README.md`, `src/lib/prompts/ingest.ts`, `src/lib/prompts/query.ts`):

> Instead of retrieving from raw documents at query time, Memex has the LLM **incrementally build and maintain a persistent wiki** — a structured, interlinked collection of markdown files that sits between you and your sources.
> --- `README.md`

The **whole-system** boundary includes the packaged CLI, exported Unix-socket client, daemon, request admission and ownership handling, wiki scaffolding and raw-file upload, SQLite registry/jobs/audit state, restart recovery, serial per-wiki queue, manual and automatic lint scheduling, runner, credential/configuration handling, mount wrapper, all shipped prompts and deployment/build definitions. This covers the shipped paths that produce, retain, reload, maintain and consume wiki state. The CLI and daemon are included callers, not excluded enclosing applications (SRC-1, `package.json`, `src/index.ts`, `src/daemon.ts`, `src/daemon/routes.ts`, `src/daemon/scaffold.ts`, `src/daemon/db.ts`, `src/daemon/queue.ts`, `src/daemon/runner.ts`).

The entry-point trace is package binary → `src/index.ts` → command modules → `src/cli/client.ts` → server/routes → scaffold or database/queue → runner → Claude Code. `serve` enters `src/daemon.ts`; startup reopens database state and resumes pending work. Ingest uploads raw bytes before submitting a job. Query submits a new job that instructs Claude to read retained wiki files; lint is a model-driven maintenance job. File browsing through the exported client and routes is also included (SRC-1, `src/cli/commands/serve.ts`, `src/cli/commands/ingest.ts`, `src/cli/commands/query.ts`, `src/cli/commands/lint.ts`, `src/cli/client.ts`, `src/daemon.ts`, `src/daemon/routes.ts`). The load-bearing retained-state consumption instruction is:

> To answer:
> - Read _index.md to understand what's in the knowledge base
> - Search for relevant files using grep and glob
> - Read the files that seem relevant
> - Synthesize an answer grounded in what you found
> --- `src/lib/prompts/query.ts`

The runner supplies the wiki system prompt on each delegated invocation (SRC-1, `src/daemon/runner.ts`):

> const systemPrompt = getWikiSystemPrompt();
>     args.push('--append-system-prompt', systemPrompt);
> --- `src/daemon/runner.ts`

These passages establish model-dependent operation and the intended later use of persistent content. They do not establish that Claude follows the instructions or that generated content improves with use.

### Frozen evidence and external limits

The evidence is the single acquired Git repository at full commit **1e223b6045be31b70b1ab9e4b28dd403150d29e7**, unchanged. The checkout's HEAD matched this revision and its working-tree status was clean when inspected. The applicability cutoff is **2026-10-14**; this does not assert anything about later revisions or deployed versions. The overall tier is **code-grounded**: executable source supports implementation accounts, while README and documentation support attributed intent. No target code, tests, examples or services were executed.

External dependencies are Claude Code and its model/authentication services, Linux namespace/mount and Unix-socket facilities, Node.js, `better-sqlite3`, `commander`, build tooling and any operator-configured MCP services (SRC-1, `package.json`, `binding.gyp`, `src/daemon/namespace.ts`, `src/daemon/peercred.c`, `src/daemon/auth.ts`, `src/daemon/runner.ts`). Their implementations and live behavior are outside this source boundary. Thus this run cannot establish Claude's actual instruction discovery, tool enforcement, model quality, provider reliability or configured MCP behavior. It can examine what Memex passes to them. Host filesystem confinement must be assessed from the mount wrapper rather than accepted from the README's stronger isolation claims (SRC-1, `README.md`, `src/daemon/namespace.ts`).

No execution traces, populated user wikis, curated evaluation corpus or causal experiments were supplied. The tracked tree contains no executable test/evaluation suite; `docs/prompts.md` supplies a proposed sequential prompt-testing procedure, not results. This prevents claims of observed cross-session improvement, measured answer quality, verified isolation or successful recovery under failure. These are evidence limits, not missing shipped paths (SRC-1, `docs/prompts.md`, `package.json`, repository tree at the frozen commit).

### Top-level coverage

All tracked top-level files and directories were inspected. No material shipped responsibility is deliberately excluded. The table records functional coverage, not a claim of exhaustive correctness review. Each path below belongs to SRC-1.

| Top-level tracked path | Treatment and material inspected paths | Role and conclusion limit |
|---|---|---|
| `.gitignore` | Included; inspected completely | Identifies ignored generated/build/local state; does not supply those artifacts or deployed state. |
| `LICENSE` | Included; inspected completely | Distribution terms; no operational evidence. |
| `README.md` | Included; inspected completely | Product purpose, usage and customization claims; claims are not observed operation. |
| `binding.gyp` | Included; inspected completely | Native peer-credential addon build definition; compilation was not tested. |
| `docs/` | Included; `docs/architecture.md`, `docs/operations.md`, `docs/prompts.md`, all complete | Architecture, lifecycle, operator maintenance/backup and prompt evaluation instructions; no evaluation results. |
| `esbuild.config.js` | Included; inspected completely | Standalone bundling entry point and external dependencies; build success untested. |
| `package-lock.json` | Included; inspected completely in bounded ranges | Dependency lock metadata; dependency internals are not captured or audited. |
| `package.json` | Included; inspected completely | Binary/export surfaces, dependencies, build/install scripts and packaged files; published package bytes are not evidence. |
| `src/` | Included; `src/index.ts`, `src/daemon.ts`; `src/cli/client.ts`; every command under `src/cli/commands/`: `serve.ts`, `create.ts`, `destroy.ts`, `config.ts`, `login.ts`, `setup-token.ts`, `chown.ts`, `ingest.ts`, `query.ts`, `lint.ts`, `logs.ts`, `list.ts`, `status.ts` | Entrypoints, callers, uploads, job submission/polling, retained result consumption, configuration and ownership. All read completely. No CLI or API behavior was executed. |
| `src/` (continued) | Included; every daemon module: `src/daemon/server.ts`, `src/daemon/routes.ts`, `src/daemon/db.ts`, `src/daemon/scaffold.ts`, `src/daemon/queue.ts`, `src/daemon/runner.ts`, `src/daemon/auth.ts`, `src/daemon/namespace.ts`, `src/daemon/peercred.ts`, `src/daemon/peercred.c` | Admission, retained wiki files, registry/queue/audit persistence and reload, maintenance scheduling, delegated calls, authentication and mount/socket integration. All read completely; correctness/security and recovery remain source-level assessments. |
| `src/` (continued) | Included; `src/lib/constants.ts`, `src/lib/errors.ts`, `src/lib/types.ts`; all shipped prompts: `src/lib/prompts/wiki.ts`, `src/lib/prompts/ingest.ts`, `src/lib/prompts/query.ts`, `src/lib/prompts/lint.ts` | Limits, contracts, system instructions, state-production and later-consumption instructions, maintenance criteria; all complete. Prompt compliance and generated outputs are unobserved. |
| `systemd/` | Included; `systemd/memex.service`, complete | Shipped daemon deployment, capability and restart settings; host deployment was not inspected. |
| `tsconfig.json` | Included; inspected completely | Compilation scope and output definitions; generated `dist/` is not part of the tracked source evidence. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/wastedcode/memex` | 1e223b6045be31b70b1ab9e4b28dd403150d29e7 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/memex-42ecde52cc05/related-systems/wastedcode--memex`. Implementation: complete `src/` tree, package/build/dependency definitions and `systemd/memex.service`, as enumerated above. Doctrine/design: complete `README.md`, all three `docs/` documents and shipped prompt/scaffold instruction text. Complete tracked-tree inventory and all tracked files inspected. | Implementation: [CLI entry](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/index.ts), [daemon startup](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon.ts), [runner](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/runner.ts), [persistent state](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/daemon/db.ts). Doctrine/design: [product account](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/README.md), [wiki instructions](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/wiki.ts), [query instructions](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/src/lib/prompts/query.ts), [evaluation procedure](https://github.com/wastedcode/memex/blob/1e223b6045be31b70b1ab9e4b28dd403150d29e7/docs/prompts.md). | No unavailable tracked files. External Claude Code/provider/dependency implementations and operator state are not captured; prevents attributing their internals or verified behavior to Memex. No observed run or causal experiment layer; prevents measured quality, compliance, confinement and failure-recovery claims. Documentation and prompt instructions establish intent, not successful execution. |
