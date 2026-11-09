---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Nemsy workflow account: CLI source ingestion through retained-page delivery and a later user-requested Wiki answer."
run-id: AAS-2026-11-09-nemsy-2a6b7963bf65-01
reviewed-boundary: "2338bab0aab96a91efb90a80249f33510b630260"
---

# Nemsy workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is **CLI ingestion of a local document or directory, followed by a separately requested Wiki query**. It was selected because it crosses Nemsy's main knowledge-production and consumption handoffs: caller selection, model synthesis, parser admission, filesystem retention and later answer generation. The later query is not an automatic ingest successor; the human must initiate it. This is the composition of the shipped [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest) and [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), not an inferred autonomous plan. Optional answer retention follows [RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive).

The evidence is SRC-1 implementation and shipped prompt intent at the boundary revision. Focused source inspection covered `src/nemsy/cli.py` ingestion dispatch and batch/single-file drivers, `src/nemsy/agent.py` prompts, context loading, ingestion parser, query and archive helper, and `src/nemsy/vault.py` ingest-log/status functions. These paths were already included in the boundary; this member adds focused coverage of the parser-to-hash-status failure consequence. No supplied run shows the sequence succeeding, and no target execution was performed. Model compliance, factual fidelity and actual later influence remain unobserved.

### Request, selection and delegation

A caller invokes CLI ingest with a local path, or omits the path to scan the configured source root. Python resolves the path, collects eligible files, reads text and groups files by content-derived status. Unchanged files are skipped unless forced; empty content is recorded without a model call. A dry run stops before pending files are processed, but after empty-file logging. A root scan with more than twenty pending files asks for confirmation; declining stops that processing. These are operation-selection controls, not approval of generated content (SRC-1: `src/nemsy/cli.py`; [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)).

