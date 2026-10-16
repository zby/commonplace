---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Memory profile of Ecdysis: retained task evidence, review guidance/checkpoints, harness
  references and separately loaded skill artifacts.'
run-id: AAS-2026-10-13-ecdysis-bb4c64dbdf60-01
source-identity: https://github.com/cuiyu-ai/Ecdysis
reviewed-boundary: cf93866d545b0974dbb0bc83b39c31fbbdeeecb8
memory-comparison:
  version: 2
  scope: 'Shipped use-derived memory: extracted trajectories and failure display; accumulated review transcript,
    normalized specification and checkpoint content/control/accounting; score-retained harness reference
    and round audit; skill content/artifact envelope and explicit reload/merge; inference outcomes and
    explicit persistence. Opaque generic harness, task/tool/output payloads, metadata and caller admission
    alternatives remain included where they limit classification. Excludes static role prompts/source
    code, provider weights and provider-internal state, external task/editor/scorer implementations and
    external harness-factory stores; their responsibilities are not attributed to Ecdysis.'
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Extracted trajectories and formatted failure display
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id001
          - memory.md#mem-obj-trajectories
          - epistemic.md#epi-obj-failure-context
          note: Python lists, dictionaries and formatted text retain extracted task evidence.
        records: *id001
        note: Input files are acquisition sources; the extracted objects are held in process memory.
      - scope: Review transcript, normalized specification and checkpoint parts
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id002
          - memory.md#mem-obj-transcript
          - runtime.md#rt-obj-review-spec
          - memory.md#mem-obj-checkpoint
          note: Live transcript/spec/progress dictionaries are retained during review.
        - value: files
          basis: wired
          records: *id002
          note: Optional checkpoint JSON retains transcript, progress and completed specification; standalone
            transcript saving is also implemented.
        records: *id002
        note: Content and control parts share these substrates, not necessarily the same consumers.
      - scope: Retained harness reference and round audit tuple
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id003
          - runtime.md#rt-obj-frozen-harness
          - memory.md#mem-obj-round-record
          - runtime.md#rt-rte-candidate-admission
          note: TrainingResult retains the generic harness value and decision tuple in the Python process.
        records: *id003
        note: The opaque harness is included as the live retained value. No external factory store is
          attributed to the shipped plane.
      - scope: Skills and artifact envelope, including caller-defined metadata
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id004
          - memory.md#mem-obj-evolved-skill
          - memory.md#mem-obj-skill-artifact
          - runtime.md#rt-rte-artifact-utilities
          note: Skill/envelope dataclasses and arbitrary metadata live in memory.
        - value: files
          basis: wired
          records: *id004
          note: Explicit save/load persists and reloads artifact JSON.
        records: *id004
        note: Opaque metadata encoding does not make the known file/dataclass substrate unknown.
      - scope: Inference outcome records and checkpoint usage accounting
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records: &id005
          - memory.md#mem-obj-inference-record
          - memory.md#mem-obj-checkpoint
          - runtime.md#rt-rte-harness-inference
          note: Runner records and client/review usage segments reside in Python state.
        - value: files
          basis: wired
          records: *id005
          note: Explicit inference JSONL output and checkpoint usage segments persist in files.
        records: *id005
        note: Output payloads can be opaque, but the shipped enclosing stores are inspected.
      records:
      - memory.md#mem-obj-trajectories
      - epistemic.md#epi-obj-failure-context
      - memory.md#mem-obj-transcript
      - runtime.md#rt-obj-review-spec
      - memory.md#mem-obj-checkpoint
      - runtime.md#rt-obj-frozen-harness
      - memory.md#mem-obj-round-record
      - runtime.md#rt-rte-candidate-admission
      - memory.md#mem-obj-evolved-skill
      - memory.md#mem-obj-skill-artifact
      - runtime.md#rt-rte-artifact-utilities
      - memory.md#mem-obj-inference-record
      - runtime.md#rt-rte-harness-inference
      note: The recorded shipped inventory is covered. Provider parameters, external adapter stores and
        static source files are not use-derived stores of this memory boundary; files and in-memory do
        not imply automatic harness persistence.
    representational_form:
      assessment: partial
      units:
      - scope: Trajectory diagnostic fields and formatted metadata display
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id006
          - memory.md#mem-obj-trajectories
          - epistemic.md#epi-obj-failure-context
          - epistemic.md#epi-rte-failure-shaping
          note: Reward, trial, tool-call and grouping fields have fixed extraction/selection rules.
        - value: natural-language
          basis: wired
          records: *id006
          note: Formatted failure evidence is interpreted by review models.
        records: *id006
        note: Different consumption paths are classified separately even when they carry the same labels.
      - scope: Trajectory message text and arbitrary task/tool payloads
        assessment: partial
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-trajectories
          note: Compacted message content can carry natural-language task evidence.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-trajectories
          note: Role and tool-call fields remain structured copied data.
        records:
        - memory.md#mem-obj-trajectories
        note: Arbitrary task payloads and tool arguments have unresolved forms; the readable message view
          does not classify those opaque parts.
      - scope: Review reply/specification prose at model and editor consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id007
          - memory.md#mem-obj-transcript
          - runtime.md#rt-obj-review-spec
          - epistemic.md#epi-obj-proposed-changes
          note: Diagnoses, descriptions, rationales, tips and notes receive meaning through interpretation.
        records: *id007
        note: No concrete reply establishes truth or criticism, but the text-consumption form is wired.
      - scope: Transcript/spec/checkpoint control containers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id008
          - memory.md#mem-obj-transcript
          - runtime.md#rt-obj-review-spec
          - memory.md#mem-obj-checkpoint
          - runtime.md#rt-rte-checkpoint-recovery
          note: Role labels, specification field keys, status, hash, model string and index follow fixed
            program rules.
        records: *id008
        note: JSON is encoding; the fixed consumer rules establish symbolic form.
      - scope: Synthetic retained revision harness
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id009
          - runtime.md#rt-obj-frozen-harness
          - runtime.md#rt-bap-retained-harness
          note: The dictionary revision has fixed reward/output consumers in quickstart.
        records: *id009
        note: This witness classifies only the shipped synthetic harness, not arbitrary real harness payloads.
      - scope: Generic retained harness payload
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-frozen-harness
        - runtime.md#rt-bap-retained-harness
        note: The API accepts arbitrary instructions, code or numerical components. No particular form
          is established for the opaque alternative.
      - scope: Skill text and artifact structural fields
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records: &id010
          - memory.md#mem-obj-evolved-skill
          - memory.md#mem-obj-skill-artifact
          - runtime.md#rt-rte-artifact-utilities
          note: Title, pattern and tip are retained behavior guidance text.
        - value: symbolic
          basis: wired
          records: *id010
          note: Identifiers, scope, round, version and parent strings follow structural load/merge rules.
        records: *id010
        note: The text form does not establish an agent consumer.
      - scope: Caller-defined artifact metadata
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-skill-artifact
        note: Metadata can be opaque; its content form and operative interpretation are not specified.
      - scope: Round decisions, inference bookkeeping and usage counters
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records: &id011
          - memory.md#mem-obj-round-record
          - memory.md#mem-obj-inference-record
          - memory.md#mem-obj-checkpoint
          note: Scores, acceptance/status, IDs, errors, timing and token counters are structured fields.
        records: *id011
        note: This excludes opaque task/output values from the classification.
      - scope: Inference task/output payloads
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-inference-record
        note: External adapter payloads and default=str display do not establish the original consumed
          form.
      records:
      - memory.md#mem-obj-trajectories
      - epistemic.md#epi-obj-failure-context
      - epistemic.md#epi-rte-failure-shaping
      - memory.md#mem-obj-transcript
      - runtime.md#rt-obj-review-spec
      - epistemic.md#epi-obj-proposed-changes
      - memory.md#mem-obj-checkpoint
      - runtime.md#rt-rte-checkpoint-recovery
      - runtime.md#rt-obj-frozen-harness
      - runtime.md#rt-bap-retained-harness
      - memory.md#mem-obj-evolved-skill
      - memory.md#mem-obj-skill-artifact
      - runtime.md#rt-rte-artifact-utilities
      - memory.md#mem-obj-round-record
      - memory.md#mem-obj-inference-record
      note: Known text and symbolic parts coexist with unresolved task/tool payloads, generic harness
        content, artifact metadata and inference payloads. No parametric use-derived memory is established
        by the fixed provider model.
    lineage:
      assessment: partial
      units:
      - scope: Imported trajectory input and extracted/compacted evidence
        assessment: partial
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-trajectories
          - epistemic.md#epi-rte-failure-shaping
          note: Collector dictionaries or explicit result files enter from outside extraction.
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-trajectories
          - epistemic.md#epi-rte-failure-shaping
          note: Reward-filtered message tails and failure metadata derive from recorded task activity.
        records:
        - memory.md#mem-obj-trajectories
        - epistemic.md#epi-rte-failure-shaping
        note: Extraction is known; original task/model/tool provenance and authenticity remain unresolved.
      - scope: Review transcript and specification derivation
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records: &id012
          - memory.md#mem-obj-transcript
          - runtime.md#rt-obj-review-spec
          - runtime.md#rt-rte-failure-review
          note: Review uses scored failure metadata and selected prior review turns to produce retained
            replies/specification.
        records: *id012
        note: The automatic derivation path is wired; actual meaning, correctness and benefit are unobserved.
      - scope: Checkpoint hash/progress/usage and training round decisions
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records: &id013
          - memory.md#mem-obj-checkpoint
          - memory.md#mem-obj-round-record
          - runtime.md#rt-rte-checkpoint-recovery
          - runtime.md#rt-rte-candidate-admission
          note: Code derives hashes, progress indices, accounting segments and scalar decision records
            from invocation state/results.
        records: *id013
        note: These control/audit parts are not conflated with model-authored review content.
      - scope: 'Retained harness: initial content and subsequent candidate path'
        assessment: partial
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-obj-frozen-harness
          - runtime.md#rt-rte-candidate-admission
          note: Collected failures/specification feed the supplied editor and score-selected replacement
            route.
        records:
        - runtime.md#rt-obj-frozen-harness
        - runtime.md#rt-rte-candidate-admission
        note: The update route is wired, but initial harness provenance and real editor derivation semantics
          are unresolved; quickstart ignores the specification.
      - scope: Caller-supplied skills, artifact metadata and parent provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-evolved-skill
        - memory.md#mem-obj-skill-artifact
        - runtime.md#rt-rte-artifact-utilities
        note: Manual, model-produced and arbitrary supplied content are possible, not verified authored/imported/trace-extracted
          instances. Default source labels and parent strings do not authenticate lineage.
      - scope: Inference outcomes and wrapper fields
        assessment: partial
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-inference-record
          - runtime.md#rt-rte-harness-inference
          note: The runner constructs task outcome/error/timing records from execution returns.
        records:
        - memory.md#mem-obj-inference-record
        - runtime.md#rt-rte-harness-inference
        note: Opaque task and output payload provenance remains external; the known wrapper derivation
          does not resolve it.
      records:
      - memory.md#mem-obj-trajectories
      - epistemic.md#epi-rte-failure-shaping
      - memory.md#mem-obj-transcript
      - runtime.md#rt-obj-review-spec
      - runtime.md#rt-rte-failure-review
      - memory.md#mem-obj-checkpoint
      - memory.md#mem-obj-round-record
      - runtime.md#rt-rte-checkpoint-recovery
      - runtime.md#rt-rte-candidate-admission
      - runtime.md#rt-obj-frozen-harness
      - memory.md#mem-obj-evolved-skill
      - memory.md#mem-obj-skill-artifact
      - runtime.md#rt-rte-artifact-utilities
      - memory.md#mem-obj-inference-record
      - runtime.md#rt-rte-harness-inference
      note: Derivation paths are classified without treating learned/evolution labels as provenance. Unresolved
        initial content and opaque payload origins prevent a complete lineage inventory.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Trajectory evidence at review/editor update consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id014
          - memory.md#mem-obj-trajectories
          - runtime.md#rt-rte-failure-review
          - epistemic.md#epi-rte-failure-shaping
          - runtime.md#rt-rte-candidate-admission
          note: Failure evidence supplies contextual assertions/advice to review and editor.
        - value: learning
          basis: wired
          records: *id014
          note: Retained task experience feeds review/specification and candidate behavior-shaping updates.
        - value: ranking
          basis: wired
          records: *id014
          note: Retained task IDs, rewards and termination/breakdown signatures determine group recurrence
            order.
        records: *id014
        note: Ranking is influence of retained evidence under fixed code, not a learned ranking policy.
      - scope: Review transcript at subsequent review calls
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id015
          - memory.md#mem-obj-transcript
          - runtime.md#rt-rte-failure-review
          note: Selected earlier turns supply advisory context to subsequent roles.
        - value: learning
          basis: wired
          records: *id015
          note: Earlier proposed repairs and criticism are inputs to subsequent durable review/specification
            generation.
        records: *id015
        note: Wired delivery does not establish actual criticism or improved capacity.
      - scope: Specification at candidate editor
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records: &id016
          - runtime.md#rt-obj-review-spec
          - runtime.md#rt-bap-review-editor
          - runtime.md#rt-rte-candidate-admission
          note: Descriptions/tips/notes supply patch directions to an interpreting editor.
        - value: knowledge
          basis: wired
          records: *id016
          note: Failure patterns and rationales supply diagnostic context/advice.
        - value: learning
          basis: wired
          records: *id016
          note: Retained review guidance feeds candidate organization updates through the editor interface.
        records: *id016
        note: These forces are on the editor path. The synthetic editor ignores the spec; semantic compliance
          is not enforced.
      - scope: Checkpoint control fields at reentry
        assessment: known
        findings:
        - value: routing
          basis: wired
          records: &id017
          - memory.md#mem-obj-checkpoint
          - runtime.md#rt-rte-checkpoint-recovery
          note: Status and next-turn index select cached return or the next review operation.
        - value: validation
          basis: wired
          records: *id017
          note: Stored hash/model criteria determine admissibility of reuse.
        - value: enforcement
          basis: wired
          records: *id017
          note: A mismatch raises and prevents checkpoint reuse.
        records: *id017
        note: The equality gate has force without establishing comprehensive freshness or trust.
      - scope: Artifact scope and identifiers at load/merge
        assessment: known
        findings:
        - value: validation
          basis: wired
          records: &id018
          - memory.md#mem-obj-skill-artifact
          - memory.md#mem-obj-evolved-skill
          - runtime.md#rt-rte-artifact-utilities
          note: Retained scope fields are compared with expected scope/merge scope.
        - value: enforcement
          basis: wired
          records: *id018
          note: Scope mismatch raises; first-seen retained IDs exclude later same-ID units from the returned
            collection.
        records: *id018
        note: Scope checks are optional on some reads; first-ID suppression is not contextual relevance
          ranking.
      - scope: Skill text/envelope returned to explicit structural test/API caller
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records: &id019
          - memory.md#mem-obj-evolved-skill
          - memory.md#mem-obj-skill-artifact
          - runtime.md#rt-rte-artifact-utilities
          note: Explicit loading supplies retained text and metadata for caller inspection and round-trip
            comparison.
        records: *id019
        note: No standing instruction force at a task agent is established by this inspected consumer.
      - scope: Synthetic harness revision at collector/executor
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-frozen-harness
        - runtime.md#rt-bap-retained-harness
        note: The revision determines a synthetic reward predicate and rendered output, but those effects
          do not establish a controlled knowledge/instruction/routing force. Program-level behavioral
          dependence is known; its authority category is not determined.
      - scope: Generic retained harness at real collector/executor
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-frozen-harness
        - runtime.md#rt-bap-retained-harness
        note: Live argument delivery is known; opaque content and external consumer interpretation prevent
          assigning a particular controlled force.
      - scope: Audit/outcome/usage parts and opaque metadata
        assessment: partial
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-inference-record
          - runtime.md#rt-rte-harness-inference
          note: Outcome records supply caller summaries and printed outputs.
        records:
        - memory.md#mem-obj-round-record
        - memory.md#mem-obj-inference-record
        - memory.md#mem-obj-checkpoint
        - memory.md#mem-obj-skill-artifact
        note: Round audit and unused accounting/metadata have no evidenced consequential update consumer;
          opaque task outputs and arbitrary metadata prevent a complete authority assessment.
      records:
      - memory.md#mem-obj-trajectories
      - runtime.md#rt-rte-failure-review
      - epistemic.md#epi-rte-failure-shaping
      - runtime.md#rt-rte-candidate-admission
      - memory.md#mem-obj-transcript
      - runtime.md#rt-obj-review-spec
      - runtime.md#rt-bap-review-editor
      - memory.md#mem-obj-checkpoint
      - runtime.md#rt-rte-checkpoint-recovery
      - memory.md#mem-obj-skill-artifact
      - memory.md#mem-obj-evolved-skill
      - runtime.md#rt-rte-artifact-utilities
      - runtime.md#rt-obj-frozen-harness
      - runtime.md#rt-bap-retained-harness
      - memory.md#mem-obj-round-record
      - memory.md#mem-obj-inference-record
      note: Authority is local to consumed parts. Learning inputs, downstream patch instruction, control
        validation/enforcement and ranking are distinct. No task-agent skill injection or parametric learning
        authority is inferred.
    write_agency:
      assessment: partial
      units:
      - scope: Extraction, review turn/spec admission and generated checkpoint writes
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id020
          - memory.md#mem-obj-trajectories
          - memory.md#mem-obj-transcript
          - runtime.md#rt-obj-review-spec
          - memory.md#mem-obj-checkpoint
          - runtime.md#rt-rte-failure-review
          - runtime.md#rt-rte-checkpoint-recovery
          note: Software/model admission proceeds without per-content operator decisions after workflow
            setup.
        records: *id020
        note: Caller launch/path configuration is not manual curation of every resulting item.
      - scope: Trainer candidate reference admission and round decisions
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id021
          - runtime.md#rt-rte-candidate-admission
          - memory.md#mem-obj-round-record
          note: The trainer accepts strictly higher scores computationally and records decisions.
        records: *id021
        note: Callback-internal human contributions remain unknown, but do not erase the known software
          reference gate.
      - scope: Inference records and usage accounting production
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records: &id022
          - memory.md#mem-obj-inference-record
          - memory.md#mem-obj-checkpoint
          - runtime.md#rt-rte-harness-inference
          note: Runner/client code creates result and accounting records without per-record human approval.
        records: *id022
        note: Explicit output requests describe I/O, not content-admission authorship.
      - scope: Initial harness/results and callback-internal candidate authoring
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-frozen-harness
        - memory.md#mem-obj-trajectories
        - runtime.md#rt-rte-candidate-admission
        note: Generic caller identity and unavailable real editor internals do not establish explicit
          human content decisions or fully automatic initial admission.
      - scope: Skill/artifact construction, caller replacements and standalone transcript payloads
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-evolved-skill
        - memory.md#mem-obj-skill-artifact
        - runtime.md#rt-rte-artifact-utilities
        - memory.md#mem-obj-transcript
        - memory.md#mem-obj-checkpoint
        note: Utility callers can supply manual or generated content and replace files; no explicit human
          decision over that content is established. Physical JSON writing alone does not classify admission.
      records:
      - memory.md#mem-obj-trajectories
      - memory.md#mem-obj-transcript
      - runtime.md#rt-obj-review-spec
      - memory.md#mem-obj-checkpoint
      - runtime.md#rt-rte-failure-review
      - runtime.md#rt-rte-checkpoint-recovery
      - runtime.md#rt-rte-candidate-admission
      - memory.md#mem-obj-round-record
      - memory.md#mem-obj-inference-record
      - runtime.md#rt-rte-harness-inference
      - runtime.md#rt-obj-frozen-harness
      - memory.md#mem-obj-evolved-skill
      - memory.md#mem-obj-skill-artifact
      - runtime.md#rt-rte-artifact-utilities
      note: Automatic subsequent production/admission is supported. Initial caller content, real callback
        control and separately supplied replacement content remain unresolved; no manual positive is established.
    curation_operations:
      assessment: partial
      units:
      - scope: Failure evidence clipping/filtering and transcript history selection
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records: &id023
          - memory.md#mem-obj-trajectories
          - epistemic.md#epi-rte-failure-shaping
          - memory.md#mem-obj-transcript
          - runtime.md#rt-rte-failure-review
          note: Extraction truncates/selects recorded messages, review reduces evidence to metadata, and
            later role context selects a twelve-turn retained-history tail.
        records: *id023
        note: Reduction of existing evidence is consolidation; raw files/full transcript can remain retained.
      - scope: Artifact first-ID merge/load filtering
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records: &id024
          - memory.md#mem-obj-evolved-skill
          - memory.md#mem-obj-skill-artifact
          - runtime.md#rt-rte-artifact-utilities
          note: Only the first occurrence of each skill identifier is returned/merged.
        records: *id024
        note: Deduplication does not revise the older same-ID tip or prefer better evidence.
      - scope: Checkpoint reuse compatibility gate
        assessment: known
        findings:
        - value: invalidate
          basis: wired
          records: &id025
          - memory.md#mem-obj-checkpoint
          - runtime.md#rt-rte-checkpoint-recovery
          note: Mismatch withdraws current reliance by raising while the checkpoint file remains.
        records: *id025
        note: This bounded invalidation is not deletion or comprehensive semantic expiry.
      - scope: Harness replacement and model review content transformations
        assessment: partial
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-obj-frozen-harness
          - runtime.md#rt-rte-candidate-admission
          note: Accepted candidates replace the existing retained harness reference.
        records:
        - runtime.md#rt-obj-frozen-harness
        - runtime.md#rt-rte-candidate-admission
        - memory.md#mem-obj-transcript
        - runtime.md#rt-obj-review-spec
        - runtime.md#rt-rte-failure-review
        note: Actual semantic editor revision and new-claim production by model replies are unresolved.
          Critic/Moderator requests alone establish neither synthesize nor reliable semantic repair.
      - scope: Caller skill/metadata revisions and opaque content transformations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-evolved-skill
        - memory.md#mem-obj-skill-artifact
        - runtime.md#rt-rte-artifact-utilities
        - runtime.md#rt-obj-frozen-harness
        note: Overwriting a path or generic content supply does not establish a semantic evolve/synthesize
          operation. Callback transformations are not inspectable.
      records:
      - memory.md#mem-obj-trajectories
      - epistemic.md#epi-rte-failure-shaping
      - memory.md#mem-obj-transcript
      - runtime.md#rt-rte-failure-review
      - memory.md#mem-obj-evolved-skill
      - memory.md#mem-obj-skill-artifact
      - runtime.md#rt-rte-artifact-utilities
      - memory.md#mem-obj-checkpoint
      - runtime.md#rt-rte-checkpoint-recovery
      - runtime.md#rt-obj-frozen-harness
      - runtime.md#rt-rte-candidate-admission
      - runtime.md#rt-obj-review-spec
      note: Inspected reductions, deduplication, reuse invalidation and retained-reference evolution are
        supported. No decay is inferred from display slicing, nor synthesis from possible model novelty.
        Opaque edits prevent complete operation coverage.
    read_back_direction:
      assessment: partial
      units:
      - scope: Subsequent role context receives retained review turns
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id026
          - memory.md#mem-obj-transcript
          - runtime.md#rt-rte-failure-review
          note: Scheduled calls automatically receive the last twelve retained turns without a role request
            for that memory.
        records: *id026
        note: Trigger is the next scheduled role invocation; code builds its history context.
      - scope: Checkpoint reentry and cached completed return
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id027
          - memory.md#mem-obj-checkpoint
          - runtime.md#rt-rte-checkpoint-recovery
          note: A caller explicitly supplies an existing checkpoint path and requests review/reentry;
            matching state supplies progress/transcript or completed outputs.
        records: *id027
        note: Status/index selection within a requested return is not an additional unsolicited delivery.
      - scope: Review/specification and next-round retained-harness delivery
        assessment: known
        findings:
        - value: push
          basis: wired
          records: &id028
          - runtime.md#rt-obj-review-spec
          - runtime.md#rt-bap-review-editor
          - runtime.md#rt-obj-frozen-harness
          - runtime.md#rt-rte-candidate-admission
          - runtime.md#rt-bap-retained-harness
          note: Trainer automatically forwards retained specification to editor and retained harness to
            the next round collector.
        records: *id028
        note: Automatic workflow delivery is distinct from a consumer request for retained material.
      - scope: Retained harness at explicit infer/infer_many
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id029
          - runtime.md#rt-obj-frozen-harness
          - runtime.md#rt-rte-harness-inference
          - runtime.md#rt-bap-retained-harness
          note: Explicit inference requests use the retained harness through the executor.
        records: *id029
        note: This is an inspected request route, not evidence about an external factory store.
      - scope: Skill artifact reload/merge caller
        assessment: known
        findings:
        - value: pull
          basis: wired
          records: &id030
          - memory.md#mem-obj-evolved-skill
          - memory.md#mem-obj-skill-artifact
          - runtime.md#rt-rte-artifact-utilities
          note: Explicit path/parent-list requests return full loaded or deduplicated artifact content.
        records: *id030
        note: IDs suppress duplicates inside a requested collection; they do not make it targeted push.
      - scope: Opaque harness/metadata later-consumption alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-frozen-harness
        - memory.md#mem-obj-skill-artifact
        - memory.md#mem-obj-inference-record
        - runtime.md#rt-rte-harness-inference
        - memory.md#mem-abs-skill-injection
        note: External callback/factory consumers and arbitrary metadata routes are not established. Known
          request routes do not resolve these opaque alternatives.
      - scope: Round/outcome/usage audit and standalone transcript files
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-round-record
        - memory.md#mem-obj-inference-record
        - memory.md#mem-obj-checkpoint
        - memory.md#mem-obj-transcript
        note: Immediate return/output storage alone is not a later consumer invocation. Checkpoint uses
          are separately classified above; no standalone transcript reader or outcome-to-training reload
          is wired.
      records:
      - memory.md#mem-obj-transcript
      - runtime.md#rt-rte-failure-review
      - memory.md#mem-obj-checkpoint
      - runtime.md#rt-rte-checkpoint-recovery
      - runtime.md#rt-obj-review-spec
      - runtime.md#rt-bap-review-editor
      - runtime.md#rt-obj-frozen-harness
      - runtime.md#rt-rte-candidate-admission
      - runtime.md#rt-bap-retained-harness
      - runtime.md#rt-rte-harness-inference
      - memory.md#mem-obj-evolved-skill
      - memory.md#mem-obj-skill-artifact
      - runtime.md#rt-rte-artifact-utilities
      - memory.md#mem-obj-inference-record
      - memory.md#mem-abs-skill-injection
      - memory.md#mem-obj-round-record
      note: Both push and pull are established on named chains. Opaque consumer alternatives remain unresolved.
        Static role prompts and mere immediate returns are not accumulated-memory read-back.
    read_back_signal:
      assessment: partial
      units:
      - scope: Automatic transcript history selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id031
          - memory.md#mem-obj-transcript
          - runtime.md#rt-rte-failure-review
          note: Next-role trigger selects the last twelve turns by position/availability, without content
            relevance or an identity match.
        records: *id031
        note: 'Trigger: scheduled role call; input: full transcript; selected part: tail of retained role/content
          turns; no token budget.'
      - scope: Trainer specification and next-round harness supply
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records: &id032
          - runtime.md#rt-obj-review-spec
          - runtime.md#rt-bap-review-editor
          - runtime.md#rt-obj-frozen-harness
          - runtime.md#rt-rte-candidate-admission
          - runtime.md#rt-bap-retained-harness
          note: Workflow position/current retained reference selects the specification for editor and
            accepted harness for subsequent collection.
        records: *id032
        note: 'Trigger: editing/next round; selector input: current review result and retained reference;
          selected part: spec/harness. No semantic targeting is implemented.'
      - scope: Checkpoint reentry, explicit inference and artifact load requests
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-checkpoint-recovery
        - runtime.md#rt-rte-harness-inference
        - runtime.md#rt-rte-artifact-utilities
        note: These are requested retained-material returns. Explicit paths, matching context/model and
          dedup IDs do not establish independent identifier-based push.
      - scope: Opaque real harness and metadata consumer alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-obj-frozen-harness
        - memory.md#mem-obj-skill-artifact
        - memory.md#mem-obj-inference-record
        - runtime.md#rt-rte-harness-inference
        note: Their automatic selection operations, if any, are unavailable; known pull branches cannot
          make unresolved alternatives inapplicable.
      records:
      - memory.md#mem-obj-transcript
      - runtime.md#rt-rte-failure-review
      - runtime.md#rt-obj-review-spec
      - runtime.md#rt-bap-review-editor
      - runtime.md#rt-obj-frozen-harness
      - runtime.md#rt-rte-candidate-admission
      - runtime.md#rt-bap-retained-harness
      - runtime.md#rt-rte-checkpoint-recovery
      - runtime.md#rt-rte-harness-inference
      - runtime.md#rt-rte-artifact-utilities
      - memory.md#mem-obj-skill-artifact
      - memory.md#mem-obj-inference-record
      note: Coarse automatic supply is wired. There is no recorded lexical, embedding, judgment or identifier-based
        push selector; opaque alternatives prevent a complete selector inventory.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatically retained review transcript/specification with later role/editor consumer
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records: &id033
          - memory.md#mem-obj-transcript
          - runtime.md#rt-obj-review-spec
          - memory.md#mem-obj-checkpoint
          - runtime.md#rt-rte-failure-review
          - runtime.md#rt-rte-checkpoint-recovery
          - runtime.md#rt-bap-review-editor
          note: Task activity and prior review turns feed automatic guidance production; optional checkpoint
            persistence retains that guidance for resumed roles or later cached-spec editing.
        records: *id033
        note: This is wired trace-fed durable guidance, not demonstrated improved capacity or semantic
          acceptance.
      - scope: Adapter-mediated retained harness update
        assessment: partial
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-obj-frozen-harness
          - runtime.md#rt-rte-candidate-admission
          - runtime.md#rt-bap-retained-harness
          note: Trace evidence feeds automatic candidate admission and the retained behavior-shaping reference
            reaches later rounds/inference.
        records:
        - runtime.md#rt-obj-frozen-harness
        - runtime.md#rt-rte-candidate-admission
        - runtime.md#rt-bap-retained-harness
        note: Wired update/consumer chain is supported; real content responsiveness, initial lineage,
          external durable persistence and callback semantics remain unresolved. Quickstart ignores review
          text.
      - scope: Separately supplied skill artifacts and caller replacements
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-evolved-skill
        - memory.md#mem-obj-skill-artifact
        - runtime.md#rt-rte-artifact-utilities
        - memory.md#mem-obj-checkpoint
        note: Artifacts accept manual/model/arbitrary content without verified trace origin. Checkpoint
          replacement admission is caller-controlled. No qualifying alternative update can be inferred
          from a source label.
      - scope: Raw extraction, outcome/audit and accounting retention alone
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-obj-trajectories
        - memory.md#mem-obj-round-record
        - memory.md#mem-obj-inference-record
        - memory.md#mem-obj-checkpoint
        note: These are evidence/control/output objects rather than standalone learned guidance updates.
          Their use as inputs to qualifying review/harness updates is classified above; raw retention
          alone is insufficient.
      records:
      - memory.md#mem-obj-transcript
      - runtime.md#rt-obj-review-spec
      - memory.md#mem-obj-checkpoint
      - runtime.md#rt-rte-failure-review
      - runtime.md#rt-rte-checkpoint-recovery
      - runtime.md#rt-bap-review-editor
      - runtime.md#rt-obj-frozen-harness
      - runtime.md#rt-rte-candidate-admission
      - runtime.md#rt-bap-retained-harness
      - memory.md#mem-obj-evolved-skill
      - memory.md#mem-obj-skill-artifact
      - runtime.md#rt-rte-artifact-utilities
      - memory.md#mem-obj-trajectories
      - memory.md#mem-obj-round-record
      - memory.md#mem-obj-inference-record
      note: A wired yes exists for retained trace-fed review guidance and the adapter-mediated update
        chain, with unresolved alternatives kept local. This axis uses the write-route definition, not
        the independently unestablished improved-capacity learning property in the reports.
    trace_source:
      assessment: partial
      units:
      - scope: FDCR guidance from scored task-trajectory metadata
        assessment: known
        findings:
        - value: trajectories
          basis: wired
          records: &id034
          - memory.md#mem-obj-trajectories
          - epistemic.md#epi-rte-failure-shaping
          - runtime.md#rt-rte-failure-review
          - memory.md#mem-obj-transcript
          - runtime.md#rt-obj-review-spec
          note: Review production consumes grouped/sampled scored records originating in task trajectories.
        records: *id034
        note: Original task experience is retained as metadata for this route. Raw task messages/tool
          details are excluded from the model display, so they are not separately asserted as sources
          on this branch.
      - scope: Review-guidance continuation from retained role turns
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records: &id035
          - memory.md#mem-obj-transcript
          - runtime.md#rt-rte-failure-review
          - memory.md#mem-obj-checkpoint
          - runtime.md#rt-rte-checkpoint-recovery
          note: Recorded Analyst/Critic/Engineer conversational turns feed subsequent review calls and
            final specification production.
        records: *id035
        note: Role/content review history is recorded conversational work, not environmental event-streams
          merely because it is serialized.
      - scope: Candidate update from fuller extracted failures
        assessment: partial
        findings:
        - value: trajectories
          basis: wired
          records:
          - memory.md#mem-obj-trajectories
          - runtime.md#rt-rte-candidate-admission
          note: Editor receives extracted scored task experience and groups.
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-obj-trajectories
          - runtime.md#rt-rte-candidate-admission
          note: Compacted task-session messages are included in editor evidence.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-obj-trajectories
          - runtime.md#rt-rte-candidate-admission
          note: Copied tool-call fields and arguments are included in the editor-facing extracted evidence.
        records:
        - memory.md#mem-obj-trajectories
        - runtime.md#rt-rte-candidate-admission
        - runtime.md#rt-obj-frozen-harness
        note: These sources are wired into the editor interface, not into metadata-only review. Original
          adapter provenance, actual tool execution and real editor use of the fields are unresolved.
      - scope: Skill construction and caller-supplied/replaced checkpoint or harness content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-evolved-skill
        - memory.md#mem-obj-skill-artifact
        - runtime.md#rt-rte-artifact-utilities
        - memory.md#mem-obj-checkpoint
        - runtime.md#rt-obj-frozen-harness
        note: The possible manual/generated/imported inputs are not traced to original activity records.
          No event-stream or other trace source is established for these opaque admission alternatives.
      records:
      - memory.md#mem-obj-trajectories
      - epistemic.md#epi-rte-failure-shaping
      - runtime.md#rt-rte-failure-review
      - memory.md#mem-obj-transcript
      - runtime.md#rt-obj-review-spec
      - memory.md#mem-obj-checkpoint
      - runtime.md#rt-rte-checkpoint-recovery
      - runtime.md#rt-rte-candidate-admission
      - runtime.md#rt-obj-frozen-harness
      - memory.md#mem-obj-evolved-skill
      - memory.md#mem-obj-skill-artifact
      - runtime.md#rt-rte-artifact-utilities
      note: Task trajectories, recorded review/task turns and editor-facing tool data retain separate
        source warrants. Metadata-only review does not gain raw tool/message sources from the fuller editor
        path. Opaque admissions prevent complete origin coverage.
