---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Voyager memory profile: retained skills and indexes, QA, chest/progress state, event replay
  and within-bot encounter memory at the frozen revision.'
run-id: AAS-2026-10-14-voyager-f16a44a0cfe3-01
source-identity: https://github.com/MineDojo/Voyager
reviewed-boundary: 55e45a880755d0c8c66ca7fb5fe7962ac8974f89
memory-comparison:
  version: 2
  scope: Active and archived retained skill code/descriptions, skill and QA access indexes, cached answers,
    chest maps, task histories, event archive/replay accounting, and encountered-block memory; includes
    checkpoint/library reload alternatives and their unresolved historical provenance. Working-frame replacement
    is assessed only where it carries accumulated memory to later invocations. Excludes shipped static
    prompts/primitives, external model weights as producer components, ordinary current-step payloads,
    and transient executor/plugin queues without an established retained-memory consumer.
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Active skill code and descriptions, including loaded checkpoints and versioned archives
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id001
          - memory.md#mem-obj-skills-code
          - memory.md#mem-obj-skill-description
          - runtime.md#rt-rte-skill-admission
          note: JSON, JavaScript and description files retain content across reloads.
        - value: in-memory
          basis: wired
          records: *id001
          note: Loaded active entries reside in the manager map.
        records: *id001
        note: Active entries have Python maps and JSON backing; code/description archives are separate
          files, not a repository write route.
      - scope: Skill description documents, name metadata and dense access vectors
        assessment: known
        findings:
        - value: vector
          basis: wired
          records: &id002
          - memory.md#mem-obj-skill-vectordb
          - memory.md#mem-rte-skill-retrieval
          note: The persisted description collection is queried by similarity.
        - value: files
          basis: wired
          records: *id002
          note: The collection is persisted under skill/vectordb.
        records: *id002
        note: Chroma persistence is a vector access structure with local disk backing; binary trial files
          were not decoded.
      - scope: QA answer map and question index
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id003
          - memory.md#mem-obj-qa-cache
          - memory.md#mem-obj-qa-questions
          - memory.md#mem-rte-qa-cache
          note: QA JSON and local index persistence are named.
        - value: in-memory
          basis: wired
          records: *id003
          note: QA answers are loaded into a Python map.
        - value: vector
          basis: wired
          records: *id003
          note: Question vectors support nearest-question reuse.
        records: *id003
        note: Answers have map/JSON storage; the separate question index has Chroma persistence. No rdbms/sqlite
          implementation is inferred from an unfrozen dependency.
      - scope: Chest maps and completed/failed task histories
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id004
          - memory.md#mem-obj-chest-memory
          - memory.md#mem-obj-task-histories
          - memory.md#mem-rte-chest-update
          - memory.md#mem-rte-progress-update
          note: JSON retains chest and history content for resume.
        - value: in-memory
          basis: wired
          records: *id004
          note: Python maps and lists supply current consumers.
        records: *id004
        note: These checkpoint-backed objects have both operative in-memory and file parts.
      - scope: Raw event archive and reconstructed recorder accounting
        assessment: known
        findings:
        - value: files
          basis: wired
          records: &id005
          - memory.md#mem-obj-events
          - memory.md#mem-rte-event-replay
          note: Task/timestamp JSON files retain events.
        - value: in-memory
          basis: wired
          records: *id005
          note: Replay reconstructs iteration, item/time and position summaries.
        records: *id005
        note: Persisted raw events and derived in-memory summaries are distinct parts.
      - scope: Encountered-block set within one bot lifetime
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id006
          - memory.md#mem-obj-block-records
          note: BlockRecords.records is a JavaScript Set.
        records: *id006
        note: The recorded Set spans observations, but no disk reload is established.
      records:
      - memory.md#mem-obj-skills-code
      - memory.md#mem-obj-skill-description
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-obj-skill-vectordb
      - memory.md#mem-rte-skill-retrieval
      - memory.md#mem-obj-qa-cache
      - memory.md#mem-obj-qa-questions
      - memory.md#mem-rte-qa-cache
      - memory.md#mem-obj-chest-memory
      - memory.md#mem-obj-task-histories
      - memory.md#mem-rte-chest-update
      - memory.md#mem-rte-progress-update
      - memory.md#mem-obj-events
      - memory.md#mem-rte-event-replay
      - memory.md#mem-obj-block-records
      note: The recorded object inventory covers active/archived skills, both indexes, QA, chests, histories,
        event files/replay summaries and within-bot block memory. Opaque trial payloads have known file/access
        locations, not known contents. External models are producer components, not a Voyager memory store
        changed through use.
    representational_form:
      assessment: partial
      units:
      - scope: Skill implementation at Node execution and code-example consumption
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id007
          - memory.md#mem-obj-skills-code
          - runtime.md#rt-bap-skill-execution
          - memory.md#mem-rte-skill-retrieval
          note: JavaScript definitions have fixed execution semantics.
        - value: natural-language
          basis: wired
          records: *id007
          note: The action model interprets retrieved code as advisory example context rather than executing
            it in its prompt.
        records: *id007
        note: Executable declarations are symbolic at Node; the same retained code is interpreted as an
          example by the action model.
      - scope: Description and QA question/answer text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id008
          - memory.md#mem-obj-skill-description
          - memory.md#mem-obj-qa-cache
          - memory.md#mem-obj-qa-questions
          note: Descriptions characterize functions; questions and answers convey Minecraft advice.
        records: *id008
        note: Function/comment wrappers and exact-key access are separated below from the natural-language
          content.
      - scope: Skill and QA index identifiers, wrappers and exact cache-key operations
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id009
          - memory.md#mem-obj-skill-vectordb
          - memory.md#mem-obj-qa-questions
          - memory.md#mem-obj-qa-cache
          - memory.md#mem-obj-skill-description
          note: Names and question equality select map entries; display wrappers are structured strings.
        records: *id009
        note: These localized keys/wrappers have fixed lookup or formatting roles, not dense meaning.
      - scope: New description/question embeddings produced through the inspected index routes
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records: &id010
          - memory.md#mem-obj-skill-vectordb
          - memory.md#mem-obj-qa-questions
          - memory.md#mem-rte-qa-cache
          - runtime.md#rt-rte-skill-admission
          note: The records explicitly identify distributed-parametric numerical access representations.
        records: *id010
        note: Dense access representations are distinct from external embedding model weights.
      - scope: Chest maps, task membership/count/order, recorder event structures/accounting and encountered-block
          Set
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id011
          - memory.md#mem-obj-chest-memory
          - memory.md#mem-obj-task-histories
          - memory.md#mem-obj-events
          - memory.md#mem-obj-block-records
          note: Position/item maps, task membership/counts, event fields, metrics and set membership are
            symbolic state.
        records: *id011
        note: Each named control/observation part has localized keys and fixed consumer rules.
      - scope: Rendered chest reports, task labels/history context and embedded event chat/error text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id012
          - memory.md#mem-obj-chest-memory
          - memory.md#mem-obj-task-histories
          - memory.md#mem-obj-events
          - memory.md#mem-rte-chest-update
          - memory.md#mem-rte-progress-update
          note: Models interpret chest reports and task histories; events also carry chat/error text.
        records: *id012
        note: This unit covers interpreted text rather than the symbolic membership/control uses of the
          same objects.
      - scope: Other shipped trial code/description/JSON and undecoded binary index payload contents
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-skills-code
        - memory.md#mem-obj-skill-vectordb
        note: Loader expectations and one sample do not classify every opaque consumed payload. Exact
          historical representations and mixed content remain uninspected.
      records:
      - memory.md#mem-obj-skills-code
      - runtime.md#rt-bap-skill-execution
      - memory.md#mem-rte-skill-retrieval
      - memory.md#mem-obj-skill-description
      - memory.md#mem-obj-qa-cache
      - memory.md#mem-obj-qa-questions
      - memory.md#mem-obj-skill-vectordb
      - memory.md#mem-rte-qa-cache
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-obj-chest-memory
      - memory.md#mem-obj-task-histories
      - memory.md#mem-obj-events
      - memory.md#mem-obj-block-records
      - memory.md#mem-rte-chest-update
      - memory.md#mem-rte-progress-update
      note: Inspected producer/consumer paths distinguish text, symbolic state/code and dense numerical
        access representations. Undecoded shipped payloads prevent a complete content/form inventory for
        those alternatives.
    lineage:
      assessment: partial
      units:
      - scope: Successful action program copied to retained skills
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id013
          - memory.md#mem-obj-skills-code
          - runtime.md#rt-rte-skill-admission
          note: Task activity and outcome select the program retained for later model/executor use.
        records: *id013
        note: Learning admission uses the program from an executed task judged successful; it is not a
          model-weight update.
      - scope: New skill descriptions derived from admitted program code
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id014
          - memory.md#mem-obj-skill-description
          - epistemic.md#epi-rte-skill-description
          - runtime.md#rt-rte-skill-admission
          note: The description is generated from code rather than copied as a raw trace.
        records: *id014
        note: A separate model summarizes code/main name. Semantic faithfulness is unresolved; the derivation
          route itself is wired.
      - scope: New dense skill-description and QA-question index outputs
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id015
          - memory.md#mem-obj-skill-vectordb
          - memory.md#mem-obj-qa-questions
          - runtime.md#rt-rte-skill-admission
          - memory.md#mem-rte-qa-cache
          note: Embedding/index construction derives numerical access material from text.
        records: *id015
        note: The embedding calls establish compilation to access representations, not exact service/version
          provenance.
      - scope: New QA answers generated on cache misses
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-qa-cache
        - memory.md#mem-rte-qa-cache
        note: The model supplies answers from its own Minecraft knowledge. Provider-internal source provenance
          is not exposed; trace-extracted versus authored/imported content origin cannot be established.
      - scope: Chest maps, task outcome histories and encountered-block memory derived during activity
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id016
          - memory.md#mem-rte-chest-update
          - memory.md#mem-rte-progress-update
          - memory.md#mem-obj-block-records
          note: Activity reports become chest state, outcome histories and block encounter sets.
        records: *id016
        note: Environmental encounters and task results drive these retained summaries; initial checkpoint
          origin is separate.
      - scope: Raw recorder files
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id017
          - memory.md#mem-obj-events
          - memory.md#mem-rte-event-replay
          note: Execution/observation events are retained as raw traces.
        records: *id017
        note: The recorder serializes returned environment activity rather than authoring a new explanation.
      - scope: Recorder summaries reconstructed from retained event files
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id018
          - memory.md#mem-obj-events
          - memory.md#mem-rte-event-replay
          note: Replay rebuilds counts, histories and elapsed-time/position metrics.
        records: *id018
        note: Chronological replay deterministically derives accounting from the raw archive.
      - scope: Checkpoint/library loading of skills, QA and other saved state
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records: &id019
          - memory.md#mem-obj-skills-code
          - memory.md#mem-obj-qa-cache
          - memory.md#mem-rte-chest-update
          - memory.md#mem-rte-progress-update
          - memory.md#mem-rte-event-replay
          note: Constructors/resume load existing saved content, including a separately selected skill
            library.
        records: *id019
        note: Import into a resumed/new invocation is known, but original authorship, admission and historical
          trace derivation remain unresolved.
      - scope: Historical embeddings and unsampled shipped-library production paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-skill-vectordb
        - memory.md#mem-obj-skills-code
        - memory.md#mem-obj-qa-questions
        note: The payloads and original runs were not inspected; their earlier derivation and embedding
          identities cannot be assigned from the live producer route.
      records:
      - memory.md#mem-obj-skills-code
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-obj-skill-description
      - epistemic.md#epi-rte-skill-description
      - memory.md#mem-obj-skill-vectordb
      - memory.md#mem-obj-qa-questions
      - memory.md#mem-rte-qa-cache
      - memory.md#mem-obj-qa-cache
      - memory.md#mem-rte-chest-update
      - memory.md#mem-rte-progress-update
      - memory.md#mem-obj-block-records
      - memory.md#mem-obj-events
      - memory.md#mem-rte-event-replay
      note: Live derivation paths are known. Loading a checkpoint establishes import into this invocation,
        not historical authorship, approval, training provenance or embedding identity.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retrieved retained code at the action model
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id020
          - memory.md#mem-rte-skill-retrieval
          - memory.md#mem-obj-skills-code
          note: Selected code supplies reference examples for generating another action.
        records: *id020
        note: The model receives examples as context; these are not an access-control policy.
      - scope: All active retained code definitions at Node eval
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id021
          - runtime.md#rt-bap-skill-execution
          - memory.md#mem-obj-skills-code
          note: Retained executable definitions direct execution when called, rather than merely describing
            capabilities.
        records: *id021
        note: Symbolic executable directions enter the programs field. Actual function invocation is conditional;
          definition supply is not enforced primitive-only behavior.
      - scope: Description text/vectors/name metadata and QA question index at similarity selection
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records: &id022
          - memory.md#mem-obj-skill-vectordb
          - memory.md#mem-obj-qa-questions
          - memory.md#mem-rte-skill-retrieval
          - memory.md#mem-rte-qa-cache
          note: Description/question content and vectors determine which retained code or cached answer
            is selected.
        records: *id022
        note: Retained access representations affect relative retrieval priority; no learned ranking policy
          is required.
      - scope: QA answers at curriculum/action context consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id023
          - memory.md#mem-obj-qa-cache
          - memory.md#mem-rte-qa-cache
          note: Cached answers supply Minecraft context to task/action generation.
        records: *id023
        note: Candidate advice is not an expected-result key or validated oracle.
      - scope: Chest map at model renderers and hardcoded inventory-management selection
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id024
          - memory.md#mem-rte-chest-update
          - memory.md#mem-obj-chest-memory
          note: Rendered chest state informs action, curriculum and critic judgments.
        - value: routing
          basis: wired
          records: *id024
          note: Chest state can trigger/select deposit-related task handling.
        records: *id024
        note: The map has different effects at its two consumers.
      - scope: Task history text at curriculum planning
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id025
          - memory.md#mem-obj-task-histories
          - memory.md#mem-rte-progress-update
          note: Completed/failed task strings inform subsequent curriculum proposals.
        records: *id025
        note: Judgment-derived labels are contextual evidence, not independent competence proofs.
      - scope: Task-history count at disclosure, difficulty and inference sequencing
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id026
          - memory.md#mem-rte-progress-update
          - memory.md#mem-obj-task-histories
          - runtime.md#rt-rte-task-inference
          note: Progress controls warmup disclosure, difficulty and next-subgoal index.
        records: *id026
        note: The count selects inputs/next work; this is not a truth-validation criterion for stored
          skills.
      - scope: Retained events/replayed iteration at learning-loop limit
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id027
          - memory.md#mem-rte-event-replay
          - memory.md#mem-obj-events
          note: Reconstructed iteration affects continuation versus exit.
        - value: enforcement
          basis: wired
          records: *id027
          note: The max_iterations branch can stop additional learning episodes.
        records: *id027
        note: Only the iteration consumer has an established downstream driver consequence; other recorder
          metrics have no established model consumer.
      - scope: Encountered-block set at curriculum rendering
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id028
          - memory.md#mem-obj-block-records
          note: Encountered names inform subsequent curriculum context.
        records: *id028
        note: The set yields previously encountered other-block context rather than a spatial map.
      - scope: Task experience at success-conditioned skill admission
        assessment: known
        findings:
        - value: learning
          basis: wired
          records: &id029
          - runtime.md#rt-rte-skill-admission
          - memory.md#mem-obj-skills-code
          note: Successful task experience feeds retention/replacement of capability artifacts.
        records: *id029
        note: The automatic update turns task activity into durable executable behavior-shaping material;
          this authority is distinct from its later instruction/knowledge effects.
      - scope: Unsampled retained skill bodies and their further executable effects
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-skills-code
        - runtime.md#rt-bap-skill-execution
        note: The delivery/definition channel is inspected, but other checks, controls or knowledge assertions
          inside those bodies are not. No complete-value union is justified.
      records:
      - memory.md#mem-rte-skill-retrieval
      - memory.md#mem-obj-skills-code
      - runtime.md#rt-bap-skill-execution
      - memory.md#mem-obj-skill-vectordb
      - memory.md#mem-obj-qa-questions
      - memory.md#mem-rte-qa-cache
      - memory.md#mem-obj-qa-cache
      - memory.md#mem-rte-chest-update
      - memory.md#mem-obj-chest-memory
      - memory.md#mem-obj-task-histories
      - memory.md#mem-rte-progress-update
      - runtime.md#rt-rte-task-inference
      - memory.md#mem-rte-event-replay
      - memory.md#mem-obj-events
      - memory.md#mem-obj-block-records
      - runtime.md#rt-rte-skill-admission
      note: Actual inspected consumers establish the listed forces, not compliance or benefit. Additional
        effects of unsampled executable bodies remain unresolved; static prompt instructions and provider
        weights are outside this memory boundary.
    write_agency:
      assessment: partial
      units:
      - scope: Learning skill admission with automatic critic; direct manager admission logic
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id030
          - runtime.md#rt-rte-skill-admission
          note: Software admits/generated descriptions and active entries after its conditions are met.
        records: *id030
        note: The driver success branch and manager deposit exclusion decide admission without further
          content approval. Generic direct-call origin itself is unresolved below.
      - scope: Learning skill admission under manual critic approval
        assessment: known
        findings:
        - value: manual
          basis: wired
          records: &id031
          - runtime.md#rt-rte-skill-admission
          - runtime.md#rt-rte-task-judgment
          note: Human approval supplies the success decision gating the retained program.
        records: *id031
        note: A human explicitly confirms success of this candidate attempt before the learning driver
          retains its program; subsequent description generation remains automatic.
      - scope: Skill-description generation and embedding/index writes after admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id032
          - epistemic.md#epi-rte-skill-description
          - runtime.md#rt-rte-skill-admission
          note: The manager accepts model-generated descriptions and derives index entries without per-description
            approval.
        records: *id032
        note: Approval of a preceding task is not separate approval of the subsequently generated description.
      - scope: QA misses, chest observations, history cleanup, event recording/replay and encountered-block
          updates
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id033
          - memory.md#mem-rte-qa-cache
          - memory.md#mem-rte-chest-update
          - memory.md#mem-rte-progress-update
          - memory.md#mem-rte-event-replay
          - memory.md#mem-obj-block-records
          note: Each named route performs its own software admission or reconstruction.
        records: *id033
        note: Models/code perform each store transformation. Human critic success may supply an outcome
          but does not manually edit each history entry or chest/event record.
      - scope: Initial shipped/checkpoint contents, external replacements and caller-supplied direct-manager
          inputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-skills-code
        - memory.md#mem-obj-skill-vectordb
        - memory.md#mem-obj-qa-cache
        - runtime.md#rt-rte-skill-admission
        note: Caller identity and library-directory selection do not establish who supplied, edited or
          approved each entry. Historical/manual versus automatic admission remains not determinable.
      records:
      - runtime.md#rt-rte-skill-admission
      - runtime.md#rt-rte-task-judgment
      - epistemic.md#epi-rte-skill-description
      - memory.md#mem-rte-qa-cache
      - memory.md#mem-rte-chest-update
      - memory.md#mem-rte-progress-update
      - memory.md#mem-rte-event-replay
      - memory.md#mem-obj-block-records
      - memory.md#mem-obj-skills-code
      - memory.md#mem-obj-skill-vectordb
      - memory.md#mem-obj-qa-cache
      note: Live software/model admission is automatic unless a human makes the content decision. Manual
        critic approval is a distinct evidenced gate. Checkpoint selection by a generic caller does not
        establish per-entry manual admission.
    curation_operations:
      assessment: partial
      units:
      - scope: Same-name active skill code/description/index replacement with versioned text archives
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id034
          - runtime.md#rt-rte-skill-admission
          - memory.md#mem-obj-skills-code
          - memory.md#mem-obj-skill-description
          - memory.md#mem-obj-skill-vectordb
          note: A new same-name admission replaces active code/description/index membership while older
            text versions survive.
        records: *id034
        note: The old active entry is revised; retaining archives does not itself promote or decay content.
      - scope: Existing chest-map entry replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records: &id035
          - memory.md#mem-rte-chest-update
          - memory.md#mem-obj-chest-memory
          note: Counts at an existing retained position are replaced by later observations.
        records: *id035
        note: New dictionary observations revise retained counts. Deletion of Invalid positions is described
          separately and not called history-preserving invalidation without that warrant.
      - scope: Completed task deduplication and failure withdrawal
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records: &id036
          - memory.md#mem-rte-progress-update
          - memory.md#mem-obj-task-histories
          - memory.md#mem-obj-events
          note: Repeated completed task strings are reduced to one ordered occurrence.
        - value: invalidate
          basis: wired
          records: *id036
          note: Failure membership is withdrawn after success; underlying recorder history is not thereby
            deleted.
        records: *id036
        note: Completed strings are deduplicated; success removes matching failures from active history
          while raw recorder events remain separately retained.
      - scope: Retained event archive to reconstructed accounting
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id037
          - memory.md#mem-rte-event-replay
          - memory.md#mem-obj-events
          note: Raw retained events are reduced to operative accounting, including the iteration count.
        records: *id037
        note: Replay selects/aggregates existing recorded information into reduced counts and histories;
          it does not create a semantic skill explanation.
      - scope: Uninspected historical/checkpoint maintenance and opaque trial-index transformations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-skill-vectordb
        - memory.md#mem-obj-skills-code
        - memory.md#mem-obj-qa-cache
        note: No complete maintenance history is available. Index rebuild/addition and primary-key replacement
          alone do not establish other curation values.
      records:
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-obj-skills-code
      - memory.md#mem-obj-skill-description
      - memory.md#mem-obj-skill-vectordb
      - memory.md#mem-rte-chest-update
      - memory.md#mem-obj-chest-memory
      - memory.md#mem-rte-progress-update
      - memory.md#mem-obj-task-histories
      - memory.md#mem-obj-events
      - memory.md#mem-rte-event-replay
      - memory.md#mem-obj-qa-cache
      note: The inspected maintenance routes establish local evolution, deduplication and replay consolidation.
        Initial/external maintenance is unknown. New-candidate description generation is not automatically
        curation of already retained memory, nor evidence of synthesis.
    read_back_direction:
      assessment: known
      units:
      - scope: Driver-requested semantic skill retrieval and checkpoint/library reload
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id038
          - memory.md#mem-rte-skill-retrieval
          - memory.md#mem-obj-skills-code
          - runtime.md#rt-rte-skill-admission
          note: A query or selected library/checkpoint load requests retained code/state.
        records: *id038
        note: The driver/constructor asks for retained material. Returning requested code is not an extra
          unsolicited push.
      - scope: QA exact/nearest-question cache lookup and checkpoint reload
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id039
          - memory.md#mem-rte-qa-cache
          - memory.md#mem-obj-qa-cache
          - memory.md#mem-obj-qa-questions
          note: Exact/semantic requests return prior answers instead of generating another answer.
        records: *id039
        note: A task-context or QA request obtains retained answers; the question index is an access part
          of that requested return.
      - scope: Automatic all-active-code supply to each environment execution
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id040
          - runtime.md#rt-bap-skill-execution
          - memory.md#mem-obj-skills-code
          note: Execution automatically receives the loaded library alongside current code.
        records: *id040
        note: The manager assembles every active definition without a per-skill consumer request; prompt
          retrieval is a separate pull route.
      - scope: Automatic selected QA pairs, rendered chest/history context and encountered-block context
          in later model calls
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id041
          - memory.md#mem-rte-qa-cache
          - memory.md#mem-rte-chest-update
          - memory.md#mem-rte-progress-update
          - memory.md#mem-obj-block-records
          - memory.md#mem-rte-context-refresh
          note: Automatic context assembly supplies retained memory to later model invocations.
        records: *id041
        note: Renderers supply memory as part of driver-owned model context; the models do not ask for
          these individual retained items.
      - scope: Explicit resume of chest/history state and chronological recorder event replay
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id042
          - memory.md#mem-rte-chest-update
          - memory.md#mem-rte-progress-update
          - memory.md#mem-rte-event-replay
          note: Resume loads/reconstructs prior saved state on request.
        records: *id042
        note: Resume requests saved state; replay scans timestamp files, optionally to a cutoff. This
          is not implicit conversational-history reload.
      - scope: Automatic use of retained progress and replayed iteration in later driver decisions
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id043
          - memory.md#mem-rte-progress-update
          - memory.md#mem-rte-event-replay
          note: Progress/iteration state automatically enters subsequent branch and input-window decisions.
        records: *id043
        note: Once available, retained control state is supplied to sequencing/continuation logic without
          a per-item request from that consumer.
      records:
      - memory.md#mem-rte-skill-retrieval
      - memory.md#mem-obj-skills-code
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-rte-qa-cache
      - memory.md#mem-obj-qa-cache
      - memory.md#mem-obj-qa-questions
      - runtime.md#rt-bap-skill-execution
      - memory.md#mem-rte-chest-update
      - memory.md#mem-rte-progress-update
      - memory.md#mem-obj-block-records
      - memory.md#mem-rte-context-refresh
      - memory.md#mem-rte-event-replay
      note: The recorded consumer inventory includes requested retrieval/reload and independent automatic
        supply. Distinct operations within each chain are not counted twice; opaque historical content
        does not obscure these inspected delivery routes.
    read_back_signal:
      assessment: known
      units:
      - scope: 'Every-execution library assembly: trigger is an action step, selector is active map membership,
          selected part is all active skill code'
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id044
          - runtime.md#rt-bap-skill-execution
          - memory.md#mem-obj-skills-code
          note: All available active definitions are supplied.
        records: *id044
        note: No relevance threshold or per-name request selects definitions for this channel.
      - scope: 'Curriculum QA display: trigger is eligible context rendering, inputs are progress/probability,
          eligible returned QA pairs and cap five'
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id045
          - memory.md#mem-rte-qa-cache
          - memory.md#mem-rte-context-refresh
          note: Category eligibility, fixed suitability exclusions and count budget control automatic
            context supply.
        records: *id045
        note: The push keeps eligible advice after fixed Unknown/language-model exclusions and a count
          budget. Nearest-question selection is separately a requested lookup, not an independent push.
      - scope: 'Chest/history/block context: trigger is the relevant later model render, inputs are retained
          object availability and renderer/task/disclosure rules'
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id046
          - memory.md#mem-rte-chest-update
          - memory.md#mem-rte-progress-update
          - memory.md#mem-obj-block-records
          - memory.md#mem-rte-context-refresh
          note: Whole retained objects or code-gated categories are rendered without a semantic per-item
            push selector.
        records: *id046
        note: Selected parts are rendered chest entries, task history and encountered names. Proximity
          is a chest acquisition rule, not identity-targeted push from the saved map.
      - scope: 'Progress/iteration delivery to driver: trigger is later sequencing/continuation, inputs
          are retained counts and fixed thresholds'
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id047
          - memory.md#mem-rte-progress-update
          - memory.md#mem-rte-event-replay
          note: Read-back makes available aggregate control state under fixed driver rules.
        records: *id047
        note: The selected retained parts are control counts; fixed branch use does not imply lexical
          or embedding targeting.
      records:
      - runtime.md#rt-bap-skill-execution
      - memory.md#mem-obj-skills-code
      - memory.md#mem-rte-qa-cache
      - memory.md#mem-rte-context-refresh
      - memory.md#mem-rte-chest-update
      - memory.md#mem-rte-progress-update
      - memory.md#mem-obj-block-records
      - memory.md#mem-rte-event-replay
      note: All recorded push operations use coarse availability, configured gates or whole-object supply.
        Embedding and name/key matching occur in requested pull chains and therefore do not establish
        inferred-embedding or identifier push findings.
    trace_learning:
      assessment: partial
      units:
      - scope: Successful task program to retained skill, then later action model/executor
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id048
          - runtime.md#rt-rte-skill-admission
          - memory.md#mem-obj-skills-code
          - memory.md#mem-rte-skill-retrieval
          - runtime.md#rt-bap-skill-execution
          note: Automatic task-experience-conditioned retention produces durable behavior-shaping code.
        records: *id048
        note: Task activity and success condition an automatic durable capability write with wired later
          consumers; direct admissions and historical libraries do not inherit this provenance.
      - scope: Chest events to persisted map, then later planning/judgment/task selection
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id049
          - memory.md#mem-rte-chest-update
          - memory.md#mem-obj-chest-memory
          note: Environmental reports automatically change a durable artifact with later behavior-shaping
            consumers.
        records: *id049
        note: The automatic trace-fed update persists and later affects model context and possible task
          override.
      - scope: Task outcome to cleaned persisted history, then curriculum/disclosure/inference
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id050
          - memory.md#mem-rte-progress-update
          - memory.md#mem-obj-task-histories
          note: Automatic outcome-derived durable state shapes later work and input selection.
        records: *id050
        note: Critic/human outcomes feed an automatic history update; no observed improvement is needed
          for this classification.
      - scope: QA answers whose questions can depend on observations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-qa-cache
        - memory.md#mem-obj-qa-cache
        note: The recorded account distinguishes model-prior answers from trace extraction, but does not
          establish how much environmental experience reaches every qualifying generation path. Neither
          universal yes nor bounded no is assigned.
      - scope: Raw event persistence and replay-derived accounting
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-event-replay
        - memory.md#mem-obj-events
        note: Later control use is wired, but raw-log retention alone is insufficient and replay summaries
          are recorded as in-memory accounting, not a separately durable learned artifact. Qualification
          under the durable-output test remains unresolved.
      - scope: Within-bot encounter set and within-task frame replacement
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-block-records
        - memory.md#mem-rte-context-refresh
        note: Cross-invocation context exists, but a durable trace-learned artifact is not established
          for these transient parts; a bounded absence record is not supplied.
      - scope: Initial checkpoint/library production and unsampled historical writes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-skills-code
        - memory.md#mem-obj-skill-vectordb
        - memory.md#mem-obj-qa-cache
        note: The loaded artifacts are available, but no original production trace or complete admission
          history is supplied.
      records:
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-obj-skills-code
      - memory.md#mem-rte-skill-retrieval
      - runtime.md#rt-bap-skill-execution
      - memory.md#mem-rte-chest-update
      - memory.md#mem-obj-chest-memory
      - memory.md#mem-rte-progress-update
      - memory.md#mem-obj-task-histories
      - memory.md#mem-rte-qa-cache
      - memory.md#mem-obj-qa-cache
      - memory.md#mem-rte-event-replay
      - memory.md#mem-obj-events
      - memory.md#mem-obj-block-records
      - memory.md#mem-rte-context-refresh
      - memory.md#mem-obj-skill-vectordb
      note: Three recorded automatic trace-to-durable-behavior chains establish yes without observed gain.
        QA mixed input, archival replay and within-task/bot state do not establish a complete positive
        or bounded negative for every included write.
    trace_source:
      assessment: partial
      units:
      - scope: Learning success-conditioned skill write
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id051
          - runtime.md#rt-rte-skill-admission
          - memory.md#mem-obj-skills-code
          - runtime.md#rt-rte-task-judgment
          note: The executed program and execution/task feedback determine which code is retained.
        records: *id051
        note: The qualifying source is executed action code and its task-completion feedback, not a stored
          conversational session. No linked multi-step training trajectory consumer is established.
      - scope: Chest-map trace-fed write
        assessment: known
        findings:
        - value: event-streams
          basis: wired
          records: &id052
          - memory.md#mem-rte-chest-update
          - memory.md#mem-obj-chest-memory
          note: Environmental chest events/reports feed the persistent map update.
        records: *id052
        note: Close/remove/discovery observations and nearbyChests reports originate in the game/environment
          callback route.
      - scope: Task-outcome history write
        assessment: known
        findings:
        - value: tool-traces
          basis: wired
          records: &id053
          - memory.md#mem-rte-progress-update
          - memory.md#mem-obj-task-histories
          note: Action/rollout outcome feedback supplies completed/failed task status.
        records: *id053
        note: Executed-task success/failure, including caught rollout failures, supplies feedback used
          by the durable control-history update.
      - scope: QA, replay accounting and transient block/frame routes whose trace-learning qualification
          is unresolved
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-qa-cache
        - memory.md#mem-rte-event-replay
        - memory.md#mem-obj-block-records
        - memory.md#mem-rte-context-refresh
        note: Source classification for a qualifying durable learning write cannot be completed before
          its qualification and exact consumed trace input are established; observed events alone do not
          prove every route qualifies.
      - scope: Initial shipped/checkpoint content and historical embedding/library writes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-skills-code
        - memory.md#mem-obj-skill-vectordb
        - memory.md#mem-obj-qa-cache
        note: Historical trace origins are uninspected; neither session-logs nor trajectories may be inferred
          from an existing library.
      records:
      - runtime.md#rt-rte-skill-admission
      - memory.md#mem-obj-skills-code
      - runtime.md#rt-rte-task-judgment
      - memory.md#mem-rte-chest-update
      - memory.md#mem-obj-chest-memory
      - memory.md#mem-rte-progress-update
      - memory.md#mem-obj-task-histories
      - memory.md#mem-rte-qa-cache
      - memory.md#mem-rte-event-replay
      - memory.md#mem-obj-block-records
      - memory.md#mem-rte-context-refresh
      - memory.md#mem-obj-skill-vectordb
      - memory.md#mem-obj-qa-cache
      note: Qualifying live writes have task-action outcomes and environmental events. Unresolved qualification/provenance
        on other included writes prevents source inapplicability or a complete source union.
