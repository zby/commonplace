---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Pond memory comparison: canonical session traces, derived retrieval state, checkpoint carriers and later recall/restoration consumers."
run-id: AAS-2026-10-14-pond-7a589a889ca1-01
source-identity: "https://github.com/tenequm/pond"
reviewed-boundary: "0c440e130faf44052d0d896a585e572090079f1f"
memory-comparison:
  version: 2
  scope: >-
    Included are accumulated canonical sessions/messages/parts and raw provider rows,
    upstream summary/checkpoint carriers, durable search text and message vectors,
    row-meta caches and sync progress, changed capture configuration, their admission,
    maintenance, transfer, recall and restored-session routes. Other codecs' opaque
    payload/checkpoint alternatives, unspecified library admissions, export consumers
    and untraced interactive delivery remain included uncertainties. Excluded are
    fixed embedding weights, static shipped skills/tool guidelines, transient check
    results and benchmark outputs without an established later behavioral consumer,
    and external hosts' internal context management. Canonical storage is not assumed
    to resolve the meaning or generation of its opaque contents.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Local canonical Lance datasets, full parts/raw rows/carriers, and archive/restored files"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-part, memory.md#mem-obj-raw-record, memory.md#mem-rte-archive-transfer, runtime.md#rt-rte-session-restore]
              note: "Canonical retained data/index files, clean archive datasets and serialized restore destinations are file-backed; JSON encoding is not another substrate."
          records: [memory.md#mem-obj-session, memory.md#mem-obj-message, memory.md#mem-obj-part, memory.md#mem-obj-checkpoint-carriers, memory.md#mem-rte-archive-transfer, runtime.md#rt-rte-session-restore]
          note: "Covers the local canonical/file branch, including opaque bytes as stored objects, without claiming codec completeness or host loading."
        - scope: "Advertised remote canonical storage in an operator-owned S3 bucket"
          assessment: partial
          findings:
            - value: service-object
              basis: claimed
              records: [epistemic.md#epi-clm-archive-recall]
              note: "The public claim names S3 storage; this is not upgraded to verified remote wiring or operation by the local file branch."
          records: [epistemic.md#epi-clm-archive-recall, memory.md#mem-rte-archive-transfer]
          note: "Remote object-store implementation internals and deployed storage are not inspected; exact backing behavior remains unresolved."
        - scope: "Version-keyed row-meta cache, resident snapshots, sync cursor/status and changed adapter configuration"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-row-meta, memory.md#mem-obj-sync-cursor, runtime.md#rt-obj-adapter-config]
              note: "Mmap cache files, local JSON progress and persisted configuration retain access/capture state across invocations."
            - value: in-memory
              basis: wired
              records: [memory.md#mem-obj-row-meta]
              note: "Resident read-only row-meta snapshots and delta chains are operative cache parts, not merely transient query results."
          records: [memory.md#mem-obj-row-meta, memory.md#mem-obj-sync-cursor, runtime.md#rt-obj-adapter-config]
          note: "Both persistent files and operative resident cache parts are classified; ordinary current-batch buffers are excluded."
        - scope: "Additional codec-specific retained state and standalone export alternatives"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-session-capture, runtime.md#rt-rte-corpus-sql, memory.md#mem-obj-raw-record]
          note: "Shared canonical storage is known, but uninspected codecs and subsequent export consumers cannot establish an exhaustive substrate inventory for their operative alternatives."
      records: [memory.md#mem-obj-part, memory.md#mem-obj-row-meta, memory.md#mem-obj-sync-cursor, runtime.md#rt-rte-session-capture, runtime.md#rt-rte-corpus-sql, epistemic.md#epi-clm-archive-recall]
      note: "Positive local and advertised remote branches remain distinct; included codec/export alternatives prevent complete inventory coverage."
    representational_form:
      assessment: partial
      units:
        - scope: "Readable historical bodies, reasoning, search-text projections and checkpoint summary text"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-message, memory.md#mem-obj-part, memory.md#mem-obj-search-text, memory.md#mem-obj-checkpoint-carriers]
              note: "These parts supply text interpreted by humans/models; summary text is separate from opaque carrier state."
          records: [memory.md#mem-obj-message, memory.md#mem-obj-part, memory.md#mem-obj-search-text, memory.md#mem-obj-checkpoint-carriers]
          note: "Classifies the inspected readable parts, not every byte delivered by full-part or native replay readers."
        - scope: "Canonical role/identity/lineage, tool fields, raw JSON structure, row-meta, cursor and capture configuration"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-session, memory.md#mem-obj-part, memory.md#mem-obj-raw-record, memory.md#mem-obj-row-meta, memory.md#mem-obj-sync-cursor, runtime.md#rt-obj-adapter-config]
              note: "Localized fields have fixed consumer rules for lookup, capture, replay and reconstruction; opaque JSON values are not classified by their wrapper."
          records: [memory.md#mem-obj-session, memory.md#mem-obj-part, memory.md#mem-obj-raw-record, memory.md#mem-obj-row-meta, memory.md#mem-obj-sync-cursor, runtime.md#rt-obj-adapter-config]
          note: "Known structure and deterministic consumers do not resolve mixed payload semantics."
        - scope: "Durable dense message vectors at semantic-search consumption"
          assessment: known
          findings:
            - value: parametric
              basis: wired
              records: [memory.md#mem-obj-message-vector, memory.md#mem-rte-message-embedding]
              note: "Distributed numerical representations influence similarity selection; these are outputs, not trained replacement weights."
          records: [memory.md#mem-obj-message-vector, memory.md#mem-rte-message-embedding]
          note: "The numerical part is distinct from its symbolic model-ID label and readable source text."
        - scope: "Full file payloads, opaque harness values and other codecs' checkpoint alternatives"
          assessment: partial
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-checkpoint-carriers]
              note: "Inspected checkpoint/lineage fields support fixed cut-point lookup, separate from summary interpretation."
          records: [memory.md#mem-obj-part, memory.md#mem-obj-raw-record, memory.md#mem-obj-checkpoint-carriers]
          note: "Readable names/MIME summaries cannot classify consumed blobs or opaque replay state; upstream semantics and remaining codecs are unresolved."
      records: [memory.md#mem-obj-part, memory.md#mem-obj-search-text, memory.md#mem-obj-message-vector, memory.md#mem-obj-checkpoint-carriers, memory.md#mem-obj-row-meta]
      note: "Text, fixed fields and numerical representations are positive witnesses; opaque consumed payloads prevent an exhaustive form union."
    lineage:
      assessment: partial
      units:
        - scope: "Canonical session/message/part and inspected Pi raw rows acquired from source logs or canonical callers"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-part, memory.md#mem-obj-raw-record]
              note: "Pond imports source-fed history rather than authoring a factual digest; upstream mixed authorship is not attributed to Pond."
          records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-part, memory.md#mem-obj-raw-record, epistemic.md#epi-rte-field-extraction]
          note: "This is the known Pond acquisition path; capped raw leaves qualify fidelity, not the acquisition classification."
        - scope: "Checkpoint summary carriers: Pond acquisition and original upstream derivation"
          assessment: partial
          findings:
            - value: imported
              basis: wired
              records: [memory.md#mem-obj-checkpoint-carriers]
              note: "Already-derived upstream compaction/branch summaries are captured as System carriers."
          records: [memory.md#mem-obj-checkpoint-carriers, memory.md#mem-obj-raw-record]
          note: "Original generation, authorship and reasons are uninspected; the imported edge does not resolve whether upstream derivation was automatic trace extraction."
        - scope: "Search-text and vector derivation from recorded sessions"
          assessment: known
          findings:
            - value: trace-extracted
              basis: wired
              records: [memory.md#mem-obj-search-text, epistemic.md#epi-rte-search-projection, memory.md#mem-rte-message-embedding]
              note: "Filtered conversational traces produce durable text projections and passage embeddings consumed by later retrieval."
          records: [memory.md#mem-obj-search-text, memory.md#mem-rte-message-embedding]
          note: "Derivation is known even though the exact upstream embedding artifact is not pinned."
        - scope: "Embedding provenance beyond the recorded text-to-vector edge"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-message-vector, runtime.md#rt-cmp-candle-embedder]
          note: "Mutable model IDs do not establish the exact fetched weights or their original provenance; no extra lineage value follows."
        - scope: "Row-meta cache and store-validated sync cursor derivation"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-row-meta, memory.md#mem-obj-sync-cursor, memory.md#mem-rte-sync-watermarks]
              note: "Fixed code compiles access/progress metadata from canonical rows and validated storage snapshots."
          records: [memory.md#mem-obj-row-meta, memory.md#mem-obj-sync-cursor, memory.md#mem-rte-sync-watermarks]
          note: "These are deterministic access structures, not independently authored session claims."
        - scope: "Capture configuration changes through explicit editing/commands and first-run discovery"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [runtime.md#rt-rte-adapter-config]
              note: "Explicit operator commands/manual configuration supply capture choices."
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-rte-adapter-config]
              note: "Software bootstrap derives persisted source configuration from discovery under its preconditions."
          records: [runtime.md#rt-rte-adapter-config]
          note: "Manual and bootstrap paths coexist and are not inferred from physical Rust writes."
        - scope: "Other codec payload/summary derivations and unspecified library content origins"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-session-capture, memory.md#mem-rte-archive-transfer, memory.md#mem-obj-raw-record]
          note: "Shared import/transfer seams do not enumerate original derivation paths of uninspected contents."
      records: [runtime.md#rt-rte-session-capture, runtime.md#rt-rte-adapter-config, memory.md#mem-obj-checkpoint-carriers, memory.md#mem-rte-message-embedding, memory.md#mem-rte-sync-watermarks]
      note: "Known acquisition and compilation paths do not resolve checkpoint origins, embedding provenance or other codec alternatives."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Historical readable material delivered as requested search/get/SQL results to a host model or human"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [memory.md#mem-bap-recalled-history, runtime.md#rt-rte-archive-recall, runtime.md#rt-rte-corpus-sql]
              note: "Selected history supplies evidence/context at the actual tool-result consumer, not certified truth or present system instructions."
          records: [memory.md#mem-bap-recalled-history, runtime.md#rt-rte-archive-recall, runtime.md#rt-rte-corpus-sql]
          note: "Known delivery force is advisory historical evidence; interpretation and changed answers remain unobserved."
        - scope: "Search text and message vectors consumed by later lexical/semantic ranking"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-search-text, memory.md#mem-obj-message-vector, runtime.md#rt-rte-archive-recall]
              note: "Retained text and vectors influence relative priority even though selector code/weights are not learned from these sessions."
          records: [memory.md#mem-obj-search-text, memory.md#mem-obj-message-vector, runtime.md#rt-rte-archive-recall]
          note: "Ranking influence does not imply factual endorsement or retrieval benefit."
        - scope: "Retained conversational traces/search text at automatic projection and embedding update consumers"
          assessment: known
          findings:
            - value: learning
              basis: wired
              records: [epistemic.md#epi-rte-search-projection, memory.md#mem-rte-message-embedding]
              note: "Recorded experience feeds automatic durable retrieval-artifact updates; their outputs separately supply ranking or context at downstream consumers."
          records: [epistemic.md#epi-rte-search-projection, memory.md#mem-rte-message-embedding]
          note: "This names the update consumer's force, not improved capacity or training of embedder parameters."
        - scope: "Canonical identity/lineage, row-meta, watermarks and persisted capture configuration at fixed selectors"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-session, memory.md#mem-obj-row-meta, memory.md#mem-rte-sync-watermarks, runtime.md#rt-rte-adapter-config, runtime.md#rt-rte-session-restore]
              note: "Retained fields choose lookup targets, restore lineage, capture sources and freshness windows at their actual software consumers."
          records: [memory.md#mem-obj-session, memory.md#mem-obj-row-meta, memory.md#mem-rte-sync-watermarks, runtime.md#rt-rte-adapter-config]
          note: "Access metadata routes operations rather than supplying model instructions."
        - scope: "Stored canonical keys and labels consumed by additive admission"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [runtime.md#rt-rte-session-capture, epistemic.md#epi-rte-ingest-disposition]
              note: "Existing stored keys/labels determine whether proposed rows or conflicting labels are admissible under fixed storage rules."
            - value: enforcement
              basis: wired
              records: [runtime.md#rt-rte-session-capture, epistemic.md#epi-rte-ingest-disposition]
              note: "The writer filters existing keys and preserves stored immutable labels, enforcing the retained criteria."
          records: [runtime.md#rt-rte-session-capture, epistemic.md#epi-rte-ingest-disposition]
          note: "These are retained-state effects, distinct from static schema checks, HTTP gates or a nonexistent purge denylist."
        - scope: "Native checkpoint/raw payload at restored host loader; foreign reconstruction and other codec alternatives"
          assessment: partial
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-checkpoint-carriers, runtime.md#rt-rte-session-restore]
              note: "Inspected checkpoint/lineage fields select cut points and reconstruction inputs; carrier omission is a separate branch."
          records: [memory.md#mem-obj-raw-record, memory.md#mem-obj-checkpoint-carriers, runtime.md#rt-bap-session-switch]
          note: "File handoff is wired, but opaque payload force at external host interpretation and other codecs remains unresolved; recorded System labels cannot establish instruction authority."
      records: [memory.md#mem-bap-recalled-history, memory.md#mem-obj-search-text, memory.md#mem-obj-message-vector, memory.md#mem-rte-sync-watermarks, runtime.md#rt-rte-session-capture, memory.md#mem-obj-checkpoint-carriers]
      note: "Actual advisory, ranking, update, routing and retained-key veto consumers are classified separately; opaque restoration prevents complete authority coverage."
    write_agency:
      assessment: partial
      units:
        - scope: "Adapter/HTTP canonical admission, searchable projection, vector updates and cursor/cache production"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-session-capture, epistemic.md#epi-rte-search-projection, memory.md#mem-rte-message-embedding, memory.md#mem-rte-sync-watermarks]
              note: "Software validation/selection admits content and derived state without a per-content human approval; workflow initiation and force flags are not such approval."
          records: [runtime.md#rt-rte-session-capture, epistemic.md#epi-rte-search-projection, memory.md#mem-rte-message-embedding, memory.md#mem-rte-sync-watermarks]
          note: "Known subsequent admission is independent of upstream authorship."
        - scope: "Explicit capture configuration and first-run bootstrap admission"
          assessment: known
          findings:
            - value: manual
              basis: wired
              records: [runtime.md#rt-rte-adapter-config]
              note: "Explicit operator enable/disable commands or manual config edits decide the retained capture choice."
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-adapter-config]
              note: "Bootstrap can admit discovered source configuration without interactive approval when its preconditions hold."
          records: [runtime.md#rt-rte-adapter-config]
          note: "The two evidenced admissions are retained independently; a recorded decline can prevent bootstrap."
        - scope: "Operator-selected session/target replacement through CLI/Pi restoration"
          assessment: known
          findings:
            - value: manual
              basis: wired
              records: [runtime.md#rt-rte-session-restore, runtime.md#rt-bap-session-switch]
              note: "An explicit operator decision selects retained content for a restored file and replacement host session; software checks constrain that choice."
          records: [runtime.md#rt-rte-session-restore, runtime.md#rt-bap-session-switch]
          note: "This is content-selected restoration, not the read that chooses a checkpoint and not evidence of automatic summary generation."
        - scope: "Bulk copy/import and generic library write admission"
          assessment: partial
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-rte-archive-transfer]
              note: "Schema/key/plan software checks govern table admission without per-fact human review."
          records: [memory.md#mem-rte-archive-transfer]
          note: "Generic caller identity does not resolve human control over initial supplied/replacement content; wire admission rules do not cover every library write."
        - scope: "Original upstream checkpoint generation and other codecs' admission alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-checkpoint-carriers, memory.md#mem-obj-raw-record, runtime.md#rt-rte-session-capture]
          note: "Original generation/control and uninspected alternatives are unresolved; known Pond capture does not establish upstream approval or automatic generation."
      records: [runtime.md#rt-rte-session-capture, runtime.md#rt-rte-adapter-config, runtime.md#rt-rte-session-restore, memory.md#mem-rte-message-embedding, memory.md#mem-rte-archive-transfer, memory.md#mem-obj-checkpoint-carriers]
      note: "Automatic admissions and explicit manual content/configuration choices coexist with unresolved initial and generic-caller control."
    curation_operations:
      assessment: partial
      units:
        - scope: "Conversational search-text projection from retained session parts"
          assessment: known
          findings:
            - value: consolidate
              basis: wired
              records: [memory.md#mem-obj-search-text, epistemic.md#epi-rte-search-projection]
              note: "Fixed selection and concatenation reduce existing conversational content into a retained searchable representation; excluded full parts remain available."
          records: [memory.md#mem-obj-search-text, epistemic.md#epi-rte-search-projection]
          note: "This is reduced representation of existing content, not a synthesized standing fact or verified new claim."
        - scope: "Replacement of existing stale-model message vectors"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [memory.md#mem-rte-message-embedding, epistemic.md#epi-rte-maintenance-recovery]
              note: "Force/model-swap maintenance revises an existing entry's numerical representation and model label; initial embedding alone is not revision."
          records: [memory.md#mem-rte-message-embedding, epistemic.md#epi-rte-maintenance-recovery]
          note: "Classifies representation replacement, not index rebuilding or trained parameter change; same-ID weight drift is not detected."
        - scope: "Pi native replay versus reconstructed transcript selection"
          assessment: partial
          findings:
            - value: consolidate
              basis: wired
              records: [runtime.md#rt-rte-session-restore, memory.md#mem-obj-checkpoint-carriers]
              note: "The memory annotation on restoration establishes reconstructed v3 files that omit System carriers while retaining selected history, a reduced representation."
          records: [runtime.md#rt-rte-session-restore, memory.md#mem-obj-checkpoint-carriers, memory.md#mem-obj-raw-record]
          note: "Known omission is retained beside native raw replay; semantic fidelity and other codecs' reconstruction transformations remain unresolved."
        - scope: "Original upstream summary production"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-checkpoint-carriers]
          note: "A compaction/branch-summary label does not establish the original transformation's implemented meaning or control."
        - scope: "Canonical key filtering, cache/index/storage maintenance, bulk transfer and deletion reporting"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-session-capture, memory.md#mem-obj-row-meta, memory.md#mem-rte-archive-transfer, memory.md#mem-rte-deletion-detection, epistemic.md#epi-rte-maintenance-recovery]
          note: "Inspected routes establish acquisition, key collision filtering, cache/index rebuilds, physical cleanup or detection-only reports, not another controlled semantic operation. No dedup, decay or invalidate value follows from those names/effects alone."
      records: [memory.md#mem-obj-search-text, memory.md#mem-rte-message-embedding, runtime.md#rt-rte-session-restore, memory.md#mem-obj-checkpoint-carriers, memory.md#mem-rte-deletion-detection]
      note: "Reduced projection and representation revision are positive operations; opaque summary/reconstruction branches and nonsemantic maintenance prevent complete operation coverage."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Requested search/get/SQL, transfer and operator-selected restoration"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-archive-recall, runtime.md#rt-rte-corpus-sql, runtime.md#rt-rte-session-restore, memory.md#mem-rte-archive-transfer]
              note: "A consumer requests retained material by query, ID or source store; automatic result selection/delivery fulfills that request rather than creating another push."
          records: [runtime.md#rt-rte-archive-recall, runtime.md#rt-rte-corpus-sql, runtime.md#rt-rte-session-restore, memory.md#mem-rte-archive-transfer]
          note: "Tool/model answering and restored host continuation are unobserved but the requested delivery paths are wired."
        - scope: "Restarted sync's automatic row-map/cursor fallback into freshness planning"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [memory.md#mem-rte-sync-watermarks, memory.md#mem-obj-row-meta, memory.md#mem-obj-sync-cursor]
              note: "On restarted sync, code supplies available validated retained progress to the capture planner without a request for those retained watermarks."
          records: [memory.md#mem-rte-sync-watermarks, memory.md#mem-obj-row-meta, memory.md#mem-obj-sync-cursor]
          note: "This is a software metadata consumer, not unsolicited host-model context insertion."
        - scope: "Inline/backlog embedding row selection into numerical update"
          assessment: known
          findings:
            - value: push
              basis: wired
              records: [memory.md#mem-rte-message-embedding]
              note: "Configured ingest or maintenance automatically supplies eligible retained search text to the embedder; configuration initiates work rather than requesting particular transcript content."
          records: [memory.md#mem-rte-message-embedding]
          note: "Automatic update-input delivery is separate from the later requested semantic-search return."
        - scope: "Interactive editor-reference insertion, export-file consumers and other codec checkpoint consumption alternatives"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-archive-recall, runtime.md#rt-rte-corpus-sql, memory.md#mem-obj-checkpoint-carriers]
          note: "The supplied requested-tool account is selective; no accepted record traces editor-reference insertion or later export reading, and remaining codec consumers are uninspected. Their directions cannot be inferred from known pull routes."
      records: [runtime.md#rt-rte-archive-recall, runtime.md#rt-rte-corpus-sql, runtime.md#rt-rte-session-restore, memory.md#mem-rte-sync-watermarks, memory.md#mem-rte-message-embedding]
      note: "Requested human/model reads coexist with automatic internal metadata/update supply; untraced alternate consumers prevent a complete direction inventory."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Known requested search/get/SQL/restore/transfer operations"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-archive-recall, runtime.md#rt-rte-corpus-sql, runtime.md#rt-rte-session-restore, memory.md#mem-rte-archive-transfer]
          note: "These are pull operations. Query lexical/embedding scores and requested IDs do not classify a push signal."
        - scope: "Automatic restarted-sync supply of row-map or validated cursor progress"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [memory.md#mem-rte-sync-watermarks]
              note: "Trigger is restarted sync; availability of a validated row map, then fallback cursor, selects the retained progress source supplied to the planner."
            - value: identifier
              basis: wired
              records: [memory.md#mem-rte-sync-watermarks, memory.md#mem-obj-sync-cursor]
              note: "Fallback selection requires stored oldest-message lineage to match the current store probe, alongside version/count bounds, before that cursor's watermarks are supplied."
          records: [memory.md#mem-rte-sync-watermarks, memory.md#mem-obj-sync-cursor]
          note: "Availability and actual lineage identity comparison are distinct selectors; subsequent freshness decisions are effects of the selected progress."
        - scope: "Automatic eligible search-text supply to inline/backlog/force embedding"
          assessment: known
          findings:
            - value: coarse
              basis: wired
              records: [memory.md#mem-rte-message-embedding]
              note: "Trigger is configured embedding work; non-null text plus missing/stale model-label eligibility selects message text for update. Primary keys address writes, not targeted context push."
          records: [memory.md#mem-rte-message-embedding]
          note: "Eligibility filtering is not embedding-inferred selection; embeddings are produced after selection."
        - scope: "Untraced editor insertion, export consumers and opaque checkpoint alternatives"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-archive-recall, runtime.md#rt-rte-corpus-sql, memory.md#mem-obj-checkpoint-carriers]
          note: "Unknown direction/selector facts prevent treating all remaining units as pull-only or assigning a push signal."
      records: [runtime.md#rt-rte-archive-recall, memory.md#mem-rte-sync-watermarks, memory.md#mem-rte-message-embedding, memory.md#mem-obj-checkpoint-carriers]
      note: "Known internal push selectors establish positives; pull-only inapplicability is local and does not erase untraced alternate delivery."
    trace_learning:
      assessment: partial
      units:
        - scope: "Automatic recorded conversational parts to durable search text to later recall/ranking"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [epistemic.md#epi-rte-search-projection, memory.md#mem-obj-search-text, runtime.md#rt-rte-archive-recall]
              note: "Automatic trace-fed reduced text is retained and changes later retrieval/context supply, meeting the artifact-write definition without requiring new facts or measured improvement."
          records: [epistemic.md#epi-rte-search-projection, memory.md#mem-obj-search-text, runtime.md#rt-rte-archive-recall]
          note: "The derived route qualifies; retaining untouched logs alone is not the warrant."
        - scope: "Automatic session projection to retained message vectors to later semantic ranking"
          assessment: known
          findings:
            - value: "yes"
              basis: wired
              records: [memory.md#mem-rte-message-embedding, memory.md#mem-obj-message-vector]
              note: "Trace-derived numerical artifacts are automatically admitted and consumed by later ranking; inference with fixed weights does not exclude this route."
          records: [memory.md#mem-rte-message-embedding, memory.md#mem-obj-message-vector, runtime.md#rt-cmp-candle-embedder]
          note: "Includes initial and maintenance production; no observed benefit, revised method or weight training is asserted."
        - scope: "Original upstream checkpoint/branch-summary generation and other codec trace-fed alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-checkpoint-carriers, memory.md#mem-obj-raw-record, runtime.md#rt-rte-session-capture]
          note: "Summary labels and native replay establish retention/possible delivery, not the automatic original write or complete later-consumer chain; other codecs remain uninspected."
        - scope: "Capture configuration, progress/cache state, bulk/library admissions and opaque restored payloads"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-adapter-config, memory.md#mem-rte-sync-watermarks, memory.md#mem-rte-archive-transfer, runtime.md#rt-rte-session-restore]
          note: "Operational persistence alone does not establish a qualifying experience-to-behavior-shaping write; generic content control and opaque host consumption remain unresolved. No system-wide no follows."
      records: [epistemic.md#epi-rte-search-projection, memory.md#mem-rte-message-embedding, memory.md#mem-obj-checkpoint-carriers, memory.md#mem-rte-archive-transfer]
      note: "Two wired artifact-update witnesses establish yes locally; unresolved original summary and alternate write/consumer routes prevent complete coverage."
    trace_source:
      assessment: partial
      units:
        - scope: "Qualifying conversational projection and message-vector writes"
          assessment: known
          findings:
            - value: session-logs
              basis: wired
              records: [epistemic.md#epi-rte-search-projection, memory.md#mem-obj-search-text, memory.md#mem-rte-message-embedding]
              note: "Original inputs are recorded conversational User/Assistant text and selected file descriptors, not new event-stream sources created by canonical serialization."
          records: [epistemic.md#epi-rte-search-projection, memory.md#mem-obj-search-text, memory.md#mem-rte-message-embedding]
          note: "Inspected projection excludes tool bodies, reasoning, injected and System content; archival tool traces therefore do not establish tool-traces on these qualifying writes."
        - scope: "Unresolved upstream summary/checkpoint updates and other codec/library trace-fed alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-checkpoint-carriers, memory.md#mem-obj-raw-record, memory.md#mem-rte-archive-transfer, runtime.md#rt-rte-session-capture]
          note: "The original qualifying write and its consumed input mixture are not established. Summary/raw wrappers do not resolve session, tool, environmental-event or trajectory origins."
      records: [epistemic.md#epi-rte-search-projection, memory.md#mem-rte-message-embedding, memory.md#mem-obj-checkpoint-carriers, memory.md#mem-rte-archive-transfer]
      note: "Session-log input is wired for the two positive writes; unresolved alternatives prevent complete trace-source coverage or global inapplicability."
---

# Pond memory profile

## Comparison rationale

The comparison boundary is retained session evidence and its access/capture state, not the entire runtime. Static recall guidelines and fixed embedder weights are excluded even though they affect behavior. Changed configuration is included because later capture loads the retained choices: [RT-RTE-adapter-config](runtime.md#rt-rte-adapter-config). Ordinary current-batch check outputs and benchmark CSVs have no established later behavioral consumer in these records; they cannot enlarge this memory inventory merely because they can be printed or stored.

All positive findings are implementation wiring unless explicitly marked claimed. Local file storage does not upgrade the S3 claim in [EPI-CLM-archive-recall](epistemic.md#epi-clm-archive-recall). No finding asserts observed operation, reliable model compliance or causal task benefit. Coverage remains partial where accepted records retain opaque payloads, uninspected codecs, original summary-generation gaps or unspecified callers. Missing execution alone does not weaken a wired architectural witness.

Canonical history, searchable text and numerical vectors have different consumers. Historical tool results can be knowledge when requested through full-message or SQL reads, but are excluded from the inspected search projection. Thus the positive trace-source value is session-logs, not every trace type found somewhere in the archive. The reduced searchable representation and vector update qualify as automatic trace-fed artifact writes under this profile's definition: [EPI-RTE-search-projection](epistemic.md#epi-rte-search-projection), [MEM-RTE-message-embedding](memory.md#mem-rte-message-embedding). This classification is independent of improved capacity, parameter training and epistemic acceptance. Their inputs have learning force at the durable-artifact update consumer; outputs have ranking force at retrieval, and readable history has knowledge force at the host: [MEM-BAP-recalled-history](memory.md#mem-bap-recalled-history).

Consolidation names the reduction performed by conversational projection and inspected reconstructed-session omission, not a claim that Pond extracts accepted beliefs. Evolve names replacement of existing stale-model vectors, not initial embedding or an index rebuild. Primary-key collision checks do not establish dedup; deletion detection does not establish invalidate or decay: [MEM-RTE-deletion-detection](memory.md#mem-rte-deletion-detection). Physical old-version cleanup is not semantic withdrawal. The 10 MiB leaf cap and reconstructed System-carrier omission qualify preservation without establishing synthesized claims: [EPI-RTE-field-extraction](epistemic.md#epi-rte-field-extraction), [MEM-OBJ-checkpoint-carriers](memory.md#mem-obj-checkpoint-carriers).

Requested recall, restore and transfer remain pull despite computational selection and delivery. Internal automatic progress fallback and embedding eligibility supply retained inputs without a consumer request for those particular retained parts, so they are separately classified as push. Cursor availability is coarse selection; the oldest-message lineage comparison is the identity match that admits the fallback cursor. Query lexical/embedding ranking on a requested recall is not a push signal: [RT-RTE-archive-recall](runtime.md#rt-rte-archive-recall), [MEM-RTE-sync-watermarks](memory.md#mem-rte-sync-watermarks). The selective workflow does not trace human-selected editor-reference insertion; no accepted canonical record establishes its direction or selector. This included missing route prevents complete read-back/signal coverage, rather than licensing a guessed manual push.

Restoration preserves separate native replay and reconstructed alternatives. A readable carrier summary cannot classify its opaque raw payload or confer present instruction authority. The native switch request is wired, but actual host parsing and force remain unresolved: [MEM-OBJ-raw-record](memory.md#mem-obj-raw-record), [MEM-OBJ-checkpoint-carriers](memory.md#mem-obj-checkpoint-carriers), [RT-BAP-session-switch](runtime.md#rt-bap-session-switch). Explicit operator selection of content for restored files/replacement is a manual admission mechanism; merely reading an existing checkpoint establishes no checkpoint write agency.

Reconciliation supersedes EPI-OBJ-search-text with [MEM-OBJ-search-text](memory.md#mem-obj-search-text), affecting form, lineage, ranking and trace classification citations. It supersedes EPI-RTE-deletion-detection with [MEM-RTE-deletion-detection](memory.md#mem-rte-deletion-detection), affecting the non-withdrawal limit. Those supersessions establish referent identity, not stronger evidence. The aggregate archive payload and its separately declared session/message/part objects remain valid containers/parts; none is treated as a replacement for the whole capture route.

Source-read log: none. This profile uses only the supplied accepted records, their annotations and reconciliation; it adds no quotes, source facts or record declarations. Validation is performed through the supplied invocation command; a structural pass is not semantic acceptance.
