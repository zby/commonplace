---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Stigmergy accumulated evidence, compiled wiki and retrieval/control memory at the frozen source boundary."
run-id: "AAS-2026-11-08-stigmergy-2de42cc04367-01"
source-identity: "https://github.com/sturlese/stigmergy"
reviewed-boundary: "0ca8bb1963ad9cf43eaf2c18329998023a9caa4f"
memory-comparison:
  version: 2
  scope: "Included: captured original/readable evidence, retained source/wiki content and metadata, contradiction payload/display, alias updates, fragments/vectors, Git/change recovery evidence, maintenance/withdrawal and replay/session control, plus unresolved operational ledger/roster surfaces named in accepted records. Excluded: static shipped code/instructions, ordinary transient plan/question state, remote inference parameters without a retained update route, external-host conversational memory and external service internals."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - 
          scope: "Source/wiki bodies, headers, contradiction payload/display and Git change history"
          assessment: "known"
          findings:
            - 
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source"
                - "memory.md#mem-obj-knowledge-body"
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-contradiction-data"
                - "memory.md#mem-obj-contradiction-display"
                - "memory.md#mem-obj-knowledge-changes"
              note: "Retained Markdown/YAML and change history are file-backed."
            - 
              value: "repo"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source"
                - "memory.md#mem-obj-knowledge-body"
                - "memory.md#mem-obj-knowledge-changes"
              note: "Tenant Git repository retains corpus revisions and publication history."
          records:
            - "memory.md#mem-obj-source"
            - "memory.md#mem-obj-knowledge-body"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-contradiction-data"
            - "memory.md#mem-obj-contradiction-display"
            - "memory.md#mem-obj-knowledge-changes"
          note: "These corpus parts have an explicit file/repository substrate."
        - 
          scope: "Original/readable evidence and compressed exact patch"
          assessment: "known"
          findings:
            - 
              value: "service-object"
              basis: "wired"
              records:
                - "memory.md#mem-obj-artifact"
                - "memory.md#mem-obj-knowledge-changes"
              note: "Private content-addressed evidence store has a remote S3 implementation."
            - 
              value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-artifact"
              note: "Exposed MemoryEvidenceStore alternative retains objects in process only, not durable across process loss."
          records:
            - "memory.md#mem-obj-artifact"
            - "memory.md#mem-obj-knowledge-changes"
          note: "Separate backing-store alternatives; in-process availability is not durability."
        - 
          scope: "Reader pages, fragments, metadata, vectors and change manifests"
          assessment: "known"
          findings:
            - 
              value: "rdbms"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-index-convergence"
                - "memory.md#mem-obj-fragment-vector"
                - "memory.md#mem-obj-knowledge-changes"
              note: "Postgres retains indexed corpus and knowledge_changes rows."
            - 
              value: "vector"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fragment-vector"
                - "runtime.md#rt-rte-index-convergence"
              note: "pgvector-backed fragment representations support similarity retrieval."
          records:
            - "runtime.md#rt-rte-index-convergence"
            - "memory.md#mem-obj-fragment"
            - "memory.md#mem-obj-fragment-vector"
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-knowledge-changes"
          note: "Vector indexing coexists with relational storage; it is not the remote embedding model's parameter store."
        - 
          scope: "Additional operational ledgers and roster/session state: storage"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-changes"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-rte-workspace-replay"
          note: "Included queue/audit/job/report/graph-measure and roster/session control surfaces are named but not fully recorded at operative-part and consumer level; complete coverage cannot be inferred from the principal corpus routes."
      records:
        - "memory.md#mem-obj-source"
        - "memory.md#mem-obj-knowledge-body"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-contradiction-data"
        - "memory.md#mem-obj-contradiction-display"
        - "memory.md#mem-obj-knowledge-changes"
        - "memory.md#mem-obj-artifact"
        - "runtime.md#rt-rte-index-convergence"
        - "memory.md#mem-obj-fragment"
        - "memory.md#mem-obj-fragment-vector"
        - "runtime.md#rt-rte-maintenance-admission"
        - "memory.md#mem-rte-workspace-replay"
      note: "Known corpus/evidence/index substrates coexist with incompletely described operational state. Remote inference parameters are excluded: no accumulated memory update to them is established."
    representational_form:
      assessment: "partial"
      units:
        - 
          scope: "Readable source/wiki/fragment content, conflict explanations and change reasons at model/human readers"
          assessment: "known"
          findings:
            - 
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source"
                - "memory.md#mem-obj-knowledge-body"
                - "memory.md#mem-obj-fragment"
                - "memory.md#mem-obj-contradiction-display"
                - "memory.md#mem-obj-knowledge-changes"
              note: "Text supplies assertions, explanations and audit reasons for interpretation."
          records:
            - "memory.md#mem-obj-source"
            - "memory.md#mem-obj-knowledge-body"
            - "memory.md#mem-obj-fragment"
            - "memory.md#mem-obj-contradiction-display"
            - "memory.md#mem-obj-knowledge-changes"
          note: "Covers readable parts, not their fixed-rule control fields."
        - 
          scope: "Headers, links, conflict serialization envelope, fragment addresses and change manifests at code consumers"
          assessment: "known"
          findings:
            - 
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-contradiction-data"
                - "memory.md#mem-obj-fragment"
                - "memory.md#mem-obj-knowledge-changes"
              note: "Localized IDs, ACLs, links, status, offsets and hashes have fixed parsing and consumer rules."
          records:
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-contradiction-data"
            - "memory.md#mem-obj-fragment"
            - "memory.md#mem-obj-knowledge-changes"
          note: "Natural-language claim values in contradiction payloads remain distinct from this envelope."
        - 
          scope: "Retained fragment embeddings"
          assessment: "known"
          findings:
            - 
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-fragment-vector"
              note: "Dense numerical representations supply similarity features; these are not updated provider weights."
          records:
            - "memory.md#mem-obj-fragment-vector"
          note: "Distributed numerical form is explicit for stored vectors."
        - 
          scope: "Original binary/document/image evidence before extraction"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-artifact"
          note: "Readable derivatives do not classify all original media encodings as natural-language or symbolic."
        - 
          scope: "Additional operational ledgers and roster/session state: form"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-changes"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-rte-workspace-replay"
          note: "Included queue/audit/job/report/graph-measure and roster/session control surfaces are named but not fully recorded at operative-part and consumer level; complete coverage cannot be inferred from the principal corpus routes."
      records:
        - "memory.md#mem-obj-source"
        - "memory.md#mem-obj-knowledge-body"
        - "memory.md#mem-obj-fragment"
        - "memory.md#mem-obj-contradiction-display"
        - "memory.md#mem-obj-knowledge-changes"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-contradiction-data"
        - "memory.md#mem-obj-fragment-vector"
        - "memory.md#mem-obj-artifact"
        - "runtime.md#rt-rte-maintenance-admission"
        - "memory.md#mem-rte-workspace-replay"
      note: "Mixed text/control/vector parts are split; opaque originals and additional state prevent complete form coverage."
    lineage:
      assessment: "partial"
      units:
        - 
          scope: "Acquired original material and replayed envelopes"
          assessment: "known"
          findings:
            - 
              value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-artifact"
                - "memory.md#mem-rte-workspace-replay"
              note: "External capture material enters retention; replay imports eligible captures into a new workspace."
          records:
            - "memory.md#mem-obj-artifact"
            - "memory.md#mem-rte-workspace-replay"
          note: "Imported is the admission lineage, not a claim of human authorship or original training provenance."
        - 
          scope: "Readable source, compiled wiki, contradiction views, aliases, fragment/vector index and change evidence"
          assessment: "known"
          findings:
            - 
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source"
                - "memory.md#mem-obj-knowledge-body"
                - "memory.md#mem-obj-contradiction-data"
                - "memory.md#mem-obj-contradiction-display"
                - "memory.md#mem-rte-alias-recording"
                - "memory.md#mem-obj-fragment"
                - "memory.md#mem-obj-fragment-vector"
                - "memory.md#mem-obj-knowledge-changes"
                - "runtime.md#rt-rte-index-convergence"
              note: "Extraction/rendering, model proposals, code projection, indexing and patch generation derive retained parts from supplied content or admitted changes."
          records:
            - "memory.md#mem-obj-source"
            - "memory.md#mem-obj-knowledge-body"
            - "memory.md#mem-obj-contradiction-data"
            - "memory.md#mem-obj-contradiction-display"
            - "memory.md#mem-rte-alias-recording"
            - "memory.md#mem-obj-fragment"
            - "memory.md#mem-obj-fragment-vector"
            - "memory.md#mem-obj-knowledge-changes"
            - "runtime.md#rt-rte-index-convergence"
          note: "Known derivation paths do not resolve original capture authorship or provider embedding provenance."
        - 
          scope: "Initial capture authorship and any upstream agent-experience derivation"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-artifact"
            - "runtime.md#rt-rte-capture-filing"
            - "memory.md#mem-rte-alias-recording"
          note: "Per-capture origin is unresolved. Neither authored nor trace-extracted lineage follows merely from adapter identity or use of a model."
        - 
          scope: "Additional operational ledgers and roster/session state: derivation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-changes"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-rte-workspace-replay"
          note: "Included queue/audit/job/report/graph-measure and roster/session control surfaces are named but not fully recorded at operative-part and consumer level; complete coverage cannot be inferred from the principal corpus routes."
      records:
        - "memory.md#mem-obj-artifact"
        - "memory.md#mem-rte-workspace-replay"
        - "memory.md#mem-obj-source"
        - "memory.md#mem-obj-knowledge-body"
        - "memory.md#mem-obj-contradiction-data"
        - "memory.md#mem-obj-contradiction-display"
        - "memory.md#mem-rte-alias-recording"
        - "memory.md#mem-obj-fragment"
        - "memory.md#mem-obj-fragment-vector"
        - "memory.md#mem-obj-knowledge-changes"
        - "runtime.md#rt-rte-index-convergence"
        - "runtime.md#rt-rte-capture-filing"
        - "runtime.md#rt-rte-maintenance-admission"
      note: "Supported import and compilation remain local; no blanket trace-extracted origin or complete initial-content lineage is established."
    behavioral_authority:
      assessment: "partial"
      units:
        - 
          scope: "Readable retained source/wiki/conflict/fragment text at later filing and answering"
          assessment: "known"
          findings:
            - 
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-source"
                - "memory.md#mem-obj-knowledge-body"
                - "memory.md#mem-obj-contradiction-display"
                - "memory.md#mem-rte-scoped-reading"
                - "runtime.md#rt-bap-corpus-data"
              note: "Selected content supplies evidence/context to planner, answer synthesizer and human readers, not standing host directions."
          records:
            - "memory.md#mem-obj-source"
            - "memory.md#mem-obj-knowledge-body"
            - "memory.md#mem-obj-contradiction-display"
            - "memory.md#mem-rte-scoped-reading"
            - "runtime.md#rt-bap-corpus-data"
          note: "Delivery and evidence force are wired; compliance and actual reliance are unobserved."
        - 
          scope: "Retained text, entity aliases and dense fragment features at relevance selectors"
          assessment: "known"
          findings:
            - 
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-metadata"
                - "memory.md#mem-obj-fragment-vector"
                - "memory.md#mem-rte-scoped-reading"
                - "runtime.md#rt-rte-capture-filing"
              note: "Names/aliases, lexical content, graph features and vectors influence candidate or retrieval priority."
          records:
            - "memory.md#mem-obj-page-metadata"
            - "memory.md#mem-obj-fragment-vector"
            - "memory.md#mem-rte-scoped-reading"
            - "runtime.md#rt-rte-capture-filing"
          note: "Fixed scoring still gives retained content ranking authority; no learned ranking policy is implied."
        - 
          scope: "Retained ACL, identity and source-reference metadata at filing/read gates"
          assessment: "known"
          findings:
            - 
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-metadata"
                - "runtime.md#rt-rte-capture-filing"
                - "memory.md#mem-rte-scoped-reading"
              note: "Access fields and current author authority permit or refuse delivery or writes."
            - 
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-page-metadata"
                - "epistemic.md#epi-rte-filing-check"
              note: "Retained source paths, identities and ACL relations supply admissibility criteria checked against proposed pages."
          records:
            - "memory.md#mem-obj-page-metadata"
            - "runtime.md#rt-rte-capture-filing"
            - "memory.md#mem-rte-scoped-reading"
            - "epistemic.md#epi-rte-filing-check"
          note: "Authority is at the actual gate, not a claim that metadata proves truth."
        - 
          scope: "Canonical contradiction records at preservation and named-resolution checks"
          assessment: "known"
          findings:
            - 
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-contradiction-data"
                - "epistemic.md#epi-rte-contradiction-disposition"
              note: "Existing records and IDs constrain admissible replacement/resolution."
            - 
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-contradiction-data"
                - "epistemic.md#epi-rte-contradiction-disposition"
              note: "Writer veto prevents prohibited rewriting or removal on capture mutation paths."
          records:
            - "memory.md#mem-obj-contradiction-data"
            - "epistemic.md#epi-rte-contradiction-disposition"
          note: "Capture-specific checks do not establish the same preservation invariant for garden."
        - 
          scope: "Operation-marked Git history/change records and replay session state at recovery/handover"
          assessment: "known"
          findings:
            - 
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-knowledge-changes"
                - "runtime.md#rt-rte-capture-filing"
                - "memory.md#mem-rte-workspace-replay"
              note: "Existing operation commit selects reconciliation instead of new planning; handover moves subsequent sessions/tokens to the target workspace."
          records:
            - "memory.md#mem-obj-knowledge-changes"
            - "runtime.md#rt-rte-capture-filing"
            - "memory.md#mem-rte-workspace-replay"
          note: "This is later operation selection, not semantic acceptance of the corpus."
        - 
          scope: "Additional operational ledgers and roster/session state: consumer force"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-changes"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-rte-workspace-replay"
          note: "Included queue/audit/job/report/graph-measure and roster/session control surfaces are named but not fully recorded at operative-part and consumer level; complete coverage cannot be inferred from the principal corpus routes."
      records:
        - "memory.md#mem-obj-source"
        - "memory.md#mem-obj-knowledge-body"
        - "memory.md#mem-obj-contradiction-display"
        - "memory.md#mem-rte-scoped-reading"
        - "runtime.md#rt-bap-corpus-data"
        - "memory.md#mem-obj-page-metadata"
        - "memory.md#mem-obj-fragment-vector"
        - "runtime.md#rt-rte-capture-filing"
        - "epistemic.md#epi-rte-filing-check"
        - "memory.md#mem-obj-contradiction-data"
        - "epistemic.md#epi-rte-contradiction-disposition"
        - "memory.md#mem-obj-knowledge-changes"
        - "memory.md#mem-rte-workspace-replay"
        - "runtime.md#rt-rte-maintenance-admission"
      note: "Knowledge, ranking, enforcement, validation and routing have specific consumers. Static packaged instructions and platform code are excluded from accumulated memory; no instruction or learning force is inferred just from corpus delivery."
    write_agency:
      assessment: "partial"
      units:
        - 
          scope: "Extraction, filing/projection, alias admission, garden/recompile output and index/change bookkeeping"
          assessment: "known"
          findings:
            - 
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-filing"
                - "runtime.md#rt-rte-maintenance-admission"
                - "memory.md#mem-rte-alias-recording"
                - "runtime.md#rt-rte-index-convergence"
                - "memory.md#mem-obj-knowledge-changes"
              note: "Software/model admission proceeds without a per-content human decision; initiating recompile does not approve its generated pages."
          records:
            - "runtime.md#rt-rte-capture-filing"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-rte-alias-recording"
            - "runtime.md#rt-rte-index-convergence"
            - "memory.md#mem-obj-knowledge-changes"
          note: "Physical write ownership and content authorship are not the admission criterion."
        - 
          scope: "Operator-confirmed replay import and handover"
          assessment: "known"
          findings:
            - 
              value: "manual"
              basis: "wired"
              records:
                - "memory.md#mem-rte-workspace-replay"
              note: "Explicit source:target confirmation and operator selection admit retained replay requests and session routing changes, not each downstream synthesized page."
          records:
            - "memory.md#mem-rte-workspace-replay"
          note: "Manual replay admission is distinct from automatic target compilation."
        - 
          scope: "Initial capture submission and explicit master entity/delete request control"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-artifact"
            - "runtime.md#rt-rte-layer-routing"
            - "epistemic.md#epi-rte-merge-check"
            - "runtime.md#rt-rte-maintenance-admission"
          note: "A person or external agent can supply requests; generic principal/master authorization does not establish human per-content approval for every admission."
        - 
          scope: "Additional operational ledgers and roster/session state: admission control"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-changes"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-rte-workspace-replay"
          note: "Included queue/audit/job/report/graph-measure and roster/session control surfaces are named but not fully recorded at operative-part and consumer level; complete coverage cannot be inferred from the principal corpus routes."
      records:
        - "runtime.md#rt-rte-capture-filing"
        - "runtime.md#rt-rte-maintenance-admission"
        - "memory.md#mem-rte-alias-recording"
        - "runtime.md#rt-rte-index-convergence"
        - "memory.md#mem-obj-knowledge-changes"
        - "memory.md#mem-rte-workspace-replay"
        - "memory.md#mem-obj-artifact"
        - "runtime.md#rt-rte-layer-routing"
        - "epistemic.md#epi-rte-merge-check"
      note: "Automatic compiled-content admissions and explicitly operator-confirmed replay are supported; caller identity leaves other admissions unresolved."
    curation_operations:
      assessment: "partial"
      units:
        - 
          scope: "Explicit evidence-backed entity merge"
          assessment: "known"
          findings:
            - 
              value: "consolidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-entity-merge"
              note: "Bodies, aliases and sources are combined under a canonical entity."
            - 
              value: "dedup"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-entity-merge"
              note: "Duplicate entity pages are removed and their links rewritten after the equivalence check."
          records:
            - "epistemic.md#epi-rte-entity-merge"
          note: "Concrete code transformation, not merely a command named merge."
        - 
          scope: "Ordinary wiki updates, alias metadata additions and accepted garden repairs"
          assessment: "known"
          findings:
            - 
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-knowledge-body"
                - "memory.md#mem-rte-alias-recording"
                - "runtime.md#rt-rte-maintenance-admission"
              note: "Existing entries/metadata are revised or extended for later use."
          records:
            - "memory.md#mem-obj-knowledge-body"
            - "memory.md#mem-rte-alias-recording"
            - "runtime.md#rt-rte-maintenance-admission"
          note: "This establishes revision capacity, not successful factual improvement."
        - 
          scope: "Explicit ordinary source/page withdrawal with retained Git history"
          assessment: "known"
          findings:
            - 
              value: "invalidate"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-evidence-withdrawal"
                - "runtime.md#rt-rte-maintenance-admission"
                - "memory.md#mem-obj-knowledge-changes"
              note: "Current managed reliance is withdrawn and dependent units removed; ordinary deletion retains history."
          records:
            - "epistemic.md#epi-rte-evidence-withdrawal"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-obj-knowledge-changes"
          note: "History-erasing purge is a separate destructive route and does not inherit this history-retention warrant."
        - 
          scope: "Semantic operation of source-to-wiki proposals and source-by-source recompilation"
          assessment: "not-determinable"
          findings: []
          records:
            - "epistemic.md#epi-rte-filing-transform"
            - "runtime.md#rt-rte-maintenance-admission"
          note: "Actual source/proposal pairs are absent; semantic preservation versus novel claims is unresolved. Filing names and requested synthesis do not establish synthesize or consolidation of every proposal."
        - 
          scope: "Additional operational ledgers and roster/session state: maintenance transformations"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-changes"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-rte-workspace-replay"
          note: "Included queue/audit/job/report/graph-measure and roster/session control surfaces are named but not fully recorded at operative-part and consumer level; complete coverage cannot be inferred from the principal corpus routes."
      records:
        - "epistemic.md#epi-rte-entity-merge"
        - "memory.md#mem-obj-knowledge-body"
        - "memory.md#mem-rte-alias-recording"
        - "runtime.md#rt-rte-maintenance-admission"
        - "epistemic.md#epi-rte-evidence-withdrawal"
        - "memory.md#mem-obj-knowledge-changes"
        - "epistemic.md#epi-rte-filing-transform"
        - "memory.md#mem-rte-workspace-replay"
      note: "Implemented merge, revision and history-preserving withdrawal support local operations; proposal semantics and incompletely recorded maintenance branches prevent exhaustive operation coverage."
    read_back_direction:
      assessment: "partial"
      units:
        - 
          scope: "Explicit search/read/list/describe, human views and model-requested evidence tools"
          assessment: "known"
          findings:
            - 
              value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-scoped-reading"
                - "runtime.md#rt-rte-scoped-answer"
              note: "Consumers request retained material; scoped service returns selected hits/pages/fragments."
          records:
            - "memory.md#mem-rte-scoped-reading"
            - "runtime.md#rt-rte-scoped-answer"
          note: "Returning a requested page is not an additional push."
        - 
          scope: "Automatic filing context selection and initial answer evidence search"
          assessment: "known"
          findings:
            - 
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-filing"
                - "runtime.md#rt-rte-scoped-answer"
              note: "On a new capture/plan or question, code selects and supplies existing corpus material before the model has requested those retained pages."
          records:
            - "runtime.md#rt-rte-capture-filing"
            - "runtime.md#rt-rte-scoped-answer"
          note: "Root workflows are request-driven, but automatic context injection within them is a separate operation from explicit memory requests."
        - 
          scope: "Additional operational ledgers and roster/session state: later delivery routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-changes"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-rte-workspace-replay"
          note: "Included queue/audit/job/report/graph-measure and roster/session control surfaces are named but not fully recorded at operative-part and consumer level; complete coverage cannot be inferred from the principal corpus routes."
      records:
        - "memory.md#mem-rte-scoped-reading"
        - "runtime.md#rt-rte-scoped-answer"
        - "runtime.md#rt-rte-capture-filing"
        - "memory.md#mem-obj-knowledge-changes"
        - "runtime.md#rt-rte-maintenance-admission"
        - "memory.md#mem-rte-workspace-replay"
      note: "Both explicit pull and automatic context supply are supported. Request-rooted workflow descriptions do not erase independent selection inside the chain."
    read_back_signal:
      assessment: "partial"
      units:
        - 
          scope: "Filing context supplied on capture/recompile planning"
          assessment: "known"
          findings:
            - 
              value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-filing"
                - "memory.md#mem-obj-page-metadata"
              note: "Named entity/project identity matches select delivered candidates; source references select retained evidence for expansion."
            - 
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-filing"
              note: "Source-text overlap ranks candidate bodies and cited source evidence."
            - 
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-filing"
              note: "Visible-layer availability, catalog inclusion and byte/candidate budgets delimit automatic context alongside targeted matching."
          records:
            - "runtime.md#rt-rte-capture-filing"
            - "memory.md#mem-obj-page-metadata"
          note: "Trigger is planning; selectors consume capture text, names, references and visibility/budget limits; selected parts are catalog, candidate bodies and source evidence. Nominal cap does not guarantee successful rendering."
        - 
          scope: "Initial answer search before model tool choice"
          assessment: "known"
          findings:
            - 
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-scoped-answer"
                - "memory.md#mem-rte-scoped-reading"
              note: "Question text feeds the initial scoped lexical retrieval."
            - 
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-scoped-answer"
                - "memory.md#mem-rte-scoped-reading"
                - "memory.md#mem-obj-fragment-vector"
              note: "Question embedding and stored fragment vectors contribute similarity selection in the service search."
            - 
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-scoped-reading"
                - "memory.md#mem-obj-page-metadata"
                - "runtime.md#rt-rte-scoped-answer"
              note: "Entity-name/alias matching contributes identity-targeted retrieval in the initial search chain."
            - 
              value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-scoped-reading"
                - "runtime.md#rt-rte-scoped-answer"
              note: "Tenant/audience visibility and bounded hit/excerpt budgets constrain the automatically supplied initial evidence."
          records:
            - "runtime.md#rt-rte-scoped-answer"
            - "memory.md#mem-rte-scoped-reading"
            - "memory.md#mem-obj-fragment-vector"
            - "memory.md#mem-obj-page-metadata"
          note: "Trigger is ask; code searches using the question and delivers bounded retained hits. Later explicitly requested tool retrieval remains pull rather than another push signal."
        - 
          scope: "Additional operational ledgers and roster/session state: automatic selectors"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-changes"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-rte-workspace-replay"
          note: "Included queue/audit/job/report/graph-measure and roster/session control surfaces are named but not fully recorded at operative-part and consumer level; complete coverage cannot be inferred from the principal corpus routes."
      records:
        - "runtime.md#rt-rte-capture-filing"
        - "memory.md#mem-obj-page-metadata"
        - "runtime.md#rt-rte-scoped-answer"
        - "memory.md#mem-rte-scoped-reading"
        - "memory.md#mem-obj-fragment-vector"
        - "memory.md#mem-obj-knowledge-changes"
        - "runtime.md#rt-rte-maintenance-admission"
        - "memory.md#mem-rte-workspace-replay"
      note: "Signals classify actual automatic context selection, not identifiers on requested files. No model-judgment push selector is established by the model's explicit tool requests."
    trace_learning:
      assessment: "not-determinable"
      units:
        - 
          scope: "Capture compilation and alias/garden/recompile derived-memory updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-artifact"
            - "runtime.md#rt-rte-capture-filing"
            - "memory.md#mem-rte-alias-recording"
            - "runtime.md#rt-rte-maintenance-admission"
            - "epistemic.md#epi-rte-filing-transform"
          note: "Automatic retained behavior-shaping outputs and later consumers are wired, but qualifying original trace inputs are unresolved. Captures may contain mixed human/agent material; derived link text alone does not establish trace-fed learning."
        - 
          scope: "Additional operational ledgers and roster/session state: possible trace-fed writes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-changes"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-rte-workspace-replay"
          note: "Included queue/audit/job/report/graph-measure and roster/session control surfaces are named but not fully recorded at operative-part and consumer level; complete coverage cannot be inferred from the principal corpus routes."
      records:
        - "memory.md#mem-obj-artifact"
        - "runtime.md#rt-rte-capture-filing"
        - "memory.md#mem-rte-alias-recording"
        - "runtime.md#rt-rte-maintenance-admission"
        - "epistemic.md#epi-rte-filing-transform"
        - "memory.md#mem-obj-knowledge-changes"
        - "memory.md#mem-rte-workspace-replay"
      note: "No accepted bounded-absence record licenses a local \"no\"; no identified qualifying original trace input licenses \"yes\". This is unresolved classification, not a negative learning claim."
    trace_source:
      assessment: "not-determinable"
      units:
        - 
          scope: "Original inputs of potentially trace-fed filing, alias and repair updates"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-artifact"
            - "runtime.md#rt-rte-capture-filing"
            - "memory.md#mem-rte-alias-recording"
            - "runtime.md#rt-rte-maintenance-admission"
          note: "Neither session-logs, tool-traces, event-streams nor trajectories are established as actual original inputs to a qualifying automatic write. Capture or queue serialization does not establish trace origin."
        - 
          scope: "Additional operational ledgers and roster/session state: possible trace origins"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-knowledge-changes"
            - "runtime.md#rt-rte-maintenance-admission"
            - "memory.md#mem-rte-workspace-replay"
          note: "Included queue/audit/job/report/graph-measure and roster/session control surfaces are named but not fully recorded at operative-part and consumer level; complete coverage cannot be inferred from the principal corpus routes."
      records:
        - "memory.md#mem-obj-artifact"
        - "runtime.md#rt-rte-capture-filing"
        - "memory.md#mem-rte-alias-recording"
        - "runtime.md#rt-rte-maintenance-admission"
        - "memory.md#mem-obj-knowledge-changes"
        - "memory.md#mem-rte-workspace-replay"
      note: "Qualifying trace learning is not completely assessed, so trace source is unresolved rather than inapplicable."
