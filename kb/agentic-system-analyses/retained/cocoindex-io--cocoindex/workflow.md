---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "CocoIndex workflow account: PDF manual extraction through typed model output and PostgreSQL delivery, with bounded rejection and recovery findings."
run-id: AAS-2026-10-15-cocoindex-3514227a0537-01
reviewed-boundary: "1639793b3602408a9cb220728fb30e306d433473"
---

# CocoIndex workflow report

## Workflow account

### Selection and boundary

The representative workflow is the shipped manuals extraction pipeline, [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction). It was selected because it connects source discovery, document conversion, a model handoff, typed acceptance and a retained product in one application. It is a fixed model-assisted indexing workflow, not evidence of an autonomous agent coordinating sub-agents. The author supplies the task policy; CocoIndex schedules processing; the model supplies structured content. No multi-agent negotiation or end-to-end answering-agent workflow is established by this example. SRC-1: `examples/manuals_llm_extraction/main.py`.

All findings concern implementation or declared instructions at the frozen revision, not an observed run. Direct inspection here covers the full manuals example and the PostgreSQL row-action dispatcher and upsert methods in `python/cocoindex/connectors/postgres/_target.py`. This adds workflow-specific inspection within SRC-1, not another source. The runtime's supplied records support the engine and maintenance baseline. No target, test, provider or database was executed.

### Request and source-to-model handoffs

