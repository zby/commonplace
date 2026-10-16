---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "deja-vu memory comparison: retained notes, historical indexes, trace-derived advisory state, continuation packets and standing-rule copies at the frozen boundary."
run-id: "AAS-2026-10-14-deja-vu-22137d4d39a5-01"
source-identity: "https://github.com/vshulcz/deja-vu"
reviewed-boundary: "4c08fb26ad8a8b8e656a120f06ca4175a7078148"
memory-comparison:
  version: 2
  scope: "Included: explicit/promoted notes and lifecycle rows; normalized historical text and access metadata; mined fix, token, command/failure and session-outcome sidecars; dense retrieval outputs and unresolved associated provider retention; cached/served digests and delivery/failure/usage state; continuation content and identity; adopted standing-rule source/copies; changed activation/suppression controls; import and recovery writes; unresolved specialized queue/checkpoint, parser, maintenance and consumer alternatives. Excluded: shipped static instructions, unchanged binary/generated wiring, external host inference/tool scheduling and original transcript production, and temporary offline-evaluation state without a later production consumer. Provider weights are not assumed to change through use."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Plain/promoted notes and local lifecycle rows"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "epistemic.md#epi-obj-lifecycle"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "memory.md#mem-obj-notes"
            - "epistemic.md#epi-obj-lifecycle"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Normalized historical text records"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-records"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "memory.md#mem-obj-records"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Session and imported lifecycle metadata"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-meta"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "memory.md#mem-obj-session-meta"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Pre-judgment fix evidence"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixraw"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "memory.md#mem-obj-fixraw"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Judged fixes and held candidates"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixes"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "memory.md#mem-obj-fixes"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Token neighbor map"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-cooccur"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "memory.md#mem-obj-cooccur"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Recurring command table"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-commands"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "memory.md#mem-obj-commands"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Failure warning table and its update evidence"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-commandfails"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "memory.md#mem-obj-commandfails"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Session commands/outcomes"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-sessionfacts"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "memory.md#mem-obj-sessionfacts"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Continuation content"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "memory.md#mem-obj-compaction-data"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Continuation identity/freshness metadata"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-state"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "memory.md#mem-obj-compaction-state"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Standing rules source and installed copies"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Dense numerical sidecar"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-embed-client"
                - "runtime.md#rt-rte-embedding-records"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Rendered digest caches and served-text snapshots"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-auto-delivery"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "runtime.md#rt-rte-auto-delivery"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Persistent delivery/failure/usage metadata"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-auto-delivery"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Changed activation policy and suppression state"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-policy"
                - "memory.md#mem-rte-forget-cleanup"
              note: "Records identify local files or persisted filesystem state for this part."
          records:
            - "runtime.md#rt-obj-policy"
            - "memory.md#mem-rte-forget-cleanup"
          note: "The named local retained part is stored on the filesystem; JSONL, gob and binary are encodings, not database substrates."
        - scope: "Process memoization of local lifecycle lookup"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-lifecycle"
              note: "Process memoization holds accumulated lifecycle rows between lookup consumers."
          records:
            - "epistemic.md#epi-obj-lifecycle"
          note: "The keyed lifecycle lookup also has a process-resident memoized representation."
        - scope: "Opaque embedding-provider state associated with retained numerical outputs"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
          note: "Endpoint substrate and any provider-retained input/output state are uninspected; the local sidecar does not resolve them."
        - scope: "Included specialized stop/deferred/checkpoint hooks, other host integrations and parser/recovery variants"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Specialized retained queue/checkpoint payloads and usage rotation/layout are not classified by the common filesystem witnesses."
      records:
        - "memory.md#mem-obj-notes"
        - "epistemic.md#epi-obj-lifecycle"
        - "memory.md#mem-obj-records"
        - "memory.md#mem-obj-session-meta"
        - "memory.md#mem-obj-fixraw"
        - "memory.md#mem-obj-fixes"
        - "memory.md#mem-obj-cooccur"
        - "memory.md#mem-obj-commands"
        - "memory.md#mem-obj-commandfails"
        - "memory.md#mem-obj-sessionfacts"
        - "memory.md#mem-obj-compaction-data"
        - "memory.md#mem-obj-compaction-state"
        - "runtime.md#rt-obj-rules"
        - "runtime.md#rt-rte-rules-sync"
        - "runtime.md#rt-cmp-embed-client"
        - "runtime.md#rt-rte-embedding-records"
        - "runtime.md#rt-rte-auto-delivery"
        - "runtime.md#rt-rte-compaction-recovery"
        - "runtime.md#rt-obj-policy"
        - "memory.md#mem-rte-forget-cleanup"
      note: "Local filesystem witnesses and lifecycle memoization are established. Opaque provider retention and specialized state prevent a complete substrate inventory; no SQLite, graph or vector-database substrate is inferred from serialization or dense encoding."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Note text and promoted receipts"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "epistemic.md#epi-obj-promoted-text"
              note: "The operative textual content supplies interpreted context, receipts or directions."
          records:
            - "memory.md#mem-obj-notes"
            - "epistemic.md#epi-obj-promoted-text"
          note: "Text is consumed through human/model interpretation, independently of its container."
        - scope: "Historical prose/code at model or human readers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-records"
              note: "The operative textual content supplies interpreted context, receipts or directions."
          records:
            - "memory.md#mem-obj-records"
          note: "Text is consumed through human/model interpretation, independently of its container."
        - scope: "Titles and imported lifecycle display text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-meta"
              note: "The operative textual content supplies interpreted context, receipts or directions."
          records:
            - "memory.md#mem-obj-session-meta"
          note: "Text is consumed through human/model interpretation, independently of its container."
        - scope: "Fix error/remedy strings at later readers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixes"
              note: "The operative textual content supplies interpreted context, receipts or directions."
          records:
            - "memory.md#mem-obj-fixes"
          note: "Text is consumed through human/model interpretation, independently of its container."
        - scope: "Command strings and failure lines at later readers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-commands"
                - "memory.md#mem-obj-commandfails"
                - "memory.md#mem-obj-sessionfacts"
              note: "The operative textual content supplies interpreted context, receipts or directions."
          records:
            - "memory.md#mem-obj-commands"
            - "memory.md#mem-obj-commandfails"
            - "memory.md#mem-obj-sessionfacts"
          note: "Text is consumed through human/model interpretation, independently of its container."
        - scope: "Continuation objective, conclusions, constraints and carry at model readers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
              note: "The operative textual content supplies interpreted context, receipts or directions."
          records:
            - "memory.md#mem-obj-compaction-data"
          note: "Text is consumed through human/model interpretation, independently of its container."
        - scope: "Rules prose at intended host instruction readers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
              note: "The operative textual content supplies interpreted context, receipts or directions."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
          note: "Text is consumed through human/model interpretation, independently of its container."
        - scope: "Rendered digest cache and snapshot text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-auto-delivery"
              note: "The operative textual content supplies interpreted context, receipts or directions."
          records:
            - "runtime.md#rt-rte-auto-delivery"
          note: "Text is consumed through human/model interpretation, independently of its container."
        - scope: "Note project/tags/provenance/lifecycle selectors"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "epistemic.md#epi-obj-lifecycle"
              note: "Keys, flags, counts or markers determine fixed-code behavior."
          records:
            - "memory.md#mem-obj-notes"
            - "epistemic.md#epi-obj-lifecycle"
          note: "Localized fields have fixed-rule consumers; this unit excludes the same objects' separately interpreted prose."
        - scope: "Record keys/roles/times and retrieval postings"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-records"
                - "runtime.md#rt-obj-index-db"
              note: "Keys, flags, counts or markers determine fixed-code behavior."
          records:
            - "memory.md#mem-obj-records"
            - "runtime.md#rt-obj-index-db"
          note: "Localized fields have fixed-rule consumers; this unit excludes the same objects' separately interpreted prose."
        - scope: "Session project/origin/path/lifecycle metadata"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-meta"
              note: "Keys, flags, counts or markers determine fixed-code behavior."
          records:
            - "memory.md#mem-obj-session-meta"
          note: "Localized fields have fixed-rule consumers; this unit excludes the same objects' separately interpreted prose."
        - scope: "Raw/judged fix signatures, flags and provenance at fixed code"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixraw"
                - "memory.md#mem-obj-fixes"
              note: "Keys, flags, counts or markers determine fixed-code behavior."
          records:
            - "memory.md#mem-obj-fixraw"
            - "memory.md#mem-obj-fixes"
          note: "Localized fields have fixed-rule consumers; this unit excludes the same objects' separately interpreted prose."
        - scope: "Token association map"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-cooccur"
              note: "Keys, flags, counts or markers determine fixed-code behavior."
          records:
            - "memory.md#mem-obj-cooccur"
          note: "Localized fields have fixed-rule consumers; this unit excludes the same objects' separately interpreted prose."
        - scope: "Command counts, failure keys and known-exit flags"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-commands"
                - "memory.md#mem-obj-commandfails"
                - "memory.md#mem-obj-sessionfacts"
              note: "Keys, flags, counts or markers determine fixed-code behavior."
          records:
            - "memory.md#mem-obj-commands"
            - "memory.md#mem-obj-commandfails"
            - "memory.md#mem-obj-sessionfacts"
          note: "Localized fields have fixed-rule consumers; this unit excludes the same objects' separately interpreted prose."
        - scope: "Continuation provenance/outcomes and capture identity/fingerprints"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
                - "memory.md#mem-obj-compaction-state"
              note: "Keys, flags, counts or markers determine fixed-code behavior."
          records:
            - "memory.md#mem-obj-compaction-data"
            - "memory.md#mem-obj-compaction-state"
          note: "Localized fields have fixed-rule consumers; this unit excludes the same objects' separately interpreted prose."
        - scope: "Rule copy markers at maintenance code"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
              note: "Keys, flags, counts or markers determine fixed-code behavior."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
          note: "Localized fields have fixed-rule consumers; this unit excludes the same objects' separately interpreted prose."
        - scope: "Delivery/failure tokens and usage event bookkeeping"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-auto-delivery"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Keys, flags, counts or markers determine fixed-code behavior."
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Localized fields have fixed-rule consumers; this unit excludes the same objects' separately interpreted prose."
        - scope: "Activation grants and forgetting tombstones"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-policy"
                - "memory.md#mem-rte-forget-cleanup"
              note: "Keys, flags, counts or markers determine fixed-code behavior."
          records:
            - "runtime.md#rt-obj-policy"
            - "memory.md#mem-rte-forget-cleanup"
          note: "Localized fields have fixed-rule consumers; this unit excludes the same objects' separately interpreted prose."
        - scope: "Retained dense sidecar at similarity/rerank code"
          assessment: "known"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-embed-client"
                - "runtime.md#rt-rte-embedding-records"
              note: "Distributed dense representations influence numerical similarity; they are not localized symbolic neighbors."
          records:
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
          note: "Dense numerical representations are distinct from text hits and token counts."
        - scope: "Included specialized stop/deferred/checkpoint hooks, other host integrations and parser/recovery variants"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
          note: "Specialized payloads, variant checkpoints, usage consumers and opaque provider-retained parts lack complete form/consumer coverage."
      records:
        - "memory.md#mem-obj-notes"
        - "epistemic.md#epi-obj-promoted-text"
        - "memory.md#mem-obj-records"
        - "memory.md#mem-obj-session-meta"
        - "memory.md#mem-obj-fixes"
        - "memory.md#mem-obj-commands"
        - "memory.md#mem-obj-commandfails"
        - "memory.md#mem-obj-sessionfacts"
        - "memory.md#mem-obj-compaction-data"
        - "runtime.md#rt-obj-rules"
        - "runtime.md#rt-rte-rules-sync"
        - "runtime.md#rt-rte-auto-delivery"
        - "epistemic.md#epi-obj-lifecycle"
        - "runtime.md#rt-obj-index-db"
        - "memory.md#mem-obj-fixraw"
        - "memory.md#mem-obj-cooccur"
        - "memory.md#mem-obj-compaction-state"
        - "runtime.md#rt-rte-compaction-recovery"
        - "runtime.md#rt-obj-policy"
        - "memory.md#mem-rte-forget-cleanup"
        - "runtime.md#rt-cmp-embed-client"
        - "runtime.md#rt-rte-embedding-records"
      note: "Natural-language, symbolic and parametric parts are separated by operative consumption. The mixed inventory remains partial; a readable summary does not classify an opaque checkpoint or provider payload."
    lineage:
      assessment: "partial"
      units:
        - scope: "Caller-supplied note text and promoted --note override"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "runtime.md#rt-rte-note-admission"
              note: "Supplied original note/decision prose is authored content, whether by a human or model."
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-note-admission"
          note: "Authorship is distinct from admission; neither human identity nor human approval is inferred."
        - scope: "Default promotion receipt extraction"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-promote-distill"
                - "memory.md#mem-obj-notes"
              note: "Fixed extraction selects the session ask, last assistant text or detected decision for a durable promoted note."
          records:
            - "epistemic.md#epi-rte-promote-distill"
            - "memory.md#mem-obj-notes"
          note: "This path differs from the caller override."
        - scope: "Standing rule formulation under the prescribed review workflow"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
              note: "The skill asks the foreground model to formulate selected standing rules."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
          note: "Model synthesis and user adoption are prescribed, not observed."
        - scope: "Installed copies of retained standing rules"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
              note: "Sync reads the retained source and copies its normalized marked body to known host files."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
          note: "Copying preserves a separate imported route into host instruction files."
        - scope: "Transcript/note/import inputs and normalized index records"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-records"
                - "runtime.md#rt-obj-index-db"
                - "runtime.md#rt-rte-import-records"
              note: "Parsed/reloaded host history, notes and external batches enter the retrieval corpus."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-records"
                - "runtime.md#rt-obj-index-db"
                - "runtime.md#rt-rte-import-records"
              note: "Normalization, redaction, clipping and posting construction produce local retrieval representations."
          records:
            - "memory.md#mem-obj-records"
            - "runtime.md#rt-obj-index-db"
            - "runtime.md#rt-rte-import-records"
          note: "Host source production remains external; each local admission/derivation path is distinguished."
        - scope: "Session/lifecycle metadata derived from parsed or imported content"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-meta"
              note: "Fixed rendering/metadata construction or embedding compilation derives this retained part from its inputs."
          records:
            - "memory.md#mem-obj-session-meta"
          note: "This classification names the recorded local derivation, not complete initial provenance."
        - scope: "Dense sidecar output derivation from record text"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-embed-client"
                - "runtime.md#rt-rte-embedding-records"
              note: "Fixed rendering/metadata construction or embedding compilation derives this retained part from its inputs."
          records:
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
          note: "This classification names the recorded local derivation, not complete initial provenance."
        - scope: "Rendered cached digests and served-text snapshots"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-auto-delivery"
              note: "Fixed rendering/metadata construction or embedding compilation derives this retained part from its inputs."
          records:
            - "runtime.md#rt-rte-auto-delivery"
          note: "This classification names the recorded local derivation, not complete initial provenance."
        - scope: "Fix evidence and judged table"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixraw"
                - "memory.md#mem-obj-fixes"
                - "memory.md#mem-rte-trace-mining"
              note: "Recorded messages, commands, outputs or edit observations supply the derivation."
          records:
            - "memory.md#mem-obj-fixraw"
            - "memory.md#mem-obj-fixes"
            - "memory.md#mem-rte-trace-mining"
          note: "The object derives from recorded session activity; previous continuation material can also feed recapture."
        - scope: "Token neighbors"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-cooccur"
              note: "Recorded messages, commands, outputs or edit observations supply the derivation."
          records:
            - "memory.md#mem-obj-cooccur"
          note: "The object derives from recorded session activity; previous continuation material can also feed recapture."
        - scope: "Recurring commands"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-commands"
              note: "Recorded messages, commands, outputs or edit observations supply the derivation."
          records:
            - "memory.md#mem-obj-commands"
          note: "The object derives from recorded session activity; previous continuation material can also feed recapture."
        - scope: "Command failures and update evidence"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-commandfails"
              note: "Recorded messages, commands, outputs or edit observations supply the derivation."
          records:
            - "memory.md#mem-obj-commandfails"
          note: "The object derives from recorded session activity; previous continuation material can also feed recapture."
        - scope: "Session commands and outcomes"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-sessionfacts"
              note: "Recorded messages, commands, outputs or edit observations supply the derivation."
          records:
            - "memory.md#mem-obj-sessionfacts"
          note: "The object derives from recorded session activity; previous continuation material can also feed recapture."
        - scope: "Continuation content and capture provenance"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
                - "memory.md#mem-obj-compaction-state"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Recorded messages, commands, outputs or edit observations supply the derivation."
          records:
            - "memory.md#mem-obj-compaction-data"
            - "memory.md#mem-obj-compaction-state"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "The object derives from recorded session activity; previous continuation material can also feed recapture."
        - scope: "Initial admission/provenance of existing rules, policies, local bookkeeping and imported original authorship"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
            - "runtime.md#rt-obj-policy"
            - "memory.md#mem-obj-session-meta"
            - "runtime.md#rt-rte-auto-delivery"
          note: "Generic file/caller identity and origin labels do not resolve every initial derivation path; imported origin is not authenticated authorship."
        - scope: "Exact embedding model/weight and opaque provider-state provenance"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
          note: "Name/dimension checks do not pin provider weights or their history."
        - scope: "Included specialized stop/deferred/checkpoint hooks, other host integrations and parser/recovery variants"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Variant parser/checkpoint and specialized retained-payload derivations remain uninspected."
      records:
        - "memory.md#mem-obj-notes"
        - "runtime.md#rt-rte-note-admission"
        - "epistemic.md#epi-rte-promote-distill"
        - "runtime.md#rt-obj-rules"
        - "runtime.md#rt-rte-rules-sync"
        - "memory.md#mem-obj-records"
        - "runtime.md#rt-obj-index-db"
        - "runtime.md#rt-rte-import-records"
        - "memory.md#mem-obj-session-meta"
        - "runtime.md#rt-cmp-embed-client"
        - "runtime.md#rt-rte-embedding-records"
        - "runtime.md#rt-rte-auto-delivery"
        - "memory.md#mem-obj-fixraw"
        - "memory.md#mem-obj-fixes"
        - "memory.md#mem-rte-trace-mining"
        - "memory.md#mem-obj-cooccur"
        - "memory.md#mem-obj-commands"
        - "memory.md#mem-obj-commandfails"
        - "memory.md#mem-obj-sessionfacts"
        - "memory.md#mem-obj-compaction-data"
        - "memory.md#mem-obj-compaction-state"
        - "runtime.md#rt-rte-compaction-recovery"
        - "runtime.md#rt-obj-policy"
      note: "Authored, imported, trace-extracted and other-compiled paths coexist. Known local derivations do not settle initial rules provenance, exact provider provenance or uninspected alternative paths."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Historical text, receipts, fixes, commands and outcomes at recall/model readers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-records"
                - "memory.md#mem-obj-fixes"
                - "memory.md#mem-obj-commands"
                - "memory.md#mem-obj-commandfails"
                - "memory.md#mem-obj-sessionfacts"
                - "runtime.md#rt-rte-requested-recall"
                - "runtime.md#rt-bap-recall-reference"
              note: "Selected historical content supplies reference/evidence to the receiving human or host model."
          records:
            - "memory.md#mem-obj-records"
            - "memory.md#mem-obj-fixes"
            - "memory.md#mem-obj-commands"
            - "memory.md#mem-obj-commandfails"
            - "memory.md#mem-obj-sessionfacts"
            - "runtime.md#rt-rte-requested-recall"
            - "runtime.md#rt-bap-recall-reference"
          note: "The force is contextual evidence or advice, not executed actions or warranted truth."
        - scope: "Continuation objectives, conclusions and recorded outcomes at recovery reader"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Recovery passes extracted prior-work context and receipts to the later model invocation."
          records:
            - "memory.md#mem-obj-compaction-data"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Framed continuation is advisory; successful host receipt/use is unobserved."
        - scope: "Accepted convention prose at the requested standing-decision consumer"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-rte-convention-delivery"
                - "runtime.md#rt-bap-recall-reference"
              note: "The reminder explicitly asks the model to follow accepted standing decisions unless the user overrides."
          records:
            - "memory.md#mem-rte-convention-delivery"
            - "runtime.md#rt-bap-recall-reference"
          note: "The imperative request coexists with untrusted-history framing; compliance and effective priority remain unresolved."
        - scope: "Continuation standing constraints and carry directions at later model reader"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Retained selected user constraints/carry instructions guide the intended continuation consumer."
          records:
            - "memory.md#mem-obj-compaction-data"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Direction-bearing content is separated from factual packet evidence."
        - scope: "Rules prose at the intended later global host instruction loader/model"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "afforded"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
                - "runtime.md#rt-bap-standing-rules"
              note: "Marked standing-rule copies are intended to supply ongoing directions."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
            - "runtime.md#rt-bap-standing-rules"
          note: "Wired file distribution establishes the intended channel, not actual host loading or obedience."
        - scope: "Retained corpus and raw sightings at automatic fix/sidecar update consumer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-records"
                - "memory.md#mem-obj-fixraw"
                - "memory.md#mem-rte-trace-mining"
                - "epistemic.md#epi-rte-fix-retention"
              note: "Accumulated session evidence feeds durable remedy/advisory artifacts; retained raw sightings permit rejudgment."
          records:
            - "memory.md#mem-obj-records"
            - "memory.md#mem-obj-fixraw"
            - "memory.md#mem-rte-trace-mining"
            - "epistemic.md#epi-rte-fix-retention"
          note: "Update force and downstream model evidence are distinct."
        - scope: "Previous continuation content at subsequent capture"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Retained continuation experience shapes the next automatically extracted behavior-guiding packet."
          records:
            - "memory.md#mem-obj-compaction-data"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Recapture reads surviving carry/rules/goal before producing the next durable packet."
        - scope: "Historical text/features and dense vectors at retrieval/rerank consumer"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-records"
                - "memory.md#mem-obj-session-meta"
                - "runtime.md#rt-cmp-embed-client"
                - "runtime.md#rt-rte-embedding-records"
                - "runtime.md#rt-rte-requested-recall"
              note: "Retained text, metadata and numerical representations affect relative retrieval priority."
          records:
            - "memory.md#mem-obj-records"
            - "memory.md#mem-obj-session-meta"
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
            - "runtime.md#rt-rte-requested-recall"
          note: "Fixed scoring can give retained content ranking authority without a learned scoring algorithm."
        - scope: "Judged fixes and lifecycle state at priority/selection consumers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixes"
                - "epistemic.md#epi-obj-lifecycle"
                - "memory.md#mem-obj-notes"
                - "epistemic.md#epi-rte-fix-disposition"
                - "epistemic.md#epi-rte-fix-selection"
              note: "Candidate flags and lifecycle state change historical priority."
          records:
            - "memory.md#mem-obj-fixes"
            - "epistemic.md#epi-obj-lifecycle"
            - "memory.md#mem-obj-notes"
            - "epistemic.md#epi-rte-fix-disposition"
            - "epistemic.md#epi-rte-fix-selection"
          note: "Confirmed-first fallback is consumer-specific; rejected history may be demoted rather than erased."
        - scope: "Session/project IDs, capture fingerprints and delivery ledgers at selectors"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-session-meta"
                - "memory.md#mem-obj-compaction-state"
                - "runtime.md#rt-rte-auto-delivery"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Symbolic metadata selects retained material and delivery/recovery branches."
          records:
            - "memory.md#mem-obj-session-meta"
            - "memory.md#mem-obj-compaction-state"
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "These retained parts choose reader scope, packet revision or repeated-delivery eligibility."
        - scope: "Activation grants, tombstones, failure/delivery tokens at withholding consumers"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-policy"
                - "memory.md#mem-rte-forget-cleanup"
                - "runtime.md#rt-rte-auto-delivery"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Origin grants, suppression and packet-delivery/failure tokens can exclude material from admission or delivery."
          records:
            - "runtime.md#rt-obj-policy"
            - "memory.md#mem-rte-forget-cleanup"
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "The enforced boundary is local admission/output eligibility, not host action permission or universal erasure."
        - scope: "Suppression and capture metadata at write/admission checks"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-rte-forget-cleanup"
                - "memory.md#mem-obj-compaction-state"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Tombstones and stored capture identity/digest/revision determine whether new input is admissible."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-rte-forget-cleanup"
                - "memory.md#mem-obj-compaction-state"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Those checks can veto forgotten, mismatched, duplicate or older captures."
          records:
            - "memory.md#mem-rte-forget-cleanup"
            - "memory.md#mem-obj-compaction-state"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "The checks concern admissibility and identity/freshness, not proposition truth."
        - scope: "Stored judged candidate flags at plan-remedy admission"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixes"
                - "epistemic.md#epi-rte-fix-selection"
                - "epistemic.md#epi-rte-plan-check"
              note: "The retained candidate flag supplies the confirmed-only criterion at the plan remedy consumer."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixes"
                - "epistemic.md#epi-rte-fix-selection"
                - "epistemic.md#epi-rte-plan-check"
              note: "A candidate remedy is withheld by that consumer."
          records:
            - "memory.md#mem-obj-fixes"
            - "epistemic.md#epi-rte-fix-selection"
            - "epistemic.md#epi-rte-plan-check"
          note: "Requested lookup can expose candidates while plan remedy refuses them."
        - scope: "Token-neighbor rescue and incompletely traced command/session-fact/update/usage consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-cooccur"
            - "memory.md#mem-obj-commands"
            - "memory.md#mem-obj-commandfails"
            - "memory.md#mem-obj-sessionfacts"
            - "runtime.md#rt-rte-auto-delivery"
          note: "Objects and some consumer roles are known, but all consequential force paths are not traced; existence of a table does not settle every consumer."
        - scope: "Included specialized stop/deferred/checkpoint hooks, other host integrations and parser/recovery variants"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
          note: "Specialized hooks, other host loaders and opaque provider state leave further authority paths uninspected."
      records:
        - "memory.md#mem-obj-records"
        - "memory.md#mem-obj-fixes"
        - "memory.md#mem-obj-commands"
        - "memory.md#mem-obj-commandfails"
        - "memory.md#mem-obj-sessionfacts"
        - "runtime.md#rt-rte-requested-recall"
        - "runtime.md#rt-bap-recall-reference"
        - "memory.md#mem-obj-compaction-data"
        - "runtime.md#rt-rte-compaction-recovery"
        - "memory.md#mem-rte-convention-delivery"
        - "runtime.md#rt-obj-rules"
        - "runtime.md#rt-rte-rules-sync"
        - "runtime.md#rt-bap-standing-rules"
        - "memory.md#mem-obj-fixraw"
        - "memory.md#mem-rte-trace-mining"
        - "epistemic.md#epi-rte-fix-retention"
        - "memory.md#mem-obj-session-meta"
        - "runtime.md#rt-cmp-embed-client"
        - "runtime.md#rt-rte-embedding-records"
        - "epistemic.md#epi-obj-lifecycle"
        - "memory.md#mem-obj-notes"
        - "epistemic.md#epi-rte-fix-disposition"
        - "epistemic.md#epi-rte-fix-selection"
        - "memory.md#mem-obj-compaction-state"
        - "runtime.md#rt-rte-auto-delivery"
        - "runtime.md#rt-obj-policy"
        - "memory.md#mem-rte-forget-cleanup"
        - "epistemic.md#epi-rte-plan-check"
        - "memory.md#mem-obj-cooccur"
      note: "Knowledge, instruction, learning, ranking, routing, validation and enforcement have distinct retained-part/consumer warrants. Model obedience, improved capacity and all alternative consumer paths are not established."
    write_agency:
      assessment: "partial"
      units:
        - scope: "MCP remember admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-note-admission"
                - "memory.md#mem-obj-notes"
              note: "MCP software admission uses structural/storage checks, not a required operator decision."
          records:
            - "runtime.md#rt-rte-note-admission"
            - "memory.md#mem-obj-notes"
          note: "The live software API admits content without per-content human approval."
        - scope: "CLI remember/promote caller-supplied content and lifecycle choices"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-rte-note-admission"
          note: "A generic CLI caller can be a human or software; human content approval is not established for every invocation."
        - scope: "Default promoted-note distillation after invocation"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-promote-distill"
                - "memory.md#mem-obj-notes"
              note: "Fixed code selects and admits derived session receipts without per-excerpt human approval."
          records:
            - "epistemic.md#epi-rte-promote-distill"
            - "memory.md#mem-obj-notes"
          note: "Starting promotion is not approval of each extracted excerpt."
        - scope: "Index, sidecar, embedding, digest-cache and continuation admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-index-db"
                - "memory.md#mem-rte-trace-mining"
                - "runtime.md#rt-cmp-embed-client"
                - "runtime.md#rt-rte-embedding-records"
                - "runtime.md#rt-rte-auto-delivery"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Derived retained parts are admitted by code/provider output and storage checks, not per-content human decision."
          records:
            - "runtime.md#rt-obj-index-db"
            - "memory.md#mem-rte-trace-mining"
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Software/model derivation and structural filtering own these admissions."
        - scope: "Rules source adoption in the prescribed candidate-review workflow"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
              note: "A user must select which proposed rule lines to append."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
          note: "The skill requires selection of exact lines before append; the API does not enforce this procedure."
        - scope: "Pre-existing rules source and direct source edits outside the prescribed workflow"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
          note: "Who supplied/approved each source line is not established by file possession or sync invocation."
        - scope: "Rules copy distribution"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
              note: "Sync selects ready targets and installs structurally valid copies without a new per-target content decision."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
          note: "The source-adoption decision and subsequent file-copy admission are separate."
        - scope: "Imported-batch local admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-import-records"
              note: "Parser, integrity, suppression and storage code decide record admission."
          records:
            - "runtime.md#rt-rte-import-records"
          note: "Choosing a peer or workflow is not approval of each admitted row."
        - scope: "Recovery write-back and span destination writes"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-recovery"
              note: "Software reconstructs/adopts conversation or recorded-span output under path/existence checks."
          records:
            - "memory.md#mem-rte-session-recovery"
          note: "Invocation/destination control does not require human per-content approval of reconstructed text."
        - scope: "Privacy/lifecycle and activation-policy source decisions"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-forget-cleanup"
            - "memory.md#mem-obj-notes"
            - "runtime.md#rt-obj-policy"
          note: "Generic caller identity leaves whether a human explicitly approved retained suppression/configuration content unresolved."
        - scope: "Included specialized stop/deferred/checkpoint hooks, other host integrations and parser/recovery variants"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Specialized queued/checkpoint writes, host parser alternatives and usage-history admission are not fully inspected."
      records:
        - "runtime.md#rt-rte-note-admission"
        - "memory.md#mem-obj-notes"
        - "epistemic.md#epi-rte-promote-distill"
        - "runtime.md#rt-obj-index-db"
        - "memory.md#mem-rte-trace-mining"
        - "runtime.md#rt-cmp-embed-client"
        - "runtime.md#rt-rte-embedding-records"
        - "runtime.md#rt-rte-auto-delivery"
        - "runtime.md#rt-rte-compaction-recovery"
        - "runtime.md#rt-obj-rules"
        - "runtime.md#rt-rte-rules-sync"
        - "runtime.md#rt-rte-import-records"
        - "memory.md#mem-rte-session-recovery"
        - "memory.md#mem-rte-forget-cleanup"
        - "runtime.md#rt-obj-policy"
      note: "Automatic admissions are wired; manual adoption is prescribed for standing rules and remains claimed. CLI caller identity, direct initialization/edit paths and specialized writes prevent complete agency coverage."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Session-to-promoted-receipt extraction"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-promote-distill"
                - "memory.md#mem-obj-notes"
              note: "Ask/outcome/decision excerpts compress retained session content into a note."
          records:
            - "epistemic.md#epi-rte-promote-distill"
            - "memory.md#mem-obj-notes"
          note: "Excerpting reduces existing session claims; lossy faithfulness does not by itself make a new claim."
        - scope: "Continuation context and carry maintenance"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Selected objective, conclusions, commands, constraints and carry reduce retained session context."
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "New captures replace the stored continuation and can carry forward surviving prior fields."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Finite carry age/count/text and bounded packet retention forget older material."
          records:
            - "memory.md#mem-obj-compaction-data"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Extraction, recapture and retention bounds operate over retained session/previous-packet content."
        - scope: "Compaction inferred command outcome labels"
          assessment: "known"
          findings:
            - value: "synthesize"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-compaction-recovery"
              note: "The packet adds a passed/failed assertion from a detector result; the passing claim is absent from no-detected-friction premises."
          records:
            - "runtime.md#rt-rte-compaction-recovery"
          note: "The accepted epistemic overlay isolates withCommandOutcomes: no detected friction can become passed, which is not entailed by the source evidence."
        - scope: "Raw fix evidence to judged maintained table"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixraw"
                - "memory.md#mem-obj-fixes"
                - "memory.md#mem-rte-trace-mining"
                - "epistemic.md#epi-rte-fix-retention"
                - "epistemic.md#epi-rte-fix-disposition"
              note: "Mined retained error/remedy sequences become bounded advisory tuples."
            - value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixraw"
                - "memory.md#mem-obj-fixes"
                - "memory.md#mem-rte-trace-mining"
                - "epistemic.md#epi-rte-fix-retention"
                - "epistemic.md#epi-rte-fix-disposition"
              note: "Repeated evidence is merged into a deduplicated judged table."
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixraw"
                - "memory.md#mem-obj-fixes"
                - "memory.md#mem-rte-trace-mining"
                - "epistemic.md#epi-rte-fix-retention"
                - "epistemic.md#epi-rte-fix-disposition"
              note: "Changed/new raw sightings cause rejudgment and can revise candidate status."
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixraw"
                - "memory.md#mem-obj-fixes"
                - "memory.md#mem-rte-trace-mining"
                - "epistemic.md#epi-rte-fix-retention"
                - "epistemic.md#epi-rte-fix-disposition"
              note: "Replaced/nonlive session contributions are withdrawn from future judging/serving while original source history may remain."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixraw"
                - "memory.md#mem-obj-fixes"
                - "memory.md#mem-rte-trace-mining"
                - "epistemic.md#epi-rte-fix-retention"
                - "epistemic.md#epi-rte-fix-disposition"
              note: "Separate pair/candidate caps evict older retained tuples."
          records:
            - "memory.md#mem-obj-fixraw"
            - "memory.md#mem-obj-fixes"
            - "memory.md#mem-rte-trace-mining"
            - "epistemic.md#epi-rte-fix-retention"
            - "epistemic.md#epi-rte-fix-disposition"
          note: "Judgment/update and lookup are different operations; candidate fallback remains possible."
        - scope: "Command/failure and session-outcome reduction"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-commands"
                - "memory.md#mem-obj-commandfails"
                - "memory.md#mem-obj-sessionfacts"
              note: "Retained commands/outcomes are reduced to recurrence or bounded session summaries."
          records:
            - "memory.md#mem-obj-commands"
            - "memory.md#mem-obj-commandfails"
            - "memory.md#mem-obj-sessionfacts"
          note: "No exact four-entry session capacity is used; the reconciliation retains a precision limit."
        - scope: "Local notes lifecycle corrections and accepted convention tier"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "epistemic.md#epi-obj-lifecycle"
                - "memory.md#mem-rte-convention-delivery"
              note: "New promotion rows revise the current decision/lifecycle presentation."
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "epistemic.md#epi-obj-lifecycle"
                - "memory.md#mem-rte-convention-delivery"
              note: "Rejected/superseded/stale state withdraws current convention reliance without erasing historical evidence."
            - value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-obj-notes"
                - "epistemic.md#epi-obj-lifecycle"
                - "memory.md#mem-rte-convention-delivery"
              note: "Accepted decisions become standing convention reminders prioritized in startup context."
          records:
            - "memory.md#mem-obj-notes"
            - "epistemic.md#epi-obj-lifecycle"
            - "memory.md#mem-rte-convention-delivery"
          note: "Append corrections preserve history; accepted reminders have elevated startup salience."
        - scope: "Convention rendering"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-convention-delivery"
              note: "A first sentence/shortened decision replaces the full rationale in the reminder."
            - value: "dedup"
              basis: "wired"
              records:
                - "memory.md#mem-rte-convention-delivery"
              note: "Duplicate displayed lines are removed from the startup block."
          records:
            - "memory.md#mem-rte-convention-delivery"
          note: "This classifies implemented reduction and line deduplication, not semantic fidelity."
        - scope: "Local forget/tombstone maintenance"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-forget-cleanup"
              note: "Selected index content and matching secondary retained material are forgotten."
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-forget-cleanup"
              note: "Persistent tombstones withdraw future local admission/reliance even when raw host sources survive."
          records:
            - "memory.md#mem-rte-forget-cleanup"
          note: "Local forgetting is not global/atomic erasure and does not necessarily delete authored note prose."
        - scope: "Rules semantic formulation in the prescribed host workflow"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
              note: "The instructed host selects recurring correction content into concise standing rules."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
          note: "The model is asked to derive recurring standing preferences; no deja internal synthesis call or observed semantic result is established."
        - scope: "Rules source-driven copy replacement/removal"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
              note: "Sync replaces previous marked retained rule blocks with the revised source."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
          note: "Editing/emptying the source drives replacement/removal of bounded copies."
        - scope: "Token-neighbor transformation beyond index rebuild"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-cooccur"
          note: "Token association computation is recorded, but acquisition/index rebuilding alone cannot assign additional controlled curation operations."
        - scope: "Included specialized stop/deferred/checkpoint hooks, other host integrations and parser/recovery variants"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-trace-mining"
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
          note: "Full incremental table repair, specialized queue/checkpoint maintenance, export/SSH withdrawal and opaque provider transformations remain unresolved."
      records:
        - "epistemic.md#epi-rte-promote-distill"
        - "memory.md#mem-obj-notes"
        - "memory.md#mem-obj-compaction-data"
        - "runtime.md#rt-rte-compaction-recovery"
        - "memory.md#mem-obj-fixraw"
        - "memory.md#mem-obj-fixes"
        - "memory.md#mem-rte-trace-mining"
        - "epistemic.md#epi-rte-fix-retention"
        - "epistemic.md#epi-rte-fix-disposition"
        - "memory.md#mem-obj-commands"
        - "memory.md#mem-obj-commandfails"
        - "memory.md#mem-obj-sessionfacts"
        - "epistemic.md#epi-obj-lifecycle"
        - "memory.md#mem-rte-convention-delivery"
        - "memory.md#mem-rte-forget-cleanup"
        - "runtime.md#rt-obj-rules"
        - "runtime.md#rt-rte-rules-sync"
        - "memory.md#mem-obj-cooccur"
        - "runtime.md#rt-rte-auto-delivery"
        - "runtime.md#rt-cmp-embed-client"
        - "runtime.md#rt-rte-embedding-records"
      note: "All seven positive operations retain their local transformations and evidence layer. Rule semantic reduction is claimed; wired extraction does not assure semantic preservation. Rebuild/embedding acquisition alone is not called curation."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Explicit CLI/MCP recall, context and resource requests"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-requested-recall"
              note: "Queries, session prefixes or URIs request retained material returned to the invoking consumer."
          records:
            - "runtime.md#rt-rte-requested-recall"
          note: "The caller requests history; ranking/delivery fulfilling it are not extra push operations."
        - scope: "Explicit handoff, native resume and span recovery"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-session-recovery"
              note: "The caller requests a digest, reopened conversation or recorded span."
          records:
            - "memory.md#mem-rte-session-recovery"
          note: "Explicit/newest-project choice still fulfills a recovery request."
        - scope: "Independent startup/prompt/tool/error/plan and spawned-input supplies"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-auto-delivery"
                - "memory.md#mem-rte-convention-delivery"
                - "runtime.md#rt-rte-spawn-context"
                - "epistemic.md#epi-rte-plan-delivery"
              note: "Automatic selectors add retained history/reminders to foreground or child context."
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "memory.md#mem-rte-convention-delivery"
            - "runtime.md#rt-rte-spawn-context"
            - "epistemic.md#epi-rte-plan-delivery"
          note: "Host events/present task signals are triggers, not requests for retained memory."
        - scope: "Session/workspace continuation recovery on eligible hooks"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-compaction-recovery"
                - "memory.md#mem-obj-compaction-state"
              note: "The next eligible invocation receives the stored recovery packet without an explicit memory request."
          records:
            - "runtime.md#rt-rte-compaction-recovery"
            - "memory.md#mem-obj-compaction-state"
          note: "Automatic hook selection supplies the matching retained capture."
        - scope: "Rule candidate extraction request"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
              note: "The foreground agent requests retained correction evidence with rules candidates."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
          note: "Candidate output is requested; it does not itself update the rules file."
        - scope: "Standing rule copies at later host context assembly"
          assessment: "known"
          findings:
            - value: "push"
              basis: "afforded"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
                - "runtime.md#rt-bap-standing-rules"
              note: "The later host is intended to include the standing rule block without a topical memory request."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
            - "runtime.md#rt-bap-standing-rules"
          note: "The shipped files supply an intended automatic instruction-loader path; actual loading is not observed."
        - scope: "Retained raw fix sightings and previous carry requested by automatic update code"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fixraw"
                - "memory.md#mem-obj-compaction-data"
                - "epistemic.md#epi-rte-fix-retention"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Update/capture code reads accumulated evidence or previous packet fields to compute the next derivative."
          records:
            - "memory.md#mem-obj-fixraw"
            - "memory.md#mem-obj-compaction-data"
            - "epistemic.md#epi-rte-fix-retention"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "This is update-only read-back; ensuing model delivery has its own direction."
        - scope: "Included specialized stop/deferred/checkpoint hooks, other host integrations and parser/recovery variants"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
          note: "Deferred/specialized hook chains and opaque provider retention lack fully assessed request/selection/delivery operations."
      records:
        - "runtime.md#rt-rte-requested-recall"
        - "memory.md#mem-rte-session-recovery"
        - "runtime.md#rt-rte-auto-delivery"
        - "memory.md#mem-rte-convention-delivery"
        - "runtime.md#rt-rte-spawn-context"
        - "epistemic.md#epi-rte-plan-delivery"
        - "runtime.md#rt-rte-compaction-recovery"
        - "memory.md#mem-obj-compaction-state"
        - "runtime.md#rt-obj-rules"
        - "runtime.md#rt-rte-rules-sync"
        - "runtime.md#rt-bap-standing-rules"
        - "memory.md#mem-obj-fixraw"
        - "memory.md#mem-obj-compaction-data"
        - "epistemic.md#epi-rte-fix-retention"
        - "runtime.md#rt-cmp-embed-client"
        - "runtime.md#rt-rte-embedding-records"
      note: "Pull and push both exist. Request fulfillment, automatic event delivery, standing-loader affordance and internal update reads remain separate; specialized alternatives prevent complete route coverage."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Startup digest coarse recency/availability and budget filtering"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-auto-delivery"
              note: "Recency, availability and budget select a broad history block, distinct from targeted task overlap."
          records:
            - "runtime.md#rt-rte-auto-delivery"
          note: "Trigger: startup event. Inputs: recent project history, policy and budget. Selected part: bounded cached/new digest."
        - scope: "Startup project convention identity selection"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-convention-delivery"
              note: "Exact project membership selects delivered retained convention parts; state/count/budget filters remain separate."
          records:
            - "memory.md#mem-rte-convention-delivery"
          note: "Trigger: startup. Input: current allowed project names and latest accepted note state. Selected part: matching local/imported decision lines."
        - scope: "Startup task-file, prompt, file/error and spawn prompt relevance"
          assessment: "known"
          findings:
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-auto-delivery"
                - "runtime.md#rt-rte-spawn-context"
              note: "Task overlap and lexical prompt/file/error relevance select history for unsolicited delivery."
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-spawn-context"
          note: "Triggers: startup/prompt/tool/failure/spawn events. Inputs: changed task files, current terms/path/error or child prompt. Selected part: corresponding prior history."
        - scope: "Automatic plan warning and remedy selection"
          assessment: "known"
          findings:
            - value: "inferred-lexical"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-mining"
                - "epistemic.md#epi-rte-plan-check"
                - "epistemic.md#epi-rte-plan-delivery"
              note: "Term/error matching selects retained wall/remedy evidence; privacy, candidate and budget gates are independent."
          records:
            - "memory.md#mem-rte-trace-mining"
            - "epistemic.md#epi-rte-plan-check"
            - "epistemic.md#epi-rte-plan-delivery"
          note: "Trigger: plan submission. Inputs: extracted plan-step terms/error walls and retained fix flags. Selected part: recurring-wall receipts and eligible remedies."
        - scope: "Continuation native session/workspace match"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-compaction-recovery"
                - "memory.md#mem-obj-compaction-state"
              note: "The identity match selects the specific stored packet for delivery; failure/delivery/freshness gates are separate."
          records:
            - "runtime.md#rt-rte-compaction-recovery"
            - "memory.md#mem-obj-compaction-state"
          note: "Trigger: eligible context/prompt/tool hook. Inputs: native session/workspace and stored capture metadata. Selected part: the matched continuation packet."
        - scope: "Standing whole-rule block in intended host loading"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "afforded"
              records:
                - "runtime.md#rt-obj-rules"
                - "runtime.md#rt-rte-rules-sync"
                - "runtime.md#rt-bap-standing-rules"
              note: "The intended loader includes the standing block broadly, without demonstrated topical or identity-based part selection."
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
            - "runtime.md#rt-bap-standing-rules"
          note: "Trigger: later host instruction assembly. Input: available marked global rules block. Selected part: that standing block, not topical history."
        - scope: "Explicit recall and recovery request fulfillment"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-requested-recall"
            - "memory.md#mem-rte-session-recovery"
          note: "Read-back signal classifies push; query/prefix/URI identifiers on these pull operations do not establish identifier push."
        - scope: "Included specialized stop/deferred/checkpoint hooks, other host integrations and parser/recovery variants"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
          note: "Deferred/checkpoint selectors and other hook implementations are uninspected; semantic pull witnesses cannot classify them."
      records:
        - "runtime.md#rt-rte-auto-delivery"
        - "memory.md#mem-rte-convention-delivery"
        - "runtime.md#rt-rte-spawn-context"
        - "memory.md#mem-rte-trace-mining"
        - "epistemic.md#epi-rte-plan-check"
        - "epistemic.md#epi-rte-plan-delivery"
        - "runtime.md#rt-rte-compaction-recovery"
        - "memory.md#mem-obj-compaction-state"
        - "runtime.md#rt-obj-rules"
        - "runtime.md#rt-rte-rules-sync"
        - "runtime.md#rt-bap-standing-rules"
        - "runtime.md#rt-rte-requested-recall"
        - "memory.md#mem-rte-session-recovery"
        - "runtime.md#rt-cmp-embed-client"
        - "runtime.md#rt-rte-embedding-records"
      note: "Coarse, identifier and inferred-lexical push signals are established at distinct selectors. Dense rerank is recorded on requested recall, not sufficient evidence for inferred-embedding push. No model-judgment push selector is established; this is not bounded absence."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic error/remedy extraction, judging and later consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-mining"
                - "memory.md#mem-obj-fixraw"
                - "memory.md#mem-obj-fixes"
                - "epistemic.md#epi-rte-fix-retention"
                - "epistemic.md#epi-rte-fix-selection"
              note: "Automatic trace-fed writes produce retained raw/judged fixes consumed by future judging and remedy selection."
          records:
            - "memory.md#mem-rte-trace-mining"
            - "memory.md#mem-obj-fixraw"
            - "memory.md#mem-obj-fixes"
            - "epistemic.md#epi-rte-fix-retention"
            - "epistemic.md#epi-rte-fix-selection"
          note: "Recorded command/error/edit experience feeds durable selector/advisory state used by later requests/events."
        - scope: "Automatic continuation extraction/recapture and later host delivery"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Session traces automatically produce durable context/guidance reloaded for a later model invocation."
          records:
            - "memory.md#mem-obj-compaction-data"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Within-session later invocation is sufficient; faithful semantics, new knowledge and demonstrated benefit are not required."
        - scope: "Recurring command/failure derivative routes with stated later consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-obj-commands"
                - "memory.md#mem-obj-commandfails"
                - "memory.md#mem-rte-trace-mining"
              note: "Transcript commands/outcomes automatically produce durable later practice/advisory artifacts."
          records:
            - "memory.md#mem-obj-commands"
            - "memory.md#mem-obj-commandfails"
            - "memory.md#mem-rte-trace-mining"
          note: "Consumers include fixed lookup and per-action warning; exact all-caller behavior remains limited."
        - scope: "Token-neighbor rescue and session-fact derivative routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-cooccur"
            - "memory.md#mem-obj-sessionfacts"
          note: "Automatic trace derivation is recorded, but full later selector/rendering paths remain uninspected; this prevents a complete qualifying-route assessment."
        - scope: "Rules source formation and out-of-workflow updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
          note: "The prescribed human approval route does not establish qualifying automatic source formation; direct source provenance/control is unresolved. Copying approved text does not by itself close an automatic trace-fed write chain."
        - scope: "Opaque embedding-provider learning/retention"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
          note: "The client requests embeddings, not training; provider parameters and retained experience are uninspected. No local no is licensed for provider internals."
        - scope: "Included specialized stop/deferred/checkpoint hooks, other host integrations and parser/recovery variants"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Specialized hook/checkpoint writes, variant host summaries and adaptive usage/evaluator consumers prevent a bounded complete negative or full qualifying-route enumeration."
      records:
        - "memory.md#mem-rte-trace-mining"
        - "memory.md#mem-obj-fixraw"
        - "memory.md#mem-obj-fixes"
        - "epistemic.md#epi-rte-fix-retention"
        - "epistemic.md#epi-rte-fix-selection"
        - "memory.md#mem-obj-compaction-data"
        - "runtime.md#rt-rte-compaction-recovery"
        - "memory.md#mem-obj-commands"
        - "memory.md#mem-obj-commandfails"
        - "memory.md#mem-obj-cooccur"
        - "memory.md#mem-obj-sessionfacts"
        - "runtime.md#rt-obj-rules"
        - "runtime.md#rt-rte-rules-sync"
        - "runtime.md#rt-cmp-embed-client"
        - "runtime.md#rt-rte-embedding-records"
        - "runtime.md#rt-rte-auto-delivery"
      note: "Wired yes findings describe automatic trace-fed durable behavior-shaping artifacts, not demonstrated improved capacity. No bounded absence record licenses a local or system-wide no; unresolved routes are retained."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Fix-mining original recorded session message content"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-mining"
                - "epistemic.md#epi-rte-fix-check"
                - "epistemic.md#epi-rte-fix-retention"
              note: "Recorded agent-session turns supply the message corpus used to mine associations."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-rte-trace-mining"
                - "epistemic.md#epi-rte-fix-check"
                - "epistemic.md#epi-rte-fix-retention"
              note: "Recorded command requests/results and edit/error observations supply remedy evidence."
          records:
            - "memory.md#mem-rte-trace-mining"
            - "epistemic.md#epi-rte-fix-check"
            - "epistemic.md#epi-rte-fix-retention"
          note: "Qualifying write: automatic mining/judgment. Original conversational and command/output/edit activity remains distinct from the intermediate normalized corpus."
        - scope: "Continuation original transcript content including recognized host summary forms"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Recorded conversational turns and summaries supply goals, constraints, conclusions and carry."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-data"
                - "runtime.md#rt-rte-compaction-recovery"
              note: "Recorded commands/results and outcomes supply test/receipt material in the packet."
          records:
            - "memory.md#mem-obj-compaction-data"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Qualifying write: automatic continuation capture. Previous carry/rules may be recaptured; full variant parser fidelity is unresolved."
        - scope: "Recurring command practice and failure original content"
          assessment: "known"
          findings:
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-commands"
                - "memory.md#mem-obj-commandfails"
                - "memory.md#mem-rte-trace-mining"
              note: "Recorded command executions and failure outputs supply the retained practice/warning tables."
          records:
            - "memory.md#mem-obj-commands"
            - "memory.md#mem-obj-commandfails"
            - "memory.md#mem-rte-trace-mining"
          note: "Qualifying write: automatic transcript-to-command/failure derivative admission."
        - scope: "Unresolved token-neighbor/session-fact qualifying chains"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-cooccur"
            - "memory.md#mem-obj-sessionfacts"
          note: "Some trace origins are known, but qualifying downstream-route coverage remains unresolved on the trace_learning axis; no complete source assessment follows."
        - scope: "Unresolved standing-rule source provenance and opaque provider update inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-rules"
            - "runtime.md#rt-rte-rules-sync"
            - "runtime.md#rt-cmp-embed-client"
            - "runtime.md#rt-rte-embedding-records"
          note: "Rules may use corrections under a prescribed manual route, while provider internals are opaque; neither establishes a fully classified automatic trace-fed write here."
        - scope: "Included specialized stop/deferred/checkpoint hooks, other host integrations and parser/recovery variants"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-auto-delivery"
            - "runtime.md#rt-rte-compaction-recovery"
          note: "Specialized queued/checkpoint and variant-summary write inputs remain uninspected. Host hook callbacks are triggers, not automatically the content of the qualifying write."
      records:
        - "memory.md#mem-rte-trace-mining"
        - "epistemic.md#epi-rte-fix-check"
        - "epistemic.md#epi-rte-fix-retention"
        - "memory.md#mem-obj-compaction-data"
        - "runtime.md#rt-rte-compaction-recovery"
        - "memory.md#mem-obj-commands"
        - "memory.md#mem-obj-commandfails"
        - "memory.md#mem-obj-cooccur"
        - "memory.md#mem-obj-sessionfacts"
        - "runtime.md#rt-obj-rules"
        - "runtime.md#rt-rte-rules-sync"
        - "runtime.md#rt-cmp-embed-client"
        - "runtime.md#rt-rte-embedding-records"
        - "runtime.md#rt-rte-auto-delivery"
      note: "Session-logs and tool-traces are supported on the named qualifying writes. Hooks do not add event-streams merely by triggering capture; temporal error/remedy pairing does not itself establish linked state-action-outcome trajectories. Mixed/opaque alternatives prevent complete source coverage."
