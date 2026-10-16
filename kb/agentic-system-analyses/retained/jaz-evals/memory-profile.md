---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'jaz-evals memory profile: ACE trace-conditioned advice, requested history handoffs, opaque
  Letta state and retained diagnostics.'
run-id: AAS-2026-10-15-jaz-evals-17ab95f93794-01
source-identity: https://github.com/jaz-lang/jaz-evals
reviewed-boundary: 2ffe7b5e6792a76fccb26f9ce188c88fb95ffa72
memory-comparison:
  version: 2
  scope: ACE accumulated advice, symbolic bullet metadata, update traces and snapshots; JAZ trace-responsive
    guidance/helpers and explicit history/progress handoffs; smolagents wrapped history and continuation
    summaries; Letta core blocks as possible editable state, retained conversations, compaction checkpoints
    and opaque archival/search state; retained outcome/trace diagnostic consumers. Excludes shipped static
    instructions, unmodified model/encoder weights, benchmark world state, ordinary transient turns without
    later retained consumption, and fresh-frame/CodeAct eviction alone. Initial provenance and all named
    opaque alternatives remain included uncertainties.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: ACE live advice and symbolic bullet metadata
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id001
          - memory.md#mem-obj-playbook
          - memory.md#mem-obj-playbook-counts
          note: Live strings carry updates; text snapshots retain advice and counts.
        - value: files
          basis: wired
          records: *id001
          note: Live strings carry updates; text snapshots retain advice and counts.
        records: *id001
        note: Live strings carry updates; text snapshots retain advice and counts.
      - scope: ACE diagnostic artifacts and retained task verdicts
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id002
          - memory.md#mem-obj-adaptation-artifacts
          - epistemic.md#epi-obj-task-verdict
          note: Attempt-local files coexist with in-process outcome dictionaries.
        - value: in-memory
          basis: wired
          records: *id002
          note: Attempt-local files coexist with in-process outcome dictionaries.
        records: *id002
        note: Attempt-local files coexist with in-process outcome dictionaries.
      - scope: JAZ and smolagents explicitly forwarded history, summaries and revised guidance
        assessment: known
        findings:
        - value: in-memory
          basis: afforded
          records: &id003
          - memory.md#mem-rte-jaz-history
          - memory.md#mem-rte-smolagents-history
          - runtime.md#rt-rte-jaz-queue
          note: Requested handoffs retain executor/invocation objects across successor calls; no cross-run
            reload is established.
        records: *id003
        note: Requested handoffs retain executor/invocation objects across successor calls; no cross-run
          reload is established.
      - scope: Letta host conversation exports
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id004
          - memory.md#mem-obj-conversation
          note: Host JSONL exports are diagnostic retention, not restorable server state.
        records: *id004
        note: Host JSONL exports are diagnostic retention, not restorable server state.
      - scope: Letta operative core blocks, server conversation, summary checkpoint and archive
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-blocks
        - memory.md#mem-obj-conversation
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-obj-archival-memory
        note: External server state and a transient summary return are exposed, but operative retained
          substrates and replacement persistence are not established. A server DB label does not identify
          a controlled substrate.
      - scope: Additional method-specific viewers and publication consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-artifact-analysis
        note: Their implementations were not audited; further retained parts cannot be enumerated.
      records:
      - memory.md#mem-obj-playbook
      - memory.md#mem-obj-playbook-counts
      - memory.md#mem-obj-adaptation-artifacts
      - epistemic.md#epi-obj-task-verdict
      - memory.md#mem-rte-jaz-history
      - memory.md#mem-rte-smolagents-history
      - runtime.md#rt-rte-jaz-queue
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-memory-blocks
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-obj-archival-memory
      - memory.md#mem-rte-artifact-analysis
      note: Positive local classifications coexist with the unresolved included alternatives named below;
        no complete system inventory or observed operation is asserted.
    representational_form:
      assessment: partial
      units:
      - scope: ACE advice at model readers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id005
          - memory.md#mem-obj-playbook
          - runtime.md#rt-rte-ace-adaptation
          note: Solver and adaptation models interpret advice text.
        records: *id005
        note: Solver and adaptation models interpret advice text.
      - scope: ACE IDs, section/count syntax and diagnostic accounting at code consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id006
          - memory.md#mem-obj-playbook-counts
          - memory.md#mem-obj-adaptation-artifacts
          note: Localized fields are parsed or counted; counters are stripped before ordinary model delivery.
        records: *id006
        note: Localized fields are parsed or counted; counters are stripped before ordinary model delivery.
      - scope: ACE trajectory and call bodies at adaptation and diagnostic consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id007
          - memory.md#mem-obj-adaptation-artifacts
          note: Trace bodies mix interpreted prose and executable/code/tool structure.
        - value: symbolic
          basis: wired
          records: *id007
          note: Trace bodies mix interpreted prose and executable/code/tool structure.
        records: *id007
        note: Trace bodies mix interpreted prose and executable/code/tool structure.
      - scope: Retained task verdicts at reporting consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id008
          - epistemic.md#epi-obj-task-verdict
          note: Numeric/Boolean fields and assertion/reason text are separate operative parts.
        - value: natural-language
          basis: wired
          records: *id008
          note: Numeric/Boolean fields and assertion/reason text are separate operative parts.
        records: *id008
        note: Numeric/Boolean fields and assertion/reason text are separate operative parts.
      - scope: Forwarded JAZ/smolagents raw histories and derived summaries/helpers
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records: &id009
          - memory.md#mem-rte-jaz-history
          - memory.md#mem-rte-smolagents-history
          - runtime.md#rt-rte-jaz-queue
          note: History code and wrapper operations are symbolic; trace prose and progress/guidance text
            require interpretation. Payload and display suffix are not interchangeable.
        - value: symbolic
          basis: afforded
          records: *id009
          note: History code and wrapper operations are symbolic; trace prose and progress/guidance text
            require interpretation. Payload and display suffix are not interchangeable.
        records: *id009
        note: History code and wrapper operations are symbolic; trace prose and progress/guidance text
          require interpretation. Payload and display suffix are not interchangeable.
      - scope: Letta configured block text and task-message bodies
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id010
          - memory.md#mem-obj-memory-blocks
          - memory.md#mem-obj-conversation
          note: Textual seams are inspectable; roles and identifiers are symbolic structure.
        - value: symbolic
          basis: wired
          records: *id010
          note: Textual seams are inspectable; roles and identifiers are symbolic structure.
        records: *id010
        note: Textual seams are inspectable; roles and identifiers are symbolic structure.
      - scope: Letta summarizer produced text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id011
          - memory.md#mem-obj-compaction-summary
          note: Only the non-streaming production seam is inspected, not its retained installation.
        records: *id011
        note: Only the non-streaming production seam is inspected, not its retained installation.
      - scope: Letta archive payload and optional dense search state
        assessment: partial
        findings:
        - value: parametric
          basis: claimed
          records:
          - memory.md#mem-obj-archival-memory
          note: Adapter describes embeddings for archival writes/queries; this is not an inspected retained
            vector store.
        records:
        - memory.md#mem-obj-archival-memory
        note: Dense representations are described, but raw consumed archive payload and exact index coverage
          remain opaque.
      records:
      - memory.md#mem-obj-playbook
      - runtime.md#rt-rte-ace-adaptation
      - memory.md#mem-obj-playbook-counts
      - memory.md#mem-obj-adaptation-artifacts
      - epistemic.md#epi-obj-task-verdict
      - memory.md#mem-rte-jaz-history
      - memory.md#mem-rte-smolagents-history
      - runtime.md#rt-rte-jaz-queue
      - memory.md#mem-obj-memory-blocks
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-obj-archival-memory
      note: Positive local classifications coexist with the unresolved included alternatives named below;
        no complete system inventory or observed operation is asserted.
    lineage:
      assessment: partial
      units:
      - scope: ACE advice derivation and initial seed provenance
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-ace-adaptation
          - memory.md#mem-obj-playbook
          note: Task trajectories and returned feedback feed admitted advice.
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-playbook
          note: An optional file seed is loaded; loading does not establish its original author.
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-rte-playbook-dedup
          note: Retained bullets feed optional computational replacement; this does not establish synthesis
            of new claims.
        records:
        - memory.md#mem-obj-playbook
        - runtime.md#rt-rte-ace-adaptation
        - memory.md#mem-rte-playbook-dedup
        note: Trace-conditioned ADDs and rewrites are known paths; seed authorship and particular model
          semantic derivations remain unresolved.
      - scope: ACE stored counters and diagnostic trace records
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id012
          - memory.md#mem-obj-playbook-counts
          - memory.md#mem-obj-adaptation-artifacts
          note: Code initializes counters and records activity; these are not measured helpfulness.
        - value: trace-extracted
          basis: wired
          records: *id012
          note: Code initializes counters and records activity; these are not measured helpfulness.
        records: *id012
        note: Code initializes counters and records activity; these are not measured helpfulness.
      - scope: Task verdicts imported from grader then retained
        assessment: known
        findings:
        - value: imported
          basis: wired
          records: &id013
          - epistemic.md#epi-obj-task-verdict
          note: Outcome content originates at environment/grader seams; its upstream warrant is unresolved.
        records: *id013
        note: Outcome content originates at environment/grader seams; its upstream warrant is unresolved.
      - scope: JAZ/smolagents passed traces and authored progress/guidance
        assessment: known
        findings:
        - value: trace-extracted
          basis: afforded
          records: &id014
          - memory.md#mem-rte-jaz-history
          - memory.md#mem-rte-smolagents-history
          - runtime.md#rt-rte-jaz-queue
          note: Model-directed procedures retain experience and derive reusable text or helpers; compliance
            is unobserved.
        records: *id014
        note: Model-directed procedures retain experience and derive reusable text or helpers; compliance
          is unobserved.
      - scope: Letta core-block initialization and task-message acquisition
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-memory-blocks
          - memory.md#mem-obj-conversation
          note: Adapter supplies configured blocks and selected environment task text.
        records:
        - memory.md#mem-obj-memory-blocks
        - memory.md#mem-obj-conversation
        note: Configured text and environment messages enter the server; original block authorship and
          further server derivations remain unknown.
      - scope: Letta archive, summary input selection and optional embedding provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-obj-archival-memory
        - memory.md#mem-obj-conversation
        note: Summary generation alone does not establish the exact retained-input chain; archive and
          dense-state origins are opaque.
      records:
      - memory.md#mem-obj-playbook
      - runtime.md#rt-rte-ace-adaptation
      - memory.md#mem-rte-playbook-dedup
      - memory.md#mem-obj-playbook-counts
      - memory.md#mem-obj-adaptation-artifacts
      - epistemic.md#epi-obj-task-verdict
      - memory.md#mem-rte-jaz-history
      - memory.md#mem-rte-smolagents-history
      - runtime.md#rt-rte-jaz-queue
      - memory.md#mem-obj-memory-blocks
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-obj-archival-memory
      note: Positive local classifications coexist with the unresolved included alternatives named below;
        no complete system inventory or observed operation is asserted.
    behavioral_authority:
      assessment: partial
      units:
      - scope: ACE advice at subsequent solver and adaptation models
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id015
          - memory.md#mem-obj-playbook
          - runtime.md#rt-rte-ace-adaptation
          note: Explicitly advisory guidance supplies context, not standing mandatory directions.
        records: *id015
        note: Explicitly advisory guidance supplies context, not standing mandatory directions.
      - scope: ACE retained trajectories and feedback at reflector/curator update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id016
          - memory.md#mem-obj-adaptation-artifacts
          - runtime.md#rt-rte-ace-adaptation
          note: Recorded experience feeds durable advice updates for later solvers; improved capacity
            is not established.
        records: *id016
        note: Recorded experience feeds durable advice updates for later solvers; improved capacity is
          not established.
      - scope: ACE retained advice bodies at similarity grouping
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id017
          - memory.md#mem-rte-playbook-dedup
          note: Advice text influences similarity-based group selection for refinement.
        records: *id017
        note: Advice text influences similarity-based group selection for refinement.
      - scope: ACE retained advice at merge model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id018
          - memory.md#mem-rte-playbook-dedup
          note: Selected retained bullets supply content for replacement wording.
        records: *id018
        note: Selected retained bullets supply content for replacement wording.
      - scope: JAZ histories at root revision consumer and revised guidance/helpers at later solvers
        assessment: known
        findings:
        - value: learning
          basis: afforded
          records: &id019
          - runtime.md#rt-rte-jaz-queue
          note: Returned experience supports requested prompt/helper adaptation, and revised prompts direct
            later solvers.
        - value: instruction
          basis: afforded
          records: *id019
          note: Returned experience supports requested prompt/helper adaptation, and revised prompts direct
            later solvers.
        records: *id019
        note: Returned experience supports requested prompt/helper adaptation, and revised prompts direct
          later solvers.
      - scope: JAZ/smolagents histories and progress summaries at successors
        assessment: known
        findings:
        - value: knowledge
          basis: afforded
          records: &id020
          - memory.md#mem-rte-jaz-history
          - memory.md#mem-rte-smolagents-history
          note: Forwarded experience supplies context and advice for continuation.
        records: *id020
        note: Forwarded experience supplies context and advice for continuation.
      - scope: Retained traces and results at post-run analysis/operator
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id021
          - memory.md#mem-rte-artifact-analysis
          - epistemic.md#epi-obj-task-verdict
          note: Diagnostics expose evidence and reference information; no automatic solver update follows.
        records: *id021
        note: Diagnostics expose evidence and reference information; no automatic solver update follows.
      - scope: ACE stored helpful/harmful counters
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-playbook-counts
        note: Counts are not measured reliability and are removed from ordinary solver/adaptation input;
          no retained-count authority is established on these assessed paths.
      - scope: Letta core blocks, searchable conversation, installed summaries and archive at external
          consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-blocks
        - memory.md#mem-obj-conversation
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-obj-archival-memory
        note: Initialization and requested search do not resolve actual context force, archive ranking,
          editing vetoes or summary injection; no inferred authority from memory labels.
      records:
      - memory.md#mem-obj-playbook
      - runtime.md#rt-rte-ace-adaptation
      - memory.md#mem-obj-adaptation-artifacts
      - memory.md#mem-rte-playbook-dedup
      - runtime.md#rt-rte-jaz-queue
      - memory.md#mem-rte-jaz-history
      - memory.md#mem-rte-smolagents-history
      - memory.md#mem-rte-artifact-analysis
      - epistemic.md#epi-obj-task-verdict
      - memory.md#mem-obj-playbook-counts
      - memory.md#mem-obj-memory-blocks
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-obj-archival-memory
      note: Positive local classifications coexist with the unresolved included alternatives named below;
        no complete system inventory or observed operation is asserted.
    write_agency:
      assessment: partial
      units:
      - scope: ACE trace-to-ADD admission and optional replacement
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id022
          - runtime.md#rt-rte-ace-adaptation
          - memory.md#mem-rte-playbook-dedup
          note: Models propose and software admits without per-content human approval.
        records: *id022
        note: Models propose and software admits without per-content human approval.
      - scope: ACE seed admission decision
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-playbook
        note: Configured file supply identifies neither human approval nor the controlling principal;
          the read is not evidence of manual writing.
      - scope: ACE diagnostics and retained verdict recording
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id023
          - memory.md#mem-obj-adaptation-artifacts
          - epistemic.md#epi-obj-task-verdict
          note: Code records activity and outcomes without per-record operator approval.
        records: *id023
        note: Code records activity and outcomes without per-record operator approval.
      - scope: JAZ/smolagents trace collection, progress summaries and guidance revision
        assessment: known
        findings:
        - value: automatic
          basis: afforded
          records: &id024
          - memory.md#mem-rte-jaz-history
          - memory.md#mem-rte-smolagents-history
          - runtime.md#rt-rte-jaz-queue
          note: Model-mediated subsequent content decisions are computational, not human per-change approval.
        records: *id024
        note: Model-mediated subsequent content decisions are computational, not human per-change approval.
      - scope: Letta task-message delivery and host exports
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id025
          - memory.md#mem-obj-conversation
          note: Software selects new task text or substitutes nudges and exports diagnostics.
        records: *id025
        note: Software selects new task text or substitutes nudges and exports diagnostics.
      - scope: Letta initial block approval and subsequent memory/archive/checkpoint admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-blocks
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-obj-archival-memory
        note: Configuration does not reveal per-content approval; server edit and installation controls
          remain opaque.
      records:
      - runtime.md#rt-rte-ace-adaptation
      - memory.md#mem-rte-playbook-dedup
      - memory.md#mem-obj-playbook
      - memory.md#mem-obj-adaptation-artifacts
      - epistemic.md#epi-obj-task-verdict
      - memory.md#mem-rte-jaz-history
      - memory.md#mem-rte-smolagents-history
      - runtime.md#rt-rte-jaz-queue
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-memory-blocks
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-obj-archival-memory
      note: Positive local classifications coexist with the unresolved included alternatives named below;
        no complete system inventory or observed operation is asserted.
    curation_operations:
      assessment: partial
      units:
      - scope: ACE merge-free similarity refinement
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records: &id026
          - memory.md#mem-rte-playbook-dedup
          note: Retain first bullet and remove selected nonleaders; similarity does not establish semantic
            equivalence.
        records: *id026
        note: Retain first bullet and remove selected nonleaders; similarity does not establish semantic
          equivalence.
      - scope: ACE model-merge replacement application
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id027
          - memory.md#mem-rte-playbook-dedup
          note: Code replaces a prior bullet and absorbs selected members when parsing succeeds.
        - value: dedup
          basis: wired
          records: *id027
          note: Code replaces a prior bullet and absorbs selected members when parsing succeeds.
        records: *id027
        note: Code replaces a prior bullet and absorbs selected members when parsing succeeds.
      - scope: ACE model-merge content compression
        assessment: known
        findings:
        - value: consolidate
          basis: afforded
          records: &id028
          - memory.md#mem-rte-playbook-dedup
          note: Prompt affords combining existing advice into one reduced representation; fidelity is
            unobserved.
        records: *id028
        note: Prompt affords combining existing advice into one reduced representation; fidelity is unobserved.
      - scope: ACE trace-to-advice semantic transformation
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-ace-adaptation
        - memory.md#mem-obj-adaptation-artifacts
        note: Trace-conditioned advice is installed, but no generated output settles reduction of existing
          claims versus a new claim. Novelty requests alone establish no synthesis.
      - scope: JAZ/smolagents continuation summaries
        assessment: known
        findings:
        - value: consolidate
          basis: afforded
          records: &id029
          - memory.md#mem-rte-jaz-history
          - memory.md#mem-rte-smolagents-history
          note: Requested progress summaries compress recorded experience into successor context.
        records: *id029
        note: Requested progress summaries compress recorded experience into successor context.
      - scope: JAZ reusable prompt/helper revisions
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records: &id030
          - runtime.md#rt-rte-jaz-queue
          note: Root is asked to revise or discard ineffective guidance; no generated revision proves
            operation.
        records: *id030
        note: Root is asked to revise or discard ineffective guidance; no generated revision proves operation.
      - scope: Letta summary transformation and archive/core maintenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-blocks
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-obj-archival-memory
        note: Produced summary text does not reveal input selection or installed transformation; archive
          maintenance is opaque.
      - scope: Additional publication/viewer transformations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-artifact-analysis
        note: Record coverage explicitly leaves viewer/release/plot implementations unaudited.
      records:
      - memory.md#mem-rte-playbook-dedup
      - runtime.md#rt-rte-ace-adaptation
      - memory.md#mem-obj-adaptation-artifacts
      - memory.md#mem-rte-jaz-history
      - memory.md#mem-rte-smolagents-history
      - runtime.md#rt-rte-jaz-queue
      - memory.md#mem-obj-memory-blocks
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-obj-archival-memory
      - memory.md#mem-rte-artifact-analysis
      note: Positive local classifications coexist with the unresolved included alternatives named below;
        no complete system inventory or observed operation is asserted.
    read_back_direction:
      assessment: partial
      units:
      - scope: ACE live advice to later solver/reflector/curator prompts
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id031
          - memory.md#mem-obj-playbook
          - runtime.md#rt-rte-ace-adaptation
          note: Driver automatically supplies all current count-stripped advice on later rounds.
        records: *id031
        note: Driver automatically supplies all current count-stripped advice on later rounds.
      - scope: ACE optional snapshot/seed request
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id032
          - memory.md#mem-obj-playbook
          note: Explicit initial_playbook configuration requests file content; loading is not a second
            automatic targeted push.
        records: *id032
        note: Explicit initial_playbook configuration requests file content; loading is not a second automatic
          targeted push.
      - scope: JAZ/smolagents successor handoff and requested hit windows
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records: &id033
          - memory.md#mem-rte-jaz-history
          - memory.md#mem-rte-smolagents-history
          note: Foreground model explicitly forwards and searches retained history; returned windows fulfill
            those requests.
        records: *id033
        note: Foreground model explicitly forwards and searches retained history; returned windows fulfill
          those requests.
      - scope: JAZ revised prompt/helpers supplied to later solver calls
        assessment: known
        findings:
        - value: push
          basis: afforded
          records: &id034
          - runtime.md#rt-rte-jaz-queue
          note: Root selects revised guidance for later delegates without those delegates requesting retained
            material.
        records: *id034
        note: Root selects revised guidance for later delegates without those delegates requesting retained
          material.
      - scope: Operator requested retained-artifact analysis
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id035
          - memory.md#mem-rte-artifact-analysis
          note: Explicit file/attempt/run path requests diagnostic consumption.
        records: *id035
        note: Explicit file/attempt/run path requests diagnostic consumption.
      - scope: Letta conversational recall request
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records: &id036
          - memory.md#mem-obj-conversation
          note: Prompt affords targeted conversation_search on retained messages.
        records: *id036
        note: Prompt affords targeted conversation_search on retained messages.
      - scope: Letta core-block context supply, summary insertion and archive retrieval alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-blocks
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-obj-archival-memory
        note: Exact automatic delivery and request boundaries remain external; a known conversation-search
          request does not resolve these alternatives.
      records:
      - memory.md#mem-obj-playbook
      - runtime.md#rt-rte-ace-adaptation
      - memory.md#mem-rte-jaz-history
      - memory.md#mem-rte-smolagents-history
      - runtime.md#rt-rte-jaz-queue
      - memory.md#mem-rte-artifact-analysis
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-memory-blocks
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-obj-archival-memory
      note: Positive local classifications coexist with the unresolved included alternatives named below;
        no complete system inventory or observed operation is asserted.
    read_back_signal:
      assessment: partial
      units:
      - scope: ACE automatic advice supply
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id037
          - memory.md#mem-obj-playbook
          - runtime.md#rt-rte-ace-adaptation
          note: Each later prompt triggers inclusion; selector input is current playbook availability,
            and selected retained part is all advice after count removal, not task-keyed retrieval.
        records: *id037
        note: Each later prompt triggers inclusion; selector input is current playbook availability, and
          selected retained part is all advice after count removal, not task-keyed retrieval.
      - scope: JAZ root selection of revised guidance/helpers for later delegates
        assessment: known
        findings:
        - value: inferred-judgment
          basis: afforded
          records: &id038
          - runtime.md#rt-rte-jaz-queue
          note: Later batch delegation triggers root choice of current prompt/helper material from history-based
            diagnosis; model judgment selects delivered revisions.
        records: *id038
        note: Later batch delegation triggers root choice of current prompt/helper material from history-based
          diagnosis; model judgment selects delivered revisions.
      - scope: Explicit seed, history search, operator analysis and Letta conversation-search request
          returns
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-playbook
        - memory.md#mem-rte-jaz-history
        - memory.md#mem-rte-smolagents-history
        - memory.md#mem-rte-artifact-analysis
        - memory.md#mem-obj-conversation
        note: These operations fulfill explicit requests, not unsolicited push. Substring matching in
          requested recall is not a push signal.
      - scope: Letta potential core/summary/archive push selectors
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-blocks
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-obj-archival-memory
        note: Trigger, selection inputs and selected retained payload are not established; no identifier
          signal follows from labels alone.
      records:
      - memory.md#mem-obj-playbook
      - runtime.md#rt-rte-ace-adaptation
      - runtime.md#rt-rte-jaz-queue
      - memory.md#mem-rte-jaz-history
      - memory.md#mem-rte-smolagents-history
      - memory.md#mem-rte-artifact-analysis
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-memory-blocks
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-obj-archival-memory
      note: Positive local classifications coexist with the unresolved included alternatives named below;
        no complete system inventory or observed operation is asserted.
    trace_learning:
      assessment: partial
      units:
      - scope: ACE automatic trajectory/feedback to retained advice to later solver
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id039
          - runtime.md#rt-rte-ace-adaptation
          - memory.md#mem-obj-adaptation-artifacts
          - memory.md#mem-obj-playbook
          note: Code admits trace-conditioned advice, carries live state and snapshots, and supplies later
            prompts. No observed benefit is required for this wired route.
        records: *id039
        note: Code admits trace-conditioned advice, carries live state and snapshots, and supplies later
          prompts. No observed benefit is required for this wired route.
      - scope: JAZ trace-responsive guidance/helper update and continuation summaries
        assessment: known
        findings:
        - value: 'yes'
          basis: afforded
          records: &id040
          - runtime.md#rt-rte-jaz-queue
          - memory.md#mem-rte-jaz-history
          note: Model-directed writes retain trace-derived guidance or progress for later invocations;
            actual artifacts and compliance are unavailable.
        records: *id040
        note: Model-directed writes retain trace-derived guidance or progress for later invocations; actual
          artifacts and compliance are unavailable.
      - scope: smolagents trace-derived retained continuation summary
        assessment: known
        findings:
        - value: 'yes'
          basis: afforded
          records: &id041
          - memory.md#mem-rte-smolagents-history
          note: Requested progress summary from recorded activity enters child context; warning alone
            does not establish execution.
        records: *id041
        note: Requested progress summary from recorded activity enters child context; warning alone does
          not establish execution.
      - scope: Letta summary and archive/core update alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-memory-blocks
        - memory.md#mem-obj-conversation
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-obj-archival-memory
        note: Summary production seam lacks established source selection, retained installation and later
          consumer; archive writes remain opaque. No local negative is inferred.
      - scope: Diagnostic/viewer paths beyond inspected analysis dispatch
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-artifact-analysis
        note: Recording raw logs alone does not qualify; unaudited consumers prevent a complete negative
          about additional trace-fed adaptation.
      records:
      - runtime.md#rt-rte-ace-adaptation
      - memory.md#mem-obj-adaptation-artifacts
      - memory.md#mem-obj-playbook
      - runtime.md#rt-rte-jaz-queue
      - memory.md#mem-rte-jaz-history
      - memory.md#mem-rte-smolagents-history
      - memory.md#mem-obj-memory-blocks
      - memory.md#mem-obj-conversation
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-obj-archival-memory
      - memory.md#mem-rte-artifact-analysis
      note: Positive local classifications coexist with the unresolved included alternatives named below;
        no complete system inventory or observed operation is asserted.
    trace_source:
      assessment: partial
      units:
      - scope: ACE solver-session trajectory input
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id042
          - memory.md#mem-obj-adaptation-artifacts
          - runtime.md#rt-rte-ace-adaptation
          note: Recorded agent-session activity feeds reflection and advice admission.
        records: *id042
        note: Recorded agent-session activity feeds reflection and advice admission.
      - scope: ACE tool execution, exception and evaluation feedback input
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id043
          - memory.md#mem-obj-adaptation-artifacts
          - runtime.md#rt-rte-ace-adaptation
          note: Tool/code execution feedback in the trajectory and completion reports feeds the same update.
        records: *id043
        note: Tool/code execution feedback in the trajectory and completion reports feeds the same update.
      - scope: JAZ trace-responsive guidance and continuation summaries
        assessment: known
        findings:
        - value: session-logs
          basis: afforded
          records: &id044
          - runtime.md#rt-rte-jaz-queue
          - memory.md#mem-rte-jaz-history
          note: Native histories or requested code/output/exception lists record session work and tool
            execution.
        - value: tool-traces
          basis: afforded
          records: *id044
          note: Native histories or requested code/output/exception lists record session work and tool
            execution.
        records: *id044
        note: Native histories or requested code/output/exception lists record session work and tool execution.
      - scope: smolagents continuation summaries
        assessment: known
        findings:
        - value: session-logs
          basis: afforded
          records: &id045
          - memory.md#mem-rte-smolagents-history
          note: Self-recorded session output/code and prior activity feed requested progress context.
        - value: tool-traces
          basis: afforded
          records: *id045
          note: Self-recorded session output/code and prior activity feed requested progress context.
        records: *id045
        note: Self-recorded session output/code and prior activity feed requested progress context.
      - scope: Letta potential qualifying summary/archive writes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-obj-archival-memory
        - memory.md#mem-obj-conversation
        note: Original inputs and complete qualifying later-consumer chain remain unresolved; event-stream
          or trajectory labels are not inferred from serialization.
      - scope: Unaudited additional diagnostic consumers
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-artifact-analysis
        note: Without a qualifying write/consumer inventory, additional original trace inputs cannot be
          classified.
      records:
      - memory.md#mem-obj-adaptation-artifacts
      - runtime.md#rt-rte-ace-adaptation
      - runtime.md#rt-rte-jaz-queue
      - memory.md#mem-rte-jaz-history
      - memory.md#mem-rte-smolagents-history
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-obj-archival-memory
      - memory.md#mem-obj-conversation
      - memory.md#mem-rte-artifact-analysis
      note: Positive local classifications coexist with the unresolved included alternatives named below;
        no complete system inventory or observed operation is asserted.
