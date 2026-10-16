---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Eigenius workflow: notebook prose formalization through asynchronous model-assisted encoding, artifact delivery and optional validated load."
run-id: AAS-2026-10-15-eigenius-fe68ed89519b-01
reviewed-boundary: "836498ebd99733067d45aa6f7b09d4ff5035dd99"
---

# Eigenius workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is running a notebook formalization cell, obtaining its generated ESL artifact, and optionally loading that artifact into the serving branch. It was selected because one shipped caller connects request, asynchronous work, model decisions, result retrieval and admission. This is a model-assisted knowledge workflow, not evidence of an autonomous multi-agent team. The notebook and kernel delegate computation; an external agent's planning and choice to trust the result are not established. The [boundary](boundary.md) remains a complete artifact with a partial operational loop.

All source evidence is SRC-1 at the frozen revision. This account combines direct implementation inspection with the supplied runtime records. No target code was executed, and no observed run or causal experiment was supplied. Thus the traced connections establish wiring, not a successful end-to-end delivery or improved scientific reliability.

### Request and task handoff

The notebook trims the cell's prose and rejects an empty input before dispatch. It chooses the cell's explicit document ID or its cell ID, requests `text/x-esl`, and passes the lexicon profile. This request initiates [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize); it does not itself approve any generated content. The initiating principal's human or automated identity is not established by the call (SRC-1, `notebooks/src/runtime/notebookStore.ts`).

The kernel resolves the request's layer and scope and passes an explicit formalization request, the read layer and persistent backend to the injected formalizer. It first persists a task identified by UUID, document ID, source hash and layer. A blocking worker owns progression after dispatch; the immediate response carries the task ID and document-branch name. This is a task/result handoff, not a model conversation transferred to another agent. The models later receive seam-specific decision prompts, not the notebook operator's whole conversation. The runtime record supplies the prompt and state boundaries and the initial persistence precondition (SRC-1, `kernel/src/server/formalize.rs`; [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize)).

### Encoding decisions and their verification limits

The formalizer reads the prior document branch before rebuilding glossary state, obtains replay/live decision arms, runs parsing and discourse resolution, emits a resource artifact and commits recorded live draws. These recordings can influence a subsequent request, but a reused document ID does not guarantee matching questions or eliminate provider calls. Replay selection and its miss cases belong to [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize), rather than a notebook-level retry guarantee (SRC-1, `crates/eigenius-encoding/src/formalize.rs`).

