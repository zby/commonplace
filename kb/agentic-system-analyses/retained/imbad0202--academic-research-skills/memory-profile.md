---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Memory profile of academic-research-skills: retained task artifacts, recovery, corpus reuse and resolver decisions, with opaque host and optional-path limits."
run-id: "AAS-2026-10-17-academic-research-skills-6fe859d62c16-01"
source-identity: "https://github.com/Imbad0202/academic-research-skills"
reviewed-boundary: "060cb3cbffc2ca1bdfb8f7c6d2ffa4883cf09b1a"
memory-comparison:
  version: 2
  scope: "Accumulated task memory: Material Passport and referenced working artifacts, run/reset and inquiry histories, imported/exported corpus and screening decisions, resolver cache, reading declarations, criteria bindings, revision/audit markers and evidence, evaluation reports, process narrative, activity store, Pi activation state and the opaque host continuation interface. Includes incompletely inspected adapters, enrichment/audit/criteria/secondary-retention alternatives rather than assuming coverage. Excludes shipped static skill/rule files, ordinary transient returns without later retention, provider parameter implementations and external scholarly source truth; these are not classified as accumulated ARS task memory."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Local retained task files: passport/artifact references, run and inquiry ledgers, human read log, criteria manifest, activity store, screening decisions, working markers and revision/evaluation artifacts"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-run-ledger"
                - "memory.md#mem-obj-human-read-log"
                - "memory.md#mem-obj-review-criteria-binding"
                - "memory.md#mem-obj-activity-store"
                - "epistemic.md#epi-obj-screening-decisions"
              note: "Inspected writers retain the ledger, read declarations, binding manifest, activity history and screening JSON as local files."
            - value: "files"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-checkpoint-recovery"
                - "memory.md#mem-obj-inquiry-ledger"
                - "runtime.md#rt-obj-ref-markers"
                - "runtime.md#rt-rte-revision-review"
                - "runtime.md#rt-rte-evaluation-admission"
              note: "Recovery, inquiry publication and later revision/evaluation consumers specify retained local artifacts; this does not upgrade uninspected persistence helpers."
          records:
            - "runtime.md#rt-rte-checkpoint-recovery"
            - "runtime.md#rt-obj-run-ledger"
            - "memory.md#mem-obj-inquiry-ledger"
            - "memory.md#mem-obj-human-read-log"
            - "memory.md#mem-obj-review-criteria-binding"
            - "memory.md#mem-obj-activity-store"
            - "epistemic.md#epi-obj-screening-decisions"
            - "runtime.md#rt-obj-ref-markers"
            - "runtime.md#rt-rte-revision-review"
            - "runtime.md#rt-rte-evaluation-admission"
          note: "The named local objects are files; JSON/YAML/Markdown encoding does not imply a database or graph."
        - scope: "Imported/exported corpus files and prescribed process narrative files"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-literature-corpus"
              note: "Folder/import and screening serialization retain YAML citation records."
            - value: "files"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-process-record"
              note: "The process record is prescribed Markdown with optional PDF conversion."
          records:
            - "memory.md#mem-obj-literature-corpus"
            - "memory.md#mem-obj-process-record"
          note: "Corpus files have executable producers; process-file production is a model protocol."
        - scope: "Resolver-decision cache"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-verification-cache"
                - "memory.md#mem-rte-cache-verification"
              note: "The inspected cache API and verification caller store and reuse rows in verification.db."
          records:
            - "memory.md#mem-obj-verification-cache"
            - "memory.md#mem-rte-cache-verification"
          note: "The local persistent cache is explicitly SQLite, independently of its JSON payload encoding."
        - scope: "Host-owned Pi session entries and host continuation summaries"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-command-dispatch"
            - "runtime.md#rt-rte-checkpoint-recovery"
          note: "Branch-local activation is persisted by the host session manager, but its physical substrate and compaction storage are not inspected. No repo, in-memory, service-object or other substrate is inferred."
      records:
        - "runtime.md#rt-rte-checkpoint-recovery"
        - "runtime.md#rt-obj-run-ledger"
        - "memory.md#mem-obj-inquiry-ledger"
        - "memory.md#mem-obj-human-read-log"
        - "memory.md#mem-obj-review-criteria-binding"
        - "memory.md#mem-obj-activity-store"
        - "epistemic.md#epi-obj-screening-decisions"
        - "runtime.md#rt-obj-ref-markers"
        - "runtime.md#rt-rte-revision-review"
        - "runtime.md#rt-rte-evaluation-admission"
        - "memory.md#mem-obj-literature-corpus"
        - "memory.md#mem-obj-process-record"
        - "memory.md#mem-obj-verification-cache"
        - "memory.md#mem-rte-cache-verification"
        - "runtime.md#rt-rte-command-dispatch"
      note: "The inventory covers named task stores and the opaque host interface. It does not classify all runtime storage or equate versioned static instructions with accumulated memory; host storage and incompletely inspected optional histories prevent complete coverage."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Human/model-interpreted text in corpus abstracts/notes, inquiry branch statements, reading notes, retained user words and manuscript/process narratives"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-literature-corpus"
                - "memory.md#mem-obj-inquiry-ledger"
                - "memory.md#mem-obj-human-read-log"
                - "runtime.md#rt-obj-run-ledger"
              note: "Inspected retained objects include text interpreted as data or user decisions, not numerical representations."
            - value: "natural-language"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-revision-review"
                - "memory.md#mem-obj-process-record"
              note: "Manuscript revision and process-narrative consumers interpret retained prose under the shipped protocol."
          records:
            - "memory.md#mem-obj-literature-corpus"
            - "memory.md#mem-obj-inquiry-ledger"
            - "memory.md#mem-obj-human-read-log"
            - "runtime.md#rt-obj-run-ledger"
            - "runtime.md#rt-rte-revision-review"
            - "memory.md#mem-obj-process-record"
          note: "These text parts remain distinct from their symbolic IDs, hashes and receipt metadata."
        - scope: "Fixed-rule fields: ledger hashes/counters, corpus trust fields, read scopes/locators, criteria receipts, activity events, screening labels and marker grammar"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-run-ledger"
                - "memory.md#mem-obj-literature-corpus"
                - "memory.md#mem-obj-human-read-log"
                - "memory.md#mem-obj-review-criteria-binding"
                - "memory.md#mem-obj-activity-store"
                - "epistemic.md#epi-obj-screening-decisions"
                - "runtime.md#rt-obj-ref-markers"
              note: "Typed fields and identifiers are consumed by deterministic writers, resolvers and validators."
          records:
            - "runtime.md#rt-obj-run-ledger"
            - "memory.md#mem-obj-literature-corpus"
            - "memory.md#mem-obj-human-read-log"
            - "memory.md#mem-obj-review-criteria-binding"
            - "memory.md#mem-obj-activity-store"
            - "epistemic.md#epi-obj-screening-decisions"
            - "runtime.md#rt-obj-ref-markers"
          note: "Localized fields have fixed validation, matching or state-transition consumers; surrounding explanations are excluded from this unit."
        - scope: "Resolver cache decisions and retained evaluation metrics"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-verification-cache"
                - "runtime.md#rt-rte-evaluation-admission"
              note: "Stored decision dictionaries and task metrics drive lookup reuse and regression classification."
          records:
            - "memory.md#mem-obj-verification-cache"
            - "runtime.md#rt-rte-evaluation-admission"
          note: "Cache match/query/version fields and numeric comparison inputs have fixed code consumers."
        - scope: "Uninspected host continuation payload and optional audit/enrichment/criteria content paths"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-checkpoint-recovery"
            - "memory.md#mem-obj-review-criteria-binding"
            - "epistemic.md#epi-rte-claim-judgment"
          note: "The host summary is described as a model summary but its operative payload is opaque; criterion semantics and all optional audit consumers were not inspected. No parametric classification follows from using an external model."
      records:
        - "memory.md#mem-obj-literature-corpus"
        - "memory.md#mem-obj-inquiry-ledger"
        - "memory.md#mem-obj-human-read-log"
        - "runtime.md#rt-obj-run-ledger"
        - "runtime.md#rt-rte-revision-review"
        - "memory.md#mem-obj-process-record"
        - "memory.md#mem-obj-review-criteria-binding"
        - "memory.md#mem-obj-activity-store"
        - "epistemic.md#epi-obj-screening-decisions"
        - "runtime.md#rt-obj-ref-markers"
        - "memory.md#mem-obj-verification-cache"
        - "runtime.md#rt-rte-evaluation-admission"
        - "runtime.md#rt-rte-checkpoint-recovery"
        - "epistemic.md#epi-rte-claim-judgment"
      note: "Mixed prose and metadata are separated by consumption. Known text and symbolic witnesses do not classify opaque continuation payloads or complete every optional artifact path."
    lineage:
      assessment: "partial"
      units:
        - scope: "External corpus material admitted by filename adapter and screening export"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-literature-corpus"
              note: "User-owned source metadata enters the corpus through an inspected adapter."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-literature-corpus"
              note: "The serializer compiles screening decisions and reasons into reusable citation records."
          records:
            - "memory.md#mem-obj-literature-corpus"
            - "memory.md#mem-rte-corpus-reuse"
          note: "Imported material and the serializer derivation are distinct provenance paths; invoking import does not identify the original author or certify source warrant."
        - scope: "Explicit user reading declarations and author inquiry decisions"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-read-attestation"
                - "memory.md#mem-rte-inquiry-summary"
              note: "User commands supply reading scope; explicit author events decide inquiry adoption, rejection and reopening."
          records:
            - "memory.md#mem-obj-human-read-log"
            - "memory.md#mem-rte-read-attestation"
            - "memory.md#mem-obj-inquiry-ledger"
            - "memory.md#mem-rte-inquiry-summary"
          note: "Declaration/adoption is authored content, not independent evidence of reading or novelty."
        - scope: "Selected workflow words/outcomes and post-terminal adjudication history"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "afforded"
              records:
                - "runtime.md#rt-obj-run-ledger"
              note: "The orchestrator captures selected user words and execution outcomes before compaction under the recovery protocol."
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-activity-store"
                - "memory.md#mem-rte-activity-history"
              note: "The post-terminal helper extracts retained activity from sealed run sources."
          records:
            - "runtime.md#rt-obj-run-ledger"
            - "memory.md#mem-obj-activity-store"
            - "memory.md#mem-rte-activity-history"
          note: "Source activity is recorded or extracted; this is not provenance for all initialized passport fields."
        - scope: "Resolver match cache and criteria-binding receipts"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-verification-cache"
                - "memory.md#mem-rte-cache-verification"
                - "memory.md#mem-obj-review-criteria-binding"
              note: "Decision logic reduces resolver results; binding code constructs hashes, selected IDs and receipts."
          records:
            - "memory.md#mem-obj-verification-cache"
            - "memory.md#mem-rte-cache-verification"
            - "memory.md#mem-obj-review-criteria-binding"
          note: "These are fixed-code derivations from resolver results and supplied context/artifact bindings."
        - scope: "Process narrative derived from current session and earlier retained evidence"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-process-record"
              note: "Session history and ledger/passport evidence feed the prescribed process summary."
          records:
            - "memory.md#mem-obj-process-record"
          note: "The narrative has a described derivation but no observed production instance."
        - scope: "Initial passport/profile/criteria content, generic injected cache dictionaries, other corpus adapters and host summaries"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-review-criteria-binding"
            - "memory.md#mem-rte-cache-verification"
            - "runtime.md#rt-rte-checkpoint-recovery"
            - "memory.md#mem-obj-literature-corpus"
          note: "Initial declaration control, caller-supplied dictionary provenance, non-folder adapter details and host derivation are not established; known subsequent derivations do not settle these alternatives."
      records:
        - "memory.md#mem-obj-literature-corpus"
        - "memory.md#mem-rte-corpus-reuse"
        - "memory.md#mem-obj-human-read-log"
        - "memory.md#mem-rte-read-attestation"
        - "memory.md#mem-obj-inquiry-ledger"
        - "memory.md#mem-rte-inquiry-summary"
        - "runtime.md#rt-obj-run-ledger"
        - "memory.md#mem-obj-activity-store"
        - "memory.md#mem-rte-activity-history"
        - "memory.md#mem-obj-verification-cache"
        - "memory.md#mem-rte-cache-verification"
        - "memory.md#mem-obj-review-criteria-binding"
        - "memory.md#mem-obj-process-record"
        - "runtime.md#rt-rte-checkpoint-recovery"
      note: "Positive provenance paths coexist with unknown initialization and opaque alternatives. Neither static repository authorship nor external model weights substitutes for the lineage of accumulated task material."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Corpus prose and metadata at later literature roles"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-corpus-reuse"
              note: "Corpus content supplies bibliography/matrix/gap context to later literature work."
          records:
            - "memory.md#mem-obj-literature-corpus"
            - "memory.md#mem-rte-corpus-reuse"
          note: "The consumer re-screens retained records as untrusted research data and can skip them; it does not adopt them as instructions."
        - scope: "Run-ledger decisions, receipts and counters at recovery and dispatch"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "afforded"
              records:
                - "runtime.md#rt-obj-run-ledger"
                - "runtime.md#rt-rte-checkpoint-recovery"
              note: "Quoted user decisions restore author directions for subsequent dispatch."
            - value: "routing"
              basis: "afforded"
              records:
                - "runtime.md#rt-obj-run-ledger"
                - "runtime.md#rt-rte-checkpoint-recovery"
              note: "Recovered decisions, valid receipts and conservative counters select continuation and retry state."
            - value: "knowledge"
              basis: "afforded"
              records:
                - "runtime.md#rt-obj-run-ledger"
              note: "Stage 6 can use retained original words as process evidence."
          records:
            - "runtime.md#rt-obj-run-ledger"
            - "runtime.md#rt-rte-checkpoint-recovery"
          note: "Actual consumer roles are the resumed orchestrator and its selected handoffs; the entire ledger is not dispatched."
        - scope: "Pi activation bit at adapter callback"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-command-dispatch"
              note: "Session/branch restore changes whether adapter guidance is injected."
          records:
            - "runtime.md#rt-rte-command-dispatch"
          note: "The retained bit selects active compatibility-guidance injection, rather than recalling paper content."
        - scope: "Cached resolver decisions at later verification wrapper"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cache-verification"
              note: "The saved match/query decision substitutes for a live resolver result."
          records:
            - "memory.md#mem-obj-verification-cache"
            - "memory.md#mem-rte-cache-verification"
          note: "Matching/version/type checks permit use of a saved lookup decision, which then supplies finalization evidence."
        - scope: "Reading log scopes and rescissions at the coverage resolver"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-rte-read-attestation"
                - "epistemic.md#epi-rte-read-withdrawal"
              note: "Current scope/locators and latest events determine anchor coverage eligibility."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-rte-read-attestation"
                - "epistemic.md#epi-rte-read-withdrawal"
              note: "Rescission or invalid/insufficient scope prevents covered eligibility in the resolver."
          records:
            - "memory.md#mem-obj-human-read-log"
            - "memory.md#mem-rte-read-attestation"
            - "epistemic.md#epi-rte-read-withdrawal"
          note: "The ledger supplies criteria and withdrawable eligibility; it is not proof of actual reading."
        - scope: "Criteria-binding manifest at initialization/receipt/handoff validation"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-review-criteria-binding"
              note: "Retained target/hash/receipt bindings determine whether supplied artifacts conform."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-review-criteria-binding"
              note: "Changed same-review authority or conflicting repeat receipts are refused."
            - value: "routing"
              basis: "afforded"
              records:
                - "memory.md#mem-obj-review-criteria-binding"
              note: "The tracker contract restricts refusal to the mismatched criteria-aware handoff."
          records:
            - "memory.md#mem-obj-review-criteria-binding"
          note: "This is identity/binding validation, not established semantic application of criterion prose."
        - scope: "Inquiry projection at author/foreground checkpoints and process narrative at human reader"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-inquiry-summary"
              note: "Live branch statements and stale-cause context inform checkpoint judgment."
            - value: "knowledge"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-process-record"
              note: "The process narrative supports human sharing/reporting/reflection, without an established automatic lesson-adoption path."
          records:
            - "memory.md#mem-rte-inquiry-summary"
            - "memory.md#mem-obj-process-record"
          note: "Selected alternatives and narrative supply context/advice; the inquiry ledger cannot override integrity gates."
        - scope: "Retained working marker statuses and revision authority at formatter/writer consumers"
          assessment: "known"
          findings:
            - value: "validation"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-final-output"
                - "runtime.md#rt-rte-revision-review"
              note: "Current evidence/policy stamps and exact author scope are criteria for output/patch admission."
            - value: "enforcement"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-final-output"
                - "runtime.md#rt-rte-revision-review"
              note: "Terminal marker failures and unauthorized patches are prescribed refusal conditions."
            - value: "instruction"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-revision-review"
              note: "The retained author sidecar supplies exact authorized revision scope."
          records:
            - "runtime.md#rt-obj-ref-markers"
            - "runtime.md#rt-rte-final-output"
            - "runtime.md#rt-rte-revision-review"
          note: "These forces attach to retained task controls, not the static rules that interpret them."
        - scope: "Stored screening decisions, pilot results and evaluation measurements at reporting/admission consumers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-screening-merge"
              note: "Retained decisions select final eligibility, pending work and export inputs."
            - value: "validation"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-pilot-comparison"
                - "runtime.md#rt-rte-screening-fanout"
                - "runtime.md#rt-rte-evaluation-admission"
              note: "Saved pilot/context evidence and baseline metrics determine current run/change admission checks."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-screening-fanout"
              note: "The builder withholds full-run generation on a failing/stale pilot absent an explicit override."
          records:
            - "epistemic.md#epi-rte-screening-merge"
            - "epistemic.md#epi-rte-pilot-comparison"
            - "runtime.md#rt-rte-screening-fanout"
            - "runtime.md#rt-rte-evaluation-admission"
          note: "Different retained results have different effects; none is a scientific truth oracle."
        - scope: "Resolver execution evidence at automatic cache-update consumer"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cache-verification"
              note: "Resolver results feed automatic production of reusable behavior-shaping lookup decisions."
          records:
            - "memory.md#mem-rte-cache-verification"
          note: "Learning here is the force of trace input at the durable decision-update path, not demonstrated improvement or downstream instruction authority."
        - scope: "Activity history at human display; host summaries, semantic criteria consumers and remaining audit/review effects"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-activity-history"
            - "runtime.md#rt-rte-checkpoint-recovery"
            - "memory.md#mem-obj-review-criteria-binding"
            - "epistemic.md#epi-rte-claim-judgment"
            - "epistemic.md#epi-rte-synthesis-content"
          note: "Activity is explicitly excluded from model/gate inputs; its human counts do not establish a controlled behavioral force. Host-summary effects, full criterion application, optional audit paths and retained synthesis weighting are incomplete. No unsupported ranking or blanket learning force is inferred."
      records:
        - "memory.md#mem-obj-literature-corpus"
        - "memory.md#mem-rte-corpus-reuse"
        - "runtime.md#rt-obj-run-ledger"
        - "runtime.md#rt-rte-checkpoint-recovery"
        - "runtime.md#rt-rte-command-dispatch"
        - "memory.md#mem-obj-verification-cache"
        - "memory.md#mem-rte-cache-verification"
        - "memory.md#mem-obj-human-read-log"
        - "memory.md#mem-rte-read-attestation"
        - "epistemic.md#epi-rte-read-withdrawal"
        - "memory.md#mem-obj-review-criteria-binding"
        - "memory.md#mem-rte-inquiry-summary"
        - "memory.md#mem-obj-process-record"
        - "runtime.md#rt-obj-ref-markers"
        - "runtime.md#rt-rte-final-output"
        - "runtime.md#rt-rte-revision-review"
        - "epistemic.md#epi-rte-screening-merge"
        - "epistemic.md#epi-rte-pilot-comparison"
        - "runtime.md#rt-rte-screening-fanout"
        - "runtime.md#rt-rte-evaluation-admission"
        - "memory.md#mem-rte-activity-history"
        - "epistemic.md#epi-rte-claim-judgment"
        - "epistemic.md#epi-rte-synthesis-content"
      note: "The inventory distinguishes retained parts, consumers and effects, including update versus downstream authority. Several controls have wired local effects but model refusal and context-use remain protocol/affordance. Unassessed optional effects prevent an exhaustive authority union."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Automatic admission by inspected folder/export writers, resolver cache computation, screening merge, criteria receipt checks and activity append"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-literature-corpus"
                - "memory.md#mem-rte-cache-verification"
                - "epistemic.md#epi-rte-screening-merge"
                - "memory.md#mem-obj-review-criteria-binding"
                - "memory.md#mem-rte-activity-history"
              note: "Producer/parser/checker rules admit derived metadata, decisions, receipts and activity records."
          records:
            - "memory.md#mem-obj-literature-corpus"
            - "memory.md#mem-rte-cache-verification"
            - "epistemic.md#epi-rte-screening-merge"
            - "memory.md#mem-obj-review-criteria-binding"
            - "memory.md#mem-rte-activity-history"
          note: "Software admits each result without a separate human content decision; starting the import/run or selecting a store is not per-content approval."
        - scope: "Run-ledger event capture under orchestrator protocol and model process-summary generation"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-run-ledger"
                - "memory.md#mem-obj-process-record"
              note: "The workflow prescribes capture and generated summary content; successful operation is unobserved."
          records:
            - "runtime.md#rt-obj-run-ledger"
            - "memory.md#mem-obj-process-record"
          note: "The model selects/captures event content or generates a narrative, rather than receiving per-entry human approval."
        - scope: "User reading marks/rescissions, explicit author inquiry adoption and item-level manuscript authority"
          assessment: "known"
          findings:
            - value: "manual"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-read-attestation"
                - "memory.md#mem-rte-inquiry-summary"
              note: "The user declares reading scope and decides author-owned inquiry events."
            - value: "manual"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-revision-review"
              note: "Item-level author choices authorize the retained revision scope before writer proposals."
          records:
            - "memory.md#mem-rte-read-attestation"
            - "memory.md#mem-rte-inquiry-summary"
            - "runtime.md#rt-rte-revision-review"
          note: "The operator explicitly supplies or approves this retained content; subsequent mechanical I/O does not alter that agency."
        - scope: "Pi activation entry admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-command-dispatch"
              note: "Adapter callbacks set and persist the activation bit."
          records:
            - "runtime.md#rt-rte-command-dispatch"
          note: "A recognized start/stop/input event causes software to append/restore activation state, without per-entry content approval."
        - scope: "Initial passport/criteria/profile creation, generic caller-injected cache dictionaries, other adapter and host summary admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-review-criteria-binding"
            - "memory.md#mem-rte-cache-verification"
            - "runtime.md#rt-rte-checkpoint-recovery"
            - "memory.md#mem-obj-literature-corpus"
          note: "Generic caller identity does not settle operator control. Criteria initialization and opaque summary control are incompletely inspected; automatic known cache computation does not upgrade these routes."
      records:
        - "memory.md#mem-obj-literature-corpus"
        - "memory.md#mem-rte-cache-verification"
        - "epistemic.md#epi-rte-screening-merge"
        - "memory.md#mem-obj-review-criteria-binding"
        - "memory.md#mem-rte-activity-history"
        - "runtime.md#rt-obj-run-ledger"
        - "memory.md#mem-obj-process-record"
        - "memory.md#mem-rte-read-attestation"
        - "memory.md#mem-rte-inquiry-summary"
        - "runtime.md#rt-rte-revision-review"
        - "runtime.md#rt-rte-command-dispatch"
        - "runtime.md#rt-rte-checkpoint-recovery"
      note: "Admission is classified per mechanism, not by authorship or filesystem write. Known manual declarations and automatic transformations coexist with unresolved initialization and external control."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Human reading declaration withdrawal"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-read-attestation"
              note: "The unmark writer adds rescinded_at instead of erasing the original mark."
          records:
            - "memory.md#mem-rte-read-attestation"
            - "memory.md#mem-obj-human-read-log"
          note: "Rescission withdraws current eligibility while keeping declaration history."
        - scope: "Resolver-decision replacement and stale-row reuse policy"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cache-verification"
              note: "Live recomputation can replace the retained lookup decision."
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cache-verification"
              note: "TTL expiry removes a row from eligible reuse, even when bytes remain stored."
          records:
            - "memory.md#mem-rte-cache-verification"
          note: "Fresh computation replaces an existing decision; expired rows become misses. No deduplication follows from composite keys."
        - scope: "Selected activity-history deletion"
          assessment: "known"
          findings:
            - value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-rte-activity-history"
              note: "Confirmed deletion forgets selected retained history and changes later displays."
          records:
            - "memory.md#mem-rte-activity-history"
          note: "The inspected deletion functions remove retained runs/whole stores; token checks do not authenticate human identity."
        - scope: "Prescribed process-history reduction"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records:
                - "memory.md#mem-obj-process-record"
              note: "The model is directed to reduce process history and retained evidence to a durable narrative."
          records:
            - "memory.md#mem-obj-process-record"
          note: "This consolidates existing session/ledger claims; lessons do not by themselves prove novel synthesis."
        - scope: "Author-scoped manuscript revision over retained drafts"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-revision-review"
              note: "The writer/apply protocol revises an existing draft within author scope."
          records:
            - "runtime.md#rt-rte-revision-review"
          note: "The operation revises a task artifact, not automatically ARS method text; helper internals remain unaudited."
        - scope: "Inquiry merge/replay, other adapters/enrichment, audit history, host compaction and semantically indeterminate synthesis"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-inquiry-summary"
            - "memory.md#mem-obj-literature-corpus"
            - "runtime.md#rt-rte-checkpoint-recovery"
            - "epistemic.md#epi-rte-synthesis-content"
          note: "Route names, index/receipt updates and acquisition alone establish no curation value. Host summary transformation is opaque; synthesis requests do not establish whether retained claims were compressed or newly created."
      records:
        - "memory.md#mem-rte-read-attestation"
        - "memory.md#mem-obj-human-read-log"
        - "memory.md#mem-rte-cache-verification"
        - "memory.md#mem-rte-activity-history"
        - "memory.md#mem-obj-process-record"
        - "runtime.md#rt-rte-revision-review"
        - "memory.md#mem-rte-inquiry-summary"
        - "memory.md#mem-obj-literature-corpus"
        - "runtime.md#rt-rte-checkpoint-recovery"
        - "epistemic.md#epi-rte-synthesis-content"
      note: "Positive transformations are local, with their own evidence layers. No dedup, promote or synthesize value is asserted solely from command names, collision checks, eligibility promotion or a request for new understanding; unresolved optional transformations remain included."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Requested corpus supply, cache lookup, reading-coverage query and activity render"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-corpus-reuse"
                - "memory.md#mem-rte-read-attestation"
              note: "Literature/finalizer consumers request the supplied corpus or citation coverage."
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cache-verification"
                - "memory.md#mem-rte-activity-history"
              note: "Exact-key verification lookup and explicit render return requested retained decisions/history."
          records:
            - "memory.md#mem-rte-corpus-reuse"
            - "memory.md#mem-rte-cache-verification"
            - "memory.md#mem-rte-read-attestation"
            - "memory.md#mem-rte-activity-history"
          note: "Consumer requests are fulfilled from retained material. Code delivery of a requested result is not an extra push."
        - scope: "Explicit fresh-session resume and named artifact reload"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "runtime.md#rt-rte-checkpoint-recovery"
              note: "The reset contract reloads a user-provided passport and referenced artifacts."
          records:
            - "runtime.md#rt-rte-checkpoint-recovery"
          note: "The user supplies the passport and the resumed orchestrator loads named references; requested reconstruction is pull."
        - scope: "Automatic checkpoint inquiry display"
          assessment: "known"
          findings:
            - value: "push"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-inquiry-summary"
              note: "The orchestrator inserts the generated live-branch/stale-artifact block at designated moments."
          records:
            - "memory.md#mem-rte-inquiry-summary"
          note: "Named checkpoint moments or a recorded signal trigger a selector without a separate request for each displayed branch."
        - scope: "Branch/session activation restoration and automatic recovery checks"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-command-dispatch"
              note: "Session-start/tree-change callbacks select retained activation state for current adapter control."
            - value: "push"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-run-ledger"
                - "runtime.md#rt-rte-checkpoint-recovery"
              note: "Protocol-triggered ledger checking supplies recovered decision/counter state after compaction, subagent return and stage close."
          records:
            - "runtime.md#rt-rte-command-dispatch"
            - "runtime.md#rt-obj-run-ledger"
            - "runtime.md#rt-rte-checkpoint-recovery"
          note: "Activation restoration and required post-return/compaction ledger checks are distinguished from the requested resume artifact read."
        - scope: "Requested later comparison of saved evaluation reports"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-evaluation-admission"
              note: "The numeric checker reads the supplied retained reports for its requested comparison."
          records:
            - "runtime.md#rt-rte-evaluation-admission"
          note: "A later gate invocation explicitly consumes baseline/compare reports."
        - scope: "Host summary delivery, all optional cross-model retention, detailed criteria consumers and later process-lesson adoption"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-checkpoint-recovery"
            - "runtime.md#rt-rte-cross-verification"
            - "memory.md#mem-obj-review-criteria-binding"
            - "memory.md#mem-obj-process-record"
          note: "No unified external summary/secondary-store consumer route or automatic lesson reload is established; prescribed output alone does not classify an unknown later delivery."
      records:
        - "memory.md#mem-rte-corpus-reuse"
        - "memory.md#mem-rte-cache-verification"
        - "memory.md#mem-rte-read-attestation"
        - "memory.md#mem-rte-activity-history"
        - "runtime.md#rt-rte-checkpoint-recovery"
        - "memory.md#mem-rte-inquiry-summary"
        - "runtime.md#rt-rte-command-dispatch"
        - "runtime.md#rt-obj-run-ledger"
        - "runtime.md#rt-rte-evaluation-admission"
        - "runtime.md#rt-rte-cross-verification"
        - "memory.md#mem-obj-review-criteria-binding"
        - "memory.md#mem-obj-process-record"
      note: "The inventory preserves pull and push within different chains and keeps opaque alternatives. A known request-driven route cannot make uninspected host/optional delivery inapplicable."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Checkpoint-triggered inquiry summary selection"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-inquiry-summary"
              note: "Inspected summary code selects live-status branches and summary-level context; this is not semantic nearest-neighbor retrieval."
          records:
            - "memory.md#mem-rte-inquiry-summary"
          note: "Trigger: designated checkpoint or recorded signal. Inputs: feature flag, branch count, live statuses, summary moment and optional signal event. Selected parts: live statements/status/provenance and stale-artifact context."
        - scope: "Session-start/tree-change activation restore"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-command-dispatch"
              note: "The callback filters the branch entry class and takes its latest state for guidance control."
          records:
            - "runtime.md#rt-rte-command-dispatch"
          note: "Trigger: session/branch event. Inputs: current branch custom entries and ARS state type. Selected part: latest applicable activation entry. This is coarse availability/latest-state selection, not a requested path identifier."
        - scope: "Protocol-triggered run-ledger recovery comparisons"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-run-ledger"
                - "runtime.md#rt-rte-checkpoint-recovery"
              note: "Claims and expected-step bindings target particular recorded decisions/outcomes rather than topical relevance."
          records:
            - "runtime.md#rt-obj-run-ledger"
            - "runtime.md#rt-rte-checkpoint-recovery"
          note: "Trigger: compaction, subagent return or stage close. Inputs: claimed decisions/expected steps and recorded artifact bindings. Selected parts: corresponding preserved words and valid receipt outcomes, with conservative counter recovery."
        - scope: "Opaque summary selection and optional inquiry signal/payload, criteria and audit alternatives"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-checkpoint-recovery"
            - "memory.md#mem-rte-inquiry-summary"
            - "memory.md#mem-obj-review-criteria-binding"
            - "epistemic.md#epi-rte-claim-judgment"
          note: "No inspected payload/selector account classifies all host and optional paths. A cache composite key and requested corpus filename belong to pull routes, not evidence of identifier push."
      records:
        - "memory.md#mem-rte-inquiry-summary"
        - "runtime.md#rt-rte-command-dispatch"
        - "runtime.md#rt-obj-run-ledger"
        - "runtime.md#rt-rte-checkpoint-recovery"
        - "memory.md#mem-obj-review-criteria-binding"
        - "epistemic.md#epi-rte-claim-judgment"
      note: "Only independently selected push operations receive signals. Inquiry display code is wired even though orchestrator delivery is afforded. Pull requests are excluded from signal findings, but unresolved directions prevent axis inapplicability."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Resolver-result to retained match decision to later verification"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cache-verification"
              note: "The cache writer derives and persists resolver decisions and later hits substitute them for new execution."
          records:
            - "memory.md#mem-rte-cache-verification"
            - "memory.md#mem-obj-verification-cache"
          note: "Automatic computation writes a durable behavior-shaping decision that a later exact-key verification invocation consumes. This satisfies the route definition without parameter training or measured gain."
        - scope: "Selected user/tool outcome capture to durable run ledger to later recovery"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-run-ledger"
                - "runtime.md#rt-rte-checkpoint-recovery"
              note: "Automatic prescribed event capture produces persistent recovery state used at later invocations; raw unconsumed logs alone would not suffice."
          records:
            - "runtime.md#rt-obj-run-ledger"
            - "runtime.md#rt-rte-checkpoint-recovery"
          note: "The model-operated capture path retains decision words, execution receipts and counters for resumed behavior. Its software append is inspected, but the complete trace-selection/consumer chain is protocol-level."
        - scope: "Activity history and process narrative at their later consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-activity-history"
            - "memory.md#mem-obj-process-record"
          note: "Activity extraction is automatic but model/gate use is forbidden; its human display does not establish a behavior-shaping update. Process summary has a human output reader but no established automatic lesson-adoption route. Neither provides a bounded absence record for a local no."
        - scope: "Host continuation summaries and remaining optional write/consumer paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-checkpoint-recovery"
            - "memory.md#mem-obj-review-criteria-binding"
            - "epistemic.md#epi-rte-claim-judgment"
            - "runtime.md#rt-rte-cross-verification"
          note: "Host compaction could qualify if automatic retained summaries reach later context, but its actual generation/payload route is opaque. Optional criteria/audit/secondary retention lacks complete trace-fed write coverage; no system-wide no is warranted."
      records:
        - "memory.md#mem-rte-cache-verification"
        - "memory.md#mem-obj-verification-cache"
        - "runtime.md#rt-obj-run-ledger"
        - "runtime.md#rt-rte-checkpoint-recovery"
        - "memory.md#mem-rte-activity-history"
        - "memory.md#mem-obj-process-record"
        - "memory.md#mem-obj-review-criteria-binding"
        - "epistemic.md#epi-rte-claim-judgment"
        - "runtime.md#rt-rte-cross-verification"
      note: "The cache and prescribed ledger route support local positive trace-fed writes. Host and optional routes remain unresolved. This axis is not a claim of improved capacity, reflection, autonomous self-improvement or changes to provider weights."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Original resolver execution results feeding match-cache admission"
          assessment: "known"
          findings:
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-rte-cache-verification"
              note: "The automatic cache transformation consumes resolver results and retains their reduced lookup decisions."
          records:
            - "memory.md#mem-rte-cache-verification"
          note: "These are recorded external lookup execution results, not session messages or model-reasoning trajectories."
        - scope: "Original conversational words and execution outcomes captured into run-ledger recovery state"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-run-ledger"
              note: "Selected user conversational words are retained by the prescribed capture route."
            - value: "tool-traces"
              basis: "claimed"
              records:
                - "runtime.md#rt-obj-run-ledger"
              note: "Selected stdout/exit outcomes from subagent/helper work feed durable receipts for later recovery."
          records:
            - "runtime.md#rt-obj-run-ledger"
            - "runtime.md#rt-rte-checkpoint-recovery"
          note: "Original content determines the categories; labeling the destination an event ledger does not turn all its inputs into event-streams."
        - scope: "Original input mix of host continuation summaries and optional trace-fed paths"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-checkpoint-recovery"
            - "memory.md#mem-obj-review-criteria-binding"
            - "epistemic.md#epi-rte-claim-judgment"
            - "runtime.md#rt-rte-cross-verification"
          note: "The exact summary inputs and optional producer provenance are uninspected; no trajectories or event-streams value follows from ledger/event serialization. Known cache/ledger sources cannot make this unit inapplicable."
      records:
        - "memory.md#mem-rte-cache-verification"
        - "runtime.md#rt-obj-run-ledger"
        - "runtime.md#rt-rte-checkpoint-recovery"
        - "memory.md#mem-obj-review-criteria-binding"
        - "epistemic.md#epi-rte-claim-judgment"
        - "runtime.md#rt-rte-cross-verification"
      note: "Only qualifying positive trace-learning routes are given source findings. Activity history and process narrative do not add trace-source positives without an established qualifying update/consumer chain; opaque qualifying alternatives remain unresolved."
