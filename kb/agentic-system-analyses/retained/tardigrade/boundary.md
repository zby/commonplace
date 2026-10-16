---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Tardigrade's shipped agent framework, hosts, callers and improvement instructions at commit 1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8."
run-id: AAS-2026-10-15-tardigrade-455e1aaccd4d-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: "1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8"
analysis-cutoff: "2026-10-15"
evidence-tier: code-grounded
source:
  identity: https://github.com/clavia-labs/tardigrade
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/tardigrade-455e1aaccd4d/related-systems/clavia-labs--tardigrade
  revision: "1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8"
  sha256: null
---

# Tardigrade boundary

## Boundary and evidence

This run analyses Tardigrade as a framework for constructing and hosting agents, including the shipped paths that admit requests, derive state, execute model and tool work, persist results, recover state and expose replies. Its primary target class is **enclosing runtime**, not a memory-only library or an external runtime's client. Retained conversation state and model-context compaction are parts of that runtime. The boundary is **whole-system**: current atom APIs, exported deprecated component APIs, platform implementations, shipped applications and examples, and authoring and improvement instructions remain in scope. They must be distinguished rather than treated as one interchangeable API generation.

The source's own statement of purpose supports this target selection (SRC-1, `README.md`):

> Tardigrade is a typescript framework for building composable agents around an immutable event log. It is built on [Effect TS](https://effect.website/) and takes a functional approach to managing agent state and effects, drawing inspiration from [Elm](https://elm-lang.org/), and [Jotai](https://jotai.org/).
> --- `README.md`

The implementation goes beyond returning a model computation. The default actor composes permissions, budgets, tools, conversation compaction and inference, and supplies message methods (SRC-1, `packages/agent/src/agent.ts`). Inference proposes model work and handles recorded results and turn settlement (SRC-1, `packages/agent/src/atoms/infer.ts`). The model service actually calls the configured provider abstraction; this is implementation evidence of a model-dependent system, not evidence of a successful provider run:

> const stream = responseFormat === undefined
>         ? languageModel.streamText(request)
>         : languageModel.streamText(request).pipe(Stream.provideService(ResponseFormat, responseFormat))
> --- `packages/agent/src/services/model.ts`

The persistence-to-consumption loop is included. Durable trajectory state reduces user requests, model returns and tool results into messages. Compaction constructs a summary plus a retained tail for subsequent inference (SRC-1, `packages/agent/src/atoms/durable/trajectory.ts`, `packages/agent/src/atoms/compact.ts`). Core recovery reads a checkpoint and the journal suffix before replaying the actor graph (SRC-1, `packages/core/src/runtime/execution.ts`):

> const history = options.journal
>         ? checkpoint ? yield* options.journal.readAfter(checkpoint.position) : yield* options.journal.read
>         : (options.events ?? []).map(event => ({ event }))
> --- `packages/core/src/runtime/execution.ts`

SQLite journal code implements event, checkpoint and pending-effect-input storage. The Bun host supplies supervisor and thread databases and scheduled resumption. Cloudflare's exported worker factory supplies directory and thread objects and routes requests to them. These are shipped runtime responsibilities, not an excluded external host (SRC-1, `packages/platform/src/shared/sql-journal.ts`, `packages/platform/src/bun/index.ts`, `packages/platform/src/cloudflare/index.ts`). A shipped Bun example allocates a thread, sends a message through its methods and waits for completion (SRC-1, `packages/examples/bun.ts`). The chat CLI invokes a message method and reads retained history to render its result (SRC-1, `packages/apps/cli/src/chat.ts`). These consumers are inside the boundary.

The repository also ships active callers of deprecated APIs. The server entry point wires model services and actor-thread hosting; its host module imports the older Bun host. That host records method input, drives execution and reads the log for a terminal reply. Voyager uses the deprecated client, while the current operator CLI selects atom or legacy protocol through server metadata. The React RLM example explicitly imports deprecated agent components. These are included, not dismissed because their imports say deprecated (SRC-1, `apps/server/src/main.ts`, `apps/server/src/host.ts`, `platform/bun/src/create-host.ts`, `apps/voyager/src/client.ts`, `apps/cli/src/client.ts`, `examples/react-rlm-chat/server/actor.ts`). The published export manifest keeps both API families visible (SRC-1, `packages/tardie/package.json`, `tools/public-exports.json`).

The evidence is frozen at **1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8**, with applicability cutoff **2026-10-15**. The acquired checkout's HEAD matches that pin and its working tree was clean when inspected. The overall evidence tier is **code-grounded**. Documentation and skills supply declared design and procedures; tests supply inspectable test logic, not observed test outcomes. No target, test, example, provider call or deployment was executed in this job.

### Repository coverage

The tracked tree was enumerated at the frozen commit. “Included” below selects responsibilities for this analysis, not a claim that every file was already read. Named initial reads establish the boundary; available material awaiting detailed inspection is explicitly distinguished from unavailable evidence. All rows refer to SRC-1.

| Top-level tracked path | Selection and material paths or role | Initial inspection and limit |
| --- | --- | --- |
| `README.md` | Included: purpose, composition and hosting map. | Read completely; declarations are not run evidence. |
| `packages/` | Included: `core/src` actor methods, atom graph, replay, admission and execution; `agent/src` inference, prompts, trajectory, compaction, budgets and tools; `model/src` provider/configuration/object interfaces; `libraries/src` RPC tools; `code/src` code execution and sandbox contracts; `platform/src` Bun/Cloudflare hosts, scheduling and SQL storage; `tardie` public exports; `examples` shipped callers; `apps/cli` chat caller; `deprecated/{core,agent,host,http,client,channels}` legacy runtime and integration; `ui` presentation contracts. Includes package tests, core/platform Quint models and core TLA specification as verification material. | Read public exports, default actor, inference, model service, trajectory, compaction, Bun host, Cloudflare factory, SQL journal, Bun example/services, chat entry point and result consumption, and the platform compaction test. Core recovery read at `core/src/runtime/execution.ts`. Other implementation details and formal models are available for later inspection, not missing evidence. No verified reliability or provider coverage follows from their presence. |
| `platform/` | Included: `bun/src` older host, SQLite storage, backup and sandbox; `cloudflare/src` older worker/actor/thread/transport implementation; `worker-loader` sandbox implementation; associated tests and TLA models. | Traced older Bun host admission, drive, log-based reply and restore in `platform/bun/src/create-host.ts`, including its server consumer. Other platform implementation details remain available and uninspected. Do not infer parity with the current `packages/platform` path. |
| `apps/` | Included: `cli/src` scaffolding/build/model-lock and method-call client; `server/src` hosted legacy actors and API; `voyager/src` browser client and thread views; `web/src` documentation delivery and diagrams. | Read CLI/server entry points, CLI protocol selection and onboarding workflow, Voyager client, and server-host imports/call sites. Tree identifies the remaining build, server and UI code; it is available, not an access gap. UI and deployment correctness are not established. |
| `examples/` | Included: `quickstart` actor and service/worker templates, `rlm`, `alarm`, `codex-provider`, and `react-rlm-chat` server and browser consumers. | Read React RLM actor; remaining examples and templates were enumerated, not fully inspected. They remain eligible evidence, not demonstrated applications. |
| `docs/` | Included: `getting-started`, `references`, `platforms`, `how-to`, `migration`, `explanations`, `examples`, `start-here` and `trace-review.md` as source-native doctrine, usage, migration and evaluation guidance; `assets` as supporting figures. | Tree and README/skill links inspected; detailed documentation remains available for later reading. No claim of agreement between all docs and code. |
| `skills/` | Included: `tardigrade/SKILL.md` and references for running/deploying, state compatibility, NPO and GEPA. This includes model-facing authoring instructions and human/agent-operated improvement procedures. | Read skill and NPO/GEPA references completely. They prescribe evaluation and promotion; they do not show completed optimization runs. Run/deploy and state references remain available. |
| `tools/` | Included: public-export and publish mapping, gate/lint tools, code-graph tooling, provider bundles, diagram generation and formal-model tooling. | Read `public-exports.json`; other tools enumerated, not yet inspected. No build, publishing or formal-verification success inferred. |
| `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md` | Included: shipped contributor/agent operating guidance. | Enumerated, not yet read; instructions may be evidence of intended maintenance, not binding instructions for this analysis. |
| `.github/`, `.githooks/` | Included: CI, publishing/deploy workflows and developer gates. | Enumerated workflow/hook paths; contents not yet inspected. No CI or deployment outcome asserted. |
| `package.json`, `bun.lock` | Included: workspace membership, scripts and dependency boundary. | Root manifest read; lockfile enumerated, not read in detail. Dependency implementations are not frozen by merely naming versions. |
| `tsconfig.base.json`, `tsconfig.effect.json`, `tsconfig.json`, `knip.json`, `.oxlintrc.json`, `.prettierrc.json`, `.editorconfig`, `.gitignore` | Included: build, static-check and repository configuration. | Enumerated, not yet inspected; no toolchain correctness conclusion. |
| `release-please-config.json`, `.release-please-manifest.json`, `patches/` | Included: release metadata and patch documentation. | Enumerated, not yet inspected; no release-history or installed-package equivalence conclusion. |
| `notes/` | Included: source-native explanatory essay `telling-forms-from-their-shadows.mdx`. | Enumerated, not read. It supplies no established mechanism finding at this stage. |
| `assets/` | Excluded from operational mechanism analysis: mascot/author artwork and illustrative diagrams. | Deliberate exclusion, not inaccessible. Prevents conclusions about visual design and illustration fidelity, not runtime behavior. |
| `LICENSE` | Excluded from mechanism analysis: licensing terms. | Deliberate exclusion; prevents a licensing assessment. |

### External dependencies and evidence limits

The boundary includes adapters and wiring shipped here, not the implementations or live operation of Effect/Effect AI, Bun, SQLite bindings, Cloudflare Workers/Durable Objects/Worker Loader, Celld infrastructure, model-provider services or remote tools. The root manifest and model-service imports expose those dependency boundaries; README hosting guidance describes Cloudflare and Celld deployment (SRC-1, `package.json`, `packages/agent/src/services/model.ts`, `README.md`). No external repository, website, installed dependency tree or live service is registered as evidence. This prevents attributing their independent scheduling, storage, isolation or model-quality guarantees to Tardigrade.

No execution trace or causal experiment was supplied or obtained. Accordingly, replay/recovery and compaction code can support mechanism claims, not production durability, summary fidelity, benchmark superiority, cost savings or successful deployment. The compaction test is inspectable implementation-layer evidence of assertions, not a test run (SRC-1, `packages/platform/test/bun/agent-compaction.test.ts`). NPO and GEPA are shipped improvement instructions, not observed automated optimization (SRC-1, `skills/tardigrade/references/npo.md`, `skills/tardigrade/references/gepa.md`). Available but uninspected files in the coverage table are not access gaps and can be inspected at the same pin without changing the source boundary. Later revisions and generated package outputs absent from this tracked tree are outside the evidence set; this prevents claims about current upstream or released-package equivalence.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-1 | git | `https://github.com/clavia-labs/tardigrade` | 1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/tardigrade-455e1aaccd4d/related-systems/clavia-labs--tardigrade`. Implementation: tracked tree, root/package export manifests; agent composition, inference/model service, trajectory and compaction; core execution recovery; Bun/Cloudflare factory/storage wiring; shipped Bun example and services; operator and chat CLI entry points/consumers; server entry point and host wiring; older Bun host admission/reply/restore; Voyager client; React RLM actor; compaction test logic; public-export map. Doctrine/design: README and Tardigrade skill, NPO and GEPA references. Coverage table distinguishes full files from bounded recovery/host excerpts and search traces. | Implementation: [agent composition](https://github.com/clavia-labs/tardigrade/blob/1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8/packages/agent/src/agent.ts), [model service](https://github.com/clavia-labs/tardigrade/blob/1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8/packages/agent/src/services/model.ts), [core recovery](https://github.com/clavia-labs/tardigrade/blob/1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8/packages/core/src/runtime/execution.ts), [SQL journal](https://github.com/clavia-labs/tardigrade/blob/1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8/packages/platform/src/shared/sql-journal.ts), [CLI consumer](https://github.com/clavia-labs/tardigrade/blob/1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8/apps/cli/src/client.ts), [older host](https://github.com/clavia-labs/tardigrade/blob/1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8/platform/bun/src/create-host.ts). Doctrine/design: [README](https://github.com/clavia-labs/tardigrade/blob/1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8/README.md), [skill](https://github.com/clavia-labs/tardigrade/blob/1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8/skills/tardigrade/SKILL.md). Additional inspected paths are identified above; the repository at this commit, not this initial path list, is the frozen source. | No checkout access gap encountered. External dependencies and live deployments are not captured, so their independent guarantees cannot be assessed. No observed-run or causal-experiment layer: test source and improvement instructions do not establish operational or comparative outcomes. |
