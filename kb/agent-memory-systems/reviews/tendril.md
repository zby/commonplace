---
description: "Tendril review: self-extending desktop agent with filesystem capability registry, model-authored TypeScript tools, and Deno sandbox execution"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-05"
---

# Tendril

Tendril, from `serverless-dna/tendril`, is a Tauri desktop agent and TypeScript sidecar built around the Agent Capability pattern: the model keeps a persistent workspace registry of generated tools, lists that registry before acting, registers a new TypeScript tool when no suitable capability exists, and executes registered code in a Deno sandbox. The reviewed code supports a Tauri/React UI, JSON-RPC/NDJSON agent transport, multi-provider Strands models, filesystem capability browsing, and workspace-scoped execution.

**Repository:** https://github.com/serverless-dna/tendril

**Reviewed commit:** [e671a4143d28de68289efd81580002041bb4cb6a](https://github.com/serverless-dna/tendril/commit/e671a4143d28de68289efd81580002041bb4cb6a)

**Last checked:** 2026-06-05

## Core Ideas

**Capabilities are durable generated tools, not retrieved notes.** The project README frames Tendril as a "self-extending agentic sandbox" where the model builds and reuses tools across sessions; the persistent unit is a capability definition in `tools/index.json` plus a `tools/{name}.ts` implementation in the selected workspace ([README.md](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/README.md), [docs/agent-capability-spec.md](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/docs/agent-capability-spec.md)).

**The implemented bootstrap surface is three model-visible tools.** Current `agent.ts` wires `listCapabilities`, `registerCapability`, and `executeCode`; `execute` internally loads the registered source by name, so the model cannot pass inline code to the execution tool ([tendril-agent/src/agent.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/agent.ts), [tendril-agent/src/loop/tools.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/tools.ts)). Some README text still mentions `loadTool` and "four bootstrap tools"; the code path I inspected exposes no separate `loadTool` tool to the model.

**Context efficiency is fixed-surface, full-registry selection.** Tendril avoids a growing model-visible tool list by always showing the same bootstrap tools, but `listCapabilities` returns every capability summary - name, description, triggers, and suppression - for the model to read ([tendril-agent/src/loop/registry.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/registry.ts)). This keeps implementation source out of the prompt until execution, but it does not implement lexical, embedding, or ranked retrieval; the Agent Capability spec explicitly argues that at personal scale the full index fits in context ([docs/agent-capability-spec.md](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/docs/agent-capability-spec.md)).

**Generated code is auditable and sandboxed, but still behaviorally strong.** Capabilities are inspectable plain files in the workspace, and the UI can read both the registry and tool source without going through the agent ([tendril-ui/src-tauri/src/capabilities.rs](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/capabilities.rs), [tendril-ui/src/components/CapabilityBrowser.tsx](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src/components/CapabilityBrowser.tsx)). Execution is confined by Deno flags to workspace read/write, optional domain-restricted network access, `--no-prompt`, timeout, output cap, and temporary-file cleanup ([tendril-agent/src/loop/sandbox.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/sandbox.ts)).

**The desktop host makes the registry a human-facing workspace.** The Rust backend initializes a chosen workspace, creates `tools/index.json`, stores app config under `~/.tendril/config.json`, spawns the agent sidecar, forwards ACP events to React, and lets users browse capabilities, files, settings, and debug traffic ([tendril-ui/src-tauri/src/workspace.rs](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/workspace.rs), [tendril-ui/src-tauri/src/acp.rs](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/acp.rs), [tendril-ui/README.md](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/README.md)).

## Artifact analysis

- **Storage substrate:** `files` `repo` - The runtime memory is filesystem state in the user workspace: `tools/index.json`, `tools/*.ts`, and `system-prompt.txt`. App configuration is another file under `~/.tendril/config.json`; the repository stores the authored prompt, tool schemas, protocol handlers, UI, specs, and tests that define how those workspace files act ([tendril-agent/src/loop/registry.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/registry.ts), [tendril-agent/src/loop/prompt.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/prompt.ts), [tendril-agent/src/config.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/config.ts)).
- **Representational form:** `prose` `symbolic` - Capability descriptions, triggers, suppression rules, the system prompt, UI labels, and specs are prose interpreted by the model or human; JSON registry fields, Zod schemas, TypeScript implementations, Rust/Tauri commands, JSON-RPC messages, Deno permission flags, and tests are symbolic. I found no retained embeddings, vector index, adapter, or model-weight update.
- **Lineage:** `authored` - The standing framework is authored source/spec code; runtime capabilities are authored by the model through `registerCapability` and may also be inspected or edited by humans as plain files. They are derived from the current task/request, but I did not find a mechanism that mines durable capabilities from stored transcripts, trajectories, or tool traces.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `enforcement` - Capability summaries are knowledge/context for the model's tool choice; the system prompt and trigger/suppression prose instruct behavior; registry entries route execution by name; name validation, config schemas, protocol handling, and workspace checks validate inputs; Deno permission flags, timeouts, output caps, and the "execute by registered name" API enforce execution boundaries.

**Capability registry.** `CapabilityRegistry` treats missing or corrupt `tools/index.json` as an empty registry, returns only selection fields for listing, enriches registered definitions with `tool_path`, `created`, `created_by: "model"`, and `version`, and writes implementation source to `tools/{name}.ts` ([tendril-agent/src/loop/registry.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/registry.ts)). That registry is the main retained behavior-shaping artifact: future turns can execute a capability because prior turns wrote it.

**System prompt and bootstrap tools.** The prompt is a high-authority prose artifact: it tells the agent to list capabilities before every action, register missing tools, never answer from memory when a tool can get live data, and retry by fixing code after failures ([tendril-agent/src/loop/prompt.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/prompt.ts)). The tool schemas and callbacks assign the symbolic consequences of listing, registering, and executing ([tendril-agent/src/loop/tools.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/tools.ts)).

**Sandbox and configuration.** The Deno runner is a system-definition artifact path, not memory content: it decides what generated code may read, write, fetch, output, and how long it may run ([tendril-agent/src/loop/sandbox.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/sandbox.ts)). Config also shapes behavior through provider selection, model ids, sandbox paths, timeout, allowed domains, and max-turn settings ([tendril-agent/src/config.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/config.ts), [tendril-ui/src-tauri/src/config.rs](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/config.rs)).

**Promotion path.** Tendril's promotion path is task need -> model-authored TypeScript capability -> registry entry -> future executable tool. This crosses from prose task intent into symbolic code and routing metadata. It does not promote generated tools into reviewed packages, tests, or validators beyond the registry/write constraints visible in this checkout.

## Comparison with Our System

Tendril and Commonplace both favor inspectable retained artifacts over opaque service memory, but they use them for different authority paths. Commonplace stores typed Markdown, source snapshots, generated indexes, and review records so agents can reason with reviewed knowledge. Tendril stores generated executable capabilities so a future agent can perform actions without rebuilding the tool.

The biggest alignment is filesystem adoption. Tendril's registry is easy to inspect, edit, delete, and version if the workspace is put under git. That matches Commonplace's bias toward files as agent-operable state. The divergence is governance: Commonplace validates frontmatter, headings, links, citations, and review warnings before artifacts gain standing; Tendril validates names, schemas, paths, sandbox permissions, and protocol shape, but it does not review whether a generated capability is correct, safe for its intended use, or still the best tool.

Tendril's "few bootstrap tools, many retained capabilities" solves a real prompt-surface problem. Commonplace solves context pressure mostly through collection contracts, indexes, lexical search, and explicit loading. Tendril keeps the live tool surface small, but then pays with full-registry listing and model judgment over trigger prose. At tens of capabilities that is pragmatic; at hundreds, it becomes a routing and context-dilution question.

### Borrowable Ideas

**Executable skill registry with human-readable policy.** Commonplace could borrow the split between a compact capability definition and a source file for workshop-only automation. Ready only for low-authority helper tools, not for library notes or validators without a review gate.

**Registered-name execution boundary.** Tendril's `execute` taking a capability name rather than arbitrary code is a clean authority boundary. Commonplace could use the same shape for generated maintenance helpers: the agent can invoke reviewed named scripts, but cannot smuggle inline code through an execution API.

**Capability browser as memory inspection UI.** The UI's side-by-side registry/source browsing is a useful pattern for agent-created artifacts. Commonplace already has files and indexes; a focused "generated operational artifacts" view would need a concrete workflow before it is worth building.

**Trigger and suppression prose beside generated code.** The trigger/suppression fields are a compact way to record when a tool should and should not apply. Commonplace could reuse that for skills or review gates, but should pair it with deterministic checks where the consequence is high authority.

**Do not borrow unreviewed self-extension as library policy.** Tendril's automatic capability creation is useful for a sandbox. Commonplace should require citations, validation, and review before a generated artifact can shape durable KB methodology or enforced operations.

## Write side

**Write agency:** `manual` `automatic` - Humans choose the workspace, configure providers/sandbox settings, and can edit or delete registry files directly; the agent automatically writes `system-prompt.txt` on startup and model-authors/upserts capability definitions plus TypeScript implementations through `registerCapability`.

**Curation operations:** `none` - The implemented automatic write path mainly acquires new executable capabilities from current tasks and can overwrite a same-name capability. I did not find code that automatically deduplicates, consolidates, synthesizes, invalidates, decays, or promotes already-stored capabilities under a durable curation policy. The prompt's "fix and retry" instruction may lead the model to rewrite a tool after failure, but the system does not retain a trace-grounded repair loop or review state that would make this a classified curation operation.

## Read-back

**Read-back:** `pull` - Retained capabilities re-enter the acting agent's context only when the model follows the prompt and calls `listCapabilities`; tool source is loaded by `execute` after the agent names a capability, and the UI reads registry/source files through explicit user actions.

Tendril is an edge case: the static system prompt strongly instructs the agent to pull memory before every action, but static shipped prompt text is not accumulated memory read-back. The accumulated memory is the capability registry, and the inspected code does not inject it unsolicited into every model call. The registry is full-list pull: all summaries are returned, metadata is omitted, and source stays out of context until execution or UI inspection.

Selection is controlled by the model reading capability names, descriptions, triggers, and suppression rules. The code does not implement a keyword search despite some README wording, does not rank by embeddings or learned relevance, and does not enforce the configured `registry.maxCapabilities` in `CapabilityRegistry.register` at this commit ([tendril-agent/src/config.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/config.ts), [tendril-agent/src/loop/registry.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/registry.ts)). Effective precision, recall, and context dilution are therefore not verified from code.

Authority at consumption is strong once execution is chosen: the selected capability runs as code in the workspace-scoped sandbox. Faithfulness is not tested as memory read-back; I found tests for registry CRUD, sandbox behavior, protocol handling, config, costs, and integration plumbing, but not an ablation showing that remembered capabilities improve future task behavior correctly ([tendril-agent/tests/registry.test.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/tests/registry.test.ts), [tendril-agent/tests/sandbox.test.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/tests/sandbox.test.ts)).

## Curiosity Pass

**The "search" name overstates the implementation.** The project examples and docs sometimes say search, but the code returns the full capability list and lets the model perform semantic matching in-context. That is simpler and inspectable, but the scaling limit is context size and model attention.

**The removed `loadTool` surface is a meaningful safety improvement.** Older explanatory text treats load as a bootstrap operation; current code makes source loading an internal step of `execute`. That reduces the chance that tool source becomes incidental prompt clutter before the agent has selected a capability.

**`created_by: "model"` is always assigned by the registry.** The type allows `"human"`, and the spec says humans can author capabilities, but the implemented register path writes `"model"` for every API-created capability. Human-authored tools are possible by direct file editing, not through a separate code path.

**Registry corruption handling favors continuity over recovery.** Corrupt JSON becomes an empty registry, so the next registration can write a new index. That avoids crashes but can temporarily hide existing tools until a human repairs the file.

**Sandbox permissions are scoped but broad by default for network.** `allowedDomains: []` becomes unrestricted `--allow-net`, matching the README. The model can build networked tools unless the user configures a domain allowlist.

## What to Watch

- Whether Tendril adds real registry search, ranking, or a capability cap; that would change context efficiency from full-list pull to selected read-back.
- Whether generated capabilities gain tests, provenance, review state, or version increments; that would raise their authority from ad hoc generated tools toward governed system-definition artifacts.
- Whether the system implements automatic repair history after failed executions; that could become an `evolve` operation if repairs are retained with lineage and quality signals.
- Whether workspace registries move under first-class git/versioning support; that would make rollback and audit closer to Commonplace's repo-native model.
- Whether the stale `loadTool`/bootstrap-count documentation is cleaned up; it currently obscures the actual authority boundary around `execute`.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Tendril stores reusable capabilities, but they reach the agent through mandatory pull rather than unsolicited memory injection.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Tendril's prompt, registry metadata, generated code, config, and sandbox permissions differ by substrate, form, lineage, and authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: generated tools, the system prompt, registry schema, and sandbox rules configure and constrain future behavior.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - relates: Tendril routes execution by declared capability names and trigger prose after the agent pulls the registry.