---

# deja-vu memory profile

## Comparison rationale

The comparison inventories memory accumulated or revised through use, not all runtime files. Local binary/gob indexes and dense sidecar files establish filesystem storage. Dense encoding separately establishes parametric form; it does not establish a vector database or mutable model weights. The provider's exact state and retention remain uninspected ([RT-CMP-embed-client](runtime.md#rt-cmp-embed-client), [RT-RTE-embedding-records](runtime.md#rt-rte-embedding-records)). Every axis remains partial because material alternatives or initial provenance/control remain unresolved in the accepted accounts. This is coverage uncertainty, not a downgrade of wired local witnesses.

Canonical fix objects are [MEM-OBJ-fixraw](memory.md#mem-obj-fixraw) and [MEM-OBJ-fixes](memory.md#mem-obj-fixes), replacing the epistemic duplicate declarations. Canonical convention selection is [MEM-RTE-convention-delivery](memory.md#mem-rte-convention-delivery), replacing the epistemic duplicate route. These supersessions affect storage, form, lineage, authority, curation and read-back citations. They preserve the epistemic consumer-specific checks and first-sentence scope-loss finding; they do not supersede the index container or the distinct check/disposition/retention routes. The exact session-fact capacity is not used: the reconciliation retains a precision limit while command/outcome distinctions remain usable ([MEM-OBJ-sessionfacts](memory.md#mem-obj-sessionfacts)).

Trace learning here means automatic trace-fed production of durable behavior-shaping artifacts and a later consumer. Fixed fix mining and continuation extraction meet that architectural test without model training, a new explanatory claim or observed improvement. Raw recorded traces alone do not. Retained raw sightings have learning authority at the rejudgment consumer, while served remedies have knowledge and ranking force; flags can additionally validate/veto the plan-remedy branch. A requested lookup may return labelled unconfirmed candidates, so the plan gate must not become a system-wide never-served assertion ([MEM-RTE-trace-mining](memory.md#mem-rte-trace-mining), [EPI-RTE-fix-disposition](epistemic.md#epi-rte-fix-disposition), [EPI-RTE-fix-selection](epistemic.md#epi-rte-fix-selection), [EPI-RTE-fix-retention](epistemic.md#epi-rte-fix-retention)).

Extracting standing facts or carry from retained sessions is consolidation even when extraction loses a qualification. It is not synthesis merely because fidelity is uncertain. The separate compaction outcome-label edge does add an assertion: the accepted epistemic recovery overlay identifies a `passed` label inferred from no detected friction, compatible with an undetected failure. That local synthesis finding is neither a truth warrant nor a blanket classification of the entire packet ([RT-RTE-compaction-recovery](runtime.md#rt-rte-compaction-recovery), [MEM-OBJ-compaction-data](memory.md#mem-obj-compaction-data)). Lifecycle changes revise current state and withdraw convention reliance without erasing history; accepted convention delivery raises salience, while forgetting and retention caps have distinct local decay effects ([MEM-OBJ-notes](memory.md#mem-obj-notes), [MEM-RTE-forget-cleanup](memory.md#mem-rte-forget-cleanup)).

Standing-rule adoption and copying have different agency and evidence. The skill prescribes human selection before append, so manual agency and semantic consolidation on that path are claimed. Software distribution is wired and automatic. The intended later instruction-loader consumer is afforded, not observed; structural copy/status checks cannot prove loading or obedience. Direct edits and initial rule content remain unresolved. The workflow annotation sharpens those limits without declaring another route ([RT-RTE-rules-sync](runtime.md#rt-rte-rules-sync), [RT-BAP-standing-rules](runtime.md#rt-bap-standing-rules)). Imperative conventions and carried constraints retain their requested instruction force even when framed as untrusted history; effective priority/compliance is not asserted ([RT-BAP-recall-reference](runtime.md#rt-bap-recall-reference)).

Explicit queries, URI/prefix reads and requested restoration are pull. Event-driven startup, prompt/tool/plan/spawn and continuation supply are push. Identifier push requires a real project or session/workspace match selecting delivered parts; an identifier on requested history alone is insufficient. Coarse recency/budget selection is kept apart from lexical targeting. Dense similarity on requested recall does not establish embedding-driven push. Rule loader inclusion is a separate coarse push affordance. A requested update-code read of old sightings/carry is not another model-facing push ([RT-RTE-requested-recall](runtime.md#rt-rte-requested-recall), [RT-RTE-auto-delivery](runtime.md#rt-rte-auto-delivery), [RT-RTE-spawn-context](runtime.md#rt-rte-spawn-context), [MEM-RTE-session-recovery](memory.md#mem-rte-session-recovery)).

Session turns and recorded tool requests/results are the supported original trace inputs. Triggering hooks do not turn their payload into event-stream learning sources; error/remedy sequence mining is not sufficient evidence of linked state-action-outcome trajectories. Opaque provider inputs, specialized queued/checkpoint forms and incompletely traced sidecar/usage consumers remain explicit unresolved units, not absence or inapplicability. No accepted bounded absence record supports a local trace-learning `no`. No execution or causal support is claimed.

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no target source was read and no new evidence or records were added.
