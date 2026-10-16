---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'SkillX memory profile: retained plans, skills, provisional summaries/proposals, retrieval access state
  and task checkpoints.'
run-id: AAS-2026-10-14-skillx-61e3fc8f9aa5-01
source-identity: https://github.com/zjunlp/SkillX
reviewed-boundary: b0047c848dbbcf019363d6d56eef8c558f69aefc
memory-comparison:
  version: 2
  scope: Includes accumulated experience inputs, derived plans and functional/atomic skill parts with access metadata,
    provisional extractor proposals, copied feedback summaries, derived retrieval vectors/cache, and synthetic task/checkpoint
    state; includes unresolved initialization and remaining bundled library/historical artifact alternatives. Excludes
    shipped static prompts/tool schemas, ordinary rollout message accumulation, statistics without a later consumer,
    immediate parser effects, and external base-model weights not established as SkillX memory updates.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Unified library content, metadata and imported experience files
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-skill-library
          - memory.md#mem-obj-trajectory
          note: JSON/JSONL stores experience and saved libraries.
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-skill-library
          - memory.md#mem-obj-trajectory
          note: Loaded dictionaries, lists and library objects retain operative parts.
        records:
        - memory.md#mem-obj-skill-library
        - memory.md#mem-obj-trajectory
        - memory.md#mem-obj-plan-skill
        - memory.md#mem-obj-functional-skill
        - memory.md#mem-obj-atomic-skill
        - memory.md#mem-obj-skill-metadata
        note: Inspected serializers and input loaders establish files and loaded objects; encoding does not add
          a database substrate.
      - scope: Provisional proposals and copied feedback
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-rte-proposal-context
          - memory.md#mem-rte-feedback-summary
          note: Lists, maps and copied histories survive to later model invocations.
        records:
        - memory.md#mem-rte-proposal-context
        - memory.md#mem-rte-feedback-summary
        note: Lifetime is extractor-instance or returned-copy retention, not a persisted file.
      - scope: Derived retrieval arrays and exact-text cache
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-vectors
          note: Arrays and cache live in process.
        - value: vector
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-vectors
          note: Dense plan and skill vectors implement similarity access.
        records:
        - memory.md#mem-obj-retrieval-vectors
        note: Dense index is held in NumPy arrays; FAISS-HNSW is only configuration.
      - scope: Synthetic task results and optional recovery checkpoint
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-task-checkpoint
          note: Optional JSON checkpoint persists tasks and progress.
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-task-checkpoint
          note: Generation results and progress also remain in process.
        records:
        - memory.md#mem-obj-task-checkpoint
        - runtime.md#rt-rte-task-synthesis
        note: Manager results and checkpoint JSON are inspected.
      - scope: Remaining bundled library and historical-result payloads
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-clm-format-boundary
        - memory.md#mem-obj-trajectory
        note: Accepted records inspect only iteration-one shapes and no historical-log update consumer; their remaining
          operative inventory is not classified.
      records:
      - memory.md#mem-obj-skill-library
      - memory.md#mem-obj-trajectory
      - memory.md#mem-obj-plan-skill
      - memory.md#mem-obj-functional-skill
      - memory.md#mem-obj-atomic-skill
      - memory.md#mem-obj-skill-metadata
      - memory.md#mem-rte-proposal-context
      - memory.md#mem-rte-feedback-summary
      - memory.md#mem-obj-retrieval-vectors
      - memory.md#mem-obj-task-checkpoint
      - runtime.md#rt-rte-task-synthesis
      - memory.md#mem-clm-format-boundary
      note: Local stores and derived access structures are resolved; remaining included bundled payloads prevent
        complete inventory coverage. External model weights are not asserted as accumulated SkillX memory.
    representational_form:
      assessment: partial
      units:
      - scope: Plans, functional descriptions/reference bodies and atomic examples at model consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-plan-skill
          - memory.md#mem-obj-functional-skill
          - memory.md#mem-obj-atomic-skill
          - runtime.md#rt-bap-skill-guidance
          note: Plans, descriptions, implementation references and examples enter model guidance.
        records:
        - memory.md#mem-obj-plan-skill
        - memory.md#mem-obj-functional-skill
        - memory.md#mem-obj-atomic-skill
        - runtime.md#rt-bap-skill-guidance
        note: Code-like reference text is interpreted by a model, not installed as callable code.
      - scope: Library keys, skill names/types/tools and checkpoint controls at fixed-code consumers
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-skill-library
          - memory.md#mem-obj-skill-metadata
          - memory.md#mem-obj-task-checkpoint
          note: Keys and tool/type fields determine access and replacement; hashes and indices control recovery.
        records:
        - memory.md#mem-obj-skill-library
        - memory.md#mem-obj-skill-metadata
        - memory.md#mem-obj-task-checkpoint
        note: Field rules operate separately from text interpretation.
      - scope: Experience and copied feedback at extraction consumers
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-trajectory
          - memory.md#mem-rte-feedback-summary
          note: Extraction models interpret history and summary text.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-trajectory
          note: Roles, tool-call fields and reward values feed fixed selection rules.
        records:
        - memory.md#mem-obj-trajectory
        - memory.md#mem-rte-feedback-summary
        note: Messages and action text are separate from role/reward fields.
      - scope: Retrieval vectors and their text/offset/cache mappings
        assessment: known
        findings:
        - value: parametric
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-vectors
          note: Numerical distributed representations drive similarity.
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-vectors
          note: Offsets and exact-text keys associate vectors with content.
        records:
        - memory.md#mem-obj-retrieval-vectors
        note: Dense representations are not readable skill evidence.
      - scope: Task objective/action text and provisional model context
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-task-checkpoint
          - memory.md#mem-rte-proposal-context
          note: Objectives, sequences and proposed skill bodies are interpreted as context.
        records:
        - memory.md#mem-obj-task-checkpoint
        - memory.md#mem-rte-proposal-context
        note: Known model-visible parts; symbolic checkpoint controls are assessed separately.
      - scope: Remaining bundled payloads
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-clm-format-boundary
        note: Only sampled shapes are recorded; remaining content and consumption forms are uninspected.
      records:
      - memory.md#mem-obj-plan-skill
      - memory.md#mem-obj-functional-skill
      - memory.md#mem-obj-atomic-skill
      - runtime.md#rt-bap-skill-guidance
      - memory.md#mem-obj-skill-library
      - memory.md#mem-obj-skill-metadata
      - memory.md#mem-obj-task-checkpoint
      - memory.md#mem-obj-trajectory
      - memory.md#mem-rte-feedback-summary
      - memory.md#mem-obj-retrieval-vectors
      - memory.md#mem-rte-proposal-context
      - memory.md#mem-clm-format-boundary
      note: Mixed operative parts are split by consumer; no form is inferred from a filename or source-native class
        alone.
    lineage:
      assessment: partial
      units:
      - scope: Imported experience
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-trajectory
          note: Caller files and normalization import histories without authenticating origin.
        records:
        - memory.md#mem-obj-trajectory
        note: Import is established; human authorship and original execution/evaluation authenticity are not.
      - scope: Automatic history-to-plan/skill and provisional proposal derivation
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - runtime.md#rt-rte-library-build
          - memory.md#mem-obj-plan-skill
          - memory.md#mem-obj-functional-skill
          - memory.md#mem-obj-atomic-skill
          - memory.md#mem-rte-proposal-context
          note: Selected histories feed model proposals and retained plans/skills.
        records:
        - runtime.md#rt-rte-library-build
        - memory.md#mem-obj-plan-skill
        - memory.md#mem-obj-functional-skill
        - memory.md#mem-obj-atomic-skill
        - memory.md#mem-rte-proposal-context
        note: The derivation is trace extraction even when output fidelity and input provenance are unresolved.
      - scope: Copied feedback summary
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-feedback-summary
          note: Long history feedback feeds summary production.
        records:
        - memory.md#mem-rte-feedback-summary
        note: Substitution derives model-visible memory from recorded feedback.
      - scope: Synthetic task derivation
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-task-checkpoint
          - runtime.md#rt-rte-task-synthesis
          note: Strategy traces feed objective/action proposal generation.
        records:
        - memory.md#mem-obj-task-checkpoint
        - runtime.md#rt-rte-task-synthesis
        note: Real and model-simulated traces remain distinct sources, not verified outcomes.
      - scope: Derived retrieval vectors
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-vectors
          note: Embedding calls compile retained text into derived access vectors.
        records:
        - memory.md#mem-obj-retrieval-vectors
        - runtime.md#rt-cmp-embedding-service
        note: Encoding of library text is known; backend parameter provenance is not.
      - scope: Initial prior plans/skills, direct caller admissions and bundled samples
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-plan-skill
        - memory.md#mem-obj-functional-skill
        - memory.md#mem-rte-proposal-context
        - memory.md#mem-obj-skill-library
        - memory.md#mem-clm-format-boundary
        note: Caller-provided content and sampled artifacts lack authorship/derivation provenance; neither authored
          nor imported is assigned to an unknown initial production path.
      records:
      - memory.md#mem-obj-trajectory
      - runtime.md#rt-rte-library-build
      - memory.md#mem-obj-plan-skill
      - memory.md#mem-obj-functional-skill
      - memory.md#mem-obj-atomic-skill
      - memory.md#mem-rte-proposal-context
      - memory.md#mem-rte-feedback-summary
      - memory.md#mem-obj-task-checkpoint
      - runtime.md#rt-rte-task-synthesis
      - memory.md#mem-obj-retrieval-vectors
      - runtime.md#rt-cmp-embedding-service
      - memory.md#mem-obj-skill-library
      - memory.md#mem-clm-format-boundary
      note: Known derivation paths do not resolve initial content or opaque embedding-model provenance.
    behavioral_authority:
      assessment: partial
      units:
      - scope: History and summaries at plan/skill update models
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-trajectory
          - memory.md#mem-rte-feedback-summary
          note: History and summary text supply contextual evidence to extraction.
        - value: learning
          basis: wired
          records:
          - memory.md#mem-obj-trajectory
          - runtime.md#rt-rte-library-build
          note: Retained experience feeds automatic durable plan/skill updates.
        records:
        - memory.md#mem-obj-trajectory
        - memory.md#mem-rte-feedback-summary
        - runtime.md#rt-rte-library-build
        note: The same material supplies evidence and feeds durable instruction updates; authority does not certify
          truth.
      - scope: Plan and skill text at later extraction and prompt consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-plan-skill
          - memory.md#mem-obj-functional-skill
          - memory.md#mem-obj-atomic-skill
          - memory.md#mem-rte-proposal-context
          - runtime.md#rt-bap-skill-guidance
          note: Selected text supplies reference/context/advice.
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-plan-skill
          - memory.md#mem-obj-functional-skill
          - memory.md#mem-obj-retrieval-vectors
          note: Task/plan and name/document/content determine vector retrieval priority.
        records:
        - memory.md#mem-obj-plan-skill
        - memory.md#mem-obj-functional-skill
        - memory.md#mem-obj-atomic-skill
        - memory.md#mem-rte-proposal-context
        - runtime.md#rt-bap-skill-guidance
        note: Reference implementation advice and task-specific plans are knowledge, not standing host policy or
          callable enforcement.
      - scope: Skill access fields at eligibility, coverage and replacement consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-skill-metadata
          - memory.md#mem-obj-skill-library
          note: Names/types and tool coverage select replacement, partition and exploration scope.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-skill-metadata
          - runtime.md#rt-rte-prompt-prepare
          note: Tool fields can exclude skills from requested retrieval on the truthy filter branch.
        records:
        - memory.md#mem-obj-skill-metadata
        - memory.md#mem-obj-skill-library
        - runtime.md#rt-rte-prompt-prepare
        note: Tools and types constrain actual inclusion; source-task metadata without a reader gets no authority.
      - scope: Task confidence and checkpoint controls at generation/recovery consumers
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-task-checkpoint
          - runtime.md#rt-rte-task-synthesis
          note: Confidence threshold and matching seed hash determine eligibility/reuse.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-task-checkpoint
          - runtime.md#rt-rte-task-synthesis
          note: Mismatch refuses reuse and deletes checkpoint; filters exclude objectives.
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-task-checkpoint
          - runtime.md#rt-rte-task-synthesis
          note: Processed indices select remaining generation batches.
        records:
        - memory.md#mem-obj-task-checkpoint
        - runtime.md#rt-rte-task-synthesis
        note: Threshold and hash checks are consequential but do not validate task solvability.
      - scope: Dense vectors at similarity selector
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-vectors
          note: Cosine similarity ranks and thresholds retained plans/skills.
        records:
        - memory.md#mem-obj-retrieval-vectors
        note: Numerical access state influences relative priority.
      - scope: Initial/remaining sample material at unestablished later consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-format-boundary
        - memory.md#mem-rte-proposal-context
        note: No recorded consumer chain covers all remaining sample content or arbitrary initial content; exercised
          authority is not inferred.
      records:
      - memory.md#mem-obj-trajectory
      - memory.md#mem-rte-feedback-summary
      - runtime.md#rt-rte-library-build
      - memory.md#mem-obj-plan-skill
      - memory.md#mem-obj-functional-skill
      - memory.md#mem-obj-atomic-skill
      - memory.md#mem-rte-proposal-context
      - runtime.md#rt-bap-skill-guidance
      - memory.md#mem-obj-skill-metadata
      - memory.md#mem-obj-skill-library
      - runtime.md#rt-rte-prompt-prepare
      - memory.md#mem-obj-task-checkpoint
      - runtime.md#rt-rte-task-synthesis
      - memory.md#mem-obj-retrieval-vectors
      - memory.md#mem-clm-format-boundary
      note: Consumer-specific knowledge, learning, ranking and control coexist. Static schemas/prompts and parser
        eval are not accumulated memory criteria or authority paths in this scope.
    write_agency:
      assessment: partial
      units:
      - scope: Pipeline and provisional model-proposal admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-library-build
          - memory.md#mem-rte-proposal-context
          note: Software/model admission updates library and provisional context.
        records:
        - runtime.md#rt-rte-library-build
        - memory.md#mem-rte-proposal-context
        note: Starting/configuring construction is not per-content human approval.
      - scope: Copied summary admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-feedback-summary
          note: Parsed model summary automatically replaces copied feedback.
        records:
        - memory.md#mem-rte-feedback-summary
        note: Tag parsing chooses replacement without a human content decision.
      - scope: Embedding cache/index admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-retrieval-vectors
          note: Computed vectors and exact-text cache entries are software-admitted.
        records:
        - memory.md#mem-obj-retrieval-vectors
        note: Software stores computed encodings, including zero-vector fallback.
      - scope: Task generation/checkpoint admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-task-checkpoint
          - runtime.md#rt-rte-task-synthesis
          note: Generation and recovery state are admitted by software.
        records:
        - memory.md#mem-obj-task-checkpoint
        - runtime.md#rt-rte-task-synthesis
        note: Models propose and code parses/filters/saves; operator configuration does not approve objectives.
      - scope: Input initialization, prior content and direct library/export admissions
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-trajectory
        - memory.md#mem-obj-plan-skill
        - memory.md#mem-obj-skill-library
        - memory.md#mem-rte-proposal-context
        - memory.md#mem-clm-format-boundary
        note: Generic caller control does not reveal an explicit human content decision; blocked checked-export
          preflight supplies no successful gate.
      records:
      - runtime.md#rt-rte-library-build
      - memory.md#mem-rte-proposal-context
      - memory.md#mem-rte-feedback-summary
      - memory.md#mem-obj-retrieval-vectors
      - memory.md#mem-obj-task-checkpoint
      - runtime.md#rt-rte-task-synthesis
      - memory.md#mem-obj-trajectory
      - memory.md#mem-obj-plan-skill
      - memory.md#mem-obj-skill-library
      - memory.md#mem-clm-format-boundary
      note: Automatic transformations are known; initial and direct-caller admission control prevents a complete
        automatic/manual classification.
    curation_operations:
      assessment: partial
      units:
      - scope: Feedback compression
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-feedback-summary
          note: Selected long feedback is compressed into substituted context.
        records:
        - memory.md#mem-rte-feedback-summary
        note: Summarization reduces retained feedback for subsequent extraction; unverified fidelity does not convert
          it to synthesis.
      - scope: Cluster merge and library maintenance
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - runtime.md#rt-rte-library-build
          note: Cluster members are combined into reusable merged representation.
        - value: dedup
          basis: wired
          records:
          - memory.md#mem-obj-skill-library
          note: Incoming atomic entries covered by functional tools are suppressed; no global old-entry sweep is
            implied.
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-obj-skill-library
          - memory.md#mem-rte-proposal-context
          note: Same-name replacements revise retained entries; provisional maps can replace proposals.
        records:
        - runtime.md#rt-rte-library-build
        - memory.md#mem-obj-skill-library
        - memory.md#mem-obj-functional-skill
        - memory.md#mem-rte-proposal-context
        note: Transformations have wired routes, not observed quality gains.
      - scope: Synthetic-task duplicate filtering and checkpoint mismatch
        assessment: known
        findings:
        - value: dedup
          basis: wired
          records:
          - runtime.md#rt-rte-task-synthesis
          note: Duplicate-query tracker removes repeated objectives.
        records:
        - memory.md#mem-obj-task-checkpoint
        - runtime.md#rt-rte-task-synthesis
        note: Normalized duplicate removal is distinct from hash-based checkpoint deletion; deletion is not history-preserving
          invalidation.
      - scope: Semantic novelty in model extraction, plan combination and merge alternatives
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-library-build
        - memory.md#mem-obj-plan-skill
        - memory.md#mem-obj-functional-skill
        note: Actual input/output claim relations are not established; no synthesis value is licensed from a generative
          route name alone.
      - scope: Remaining optional transformations and bundled artifact maintenance
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-clm-format-boundary
        - runtime.md#rt-rte-task-synthesis
        note: Optional parsers and remaining sample content are not exhaustively assessed in accepted records.
      records:
      - memory.md#mem-rte-feedback-summary
      - runtime.md#rt-rte-library-build
      - memory.md#mem-obj-skill-library
      - memory.md#mem-obj-functional-skill
      - memory.md#mem-rte-proposal-context
      - memory.md#mem-obj-task-checkpoint
      - runtime.md#rt-rte-task-synthesis
      - memory.md#mem-obj-plan-skill
      - memory.md#mem-clm-format-boundary
      note: Consolidation, duplicate suppression and revision are positive witnesses. Unknown semantic outputs and
        optional branches prevent exhaustive operation coverage; index rebuild alone adds no curation value.
    read_back_direction:
      assessment: partial
      units:
      - scope: Saved-library service task/step requests
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-prompt-prepare
          note: Caller requests retained plans/skills from the service for a task or step.
        records:
        - runtime.md#rt-rte-prompt-prepare
        note: Requested selection and returned prompt/material are pull; subsidiary semantic retrieval is not counted
          as another push. This unit excludes the alternate public rewrite helper.
      - scope: Alternative public PlanRewriteService.get_pseudo_plan invocation
        assessment: known
        findings:
        - value: pull
          basis: afforded
          records:
          - runtime.md#rt-rte-prompt-prepare
          note: Public helper affords caller-requested reference-plan retrieval and pseudo-plan/metadata return.
        records:
        - runtime.md#rt-rte-prompt-prepare
        note: Internal progression is wired, but no shipped caller or later delivery is established; this alternative
          invocation retains afforded rather than service-route wired read-back evidence.
      - scope: Provisional extraction context across invocations
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-proposal-context
          note: Sequential functional calls and atomic tool calls receive automatically selected prior proposals.
        records:
        - memory.md#mem-rte-proposal-context
        note: Code supplies proposals to a later extraction model without that consumer requesting stored proposals.
      - scope: Copied feedback to later extractors
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-feedback-summary
          - runtime.md#rt-rte-library-build
          note: Later extraction receives the retained summary copy selected upstream.
        records:
        - memory.md#mem-rte-feedback-summary
        - runtime.md#rt-rte-library-build
        note: Substitution is automatically included in subsequent invocation input.
      - scope: Task-manager checkpoint recovery
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-task-checkpoint
          - runtime.md#rt-rte-task-synthesis
          note: Automatic recovery supplies saved results/progress to continued generation.
        records:
        - memory.md#mem-obj-task-checkpoint
        - runtime.md#rt-rte-task-synthesis
        note: Code resumes matching checkpoint state on generation startup; no caller request for its retained entries
          is recorded.
      - scope: Remaining sample/historical artifacts and unspecified public API consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-format-boundary
        - memory.md#mem-rte-self-filter
        note: Storage and selection capability do not establish later delivery for these alternatives.
      records:
      - runtime.md#rt-rte-prompt-prepare
      - memory.md#mem-rte-proposal-context
      - memory.md#mem-rte-feedback-summary
      - runtime.md#rt-rte-library-build
      - memory.md#mem-obj-task-checkpoint
      - runtime.md#rt-rte-task-synthesis
      - memory.md#mem-clm-format-boundary
      - memory.md#mem-rte-self-filter
      note: Pull library service and push internal context/recovery routes coexist; the absence of background injection
        on the library service is not a system-wide pull-only finding.
    read_back_signal:
      assessment: partial
      units:
      - scope: Functional proposal-list supply
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-proposal-context
          note: Next functional extraction invocation receives available provisional list.
        records:
        - memory.md#mem-rte-proposal-context
        note: Trigger is next plan step; selector supplies the currently available augmented list rather than a
          targeted semantic match.
      - scope: Atomic/hybrid proposal-map supply
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-proposal-context
          note: Tool identity match in existing_skills selects the prior tool entry.
        records:
        - memory.md#mem-rte-proposal-context
        note: Trigger is tool extraction; actual tool-name lookup selects a retained proposal for delivery.
      - scope: Copied summary supply
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-feedback-summary
          - runtime.md#rt-rte-library-build
          note: Prepared copied history supplies its summaries to subsequent extractors.
        records:
        - memory.md#mem-rte-feedback-summary
        - runtime.md#rt-rte-library-build
        note: Long-feedback role/length selects replacement; later assembled history carries that replacement, not
          embedding-ranked memory.
      - scope: Checkpoint recovery supply
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-task-checkpoint
          - runtime.md#rt-rte-task-synthesis
          note: Available matching checkpoint supplies results/progress as a whole.
        records:
        - memory.md#mem-obj-task-checkpoint
        - runtime.md#rt-rte-task-synthesis
        note: Generation startup and seed-hash validity select whole checkpoint; processed indices control continuation,
          not identity-targeted delivered content.
      - scope: Requested library retrieval
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-prompt-prepare
        note: Push signal does not apply to fulfilling explicit task/step requests; cosine retrieval remains a pull
          selector.
      - scope: Unestablished remaining artifact/API delivery
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-clm-format-boundary
        - memory.md#mem-rte-self-filter
        note: No complete direction account licenses a signal or inapplicability for these alternatives.
      records:
      - memory.md#mem-rte-proposal-context
      - memory.md#mem-rte-feedback-summary
      - runtime.md#rt-rte-library-build
      - memory.md#mem-obj-task-checkpoint
      - runtime.md#rt-rte-task-synthesis
      - runtime.md#rt-rte-prompt-prepare
      - memory.md#mem-clm-format-boundary
      - memory.md#mem-rte-self-filter
      note: Push selectors have coarse and identifier signals; embedding and optional model judgment on requested
        retrieval do not establish push signals.
    trace_learning:
      assessment: partial
      units:
      - scope: Experience-to-durable library write and later inference consumer
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - runtime.md#rt-rte-library-build
          - memory.md#mem-obj-trajectory
          - runtime.md#rt-rte-prompt-prepare
          note: Histories feed saved reusable plans/skills, later loaded for guidance.
        records:
        - runtime.md#rt-rte-library-build
        - memory.md#mem-obj-trajectory
        - memory.md#mem-obj-plan-skill
        - memory.md#mem-obj-functional-skill
        - memory.md#mem-obj-atomic-skill
        - runtime.md#rt-rte-prompt-prepare
        note: Automatic trace-fed instructional artifacts persist and have a later requested context route; successful
          learning is not asserted.
      - scope: Feedback summary and subsequent extraction
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-feedback-summary
          - runtime.md#rt-rte-library-build
          note: Recorded feedback automatically becomes retained model-visible summary context.
        records:
        - memory.md#mem-rte-feedback-summary
        - runtime.md#rt-rte-library-build
        note: Returned-copy retention and later invocation suffice even without a separately saved summary file.
      - scope: Provisional proposal update and subsequent model invocation
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-proposal-context
          - runtime.md#rt-rte-library-build
          note: Trace-derived proposals are automatically retained for later extraction guidance.
        records:
        - memory.md#mem-rte-proposal-context
        - runtime.md#rt-rte-library-build
        note: Instance/list lifetime crosses consumer calls; final-library rejection does not erase this path.
      - scope: Synthetic objectives/checkpoint recovery
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-task-checkpoint
        - runtime.md#rt-rte-task-synthesis
        note: Trace-fed objectives persist, but accepted records do not establish task execution or exactly how
          recovered objective content shapes a later model; symbolic resume progress alone does not settle that
          relation.
      - scope: Arbitrary initialization, remaining historical artifacts and opaque service changes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-trajectory
        - memory.md#mem-clm-format-boundary
        - runtime.md#rt-cmp-embedding-service
        note: Unknown input origin and absent recorded provider-update internals cannot establish qualifying writes
          or bounded absence.
      records:
      - runtime.md#rt-rte-library-build
      - memory.md#mem-obj-trajectory
      - memory.md#mem-obj-plan-skill
      - memory.md#mem-obj-functional-skill
      - memory.md#mem-obj-atomic-skill
      - runtime.md#rt-rte-prompt-prepare
      - memory.md#mem-rte-feedback-summary
      - memory.md#mem-rte-proposal-context
      - memory.md#mem-obj-task-checkpoint
      - runtime.md#rt-rte-task-synthesis
      - memory.md#mem-clm-format-boundary
      - runtime.md#rt-cmp-embedding-service
      note: Wired yes routes establish trace-fed memory capacity, not observed improvement. Unresolved alternatives
        remain local; no system-wide no is warranted.
    trace_source:
      assessment: partial
      units:
      - scope: Library and provisional-context extraction from normalized histories
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-obj-trajectory
          - runtime.md#rt-rte-library-build
          - memory.md#mem-rte-proposal-context
          note: Recorded user/assistant work-session turns enter extraction.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-obj-trajectory
          - runtime.md#rt-rte-library-build
          - memory.md#mem-rte-proposal-context
          note: Recorded tool calls, code actions and execution feedback enter extraction.
        - value: trajectories
          basis: wired
          records:
          - memory.md#mem-obj-trajectory
          - runtime.md#rt-rte-library-build
          note: Task histories link actions/observations with supplied outcomes for extraction.
        records:
        - memory.md#mem-obj-trajectory
        - runtime.md#rt-rte-library-build
        - memory.md#mem-rte-proposal-context
        note: Recorded turns and tool activity are consumed; original authenticity remains unresolved. Sequence
          linkage into trajectories is retained.
      - scope: Feedback-summary qualifying write
        assessment: partial
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-feedback-summary
          note: Recorded user-turn feedback can feed summary replacement.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-feedback-summary
          note: Recorded tool feedback and preceding action feed summary replacement.
        records:
        - memory.md#mem-rte-feedback-summary
        - memory.md#mem-obj-trajectory
        note: User/tool feedback and preceding action are known; arbitrary supplied body origin remains unresolved.
      - scope: Synthetic-task recovery and remaining opaque/initial routes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-task-checkpoint
        - runtime.md#rt-rte-task-synthesis
        - memory.md#mem-obj-trajectory
        - memory.md#mem-clm-format-boundary
        note: Simulated versus real trace inputs are recorded but their qualifying later behavior-shaping consumer
          remains unresolved; arbitrary input and remaining artifact provenance prevent exhaustive original-source
          classification.
      records:
      - memory.md#mem-obj-trajectory
      - runtime.md#rt-rte-library-build
      - memory.md#mem-rte-proposal-context
      - memory.md#mem-rte-feedback-summary
      - memory.md#mem-obj-task-checkpoint
      - runtime.md#rt-rte-task-synthesis
      - memory.md#mem-clm-format-boundary
      note: Source content, not adapter labels, supplies session, tool and linked-trajectory findings. Opaque original
        origins and unresolved qualifying task routes prevent complete source coverage; no event-stream value is
        inferred.