---

# academic-research-skills memory profile

## Comparison rationale

This profile classifies accepted records, not new source evidence. All ten axes
remain partial because their inventories include unresolved host or optional
paths. A strong cache or file-writing witness does not resolve another
admission mechanism, payload or later consumer. Findings with different bases
remain separate even when their controlled value agrees.

The resolver cache is SQLite with symbolic, compiled decisions. Its retained
result supplies knowledge to later verification; the original resolver results
have learning authority at the automatic durable-update consumer. The trace
learning value means this write-and-later-consumer route, not improved accuracy
or parameter training. Its source is tool execution feedback, not an inferred
session transcript. See [MEM-OBJ-verification-cache](memory.md#mem-obj-verification-cache)
and [MEM-RTE-cache-verification](memory.md#mem-rte-cache-verification).

Selected session words and tool outcomes also feed durable recovery state.
The complete capture-to-recovery chain is prescribed rather than observed;
the ledger append helper's wiring does not upgrade that chain. This supports a
claimed trace-learning route without treating every raw log as learned guidance.
The retained decisions supply directions, while receipts/counters route recovery.
See [RT-OBJ-run-ledger](runtime.md#rt-obj-run-ledger) and
[RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery), including their
memory annotations. Host summary production remains opaque, not an evidenced
negative or a hidden complete-value assertion.

Corpus imports supply data, not standing directions. Imported and compiled
lineage coexist; starting an import does not make its automatic per-record
admission manual. Explicit reading declarations, author inquiry adoption and
revision authorizations instead have local human control. Criteria bindings
validate identities and receipts, not substantive application of criterion
meaning. See [MEM-RTE-corpus-reuse](memory.md#mem-rte-corpus-reuse),
[MEM-RTE-read-attestation](memory.md#mem-rte-read-attestation),
[MEM-RTE-inquiry-summary](memory.md#mem-rte-inquiry-summary),
[MEM-OBJ-review-criteria-binding](memory.md#mem-obj-review-criteria-binding) and
[RT-RTE-revision-review](runtime.md#rt-rte-revision-review).

Read-back direction is operation-local. Exact-key cache queries and explicit
history rendering are pull. Automatic checkpoint inquiry display and session
activation restoration are push. Inquiry's summary selector is inspected code,
while its insertion into model context is an afforded orchestration route.
A requested file identifier is not an identifier-push witness. See
[MEM-RTE-cache-verification](memory.md#mem-rte-cache-verification),
[MEM-RTE-activity-history](memory.md#mem-rte-activity-history),
[MEM-RTE-inquiry-summary](memory.md#mem-rte-inquiry-summary) and
[RT-RTE-command-dispatch](runtime.md#rt-rte-command-dispatch).

Curation findings follow transformations, not names. Read rescission invalidates
reliance while retaining history; cache replacement evolves a decision and TTL
expiry removes reuse eligibility. Activity deletion forgets selected history.
The prescribed process narrative consolidates existing history. Index updates,
idempotence checks and a request for new synthesis do not establish deduplication
or novel-claim synthesis. See
[MEM-RTE-read-attestation](memory.md#mem-rte-read-attestation),
[MEM-RTE-cache-verification](memory.md#mem-rte-cache-verification),
[MEM-RTE-activity-history](memory.md#mem-rte-activity-history),
[MEM-OBJ-process-record](memory.md#mem-obj-process-record) and
[EPI-RTE-synthesis-content](epistemic.md#epi-rte-synthesis-content).

Reconciliation supersedes the duplicate epistemic reading-ledger object with
[MEM-OBJ-human-read-log](memory.md#mem-obj-human-read-log). This profile cites that
canonical object, retaining the distinct writer/resolution routes. No other
supersession changes a value. Valid stage/final-output containers do not replace
the more specific cache, corpus, reading or screening records.

Activity extraction is retained history but its contract excludes model, gate
and checkpoint input. The process record has a human reader without an
established automatic lesson-consumption route. Neither establishes a blanket
negative trace-learning classification; no bounded absence record is declared
for that purpose. Unknown initial-content control, generic cache caller
provenance, complete criterion consumers and optional audit/secondary retention
remain limitations, not silently excluded alternatives. See
[MEM-RTE-activity-history](memory.md#mem-rte-activity-history),
[MEM-OBJ-process-record](memory.md#mem-obj-process-record),
[MEM-OBJ-review-criteria-binding](memory.md#mem-obj-review-criteria-binding),
[EPI-RTE-claim-judgment](epistemic.md#epi-rte-claim-judgment) and
[RT-RTE-cross-verification](runtime.md#rt-rte-cross-verification).

Source-read log: none. Classification uses only supplied records and their
annotations; no frozen-source files or incumbent/reference profiles were read.
