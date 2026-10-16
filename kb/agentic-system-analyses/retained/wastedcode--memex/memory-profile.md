---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memex memory comparison of retained wiki products, archive, histories, mutable configuration and unresolved external auxiliary state."
run-id: "AAS-2026-10-14-memex-42ecde52cc05-01"
source-identity: "https://github.com/wastedcode/memex"
reviewed-boundary: "1e223b6045be31b70b1ab9e4b28dd403150d29e7"
memory-comparison:
  version: 2
  scope: "Includes raw archive, model-changeable wiki pages/schema/index/activity log, retained queue payload/results/audit events, mutable per-wiki instruction/tool/model/MCP configuration and unresolved use-accumulated external auxiliary/checkpoint alternatives. Includes their write, maintenance, replay, requested file/client read and configuration delivery routes. Excludes bundled static prompts, current-run transient context, credentials as access metadata, and model weights with no established Memex use-fed update; external provider internals are not attributed to Memex."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Raw archive, derived pages, schema, index and activity log"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-schema"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-wiki-pages"
              note: "Scaffold/upload create files and delegated Write/Edit admits surviving markdown effects."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-obj-schema"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
          note: "All named local products persist as files; model-created instances are not supplied."
        - scope: "Queue payload/results and daemon audit rows"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-queue-jobs"
                - "memory.md#mem-obj-audit-log"
              note: "Rows persist in memex.db and are reloaded or displayed."
          records:
            - "runtime.md#rt-obj-queue-jobs"
            - "memory.md#mem-obj-audit-log"
          note: "These distinct retained objects share SQLite persistence."
        - scope: "Mutable custom guidance, allowed-tool lines and MCP configuration"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-config-change"
              note: "The runner reloads disk tool configuration and passes an existing MCP file path; custom text is editable on disk."
          records:
            - "runtime.md#rt-rte-config-change"
          note: "Configuration files are distinct from bundled static policy."
        - scope: "Per-wiki model selection retained in registry"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-config-change"
              note: "Owner configuration stores model choice for later runner resolution."
          records:
            - "runtime.md#rt-rte-config-change"
          note: "The model string is registry state, not retained model weights."
        - scope: "Included external Claude auxiliary/checkpoint state and configured MCP alternatives: storage"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-config-change"
            - "runtime.md#rt-rte-job-recovery"
          note: "The accepted annotations leave provider-managed directory state, internal context retention and configured MCP behavior uninspected. No controlled value or exhaustive route inventory follows."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-wiki-pages"
        - "memory.md#mem-obj-schema"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-obj-queue-jobs"
        - "memory.md#mem-obj-audit-log"
        - "runtime.md#rt-rte-config-change"
        - "runtime.md#rt-rte-job-recovery"
      note: "The inventory covers wiki products, archive, operational histories and mutable configuration. Local stores are classified; included opaque external retained alternatives prevent complete substrate coverage."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Derived page assertions/links, schema conventions, index summaries and activity descriptions at model/reader consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-wiki-pages"
                - "memory.md#mem-obj-schema"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
              note: "The requested products carry prose facts, filing guidance, semantic navigation and operation descriptions."
          records:
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-obj-schema"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
          note: "Model-interpreted links/counts do not acquire symbolic form merely through Markdown syntax."
        - scope: "Queue control columns/envelopes and audit IDs/action/timestamps"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-queue-jobs"
                - "memory.md#mem-obj-audit-log"
              note: "IDs, status and envelopes have fixed computational interpretation."
          records:
            - "runtime.md#rt-obj-queue-jobs"
            - "memory.md#mem-obj-audit-log"
          note: "Fixed scheduler/status/display rules consume localized fields."
        - scope: "Embedded task/history and returned answer/report/detail text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-queue-jobs"
                - "memory.md#mem-obj-audit-log"
              note: "Task strings reach Claude and retained output/detail text reaches readers."
          records:
            - "runtime.md#rt-obj-queue-jobs"
            - "memory.md#mem-obj-audit-log"
          note: "These parts differ from the enclosing control fields."
        - scope: "Allowed-tool lines, model name and MCP configuration envelope"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-config-change"
              note: "Runner filters tool names and supplies model/configuration arguments."
          records:
            - "runtime.md#rt-rte-config-change"
          note: "Fixed name filtering and invocation arguments consume symbolic metadata; MCP semantics are a separate unresolved part."
        - scope: "Mutable .claude.md convention text"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-config-change"
              note: "The editor surface permits natural-language custom instructions."
          records:
            - "runtime.md#rt-rte-config-change"
          note: "Text form is established even though external discovery is uninspected."
        - scope: "Caller-uploaded archive formats and external interpretation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw"
          note: "Files may contain prose, images or opaque PDFs. No actual input corpus establishes controlled forms of its operative contents."
        - scope: "Included external Claude auxiliary/checkpoint state and configured MCP alternatives: form and consumption"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-config-change"
            - "runtime.md#rt-rte-job-recovery"
          note: "The accepted annotations leave provider-managed directory state, internal context retention and configured MCP behavior uninspected. No controlled value or exhaustive route inventory follows."
      records:
        - "memory.md#mem-obj-wiki-pages"
        - "memory.md#mem-obj-schema"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-obj-queue-jobs"
        - "memory.md#mem-obj-audit-log"
        - "runtime.md#rt-rte-config-change"
        - "memory.md#mem-obj-raw"
        - "runtime.md#rt-rte-job-recovery"
      note: "Text and fixed-rule metadata are separated by consumption. Raw formats and external auxiliary payloads remain unresolved; no parametric memory accumulated through Memex use is established."
    lineage:
      assessment: "partial"
      units:
        - scope: "Raw archive acquisition"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw"
              note: "Local caller files are decoded from transport and stored."
          records:
            - "memory.md#mem-obj-raw"
          note: "The acquisition path preserves supplied bytes; it does not resolve their earlier provenance."
        - scope: "Model-authored page content and revised filing conventions"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-wiki-pages"
                - "memory.md#mem-obj-schema"
                - "runtime.md#rt-rte-ingest-job"
              note: "Claude is asked to formulate pages and filing conventions from supplied content and encountered patterns."
          records:
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-obj-schema"
            - "runtime.md#rt-rte-ingest-job"
          note: "Authorship here is the instructed model derivation path, not observed products or resolved source warrant."
        - scope: "Index summaries derived from retained pages"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-index"
              note: "One-line page summaries and connection descriptions are requested from existing page content."
          records:
            - "memory.md#mem-obj-index"
          note: "This is compilation of a semantic navigation map, not a captured activity trace."
        - scope: "Activity summaries and coarse audit event records"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-log"
              note: "Requested log entries describe completed ingest/query/lint activity."
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-audit-log"
              note: "Queue/route events produce timestamped lifecycle records."
          records:
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-audit-log"
          note: "Keep distinct evidence layers for model summarization and fixed event writes."
        - scope: "Default schema/index/log and customization seeds"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-schema"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-config-change"
              note: "Shipped placeholder content is copied into use-changeable files."
          records:
            - "memory.md#mem-obj-schema"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-config-change"
          note: "Known scaffold initialization does not establish later generated content."
        - scope: "Stored model output text"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-queue-jobs"
              note: "Runner extracts model result text and database retains it for clients."
          records:
            - "runtime.md#rt-obj-queue-jobs"
          note: "The result route stores generated answers, reports and possible edit reasons; it is not a complete trace."
        - scope: "Initial caller payload/history and later local configuration edits"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-obj-queue-jobs"
            - "runtime.md#rt-rte-config-change"
          note: "Caller identity and arbitrary supplied text do not establish whether content was authored, imported or trace-derived."
        - scope: "Included external Claude auxiliary/checkpoint state and configured MCP alternatives: lineage"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-config-change"
            - "runtime.md#rt-rte-job-recovery"
          note: "The accepted annotations leave provider-managed directory state, internal context retention and configured MCP behavior uninspected. No controlled value or exhaustive route inventory follows."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-wiki-pages"
        - "memory.md#mem-obj-schema"
        - "runtime.md#rt-rte-ingest-job"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-audit-log"
        - "runtime.md#rt-rte-config-change"
        - "runtime.md#rt-obj-queue-jobs"
        - "runtime.md#rt-rte-job-recovery"
      note: "Known acquisition and requested derivations coexist. Source content before upload, caller histories and external retained state have unresolved origins."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Raw sources and wiki pages at ingest/query/reader consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-raw"
                - "memory.md#mem-obj-wiki-pages"
                - "runtime.md#rt-rte-ingest-job"
                - "runtime.md#rt-rte-query-job"
              note: "Claude is asked to read sources/pages as factual context."
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-file-browse"
              note: "The file API supplies requested retained text to a reader without semantic validation."
          records:
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki-pages"
            - "runtime.md#rt-rte-ingest-job"
            - "runtime.md#rt-rte-query-job"
            - "memory.md#mem-rte-file-browse"
          note: "Content supplies reference/evidence; grounding is not an enforced truth gate."
        - scope: "Schema at future filing consumer"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-schema"
                - "memory.md#mem-bap-schema-guidance"
              note: "Retained categories/templates/heuristics guide subsequent ingest decisions."
          records:
            - "memory.md#mem-obj-schema"
            - "memory.md#mem-bap-schema-guidance"
          note: "Standing conventions are requested through file reads, not injected by the daemon."
        - scope: "Schema at lint comparison consumer"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-schema"
                - "runtime.md#rt-rte-lint-job"
              note: "Schema-pattern agreement supplies a conformity criterion for requested drift diagnosis."
          records:
            - "memory.md#mem-obj-schema"
            - "runtime.md#rt-rte-lint-job"
          note: "The model compares file patterns against retained conventions; no fixed validator enforces their truth."
        - scope: "Index at model discovery and relevance-selection consumer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-index"
              note: "Index descriptions supply contextual knowledge of the wiki."
            - value: "routing"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-index"
                - "runtime.md#rt-rte-query-job"
              note: "The retained navigation map informs selection of files to read."
            - value: "ranking"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-index"
                - "runtime.md#rt-rte-query-job"
              note: "Model relevance judgments over index descriptions influence relative page priority."
          records:
            - "memory.md#mem-obj-index"
            - "runtime.md#rt-rte-query-job"
          note: "Semantic summaries guide which pages are selected, without a daemon scorer."
        - scope: "Activity log at maintenance/file-reader consumer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-lint-job"
              note: "Lint is requested to inspect non-raw Markdown including activity history."
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-log"
                - "memory.md#mem-rte-file-browse"
              note: "Surviving log text is available by requested file delivery."
          records:
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-lint-job"
            - "memory.md#mem-rte-file-browse"
          note: "Historical descriptions are context, not approval records."
        - scope: "Queue payload/control state at scheduler and replay consumer"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-queue-jobs"
                - "runtime.md#rt-rte-job-recovery"
              note: "Status, job/wiki IDs and persisted payload choose replayed task and input."
          records:
            - "runtime.md#rt-obj-queue-jobs"
            - "runtime.md#rt-rte-job-recovery"
          note: "Use-accumulated pending work chooses continuation/input rather than warrant."
        - scope: "Returned results and audit details at later client reader"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-queue-jobs"
                - "memory.md#mem-obj-audit-log"
              note: "Status/log clients display retained answer/report/error and lifecycle details."
          records:
            - "runtime.md#rt-obj-queue-jobs"
            - "memory.md#mem-obj-audit-log"
          note: "Completion and audit metadata establish operational history, not accepted facts."
        - scope: "Allowed-tool and model configuration at next runner"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-config-change"
              note: "Filtered names and retained model string select tool/model invocation arguments."
          records:
            - "runtime.md#rt-rte-config-change"
          note: "Actual tool enforcement belongs to external Claude; Memex controls invocation selection."
        - scope: "Mutable .claude.md at intended external discovery consumer"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-config-change"
              note: "Local convention text can supply custom standing guidance through external Claude discovery."
          records:
            - "runtime.md#rt-rte-config-change"
          note: "Intended guidance is classified only at its documented affordance; activation is uninspected."
        - scope: "MCP consumed payload and provider-managed auxiliary/checkpoint state"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-config-change"
            - "runtime.md#rt-rte-job-recovery"
          note: "A supplied configuration path or credential directory does not reveal its later consumer/effects."
      records:
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-wiki-pages"
        - "runtime.md#rt-rte-ingest-job"
        - "runtime.md#rt-rte-query-job"
        - "memory.md#mem-rte-file-browse"
        - "memory.md#mem-obj-schema"
        - "memory.md#mem-bap-schema-guidance"
        - "runtime.md#rt-rte-lint-job"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-obj-queue-jobs"
        - "runtime.md#rt-rte-job-recovery"
        - "memory.md#mem-obj-audit-log"
        - "runtime.md#rt-rte-config-change"
      note: "Authority is assigned at each recorded consumer, not inferred from file names or retention alone. Opaque MCP/custom-discovery effects and auxiliary state prevent complete coverage."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Delegated page/schema/index/log writes during ingest/query/lint"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-ingest-job"
                - "runtime.md#rt-rte-query-job"
                - "runtime.md#rt-rte-lint-job"
              note: "Pre-approved Write/Edit admits model-selected effects without a human per-edit decision."
          records:
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-obj-schema"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-ingest-job"
            - "runtime.md#rt-rte-query-job"
            - "runtime.md#rt-rte-lint-job"
          note: "Starting a job is not per-content approval; prompt partitions do not add an approval gate."
        - scope: "Queue/result and coarse audit admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-queue-jobs"
                - "memory.md#mem-obj-audit-log"
                - "runtime.md#rt-rte-job-recovery"
              note: "Scheduler/result/event code admits operational updates and retained model output."
          records:
            - "runtime.md#rt-obj-queue-jobs"
            - "memory.md#mem-obj-audit-log"
            - "runtime.md#rt-rte-job-recovery"
          note: "Physical persistence follows fixed runtime rules, separate from authorship."
        - scope: "Scaffold seeds"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-schema"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-config-change"
              note: "Creation initializes use-changeable files from shipped placeholders."
          records:
            - "memory.md#mem-obj-schema"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-config-change"
          note: "Defaults are admitted by creation code, not individually approved content."
        - scope: "Owner raw upload, job/history submission, administrative withdrawal and configuration/editor replacement"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw"
            - "runtime.md#rt-obj-queue-jobs"
            - "memory.md#mem-rte-wiki-withdrawal"
            - "runtime.md#rt-rte-config-change"
          note: "The recorded owner/caller can be human or automation. An editor command and UID authorization do not establish an explicit human content decision."
        - scope: "Included external Claude auxiliary/checkpoint state and configured MCP alternatives: admission control"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-config-change"
            - "runtime.md#rt-rte-job-recovery"
          note: "The accepted annotations leave provider-managed directory state, internal context retention and configured MCP behavior uninspected. No controlled value or exhaustive route inventory follows."
      records:
        - "memory.md#mem-obj-wiki-pages"
        - "memory.md#mem-obj-schema"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-rte-ingest-job"
        - "runtime.md#rt-rte-query-job"
        - "runtime.md#rt-rte-lint-job"
        - "runtime.md#rt-obj-queue-jobs"
        - "memory.md#mem-obj-audit-log"
        - "runtime.md#rt-rte-job-recovery"
        - "runtime.md#rt-rte-config-change"
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-rte-wiki-withdrawal"
      note: "Model/software admission has positive automatic witnesses. Owner calls and editor access do not resolve human versus automation control for supplied content."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Ingest extraction into pages and compressed index"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-wiki-pages"
                - "memory.md#mem-obj-index"
                - "runtime.md#rt-rte-ingest-job"
              note: "Extraction and one-line summaries reduce input content while aiming to preserve existing claims."
          records:
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-obj-index"
            - "runtime.md#rt-rte-ingest-job"
          note: "Requested reduction of source/page claims is consolidation; compliance is unobserved."
        - scope: "Ingest revision of existing pages and schema; lint index/link/schema correction"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-wiki-pages"
                - "memory.md#mem-obj-schema"
                - "memory.md#mem-obj-index"
                - "runtime.md#rt-rte-ingest-job"
                - "runtime.md#rt-rte-lint-job"
              note: "Existing entries and filing conventions are requested to be revised."
          records:
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-obj-schema"
            - "memory.md#mem-obj-index"
            - "runtime.md#rt-rte-ingest-job"
            - "runtime.md#rt-rte-lint-job"
          note: "Route names alone do not supply the operation; recorded update instructions do."
        - scope: "Activity log recording"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-log"
          note: "The record establishes a requested append describing completed activity, not selection, compression or combination of retained memory. No controlled curation operation is established; a later lint reader does not establish retained input to the writing transformation."
        - scope: "Whole-wiki successful deletion"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-wiki-withdrawal"
              note: "The handler deletes retained files and cascades queue/audit history on successful withdrawal."
          records:
            - "memory.md#mem-rte-wiki-withdrawal"
          note: "This removes memory, not invalidate-with-history. Lost DELETE body means keep-data is not an operable preservation branch."
        - scope: "Meaning of generated page synthesis and unresolved merge/contradiction diagnoses"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-pages"
            - "runtime.md#rt-rte-ingest-job"
            - "runtime.md#rt-rte-lint-job"
          note: "No generated proposition establishes a new claim absent from inputs. Lint reports merge candidates rather than implementing an assured deduplication transformation."
        - scope: "Included external Claude auxiliary/checkpoint state and configured MCP alternatives: curation transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-config-change"
            - "runtime.md#rt-rte-job-recovery"
          note: "The accepted annotations leave provider-managed directory state, internal context retention and configured MCP behavior uninspected. No controlled value or exhaustive route inventory follows."
      records:
        - "memory.md#mem-obj-wiki-pages"
        - "memory.md#mem-obj-index"
        - "runtime.md#rt-rte-ingest-job"
        - "memory.md#mem-obj-schema"
        - "runtime.md#rt-rte-lint-job"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-rte-wiki-withdrawal"
        - "runtime.md#rt-rte-config-change"
        - "runtime.md#rt-rte-job-recovery"
      note: "Requested content transformations and wired destructive forgetting remain separate findings. Unseen model outputs prevent classifying novel synthesis; external alternatives remain uninspected."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Ingest/query/lint requested filesystem reads"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-ingest-job"
                - "runtime.md#rt-rte-query-job"
                - "runtime.md#rt-rte-lint-job"
              note: "Tasks ask Claude to read schema/index/raw/pages or all non-raw Markdown."
          records:
            - "runtime.md#rt-rte-ingest-job"
            - "runtime.md#rt-rte-query-job"
            - "runtime.md#rt-rte-lint-job"
          note: "Request, model selection and file delivery are one pull chain; path mismatch limits realized access."
        - scope: "File browsing and later stored result/audit retrieval"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-file-browse"
                - "runtime.md#rt-obj-queue-jobs"
                - "memory.md#mem-obj-audit-log"
              note: "Client requests retrieve surviving files, result rows and audit events."
          records:
            - "memory.md#mem-rte-file-browse"
            - "runtime.md#rt-obj-queue-jobs"
            - "memory.md#mem-obj-audit-log"
          note: "Exact-path reads/status/log calls fulfill consumer requests rather than automatically targeting memory."
        - scope: "Restart pending-payload consumption"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-queue-jobs"
                - "runtime.md#rt-rte-job-recovery"
              note: "Restart resets running state and pending drain rebuilds task text from persisted payload."
          records:
            - "runtime.md#rt-obj-queue-jobs"
            - "runtime.md#rt-rte-job-recovery"
          note: "Scheduler automatically reintroduces stored work into a fresh model task without a new request for that retained payload."
        - scope: "Per-job retained tool/model/MCP configuration resolution"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-config-change"
              note: "Runner supplies current tool/model selections and an existing MCP configuration path."
          records:
            - "runtime.md#rt-rte-config-change"
          note: "A job request is not a request for these retained configuration contents; the runner automatically resolves them."
        - scope: "Included external Claude auxiliary/checkpoint state and configured MCP alternatives: read-back direction, including custom instruction discovery"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-config-change"
            - "runtime.md#rt-rte-job-recovery"
          note: "The accepted annotations leave provider-managed directory state, internal context retention and configured MCP behavior uninspected. No controlled value or exhaustive route inventory follows."
      records:
        - "runtime.md#rt-rte-ingest-job"
        - "runtime.md#rt-rte-query-job"
        - "runtime.md#rt-rte-lint-job"
        - "memory.md#mem-rte-file-browse"
        - "runtime.md#rt-obj-queue-jobs"
        - "memory.md#mem-obj-audit-log"
        - "runtime.md#rt-rte-job-recovery"
        - "runtime.md#rt-rte-config-change"
      note: "Model-directed file requests and client requests are pull; fixed replay/configuration supply is push. Automatic lint scheduling alone is not another push of wiki content. External host read-back remains unresolved."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Runner configuration push: job trigger, wiki identity, selected per-wiki files/model row"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-config-change"
              note: "The job wiki selects its registry model and configuration directory, determining supplied tool/model/MCP state."
          records:
            - "runtime.md#rt-rte-config-change"
          note: "Wiki identity selects the configuration actually supplied to the next invocation."
        - scope: "MCP path push: per-job presence check"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-config-change"
              note: "Presence of .tools/mcp.json determines whether its path is supplied."
          records:
            - "runtime.md#rt-rte-config-change"
          note: "File availability is an additional coarse selector, not proof of payload interpretation."
        - scope: "Replay payload push: startup/pending-drain trigger, status/order and wiki match, selected queued payload"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-queue-jobs"
                - "runtime.md#rt-rte-job-recovery"
              note: "Running-to-pending reset and ascending pending-job order determine replay eligibility."
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-queue-jobs"
                - "runtime.md#rt-rte-job-recovery"
              note: "Per-wiki claiming selects the associated retained payload supplied in the rebuilt task."
          records:
            - "runtime.md#rt-obj-queue-jobs"
            - "runtime.md#rt-rte-job-recovery"
          note: "Status/order filtering and identity selection have separate warrants."
        - scope: "Requested file/result/audit delivery"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-ingest-job"
            - "runtime.md#rt-rte-query-job"
            - "runtime.md#rt-rte-lint-job"
            - "memory.md#mem-rte-file-browse"
            - "runtime.md#rt-obj-queue-jobs"
            - "memory.md#mem-obj-audit-log"
          note: "These pull operations have no independent push selector; exact requested paths are not identifier-push evidence."
        - scope: "Included external Claude auxiliary/checkpoint state and configured MCP alternatives: automatic selection signals"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-config-change"
            - "runtime.md#rt-rte-job-recovery"
          note: "The accepted annotations leave provider-managed directory state, internal context retention and configured MCP behavior uninspected. No controlled value or exhaustive route inventory follows."
      records:
        - "runtime.md#rt-rte-config-change"
        - "runtime.md#rt-obj-queue-jobs"
        - "runtime.md#rt-rte-job-recovery"
        - "runtime.md#rt-rte-ingest-job"
        - "runtime.md#rt-rte-query-job"
        - "runtime.md#rt-rte-lint-job"
        - "memory.md#mem-rte-file-browse"
        - "memory.md#mem-obj-audit-log"
      note: "Selectors of wired configuration/replay pushes are retained separately from requested file names. No embedding or lexical push selector is established; external discovery remains opaque."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Current filing experience to revised schema to future ingest/lint guidance"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-schema"
                - "memory.md#mem-bap-schema-guidance"
                - "runtime.md#rt-rte-ingest-job"
                - "runtime.md#rt-rte-lint-job"
              note: "Encountered filing behavior/patterns are requested to shape durable conventions for later tasks."
          records:
            - "memory.md#mem-obj-schema"
            - "memory.md#mem-bap-schema-guidance"
            - "runtime.md#rt-rte-ingest-job"
            - "runtime.md#rt-rte-lint-job"
          note: "The requested automatic policy update and later read are qualifying at the claim layer; no historical log transformer or instrumented execution is established."
        - scope: "Completed job activity to durable log summary to later maintenance/reader context"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-lint-job"
              note: "Automatic activity descriptions are requested to persist in a log included in later non-raw Markdown inspection."
          records:
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-lint-job"
            - "memory.md#mem-rte-file-browse"
          note: "A generated continuation/history summary can qualify without new knowledge; logging alone would not suffice, so retain the named later read routes."
        - scope: "Audit/job histories, mixed supplied inputs and source-driven page updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-audit-log"
            - "runtime.md#rt-obj-queue-jobs"
            - "memory.md#mem-obj-raw"
            - "memory.md#mem-obj-wiki-pages"
          note: "Raw retention is not a qualifying learned artifact. Prior results are not automatically fetched by the model, while source files/history can have unspecified trace origins; records do not supply a bounded absence warrant."
        - scope: "Included external Claude auxiliary/checkpoint state and configured MCP alternatives: trace-fed updates"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-config-change"
            - "runtime.md#rt-rte-job-recovery"
          note: "The accepted annotations leave provider-managed directory state, internal context retention and configured MCP behavior uninspected. No controlled value or exhaustive route inventory follows."
      records:
        - "memory.md#mem-obj-schema"
        - "memory.md#mem-bap-schema-guidance"
        - "runtime.md#rt-rte-ingest-job"
        - "runtime.md#rt-rte-lint-job"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-rte-file-browse"
        - "memory.md#mem-obj-audit-log"
        - "runtime.md#rt-obj-queue-jobs"
        - "memory.md#mem-obj-raw"
        - "memory.md#mem-obj-wiki-pages"
        - "runtime.md#rt-rte-config-change"
        - "runtime.md#rt-rte-job-recovery"
      note: "Schema adaptation and retained activity summaries supply requested automatic experience-to-later-context paths, not observed learning or benefit. Opaque sources/host updates prevent a complete trace-learning verdict."
    trace_source:
      assessment: "not-determinable"
      units:
        - scope: "Requested schema adaptation from supplied material and current filing experience"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-schema"
            - "runtime.md#rt-rte-ingest-job"
            - "runtime.md#rt-rte-lint-job"
          note: "The records describe mixed sources and current organization, not recorded conversational turns, tool requests/results, discrete event records or linked trajectories actually consumed by this update. No controlled trace-source value is established."
        - scope: "Requested activity-to-log summary with later maintenance consumer"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-lint-job"
          note: "The append instruction describes operation summaries, not which original event/turn/tool records feed their production. The generated log is the output, not evidence of its original trace source."
        - scope: "Other supplied-source origins and external auxiliary/MCP trace-fed writes"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw"
            - "runtime.md#rt-rte-config-change"
            - "runtime.md#rt-rte-job-recovery"
          note: "Input origin and opaque host transformations are unresolved. Retention or a directory path establishes no qualifying trace-source class."
      records:
        - "memory.md#mem-obj-schema"
        - "runtime.md#rt-rte-ingest-job"
        - "runtime.md#rt-rte-lint-job"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-raw"
        - "runtime.md#rt-rte-config-change"
        - "runtime.md#rt-rte-job-recovery"
      note: "Qualifying trace-learning paths have claim-layer support, but accepted records establish none of the four original-input classes. This is not inapplicability or evidenced absence; source content and host alternatives prevent classification."