---

# Voyager memory profile

## Comparison rationale

This profile classifies accepted records, not a new source inspection. All positive findings have a wired implementation basis. No supplied execution or causal evidence upgrades them to observed operation or demonstrated benefit. The inventory distinguishes accumulated objects from current parser output and static helper code: [MEM-OBJ-skills-code](memory.md#mem-obj-skills-code), [RT-OBJ-program-code](runtime.md#rt-obj-program-code) and [RT-OBJ-control-primitives](runtime.md#rt-obj-control-primitives).

Reconciliation supersedes the epistemic chest and description objects and the epistemic QA, chest and progress routes with their memory counterparts. The classifications therefore cite [MEM-OBJ-chest-memory](memory.md#mem-obj-chest-memory), [MEM-OBJ-skill-description](memory.md#mem-obj-skill-description), [MEM-RTE-qa-cache](memory.md#mem-rte-qa-cache), [MEM-RTE-chest-update](memory.md#mem-rte-chest-update) and [MEM-RTE-progress-update](memory.md#mem-rte-progress-update). The combined epistemic QA container is not substituted for its separate answer-map and question-index parts. The distinct description-generation subroute remains [EPI-RTE-skill-description](epistemic.md#epi-rte-skill-description).

The executable library is standing symbolic direction at Node, classified as instruction rather than enforcement. A definition can guide execution when called without vetoing arbitrary code. The model-facing copy instead supplies knowledge/examples; the description index supplies ranking. These are separate forces and consumers, not a claim that the executor actually called every delivered function. See [RT-BAP-skill-execution](runtime.md#rt-bap-skill-execution) and [MEM-RTE-skill-retrieval](memory.md#mem-rte-skill-retrieval). Unknown additional effects inside unsampled bodies keep authority partial.

Requested semantic retrieval remains pull even though the driver later formats its result. The separate automatic whole-library channel is push. Likewise requested QA lookup differs from automatic curriculum display of eligible pairs. Identifier lookup and embedding similarity inside those requested returns do not establish identifier-based or embedding-based push. Fixed display eligibility, budgets and whole-map supply establish coarse push selection; they are not a new relevance inference. See [MEM-RTE-skill-retrieval](memory.md#mem-rte-skill-retrieval), [MEM-RTE-qa-cache](memory.md#mem-rte-qa-cache) and [MEM-RTE-context-refresh](memory.md#mem-rte-context-refresh).

Manual task approval is local to the manual critic gate on the retained program. It does not turn later generated descriptions, chest observations or progress-list mutation into manual content decisions. Conversely, an arbitrary caller selecting a checkpoint does not establish automatic or manual original admission for each entry. These unknown alternatives remain in write agency and lineage rather than inheriting the live automatic route: [RT-RTE-task-judgment](runtime.md#rt-rte-task-judgment), [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission).

Curation classifies implemented changes to retained content. Same-name skill replacement evolves an active artifact; progress cleanup deduplicates and withdraws failure membership while recorder history remains. Replay consolidates retained event information into reduced accounting. New-candidate description generation, embedding construction and ordinary cache acquisition do not alone establish curation; semantic indeterminacy does not establish synthesis. See [MEM-RTE-progress-update](memory.md#mem-rte-progress-update), [MEM-RTE-event-replay](memory.md#mem-rte-event-replay) and [EPI-RTE-skill-description](epistemic.md#epi-rte-skill-description).

Trace learning is an automatic durable-write classification, not proof of capacity gain or model-weight training. Skill, chest and outcome-history chains support local yes findings. Event archives have a later limit-control consumer, but the records do not establish a separately durable derived learning output; block sets and replacement action frames likewise have insufficient durability warrant for a stronger classification here. QA observations may shape questions while answers come from model knowledge; its exact trace-fed contribution remains unresolved. No local no finding or system-wide negative is inferred from these gaps. See [RT-RTE-skill-admission](runtime.md#rt-rte-skill-admission), [MEM-RTE-chest-update](memory.md#mem-rte-chest-update), [MEM-RTE-progress-update](memory.md#mem-rte-progress-update), [MEM-RTE-event-replay](memory.md#mem-rte-event-replay), [MEM-OBJ-block-records](memory.md#mem-obj-block-records) and [MEM-RTE-qa-cache](memory.md#mem-rte-qa-cache).

Source-read log: none. Only the supplied members and governing contracts were read; no frozen target files were reopened. Historical trial payloads, embedding identities and initial content-control facts remain missing recorded evidence, not absent mechanisms. The known storage and delivery architecture does not make those content/provenance axes complete.
