---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Letta Code's shipped agent harness, local backend and hosted-service client at commit 271f119dcf37d58649a18e6c733386b3c710a456."
run-id: AAS-2026-10-12-letta-code-be76afeab9b7-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "271f119dcf37d58649a18e6c733386b3c710a456"
analysis-cutoff: "2026-10-12"
evidence-tier: code-grounded
source:
  identity: https://github.com/letta-ai/letta-code
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/letta-code-workflow-be76afeab9b7/related-systems/letta-ai--letta-code
  revision: "271f119dcf37d58649a18e6c733386b3c710a456"
  sha256: null
---

# Letta Code boundary

## Boundary and evidence

This run analyses the shipped Letta Code harness to explain how persistent agents operate across terminal sessions, headless requests and server/channel interfaces. The target is the repository's complete shipped system, not just its memory API. Memory creation, editing, validation, synchronization, reflection and later context consumption belong to the boundary, alongside the foreground execution loop. The intended result is a source-grounded account, not a deployment test or a claim that learning improves outcomes.

### Classification and entry-point trace

Letta Code qualifies as an **enclosing runtime**: its shipped command selects an agent/backend, drives conversation turns and executes approvals; its local backend also constructs the provider-call executor. Hosted execution is a client path within this runtime, not evidence that Code implements the external Letta service. The **whole-system** boundary includes all repository-shipped drivers and their state responsibilities. It does not include external services or applications merely because they connect to those drivers. SRC-1: `src/index.ts`, `src/headless.ts`, `src/cli/app/use-conversation-loop.ts`, `src/agent/message.ts`, `src/backend/backend.ts`, `src/backend/local/local-executor-factory.ts`.

The build's main entry is `src/standalone-entry.ts`, which imports `src/index.ts`; that entry dispatches subcommands before interactive initialization and routes headless execution to `handleHeadlessCommand`. The package also exports App Server clients, memory contracts, MCP helpers, presets, schedules and channel/gateway interfaces. These exports are included, not treated as a different target. The Python package launches the bundled CLI rather than supplying an independent agent runtime. SRC-1: `build.js`, `package.json`, `src/standalone-entry.ts`, `src/index.ts`, `python/letta_code/__init__.py`.

> // Subcommands exit before TUI initialization and tool bootstrapping.
> const subcommandResult = await runSubcommand(subcommandArgs);
> --- `src/index.ts`

The server command explicitly dispatches both shipped server modes:

> if (command.kind === "app-server") {
>     return runAppServerSubcommand(command.argv);
>   }
>
>   return runListenSubcommand(command.argv);
> --- `src/cli/subcommands/server.ts`

The local backend is not merely a storage library. Its default executor wraps a provider stream adapter:

> return new ProviderTurnExecutor(
>     new PiStreamAdapter({
>       stream: options.stream,
>       localProviderAuthStorageDir: options.storageDir,
>       modelsRuntime,
>       onContextWindowOverflow,
>       onContextPressure,
>       onLlmStart,
>       onLlmEnd,
>     }),
>   );
> --- `src/backend/local/local-executor-factory.ts`

### State-loop inclusions

The boundary includes agent creation and settings; local agent/conversation/transcript storage; hosted API adapters; prompt compilation and skills discovery; foreground and background tool execution; permission/sandbox checks; memory Git repositories and worktrees; shared/attached memory; memory admission constraints and Git hooks; post-turn synchronization; transcript-based reflection; conflict repair and integration; recall/search; schedules; mods and hooks; listener/App Server/channel ingress and outbound notifications. SRC-1: `src/headless.ts`, `src/backend/local/local-backend.ts`, `src/backend/local/local-store.ts`, `src/agent/message.ts`, `src/reminders/memory-git-sync.ts`, `src/cli/helpers/reflection-launcher.ts`, `src/websocket/listener/turn-completion.ts`, `src/websocket/listener/turn-cleanup.ts`, `package.json`.

The initial trace reaches both maintenance and subsequent consumption. Listener completion appends transcript deltas and evaluates reflection; listener cleanup invokes memory sync. Local prompt compilation compares the committed MemFS revision against retained compiled state and can prepare a memory-update message. These paths are included even when they run after the visible foreground response. SRC-1: `src/websocket/listener/turn-completion.ts`, `src/websocket/listener/turn-cleanup.ts`, `src/backend/local/local-backend.ts`.

> if (
>       existing?.rawSystemHash === rawSystemHash &&
>       existing.memfsRevision === memfsRevision
>     ) {
>       return existing;
>     }
> --- `src/backend/local/local-backend.ts`

Shipped memory and reflection instructions supply design evidence, not proof that a model follows them. They are part of the operational mechanism rather than excluded documentation. SRC-1: `src/agent/prompts/letta_local_memfs.md`, `src/agent/subagents/builtin/reflection-v2.md`, `src/skills/builtin/initializing-memory/SKILL.md`.

> The MemFS is a git-backed projection of your memory. Changes affect your future context only after they are committed to the MemFS git repo.
> --- `src/agent/prompts/letta_local_memfs.md`

