---
type: types/agent-memory-analysis-report.md
description: "PageIndex local-mode memory boundary: a per-document tree and page-text store that grows by submission and shrinks by deletion, never changes through querying, and is read by model-called tools plus one doc_id-keyed metadata push"
run-id: AAS-2026-09-29-pageindex-02
source-identity: "https://github.com/VectifyAI/PageIndex"
reviewed-boundary: "d2693d80791a86345ef78b3234834f5fe53a70a0"
report-status: complete
memory-comparison:
  scope: "The local-mode document store (tree.json, pages.json, doc.json and manifest.json under storage_path) that indexing writes and the chat tools read, with its write routes, its read-back routes and the CLI classic-run log. Excluded: PageIndex Cloud storage, host-runtime loops and memory, caller-held conversation transcripts, the provider prompt cache, and static instruction text. The store accumulates through use in one sense only: each submit_document call adds a retained document directory and each delete_document call removes one (RT-RTE-1, MEM-ABS-1). Querying (chat, tool calls, citation resolution) writes nothing back, and no stored document is edited or revised after it is written. Accumulation is by submission, not by learning from queries."
  axes:
    storage_substrate:
      assessment: known
      values: ["files"]
      evidence:
        files:
          basis: wired
          records: ["RT-OBJ-1", "RT-OBJ-2", "RT-OBJ-3", "MEM-OBJ-1"]
          note: "Every scoped retained object is JSON on disk: three files per document, a manifest cache and the CLI log. There is no database, vector store or in-memory retained state."
      records: ["RT-OBJ-1", "RT-OBJ-2", "RT-OBJ-3", "MEM-OBJ-1"]
      note: "Complete within the scope. Cloud-side storage (which may be a service object) is excluded and unexamined, so no conclusion covers cloud mode."
    representational_form:
      assessment: known
      values: ["natural-language", "symbolic"]
      evidence:
        natural-language:
          basis: wired
          records: ["RT-OBJ-1", "RT-OBJ-2", "RT-OBJ-3"]
          note: "Node titles and summaries, the page text and the document description are natural language delivered to the chat model."
        symbolic:
          basis: wired
          records: ["RT-OBJ-1"]
          note: "Node ids and start and end page indexes are symbolic fields that code uses to slice page text and to check page bounds at write time. The model also sees them as text, so the symbolic role is limited to those code consumers."
      records: ["RT-OBJ-1", "RT-OBJ-2", "RT-OBJ-3"]
      note: "No parametric object is retained by PageIndex; model weights are provider-side and outside the scope."
    lineage:
      assessment: known
      values: ["imported", "other-compiled", "authored"]
      evidence:
        imported:
          basis: wired
          records: ["RT-OBJ-2"]
          note: "Page text is PyPDF2 extraction of the source PDF with surrogates replaced, stored without summarization."
        other-compiled:
          basis: wired
          records: ["RT-OBJ-1", "RT-OBJ-3", "RT-RTE-1"]
          note: "The tree structure, node summaries and document description are derived from the PDF by layout statistics and model calls at indexing time."
        authored:
          basis: wired
          records: ["RT-OBJ-3"]
          note: "The optional metadata dict passed to submit_document is stored as given and shown to the model. Nothing shows who wrote it, so authored means caller-supplied."
      records: ["RT-OBJ-1", "RT-OBJ-2", "RT-OBJ-3", "RT-RTE-1"]
      note: "No value is trace-extracted: the only trace file (MEM-OBJ-1) has no reader."
    behavioral_authority:
      assessment: known
      values: ["knowledge"]
      evidence:
        knowledge:
          basis: wired
          records: ["RT-BAP-2", "RT-RTE-2"]
          note: "Stored outline, summaries, page text and description reach the chat model as tool results or as the targeting message. The consumer paths deliver them as data the model may use or ignore."
      records: ["RT-BAP-2", "RT-RTE-2", "MEM-RTE-1"]
      note: "Routing and ranking are not values: the outline guides the model, but no code selects or orders content from it (RT-RTE-2). The agent instructions and tool descriptions are static instruction text and outside the memory scope."
    write_agency:
      assessment: known
      values: ["automatic", "manual"]
      evidence:
        automatic:
          basis: wired
          records: ["RT-RTE-1"]
          note: "submit_document runs extraction, summarization and store writing without per-object human input. A human-triggered automatic extraction remains automatic."
        manual:
          basis: wired
          records: ["RT-OBJ-3"]
          note: "Only the caller-supplied metadata field is entered by hand. No route lets a caller edit the tree, summaries or pages after storing."
      records: ["RT-RTE-1", "RT-OBJ-3", "RT-ABS-1"]
      note: "Complete within the scope. Editing the plain JSON files outside PageIndex is possible but is not a shipped route."
    curation_operations:
      assessment: absent
      values: []
      evidence: {}
      records: ["MEM-ABS-1", "RT-ABS-1"]
      note: "No consolidate, decay, dedup, evolve, invalidate, promote or synthesize operation runs over stored documents (MEM-ABS-1). Index-time merge and expand act on a tree before it is stored, deletion keeps no history, and name suffixing is only a collision check."
    read_back_direction:
      assessment: known
      values: ["pull", "push"]
      evidence:
        pull:
          basis: wired
          records: ["RT-RTE-2", "RT-RTE-4"]
          note: "The chat model calls browse_documents, get_document, get_document_structure and get_page_content; host adapters expose the same tools."
        push:
          basis: wired
          records: ["MEM-RTE-1"]
          note: "When a chat call supplies doc_id, code prepends the named documents' metadata rows as the first user message without a model request."
      records: ["RT-RTE-2", "RT-RTE-4", "MEM-RTE-1"]
      note: "Complete within the scope. Cloud own-model chat also uses the same targeting block on cloud documents, which this report does not scope."
    read_back_signal:
      assessment: known
      values: ["identifier"]
      evidence:
        identifier:
          basis: wired
          records: ["MEM-RTE-1"]
          note: "The caller's doc_id selects a metadata row through the store's id lookup, and the selected row is what is delivered. The push is only this route."
      records: ["MEM-RTE-1"]
      note: "The signal describes push selection only. The model's own choice of documents and pages in pull routes is inferred judgment by the model, not a push signal."
    trace_learning:
      assessment: known
      values: ["no"]
      evidence:
        "no":
          basis: wired
          records: ["RT-ABS-1", "MEM-ABS-1", "MEM-OBJ-1"]
          note: "The negative rests on bounded code searches (RT-ABS-1, MEM-ABS-1), not on a wired route. The only trace file is written by the CLI classic run and no code reads it."
      records: ["RT-ABS-1", "MEM-ABS-1", "MEM-OBJ-1"]
      note: "Within the frozen SDK and CLI code, no trace feeds any retained artifact. Cloud-side learning and host runtimes are outside the scope."
    trace_source:
      assessment: inapplicable
      values: []
      evidence: {}
      records: ["RT-ABS-1"]
      note: "Trace learning is known not to occur in scope."
    learning_scope:
      assessment: inapplicable
      values: []
      evidence: {}
      records: ["RT-ABS-1"]
      note: "Trace learning is known not to occur in scope."
    learning_timing:
      assessment: inapplicable
      values: []
      evidence: {}
      records: ["RT-ABS-1"]
      note: "Trace learning is known not to occur in scope."
    distilled_form:
      assessment: inapplicable
      values: []
      evidence: {}
      records: ["RT-ABS-1"]
      note: "Trace learning is known not to occur in scope."
    faithfulness_tested:
      assessment: absent
      values: []
      evidence: {}
      records: ["MEM-ABS-2"]
      note: "The frozen repository retains no execution evidence that tests answers' dependence on retrieved content. README accuracy figures come from benchmarks outside the frozen boundary."
