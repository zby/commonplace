---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "OKF memory comparison: retained Markdown knowledge and work state, selective retrieval and hook supply, with opaque payload/backend alternatives."
run-id: "AAS-2026-11-08-okf-8bc42addf404-01"
source-identity: "https://github.com/serradura/okf"
reviewed-boundary: "cfb7ffac7fef37d56e97b5b7dd8fe97ffc648c7c"
memory-comparison:
  version: 2
  scope: "Retained concept prose and metadata; authored indexes and update logs; Pro board, journal, caller-retained Snapshot lines and friction events; reference payloads/computation contracts; their acquisition, maintenance, access structures and later consumers, including the unresolved optional backend seam. Includes requested use-derived refinement of retained layout/guidance, not fixed shipped skills/settings as accumulated memory. Excludes external model weights, host conversation/compaction state and transient attestation receipts."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Retained concept bodies/metadata, authored indexes/logs, Pro board/journal/snapshot and friction events"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-concept-body"
                - "memory.md#mem-obj-concept-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-board"
                - "memory.md#mem-obj-journal"
                - "memory.md#mem-obj-snapshot"
                - "memory.md#mem-obj-friction"
              note: "Markdown/YAML and JSON-lines are retained as filesystem objects; encoding does not make these database or graph storage."
          records:
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-concept-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-board"
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-obj-friction"
          note: "Records inventory the disk corpus and its separate work-state and telemetry objects."
        -
          scope: "Parsed access views and fallback MCP corpus/cache"
          assessment: "known"
          findings:
            -
              value: "in-memory"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-mcp-retrieve"
              note: "Parsed folders and prepared search corpora reside in the Ruby process; this is the access structure, not replacement durable storage."
          records:
            - "runtime.md#rt-rte-mcp-retrieve"
          note: "Known fallback residency; no inference to the optional backend."
        -
          scope: "Reference payloads and computation contracts retained in the bundle"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-references"
                - "epistemic.md#epi-obj-computation"
              note: "Contract fields, inline computation and referenced payload paths are filesystem-backed; unknown payload semantics do not obscure their local storage."
          records:
            - "memory.md#mem-obj-references"
            - "epistemic.md#epi-obj-computation"
          note: "Covers the retained local assets, not external executor state or transient receipts."
        -
          scope: "Journal reconstruction's retained Git-history input"
          assessment: "known"
          findings:
            -
              value: "repo"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-journal"
              note: "The authored recovery procedure explicitly reconstructs from log.md and Git history."
          records:
            - "memory.md#mem-obj-journal"
          note: "The repo value is confined to the requested history input, not inferred merely because Markdown sits in a repository."
        -
          scope: "Optional okf-sqlite3 backend's operative retained/index state"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-mcp-retrieve"
          note: "Detection/fallback does not expose backend internals; its name cannot establish sqlite storage."
      records:
        - "memory.md#mem-obj-concept-body"
        - "memory.md#mem-obj-concept-metadata"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-board"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-obj-snapshot"
        - "memory.md#mem-obj-friction"
        - "runtime.md#rt-rte-mcp-retrieve"
        - "memory.md#mem-obj-references"
        - "epistemic.md#epi-obj-computation"
      note: "Local corpus and fallback access storage are classified; included optional backend state prevents complete coverage. External host conversation storage/model weights and runtime receipts are excluded."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Concept prose and text metadata, authored indexes/logs, board task prose and journal narrative at agent/human readers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-concept-body"
                - "memory.md#mem-obj-concept-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-board"
                - "memory.md#mem-obj-journal"
              note: "Readers interpret explanations, descriptions, tasks and narrative; search also treats text as features."
          records:
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-concept-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-board"
            - "memory.md#mem-obj-journal"
          note: "Interpretive content is separate from fixed-rule fields in the same files."
        -
          scope: "Concept metadata, index version, board grammar/cap, Snapshot counters, friction event fields and access maps at Ruby consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-concept-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-board"
                - "memory.md#mem-obj-snapshot"
                - "memory.md#mem-obj-friction"
                - "runtime.md#rt-rte-mcp-retrieve"
              note: "Localized fields and fixed parsing/filter/count rules determine these consumers' behavior."
          records:
            - "memory.md#mem-obj-concept-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-board"
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-obj-friction"
            - "runtime.md#rt-rte-mcp-retrieve"
          note: "A numerical counter is symbolic, not distributed-parametric."
        -
          scope: "Attested computation binding/check contract"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-computation"
              note: "Fixed runtime/parameter/resource declarations are retained independently of the opaque payload they name."
          records:
            - "epistemic.md#epi-obj-computation"
          note: "Contract representation is inspected; executor operation is not."
        -
          scope: "Documented reference code and run-instruction consumption paths"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-references"
              note: "Executable code is offered to an external executor under the documented contract."
            -
              value: "natural-language"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-references"
              note: "Run instructions are interpreted by the agent, not executed as fixed syntax."
          records:
            - "memory.md#mem-obj-references"
          note: "Classifies only the described code/instruction paths, not every referenced asset."
        -
          scope: "Arbitrary reference payload contents"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-references"
          note: "Inventory and contracts cannot classify every actual payload's operative encoding."
        -
          scope: "Optional backend's stored/index payload"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-mcp-retrieve"
          note: "No inspected payload establishes symbolic, text or dense numerical representation."
      records:
        - "memory.md#mem-obj-concept-body"
        - "memory.md#mem-obj-concept-metadata"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-board"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-obj-snapshot"
        - "memory.md#mem-obj-friction"
        - "runtime.md#rt-rte-mcp-retrieve"
        - "epistemic.md#epi-obj-computation"
        - "memory.md#mem-obj-references"
      note: "Mixed prose and fixed-rule material are split by consumer. Opaque payload and backend alternatives preclude known coverage; external model parameters are not this memory boundary."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Agent/user-authored concepts, metadata, maps, logs, board and journal narrative"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-concept-body"
                - "memory.md#mem-obj-concept-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-board"
                - "memory.md#mem-obj-journal"
                - "runtime.md#rt-rte-skill-work"
              note: "Procedures assign content construction and revision to agents/users; no observed authorship episode is supplied."
          records:
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-concept-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-board"
            - "memory.md#mem-obj-journal"
            - "runtime.md#rt-rte-skill-work"
          note: "Covers the specified authored paths, not every initial adopter byte."
        -
          scope: "Verbatim migrated document bodies"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-concept-body"
              note: "Migration adopts existing bodies and preserves them apart from permitted relocation-link edits."
          records:
            - "memory.md#mem-obj-concept-body"
          note: "Import is distinct from the authored distillation path."
        -
          scope: "Mechanically derived work-state text, counter lines and instrumented event records"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pro-writes"
                - "memory.md#mem-obj-snapshot"
                - "memory.md#mem-obj-friction"
              note: "Fixed transforms render scaffolds, state counters and structured event fields; no model-weight lineage follows."
          records:
            - "runtime.md#rt-rte-pro-writes"
            - "memory.md#mem-obj-snapshot"
            - "memory.md#mem-obj-friction"
          note: "Known subsequent derivation does not resolve initial prose provenance."
        -
          scope: "Initial adopter content and arbitrary reference payload derivations"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-board"
            - "memory.md#mem-obj-references"
          note: "Caller-dependent initial material and per-file payload origins prevent a complete lineage inventory."
        -
          scope: "Optional backend index/payload derivation"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-mcp-retrieve"
          note: "Neither initial index nor any embedding provenance is supplied."
      records:
        - "memory.md#mem-obj-concept-body"
        - "memory.md#mem-obj-concept-metadata"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-board"
        - "memory.md#mem-obj-journal"
        - "runtime.md#rt-rte-skill-work"
        - "runtime.md#rt-rte-pro-writes"
        - "memory.md#mem-obj-snapshot"
        - "memory.md#mem-obj-friction"
        - "memory.md#mem-obj-references"
        - "runtime.md#rt-rte-mcp-retrieve"
      note: "Authored, adopted and mechanically rendered paths coexist. No trace-extracted lesson lineage is inferred merely from a Learning label or raw event persistence."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Selected concept/index/log/journal content and opening state at later agent/human interpretation"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-concept-body"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-journal"
                - "memory.md#mem-rte-snapshot-context"
                - "memory.md#mem-rte-friction-feedback"
              note: "Retained content supplies project reference, history and state cues; delivery does not establish compliance or benefit."
          records:
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-journal"
            - "memory.md#mem-rte-snapshot-context"
            - "memory.md#mem-rte-friction-feedback"
          note: "Force is contextual/advisory at the actual later reader."
        -
          scope: "Retained text and metadata consumed by search and filters"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-concept-body"
                - "memory.md#mem-obj-concept-metadata"
                - "runtime.md#rt-rte-mcp-retrieve"
                - "memory.md#mem-rte-reconcile-search"
              note: "Text features and metadata influence relative search priority; fixed scoring still makes retained text a ranking input."
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-concept-metadata"
                - "runtime.md#rt-rte-mcp-retrieve"
                - "epistemic.md#epi-rte-trust-tier"
              note: "Requested status/trust and other predicates select which retained rows reach the consumer."
          records:
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-concept-metadata"
            - "runtime.md#rt-rte-mcp-retrieve"
            - "memory.md#mem-rte-reconcile-search"
            - "epistemic.md#epi-rte-trust-tier"
          note: "Ranking and membership are distinct effects; full concept reads have no universal trust precondition."
        -
          scope: "Retained board grammar/cap and provenance/links at writer and pairing checks"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-board"
                - "runtime.md#rt-rte-pro-writes"
                - "epistemic.md#epi-rte-read-pairing"
              note: "The retained cap and metadata/board pairing determine admissibility or consistency under fixed rules."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-board"
                - "runtime.md#rt-rte-pro-writes"
                - "epistemic.md#epi-rte-read-pairing"
              note: "Cap can refuse promotion; pairing failures can block configured Stop/audit doors. Force depends on the relevant integration."
          records:
            - "memory.md#mem-obj-board"
            - "runtime.md#rt-rte-pro-writes"
            - "epistemic.md#epi-rte-read-pairing"
          note: "These retained criteria are not the static checker source; they license structural/work-state consequences, not truth."
        -
          scope: "Authored branch maps, board priorities and retained deprecated explanations at interpreting agents"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-board"
                - "epistemic.md#epi-rte-semantic-disposition"
              note: "Maps guide traversal; task and conflict prose direct attention; deprecation changes requested reliance."
          records:
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-board"
            - "epistemic.md#epi-rte-semantic-disposition"
          note: "Requested interpretation is not automatic semantic compliance."
        -
          scope: "Reference run instructions and sanctioned computation contract at documented consumers"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-references"
              note: "Retained run instructions guide the external agent."
            -
              value: "validation"
              basis: "claimed"
              records:
                - "epistemic.md#epi-obj-computation"
                - "epistemic.md#epi-rte-run-attestation"
              note: "The sanctioned binding is the criterion for the specified per-call fidelity comparison."
            -
              value: "enforcement"
              basis: "claimed"
              records:
                - "epistemic.md#epi-obj-computation"
                - "epistemic.md#epi-rte-display-gate"
              note: "The consumer protocol calls for refusal of failed attestation, not an implemented MCP execution gate."
          records:
            - "memory.md#mem-obj-references"
            - "epistemic.md#epi-obj-computation"
            - "epistemic.md#epi-rte-run-attestation"
            - "epistemic.md#epi-rte-display-gate"
          note: "Separate offered instruction path and specified validation/refusal effects; no operated executor is supplied."
        -
          scope: "Opaque reference payload and optional backend-specific consumer effects"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-references"
            - "runtime.md#rt-rte-mcp-retrieve"
          note: "Known contract and fallback witnesses do not classify arbitrary payload effects or opaque backend consumers."
      records:
        - "memory.md#mem-obj-concept-body"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-journal"
        - "memory.md#mem-rte-snapshot-context"
        - "memory.md#mem-rte-friction-feedback"
        - "memory.md#mem-obj-concept-metadata"
        - "runtime.md#rt-rte-mcp-retrieve"
        - "memory.md#mem-rte-reconcile-search"
        - "epistemic.md#epi-rte-trust-tier"
        - "memory.md#mem-obj-board"
        - "runtime.md#rt-rte-pro-writes"
        - "epistemic.md#epi-rte-read-pairing"
        - "epistemic.md#epi-rte-semantic-disposition"
        - "memory.md#mem-obj-references"
        - "epistemic.md#epi-obj-computation"
        - "epistemic.md#epi-rte-run-attestation"
        - "epistemic.md#epi-rte-display-gate"
      note: "Authority is assigned at each consuming path. Learning authority is not inferred from recording telemetry; shipped static skills/hooks are excluded as memory values."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Ordinary agent semantic filing/maintenance without per-content human approval"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-skill-work"
                - "memory.md#mem-obj-concept-body"
              note: "The agent admits and edits durable findings without a required operator decision for each content item."
          records:
            - "runtime.md#rt-rte-skill-work"
            - "memory.md#mem-obj-concept-body"
          note: "This is the requested agent route; software file I/O alone does not establish it."
        -
          scope: "Owner verification and approved refine execution"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-semantic-review"
                - "runtime.md#rt-rte-refine-proposal"
              note: "Owner review supplies the verification decision; refine reserves execution approval to the user."
          records:
            - "epistemic.md#epi-rte-semantic-review"
            - "runtime.md#rt-rte-refine-proposal"
          note: "Human control is bounded to these decisions, not all bundle edits."
        -
          scope: "Mechanical Pro transformations and instrumented friction append"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-pro-writes"
                - "memory.md#mem-obj-friction"
              note: "Software constructs/admit deltas and appends event records without separate per-output human approval."
          records:
            - "runtime.md#rt-rte-pro-writes"
            - "memory.md#mem-obj-friction"
          note: "Starting the command does not turn software admission into manual admission."
        -
          scope: "Initial caller-supplied bundle/board content and caller append of a Snapshot line"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-publish-bundle"
            - "memory.md#mem-obj-board"
            - "memory.md#mem-rte-snapshot-context"
          note: "Generic caller identity and agent/person alternatives do not establish an explicit human admission decision or its absence for these particular writes."
        -
          scope: "Arbitrary reference payload admission and optional backend writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-references"
            - "runtime.md#rt-rte-mcp-retrieve"
          note: "Documented sanctioned-code constraints do not reveal every payload's actual admission, and backend write control is uninspected."
      records:
        - "runtime.md#rt-rte-skill-work"
        - "memory.md#mem-obj-concept-body"
        - "epistemic.md#epi-rte-semantic-review"
        - "runtime.md#rt-rte-refine-proposal"
        - "runtime.md#rt-rte-pro-writes"
        - "memory.md#mem-obj-friction"
        - "runtime.md#rt-rte-publish-bundle"
        - "memory.md#mem-obj-board"
        - "memory.md#mem-rte-snapshot-context"
        - "memory.md#mem-obj-references"
        - "runtime.md#rt-rte-mcp-retrieve"
      note: "Known agent, operator and software admission mechanisms coexist with unresolved caller and opaque alternatives. Snapshot derivation is not an automatic snapshot write."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Requested revision and retirement over retained concepts"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-skill-work"
                - "epistemic.md#epi-rte-semantic-disposition"
              note: "Maintenance revises existing bodies, descriptions, links and provenance."
            -
              value: "invalidate"
              basis: "claimed"
              records:
                - "epistemic.md#epi-rte-semantic-disposition"
              note: "Deprecation withdraws current reliance while preserving superseded reasoning/history."
          records:
            - "runtime.md#rt-rte-skill-work"
            - "epistemic.md#epi-rte-semantic-disposition"
          note: "These are authored semantic operations, not automatic conclusions from lint or vocabulary collision."
        -
          scope: "Distillation and closure lesson extraction's precise retained-input transformation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-journal"
            - "runtime.md#rt-rte-pro-writes"
          note: "Distillation/extraction is requested, but accepted records do not fix all retained inputs or establish whether particular output claims are compressed or novel; no consolidate/synthesize value is inferred from the label alone."
        -
          scope: "Refinement, arbitrary payload maintenance and optional backend transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-refine-proposal"
            - "memory.md#mem-obj-references"
            - "runtime.md#rt-rte-mcp-retrieve"
          note: "Proposal/route names, payload inventory and backend detection do not establish dedup, decay, consolidation or other implemented curation."
      records:
        - "runtime.md#rt-rte-skill-work"
        - "epistemic.md#epi-rte-semantic-disposition"
        - "memory.md#mem-obj-concept-body"
        - "memory.md#mem-obj-journal"
        - "runtime.md#rt-rte-pro-writes"
        - "runtime.md#rt-rte-refine-proposal"
        - "memory.md#mem-obj-references"
        - "runtime.md#rt-rte-mcp-retrieve"
      note: "Supported evolve/invalidate requests remain classified despite unresolved transformations. Board promotion is work placement, index rebuild is access maintenance and friction clear is telemetry deletion, not by themselves the controlled promote/decay operations."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "CLI/MCP task retrieval, requested resource reads and human browser/TUI consumption"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-skill-work"
                - "runtime.md#rt-rte-mcp-retrieve"
                - "runtime.md#rt-rte-registry-manage"
              note: "A consumer requests branch/query/id/history; code returns the selected retained material."
          records:
            - "runtime.md#rt-rte-skill-work"
            - "runtime.md#rt-rte-mcp-retrieve"
            - "runtime.md#rt-rte-registry-manage"
          note: "Returning a requested file is not an extra push. Host resource requests are pull at the OKF interface."
        -
          scope: "Pro SessionStart snapshot/state/friction and eligible Write reconciliation feedback"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-snapshot-context"
                - "memory.md#mem-rte-friction-feedback"
                - "memory.md#mem-rte-reconcile-search"
              note: "Hooks automatically supply retained-state cues and selected existing concepts without a request for those retained parts."
          records:
            - "memory.md#mem-rte-snapshot-context"
            - "memory.md#mem-rte-friction-feedback"
            - "memory.md#mem-rte-reconcile-search"
          note: "Installed hook/host protocol conditions apply; activation is unobserved."
        -
          scope: "External computation consumer loading a retained sanctioned definition"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-references"
                - "epistemic.md#epi-obj-computation"
              note: "The documented consumer discovers/loads a computation before binding and executing it."
          records:
            - "memory.md#mem-obj-references"
            - "epistemic.md#epi-obj-computation"
          note: "Specified external role only, not a deployed executor."
        -
          scope: "Optional backend-specific later delivery and arbitrary payload consumption"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-mcp-retrieve"
            - "memory.md#mem-obj-references"
          note: "The fallback chain and contract do not exhaust opaque backend or per-payload consumption alternatives."
      records:
        - "runtime.md#rt-rte-skill-work"
        - "runtime.md#rt-rte-mcp-retrieve"
        - "runtime.md#rt-rte-registry-manage"
        - "memory.md#mem-rte-snapshot-context"
        - "memory.md#mem-rte-friction-feedback"
        - "memory.md#mem-rte-reconcile-search"
        - "memory.md#mem-obj-references"
        - "epistemic.md#epi-obj-computation"
      note: "Both requested retrieval and unsolicited hook supply are supported. External host resource attachment/window policy is not an OKF autonomous selector, and opaque alternatives retain uncertainty."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "SessionStart delivery of historical Snapshot and selected friction cues"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-snapshot-context"
                - "memory.md#mem-rte-friction-feedback"
              note: "SessionStart triggers selection of the latest dated Snapshot in the cwd-scoped bundle, plus verb-covered event counts; recency/availability and category predicates are coarse, not semantic targeting."
          records:
            - "memory.md#mem-rte-snapshot-context"
            - "memory.md#mem-rte-friction-feedback"
          note: "Names the trigger, selector and selected retained parts; no embedding or lexical query is used on this path."
        -
          scope: "Write-triggered reconciliation of retained concepts"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "memory.md#mem-rte-reconcile-search"
              note: "An eligible Write provides up to four basename terms; lexical search selects up to five concept hits per term for snippets/ids, excluding self."
          records:
            - "memory.md#mem-rte-reconcile-search"
          note: "Actual automatic text matching establishes the signal, not the mere presence of ids in its output."
        -
          scope: "Host attachment selection, opaque backend and arbitrary payload push alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-mcp-retrieve"
            - "memory.md#mem-obj-references"
          note: "Host chooses attachments outside inspected selector code; opaque internals do not establish a targeted signal. Requested exact-id reads alone do not establish identifier push."
      records:
        - "memory.md#mem-rte-snapshot-context"
        - "memory.md#mem-rte-friction-feedback"
        - "memory.md#mem-rte-reconcile-search"
        - "runtime.md#rt-rte-mcp-retrieve"
        - "memory.md#mem-obj-references"
      note: "Known hook push selectors coexist with unresolved host/opaque alternatives. Pull task judgment and exact-id reads are excluded from push-signal findings; no blanket inapplicability follows."
    trace_learning:
      assessment: "not-determinable"
      units:
        -
          scope: "Agent write-back and journal/closure extraction into durable task guidance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-skill-work"
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-journal"
            - "runtime.md#rt-rte-pro-writes"
          note: "Records establish requested findings/extraction and later retrieval, but not a qualifying automatic trace-fed write with recorded trace input and durable behavior-shaping output; no bounded absence record warrants no."
        -
          scope: "Caller-retained mechanical Snapshot and automatic raw friction telemetry"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-snapshot-context"
            - "memory.md#mem-rte-friction-feedback"
          note: "Snapshot retention is caller-mediated; friction automatically retains raw intent and later computes a transient count, not a demonstrated durable derived behavior-shaping artifact. These facts do not supply an evidenced-absence record for a local no."
        -
          scope: "Reference-payload, optional backend and instruction-refinement alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-references"
            - "runtime.md#rt-rte-mcp-retrieve"
            - "runtime.md#rt-rte-refine-proposal"
          note: "Opaque internals and requested restructuring do not settle qualifying trace-fed writes; no whole-inventory negative is warranted."
      records:
        - "runtime.md#rt-rte-skill-work"
        - "memory.md#mem-obj-concept-body"
        - "memory.md#mem-obj-journal"
        - "runtime.md#rt-rte-pro-writes"
        - "memory.md#mem-rte-snapshot-context"
        - "memory.md#mem-rte-friction-feedback"
        - "memory.md#mem-obj-references"
        - "runtime.md#rt-rte-mcp-retrieve"
        - "runtime.md#rt-rte-refine-proposal"
      note: "No controlled yes is established and no accepted evidenced-absence record licenses a known local no. This is uncertainty about the comparison definition, not a claim that OKF never learns or that future capacity is absent."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Potential agent finding/journal extraction chain"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-skill-work"
            - "memory.md#mem-obj-journal"
            - "runtime.md#rt-rte-pro-writes"
          note: "No qualifying automatic trace-learning write is established; authored work narrative and reconstructed log/Git history do not automatically establish session-logs or trajectories as its original consumed trace source."
        -
          scope: "Snapshot/friction chain"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-snapshot-context"
            - "memory.md#mem-rte-friction-feedback"
            - "memory.md#mem-obj-friction"
          note: "Raw friction inputs are runtime hook intents, but no qualifying durable learning output is established. Thus event-streams is not asserted merely for logging them."
        -
          scope: "Opaque reference/backend and refinement alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-references"
            - "runtime.md#rt-rte-mcp-retrieve"
            - "runtime.md#rt-rte-refine-proposal"
          note: "Original inputs to any qualifying update remain unresolved; cannot mark trace source inapplicable while trace-learning inventory is unresolved."
      records:
        - "runtime.md#rt-rte-skill-work"
        - "memory.md#mem-obj-journal"
        - "runtime.md#rt-rte-pro-writes"
        - "memory.md#mem-rte-snapshot-context"
        - "memory.md#mem-rte-friction-feedback"
        - "memory.md#mem-obj-friction"
        - "memory.md#mem-obj-references"
        - "runtime.md#rt-rte-mcp-retrieve"
        - "runtime.md#rt-rte-refine-proposal"
      note: "Source values describe qualifying learning inputs, not every retained activity record. Lack of a positive learning classification is not completely assessed absence."
