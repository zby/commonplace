---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: 'Memory profile of Auto-claude-code-research-in-sleep: wiki, review continuity, recovery
  checkpoints and usage-guided maintenance at a frozen partial-loop boundary.'
run-id: AAS-2026-10-15-auto-claude-code-research-in-sleep-a8abf5f80cbb-01
source-identity: https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep
reviewed-boundary: 26b95cfa0d8747078e9e43b42e20952709e561b8
memory-comparison:
  version: 2
  scope: Accumulated project wiki pages, relationships and query pack; reviewer responses and derived
    memory; compact recovery checkpoints; usage and iteration history; trace/audit artifacts; trace-guided
    proposal/ledger and human-adopted skill revisions; retained phase/thread access metadata and opaque
    external conversation state on their later-use routes. Includes unresolved global-log consumers, style-profile
    extraction, trace writers and platform maintenance identified by accepted records. Excludes static
    unmodified shipped instructions, model inference weights, ordinary unretained working turns, and host
    scheduling/eviction implementation.
  axes:
    storage_substrate:
      assessment: partial
      units:
      - scope: Wiki pages and cached projection
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-papers
          - memory.md#mem-obj-ideas
          - memory.md#mem-obj-experiments
          - memory.md#mem-obj-claims
          - memory.md#mem-obj-edges
          - memory.md#mem-obj-query-pack
          note: Markdown pages and query pack are operative disk files.
        records:
        - memory.md#mem-obj-papers
        - memory.md#mem-obj-ideas
        - memory.md#mem-obj-experiments
        - memory.md#mem-obj-claims
        - memory.md#mem-obj-edges
        - memory.md#mem-obj-query-pack
        note: Markdown pages and query pack are operative disk files.
      - scope: Relationship triples and quarantine history
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-edges
          note: JSONL triples are files; the graph is their logical organization, not an evidenced separate
            graph database.
        records:
        - memory.md#mem-obj-edges
        note: JSONL triples are files; the graph is their logical organization, not an evidenced separate
          graph database.
      - scope: Reviewer memory and compact recovery checkpoints
        assessment: known
        findings:
        - value: files
          basis: claimed
          records:
          - memory.md#mem-obj-reviewer-memory
          - memory.md#mem-rte-reviewer-memory
          - memory.md#mem-obj-compact-files
          - memory.md#mem-rte-compact-recovery
          note: The procedures specify retained Markdown files; their production and replay are not observed.
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: The procedures specify retained Markdown files; their production and replay are not observed.
      - scope: Usage events and iteration history
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - memory.md#mem-obj-events
          - memory.md#mem-rte-stall-pivot
          note: Event summaries and iteration records are JSONL disk files.
        records:
        - memory.md#mem-obj-events
        - memory.md#mem-rte-stall-pivot
        note: Event summaries and iteration records are JSONL disk files.
      - scope: Edited skill body, staged patches and cycle ledger
        assessment: known
        findings:
        - value: files
          basis: claimed
          records:
          - runtime.md#rt-obj-skill
          - runtime.md#rt-rte-meta-landing
          note: The proposal and landing procedures specify disk skill text, staged diffs and cycle ledger;
            the wired receipt producer does not establish these procedural writes.
        records:
        - runtime.md#rt-obj-skill
        - runtime.md#rt-rte-meta-landing
        note: File storage is classified for the specified proposal/ledger and skill-replacement branches
          at their claimed procedural basis, without borrowing receipt implementation strength.
      - scope: Provenance receipt sidecars
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-skill
          - runtime.md#rt-rte-meta-landing
          note: The inspected stamping implementation persists process receipts and content hashes in sidecars.
        records:
        - runtime.md#rt-obj-skill
        - runtime.md#rt-rte-meta-landing
        note: Wired file storage applies to receipt stamping, not the separate model-followed proposal,
          ledger or skill-replacement procedures.
      - scope: Review request/response and acquittal artifacts
        assessment: known
        findings:
        - value: files
          basis: claimed
          records:
          - memory.md#mem-obj-review-traces
          note: The trace protocol specifies filesystem artifacts; serialization helper is uninspected.
        records:
        - memory.md#mem-obj-review-traces
        note: The trace protocol specifies filesystem artifacts; serialization helper is uninspected.
      - scope: Phase and per-thread access metadata
        assessment: known
        findings:
        - value: files
          basis: wired
          records:
          - runtime.md#rt-obj-run-state
          - runtime.md#rt-rte-codex-call
          note: Run JSON and per-thread option files persist symbolic access/recovery metadata.
        records:
        - runtime.md#rt-obj-run-state
        - runtime.md#rt-rte-codex-call
        note: Run JSON and per-thread option files persist symbolic access/recovery metadata.
      - scope: External CLI/provider conversation payload
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-codex-call
        - memory.md#mem-rte-reviewer-memory
        note: The bridge delegates conversation retention; neither its storage substrate nor opaque payload
          internals is inspected.
      - scope: Included remaining maintenance and platform routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-review-traces
        - memory.md#mem-obj-events
        - memory.md#mem-rte-paper-capture
        - runtime.md#rt-rte-meta-landing
        note: Global-log consumers, style-profile extraction, trace writers and platform alternatives
          remain uninspected; known file witnesses do not resolve their operative storage.
      records:
      - memory.md#mem-obj-papers
      - memory.md#mem-obj-ideas
      - memory.md#mem-obj-experiments
      - memory.md#mem-obj-claims
      - memory.md#mem-obj-edges
      - memory.md#mem-obj-query-pack
      - memory.md#mem-obj-reviewer-memory
      - memory.md#mem-rte-reviewer-memory
      - memory.md#mem-obj-compact-files
      - memory.md#mem-rte-compact-recovery
      - memory.md#mem-obj-events
      - memory.md#mem-rte-stall-pivot
      - runtime.md#rt-obj-skill
      - runtime.md#rt-rte-meta-landing
      - memory.md#mem-obj-review-traces
      - runtime.md#rt-obj-run-state
      - runtime.md#rt-rte-codex-call
      - memory.md#mem-rte-paper-capture
      note: File storage has wired witnesses for helper-produced artifacts and receipts, and claimed
        witnesses for procedural reviewer, checkpoint, proposal/ledger and skill-replacement writes.
        External conversation state and the remaining partial-loop inventory prevent complete enumeration.
    representational_form:
      assessment: partial
      units:
      - scope: Wiki thesis, hypothesis, lessons, statement/scope and relationship evidence
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-papers
          - memory.md#mem-obj-ideas
          - memory.md#mem-obj-experiments
          - memory.md#mem-obj-claims
          - memory.md#mem-obj-edges
          - memory.md#mem-obj-query-pack
          note: These retained prose parts require model or human interpretation.
        records:
        - memory.md#mem-obj-papers
        - memory.md#mem-obj-ideas
        - memory.md#mem-obj-experiments
        - memory.md#mem-obj-claims
        - memory.md#mem-obj-edges
        - memory.md#mem-obj-query-pack
        note: These retained prose parts require model or human interpretation.
      - scope: Wiki outcome/status/node IDs and delivered relation triples
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-papers
          - memory.md#mem-obj-ideas
          - memory.md#mem-obj-experiments
          - memory.md#mem-obj-claims
          - memory.md#mem-obj-edges
          - memory.md#mem-obj-query-pack
          - memory.md#mem-rte-pack-read
          note: Fixed code selects by outcome, parses frontmatter and constructs typed relation displays;
            text encoding alone is not natural-language form.
        records:
        - memory.md#mem-obj-papers
        - memory.md#mem-obj-ideas
        - memory.md#mem-obj-experiments
        - memory.md#mem-obj-claims
        - memory.md#mem-obj-edges
        - memory.md#mem-obj-query-pack
        - memory.md#mem-rte-pack-read
        note: Fixed code selects by outcome, parses frontmatter and constructs typed relation displays;
          text encoding alone is not natural-language form.
      - scope: Reviewer raw responses and reviewer-authored memory
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records:
          - memory.md#mem-obj-reviewer-memory
          - memory.md#mem-rte-reviewer-memory
          note: Later reviewers interpret full responses and suspicions as text.
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        note: Later reviewers interpret full responses and suspicions as text.
      - scope: 'Compact summaries: prose'
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records:
          - memory.md#mem-obj-compact-files
          - memory.md#mem-rte-compact-recovery
          note: Candidate and experiment summaries supply model-interpreted context.
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: Candidate and experiment summaries supply model-interpreted context.
      - scope: 'Compact summaries: configuration, metrics and reproduction commands'
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records:
          - memory.md#mem-obj-compact-files
          - memory.md#mem-rte-compact-recovery
          note: Tables/configurations, metrics and commands preserve localized formal inputs alongside
            prose.
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: Tables/configurations, metrics and commands preserve localized formal inputs alongside prose.
      - scope: Usage previews and iteration directions
        assessment: known
        findings:
        - value: natural-language
          basis: wired
          records:
          - memory.md#mem-obj-events
          - memory.md#mem-rte-stall-pivot
          note: Prompt/command previews and recorded directions preserve interpretable textual material.
        records:
        - memory.md#mem-obj-events
        - memory.md#mem-rte-stall-pivot
        note: Prompt/command previews and recorded directions preserve interpretable textual material.
      - scope: Event fields, counters and resume/access metadata
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - memory.md#mem-obj-events
          - memory.md#mem-rte-stall-pivot
          - runtime.md#rt-obj-run-state
          - runtime.md#rt-rte-codex-call
          note: Event labels, counts, phase policy and saved options have fixed-rule consumers.
        records:
        - memory.md#mem-obj-events
        - memory.md#mem-rte-stall-pivot
        - runtime.md#rt-obj-run-state
        - runtime.md#rt-rte-codex-call
        note: Event labels, counts, phase policy and saved options have fixed-rule consumers.
      - scope: Landed skill procedural body and patch rationale
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records:
          - runtime.md#rt-obj-skill
          - runtime.md#rt-bap-skill-instructions
          note: Later host invocation interprets revised method text; model weights are not the retained
            artifact classified here.
        records:
        - runtime.md#rt-obj-skill
        - runtime.md#rt-bap-skill-instructions
        note: Later host invocation interprets revised method text; model weights are not the retained
          artifact classified here.
      - scope: Staged patch syntax
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records:
          - runtime.md#rt-obj-skill
          - runtime.md#rt-rte-meta-landing
          note: The model-followed proposal procedure specifies symbolic unified diffs; receipt implementation
            does not establish patch production.
        records:
        - runtime.md#rt-obj-skill
        - runtime.md#rt-rte-meta-landing
        note: Unified-diff structure is classified at the proposal procedure's claimed basis, separately
          from wired receipt fields.
      - scope: Provenance receipt fields
        assessment: known
        findings:
        - value: symbolic
          basis: wired
          records:
          - runtime.md#rt-obj-skill
          - runtime.md#rt-rte-meta-landing
          note: The inspected receipt implementation persists symbolic hash and identity fields.
        records:
        - runtime.md#rt-obj-skill
        - runtime.md#rt-rte-meta-landing
        note: Wired symbolic form applies to receipt fields, not the separate model-followed staged-patch
          proposal procedure.
      - scope: Trace prompt/response bodies
        assessment: known
        findings:
        - value: natural-language
          basis: claimed
          records:
          - memory.md#mem-obj-review-traces
          note: Full natural-language prompt and response are prescribed separately from metadata.
        records:
        - memory.md#mem-obj-review-traces
        note: Full natural-language prompt and response are prescribed separately from metadata.
      - scope: Trace identities, hashes and acquittal metadata
        assessment: known
        findings:
        - value: symbolic
          basis: claimed
          records:
          - memory.md#mem-obj-review-traces
          note: Identity/evidence pointers and hashes are symbolic metadata, not an attested model-attention
            representation.
        records:
        - memory.md#mem-obj-review-traces
        note: Identity/evidence pointers and hashes are symbolic metadata, not an attested model-attention
          representation.
      - scope: Opaque retained provider conversation
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-codex-call
        - memory.md#mem-rte-reviewer-memory
        note: A readable final reply does not classify the retained conversation payload.
      - scope: Included remaining maintenance and platform routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-review-traces
        - memory.md#mem-obj-events
        - memory.md#mem-rte-paper-capture
        - runtime.md#rt-rte-meta-landing
        note: Uninspected style-profile generation, platform variants and remaining maintenance can contain
          additional operative forms.
      records:
      - memory.md#mem-obj-papers
      - memory.md#mem-obj-ideas
      - memory.md#mem-obj-experiments
      - memory.md#mem-obj-claims
      - memory.md#mem-obj-edges
      - memory.md#mem-obj-query-pack
      - memory.md#mem-rte-pack-read
      - memory.md#mem-obj-reviewer-memory
      - memory.md#mem-rte-reviewer-memory
      - memory.md#mem-obj-compact-files
      - memory.md#mem-rte-compact-recovery
      - memory.md#mem-obj-events
      - memory.md#mem-rte-stall-pivot
      - runtime.md#rt-obj-run-state
      - runtime.md#rt-rte-codex-call
      - runtime.md#rt-obj-skill
      - runtime.md#rt-bap-skill-instructions
      - runtime.md#rt-rte-meta-landing
      - memory.md#mem-obj-review-traces
      - memory.md#mem-rte-paper-capture
      note: Split textual content from fields consumed by fixed rules. Staged unified diffs retain a claimed
        symbolic finding; wired receipt fields do not upgrade the proposal procedure. Opaque conversation
        payloads and uninspected derived profiles prevent complete form coverage.
    lineage:
      assessment: partial
      units:
      - scope: Paper metadata and original abstract
        assessment: known
        findings:
        - value: imported
          basis: wired
          records:
          - memory.md#mem-obj-papers
          - memory.md#mem-rte-paper-capture
          note: The arXiv branch imports metadata and abstract into a page scaffold.
        records:
        - memory.md#mem-obj-papers
        - memory.md#mem-rte-paper-capture
        note: The arXiv branch imports metadata and abstract into a page scaffold.
      - scope: Paper enrichment prose
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-obj-papers
          - memory.md#mem-rte-paper-capture
          note: The model is directed to write source-derived summaries from fetched summaries or abstract.
        records:
        - memory.md#mem-obj-papers
        - memory.md#mem-rte-paper-capture
        note: The model is directed to write source-derived summaries from fetched summaries or abstract.
      - scope: Caller-supplied paper metadata and direct helper content
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-paper-capture
        - memory.md#mem-rte-evaluation-write
        note: Generic caller strings do not establish whether initial content was authored, imported or
          extracted.
      - scope: Initial idea hypotheses and risk text
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-obj-ideas
          - memory.md#mem-rte-evaluation-write
          note: The instructed model-generated initial ideas are authored research candidates.
        records:
        - memory.md#mem-obj-ideas
        - memory.md#mem-rte-evaluation-write
        note: The instructed model-generated initial ideas are authored research candidates.
      - scope: Experiment judgments and outcome lessons
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - memory.md#mem-obj-experiments
          - memory.md#mem-rte-evaluation-write
          - epistemic.md#epi-rte-result-integration
          note: The instructed result branch derives retained judgments/lessons from experiment feedback;
            direct helper inputs remain a separate unresolved alternative.
        records:
        - memory.md#mem-obj-experiments
        - memory.md#mem-rte-evaluation-write
        - epistemic.md#epi-rte-result-integration
        note: The instructed result branch derives retained judgments/lessons from experiment feedback;
          direct helper inputs remain a separate unresolved alternative.
      - scope: Proof-audit claim prose
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-obj-claims
          - epistemic.md#epi-rte-proof-disposition
          note: The proof branch records an audited statement and scope supplied by the model-followed
            procedure, not an automatically verified theorem.
        records:
        - memory.md#mem-obj-claims
        - epistemic.md#epi-rte-proof-disposition
        note: The proof branch records an audited statement and scope supplied by the model-followed procedure,
          not an automatically verified theorem.
      - scope: Query pack and rendered relationship displays
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - memory.md#mem-obj-query-pack
          - memory.md#mem-rte-pack-read
          - memory.md#mem-obj-edges
          note: Fixed code compiles retained excerpts and triples; graph evidence itself remains caller-supplied.
        records:
        - memory.md#mem-obj-query-pack
        - memory.md#mem-rte-pack-read
        - memory.md#mem-obj-edges
        note: Fixed code compiles retained excerpts and triples; graph evidence itself remains caller-supplied.
      - scope: Initial relationship evidence and direct claim/experiment fields
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-edges
        - memory.md#mem-rte-evaluation-write
        - epistemic.md#epi-rte-wiki-retention
        note: Persistence/rendering establishes no uniform origin for caller-provided assertions.
      - scope: Raw reviewer response replay
        assessment: known
        findings:
        - value: imported
          basis: claimed
          records:
          - memory.md#mem-obj-reviewer-memory
          - memory.md#mem-rte-reviewer-memory
          note: Verbatim review text is brought into the memory file from the reviewer output without
            executor rewriting.
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        note: Verbatim review text is brought into the memory file from the reviewer output without executor
          rewriting.
      - scope: Reviewer-authored memory update
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - memory.md#mem-obj-reviewer-memory
          - memory.md#mem-rte-reviewer-memory
          note: The reviewer derives suspicions and judgments from its ongoing review experience; the
            raw-response part is kept distinct.
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        note: The reviewer derives suspicions and judgments from its ongoing review experience; the raw-response
          part is kept distinct.
      - scope: Compact candidate summary
        assessment: known
        findings:
        - value: authored
          basis: claimed
          records:
          - memory.md#mem-obj-compact-files
          - memory.md#mem-rte-compact-recovery
          note: The candidate checkpoint is a model-authored condensation of the idea artifacts; source
            session history is not established for every candidate.
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: The candidate checkpoint is a model-authored condensation of the idea artifacts; source
          session history is not established for every candidate.
      - scope: Compact experiment log
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - memory.md#mem-obj-compact-files
          - memory.md#mem-rte-compact-recovery
          note: Retained configuration/results/verdict/reproduction entries are derived from experiment
            activity, not full raw output.
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: Retained configuration/results/verdict/reproduction entries are derived from experiment
          activity, not full raw output.
      - scope: findings.md recovery input production
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: Production is only partly inspected; later consumption does not establish its complete lineage.
      - scope: Usage summaries and iteration count derivation
        assessment: known
        findings:
        - value: trace-extracted
          basis: wired
          records:
          - memory.md#mem-obj-events
          - memory.md#mem-rte-stall-pivot
          note: Logger transforms host payloads and prior counts into retained summaries/counters.
        records:
        - memory.md#mem-obj-events
        - memory.md#mem-rte-stall-pivot
        note: Logger transforms host payloads and prior counts into retained summaries/counters.
      - scope: Meta diagnosis, patch and next-cycle bottleneck ledger
        assessment: known
        findings:
        - value: trace-extracted
          basis: claimed
          records:
          - memory.md#mem-obj-events
          - runtime.md#rt-rte-meta-landing
          note: Model diagnosis and patch proposals derive from usage records and previous cycle evidence.
            Human landing is a separate adoption operation.
        records:
        - memory.md#mem-obj-events
        - runtime.md#rt-rte-meta-landing
        note: Model diagnosis and patch proposals derive from usage records and previous cycle evidence.
          Human landing is a separate adoption operation.
      - scope: Phase JSON and thread option persistence
        assessment: known
        findings:
        - value: other-compiled
          basis: wired
          records:
          - runtime.md#rt-obj-run-state
          - runtime.md#rt-rte-codex-call
          note: Fixed helper code serializes caller metadata and selected policy/options; it does not
            extract research claims.
        records:
        - runtime.md#rt-obj-run-state
        - runtime.md#rt-rte-codex-call
        note: Fixed helper code serializes caller metadata and selected policy/options; it does not extract
          research claims.
      - scope: External retained conversation and full trace serialization
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-codex-call
        - memory.md#mem-rte-reviewer-memory
        - memory.md#mem-obj-review-traces
        note: Provider history and trace-writer fidelity are not inspected.
      - scope: Included remaining maintenance and platform routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-review-traces
        - memory.md#mem-obj-events
        - memory.md#mem-rte-paper-capture
        - runtime.md#rt-rte-meta-landing
        note: Style extraction, global-log routes and platform maintenance may introduce additional derivations.
      records:
      - memory.md#mem-obj-papers
      - memory.md#mem-rte-paper-capture
      - memory.md#mem-rte-evaluation-write
      - memory.md#mem-obj-ideas
      - memory.md#mem-obj-experiments
      - epistemic.md#epi-rte-result-integration
      - memory.md#mem-obj-claims
      - epistemic.md#epi-rte-proof-disposition
      - memory.md#mem-obj-query-pack
      - memory.md#mem-rte-pack-read
      - memory.md#mem-obj-edges
      - epistemic.md#epi-rte-wiki-retention
      - memory.md#mem-obj-reviewer-memory
      - memory.md#mem-rte-reviewer-memory
      - memory.md#mem-obj-compact-files
      - memory.md#mem-rte-compact-recovery
      - memory.md#mem-obj-events
      - memory.md#mem-rte-stall-pivot
      - runtime.md#rt-rte-meta-landing
      - runtime.md#rt-obj-run-state
      - runtime.md#rt-rte-codex-call
      - memory.md#mem-obj-review-traces
      note: Acquisition, authored content, trace extraction and deterministic compilation coexist. Known
        subsequent derivation does not settle every initial caller-controlled input or opaque provider
        lineage.
    behavioral_authority:
      assessment: partial
      units:
      - scope: Wiki excerpts at later idea model
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-bap-wiki-ideation
          - memory.md#mem-rte-pack-read
          note: Papers and gaps provide reference/context to ideation through a scanned file read.
        records:
        - memory.md#mem-bap-wiki-ideation
        - memory.md#mem-rte-pack-read
        note: Papers and gaps provide reference/context to ideation through a scanned file read.
      - scope: Failed-idea outcomes at later ideation choice
        assessment: known
        findings:
        - value: ranking
          basis: claimed
          records:
          - memory.md#mem-bap-wiki-ideation
          - epistemic.md#epi-rte-query-consumption
          note: Failed ideas bias candidate priority/exclusion as a model-interpreted banlist. This is
            not a code-enforced action veto.
        records:
        - memory.md#mem-bap-wiki-ideation
        - epistemic.md#epi-rte-query-consumption
        note: Failed ideas bias candidate priority/exclusion as a model-interpreted banlist. This is not
          a code-enforced action veto.
      - scope: Outcome fields at projection selector
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-rte-pack-read
          - memory.md#mem-obj-ideas
          note: Retained negative/mixed outcomes select which idea snippets enter the pack.
        records:
        - memory.md#mem-rte-pack-read
        - memory.md#mem-obj-ideas
        note: Retained negative/mixed outcomes select which idea snippets enter the pack.
      - scope: Reviewer responses and derived memory at later reviewer
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-obj-reviewer-memory
          - memory.md#mem-rte-reviewer-memory
          note: Past critiques and unresolved suspicions provide context for subsequent assessment.
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        note: Past critiques and unresolved suspicions provide context for subsequent assessment.
      - scope: Reviewer experience at memory-update producer
        assessment: known
        findings:
        - value: learning
          basis: claimed
          records:
          - memory.md#mem-obj-reviewer-memory
          - memory.md#mem-rte-reviewer-memory
          note: Reviewer-owned accumulated review experience feeds a durable memory update for later critique;
            no improved review accuracy is inferred.
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        note: Reviewer-owned accumulated review experience feeds a durable memory update for later critique;
          no improved review accuracy is inferred.
      - scope: Compact summaries at later experiment/review consumer
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-obj-compact-files
          - memory.md#mem-rte-compact-recovery
          note: Selected ideas, results and reproduction inputs guide later invocations as context rather
            than standing host rules.
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: Selected ideas, results and reproduction inputs guide later invocations as context rather
          than standing host rules.
      - scope: Iteration stale counter at next logger call
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - memory.md#mem-rte-stall-pivot
          note: Last valid stale count determines next pivot/escalation decision.
        records:
        - memory.md#mem-rte-stall-pivot
        note: Last valid stale count determines next pivot/escalation decision.
      - scope: Iteration direction ledger at subsequent host tick
        assessment: known
        findings:
        - value: knowledge
          basis: claimed
          records:
          - memory.md#mem-rte-stall-pivot
          note: Recorded tried directions supply context to avoid repeating the same frame.
        records:
        - memory.md#mem-rte-stall-pivot
        note: Recorded tried directions supply context to avoid repeating the same frame.
      - scope: Usage summaries and prior bottleneck ledger at optimizer
        assessment: known
        findings:
        - value: learning
          basis: claimed
          records:
          - memory.md#mem-obj-events
          - runtime.md#rt-rte-meta-landing
          note: Accumulated experience supplies evidence for a durable diagnosis/patch/ledger update.
            The later skill admission remains human-gated.
        records:
        - memory.md#mem-obj-events
        - runtime.md#rt-rte-meta-landing
        note: Accumulated experience supplies evidence for a durable diagnosis/patch/ledger update. The
          later skill admission remains human-gated.
      - scope: Revised skill body at future host invocation
        assessment: known
        findings:
        - value: instruction
          basis: claimed
          records:
          - runtime.md#rt-obj-skill
          - runtime.md#rt-bap-skill-instructions
          note: Landed procedural text supplies standing directions when loaded by a later host.
        records:
        - runtime.md#rt-obj-skill
        - runtime.md#rt-bap-skill-instructions
        note: Landed procedural text supplies standing directions when loaded by a later host.
      - scope: Phase status/order/policy at resume selector
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-obj-run-state
          - runtime.md#rt-rte-phase-resume
          note: Retained status/policy determines the next unfinished stage, not scientific acceptance.
        records:
        - runtime.md#rt-obj-run-state
        - runtime.md#rt-rte-phase-resume
        note: Retained status/policy determines the next unfinished stage, not scientific acceptance.
      - scope: Saved model/config/sandbox/cwd at continuation launcher
        assessment: known
        findings:
        - value: routing
          basis: wired
          records:
          - runtime.md#rt-rte-codex-call
          note: Saved options choose continuation configuration and scope; external CLI owns its enforcement.
        records:
        - runtime.md#rt-rte-codex-call
        note: Saved options choose continuation configuration and scope; external CLI owns its enforcement.
      - scope: Provenance receipt/hash at is_auto_curatable
        assessment: known
        findings:
        - value: validation
          basis: wired
          records:
          - runtime.md#rt-rte-meta-landing
          note: Stored accepted fields and current hash are criteria for automatic-curation eligibility,
            and a failing check refuses eligibility when the consumer invokes it.
        - value: enforcement
          basis: wired
          records:
          - runtime.md#rt-rte-meta-landing
          note: Stored accepted fields and current hash are criteria for automatic-curation eligibility,
            and a failing check refuses eligibility when the consumer invokes it.
        records:
        - runtime.md#rt-rte-meta-landing
        note: Stored accepted fields and current hash are criteria for automatic-curation eligibility,
          and a failing check refuses eligibility when the consumer invokes it.
      - scope: Run-scoped acquittal artifacts at review procedure
        assessment: partial
        findings:
        - value: validation
          basis: claimed
          records:
          - memory.md#mem-obj-review-traces
          - runtime.md#rt-rte-review-transition
          note: Current receipts/evidence pointers support stop eligibility checks; writer fidelity and
            native validator internals remain unresolved.
        records:
        - memory.md#mem-obj-review-traces
        - runtime.md#rt-rte-review-transition
        note: Current receipts/evidence pointers support stop eligibility checks; writer fidelity and
          native validator internals remain unresolved.
      - scope: Quarantine raw history later consumer
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-edges
        - epistemic.md#epi-rte-wiki-retention
        note: Human review is afforded, but no actual automatic later consumer of raw quarantine history
          is established; retention alone has no authority.
      - scope: Opaque provider conversation at resumed reviewer
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-codex-call
        - memory.md#mem-rte-reviewer-memory
        note: The requested continuation is known, but what retained internal parts exert which force
          is not inspected.
      - scope: Included remaining maintenance and platform routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-review-traces
        - memory.md#mem-obj-events
        - memory.md#mem-rte-paper-capture
        - runtime.md#rt-rte-meta-landing
        note: Global log consumers, style-profile use and remaining platform maintenance are uninspected;
          no blanket authority union is complete.
      records:
      - memory.md#mem-bap-wiki-ideation
      - memory.md#mem-rte-pack-read
      - epistemic.md#epi-rte-query-consumption
      - memory.md#mem-obj-ideas
      - memory.md#mem-obj-reviewer-memory
      - memory.md#mem-rte-reviewer-memory
      - memory.md#mem-obj-compact-files
      - memory.md#mem-rte-compact-recovery
      - memory.md#mem-rte-stall-pivot
      - memory.md#mem-obj-events
      - runtime.md#rt-rte-meta-landing
      - runtime.md#rt-obj-skill
      - runtime.md#rt-bap-skill-instructions
      - runtime.md#rt-obj-run-state
      - runtime.md#rt-rte-phase-resume
      - runtime.md#rt-rte-codex-call
      - memory.md#mem-obj-review-traces
      - runtime.md#rt-rte-review-transition
      - memory.md#mem-obj-edges
      - epistemic.md#epi-rte-wiki-retention
      - memory.md#mem-rte-paper-capture
      note: Classifications name actual consumers, not authority inferred from a status name. Requested
        use remains claimed; opaque and uninspected consumers remain unresolved.
    write_agency:
      assessment: partial
      units:
      - scope: Hook event append and iteration derived-state append
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-obj-events
          - memory.md#mem-rte-stall-pivot
          note: Once invoked/deployed, software admits each summary/count without a per-content human
            verdict.
        records:
        - memory.md#mem-obj-events
        - memory.md#mem-rte-stall-pivot
        note: Once invoked/deployed, software admits each summary/count without a per-content human verdict.
      - scope: Deterministic pack rebuild
        assessment: known
        findings:
        - value: automatic
          basis: wired
          records:
          - memory.md#mem-rte-pack-read
          note: Code admits the selected extracts; an initiating request is not approval of every extract.
        records:
        - memory.md#mem-rte-pack-read
        note: Code admits the selected extracts; an initiating request is not approval of every extract.
      - scope: Skill-driven paper capture/enrichment and evaluation write-back
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records:
          - memory.md#mem-rte-paper-capture
          - memory.md#mem-rte-evaluation-write
          note: Models admit page content and outcome changes without mandatory per-content human approval.
        records:
        - memory.md#mem-rte-paper-capture
        - memory.md#mem-rte-evaluation-write
        note: Models admit page content and outcome changes without mandatory per-content human approval.
      - scope: Manual-field paper metadata admission
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-papers
        - memory.md#mem-rte-paper-capture
        note: Manual metadata fields are an alternative input format, but the generic caller is not authenticated
          as a human making a per-content admission decision.
      - scope: Generic direct helper/API writes
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-paper-capture
        - memory.md#mem-rte-evaluation-write
        - runtime.md#rt-rte-phase-resume
        note: Caller identity/control is unspecified; physical Python I/O does not determine whether admission
          is human or computational.
      - scope: Reviewer append, derived memory and compact production
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records:
          - memory.md#mem-obj-reviewer-memory
          - memory.md#mem-rte-reviewer-memory
          - memory.md#mem-obj-compact-files
          - memory.md#mem-rte-compact-recovery
          note: The model-followed procedures admit outputs without a required per-append or per-summary
            human decision.
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: The model-followed procedures admit outputs without a required per-append or per-summary
          human decision.
      - scope: Meta diagnosis, pending diff and bottleneck report production
        assessment: known
        findings:
        - value: automatic
          basis: claimed
          records:
          - memory.md#mem-obj-events
          - runtime.md#rt-rte-meta-landing
          note: Producer model creates proposals and durable cycle evidence before human selection; this
            is separate from live skill adoption.
        records:
        - memory.md#mem-obj-events
        - runtime.md#rt-rte-meta-landing
        note: Producer model creates proposals and durable cycle evidence before human selection; this
          is separate from live skill adoption.
      - scope: Landed skill replacement
        assessment: known
        findings:
        - value: manual
          basis: claimed
          records:
          - runtime.md#rt-rte-meta-landing
          - runtime.md#rt-obj-skill
          note: Human selects patches and separately invokes landing; jury PASS is additionally required.
            Applier I/O does not erase the explicit content-adoption decision.
        records:
        - runtime.md#rt-rte-meta-landing
        - runtime.md#rt-obj-skill
        note: Human selects patches and separately invokes landing; jury PASS is additionally required.
          Applier I/O does not erase the explicit content-adoption decision.
      - scope: Trace-writer, external conversation and remaining maintenance admission
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-codex-call
        - memory.md#mem-rte-reviewer-memory
        - memory.md#mem-obj-review-traces
        - memory.md#mem-obj-events
        - memory.md#mem-rte-paper-capture
        - runtime.md#rt-rte-meta-landing
        note: Uninspected writers and provider internals prevent a complete admission-control account.
      records:
      - memory.md#mem-obj-events
      - memory.md#mem-rte-stall-pivot
      - memory.md#mem-rte-pack-read
      - memory.md#mem-rte-paper-capture
      - memory.md#mem-rte-evaluation-write
      - memory.md#mem-obj-papers
      - runtime.md#rt-rte-phase-resume
      - memory.md#mem-obj-reviewer-memory
      - memory.md#mem-rte-reviewer-memory
      - memory.md#mem-obj-compact-files
      - memory.md#mem-rte-compact-recovery
      - runtime.md#rt-rte-meta-landing
      - runtime.md#rt-obj-skill
      - runtime.md#rt-rte-codex-call
      - memory.md#mem-obj-review-traces
      note: Admission control is separate from authorship and physical I/O. Model/software admissions
        are automatic, explicit patch selection/landing is manual, and generic helper callers remain unresolved.
    curation_operations:
      assessment: partial
      units:
      - scope: Wiki pack excerpting
        assessment: known
        findings:
        - value: consolidate
          basis: wired
          records:
          - memory.md#mem-rte-pack-read
          - epistemic.md#epi-rte-query-pack
          note: Fixed budgets compress and combine existing retained claims; omitted qualifiers do not
            turn extraction into synthesis.
        records:
        - memory.md#mem-rte-pack-read
        - epistemic.md#epi-rte-query-pack
        note: Fixed budgets compress and combine existing retained claims; omitted qualifiers do not turn
          extraction into synthesis.
      - scope: Existing wiki experiment/claim page replacement
        assessment: known
        findings:
        - value: evolve
          basis: wired
          records:
          - memory.md#mem-rte-evaluation-write
          - epistemic.md#epi-rte-wiki-retention
          note: Explicit overwrite/re-audit revises an existing retained page; it does not ensure scientific
            correctness or consistent edges.
        records:
        - memory.md#mem-rte-evaluation-write
        - epistemic.md#epi-rte-wiki-retention
        note: Explicit overwrite/re-audit revises an existing retained page; it does not ensure scientific
          correctness or consistent edges.
      - scope: Paper enrichment and idea-outcome revision
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records:
          - memory.md#mem-rte-paper-capture
          - memory.md#mem-rte-evaluation-write
          note: Models fill source-derived prose and revise retained outcomes under procedure.
        records:
        - memory.md#mem-rte-paper-capture
        - memory.md#mem-rte-evaluation-write
        note: Models fill source-derived prose and revise retained outcomes under procedure.
      - scope: Claim withdrawal via retracted status
        assessment: known
        findings:
        - value: invalidate
          basis: claimed
          records:
          - memory.md#mem-obj-claims
          - memory.md#mem-rte-evaluation-write
          - epistemic.md#epi-rte-proof-disposition
          note: Retraction marks withdrawn reliance while retaining a claim page; no global edge revocation
            is established.
        records:
        - memory.md#mem-obj-claims
        - memory.md#mem-rte-evaluation-write
        - epistemic.md#epi-rte-proof-disposition
        note: Retraction marks withdrawn reliance while retaining a claim page; no global edge revocation
          is established.
      - scope: Compact handoff creation
        assessment: partial
        findings:
        - value: consolidate
          basis: claimed
          records:
          - memory.md#mem-obj-compact-files
          - memory.md#mem-rte-compact-recovery
          note: Summarization reduces retained candidates/results to selected existing information; findings.md
            production remains uninspected.
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: Summarization reduces retained candidates/results to selected existing information; findings.md
          production remains uninspected.
      - scope: Reviewer-derived memory
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        note: Records establish optional reviewer-authored suspicions/judgments and append/replay, but
          not selection, compression or combination into a reduced representation of existing claims.
          Derivation alone establishes no controlled curation operation; raw responses remain verbatim
          and append-only.
      - scope: Landed skill revision
        assessment: known
        findings:
        - value: evolve
          basis: claimed
          records:
          - runtime.md#rt-rte-meta-landing
          - runtime.md#rt-obj-skill
          note: Selected edits revise existing procedural entries; optional rollout and actual improvement
            are unobserved.
        records:
        - runtime.md#rt-rte-meta-landing
        - runtime.md#rt-obj-skill
        note: Selected edits revise existing procedural entries; optional rollout and actual improvement
          are unobserved.
      - scope: Semantic novelty of wiki ideas, judgment prose and meta diagnoses
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-evaluation-write
        - epistemic.md#epi-rte-result-judgment
        - runtime.md#rt-rte-meta-landing
        note: Records do not establish which particular claims are absent from inputs. No synthesis value
          follows merely from generated prose or a route name.
      - scope: Graph/paper collision skips as curation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-edges
        - memory.md#mem-rte-paper-capture
        note: Existing-key/triple suppression alone establishes no controlled curation operation; changed
          edge evidence may remain stale.
      - scope: Provider conversation transformations
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-codex-call
        - memory.md#mem-rte-reviewer-memory
        note: Resumption does not expose internal summarization, trimming or maintenance.
      - scope: Included remaining maintenance and platform routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-review-traces
        - memory.md#mem-obj-events
        - memory.md#mem-rte-paper-capture
        - runtime.md#rt-rte-meta-landing
        note: Generic wiki update/lint, style-profile extraction, logging consumers and platform alternatives
          are not completely inspected.
      records:
      - memory.md#mem-rte-pack-read
      - epistemic.md#epi-rte-query-pack
      - memory.md#mem-rte-evaluation-write
      - epistemic.md#epi-rte-wiki-retention
      - memory.md#mem-rte-paper-capture
      - memory.md#mem-obj-claims
      - epistemic.md#epi-rte-proof-disposition
      - memory.md#mem-obj-compact-files
      - memory.md#mem-rte-compact-recovery
      - memory.md#mem-obj-reviewer-memory
      - memory.md#mem-rte-reviewer-memory
      - runtime.md#rt-rte-meta-landing
      - runtime.md#rt-obj-skill
      - epistemic.md#epi-rte-result-judgment
      - memory.md#mem-obj-edges
      - runtime.md#rt-rte-codex-call
      - memory.md#mem-obj-review-traces
      - memory.md#mem-obj-events
      note: Projection and selected overwrite routes establish positive operations, but no complete transformation
        inventory. Reviewer-derived updates lack a recorded transformation sufficient to classify their
        curation operation. Collision skips alone do not establish deduplication; requested semantic work
        is not upgraded to wired execution.
    read_back_direction:
      assessment: partial
      units:
      - scope: Idea-creator request for cached/rebuilt wiki pack
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records:
          - memory.md#mem-rte-pack-read
          note: Later consumer requests retained context, scans and Reads it; mutation-time projection
            is production, not unsolicited delivery.
        records:
        - memory.md#mem-rte-pack-read
        note: Later consumer requests retained context, scans and Reads it; mutation-time projection is
          production, not unsolicited delivery.
      - scope: Explicit reviewer thread continuation
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-codex-call
          note: Caller supplies a thread ID to request read-back; normal requested tool return is not
            an additional push.
        records:
        - runtime.md#rt-rte-codex-call
        note: Caller supplies a thread ID to request read-back; normal requested tool return is not an
          additional push.
      - scope: Hard-mode reviewer full-memory injection
        assessment: known
        findings:
        - value: push
          basis: claimed
          records:
          - memory.md#mem-obj-reviewer-memory
          - memory.md#mem-rte-reviewer-memory
          note: The next round triggers automatic supply of full retained reviewer memory into the assigned
            prompt, without a new reviewer request for that content.
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        note: The next round triggers automatic supply of full retained reviewer memory into the assigned
          prompt, without a new reviewer request for that content.
      - scope: Reviewer file-path access and medium-thread continuation
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records:
          - memory.md#mem-obj-reviewer-memory
          - memory.md#mem-rte-reviewer-memory
          note: Reviewer can request the named memory file or continue its thread; path supply alone does
            not prove its content was read.
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        note: Reviewer can request the named memory file or continue its thread; path supply alone does
          not prove its content was read.
      - scope: Compact checkpoint selection for downstream context
        assessment: known
        findings:
        - value: push
          basis: claimed
          records:
          - memory.md#mem-obj-compact-files
          - memory.md#mem-rte-compact-recovery
          note: A later experiment/review invocation automatically selects available compact summaries
            under the COMPACT/recovery procedure.
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: A later experiment/review invocation automatically selects available compact summaries under
          the COMPACT/recovery procedure.
      - scope: Next-cycle optimizer reading prior ledger and project events
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records:
          - memory.md#mem-obj-events
          - runtime.md#rt-rte-meta-landing
          note: The maintenance invocation requests retained usage and prior-cycle evidence; no idle-host
            context injector is established.
        records:
        - memory.md#mem-obj-events
        - runtime.md#rt-rte-meta-landing
        note: The maintenance invocation requests retained usage and prior-cycle evidence; no idle-host
          context injector is established.
      - scope: Iteration logger prior counter and explicit direction-history show
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - memory.md#mem-rte-stall-pivot
          note: Next note reads the last valid retained count as input; explicit show requests the recorded
            ledger.
        records:
        - memory.md#mem-rte-stall-pivot
        note: Next note reads the last valid retained count as input; explicit show requests the recorded
          ledger.
      - scope: Phase reload and per-thread options
        assessment: known
        findings:
        - value: pull
          basis: wired
          records:
          - runtime.md#rt-rte-phase-resume
          - runtime.md#rt-rte-codex-call
          note: Resume/reply requests cause loading retained metadata.
        records:
        - runtime.md#rt-rte-phase-resume
        - runtime.md#rt-rte-codex-call
        note: Resume/reply requests cause loading retained metadata.
      - scope: Later host loads changed skill
        assessment: known
        findings:
        - value: pull
          basis: claimed
          records:
          - runtime.md#rt-bap-skill-instructions
          note: A later skill invocation requests its installed procedural body; static unmodified instructions
            are outside this memory boundary.
        records:
        - runtime.md#rt-bap-skill-instructions
        note: A later skill invocation requests its installed procedural body; static unmodified instructions
          are outside this memory boundary.
      - scope: Opaque conversation internal selection
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-codex-call
        - memory.md#mem-rte-reviewer-memory
        note: Known requested continuation does not resolve internal delivery/selection operations.
      - scope: Included remaining maintenance and platform routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-review-traces
        - memory.md#mem-obj-events
        - memory.md#mem-rte-paper-capture
        - runtime.md#rt-rte-meta-landing
        note: Global-log consumer, style-profile reload, trace consumers and platform alternatives retain
          uninspected read-back paths.
      records:
      - memory.md#mem-rte-pack-read
      - runtime.md#rt-rte-codex-call
      - memory.md#mem-obj-reviewer-memory
      - memory.md#mem-rte-reviewer-memory
      - memory.md#mem-obj-compact-files
      - memory.md#mem-rte-compact-recovery
      - memory.md#mem-obj-events
      - runtime.md#rt-rte-meta-landing
      - memory.md#mem-rte-stall-pivot
      - runtime.md#rt-rte-phase-resume
      - runtime.md#rt-bap-skill-instructions
      - memory.md#mem-obj-review-traces
      - memory.md#mem-rte-paper-capture
      note: Requested retrieval and automatic later-context selection coexist. File rebuild alone is not
        push; opaque payload internals and uninspected routes prevent complete coverage.
    read_back_signal:
      assessment: partial
      units:
      - scope: Hard reviewer-memory prompt supply
        assessment: known
        findings:
        - value: coarse
          basis: claimed
          records:
          - memory.md#mem-obj-reviewer-memory
          - memory.md#mem-rte-reviewer-memory
          note: 'Trigger: next review round. Selector inputs: backend, difficulty and round. Selected
            part: entire reviewer memory file, without relevance filtering or truncation.'
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        note: 'Trigger: next review round. Selector inputs: backend, difficulty and round. Selected part:
          entire reviewer memory file, without relevance filtering or truncation.'
      - scope: Compact recovery context supply
        assessment: partial
        findings:
        - value: coarse
          basis: claimed
          records:
          - memory.md#mem-obj-compact-files
          - memory.md#mem-rte-compact-recovery
          note: 'Trigger: later experiment/review initialization. Selector inputs: COMPACT flag and file
            availability. Selected parts: candidate checkpoint or findings plus experiment log. File names
            are not targeted identity matches among retained content.'
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: 'Trigger: later experiment/review initialization. Selector inputs: COMPACT flag and file
          availability. Selected parts: candidate checkpoint or findings plus experiment log. File names
          are not targeted identity matches among retained content.'
      - scope: Requested wiki pack read
        assessment: inapplicable
        findings: []
        records:
        - memory.md#mem-rte-pack-read
        note: This local delivery fulfills a consumer request. Filename order/outcomes/budgets select
          the requested projection, not unsolicited push context.
      - scope: Explicit phase/thread/ledger/skill requests
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-phase-resume
        - runtime.md#rt-rte-codex-call
        - memory.md#mem-rte-stall-pivot
        - runtime.md#rt-bap-skill-instructions
        note: These local requested returns need no push signal; this does not classify provider-internal
          alternatives.
      - scope: Provider-internal context supply
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-codex-call
        - memory.md#mem-rte-reviewer-memory
        note: The bridge does not reveal how conversation parts are selected or whether additional push
          operations exist.
      - scope: Included remaining maintenance and platform routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-review-traces
        - memory.md#mem-obj-events
        - memory.md#mem-rte-paper-capture
        - runtime.md#rt-rte-meta-landing
        note: Uninspected style-profile, global-event and platform consumers prevent a complete inventory
          of push selectors.
      records:
      - memory.md#mem-obj-reviewer-memory
      - memory.md#mem-rte-reviewer-memory
      - memory.md#mem-obj-compact-files
      - memory.md#mem-rte-compact-recovery
      - memory.md#mem-rte-pack-read
      - runtime.md#rt-rte-phase-resume
      - runtime.md#rt-rte-codex-call
      - memory.md#mem-rte-stall-pivot
      - runtime.md#rt-bap-skill-instructions
      - memory.md#mem-obj-review-traces
      - memory.md#mem-obj-events
      - memory.md#mem-rte-paper-capture
      - runtime.md#rt-rte-meta-landing
      note: Only push selection is classified. Coarse route/availability selectors are not semantic or
        identity matching; pull-only local operations do not settle opaque alternatives.
    trace_learning:
      assessment: partial
      units:
      - scope: Compact experiment summary to later review
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - memory.md#mem-obj-compact-files
          - memory.md#mem-rte-compact-recovery
          note: Experiment activity feeds automatic model-authored retained results/verdict/reproduction
            summaries, later selected as review context. This qualifies by design even though runs are
            unobserved.
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: Experiment activity feeds automatic model-authored retained results/verdict/reproduction
          summaries, later selected as review context. This qualifies by design even though runs are unobserved.
      - scope: Reviewer-authored memory update to later reviewer
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - memory.md#mem-obj-reviewer-memory
          - memory.md#mem-rte-reviewer-memory
          note: Recorded review experience feeds automatically admitted durable suspicions/judgments,
            subsequently delivered to later rounds. Verbatim append alone would not establish this finding.
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        note: Recorded review experience feeds automatically admitted durable suspicions/judgments, subsequently
          delivered to later rounds. Verbatim append alone would not establish this finding.
      - scope: Experiment outcomes/lessons to later ideation
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - memory.md#mem-rte-evaluation-write
          - memory.md#mem-rte-pack-read
          - epistemic.md#epi-rte-result-integration
          note: The instructed automatic verdict/outcome update is retained and projected into later ideation
            as guidance; generic API content is not thereby classified.
        records:
        - memory.md#mem-rte-evaluation-write
        - memory.md#mem-rte-pack-read
        - epistemic.md#epi-rte-result-integration
        note: The instructed automatic verdict/outcome update is retained and projected into later ideation
          as guidance; generic API content is not thereby classified.
      - scope: Usage evidence to retained diagnosis/bottleneck ledger and next optimizer
        assessment: known
        findings:
        - value: 'yes'
          basis: claimed
          records:
          - memory.md#mem-obj-events
          - runtime.md#rt-rte-meta-landing
          note: Trace-fed model diagnosis and durable cycle ledger are produced before human landing,
            then requested by a later maintenance cycle. The qualifying automatic artifact is the proposal/ledger,
            not the manually adopted skill.
        records:
        - memory.md#mem-obj-events
        - runtime.md#rt-rte-meta-landing
        note: Trace-fed model diagnosis and durable cycle ledger are produced before human landing, then
          requested by a later maintenance cycle. The qualifying automatic artifact is the proposal/ledger,
          not the manually adopted skill.
      - scope: Human-approved live skill replacement
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-meta-landing
        note: Explicit human patch selection/adoption makes this admission manual. It cannot supply an
          automatic trace-learning witness, even though earlier proposals can.
      - scope: Counter/phase/options persistence in isolation
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-rte-stall-pivot
        - runtime.md#rt-rte-phase-resume
        - runtime.md#rt-rte-codex-call
        note: Counters and ordinary recovery/access metadata do not by themselves establish a durable
          behavior-shaping artifact update. No bounded system-wide negative is inferred.
      - scope: Candidate checkpoint and findings production
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: Candidate condensation is specified, but complete trace origin and findings production are
          missing; the known experiment-log witness does not resolve these alternatives.
      - scope: External conversation maintenance and trace consumers
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-codex-call
        - memory.md#mem-rte-reviewer-memory
        - memory.md#mem-obj-review-traces
        note: Opaque retained history and uninspected serialization/consumer internals prevent qualifying
          or excluding their update routes.
      - scope: Included remaining maintenance and platform routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-review-traces
        - memory.md#mem-obj-events
        - memory.md#mem-rte-paper-capture
        - runtime.md#rt-rte-meta-landing
        note: Style extraction, global-log use and platform maintenance may add qualifying routes; raw
          event logging alone is not counted.
      records:
      - memory.md#mem-obj-compact-files
      - memory.md#mem-rte-compact-recovery
      - memory.md#mem-obj-reviewer-memory
      - memory.md#mem-rte-reviewer-memory
      - memory.md#mem-rte-evaluation-write
      - memory.md#mem-rte-pack-read
      - epistemic.md#epi-rte-result-integration
      - memory.md#mem-obj-events
      - runtime.md#rt-rte-meta-landing
      - memory.md#mem-rte-stall-pivot
      - runtime.md#rt-rte-phase-resume
      - runtime.md#rt-rte-codex-call
      - memory.md#mem-obj-review-traces
      - memory.md#mem-rte-paper-capture
      note: Positive classifications concern automatic trace-fed durable context/guidance, not demonstrated
        improvement. Manual skill adoption is distinct from automatic proposal/ledger production, and
        raw logging alone is insufficient.
    trace_source:
      assessment: partial
      units:
      - scope: Compact experiment-log generation
        assessment: known
        findings:
        - value: tool-traces
          basis: claimed
          records:
          - memory.md#mem-obj-compact-files
          - memory.md#mem-rte-compact-recovery
          note: Original input comprises experiment execution feedback/results and reproduction activity,
            not merely a Markdown adapter label. Full log reasons may be omitted.
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: Original input comprises experiment execution feedback/results and reproduction activity,
          not merely a Markdown adapter label. Full log reasons may be omitted.
      - scope: Reviewer-derived memory update
        assessment: known
        findings:
        - value: session-logs
          basis: claimed
          records:
          - memory.md#mem-obj-reviewer-memory
          - memory.md#mem-rte-reviewer-memory
          note: Original input is conversational reviewer responses from ongoing agent review sessions.
            Provider-internal tool history is not established as an input to every memory update.
        records:
        - memory.md#mem-obj-reviewer-memory
        - memory.md#mem-rte-reviewer-memory
        note: Original input is conversational reviewer responses from ongoing agent review sessions.
          Provider-internal tool history is not established as an input to every memory update.
      - scope: Evaluation-derived outcome/lesson update
        assessment: known
        findings:
        - value: tool-traces
          basis: claimed
          records:
          - memory.md#mem-rte-evaluation-write
          - epistemic.md#epi-rte-result-judgment
          - epistemic.md#epi-rte-result-integration
          note: Experiment feedback and reviewer-session judgments are the original mixed sources for
            retained outcomes used by later ideation.
        - value: session-logs
          basis: claimed
          records:
          - memory.md#mem-rte-evaluation-write
          - epistemic.md#epi-rte-result-judgment
          - epistemic.md#epi-rte-result-integration
          note: Experiment feedback and reviewer-session judgments are the original mixed sources for
            retained outcomes used by later ideation.
        records:
        - memory.md#mem-rte-evaluation-write
        - epistemic.md#epi-rte-result-judgment
        - epistemic.md#epi-rte-result-integration
        note: Experiment feedback and reviewer-session judgments are the original mixed sources for retained
          outcomes used by later ideation.
      - scope: Usage-driven diagnosis and next-cycle ledger
        assessment: known
        findings:
        - value: event-streams
          basis: claimed
          records:
          - memory.md#mem-obj-events
          - runtime.md#rt-rte-meta-landing
          note: Host lifecycle callbacks supply discrete events, tool request/result-related payloads
            supply tool traces, and logged user prompt previews supply recorded session turns. These origins
            are not inferred solely from JSONL serialization.
        - value: tool-traces
          basis: claimed
          records:
          - memory.md#mem-obj-events
          - runtime.md#rt-rte-meta-landing
          note: Host lifecycle callbacks supply discrete events, tool request/result-related payloads
            supply tool traces, and logged user prompt previews supply recorded session turns. These origins
            are not inferred solely from JSONL serialization.
        - value: session-logs
          basis: claimed
          records:
          - memory.md#mem-obj-events
          - runtime.md#rt-rte-meta-landing
          note: Host lifecycle callbacks supply discrete events, tool request/result-related payloads
            supply tool traces, and logged user prompt previews supply recorded session turns. These origins
            are not inferred solely from JSONL serialization.
        records:
        - memory.md#mem-obj-events
        - runtime.md#rt-rte-meta-landing
        note: Host lifecycle callbacks supply discrete events, tool request/result-related payloads supply
          tool traces, and logged user prompt previews supply recorded session turns. These origins are
          not inferred solely from JSONL serialization.
      - scope: Manually adopted live skill patch
        assessment: inapplicable
        findings: []
        records:
        - runtime.md#rt-rte-meta-landing
        note: This admission is not a qualifying automatic trace-fed write; its proposal/ledger source
          is classified separately.
      - scope: Candidate checkpoint/findings complete original inputs
        assessment: not-determinable
        findings: []
        records:
        - memory.md#mem-obj-compact-files
        - memory.md#mem-rte-compact-recovery
        note: A compact output label does not establish all original trace types; production of findings
          is partly uninspected.
      - scope: Opaque conversation-derived updates
        assessment: uninspected
        findings: []
        records:
        - runtime.md#rt-rte-codex-call
        - memory.md#mem-rte-reviewer-memory
        note: No inspected raw-to-derived provider chain establishes its original input inventory.
      - scope: Included remaining maintenance and platform routes
        assessment: uninspected
        findings: []
        records:
        - memory.md#mem-obj-review-traces
        - memory.md#mem-obj-events
        - memory.md#mem-rte-paper-capture
        - runtime.md#rt-rte-meta-landing
        note: Remaining extraction/global-event/platform routes lack inspected qualifying writes and original-input
          coverage.
      records:
      - memory.md#mem-obj-compact-files
      - memory.md#mem-rte-compact-recovery
      - memory.md#mem-obj-reviewer-memory
      - memory.md#mem-rte-reviewer-memory
      - memory.md#mem-rte-evaluation-write
      - epistemic.md#epi-rte-result-judgment
      - epistemic.md#epi-rte-result-integration
      - memory.md#mem-obj-events
      - runtime.md#rt-rte-meta-landing
      - runtime.md#rt-rte-codex-call
      - memory.md#mem-obj-review-traces
      - memory.md#mem-rte-paper-capture
      note: Original inputs to each qualifying route are classified locally. Mixed usage inputs retain
        separate content origins; unresolved summary/provider routes prevent a complete source union.
