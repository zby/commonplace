---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "LLM Wiki v2 workflow: classic text filing through persistent notes to a later question, including structural rejection and partial-success recovery."
run-id: AAS-2026-11-08-llm-wiki-v2-5abff9a6c5c3-01
reviewed-boundary: "e0a205afe60bd1913d083a3ed4cdab81e38e4c26"
---

# LLM Wiki v2 workflow report

## Workflow account

### Selection and evidence boundary

This account selects one ordinary lifecycle: a caller files a text through `Wiki.ingest` using classic steps, then a caller asks a later question through `Wiki.ask` against the same bundle. It is representative because it crosses the system's central durable handoff: the Librarian writes knowledge that a fresh Researcher later selects. It is not a claim that ingest automatically triggers a question. These are two caller-triggered invocations connected by retained state, not a fabricated single agent conversation. The route identities already belong to [RT-RTE-source-filing](runtime.md#rt-rte-source-filing) and [RT-RTE-question-answer](runtime.md#rt-rte-question-answer).

The evidence is SRC-1 implementation and shipped instructions at the revision in [boundary](boundary.md). No target execution or model call was performed. The trace establishes code-controlled progression, not successful execution, factual preservation or answer quality. This member directly inspected `src/llmw2/agents/librarian.py`, `src/llmw2/agents/researcher.py`, `src/llmw2/agents/steps.py` checks, `src/llmw2/agents/steps_classic.py` selection/answer, and `src/llmw2/wiki.py` entry, filing and ask paths. These extend detail within the already registered SRC-1; the evidence layer is implementation. Persistence guarantees and other modes remain bounded by the runtime's account, not independently established run evidence.

### 1. Caller supplies a source; Python owns progression

The caller supplies text and optional title, resource, origin and fields. `Wiki.ingest` packages those into a Source. Preparation and filing are separate phases: preparation summarizes without reading the tree; filing acquires the bundle lock and works against current state. For supplied origins, the locked phase rechecks whether another writer has already filed the same version/content. That path returns an unchanged result rather than repeating admission (SRC-1 `src/llmw2/wiki.py`; [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)).

The Librarian is a pipeline coordinator, not a principal that invents arbitrary subtasks or tools. Its own source describes the handoffs:

> summarize → route → match → consolidate → merge | (name_folder →) write → relate → link
> --- `src/llmw2/agents/librarian.py`

A `Prepared` value carries the Source, Candidate, preparation usage and decision trace into filing. The Candidate carries the summarized note material and decision state; the original Source remains available for provenance and merge. Model requests receive rendered task context, not an inherited autonomous worker session. The runtime's [RT-BAP-model-instructions](runtime.md#rt-bap-model-instructions) establishes the prompt channel; that channel requests behavior rather than enforcing semantic correctness (SRC-1 `src/llmw2/agents/librarian.py`, `src/llmw2/agents/steps.py`).

### 2. Checked semantic decisions choose merge or creation

Under the caller-held lock, `Librarian.file` reloads the tree, asks routing to choose a folder/candidate set, excludes notes with conflicting fields, asks matching to choose a note, and asks consolidation whether to merge. A non-null match alone is insufficient: consolidation must also accept. Merge receives the matched note and incoming source; otherwise code creates the route's folders or asks for a new folder name, then writes the Candidate as a new note (SRC-1 `src/llmw2/agents/librarian.py`; [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)).

The model supplies semantic choices and prose; Python owns structural acceptance and filesystem effects. Checks reject a route outside the loaded tree, excessive creation depth, invalid names, a match outside its offered pool, or a non-boolean consolidation result. Candidate/draft checks require the expected data type, a nonempty title, string tags and serializable fields. These are not tests of factual entailment. For example:

> if match is not None and not any(match is n for n in pool):
>     raise StepError("match", "must return None or one of the notes it was given")
> --- `src/llmw2/agents/steps.py`

