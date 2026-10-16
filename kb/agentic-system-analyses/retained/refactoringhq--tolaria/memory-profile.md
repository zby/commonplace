---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Tolaria memory comparison: retained vault notes, mutable guidance, workspace transcripts
  and operational metadata, with unresolved application alternatives.'
run-id: AAS-2026-10-14-tolaria-42ddaf2ee8cd-01
source-identity: https://github.com/refactoringhq/tolaria
reviewed-boundary: 48f2a70844c1e8005a7aa5f1499c66f7678360de
memory-comparison:
  version: 2
  scope: 'Included: accumulated vault Markdown and mutable root/legacy guidance, workspace transcript
    files/cache/frontend state, retained workflow flags and vault registry entries, with their admission,
    maintenance and later consumers. Included but unresolved: desktop index/cache and watcher/Git reconciliation,
    editor admission, web/server collaborative checkpoints, remote persistence and remaining maintenance/evaluator
    paths. Excluded: shipped static prompts/docs as such, transient request/read/snippet products, external
    CLI checkpoints and extension internals, and provider/model parameters.'
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Vault Markdown bodies, frontmatter and mutable root/legacy guidance
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-vault-notes
          - runtime.md#rt-rte-guidance-sync
          note: Vault filesystem retains notes and guidance.
        records:
        - memory.md#mem-obj-vault-notes
        - runtime.md#rt-rte-guidance-sync
        - memory.md#mem-rte-mcp-read
        note: Inspected retained files; transient parsed reads and request strings are not separate retained
          substrates.
      - scope: Workspace transcript native file
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-workspace-sessions
          - memory.md#mem-rte-transcript-replay
          note: Native app configuration file retains the session map.
        records:
        - memory.md#mem-obj-workspace-sessions
        - memory.md#mem-rte-transcript-replay
        note: JSON encoding does not imply an RDBMS substrate.
      - scope: Workspace localStorage cache
        assessment: known
        findings:
        - value: kv
          basis: wired
          records:
          - memory.md#mem-obj-workspace-sessions
          note: Session map is cached under a localStorage key.
        records:
        - memory.md#mem-obj-workspace-sessions
        - memory.md#mem-rte-transcript-replay
        note: Browser key-addressed retained cache is distinct from the native JSON file.
      - scope: Workspace frontend session map
        assessment: known
        findings:
        - value: in-memory
          basis: wired
          records:
          - memory.md#mem-obj-workspace-sessions
          - memory.md#mem-rte-transcript-replay
          note: Frontend retains the session map across sends.
        records:
        - memory.md#mem-obj-workspace-sessions
        - memory.md#mem-rte-transcript-replay
        note: In-process retained state feeds later sends.
      - scope: Organized workflow state and requested persistence
        assessment: partial
        findings:
        - value: in-memory
          basis: wired
          records:
          - epistemic.md#epi-obj-organized-flag
          - epistemic.md#epi-rte-organized-toggle
          note: Entry state holds the flag consumed by the workflow.
        records:
        - epistemic.md#epi-obj-organized-flag
        - epistemic.md#epi-rte-organized-toggle
        note: Frontend boolean state is inspected; lower persistence/reload dependencies remain uninspected.
      - scope: Vault registry persisted entries
        assessment: not-determinable
        findings: []
        records:
        - epistemic.md#epi-rte-vault-register
        note: Registry persistence is recorded, but its substrate is not classified by the accepted record.
      - scope: Included desktop index/cache, watcher/Git reconciliation, editor admission, and web/server
          collaborative and remote memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-rte-transcript-replay
        note: The accepted memory inventory leaves these paths untraced. Their storage facts and alternative
          operative parts are missing; inspected desktop witnesses cannot classify them.
      records:
      - memory.md#mem-obj-vault-notes
      - runtime.md#rt-rte-guidance-sync
      - memory.md#mem-rte-mcp-read
      - memory.md#mem-obj-workspace-sessions
      - memory.md#mem-rte-transcript-replay
      - epistemic.md#epi-obj-organized-flag
      - epistemic.md#epi-rte-organized-toggle
      - epistemic.md#epi-rte-vault-register
      note: Positive file, key-value and in-memory witnesses coexist with unresolved registry storage
        and included application alternatives. External model weights and external CLI checkpoints are
        outside Tolaria memory; transient tool results and shipped static prompts are excluded.
    representational_form:
      assessment: partial
      units:
      - scope: Note body/title and retained user/assistant history at model or human interpretation
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-vault-notes
          - memory.md#mem-obj-workspace-sessions
          - memory.md#mem-bap-retained-context
          note: Text supplies conversational evidence or note context.
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-obj-workspace-sessions
        - memory.md#mem-bap-retained-context
        note: Natural-language retained content is distinct from its serialized envelope.
      - scope: Mutable AGENTS guidance at later instruction consumer
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - runtime.md#rt-rte-guidance-sync
          - memory.md#mem-rte-mcp-read
          - memory.md#mem-bap-retained-context
          note: Retained directions reach the MCP caller or are available for later agent reading.
        records:
        - runtime.md#rt-rte-guidance-sync
        - memory.md#mem-rte-mcp-read
        - memory.md#mem-bap-retained-context
        note: Guidance conventions and reasons are interpreted text; compliance is not observed.
      - scope: Session status/IDs/actions, note frontmatter and organized-state fields
        assessment: partial
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-workspace-sessions
          - epistemic.md#epi-obj-organized-flag
          - epistemic.md#epi-rte-organized-toggle
          note: Flags and IDs drive normalization, filtering and workflow state.
        records:
        - memory.md#mem-obj-workspace-sessions
        - memory.md#mem-obj-vault-notes
        - epistemic.md#epi-obj-organized-flag
        - epistemic.md#epi-rte-organized-toggle
        note: Symbolic encoding and some fixed-rule consumers are recorded; complete frontend type/view
          semantics are unresolved.
      - scope: Persisted registry path entries at later service scope selection
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - epistemic.md#epi-rte-vault-register
          note: Registry/session root paths define subsequent tool scope.
        records:
        - epistemic.md#epi-rte-vault-register
        note: Path-list consumption is deterministic.
      - scope: Included desktop index/cache, watcher/Git reconciliation, editor admission, and web/server
          collaborative and remote memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-rte-transcript-replay
        note: The accepted memory inventory leaves these paths untraced. Their representational form facts
          and alternative operative parts are missing; inspected desktop witnesses cannot classify them.
      records:
      - memory.md#mem-obj-vault-notes
      - memory.md#mem-obj-workspace-sessions
      - memory.md#mem-bap-retained-context
      - runtime.md#rt-rte-guidance-sync
      - memory.md#mem-rte-mcp-read
      - epistemic.md#epi-obj-organized-flag
      - epistemic.md#epi-rte-organized-toggle
      - epistemic.md#epi-rte-vault-register
      - memory.md#mem-rte-transcript-replay
      note: Text and symbolic parts are split by consumer. No retained numerical learning state is established
        inside the scoped memory; excluded inference models do not add parametric memory findings.
    lineage:
      assessment: partial
      units:
      - scope: Foreground conversation content
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - memory.md#mem-obj-workspace-sessions
          - memory.md#mem-rte-transcript-replay
          note: Foreground participants produce retained text.
        records:
        - memory.md#mem-obj-workspace-sessions
        - memory.md#mem-rte-transcript-replay
        note: User prompts and model responses are supplied directly by the foreground participants; replay
          is not extraction of lessons.
      - scope: Native transcript normalization and prefix cloning
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-workspace-sessions
          - memory.md#mem-rte-transcript-replay
          note: Code produces normalized flags and cloned prefixes from existing session state.
        records:
        - memory.md#mem-obj-workspace-sessions
        - memory.md#mem-rte-transcript-replay
        note: Code reshapes retained session records rather than importing another source.
      - scope: Provider-created note content
        assessment: partial
        findings:
        - value: authored
          basis: wired
          records:
          - runtime.md#rt-rte-provider-create
          - memory.md#mem-obj-vault-notes
          note: Provider proposes new note text for local retention.
        records:
        - memory.md#mem-obj-vault-notes
        - runtime.md#rt-rte-provider-create
        note: Model-produced content has an inspected admission path; its upstream factual provenance
          is not authenticated.
      - scope: Managed template guidance admitted to mutable vault files
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - runtime.md#rt-rte-guidance-sync
          - memory.md#mem-obj-vault-notes
          note: Managed defaults are copied into vault guidance.
        records:
        - runtime.md#rt-rte-guidance-sync
        - memory.md#mem-obj-vault-notes
        note: Shipped static assembly is excluded, but its copied retained guidance instance has an acquisition
          path.
      - scope: Cloned vault files
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - epistemic.md#epi-rte-vault-register
          note: Git clone imports a tree for later vault consumption.
        records:
        - epistemic.md#epi-rte-vault-register
        - memory.md#mem-obj-vault-notes
        note: Imported tree path is wired; the remote contents and their original authorship are not supplied.
      - scope: Existing notes, custom guidance and generic MCP-proposed content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - runtime.md#rt-rte-mcp-write
        note: Records name possible human, agent, imported and seeded origins without authenticating which
          path produced existing contents.
      - scope: Included desktop index/cache, watcher/Git reconciliation, editor admission, and web/server
          collaborative and remote memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-rte-transcript-replay
        note: The accepted memory inventory leaves these paths untraced. Their lineage facts and alternative
          operative parts are missing; inspected desktop witnesses cannot classify them.
      records:
      - memory.md#mem-obj-workspace-sessions
      - memory.md#mem-rte-transcript-replay
      - memory.md#mem-obj-vault-notes
      - runtime.md#rt-rte-provider-create
      - runtime.md#rt-rte-guidance-sync
      - epistemic.md#epi-rte-vault-register
      - runtime.md#rt-rte-mcp-write
      note: Known derivation paths do not certify initial content provenance. No trace-extracted lineage
        is established by raw logging or generic append capability.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Retained note bodies and user/assistant history at later model context consumers
        assessment: known
        findings:
        - value: knowledge
          basis: wired
          records:
          - memory.md#mem-bap-retained-context
          - memory.md#mem-rte-reference-context
          - memory.md#mem-rte-mcp-read
          - runtime.md#rt-rte-workspace-send
          note: Later agents/providers or MCP callers receive retained content as context.
        records:
        - memory.md#mem-bap-retained-context
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-obj-workspace-sessions
        - memory.md#mem-rte-reference-context
        - memory.md#mem-rte-mcp-read
        - runtime.md#rt-rte-workspace-send
        note: Delivered evidence/context has interpretive force, not proven correctness or observed reliance.
      - scope: Mutable root and legacy AGENTS guidance at MCP/agent instruction consumers
        assessment: known
        findings:
        - value: instruction
          basis: wired
          records:
          - runtime.md#rt-rte-guidance-sync
          - memory.md#mem-rte-mcp-read
          - memory.md#mem-bap-retained-context
          note: Guidance supplies standing directions to later consumers.
        records:
        - runtime.md#rt-rte-guidance-sync
        - memory.md#mem-rte-mcp-read
        - memory.md#mem-bap-retained-context
        note: Instruction-bearing retained files are separate from the shipped static prompt.
      - scope: Session IDs, status and streaming flags at history/recovery consumers
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-obj-workspace-sessions
          - memory.md#mem-rte-transcript-replay
          note: Session identity selects retained messages for reconstruction.
        - value: enforcement
          basis: wired
          records:
          - memory.md#mem-obj-workspace-sessions
          - runtime.md#rt-rte-workspace-send
          note: Streaming/local-marker predicates prevent excluded material entering history.
        records:
        - memory.md#mem-obj-workspace-sessions
        - memory.md#mem-rte-transcript-replay
        - runtime.md#rt-rte-workspace-send
        note: These fixed-rule controls select a session and exclude ineligible material.
      - scope: Note mtime at optional replacement check
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - epistemic.md#epi-rte-mtime-check
          note: Retained file mtime is compared to the caller expectation.
        - value: enforcement
          basis: wired
          records:
          - epistemic.md#epi-rte-mtime-check
          note: Mismatch blocks the replacement when the token is supplied.
        records:
        - epistemic.md#epi-rte-mtime-check
        - runtime.md#rt-rte-mcp-write
        note: Sampled equality supplies an admission criterion and a veto, not a semantic verdict.
      - scope: Note mtimes at recent-note orientation selector
        assessment: known
        findings:
        - value: ranking
          basis: wired
          records:
          - memory.md#mem-rte-mcp-read
          note: Retained mtimes order which recent-note metadata is returned.
        records:
        - memory.md#mem-rte-mcp-read
        note: Relative priority is fixed-code recency, not semantic quality.
      - scope: Vault registry/root state at later tool-scope consumer
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - epistemic.md#epi-rte-vault-register
          note: Root entries select operation scope.
        - value: enforcement
          basis: wired
          records:
          - epistemic.md#epi-rte-vault-register
          note: Admitted roots bound the inspected service access envelope.
        records:
        - epistemic.md#epi-rte-vault-register
        note: Retained root entries widen later read/write scope.
      - scope: Organized flag at UI inbox workflow consumer
        assessment: partial
        findings:
        - value: routing
          basis: wired
          records:
          - epistemic.md#epi-rte-organized-toggle
          note: Flag and focus conditions control inbox advancement.
        records:
        - epistemic.md#epi-obj-organized-flag
        - epistemic.md#epi-rte-organized-toggle
        note: State transition and next-note selection are inspected; complete persistent reload is not.
      - scope: Other frontmatter/type/view and retained action/reasoning consumers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-obj-workspace-sessions
        note: Complete type/view semantics and later consumption of stored reasoning/actions are not established.
      - scope: Included desktop index/cache, watcher/Git reconciliation, editor admission, and web/server
          collaborative and remote memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-rte-transcript-replay
        note: The accepted memory inventory leaves these paths untraced. Their authority facts and alternative
          operative parts are missing; inspected desktop witnesses cannot classify them.
      records:
      - memory.md#mem-bap-retained-context
      - memory.md#mem-obj-vault-notes
      - memory.md#mem-obj-workspace-sessions
      - memory.md#mem-rte-reference-context
      - memory.md#mem-rte-mcp-read
      - runtime.md#rt-rte-workspace-send
      - runtime.md#rt-rte-guidance-sync
      - memory.md#mem-rte-transcript-replay
      - epistemic.md#epi-rte-mtime-check
      - runtime.md#rt-rte-mcp-write
      - epistemic.md#epi-rte-vault-register
      - epistemic.md#epi-obj-organized-flag
      - epistemic.md#epi-rte-organized-toggle
      note: Knowledge, instruction, routing, enforcement, validation and ranking are local consumer effects.
        No learning authority follows merely from storing traces; external model behavior and semantic
        approval are not inferred.
    write_agency:
      assessment: partial
      units:
      - scope: MCP create/update/append admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-mcp-write
          note: Root/path and operation checks decide admission.
        records:
        - runtime.md#rt-rte-mcp-write
        note: Local software admits caller-proposed changes without per-content human approval.
      - scope: Direct-provider create-note admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-provider-create
          note: Parsed supported tool calls reach local execution without a per-content confirmation branch.
        records:
        - runtime.md#rt-rte-provider-create
        note: Starting the chat does not approve each returned note.
      - scope: Managed guidance refresh admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-guidance-sync
          note: Seed/restore code admits recognized template replacements.
        records:
        - runtime.md#rt-rte-guidance-sync
        note: Content predicate preserves custom guidance but software selects replacement.
      - scope: Transcript save/load normalization and prefix clone
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-transcript-replay
          note: Code publishes and serializes session updates without transcript review.
        records:
        - memory.md#mem-rte-transcript-replay
        - memory.md#mem-obj-workspace-sessions
        note: UI initiation is separate from subsequent transcript admission.
      - scope: Vault attach/clone registry and content admission
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - epistemic.md#epi-rte-vault-register
          note: Checks and registry update decide admission without per-content human approval.
        records:
        - epistemic.md#epi-rte-vault-register
        note: Caller proposes root or URL; local code admits registry/tree changes.
      - scope: Organized flag supplied by operator toggle
        assessment: known
        findings:
        - value: manual
          basis: wired
          records:
          - epistemic.md#epi-rte-organized-toggle
          note: User mark/unmark action supplies the content decision.
        records:
        - epistemic.md#epi-rte-organized-toggle
        note: The user explicitly decides the retained boolean value; automatic persistence is physical
          I/O, not admission agency.
      - scope: Native note save/delete and initial existing note/custom-guidance admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-note-withdrawal
        - memory.md#mem-obj-vault-notes
        note: Generic callers and untraced editor confirmation do not establish explicit human content
          control.
      - scope: Included desktop index/cache, watcher/Git reconciliation, editor admission, and web/server
          collaborative and remote memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-rte-transcript-replay
        note: The accepted memory inventory leaves these paths untraced. Their write agency facts and
          alternative operative parts are missing; inspected desktop witnesses cannot classify them.
      records:
      - runtime.md#rt-rte-mcp-write
      - runtime.md#rt-rte-provider-create
      - runtime.md#rt-rte-guidance-sync
      - memory.md#mem-rte-transcript-replay
      - memory.md#mem-obj-workspace-sessions
      - epistemic.md#epi-rte-vault-register
      - epistemic.md#epi-rte-organized-toggle
      - memory.md#mem-rte-note-withdrawal
      - memory.md#mem-obj-vault-notes
      note: Automatic admissions coexist with the explicit manual workflow-flag decision. Human authorship
        or workflow initiation alone does not classify other admissions as manual.
    curation_operations:
      assessment: partial
      units:
      - scope: MCP full replacement and append of an existing note
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-mcp-write
          note: Replacement revises an entry; append extends it.
        records:
        - runtime.md#rt-rte-mcp-write
        - memory.md#mem-obj-vault-notes
        note: Implemented revision of an existing entry is local evolution; no claim-quality gate is implied.
      - scope: Managed retained guidance replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - runtime.md#rt-rte-guidance-sync
          note: Recognized guidance is replaced with current defaults.
        records:
        - runtime.md#rt-rte-guidance-sync
        note: Software refresh revises retained instruction content.
      - scope: Transcript reset, regenerate and prefix replacement
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-transcript-replay
          - runtime.md#rt-rte-workspace-send
          note: Reset and suffix removal forget selected retained turns.
        records:
        - memory.md#mem-rte-transcript-replay
        - runtime.md#rt-rte-workspace-send
        note: These alter the retained conversation, unlike prompt-only suffix eviction.
      - scope: Native permanent note removal
        assessment: known
        findings:
        - value: decay
          basis: wired
          records:
          - memory.md#mem-rte-note-withdrawal
          note: Permanent removal makes the note unavailable at its former path.
        records:
        - memory.md#mem-rte-note-withdrawal
        note: Forgetting a file is not invalidation with history retained; copied contexts are not revoked.
      - scope: Organized workflow flag revision
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - epistemic.md#epi-rte-organized-toggle
          note: Mark/unmark changes an existing workflow property.
        records:
        - epistemic.md#epi-rte-organized-toggle
        note: Operator revises a retained entry property; no salience promotion or semantic endorsement
          is established.
      - scope: Trace-to-note or other maintenance transformations
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-rte-transcript-replay
        - runtime.md#rt-rte-mcp-write
        note: Generic writes and raw logging establish no specific trace-fed consolidation, synthesis
          or dedup route.
      - scope: Included desktop index/cache, watcher/Git reconciliation, editor admission, and web/server
          collaborative and remote memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-rte-transcript-replay
        note: The accepted memory inventory leaves these paths untraced. Their curation facts and alternative
          operative parts are missing; inspected desktop witnesses cannot classify them.
      records:
      - runtime.md#rt-rte-mcp-write
      - memory.md#mem-obj-vault-notes
      - runtime.md#rt-rte-guidance-sync
      - memory.md#mem-rte-transcript-replay
      - runtime.md#rt-rte-workspace-send
      - memory.md#mem-rte-note-withdrawal
      - epistemic.md#epi-rte-organized-toggle
      note: Evolution and forgetting have inspected retained-state effects. Current-request truncation,
        search excerpts, acquisition and exclusive-create collision checks are not retained consolidation
        or deduplication.
    read_back_direction:
      assessment: partial
      units:
      - scope: Automatic transcript selection on later send
        assessment: known
        findings:
        - value: push
          basis: wired
          records:
          - memory.md#mem-rte-transcript-replay
          - runtime.md#rt-rte-workspace-send
          note: Later send triggers session selection, filtering and suffix delivery to the model.
        records:
        - memory.md#mem-rte-transcript-replay
        - runtime.md#rt-rte-workspace-send
        note: User requests a new answer, not the history payload; code independently supplies retained
          history.
      - scope: Explicit note-reference request and hydration
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-reference-context
          note: Consumer/operator names references for the current request.
        records:
        - memory.md#mem-rte-reference-context
        note: Requested note selection and its deterministic delivery are one pull chain, not an extra
          push.
      - scope: MCP requested get/search/context, including recent metadata and AGENTS
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-mcp-read
          note: Caller asks for retained material through read/search/context tools.
        records:
        - memory.md#mem-rte-mcp-read
        - epistemic.md#epi-rte-vault-register
        note: Requested context remains pull even when code sorts recent files.
      - scope: Active-note snapshot and complete panel dispatch
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-rte-reference-context
        - memory.md#mem-obj-vault-notes
        note: Builder inspection is described in the memory account but complete dispatch and automatic
          consumption are not established by a canonical route record.
      - scope: Included desktop index/cache, watcher/Git reconciliation, editor admission, and web/server
          collaborative and remote memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-rte-transcript-replay
        note: The accepted memory inventory leaves these paths untraced. Their read-back facts and alternative
          operative parts are missing; inspected desktop witnesses cannot classify them.
      records:
      - memory.md#mem-rte-transcript-replay
      - runtime.md#rt-rte-workspace-send
      - memory.md#mem-rte-reference-context
      - memory.md#mem-rte-mcp-read
      - epistemic.md#epi-rte-vault-register
      - memory.md#mem-obj-vault-notes
      note: Transcript push and requested note/MCP pull coexist. Static prompt delivery, immediate tool
        returns and registry scope use alone are not additional memory-content read-back routes.
    read_back_signal:
      assessment: partial
      units:
      - scope: Transcript push session selection
        assessment: known
        findings:
        - value: identifier
          basis: wired
          records:
          - memory.md#mem-rte-transcript-replay
          - memory.md#mem-obj-workspace-sessions
          note: Session-ID match selects retained messages supplied to the later history builder.
        records:
        - memory.md#mem-rte-transcript-replay
        - memory.md#mem-obj-workspace-sessions
        - runtime.md#rt-rte-workspace-send
        note: 'Trigger: later send. Input: current session identity. Selected retained part: that session
          message array.'
      - scope: Transcript push eligibility and budget selection
        assessment: known
        findings:
        - value: coarse
          basis: wired
          records:
          - runtime.md#rt-rte-workspace-send
          - memory.md#mem-rte-transcript-replay
          note: Availability and budget filters select eligible retained text without semantic matching.
        records:
        - runtime.md#rt-rte-workspace-send
        - memory.md#mem-rte-transcript-replay
        note: 'Trigger: later send. Inputs: completed/nonmarker flags, recency and estimated character
          budget. Selected part: newest fitting user/response suffix.'
      - scope: Explicit references and MCP requested note material
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-reference-context
        - memory.md#mem-rte-mcp-read
        note: These completely assessed requested operations are pull; push-selection signal does not
          classify their path/query/mtime selectors.
      - scope: Included desktop index/cache, watcher/Git reconciliation, editor admission, and web/server
          collaborative and remote memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-rte-transcript-replay
        note: The accepted memory inventory leaves these paths untraced. Their push-selection signal facts
          and alternative operative parts are missing; inspected desktop witnesses cannot classify them.
      records:
      - memory.md#mem-rte-transcript-replay
      - memory.md#mem-obj-workspace-sessions
      - runtime.md#rt-rte-workspace-send
      - memory.md#mem-rte-reference-context
      - memory.md#mem-rte-mcp-read
      - memory.md#mem-obj-vault-notes
      note: Identifier matching and coarse filtering are separate operations on the transcript push. Requested
        filenames, search terms and context recency do not become push signals. Untraced alternatives
        prevent complete signal coverage.
    trace_learning:
      assessment: not-determinable
      units:
      - scope: Raw transcript retention/replay and context trimming
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-workspace-sessions
        - memory.md#mem-rte-transcript-replay
        - runtime.md#rt-rte-workspace-send
        note: The inspected chain retains raw turns, normalizes flags and evicts prompt text, not a recorded
          durable trace-derived summary. No bounded absence record supplies a controlled no finding.
      - scope: Generic note writes and managed guidance refresh
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - runtime.md#rt-rte-mcp-write
        - runtime.md#rt-rte-provider-create
        - runtime.md#rt-rte-guidance-sync
        note: Writes can carry arbitrary experience, but records establish no automatic trace-fed derivation
          into behavior-shaping artifacts. Template refresh is code-selected defaults, not trace learning.
      - scope: Included desktop index/cache, watcher/Git reconciliation, editor admission, and web/server
          collaborative and remote memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-rte-transcript-replay
        note: The accepted memory inventory leaves these paths untraced. Their qualifying automatic trace-fed
          writes facts and alternative operative parts are missing; inspected desktop witnesses cannot
          classify them.
      records:
      - memory.md#mem-obj-workspace-sessions
      - memory.md#mem-rte-transcript-replay
      - runtime.md#rt-rte-workspace-send
      - memory.md#mem-obj-vault-notes
      - runtime.md#rt-rte-mcp-write
      - runtime.md#rt-rte-provider-create
      - runtime.md#rt-rte-guidance-sync
      note: No controlled yes or no is established by accepted records. Raw logging/replay is insufficient
        for yes; untraced maintenance and collaborative checkpoint alternatives prevent a system-wide
        no.
    trace_source:
      assessment: not-determinable
      units:
      - scope: Inspected raw transcript and generic note-write paths
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-workspace-sessions
        - memory.md#mem-rte-transcript-replay
        - runtime.md#rt-rte-mcp-write
        - runtime.md#rt-rte-provider-create
        - runtime.md#rt-rte-guidance-sync
        note: Session/tool/event fields exist in logs, but no qualifying trace-learning write is established;
          logging inputs cannot be projected into learning-source positives.
      - scope: Included desktop index/cache, watcher/Git reconciliation, editor admission, and web/server
          collaborative and remote memory paths
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-vault-notes
        - memory.md#mem-rte-transcript-replay
        note: The accepted memory inventory leaves these paths untraced. Their original inputs to qualifying
          trace-fed writes facts and alternative operative parts are missing; inspected desktop witnesses
          cannot classify them.
      records:
      - memory.md#mem-obj-workspace-sessions
      - memory.md#mem-rte-transcript-replay
      - runtime.md#rt-rte-mcp-write
      - runtime.md#rt-rte-provider-create
      - runtime.md#rt-rte-guidance-sync
      - memory.md#mem-obj-vault-notes
      note: No qualifying route supports a positive learning-source value. The partial learning assessment
        cannot make this axis inapplicable; unresolved maintenance and collaboration could have other
        inputs.
