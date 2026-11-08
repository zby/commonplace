---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Amanuensis memory comparison: retained conspectus, task packets, publication and unresolved outcome-to-policy consumers at the frozen revision."
run-id: "AAS-2026-11-08-amanuensis-b3a8e3e53488-01"
source-identity: "https://github.com/nfeldman/amanuensis"
reviewed-boundary: "a98093dc7aad3c0e64d42132ece305fc5ea7f3f9"
memory-comparison:
  version: 2
  scope: "Accumulated SQLite survey accounts, evidence, findings, explanations, standing/access metadata, carry obligations, registered prose and Git checkpoints; derived task briefs/design packets, research and review/evaluation records, generated views, and lesson/policy history and representations. Includes unresolved registered maintenance, review/design/composition, revalidation/evaluation, adapter and development-driver alternatives. Excludes static shipped instructions, ordinary transient current-request state and external host/provider internals; their storage and parameters are not memory findings."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Inspected retained conspectus content, provenance, standing, usage, task/research and learning tables"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records: ["memory.md#mem-obj-claims","memory.md#mem-obj-findings","memory.md#mem-obj-explanations","memory.md#mem-obj-field-notes","memory.md#mem-obj-file-ledger","memory.md#mem-obj-query-log","memory.md#mem-obj-access-log","memory.md#mem-obj-carried-findings","memory.md#mem-obj-codebase-brief","memory.md#mem-obj-research-results","memory.md#mem-obj-learning-lessons","memory.md#mem-obj-learning-policy","epistemic.md#epi-obj-evidence","epistemic.md#epi-obj-dispositions","epistemic.md#epi-obj-contradictions","epistemic.md#epi-obj-diagnosticity","epistemic.md#epi-obj-review-analysis","epistemic.md#epi-obj-blind-truth"]
              note: "These retained objects and their access/event metadata are SQLite rows; relational links do not separately establish a graph substrate."
          records: ["memory.md#mem-obj-claims","memory.md#mem-obj-findings","memory.md#mem-obj-explanations","memory.md#mem-obj-field-notes","memory.md#mem-obj-file-ledger","memory.md#mem-obj-query-log","memory.md#mem-obj-access-log","memory.md#mem-obj-carried-findings","memory.md#mem-obj-codebase-brief","memory.md#mem-obj-research-results","memory.md#mem-obj-learning-lessons","memory.md#mem-obj-learning-policy","epistemic.md#epi-obj-evidence","epistemic.md#epi-obj-dispositions","epistemic.md#epi-obj-contradictions","epistemic.md#epi-obj-diagnosticity","epistemic.md#epi-obj-review-analysis","epistemic.md#epi-obj-blind-truth"]
          note: "Covers the declared SQLite objects, including policy storage even though configuration semantics remain opaque."
        -
          scope: "Registered prose and generated conspectus views"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records: ["memory.md#mem-obj-prose-artifacts","runtime.md#rt-rte-docs-publication"]
              note: "Registered prose and derived HTML/Markdown are filesystem artifacts; file existence is not assured by registration alone."
          records: ["memory.md#mem-obj-prose-artifacts","runtime.md#rt-rte-docs-publication"]
          note: "Includes both durable prose inputs and regenerable later-readable outputs."
        -
          scope: "Versioned conspectus checkpoints"
          assessment: "known"
          findings:
            -
              value: "repo"
              basis: "wired"
              records: ["runtime.md#rt-rte-survey-cycle","runtime.md#rt-rte-docs-publication"]
              note: "Survey state has storage Git checkpoints; this is not model-weight persistence."
          records: ["runtime.md#rt-rte-survey-cycle","runtime.md#rt-rte-docs-publication"]
          note: "Checkpoint recovery is bounded by the active-session ordering caveat."
        -
          scope: "Additional registered memory, maintenance, evaluation and driver alternatives"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-policy-admission","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-tool-dispatch"]
          note: "Included composition, review/design-session, impact/revalidation/refresh, evaluation/envelope, adapter recovery and development/historical-driver alternatives are not fully traced by accepted records. Their operative payloads, admission and later consumers cannot be completely classified."
      records: ["memory.md#mem-obj-claims","memory.md#mem-obj-findings","memory.md#mem-obj-explanations","memory.md#mem-obj-field-notes","memory.md#mem-obj-file-ledger","memory.md#mem-obj-query-log","memory.md#mem-obj-access-log","memory.md#mem-obj-carried-findings","memory.md#mem-obj-codebase-brief","memory.md#mem-obj-research-results","memory.md#mem-obj-learning-lessons","memory.md#mem-obj-learning-policy","epistemic.md#epi-obj-evidence","epistemic.md#epi-obj-dispositions","epistemic.md#epi-obj-contradictions","epistemic.md#epi-obj-diagnosticity","epistemic.md#epi-obj-review-analysis","epistemic.md#epi-obj-blind-truth","memory.md#mem-obj-prose-artifacts","runtime.md#rt-rte-docs-publication","runtime.md#rt-rte-survey-cycle","runtime.md#rt-rte-policy-admission","runtime.md#rt-rte-tool-dispatch"]
      note: "SQLite, files and storage-repository persistence are supported locally; included alternative state/driver chains prevent complete substrate coverage. External provider weights and static shipped skills are outside this accumulated-memory inventory."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Interpretive survey/research/prose bodies and usage questions"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records: ["memory.md#mem-obj-claims","memory.md#mem-obj-findings","memory.md#mem-obj-explanations","memory.md#mem-obj-field-notes","memory.md#mem-obj-prose-artifacts","memory.md#mem-obj-query-log","memory.md#mem-obj-carried-findings","memory.md#mem-obj-research-results","epistemic.md#epi-obj-evidence","epistemic.md#epi-obj-dispositions","epistemic.md#epi-obj-contradictions","epistemic.md#epi-obj-diagnosticity","epistemic.md#epi-obj-review-analysis"]
              note: "Bodies, excerpts, reasons and questions require human/model interpretation."
          records: ["memory.md#mem-obj-claims","memory.md#mem-obj-findings","memory.md#mem-obj-explanations","memory.md#mem-obj-field-notes","memory.md#mem-obj-prose-artifacts","memory.md#mem-obj-query-log","memory.md#mem-obj-carried-findings","memory.md#mem-obj-research-results","epistemic.md#epi-obj-evidence","epistemic.md#epi-obj-dispositions","epistemic.md#epi-obj-contradictions","epistemic.md#epi-obj-diagnosticity","epistemic.md#epi-obj-review-analysis"]
          note: "Text is split from the fixed-rule fields in the same rows."
        -
          scope: "Typed identifiers, validity, standing, provenance, selection and evaluation fields"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records: ["memory.md#mem-obj-claims","memory.md#mem-obj-findings","memory.md#mem-obj-explanations","memory.md#mem-obj-field-notes","memory.md#mem-obj-file-ledger","memory.md#mem-obj-query-log","memory.md#mem-obj-access-log","memory.md#mem-obj-carried-findings","memory.md#mem-obj-codebase-brief","memory.md#mem-obj-research-results","memory.md#mem-obj-learning-lessons","memory.md#mem-obj-learning-policy","epistemic.md#epi-obj-evidence","epistemic.md#epi-obj-dispositions","epistemic.md#epi-obj-contradictions","epistemic.md#epi-obj-diagnosticity","epistemic.md#epi-obj-review-analysis","epistemic.md#epi-obj-blind-truth","memory.md#mem-rte-brief-delivery"]
              note: "Localized keys, enums, links, counts, verdicts, scores and selection metadata have deterministic consumers; numerical scores are not distributed parameters."
          records: ["memory.md#mem-obj-claims","memory.md#mem-obj-findings","memory.md#mem-obj-explanations","memory.md#mem-obj-field-notes","memory.md#mem-obj-file-ledger","memory.md#mem-obj-query-log","memory.md#mem-obj-access-log","memory.md#mem-obj-carried-findings","memory.md#mem-obj-codebase-brief","memory.md#mem-obj-research-results","memory.md#mem-obj-learning-lessons","memory.md#mem-obj-learning-policy","epistemic.md#epi-obj-evidence","epistemic.md#epi-obj-dispositions","epistemic.md#epi-obj-contradictions","epistemic.md#epi-obj-diagnosticity","epistemic.md#epi-obj-review-analysis","epistemic.md#epi-obj-blind-truth","memory.md#mem-rte-brief-delivery"]
          note: "Includes the policy envelope but not an inferred interpretation of arbitrary configuration JSON."
        -
          scope: "Policy configuration internals and affected-future-run semantics"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-learning-policy","runtime.md#rt-rte-policy-admission"]
          note: "JSON serialization establishes an envelope, not the internal form or actual future interpretation of configuration values. No parametric or instruction classification follows."
        -
          scope: "Additional registered memory, maintenance, evaluation and driver alternatives"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-policy-admission","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-tool-dispatch"]
          note: "Included composition, review/design-session, impact/revalidation/refresh, evaluation/envelope, adapter recovery and development/historical-driver alternatives are not fully traced by accepted records. Their operative payloads, admission and later consumers cannot be completely classified."
      records: ["memory.md#mem-obj-claims","memory.md#mem-obj-findings","memory.md#mem-obj-explanations","memory.md#mem-obj-field-notes","memory.md#mem-obj-prose-artifacts","memory.md#mem-obj-query-log","memory.md#mem-obj-carried-findings","memory.md#mem-obj-research-results","epistemic.md#epi-obj-evidence","epistemic.md#epi-obj-dispositions","epistemic.md#epi-obj-contradictions","epistemic.md#epi-obj-diagnosticity","epistemic.md#epi-obj-review-analysis","memory.md#mem-obj-file-ledger","memory.md#mem-obj-access-log","memory.md#mem-obj-codebase-brief","memory.md#mem-obj-learning-lessons","memory.md#mem-obj-learning-policy","epistemic.md#epi-obj-blind-truth","memory.md#mem-rte-brief-delivery","runtime.md#rt-rte-policy-admission","runtime.md#rt-rte-tool-dispatch"]
      note: "Natural-language and symbolic operative parts coexist. Opaque configuration semantics and additional included payloads prevent complete form coverage."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Survey statements, findings, explanations, notes, prose and caller lesson propositions"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records: ["memory.md#mem-obj-claims","memory.md#mem-obj-findings","memory.md#mem-obj-explanations","memory.md#mem-obj-field-notes","memory.md#mem-obj-prose-artifacts","memory.md#mem-obj-learning-lessons"]
              note: "Callers supply content; model-authored survey prose is not automatically extracted from conversational logs."
          records: ["memory.md#mem-obj-claims","memory.md#mem-obj-findings","memory.md#mem-obj-explanations","memory.md#mem-obj-field-notes","memory.md#mem-obj-prose-artifacts","memory.md#mem-obj-learning-lessons"]
          note: "Authorship does not imply human admission."
        -
          scope: "Archive carry and external evidence/research ingress"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records: ["memory.md#mem-obj-carried-findings","memory.md#mem-rte-carry-recheck","epistemic.md#epi-rte-evidence-record","memory.md#mem-obj-research-results","epistemic.md#epi-rte-research-landing"]
              note: "Prior-store findings and caller source excerpts/statements enter with declared lineage; custody checks do not authenticate their truth."
          records: ["memory.md#mem-obj-carried-findings","memory.md#mem-rte-carry-recheck","epistemic.md#epi-rte-evidence-record","memory.md#mem-obj-research-results","epistemic.md#epi-rte-research-landing"]
          note: "Includes imported origins without upgrading source warrant."
        -
          scope: "Compiled task briefs, review aggregates and published views"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records: ["memory.md#mem-obj-codebase-brief","memory.md#mem-rte-brief-delivery","epistemic.md#epi-rte-review-aggregation","runtime.md#rt-rte-docs-publication"]
              note: "Deterministic compilation, aggregation and projection derive retained artifacts from existing content."
          records: ["memory.md#mem-obj-codebase-brief","memory.md#mem-rte-brief-delivery","epistemic.md#epi-rte-review-aggregation","runtime.md#rt-rte-docs-publication"]
          note: "Does not classify arbitrary generated prose as semantically novel."
        -
          scope: "Terminal-outcome extraction ledger"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records: ["memory.md#mem-obj-learning-lessons","runtime.md#rt-rte-policy-admission"]
              note: "Extraction serializes terminal session/review/design artifact states; a separately supplied proposition is not itself automatically induced."
          records: ["memory.md#mem-obj-learning-lessons","runtime.md#rt-rte-policy-admission"]
          note: "Trace-derived lineage does not establish trace learning without a later behavior-shaping consumer."
        -
          scope: "Initial file-ledger provenance/control and exact configuration derivation"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-file-ledger","memory.md#mem-obj-learning-policy"]
          note: "Known subsequent changes do not resolve initialization or internal configuration provenance."
        -
          scope: "Additional registered memory, maintenance, evaluation and driver alternatives"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-policy-admission","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-tool-dispatch"]
          note: "Included composition, review/design-session, impact/revalidation/refresh, evaluation/envelope, adapter recovery and development/historical-driver alternatives are not fully traced by accepted records. Their operative payloads, admission and later consumers cannot be completely classified."
      records: ["memory.md#mem-obj-claims","memory.md#mem-obj-findings","memory.md#mem-obj-explanations","memory.md#mem-obj-field-notes","memory.md#mem-obj-prose-artifacts","memory.md#mem-obj-learning-lessons","memory.md#mem-obj-carried-findings","memory.md#mem-rte-carry-recheck","epistemic.md#epi-rte-evidence-record","memory.md#mem-obj-research-results","epistemic.md#epi-rte-research-landing","memory.md#mem-obj-codebase-brief","memory.md#mem-rte-brief-delivery","epistemic.md#epi-rte-review-aggregation","runtime.md#rt-rte-docs-publication","runtime.md#rt-rte-policy-admission","memory.md#mem-obj-file-ledger","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-tool-dispatch"]
      note: "Authored, imported, compiled and terminal-trace-derived paths are supported independently. Initial metadata and opaque configuration provenance remain unresolved."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retained accounts, evidence and context at later model/human readers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records: ["memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","memory.md#mem-rte-carry-recheck","runtime.md#rt-rte-locus-read","memory.md#mem-rte-brief-delivery","runtime.md#rt-rte-docs-publication","epistemic.md#epi-rte-evidence-record"]
              note: "Stored statements, explanations, archive obligations, briefs and projected prose supply context/reference. Delivery does not establish compliance or truth."
          records: ["memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","memory.md#mem-rte-carry-recheck","runtime.md#rt-rte-locus-read","memory.md#mem-rte-brief-delivery","runtime.md#rt-rte-docs-publication","epistemic.md#epi-rte-evidence-record"]
          note: "Actual read/query/projection routes exist; model effects remain unobserved."
        -
          scope: "Changing recorded standing at the answering host"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records: ["memory.md#mem-bap-recorded-standing"]
              note: "Notes-mode guidance asks the later host to state recorded limits before positive content; the changing standing is interpreted as answer guidance."
          records: ["memory.md#mem-bap-recorded-standing"]
          note: "This is not the static MCP opening or shipped phase instructions, which are excluded from accumulated memory."
        -
          scope: "Retained evidence, slot state, verdicts and custody at deterministic gates"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records: ["epistemic.md#epi-rte-claim-admission","epistemic.md#epi-rte-claim-challenge","epistemic.md#epi-rte-finding-resolution","epistemic.md#epi-rte-explanation-record","epistemic.md#epi-rte-explanation-selection","epistemic.md#epi-rte-review-aggregation","runtime.md#rt-rte-policy-admission"]
              note: "Existing evidence roles/links, slot dispositions, pass judgments and policy predecessor/configuration records determine candidate conformity."
            -
              value: "enforcement"
              basis: "wired"
              records: ["epistemic.md#epi-rte-claim-admission","epistemic.md#epi-rte-claim-challenge","epistemic.md#epi-rte-finding-resolution","epistemic.md#epi-rte-explanation-selection","epistemic.md#epi-rte-review-aggregation","runtime.md#rt-rte-policy-admission"]
              note: "The corresponding checks refuse writes, ordinary progression, deficient landing or activation; these vetoes are local, with deferred/alternate-path limits."
          records: ["epistemic.md#epi-rte-claim-admission","epistemic.md#epi-rte-claim-challenge","epistemic.md#epi-rte-finding-resolution","epistemic.md#epi-rte-explanation-record","epistemic.md#epi-rte-explanation-selection","epistemic.md#epi-rte-review-aggregation","runtime.md#rt-rte-policy-admission"]
          note: "Same retained criteria can validate and enforce; no universal semantic-correctness gate is inferred."
        -
          scope: "Retained content/features at priority selectors"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records: ["memory.md#mem-obj-access-log","memory.md#mem-obj-file-ledger","memory.md#mem-obj-query-log","memory.md#mem-rte-brief-delivery"]
              note: "Heat orders stale work, demand supplies field priorities, and candidate text scored against task terms orders optional brief content."
          records: ["memory.md#mem-obj-access-log","memory.md#mem-obj-file-ledger","memory.md#mem-obj-query-log","memory.md#mem-rte-brief-delivery"]
          note: "Fixed scoring still gives retained features ranking force; adaptive compression is not established."
        -
          scope: "Retained validity, scope, disposition and task-mode metadata at selection code"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records: ["memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","memory.md#mem-rte-brief-delivery","epistemic.md#epi-rte-contradiction-resolution","epistemic.md#epi-rte-staleness-clear"]
              note: "Validity and disposition choose visible records, stale flags select backlog membership, and task/lens metadata choose context sections."
          records: ["memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","memory.md#mem-rte-brief-delivery","epistemic.md#epi-rte-contradiction-resolution","epistemic.md#epi-rte-staleness-clear"]
          note: "Selection force is separate from interpreting the selected prose."
        -
          scope: "Outcome/lesson inputs at a future behavior-shaping update and active configuration at future host"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-learning-lessons","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-policy-admission"]
          note: "Qualification and active readback are wired, but supplied records do not establish which future host consumes configuration or how it changes behavior; learning authority and configuration's downstream force remain unresolved."
        -
          scope: "Additional registered memory, maintenance, evaluation and driver alternatives"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-policy-admission","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-tool-dispatch"]
          note: "Included composition, review/design-session, impact/revalidation/refresh, evaluation/envelope, adapter recovery and development/historical-driver alternatives are not fully traced by accepted records. Their operative payloads, admission and later consumers cannot be completely classified."
      records: ["memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","memory.md#mem-rte-carry-recheck","runtime.md#rt-rte-locus-read","memory.md#mem-rte-brief-delivery","runtime.md#rt-rte-docs-publication","epistemic.md#epi-rte-evidence-record","memory.md#mem-bap-recorded-standing","epistemic.md#epi-rte-claim-admission","epistemic.md#epi-rte-claim-challenge","epistemic.md#epi-rte-finding-resolution","epistemic.md#epi-rte-explanation-record","epistemic.md#epi-rte-explanation-selection","epistemic.md#epi-rte-review-aggregation","runtime.md#rt-rte-policy-admission","memory.md#mem-obj-access-log","memory.md#mem-obj-file-ledger","memory.md#mem-obj-query-log","epistemic.md#epi-rte-contradiction-resolution","epistemic.md#epi-rte-staleness-clear","memory.md#mem-obj-learning-lessons","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-tool-dispatch"]
      note: "Knowledge, afforded standing guidance, validation/enforcement, ranking and routing have local consumers. Opaque downstream policy and other included consumers prevent complete authority coverage."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Ordinary model-directed survey admission and software-controlled transformations"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "afforded"
              records: ["runtime.md#rt-rte-survey-cycle","memory.md#mem-obj-prose-artifacts"]
              note: "The shipped workflow assigns content writing to the coordinator/phase agents without per-content human approval."
            -
              value: "automatic"
              basis: "wired"
              records: ["memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","memory.md#mem-rte-brief-delivery","epistemic.md#epi-rte-review-aggregation","runtime.md#rt-rte-docs-publication"]
              note: "Software gates typed writes and automatically compiles, aggregates and projects content once invoked; initiating a request is not approval of each retained item."
          records: ["runtime.md#rt-rte-survey-cycle","memory.md#mem-obj-prose-artifacts","memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","memory.md#mem-rte-brief-delivery","epistemic.md#epi-rte-review-aggregation","runtime.md#rt-rte-docs-publication"]
          note: "Distinct afforded model authorship and wired admission/compilation evidence are retained."
        -
          scope: "Initial ledger, generic caller contributions, decision actors and preference confirmations"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-file-ledger","memory.md#mem-obj-query-log","runtime.md#rt-rte-decision-admission","runtime.md#rt-rte-policy-admission"]
          note: "Caller identity, direct-user labels and confirmation fields do not authenticate an explicit human per-content decision. Manual admission is not established; model-driven witnessed paths do not resolve every alternative."
        -
          scope: "Additional registered memory, maintenance, evaluation and driver alternatives"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-policy-admission","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-tool-dispatch"]
          note: "Included composition, review/design-session, impact/revalidation/refresh, evaluation/envelope, adapter recovery and development/historical-driver alternatives are not fully traced by accepted records. Their operative payloads, admission and later consumers cannot be completely classified."
      records: ["runtime.md#rt-rte-survey-cycle","memory.md#mem-obj-prose-artifacts","memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","memory.md#mem-rte-brief-delivery","epistemic.md#epi-rte-review-aggregation","runtime.md#rt-rte-docs-publication","memory.md#mem-obj-file-ledger","memory.md#mem-obj-query-log","runtime.md#rt-rte-decision-admission","runtime.md#rt-rte-policy-admission","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-tool-dispatch"]
      note: "Automatic admission is supported for named mechanisms. No manual finding is inferred from actor labels or workflow initiation; unresolved caller/initialization alternatives remain included."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Claim/finding/disposition/explanation revision and historical withdrawal"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records: ["memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","epistemic.md#epi-rte-concern-disposition","epistemic.md#epi-rte-finding-resolution"]
              note: "Successor statements, new effective explanation bodies and revised concern/finding states change retained entries."
            -
              value: "invalidate"
              basis: "wired"
              records: ["epistemic.md#epi-rte-claim-withdrawal","memory.md#mem-rte-explanation-cycle","runtime.md#rt-rte-decision-admission"]
              note: "Claim interval closure, explanation withdrawal and decision invalidation withdraw current reliance while retaining corresponding history."
          records: ["memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","epistemic.md#epi-rte-concern-disposition","epistemic.md#epi-rte-finding-resolution","epistemic.md#epi-rte-claim-withdrawal","runtime.md#rt-rte-decision-admission"]
          note: "Reset also deletes other records; it is not uniformly history-preserving invalidation."
        -
          scope: "Persisted brief compilation and role-review reduction"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records: ["memory.md#mem-rte-brief-delivery","epistemic.md#epi-rte-review-aggregation"]
              note: "Brief selection reduces retained candidates to bounded context; role fan-in combines judgments into retained finding keys without a new semantic conjecture."
          records: ["memory.md#mem-rte-brief-delivery","epistemic.md#epi-rte-review-aggregation"]
          note: "Selection/combination over retained content qualifies; primary-key refusal and hash rebuild alone do not."
        -
          scope: "Qualified candidate to active policy and draft to accepted decision"
          assessment: "known"
          findings:
            -
              value: "promote"
              basis: "wired"
              records: ["runtime.md#rt-rte-policy-admission","runtime.md#rt-rte-decision-admission"]
              note: "Successful qualification/activation or acceptance raises a retained candidate into the active/current authority tier."
          records: ["runtime.md#rt-rte-policy-admission","runtime.md#rt-rte-decision-admission"]
          note: "Recorded promotion is not observed deployment or beneficial behavior change."
        -
          scope: "Semantic novelty of model account revisions"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-explanations","epistemic.md#epi-rte-explanation-record"]
          note: "No populated body and checked inputs establish whether a new proposition is synthesized rather than reshaped or restated; a generation request cannot establish synthesis."
        -
          scope: "Additional registered memory, maintenance, evaluation and driver alternatives"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-policy-admission","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-tool-dispatch"]
          note: "Included composition, review/design-session, impact/revalidation/refresh, evaluation/envelope, adapter recovery and development/historical-driver alternatives are not fully traced by accepted records. Their operative payloads, admission and later consumers cannot be completely classified."
      records: ["memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","epistemic.md#epi-rte-concern-disposition","epistemic.md#epi-rte-finding-resolution","epistemic.md#epi-rte-claim-withdrawal","runtime.md#rt-rte-decision-admission","memory.md#mem-rte-brief-delivery","epistemic.md#epi-rte-review-aggregation","runtime.md#rt-rte-policy-admission","memory.md#mem-obj-explanations","epistemic.md#epi-rte-explanation-record","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-tool-dispatch"]
      note: "Evolution, withdrawal, consolidation and authority-tier promotion are supported. No deduplication, decay or synthesis is inferred from route names, hashes, retrieval omissions or model generation alone."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested locus/raw/history/carry/research/brief lookup and projected-view consumption"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records: ["runtime.md#rt-rte-locus-read","memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","memory.md#mem-rte-carry-recheck","memory.md#mem-rte-research-consumption","memory.md#mem-rte-brief-delivery","runtime.md#rt-rte-docs-publication"]
              note: "A later caller requests prior content; deterministic selection and delivery fulfill the request rather than adding a second push."
          records: ["runtime.md#rt-rte-locus-read","memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","memory.md#mem-rte-carry-recheck","memory.md#mem-rte-research-consumption","memory.md#mem-rte-brief-delivery","runtime.md#rt-rte-docs-publication"]
          note: "Warm-start/dashboard requests follow the same requested-consumption distinction."
        -
          scope: "Stored brief to design-planning lens context and frozen dispatch payload"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records: ["memory.md#mem-rte-brief-delivery"]
              note: "Design planning automatically reads the stored brief, selects lens-specific sections, persists packets and delivers selected task context through dispatch; the lens consumer need not request those individual retained parts."
          records: ["memory.md#mem-rte-brief-delivery"]
          note: "This identifies the automatic context-supply operation within a larger requested design workflow, not a blanket claim of unsolicited host injection."
        -
          scope: "Active policy beyond verification reader and additional driver/packet consumers"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-learning-policy","runtime.md#rt-rte-policy-admission","runtime.md#rt-rte-tool-dispatch"]
          note: "Internal active readback is established; automatic future-host delivery and complete alternate consumer chains are not."
        -
          scope: "Additional registered memory, maintenance, evaluation and driver alternatives"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-policy-admission","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-tool-dispatch"]
          note: "Included composition, review/design-session, impact/revalidation/refresh, evaluation/envelope, adapter recovery and development/historical-driver alternatives are not fully traced by accepted records. Their operative payloads, admission and later consumers cannot be completely classified."
      records: ["runtime.md#rt-rte-locus-read","memory.md#mem-rte-knowledge-revision","memory.md#mem-rte-explanation-cycle","memory.md#mem-rte-carry-recheck","memory.md#mem-rte-research-consumption","memory.md#mem-rte-brief-delivery","runtime.md#rt-rte-docs-publication","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-policy-admission","runtime.md#rt-rte-tool-dispatch"]
      note: "Requested memory readers and automatic task-packet supply coexist at different operations. Other registered and policy consumers prevent complete direction coverage."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Task-targeted retained candidates compiled for automatic design context"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records: ["memory.md#mem-rte-brief-delivery","memory.md#mem-obj-codebase-brief"]
              note: "Trigger is task-context preparation/design planning; explicit registry IDs force matching retained candidates into the brief later consumed in lens packets."
            -
              value: "inferred-lexical"
              basis: "wired"
              records: ["memory.md#mem-rte-brief-delivery","memory.md#mem-obj-codebase-brief"]
              note: "Tokenized lexical query or objective scores retained candidate text; positive scores and stable ties select optional brief content for later task context."
            -
              value: "coarse"
              basis: "wired"
              records: ["memory.md#mem-rte-brief-delivery"]
              note: "Required objective/constraints, item limit and lens section filters constrain which compiled retained parts reach the design packet; these filters are separate from targeted ID and lexical matching."
          records: ["memory.md#mem-rte-brief-delivery","memory.md#mem-obj-codebase-brief"]
          note: "Forced IDs bypass optional mode filtering; a generic task/request identifier alone would not justify identifier-based push."
        -
          scope: "Policy and other included packet-supply selectors"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-learning-policy","runtime.md#rt-rte-policy-admission","runtime.md#rt-rte-tool-dispatch"]
          note: "No complete account of alternative push operations or their selected payloads is recorded; embedding or judgment selection cannot be inferred."
      records: ["memory.md#mem-rte-brief-delivery","memory.md#mem-obj-codebase-brief","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-policy-admission","runtime.md#rt-rte-tool-dispatch"]
      note: "Known task-packet selection retains trigger/input/selected-part distinctions. Pull-only readers do not acquire push signals from having a deterministic handler; unresolved alternatives prevent inapplicability or complete coverage."
    trace_learning:
      assessment: "not-determinable"
      units:
        -
          scope: "Terminal outcome extraction, caller-authored lessons and active configuration"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-learning-lessons","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-policy-admission"]
          note: "Automatic extraction and durable qualified configuration are established, but trace-informed authored proposals and internal representation readback do not establish a later behavior-shaping consumer of the changed content. No qualifying yes or bounded no can be concluded."
        -
          scope: "Query/access usage, adversarial notes and retained review outputs"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-query-log","memory.md#mem-obj-access-log","epistemic.md#epi-rte-review-aggregation","epistemic.md#epi-rte-review-scoring","workflow.md#wf-rte-adversarial-review"]
          note: "Usage affects priority and review outputs feed scoring; the accepted records do not close an automatic trace-to-durable-behavior-shaping-artifact chain. Prescribed packaging revision is not evidence of automatic trace induction, and no bounded absence record supports no."
        -
          scope: "Additional registered memory, maintenance, evaluation and driver alternatives"
          assessment: "uninspected"
          findings: []
          records: ["runtime.md#rt-rte-policy-admission","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-tool-dispatch"]
          note: "Included composition, review/design-session, impact/revalidation/refresh, evaluation/envelope, adapter recovery and development/historical-driver alternatives are not fully traced by accepted records. Their operative payloads, admission and later consumers cannot be completely classified."
      records: ["memory.md#mem-obj-learning-lessons","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-policy-admission","memory.md#mem-obj-query-log","memory.md#mem-obj-access-log","epistemic.md#epi-rte-review-aggregation","epistemic.md#epi-rte-review-scoring","workflow.md#wf-rte-adversarial-review","runtime.md#rt-rte-tool-dispatch"]
      note: "No accepted evidenced-absence record supports a local no; no recorded route fully establishes automatic trace-fed production plus a qualifying later consumer. This is unresolved learning inventory, not absence of learning or a negative system union."
    trace_source:
      assessment: "not-determinable"
      units:
        -
          scope: "Potential outcome-to-policy route"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-learning-lessons","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-policy-admission"]
          note: "Terminal agent/review/design state and allowed query-log provenance are described, but original trace content and qualifying downstream update consumption are not fully established. A session label alone cannot classify conversational session-logs, tool-traces or trajectories."
        -
          scope: "Other included usage/review/evaluation-fed alternatives"
          assessment: "uninspected"
          findings: []
          records: ["memory.md#mem-obj-query-log","memory.md#mem-obj-access-log","epistemic.md#epi-rte-review-aggregation","epistemic.md#epi-rte-review-scoring","runtime.md#rt-rte-tool-dispatch"]
          note: "No fully qualified trace-learning route or complete original-input account is established for these alternatives; symbolic events or wrapper labels alone do not justify event-streams."
      records: ["memory.md#mem-obj-learning-lessons","memory.md#mem-obj-learning-policy","runtime.md#rt-rte-policy-admission","memory.md#mem-obj-query-log","memory.md#mem-obj-access-log","epistemic.md#epi-rte-review-aggregation","epistemic.md#epi-rte-review-scoring","runtime.md#rt-rte-tool-dispatch"]
      note: "No source value is assigned without a qualifying trace-fed durable update. Unresolved learning inventory prevents treating trace source as inapplicable."
