---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "RepoCodex memory comparison: repository explanations, access metadata, deterministic maintenance and trace-fed draft production at the frozen revision."
run-id: "AAS-2026-11-08-repocodex-bf22ac3623d8-01"
source-identity: "https://github.com/azaylamba/repocodex"
reviewed-boundary: "96978e292fcb3b100f53ac024b353e1b8b2c8af4"
memory-comparison:
  version: 2
  scope: "Included: accumulated concept explanations/frontmatter in .context shards; bootstrap drafts and their repository-history input; catalogs, write logs, persisted reverse indexes and metrics; command-mediated and direct/repair write alternatives; later context, identity, checking, impact, screening and diagnostic consumers. Excluded: static shipped skills/rules/hooks/config as accumulated memory, external host/provider retention and parameters, and actual consuming deployments. Known local stores do not resolve arbitrary initial provenance or opaque repair outputs."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Concept bodies and frontmatter, copied bootstrap drafts, catalogs, write logs and persisted reverse indexes"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-concept-body"
                - "runtime.md#rt-obj-concept-frontmatter"
                - "epistemic.md#epi-obj-bootstrap-body"
                - "memory.md#mem-obj-context-catalog"
                - "memory.md#mem-obj-context-log"
                - "memory.md#mem-obj-reverse-index"
              note: "Markdown files in discovered repository shards and generated index paths are the operative local stores."
          records:
            - "runtime.md#rt-obj-concept-body"
            - "runtime.md#rt-obj-concept-frontmatter"
            - "epistemic.md#epi-obj-bootstrap-body"
            - "memory.md#mem-obj-context-catalog"
            - "memory.md#mem-obj-context-log"
            - "memory.md#mem-obj-reverse-index"
          note: "The accepted inventory identifies readable filesystem persistence, with no included opaque memory service."
        -
          scope: "Diagnostic metrics sink"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-metrics"
              note: "Timestamped JSONL is appended to a configurable filesystem path; the default ignored sink is not necessarily Git-versioned."
          records:
            - "memory.md#mem-obj-metrics"
            - "memory.md#mem-rte-metric-readback"
          note: "Both retention and the later diagnostic reader are recorded."
        -
          scope: "Bootstrap's retained commit-history input"
          assessment: "known"
          findings:
            -
              value: "repo"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bootstrap-drafts"
                - "epistemic.md#epi-rte-bootstrap-import"
              note: "Git history supplies the last 100 subjects and file-touch commit references to draft extraction."
          records:
            - "runtime.md#rt-rte-bootstrap-drafts"
            - "epistemic.md#epi-rte-bootstrap-import"
          note: "This is repository history, not a vector or model-parameter store."
      records:
        - "runtime.md#rt-obj-concept-body"
        - "runtime.md#rt-obj-concept-frontmatter"
        - "epistemic.md#epi-obj-bootstrap-body"
        - "memory.md#mem-obj-context-catalog"
        - "memory.md#mem-obj-context-log"
        - "memory.md#mem-obj-reverse-index"
        - "memory.md#mem-obj-metrics"
        - "memory.md#mem-rte-metric-readback"
        - "runtime.md#rt-rte-bootstrap-drafts"
        - "epistemic.md#epi-rte-bootstrap-import"
      note: "The inventory covers local semantic memory, access metadata, operation history, diagnostics and the history input to bootstrap. Static installed instructions and external provider stores are excluded."
    representational_form:
      assessment: "known"
      units:
        -
          scope: "Concept explanations, copied bootstrap notes and descriptive catalog/write-log text at interpretive consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-concept-body"
                - "epistemic.md#epi-obj-bootstrap-body"
                - "memory.md#mem-obj-context-catalog"
                - "memory.md#mem-obj-context-log"
              note: "Explanation bodies and descriptive/event prose are interpreted by agents or readers rather than executed as fixed rules."
          records:
            - "runtime.md#rt-obj-concept-body"
            - "epistemic.md#epi-obj-bootstrap-body"
            - "memory.md#mem-obj-context-catalog"
            - "memory.md#mem-obj-context-log"
            - "runtime.md#rt-bap-memory-consumption"
          note: "Wiring establishes availability to later readers, not comprehension or compliance."
        -
          scope: "Concept keys, paths, literals, statuses, body-link targets and catalog link targets at fixed-rule consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-concept-frontmatter"
                - "runtime.md#rt-obj-concept-body"
                - "memory.md#mem-obj-context-catalog"
                - "epistemic.md#epi-rte-impact-read"
                - "epistemic.md#epi-rte-audit-gc"
              note: "Parsed fields and extracted link identities control selection, impact, checking and retirement; their operative meaning is rule-defined."
          records:
            - "runtime.md#rt-obj-concept-frontmatter"
            - "runtime.md#rt-obj-concept-body"
            - "memory.md#mem-obj-context-catalog"
            - "epistemic.md#epi-rte-impact-read"
            - "epistemic.md#epi-rte-audit-gc"
          note: "Body prose and body links have distinct consumption paths even in one file."
        -
          scope: "Generated reverse mappings and diagnostic event fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-reverse-index"
                - "memory.md#mem-obj-metrics"
                - "memory.md#mem-rte-metric-readback"
              note: "Path/identity mappings and JSONL fields are consumed through fixed comparisons and arithmetic."
          records:
            - "memory.md#mem-obj-reverse-index"
            - "memory.md#mem-obj-metrics"
            - "memory.md#mem-rte-metric-readback"
          note: "Numerical diagnostics are localized values, not distributed parameters."
        -
          scope: "Commit records at bootstrap selection"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bootstrap-drafts"
                - "epistemic.md#epi-rte-bootstrap-import"
              note: "The subject note supplies copied explanatory prose."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bootstrap-drafts"
                - "epistemic.md#epi-rte-bootstrap-import"
              note: "Commit identities and changed paths supply source pointers and addressing."
          records:
            - "runtime.md#rt-rte-bootstrap-drafts"
            - "epistemic.md#epi-rte-bootstrap-import"
          note: "The mixed history input is split by consumed part. External model weights are not retained RepoCodex memory."
      records:
        - "runtime.md#rt-obj-concept-body"
        - "epistemic.md#epi-obj-bootstrap-body"
        - "memory.md#mem-obj-context-catalog"
        - "memory.md#mem-obj-context-log"
        - "runtime.md#rt-bap-memory-consumption"
        - "runtime.md#rt-obj-concept-frontmatter"
        - "epistemic.md#epi-rte-impact-read"
        - "epistemic.md#epi-rte-audit-gc"
        - "memory.md#mem-obj-reverse-index"
        - "memory.md#mem-obj-metrics"
        - "memory.md#mem-rte-metric-readback"
        - "runtime.md#rt-rte-bootstrap-drafts"
        - "epistemic.md#epi-rte-bootstrap-import"
      note: "All included encodings and their consumers are accounted for; natural-language and symbolic material coexist without implying a parametric memory store."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Bootstrap-derived note bodies"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-bootstrap-body"
                - "epistemic.md#epi-rte-bootstrap-import"
              note: "Existing repository comments/doc text or commit subjects are copied with a wrapper; the system does not originate their explanation."
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bootstrap-drafts"
                - "epistemic.md#epi-rte-bootstrap-import"
              note: "Within the copied-note subset, history subjects are extracted from recorded repository change activity into durable drafts; comment/document imports alone do not establish this lineage."
          records:
            - "epistemic.md#epi-obj-bootstrap-body"
            - "epistemic.md#epi-rte-bootstrap-import"
          note: "The import path is known even though source truth and original authorship are not authenticated."
        -
          scope: "Agent-authored concept proposals under the coding skill"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-coding-loop"
                - "runtime.md#rt-rte-memory-write"
              note: "The shipped procedure asks the foreground agent to formulate or revise explanations and submit Markdown; actual authorship instances are unobserved."
          records:
            - "runtime.md#rt-rte-coding-loop"
            - "runtime.md#rt-rte-memory-write"
          note: "The authoring route is available; this does not classify every pre-existing page as agent-authored."
        -
          scope: "Generated catalogs, reverse indexes, write logs, metrics and modified anchor/status metadata"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-context-catalog"
                - "memory.md#mem-obj-reverse-index"
                - "memory.md#mem-obj-context-log"
                - "memory.md#mem-obj-metrics"
                - "runtime.md#rt-rte-anchor-patch"
                - "epistemic.md#epi-rte-audit-gc"
              note: "Deterministic code derives navigation, event and maintenance state from retained concepts or command activity."
          records:
            - "memory.md#mem-obj-context-catalog"
            - "memory.md#mem-obj-reverse-index"
            - "memory.md#mem-obj-context-log"
            - "memory.md#mem-obj-metrics"
            - "runtime.md#rt-rte-anchor-patch"
            - "epistemic.md#epi-rte-audit-gc"
          note: "These are software-derived parts, not model-authored explanations or extracted session summaries."
        -
          scope: "Initial arbitrary concepts and original imported-note authorship"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-concept-body"
            - "runtime.md#rt-obj-concept-frontmatter"
            - "epistemic.md#epi-rte-bootstrap-import"
          note: "Caller-supplied stamps and latest-touch commit pointers do not establish initial authorship or a complete provenance chain."
        -
          scope: "Repair-harness semantic outputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-repair"
          note: "A static repair request and process outcome do not reveal what content the external agent produced or its derivation."
      records:
        - "epistemic.md#epi-obj-bootstrap-body"
        - "epistemic.md#epi-rte-bootstrap-import"
        - "runtime.md#rt-rte-coding-loop"
        - "runtime.md#rt-rte-memory-write"
        - "memory.md#mem-obj-context-catalog"
        - "memory.md#mem-obj-reverse-index"
        - "memory.md#mem-obj-context-log"
        - "memory.md#mem-obj-metrics"
        - "runtime.md#rt-rte-anchor-patch"
        - "epistemic.md#epi-rte-audit-gc"
        - "runtime.md#rt-obj-concept-body"
        - "runtime.md#rt-obj-concept-frontmatter"
        - "runtime.md#rt-rte-agent-repair"
      note: "Known import, history-trace extraction, authoring and deterministic derivation coexist with unresolved initial provenance and repair outputs. Copying static comments is not by itself trace extraction."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Concept bodies, source pointers and navigation descriptions delivered to coding/read/audit consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-concept-body"
                - "runtime.md#rt-bap-memory-consumption"
                - "runtime.md#rt-rte-context-read"
                - "memory.md#mem-rte-concept-read"
                - "memory.md#mem-obj-context-catalog"
                - "runtime.md#rt-rte-review-audit"
              note: "Retained explanations and descriptions supply reference context through JSON or screening payloads; delivery does not prove changed decisions."
          records:
            - "runtime.md#rt-obj-concept-body"
            - "runtime.md#rt-bap-memory-consumption"
            - "runtime.md#rt-rte-context-read"
            - "memory.md#mem-rte-concept-read"
            - "memory.md#mem-obj-context-catalog"
            - "runtime.md#rt-rte-review-audit"
          note: "This classifies the established explanatory consumer, not all possible meanings in arbitrary prose."
        -
          scope: "Retained sources/verified/status fields at retrieval ranking"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-concept-frontmatter"
                - "memory.md#mem-clm-context-selection"
              note: "Presence of sources, stable status and verified metadata changes relative order without authenticating truth."
          records:
            - "runtime.md#rt-obj-concept-frontmatter"
            - "memory.md#mem-clm-context-selection"
          note: "Fixed ranking code can consume retained ranking inputs without a learned ranker."
        -
          scope: "Pins, statuses, concept/body links and catalog link targets at selectors"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-concept-frontmatter"
                - "memory.md#mem-obj-context-catalog"
                - "runtime.md#rt-rte-context-read"
                - "epistemic.md#epi-rte-impact-read"
                - "epistemic.md#epi-rte-audit-gc"
              note: "Retained identities, paths and links select concept bodies, related identities and maintenance targets."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-concept-frontmatter"
                - "runtime.md#rt-rte-context-read"
                - "epistemic.md#epi-rte-audit-gc"
              note: "Deprecated status excludes full bodies from ordinary path retrieval; draft status excludes them by default, not from direct reads."
          records:
            - "runtime.md#rt-obj-concept-frontmatter"
            - "memory.md#mem-obj-context-catalog"
            - "runtime.md#rt-rte-context-read"
            - "epistemic.md#epi-rte-impact-read"
            - "epistemic.md#epi-rte-audit-gc"
            - "memory.md#mem-rte-concept-read"
          note: "Selection and selective denial are consumer-specific; deprecation is not universal access withdrawal."
        -
          scope: "Retained anchors/claims and committed reverse indexes at validation and configured check consumers"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-concept-frontmatter"
                - "memory.md#mem-obj-reverse-index"
                - "runtime.md#rt-rte-validate-change"
                - "epistemic.md#epi-rte-claim-check"
              note: "Stored literals, anchors and expected index material supply criteria for current conformance checks."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-concept-frontmatter"
                - "memory.md#mem-obj-reverse-index"
                - "runtime.md#rt-rte-validate-change"
              note: "A defect in retained criteria or index synchronization can contribute to configured hook/check denial, qualified by posture and exemption."
          records:
            - "runtime.md#rt-obj-concept-frontmatter"
            - "memory.md#mem-obj-reverse-index"
            - "runtime.md#rt-rte-validate-change"
            - "epistemic.md#epi-rte-claim-check"
          note: "The enforced domain is mechanical attachment/maintenance, not semantic truth."
        -
          scope: "Retained commit-history notes at automatic bootstrap update"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bootstrap-drafts"
                - "epistemic.md#epi-rte-bootstrap-import"
              note: "Recorded change subjects feed automatic production of durable draft explanations that later draft-enabled or direct consumers can receive."
          records:
            - "runtime.md#rt-rte-bootstrap-drafts"
            - "epistemic.md#epi-rte-bootstrap-import"
            - "memory.md#mem-rte-concept-read"
          note: "Learning authority is at the update consumer; the resulting body's downstream authority is knowledge. No improvement is demonstrated."
        -
          scope: "Metrics at later validation's diagnostic consumer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-metrics"
                - "memory.md#mem-rte-metric-readback"
              note: "Retained events supply diagnostic evidence for a returned ratio; no policy revision follows in the inspected reader."
          records:
            - "memory.md#mem-obj-metrics"
            - "memory.md#mem-rte-metric-readback"
          note: "The ratio is informational, not an enforced adaptive policy."
        -
          scope: "Write-log prose without a specified automatic consumer"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-obj-context-log"
          note: "The log has a documented readable surface but no established automatic selection/update effect. Storage alone supplies no such authority."
        -
          scope: "Additional standing directions or other effects of arbitrary initial and repair-authored prose"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-concept-body"
            - "runtime.md#rt-rte-agent-repair"
          note: "No concrete initial/repair payload or actual consumer path establishes whether such prose supplies standing instruction or other authority beyond the recorded explanatory channel."
      records:
        - "runtime.md#rt-obj-concept-body"
        - "runtime.md#rt-bap-memory-consumption"
        - "runtime.md#rt-rte-context-read"
        - "memory.md#mem-rte-concept-read"
        - "memory.md#mem-obj-context-catalog"
        - "runtime.md#rt-rte-review-audit"
        - "runtime.md#rt-obj-concept-frontmatter"
        - "memory.md#mem-clm-context-selection"
        - "epistemic.md#epi-rte-impact-read"
        - "epistemic.md#epi-rte-audit-gc"
        - "memory.md#mem-obj-reverse-index"
        - "runtime.md#rt-rte-validate-change"
        - "epistemic.md#epi-rte-claim-check"
        - "runtime.md#rt-rte-bootstrap-drafts"
        - "epistemic.md#epi-rte-bootstrap-import"
        - "memory.md#mem-obj-metrics"
        - "memory.md#mem-rte-metric-readback"
        - "memory.md#mem-obj-context-log"
        - "runtime.md#rt-rte-agent-repair"
      note: "The established explanatory, ranking, routing, checking, denial and trace-fed update paths are retained separately. Unknown arbitrary prose and repair payloads prevent a complete inventory of their semantic forces; static shipped skills are not accumulated memory."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Command admission of caller Markdown, supersession, reanchor patches and identity relocation"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-memory-write"
                - "runtime.md#rt-rte-anchor-patch"
                - "runtime.md#rt-rte-relocate-identity"
              note: "Software admits or rejects supplied changes without an explicit per-content human approval requirement; caller initiation is not approval of each retained change."
          records:
            - "runtime.md#rt-rte-memory-write"
            - "runtime.md#rt-rte-anchor-patch"
            - "runtime.md#rt-rte-relocate-identity"
          note: "Authorship and physical serialization are separate from this admission mechanism."
        -
          scope: "Bootstrap candidates, GC retirement and derived metadata/event writes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bootstrap-drafts"
                - "epistemic.md#epi-rte-audit-gc"
                - "memory.md#mem-obj-context-catalog"
                - "memory.md#mem-obj-reverse-index"
                - "memory.md#mem-obj-context-log"
                - "memory.md#mem-obj-metrics"
              note: "Code selects/adopts drafts, writes retirement status and maintains metadata/events without per-item human decisions."
          records:
            - "runtime.md#rt-rte-bootstrap-drafts"
            - "epistemic.md#epi-rte-audit-gc"
            - "memory.md#mem-obj-context-catalog"
            - "memory.md#mem-obj-reverse-index"
            - "memory.md#mem-obj-context-log"
            - "memory.md#mem-obj-metrics"
          note: "Explicitly starting bootstrap/audit does not make individual admissions manual."
        -
          scope: "Initial imports, direct filesystem edits and actual repair-harness changes"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-concept-body"
            - "runtime.md#rt-rte-memory-write"
            - "runtime.md#rt-rte-agent-repair"
          note: "Generic caller identity and external agent/host approval policy do not establish per-content human control. The records allow these alternatives without resolving their admission decisions."
      records:
        - "runtime.md#rt-rte-memory-write"
        - "runtime.md#rt-rte-anchor-patch"
        - "runtime.md#rt-rte-relocate-identity"
        - "runtime.md#rt-rte-bootstrap-drafts"
        - "epistemic.md#epi-rte-audit-gc"
        - "memory.md#mem-obj-context-catalog"
        - "memory.md#mem-obj-reverse-index"
        - "memory.md#mem-obj-context-log"
        - "memory.md#mem-obj-metrics"
        - "runtime.md#rt-obj-concept-body"
        - "runtime.md#rt-rte-agent-repair"
      note: "Software admission is supported for the inspected command routes. No manual finding is inferred solely from a human initiating a task or choosing a command; external/direct admission remains unresolved."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Anchor path/term maintenance and admitted concept revisions"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-anchor-patch"
                - "runtime.md#rt-rte-memory-write"
              note: "Patch application changes an existing anchor's path/terms; the ordinary write route admits eligible concept revisions."
          records:
            - "runtime.md#rt-rte-anchor-patch"
            - "runtime.md#rt-rte-memory-write"
          note: "No semantic novelty or faithfulness is implied by the existence of a revision route."
        -
          scope: "Supersession and GC retirement with retained history"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-memory-write"
                - "epistemic.md#epi-rte-audit-gc"
              note: "Predecessor or retired concept status becomes deprecated while the file/history remains; default body retrieval withholds reliance."
          records:
            - "runtime.md#rt-rte-memory-write"
            - "epistemic.md#epi-rte-audit-gc"
            - "memory.md#mem-rte-concept-read"
          note: "Direct reads can still expose retired bodies. Supersession can invalidate before replacement rejection."
        -
          scope: "Draft-to-stable write normalization"
          assessment: "known"
          findings:
            -
              value: "promote"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-memory-write"
              note: "The recorded ordinary write route promotes a draft lacking stale_after to stable, changing its default retrieval eligibility."
          records:
            - "runtime.md#rt-rte-memory-write"
            - "runtime.md#rt-rte-context-read"
          note: "This is lifecycle-tier promotion, not semantic endorsement."
        -
          scope: "Unobserved semantic transformation by foreground/repair agents"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-coding-loop"
            - "runtime.md#rt-rte-agent-repair"
          note: "Requests to write or repair do not establish whether actual retained content was consolidated, synthesized, deduplicated or otherwise transformed."
      records:
        - "runtime.md#rt-rte-anchor-patch"
        - "runtime.md#rt-rte-memory-write"
        - "epistemic.md#epi-rte-audit-gc"
        - "memory.md#mem-rte-concept-read"
        - "runtime.md#rt-rte-context-read"
        - "runtime.md#rt-rte-coding-loop"
        - "runtime.md#rt-rte-agent-repair"
      note: "Known evolution, invalidation and promotion are supported. Bootstrap acquisition/copying, stable-ID collision avoidance, reverse-index rebuilding and byte-preserving identity moves do not alone establish consolidation, synthesis or deduplication. Unobserved agent transformations prevent a complete operation inventory."
    read_back_direction:
      assessment: "known"
      units:
        -
          scope: "Path-requested context and direct identity read"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-read"
                - "memory.md#mem-rte-concept-read"
                - "memory.md#mem-clm-context-selection"
              note: "The foreground consumer requests paths or an identity; deterministic selection and return fulfill that request, rather than constituting an unsolicited push."
          records:
            - "runtime.md#rt-rte-context-read"
            - "memory.md#mem-rte-concept-read"
            - "memory.md#mem-clm-context-selection"
          note: "Related/catalog titles are part of the requested return; subsequent body expansion is another consumer request."
        -
          scope: "Validation, MCP impact and audit screening/GC consumers"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-validate-change"
                - "epistemic.md#epi-rte-impact-read"
                - "runtime.md#rt-rte-review-audit"
                - "epistemic.md#epi-rte-audit-gc"
                - "memory.md#mem-obj-reverse-index"
              note: "Explicit command/tool invocations load retained concepts, links, statuses and index copies for their requested checks or screening."
          records:
            - "runtime.md#rt-rte-validate-change"
            - "epistemic.md#epi-rte-impact-read"
            - "runtime.md#rt-rte-review-audit"
            - "epistemic.md#epi-rte-audit-gc"
            - "memory.md#mem-obj-reverse-index"
          note: "Internal selection during a requested computation is not independently unsolicited injection."
        -
          scope: "Metrics diagnostic read-back"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-metric-readback"
              note: "A later explicitly invoked validation reads persisted events for its diagnostic calculation."
          records:
            - "memory.md#mem-rte-metric-readback"
            - "memory.md#mem-obj-metrics"
          note: "Automatic event recording is a write, not push delivery."
        -
          scope: "Documented file-reader access to catalogs, concepts and operation logs"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-context-catalog"
                - "memory.md#mem-obj-context-log"
                - "memory.md#mem-rte-concept-read"
              note: "The documented bundle layout permits readers to open retained material; no deployed human/agent file read is evidenced."
          records:
            - "memory.md#mem-obj-context-catalog"
            - "memory.md#mem-obj-context-log"
            - "memory.md#mem-rte-concept-read"
          note: "Afforded file reads are not upgraded to observed or wired use."
      records:
        - "runtime.md#rt-rte-context-read"
        - "memory.md#mem-rte-concept-read"
        - "memory.md#mem-clm-context-selection"
        - "runtime.md#rt-rte-validate-change"
        - "epistemic.md#epi-rte-impact-read"
        - "runtime.md#rt-rte-review-audit"
        - "epistemic.md#epi-rte-audit-gc"
        - "memory.md#mem-obj-reverse-index"
        - "memory.md#mem-rte-metric-readback"
        - "memory.md#mem-obj-metrics"
        - "memory.md#mem-obj-context-catalog"
        - "memory.md#mem-obj-context-log"
      note: "The accepted local inventory has requested read-back, including deterministic later consumers and documented file access. Static skill loading and opaque external host context policies are excluded; no separate included unsolicited injection path is established."
    read_back_signal:
      assessment: "inapplicable"
      units:
        -
          scope: "All included requested memory read-back routes"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-context-read"
            - "memory.md#mem-rte-concept-read"
            - "memory.md#mem-clm-context-selection"
            - "runtime.md#rt-rte-validate-change"
            - "epistemic.md#epi-rte-impact-read"
            - "runtime.md#rt-rte-review-audit"
            - "epistemic.md#epi-rte-audit-gc"
            - "memory.md#mem-rte-metric-readback"
            - "memory.md#mem-obj-context-catalog"
            - "memory.md#mem-obj-context-log"
          note: "The completely classified local direction inventory is pull-only. Requested path/identity matching, sampling and status/rank filtering do not establish a push selector."
      records:
        - "runtime.md#rt-rte-context-read"
        - "memory.md#mem-rte-concept-read"
        - "memory.md#mem-clm-context-selection"
        - "runtime.md#rt-rte-validate-change"
        - "epistemic.md#epi-rte-impact-read"
        - "runtime.md#rt-rte-review-audit"
        - "epistemic.md#epi-rte-audit-gc"
        - "memory.md#mem-rte-metric-readback"
        - "memory.md#mem-obj-context-catalog"
        - "memory.md#mem-obj-context-log"
      note: "Push selection signal is inapplicable to this local pull-only boundary, not absent worldwide. Identity addresses on requested reads do not justify identifier-based push."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "History-subject bootstrap into retained drafts and later agent context"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bootstrap-drafts"
                - "epistemic.md#epi-rte-bootstrap-import"
                - "epistemic.md#epi-obj-bootstrap-body"
                - "runtime.md#rt-rte-context-read"
                - "memory.md#mem-rte-concept-read"
              note: "Recorded commit-change activity feeds automatic draft production; persisted explanations can reach a later draft-enabled context invocation or direct read. This satisfies the trace-fed artifact criterion without observed benefit."
          records:
            - "runtime.md#rt-rte-bootstrap-drafts"
            - "epistemic.md#epi-rte-bootstrap-import"
            - "epistemic.md#epi-obj-bootstrap-body"
            - "runtime.md#rt-rte-context-read"
            - "memory.md#mem-rte-concept-read"
          note: "This local positive is architectural. Default draft filtering does not remove the alternate later-consumer route."
        -
          scope: "Foreground validation-feedback-to-memory revision requested by coding skill"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-coding-loop"
                - "runtime.md#rt-rte-validate-change"
                - "runtime.md#rt-rte-memory-write"
              note: "The agent is instructed to use command diagnostics to repair or author retained explanations and revalidate; the route is afforded by the protocol, not an observed model revision."
          records:
            - "runtime.md#rt-rte-coding-loop"
            - "runtime.md#rt-rte-validate-change"
            - "runtime.md#rt-rte-memory-write"
          note: "Trace-responsive authoring is weaker evidence than bootstrap's deterministic transformation; bases remain separate."
        -
          scope: "Actual repair-harness trace-fed durable update"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-repair"
          note: "The child can inspect repository state, but its consumed traces, writes and later behavior-shaping result are not established by process success."
        -
          scope: "Metrics/log retention and arbitrary initial-content update alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-metrics"
            - "memory.md#mem-rte-metric-readback"
            - "memory.md#mem-obj-context-log"
            - "runtime.md#rt-obj-concept-body"
          note: "Metrics have diagnostic reuse and logs have a readable surface, but these records establish no qualifying behavior-shaping update from them. No bounded evidenced-absence record warrants a local no; unknown initial/direct updates remain unresolved."
      records:
        - "runtime.md#rt-rte-bootstrap-drafts"
        - "epistemic.md#epi-rte-bootstrap-import"
        - "epistemic.md#epi-obj-bootstrap-body"
        - "runtime.md#rt-rte-context-read"
        - "memory.md#mem-rte-concept-read"
        - "runtime.md#rt-rte-coding-loop"
        - "runtime.md#rt-rte-validate-change"
        - "runtime.md#rt-rte-memory-write"
        - "runtime.md#rt-rte-agent-repair"
        - "memory.md#mem-obj-metrics"
        - "memory.md#mem-rte-metric-readback"
        - "memory.md#mem-obj-context-log"
        - "runtime.md#rt-obj-concept-body"
      note: "A wired bootstrap positive and an afforded feedback route coexist with unresolved alternatives. Coverage is partial, system-level yes is supported, and no local or system-wide negative is asserted. This axis does not establish improved future capacity or model-parameter change."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "History-subject bootstrap's original trace input"
          assessment: "known"
          findings:
            -
              value: "event-streams"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bootstrap-drafts"
                - "epistemic.md#epi-rte-bootstrap-import"
              note: "Git commit records describe discrete repository change events; the selected subjects are recorded activity, not conversational sessions, tool-call transcripts or linked state/action/outcome trajectories."
          records:
            - "runtime.md#rt-rte-bootstrap-drafts"
            - "epistemic.md#epi-rte-bootstrap-import"
          note: "The source is the commit-change record itself, not merely an attached commit pointer on an imported comment."
        -
          scope: "Requested validation-feedback-driven foreground revision"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-coding-loop"
                - "runtime.md#rt-rte-validate-change"
                - "runtime.md#rt-rte-memory-write"
              note: "Command execution feedback supplies classifications, missing-memory findings and repair diagnostics used by the requested revision loop."
          records:
            - "runtime.md#rt-rte-coding-loop"
            - "runtime.md#rt-rte-validate-change"
            - "runtime.md#rt-rte-memory-write"
          note: "Only the afforded feedback route is classified; no complete host-session capture is inferred."
        -
          scope: "Repair-harness consumed traces"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-agent-repair"
          note: "The static prompt does not include computed lost/candidate data; actual child inspection and original trace inputs are unobserved."
        -
          scope: "Comment/document bootstrap branch"
          assessment: "inapplicable"
          findings: []
          records:
            - "epistemic.md#epi-rte-bootstrap-import"
          note: "This branch copies static repository text rather than consuming activity traces; a last-touch commit pointer does not establish a trace-fed transformation of the note."
        -
          scope: "Metrics/log and arbitrary initial-content update alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-metrics"
            - "memory.md#mem-rte-metric-readback"
            - "memory.md#mem-obj-context-log"
            - "runtime.md#rt-obj-concept-body"
          note: "No qualifying behavior-shaping update and original trace source are established for these alternatives. Their uncertainty cannot be erased by the bootstrap witness."
      records:
        - "runtime.md#rt-rte-bootstrap-drafts"
        - "epistemic.md#epi-rte-bootstrap-import"
        - "runtime.md#rt-rte-coding-loop"
        - "runtime.md#rt-rte-validate-change"
        - "runtime.md#rt-rte-memory-write"
        - "runtime.md#rt-rte-agent-repair"
        - "memory.md#mem-obj-metrics"
        - "memory.md#mem-rte-metric-readback"
        - "memory.md#mem-obj-context-log"
        - "runtime.md#rt-obj-concept-body"
      note: "Original inputs are classified per qualifying route. Importing static comments with a last-touch commit reference does not turn those comments into event-stream traces. Repair provenance prevents complete source coverage."
