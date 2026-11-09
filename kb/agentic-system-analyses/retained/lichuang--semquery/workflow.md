---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "semquery workflow: a streamed question over an indexed workspace, from retrieval handoffs to citation filtering and CLI delivery."
run-id: AAS-2026-11-09-semquery-b21559990932-01
reviewed-boundary: "0820927160b1400990fa8cc057807c73bbf6d025"
---

# semquery workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is `semq ask` over a previously indexed workspace. It connects semquery's persistent knowledge state to its model-backed delivered product, rather than joining unrelated capabilities into an invented autonomous-agent loop. The preparatory ingestion route is [RT-RTE-index-admission](runtime.md#rt-rte-index-admission); the request itself follows [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search) and [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation). Code owns the stage sequence. The model supplies answer text, not task delegation, tool choice or a decision to retry.

This is an implementation account under SRC-1 at the revision in [boundary](boundary.md), not an observed successful workflow. Direct inspection for this member covers `crates/semquery/src/main.rs` (`run_ask`), `crates/semquery/src/engine.rs` (`ask`, `ask_stream`, `spawn_ask`), `crates/semquery-synth/src/synthesizer.rs` (stream setup and `ask_internal`), `crates/semquery-synth/src/prompt.rs`, and `crates/semquery-synth/src/citation.rs`. These supply implementation evidence, including inspection of the citation parser initially left unread in the boundary account. No additional source or evidence layer is introduced. Other stage details below use the supplied runtime records and their retained passages. Neither model compliance nor end-to-end answer quality is established by shipped code or test bodies.

### Request and consequential handoffs

