---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Sentry Skills memory comparison of use-revised guidance, maintenance evidence and later document
  consumers at the frozen package boundary.
run-id: AAS-2026-10-14-skills-2719567f917c-01
source-identity: https://github.com/getsentry/skills
reviewed-boundary: d18b7aa8ba878354e5c348310230e652f7690f9c
memory-comparison:
  version: 2
  scope: 'Included: use-revised skill instructions/metadata and routed references; working/holdout examples,
    findings, SOURCES and SPEC read by later maintenance; generated project guidance; saved document and
    Notion Work Summary handoffs; opaque AXIS reports/baselines and unresolved reply/leaf consumer alternatives.
    Excluded: unchanged shipped prompts/configuration as such, ordinary current-window tool results, host
    frame state, provider weights, application code/status effects without an established memory consumer,
    and final SRED outputs without a subsequent agent route. External retention and loading remain unresolved
    included mechanisms, not claims to cover enclosing hosts.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Changed SKILL.md bodies, routed references and maintenance SOURCES/SPEC files
        assessment: known
        findings:
        - value: files
          basis: afforded
          records: &id001
          - runtime.md#rt-obj-skill-md
          - runtime.md#rt-rte-skill-revision
          - memory.md#mem-obj-sources
          - memory.md#mem-obj-spec
          note: The inspected Git-backed files and prescribed revisions provide filesystem and repository
            retention; no exercised update is supplied.
        - value: repo
          basis: afforded
          records: *id001
          note: The inspected Git-backed files and prescribed revisions provide filesystem and repository
            retention; no exercised update is supplied.
        records: *id001
        note: The inspected Git-backed files and prescribed revisions provide filesystem and repository
          retention; no exercised update is supplied.
      - scope: Working/holdout examples and interpreted findings retained for later revision
        assessment: known
        findings:
        - value: files
          basis: claimed
          records: &id002
          - memory.md#mem-obj-working-set
          - memory.md#mem-obj-findings-log
          - epistemic.md#epi-rte-example-retention
          note: Markdown paths on filesystem/Git are prescribed; populated evidence files are not supplied.
        - value: repo
          basis: claimed
          records: *id002
          note: Markdown paths on filesystem/Git are prescribed; populated evidence files are not supplied.
        records: *id002
        note: Markdown paths on filesystem/Git are prescribed; populated evidence files are not supplied.
      - scope: Generated consuming-project AGENTS.md guidance
        assessment: known
        findings:
        - value: files
          basis: claimed
          records: &id003
          - memory.md#mem-obj-agents-md
          - memory.md#mem-rte-project-guidance
          note: Repository filesystem/Git is the specified destination; CLAUDE.md is an alias, not separate
            storage.
        - value: repo
          basis: claimed
          records: *id003
          note: Repository filesystem/Git is the specified destination; CLAUDE.md is an alias, not separate
            storage.
        records: *id003
        note: Repository filesystem/Git is the specified destination; CLAUDE.md is an alias, not separate
          storage.
      - scope: Work Summary consumed by the later SRED organizer
        assessment: known
        findings:
        - value: service-object
          basis: claimed
          records: &id004
          - memory.md#mem-obj-work-summary
          - memory.md#mem-rte-sred-handoff
          note: A private Notion document is prescribed. Link/date/count metadata does not reveal the
            linked payloads or service internals.
        records: *id004
        note: A private Notion document is prescribed. Link/date/count metadata does not reveal the linked
          payloads or service internals.
      - scope: Saved coauthored document consumed by a fresh reader
        assessment: partial
        findings:
        - value: files
          basis: claimed
          records:
          - memory.md#mem-obj-document-draft
          - memory.md#mem-rte-reader-testing
          note: The working-directory Markdown alternative has a named filesystem destination.
        records:
        - memory.md#mem-obj-document-draft
        - memory.md#mem-rte-reader-testing
        note: The host-artifact alternative is included but its physical substrate is not established;
          the file witness cannot classify it.
      - scope: AXIS reports, raw transcripts, generated artifacts and comparison baseline
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-maintainer-eval
        note: External AXIS owns retention; accepted annotations leave storage path and payload uninspected.
          Configuration wiring does not identify the result substrate.
      - scope: Persisted review-thread reply with unresolved later agent receipt
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-thread-reply
        note: The helper wires publication, but service retention details and a later consumer route are
          unresolved; remote mutation alone does not establish a scoped memory substrate.
      - scope: Other included skill/reference maintenance and later-consumer paths not enumerated in the
          accepted records
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-skill-md
        - runtime.md#rt-rte-skill-revision
        note: The recorded instruction container and revision route do not enumerate every domain leaf
          or admission/read path. Unread leaves remain included; complete package-memory coverage is prevented.
      records:
      - runtime.md#rt-obj-skill-md
      - runtime.md#rt-rte-skill-revision
      - memory.md#mem-obj-sources
      - memory.md#mem-obj-spec
      - memory.md#mem-obj-working-set
      - memory.md#mem-obj-findings-log
      - epistemic.md#epi-rte-example-retention
      - memory.md#mem-obj-agents-md
      - memory.md#mem-rte-project-guidance
      - memory.md#mem-obj-work-summary
      - memory.md#mem-rte-sred-handoff
      - memory.md#mem-obj-document-draft
      - memory.md#mem-rte-reader-testing
      - runtime.md#rt-rte-maintainer-eval
      - memory.md#mem-rte-thread-reply
      note: Filesystem/repository and prescribed Notion witnesses coexist with opaque host artifacts,
        AXIS retention and unenumerated leaf paths. External model weights are not an accumulated-memory
        object established by these records.
    representational_form:
      assessment: partial
      units:
      - scope: Revised skill bodies/references, maintenance provenance/contracts, and generated project
          guidance at human/model consumers
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records: &id005
          - runtime.md#rt-obj-skill-md
          - runtime.md#rt-rte-skill-revision
          - memory.md#mem-obj-sources
          - memory.md#mem-obj-spec
          - memory.md#mem-obj-agents-md
          - memory.md#mem-rte-project-guidance
          note: Markdown rules, reasons and contracts have consequences through interpretation. Initial
            shipped copies alone are excluded.
        records: *id005
        note: Markdown rules, reasons and contracts have consequences through interpretation. Initial
          shipped copies alone are excluded.
      - scope: Changed skill frontmatter/registration at host metadata consumers
        assessment: known
        findings:
        - value: symbolic
          basis: afforded
          records: &id006
          - runtime.md#rt-obj-skill-md
          - runtime.md#rt-rte-skill-revision
          note: The record separates host-parsed metadata from model-interpreted prose; the revision route
            can change descriptions and registration. Actual host parsing and activation are external.
        records: *id006
        note: The record separates host-parsed metadata from model-interpreted prose; the revision route
          can change descriptions and registration. Actual host parsing and activation are external.
      - scope: Retained working/holdout examples and interpreted findings at revision consumers
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id007
          - memory.md#mem-obj-working-set
          - memory.md#mem-obj-findings-log
          - epistemic.md#epi-rte-example-retention
          note: Origin and status labels are author-interpreted fields, not fixed-rule executable state.
        records: *id007
        note: Origin and status labels are author-interpreted fields, not fixed-rule executable state.
      - scope: Work Summary text and link/date/count metadata interpreted by the organizer
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records: &id008
          - memory.md#mem-obj-work-summary
          - memory.md#mem-rte-sred-handoff
          note: Project headings and access metadata are interpreted by a model, not a frozen symbolic
            selector.
        records: *id008
        note: Project headings and access metadata are interpreted by a model, not a frozen symbolic selector.
      - scope: Saved draft content at the isolated reader
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records: &id009
          - memory.md#mem-obj-document-draft
          - memory.md#mem-rte-reader-testing
          note: The document is delivered as text for comprehension, regardless of file versus host-artifact
            retention.
        records: *id009
        note: The document is delivered as text for comprehension, regardless of file versus host-artifact
          retention.
      - scope: Opaque AXIS retained raw outputs, artifact payloads and baseline
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-maintainer-eval
        note: The displayed score/report description does not establish operative payload encoding or
          baseline consumption form; numerical scores alone are not parametric memory.
      - scope: Review reply payload at an unestablished later consumer
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-thread-reply
        note: Caller text is known at publication, but the retained part actually selected for a later
          consumer is not established.
      - scope: Other included skill/reference maintenance and later-consumer paths not enumerated in the
          accepted records
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-skill-md
        - runtime.md#rt-rte-skill-revision
        note: The recorded instruction container and revision route do not enumerate every domain leaf
          or admission/read path. Unread leaves remain included; complete package-memory coverage is prevented.
      records:
      - runtime.md#rt-obj-skill-md
      - runtime.md#rt-rte-skill-revision
      - memory.md#mem-obj-sources
      - memory.md#mem-obj-spec
      - memory.md#mem-obj-agents-md
      - memory.md#mem-rte-project-guidance
      - memory.md#mem-obj-working-set
      - memory.md#mem-obj-findings-log
      - epistemic.md#epi-rte-example-retention
      - memory.md#mem-obj-work-summary
      - memory.md#mem-rte-sred-handoff
      - memory.md#mem-obj-document-draft
      - memory.md#mem-rte-reader-testing
      - runtime.md#rt-rte-maintainer-eval
      - memory.md#mem-rte-thread-reply
      note: Natural-language consumers and a separate symbolic metadata path are supported. Opaque result
        payloads and unresolved consumers prevent complete form classification; external provider parameters
        are not classified as this memory.
    lineage:
      assessment: partial
      units:
      - scope: Model-authored revised instructions, interpreted findings, maintenance decisions and generated
          project guidance
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records: &id010
          - runtime.md#rt-rte-skill-revision
          - memory.md#mem-obj-findings-log
          - memory.md#mem-obj-sources
          - memory.md#mem-obj-spec
          - memory.md#mem-rte-project-guidance
          note: Authors generate rules, suspected causes, decisions and project instructions; source retention
            does not establish truth or initial provenance.
        records: *id010
        note: Authors generate rules, suspected causes, decisions and project instructions; source retention
          does not establish truth or initial provenance.
      - scope: Source-adapted guidance and provenance retained for future revision
        assessment: known
        findings:
        - value: imported
          basis: claimed
          records: &id011
          - runtime.md#rt-obj-skill-md
          - runtime.md#rt-rte-skill-revision
          - memory.md#mem-obj-sources
          note: Recorded source synthesis/adaptation imports upstream contributions while keeping decisions
            in SOURCES; cited upstream truth is not independently authenticated.
        records: *id011
        note: Recorded source synthesis/adaptation imports upstream contributions while keeping decisions
          in SOURCES; cited upstream truth is not independently authenticated.
      - scope: Redacted behavior examples promoted into later rules and references
        assessment: partial
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - runtime.md#rt-rte-skill-revision
          - memory.md#mem-obj-working-set
          - epistemic.md#epi-rte-example-retention
          note: Expected/observed behavior examples are summarized/redacted and transformed into later
            guidance in the prescribed evidence route.
        records:
        - runtime.md#rt-rte-skill-revision
        - memory.md#mem-obj-working-set
        - epistemic.md#epi-rte-example-retention
        note: Human-verified, mixed and synthetic origin labels are not authenticated. This finding covers
          the declared experience-extraction path, not an assertion that all initial examples derive from
          actual sessions.
      - scope: Generated Work Summary and draft prose
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records: &id012
          - memory.md#mem-obj-work-summary
          - memory.md#mem-rte-sred-handoff
          - memory.md#mem-obj-document-draft
          - memory.md#mem-rte-reader-testing
          note: Models draft and group human/shared-document/PR/ticket material; imported inputs and authored
            organization coexist without a claim of semantic entailment.
        - value: imported
          basis: claimed
          records: *id012
          note: Models draft and group human/shared-document/PR/ticket material; imported inputs and authored
            organization coexist without a claim of semantic entailment.
        records: *id012
        note: Models draft and group human/shared-document/PR/ticket material; imported inputs and authored
          organization coexist without a claim of semantic entailment.
      - scope: AXIS baseline and retained result payload derivation
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-maintainer-eval
        note: Declared transcripts, artifacts and scores have different derivations; actual retained payloads
          and baseline initialization are not supplied.
      - scope: Remote reply origin and later selected content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-thread-reply
        note: Caller supplies content, but caller identity and upstream derivation are unresolved. Publication
          is not evidence of manual authorship or trace extraction.
      - scope: Other included skill/reference maintenance and later-consumer paths not enumerated in the
          accepted records
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-skill-md
        - runtime.md#rt-rte-skill-revision
        note: The recorded instruction container and revision route do not enumerate every domain leaf
          or admission/read path. Unread leaves remain included; complete package-memory coverage is prevented.
      records:
      - runtime.md#rt-rte-skill-revision
      - memory.md#mem-obj-findings-log
      - memory.md#mem-obj-sources
      - memory.md#mem-obj-spec
      - memory.md#mem-rte-project-guidance
      - runtime.md#rt-obj-skill-md
      - memory.md#mem-obj-working-set
      - epistemic.md#epi-rte-example-retention
      - memory.md#mem-obj-work-summary
      - memory.md#mem-rte-sred-handoff
      - memory.md#mem-obj-document-draft
      - memory.md#mem-rte-reader-testing
      - runtime.md#rt-rte-maintainer-eval
      - memory.md#mem-rte-thread-reply
      note: Authored, imported and prescribed trace-extracted paths are retained separately. Initial example
        origins, opaque results and leaf alternatives remain unresolved; no other-compiled or parametric
        provenance is inferred.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Revised skill rules and project guidance at later task-agent consumers
        assessment: known
        findings:
        - value: instruction
          basis: afforded
          records: &id013
          - runtime.md#rt-obj-skill-md
          - runtime.md#rt-bap-skill-consumption
          - runtime.md#rt-rte-skill-revision
          - memory.md#mem-obj-agents-md
          - memory.md#mem-rte-project-guidance
          note: Later hosts deliver standing directions; delivery affords instruction authority, not compliance.
        records: *id013
        note: Later hosts deliver standing directions; delivery affords instruction authority, not compliance.
      - scope: Retained behavior examples and findings at the instruction-revision consumer
        assessment: known
        findings:
        - value: learning
          basis: claimed
          records: &id014
          - runtime.md#rt-rte-skill-revision
          - memory.md#mem-obj-working-set
          - memory.md#mem-obj-findings-log
          - epistemic.md#epi-rte-example-retention
          note: Experience and interpreted deltas are prescribed inputs to durable guidance updates. Learning
            authority here does not establish improved future capacity.
        records: *id014
        note: Experience and interpreted deltas are prescribed inputs to durable guidance updates. Learning
          authority here does not establish improved future capacity.
      - scope: SOURCES and evidence explanations at future synthesis/maintenance agents
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records: &id015
          - memory.md#mem-obj-sources
          - memory.md#mem-obj-findings-log
          - runtime.md#rt-rte-skill-revision
          note: These supply provenance, context and suspected causes. Ordinary task consumers need not
            receive the reasons behind promoted rules.
        records: *id015
        note: These supply provenance, context and suspected causes. Ordinary task consumers need not
          receive the reasons behind promoted rules.
      - scope: SPEC scope/output/validation contract and held-out expected behavior at maintenance/replay
          judgment
        assessment: known
        findings:
        - value: validation
          basis: claimed
          records: &id016
          - memory.md#mem-obj-spec
          - memory.md#mem-obj-working-set
          - runtime.md#rt-rte-skill-revision
          note: Retained contracts and example-specific reference outcomes guide conformity judgments;
            they are not a machine-enforced repository admission gate.
        records: *id016
        note: Retained contracts and example-specific reference outcomes guide conformity judgments; they
          are not a machine-enforced repository admission gate.
      - scope: Changed skill metadata at external host selection
        assessment: known
        findings:
        - value: routing
          basis: afforded
          records: &id017
          - runtime.md#rt-obj-skill-md
          - runtime.md#rt-rte-skill-revision
          - runtime.md#rt-bap-skill-consumption
          note: Host-consumed invocation metadata and descriptions select guidance or an invocation; host
            selection details and actual triggering are not inspected.
        records: *id017
        note: Host-consumed invocation metadata and descriptions select guidance or an invocation; host
          selection details and actual triggering are not inspected.
      - scope: Retained Work Summary at organizer and saved draft at fresh reader
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records: &id018
          - memory.md#mem-obj-work-summary
          - memory.md#mem-rte-sred-handoff
          - memory.md#mem-obj-document-draft
          - memory.md#mem-rte-reader-testing
          note: Summary supplies evidence for project analysis; draft supplies the content being understood
            and checked. Neither is a package-level standing policy update.
        records: *id018
        note: Summary supplies evidence for project analysis; draft supplies the content being understood
          and checked. Neither is a package-level standing policy update.
      - scope: AXIS retained reports/baseline at later maintainer comparison/adoption
        assessment: partial
        findings:
        - value: knowledge
          basis: claimed
          records:
          - runtime.md#rt-rte-maintainer-eval
          note: Reviewed reports and baseline comparisons inform subsequent revision/adoption judgments.
        - value: learning
          basis: claimed
          records:
          - runtime.md#rt-rte-maintainer-eval
          - runtime.md#rt-rte-skill-revision
          note: Failure/slow transcripts are prescribed feedback for durable instruction revision, with
            human adoption separate.
        records:
        - runtime.md#rt-rte-maintainer-eval
        - runtime.md#rt-rte-skill-revision
        note: Opaque baseline/report parts and actual payload consumption prevent assigning every local
          effect. A score is not itself a deployed enforcing control.
      - scope: Published review reply at a later repair-agent consumer
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-thread-reply
        note: Advisory remote publication is wired but future receipt is unestablished; do not infer knowledge
          authority at a hypothetical reader.
      - scope: Other included skill/reference maintenance and later-consumer paths not enumerated in the
          accepted records
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-skill-md
        - runtime.md#rt-rte-skill-revision
        note: The recorded instruction container and revision route do not enumerate every domain leaf
          or admission/read path. Unread leaves remain included; complete package-memory coverage is prevented.
      records:
      - runtime.md#rt-obj-skill-md
      - runtime.md#rt-bap-skill-consumption
      - runtime.md#rt-rte-skill-revision
      - memory.md#mem-obj-agents-md
      - memory.md#mem-rte-project-guidance
      - memory.md#mem-obj-working-set
      - memory.md#mem-obj-findings-log
      - epistemic.md#epi-rte-example-retention
      - memory.md#mem-obj-sources
      - memory.md#mem-obj-spec
      - memory.md#mem-obj-work-summary
      - memory.md#mem-rte-sred-handoff
      - memory.md#mem-obj-document-draft
      - memory.md#mem-rte-reader-testing
      - runtime.md#rt-rte-maintainer-eval
      - memory.md#mem-rte-thread-reply
      note: Authority follows each retained part and consumer. Knowledge, instruction, learning, validation
        and routing are locally supported; helper structure checks and triage approval are not reclassified
        as retained-memory enforcement.
    write_agency:
      assessment: partial
      units:
      - scope: Model admission of package guidance and evidence deltas without per-content human approval
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id019
          - runtime.md#rt-rte-skill-revision
          - epistemic.md#epi-rte-example-retention
          note: Starting the workflow is not per-change approval. The author chooses deltas/promotion
            or deferral under the prescribed policy, not an implemented automatic ingester.
        records: *id019
        note: Starting the workflow is not per-change approval. The author chooses deltas/promotion or
          deferral under the prescribed policy, not an implemented automatic ingester.
      - scope: Explicit holdout-to-working reassignment
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records: &id020
          - memory.md#mem-obj-working-set
          - epistemic.md#epi-rte-example-retention
          note: The user must explicitly decide to move those examples; this is separate from ordinary
            model revisions.
        records: *id020
        note: The user must explicitly decide to move those examples; this is separate from ordinary model
          revisions.
      - scope: Maintainer adoption and baseline replacement
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records: &id021
          - runtime.md#rt-rte-maintainer-eval
          note: Maintainer reviews results and chooses adoption or baseline refresh; configured generation/scoring
            does not automatically install a revision.
        records: *id021
        note: Maintainer reviews results and chooses adoption or baseline refresh; configured generation/scoring
          does not automatically install a revision.
      - scope: Project guidance model admission
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id022
          - memory.md#mem-rte-project-guidance
          note: No per-rule human approval is required; host tools and repository review are external
            controls.
        records: *id022
        note: No per-rule human approval is required; host tools and repository review are external controls.
      - scope: SRED summary grouping/drafting before human classification review
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id023
          - memory.md#mem-rte-sred-handoff
          note: Model groups and drafts content; user query initiation does not supply a per-group admission
            decision.
        records: *id023
        note: Model groups and drafts content; user query initiation does not supply a per-group admission
          decision.
      - scope: SRED human classification adjustment and reviewed project content
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records: &id024
          - memory.md#mem-rte-sred-handoff
          note: Explicit user classification changes and repeated review decide the displayed content,
            unlike service physical I/O.
        records: *id024
        note: Explicit user classification changes and repeated review decide the displayed content, unlike
          service physical I/O.
      - scope: Coauthored draft human content curation
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records: &id025
          - memory.md#mem-obj-document-draft
          - memory.md#mem-rte-reader-testing
          note: The user curates content, selects changes and can finalize or decline the structured workflow.
        records: *id025
        note: The user curates content, selects changes and can finalize or decline the structured workflow.
      - scope: Model-directed reader-gap repair
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records: &id026
          - memory.md#mem-rte-reader-testing
          note: Foreground proposes and revises problematic sections in the prescribed route; this is
            separate from human content selections.
        records: *id026
        note: Foreground proposes and revises problematic sections in the prescribed route; this is separate
          from human content selections.
      - scope: AXIS retained report admission and initial baseline control beyond reviewed refresh
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-maintainer-eval
        note: External result generation is configured, but exact retained-report admission and initial
          baseline mechanism are not established.
      - scope: Reply publication caller content admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-thread-reply
        note: CLI caller identity alone does not decide manual versus automatic admission. The helper
          performs physical publication, not content choice.
      - scope: Other included skill/reference maintenance and later-consumer paths not enumerated in the
          accepted records
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-skill-md
        - runtime.md#rt-rte-skill-revision
        note: The recorded instruction container and revision route do not enumerate every domain leaf
          or admission/read path. Unread leaves remain included; complete package-memory coverage is prevented.
      records:
      - runtime.md#rt-rte-skill-revision
      - epistemic.md#epi-rte-example-retention
      - memory.md#mem-obj-working-set
      - runtime.md#rt-rte-maintainer-eval
      - memory.md#mem-rte-project-guidance
      - memory.md#mem-rte-sred-handoff
      - memory.md#mem-obj-document-draft
      - memory.md#mem-rte-reader-testing
      - memory.md#mem-rte-thread-reply
      - runtime.md#rt-obj-skill-md
      note: Model admission is automatic despite user-started tasks. Explicit holdout, adoption, baseline-refresh
        and content-review decisions are manual. Unknown initial controls and generic callers remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Retained instruction precision/replacement and evidence promotion
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records: &id027
          - runtime.md#rt-rte-skill-revision
          note: The recorded revision/annotation prescribes revising/narrowing/replacing existing rules,
            deleting redundant rules, and moving evidence into future runtime guidance. These are requested
            transformations, not observed edits.
        - value: dedup
          basis: claimed
          records: *id027
          note: The recorded revision/annotation prescribes revising/narrowing/replacing existing rules,
            deleting redundant rules, and moving evidence into future runtime guidance. These are requested
            transformations, not observed edits.
        - value: promote
          basis: claimed
          records: *id027
          note: The recorded revision/annotation prescribes revising/narrowing/replacing existing rules,
            deleting redundant rules, and moving evidence into future runtime guidance. These are requested
            transformations, not observed edits.
        records: *id027
        note: The recorded revision/annotation prescribes revising/narrowing/replacing existing rules,
          deleting redundant rules, and moving evidence into future runtime guidance. These are requested
          transformations, not observed edits.
      - scope: Retained experience/example summarization into concise examples and guidance
        assessment: known
        findings:
        - value: consolidate
          basis: claimed
          records: &id028
          - epistemic.md#epi-rte-example-retention
          - runtime.md#rt-rte-skill-revision
          note: Summarization/redaction and conversion of existing experience into reduced guidance is
            consolidation; preserving raw examples does not exclude it.
        records: *id028
        note: Summarization/redaction and conversion of existing experience into reduced guidance is consolidation;
          preserving raw examples does not exclude it.
      - scope: Saved document refinement after reader checks
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records: &id029
          - memory.md#mem-obj-document-draft
          - memory.md#mem-rte-reader-testing
          note: Problematic retained sections are revised after comprehension feedback; no exercised repair
            is supplied.
        records: *id029
        note: Problematic retained sections are revised after comprehension feedback; no exercised repair
          is supplied.
      - scope: Novel suspected-cause findings and source synthesis semantics
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-findings-log
        - memory.md#mem-obj-sources
        - runtime.md#rt-rte-skill-revision
        note: Records name suspected causes and synthesis but supply no particular input/output claim
          proving a new claim absent from inputs. The command name does not establish synthesize.
      - scope: AXIS baseline/report transformations beyond human refresh
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-maintainer-eval
        note: Replacing a baseline after review does not itself establish consolidation, decay, deduplication
          or promotion; operative retained transformations are unspecified.
      - scope: SRED retained summary-to-project transformation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-work-summary
        - memory.md#mem-rte-sred-handoff
        note: Grouping and project drafting are prescribed but semantic preservation versus novel claims
          and revision of an existing entry are not established by the accepted records.
      - scope: Reply persistence maintenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-thread-reply
        note: Append publication is wired; no retained-content curation operation is established. No bounded
          absence record licenses an absent assessment.
      - scope: Other included skill/reference maintenance and later-consumer paths not enumerated in the
          accepted records
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-skill-md
        - runtime.md#rt-rte-skill-revision
        note: The recorded instruction container and revision route do not enumerate every domain leaf
          or admission/read path. Unread leaves remain included; complete package-memory coverage is prevented.
      records:
      - runtime.md#rt-rte-skill-revision
      - epistemic.md#epi-rte-example-retention
      - memory.md#mem-obj-document-draft
      - memory.md#mem-rte-reader-testing
      - memory.md#mem-obj-findings-log
      - memory.md#mem-obj-sources
      - runtime.md#rt-rte-maintainer-eval
      - memory.md#mem-obj-work-summary
      - memory.md#mem-rte-sred-handoff
      - memory.md#mem-rte-thread-reply
      - runtime.md#rt-obj-skill-md
      note: Claimed evolution, deduplication, promotion and consolidation remain distinct from wired structural
        validation. Opaque transformations and indeterminate novelty prevent complete curation coverage;
        no synthesize value is inferred from a route name.
    read_back_direction:
      assessment: partial
      units:
      - scope: Later skill host relevance activation of changed installed guidance
        assessment: known
        findings:
        - value: push
          basis: claimed
          records: &id030
          - runtime.md#rt-bap-skill-consumption
          - runtime.md#rt-rte-skill-revision
          - runtime.md#rt-obj-skill-md
          note: Automatic relevance activation supplies changed guidance without a separate request for
            that retained text. Host activation is declared, not observed.
        records: *id030
        note: Automatic relevance activation supplies changed guidance without a separate request for
          that retained text. Host activation is declared, not observed.
      - scope: Future project host loading of generated root/nested guidance
        assessment: known
        findings:
        - value: push
          basis: afforded
          records: &id031
          - memory.md#mem-obj-agents-md
          - memory.md#mem-rte-project-guidance
          note: Standing project defaults are intended to enter later host guidance automatically; actual
            loading and precedence remain external.
        records: *id031
        note: Standing project defaults are intended to enter later host guidance automatically; actual
          loading and precedence remain external.
      - scope: Later maintenance intake of prior SPEC/SOURCES/examples and requested step references
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records: &id032
          - runtime.md#rt-rte-skill-revision
          - memory.md#mem-obj-sources
          - memory.md#mem-obj-spec
          - memory.md#mem-obj-working-set
          - memory.md#mem-obj-findings-log
          note: Synthesis/revision agents request relevant retained material by maintenance task/current
            step; returning those requested files is not another push.
        records: *id032
        note: Synthesis/revision agents request relevant retained material by maintenance task/current
          step; returning those requested files is not another push.
      - scope: User-identified Work Summary requested by organizer
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records: &id033
          - memory.md#mem-obj-work-summary
          - memory.md#mem-rte-sred-handoff
          note: The later organizer asks for and reads the prior summary link and related source content.
        records: *id033
        note: The later organizer asks for and reads the prior summary link and related source content.
      - scope: Requested saved-draft reader test, including human fresh-chat transfer
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records: &id034
          - memory.md#mem-obj-document-draft
          - memory.md#mem-rte-reader-testing
          note: Invoker requests comprehension of the selected document/question. Delivery in the requested
            test does not become unsolicited push; the manual fresh-chat alternative remains included.
        records: *id034
        note: Invoker requests comprehension of the selected document/question. Delivery in the requested
          test does not become unsolicited push; the manual fresh-chat alternative remains included.
      - scope: Later maintainer request for AXIS reports and baseline comparison
        assessment: partial
        findings:
        - value: pull
          basis: claimed
          records:
          - runtime.md#rt-rte-maintainer-eval
          note: Maintainer reviews reports and selects baseline comparison for later evaluation/adoption.
        records:
        - runtime.md#rt-rte-maintainer-eval
        note: Actual harness payload delivery and additional automatic report routes are not inspected;
          the requested review witness does not resolve them.
      - scope: Later receipt of stored review-thread replies
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-thread-reply
        note: Future caller is not established; feedback first-comment projection and self-comment omission
          prevent inferring a reply read-back route from persistence.
      - scope: Other included skill/reference maintenance and later-consumer paths not enumerated in the
          accepted records
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-skill-md
        - runtime.md#rt-rte-skill-revision
        note: The recorded instruction container and revision route do not enumerate every domain leaf
          or admission/read path. Unread leaves remain included; complete package-memory coverage is prevented.
      records:
      - runtime.md#rt-bap-skill-consumption
      - runtime.md#rt-rte-skill-revision
      - runtime.md#rt-obj-skill-md
      - memory.md#mem-obj-agents-md
      - memory.md#mem-rte-project-guidance
      - memory.md#mem-obj-sources
      - memory.md#mem-obj-spec
      - memory.md#mem-obj-working-set
      - memory.md#mem-obj-findings-log
      - memory.md#mem-obj-work-summary
      - memory.md#mem-rte-sred-handoff
      - memory.md#mem-obj-document-draft
      - memory.md#mem-rte-reader-testing
      - runtime.md#rt-rte-maintainer-eval
      - memory.md#mem-rte-thread-reply
      note: Both requested retention reads and declared/afforded host guidance pushes exist. Host implementation,
        AXIS alternatives, reply receipt and unread leaves prevent a complete direction inventory.
    read_back_signal:
      assessment: not-determinable
      units:
      - scope: Automatic relevance selection of changed installed skill guidance
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-bap-skill-consumption
        - runtime.md#rt-obj-skill-md
        - runtime.md#rt-rte-skill-revision
        note: Trigger is a relevant task; selected retained part is updated SKILL.md/references. The records
          do not establish selector implementation/input matching, so neither inferred-judgment nor identifier
          can be assigned.
      - scope: Automatic later host loading of generated project guidance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-agents-md
        - memory.md#mem-rte-project-guidance
        note: Trigger is later project work, selected part is root/nested AGENTS.md. Scope names and a
          closest-file policy do not establish an actual identity-match selector or its host wiring.
      - scope: Requested maintenance, SRED and reader-test delivery operations only
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-skill-revision
        - memory.md#mem-rte-sred-handoff
        - memory.md#mem-rte-reader-testing
        note: 'These scoped operations are pull: a consumer/invoker requests retained files, summary or
          draft. Push-signal classification is inapplicable to these operations, not to the entire package.'
      - scope: Opaque AXIS automatic delivery alternatives and unresolved review-reply/leaf read-back
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-maintainer-eval
        - memory.md#mem-rte-thread-reply
        - runtime.md#rt-obj-skill-md
        note: Read direction/selection for these alternatives is unresolved. Known pull review or a thread
          identifier cannot make their push signals inapplicable.
      records:
      - runtime.md#rt-bap-skill-consumption
      - runtime.md#rt-obj-skill-md
      - runtime.md#rt-rte-skill-revision
      - memory.md#mem-obj-agents-md
      - memory.md#mem-rte-project-guidance
      - memory.md#mem-rte-sred-handoff
      - memory.md#mem-rte-reader-testing
      - runtime.md#rt-rte-maintainer-eval
      - memory.md#mem-rte-thread-reply
      note: No controlled push selector is established in accepted records. Host relevance/scope declarations
        do not reveal selection rules; unresolved alternatives prevent a pull-only or absent boundary
        assessment.
    trace_learning:
      assessment: partial
      units:
      - scope: Model admission of behavior-example-derived findings and durable skill rules for later
          invocation
        assessment: partial
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - runtime.md#rt-rte-skill-revision
          - epistemic.md#epi-rte-example-retention
          - memory.md#mem-obj-working-set
          - memory.md#mem-obj-findings-log
          - runtime.md#rt-bap-skill-consumption
          note: The prescribed experience-to-findings-to-guidance chain allows model admission without
            per-change human approval and later task consumption. It qualifies as a claimed trace-fed
            durable behavioral write, not exercised learning.
        records:
        - runtime.md#rt-rte-skill-revision
        - epistemic.md#epi-rte-example-retention
        - memory.md#mem-obj-working-set
        - memory.md#mem-obj-findings-log
        - runtime.md#rt-bap-skill-consumption
        note: Origin tags include human-verified, mixed and synthetic inputs; actual trace provenance
          and populated promotion/adoption are unknown. The qualifying route does not imply every example
          or revision is trace learning.
      - scope: AXIS transcript feedback through human adoption and opaque report writes
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-maintainer-eval
        - runtime.md#rt-rte-skill-revision
        note: Retained transcripts can guide revision, but the recorded adoption gate is manual and the
          precise automatic trace-fed admitted artifact chain is not established. Do not infer an automatic
          installed update from scores.
      - scope: Project guidance, SRED summaries and reader-gap document repairs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-project-guidance
        - memory.md#mem-rte-sred-handoff
        - memory.md#mem-rte-reader-testing
        note: Durable model writes are prescribed, but records do not establish the original input as
          qualifying activity traces for every such update. Repository facts/shared documents and reader
          feedback cannot be relabelled wholesale as traces.
      - scope: Review replies and unenumerated domain-leaf writes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-thread-reply
        - runtime.md#rt-obj-skill-md
        - runtime.md#rt-rte-skill-revision
        note: Reply caller origin and later consumption are unresolved; other leaf writes are not enumerated.
          Neither supports a system-wide no.
      records:
      - runtime.md#rt-rte-skill-revision
      - epistemic.md#epi-rte-example-retention
      - memory.md#mem-obj-working-set
      - memory.md#mem-obj-findings-log
      - runtime.md#rt-bap-skill-consumption
      - runtime.md#rt-rte-maintainer-eval
      - memory.md#mem-rte-project-guidance
      - memory.md#mem-rte-sred-handoff
      - memory.md#mem-rte-reader-testing
      - memory.md#mem-rte-thread-reply
      - runtime.md#rt-obj-skill-md
      note: The prescribed skill-evidence chain supports a local claimed yes independently of observed
        capacity improvement. No bounded absence record supports no; other write chains and initial origins
        remain unresolved.
    trace_source:
      assessment: not-determinable
      units:
      - scope: Original inputs to the qualifying skill-example-to-guidance write
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-skill-revision
        - memory.md#mem-obj-working-set
        - epistemic.md#epi-rte-example-retention
        - memory.md#mem-obj-findings-log
        note: Expected/observed behavior and human-verified/mixed/synthetic labels establish experience-oriented
          intake but not recorded conversational turns, tool requests/results, discrete event records
          or linked state/action/outcome trajectories. None of the four controlled source values is established.
      - scope: AXIS failure/slow transcripts and alternative write chains
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-maintainer-eval
        - runtime.md#rt-rte-skill-revision
        - memory.md#mem-rte-project-guidance
        - memory.md#mem-rte-sred-handoff
        - memory.md#mem-rte-reader-testing
        note: Transcripts are declared, but their contents/origin and exact qualifying automatic admission
          are opaque. Artifact or journal labels alone cannot establish session-logs, tool-traces, event-streams
          or trajectories.
      - scope: Other included skill/reference maintenance and later-consumer paths not enumerated in the
          accepted records
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-obj-skill-md
        - runtime.md#rt-rte-skill-revision
        note: The recorded instruction container and revision route do not enumerate every domain leaf
          or admission/read path. Unread leaves remain included; complete package-memory coverage is prevented.
      records:
      - runtime.md#rt-rte-skill-revision
      - memory.md#mem-obj-working-set
      - epistemic.md#epi-rte-example-retention
      - memory.md#mem-obj-findings-log
      - runtime.md#rt-rte-maintainer-eval
      - memory.md#mem-rte-project-guidance
      - memory.md#mem-rte-sred-handoff
      - memory.md#mem-rte-reader-testing
      - runtime.md#rt-obj-skill-md
      note: A claimed trace-learning route does not identify its original trace class. Records lack the
        content/origin facts needed for any controlled trace_source value; no negative trace-learning
        inventory makes the axis inapplicable.
