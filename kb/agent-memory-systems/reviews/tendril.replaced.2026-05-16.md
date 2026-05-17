---
description: "Tauri/Strands sandbox that turns live user requests into persistent Deno TypeScript capabilities in a workspace-local registry"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-04-27"
---

# Tendril

> Replaced 2026-05-16. See [Tendril](./tendril.md) for the current review.

Tendril is a desktop agent sandbox by serverless-dna that demonstrates an "Agent Capability" pattern: instead of exposing a large fixed tool set, the running agent sees a tiny bootstrap surface and writes persistent TypeScript tools when the current workspace lacks a matching capability. The README framing is broadly accurate, but the current implementation has converged on three hardcoded tools (`listCapabilities`, `registerCapability`, and `execute`) rather than the older four-tool `searchCapabilities`/`loadTool` design still present in some docs.

**Repository:** https://github.com/serverless-dna/tendril

**Reviewed commit:** e671a4143d28de68289efd81580002041bb4cb6a

**Commit URL:** https://github.com/serverless-dna/tendril/commit/e671a4143d28de68289efd81580002041bb4cb6a

## Core Ideas

**The memory unit is an executable capability, not a fact record.** A workspace stores capabilities under `tools/`: `index.json` carries name, one-sentence capability, triggers, suppression rules, creation metadata, and version, while `tools/{name}.ts` carries the executable implementation. `CapabilityRegistry.register()` validates snake-case names, upserts the definition, writes the index, and writes the TypeScript source; `load()` later reads code by capability name. This is memory as accumulated affordance: the next session changes because a named operation exists, not because a retrieved note describes what happened ([tendril-agent/src/loop/registry.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/registry.ts), [tendril-agent/src/types.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/types.ts)).

**The bootstrap surface deliberately compresses tool choice into one list-read-execute loop.** `createAgent()` instantiates a Strands agent with only `listCapabilities`, `registerCapability`, and `execute`. The system prompt requires every action to list the registry first, execute a matching capability by name, or register a new one before execution. There is no separate keyword search implementation in the current code; `listCapabilities()` returns all capability summaries and leaves semantic matching to the model ([tendril-agent/src/agent.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/agent.ts), [tendril-agent/src/loop/tools.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/tools.ts), [tendril-agent/src/loop/prompt.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/prompt.ts)).

**Execution is name-gated and Deno-sandboxed.** The `execute` tool accepts a registered capability name plus JSON arguments, loads `tools/{name}.ts`, injects `args` and `__workspace`, writes a temporary script, and runs Deno with workspace-scoped read/write permissions, configured network permissions, `--no-prompt`, a timeout, output-size cap, and best-effort temp cleanup. The API boundary matters: the model cannot pass arbitrary inline code to `execute`; it must first persist a capability through the registry ([tendril-agent/src/loop/tools.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/tools.ts), [tendril-agent/src/loop/sandbox.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/sandbox.ts)).

**The desktop shell is a protocol host, not the learning mechanism.** The Rust/Tauri side spawns the Node sidecar, sends JSON-RPC `initialize`, `new_session`, prompt, and cancel messages over stdin, and forwards agent stdout into Tauri events. The agent process translates Strands stream events into ACP-style session updates for thoughts, tool calls, observations, usage, and completion. This makes Tendril inspectable as an app, but the durable adaptation loop still lives in the workspace registry and Deno tool files ([tendril-ui/src-tauri/src/acp.rs](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/acp.rs), [tendril-agent/src/transport/protocol.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/transport/protocol.ts), [tendril-agent/src/transport/stream.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/transport/stream.ts)).

**Capabilities are inspectable but weakly governed.** The UI reads `tools/index.json`, lists capability metadata, and can open the source for a named capability after validating the tool name. Workspace initialization creates `tools/index.json`, config writes reject obvious dangerous workspace paths, and Rust validates configured fields before saving. But there is no semantic review, test suite per generated capability, approval state, provenance field, stale/superseded state, dependency pinning policy, or automatic deletion. The `registry.maxCapabilities` setting is parsed and validated, but the registry implementation does not enforce it at registration time ([tendril-ui/src-tauri/src/capabilities.rs](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/capabilities.rs), [tendril-ui/src/components/CapabilityBrowser.tsx](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src/components/CapabilityBrowser.tsx), [tendril-ui/src-tauri/src/workspace.rs](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/workspace.rs), [tendril-agent/src/config.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/config.ts)).