---

# PageIndex memory analysis

## Boundary and evidence

**Subject.** PageIndex, the `pageindex` Python SDK at commit `d2693d80791a86345ef78b3234834f5fe53a70a0` (SRC-1 implementation, SRC-2 design prose, SRC-3 reported operation). This report analyses memory and context routes only and takes the runtime member `output/runtime.md` as provisional findings to check.

**Memory scope, chosen from the runtime member's routes.** The retained material is the local-mode document store: for each submitted PDF, `tree.json` (an outline of titled, summarized nodes with page ranges), `pages.json` (page text) and `doc.json` (name, model-written description, page count, caller metadata), plus a `manifest.json` cache. Indexing writes it once (RT-RTE-1, RT-RTE-3) and chat tools read it (RT-RTE-2, RT-RTE-4, RT-RTE-5). **Scope reading.** The memory type defines the scope as retained objects accumulated or changed through use. This report takes the reading that use includes submission: each `submit_document` call adds a retained document and `delete_document` removes one, so the store's content is accumulated through the system's use and the scope holds (RT-RTE-1). It does not accumulate through querying: no query, tool call or chat turn writes anything back, and a stored document is never edited (RT-ABS-1, MEM-ABS-1). Every statement below that nothing changes "through use" means through querying, and every statement about accumulation means by submission. The store is included because it is the only retained state the agent reads. The alternative reading, in which only query-time writes count, would make the boundary empty; it is not adopted, and Integration issues item 1 records the choice.

