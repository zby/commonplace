---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory profile of Labyrinth Exploration across project research state, generated views and later research handoffs."
run-id: "AAS-2026-11-23-labyrinth-exploration-4000731242d4-01"
source-identity: "https://github.com/nasqret/labyrinth-exploration"
reviewed-boundary: "019a93da59313e697dc6f28bcfe1588a376c7565"
memory-comparison:
  version: 2
  scope: "Accumulated project map, result history, evidence, logs, journal, plans, proofs and reports, optional blueprint and document paths, generated status and dashboard artifacts (including test read-back), browser view preference, and the documented host recovery leg. Keep unpinned project producers, remote evidence and the host payload unresolved where they enter these routes. Exclude shipped static prompts/templates as memory, ordinary live context and job state, unrelated persistent client memory, provider weights/serving internals, and package release history."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Canonical project records and optional blueprint"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-review-metadata","memory.md#mem-obj-blueprint-data","memory.md#mem-obj-events","memory.md#mem-obj-frontier","memory.md#mem-obj-scatter","memory.md#mem-obj-frontier-history","memory.md#mem-obj-sota"]
              note: "The loaders and producers use project-local files."
          records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-review-metadata","memory.md#mem-obj-blueprint-data","memory.md#mem-obj-events","memory.md#mem-obj-frontier","memory.md#mem-obj-scatter","memory.md#mem-obj-frontier-history","memory.md#mem-obj-sota"]
          note: "The structured records and module are project files; graph edges do not establish a graph database."
        - scope: "Project notes, journal, saved agent reports and local evidence"
          assessment: "known"
          findings:
            - value: "files"
              basis: "claimed"
              records: ["memory.md#mem-obj-proof-documents","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","memory.md#mem-obj-compute-evidence"]
              note: "The procedure keeps notes, handoff and evidence in project files."
          records: ["memory.md#mem-obj-proof-documents","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","memory.md#mem-obj-compute-evidence"]
          note: "The documented workspace and archive use files."
        - scope: "Build exports and optional document copies"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records: ["memory.md#mem-obj-status-summary","memory.md#mem-obj-dashboard-snapshot","epistemic.md#epi-obj-dashboard-data","epistemic.md#epi-obj-book-status","memory.md#mem-obj-sota-md","memory.md#mem-obj-sota-tex"]
              note: "Build writes HTML, JSON, Markdown and configured document outputs."
          records: ["memory.md#mem-obj-status-summary","memory.md#mem-obj-dashboard-snapshot","epistemic.md#epi-obj-dashboard-data","epistemic.md#epi-obj-book-status","memory.md#mem-obj-sota-md","memory.md#mem-obj-sota-tex"]
          note: "Printed status is delivery; this unit covers retained output files."
        - scope: "Browser tab preference"
          assessment: "known"
          findings:
            - value: "kv"
              basis: "wired"
              records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
              note: "Page code reads and writes the labyrinth-tab key in localStorage."
          records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
          note: "The browser API establishes keyed storage, not its physical implementation."
        - scope: "Host transcript used to recover a missing report"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-research-iteration","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive"]
          note: "The procedure names the transcript, but its storage and retention are not inspected."
        - scope: "Remote computation evidence before project archival"
          assessment: "uninspected"
          findings: []
          records: ["memory.md#mem-obj-compute-evidence"]
          note: "Deployed job output stores and formats are not pinned."
      records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-review-metadata","memory.md#mem-obj-blueprint-data","memory.md#mem-obj-events","memory.md#mem-obj-frontier","memory.md#mem-obj-scatter","memory.md#mem-obj-frontier-history","memory.md#mem-obj-sota","memory.md#mem-obj-proof-documents","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","memory.md#mem-obj-compute-evidence","memory.md#mem-obj-status-summary","memory.md#mem-obj-dashboard-snapshot","epistemic.md#epi-obj-dashboard-data","epistemic.md#epi-obj-book-status","memory.md#mem-obj-sota-md","memory.md#mem-obj-sota-tex","memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab","runtime.md#rt-rte-research-iteration"]
      note: "Project and browser stores are classified; the host recovery leg and remote evidence are not."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Statements, tests, lessons, reasons and event/SOTA prose"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-review-metadata","memory.md#mem-obj-blueprint-data","memory.md#mem-obj-events","memory.md#mem-obj-frontier","memory.md#mem-obj-scatter","memory.md#mem-obj-frontier-history","memory.md#mem-obj-sota"]
              note: "Prose conveys conjectures, reasons and historical accounts to research readers."
          records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-review-metadata","memory.md#mem-obj-blueprint-data","memory.md#mem-obj-events","memory.md#mem-obj-frontier","memory.md#mem-obj-scatter","memory.md#mem-obj-frontier-history","memory.md#mem-obj-sota"]
          note: "Human and model readers interpret the text."
        - scope: "Project keys, edges, labels, module code, values and intervals"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-review-metadata","memory.md#mem-obj-blueprint-data","memory.md#mem-obj-events","memory.md#mem-obj-frontier","memory.md#mem-obj-scatter","memory.md#mem-obj-frontier-history","memory.md#mem-obj-sota"]
              note: "Engine or browser interprets code, IDs, statuses and numerical fields by fixed rules."
          records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-review-metadata","memory.md#mem-obj-blueprint-data","memory.md#mem-obj-events","memory.md#mem-obj-frontier","memory.md#mem-obj-scatter","memory.md#mem-obj-frontier-history","memory.md#mem-obj-sota"]
          note: "Fixed rules consume these localized fields, including explicit numeric data."
        - scope: "Saved report, project handoff and proof prose"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records: ["memory.md#mem-obj-proof-documents","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","memory.md#mem-obj-compute-evidence"]
              note: "Readers interpret findings, proofs, verdict reasons and plans."
          records: ["memory.md#mem-obj-proof-documents","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","memory.md#mem-obj-compute-evidence"]
          note: "Interpretation of the content is distinct from following a locator."
        - scope: "Proof labels, recovery IDs, code, manifests and data"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "claimed"
              records: ["memory.md#mem-obj-proof-documents","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","memory.md#mem-obj-compute-evidence"]
              note: "Document and recovery procedures use labels and IDs; code/data and manifests have explicit structure."
          records: ["memory.md#mem-obj-proof-documents","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","memory.md#mem-obj-compute-evidence"]
          note: "The structured parts are separately addressable and are not embeddings."
        - scope: "Projection text for research and document readers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "afforded"
              records: ["memory.md#mem-obj-status-summary","memory.md#mem-obj-dashboard-snapshot","epistemic.md#epi-obj-dashboard-data","epistemic.md#epi-obj-book-status","memory.md#mem-obj-sota-md","memory.md#mem-obj-sota-tex"]
              note: "Rendered or exported text conveys selected existing statements."
          records: ["memory.md#mem-obj-status-summary","memory.md#mem-obj-dashboard-snapshot","epistemic.md#epi-obj-dashboard-data","epistemic.md#epi-obj-book-status","memory.md#mem-obj-sota-md","memory.md#mem-obj-sota-tex"]
          note: "Formatting does not turn result or status prose into a policy rule."
        - scope: "Projection counts, links, dates, grouping and reference commands"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-status-summary","memory.md#mem-obj-dashboard-snapshot","epistemic.md#epi-obj-dashboard-data","epistemic.md#epi-obj-book-status","memory.md#mem-obj-sota-md","memory.md#mem-obj-sota-tex"]
              note: "Rendering, tests and formatters consume explicit fields or generate structured references."
          records: ["memory.md#mem-obj-status-summary","memory.md#mem-obj-dashboard-snapshot","epistemic.md#epi-obj-dashboard-data","epistemic.md#epi-obj-book-status","memory.md#mem-obj-sota-md","memory.md#mem-obj-sota-tex"]
          note: "The fixed consumers interpret localized fields or commands."
        - scope: "Browser tab key and value"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
              note: "An allowed tab ID selects a panel."
          records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
          note: "The value is interpreted by the tab selector."
        - scope: "Host transcript and remote evidence payloads"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-research-iteration","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","memory.md#mem-obj-compute-evidence"]
          note: "Neither the saved final message nor the local archive fixes the encoding of the unseen source payload."
      records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-review-metadata","memory.md#mem-obj-blueprint-data","memory.md#mem-obj-events","memory.md#mem-obj-frontier","memory.md#mem-obj-scatter","memory.md#mem-obj-frontier-history","memory.md#mem-obj-sota","memory.md#mem-obj-proof-documents","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","memory.md#mem-obj-compute-evidence","memory.md#mem-obj-status-summary","memory.md#mem-obj-dashboard-snapshot","epistemic.md#epi-obj-dashboard-data","epistemic.md#epi-obj-book-status","memory.md#mem-obj-sota-md","memory.md#mem-obj-sota-tex","memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab","runtime.md#rt-rte-research-iteration"]
      note: "Classify the locally inspectable parts and consumption paths without generalizing to remote or recovered payloads."
    lineage:
      assessment: "partial"
      units:
        - scope: "Project-authored proof text, plan and conjecture formulations"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "claimed"
              records: ["memory.md#mem-obj-proof-documents","memory.md#mem-obj-project-handoff","epistemic.md#epi-rte-predict-test"]
              note: "Coordinators and project authors formulate proofs, questions and plans."
          records: ["memory.md#mem-obj-proof-documents","memory.md#mem-obj-project-handoff","epistemic.md#epi-rte-predict-test"]
          note: "Authorship here does not identify the admission principal."
        - scope: "Source/family statements and external evidence"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "claimed"
              records: ["epistemic.md#epi-obj-source-family","epistemic.md#epi-rte-source-retain","memory.md#mem-obj-compute-evidence"]
              note: "Outside results and papers enter the project as selected material."
          records: ["epistemic.md#epi-obj-source-family","epistemic.md#epi-rte-source-retain","memory.md#mem-obj-compute-evidence"]
          note: "Acquisition does not establish source checking."
        - scope: "Blueprint statements entering the merged graph"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records: ["epistemic.md#epi-rte-blueprint-label"]
              note: "Loader takes statements from the optional project module."
          records: ["epistemic.md#epi-rte-blueprint-label","memory.md#mem-obj-blueprint-data"]
          note: "Import at the consumer is known even though the source module’s own provenance is not."
        - scope: "Research logs, selected returned reports and counterexample lessons"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "claimed"
              records: ["memory.md#mem-obj-events","memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-refutation-record"]
              note: "Narrated outcomes, copied final returns and lessons from failures preserve selected experience."
          records: ["memory.md#mem-obj-events","memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-refutation-record"]
          note: "These retain or derive from work, rather than carrying a whole transcript."
        - scope: "Recent-event excerpt and timeline payload"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records: ["memory.md#mem-obj-events","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-snapshot-write"]
              note: "The engine selects an event tail and embeds parsed event objects for later display."
          records: ["memory.md#mem-obj-events","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-snapshot-write"]
          note: "Trace-derived pieces of mixed exports are separate from structural aggregates."
        - scope: "Example results, derived metrics and table/document copies"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records: ["runtime.md#rt-rte-example-update","epistemic.md#epi-rte-example-compute","epistemic.md#epi-rte-example-write","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-frontier-project","epistemic.md#epi-rte-dashboard-json","epistemic.md#epi-rte-snapshot-write","epistemic.md#epi-rte-table-project","epistemic.md#epi-rte-book-status"]
              note: "Code computes counts/projections or formats existing results into the corresponding files."
          records: ["runtime.md#rt-rte-example-update","epistemic.md#epi-rte-example-compute","epistemic.md#epi-rte-example-write","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-frontier-project","epistemic.md#epi-rte-dashboard-json","epistemic.md#epi-rte-snapshot-write","epistemic.md#epi-rte-table-project","epistemic.md#epi-rte-book-status"]
          note: "Derived from computations or existing project inputs; not a new scientific warrant."
        - scope: "Example fixed answer text, milestone and review tags"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records: ["runtime.md#rt-rte-example-update","epistemic.md#epi-rte-example-compute","epistemic.md#epi-rte-example-write"]
              note: "The script inserts preset content."
          records: ["runtime.md#rt-rte-example-update","epistemic.md#epi-rte-example-compute","epistemic.md#epi-rte-example-write"]
          note: "These parts do not come from the verdict or from analyzing the stored conjecture."
        - scope: "Tab preference"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
              note: "A click supplies the reader’s tab choice."
            - value: "other-compiled"
              basis: "wired"
              records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
              note: "Startup resolves the route, prior preference or default and saves the selected ID."
          records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
          note: "Selection supplies the stored value, directly on click or through startup resolution."
        - scope: "Private seed contents, blueprint source and overrides, project evidence and review provenance"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-review-metadata","memory.md#mem-obj-blueprint-data","memory.md#mem-obj-events","memory.md#mem-obj-frontier","memory.md#mem-obj-scatter","memory.md#mem-obj-frontier-history","memory.md#mem-obj-sota","memory.md#mem-obj-proof-documents","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","memory.md#mem-obj-compute-evidence"]
          note: "The records name the surfaces but cannot establish their actual initial authors, derivation or provenance."
        - scope: "Project-specific extractor outputs and host recovery provenance"
          assessment: "uninspected"
          findings: []
          records: ["memory.md#mem-rte-extract-writeups","runtime.md#rt-rte-research-iteration","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive"]
          note: "No pinned extractor implementation, actual document chain or host retention payload fixes the lineage of those alternatives."
      records: ["memory.md#mem-obj-proof-documents","memory.md#mem-obj-project-handoff","epistemic.md#epi-rte-predict-test","epistemic.md#epi-obj-source-family","epistemic.md#epi-rte-source-retain","memory.md#mem-obj-compute-evidence","epistemic.md#epi-rte-blueprint-label","memory.md#mem-obj-blueprint-data","memory.md#mem-obj-events","memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-refutation-record","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-snapshot-write","runtime.md#rt-rte-example-update","epistemic.md#epi-rte-example-compute","epistemic.md#epi-rte-example-write","epistemic.md#epi-rte-frontier-project","epistemic.md#epi-rte-dashboard-json","epistemic.md#epi-rte-table-project","epistemic.md#epi-rte-book-status","memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab","memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-review-metadata","memory.md#mem-obj-frontier","memory.md#mem-obj-scatter","memory.md#mem-obj-frontier-history","memory.md#mem-obj-sota","memory.md#mem-rte-extract-writeups","runtime.md#rt-rte-research-iteration"]
      note: "Authored, imported, computed and trace-derived parts coexist. Initial state and project-specific producers remain unresolved."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Project statements, reports, sources and proofs at research readers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "claimed"
              records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-agent-archive","memory.md#mem-obj-proof-documents","epistemic.md#epi-rte-source-rely"]
              note: "Coordinator and workers use these as claims, evidence or leads."
          records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-agent-archive","memory.md#mem-obj-proof-documents","epistemic.md#epi-rte-source-rely"]
          note: "The reader can use scoped evidence; unchecked material stays advisory."
        - scope: "Retained plan and lessons in coordinator and worker guidance"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "claimed"
              records: ["memory.md#mem-obj-project-handoff","epistemic.md#epi-rte-refutation-record","runtime.md#rt-bap-brief-worker"]
              note: "A later coordinator follows the saved plan and a brief supplies selected directions or cautions."
          records: ["memory.md#mem-obj-project-handoff","epistemic.md#epi-rte-refutation-record","runtime.md#rt-bap-brief-worker"]
          note: "Only the portions prescribing the next step or directing the assignment have instruction force."
        - scope: "Retained frontier gaps and named questions at coordinator selection"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "claimed"
              records: ["epistemic.md#epi-rte-resume-select"]
              note: "Expected impact of work on retained questions affects which get priority."
            - value: "routing"
              basis: "claimed"
              records: ["epistemic.md#epi-rte-resume-select","runtime.md#rt-rte-research-iteration"]
              note: "The selected gap directs which task or escalation to pursue."
          records: ["epistemic.md#epi-rte-resume-select","runtime.md#rt-rte-research-iteration"]
          note: "Priority is a coordinator judgment, not a learned ranker."
        - scope: "Journal recovery fields used by coordinator"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "claimed"
              records: ["runtime.md#rt-rte-research-iteration","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive"]
              note: "Thread and directory references direct follow-up and report recovery."
          records: ["runtime.md#rt-rte-research-iteration","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive"]
          note: "Recorded IDs select where to check; they do not validate liveness."
        - scope: "Referee results and tier/review fields at their policy consumers"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "claimed"
              records: ["epistemic.md#epi-rte-verdict-dispose","epistemic.md#epi-rte-writer-check"]
              note: "Coordinator checks a candidate or edit against retained verdict and corrections."
            - value: "enforcement"
              basis: "claimed"
              records: ["epistemic.md#epi-rte-verdict-dispose","epistemic.md#epi-rte-tier-citation"]
              note: "The policy withholds established use or unqualified citation when verdict, scope or tier does not allow it."
          records: ["epistemic.md#epi-rte-verdict-dispose","epistemic.md#epi-rte-tier-citation","epistemic.md#epi-rte-writer-check"]
          note: "Validation of a proposed use and withholding permission are procedural, not engine guarantees."
        - scope: "Reference IDs and frontier bounds at check"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records: ["epistemic.md#epi-rte-schema-check","epistemic.md#epi-rte-conflict-check"]
              note: "Stored node identities and grid fields provide criteria for reference and overlap diagnostics."
          records: ["epistemic.md#epi-rte-schema-check","epistemic.md#epi-rte-conflict-check"]
          note: "The result is limited to declared predicates on the invoked snapshot."
        - scope: "Existing exhaustive marker at the tutorial writer"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "wired"
              records: ["epistemic.md#epi-rte-example-write"]
              note: "Stored target ID and exhaustive kind veto the write on rerun."
          records: ["epistemic.md#epi-rte-example-write"]
          note: "Only this guarded script path is covered."
        - scope: "Blueprint overlays, dashboard categories and browser preference"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records: ["epistemic.md#epi-rte-blueprint-label","epistemic.md#epi-rte-browser-select","memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
              note: "Matched overrides set which fields apply; category fields and the saved ID select views or parts for rendering."
          records: ["epistemic.md#epi-rte-blueprint-label","epistemic.md#epi-rte-browser-select","memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
          note: "These selectors affect merge or display, not scientific acceptance."
        - scope: "Competing frontier labels in the projection"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records: ["epistemic.md#epi-rte-frontier-project"]
              note: "Retained categories have relative priority for a contested value."
          records: ["epistemic.md#epi-rte-frontier-project"]
          note: "Priority is fixed code applied to retained claims."
        - scope: "Research projections at downstream readers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records: ["epistemic.md#epi-rte-status-project","memory.md#mem-rte-snapshot-browse"]
              note: "Status and rendered snapshot present evidence summaries and research context."
            - value: "knowledge"
              basis: "afforded"
              records: ["memory.md#mem-obj-sota-tex","memory.md#mem-obj-sota-md","epistemic.md#epi-obj-book-status"]
              note: "Configured document copies can supply current results or progress to readers."
          records: ["epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-frontier-project","epistemic.md#epi-rte-dashboard-json","epistemic.md#epi-rte-snapshot-write","memory.md#mem-rte-snapshot-browse","memory.md#mem-obj-sota-tex","memory.md#mem-obj-sota-md","epistemic.md#epi-obj-book-status"]
          note: "Status and browser expose selected context; optional document consumers are not pinned."
        - scope: "Standalone export at example assertions"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records: ["epistemic.md#epi-rte-json-assertions"]
              note: "Selected persisted fields supply evidence to the test; the expected constants, not the file under test, set the criteria."
          records: ["epistemic.md#epi-rte-json-assertions"]
          note: "This is a software test consumer, not research admission."
        - scope: "Research-event summaries at automatic projection"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records: ["memory.md#mem-obj-events","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-snapshot-write"]
              note: "Build turns retained activity into context files available to later readers."
          records: ["memory.md#mem-obj-events","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-snapshot-write"]
          note: "Trace input has a different force from its downstream projection."
        - scope: "Prior result reports and counterexamples at the lesson/update decision"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "claimed"
              records: ["memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-refutation-record","runtime.md#rt-rte-review-integration"]
              note: "Counterexamples and criticism shape retained corrections and lessons for later work."
          records: ["memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-refutation-record","runtime.md#rt-rte-review-integration"]
          note: "This is the instructed update from experience, not proven improvement."
        - scope: "Host transcript and remote/project-specific consumers"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-research-iteration","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","memory.md#mem-obj-compute-evidence","memory.md#mem-rte-extract-writeups"]
          note: "Fallback and project workflows are documented, but exact delivered payloads, independent consumers and effects are not pinned."
      records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-agent-archive","memory.md#mem-obj-proof-documents","epistemic.md#epi-rte-source-rely","memory.md#mem-obj-project-handoff","epistemic.md#epi-rte-refutation-record","runtime.md#rt-bap-brief-worker","epistemic.md#epi-rte-resume-select","runtime.md#rt-rte-research-iteration","epistemic.md#epi-rte-verdict-dispose","epistemic.md#epi-rte-tier-citation","epistemic.md#epi-rte-writer-check","epistemic.md#epi-rte-schema-check","epistemic.md#epi-rte-conflict-check","epistemic.md#epi-rte-example-write","epistemic.md#epi-rte-blueprint-label","epistemic.md#epi-rte-browser-select","memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab","epistemic.md#epi-rte-frontier-project","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-dashboard-json","epistemic.md#epi-rte-snapshot-write","memory.md#mem-rte-snapshot-browse","memory.md#mem-obj-sota-tex","memory.md#mem-obj-sota-md","epistemic.md#epi-obj-book-status","epistemic.md#epi-rte-json-assertions","memory.md#mem-obj-events","runtime.md#rt-rte-review-integration","memory.md#mem-obj-compute-evidence","memory.md#mem-rte-extract-writeups"]
      note: "Research advice, procedural force and deterministic selection are distinct. Delivery or a label alone does not establish compliance or scientific approval."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Shipped compute writers"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records: ["runtime.md#rt-rte-example-update","epistemic.md#epi-rte-example-compute","epistemic.md#epi-rte-example-write"]
              note: "Code chooses which computed values and preset fields are persisted."
          records: ["runtime.md#rt-rte-example-update","epistemic.md#epi-rte-example-compute","epistemic.md#epi-rte-example-write"]
          note: "Caller launch or persistence flag is not content approval."
        - scope: "Build writes and configured export refresh"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records: ["epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-frontier-project","epistemic.md#epi-rte-dashboard-json","epistemic.md#epi-rte-snapshot-write","epistemic.md#epi-rte-sota-md","epistemic.md#epi-rte-sota-tex","epistemic.md#epi-rte-book-status"]
              note: "Formatters select and write each enabled projection."
          records: ["epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-frontier-project","epistemic.md#epi-rte-dashboard-json","epistemic.md#epi-rte-snapshot-write","epistemic.md#epi-rte-sota-md","epistemic.md#epi-rte-sota-tex","epistemic.md#epi-rte-book-status"]
          note: "The build request initiates writes without deciding each retained row."
        - scope: "Content decision for an individual CLI event"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-event-append","memory.md#mem-obj-events"]
          note: "The caller supplies the summary and references. The type whitelist and timestamped append are wired, but the records do not establish whether a human or a model decided to supply that content."
        - scope: "Coordinator-controlled campaign updates and archive/handoff writes"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records: ["runtime.md#rt-rte-review-integration","epistemic.md#epi-rte-canonical-integrate","epistemic.md#epi-rte-refutation-record","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-source-retain"]
              note: "Coordinator selects reports, entries, corrections and next-step records for persistence."
          records: ["runtime.md#rt-rte-review-integration","epistemic.md#epi-rte-canonical-integrate","epistemic.md#epi-rte-refutation-record","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-source-retain"]
          note: "The prescribed model branch does not require per-content operator confirmation; co-author evidence is not a transfer of write control."
        - scope: "Tab click and startup writes"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "wired"
              records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
              note: "Reader click explicitly supplies the tab preference."
            - value: "automatic"
              basis: "wired"
              records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
              note: "Startup can save the selected fallback/default without a click."
          records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
          note: "The explicit choice and the startup fallback are different admissions."
        - scope: "Initial seeds/backfill, direct edits and blueprint/override producers"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-events","memory.md#mem-obj-blueprint-data","memory.md#mem-obj-project-handoff"]
          note: "The source and effective content-admission principal vary by project or caller; copying and physical file writes do not resolve them."
        - scope: "Project extraction, remote archive and host-side retention"
          assessment: "uninspected"
          findings: []
          records: ["memory.md#mem-rte-extract-writeups","memory.md#mem-obj-compute-evidence","runtime.md#rt-rte-research-iteration","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive"]
          note: "There is no pinned deployment to identify which project- or host-side admissions are operator-controlled."
      records: ["runtime.md#rt-rte-example-update","epistemic.md#epi-rte-example-compute","epistemic.md#epi-rte-example-write","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-frontier-project","epistemic.md#epi-rte-dashboard-json","epistemic.md#epi-rte-snapshot-write","epistemic.md#epi-rte-sota-md","epistemic.md#epi-rte-sota-tex","epistemic.md#epi-rte-book-status","runtime.md#rt-rte-event-append","memory.md#mem-obj-events","runtime.md#rt-rte-review-integration","epistemic.md#epi-rte-canonical-integrate","epistemic.md#epi-rte-refutation-record","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-source-retain","memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab","memory.md#mem-obj-knowledge-nodes","memory.md#mem-obj-blueprint-data","memory.md#mem-rte-extract-writeups","memory.md#mem-obj-compute-evidence","runtime.md#rt-rte-research-iteration"]
      note: "Automatic writes in build and the example and prescribed model admission do not resolve the CLI event caller’s content decision, initial seeding, direct writes or project/host recovery control."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Status tail, frontier runs/bins and selective table projections"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records: ["epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-frontier-project","epistemic.md#epi-rte-sota-md","epistemic.md#epi-rte-sota-tex"]
              note: "The projections select fields, reduce event history or compress frontier reasons; table exports keep only selected columns/groups."
          records: ["epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-frontier-project","epistemic.md#epi-rte-sota-md","epistemic.md#epi-rte-sota-tex"]
          note: "This is reduced presentation of retained inputs, not conjecture generation or withdrawal from the canonical store."
        - scope: "Guarded example record replacement"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records: ["epistemic.md#epi-rte-example-write","memory.md#mem-obj-sota"]
              note: "The script revises stored door, frontier and best-result state."
          records: ["epistemic.md#epi-rte-example-write","memory.md#mem-obj-sota"]
          note: "The previous result text remains without full rollback."
        - scope: "Coordinator revision, refutation and revised conjecture"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "claimed"
              records: ["runtime.md#rt-rte-review-integration","epistemic.md#epi-rte-canonical-integrate","epistemic.md#epi-rte-refutation-record"]
              note: "Apply supported corrections to the current notes and map."
            - value: "invalidate"
              basis: "claimed"
              records: ["epistemic.md#epi-rte-refutation-record"]
              note: "Keep refuting history while withdrawing reliance on the failed statement."
            - value: "synthesize"
              basis: "claimed"
              records: ["epistemic.md#epi-rte-predict-test","runtime.md#rt-rte-review-integration"]
              note: "Form a next-size prediction not entailed by prior values and frame it for testing."
          records: ["runtime.md#rt-rte-review-integration","epistemic.md#epi-rte-canonical-integrate","epistemic.md#epi-rte-refutation-record","epistemic.md#epi-rte-predict-test"]
          note: "Prescribed acts are not deterministic transformations or observed executions."
        - scope: "Condensed briefing write-ups and failure lessons"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records: ["memory.md#mem-rte-extract-writeups","epistemic.md#epi-rte-refutation-record"]
              note: "Select an anchored proof subset or retain a concise lesson from a failed route."
          records: ["memory.md#mem-rte-extract-writeups","epistemic.md#epi-rte-refutation-record"]
          note: "The procedure calls for reduced, reusable context; actual extractor behavior is a separate unknown."
        - scope: "Project-specific extraction and host compaction alternatives"
          assessment: "uninspected"
          findings: []
          records: ["memory.md#mem-rte-extract-writeups","runtime.md#rt-rte-research-iteration","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive"]
          note: "No executable project extractor or host compaction payload is pinned. Neither an index rebuild nor malformed-line skipping establishes deduplication, decay or history withdrawal."
      records: ["epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-frontier-project","epistemic.md#epi-rte-sota-md","epistemic.md#epi-rte-sota-tex","epistemic.md#epi-rte-example-write","memory.md#mem-obj-sota","runtime.md#rt-rte-review-integration","epistemic.md#epi-rte-canonical-integrate","epistemic.md#epi-rte-refutation-record","epistemic.md#epi-rte-predict-test","memory.md#mem-rte-extract-writeups","runtime.md#rt-rte-research-iteration","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive"]
      note: "The projections reduce existing material and the example replaces entries. Procedural transformations and private tooling do not establish a complete implemented inventory."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "CLI loads and guarded example rerun"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records: ["runtime.md#rt-rte-build-views","epistemic.md#epi-rte-event-reload","runtime.md#rt-rte-blueprint-import","epistemic.md#epi-rte-example-write"]
              note: "The engine and writer read project inputs on an explicit operation."
          records: ["runtime.md#rt-rte-build-views","epistemic.md#epi-rte-event-reload","runtime.md#rt-rte-blueprint-import","epistemic.md#epi-rte-example-write"]
          note: "Each invoked operation asks for its retained inputs; a resulting print/write is not a second read-back."
        - scope: "Coordinator restart and worker opens of referenced documents"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "claimed"
              records: ["runtime.md#rt-rte-research-iteration","runtime.md#rt-bap-brief-worker","memory.md#mem-rte-extract-writeups","epistemic.md#epi-rte-resume-select"]
              note: "Coordinator opens project status/map and workers open named sections or evidence."
          records: ["runtime.md#rt-rte-research-iteration","runtime.md#rt-bap-brief-worker","memory.md#mem-rte-extract-writeups","epistemic.md#epi-rte-resume-select"]
          note: "Prescribed file and document opens are requests rather than automatic context restoration."
        - scope: "Selected existing project material delivered in campaign briefs"
          assessment: "known"
          findings:
            - value: "push"
              basis: "claimed"
              records: ["runtime.md#rt-bap-brief-worker","memory.md#mem-rte-extract-writeups","epistemic.md#epi-rte-resume-select","workflow.md#wf-rte-writer-draft"]
              note: "Model coordinator supplies selected prior results, counterexamples, lessons and correction material on task dispatch."
          records: ["runtime.md#rt-bap-brief-worker","memory.md#mem-rte-extract-writeups","epistemic.md#epi-rte-resume-select","workflow.md#wf-rte-writer-draft"]
          note: "Separate the coordinator’s unsolicited selection for the worker from that worker’s later file requests."
        - scope: "Dashboard open and requested detail"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records: ["memory.md#mem-rte-snapshot-browse","epistemic.md#epi-rte-browser-select"]
              note: "The page uses the built payload rather than retrieving the sibling JSON or canonical files."
          records: ["memory.md#mem-rte-snapshot-browse","epistemic.md#epi-rte-browser-select"]
          note: "Opening the retained HTML and requesting a node or view are pulls."
        - scope: "Board and table population at page initialization"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records: ["memory.md#mem-rte-snapshot-browse","epistemic.md#epi-rte-browser-select"]
              note: "Page initialization supplies selected board and table content without individual row requests."
          records: ["memory.md#mem-rte-snapshot-browse","epistemic.md#epi-rte-browser-select"]
          note: "Population from the embedded payload is independent of which panel the preference makes visible."
        - scope: "Fixed-key tab preference read at page initialization"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
              note: "The startup handler requests the single stored preference when it has no valid route choice."
          records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab","epistemic.md#epi-rte-browser-select"]
          note: "Matching the returned value to a visible panel does not deliver another retained payload."
        - scope: "Standalone export in tests"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records: ["epistemic.md#epi-rte-json-assertions"]
              note: "Example tests reopen the JSON and read designated fields."
          records: ["epistemic.md#epi-obj-dashboard-data","epistemic.md#epi-rte-json-assertions"]
          note: "The explicit decode is a separate consumer from the browser."
        - scope: "Optional document exports"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records: ["memory.md#mem-obj-sota-md","memory.md#mem-obj-sota-tex","epistemic.md#epi-obj-book-status"]
              note: "A notes compiler or reader can ask for the generated artifact."
          records: ["memory.md#mem-obj-sota-md","memory.md#mem-obj-sota-tex","epistemic.md#epi-obj-book-status"]
          note: "An explicit include/open is afforded; no configured inclusion is established."
        - scope: "Coordinator request to recover a missing final message"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "claimed"
              records: ["runtime.md#rt-rte-research-iteration","memory.md#mem-obj-agent-archive"]
              note: "After a missing completion notice, the coordinator is instructed to consult the transcript for the worker’s final report."
          records: ["runtime.md#rt-rte-research-iteration","memory.md#mem-obj-agent-archive"]
          note: "Only the coordinator’s request is classified; host-side selection and additional delivery remain uninspected."
        - scope: "Host-side transcript selection and follow-up, private document readers and research use of standalone JSON"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-research-iteration","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","epistemic.md#epi-obj-dashboard-data","memory.md#mem-obj-sota-md","memory.md#mem-obj-sota-tex","epistemic.md#epi-obj-book-status"]
          note: "Records do not establish what the host selects or delivers beyond the requested report, or what project-specific continuations actually read."
      records: ["runtime.md#rt-rte-build-views","epistemic.md#epi-rte-event-reload","runtime.md#rt-rte-blueprint-import","epistemic.md#epi-rte-example-write","runtime.md#rt-rte-research-iteration","runtime.md#rt-bap-brief-worker","memory.md#mem-rte-extract-writeups","epistemic.md#epi-rte-resume-select","workflow.md#wf-rte-writer-draft","memory.md#mem-rte-snapshot-browse","epistemic.md#epi-rte-browser-select","memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab","epistemic.md#epi-obj-dashboard-data","epistemic.md#epi-rte-json-assertions","memory.md#mem-obj-sota-md","memory.md#mem-obj-sota-tex","epistemic.md#epi-obj-book-status","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive"]
      note: "Requested reads and independently selected delivery coexist. Host recovery and project-specific routes are not fully classified."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Fixed-key tab preference read at page initialization"
          assessment: "inapplicable"
          findings: []
          records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab","epistemic.md#epi-rte-browser-select"]
          note: "Startup requests one preference from a fixed key. The saved ID changes panel visibility, not which retained parts are delivered. Board and table population has its own selector."
        - scope: "Board and table rows at page initialization"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records: ["epistemic.md#epi-rte-browser-select"]
              note: "Page load filters embedded nodes by kind/status and groups SOTA rows for display."
          records: ["epistemic.md#epi-rte-browser-select"]
          note: "The fixed predicates select content before any individual row request."
        - scope: "Campaign context chosen at attack/referee/writer dispatch"
          assessment: "known"
          findings:
            - value: "inferred-judgment"
              basis: "claimed"
              records: ["runtime.md#rt-bap-brief-worker","memory.md#mem-rte-extract-writeups","epistemic.md#epi-rte-resume-select","workflow.md#wf-rte-writer-draft"]
              note: "At dispatch the coordinator judges relevance to the selected question or concerns, and includes selected proofs, failed routes, findings or corrections."
          records: ["runtime.md#rt-bap-brief-worker","memory.md#mem-rte-extract-writeups","epistemic.md#epi-rte-resume-select","workflow.md#wf-rte-writer-draft"]
          note: "Named labels/paths can support later retrieval, but pointers alone do not establish automatic identity-match selection."
        - scope: "Host fallback, project-specific context delivery and unpinned inclusion routes"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-research-iteration","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","memory.md#mem-rte-extract-writeups","epistemic.md#epi-obj-dashboard-data"]
          note: "Unknown delivery direction and selector inputs prevent classifying any additional push signal."
      records: ["memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab","epistemic.md#epi-rte-browser-select","runtime.md#rt-bap-brief-worker","memory.md#mem-rte-extract-writeups","epistemic.md#epi-rte-resume-select","workflow.md#wf-rte-writer-draft","runtime.md#rt-rte-research-iteration","memory.md#mem-obj-project-handoff","memory.md#mem-obj-agent-archive","epistemic.md#epi-obj-dashboard-data"]
      note: "The signal classifies what is selected without a request for that retained part, not every identifier or predicate found on a pull."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Event tail in retained status and snapshot timeline"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records: ["memory.md#mem-obj-events","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-snapshot-write","memory.md#mem-rte-snapshot-browse","runtime.md#rt-rte-research-iteration"]
              note: "Stored project events feed automatic retained status/dashboard output, which later readers use as research context."
          records: ["memory.md#mem-obj-events","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-snapshot-write","memory.md#mem-rte-snapshot-browse","runtime.md#rt-rte-research-iteration"]
          note: "The build writes research activity into context for later sessions/readers, unlike merely appending raw trace."
        - scope: "Coordinator-authored revisions and lessons from checked experience"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records: ["memory.md#mem-obj-compute-evidence","memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-refutation-record","runtime.md#rt-rte-review-integration","runtime.md#rt-bap-brief-worker"]
              note: "Under the protocol the coordinator uses failed computations, evidence and referee corrections to change the durable map/lesson read by future workers."
          records: ["memory.md#mem-obj-compute-evidence","memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-refutation-record","runtime.md#rt-rte-review-integration","runtime.md#rt-bap-brief-worker"]
          note: "This is the model-coordinator path prescribed by the skill, not an engine inference from labels or evidence of its activation."
        - scope: "Append and report capture, example enumeration and preference writes"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-event-append","memory.md#mem-obj-agent-archive","runtime.md#rt-rte-example-update","epistemic.md#epi-rte-example-compute","epistemic.md#epi-rte-example-write","memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
          note: "Raw capture by itself, current enumeration supplying explicit results, and preference restoration do not warrant another qualifying trace-fed update; no accepted absence record covers these paths."
        - scope: "Host recovery or compaction, private project updates and document extractors"
          assessment: "uninspected"
          findings: []
          records: ["memory.md#mem-obj-project-handoff","memory.md#mem-rte-extract-writeups","runtime.md#rt-rte-research-iteration","memory.md#mem-obj-agent-archive"]
          note: "No exact transformation and later input chain is pinned for those alternatives."
      records: ["memory.md#mem-obj-events","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-snapshot-write","memory.md#mem-rte-snapshot-browse","runtime.md#rt-rte-research-iteration","memory.md#mem-obj-compute-evidence","memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-refutation-record","runtime.md#rt-rte-review-integration","runtime.md#rt-bap-brief-worker","runtime.md#rt-rte-event-append","runtime.md#rt-rte-example-update","epistemic.md#epi-rte-example-compute","epistemic.md#epi-rte-example-write","memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab","memory.md#mem-obj-project-handoff","memory.md#mem-rte-extract-writeups"]
      note: "Wired trace-fed projection and a claimed coordinator update establish local positives, not evidence that later research improved."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Event input to status/dashboard projection"
          assessment: "known"
          findings:
            - value: "event-streams"
              basis: "wired"
              records: ["memory.md#mem-obj-events","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-snapshot-write","memory.md#mem-rte-snapshot-browse","runtime.md#rt-rte-research-iteration"]
              note: "The generator reads discrete recorded research events as original inputs to the recent-history projection."
          records: ["memory.md#mem-obj-events","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-snapshot-write","memory.md#mem-rte-snapshot-browse","runtime.md#rt-rte-research-iteration"]
          note: "Narrated project activity is not a conversation transcript."
        - scope: "Evidence input to coordinator’s durable corrections and failure lessons"
          assessment: "partial"
          findings:
            - value: "tool-traces"
              basis: "claimed"
              records: ["memory.md#mem-obj-compute-evidence","memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-refutation-record","runtime.md#rt-rte-review-integration","runtime.md#rt-bap-brief-worker"]
              note: "Saved computation outputs and counterexamples produced by research tools can feed retained corrections and lessons."
          records: ["memory.md#mem-obj-compute-evidence","memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-refutation-record","runtime.md#rt-rte-review-integration","runtime.md#rt-bap-brief-worker"]
          note: "Recorded computation evidence is one prescribed input; the exact source mix and any additional session/trajectory origin are not supplied."
        - scope: "Other candidate trace inputs at the write boundary"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-event-append","memory.md#mem-obj-agent-archive","runtime.md#rt-rte-example-update","epistemic.md#epi-rte-example-compute","epistemic.md#epi-rte-example-write","memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab"]
          note: "A raw event, a final agent message, a computed set, or a click does not by itself establish an additional qualifying write and source type."
        - scope: "Original input to opaque host/project continuation updates"
          assessment: "uninspected"
          findings: []
          records: ["memory.md#mem-obj-project-handoff","memory.md#mem-rte-extract-writeups","runtime.md#rt-rte-research-iteration","memory.md#mem-obj-agent-archive"]
          note: "A recovered report or a display excerpt does not identify which source material any opaque update consumes."
      records: ["memory.md#mem-obj-events","epistemic.md#epi-rte-status-project","epistemic.md#epi-rte-snapshot-write","memory.md#mem-rte-snapshot-browse","runtime.md#rt-rte-research-iteration","memory.md#mem-obj-compute-evidence","memory.md#mem-obj-agent-archive","epistemic.md#epi-rte-refutation-record","runtime.md#rt-rte-review-integration","runtime.md#rt-bap-brief-worker","runtime.md#rt-rte-event-append","runtime.md#rt-rte-example-update","epistemic.md#epi-rte-example-compute","epistemic.md#epi-rte-example-write","memory.md#mem-obj-labyrinth-tab","memory.md#mem-rte-restore-tab","memory.md#mem-obj-project-handoff","memory.md#mem-rte-extract-writeups"]
      note: "Activity records and computation evidence can feed different qualifying writes. Their source types do not classify undisclosed payloads."
---

# Labyrinth Exploration memory profile

## Comparison rationale

The retained map is file-backed; a graph layout does not make it a graph
database. The browser has a separate keyed preference with authority over
a panel, not over research. Restoring that preference does not target
retained content by ID: the board and table populate independently from
the embedded payload. Status and the dashboard are selective
projections, not proof or acceptance. The embedded snapshot reaches the
browser; the standalone export reaches [EPI-RTE-json-assertions](epistemic.md#epi-rte-json-assertions).
An optional table or book copy is another retained destination, not another
canonical input. The installed method and the user's task authorization
are not retained research content.

The append counts once under [RT-RTE-event-append](runtime.md#rt-rte-event-append),
not under the superseded EPI-RTE-event-keep. The event, frontier, source
table, status and two table-export object supersessions make the memory
records canonical for those objects. They do not absorb the read and
projection routes, separate scatter data, configured book status or
standalone dashboard JSON. The status tail is classified as a reduction
in file order, not as a chronological transcript or a new claim. The
append’s type check governs whether the supplied input can be written;
it does not identify who decided to supply each event’s content.

A trace-fed status build qualifies on the path from project events through
a retained summary to later context, not from storing raw logs alone.
The prescribed failure-lesson update is separate and has only a doctrine
basis. Neither qualifies a claim about improved capacity. No accepted
evidenced-absence record justifies a local trace-learning negative.
Private project producers, remote evidence and host recovery do not have
pinned payloads, per-content admission decisions or complete consumer
chains. The coordinator’s request for a missing final message is a
documented pull. It does not reveal what else the host selects or
delivers or whether the host compacted its transcript. No direct
frozen-source reads were needed.
