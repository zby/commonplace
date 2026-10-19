---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "llm-wiki memory profile: maintained wiki content, routing and access traces, plus optional L1 rules and their external loading boundary."
run-id: AAS-2026-10-17-llm-wiki-1c5eb6f83ce5-01
source-identity: "https://github.com/MehmetGoekce/llm-wiki"
reviewed-boundary: "11538c1195666db24e25e23cc64bb1d70587aef9"
memory-comparison:
  version: 2
  scope: >-
    Retained wiki current state and History, live and archived hub routing,
    Access-Log, lint Dashboard, mutable configuration as an access structure,
    optional L1 rule bodies, descriptions and index, and their admission,
    maintenance, recovery and later-consumer routes. Includes unresolved initial
    L1 admission, external L1 payload selection and the conflicting claimed
    automatic re-promotion alternative. Setup is included as initialization of
    these structures, not as use-derived read-back. Excludes the shipped static
    skill and Schema conventions as memory payloads, external model weights,
    host session/compaction state and external UI implementation. These excluded
    host mechanisms are not classified as absent.
  axes:
    storage_substrate:
      assessment: known
      units:
        - scope: "Wiki current state and retained History"
          assessment: known
          findings:
            - value: files
              basis: claimed
              records: [memory.md#mem-obj-page-state, memory.md#mem-obj-page-history]
              note: "The maintained knowledge and superseded wording occupy Markdown pages in either supported vault format."
          records: [memory.md#mem-obj-page-state, memory.md#mem-obj-page-history]
          note: "Both current and historical parts have explicit filesystem identities; no actual vault contents are supplied."
        - scope: "Live Index, Archive, Access-Log and Dashboard"
          assessment: known
          findings:
            - value: files
              basis: claimed
              records: [memory.md#mem-obj-hub-index, memory.md#mem-obj-hub-archive, memory.md#mem-obj-access-log, memory.md#mem-obj-dashboard]
              note: "Selection metadata, read traces and health metrics persist in Markdown, not in an inspected graph or vector service."
          records: [memory.md#mem-obj-hub-index, memory.md#mem-obj-hub-archive, memory.md#mem-obj-access-log, memory.md#mem-obj-dashboard]
          note: "The records enumerate the retained access and feedback surfaces, including the archive rather than only preferred query inputs."
        - scope: "Configuration and initial wiki access/feedback skeleton"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-config, runtime.md#rt-rte-wiki-setup]
              note: "The initializer writes YAML configuration and Markdown skeleton files with existence guards."
          records: [memory.md#mem-obj-config, runtime.md#rt-rte-wiki-setup]
          note: "Executable initialization establishes substrate, not subsequent model compliance."
        - scope: "L1 rule files, descriptions and index"
          assessment: known
          findings:
            - value: files
              basis: claimed
              records: [memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
              note: "The target describes Markdown files in the configured memory directory; the external host's internal state is excluded."
          records: [memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
          note: "Missing initial contents and unknown host loading do not erase the declared file substrate."
        - scope: "Git retention and recovery for structural wiki changes"
          assessment: known
          findings:
            - value: repo
              basis: wired
              records: [runtime.md#rt-rte-wiki-setup]
              note: "Optional setup initializes Git and attempts a commit; failure can leave files uncommitted."
            - value: repo
              basis: claimed
              records: [runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-health-maintenance]
              note: "Structural maintenance commits afford persistent revision history and manual recovery, not transactional rollback."
          records: [runtime.md#rt-rte-wiki-setup, runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-health-maintenance]
          note: "Repo describes the optional revision layer, separate from Markdown file storage; L1 Git protection is not guaranteed."
      records: [memory.md#mem-obj-page-state, memory.md#mem-obj-page-history, memory.md#mem-obj-hub-index, memory.md#mem-obj-hub-archive, memory.md#mem-obj-access-log, memory.md#mem-obj-dashboard, memory.md#mem-obj-config, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index, runtime.md#rt-rte-wiki-setup]
      note: "The accepted inventory covers all included retained objects and the optional Git layer. Links and graph-shaped content do not establish a graph substrate."
    representational_form:
      assessment: partial
      units:
        - scope: "Wiki state, History and hub descriptions at query and maintenance consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-page-state, memory.md#mem-obj-page-history, memory.md#mem-obj-hub-index, memory.md#mem-obj-hub-archive]
              note: "The foreground model interprets knowledge, historical wording, descriptions, tags and links; markup alone does not establish fixed symbolic consumption."
          records: [memory.md#mem-obj-page-state, memory.md#mem-obj-page-history, memory.md#mem-obj-hub-index, memory.md#mem-obj-hub-archive]
          note: "The classified path is model-mediated consumption, not external UI link resolution or execution of code examples."
        - scope: "Access-Log, Dashboard and configuration at model-mediated later commands"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-access-log, memory.md#mem-obj-dashboard, memory.md#mem-obj-config]
              note: "Structured fields supply model-interpreted selection, recency and comparison inputs; the requested fixed-position log parsing is not an implemented target parser."
          records: [memory.md#mem-obj-access-log, memory.md#mem-obj-dashboard, memory.md#mem-obj-config]
          note: "Localized fields do not by themselves turn the prose-maintenance consumer into symbolic code."
        - scope: "Described L1 rules, descriptions and index lines"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
              note: "Rule bodies and descriptions state behavior claims/preferences; maintenance metadata is interpreted by the agent."
          records: [memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
          note: "The declared file surfaces are classified, not an assertion about every secret representation or provider payload."
        - scope: "Exact externally loaded L1 payload and any transformation before consumption"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-bap-l1-loading, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
          note: "The host implementation, actual contents and selected payload are not supplied; the readable file account cannot classify an opaque host transformation."
      records: [memory.md#mem-obj-page-state, memory.md#mem-obj-page-history, memory.md#mem-obj-hub-index, memory.md#mem-obj-hub-archive, memory.md#mem-obj-access-log, memory.md#mem-obj-dashboard, memory.md#mem-obj-config, memory.md#mem-bap-l1-loading]
      note: "Known model-mediated file-consumption forms coexist with an unresolved external L1 payload path. Fixed processing of setup inputs produces retained configuration but does not establish symbolic consumption of accumulated memory. No included record establishes retained distributed-parametric memory."
    lineage:
      assessment: partial
      units:
        - scope: "Source-derived wiki state from ingest and Markdown import"
          assessment: known
          findings:
            - value: imported
              basis: claimed
              records: [runtime.md#rt-rte-source-ingest, memory.md#mem-obj-page-state]
              note: "User URL/file/text and Markdown notes supply the acquired knowledge; extraction does not establish independently produced facts."
            - value: other-compiled
              basis: claimed
              records: [runtime.md#rt-rte-source-ingest, memory.md#mem-obj-page-state]
              note: "The model extracts, converts and redistributes source material into retained pages."
          records: [runtime.md#rt-rte-source-ingest, memory.md#mem-obj-page-state]
          note: "These are described derivation paths, not a universal fact-to-source proof or a reconstruction of actual vault provenance."
        - scope: "Query write-back and L1 carry-over summaries; retained old wording"
          assessment: known
          findings:
            - value: other-compiled
              basis: claimed
              records: [runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-l1-verification, memory.md#mem-obj-page-history]
              note: "Confirmed summaries compile prior pages or L1 material; History also preserves moved superseded wording without implying novel claims."
          records: [runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-l1-verification, memory.md#mem-obj-page-history]
          note: "The recorded transformations are known, but completeness of retained reasons is not."
        - scope: "Hub routing descriptions and lint Dashboard"
          assessment: known
          findings:
            - value: other-compiled
              basis: claimed
              records: [memory.md#mem-obj-hub-index, memory.md#mem-obj-hub-archive, memory.md#mem-obj-dashboard, runtime.md#rt-rte-health-maintenance]
              note: "Descriptions derive from page content/tags, archive lines move verbatim, and Dashboard metrics derive from lint checks."
          records: [memory.md#mem-obj-hub-index, memory.md#mem-obj-hub-archive, memory.md#mem-obj-dashboard, runtime.md#rt-rte-health-maintenance]
          note: "Import does not guarantee complete routing descriptions; derivation classification is not an assertion of a populated usable index."
        - scope: "Query-read Access-Log entries"
          assessment: known
          findings:
            - value: trace-extracted
              basis: claimed
              records: [memory.md#mem-obj-access-log, runtime.md#rt-rte-wiki-query]
              note: "The maintainer records actual full-page reads and short selector reasons, not complete conversational transcripts or independent outcomes."
          records: [memory.md#mem-obj-access-log, runtime.md#rt-rte-wiki-query]
          note: "The static bootstrap line is initialization, not an observed query trace."
        - scope: "Initialized configuration and wiki structure"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [runtime.md#rt-rte-wiki-setup, memory.md#mem-obj-config]
              note: "User-selected settings supply configured choices on the interactive paths."
            - value: other-compiled
              basis: wired
              records: [runtime.md#rt-rte-wiki-setup, memory.md#mem-obj-config]
              note: "The initializer renders templates and settings into retained access structures; this does not make static Schema use-derived memory."
          records: [runtime.md#rt-rte-wiki-setup, memory.md#mem-obj-config]
          note: "The direct initializer accepts generic caller flags; that does not resolve human admission on that path."
        - scope: "Subsequent approved L1 corrections and synchronized index text"
          assessment: known
          findings:
            - value: authored
              basis: claimed
              records: [runtime.md#rt-rte-l1-verification, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
              note: "The model proposes and the user approves corrected rule text and metadata; these are explicit subsequent revisions."
          records: [runtime.md#rt-rte-l1-verification, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
          note: "Known revisions do not supply initial rule provenance."
        - scope: "Initial L1 rules/index and exact externally loaded payload provenance"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index, memory.md#mem-bap-l1-loading]
          note: "Original files, initial authorship and host transformations are unavailable; imported, authored and trace-derived alternatives cannot be resolved for this part."
      records: [runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-wiki-setup, runtime.md#rt-rte-l1-verification, memory.md#mem-obj-page-history, memory.md#mem-obj-hub-index, memory.md#mem-obj-dashboard, memory.md#mem-obj-access-log, memory.md#mem-obj-l1-rules, memory.md#mem-bap-l1-loading]
      note: "The inventory retains both source acquisition and derived paths; unknown original L1 provenance prevents complete lineage coverage."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Wiki current/history content at later answer synthesis"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-bap-wiki-answer, memory.md#mem-obj-page-state, memory.md#mem-obj-page-history]
              note: "Requested page reads supply informational material for attributed answers; history is not necessarily examined as historical rationale."
          records: [memory.md#mem-bap-wiki-answer, memory.md#mem-obj-page-state, memory.md#mem-obj-page-history]
          note: "Information delivery is not instruction precedence, factual endorsement or demonstrated reliance."
        - scope: "Hub descriptions/tags and fallback page text at query selection"
          assessment: known
          findings:
            - value: ranking
              basis: claimed
              records: [memory.md#mem-obj-hub-index, runtime.md#rt-rte-wiki-query]
              note: "Retained descriptions/tags and grep-matched text influence the relative priority of pages to read."
          records: [memory.md#mem-obj-hub-index, runtime.md#rt-rte-wiki-query]
          note: "Live-index membership affects preferred selection; Archive is not an enforced read prohibition."
        - scope: "Configuration at later command dispatch and review scheduling"
          assessment: known
          findings:
            - value: routing
              basis: claimed
              records: [memory.md#mem-obj-config, runtime.md#rt-rte-l1-verification]
              note: "Paths/tool/namespaces select scope, and the verification interval determines which retained rules are due for review."
          records: [memory.md#mem-obj-config, runtime.md#rt-rte-l1-verification]
          note: "Due selection is not an action-time veto on stale rules."
        - scope: "Access traces, Archive lines and Dashboard at maintenance/status consumers"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-obj-access-log, memory.md#mem-obj-hub-archive, memory.md#mem-obj-dashboard, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-health-maintenance]
              note: "Recency/reasons inform proposals and hot/cold reports; archived lines support re-promotion, and Dashboard supports later status comparison."
          records: [memory.md#mem-obj-access-log, memory.md#mem-obj-hub-archive, memory.md#mem-obj-dashboard, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-health-maintenance]
          note: "Manual admission mediates durable pruning changes. Reporting use is not evidence of improved behavior or automatic learning authority."
        - scope: "L1 rule bodies/descriptions and index summaries at described later sessions"
          assessment: known
          findings:
            - value: instruction
              basis: afforded
              records: [memory.md#mem-bap-l1-loading, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
              note: "The documented external host consumer receives behavior-steering rules/preferences and summaries as standing context."
          records: [memory.md#mem-bap-l1-loading, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
          note: "This is an external consumer role, not inspected loading wiring or proof each body reaches every session."
        - scope: "L1 claims and verification metadata at requested rule review"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [runtime.md#rt-rte-l1-verification, memory.md#mem-obj-l1-rules]
              note: "Rule content supplies the claim under examination and retained dates/classes supply evidence for review scheduling."
            - value: routing
              basis: claimed
              records: [runtime.md#rt-rte-l1-verification, memory.md#mem-obj-l1-rules]
              note: "Class and verification age select claims to check, never-verified first and oldest next."
          records: [runtime.md#rt-rte-l1-verification, memory.md#mem-obj-l1-rules]
          note: "The rule under test is not itself the retained validation criterion, and a date is not an enforced freshness gate."
        - scope: "Unspecified L1 contents and exact host-selected payload effects"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index, memory.md#mem-bap-l1-loading]
          note: "Actual rule types, selected parts and host force beyond the described guidance role are unknown; credential references are not evidence of retained enforcement controls."
      records: [memory.md#mem-bap-wiki-answer, memory.md#mem-obj-hub-index, runtime.md#rt-rte-wiki-query, memory.md#mem-obj-config, memory.md#mem-obj-access-log, memory.md#mem-obj-hub-archive, memory.md#mem-obj-dashboard, memory.md#mem-bap-l1-loading, runtime.md#rt-rte-l1-verification]
      note: "Consumers establish local knowledge, ranking, routing and instruction forces. Static skill/Schema validation instructions are outside this accumulated-memory boundary; unresolved host effects remain included."
    write_agency:
      assessment: partial
      units:
        - scope: "Ingest/import, query access logging, lint repairs and Dashboard admission"
          assessment: known
          findings:
            - value: automatic
              basis: claimed
              records: [runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-health-maintenance]
              note: "The model admits derived facts, access records and authorized repairs/metrics without a separate human content decision; invoking ingest or --fix is not per-content approval."
          records: [runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-health-maintenance]
          note: "Automatic names the prescribed admission mechanism, not executable maintenance code or observed compliance."
        - scope: "Query knowledge write-back, skill re-promotion, L2 demotion and subsequent L1 edits/removal"
          assessment: known
          findings:
            - value: manual
              basis: claimed
              records: [runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-l1-verification]
              note: "Explicit user acceptance authorizes the proposed summary/page, archive move or per-item rule change."
          records: [runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-l1-verification]
          note: "Model authorship and tool I/O do not turn human-approved content admission into automatic admission."
        - scope: "README's conflicting automatic archived-page re-promotion alternative"
          assessment: known
          findings:
            - value: automatic
              basis: claimed
              records: [epistemic.md#epi-clm-automatic-repromotion]
              note: "README expressly claims automatic re-promotion on another query hit; the skill instead prescribes an offer. This is only a conflicting claim, not established wiring."
          records: [epistemic.md#epi-clm-automatic-repromotion, runtime.md#rt-rte-wiki-query]
          note: "The claimed alternative is retained separately so skill confirmation does not silently erase it."
        - scope: "Interactive configuration choices and installer-confirmed replacement"
          assessment: known
          findings:
            - value: manual
              basis: wired
              records: [runtime.md#rt-rte-wiki-setup, memory.md#mem-obj-config]
              note: "The wrappers collect explicit user settings, and the installer asks before removing an existing configuration."
          records: [runtime.md#rt-rte-wiki-setup, memory.md#mem-obj-config]
          note: "This classifies the operator's retained settings/replacement decision, not all generated template content as manually reviewed."
        - scope: "Initial generated skeleton content after setup settings"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-wiki-setup]
              note: "After settings are supplied, code renders/adopts missing template content using syntax/existence guards, without per-page content approval."
          records: [runtime.md#rt-rte-wiki-setup]
          note: "The software admission of generated structure is separate from manual configuration choice."
        - scope: "Direct initializer caller's settings admission"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-wiki-setup]
          note: "Caller-supplied flags are known but the generic direct caller is not identified as a human content decision."
        - scope: "Initial L1 rule/index admission"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
          note: "The initial authoring and admission controls were not supplied; later per-item confirmation cannot resolve them."
      records: [runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-l1-verification, runtime.md#rt-rte-health-maintenance, runtime.md#rt-rte-wiki-setup, epistemic.md#epi-clm-automatic-repromotion, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
      note: "Known manual and automatic mechanisms coexist with unresolved direct-caller settings and initial L1 control; the conflicting re-promotion claim stays at claimed strength."
    curation_operations:
      assessment: partial
      units:
        - scope: "Ingest current-state replacement and retained superseded History"
          assessment: known
          findings:
            - value: evolve
              basis: claimed
              records: [runtime.md#rt-rte-source-ingest, memory.md#mem-obj-page-history]
              note: "New superseding facts revise current headlines/properties/next steps in place."
            - value: invalidate
              basis: claimed
              records: [runtime.md#rt-rte-source-ingest, memory.md#mem-obj-page-history]
              note: "Superseded wording loses current-state reliance while remaining dated and readable in History."
          records: [runtime.md#rt-rte-source-ingest, memory.md#mem-obj-page-history]
          note: "These are prescribed semantic state transitions, not implemented independent curation algorithms."
        - scope: "Hub description production, proposed query summaries and L1 carry-over summaries"
          assessment: known
          findings:
            - value: consolidate
              basis: claimed
              records: [memory.md#mem-obj-hub-index, runtime.md#rt-rte-wiki-query, memory.md#mem-obj-page-history, runtime.md#rt-rte-l1-verification]
              note: "Existing page/rule material is compressed into routing descriptions or summaries; carry-over can drop information."
          records: [memory.md#mem-obj-hub-index, runtime.md#rt-rte-wiki-query, memory.md#mem-obj-page-history, runtime.md#rt-rte-l1-verification]
          note: "This classifies the stated compression function; no recorded non-entailed new claim establishes synthesize."
        - scope: "L2 archive demotion and optional archive re-promotion"
          assessment: known
          findings:
            - value: decay
              basis: claimed
              records: [runtime.md#rt-rte-index-prune, memory.md#mem-obj-hub-archive]
              note: "Cold pages lose live-index salience while files and archived routing lines remain available."
            - value: promote
              basis: claimed
              records: [runtime.md#rt-rte-wiki-query, epistemic.md#epi-clm-automatic-repromotion]
              note: "Re-promotion restores live-index salience; sources disagree about automatic versus user-confirmed admission, not the proposed transformation."
          records: [runtime.md#rt-rte-index-prune, memory.md#mem-obj-hub-archive, runtime.md#rt-rte-wiki-query, epistemic.md#epi-clm-automatic-repromotion]
          note: "Demotion is neither content deletion nor enforced access denial."
        - scope: "Subsequent L1 correction, demotion and deletion"
          assessment: known
          findings:
            - value: evolve
              basis: claimed
              records: [runtime.md#rt-rte-l1-verification, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
              note: "Approved corrections revise rule body, frontmatter description and index claim text together."
            - value: decay
              basis: claimed
              records: [runtime.md#rt-rte-l1-verification, memory.md#mem-obj-page-history]
              note: "Approved demotion reduces always-loaded guidance to on-demand L2 history; approved deletion forgets the rule and references."
            - value: invalidate
              basis: claimed
              records: [runtime.md#rt-rte-l1-verification, memory.md#mem-obj-page-history]
              note: "Demotion withdraws standing L1 reliance while retaining a carry-over history record; deletion alone is not historical invalidation."
          records: [runtime.md#rt-rte-l1-verification, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index, memory.md#mem-obj-page-history]
          note: "Per-item user admission is required; merely setting a verification date does not establish a new truth claim."
        - scope: "Lint confidence and content/routing repairs"
          assessment: known
          findings:
            - value: decay
              basis: claimed
              records: [runtime.md#rt-rte-health-maintenance]
              note: "High-to-stale confidence downgrade lowers retained confidence based on age, not factual refutation."
            - value: evolve
              basis: claimed
              records: [runtime.md#rt-rte-health-maintenance, memory.md#mem-obj-hub-index]
              note: "Repairs revise retained metadata, descriptions and links; acquisition and index creation alone are not counted as additional curation operations."
          records: [runtime.md#rt-rte-health-maintenance, memory.md#mem-obj-hub-index]
          note: "--fix permits model repairs but never L1 edits; no independent implementation or executed repair is supplied."
        - scope: "Unspecified semantic changes in answer gap-filling, extraction and initial L1 production"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-wiki-query, memory.md#mem-obj-l1-rules]
          note: "Actual inputs/outputs and initial L1 derivation are missing. Novel synthesis, deduplication or other operations beyond the described transformations cannot be decided from labels."
      records: [runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-l1-verification, runtime.md#rt-rte-health-maintenance, memory.md#mem-obj-hub-index, memory.md#mem-obj-page-history, epistemic.md#epi-clm-automatic-repromotion, memory.md#mem-obj-l1-rules]
      note: "Positive operations remain at doctrine strength. Unspecified semantic transformations and initial L1 production prevent a complete operation inventory; no dedup or synthesize value is inferred."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Requested wiki query, grep fallback and optional L1 reads within query"
          assessment: known
          findings:
            - value: pull
              basis: claimed
              records: [runtime.md#rt-rte-wiki-query, memory.md#mem-bap-wiki-answer]
              note: "The user's question requests retained material; model relevance selection and tool delivery fulfill that request rather than constituting an extra push."
          records: [runtime.md#rt-rte-wiki-query, memory.md#mem-bap-wiki-answer]
          note: "Hubs, full pages and fallback content belong to one request-driven chain."
        - scope: "Requested ingest, prune, L1 review, lint and status reads of accumulated state"
          assessment: known
          findings:
            - value: pull
              basis: claimed
              records: [runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-l1-verification, runtime.md#rt-rte-health-maintenance, memory.md#mem-obj-config]
              note: "A later maintenance invocation requests current/history pages, routing, access traces, rule files, config or prior Dashboard as needed."
          records: [runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-l1-verification, runtime.md#rt-rte-health-maintenance, memory.md#mem-obj-config]
          note: "External scheduling can request maintenance; it does not establish unsolicited context injection by the target."
        - scope: "Described automatic host L1 loading into later sessions"
          assessment: partial
          findings:
            - value: push
              basis: afforded
              records: [memory.md#mem-bap-l1-loading, memory.md#mem-obj-l1-index]
              note: "The documented host role supplies standing memory context without a contemporaneous request for those retained parts."
          records: [memory.md#mem-bap-l1-loading, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
          note: "Exact body/description/index delivery and host alternatives are unknown; no claim of deployed wiring or universal body loading follows."
      records: [runtime.md#rt-rte-wiki-query, memory.md#mem-bap-wiki-answer, runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-l1-verification, runtime.md#rt-rte-health-maintenance, memory.md#mem-bap-l1-loading]
      note: "Request-driven target routes and afforded external push coexist. Opaque host payload selection prevents complete direction coverage of the L1 branch."
    read_back_signal:
      assessment: partial
      units:
        - scope: "Wiki query and requested maintenance delivery chains"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-l1-verification, runtime.md#rt-rte-health-maintenance]
          note: "These assessed chains are pull: model relevance ranking, grep terms and requested file identifiers are not push signals."
        - scope: "Automatic L1 index availability at later session startup"
          assessment: known
          findings:
            - value: coarse
              basis: afforded
              records: [memory.md#mem-bap-l1-loading, memory.md#mem-obj-l1-index]
              note: "Trigger is a later session; selector input is the configured standing memory/index availability; selected retained part is index guidance described as auto-loaded. No question-specific identity match is established."
          records: [memory.md#mem-bap-l1-loading, memory.md#mem-obj-l1-index]
          note: "This classifies the documented broad index-loading role only, not exact host budgets or selection of rule bodies."
        - scope: "Automatic selection of L1 bodies/descriptions and intervening host payload processing"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-bap-l1-loading, memory.md#mem-obj-l1-rules]
          note: "Host selector inputs and actually delivered parts are unknown. File pointers and readable summaries alone cannot establish identifier, lexical, embedding or judgment-based push selection."
      records: [runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-l1-verification, runtime.md#rt-rte-health-maintenance, memory.md#mem-bap-l1-loading, memory.md#mem-obj-l1-index, memory.md#mem-obj-l1-rules]
      note: "Coarse index loading is afforded, while finer host selection remains unresolved. Known pull retrieval cannot make the whole signal axis inapplicable."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Specified Access-Log to L2 demotion and confirmed re-promotion route"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-access-log, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-wiki-query]
          note: "The specified durable change is human-gated and raw logging alone is insufficient. No canonical bounded-absence record establishes a controlled no finding; this route establishes no qualifying automatic update either."
        - scope: "Specified approved query summary write-back and L1 verification/demotion"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-l1-verification, memory.md#mem-obj-page-history]
          note: "Recorded content-specific human approval does not establish an automatic trace-fed write. A bounded-absence record is also missing, so manual revision is not converted into a controlled no finding."
        - scope: "Specified ingest/import and lint-derived routing/content repairs"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-health-maintenance, memory.md#mem-obj-hub-index, memory.md#mem-obj-dashboard]
          note: "Source/page processing and diagnostics do not establish a qualifying activity-trace-fed update. Actual source content is missing and there is no canonical bounded-absence record; neither yes nor no is established."
        - scope: "README automatic re-promotion alternative"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-clm-automatic-repromotion, runtime.md#rt-rte-wiki-query]
          note: "A conflicting automatic re-promotion claim names a query re-hit but supplies no separate accepted trace-fed write chain; whether this alternative meets the qualifying trace-input boundary remains unresolved."
        - scope: "Initial L1 production and external host alternatives"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index, memory.md#mem-bap-l1-loading]
          note: "Initial admission and inputs are unknown; excluded host compaction is not reclassified as absent, and no qualifying host update is established by loading alone."
      records: [memory.md#mem-obj-access-log, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-l1-verification, runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-health-maintenance, epistemic.md#epi-clm-automatic-repromotion, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
      note: "No qualifying automatic trace-fed chain or canonical bounded absence is established. Human-gated specified feedback routes, unresolved initial L1 production, possible source-trace content and the conflicting automatic re-promotion claim cannot establish a controlled yes or no."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Specified human-approved trace-feedback and summary/rule-update routes"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-access-log, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-l1-verification]
          note: "The described behavior-shaping writes require approval. Without canonical bounded absence of qualifying trace learning, source inapplicability is not asserted. Raw logs alone establish no learning-source value."
        - scope: "Recorded source/page ingest/import and lint transformations"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-health-maintenance, memory.md#mem-obj-hub-index, memory.md#mem-obj-dashboard]
          note: "The recorded inputs establish source/page processing and diagnostics, not a qualifying trace-learning chain or bounded absence. Arbitrary unprovided source contents remain unresolved."
        - scope: "Unresolved automatic re-promotion and initial L1 derivation inputs"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-clm-automatic-repromotion, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
          note: "No qualifying original input is specified well enough to classify session logs, tool traces, event streams or trajectories. Query activity alone does not establish a recorded multi-step trajectory."
      records: [memory.md#mem-obj-access-log, runtime.md#rt-rte-index-prune, runtime.md#rt-rte-wiki-query, runtime.md#rt-rte-l1-verification, runtime.md#rt-rte-source-ingest, runtime.md#rt-rte-health-maintenance, epistemic.md#epi-clm-automatic-repromotion, memory.md#mem-obj-l1-rules, memory.md#mem-obj-l1-index]
      note: "There is no supported positive source classification and no completely assessed bounded absence of qualifying trace learning. Missing inputs and unresolved alternatives prevent both controlled source values and inapplicability."
---

# llm-wiki memory profile

## Comparison rationale

This profile classifies the accepted records, not a running vault. The central
maintenance and query routes are model-consumed doctrine. Their findings remain
`claimed`; executable setup supports only its own `wired` findings. The external
L1 consumer role is `afforded`. No finding claims observed use or benefit.

The memory inventory separates current pages, historical wording, live and
archived routing, raw read traces, health metadata and L1 guidance. The
filesystem is the primary substrate. Optional Git commits add a revision and
recovery layer, not atomic admission. Model interpretation makes structured
Markdown fields natural-language material on those consumer paths. The
initializer's fixed processing consumes current setup inputs to produce retained
configuration; it does not establish a symbolic later-consumption path for that
retained configuration. The unsupported symbolic finding is withdrawn, not
retained under partial coverage. The exact external L1 payload remains unresolved.
See [MEM-OBJ-config](memory.md#mem-obj-config),
[MEM-OBJ-access-log](memory.md#mem-obj-access-log) and
[RT-RTE-wiki-setup](runtime.md#rt-rte-wiki-setup).

Retained page descriptions rank later candidates even without learned scoring
weights. Requested semantic selection remains pull, so it does not produce an
`inferred-judgment` push signal. The external host's described automatic index
loading supports coarse push at an afforded layer; unknown body/description
selection remains separate. Neither a page identifier nor an index pointer
proves targeted push. See [MEM-OBJ-hub-index](memory.md#mem-obj-hub-index),
[RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query) and
[MEM-BAP-l1-loading](memory.md#mem-bap-l1-loading).

Compression of existing material supports consolidation, not automatically
synthesis of a new claim. Query answer semantics remain indeterminate without
actual inputs and outputs. State replacement supports evolution and withdrawal
of current reliance with retained history. Archive demotion lowers salience;
it does not deny access. These distinctions follow
[MEM-OBJ-page-history](memory.md#mem-obj-page-history),
[RT-RTE-source-ingest](runtime.md#rt-rte-source-ingest),
[RT-RTE-index-prune](runtime.md#rt-rte-index-prune) and
[RT-RTE-wiki-query](runtime.md#rt-rte-wiki-query).

Automatic raw logging and human-approved index revision are different admission
mechanisms. The specified access-feedback chain therefore does not establish
an automatic trace-learning write. The README's contrary automatic re-promotion
claim remains a separate claimed agency alternative, not upgraded to wiring or
silently treated as the confirmed skill route. Its original trace input is not
specified as a qualifying learning chain in the records. Initial L1 provenance
and admission are also unresolved. These limits and the lack of canonical bounded-absence records prevent controlled
trace-learning negatives and trace-source inapplicability. See
[MEM-OBJ-access-log](memory.md#mem-obj-access-log),
[RT-RTE-index-prune](runtime.md#rt-rte-index-prune),
[EPI-CLM-automatic-repromotion](epistemic.md#epi-clm-automatic-repromotion) and
[MEM-OBJ-l1-rules](memory.md#mem-obj-l1-rules).

The reconciliation supersedes EPI-OBJ-access-log with
[MEM-OBJ-access-log](memory.md#mem-obj-access-log); only the canonical latter
record is used here. Its other object containers remain valid, but this profile
uses the finer memory parts where their consumers or coverage differ. No other
supersession changes a classification. Missing initial L1 control, exact host
payloads and actual semantic outputs remain limitations, not invitations to
reopen report verification.

No source files were read for this profile. All classifications use the supplied
accepted records and their annotations; no evidence or analyst record is added.
