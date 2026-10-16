---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Agentic Local Brain workflow: host-assisted restricted-page collection through file admission, metadata extraction and best-effort indexing."
run-id: AAS-2026-10-12-agentic-local-brain-f00cbd577178-01
reviewed-boundary: "41ea0cb104686eb0d39f32c94c2b84d37cdff0e7"
---

# Agentic Local Brain workflow report

## Workflow account

### Selected workflow and evidence

The representative workflow is **save a web article, recover from restricted-page fetching, and admit the recovered text as a file**. It is selected because the shipped collection skill explicitly connects the user request, command attempt, external-agent recovery and second command. This is not a workflow inferred by joining independent mining and retrieval features. The ordinary webpage path is the first attempt; the file path is the documented recovery branch ([RT-RTE-host-fallback](runtime.md#rt-rte-host-fallback), [RT-RTE-file-admission](runtime.md#rt-rte-file-admission)).

The evidence is SRC-1 at the revision fixed by [the boundary](boundary.md). The skill supplies doctrine/design; the command, collector and indexing helper supply implementation. No host session, user store or execution trace is supplied. The workflow is therefore instructed across the host boundary and wired inside the application, not observed to complete. The external agent's browser, shell permissions and orchestration are not Local Brain capabilities.

Additional inspection for this member covers the complete SRC-1 `skills/localbrain-collect/SKILL.md`, the file and webpage command branches in `kb/commands/collect.py`, the collection method in `kb/collectors/file_collector.py`, and the indexing function in `kb/commands/utils.py`. These extend source inspection, not the source identity or functional boundary. Other collection types, installer execution and the development-agent scaffolding are not this selected workflow.

### 1. Request interpretation and first handoff

A user asks an external agent to save an article URL. The collection skill tells that agent to evaluate intent in order: local path, URL, academic-paper signal, explicit bookmark request, then webpage by default. It directs the agent not to invent tags or summaries by default; supplied user values are passed through, otherwise application extraction supplies them. This is model-interpreted guidance, not a Python routing invariant (SRC-1 `skills/localbrain-collect/SKILL.md`).

> When a user's request is ambiguous, use the following decision rules to choose the correct collection type. **The order of evaluation matters — check from top to bottom and use the FIRST match.**
> --- `skills/localbrain-collect/SKILL.md`

The host invokes `localbrain collect webpage add <url>`. The handoff supplies the URL, optional title/tags/summary and command flags. Python, rather than a second agent, owns the next application step: `webpage_add` calls `WebpageCollector.collect`, then inspects `result.success`. On a nonduplicate failure it prints the collector error and exits with status 1; a duplicate is reported as skipped and returns normally. This result distinguishes failed admission from a skip, but does not prove that the fetched article is complete or authentic (SRC-1 `kb/commands/collect.py`).

> click.echo(f"Skipped (duplicate): {result.error}")
> return
> click.echo(f"\n✗ Collection failed: {result.error}")
> raise SystemExit(1)
> --- `kb/commands/collect.py:176-305`

### 2. Recovery ownership moves back to the host

When direct webpage fetching fails on a restricted URL, the skill directs the external agent to try its own browser/fetch tool. The host then saves retrieved content as temporary Markdown and invokes file collection with the original page title. If automated methods fail, the host asks the user to paste the article and saves that content as a note or file. These are explicit recovery instructions, not an application-internal retry dispatcher ([RT-RTE-host-fallback](runtime.md#rt-rte-host-fallback); SRC-1 `skills/localbrain-collect/SKILL.md`).

> - Fetch/render the page content using the agent's tools
> - Save the content to a temporary markdown file (e.g., `/tmp/webpage_title.md`)
> - Use `localbrain collect file add /tmp/webpage_title.md --title "Original Page Title"` to collect it
> --- `skills/localbrain-collect/SKILL.md`

The second handoff supplies a filesystem path and title, not a browser session, credentials or the failed collector's result. The file command resolves that path and records it as the source. Consequently, the original URL is not automatically preserved as the structured source field by this fallback. It may remain in host-written content, but the instruction does not require that. Temporary-file cleanup, host fetch validation and a final host-to-user confirmation are unestablished by this procedure.

### 3. File admission and automatic derivation

Click requires an existing input path. `FileCollector.collect` additionally rejects unsupported suffixes; the implementation supports `.pdf`, `.md`, `.markdown` and `.txt`, despite the skill's broader file-reference wording. With `--skip-existing` and storage supplied, it checks the resolved source path before heavy processing. In the fallback this is the temporary path, not the original article URL; the check should not be read as proof of article-level deduplication (SRC-1 `kb/collectors/file_collector.py`).

> if skip_existing and storage:
>     source_key = str(file_path)
>     existing = self._check_duplicate(source=source_key, storage=storage)
> --- `kb/collectors/file_collector.py`

The collector extracts text, generates metadata and a safe filename, writes Markdown and returns `CollectResult` containing success, saved path, title, word count, metadata and content hash. Exceptions in that block become a failed result. The driver then reloads saved text, applies smart extraction when enabled, updates frontmatter, writes the knowledge row and tags, and attempts search indexing. The model proposes missing metadata; software admits it. Neither the host starting collection nor the user supplying a title constitutes review of each extracted field ([RT-RTE-file-admission](runtime.md#rt-rte-file-admission); SRC-1 `kb/commands/collect.py`, `kb/collectors/file_collector.py`).

Indexing receives item ID, content, title, tags, resolved source path and content type. The helper chunks the text, sends chunks to the configured embedding provider, writes Chroma documents/vectors, then saves SQLite chunk records. These are local function/service handoffs, not independently identified worker agents. The provider receives document-derived text; it does not receive a grant to run commands. Metadata extraction and embedding components retain the model-fixity limits described in [RT-CMP-litellm-provider](runtime.md#rt-cmp-litellm-provider) and [RT-CMP-embedding-provider](runtime.md#rt-cmp-embedding-provider).

### 4. Acceptance, degraded delivery and terminal output

The implemented checks establish input admissibility, conditional duplicate detection and execution success/failure, not a content-quality oracle. No per-document approval or independent reference answer is used in the inspected sequence. This is an open collection request, not a bounded improvement experiment. The caller can decline the request or provide explicit fields; generated missing fields and index results are admitted by software under the configured extraction/indexing guidance. Later editing/deletion is separate from this procedure ([RT-RTE-file-admission](runtime.md#rt-rte-file-admission)).

The application terminal result is printed collection status with title, word count, saved path and optional tags/summary. Semantic indexing has its own optional success line. The helper returns false after failed chunking or caught indexing errors, and the driver suppresses indexing exceptions. Collection can thus be delivered in a degraded state: retained file/metadata without demonstrated semantic-search availability (SRC-1 `kb/commands/collect.py`, `kb/commands/utils.py`).

> except Exception as e:
>     # Log error but don't fail the collection
>     click.echo(f"  Warning: Failed to index content for search: {e}", err=True)
>     return False
> --- `kb/commands/utils.py`

The success display is an application completion signal, not verification that every retained representation is synchronized:

> click.echo("\n✓ Collection successful!")
> click.echo(f"  Title: {result.title}")
> click.echo(f"  Word count: {result.word_count}")
> click.echo(f"  Saved to: {result.file_path}")
> --- `kb/commands/collect.py:1-175`

The file write, metadata admission and index writes are staged effects without a workflow-wide transaction or rollback in the inspected sequence. Host fallback recovers a fetching failure; it does not repair a later partial indexing write. The skill recommends checking statistics periodically and browsing via the web interface, but those instructions do not add article-content validation to this fallback. Actual final user receipt, successful restart read-back and retrieval benefit remain unobserved. Later retained-state consumption is established as a wired possibility by [RT-RTE-file-admission](runtime.md#rt-rte-file-admission), not a required final step of this selected collection procedure.

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

#### On [RT-RTE-host-fallback](runtime.md#rt-rte-host-fallback)

Workflow role: recovery after the direct webpage command fails; the external host owns tool selection and the next command. The recovery handoff is temporary Markdown plus a title. Asking the user for pasted content is the instructed escalation when automated methods fail. Application completion and host-to-user delivery are separate boundaries; only the former has the inspected command output mechanism.

#### On [RT-RTE-file-admission](runtime.md#rt-rte-file-admission)

Workflow role: terminal application admission after host recovery. Input checks can reject a path/format or skip an existing resolved source; they are not semantic acceptance criteria. Collection output can be delivered despite indexing failure. The recovered page's structured source becomes a file path, so original-URL provenance and article-level deduplication require more than this handoff supplies.