---

# RepoCodex memory profile

## Comparison rationale

The comparison concerns accumulated repository memory, not every persistent file installed by the runtime. Static skills supply the write/read protocol but are not an additional memory instruction registry. Files hold explanations and access structures; Git history supplies bootstrap's activity input. Metrics remain a separate, usually ignored file store. The operative inventory is supported by [RT-OBJ-concept-body](runtime.md#rt-obj-concept-body), [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter), [MEM-OBJ-context-catalog](memory.md#mem-obj-context-catalog), [MEM-OBJ-context-log](memory.md#mem-obj-context-log), [MEM-OBJ-reverse-index](memory.md#mem-obj-reverse-index) and [MEM-OBJ-metrics](memory.md#mem-obj-metrics).

### Mixed parts and consumer-specific authority

Prose explanations supply knowledge to coding agents. Body-link targets and parsed frontmatter supply symbolic selectors and criteria. Sources and stamps also affect rank without authenticating content. Persisted reverse-index copies are checked for synchronization; retrieval reconstructs current mappings rather than loading those copies. These forces must not be collapsed into one knowledge or enforcement value: see [RT-BAP-memory-consumption](runtime.md#rt-bap-memory-consumption), [MEM-CLM-context-selection](memory.md#mem-clm-context-selection), [MEM-OBJ-reverse-index](memory.md#mem-obj-reverse-index), [EPI-RTE-impact-read](epistemic.md#epi-rte-impact-read) and [EPI-RTE-claim-check](epistemic.md#epi-rte-claim-check).

Deprecation is invalidation with history retained, not global deletion. It enforces ordinary body exclusion but does not prevent direct reads. Reanchor evolves existing evidence pointers; identity relocation alone preserves body bytes and does not establish semantic curation. Draft-to-stable normalization is a tier promotion. No observed semantic synthesis, consolidation or deduplication follows from a repair command name, import wrapper or primary-key check: see [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [RT-RTE-anchor-patch](runtime.md#rt-rte-anchor-patch), [RT-RTE-relocate-identity](runtime.md#rt-rte-relocate-identity), [EPI-RTE-audit-gc](epistemic.md#epi-rte-audit-gc) and [MEM-RTE-concept-read](memory.md#mem-rte-concept-read).

### Requests versus unsolicited selection

All established local later-consumer routes are requested reads or requested computations. Path/identity matching inside a requested context return is pull, not an additional push. Audit sampling, impact traversal and validation loading likewise fulfill an explicit command request. The record inventory supplies no independent unsolicited injection route within this boundary. Consequently read-back signal is inapplicable here, not identifier merely because a requested identity is exact. The relevant warrants are [RT-RTE-context-read](runtime.md#rt-rte-context-read), [MEM-RTE-concept-read](memory.md#mem-rte-concept-read), [RT-RTE-review-audit](runtime.md#rt-rte-review-audit), [EPI-RTE-impact-read](epistemic.md#epi-rte-impact-read) and [MEM-RTE-metric-readback](memory.md#mem-rte-metric-readback). Host injection and provider retention are outside this inventory, not classified as absent.

### Trace-fed artifacts without demonstrated benefit

The bootstrap history branch selects recorded change subjects, automatically persists drafts and exposes them to later draft-enabled or direct readers. This supports wired trace learning under the profile's artifact-update definition, with event-stream origin and trace-extracted lineage for that history subset. Its update consumer has learning authority; the resulting explanation supplies knowledge downstream. The comment/document branch instead imports static authored text. A last-touch commit pointer does not transform that text's origin into an activity trace. Import and trace extraction describe distinct provenance aspects of the history branch, not a new semantic inference: see [RT-RTE-bootstrap-drafts](runtime.md#rt-rte-bootstrap-drafts), [EPI-RTE-bootstrap-import](epistemic.md#epi-rte-bootstrap-import) and [EPI-OBJ-bootstrap-body](epistemic.md#epi-obj-bootstrap-body).

The coding skill affords a second, weaker route from validation feedback to retained explanation revision. Its tool-feedback origin remains separate from the wired bootstrap witness. No trace establishes actual foreground revision or improved capacity. The repair subprocess remains unresolved: process success neither identifies its inputs nor certifies a durable update. Metrics supply a diagnostic ratio, not an inspected policy-update consumer. These distinctions follow [RT-RTE-coding-loop](runtime.md#rt-rte-coding-loop), [RT-RTE-validate-change](runtime.md#rt-rte-validate-change), [RT-RTE-agent-repair](runtime.md#rt-rte-agent-repair) and [MEM-RTE-metric-readback](memory.md#mem-rte-metric-readback).

Partial trace-learning coverage retains a supported system-level yes but licenses neither a complete learning inventory nor a no. No accepted evidenced-absence record warrants a local no for the diagnostic or arbitrary-content alternatives. Original authorship, explicit human control on direct/initial writes, actual repair transformations and any additional semantic authority of their payloads remain unresolved rather than borrowing the strongest witness from another route.

### Reconciliation and inspection limits

The supplied reconciliation makes no supersession amendment. Valid containers and their declared parts remain canonical; no comparison value depends on replacing a record. It separates path retrieval from direct identity reads and index reconstruction from persisted sync-check copies. Possible shard identity collisions limit unambiguous addressing, not the existence of retained file memory. The local warrants are [RT-RTE-context-read](runtime.md#rt-rte-context-read), [MEM-RTE-concept-read](memory.md#mem-rte-concept-read), [MEM-OBJ-reverse-index](memory.md#mem-obj-reverse-index) and [RT-OBJ-concept-frontmatter](runtime.md#rt-obj-concept-frontmatter).

Source-read log: none. This profile classifies the supplied accepted records only. No source ambiguity required a frozen-source read. All positive bases remain implementation wiring or afforded protocol routes; no observed or causal finding is inferred. Unknown provenance and repair behavior prevent stronger coverage where explicitly named, while external hosts are excluded consistently rather than treated as opaque local stores.