> **You can make two kinds of updates:**
> 1. **Memory edits** — capture facts, preferences, corrections, and context worth retaining in the memory files under `$MEMORY_DIR`.
> 2. **Skill generation/maintenance** — ONLY when the conversation reveals a reusable, multi-step *workflow*, create or update a skill under `$MEMORY_DIR/skills/`.
> --- `src/agent/subagents/builtin/reflection-v2.md`

### Frozen evidence and limits

The acquired checkout is clean and its HEAD equals `271f119dcf37d58649a18e6c733386b3c710a456`. That full commit is the reviewed boundary; the applicability cutoff is **2026-10-12**, the opening's run date. The overall tier is **code-grounded**, combining implementation text with repository-declared design. Only this Git repository at this commit is registered. No external documentation, dependencies, captures, execution traces or experimental results are added.

External Letta Cloud/self-hosted service internals, model-provider internals, the desktop application's implementation, hosted browser UI and messaging-network implementations are unavailable within this source. This prevents conclusions about their internal state retention, server-side dreaming, routing guarantees, provider inference behavior or end-to-end cross-device reliability. Their observable client contracts in this repository remain included. Package declarations identify external SDKs and provider libraries, but do not freeze their implementation. SRC-1: `README.md`, `package.json`, `src/backend/backend.ts`, `src/channels/README.md`.

No target, tests or examples were executed. Test source establishes intended checks, not passing results, observed operation, causal improvement, memory quality or production latency. Dynamic user-installed skills, mods, hooks, channel plugins and live agent memories are not captured; included loaders and shipped defaults cannot establish behavior of arbitrary installed content. External URLs in repository documentation are references only and are not independent evidence. SRC-1: `src/backend/local-system-prompt-compilation.test.ts`, `src/channels/README.md`, `README.md`.

### Top-level coverage

Every top-level tracked entry is classified below. “Included” defines the source scope, not a claim that every file has been read. Initial inspection traced the material foreground, memory-maintenance and memory-consumption paths above. Tree/search inspection and file inspection are distinguished. Included paths not yet read are available evidence for later jobs, not access gaps. Deliberate exclusions below remove build/development detail from behavioral conclusions, not shipped runtime responsibilities.

| Top-level entry | Treatment and material paths | Initial inspection and limits |
|---|---|---|
| `src/` | Included: `index.ts`, `standalone-entry.ts`, `headless.ts`; `cli/app/` and `cli/subcommands/`; `backend/local/`, `backend/api/`, shared executors in `backend/dev/`; `agent/` prompts, creation, memory Git/worktrees, skills and subagents; `reminders/`; `tools/`; `permissions/`, `sandbox/`; `websocket/`, `channels/`, `web/`, `cron/`, `queue/`, `mods/`, `hooks/`; auth, providers, telemetry, settings, LSP, updater and utilities. Tests, integration tests and test utilities are included as evaluator source. | Tree inspected. Files/ranges inspected in the entry, local executor, local backend/store, memory compiler/sync, reflection triggers/launcher, listener completion/cleanup, channel contract and memory prompt/skill paths. Test setup inspected in `backend/local-system-prompt-compilation.test.ts`; other evaluators inventoried, not run. Remaining implementation is available but not yet inspected in detail. |
| `package.json` | Included: binary, exports, dependencies and build/test commands. | Read completely; defines shipped surfaces, not installed dependency behavior. |
| `build.js` | Included: standalone entry, public-library entrypoints and bundled-skill copying. | Targeted search; build execution and produced bytes not verified. |
| `bin/` | Included: `letta.js` platform-binary launcher. | Read; distribution path, not a separate loop. |
| `python/` | Included: `letta_code/__init__.py`, packaging backend and wheel metadata. | Tree and launcher read; packaging backend not yet inspected. No separate Python agent API inferred. |
| `docker/` | Included: `Dockerfile`, `entrypoint.sh` deployment and cron launcher. | Entrypoint read, Dockerfile entry searched; deployed-image behavior unobserved. |
| `nix/` | Included: `modules/home-manager.nix`, `modules/nixos.nix` launch/service configuration. | Tree/search only; service lifecycle not yet inspected. |
| `flake.nix` | Included distribution/launch configuration. | Targeted search only; no installed-flake claim. |
| `bun.nix` | Included distribution dependency configuration. | Inventoried, not yet read; no Nix dependency-resolution claim. |
| `flake.lock` | Included declared distribution pin. | Inventoried, not resolved or executed. |
| `hooks/` | Included shipped example hooks: memory logger, prompt instructions, permission status, notifications, API-key retrieval and change checks. | Tree inspected; contents not yet read. No claim of default activation or actual logging. |
| `vendor/` | Included terminal/UI patches in `ink/` and `ink-text-input/`. | Tree inspected; rendering details not yet read. |
| `scripts/` | Included build/postinstall/packaging support, test runners, latency benchmark and `mod-learning/learn-mod.ts`; agent-watch scripts included as repository improvement automation, not an agent's ordinary memory loop. | Tree and package consumers inspected; script contents not yet read. No measured benchmark or improvement-automation success claimed. |
| `docs/` | Included `examples/mods/` and learning configurations, `nix.md`; `plans/` as design proposals only. | Tree inspected; examples/proposals not yet read. Plans cannot establish shipped behavior. |
| `README.md` | Included usage and declared architecture. | Read completely; external linked pages excluded. |
| `AGENTS.md` | Included repository development instructions as design/support context, not automatically a runtime system prompt. | Inventoried, not yet read. |
| `CLAUDE.md` | Included repository development instructions with the same restriction. | Inventoried, not yet read. |
| `AI_POLICY.md` | Excluded contribution-policy detail. | Prevents conclusions about compliance with repository AI-contribution policy. |
| `CONTRIBUTING.md` | Excluded contribution-process detail. | Prevents conclusions about contributor workflow and governance. |
| `LICENSE` | Excluded legal analysis. | No licensing/compliance conclusion. |
| `assets/` | Included shipped visual assets; not memory evidence. | Top-level inventory only; no visual-product assessment. |
| `.github/` | Included release/build/test workflows, tool/skill-sync and agent-watch automation; issue templates and PR media excluded from runtime analysis. | Recursive tree inspected. Workflow/prompt contents not yet read; no CI/release outcome or automation effectiveness claim. |
| `.skills/` | Included developer skills `adding-models/` and `capturing-tui-visual-proof/`, distinct from runtime `src/skills/builtin/`. | Tree inspected; content not yet read. No runtime auto-loading inferred. |
| `.cursor` | Excluded editor-specific development configuration. | No Cursor integration conclusion. |
| `.editorconfig` | Excluded editor formatting configuration. | No editor-enforcement conclusion. |
| `.gitattributes` | Excluded Git development configuration. | No checkout-normalization analysis. |
| `.gitignore` | Excluded development ignore rules. | No generated-file completeness claim. |
| `.husky/` | Excluded developer `pre-commit` automation; not the included MemFS hooks under `src/agent/`. | Tree inspected; no developer-hook enforcement conclusion. |
| `biome.json` | Excluded development lint configuration. | No lint-policy assessment. |
| `bun.lock` | Included declared application dependency pin. | Inventoried, not resolved; dependency source is not registered. |
| `bunfig.toml` | Included build/test runtime configuration. | Inventoried, not yet read. No test-environment claim. |
| `npm-shrinkwrap.json` | Included published dependency pin. | Inventoried, not resolved; no installed dependency behavior claimed. |
| `tsconfig.json` | Included source compilation configuration. | Inventoried, not yet read. No compiler correctness claim. |
| `tsconfig.types.json` | Included public-type build configuration. | Inventoried, not yet read. No generated-declaration verification. |

