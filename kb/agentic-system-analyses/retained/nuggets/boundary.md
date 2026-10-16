---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Nuggets' shipped TypeScript memory, Pi extensions and messaging gateway at commit 714cab8a3b1fb843aa98dfb51584d2c07a6739f3."
run-id: AAS-2026-10-14-nuggets-c2e87e6916cc-01
result-disposition: complete
target-class: memory/knowledge/context-engineering system
boundary-kind: whole-system
reviewed-boundary: "714cab8a3b1fb843aa98dfb51584d2c07a6739f3"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/NeoVertex1/nuggets
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/nuggets-c2e87e6916cc/related-systems/NeoVertex1--nuggets
  revision: "714cab8a3b1fb843aa98dfb51584d2c07a6739f3"
  sha256: null
---

# Nuggets boundary

## Boundary and evidence

This run analyses the Nuggets implementation shipped in the registered repository: a persistent associative memory system integrated with Pi and a Telegram/WhatsApp assistant gateway. Its intended analytical use is to explain how facts enter, persist, reload and reach later model turns, including maintenance and proactive consumption. The target class is **memory/knowledge/context-engineering system**, not an independent model runtime. The boundary kind is **whole-system** for this shipped implementation, including its gateway drivers rather than treating them as external callers. All evidence is frozen at `714cab8a3b1fb843aa98dfb51584d2c07a6739f3`, with applicability cutoff **2026-10-14** and overall tier **code-grounded**. This is source inspection, not a successful deployment or execution finding.

The target is in scope because its memory is exposed to a model through a Pi tool and injected into subsequent system prompts. The gateway supplies messages and proactive prompts to an external Pi process and consumes its responses. The memory arithmetic itself does not call a model. SRC-1: `.pi/extensions/nuggets.ts`, `src/gateway/pi-rpc.ts`, `src/gateway/router.ts`.