---

# Amanuensis memory profile

## Comparison rationale

This profile classifies accepted records, not a new source inspection. All positive implementation findings remain wired; model-facing survey and standing guidance retain afforded status. No finding is upgraded to observed operation or causal benefit.

### Boundary and canonical identities

The retained unit is the conspectus and its later-consumer routes, not the whole host's storage. Static phase references and MCP opening guidance are excluded from accumulated memory; the changing standing delivered to an answering host remains included through [MEM-BAP-recorded-standing](memory.md#mem-bap-recorded-standing). External provider opacity does not add model-weights or parametric memory values. [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) bounds host orchestration, persistence and resume; [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch) bounds the service rather than every alternate file writer.

Reconciliation supersedes the epistemic claims, findings, explanations, research-results and stale-ledger objects with the corresponding memory declarations. All classifications therefore cite [MEM-OBJ-claims](memory.md#mem-obj-claims), [MEM-OBJ-findings](memory.md#mem-obj-findings), [MEM-OBJ-explanations](memory.md#mem-obj-explanations), [MEM-OBJ-research-results](memory.md#mem-obj-research-results) and [MEM-OBJ-file-ledger](memory.md#mem-obj-file-ledger), not their superseded duplicates. The narrower epistemic routes remain canonical and usable; no route is replaced merely because it overlaps a broader memory lifecycle. These supersessions affect citation identity, not controlled values or evidence strength.

### Content, metadata and force

Natural-language statements and explanations are split from symbolic keys, intervals and dispositions. Both are retained in SQLite, but consumers differ: a model interprets content as knowledge; fixed gates use evidence links and slot state as validation criteria and enforce refusals. [EPI-RTE-explanation-selection](epistemic.md#epi-rte-explanation-selection) illustrates why a retained positive body need not retain current authority after a decline or withdrawal. The status-admission exception in [RT-RTE-survey-cycle](runtime.md#rt-rte-survey-cycle) prevents turning these local gates into universal completion enforcement.

Ranking includes retained candidate text, demand and heat even though fixed code supplies scoring. [MEM-RTE-brief-delivery](memory.md#mem-rte-brief-delivery) supplies lexical ranking and forced identity matches; [MEM-OBJ-query-log](memory.md#mem-obj-query-log) supplies a demand-priority view, not demonstrated adaptive compression. Standing, validity and mode fields also route which work or content is selected. Arbitrary policy JSON has known SQLite storage and a symbolic envelope, but its internal semantics and later host effect remain unresolved in [MEM-OBJ-learning-policy](memory.md#mem-obj-learning-policy).

Software admission without per-content human approval is automatic even when a person starts a survey. Explicit confirmation fields, actor labels and direct-user provenance do not authenticate manual control. [RT-RTE-decision-admission](runtime.md#rt-rte-decision-admission) and [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) preserve that distinction. Initial ledger control remains unresolved rather than inherited from known subsequent writers.

### Transformation and later delivery

Whole-body explanation replacement and claim successors support evolution; interval closure and withdrawal support invalidation. Persisted brief selection and role aggregation reduce retained material and support consolidation. Acceptance/activation promotes a draft or qualified candidate into current authority, without implying deployment or correctness. [EPI-RTE-review-aggregation](epistemic.md#epi-rte-review-aggregation) derives retained keys from judgments, not new source truth. No synthesis value follows from a model being asked to explain code; [EPI-RTE-explanation-record](epistemic.md#epi-rte-explanation-record) leaves actual body entailment unresolved. Hash checks and primary-key uniqueness do not establish deduplication.

Requested locus/raw/brief lookup is pull. The automatic provision of stored task context to a design lens is the push operation inside the wider requested workflow: compilation selects retained candidates, planning narrows sections, and dispatch delivers the frozen packet. The signal units name actual selection inputs rather than treating any request ID as an identity-based selector. Forced registry matches, optional lexical matching and coarse lens/item filtering remain distinct. [MEM-RTE-brief-delivery](memory.md#mem-rte-brief-delivery) records both this chain and its forced-before-mode-filter caveat. [RT-RTE-locus-read](runtime.md#rt-rte-locus-read) instead fulfills a retained-content request; its byte budgeting alone does not make that route push.

Generated views add file-backed later consumption; they do not replace durable SQLite/prose authority. [RT-RTE-docs-publication](runtime.md#rt-rte-docs-publication) retains normal, clean, verification-disabled and standalone paths. Projection checking does not certify codebase knowledge, and a successful clean promotion need not include readback when verification is disabled.

### Learning uncertainty and inventory coverage

Trace-derived lineage is not equivalent to trace learning. [MEM-OBJ-learning-lessons](memory.md#mem-obj-learning-lessons) records automatic terminal-artifact extraction beside separately authored propositions/configuration. [RT-RTE-policy-admission](runtime.md#rt-rte-policy-admission) establishes qualification, durable active representation and internal reader comparison. [MEM-OBJ-learning-policy](memory.md#mem-obj-learning-policy) leaves future host interpretation unresolved; the active serializer omits the proposition and evidence ledger. These facts do not close a qualifying later behavior-shaping route, but neither establish its absence.

Usage traces and adversarial/review history are likewise not automatically qualifying learned artifacts. [MEM-OBJ-access-log](memory.md#mem-obj-access-log) and [MEM-OBJ-query-log](memory.md#mem-obj-query-log) establish priority inputs; [WF-RTE-adversarial-review](workflow.md#wf-rte-adversarial-review) establishes retained criticism and prescribed packaging use, not automatic induction from conversational traces. No accepted evidenced-absence record licenses a local trace-learning no. Consequently trace learning and trace source remain unresolved with no union value, rather than negative or inapplicable. Session identifiers alone cannot distinguish conversational logs, tool traces, event streams and linked state/action/outcome trajectories.

The unresolved inventory includes the additional registered maintenance, evaluation, adapter and driver chains retained in the analysts' limitations, not merely active policy. Their missing payload, control and downstream-consumer facts prevent complete-value conclusions even where a strong local witness exists. The policy and dispatcher records anchor these limits; inspected disposition, contradiction, diagnosticity and sealed-review mechanisms are included through the epistemic records, not discarded because memory's earlier inspection was narrower. No overall absence, improvement or complete enumeration is inferred.

### Source-read log

None. This classification used only the supplied accepted members and reconciliation; no named record ambiguity required a frozen-source read.
