---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "o-o workflow: sequential library refresh through per-document research, in-place admission and browser delivery."
run-id: AAS-2026-10-15-o-o-b6fd0055e5c1-01
reviewed-boundary: b0d5063e37b4eafdbc23c1899a31f1836168b989
---

# o-o workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is an operator-requested library refresh: `bash example/index.o-o.html --update-all`, followed by reading the updated library and articles in a browser. This route was selected because one shipped control path connects document selection, repeated agent delegation, durable research edits and navigation rebuilding. An ordinary article such as `example/anthropic-leadership.o-o.html` supplies the research contract inside each eligible child invocation. This is not a constructed chain of unrelated features: `update_all` explicitly calls each selected document and then `rebuild_index`. See [RT-RTE-batch-create](runtime.md#rt-rte-batch-create), [RT-RTE-document-update](runtime.md#rt-rte-document-update) and [RT-RTE-library-read](runtime.md#rt-rte-library-read). SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`.

The account establishes implementation and requested agent behavior at the frozen commit, not a successful refresh. No target was executed, no provider was called and no observed-run evidence was supplied. Source inspection for this lens covered index batch selection, freshness, dispatch, terminal action routing, index projection and browser metadata consumption, plus the representative ordinary research contract. These are additional focused reads within SRC-1's already included implementation and doctrine/design scope, not a new source or evidence layer.

### 1. Operator to library driver