The table's implementation and design scopes refer to SRC-1. The source register permits further inspection anywhere in this repository at the pinned commit, while keeping the stated external exclusions and evidence-layer limits.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/letta-ai/letta-code` | 271f119dcf37d58649a18e6c733386b3c710a456 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/letta-code-workflow-be76afeab9b7/related-systems/letta-ai--letta-code`. Implementation: tracked top-level/selected recursive trees; package/build entrypoints; `bin/letta.js`; Python/container launchers; `src/index.ts` startup; headless and TUI consumers by search; `src/backend/backend.ts` by search; local backend, executor, store and compiler by ranges/search; message preparation; reflection launcher/triggers; memory sync; listener completion/cleanup; local prompt-compilation test setup. Doctrine/design: `README.md`; `src/agent/prompts/README.md`; selected local MemFS prompt, reflection-v2 and initialization-skill passages; channel contract. | Implementation: [build](https://github.com/letta-ai/letta-code/blob/271f119dcf37d58649a18e6c733386b3c710a456/build.js), [entry](https://github.com/letta-ai/letta-code/blob/271f119dcf37d58649a18e6c733386b3c710a456/src/index.ts), [local executor](https://github.com/letta-ai/letta-code/blob/271f119dcf37d58649a18e6c733386b3c710a456/src/backend/local/local-executor-factory.ts), [local backend](https://github.com/letta-ai/letta-code/blob/271f119dcf37d58649a18e6c733386b3c710a456/src/backend/local/local-backend.ts), [post-turn sync](https://github.com/letta-ai/letta-code/blob/271f119dcf37d58649a18e6c733386b3c710a456/src/reminders/memory-git-sync.ts). Doctrine/design: [README](https://github.com/letta-ai/letta-code/blob/271f119dcf37d58649a18e6c733386b3c710a456/README.md), [local prompt](https://github.com/letta-ai/letta-code/blob/271f119dcf37d58649a18e6c733386b3c710a456/src/agent/prompts/letta_local_memfs.md), [reflection instructions](https://github.com/letta-ai/letta-code/blob/271f119dcf37d58649a18e6c733386b3c710a456/src/agent/subagents/builtin/reflection-v2.md). | No identified inaccessible material path in the pinned checkout. External services, provider/SDK internals, desktop/browser hosts and dynamic user content are not captured: no claims about their internals or complete deployed loop. No observed runs or experiments: no passing-test, reliability, learning-quality or causal-effect claim. Initially uninspected repository files remain available, not access gaps. |
