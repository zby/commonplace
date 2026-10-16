---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: Letta Code memory comparison of local MemFS, retained session/summary state, reflection and
  attached/hosted alternatives at the frozen commit.
run-id: AAS-2026-10-12-letta-code-be76afeab9b7-01
source-identity: https://github.com/letta-ai/letta-code
reviewed-boundary: 271f119dcf37d58649a18e6c733386b3c710a456
memory-comparison:
  version: 2
  scope: Retained core/deferred MemFS bodies and access metadata; agent and attached skill content changed
    or accumulated through use; raw local session history, derived compaction summaries and their checkpoint/access
    structures; reflection payload/progress, arena disposition records and mutable memory policy; their
    admission, maintenance and later consumers; opaque hosted agent/conversation and attached non-skill
    memory alternatives. Excludes shipped static prompts/bundled skills, arbitrary uncaptured extension
    code, package replacement and the separate executable mod-learning builder. Optional mirrors and feedback
    uploads have no established later memory consumer; their storage alone is not read-back. Provider
    inference weights are not an established accumulated-memory surface; external memory update internals
    remain unresolved.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Local core/deferred MemFS and agent or attached skill files
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-core-memory
          - memory.md#mem-obj-deferred-memory
          - memory.md#mem-rte-core-projection
          - memory.md#mem-rte-deferred-read
          - memory.md#mem-obj-agent-skills
          - memory.md#mem-rte-skill-loading
          note: Markdown bodies, indexes and skill resources occupy local filesystem files.
        - value: repo
          basis: wired
          records:
          - memory.md#mem-obj-core-memory
          - memory.md#mem-obj-deferred-memory
          - memory.md#mem-rte-core-projection
          - memory.md#mem-rte-deferred-read
          - memory.md#mem-obj-agent-skills
          - memory.md#mem-rte-skill-loading
          note: Committed MemFS and attached repositories supply revisioned retained content and access
            structures.
        records:
        - memory.md#mem-obj-core-memory
        - memory.md#mem-obj-deferred-memory
        - memory.md#mem-rte-core-projection
        - memory.md#mem-rte-deferred-read
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-rte-skill-loading
        note: Bodies and their access paths are retained in files and Git checkouts; project/global acquisition
          is uncaptured but does not obscure the recorded file substrate.
      - scope: Raw local transcript, retained summary and active cached projection
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-local-transcript
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-transcript-compaction
          note: Session entries and compaction entries are appended to local JSONL files.
        - value: in-memory
          basis: wired
          records:
          - runtime.md#rt-obj-local-transcript
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-transcript-compaction
          note: Resident message/index caches and summary-plus-tail projection retain loaded state between
            invocations.
        records:
        - runtime.md#rt-obj-local-transcript
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-transcript-compaction
        note: JSONL persistence and resident message/index caches are both recorded; this does not classify
          the uninspected replay algorithm.
      - scope: Reflection payload, manifest and successful-progress checkpoints
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-reflection-payload
          - memory.md#mem-bap-reflection-progress
          - memory.md#mem-rte-reflection-integration
          note: Transcript payloads and progress state use local files.
        records:
        - memory.md#mem-obj-reflection-payload
        - memory.md#mem-bap-reflection-progress
        - memory.md#mem-rte-reflection-integration
        note: Local slice files and locked progress updates are the inspected retained parts.
      - scope: Mutable MemFS policy and arena disposition records
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-memory-constraints
          - memory.md#mem-rte-memory-admission
          - epistemic.md#epi-rte-commit-admission
          - memory.md#mem-rte-arena-selection
          - epistemic.md#epi-obj-arena-choice
          note: Policy and choice records occupy local files.
        - value: repo
          basis: wired
          records:
          - memory.md#mem-obj-memory-constraints
          - memory.md#mem-rte-memory-admission
          - epistemic.md#epi-rte-commit-admission
          - memory.md#mem-rte-arena-selection
          - epistemic.md#epi-obj-arena-choice
          note: Tracked .memfs.config.json is revisioned policy in the memory repository.
        records:
        - memory.md#mem-obj-memory-constraints
        - memory.md#mem-rte-memory-admission
        - epistemic.md#epi-rte-commit-admission
        - memory.md#mem-rte-arena-selection
        - epistemic.md#epi-obj-arena-choice
        note: Tracked JSON policy/Git metadata and local run JSON/choice JSONL are retained; no feedback-training
          substrate is inferred.
      - scope: Hosted agent/conversation and non-skill attached-memory payloads
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hosted-memory
        - memory.md#mem-rte-repository-sync
        note: The client contract and readable mounts do not reveal external persistence; no service-object,
          database, vector or weight substrate can be established.
      records:
      - memory.md#mem-obj-core-memory
      - memory.md#mem-obj-deferred-memory
      - memory.md#mem-rte-core-projection
      - memory.md#mem-rte-deferred-read
      - memory.md#mem-obj-agent-skills
      - memory.md#mem-rte-skill-loading
      - runtime.md#rt-obj-local-transcript
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-transcript-compaction
      - memory.md#mem-obj-reflection-payload
      - memory.md#mem-bap-reflection-progress
      - memory.md#mem-rte-reflection-integration
      - memory.md#mem-obj-memory-constraints
      - memory.md#mem-rte-memory-admission
      - epistemic.md#epi-rte-commit-admission
      - memory.md#mem-rte-arena-selection
      - epistemic.md#epi-obj-arena-choice
      - memory.md#mem-obj-hosted-memory
      - memory.md#mem-rte-repository-sync
      note: Local retained files, Git access structures and resident transcript projections are classified;
        external retained state has no established substrate. Optional mirrors have no recorded later
        consumer and are not additional operative memory units.
    representational_form:
      assessment: partial
      units:
      - scope: Core/deferred bodies, index prose and loaded skill procedure text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-core-memory
          - memory.md#mem-obj-deferred-memory
          - memory.md#mem-rte-core-projection
          - memory.md#mem-rte-deferred-read
          - memory.md#mem-obj-agent-skills
          - memory.md#mem-rte-skill-loading
          note: Facts, preferences, descriptions and procedures reach turn models as prose.
        records:
        - memory.md#mem-obj-core-memory
        - memory.md#mem-obj-deferred-memory
        - memory.md#mem-rte-core-projection
        - memory.md#mem-rte-deferred-read
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-rte-skill-loading
        note: These bodies receive consequences through model interpretation, independently of delivery
          role.
      - scope: MemFS paths/frontmatter, skill discovery identity and mutable layout policy
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-core-memory
          - memory.md#mem-obj-deferred-memory
          - memory.md#mem-rte-core-projection
          - memory.md#mem-rte-deferred-read
          - memory.md#mem-obj-agent-skills
          - memory.md#mem-rte-skill-loading
          - memory.md#mem-obj-memory-constraints
          - memory.md#mem-rte-memory-admission
          - epistemic.md#epi-rte-commit-admission
          note: Paths, names, policy limits and read-only globs determine selection or admissibility.
        records:
        - memory.md#mem-obj-core-memory
        - memory.md#mem-obj-deferred-memory
        - memory.md#mem-rte-core-projection
        - memory.md#mem-rte-deferred-read
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-rte-skill-loading
        - memory.md#mem-obj-memory-constraints
        - memory.md#mem-rte-memory-admission
        - epistemic.md#epi-rte-commit-admission
        note: The path/name/layout fields have fixed compiler, discovery or admission consumers.
      - scope: Raw transcript prose, compaction summary and normalized reflection evidence text
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-obj-local-transcript
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-transcript-compaction
          - memory.md#mem-obj-reflection-payload
          - memory.md#mem-bap-reflection-progress
          - memory.md#mem-rte-reflection-integration
          note: Session content and derived summaries are interpreted by later turn or reflection models.
        records:
        - runtime.md#rt-obj-local-transcript
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-transcript-compaction
        - memory.md#mem-obj-reflection-payload
        - memory.md#mem-bap-reflection-progress
        - memory.md#mem-rte-reflection-integration
        note: Prose is distinct from its JSON/session envelope; completeness and fidelity remain unestablished.
      - scope: Transcript envelope, compaction checkpoint, reflection manifest/progress and arena disposition
          labels
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-local-transcript
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-transcript-compaction
          - memory.md#mem-obj-reflection-payload
          - memory.md#mem-bap-reflection-progress
          - memory.md#mem-rte-reflection-integration
          - memory.md#mem-rte-arena-selection
          - epistemic.md#epi-obj-arena-choice
          note: IDs and checkpoint/disposition fields govern history projection, maintenance scope and
            branch selection.
        records:
        - runtime.md#rt-obj-local-transcript
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-transcript-compaction
        - memory.md#mem-obj-reflection-payload
        - memory.md#mem-bap-reflection-progress
        - memory.md#mem-rte-reflection-integration
        - memory.md#mem-rte-arena-selection
        - epistemic.md#epi-obj-arena-choice
        note: IDs, kept-entry metadata, replay boundaries and chosen labels have fixed store/selector/finalizer
          consumers.
      - scope: Skill companion-resource behavior and uncaptured dynamic skill contents
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-rte-skill-loading
        note: Scripts can supply symbolic behavior when invoked, but records do not establish their actual
          memory-consumption routes or contents.
      - scope: Opaque hosted memory payload and encoding
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hosted-memory
        - memory.md#mem-rte-repository-sync
        note: Readable response metadata cannot classify the payload consumed by the server; numerical
          or symbolic alternatives remain unresolved.
      records:
      - memory.md#mem-obj-core-memory
      - memory.md#mem-obj-deferred-memory
      - memory.md#mem-rte-core-projection
      - memory.md#mem-rte-deferred-read
      - memory.md#mem-obj-agent-skills
      - memory.md#mem-rte-skill-loading
      - memory.md#mem-obj-memory-constraints
      - memory.md#mem-rte-memory-admission
      - epistemic.md#epi-rte-commit-admission
      - runtime.md#rt-obj-local-transcript
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-transcript-compaction
      - memory.md#mem-obj-reflection-payload
      - memory.md#mem-bap-reflection-progress
      - memory.md#mem-rte-reflection-integration
      - memory.md#mem-rte-arena-selection
      - epistemic.md#epi-obj-arena-choice
      - memory.md#mem-obj-hosted-memory
      - memory.md#mem-rte-repository-sync
      note: Local prose and symbolic selectors are separated by consumption; hosted encoding and uncaptured
        executable skill resources remain unresolved. Provider model weights are inference components,
        not an established accumulated-memory part.
    lineage:
      assessment: partial
      units:
      - scope: New text proposed through ordinary model memory editing
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-rte-memory-admission
          note: An agent can propose memory text and commit it through the recorded authoring route.
        records:
        - memory.md#mem-rte-memory-admission
        note: This unit names model-produced edits, not all caller-supplied creation bodies.
      - scope: Backup replacement and remote repository import paths
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - epistemic.md#epi-rte-memory-restore
          - memory.md#mem-obj-core-memory
          - memory.md#mem-rte-repository-sync
          note: Restore copies an external backup directory; remote repository history can enter the local
            checkout.
        records:
        - epistemic.md#epi-rte-memory-restore
        - memory.md#mem-obj-core-memory
        - memory.md#mem-rte-repository-sync
        note: Imported directory/history provenance is classified at the entry path, without authenticating
          its prior claims.
      - scope: Transcript-derived compaction summary and reflection memory/skill proposal paths
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-rte-transcript-compaction
          - epistemic.md#epi-rte-summary-generation
          - epistemic.md#epi-rte-summary-retention
          - memory.md#mem-rte-reflection-integration
          - epistemic.md#epi-rte-reflection-guidance
          note: Automatic summary generation and reflection proposal production use recorded conversation
            activity.
        records:
        - memory.md#mem-rte-transcript-compaction
        - epistemic.md#epi-rte-summary-generation
        - epistemic.md#epi-rte-summary-retention
        - memory.md#mem-rte-reflection-integration
        - epistemic.md#epi-rte-reflection-guidance
        note: The routes wire bounded conversational inputs to retained derived prose; reliable semantic
          extraction is not inferred.
      - scope: Selected reflection transcript payload and progress derived from conversation capture
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-reflection-payload
          - memory.md#mem-bap-reflection-progress
          - memory.md#mem-rte-reflection-integration
          note: Conversation slices and reflected-through state derive from captured session activity.
        records:
        - memory.md#mem-obj-reflection-payload
        - memory.md#mem-bap-reflection-progress
        - memory.md#mem-rte-reflection-integration
        note: Capture, range selection and normalization identify this derivation path; missing normalization
          details do not identify new source claims.
      - scope: Initial create-body content and preexisting core/deferred/skill content provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-core-memory
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-rte-memory-admission
        note: Caller authorship and prior derivation are unresolved; known later edits cannot settle initialization
          or dynamic skill provenance.
      - scope: Migration/import guidance, generic-worker repair derivations and full replay transformations
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-reflection-integration
        - memory.md#mem-rte-memory-admission
        - runtime.md#rt-obj-local-transcript
        note: Available source was not fully inspected; no additional compiled or extraction provenance
          is established.
      - scope: Hosted initial content and embedding provenance
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hosted-memory
        - memory.md#mem-rte-repository-sync
        note: Service internals are outside the source; local display metadata does not settle initial
          or embedding lineage.
      records:
      - memory.md#mem-rte-memory-admission
      - epistemic.md#epi-rte-memory-restore
      - memory.md#mem-obj-core-memory
      - memory.md#mem-rte-repository-sync
      - memory.md#mem-rte-transcript-compaction
      - epistemic.md#epi-rte-summary-generation
      - epistemic.md#epi-rte-summary-retention
      - memory.md#mem-rte-reflection-integration
      - epistemic.md#epi-rte-reflection-guidance
      - memory.md#mem-obj-reflection-payload
      - memory.md#mem-bap-reflection-progress
      - memory.md#mem-obj-agent-skills
      - runtime.md#rt-obj-local-transcript
      - memory.md#mem-obj-hosted-memory
      note: Known write paths do not resolve initial authorship, imported material provenance or hosted
        embedding origins. Authored, imported and trace-extracted coexist on different derivation paths,
        not as a complete provenance list.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Core/deferred factual prose at later turn-model context consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-obj-core-memory
          - memory.md#mem-obj-deferred-memory
          - memory.md#mem-rte-core-projection
          - memory.md#mem-rte-deferred-read
          - memory.md#mem-bap-memory-context
          note: Retained facts and context are evidence/reference supplied to a later turn model.
        records:
        - memory.md#mem-obj-core-memory
        - memory.md#mem-obj-deferred-memory
        - memory.md#mem-rte-core-projection
        - memory.md#mem-rte-deferred-read
        - memory.md#mem-bap-memory-context
        note: Compiler and tool delivery are wired; model obedience and factual endorsement are not.
      - scope: Retained preference/direction prose and loaded skill procedure at later turn-model consumers
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - memory.md#mem-obj-core-memory
          - memory.md#mem-obj-deferred-memory
          - memory.md#mem-rte-core-projection
          - memory.md#mem-rte-deferred-read
          - memory.md#mem-obj-agent-skills
          - memory.md#mem-rte-skill-loading
          - memory.md#mem-bap-memory-context
          note: Preferences and skill procedures supply model-interpreted directions rather than host
            enforcement.
        records:
        - memory.md#mem-obj-core-memory
        - memory.md#mem-obj-deferred-memory
        - memory.md#mem-rte-core-projection
        - memory.md#mem-rte-deferred-read
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-rte-skill-loading
        - memory.md#mem-bap-memory-context
        note: This unit names standing directions/procedures, not every fact in the same files.
      - scope: Retained raw session and previous summary at compaction/reflection update consumers
        assessment: known
        findings:
        - value: learning
          basis: wired
          records:
          - memory.md#mem-rte-transcript-compaction
          - epistemic.md#epi-rte-summary-generation
          - epistemic.md#epi-rte-summary-retention
          - memory.md#mem-rte-reflection-integration
          - epistemic.md#epi-rte-reflection-guidance
          - memory.md#mem-obj-reflection-payload
          note: Recorded experience is consumed to produce retained summaries or revise durable behavior-shaping
            memory/skills.
        records:
        - memory.md#mem-rte-transcript-compaction
        - epistemic.md#epi-rte-summary-generation
        - epistemic.md#epi-rte-summary-retention
        - memory.md#mem-rte-reflection-integration
        - epistemic.md#epi-rte-reflection-guidance
        - memory.md#mem-obj-reflection-payload
        note: Traces feed durable context or memory/skill updates, independently of downstream knowledge/instruction
          authority.
      - scope: Raw history and retained compaction prose at later turn-model consumer
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - runtime.md#rt-obj-local-transcript
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-transcript-compaction
          - runtime.md#rt-bap-provider-context
          note: Selected messages and summary account supply prior context to subsequent inference.
        records:
        - runtime.md#rt-obj-local-transcript
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-transcript-compaction
        - runtime.md#rt-bap-provider-context
        note: The selected history/summary provides context; no reliable imperative content or enforcement
          is inferred from a user-role wrapper.
      - scope: Stored transcript text and conversation summary at local search selector
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-transcript-search
          - runtime.md#rt-obj-local-transcript
          note: Retained text and summary term matches influence which results rank or match.
        records:
        - memory.md#mem-rte-transcript-search
        - runtime.md#rt-obj-local-transcript
        note: Query/term-match selection and ranked returned results establish a ranking input; complete
          ranking code remains unaudited.
      - scope: Mutable memory constraints at hook-covered commit admission
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - memory.md#mem-obj-memory-constraints
          - memory.md#mem-rte-memory-admission
          - epistemic.md#epi-rte-commit-admission
          note: Retained policy criteria determine whether staged memory conforms.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-memory-constraints
          - memory.md#mem-rte-memory-admission
          - epistemic.md#epi-rte-commit-admission
          note: Policy violations can veto the ordinary hook-covered commit.
        records:
        - memory.md#mem-obj-memory-constraints
        - memory.md#mem-rte-memory-admission
        - epistemic.md#epi-rte-commit-admission
        note: Budgets/layout/read-only criteria have a program consumer; hook bypass and restore limit
          the enforcement boundary.
      - scope: Reflection successful-progress IDs and counters at later maintenance selector
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-reflection-payload
          - memory.md#mem-bap-reflection-progress
          - memory.md#mem-rte-reflection-integration
          note: Reflected-through IDs, replay distinctions and thresholds select later transcript windows
            or attempts.
        records:
        - memory.md#mem-obj-reflection-payload
        - memory.md#mem-bap-reflection-progress
        - memory.md#mem-rte-reflection-integration
        note: Progress is consumed symbolically rather than as model advice.
      - scope: Attachment membership at shared-skill discovery
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-hosted-memory
          - memory.md#mem-rte-repository-sync
          - memory.md#mem-obj-agent-skills
          - memory.md#mem-rte-skill-loading
          note: Current attachment membership selects which shared skill sources discovery may use.
        records:
        - memory.md#mem-obj-hosted-memory
        - memory.md#mem-rte-repository-sync
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-rte-skill-loading
        note: This unit covers local eligibility, not the external attachment enforcement contract.
      - scope: Arena choice log feedback consumer
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-arena-selection
        - epistemic.md#epi-obj-arena-choice
        note: Choice controls current integration, but no later learning or selection consumer of its
          persisted log is established.
      - scope: Hosted non-skill consumers and generic-worker repair/update effects
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hosted-memory
        - memory.md#mem-rte-repository-sync
        - memory.md#mem-rte-reflection-integration
        note: Server consumers are opaque and precise repair behavior is uninspected; no global authority
          inventory follows.
      records:
      - memory.md#mem-obj-core-memory
      - memory.md#mem-obj-deferred-memory
      - memory.md#mem-rte-core-projection
      - memory.md#mem-rte-deferred-read
      - memory.md#mem-bap-memory-context
      - memory.md#mem-obj-agent-skills
      - memory.md#mem-rte-skill-loading
      - memory.md#mem-rte-transcript-compaction
      - epistemic.md#epi-rte-summary-generation
      - epistemic.md#epi-rte-summary-retention
      - memory.md#mem-rte-reflection-integration
      - epistemic.md#epi-rte-reflection-guidance
      - memory.md#mem-obj-reflection-payload
      - runtime.md#rt-obj-local-transcript
      - memory.md#mem-obj-compaction-summary
      - runtime.md#rt-bap-provider-context
      - memory.md#mem-rte-transcript-search
      - memory.md#mem-obj-memory-constraints
      - memory.md#mem-rte-memory-admission
      - epistemic.md#epi-rte-commit-admission
      - memory.md#mem-bap-reflection-progress
      - memory.md#mem-obj-hosted-memory
      - memory.md#mem-rte-repository-sync
      - memory.md#mem-rte-arena-selection
      - epistemic.md#epi-obj-arena-choice
      note: Authority follows each retained part at its actual consumer. Local context, learning inputs,
        ranking inputs, policy vetoes and maintenance selectors have distinct warrants; opaque server
        and feedback consumers prevent completeness.
    write_agency:
      assessment: partial
      units:
      - scope: Compaction summary retention after model return
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-transcript-compaction
          - epistemic.md#epi-rte-summary-generation
          - epistemic.md#epi-rte-summary-retention
          note: Software admits model-produced summary text for later history consumption.
        records:
        - memory.md#mem-rte-transcript-compaction
        - epistemic.md#epi-rte-summary-generation
        - epistemic.md#epi-rte-summary-retention
        note: The backend trims/clips and persists returned text without a per-content human decision.
      - scope: Default reflection proposal integration and agent-mediated explicit integration
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-reflection-integration
          - epistemic.md#epi-rte-reflection-guidance
          - epistemic.md#epi-rte-reflection-merge
          note: Model/software admission can install trace-derived memory or skill text without human
            review of each edit.
        records:
        - memory.md#mem-rte-reflection-integration
        - epistemic.md#epi-rte-reflection-guidance
        - epistemic.md#epi-rte-reflection-merge
        note: Default clean proposals merge mechanically; explicit integration asks another agent not
          to wait for the user.
      - scope: Hook-covered model edit admission and successful-progress update
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-memory-constraints
          - memory.md#mem-rte-memory-admission
          - epistemic.md#epi-rte-commit-admission
          - memory.md#mem-obj-reflection-payload
          - memory.md#mem-bap-reflection-progress
          - memory.md#mem-rte-reflection-integration
          note: The hook decides conformance and the finalizer updates successful-progress state under
            program predicates.
        records:
        - memory.md#mem-obj-memory-constraints
        - memory.md#mem-rte-memory-admission
        - epistemic.md#epi-rte-commit-admission
        - memory.md#mem-obj-reflection-payload
        - memory.md#mem-bap-reflection-progress
        - memory.md#mem-rte-reflection-integration
        note: This unit names inspected software gates and completion-state updates, not all physical
          file writers.
      - scope: Offered human reflection-arena winner/tie selection
        assessment: known
        findings:
        - value: manual
          basis: afforded
          records:
          - memory.md#mem-rte-arena-selection
          - epistemic.md#epi-obj-arena-choice
          note: A human-facing choice can explicitly approve one candidate or veto both; repository checks
            can still reject the chosen proposal.
        records:
        - memory.md#mem-rte-arena-selection
        - epistemic.md#epi-obj-arena-choice
        note: The user-facing branch-selection interface affords explicit approval of selected content;
          actual chooser identity is not established.
      - scope: Generic arena choice caller and listener/create-body or backup-restore content control
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-arena-selection
        - epistemic.md#epi-obj-arena-choice
        - memory.md#mem-rte-memory-admission
        - epistemic.md#epi-rte-memory-restore
        note: Choice values, listener requests and restore force flags do not authenticate an explicit
          human per-content decision; generic caller identity leaves admission agency unresolved.
      - scope: Mutable constraint overrides, initial/dynamic skill admissions and generic-worker/repair
          finalization
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-memory-constraints
        - memory.md#mem-rte-memory-admission
        - epistemic.md#epi-rte-commit-admission
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-rte-skill-loading
        - memory.md#mem-rte-reflection-integration
        note: An environment authorization flag is not proof of human control; complete source routes
          for these alternatives are not recorded.
      - scope: Hosted and attached repository content admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hosted-memory
        - memory.md#mem-rte-repository-sync
        note: Service acceptance and content authorship/control are external or unresolved; sync software
          alone does not establish who admits each memory assertion.
      records:
      - memory.md#mem-rte-transcript-compaction
      - epistemic.md#epi-rte-summary-generation
      - epistemic.md#epi-rte-summary-retention
      - memory.md#mem-rte-reflection-integration
      - epistemic.md#epi-rte-reflection-guidance
      - epistemic.md#epi-rte-reflection-merge
      - memory.md#mem-obj-memory-constraints
      - memory.md#mem-rte-memory-admission
      - epistemic.md#epi-rte-commit-admission
      - memory.md#mem-obj-reflection-payload
      - memory.md#mem-bap-reflection-progress
      - memory.md#mem-rte-arena-selection
      - epistemic.md#epi-obj-arena-choice
      - epistemic.md#epi-rte-memory-restore
      - memory.md#mem-obj-agent-skills
      - memory.md#mem-rte-skill-loading
      - memory.md#mem-obj-hosted-memory
      - memory.md#mem-rte-repository-sync
      note: Automatic trace-fed and hook admission paths are established. Human-facing arena selection
        is an affordance, not evidence authenticating generic callers; initialization, restore and external
        controls remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Transcript-to-retained compaction summary
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-transcript-compaction
          - epistemic.md#epi-rte-summary-generation
          - epistemic.md#epi-rte-summary-retention
          - runtime.md#rt-obj-local-transcript
          - memory.md#mem-obj-compaction-summary
          note: Selected retained messages are compressed into a summary used in place of prior active
            history.
        records:
        - memory.md#mem-rte-transcript-compaction
        - epistemic.md#epi-rte-summary-generation
        - epistemic.md#epi-rte-summary-retention
        - runtime.md#rt-obj-local-transcript
        - memory.md#mem-obj-compaction-summary
        note: The implemented summarization/clip/summary-plus-tail route reduces the representation of
          existing conversational claims; no fidelity check is inferred.
      - scope: Requested reflection fact selection and stale-entry/duplicate handling
        assessment: known
        findings:
        - value: consolidate
          basis: claimed
          records:
          - memory.md#mem-rte-reflection-integration
          - epistemic.md#epi-rte-reflection-guidance
          note: Instructions request lasting facts and reusable procedures from retained session evidence,
            rather than raw logs.
        - value: evolve
          basis: claimed
          records:
          - memory.md#mem-rte-reflection-integration
          - epistemic.md#epi-rte-reflection-guidance
          note: Contradiction guidance asks the child to fix the stale entry at its source.
        - value: dedup
          basis: claimed
          records:
          - memory.md#mem-rte-reflection-integration
          - epistemic.md#epi-rte-reflection-guidance
          note: Guidance filters duplicated material and forbids appending the contradictory version beside
            the old one.
        records:
        - memory.md#mem-rte-reflection-integration
        - epistemic.md#epi-rte-reflection-guidance
        note: Known here classifies the requested operations at doctrine strength, not completed semantic
          transformations.
      - scope: Requested archival and semantic generalization effects
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-reflection-guidance
        - memory.md#mem-clm-archive-projection
        - memory.md#mem-rte-reflection-integration
        note: Root ARCHIVE.md remains core, so that placement alone cannot establish invalidate or decay.
          No actual output establishes synthesis of a new claim or effective withdrawal; generalization
          requests do not settle implemented semantic effects.
      - scope: Generic worker repairs, migration and hosted maintenance alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-reflection-integration
        - memory.md#mem-rte-memory-admission
        - memory.md#mem-obj-hosted-memory
        - memory.md#mem-rte-repository-sync
        note: Precise repair/migration transformations are uninspected and external server curation is
          opaque; transport, clean Git merge and cache invalidation alone establish no memory curation
          value.
      records:
      - memory.md#mem-rte-transcript-compaction
      - epistemic.md#epi-rte-summary-generation
      - epistemic.md#epi-rte-summary-retention
      - runtime.md#rt-obj-local-transcript
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-reflection-integration
      - epistemic.md#epi-rte-reflection-guidance
      - memory.md#mem-clm-archive-projection
      - memory.md#mem-rte-memory-admission
      - memory.md#mem-obj-hosted-memory
      - memory.md#mem-rte-repository-sync
      note: Compaction implements reduction of retained context. Reflection requests additional semantic
        operations, whose compliance is unobserved; opaque maintenance and repairs prevent a complete
        operation inventory.
    read_back_direction:
      assessment: partial
      units:
      - scope: Core bodies/directory pointers and active local history or summary to subsequent turn
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-core-memory
          - memory.md#mem-obj-deferred-memory
          - memory.md#mem-rte-core-projection
          - memory.md#mem-rte-deferred-read
          - runtime.md#rt-obj-local-transcript
          - memory.md#mem-obj-compaction-summary
          - memory.md#mem-rte-transcript-compaction
          - runtime.md#rt-rte-foreground-turn
          note: Compiler and history loader automatically deliver selected memory to a later model invocation.
        records:
        - memory.md#mem-obj-core-memory
        - memory.md#mem-obj-deferred-memory
        - memory.md#mem-rte-core-projection
        - memory.md#mem-rte-deferred-read
        - runtime.md#rt-obj-local-transcript
        - memory.md#mem-obj-compaction-summary
        - memory.md#mem-rte-transcript-compaction
        - runtime.md#rt-rte-foreground-turn
        note: A new turn automatically selects and supplies retained context without a request for those
          specific retained parts.
      - scope: Deferred Memory path, Skill name and transcript/conversation search requests
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-deferred-read
          - memory.md#mem-rte-skill-loading
          - memory.md#mem-rte-transcript-search
          note: Requested files, procedures and search results are returned to the requesting model or
            UI/CLI caller.
        records:
        - memory.md#mem-rte-deferred-read
        - memory.md#mem-rte-skill-loading
        - memory.md#mem-rte-transcript-search
        note: The consumer/caller requests retained content; queued skill text is fulfillment of that
          request.
      - scope: Available retained-skill metadata to later model discovery context
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-agent-skills
          - memory.md#mem-rte-skill-loading
          note: Discovery automatically advertises eligible retained skill metadata to the model.
        records:
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-rte-skill-loading
        note: Eligible names/descriptions are supplied before the model requests full bodies; procedure
          loading is a separate pull unit.
      - scope: Reflection evidence/current memory and successful-progress state at later maintenance invocation
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-obj-reflection-payload
          - memory.md#mem-bap-reflection-progress
          - memory.md#mem-rte-reflection-integration
          - epistemic.md#epi-rte-reflection-guidance
          note: Maintenance automatically selects evidence and consumes retained progress to construct
            the later update context.
        records:
        - memory.md#mem-obj-reflection-payload
        - memory.md#mem-bap-reflection-progress
        - memory.md#mem-rte-reflection-integration
        - epistemic.md#epi-rte-reflection-guidance
        note: Trigger and selector automatically supply transcript slices/checkpoints; upstream manual
          launch does not make later automatic selection a request for each item.
      - scope: Hosted non-skill projection, full replay and repair/arena feedback later-consumer alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hosted-memory
        - memory.md#mem-rte-repository-sync
        - memory.md#mem-rte-arena-selection
        - epistemic.md#epi-obj-arena-choice
        - runtime.md#rt-obj-local-transcript
        - memory.md#mem-rte-reflection-integration
        note: External delivery is opaque and complete replay/repair/feedback routes are uninspected;
          local pushes and pulls cannot close those alternatives.
      records:
      - memory.md#mem-obj-core-memory
      - memory.md#mem-obj-deferred-memory
      - memory.md#mem-rte-core-projection
      - memory.md#mem-rte-deferred-read
      - runtime.md#rt-obj-local-transcript
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-transcript-compaction
      - runtime.md#rt-rte-foreground-turn
      - memory.md#mem-rte-skill-loading
      - memory.md#mem-rte-transcript-search
      - memory.md#mem-obj-agent-skills
      - memory.md#mem-obj-reflection-payload
      - memory.md#mem-bap-reflection-progress
      - memory.md#mem-rte-reflection-integration
      - epistemic.md#epi-rte-reflection-guidance
      - memory.md#mem-obj-hosted-memory
      - memory.md#mem-rte-repository-sync
      - memory.md#mem-rte-arena-selection
      - epistemic.md#epi-obj-arena-choice
      note: 'Both automatic context supply and requested retrieval exist locally. Operations within a
        chain are separated: fulfilling a Memory/Skill/search request is pull, not an additional push
        because code transports its result. Hosted alternatives remain unresolved.'
    read_back_signal:
      assessment: partial
      units:
      - scope: Turn-triggered committed core/index projection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-rte-core-projection
          - memory.md#mem-obj-core-memory
          - memory.md#mem-obj-deferred-memory
          note: All layout-eligible core content is supplied, not semantic relevance selection for the
            current problem.
        records:
        - memory.md#mem-rte-core-projection
        - memory.md#mem-obj-core-memory
        - memory.md#mem-obj-deferred-memory
        note: Trigger is a local agent/conversation turn; selector inputs are MemFS enablement, committed
          HEAD and Markdown layout; delivered parts are root bodies and directory pointers.
      - scope: Agent/conversation identity selects retained history and active summary projection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - runtime.md#rt-rte-foreground-turn
          - runtime.md#rt-obj-local-transcript
          - memory.md#mem-rte-transcript-compaction
          note: The chosen agent/conversation matches the retained session whose history is delivered.
        records:
        - runtime.md#rt-rte-foreground-turn
        - runtime.md#rt-obj-local-transcript
        - memory.md#mem-rte-transcript-compaction
        note: Trigger is the next turn; agent/conversation identity selects its ordered retained history
          and compaction projection, rather than identifying a requested file only.
      - scope: Automatic eligible-skill metadata advertisement
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-agent-skills
          - memory.md#mem-rte-skill-loading
          note: Discovery advertises eligible names/descriptions without a recorded problem-relevance
            selector.
        records:
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-rte-skill-loading
        note: Trigger is skill discovery for turn context; source/attachment eligibility and model-invocable
          filtering select metadata, not full procedure text.
      - scope: Reflection progress-based transcript slice selection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-obj-reflection-payload
          - memory.md#mem-bap-reflection-progress
          - memory.md#mem-rte-reflection-integration
          note: A successful-progress message identity locates the boundary selecting later transcript
            messages.
        - value: coarse
          basis: wired
          records:
          - memory.md#mem-obj-reflection-payload
          - memory.md#mem-bap-reflection-progress
          - memory.md#mem-rte-reflection-integration
          note: Step/compaction triggers, replay-turn and character bounds constrain available evidence
            without semantic targeting.
        records:
        - memory.md#mem-obj-reflection-payload
        - memory.md#mem-bap-reflection-progress
        - memory.md#mem-rte-reflection-integration
        note: Trigger is reflection launch; reflected-through message ID and per-conversation state identify
          the next recorded slice, with replay boundaries/thresholds separately limiting coverage.
      - scope: Complete multi-conversation/reflection normalization and selection machinery
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-reflection-payload
        - memory.md#mem-bap-reflection-progress
        - memory.md#mem-rte-reflection-integration
        note: Automatic conversation selection is not fully inspected; supplied reasons/priorities do
          not establish a complete inferred-judgment selection algorithm.
      - scope: Hosted memory push selectors
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hosted-memory
        - memory.md#mem-rte-repository-sync
        note: Server-side selection and embedding mechanisms are opaque; visible metadata and hosted vector/hybrid
          API options do not classify actual push signals.
      records:
      - memory.md#mem-rte-core-projection
      - memory.md#mem-obj-core-memory
      - memory.md#mem-obj-deferred-memory
      - runtime.md#rt-rte-foreground-turn
      - runtime.md#rt-obj-local-transcript
      - memory.md#mem-rte-transcript-compaction
      - memory.md#mem-obj-agent-skills
      - memory.md#mem-rte-skill-loading
      - memory.md#mem-obj-reflection-payload
      - memory.md#mem-bap-reflection-progress
      - memory.md#mem-rte-reflection-integration
      - memory.md#mem-obj-hosted-memory
      - memory.md#mem-rte-repository-sync
      note: Signals classify automatic selection only. Requested file paths, skill names and search terms
        are not identifier/lexical push merely because they select pull results. Hosted selectors and
        complete maintenance selection remain unresolved.
    trace_learning:
      assessment: partial
      units:
      - scope: Automatic summary production, retention and later continuation
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-transcript-compaction
          - epistemic.md#epi-rte-summary-generation
          - epistemic.md#epi-rte-summary-retention
          - runtime.md#rt-obj-local-transcript
          - memory.md#mem-obj-compaction-summary
          note: Recorded conversation activity feeds automatic retained behavior-shaping summary production
            and later model consumption.
        records:
        - memory.md#mem-rte-transcript-compaction
        - epistemic.md#epi-rte-summary-generation
        - epistemic.md#epi-rte-summary-retention
        - runtime.md#rt-obj-local-transcript
        - memory.md#mem-obj-compaction-summary
        note: The summary persists as a compaction entry and is later consumed as model context; manual
          launch does not supply per-summary human admission.
      - scope: Automatic reflection proposal/integration to future memory or skill consumers
        assessment: known
        findings:
        - value: 'yes'
          basis: wired
          records:
          - memory.md#mem-rte-reflection-integration
          - epistemic.md#epi-rte-reflection-guidance
          - memory.md#mem-bap-memory-context
          - memory.md#mem-obj-agent-skills
          - memory.md#mem-rte-skill-loading
          note: Session evidence feeds automatic memory/skill updates with wired later consumers.
        records:
        - memory.md#mem-rte-reflection-integration
        - epistemic.md#epi-rte-reflection-guidance
        - memory.md#mem-bap-memory-context
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-rte-skill-loading
        note: The route can admit transcript-fed edits for core/deferred/skill use; no-change outcomes
          and unobserved semantic quality do not negate the wired write path.
      - scope: Initial/caller-authored content and dynamic skills
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-core-memory
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-rte-memory-admission
        note: Provenance and per-content control are unresolved; retaining imported/authored text alone
          establishes neither qualifying automatic trace-fed learning nor bounded absence.
      - scope: Generic-worker repairs, arena feedback consumers and migration alternatives
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-reflection-integration
        - memory.md#mem-rte-arena-selection
        - epistemic.md#epi-obj-arena-choice
        note: Worker update inputs and later feedback use are not fully traced; the recorded choice log
          is not proof of automatic learning.
      - scope: Hosted maintenance and provider-retained learning alternatives
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hosted-memory
        - memory.md#mem-rte-repository-sync
        note: External update internals and later consumers are not captured; a wired local yes cannot
          resolve external learning coverage.
      records:
      - memory.md#mem-rte-transcript-compaction
      - epistemic.md#epi-rte-summary-generation
      - epistemic.md#epi-rte-summary-retention
      - runtime.md#rt-obj-local-transcript
      - memory.md#mem-obj-compaction-summary
      - memory.md#mem-rte-reflection-integration
      - epistemic.md#epi-rte-reflection-guidance
      - memory.md#mem-bap-memory-context
      - memory.md#mem-obj-agent-skills
      - memory.md#mem-rte-skill-loading
      - memory.md#mem-obj-core-memory
      - memory.md#mem-rte-memory-admission
      - memory.md#mem-rte-arena-selection
      - epistemic.md#epi-obj-arena-choice
      - memory.md#mem-obj-hosted-memory
      - memory.md#mem-rte-repository-sync
      note: Compaction and reflection establish wired automatic trace-fed durable outputs with later context
        consumers. This is not observed improvement or parametric training. No bounded absence records
        support a system-wide or local no.
    trace_source:
      assessment: partial
      units:
      - scope: Original conversational input to automatic compaction
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-transcript-compaction
          - epistemic.md#epi-rte-summary-generation
          - epistemic.md#epi-rte-summary-retention
          - runtime.md#rt-obj-local-transcript
          note: Recorded conversational turns supply the summarization input.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-transcript-compaction
          - epistemic.md#epi-rte-summary-generation
          - epistemic.md#epi-rte-summary-retention
          - runtime.md#rt-obj-local-transcript
          note: Recorded tool requests/results within that transcript feed the retained summary.
        records:
        - memory.md#mem-rte-transcript-compaction
        - epistemic.md#epi-rte-summary-generation
        - epistemic.md#epi-rte-summary-retention
        - runtime.md#rt-obj-local-transcript
        note: Formatted conversation includes recorded turns and bounded tool returns; truncation limits
          completeness, not their source category.
      - scope: Original conversational input to transcript-fed reflection edits
        assessment: known
        findings:
        - value: session-logs
          basis: wired
          records:
          - memory.md#mem-rte-reflection-integration
          - epistemic.md#epi-rte-reflection-guidance
          - memory.md#mem-obj-reflection-payload
          note: Session slices, including user messages/corrections, supply reflection evidence.
        - value: tool-traces
          basis: wired
          records:
          - memory.md#mem-rte-reflection-integration
          - epistemic.md#epi-rte-reflection-guidance
          - memory.md#mem-obj-reflection-payload
          note: Tool arguments/results retained in the selected session payload supply update evidence.
        records:
        - memory.md#mem-rte-reflection-integration
        - epistemic.md#epi-rte-reflection-guidance
        - memory.md#mem-obj-reflection-payload
        note: The selected payload includes user, assistant and tool activity; normalization does not
          change the recorded original sources.
      - scope: Full reflection normalization, generic repair and arena-feedback update inputs
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-reflection-payload
        - memory.md#mem-bap-reflection-progress
        - memory.md#mem-rte-reflection-integration
        - epistemic.md#epi-rte-reflection-guidance
        - memory.md#mem-rte-arena-selection
        - epistemic.md#epi-obj-arena-choice
        note: Complete input selection and feedback-learning consumers are uninspected; no additional
          original trace category can be established.
      - scope: Initial/dynamic skill and hosted update inputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-agent-skills
        - memory.md#mem-obj-core-memory
        - memory.md#mem-obj-hosted-memory
        - memory.md#mem-rte-repository-sync
        note: Initial provenance and external qualifying writes remain unresolved; static imported instructions
          alone do not establish a trace source.
      records:
      - memory.md#mem-rte-transcript-compaction
      - epistemic.md#epi-rte-summary-generation
      - epistemic.md#epi-rte-summary-retention
      - runtime.md#rt-obj-local-transcript
      - memory.md#mem-rte-reflection-integration
      - epistemic.md#epi-rte-reflection-guidance
      - memory.md#mem-obj-reflection-payload
      - memory.md#mem-bap-reflection-progress
      - memory.md#mem-rte-arena-selection
      - epistemic.md#epi-obj-arena-choice
      - memory.md#mem-obj-agent-skills
      - memory.md#mem-obj-core-memory
      - memory.md#mem-obj-hosted-memory
      - memory.md#mem-rte-repository-sync
      note: Original session and tool activity feed the two qualifying local update routes. Session IDs,
        hook-trigger labels and journal serialization do not by themselves add event-streams or trajectories.
        Unknown alternatives remain included.