**Included surfaces.** The store and its access structures (RT-OBJ-1, RT-OBJ-2, RT-OBJ-3), its write routes (RT-RTE-1, RT-RTE-3), its read routes (RT-RTE-2, RT-RTE-4, RT-RTE-5, MEM-RTE-1), and the CLI classic-run log (MEM-OBJ-1).

**Excluded surfaces and the conclusion each prevents.**

- PageIndex Cloud storage and served instructions (RT-RTE-6, RT-BAP-4): prevents any conclusion about cloud-side memory, retrieval or learning.
- Host runtimes behind the adapters (RT-RTE-4): prevents attributing session memory or approval behavior to PageIndex.
- The caller-held conversation history (RT-RTE-5): it is passed in and returned by the caller, and PageIndex retains none of it, so it is not scoped memory.
- The provider prompt cache and model weights (RT-CMP-1, RT-CMP-2): provider-side and uninspected.
- Static instruction text and tool descriptions (RT-OBJ-4): system-definition text, not retained material.
- The Markdown pipeline (RT-RTE-7): writes a user-named result file that no shipped route reads, so it establishes no read-back route.

**Inspected paths (SRC-1, commit-addressed blobs).** `pageindex/local_store.py`, `pageindex/local_api.py`, `pageindex/agent_tools.py`, `pageindex/client.py`, `pageindex/utils.py`, `pageindex/page_index_classic.py`, `run_pageindex.py`, and a repository-wide search of `pageindex/` and the file list for writers, session, memory and ablation terms. SRC-2 `README.md` for the memory-relevant claims.

**Evidence layers and limits.** Implementation only, read statically at the frozen commit. No test or indexing run was executed, so every operation conclusion is `uninspected` and no value is `observed`. Cloud client code was not re-traced.

## Core ideas

**1. The retained store is a per-document index built once per document; submission adds to it and querying never changes it.** Indexing writes the tree, page text and metadata in one call. The call stores the tree with node text removed and the page text separately:

> doc_id, meta, remove_fields(structure, fields=["text"]), pages)
> --- `pageindex/local_api.py:173-173` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

The store exposes only `save_document`, `delete_document` and readers, and `submit_document` is the only writer in the SDK path (MEM-ABS-1, RT-ABS-1). The store therefore grows by one directory per submitted document and shrinks by one per deletion, and a changed document is a deleted and resubmitted one with a new id. So the store is a retained document index accumulated by submission, not an experience memory, and PageIndex has no trace-fed learning route (MEM-ABS-1).

**2. Context selection is model navigation over an outline, with a size budget.** The tools return the outline with summaries but without node text, then page text on request. The structure tool strips only text:

> """Drop node text and normalize key order, recursively."""
> --- `pageindex/agent_tools.py:654-654` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

So the outline and its model-written summaries reach the model whole (split into parts when large), and the model chooses which pages to read. Page reads stop at a character budget derived from a 100,000-character tool limit:

> _CHAR_BUDGET = int(TOOL_RESPONSE_CHAR_LIMIT * 0.95)
> --- `pageindex/agent_tools.py:42-42` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

There is no ranking in local mode: discovery lists documents newest first and the source tells the model to match names and descriptions itself:

> Retry without sort/query and match the returned names and descriptions against the intent yourself
> --- `pageindex/agent_tools.py:745-745` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

Consumers, budgets and the pull route are annotated on RT-RTE-2.

