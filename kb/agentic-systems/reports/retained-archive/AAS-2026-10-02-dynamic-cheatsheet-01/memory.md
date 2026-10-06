---
type: agentic-systems/types/agent-memory-analysis-report.md
description: "Memory mechanisms of Dynamic Cheatsheet across caller-supplied cheatsheets and retrieval examples"
run-id: AAS-2026-10-02-dynamic-cheatsheet-01
source-identity: "https://github.com/suzgunmirac/dynamic-cheatsheet"
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
report-status: complete
memory-comparison:
  scope: "The API-level memory boundary includes caller-supplied cumulative cheatsheet text and prior input/output examples with their supplied embeddings, the code that updates or selects them, and later calls that consume returned or supplied material. Caller backing stores are outside the inspected boundary. It excludes the active query and answer as ordinary current-call state, temporary prompt assembly, provider-owned memory, and general client chat history."
  axes:
    storage_substrate:
      assessment: partial
      values: [in-memory]
      evidence:
        in-memory:
          basis: wired
          records: [RT-OBJ-1, MEM-OBJ-1, MEM-OBJ-2, RT-RTE-1, RT-RTE-2, RT-RTE-3, RT-RTE-4, RT-RTE-5]
          note: "The methods receive text, arrays and vectors as arguments and use them in process memory; the cumulative route returns its candidate string. The substrate callers use between calls is outside this boundary."
      records: [RT-OBJ-1, RT-OBJ-2, MEM-OBJ-1, MEM-OBJ-2, RT-RTE-1, RT-RTE-2, RT-RTE-3, RT-RTE-4, RT-RTE-5]
      note: "In-process access is inspected. The README documents checkpoint/resume and a file-based initialization path for its benchmark CLI, but that CLI implementation is outside the registered source paths; the underlying persisted-memory substrate and its use cannot be completed from this boundary."
    representational_form:
      assessment: known
      values: [natural-language, parametric]
      evidence:
        natural-language:
          basis: wired
          records: [RT-OBJ-1, MEM-OBJ-1, RT-RTE-1, RT-RTE-2, RT-RTE-3, RT-RTE-4, RT-RTE-5]
          note: "Cheatsheets and prior input/output examples are strings assembled into model input."
        parametric:
          basis: wired
          records: [MEM-OBJ-2, RT-RTE-2, RT-RTE-3, RT-RTE-5]
          note: "The caller supplies a dense embedding matrix; cosine similarity over its rows selects prior examples. Its producer is outside the boundary."
      records: [RT-OBJ-1, RT-OBJ-2, MEM-OBJ-1, MEM-OBJ-2, RT-RTE-1, RT-RTE-2, RT-RTE-3, RT-RTE-4, RT-RTE-5]
      note: "The scoped text and dense-vector parts are represented and consumed in these two forms. Temporary formatting does not introduce a separate retained form."
    lineage:
      assessment: partial
      values: [authored, trace-extracted]
      evidence:
        authored:
          basis: afforded
          records: [RT-OBJ-1, RT-RTE-1]
          note: "A caller can supply initial cheatsheet text; the README demonstrates an initial value."
        trace-extracted:
          basis: wired
          records: [RT-OBJ-1, RT-RTE-1, RT-RTE-3]
          note: "The curator response is extracted as the next cheatsheet after receiving the current question, generator response and prior sheet."
      records: [RT-OBJ-1, RT-OBJ-2, MEM-OBJ-1, MEM-OBJ-2, RT-RTE-1, RT-RTE-2, RT-RTE-3, RT-RTE-4, RT-RTE-5]
      note: "Authored initial text and automatic extraction from a query episode are evidenced. The caller's prior example corpus and vector provenance are not supplied by the library, preventing complete lineage classification for those parts."
    behavioral_authority:
      assessment: partial
      values: [knowledge, ranking, learning]
      evidence:
        knowledge:
          basis: wired
          records: [MEM-OBJ-1, RT-RTE-2, RT-RTE-4, RT-RTE-5]
          note: "Selected past input/output pairs are assembled as reference material for the generator; the retrieval route explicitly says to verify and adapt examples."
        ranking:
          basis: wired
          records: [MEM-OBJ-2, RT-RTE-2, RT-RTE-3, RT-RTE-5]
          note: "The supplied embedding vectors determine the relative order and top-k selection of delivered examples."
        learning:
          basis: afforded
          records: [RT-OBJ-1, RT-RTE-1, RT-RTE-3]
          note: "An automatic curator updates a candidate cheatsheet from a query and answer, and the documented caller flow passes the returned candidate to a later query. No operation or benefit was observed."
      records: [RT-OBJ-1, RT-OBJ-2, MEM-OBJ-1, MEM-OBJ-2, RT-RTE-1, RT-RTE-2, RT-RTE-3, RT-RTE-4, RT-RTE-5]
      note: "Knowledge, ranking and learning paths are supported at the stated bases. The external curator/generator templates are not registered sources, so whether cheatsheet text is framed as standing instruction cannot be resolved; provider compliance and actual effects are unobserved."
    write_agency:
      assessment: known
      values: [automatic, manual]
      evidence:
        automatic:
          basis: wired
          records: [RT-OBJ-1, RT-RTE-1, RT-RTE-3]
          note: "The wrapper calls the model curator and extracts its tagged candidate without a human admission step."
        manual:
          basis: afforded
          records: [RT-OBJ-1, RT-RTE-1]
          note: "The caller supplies the initial cheatsheet argument; documentation demonstrates a caller-provided starting string."
      records: [RT-OBJ-1, RT-RTE-1, RT-RTE-3]
      note: "Both caller authoring and automatic candidate production are supported. Caller-side persistence and acceptance remain external choices."
    curation_operations:
      assessment: not-determinable
      values: []
      evidence: {}
      records: [RT-OBJ-1, RT-RTE-1, RT-RTE-2, RT-RTE-3]
      note: "The wrapper delegates content transformation to caller-provided templates and model output, which are not registered sources. The code establishes full-string extraction and replacement, but cannot establish whether content is consolidated, evolved or synthesized."
    read_back_direction:
      assessment: known
      values: [pull, push]
      evidence:
        pull:
          basis: wired
          records: [RT-OBJ-1, MEM-OBJ-1, RT-RTE-1, RT-RTE-4]
          note: "The caller supplies the cumulative cheatsheet or the full prior corpus to the selected method, which assembles that requested material for the generator."
        push:
          basis: wired
          records: [MEM-OBJ-1, MEM-OBJ-2, RT-RTE-2, RT-RTE-3, RT-RTE-5]
          note: "On a query, the wrapper automatically selects prior examples by cosine similarity and supplies them to the generator or curator."
      records: [RT-RTE-1, RT-RTE-2, RT-RTE-3, RT-RTE-4, RT-RTE-5]
      note: "Caller-requested supplied material and automatic similarity selection are separate read-back routes. Cross-call availability depends on caller-managed state."
    read_back_signal:
      assessment: known
      values: [inferred-embedding]
      evidence:
        inferred-embedding:
          basis: wired
          records: [MEM-OBJ-2, RT-RTE-2, RT-RTE-3, RT-RTE-5]
          note: "The current supplied query embedding is compared with prior supplied embeddings; descending cosine similarity selects the delivered rows and paired examples."
      records: [MEM-OBJ-2, RT-RTE-2, RT-RTE-3, RT-RTE-5]
      note: "The only automatic push selector in the scoped routes uses embedding similarity. The full-history and cumulative-cheatsheet paths are caller-selected pull routes."
    trace_learning:
      assessment: known
      values: ["yes"]
      evidence:
        "yes":
          basis: afforded
          records: [RT-OBJ-1, RT-RTE-1, RT-RTE-3]
          note: "The current query and generated answer feed automatic cheatsheet production; the README shows the returned text supplied to a later invocation. This establishes an afforded trace-fed behavior-shaping update, not observed improvement."
      records: [RT-OBJ-1, RT-RTE-1, RT-RTE-3]
      note: "The finding covers the cumulative cheatsheet route only. The temporary retrieval-synthesis sheet is not retained internally and is excluded unless a caller separately reuses it."
    trace_source:
      assessment: known
      values: [session-logs]
      evidence:
        session-logs:
          basis: wired
          records: [RT-RTE-1, RT-RTE-3]
          note: "The curator consumes the current query and the generator's answer from the same work episode as its update input; no stored tool trace or environmental event stream feeds this route."
      records: [RT-RTE-1, RT-RTE-3]
      note: "The classified trace source is the query/answer episode used for cumulative extraction. Caller-supplied historic examples have unknown origin and do not add a trace-source value."
