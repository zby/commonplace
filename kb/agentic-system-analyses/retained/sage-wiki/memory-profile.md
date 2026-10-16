---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Sage-wiki memory comparison of retained knowledge, access/control state and later-consumer routes at the frozen repository revision."
run-id: "AAS-2026-10-15-sage-wiki-cc43456fb833-01"
source-identity: "https://github.com/xoai/sage-wiki"
reviewed-boundary: "d3ef3a1346405c82eac01b4d7c493c94c1c59169"
memory-comparison:
  version: 2
  scope: "Accumulated source/capture files, summaries, articles, entries/chunks/vectors, ontology entities/relations/aliases, communities, lessons, retained answers/trust evidence, manifest and compile recovery state; changed installed prompts/configuration/skills; their admissions, maintenance and later consumers. Included unresolved alternatives: provider-native batch checkpoints, backend representations, deeper restored state, lint/evaluator retained artifacts and external lesson consumers identified in accepted records. Excludes shipped static defaults, ordinary invocation-local Q&A/map/reduce context, external provider-internal weights/state and enclosing-host history. Restore/pack routes are included only for retained material installed for later use, not all runtime storage or permissions."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        -
          scope: "Readable source, summary, concept, community and answer files; source/concept manifest"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-sources"
                - "memory.md#mem-obj-summaries"
                - "memory.md#mem-obj-articles"
                - "memory.md#mem-obj-communities"
                - "memory.md#mem-obj-pending-outputs"
                - "memory.md#mem-obj-manifest"
              note: "Markdown and the JSON manifest persist on the filesystem."
          records:
            - "memory.md#mem-obj-raw-sources"
            - "memory.md#mem-obj-summaries"
            - "memory.md#mem-obj-articles"
            - "memory.md#mem-obj-communities"
            - "memory.md#mem-obj-pending-outputs"
            - "memory.md#mem-obj-manifest"
          note: "Includes readable bodies and file metadata, not merely a search display."
        -
          scope: "Entry/chunk, ontology, alias, community, learning, output-trust and compile-item rows"
          assessment: "known"
          findings:
            -
              value: "rdbms"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entries"
                - "memory.md#mem-obj-entities"
                - "memory.md#mem-obj-relations"
                - "memory.md#mem-obj-entity-aliases"
                - "memory.md#mem-obj-communities"
                - "memory.md#mem-obj-learnings"
                - "memory.md#mem-obj-pending-outputs"
                - "runtime.md#rt-obj-compile-items"
              note: "Relational database rows retain content and control state."
          records:
            - "memory.md#mem-obj-entries"
            - "memory.md#mem-obj-entities"
            - "memory.md#mem-obj-relations"
            - "memory.md#mem-obj-entity-aliases"
            - "memory.md#mem-obj-communities"
            - "memory.md#mem-obj-learnings"
            - "memory.md#mem-obj-pending-outputs"
            - "runtime.md#rt-obj-compile-items"
          note: "Database objects are distinct from their markdown counterparts; backend parity is not asserted."
        -
          scope: "Inspected document/chunk embedding BLOBs"
          assessment: "known"
          findings:
            -
              value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vectors"
              note: "The retained float-array vectors are BLOBs in SQLite; numerical encoding is not a separate storage substrate."
          records:
            - "memory.md#mem-obj-vectors"
          note: "This unit covers the inspected SQLite vector path only."
        -
          scope: "Installed workspace prompt, skill and configuration changes"
          assessment: "known"
          findings:
            -
              value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-apply-pack"
                - "runtime.md#rt-obj-prompts"
                - "runtime.md#rt-obj-config"
              note: "Pack application and workspace overrides retain changed machinery in files."
          records:
            - "runtime.md#rt-rte-apply-pack"
            - "runtime.md#rt-obj-prompts"
            - "runtime.md#rt-obj-config"
          note: "Only installed or edited retained state is included, not the shipped embedded defaults or transient registry."
        -
          scope: "Provider-native batch checkpoints; ANN/mmap/PostgreSQL alternative representations; deeper restore and lint/evaluator artifacts"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-compile-sources"
            - "memory.md#mem-obj-vectors"
            - "runtime.md#rt-rte-hydrate-workspace"
            - "epistemic.md#epi-rte-style-check"
            - "epistemic.md#epi-rte-benchmark-judge"
          note: "Available records identify these alternatives without a complete object/substrate inventory. Remote restore copies known state but does not establish every remote operative representation."
      records:
        - "memory.md#mem-obj-raw-sources"
        - "memory.md#mem-obj-summaries"
        - "memory.md#mem-obj-articles"
        - "memory.md#mem-obj-communities"
        - "memory.md#mem-obj-pending-outputs"
        - "memory.md#mem-obj-manifest"
        - "memory.md#mem-obj-entries"
        - "memory.md#mem-obj-entities"
        - "memory.md#mem-obj-relations"
        - "memory.md#mem-obj-entity-aliases"
        - "memory.md#mem-obj-learnings"
        - "runtime.md#rt-obj-compile-items"
        - "memory.md#mem-obj-vectors"
        - "runtime.md#rt-rte-apply-pack"
        - "runtime.md#rt-obj-prompts"
        - "runtime.md#rt-obj-config"
        - "runtime.md#rt-rte-compile-sources"
        - "runtime.md#rt-rte-hydrate-workspace"
        - "epistemic.md#epi-rte-style-check"
        - "epistemic.md#epi-rte-benchmark-judge"
      note: "Known file, relational and SQLite parts coexist with incomplete checkpoint, backend and ancillary-artifact coverage. External provider weights and enclosing-host history are outside the retained-memory boundary."
    representational_form:
      assessment: "partial"
      units:
        -
          scope: "Source, summary, article, entity-definition, evidence-span, community, lesson and answer prose at text/model/display consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-sources"
                - "memory.md#mem-obj-summaries"
                - "memory.md#mem-obj-articles"
                - "memory.md#mem-obj-entities"
                - "memory.md#mem-obj-relations"
                - "memory.md#mem-obj-communities"
                - "memory.md#mem-obj-learnings"
                - "memory.md#mem-obj-pending-outputs"
              note: "Consumers interpret prose as source material, domain definitions, evidence, themes or lessons."
          records:
            - "memory.md#mem-obj-raw-sources"
            - "memory.md#mem-obj-summaries"
            - "memory.md#mem-obj-articles"
            - "memory.md#mem-obj-entities"
            - "memory.md#mem-obj-relations"
            - "memory.md#mem-obj-communities"
            - "memory.md#mem-obj-learnings"
            - "memory.md#mem-obj-pending-outputs"
          note: "Readable prose is separated from the controls stored beside it."
        -
          scope: "IDs, frontmatter, hashes, source associations, typed edges, validity, alias status, membership, queue and trust controls"
          assessment: "known"
          findings:
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-sources"
                - "memory.md#mem-obj-entries"
                - "memory.md#mem-obj-manifest"
                - "memory.md#mem-obj-entities"
                - "memory.md#mem-obj-relations"
                - "memory.md#mem-obj-entity-aliases"
                - "memory.md#mem-obj-communities"
                - "memory.md#mem-obj-pending-outputs"
                - "runtime.md#rt-obj-compile-items"
              note: "Localized fields are consumed by fixed matching, traversal, eligibility, cache and scheduling rules."
          records:
            - "memory.md#mem-obj-raw-sources"
            - "memory.md#mem-obj-entries"
            - "memory.md#mem-obj-manifest"
            - "memory.md#mem-obj-entities"
            - "memory.md#mem-obj-relations"
            - "memory.md#mem-obj-entity-aliases"
            - "memory.md#mem-obj-communities"
            - "memory.md#mem-obj-pending-outputs"
            - "runtime.md#rt-obj-compile-items"
          note: "Includes numerical confidence/quality fields used by fixed threshold rules, not as dense learned representations."
        -
          scope: "Stored dense embeddings at similarity-search consumers"
          assessment: "known"
          findings:
            -
              value: "parametric"
              basis: "wired"
              records:
                - "memory.md#mem-obj-vectors"
              note: "Dense float arrays supply distributed numerical similarity representations, not readable reasons."
          records:
            - "memory.md#mem-obj-vectors"
          note: "This does not classify or freeze the external embedding model weights."
        -
          scope: "Changed prompt/skill prose and installed configuration at future consumers"
          assessment: "known"
          findings:
            -
              value: "natural-language"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-apply-pack"
                - "runtime.md#rt-obj-prompts"
                - "runtime.md#rt-bap-generated-skill"
              note: "Installed guidance is interpreted by completion providers or a host that loads it."
            -
              value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-apply-pack"
                - "runtime.md#rt-obj-config"
              note: "Installed configuration fields select fixed operations and permissions."
          records:
            - "runtime.md#rt-rte-apply-pack"
            - "runtime.md#rt-obj-prompts"
            - "runtime.md#rt-obj-config"
            - "runtime.md#rt-bap-generated-skill"
          note: "Prose guidance and symbolic controls are separate operative parts even when installed together."
        -
          scope: "Batch checkpoint payloads and incompletely inventoried lint/evaluator/backend retained parts"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-compile-sources"
            - "epistemic.md#epi-rte-benchmark-judge"
            - "memory.md#mem-obj-vectors"
          note: "No consumed-payload inventory supports complete form classification of these included alternatives."
      records:
        - "memory.md#mem-obj-raw-sources"
        - "memory.md#mem-obj-summaries"
        - "memory.md#mem-obj-articles"
        - "memory.md#mem-obj-entities"
        - "memory.md#mem-obj-relations"
        - "memory.md#mem-obj-communities"
        - "memory.md#mem-obj-learnings"
        - "memory.md#mem-obj-pending-outputs"
        - "memory.md#mem-obj-entries"
        - "memory.md#mem-obj-manifest"
        - "memory.md#mem-obj-entity-aliases"
        - "runtime.md#rt-obj-compile-items"
        - "memory.md#mem-obj-vectors"
        - "runtime.md#rt-rte-apply-pack"
        - "runtime.md#rt-obj-prompts"
        - "runtime.md#rt-obj-config"
        - "runtime.md#rt-bap-generated-skill"
        - "runtime.md#rt-rte-compile-sources"
        - "epistemic.md#epi-rte-benchmark-judge"
      note: "Text, symbolic and dense numerical parts are positively identified. Opaque checkpoint and ancillary parts prevent complete coverage; display text cannot classify an unknown payload."
    lineage:
      assessment: "partial"
      units:
        -
          scope: "Caller-supplied source bytes, finished articles/summaries/lessons and externally supplied saved answers"
          assessment: "known"
          findings:
            -
              value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-obj-raw-sources"
                - "runtime.md#rt-rte-write-article"
                - "memory.md#mem-obj-learnings"
                - "memory.md#mem-obj-pending-outputs"
              note: "Caller-authored content is admitted as supplied; authored does not identify a human author."
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-source"
                - "runtime.md#rt-rte-write-article"
                - "memory.md#mem-obj-pending-outputs"
              note: "Existing external content enters through capture, direct writes or SaveAnswer."
          records:
            - "memory.md#mem-obj-raw-sources"
            - "runtime.md#rt-rte-capture-source"
            - "runtime.md#rt-rte-write-article"
            - "memory.md#mem-obj-learnings"
            - "memory.md#mem-obj-pending-outputs"
          note: "These are supported admission/derivation paths, not proof of the original provenance of every supplied sentence."
        -
          scope: "Compiler summaries/articles, capture decomposition, indexes, graph/community material and retained generated native answers"
          assessment: "known"
          findings:
            -
              value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-summaries"
                - "memory.md#mem-obj-articles"
                - "memory.md#mem-obj-entries"
                - "memory.md#mem-obj-vectors"
                - "memory.md#mem-obj-relations"
                - "memory.md#mem-obj-communities"
                - "runtime.md#rt-rte-capture-knowledge"
                - "runtime.md#rt-rte-query-answer"
              note: "Software/model transformations derive retained material from sources, other retained parts or retrieved context."
          records:
            - "memory.md#mem-obj-summaries"
            - "memory.md#mem-obj-articles"
            - "memory.md#mem-obj-entries"
            - "memory.md#mem-obj-vectors"
            - "memory.md#mem-obj-relations"
            - "memory.md#mem-obj-communities"
            - "runtime.md#rt-rte-capture-knowledge"
            - "runtime.md#rt-rte-query-answer"
          note: "Generic compilation is distinguished from the separately evidenced session-extraction route."
        -
          scope: "Scribe-produced ontology definitions and relations"
          assessment: "known"
          findings:
            -
              value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-scribe-session"
                - "memory.md#mem-obj-entities"
              note: "Filtered recorded user/assistant turns feed durable entity/definition/relationship extraction."
          records:
            - "runtime.md#rt-rte-scribe-session"
            - "memory.md#mem-obj-entities"
          note: "Other entity admissions do not inherit this lineage."
        -
          scope: "Installed packs and restored workspace generations"
          assessment: "known"
          findings:
            -
              value: "imported"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-apply-pack"
                - "runtime.md#rt-rte-hydrate-workspace"
              note: "Existing pack material or a selected retained generation is installed for future consumption."
          records:
            - "runtime.md#rt-rte-apply-pack"
            - "runtime.md#rt-rte-hydrate-workspace"
          note: "Copying preserves an import path, not the complete original authorship or derivation."
        -
          scope: "Original provenance of caller content, embedding-model identity and batch/ancillary artifacts"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-raw-sources"
            - "memory.md#mem-obj-learnings"
            - "memory.md#mem-obj-pending-outputs"
            - "memory.md#mem-obj-vectors"
            - "runtime.md#rt-rte-compile-sources"
          note: "Caller identity and model labels do not resolve initial provenance, immutable embedding identity or opaque batch derivation."
      records:
        - "memory.md#mem-obj-raw-sources"
        - "runtime.md#rt-rte-capture-source"
        - "runtime.md#rt-rte-write-article"
        - "memory.md#mem-obj-learnings"
        - "memory.md#mem-obj-pending-outputs"
        - "memory.md#mem-obj-summaries"
        - "memory.md#mem-obj-articles"
        - "memory.md#mem-obj-entries"
        - "memory.md#mem-obj-vectors"
        - "memory.md#mem-obj-relations"
        - "memory.md#mem-obj-communities"
        - "runtime.md#rt-rte-capture-knowledge"
        - "runtime.md#rt-rte-query-answer"
        - "runtime.md#rt-rte-scribe-session"
        - "memory.md#mem-obj-entities"
        - "runtime.md#rt-rte-apply-pack"
        - "runtime.md#rt-rte-hydrate-workspace"
        - "runtime.md#rt-rte-compile-sources"
      note: "Known authorship/import, generic compilation and session extraction are local paths, not a complete origin history for every object."
    behavioral_authority:
      assessment: "partial"
      units:
        -
          scope: "Retained prose, graph descriptions/evidence and community summaries supplied to answering, writing, traversal and review consumers"
          assessment: "known"
          findings:
            -
              value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-articles"
                - "memory.md#mem-obj-summaries"
                - "memory.md#mem-obj-entities"
                - "memory.md#mem-obj-relations"
                - "memory.md#mem-obj-communities"
                - "memory.md#mem-obj-pending-outputs"
                - "memory.md#mem-rte-graph-query"
                - "memory.md#mem-rte-global-query"
                - "runtime.md#rt-rte-search-wiki"
              note: "Later model/tool/display consumers receive reference content or evidence, not enforced truth."
          records:
            - "memory.md#mem-obj-articles"
            - "memory.md#mem-obj-summaries"
            - "memory.md#mem-obj-entities"
            - "memory.md#mem-obj-relations"
            - "memory.md#mem-obj-communities"
            - "memory.md#mem-obj-pending-outputs"
            - "memory.md#mem-rte-graph-query"
            - "memory.md#mem-rte-global-query"
            - "runtime.md#rt-rte-search-wiki"
          note: "Includes existing articles in later writing and stored answers at comparison consumers; delivered content need not activate real host behavior."
        -
          scope: "Entry/chunk text, vectors, entity aliases and persisted scores at retrieval/candidate-priority consumers"
          assessment: "known"
          findings:
            -
              value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entries"
                - "memory.md#mem-obj-vectors"
                - "memory.md#mem-rte-resolve-aliases"
                - "runtime.md#rt-obj-compile-items"
                - "epistemic.md#epi-rte-quality-score"
              note: "Retained text/vectors affect relative retrieval or blocking priority; stored quality affects later scheduling."
          records:
            - "memory.md#mem-obj-entries"
            - "memory.md#mem-obj-vectors"
            - "memory.md#mem-rte-resolve-aliases"
            - "runtime.md#rt-obj-compile-items"
            - "epistemic.md#epi-rte-quality-score"
          note: "Ranking input does not require a retained learned ranking policy."
        -
          scope: "Manifest/source hashes, queue/pass/lease state, community cache metadata and applied alias identities at later work selectors"
          assessment: "known"
          findings:
            -
              value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-manifest"
                - "runtime.md#rt-obj-compile-items"
                - "memory.md#mem-obj-summaries"
                - "memory.md#mem-obj-communities"
                - "memory.md#mem-obj-entity-aliases"
                - "memory.md#mem-rte-resolve-aliases"
              note: "Retained state selects changed work, summary reuse, summary regeneration or canonical identity/edge replay."
          records:
            - "memory.md#mem-obj-manifest"
            - "runtime.md#rt-obj-compile-items"
            - "memory.md#mem-obj-summaries"
            - "memory.md#mem-obj-communities"
            - "memory.md#mem-obj-entity-aliases"
            - "memory.md#mem-rte-resolve-aliases"
          note: "These controls route computation rather than supply ordinary prose advice."
        -
          scope: "Alias rejection/active status and output trust/confirmation/grounding/dependency state at admission and retrieval controls"
          assessment: "known"
          findings:
            -
              value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entity-aliases"
                - "memory.md#mem-rte-resolve-aliases"
                - "memory.md#mem-obj-pending-outputs"
                - "runtime.md#rt-rte-admit-output"
                - "epistemic.md#epi-rte-verify-promote"
              note: "Retained pair/status and score/confirmation criteria determine whether proposals or outputs are admissible."
            -
              value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-entity-aliases"
                - "memory.md#mem-rte-resolve-aliases"
                - "memory.md#mem-obj-pending-outputs"
                - "runtime.md#rt-rte-admit-output"
                - "epistemic.md#epi-rte-output-withdrawal"
              note: "Rejection guards veto alias proposals; participating retrieval predicates and deindexing exclude ineligible outputs."
          records:
            - "memory.md#mem-obj-entity-aliases"
            - "memory.md#mem-rte-resolve-aliases"
            - "memory.md#mem-obj-pending-outputs"
            - "runtime.md#rt-rte-admit-output"
            - "epistemic.md#epi-rte-verify-promote"
            - "epistemic.md#epi-rte-output-withdrawal"
          note: "Veto force is path-local: direct file reads and non-output admissions bypass output trust."
        -
          scope: "Recorded session text at automatic scribe update consumer"
          assessment: "known"
          findings:
            -
              value: "learning"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-scribe-session"
                - "memory.md#mem-obj-entities"
              note: "Experience text feeds a durable graph-content update with a wired later ontology-tool consumer."
          records:
            - "runtime.md#rt-rte-scribe-session"
            - "memory.md#mem-obj-entities"
          note: "Learning authority at the update is distinct from knowledge authority of the resulting definitions; no improved capacity is established."
        -
          scope: "Installed workspace prompt overrides at completion-provider consumers"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-apply-pack"
                - "runtime.md#rt-obj-prompts"
              note: "The implemented registry loads workspace overrides for later completion calls, where their bodies supply proposal guidance."
          records:
            - "runtime.md#rt-rte-apply-pack"
            - "runtime.md#rt-obj-prompts"
          note: "Override loading and the internal completion-consumer path are wired; model compliance and observed activation are not established."
        -
          scope: "Generated or installed standing guidance at external host consumers"
          assessment: "known"
          findings:
            -
              value: "instruction"
              basis: "afforded"
              records:
                - "runtime.md#rt-bap-generated-skill"
                - "runtime.md#rt-rte-apply-pack"
              note: "Retained directions are written into host instruction files or installed as skills for a host that loads them; instruction force is conditional on that external loading contract."
          records:
            - "runtime.md#rt-bap-generated-skill"
            - "runtime.md#rt-rte-apply-pack"
          note: "The conditional instruction path is classified as afforded, not wired. File installation is implemented, but actual host loading, precedence, reload and compliance remain unestablished."
        -
          scope: "Stored learning entries at hypothetical external consumers; opaque batch and full lint/evaluator feedback consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-learnings"
            - "runtime.md#rt-rte-compile-sources"
            - "epistemic.md#epi-rte-benchmark-judge"
          note: "No native lesson-to-article delivery is established. A template slot or retained benchmark result does not establish instruction or learning force."
      records:
        - "memory.md#mem-obj-articles"
        - "memory.md#mem-obj-summaries"
        - "memory.md#mem-obj-entities"
        - "memory.md#mem-obj-relations"
        - "memory.md#mem-obj-communities"
        - "memory.md#mem-obj-pending-outputs"
        - "memory.md#mem-rte-graph-query"
        - "memory.md#mem-rte-global-query"
        - "runtime.md#rt-rte-search-wiki"
        - "memory.md#mem-obj-entries"
        - "memory.md#mem-obj-vectors"
        - "memory.md#mem-rte-resolve-aliases"
        - "runtime.md#rt-obj-compile-items"
        - "epistemic.md#epi-rte-quality-score"
        - "memory.md#mem-obj-manifest"
        - "memory.md#mem-obj-entity-aliases"
        - "runtime.md#rt-rte-admit-output"
        - "epistemic.md#epi-rte-verify-promote"
        - "epistemic.md#epi-rte-output-withdrawal"
        - "runtime.md#rt-rte-scribe-session"
        - "runtime.md#rt-rte-apply-pack"
        - "runtime.md#rt-obj-prompts"
        - "runtime.md#rt-bap-generated-skill"
        - "memory.md#mem-obj-learnings"
        - "runtime.md#rt-rte-compile-sources"
        - "epistemic.md#epi-rte-benchmark-judge"
      note: "Actual content and control consumers support seven local forces. Unwired lesson delivery and incomplete checkpoint/ancillary consumers prevent a complete authority inventory."
    write_agency:
      assessment: "partial"
      units:
        -
          scope: "Model capture, standard compile/curation/quality rewrite, scribe, community and automatic trust admissions"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-capture-knowledge"
                - "runtime.md#rt-rte-compile-sources"
                - "runtime.md#rt-rte-scribe-session"
                - "memory.md#mem-rte-resolve-aliases"
                - "epistemic.md#epi-rte-community-summary"
                - "runtime.md#rt-rte-admit-output"
                - "epistemic.md#epi-rte-verify-promote"
              note: "Models propose and software admits without a per-content human decision; workflow initiation does not make these admissions manual."
          records:
            - "runtime.md#rt-rte-capture-knowledge"
            - "runtime.md#rt-rte-compile-sources"
            - "runtime.md#rt-rte-scribe-session"
            - "memory.md#mem-rte-resolve-aliases"
            - "epistemic.md#epi-rte-community-summary"
            - "runtime.md#rt-rte-admit-output"
            - "epistemic.md#epi-rte-verify-promote"
          note: "Includes automatic alias application and promotion when their configured conditions hold."
        -
          scope: "Program-selected metadata repairs and source/age/validity-driven maintenance"
          assessment: "known"
          findings:
            -
              value: "automatic"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-style-fix"
                - "epistemic.md#epi-rte-edge-supersession"
                - "epistemic.md#epi-rte-output-withdrawal"
              note: "After activation, code determines the changed metadata, edge validity or withdrawal without per-entry approval."
          records:
            - "epistemic.md#epi-rte-style-fix"
            - "epistemic.md#epi-rte-edge-supersession"
            - "epistemic.md#epi-rte-output-withdrawal"
          note: "An explicit request to run repair/cleanup is not approval of each retained edit."
        -
          scope: "Caller-authored captures/direct writes/lessons, explicit alias/output decisions, pack/config editing and restore selection"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-capture-source"
            - "runtime.md#rt-rte-write-article"
            - "memory.md#mem-obj-learnings"
            - "memory.md#mem-rte-resolve-aliases"
            - "runtime.md#rt-rte-admit-output"
            - "runtime.md#rt-rte-apply-pack"
            - "runtime.md#rt-rte-hydrate-workspace"
            - "runtime.md#rt-obj-config"
          note: "Generic caller may be human or computational. Records do not establish a per-content human decision, so neither manual nor automatic admission is assigned to these caller-controlled branches."
        -
          scope: "Provider-native batch checkpoint admission and full ancillary-artifact write paths"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-compile-sources"
            - "epistemic.md#epi-rte-benchmark-judge"
          note: "The inspected standard path does not classify all alternative checkpoint or evaluator/lint admissions."
      records:
        - "runtime.md#rt-rte-capture-knowledge"
        - "runtime.md#rt-rte-compile-sources"
        - "runtime.md#rt-rte-scribe-session"
        - "memory.md#mem-rte-resolve-aliases"
        - "epistemic.md#epi-rte-community-summary"
        - "runtime.md#rt-rte-admit-output"
        - "epistemic.md#epi-rte-verify-promote"
        - "epistemic.md#epi-rte-style-fix"
        - "epistemic.md#epi-rte-edge-supersession"
        - "epistemic.md#epi-rte-output-withdrawal"
        - "runtime.md#rt-rte-capture-source"
        - "runtime.md#rt-rte-write-article"
        - "memory.md#mem-obj-learnings"
        - "runtime.md#rt-rte-apply-pack"
        - "runtime.md#rt-rte-hydrate-workspace"
        - "runtime.md#rt-obj-config"
        - "epistemic.md#epi-rte-benchmark-judge"
      note: "Automatic admission is wired on specified computational routes. Caller identity and uninspected alternatives prevent a complete agency classification; no manual value is inferred from a command name."
    curation_operations:
      assessment: "partial"
      units:
        -
          scope: "Reusable summary production and scribe fact extraction over recorded session content"
          assessment: "known"
          findings:
            -
              value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-summaries"
                - "runtime.md#rt-rte-scribe-session"
                - "memory.md#mem-obj-entities"
              note: "Summaries reduce source accounts; scribe selects standing domain definitions from recorded turns for later use."
          records:
            - "memory.md#mem-obj-summaries"
            - "runtime.md#rt-rte-scribe-session"
            - "memory.md#mem-obj-entities"
          note: "This structural reduction does not guarantee semantic faithfulness or turn a defect into synthesis."
        -
          scope: "Concept folding, alias identity consolidation and learning-entry content-hash deduplication"
          assessment: "known"
          findings:
            -
              value: "dedup"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-compile-sources"
                - "memory.md#mem-obj-manifest"
                - "memory.md#mem-rte-resolve-aliases"
                - "memory.md#mem-obj-learnings"
              note: "Near-duplicate concepts/identities are folded or linked; identical lesson content is suppressed by content hash."
          records:
            - "runtime.md#rt-rte-compile-sources"
            - "memory.md#mem-obj-manifest"
            - "memory.md#mem-rte-resolve-aliases"
            - "memory.md#mem-obj-learnings"
          note: "Deduplication concerns retained/consolidated knowledge, not merely a primary-key collision or index rebuild."
        -
          scope: "Existing article updates, differing scribe definitions and explicit caller replacements"
          assessment: "known"
          findings:
            -
              value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-obj-articles"
                - "runtime.md#rt-rte-scribe-session"
                - "runtime.md#rt-rte-write-article"
              note: "These mechanisms revise an existing retained entry rather than only add new storage."
          records:
            - "memory.md#mem-obj-articles"
            - "runtime.md#rt-rte-scribe-session"
            - "runtime.md#rt-rte-write-article"
          note: "Revision can discard old content or rationale; no improvement or complete rollback follows."
        -
          scope: "Temporal graph supersession, source-change output demotion and rejected/unlinked aliases"
          assessment: "known"
          findings:
            -
              value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-obj-relations"
                - "epistemic.md#epi-rte-edge-supersession"
                - "memory.md#mem-obj-pending-outputs"
                - "epistemic.md#epi-rte-output-withdrawal"
                - "memory.md#mem-rte-resolve-aliases"
              note: "Validity/state changes withdraw current reliance while retaining historical edges, stale records or rejected-pair history."
          records:
            - "memory.md#mem-obj-relations"
            - "epistemic.md#epi-rte-edge-supersession"
            - "memory.md#mem-obj-pending-outputs"
            - "epistemic.md#epi-rte-output-withdrawal"
            - "memory.md#mem-rte-resolve-aliases"
          note: "Separate deletion/rejection branches need not retain history and are not relabeled as invalidation."
        -
          scope: "Output trust promotion"
          assessment: "known"
          findings:
            -
              value: "promote"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-admit-output"
                - "epistemic.md#epi-rte-verify-promote"
              note: "Promotion raises a retained answer into eligible/indexed reuse under the configured policy."
          records:
            - "runtime.md#rt-rte-admit-output"
            - "epistemic.md#epi-rte-verify-promote"
          note: "Output promotion is distinct from advancing a source compile tier."
        -
          scope: "Learning-store age/count prune capability"
          assessment: "known"
          findings:
            -
              value: "decay"
              basis: "wired"
              records:
                - "memory.md#mem-obj-learnings"
              note: "Prune removes lessons older than 180 days and oldest excess over 500."
          records:
            - "memory.md#mem-obj-learnings"
          note: "Transformation capability is implemented, but no scheduled production caller is established."
        -
          scope: "Semantic novelty of model article/capture/community production and full batch/backend/lint maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-compile-sources"
            - "runtime.md#rt-rte-capture-knowledge"
            - "epistemic.md#epi-rte-community-summary"
            - "epistemic.md#epi-rte-article-cleanup"
            - "memory.md#mem-obj-learnings"
          note: "Generic generation and requested themes do not establish creation of a claim absent from inputs. Synthesize remains unresolved, as do the complete operations on opaque alternatives."
      records:
        - "memory.md#mem-obj-summaries"
        - "runtime.md#rt-rte-scribe-session"
        - "memory.md#mem-obj-entities"
        - "runtime.md#rt-rte-compile-sources"
        - "memory.md#mem-obj-manifest"
        - "memory.md#mem-rte-resolve-aliases"
        - "memory.md#mem-obj-learnings"
        - "memory.md#mem-obj-articles"
        - "runtime.md#rt-rte-write-article"
        - "memory.md#mem-obj-relations"
        - "epistemic.md#epi-rte-edge-supersession"
        - "memory.md#mem-obj-pending-outputs"
        - "epistemic.md#epi-rte-output-withdrawal"
        - "runtime.md#rt-rte-admit-output"
        - "epistemic.md#epi-rte-verify-promote"
        - "runtime.md#rt-rte-capture-knowledge"
        - "epistemic.md#epi-rte-community-summary"
        - "epistemic.md#epi-rte-article-cleanup"
      note: "Consolidate, dedup, evolve, invalidate, promote and decay have distinct local mechanisms. Indexing or mere acquisition establishes none; semantic novelty and complete alternative maintenance remain unresolved."
    read_back_direction:
      assessment: "partial"
      units:
        -
          scope: "Requested search/full read/ontology traversal, document answering and local/global graph answering"
          assessment: "known"
          findings:
            -
              value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-search-wiki"
                - "runtime.md#rt-rte-query-answer"
                - "memory.md#mem-rte-graph-query"
                - "memory.md#mem-rte-global-query"
                - "memory.md#mem-obj-entities"
              note: "A consumer requests retained material or an answer; software selection and delivery fulfill that request."
          records:
            - "runtime.md#rt-rte-search-wiki"
            - "runtime.md#rt-rte-query-answer"
            - "memory.md#mem-rte-graph-query"
            - "memory.md#mem-rte-global-query"
            - "memory.md#mem-obj-entities"
          note: "Graph expansion and community selection inside requested answering do not by themselves add an unsolicited push."
        -
          scope: "Automatic compile/resume selection of retained summaries, existing articles and relevant source sections into independent completion calls"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-compile-sources"
                - "memory.md#mem-obj-summaries"
                - "memory.md#mem-obj-articles"
                - "memory.md#mem-obj-manifest"
              note: "Compilation/resumption code supplies saved summaries, existing article prose and selected source material without the receiving completion requesting them."
          records:
            - "runtime.md#rt-rte-compile-sources"
            - "memory.md#mem-obj-summaries"
            - "memory.md#mem-obj-articles"
            - "memory.md#mem-obj-manifest"
          note: "The upstream operator may start compile; the later extraction/writer completion is automatically supplied selected memory."
        -
          scope: "Automatic maintenance reuse of alias decisions, output evidence and queue/cache state"
          assessment: "known"
          findings:
            -
              value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-resolve-aliases"
                - "memory.md#mem-obj-entity-aliases"
                - "memory.md#mem-obj-pending-outputs"
                - "runtime.md#rt-rte-admit-output"
                - "runtime.md#rt-obj-compile-items"
                - "memory.md#mem-obj-communities"
              note: "Later resolver, trust and scheduler invocations automatically consult retained decisions/evidence/state when their triggers fire."
          records:
            - "memory.md#mem-rte-resolve-aliases"
            - "memory.md#mem-obj-entity-aliases"
            - "memory.md#mem-obj-pending-outputs"
            - "runtime.md#rt-rte-admit-output"
            - "runtime.md#rt-obj-compile-items"
            - "memory.md#mem-obj-communities"
          note: "These internal software consumers count separately from the requested return to an external host."
        -
          scope: "Learning recall external use, batch checkpoint reload and incompletely traced lint/evaluator/restored consumers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-learnings"
            - "runtime.md#rt-rte-compile-sources"
            - "runtime.md#rt-rte-hydrate-workspace"
            - "epistemic.md#epi-rte-benchmark-judge"
          note: "Library recall and restoration capabilities do not resolve every actual later consumer or direction."
      records:
        - "runtime.md#rt-rte-search-wiki"
        - "runtime.md#rt-rte-query-answer"
        - "memory.md#mem-rte-graph-query"
        - "memory.md#mem-rte-global-query"
        - "memory.md#mem-obj-entities"
        - "runtime.md#rt-rte-compile-sources"
        - "memory.md#mem-obj-summaries"
        - "memory.md#mem-obj-articles"
        - "memory.md#mem-obj-manifest"
        - "memory.md#mem-rte-resolve-aliases"
        - "memory.md#mem-obj-entity-aliases"
        - "memory.md#mem-obj-pending-outputs"
        - "runtime.md#rt-rte-admit-output"
        - "runtime.md#rt-obj-compile-items"
        - "memory.md#mem-obj-communities"
        - "memory.md#mem-obj-learnings"
        - "runtime.md#rt-rte-hydrate-workspace"
        - "epistemic.md#epi-rte-benchmark-judge"
      note: "Requested external/answer routes are pull; automatically supplied compile and maintenance inputs are push at their own consumer boundary. Unknown alternatives prevent a pull-only or complete-direction conclusion."
    read_back_signal:
      assessment: "partial"
      units:
        -
          scope: "Compile/resume saved-summary and existing-article injection"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-summaries"
                - "memory.md#mem-obj-articles"
                - "runtime.md#rt-rte-compile-sources"
              note: "Compile/resume trigger matches source hash/path for saved summary reuse and concept identity/path for loading an existing article into a later completion."
          records:
            - "memory.md#mem-obj-summaries"
            - "memory.md#mem-obj-articles"
            - "runtime.md#rt-rte-compile-sources"
          note: "Actual matched retained bodies are delivered, not merely an ID displayed in a catalog."
        -
          scope: "Compiler source-section supply to article-writing completion"
          assessment: "known"
          findings:
            -
              value: "inferred-lexical"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-compile-sources"
                - "memory.md#mem-obj-articles"
              note: "Writer preparation matches concept/formatted name/aliases to retained source sections, ranks relevance and supplies bounded selected text."
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-compile-sources"
              note: "When no section matches, first-section fallback still supplies retained source text; part-size and budget rules are coarse filters."
          records:
            - "runtime.md#rt-rte-compile-sources"
            - "memory.md#mem-obj-articles"
          note: "Trigger is article preparation; selector inputs are concept names/aliases and source text; selected parts are the source sections, separate from the whole existing article."
        -
          scope: "Alias replay and candidate arbitration using retained decisions"
          assessment: "known"
          findings:
            -
              value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-resolve-aliases"
                - "memory.md#mem-obj-entity-aliases"
              note: "Resolution/replay matches alias/canonical identity pairs and active/rejected status to select retained decisions governing canonical lookup and edge replay."
          records:
            - "memory.md#mem-rte-resolve-aliases"
            - "memory.md#mem-obj-entity-aliases"
          note: "Compile-end/re-extract triggers maintenance; pair identity selects relevant retained decision state. Retained reason prose is not interpreted by the rejection selector."
        -
          scope: "Recurring-answer trust comparison"
          assessment: "known"
          findings:
            -
              value: "inferred-embedding"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-admit-output"
                - "epistemic.md#epi-rte-answer-agreement"
                - "memory.md#mem-obj-pending-outputs"
              note: "New answer filing triggers similar-question cosine selection of an earlier retained answer for comparison."
          records:
            - "runtime.md#rt-rte-admit-output"
            - "epistemic.md#epi-rte-answer-agreement"
            - "memory.md#mem-obj-pending-outputs"
          note: "The retained answer is selected by question embedding similarity, not by the subsequent answer-agreement judgment."
        -
          scope: "Automatic queue/cache/state filtering"
          assessment: "known"
          findings:
            -
              value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-compile-items"
                - "memory.md#mem-obj-communities"
                - "runtime.md#rt-rte-compile-sources"
              note: "Worker scans and compile maintenance use eligibility, tier, lease, membership/hash/model and availability conditions to choose retained work/cache state."
          records:
            - "runtime.md#rt-obj-compile-items"
            - "memory.md#mem-obj-communities"
            - "runtime.md#rt-rte-compile-sources"
          note: "These are coarse lifecycle filters, not proof of semantic targeting or exact content freshness."
        -
          scope: "Batch checkpoint selection and hypothetical learning/lint/evaluator push branches"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-compile-sources"
            - "memory.md#mem-obj-learnings"
            - "epistemic.md#epi-rte-benchmark-judge"
          note: "Accepted records do not enumerate selector inputs and delivered payloads for these alternatives."
      records:
        - "memory.md#mem-obj-summaries"
        - "memory.md#mem-obj-articles"
        - "runtime.md#rt-rte-compile-sources"
        - "memory.md#mem-rte-resolve-aliases"
        - "memory.md#mem-obj-entity-aliases"
        - "runtime.md#rt-rte-admit-output"
        - "epistemic.md#epi-rte-answer-agreement"
        - "memory.md#mem-obj-pending-outputs"
        - "runtime.md#rt-obj-compile-items"
        - "memory.md#mem-obj-communities"
        - "memory.md#mem-obj-learnings"
        - "epistemic.md#epi-rte-benchmark-judge"
      note: "Each positive signal names an actual push operation. Query search/graph expansion is classified under its pull request and does not establish push signals. Opaque alternatives remain unresolved, not inapplicable."
    trace_learning:
      assessment: "partial"
      units:
        -
          scope: "Session scribe: recorded conversation to retained ontology to later explicit ontology query"
          assessment: "known"
          findings:
            -
              value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-scribe-session"
                - "memory.md#mem-obj-entities"
                - "runtime.md#rt-rte-search-wiki"
              note: "Filtered user/assistant session text automatically produces durable definitions/relations; later ontology traversal serializes the retained result."
          records:
            - "runtime.md#rt-rte-scribe-session"
            - "memory.md#mem-obj-entities"
            - "runtime.md#rt-rte-search-wiki"
          note: "A wired trace-fed behavior-shaping artifact suffices. No improved capacity, automatic host hook or general prose-Q&A delivery is asserted."
        -
          scope: "Conversation/text capture, arbitrary imported source compilation, caller-authored lessons and saved answers"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-capture-knowledge"
            - "memory.md#mem-obj-raw-sources"
            - "runtime.md#rt-rte-compile-sources"
            - "memory.md#mem-obj-learnings"
            - "memory.md#mem-obj-pending-outputs"
          note: "Some input may record activity, but accepted records do not resolve the original content of every route or establish every qualifying trace-to-later-consumer chain. Generic Q&A prose and a learning label are not themselves trace evidence."
        -
          scope: "Batch checkpoints, full evaluator-session ingestion and lint feedback alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-compile-sources"
            - "epistemic.md#epi-rte-benchmark-judge"
            - "memory.md#mem-obj-learnings"
          note: "The records do not completely trace these alternative automatic writes through durable artifacts to later consumers. No bounded absence record licenses a local or system-wide no."
      records:
        - "runtime.md#rt-rte-scribe-session"
        - "memory.md#mem-obj-entities"
        - "runtime.md#rt-rte-search-wiki"
        - "runtime.md#rt-rte-capture-knowledge"
        - "memory.md#mem-obj-raw-sources"
        - "runtime.md#rt-rte-compile-sources"
        - "memory.md#mem-obj-learnings"
        - "memory.md#mem-obj-pending-outputs"
        - "epistemic.md#epi-rte-benchmark-judge"
      note: "The scribe route establishes a local wired yes. Unresolved input provenance and alternate writes prevent complete coverage; no system-wide negative or improvement claim follows."
    trace_source:
      assessment: "partial"
      units:
        -
          scope: "Qualifying scribe session extraction input"
          assessment: "known"
          findings:
            -
              value: "session-logs"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-scribe-session"
                - "memory.md#mem-obj-entities"
              note: "Original input is JSONL conversational user/assistant turns; filtering removes thinking/tool-use/tool-result material before extraction."
          records:
            - "runtime.md#rt-rte-scribe-session"
            - "memory.md#mem-obj-entities"
          note: "This route does not acquire tool-traces merely because the original file could contain omitted tool records."
        -
          scope: "Other potentially trace-fed capture/compile/lesson/answer routes"
          assessment: "not-determinable"
          findings: []
          records:
            - "runtime.md#rt-rte-capture-knowledge"
            - "memory.md#mem-obj-raw-sources"
            - "runtime.md#rt-rte-compile-sources"
            - "memory.md#mem-obj-learnings"
            - "memory.md#mem-obj-pending-outputs"
          note: "Original input may be a conversation, static project content or externally authored text. No complete trace-origin inventory supports event-streams, tool-traces or trajectories for these routes."
        -
          scope: "Opaque batch checkpoint and fuller evaluator/lint update inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-rte-compile-sources"
            - "epistemic.md#epi-rte-benchmark-judge"
          note: "Source content and qualifying durable write/later-consumer chains are incompletely established; this is not inapplicability."
      records:
        - "runtime.md#rt-rte-scribe-session"
        - "memory.md#mem-obj-entities"
        - "runtime.md#rt-rte-capture-knowledge"
        - "memory.md#mem-obj-raw-sources"
        - "runtime.md#rt-rte-compile-sources"
        - "memory.md#mem-obj-learnings"
        - "memory.md#mem-obj-pending-outputs"
        - "epistemic.md#epi-rte-benchmark-judge"
      note: "Session-logs is supported for the qualifying scribe chain. One known source cannot resolve the original inputs to other potentially qualifying writes."