**3. The one automatic supply is a document-metadata message keyed by the caller's `doc_id`.** When a chat call passes `doc_id`, code fetches the named documents' metadata rows and places them in the first user message before the model's first turn. The source says the block is conversation content, not system prompt:

> Conversation content, never system prompt: the chat
>     lanes prepend it as the first user message
> --- `pageindex/agent_tools.py:1698-1699` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

The row content includes the model-written description and any caller metadata, serialized whole:

> f"Document metadata: {json.dumps(details[0], ensure_ascii=False)}\n"
> --- `pageindex/agent_tools.py:1725-1725` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

This is a push route selected by an identifier the caller supplies (MEM-RTE-1). It is the only place retained material enters context without a model tool request.

**4. Source trust.** Retained content has three origins: verbatim page text (RT-OBJ-2), model-written summaries and description (RT-OBJ-1, RT-OBJ-3), and caller-supplied metadata (RT-OBJ-3). All three reach the model in JSON fields with no delimiter framing or redaction at query time (RT-ABS-3), and the description and metadata enter as user-role message content. The classic indexing prompts use delimiters and redaction, but the read side does not. Whether a model follows instructions inside these fields is not established here.

**5. Editing and adoption surface.** There is no edit or revision surface for stored content. Removal exists as `remove_document`, which the source labels destructive and irreversible:

> "Permanently delete documents and all associated data. Only invoke "
>             "when the user explicitly names the documents AND confirms "
>             "deletion.
> --- `pageindex/agent_tools.py:272-274` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

The tool is registered only when a host passes `include_management=True` (RT-RTE-4), and the chat lanes never do (Guarantee B in `output/runtime.md`). Deletion removes the directory, so no history is kept and no invalidation step exists.

**6. Curiosity pass.**

- *README label "full context: conversation history".* The README table row claims PageIndex retrieval uses conversation history (MEM-CLM-1):

> | **Context** | query embedding only | full context: conversation history, domain knowledge, etc. |
> --- `README.md:69-69` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

  The code supports a narrower reading. History is the caller's message list, passed to the chat model as its transcript; the tree index and store take no part in it, and PageIndex keeps no conversation store (RT-RTE-2, RT-RTE-5). The claim stays `claimed`.
- *"Index" names two parts.* The tree in `tree.json` is the only routing aid, and `pages.json` is the content store the model actually reads. Retrieval quality depends on the model reading the outline, which this pass did not test (RT-RTE-2).
- *Trace file.* A raw index-time trace exists but is written only by the CLI classic run and has no reader (MEM-OBJ-1). The runtime member's RT-ABS-1 writer search names `open(..., "w")` and `json.dump`; this writer sits inside that search and does not change its conclusion, but the runtime member does not mention it.
- *Caller `metadata` is retained input.* The runtime member lists it in RT-OBJ-3 without noting it is caller-supplied and shown to the model (annotated on RT-OBJ-3).

## Shared records

### Components

none

### Operative objects

#### MEM-OBJ-1 — CLI classic-run log
- **Source-native identity.** `logs/<pdf-name>_<timestamp>.json`, written by `JsonLogger` in `pageindex/utils.py` for the standard pipeline when `run_pageindex.py` calls `page_index_main` without a logger. SRC-1 `pageindex/utils.py`, `run_pageindex.py`, `pageindex/page_index_classic.py`.
- **Form and substrate.** Raw trace: JSON list of model-call responses and pipeline messages, natural language and symbolic mixed, on disk. The SDK path passes a standard-library logger instead, so this file is not written there (`pageindex/local_api.py`).
- **Lineage.** Trace of an index-time run; not derived memory.
- **Consumers and authority.** None: no code in `pageindex/` or the CLI opens a log file. Authority: none.
- **Evidence.** The log directory is created by the logger:

> os.makedirs("./logs", exist_ok=True)
> --- `pageindex/utils.py:440-440` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

  The CLI's standard branch calls the pipeline with no logger, so this default applies:

> toc_with_page_number = page_index_main(args.pdf_path, opt)
> --- `run_pageindex.py:141-141` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

  Implementation conclusion status: `wired` for the write. Operation conclusion status: `uninspected`.
- **Limits.** Search covered `pageindex/` and `run_pageindex.py` for readers of `logs`; the file may be read by a human or external tool, which is outside the boundary.

### Routes

