---
description: "Tendril review: desktop Strands agent whose model-authored Deno tools persist in a workspace capability registry"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: []
status: outdated
last-checked: "2026-06-02"
---

# Tendril

> Replaced 2026-06-05. See [Tendril](./tendril.md) for the current review.

Tendril, by serverless-dna, is a desktop agentic sandbox for the Agent Capability pattern: a Strands-powered model gets a tiny bootstrap tool surface, writes missing tools as TypeScript, stores them in a workspace registry, and reuses them in later sessions. The reviewed implementation is a Tauri shell plus a TypeScript sidecar agent speaking ACP-style JSON-RPC over stdio.

**Repository:** https://github.com/serverless-dna/tendril

**Reviewed commit:** [e671a4143d28de68289efd81580002041bb4cb6a](https://github.com/serverless-dna/tendril/commit/e671a4143d28de68289efd81580002041bb4cb6a)

**Last checked:** 2026-06-02

## Core Ideas

**The retained unit is an executable capability, not a note.** Tendril stores capabilities under the chosen workspace as `tools/index.json` plus one TypeScript file per capability. Each registry entry carries a name, one-sentence capability description, triggers, suppression conditions, creation metadata, and a version, while execution loads `tools/{name}.ts` by name ([registry.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/registry.ts), [types.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/types.ts), [Agent Capability spec](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/docs/agent-capability-spec.md)). The future behavior changed by memory is practical action: the agent can run a previously authored tool instead of re-solving or re-coding the same operation.

**The bootstrap surface is deliberately small.** The current agent wires exactly three Strands tools: `listCapabilities`, `registerCapability`, and `execute`. Older README phrasing still says "searchCapabilities" and sometimes "four bootstrap tools", but the code and current specification use a full-registry listing rather than a separate semantic search or `loadTool` tool ([agent.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/agent.ts), [tools.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/tools.ts), [README.md](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/README.md), [Agent Capability spec](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/docs/agent-capability-spec.md)). This is the system's main context-efficiency move: the model sees a stable small tool API, while the growing capability set is read as registry summaries on demand.

**Selection is model-mediated over the full registry.** `listCapabilities()` returns every capability summary, omitting metadata fields to reduce tokens, and the system prompt orders the model to list first before every action and decide whether a matching tool exists ([registry.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/registry.ts), [tools.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/tools.ts), [prompt.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/prompt.ts)). This keeps retrieval simple and inspectable, but context volume grows linearly with the number and verbosity of capability summaries; `registry.maxCapabilities` exists in config but is not enforced by the registry implementation as reviewed ([config.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/config.ts)).

**Execution is constrained by name loading and a Deno sandbox.** The model cannot pass code directly to `execute`; it passes a registered name, the callback loads stored source, injects `args` and `__workspace`, writes a temporary script, and runs Deno with workspace-scoped read/write, configurable network permission, `--no-prompt`, timeout, cancellation, output cap, and cleanup ([tools.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/tools.ts), [sandbox.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/src/loop/sandbox.ts), [sandbox.test.ts](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-agent/tests/sandbox.test.ts)). The registry is auditable plain files, but tool correctness, safety beyond Deno permissions, and whether triggers are faithfully followed remain runtime/model-quality questions.

**The host is a protocol bridge and inspection UI.** The Tauri app initializes a workspace, spawns the sidecar, forwards JSON-RPC messages, maps Strands events into UI events, exposes a capability browser, reads tool source, stores settings in `~/.tendril/config.json`, and passes secrets or Deno path through environment variables ([workspace.rs](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/workspace.rs), [acp.rs](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/acp.rs), [events.rs](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/events.rs), [capabilities.rs](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/capabilities.rs), [config.rs](https://github.com/serverless-dna/tendril/blob/e671a4143d28de68289efd81580002041bb4cb6a/tendril-ui/src-tauri/src/config.rs)). Adoption is native to a desktop workspace rather than to editor hooks, MCP, or git-native KB tooling.

## Artifact analysis

- **Storage substrate:** `files` — Workspace-local `tools/index.json`
- **Representational form:** `prose` `symbolic` — prose capability descriptions, triggers, suppressions, prompts, and comments are paired with symbolic JSON, TypeScript, Zod schemas, and sandbox arguments
- **Lineage:** `authored` — capabilities are model-authored or human-edited, while prompts, schemas, and wrappers are authored in repository code or generated from that code
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` — registry summaries advise tool choice, prompts instruct list-first behavior, sandbox wrappers enforce execution bounds, registry names route execution, and schemas/config checks validate accepted shapes

**Capability registry index.** Storage substrate: workspace-local `tools/index.json`. Representational form: symbolic JSON records with prose fields for `capability`, `triggers`, and `suppression`. Lineage: model-authored or human-edited capability definitions, enriched by the system with `tool_path`, creation date, `created_by`, and version; the registry treats missing or malformed JSON as an empty registry rather than preserving an error artifact. Behavioral authority: system-definition artifact for routing and tool selection, because the model reads the summary list before deciding which executable action to take. The invocation policy is advisory, not programmatically enforced.

**Capability source files.** Storage substrate: workspace-local `tools/{name}.ts` files. Representational form: symbolic TypeScript plus any embedded prose comments or prompts the author includes. Lineage: generated by the model during `registerCapability` or manually edited by a human; replacement by name overwrites the previous index entry and source file, with no built-in history unless the workspace is externally version-controlled. Behavioral authority: system-definition artifact with direct action authority when loaded by `execute`; a faulty capability can change future answers or workspace files.

**System prompt and bootstrap tool schemas.** Storage substrate: repository code plus a generated workspace `system-prompt.txt` copy for the settings UI. Representational form: prose instructions and symbolic Zod schemas. Lineage: authored in the repo, regenerated on sidecar startup for the selected workspace. Behavioral authority: system-definition artifact with instruction and API-shaping authority; it forces list-first behavior, constrains capability definition format, and blocks inline-code execution by tool schema rather than by trusting prose alone.

**Sandbox execution wrapper and temporary scripts.** Storage substrate: repository code, runtime temp files under the OS temp directory, and process configuration. Representational form: symbolic TypeScript/Node/Deno subprocess arguments. Lineage: assembled at invocation from stored capability source, JSON args, workspace path, sandbox config, and cancellation signal; the temp script is deleted after execution. Behavioral authority: enforcement authority over filesystem scope, network scope, timeout, output size, and no-prompt execution. Effective security still depends on Deno behavior and configured network allowance.

**Conversation and UI event stream.** Storage substrate: live process streams and frontend state, not a durable memory corpus in the reviewed code. Representational form: symbolic JSON-RPC and `session/update` events with streamed text/tool-call payloads. Lineage: emitted from Strands SDK events and host messages during a prompt. Behavioral authority: observability and interaction authority for the user interface; it does not itself distill logs into future capabilities.

The promotion path is direct but shallow. A need in the current conversation can become an executable tool in one turn, and that tool then has stronger authority than a prose note because it can be run. There is no built-in promotion from "frequently useful" to reviewed, tested, versioned, trusted, deprecated, or deleted; capability lifecycle beyond upsert is manual.

## Comparison with Our System

| Dimension | Tendril | Commonplace |
|---|---|---|
| Primary purpose | Self-extending desktop agent that creates and reuses executable tools | Agent-operated methodology KB with typed notes, reviews, instructions, ADRs, validation, and indexes |
| Main substrate | Workspace `tools/index.json` plus TypeScript capability files | Git-tracked Markdown, source snapshots, schemas, generated indexes, and Python commands |
| Memory unit | Executable capability with advisory triggers/suppression | Knowledge and system-definition artifacts with type contracts, status, citations, and links |
| Retrieval | Agent calls `listCapabilities()` and reads full summaries | Agents use `rg`, indexes, links, skills, validation, and review workflows |
| Governance | Name validation, Deno sandbox, config validation, tests; no review lifecycle for tools | Frontmatter/type validation, review gates, source-pinned citations, archive/replacement lifecycle |
| Activation | Always-loaded prompt mandates pull lookup before action | Mostly deliberate pull, with explicit instructions/skills when loaded |

Tendril and Commonplace share the assumption that durable agent behavior should be inspectable on disk. Tendril's artifacts are stronger at immediate action: a retained capability changes behavior by executing code. Commonplace's artifacts are stronger at epistemic governance: a retained claim can be cited, reviewed, linked, validated, replaced, or demoted without becoming executable.

The largest divergence is context strategy. Tendril solves tool-surface growth by keeping the model's formal API fixed at three bootstrap tools, but it still pushes the complete capability summary list into the model whenever the agent lists capabilities. Commonplace spreads context across lexical search, curated indexes, collection contracts, and type-specific loading; that is slower and more manual, but it avoids requiring every candidate memory summary to fit into one prompt.

Tendril's executable-memory pattern also shifts trust. In Commonplace, a note can be wrong and still mostly act as advice. In Tendril, a wrong retained capability can run code, fetch wrong data, or write files. The Deno wrapper handles some safety boundaries, but the code does not provide built-in capability tests, review status, source citations, deprecation, or rollback.

**Read-back:** `pull` — The retained capability registry enters action when the agent deliberately calls `listCapabilities()` and then `execute`; the always-loaded Tendril system prompt is shipped baseline instruction, not retained memory read-back. I did not find a code-grounded relevance-gated or hook-based memory-content push path that warrants `push-activation`

### Borrowable Ideas

**Fixed bootstrap API for expanding operational memory.** Ready as a design lens. Commonplace could distinguish stable operator commands from a growing library of generated procedures, so agents learn a small command surface while the retained operation set expands behind it.

**Executable artifact as a promoted form.** Useful but needs a use case. Tendril shows a clean jump from remembered advice to runnable tool. In Commonplace, the analogue would be a promotion path from repeated instructions or review fixes into a validated command, not an automatic conversion of notes into scripts.

**Model-authored trigger and suppression metadata.** Ready cautiously. Tendril's trigger/suppression fields are compact selection hints that are cheap for a model to read. Commonplace could use similar fields for skills or instructions, while keeping them advisory unless backed by a router or validator.

**Name-only execution boundary.** Ready now as a security pattern. Tendril's `execute` API accepts a registered name and args, not arbitrary code. Commonplace commands that run generated helpers should prefer named, versioned artifacts over inline code pasted into a runtime.

**Do not borrow unreviewed executable memory as authority.** Tendril's one-turn tool creation is powerful, but Commonplace should require explicit review, tests, or provenance before model-authored code becomes a trusted operational artifact.

## Write-side placement

**Write agency:** `automatic` `manual` — the review describes system-driven generation, extraction, consolidation, or update of retained artifacts rather than only manual authoring.

**Curation operations:** `evolve` `synthesize` `invalidate` `decay` `promote` — the existing review evidence identifies automatic store-changing operations matching these curation classes.

## Curiosity Pass

The surprising part is that Tendril is less a retrieval system than a tool compiler with memory. Its durable artifact is not context about the world; it is a new affordance for acting in the workspace.

The README's "search" language sounds like retrieval, but the checked-in implementation lists all summaries and lets the model do the semantic match. That is simpler and more inspectable than embedding search, and it fits the spec's personal-scale assumption, but it will eventually run into summary volume and ambiguous trigger conflicts.

The config schema includes `registry.maxCapabilities`, but the registry does not enforce it in code as reviewed. That makes the context-efficiency claim depend on user scale rather than an implemented budget.

The trace-derived question is easy to overstate. Tendril creates durable tools from live model work, and failures can lead the prompt to tell the model to fix and retry, but the reviewed code does not retain transcripts, mine action traces, or run an extraction loop over session history. It is self-extending, not trace-derived learning under the current review rules.

The strongest governance surface is the sandbox, not the registry. The registry is easy to inspect, but it does not carry review state, tests, ownership, or deprecation policy; safety comes mainly from constraining what execution can touch.

## What to Watch

- Whether Tendril adds a real search/ranking layer over capabilities; that would change the read-back mechanism from full-list pull to relevance-scoped pull, and possibly create a token budget surface.
- Whether `registry.maxCapabilities` becomes enforced; that would turn a configuration hint into an actual context-efficiency boundary.
- Whether capabilities gain tests, review status, provenance, or version history; that would make executable memory closer to Commonplace's governed system-definition artifacts.
- Whether session logs or tool-failure traces become durable inputs to capability improvement; that would reopen the `trace-derived` classification.
- Whether the Tauri app adds git integration or workspace backups for `tools/`; without it, capability replacement is operationally convenient but weakly reversible.

Relevant Notes:

- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Tendril separates registry JSON, executable tool files, prompt/tool schemas, sandbox wrappers, and event streams into distinct substrates, forms, lineages, and authorities.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - distinguishes: Tendril's durable capabilities and bootstrap prompt directly instruct, route, and execute future behavior.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Tendril stores capabilities, but current read-back is still the agent's explicit registry listing.
- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - contrasts: Tendril is self-extending through model-authored tools, but the reviewed code does not mine traces into durable learned artifacts.
