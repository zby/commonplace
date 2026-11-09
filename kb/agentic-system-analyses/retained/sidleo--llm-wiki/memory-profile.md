---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "llm-wiki memory comparison of retained bundles, editable rules and access/control state."
run-id: AAS-2026-11-08-llm-wiki-97b740596442-01
source-identity: https://github.com/sidleo/llm-wiki
reviewed-boundary: f70e680d852a78d48504425d87252531e68c5624
memory-comparison:
  version: 2
  scope: "Through-use concept bodies/frontmatter, raw registered assets and conditional Reference pages, editable AGENTS/APPEND rules, derived indexes/logs, Git/Feishu replicas and recovery copies, registry, sync/autosync metadata and Codex context digest. Excludes ephemeral graphs/current tool returns, static shipped skill/schema/test code, and external host/provider storage, transcripts, weights and compaction."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        -
          scope: "Local concepts, raw resources, navigation, operation logs, editable rules, access settings, sync ledger/backups and Codex digest"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-concept-body"
                - "memory.md#mem-obj-concept-metadata"
                - "memory.md#mem-obj-reference-source"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-wiki-cloud"
                - "memory.md#mem-obj-wiki-registry"
                - "memory.md#mem-obj-wiki-autosync"
                - "runtime.md#rt-rte-context-delivery"
              note: "Markdown, copied assets, JSON control files and digest files persist on the local filesystem."
          records:
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-concept-metadata"
            - "memory.md#mem-obj-reference-source"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-wiki-cloud"
            - "memory.md#mem-obj-wiki-registry"
            - "memory.md#mem-obj-wiki-autosync"
            - "runtime.md#rt-rte-context-delivery"
          note: "All named retained local parts use files, including symbolic control state."
        -
          scope: "Git-replicated bundle and retained history"
          assessment: "known"
          findings:
            -
              value: "repo"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-remote-sync"
              note: "Local commits and Git history retain bundle revisions."
          records:
            - "runtime.md#rt-rte-remote-sync"
          note: "Git is a repository persistence route; live remote success is unobserved."
        -
          scope: "Feishu replicated bundle payloads"
          assessment: "known"
          findings:
            -
              value: "service-object"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-remote-sync"
                - "memory.md#mem-obj-wiki-cloud"
              note: "Remote file/directory tokens address retained Feishu objects."
          records:
            - "runtime.md#rt-rte-remote-sync"
            - "memory.md#mem-obj-wiki-cloud"
          note: "Classifies target-side remote object references and transfer wiring, not service internals."
      records:
        - "memory.md#mem-obj-concept-body"
        - "memory.md#mem-obj-concept-metadata"
        - "memory.md#mem-obj-reference-source"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-wiki-cloud"
        - "memory.md#mem-obj-wiki-registry"
        - "memory.md#mem-obj-wiki-autosync"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-rte-remote-sync"
      note: "Inventory covers retained bundle objects, access/control files, backups and replication; ephemeral graphs and external host state are excluded."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Concept prose, descriptive metadata, navigation descriptions, operation descriptions and editable rule prose at interpreting readers"
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
                - "runtime.md#rt-obj-append-system-prompt"
                - "runtime.md#rt-obj-agents"
              note: "Hosts interpret domain advice and rule prose; descriptions and operation history are readable text."
          records:
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-concept-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-obj-append-system-prompt"
            - "runtime.md#rt-obj-agents"
          note: "Classification follows interpretation, not the presence of code fences."
        -
          scope: "IDs, type/tag/status fields, links, gate type lists, registry, sync/autosync metadata and context digest at fixed code consumers"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-concept-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-wiki-cloud"
                - "memory.md#mem-obj-wiki-registry"
                - "memory.md#mem-obj-wiki-autosync"
                - "runtime.md#rt-obj-agents"
                - "runtime.md#rt-rte-context-delivery"
              note: "Code interprets field keys, identity mappings, type membership, timestamps and digests by fixed rules."
          records:
            - "memory.md#mem-obj-concept-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-wiki-cloud"
            - "memory.md#mem-obj-wiki-registry"
            - "memory.md#mem-obj-wiki-autosync"
            - "runtime.md#rt-obj-agents"
            - "runtime.md#rt-rte-context-delivery"
          note: "Fixed comparisons and selectors consume localized symbolic units."
        -
          scope: "Arbitrary imported raw assets and their backup payloads"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-reference-source"
            - "memory.md#mem-obj-wiki-cloud"
          note: "Copying opaque or binary files does not establish their representational form at a later consumer."
      records:
        - "memory.md#mem-obj-concept-body"
        - "memory.md#mem-obj-concept-metadata"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-obj-append-system-prompt"
        - "runtime.md#rt-obj-agents"
        - "memory.md#mem-obj-wiki-cloud"
        - "memory.md#mem-obj-wiki-registry"
        - "memory.md#mem-obj-wiki-autosync"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-obj-reference-source"
      note: "Readable content and fixed-rule control parts are classified; imported arbitrary payloads and backup encodings retain local uncertainty."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Caller-authored concepts and editable rules"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-concept-body"
                - "runtime.md#rt-obj-append-system-prompt"
                - "runtime.md#rt-obj-agents"
                - "epistemic.md#epi-clm-knowledge-recording"
              note: "External authors/agents supply concepts and editable domain guidance."
          records:
            - "memory.md#mem-obj-concept-body"
            - "runtime.md#rt-obj-append-system-prompt"
            - "runtime.md#rt-obj-agents"
            - "epistemic.md#epi-clm-knowledge-recording"
          note: "Authored denotes a supported production path, not an authenticated author label."
        -
          scope: "Raw copies, migration outputs and remote acquisitions"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-reference-source"
                - "memory.md#mem-rte-bundle-migration"
                - "runtime.md#rt-rte-remote-sync"
              note: "Explicit files, legacy collections and remote bundle content enter retained state."
          records:
            - "memory.md#mem-obj-reference-source"
            - "memory.md#mem-rte-bundle-migration"
            - "runtime.md#rt-rte-remote-sync"
          note: "Import preserves or maps existing material without establishing original source warrant."
        -
          scope: "Conditional Reference page, generated metadata, index/log, sync ledger, autosync results and digest"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-derived-reference"
                - "memory.md#mem-obj-concept-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-wiki-cloud"
                - "memory.md#mem-obj-wiki-autosync"
                - "runtime.md#rt-rte-context-delivery"
              note: "Code derives excerpts, labels, navigation, operation entries and control state."
          records:
            - "epistemic.md#epi-obj-derived-reference"
            - "memory.md#mem-obj-concept-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-wiki-cloud"
            - "memory.md#mem-obj-wiki-autosync"
            - "runtime.md#rt-rte-context-delivery"
          note: "Fixed transformations compile descriptions and control metadata; they do not by themselves extract semantic experience."
        -
          scope: "Actual initial concept/rule/configuration content and arbitrary source origin"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-reference-source"
            - "memory.md#mem-obj-wiki-registry"
            - "runtime.md#rt-obj-append-system-prompt"
          note: "No original authoring history or source/proposal trace establishes every retained item's provenance."
      records:
        - "memory.md#mem-obj-concept-body"
        - "runtime.md#rt-obj-append-system-prompt"
        - "runtime.md#rt-obj-agents"
        - "epistemic.md#epi-clm-knowledge-recording"
        - "memory.md#mem-obj-reference-source"
        - "memory.md#mem-rte-bundle-migration"
        - "runtime.md#rt-rte-remote-sync"
        - "epistemic.md#epi-obj-derived-reference"
        - "memory.md#mem-obj-concept-metadata"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-wiki-cloud"
        - "memory.md#mem-obj-wiki-autosync"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-obj-wiki-registry"
      note: "Known authoring, copying and deterministic derivation paths coexist with unresolved initial content and raw-resource provenance."
    behavioral_authority:
      assessment: "known"
      units:
        -
          scope: "Concept bodies and displayed descriptive fields at requesting hosts"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-concept-body"
                - "memory.md#mem-obj-concept-metadata"
                - "runtime.md#rt-rte-bundle-read"
              note: "Returned advice supplies later host reference/context."
          records:
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-concept-metadata"
            - "runtime.md#rt-rte-bundle-read"
          note: "The get display may omit structured provenance; knowledge delivery is not endorsement."
        -
          scope: "Retained concept body and indexed metadata at lexical search scorer"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-concept-body"
                - "memory.md#mem-obj-concept-metadata"
                - "runtime.md#rt-rte-bundle-read"
              note: "Text matches, fields and filters affect returned search order."
          records:
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-concept-metadata"
            - "runtime.md#rt-rte-bundle-read"
          note: "Retained text influences priority even though ranking code is fixed."
        -
          scope: "Editable APPEND and AGENTS prose at host instruction readers"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-rule-delivery"
                - "runtime.md#rt-rte-context-delivery"
              note: "Retained directions are supplied as host guidance or requested rules."
          records:
            - "runtime.md#rt-bap-rule-delivery"
            - "runtime.md#rt-rte-context-delivery"
          note: "Wired channel is subject to truncation, cadence and host interpretation."
        -
          scope: "AGENTS type list at create admission code"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-agents"
                - "runtime.md#rt-rte-concept-create"
              note: "Type membership supplies the confirmation criterion."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-agents"
                - "runtime.md#rt-rte-concept-create"
              note: "Matching unconfirmed creates are refused on covered adapter paths."
          records:
            - "runtime.md#rt-obj-agents"
            - "runtime.md#rt-rte-concept-create"
          note: "Criteria and veto are separate forces of the same retained gate."
        -
          scope: "Registry, sync ledger, autosync settings/results and digest at resolvers, sync/scheduling and hook consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-registry"
                - "memory.md#mem-obj-wiki-cloud"
                - "memory.md#mem-obj-wiki-autosync"
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-rte-remote-sync"
              note: "Retained values select bundles, transfer/scheduling operations and whether context is injected."
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-registry"
                - "memory.md#mem-obj-wiki-cloud"
                - "memory.md#mem-obj-wiki-autosync"
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-rte-remote-sync"
              note: "Ledger comparisons provide conflict/destructive-action criteria."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-registry"
                - "memory.md#mem-obj-wiki-cloud"
                - "memory.md#mem-obj-wiki-autosync"
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-rte-remote-sync"
              note: "Ledger-dependent refusal can block covered destructive actions; wrapper failures limit universal guarantees."
          records:
            - "memory.md#mem-obj-wiki-registry"
            - "memory.md#mem-obj-wiki-cloud"
            - "memory.md#mem-obj-wiki-autosync"
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-rte-remote-sync"
          note: "Operational control does not establish semantic learning."
      records:
        - "memory.md#mem-obj-concept-body"
        - "memory.md#mem-obj-concept-metadata"
        - "runtime.md#rt-rte-bundle-read"
        - "runtime.md#rt-bap-rule-delivery"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-obj-agents"
        - "runtime.md#rt-rte-concept-create"
        - "memory.md#mem-obj-wiki-registry"
        - "memory.md#mem-obj-wiki-cloud"
        - "memory.md#mem-obj-wiki-autosync"
        - "runtime.md#rt-rte-remote-sync"
      note: "Covers recorded consumer paths, not unconsumed metadata or external model compliance. Static shipped schema/test predicates are excluded."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Ungated agent concept recording and caller-directed update admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-concept-create"
                - "runtime.md#rt-rte-concept-update"
                - "epistemic.md#epi-clm-knowledge-recording"
              note: "Software can admit externally agent-proposed content without a mandatory human content decision."
          records:
            - "runtime.md#rt-rte-concept-create"
            - "runtime.md#rt-rte-concept-update"
            - "epistemic.md#epi-clm-knowledge-recording"
          note: "These paths do not require a per-content human decision; configured confirmation alternatives are separate."
        -
          scope: "Ingest registration, migration mapping/copy, derived navigation/log/provenance and sync/control-state updates"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "memory.md#mem-rte-bundle-migration"
                - "memory.md#mem-rte-index-refresh"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-concept-metadata"
                - "memory.md#mem-obj-wiki-cloud"
                - "memory.md#mem-obj-wiki-autosync"
                - "runtime.md#rt-rte-context-delivery"
              note: "Code admits copied and derived retained content/state after operation-level triggers."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "memory.md#mem-rte-bundle-migration"
            - "memory.md#mem-rte-index-refresh"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-concept-metadata"
            - "memory.md#mem-obj-wiki-cloud"
            - "memory.md#mem-obj-wiki-autosync"
            - "runtime.md#rt-rte-context-delivery"
          note: "Starting a bulk operation or timer is not approval of each derived retained item."
        -
          scope: "Cooperating human-confirmation workflow for configured create types"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-concept-create"
                - "epistemic.md#epi-clm-knowledge-recording"
              note: "Guidance requests displaying the actual proposal and obtaining human approval before retry."
          records:
            - "runtime.md#rt-rte-concept-create"
            - "epistemic.md#epi-clm-knowledge-recording"
          note: "Classifies the prescribed human decision, not every flagged invocation."
        -
          scope: "Actual flagged creates, initial/directly edited rules/concepts, registry and autosync policy initialization or replacement"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-concept-create"
            - "memory.md#mem-obj-wiki-registry"
            - "memory.md#mem-obj-wiki-autosync"
            - "runtime.md#rt-obj-append-system-prompt"
          note: "Flags and generic callers do not resolve whether a human supplied, edited or approved that particular content."
      records:
        - "runtime.md#rt-rte-concept-create"
        - "runtime.md#rt-rte-concept-update"
        - "epistemic.md#epi-clm-knowledge-recording"
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-rte-bundle-migration"
        - "memory.md#mem-rte-index-refresh"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-concept-metadata"
        - "memory.md#mem-obj-wiki-cloud"
        - "memory.md#mem-obj-wiki-autosync"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-obj-wiki-registry"
        - "runtime.md#rt-obj-append-system-prompt"
      note: "Software admissions are established independently of physical I/O. Actual human approval and generic caller-controlled initialization remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Existing concept body/metadata revision"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-concept-update"
              note: "Existing body can be replaced and fields merged."
          records:
            - "runtime.md#rt-rte-concept-update"
          note: "Caller-directed overwrite/merge revises retained entries."
        -
          scope: "Directory lifecycle withdrawal"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-directory-deprecation"
              note: "Retained deprecated status withdraws recommended reliance without deleting the entry."
          records:
            - "memory.md#mem-rte-directory-deprecation"
          note: "History/body remain; ordinary retrieval does not enforce withdrawal."
        -
          scope: "External semantic synthesis/repair and unenumerated remote reconciliation transformations"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-remote-sync"
            - "memory.md#mem-rte-bundle-diagnostics"
          note: "The records do not establish the actual semantic operation performed by external agents or enumerate all sync/adopt branches; index rebuild and existence checks add no curation value."
      records:
        - "runtime.md#rt-rte-concept-update"
        - "memory.md#mem-rte-directory-deprecation"
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-remote-sync"
        - "memory.md#mem-rte-bundle-diagnostics"
      note: "Implemented replacement and soft withdrawal are classified; requested semantic work and exhaustive remote reconciliation do not establish a complete operation inventory."
    read_back_direction:
      assessment: "known"
      units:
        -
          scope: "Requested list/search/get/rules and explicit source/navigation/recovery reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-bundle-read"
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-obj-reference-source"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-wiki-cloud"
              note: "Bundle and explicit rule requests return selected retained content to the requesting host."
            -
              value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-bundle-read"
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-obj-reference-source"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-wiki-cloud"
              note: "File navigation and explicit recovery/resource reads can obtain retained material outside ordinary graph results."
          records:
            - "runtime.md#rt-rte-bundle-read"
            - "runtime.md#rt-rte-context-delivery"
            - "memory.md#mem-obj-reference-source"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-wiki-cloud"
          note: "Tool retrieval is wired; separate file/resource consumption is an affordance."
        -
          scope: "Lifecycle/initialize instruction injection"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
              note: "Host lifecycle hooks/context builders collect instructions for later host invocations."
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "Code independently supplies retained APPEND material without a specific request for those files."
        -
          scope: "Automatic scoped CLI rule appendix on get/create/update"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-rte-bundle-read"
              note: "The CLI independently appends retained APPEND ancestor text and AGENTS gate sections to concept or mutation output; those rule files were not requested."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-rte-bundle-read"
          note: "Get's requested body remains pull. Create/update results and get output separately carry this automatic rule delivery, subject to silent appendix failure."
      records:
        - "runtime.md#rt-rte-bundle-read"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-obj-reference-source"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-wiki-cloud"
      note: "Requested content returns, broad lifecycle injection and automatic CLI rule appendices are distinct operations. The appendix is push even when attached to a requested concept or mutation result. External host compaction and hypothetical deployed file readers are excluded."
    read_back_signal:
      assessment: "known"
      units:
        -
          scope: "APPEND collection on host lifecycle/initialize or changed Codex submissions"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
              note: "Root and nonhidden directory rule files are broadly collected, budgeted and sometimes suppressed unchanged; no task-targeted identity match selects delivered content."
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "Trigger is lifecycle/initialize; inputs are selected bundle, file availability, directory order, caps/cache and rendered digest; selected parts are broad retained APPEND text."
        -
          scope: "Directory-ancestor selection of automatic CLI get/create/update rule appendices"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-rte-bundle-read"
              note: "The operated-on concept's directory identifies its root-to-directory ancestor chain; matching ancestor locations select delivered APPEND text and AGENTS gate sections."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-rte-bundle-read"
          note: "Trigger is CLI get/create/update output. Selection input is the target directory, not merely a displayed concept ID: the ancestor match selects actual retained rule parts. APPEND text is included in full for that chain; AGENTS prose outside gate sections is omitted. Appendix errors can suppress delivery."
      records:
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-rte-bundle-read"
      note: "Inventory includes broad lifecycle collection (coarse) and directory-ancestor CLI appendix selection (identifier). Requested query/ID selection of concept content remains pull; it does not erase the separate automatic rule selection."
    trace_learning:
      assessment: "not-determinable"
      units:
        -
          scope: "External agent investigation/root-cause to retained concept and later retrieval"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-concept-body"
            - "runtime.md#rt-rte-concept-create"
            - "epistemic.md#epi-clm-knowledge-recording"
          note: "Guidance requests recording discoveries, but records do not identify consumed recorded session/tool/event/trajectory inputs for the semantic producer. No automatic trace-fed transformation is established merely by the write API."
        -
          scope: "Operational log, autosync outcomes, ledger and digest maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-wiki-autosync"
            - "memory.md#mem-obj-wiki-cloud"
            - "runtime.md#rt-rte-context-delivery"
          note: "Outcome retention and scheduling/suppression control are documented, not a qualifying durable behavior-shaping trace transformation. With no evidenced-absence declaration, no controlled no is assigned."
      records:
        - "memory.md#mem-obj-concept-body"
        - "runtime.md#rt-rte-concept-create"
        - "epistemic.md#epi-clm-knowledge-recording"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-wiki-autosync"
        - "memory.md#mem-obj-wiki-cloud"
        - "runtime.md#rt-rte-context-delivery"
      note: "No bounded absence record supports a local no. A caller-mediated experience-recording affordance lacks a specified original trace-fed write chain sufficient to classify yes."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Caller-mediated experience recording and operational-state alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-concept-body"
            - "memory.md#mem-obj-reference-source"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-wiki-autosync"
            - "epistemic.md#epi-clm-knowledge-recording"
          note: "A source path, task discovery or operation entry does not establish which original recorded activity fed a qualifying update; no trace source value is asserted."
      records:
        - "memory.md#mem-obj-concept-body"
        - "memory.md#mem-obj-reference-source"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-wiki-autosync"
        - "epistemic.md#epi-clm-knowledge-recording"
      note: "Original trace inputs are not established for a qualifying automatic learning write; unresolved learning prevents inapplicability."