There is no per-note human approval stage in this ordinary route, and no expected-answer oracle. Starting ingest supplies the source; it does not establish that a human approved each generated sentence. The source-faithfulness goals remain [RT-CLM-factual-preservation](runtime.md#rt-clm-factual-preservation), not a semantic acceptance invariant.

### 3. Durable admission precedes optional enrichment

On merge, code checks that the existing note has not changed before updating it. On either branch, it saves the raw source and constructs its reference immediately before writing the note. The reference includes the source content hash and step provenance. Note admission therefore precedes related-link enrichment. Related candidates come from the routing pool and destination folder; checked related results are capped, code links them, then appends the operation log. The returned IngestResult carries action, note/title/folder, created folders, related paths, decisions and usage (SRC-1 `src/llmw2/agents/librarian.py`; [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)).

Delivery at this phase means a returned filing result after those code steps, not independently verified factual preservation. There is no single multi-file transaction covering raw, note, indexes, links and log; the runtime's writer-control account bounds cooperating locks and individual file replacement (SRC-1 `src/llmw2/wiki.py`, `src/llmw2/bundle/store.py`; [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)).

### 4. A later request reconstructs context from retained notes

A subsequent nonempty question starts a fresh Researcher and loads the current tree. Optional `where` fields filter it before selection; they are not access control. Classic selection navigates folder by folder, supplying the question, visited folders, current description, child-folder listings, note summaries and summaries of already selected notes. Code bounds visited steps and selected notes and ignores model-selected paths that are not in the current folder's note mapping. A model's `done` stops navigation only when something has been selected (SRC-1 `src/llmw2/wiki.py`, `src/llmw2/agents/researcher.py`, `src/llmw2/agents/steps_classic.py`; [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)).

The answering call is a separate context handoff, not the entire navigation transcript:

> notes="\n\n".join(f"### {n.rel}\n\n{n.full_text()}" for n in notes),
> --- `src/llmw2/agents/steps_classic.py`

Only selected full notes enter that argument. Python must load and insert retained text; a path in a prompt is not an automatically followed reference. Spreadsheet rows can be loaded into temporary note copies when selected notes cite sheet sources. The Researcher also contains classifier-dependent historical/conflict branches, but they are not necessary to this classic trace. Their presence must not be mistaken for universal classic verification or adjudication (SRC-1 `src/llmw2/agents/researcher.py`; [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)).

### 5. Answer delivery checks membership, not truth

`check_select` rejects notes outside the supplied tree. If no notes survive, Researcher returns its fixed no-relevant-notes message without an answering call. Otherwise the answer check only requires a string. Researcher parses bracketed citation paths and intersects them with delivered note paths; it returns text, selected paths, filtered citations, cited titles, decisions and usage. This is the terminal result for the library workflow. It does not retain the answer as new knowledge or require an internal human approval before returning it (SRC-1 `src/llmw2/agents/researcher.py`, `src/llmw2/agents/steps.py`; [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)).

A filtered citation list does not remove unsupported assertions or invalid citation strings from answer text. No inspected step compares the answer with a known correct reference. Thus delivered means returned to the caller, not accepted as true by an oracle or demonstrated useful in operation.

### Rejection and recovery across the handoffs

The failure boundary depends on when failure occurs. A hosted writer's invalid summary or merge normally propagates; an Ollama local writer can substitute source text for a failed summary or append incoming material when merge fails. Those code fallbacks trade generated consolidation for preservation-oriented continuation; they do not prove successful preservation. A stale merge target can be rejected before overwriting it. On a filing exception Wiki forgets its cached tree and rethrows; that refresh is not filesystem rollback (SRC-1 `src/llmw2/agents/librarian.py`, `src/llmw2/wiki.py`; [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)).

A concrete partial-success path occurs after note admission: relating ModelError is caught and produces no related links, while the note remains written and filing continues to log/result. The minimum passage is already retained in [RT-RTE-source-filing](runtime.md#rt-rte-source-filing). This is code-owned recovery from optional enrichment failure, not a second agent rejecting and repairing the note. Errors outside that catch can still leave partial effects. Retrying is caller-owned; the source does not establish universal automatic restart or all-or-nothing recovery.

For the later read, empty selection yields a bounded no-answer result rather than a repair loop. Other selection/answer failures are not converted here into independently verified answers. Consequently this workflow coordinates multiple model decisions and durable handoffs, but supplies neither an autonomous critic-author cycle nor evidence of reliable end-to-end operation (SRC-1 `src/llmw2/agents/researcher.py`, `src/llmw2/agents/steps.py`).

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

#### On [RT-RTE-source-filing](runtime.md#rt-rte-source-filing)

Workflow role: first durable handoff. Prepared transfers source, Candidate, usage and decisions from tree-independent preparation to locked admission. Code, not the semantic model, owns the transition to persistence and optional relating. The post-write relating failure path permits a delivered filing result without links; it does not undo note admission. Recovery ownership changes from code's local fallbacks/cache invalidation to the caller's retry when an error propagates.

#### On [RT-RTE-question-answer](runtime.md#rt-rte-question-answer)

Workflow role: later consumer and terminal delivery. A separate caller request reconstructs a bounded selection context, then passes selected full notes to answering. No automatic ingest-to-question trigger is implied. Returned answer and citation metadata complete the read request without re-admitting the answer to the store or establishing semantic acceptance.