---

# Tolaria memory profile

## Comparison rationale

This is a classification of accepted implementation records, not observed operation or demonstrated benefit. Partial coverage remains local to each axis. The same unresolved application inventory is retained throughout: a desktop witness cannot resolve collaborative checkpoints, editor admission, cache reconciliation or other maintenance routes. External models and external CLI memory are excluded from the memory boundary, not classified as Tolaria memory.

The reconciliation supersedes EPI-OBJ-note-content with [MEM-OBJ-vault-notes](memory.md#mem-obj-vault-notes). All note-object classifications use that canonical record. Parsed reads and snippets are transient delivery products, not extra storage substrates. The transcript and reference parts remain valid parts of [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send); neither supersedes the invocation container.

A later send requests an answer. Its automatic history builder independently supplies retained turns, so that operation is push. Session identity selects the message array; completed-message and budget checks then select its suffix. In contrast, explicit references and MCP context requests are pull, including their deterministic hydration and recent-file selection. Recency affects relative priority at the orientation consumer and therefore has ranking authority, but it is not a push signal. See [MEM-RTE-transcript-replay](memory.md#mem-rte-transcript-replay), [MEM-RTE-reference-context](memory.md#mem-rte-reference-context) and [MEM-RTE-mcp-read](memory.md#mem-rte-mcp-read).

Current-request omission does not produce a retained summary. Reset/regenerate can forget retained turns, and permanent note deletion forgets a file without retaining withdrawal history. Generic replacement/append revises an existing entry but does not establish semantic synthesis, consolidation or improved knowledge. These mappings concern implemented transformations, not command names: [RT-RTE-mcp-write](runtime.md#rt-rte-mcp-write), [MEM-RTE-note-withdrawal](memory.md#mem-rte-note-withdrawal) and [RT-RTE-workspace-send](runtime.md#rt-rte-workspace-send).

Local software decides MCP, provider and managed-guidance admission. The operator's explicit organized-flag toggle is a different manual content decision; its persistence callback does not change that agency. Unknown editor and initial-note admissions remain unresolved. The organized consumer supplies workflow routing, not acceptance of note truth. See [EPI-RTE-organized-toggle](epistemic.md#epi-rte-organized-toggle).

Raw retained sessions contain conversational and tool/event material, but no accepted record establishes a qualifying automatic trace-fed update to durable behavior-shaping material. Nor is there a bounded absence record warranting a controlled trace-learning no. The trace axes therefore retain no positive findings and remain not-determinable rather than converting untraced alternatives into absence or inapplicability. This does not classify external CLI compaction or learning. See [MEM-OBJ-workspace-sessions](memory.md#mem-obj-workspace-sessions) and [MEM-RTE-transcript-replay](memory.md#mem-rte-transcript-replay).

Source-read log: none. This member uses only the supplied accepted records and reconciliation; no frozen source files or incumbent profiles were read.