> pi.registerTool({
> name: "nuggets",
> label: "Nuggets Memory",
> --- `.pi/extensions/nuggets.ts`

> return {
> systemPrompt: event.systemPrompt + injection,
> };
> --- `.pi/extensions/nuggets.ts`

The functional inclusions cover the whole shipped memory loop:

- **Production and admission:** explicit remember/forget/list/recall tool handling, preference extraction from input, file-path capture from tool results, task retention before compaction, and kind inference. SRC-1: `.pi/extensions/nuggets.ts`, `src/nuggets/kinds.ts`.
- **Persistence and retrieval:** fact records and hit metadata in JSON, deterministic reconstruction of HRR vectors, key resolution and value decoding, shelf loading and kind-aware routing. SRC-1: `src/nuggets/memory.ts`, `src/nuggets/core.ts`, `src/nuggets/shelf.ts`.
- **Later consumption:** reconstruction from Pi session history, hydration from saved facts, per-turn prompt injection and model-invoked recall. Both gateway entry points, their per-user Pi session directories, message routing, cron jobs and heartbeat prompts belong to the target. SRC-1: `.pi/extensions/nuggets.ts`, `src/gateway/main.ts`, `src/gateway/pi-pool.ts`, `src/gateway/router.ts`, `src/gateway/heartbeat.ts`, `gateway/src/main.ts`.
- **Maintenance:** the legacy-to-kind migration, compaction-triggered promotion writer, schedule request bridge, persisted job loading and one-shot removal. Promotion to a Claude-project `MEMORY.md` is included as a writer; actual reading of that file by Claude is an external-host responsibility, not established here. SRC-1: `src/migrate-memory.ts`, `src/nuggets/promote.ts`, `.pi/extensions/nuggets.ts`, `.pi/extensions/proactive.ts`, `src/gateway/cron.ts`.
- **Evaluation and instructions:** shipped core and memory test source, root usage instructions and model-facing extension prompts. Tests were inspected, not run. Their presence supplies implementation evidence about assertions, not observed-run evidence. SRC-1: `tests/core.test.ts`, `tests/memory.test.ts`, `CLAUDE.md`, `NUGGETS_INSTRUCTIONS.md`, `.pi/extensions/nuggets.ts`, `.pi/extensions/proactive.ts`.

The shipped root entry point establishes that the gateway is not merely a hypothetical external consumer:

> "dev": "tsx src/gateway/main.ts",
> --- `package.json`

> const sessionDir = resolve(SESSIONS_DIR, jidHash(jid));
> mkdirSync(sessionDir, { recursive: true });
> --- `src/gateway/pi-pool.ts`

### Documentation and external limits

The README advertises a newer `nuggets-memory-plugin` and points to a `nuggets-memory/` workspace. That directory is absent from the tracked tree at this revision. This run therefore characterizes the shipped original application, not the advertised npm plugin or its MCP integrations. It neither acquires that package nor infers plugin behavior from the older implementation. This is a missing advertised component, not an uninspected shipped state path. SRC-1: `README.md`, `package.json`, `src/nuggets/index.ts`; repository tree inspection.

> The rest of this README documents the original Nuggets app/gateway project and older non-plugin workflow.
> --- `README.md`

`CLAUDE.md` and `NUGGETS_INSTRUCTIONS.md` prescribe a CLI and the latter describes a Python API. They remain included as shipped doctrine, but the tracked tree and root manifest establish a TypeScript app; these instructions do not establish a shipped Python/CLI implementation. Later findings must keep documentation assertions separate from the inspected code. SRC-1: `CLAUDE.md`, `NUGGETS_INSTRUCTIONS.md`, `package.json`, `src/nuggets/index.ts`.

External dependencies are the installed Pi runtime and extension APIs, model providers and credentials, Node/TypeScript tooling, grammY/Telegram, Baileys/WhatsApp, and the host filesystem. The repository contains the integration code and configuration, not frozen implementations or execution traces for these dependencies. Their exclusion prevents claims about Pi's internal model loop, actual extension discovery, provider behavior, delivery reliability, or external hosts' loading of promoted memory. SRC-1: `package.json`, `.env.example`, `.pi/extensions/nuggets.ts`, `.pi/extensions/proactive.ts`, `src/gateway/pi-rpc.ts`, `src/gateway/telegram.ts`, `src/gateway/whatsapp.ts`, `src/nuggets/promote.ts`.

No live user memory, `.gateway` state, credentials, installed plugin package or observed execution was supplied. The checkout's ignore rules identify local runtime/session directories and an ignored shelf test; this run cannot conclude deployment success, user-level recall quality, promotion effectiveness, or outcomes of that untracked test. These are unavailable evidence, not authorization to execute the target. SRC-1: `.gitignore`, `src/gateway/config.ts`, `src/nuggets/memory.ts`. No material tracked runtime path was inaccessible.

### Top-level coverage

The tracked tree was enumerated at the frozen commit. “Included” means within the functional evidence boundary; the inspection column distinguishes source reads from inventory-only coverage. Excluded publication and artwork are deliberate exclusions, not access failures. Every row is under SRC-1.

| Top-level tracked file or directory | Inclusion | Role and inspected material | Limit / conclusion prevented |
|---|---|---|---|
| `.env.example` | Included | Read provider, channel, process-pool and proactive configuration template. | Template values are not deployment evidence. |
| `.github/` | Excluded | Read `.github/workflows/deploy-blog.yml`: builds `blog/` and publishes GitHub Pages. | No conclusion about successful website publication. No assistant-state loop excluded. |
| `.gitignore` | Included | Read runtime, legacy and test-fixture exclusions. | Ignored files' contents and outcomes are unavailable. |
| `.pi/` | Included | Read `.pi/extensions/nuggets.ts` and `.pi/extensions/proactive.ts` fully: memory tool, capture, reload, prompt injection, compaction/promotion hook, schedule tool and request bridge. | Installed Pi behavior and execution outcomes are not observed. |
| `CLAUDE.md` | Included | Read recall-first and retention instructions. | Instructions alone do not establish CLI availability or compliance. |
| `NUGGETS_INSTRUCTIONS.md` | Included | Read memory usage, CLI/Python interface claims and capacity guidance. | No Python implementation or numerical capacity validation established. |
| `README.md` | Included | Read app architecture, setup, plugin advertisement and intended promotion/proactive behavior. | Declared intent is not proof that every advertised path works. |
| `blog/` | Excluded | Read `blog/package.json` and `blog/astro.config.mjs` to identify an Astro publication site; inventoried `blog/src/`, pages, articles and assets, without reading article claims. | No assessment of published explanations or comparison claims; no runtime memory responsibilities attributed to the blog. |
| `gateway/` | Included | Read `gateway/package.json`, `gateway/tsconfig.json`, `.env.example` and `.gitignore`; compared all `gateway/src/` against `src/gateway/`. The second entry point ships `main.ts`, pool/RPC/router, config, transports, event queue, cron and heartbeat. Differences are the config comment and RPC logging; functional code is covered by the reads of `src/gateway/`. | Not treated as an external app. No claim that either package was built or launched. |
| `images/` | Excluded | Inventoried logo image and `_empty_` marker; README identifies the image as a logo. | No artwork/content assessment; no assistant-state responsibility excluded. |
| `package-lock.json` | Included | Tracked dependency lock inventoried; root dependency declarations read in `package.json`; lock contents not inspected. | No exact transitive-dependency or dependency-security conclusions. |
| `package.json` | Included | Read gateway, setup, migration, test and build entry points and direct dependency declarations. | Commands' presence does not establish successful execution. |
| `src/` | Included | Read all `src/nuggets/{core,memory,shelf,kinds,promote,index}.ts`, `src/{setup,migrate-memory}.ts`, and all `src/gateway/{main,config,pi-pool,pi-rpc,router,telegram,whatsapp,event-queue,cron,heartbeat}.ts`. Covers fact production, persistence, reconstruction, maintenance and later user/proactive consumption. | Static evidence only; model-host internals and live state remain external/unavailable. |
| `tests/` | Included | Read `tests/core.test.ts` and `tests/memory.test.ts`: arithmetic, remember/recall/forget, save/load, hit counting and matching assertions. | Not executed; no end-to-end gateway, extension or promotion outcomes supplied. |
| `tsconfig.json` | Included | Read `src` compilation boundary and output configuration. | No successful compilation established. |

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/NeoVertex1/nuggets` | 714cab8a3b1fb843aa98dfb51584d2c07a6739f3 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/nuggets-c2e87e6916cc/related-systems/NeoVertex1--nuggets`. Implementation: all `src/nuggets/` and `src/gateway/` files, both `.pi/extensions/` files, setup/migration scripts, tests, root and secondary gateway manifests/config; comparison of `gateway/src/` with `src/gateway/`. Doctrine/design: `README.md`, `CLAUDE.md`, `NUGGETS_INSTRUCTIONS.md`, extension tool guidelines/system prompts, heartbeat and RPC prompts. Publication boundary: blog manifest/config and deployment workflow only. Full tree inventoried; initial paths are not an allowlist. | Implementation: [memory](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/memory.ts), [extension](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/.pi/extensions/nuggets.ts), [driver](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/gateway/main.ts), [promotion](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/src/nuggets/promote.ts), [tests](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/tests/memory.test.ts). Doctrine/design: [README](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/README.md), [usage instructions](https://github.com/NeoVertex1/nuggets/blob/714cab8a3b1fb843aa98dfb51584d2c07a6739f3/NUGGETS_INSTRUCTIONS.md). | No material tracked runtime file inaccessible. Advertised `nuggets-memory/` plugin workspace absent: no plugin/MCP behavior conclusion. External Pi/provider/channel implementations and actual host-memory consumption not frozen: only integration behavior can be assessed. No supplied observed run or causal experiment: no operational-success, performance or effectiveness finding. Publication articles/artwork deliberately excluded; dependency locks inventoried but unread, preventing article/comparison and transitive-dependency conclusions. |
