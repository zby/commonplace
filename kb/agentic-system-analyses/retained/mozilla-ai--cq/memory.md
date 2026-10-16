---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "CQ memory: structured advice, local fallback and transfer, review-gated remote retrieval, feedback, optional vectors and auxiliary retained state."
run-id: AAS-2026-10-14-cq-8fb3dc41c334-01
source-identity: "https://github.com/mozilla-ai/cq"
reviewed-boundary: "5765494a3840e5f5a7223c42101f41e85cb9d898"
---

# CQ memory report

## Boundary and evidence

CQ retains knowledge units for later agent queries. This report includes their text, selection and feedback metadata, remote review state, local replacement/deletion capabilities, optional vector derivation, discovery caches, Cursor failure reminders, static instruction installation and operator maintenance. It uses SRC-1 at the frozen revision above. The source register remains in [boundary](boundary.md#source-register). The checkout HEAD was rechecked against the pin and Git status was clean. No target code, tests, examples, provider or service was executed.

Direct source reads establish implementation; prompts and schema descriptions establish doctrine/design. Supplied runtime findings are provisional and explicitly identified below. External host context, model weights, provider embedding provenance and live deployment remain outside the source boundary. Their exclusion prevents conclusions about actual reliance, context-window eviction, deployed confidentiality and learning benefit. Credentials and installed manifests are access/configuration metadata, not task-derived advice; detailed credential lifecycle is not assessed here.

| Entry point or retained part | Source paths under SRC-1 | Coverage and limit |
|---|---|---|
| CLI dispatch and MCP registration | `cli/main.go`, `cli/mcpserver/server.go` | Direct reads confirm query/propose/confirm/flag/status, explicit CLI drain and internal hook. [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query), [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal), [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback). No registered content-edit or server-reflection tool here. |
| Knowledge payload and metadata | `schema/knowledge_unit.json`, `sdk/python/src/cq/models.py`, `sdk/go/client.go` | Direct reads: [MEM-OBJ-insight](#mem-obj-insight), [MEM-OBJ-selection-metadata](#mem-obj-selection-metadata), [MEM-OBJ-flags](#mem-obj-flags), [MEM-OBJ-extensions](#mem-obj-extensions). Arbitrary extension meaning and actual candidate provenance remain unknown. |
| Local SQLite persistence, indexes and reload | `sdk/go/store_sqlite.go`, `sdk/go/store.go`, `sdk/python/src/cq/store.py` | Direct Go insert/query/get/update reads; Python persistence/reload additionally supplied by boundary. [MEM-RTE-store-replacement](#mem-rte-store-replacement), query annotation. No universal custom-store semantics inferred. |
| Alternative stores | `sdk/go/stores/postgres/postgres.go`, `sdk/python/src/cq/stores/postgres.py`, `sdk/python/src/cq/stores/memory.py` | Direct query bodies: domain candidates and shared ranking, without SQLite's FTS expansion. Python in-memory selection uses dictionary values. Durability, all mutation paths and full parity are not exhaustively inspected; those conclusions are prevented. |
| Remote proposal, transfer and feedback | `sdk/go/client.go`, `sdk/go/remote.go`, `sdk/python/src/cq/client.py`, `server/backend/src/cq_server/services/knowledge.py`, `server/backend/src/cq_server/api/routes/knowledge.py`, `server/backend/src/cq_server/models/knowledge.py` | Direct reads supplement [RT-RTE-local-drain](runtime.md#rt-rte-local-drain) and feedback/proposal annotations. Transfer omits evidence/flags; Python also omits extensions. Remote duplicate-flag handling has an integration defect below. |
| Remote review, rejection and alternative review reads | `server/backend/src/cq_server/services/reviews.py`, `server/backend/src/cq_server/repositories/reviews.py`, `server/frontend/src/pages/ReviewPage.tsx` | Direct service/repository/UI excerpts; [RT-RTE-remote-review](runtime.md#rt-rte-remote-review). Retained decisions gate public retrieval, but review readers can still inspect rejected units. UI approve/reject/skip is not content editing. |
| Ordinary remote query | `server/backend/src/cq_server/repositories/knowledge.py` | Direct dispatch and supplied SQL findings in [RT-CLM-approved-query](runtime.md#rt-clm-approved-query); no expiry or supersession enforcement established. |
| Optional vectors | `server/backend/src/cq_server/semsearch/queries.py`, `server/backend/src/cq_server/semsearch/__init__.py` | Direct derivation/query reads: [MEM-OBJ-knowledge-vectors](#mem-obj-knowledge-vectors), query/feedback annotations. Provider internals inaccessible; initial vectors from a pre-existing deployment are uninspected. |
| Reflection and instruction distribution | `sdk/go/prompts/reflect.md`, `sdk/go/prompts/SKILL.md`, `sdk/python/src/cq/reflect.py`, `cli/internal/install/pi.go` | Reflection directly read; other prompt/installer findings supplied by [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection), [RT-RTE-host-installation](runtime.md#rt-rte-host-installation), [RT-OBJ-skill](runtime.md#rt-obj-skill). Full host adapter equivalence remains uninspected. |
| Failure capture and cleanup | `cli/internal/hook/cursor.go` | Direct event, persistence, rendering and cleanup reads; annotations on [RT-OBJ-failure-record](runtime.md#rt-obj-failure-record), [RT-RTE-failure-reminder](runtime.md#rt-rte-failure-reminder). No success pairing or automatic lesson extraction established by this hook. |
| Discovery/cache read-back | `sdk/go/discovery/cache.go`, `sdk/go/discovery/discovery.go`, `sdk/go/remote.go`, `sdk/python/src/cq/discovery/_cache.py`, `sdk/python/src/cq/discovery/_resolver.py` | Direct reads: [MEM-OBJ-node-info](#mem-obj-node-info), [MEM-RTE-discovery-resolution](#mem-rte-discovery-resolution). Persistent endpoint metadata, not retained advice. Full probe validation internals are not inspected. |
| Maintenance and synthetic evaluation | `server/scripts/migrate-team-db.sh`, `server/scripts/migrate-v1.sh`, `server/scripts/seed-kus.py`, `server/scripts/backup-db.sh`, `server/backend/alembic/versions/0001_baseline.py` | Direct migration/seed bodies and supplied backup/schema findings; [MEM-RTE-maintenance-migration](#mem-rte-maintenance-migration). Test source coverage is supplied by boundary, not executed results. Seeds adjust scores by target values, not independent verification. Makefile orchestration and full migration correctness remain uninspected. |

Uninspected available paths are not access gaps or evidenced absences. The inventory covers the operative parts relevant to this account without claiming every file or deployment alternative was audited.

## Core ideas

1. **The retained lesson is text, not a session checkpoint.** A unit carries summary, detail and action. Reflection requests selection and rewriting of session events into that form, followed by ordinary proposal. Neither the compact session summary nor the full raw session has a wired durable store in the supplied reflection route. The host supplies interpretation and application. [MEM-OBJ-insight](#mem-obj-insight), [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection).
2. **Admission and ranking have different authority.** Remote review status gates normal remote reads; confidence influences ordering. A stale/incorrect flag changes confidence and retains a flag but does not revoke review approval or rewrite the advice. Local advice has no corresponding remote review gate. [MEM-OBJ-selection-metadata](#mem-obj-selection-metadata), [MEM-OBJ-flags](#mem-obj-flags), [RT-CLM-approved-query](runtime.md#rt-clm-approved-query).
3. **Local fallback is not a faithful replica.** Drain sends selected content fields, creates a new remote identity and deletes the old local unit after success. It does not carry local confirmations, flags, original observation timestamps or supersession links. Future retrieval can lose the local item before its remote successor is approved. [RT-RTE-local-drain](runtime.md#rt-rte-local-drain), its annotation below.
4. **Context selection is count-bounded retrieval plus a small automatic reminder.** Queries select external knowledge by tags, context and scores; they do not evict host turns. Cursor pushes one clipped failure at stop and clears its file. Reflection requests a dense summary but does not implement compaction. Host frames, delegation, token windows and reload of removed host turns are uninspected. [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query), [RT-RTE-failure-reminder](runtime.md#rt-rte-failure-reminder).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-insight
Label: Knowledge unit insight

Source-native identity: KnowledgeUnit.insight, containing summary/detail/action. Natural-language text is serialized inside local SQLite JSON, SDK PostgreSQL records or remote database unit data; its later host/reviewer consumers interpret meaning. It is distinct from the route [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal), which admits it, and from the shipped [RT-OBJ-skill](runtime.md#rt-obj-skill), which instructs its use. No supplied object record denotes this payload.

Lineage: caller-authored content, optionally extracted/rewritten by the host following reflection; demonstration seed text is another input. The schema limits summary/detail/action to 500/8000/2000 characters. That bounds fields, not the complete model context. Reasons can persist in detail; raw events, verification sources and safety-gate reasoning are not required payload fields. Later query delivers detail and action, under [RT-BAP-knowledge-guidance](runtime.md#rt-bap-knowledge-guidance), with advisory authority rather than automatic execution. Actual source trust and application remain unobserved. SRC-1: `schema/knowledge_unit.json`, `sdk/go/client.go`, `sdk/go/store_sqlite.go`, `sdk/go/prompts/reflect.md`.

> "description": "Tripartite insight: what happened, why it matters, what to do.",
> --- `schema/knowledge_unit.json`

> - **detail** — two to four sentences explaining the context and why this behavior exists or matters.
> - **action** — a concrete instruction on what to do (start with an imperative verb).
> --- `sdk/go/prompts/reflect.md`

#### MEM-OBJ-selection-metadata
Label: Knowledge selection metadata

Source-native identity: unit domains/context/evidence/tier/ID/version/superseded_by and remote row review status/reviewer/time. These are symbolic selector inputs and identifiers, not natural-language explanations. The JSON body and domain-index rows coexist with remote SQL review columns. Version is schema version, not a content-revision history. These fields differ from [MEM-OBJ-insight](#mem-obj-insight) in consumer, transformation and authority. The closest supplied referents are the query, feedback and review routes, not an existing metadata object: [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query), [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback), [RT-RTE-remote-review](runtime.md#rt-rte-remote-review).

Lineage: proposer supplies tags/context; code creates identity, default confidence 0.5 and confirmations 1, plus timestamps; feedback changes evidence; review writes status/reviewer/time separately. Initial confirmations therefore need not represent a separate agent's successful use. Domain normalization produces indexable tags; SQLite FTS duplicates insight text for candidate gathering. FTS is a derived search surface, not a replacement lesson. Review status affects remote visibility; domains/context/confidence affect selection; timestamps and superseded_by have no operative invalidation predicate established in the inspected local query or supplied remote selectors. Do not equate a tier label with isolation. Created_by is retained attribution/access metadata, but the public server query explicitly removes it. SRC-1: `sdk/go/client.go`, `sdk/go/store_sqlite.go`, `schema/knowledge_unit.json`, `server/backend/src/cq_server/services/reviews.py`, `server/backend/src/cq_server/api/routes/knowledge.py`; [RT-CLM-approved-query](runtime.md#rt-clm-approved-query).

> // defaultEvidenceConfirmations is the starting confirmation count for a new unit.
> defaultEvidenceConfirmations = 1
> --- `sdk/go/client.go`

> @router.get("", response_model_exclude={"data": {"__all__": {"created_by"}}})
> --- `server/backend/src/cq_server/api/routes/knowledge.py`

#### MEM-OBJ-flags
Label: Knowledge unit flags

Source-native identity: KnowledgeUnit.flags, a retained array of reason/timestamp with optional detail/duplicate_of. Reason and duplicate target are symbolic; optional explanatory detail is natural-language material. Both are serialized in unit data, but have different consumer behavior: ranking uses the changed confidence, not the detail's argument. Flags are distinct from the feedback invocation [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback); no supplied object denotes them.

Go local feedback records reason, time, explanation and duplicate link. Python apply_flag supports duplicate_of, but its client and remote service call only reason. Server FlagRequest has only reason. Consequently the complete Go flag payload does not survive remote admission; a duplicate reason reaches Python Flag construction without the required reference and fails model validation before update. Stale/incorrect flags can persist and influence later scores. No underlying failed-task trace or caller identity is required per flag in these paths. Local Go query serializes the stored unit without removing flag detail, challenging the schema's blanket display claim. SRC-1: `sdk/go/scoring.go`, `sdk/go/store_sqlite.go`, `sdk/python/src/cq/scoring.py`, `sdk/python/src/cq/models.py`, `server/backend/src/cq_server/models/knowledge.py`, `server/backend/src/cq_server/api/routes/knowledge.py`.

> out.Flags = append(slices.Clone(ku.Flags), Flag{
> Reason: reason,
> Timestamp: &now,
> Detail: cfg.detail,
> DuplicateOf: cfg.duplicateOf,
> })
> --- `sdk/go/scoring.go`

> return await knowledge.flag(unit_id, request.reason)
> --- `server/backend/src/cq_server/api/routes/knowledge.py`

> if self.reason is FlagReason.DUPLICATE and not self.duplicate_of:
> raise ValueError("duplicate_of is required when reason is 'duplicate'")
> --- `sdk/python/src/cq/models.py`

The schema declares a different intended display contract:

> "description": "Optional explanation when flagging. Server-side only; never returned to querying agents."
> --- `schema/knowledge_unit.json`

That declaration does not enforce stripping in the local store or query delivery path.

#### MEM-OBJ-extensions
Label: Knowledge unit extensions

Source-native identity: KnowledgeUnit.extensions. Namespaced keys are symbolic; values are arbitrary retained JSON with opaque application meaning. Storage follows the unit's JSON body. These values cannot be classified uniformly as prose, rules or numerical representations without a concrete payload/consumer. No supplied object counterpart exists; this is optional material carried through [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal), not executable capability loading.

Go proposal can admit extensions after key validation and forward them remotely; Python Client.propose exposes no extensions argument and its remote body omits them even when draining a store-inserted unit. The server can accept them and the unit model reloads them. Ordinary query may deliver their JSON, but no semantic interpretation by an application-specific consumer is established. The schema tells consumers to ignore unknown keys. Initial authorship is caller-dependent; no required rationale, canonical meaning or verification evidence accompanies a value. SRC-1: `schema/knowledge_unit.json`, `sdk/go/client.go`, `sdk/go/remote.go`, `sdk/python/src/cq/client.py`, `server/backend/src/cq_server/services/knowledge.py`.

> if len(ku.Extensions) > 0 {
> body["extensions"] = ku.Extensions
> }
> --- `sdk/go/remote.go`

#### MEM-OBJ-knowledge-vectors
Label: Knowledge unit vectors

Source-native identity: knowledge_units_vec.embedding linked by unit ID. Dense numerical representations have distributed-parametric form; substrate is float32 SQLite blobs. They are distinct from [RT-CMP-token-embedding](runtime.md#rt-cmp-token-embedding), the opaque provider that produces them, and from the natural-language source lesson. No supplied vector object counterpart exists.

Lineage: insert/update concatenates summary, detail and action, calls the provider and serializes the returned embedding. Query derives a transient search embedding from domain words. Initial pre-existing vectors, provider version compatibility and regeneration after provider changes are uninspected. The vectors affect code's distance selection, not the host as readable reasons. The consumer receives the associated unit JSON, not a prose decoding of numerical state. Approval filters selection but does not establish vector quality. Feedback can regenerate the vector despite unchanged insight text, because repository update follows the same semantic update path. SRC-1: `server/backend/src/cq_server/semsearch/queries.py`, `server/backend/src/cq_server/semsearch/__init__.py`, `server/backend/src/cq_server/repositories/knowledge.py`.

> embedding = await _get_embeddings([text])
> serialized = _serialize_embedding(embedding)
> clauses = [*(base_clauses or []), *build_insert_vec_clauses(unit, serialized)]
> await db.run_sync(db.run_clauses_sync, clauses)
> --- `server/backend/src/cq_server/semsearch/queries.py`

The inspected implementation passes base and vector clauses together; the repository's prose description of a separate transaction must not replace this call structure.

#### MEM-OBJ-node-info
Label: Discovery NodeInfo cache

Source-native identity: NodeInfo cached by node address. Symbolic endpoint/version metadata lives in resolver memory and optional SHA-256-address-keyed JSON files. It is not advice, a query-result cache or a raw task trace. Distinct from all supplied objects; the closest route is knowledge query, whose remote transport consumes this metadata: [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query).

Lineage: successful node discovery or documented 404 defaults; initialization of any pre-existing cache file is not authenticated by this source inspection. A later resolver reads the file, checks age and validates shape/compatibility; an HTTP client uses api_base_url to construct the operation destination. This is transport authority, not host model instruction authority. Go and Python disk entries expire by mtime; successful in-process entries persist for resolver lifetime without a TTL check on the memo hit. SRC-1: `sdk/go/discovery/cache.go`, `sdk/go/discovery/discovery.go`, `sdk/go/remote.go`, `sdk/python/src/cq/discovery/_cache.py`, `sdk/python/src/cq/discovery/_resolver.py`.

> if info, ok := r.memCache[addr]; ok {
> r.mu.Unlock()
> return info, nil
> }
> --- `sdk/go/discovery/discovery.go`

### Routes

#### MEM-RTE-store-replacement
Label: Local store replacement

Owner/endpoints: caller holding a Store → Update/Delete → local store and indexes → later Query/Unit. This is an exposed storage capability, not an established deployed caller editing advice. It differs from [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback), which actually invokes Update for evidence changes. SRC-1: `sdk/go/store.go`, `sdk/go/store_sqlite.go`.

- Immediate return: storage success/error; Update replaces JSON and refreshes domains/FTS in a transaction; Delete removes the unit and search entries.
- Later read-back: capability only — Query/Unit can reload replacement data, but an unspecified direct editing caller is not a wired behavioral consumer route; feedback's wired read-back is annotated separately.
- Delegated visibility: local store readers under process/database access; no automatic remote forwarding is established by these methods.
- Selection predicate: caller provides unit ID and replacement object or deletion ID; nonempty normalized domains required for replacement, absent ID errors.
- Invalidation or expiry: Delete removes local content; Update replaces current data without retaining a revision history in this path.
- Activation or effect: wired physical replacement/index maintenance; advisory use of rewritten content remains uninspected.
- Evidence limits: direct API capability, not evidence of an agent content-edit workflow; custom-store behavior and exercised caller identity uninspected.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission: generic caller chooses content and can abandon it; human per-content control is unresolved. Store code checks domains/existence, not the content's truth or user approval. Trigger/mode: explicit API operation, not automatic trace mining. Answer oracle: inapplicable — no expected task outcome checked. Recovery: SQLite transaction rollback on failed replacement; caller must retain old content for a later restoration. The storage API supplies no epistemic writing guidance. What persists is the replacement unit, not its edit justification.

> // Update replaces an existing knowledge unit.
> --- `sdk/go/store_sqlite.go`

#### MEM-RTE-discovery-resolution
Label: Discovery resolution read-back

Owner/endpoints: Go/Python remote operation → resolver → memory/disk cache or discovery probe → NodeInfo → HTTP destination construction. This route supplies transport metadata, not the knowledge-query selection already declared by [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query). SRC-1: `sdk/go/discovery/discovery.go`, `sdk/go/discovery/cache.go`, `sdk/go/remote.go`, `sdk/python/src/cq/discovery/_resolver.py`.

- Immediate return: cached or newly resolved NodeInfo, or discovery error.
- Later read-back: successful resolution is memoized; optional disk JSON reaches a subsequent resolver/process invocation.
- Delegated visibility: endpoint metadata goes to the remote client, not directly to the foreground model; on a miss the configured node receives a discovery request.
- Selection predicate: normalized user-supplied node address; memo first, fresh valid disk entry next, network probe last; no ranking or model token budget.
- Invalidation or expiry: disk mtime TTL and invalid-record removal; successful memory entries last for resolver lifetime, while unsuccessful probes are not memoized.
- Activation or effect: wired endpoint reuse and URL construction; actual remote calls and deployed destination correctness uninspected.
- Evidence limits: cached shape/version validity does not independently verify endpoint trust; complete probe validation/security and cache concurrency outcomes uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission is software decoding/validation or predefined fallback, not human review of each NodeInfo. The configured address is caller-supplied, not proof of a human content decision. Trigger/mode: first remote operation or cache miss; proposed change is cached endpoint metadata. Probe failures reject persistence; cache write failure is nonfatal and leaves the in-process result usable. Recovery is re-probing after a miss/new resolver; no deployed rollback trace supplied. Answer oracle: inapplicable — protocol version/shape checks are not knowledge correctness outcomes. Guidance is the compiled discovery contract; its result, not its reasoning, persists.

> return url.JoinPath(info.APIBaseURL, path)
> --- `sdk/go/remote.go`

#### MEM-RTE-maintenance-migration
Label: Operator maintenance migration

Owner/endpoints: operator chooses database migration → shipped shell script → SQLite knowledge data/indexes or renamed snapshot → subsequent store/server readers. Distinct from [RT-RTE-host-installation](runtime.md#rt-rte-host-installation), which writes host instructions, and from [RT-RTE-local-drain](runtime.md#rt-rte-local-drain), which submits new remote units. SRC-1: `server/scripts/migrate-v1.sh`, `server/scripts/migrate-team-db.sh`.

- Immediate return: migration diagnostics or error; v1 normalizes enums, domains and dashed row IDs, synchronizes JSON ID and conditionally rebuilds FTS; rename driver creates cq.db from team.db.
- Later read-back: changed database is available to subsequent store/server reload; actual operator migration and later application use remain unobserved.
- Delegated visibility: database/filesystem consumers, not automatic upload of session history or direct model delivery.
- Selection predicate: operator-selected path and SQL legacy-value predicates; optional FTS table presence determines rebuild.
- Invalidation or expiry: v1 replaces selected legacy encodings; rename leaves original database and backup, and skips an existing destination.
- Activation or effect: wired maintenance source, not an exercised migration or learning mechanism.
- Evidence limits: no migration run; v1 FTS rebuild follows the main transaction; complete reference/vector consistency and live-writer safety uninspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Admission: operator starts the script, code decides each transformed field; not human approval of every lesson or model-authored revision. Proposed change is format/compatibility, not experiential advice. Checks can abort; scripts create backup material, but successful restore and transactional rollback across the FTS rebuild are not established. Mode is bounded maintenance. Answer oracle: inapplicable — legacy-format counts and database checks do not evaluate lesson truth. Guidance is shipped SQL/script policy; normalized unit data and rebuilt search state persist.

> -- Sync the ID inside JSON data with the row ID.
> UPDATE knowledge_units
> SET data = json_set(data, '$.id', id)
> WHERE json_extract(data, '$.id') != id;
> --- `server/scripts/migrate-v1.sh`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal)

Write agency: host or direct caller authors [MEM-OBJ-insight](#mem-obj-insight). The shipped reflection procedure requests generalization, deduplication, safety checking and user edit/approval, but software proposal validates fields rather than that reasoning. Interactive human editing is an afforded content control; headless and direct API paths prevent treating it as universal enforced admission. The unit retains reasons only insofar as the author puts them in detail. The VIBE√ provenance labels belong to the requested session presentation, not a required unit field. SRC-1: `sdk/go/prompts/reflect.md`, `schema/knowledge_unit.json`; [RT-CLM-proposal-approval](runtime.md#rt-clm-proposal-approval).

Remote creation is PRIVATE with authenticated created_by and newly generated ID/default evidence; local creation timestamps reflect admission time, not authenticated event timing. Subsequent queries can consume local content immediately or remote content after approval. No required task trace, cited reference or independently verified result accompanies admission. SRC-1: `sdk/go/client.go`, `sdk/python/src/cq/models.py`, `server/backend/src/cq_server/services/knowledge.py`.

#### On [RT-RTE-local-drain](runtime.md#rt-rte-local-drain)

Retained-input transformation: Go sends domains, insight, context, created_by and optional extensions; it omits unit ID, evidence, flags and superseded_by. Python sends domains, insight, context and created_by, omitting extensions too. Server overrides created_by and creates new default evidence. Hence confidence and flag history do not survive as history of the successor; local failure evidence can be discarded when the local copy is deleted. Source-native lesson text survives, not a complete checkpoint or identity-preserving replica. SRC-1: `sdk/go/remote.go`, `sdk/python/src/cq/client.py`, `server/backend/src/cq_server/services/knowledge.py`.

Success-to-pending transfer changes later availability: local deletion precedes any remote review approval. Startup scheduling and failure limitations remain as supplied; no additional human content-admission step is wired by transfer. The successor's new identity prevents assuming local feedback will refer to it. Malformed successful responses are especially weak identity evidence: both clients return promoted copies with server fields cleared. No deployment trace establishes continuity or loss rates.

#### On [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback)

Automatic transformation takes a caller's claimed success/problem and updates numerical evidence/flags. This is not automatic extraction of a lesson from raw task traces: underlying experience is opaque, and code does not inspect it. Later query ranking reads confidence; the host can see retained flags in delivered units. Go local detail may preserve criticism as prose, but score adjustment is independent of what that prose says. The remote and Python-client paths lack that content-level rationale. SRC-1: `sdk/go/scoring.go`, `sdk/python/src/cq/scoring.py`, `server/backend/src/cq_server/services/knowledge.py`.

The source-supported exception is duplicate handling in [MEM-OBJ-flags](#mem-obj-flags): remote/Python Client flag cannot supply duplicate_of to the scoring constructor. Do not infer successful duplicate-flag storage from the enum or handler's name. Optional semantic repository update also regenerates vectors on confirmation/flag; provider failure can block the feedback write even though insight text is unchanged. SRC-1: `server/backend/src/cq_server/repositories/knowledge.py`, `server/backend/src/cq_server/semsearch/queries.py`.

#### On [RT-RTE-remote-review](runtime.md#rt-rte-remote-review)

Curation is visibility admission, not content rewriting. The browser requests 20 pending units, skips seen IDs in session state and lets a human choose approve/reject/skip. Status/reviewer/time persists in SQL columns; a required textual reason does not. Reject excludes the unit from ordinary remote query while retaining its payload for authenticated review get/list. Skip is local UI state rather than a durable rejection. SRC-1: `server/frontend/src/pages/ReviewPage.tsx`, `server/backend/src/cq_server/services/reviews.py`, `server/backend/src/cq_server/repositories/reviews.py`.

Read-back therefore has two consumers with different authority: server query selector obeys review status mechanically; review reader can interpret the content regardless of approval. API caller identity does not establish a human decision. The shipped seed driver performs approve and score adjustment programmatically. These are implementation paths, not evidence that any advice was evaluated correctly.

> # Adjust confidence via confirmations/flags (only works on approved units).
> if target > 0.5:
> for _ in range(_confirms_needed(target)):
> --- `server/scripts/seed-kus.py`

#### On [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query)

Requested external-memory read-back: foreground caller chooses domains/context/limit; SQLite selects domain OR FTS candidates and ranks relevance × confidence. Direct inspected SDK PostgreSQL and Python in-memory query paths use domain candidates without that FTS alternative. Go defaults to five results and clamps client requests to 50; this is an item-count budget, not a token budget. Local-first merge has no common rerank and can suppress remote advice. Remote query strips created_by before SDK/MCP delivery. MCP also omits warning/source metadata as supplied in runtime, so the host sees less provenance/retrieval-failure information than a direct SDK caller. SRC-1: `sdk/go/client.go`, `sdk/go/store_sqlite.go`, `sdk/go/stores/postgres/postgres.go`, `sdk/python/src/cq/stores/postgres.py`, `sdk/python/src/cq/stores/memory.py`, `server/backend/src/cq_server/api/routes/knowledge.py`.

Optional semantic selection first limits approved domain matches by distance. Its final ranking combines relevance and inverse normalized distance, then confidence, rather than simply relevance × confidence. Stored vectors are not delivered as readable evidence. The provider-derived representation changes selection, not the advice's truth or authority. Wrapped errors can bypass intended SQL fallback as supplied in runtime. SRC-1: `server/backend/src/cq_server/semsearch/queries.py`, `server/backend/src/cq_server/semsearch/__init__.py`.

> relevance_weight = 0.8
> distance_weight = 0.2
> normalized_distance = distance / total_distance if total_distance > 0 else 0
> result = relevance * relevance_weight + (1 - normalized_distance) * distance_weight
> return result
> --- `server/backend/src/cq_server/semsearch/queries.py`

No inspected query path trims the host's existing turns. Selected full unit payloads accumulate through ordinary delivery; memory retrieval does not establish eviction, isolated task frames or a host context reload facility.

#### On [RT-OBJ-failure-record](runtime.md#rt-obj-failure-record)

Raw-to-derived lineage: a host tool-failure event becomes one mechanically formatted and clipped JSON record, replacing the previous conversation record. Tool-specific formatting can keep a command, path or bounded content; it is not a complete original payload or a readable summary of an opaque checkpoint. Error/input are bounded to 200 runes plus ellipsis. The host trace's deeper origin, authenticity and interpretation remain outside CQ. SRC-1: `cli/internal/hook/cursor.go`.

#### On [RT-RTE-failure-reminder](runtime.md#rt-rte-failure-reminder)

Automatic external-state supply is triggered by stop, with conversation key selecting the latest failure record. Delivery is hook stdout, not a knowledge proposal. The text can influence the host but diagnoses no cause and produces no persistent lesson. Successful tool events do not clear the previous failure: ModePostToolUse returns immediately. Stop clears after output; malformed stored JSON is removed; session-start sweeps files older than 24 hours. These cleanup rules affect the auxiliary record, not knowledge TTL. SRC-1: `cli/internal/hook/cursor.go`.

> _, _ = fmt.Fprintf(out, "cq: previous tool %s failed: %s\n  input: %s\n",
> record.ToolName, record.Error, record.Input)
> return clearState(path)
> --- `cli/internal/hook/cursor.go`

#### On [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection)

Trace origin is the host's current session: APIs, fixes, workarounds, failed attempts and dead ends. Requested derivation is compact summary → candidate summary/detail/action → user-approved proposal. The command excludes routine/documented events and already proposed/confirmed insights, requests sanitization, and allows user editing. It does not durably retain the intermediate summary or full raw trace, and provides no host compaction checkpoint alternatives. Only proposed candidate fields reach later queries through the separate proposal route. SRC-1: `sdk/go/prompts/reflect.md`; dedicated command/stub evidence in runtime bounds server-extraction claims.

> If the user requests an edit, show the current field values and ask which field to change. Apply the changes and confirm the updated candidate before proposing.
> --- `sdk/go/prompts/reflect.md`

The summary request is a working-context selection affordance performed by the foreground agent, not code-owned eviction or isolation. No removed turns, verbatim tail, pointer checkpoint or reload of omitted session material is established. A stack-frame analogy does not describe a shipped CQ worker context: no separate frame is created here. The external store is reachable through explicit retrieval by value, not a reference held in the model window.

#### On [RT-RTE-host-installation](runtime.md#rt-rte-host-installation)

Static Markdown instructions and installation manifests persist for future host loads. Packaged text/ownership hashes supply lineage and replacement control; user-modified files can veto overwrite. This is operator configuration, not experience-derived read-back. Prompt distribution can shape candidate admission and reliance when the host follows it, but actual loading, priority and host compliance are unobserved. The supplied Pi installation findings do not establish other adapters' identical behavior. SRC-1: `cli/internal/install/pi.go`, `cli/internal/install/files.go`; passages retained in runtime.

## Write side

Acquisition has three independently controlled paths. Ordinary proposal admits caller text after validation; interactive prompts request approval/editing while headless/direct calls do not enforce it. Reflection affords host extraction from session traces but retains only fields later proposed. Direct store replacement permits caller-chosen mutation without proving a deployed content editor. [RT-RTE-knowledge-proposal](runtime.md#rt-rte-knowledge-proposal), [RT-RTE-session-reflection](runtime.md#rt-rte-session-reflection), [MEM-RTE-store-replacement](#mem-rte-store-replacement).

Maintenance transformations are separate from semantic authorship: normalization and index updates, numerical confirmation/flagging, optional embedding production, transfer with reinitialization, review status updates and operator migration. Each has a known software admission point even when original content authorship or initialization is unknown. None proves improved future capacity. Score evidence and vector derivation are behavior-shaping selection inputs, not automatic acquisition of verified explanatory knowledge. [MEM-OBJ-selection-metadata](#mem-obj-selection-metadata), [MEM-OBJ-flags](#mem-obj-flags), [MEM-OBJ-knowledge-vectors](#mem-obj-knowledge-vectors), [MEM-RTE-maintenance-migration](#mem-rte-maintenance-migration).

Withdrawal differs by substrate. Store deletion removes local content; drain removes it after posting a newly identified remote proposal; review rejection keeps content but withholds ordinary query visibility; stale/incorrect flags lower score without status revocation. No exposed correction/reversal of an already completed review is established by the supplied review handlers. A superseded_by field alone is not a wired supersession workflow or removal rule. These are scoped findings, not a global absence claim. SRC-1: `sdk/go/store.go`, `sdk/go/client.go`, `schema/knowledge_unit.json`, `server/backend/src/cq_server/services/reviews.py`; supplied review/query records.

For trace-fed retention, the automatic Cursor chain is raw failure event → clipped record → later stop reminder → deletion. Reflection's richer session-to-lesson chain is requested model reasoning followed by explicit proposal, not a CQ-owned automatic transformer. Neither keeps a durable full session. Reasons may remain in insight.detail and Go local flag.detail; remote review retains decision metadata without required justification. Query can deliver insight.detail, but no later consumer is shown reconstructing the safety check or full failed-attempt history. The initial provenance of injected stores, opaque extensions and provider representations remains unresolved locally rather than being hidden by known later transformations.

## Read-back

The principal direction is pull: an agent or direct caller requests advice, code selects stored content, transport returns unit data, and the host decides reliance. A persistence method alone does not establish that last decision. Actual selection/interpretation authority is split between metadata/index consumers and the host's prose interpretation. [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query), [RT-BAP-knowledge-guidance](runtime.md#rt-bap-knowledge-guidance).

Alternative reads matter: review queue/get/list can see non-approved content; local Store.Unit reads a named unit for feedback without proving targeted knowledge selection for a task; status reads recent units and aggregate evidence for a caller rather than automatically pushing lessons. Status source behavior is supplied by runtime and directly inspected in Go Client.Status: remote aggregates are merged into local statistics, with no newly retained query artifact established. SRC-1: `sdk/go/client.go`, `server/backend/src/cq_server/services/reviews.py`.

Cursor is the automatic push case: stop selects one conversation failure, prints bounded text and clears it. Discovery is automatic reuse within an explicitly requested remote operation: endpoint metadata chooses transport destination but is not unsolicited knowledge injection. Static installation supports later loading, not experience-derived read-back. Host token-budget enforcement, frame isolation, old-turn eviction and host checkpoint reload are not inspectable in CQ's source boundary. No activation or benefit is claimed for any delivered advice.

## Integration issues

- **Feedback exception:** [RT-RTE-knowledge-feedback](runtime.md#rt-rte-knowledge-feedback) needs qualification for duplicate flags. [MEM-OBJ-flags](#mem-obj-flags) traces server/Python-client reason-only calls to a constructor requiring duplicate_of. Enum availability does not establish a successful update. Consequence: generic flag wiring must not imply all three reasons work on every client/server path.
- **Semantic ranking refinement:** [RT-RTE-knowledge-query](runtime.md#rt-rte-knowledge-query) describes nearest-vector preselection and reranking; [MEM-OBJ-knowledge-vectors](#mem-obj-knowledge-vectors) and its query annotation establish the 0.8 relevance/0.2 inverse-distance combination before confidence. This qualifies the runtime account's compressed description of relevance/confidence reranking; ordinary SQL still uses relevance × confidence.
- **Partial transfer:** [RT-RTE-local-drain](runtime.md#rt-rte-local-drain) is not a replica route. Its annotation establishes lost feedback/provenance and Python extension omission, concerning [MEM-OBJ-selection-metadata](#mem-obj-selection-metadata), [MEM-OBJ-flags](#mem-obj-flags), [MEM-OBJ-extensions](#mem-obj-extensions). Consequence: lineage/horizon cannot be inferred from text continuity alone.
- **Misleading display doctrine:** schema flag.detail says never returned to querying agents, while the Go local stored-unit query has no stripping step. [MEM-OBJ-flags](#mem-obj-flags). Consequence: requested server-only rationale storage is not a universal confidentiality guarantee. Remote service does not admit that detail in the first place.
- **Transaction description:** the repository insertion docstring says semantic storage uses a separate transaction; direct semantic implementation combines base/vector clauses in one call. [MEM-OBJ-knowledge-vectors](#mem-obj-knowledge-vectors). Consequence: use executable call structure rather than the docstring for the write account; this is not an observed atomicity experiment.
- **Unresolved initialized state and host processing:** pre-existing stores/caches/vectors, actual extension meaning, full alternative-store mutation parity, host context operations, provider compatibility after model changes, maintenance reference/vector consistency and live deployment behavior remain uninspected. The coverage table names the parts and prevented conclusions. These limits do not defeat known subsequent transformations.

Possible duplicate records: none identified after comparison with supplied declarations. New objects denote retained operative parts not declared as runtime objects; new routes denote local replacement capability, transport-cache resolution and operator database maintenance. Existing query/proposal/feedback/review/drain/reflection/reminder/installation referents receive annotations rather than new declarations.

## Limitations and checks

All executable findings are implementation evidence under SRC-1; prompt/schema guidance is doctrine/design. No observed run or causal experiment establishes exercised mining, human review, host adherence, correctness, benefit or self-improvement. Source identity, immutable commit and clean checkout were rechecked; added reads remain within registered SRC-1. The supplied report/type/record contracts were read completely, including bounded continuations. No prior characterization or other worker output was used.

Deterministic validation: the prescribed validate-output check passed with “Member content check passes; invocation residue not checked.” This establishes the checked member form and quotation occurrence, not job acceptance or claim support.
