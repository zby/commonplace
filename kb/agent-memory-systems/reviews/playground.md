---
description: "Playground review: TribleSpace pile runtime with user-created temporal memory chunks and budget-aware context cover"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
last-checked: "2026-06-04"
---

# Playground

`playground`, by triblespace, is a Rust runtime for a shell-first autonomous agent whose durable state lives in a TribleSpace pile. At the reviewed commit, it records model thoughts, model requests/results, shell command requests/results, imported archive messages, configuration, and user-created memory chunks; the core loop assembles future model context from a budget-aware memory cover plus recent shell interaction history.

**Repository:** https://github.com/triblespace/playground

**Reviewed commit:** [3f55072517b9dc47802b9b1199d3a83607610cd0](https://github.com/triblespace/playground/commit/3f55072517b9dc47802b9b1199d3a83607610cd0)

**Source directory:** `related-systems/triblespace--playground`

## Core Ideas

**The pile is the agent's durable world model.** Playground stores runtime configuration, cognition events, command execution state, archive imports, and memory chunks in pile branches rather than in ephemeral process variables. The event-model docs define a thought -> model request -> model result -> command request -> command result chain, and the schema modules assign concrete attributes for those entities ([event model](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/docs/playground_event_model.md), [cognition schema](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/cog_schema.rs), [model schema](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/model_chat_schema.rs), [exec schema](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/exec_schema.rs)).

**The runtime separates memory from moment.** The model prompt is built from static system prompt text, selected memory summaries, a fixed breath boundary, and recent raw command results. The docs call this a `memory` stratum plus a `moment` stratum, and `build_context_messages()` implements the split by serving memory-cover messages before projecting post-boundary exec results ([system prompt](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/prompts/system_prompt.md), [context builder](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/main.rs)).

**Memory chunks are temporal summaries, not arbitrary notes.** The memory architecture defines a `memory` branch of summary chunks with `summary`, `created_at`, `start_at`, `end_at`, and `child` attributes. Chunks are addressed by time range, can form an n-ary hierarchy, and recover provenance to cognition/archive data by temporal overlap rather than by eagerly storing every source edge ([memory architecture](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/docs/playground_memory_architecture.md), [context schema](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/context_schema.rs)).

**Context efficiency is budgeted cover selection.** `build_memory_cover_messages()` starts from root chunks, drops oldest roots if summaries exceed the context body budget, then greedily replaces the widest parent with its children when the children fit. Recent moment turns fill the remaining budget, with image blob references charged conservatively so short image markers do not silently exceed the window ([cover builder](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/main.rs)).

**The breath boundary is a cache and identity device.** The fixed assistant/user pair `"breath"` and `"present moment begins."` separates stable recalled history from live moment turns. The implementation delays changed memory covers by one turn so the prompt prefix can remain stable before the cache boundary shifts ([memory architecture](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/docs/playground_memory_architecture.md), [cover delay](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/main.rs)).

**The inspected checkout exposes more read-side machinery than write-side memory automation.** The README mentions `memory build` and docs mention faculty commands such as `memory create`, but the playground CLI in this checkout has `run`, `core`, `exec`, `model`, diagnostics, and config modes, and the `faculties` symlink is not resolved inside the checkout. The review therefore treats memory creation as documented user/model faculty use, not as an inspectable automatic trace-to-chunk compiler in this repository ([CLI modes](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/main.rs), [README memory commands](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/README.md)).

## Artifact analysis

- **Storage substrate:** `graph` `files` `in-memory` — The pile stores branch facts and blob handles for configuration, cognition, execution, archive, and memory entities; imported archives and text/blob payloads are stored as pile blobs; `MemoryCoverState` is an in-process cache of the last served cover.
- **Representational form:** `prose` `symbolic` — Memory summaries, system prompts, reasoning notes, command text, outputs, and imported message text are prose; schemas, branch ids, entity links, timestamps, model/request/result metadata, config, and chunk hierarchy are symbolic.
- **Lineage:** `authored` `imported` — System prompts, configuration, and memory summaries are authored through config or faculty-style commands; archive importers preserve external chat histories as imported messages and raw JSON trees. The inspected playground repo does not include an implemented automatic trace-to-memory-summary compiler, so the review does not classify current memory chunks as code-grounded `trace-extracted`.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` — Memory summaries and archive/cognition provenance serve as knowledge; the system prompt instructs the model's one-command shell loop and memory discipline; branch/config ids route faculties and context assembly; command/result schemas, pending-result checks, and repeated failed-memory-lookup guards validate or constrain execution flow.

**Memory chunks.** The central retained memory artifact is a `kind_chunk` entity on the `memory` branch. Its operative prose is the summary blob; its symbolic parts are the time interval, child links, and legacy source-reference attributes. It shapes later behavior when the context builder renders it as a synthetic `memory.rs <range>` exchange.

**Cognition and execution traces.** Thoughts, model requests/results, command requests/results, reasoning text, stdout/stderr, and timestamps are durable trace surfaces. They are behavior-shaping as the recent moment tail and as provenance for memory chunks, but they are not themselves distilled long-term memory unless a user or faculty creates memory chunks covering their intervals.

**Archive imports.** ChatGPT, Claude Code, Codex, Copilot, Gemini, and other imported conversations enter archive branches as source material. The memory architecture recovers which archive messages a chunk summarizes by overlap against chunk time intervals, so imports can become evidence for existing memory without rewriting the chunk.

**Context snapshots.** Each thought stores the serialized context that prompted the model. This is an audit and replay artifact: it records exactly what memory/moment material the model saw, but future prompts are rebuilt from current pile state rather than reusing old thought contexts.

Promotion path: raw cognition and imported archives can be summarized into memory chunks through the memory interface described by the docs and prompt. The implemented serving path then promotes selected chunks from passive pile state into model context, with parent/child splitting increasing detail when budget allows.

## Comparison with Our System

| Dimension | playground | Commonplace |
|---|---|---|
| Primary purpose | Runtime substrate for an autonomous shell agent with pile-backed memory and execution traces | Git-native methodology KB and framework for agent-operated knowledge systems |
| Canonical artifacts | Pile branches, entity schemas, memory chunks, context snapshots, command/model traces, imported archives | Typed Markdown notes, source snapshots, reviews, type specs, generated indexes, validation reports |
| Memory shape | Temporal summary chunks over cognition/archive time ranges | Topic/claim/type-shaped Markdown artifacts with explicit links and source citations |
| Read-back | Automatic memory cover before each model request, plus explicit memory commands | Mostly deliberate pull through `rg`, indexes, links, skills, and review workflows |
| Governance | Schemas, prompt invariants, branch routing, failed-lookup guard, deterministic event chain | Schemas, deterministic validation, semantic gates, source citations, replacement archives |

The strongest alignment is source-preserving lineage. Playground keeps raw cognition, execution output, provider artifacts, and imported archives near the memory layer, while Commonplace keeps source snapshots, ingests, citations, and replaced reviews. Both designs treat memory as reviewable retained state rather than just hidden vector recall.

The main divergence is shape. Playground's memory is temporal and runtime-facing: it asks "what time interval has been summarized enough to drop from the moment?" Commonplace's memory is conceptual and library-facing: it asks "what durable claim, definition, or operating rule should future agents load or validate?"

### Borrowable Ideas

**Use temporal cover as a workshop compression model.** Needs a concrete Commonplace workshop use case. A work log could expose coarse summaries of older activity while keeping the current task raw, mirroring playground's memory/moment split.

**Make the context boundary visible.** Ready now. Commonplace prompts could name where generated context ends and live task state begins, especially in long review runs where stale summaries and current findings can blur.

**Delay changed context by one turn when caching matters.** Needs an execution harness that actually reuses prefix cache. The pattern is worth retaining for future long-running review agents.

**Recover provenance by coordinate overlap.** Ready for narrow cases. Commonplace could use timestamp or source-range overlap to associate log summaries with raw run artifacts without rewriting every summary when new raw material lands.

**Do not borrow unresolved faculty coupling as a contract.** The broken `faculties` symlink and README/CLI mismatch are adoption risks. Commonplace should keep memory-writing commands in the inspected repo or make external tool dependencies explicit.

## Write side

**Write agency:** `manual` — The code-grounded memory write path in this checkout is documented as `memory create` / consolidation through faculties and prompt instructions, while the inspected Rust runner primarily records cognition/exec traces and serves existing memory chunks. I did not find an implemented automatic memory-chunk compiler in the present checkout.

Memory writing is still behaviorally significant: a model or operator can create summaries over time ranges, link child chunks, and use temporal provenance. But under the review contract this is not enough to mark a current automatic curation operation, because the store-changing summarization implementation is outside the inspected playground source.

## Read-back

**Read-back:** `both` — Memory chunks are pushed into future model context by the core loop's pre-request context builder, and the system prompt also exposes explicit pull commands such as `memory <range>` and `memory meta <range>`.

**Read-back signal:** `coarse` — The pushed memory cover is selected by temporal roots, continuity, parent/child hierarchy, and character budget, not by semantic similarity, keyword search, identifiers emitted by the current task, or an LLM relevance judgment.

**Faithfulness tested:** `no` — I found structural context assembly, thought-context storage, prompt-cache handling, and diagnostics surfaces, but no with/without memory ablation or post-action audit proving that pushed chunks are faithfully used by the model.

**Direction edge cases.** User or model commands like `memory <range>` are pull. The automatic cover is push because the model receives selected retained memory before it chooses the next command. Recent cognition turns after the breath are active conversational state rather than long-term memory read-back.

**Targeting and signal.** The signal is coarse temporal coverage. The builder starts with roots, drops oldest roots under budget pressure, splits wide parents into children when they fit, and stops the coverage boundary at the first temporal gap. This improves granularity but does not target the current task instance by content.

**Injection point.** The injection point is pre-invocation. `create_thought_and_request()` builds a serialized context before a model request, with system prompt prepended, memory cover inserted before breath, and recent moment turns appended after breath. Memory writes or consolidation after a command would affect later context assembly, not the already-running turn.

**Selection, scope, and complexity.** Volume is bounded by model context window, max output, safety margin, system prompt cost, summary text size, and image-marker cost estimates. Complexity is bounded by the selected antichain of memory chunks, but wide parent summaries and detailed children can still carry dense, loosely related prose.

**Authority at consumption.** Served memory acts as advisory context. The system prompt gives it identity-level significance and instructs the model how to create, consolidate, and recall memories, but the memory summary text itself is not a hard gate. The failed-memory-lookup guard can inject corrective instruction when the model repeatedly queries invalid memory ids.

**Other consumers.** Diagnostics can inspect context chunks and origins. Operators can configure the pile, inspect branches, run archive importers, and use memory commands described in the prompt/docs.

## Curiosity Pass

**The README is ahead of the inspected CLI.** The README documents `memory estimate` and `memory build`, but the checked `CommandMode` enum does not expose a memory subcommand. That may reflect a split into external faculties, but the symlink is unresolved in this checkout.

**Temporal provenance is deliberately loose.** Time overlap lets newly imported archive data become evidence for old memory chunks without a rewrite pass. The tradeoff is that provenance is approximate unless intervals are chosen carefully.

**The memory cover is not retrieval in the search sense.** It is a budgeted temporal antichain. This is predictable and cache-friendly, but it will not find an old fact just because the current task semantically needs it.

**Context snapshots are a strong audit artifact.** Storing each thought's serialized context makes it possible to inspect what the model actually saw, even though the system does not yet use that audit trail to test memory faithfulness.

## What to Watch

- Whether the memory faculty source becomes part of the inspected repository or the external dependency is documented as a required companion checkout.
- Whether `memory build` / backfill gains an implemented trace-to-summary compiler in the playground repo.
- Whether memory chunks retain explicit source ids, model metadata, or review state in addition to temporal overlap.
- Whether read-back gains identifier, lexical, embedding, or judgment-based selection over memory chunks.
- Whether diagnostics or tests compare model behavior with and without the memory cover.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: playground's memory matters when chunks are served into the model context, not merely because they live in the pile.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: pile facts, prose summaries, branch schemas, context snapshots, and prompt instructions carry different forms and authorities.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: memory summaries, imported archives, and cognition traces advise as evidence and context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: schemas, prompt invariants, branch routing, context assembly, and guards configure future behavior.
- [Symbolic context engineering is bounded by symbol availability](../../notes/symbolic-context-engineering-is-bounded-by-symbol-availability.md) - explains: playground's temporal chunk selection can only target by time and hierarchy unless richer symbols are emitted into the memory layer.
