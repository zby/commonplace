---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: MemWiki comparison profile of mutable project wiki, raw originals and their agent-mediated
  maintenance/read-back routes.
run-id: AAS-2026-10-14-memwiki-79dcc4d04bcb-01
source-identity: https://github.com/hereisSwapnil/memwiki
reviewed-boundary: 8034a3da991ac2639b87875172a9572903ecf1d5
memory-comparison:
  version: 2
  scope: Includes mutable hot/index/domain/decision/log wiki files accumulated or changed through use;
    human-supplied raw originals, including unresolved payloads; current and legacy starter admission;
    foreground-agent work/raw/repository writes; lint proposal-to-edit uncertainty; fold; and later session/source/maintenance
    readers. Excludes static shipped protocol/hooks as memory content, external host parameters/context/compaction,
    npm/dependency internals and untracked pages merely claimed in the log. Static instructions establish
    the included routes but are not themselves accumulated memory.
  axes:
    storage_substrate:
      assessment: known
      units:
      - scope: Mutable hot cache, index, stack/patterns/bugs, decisions and work log in the project wiki
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-rte-cli-init
          - runtime.md#rt-rte-legacy-init
          note: Both inspected scaffold paths write starter wiki files; subsequent project-memory retention
            uses those destinations.
        - value: files
          basis: afforded
          records:
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-index
          - memory.md#mem-obj-domain-pages
          - memory.md#mem-obj-decisions
          - memory.md#mem-obj-log
          note: The accepted object inventory identifies all seven retained Markdown pages on the project
            filesystem.
        records:
        - runtime.md#rt-rte-cli-init
        - runtime.md#rt-rte-legacy-init
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-index
        - memory.md#mem-obj-domain-pages
        - memory.md#mem-obj-decisions
        - memory.md#mem-obj-log
        note: The complete wiki inventory shares filesystem retention; neither Markdown encoding nor links
          establish a database or graph substrate.
      - scope: Human-supplied raw originals and their directory
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-rte-cli-init
          - memory.md#mem-obj-raw
          note: The CLI creates the filesystem directory for original documents.
        - value: files
          basis: claimed
          records:
          - memory.md#mem-obj-raw
          - runtime.md#rt-rte-agent-session
          note: The protocol describes human-deposited source files retained unchanged for agent reading.
        records:
        - runtime.md#rt-rte-cli-init
        - memory.md#mem-obj-raw
        - runtime.md#rt-rte-agent-session
        note: Payload encoding and initial deployed content are unresolved, but their declared retention
          substrate is files.
      records:
      - runtime.md#rt-rte-cli-init
      - runtime.md#rt-rte-legacy-init
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-index
      - memory.md#mem-obj-domain-pages
      - memory.md#mem-obj-decisions
      - memory.md#mem-obj-log
      - memory.md#mem-obj-raw
      - runtime.md#rt-rte-agent-session
      note: All included retained parts are project files. External host context/parameters and static
        hook/protocol installations are excluded, not alternative internal memory stores.
    representational_form:
      assessment: partial
      units:
      - scope: 'Wiki prose: hot state/checklists, directory labels/links, domain conventions/rationale
          and historical summaries at model consumers'
        assessment: known
        findings:
        - value: natural-language
          basis: afforded
          records:
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-index
          - memory.md#mem-obj-domain-pages
          - memory.md#mem-obj-decisions
          - memory.md#mem-obj-log
          note: The retained parts are interpreted prose and notation; the index has no fixed-rule link
            resolver and checklists are not enforced symbolic controls.
        records:
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-index
        - memory.md#mem-obj-domain-pages
        - memory.md#mem-obj-decisions
        - memory.md#mem-obj-log
        note: Code names, textual dates and wiki-link notation remain model-interpreted material on the
          recorded consumption paths.
      - scope: Raw original payloads consumed during source reading and synthesis
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw
        - runtime.md#rt-rte-agent-session
        note: No concrete original is retained in the frozen source. PDF/gist/meeting-note examples do
          not resolve mixed text, binary or other operative parts; wiki display prose cannot classify
          those payloads.
      records:
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-index
      - memory.md#mem-obj-domain-pages
      - memory.md#mem-obj-decisions
      - memory.md#mem-obj-log
      - memory.md#mem-obj-raw
      - runtime.md#rt-rte-agent-session
      note: Natural-language wiki material is classified; raw-input form remains unresolved. No scoped
        retained numerical or fixed-rule symbolic consumer is established.
    lineage:
      assessment: partial
      units:
      - scope: Starter wiki content on current and older scaffold paths
        assessment: known
        findings:
        - value: authored
          basis: wired
          records:
          - runtime.md#rt-rte-cli-init
          - runtime.md#rt-rte-legacy-init
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-index
          - memory.md#mem-obj-log
          note: Fixed authored templates seed absent wiki pages, rather than extracting accumulated work.
        records:
        - runtime.md#rt-rte-cli-init
        - runtime.md#rt-rte-legacy-init
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-index
        - memory.md#mem-obj-log
        note: This resolves template seeding only, not the production history of later populated sentences.
      - scope: Protocol-directed repository/raw synthesis into domain pages
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records:
          - runtime.md#rt-rte-agent-session
          - memory.md#mem-rte-repository-ingest
          - memory.md#mem-obj-domain-pages
          - memory.md#mem-obj-decisions
          note: The foreground model selects and authors retained project prose.
        - value: other-compiled
          basis: claimed
          records:
          - runtime.md#rt-rte-agent-session
          - memory.md#mem-rte-repository-ingest
          - memory.md#mem-obj-raw
          note: Repository findings or deposited documents feed derived wiki content; this is a specified
            compilation path, not proof of faithful transformation.
        records:
        - runtime.md#rt-rte-agent-session
        - memory.md#mem-rte-repository-ingest
        - memory.md#mem-obj-raw
        - memory.md#mem-obj-domain-pages
        - memory.md#mem-obj-decisions
        note: These findings classify the declared derivation routes; they do not establish the exact
          inputs behind the frozen page instances.
      - scope: Work discoveries, task-end hot refresh and work-summary admission
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records:
          - runtime.md#rt-rte-agent-session
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-log
          - memory.md#mem-obj-domain-pages
          - memory.md#mem-obj-decisions
          note: The foreground agent authors state, summaries and selected discoveries.
        - value: trace-extracted
          basis: claimed
          records:
          - runtime.md#rt-rte-agent-session
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-log
          note: Recorded protocol requests derive hot context and historical summaries from coding work
            and task experience.
        records:
        - runtime.md#rt-rte-agent-session
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-log
        - memory.md#mem-obj-domain-pages
        - memory.md#mem-obj-decisions
        note: Work-to-memory extraction is requested; no execution trace authenticates an instance or
          its original trace serialization.
      - scope: Further derivation of already-retained work history by fold
        assessment: known
        findings:
        - value: other-compiled
          basis: claimed
          records:
          - memory.md#mem-rte-log-fold
          - memory.md#mem-obj-log
          note: The requested folded paragraph is derived from older work summaries rather than directly
            from demonstrated raw session turns.
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-rte-log-fold
          note: The model determines the replacement summary text.
        records:
        - memory.md#mem-rte-log-fold
        - memory.md#mem-obj-log
        note: The further-summary path is distinguished from the initial work-to-log path.
      - scope: Human-deposited raw originals
        assessment: partial
        findings:
        - value: imported
          basis: claimed
          records:
          - memory.md#mem-obj-raw
          - runtime.md#rt-rte-agent-session
          note: A human supplies external originals for source reading and wiki synthesis.
        records:
        - memory.md#mem-obj-raw
        - runtime.md#rt-rte-agent-session
        note: Import is specified, but no concrete original or its prior provenance is supplied; cannot
          classify all deployed raw-input derivations.
      - scope: Exact production provenance of populated frozen hot/domain/decision/log instances
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-domain-pages
        - memory.md#mem-obj-decisions
        - memory.md#mem-obj-log
        - memory.md#mem-rte-repository-ingest
        note: Population is attributed to ingestion, not linked to an authenticatable input/output trace.
          Template, document, repository and work derivations cannot be assigned sentence by sentence.
      records:
      - runtime.md#rt-rte-cli-init
      - runtime.md#rt-rte-legacy-init
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-index
      - memory.md#mem-obj-log
      - runtime.md#rt-rte-agent-session
      - memory.md#mem-rte-repository-ingest
      - memory.md#mem-obj-raw
      - memory.md#mem-obj-domain-pages
      - memory.md#mem-obj-decisions
      - memory.md#mem-rte-log-fold
      note: Known declared paths coexist with unresolved original provenance and instance history. Reported
        ingestion does not upgrade those paths to observed derivation.
    behavioral_authority:
      assessment: known
      units:
      - scope: Hot state and next steps at the later foreground coding agent
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-obj-hot
          - runtime.md#rt-rte-agent-session
          - runtime.md#rt-bap-host-protocol
          note: Retained state supplies project context to the requested first reader.
        - value: instruction
          basis: claimed
          records:
          - memory.md#mem-obj-hot
          - runtime.md#rt-rte-agent-session
          note: Retained next steps supply task guidance for the later agent.
        records:
        - memory.md#mem-obj-hot
        - runtime.md#rt-rte-agent-session
        - runtime.md#rt-bap-host-protocol
        note: Context and next-step directions are distinct effects; host compliance remains unobserved.
      - scope: Wiki index at the agent choosing additional pages
        assessment: known
        findings:
        - value: routing
          basis: claimed
          records:
          - memory.md#mem-obj-index
          - runtime.md#rt-rte-agent-session
          note: Retained page labels and locations guide the task-dependent choice of domain material.
        records:
        - memory.md#mem-obj-index
        - runtime.md#rt-rte-agent-session
        note: Navigation does not approve facts or impose a permission check. The outgoing-link count
          conflict does not change this force.
      - scope: Stack/patterns/bugs and decisions at the task-dependent coding reader
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-obj-domain-pages
          - memory.md#mem-obj-decisions
          - runtime.md#rt-rte-agent-session
          note: Facts, bug context and architectural rationale supply project reference/advice.
        - value: instruction
          basis: claimed
          records:
          - memory.md#mem-obj-domain-pages
          - runtime.md#rt-rte-agent-session
          note: Established coding conventions supply retained directions to the coding reader.
        records:
        - memory.md#mem-obj-domain-pages
        - memory.md#mem-obj-decisions
        - runtime.md#rt-rte-agent-session
        note: Conventions and advisory rationale do not become executable enforcement. The bug placeholder
          establishes no actual bug-learning instance.
      - scope: Work log at later history readers
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-obj-log
          - runtime.md#rt-rte-agent-session
          note: Historical summaries can supply context through index-mediated reading.
        records:
        - memory.md#mem-obj-log
        - runtime.md#rt-rte-agent-session
        note: Reading the log is conditional, unlike the hot-cache obligation.
      - scope: Retained work history at the fold update consumer
        assessment: known
        findings:
        - value: learning
          basis: claimed
          records:
          - memory.md#mem-obj-log
          - memory.md#mem-rte-log-fold
          note: The summarizing model consumes retained work experience to produce another durable context
            artifact for later sessions.
        records:
        - memory.md#mem-obj-log
        - memory.md#mem-rte-log-fold
        note: Update-consumer learning force is distinct from the folded output's downstream contextual
          force; no improved capacity is demonstrated.
      - scope: Raw originals at source-reading and synthesis consumers
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-obj-raw
          - runtime.md#rt-rte-agent-session
          note: Original documents supply reference and premises for project work and derived wiki content.
        records:
        - memory.md#mem-obj-raw
        - runtime.md#rt-rte-agent-session
        note: Unknown payload form and source truth do not prevent classification of this declared consumer
          role.
      records:
      - memory.md#mem-obj-hot
      - runtime.md#rt-rte-agent-session
      - runtime.md#rt-bap-host-protocol
      - memory.md#mem-obj-index
      - memory.md#mem-obj-domain-pages
      - memory.md#mem-obj-decisions
      - memory.md#mem-obj-log
      - memory.md#mem-rte-log-fold
      - memory.md#mem-obj-raw
      note: The included consumers and effects are recorded across the complete wiki/raw inventory. Static
        protocol criteria and external host controls are outside this memory scope; no ranking, validation
        or enforcement force is inferred from priority language or lint proposals.
    write_agency:
      assessment: partial
      units:
      - scope: Seeding absent wiki pages through either scaffold executable
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - runtime.md#rt-rte-cli-init
          - runtime.md#rt-rte-legacy-init
          note: Software admits fixed content after launch without an operator decision about each retained
            page.
        records:
        - runtime.md#rt-rte-cli-init
        - runtime.md#rt-rte-legacy-init
        note: Operator launch and cwd selection do not turn fixed-template admission into manual content
          control.
      - scope: Human delivery of raw original files
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records:
          - memory.md#mem-obj-raw
          note: The protocol assigns the human an explicit content-supply decision for raw originals.
        records:
        - memory.md#mem-obj-raw
        note: This is source admission, not approval of the subsequent wiki sentences.
      - scope: Agent discovery/raw synthesis, repository ingestion, hot refresh and work-log append
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records:
          - runtime.md#rt-rte-agent-session
          - memory.md#mem-rte-repository-ingest
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-log
          note: The foreground model selects and admits content through host file tools without a required
            per-content human decision.
        records:
        - runtime.md#rt-rte-agent-session
        - memory.md#mem-rte-repository-ingest
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-log
        note: Launching ingestion is not approving its results. Actual execution and external host vetoes
          remain unobserved.
      - scope: Older-history replacement by fold
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records:
          - memory.md#mem-rte-log-fold
          note: The model chooses retained summary content and its replacement after a user request, with
            no required content approval.
        records:
        - memory.md#mem-rte-log-fold
        note: The admission mechanism is separate from the read selecting older entries.
      - scope: Admission of lint proposals as retained corrections
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-wiki-lint
        note: Protocol says propose; README says fix. No required edit transition or approving principal
          is established, so neither automatic nor manual correction admission can be concluded.
      records:
      - runtime.md#rt-rte-cli-init
      - runtime.md#rt-rte-legacy-init
      - memory.md#mem-obj-raw
      - runtime.md#rt-rte-agent-session
      - memory.md#mem-rte-repository-ingest
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-log
      - memory.md#mem-rte-log-fold
      - memory.md#mem-rte-wiki-lint
      note: All specified write paths are retained, including the unresolved lint-to-edit transition.
        No arbitrary manual wiki editing is added merely because files are editable.
    curation_operations:
      assessment: partial
      units:
      - scope: Task-end hot/log summarization of work experience
        assessment: known
        findings:
        - value: consolidate
          basis: claimed
          records:
          - runtime.md#rt-rte-agent-session
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-log
          note: The requested state checkpoint and timestamped work summary reduce work experience into
            retained context.
        records:
        - runtime.md#rt-rte-agent-session
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-log
        note: This is a requested transformation, not a wired transcript-compaction interceptor or observed
          summary production.
      - scope: Refinement of existing wiki entries and refreshed hot content
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records:
          - runtime.md#rt-rte-agent-session
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-domain-pages
          - memory.md#mem-obj-decisions
          note: The protocol permits refinement of existing entries and asks replacement/refresh of current
            state.
        records:
        - runtime.md#rt-rte-agent-session
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-domain-pages
        - memory.md#mem-obj-decisions
        note: Revision intent is classified locally; no invalidation ledger or correctness check follows
          from refinement.
      - scope: Older retained log entries to a folded paragraph
        assessment: known
        findings:
        - value: consolidate
          basis: claimed
          records:
          - memory.md#mem-rte-log-fold
          - memory.md#mem-obj-log
          note: The specified operation condenses existing historical claims into a reduced representation
            while requesting preservation of crucial history.
        records:
        - memory.md#mem-rte-log-fold
        - memory.md#mem-obj-log
        note: Unknown semantic fidelity does not establish synthesis; fold is a claimed condensation route,
          not implemented model machinery.
      - scope: Raw/repository synthesis into domain prose
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw
        - runtime.md#rt-rte-agent-session
        - memory.md#mem-rte-repository-ingest
        - memory.md#mem-obj-domain-pages
        - memory.md#mem-obj-decisions
        note: No paired input/output establishes whether this transformation reduces existing claims,
          entails new ones or conjectures new claims. The word synthesis does not establish controlled
          synthesize.
      - scope: Lint proposals and any resulting retained-content transformation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-wiki-lint
        note: The proposed health fixes and their admission are unresolved. No recorded change establishes
          evolve, invalidate, dedup or another operation on this branch.
      records:
      - runtime.md#rt-rte-agent-session
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-log
      - memory.md#mem-obj-domain-pages
      - memory.md#mem-obj-decisions
      - memory.md#mem-rte-log-fold
      - memory.md#mem-obj-raw
      - memory.md#mem-rte-repository-ingest
      - memory.md#mem-rte-wiki-lint
      note: Consolidation and evolution are supported at claimed request level. Opaque synthesis and health-fix
        transitions prevent complete operation coverage; scaffold writes and index additions alone are
        not curation.
    read_back_direction:
      assessment: known
      units:
      - scope: Session-entry hot reads and conditional index/domain/history reads
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records:
          - runtime.md#rt-rte-agent-session
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-index
          - memory.md#mem-obj-domain-pages
          - memory.md#mem-obj-decisions
          - memory.md#mem-obj-log
          note: The foreground consumer requests project files using its task context and judgment of
            sufficiency; hooks request reading rather than selecting and delivering retained parts independently.
        records:
        - runtime.md#rt-rte-agent-session
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-index
        - memory.md#mem-obj-domain-pages
        - memory.md#mem-obj-decisions
        - memory.md#mem-obj-log
        note: The recorded route covers hot-first and conditional wiki access; external host injection/compaction
          is excluded.
      - scope: Raw original rereading for source use and synthesis
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records:
          - memory.md#mem-obj-raw
          - runtime.md#rt-rte-agent-session
          note: The agent reads user-supplied originals on the documented processing route.
        records:
        - memory.md#mem-obj-raw
        - runtime.md#rt-rte-agent-session
        note: There is no recorded watcher or unsolicited original-payload supply in the included mechanism.
      - scope: Retained older log input to fold and wiki input to lint
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records:
          - memory.md#mem-rte-log-fold
          - memory.md#mem-rte-wiki-lint
          - memory.md#mem-obj-log
          note: The requested maintenance consumer reads retained history or wiki evidence to perform
            the user-requested operation.
        records:
        - memory.md#mem-rte-log-fold
        - memory.md#mem-rte-wiki-lint
        - memory.md#mem-obj-log
        note: Requested material delivery is not another push operation. Unknown lint-result admission
          does not create an alternative input direction.
      records:
      - runtime.md#rt-rte-agent-session
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-index
      - memory.md#mem-obj-domain-pages
      - memory.md#mem-obj-decisions
      - memory.md#mem-obj-log
      - memory.md#mem-obj-raw
      - memory.md#mem-rte-log-fold
      - memory.md#mem-rte-wiki-lint
      note: All included later-consumer routes are requested file reads. Static host-hook discovery is
        not independent memory push; unknown external host behavior is not an included alternative.
    read_back_signal:
      assessment: inapplicable
      units:
      - scope: All scoped session, source-rereading and maintenance read-back operations
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-agent-session
        - memory.md#mem-obj-raw
        - memory.md#mem-rte-log-fold
        - memory.md#mem-rte-wiki-lint
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-index
        - memory.md#mem-obj-log
        note: Every included direction unit is requested pull. File identifiers and index entries select
          requested reads, not unsolicited delivery; therefore no push selector needs a signal classification.
      records:
      - runtime.md#rt-rte-agent-session
      - memory.md#mem-obj-raw
      - memory.md#mem-rte-log-fold
      - memory.md#mem-rte-wiki-lint
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-index
      - memory.md#mem-obj-log
      note: Inapplicability is bounded to the completely classified pull-only MemWiki file-read routes,
        not to external host context machinery.
    trace_learning:
      assessment: partial
      units:
      - scope: Work/task experience to hot continuation context and timestamped work summaries, then later
          coding readers
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - runtime.md#rt-rte-agent-session
          - memory.md#mem-obj-hot
          - memory.md#mem-obj-log
          note: The protocol asks automatic model admission of durable work-derived context/guidance for
            subsequent tasks or sessions.
        records:
        - runtime.md#rt-rte-agent-session
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-log
        note: This qualifies at claimed route level even without an automatic MemWiki model call or demonstrated
          improvement. Actual trace production and read-back remain unobserved.
      - scope: Retained summarized work history to folded summary, then conditional later history reader
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - memory.md#mem-rte-log-fold
          - memory.md#mem-obj-log
          note: Work history feeds model-chosen durable summary replacement with a later context-consumer
            role.
        records:
        - memory.md#mem-rte-log-fold
        - memory.md#mem-obj-log
        note: Already-derived experience can feed another qualifying update; no raw transcript is asserted.
      - scope: Pure repository-source ingestion into project reference pages
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-repository-ingest
        - memory.md#mem-obj-domain-pages
        - memory.md#mem-obj-decisions
        note: This unit acquires/compiles repository reference material rather than a qualifying trace-fed write. Inapplicability concerns that source-defined branch, not bounded absence of learning elsewhere.
      - scope: Human-supplied raw originals to wiki and later project readers
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw
        - runtime.md#rt-rte-agent-session
        note: No concrete payload determines whether imported material is static reference or recorded
          experience such as meeting activity. A qualifying trace-fed alternative cannot be ruled in or
          out.
      - scope: Lint-generated corrections, if admitted
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-wiki-lint
        note: No recorded input/evaluation experience, correction admission and durable later-consumer
          chain resolve a qualifying trace update.
      records:
      - runtime.md#rt-rte-agent-session
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-log
      - memory.md#mem-rte-log-fold
      - memory.md#mem-rte-repository-ingest
      - memory.md#mem-obj-domain-pages
      - memory.md#mem-obj-decisions
      - memory.md#mem-obj-raw
      - memory.md#mem-rte-wiki-lint
      note: Claimed work-derived continuation and fold routes establish positive existence. Raw payload and lint-admission uncertainties remain local. Repository-reference acquisition is a nonqualifying branch; no local or system-wide no is asserted without a bounded absence warrant.
    trace_source:
      assessment: not-determinable
      units:
      - scope: Original activity feeding work-derived hot/log context
        assessment: not-determinable
        findings: []
        records:
        - runtime.md#rt-rte-agent-session
        - memory.md#mem-obj-hot
        - memory.md#mem-obj-log
        note: Coding experience and work are named, but no recorded conversational turns, tool feedback,
          discrete event records or linked state/action/outcome sequence is established as the original
          input. Dates and summaries alone do not supply a controlled trace-source value.
      - scope: Original activity behind work summaries subsequently consumed by fold
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-log-fold
        - memory.md#mem-obj-log
        - runtime.md#rt-rte-agent-session
        note: Fold consumes already-summarized history; no raw transcript or original activity record
          permits session-logs, tool-traces, event-streams or trajectories classification.
      - scope: Possible trace-bearing raw inputs and any lint-derived correction path
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-raw
        - runtime.md#rt-rte-agent-session
        - memory.md#mem-rte-wiki-lint
        note: Neither qualifying trace content in a deployed original nor an admitted evaluation-fed correction
          is established. Unknown routes cannot inherit a trace-source value from the wiki display or
          a timestamp.
      records:
      - runtime.md#rt-rte-agent-session
      - memory.md#mem-obj-hot
      - memory.md#mem-obj-log
      - memory.md#mem-rte-log-fold
      - memory.md#mem-obj-raw
      - memory.md#mem-rte-wiki-lint
      note: Positive trace-learning routes have indeterminate original source content. No controlled trace-source
        positive is supported; this is not inapplicability or absence.