---

# Letta Code memory profile

## Comparison rationale

### Scope and coverage

The profile classifies retained memory rather than the entire runtime's storage or permissions. Local prose, symbolic access state and mutable policy remain separate operative parts. Attached local files do not disclose hosted payload encoding, provenance, maintenance or selection. Every axis is partial because positive local mechanisms coexist with unresolved included alternatives. “Known” units identify only their named scope and evidence layer; they do not upgrade another branch. The inventory and limits come from [MEM-OBJ-hosted-memory](memory.md#mem-obj-hosted-memory), [MEM-RTE-repository-sync](memory.md#mem-rte-repository-sync), [MEM-RTE-reflection-integration](memory.md#mem-rte-reflection-integration) and [MEM-RTE-memory-admission](memory.md#mem-rte-memory-admission).

The mod-learning builder retains evaluation reports and can copy executable successor code, but the accepted memory account explicitly treats executable mods and package replacement as separate runtime change routes. They are not silently used to assign memory promotion, validation, parametric storage or trace learning here. The retained inference components likewise do not establish accumulated parameter updates. See [EPI-RTE-mod-selection](epistemic.md#epi-rte-mod-selection), [RT-RTE-extension-load](runtime.md#rt-rte-extension-load), [RT-RTE-package-update](runtime.md#rt-rte-package-update) and [RT-CMP-turn-model](runtime.md#rt-cmp-turn-model).

### Non-obvious mappings

Files and repo coexist for Git-backed memory: files supply bodies while the repository supplies retained revision/access structure. Raw session envelopes, summary prose and first-kept/progress metadata are not one representation or consumer. Trace-fed inputs have learning authority at their update consumer; resulting summaries supply knowledge at a later model, while retained preferences/procedures can supply instruction. This establishes delivery force, not compliance, factual acceptance or improved capacity. See [RT-OBJ-local-transcript](runtime.md#rt-obj-local-transcript), [MEM-OBJ-compaction-summary](memory.md#mem-obj-compaction-summary), [MEM-BAP-memory-context](memory.md#mem-bap-memory-context) and [MEM-BAP-reflection-progress](memory.md#mem-bap-reflection-progress).

Compaction is wired consolidation and trace learning even though the summary's semantic fidelity is indeterminate. Its retained summary replaces active context and later reaches another invocation. This operational mapping neither claims synthesis nor resolves the epistemic assessment of the generated propositions. Reflection's automatic write/integration chain is wired; its requested contradiction resolution and duplicate filtering remain claimed curation findings. Root archival placement does not implement reduced reliance because root ARCHIVE.md remains automatically supplied. See [MEM-RTE-transcript-compaction](memory.md#mem-rte-transcript-compaction), [EPI-RTE-summary-generation](epistemic.md#epi-rte-summary-generation), [EPI-RTE-reflection-guidance](epistemic.md#epi-rte-reflection-guidance) and [MEM-CLM-archive-projection](memory.md#mem-clm-archive-projection).

The manual finding is only afforded on the offered human arena selection path. Generic choice callers, force flags and policy-authorization environment values do not authenticate per-content human approval. Compaction and default reflection admission remain automatic despite optional human initiation. See [MEM-RTE-arena-selection](memory.md#mem-rte-arena-selection), [MEM-RTE-memory-admission](memory.md#mem-rte-memory-admission), [EPI-RTE-memory-restore](epistemic.md#epi-rte-memory-restore) and [EPI-RTE-summary-retention](epistemic.md#epi-rte-summary-retention).

Read-back direction follows operations, not message role. Automatic core/history and skill advertisement are push; requested Memory/Skill/search returns are pull. A requested name/path does not make pull into identifier push. Identity matching is retained for the automatic conversation-history selection and progress-bounded reflection slice. Core layout and eligibility/budget filters remain coarse. Query-dependent local search is a ranking consumer of retained text, not inferred-lexical push. See [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn), [MEM-RTE-core-projection](memory.md#mem-rte-core-projection), [MEM-RTE-skill-loading](memory.md#mem-rte-skill-loading), [MEM-RTE-transcript-search](memory.md#mem-rte-transcript-search) and [MEM-BAP-reflection-progress](memory.md#mem-bap-reflection-progress).

Session logs and tool traces name the original content actually supplied to summary/reflection updates. A compaction trigger, user-role summary wrapper or manifest checkpoint is not a new event-stream source. No recorded linked state/action/outcome training path establishes trajectories. Those omissions are not bounded negatives. See [MEM-OBJ-reflection-payload](memory.md#mem-obj-reflection-payload) and [MEM-RTE-transcript-compaction](memory.md#mem-rte-transcript-compaction).

### Canonical records and remaining limits

Reconciliation supersedes the epistemic summary object with [MEM-OBJ-compaction-summary](memory.md#mem-obj-compaction-summary), projection with [MEM-RTE-core-projection](memory.md#mem-rte-core-projection), fetch with [MEM-RTE-deferred-read](memory.md#mem-rte-deferred-read), and arena choice route with [MEM-RTE-arena-selection](memory.md#mem-rte-arena-selection). Classifications cite those canonical records. These identity changes alter no controlled value and do not upgrade epistemic fidelity or actual chooser identity. The broader compaction/reflection chains coexist with their separate producer, retention, guidance and merge functions; those narrower records remain canonical.

Missing initial-content control prevents complete agency and lineage classifications. Uninspected replay/search-cache, normalization/multi-conversation selection, generic-worker repair, migration and feedback-consumer details prevent a complete transformation/consumer inventory. Opaque service state prevents external substrate, encoding, provenance and selection classifications. No evidenced-absence record supports a local trace-learning “no”; one known automatic route cannot make another unresolved route or its trace source inapplicable. See [MEM-OBJ-core-memory](memory.md#mem-obj-core-memory), [MEM-OBJ-agent-skills](memory.md#mem-obj-agent-skills), [MEM-RTE-reflection-integration](memory.md#mem-rte-reflection-integration), [MEM-RTE-transcript-search](memory.md#mem-rte-transcript-search) and [MEM-OBJ-hosted-memory](memory.md#mem-obj-hosted-memory).

### Source-read log

No source files were read. All classifications use the supplied accepted records and their retained passages; no evidence, quotes or analyst records were added. Source execution, report verification, publication and coordinator-owned state remain outside this assignment.