---

# Sage-wiki memory profile

## Comparison rationale

### Boundary and coverage

This profile classifies accepted records, not newly inspected implementation. Positive findings describe wired capacity except for external host instruction authority, which is afforded under a conditional loading contract; none establishes observed use or benefit. Every axis is partial because the accepted inventory leaves included alternatives unresolved. The unresolved units are not erased by strong witnesses on other paths. No bounded absence record supports a blanket negative.

The central retained objects are prose and structured knowledge, their access representations, and retained control state. Dense embeddings are parametric representations stored in SQLite, not evidence of updated model weights. Symbolic queue, alias and output-trust fields are included because later invocations consume them to select work, reject candidates or control retrieval. Changed installed guidance is included as retained machinery; shipped static instructions and current-call prompt assembly are not themselves accumulated memory. See [MEM-OBJ-vectors](memory.md#mem-obj-vectors), [RT-OBJ-compile-items](runtime.md#rt-obj-compile-items), [MEM-OBJ-entity-aliases](memory.md#mem-obj-entity-aliases), [MEM-OBJ-pending-outputs](memory.md#mem-obj-pending-outputs) and [RT-RTE-apply-pack](runtime.md#rt-rte-apply-pack).

### Local agency and authority

A caller-authored write does not establish manual agency: the caller could be an agent. Software admission after model generation is automatic even when a human starts compilation. Explicit caller-selected alias/output review and pack/restore selection retain unresolved human control. This uncertainty does not weaken the separately wired automatic branches. See [RT-RTE-write-article](runtime.md#rt-rte-write-article), [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources), [MEM-RTE-resolve-aliases](memory.md#mem-rte-resolve-aliases) and [RT-RTE-admit-output](runtime.md#rt-rte-admit-output).

Retained prose has knowledge force at later answering/writing consumers; retained text and vectors can also influence ranking. Alias status and output evidence have validation and enforced-veto force at their particular consumers. Those controls are not universal: direct file reads bypass output eligibility. Installed prompt overrides have wired instruction authority at internal completion consumers through registry loading. Generated or installed host guidance instead has afforded instruction authority: writing the files makes standing directions available, but does not wire their force at an external host whose loading, precedence and reload remain unestablished. Neither path proves compliance. The stored learning table has no established native lesson-to-article delivery despite its template slot. See [MEM-OBJ-entries](memory.md#mem-obj-entries), [MEM-OBJ-vectors](memory.md#mem-obj-vectors), [MEM-OBJ-entity-aliases](memory.md#mem-obj-entity-aliases), [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki), [RT-OBJ-prompts](runtime.md#rt-obj-prompts), [RT-RTE-apply-pack](runtime.md#rt-rte-apply-pack), [RT-BAP-generated-skill](runtime.md#rt-bap-generated-skill) and [MEM-OBJ-learnings](memory.md#mem-obj-learnings).

### Read-back chains

Requested search, document answering and graph/community answering are pull operations. Automatic delivery within that requested return is not counted again as push. At a different consumer boundary, compile/resume code automatically selects saved summaries, existing articles and source sections for independent model calls; these are push operations into the receiving completion. Hash/path/concept identity matches and lexical section selection establish different signals; first-section fallback and lifecycle/budget filters are coarse. Retained alias decisions and earlier answers likewise have automatic internal maintenance consumers. See [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki), [RT-RTE-query-answer](runtime.md#rt-rte-query-answer), [MEM-RTE-graph-query](memory.md#mem-rte-graph-query), [MEM-RTE-global-query](memory.md#mem-rte-global-query), [MEM-OBJ-summaries](memory.md#mem-obj-summaries), [RT-RTE-compile-sources](runtime.md#rt-rte-compile-sources), [MEM-RTE-resolve-aliases](memory.md#mem-rte-resolve-aliases) and [EPI-RTE-answer-agreement](epistemic.md#epi-rte-answer-agreement).

### Curation and trace-fed updates

Summary reduction and extraction of standing definitions from recorded session turns support consolidation. Folding near-duplicate concepts, alias consolidation, revision, validity withdrawal, output promotion and age/count pruning have their own local mechanisms. Requested theme/article generation does not by itself establish a new claim absent from the inputs, so synthesis is unresolved rather than silently inferred from a route name. A faithfulness defect also does not turn compression into synthesis. See [MEM-OBJ-summaries](memory.md#mem-obj-summaries), [RT-RTE-scribe-session](runtime.md#rt-rte-scribe-session), [MEM-OBJ-manifest](memory.md#mem-obj-manifest), [MEM-RTE-resolve-aliases](memory.md#mem-rte-resolve-aliases), [EPI-RTE-edge-supersession](epistemic.md#epi-rte-edge-supersession), [EPI-RTE-verify-promote](epistemic.md#epi-rte-verify-promote), [MEM-OBJ-learnings](memory.md#mem-obj-learnings) and [EPI-RTE-community-summary](epistemic.md#epi-rte-community-summary).

Scribing establishes trace learning in the profile's write-route sense: recorded user/assistant turns feed automatic durable ontology writes, and later ontology traversal returns their definitions. The trace input has learning authority at the update; the derived definitions have knowledge authority at later consumers. Tool records are filtered out, so this chain supports session-logs, not tool-traces. A pathless entity need not enter ordinary article Q&A. This finding establishes neither improved capacity nor exercised self-improvement. Other capture/source origins and checkpoint/evaluator alternatives remain unresolved rather than inheriting the scribe classification. See [RT-RTE-scribe-session](runtime.md#rt-rte-scribe-session), [MEM-OBJ-entities](memory.md#mem-obj-entities) and [RT-RTE-search-wiki](runtime.md#rt-rte-search-wiki).

### Canonical identities and source-read log

Reconciliation supersedes the epistemic raw-source, local graph-answer and global community-answer duplicates with the memory raw-source object and graph/global routes. This profile cites those canonical memory records. The prose-only article, output, relation and community parts remain valid alongside their mixed containers; their distinct consumers are not collapsed. These identity resolutions change citation targets, not classification strength. See [MEM-OBJ-raw-sources](memory.md#mem-obj-raw-sources), [MEM-RTE-graph-query](memory.md#mem-rte-graph-query), [MEM-RTE-global-query](memory.md#mem-rte-global-query), [EPI-OBJ-article-text](epistemic.md#epi-obj-article-text), [EPI-OBJ-output-text](epistemic.md#epi-obj-output-text), [EPI-OBJ-relation-state](epistemic.md#epi-obj-relation-state) and [EPI-OBJ-community-text](epistemic.md#epi-obj-community-text).

No source files were read for this profile. All warrants come from the supplied accepted records and their annotations; no records, source quotations or new evidence are introduced. Missing batch-payload, initial-provenance, backend/restore-parity, full lint/evaluator-consumer and caller-control facts prevent stronger coverage assessments, not the bounded positive classifications.
