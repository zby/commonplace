---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'ai-modules memory comparison: accumulated wiki knowledge, work contracts, checking policy
  and retained evaluation/history state at the frozen commit.'
run-id: AAS-2026-10-14-ai-modules-a7044d5627d2-01
source-identity: https://github.com/TheAFH/ai-modules
reviewed-boundary: 0cf0227c416f75a79d7317f603a209a63e7a3c8f
memory-comparison:
  version: 2
  scope: Accumulated raw captures and metadata (including unresolved image assets), wiki declarative/procedural
    pages, locally customized schema and lint policies, index/action/audit metadata, live/archive task
    contracts and completion state, later-invocation relay evidence, incremental changelog, retained evaluator/benchmark
    artifacts, and unresolved remaining shipped-family retained-output consumers. Excludes static shipped
    skill/role/registration/deployment content, unchanged standing instructions, ordinary immediate call
    state, standalone summary outputs without a retained reload contract, and host inference/provider
    state with no established accumulated-memory write route.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Raw bodies and origin/digest parts; wiki page bodies/frontmatter; local schema; catalog
          and action log; task body/status; relay snapshots/returns; changelog
        assessment: known
        findings:
        - value: files
          basis: claimed
          records:
          - memory.md#mem-obj-raw-body
          - memory.md#mem-obj-raw-frontmatter
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-schema-guidance
          - memory.md#mem-obj-index
          - memory.md#mem-obj-wiki-log
          - memory.md#mem-obj-task-files
          - epistemic.md#epi-obj-audit-verdict
          - runtime.md#rt-obj-relay-files
          - runtime.md#rt-rte-readiness-repair
          - memory.md#mem-rte-changelog-update
          note: Accepted instruction-level accounts name Markdown or relay text persistence. Optional
            Git practice does not establish a required repository-backed admission route.
        - value: repo
          basis: afforded
          records:
          - memory.md#mem-obj-raw-body
          - memory.md#mem-obj-raw-frontmatter
          - memory.md#mem-obj-task-files
          - epistemic.md#epi-obj-audit-verdict
          note: Raw history may use project Git; tracked task renames preserve Git history. Repository
            storage is available, not mandatory or observed.
        records:
        - memory.md#mem-obj-raw-body
        - memory.md#mem-obj-raw-frontmatter
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-schema-guidance
        - memory.md#mem-obj-index
        - memory.md#mem-obj-wiki-log
        - memory.md#mem-obj-task-files
        - epistemic.md#epi-obj-audit-verdict
        - runtime.md#rt-obj-relay-files
        - runtime.md#rt-rte-readiness-repair
        - memory.md#mem-rte-changelog-update
        note: These named retained objects are filesystem files; this does not characterize accompanying
          image assets or every local instance history.
      - scope: Retained lint policy declarations and evaluator benchmark artifacts
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-lint-acceptance
          - epistemic.md#epi-obj-lint-settings
          - epistemic.md#epi-rte-lint-acknowledge
          - epistemic.md#epi-obj-test-report
          - epistemic.md#epi-rte-benchmark-rollup
          - runtime.md#rt-rte-evaluator-worker
          note: Fixed lint parser and benchmark consumer read retained Markdown/JSON artifacts.
        records:
        - memory.md#mem-obj-lint-acceptance
        - epistemic.md#epi-obj-lint-settings
        - epistemic.md#epi-rte-lint-acknowledge
        - epistemic.md#epi-obj-test-report
        - epistemic.md#epi-rte-benchmark-rollup
        - runtime.md#rt-rte-evaluator-worker
        note: Inspected code reads schema policy and filesystem benchmark inputs; temporary Python values
          are not an additional retained-memory substrate.
      - scope: Accompanying raw image assets
        assessment: uninspected
        findings: []
        records: &id003
        - memory.md#mem-obj-raw-body
        - memory.md#mem-obj-raw-frontmatter
        note: Raw body record explicitly leaves image assets uncharacterized; their operative retained
          object/substrate inventory is unresolved.
      - scope: Remaining shipped-family retained outputs and their later consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-helper-dispatch
        - memory.md#mem-clm-summary-transfer
        - runtime.md#rt-rte-task-implement
        note: Detailed output-consumer routes of remaining instruction-writing, portability, git, formatting
          and editorial families were not established by accepted records. Standalone summary delivery
          alone supplies no save/reload chain. This prevents exhaustive classification, not the positive
          local findings.
      records:
      - memory.md#mem-obj-raw-body
      - memory.md#mem-obj-raw-frontmatter
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-schema-guidance
      - memory.md#mem-obj-index
      - memory.md#mem-obj-wiki-log
      - memory.md#mem-obj-task-files
      - epistemic.md#epi-obj-audit-verdict
      - runtime.md#rt-obj-relay-files
      - runtime.md#rt-rte-readiness-repair
      - memory.md#mem-rte-changelog-update
      - memory.md#mem-obj-lint-acceptance
      - epistemic.md#epi-obj-lint-settings
      - epistemic.md#epi-rte-lint-acknowledge
      - epistemic.md#epi-obj-test-report
      - epistemic.md#epi-rte-benchmark-rollup
      - runtime.md#rt-rte-evaluator-worker
      - runtime.md#rt-rte-helper-dispatch
      - memory.md#mem-clm-summary-transfer
      - runtime.md#rt-rte-task-implement
      note: The named file objects are covered. Assets and remaining retained-output families prevent
        an exhaustive inventory. External inference service/weights and static deployment stores are not
        substituted for accumulated memory.
    representational_form:
      assessment: partial
      units:
      - scope: Raw text, wiki declarative/procedure bodies, schema prose, catalog summaries, action summaries,
          task contracts, helper judgments and changelog summaries
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records:
          - memory.md#mem-obj-raw-body
          - memory.md#mem-obj-raw-frontmatter
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-schema-guidance
          - memory.md#mem-obj-index
          - memory.md#mem-obj-wiki-log
          - memory.md#mem-obj-task-files
          - epistemic.md#epi-obj-audit-verdict
          - runtime.md#rt-obj-relay-files
          - runtime.md#rt-rte-readiness-repair
          - memory.md#mem-rte-changelog-update
          note: Later readers interpret claims, guidance, summaries and criticism as language.
        records:
        - memory.md#mem-obj-raw-body
        - memory.md#mem-obj-raw-frontmatter
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-schema-guidance
        - memory.md#mem-obj-index
        - memory.md#mem-obj-wiki-log
        - memory.md#mem-obj-task-files
        - epistemic.md#epi-obj-audit-verdict
        - runtime.md#rt-obj-relay-files
        - runtime.md#rt-rte-readiness-repair
        - memory.md#mem-rte-changelog-update
        note: Classification is at human/model text consumers, not at Markdown serialization.
      - scope: Origin/digest fields; page type/tag fields; schema enums; acceptance/exclusion/boilerplate
          policies; task lifecycle strings and relay byte/diff anchors
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-raw-body
          - memory.md#mem-obj-raw-frontmatter
          - memory.md#mem-obj-schema-guidance
          - memory.md#mem-obj-lint-acceptance
          - epistemic.md#epi-obj-lint-settings
          - epistemic.md#epi-rte-lint-acknowledge
          note: Hash and lint implementations consume digest, enum and policy keys with fixed rules.
        - value: symbolic
          basis: claimed
          records:
          - memory.md#mem-obj-task-files
          - epistemic.md#epi-obj-audit-verdict
          - runtime.md#rt-obj-relay-files
          - runtime.md#rt-rte-readiness-repair
          note: Task workflow predicates and exact baseline/anchor comparisons are prescribed, not observed.
        records:
        - memory.md#mem-obj-raw-body
        - memory.md#mem-obj-raw-frontmatter
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-schema-guidance
        - memory.md#mem-obj-lint-acceptance
        - epistemic.md#epi-obj-lint-settings
        - epistemic.md#epi-rte-lint-acknowledge
        - memory.md#mem-obj-task-files
        - epistemic.md#epi-obj-audit-verdict
        - runtime.md#rt-obj-relay-files
        - runtime.md#rt-rte-readiness-repair
        note: These parts have localized comparison/checking roles separate from surrounding prose.
      - scope: Audit baseline/path metadata at model working-set consumer
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id001
          - memory.md#mem-obj-index
          - memory.md#mem-obj-wiki-log
          note: The record explicitly places workload-selection interpretation at the maintenance model.
        records: *id001
        note: A Git SHA/path list is interpreted by the maintenance model to choose tools; no fixed cache-validity
          engine is established.
      - scope: Retained evaluation report assertions versus parsed benchmark fields
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records:
          - epistemic.md#epi-obj-test-report
          note: Worker report assertions are textual claims.
        - value: symbolic
          basis: wired
          records: &id002
          - epistemic.md#epi-obj-test-report
          - epistemic.md#epi-rte-benchmark-rollup
          - runtime.md#rt-rte-evaluator-worker
          note: Fixed grading/aggregation consumes fields, booleans and statistics.
        records: *id002
        note: 'Split by consumption: human-readable claims and fixed statistical/predicate fields.'
      - scope: Accompanying images
        assessment: uninspected
        findings: []
        records: *id003
        note: No consumption-form assessment of assets is recorded.
      - scope: Remaining shipped-family retained outputs and their later consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-helper-dispatch
        - memory.md#mem-clm-summary-transfer
        - runtime.md#rt-rte-task-implement
        note: Detailed output-consumer routes of remaining instruction-writing, portability, git, formatting
          and editorial families were not established by accepted records. Standalone summary delivery
          alone supplies no save/reload chain. This prevents exhaustive classification, not the positive
          local findings.
      records:
      - memory.md#mem-obj-raw-body
      - memory.md#mem-obj-raw-frontmatter
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-schema-guidance
      - memory.md#mem-obj-index
      - memory.md#mem-obj-wiki-log
      - memory.md#mem-obj-task-files
      - epistemic.md#epi-obj-audit-verdict
      - runtime.md#rt-obj-relay-files
      - runtime.md#rt-rte-readiness-repair
      - memory.md#mem-rte-changelog-update
      - memory.md#mem-obj-lint-acceptance
      - epistemic.md#epi-obj-lint-settings
      - epistemic.md#epi-rte-lint-acknowledge
      - epistemic.md#epi-obj-test-report
      - epistemic.md#epi-rte-benchmark-rollup
      - runtime.md#rt-rte-evaluator-worker
      - runtime.md#rt-rte-helper-dispatch
      - memory.md#mem-clm-summary-transfer
      - runtime.md#rt-rte-task-implement
      note: Text and symbolic paths coexist. No retained parametric-memory update follows from opaque
        host inference or the SPR priming claim.
    lineage:
      assessment: partial
      units:
      - scope: Externally captured raw text and copied local schema template
        assessment: known
        findings:
        - value: imported
          basis: claimed
          records:
          - memory.md#mem-obj-raw-body
          - memory.md#mem-obj-raw-frontmatter
          - memory.md#mem-obj-schema-guidance
          note: Source capture imports supplied/published material; schema initialization copies a shipped
            template.
        records:
        - memory.md#mem-obj-raw-body
        - memory.md#mem-obj-raw-frontmatter
        - memory.md#mem-obj-schema-guidance
        note: Known acquisition paths, not a claim of faithful conversion or complete authorship provenance.
      - scope: Current wiki pages and procedures from direct authoring, sources, session extraction and
          query composition
        assessment: partial
        findings:
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-obj-wiki-pages
          - runtime.md#rt-rte-wiki-consume
          - epistemic.md#epi-rte-wiki-retain
          note: Model/direct authoring and cross-page composition produce page text.
        - value: trace-extracted
          basis: claimed
          records:
          - runtime.md#rt-rte-wiki-triage
          - memory.md#mem-rte-procedure-capture
          - memory.md#mem-bap-procedure-guidance
          note: Visible-session mining extracts durable claims; operational-pattern capture can strip
            instances into procedure guidance.
        records:
        - memory.md#mem-obj-wiki-pages
        - runtime.md#rt-rte-wiki-triage
        - memory.md#mem-rte-procedure-capture
        - memory.md#mem-bap-procedure-guidance
        - runtime.md#rt-rte-wiki-consume
        - epistemic.md#epi-rte-wiki-retain
        note: Supported derivation paths coexist. Initial provenance of preexisting instances is uninspected;
          composition does not establish novel claims.
      - scope: Origin/body digest computation and catalog/log derivation
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-raw-frontmatter
          note: Hash code derives digest metadata from retained body.
        - value: authored
          basis: claimed
          records: *id001
          note: Models maintain catalog summaries and action/audit records from changes and audit work.
        records:
        - memory.md#mem-obj-raw-body
        - memory.md#mem-obj-raw-frontmatter
        - memory.md#mem-obj-index
        - memory.md#mem-obj-wiki-log
        note: Known subsequent generation paths do not certify original source authorship.
      - scope: Task briefs and relay baseline/judgment parts
        assessment: partial
        findings:
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-obj-task-files
          - epistemic.md#epi-obj-audit-verdict
          - runtime.md#rt-obj-relay-files
          - runtime.md#rt-rte-readiness-repair
          note: Model-assisted task creation and helper proposals/verdicts are authored artifacts.
        - value: trace-extracted
          basis: claimed
          records: &id004
          - runtime.md#rt-obj-relay-files
          - runtime.md#rt-rte-readiness-repair
          note: Criticism/verification results feed retained task revisions for later implementation.
        - value: other-compiled
          basis: claimed
          records:
          - runtime.md#rt-obj-relay-files
          note: Byte-preserving frozen snapshots and diffs derive from task/file state.
        records:
        - memory.md#mem-obj-task-files
        - epistemic.md#epi-obj-audit-verdict
        - runtime.md#rt-obj-relay-files
        - runtime.md#rt-rte-readiness-repair
        note: Snapshots copy baselines, helper judgments are authored, and approved repairs can extract
          criticism. Initial task-instance provenance remains uninspected.
      - scope: Accepted finding declarations
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - memory.md#mem-rte-finding-acceptance
          note: Maintenance extracts persistent matching metadata from lint feedback.
        records: &id005
        - memory.md#mem-rte-finding-acceptance
        - epistemic.md#epi-rte-lint-acknowledge
        note: The declaration derives from a judged lint result, not a domain-source claim.
      - scope: Changelog summaries and evaluator artifacts
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records: &id006
          - memory.md#mem-rte-changelog-update
          note: Model summarizes committed change history.
        - value: other-compiled
          basis: wired
          records: *id002
          note: Capture and fixed grading/aggregation generate retained evaluation artifacts.
        records:
        - memory.md#mem-rte-changelog-update
        - epistemic.md#epi-obj-test-report
        - epistemic.md#epi-rte-benchmark-rollup
        - runtime.md#rt-rte-evaluator-worker
        note: Classifies prescribed changelog derivation and inspected evaluator generation, not the history
          of checked-in instances.
      - scope: Remaining shipped-family retained outputs and their later consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-helper-dispatch
        - memory.md#mem-clm-summary-transfer
        - runtime.md#rt-rte-task-implement
        note: Detailed output-consumer routes of remaining instruction-writing, portability, git, formatting
          and editorial families were not established by accepted records. Standalone summary delivery
          alone supplies no save/reload chain. This prevents exhaustive classification, not the positive
          local findings.
      records:
      - memory.md#mem-obj-raw-body
      - memory.md#mem-obj-raw-frontmatter
      - memory.md#mem-obj-schema-guidance
      - memory.md#mem-obj-wiki-pages
      - runtime.md#rt-rte-wiki-triage
      - memory.md#mem-rte-procedure-capture
      - memory.md#mem-bap-procedure-guidance
      - runtime.md#rt-rte-wiki-consume
      - epistemic.md#epi-rte-wiki-retain
      - memory.md#mem-obj-index
      - memory.md#mem-obj-wiki-log
      - memory.md#mem-obj-task-files
      - epistemic.md#epi-obj-audit-verdict
      - runtime.md#rt-obj-relay-files
      - runtime.md#rt-rte-readiness-repair
      - memory.md#mem-rte-finding-acceptance
      - epistemic.md#epi-rte-lint-acknowledge
      - memory.md#mem-rte-changelog-update
      - epistemic.md#epi-obj-test-report
      - epistemic.md#epi-rte-benchmark-rollup
      - runtime.md#rt-rte-evaluator-worker
      - runtime.md#rt-rte-helper-dispatch
      - memory.md#mem-clm-summary-transfer
      - runtime.md#rt-rte-task-implement
      note: Known derivation routes do not resolve preexisting corpus provenance; no lineage of host embeddings
        or weights is assigned.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Raw and wiki declarative text, catalog summaries and historical tasks at query/prior-art
          readers
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-obj-raw-body
          - memory.md#mem-obj-raw-frontmatter
          - memory.md#mem-obj-wiki-pages
          - memory.md#mem-obj-task-files
          - epistemic.md#epi-obj-audit-verdict
          - runtime.md#rt-bap-wiki-guidance
          note: Retained text supplies reference/evidence to model consumers.
        records:
        - memory.md#mem-obj-raw-body
        - memory.md#mem-obj-raw-frontmatter
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-index
        - memory.md#mem-obj-wiki-log
        - memory.md#mem-obj-task-files
        - epistemic.md#epi-obj-audit-verdict
        - runtime.md#rt-bap-wiki-guidance
        note: Content informs answers, authoring or precedent use, without semantic acceptance or demonstrated
          activation.
      - scope: Wiki procedures and schema prose at later operational/writing readers; task Goal/Approach
          at implementation
        assessment: known
        findings:
        - value: instruction
          basis: claimed
          records:
          - memory.md#mem-rte-procedure-capture
          - memory.md#mem-bap-procedure-guidance
          - memory.md#mem-obj-schema-guidance
          - runtime.md#rt-bap-task-guidance
          note: Procedure rules, local writing conventions and work contracts direct later behavior.
        records:
        - memory.md#mem-rte-procedure-capture
        - memory.md#mem-bap-procedure-guidance
        - memory.md#mem-obj-schema-guidance
        - memory.md#mem-obj-task-files
        - epistemic.md#epi-obj-audit-verdict
        - runtime.md#rt-bap-task-guidance
        note: Guidance authority is distinct from executable denial.
      - scope: Schema enum/policy parts at lint parser and coverage/report consumer
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-schema-guidance
          - memory.md#mem-obj-lint-acceptance
          - epistemic.md#epi-obj-lint-settings
          - epistemic.md#epi-rte-lint-acknowledge
          note: Retained enums and policy criteria condition fixed conformance checks and acceptance matching.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-lint-acceptance
          - epistemic.md#epi-obj-lint-settings
          - epistemic.md#epi-rte-lint-acknowledge
          note: Matching accepted info is removed from live findings; blocking issues cannot be waived
            this way.
        - value: routing
          basis: wired
          records:
          - epistemic.md#epi-rte-lint-acknowledge
          note: Page-check exclusions select coverage; declared boilerplate changes scaffold checking.
        records:
        - memory.md#mem-obj-schema-guidance
        - memory.md#mem-obj-lint-acceptance
        - epistemic.md#epi-obj-lint-settings
        - epistemic.md#epi-rte-lint-acknowledge
        note: Acceptance bullets enforce info-only report partitioning; exclusions select checked trees;
          these do not certify source truth.
      - scope: Audit baseline and task lifecycle/design flags at maintenance and finish consumers
        assessment: known
        findings:
        - value: routing
          basis: claimed
          records:
          - memory.md#mem-obj-index
          - memory.md#mem-obj-wiki-log
          - memory.md#mem-rte-task-close
          - epistemic.md#epi-rte-task-stamp
          note: Baseline selects cold-read working set; audit/design stamps select close-out and architecture-refresh
            paths.
        records:
        - memory.md#mem-obj-index
        - memory.md#mem-obj-wiki-log
        - memory.md#mem-obj-task-files
        - epistemic.md#epi-obj-audit-verdict
        - memory.md#mem-rte-task-close
        - epistemic.md#epi-rte-task-stamp
        note: Model consumers use durable state to choose work, rechecking or conditional architecture
          refresh.
      - scope: Frozen task/intent and verifier returns at repair checks
        assessment: known
        findings:
        - value: validation
          basis: claimed
          records: *id004
          note: Frozen commitments and approved edits determine proposed/landed repair conformity.
        - value: routing
          basis: claimed
          records: *id004
          note: Gate/verifier result selects continuation, retry, restore or human stop.
        - value: learning
          basis: claimed
          records: *id004
          note: Retained criticism feeds durable task-contract revision, whose later consumer is implementation.
        records: *id004
        note: Retained baseline criteria and licensed edits constrain later model checks/writes, with
          protocol rather than host enforcement.
      - scope: Lint feedback at acceptance-declaration update consumer
        assessment: known
        findings:
        - value: learning
          basis: claimed
          records:
          - memory.md#mem-rte-finding-acceptance
          note: Experience from lint is retained as behavior-shaping checking metadata.
        records: *id005
        note: Update-consumer learning force is separate from downstream symbolic suppression.
      - scope: Catalog/page relevance and remaining selectors
        assessment: partial
        findings:
        - value: routing
          basis: claimed
          records:
          - memory.md#mem-obj-index
          - memory.md#mem-obj-wiki-log
          - runtime.md#rt-rte-wiki-consume
          - epistemic.md#epi-rte-wiki-retain
          note: Catalog and question/topic information select pages for requested reads.
        records:
        - memory.md#mem-obj-index
        - memory.md#mem-obj-wiki-log
        - runtime.md#rt-rte-wiki-consume
        - epistemic.md#epi-rte-wiki-retain
        note: Index summaries influence model relevance selection; accepted records do not establish a
          relative-priority/ranking mechanism distinct from selection, so ranking is not asserted.
      - scope: Previous benchmark at regression aggregation; changelog latest day at update consumer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: *id002
          note: Prior benchmark supplies evidence for regression comparison.
        - value: routing
          basis: claimed
          records: *id006
          note: Latest recorded day selects the next history window.
        records:
        - epistemic.md#epi-obj-test-report
        - epistemic.md#epi-rte-benchmark-rollup
        - runtime.md#rt-rte-evaluator-worker
        - memory.md#mem-rte-changelog-update
        note: These paths change report/processing decisions, not worker training.
      - scope: Remaining shipped-family retained outputs and their later consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-helper-dispatch
        - memory.md#mem-clm-summary-transfer
        - runtime.md#rt-rte-task-implement
        note: Detailed output-consumer routes of remaining instruction-writing, portability, git, formatting
          and editorial families were not established by accepted records. Standalone summary delivery
          alone supplies no save/reload chain. This prevents exhaustive classification, not the positive
          local findings.
      records:
      - memory.md#mem-obj-raw-body
      - memory.md#mem-obj-raw-frontmatter
      - memory.md#mem-obj-wiki-pages
      - memory.md#mem-obj-index
      - memory.md#mem-obj-wiki-log
      - memory.md#mem-obj-task-files
      - epistemic.md#epi-obj-audit-verdict
      - runtime.md#rt-bap-wiki-guidance
      - memory.md#mem-rte-procedure-capture
      - memory.md#mem-bap-procedure-guidance
      - memory.md#mem-obj-schema-guidance
      - runtime.md#rt-bap-task-guidance
      - memory.md#mem-obj-lint-acceptance
      - epistemic.md#epi-obj-lint-settings
      - epistemic.md#epi-rte-lint-acknowledge
      - memory.md#mem-rte-task-close
      - epistemic.md#epi-rte-task-stamp
      - runtime.md#rt-obj-relay-files
      - runtime.md#rt-rte-readiness-repair
      - memory.md#mem-rte-finding-acceptance
      - runtime.md#rt-rte-wiki-consume
      - epistemic.md#epi-rte-wiki-retain
      - epistemic.md#epi-obj-test-report
      - epistemic.md#epi-rte-benchmark-rollup
      - runtime.md#rt-rte-evaluator-worker
      - memory.md#mem-rte-changelog-update
      - runtime.md#rt-rte-helper-dispatch
      - memory.md#mem-clm-summary-transfer
      - runtime.md#rt-rte-task-implement
      note: Authority is consumer-specific. Learning at durable update consumers is not a benefit claim;
        no parametric adaptation or global enforcement/ranking authority is inferred.
    write_agency:
      assessment: partial
      units:
      - scope: Import/wrapup page selections and explicit human task edits/accepted findings
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records:
          - runtime.md#rt-rte-wiki-triage
          - memory.md#mem-obj-task-files
          - epistemic.md#epi-obj-audit-verdict
          note: Human selects page candidates or explicitly edits/accepts task content.
        records:
        - runtime.md#rt-rte-wiki-triage
        - memory.md#mem-obj-task-files
        - epistemic.md#epi-obj-audit-verdict
        note: Manual is content approval, not merely starting a workflow.
      - scope: Raw acquisition, direct hub/query filing, deterministic page maintenance and procedure
          capture
        assessment: partial
        findings:
        - value: automatic
          basis: claimed
          records:
          - memory.md#mem-obj-raw-body
          - memory.md#mem-obj-raw-frontmatter
          - runtime.md#rt-rte-wiki-consume
          - epistemic.md#epi-rte-wiki-retain
          - memory.md#mem-rte-procedure-capture
          - memory.md#mem-bap-procedure-guidance
          - epistemic.md#epi-rte-wiki-remediate
          note: Model capture, trigger filing and recoverable maintenance decide admission; invoking the
            workflow is not content approval.
        records:
        - memory.md#mem-obj-raw-body
        - memory.md#mem-obj-raw-frontmatter
        - runtime.md#rt-rte-wiki-consume
        - epistemic.md#epi-rte-wiki-retain
        - memory.md#mem-rte-procedure-capture
        - memory.md#mem-bap-procedure-guidance
        - epistemic.md#epi-rte-wiki-remediate
        note: Model admits content without per-item human approval on these paths. Maintenance raw-body
          exception conflicts with general read-only constraint; operative precedence remains unresolved.
      - scope: Schema initialization domain/tag decision versus generated conventions
        assessment: partial
        findings:
        - value: manual
          basis: claimed
          records: &id007
          - memory.md#mem-obj-schema-guidance
          note: Human supplies local domain and starting taxonomy content.
        - value: automatic
          basis: wired
          records: *id007
          note: Initializer copies the shipped schema template without a separate per-convention approval
            gate.
        records: *id007
        note: Human supplies domain/starting tags; scaffold copying is code generation. Full convention/template
          admission inventory remains uninspected.
      - scope: Readiness task repair, audit stamp, lint acceptance, navigation/log and changelog update
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records:
          - runtime.md#rt-obj-relay-files
          - runtime.md#rt-rte-readiness-repair
          - epistemic.md#epi-rte-task-stamp
          - memory.md#mem-rte-finding-acceptance
          - epistemic.md#epi-rte-lint-acknowledge
          - memory.md#mem-obj-index
          - memory.md#mem-obj-wiki-log
          - memory.md#mem-rte-changelog-update
          note: Model-owned verified edits, verdict stamps, acceptance bullets and summaries persist without
            per-output human approval.
        records:
        - runtime.md#rt-obj-relay-files
        - runtime.md#rt-rte-readiness-repair
        - epistemic.md#epi-rte-task-stamp
        - memory.md#mem-rte-finding-acceptance
        - epistemic.md#epi-rte-lint-acknowledge
        - memory.md#mem-obj-index
        - memory.md#mem-obj-wiki-log
        - memory.md#mem-rte-changelog-update
        note: Computational judgment admits these outputs; consequential intent changes remain separately
          human-owned.
      - scope: Evaluation capture/benchmark generation
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: *id002
          note: Driver and aggregators write retained evaluation results.
        records: *id002
        note: Caller selects experiment; software admits captured/generated artifacts.
      - scope: Preexisting corpus initialization and remaining Lint-policy admission mechanisms
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-wiki-pages
        - memory.md#mem-obj-task-files
        - epistemic.md#epi-obj-audit-verdict
        - epistemic.md#epi-obj-lint-settings
        note: Current files and fixed read consumers do not establish who approved original content or
          each exclusion/boilerplate declaration.
      - scope: Remaining shipped-family retained outputs and their later consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-helper-dispatch
        - memory.md#mem-clm-summary-transfer
        - runtime.md#rt-rte-task-implement
        note: Detailed output-consumer routes of remaining instruction-writing, portability, git, formatting
          and editorial families were not established by accepted records. Standalone summary delivery
          alone supplies no save/reload chain. This prevents exhaustive classification, not the positive
          local findings.
      records:
      - runtime.md#rt-rte-wiki-triage
      - memory.md#mem-obj-task-files
      - epistemic.md#epi-obj-audit-verdict
      - memory.md#mem-obj-raw-body
      - memory.md#mem-obj-raw-frontmatter
      - runtime.md#rt-rte-wiki-consume
      - epistemic.md#epi-rte-wiki-retain
      - memory.md#mem-rte-procedure-capture
      - memory.md#mem-bap-procedure-guidance
      - epistemic.md#epi-rte-wiki-remediate
      - memory.md#mem-obj-schema-guidance
      - runtime.md#rt-obj-relay-files
      - runtime.md#rt-rte-readiness-repair
      - epistemic.md#epi-rte-task-stamp
      - memory.md#mem-rte-finding-acceptance
      - epistemic.md#epi-rte-lint-acknowledge
      - memory.md#mem-obj-index
      - memory.md#mem-obj-wiki-log
      - memory.md#mem-rte-changelog-update
      - epistemic.md#epi-obj-test-report
      - epistemic.md#epi-rte-benchmark-rollup
      - runtime.md#rt-rte-evaluator-worker
      - memory.md#mem-obj-wiki-pages
      - epistemic.md#epi-obj-lint-settings
      - runtime.md#rt-rte-helper-dispatch
      - memory.md#mem-clm-summary-transfer
      - runtime.md#rt-rte-task-implement
      note: Manual and automatic coexist at distinct admissions. Raw-maintenance conflict and initial/remaining-policy
        control prevent complete coverage.
    curation_operations:
      assessment: partial
      units:
      - scope: Visible-session extraction and instance-stripping procedure derivation
        assessment: known
        findings:
        - value: consolidate
          basis: claimed
          records:
          - runtime.md#rt-rte-wiki-triage
          - memory.md#mem-rte-procedure-capture
          - memory.md#mem-bap-procedure-guidance
          note: Durable claims are selected from session turns; instance details are stripped from reusable
            procedures.
        records:
        - runtime.md#rt-rte-wiki-triage
        - memory.md#mem-rte-procedure-capture
        - memory.md#mem-bap-procedure-guidance
        note: Requested compression/extraction preserves existing operational content; no paired run is
          claimed.
      - scope: Task contract repair and source/page maintenance
        assessment: partial
        findings:
        - value: evolve
          basis: claimed
          records:
          - runtime.md#rt-obj-relay-files
          - runtime.md#rt-rte-readiness-repair
          - memory.md#mem-obj-raw-body
          - memory.md#mem-obj-raw-frontmatter
          - epistemic.md#epi-rte-wiki-remediate
          note: Verified task edits, hub re-ingest replacement and recoverable page correction revise
            existing entries.
        records:
        - runtime.md#rt-obj-relay-files
        - runtime.md#rt-rte-readiness-repair
        - memory.md#mem-obj-raw-body
        - memory.md#mem-obj-raw-frontmatter
        - epistemic.md#epi-rte-wiki-remediate
        note: Known requested revisions remain positive; raw exception precedence and uninspected semantic
          moves prevent exhaustive operation mapping.
      - scope: Wiki supersession archive
        assessment: known
        findings:
        - value: invalidate
          basis: claimed
          records:
          - epistemic.md#epi-rte-wiki-archive
          note: Fully superseded/out-of-scope pages leave index/live links while remaining archived.
        records:
        - epistemic.md#epi-rte-wiki-archive
        note: Retains body/history while withdrawing active navigation, not complete access revocation.
      - scope: Query cross-page composition and task lessons
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-wiki-consume
        - epistemic.md#epi-rte-wiki-retain
        - memory.md#mem-rte-task-close
        - epistemic.md#epi-rte-wiki-compose
        note: Records establish reasoning/lesson production but neither semantic preservation nor a claim
          absent from inputs. Synthesize cannot be established merely from the route name.
      - scope: Catalog rebuilding, digest refresh, lint acknowledgement and evaluator generation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-index
        - memory.md#mem-obj-wiki-log
        - memory.md#mem-obj-raw-body
        - memory.md#mem-obj-raw-frontmatter
        - memory.md#mem-rte-finding-acceptance
        - epistemic.md#epi-rte-lint-acknowledge
        - epistemic.md#epi-obj-test-report
        - epistemic.md#epi-rte-benchmark-rollup
        - runtime.md#rt-rte-evaluator-worker
        note: Access metadata generation, matching/suppression and artifact processing alone establish
          none of the controlled curation transformations over retained claims.
      - scope: Remaining shipped-family retained outputs and their later consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-helper-dispatch
        - memory.md#mem-clm-summary-transfer
        - runtime.md#rt-rte-task-implement
        note: Detailed output-consumer routes of remaining instruction-writing, portability, git, formatting
          and editorial families were not established by accepted records. Standalone summary delivery
          alone supplies no save/reload chain. This prevents exhaustive classification, not the positive
          local findings.
      records:
      - runtime.md#rt-rte-wiki-triage
      - memory.md#mem-rte-procedure-capture
      - memory.md#mem-bap-procedure-guidance
      - runtime.md#rt-obj-relay-files
      - runtime.md#rt-rte-readiness-repair
      - memory.md#mem-obj-raw-body
      - memory.md#mem-obj-raw-frontmatter
      - epistemic.md#epi-rte-wiki-remediate
      - epistemic.md#epi-rte-wiki-archive
      - runtime.md#rt-rte-wiki-consume
      - epistemic.md#epi-rte-wiki-retain
      - memory.md#mem-rte-task-close
      - epistemic.md#epi-rte-wiki-compose
      - memory.md#mem-obj-index
      - memory.md#mem-obj-wiki-log
      - memory.md#mem-rte-finding-acceptance
      - epistemic.md#epi-rte-lint-acknowledge
      - epistemic.md#epi-obj-test-report
      - epistemic.md#epi-rte-benchmark-rollup
      - runtime.md#rt-rte-evaluator-worker
      - runtime.md#rt-rte-helper-dispatch
      - memory.md#mem-clm-summary-transfer
      - runtime.md#rt-rte-task-implement
      note: Consolidation, revision and active withdrawal are supported at claimed model paths. No dedup,
        decay, promote or synthesis is inferred from command names, budgets, confidence labels or logging
        alone.
    read_back_direction:
      assessment: partial
      units:
      - scope: Question/activated wiki orientation and page retrieval; named task lifecycle reads; procedure
          retrieval; pointer-admitted relay reads; incremental changelog read
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records:
          - runtime.md#rt-rte-wiki-consume
          - epistemic.md#epi-rte-wiki-retain
          - memory.md#mem-obj-task-files
          - epistemic.md#epi-obj-audit-verdict
          - memory.md#mem-rte-procedure-capture
          - memory.md#mem-bap-procedure-guidance
          - runtime.md#rt-obj-relay-files
          - runtime.md#rt-rte-readiness-repair
          - memory.md#mem-obj-index
          - memory.md#mem-obj-wiki-log
          - memory.md#mem-rte-changelog-update
          note: Consumers request files/context for query, maintenance, task work and update windows.
        records:
        - runtime.md#rt-rte-wiki-consume
        - epistemic.md#epi-rte-wiki-retain
        - memory.md#mem-obj-task-files
        - epistemic.md#epi-obj-audit-verdict
        - memory.md#mem-rte-procedure-capture
        - memory.md#mem-bap-procedure-guidance
        - runtime.md#rt-obj-relay-files
        - runtime.md#rt-rte-readiness-repair
        - memory.md#mem-obj-index
        - memory.md#mem-obj-wiki-log
        - memory.md#mem-rte-changelog-update
        note: These fulfill activated consumer work requests; subsequent tool delivery is not a second
          unsolicited push.
      - scope: Schema policy reads by later linter and previous benchmark by later evaluation
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-obj-lint-acceptance
          - epistemic.md#epi-obj-lint-settings
          - epistemic.md#epi-rte-lint-acknowledge
          - epistemic.md#epi-obj-test-report
          - epistemic.md#epi-rte-benchmark-rollup
          - runtime.md#rt-rte-evaluator-worker
          note: Linter and aggregator read retained inputs for requested checking/comparison.
        records:
        - memory.md#mem-obj-lint-acceptance
        - epistemic.md#epi-obj-lint-settings
        - epistemic.md#epi-rte-lint-acknowledge
        - epistemic.md#epi-obj-test-report
        - epistemic.md#epi-rte-benchmark-rollup
        - runtime.md#rt-rte-evaluator-worker
        note: Fixed consumers load retained criteria/reference inputs on invocation.
      - scope: Remaining shipped-family retained outputs and their later consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-helper-dispatch
        - memory.md#mem-clm-summary-transfer
        - runtime.md#rt-rte-task-implement
        note: Detailed output-consumer routes of remaining instruction-writing, portability, git, formatting
          and editorial families were not established by accepted records. Standalone summary delivery
          alone supplies no save/reload chain. This prevents exhaustive classification, not the positive
          local findings.
      records:
      - runtime.md#rt-rte-wiki-consume
      - epistemic.md#epi-rte-wiki-retain
      - memory.md#mem-obj-task-files
      - epistemic.md#epi-obj-audit-verdict
      - memory.md#mem-rte-procedure-capture
      - memory.md#mem-bap-procedure-guidance
      - runtime.md#rt-obj-relay-files
      - runtime.md#rt-rte-readiness-repair
      - memory.md#mem-obj-index
      - memory.md#mem-obj-wiki-log
      - memory.md#mem-rte-changelog-update
      - memory.md#mem-obj-lint-acceptance
      - epistemic.md#epi-obj-lint-settings
      - epistemic.md#epi-rte-lint-acknowledge
      - epistemic.md#epi-obj-test-report
      - epistemic.md#epi-rte-benchmark-rollup
      - runtime.md#rt-rte-evaluator-worker
      - runtime.md#rt-rte-helper-dispatch
      - memory.md#mem-clm-summary-transfer
      - runtime.md#rt-rte-task-implement
      note: Inspected routes are pull; no bounded exhaustive absence of other directions is declared.
        Static installed guidance is excluded, not counted as accumulated-memory push.
    read_back_signal:
      assessment: uninspected
      units:
      - scope: Completely classified requested wiki/task/relay/changelog and fixed lint/benchmark reads
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-wiki-consume
        - epistemic.md#epi-rte-wiki-retain
        - memory.md#mem-obj-task-files
        - epistemic.md#epi-obj-audit-verdict
        - runtime.md#rt-obj-relay-files
        - runtime.md#rt-rte-readiness-repair
        - memory.md#mem-rte-changelog-update
        - memory.md#mem-obj-lint-acceptance
        - epistemic.md#epi-obj-lint-settings
        - epistemic.md#epi-rte-lint-acknowledge
        - epistemic.md#epi-obj-test-report
        - epistemic.md#epi-rte-benchmark-rollup
        - runtime.md#rt-rte-evaluator-worker
        note: These direction units are pull-only; push selector classification is inapplicable to them.
          Topic search and a named file do not establish push.
      - scope: Remaining shipped-family retained outputs and their later consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-helper-dispatch
        - memory.md#mem-clm-summary-transfer
        - runtime.md#rt-rte-task-implement
        note: Detailed output-consumer routes of remaining instruction-writing, portability, git, formatting
          and editorial families were not established by accepted records. Standalone summary delivery
          alone supplies no save/reload chain. This prevents exhaustive classification, not the positive
          local findings.
      records:
      - runtime.md#rt-rte-wiki-consume
      - epistemic.md#epi-rte-wiki-retain
      - memory.md#mem-obj-task-files
      - epistemic.md#epi-obj-audit-verdict
      - runtime.md#rt-obj-relay-files
      - runtime.md#rt-rte-readiness-repair
      - memory.md#mem-rte-changelog-update
      - memory.md#mem-obj-lint-acceptance
      - epistemic.md#epi-obj-lint-settings
      - epistemic.md#epi-rte-lint-acknowledge
      - epistemic.md#epi-obj-test-report
      - epistemic.md#epi-rte-benchmark-rollup
      - runtime.md#rt-rte-evaluator-worker
      - runtime.md#rt-rte-helper-dispatch
      - memory.md#mem-clm-summary-transfer
      - runtime.md#rt-rte-task-implement
      note: No supported push operation is classified. Remaining-family direction coverage is unresolved,
        so the whole axis cannot be inapplicable or absent.
    trace_learning:
      assessment: partial
      units:
      - scope: Maintenance lint feedback to automatically retained finding declaration to later linter
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - memory.md#mem-rte-finding-acceptance
          note: Tool feedback yields retained policy metadata governing later lint reports.
        records: *id005
        note: Qualifying automatic trace-fed checking-policy write is prescribed; fixed downstream matching
          is wired but does not upgrade admission to wired.
      - scope: Helper criticism/verification to automatically repaired task to later implementation
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - runtime.md#rt-obj-relay-files
          - runtime.md#rt-rte-readiness-repair
          - runtime.md#rt-bap-task-guidance
          note: Recorded helper/evaluation experience feeds verified task revisions consumed by later
            implementation.
        records:
        - runtime.md#rt-obj-relay-files
        - runtime.md#rt-rte-readiness-repair
        - runtime.md#rt-bap-task-guidance
        note: Task remains durable behavior-shaping contract, even though relay is cleared next run and
          improved capacity is unobserved.
      - scope: Operational-pattern procedure and completed-work lesson writes
        assessment: partial
        findings:
        - value: 'yes'
          basis: afforded
          records:
          - memory.md#mem-rte-procedure-capture
          - memory.md#mem-bap-procedure-guidance
          - memory.md#mem-rte-task-close
          note: Operational experience can automatically produce retained procedural/lesson guidance for
            later project work.
        records:
        - memory.md#mem-rte-procedure-capture
        - memory.md#mem-bap-procedure-guidance
        - memory.md#mem-rte-task-close
        note: Trace-fed use is afforded; generic direct authoring need not have trace origin, and lesson
          source mixtures are not fully characterized.
      - scope: Selection-approved session wrapup
        assessment: inapplicable
        findings: []
        records: &id008
        - runtime.md#rt-rte-wiki-triage
        note: This admission mechanism requires explicit human content selection, so it is not the automatic
          write required by trace_learning; trace-extracted lineage remains positive.
      - scope: Evaluation snapshots/benchmarks, Git changelog and audit baselines
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-obj-test-report
        - epistemic.md#epi-rte-benchmark-rollup
        - runtime.md#rt-rte-evaluator-worker
        - memory.md#mem-rte-changelog-update
        - memory.md#mem-obj-index
        - memory.md#mem-obj-wiki-log
        note: Retention and comparison alone do not establish every qualifying durable behavior-shaping
          update. Benchmarks have no automatic later-worker update in the inspected path; there is no
          bounded absence record for all possible consumers.
      - scope: Remaining shipped-family retained outputs and their later consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-helper-dispatch
        - memory.md#mem-clm-summary-transfer
        - runtime.md#rt-rte-task-implement
        note: Detailed output-consumer routes of remaining instruction-writing, portability, git, formatting
          and editorial families were not established by accepted records. Standalone summary delivery
          alone supplies no save/reload chain. This prevents exhaustive classification, not the positive
          local findings.
      records:
      - memory.md#mem-rte-finding-acceptance
      - epistemic.md#epi-rte-lint-acknowledge
      - runtime.md#rt-obj-relay-files
      - runtime.md#rt-rte-readiness-repair
      - runtime.md#rt-bap-task-guidance
      - memory.md#mem-rte-procedure-capture
      - memory.md#mem-bap-procedure-guidance
      - memory.md#mem-rte-task-close
      - runtime.md#rt-rte-wiki-triage
      - epistemic.md#epi-obj-test-report
      - epistemic.md#epi-rte-benchmark-rollup
      - runtime.md#rt-rte-evaluator-worker
      - memory.md#mem-rte-changelog-update
      - memory.md#mem-obj-index
      - memory.md#mem-obj-wiki-log
      - runtime.md#rt-rte-helper-dispatch
      - memory.md#mem-clm-summary-transfer
      - runtime.md#rt-rte-task-implement
      note: Positive automatic trace-fed routes coexist with manual extraction and unresolved consumers.
        No system-wide no, exercised improvement or model-weight learning is asserted.
    trace_source:
      assessment: partial
      units:
      - scope: Lint acceptance learning input
        assessment: known
        findings:
        - value: tool-traces
          basis: claimed
          records:
          - memory.md#mem-rte-finding-acceptance
          note: Lint output records tool execution feedback consumed by the persistent-policy update.
        records:
        - memory.md#mem-rte-finding-acceptance
        note: Original input is lint execution feedback plus page intent. Page intent is auxiliary nontrace
          content, not a session-log trace by itself.
      - scope: Readiness repair learning input
        assessment: partial
        findings:
        - value: tool-traces
          basis: claimed
          records: *id004
          note: Lint output and verification/apply-diff feedback feed task revision. No event-stream label
            follows from file serialization.
        records: *id004
        note: Gate/reviewer/verifier returns record agent work and tool/evidence checking; exact mix and
          original tool provenance of all returned passages remains unresolved.
      - scope: Operational-pattern procedures and completed-task lessons
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-procedure-capture
        - memory.md#mem-bap-procedure-guidance
        - memory.md#mem-rte-task-close
        note: Qualifying trace-fed use is afforded, but noticed patterns/finished work may mix session,
          tool and code/task interpretation. No original trace type is fully specified for these alternatives.
      - scope: Manual selection-approved wrapup
        assessment: inapplicable
        findings: []
        records: *id008
        note: Visible session turns have session origin, but their explicitly human-approved admission
          is not a qualifying automatic learning write. Do not transfer session-logs to unrelated automatic
          paths.
      - scope: Remaining shipped-family retained outputs and their later consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-helper-dispatch
        - memory.md#mem-clm-summary-transfer
        - runtime.md#rt-rte-task-implement
        note: Detailed output-consumer routes of remaining instruction-writing, portability, git, formatting
          and editorial families were not established by accepted records. Standalone summary delivery
          alone supplies no save/reload chain. This prevents exhaustive classification, not the positive
          local findings.
      records:
      - memory.md#mem-rte-finding-acceptance
      - runtime.md#rt-obj-relay-files
      - runtime.md#rt-rte-readiness-repair
      - memory.md#mem-rte-procedure-capture
      - memory.md#mem-bap-procedure-guidance
      - memory.md#mem-rte-task-close
      - runtime.md#rt-rte-wiki-triage
      - runtime.md#rt-rte-helper-dispatch
      - memory.md#mem-clm-summary-transfer
      - runtime.md#rt-rte-task-implement
      note: Tool-feedback source is positive on qualifying automatic writes. Missing original-input detail
        prevents classifying all sources, particularly session logs, event streams and trajectories.
