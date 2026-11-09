---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Curated Thoughts workflow: agent deposit through librarian generation, proposal admission and later recall, with bounded recovery paths."
run-id: AAS-2026-11-08-curated-thoughts-00ab3a770403-01
reviewed-boundary: "433ebbd48c2ffd0e871e34a1505dcdef1a78c8fd"
---

# Curated Thoughts workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is **an agent deposits a completed task's finding, Curated Thoughts processes it into proposals, an admission route resolves them, and a later agent requests relevant context**. It was selected because the shipped integration skill explicitly connects post-task deposit to later pre-task recall, and the implementation connects deposit to ingest and librarian processing. It exposes model delegation, verification, admission and return without assuming a general-purpose agent executor inside Curated Thoughts. SRC-1, `.skills/curated-thoughts/skill.md`, `src-tauri/src/wisdom_deposit.rs`; [RT-CLM-agent-workflow](runtime.md#rt-clm-agent-workflow), [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick).

This is a source-grounded capacity trace, not a supplied execution of that workflow. The task-solving agent and its coding result remain outside the inspected runtime; the skill requests ordering but cannot enforce it. There is no supplied vault/session trace showing that any deposited finding reached a later agent or improved its work. CTI and model/provider internals remain outside the frozen sources, as stated in the [boundary](boundary.md#boundary-and-evidence). All additional source inspection below supplies SRC-1 implementation evidence, except the skill, which supplies doctrine/design. No target code, test or provider was executed.

### Request and handoff to processing

1. **The external agent supplies a finding, not a database mutation.** After non-trivial work, the skill requests `wisdom_deposit`. The call supplies a path, title and body, with optional metadata. Rust rejects an empty title/body, an invalid lane or an existing destination; a correction must use a new deposit or the separate supersession route. The write uses exclusive creation rather than replacing an old source. These are source-admission checks, not judgments about the finding's truth. SRC-1, `.skills/curated-thoughts/skill.md`, `src-tauri/src/wisdom_deposit.rs`; [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick).

2. **The dispatcher hands durable paths and configuration to a blocking worker.** The file is written before a transaction seeds audit and kick state. Audit failure attempts compensating file removal. With generation configured, the MCP path detaches processing and returns `pending: true` with `kick: started`; without it, the label is `no_ingest_host`. Thus successful deposit delivery means a source-file handoff, not a completed knowledge product. The short-lived CLI awaits the kick to avoid dropping its runtime with queued work, but that does not turn its original response shape into proof of knowledge admission. SRC-1, `src-tauri/src/wisdom_deposit.rs`; [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick).

3. **Rust, not the model, owns ingestion and scheduling.** The worker serializes kicks, takes the vault lock, derives a canonical document key, reads bytes from the vault and calls shared ingest. It records `chunked` before attempting the librarian. Sustained lock contention records `queued_watcher`, placing progress on a running watcher rather than guaranteeing that this worker completed processing. Non-contention lock errors fail instead of following that retry path. The handoff is conventional worker execution, not a fresh reasoning agent with its own tools. SRC-1, `src-tauri/src/wisdom_deposit.rs`; [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick).

### Model delegation and verification

4. **The librarian delegates a bounded content proposal.** Folder, tier and note-level gates decide whether extraction runs. The content-hash/model watermark can skip unchanged documents. When it runs, Rust selects retained candidate entities/facts and numbered source chunks, constructs structural context, truncates the assembled input and supplies a system/user request to the configured generation provider. Candidate context precedes source context, so truncation can remove source suffixes. The model receives this selected text, not a database connection, tool-selection loop or full vault. Its response returns to Rust as proposal JSON. SRC-1, `src-tauri/src/librarian/mod.rs`, `src-tauri/src/librarian/synthesis.rs`; [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis), [RT-CMP-generation-provider](runtime.md#rt-cmp-generation-provider).

5. **Verification can reject structure and identifiers, not certify truth.** JSON/schema parsing has one corrective retry; the retry appends the parse error to the original user request. Subsequent validation filters proposal items using the full candidate/chunk collections, not just the text that survived truncation. A citation passing an identifier check therefore does not prove the model saw or correctly interpreted its source. Nonempty facts can survive with unknown evidence references omitted. There is no expected-answer oracle in this open-document processing route. SRC-1, `src-tauri/src/librarian/synthesis.rs`; [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis).

> let second = completer.complete(system, &retry_user)?;
>             parse_json_only(&second)?;
>             Ok(second)
> --- `src-tauri/src/librarian/synthesis.rs`

### Admission and delivered result

6. **Proposal storage is not final admission.** Folder policy chooses pending review or automatic resolution. Seeded agent-lane rules enable synthesis with auto-approval, while the fallback does not. Automatic resolution constructs accept decisions for every proposal item; a GUI operator can accept, edit or reject items on the manual route. Both reach the shared resolver and its transaction. CLI review is another manual route, but terminal presence does not authenticate a human. There is consequently no universal per-fact human approval gate. SRC-1, `src-tauri/src/librarian/synthesis.rs`, `src-tauri/src/db/commit.rs`, `src-tauri/src/proposals_api.rs`, `tools/src/cmds.rs`; [RT-OBJ-folder-rules](runtime.md#rt-obj-folder-rules), [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission).

7. **Delivery has separate milestones.** A committed entry is a retained knowledge product; an embedding failure can leave later repair work without undoing that commitment. A later external agent must independently request `curated_recall_context`. That handler selects live wiki entries lexically and code chunks by cosine ranking and returns structured JSON, not a generated answer. Query selection can omit a committed finding. Full MCP also requires its audit write to succeed before returning. Only a returned matching entry establishes delivery to the caller; neither commitment nor return establishes behavioral use. The separate tools MCP has different, best-effort logging. SRC-1, `src-tauri/src/tool_dispatch.rs`, `tools/src/bin/curated_thoughts_mcp.rs`; [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission), [RT-RTE-context-recall](runtime.md#rt-rte-context-recall).

### Failure, rejection and recovery

**Malformed generation output** follows the most direct failure path in this workflow. After the bounded correction attempt fails, synthesis writes an error and returns a successful unit result without a proposal. Validation failure similarly logs and returns. These branches do not write the synthesis watermark, leaving the document eligible for a later dirty-document processing attempt; eligibility is not an autonomous retry guarantee. The kick can nevertheless label an `Ok(())` result `ingested`. A successful kick ledger value therefore cannot certify that useful knowledge was produced. Empty validated output, unlike failure, does write the watermark. SRC-1, `src-tauri/src/librarian/synthesis.rs`, `src-tauri/src/wisdom_deposit.rs`; [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis).

> let msg = format!("synthesis JSON failure for {source_path}: {e:#}");
>             write_synthesis_error(vault_root, &msg);
>             return Ok(());
> --- `src-tauri/src/librarian/synthesis.rs`

**A vanished evidence source can veto automatic admission.** The shared transaction checks deleted-source provenance for auto-approval. Synthesis recognizes the typed refusal, checks whether the proposal remains pending, and continues other bundles. A missing trigger document instead ends remaining writes; unrelated write errors propagate. Pending review is a recovery destination, not proof that a person subsequently resolved the item. Manual resolution is outside the auto-only guard, so the veto cannot be described as an absolute ban on admitting deleted-source material. SRC-1, `src-tauri/src/librarian/synthesis.rs`, `src-tauri/src/db/commit.rs`; [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission).

Recovery ownership is thus split among caller correction, worker/watcher progress, later librarian attempts and proposal review. Source inspection establishes these routes, not exactly-once completion or successful operation. No additional workflow components or routes are declared: the supplied runtime records already identify the consequential referents. Focused inspection covered the shipped skill and the deposit dispatch/kick, synthesis context, corrective retry, validation-return and vanished-source branches in SRC-1, `.skills/curated-thoughts/skill.md`, `src-tauri/src/wisdom_deposit.rs`, `src-tauri/src/librarian/synthesis.rs`.

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

#### On [RT-RTE-deposit-kick](runtime.md#rt-rte-deposit-kick)

Workflow milestone: the initial response acknowledges a durable source and scheduling state, not completion of the model/admission stages. Worker lock handoff requires watcher progress; it is not a second agent assigned the task-solving role.

#### On [RT-RTE-librarian-synthesis](runtime.md#rt-rte-librarian-synthesis)

Workflow verification boundary: one parse correction precedes item filtering. Logged failure without a watermark preserves later processing eligibility but can still appear successful to the kick's unit-result check. This separates scheduler completion from proposal production.

#### On [RT-RTE-proposal-admission](runtime.md#rt-rte-proposal-admission)

Workflow rejection/recovery boundary: automatic deleted-source refusal can leave an item pending while other bundles proceed. No supplied execution establishes that pending review was reached or completed. Transaction acceptance is not factual verification.

#### On [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

Workflow delivery boundary: commitment and later retrieval are separate invocations with no guaranteed selection of this deposit's derived entry. Returned selected context ends the inspected handoff; downstream agent use remains unobserved.
