---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Pi Posthorse memory: caller-maintained notes, projection-sensitive automatic recovery and bounded journal reload across retain-none windows."
run-id: AAS-2026-10-14-pi-posthorse-58b9647d2f29-01
source-identity: https://github.com/fitchmultz/pi-posthorse
reviewed-boundary: "307ef6bf05bc8bd8d718725761ffdf2f2ef72539"
---

# Pi Posthorse memory report

## Boundary and evidence

This report covers the extension's note storage, handoffs, automatic recovery construction, journal normalization, archive membership, retrieval budgets and reminder retention. The frozen source is SRC-1 at commit **307ef6bf05bc8bd8d718725761ffdf2f2ef72539**, as registered in [boundary](boundary.md#source-register). Pi owns model execution, journal persistence, compaction projection and external editors. Their implementations and deployment permissions are excluded; the extension's code establishes proposed and delivered memory paths, not independently certified host persistence or successful continuation.

Direct reads covered complete `index.ts`, `package.json`, `ui.ts`, `docs/reference.md`, `src/contracts.ts`, `src/context-tools.ts`, `src/budget.ts`, `src/rollover.ts`, `src/reminders.ts`, `src/notes.ts`, `src/files.ts`, `src/recovery.ts`, `src/recovery-results.ts`, `src/history.ts`, `src/history-entries.ts`, `src/history-search.ts`, `src/session-files.ts`, `src/history-pages.ts`, `src/paging.ts`, `src/message-text.ts`, `src/ui/cards.ts` and `src/ui/display.ts`. These are implementation or doctrine/design evidence from SRC-1. A bounded direct read of `test/official.test.mjs`'s reset/read/reopen scenario and a declaration/search inventory add evaluator-design evidence only. Runtime findings below are supplied records, independently checked at the named source paths where consequential. No target was executed and no observed trace or causal experiment was supplied.