---

# OKF memory profile

## Comparison rationale

This profile classifies accepted records, not source files or an executed OKF session. Implementation findings use wired basis; requested agent semantics retain claimed basis. The external computation consumer is an afforded role, while its specified attestation/refusal rules remain claimed. No observed or causally supported basis is available. Evidence limits do not erase the known file-based paths.

The retained inventory is not the whole runtime's storage. Parsed folders/corpora are access structures over retained files; the optional backend remains opaque despite its SQLite-like package name. Git history appears only as the requested journal-reconstruction input. Fixed shipped skill and hook machinery do not become acquired memory merely because installation copies them. See [MEM-OBJ-journal](memory.md#mem-obj-journal), [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve) and [RT-RTE-governance-install](runtime.md#rt-rte-governance-install).

Canonical citations reflect all three reconciliation supersessions: concept prose uses [MEM-OBJ-concept-body](memory.md#mem-obj-concept-body), provenance uses [MEM-OBJ-concept-metadata](memory.md#mem-obj-concept-metadata), and collision feedback uses [MEM-RTE-reconcile-search](memory.md#mem-rte-reconcile-search). The corresponding epistemic declarations are not cited as separate objects/routes. The computation contract remains separate from the broader reference-payload inventory, because those referents are not coextensive. Its symbolic fields cannot classify an opaque executable or numerical payload. See [EPI-OBJ-computation](epistemic.md#epi-obj-computation) and [MEM-OBJ-references](memory.md#mem-obj-references).

Knowledge, ranking, routing and validation concern distinct consumption paths. Searchable retained text can influence ranking without a learned retrieval policy. Trust/status filters route optional result membership; human-review metadata and board links also become criteria at the pairing checks. The board cap can veto promotion through a mechanical writer. These are retained-data effects, not a claim that every concept is an enforced instruction or semantically validated. See [EPI-RTE-trust-tier](epistemic.md#epi-rte-trust-tier), [EPI-RTE-read-pairing](epistemic.md#epi-rte-read-pairing), [MEM-OBJ-board](memory.md#mem-obj-board) and [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes).

Ordinary model admission without per-content operator approval is the automatic write-agency branch, although its operation remains unobserved. Human verification and refine approval are separately claimed manual decisions. A generic caller at Writer or the Snapshot append does not resolve that caller's control. Mechanical derivation and physical writing are not human approval; computing a Snapshot does not write it. See [RT-RTE-skill-work](runtime.md#rt-rte-skill-work), [RT-RTE-refine-proposal](runtime.md#rt-rte-refine-proposal), [EPI-RTE-semantic-review](epistemic.md#epi-rte-semantic-review) and [MEM-RTE-snapshot-context](memory.md#mem-rte-snapshot-context).

Curation findings retain their requested layer. Correction evolves existing content; deprecation invalidates reliance while keeping context. Distillation, closure extraction and proposal terminology alone cannot decide consolidation versus synthesis for a particular retained-input transformation. No new claim is inferred from requested cross-cutting explanation, and faithfulness is not established by structural conformance. Mechanical promotion moves board work, not necessarily a memory item to a higher salience tier. See [EPI-RTE-semantic-disposition](epistemic.md#epi-rte-semantic-disposition), [MEM-OBJ-concept-body](memory.md#mem-obj-concept-body), [RT-RTE-pro-writes](runtime.md#rt-rte-pro-writes) and [WF-RTE-maintenance-closeout](workflow.md#wf-rte-maintenance-closeout).

Read-back separates request, selection and delivery. CLI/MCP query or id requests are pull; exact-id delivery does not become identifier push. SessionStart and eligible Write feedback supply retained material without requesting those parts. Recency/category selection is coarse; automatic filename-term collision search is inferred-lexical. Host attachment may supply model context without a model fetch decision, but the accepted records do not reveal the host's selector. Its attachment request to OKF remains pull at that interface. See [RT-RTE-mcp-retrieve](runtime.md#rt-rte-mcp-retrieve), [MEM-RTE-snapshot-context](memory.md#mem-rte-snapshot-context), [MEM-RTE-friction-feedback](memory.md#mem-rte-friction-feedback) and [MEM-RTE-reconcile-search](memory.md#mem-rte-reconcile-search).

Trace learning cannot be reduced to persistence, a Learning label or improved-capacity claims. Caller-appended counters and automatically logged raw intents have later consumers, but the records do not establish an automatic trace-fed write of a durable behavior-shaping derivative. Nor do they declare an evidenced absence spanning each route. Thus neither a local controlled no nor a system-wide no is warranted; source classification remains unresolved rather than inapplicable. The telemetry's event origin does not by itself make event-streams a qualifying learning source. See [MEM-RTE-snapshot-context](memory.md#mem-rte-snapshot-context), [MEM-RTE-friction-feedback](memory.md#mem-rte-friction-feedback), [MEM-OBJ-friction](memory.md#mem-obj-friction) and [RT-RTE-refine-proposal](runtime.md#rt-rte-refine-proposal).

The supported system unions are derived only from findings; opaque alternatives remain in their units. In particular, the known fallback does not settle optional-backend storage/form/lineage, a reference inventory does not settle payload semantics, and claimed semantic operations do not acquire wired strength from executable storage. These unresolved facts prevent complete-value coverage, not existence of the supported branches.

Source-read log: none. No source ambiguity required a permitted frozen-source reread; all classifications use the supplied accepted records and their annotations.
