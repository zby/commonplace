---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Gnosis memory profile: caller-curated JSONL entries, SQLite access state and requested cross-session consultation."
run-id: AAS-2026-10-15-gnosis-5bfb42422ce3-01
source-identity: "https://github.com/skorokithakis/gnosis"
reviewed-boundary: "429528bf98e424b40837d2dbe3631d0fb42da6fd"
memory-comparison:
  version: 2
  scope: "Accumulated entry bodies and structural fields in .gnosis/entries.jsonl, their retained SQLite FTS projection and mtime control value, caller admission and replacement, maintenance, and later search/show/latest/topics consumers. Includes instructed external-agent consultation and repository sharing, with unresolved caller control and original provenance. Excludes static embedded doctrine as a memory object, transient topic aggregates, unused library capabilities as deployed routes, and external host windows, compaction, model weights and hidden session machinery."
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Canonical entry bodies and structural fields"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-entry-text, memory.md#mem-obj-entry-metadata, epistemic.md#epi-rte-entry-retention]
              note: "JSONL retains bodies and fields across processes; decoded Go values and stdout are access stages, not additional independent retained stores."
            - value: repo
              basis: afforded
              records: [runtime.md#rt-rte-entry-maintenance, runtime.md#rt-rte-entry-admission]
              note: "The shipped workflow requests version-control sharing of .gnosis; committing and distribution remain caller responsibilities, not observed synchronization."
          records: [memory.md#mem-obj-entry-text, memory.md#mem-obj-entry-metadata, runtime.md#rt-rte-entry-maintenance, epistemic.md#epi-rte-entry-retention]
          note: "Records identify the canonical corpus and its instructed sharing path; unresolved authorship does not obscure its storage."
        - scope: "Retained lexical projection and freshness control"
          assessment: known
          findings:
            - value: sqlite
              basis: wired
              records: [memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata]
              note: "entries_fts and metadata are tables in the root-keyed cache index.db; the key/value encoding of mtime is not a separate KV service."
          records: [memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata]
          note: "Both operative cache parts are identified; disposability does not prevent retention between invocations."
      records: [memory.md#mem-obj-entry-text, memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, runtime.md#rt-rte-entry-maintenance]
      note: "The accepted inventory covers canonical content, access projection and refresh control. No opaque provider state is included in this CLI memory boundary."
    representational_form:
      assessment: known
      units:
        - scope: "Entry bodies and copied body excerpts interpreted by the later caller"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [memory.md#mem-obj-entry-text, memory.md#mem-obj-entries-fts, runtime.md#rt-rte-knowledge-read]
              note: "Bodies, reasons and returned excerpts are prose; JSON encoding does not change their form at the interpreting consumer."
          records: [memory.md#mem-obj-entry-text, memory.md#mem-obj-entries-fts, runtime.md#rt-rte-knowledge-read]
          note: "Full bodies and lossy excerpts are both covered; delivery is implemented without proving interpretation or compliance."
        - scope: "Structural fields, lexical indexing and refresh comparisons at fixed code consumers"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata]
              note: "IDs, topic keys, timestamps, FTS tokens and mtime use localized fixed lookup, ranking and comparison rules; BM25 scores are not distributed parameters."
          records: [memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata]
          note: "The symbolic access path is distinct from prose interpretation, even when the indexed source is the same text."
      records: [memory.md#mem-obj-entry-text, memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, runtime.md#rt-rte-knowledge-read]
      note: "The inventory resolves both operative forms; external host parameters are excluded rather than classified from this CLI."
    lineage:
      assessment: partial
      units:
        - scope: "Caller composition and session-to-entry selection"
          assessment: partial
          findings:
            - value: authored
              basis: afforded
              records: [memory.md#mem-obj-entry-text, runtime.md#rt-rte-entry-admission]
              note: "The workflow affords caller-authored reasons and decisions; it does not authenticate the origin of every stored assertion."
            - value: trace-extracted
              basis: afforded
              records: [runtime.md#rt-rte-entry-admission, memory.md#mem-obj-entry-text]
              note: "The memory annotation describes caller-mediated session-to-entry extraction under review doctrine; raw conversations are not automatically attached or retained."
          records: [memory.md#mem-obj-entry-text, runtime.md#rt-rte-entry-admission]
          note: "Initial composition, empirical provenance and the actual derivation of shipped bodies remain unresolved; intended session selection does not classify every existing entry."
        - scope: "CLI acquisition and replacement of caller-supplied body text"
          assessment: known
          findings:
            - value: imported
              basis: wired
              records: [epistemic.md#epi-rte-entry-import, epistemic.md#epi-rte-entry-replacement]
              note: "At this boundary software acquires submitted or edited text; the upstream authoring process and source warrant are separate unknowns."
          records: [epistemic.md#epi-rte-entry-import, epistemic.md#epi-rte-entry-replacement]
          note: "Import is resolved for the CLI acquisition edge, not for original composition."
        - scope: "Generated entry fields, normalized structural fields, lexical projection and captured mtime"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata]
              note: "Fixed code generates IDs/times, normalizes fields, copies bodies/topics into FTS and captures the snapshot timestamp; this is not extraction of original experience."
          records: [memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata]
          note: "These local derivation paths are inspected; caller-supplied fields do not acquire authenticated upstream provenance through normalization."
      records: [memory.md#mem-obj-entry-text, memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, runtime.md#rt-rte-entry-admission, epistemic.md#epi-rte-entry-import, epistemic.md#epi-rte-entry-replacement]
      note: "Supported authoring, extraction, import and compilation paths coexist. Missing initial origin prevents complete lineage classification of the corpus."
    behavioral_authority:
      assessment: known
      units:
        - scope: "Retained entry prose at the instructed later coding-agent consumer"
          assessment: known
          findings:
            - value: knowledge
              basis: afforded
              records: [memory.md#mem-obj-entry-text, runtime.md#rt-bap-agent-guidance]
              note: "Requested prose supplies advisory repository context and reasons for planning; the external agent must interpret it. No later decision effect is observed."
          records: [memory.md#mem-obj-entry-text, runtime.md#rt-bap-agent-guidance]
          note: "This is advisory knowledge consumption, not standing host instructions or a code-edit veto; static doctrine is excluded from accumulated memory."
        - scope: "Retained body/topic features and creation times at search and recent-entry ordering consumers"
          assessment: known
          findings:
            - value: ranking
              basis: wired
              records: [memory.md#mem-obj-entries-fts, memory.md#mem-obj-entry-metadata, epistemic.md#epi-rte-lexical-selection, runtime.md#rt-rte-knowledge-read]
              note: "Text/topics affect FTS match and relative rank; CreatedAt affects latest order. Fixed scoring code does not remove the retained inputs' ranking authority."
          records: [memory.md#mem-obj-entries-fts, memory.md#mem-obj-entry-metadata, epistemic.md#epi-rte-lexical-selection, runtime.md#rt-rte-knowledge-read]
          note: "The authority is output priority, not credibility or demonstrated task influence."
        - scope: "Retained entry IDs/topics at lookup and membership selection; cached mtime at refresh branching"
          assessment: known
          findings:
            - value: routing
              basis: wired
              records: [memory.md#mem-obj-entry-metadata, memory.md#mem-obj-metadata, epistemic.md#epi-rte-cache-refresh]
              note: "IDs/topics select retained entries or groups; mtime comparison selects rebuild versus reuse of the retained projection."
          records: [memory.md#mem-obj-entry-metadata, memory.md#mem-obj-metadata, epistemic.md#epi-rte-cache-refresh]
          note: "Attribution and displayed Related fields have no additional executable supersession force; mtime routing is not semantic endorsement."
        - scope: "Existing retained IDs at related-reference admission and edit checks"
          assessment: known
          findings:
            - value: validation
              basis: wired
              records: [memory.md#mem-obj-entry-metadata, epistemic.md#epi-rte-structure-check, epistemic.md#epi-rte-edit-check]
              note: "Existing IDs determine whether submitted related prefixes resolve uniquely within the path-specific validation snapshot."
            - value: enforcement
              basis: wired
              records: [epistemic.md#epi-rte-structure-check, epistemic.md#epi-rte-edit-check]
              note: "Failure of reference resolution can veto the write or changed interactive edit; non-interactive body edits do not revalidate surviving references."
          records: [memory.md#mem-obj-entry-metadata, epistemic.md#epi-rte-structure-check, epistemic.md#epi-rte-edit-check]
          note: "This force belongs to retained IDs as structural criteria, not to the prose's truth or an authenticated author. Pre-append resolution and interactive locked resolution have different timing guarantees."
      records: [memory.md#mem-obj-entry-text, memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, runtime.md#rt-bap-agent-guidance, epistemic.md#epi-rte-structure-check, epistemic.md#epi-rte-edit-check, epistemic.md#epi-rte-cache-refresh, epistemic.md#epi-rte-lexical-selection]
      note: "Known covers the recorded consumers and their forces, not actual compliance. Display-only attribution/navigation does not add authority, and unknown upstream composition does not obscure these local consumers."
    write_agency:
      assessment: partial
      units:
        - scope: "Caller decision supplying, replacing or removing retained body/metadata through CLI or direct JSONL edits/merges"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-entry-admission, runtime.md#rt-rte-entry-maintenance, epistemic.md#epi-rte-candidate-choice, epistemic.md#epi-rte-entry-replacement, memory.md#mem-obj-entry-metadata]
          note: "The records leave human versus computational decision-making unresolved. An editor, author flag, Git identity or explicit command is not per-content human approval; software I/O alone does not resolve semantic admission control."
        - scope: "Code-generated IDs/timestamps and automatic normalization on admission or reload"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-entry-metadata, epistemic.md#epi-rte-entry-retention]
              note: "Code determines generated fields and read-time normalization without a separate human content decision. This does not classify admission of caller-selected prose."
          records: [memory.md#mem-obj-entry-metadata, epistemic.md#epi-rte-entry-retention]
          note: "Known only for these generated/normalized structural parts."
        - scope: "FTS projection and freshness timestamp admission on automatic refresh or requested reindex"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-cache-refresh]
              note: "Software copies the corpus and captures mtime without approval of each derived row. Requesting reindex does not make its row admission manual."
          records: [memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-cache-refresh]
          note: "Both refresh triggers share program-controlled derived-state admission."
      records: [runtime.md#rt-rte-entry-admission, runtime.md#rt-rte-entry-maintenance, memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-candidate-choice, epistemic.md#epi-rte-cache-refresh]
      note: "Automatic derived-state and field updates are supported; unresolved per-content caller control prevents a complete agency classification or a manual finding."
    curation_operations:
      assessment: partial
      units:
        - scope: "Existing-entry body and interactive metadata replacement"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-entry-maintenance, epistemic.md#epi-rte-entry-replacement]
              note: "Edit revises an existing retained entry and UpdatedAt; this capacity does not establish that the replacement is better or true."
          records: [runtime.md#rt-rte-entry-maintenance, epistemic.md#epi-rte-entry-replacement]
          note: "Positional, piped and editor replacements are covered with their different checks; internal prior-body history is not retained."
        - scope: "Explicit removal of retained entries"
          assessment: known
          findings:
            - value: decay
              basis: wired
              records: [epistemic.md#epi-rte-entry-withdrawal, runtime.md#rt-rte-entry-maintenance]
              note: "rm forgets selected entries by deleting corpus membership. It is caller-triggered, not time-based downweighting."
          records: [epistemic.md#epi-rte-entry-withdrawal, memory.md#mem-obj-metadata]
          note: "Deletion does not retain an internal tombstone/history, so it does not establish invalidate. Previously delivered context and stale cache copies can survive."
        - scope: "Caller session-to-entry selection and semantic maintenance beyond replacement/removal mechanics"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-entry-text, runtime.md#rt-rte-entry-admission, epistemic.md#epi-rte-candidate-filter, epistemic.md#epi-rte-candidate-choice]
          note: "Doctrine requests selection of useful session knowledge, but records do not establish the caller's actual transformation. Consolidation, synthesis or deduplication of retained content cannot be inferred from review instructions or unknown composition."
        - scope: "FTS rebuild, mtime capture and structural normalization"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-cache-refresh]
          note: "These access/encoding operations alone do not implement a controlled curation operation; topic-array normalization is not semantic duplicate-memory removal."
      records: [runtime.md#rt-rte-entry-maintenance, runtime.md#rt-rte-entry-admission, epistemic.md#epi-rte-entry-replacement, epistemic.md#epi-rte-entry-withdrawal, epistemic.md#epi-rte-cache-refresh, epistemic.md#epi-rte-candidate-filter, memory.md#mem-obj-entry-text, memory.md#mem-obj-metadata]
      note: "Replacement and forgetting are supported positives. Unknown caller transformations prevent complete curation coverage; related prose alone does not execute supersession or promotion."
    read_back_direction:
      assessment: known
      units:
        - scope: "Later search, show, latest and topics requests, including lexical selection and formatted return"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [runtime.md#rt-rte-knowledge-read, epistemic.md#epi-rte-lexical-selection, memory.md#mem-obj-entry-text]
              note: "The caller explicitly requests retained material. Internal ranking, snippet production and stdout delivery fulfill that request rather than creating independent pushes."
          records: [runtime.md#rt-rte-knowledge-read, epistemic.md#epi-rte-lexical-selection, memory.md#mem-obj-entry-text]
          note: "ID/topic full reads, lexical search and recent/topic browsing cover the recorded later-consumer routes. Static help is not accumulated memory; external hooks are excluded."
        - scope: "Retained access state consumed during requested search"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-cache-refresh]
              note: "The search invocation reads retained index rows and freshness state as dependencies of the requested operation; no unsolicited agent-context delivery follows."
          records: [memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-cache-refresh]
          note: "Automatic refresh is a derived-state write inside this chain, not an independent read-back push."
      records: [runtime.md#rt-rte-knowledge-read, memory.md#mem-obj-entry-text, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-lexical-selection, epistemic.md#epi-rte-cache-refresh]
      note: "The accepted inventory and memory annotation cover the shipped dispatch and later read routes without an unresolved alternative delivery mechanism inside this boundary. Actual invocation remains unobserved."
    read_back_signal:
      assessment: inapplicable
      units:
        - scope: "All scoped later read-back operations"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-knowledge-read, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-cache-refresh]
          note: "The completely classified direction inventory is request-driven. FTS lexical matching, ID matching and recent-entry filters are pull selectors here, not push signals."
      records: [runtime.md#rt-rte-knowledge-read, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-cache-refresh]
      note: "No included unresolved push alternative remains in the recorded CLI boundary. Host-side context injection is excluded rather than declared absent."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Caller-mediated session-to-entry writing and subsequent semantic replacement"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-entry-admission, memory.md#mem-obj-entry-text, epistemic.md#epi-rte-candidate-choice, epistemic.md#epi-rte-entry-replacement, runtime.md#rt-bap-agent-guidance]
          note: "Session-derived durable prose and a later advisory consumer are afforded, but automatic per-content admission and original trace inputs are unresolved. Thus neither yes nor a bounded no is established for this route. Missing observed improvement is not the reason for withholding yes."
        - scope: "Generated structural fields and JSONL-to-FTS/mtime updates"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-cache-refresh]
          note: "These automatic updates take entry values and file metadata, not an established activity-trace learning input. Indexing is not an additional trace-fed behavior-shaping write merely because upstream prose may describe experience."
      records: [runtime.md#rt-rte-entry-admission, memory.md#mem-obj-entry-text, memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-candidate-choice, epistemic.md#epi-rte-entry-replacement, epistemic.md#epi-rte-cache-refresh, runtime.md#rt-bap-agent-guidance]
      note: "No positive qualifying automatic trace-fed route is established, and unknown caller control prevents a complete negative. This is not an absence claim about external agents."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Potential caller session-to-entry learning routes"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-entry-text, runtime.md#rt-rte-entry-admission, epistemic.md#epi-rte-entry-import, epistemic.md#epi-rte-candidate-choice]
          note: "Review mentions sessions and human/empirical information, but the records establish neither a qualifying automatic write nor whether original content was recorded conversation, tools, events or linked trajectories. A session reference alone does not prove session-logs as the actual consumed source."
        - scope: "Structural generation and derived access-state updates"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-cache-refresh]
          note: "No qualifying trace-learning route is established for these fixed transformations of entries and file metadata, so they have no learning trace-source value."
      records: [memory.md#mem-obj-entry-text, runtime.md#rt-rte-entry-admission, epistemic.md#epi-rte-entry-import, epistemic.md#epi-rte-candidate-choice, memory.md#mem-obj-entry-metadata, memory.md#mem-obj-entries-fts, memory.md#mem-obj-metadata, epistemic.md#epi-rte-cache-refresh]
      note: "Unresolved caller-mediated learning prevents system-level inapplicability; trace origin is not inferred from storage format, prose subject or review terminology."
---

# Gnosis memory profile

## Comparison rationale

The comparison boundary is accumulated entries and their retained access state, not the static help text or the external coding runtime. The four operative parts are [MEM-OBJ-entry-text](memory.md#mem-obj-entry-text), [MEM-OBJ-entry-metadata](memory.md#mem-obj-entry-metadata), [MEM-OBJ-entries-fts](memory.md#mem-obj-entries-fts) and [MEM-OBJ-metadata](memory.md#mem-obj-metadata). Decoded objects, snippets and topic counts are consumption stages, not independently accumulated stores. Repository sharing is an afforded use of the canonical file, not a wired replication service.

Reconciliation supersedes the epistemic declarations of entry text, entry metadata and entries FTS with the corresponding memory declarations. This profile cites those canonical memory objects. The epistemic import, check, replacement, withdrawal and refresh routes remain distinct functional parts of valid runtime containers; they are not superseded. These connections change citation ownership, not evidence strength.

Authority is consumer-specific. Entry prose provides advisory knowledge at the external agent, while retained text/topics influence lexical priority and metadata controls lookup and refresh. Existing IDs also act as criteria and veto inputs for related-reference admission. These are structural validation and enforcement, not epistemic acceptance of body claims. See [RT-BAP-agent-guidance](runtime.md#rt-bap-agent-guidance), [EPI-RTE-structure-check](epistemic.md#epi-rte-structure-check) and [EPI-RTE-edit-check](epistemic.md#epi-rte-edit-check). Unauthenticated author metadata and displayed Related pointers do not confer additional force.

Editing supports evolution; deletion supports forgetting. Neither establishes history-preserving invalidation. Writing a related replacement does not automatically suppress the original, and cache freshness is not reliable semantic withdrawal. The limits follow [EPI-RTE-entry-replacement](epistemic.md#epi-rte-entry-replacement), [EPI-RTE-entry-withdrawal](epistemic.md#epi-rte-entry-withdrawal) and [MEM-OBJ-metadata](memory.md#mem-obj-metadata). No consolidation or synthesis finding is inferred from a request to review session knowledge; the original session and the caller's actual transformation are unresolved.

All recorded read-back routes fulfill explicit requests. Ranking and identifier lookup inside those requests are not push delivery, so the push-signal axis is inapplicable even though lexical and identity selectors exist. This conclusion uses the complete shipped read-route inventory and annotation on [RT-RTE-knowledge-read](runtime.md#rt-rte-knowledge-read), not a claim that every possible external integration was inspected.

The automatic generation of fields and derived indexes does not resolve who decided to admit prose. Likewise, an afforded session-extraction path does not establish an automatic trace-fed write. Unknown per-content caller control and original inputs remain in both trace axes. No positive trace-learning value or system-wide negative is asserted. No source files were read for this classification; all warrants and coverage limits come from the supplied accepted records. No operation, compliance, improved capacity or causal benefit is inferred from implementation evidence.