---

# SkillX memory profile

## Comparison rationale

This profile classifies accepted records, not source execution. All positive findings concern inspected wiring unless explicitly marked otherwise. No record establishes exercised downstream compliance, improved capacity or causal gains. Coverage remains partial where initial content, remaining bundled artifacts, optional transformations or trace origins are unresolved. Those limits do not erase automatic trace-to-instruction writes.

Reference implementations are natural-language material at their model consumer, not symbolic executable tools. Library keys, eligibility fields and checkpoint controls are symbolic at their fixed-code consumers. Dense retrieval encodings are parametric access material; the numerical vectors are not provider weights. The persisted FAISS-HNSW label establishes no additional implemented index substrate. See [MEM-OBJ-functional-skill](memory.md#mem-obj-functional-skill), [MEM-OBJ-retrieval-vectors](memory.md#mem-obj-retrieval-vectors) and [MEM-OBJ-skill-library](memory.md#mem-obj-skill-library).

History has knowledge authority as evidence and learning authority at the durable update consumer. Output plans and reference skills provide contextual advice, rather than standing host instructions. The downstream formatter route is distinct from the update route; neither requires observed improvement for wired classification. See [RT-RTE-library-build](runtime.md#rt-rte-library-build) and [RT-BAP-skill-guidance](runtime.md#rt-bap-skill-guidance).

Requested service task/step retrieval is wired pull even when code automatically makes subsidiary vector queries. The alternative public `PlanRewriteService.get_pseudo_plan` invocation is a separate afforded pull finding: its wired internal progression does not establish a shipped caller or later delivery. In contrast, subsequent extraction models do not request the provisional proposal list or prior tool entry: code selects and supplies them. Whole-list availability is coarse; the atomic map's actual tool identity match is identifier selection. Automatically substituted feedback and checkpoint recovery are separate coarse supply operations, not evidence of unsolicited embedding-based push. See [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare), [MEM-RTE-proposal-context](memory.md#mem-rte-proposal-context), [MEM-RTE-feedback-summary](memory.md#mem-rte-feedback-summary) and [MEM-OBJ-task-checkpoint](memory.md#mem-obj-task-checkpoint).

Consolidation does not require verified semantic faithfulness. Feedback compression and cluster merging have implemented reduction routes; semantic novelty in actual model outputs remains indeterminate, so synthesis is not inferred. Same-name revision does not imply history-preserving invalidation, global predecessor withdrawal or rollback. See [MEM-RTE-feedback-summary](memory.md#mem-rte-feedback-summary), [RT-RTE-library-build](runtime.md#rt-rte-library-build) and [MEM-OBJ-skill-library](memory.md#mem-obj-skill-library).

Reconciliation supersedes EPI-RTE-feedback-summary with MEM-RTE-feedback-summary and EPI-OBJ-plan-content with MEM-OBJ-plan-skill. All classifications use the canonical memory records. Combined raw/summary, skill-content and synthetic-task records are not superseded by their noncoextensive parts. The corrected exporter preflight remains blocked, and the afforded public rewrite helper does not repair the shipped service mismatch or establish persistence. See [EPI-RTE-export-validation](epistemic.md#epi-rte-export-validation), [RT-RTE-prompt-prepare](runtime.md#rt-rte-prompt-prepare) and [MEM-CLM-format-boundary](memory.md#mem-clm-format-boundary).

Source-read log: none. Classification used only the supplied accepted members and reconciliation; no frozen-source ambiguity required an additional read.
