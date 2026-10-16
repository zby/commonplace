---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "LLM Project Wiki memory comparison: the specified project vault, maintenance records and generated later-consumer rules at the frozen prompt boundary."
run-id: "AAS-2026-10-14-llm-project-wiki-c6c664168f3e-01"
source-identity: "https://github.com/akash-r34/llm-project-wiki"
reviewed-boundary: "1fdfba9129a46afd18aa68a83f12d6716ab694c6"
memory-comparison:
  version: 2
  scope: "Specified retained Sources snapshots, compiled Wiki content and metadata, index, logs, templates, health dashboard, schema, generated commands and repaired live project/maintenance rules, including pre-existing vault/input provenance and unresolved host delivery of these rules. Excludes static shipped setup text as current invocation input, provider parameters, host compaction/working state, consuming project source code except retained imports, and external plugin implementations. Classifies the prompt-defined memory design, not an inspected installation."
  axes:
    storage_substrate:
      assessment: "known"
      units:
        - scope: "Specified vault and project support files: Sources, Wiki content/metadata, index, log, templates, health, schema, commands and repaired live rules"
          assessment: "known"
          findings:
            - value: "files"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-templates"
                - "memory.md#mem-obj-health"
                - "runtime.md#rt-obj-schema"
                - "runtime.md#rt-obj-wiki-ingest"
                - "runtime.md#rt-bap-project-rules"
                - "runtime.md#rt-bap-maintenance-rules"
                - "runtime.md#rt-rte-gap-audit"
              note: "All included retained surfaces are specified filesystem files; none is a supplied generated instance."
            - value: "repo"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-clm-retention-limits"
                - "runtime.md#rt-rte-vault-bootstrap"
              note: "Wiki and Sources are also explicitly intended as Git-tracked repository content; no installed Git history is observed."
          records:
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-templates"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-obj-schema"
            - "runtime.md#rt-obj-wiki-ingest"
            - "runtime.md#rt-bap-project-rules"
            - "runtime.md#rt-bap-maintenance-rules"
            - "runtime.md#rt-rte-gap-audit"
            - "runtime.md#rt-rte-vault-bootstrap"
            - "memory.md#mem-clm-retention-limits"
          note: "The accepted inventory covers the prompt-defined retained file surfaces, including generated and repaired support files; provider state is excluded, not classified."
      records:
        - "memory.md#mem-obj-sources"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-templates"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-obj-schema"
        - "runtime.md#rt-obj-wiki-ingest"
        - "runtime.md#rt-bap-project-rules"
        - "runtime.md#rt-bap-maintenance-rules"
        - "runtime.md#rt-rte-gap-audit"
        - "runtime.md#rt-rte-vault-bootstrap"
        - "memory.md#mem-clm-retention-limits"
      note: "Complete classification of the specified substrate inventory, not proof of actual persistence or deployment."
    representational_form:
      assessment: "known"
      units:
        - scope: "Prose in source snapshots, Wiki descriptions/rationales, index intent table, logs, schema, template guidance and live maintenance/project rules at model consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-templates"
                - "memory.md#mem-obj-health"
                - "runtime.md#rt-obj-schema"
                - "runtime.md#rt-obj-wiki-ingest"
                - "runtime.md#rt-bap-project-rules"
                - "runtime.md#rt-bap-maintenance-rules"
              note: "Models interpret the retained prose as reference, navigation, diagnosis or standing guidance."
          records:
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-templates"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-obj-schema"
            - "runtime.md#rt-obj-wiki-ingest"
            - "runtime.md#rt-bap-project-rules"
            - "runtime.md#rt-bap-maintenance-rules"
          note: "All named prose parts have specified model consumers; inaccessible concrete wording prevents correctness judgments, not this declared-form classification."
        - scope: "Code/config excerpts, frontmatter selectors, wikilink targets, template placeholders, health/index queries and command shell fragments at fixed-rule consumers"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-templates"
                - "memory.md#mem-obj-health"
                - "runtime.md#rt-obj-wiki-ingest"
                - "runtime.md#rt-rte-source-sync"
              note: "Named keys, paths, code and query structures have localized fixed semantics on their specified consumption paths; excerpts need not execute to remain symbolic code."
          records:
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-templates"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-obj-wiki-ingest"
            - "runtime.md#rt-rte-source-sync"
          note: "Separates symbolic parts from model-interpreted prose; concrete plugin execution is unavailable."
      records:
        - "memory.md#mem-obj-sources"
        - "memory.md#mem-obj-wiki"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-templates"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-obj-schema"
        - "runtime.md#rt-obj-wiki-ingest"
        - "runtime.md#rt-bap-project-rules"
        - "runtime.md#rt-bap-maintenance-rules"
        - "runtime.md#rt-rte-source-sync"
      note: "The inventory specifies mixed natural-language and symbolic parts. Excluded provider weights do not add parametric memory to this boundary."
    lineage:
      assessment: "partial"
      units:
        - scope: "Sources acquisition and verbatim source/code material retained in compiled pages"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-obj-wiki"
                - "runtime.md#rt-rte-source-sync"
              note: "Sync/manual copy imports existing project material; required literal excerpts carry imported source material into page references."
          records:
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-source-sync"
          note: "Copying is specified, but initial human/model authorship and installation-specific input provenance are unresolved."
        - scope: "Model-created Wiki prose, navigation, logs, metadata, templates and maintenance/support rules, including later repairs"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-obj-wiki"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-log"
                - "memory.md#mem-obj-templates"
                - "memory.md#mem-obj-health"
                - "runtime.md#rt-obj-schema"
                - "runtime.md#rt-obj-wiki-ingest"
                - "runtime.md#rt-bap-project-rules"
                - "runtime.md#rt-bap-maintenance-rules"
                - "runtime.md#rt-rte-vault-bootstrap"
                - "runtime.md#rt-rte-diff-ingest"
                - "runtime.md#rt-rte-gap-audit"
              note: "Foreground model authoring creates page prose, summaries, navigation and operational guidance, then revises them."
          records:
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-wiki"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-log"
            - "memory.md#mem-obj-templates"
            - "memory.md#mem-obj-health"
            - "runtime.md#rt-obj-schema"
            - "runtime.md#rt-obj-wiki-ingest"
            - "runtime.md#rt-bap-project-rules"
            - "runtime.md#rt-bap-maintenance-rules"
            - "runtime.md#rt-rte-vault-bootstrap"
            - "runtime.md#rt-rte-diff-ingest"
            - "runtime.md#rt-rte-gap-audit"
          note: "Authored names the specified model content-production path, not a claim of human authorship or epistemic novelty."
        - scope: "Pre-existing vault and fallback project memory initial content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-sources"
            - "runtime.md#rt-obj-schema"
            - "runtime.md#rt-rte-gap-audit"
          note: "Accepted records leave installation-specific initial provenance unknown; subsequent model revisions do not determine it."
      records:
        - "memory.md#mem-obj-sources"
        - "memory.md#mem-obj-wiki"
        - "runtime.md#rt-rte-source-sync"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-log"
        - "memory.md#mem-obj-templates"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-obj-schema"
        - "runtime.md#rt-obj-wiki-ingest"
        - "runtime.md#rt-bap-project-rules"
        - "runtime.md#rt-bap-maintenance-rules"
        - "runtime.md#rt-rte-vault-bootstrap"
        - "runtime.md#rt-rte-diff-ingest"
        - "runtime.md#rt-rte-gap-audit"
      note: "Imported and authored paths are supported, but initial provenance of copied/fallback and existing-vault content prevents complete lineage coverage. No recorded automatic raw-session extraction establishes trace-extracted lineage."
    behavioral_authority:
      assessment: "known"
      units:
        - scope: "Sources snapshots and Wiki domain content at bootstrap, answering, status and maintenance model consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-sources"
                - "memory.md#mem-obj-wiki"
                - "runtime.md#rt-rte-wiki-lookup"
              note: "Retained project content supplies references, facts, constraints and decision reasons, not enforced controls."
          records:
            - "memory.md#mem-obj-sources"
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-wiki-lookup"
          note: "This is the intended content force; source warrant and deployed compliance remain unknown."
        - scope: "Schema, commands, template guidance, archive warning and live repaired rules at subsequent model consumers"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-schema"
                - "runtime.md#rt-obj-wiki-ingest"
                - "memory.md#mem-obj-templates"
                - "memory.md#mem-obj-sources"
                - "runtime.md#rt-bap-project-rules"
                - "runtime.md#rt-bap-maintenance-rules"
              note: "Retained directions govern maintenance, page construction, interpretive trust and wiki-first work."
          records:
            - "runtime.md#rt-obj-schema"
            - "runtime.md#rt-obj-wiki-ingest"
            - "memory.md#mem-obj-templates"
            - "memory.md#mem-obj-sources"
            - "runtime.md#rt-bap-project-rules"
            - "runtime.md#rt-bap-maintenance-rules"
          note: "Policy force is specified; it is not host enforcement."
        - scope: "Retained live wiki-first project rules at future question/edit model consumers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "claimed"
              records:
                - "runtime.md#rt-clm-wiki-first"
                - "runtime.md#rt-bap-project-rules"
                - "runtime.md#rt-rte-wiki-lookup"
              note: "The retained live rules give Wiki pages priority over fallback memory and source in later project sessions; relative priority does not require numerical scores."
          records:
            - "runtime.md#rt-clm-wiki-first"
            - "runtime.md#rt-bap-project-rules"
            - "runtime.md#rt-rte-wiki-lookup"
          note: "This specified priority effect coexists with standing instruction and operation-selection effects; actual host loading and model compliance remain unobserved."
        - scope: "Index mappings, freshness/path metadata, health predicates and log deferrals at lookup and maintenance selectors"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-health"
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-wiki-lookup"
                - "runtime.md#rt-rte-diff-ingest"
                - "runtime.md#rt-rte-gap-audit"
              note: "Intent mappings, source references, stale flags and logged gaps select pages, fallback or repair work."
          records:
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-health"
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-wiki-lookup"
            - "runtime.md#rt-rte-diff-ingest"
            - "runtime.md#rt-rte-gap-audit"
          note: "These selector effects concern scope and operation; the separate live-rule unit preserves wiki-first relative priority as ranking without requiring a numerical algorithm."
        - scope: "Retained schema/template criteria at authoring and audit conformity checks"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-schema"
                - "memory.md#mem-obj-templates"
                - "epistemic.md#epi-rte-schema-check"
                - "runtime.md#rt-rte-gap-audit"
              note: "Required fields and page conventions supply criteria for checking and repairing conformity."
          records:
            - "runtime.md#rt-obj-schema"
            - "memory.md#mem-obj-templates"
            - "epistemic.md#epi-rte-schema-check"
            - "runtime.md#rt-rte-gap-audit"
          note: "Diagnostic/schema force is bounded to conformity; incomplete grep checks do not certify page truth."
        - scope: "Task-derived gap reports at ingest/audit updates to durable pages"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-diff-ingest"
                - "runtime.md#rt-rte-gap-audit"
                - "memory.md#mem-obj-wiki"
              note: "Retained task experience feeds model revision of durable references used by later answering models."
          records:
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-diff-ingest"
            - "runtime.md#rt-rte-gap-audit"
            - "memory.md#mem-obj-wiki"
          note: "Learning authority at the update consumer is distinct from knowledge authority at the downstream page reader and from improved capacity."
      records:
        - "memory.md#mem-obj-sources"
        - "memory.md#mem-obj-wiki"
        - "runtime.md#rt-rte-wiki-lookup"
        - "runtime.md#rt-obj-schema"
        - "runtime.md#rt-obj-wiki-ingest"
        - "memory.md#mem-obj-templates"
        - "runtime.md#rt-bap-project-rules"
        - "runtime.md#rt-bap-maintenance-rules"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-health"
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-rte-diff-ingest"
        - "runtime.md#rt-rte-gap-audit"
        - "epistemic.md#epi-rte-schema-check"
        - "runtime.md#rt-clm-wiki-first"
      note: "Coverage concerns the specified consumer/effect paths, including live-rule instruction and wiki-first ranking, selection routing and diagnostics. Ranking is warranted by the ordered lookup policy in runtime.md#rt-clm-wiki-first as well as its rule channel and lookup consumer. No retained veto or enforcement consumer is established; all positive force remains claimed design."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Bootstrap page/support generation, task gap/stale bookkeeping, diff ingest and audit model repairs"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-vault-bootstrap"
                - "runtime.md#rt-rte-wiki-lookup"
                - "runtime.md#rt-rte-diff-ingest"
                - "runtime.md#rt-rte-gap-audit"
              note: "Models admit writes without a required per-content human decision; workflow initiation and later committing do not make admission manual."
          records:
            - "runtime.md#rt-rte-vault-bootstrap"
            - "runtime.md#rt-rte-wiki-lookup"
            - "runtime.md#rt-rte-diff-ingest"
            - "runtime.md#rt-rte-gap-audit"
          note: "These specified admission mechanisms are computational, although actual host write permissions and execution are unavailable."
        - scope: "Invoked source sync copy/header admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-source-sync"
                - "memory.md#mem-obj-sources"
              note: "Fixed shell selection admits copies once invoked without per-file human approval."
          records:
            - "runtime.md#rt-rte-source-sync"
            - "memory.md#mem-obj-sources"
          note: "Original source authorship is separate from copy admission."
        - scope: "Initial existing-vault/project-memory admission and G2 manual-copy alternative"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-sources"
            - "runtime.md#rt-obj-schema"
            - "runtime.md#rt-rte-gap-audit"
          note: "Initial content control is unspecified. Manual copy names a physical recovery action without establishing an explicit human content decision; the foreground audit model may perform it."
      records:
        - "runtime.md#rt-rte-vault-bootstrap"
        - "runtime.md#rt-rte-wiki-lookup"
        - "runtime.md#rt-rte-diff-ingest"
        - "runtime.md#rt-rte-gap-audit"
        - "runtime.md#rt-rte-source-sync"
        - "memory.md#mem-obj-sources"
        - "runtime.md#rt-obj-schema"
      note: "Known automatic admissions coexist with unresolved initial and alternate copy control. No supported explicit human content gate justifies manual."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Ingest section/page revisions, audit content/link/metadata/protocol repairs and edit-time stale marking"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-diff-ingest"
                - "runtime.md#rt-rte-gap-audit"
                - "memory.md#mem-obj-page-metadata"
              note: "Existing entries, references and method files are revised by instructed model updates."
            - value: "invalidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-wiki-lookup"
                - "memory.md#mem-obj-page-metadata"
              note: "Stale flags retain history/content but withdraw current reliance at the specified status consumer, which falls back when stale."
          records:
            - "runtime.md#rt-rte-diff-ingest"
            - "runtime.md#rt-rte-gap-audit"
            - "runtime.md#rt-rte-wiki-lookup"
            - "memory.md#mem-obj-page-metadata"
          note: "The invalidation finding is local to stale-sensitive status consumption, not a universal stale-page rejection gate."
        - scope: "Compilation/new-page production from sources and task gaps"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-diff-ingest"
            - "runtime.md#rt-rte-vault-bootstrap"
            - "epistemic.md#epi-obj-wiki-pages"
          note: "Records specify summaries/excerpts/explanations but provide no source/page pairs to establish semantic preservation or a new claim. The analyst phrase synthesis alone cannot establish controlled synthesize; consolidation versus synthesis remains unresolved."
        - scope: "Source copying and query/index acquisition machinery"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-source-sync"
            - "memory.md#mem-obj-health"
            - "memory.md#mem-obj-index"
          note: "Copying, warning insertion and query/index support alone are not a controlled semantic curation operation over existing claims."
      records:
        - "runtime.md#rt-rte-diff-ingest"
        - "runtime.md#rt-rte-gap-audit"
        - "runtime.md#rt-rte-wiki-lookup"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-wiki"
        - "runtime.md#rt-rte-vault-bootstrap"
        - "epistemic.md#epi-obj-wiki-pages"
        - "runtime.md#rt-rte-source-sync"
        - "memory.md#mem-obj-health"
        - "memory.md#mem-obj-index"
      note: "Supported revisions and bounded stale invalidation do not resolve compilation semantics, deletion/retirement or all proposed maintenance transformations."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Question/edit/status page lookup and requested bootstrap/ingest/audit reads of retained references and metadata"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-wiki-lookup"
                - "runtime.md#rt-rte-diff-ingest"
                - "runtime.md#rt-rte-gap-audit"
                - "memory.md#mem-obj-index"
                - "memory.md#mem-obj-health"
              note: "A task or maintenance invocation requests retained material, then models/tools select and load it; delivery fulfilling those reads is not another push."
          records:
            - "runtime.md#rt-rte-wiki-lookup"
            - "runtime.md#rt-rte-diff-ingest"
            - "runtime.md#rt-rte-gap-audit"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-health"
          note: "Intent matching and diagnostic selection occur inside the requested read chain; no unsolicited page injection is specified."
        - scope: "Later delivery/loading of generated live project rules and command guidance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-bap-project-rules"
            - "runtime.md#rt-bap-maintenance-rules"
            - "runtime.md#rt-obj-wiki-ingest"
          note: "The records specify future instruction channels but leave host discovery/loading uninspected; whether delivery is automatic push or explicit requested pull cannot be determined."
      records:
        - "runtime.md#rt-rte-wiki-lookup"
        - "runtime.md#rt-rte-diff-ingest"
        - "runtime.md#rt-rte-gap-audit"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-bap-project-rules"
        - "runtime.md#rt-bap-maintenance-rules"
        - "runtime.md#rt-obj-wiki-ingest"
      note: "Known requested content reads coexist with unresolved host instruction delivery. Host context management and provider state are excluded, but included live generated rules are not silently dropped."
    read_back_signal:
      assessment: "not-determinable"
      units:
        - scope: "Requested file/page/query read chains"
          assessment: "inapplicable"
          findings: []
          records:
            - "runtime.md#rt-rte-wiki-lookup"
            - "runtime.md#rt-rte-diff-ingest"
            - "runtime.md#rt-rte-gap-audit"
            - "memory.md#mem-obj-index"
            - "memory.md#mem-obj-health"
          note: "These inspected design routes are pull; their path identifiers and intent matching are not push selectors."
        - scope: "Possible host delivery of generated live rules/commands"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-bap-project-rules"
            - "runtime.md#rt-bap-maintenance-rules"
            - "runtime.md#rt-obj-wiki-ingest"
          note: "No automatic trigger, selector input or selected delivered part is recorded for host loading. Neither coarse nor targeted push signal is supported."
      records:
        - "runtime.md#rt-rte-wiki-lookup"
        - "runtime.md#rt-rte-diff-ingest"
        - "runtime.md#rt-rte-gap-audit"
        - "memory.md#mem-obj-index"
        - "memory.md#mem-obj-health"
        - "runtime.md#rt-bap-project-rules"
        - "runtime.md#rt-bap-maintenance-rules"
        - "runtime.md#rt-obj-wiki-ingest"
      note: "No supported push signal is classifiable; an unresolved included delivery alternative prevents a pull-only system-wide inapplicable assessment."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Task-insufficiency gap report to ingest/audit page revision to later lookup"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-log"
                - "runtime.md#rt-rte-diff-ingest"
                - "runtime.md#rt-rte-gap-audit"
                - "memory.md#mem-obj-wiki"
                - "runtime.md#rt-rte-wiki-lookup"
              note: "Task experience produces retained gap diagnoses, consumed by computational repair to write durable pages for subsequent answering context."
          records:
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-diff-ingest"
            - "runtime.md#rt-rte-gap-audit"
            - "memory.md#mem-obj-wiki"
            - "runtime.md#rt-rte-wiki-lookup"
          note: "This is a claimed automatic experience-fed update, not a claim of raw conversation collection, weight training, exercised learning or benefit."
        - scope: "Existing project-memory input and other compilation/repair inputs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-sources"
            - "runtime.md#rt-rte-vault-bootstrap"
            - "runtime.md#rt-rte-gap-audit"
            - "runtime.md#rt-obj-schema"
          note: "Installation-specific memory content and provenance are unknown; the records do not establish whether additional trace-fed writes qualify."
      records:
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-rte-diff-ingest"
        - "runtime.md#rt-rte-gap-audit"
        - "memory.md#mem-obj-wiki"
        - "runtime.md#rt-rte-wiki-lookup"
        - "memory.md#mem-obj-sources"
        - "runtime.md#rt-rte-vault-bootstrap"
        - "runtime.md#rt-obj-schema"
      note: "The gap-fed route supports a positive at the design layer while opaque project-memory provenance prevents complete trace-learning coverage. No bounded absence record supports a local or system-wide no."
    trace_source:
      assessment: "not-determinable"
      units:
        - scope: "Qualifying task-gap-fed page repair"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-log"
            - "runtime.md#rt-rte-diff-ingest"
            - "runtime.md#rt-rte-gap-audit"
          note: "Gap entries are one-sentence task/maintenance reports, explicitly not raw conversation or tool traces. Recorded topic/task/diagnosis does not establish session-logs, tool-traces, trajectories or a discrete runtime/environment event-stream origin; original input needed to select a controlled source remains unspecified."
        - scope: "Other possible project-memory-fed updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-sources"
            - "runtime.md#rt-rte-vault-bootstrap"
            - "runtime.md#rt-rte-gap-audit"
          note: "The source content/origin of installation-specific project memory is unavailable, so no additional qualifying trace-source value can be assigned."
      records:
        - "memory.md#mem-obj-log"
        - "runtime.md#rt-rte-diff-ingest"
        - "runtime.md#rt-rte-gap-audit"
        - "memory.md#mem-obj-sources"
        - "runtime.md#rt-rte-vault-bootstrap"
      note: "A claimed trace-learning route need not have a determinable controlled trace-source value. Serializing experience as a log entry does not establish event-stream origin."
