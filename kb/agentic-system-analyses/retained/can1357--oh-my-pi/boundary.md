---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "oh-my-pi's shipped agent runtime at commit 2431e8a8716a4da73ae327a412f6d54c22f681e5, with the primary runtime traced and other shipped loops awaiting inspection"
run-id: AAS-2026-10-14-oh-my-pi-c0ffc54ff768-01
result-disposition: complete
target-class: enclosing runtime
boundary-kind: complete artifact, partial loop
reviewed-boundary: "2431e8a8716a4da73ae327a412f6d54c22f681e5"
analysis-cutoff: "2026-10-14"
evidence-tier: code-grounded
source:
  identity: https://github.com/can1357/oh-my-pi
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/oh-my-pi-c0ffc54ff768/related-systems/can1357--oh-my-pi
  revision: 2431e8a8716a4da73ae327a412f6d54c22f681e5
  sha256: null
---

# oh-my-pi boundary

## Boundary and evidence

This run analyses oh-my-pi's shipped coding-agent runtime and its state, context and memory mechanisms. Its intended use is to establish how the system operates from pinned implementation and declared contracts, not to assess deployment quality or recommend Commonplace adoption. The target is in scope as an **enclosing runtime**: its own CLI constructs sessions and an agent that dispatches model requests. It is not merely a client library embedded in an excluded application.

The package declares its executable directly (SRC-1, `packages/coding-agent/package.json`):

> "bin": {
> "omp": "src/cli.ts"
> },
> --- `packages/coding-agent/package.json`

The inspected entry path runs from CLI command routing through the root launch command to `runRootCommand`, then `createAgentSession`, `AgentSession` and the core `Agent`. The SDK supplies the agent's model, tools, context transforms and streaming function. These are shipped callers, not external hosts (SRC-1, `packages/coding-agent/src/cli.ts`, `packages/coding-agent/src/commands/launch.ts`, `packages/coding-agent/src/main.ts`, `packages/coding-agent/src/sdk.ts`). The core loop admits prompts to its context before running the model/tool loop (SRC-1, `packages/agent/src/agent-loop.ts`):

> messages: [...context.messages, ...prompts],
> --- `packages/agent/src/agent-loop.ts`

> await runLoop(currentContext, newMessages, config, signal, stream, streamFn, prompts);
> --- `packages/agent/src/agent-loop.ts`

State production and later consumption belong to the target. Initial inspection found session message append, resumed-context reconstruction, CLI resume/fork selection and memory-backend selection. Backend contracts include startup subscriptions, prompt instructions, explicit retention and recall preparation; their implementations remain to be traced, so these contracts do not establish successful memory operation (SRC-1, `packages/coding-agent/src/session/session-manager.ts`, `packages/coding-agent/src/sdk.ts`, `packages/coding-agent/src/main.ts`, `packages/coding-agent/src/memory-backend/resolve.ts`, `packages/coding-agent/src/memory-backend/types.ts`).

> deobfuscateSessionContext(sessionManager.buildSessionContext(), obfuscator),
> --- `packages/coding-agent/src/sdk.ts:1940-1979`

> if (id === "hindsight") return (await import("../hindsight/backend")).hindsightBackend;
> if (id === "mnemopi") return (await import("../mnemopi/backend")).mnemopiBackend;
> if (id === "sharpshooter") return (await import("../sharpshooter/backend")).sharpshooterBackend;
> if (id === "local") return localBackend;
> return offBackend;
> --- `packages/coding-agent/src/memory-backend/resolve.ts`

The frozen artifact is the entire registered repository at **2431e8a8716a4da73ae327a412f6d54c22f681e5**. HEAD matches the acquisition pin and the checkout reports no tracked or untracked changes. The applicability cutoff is **2026-10-14**, the supplied run date, not a claim that the implementation remained unchanged through that date. The overall tier is **code-grounded**. No target execution, test run, provider request or experiment was performed.

The boundary kind is **complete artifact, partial loop**, not whole-system. The repository tree and primary entry/caller chain were inspected, but initial inspection has not covered every material shipped state producer and consumer. The following inventory separates included-but-not-yet-inspected material from deliberate exclusions. All included paths at the registered commit remain eligible for subsequent inspection; this is not a path allowlist.