---

# llm-wiki memory profile

## Comparison rationale

This profile classifies accepted records, not fresh source evidence. No source files were read. Wiring supports persistence, selectors and delivery, not observed compliance or benefit.

Raw source and conditional excerpt are separate units. [MEM-OBJ-reference-source](memory.md#mem-obj-reference-source) is the canonical raw asset after reconciliation; [EPI-OBJ-derived-reference](epistemic.md#epi-obj-derived-reference) remains the conditional concept part. A readable copied Markdown source can skip generation of the latter. Arbitrary resource encoding and initial provenance therefore remain unresolved rather than inheriting the excerpt's readable display.

Reconciliation also makes [MEM-RTE-directory-deprecation](memory.md#mem-rte-directory-deprecation) and [MEM-RTE-index-refresh](memory.md#mem-rte-index-refresh) canonical for the duplicate retirement and refresh routes. Soft withdrawal supports invalidate even though search/get still deliver the body. Index regeneration is not consolidation or synthesis; standalone refresh does not imply a change-log write. Neither operation establishes acceptance of domain claims.

Retained text is a ranking input at lexical search and knowledge at the answering host. Editable rule prose supplies instruction, while the parsed AGENTS type list supplies validation and an enforced create veto. These do not make optional diagnostics a retained universal admission policy. Confirmation flags establish neither an authenticated human decision nor fresh approval of revised bodies ([RT-RTE-concept-create](runtime.md#rt-rte-concept-create), [RT-RTE-concept-update](runtime.md#rt-rte-concept-update)).

The lifecycle push is broad, budgeted rule collection with a coarse signal. Requested search/get content and explicit rules calls remain pull. CLI get/create/update additionally push a scoped rule appendix without a request for those rule files. Its target-directory ancestor match selects actual retained APPEND files and AGENTS gate sections, supporting identifier selection independently of the requested concept return. The appendix omits other AGENTS prose and may silently fail; these limits do not turn it into a requested rules return. A session-keyed digest only suppresses unchanged lifecycle text and does not itself establish identifier-based targeting ([RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-bundle-read](runtime.md#rt-rte-bundle-read)).

The records retain a caller-mediated experience-recording affordance, not a specified recorded-trace-to-derived-memory producer. [EPI-CLM-knowledge-recording](epistemic.md#epi-clm-knowledge-recording) requests investigation and recording; it does not name the original recorded inputs consumed by the external semantic producer. Operation logs and counters alone do not supply that missing chain. No member declares an evidenced absence, so neither trace-learning no nor trace-source inapplicability is warranted. These limits do not deny persistence, the recording affordance or possible host learning.