## Comparison with Our System

| Lens axis | Tendril | Commonplace |
|---|---|---|
| Creation and import | Creates executable TypeScript capabilities online from the current user task | Authors typed notes, sources, reviews, ADRs, instructions, reports, and skills through explicit workflows |
| Evidence and trust | Keeps readable source code and registry metadata, but no required provenance or review state | Uses frontmatter contracts, citations, validation, semantic review, and generated indexes |
| Artifact contracts | One capability definition plus code file; triggers and suppression are advisory model guidance | Path-valued type specs and collection conventions define role-specific sections, metadata, and links |
| Consumer surfaces | Agent prompt, Strands tools, Deno sandbox, Tauri capability browser | Agent instructions, CLI commands, skills, validators, indexes, notes, and reports |
| Activation | Always list the full capability registry, then model-select by trigger/suppression text | Search/index/link-driven loading of relevant artifacts, with skills and type specs read on demand |
| Promotion/codification | Directly codifies a need into a tool, with no intermediate note or approval workflow | Can promote source/workshop material into notes, instructions, scripts, validators, and skills |
| Lifecycle | Upsert by name; manual file edits/deletion; no built-in retirement or quality gates | Status fields, review gates, link checks, relocation commands, generated indexes, and validation |

Tendril is much narrower than commonplace but hits a sharper behavior-change target. Commonplace mostly accumulates readable prose and structured markdown so future agents can reason better. Tendril accumulates symbolic artifacts that a deterministic interpreter executes. That makes each successful capability closer to codification than to ordinary memory storage.

The strongest alignment is inspectability. Both systems choose durable files over hidden service state and make generated artifacts available for later inspection. The divergence is authority. Commonplace treats artifact type and workflow as a promise that some review, source reading, or validation happened. Tendril treats successful registration as enough to join the operational tool surface.

The second divergence is activation cost. Commonplace spends effort on descriptions, indexes, and links because a large KB cannot be fully loaded every turn. Tendril currently assumes a personal-scale registry where the full capability summary list fits in context. That is a reasonable starting point, but the design has an obvious scaling cliff: triggers and suppression rules become a prompt-time retrieval corpus without ranking, ownership, or decay.

## Borrowable Ideas

**Name-gated execution for generated tools.** Ready now as a design pattern. The model can write code, but `execute` only accepts a registered name. That single API choice forces generated code through a durable, inspectable registry before it runs. Commonplace skills that generate helper scripts should prefer this shape over hidden one-off execution.

**Trigger/suppression metadata on callable artifacts.** Ready for skills and future generated commands. Tendril's trigger and suppression fields are concise, agent-readable activation policy. Commonplace already uses skill descriptions as routing triggers; explicit suppression conditions would improve "do not use this when..." cases.

**Capability browser as a governance surface.** Needs a use case, but the direction is right. A UI that shows generated tool code, trigger policy, and metadata gives operators a review affordance. Commonplace's nearest equivalent is indexes plus source files; a focused browser for generated skills/scripts could make drift and duplication easier to see.

**Workspace-scoped Deno execution.** Worth studying if commonplace ever allows model-authored helper tools during workflows. Deno's read/write/network flags, timeout, no-prompt mode, and temp-script cleanup form a small concrete sandbox story. It is not a complete governance story, but it is a practical execution substrate.

**Full-registry listing as the minimal baseline.** Useful as a lower bound. Before building vector search or ranked retrieval for small callable registries, Tendril shows that returning compact summaries and letting the model decide may be enough. Commonplace should only add heavier retrieval when the registry crosses the context or ambiguity threshold.

## Trace-derived learning placement

**Trace source.** Tendril consumes the live conversation and tool-loop state: the user's current request, the model's registry read, the absence or presence of a matching capability, and execution errors returned by the sandbox. It does not preserve raw transcripts as training data. The trigger boundary is online and per action, enforced by the system prompt's list-first sequence.

**Extraction.** Extraction is model-mediated. The model decides that no existing capability fits, writes a capability definition and TypeScript implementation, registers it, and retries after failure when needed. There is no separate judge, benchmark oracle, human approval gate, or automatic success test beyond the task outcome and Deno execution result.