The operator requests a refresh; the index shell determines which documents receive work. The `--update-all` action rejects a non-index invocation. For an index, it recursively discovers `.o-o.html` files under the index directory, excludes itself and examines first-matching date and interval fields. Force selects every candidate; otherwise missing or invalid dates qualify, or parsed age must exceed the interval. Fresh documents are skipped. This is a scheduling/spend gate, not research verification. It does not compare a candidate article against a reference answer. SRC-1: `example/index.o-o.html`; [RT-RTE-batch-create](runtime.md#rt-rte-batch-create).

The parent runs eligible children sequentially, passing the file path and optionally `--force`. It does not hand them a combined research context or forward a parent model override. Each child re-enters its own shell and freshness gate. At the exact interval boundary the batch's strict greater-than selection differs from the child's less-than skip test; this workflow does not normalize that discrepancy. SRC-1: `example/index.o-o.html`; [RT-RTE-batch-create](runtime.md#rt-rte-batch-create), [RT-RTE-document-update](runtime.md#rt-rte-document-update).

### 2. Document driver to external research agent

For an eligible ordinary article, the child extracts a budget, constructs a prompt containing its absolute path and launches the external Claude CLI. The prompt requests reading the document contract and date, restricts edits to article and retained-state blocks, and grants the requested tool surface through CLI flags. An optional model applies to a direct child invocation when supplied there; the batch itself does not carry it through. The delegate receives a pointer and instructions, not automatically the complete document in the initial prompt. Reading the article, contract and cache remains requested agent work. SRC-1: `example/index.o-o.html`; [RT-CMP-claude](runtime.md#rt-cmp-claude), [RT-BAP-update-prompt](runtime.md#rt-bap-update-prompt).

Responsibility changes here: o-o owns file selection and process launch; the external agent owns research queries, source judgments, synthesis and edits. No o-o supervisor observes those internal decisions or assigns independent reviewer agents. The external runtime's own subagents, permissions and context management remain uninspected, not established absent. SRC-1: `example/index.o-o.html`; [RT-RTE-document-update](runtime.md#rt-rte-document-update).

### 3. Research, requested checks and direct admission

The representative contract supplies the subject, audience, research intents, required sections, preferred and denied domains, image constraints and output conventions. It asks the agent to reuse prior research and focus on changes since `as_of`; if little changed, it asks for enrichment rather than merely a minimal update. These conditions guide open-ended research, not a bounded evaluation with an expected answer. SRC-1: `example/anthropic-leadership.o-o.html`; [RT-RTE-document-update](runtime.md#rt-rte-document-update).

The deliverable spans both visible content and state needed for later maintenance:

>       "9. Update oo-manifest: increment version, set as_of to today (YYYY-MM-DD).",
>       "10. Update oo-source-cache: record all sources you used (url, title, tier, accessed date). Preserve previous sources that are still valid.",
>       "11. Update oo-changelog: append an entry with version, timestamp, and summary of what changed.",
> --- `example/anthropic-leadership.o-o.html:434-436`

Source-policy judgments and image size/type checks are assigned to the research agent. They can inform rejection of a source or an oversized image, but the shell does not independently inspect their decisions. The operator starts the run without approving each claim. The agent's tool writes admit changes directly to the original file, rather than submitting a candidate for a separate accept/reject decision. The section-preservation instruction is best effort at the o-o boundary: the same delegate has requested Bash access, and no section-aware write filter is interposed here. SRC-1: `example/index.o-o.html`, `example/anthropic-leadership.o-o.html`; [RT-RTE-document-update](runtime.md#rt-rte-document-update), [RT-BAP-update-prompt](runtime.md#rt-bap-update-prompt).

### 4. Process completion to reader delivery

When the CLI exits successfully, the child announces completion; there is no intervening factual, citation, JSON or preservation acceptance test. Thus the shell's success condition is process return, not a verified article. The parent increments its count after the child returns, continues sequentially and rebuilds navigation if it processed at least one document. This explicit handoff links maintenance to the reader-facing library:

>   if [[ "$updated_count" -gt 0 ]]; then
>     echo "o-o: Updated $updated_count document(s)."
>     echo "o-o: Rebuilding index..."
>     rebuild_index
> --- `example/index.o-o.html`

Rebuilding extracts title, version, date, size and an article excerpt. Table links use basenames despite recursive discovery; top-eight cards are a sorted projection, not delivery of the full research cache or a quality assessment. Browser article rendering reads HTML and manifest metadata and builds navigation/citation links. The durable product is the edited local file plus rebuilt library projection, available when the operator opens them; there is no inspected automatic browser launch, publication or reader acknowledgment in this path. Correct rendering and correct nested links are not demonstrated. SRC-1: `example/index.o-o.html`; [RT-RTE-library-read](runtime.md#rt-rte-library-read).

### Failure and recovery

A concrete inspected failure branch is a missing Claude executable:

>       if ! command -v claude &>/dev/null; then
>         echo "o-o: Error — 'claude' CLI not found." >&2
>         echo "o-o: Install: https://docs.anthropic.com/en/docs/claude-code" >&2
>         exit 1
>       fi
> --- `example/index.o-o.html`

This rejects dispatch before research, rather than falling back to another agent. A nonzero child process can interrupt the strict-mode batch before its final index rebuild. If earlier children already edited their files, those edits remain; the library-wide operation is not transactional. A delegate that fails after writing may likewise leave partial edits. Neither the child nor batch route retains a candidate snapshot, automatically restores previous state or retries failed research. Recovery is left to the operator and external environment: repair the dependency or file, then rerun or force the update as appropriate. A rerun still uses freshness metadata, so it is not an unconditional retry of a partially changed document. No successful recovery is observed. SRC-1: `example/index.o-o.html`; [RT-RTE-batch-create](runtime.md#rt-rte-batch-create), [RT-RTE-document-update](runtime.md#rt-rte-document-update).

The resulting coordination mechanism is sequential shell orchestration around one external research executor per eligible document. It delivers through direct persistent mutation and later local consumption, not through review-gated proposals. That source-level structure is established; successful research, policy compliance, actual spending and reliability remain unobserved.

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

#### On [RT-RTE-batch-create](runtime.md#rt-rte-batch-create)

Workflow role: outer sequencing and final navigation refresh. This account selects its batch branch, not creation. A completed child command advances the sequence; there is no separate research-quality acknowledgment. Failure before the loop completes can prevent the final projection refresh even when earlier child files changed.

#### On [RT-RTE-document-update](runtime.md#rt-rte-document-update)

Workflow role: per-document delegated research and direct admission. The consequential handoff supplies a path, document-specific instructions obtained by reading, budget and requested tools. Verification remains inside the same agent's requested work; successful process return ends the shell step without a distinct review gate. Recovery responsibility returns to the operator rather than a shipped repair worker.

#### On [RT-RTE-library-read](runtime.md#rt-rte-library-read)

Workflow role: delivery projection and reader entry. Batch success initiates rebuilding, while browser opening remains a separate reader action. Metadata extraction and rendering consume edited state without establishing its factual correctness or the completeness of the preceding maintenance work.