---

# Dynamic Cheatsheet memory report

## Boundary and evidence

This report covers the API-level memory surfaces of Dynamic Cheatsheet at commit `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`. The included material is the caller-supplied cumulative cheatsheet, the caller-supplied prior input/output examples and dense embeddings, the cumulative update and retrieval routes, and later calls that consume supplied or returned material. The library itself does not persist these values between calls. Caller-managed storage is outside the registered implementation evidence; the API representation is available only while passed through the process. The source boundary lists implementation in `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py` and `text_generation/simple_unified_client.py` (`SRC-1`), plus the documented usage contract in `README.md` (`SRC-2`). No provider calls, caller application, execution traces, or experiments were supplied.

The runtime report is a starting account, not the source. I checked each memory-bearing `advanced_generate` branch, tagged extraction, caller handoff, embedding selection, and the exposed client chat history against those registered files. The repository describes a CLI checkpoint/resume and initialization-from-file path, but its dispatcher and persistence implementation are not among the registered anchors. This report therefore treats those as an access gap rather than claiming a file-backed implementation. The README example does show the caller passing `results['final_cheatsheet']` to a later query:

> # Pass the updated cheatsheet to the next query to accumulate knowledge
> next_results = model.advanced_generate(
>     approach_name="DynamicCheatsheet_Cumulative",
>     input_txt="Question #2: 1 3 8 9",
>     cheatsheet=results['final_cheatsheet'],  # Reuse the cheatsheet
> --- `README.md:113-117` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

| Entry point or operation | Registered source path | Coverage record or disposition |
|---|---|---|
| Cumulative cheatsheet generation, extraction and caller resubmission | `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/extractor.py`; `README.md` | `RT-OBJ-1`, `RT-RTE-1`; annotated below. Caller backing store excluded. |
| Retrieval synthesis and top-k example selection | `dynamic_cheatsheet/language_model.py` | `RT-RTE-2`; annotated below. Its synthesized sheet is a returned temporary value, not internally retained. |
| Cumulative cheatsheet plus retrieval | `dynamic_cheatsheet/language_model.py` | `RT-OBJ-1`, `RT-RTE-3`; annotated below. |
| Full history and similarity-only retrieval | `dynamic_cheatsheet/language_model.py` | `RT-OBJ-2`, `RT-RTE-4`, `RT-RTE-5`; corpus and embeddings split into `MEM-OBJ-1` and `MEM-OBJ-2`. |
| Direct `UnifiedLLMClient.chat` and caller-built message lists | `text_generation/simple_unified_client.py` | Excluded as ordinary current-run conversation state; no cross-process persistence is implemented by the client object. |
| Default single-call generation and local recursive code output | `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/execute_code.py` | No retained-memory route: prompt and execution output are current-call state. |
| Provider-native code interpreter state | `text_generation/simple_unified_client.py` | Excluded provider-owned state; persistence and later consumers are uninspected. |
| Benchmark CLI checkpoint, resume and initialization | `README.md` | Documentation advertises these paths; the implementation file is outside the Source register, preventing a source-grounded persistence classification. |
| Solution-evaluation helper and memory quality assessment | `dynamic_cheatsheet/utils/extractor.py`; `dynamic_cheatsheet/language_model.py` | `extract_solution` exists in the extractor, but the registered memory orchestration contains no call to it; no memory admission quality evaluation is evidenced in the inspected paths. |

## Core ideas

Cumulative memory is text passed into each call. The wrapper gives the current sheet to the generator, then sends the current question, complete generator response and previous sheet to the curator. The curator's response replaces the in-call sheet only when tag extraction succeeds; subsequent configured rounds consume that replacement. The result includes the updated text, and the README shows how a caller can pass it to another query. The library does not own the persistence step. The extractor's fallback also preserves the old in-call value when the expected tags are missing:

> new_cheatsheet = extract_cheatsheet(response=cheatsheet_output, old_cheatsheet=current_cheatsheet)
>                 cheatsheet = new_cheatsheet
> --- `dynamic_cheatsheet/language_model.py:434-435` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

Retrieval reads caller-supplied prior inputs, outputs and embeddings. It compares the final embedding row to earlier rows, sorts by cosine similarity and indexes the aligned text pairs. The automatic selector determines which examples reach the model; it does not assess whether the prior answer is correct. The retrieval prompt text itself warns that examples may be wrong and asks for verification and adaptation. No execution evidence shows whether the model follows that warning:

> current_original_input_embedding = original_input_embeddings[-1]
>             prev_original_input_embeddings = original_input_embeddings[:-1]
>
>             # Retrieve the most similar k input-output pairs from the previous inputs and outputs
>             if len(prev_original_input_embeddings) > 0:
>                 similarities = cosine_similarity([current_original_input_embedding], prev_original_input_embeddings)
>                 top_k_indices = np.argsort(similarities[0])[::-1][:retrieve_top_k]
>                 top_k_original_inputs = [original_input_corpus[i] for i in top_k_indices]
>                 top_k_original_outputs = [generator_outputs_so_far[i] for i in top_k_indices]
> --- `dynamic_cheatsheet/language_model.py:505-513` @ `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`

The curator and generator templates are caller-supplied files in the documented example. Their contents are not registered evidence, so their treatment of source trust, instruction strength, rationale retention and editing guidance is unknown. The code does expose a narrow structural gate: a tagged proposal is accepted as the entire new string, including an empty tagged string; if tags are absent, the supplied fallback string is returned. Each cumulative step also returns both the prior and proposed sheet, which gives a caller a value to preserve, but does not create internal version history or rollback.

The directly exposed `UnifiedLLMClient.chat` stores user and assistant turns in an object-level list and later calls read that list. Under the shared record contract this is ordinary current-run state, not accumulated memory of the scoped query-memory framework. The repository also has provider-native tool routes, but provider-managed memory or later tool consumers are outside this boundary.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-1 — Caller-supplied prior input/output examples

Part of: RT-OBJ-2
- Source-native identity: prior rows of `original_input_corpus` paired by index with `generator_outputs_so_far`.
- Representational form: natural-language input and output strings.
- Storage substrate: caller-managed before the call; passed to and formatted by the wrapper in process memory.
- Lineage: unknown for the supplied rows; the library consumes but does not acquire or persist the corpus.
- Memory consumer and behavioral authority: the generator receives all rows in `FullHistoryAppending`, or selected rows in retrieval routes, as context/reference. Actual response effects are unobserved.
- Raw versus derived: source input/output strings are the supplied examples; formatted prompt sections are temporary derived views and are not retained.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py`, `FullHistoryAppending` and retrieval branches. The retrieved inputs and outputs are indexed from the caller's arrays.

#### MEM-OBJ-2 — Caller-supplied embedding matrix

Part of: RT-OBJ-2
- Source-native identity: rows of `original_input_embeddings`, with the final row treated as the current query in retrieval-only and retrieval-synthesis routes and earlier rows treated as candidates.
- Representational form: distributed-parametric dense vectors.
- Storage substrate: caller-managed before the call; passed and compared in process memory.
- Lineage: producer and model version are outside the registered source boundary.
- Memory consumer and behavioral authority: the wrapper's cosine-similarity selector uses vector values to rank and select input/output rows for the generator or curator.
- Raw versus derived: supplied dense vectors are access structures for the paired text; no vector update or learning occurs in the inspected routes.
- Evidence: `SRC-1` at `dynamic_cheatsheet/language_model.py`, retrieval branches. The method compares the last row with previous rows and selects paired corpus/output indices.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On RT-OBJ-1 — Cumulative cheatsheet text

- Storage substrate: argument and returned string in process memory; external durable storage is caller-owned and uninspected.
- Representational form: natural-language.
- Lineage: caller-authored initial text is afforded; curator-produced replacement is trace-extracted and wired.
- Memory consumers and their behavioral authority: generator receives the supplied text as query context; the curator receives it as the previous sheet when updating. Compliance and effect are unobserved.
- Raw versus derived: the caller's initial value is source content; each accepted curator value is a derived candidate replacing it.
- Write agency, curation, trace learning and source: initial supply can be manual; curator generation and tag extraction are automatic. Trace learning is afforded through caller resubmission of the returned value. Exact content operation is not determinable because the template is outside the Source register; current query and generator answer feed the update.
- Read-back: caller supplies the sheet to a later call; the wrapper inserts it in the generator prompt. Within a multi-round call, the next round receives the just-extracted value. It has no automatic selector, budget or expiry. Missing tags preserve the previous value; an empty tagged body can replace it with an empty string. The returned step values expose previous and new strings for caller-side recovery. Cross-call delivery is documented, not observed.

#### On RT-OBJ-2 — Caller-supplied retrieval corpus and embeddings

- Storage substrate: the caller supplies in-process arrays; backing store and between-call retention are external.
- Representational form: mixed natural-language examples and distributed-parametric vectors; see the declared parts `MEM-OBJ-1` and `MEM-OBJ-2`.
- Lineage: unknown for corpus rows and vectors; the runtime accepts them without acquisition or provenance validation.
- Memory consumers and their behavioral authority: full-history formatting supplies prior examples as context; retrieval uses vectors for ranking and delivers aligned text pairs as reference. Effects remain unobserved.
- Raw versus derived: corpus strings and vectors are inputs; formatted retrieval sections are temporary views.
- Write agency, curation, trace learning and source: no corpus or embedding write is implemented by the inspected retrieval methods. Any accumulation by the caller is outside the boundary.
- Read-back: on each query, the selected route either supplies all caller-provided history or the cosine-ranked top-k pairs. The push route uses the current query vector and earlier vectors, with `retrieve_top_k` as its count limit. No invalidation, expiry, confidence filter or correctness gate is implemented by these paths.

#### On RT-RTE-1 — Cumulative cheatsheet generation and update

- Write agency, curation, trace learning and source: a model automatically proposes a whole replacement after generation; tag extraction admits the string within the call. Current query and complete generator response feed the update. Exact content operation is not determinable without the caller template.
- Read-back: the generator reads the current sheet; configured later rounds read the accepted string. A later method call reads it only if the caller supplies it. No internal persistent write or invalidation exists. Missing tags reject the proposal by falling back to the current sheet. Empty tagged text is accepted. Per-step results include prior and proposed strings, but no rollback store exists.
- Behavioral authority: prompt context to the generator and input to the curator; actual model compliance is unobserved.

#### On RT-RTE-2 — Retrieval-synthesis query route

- Write agency, curation, trace learning and source: a curator automatically receives selected prior input/output pairs, the current query and a caller-provided previous sheet, then returns a query-specific candidate. This candidate is returned; the route does not retain it internally. Its content operation is not determinable without the template.
- Read-back: current query embedding triggers cosine top-k selection from caller-supplied vectors. Selected paired text is passed to the curator, whose output is passed to the generator. There is no internal later read-back, persistence, expiry or rejection quality test beyond tag extraction. If tags are missing, the fallback is the formatted retrieval examples, not the prior cumulative sheet passed into the template.
- Behavioral authority: selected examples provide reference/context; vectors drive ranking. Actual effects are unobserved.

#### On RT-RTE-3 — Cumulative cheatsheet with retrieval

- Write agency, curation, trace learning and source: the caller supplies the initial cumulative sheet and examples; embedding ranking supplies examples to the generator; the curator then creates a replacement candidate from the current query, full generator response and previous sheet. The current query/answer feed an afforded trace-learning route when the caller reuses the returned string.
- Read-back: the generator receives the supplied sheet plus selected examples; the curator receives the prior sheet. The code admits a tagged candidate or falls back to the previous sheet. Later calls receive the result only by caller action. No internal persistence, versioning or expiry exists.
- Behavioral authority: examples provide reference/context, embeddings determine ranking, and the updated sheet can shape a later generator prompt. No observed behavioral effect is available.

#### On RT-RTE-4 — Full-history appending

- Write agency, curation, trace learning and source: the route does not write or curate prior examples; caller acquisition and storage are outside the boundary.
- Read-back: the caller selects this route and supplies aligned examples; the method formats every supplied prior input/output pair into the current prompt. No automatic ranker, retained update, expiry or quality check is present.
- Behavioral authority: prior pairs enter as generator context; use is unobserved.

#### On RT-RTE-5 — Dynamic retrieval without synthesis

- Write agency, curation, trace learning and source: no write or curation occurs; the route consumes caller-provided examples and vectors.
- Read-back: the current query vector triggers cosine similarity over earlier rows; top-k paired examples are supplied to the generator for that call. Later calls recompute from caller-supplied arrays. No persistence, invalidation or expiry is implemented.
- Behavioral authority: selected examples enter as reference/context and vector similarity determines ranking; effect is unobserved.

## Write side

The caller supplies initial cheatsheet text and, for retrieval routes, previous input/output strings and their embeddings. The library does not acquire benchmark traces, generate embeddings, or append new rows to the caller's corpus in the registered methods. The cumulative route is the only inspected automatic memory update: it generates an answer, sends that answer together with the query and old cheatsheet to a curator, extracts a tagged string and returns it. Cumulative retrieval follows the same update after supplying ranked examples. No second evaluation oracle is supplied to decide whether an answer or updated sheet is correct.

The tag gate is a format gate, not a content review. Missing tags retain the prior string. A tagged empty body becomes an empty string and therefore can withdraw current reliance when returned and reused. Each round's result carries both the current and new strings, which offers caller-side recovery if the caller preserves them. No history, rollback, deletion protocol or independent reviewer is maintained by the library. The exact curation guidance and whether the derived sheet retains reasons are unknown because the templates are caller-provided and outside the registered evidence.

Retrieval-synthesis creates a formatted view from selected pairs, then asks the curator for query-specific text. It returns that view or extracted replacement but does not write the candidate to a retained store. Its fallback is the formatted retrieval view itself. No maintenance operation cleans, deduplicates, expires, invalidates or promotes corpus rows in the inspected routes.

## Read-back

Cumulative generation reads the caller-supplied cheatsheet. The cumulative retrieval variant also reads the top-k examples selected automatically from caller-supplied embeddings. The retrieval-only and synthesis routes use the final embedding row as the current query and select aligned earlier inputs and outputs by cosine score. `FullHistoryAppending` supplies all caller-provided pairs. These are distinct: passing a specified sheet or corpus is pull, while similarity-ranked examples are pushed by an automatic selector during a query.

The retrieval methods assemble selected material into the prompt, but no execution trace shows delivery to a provider or later behavior. The code limits the number of selected examples with `retrieve_top_k`; it does not verify array alignment, embedding provenance or answer correctness in these branches. Cumulative output can reach a later consumer only when a caller persists and resubmits it. The README demonstrates that handoff, while the actual caller store and any checkpoint/resume implementation remain uninspected. No evidence establishes realized benefit.

## Comparison rationale

The profile treats caller-supplied text and vectors as separate operative parts. Text supplies the generator with knowledge/context; dense embeddings supply a ranking signal for paired examples. Both are accessed in process memory, while the caller's persistent store is unresolved. The query/answer update is automatic, but cross-call retention depends on caller action, so trace learning is afforded at the system boundary and does not imply measured improvement.

`inferred-embedding` is the only push signal because the inspected automatic selector compares query and corpus vectors. The full-history and cumulative-sheet routes use caller-selected material, so they are pull routes. Curation operation remains not determinable: the code's tagged-string replacement does not reveal whether the model consolidates existing claims, revises them, or synthesizes new ones. The templates and output are not available as source evidence.

The automatic update consumes the active query and answer from one work episode. It does not read a stored session log or tool trace. The report classifies that episode as session-log content at the trace-source level; this describes the content feeding the write, not a separate retained log object. Historical corpus rows have unknown provenance and do not justify additional trace-source values.

## Integration issues

- `RT-OBJ-2` groups prior text pairs and dense embeddings. This report declares `MEM-OBJ-1` and `MEM-OBJ-2` as distinct operative parts because text is delivered to a model while vectors drive selection and have different forms and provenance. The combined `RT-OBJ-2` remains a valid container; no supersession is requested.
- `RT-RTE-2` passes `previous_cheatsheet` into the curator template, but `extract_cheatsheet` receives `curated_cheatsheet` as its `old_cheatsheet` fallback. Therefore missing tags preserve the formatted retrieval view, not the prior cumulative sheet. This affects the meaning of rejection and possible loss of prior sheet content in the returned candidate. Reconciliation should retain this route-level distinction.
- The tagged extractor accepts an empty body as a new empty string. This makes caller-side withdrawal of current cheatsheet reliance possible on resubmission. The previous value appears in the returned per-step data, but the runtime report's description of caller recovery should not be read as an implemented rollback store.
- The runtime's memory scope does not inspect the benchmark CLI implementation even though `README.md` documents save, resume and initial-cheatsheet paths. The storage mechanism, ordering of checkpoint writes and later consumer are unresolved; this report limits its storage assessment accordingly.
- The source contains an `extract_solution` helper, but the registered orchestration paths did not show it participating in memory update or admission. No finding about benchmark evaluation or quality-based memory selection follows from that helper alone.

## Limitations and checks

The source boundary is the registered commit `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`; implementation anchors were checked against the supplied boundary and runtime member. Quotation blocks were generated with `commonplace-quote` from the supplied run-state and registered source paths. Caller storage, CLI implementation, prompt-template contents, embedding origin, provider internals, model outputs, execution traces, answer quality, activation and performance are uninspected; conclusions about those matters are prevented. A bounded search of the registered implementation paths for evaluation, correctness, feedback, persistence, cleanup and update operations found no memory admission evaluator or corpus-maintenance path; this does not establish their absence in the excluded CLI or caller application.

Validation: `commonplace-validate --full` passed after the report structure was repaired.