---

# MemWiki memory profile

## Comparison rationale

The operative memory is the mutable project wiki and its original-input directory, not the entire installed prompt surface. The current and legacy CLIs seed authored starter files, but the consequential cross-session writes and reads are requests to an external foreground agent. Hence wired seeding does not upgrade claimed model admission, condensation or consumption. The inspected retained prose establishes available representations, not observed production or beneficial activation. See [RT-RTE-cli-init](runtime.md#rt-rte-cli-init), [RT-RTE-legacy-init](runtime.md#rt-rte-legacy-init) and [RT-RTE-agent-session](runtime.md#rt-rte-agent-session).

The index supplies routing through model-interpreted page labels and links, not a symbolic resolver or retrieval ranker. Hot next steps and coding conventions supply instruction; facts and architectural rationale supply knowledge. The work log has a separate update consumer in fold: retained experience feeds another durable context artifact, while its later reader receives contextual knowledge. None of these paths establishes permission enforcement or epistemic acceptance. See [MEM-OBJ-index](memory.md#mem-obj-index), [MEM-OBJ-hot](memory.md#mem-obj-hot), [MEM-OBJ-domain-pages](memory.md#mem-obj-domain-pages), [MEM-OBJ-decisions](memory.md#mem-obj-decisions), [MEM-RTE-log-fold](memory.md#mem-rte-log-fold) and [EPI-ABS-acceptance-gate](epistemic.md#epi-abs-acceptance-gate).

Work-derived hot/log writes and fold satisfy the trace-learning axis at claimed route level: automatic content admission, durable derived context, and an identified later-consumer role. This classification is independent of improved capacity, source truth or successful execution. It does not license a trace-source guess: the recorded chain starts from coding experience or already-summarized work, not evidenced conversational turns, tool results or event callbacks. Repository-reference acquisition is outside qualifying trace-fed writes; this does not establish a bounded trace-learning absence. Raw inputs may contain activity or static reference, but no actual payload resolves that alternative. See [RT-RTE-agent-session](runtime.md#rt-rte-agent-session), [MEM-OBJ-log](memory.md#mem-obj-log), [MEM-RTE-log-fold](memory.md#mem-rte-log-fold), [MEM-RTE-repository-ingest](memory.md#mem-rte-repository-ingest) and [MEM-OBJ-raw](memory.md#mem-obj-raw).

Consolidation follows the requested work-summary and older-history reduction. A named synthesis command does not establish novel claims. The epistemic ledger leaves the exact semantic relation indeterminate without paired inputs/outputs; therefore the raw/repository branch cannot establish controlled synthesize, while fidelity uncertainty does not erase the explicitly requested fold consolidation. Lint may end at proposals, so its correction admission and curation stay unresolved. See [MEM-RTE-log-fold](memory.md#mem-rte-log-fold), [MEM-RTE-wiki-lint](memory.md#mem-rte-wiki-lint) and [MEM-RTE-repository-ingest](memory.md#mem-rte-repository-ingest).

Read-back remains pull within the scoped shipped routes. The foreground agent requests hot and conditional index/domain files; fold requests retained history. Hook discovery requests those reads but does not independently select and inject retained content. The push-only signal axis is therefore inapplicable here, not unknown because of the excluded host's private context machinery. See [RT-RTE-agent-session](runtime.md#rt-rte-agent-session), [MEM-OBJ-raw](memory.md#mem-obj-raw), [MEM-RTE-log-fold](memory.md#mem-rte-log-fold) and [MEM-RTE-wiki-lint](memory.md#mem-rte-wiki-lint).

Reconciliation supersedes the epistemic hot/index/log and lint/fold duplicates with their memory declarations; this profile cites those canonical memory records. The epistemic four-domain-page container remains valid but overlaps the memory domain/decision parts rather than replacing them. These identity decisions change no comparison value. The retained unresolved index-count conflict prevents a consistent numerical link inventory, not filesystem/form/routing or direction classification: no finding here depends on that count. The shared missing landscape/competitor links remain a limitation of reported delivery, not included opaque retained objects. See [MEM-OBJ-index](memory.md#mem-obj-index), [MEM-OBJ-log](memory.md#mem-obj-log), [MEM-OBJ-domain-pages](memory.md#mem-obj-domain-pages), [MEM-OBJ-decisions](memory.md#mem-obj-decisions) and [RT-RTE-agent-commands](runtime.md#rt-rte-agent-commands).

No source files were read for this profile. Classifications use only the supplied accepted records and their annotations, resolved through supplied reconciliation. Missing original payloads, exact sentence provenance, trace content and lint-admission facts prevent stronger coverage assessments. External host behavior is an explicit boundary exclusion, not a silently discarded internal alternative.