The foreground driver owns every executable transition. For each pending file it supplies source content, a title derived from the filename unless overridden, source path, ancestor directory guidance, the wide-context setting and output controls to agent.ingest. Ingest adds the Wiki index and up to ten recently modified other pages, or fifty with wide enabled. It supplies fixed task/schema instructions as the system argument and source, guidance and Wiki text as the user prompt. The generation service receives those texts; it does not receive an executable tool grant or delegated authority to choose filesystem actions. The service proposes SUMMARY and QUESTIONS text; Python determines how it is consumed (SRC-1: `src/nemsy/agent.py`, `src/nemsy/cli.py`; [RT-CMP-deepseek](runtime.md#rt-cmp-deepseek), [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)).

For a directory, processing is serial. Each completed write precedes the next file's fresh Wiki-context load, so an earlier generated page can become input to a later file's synthesis if selected by the recency window. That is a wired state dependency, not evidence of beneficial cross-document integration. Batch mode awaits each single-file call with streaming disabled:

> for f, content in pending:
>     short_name = _display_path(f)
>     # 更新描述，不影响进度条刷新节奏
>     progress.update(task, current_file=short_name)
>     # 批量模式关闭流式输出，结果由进度条上方统一打印
>     ok = await _run_ingest_single(
>         f, content=content, wide=wide,
>         out_console=progress.console,
>         stream=False,
>     )
> --- `src/nemsy/cli.py`

### Verification and durable delivery

For a streaming single-file call, the user sees text as it arrives, before parser admission. Batch mode awaits the full response. In both branches, code logs token usage and then invokes the parser. The parser requires a SUMMARY delimiter, removes a whole enclosing Markdown fence when matched, strips a duplicated pending-questions section from the summary, and appends the separately extracted QUESTIONS section. It writes a sanitized-title/date Markdown page, updates the Wiki index, then returns the relative page path. The ingest function subsequently appends an operation log and records the source hash (SRC-1: `src/nemsy/agent.py`; [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)).

The delimiter test is a syntactic rejection point. It is not a semantic reviewer, schema validator, source-fidelity test or link checker. The human authorizes processing but does not inspect and approve the particular summary before the write. The model's instructions to relate existing pages and mark contradictions are requests; the inspected executor writes one source-summary page and an index entry rather than executing a model-directed multi-page edit plan. There is no expected-answer oracle in this route. These limits and the retained passages are established in [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest).

Delivery has several different meanings here: streamed text is visible output; a successfully returned page path identifies a durable summary; the CLI batch success counter identifies only a completed single-file call. The latter is weaker than page delivery because the wrapper does not test the optional parser result. File writing, index updating and logs are separate operations, so partial completion is possible rather than an atomic knowledge update (SRC-1: `src/nemsy/agent.py`, `src/nemsy/cli.py`; [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)).

### Checked rejection and recovery path

A response without SUMMARY returns None from the parser. Ingest nevertheless proceeds to operation logging and record_ingest, and the CLI wrapper returns True. The supplied runtime record retains those exact passages. Further inspection establishes an important next-request consequence: record_ingest assigns a hash and done status for any nonempty input, while get_file_status later decides done from matching hash alone. It does not require that the recorded Wiki page exists or is non-null (SRC-1: `src/nemsy/vault.py`).

> if record is None:
>     return "new"
> if record.get("hash") == current_hash:
>     return "done"
> return "changed"
> --- `src/nemsy/vault.py`

> stripped = content.strip()
> current_hash = compute_hash(stripped) if stripped else _EMPTY_HASH
> status = "empty" if not stripped else "done"
> --- `src/nemsy/vault.py`

Consequently, an initially new, nonempty file whose summary was rejected can be skipped as unchanged on the next ordinary CLI ingest, despite having produced no page. This is a source-predicted failure path, not an observed incident. The status record is not a successful-delivery certificate. The caller must deliberately force another attempt or change the input to re-enter processing; manual state/content repair is outside this automatic sequence. A same-title/date retry can overwrite rather than restore a prior page. Exceptions from generation or later writes are not caught by the inspected per-file batch loop, so its success/failed counters are not a continue-on-every-error recovery protocol (SRC-1: `src/nemsy/cli.py`, `src/nemsy/agent.py`, `src/nemsy/vault.py`; [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)).

### Later consumption and final answer

After successful ingestion, a later ordinary CLI query loads the current Wiki index and up to thirty recent other pages. The source summary is eligible, not guaranteed to be included: the selector is recency/count rather than question-specific retrieval. Source-document content is not fetched again to verify the answer. The model receives the selected Wiki and question, with instructions to synthesize, cite pages and refuse to fill gaps with training knowledge. Python returns and displays the answer without a semantic acceptance gate. Thus the answer is delivered text, not a verified conclusion; citation and grounding compliance remain unobserved (SRC-1: `src/nemsy/agent.py`; [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer), [RT-CLM-wiki-grounding](runtime.md#rt-clm-wiki-grounding)).

The user can request archive when starting that ordinary query. If set, code writes the returned answer and fixed metadata, removes the advisory ARCHIVABLE marker and updates the index without another model call or post-answer human approval. Without that flag, the marker alone does not persist the answer. This finishes either with transient answer delivery or with an additional retained query page; it does not automatically initiate lint, criticism, regeneration or installation of new instructions (SRC-1: `src/nemsy/agent.py`; [RT-RTE-answer-archive](runtime.md#rt-rte-answer-archive)). The reasoning-query variant has different, tuple-incompatible archive handling and is not covered by this successful-path description; see [RT-RTE-reasoning-query](runtime.md#rt-rte-reasoning-query).

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

#### On [RT-RTE-document-ingest](runtime.md#rt-rte-document-ingest)

Workflow handoff: the CLI foreground driver selects pending sources and serially supplies each to agent.ingest; the generation service returns text, not executable next-step authority. Parser admission and filesystem completion are separate from visible response delivery and from the CLI's success count.

Workflow recovery: missing SUMMARY can still advance the stored hash to the current nonempty input, suppressing an unchanged retry unless the caller forces it. The Workflow account retains the additional status-function evidence. This extends the rejection consequence without declaring a second ingestion route.

#### On [RT-RTE-wiki-answer](runtime.md#rt-rte-wiki-answer)

Workflow successor: a new human query request, not ingestion completion, initiates answer generation. A retained summary crosses into that request only if the fresh context selection includes it. The result is delivered when returned/displayed, without a semantic verifier certifying the answer.
