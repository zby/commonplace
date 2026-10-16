---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Sparks workflow account: human-requested inbox ingestion through external-agent writing, mechanical finalization and later lookup."
run-id: AAS-2026-10-15-sparks-563865f8b26f-01
reviewed-boundary: "49abddc848ea55f78518bfbbbe04c3d37a5f2705"
---

# Sparks workflow report

## Workflow account

### Selection and evidence

The representative workflow is **process the inbox, persist its derived wiki content, then make that content available to a later question**. It is selected because the shipped contract explicitly joins prepare, semantic edits and finalize, while its Query section specifies later consumption. This is a prescribed workflow with inspected mechanical wiring, not a reconstructed successful agent session. The enclosing agent controls the sequence; Sparks does not launch or schedule that agent. The [boundary](boundary.md) fixes SRC-1 and excludes the external harness implementation and actual personal vault. The existing [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle) and [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume) identify the routes; workflow-specific conclusions below annotate them rather than duplicate them.

Independent source inspection covered SRC-1, `internal/contract/contract.md`, `internal/core/ingest.go`, `internal/core/ingest_finalize.go`, `cmd/sparks/ingest.go`, `internal/manifest/ingests.go` and `internal/inbox/archive.go`. These supply implementation and doctrine/design evidence only. No target commands, tests or services were executed. No supplied trace establishes agent compliance, actual delivery, safe recovery or improved answers.

### 1. Human capture and the first handoff