| Shipped area | Treatment and initial coverage | Limit on conclusions |
|---|---|---|
| `packages/coding-agent/src/cli.ts`, `packages/coding-agent/src/commands/launch.ts`, `packages/coding-agent/src/main.ts`, `packages/coding-agent/src/sdk.ts` | Included; executable declaration, launch bridge and selected construction/resume/mode-dispatch sites inspected. | Does not establish every command or host-mode lifecycle. |
| `packages/agent/src/agent.ts`, `packages/agent/src/agent-loop.ts`; `packages/ai/`, `packages/catalog/` | Included; agent-loop wiring searched and prompt admission inspected; provider/auth/catalog implementations not yet inspected. | No provider-specific reliability or complete dispatch-policy conclusion. |
| `packages/coding-agent/src/session/`, `packages/coding-agent/src/memory-backend/`, `packages/coding-agent/src/memories/`, `packages/coding-agent/src/sharpshooter/`, `packages/coding-agent/src/hindsight/`, `packages/coding-agent/src/mnemopi/`, `packages/mnemopi/` | Included; selected session reconstruction, append, backend resolution and lifecycle contract inspected; storage and backend internals not yet traced. | No complete retention-to-recall, consolidation or durability account yet. |
| `packages/coding-agent/src/prompts/`, `packages/coding-agent/src/discovery/`, `packages/coding-agent/src/extensibility/`, `packages/coding-agent/src/autolearn/`, `packages/agent/src/compaction/`, `packages/snapcompact/`; `.omp/commands`, `.omp/skills`, `.omp/tools` | Included; tree inventory identifies shipped prompts, maintenance, discovery and context mechanisms; bodies not yet inspected. | No complete instruction-admission, maintenance or context-transformation account. |
| `packages/coding-agent/src/task/`, `packages/coding-agent/src/eval/`, `packages/coding-agent/src/tools/`, `packages/coding-agent/src/modes/`; `packages/tui/`, `packages/collab-web/`, `packages/browser-relay/`, `packages/stats/`, `packages/wire/`, `packages/utils/`, `packages/natives/`, `packages/omptype/`, `crates/` | Included; repository inventory and dependency declarations inspected, with selected mode dispatch sites searched; implementations largely not yet inspected. | Cannot assert closure of delegation, tool, collaboration, telemetry or native-support loops. |
| `python/robomp/`, `sdk/go/`, `sdk/python/`, `sdk/rust/` | Included shipped drivers and clients; top-level tree and root script declarations inspected, not their implementations. | No orchestration, RPC-client persistence or cross-language host account. These callers are not reclassified as external merely for using APIs. |
| `packages/metaharness/`, `packages/typescript-edit-benchmark/`, package tests/benchmarks, `scripts/`, `docs/`, `README.md` | Included as evaluation, tooling or declared-design evidence; inventory and selected root manifest/README passages inspected. | Test presence and performance claims do not establish observed results; evaluator conditions remain uninspected. |
| Build/distribution/configuration material in root files, `.cargo/`, `.config/`, `.github/`, `assets/`, `bazel/`, `infra/`, `nix/`, `patches/`, `types/` | Included where it changes shipped runtime behavior; otherwise development context. Mostly not yet inspected. | No installation, release-reproducibility or platform-parity assessment. |
| External provider services, model weights, installed third-party extensions/MCP servers, user projects and deployed Hindsight service | Excluded implementations; target-side integration code remains included. | Their internal behavior, actual user configuration and deployed outcomes cannot be attributed to oh-my-pi. |

There is no known inaccessible file in the frozen checkout. Uninspected available files are coverage limits, not access gaps. No execution trace or controlled intervention was supplied; therefore the source can establish executable structure and attributed intent, not observed success, comparative efficacy or causality. Later revisions, linked external pages and other repositories are outside this evidence pin.

## Source register

| source ID | kind | identity/location | revision or capture | evidence layer | inspected scope | citation anchors | access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/can1357/oh-my-pi` | 2431e8a8716a4da73ae327a412f6d54c22f681e5 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/oh-my-pi-c0ffc54ff768/related-systems/can1357--oh-my-pi`. Implementation: tracked tree; root/package manifests; selected CLI routing, launch, main session/mode dispatch, SDK construction/reload, session append, core-loop admission, memory resolution and lifecycle contract. Doctrine/design: opening README/install/product passages and comments in those inspected paths. Initial inventory and uninspected material are distinguished above. | Implementation: [CLI routing](https://github.com/can1357/oh-my-pi/blob/2431e8a8716a4da73ae327a412f6d54c22f681e5/packages/coding-agent/src/cli.ts), [SDK](https://github.com/can1357/oh-my-pi/blob/2431e8a8716a4da73ae327a412f6d54c22f681e5/packages/coding-agent/src/sdk.ts), [core loop](https://github.com/can1357/oh-my-pi/blob/2431e8a8716a4da73ae327a412f6d54c22f681e5/packages/agent/src/agent-loop.ts), [backend selection](https://github.com/can1357/oh-my-pi/blob/2431e8a8716a4da73ae327a412f6d54c22f681e5/packages/coding-agent/src/memory-backend/resolve.ts). Doctrine/design: [README](https://github.com/can1357/oh-my-pi/blob/2431e8a8716a4da73ae327a412f6d54c22f681e5/README.md), `packages/coding-agent/src/memory-backend/types.ts`. | No known checkout access gap. No supplied observed-run or causal-experiment evidence; no operational-success or efficacy conclusion. Uninspected shipped paths prevent a whole-system coverage claim. |