#### MEM-RTE-1 — Document-targeting metadata push
- **Trigger.** A `chat`, `chat_completions` or protocol-lane call with `doc_id` set. SRC-1 `pageindex/agent_tools.py` (`targeting_block`, `doc_targeting_block`), `pageindex/local_chat.py` (three lane prologues).
- **Selector and selector input.** Code, not the model. The input is the caller-supplied `doc_id` (a string or list); each id is resolved through `client.get_document`, which returns the stored metadata row for that id or raises when not found.
- **Retained input.** The `doc.json` fields `id`, `name`, `description`, `status`, `createdAt`, `pageNum`, `folderId` and caller `metadata` (RT-OBJ-3). The `description` is model-written; `metadata` is caller-supplied.
- **Persistence.** Nothing new is stored. The message is rebuilt per call from the store.
- **Delivery.** First user-role message of the conversation, with a fixed directive to retrieve content with `get_document_structure()` and `get_page_content()`. Selected part: the whole metadata row per named document, with no size budget applied here.
- **Later consumer.** The chat model in RT-RTE-2 and its protocol variants (RT-RTE-5).
- **Authority at the consumer.** Advisory content in a user message; the model chooses its next tool calls.
- **Scope link.** With `doc_id` set on a local client, the same ids also restrict the tools' document lookups (Guarantee A in `output/runtime.md`). That restriction is scoping, not selection of delivered content.
- **Implementation conclusion status:** `wired`. **Operation conclusion status:** `uninspected`.
- **Evidence limits.** Whether the model uses the metadata is unobserved. On a cloud client the same block is built from cloud documents, outside the scope. Possible overlap with the context description in RT-RTE-2 (Integration issues).

### Claims

#### MEM-CLM-1 — Retrieval uses conversation history
- **Claimed operation.** The README comparison table says PageIndex uses "full context: conversation history, domain knowledge, etc." where vector RAG uses the query embedding only. SRC-2 `README.md`. Conclusion status: `claimed`. Implementation support is limited to the caller's history reaching the chat model as its transcript (RT-RTE-2).

### Evidenced absences

#### MEM-ABS-1 — No curation or write-back operation over stored documents
- **Searched boundary.** SRC-1 `pageindex/`, all `.py` files at the frozen commit: every use of the `DocStore` methods (`save_document`, `delete_document`, `list_metas`, `get_meta`, `get_tree`, `get_pages`) and every writer call (`json.dump`, `open` in write mode, `write_text`). Also searched for `sqlite`, `pickle`, `shelve`, `memory`, `remember` and `session` outside `pageindex/flash/`; hits are the store's atomic writer, CLI result files, the classic-run log, cloud MCP session ids and docstrings on the caller's transcript.
- **Conclusion status:** `absent`.
- **Conclusion supported.** The only store writes are `save_document` (called once, from `submit_document`) and `delete_document`. No route consolidates, decays, deduplicates, evolves, invalidates, promotes or synthesizes stored documents. Name suffixing (`_1` to `_99`) is a collision check on new submissions, and deletion removes the directory without history. No trace feeds a retained artifact.
- **Conclusion prevented.** Nothing about cloud-side behavior, host runtimes, provider learning or manual edits of the JSON files. Commit history of the repository was not examined.

#### MEM-ABS-2 — No retained evidence that answers depend on retrieved content
- **Searched boundary.** SRC-1 `tests/`, `cookbook/`, `examples/` and SRC-2 `README.md` at the frozen commit, searched for ablation, faithfulness, closed-book and counterfactual comparisons. The only hits are unrelated (a rubric word in a cookbook notebook, and an unrelated test docstring).
- **Conclusion status:** `absent`.
- **Conclusion supported.** The frozen repository contains no run record or test that removes or alters retrieved content and compares answers. The test suite stubs the model and was not executed.
- **Conclusion prevented.** The external benchmarks in SRC-3 are not frozen, so this says nothing about whether they test dependence on retrieved content.

### Behavioral-authority paths

none

### Annotations of runtime records