Within encoding, parser code constructs candidates; the ranker or replay arm chooses among presented alternatives. Code can refuse indistinguishable presentations and invalid selections. A sole surviving candidate need not invoke a selector. The served emitter supplies no human skeleton pin. Selection membership is not an answer oracle for authorial meaning: the ranker cannot choose candidates omitted from its presentation, and type-compatible readings can still misinterpret prose. These decision and veto boundaries are supported by [RT-RTE-reading-selection](runtime.md#rt-rte-reading-selection), including its source passage distinguishing selection from a kernel semantic veto (SRC-1, `kernel/src/dcg/reading_ranker.rs`, `kernel/src/dcg/parse/resolve.rs`).

Emission uses `partial: !req.strict`: strict requests can fail at an unencodable unit, while partial requests can return an artifact with explicit cuts. The notebook's successful result therefore includes encoded and cut counts, not a certificate of complete faithful translation. Recorded decisions are retained without mandatory per-content human approval. This is an open document request, not an improvement curriculum or a criticism-and-revision loop established by this workflow (SRC-1, `crates/eigenius-encoding/src/formalize.rs`; [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize)).

### Result delivery and failure ownership

The worker turns a returned formalizer error into a stored result with an error string and marks the task Failed; an ordinary success stores artifact bytes, counts and structure identity and marks it Completed. Serialization, result storage and terminal task updates discard their errors. A returned computation is consequently not guaranteed to become a retrievable terminal task. The runtime record retains the decisive ignored-write passage (SRC-1, `kernel/src/server/formalize.rs`; [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize)).

The notebook polls at three-second intervals and stops on Completed, Failed or Cancelled. It then fetches the result, rejects `found: false`, and surfaces any result error before decoding the artifact. After thirty minutes it returns a client error explaining that the server task may still be running. This deadline is not cancellation or recovery of the worker. The inspected caller contains no automatic repair-and-resubmit loop; resubmission and any change to prose or settings remain caller responsibilities at this boundary. Server crash recovery and cancellation enforcement were not established (SRC-1, `notebooks/src/runtime/notebookStore.ts`).

> `formalization task ${started.taskId} did not finish within 30 minutes — ` +
> `it may still be running; check the Tasks panel`,
> --- `notebooks/src/runtime/notebookStore.ts`

Without `land`, delivery at this caller boundary is a formalize-cell output containing the artifact, structure IRI, encoded/cut counts, committed-draw count and document branch. Its separate artifact identity and result-metadata substrate are [RT-OBJ-formalization-artifact](runtime.md#rt-obj-formalization-artifact). Output delivery neither asserts the artifact into the serving chain nor proves the operator read it (SRC-1, `notebooks/src/runtime/notebookStore.ts`).

### Optional admission and rejection path

With `cell.land`, the notebook immediately calls Load on the artifact with ESL content type and auto-commit enabled. There is no intervening mandatory human inspection. Load admission, including structural, retroactive and applicable institution phases, is the separate [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission). The caller proposes the artifact; code and applicable institutions can reject it. This gate checks admission under those mechanisms, not scientific truth or faithful translation (SRC-1, `notebooks/src/runtime/notebookStore.ts`, `kernel/src/server/load.rs`).

The SDK is a consequential intermediary: `load` wraps the kernel response in an Outcome whose discriminant follows the response's `success` field. The notebook checks `outcome.ok` before reading the layer ID. Thus an RPC that returns normally but refuses content is not presented as successful landing. On this rejection path the notebook returns an error rather than a formalize-cell success; the generated artifact/result and document recordings are separate from serving-chain admission. No automatic model revision follows the rejection in this inspected caller. Commit recovery belongs to the admission machinery, while choosing a corrected request remains with the caller; this does not establish rollback of every earlier formalization write (SRC-1, `clients/eigenius-ts/src/client.ts`, `notebooks/src/runtime/notebookStore.ts`; [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission)).

> if (response.success) return { ok: true, value: response };
> --- `clients/eigenius-ts/src/client.ts`

> if (!outcome.ok) {
>   return {
>     kind: "error",
>     message: `the artifact failed to land:\n${outcome.message}`,
>   };
> }
> --- `notebooks/src/runtime/notebookStore.ts`

On accepted Load, the notebook adds returned layer ID and resource count to its output. This is the caller's landing criterion. It does not independently inspect branch advancement or certify a new layer was created on every rerun; the admission record distinguishes those outcomes. Generation, client-visible delivery and serving-chain admission are therefore three different milestones, each with a distinct failure surface.

### Added inspection coverage

Direct reads covered the formalization-cell dispatch in SRC-1, `notebooks/src/runtime/notebookStore.ts`; task dispatch and result retrieval in `kernel/src/server/formalize.rs`; served emission and draw commitment in `crates/eigenius-encoding/src/formalize.rs`; and Outcome conversion plus Load construction in `clients/eigenius-ts/src/client.ts`. These are implementation evidence. Source comments were not treated as observed operation: in particular, the notebook comment promising fast, deterministic, free replay is bounded by the runtime record's keyed replay/miss analysis. This selective workflow does not establish the uninspected maintenance and evaluation responsibilities listed in the boundary.

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

#### On [RT-RTE-document-formalize](runtime.md#rt-rte-document-formalize)

Workflow completion criterion: the notebook requires a terminal task status followed by a found, error-free result before returning its formalize-cell payload. Timeout stops client waiting, not server work. Failed/Cancelled status still leads to result retrieval so that a stored error can be surfaced. The inspected caller does not itself revise failed content or resubmit it; server recovery beyond returned failures remains uninspected. Source evidence and the terminal-write limitation are retained in the workflow account and the supplied record.

#### On [RT-RTE-resource-admission](runtime.md#rt-rte-resource-admission)

Workflow rejection propagation: SDK Outcome conversion makes a kernel response with `success: false` into `ok: false`; the notebook checks that discriminant before consuming landing fields. The workflow account supplies the additional SDK evidence. Optional landing can occur in the same run without human review. An accepted response supplies the notebook's landed metadata, while a refusal returns an error; neither outcome establishes a content-revision loop or reverses already retained formalization decisions.
