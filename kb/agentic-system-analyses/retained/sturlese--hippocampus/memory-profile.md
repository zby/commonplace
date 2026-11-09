---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Hippocampus memory comparison: retained Markdown vault, source archives, catalog, journal, hot-cache delivery and optional diagnostic reports."
run-id: "AAS-2026-11-08-hippocampus-30a5ab9b2a87-01"
source-identity: "https://github.com/sturlese/hippocampus"
reviewed-boundary: "99531951ae60a9814ac7d27a32dd00f0c81a5008"
memory-comparison:
  version: 2
  scope: "Accumulated source archives and auxiliary attachments; source, entity, concept, project and saved-note pages; catalog, operations journal, overwritten hot cache and optional retained mechanical/editorial lint reports; their prescribed writes, maintenance and later agent consumers, with conditional Git history. Excludes static shipped project contracts, skills, templates, hook configuration, framework synchronization products, ordinary current-run stdout and external host/model internals. Host handling of configured cache delivery remains a limit, not an alternative vault store."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        - scope: "Archived originals and auxiliary attachments"
          assessment: "known"
          findings:
            - value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-archive"
              note: "Archiving retains local filesystem payloads irrespective of their encoding."
          records:
            - "memory.md#mem-obj-archive"
          note: "Payload encoding uncertainty does not obscure the prescribed filesystem substrate."
        - scope: "Accumulated source, derived and saved pages, catalog, journal and hot cache"
          assessment: "known"
          findings:
            - value: "files"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-source"
                - "memory.md#mem-obj-pages"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-hot"
              note: "The model workflows retain Markdown files."
            - value: "repo"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-lifecycle-hooks"
              note: "The stop hook stages content roots and conditionally creates Git history; failures do not undo the file retention."
          records:
            - "memory.md#mem-obj-source"
            - "memory.md#mem-obj-pages"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-hot"
            - "runtime.md#rt-rte-lifecycle-hooks"
          note: "Covers the six named retained surfaces and their conditional history, not an external model's weights."
        - scope: "Optional retained lint report, mechanical and editorial parts"
          assessment: "known"
          findings:
            - value: "files"
              basis: "afforded"
              records:
                - "epistemic.md#epi-obj-findings"
              note: "The lint skill permits a combined Markdown report under wiki/meta."
          records:
            - "epistemic.md#epi-obj-mechanical-findings"
            - "epistemic.md#epi-obj-editorial-findings"
          note: "Only the optional retained form is memory here; current stdout alone is excluded."
      records:
        - "memory.md#mem-obj-archive"
        - "memory.md#mem-obj-source"
        - "memory.md#mem-obj-pages"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-hot"
        - "runtime.md#rt-rte-lifecycle-hooks"
        - "epistemic.md#epi-obj-mechanical-findings"
        - "epistemic.md#epi-obj-editorial-findings"
        - "epistemic.md#epi-obj-findings"
      note: "The records inventory local vault payloads and conditional Git history. Wikilinks do not establish a graph database."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Textual archive branch"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-archive"
              note: "Prose source notes and extracted URL text are retained as source content."
          records:
            - "memory.md#mem-obj-archive"
          note: "Restricted to the expressly described prose branch."
        - scope: "Nontext archive and attachment payloads"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-archive"
          note: "The scaffold supplies no payload; arbitrary PDFs, images or data cannot receive one complete form classification."
        - scope: "Vault prose consumed by agents and humans"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-source"
                - "memory.md#mem-obj-pages"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-hot"
              note: "Claims, explanations, descriptions and recent-context summaries require interpretation."
          records:
            - "memory.md#mem-obj-source"
            - "memory.md#mem-obj-pages"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-hot"
          note: "Includes source and derived pages, catalog descriptions, journal prose and hot text."
        - scope: "Vault identity, navigation and structural metadata"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-source"
                - "memory.md#mem-obj-pages"
                - "memory.md#mem-obj-index"
              note: "Hash, origin paths, links and schema fields support fixed identity/navigation checks."
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-vault-lint"
              note: "Python consumes parsed fields, names and links under fixed rules."
          records:
            - "memory.md#mem-obj-source"
            - "memory.md#mem-obj-pages"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-hot"
            - "memory.md#mem-obj-log"
          note: "Dates and links are distinct from the prose they accompany."
        - scope: "Optional report mechanical part"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-mechanical-findings"
              note: "Fixed severity/check/file/message dictionaries encode structural findings."
          records:
            - "epistemic.md#epi-obj-mechanical-findings"
          note: "Program-generated part, not the editorial model assessment."
        - scope: "Optional report editorial part"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "afforded"
              records:
                - "epistemic.md#epi-obj-editorial-findings"
              note: "Allegations and proposed repairs are interpreted by the agent and user."
          records:
            - "epistemic.md#epi-obj-editorial-findings"
          note: "Report retention does not merge the two parts' forms."
      records:
        - "memory.md#mem-obj-archive"
        - "memory.md#mem-obj-source"
        - "memory.md#mem-obj-pages"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-hot"
        - "runtime.md#rt-rte-vault-lint"
        - "epistemic.md#epi-obj-mechanical-findings"
        - "epistemic.md#epi-obj-editorial-findings"
      note: "Prose and localized metadata are classified separately; nontext archived payloads remain unresolved. External model weights are not retained vault memory."
    lineage:
      assessment: "partial"
      units:
        - scope: "Moved/copied/pasted originals and fetched URL extractions"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-archive"
              note: "External content enters through move, copy, verbatim paste or fetched extraction; URL extraction need not preserve response bytes."
          records:
            - "memory.md#mem-obj-archive"
          note: "Imported content is not thereby endorsed."
        - scope: "Source-derived pages, catalog descriptions and refreshed summaries"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "memory.md#mem-obj-source"
                - "memory.md#mem-obj-hot"
                - "memory.md#mem-obj-index"
              note: "Model transforms source content and page state into reusable summaries and access metadata."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "memory.md#mem-obj-source"
            - "memory.md#mem-obj-pages"
            - "memory.md#mem-obj-hot"
            - "memory.md#mem-obj-index"
          note: "Compilation describes derivation, not verified semantic preservation."
        - scope: "Conversation-save pages and their derivative cache/catalog/journal"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-conversation-save"
                - "memory.md#mem-obj-pages"
              note: "Current conversation supplies retained conclusions, decisions and findings, with derivative metadata and later read-back."
          records:
            - "runtime.md#rt-rte-conversation-save"
            - "memory.md#mem-obj-pages"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-hot"
          note: "Trace extraction does not require copying the transcript."
        - scope: "Optional lint report mechanical part"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "epistemic.md#epi-obj-mechanical-findings"
              note: "Fixed scanner predicates derive findings from a file snapshot."
          records:
            - "epistemic.md#epi-obj-mechanical-findings"
          note: "Optional report persistence is afforded, not observed."
        - scope: "Optional editorial report and model-written operations journal"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "afforded"
              records:
                - "epistemic.md#epi-obj-editorial-findings"
                - "memory.md#mem-obj-log"
              note: "The agent formulates maintenance proposals and operation descriptions."
          records:
            - "epistemic.md#epi-obj-editorial-findings"
            - "memory.md#mem-obj-log"
          note: "Authored diagnoses remain candidates rather than accepted claims."
        - scope: "Arbitrary auxiliary attachment provenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-archive"
          note: "Reference to auxiliary files does not establish every attachment's original derivation."
      records:
        - "memory.md#mem-obj-archive"
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-obj-source"
        - "memory.md#mem-obj-pages"
        - "memory.md#mem-obj-hot"
        - "memory.md#mem-obj-index"
        - "runtime.md#rt-rte-conversation-save"
        - "memory.md#mem-obj-log"
        - "epistemic.md#epi-obj-mechanical-findings"
        - "epistemic.md#epi-obj-editorial-findings"
      note: "Known subsequent transformations are retained despite unresolved arbitrary payload provenance; initial shipped scaffolds are excluded as static content."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Selected page claims and hot context at later answering/curation agent"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-bap-vault-knowledge"
                - "runtime.md#rt-rte-vault-query"
              note: "Explicit file reads supply evidence/context for synthesis and curation."
            - value: "knowledge"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-lifecycle-hooks"
                - "memory.md#mem-obj-hot"
              note: "Configured SessionStart emits hot as later agent context, subject to external host handling."
          records:
            - "memory.md#mem-bap-vault-knowledge"
            - "memory.md#mem-obj-pages"
            - "memory.md#mem-obj-source"
            - "memory.md#mem-obj-hot"
          note: "Delivery is not observed compliance; cache content is not standing instruction."
        - scope: "Catalog descriptions, aliases and page text at relevance selector"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-vault-query"
                - "memory.md#mem-obj-index"
              note: "The model uses catalog relevance and strongest term-search matches to prioritize pages."
            - value: "routing"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-vault-query"
                - "memory.md#mem-obj-index"
              note: "Catalog and wikilinks identify which page inputs the agent opens next."
          records:
            - "runtime.md#rt-rte-vault-query"
            - "memory.md#mem-obj-index"
          note: "These effects concern selection, not truth certification."
        - scope: "Stored source hashes at duplicate admission decision"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "memory.md#mem-obj-source"
              note: "An existing content_hash supplies the identity criterion before extraction."
            - value: "enforcement"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-source-ingest"
              note: "A duplicate requests stopping unless explicit re-ingest overrides it; enforcement depends on model compliance."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "memory.md#mem-obj-source"
          note: "The protocol's veto is not a filesystem gate."
        - scope: "Conversation experience at save/update consumer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-conversation-save"
                - "memory.md#mem-obj-pages"
              note: "Conversation-derived conclusions feed durable behavior-shaping pages and derivative context for later agents."
          records:
            - "runtime.md#rt-rte-conversation-save"
            - "memory.md#mem-obj-pages"
          note: "Learning authority is local to the update; downstream pages have knowledge authority, and no improvement is demonstrated."
        - scope: "Retained optional diagnostics, archive and journal at future consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-obj-findings"
            - "memory.md#mem-obj-archive"
            - "memory.md#mem-obj-log"
          note: "Current maintenance advice is established, but retaining a report or origin pointer alone does not establish its later consumer and force."
      records:
        - "memory.md#mem-bap-vault-knowledge"
        - "memory.md#mem-obj-pages"
        - "memory.md#mem-obj-source"
        - "memory.md#mem-obj-hot"
        - "runtime.md#rt-rte-vault-query"
        - "runtime.md#rt-rte-lifecycle-hooks"
        - "memory.md#mem-obj-index"
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-conversation-save"
        - "epistemic.md#epi-obj-findings"
        - "memory.md#mem-obj-archive"
        - "memory.md#mem-obj-log"
      note: "Knowledge, selection, duplicate-admission and save-update consumers are distinct. No instruction authority is transferred from shipped contracts to vault content; optional later report/archive use is unresolved."
    write_agency:
      assessment: "known"
      units:
        - scope: "Ordinary ingest/save, metadata and hot rewrite admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "runtime.md#rt-rte-conversation-save"
                - "memory.md#mem-obj-hot"
              note: "The model selects and writes content without universal per-content approval; initiating the workflow is not manual admission."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-conversation-save"
            - "memory.md#mem-obj-hot"
          note: "Includes ordinary archive placement and cache replacement; selective user vetoes are separate."
        - scope: "Project creation, same-name overwrite and approved editorial repairs"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "runtime.md#rt-rte-conversation-save"
                - "runtime.md#rt-rte-vault-lint"
              note: "Explicit user confirmation or approval supplies the admission decision for these branches."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-conversation-save"
            - "runtime.md#rt-rte-vault-lint"
          note: "Model performs physical writes, but approval makes admission manual."
        - scope: "Optional retained diagnostic report admission on user request or many findings"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "afforded"
              records:
                - "epistemic.md#epi-obj-findings"
                - "epistemic.md#epi-obj-mechanical-findings"
                - "epistemic.md#epi-obj-editorial-findings"
              note: "The skill directs the model to retain a report when the user wants a record or findings are numerous; neither branch requires approval of the generated report content."
          records:
            - "epistemic.md#epi-obj-findings"
            - "epistemic.md#epi-obj-mechanical-findings"
            - "epistemic.md#epi-obj-editorial-findings"
          note: "The user-request branch initiates report production, not per-content approval. The many-findings branch delegates retention to the model. Scanner generation is wired, but this optional retention instruction is only afforded."
      records:
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-conversation-save"
        - "memory.md#mem-obj-hot"
        - "runtime.md#rt-rte-vault-lint"
        - "epistemic.md#epi-obj-findings"
        - "epistemic.md#epi-obj-mechanical-findings"
        - "epistemic.md#epi-obj-editorial-findings"
      note: "Covers ordinary ingest/save/cache admission, selectively human-approved branches and optional report admission, not every hypothetical direct filesystem edit. Stop-time staging and commits persist already-admitted content and establish no additional admission mechanism or wired write-agency finding."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Source extraction, conversation conclusion saving and hot refresh"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-source-ingest"
                - "runtime.md#rt-rte-conversation-save"
                - "memory.md#mem-obj-hot"
              note: "The prescribed operation selects/compresses source or session material into reusable pages and recent context."
            - value: "evolve"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-pages"
                - "memory.md#mem-obj-hot"
              note: "Existing pages are updated and the cache is overwritten."
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "runtime.md#rt-rte-conversation-save"
            - "memory.md#mem-obj-hot"
            - "memory.md#mem-obj-pages"
          note: "Warrants requested transformations, not actual faithful model execution."
        - scope: "User-approved duplicate merges, page repairs and deletion"
          assessment: "known"
          findings:
            - value: "dedup"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-vault-lint"
                - "epistemic.md#epi-obj-editorial-findings"
              note: "Individually approved duplicate merges reduce duplicate retained pages."
            - value: "evolve"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-vault-lint"
              note: "Approved fixes revise existing content."
            - value: "decay"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-vault-lint"
              note: "Individually approved deletion forgets selected retained pages; seed age only nominates review."
          records:
            - "runtime.md#rt-rte-vault-lint"
            - "epistemic.md#epi-obj-editorial-findings"
          note: "Scanner detection alone does not implement these edits."
        - scope: "Semantic novelty in saved conclusions and summaries"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-conversation-save"
            - "memory.md#mem-obj-pages"
            - "memory.md#mem-obj-hot"
          note: "No recorded input/output pair establishes a new non-entailed claim. The word synthesis does not establish synthesize; indeterminate semantic alternatives prevent complete coverage."
      records:
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-conversation-save"
        - "memory.md#mem-obj-hot"
        - "memory.md#mem-obj-pages"
        - "runtime.md#rt-rte-vault-lint"
        - "epistemic.md#epi-obj-editorial-findings"
      note: "Primary-key hash rejection is not memory deduplication by itself. Callouts preserve competing claims rather than establishing invalidate; no promotion or automatic age decay is inferred."
    read_back_direction:
      assessment: "known"
      units:
        - scope: "Requested vault/cross-project reads and later ingest context reads"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-vault-query"
                - "memory.md#mem-bap-vault-knowledge"
                - "runtime.md#rt-rte-source-ingest"
              note: "A consumer requests hot/catalog/pages and receives selected files, with bounded link/search fallback."
          records:
            - "runtime.md#rt-rte-vault-query"
            - "memory.md#mem-bap-vault-knowledge"
            - "runtime.md#rt-rte-source-ingest"
          note: "Model page selection within the requested read chain is not an additional unsolicited delivery."
        - scope: "SessionStart cache delivery"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-lifecycle-hooks"
                - "memory.md#mem-obj-hot"
              note: "The configured startup/resume/clear/compact callback supplies retained hot without an explicit request for its contents."
          records:
            - "runtime.md#rt-rte-lifecycle-hooks"
            - "memory.md#mem-obj-hot"
          note: "The whole existing file is selected; exact host-visible truncation and activation remain unobserved."
      records:
        - "runtime.md#rt-rte-vault-query"
        - "memory.md#mem-bap-vault-knowledge"
        - "runtime.md#rt-rte-source-ingest"
        - "runtime.md#rt-rte-lifecycle-hooks"
        - "memory.md#mem-obj-hot"
      note: "The accepted records establish both operative later-consumer routes. Archive pointers, Git capability and optional report retention establish no additional read-back route."
    read_back_signal:
      assessment: "known"
      units:
        - scope: "Automatic SessionStart hot supply"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-lifecycle-hooks"
                - "memory.md#mem-obj-hot"
              note: "Trigger: startup/resume/clear/compact. Selector input: hot-file existence. Selected part: entire hot file, without question- or identity-matched fact selection."
          records:
            - "runtime.md#rt-rte-lifecycle-hooks"
            - "memory.md#mem-obj-hot"
          note: "Earlier model summary construction is not the later push selector; a fixed filename alone does not establish identifier targeting."
        - scope: "Requested catalog/page/link/search read chain"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-vault-query"
          note: "Push signal classifies unsolicited supply, not selection inside an explicit consumer request."
      records:
        - "runtime.md#rt-rte-lifecycle-hooks"
        - "memory.md#mem-obj-hot"
        - "runtime.md#rt-rte-vault-query"
      note: "Only recorded push is coarse cache delivery. Catalog relevance and lexical fallback belong to pull, so do not add inferred-judgment or inferred-lexical push signals."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Conversation save and its later-consumed page/cache derivatives"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-conversation-save"
                - "memory.md#mem-obj-pages"
                - "memory.md#mem-obj-hot"
              note: "Automatic model selection extracts durable conclusions from current session conversation; later queries and sessions consume pages/hot as context."
          records:
            - "runtime.md#rt-rte-conversation-save"
            - "memory.md#mem-obj-pages"
            - "memory.md#mem-obj-hot"
            - "runtime.md#rt-rte-vault-query"
          note: "User initiation is not per-content approval. This local write-route sense establishes neither parameter change nor improved capacity."
        - scope: "General external-source ingest, derivative hot and activity journal alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "memory.md#mem-obj-archive"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-hot"
          note: "Sources may contain experience, but the empty scaffold does not establish each input's trace content or a separate automatic journal-to-durable-update consumer. No bounded absence record warrants a local no."
      records:
        - "runtime.md#rt-rte-conversation-save"
        - "memory.md#mem-obj-pages"
        - "memory.md#mem-obj-hot"
        - "runtime.md#rt-rte-vault-query"
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-obj-archive"
        - "memory.md#mem-obj-log"
      note: "The afforded save chain supports a system yes while arbitrary input alternatives remain unresolved. No system-wide no or observed-learning claim follows."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Conversation-fed save and derivative page/cache update"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-conversation-save"
                - "memory.md#mem-obj-pages"
              note: "Original input is recorded conversational turns from the current agent work session, even though the retained output omits the transcript."
          records:
            - "runtime.md#rt-rte-conversation-save"
            - "memory.md#mem-obj-pages"
          note: "This classifies the evidenced conversational source; no separately evidenced tool-trace or trajectory input is added."
        - scope: "Arbitrary ingested external payloads and possible experience-derived alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-source-ingest"
            - "memory.md#mem-obj-archive"
            - "memory.md#mem-obj-log"
          note: "Input origin/content is not supplied, preventing classification as event-streams, tool-traces, trajectories or a bounded non-trace source."
      records:
        - "runtime.md#rt-rte-conversation-save"
        - "memory.md#mem-obj-pages"
        - "runtime.md#rt-rte-source-ingest"
        - "memory.md#mem-obj-archive"
        - "memory.md#mem-obj-log"
      note: "A route label or journal serialization does not prove event-stream origin. Incomplete trace inventory prevents making this axis globally inapplicable."