#### On RT-OBJ-1 — Tree index (`tree.json`)
- **Storage and form.** JSON file on disk. Titles and summaries are natural language; ids and page ranges are symbolic fields that code uses to slice page text and check bounds. Node text is removed before saving (see the save site quoted in Core ideas).
- **Lineage.** Other-compiled from the PDF by layout statistics and model calls (RT-RTE-1, RT-RTE-3).
- **Consumers and authority.** The structure tool returns it minus node text, summaries included; the model uses it to choose pages. Authority: advisory (RT-BAP-2).
- **Limits.** Not changed after storing. A re-index produces a new document id.

#### On RT-OBJ-2 — Page text store (`pages.json`)
- **Storage and form.** JSON file; natural language.
- **Lineage.** Imported: PyPDF2 extraction of the source PDF, stored without summarization. It differs from the parser that built the tree.
- **Consumers and authority.** `get_page_content` serves it by page number under the character budget quoted in Core ideas. Authority: advisory (RT-BAP-2).
- **Limits.** Text extraction quality is uninspected; scanned PDFs are refused in local mode (RT-RTE-1).

#### On RT-OBJ-3 — Document metadata and manifest (`doc.json`, `manifest.json`)
- **Storage and form.** JSON on disk. Mixed: symbolic fields plus a natural-language description.
- **Lineage.** Mixed. The description is model-written (other-compiled); the `metadata` dict is caller-supplied and stored as given (authored, in the sense of caller-supplied). The stored `metadata` field is the one part a caller can enter by hand:

> "metadata": metadata,
> --- `pageindex/local_api.py:169-169` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

- **Consumers and authority.** Listing tools show name, description and flattened metadata; the targeting message (MEM-RTE-1) serializes the whole row. Authority: advisory.
- **Limits.** The manifest is a cache rebuilt from `doc.json` files and carries no independent content.

#### On RT-RTE-1 — Flash indexing (default local)
- **Write agency.** Automatic after a human or program triggers `submit_document`. No trace is used as input.
- **Later read-back.** The tree, pages and metadata it stores are what every later read returns. It is the write route for all scoped objects, and it stores no history of indexing runs.
- **Limits.** Optimizer merge and expand act before storing and do not count as curation of retained memory (MEM-ABS-1).

#### On RT-RTE-2 — Own-model chat agent over local tools
- **Pull route.** The chat model calls `browse_documents` (name, description, status, created date, newest first, at most 50 per call), `get_document` (metadata), `get_document_structure` (outline with summaries, split into parts by the character budget) and `get_page_content` (page text under the budget, reporting omitted pages). Discovery is by the model matching names and descriptions; local mode refuses ranking. Consumer: the chat model. Delivery: tool results. Authority: advisory.
- **Requested versus supplied.** Everything in this route is a requested return, so it is pull. The automatic supply in the same conversation is MEM-RTE-1.
- **Limits.** Whether the model follows the reading workflow is unobserved; no model call was run.

#### On RT-RTE-4 — Host-framework tool adapters
- **Pull route.** The same four read tools are handed to a host model. The host owns the loop, transcript and any persistence, all outside the scope. Document scoping is not enforced on these public methods, so their content selection is the model's alone.
- **Limits.** `include_management=True` adds irreversible deletion, but no scoped retained content is added or edited by these tools.

#### On RT-RTE-5 — Responses and Messages protocol lanes
- **Read-back.** Read tools and the targeting message are the same as in RT-RTE-2 and MEM-RTE-1. The caller may append the returned provider transcript to the next call. The docstring calls this the agent's memory and the provider's cached prefix:

> A round-tripped transcript continues the
>         agent's memory and the provider's cached prefix
> --- `pageindex/client.py:1197-1198` @ `d2693d80791a86345ef78b3234834f5fe53a70a0`

- **Classification.** That transcript is caller-held session state passed back in as history. PageIndex writes and retains none of it, so it is not scoped memory and not a read-back route of the store.

#### On RT-ABS-1 — No write-back from use into the store or model parameters
- **Memory link.** Supports `trace_learning: "no"` and the inapplicable trace-learning axes. Bounded to the frozen SDK and CLI code. It agrees with MEM-ABS-1, which covers the curation operations and names one writer, the CLI classic-run log (MEM-OBJ-1), that the runtime search hits but the runtime member does not mention.