---

# ai-modules memory profile

## Comparison rationale

The comparison preserves local evidence strength. Model-interpreted procedures supply claimed transformations and admissions; executable hashing, policy matching and benchmark consumption supply wired mechanisms only at those parts. No inspected execution or causal comparison upgrades them to observed or causally supported findings. Coverage remains partial even where a positive file witness exists.

Reconciliation supersedes EPI-OBJ-wiki-pages with [MEM-OBJ-wiki-pages](memory.md#mem-obj-wiki-pages). All page-object findings therefore cite the memory declaration; epistemic composition/remediation routes remain distinct consumers/functions, not superseded records. The raw-sidecar and Lint-settings containers remain valid alongside their finer body/metadata and acceptance parts. No other supersession changes a value.

Admission and lineage must not be conflated. [RT-RTE-wiki-triage](runtime.md#rt-rte-wiki-triage) extracts visible-session content, but human selections make page admission manual. The positive automatic trace-learning witnesses are instead [MEM-RTE-finding-acceptance](memory.md#mem-rte-finding-acceptance) and [RT-RTE-readiness-repair](runtime.md#rt-rte-readiness-repair). Their later checking-policy and task-contract consumers satisfy the write-route definition without establishing improved capacity. Experience supplies learning force at the update consumer; its outputs separately supply validation/enforcement or instruction downstream.

[MEM-OBJ-raw-body](memory.md#mem-obj-raw-body) retains the maintenance instruction conflict: general read-only raw content versus source-drift re-recording. Hub re-ingest supports revision, but neither immutable preservation nor unrestricted maintenance replacement follows. [EPI-RTE-wiki-compose](epistemic.md#epi-rte-wiki-compose) leaves semantic novelty indeterminate, so the word synthesis does not establish synthesize. [EPI-RTE-wiki-archive](epistemic.md#epi-rte-wiki-archive) supports invalidate only for active reliance/navigation; archived bodies remain searchable rather than revoked.

Requested retrieval is pull even when index/topic selection or fixed matching occurs internally. The inspected pull-only units make push signals locally inapplicable; unresolved remaining consumers prevent a whole-axis inapplicable judgment. Static guidance installation and SPR output intent do not supply accumulated-memory push. [MEM-CLM-summary-transfer](memory.md#mem-clm-summary-transfer) specifies no retained checkpoint save/reload route.

Initial corpus provenance, image consumption, remaining output-consumer paths, exact automatic lesson trace mixtures and several admission alternatives remain unresolved. These prevent complete-value statistics and system-wide negatives. Opaque inference weights are outside this memory inventory because [RT-CMP-host-model](runtime.md#rt-cmp-host-model) establishes inference use, not accumulated provider memory. It is not evidence that learning is absent elsewhere.

Source-read log: none. This member was classified only from the supplied accepted records and reconciliation; no frozen-source ambiguity required direct inspection.