---

# Ecdysis memory profile

## Comparison rationale

This profile classifies the accepted records, not fresh source facts. No source files were read for this mapping. Evidence is implementation wiring unless a finding says otherwise; no inspected execution or causal comparison supports an observed benefit.

The memory boundary is narrower than all runtime storage. Static role prompts and provider parameters are not accumulated memory of the shipped improvement plane. The generic live harness is included even though its internal form and consumer force are unresolved. Its in-process substrate is known; this does not establish external persistence or deep immutability ([RT-OBJ-frozen-harness](runtime.md#rt-obj-frozen-harness), [RT-BAP-retained-harness](runtime.md#rt-bap-retained-harness)). Opaque artifact metadata and task/output payloads likewise remain visible in the unresolved units rather than being classified from JSON display alone ([MEM-OBJ-skill-artifact](memory.md#mem-obj-skill-artifact), [MEM-OBJ-inference-record](memory.md#mem-obj-inference-record)).

Reconciliation supersedes the epistemic transcript, round-record and evolved-skill declarations with the memory declarations. All classifications cite the canonical [MEM-OBJ-transcript](memory.md#mem-obj-transcript), [MEM-OBJ-round-record](memory.md#mem-obj-round-record) and [MEM-OBJ-evolved-skill](memory.md#mem-obj-evolved-skill). This changes citation identity, not a value or evidence strength. The formatted failure display and proposed-change part remain distinct from extracted trajectories and the whole specification ([EPI-OBJ-failure-context](epistemic.md#epi-obj-failure-context), [EPI-OBJ-proposed-changes](epistemic.md#epi-obj-proposed-changes)).

Read-back direction is operation-relative. A caller's checkpoint-path request and explicit artifact load are pull. Automatic history-tail supply to the next review role is push even within an operator-started workflow. The requested cached return is not counted twice as a second push. Automatic trainer supply of the retained spec/reference has only coarse workflow selection; path names, context/model compatibility and duplicate IDs do not establish a targeted identifier push ([RT-RTE-checkpoint-recovery](runtime.md#rt-rte-checkpoint-recovery), [RT-RTE-failure-review](runtime.md#rt-rte-failure-review), [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities)).

Trace learning here means automatic trace-fed retained guidance with a later consumer, not proven improvement. Optional checkpointed review turns/specification provide that wired chain even without an observed run. The score-retained harness update also has a wired evidence/admission/consumer chain, while its real semantics and initial provenance remain unresolved. The synthetic editor's disregard of the spec prevents review-content attribution, not the existence of delivery and reference replacement ([MEM-OBJ-checkpoint](memory.md#mem-obj-checkpoint), [RT-BAP-review-editor](runtime.md#rt-bap-review-editor), [RT-RTE-candidate-admission](runtime.md#rt-rte-candidate-admission)). Separately stored skills neither inherit that provenance nor acquire task-agent instruction force merely from their tip text ([MEM-ABS-skill-injection](memory.md#mem-abs-skill-injection)).

Curation maps actual reductions, duplicate suppression and withdrawal of checkpoint reliance. It does not map requested conservative review to proven synthesis, first-ID merging to semantic revision, history-tail omission to forgetting, or candidate rejection to deletion of retained advice. Reasons can survive in transcript/specification without reaching the final harness or skill consumer ([MEM-OBJ-transcript](memory.md#mem-obj-transcript), [RT-OBJ-review-spec](runtime.md#rt-obj-review-spec), [RT-RTE-artifact-utilities](runtime.md#rt-rte-artifact-utilities)).

Every supported local finding contributes to the derived union without resolving other units. Missing caller-control facts prevent manual admission classification; missing opaque content/consumer facts prevent complete form, authority and transformation coverage. No local negative is promoted to a system-wide no, and no known pull route makes an unresolved push alternative inapplicable.