The human supplies inbox material and asks the external agent to process it. The contract assigns semantic page work to the agent and mechanical effects to the CLI; this is task allocation across a human, agent and deterministic tool, not delegation to another autonomous worker. The instruction-delivery dependency is [RT-BAP-agent-contract](runtime.md#rt-bap-agent-contract): a conventional instruction file or describe result can supply the protocol, but actual harness loading remains unobserved (SRC-1, `internal/contract/contract.md`).

The agent calls `sparks ingest --prepare`. Core reads and splits the current inbox, then opens an ingest row for a nonempty list. Its JSON handoff supplies ingest ID, entry content and capture dates, deterministic hints, total count and conservative affected-collection names. The agent, not prepare, chooses which pages to inspect and what semantic changes to make. An empty inbox returns zero entries without opening a row; that branch needs no finalize. An already-active ingest returns an ID and `already_in_progress`, not a fresh entry list (SRC-1, `internal/core/ingest.go`, `cmd/sparks/ingest.go`; lifecycle identity: [RT-OBJ-ingests](runtime.md#rt-obj-ingests)).

> // An empty inbox is a non-error: returns PrepareResult with zero entries
> // and does NOT open an in_progress row. Nothing to lock over.
> --- `internal/core/ingest.go`

### 2. Agent-owned writing and verification

The contract gives the agent a sequence: identify relevant pages; use capture dates for new-page creation dates; check aliases and prefer updates; preserve contradictions in a Revision section with both sources; set new-page maturity conservatively; update the index and append an ingest log entry; route TODOs to Tasks; then finalize. Existing pages, aliases and sources must be acquired by the agent through host reads or lookup. Prepare does not supply a complete existing-page context or perform these judgments (SRC-1, `internal/contract/contract.md`, `internal/core/ingest.go`; semantic actor: [RT-CMP-agent](runtime.md#rt-cmp-agent)).

> 3. Check existing pages' `aliases:` for dedup before creating. Prefer updating over creating.
> 4. If an existing wiki page contradicts a new entry, append a `## Revision` section noting the contradiction and both sources. Never silently overwrite.
> --- `internal/contract/contract.md`

The page/index/log changes are ordinary agent filesystem edits, not proposals awaiting a Sparks reviewer. There is no distinct critic agent or semantic acceptance oracle in this route. The human's initial request does not establish human approval of each page. The semantic checks above are protocol obligations. Task insertion is a separate deterministic write available through [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write); its successful append does not establish correct project assignment or duplicate suppression (SRC-1, `internal/contract/contract.md`, `internal/core/tasks.go`, as inspected in runtime).

The same contract requests `sparks lint` before declaring work done and `sparks fmt --check` for frontmatter. These can diagnose mechanical defects, but they are not prerequisites checked by finalize. The scan inside finalize checks only Scan's error return, not its per-file error list. Thus mechanical completion cannot stand in for semantic verification or even a clean diagnostic report. The inspected enforcement limits and quotations are retained in [RT-CLM-mechanical-integrity](runtime.md#rt-clm-mechanical-integrity) and [RT-RTE-maintenance-write](runtime.md#rt-rte-maintenance-write) (SRC-1, `internal/contract/contract.md`, `internal/core/ingest_finalize.go`, `internal/core/scan.go`, `cmd/sparks/lint.go`).

### 3. Finalize and the delivery boundary

When the agent judges its semantic work done, it calls `sparks ingest --finalize`. The handoff carries an operation request and optional commit message, not the prepared entry IDs, a per-entry completion receipt or reviewed page contents. Core requires an active ingest, rereads the live inbox, archives entries by capture date, clears the inbox, scans, optionally commits and finally completes the row. CLI prints counts and commit/skip information only after a successful core return (SRC-1, `cmd/sparks/ingest.go`, `internal/core/ingest_finalize.go`, `internal/inbox/archive.go`; [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle)).

> if err := db.CompleteIngest(current.ID, result.EntryCount, result.CommitSHA); err != nil {
> return result, fmt.Errorf("complete ingest: %w", err)
> }
> return result, nil
> --- `internal/core/ingest_finalize.go`

This mechanical delivery boundary consists of persisted files, refreshed manifest state subject to scan limits, and a completed ingest row. A Git commit is optional: disabled auto-commit, a non-repository or a clean tree can produce a successful completion with a skip reason. Git also stages the dirty vault tree rather than an isolated semantic batch, as established in runtime. Completion proves neither that every archived entry received a wiki treatment nor that the agent's prose is correct (SRC-1, `internal/core/ingest_finalize.go`, `internal/git/git.go`; [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle)).

The contract's 10–15-entry session budget is particularly consequential here. Prepare returns all entries; finalize selects all entries from the current inbox rather than a processed subset. If the agent handles only the suggested budget and nevertheless finalizes, remaining entries can be archived and cleared without corresponding semantic work. Entries appended between prepare and finalize can also enter the finalized set. External coordination is required; the source does not provide a subset-finalize handoff (SRC-1, `internal/contract/contract.md`, `internal/core/ingest.go`, `internal/core/ingest_finalize.go`; quote and selection fields in [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle)).

### 4. Rejection and operator-owned recovery

Two rejection branches establish the interlock's actual scope. Finalize without an active ingest returns an error before archiving. Prepare while a row is active refuses to open another session, but CLI deliberately serializes the existing-session result rather than propagating that particular error. An agent relying solely on command success can therefore miss that no new batch was prepared. It must examine `already_in_progress` and choose finalize, abort or escalation (SRC-1, `internal/core/ingest_finalize.go`, `internal/core/ingest.go`, `cmd/sparks/ingest.go`).

> res, err := core.PrepareIngest(v, db)
> if err != nil && !errors.Is(err, manifest.ErrIngestInProgress) {
> return err
> }
> --- `cmd/sparks/ingest.go`

> return FinalizeResult{}, fmt.Errorf("no in_progress ingest: run `sparks ingest --prepare` first")
> --- `internal/core/ingest_finalize.go`

Recovery is assigned to the caller/operator, not an automatic retry agent. CLI `--abort` changes the active row to aborted and unblocks subsequent prepare; it does not undo agent page edits, archive appends or inbox clearing. The abort branch calls only the manifest transition, with no file restoration (SRC-1, `cmd/sparks/ingest.go`, `internal/manifest/ingests.go`).

> if err := db.AbortIngest(current.ID); err != nil {
> return err
> }
> --- `cmd/sparks/ingest.go`

The finalize source comments prescribe abort/reprepare before clear, manual inspection/commit after clear, and abort after a commit whose row completion failed. These are recovery guidance, not demonstrated recovery. Archive writes append without entry deduplication: if interruption occurs after append but before clear, retrying can append the same entry again. After clear, an error does not reconstruct the inbox or revert semantic edits. There is no transaction across file changes, Git and the manifest. The stage reached determines what the operator must inspect (SRC-1, `internal/core/ingest_finalize.go`, `internal/inbox/archive.go`).

> f, err := os.OpenFile(path, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0o644)
> --- `internal/inbox/archive.go`

### 5. Later answer delivery

A later human question triggers a separate invocation: structured query selects metadata, the external agent reads matching wiki bodies and synthesizes an answer with wikilinks. Query output is not the persisted body content; page reads are the load-bearing bridge from retained semantic edits to possible answer influence. This is requested retrieval rather than an autonomous follow-up. The result is delivered as an external agent answer, not by finalize or query itself. No trace shows that retained edits changed a later answer or that citations were faithful (SRC-1, `internal/contract/contract.md`, `internal/manifest/queries.go`; quotation and consumer-selection details in [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume)).

The account therefore establishes a joined, source-prescribed persistence-to-consumption workflow with deterministic mechanical steps and agent-owned semantic decisions. Its success conditions remain separate: session completion, diagnostic cleanliness, semantic completeness and later answer quality are not interchangeable.

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

#### On [RT-RTE-ingest-cycle](runtime.md#rt-rte-ingest-cycle)

Workflow-specific delegation: the human requests ingest; the external agent calls prepare, interprets the result, writes derived content and chooses finalize. Sparks is a deterministic executor, not a delegated agent scheduler. Prepare supplies a structured entry list rather than a reviewed writing plan. Finalize receives no semantic completion receipt.

Verification and delivery: alias checks, contradiction preservation, lint and format checks are requested protocol work. The core completion transition accepts mechanical progress without checking those semantic obligations. The successful CLI summary marks mechanical return, not verified semantic completion. Recovery is caller/operator-owned through abort and inspection; abort releases lifecycle state without rolling back content. An active-row prepare result needs field inspection even when CLI returns successfully. These workflow findings are supported by the source passages in the account and the route's retained evidence; exercised compliance and recovery remain uninspected.

#### On [RT-RTE-vault-consume](runtime.md#rt-rte-vault-consume)

Workflow-specific terminal handoff: the later caller receives metadata first; the external agent must then read bodies before synthesizing a source-informed answer. The contract requests wikilink citations but does not evaluate the resulting answer. This later invocation is a separate requested workflow, not an automatic continuation scheduled by ingest. Persisted availability is established; actual read-back, answer delivery and semantic benefit remain unobserved.