---

# Stigmergy memory profile

## Comparison rationale

This profile classifies accepted records, not a live tenant corpus. All positive findings are wired architectural mechanisms. No supplied execution or causal experiment supports observed activation, improvement, or causal benefit. Each partial axis preserves its unresolved included surfaces rather than treating an inspected corpus route as the whole inventory.

### Scope and operative parts

[MEM-OBJ-artifact](memory.md#mem-obj-artifact), [MEM-OBJ-source](memory.md#mem-obj-source), [MEM-OBJ-knowledge-body](memory.md#mem-obj-knowledge-body), [MEM-OBJ-page-metadata](memory.md#mem-obj-page-metadata), [MEM-OBJ-contradiction-data](memory.md#mem-obj-contradiction-data), [MEM-OBJ-contradiction-display](memory.md#mem-obj-contradiction-display), [MEM-OBJ-fragment](memory.md#mem-obj-fragment), [MEM-OBJ-fragment-vector](memory.md#mem-obj-fragment-vector) and [MEM-OBJ-knowledge-changes](memory.md#mem-obj-knowledge-changes) retain separate parts and consumers. Binary originals are not classified from readable extraction alone. The remote embedding producer is not the retained vector. The in-process evidence-store alternative is included without a durability claim.

Operational recovery state is included where retained commits/manifests determine later reconciliation, and replay/session state where it directs later consumers. The accepted records do not fully characterize audit/job/report/roster objects or every consumer, so these remain included unresolved units. Static librarian instructions and product release machinery are not accumulated memory merely because stored in the same source repository. Fresh per-question ledgers and draft plans are ordinary invocation state; their delivery does not establish a retained continuation summary.

### Agency, transformations and authority

[RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing), [RT-RTE-maintenance-admission](runtime.md#rt-rte-maintenance-admission) and [MEM-RTE-alias-recording](memory.md#mem-rte-alias-recording) establish automatic admission of derived content. A human starting maintenance does not manually approve its generated output. [MEM-RTE-workspace-replay](memory.md#mem-rte-workspace-replay) separately establishes operator-confirmed import/handover. Master authorization on other APIs does not establish that every caller is human.

[EPI-RTE-entity-merge](epistemic.md#epi-rte-entity-merge) supports consolidation and duplicate removal independently of unresolved proposal semantics in [EPI-RTE-filing-transform](epistemic.md#epi-rte-filing-transform). Neither a requested synthesis nor an unverified factual change establishes the controlled synthesis value. Ordinary withdrawal under [EPI-RTE-evidence-withdrawal](epistemic.md#epi-rte-evidence-withdrawal) invalidates current managed reliance while Git history remains; destructive history erasure has a different horizon. No decay or promotion mechanism is inferred from editorial status labels.

Corpus text supplies knowledge at the later planner/answer consumer. The same text, aliases and vectors supply ranking inputs at selectors. Metadata and canonical conflict payloads supply criteria and vetoes at code gates. These distinct paths do not make all corpus text standing instructions. Retention of mutation reasons in change manifests does not demonstrate an automatic later model reader or learning authority for those reasons.

### Requests, automatic selection and limits

[MEM-RTE-scoped-reading](memory.md#mem-rte-scoped-reading) establishes explicit pull routes. Within [RT-RTE-capture-filing](runtime.md#rt-rte-capture-filing) and [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer), code also supplies selected retained context before the model requests those pages. That operation is push even though an upstream capture or question triggered the enclosing workflow. Identity matches, lexical selection, vector similarity and coarse visibility/budget limits retain separate warrants; a requested page identifier is not itself evidence of targeted push.

The accepted memory annotation qualifies the filing route's nominal context cap: compact-size trimming can still fail indented rendering, and one candidate may survive while excess source evidence is removed. This prevents a guaranteed delivery-size or total-relevance conclusion, not classification of the automatic selectors. The answer records disagree about whether every passing citation quote was actually delivered earlier to the model. [EPI-RTE-answer-check](epistemic.md#epi-rte-answer-check) retains a refetched-head path; [RT-RTE-scoped-answer](runtime.md#rt-rte-scoped-answer) uses surfaced-content wording. No classification here requires snapshot identity or prior delivery of every passing quotation. Scoped retained-content supply and pull tools remain established by both accounts.

### Trace inventory and unions

The automatic write and later-consumer links do not resolve original trace input. [MEM-OBJ-artifact](memory.md#mem-obj-artifact), [MEM-RTE-alias-recording](memory.md#mem-rte-alias-recording) and [EPI-RTE-filing-transform](epistemic.md#epi-rte-filing-transform) leave mixed capture origins and concrete semantic transformations unresolved. Raw queue/audit/evaluation retention is not itself a qualifying trace-fed update. No accepted evidenced-absence declaration covers these alternatives. Therefore neither local trace-learning negative nor positive is established, and trace source is not inapplicable. The derived system union has no supported trace-learning value; this does not claim absent learning or absent improved capacity.

All classifications cite declaring records rather than new evidence. Reconciliation contains no supersessions affecting these values; valid containers and operative parts remain distinct. Its unresolved context-budget and quote-delivery disagreements are retained as limits above, not settled by choosing a stronger status.

### Source-read log

No frozen-source reads were made. The supplied records and their retained passages sufficed; no new records, evidence, quotes or report corrections were introduced.
