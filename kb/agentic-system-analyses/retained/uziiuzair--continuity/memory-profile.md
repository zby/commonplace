---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Continuity memory comparison across retained desktop facts, narratives, work/history, vault context, organization and plugin state, and developer memory-bank procedures."
run-id: "AAS-2026-10-14-continuity-3e490e1d39f0-01"
source-identity: "https://github.com/uziiuzair/continuity"
reviewed-boundary: "4ca8f6b4108aa4494e3861ed33c8019dbd662c67"
memory-comparison:
  version: 2
  scope: "Included: accumulated local facts and metadata/history/projects/links, learning observations and narratives, saved messages and research products, human profile/custom instructions, journal/canvas/database/briefing state, vault files and derived index, organization rows, Threads posts/drafts/results/activity state, documented developer memory-bank updates, and unresolved provider-retained memory alternatives. Excluded: static shipped runtime prompts, current-run model/tool protocol and research windows, plugin session registrations/capability maps, volatile sync queues/cursors as current-run transport state, general runtime configuration/credentials, historical plugin database contents, external service/client implementations and actual external vault bodies. Provider inference weights are not positively classified as accumulated memory merely because they are parametric."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Local memories, access metadata, revisions, projects/links, observations, narratives and the stored vault index"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records: ["memory.md#mem-obj-memories", "memory.md#mem-obj-memory-metadata", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-memory-links", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-obj-vault-index"]
              note: "These retained objects reside in local SQLite memory.db; typed edges do not establish a separate graph storage engine."
          records: ["memory.md#mem-obj-memories", "memory.md#mem-obj-memory-metadata", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-memory-links", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-obj-vault-index"]
          note: "These retained objects reside in local SQLite memory.db; typed edges do not establish a separate graph storage engine."
        -
          scope: "Saved messages, human profile settings, journal/canvas/database blocks and briefing state"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records: ["memory.md#mem-obj-messages", "memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state"]
              note: "These parts reside in app SQLite, including research report blocks and summary messages."
          records: ["memory.md#mem-obj-messages", "memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state"]
          note: "These parts reside in app SQLite, including research report blocks and summary messages."
        -
          scope: "Organization memory rows"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
              note: "Organization SQLite storage is distinct from local memory.db; the pull-target defect does not erase server storage."
          records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
          note: "Organization SQLite storage is distinct from local memory.db; the pull-target defect does not erase server storage."
        -
          scope: "Threads retained posts, scores/reasons, drafts, engagements and search logs"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
              note: "The plugin persists these objects in threads-engagement.db."
          records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
          note: "The plugin persists these objects in threads-engagement.db."
        -
          scope: "Vault files written and later read through the shipped vault tools"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records: ["memory.md#mem-rte-vault-context"]
              note: "The tool path persists file content separately from its SQLite overview. Actual external files and scanner internals were not inspected."
          records: ["memory.md#mem-rte-vault-context"]
          note: "The tool path persists file content separately from its SQLite overview. Actual external files and scanner internals were not inspected."
        -
          scope: "Developer-agent current-context and progress Markdown"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "claimed"
              records: ["memory.md#mem-rte-developer-memory"]
              note: "The documented memory bank uses Git-tracked Markdown files; update/reload execution is only declared."
            -
              value: "repo"
              basis: "claimed"
              records: ["memory.md#mem-rte-developer-memory"]
              note: "The documented memory bank uses Git-tracked Markdown files; update/reload execution is only declared."
          records: ["memory.md#mem-rte-developer-memory"]
          note: "The documented memory bank uses Git-tracked Markdown files; update/reload execution is only declared."
        -
          scope: "Possible retained provider-internal state"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
          note: "Remote parameter storage and any provider-side retained state are inaccessible; no memory substrate classification follows."
      records: ["memory.md#mem-obj-memories", "memory.md#mem-obj-memory-metadata", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-memory-links", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-obj-vault-index", "memory.md#mem-obj-messages", "memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement", "memory.md#mem-rte-vault-context", "memory.md#mem-rte-developer-memory", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
      note: "The accepted inventory covers local memory/app databases, organization and plugin databases, vault files and developer documents. Provider-retained state remains opaque; storage of that alternative cannot be inferred from remote inference."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Fact/revision text, project descriptions, observations, narrative briefing and insight strings, vault overview at model or human readers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records: ["memory.md#mem-obj-memories", "memory.md#mem-obj-memory-metadata", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-memory-links", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-obj-vault-index"]
              note: "Natural-language meaning reaches model/human consumers; the JSON container is not a fourth form."
          records: ["memory.md#mem-obj-memories", "memory.md#mem-obj-memory-metadata", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-memory-links", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-obj-vault-index"]
          note: "Natural-language meaning reaches model/human consumers; the JSON container is not a fourth form."
        -
          scope: "Memory IDs, versions, scope/archive/time/type/source fields, project/link endpoints, absorption flags and narrative JSON access fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-memory-metadata", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-memory-links", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "epistemic.md#epi-obj-memory-source"]
              note: "SQL and fixed code consume localized metadata and container fields. Arbitrary metadata payload semantics remain separate."
          records: ["memory.md#mem-obj-memory-metadata", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-memory-links", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "epistemic.md#epi-obj-memory-source"]
          note: "SQL and fixed code consume localized metadata and container fields. Arbitrary metadata payload semantics remain separate."
        -
          scope: "Arbitrary memories.metadata payload contents and their possible consumers"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-memory-metadata"]
          note: "The container is known, but opaque caller payload semantics and consumption do not establish an exhaustive content-form classification."
        -
          scope: "Saved conversational/research prose, profile/custom directions, workspace prose and later-read vault file text"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records: ["memory.md#mem-obj-messages", "memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state", "memory.md#mem-rte-vault-context"]
              note: "Human/model interpretation consumes retained text, distinct from block and message metadata."
          records: ["memory.md#mem-obj-messages", "memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state", "memory.md#mem-rte-vault-context"]
          note: "Human/model interpretation consumes retained text, distinct from block and message metadata."
        -
          scope: "Message/thread/display fields and workspace block/date/type/link/work-state structures"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-messages", "memory.md#mem-obj-workspace-state"]
              note: "Fixed reload/projection rules consume symbolic wrappers and state."
          records: ["memory.md#mem-obj-messages", "memory.md#mem-obj-workspace-state"]
          note: "Fixed reload/projection rules consume symbolic wrappers and state."
        -
          scope: "Organization key/content and Threads post/reason/draft/error text"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
              note: "These text parts supply context, proposed replies or human review material."
          records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
          note: "These text parts supply context, proposed replies or human review material."
        -
          scope: "Organization scope/version/timestamps and Threads identities, statuses, selection flags and budget counts"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
              note: "Fixed upsert, cursor, selection and budget code consume these localized fields."
          records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
          note: "Fixed upsert, cursor, selection and budget code consume these localized fields."
        -
          scope: "Developer memory-bank Markdown at the instructed coding-agent reader"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "claimed"
              records: ["memory.md#mem-rte-developer-memory"]
              note: "Declared development guidance and summaries are natural-language memory, not desktop static instructions."
          records: ["memory.md#mem-rte-developer-memory"]
          note: "Declared development guidance and summaries are natural-language memory, not desktop static instructions."
        -
          scope: "Provider-internal retained memory representation"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
          note: "Parametric computation alone does not establish an accumulated memory representation; provider internals remain outside inspection."
      records: ["memory.md#mem-obj-memories", "memory.md#mem-obj-memory-metadata", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-memory-links", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-obj-vault-index", "epistemic.md#epi-obj-memory-source", "memory.md#mem-obj-messages", "memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state", "memory.md#mem-rte-vault-context", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement", "memory.md#mem-rte-developer-memory", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
      note: "Text and access/control parts are classified separately. Provider model computation is parametric, but the records do not establish that its weights are an accumulated memory object; provider-retained memory encoding remains uninspected."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Desktop model-proposed remembered content from conversational work"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records: ["memory.md#mem-rte-desktop-retention", "runtime.md#rt-rte-desktop-chat"]
              note: "Foreground conversation supplies the model context from which remember proposes durable facts; admission is implemented, not observed extraction quality."
          records: ["memory.md#mem-rte-desktop-retention", "runtime.md#rt-rte-desktop-chat"]
          note: "Foreground conversation supplies the model context from which remember proposes durable facts; admission is implemented, not observed extraction quality."
        -
          scope: "Explicit human profile/custom-instruction edits and journal block authorship"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records: ["memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state"]
              note: "The UI supplies actual human-authored retained content."
          records: ["memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state"]
          note: "The UI supplies actual human-authored retained content."
        -
          scope: "MCP-supplied facts, observations and caller narrative replacements; remote organization rows and fetched Threads posts"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records: ["memory.md#mem-rte-mcp-memory", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
              note: "These entry paths acquire supplied content rather than demonstrating its upstream derivation."
          records: ["memory.md#mem-rte-mcp-memory", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
          note: "These entry paths acquire supplied content rather than demonstrating its upstream derivation."
        -
          scope: "Initial authorship/derivation of generic MCP fact, observation and narrative content"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-rte-mcp-memory", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-clm-source-trust"]
          note: "Import is known on the receiving path; generic caller identity and self-reported source cannot distinguish upstream human authorship, trace extraction or compilation."
        -
          scope: "Automatically saved narrative model output from facts, observations and prior briefing"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records: ["memory.md#mem-rte-narrative-synthesis", "epistemic.md#epi-rte-narrative-generation"]
              note: "The inspected derivation compiles retained inputs through a model call; original conversational provenance of observations is unresolved."
          records: ["memory.md#mem-rte-narrative-synthesis", "epistemic.md#epi-rte-narrative-generation"]
          note: "The inspected derivation compiles retained inputs through a model call; original conversational provenance of observations is unresolved."
        -
          scope: "Vault scan overview, incremental index formatting and deterministic briefing projection"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records: ["memory.md#mem-obj-vault-index", "memory.md#mem-rte-vault-context", "memory.md#mem-obj-workspace-state"]
              note: "Code projects scan or retained workspace material into another representation; an index is not a raw vault snapshot."
          records: ["memory.md#mem-obj-vault-index", "memory.md#mem-rte-vault-context", "memory.md#mem-obj-workspace-state"]
          note: "Code projects scan or retained workspace material into another representation; an index is not a raw vault snapshot."
        -
          scope: "Saved conversation role/content and display projection"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records: ["memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat"]
              note: "Persistence records user/assistant conversational activity for later thread use."
          records: ["memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat"]
          note: "Persistence records user/assistant conversational activity for later thread use."
        -
          scope: "Research summary/report and Threads generated reasons/drafts"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records: ["runtime.md#rt-rte-deep-research", "epistemic.md#epi-rte-research-findings", "memory.md#mem-obj-threads-results"]
              note: "Model-produced retained work products compile acquired content; external answers and fallback excerpts remain distinct input branches."
          records: ["runtime.md#rt-rte-deep-research", "epistemic.md#epi-rte-research-findings", "memory.md#mem-obj-threads-results"]
          note: "Model-produced retained work products compile acquired content; external answers and fallback excerpts remain distinct input branches."
        -
          scope: "Threads engagement/error and search activity records"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
              note: "These retained records derive from API outcomes and scan activity, not from a demonstrated training update."
          records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
          note: "These retained records derive from API outcomes and scan activity, not from a demonstrated training update."
        -
          scope: "Developer task-end current-context/progress summaries"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "claimed"
              records: ["memory.md#mem-rte-developer-memory"]
              note: "The maintenance doctrine requests summaries of completed development work for later sessions."
          records: ["memory.md#mem-rte-developer-memory"]
          note: "The maintenance doctrine requests summaries of completed development work for later sessions."
        -
          scope: "Complete canvas/database and journal-auto-link derivation; initial developer document provenance; provider-retained state"
          assessment: "uninspected"
          findings: []
          records: ["memory.md#mem-obj-workspace-state", "memory.md#mem-rte-developer-memory", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
          note: "The records do not resolve all producers or original inputs of these included alternatives."
      records: ["memory.md#mem-rte-desktop-retention", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state", "memory.md#mem-rte-mcp-memory", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement", "memory.md#mem-clm-source-trust", "memory.md#mem-rte-narrative-synthesis", "epistemic.md#epi-rte-narrative-generation", "memory.md#mem-obj-vault-index", "memory.md#mem-rte-vault-context", "memory.md#mem-obj-messages", "runtime.md#rt-rte-deep-research", "epistemic.md#epi-rte-research-findings", "memory.md#mem-rte-developer-memory", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
      note: "Known derivation paths do not resolve all initial provenance. Caller-set source labels and optional source IDs are not authorship evidence; opaque provider state and uninspected workspace paths remain included."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Active fact text and vault overview at foreground/tool-result readers; revisions, projects and links at requested UI/MCP readers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records: ["memory.md#mem-obj-memories", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-memory-links", "memory.md#mem-rte-passive-context", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-vault-context", "epistemic.md#epi-rte-relation-retention"]
              note: "Retained content supplies context/reference or advisory relationship/history display; typed relations do not adjudicate truth."
          records: ["memory.md#mem-obj-memories", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-memory-links", "memory.md#mem-rte-passive-context", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-vault-context", "epistemic.md#epi-rte-relation-retention"]
          note: "Retained content supplies context/reference or advisory relationship/history display; typed relations do not adjudicate truth."
        -
          scope: "Passive preference/constraint content and human custom instructions at the foreground model"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records: ["memory.md#mem-rte-passive-context", "memory.md#mem-rte-profile-context", "runtime.md#rt-bap-system-guidance"]
              note: "The system-message path supplies behavioral directions through natural-language interpretation, without deterministic enforcement."
          records: ["memory.md#mem-rte-passive-context", "memory.md#mem-rte-profile-context", "runtime.md#rt-bap-system-guidance"]
          note: "The system-message path supplies behavioral directions through natural-language interpretation, without deterministic enforcement."
        -
          scope: "Narrative briefing at foreground and prior-content reader; observation text at synthesis"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records: ["memory.md#mem-obj-narratives", "memory.md#mem-obj-learnings", "epistemic.md#epi-rte-narrative-consumption", "memory.md#mem-rte-narrative-synthesis"]
              note: "These parts supply context and evidence-like input. Self-reported confidence is not factual validation."
          records: ["memory.md#mem-obj-narratives", "memory.md#mem-obj-learnings", "epistemic.md#epi-rte-narrative-consumption", "memory.md#mem-rte-narrative-synthesis"]
          note: "These parts supply context and evidence-like input. Self-reported confidence is not factual validation."
        -
          scope: "Retained observations at automatic narrative update consumer"
          assessment: "partial"
          findings:
            -
              value: "learning"
              basis: "wired"
              records: ["memory.md#mem-obj-learnings", "memory.md#mem-rte-narrative-synthesis"]
              note: "The recorded observation-to-narrative-to-later-context path feeds experience interpretations into a durable behavior-shaping artifact; it does not establish improvement."
          records: ["memory.md#mem-obj-learnings", "memory.md#mem-rte-narrative-synthesis"]
          note: "Conversation-derived observations can shape a durable briefing, but optional source IDs do not establish the origin of every admitted observation."
        -
          scope: "Saved conversational content at later foreground sends, including the model remember proposal consumer"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records: ["memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention"]
              note: "Later history supplies context and can feed automatic durable fact writes; raw storage alone would not establish the update effect."
            -
              value: "learning"
              basis: "wired"
              records: ["memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention"]
              note: "Later history supplies context and can feed automatic durable fact writes; raw storage alone would not establish the update effect."
          records: ["memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention"]
          note: "Later history supplies context and can feed automatic durable fact writes; raw storage alone would not establish the update effect."
        -
          scope: "Archive state at active recall/passive/synthesis selection"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records: ["memory.md#mem-obj-memory-metadata", "epistemic.md#epi-rte-memory-withdrawal"]
              note: "The retained archive flag enforces exclusion from these active reads, not derivative forgetting."
          records: ["memory.md#mem-obj-memory-metadata", "epistemic.md#epi-rte-memory-withdrawal"]
          note: "The retained archive flag enforces exclusion from these active reads, not derivative forgetting."
        -
          scope: "Retained memory recency/type fields at passive top-50/type-order selection"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records: ["memory.md#mem-obj-memory-metadata", "memory.md#mem-rte-passive-context"]
              note: "Retained features influence relative delivery priority under fixed code."
          records: ["memory.md#mem-obj-memory-metadata", "memory.md#mem-rte-passive-context"]
          note: "Retained features influence relative delivery priority under fixed code."
        -
          scope: "Retained scope/identity fields, learning pending state and narrative snapshot at retrieval/synthesis selection"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records: ["memory.md#mem-obj-memory-metadata", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-rte-narrative-synthesis"]
              note: "IDs/scopes select retained inputs; pending count/hash can select or suppress subsequent synthesis."
          records: ["memory.md#mem-obj-memory-metadata", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-rte-narrative-synthesis"]
          note: "IDs/scopes select retained inputs; pending count/hash can select or suppress subsequent synthesis."
        -
          scope: "Existing retained memory endpoints at relationship admission"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records: ["epistemic.md#epi-rte-relation-retention"]
              note: "Stored endpoint existence is checked as a candidate-edge admission criterion and absence blocks the edge. This validates identifiers, not relation truth."
            -
              value: "enforcement"
              basis: "wired"
              records: ["epistemic.md#epi-rte-relation-retention"]
              note: "Stored endpoint existence is checked as a candidate-edge admission criterion and absence blocks the edge. This validates identifiers, not relation truth."
          records: ["epistemic.md#epi-rte-relation-retention"]
          note: "Stored endpoint existence is checked as a candidate-edge admission criterion and absence blocks the edge. This validates identifiers, not relation truth."
        -
          scope: "Workspace prose/projections and retained Threads drafts/reasons at human review or later chat history"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records: ["memory.md#mem-obj-workspace-state", "memory.md#mem-obj-threads-results", "memory.md#mem-obj-messages"]
              note: "These consumers receive reference material or candidate work; no endorsement follows from availability."
          records: ["memory.md#mem-obj-workspace-state", "memory.md#mem-obj-threads-results", "memory.md#mem-obj-messages"]
          note: "These consumers receive reference material or candidate work; no endorsement follows from availability."
        -
          scope: "Threads stored draft-selection flags and post IDs at later approval/dedup consumers"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
              note: "Selection state routes the draft for publication; stored post identity prevents duplicate queue work."
            -
              value: "enforcement"
              basis: "wired"
              records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
              note: "Selection state routes the draft for publication; stored post identity prevents duplicate queue work."
          records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
          note: "Selection state routes the draft for publication; stored post identity prevents duplicate queue work."
        -
          scope: "Threads retained search-log counts at scan budget checks"
          assessment: "known"
          findings:
            -
              value: "enforcement"
              basis: "wired"
              records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
              note: "Recorded search activity blocks scans beyond the configured rolling budget."
          records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
          note: "Recorded search activity blocks scans beyond the configured rolling budget."
        -
          scope: "Organization retained timestamp at server conflict admission"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
              note: "Existing updated_at is the validation criterion for a candidate replacement and enforces the timestamp guard."
            -
              value: "enforcement"
              basis: "wired"
              records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
              note: "Existing updated_at is the validation criterion for a candidate replacement and enforces the timestamp guard."
          records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
          note: "Existing updated_at is the validation criterion for a candidate replacement and enforces the timestamp guard."
        -
          scope: "Organization retained rows at requested server pull/search delivery"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
              note: "The server returns knowledge; the defective desktop pull target and missing tool discovery do not prove foreground consumption."
          records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
          note: "The server returns knowledge; the defective desktop pull target and missing tool discovery do not prove foreground consumption."
        -
          scope: "Developer memory-bank summaries/directions at the instructed external agent"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "claimed"
              records: ["memory.md#mem-rte-developer-memory"]
              note: "The documented reader receives task context and maintenance directions; actual loading/compliance is unobserved."
            -
              value: "instruction"
              basis: "claimed"
              records: ["memory.md#mem-rte-developer-memory"]
              note: "The documented reader receives task context and maintenance directions; actual loading/compliance is unobserved."
          records: ["memory.md#mem-rte-developer-memory"]
          note: "The documented reader receives task context and maintenance directions; actual loading/compliance is unobserved."
        -
          scope: "Arbitrary metadata consumers, richer canvas/journal-auto-link paths and provider-internal memory consumers"
          assessment: "uninspected"
          findings: []
          records: ["memory.md#mem-obj-memory-metadata", "memory.md#mem-obj-workspace-state", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
          note: "Missing actual consumers/effects prevent additional authority classification."
      records: ["memory.md#mem-obj-memories", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-memory-links", "memory.md#mem-rte-passive-context", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-vault-context", "epistemic.md#epi-rte-relation-retention", "memory.md#mem-rte-profile-context", "runtime.md#rt-bap-system-guidance", "memory.md#mem-obj-narratives", "memory.md#mem-obj-learnings", "epistemic.md#epi-rte-narrative-consumption", "memory.md#mem-rte-narrative-synthesis", "memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-obj-memory-metadata", "epistemic.md#epi-rte-memory-withdrawal", "memory.md#mem-obj-workspace-state", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-rte-developer-memory", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
      note: "Authority belongs to each retained part at its consumer, not to the database as a whole. Text delivery is not compliance; organization/plugin discovery and opaque workspace/provider consumers prevent complete enumeration."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Desktop remember/forget model dispatch"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records: ["memory.md#mem-rte-desktop-retention"]
              note: "Code persists model-proposed content without an item-specific human confirmation gate."
          records: ["memory.md#mem-rte-desktop-retention"]
          note: "Code persists model-proposed content without an item-specific human confirmation gate."
        -
          scope: "Scheduled or manually launched narrative replacement"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records: ["memory.md#mem-rte-narrative-synthesis", "epistemic.md#epi-rte-narrative-retention"]
              note: "Model output, including fallback text, is admitted automatically. Synthesize initiation is not output approval."
          records: ["memory.md#mem-rte-narrative-synthesis", "epistemic.md#epi-rte-narrative-retention"]
          note: "Model output, including fallback text, is admitted automatically. Synthesize initiation is not output approval."
        -
          scope: "Scan-to-vault-index projection and model-requested file/index updates"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records: ["memory.md#mem-rte-vault-context"]
              note: "A scan initiation or approval request in prompt text is not per-output content approval in the executor."
          records: ["memory.md#mem-rte-vault-context"]
          note: "A scan initiation or approval request in prompt text is not per-output content approval in the executor."
        -
          scope: "Conversation saves and research completion report/summary writes"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records: ["runtime.md#rt-rte-desktop-chat", "runtime.md#rt-rte-deep-research", "memory.md#mem-obj-messages"]
              note: "The driver and callbacks admit output without per-content review; callback success is not observed."
          records: ["runtime.md#rt-rte-desktop-chat", "runtime.md#rt-rte-deep-research", "memory.md#mem-obj-messages"]
          note: "The driver and callbacks admit output without per-content review; callback success is not observed."
        -
          scope: "Human profile/custom-instruction save and journal block edit"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "wired"
              records: ["memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state"]
              note: "An explicit human decision supplies/edits this retained content; debounce/SQL does not change admission agency."
          records: ["memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state"]
          note: "An explicit human decision supplies/edits this retained content; debounce/SQL does not change admission agency."
        -
          scope: "Threads scheduled post/score/draft and outcome/log admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement", "epistemic.md#epi-rte-threads-retention"]
              note: "Code admits generated drafts and records activity/outcomes without individual human content approval."
          records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement", "epistemic.md#epi-rte-threads-retention"]
          note: "Code admits generated drafts and records activity/outcomes without individual human content approval."
        -
          scope: "Threads draft editing/selection through the intended human review surface"
          assessment: "known"
          findings:
            -
              value: "manual"
              basis: "afforded"
              records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
              note: "The review UI affords a human per-content edit/choice, distinct from any generic endpoint caller."
          records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
          note: "The review UI affords a human per-content edit/choice, distinct from any generic endpoint caller."
        -
          scope: "MCP memory/project/link/learning/narrative admission and generic Threads edit/select endpoint callers"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-rte-mcp-memory", "epistemic.md#epi-rte-signal-retention", "epistemic.md#epi-rte-threads-publication"]
          note: "Caller-supplied content and available endpoints do not identify whether a human selected that content or software did."
        -
          scope: "Organization server upsert and plugin pull admission"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
              note: "Code checks schema/timestamp and applies rows without per-content human approval; intended local database integration is defective."
          records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
          note: "Code checks schema/timestamp and applies rows without per-content human approval; intended local database integration is defective."
        -
          scope: "Developer document update control and incompletely traced canvas/database/journal-auto-link producers"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-rte-developer-memory", "memory.md#mem-obj-workspace-state"]
          note: "Maintenance instructions do not establish content approval control; complete alternative workspace admission routes are not recorded."
        -
          scope: "Provider-retained memory admission"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
          note: "The inference adapters do not expose provider memory/weight write control."
      records: ["memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-narrative-synthesis", "epistemic.md#epi-rte-narrative-retention", "memory.md#mem-rte-vault-context", "runtime.md#rt-rte-desktop-chat", "runtime.md#rt-rte-deep-research", "memory.md#mem-obj-messages", "memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement", "epistemic.md#epi-rte-threads-retention", "memory.md#mem-rte-mcp-memory", "epistemic.md#epi-rte-signal-retention", "epistemic.md#epi-rte-threads-publication", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-rte-developer-memory", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
      note: "Software/model admission is automatic even after manual launch. Generic MCP/HTTP caller identity does not prove human per-content control; explicit human editing is classified only on its own surface."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Existing keyed memory content replacement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records: ["memory.md#mem-rte-desktop-retention", "epistemic.md#epi-rte-memory-retention", "memory.md#mem-obj-memory-versions"]
              note: "Updates revise the existing entry and preserve fact content snapshots; this is evolution, not truth acceptance."
          records: ["memory.md#mem-rte-desktop-retention", "epistemic.md#epi-rte-memory-retention", "memory.md#mem-obj-memory-versions"]
          note: "Updates revise the existing entry and preserve fact content snapshots; this is evolution, not truth acceptance."
        -
          scope: "Memory archive and active-read predicates"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records: ["epistemic.md#epi-rte-memory-withdrawal", "memory.md#mem-rte-desktop-retention"]
              note: "Archival withdraws active reliance while retained content/history remain. It does not retract narrative derivatives or remote copies."
          records: ["epistemic.md#epi-rte-memory-withdrawal", "memory.md#mem-rte-desktop-retention"]
          note: "Archival withdraws active reliance while retained content/history remain. It does not retract narrative derivatives or remote copies."
        -
          scope: "Vault index rescan and incremental existing-index edits"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records: ["memory.md#mem-obj-vault-index", "epistemic.md#epi-rte-vault-projection"]
              note: "The stored overview is a reduced selection of existing scan claims; rescans and line replacements revise the existing index. Lossy defects do not establish novel claim synthesis."
            -
              value: "evolve"
              basis: "wired"
              records: ["memory.md#mem-obj-vault-index", "epistemic.md#epi-rte-vault-projection"]
              note: "The stored overview is a reduced selection of existing scan claims; rescans and line replacements revise the existing index. Lossy defects do not establish novel claim synthesis."
          records: ["memory.md#mem-obj-vault-index", "epistemic.md#epi-rte-vault-projection"]
          note: "The stored overview is a reduced selection of existing scan claims; rescans and line replacements revise the existing index. Lossy defects do not establish novel claim synthesis."
        -
          scope: "Automatic narrative current-entry replacement and semantic transformation"
          assessment: "partial"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records: ["memory.md#mem-rte-narrative-synthesis", "epistemic.md#epi-rte-narrative-retention"]
              note: "The current narrative is replaced in place, including a raw-response fallback; its version is not stored rollback history."
          records: ["memory.md#mem-rte-narrative-synthesis", "epistemic.md#epi-rte-narrative-generation", "epistemic.md#epi-rte-narrative-retention"]
          note: "Current-row evolution is wired, but no premise/output instance distinguishes compression, entailed derivation and novel claim creation. Requested contradiction handling is not enforced curation."
        -
          scope: "Human saved profile replacement and existing journal content edits"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records: ["memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state"]
              note: "These explicit edits revise retained entries. Emptying/clearing alone does not establish history-retaining invalidation."
          records: ["memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state"]
          note: "These explicit edits revise retained entries. Emptying/clearing alone does not establish history-retaining invalidation."
        -
          scope: "Threads retained draft editing"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records: ["memory.md#mem-obj-threads-results", "epistemic.md#epi-rte-threads-retention"]
              note: "The implemented string-edit path revises an existing candidate; regeneration deletion is not semantic deduplication."
          records: ["memory.md#mem-obj-threads-results", "epistemic.md#epi-rte-threads-retention"]
          note: "The implemented string-edit path revises an existing candidate; regeneration deletion is not semantic deduplication."
        -
          scope: "Organization current-row timestamp-guarded replacement"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
              note: "Upsert revises current content. Missing tombstones prevent interpreting sync deletion as remote invalidation."
          records: ["memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
          note: "Upsert revises current content. Missing tombstones prevent interpreting sync deletion as remote invalidation."
        -
          scope: "Developer current-context task-end revision"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "claimed"
              records: ["memory.md#mem-rte-developer-memory"]
              note: "Doctrine requests updating current-state prose and progress; it does not prove the requested operation occurred."
          records: ["memory.md#mem-rte-developer-memory"]
          note: "Doctrine requests updating current-state prose and progress; it does not prove the requested operation occurred."
        -
          scope: "Research output semantics, generic caller transformations and richer canvas/journal-auto-link maintenance"
          assessment: "not-determinable"
          findings: []
          records: ["epistemic.md#epi-rte-research-findings", "memory.md#mem-rte-mcp-memory", "memory.md#mem-obj-workspace-state"]
          note: "Recorded production and retention do not establish a specific additional curation operation."
        -
          scope: "Provider-internal memory maintenance"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
          note: "Opaque provider behavior prevents curation classification."
      records: ["memory.md#mem-rte-desktop-retention", "epistemic.md#epi-rte-memory-retention", "memory.md#mem-obj-memory-versions", "epistemic.md#epi-rte-memory-withdrawal", "memory.md#mem-obj-vault-index", "epistemic.md#epi-rte-vault-projection", "memory.md#mem-rte-narrative-synthesis", "epistemic.md#epi-rte-narrative-generation", "epistemic.md#epi-rte-narrative-retention", "memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state", "memory.md#mem-obj-threads-results", "epistemic.md#epi-rte-threads-retention", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-rte-developer-memory", "epistemic.md#epi-rte-research-findings", "memory.md#mem-rte-mcp-memory", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
      note: "Inspected replacements and archival establish evolve/invalidate locally; vault overview reduction establishes consolidation. Neither an operation name nor an unvalidated inference request proves synthesis, contradiction resolution, promotion, decay or semantic deduplication."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Desktop recall/search/project and external MCP memory/history/relationship/narrative/learning readers"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records: ["memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-mcp-memory", "epistemic.md#epi-rte-relation-retention"]
              note: "These readers explicitly request retained material; returned tool/API data are not a second push."
          records: ["memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-mcp-memory", "epistemic.md#epi-rte-relation-retention"]
          note: "These readers explicitly request retained material; returned tool/API data are not a second push."
        -
          scope: "Per-send passive facts, profile and global narrative injection"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records: ["memory.md#mem-rte-passive-context", "memory.md#mem-rte-profile-context", "epistemic.md#epi-rte-narrative-consumption"]
              note: "Prompt code supplies retained content without a request for those parts; failures can omit it."
          records: ["memory.md#mem-rte-passive-context", "memory.md#mem-rte-profile-context", "epistemic.md#epi-rte-narrative-consumption"]
          note: "Prompt code supplies retained content without a request for those parts; failures can omit it."
        -
          scope: "Narrative synthesis input selection and automatic delivery to its model"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records: ["memory.md#mem-rte-narrative-synthesis"]
              note: "After an initiation trigger, code selects active facts, pending observations and prior narrative for a tool-free model call."
          records: ["memory.md#mem-rte-narrative-synthesis"]
          note: "After an initiation trigger, code selects active facts, pending observations and prior narrative for a tool-free model call."
        -
          scope: "Dedicated connected-vault index prompt supply"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records: ["memory.md#mem-rte-vault-context"]
              note: "Prompt construction automatically selects the retained index, outside the general memory budget."
          records: ["memory.md#mem-rte-vault-context"]
          note: "Prompt construction automatically selects the retained index, outside the general memory budget."
        -
          scope: "Requested vault file/path/search/folder reads"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records: ["memory.md#mem-rte-vault-context"]
              note: "The model requests retained file content; its chosen path is a pull argument."
          records: ["memory.md#mem-rte-vault-context"]
          note: "The model requests retained file content; its chosen path is a pull argument."
        -
          scope: "Thread selection/reload and subsequent history supply to the foreground model"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records: ["memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat"]
              note: "Thread reload is requested by the UI; later send construction independently supplies saved role/content as model history."
            -
              value: "push"
              basis: "wired"
              records: ["memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat"]
              note: "Thread reload is requested by the UI; later send construction independently supplies saved role/content as model history."
          records: ["memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat"]
          note: "Thread reload is requested by the UI; later send construction independently supplies saved role/content as model history."
        -
          scope: "Journal date selection, memory browser/history, Threads review/approval and server org pull/search requests"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records: ["memory.md#mem-obj-workspace-state", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-threads-results", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
              note: "These subsequent consumers request retained work or rows. Organization frontend model discovery remains unresolved."
          records: ["memory.md#mem-obj-workspace-state", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-threads-results", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion"]
          note: "These subsequent consumers request retained work or rows. Organization frontend model discovery remains unresolved."
        -
          scope: "Threads scheduled retained-post dedup and search-budget reads"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
              note: "The scheduler independently selects retained activity state for later scan control, rather than returning a caller-requested memory payload."
          records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
          note: "The scheduler independently selects retained activity state for later scan control, rather than returning a caller-requested memory payload."
        -
          scope: "Developer instructed fixed startup pair and specialized-file requests"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "claimed"
              records: ["memory.md#mem-rte-developer-memory"]
              note: "Doctrine specifies automatic startup supply plus on-demand specialized context. Host execution is not established."
            -
              value: "pull"
              basis: "claimed"
              records: ["memory.md#mem-rte-developer-memory"]
              note: "Doctrine specifies automatic startup supply plus on-demand specialized context. Host execution is not established."
          records: ["memory.md#mem-rte-developer-memory"]
          note: "Doctrine specifies automatic startup supply plus on-demand specialized context. Host execution is not established."
        -
          scope: "Complete canvas/database model context, briefing/journal-auto-link selection and org frontend prompt/tool delivery"
          assessment: "uninspected"
          findings: []
          records: ["memory.md#mem-obj-workspace-state", "runtime.md#rt-rte-plugin-admission", "runtime.md#rt-rte-org-ingestion"]
          note: "Known UI/API requests do not resolve all included automatic consumer chains."
        -
          scope: "Provider-internal read-back"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
          note: "Request construction is inspected, but opaque provider memory retrieval is not."
      records: ["memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-mcp-memory", "epistemic.md#epi-rte-relation-retention", "memory.md#mem-rte-passive-context", "memory.md#mem-rte-profile-context", "epistemic.md#epi-rte-narrative-consumption", "memory.md#mem-rte-narrative-synthesis", "memory.md#mem-rte-vault-context", "memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-obj-workspace-state", "memory.md#mem-obj-memory-versions", "memory.md#mem-obj-threads-results", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "runtime.md#rt-rte-threads-engagement", "memory.md#mem-rte-developer-memory", "runtime.md#rt-rte-plugin-admission", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
      note: "Explicit requests and independent context supply coexist. Selecting a stored identifier to fulfill a request remains pull; automatic selection inside prompt construction is push. Untraced workspace/provider alternatives prevent complete coverage."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Per-send passive fact push"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records: ["memory.md#mem-rte-passive-context", "memory.md#mem-obj-memory-metadata"]
              note: "Trigger: each prompt rebuild. Inputs: active state, recency, type and budget. Selected part: recent top-50 fact content, grouped by type with a nominal character cutoff; no current-topic selector."
          records: ["memory.md#mem-rte-passive-context", "memory.md#mem-obj-memory-metadata"]
          note: "Trigger: each prompt rebuild. Inputs: active state, recency, type and budget. Selected part: recent top-50 fact content, grouped by type with a nominal character cutoff; no current-topic selector."
        -
          scope: "Profile/custom instructions, latest global narrative and dedicated vault-index push"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records: ["memory.md#mem-rte-profile-context", "epistemic.md#epi-rte-narrative-consumption", "memory.md#mem-rte-vault-context"]
              note: "Trigger: prompt rebuild. Exact saved setting keys, global scope and obsidian_vault_index select delivered retained parts; nonempty/connected conditions also gate availability."
            -
              value: "coarse"
              basis: "wired"
              records: ["memory.md#mem-rte-profile-context", "epistemic.md#epi-rte-narrative-consumption", "memory.md#mem-rte-vault-context"]
              note: "Trigger: prompt rebuild. Exact saved setting keys, global scope and obsidian_vault_index select delivered retained parts; nonempty/connected conditions also gate availability."
          records: ["memory.md#mem-rte-profile-context", "epistemic.md#epi-rte-narrative-consumption", "memory.md#mem-rte-vault-context"]
          note: "Trigger: prompt rebuild. Exact saved setting keys, global scope and obsidian_vault_index select delivered retained parts; nonempty/connected conditions also gate availability."
        -
          scope: "Narrative update input push"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records: ["memory.md#mem-rte-narrative-synthesis", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives"]
              note: "Trigger: scheduled/manual synthesis. Scope selects pending observations and prior narrative; active-row availability, pending state and snapshot checks select input sets. All active memories across scopes also enter."
            -
              value: "coarse"
              basis: "wired"
              records: ["memory.md#mem-rte-narrative-synthesis", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives"]
              note: "Trigger: scheduled/manual synthesis. Scope selects pending observations and prior narrative; active-row availability, pending state and snapshot checks select input sets. All active memories across scopes also enter."
          records: ["memory.md#mem-rte-narrative-synthesis", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives"]
          note: "Trigger: scheduled/manual synthesis. Scope selects pending observations and prior narrative; active-row availability, pending state and snapshot checks select input sets. All active memories across scopes also enter."
        -
          scope: "Saved thread history push to a later foreground invocation"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records: ["memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat"]
              note: "Trigger: subsequent send. Upstream selected thread ID selects the retained message set mapped to role/content; current-run protocol state is not the delivered payload."
          records: ["memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat"]
          note: "Trigger: subsequent send. Upstream selected thread ID selects the retained message set mapped to role/content; current-run protocol state is not the delivered payload."
        -
          scope: "Threads later scan state push"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
              note: "Trigger: scheduled scan. Post-ID matches choose retained duplicate state; a rolling time window and configured budget choose retained search counts. These are control inputs, not model relevance retrieval."
            -
              value: "coarse"
              basis: "wired"
              records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
              note: "Trigger: scheduled scan. Post-ID matches choose retained duplicate state; a rolling time window and configured budget choose retained search counts. These are control inputs, not model relevance retrieval."
          records: ["memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
          note: "Trigger: scheduled scan. Post-ID matches choose retained duplicate state; a rolling time window and configured budget choose retained search counts. These are control inputs, not model relevance retrieval."
        -
          scope: "Developer startup context push"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "claimed"
              records: ["memory.md#mem-rte-developer-memory"]
              note: "Trigger: next development conversation. Doctrine fixes ACTIVE_CONTEXT/CLAUDE filenames as the selected retained startup parts; actual host delivery remains unobserved."
          records: ["memory.md#mem-rte-developer-memory"]
          note: "Trigger: next development conversation. Doctrine fixes ACTIVE_CONTEXT/CLAUDE filenames as the selected retained startup parts; actual host delivery remains unobserved."
        -
          scope: "Untraced canvas/briefing/journal automatic selection, arbitrary metadata and org frontend delivery"
          assessment: "uninspected"
          findings: []
          records: ["memory.md#mem-obj-workspace-state", "memory.md#mem-obj-memory-metadata", "runtime.md#rt-rte-plugin-admission"]
          note: "No complete trigger/input/selected-part chain is recorded for these alternatives."
        -
          scope: "Provider-internal push selectors"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
          note: "Opaque provider memory cannot be classified as embedding retrieval from parametric computation alone."
      records: ["memory.md#mem-rte-passive-context", "memory.md#mem-obj-memory-metadata", "memory.md#mem-rte-profile-context", "epistemic.md#epi-rte-narrative-consumption", "memory.md#mem-rte-vault-context", "memory.md#mem-rte-narrative-synthesis", "memory.md#mem-obj-learnings", "memory.md#mem-obj-narratives", "memory.md#mem-obj-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement", "memory.md#mem-rte-developer-memory", "memory.md#mem-obj-workspace-state", "runtime.md#rt-rte-plugin-admission", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
      note: "Signals apply to automatic selection, not to requested lookup arguments. Coarse availability/budget filtering remains distinct from identity targeting. Workspace, arbitrary metadata and provider alternatives are unresolved."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Conversation-fed desktop remember to retained facts to later context/recall"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records: ["runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-passive-context"]
              note: "Conversation activity feeds an automatic model-proposed durable fact write with a wired later model consumer; usefulness and faithful extraction are unobserved."
          records: ["runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-passive-context"]
          note: "Conversation activity feeds an automatic model-proposed durable fact write with a wired later model consumer; usefulness and faithful extraction are unobserved."
        -
          scope: "Tool-feedback-fed desktop remember to retained facts to later context/recall"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records: ["runtime.md#rt-obj-current-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-passive-context"]
              note: "Tool results enter subsequent foreground model calls, where the model can propose automatically admitted facts for later context/recall. Actual extraction and which returned details become facts are unobserved."
          records: ["runtime.md#rt-obj-current-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-passive-context"]
          note: "This classifies the implemented feedback-to-fact-write branch, not raw tool-result retention or observed use."
        -
          scope: "Desktop trace-derived active facts at automatic narrative production and later briefing delivery"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records: ["runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-narrative-synthesis"]
              note: "Synthesis automatically consumes active facts, including the conversational and tool-feedback-derived alternatives, saves a durable briefing and supplies it to later sends. No particular synthesis input instance or improvement is established."
          records: ["runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-narrative-synthesis"]
          note: "The known trace-derived fact branch is separate from generic observations, other facts and prior briefing of unresolved original provenance."
        -
          scope: "Other observation/fact/prior-briefing origins at automatic narrative production"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-learnings", "memory.md#mem-rte-narrative-synthesis", "memory.md#mem-abs-learning-extractor"]
          note: "Automatic production and later briefing delivery are wired, but generic observation provenance and absent inspected desktop extractor do not establish original trace input for every included synthesis path."
        -
          scope: "Developer task-summary update and next-conversation context"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "claimed"
              records: ["memory.md#mem-rte-developer-memory"]
              note: "Doctrine directs the coding agent to retain work-derived summaries and reread them; admission execution is not established and no improvement is inferred."
          records: ["memory.md#mem-rte-developer-memory"]
          note: "Doctrine directs the coding agent to retain work-derived summaries and reread them; admission execution is not established and no improvement is inferred."
        -
          scope: "Research report/summary and Threads generated draft/reason paths"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-deep-research", "epistemic.md#epi-rte-research-findings", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
          note: "Acquired source/post text and generated work products do not by themselves establish an original activity-trace-fed behavior-shaping update. Retained outcome logs have no recorded feedback-to-guidance update."
        -
          scope: "Explicit human profile/journal edits and ordinary static-content vault scan acquisition"
          assessment: "inapplicable"
          findings: []
          records: ["memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state", "memory.md#mem-rte-vault-context"]
          note: "The named human edits are not automatic admission; the recorded scan input is file metadata/excerpts, not an established activity trace. This excludes neither model-written files nor unresolved auto-link alternatives."
        -
          scope: "Generic MCP narrative/fact/observation writes, organization imports and other canvas/journal-auto-link updates"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-rte-mcp-memory", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-obj-workspace-state"]
          note: "Caller agency and original inputs or later model-consumer chains are unresolved; optional IDs and event wrappers alone are not trace-learning evidence."
        -
          scope: "Provider-internal trace-fed adaptation"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
          note: "No provider update/retention route is exposed by inference adapters."
      records: ["runtime.md#rt-obj-current-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-passive-context", "memory.md#mem-obj-learnings", "memory.md#mem-rte-narrative-synthesis", "memory.md#mem-abs-learning-extractor", "memory.md#mem-rte-developer-memory", "runtime.md#rt-rte-deep-research", "epistemic.md#epi-rte-research-findings", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement", "memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state", "memory.md#mem-rte-vault-context", "memory.md#mem-rte-mcp-memory", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
      note: "Automatic conversational and tool-feedback fact writes qualify locally, as does their active-fact-fed narrative continuation; documented development summaries qualify at claimed strength. Other narrative input origins, research/Threads origins, workspace alternatives and provider state remain unresolved. This is not demonstrated improved capacity or a system-wide negative."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Desktop conversational remember write"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records: ["runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-obj-messages"]
              note: "Conversational turns from the agent work session feed this qualifying automatic fact-write branch; actual extraction is unobserved."
          records: ["runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-obj-messages"]
          note: "Known within the conversational-input branch only; tool feedback is classified separately and no linked state/action/outcome trajectory source is established."
        -
          scope: "Desktop tool-feedback-fed remember write"
          assessment: "known"
          findings:
            -
              value: "tool-traces"
              basis: "wired"
              records: ["runtime.md#rt-obj-current-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention"]
              note: "Recorded tool results are appended to currentMessages and consumed by subsequent model calls that can choose remember content. Software admits that content as durable facts with later context/recall consumers."
          records: ["runtime.md#rt-obj-current-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention"]
          note: "Known at the implemented tool-feedback input branch; no observed extraction instance or claim about which returned details become facts is made. Current-run protocol need not itself be durably stored to feed the qualifying fact write."
        -
          scope: "Narrative update from desktop trace-derived active facts"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records: ["runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-narrative-synthesis"]
              note: "The original input is conversational turns, mediated by automatically retained facts that synthesis consumes to produce the later-delivered briefing."
            -
              value: "tool-traces"
              basis: "wired"
              records: ["runtime.md#rt-obj-current-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-narrative-synthesis"]
              note: "The original input is tool feedback in the foreground loop, mediated by the fact-write branch and active-fact synthesis input."
          records: ["runtime.md#rt-obj-current-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-rte-narrative-synthesis"]
          note: "These are wired original-source alternatives of the fact-fed narrative route, not proof that a particular synthesis used either. Other observation/fact/prior-briefing origins remain unresolved separately."
        -
          scope: "Other narrative update observation/fact/prior-briefing origins"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-learnings", "memory.md#mem-rte-narrative-synthesis", "memory.md#mem-abs-learning-extractor"]
          note: "Optional thread/message IDs do not establish original content; synthesis receives observations rather than source messages. Trace-fed alternatives cannot be completely enumerated."
        -
          scope: "Claimed developer task-summary update origin"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-rte-developer-memory"]
          note: "Task completion and changed-file summaries are prescribed, but the recorded doctrine does not identify whether their actual source is conversation, tool feedback, events or linked trajectories."
        -
          scope: "Research/Threads generated work and possible outcome-fed updates"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-deep-research", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement"]
          note: "Imported source/post content is not automatically a trace source; retained engagement/search logs lack an established subsequent qualifying update."
        -
          scope: "Explicit human profile/journal edit and recorded static-file vault scan routes"
          assessment: "inapplicable"
          findings: []
          records: ["memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state", "memory.md#mem-rte-vault-context"]
          note: "These precisely scoped paths do not establish a qualifying automatic trace-fed write, so no trace-source finding applies to them."
        -
          scope: "Generic caller, organization, workspace-auto-link and provider alternatives"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-rte-mcp-memory", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "memory.md#mem-obj-workspace-state", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
          note: "Missing original inputs, admission control and later-consumer evidence prevent a complete source inventory; event subscription names do not establish event-stream learning."
      records: ["runtime.md#rt-obj-current-messages", "runtime.md#rt-rte-desktop-chat", "memory.md#mem-rte-desktop-retention", "memory.md#mem-obj-messages", "memory.md#mem-obj-learnings", "memory.md#mem-rte-narrative-synthesis", "memory.md#mem-abs-learning-extractor", "memory.md#mem-rte-developer-memory", "runtime.md#rt-rte-deep-research", "memory.md#mem-obj-threads-results", "runtime.md#rt-rte-threads-engagement", "memory.md#mem-rte-profile-context", "memory.md#mem-obj-workspace-state", "memory.md#mem-rte-vault-context", "memory.md#mem-rte-mcp-memory", "memory.md#mem-obj-org-memories", "runtime.md#rt-rte-org-ingestion", "runtime.md#rt-cmp-ai-client", "runtime.md#rt-cmp-ai-evaluator"]
      note: "Original conversational turns and tool feedback support session-logs and tool-traces for desktop fact writes and their fact-fed narrative continuation. Other input origins remain unknown rather than inheriting a trace class from a table/tool label. No complete route-level inventory or absence of qualifying trace learning is established."
---

# Continuity memory profile

## Comparison rationale

This profile classifies the accepted record inventory, not all runtime storage. All positive implementation findings are wired capacities, not observed use or causal benefit. Developer maintenance remains claimed, and the human Threads review edit surface is afforded independently of generic endpoint agency. Each partial axis retains the unresolved included alternatives rather than treating a strong witness as complete coverage.

Reconciliation supersedes the epistemic memory-content, learning-observation, narrative and vault-overview objects by their memory-member counterparts. The profile cites [MEM-OBJ-memories](memory.md#mem-obj-memories), [MEM-OBJ-learnings](memory.md#mem-obj-learnings), [MEM-OBJ-narratives](memory.md#mem-obj-narratives) and [MEM-OBJ-vault-index](memory.md#mem-obj-vault-index). Epistemic source-label and relationship-edge parts remain distinct from their broader metadata/project containers. Narrative generation, retention and consumption are separate routes; no supersession upgrades their statuses.

SQLite is the retained local/organization/plugin substrate. Stored links are symbolic access structures, not evidence of a separate graph engine; no recorded vector store exists as a positive finding. Natural-language text and symbolic wrappers have different consumers. Remote parametric inference in [RT-CMP-ai-client](runtime.md#rt-cmp-ai-client) and [RT-CMP-ai-evaluator](runtime.md#rt-cmp-ai-evaluator) does not prove a model-weights memory substrate or a parametric accumulated memory object. Opaque provider memory remains unresolved, so these axes are not system-complete negatives about it.

Known lineage concerns the recorded path. Model-selected conversational facts and saved messages differ from caller imports, scan projections and other compiled model work products. [MEM-CLM-source-trust](memory.md#mem-clm-source-trust) prevents treating source=user as authenticated authorship. [MEM-RTE-narrative-synthesis](memory.md#mem-rte-narrative-synthesis) establishes an automatic durable update, but [EPI-RTE-narrative-generation](epistemic.md#epi-rte-narrative-generation) leaves semantic preservation and novelty unresolved. Accordingly current-entry evolution is classified without assuming consolidation or synthesis of new claims on every model branch.

Authority is local to a retained part's consumer. Archive flags enforce active-read exclusion; recency/type fields rank passive delivery; pending observations and snapshot state route synthesis; source text supplies knowledge or instructions. Retained endpoint existence validates and blocks relation admission in [EPI-RTE-relation-retention](epistemic.md#epi-rte-relation-retention), without validating contradiction or supersession. Existing organization timestamps similarly validate replacement eligibility rather than truth. Unconsumed narrative reasons, confidence and historical change reasons are not promoted into foreground factual-validation authority.

The desktop remember path has separately classified conversational and tool-feedback-fed branches at wired strength. Work-session turns supply session-log input. [RT-OBJ-current-messages](runtime.md#rt-obj-current-messages) and [RT-RTE-desktop-chat](runtime.md#rt-rte-desktop-chat) establish that tool results enter subsequent model calls in the same loop that chooses memory-tool content. That feedback supplies tool-trace input to automatic durable fact writes; later context/recall delivers the result. This does not require an observed extraction instance, and it does not establish which returned details become facts, faithful extraction or benefit. The scope excludes current-run protocol as a retained memory object, not as an input to qualifying writes.

[MEM-RTE-narrative-synthesis](memory.md#mem-rte-narrative-synthesis) additionally consumes active facts automatically, saves a durable briefing and supplies it to later sends. The desktop conversational-fact and tool-feedback-fact branches therefore retain their original session-log and tool-trace classifications through this intermediate fact store. Generic observation origins and other fact/prior-briefing origins remain unresolved in separate units; they do not erase those supported branches or establish complete narrative-route coverage. No particular synthesis instance is shown to have used either trace-derived input. These wired trace-learning capacities are separate from the broader capacity-improvement claims the runtime and epistemic accounts decline to establish. Caller-recorded observations can carry learning authority at narrative update while their original trace source remains unknown. [MEM-ABS-learning-extractor](memory.md#mem-abs-learning-extractor) excludes the inspected desktop observation extractor only; it neither erases desktop remember nor establishes a system-wide trace-learning no. Raw message retention and Threads engagement logs alone are insufficient without an update consumer. Imported research sources and vault file excerpts are not converted into activity traces by serialization or automatic processing.

Push and pull distinguish operations within chains. Requested recall, server pull/search and vault file reads remain pull. Automatic per-send fact/profile/narrative/vault/history supply is push; thread or saved-key identity actually selects delivered material. Passive memory availability, recency/type ordering and character budgeting are coarse rather than topic judgment, lexical relevance or embeddings. [MEM-RTE-passive-context](memory.md#mem-rte-passive-context) records no query targeting. Threads model relevance scoring is not classified as a retained-memory push signal: the selected posts are current acquisition, and the stored score is not shown to select a later memory delivery.

Organization pull routing and plugin foreground discovery remain bounded by [RT-RTE-org-ingestion](runtime.md#rt-rte-org-ingestion) and [RT-RTE-plugin-admission](runtime.md#rt-rte-plugin-admission). Server persistence/read endpoints do not establish a joined desktop memory loop. Research callback persistence remains wired but not confirmed delivery; the workflow annotation on [RT-RTE-deep-research](runtime.md#rt-rte-deep-research) distinguishes result handoff from successful canvas/message writes. These constraints prevent stronger coverage or observed classifications without suppressing inspected local routes.

Missing recorded facts include arbitrary metadata interpretation, complete canvas/database and journal-auto-link admission/context paths, generic caller content control and provenance, original observation inputs, developer document derivation/control, provider-internal memory operations, and the remaining organization/frontend integration. No source file was read for this classification; all warrants are in the supplied accepted members, with supersessions resolved through the supplied reconciliation. No new evidence, quotes or records are added.
