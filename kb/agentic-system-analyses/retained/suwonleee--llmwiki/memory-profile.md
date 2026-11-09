---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "llmwiki memory comparison: transcript-derived project wiki, rule and recall metadata, feedback selectors and maintenance state; alternate channels remain partially inventoried."
run-id: "AAS-2026-11-08-llmwiki-7f7e35008c0f-01"
source-identity: "https://github.com/suwonleee/llmwiki"
reviewed-boundary: "e6be788bdfd969c3695f839a5d6b5752bb233cfc"
memory-comparison:
  version: 2
  scope: "Accumulated project wiki/L0/topic prose, rule/recall parts, raw session pointers/exports, capture receipts, SQLite index/provenance, review/gap work state, human quiz notebook/schedule, emissions, version-bound feedback/rechecks, silver regression cases, affinity and disposable cross-invocation turn selector state. Includes unresolved commit/absence channel inputs and partially inventoried maintenance/import alternatives. Excludes static shipped skills/conventions as memory products, ordinary single-call working state, external host-window machinery and provider parameters not shown updated by a scoped memory route."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - 
          scope: "Project wiki, rule metadata, human quiz notebook and advisory review files"
          assessment: "known"
          findings:
            - 
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-pages"
                - "memory.md#mem-obj-wiki-rules"
                - "memory.md#mem-obj-quiz-ledger"
                - "memory.md#mem-obj-review-reports"
              note: "Markdown bodies and YAML persist on disk."
            - 
              value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-pages"
                - "memory.md#mem-obj-quiz-ledger"
                - "memory.md#mem-obj-review-reports"
              note: "These retained project Markdown products live in the project repository; this does not assert that every change is committed."
          records:
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-obj-wiki-rules"
            - "memory.md#mem-obj-quiz-ledger"
            - "memory.md#mem-obj-review-reports"
          note: "These named file-backed products are resolved; they are distinct from provider weights."
        - 
          scope: "Engine capture queue, wiki index, reference graph and freshness receipts"
          assessment: "known"
          findings:
            - 
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-capture-state"
                - "memory.md#mem-obj-wiki-index"
                - "memory.md#mem-rte-freshness-recheck"
              note: "capture.db/index.db hold symbolic queue/index/receipt state; graph rows are SQLite data, not evidence of a separate graph database."
          records:
            - "memory.md#mem-obj-capture-state"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-rte-freshness-recheck"
          note: "Covers the declared database-backed retained objects."
        - 
          scope: "Machine-local emissions, feedback, aggregates, gap history and disposable session selector state"
          assessment: "known"
          findings:
            - 
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-emission-ledger"
                - "memory.md#mem-obj-usage-affinity"
                - "memory.md#mem-obj-work-feedback"
                - "epistemic.md#epi-obj-gap-task"
                - "runtime.md#rt-rte-context-delivery"
              note: "JSONL/JSON/Markdown files retain access and evaluation state, including OS-temp turn state."
          records:
            - "memory.md#mem-obj-emission-ledger"
            - "memory.md#mem-obj-usage-affinity"
            - "memory.md#mem-obj-work-feedback"
            - "epistemic.md#epi-obj-gap-task"
            - "runtime.md#rt-rte-context-delivery"
          note: "Session state survives later invocations within a session; disposability does not remove it from memory."
        - 
          scope: "Included alternate commit/absence context channels and their retained inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "Accepted records name these alternatives but do not inventory their retained parts. Storage classification cannot be completed from the wiki witness."
      records:
        - "memory.md#mem-obj-wiki-pages"
        - "memory.md#mem-obj-wiki-rules"
        - "memory.md#mem-obj-quiz-ledger"
        - "memory.md#mem-obj-review-reports"
        - "memory.md#mem-obj-capture-state"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-rte-freshness-recheck"
        - "memory.md#mem-obj-emission-ledger"
        - "memory.md#mem-obj-usage-affinity"
        - "memory.md#mem-obj-work-feedback"
        - "epistemic.md#epi-obj-gap-task"
        - "runtime.md#rt-rte-context-delivery"
      note: "Known file/repository and SQLite witnesses coexist with uninspected alternate-channel retained inputs. External provider weights are not an operative memory write established by these records."
    representational_form:
      assessment: "partial"
      units:
        - 
          scope: "Wiki prose, delivered rule imperatives, review criticisms, human quiz text and feedback reasons"
          assessment: "known"
          findings:
            - 
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-pages"
                - "memory.md#mem-obj-wiki-rules"
                - "memory.md#mem-obj-review-reports"
                - "memory.md#mem-obj-quiz-ledger"
                - "memory.md#mem-obj-usage-affinity"
                - "memory.md#mem-obj-work-feedback"
              note: "Model or human interpretation consumes claims, reminders, criticisms, answers and reasons."
          records:
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-obj-wiki-rules"
            - "memory.md#mem-obj-review-reports"
            - "memory.md#mem-obj-quiz-ledger"
            - "memory.md#mem-obj-usage-affinity"
            - "memory.md#mem-obj-work-feedback"
          note: "Classification applies to interpreted text, not every byte of the containing files."
        - 
          scope: "Paths, globs, offsets, hashes, schedules, gap status, lexical trigger projection and numerical affinity/term aggregates"
          assessment: "known"
          findings:
            - 
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-capture-state"
                - "memory.md#mem-obj-wiki-index"
                - "memory.md#mem-obj-recall-triggers"
                - "memory.md#mem-obj-emission-ledger"
                - "memory.md#mem-obj-usage-affinity"
                - "memory.md#mem-obj-work-feedback"
                - "memory.md#mem-obj-quiz-ledger"
                - "epistemic.md#epi-obj-gap-task"
                - "runtime.md#rt-rte-context-delivery"
              note: "Localized fields have fixed consumer rules. Trigger strings are substring/rareness inputs; numeric counts and term weights are not distributed parameters."
          records:
            - "memory.md#mem-obj-capture-state"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-obj-recall-triggers"
            - "memory.md#mem-obj-emission-ledger"
            - "memory.md#mem-obj-usage-affinity"
            - "memory.md#mem-obj-work-feedback"
            - "memory.md#mem-obj-quiz-ledger"
            - "epistemic.md#epi-obj-gap-task"
            - "runtime.md#rt-rte-context-delivery"
          note: "Separates the same rule string's lexical selection path from its imperative interpretation."
        - 
          scope: "Included alternate commit/absence context channels and their retained inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "Accepted records name these alternatives but do not inventory their retained parts. Representational form cannot be completed from the wiki witness."
      records:
        - "memory.md#mem-obj-wiki-pages"
        - "memory.md#mem-obj-wiki-rules"
        - "memory.md#mem-obj-review-reports"
        - "memory.md#mem-obj-quiz-ledger"
        - "memory.md#mem-obj-usage-affinity"
        - "memory.md#mem-obj-work-feedback"
        - "memory.md#mem-obj-capture-state"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-obj-recall-triggers"
        - "memory.md#mem-obj-emission-ledger"
        - "epistemic.md#epi-obj-gap-task"
        - "runtime.md#rt-rte-context-delivery"
      note: "Both interpreted prose and fixed-rule metadata are established. No retained embedding or parameter update is established; missing alternatives prevent complete enumeration."
    lineage:
      assessment: "partial"
      units:
        - 
          scope: "Compiled wiki/L0/topic knowledge and explicit usage-derived selector metadata"
          assessment: "known"
          findings:
            - 
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-warm-save"
                - "runtime.md#rt-rte-auto-update"
                - "memory.md#mem-rte-topic-merge"
                - "memory.md#mem-rte-feedback-fold"
              note: "Session extracts become durable pages; emitted/read/use experience becomes selector aggregates."
            - 
              value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-warm-save"
                - "runtime.md#rt-rte-auto-update"
                - "memory.md#mem-rte-topic-merge"
              note: "Foreground or optional model authors page content rather than retaining only verbatim logs."
          records:
            - "runtime.md#rt-rte-warm-save"
            - "runtime.md#rt-rte-auto-update"
            - "memory.md#mem-rte-topic-merge"
            - "memory.md#mem-rte-feedback-fold"
          note: "Known derivation paths do not resolve provenance of all existing pages."
        - 
          scope: "Explicit arbitrary-file ingest and source acquisition"
          assessment: "known"
          findings:
            - 
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-auto-update"
                - "memory.md#mem-obj-capture-state"
              note: "Ingest annotation admits dropped source text; capture retains external session sources/pointers."
          records:
            - "runtime.md#rt-rte-auto-update"
            - "memory.md#mem-obj-capture-state"
          note: "Imported static documents are not automatically traces."
        - 
          scope: "Index, lexical trigger projection, emissions, schedules, gap state and navigation products"
          assessment: "known"
          findings:
            - 
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-index"
                - "memory.md#mem-obj-recall-triggers"
                - "memory.md#mem-obj-emission-ledger"
                - "memory.md#mem-obj-quiz-ledger"
                - "epistemic.md#epi-rte-gap-disposition"
                - "epistemic.md#epi-rte-navigation-view"
              note: "Deterministic parsing, hashing, counting and view assembly derive retained access structures from pages/activity."
          records:
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-obj-recall-triggers"
            - "memory.md#mem-obj-emission-ledger"
            - "memory.md#mem-obj-quiz-ledger"
            - "epistemic.md#epi-rte-gap-disposition"
            - "epistemic.md#epi-rte-navigation-view"
          note: "Classifies these derivations independently of initial content provenance."
        - 
          scope: "Initialization of arbitrary existing pages and recall phrases"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-obj-recall-triggers"
          note: "Initial page/phrase provenance is unresolved; known later maintenance does not classify every initial entry."
        - 
          scope: "Included alternate commit/absence context channels and their retained inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "Accepted records name these alternatives but do not inventory their retained parts. Lineage cannot be completed from the wiki witness."
      records:
        - "runtime.md#rt-rte-warm-save"
        - "runtime.md#rt-rte-auto-update"
        - "memory.md#mem-rte-topic-merge"
        - "memory.md#mem-rte-feedback-fold"
        - "memory.md#mem-obj-capture-state"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-obj-recall-triggers"
        - "memory.md#mem-obj-emission-ledger"
        - "memory.md#mem-obj-quiz-ledger"
        - "epistemic.md#epi-rte-gap-disposition"
        - "epistemic.md#epi-rte-navigation-view"
        - "memory.md#mem-obj-wiki-pages"
        - "runtime.md#rt-rte-context-delivery"
      note: "Authorship, import, trace extraction and other compilation coexist by path; neither initial provenance nor alternate-channel inputs are fully recorded."
    behavioral_authority:
      assessment: "partial"
      units:
        - 
          scope: "Wiki claims, L0 and review advice at later answering/maintenance consumers"
          assessment: "known"
          findings:
            - 
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-pages"
                - "runtime.md#rt-rte-context-delivery"
                - "epistemic.md#epi-rte-semantic-review"
              note: "Wiki text supplies project reference context; advisory review reports supply candidate criticism, not certified truth."
          records:
            - "memory.md#mem-obj-wiki-pages"
            - "runtime.md#rt-rte-context-delivery"
            - "epistemic.md#epi-rte-semantic-review"
          note: "Knowledge authority means reference use, not epistemic endorsement."
        - 
          scope: "Rule imperative at host model and scoped first-edit gate"
          assessment: "known"
          findings:
            - 
              value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-rules"
                - "runtime.md#rt-rte-edit-rules"
              note: "Eligible rule text reaches the host as an imperative reminder."
            - 
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-rules"
                - "runtime.md#rt-rte-edit-rules"
              note: "Rule/path state can cause a first matching edit denial; host enforcement and retries bound its force."
          records:
            - "memory.md#mem-obj-wiki-rules"
            - "runtime.md#rt-rte-edit-rules"
          note: "No reliable compliance or universal write veto follows."
        - 
          scope: "Lexical triggers and bounded usage statistics at retrieval rankers"
          assessment: "known"
          findings:
            - 
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-recall-triggers"
                - "memory.md#mem-obj-usage-affinity"
                - "memory.md#mem-rte-feedback-fold"
              note: "Rule-plus-recall strings affect fixed lexical scores; usage counts change eligible near-tie ordering."
          records:
            - "memory.md#mem-obj-recall-triggers"
            - "memory.md#mem-obj-usage-affinity"
            - "memory.md#mem-rte-feedback-fold"
          note: "Recall selection is not imperative delivery."
        - 
          scope: "Queue offsets, gap status and human quiz schedule at their next-work selectors"
          assessment: "known"
          findings:
            - 
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-capture-state"
                - "epistemic.md#epi-obj-gap-task"
                - "epistemic.md#epi-rte-gap-disposition"
                - "memory.md#mem-obj-quiz-ledger"
              note: "Offsets choose extraction windows; open gap state selects maintenance work; due/box fields select human recall items."
          records:
            - "memory.md#mem-obj-capture-state"
            - "epistemic.md#epi-obj-gap-task"
            - "epistemic.md#epi-rte-gap-disposition"
            - "memory.md#mem-obj-quiz-ledger"
          note: "These metadata consumers differ from knowledge consumers."
        - 
          scope: "Versioned wrong/freshness markers at rule eligibility"
          assessment: "known"
          findings:
            - 
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-usage-affinity"
                - "memory.md#mem-rte-feedback-fold"
                - "memory.md#mem-rte-freshness-recheck"
                - "runtime.md#rt-rte-edit-rules"
              note: "Retained revision/currency markers determine eligibility for supplying a rule."
            - 
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-usage-affinity"
                - "memory.md#mem-rte-feedback-fold"
                - "memory.md#mem-rte-freshness-recheck"
                - "runtime.md#rt-rte-edit-rules"
              note: "The same markers withhold ineligible imperative text while ordinary prose can remain warned."
          records:
            - "memory.md#mem-obj-usage-affinity"
            - "memory.md#mem-rte-feedback-fold"
            - "memory.md#mem-rte-freshness-recheck"
            - "runtime.md#rt-rte-edit-rules"
          note: "Version-specific withholding is not a permanent path-wide ban."
        - 
          scope: "Stored silver required/forbidden strings at regression replay"
          assessment: "known"
          findings:
            - 
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-work-feedback"
                - "epistemic.md#epi-rte-feedback-replay"
              note: "Retained author expectations define excerpt conformance; result is diagnostic, not project-truth acceptance."
          records:
            - "memory.md#mem-obj-work-feedback"
            - "epistemic.md#epi-rte-feedback-replay"
          note: "No ranking reward or independent answer truth follows."
        - 
          scope: "Retained session experience and usage receipts at automatic durable update consumers"
          assessment: "known"
          findings:
            - 
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-warm-save"
                - "runtime.md#rt-rte-auto-update"
                - "memory.md#mem-rte-topic-merge"
                - "memory.md#mem-rte-feedback-fold"
              note: "Experience feeds page compilation or durable selector adaptation. Outputs separately supply knowledge, instructions or ranking."
          records:
            - "runtime.md#rt-rte-warm-save"
            - "runtime.md#rt-rte-auto-update"
            - "memory.md#mem-rte-topic-merge"
            - "memory.md#mem-rte-feedback-fold"
          note: "Learning authority at the update consumer is not demonstrated capacity improvement."
        - 
          scope: "Included alternate commit/absence context channels and their retained inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "Accepted records name these alternatives but do not inventory their retained parts. Consumer and authority classification cannot be completed from the wiki witness."
      records:
        - "memory.md#mem-obj-wiki-pages"
        - "runtime.md#rt-rte-context-delivery"
        - "epistemic.md#epi-rte-semantic-review"
        - "memory.md#mem-obj-wiki-rules"
        - "runtime.md#rt-rte-edit-rules"
        - "memory.md#mem-obj-recall-triggers"
        - "memory.md#mem-obj-usage-affinity"
        - "memory.md#mem-rte-feedback-fold"
        - "memory.md#mem-obj-capture-state"
        - "epistemic.md#epi-obj-gap-task"
        - "epistemic.md#epi-rte-gap-disposition"
        - "memory.md#mem-obj-quiz-ledger"
        - "memory.md#mem-rte-freshness-recheck"
        - "memory.md#mem-obj-work-feedback"
        - "epistemic.md#epi-rte-feedback-replay"
        - "runtime.md#rt-rte-warm-save"
        - "runtime.md#rt-rte-auto-update"
        - "memory.md#mem-rte-topic-merge"
      note: "All seven forces have local supporting consumers. Their scope and evidential status remain separate; alternate read-back inputs prevent a complete authority inventory."
    write_agency:
      assessment: "partial"
      units:
        - 
          scope: "Routine foreground and optional engine page admission; topic replacement; feedback aggregate and deterministic metadata writes"
          assessment: "known"
          findings:
            - 
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-warm-save"
                - "runtime.md#rt-rte-auto-update"
                - "memory.md#mem-rte-topic-merge"
                - "memory.md#mem-rte-feedback-fold"
                - "memory.md#mem-obj-wiki-index"
                - "memory.md#mem-obj-emission-ledger"
                - "epistemic.md#epi-rte-gap-disposition"
                - "memory.md#mem-obj-quiz-ledger"
                - "memory.md#mem-rte-tier-cleanup"
              note: "Models/software admit routine content or compute metadata without per-content human approval. Starting save or passing commit does not make these admissions manual."
          records:
            - "runtime.md#rt-rte-warm-save"
            - "runtime.md#rt-rte-auto-update"
            - "memory.md#mem-rte-topic-merge"
            - "memory.md#mem-rte-feedback-fold"
            - "memory.md#mem-obj-wiki-index"
            - "memory.md#mem-obj-emission-ledger"
            - "epistemic.md#epi-rte-gap-disposition"
            - "memory.md#mem-obj-quiz-ledger"
            - "memory.md#mem-rte-tier-cleanup"
          note: "Includes code-selected tier updates, not ambiguous reviewed tier decisions."
        - 
          scope: "Human direction review under warm save and approved ask answer file-back"
          assessment: "known"
          findings:
            - 
              value: "manual"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-warm-save"
                - "memory.md#mem-rte-query-fileback"
              note: "Procedure requires a human direction answer or explicit approval of the proposed reusable answer before filing."
          records:
            - "runtime.md#rt-rte-warm-save"
            - "memory.md#mem-rte-query-fileback"
          note: "These are human-decision policies, not parser guarantees or observed signatures."
        - 
          scope: "Ambiguous tier changes approved through review IDs"
          assessment: "known"
          findings:
            - 
              value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tier-cleanup"
              note: "Reviewed path selects accepted IDs and checks hashes before application; human editing is the declared policy, not authenticated identity."
          records:
            - "memory.md#mem-rte-tier-cleanup"
          note: "Separate from automatic tier writes; no observed human approval is claimed."
        - 
          scope: "Generic freshness/recheck/receipt callers and initial existing content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-freshness-recheck"
            - "epistemic.md#epi-rte-feedback-recheck"
            - "epistemic.md#epi-rte-reflection-receipt"
            - "memory.md#mem-obj-recall-triggers"
          note: "APIs validate structure/revisions but generic caller identity does not determine per-content human control; initial phrase admission is unresolved."
        - 
          scope: "Included alternate commit/absence context channels and their retained inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "Accepted records name these alternatives but do not inventory their retained parts. Admission control cannot be completed from the wiki witness."
      records:
        - "runtime.md#rt-rte-warm-save"
        - "runtime.md#rt-rte-auto-update"
        - "memory.md#mem-rte-topic-merge"
        - "memory.md#mem-rte-feedback-fold"
        - "memory.md#mem-obj-wiki-index"
        - "memory.md#mem-obj-emission-ledger"
        - "epistemic.md#epi-rte-gap-disposition"
        - "memory.md#mem-obj-quiz-ledger"
        - "memory.md#mem-rte-tier-cleanup"
        - "memory.md#mem-rte-query-fileback"
        - "memory.md#mem-rte-freshness-recheck"
        - "epistemic.md#epi-rte-feedback-recheck"
        - "epistemic.md#epi-rte-reflection-receipt"
        - "memory.md#mem-obj-recall-triggers"
        - "runtime.md#rt-rte-context-delivery"
      note: "Automatic writes and explicit human-decision routes coexist; caller-dependent acknowledgements and initialization remain unresolved."
    curation_operations:
      assessment: "partial"
      units:
        - 
          scope: "Transcript-to-page extraction and living-topic combination"
          assessment: "known"
          findings:
            - 
              value: "consolidate"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-auto-update"
                - "memory.md#mem-rte-topic-merge"
              note: "Useful source material is reduced/combined into page/topic claims; raw input may remain."
            - 
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-topic-merge"
              note: "Existing topic content can be replaced in place; failed-merge lint does not guarantee rollback."
          records:
            - "runtime.md#rt-rte-auto-update"
            - "memory.md#mem-rte-topic-merge"
          note: "Classification follows transformation, not the command name; complete claim preservation is not established."
        - 
          scope: "Foreground save/deep L0 and raw-grounded distillation policy"
          assessment: "known"
          findings:
            - 
              value: "consolidate"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-warm-save"
                - "runtime.md#rt-rte-deep-maintenance"
              note: "Model is instructed to reduce useful experience and rebuild oversized pages from cited raw sources."
            - 
              value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-warm-save"
                - "runtime.md#rt-rte-deep-maintenance"
              note: "L0/rules/topic knowledge are revised by foreground procedure."
          records:
            - "runtime.md#rt-rte-warm-save"
            - "runtime.md#rt-rte-deep-maintenance"
          note: "Model compliance is not observed; deterministic distill check preserves only source sets/conflict lines."
        - 
          scope: "Tiering, version-bound withdrawal and context relevance state"
          assessment: "known"
          findings:
            - 
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-tier-cleanup"
                - "runtime.md#rt-rte-context-delivery"
              note: "Cold tier suppresses automatic body excerpts; session term weights halve and expire."
            - 
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-feedback-fold"
                - "memory.md#mem-rte-freshness-recheck"
                - "memory.md#mem-rte-tier-cleanup"
              note: "Wrong/currency/retirement controls withdraw current reliance on selected parts while history/text can remain."
          records:
            - "memory.md#mem-rte-tier-cleanup"
            - "runtime.md#rt-rte-context-delivery"
            - "memory.md#mem-rte-feedback-fold"
            - "memory.md#mem-rte-freshness-recheck"
          note: "Withholding differs by consumer; ordinary prose may remain visible with a warning."
        - 
          scope: "Repeated usage evidence at eligible-page ranking"
          assessment: "known"
          findings:
            - 
              value: "promote"
              basis: "wired"
              records:
                - "memory.md#mem-rte-feedback-fold"
                - "epistemic.md#epi-rte-affinity-update"
              note: "Positive usage can raise near-tie priority or bounded list prominence; it does not establish truth."
          records:
            - "memory.md#mem-rte-feedback-fold"
            - "epistemic.md#epi-rte-affinity-update"
          note: "Promotion is salience, not page acceptance."
        - 
          scope: "Semantic novelty and duplicate-removal in generated topic/answer/overview content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-topic-merge"
            - "memory.md#mem-rte-query-fileback"
            - "runtime.md#rt-rte-deep-maintenance"
          note: "Accepted records do not establish an output claim absent from its inputs or complete near-duplicate elimination. Requested synthesis and overlap labels alone cannot establish synthesize or dedup."
        - 
          scope: "Included alternate commit/absence context channels and their retained inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "Accepted records name these alternatives but do not inventory their retained parts. Curation transformations cannot be completed from the wiki witness."
      records:
        - "runtime.md#rt-rte-auto-update"
        - "memory.md#mem-rte-topic-merge"
        - "runtime.md#rt-rte-warm-save"
        - "runtime.md#rt-rte-deep-maintenance"
        - "memory.md#mem-rte-tier-cleanup"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-rte-feedback-fold"
        - "memory.md#mem-rte-freshness-recheck"
        - "epistemic.md#epi-rte-affinity-update"
        - "memory.md#mem-rte-query-fileback"
      note: "Supported reduction, revision, decay, withdrawal and salience changes remain local. Novel semantic synthesis and unresolved maintenance/channel transformations prevent complete values."
    read_back_direction:
      assessment: "partial"
      units:
        - 
          scope: "Explicit wiki query, page/raw verification, maintenance, feedback replay and human quiz consumption"
          assessment: "known"
          findings:
            - 
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-obj-wiki-pages"
                - "memory.md#mem-obj-work-feedback"
                - "memory.md#mem-obj-quiz-ledger"
                - "memory.md#mem-rte-topic-merge"
                - "epistemic.md#epi-rte-semantic-review"
              note: "Requested operations read retained pages, prior topics, regression cases or schedules."
            - 
              value: "pull"
              basis: "claimed"
              records:
                - "memory.md#mem-rte-query-fileback"
                - "runtime.md#rt-rte-deep-maintenance"
                - "epistemic.md#epi-rte-human-quiz"
              note: "Foreground procedures explicitly request page/raw reads and maintenance/quiz inputs."
          records:
            - "memory.md#mem-obj-wiki-pages"
            - "memory.md#mem-obj-work-feedback"
            - "memory.md#mem-obj-quiz-ledger"
            - "memory.md#mem-rte-topic-merge"
            - "epistemic.md#epi-rte-semantic-review"
            - "memory.md#mem-rte-query-fileback"
            - "runtime.md#rt-rte-deep-maintenance"
            - "epistemic.md#epi-rte-human-quiz"
          note: "Requested delivery is not counted again as push simply because code returns it."
        - 
          scope: "Automatic SessionStart, prompt and pre-edit knowledge delivery"
          assessment: "known"
          findings:
            - 
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "runtime.md#rt-rte-edit-rules"
              note: "Host events select and inject retained L0, page pointers/excerpts or matching rule reminders without a wiki lookup request."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "runtime.md#rt-rte-edit-rules"
          note: "Cold/turn and edit operations are unsolicited memory supply to the later host invocation."
        - 
          scope: "Included alternate commit/absence context channels and their retained inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "Accepted records name these alternatives but do not inventory their retained parts. Direction and later consumption cannot be completed from the wiki witness."
      records:
        - "memory.md#mem-obj-wiki-pages"
        - "memory.md#mem-obj-work-feedback"
        - "memory.md#mem-obj-quiz-ledger"
        - "memory.md#mem-rte-topic-merge"
        - "epistemic.md#epi-rte-semantic-review"
        - "memory.md#mem-rte-query-fileback"
        - "runtime.md#rt-rte-deep-maintenance"
        - "epistemic.md#epi-rte-human-quiz"
        - "runtime.md#rt-rte-context-delivery"
        - "runtime.md#rt-rte-edit-rules"
      note: "Both requested read-back and unsolicited host-context supply are established. Commit/absence alternatives prevent complete inventory."
    read_back_signal:
      assessment: "partial"
      units:
        - 
          scope: "Cold-start automatic entry-page and list supply"
          assessment: "known"
          findings:
            - 
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
              note: "SessionStart uses enrolled project availability and current-state/overview fallback; list/category budgets supply general context rather than query-targeted matching."
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "Names the trigger, project/L0 availability selector and selected entry/list parts."
        - 
          scope: "Current-prompt page and recall-trigger selection"
          assessment: "known"
          findings:
            - 
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-context-delivery"
                - "memory.md#mem-obj-recall-triggers"
              note: "UserPromptSubmit supplies prompt terms; fixed rarity/coverage/substring scoring selects retained pages, with dedupe, top-three and excerpt budgets."
          records:
            - "runtime.md#rt-rte-context-delivery"
            - "memory.md#mem-obj-recall-triggers"
          note: "Lexical identity features remain query inference, not an identity-key lookup merely because paths are scored."
        - 
          scope: "Before-edit path-to-rule selection"
          assessment: "known"
          findings:
            - 
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-edit-rules"
                - "memory.md#mem-obj-wiki-rules"
              note: "PreToolUse supplies concrete target paths; applies_to globs match identities to select delivered rule parts. Currency and once-per-path markers further filter."
          records:
            - "runtime.md#rt-rte-edit-rules"
            - "memory.md#mem-obj-wiki-rules"
          note: "Actual target match selects supplied content; a page pointer alone would not suffice."
        - 
          scope: "Included alternate commit/absence context channels and their retained inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-context-delivery"
          note: "Accepted records name these alternatives but do not inventory their retained parts. Push selector inputs and selected retained parts cannot be completed from the wiki witness."
      records:
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-obj-recall-triggers"
        - "runtime.md#rt-rte-edit-rules"
        - "memory.md#mem-obj-wiki-rules"
      note: "Coarse cold supply, lexical turn relevance and path-targeted rule delivery coexist. Alternate channels' selectors remain uninspected; no blanket pull-only inapplicability applies."
    trace_learning:
      assessment: "partial"
      units:
        - 
          scope: "Automatic session-extract compilation into durable wiki/L0/topic pages and later context"
          assessment: "known"
          findings:
            - 
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-warm-save"
                - "runtime.md#rt-rte-auto-update"
                - "memory.md#mem-rte-topic-merge"
                - "runtime.md#rt-rte-context-delivery"
              note: "Session traces feed model-authored retained summaries/pages; later host invocations consume them as reference or guidance. A generated summary need not add a novel claim to qualify."
          records:
            - "runtime.md#rt-rte-warm-save"
            - "runtime.md#rt-rte-auto-update"
            - "memory.md#mem-rte-topic-merge"
            - "runtime.md#rt-rte-context-delivery"
          note: "Wiring includes host-model authoring under the procedure and optional generation; actual compliance, exercise and improved capacity are unobserved."
        - 
          scope: "Versioned usage/read experience folded into durable future selectors"
          assessment: "known"
          findings:
            - 
              value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-feedback-fold"
                - "epistemic.md#epi-rte-affinity-update"
                - "runtime.md#rt-rte-context-delivery"
              note: "Recorded emissions/usage/read activity feeds aggregates that later rerank eligible retained pages or withhold rules."
          records:
            - "memory.md#mem-rte-feedback-fold"
            - "epistemic.md#epi-rte-affinity-update"
            - "runtime.md#rt-rte-context-delivery"
          note: "Explicit legacy read scans are available, not an active default daemon learner; no benefit inference."
        - 
          scope: "Other maintenance/import inputs, caller-dependent updates and uninspected alternate-channel memory"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-deep-maintenance"
            - "runtime.md#rt-rte-auto-update"
            - "memory.md#mem-rte-freshness-recheck"
            - "runtime.md#rt-rte-context-delivery"
          note: "Arbitrary ingest can be static rather than trace-derived; maintenance and alternate parts lack a complete qualifying-write inventory. No bounded evidenced-absence record licenses a local no."
      records:
        - "runtime.md#rt-rte-warm-save"
        - "runtime.md#rt-rte-auto-update"
        - "memory.md#mem-rte-topic-merge"
        - "runtime.md#rt-rte-context-delivery"
        - "memory.md#mem-rte-feedback-fold"
        - "epistemic.md#epi-rte-affinity-update"
        - "runtime.md#rt-rte-deep-maintenance"
        - "memory.md#mem-rte-freshness-recheck"
      note: "Supported yes routes establish trace-fed durable behavior-shaping capacity, not successful learning. Incomplete inventory prevents a complete-value assertion and supplies no system-wide no."
    trace_source:
      assessment: "partial"
      units:
        - 
          scope: "Session-to-wiki compilation and tool-grounded page evidence"
          assessment: "known"
          findings:
            - 
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-warm-save"
                - "runtime.md#rt-rte-auto-update"
                - "memory.md#mem-rte-topic-merge"
                - "memory.md#mem-obj-capture-state"
              note: "Original inputs are recorded user/assistant session turns, including expressed decisions."
            - 
              value: "tool-traces"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-auto-update"
                - "epistemic.md#epi-obj-tool-facts"
                - "epistemic.md#epi-rte-mechanical-check"
              note: "Structured transcript tool requests/results feed grounding cards/corpus and page evidence used in the automatic compilation path; tool request text does not prove success."
          records:
            - "runtime.md#rt-rte-warm-save"
            - "runtime.md#rt-rte-auto-update"
            - "memory.md#mem-rte-topic-merge"
            - "memory.md#mem-obj-capture-state"
            - "epistemic.md#epi-obj-tool-facts"
            - "epistemic.md#epi-rte-mechanical-check"
          note: "Mixed transcript content retains both source classes; no trajectory or environmental-event inference from JSON envelopes."
        - 
          scope: "Usage/feedback-to-selector adaptation"
          assessment: "known"
          findings:
            - 
              value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-feedback-fold"
              note: "Task-local human/model activity and judgments recorded through close-out feed persistent usage metadata."
            - 
              value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-rte-feedback-fold"
                - "epistemic.md#epi-rte-affinity-update"
              note: "Read observations and tool outcomes supply activity evidence to explicit adaptation routes; legacy refresh is not default activation."
          records:
            - "memory.md#mem-rte-feedback-fold"
            - "epistemic.md#epi-rte-affinity-update"
          note: "Original activity content matters, not receipt serialization or adapter labels."
        - 
          scope: "Arbitrary dropped-file inputs and partially inspected observer/maintenance/channel alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-auto-update"
            - "runtime.md#rt-rte-deep-maintenance"
            - "runtime.md#rt-rte-context-delivery"
            - "epistemic.md#epi-rte-affinity-update"
          note: "Records do not fully establish original content of every qualifying update. Static imports do not gain a trace class by entering the queue; observer coverage is partial."
      records:
        - "runtime.md#rt-rte-warm-save"
        - "runtime.md#rt-rte-auto-update"
        - "memory.md#mem-rte-topic-merge"
        - "memory.md#mem-obj-capture-state"
        - "epistemic.md#epi-obj-tool-facts"
        - "epistemic.md#epi-rte-mechanical-check"
        - "memory.md#mem-rte-feedback-fold"
        - "epistemic.md#epi-rte-affinity-update"
        - "runtime.md#rt-rte-deep-maintenance"
        - "runtime.md#rt-rte-context-delivery"
      note: "Session logs and tool activity have local wired witnesses. No accepted record establishes trajectories or event-streams as additional qualifying original inputs; this is not evidenced absence."
