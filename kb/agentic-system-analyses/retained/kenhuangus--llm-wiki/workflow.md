---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "LLM Wiki workflow account: batch source ingestion through model extraction, merge admission, failure handling and persisted catalog delivery."
run-id: AAS-2026-10-17-llm-wiki-507fade8a56e-01
reviewed-boundary: d2bd485921f6c7b6071afbb389f44ab8e4e83c69
---

# LLM Wiki workflow report

## Workflow account

### Selection and evidence

The representative workflow is the shipped `python tools/pipeline_all.py` batch, selected because one driver explicitly connects source acquisition, normalization, model extraction, wiki admission and catalog delivery. It is not a workflow constructed by joining unrelated capabilities. Its owner is Python code acting under the operator's process authority; the models receive bounded stage inputs, not responsibility for choosing subsequent tools or scheduling work. This account traces [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion) and [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission).

Evidence is SRC-1 implementation and shipped prompt doctrine at the [frozen boundary](boundary.md#boundary-and-evidence). Direct inspection for this lens covered complete `tools/pipeline_all.py`, `tools/normalize.py`, `tools/extract.py`, `tools/integrate.py`, `tools/index.py` and `tools/prompts.py`. This adds detailed workflow inspection within the already registered source, not a new evidence source. No target execution, provider response or independently inspectable completed batch was observed. The following sequence describes wiring, not demonstrated successful operation.

### Request and handoffs

1. **Operator to driver.** A repository-root CLI launch starts an open ingestion batch. The driver sequentially launches arXiv, CVE, GitHub, RSS and curated monitor subprocesses. It then independently discovers all files matching its recursive glob under `raw/auto_ingest/` and `raw/manual/`; discovery is not restricted to files produced during this invocation. Subprocess command paths are relative, so the launch directory matters. Monitors supply files rather than a typed per-item return object to the remaining stages (SRC-1: `tools/pipeline_all.py`; [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion)).
2. **Driver to normalizer.** Each discovered file path and a domain derived from its parent directory become CLI arguments. The normalizer reads text or extracts PDF text, constructs a content-derived ID and writes frontmatter plus body under `raw/normalized/<domain>/`. Empty or unreadable input returns without writing the normalized artifact, but does not deliberately exit nonzero. The next handoff is a new directory scan, not a returned source-to-output mapping (SRC-1: `tools/normalize.py`, `tools/pipeline_all.py`).
3. **Driver to extractor and model.** The driver selects normalized Markdown lacking a `.json` sidecar. Extraction strips frontmatter, sends the body with the active extraction instruction and requests structured intelligence. The instruction asks for entities, claims, relationships, evidence sentences and confidence; the implementation's gate is JSON parsing, not validation of that whole structure or evidence accuracy. The extractor adds the normalized ID and writes the sidecar. Model-call retries and optional cloud fallback belong to [RT-RTE-model-call](runtime.md#rt-rte-model-call), not an independent reviewing agent (SRC-1: `tools/extract.py`, `tools/prompts.py`, `tools/pipeline_all.py`).
4. **Driver to integrator and optional merge model.** The driver scans every normalized JSON sidecar, including older ones. It supplies category, domain and a basename-derived title. The integrator constructs the destination and formats only claim text, confidence and source ID into the new claim body. Extracted evidence sentences, entities and relationships remain in the sidecar but are not passed through this projection. A new destination is written without another model judgment. An existing destination causes a merge call containing its old body and the projected new claims. Any nonempty completion is admitted as the replacement body; empty output instead appends claims to the old body. This is software admission without per-page human approval or an independent answer oracle (SRC-1: `tools/integrate.py`, `tools/pipeline_all.py`; [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission)).
5. **Integrator to persisted page and catalog.** The integrator directly writes frontmatter and body, then logs the update. After all attempts, the driver invokes `tools/index.py`, which rereads wiki pages and writes `wiki/index.md` with domain listings, confidence summaries and pending-review links. It does not build a persisted BM25 search index. The batch finally prints completion and writes a success-labelled log entry (SRC-1: `tools/integrate.py`, `tools/index.py`, `tools/pipeline_all.py`).

The distinction between extraction and integration contexts is load-bearing: the model's requested evidence-rich JSON is not what the merge model receives. The supplied runtime record establishes the merge input; the extractor's instruction specifies the richer requested output (SRC-1: `tools/prompts.py`; [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission)):

> - Cite specific sentences as evidence for each claim
> --- `tools/prompts.py:22-22`

### Verification, rejection and recovery

**Malformed extraction output is a real local rejection.** JSON parsing failure logs an error and exits extraction with status 1 before sidecar writing. The driver catches subprocess failure in `run_command`, prints it and returns false. Its callers do not branch on that return, so the batch continues to other files, integration scans and final indexing. Successful JSON parsing can still be followed by failure on an unexpected structure; parsing alone does not establish admissible claim content (SRC-1: `tools/extract.py`, `tools/pipeline_all.py`; [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission)).

> except subprocess.CalledProcessError as e:
>     print(f"FAILED: {' '.join(cmd_list)} - {e}")
>     return False
> --- `tools/pipeline_all.py`

**Conflict detection is advisory admission, not a veto.** The merge instruction requests preservation, attribution, historical claims and a conflict marker. Code recognizes `STATUS: CONFLICT`, changes metadata and still writes the merged page. The catalog subsequently lists conflict/review-needed pages for humans; it neither obtains acknowledgment nor stops publication. No independent evidence check or semantic preservation validator intervenes. A nonempty merge may replace old content regardless of prompt compliance (SRC-1: `tools/prompts.py`, `tools/integrate.py`, `tools/index.py`; [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission)).

**Recovery is best effort, not batch rollback.** The merge's empty-output append is a local fallback. The batch contains no compensating restoration of already written pages after a later subprocess fails. A later invocation can retry extraction when no sidecar exists; an existing sidecar suppresses extraction even if its source has changed. Conversely, integration has no consumed-sidecar marker: all sidecars are selected again. The implementation explicitly chooses reintegration rather than tracking completion (SRC-1: `tools/pipeline_all.py`):

> # Avoid double integration if marked?
> # For simplicity, we just integrate. integrate.py handles deep merging.
> --- `tools/pipeline_all.py`

Repeated integration can therefore increment `source_count` for the same sidecar rather than establish independent corroboration. Previously successful artifacts persist alongside failures, and this driver does not automatically assign a human or another agent to repair them. Those are inspected control-flow consequences, not observed incidents (SRC-1: `tools/pipeline_all.py`, `tools/integrate.py`; [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion)).

### Delivery and limits

The batch's product is persisted Markdown, sidecars, catalog and logs, not a conversational answer. Its success-labelled terminal message means the driver reached its end after stage attempts; it does not certify that every artifact was produced, verified or cataloged. A page becomes available after its direct write, before catalog completion or human review. Subsequent integrations reload existing bodies, and later search/API/synthesis consumers can read retained pages through [RT-RTE-wiki-consumption](runtime.md#rt-rte-wiki-consumption). These are wired delivery paths, not evidence of accurate content or actual downstream use (SRC-1: `tools/pipeline_all.py`, `tools/integrate.py`, `tools/index.py`).

This selection does not generalize the batch's destinations, scheduling or recovery to daemon, watcher or API routes. Their material differences remain in [RT-RTE-scheduled-drivers](runtime.md#rt-rte-scheduled-drivers) and [RT-RTE-api-mutation](runtime.md#rt-rte-api-mutation). Within the selected workflow, stage delegation and durable handoff are established; successful unattended completion, reliable semantic verification and human response are unobserved.

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

#### On [RT-RTE-batch-ingestion](runtime.md#rt-rte-batch-ingestion)

Workflow role: Representative end-to-end driver. Stage handoffs are synchronous subprocess calls followed by fresh filesystem scans, not per-source acknowledgments. Its terminal delivery signal is unconditional with respect to the caught subprocess failures. The pending-human-review catalog is a post-write notification surface, not acceptance before delivery. The workflow account above supplies the additional implementation passages from SRC-1: `tools/pipeline_all.py`, `tools/index.py`.

#### On [RT-RTE-knowledge-admission](runtime.md#rt-rte-knowledge-admission)

Workflow role: Local extraction rejection and optional merge decision inside the selected batch. Parse failure prevents that extraction's sidecar; it does not reject the batch. Empty merge output activates append fallback, whereas conflict-marked nonempty output remains admissible. No stage in this traced driver waits for human review before the page write or catalog delivery (SRC-1: `tools/extract.py`, `tools/integrate.py`, `tools/pipeline_all.py`, `tools/index.py`).