---

# Memex memory profile

## Comparison rationale

The principal memory is retained editable text, not a resumed conversation or vector store. The archive, derived pages, schema, index, activity summaries and two distinct database histories have different consumers. [MEM-OBJ-wiki-pages](memory.md#mem-obj-wiki-pages), [MEM-OBJ-schema](memory.md#mem-obj-schema), [MEM-OBJ-index](memory.md#mem-obj-index), [MEM-OBJ-log](memory.md#mem-obj-log), [MEM-OBJ-audit-log](memory.md#mem-obj-audit-log) and [RT-OBJ-queue-jobs](runtime.md#rt-obj-queue-jobs) supply that inventory. Local substrate and fixed admission wiring do not upgrade requested semantic transformations or instruction activation.

Reconciliation supersedes the epistemic raw/page/schema/index/log declarations with their memory counterparts, the epistemic browsing route with [MEM-RTE-file-browse](memory.md#mem-rte-file-browse), and the epistemic audit-reasons claim with [MEM-CLM-reason-audit](memory.md#mem-clm-reason-audit). Those identity amendments affect citation choice, not evidence strength. [EPI-RTE-result-display](epistemic.md#epi-rte-result-display) remains a valid part of the recovery/result container, not a superseded whole-route duplicate. No superseded ID supplies a profile finding.

The file-selection chain is pull: a task asks Claude to read and choose files. Automatic lint scheduling does not inject selected pages independently. In contrast, restart code selects retained payloads for replay, and each runner automatically supplies retained configuration. Status/order availability and wiki-identity matching are distinct push signals; an exact requested file path is not another push signal. See [RT-RTE-query-job](runtime.md#rt-rte-query-job), [RT-RTE-lint-job](runtime.md#rt-rte-lint-job), [RT-RTE-job-recovery](runtime.md#rt-rte-job-recovery) and [RT-RTE-config-change](runtime.md#rt-rte-config-change).

Experience-based schema revision and generated activity summaries have claim-layer trace-learning paths to later consumers. This classification does not establish improved capacity, observed reflection, or exercised self-improvement. It also does not reveal original trace formats: the records do not identify actual session logs, tool records, discrete event inputs or trajectories consumed by these updates. Mixed raw sources and opaque host state remain included uncertainty, not evidence of a system-wide negative. See [MEM-OBJ-schema](memory.md#mem-obj-schema), [MEM-BAP-schema-guidance](memory.md#mem-bap-schema-guidance) and [MEM-OBJ-log](memory.md#mem-obj-log).

Extraction/index compression supports requested consolidation and existing-entry correction supports requested evolution. Activity recording does not establish a separate consolidation operation: [MEM-OBJ-log](memory.md#mem-obj-log) identifies no retained memory selected, compressed or combined by the append transformation. Later log consumption does not fill that input gap. The activity-log curation unit therefore retains no positive finding; its other classifications concern distinct properties and remain unchanged. A synthesis label without a concrete new proposition does not establish the curation value synthesize. [RT-RTE-ingest-job](runtime.md#rt-rte-ingest-job) and [RT-RTE-lint-job](runtime.md#rt-rte-lint-job) retain those limits. Whole-wiki deletion supplies wired forgetting, not history-preserving invalidation: [MEM-RTE-wiki-withdrawal](memory.md#mem-rte-wiki-withdrawal) establishes that the keep-data body does not reach the handler. It therefore cannot be retained as an alternative preservation route.

The scaffold/mount relative-path mismatch limits successful file access and activation; lack of traces limits observation and benefit, not the known existence of disk stores or admission mechanisms. Mutable custom-instruction discovery, MCP consumed payloads and external auxiliary/checkpoint semantics remain uninspected rather than inheriting an inspected branch's values. Generic owner identity leaves human admission unresolved. The profile excludes neither opaque alternatives nor supported positives merely to obtain complete coverage.

Source-read log: none. Classification used the supplied accepted reports and reconciliation, with the supplied previous profile as the refusal-correction baseline. No source checkout or separate incumbent/reference profile was read.
