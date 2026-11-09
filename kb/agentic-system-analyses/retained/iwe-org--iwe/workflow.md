---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "IWE workflow account: policy-guided session distillation through staged selection, strict writes, bookkeeping and later discovery."
run-id: AAS-2026-11-08-iwe-923f804db3b4-01
reviewed-boundary: "930c184b7cc8508d207e6ca7999ca6e415bc02ac"
---

# IWE workflow report

## Workflow account

### Selection and evidence limit

The representative workflow is distilling several conversation sessions into selected memory documents. It is selected because the shipped Distill procedure explicitly connects a request, delegated reading, durable intermediate results, human admission, document writes and a final report. This is one prescribed workflow, not a reconstruction from unrelated tools. Its baseline is [RT-RTE-session-capture](runtime.md#rt-rte-session-capture). SRC-1, `crates/iwe/templates/claude/prompts/distill.md` supplies doctrine/design; `crates/iwe/src/internal/claude/session.rs` supplies implementation of supporting commands. Neither supplies an observed end-to-end run. The external host owns model calls, question controls, worker launch and actual compliance; IWE supplies instructions and document/bookkeeping services, not an enclosing agent scheduler.

### 1. Establish policy and scope

A user asks to distill the current session, named sessions or a backlog. The foreground agent is instructed to run `session brief`, obtaining MEMORY policy, policy check, knowledge filter, schemas, areas, recent documents and rejections. A nonzero result means stop rather than invent a policy; policy-check problems go to user-assisted repair. The agent then lists sessions and obtains scope in user turns, excluding other active conversations unless named. Adoption is a separate deliberate bypass of reading, not evidence that an adopted conversation was reviewed. These are procedural decisions, not independently enforced user authorization. SRC-1, `crates/iwe/templates/claude/prompts/distill.md`; [RT-RTE-session-capture](runtime.md#rt-rte-session-capture).

> A non-zero exit means memory is not enabled here: do not improvise a policy, `/iwe:init` turns it on. A policy check that is not `ok` is fixed with the user first (§8).
> --- `crates/iwe/templates/claude/prompts/distill.md`

### 2. Delegate reading, not admission

For multiple sessions the foreground agent is told to delegate one session to each subagent. The handoff supplies one session ID, the policy's capture, shape and dedup sections, and the brief's knowledge filter. Each reader runs only the read-and-stage section and stops. It does not receive authority under this procedure to select or write memory documents. The foreground agent remains responsible for cross-session merging and asking the user. SRC-1, `crates/iwe/templates/claude/prompts/distill.md`; [RT-RTE-session-capture](runtime.md#rt-rte-session-capture).

> **More than one session: one subagent each.** Reading is the long half and nobody has to sit through it. Give each subagent one session id, the policy's "what to capture", "how to write it" and "dedup and updates" sections, and the knowledge filter from the brief; have it run this section for its session and stop there. Each stages into its own session record, so parallel readers never collide.
> --- `crates/iwe/templates/claude/prompts/distill.md`

The final sentence is the source's isolation claim about the per-session output convention, not demonstrated concurrency safety. Separate session records prevent the instructed readers from intentionally sharing an output record; they do not establish filesystem transactions or host context isolation. The host must implement launches and decide what worker messages return. The prescribed durable return is staged proposals, not entire worker reasoning. The foreground agent need not load each worker's transcript. No IWE-owned disposal or compaction of host windows is established.

Readers prefer already-held current-session context; otherwise `session read` supplies a bounded transcript window and coverage header. The instructed reader repeats from `covers_lines`, proposes only quotable policy-relevant candidates, searches the store for same-fact duplicates, retrieves plausible matches, stages each candidate, and records coverage with `complete --lines ... --offered ...`. The latter advances read progress before selection; it does not mean documents were admitted. The inbox preserves unfinished candidates across interruption or host compaction. SRC-1, `crates/iwe/templates/claude/prompts/distill.md`, `crates/iwe/src/internal/claude/session.rs`; [RT-OBJ-session-record](runtime.md#rt-obj-session-record).

### 3. Transform worker output before the user decides

The foreground agent requests the grouped inbox. Code groups pending entries by target key and prints contributor counts and summaries; the agent is then instructed to merge each group into one candidate retaining every contributing session's evidence. The group listing is not itself a merged, fully evidenced candidate: evidence requires the per-session inbox when needed. This consequential transformation is [WF-RTE-inbox-selection](#wf-rte-inbox-selection).

The user can keep all, skip all or pick. Five or fewer candidates are presented individually; larger sets use a numbered list with batch disposition controls or a plain-text equivalent. Edits are instructions: they can change a key, merge candidates or exclude a subject. All answers precede all document writes. A key-changing edit requires renewed lookup and later settlement of the old staged title as rewritten. The user is the admission decision-maker; the foreground agent owns applying that decision. No expected-answer oracle checks truth: user selection is consent within the procedure, while policy/evidence/dedup guide the proposal. SRC-1, `crates/iwe/templates/claude/prompts/distill.md`; [RT-RTE-session-capture](runtime.md#rt-rte-session-capture).

### 4. Write and handle rejection

After selection, the foreground agent reads a recent full document for body conventions and writes the selected new or merged content through strict CLI create/update. It must follow the policy without inventing fields or areas. Schema rejection is a software gate on these strict calls; the agent is instructed to repair the item, not remove the flag. SRC-1, `crates/iwe/templates/claude/prompts/distill.md`; [RT-RTE-cli-document](runtime.md#rt-rte-cli-document), [RT-BAP-schema-admission](runtime.md#rt-bap-schema-admission).

> `--strict` on every write. It enforces whatever the brief's schemas section names; when it fails, fix the item against the report, never drop the flag, and never pass `--set` alongside a template.
> --- `crates/iwe/templates/claude/prompts/distill.md`

User rejection has a different result: skip everything is valid, produces no memory documents and still requires completion bookkeeping. Unattended readers normally stop at staging, except for content already named in the instruction. Neither rule is a universal store-access invariant: direct CLI, MCP and editor routes exist without a selection token. [RT-CLM-capture-exclusivity](runtime.md#rt-clm-capture-exclusivity) bounds the prompt's exclusivity claim.

A post-create similarity report is after-write feedback, not a veto. The requested recovery is to read the match and, if it is the same fact, merge into the older document, delete the newer one and tell the user the surviving key. [RT-RTE-editor-reload](runtime.md#rt-rte-editor-reload) establishes the diagnostic path's limits. This requires another agent decision and further writes; no successful dedup or automatic undo is demonstrated. SRC-1, `crates/iwe/templates/claude/prompts/distill.md`.

### 5. Settle each contributing session and report delivery

After the last answer, the foreground agent calls completion for every contributing session, repeating written keys and meaningful rejected titles and finally dropping remaining pending proposals. A merged candidate must settle in every contributing record. Dropping pending proposals prematurely would record unasked items as rejected; the code cannot infer whether a user actually saw them. This is an ordering requirement on the foreground agent, not a question-history check. SRC-1, `crates/iwe/templates/claude/prompts/distill.md`; [RT-RTE-session-capture](runtime.md#rt-rte-session-capture).

Completion resolves written links, links eligible area hubs, settles proposals, updates the ledger and saves the session record. Document writes and record saving are separate. The implementation performs hub linking before saving the record; a record-save failure returns an error without undoing the already-written documents or demonstrating rollback of hub effects. Recovery therefore needs reconciliation of existing documents and pending records, not blind assumption that an error means nothing was written. SRC-1, `crates/iwe/src/internal/claude/session.rs`; see the workflow annotation below.

Delivery under the procedure means the selected files exist, session outcomes have been recorded, and the agent names new/updated keys, remaining inbox entries and backlog. It does not commit the files. Later discovery is a distinct handoff: [RT-RTE-session-index](runtime.md#rt-rte-session-index) emits selected metadata and optional policy, then explicit retrieval can supply bodies through [RT-RTE-document-retrieval](runtime.md#rt-rte-document-retrieval). The delivered document label alone does not establish visibility, full-body injection, model compliance or benefit. SRC-1, `crates/iwe/templates/claude/prompts/distill.md`.

> Name each key written, new or updated, anything still staged in the inbox, and what is left in the backlog. Nothing commits: the documents are files in the store the user reviews.
> --- `crates/iwe/templates/claude/prompts/distill.md`

### Added inspection coverage

This member read the complete SRC-1 Distill prompt and inspected `crates/iwe/src/internal/claude/session.rs` at `session_read`, `session_stage`, `grouped_inbox` and `session_complete`. These add implementation detail about the reader-to-foreground projection and settlement failure boundary to the supplied baseline. They establish no execution trace. The optional policy-feedback step remains characterized by [RT-RTE-policy-maintenance](runtime.md#rt-rte-policy-maintenance), rather than being assumed to occur on every capture run.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-inbox-selection
Label: Grouped inbox selection handoff

Part of: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

This is the material reader-output-to-user-selection subroute of capture, not a second identity for the complete capture workflow. It operates on [RT-OBJ-session-record](runtime.md#rt-obj-session-record). Endpoints: pending per-session proposals → grouped inbox output → foreground synthesis → user disposition. Code owns grouping; the foreground agent owns evidence-preserving merge and presentation; the user can keep, edit or veto. Operating mode: open user-requested capture, not an experiment. Answer oracle: inapplicable — user preference supplies admission, not a known correct factual answer. Guidance is the store policy plus the Distill procedure. Proposed changes are new/updated memory documents; rejection leaves them unwritten under the procedure and is later recorded. Recovery is resuming durable pending entries; no transaction encloses selection and later writes. SRC-1, `crates/iwe/src/internal/claude/session.rs` (implementation), `crates/iwe/templates/claude/prompts/distill.md` (doctrine/design).

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: grouped inbox prints target keys, contributor counts, titles, classification, new/update shape and proposal summaries; per-session inbox is requested for evidence detail.
- Later read-back: pending proposals remain in session records for resumed selection until explicitly settled or dropped.
- Delegated visibility: reader outputs persist in separate session records; foreground receives the grouped projection, not automatically each reader's full context.
- Selection predicate: pending proposals grouped by `proposal.target()`, sorted by descending entry count then key; foreground instructed to merge by candidate key before user decision.
- Invalidation or expiry: completion settles written keys/rejected titles and optionally rejects everything remaining pending; no automatic expiry established here.
- Activation or effect: code wires grouped output; the host is instructed to turn that output into user-approved writes, without an enforced approval token.
- Evidence limits: grouped output is not evidence-complete synthesis; agent merge, user interaction, worker isolation and actual writes are unobserved.

> groups
>     .entry(proposal.target().to_string())
>     .or_default()
>     .push((record.session.as_str(), proposal));
> --- `crates/iwe/src/internal/claude/session.rs`

> `session inbox <id>` prints one session's staged proposals with their evidence\n
> --- `crates/iwe/src/internal/claude/session.rs`

> Merge each such group into a single candidate whose evidence names every contributing session and line range.
> --- `crates/iwe/templates/claude/prompts/distill.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)

Workflow failure boundary: `session_complete` calls `link_into_hubs` before record save. Its error return does not establish that earlier document or hub writes were undone. The foreground agent owns recovery and must not equate completed document writes with completed bookkeeping. This adds a workflow ordering limit, not a new referent. SRC-1, `crates/iwe/src/internal/claude/session.rs`.

> let keys = resolve_links(store, &complete.wrote)?;
> let linked = link_into_hubs(store, &keys);
> --- `crates/iwe/src/internal/claude/session.rs`

> if !save_session_record(&record) {
>     return Err(format!(
>         "could not write the session record for {}",
>         session
>     ));
> }
> --- `crates/iwe/src/internal/claude/session.rs:567-708`