1. **Operator to application.** The example documents `cocoindex update main` for catch-up and `-L` for live operation. Its application is named `ManualsLlmExtraction`, with `./manuals` as its source directory. The lifespan creates an asyncpg pool from `POSTGRES_URL` and supplies the change-detected `LLM_MODEL` context key. The default model is `openai/gpt-4o`, with an environment override. The operator starts processing, not approval of each extracted assertion. The entry and scheduling baseline is [RT-RTE-index-update](runtime.md#rt-rte-index-update); model identity limits are in [RT-CMP-llm-model](runtime.md#rt-cmp-llm-model). SRC-1: `examples/manuals_llm_extraction/main.py`.

2. **Application to file processors.** The application mounts a PostgreSQL table target, using `ModuleRecord` and primary key `filename`, then recursively selects `**/*.pdf` and mounts `process_file` over the resulting items. Each processor receives a file object and the target, rather than an open-ended task description. `live=True` enables the source's live capability; it does not itself grant continuous application execution, as [RT-RTE-live-maintenance](runtime.md#rt-rte-live-maintenance) explains. SRC-1: `examples/manuals_llm_extraction/main.py`.

3. **File processor to converter.** `process_file` reads bytes and awaits conversion before extraction. The conversion is assigned to the CocoIndex GPU runner, but the converter's actual Docling accelerator option is CPU. Runner placement and converter device are distinct choices. The provider later receives converted Markdown, not the original PDF bytes or the source directory. Whether conversion preserves every relevant table, symbol or layout feature is not established: Docling's implementation and an execution artifact are outside the inspected evidence. SRC-1: `examples/manuals_llm_extraction/main.py`.

> options = PdfPipelineOptions(
>         accelerator_options=AcceleratorOptions(device=AcceleratorDevice.CPU)
>     )
> --- `examples/manuals_llm_extraction/main.py`

> @coco.fn.as_async(runner=coco.GPU)
> def pdf_to_markdown(content: bytes) -> str:
>     source = DocumentStream(name="manual.pdf", stream=io.BytesIO(content))
>     return pdf_converter().convert(source).document.export_to_markdown()
> --- `examples/manuals_llm_extraction/main.py`

4. **Extraction function to model.** The memoized extractor creates an Instructor client over `litellm.acompletion`, requests JSON mode and supplies `ModuleInfo` as the response model. The model-visible context consists of the fixed extraction instruction in a system message and the converted manual in a user message. The request asks for a title, description, classes, methods and arguments, restricted to what the text supports. The source passage and authority limits are already retained in [RT-BAP-extraction-prompt](runtime.md#rt-bap-extraction-prompt). The model is delegated content extraction, not database access, source selection, or deciding whether another agent should run. Provider/tool internals are uninspected. SRC-1: `examples/manuals_llm_extraction/main.py`.

### Verification, admission and delivery

Instructor's response-model request is followed by `ModuleInfo.model_validate(result.model_dump())`; the passage is retained in [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction). The schema requires title and description and defines nested classes, methods and arguments, with empty-list and empty-description defaults for several fields. This checks representational compatibility, not factual support or extraction completeness. There is no separate expected-answer oracle or human review step between that return and row declaration in the inspected function. The system-message instruction is requested model behavior, not an enforcement mechanism. SRC-1: `examples/manuals_llm_extraction/main.py`.

After successful extraction, code copies selected fields into `ModuleRecord`, computes the two counts and serializes the complete model object as JSON. In particular, `num_methods` counts the module-level `info.methods` list, not every method nested under classes. The stored product contains derived summaries and structured JSON; it does not automatically retain the full converted manual as a separate row field. SRC-1: `examples/manuals_llm_extraction/main.py`.

> filename=file.file_path.path.name,
>             title=info.title,
>             description=info.description,
>             num_classes=len(info.classes),
>             num_methods=len(info.methods),
>             module_info=json.dumps(info.model_dump()),
> --- `examples/manuals_llm_extraction/main.py`

Declaring the row is a handoff to target reconciliation, not itself evidence of a committed database write. The PostgreSQL connector separates upserts and deletes, schedules chunks in a task group, and executes SQL through an acquired connection. The dispatch passage is in [RT-RTE-index-update](runtime.md#rt-rte-index-update). Both upsert implementations await `conn.execute`; one uses a VALUES statement and the other an unnest statement. SRC-1: `python/cocoindex/connectors/postgres/_target.py`.

> sql = f"{self._insert_into} VALUES {values_sql} {self._conflict_clause}"
>         async with self._pool.acquire() as conn:
>             await conn.execute(sql, *params)
> --- `python/cocoindex/connectors/postgres/_target.py`

The intended delivered result is reconciled records in `coco_examples.modules_info`, while the application function returns `None`. Completion is therefore indexing completion, not a conversational answer. This source establishes a wired delivery path conditional on successful conversion, inference, validation and external writes. No database artifact establishes actual delivery here. A later query or answering consumer for these manual records was not traced; the separate text-index query in [RT-RTE-query-index](runtime.md#rt-rte-query-index) must not be attached to this pipeline as if it were its shipped consumer. SRC-1: `examples/manuals_llm_extraction/main.py`, `python/cocoindex/connectors/postgres/_target.py`.

### Rejection and recovery

The checked rejection branch is a conversion, provider or validation exception before `extract_module` returns successfully. The call sequence awaits conversion, then extraction, then declares the row. Neither local function catches these exceptions. Thus a failing extraction does not produce this invocation's new row declaration. This does not prove that an old row is immediately removed, or that other files' completed effects are rolled back. Instructor's internal retries and provider behavior are outside this source pin; no successful recovery is observed. SRC-1: `examples/manuals_llm_extraction/main.py`.

> markdown = await pdf_to_markdown(await file.read())
>     info = await extract_module(markdown)
>     table.declare_row(
> --- `examples/manuals_llm_extraction/main.py`

A schema-valid but unsupported assertion has no factual rejection gate in that sequence. The application author/operator would have to change source material, prompt, schema, model configuration or processing code and invoke maintenance again. Both extraction and file processing are memoized; tracked invalidation matters when rerunning, and an unchanged provider alias does not pin behavior. Dependency-conditioned reuse is described in [RT-OBJ-component-memoization](runtime.md#rt-obj-component-memoization). Full reprocessing and explicit drop are available maintenance controls in the runtime baseline, with the failure and partial-retirement qualifications of [RT-RTE-drop-app](runtime.md#rt-rte-drop-app). They are not demonstrated semantic repair or a transaction spanning every model call, memo write and PostgreSQL action.

The workflow consequently supplies computational shape admission and external target reconciliation, not an independently verified correctness decision. It retains extracted content and memoized work. This inspection does not establish a critique-driven revision of the extraction method, downstream answer benefit, or successful unattended recovery.

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

#### On [RT-RTE-manual-extraction](runtime.md#rt-rte-manual-extraction)

Workflow selection: this is the single representative model-assisted pipeline traced above, not a new route identity. Delegation is fixed by author-written code: file bytes go to conversion, converted Markdown goes to the provider with a schema and instruction, and accepted structured content returns to code for row construction. There is no sub-agent return protocol established by these handoffs.

Verification and recovery boundary: acceptance concerns typed structure, not support by the original PDF. Conversion or extraction failure prevents the new row declaration in that function's sequence; it does not establish whole-application rollback. Delivery is a database-target product conditional on successful reconciliation, not a later agent answer. The workflow account retains the new source passages supporting these refinements; generic route identity, evidence and status remain in the runtime member.