#### On RT-BAP-2 — Document text and summaries as model-visible data
- **Memory link.** The retained parts consumed are the stored summaries, page text, description and caller metadata. Force: advisory content; the model may use, ignore or misread it. Delivery: tool results (RT-RTE-2) and the first user message (MEM-RTE-1). No source-trust framing is applied at read time (RT-ABS-3).
- **Limits.** Effects on model behavior are unobserved.

## Write side

**Acquisition.** The only acquisition route is indexing a caller-named PDF (RT-RTE-1 flash, RT-RTE-3 standard). Extraction and structure detection run without per-object human input, so write agency is automatic even though a human triggers the call. PDF text goes to `pages.json` unsummarized; layout statistics, bookmarks and model calls produce the tree; a model writes summaries and the document description; the caller may add a `metadata` dict. Manual authoring is limited to that field.

**Automatic operations over retained material.** None. The tree optimizer, the standard-mode verify and fix passes and the summary scheduler all operate on a tree still in flight (RT-RTE-8, RT-RTE-9), and the optimizer's cost report is not stored. After the write, no route edits, merges or re-summarizes a stored document (MEM-ABS-1).

**Trace-fed transformation.** None. The only trace, the CLI classic-run log, is written and never read (MEM-OBJ-1). There is no compaction, checkpoint or continuation summary, since PageIndex keeps no conversation state. No derived behavior-shaping material exists, so there are no retained reasons to trace.

**Rejection and withdrawal.** Indexing refuses unsuitable inputs before writing (scanned or layout-less PDFs, non-PDF files, blank PDFs, out-of-range page spans) and writes `doc.json` last, so an interrupted write leaves an unlisted directory (RT-RTE-1). Withdrawal is deletion of the document directory by `delete_document`, reachable by an agent only under `include_management=True`; it keeps no history. Names taken get a numeric suffix rather than replacing the stored document.

**Horizons.** No task or project horizon applies: the store is durable and shared by all later calls that use the same `storage_path`. Nothing is timed against use.

## Read-back

**Pull (requested).** The chat model reads through the four tools (RT-RTE-2, annotated), and host models do through the adapters (RT-RTE-4). Selection is the model's judgment over names, descriptions, the outline and its summaries. Delivery is a tool result carrying JSON. The outline splits into parts when large, page text stops at the character budget, and omitted pages are named so the model can ask again. Local mode adds no code ranking; with `doc_id` set, a fixed allow-list restricts lookups to the named documents (Guarantee A in `output/runtime.md`), which bounds availability without targeting a part of a document.

**Push (automatic).** One route, MEM-RTE-1. Trigger: a chat call with `doc_id`. Selector: code. Selector input: the caller's `doc_id`, an upstream operator choice. Selected part: the metadata row of each named document, including the model-written description and caller metadata. Budget: none applied to this block. Channel: first user message. Signal: identifier, since the id matches a stored row and the matched row is what is delivered.

**Availability, delivery and activation.** Availability is the store. Delivery is wired for both routes. Activation, meaning whether the model reads the outline, follows the instructions to fetch pages or uses the delivered metadata, was not observed. No benefit is demonstrated here; README figures are reported only (SRC-3).

**Caller-held history.** A caller may pass the previous transcript back (RT-RTE-5). This is input the caller retains, not read-back from PageIndex's store.

## Comparison rationale

- **`storage_substrate: files`.** All scoped objects are JSON files. `service-object` would apply to cloud storage, which is excluded, so `known` is limited to that scope.
- **`representational_form: natural-language, symbolic`.** Summaries, page text and description are natural language. Node ids and page ranges are symbolic because code slices page text with them and checks their bounds, which is narrower than a symbolic index consumed by the model.
- **`lineage: imported, other-compiled, authored`.** Page text is imported, the tree and summaries are compiled, and `authored` records only the caller-supplied `metadata` field. Lineage is not trace-extracted because no trace feeds a stored object.
- **`behavioral_authority: knowledge` only.** The outline does not bind: the model decides which pages to read, and no code ranks or routes from the tree. The static instruction text has authority over the model but is not retained memory in this scope.
- **`write_agency: automatic, manual`.** Automatic is the indexing route. Manual is the metadata field only, and it is included because it is a wired route. Set aside, the profile would say automatic.
- **`curation_operations: absent`.** MEM-ABS-1 gives the bounded search. The index-time merge and expand steps and the name-suffix check are the nearest candidates and each is excluded by the type's rules on acquisition and collision checks.
- **`read_back_direction: pull, push`, `read_back_signal: identifier`.** Pull is every model-requested tool result. Push is the doc-targeting block (MEM-RTE-1), whose selection is an id lookup. Coarse availability (newest first in `browse_documents`) is pull-side listing, not a push signal.
- **`trace_learning: "no"` with `wired` basis.** The type encodes known non-occurrence as `known` with the value `"no"`, which makes the four dependent axes inapplicable. The evidence basis vocabulary has no negative, so `wired` only fills the required field; the entry's note says the negative rests on bounded searches (RT-ABS-1, MEM-ABS-1), not on a wired route.
- **`faithfulness_tested: absent`.** MEM-ABS-2. It is `absent` and not `no` because the search covered only the frozen repository, and the benchmarks that would matter are not frozen.

