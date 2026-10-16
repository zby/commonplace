---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Echel memory: separate legacy prompt delivery and canonical review, query, staleness and recovery paths."
run-id: AAS-2026-10-15-echel-08d27848b99a-01
source-identity: https://github.com/alirezabbasi/echel
reviewed-boundary: aee36de4d2d1c404fb36e9ad68cc0a920784ee61
---

# Echel memory report

## Boundary and evidence

This report covers the frozen repository registered as SRC-1 in [boundary](boundary.md#source-register). It includes both storage families, the context/run/verification CLI, canonical clarification, query and maintenance APIs, and evaluation artifacts. It excludes Hermes internals and provider state, external artifact bytes not supplied in the repository, and deployed identity/filesystem controls. These exclusions prevent conclusions about runtime compaction, model learning, actual agent compliance, authentication or effective revocation inside an already launched session.

The memory boundary follows runtime's actual consumer routes, not the word “canonical” in a class description. Canonical records and legacy files share a `.echel` root but differ in shape, paths and callers. The current CLI initializes canonical records and executes legacy work. The mismatch is preserved in [RT-RTE-idea-init](runtime.md#rt-rte-idea-init), [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) and [RT-RTE-compile-run](runtime.md#rt-rte-compile-run); no continuous fresh-init-to-agent journey is inferred.

Direct inspection added canonical index/query, clarification, lifecycle, findings, relationships, profiles, transaction, migration, portability and integrity service bodies and schema definitions. It also re-read CLI, compiler, legacy store/model/verification and the synthetic kernel evaluator. This is SRC-1 implementation evidence. Supplied runtime records provide initial authority, adapter, initialization and skill findings; their quoted passages are reused by citation. No target execution occurred. Available tests and benchmark assets do not establish passing operation.

| Entry point or operation | Source path in SRC-1 | Coverage and limit |
|---|---|---|
| CLI init; direct FileStore initialization/add/work | `src/echel/cli/main.py`, `src/echel/storage/files.py` | Supplied [RT-RTE-idea-init](runtime.md#rt-rte-idea-init), [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow); direct layout/model checks here |
| Context and run, including direct adapter | `src/echel/context/compiler.py`, `src/echel/cli/main.py` | Direct compiler/CLI read; annotations on [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context), [RT-RTE-compile-run](runtime.md#rt-rte-compile-run); adapter supplied by runtime |
| Verify and retained outcomes | `src/echel/verification/runner.py` | Direct read; [MEM-OBJ-run](#mem-obj-run), [MEM-OBJ-evidence](#mem-obj-evidence); no demonstrated evidence-to-knowledge consumer |
| Canonical load/scan/write and protected decisions | `src/echel/storage/records.py`, `src/echel/authority.py` | Store directly inspected; authority supplied by [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide) |
| Clarify | `src/echel/methodology/clarification.py` | [MEM-RTE-clarification-read](#mem-rte-clarification-read); direct read |
| Search/reverse links/impact; index rebuild/discard | `src/echel/queries.py`, `src/echel/storage/index.py` | [MEM-RTE-canonical-query](#mem-rte-canonical-query); direct read; library return, not prompt injection |
| Findings and relationship creation; finding resolution/dismissal | `src/echel/findings.py`, `src/echel/relationships.py` | [MEM-RTE-finding-maintenance](#mem-rte-finding-maintenance); direct read |
| Maturity/profile and backward revision | `src/echel/lifecycle.py`, `src/echel/profiles.py` | [MEM-RTE-policy-revision](#mem-rte-policy-revision), [MEM-RTE-staleness-propagation](#mem-rte-staleness-propagation); direct read |
| Multi-record recovery, migration, import/export, integrity | `src/echel/storage/transactions.py`, `src/echel/migrations.py`, `src/echel/portability.py`, `src/echel/integrity.py` | [MEM-RTE-storage-maintenance](#mem-rte-storage-maintenance); direct substantive bodies; helper-level fault/security audit not attempted |
| Canonical artifacts, tasks, runs, evidence, releases, learnings | `src/echel/schemas/v1/record.schema.json` | Inventory in [MEM-OBJ-canonical-records](#mem-obj-canonical-records); direct schema read. Generic storage/query is known; specialized execution/adoption consumers not established |
| Static skills and source contribution | `skills/implementation/SKILL.md`, `CONTRIBUTING.md` | Supplied [RT-BAP-implementation-skill](runtime.md#rt-bap-implementation-skill), [RT-RTE-source-admission](runtime.md#rt-rte-source-admission); not automatically loaded or revised memory |
| Synthetic evaluation | `benchmarks/kernel/gate.py` | Direct evaluator read; [MEM-CLM-kernel-scope](#mem-clm-kernel-scope); scenario execution and model effects uninspected |
| Hook/tool registration alternatives | `pyproject.toml`, `src/echel/cli/main.py`, `src/` | Source search for hook/register/entry-points/scripts/compaction/summarization and dispatch inspection found the CLI entry point and exposed services above, not another supplied prompt-injection hook. Search is bounded, not evidence about external Hermes plugins |

## Core ideas

1. Echel's demonstrated source architecture is two memory planes. Legacy knowledge and open findings reach an external agent through explicit work relationships. Canonical records support attributed decisions, structured diagnostics and query consumers, but are not read by that compiler. See [RT-RTE-compile-run](runtime.md#rt-rte-compile-run) and [MEM-OBJ-canonical-records](#mem-obj-canonical-records).
2. “Authoritative” is not accepted-only selection. Knowledge status is displayed, not filtered. Canonical clarification also lets proposed claim kinds suppress questions, while canonical maturity requires accepted claims. These consumers have different trust rules: [MEM-RTE-clarification-read](#mem-rte-clarification-read), [MEM-RTE-policy-revision](#mem-rte-policy-revision).
3. A canonical index is a replaceable projection, not promoted knowledge. Search reloads files and checks freshness; withdrawal changes consumer predicates rather than erasing content. [MEM-RTE-canonical-query](#mem-rte-canonical-query) and [MEM-RTE-staleness-propagation](#mem-rte-staleness-propagation) retain those distinctions.
4. Run summaries and verification outcomes are retained traces. Their existence does not establish automatic experience-derived guidance or later agent read-back. [MEM-OBJ-run](#mem-obj-run) and [MEM-OBJ-evidence](#mem-obj-evidence) identify precisely what survives.

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-canonical-records
Label: Canonical record families

Source-native identity: `CanonicalRecordStore` records at `.echel/project.json` and `.echel/records/<collection>/<local>.json`, with colon-namespaced IDs. Storage substrate: local JSON files. Representational form: symbolic envelopes, identifiers, predicates, statuses and transitions; natural-language statements, outcomes, observations, implications and reasons interpreted by callers. Lineage: caller-authored records, initializer-produced raw idea, and service-produced revisions. This container spans several runtime routes, not one supplied object; closest records are [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) and [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide). It does not duplicate the in-process compiled context.

Operative parts and consumers differ (SRC-1, `src/echel/schemas/v1/record.schema.json`, `src/echel/storage/layout.py`, `src/echel/queries.py`, `src/echel/lifecycle.py`):

| Part | Retained content and actual inspected consumer |
|---|---|
| Project | Name/mode plus symbolic maturity/profile; profile/lifecycle select policies; clarification uses project identity |
| Claim | Natural-language statement plus kind/stage/status/confidence; clarification uses kind/status, maturity uses accepted stage/kind, query returns full record |
| Decision | Title/outcome/alternatives plus status/authority; authority and staleness services operate on it; generic query returns it, not legacy compiler |
| Learning | Observation/implication/evidence IDs plus status/authority; protected review and staleness apply; generic query returns it. Name and `applied` state do not establish trace derivation or downstream adoption |
| Relationship | Source/predicate/target plus reason/policy/provenance; query traversal, finding targets and staleness propagation consume the symbolic edges; query returns readable reasons |
| Finding | Statement/kind plus severity/status/decision rationale; finding assessment and lifecycle gate consume status/severity and affects edges |
| Work item | Objective/title/acceptance, priority/status/dependencies; generic canonical storage/query known, legacy `work` consumer is a different schema |
| Task specification | Objective/instructions/acceptance/verification and work reference; revision fixed to 1 by schema. Canonical execution consumer not established |
| Run | Task specification/runtime/status/context digest; generic storage/query known; distinct from legacy Run below |
| Evidence | Subject/kind/summary/result and optional artifact reference; no inspected automatic promotion consumer |
| Release | Version/status/artifact and evidence IDs; `withdrawn` is a schema state, not an inspected deployment withdrawal mechanism |
| Artifact | Kind/URI/digest: access metadata, not the referred payload. No automatic dereference or payload verification established by generic query |

Each family can be loaded/scanned and exported; index/query operate on their records. Specialized model consumers for canonical tasks, evidence, releases and learnings remain unestablished. Their payload origins are caller-dependent, not necessarily human or model-produced. Protected decision rationale persists in authority metadata; staleness reason persists separately. Query exposes both, whereas lifecycle's gate does not assess their semantic soundness.

The store validates schemas and expectations, not authenticated authorship:

> self.schemas.validate(record)
> path = self._record_path(record)
> --- `src/echel/storage/records.py:189-190`

This exact passage is in `preview_write`; it does not imply a semantic approval gate. Direct writes can install schema-valid authority fields without traversing [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide).

#### MEM-OBJ-disposable-index
Label: DisposableIndex projection

Source-native identity: `DisposableIndex`, `.echel/cache/index.sqlite3`. Storage substrate: SQLite/FTS5. Representational form: symbolic rows, lexical search index and byte fingerprint, not embeddings or model parameters. Lineage: rebuild scans canonical files and derives searchable strings, relationship rows and full JSON copies; `extensions` values are excluded from searchable text. QueryService returns freshly loaded canonical content, not the cached copy as authority (SRC-1, `src/echel/storage/index.py`, `src/echel/queries.py`). Distinct from [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context): search acceleration rather than model text.

> if metadata.get("fingerprint") != current:
>     connection.close()
>     raise IndexError(
>         "ECHEL-INDEX-STALE", self.path, "canonical records changed; rebuild the index"
>     )
> --- `src/echel/storage/index.py`

The retained projection has no independent semantic admission. Code mechanically includes schema-valid records regardless of accepted status. Discard removes only this database; canonical records remain.

#### MEM-OBJ-run
Label: Legacy Run retention

Source-native identity: `Run` in `.echel/runs/RUN-*.json`. Storage: local JSON. Form: symbolic runtime/model/work identity, command, digest/status/exit code plus natural-language stdout tail. Lineage: CLI preview or subprocess return, not a model-authored distilled lesson. Different from [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context), which is input; associated producer is [RT-RTE-compile-run](runtime.md#rt-rte-compile-run). SRC-1, `src/echel/cli/main.py`, `src/echel/model/records.py`:

> run.summary = result.stdout[-4000:]
> --- `src/echel/cli/main.py`

The command retains prompt text as argv, so retention is not only a digest. Preview records are not execution traces. Executed summaries omit earlier stdout and stderr; no full session/tool transcript or reasoning is reconstructed. `FileStore.get/records` affords later retrieval, but the compiler does not select runs. The automatic write has no per-summary review; caller grants execution, not approval of the returned text. Later behavior-shaping use remains unestablished.

#### MEM-OBJ-evidence
Label: Legacy Evidence retention

Source-native identity: verification `Evidence` at `.echel/evidence/EVID-*.json`. Storage: JSON. Form: symbolic subject/argv/exit code/checksum and generated passed/failed text. Distinct from Run: a different producer, output-loss rule and consumer possibility. Closest supplied record is [RT-RTE-verify-work](runtime.md#rt-rte-verify-work). SRC-1, `src/echel/verification/runner.py`:

> output = completed.stdout + completed.stderr
> --- `src/echel/verification/runner.py`

> checksum=hashlib.sha256(output.encode("utf-8")).hexdigest(),
> --- `src/echel/verification/runner.py`

Only the checksum of these bytes persists, not the output itself. A digest is not a readable diagnostic or reference answer. The runner records each command result automatically without a content approval gate; no subsequent knowledge transformation or compiler selection is wired there. FileStore retrieval is a capability, not proof of a later consumer invocation.

#### MEM-OBJ-recovery-state
Label: Transaction and migration recovery state

Source-native identities: transaction `journal.json` and staged records; migration journals, staged target bytes and exact source-byte backups. Storage: `.echel/transactions`, `.echel/migrations`, `.echel/backups`. Form: symbolic state/expectations/digests/paths plus copied JSON payloads; lineage is write plans, not conversation traces. Consumers are recovery/commit/rollback services, not model context. Distinct from runtime's single-record guarantee and [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide): these are multi-record installation/recovery objects. SRC-1, `src/echel/storage/transactions.py`, `src/echel/migrations.py`:

> "committing transactions must roll forward through recovery",
> --- `src/echel/storage/transactions.py`

Successful transaction commit deletes its staging directory. Migration keeps backups for explicit restoration, guarded against post-migration target changes. These are operational memory used by later recovery calls, not evidence-derived guidance.

### Routes

#### MEM-RTE-clarification-read
Label: Canonical clarification read

Endpoints/progression: CLI `clarify` → discover canonical store → scan project/claims → code selects first unresolved nonexcluded problem gap → display question/reason/basis. Owner is deterministic code; caller controls temporary exclusion IDs. Distinct from initialization in [RT-RTE-idea-init](runtime.md#rt-rte-idea-init): later retained-claim consumption, not creation. SRC-1, `src/echel/methodology/clarification.py`:

> if item.record["status"] not in {"rejected", "superseded", "stale"}
> --- `src/echel/methodology/clarification.py`

- Immediate return: Question prompt/reason/expected claim kind, raw-idea ID@revision basis, unresolved kinds and next action.
- Later read-back: Each invocation scans current retained claims; active claim kinds suppress corresponding fixed questions.
- Delegated visibility: inapplicable — no agent invocation; CLI displays the selected question.
- Selection predicate: Exactly one project and one raw-idea claim; first gap whose kind is absent and ID not excluded. Proposed claims count as active. Raw-idea cardinality counts all raw ideas, not just active ones.
- Invalidation or expiry: Changed claims change next selection; exclusions are supplied anew, not persisted as a dialogue checkpoint.
- Activation or effect: Retained symbolic kind/status affects generated question selection; no semantic assessment of statement truth.
- Evidence limits: Implementation only; no observed interaction or automatic answer capture.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Read-only selection is not knowledge admission. Fixed question reasons are shipped doctrine, not learned from the raw idea. No answer oracle or comparison experiment is present; this is an open caller-driven clarification request.

#### MEM-RTE-canonical-query
Label: Canonical query read-back

Endpoints/progression: explicit library query → current disposable index → hit IDs → canonical reload and provenance wrapper → final freshness check → caller. Owner: code; caller supplies query/type/limit or origin/predicate/depth. Distinct from [RT-RTE-compile-run](runtime.md#rt-rte-compile-run): no agent launch, prompt or legacy collection. SRC-1, `src/echel/queries.py`, `src/echel/storage/index.py`:

> hits = self.index.search(query, record_type=record_type, limit=limit)
> records = tuple(self._from_search_hit(hit) for hit in hits)
> self.index.assert_current()
> return records
> --- `src/echel/queries.py`

- Immediate return: ProvenancedRecord tuples, incoming link explanations or impact paths with reasons/provenance.
- Later read-back: Canonical content accumulated across calls is selected by lexical search or graph relationships and returned to the requesting caller role. A storage load alone would not establish this selector/consumer chain.
- Delegated visibility: inapplicable — no delegation in this service; model delivery would require additional wiring.
- Selection predicate: FTS MATCH/BM25 with ID tie-break; default 20, permitted 1–100 results and optional type. Reverse links use incoming edges/predicate. Impact uses fixed directional predicates, visited set and default depth 3, permitted 1–10.
- Invalidation or expiry: Byte fingerprint mismatch refuses query until rebuild; no TTL. Reload compares hit identity/revision/path and relationship content.
- Activation or effect: Returns retained records and reasons for inspection; downstream caller decisions unobserved.
- Evidence limits: Library implementation establishes caller-facing retrieval, not a deployed assistant retrieval tool or prompt route. Concurrency between checks is not experimentally tested.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Index rebuild/discard is caller-triggered software projection and cleanup, not human per-record approval. Query preserves rejected/stale content unless caller filters by other criteria; result inclusion does not confer accepted authority. Source trust is schema/identity/byte freshness, not truth verification.

#### MEM-RTE-finding-maintenance
Label: Canonical finding maintenance

Endpoints/progression: caller statement/kind/severity/targets/provenance → finding plus justified affects relationships → transaction; later Principal/rationale/action → finding status revision. Owner: caller proposes, software validates, human-labelled capability decides resolution/acceptance/dismissal. Distinct from [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide): finding states and downstream gate, not protected claim acceptance. SRC-1, `src/echel/findings.py`, `src/echel/relationships.py`:

> "status": "open",
> --- `src/echel/findings.py`

> active = finding["status"] in ACTIVE_FINDING_STATES
> --- `src/echel/findings.py`

- Immediate return: Preview finding/impact or applied transaction; later decision plan/record.
- Later read-back: Finding assessment and lifecycle reload finding status/severity and affects edges; resolved/dismissed findings become inactive and stop contributing gate impact.
- Delegated visibility: inapplicable — canonical service does not invoke an agent or update legacy findings.
- Selection predicate: Caller-selected unique affected IDs and permitted finding kinds/severities; relationship endpoint/predicate policy and nonempty reason; decisions limited to active states and finding:decide human-labelled Principal.
- Invalidation or expiry: Revision/expectation conflicts reject writes; inactive finding cannot be redecided through this route; no expiry.
- Activation or effect: Retains proposed criticism and attributable disposition; does not itself rewrite the challenged knowledge.
- Evidence limits: Statements are caller content, not automatically diagnosed contradictions; identity authenticity and review quality unresolved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Creation does not require human approval; it admits an open finding through software structural checks. Relationship authorship is caller-supplied; code produces its physical records and generated affects reasons. Decision requires rationale, time and capability labels; schema/conflict checks can veto. No semantic answer oracle or autonomous repair is supplied. Recovery uses transaction recovery or reload/retry; resolution is not automatic rollback of prior knowledge. This is an open review API, not an evaluated improvement curriculum.

#### MEM-RTE-staleness-propagation
Label: Backward staleness propagation

Endpoints/progression: caller active finding/root/Principal/reason → traverse informs/supports → copy accepted protected records → status stale with staleness rationale → multi-record transaction. Owner: caller selects revision, code traverses/validates. This extends, rather than duplicates, [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide): withdrawal from accepted reliance, not acceptance/rejection of a proposed record. SRC-1, `src/echel/lifecycle.py`:

> updated["status"] = "stale"
> updated["revision"] = loaded.record["revision"] + 1
> --- `src/echel/lifecycle.py`

- Immediate return: BackwardRevision preview or applied transaction.
- Later read-back: Clarification excludes stale claim kinds; maturity no longer counts stale claims as accepted. Query still exposes records and retained staleness reason. Index queries require rebuild after changed canonical bytes.
- Delegated visibility: inapplicable — no runtime delivery; already delivered legacy prompts are not revoked.
- Selection predicate: Active finding must explicitly affect root; root must be accepted protected knowledge; forward informs/supports traversal through protected claim/decision/learning nodes; only accepted records receive stale revisions.
- Invalidation or expiry: Changes persist until another explicit write; reason includes finding/root/actor/prior revision. No time-based forgetting.
- Activation or effect: Changes consumer eligibility and retains why reliance was withdrawn; does not delete statements or derive replacements.
- Evidence limits: Source supports structural propagation, not semantic sufficiency of dependency edges or actual exercised repair.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission requires caller-supplied human knowledge:decide capability and reason/time; software can veto inactive/unrelated findings, unaccepted root or invalid transition. Caller supplies criticism; code supplies conservative status changes, not an answer oracle. Transaction recovery rolls forward durable commit intent; it is not semantic undo. Open user-driven revision; no claim of a theory-building cycle or learning benefit follows from the status change.

#### MEM-RTE-policy-revision
Label: Canonical lifecycle policy revision

Endpoints/progression: retained project profile/maturity and claims/findings → assessment; authorized caller rationale → profile or maturity revision → canonical write. Owner: code computes usable/missing/blocking; human-labelled Principal chooses requested transition. Closest supplied route [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow) is distinct legacy stage logic with force bypass. SRC-1, `src/echel/lifecycle.py`, `src/echel/profiles.py`:

> if loaded.record.get("status") == "accepted"
> and loaded.record.get("stage") == stage.id
> --- `src/echel/lifecycle.py`

- Immediate return: Assessment/inspection, preview transition or applied write.
- Later read-back: Persisted project profile changes the registered required-kind policy used in subsequent assessments; accepted claim kinds and active finding severity determine usability.
- Delegated visibility: inapplicable — no prompt or agent invocation.
- Selection predicate: Current stage/profile; accepted claims at that stage; active findings affecting selected required claim IDs. Error/critical block, warning/info caution. Profile selection requires registered target; advance requires usable stage and a successor.
- Invalidation or expiry: Reassessment reads current files; revisions guarded by record expectations; no expiration or automatic backward maturity movement.
- Activation or effect: Updates symbolic project policy/stage and retains transition rationale; profile labels select shipped policy rather than rewriting policy text.
- Evidence limits: No semantic assessment of claims or observed human decision quality; duplicate accepted kinds collapse into a dictionary, not a guarantee of inspecting every equivalent claim's findings.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Caller proposes target; human-labelled profile:change or lifecycle:advance capability and rationale/time provide admission metadata. Software vetoes disallowed/unchanged/unusable transitions. No expected product answer oracle; kind presence and severity are fixed predicates. Recovery is reload/retry, not automatic rollback. Profile changes are explicit policy selection in an open workflow, not trace-trained policy improvement.

#### MEM-RTE-storage-maintenance
Label: Canonical storage maintenance

Endpoints/progression: explicit library calls → validate canonical state or bundle/version plan → optionally stage/commit/import/migrate/recover → canonical files and operational artifacts. Owner is caller; deterministic software performs installation. Distinct from [RT-RTE-source-admission](runtime.md#rt-rte-source-admission) and [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide): storage transport/recovery, not source merge or semantic knowledge review. SRC-1, `src/echel/storage/transactions.py`, `src/echel/migrations.py`, `src/echel/portability.py`, `src/echel/integrity.py`:

> "portable import does not merge with existing canonical records",
> --- `src/echel/portability.py`

> migrated.update(set_fields)
> migrated["schema_version"] = 1
> --- `src/echel/migrations.py`

- Immediate return: Integrity report, export bytes/fingerprint, import/migration/transaction plan or installation/recovery result.
- Later read-back: Commit/recovery reload staged intent; rollback reads backups; imported/migrated canonical records feed query/clarification/lifecycle on later calls. Export alone does not demonstrate a later import.
- Delegated visibility: inapplicable — these services invoke no agent.
- Selection predicate: Export scans all canonical families. Import requires empty target, supported schemas, canonical sorted paths, unique IDs, included relationship endpoints, matching digest and size bounds. Migration supports uniform version 0→1, explicit caller field removals/sets and target validation; current version is unchanged.
- Invalidation or expiry: Canonical digest/expectation conflicts reject; migration rollback refuses changed target bytes; prepared transactions can be discarded, committing intent must roll forward. Successful transaction cleanup removes journals/staged copies, not admitted records.
- Activation or effect: Replaces canonical representation, installs transported content or finishes earlier writes; integrity diagnostics return remedies but do not apply them.
- Evidence limits: No authenticated bundle origin, per-content human admission, deployed crash test or cross-record read-isolation guarantee is established. Helper-level security and all exceptional paths were not audited.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is software structural validation plus caller initiation, not human review of each imported claim. Authorship remains bundle/resolution-supplier dependent. Migration can edit content through explicit resolutions; schema version change alone is not semantic curation. Backup/restore and commit-state recovery are mechanical, with no answer oracle for product truth. This route intentionally groups storage operations sharing caller-driven structural admission; they do not inherit authority-service authentication. Integrity can detect corruption/orphans/stale cache and recommend repair; retaining a report or remedy is not an automatic repair learner.

### Claims

#### MEM-CLM-kernel-scope
Label: Synthetic kernel evaluation scope

Claimed operation: the kernel gate measures synthetic SQL status/search/reverse-link performance, not end-to-end canonical query freshness/reload or agent context benefit. SRC-1, `benchmarks/kernel/gate.py`:

> "context compilation and model execution are owned by downstream benchmark tasks",
> --- `benchmarks/kernel/gate.py`

It writes synthetic database rows directly, times SQL on that connection, and emits a report; it does not run QueryService's canonical snapshot/reload chain. The supplied local JSON result remains reported operation as scoped in [boundary](boundary.md#boundary-and-evidence). No inspected automatic consumer changes memory, admission policy or prompts in response to gate metrics. Distinct from [RT-CLM-runtime-boundary](runtime.md#rt-clm-runtime-boundary): evaluator scope, not runtime ownership. This limits performance and improvement claims; it does not establish poor performance.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### MEM-BAP-canonical-gates
Label: Canonical retained eligibility gates

Consumer: ClarificationService and LifecycleService. Channel: canonical store scan/load on later explicit calls. Force: fixed symbolic rules over kinds, status, stage, severity, relationships and project profile; no semantic obedience to the natural-language statement is required. Horizon: later invocations in the same retained repository; observed repeated use uninspected. Reasons remain readable through query, but gate predicates do not evaluate their meaning. Evidence: SRC-1, `src/echel/methodology/clarification.py`, `src/echel/lifecycle.py`, `src/echel/profiles.py`, through [MEM-RTE-clarification-read](#mem-rte-clarification-read), [MEM-RTE-policy-revision](#mem-rte-policy-revision). Distinct from [RT-BAP-context-prompt](runtime.md#rt-bap-context-prompt): deterministic canonical control, not natural-language model guidance.

## Annotations

#### On [RT-OBJ-compiled-context](runtime.md#rt-obj-compiled-context)

Memory-specific consumption split: JSON context output preserves complete selected record dictionaries, while actual run text supplies only selected visible fields. Legacy knowledge `sources`/tags and work dependency/status metadata are not rendered. The digest covers this rendering, not every retained source field (SRC-1, `src/echel/context/compiler.py`). Model-facing statements are natural language; IDs/status/confidence annotations do not enforce acceptance. Canonical authority/staleness rationale is not reachable through this compiler at all.

#### On [RT-RTE-compile-run](runtime.md#rt-rte-compile-run)

Read-back trigger is explicit context/run invocation. Code selects explicit work relationships, open findings intersecting those IDs, then renders text; no token budget, ranker, transitive closure or context compaction is implemented in this compiler. All selected statements are delivered via Hermes request; unrelated content remains on disk and may be reachable through tools. The current prompt is copied by value into command arguments, not a dereferenceable reference. This resembles a task input frame only at the Echel boundary: no inspected frame isolation, subagent return policy or pop operation is implemented there. Hermes window management and checkpoint alternatives remain opaque, not absent. SRC-1, `src/echel/context/compiler.py`, `src/echel/cli/main.py`; external control limits are supplied in the route's runtime evidence.

#### On [RT-RTE-knowledge-decide](runtime.md#rt-rte-knowledge-decide)

Accepted/rejected canonical status and rationale survive as record metadata for later query inspection. Rejection leaves content retained; clarification excludes rejected claims, maturity counts accepted claims only. This is consumer-specific withdrawal rather than file deletion or model-session revocation. Source: SRC-1, `src/echel/methodology/clarification.py`, `src/echel/lifecycle.py`, `src/echel/queries.py`; authority-service evidence is supplied by the cited record. Legacy selection does not inherit these canonical checks.

## Write side

Acquisition has two caller-controlled origins: canonical raw-idea initialization and legacy add/work inputs. Their admission rules are already distinguished by [RT-RTE-idea-init](runtime.md#rt-rte-idea-init) and [RT-RTE-file-workflow](runtime.md#rt-rte-file-workflow). Unknown/authentication-dependent caller identity does not suppress known transformations: compiler rendering, stdout truncation, generated verification summary/checksum, index projection, finding impact, staleness propagation, migration resolution and transaction recovery are inspectable code operations.

Automatic trace-fed writes stop at [MEM-OBJ-run](#mem-obj-run) and [MEM-OBJ-evidence](#mem-obj-evidence): subprocess output → bounded tail or generated outcome/hash → retained file. A durable behavior-shaping derivation and later model consumer are not established by these producers. In particular, a hash cannot reload discarded output. Canonical learning's evidence references provide a representational affordance, not an implemented bridge from these legacy traces. No learned capacity or reason-preserving experience loop is inferred.

Canonical decisions and finding dispositions retain human-labelled rationales. Staleness preserves finding/root/reason rather than silently rewriting the statement. [MEM-RTE-finding-maintenance](#mem-rte-finding-maintenance) and [MEM-RTE-staleness-propagation](#mem-rte-staleness-propagation) separate criticism capture, admission and changed reliance. No automatic semantic replacement follows. Schema-valid direct writes/imports remain alternatives to service-mediated review, so attribution metadata is not universal approval enforcement.

Maintenance has different deletion semantics: index discard removes only a projection; transaction cleanup removes staging; migration rollback restores exact earlier bytes if targets are unchanged; rejected/stale knowledge and resolved/dismissed findings remain retained. Integrity emits remedies without applying them. These distinctions are supported by [MEM-RTE-storage-maintenance](#mem-rte-storage-maintenance) and [MEM-RTE-canonical-query](#mem-rte-canonical-query), not generalized into a system-wide forgetting policy.

## Read-back

The agent-facing route is request-driven: caller chooses work, code chooses related knowledge/open findings, Hermes receives text. It is not unsolicited memory injection. There is no Echel model-context budget beyond relationship exclusion; the 4,000-character stdout retention limit is an output retention rule, not an input token budget. Recompilation reloads current legacy records but does not revoke a prior delivered prompt.

Canonical consumers differ: clarification consumes kind/status for question selection; lifecycle consumes accepted claims, profile and finding impact for gate decisions; QueryService selects and returns retained content/reasons to its explicit caller. Query result limits/depth are selection budgets, not agent window limits. Recovery consumers use durable intent/backups for later installation decisions, not product guidance. See [MEM-BAP-canonical-gates](#mem-bap-canonical-gates), [MEM-RTE-canonical-query](#mem-rte-canonical-query) and [MEM-OBJ-recovery-state](#mem-obj-recovery-state).

Generic record load/scan alone establishes storage capability, not an additional later-consumer route. Canonical artifact payloads, release withdrawal deployment effects, task execution, run/evidence-to-learning adoption, and Hermes summary/checkpoint read-back remain unresolved beyond the specific consumers described here. Static skills are instruction supply only when externally loaded, as [RT-BAP-implementation-skill](runtime.md#rt-bap-implementation-skill) already qualifies.

## Integration issues

- No supplied fact is corrected. The canonical/legacy mismatch and accepted-status delivery weakness independently survive direct compiler/CLI/store inspection. They prevent merging canonical authority guarantees into the legacy agent route.
- No new declaration intentionally duplicates a supplied referent. Run/evidence are outputs of supplied runtime routes, not replacement route records; canonical objects and recovery state span several supplied operations. New canonical routes are distinct from legacy workflow/compile routes. Annotations preserve the existing compiled-context and authority referents.
- Canonical task/run/evidence/release/learning specialized consumers remain unestablished. SRC-1, `src/echel/schemas/v1/record.schema.json`, `src/echel/cli/main.py`, `src/echel/queries.py` support storage, schema and generic retrieval, not canonical agent execution or automatic learned guidance. See [MEM-OBJ-canonical-records](#mem-obj-canonical-records). Do not equate a schema's `applied`/`withdrawn` labels with observed adoption/withdrawal.
- Finding resolution changes gate impact, whereas staleness changes accepted eligibility; neither bridges into legacy findings automatically. [MEM-RTE-finding-maintenance](#mem-rte-finding-maintenance), [MEM-RTE-staleness-propagation](#mem-rte-staleness-propagation), [RT-RTE-compile-run](runtime.md#rt-rte-compile-run). This prevents a universal claim that resolved criticism revokes or repairs every prompt.
- Query returns retained reasons, but only symbolic fields affect inspected automatic gates. Whether a later human/model actually evaluates those reasons is unobserved. [MEM-RTE-canonical-query](#mem-rte-canonical-query), [MEM-BAP-canonical-gates](#mem-bap-canonical-gates). Preserve this limit when assessing content-directed learning or theory use.
- External runtime window management, model parameter changes and alternative checkpoint consumption remain uninspected, as [RT-CMP-runtime-model](runtime.md#rt-cmp-runtime-model) already states. No repository-only search settles provider memory.
- The kernel gate bypasses canonical query overhead and has no inspected feedback-to-memory route. [MEM-CLM-kernel-scope](#mem-clm-kernel-scope) prevents treating reported SQL timings as end-to-end retrieval latency or demonstrated learning benefit.

## Limitations and checks

HEAD was rechecked as `aee36de4d2d1c404fb36e9ad68cc0a920784ee61`, matching the supplied boundary and report identity. All added reads are at SRC-1; no additional source or target execution was introduced. Supplied method/type/records/worker instructions were read completely. Source inspection and bounded searches support implemented wiring, not observed activation or causal benefit. Helper-level durability/security proofs, deployed principal authentication, external artifact payloads, full benchmark scenario execution and Hermes internals remain outside the established conclusions.

Deterministic validation: passed with the supplied `commonplace-run validate-output` command. This checks structure, identities and quotation occurrence, not semantic completeness or acceptance.
