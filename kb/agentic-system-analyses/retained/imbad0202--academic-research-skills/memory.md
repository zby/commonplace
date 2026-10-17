---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Memory mechanisms of academic-research-skills: passport recovery, corpus reuse, resolver caching and explicitly bounded advisory histories."
run-id: AAS-2026-10-17-academic-research-skills-6fe859d62c16-01
source-identity: "https://github.com/Imbad0202/academic-research-skills"
reviewed-boundary: "060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a"
---

# academic-research-skills memory report

## Boundary and evidence

The memory boundary includes accumulated task material that can reach a later invocation, recovery after host compaction, and working-context controls even when nothing durable results. It includes the Material Passport, referenced artifacts, separate run ledger, screening state/corpus, resolver cache, reading attestations, inquiry branches, criteria-binding receipts, process records and activity history. Static skill files are behavioral guidance, not accumulated memory. Provider parameters and host summaries remain external/opaque; the supplied runtime describes their interfaces, not their implementation. Source identity and exclusions are those of [the boundary](boundary.md).

All added inspection uses SRC-1 at the frozen commit. Direct reads below establish implementation or doctrine/design, never observed operation. The source HEAD matched the boundary and its status was clean at inspection. No target program, provider, test or example was executed. Available but uninspected helpers remain named limits, not absences.