---

# Auto-claude-code-research-in-sleep memory profile

## Comparison rationale

The inventory remains partial on every axis. The accepted records distinguish inspected helper behavior, model-followed procedures, opaque conversation state and included but uninspected maintenance. No supplied execution or causal evidence upgrades a finding to observed or causally supported. Local known units mean classification coverage, not reliable model compliance.

### Canonical identities and scope

Reconciliation supersedes the epistemic query-pack object with [MEM-OBJ-query-pack](memory.md#mem-obj-query-pack), and the epistemic wiki-claim object with [MEM-OBJ-claims](memory.md#mem-obj-claims). All classifications use those canonical objects. The separately retained graph is [MEM-OBJ-edges](memory.md#mem-obj-edges), not part of a claim page. Construction and consumption remain separate routes: [EPI-RTE-query-pack](epistemic.md#epi-rte-query-pack) supports wired compression, while [EPI-RTE-query-consumption](epistemic.md#epi-rte-query-consumption) supports claimed later use. No supersession promotes either status.

The wiki graph uses file-backed triples. Its logical graph organization does not establish a distinct graph storage service. Provider weights are inference components, not retained memory updated by these routes. Opaque conversation state remains included, but a returned final message cannot classify its internal substrate or encoding. See [MEM-OBJ-edges](memory.md#mem-obj-edges) and [RT-RTE-codex-call](runtime.md#rt-rte-codex-call).

### Transformations and authority

The maintenance storage and form branches keep separate evidence bases. Proposal/ledger production and skill replacement specify files through claimed procedures; only receipt stamping supplies wired storage on its own branch. Staged unified-diff syntax is symbolic at a claimed procedural basis, while the receipt implementation supplies wired symbolic hash/identity fields. The receipt witness upgrades neither storage nor form on the proposal branch. See [RT-OBJ-skill](runtime.md#rt-obj-skill) and [RT-RTE-meta-landing](runtime.md#rt-rte-meta-landing).

Reviewer-derived suspicions and judgments do not establish consolidation. The accepted records specify optional updates and append/replay, but do not establish reduction of existing claims. This local curation operation remains not-determinable, independently of the supported consolidation of the wiki pack and compact handoffs. Trace-fed derivation and later consumption do not require a known curation operation. See [MEM-OBJ-reviewer-memory](memory.md#mem-obj-reviewer-memory) and [MEM-RTE-reviewer-memory](memory.md#mem-rte-reviewer-memory).

Fixed excerpting is consolidation. Filename order and character budgets are not semantic ranking, while retained outcome fields do route inclusion. The later model's instructed banlist affects candidate priority, not a guaranteed filesystem or action veto. Graph evidence, claim scope and full experiment reasoning can remain stored without reaching ideation. These limits follow [MEM-RTE-pack-read](memory.md#mem-rte-pack-read), [MEM-CLM-pack-contract](memory.md#mem-clm-pack-contract) and [MEM-BAP-wiki-ideation](memory.md#mem-bap-wiki-ideation).

Structural checks and scanners are not themselves accumulated memory merely because they control a write. By contrast, retained provenance receipt fields/hash are consumed by the eligibility checker and thus carry validation and enforcement locally. The receipt proves neither correctness nor reviewer execution. Full review trace writer/native-validator internals remain unknown. See [RT-RTE-meta-landing](runtime.md#rt-rte-meta-landing) and [MEM-OBJ-review-traces](memory.md#mem-obj-review-traces).

Overwrite supports evolution; a retraction status supports requested withdrawal, not removal of stale graph edges. Primary-key skips alone supply no dedup finding. Novel prose supplies no synthesis finding without recorded non-entailment. Requested stage-summary synthesis also cannot be promoted into a verified curation mechanism merely from its name. See [MEM-RTE-evaluation-write](memory.md#mem-rte-evaluation-write), [EPI-RTE-wiki-retention](epistemic.md#epi-rte-wiki-retention), [EPI-RTE-result-judgment](epistemic.md#epi-rte-result-judgment) and [RT-RTE-research-pipeline](runtime.md#rt-rte-research-pipeline).

### Read-back and trace-fed updates

A requested wiki pack is pull even though a mutation automatically rebuilds the file. Next-round full-memory injection and automatic compact-context substitution are push operations with coarse selectors. Their selected file names alone do not establish identifier-based targeting. Thread continuation is explicitly requested pull; internal provider selection stays uninspected. See [MEM-RTE-pack-read](memory.md#mem-rte-pack-read), [MEM-RTE-reviewer-memory](memory.md#mem-rte-reviewer-memory), [MEM-RTE-compact-recovery](memory.md#mem-rte-compact-recovery) and [RT-RTE-codex-call](runtime.md#rt-rte-codex-call).

Trace learning here means automatic trace-fed production of durable later context or guidance, not measured improved capacity. Compact experiment logs, reviewer-derived memory, evaluation-derived outcome guidance and the next-cycle maintenance ledger supply claimed positive chains. Verbatim logs alone do not. Human-selected live skill adoption is manual even though proposal/ledger production is computational. Experience supplies learning authority at an update consumer; derived context supplies knowledge at a later reviewer or ideator; revised live skill text supplies instruction. These are separate paths, not a blanket authority inference. See [MEM-RTE-compact-recovery](memory.md#mem-rte-compact-recovery), [MEM-RTE-reviewer-memory](memory.md#mem-rte-reviewer-memory), [EPI-RTE-result-integration](epistemic.md#epi-rte-result-integration), [RT-RTE-meta-landing](runtime.md#rt-rte-meta-landing) and [RT-BAP-skill-instructions](runtime.md#rt-bap-skill-instructions).

The remaining unknowns are consequential: findings production, opaque provider maintenance, global event consumers, trace serialization/native evidence checks, style extraction and platform alternatives prevent complete source, admission and consumer inventories. No local witness resolves them, and no trace-learning negative is inferred from ordinary recovery counters or manual skill landing. The accepted memory report retains these boundaries in [MEM-OBJ-compact-files](memory.md#mem-obj-compact-files), [MEM-OBJ-events](memory.md#mem-obj-events) and [MEM-OBJ-review-traces](memory.md#mem-obj-review-traces), with the provider boundary in [RT-RTE-codex-call](runtime.md#rt-rte-codex-call).

### Source-read log

No target source files were read for this classification. Only the supplied contracts, accepted members and reconciliation were used; no new records, evidence or quotations were added.