## Integration issues

1. **Scope choice, resolved in this round.** The reconciliation returned the conflict between the scope statement and the memory boundary definition. This report adopts reading one: the store accumulates through use because each submission adds a retained document and each deletion removes one, while querying changes nothing. The profile scope, Boundary and evidence, Core ideas and Write side use that wording. The positive values for `storage_substrate`, `lineage`, `read_back_direction` and `read_back_signal` stand on that reading, and no evidence basis or status was raised. Under the alternative reading (only query-time writes count) the boundary would be empty and those axes would be `absent` or `inapplicable`. Evidence: RT-RTE-1, MEM-ABS-1, RT-ABS-1. Concerns: RT-OBJ-1, RT-OBJ-2, RT-OBJ-3, MEM-RTE-1.
2. **Distinct grouping.** MEM-RTE-1 supplies document-targeting metadata within RT-RTE-2 and its RT-RTE-5 protocol variants. It owns the trigger, selector and selected input across those paths; no single-parent relation or duplicate supersession is asserted. Concerns: MEM-RTE-1, RT-RTE-2, RT-RTE-5.
3. **Addition to a supplied fact.** The runtime RT-ABS-1 search does not name the CLI classic-run log writer (MEM-OBJ-1). The conclusion of RT-ABS-1 is unchanged because the log is index-time and has no reader, but the RT-ABS-1 writer list is incomplete. Evidence: MEM-OBJ-1. Concerns: RT-ABS-1, MEM-OBJ-1.
4. **Supplied fact refined.** The runtime RT-OBJ-3 does not say the `metadata` field is caller-supplied and shown to the model; annotated on RT-OBJ-3. Concerns: RT-OBJ-3.
5. **Unresolved, not blocking.** The trace_learning encoding (`known`, `"no"`, basis `wired`) fills the required basis field with `wired` although the negative rests on searches (see Comparison rationale); the reconciliation may prefer another encoding. Concerns: MEM-ABS-1, RT-ABS-1.
6. **Untraced.** Citation resolution (`get_citations`, `resolve_citations`) reads the store's pages when checking citations and was not traced here. If it reads the store on a route the model does not request, it may add a read-back route. Concerns: RT-RTE-2, RT-CLM-5.

## Limitations and checks

**Prevented conclusions.** Nothing about cloud-mode indexing, storage or retrieval, host-runtime memory, provider caching or learning, model behavior on the delivered content, text-extraction quality, or retrieval accuracy and cost (README figures are reported only). No operation conclusion is above `uninspected`, and no run was made.

**Method and identity rechecks.** All reads were of commit-addressed blobs at `d2693d80791a86345ef78b3234834f5fe53a70a0` through `git --no-replace-objects -C related-systems/VectifyAI--PageIndex`. The worktree was not used as evidence. Every quote block was generated with `commonplace-quote` against the run's `run-state.md`; semantic support was judged by the analyst. The MEM-ABS-1 and MEM-ABS-2 searches were regex searches with the terms listed in those records, and a regex search can miss an unlisted synonym.

**Weaknesses.** The scope reading in Integration issues item 1 (accumulation by submission, not by querying) carries the report. Citation resolution was not traced (item 6). The `symbolic` and `manual` values rest on narrow wired uses stated in their evidence notes.

**Deterministic validation.** `commonplace-validate --full` was run on this correction-round report; result below.

Validation result: `commonplace-validate --full` on this report exited 0 with overall PASS (clean), no warnings or failures.