**Storage substrate, form, and lineage.** The durable learned artifact is symbolic: TypeScript source plus JSON metadata on a filesystem backend. Its lineage is live request plus registry miss or execution failure -> model-written capability -> registered workspace artifact.

**Behavioral authority.** Its authority is system-definition: a future Tendril session does not merely retrieve the artifact as a fact; it can execute the registered capability by name, so the durable write changes what the system can do.

**Scope and timing.** Scope is per workspace. Timing is online during deployment: each task can create or update a capability, and later sessions inherit it. The system does not generalize across workspaces, cluster similar tools, mine repeated trajectories, or train weights.

**Survey placement.** On the [survey's axes](../trace-derived-learning-techniques-in-related-systems.md), Tendril is an online trace-to-symbolic-tool case. It strengthens the survey's readable-artifact branch by showing a direct path from deployment interaction to executable capability, rather than to prose lessons or retrieved facts. It also exposes the weak oracle problem: candidate generation is easy, but promotion quality is only as strong as the model's live judgment and the immediate execution feedback.

## Curiosity Pass

Tendril's strongest move is replacing "too many tools" with "one stable tool-making interface." That is not just UI simplification. It makes the model's tool surface stationary while the workspace's capability set grows behind it. This is a clean answer to framework tool-list bloat, especially for personal or project-local automation.

The cost is that scheduling is now prompt law. The code cannot force the model to call `listCapabilities()` before every subtask; it can only make the three tools available and describe the rule. If the model skips the list step or over-creates duplicate tools, the runtime has no hard corrective mechanism.

The implementation is less search-oriented than the older docs imply. Current code lists all capabilities and relies on the model to read triggers and suppression. That is probably better than brittle keyword search at small scale, but it means "capability search" is really context loading. Once capability count grows, Tendril will need either ranked retrieval or stronger namespace/lifecycle conventions.

The sandbox boundary is meaningful but incomplete. Deno denies shell access and scopes filesystem access to the workspace, but generated code can still mutate any workspace file and, by default, has unrestricted network access when `allowedDomains` is empty. The README documents that empty means unrestricted network. That may be fine for a sandbox demo; it is not enough for shared or sensitive workspaces.

The registry is append/upsert-heavy. There is no distinction between experimental, approved, deprecated, or dangerous capabilities. There is also no link from a capability back to the conversation or user request that caused it to be created. That keeps the system simple, but makes later trust and cleanup harder than the creation path.

## What to Watch

- Whether Tendril adds approval states, tests, provenance, or version history for generated capabilities without losing its autonomous creation loop.
- Whether `listCapabilities()` remains full-registry loading or grows ranked search once personal registries pass the prompt-comfort threshold.
- Whether trigger/suppression metadata becomes enforceable policy, or stays advisory text read by the model.
- Whether sandbox defaults tighten, especially unrestricted network access when `allowedDomains` is empty.
- Whether the older four-tool docs are fully retired, or whether separate search/load tools return as the registry scales.

---

Relevant Notes:

- [trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) — extends: Tendril adds online trace-to-symbolic-tool learning, where the promoted artifact is executable code rather than prose memory.
- [constraining during deployment is continuous learning](../../notes/constraining-during-deployment-is-continuous-learning.md) — exemplifies: Tendril accumulates deterministic tools during deployment as durable behavior change outside model weights.
- [continual learning's open problem is behaviour, not knowledge](../../notes/continual-learning-open-problem-is-behaviour-not-knowledge.md) — grounds: Tendril's capabilities are system-definition artifacts, not merely retrieved knowledge.
- [ephemeral computation prevents accumulation](../../notes/ephemeral-computation-prevents-accumulation.md) — contrasts: Tendril persists generated code after execution, turning one-off computation into a reusable capability.
- [inspectable artifact, not supervision, defeats the blackbox problem](../../notes/inspectable-artifact-not-supervision-defeats-the-blackbox-problem.md) — supports: model-authored tools stay readable, diffable, and inspectable instead of becoming hidden runtime state.
- [tool loop](../../notes/tool-loop-index.md) — sharpens: Tendril keeps the outer framework-owned loop but lets the capability surface grow through generated symbolic artifacts.
