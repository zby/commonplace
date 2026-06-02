---
description: "Review of Playground, a TribleSpace-backed Rust agent runtime with shell-first turns, branch-separated traces, archive imports, and prompt-time memory covers"
type: ../types/agent-memory-system-review.md
tags: []
status: outdated
last-checked: "2026-05-16"
---

# Playground

> Replaced 2026-06-02. See [playground](./playground.md) for the current review.

Playground is TribleSpace's Rust experiment in a shell-first agent runtime. It stores cognition, model calls, shell execution, imported chat archives, configuration, and memory summaries in an append-oriented TribleSpace pile, then rebuilds each model prompt from branch-local state instead of treating chat history as the only source of context.

**Repository:** https://github.com/triblespace/playground

**Reviewed commit:** [462c4aca532d1c0b9de6ae70bf029e6c2fc60e52](https://github.com/triblespace/playground/commit/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52)

## Core Ideas

**The runtime is a shell-first loop over an append-only pile.** The design document defines the core as "LLM result -> exec request -> exec result -> new prompt", and the code follows that shape: `run_loop` waits for model results, interprets the model's `output_text` as one shell command, appends a command request, waits for a command result, and then appends the next thought/request pair ([design.md](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/design.md), [src/main.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/main.rs)). The execution worker runs `sh -lc`, records stdout/stderr bytes, UTF-8 projections, exit code, duration, timeout errors, and process-tree termination into `playground_exec` result entities ([src/exec_worker.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/exec_worker.rs)). The behavioral authority of this trace is mostly evidential: command results are knowledge artifacts for the next prompt, while the loop and system prompt are system-definition artifacts because they route the model into one side-effecting shell action per turn.

**Branches separate raw execution, imported archives, memory summaries, and configuration.** The memory architecture doc names independent `memory`, `cognition`, and `archive` branches, and the config loader uses a separate `config` branch for runtime settings ([docs/playground_memory_architecture.md](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/docs/playground_memory_architecture.md), [src/config.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/config.rs)). In code, the cognition branch holds thoughts, model requests/results, command requests/results, and moment boundaries; the `memory` branch is pulled separately before prompt assembly; and diagnostics can inspect configured role branches such as config, exec, compass, local messages, relations, teams, and wiki ([src/main.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/main.rs), [src/diagnostics.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/diagnostics.rs)). The storage substrate is one pile, but branch identity gives different retained artifacts different ownership and consumption paths.

**Prompt context is a budget-adaptive memory cover plus recent moment.** `playground_context::kind_chunk` stores a summary blob, start/end TAI intervals, child links, and optional provenance links to exec results or archive messages ([src/context_schema.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/context_schema.rs)). At prompt-build time, Playground loads memory chunks, starts from root chunks, drops oldest roots if the summaries exceed budget, then greedily splits the widest parent whose children fit; it inserts a fixed `breath` / `present moment begins.` boundary and fills the remaining budget with recent raw shell turns ([src/main.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/main.rs), [docs/playground_memory_architecture.md](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/docs/playground_memory_architecture.md)). The memory summaries are prose knowledge artifacts when read as recalled context; the selection algorithm, context budget fields, and breath boundary are symbolic system-definition artifacts because they decide what reaches the model.

**Imported archives preserve raw provenance before memory promotion.** The importer files cover ChatGPT, Claude Code, Codex, Copilot, and Gemini exports, importing raw JSON trees and projecting conversations/messages with `source_format`, source conversation/message IDs, source roles, timestamps, authors, content, and raw roots ([importers](https://github.com/triblespace/playground/tree/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/importers), [src/archive_schema.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/archive_schema.rs)). These imported archive artifacts are retained knowledge artifacts: queryable evidence and source material, not instructions. They become behavior-shaping prompt memory only when summarized into `playground_context::kind_chunk` entities that the memory cover consumes.

**Provider artifacts are retained without becoming the canonical dialogue.** The model worker builds OpenAI-compatible or Anthropic payloads, retries transient failures, stores request payloads, response raw JSON, output text, reasoning text, response IDs, token usage, cache usage, and imported response JSON roots ([src/model_worker.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/model_worker.rs)). That gives the system a detailed audit trail while keeping the canonical turn chain as thought -> request -> result -> command request -> command result. The raw provider response is evidence; the extracted output text has stronger authority because the core treats it as the next shell command.

**Diagnostics are a real runtime surface, not just logging.** The optional diagnostics feature uses `eframe`, `GORBIE`, and `egui_plot` to inspect pile branches, timelines, archive messages, config, and context chunks, including child relationships and leaf origins ([Cargo.toml](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/Cargo.toml), [src/diagnostics.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/diagnostics.rs)). This matters because Playground's memory system is otherwise hard to inspect from flat files: diagnostics are the human-facing projection over the append-only pile.

## Comparison with Our System

| Dimension | Playground | Commonplace |
|---|---|---|
| Primary substrate | TribleSpace pile with branches and blob handles | Git-tracked Markdown files plus generated indexes |
| Raw traces | Cognition/model/exec entities and imported archive projections | Shell history is mostly outside the KB unless snapshotted or written into notes |
| Durable memory | Time-ranged prose chunks with child/provenance edges | Typed notes, references, instructions, reviews, source snapshots, and generated reports |
| Prompt assembly | Runtime algorithm selects memory cover and recent moment under a token budget | Agents navigate indexes and load files by task; no central prompt builder |
| Provenance | Chunk links to exec result/archive message IDs; raw provider JSON roots retained | Source URLs, frontmatter, git history, validation/review reports |
| Governance | System prompt, faculties, config, branch conventions, diagnostics | Collection/type contracts, validation, review gates, skills, indexes |

The strongest alignment is that both systems distinguish raw retained evidence from behavior-shaping summaries. Playground's raw cognition branch, provider JSON, shell outputs, and archive imports are not themselves the memory that guides future action; memory chunks are the distilled surface selected into the prompt. Commonplace makes a similar split through source snapshots, reviews, notes, instructions, and generated indexes, but uses readable files and validation rather than a graph pile and runtime prompt assembler.

Playground is much stronger than commonplace on live context assembly. Its budget model reserves output and safety tokens, computes body characters, gives memory priority, uses recent moment for unsummarized turns, and warns the model about context fill ([src/main.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/main.rs), [docs/playground_event_model.md](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/docs/playground_event_model.md)). Commonplace relies on progressive disclosure and agent discipline; it has no equivalent central scheduler deciding the prompt cover.

Commonplace is stronger on artifact contracts and maintainability. A commonplace note can be opened, reviewed, linked, validated, retired, and diffed with ordinary repo tools. Playground's pile gives precise provenance and append discipline, but most semantic structure is visible through Rust schemas, diagnostics, and faculties rather than through directly editable source artifacts.

The docs slightly overclaim current mechanics. The README advertises `memory estimate` and `memory build`, but the checked-in `CommandMode` enum at this commit exposes `run`, `core`, `exec`, `model`, `diagnostics`, and `config`, not `memory` subcommands ([README.md](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/README.md), [src/main.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/main.rs)). The memory architecture doc is explicit that automatic compaction and lenses were dropped; current promotion is explicit via a memory faculty, not an in-core automatic compactor ([docs/memory_temporal_redesign.md](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/docs/memory_temporal_redesign.md), [docs/playground_memory_architecture.md](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/docs/playground_memory_architecture.md)).

**Read-back:** push — the runtime selects memory chunks and recent shell turns into a budgeted prompt cover before each model call.

## Borrowable Ideas

**Separate raw trace branches from prompt memory.** Commonplace should keep treating raw logs and source snapshots as evidence rather than as immediately loaded memory. Playground's branch split is a useful design analogue for making raw execution/chat traces, imported archives, summaries, and runtime config visibly different artifacts. Ready to borrow as vocabulary and documentation, not as a pile dependency.

**Use a memory cover rather than a flat summary.** The n-ary time-range chunk tree is a practical answer to "which summary should fit?" In commonplace this would look like generated session/workshop digests with child summaries and a budget-aware loader, not a wholesale replacement for notes. Needs a concrete long-session use case first.

**Put context pressure in the agent's lived prompt.** Playground appends context fill percentage to the latest user message so the model can decide when to consolidate or become concise. Commonplace could expose a cheaper version in long-running skills: report loaded-token pressure and recommend promotion/compaction before the session fails.

**Keep provenance edges on summaries.** `about_exec_result` and `about_archive_message` are exactly the right lineage shape for trace-derived summaries: the summary is compact, but the raw event remains inspectable. Commonplace already has source links and review reports; the borrowable idea is tighter machine-readable links from summaries to raw execution or import records.

**Use diagnostics as a first-class memory interface.** A graph/pile substrate needs a dashboard that shows branches, chunks, origins, and timelines. Commonplace's equivalent is not a GUI, but richer review reports and generated indexes that make derived memory surfaces inspectable without reading implementation code.

## Trace-derived learning placement

Playground qualifies as trace-derived learning, but not as automatic trace mining inside the core loop. The qualifying pattern is staged: raw cognition turns and imported chat archives are retained as evidence, then explicit memory chunks derived from those traces can become durable prompt memory consumed by later model calls.

**Trace source.** Playground records live agent traces as thoughts, model requests/results, command requests/results, reasoning text, provider raw JSON, stdout/stderr, exit codes, and timestamps in the cognition branch ([src/main.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/main.rs), [src/model_worker.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/model_worker.rs), [src/exec_worker.rs](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/src/exec_worker.rs)). It also imports prior ChatGPT, Claude Code, Codex, Copilot, and Gemini conversations into a unified archive projection while keeping raw JSON roots ([importers](https://github.com/triblespace/playground/tree/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/importers)).

**Extraction.** The core repository defines and consumes memory chunks, and the docs say the `memory create [<from>..<to>] <summary>` faculty creates summaries, parses child links, and links leaf chunks to in-range cognition/archive events when no children are supplied ([docs/playground_memory_architecture.md](https://github.com/triblespace/playground/blob/462c4aca532d1c0b9de6ae70bf029e6c2fc60e52/docs/playground_memory_architecture.md)). That extraction oracle is the user or model operating the faculty, not an automatic in-core compaction worker at this commit.

**Storage substrate.** Raw and distilled artifacts live in the same TribleSpace pile but on different branches. Raw execution/chat traces live on cognition and archive branches; distilled memory chunks live on the memory branch; config/headspace state lives on config-like branch surfaces; diagnostics are projections over the pile rather than canonical memory.

**Representational form.** Raw trace entities are mixed: symbolic schemas and IDs wrap prose command text, outputs, summaries, and provider JSON/blob payloads. Memory chunks are prose summaries with symbolic time intervals, child links, and provenance IDs. The prompt cover is a derived mixed representation: assistant/user chat turns synthesized from memory chunk summaries and raw shell moments.

**Lineage.** The strongest lineage path is from memory chunk to `about_exec_result` or `about_archive_message`, plus child edges for consolidated chunks. Raw archive importers also retain source format, source IDs, timestamps, and raw JSON roots. Invalidation and regeneration are weaker: append-only history is preserved, but the current repo does not show a review state, confidence score, stale marker, or automatic rebuild rule for memory chunks.

**Behavioral authority.** Raw command results, model results, archive messages, and provider JSON are knowledge artifacts: they can inform later prompts and diagnostics as evidence. Memory chunks are knowledge artifacts when read as recalled context, but they acquire stronger behavior-shaping force because the prompt builder selects them into the model context before current moment turns. The system prompt, branch/config settings, faculties, and prompt assembly code are system-definition artifacts because they instruct, route, configure, and prioritize behavior.

**Scope and timing.** The scope is per-pile/persona and cross-session. Extraction is staged and explicit, while consumption is online: every new thought can receive a budget-adaptive memory cover before the recent moment.

**Survey placement.** Playground strengthens the survey axis separating raw trace retention from distilled behavior-shaping artifacts. It is not a "chat transcript as memory" system; it is a trace/archive substrate plus explicit summary promotion plus runtime prompt-cover selection.

## Curiosity Pass

**The most interesting memory code is consumption, not creation.** The core binary contains robust prompt-cover selection and trace storage, but not the advertised `memory build` CLI path. That makes Playground more compelling as a runtime context assembler than as a fully closed memory-consolidation loop at this commit.

**Append-only does not automatically mean authoritative.** A pile preserves event history and provenance, but the system still needs policies for which summary to trust, when to replace stale chunks, and when a memory should become instruction. Playground has storage lineage; commonplace has stronger curation contracts.

**The shell-first loop is both elegant and narrow.** Treating the shell as the model's physical reality makes every action observable and replayable, but it also turns non-shell actions into faculties or command wrappers. The architecture works best when tool surfaces can be reduced to commands.

**Diagnostics compensate for an opaque substrate.** The pile is richer than files, but harder to inspect with ordinary tools. The diagnostics dashboard is therefore part of the memory architecture, not a convenience feature.

**Docs and code are in active negotiation.** `memory_temporal_redesign.md` is unusually useful because it says what was dropped: lenses, automatic compaction, merge arity, and archive reification. That prevents reviewers from mistaking design history for shipped behavior.

## What to Watch

- Whether memory chunk creation and backfill move into the checked-in core binary or remain in external faculties.
- Whether memory chunks gain lifecycle fields such as confidence, reviewer, stale/superseded state, or regeneration policy.
- Whether archive importers become part of a packaged CLI surface rather than source files under `importers/`.
- Whether diagnostics evolves from inspection into repair, review, or promotion workflow.
- Whether wiki and cognition faculties produce durable system-definition artifacts, not only knowledge-artifact summaries.

---

Relevant Notes:

- [knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: raw traces, archive messages, provider JSON, and memory summaries mostly advise future behavior as evidence or context
- [system-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: the prompt builder, config, system prompt, and faculties carry routing/instruction/configuration force
- [behavioral authority](../../notes/definitions/behavioral-authority.md) - explains: Playground's same pile holds evidence artifacts and stronger runtime-control artifacts
- [lineage](../../notes/definitions/lineage.md) - frames: chunk provenance links preserve source trace dependencies
- [retained artifact](../../notes/definitions/retained-artifact.md) - grounds: raw turns, imported archives, chunks, configs, and prompts are retained only when they can shape later behavior
- [context efficiency is the central design concern in agent systems](../../notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md) - exemplifies: prompt covers adapt detail to a bounded context budget