| Entry point or memory operation | Source path and inspection basis | Coverage and prevented conclusion |
|---|---|---|
| Command loading, activation restore, host hooks | Direct bounded `pi/wrapper.js`, complete `hooks/hooks.json`; supplied runtime dispatch/guard findings | [RT-RTE-command-dispatch](runtime.md#rt-rte-command-dispatch), [RT-RTE-tool-scope](runtime.md#rt-rte-tool-scope); activation metadata is not paper content; host compaction implementation is not inspected |
| Checkpoint/reset and run-ledger recovery | Complete `academic-pipeline/references/passport_as_reset_boundary.md`; direct tracker ownership/recovery and orchestrator Run ledger section; supplied ledger implementation | [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery), [RT-OBJ-run-ledger](runtime.md#rt-obj-run-ledger), annotations below; no verified runtime reset or authentic user history follows |
| Folder import and rejected files | Direct `scripts/adapters/folder_scan.py` producer loop | [MEM-OBJ-literature-corpus](#mem-obj-literature-corpus), [MEM-RTE-corpus-reuse](#mem-rte-corpus-reuse); other Zotero/Obsidian adapter internals uninspected, preventing uniform import guarantees |
| Screening decisions, export and re-screening | Direct `sr-screener/scripts/build_outputs.py` serializer; bounded search of `merge_decisions.py`; supplied builder/template findings | [RT-RTE-screening-fanout](runtime.md#rt-rte-screening-fanout), [MEM-RTE-corpus-reuse](#mem-rte-corpus-reuse); no full merger or revision-archive audit |
| Both corpus consumers and trust metadata | Direct bounded `academic-paper/agents/literature_strategist_agent.md` and `deep-research/agents/bibliography_agent.md` searches/passages | [MEM-RTE-corpus-reuse](#mem-rte-corpus-reuse); metadata is not source text, and parse fallback is not successful corpus use |
| Verification cache API, CLI/defaults, bypass and invalidation | Complete `scripts/verification_cache.py`; direct detailed cache wrapper in `scripts/contamination_signals.py`; gate defaults, CLI/command searches | [MEM-OBJ-verification-cache](#mem-obj-verification-cache), [MEM-RTE-cache-verification](#mem-rte-cache-verification); not a full scholarly-service audit |
| User reading declarations and rescission | Complete `commands/ars-mark-read.md`; direct update/unmark and resolver functions | [MEM-RTE-read-attestation](#mem-rte-read-attestation); cannot certify actual reading or understanding |
| Inquiry ledger replay/publication and checkpoint display | Direct orchestrator inquiry section and `scripts/inquiry_branch_ledger.py` summary implementation; API/CLI inventory search | [MEM-RTE-inquiry-summary](#mem-rte-inquiry-summary); full replay/transaction internals not audited; initial workflow-profile creation remains outside this shipped pipeline step |
| Criteria-aware handoff binding | Direct tracker contract and `scripts/review_criteria_binding.py` init/receipt/validate implementation | [MEM-OBJ-review-criteria-binding](#mem-obj-review-criteria-binding); full registry resolver and all three consumer bodies uninspected, preventing semantic criterion-use conclusions |
| Cross-model, citation markers, revision evidence, package freshness | Supplied runtime findings; direct reset audit-revalidation contract | [RT-RTE-cross-verification](runtime.md#rt-rte-cross-verification), [RT-RTE-final-output](runtime.md#rt-rte-final-output), [RT-RTE-revision-review](runtime.md#rt-rte-revision-review); unified cross-model retention, package checker internals and apply rollback remain uninspected |
| Process summary and observer | Direct `academic-pipeline/references/process_summary_protocol.md` workflow/exclusion; reset interactions | [MEM-OBJ-process-record](#mem-obj-process-record); observer internals and a later automated lesson-consumption path not established |
| Post-terminal activity store, render and deletion | Direct tracker/orchestrator contracts and `scripts/adjudication_activity.py` append/render/delete functions | [MEM-RTE-activity-history](#mem-rte-activity-history); source extraction internals only inventoried, so semantic completeness of captured events unestablished |
| Evaluation reports and regression admission | Supplied runtime findings | [RT-RTE-evaluation-admission](runtime.md#rt-rte-evaluation-admission); saved reports feed comparison, not demonstrated live method installation |
| Local enrichment, contamination/retraction metadata and audit histories | Bounded bibliography search; direct reset audit contract | Corpus metadata enrichment and audit evidence are included but incompletely inspected; current matcher snapshots, retraction evidence producers, all audit checks and inquiry replay details cannot receive uniform trust/rollback conclusions |

## Core ideas

ARS preserves different kinds of state for different consumers. The passport names materials and stage state; the run ledger preserves selected words, receipts and counters against lossy host summaries. Recovery does not replay every transcript. In particular, turn-range pointers do not retain the underlying conversation across reset. See [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery) and its annotation.

Corpus reuse is selective task knowledge, not automatic instruction adoption. A screening export retains a decision explanation in `user_notes`, but later bibliography roles re-screen it under the current research question. Folder import can retain only filename-derived metadata and a pointer. Neither label establishes that the source was read. [MEM-RTE-corpus-reuse](#mem-rte-corpus-reuse).

The resolver cache is narrower still: the inspected caller stores versioned match decisions, not complete papers or a chain of model reasoning. Matching lookup keys can feed later verification summaries without a live resolver call. Invalidating or bypassing those rows changes the next check, not a model's parameters. [MEM-RTE-cache-verification](#mem-rte-cache-verification).

Not every retained history is intended to govern models. Inquiry summaries reach checkpoints under explicit author authority; adjudication-activity history is restricted to a standalone human-facing advisory and explicitly excluded from model input. Process-record lessons have an output reader but no established automatic adoption route. These distinctions prevent equating durable storage, delivery, behavioral activation and learning.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-literature-corpus
Label: Literature corpus

Structured YAML entries retained in a Material Passport or exported corpus file. Citation keys, dates, enumerated trust fields and pointers are symbolic metadata; titles, abstracts and notes are natural-language data for model interpretation. The source paper is a separate object reached only through some other acquisition route; a `source_pointer` is not the paper's contents. Lineage includes user-owned inputs transformed by adapters and screening results transformed by the serializer. Initialization/per-entry human approval is not established merely by the user invoking an import.

Distinct from [RT-OBJ-run-ledger](runtime.md#rt-obj-run-ledger) and [RT-OBJ-ref-markers](runtime.md#rt-obj-ref-markers): these are source records, not checkpoint receipts or prose joins. Its export/read-back route is a material part of [RT-RTE-screening-fanout](runtime.md#rt-rte-screening-fanout), but corpus identity also includes non-screening imports. SRC-1, `scripts/adapters/folder_scan.py`, `sr-screener/scripts/build_outputs.py`, `academic-paper/agents/literature_strategist_agent.md`.

> f.write("# or give the file to academic-paper / deep-research as your curated corpus.\n")
> --- `sr-screener/scripts/build_outputs.py`

The serializer actually writes that comment inside a string, so the operative delivery contract is also visible in the consumer instructions quoted under the route below. Export retains screening decision, exclusion code, explanation and deciding role in notes; folder scanning instead produces filename-derived family/year/title plus file URI and unknown venue type. Reasons for importer rejection are kept in a separate rejection log, not silently converted into accepted corpus records.

#### MEM-OBJ-verification-cache
Label: Verification cache

Local SQLite database, default `~/.cache/ars/verification.db`, overridable by explicit API path then `ARS_VERIFICATION_CACHE_PATH`. Rows key on citation key, resolver name and query form; JSON payload plus UTC verification timestamp are stored. The inspected detailed wrapper writes `matched`, `matched_by`, `queried_by` and `decision_version`: derived symbolic resolver decisions, not the complete upstream response despite the generic storage API accepting any dictionary. Timestamp/age is access/freshness metadata, not stronger evidence of truth. No closest supplied object has this identity; [RT-RTE-final-output](runtime.md#rt-rte-final-output) already describes its consumer route broadly. SRC-1, `scripts/verification_cache.py`, `scripts/contamination_signals.py`.

> {"matched": not unmatched, "matched_by": matched_by,
>          "queried_by": queried_by,
>          "decision_version": RESOLVER_DECISION_VERSION},
> --- `scripts/contamination_signals.py`

#### MEM-OBJ-human-read-log
Label: Human read log

Session/passport-scoped YAML peer file `<passport-stem>_human_read_log.yaml`; not mutable fields inside corpus entries. Symbolic citation key, scope, locators and mark/rescind timestamps select authority; optional notes remain natural language. Lineage is a user declaration mediated by a command and deterministic writer, not independent observation of human reading. Distinct from [RT-OBJ-run-ledger](runtime.md#rt-obj-run-ledger): it is a reading-attestation ledger, not run-event receipts. SRC-1, `commands/ars-mark-read.md`, `scripts/ars_mark_read.py`.

> This is a user statement, not independent evidence that a person read or understood the source.
> --- `commands/ars-mark-read.md`

#### MEM-OBJ-inquiry-ledger
Label: Inquiry branch ledger

Canonical JSON event ledger with symbolic actor/status/event links, profile bindings, artifact references and stale-cause IDs, alongside natural-language branch statements, original surfaced text and reopen conditions. Passport pointer and recovery journal participate in publication; the display summary is a derived projection, not the entire ledger. Its source-native purposes are remembering alternatives, author adoption and stale dependencies, not replacing manuscript integrity gates. Distinct from both run and reset ledgers in [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery). SRC-1, `scripts/inquiry_branch_ledger.py`, `academic-pipeline/agents/pipeline_orchestrator_agent.md`.

> The ledger is a memory surface, not a gate: it cannot change an integrity
> PASS/FAIL, satisfy a mandatory checkpoint, establish novelty/correctness/value,
> or silently regenerate a stale artifact.
> --- `academic-pipeline/agents/pipeline_orchestrator_agent.md`

#### MEM-OBJ-review-criteria-binding
Label: Review criteria binding

JSON manifest retains target review identity, references/hashes of context and registry, selected criterion IDs and consumer receipts with artifact hashes. These are symbolic bindings; criterion meaning remains in separately named natural-language registry/context material. A tracker index is explicitly non-authoritative and does not copy the content. The builder creates a manifest only after context-pair validation; changed target authority under the same review ID is refused, while a new target ID records a non-comparable predecessor. Receipt recording requires ordered artifact roles and exactly one binding marker/conflict line, under a lock; differing repeat receipts conflict. These checks establish binding consistency, not that a reviewer substantively applied the criteria. No supplied record names this specific object; it complements the review handoffs in [RT-RTE-revision-review](runtime.md#rt-rte-revision-review). SRC-1, `scripts/review_criteria_binding.py`, `academic-pipeline/agents/state_tracker_agent.md`.

> "same target_review_id cannot bind a changed review target"
> --- `scripts/review_criteria_binding.py`

The tracker contract names later criteria-aware handoffs and permits refusal of that handoff on mismatch, not alteration of severity, verdict or author triage. Its selected criterion IDs are targeting evidence for this binding, not evidence of semantic retrieval over previous reviews. The initial declaration's human-control details and full downstream consumer behavior remain uninspected.

#### MEM-OBJ-process-record
Label: Process record

Natural-language Markdown, optionally converted to PDF, derived by the model from current session history and earlier passport/run-ledger evidence. Includes user quotes, decisions, iteration history and lessons. User can request corrections before terminal acknowledgement. Its documented later consumer is the user sharing/reporting/reflecting on the process; no inspected instruction automatically reloads its lessons into a later research task. Distinct from the workflow's event ledger and from the activity store below. SRC-1, `academic-pipeline/references/process_summary_protocol.md`.

> words from the passport and run ledger, and say in the record which parts come
>    from those rather than the conversation):
> --- `academic-pipeline/references/process_summary_protocol.md`

#### MEM-OBJ-activity-store
Label: Adjudication activity store

Canonical JSON local store contains retained eligible terminal-run records, source receipts, extracted adjudication events and sequence/revision metadata. It is derived symbolic history, not a raw transcript, manuscript guidance or model evaluation score. A user explicitly selects the store; deterministic post-terminal seal/build/append computes bindings and extracts events. Append checks store/input identity, idempotence and caps; individual source extraction completeness is not independently audited here. No supplied record has this object's identity; [RT-RTE-pipeline-stages](runtime.md#rt-rte-pipeline-stages) supplies the ordinary terminal workflow from which this advisory path is deliberately separated. SRC-1, `scripts/adjudication_activity.py`, `academic-pipeline/agents/state_tracker_agent.md`.

> record = _extract_run(manifest, root, store["next_sequence"])
> --- `scripts/adjudication_activity.py`

### Routes

#### MEM-RTE-corpus-reuse
Label: Corpus export and reuse
Part of: [RT-RTE-screening-fanout](runtime.md#rt-rte-screening-fanout)

This route isolates screening's exported retained result and its later consumer; non-screening acquisition into the same object is described above, not asserted as part of screening. Exporter code owns serialization; the user supplies/passes the resulting corpus; literature roles own relevance screening. SRC-1, `sr-screener/scripts/build_outputs.py`, `academic-paper/agents/literature_strategist_agent.md`, `deep-research/agents/bibliography_agent.md`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: curated YAML records, with missing-authors/year rows rejected; producer instructions say to pass the file or paste it into the passport.
- Later read-back: a later literature-role invocation reads the supplied non-empty corpus, screens under the current question and merges retained inclusions with external inclusions.
- Delegated visibility: corpus metadata/abstract/notes reach the role; pointers are not dereferenced by this consumer protocol and the full screening worker transcript is not required.
- Selection predicate: minimal shape check, current inclusion/exclusion criteria, uncovered topics and explicit corpus-only user request; not similarity search over a memory database.
- Invalidation or expiry: parse/shape failure emits a failure marker and falls back to external-only search; irrelevant records are logged as skipped, not removed from the adapter-owned corpus.
- Activation or effect: prescribed bibliography/matrix/gap selection; neither actual consumption nor accurate screening was observed.
- Evidence limits: model-operated read-only/screening rules are doctrine/design; serializer is implementation. A screening decision is not automatic manuscript admission or evidence of source acquisition.

> 3. **Iron Rule 3 — No corpus mutation.** Consumer agents never modify, backfill, or derive new content into `literature_corpus[]`. Read only.
> --- `academic-paper/agents/literature_strategist_agent.md`

> 4. **Iron Rule 4 — Graceful fallback on parse failure.** Consumer agents do NOT re-validate schema, do NOT parse JSON Schema at runtime, and do NOT dereference `source_pointer` URIs. When the corpus cannot be parsed, emit `[CORPUS PARSE FAILURE: <cause>]` and fall back to external-DB-only flow.
> --- `deep-research/agents/bibliography_agent.md`

Admission is split: model/human screening proposes decisions under the confirmed protocol; export software admits metadata shapes; a later model judges relevance again. No independent answer oracle exists on that later open-research route. Selection retains screening reasons in notes, but no inspected consumer contract requires reconstructing their full evidential derivation. Corpus abstracts/notes are explicitly untrusted data, not instructions. No fixed token budget is specified in these inspected consumer passages. User corpus-only control can suppress external supplementation while requiring known gaps to remain visible.

#### MEM-RTE-cache-verification
Label: Cached resolver verification

Omitted cache argument/default CLI → persistent cache → detailed resolver wrapper → verification summary → finalization consumer. Software owns match admission; a generic cache caller can also put/replace dictionaries without a human approval step. The automatic write derives a later behavior-shaping lookup decision from a resolver result; it is not training or a retained model-reasoning trace. Complements, rather than duplicates, the broader [RT-RTE-final-output](runtime.md#rt-rte-final-output). SRC-1, `scripts/verification_gate/__init__.py`, `scripts/contamination_signals.py`, `scripts/verification_cache.py`, `scripts/verify_passport.py`, `commands/ars-cache-invalidate.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: resolver match/query metadata and served-from-cache signal, or live recomputation and cache replacement.
- Later read-back: later verification calls with matching citation/resolver/query-form read saved decisions; gate callers further require current decision version, boolean matched and id/title queried_by.
- Delegated visibility: summary fields reach integrity/final-output logic; the database row does not provide the original paper or resolver evidence rationale.
- Selection predicate: exact composite key and payload/version checks; TTL 90 days, with optional per-row stale bypass controlled by ARS_CACHE_REVALIDATE; explicit cache=None or --no-cache runs live.
- Invalidation or expiry: expired/malformed data becomes a miss; citation invalidation deletes all its resolver/query rows; command documentation also permits deleting the database; next lookup repopulates.
- Activation or effect: successful cache hit returns the stored decision instead of invoking compute; no deployed activation/benefit was observed.
- Evidence limits: existence/metadata matching does not establish claim faithfulness; age advisory alone never changes the gate. Generic API writers and looser boolean-only consumers have different admission checks.

> # Gate callers additionally require TYPED payload values: matched
>             # must be a real bool (a string "false" is truthy and would launder
>             # into lookup_verified="true") and queried_by must be a valid
> --- `scripts/contamination_signals.py`

> # ARS_CACHE_REVALIDATE; an EXPLICIT cache=None is the live opt-out.
> --- `scripts/verification_gate/__init__.py`

Guidance shaping the derived result is fixed resolver decision logic, not an inferred theory revision. Resolver failure/rejection can force recomputation; invalidation is recovery by removal, not restoration of an earlier trusted verdict. External resolver results are fallible evidence, not an expected-answer oracle. Human per-row admission and original provenance of caller-injected cache dictionaries remain unresolved. Automatic caching can improve reuse capacity operationally, but no measured learning or accuracy gain is established.

#### MEM-RTE-read-attestation
Label: Reading attestation resolution

User-issued command → validated/locked peer-log update → later finalizer invokes deterministic resolver for citation/anchor → transient covered/partial/unknown/rescinded result. The user supplies the claim and scope; software checks key/environment/log and deterministic coverage, not truth of the declaration. This is a distinct retained input to [RT-RTE-final-output](runtime.md#rt-rte-final-output), not another complete final-output route. SRC-1, `commands/ars-mark-read.md`, `scripts/ars_mark_read.py`, `scripts/human_read_attestation_resolver.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: stored user mark or rescission, or validation/refusal diagnostics.
- Later read-back: each finalizer pass resolves the current peer log for a named citation and anchor; result is transient, not a persisted audit receipt.
- Delegated visibility: finalizer receives coverage eligibility; corpus remains unmodified and the declaration is not elevated to independent reading evidence.
- Selection predicate: matching citation events, latest timestamp/index event, valid anchor and explicit scope/locator coverage; full_text covers resolved anchors, unknown/legacy scopes do not.
- Invalidation or expiry: latest matching rescission returns rescinded; invalid ledger returns ledger_invalid; changed anchor re-evaluates coverage rather than reusing a past promotion.
- Activation or effect: only covered is ok-eligible in deterministic resolution; marker promotion is instructed finalizer behavior, not observed execution.
- Evidence limits: latest-event ordering and coverage do not prove comprehension, correct sources or faithful claims; subsequent finalization is necessary to reflect withdrawal in output.

> "latest matching event rescinds the attestation",
> --- `scripts/human_read_attestation_resolver.py`

> Returning missing active marks keeps batch unmark all-or-nothing: the
>     in-memory partial mutation is discarded and no replacement occurs.
> --- `scripts/ars_mark_read.py`

The unmark path adds `rescinded_at` to an existing mark rather than erasing the historical declaration. User veto/replacement concerns the attestation, not the underlying source truth. There is no answer oracle or automatic content-quality improvement claim; the operating mode is open manuscript verification.

#### MEM-RTE-inquiry-summary
Label: Inquiry branch summary

Opted-in inquiry events → replayed projection → checkpoint summary → author/foreground checkpoint context. Code selects the display; the orchestrator is instructed to insert it without rewriting. A bound research-workflow profile and a second explicitly recorded branch are preconditions for durable publication. SRC-1, `academic-pipeline/agents/pipeline_orchestrator_agent.md`, `scripts/inquiry_branch_ledger.py`. Distinct from reset/run recovery in [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery): remembers author-owned alternatives rather than proving checkpoint responses.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: compact provenance-labelled live-branch/stale-artifact block, or no display when disabled/single-branch.
- Later read-back: load/replay CLI and checkpoint calls reconstruct from explicit ledger, passport pointer and bound profiles; automatic display occurs at design freeze, Stage 2.5, Stage 4.5 or a recorded reopen-condition signal.
- Delegated visibility: checkpoint receives live statements with status/provenance, stale-cause references, parked/rejected counts and optional named reopen condition/evidence pointer, not all historical text.
- Selection predicate: flag, summary moment, introduced-branch count, current live statuses and optional signal event ID; profile branch_budget limits live state, not a measured token budget.
- Invalidation or expiry: invalid chain/profile/pointer/budget is a hard error by contract; reject/park/archive and stale resolution are explicit author events. Display off/reset-to-simple-path preserves history.
- Activation or effect: afforded visibility for author judgment; signal never automatically reopens a branch or satisfies an integrity gate.
- Evidence limits: summary code inspected; replay/publication implementation only inventoried, so no independent full transaction-safety audit or observed author adoption follows.

> Activation requires
> an explicit author adoption receipt retaining its source event and original
> text.
> --- `academic-pipeline/agents/pipeline_orchestrator_agent.md`

> live = [branch for branch in branches if branch.get("status") in LIVE_STATUSES]
> --- `scripts/inquiry_branch_ledger.py`

AI proposes a parked facet; author adoption/park/reject/reopen/merge/archive decides reliance. User questions are not automatic internal decisions. Original text and event identity are retained, while summary selection can omit rejected content except counts. The declared transaction uses the stable passport sidecar/recovery journal; the complete crash-recovery implementation remains uninspected. There is no known-answer oracle, established explanatory theory revision or demonstrated future-capacity improvement on this open research branch-management route.

#### MEM-RTE-activity-history
Label: Activity history rendering

Durable terminal transition → optional sealed source inventory → build-input/append-run → later explicit render → standalone user advisory. Owner: tracker for pending inventory, deterministic helpers for bindings/extraction/store, user for store selection and requested display/deletion. Distinct from [RT-RTE-evaluation-admission](runtime.md#rt-rte-evaluation-admission): records adjudication activity, not baseline metrics admitting package changes. SRC-1, `scripts/adjudication_activity.py`, `academic-pipeline/agents/state_tracker_agent.md`, `academic-pipeline/agents/pipeline_orchestrator_agent.md`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: appended/idempotent/conflict diagnostic and optionally advisory counts; failures cannot undo terminal completion.
- Later read-back: explicit render opens/validates the selected store and selects the last requested window of retained runs for human-facing counts.
- Delegated visibility: renderer exposes counts/denominators, terminal state and unavailable-source coverage; the contract forbids these data entering passport, handoffs, Process Record, model/reviewer/observer/eval inputs, gates or verdicts.
- Selection predicate: explicit store/input/run identity, canonical valid store, terminal eligible source records and last-window sequence selection, not semantic retrieval.
- Invalidation or expiry: identical run/input receipt is idempotent; conflicting identities/caps refuse. Confirmed delete-runs removes selected IDs/ranges without reusing sequence numbers; whole-store deletion requires raw hash and confirmation token.
- Activation or effect: later render reflects retained survivors; no model behavioral authority or successful user learning is established.
- Evidence limits: post-terminal orchestration is a protocol; inspected local append/render/delete code supports those operations, not exercised completeness of upstream event capture.

> selected = store["runs"][-window:]
> --- `scripts/adjudication_activity.py`

> Neither pending bindings, sealed inventory, selected-store information, store
> contents, renderer output, nor diagnostics may enter a Material Passport,
> stage handoff, Process Record, reviewer/model/observer input, compliance
> decision, gate, verdict, or checkpoint input.
> --- `academic-pipeline/agents/state_tracker_agent.md`

This automatic trace-derived store retains events/countable activity rather than new behavioral guidance; its prohibited downstream model route defeats a claim that retaining it establishes trace-fed model learning. Human review of the standalone output is afforded, but benefit is not observed. Deletion changes future displayed history; no separate automatic forgetting of manuscript or other logs is implied. Deletion confirmation is a software token check; actual authorized human identity is not independently authenticated by that fact.

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-run-ledger](runtime.md#rt-obj-run-ledger)

Memory-specific lineage: orchestrator-selected user words, stdout/exit outcomes, retry counters and transient file paths are written as events before compaction or subagent return can lose them. Tracker conversation state is not the durable writer. The report validates only what has been recorded; hashes cannot recover an omitted event or authenticate a fabricated one. Raw user words are retained alongside derived report classifications; report output is not a retained model summary. Later consumers are orchestrator recovery and Stage 6 quoting; dispatches receive only particular decision words, not the whole ledger. SRC-1, `academic-pipeline/agents/pipeline_orchestrator_agent.md`, `academic-pipeline/agents/state_tracker_agent.md`.

> - **Keep it local.** Never put the whole ledger into a dispatch; a dispatch that carries a decision quotes only that decision's words (§ Checkpoint authority fidelity). Never name the ledger as a supporting file for the Codex audit wrapper. When the Stage 6 record quotes the initial instructions or a decision, take the words from what `show` prints.
> --- `academic-pipeline/agents/pipeline_orchestrator_agent.md`

Read-back triggers are after compaction, on resume, after every subagent return and at stage close. Claims/expected-steps files select comparison against purported decisions/outcomes, not topic relevance. `show` supplies only the prefix before a chain break. Named-file changes invalidate receipt outcomes. Source notes that fabricated entries, lost tails and restored old copies remain outside the hash guarantee. No complete durable thought trace or automatic reasoning-to-instruction synthesis is established.

#### On [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery)

Retained context comprises passport boundary state, artifact references and separate run-ledger receipts. Reset replaces raw dialogue with selected artifacts only if a fresh host session is actually used. A path is a reload instruction, not a live reference already inside the model window. In-session override changes declared authority but cannot erase older tokens. No numeric savings or measured budget is supported. SRC-1, `academic-pipeline/references/passport_as_reset_boundary.md`.

> - Do NOT ask the user to re-summarize prior stages; the passport is authoritative. Load artifacts by reference (paths or IDs recorded in the entry).
> --- `academic-pipeline/references/passport_as_reset_boundary.md`

The later consumer is the resumed orchestrator, which selects an unconsumed matching boundary hash and loads named artifacts. Sprint contracts and audit/compliance history survive by passport inclusion. Observer session state does not cross reset; reading-probe counters restart. Audit history is not blindly trusted: with the audit gate active and user agreement, current tuple selection, superseding-proposal preflight and file/hash/schema re-verification can reject reuse and require a fresh proposal. Historical stale entries remain history and do not block unrelated transitions. This is the inspected reset contract, not an audit-helper implementation guarantee.

#### On [RT-RTE-command-dispatch](runtime.md#rt-rte-command-dispatch)

Pi persists only an ARS activation bit as a custom host-session entry, then restores the latest applicable branch entry on session start/tree change. The later consumer is adapter control logic selecting whether to inject compatibility guidance, not a model recalling a paper. Raw prompt/command text is reloaded static material. Host session storage format and compaction of other turns are external. SRC-1, `pi/wrapper.js`.

> const state = ctx.sessionManager.getBranch()
>       .filter((entry) => entry.type === "custom" && entry.customType === stateEntryType)
>       .pop();
> --- `pi/wrapper.js`

#### On [RT-RTE-revision-review](runtime.md#rt-rte-revision-review)

The retained drafts/roadmap/author sidecar/patch/evidence bundle carry external manuscript revision history, not automatically revised ARS method text. Raw artifacts and derived traceability remain distinct. Criteria-first and persuasion-blind phases select exposure order; earlier transcripts are kept out only with actual isolated dispatch. The frame analogy fits selected inputs and typed returns; sequential inline fallback cannot evict what the foreground already saw. Supplied runtime establishes the contract and its apply/checker audit gap; this member does not promote that to observed semantic preservation.

#### On [RT-RTE-evaluation-admission](runtime.md#rt-rte-evaluation-admission)

Saved baseline/compare reports are derived measurement memory consumed by a later regression checker. Numeric shared-task metrics, acknowledgement text and issue references affect its admission output, not directly a research model's context. The supplied source passages support a maintainer-controlled evaluation capability; no retained report-to-live-method installation route or causal later benefit is established.

## Write side

Admission varies by artifact, not by the generic fact of file writing. Folder scanning admits parseable filenames and logs rejects; screening export admits sufficient metadata after prior decision processing. Neither requires a new human approval for every emitted entry. Later corpus consumers are prohibited from editing the input corpus; their output bibliography is a new selection. Metadata enrichment is a separate write surface: the inspected bibliography instructions name `scripts/tortured_phrase_screening.py enrich-passport` with explicit snapshot/manifest and distinct output path, preserving the input passport. Its matcher implementation and all other adapters were not audited; this prevents a package-wide curation guarantee. SRC-1, `deep-research/agents/bibliography_agent.md`.

The cache automatically reduces resolver responses to reusable decisions; software version/type/age checks admit later reuse, while a generic API caller can write dictionaries independently. Reading-state control instead belongs to user declarations; software refuses invalid keys/logs and scopes, and rescission persists for later resolution. Inquiry control preserves AI origin separately from author adoption; activity control uses explicit store selection and post-terminal deterministic extraction. These mechanisms retain different reasons: corpus notes retain screening rationale, the inquiry ledger retains original surfaced/adopted text, while cached resolver decisions do not retain full underlying scholarly evidence. See their object/route records above.

Host compaction is an external raw-turn-to-model-summary transformation; summary generation, trimming policy and exact preserved tail are uninspected. ARS does not make that summary a reliable decision receipt. The orchestrator instead prescribes event capture before loss, claims comparison afterwards, and refusal/re-asking where the ledger cannot back a decision. State counters take the higher recovered value to prevent a forgotten retry count reopening a limit. These are recovery controls over preserved evidence, not proof that no user intention is ever lost. See the run-ledger annotation and [RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery).

Revision rejection, finalizer refusal, reset duplicate-consumption refusal, stale audit reuse rejection and evaluation regression checks are retained in the supplied runtime routes. Their different rollback domains must stay separate: a rejected patch preserves its base by contract; a broken ledger is not silently repaired; cache invalidation recomputes rather than restores an earlier truth; activity deletion removes history without changing terminal outcomes. No uniform global rollback mechanism is established.

## Read-back

The explicit consumer routes are corpus-to-literature role, cache-to-verification summary, read-log-to-anchor resolver/finalizer, inquiry-to-checkpoint summary, activity-to-human advisory, and passport/run-ledger-to-resumed orchestrator. They differ from a generic storage method with no caller. Criteria-binding validation checks explicitly supplied context/registry identity before a handoff; receipt persistence alone does not establish substantive criterion consumption. Process summaries provide a human output; their lesson content has no established later automated reader.

Automatic delivery is local and conditional, not an autonomous global memory service: Pi session events restore activation; cache lookups happen when verification requests a composite key; inquiry summaries display at named checkpoint moments. Each selector's inputs, retained subset and authority are recorded above. None warrants inferring semantic retrieval or an unspecified context budget.

Working-context boundaries remain host-dependent. Screening workers get selected batch/protocol inputs and return typed decisions; re-review phases order criteria/evidence/response visibility; reset asks the human to discard the old session and reload file-selected state. Subagent frames can keep worker transcripts out and return only results, but the model window has no dereferenceable pointers. A fresh artifact read copies content into context; retained paths alone do not perform that read. Plain shared-conversation accumulation and in-session authority declarations are not physical eviction. SRC-1, `academic-pipeline/references/passport_as_reset_boundary.md`; supplied [RT-RTE-screening-fanout](runtime.md#rt-rte-screening-fanout), [RT-RTE-revision-review](runtime.md#rt-rte-revision-review).

## Integration issues

1. **No supplied fact correction required.** The runtime's verification-cache statement is broad; this member narrows its payload account with direct wrapper evidence: the generic store can hold a dictionary, but the inspected producer stores versioned match/query decisions, not complete resolver responses. [MEM-OBJ-verification-cache](#mem-obj-verification-cache), [MEM-RTE-cache-verification](#mem-rte-cache-verification), [RT-RTE-final-output](runtime.md#rt-rte-final-output). This prevents treating a cached match as retained full source evidence.
2. **Referent overlaps, not replacement.** Corpus reuse explicitly isolates a part of screening fan-out. Read attestations/cache are distinct inputs/routes overlapping final-output verification; inquiry is distinct from run/reset recovery; activity history is distinct from evaluated-change admission. All new declarations identify their closest supplied records. No duplicate object identity or supersession is asserted.
3. **Included optional mechanisms remain partially inspected.** Inquiry replay/publication internals, criteria resolver/all consumer bodies, non-folder adapters, local contamination/retraction enrichment and complete audit/package/revision helper implementations are available but not fully audited. Their names, known behavior and prevented guarantees remain in the coverage table and records; reconciliation must not infer complete admission/rollback/consumer coverage from the ordinary route.
4. **Human versus software approval remains local.** Import invocation is not per-entry approval; generic cache writes have unresolved caller provenance; criteria initialization's declaration control is incompletely inspected; activity deletion confirms tokens, not independently authenticated human identity. These prevent uniform human-curation classifications. [MEM-RTE-corpus-reuse](#mem-rte-corpus-reuse), [MEM-RTE-cache-verification](#mem-rte-cache-verification), [MEM-OBJ-review-criteria-binding](#mem-obj-review-criteria-binding), [MEM-RTE-activity-history](#mem-rte-activity-history).
5. **No model-learning inference from retained histories.** Host summary generation is opaque; ledger recovery preserves words/receipts, not learned method rules. Activity history is explicitly forbidden from model input; process lessons have no established automated reader. Any learning, reflection or exercised self-improvement classification needs additional route-specific evidence rather than persistence alone. [MEM-OBJ-process-record](#mem-obj-process-record), [MEM-RTE-activity-history](#mem-rte-activity-history), [RT-OBJ-run-ledger](runtime.md#rt-obj-run-ledger).

## Limitations and checks

This is source inspection with explicit partial-helper coverage, not an observed run or causal experiment. Presence, intended delivery, actual activation and benefit remain separate. Source/model trust rules are model instructions unless the named code check enforces a narrower property. Provider weights, host compaction implementation, actual tool grants, scholarly-source truth and human compliance remain external/uninspected. No source ID, boundary revision or supplied member was changed. Report identity repeats the supplied boundary/run values; newly inspected paths all belong to SRC-1 at the checked commit. The supplied method/types/records contract were read, including bounded-range continuations.

Validation result: the required deterministic validate-output check passed. This check assesses format/quotation occurrence and invocation identity, not analytical correctness or acceptance.