---

# jaz-evals memory profile

## Comparison rationale

All ten axes are partial. The accepted records establish real advice delivery and diagnostic read-back, but do not enumerate external Letta memory internals or unaudited publication consumers. A known wired ACE witness cannot resolve those alternatives. The profile classifies implementation and afforded model-mediated routes, not exercised learning or improved outcomes.

ACE has distinct operative parts. Advice is interpreted natural language; counts and IDs are symbolic. Counts do not establish reliability weighting or ranking. Advice bodies do influence similarity grouping, so they have ranking authority at that consumer. Recorded trajectories have learning authority at the update consumer, while the resulting advisory playbook has knowledge authority at the solver. This does not make advice mandatory instruction or make static parser rules retained validation memory. See [MEM-OBJ-playbook](memory.md#mem-obj-playbook), [MEM-OBJ-playbook-counts](memory.md#mem-obj-playbook-counts), [MEM-RTE-playbook-dedup](memory.md#mem-rte-playbook-dedup) and [RT-RTE-ace-adaptation](runtime.md#rt-rte-ace-adaptation).

Similarity refinement supports deduplication and replacement, including the merge-free branch. Model merging affords consolidation but establishes neither semantic fidelity nor synthesis of a new claim. Trace-conditioned ADDs likewise do not settle the semantic relation of particular advice to its inputs. No generated example supports a stronger transformation classification. See [EPI-RTE-dedup-replacement](epistemic.md#epi-rte-dedup-replacement) and [MEM-RTE-playbook-dedup](memory.md#mem-rte-playbook-dedup).

ACE prompt supply is coarse push: all current advice is inserted automatically. Optional seed loading, foreground history searches and operator analysis fulfill explicit requests. Identifier-bearing paths and substring searches on those pull operations are not identifier or lexical push. JAZ root-authored revisions have a separate afforded judgment-selected push to subsequent delegates. See [MEM-OBJ-playbook](memory.md#mem-obj-playbook), [MEM-RTE-jaz-history](memory.md#mem-rte-jaz-history), [MEM-RTE-smolagents-history](memory.md#mem-rte-smolagents-history) and [RT-RTE-jaz-queue](runtime.md#rt-rte-jaz-queue).

Requested continuation summaries qualify locally as trace learning because model-authored trace-derived context is retained for a successor, even without a new claim or demonstrated improvement. The smolagents wrapper display suffix does not classify the complete payload as a summary. Letta's inspected summary return does not establish its retention or injection; that route remains unresolved, not negative. Optional dense archive representations have only the adapter's descriptive warrant, not a wired vector-store classification. See [MEM-RTE-smolagents-history](memory.md#mem-rte-smolagents-history), [MEM-OBJ-compaction-summary](memory.md#mem-obj-compaction-summary) and [MEM-OBJ-archival-memory](memory.md#mem-obj-archival-memory).

The reconciliation supersedes EPI-RTE-analysis-report with [MEM-RTE-artifact-analysis](memory.md#mem-rte-artifact-analysis); all diagnostic classifications use the latter. Advice/count objects and the combined playbook container remain valid separately, as do grouping and replacement subroutes. No supersession strengthens evidence or converts structural admission into epistemic acceptance.

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no source ambiguity required a new read. Missing initialization control prevents a manual-write classification; missing external consumer and installation facts prevent complete authority, curation, read-back and trace-learning assessments. No bounded absence record licenses a system-wide negative.
