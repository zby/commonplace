---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "WikiSkill memory comparison of its documented execution-derived Raw/Wiki/Skill workspace and unresolved retention alternatives at the frozen arXiv v1 capture."
run-id: "AAS-2026-10-15-2608-27454-65116a9d0de7-01"
source-identity: "https://arxiv.org/abs/2608.27454"
reviewed-boundary: "arxiv-2608.27454v1-text-2026-10-15"
memory-comparison:
  version: 2
  scope: "Accumulated raw training trajectories; wiki pattern pages, relevance index, evolution log and intervention/validation history; candidate/active SKILL.md and companion PURPOSE.md; their automatic writes, edits, withdrawal and later maintainer/proposer/task consumers, including wiki-enabled inference. Unresolved provider caches, validation-trace retention, durable restore checkpoints, initial admission and companion delivery remain named coverage limits. Excludes static shipped prompts, pretrained model weights without an evidenced update, task documents/current outcomes except where retained within experience, ordinary current rollout/history state and the live scalar best-score variable. Cross-run reload is not established; described persistence spans evolution rounds and final skills/wiki return."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Documented Raw, Wiki and Skill filesystem objects, including the separately retained PURPOSE.md"
          assessment: "known"
          findings:
            - value: "files"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "memory.md#mem-obj-skill-impact", "memory.md#mem-obj-skill", "memory.md#mem-obj-purpose"]
              note: "All seven objects are described as retained workspace files; Markdown, JSON and diff encoding do not add another substrate."
          records: ["memory.md#mem-obj-raw", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "memory.md#mem-obj-skill-impact", "memory.md#mem-obj-skill", "memory.md#mem-obj-purpose"]
          note: "The seven named objects cover the documented three-layer workspace. The log filename ambiguity does not change its declared filesystem substrate; companion rollback mechanics do not change its declared storage."
        - scope: "Potential retained provider state, validation-trajectory archive and durable restore checkpoint"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-cmp-model-backends", "memory.md#mem-obj-raw", "runtime.md#rt-rte-validation-gate"]
          note: "The accepted records leave provider caches, validation-trace retention and durable incumbent snapshot storage unresolved. Their existence, content and later-consumer routes are not established, preventing complete storage-substrate coverage; model backend weights alone are not evidence of accumulated memory."
      records: ["memory.md#mem-obj-raw", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "memory.md#mem-obj-skill-impact", "memory.md#mem-obj-skill", "memory.md#mem-obj-purpose", "runtime.md#rt-cmp-model-backends", "runtime.md#rt-rte-validation-gate"]
      note: "The described seven-object workspace has files storage at claimed strength. Potential additional retention and restore substrates remain unresolved; this is not a whole-runtime storage inventory."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Raw reasoning, answers and observations interpreted by later maintainer/proposer models"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal"]
              note: "Retained reasoning and answers provide interpretable diagnostic content."
          records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal"]
          note: "This classifies textual interaction content, not the serialization of every raw trace."
        - scope: "Raw tool-call/result and task-action fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "epistemic.md#epi-obj-imported-evidence", "epistemic.md#epi-obj-produced-predictions"]
              note: "The raw-object records distinguish structured calls, results and action fields from narrative reasoning."
          records: ["memory.md#mem-obj-raw", "epistemic.md#epi-obj-imported-evidence", "epistemic.md#epi-obj-produced-predictions"]
          note: "Symbolic fields coexist with narrative content; their presence does not imply that later diagnostic model interpretation executes recorded calls."
        - scope: "Pattern explanations, evolution narrative, proposal diffs, skill instructions and purpose rationale at model readers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records: ["memory.md#mem-obj-patterns", "memory.md#mem-obj-log", "memory.md#mem-obj-skill-impact", "memory.md#mem-obj-skill", "memory.md#mem-obj-purpose", "memory.md#mem-bap-wiki-guidance", "runtime.md#rt-bap-skill-injection"]
              note: "These retained parts are interpreted as explanations, history or procedures rather than as executable skill scripts."
          records: ["memory.md#mem-obj-patterns", "memory.md#mem-obj-log", "memory.md#mem-obj-skill-impact", "memory.md#mem-obj-skill", "memory.md#mem-obj-purpose", "memory.md#mem-bap-wiki-guidance", "runtime.md#rt-bap-skill-injection"]
          note: "PURPOSE.md has a described natural-language form even though its separate later delivery is unresolved. No executable skill script is established for this workspace."
        - scope: "Index relevance summaries at proposer/maintainer readers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "claimed"
              records: ["memory.md#mem-obj-index", "runtime.md#rt-rte-skill-proposal"]
              note: "Problem, root cause and fix summaries allow model judgment of relevance."
          records: ["memory.md#mem-obj-index", "runtime.md#rt-rte-skill-proposal"]
          note: "The summary is a distinct consumed access aid, not the entire underlying pattern payload."
        - scope: "Index paths resolved by requested file reads; skill metadata and impact score/identity/outcome fields"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "claimed"
              records: ["memory.md#mem-obj-index", "memory.md#mem-obj-skill", "memory.md#mem-obj-skill-impact", "runtime.md#rt-rte-skill-proposal"]
              note: "Localized path identities, YAML fields and numeric/disposition fields have structured meanings distinct from their surrounding prose."
          records: ["memory.md#mem-obj-index", "memory.md#mem-obj-skill", "memory.md#mem-obj-skill-impact", "runtime.md#rt-rte-skill-proposal"]
          note: "These structured parts do not establish a retained learned ranking policy or machine enforcement by the history itself."
        - scope: "Potential retained provider state, validation-trajectory archive and durable restore checkpoint"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-cmp-model-backends", "memory.md#mem-obj-raw", "runtime.md#rt-rte-validation-gate"]
          note: "The accepted records leave provider caches, validation-trace retention and durable incumbent snapshot storage unresolved. Their existence, content and later-consumer routes are not established, preventing complete representational-form coverage; model backend weights alone are not evidence of accumulated memory."
      records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "epistemic.md#epi-obj-imported-evidence", "epistemic.md#epi-obj-produced-predictions", "memory.md#mem-obj-patterns", "memory.md#mem-obj-log", "memory.md#mem-obj-skill-impact", "memory.md#mem-obj-skill", "memory.md#mem-obj-purpose", "memory.md#mem-bap-wiki-guidance", "runtime.md#rt-bap-skill-injection", "memory.md#mem-obj-index", "runtime.md#rt-cmp-model-backends", "runtime.md#rt-rte-validation-gate"]
      note: "Natural-language and symbolic parts are separated by payload and consumption. The distributed-parametric model component is an executor, not an evidenced memory update; potential additional retained payloads remain unclassified."
    lineage:
      assessment: "partial"
      units:
        - scope: "Raw training interaction record produced by task rollouts"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-task-execution"]
              note: "The retained record originates in training reasoning, actions, tool results and answers rather than in wiki summaries."
          records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-task-execution"]
          note: "Recorded interaction lineage is specified; raw serialization and validation-trace retention are not."
        - scope: "External evidence and environment/tool outputs retained within raw training traces"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "epistemic.md#epi-obj-imported-evidence", "epistemic.md#epi-rte-task-import"]
              note: "External task/tool/environment content enters traces through acquisition rather than model generation."
          records: ["memory.md#mem-obj-raw", "epistemic.md#epi-obj-imported-evidence", "epistemic.md#epi-rte-task-import"]
          note: "Imported lineage applies to the incoming part only. Generated predictions have a different producer; import does not certify source truth."
        - scope: "Generated answers and reasoning retained in raw training traces"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "epistemic.md#epi-obj-produced-predictions", "runtime.md#rt-rte-task-execution"]
              note: "The task model produces these candidates; they are not imports merely because task evidence informs them."
          records: ["memory.md#mem-obj-raw", "epistemic.md#epi-obj-produced-predictions", "runtime.md#rt-rte-task-execution"]
          note: "This does not classify generated answers as entailed, true or accepted."
        - scope: "Maintainer-generated pattern explanations and fixes, and proposer-generated SKILL.md/PURPOSE.md"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "claimed"
              records: ["memory.md#mem-obj-patterns", "memory.md#mem-obj-skill", "memory.md#mem-obj-purpose", "epistemic.md#epi-rte-wiki-formulation", "runtime.md#rt-rte-skill-proposal"]
              note: "Models author diagnoses, candidate procedures and origin/rationale text using supplied evidence and prior content."
          records: ["memory.md#mem-obj-patterns", "memory.md#mem-obj-skill", "memory.md#mem-obj-purpose", "epistemic.md#epi-rte-wiki-formulation", "runtime.md#rt-rte-skill-proposal"]
          note: "Authorship names the derivation mechanism, not human admission. Exact truth-apt semantics of individual generated claims remain indeterminate."
        - scope: "Trace-derived command evidence and findings retained in wiki patterns and evolution summaries"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "memory.md#mem-obj-patterns", "memory.md#mem-obj-log", "runtime.md#rt-rte-wiki-maintenance"]
              note: "Sampled successes/failures supply command sequences and iteration findings for durable wiki content."
          records: ["memory.md#mem-obj-raw", "memory.md#mem-obj-patterns", "memory.md#mem-obj-log", "runtime.md#rt-rte-wiki-maintenance"]
          note: "The trace-derived parts are distinguished from the model-authored explanatory claims. Capped delivery limits the evidence available to authors."
        - scope: "Replacement index summaries compiled from wiki pages"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "claimed"
              records: ["memory.md#mem-obj-index", "runtime.md#rt-rte-wiki-maintenance"]
              note: "The maintainer constructs a complete derived access summary from the current wiki."
          records: ["memory.md#mem-obj-index", "runtime.md#rt-rte-wiki-maintenance"]
          note: "The summarized index is derived from retained pages; faithful preservation of every claim is not established."
        - scope: "Harness-written intervention and score/disposition history"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "claimed"
              records: ["memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-validation-gate"]
              note: "The harness assembles proposal metadata/diff with evaluator scores and admission results after either decision."
          records: ["memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-validation-gate"]
          note: "This derivation is distinct from model-authored causal diagnosis; full rejected-file reconstructability remains unknown."
        - scope: "Initial wiki/skill scaffolding, undocumented seeds/replacements and additional provider/checkpoint provenance"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "runtime.md#rt-cmp-model-backends", "runtime.md#rt-rte-validation-gate"]
          note: "Empty initial skills/wiki are specified, but setup control, any alternate seeding/replacement and additional retention provenance are not. A known subsequent derivation does not resolve these alternatives."
      records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-task-execution", "epistemic.md#epi-obj-imported-evidence", "epistemic.md#epi-rte-task-import", "epistemic.md#epi-obj-produced-predictions", "memory.md#mem-obj-patterns", "memory.md#mem-obj-skill", "memory.md#mem-obj-purpose", "epistemic.md#epi-rte-wiki-formulation", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-log", "runtime.md#rt-rte-wiki-maintenance", "memory.md#mem-obj-index", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-validation-gate", "runtime.md#rt-cmp-model-backends"]
      note: "The documented derivations include model authorship, imported raw evidence, trace extraction and derived access/audit compilation. Missing initialization and additional-state provenance prevent complete lineage coverage."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Raw traces consumed by maintainer and proposer to construct durable wiki and skills"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-patterns", "memory.md#mem-obj-skill"]
              note: "Recorded actions, reasoning and outcomes supply diagnostic evidence/context."
            - value: "learning"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-patterns", "memory.md#mem-obj-skill"]
              note: "Retained experience feeds the specified automatic creation/revision of durable behavior-shaping wiki and procedures."
          records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-patterns", "memory.md#mem-obj-skill"]
          note: "Evidence supply and update use are distinct effects of the same retained traces. Neither establishes truthful diagnosis or improved future capacity."
        - scope: "Patterns, index and evolution log at subsequent maintainer/proposer consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "claimed"
              records: ["memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-bap-wiki-guidance"]
              note: "Explanations and historical summaries supply reference and advice."
            - value: "learning"
              basis: "claimed"
              records: ["memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-bap-wiki-guidance"]
              note: "Prior wiki content feeds later wiki edits and skill proposals that persist beyond the current model call."
          records: ["memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-bap-wiki-guidance"]
          note: "This is the default mediated wiki pathway. Pattern advice is not automatically standing instruction to default task inference."
        - scope: "Index summaries influencing which pattern pages the proposer reads"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "claimed"
              records: ["memory.md#mem-obj-index", "runtime.md#rt-rte-skill-proposal"]
              note: "Specific problem/cause/fix summaries influence relative relevance of candidate page reads."
          records: ["memory.md#mem-obj-index", "runtime.md#rt-rte-skill-proposal"]
          note: "Ranking influence is model-interpreted relevance judgment, not an evidenced vector index or learned retrieval scorer. Requested read selection is still pull."
        - scope: "Intervention history supplied to later proposer"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "claimed"
              records: ["memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-skill-proposal"]
              note: "Diffs, scores and outcomes provide context about previous attempts."
            - value: "learning"
              basis: "claimed"
              records: ["memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-skill-proposal"]
              note: "Retained feedback informs later durable skill revisions, including avoidance of previously rejected approaches."
          records: ["memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-skill-proposal"]
          note: "The proposer route is specified. The history advises; no machine-enforced veto on repeating proposals is established."
        - scope: "Procedural SKILL.md at provisional validation inference and later active task inference"
          assessment: "known"
          findings:
            - value: "instruction"
              basis: "claimed"
              records: ["memory.md#mem-obj-skill", "runtime.md#rt-bap-skill-injection", "runtime.md#rt-rte-task-execution", "runtime.md#rt-rte-validation-gate"]
              note: "Applicability conditions and procedures are delivered through the system-prompt skill channel."
          records: ["memory.md#mem-obj-skill", "runtime.md#rt-bap-skill-injection", "runtime.md#rt-rte-task-execution", "runtime.md#rt-rte-validation-gate"]
          note: "Candidate exposure can precede acceptance. This is interpreted guidance, not enforced compliance or explanation endorsement."
        - scope: "Separate PURPOSE.md consumers; complete maintainer intervention-history supply; wiki-enabled inference force"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-purpose", "memory.md#mem-obj-skill-impact", "memory.md#mem-bap-wiki-guidance", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-validation-gate"]
          note: "Rationale delivery is not separately specified. Runtime and specialist records disagree about necessarily complete maintainer tracker delivery. Alternative inference wiki access is described but its consumed payload/channel is unresolved. These limits prevent a complete consumer/effect inventory."
        - scope: "Potential retained provider state, validation-trajectory archive and durable restore checkpoint"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-cmp-model-backends", "memory.md#mem-obj-raw", "runtime.md#rt-rte-validation-gate"]
          note: "The accepted records leave provider caches, validation-trace retention and durable incumbent snapshot storage unresolved. Their existence, content and later-consumer routes are not established, preventing complete behavioral-authority coverage; model backend weights alone are not evidence of accumulated memory."
      records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-patterns", "memory.md#mem-obj-skill", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "memory.md#mem-bap-wiki-guidance", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-bap-skill-injection", "runtime.md#rt-rte-task-execution", "runtime.md#rt-rte-validation-gate", "memory.md#mem-obj-purpose", "runtime.md#rt-cmp-model-backends"]
      note: "Supported knowledge, learning, ranking and instruction findings stay on actual retained-part consumers. The scalar current best score and static prompts are outside this accumulated-memory boundary, so their admission/enforcement roles are not attributed to retained history. Unresolved consumers and additional state keep coverage partial."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Harness admission of generated raw training trajectories"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-task-execution"]
              note: "Software retains model/tool interaction records without a described per-trace operator content approval."
          records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-task-execution"]
          note: "Starting an experiment is not a per-content admission decision."
        - scope: "Maintainer-selected pattern edits, replacement index and log append"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records: ["runtime.md#rt-rte-wiki-maintenance", "epistemic.md#epi-rte-wiki-formulation", "epistemic.md#epi-rte-wiki-retention", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log"]
              note: "The model chooses content and edit operations; surrounding software applies them without a described wiki-content human veto."
          records: ["runtime.md#rt-rte-wiki-maintenance", "epistemic.md#epi-rte-wiki-formulation", "epistemic.md#epi-rte-wiki-retention", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log"]
          note: "Model authorship, admission choice and physical application are separate roles, all computational in the documented route. Edit failure handling remains unknown."
        - scope: "Single-skill creation/patch and associated creation-time rationale admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records: ["runtime.md#rt-rte-skill-proposal", "runtime.md#rt-rte-validation-gate", "memory.md#mem-obj-skill", "memory.md#mem-obj-purpose"]
              note: "The proposer submits content and the harness uses the strict validation comparison to accept or restore active skills, with no per-candidate human approval."
          records: ["runtime.md#rt-rte-skill-proposal", "runtime.md#rt-rte-validation-gate", "memory.md#mem-obj-skill", "memory.md#mem-obj-purpose"]
          note: "This classifies the described candidate route, including creation-time PURPOSE.md supply; synchronized companion patch/restore coverage remains unspecified."
        - scope: "Harness append of intervention history after acceptance or rejection"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records: ["memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-validation-gate"]
              note: "Outcome and proposal/diff logging follows the software decision rather than a per-entry human admission choice."
          records: ["memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-validation-gate"]
          note: "Rejected content can be admitted as history without being admitted as active instructions."
        - scope: "Initial workspace creation, alternate human seeding/replacement and undocumented companion-file updates"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-purpose"]
          note: "Initial content is declared empty but initializer identity/control and alternate content replacement are unspecified. Generic caller identity cannot establish manual agency; no manual finding is inferred."
        - scope: "Potential retained provider state, validation-trajectory archive and durable restore checkpoint"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-cmp-model-backends", "memory.md#mem-obj-raw", "runtime.md#rt-rte-validation-gate"]
          note: "The accepted records leave provider caches, validation-trace retention and durable incumbent snapshot storage unresolved. Their existence, content and later-consumer routes are not established, preventing complete write-agency coverage; model backend weights alone are not evidence of accumulated memory."
      records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-task-execution", "runtime.md#rt-rte-wiki-maintenance", "epistemic.md#epi-rte-wiki-formulation", "epistemic.md#epi-rte-wiki-retention", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "runtime.md#rt-rte-skill-proposal", "runtime.md#rt-rte-validation-gate", "memory.md#mem-obj-skill", "memory.md#mem-obj-purpose", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-cmp-model-backends"]
      note: "Known computational admission routes coexist with unresolved initialization, companion maintenance and potential additional retention. The automatic findings do not upgrade unknown alternative admission mechanisms."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Condensed wiki index and brief evolution summaries derived from retained pages and training experience"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "claimed"
              records: ["memory.md#mem-obj-index", "memory.md#mem-obj-log", "runtime.md#rt-rte-wiki-maintenance", "memory.md#mem-obj-raw"]
              note: "Problem/cause/fix summaries and brief findings/actions reduce retained content to smaller representations for subsequent consumption."
          records: ["memory.md#mem-obj-index", "memory.md#mem-obj-log", "runtime.md#rt-rte-wiki-maintenance", "memory.md#mem-obj-raw"]
          note: "This maps the described summarizing transformations, not index acquisition/rebuild alone. It does not resolve the semantics of newly formulated root causes."
        - scope: "Refinement of existing pattern text and existing skill instructions"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "claimed"
              records: ["epistemic.md#epi-rte-wiki-formulation", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-patterns", "memory.md#mem-obj-skill"]
              note: "Maintainer replace operations refine existing text and proposer patches revise existing procedural entries."
          records: ["epistemic.md#epi-rte-wiki-formulation", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-patterns", "memory.md#mem-obj-skill"]
          note: "The transformation is declared; actual patch application, fidelity and companion synchronization are uninspected."
        - scope: "Rejected candidate procedural reliance withdrawn while its intervention evidence remains"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "claimed"
              records: ["runtime.md#rt-rte-validation-gate", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-skill-disposition", "epistemic.md#epi-rte-impact-retention"]
              note: "Rollback removes rejected candidate changes from active skills while impact history preserves the attempted intervention and outcome."
          records: ["runtime.md#rt-rte-validation-gate", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-skill-disposition", "epistemic.md#epi-rte-impact-retention"]
          note: "Withdrawal is bounded to active candidate instructions. It neither retracts related wiki claims nor deletes the history."
        - scope: "New causal claims, generalized remedies and newly composed skill content"
          assessment: "not-determinable"
          findings: []
          records: ["epistemic.md#epi-rte-wiki-formulation", "runtime.md#rt-rte-skill-proposal", "epistemic.md#epi-clm-knowledge-growth"]
          note: "The records leave preservation, entailment and non-entailment indeterminate for particular content edges. Requested root-cause analysis and novelty do not establish synthesize; nor do they justify treating every generated explanation as consolidate."
        - scope: "Semantic duplicate handling, longer-horizon pruning/expiry and companion-file maintenance"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-rte-wiki-maintenance", "memory.md#mem-obj-patterns", "memory.md#mem-obj-purpose", "epistemic.md#epi-clm-knowledge-growth"]
          note: "No-duplicate and concise-page requirements request behavior rather than demonstrate a dedup transformation. The declared lack of automated wiki pruning is not a searched implementation-wide absence; decay, manual cleanup and synchronized rationale edits remain unresolved."
        - scope: "Potential retained provider state, validation-trajectory archive and durable restore checkpoint"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-cmp-model-backends", "memory.md#mem-obj-raw", "runtime.md#rt-rte-validation-gate"]
          note: "The accepted records leave provider caches, validation-trace retention and durable incumbent snapshot storage unresolved. Their existence, content and later-consumer routes are not established, preventing complete curation-operation coverage; model backend weights alone are not evidence of accumulated memory."
      records: ["memory.md#mem-obj-index", "memory.md#mem-obj-log", "runtime.md#rt-rte-wiki-maintenance", "memory.md#mem-obj-raw", "epistemic.md#epi-rte-wiki-formulation", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-patterns", "memory.md#mem-obj-skill", "runtime.md#rt-rte-validation-gate", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-skill-disposition", "epistemic.md#epi-rte-impact-retention", "epistemic.md#epi-clm-knowledge-growth", "memory.md#mem-obj-purpose", "runtime.md#rt-cmp-model-backends"]
      note: "Consolidation, revision and bounded withdrawal have claimed mechanism support. Requested deduplication and uncertain semantic novelty are not promoted into positive operations; unresolved maintenance and unavailable implementation prevent complete coverage."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Training traces and current wiki delivered to the maintainer at each maintenance call"
          assessment: "known"
          findings:
            - value: "push"
              basis: "claimed"
              records: ["runtime.md#rt-rte-wiki-maintenance", "memory.md#mem-obj-raw", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log"]
              note: "The harness independently supplies selected/capped retained traces and current wiki, without a maintainer file-content request."
          records: ["runtime.md#rt-rte-wiki-maintenance", "memory.md#mem-obj-raw", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log"]
          note: "Stratified sampling and full-wiki supply are declared. Complete intervention-tracker inclusion is separated as unresolved."
        - scope: "Initial index and intervention-history delivery to each proposer invocation"
          assessment: "known"
          findings:
            - value: "push"
              basis: "claimed"
              records: ["runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-index", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention"]
              note: "The harness supplies retained access summaries and prior feedback as initial context."
          records: ["runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-index", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention"]
          note: "The initial all-task outcome summary also appears, but current outcomes alone are not an additional accumulated-memory object."
        - scope: "Proposer-requested pattern, trace and history file reads"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "claimed"
              records: ["runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-raw", "memory.md#mem-obj-patterns", "memory.md#mem-obj-skill-impact", "memory.md#mem-bap-wiki-guidance"]
              note: "Model read_file requests select retained detailed content; returning a requested file fulfills that request rather than adding a second push."
          records: ["runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-raw", "memory.md#mem-obj-patterns", "memory.md#mem-obj-skill-impact", "memory.md#mem-bap-wiki-guidance"]
          note: "Trace aliases and filenames resolve requested content; they do not establish unsolicited identifier selection."
        - scope: "Candidate/active procedural content automatically supplied to task inference"
          assessment: "known"
          findings:
            - value: "push"
              basis: "claimed"
              records: ["runtime.md#rt-rte-task-execution", "memory.md#mem-obj-skill", "runtime.md#rt-bap-skill-injection", "runtime.md#rt-rte-validation-gate"]
              note: "All candidate or accepted active skill contents are supplied at task invocation without a request for those retained files."
          records: ["runtime.md#rt-rte-task-execution", "memory.md#mem-obj-skill", "runtime.md#rt-bap-skill-injection", "runtime.md#rt-rte-validation-gate"]
          note: "Provisional validation and later accepted inference are both specified. Full injection is not task-relevance retrieval."
        - scope: "Separate PURPOSE.md delivery, complete maintainer tracker supply and wiki-enabled inference access"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-purpose", "memory.md#mem-obj-skill-impact", "memory.md#mem-bap-wiki-guidance", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-validation-gate"]
          note: "These included alternatives lack a settled consumer/delivery chain. Wiki access alone does not decide pull versus push; conflicting maintainer completeness claims cannot supply a joint complete route."
        - scope: "Potential retained provider state, validation-trajectory archive and durable restore checkpoint"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-cmp-model-backends", "memory.md#mem-obj-raw", "runtime.md#rt-rte-validation-gate"]
          note: "The accepted records leave provider caches, validation-trace retention and durable incumbent snapshot storage unresolved. Their existence, content and later-consumer routes are not established, preventing complete read-back-direction coverage; model backend weights alone are not evidence of accumulated memory."
      records: ["runtime.md#rt-rte-wiki-maintenance", "memory.md#mem-obj-raw", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "memory.md#mem-bap-wiki-guidance", "runtime.md#rt-rte-task-execution", "memory.md#mem-obj-skill", "runtime.md#rt-bap-skill-injection", "runtime.md#rt-rte-validation-gate", "memory.md#mem-obj-purpose", "runtime.md#rt-cmp-model-backends"]
      note: "The default routes support both push and pull. Missing companion, alternative inference and additional-state routes prevent complete enumeration; default wiki denial is not a universal absence of direct wiki read-back."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Maintenance-call trace push: success/failure stratification and capped logs"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "claimed"
              records: ["runtime.md#rt-rte-wiki-maintenance", "memory.md#mem-obj-raw"]
              note: "After training, the harness selects up to five failing and three passing traces using outcome categories and caps each delivered log at 15,000 characters."
          records: ["runtime.md#rt-rte-wiki-maintenance", "memory.md#mem-obj-raw"]
          note: "The trigger, selector input and selected retained traces are named. Tie-breaking and which characters survive the cap are unspecified; categories/budgets are not targeted identity matches."
        - scope: "Maintenance-call current-wiki push and proposer-start index/history push"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "claimed"
              records: ["runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention"]
              note: "Role and invocation determine supply of current wiki or its index/history view, without an evidenced per-page relevance selector on these pushes."
          records: ["runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention"]
          note: "This classifies the documented wholesale/default payload supply, not the later model-requested detail reads. It does not claim complete maintainer tracker delivery."
        - scope: "Task-invocation full skill push"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "claimed"
              records: ["runtime.md#rt-rte-task-execution", "runtime.md#rt-bap-skill-injection", "memory.md#mem-obj-skill", "runtime.md#rt-rte-validation-gate"]
              note: "Task invocation triggers injection of the full active configuration; membership/availability determines inclusion, not task-relevance or identity matching against a targeting input."
          records: ["runtime.md#rt-rte-task-execution", "runtime.md#rt-bap-skill-injection", "memory.md#mem-obj-skill", "runtime.md#rt-rte-validation-gate"]
          note: "Accepted or provisionally applied configuration supplies the entire set. File identities alone do not establish identifier push."
        - scope: "Wiki-enabled inference selector and uncertain rationale/maintainer-history delivery"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-bap-wiki-guidance", "memory.md#mem-obj-purpose", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-validation-gate"]
          note: "Access is described without selection inputs, budget or delivery mechanics for the alternative inference route; rationale and necessarily complete tracker supply remain unresolved. Their push signals cannot be inferred from the known default paths."
        - scope: "Potential retained provider state, validation-trajectory archive and durable restore checkpoint"
          assessment: "not-determinable"
          findings: []
          records: ["runtime.md#rt-cmp-model-backends", "memory.md#mem-obj-raw", "runtime.md#rt-rte-validation-gate"]
          note: "The accepted records leave provider caches, validation-trace retention and durable incumbent snapshot storage unresolved. Their existence, content and later-consumer routes are not established, preventing complete push-selection coverage; model backend weights alone are not evidence of accumulated memory."
      records: ["runtime.md#rt-rte-wiki-maintenance", "memory.md#mem-obj-raw", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-task-execution", "runtime.md#rt-bap-skill-injection", "memory.md#mem-obj-skill", "runtime.md#rt-rte-validation-gate", "memory.md#mem-bap-wiki-guidance", "memory.md#mem-obj-purpose", "runtime.md#rt-cmp-model-backends"]
      note: "Coarse push selection is supported for the default automatic supplies. Model relevance judgment guides requested pulls, so it is not an inferred-judgment push finding. Unknown alternative directions cannot be made signal-inapplicable."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic trace-fed wiki pattern, index and evolution-log production with later maintainer/proposer consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "epistemic.md#epi-rte-wiki-formulation", "epistemic.md#epi-rte-wiki-retention", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "memory.md#mem-bap-wiki-guidance"]
              note: "Sampled retained trajectories feed automatic wiki edits and summaries that persist and inform later edits/procedures."
          records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "epistemic.md#epi-rte-wiki-formulation", "epistemic.md#epi-rte-wiki-retention", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "memory.md#mem-bap-wiki-guidance"]
          note: "The complete claimed raw-to-derived-to-later-consumer path qualifies without weight updates or demonstrated improvement. Raw archiving alone is not the qualifying write."
        - scope: "Trace/wiki/feedback-fed skill creation or refinement followed by validation or later task consumption"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-skill-proposal", "runtime.md#rt-rte-validation-gate", "memory.md#mem-obj-skill", "runtime.md#rt-bap-skill-injection", "memory.md#mem-obj-skill-impact"]
              note: "The automatic proposer and harness produce durable procedural artifacts from selected experience and prior feedback; candidate and accepted content reach task inference."
          records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-skill-proposal", "runtime.md#rt-rte-validation-gate", "memory.md#mem-obj-skill", "runtime.md#rt-bap-skill-injection", "memory.md#mem-obj-skill-impact"]
          note: "Acceptance controls the later active instruction set but provisional validation consumption can precede it. Rationale delivery is not required to establish the SKILL.md path."
        - scope: "Automatic validation-feedback history append followed by later proposer consumption"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records: ["memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-validation-gate", "runtime.md#rt-rte-skill-proposal"]
              note: "A retained intervention/outcome record is automatically compiled after task evaluation and later supplied to guide durable future procedures."
          records: ["memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-rte-validation-gate", "runtime.md#rt-rte-skill-proposal"]
          note: "This is a qualifying feedback-to-durable-guidance route, not proof that every entry changes behavior or improves capacity."
        - scope: "PURPOSE.md considered separately from consumed procedures, complete maintainer tracker feedback and additional provider/checkpoint writes"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-purpose", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-cmp-model-backends", "memory.md#mem-obj-raw", "runtime.md#rt-rte-validation-gate"]
          note: "Rationale is retained but separate later consumption is unresolved; complete maintainer feedback delivery is disputed. Potential additional trace retention and durable writes have no established raw-to-derived-to-later-consumer chain. No bounded system-wide no follows."
      records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "epistemic.md#epi-rte-wiki-formulation", "epistemic.md#epi-rte-wiki-retention", "memory.md#mem-obj-patterns", "memory.md#mem-obj-index", "memory.md#mem-obj-log", "memory.md#mem-bap-wiki-guidance", "runtime.md#rt-rte-skill-proposal", "runtime.md#rt-rte-validation-gate", "memory.md#mem-obj-skill", "runtime.md#rt-bap-skill-injection", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "memory.md#mem-obj-purpose", "runtime.md#rt-cmp-model-backends"]
      note: "Several claimed automatic trace-fed artifact routes qualify. Unresolved companion and additional-state chains keep the axis partial; no local or system-wide no is inferred from missing execution evidence."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Original sampled training experience feeding wiki production and selected trace experience feeding skills"
          assessment: "known"
          findings:
            - value: "trajectories"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "runtime.md#rt-rte-task-execution"]
              note: "Raw records link step-by-step reasoning, actions, observations/results and final answers across a task rollout."
            - value: "tool-traces"
              basis: "claimed"
              records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "runtime.md#rt-rte-task-execution"]
              note: "The qualifying inputs explicitly contain recorded tool calls and tool-call outputs for tool-using tasks."
          records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "runtime.md#rt-rte-task-execution"]
          note: "Tool-free task reasoning still supplies trajectory experience; tool-traces applies to the tool-using part, not every task. No session-logs or event-streams value is inferred solely from interaction or simulator terminology."
        - scope: "Validation experience underlying the retained impact-feedback write"
          assessment: "partial"
          findings:
            - value: "trajectories"
              basis: "claimed"
              records: ["runtime.md#rt-rte-validation-gate", "epistemic.md#epi-rte-impact-retention", "memory.md#mem-obj-skill-impact", "runtime.md#rt-rte-task-execution"]
              note: "Validation task rollouts and their scored outcomes supply the experience behind automatically retained intervention feedback."
          records: ["runtime.md#rt-rte-validation-gate", "epistemic.md#epi-rte-impact-retention", "memory.md#mem-obj-skill-impact", "runtime.md#rt-rte-task-execution", "memory.md#mem-obj-raw"]
          note: "The route records establish validation rollouts and retained score/diff feedback, not a persisted full validation trajectory archive. Exact scorer inputs, treatment of tool-level feedback and fidelity of retained serialization remain unavailable; the known rollout origin does not establish every possible original-source category."
        - scope: "Inherited wiki/rationale provenance, alternative maintainer history delivery and potential provider/checkpoint learning inputs"
          assessment: "not-determinable"
          findings: []
          records: ["memory.md#mem-obj-purpose", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "memory.md#mem-obj-skill-impact", "epistemic.md#epi-rte-impact-retention", "runtime.md#rt-cmp-model-backends", "runtime.md#rt-rte-validation-gate"]
          note: "Known training traces do not resolve all mixed antecedents or additional writes. Static task references/ground truth are imported inputs, not a trace-source category merely by inclusion. Unknown companion consumption and additional-state provenance prevent complete qualifying-route coverage."
      records: ["memory.md#mem-obj-raw", "runtime.md#rt-rte-wiki-maintenance", "runtime.md#rt-rte-skill-proposal", "runtime.md#rt-rte-task-execution", "runtime.md#rt-rte-validation-gate", "epistemic.md#epi-rte-impact-retention", "memory.md#mem-obj-skill-impact", "memory.md#mem-obj-purpose", "runtime.md#rt-cmp-model-backends"]
      note: "Trajectory experience and recorded tool activity support positive source values on their qualifying writes. Mixed current references, unresolved feedback details and potential additional writes prevent a complete trace-source inventory; inapplicable is not justified by one unclassified route."
---

# WikiSkill memory profile

## Comparison rationale

This comparison classifies accepted records of the documented Raw/Wiki/Skill loop, not an inspected executable system. All positive findings have `claimed` basis. Source-native descriptions and author-reported examples do not establish wiring, observed activation or causal benefit. Coverage and evidence strength are independent: a documented part can have known classification at claimed strength while the enclosing axis remains partial.

### Inventory and unresolved alternatives

The seven filesystem objects are distinct payloads, not seven copies of runtime routes. Retained training records contain both external evidence and model-produced predictions; imported evidence and generated content must not inherit one another's lineage. The incoming and generated parts are identified by [EPI-OBJ-imported-evidence](epistemic.md#epi-obj-imported-evidence) and [EPI-OBJ-produced-predictions](epistemic.md#epi-obj-produced-predictions). The profile does not add current task evidence or pretrained model parameters to accumulated memory simply because the runtime consumes them.

Potential provider state, retained validation trajectories and durable restore snapshots remain unresolved in [RT-CMP-model-backends](runtime.md#rt-cmp-model-backends), [MEM-OBJ-raw](memory.md#mem-obj-raw) and [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate). Those records do not establish an opaque provider memory payload, a replay archive or a durable checkpoint; neither do they warrant excluding those alternatives to obtain complete coverage. Initialization and companion maintenance are separately unresolved. Unknown means no controlled value established within that named branch, not evidenced absence.

### Authority and direction

Experience has learning authority at automatic wiki/skill update consumers; the resulting procedures have instruction authority at task inference. Wiki explanations and intervention history supply knowledge and update guidance, not universal enforcement. Index summaries also influence relative relevance of page reads, supporting ranking authority at the proposer without a learned ranking algorithm. These effects are separate from the retained content's write agency ([MEM-OBJ-index](memory.md#mem-obj-index), [RT-RTE-skill-proposal](runtime.md#rt-rte-skill-proposal), [RT-BAP-skill-injection](runtime.md#rt-bap-skill-injection)). The current scalar threshold supplies the harness's gate, but it is ordinary loop state rather than an established accumulated retained criterion object. Its enforcing comparison is not attributed to model-read impact history.

The initial wiki/index/history supplies, stratified trace delivery and full skill injection are push. Requested `read_file` results are pull, even though a model chooses relevant pages using index summaries. Paths resolve those requests; no accepted record establishes targeted identifier-based push. Coarse outcome categories, availability and budgets remain coarse selectors ([RT-RTE-wiki-maintenance](runtime.md#rt-rte-wiki-maintenance), [RT-RTE-task-execution](runtime.md#rt-rte-task-execution)). Alternative inference wiki access has an unresolved selector, so its signal is not inapplicable. Separate PURPOSE.md delivery is also unresolved, rather than inferred from its rationale role ([MEM-OBJ-purpose](memory.md#mem-obj-purpose), [MEM-BAP-wiki-guidance](memory.md#mem-bap-wiki-guidance)).

### Transformations and trace-fed writes

Condensed index/log views support consolidation; explicit patches/refinements support evolution. Skill rollback withdraws active reliance while retaining the failed intervention in history, supporting bounded invalidation rather than wiki-wide retraction. These are declared transformations, not executed curation observations. No-duplicate instructions alone establish no semantic deduplication. Requested root causes and novel remedies cannot establish synthesis when the accepted content-edge assessment remains indeterminate ([EPI-RTE-wiki-formulation](epistemic.md#epi-rte-wiki-formulation), [EPI-CLM-knowledge-growth](epistemic.md#epi-clm-knowledge-growth), [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate)).

The trace-learning positives follow automatic trace/feedback-to-durable-artifact-to-later-consumer chains, including wiki views, procedures and retained intervention feedback. They do not require new propositions, parameter updates or observed improvement. Archiving raw traces alone is not a qualifying update. The original training experience includes linked trajectories and recorded tool activity; fixed benchmark references do not become traces merely because they enter the same update context. Validation feedback has a described rollout origin without an established persisted raw validation archive ([MEM-OBJ-raw](memory.md#mem-obj-raw), [EPI-RTE-impact-retention](epistemic.md#epi-rte-impact-retention)). No complete negative is derived from an unresolved companion or provider branch.

### Supersessions and disagreement

Reconciliation supersedes the seven epistemic duplicate object IDs with the corresponding memory IDs: raw traces, wiki patterns, wiki index, evolution log, skill impact, skill content and skill purpose. Every profile object citation uses the canonical memory declaration. Supersession connects identity and keeps both analysts' findings; it does not upgrade evidence or erase unresolved consumers. The epistemic imported-evidence/produced-prediction parts and the diagnostic, formulation, retention, scoring, disposition and integration phases remain distinct records, not superseded runtime containers.

Reconciliation retains one delivery disagreement: [RT-RTE-validation-gate](runtime.md#rt-rte-validation-gate) describes later proposer/maintainer history contexts, whereas [MEM-OBJ-skill-impact](memory.md#mem-obj-skill-impact) and [EPI-RTE-impact-retention](epistemic.md#epi-rte-impact-retention) leave necessarily complete maintainer tracker supply unresolved. The profile retains the positive proposer route and an unresolved maintainer unit; it selects neither side as a complete joint delivery fact. Unified diffs versus full rejected-content wording also cannot establish reconstructable whole files. The log-name ambiguity changes no files finding, while companion delivery/patch/rollback uncertainty prevents a complete authority or consumption account.

### Source-read log

No source files were read. Classification used only the supplied accepted runtime, memory, epistemic and workflow members and their reconciliation. No additional evidence, quotations or records were introduced; no report verification was reopened.