1. **User to CLI and Engine.** The user supplies a query and chooses text or JSON output; the workspace already holds admitted documents and retrieval representations. `run_ask` opens an Engine using configuration, workspace and model-cache paths, then drains its ask stream. Ordinary `Engine::open` does not immediately load models. The spawned ask task lazily ensures embedding, reranking and chat models before building the synthesizer; model-load failures become error items. An Engine built with injected components can reuse a prebuilt synthesizer instead. These are software component calls, not task-owning agents. Configuration admission and adapter limits remain as recorded in [RT-RTE-config-admission](runtime.md#rt-rte-config-admission). Evidence: SRC-1, `crates/semquery/src/main.rs`, `crates/semquery/src/engine.rs`.

2. **Synthesizer to retriever.** `ask_internal` requests five hits and forwards retrieval stage events. Recall reads retained workspace state; lexical and vector recall run concurrently, fusion combines ranks, and the reranker scores a configured prefix. Code selects and assembles the final hits. A model relevance score is not an external reference answer or human approval. The caller gets stage progress, but does not decide each hit. Either recall error terminates this path rather than triggering a one-channel fallback; see [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search). Evidence: SRC-1, `crates/semquery-synth/src/synthesizer.rs`, `crates/semquery-retrieve/src/retriever.rs`.

3. **Selected hits to chat inference.** The synthesizer emits the hits, numbers the available citation markers and builds a prompt containing paths, byte ranges, chunk text and query. The prompt asks for grounding in that context and numeric citations. This supplies selected document content and instructions, not a separately delegated research task. In the default GGUF adapter, formatted input exceeding the reserved context budget loses its beginning; therefore the offered hits and marker list do not establish that every passage reached inference. No semantic summary or within-generation reload repairs that loss. The concrete model's version and mutability limits are in [RT-CMP-gguf-llm](runtime.md#rt-cmp-gguf-llm); context selection and suffix retention are in [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation). Their effect is model-visible context control, not a durable subagent workspace. Evidence: SRC-1, `crates/semquery-synth/src/prompt.rs`, `crates/semquery-synth/src/synthesizer.rs`, `crates/semquery-model/src/gguf.rs`.

4. **Inference to citation metadata and output.** The inference callback emits token events before citation parsing. After inference returns, code extracts valid markers, deduplicates them and maps them to hit paths and byte ranges. It then emits `AnswerComplete` carrying raw answer text, citation metadata and timings. The Engine forwards those events; the CLI consumes them. No second model critiques the answer, and the inspected route does not revise answer text in response to invalid markers. The limited rejection mechanism is [RT-CLM-citation-filter](runtime.md#rt-clm-citation-filter), not factual verification. Evidence: SRC-1, `crates/semquery-synth/src/synthesizer.rs`, `crates/semquery-synth/src/citation.rs`, `crates/semquery/src/engine.rs`.

### Verification, rejection and recovery

The parser can reject a marker from the metadata list because it is outside the offered marker set or already seen. It cannot reject an unsupported sentence, require any citation, or prove that a valid marker entails the sentence. Raw output is retained unchanged. The relevant passage and counterpath are already retained in [RT-CLM-citation-filter](runtime.md#rt-clm-citation-filter). Grounding remains a natural-language request through [RT-BAP-prompt-influence](runtime.md#rt-bap-prompt-influence), with no answer oracle or per-answer human admission on this open-query route.

A concrete non-generation branch occurs after retrieval: zero hits produce an `AnswerComplete` with empty text and citations, followed by return, rather than an ungrounded completion. Engine model loading precedes this check, so this is not a guarantee of avoiding model setup. Evidence: SRC-1, `crates/semquery/src/engine.rs`, `crates/semquery-synth/src/synthesizer.rs`; [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation).

Failures propagate outward rather than being assigned to a recovery agent. The synthesizer task forwards an `ask_internal` error:

> if let Err(e) = this.ask_internal(&query, &tx).await {
>         let _ = tx.send(Err(e)).await;
>       }
> --- `crates/semquery-synth/src/synthesizer.rs`

The CLI's `match event?` returns early on an error. In text mode some tokens may already have been printed before a later inference failure; there is no display rollback in `run_ask`. The inspected functions do not implement automatic retry, alternate-model recovery, answer checkpoints or resume. Recovery requires another caller invocation; a fresh call repeats retrieval/generation rather than resuming a durable job. This is a bounded finding about these functions, not all downstream hosts. Receiver closure stops forwarding at checked boundaries, but ignored token-send failures do not establish interruption of active inference; the callback distinction is retained in [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation). Evidence: SRC-1, `crates/semquery/src/main.rs`, `crates/semquery/src/engine.rs`, `crates/semquery-synth/src/synthesizer.rs`.

### What counts as delivered

There are two distinct delivery surfaces. Text mode prints and flushes each token delta, then prints source metadata if a terminal answer supplies it. It does not replace already printed deltas with the full terminal text. JSON mode withholds token printing and serializes the terminal Answer when present. If the stream ends without a terminal answer and without an error, the CLI instead serializes buffered deltas with empty citations:

> None => {
>         print_json(&Answer {
>           text: buffered_text,
>           citations: Vec::new(),
>         });
>       }
> --- `crates/semquery/src/main.rs`

This fallback is not proof that such a stream ending occurred. It differs from nonstreaming `Engine::ask`, which explicitly rejects a missing terminal answer:

> answer.ok_or_else(|| SynthError::Other("ask stream ended without AnswerComplete".into()).into())
> --- `crates/semquery/src/engine.rs`

Thus successful stream completion and a complete text-mode display are different claims: token delivery has runtime-dependent limits, while the terminal Answer holds the full returned string. Neither surface adds a factual acceptance gate. No subsequent user acceptance is required by these functions, and this path does not save answers as knowledge for future questions. The persistent resource is the indexed corpus, not the completed reasoning episode. Evidence: SRC-1, `crates/semquery/src/main.rs`, `crates/semquery/src/engine.rs`; [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation). Actual delivery, use of the answer and benefits remain unobserved.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation)

Workflow role: terminal synthesis stage of the selected `semq ask` workflow, not a worker delegation. Inputs cross from retrieval as five selected hits; generation returns tokens and a terminal Answer. Verification is marker membership/deduplication, not factual admission. The CLI distinguishes immediate text display from terminal JSON serialization and has a no-terminal-event buffered fallback; `Engine::ask` instead requires `AnswerComplete`. Recovery is caller-driven reinvocation after propagated errors, not a code-owned revision round. No human per-answer veto or reference-answer oracle appears on this inspected path.

#### On [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search)

Workflow role: evidence-selection handoff before synthesis. Computational ranking selects the candidate passages; the foreground user supplies the question rather than approving each result. Empty hits terminate with an empty answer; retrieval errors propagate rather than authorizing unsupported generation. A successful hit handoff establishes selected material, not its untruncated arrival at inference or its use in a faithful answer.
