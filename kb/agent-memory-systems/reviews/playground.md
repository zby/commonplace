---
description: "Playground review: TribleSpace-backed autonomous model-shell loop with budgeted memory-cover push, archive importers, and durable cognition/model/exec traces"
type: ../types/agent-memory-system-review.md
tags: [push-activation]
status: current
last-checked: "2026-06-02"
---

# playground

Playground, from TribleSpace's `triblespace/playground` repository, is a Rust runtime for an autonomous model-shell loop over a TribleSpace pile. It records cognition, model requests/results, command requests/results, archive imports, configuration, and context-memory chunks as branch-local graph facts and blob handles. At the reviewed commit, its strongest memory mechanism is not vector retrieval or automatic lesson extraction. It is a pre-model-call context assembler that pushes a budgeted, hierarchical memory cover into every prompt, then appends recent raw command turns after a fixed "breath" boundary.

**Repository:** https://github.com/triblespace/playground

**Reviewed commit:** [3f55072517b9dc47802b9b1199d3a83607610cd0](https://github.com/triblespace/playground/commit/3f55072517b9dc47802b9b1199d3a83607610cd0)

**Last checked:** 2026-06-02

## Core Ideas

**The pile is the durable substrate for cognition, execution, model calls, archive history, memory, and config.** The design document frames Playground as a deterministic loop: LLM result to exec request, exec result to new prompt, with all effects mediated by TribleSpace rather than direct provider or OS calls from the core ([design.md](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/design.md)). The implementation opens a pile, ensures branches, writes `kind_thought`, `model_chat::kind_request`, `model_chat::kind_result`, `playground_exec::kind_command_request`, and `playground_exec::kind_command_result` facts, and stores large text or JSON payloads as blobs ([src/main.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/main.rs), [src/model_chat_schema.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/model_chat_schema.rs), [src/exec_schema.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/exec_schema.rs)).

**The agent loop is shell-first and sequential.** The system prompt tells the model to emit exactly one shell command line per turn, and the core loop trims the model output into a command request, waits for an exec result, and creates the next thought from that result ([prompts/system_prompt.md](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/prompts/system_prompt.md), [src/main.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/main.rs)). The exec worker runs commands in a non-interactive shell, captures stdout/stderr/exit/error, exports `PILE`, `WORKER_ID`, and `TURN_ID`, and puts `/workspace/faculties` plus `/opt/playground/faculties` on `PATH` ([src/exec_worker.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/exec_worker.rs)).

**Memory is a separate branch of hierarchical chunks.** The current memory architecture document describes three independent branches: `memory` for summary chunks, `cognition` for active execution state, and `archive` for imported historical messages ([docs/playground_memory_architecture.md](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/docs/playground_memory_architecture.md)). The code backs the chunk schema with `summary`, `start_at`, `end_at`, child links, and legacy provenance attributes ([src/context_schema.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/context_schema.rs)). In the inspected Playground repo, chunk creation is not implemented as a `playground` CLI subcommand; docs and prompts point to a `memory` faculty, while the `faculties` path is a symlink to a sibling repo and the Cargo manifest depends on `../faculties` ([Cargo.toml](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/Cargo.toml), [faculties](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/faculties)).

**Context efficiency is implemented as a memory-cover plus moment-tail budget.** `build_context_messages` computes a body budget from context window, max output, safety margin, chars-per-token, and system prompt length; pushes selected memory chunks before the breath boundary; then fills the remaining budget with the most recent raw command turns ([src/main.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/main.rs)). Memory cover selection starts from chronological root chunks, drops oldest roots if the coarse cover exceeds budget, then greedily replaces the widest parent with its children when the extra cost fits. This bounds both volume and complexity: old history is compressed into summaries, recent state remains raw, and hierarchical splits expose detail only where budget allows.

**The breath boundary is a prompt-cache and cognition boundary.** The prompt assembler inserts assistant `"breath"` and user `"present moment begins."` between memory and moment, delays memory-cover changes by one turn, and appends context-fill percentage to the tail rather than the cacheable prefix ([src/main.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/main.rs)). The model worker places Anthropic cache-control breakpoints at the breath user message and the second-to-last user message ([src/model_worker.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/model_worker.rs)).

**Archive importers preserve prior conversations as message graphs, not as automatically distilled memory.** Importers for Claude Code, Codex, ChatGPT, Gemini, and Copilot parse external logs, import raw JSON trees where applicable, and write semantic `archive::kind_message` facts with author, content, timestamp, source-role metadata, and reply links ([importers/archive_import_claude_code.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/importers/archive_import_claude_code.rs), [importers/archive_import_codex.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/importers/archive_import_codex.rs), [importers/archive_import_chatgpt.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/importers/archive_import_chatgpt.rs)). Claude Code imports also render thinking/tool-use/tool-result blocks into readable archive content. I did not find implemented code in this checkout that turns archive messages or cognition traces into durable `kind_chunk` summaries.

**Diagnostics treats memory shape as inspectable state.** With the default `diagnostics` feature, the dashboard reads branches incrementally and renders context compaction trees, selected chunks, children, and leaf origins directly from `kind_chunk` facts ([src/diagnostics.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/diagnostics.rs), [Cargo.toml](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/Cargo.toml)). That makes the retained memory cover auditable as a graph, not only visible through prompt text.

## Artifact analysis

- **Storage substrate:** `files` — A local TribleSpace pile file, with named branches such as config, cognition, memory, archive, and auxiliary branches used by faculties or diagnostics
- **Representational form:** `symbolic` — Symbolic graph facts plus blob handles for long strings, unknown blobs, raw JSON, and simple archives
- **Lineage:** `authored` `imported` `trace-extracted` — Runtime/config/faculty actions author pile facts, archive importers preserve external logs, and cognition/model/exec traces are generated online; this does not imply an implemented trace-to-memory compiler in this checkout
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` — History, archive, and diagnostics surfaces are knowledge artifacts; prompt/config/context assembly instruct and route the model loop; command-only behavior and schema-shaped branch facts constrain and check runtime state

**TribleSpace pile and branches.** Storage substrate: a local TribleSpace pile file, with named branches such as config, cognition, memory, archive, and auxiliary branches used by faculties or diagnostics. Representational form: symbolic graph facts plus blob handles for long strings, unknown blobs, raw JSON, and simple archives. Lineage: authored by the runtime, workers, importers, config commands, and external faculty commands; invalidation is branch/head and blob-handle based rather than file-path based. Behavioral authority: system-definition artifact when branch state drives model requests, command execution, config, routing, prompt assembly, and diagnostics; knowledge artifact when inspected as history.

**Cognition/model/exec turn chain.** Storage substrate: the cognition branch in the pile. Representational form: symbolic lifecycle entities plus prose/blob payloads for contexts, model outputs, reasoning text, commands, stdout, stderr, and raw provider responses. Lineage: generated online by the core loop, model worker, and exec worker. Each turn links thought to model request/result and command request/result, with provider raw JSON imported where possible. Behavioral authority: system-definition artifact because the latest result determines the next prompt and next command; knowledge artifact when later read for audit, provenance, or diagnostics.

**Memory chunks.** Storage substrate: the `memory` branch in the pile. Representational form: mixed prose and symbolic structure: a summary blob, time intervals, child edges, and legacy explicit provenance links. Lineage: documented as user/model-created by a `memory` faculty, but the supplied Playground repo only contains the schema and read path. The implemented prompt builder treats chunks as already existing retained summaries and does not verify how they were created. Behavioral authority: advisory context pushed into model prompts; authority becomes stronger than ordinary reference material because it is automatically included before actions when selected by the cover algorithm.

**Memory cover.** Storage substrate: transient prompt JSON stored as the `playground_cog::context` and `model_chat::context` blob for each thought/request. Representational form: chat messages that synthesize memory chunks into alternating assistant command strings like `memory.rs <range>` and user summary text. Lineage: derived from the current memory branch, budget settings, moment boundary, chunk hierarchy, and previous-cover delay. Behavioral authority: pre-action push context for the next model call; it can change the next command without the model asking for memory.

**Moment turns and breath boundary.** Storage substrate: transient assembled context plus durable thought/request context blobs. Representational form: chat messages with raw command/result projections, reason events, reasoning text, timestamps, and context-fill annotation. Lineage: derived from cognition branch exec/model facts after the selected moment floor. Behavioral authority: immediate working context. The breath boundary itself is system-definition prompt structure because it partitions cacheable recalled history from volatile present-moment evidence.

**Archive imports.** Storage substrate: archive branch facts and imported raw JSON/blob trees. Representational form: symbolic message/author/reply metadata with prose content blobs and, for some importers, lossless raw JSON tree imports. Lineage: imported from external logs or exports such as Claude Code JSONL, Codex JSONL, ChatGPT data exports, Gemini, and Copilot. Behavioral authority: knowledge artifacts until a human, model, or unavailable faculty summarizes them into memory chunks or reads them through an archive faculty. The importers alone do not give archive messages prompt authority.

**Runtime configuration and system prompt.** Storage substrate: config branch facts plus bundled prompt files. Representational form: symbolic model/base-url/context-window/max-output/safety-margin/exec settings plus prose system prompt. Lineage: defaults in code and prompts, overridden through `config set` fields persisted in the pile. Behavioral authority: system-definition artifact. It sets the agent role, command-only policy, context budget, provider payload shape, execution defaults, and faculty expectations.

**Diagnostics and conceptual notebooks.** Storage substrate: authored Rust code and transient UI state. Representational form: symbolic queries and visualization code. Lineage: authored tooling over pile branches. Behavioral authority: audit and operator-facing knowledge surface, not direct prompt authority, except insofar as diagnostics findings lead a human or agent to edit memory/config.

There is no verified promotion ladder in this checkout from raw trace to memory chunk to enforced rule. There is a strong read path for already-created chunks, and there are archive/cognition traces with provenance, but durable behavior-shaping memory creation lives in the unavailable sibling faculties surface or in manual model actions described by the prompt.

## Comparison with Our System

| Dimension | Playground | Commonplace |
|---|---|---|
| Primary purpose | Autonomous model-shell runtime with durable graph state and prompt assembly | Git-native agent-operated methodology KB |
| Main retained substrate | TribleSpace pile branches plus blobs | Markdown collections, schemas, generated indexes, reports, git history |
| Memory unit | Time-scoped summary chunks in a hierarchy | Typed notes, instructions, ADRs, reviews, sources, indexes |
| Context strategy | Pre-call memory cover plus breath plus recent moment turns under budget | Agent pull over indexes/search/links, collection contracts, skills, validation/review outputs |
| Trace handling | Durable cognition/model/exec/archive traces; no verified trace-to-chunk compiler in this repo | Source snapshots, work artifacts, review reports, and explicit promotion into library artifacts |
| Governance | Schema IDs, append-style event facts, diagnostics, cache-aware context policy | Type specs, collection contracts, deterministic validation, semantic review, replacement archives |

Playground is much closer to an agent runtime than to a knowledge base. Commonplace stores durable methodology artifacts and asks agents to pull the relevant ones by search, index, links, or skill workflow. Playground stores the agent's lived event stream and pushes a selected memory cover into every model call. That makes the read-back path more active than Commonplace's default navigation, but the retained artifacts are less governed: a selected memory chunk is trusted because it exists and fits the temporal cover, not because it passed a collection contract or review gate.

The most useful Commonplace comparison is the split between retained evidence and prompt authority. Playground preserves excellent evidence: raw command results, model outputs, provider responses, archive imports, timestamps, and branch state. But once a memory chunk exists, the prompt assembler can grant it immediate advisory authority. Commonplace is slower but more explicit: source material and traces must be written, typed, validated, reviewed, and linked before they become high-authority instructions or durable methodology claims.

Playground also treats context caching as a first-class design constraint. Commonplace usually optimizes retrieval and reviewability; Playground optimizes continuity under a live model loop, including prefix-cache survival across memory-cover changes. That is a distinct form of context engineering worth borrowing, but only for runtime packs where repeated model calls consume a stable history prefix.

**Read-back:** `both` — With engineered push. The model can run memory/archive/orient faculties as pull commands, but the implemented core also pushes a selected memory cover before each model action. Targeting is `coarse`: every model request receives a continuity cover selected by time, hierarchy, and budget, not by an instance identifier or inferred task relevance.

### Borrowable Ideas

**Budgeted memory cover as a runtime context pack.** Commonplace could build optional session-start or per-task context packs that choose an antichain over durable notes or work artifacts under a budget. Needs a specific runtime use case first; the current KB is still better served by explicit pull navigation.

**A visible boundary between recalled memory and live moment.** The breath pattern cleanly separates stable long-term context from volatile current work and makes cache behavior inspectable. Ready to borrow for any Commonplace-driven agent loop that repeatedly assembles prompts.

**One-turn delay before switching stable context.** Playground's delayed cover update is an operational trick for prompt-cache stability. Ready only when we have a repeated-call runtime where cache churn matters.

**Treat context fill as a behavioral signal.** Playground appends fill percentage so the model can choose consolidation or brevity. Commonplace could expose budget pressure in review/write workflows, but it should be advisory rather than automatic until the failure mode is observed.

**Keep archive imports separate from behavior-shaping memory.** Playground's split between imported archive messages and memory chunks is the right boundary. Commonplace should preserve that distinction: sources and traces are evidence until an explicit promotion step writes a reviewed artifact.

**Do not borrow implicit authority for unreviewed summaries.** Playground's automatic memory cover is powerful, but Commonplace should not let arbitrary summaries become high-authority methodology context without type, review, and validation status.

## Read-back placement

**Direction.** Both. Pull exists through command/faculty affordances described in the system prompt and docs. Push exists in the implemented core: `create_thought_and_request` loads the memory branch, builds context messages, stores the context blob, and creates the model request before the model acts.

**Read-back signal:** `coarse` — Every model request receives a continuity cover selected by time, hierarchy, and budget, not by an instance identifier, lexical query, embedding similarity, or judgment.

**Read-back timing:** `pre-action` — The selected memory cover is assembled before the model call that produces the next shell command.

**Faithfulness tested:** `no` — The review found no WITH/WITHOUT ablation, perturbation test, or post-action audit proving selected memory changes behavior as intended.

**Targeting and signal.** The memory-cover push is `coarse`. It fires for each model request and selects a continuity cover from the memory branch using root chunks, `start_at`/`end_at`, child edges, moment boundary, continuous coverage, and budget fit. Signal is n/a because the selected cover is not keyed to this task by an identifier, lexical query, embedding similarity, or LLM relevance judgment. Static code verifies the cover-selection mechanics, not precision, context dilution, or effective behavioral use.

**Timing relative to action.** The selected memory cover is assembled before the model call that produces the next shell command. It is therefore pre-action context, not a post-action reflection.

**Selection, scope, and complexity.** Selection is budgeted. The body budget reserves output and safety margin, subtracts system prompt cost, chooses memory first, then moment turns. The cover starts coarse, drops oldest roots if needed, and splits the widest parent into children only when the children's extra cost fits. Moment turns keep the most recent raw command interactions after the breath/memory floor. Complexity is bounded by tree depth and the number of selected summaries plus tail turns, not by arbitrary archive size.

**Authority at consumption.** Memory cover chunks are advisory prompt context. They do not hard-gate commands, but because they arrive without a model pull decision, they have stronger behavioral authority than ordinary archive records. Config and system prompt remain higher authority because they set command-only behavior and context construction policy.

**Faithfulness.** I found no WITH/WITHOUT ablation, perturbation test, or post-action audit that proves selected memory changes behavior as intended. Static code verifies activation mechanics, budget policy, and prompt placement, not effective use.

**Other consumers.** Diagnostics consumes the same chunk graph for human/operator inspection. Importers and archive faculties can support retrospective querying, but archive records are not automatically pushed unless they become memory chunks or are pulled into the moment by a command.

## Curiosity Pass

**The README currently outruns `main.rs`.** The README advertises `memory estimate`, `memory build`, `memory-compaction-arity`, and lens configuration; the current `CommandMode` enum exposes run/core/exec/model/diagnostics/config, and config field enums do not include those memory or lens fields ([README.md](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/README.md), [src/main.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/main.rs), [src/config.rs](https://github.com/triblespace/playground/blob/3f55072517b9dc47802b9b1199d3a83607610cd0/src/config.rs)). The older `docs/playground.md` says memory lenses are computed on failed turns, while `docs/memory_temporal_redesign.md` says lenses and automatic compaction were removed or replaced. The code supports the latter for this checkout.

**The sibling faculties repo is architecturally important but not available inside the supplied source directory.** The system prompt names faculties as core agent tools, `exec_worker` puts faculty directories on `PATH`, and `Cargo.toml` depends on `../faculties`. Because the symlink target is outside the reviewed checkout, this review does not treat faculty-side `memory create` or archive query behavior as code-verified Playground implementation.

**The memory-cover push is not relevance matching in the usual RAG sense.** It can be very effective for autobiographical continuity, but it does not answer "which memory is relevant to this task?" It answers "which summarized time ranges should remain in the agent's continuity under budget?"

**Archive imports are trace preservation, not trace-derived learning by themselves.** They are valuable because they retain prior sessions in a queryable graph. The missing step is durable summarization into behavior-shaping chunks with a clear oracle, curation policy, and invalidation story.

**The diagnostics dashboard makes the memory tree unusually inspectable.** Many memory systems hide retrieval state inside vector indexes or provider calls. Playground's selected chunks, children, and origins are graph-visible, which makes context-cover debugging much more concrete.

## What to Watch

- Whether the `triblespace/faculties` memory faculty is vendored, pinned, or reviewed together with Playground; that would determine whether `memory create` and archive-to-memory workflows are implemented enough to classify trace-derived learning.
- Whether `memory estimate/build` and lens/compaction config return to `main.rs` or are removed from README/docs; that drift currently affects operator trust.
- Whether archive and cognition traces gain an implemented summarization pipeline into `kind_chunk` summaries; that would change the trace-derived tag decision.
- Whether cover selection adds task relevance, retrieval scoring, or source freshness checks; that would move it from temporal continuity push toward relevance-gated push.
- Whether selected memory influence is evaluated with ablations or diagnostics; that would clarify whether context presence actually changes behavior.
- Whether memory chunks gain review/status/provenance metadata beyond temporal overlap; that would make automatic push safer for high-authority contexts.

## Bottom Line

Playground is a serious runtime memory design for an autonomous terminal agent. Its durable state is a TribleSpace event graph; its distinctive context mechanism is an engineered pre-action memory-cover push with a stable breath boundary and budget-aware hierarchical splitting. It should carry `push-activation`. It should not carry `trace-derived` from this checkout: raw traces and archive imports are durable, but the implemented path from those traces into durable behavior-shaping memory chunks is not present in the reviewed Playground source.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - contrasts: Playground does implement contextual activation for memory chunks, while archive imports remain stored evidence until pulled or summarized.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Playground separates pile branches, memory chunks, context blobs, archive imports, runtime config, and diagnostics by substrate, form, lineage, and authority.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: archive records, raw model/exec traces, and diagnostics views mostly serve as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: system prompt, config facts, prompt assembly code, worker schemas, and pushed memory cover shape future behavior.
- [Context engineering](../../notes/definitions/context-engineering.md) - frames: Playground's central design problem is selecting and arranging memory plus recent moment under a bounded context window.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - gap: Playground preserves traces, but this checkout does not implement the durable trace-to-memory extraction step.