---

# Hippocampus memory profile

## Comparison rationale

This profile classifies accepted records, not target execution. Semantic extraction, saving and editorial repair are afforded by model-facing instructions. Hook delivery and Git persistence are wired. No finding is upgraded to observed or causally supported. The vault is a file-based linked knowledge system: links alone do not establish graph storage, and external agent weights are not accumulated vault state.

Reconciliation supersedes EPI-OBJ-source, EPI-OBJ-pages and EPI-OBJ-hot with their memory-member counterparts. The classifications therefore cite [MEM-OBJ-source](memory.md#mem-obj-source), [MEM-OBJ-pages](memory.md#mem-obj-pages) and [MEM-OBJ-hot](memory.md#mem-obj-hot). Archive records overlap without whole-record identity. The combined epistemic catalog/journal record is not substituted for the separate catalog and journal. Mechanical and editorial report parts retain distinct forms and bases: [EPI-OBJ-mechanical-findings](epistemic.md#epi-obj-mechanical-findings) and [EPI-OBJ-editorial-findings](epistemic.md#epi-obj-editorial-findings).

Conversation saving supplies a qualifying automatic trace-fed write despite its user trigger. The model selects durable conclusions, and later agents receive pages or their cache derivatives. This supports afforded trace learning and session-log origin, not measured improvement. Learning authority at the update consumer is separate from knowledge authority downstream. Arbitrary source payloads remain unresolved rather than receiving unsupported negative learning values; no accepted evidenced-absence record supplies such a negative. See [RT-RTE-conversation-save](runtime.md#rt-rte-conversation-save) and [MEM-OBJ-pages](memory.md#mem-obj-pages).

Consolidation follows the requested selection/compression mechanism. It does not certify fidelity. The source word synthesis does not establish new claims absent from inputs; semantic novelty remains unresolved. Approved merging and deletion afford deduplication and forgetting, but mere duplicate-hash rejection, age flags and contradiction callouts do not establish those transformations by themselves. See [RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest) and [RT-RTE-vault-lint](runtime.md#rt-rte-vault-lint).

The automatic cache branch is coarse push: an event and file-existence check supply the whole hot file. Requested catalog and lexical searches are pull selection, not extra push signals. Missing host truncation semantics prevent an exact deployed context-size claim, not classification of the wired selector. See [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks) and [RT-RTE-vault-query](runtime.md#rt-rte-vault-query).

Write agency classifies content admission, not physical persistence. The stop hook's wired staging and commit remain storage findings only; they do not upgrade the afforded automatic content admission to wired. Optional diagnostic report admission is separately afforded: the model writes the report on user request or when findings are numerous, without a prescribed per-content approval step. A user request starts that production rather than approving its generated content. Mechanical findings are wired outputs, but their optional retention and the editorial report remain model-facing instructions. See [RT-RTE-lifecycle-hooks](runtime.md#rt-rte-lifecycle-hooks), [EPI-OBJ-findings](epistemic.md#epi-obj-findings), [EPI-OBJ-mechanical-findings](epistemic.md#epi-obj-mechanical-findings) and [EPI-OBJ-editorial-findings](epistemic.md#epi-obj-editorial-findings).

Source-read log: none. This mapping used only the supplied accepted members and reconciliation; no frozen target files were reread.