---

# Sentry Skills memory profile

## Comparison rationale

The strongest supported boundary is editable guidance with separate evidence and task consumers. [RT-RTE-skill-revision](runtime.md#rt-rte-skill-revision) and [RT-OBJ-skill-md](runtime.md#rt-obj-skill-md) support changes intended for later loading; static installation alone is not accumulated memory. Markdown rules are natural-language at model consumers, while changed invocation metadata is symbolic at external host consumers. Neither form licenses compliance or observed activation.

[MEM-OBJ-working-set](memory.md#mem-obj-working-set) and [MEM-OBJ-findings-log](memory.md#mem-obj-findings-log) distinguish semi-raw examples from interpreted causes/deltas. [EPI-RTE-example-retention](epistemic.md#epi-rte-example-retention) is the retention part of the revision route, not an additional copy of that route. Its summarization supports claimed consolidation; promotion into standing rules supports claimed promotion. The revision account also supports claimed evolution and removal of redundant rules. No particular novel proposition establishes synthesis, despite the source-native synthesis route name.

Experience has learning authority at the guidance-update consumer; the output has instruction authority at the later task consumer. The prescribed model-admitted example-to-guidance route supports trace_learning "yes" at claimed basis. This does not establish automatic ingestion, exercised update, improved capacity or successful self-improvement. Actual example origins and their original trace contents remain unknown, so trace_source has no positive controlled classification. The manual maintainer gate and explicit holdout reassignment remain separate admission mechanisms; neither converts every model-chosen delta to manual admission.

[MEM-OBJ-sources](memory.md#mem-obj-sources) retains reasons for maintenance, and [MEM-OBJ-spec](memory.md#mem-obj-spec) supplies an interpreted conformity contract. Runtime consumers are not promised those reasons. [MEM-RTE-sred-handoff](memory.md#mem-rte-sred-handoff) instead requests a prior summary as evidence; [MEM-RTE-reader-testing](memory.md#mem-rte-reader-testing) requests a saved draft for comprehension. Both are pull chains, including the manual reader transfer. They are not automatically instruction-learning routes merely because models generate documents.

Host relevance activation supplies a claimed push path through [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption). Generated project defaults supply an afforded push through [MEM-RTE-project-guidance](memory.md#mem-rte-project-guidance). Neither accepted account establishes the automatic selector's actual matching algorithm. A filename, project scope or requested summary link alone does not warrant an identifier push signal. Requested step-reference reads remain pull rather than being counted again as push delivery.

The reconciliation resolves the epistemic and workflow reply duplicates to [MEM-RTE-thread-reply](memory.md#mem-rte-thread-reply), and the epistemic reader duplicate to [MEM-RTE-reader-testing](memory.md#mem-rte-reader-testing). This profile uses those canonical routes. Reader supersession preserves the fuller saved-draft read-back account without upgrading isolation or fact checking. Reply supersessions do not establish future agent receipt: service publication and first-comment/self-comment selection remain distinct. The evidence-file container is not superseded; this profile uses its separately recorded example/findings parts without double-counting them.

[RT-RTE-maintainer-eval](runtime.md#rt-rte-maintainer-eval) records a configured evaluation harness but opaque retained results. Wiring of scenario generation does not upgrade report substrate, original trace contents, baseline initialization or later payload delivery. The file alternative for a document draft does not classify its host-artifact alternative. These uncertainties and unenumerated domain leaves prevent system-complete axis inventories. They remain explicitly included rather than being discarded to obtain known coverage. No accepted evidenced-absence record warrants a system-wide negative.

No frozen-source files were read for this classification. All warrants come from supplied accepted records and their annotations; reconciliation was used only to resolve identity. No new records, quotes or evidence were added.