---

# LLM Project Wiki memory profile

## Comparison rationale

The accepted records describe a prompt-defined file memory design, not an installed runtime. Every positive finding therefore has claimed basis. Complete coverage of a specified inventory does not upgrade its evidence to wiring, operation or benefit. Provider weights and host compaction are outside the memory boundary; unknown delivery of included live rules remains inside it.

Compilation, admission and consumption are separate. [MEM-OBJ-sources](memory.md#mem-obj-sources) supports imported reference copies; [MEM-OBJ-wiki](memory.md#mem-obj-wiki) supports model-authored pages. [EPI-OBJ-wiki-pages](epistemic.md#epi-obj-wiki-pages) preserves uncertainty about semantic derivation, so new-page creation is not automatically controlled synthesis or consolidation. Revisions of existing entries do support evolution. Stale marking supports invalidation only at the specified stale-sensitive status consumer, not universal withdrawal; [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup) and [MEM-CLM-retention-limits](memory.md#mem-clm-retention-limits) retain that distinction.

The retained live project rules give Wiki pages relative priority over fallback memory and source at the future question/edit model consumer. This is ranking authority at claimed basis, supported by the ordered flow in [RT-CLM-wiki-first](runtime.md#rt-clm-wiki-first), the retained future-session channel in [RT-BAP-project-rules](runtime.md#rt-bap-project-rules) and its consumer operation in [RT-RTE-wiki-lookup](runtime.md#rt-rte-wiki-lookup). It coexists with instruction authority for standing directions and routing authority for operation/scope selection. No numerical ranking algorithm is required; actual loading and compliance remain unobserved. Known authority coverage describes these specified effects, not deployed enforcement.

The gap route gives retained experience learning authority at the repair consumer, and its revised page knowledge authority at later lookup. [MEM-OBJ-log](memory.md#mem-obj-log) and the memory annotation on [RT-RTE-diff-ingest](runtime.md#rt-rte-diff-ingest) support the claimed chain without proving improved capacity. Reports of task insufficiency do not establish one of the four controlled original trace sources; no raw conversation, tool recording or state/action/outcome sequence is supplied. Unknown project-memory provenance remains a separate unresolved branch.

Requested index/page/diagnostic reads are pull, even when a model or fixed predicate selects candidates within the request. [RT-BAP-project-rules](runtime.md#rt-bap-project-rules) and [RT-BAP-maintenance-rules](runtime.md#rt-bap-maintenance-rules) specify future live channels without exposing their host loading operation. This prevents classifying all read-back as pull-only or assigning an unsupported push signal. File paths on requested reads do not establish identifier-based push.

Reconciliation supersedes EPI-OBJ-sources and EPI-OBJ-log with the corresponding memory objects. Findings cite those canonical memory declarations. EPI-OBJ-wiki-pages and EPI-OBJ-index remain valid containers; finer memory parts distinguish domain content, metadata, navigation and health predicates rather than flattening their effects. No classification depends on a superseded record.

Source-read log: no frozen source files were read for this profile. Classification uses only the supplied accepted members and reconciliation; no new evidence or records were added.