| Entry point or operation | Source path, SRC-1 | Coverage and conclusion limits |
| --- | --- | --- |
| Package/SDK factory and registered tools | `package.json`, `index.ts`, `src/context-tools.ts`, `src/notes.ts`, `src/history.ts` | Direct reads establish all four registered tools and hook installation; [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset), [RT-RTE-request-guidance](runtime.md#rt-rte-request-guidance). No independent shipped service/CLI memory consumer is declared by the package; host loading and tool activation remain external. |
| Note creation, replacement, append and empty clear | `src/notes.ts`, `src/files.ts` | Direct reads; [MEM-OBJ-notes](#mem-obj-notes), annotation on [RT-RTE-note-admission](runtime.md#rt-rte-note-admission). Caller content admission is distinct from I/O admission. |
| External sectional editing | `src/budget.ts`, `docs/reference.md` | Direct doctrine reads; [MEM-OBJ-notes](#mem-obj-notes). Explicitly afforded writer, with editor permissions, approval policy and implementation uninspected; no tool-publication guarantee extends to it. |
| Location resolution and checkout migration | `src/files.ts` | Direct read; [MEM-RTE-notes-migration](#mem-rte-notes-migration). Moves preserve content rather than evaluate it; per-project installed-package protection is limited. |
| Explicit handoff and native/manual alternative | `src/context-tools.ts`, `src/rollover.ts`, `src/history-entries.ts` | Direct reads; [MEM-OBJ-explicit-handoff](#mem-obj-explicit-handoff), [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset). Native summary creation remains host-owned; its existing checkpoint is consumed, not silently excluded. |
| Automatic native hook and threshold fallback | `src/rollover.ts`, `src/recovery.ts`, `src/recovery-results.ts` | Direct reads; [MEM-OBJ-recovery-record](#mem-obj-recovery-record), annotation on [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery). Supported custom construction is code-decided; manual/unsupported cases and later competing handlers prevent a universal summary-free guarantee. |
| Context edits, legacy windows, result provenance | `src/recovery.ts`, `src/history-entries.ts`, `src/recovery-results.ts` | Direct reads; [MEM-OBJ-session-journal](#mem-obj-session-journal), [MEM-OBJ-recovery-record](#mem-obj-recovery-record). Raw originals remain retrievable after projection withdrawal. |
| Notes list/read/search | `src/notes.ts`, `src/paging.ts` | Direct reads; [MEM-RTE-notes-recall](#mem-rte-notes-recall). Literal selection, binary/size exclusions and live offsets constrain completeness. |
| Current-branch and project/subagent archive history | `src/history.ts`, `src/history-search.ts`, `src/session-files.ts`, `src/history-entries.ts`, `src/history-pages.ts`, `src/message-text.ts` | Direct reads; [MEM-RTE-history-recall](#mem-rte-history-recall). Normalized accessible entry types, not every raw byte or arbitrary project, reach the model. |
| Shared budgets, request guidance, reminder filtering | `src/paging.ts`, `src/budget.ts`, `src/rollover.ts`, `src/reminders.ts` | Direct reads; [RT-CMP-page-reservations](runtime.md#rt-cmp-page-reservations), annotations below. Request guidance is regenerated; reminder records and fingerprints are retained. |
| Operator cards and display metadata | `ui.ts`, `src/ui/cards.ts`, `src/ui/display.ts`, `src/contracts.ts` | Direct reads; [MEM-OBJ-posthorse-display](#mem-obj-posthorse-display). Collapsed preview differs from returned content; expansion does not fetch unseen pages. |
| Shipped evaluator read/reopen | `test/official.test.mjs` | Direct bounded scenario read plus search inventory; intended preservation checks, not suite-pass or behavioral benefit evidence. Remaining evaluator bodies are available but uninspected here. |

## Core ideas

Posthorse separates a small active window from two longer-lived stores: caller-maintained plaintext notes and the host journal. A handoff reaches the next invocation automatically; notes and detailed history require explicit calls. Reset does not automatically select a task note or restore its linked evidence ([RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset), [MEM-RTE-notes-recall](#mem-rte-notes-recall), [MEM-RTE-history-recall](#mem-rte-history-recall)).

Its automatic record is a deterministic transformation of traces, not a model's progress summary. Source roles, projection edits, provenance links, recency and character budgets determine what survives. The next model gets selected inputs, bounded receipts, history references and warnings. It does not get certified task status. Nonautomatic checkpoints can still carry model-authored interpretation into a later recovery record ([MEM-OBJ-recovery-record](#mem-obj-recovery-record)). Thus “no summaries” describes the supported custom construction path, not all retained material or all host compaction.

Read-back applies fixed symbolic selection to literal text and IDs; no embedding or similarity ranking is needed to explain the inspected selectors. Recalled prose can nevertheless influence future model decisions. Selection and publication do not validate truth, current relevance or compliance with safety constraints ([MEM-BAP-recalled-content](#mem-bap-recalled-content); SRC-1, `src/notes.ts`, `src/history-search.ts`, `src/budget.ts`).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-notes
Label: Durable notes

Source-native identity: text files at `notesDir(ctx.cwd)`. Representational form: caller-authored plaintext, generally natural-language task state; arbitrary file content is possible and its semantic form is not fixed by the tool. Storage substrate: `.pi/notes` at the shared Git root/common directory, local cwd outside Git, or agent-directory package notes. Lineage: caller/model creation, whole replacement, newline append, external editor revisions and content-preserving migration. Imported/pre-existing note authorship is unresolved; it does not prevent tracing subsequent writes and reads (SRC-1, `src/notes.ts`, `src/files.ts`, `docs/reference.md`).

This is the persistent result of [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), not another declaration of that route. There is no supplied persistent note object counterpart. Readers are later notes tools, filesystem editors and ultimately the foreground model. Filesystem selection treats paths and timestamps symbolically; retrieved task prose exercises model-interpreted authority, not an executable correctness gate. Notes may preserve decisions and reasons if the author supplies them, but there is no required rationale field or implemented rationale evaluator. [MEM-RTE-notes-recall](#mem-rte-notes-recall) can read that rationale as ordinary text.

> Prefer available file-editing tools for changed sections of one concise current-state note; write for creation or substantial restructuring. Link fuller evidence instead of copying them.
> --- `src/notes.ts`

This is requested curation, not evidence that authors actually maintain concise or true state. Replacement overwrites the retained content; empty replacement clears it. Append does not reconcile contradictions. The tool schema supplies no delete operation; external editors/filesystem actions can withdraw content, and raw earlier content may survive in the host's tool-call journal. No automatic semantic expiry is established by the inspected note callbacks (SRC-1, `src/notes.ts`, `src/history-entries.ts`).

#### MEM-OBJ-session-journal
Label: Session journal

Source-native identity: Pi branch entries and project-scoped `.jsonl` session files, consumed through `sessionManager` and `sessionWindowEntries`. Representational form: symbolic entry IDs, parent links, kinds, scopes and replacement relationships; natural-language messages, summaries, thinking and tool arguments/results; stored image blocks are encoded media, not their readable count/MIME summaries. Storage substrate: external host session files, with in-process branch/projection access. Lineage: host-persisted inputs and outputs, custom reminders, compaction records and context-edit entries. Provider/host generation and persistence internals are uninspected (SRC-1, `src/history.ts`, `src/session-files.ts`, `src/history-entries.ts`, `src/message-text.ts`).

The supplied [RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval) consumes this object; no supplied journal object duplicates it. It contains raw traces and derived checkpoints, which must not be classified together as evaluated knowledge. Posthorse's normalization makes supported content readable but is not byte-for-byte replay: excluded shell output becomes a placeholder; unknown entry types and malformed lines do not produce readable entries. Original and replacement IDs expose different versions. Active projection withdrawal is not deletion from this archive (SRC-1, `src/history-entries.ts`, `src/session-files.ts`).

> return "[bashExecution] (excluded from model context by Pi)";
> --- `src/history-entries.ts`

IDs/window ancestry are access metadata consumed by fixed rules. Normalized selected text/images are tool-result input to the current model, under the host's role semantics, not inherently fresh owner instructions. Archive descendants receive a subagent label based on nested file location; Posthorse does not launch or initialize their contexts (SRC-1, `src/message-text.ts`, `src/session-files.ts`).

#### MEM-OBJ-explicit-handoff
Label: Explicit continuation handoff

Part of: [RT-RTE-explicit-reset](runtime.md#rt-rte-explicit-reset)

This object is the route's retained output payload, not the route's ID-authorization map [RT-OBJ-reset-requests](runtime.md#rt-obj-reset-requests). Source-native identity: trimmed `new_context.handoff`, or `EMPTY_HANDOFF`, written to the admitted compaction `summary`. Representational form: natural-language continuation prose. Storage substrate: host compaction journal entry and later projected summary message. Lineage: foreground caller/model formulation; absence/blankness substitutes a fixed restoration instruction. Earlier note writes need not be included in this text (SRC-1, `src/context-tools.ts`, `src/contracts.ts`, `src/rollover.ts`).

> export const EMPTY_HANDOFF = "Fresh context. Restore relevant notes and history before continuing.";
> --- `src/contracts.ts`

The future model reads this payload automatically if Pi commits and continues. Callback/turn-end checks admit size and origin, not truth or completeness. The author may retain reasons and constraints, but no mandatory rationale preservation exists. History can later retrieve the compaction entry; further automatic recovery can reuse this as a possibly stale nonautomatic checkpoint ([MEM-OBJ-recovery-record](#mem-obj-recovery-record); SRC-1, `src/recovery.ts`, `src/history-entries.ts`).

#### MEM-OBJ-recovery-record
Label: Automatic recovery record

Part of: [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery)

This is the automatic route's derived payload, distinct from the explicit handoff above and the host-control protocol [RT-BAP-compaction-draft](runtime.md#rt-bap-compaction-draft). Source-native identity: `buildAutoHandoff` output. Storage substrate: admitted host compaction summary; legacy `context_window.handoff` is an alternative historical checkpoint representation. Representational form has two consumption parts: natural-language input/receipt excerpts and fixed warnings interpreted by the future model; symbolic entry references, labels and timestamps that support explicit retrieval. Neither image count summaries nor result headers contain the full original media/result (SRC-1, `src/recovery.ts`, `src/recovery-results.ts`, `src/history-entries.ts`).

Lineage is raw branch input → projected omission/replacement and tool provenance filtering → anchor/index/receipt selection → bounded derived record → host commit → later model and, on later automatic rollover, checkpoint ancestry selection. Direct user inputs, linked successful registered unnamespaced `ask_question` outcomes and visible non-reminder coordination have distinct roles. Tool receipts include errors, requested/admitted arguments when available and missing-call warnings; eligibility does not certify successful action. Current synchronous linked receipts come from the trailing batch; projected orphan and legacy async receipts remain possible even outside it (SRC-1, `src/recovery.ts`, `src/recovery-results.ts`).

> // Only projected provenance is eligible. Orphans never resurrect a raw call.
> return index > start || call === undefined || call.block.async === true;
> --- `src/recovery-results.ts`

Anchor selection preserves first direct-owner request (or first input fallback), latest owner and latest overall input. Other current inputs receive a budgeted index, newest fitting lines retained but displayed chronologically. Each anchor/checkpoint excerpt is capped at 4,000 characters; result excerpts at 1,500. Middle omission, header-only results, omitted older result headers and unlisted inputs prevent completeness. Shared payload allocation reserves 1,000 characters of overhead and then checks final size at admission (SRC-1, `src/recovery.ts`, `src/rollover.ts`).

> const MAX_RECOVERY_RECORD_CHARS = 4_000;
> const MAX_RECOVERY_RESULT_CHARS = 1_500;
> const HANDOFF_OVERHEAD_RESERVE = 1_000;
> --- `src/recovery.ts`

Consecutive automatic records are not nested wholesale. An ancestry walk stops at a nearer window with recoverable owner inputs or a nonautomatic checkpoint. A current window with no owner inputs carries selected earlier owner anchors, labels them possibly already handled, and points to skipped automatic records. Earlier tool evidence is not recursively copied. Explicit/native summaries can survive as bounded, possibly stale checkpoints. Automatic output retains source references and warning reasons, but not necessarily complete original rationale; later history read is needed for omitted evidence. Actual model reliance and improved capacity are unobserved (SRC-1, `src/recovery.ts`, `src/message-text.ts`).

#### MEM-OBJ-posthorse-display
Label: Posthorse display metadata

Source-native identity: `PosthorseDisplay`, attached as result `details`. Representational form: symbolic kind tags, counts, spans, offsets and usage facts. Storage substrate: returned tool-result metadata, with any subsequent persistence owned by Pi. Lineage: note/history page construction and context/write callbacks. Consumer: operator-facing renderers, not a second semantic memory payload. This is distinct from [RT-CMP-page-reservations](runtime.md#rt-cmp-page-reservations), which controls admission, and from [MEM-OBJ-session-journal](#mem-obj-session-journal), which may contain the host's saved tool result (SRC-1, `src/contracts.ts`, `src/ui/display.ts`, `src/ui/cards.ts`).

> /** Display-only facts and offsets into content, never a second copy of a note or history page. */
> --- `src/ui/display.ts`

Collapsed cards elide headers/content and show short previews; expanded cards show the returned page, metadata and submitted note/handoff. They do not load missing pages. Image display can be hidden while tool content still contains attached images. Saved legacy results lacking recognized metadata fall back to raw presentation. The model-facing text/image result is separate from this display summary (SRC-1, `src/ui/cards.ts`, `src/contracts.ts`, `docs/reference.md`).

### Routes

#### MEM-RTE-notes-migration
Label: Notes location migration

Endpoints/progression: notes callback → `notesDir(cwd)` → Git/common-root and package-location resolution → move old checkout folder and install compatibility link → returned shared location. Owner: Posthorse code selects and moves; OS grants determine physical success. This is a storage-maintenance route associated with [RT-RTE-note-admission](runtime.md#rt-rte-note-admission), not contained in its write-only referent: reads/list/search also trigger resolution (SRC-1, `src/files.ts`, `src/notes.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Resolved notes directory; move/link errors can propagate, while a concurrent successful move or compatibility-link-only failure is tolerated.
- Later read-back: Subsequent notes operations and old sessions via the link can reach moved content; when destination exists, old files move into a distinct `from-checkout-<time>` folder rather than merging.
- Delegated visibility: Shared roots can be accessed by other worktrees/processes under OS permissions; no delegate-specific content delivery is performed.
- Selection predicate: Ascend to Git marker/common directory; agent-installed Git checkout inside agent `git` tree gets corresponding agent `notes` location; an existing real local notes directory triggers relocation.
- Invalidation or expiry: Package updates may remove the old compatibility link; migrated storage survives the checkout cleanup under the documented installation contract. Missing/orphaned metadata falls back to local storage.
- Activation or effect: Changes storage and future addressing, preserving text without semantic evaluation.
- Evidence limits: Per-project `.pi/git` packages remain checkout-local; tracked package notes may recur on update. No actual migration, concurrent-race or update trace was supplied.

Admission is automatic software maintenance, not human per-note approval; authorship remains unchanged. Failure does not offer semantic rollback. Existing destination content is kept separately, not overwritten by a merge (SRC-1, `src/files.ts`).

> const target = existsSync(moved) ? join(moved, `from-checkout-${Date.now()}`) : moved;
> --- `src/files.ts`

#### MEM-RTE-notes-recall
Label: Notes recall

Part of: [RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval)

Endpoints/progression: foreground caller path/query/offset → live filesystem traversal or exact-file read → literal line matching/page sizing → tool text → current model. Owner: caller requests; Posthorse orders, filters and pages; Pi delivers. This route is the notes part of the combined supplied route, with different substrate/filters from history (SRC-1, `src/notes.ts`, `src/files.ts`, `src/paging.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Bounded text page, newest-modified file listing or matching `path:line` excerpts, with absolute location and continuation offset when relevant; capacity/errors can refuse delivery.
- Later read-back: Retained notes reach a later invocation when explicitly requested; there is no automatic task-note reload at reset.
- Delegated visibility: uninspected — shared OS storage enables access but this callback returns to its invoking foreground context, not a separately initialized delegate.
- Selection predicate: Exact path for read; optional folder for list; case-insensitive literal substring for search across newest-modified notes. Search skips binary files and files over 1 MiB and caps continuation offsets below 1,000,000.
- Invalidation or expiry: Live content and ordering can change between calls; offsets are not revision-pinned. Budget reservations expire at turn/session reset, not note content.
- Activation or effect: Returned text enters a host tool result; influence on later task decisions is possible but unobserved.
- Evidence limits: Search omissions, partial excerpts, symlink traversal and external mutation prevent exhaustive or immutable recall. NUL-prefix binary detection is a heuristic, not a text schema.

Selection is requested, not an independent push. File mtime influences order, not task relevance or truth. Read can retrieve a large text file page even though search excludes that file by size. Notes support episodes or sessions sharing the root, with no encoded task/session expiry. Tool budget is at most 40,000 characters, shrinks with current capacity and shares sibling reservations with history (SRC-1, `src/notes.ts`, `src/paging.ts`, `src/contracts.ts`).

> /** Larger files are logs or evidence rather than notes; reading them would dominate a search. */
> const SEARCH_FILE_BYTES = 1024 * 1024;
> --- `src/notes.ts`

#### MEM-RTE-history-recall
Label: History recall

Part of: [RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval)

Endpoints/progression: foreground query/scope/cursor or exact entry ID → branch/archive membership and normalization → priority/excerpt or text/image page → current model tool result. Owner: caller targets; Posthorse selects; Pi supplies current projection and delivery. This is the history part of the supplied route, not a duplicate combined declaration (SRC-1, `src/history.ts`, `src/history-search.ts`, `src/session-files.ts`, `src/history-entries.ts`, `src/history-pages.ts`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Search excerpts/IDs or normalized text and stored images with text/image continuation positions; invalid cursors, missing entries or unsafe budgets yield errors.
- Later read-back: Earlier raw or edited journal entries reach a later model invocation on explicit search/read, including prior checkpoints and reminders.
- Delegated visibility: `all: true` searches nested descendant session files whose parent belongs to this project; parent-agent inputs are tagged subagent material, not newly authenticated direct owner intent. It does not send foreground memory to those agents.
- Selection predicate: Search defaults to current branch; all-session search scans valid project-matching/current session files and inherited descendants, originals before recovery echoes, newest file modification then newest entry within priority. Exact read first resolves an unqualified ID in branch, otherwise scoped archive, optionally selected by file key.
- Invalidation or expiry: Cursor is tied to query/scope and anchor but not an immutable archive snapshot; changed/missing anchors require restart. Projection changes visibility exclusion; raw originals remain addressable.
- Activation or effect: Selected normalized text and image payloads enter current provider context as a tool result; actual behavioral reliance is unobserved.
- Evidence limits: Unknown entry kinds, malformed lines, excluded shell payloads and normalized omission mean this is not complete raw-journal replay. File membership/parent paths and short file keys are selectors, not cryptographic content provenance or an access-control sandbox.

Search excludes entries whose complete normalized content is already visible in projection; a changed-away original can remain searchable. Recovery material ranks after matching original content, including assistant entries mixing recovery tool calls with other text. `read` returns the whole normalized entry in pages rather than the search excerpt. Original IDs and replacement IDs can both resolve. Archive traversal excludes `.intent.` files and unsupported headers; current-branch access is a separate alternative. Optional ripgrep/line prefilters are accelerators, with failed runs retaining candidates; no measured full-scan equivalence claim is made here (SRC-1, `src/history-search.ts`, `src/history-entries.ts`, `src/session-files.ts`, `src/history.ts`).

> /** Files containing a needle, per ripgrep; files of a failed run stay candidates. */
> --- `src/session-files.ts`

Text/images share capacity: images cost an estimated 4,800 characters each; initial image reservation and separate `imageOffset` allow later image-only pages. Thinking text, requested tool arguments, admitted execution arguments when present and assistant failures can be recalled. Images are returned as stored image blocks, not inferred from their display summary (SRC-1, `src/contracts.ts`, `src/history-pages.ts`, `src/message-text.ts`).

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-recalled-content
Label: Recalled task content

Consumer: current foreground model. Channel: note/history tool-result text and images; host-projected explicit/automatic compaction summary. Force: model interpretation under host role semantics, not an executable task-validity gate. Horizon: later invocations/windows and, for notes/project archives, separate sessions sharing storage/scope. This differs from static/regenerated guidance in [RT-BAP-model-guidance](runtime.md#rt-bap-model-guidance): the content accumulates or changes through use. Symbolic projection/admission control remains [RT-BAP-compaction-draft](runtime.md#rt-bap-compaction-draft) (SRC-1, `src/history.ts`, `src/history-pages.ts`, `src/notes.ts`, `src/rollover.ts`, `docs/reference.md`).

> - Returned history content enters the currently selected model and provider context.
> --- `docs/reference.md`

Owner/coordination labels warn about trust, but do not mechanically prevent a model treating recalled text as an instruction. A successful write/read or result receipt proves neither truth nor current authorization. Guidance explicitly asks for live-state verification before stateful/external work; the later model's compliance is unobserved ([RT-OBJ-context-guidance](runtime.md#rt-obj-context-guidance), [MEM-OBJ-recovery-record](#mem-obj-recovery-record)).

## Annotations

#### On [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)

Retained result is [MEM-OBJ-notes](#mem-obj-notes). Caller/model authorship and software physical publication are separate; no required human content approval is visible in these callbacks. Software rejects invalid lexical paths, missing content, abort/failing publication, not false content. Replacement stages and renames at the resolved target; append performs a newline-terminated `O_APPEND` record. Pre-rename failures preserve the old file; temporary cleanup does not create a prior-content version for later rollback. Symlink targets and external editors are counterexamples to sandboxed or single-writer interpretations (SRC-1, `src/notes.ts`, `src/files.ts`).

Subsequent revisions may be trace-informed by the foreground model, but only the request to maintain task state is established; no implemented model reflection/evaluation cycle is inferred from the write label. Removal of the extension leaves notes in place by documented contract (SRC-1, `src/budget.ts`, `docs/reference.md`).

#### On [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery)

The durable derived result is [MEM-OBJ-recovery-record](#mem-obj-recovery-record), not an unchanged raw trace. Its next model consumer receives bounded text automatically through compaction projection, while further detail needs [MEM-RTE-history-recall](#mem-rte-history-recall). Trace origin is mixed direct user, provenance-checked owner answers, visible coordination and projected model/tool receipts; the selector is code, not a summarizer model. Fixed reasons warn that receipts/inputs are not current progress. Retained original reasons may be truncated and require history retrieval (SRC-1, `src/recovery.ts`, `src/recovery-results.ts`).

Automatic push is triggered by the reached host compaction hook or eligible threshold fallback. Its inputs are branch/projection, effective tool registration and fresh capacity. It selects bounded anchors, indices, receipts and checkpoint references before host persistence. This is an inspectable trace-fed artifact update with a later behavior-shaping channel; improved future capacity, exercised learning and reliable task restoration remain unestablished without operation evidence. Recovery-building failure cancels the custom boundary; sentinel append can outlive a later cancellation, so journal mutation is not completely rolled back (SRC-1, `src/rollover.ts`).

#### On [RT-RTE-request-guidance](runtime.md#rt-rte-request-guidance)

Guidance is regenerated, not learned memory. Reminder prose and symbolic fingerprints are host-retained records. Later reminder lookup reads them to suppress duplicates for the same window/context/reserve; projection filtering removes stale/disabled reminders from model input while leaving history recall available. Lookup cache is ephemeral, leaf-identity-certified, and invalidated on session/tree changes. Retained metadata therefore affects later code eligibility separately from reminder prose influencing the model (SRC-1, `src/reminders.ts`, `src/rollover.ts`).

#### On [RT-CMP-page-reservations](runtime.md#rt-cmp-page-reservations)

Reservations control memory delivery, but are not durable acquired knowledge. The 40,000-character cap, 1,000-token margin, text-length/4 estimate, current usage growth and fixed image estimate bound concurrent/serial recall. Unknown usage falls back to half fresh operational capacity after overhead. These controls cover notes/history, not arbitrary editors or transport/tool output. Refusal retains caller positions for retry and can omit error guidance when even that would not fit (SRC-1, `src/paging.ts`, `src/budget.ts`, `src/contracts.ts`).

## Write side

Note acquisition is caller-selected content: create/replace/append and externally afforded sectional edits. Curation is requested, not semantically enforced. Software admits physical writes; generic filesystem access does not establish human editorial approval. Content can be cleared or replaced without a semantic rollback ledger. Location migration preserves prior content separately instead of judging conflicts ([MEM-OBJ-notes](#mem-obj-notes), [MEM-RTE-notes-migration](#mem-rte-notes-migration)).

Automatic curation is different: raw journal → current/historical projection edits → owner/provenance and receipt filters → budgeted derived payload → admitted host checkpoint → next model. Rejected owner provenance can still survive as labeled tool evidence; edited-away data does not re-enter automatic recovery merely because it exists raw. Previous automatic payloads are not nested, but older explicit/native checkpoints are permitted. Therefore a conclusion that all recovery text is raw owner intent, or that no model-authored interpretation ever survives, would be false ([MEM-OBJ-recovery-record](#mem-obj-recovery-record); SRC-1, `src/recovery.ts`, `src/recovery-results.ts`).

Retain-none compaction discards old active input as a whole. The frame analogy fits a bounded continuation value escaping a removed window; it fails as a literal memory-reference model because IDs require explicit tools, not live references or automatic dereferencing. Note state remains outside the window. Context edits/filtering withdraw material from projection without deleting raw journal evidence. Nested subagent archives establish a recall surface, not an included subagent isolation or launch mechanism (SRC-1, `src/rollover.ts`, `src/history-entries.ts`, `src/session-files.ts`; [MEM-RTE-history-recall](#mem-rte-history-recall)).

Evaluation source contains intended restoration/reopening checks: the shipped faux-model scenario writes a note and handoff, reads notes/history in the fresh window, then opens the saved session and compares context messages. It does not judge task-state truth or establish that the scenario passed in this analysis. No inspected production route feeds evaluator scores back into note/recovery admission (SRC-1, `test/official.test.mjs`, `src/notes.ts`, `src/rollover.ts`).

> assert.match(textOf(toolResult(h, "notes")), /DURABLE_NEXT_STEP/);
> assert.match(textOf(toolResult(h, "history")), /RAW_ORIGINAL_OWNER/);
> --- `test/official.test.mjs`

## Read-back

Three channels are distinct. Explicit and automatic handoffs are automatically delivered as next-window summary input if the host commits. Notes/history are caller-requested recall; a reset does not itself reload all durable state. Persisted reminder metadata is code-read for eligibility, while reminder text is model-visible guidance or later historical recall. Display metadata supplies operator presentation, not another note/history body ([MEM-OBJ-explicit-handoff](#mem-obj-explicit-handoff), [MEM-OBJ-recovery-record](#mem-obj-recovery-record), [MEM-RTE-notes-recall](#mem-rte-notes-recall), [MEM-RTE-history-recall](#mem-rte-history-recall), annotation on [RT-RTE-request-guidance](runtime.md#rt-rte-request-guidance), [MEM-OBJ-posthorse-display](#mem-obj-posthorse-display)).

Targeting inputs are literal query, path, entry ID, cursor and project/branch scope, not inferred task relevance. Budgets constrain delivered parts, and the result may be a partial page, excerpt or image subset. Publication, delivery and behavioral activation remain separate. Rationale is retrievable only when originally retained and surviving normalization/paging; nothing forces a later agent to read linked reasons. Provider selection determines where recalled text/images go (SRC-1, `src/notes.ts`, `src/history-search.ts`, `src/history-pages.ts`, `docs/reference.md`).

## Integration issues

- No correction to a supplied runtime fact is required. Its provisional normalization/prefilter inspection limit is reduced by direct complete reads here; this does not independently prove exhaustive search equivalence or host correctness ([RT-RTE-retained-retrieval](runtime.md#rt-rte-retained-retrieval), [MEM-RTE-history-recall](#mem-rte-history-recall); SRC-1, `src/history-entries.ts`, `src/session-files.ts`).
- The two recall routes are declared parts of the combined runtime retrieval route; the two handoff objects are retained payload parts of their respective runtime routes. Notes/journal/display objects are new storage/content referents, not route duplicates. Migration spans read and write location resolution, so it is not merely a part of note-write admission. Reconciliation should preserve these distinctions; no possible-duplicate declaration remains after this comparison ([MEM-RTE-notes-recall](#mem-rte-notes-recall), [MEM-RTE-history-recall](#mem-rte-history-recall), [MEM-OBJ-explicit-handoff](#mem-obj-explicit-handoff), [MEM-OBJ-recovery-record](#mem-obj-recovery-record), [MEM-RTE-notes-migration](#mem-rte-notes-migration)).
- Initial imported note provenance, actual note reasons/revisions and deployed external-editor approval remain unknown. This prevents attributing all note content to autonomous model curation or human approval, without obscuring known later software writes ([MEM-OBJ-notes](#mem-obj-notes), [RT-RTE-note-admission](runtime.md#rt-rte-note-admission); SRC-1, `src/notes.ts`, `docs/reference.md`).
- Native/manual checkpoint authorship, host projection/persistence and legacy cross-host interpretation are external responsibilities. Existing native summaries are known later inputs, but their generation fidelity is not established. Later same-phase edits/competing handlers can displace the recovery proposal; a sentinel may remain after cancellation ([MEM-OBJ-recovery-record](#mem-obj-recovery-record), [RT-RTE-automatic-recovery](runtime.md#rt-rte-automatic-recovery); SRC-1, `src/recovery.ts`, `src/rollover.ts`, `docs/reference.md`).
- Actual retrieval reliance, successful restoration and any improved future capacity remain unobserved. Evaluator assertions are source design, not supplied results; generic retained-state wiring must not be promoted into reliable continuity or learning ([MEM-BAP-recalled-content](#mem-bap-recalled-content), [RT-CLM-context-continuation](runtime.md#rt-clm-context-continuation); SRC-1, `test/official.test.mjs`, `src/budget.ts`).

## Limitations and checks

Frozen checkout HEAD matched the boundary commit; `git status --short` was empty and `git diff --exit-code` passed. Source inspection was read-only. Required invocation, supplied members/types, worker rules and record contract were read completely; source reads were bounded and recovered where split. New declarations were compared with supplied records and retain separate consumers/forms rather than relabeling existing referents.

Counterexample checks retained manual/unsupported native compaction, old nonautomatic summaries, raw original recall after context edits, projected orphan/legacy async receipts, note search size omissions, symlink/editor bypasses, live cursors and late-hook cancellation/edit limits. These prevent stronger claims of summary-free universality, exact transcript replay, semantic admission, complete transactional rollback or enforced model compliance. No target tests/providers were run; remaining evaluator bodies, external persistence/editor implementations and actual provider behavior are uninspected, not absent.

Deterministic validation: `commonplace-run validate-output` passed for this invocation. This establishes structural identity, references and quotation occurrence, not semantic acceptance or observed runtime benefit.
