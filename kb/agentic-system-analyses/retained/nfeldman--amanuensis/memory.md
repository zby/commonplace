---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Amanuensis memory: revision-bound survey records, append-only explanations, bounded readers, carry obligations, task briefs and qualified policy state."
run-id: AAS-2026-11-08-amanuensis-b3a8e3e53488-01
source-identity: https://github.com/nfeldman/amanuensis
reviewed-boundary: a98093dc7aad3c0e64d42132ece305fc5ea7f3f9
---

# Amanuensis memory report

## Boundary and evidence

The memory boundary includes the shipped agent method, SQLite conspectus, registered prose, ordinary and alternative readers, maintenance and withdrawal, import from predecessor stores, derived task packets, and outcome-to-policy machinery. It follows the whole-system boundary, not just the principal database reader. The source is SRC-1 at `a98093dc7aad3c0e64d42132ece305fc5ea7f3f9`; the source register is in [boundary](boundary.md#source-register). Host model internals, private populated stores and actual host context assembly are outside the supplied evidence. No target code, tests or examples were executed.

Direct inspection added executable passages of tools `explanations.ts`, `artifacts.ts`, `field-notes.ts`, `stale.ts`, `logging.ts`, `claims.ts`, `findings.ts`, `carried.ts`, `codebase-brief.ts`, `learning.ts`, `research.ts`, `design-session.ts`, `subsystems.ts`, `locus.ts`, plus `invariants.ts` and `codebase-brief-contract.ts`, all under `mcp-server/src/`. The skill and notes reference supply doctrine/design, not observed compliance. CLI dispatch, server imports and the tracked source tree were checked against the runtime inventory. The other runtime findings remain supplied evidence, explicitly distinguished below. The source identity was rechecked with Git HEAD. Uninspected included parts remain visible in this table; inclusion is not a claim of completed tracing.

| Entry point or operation | SRC-1 source paths | Coverage and conclusion limit |
|---|---|---|
| Host entry, cold/warm start, phase isolation, resume | `.claude/skills/amanuensis/SKILL.md`, `.mcp.json`, `mcp-server/src/cli.ts` | Direct skill/registration reads and CLI dispatch search; [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle), [RT-OBJ-amanuensis-skill](runtime.md#rt-obj-amanuensis-skill). Host enforcement remains uninspected. CLI dispatch is install/upgrade/doctor/uninstall, not a separate semantic-memory query loop. No hook implementation was identified in the inspected `.claude/` tracked inventory; this is not a system-wide absence claim. |
| Bound MCP and alternate handler executor | `mcp-server/src/index.ts`, `mcp-server/src/tools/chorusmith-adapter.ts` | Import inventory directly checked; admission bypass and binding supplied by [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch). Adapter's entire state/export/recovery chain is uninspected here; no universal outer-schema guarantee. |
| Typed claims and findings, correction and resolution | `mcp-server/src/tools/claims.ts`, `mcp-server/src/tools/findings.ts` | Direct writer, invalidation, successor, reader and fix-verification passages; [MEM-OBJ-claims](#mem-obj-claims), [MEM-OBJ-findings](#mem-obj-findings), [MEM-RTE-knowledge-revision](#mem-rte-knowledge-revision). Challenge internals and full resolution audit remain uninspected. |
| Purpose/account, declination and reset | `mcp-server/src/tools/explanations.ts`, `mcp-server/src/invariants.ts`, `mcp-server/src/tools/subsystems.ts` | Direct reads; [MEM-OBJ-explanations](#mem-obj-explanations), [MEM-RTE-explanation-cycle](#mem-rte-explanation-cycle). No semantic truth guarantee from admission. |
| Field notes and prose | `mcp-server/src/tools/field-notes.ts`, `mcp-server/src/tools/artifacts.ts`, `.claude/skills/amanuensis/references/notes.md` | Direct reads; [MEM-OBJ-field-notes](#mem-obj-field-notes), [MEM-OBJ-prose-artifacts](#mem-obj-prose-artifacts). File registration is not content approval. |
| File staleness, heat and demand | `mcp-server/src/tools/stale.ts`, `mcp-server/src/tools/logging.ts` | Direct reads; [MEM-OBJ-file-ledger](#mem-obj-file-ledger), [MEM-OBJ-query-log](#mem-obj-query-log), [MEM-OBJ-access-log](#mem-obj-access-log). Full `git.ts` change detection and `files.ts` initial admission are not traced; initial human content control remains unresolved. |
| Requested locus/attention/history | `mcp-server/src/tools/locus.ts` | Direct budget and public-tool passages plus supplied [RT-RTE-locus-read](runtime.md#rt-rte-locus-read); annotation below. Detailed builders for every record class remain uninspected, preventing a completeness claim about delivery of every stored field. |
| Checkpoint and restart; rebuild carry | `mcp-server/src/tools/storage-history.ts`, `dev/rebuild-self-conspectus-store.mjs`, `mcp-server/src/tools/carried.ts` | Checkpoint/rebuild caller supplied by boundary/runtime; carry and outcome handlers directly read. [MEM-OBJ-carried-findings](#mem-obj-carried-findings), [MEM-RTE-carry-recheck](#mem-rte-carry-recheck). Archive authentication and all driver recovery branches are uninspected. |
| Human publication and verification | `mcp-server/src/tools/materialize.ts`, `materializer/materialize.py`, `materializer/amanuensis_materializer/core.py` | Supplied [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication). No second declaration; ordinary, clean and verification-disabled paths retain runtime's distinct guarantees. Per-page projection fields remain uninspected here. |
| Review-to-task context and design delivery | `mcp-server/src/tools/codebase-brief.ts`, `mcp-server/src/codebase-brief-contract.ts`, `mcp-server/src/tools/design-session.ts` | Direct preparation/compiler/lookup and packet delivery reads; [MEM-OBJ-codebase-brief](#mem-obj-codebase-brief), [MEM-RTE-brief-delivery](#mem-rte-brief-delivery). Review source compilation and design output aggregation are not fully traced. |
| External research landing and consumption | `mcp-server/src/tools/research.ts` | Direct landing/consumption/get reads; [MEM-OBJ-research-results](#mem-obj-research-results), [MEM-RTE-research-consumption](#mem-rte-research-consumption). Proposal admission, external execution and dispatch budget enforcement are uninspected. |
| Outcome extraction, lessons and policy | `mcp-server/src/tools/learning.ts`, `mcp-server/src/tools/crosswalk.ts` | Direct terminal-source/extraction/proposal/runtime reader/ledger reads; [MEM-OBJ-learning-lessons](#mem-obj-learning-lessons), [MEM-OBJ-learning-policy](#mem-obj-learning-policy), annotation on [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission). Full qualification supplied only by runtime; downstream host adoption unresolved. |
| Additional included state and alternative paths | `mcp-server/src/tools/evidence.ts`, `dispositions.ts`, `concerns.ts`, `vocabulary.ts`, `open-questions.ts`, `contradictions.ts`, `seams.ts`, `xrefs.ts`, `dispatch.ts`, `dashboard.ts`, `compare.ts` | Identified through server registration and supplied skill/runtime; detailed handlers uninspected except supplied findings. These include evidence links, glossary, questions, contradictions, seam/xref relationships, resume traces and comparisons. Cannot establish every admission, withdrawal or read-back rule from the principal reader alone. |
| Controlled review, composition and refresh/revalidation | `mcp-server/src/tools/review.ts`, `review-analysis.ts`, `review-session.ts`, `composition.ts`, `diagnosticity.ts`, `impact.ts`, `revalidation.ts`, `refresh.ts`, `resolution.ts` | Registered surfaces inventoried; named plan/dispatch/land/score/reconcile and review/export tools located by bounded search. Full packet construction, cancellation, failed-result retention and downstream eligibility remain uninspected. No inference that all are equivalent to ordinary survey admission. |
| Decisions and crosswalk registry | `mcp-server/src/tools/decisions.ts`, `crosswalk.ts`, `schema.sql` | Supplied [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) and [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission); projection payload details and registry consumers unresolved. |
| Evaluation and development drivers | `mcp-server/src/tools/evaluation.ts`, `mcp-server/scripts/historical-evaluation.mjs`, `dev/`, `design/`, `scholiast/` | Evaluation tool names and schema table inventory inspected; historical driver role supplied by boundary. Landed results, envelope reports/rebaselines and embedded trials are included but not used as operation evidence here. No effectiveness, causal benefit or exhaustive driver-consumer conclusion. |

## Core ideas

Amanuensis retains a codebase account, not just a conversation transcript. Typed records bind prose to evidence, revision and workflow standing. A later model is instructed to answer from that standing rather than replace an empty record with an improvised source reading. The ordinary read path is requested, deterministic selection followed by model interpretation; it is not evidence of unsolicited memory injection. See [MEM-RTE-knowledge-revision](#mem-rte-knowledge-revision) and [RT-RTE-locus-read](runtime.md#rt-rte-locus-read).

History and effective authority differ. A superseded claim, withdrawn explanation or predecessor finding can remain recoverable without being current knowledge. The carry route deliberately turns an old finding into a re-examination obligation, not a fresh confirmation. A label such as `fixed` likewise does not mean verified-fixed. See [MEM-RTE-carry-recheck](#mem-rte-carry-recheck), [MEM-RTE-explanation-cycle](#mem-rte-explanation-cycle) and [MEM-OBJ-findings](#mem-obj-findings).

There are at least two materially different context selectors: byte-bounded locus lenses and persisted, item-bounded CodebaseBriefs with exact-ID and lexical selection. Design dispatch further filters a brief into a lens-specific packet. A stored full object is therefore not necessarily the object a later agent receives. See [MEM-RTE-brief-delivery](#mem-rte-brief-delivery) and the locus annotation.

The named learning machinery stores propositions, outcome lineage and qualified active configurations. It does not establish automatic induction from raw chat, model-weight updates or exercised future improvement. The runtime policy response excludes the lesson proposition and its evidence ledger; those remain separately readable. See [MEM-OBJ-learning-lessons](#mem-obj-learning-lessons), [MEM-OBJ-learning-policy](#mem-obj-learning-policy).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-claims
Label: Typed claims and validity history

Source-native identity: `claims`, `claim_evidence`, validity events and supersession edges. Storage: SQLite. Operative form: natural-language statement interpreted by agents, separately symbolic keys, epistemic-kind tags, evidence links and Git validity boundaries used by code. Lineage: session caller supplies statement and evidence IDs; handler resolves revisions, checks ancestry/evidence and transactionally inserts. Correction closes an exclusive interval and records a reason/new evidence; supersession admits a new same-key successor with only newly supporting evidence. Current and as-of readers differ from full history. Authority: current/as-of knowledge for readers and future survey passes, not a source-code edit or proof of truth. No object counterpart is declared in runtime; this is the retained input of its survey and locus routes, not a duplicate of those routes. SRC-1: `mcp-server/src/tools/claims.ts`.

> successorRows = evidenceRows.filter((row) => !predecessorEvidence.has(row.id));
> --- `mcp-server/src/tools/claims.ts`

> clauses.push("valid_until_sha IS NULL");
> --- `mcp-server/src/tools/claims.ts`

#### MEM-OBJ-findings
Label: Findings and resolution events

Source-native identity: `findings`, `finding_resolution_events`. Storage: SQLite; form: natural-language symptom, root cause, business context and resolution rationale, plus symbolic severity, revision, status and evidence links. Caller-authored concern/adversarial outputs are admitted after session, phase and revision checks. Initial `fixed` or `ruled-out` insertion is refused. A later coarse fixed status produces `fixed-pending-verification`; the verification handler requires active-session evidence attached as `fix-verification` at the fix revision or a descendant. Reader authority is defect/repair context, not authenticated execution of a fix. SRC-1: `mcp-server/src/tools/findings.ts`; later attention/history consumers are identified in `mcp-server/src/tools/locus.ts`. No supplied object counterpart; distinct from [MEM-OBJ-claims](#mem-obj-claims), which has claim-key validity intervals rather than finding-resolution states.

> "fixed requires both fix_location and fix_sha and remains pending until verify_finding_fix succeeds",
> --- `mcp-server/src/tools/findings.ts`

> if (evidence.role !== "fix-verification") {
>   throw new ToolError("verification evidence must be attached with role fix-verification");
> }
> --- `mcp-server/src/tools/findings.ts`

#### MEM-OBJ-explanations
Label: Purpose and account explanations

Storage: append-only SQLite `explanations` with `explanation_evidence` links. Form: model-authored natural-language bodies; symbolic subject/slot/disposition, revision/session and row IDs govern admission and effective selection. Purpose is capped at 400 UTF-8 bytes and account at 4096; evidence count at 64. A declined slot retains a reason rather than an account. These are derived codebase descriptions, not summaries automatically extracted from raw chat. Consumers: `get_explanations`, completion checks through `readExplanation`, and the documented projections; authority differs between a code gate's slot discharge and a model interpreting the prose. No supplied object counterpart; the object is distinct from [RT-OBJ-amanuensis-skill](runtime.md#rt-obj-amanuensis-skill), which is static method text. SRC-1: `mcp-server/src/tools/explanations.ts`, `mcp-server/src/invariants.ts`.

> const BODY_CAPS = { purpose: 400, account: 4096 } as const;
> --- `mcp-server/src/tools/explanations.ts`

#### MEM-OBJ-field-notes
Label: Peripheral observations

Storage: SQLite `field_notes`. Form: natural-language observation and location, with symbolic category, revision, follow-up and session fields. Admission: active-session caller supplies the content; no per-note human approval or evidence-link requirement appears in this handler. `resolve_field_note` updates follow-up to a caller-supplied string; its label does not prove promotion into a finding. `get_field_notes` filters category/follow-up, newest first, default limit 50. Notes mode explicitly affords later conversational use. No supplied object counterpart. SRC-1: `mcp-server/src/tools/field-notes.ts`, `.claude/skills/amanuensis/references/notes.md`.

> `category="candidate-concern"` and flag it for the next survey
> pass to examine.
> --- `.claude/skills/amanuensis/references/notes.md`

#### MEM-OBJ-prose-artifacts
Label: Registered prose and artifact metadata

Storage separates natural-language files in project storage from symbolic SQLite `artifacts` rows: path, kind, subsystem, content hash, byte size, revision and registration notes. Agent authorship and file I/O precede registration; an active session permits registration/rehashing but is not human content approval. Registration may precede file existence. The materializer uses hashes for changed-input selection; a hash is not a summary or validity assessment. Human/agent reading of prose is interpretive; incremental render decisions use fixed metadata rules. This is the durable input, not a duplicate of [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication)'s derived output route. SRC-1: `mcp-server/src/tools/artifacts.ts`; publication consumer supplied by runtime.

> // File doesn't exist yet — the agent may be registering upfront
> // and will update the hash on a later call. Not an error.
> --- `mcp-server/src/tools/artifacts.ts`

#### MEM-OBJ-file-ledger
Label: File standing and stale metadata

Storage: SQLite `file_ledger`, associated `scope_gaps`, with heat joined from `hot_subsystems`. Form: symbolic path, owner, classification, revision and stale flags; not a semantic memory body. Known subsequent changes: stale backlog filters obligation-bearing rows and orders by heat; `clear_staleness` changes one file's freshness and revision; absent files require retirement rather than clearing. These handlers do not establish that a model re-read the file. Initial file-ledger content admission and exact heat-view formula remain uninspected. No supplied object counterpart; this metadata feeds [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) and survey scope, rather than being the account itself. SRC-1: `mcp-server/src/tools/stale.ts`.

> ORDER BY heat DESC, fl.subsystem_id, fl.file_path
> --- `mcp-server/src/tools/stale.ts`

#### MEM-OBJ-query-log
Label: Query demand traces

Storage: SQLite `query_log`; form: natural-language question plus symbolic fields-hit JSON, tier, subsystem/session metadata. Caller supplies records through `log_query`; the handler checks strings/integers but does not authenticate a human origin or infer fields from an answer. `get_field_demand` returns a ranking view, or static field priority when no data exist. This is trace metadata and a compression-priority affordance, not itself rewritten semantic memory or observed adaptive compression. No supplied object counterpart. SRC-1: `mcp-server/src/tools/logging.ts`.

> "SELECT field, demand_count, demand_ratio, last_demanded, avg_tier_reached FROM field_demand",
> --- `mcp-server/src/tools/logging.ts`

#### MEM-OBJ-access-log
Label: Access heat traces

Storage: SQLite `access_log`; form: symbolic entry ID/tier/session/time with caller-authored trigger text. `log_access` records a claimed load/read. Heat is access metadata, distinct from the content accessed and from query demand. Stale backlog uses heat to prioritize later work; the locus code warns that access counts reaching no subsystem through entries do not establish subsystem access measurement. Initial log authorship can be an agent/caller; it is not automatic instrumentation of every reader. No supplied object counterpart. SRC-1: `mcp-server/src/tools/logging.ts`, `mcp-server/src/tools/stale.ts`, `mcp-server/src/tools/locus.ts`.

> "Access heat is not measured: no access_log row reaches a subsystem through entries.",
> --- `mcp-server/src/tools/locus.ts`

#### MEM-OBJ-carried-findings
Label: Predecessor findings as obligations

Storage: SQLite carry runs, carried findings, evidence attachments and terminal outcomes. Form: natural-language symptom/root cause/rationale plus symbolic archive identity, anchor, archived resolution and successor/evidence links. Caller imports predecessor findings; server enforces run counts, uniqueness and subsequent outcome checks. A carried record is not a finding confirmed in the new store. Full reads expose rationale/evidence; compact lists are a different delivery form. This is distinct from [MEM-OBJ-findings](#mem-obj-findings) and no supplied object counterpart exists. SRC-1: `mcp-server/src/tools/carried.ts`; included rebuild caller is supplied in boundary.

> "Carry one finding out of an archived conspectus into this store, as an obligation to decide rather than a finding this store confirmed. Every archived finding is carried whatever its archived resolution state; one the archive had already closed is recorded with the outcome 'archived-terminal' by this call, which is the only writer of that outcome. A carried record is unique by (archived_store_id, archived_finding_id) and is never updated or deleted.",
> --- `mcp-server/src/tools/carried.ts`

#### MEM-OBJ-codebase-brief
Label: Frozen CodebaseBrief source and selection

Storage: SQLite source, candidate and brief JSON/hash rows plus validations. Form: natural-language task objective, constraints, inherited review statements and caller-authored inferred intents/options; symbolic provenance, epistemic/validity tags, modes, candidate IDs/hashes and omission/selection metadata govern deterministic compilation. Source preparation derives candidates from a review session and caller additions. `direct-user` is a supplied provenance designation, not authenticated human authorship. Persisted full source candidates remain reachable separately from the selected brief. Distinct from ordinary locus responses and the static skill; no supplied object counterpart. SRC-1: `mcp-server/src/tools/codebase-brief.ts`, `mcp-server/src/codebase-brief-contract.ts`.

> const lexicalQuery = input.lexical_query ?? source.objective;
> --- `mcp-server/src/codebase-brief-contract.ts`

#### MEM-OBJ-research-results
Label: Landed external research with provenance

Storage: SQLite result JSON/hash, sources, external claims, code contradictions and consumption records, plus artifact manifest pointing into a durable research workspace. Form separates natural-language summary, held excerpts, limitations and external statements from symbolic access/confidence/destination fields. Landing checks source references and confidence eligibility; reported directly-read/snippet sources must supply excerpts. This is not independent proof that the sources were read or true. Research results remain readable after a no-change decision; consumption bookkeeping is not a source-code or decision-premise mutation. No supplied object counterpart; distinct from ordinary code claims. SRC-1: `mcp-server/src/tools/research.ts`.

> if (["directly-read", "snippet"].includes(accessStatus) && !heldExcerpt) {
>   throw new ToolError(`sources[${index}] read source requires held_excerpt`);
> }
> --- `mcp-server/src/tools/research.ts`

#### MEM-OBJ-learning-lessons
Label: Outcome extraction and lesson ledger

Storage: SQLite extraction JSON/hash, immutable lesson payload, evaluation/events and rollback lineage. Form: natural-language proposition and provenance statements, symbolic channel, scope/configuration, artifact IDs, counts and rollback plan. Extraction validates a terminal agent/review/design source and serializes supplied artifact states; lesson authoring is a separate caller contribution, not automatic model induction. Channels distinguish corpus, retrieval, method, research and user preference, with different evidence eligibility. Reasons/evidence survive in the ledger, but not all pass into the runtime reader. No supplied object counterpart; these are inputs/history of [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission), not a replacement route declaration. SRC-1: `mcp-server/src/tools/learning.ts`.

> retrieval: ["review-evaluation", "query-log", "review-item"],
> --- `mcp-server/src/tools/learning.ts`

#### MEM-OBJ-learning-policy
Label: Active learning policy representation

Storage: SQLite versioned policy configuration and readback records. Form: symbolic policy/version/lesson IDs, channel, revision, status, configuration JSON and affected-future-run selector. Configuration is caller-supplied JSON; its internal semantics and any natural-language values remain opaque here, not established model weights or executable routing rules. The actual active reader delivers those fields, not proposition, evidence or rollback rationale; the ledger permits a separate lookup. Qualification/admission can switch the database's active version without establishing a deployed consumer that interprets its content. Distinct from the lesson history and no supplied object counterpart. SRC-1: `mcp-server/src/tools/learning.ts`; admission is [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission).

> configuration: JSON.parse(row.configuration_json),
> affected_future_runs: JSON.parse(row.affected_future_runs_json),
> status: row.status,
> --- `mcp-server/src/tools/learning.ts`

### Routes

#### MEM-RTE-knowledge-revision
Label: Evidence-bound knowledge correction and reuse

Owner: caller proposes statements, reasons, findings and transitions; code admits or refuses record changes. Mode: open survey/maintenance requests; no independently supplied expected-answer oracle. Admission is software gating, not per-content human approval. A claim correction transaction closes the predecessor and adds newly supported successor/evidence/events; finding correction separately records pending or verified resolution. Rejection leaves the transaction unapplied. Historical readers retain versions/reasons; ordinary current selection excludes closed validity intervals. No supplied route is identical: this is the knowledge-write/history path used within [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle), not the whole model-directed survey. SRC-1: `mcp-server/src/tools/claims.ts`, `mcp-server/src/tools/findings.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Claim receipt or finding transition/verification result, not a regenerated narrative account.
- Later read-back: `get_claims` selects current or Git-as-of versions; `get_claim_history` exposes evidence, events and edges; attention/history lenses and future survey passes use retained conclusions.
- Delegated visibility: Permitted callers can request the stored records; no per-agent context isolation is implemented by these handlers.
- Selection predicate: Exact IDs/keys/subjects or literal subsystem key prefix; optional query revision and historical flag. Finding verification additionally matches active-session, fix-verification evidence and ancestry.
- Invalidation or expiry: Explicit claim interval closure/supersession; finding state events; subsystem reset is a distinct destructive path, not a validity successor.
- Activation or effect: Database knowledge and recorded resolution change; later answer/action effects remain model-mediated and unobserved.
- Evidence limits: Names such as contradictory evidence and verified-fixed encode record checks, not an independent semantic oracle or proof a fix works.

> if (!evidenceIds.some((id) => !existing.has(id))) {
>   throw new ToolError("invalidation requires new evidence not already attached to the claim");
> }
> --- `mcp-server/src/tools/claims.ts`

#### MEM-RTE-explanation-cycle
Label: Explanation admission, replacement and withdrawal

Owner: session caller authors a body or decline reason; code checks subject eligibility, text shape/size, existing evidence, non-name/pattern support and subsystem-ledger overlap. Mode: ordinary evidence-based account writing; no answer oracle or human content gate. New rows replace effective content without overwriting old prose. Reset separately appends withdrawal rows; no semantic rollback validation follows from preserving old rows. Distinct from supplied survey route: this is its explanation slot's write/read lifecycle. SRC-1: `mcp-server/src/tools/explanations.ts`, `mcp-server/src/invariants.ts`, `mcp-server/src/tools/subsystems.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Receipt with identity/disposition/revision, without echoing body or decline reason.
- Later read-back: `get_explanations` returns whole effective body and evidence IDs, earlier-row count, checked flag and zero model calls; completion gate uses effective slot state.
- Delegated visibility: A later session or phase can request the same slot; its host visibility is externally controlled.
- Selection predicate: Subject/slot eligibility and greatest row ID among revisions resolving in the workspace; without workspace checks, greatest ID with checked false. Resolution is not a freshness or semantic correctness test.
- Invalidation or expiry: A newer decline changes slot disposition; withdrawal or ineligibility yields not-recorded. No time-to-live is identified in this selector.
- Activation or effect: Fixed code interprets slot discharge for status admission; models/humans interpret returned prose. Actual improved explanation or model compliance is unobserved.
- Evidence limits: Earlier bodies persist but are not all returned; preserving them does not prove a later consumer reads their reasons. Resolving a Git object does not alone prove that its contents match current HEAD.

> if (resolvable !== null && !resolvable.has(row.ref_sha)) continue;
> if (effective === null || row.id > effective.id) effective = row;
> --- `mcp-server/src/invariants.ts`

> VALUES ('subsystem', ?, ?, 'withdrawn', ?, ?, ?)
> --- `mcp-server/src/tools/subsystems.ts`

#### MEM-RTE-carry-recheck
Label: Carry import and fresh-store discharge

Owner: included rebuild caller/agent supplies imported findings; handler admits archive-bound obligations, then caller proposes successor, ruled-out or repaired outcome. Code can veto counts, duplication and unsupported outcomes. Mode: rebuild/re-examination; no expected-answer oracle. Historical terminal status produces archived-terminal automatically at import, not a fresh-store verified repair. Distinct from [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle); this crosses stores instead of resuming a single current survey. SRC-1: `mcp-server/src/tools/carried.ts`; boundary supplies `dev/rebuild-self-conspectus-store.mjs` as actual shipped caller.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Carried/obligation ID, then terminal-outcome receipt after discharge.
- Later read-back: Full carried reader returns original symptom/root cause, archive lineage, terminal rationale and attached evidence; lists support pending re-examination.
- Delegated visibility: Archive context reaches permitted reader callers as an obligation, not as inherited fresh confirmation.
- Selection predicate: Carry-run/archive identity and finding ID; successor must have been filed in current session; ruled-out requires attached current-session evidence; repaired requires post-repair ancestry evidence.
- Invalidation or expiry: Terminal outcome cannot be overwritten by this tool. Correction is described as a new carry; actual uniqueness is by archive-store/finding pair, so repeat-carry recovery deserves the integration caveat below.
- Activation or effect: Changes fresh store's outstanding obligations; no automatic source-code repair or demonstrated re-discovery follows.
- Evidence limits: Import verifies structural custody and evidence relationships, not archive truth or model re-examination quality.

> if (successor.session_id !== sessionId) {
> --- `mcp-server/src/tools/carried.ts`

#### MEM-RTE-brief-delivery
Label: Task brief selection into design packets

Owner: caller supplies task objective, constraints, inferred intents/options and selection inputs; deterministic preparation/compiler derives and persists candidates/briefs. Code refuses unknown source IDs and insufficient item budgets for forced content; validation is retained. Design planner reads the brief and constructs lens packets, dispatch returns frozen runtime input. No authenticated human gate follows from direct-user labels. Mode: requested task/design context; no expected-answer oracle. Distinct from [RT-RTE-locus-read](runtime.md#rt-rte-locus-read): a separately persisted task artifact with lexical targeting and a concrete design-packet consumer. SRC-1: `mcp-server/src/tools/codebase-brief.ts`, `mcp-server/src/codebase-brief-contract.ts`, `mcp-server/src/tools/design-session.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Compiled brief plus validation, exact registry lookup candidates, or frozen design runtime_input with packet hash.
- Later read-back: Stored brief is retrievable by ID; design planning reads its JSON, selects lens-specific sections and persists packets later returned by dispatch.
- Delegated visibility: Each lens receives controlled selected sections and desires, not other lens outputs in that packet; source guards do not prove host-side blindness.
- Selection predicate: Required objective/constraints plus requested exact registry IDs are forced. Remaining candidates rank by lexical substring matches to tokenized query/objective and stable ID ties; mode and positive score gate optional selection. Item limit defaults to 50 in the tool. Lens section filtering applies after brief compilation.
- Invalidation or expiry: Duplicate source/brief IDs are refused; frozen validity metadata does not auto-refresh on a later code change in the inspected get handler. Recompile requires a new artifact identity.
- Activation or effect: Delivers task context through a tool result; planner/dispatcher are wired consumers, while resulting model decision changes are unobserved.
- Evidence limits: Item count is not a token budget. Forced registry IDs bypass the optional mode filter; no universal mode-exclusion guarantee. Full review-source construction and final design evaluation are uninspected.

> if (!row.candidate.modes.includes(input.mode) || row.score === 0) continue;
> --- `mcp-server/src/codebase-brief-contract.ts`

> context: Object.fromEntries(
>   includedSections.map((section) => [section, sections[section] ?? []]),
> ),
> --- `mcp-server/src/tools/design-session.ts`

#### MEM-RTE-research-consumption
Label: External research landing and destination receipt

Owner: caller lands summary/sources/claims and chooses consumption effect; code checks dispatched state, durable workspace manifest, source/confidence relationships and named destinations. Code can refuse inadequate excerpts, unsupported confidence or mismatched destination; expired requests are terminal. Mode: research requests; no independently executed answer oracle inspected. Proposed knowledge remains external-claim material, distinct from an evidence-backed code observation. No supplied route counterpart. SRC-1: `mcp-server/src/tools/research.ts`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Landed result or consumption receipt with changed/no-change flag.
- Later read-back: `get_research_request` returns stored contract, result payload, held sources, external claims, contradictions, dispatch and consumption. A destination-matched receipt records claimed effect, not automatic mutation of that destination.
- Delegated visibility: Dispatch handoff and returned result are explicit artifacts; full external worker context and execution are uninspected.
- Selection predicate: Exact request/result/external-claim identities and matching target kind/ref; no-change requires only a reason and forbids target/effect statement.
- Invalidation or expiry: Explicit expiry changes request state; it does not delete retained result in the inspected getter. Contradictions remain separately linked to code observations.
- Activation or effect: Records reconciliation and transitions to consumed; this handler does not itself revise the destination decision, code claim or policy.
- Evidence limits: The changed flag is not proof of downstream adoption. Proposal rejection/defer and dispatch budget controls remain uninspected.

> if (externalClaim.target_kind !== effectKind || externalClaim.target_ref !== targetRef) {
>   throw new ToolError("consumption effect must match the cited external claim destination");
> }
> --- `mcp-server/src/tools/research.ts`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-recorded-standing
Label: Recorded standing to later answer

Consumer: later host agent answering a locus question. Channel: requested `describe_locus` result and notes-mode instructions; force: model-interpreted limit on what the record justifies, not code-enforced answer compliance. Horizon: later calls/sessions sharing the store. This is distinct from [RT-BAP-server-opening](runtime.md#rt-bap-server-opening): the opening tells a model to call the reader, while this path carries the changing retained standing/account into the answer. SRC-1: `.claude/skills/amanuensis/references/notes.md`, `mcp-server/src/tools/locus.ts`.

> Say what the record cannot
> justify before you say what it holds.
> --- `.claude/skills/amanuensis/references/notes.md`

## Annotations

#### On [RT-RTE-locus-read](runtime.md#rt-rte-locus-read)

The reader's budget applies to emitted compact text plus repeated structured content, not just body text. Constants are 8192 base wire bytes, 4096 additional bytes per optional section up to a 32768 ceiling, 3072 standing-value bytes and 4096 optional-section-value bytes. Unknown samples are removed first; sections lose whole items round-robin, with ID samples reduced last and census/omission counts retained. This is selection of what reaches the model, not database deletion, semantic summarization or trimming of earlier host turns. Count floors may exceed a target budget; ceiling overflow refuses the call. Kept records remain reachable through narrower/other readers, but exact completeness across all raw classes is uninspected. SRC-1: `mcp-server/src/tools/locus.ts`.

> const WIRE_BUDGET = 8192;
> const WIRE_BUDGET_PER_OPTIONAL_SECTION = 4096;
> const WIRE_CEILING = 32768;
> const STANDING_VALUE_BUDGET = 3072;
> const OPTIONAL_SECTION_VALUE_BUDGET = 4096;
> --- `mcp-server/src/tools/locus.ts`

#### On [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission)

Memory lineage begins with terminal agent-session, furnished review-session or terminal design-session records, then explicit caller-supplied artifact extraction. Query-log provenance is one allowed retrieval-channel input; method, corpus, research and user-preference lessons have other evidence classes. Deterministic extraction/validation is automatic once requested, but lesson propositions and configuration are authored inputs. Therefore this wiring supports trace-informed retained policy proposals, not autonomous discovery of lessons from every raw trace.

The active reader's representation is [MEM-OBJ-learning-policy](#mem-obj-learning-policy); full proposition/evidence/rollback lineage is [MEM-OBJ-learning-lessons](#mem-obj-learning-lessons). Its runtime serializer omits those reasons. A separate ledger reader can expose them, including later invalidation inputs, without establishing that a future agent consults the ledger. SRC-1: `mcp-server/src/tools/learning.ts`.

> const artifacts = extractionArtifacts(ctx, extractionId);
> --- `mcp-server/src/tools/learning.ts`

> proposition: requireString(args, "proposition"),
> --- `mcp-server/src/tools/learning.ts`

#### On [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle)

Working-context control is prescribed rather than server-enforced: load only the current phase reference; optionally spawn a Task agent with reference instructions, subsystem/session IDs and survey SHA; return its short summary and persist work through tools. This resembles a separate frame whose local structural read need not enter later concern reasoning. The break in that analogy is material: host window isolation, transcript retention, compaction and exact return selection are not implemented or verified by Amanuensis. Inline fallback keeps work in the foreground context. The persistent store is independently reloadable, not a reference that automatically restores an earlier model window. No source-grounded automatic chat-compaction or alternate checkpoint-summary format is established by this inspection. SRC-1: `.claude/skills/amanuensis/SKILL.md`; its load-bearing passages are retained in [RT-CMP-host-model](runtime.md#rt-cmp-host-model), [RT-OBJ-amanuensis-skill](runtime.md#rt-obj-amanuensis-skill) and [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle).

## Write side

The ordinary writer is the host agent/caller, not the database. Software admission checks sessions, argument shapes, revision/evidence relationships and phase eligibility. Starting an autonomous survey is not human approval of each claim, note or explanation. Available user interruption/redirection remains different from per-content admission. The scoped checks and transactional correction paths are retained in [MEM-RTE-knowledge-revision](#mem-rte-knowledge-revision), [MEM-RTE-explanation-cycle](#mem-rte-explanation-cycle), [MEM-RTE-carry-recheck](#mem-rte-carry-recheck) and [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission).

Physical file writing is separate. The skill permits agent writes to project storage, while `register_artifact` records metadata and can succeed without a file. Prose authorship, registration, hash refresh and publication are not a single approval event. Reset deletes selected survey records and appends explanation withdrawal rows; it is not an archive-preserving semantic successor for every deleted object. See [MEM-OBJ-prose-artifacts](#mem-obj-prose-artifacts), [MEM-RTE-explanation-cycle](#mem-rte-explanation-cycle); SRC-1: `mcp-server/src/tools/subsystems.ts`.

Re-examination control is also split. `clear_staleness` physically changes freshness metadata but cannot establish the re-reading it asserts. Retirement removes an absent file-ledger row while leaving findings and other survey records; that is scope maintenance, not a conclusion that earlier claims are false. Full change-detection, impact and revalidation propagation remain an integration limit, not a negative finding. See [MEM-OBJ-file-ledger](#mem-obj-file-ledger).

Trace-fed paths are not uniform. Access/query logs retain usage reports and feed heat/demand views; no rewritten semantic summary follows merely from those logs. Outcome extraction derives a typed artifact ledger from terminal session state; a caller then formulates a lesson, supplies configuration/evaluation and invokes gated staging/activation. This preserves reasons in a separately readable ledger while delivering a smaller configuration representation. It establishes neither automatic raw-chat-to-policy induction nor later host adoption. See [MEM-OBJ-query-log](#mem-obj-query-log), [MEM-OBJ-access-log](#mem-obj-access-log) and the policy annotation. Raw session/dispatch logs, checkpoint commits and derived explanations are different retained results; checkpointing alone does not add a learned behavioral rule.

## Read-back

Ordinary consumption is a pull chain: a model follows the installed skill/server instruction, requests a locus or raw reader, code selects prior material, and the tool response enters the host's context. The automatic deterministic selector inside that request is not an independent unsolicited push. Warm-start dashboard and resume queries are instructed requests as well. See [RT-BAP-server-opening](runtime.md#rt-bap-server-opening), [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle), [MEM-BAP-recorded-standing](#mem-bap-recorded-standing).

The locus lenses keep counts and standing while dropping selected items, rather than compacting prose. Explanations return an effective whole body and cited IDs, not all earlier bodies. Claims permit current, historical and Git-as-of queries; carried findings permit a compact list followed by a full exact record. Field-note readers use filter/limit, not semantic retrieval. CodebaseBrief compilation adds actual task targeting through lexical/exact-ID selection and persists its omissions; design packet construction narrows it again. These mechanisms must not be conflated into one retrieval policy. See [MEM-RTE-explanation-cycle](#mem-rte-explanation-cycle), [MEM-RTE-knowledge-revision](#mem-rte-knowledge-revision), [MEM-RTE-carry-recheck](#mem-rte-carry-recheck), [MEM-RTE-brief-delivery](#mem-rte-brief-delivery).

Documentation is another delivery channel: generated HTML/Markdown is human-readable derived memory, with durable source in database/prose. Its verifier compares projection to retained source, not retained knowledge to reality. Runtime's clean/default/no-verification distinctions remain binding; no unconditional publication-health claim is made. See [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication).

The policy reader is a storage/service affordance with an internal verification consumer, not established automatic delivery to a future host. Research consumption similarly records a matched destination receipt without applying that destination's change. A returned `active`, `changed` or `consumed` label therefore does not close the path to behavioral activation. See [MEM-OBJ-learning-policy](#mem-obj-learning-policy), [MEM-RTE-research-consumption](#mem-rte-research-consumption).

## Integration issues

- No supplied runtime fact is replaced by a contradictory finding here. The report refines it with distinct retained objects and concrete packet delivery. No new declaration is intended to duplicate a supplied referent. [MEM-BAP-recorded-standing](#mem-bap-recorded-standing) is adjacent to, but distinct from, [RT-BAP-server-opening](runtime.md#rt-bap-server-opening): changing retained payload versus static instructions to request it. [MEM-RTE-brief-delivery](#mem-rte-brief-delivery) is not a renamed locus route.
- [MEM-RTE-carry-recheck](#mem-rte-carry-recheck) retains a source tension: outcome correction instructions say to carry the finding again from the same archive, but `carry_finding` rejects an existing archive-store/finding pair. SRC-1: `mcp-server/src/tools/carried.ts`. Whether a fresh archive identity or another recovery mechanism resolves that conflict is uninspected; straightforward same-pair recarry is not an established rollback path.
- [MEM-OBJ-learning-policy](#mem-obj-learning-policy) and [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) establish active representation/readback, not future consumer enforcement. A bounded search for `learning_policy_versions`, `get_learning_policy` and `activePolicy(` under `mcp-server/src/` and the shipped skill found policy service/schema use, not an ordinary-survey automatic consumer. Broader driver adoption remains uninspected. Prevented conclusion: that active corpus/retrieval/method configurations actually change subsequent host decisions or preserve their reasons at that consumer.
- [MEM-RTE-brief-delivery](#mem-rte-brief-delivery) has a narrower mode guarantee than its labels might suggest: exact registry/required selections are forced before optional mode filtering. Design packet filtering is a subsequent control. Full review-session admission, contamination handling and evaluation of these contexts remain unresolved; do not infer blind independent model contexts from packet separation alone.
- The coverage table's additional included families remain unresolved, not excluded: evidence/disposition/vocabulary/question/contradiction/seam/xref writers; composition, review and diagnosticity; impact/revalidation/refresh cancellation and result scoring; evaluation/envelope rebaseline; adapter recovery and projection verification; historical/dev drivers and receipts. Their missing full chains prevent a complete account of every alternative write, invalidation, evaluation-fed update or downstream consumer. Supplied runtime facts remain usable within their narrower trace. No system-wide absence, complete enumeration of memory behavior or benefit inference is licensed.
- [MEM-OBJ-file-ledger](#mem-obj-file-ledger) preserves unknown initial content control beside known subsequent cleanup and ranking. [MEM-OBJ-query-log](#mem-obj-query-log) preserves claimed human-query provenance as caller data, not authenticated trace origin. These limits matter to classifying human-controlled admission and automatic trace learning.

## Limitations and checks

This is implementation/doctrine evidence, not an observed deployment or causal experiment. Git HEAD matched the boundary revision; input identities and role/type contracts were read completely, with bounded continuation of oversized inputs. Source-native countercases checked included withdrawn/declined explanations, unchecked revision selection, archived-terminal findings versus fresh repairs, coarse fixed versus verified-fixed, forced brief selections versus optional mode filtering, receipt-only research consumption, and active policy readback versus actual future adoption. These qualify stronger readings without erasing supported wiring.

A bounded search of runtime TypeScript for compression/embedding terms found logging descriptions and vocabulary compression, not a traced chat-compaction writer. This is an inspection limit, not an evidenced absence or a claim that hosts do not compact. Provider state is opaque; no exact model version, parameter update, semantic accuracy, guaranteed host compliance or improved future capacity is established by this memory report. The source contracts and supplied runtime distinguish those conclusions independently.

Validation: the required role-specific deterministic validator is run against this report and the supplied artifact; its successful result checks structure, references and quotation occurrence, not analytical correctness or workflow acceptance.