---

# llmwiki memory profile

## Comparison rationale

The inventory separates retained knowledge from access structures and from the static policy that writes it. [MEM-OBJ-wiki-pages](memory.md#mem-obj-wiki-pages) is the changed-through-use product; the shipped save skill is not counted as an accumulated instruction store. Provider model components are not evidence that this memory system writes parameters. Session-local term and seen-state still count where later invocations consume them, while current-call grounding cards alone are not an additional durable store.

The accepted reconciliation supersedes the epistemic page, quiz and topic-merge duplicates with [MEM-OBJ-wiki-pages](memory.md#mem-obj-wiki-pages), [MEM-OBJ-quiz-ledger](memory.md#mem-obj-quiz-ledger) and [MEM-RTE-topic-merge](memory.md#mem-rte-topic-merge). These canonical declarations are used for those referents. The narrower [EPI-OBJ-edit-rule](epistemic.md#epi-obj-edit-rule) overlaps, but does not replace, the broader rule/recall extension. Feedback and review containers are not flattened into a pooled consumer or stronger evidence basis.

The same rule string has two consumption paths. [MEM-OBJ-recall-triggers](memory.md#mem-obj-recall-triggers) is symbolic lexical input to ranking, even when imperative delivery is withheld. [MEM-OBJ-wiki-rules](memory.md#mem-obj-wiki-rules) separately supplies natural-language instructions and path targeting. The [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules) can produce a scoped first-edit denial, not proof that a host followed a rule. This distinction supports ranking, instruction and enforcement without equating them.

An operator starting save or enabling commit does not approve every admitted claim. [RT-RTE-warm-save](runtime.md#rt-rte-warm-save), [RT-RTE-auto-update](runtime.md#rt-rte-auto-update) and [MEM-RTE-topic-merge](memory.md#mem-rte-topic-merge) establish routine model/software admission. Human direction answers and [MEM-RTE-query-fileback](memory.md#mem-rte-query-fileback) are separate manual policies. Generic verification APIs do not identify a human decision merely by accepting a caller string.

The profile classifies reduction of retained session content as consolidation and topic replacement as evolution. It does not infer semantic synthesis from the word “synthesis”: [MEM-RTE-topic-merge](memory.md#mem-rte-topic-merge) and the [MEM-RTE-query-fileback](memory.md#mem-rte-query-fileback) do not establish non-entailment of an actual new output claim. The distill check's narrow source/conflict preservation and the merge route's failed-replacement recovery limit remain limits on fidelity, not reasons to suppress supported curation operations. [MEM-RTE-tier-cleanup](memory.md#mem-rte-tier-cleanup) changes availability while preserving bodies; feedback withholding is version-bound.

[RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) and its memory annotation support automatic cold and lexical turn supply. Requested page reads are pull, not a second push inside that delivery. [RT-RTE-edit-rules](runtime.md#rt-rte-edit-rules) supplies an actual target-path match for identifier-based push. Pointer-only delivery is not a demonstrated later page Read, and bounded excerpts omit evidence lines and footnote definitions. The scope therefore does not assume every delivered claim carries retained reasons.

Automatic trace-fed production of durable wiki context qualifies for trace learning even if the content only summarizes prior experience. [MEM-RTE-feedback-fold](memory.md#mem-rte-feedback-fold) independently qualifies through durable selector adaptation. The raw-input learning authority and downstream knowledge/ranking authority are separate consumer paths. Wired trace learning does not assert observed improvement, model-weight updates or exercised self-improvement. Legacy read-scan refresh is explicit, not a default running daemon learner. The profile asserts no local negative because the accepted reports declare no bounded evidenced-absence records establishing one.

Every axis preserves unresolved coverage rather than excluding an inconvenient branch. The accepted [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) names commit and absence channels, but records do not inventory their retained parts or evaluator domains. Initial page/recall provenance, generic caller control, some maintenance transformations and observer inputs impose additional local limits. These gaps prevent a complete memory-value inventory, not the positive wiki, rule, feedback and quiz classifications. No full-history absence claim follows from an absence-channel label.

No source files were read for this profile. All classification warrants come from the supplied accepted records and their annotations; no new evidence or records were introduced.
