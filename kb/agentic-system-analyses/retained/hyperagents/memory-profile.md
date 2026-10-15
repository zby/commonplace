---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Hyperagents memory profile: executable lineage, evaluation archives, trace-derived DGM guidance and Genesis policy checkpoints, with opaque alternatives retained."
run-id: "AAS-2026-10-14-hyperagents-dd9d501b160c-01"
source-identity: "https://github.com/facebookresearch/Hyperagents"
reviewed-boundary: "59a68f672dfb92c74aeb7e61535d776fb36e172d"
memory-comparison:
  version: 2
  scope: "Through-use retained executable lineage and reconstructed repositories; archive/control metadata; task predictions, grading and evaluation reports; interaction/episode/test artifacts; DGM derived guidance; Genesis generated reward code, saved configurations and learned checkpoint state; their admission, maintenance and later-consumer paths. Includes unresolved bootstrap provenance, checkpoint ancillary parts, environment-context/transfer detail and possible provider retention. Excludes unchanged shipped README/tool instructions, fixed provider weights as such, fresh conversation accumulation and process-local undo/inference tensors; source availability is not evidence of through-use memory."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Generation patches and reconstructed executable lineage"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-model-patch"
              note: "Saved diff files retain the changes."
            - value: "repo"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-model-patch"
                - "runtime.md#rt-bap-code-replay"
              note: "Reconstructed and committed Git worktrees retain inherited executable state."
          records:
            - "runtime.md#rt-obj-model-patch"
            - "runtime.md#rt-bap-code-replay"
          note: "Both persisted patch carriers and their repository reconstruction are included; current subprocess memory is not another retained substrate."
        - scope: "Local metadata, prediction/report/grade files, raw interaction and episode artifacts, reward code and saved configurations"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-metadata"
                - "memory.md#mem-obj-predictions"
                - "memory.md#mem-obj-report"
                - "memory.md#mem-obj-chat-history"
                - "memory.md#mem-obj-episode-log"
                - "memory.md#mem-obj-reward-function"
                - "memory.md#mem-obj-cfgs"
                - "epistemic.md#epi-obj-proof-grades"
              note: "JSON/JSONL, CSV, Markdown, images, Python and pickle are file encodings, not additional storage technologies."
          records:
            - "runtime.md#rt-obj-metadata"
            - "memory.md#mem-obj-predictions"
            - "memory.md#mem-obj-report"
            - "memory.md#mem-obj-chat-history"
            - "memory.md#mem-obj-episode-log"
            - "memory.md#mem-obj-reward-function"
            - "memory.md#mem-obj-cfgs"
            - "epistemic.md#epi-obj-proof-grades"
          note: "The records locate these parts in generated worktrees or output directories, including copied bootstrap files."
        - scope: "Genesis retained policy checkpoint carrier"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-policy-runner"
              note: "The evaluator loads a local model_{ckpt}.pt checkpoint; no run-produced checkpoint was supplied."
          records:
            - "runtime.md#rt-cmp-policy-runner"
          note: "The local file substrate is known independently of opaque checkpoint fields; active inference tensors are current computation, not an additional retained store."
        - scope: "Provider-side retained state, if any"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-provider-models"
          note: "Provider weights and hidden retention are opaque; API inference does not determine a controlled substrate for any through-use provider memory."
      records:
        - "runtime.md#rt-obj-model-patch"
        - "runtime.md#rt-bap-code-replay"
        - "runtime.md#rt-obj-metadata"
        - "memory.md#mem-obj-predictions"
        - "memory.md#mem-obj-report"
        - "memory.md#mem-obj-chat-history"
        - "memory.md#mem-obj-episode-log"
        - "memory.md#mem-obj-reward-function"
        - "memory.md#mem-obj-cfgs"
        - "epistemic.md#epi-obj-proof-grades"
        - "runtime.md#rt-cmp-policy-runner"
        - "runtime.md#rt-cmp-provider-models"
      note: "Local retained carriers are classified, including the dependency-controlled checkpoint file. Opaque provider-side retention prevents complete inventory coverage; model-weights is not inferred merely from parametric content."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Executable lineage/reward/solution patches and fixed-rule control, configuration, outcome and keyed-answer parts"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-model-patch"
                - "runtime.md#rt-obj-metadata"
                - "memory.md#mem-obj-reward-function"
                - "memory.md#mem-obj-cfgs"
                - "memory.md#mem-obj-predictions"
                - "memory.md#mem-obj-episode-log"
                - "memory.md#mem-obj-report"
                - "epistemic.md#epi-obj-proof-grades"
              note: "Python/diffs, flags, IDs, configuration fields, numerical reports and label comparisons have fixed-rule consumers."
          records:
            - "runtime.md#rt-obj-model-patch"
            - "runtime.md#rt-obj-metadata"
            - "memory.md#mem-obj-reward-function"
            - "memory.md#mem-obj-cfgs"
            - "memory.md#mem-obj-predictions"
            - "memory.md#mem-obj-episode-log"
            - "memory.md#mem-obj-report"
            - "epistemic.md#epi-obj-proof-grades"
          note: "This unit excludes prose literals interpreted by models, image payloads and the numerical checkpoint; CSV and pickle alone do not classify payload semantics."
        - scope: "Retained answer/proof prose, conversation text, observations, stdout and DGM implementation statement at model/text consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-predictions"
                - "memory.md#mem-obj-chat-history"
                - "memory.md#mem-obj-episode-log"
                - "memory.md#mem-rte-dgm-diagnosis"
                - "epistemic.md#epi-rte-proof-grading"
              note: "Answer/proof content, logged prose and the extracted DGM statement are interpreted as text; DGM delivers its statement to the editor."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-history"
                - "memory.md#mem-rte-dgm-diagnosis"
              note: "Serialized tool-call structure and extracted JSON keys have parsing consumers distinct from their prose payload."
          records:
            - "memory.md#mem-obj-predictions"
            - "memory.md#mem-obj-chat-history"
            - "memory.md#mem-obj-episode-log"
            - "memory.md#mem-rte-dgm-diagnosis"
            - "epistemic.md#epi-rte-proof-grading"
          note: "Raw tool calls are separated from interpreted prose; ordinary archive-to-model reading remains an affordance, not demonstrated operation."
        - scope: "Genesis checkpoint policy parameters at inference"
          assessment: "partial"
          findings:
            - value: "parametric"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-policy-runner"
              note: "Loaded numerical policy state supplies actions through get_inference_policy and policy(obs)."
          records:
            - "runtime.md#rt-cmp-policy-runner"
          note: "Distributed policy parameters are supported, but optimizer/auxiliary checkpoint fields and their consumers are uninspected; cfgs.pkl is classified separately."
        - scope: "Episode image payloads"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-episode-log"
          note: "Images are retained, but the record establishes no controlled form at an operative image consumer; symbolic filenames do not classify image content."
        - scope: "Opaque provider-side through-use content"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-provider-models"
          note: "Provider model parameters are parametric as a runtime component, but through-use retained content and its consumer are not inspected."
      records:
        - "runtime.md#rt-obj-model-patch"
        - "runtime.md#rt-obj-metadata"
        - "memory.md#mem-obj-reward-function"
        - "memory.md#mem-obj-cfgs"
        - "memory.md#mem-obj-predictions"
        - "memory.md#mem-obj-episode-log"
        - "memory.md#mem-obj-report"
        - "epistemic.md#epi-obj-proof-grades"
        - "memory.md#mem-obj-chat-history"
        - "memory.md#mem-rte-dgm-diagnosis"
        - "epistemic.md#epi-rte-proof-grading"
        - "runtime.md#rt-cmp-policy-runner"
        - "runtime.md#rt-cmp-provider-models"
      note: "Mixed text, fixed-rule structures and numerical policy state retain separate consumption paths. Images, ancillary checkpoint payload and provider retention prevent a complete form inventory."
    lineage:
      assessment: "partial"
      units:
        - scope: "New model-authored code patches, task answers and generated reward code"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-editor-admission"
                - "memory.md#mem-obj-predictions"
                - "memory.md#mem-obj-reward-function"
              note: "Models propose these retained contents, while software handles admission and persistence."
          records:
            - "runtime.md#rt-rte-editor-admission"
            - "memory.md#mem-obj-predictions"
            - "memory.md#mem-obj-reward-function"
          note: "Authorship is not a human approval claim and does not establish that ordinary edits depend on archive evidence."
        - scope: "Copied bootstrap evaluations and imported dataset/configuration material"
          assessment: "partial"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-predictions"
                - "memory.md#mem-obj-cfgs"
                - "memory.md#mem-obj-report"
              note: "Dataset rows, precomputed bootstrap evaluations and saved environment/training configurations enter from existing content."
          records:
            - "memory.md#mem-obj-predictions"
            - "memory.md#mem-obj-cfgs"
            - "memory.md#mem-obj-report"
          note: "The copy/import path is known; original evaluation provenance, content approval and initialization history are unresolved."
        - scope: "Host-authored lineage/access metadata"
          assessment: "known"
          findings:
            - value: "authored"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-metadata"
              note: "Host software creates and updates run IDs, patch paths, validity flags and archive snapshots."
          records:
            - "runtime.md#rt-obj-metadata"
          note: "The control record is authored by software; measured reports remain a separate derivation path."
        - scope: "Raw interaction and episode/test records and derived report/grade summaries"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-chat-history"
                - "memory.md#mem-obj-episode-log"
                - "memory.md#mem-obj-report"
                - "epistemic.md#epi-obj-proof-grades"
                - "epistemic.md#epi-rte-outcome-summary"
                - "epistemic.md#epi-rte-label-scoring"
              note: "Logging and report programs retain interactions, execution outcomes and measurements derived from those outcomes."
          records:
            - "memory.md#mem-obj-chat-history"
            - "memory.md#mem-obj-episode-log"
            - "memory.md#mem-obj-report"
            - "epistemic.md#epi-obj-proof-grades"
            - "epistemic.md#epi-rte-outcome-summary"
            - "epistemic.md#epi-rte-label-scoring"
          note: "This classifies the recorded runtime derivation, not the truth or original provenance of dataset references or external grader internals."
        - scope: "DGM derived implementation/problem statement"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
              note: "Selected saved failure evidence feeds diagnosis and extraction of fields for a later editor."
            - value: "authored"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
              note: "A model authors the diagnosis and proposed implementation text; it is not a verbatim trace replay."
          records:
            - "memory.md#mem-rte-dgm-diagnosis"
          note: "These findings name distinct aspects of the recorded derivation, not observed success or evidence that the proposed explanation is correct."
        - scope: "Genesis learned policy derivation"
          assessment: "partial"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-policy-runner"
                - "runtime.md#rt-rte-domain-effects"
              note: "The shipped rollout training call feeds experience to a runner intended to update retained policy parameters."
          records:
            - "runtime.md#rt-cmp-policy-runner"
            - "runtime.md#rt-rte-domain-effects"
          note: "The training-to-checkpoint-to-inference route is wired; initial parameter provenance, optimizer state and precise dependency transformation are uninspected."
        - scope: "Provider-side through-use retention provenance"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-provider-models"
          note: "No provider-side write or derivation is established by the API call."
      records:
        - "runtime.md#rt-rte-editor-admission"
        - "memory.md#mem-obj-predictions"
        - "memory.md#mem-obj-reward-function"
        - "memory.md#mem-obj-cfgs"
        - "memory.md#mem-obj-report"
        - "runtime.md#rt-obj-metadata"
        - "memory.md#mem-obj-chat-history"
        - "memory.md#mem-obj-episode-log"
        - "epistemic.md#epi-obj-proof-grades"
        - "epistemic.md#epi-rte-outcome-summary"
        - "epistemic.md#epi-rte-label-scoring"
        - "memory.md#mem-rte-dgm-diagnosis"
        - "runtime.md#rt-cmp-policy-runner"
        - "runtime.md#rt-rte-domain-effects"
        - "runtime.md#rt-cmp-provider-models"
      note: "Known authored, imported and trace-derived paths coexist. Unknown bootstrap origins, policy initialization/dependency payload and provider retention preclude complete lineage classification; no other-compiled path is established."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Inherited executable lineage and reward code at Python/training consumers"
          assessment: "partial"
          findings:
            - value: "instruction"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-model-patch"
                - "runtime.md#rt-bap-code-replay"
                - "memory.md#mem-obj-reward-function"
              note: "Retained executable code supplies standing program directions to later Python imports/task/editor execution and reward computation; its force is executable, not advisory prose."
          records:
            - "runtime.md#rt-obj-model-patch"
            - "runtime.md#rt-bap-code-replay"
            - "memory.md#mem-obj-reward-function"
          note: "Instruction includes symbolic program directions here. Descendant code can change tools, admission or selectors; the records do not enumerate every possible descendant effect, so no universal enforcement or validation guarantee is assigned to code."
        - scope: "Metadata flags and lineage IDs at host and editable-selector control consumers"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-selector-flags"
                - "runtime.md#rt-obj-metadata"
                - "runtime.md#rt-rte-optional-consumers"
              note: "Validity flags veto ordinary parent or selector-source reuse, subject to starting-node/fallback exceptions."
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-selector-flags"
                - "runtime.md#rt-obj-metadata"
                - "runtime.md#rt-rte-parent-selection"
              note: "The retained validity flags supply eligibility criteria checked before candidate admission."
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-metadata"
                - "runtime.md#rt-rte-parent-selection"
                - "runtime.md#rt-bap-code-replay"
              note: "IDs and ordered patch paths determine resume state, selected lineage and replay inputs."
            - value: "ranking"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-parent-selection"
                - "runtime.md#rt-obj-metadata"
              note: "Retained child links influence score-and-child-count selection priority."
          records:
            - "runtime.md#rt-bap-selector-flags"
            - "runtime.md#rt-obj-metadata"
            - "runtime.md#rt-rte-optional-consumers"
            - "runtime.md#rt-rte-parent-selection"
            - "runtime.md#rt-bap-code-replay"
          note: "Criteria, vetoes, routing and ranking are separate actual consumers/effects. Archive membership is not certification of success."
        - scope: "Saved numerical reports at score, staged-gate and ensemble consumers"
          assessment: "known"
          findings:
            - value: "ranking"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "runtime.md#rt-rte-parent-selection"
                - "runtime.md#rt-rte-optional-consumers"
              note: "Retained domain scores influence relative parent/ensemble priority."
            - value: "validation"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "runtime.md#rt-rte-parent-selection"
              note: "Score presence and positive staged scores determine eligibility for candidate selection or fuller evaluation."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "runtime.md#rt-rte-parent-selection"
              note: "Missing/nonpositive scores can exclude candidates or suppress fuller evaluation on the recorded gated paths."
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-report"
                - "runtime.md#rt-rte-parent-selection"
                - "runtime.md#rt-rte-optional-consumers"
              note: "Selected scores determine which lineage or saved-answer source proceeds."
          records:
            - "memory.md#mem-obj-report"
            - "runtime.md#rt-rte-parent-selection"
            - "runtime.md#rt-rte-optional-consumers"
          note: "These effects are bounded by mode and fallback; they license neither explanation acceptance nor unseen-split generalization."
        - scope: "Saved answers and completed-result records at reuse, scoring and proof-grading consumers"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-predictions"
                - "epistemic.md#epi-rte-proof-grading"
                - "runtime.md#rt-rte-optional-consumers"
              note: "Saved answers supply candidate/reference context to grading or become returned ensemble answers; no correctness endorsement is implied."
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-rte-prediction-reuse"
                - "memory.md#mem-obj-episode-log"
              note: "Non-NA predictions and existing result records choose skip-versus-execute branches."
            - value: "enforcement"
              basis: "wired"
              records:
                - "memory.md#mem-rte-prediction-reuse"
                - "memory.md#mem-obj-episode-log"
              note: "The reuse branches suppress a fresh task call or test execution."
          records:
            - "memory.md#mem-obj-predictions"
            - "epistemic.md#epi-rte-proof-grading"
            - "runtime.md#rt-rte-optional-consumers"
            - "memory.md#mem-rte-prediction-reuse"
            - "memory.md#mem-obj-episode-log"
          note: "The stored answer is consumed directly rather than delivered as a fresh task-model conversation; report comparisons do not turn the answer itself into a validation criterion."
        - scope: "Historical traces/reports at DGM diagnosis and the extracted statement at the next editor"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
                - "memory.md#mem-obj-chat-history"
                - "memory.md#mem-obj-episode-log"
              note: "Retained failed-case experience feeds an automatic update to implementation guidance and potentially durable executable behavior."
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
              note: "Saved task/report/log content supplies evidence and context to the diagnosis model."
            - value: "instruction"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
              note: "Extracted implementation/problem text enters the coding-agent instruction."
          records:
            - "memory.md#mem-rte-dgm-diagnosis"
            - "memory.md#mem-obj-chat-history"
            - "memory.md#mem-obj-episode-log"
          note: "Update-consumer learning authority is separate from downstream instruction authority; neither means improved capacity."
        - scope: "Ordinary archive files at a tool-reading editor"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-archive-delivery"
              note: "Surviving historical artifacts can supply evidence after a model requests a file; filesystem copy alone is not model consumption."
          records:
            - "memory.md#mem-rte-archive-delivery"
          note: "No wired evidence-responsive ordinary code update is inferred from availability."
        - scope: "Genesis saved configuration and learned policy at evaluation"
          assessment: "partial"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-cfgs"
              note: "Deserialized configuration selects the environment/runner setup used for later evaluation."
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-policy-runner"
              note: "Loaded policy state selects actions through policy(obs), and those actions are passed to env.step; the retained parameters are not localized prose instructions."
          records:
            - "memory.md#mem-obj-cfgs"
            - "runtime.md#rt-cmp-policy-runner"
          note: "Configuration routes evaluation setup; retained policy parameters route action choice at the environment consumer. Ancillary checkpoint fields and optimizer consumers remain opaque."
        - scope: "Detailed transfer/analysis consumers and full environment-context derivation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-episode-log"
            - "memory.md#mem-obj-report"
            - "runtime.md#rt-rte-domain-effects"
          note: "Recorded score/plot readers and environment context do not determine every retained-part effect in the uninspected transformations."
        - scope: "Provider hidden-retention authority"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-provider-models"
          note: "No through-use retained part or downstream force is inspectable."
      records:
        - "runtime.md#rt-obj-model-patch"
        - "runtime.md#rt-bap-code-replay"
        - "memory.md#mem-obj-reward-function"
        - "runtime.md#rt-bap-selector-flags"
        - "runtime.md#rt-obj-metadata"
        - "runtime.md#rt-rte-optional-consumers"
        - "runtime.md#rt-rte-parent-selection"
        - "memory.md#mem-obj-report"
        - "memory.md#mem-obj-predictions"
        - "epistemic.md#epi-rte-proof-grading"
        - "memory.md#mem-rte-prediction-reuse"
        - "memory.md#mem-obj-episode-log"
        - "memory.md#mem-rte-dgm-diagnosis"
        - "memory.md#mem-obj-chat-history"
        - "memory.md#mem-rte-archive-delivery"
        - "memory.md#mem-obj-cfgs"
        - "runtime.md#rt-cmp-policy-runner"
        - "runtime.md#rt-rte-domain-effects"
        - "runtime.md#rt-cmp-provider-models"
      note: "The inventory separates code execution, control vetoes, score ranking, answer reuse and trace-fed updates. Opaque checkpoint/provider parts and incomplete transfer/environment routes prevent a complete authority inventory."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Model code/reward/answer proposals admitted by shipped software"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-editor-admission"
                - "memory.md#mem-obj-reward-function"
                - "memory.md#mem-obj-predictions"
              note: "Model/software admission has no per-content human approval; an operator starting a run does not make each change manual."
          records:
            - "runtime.md#rt-rte-editor-admission"
            - "memory.md#mem-obj-reward-function"
            - "memory.md#mem-obj-predictions"
          note: "This covers the ordinary proposal/extraction/diff admissions, not unknown replacement of initial files."
        - scope: "Host metadata, logging, prediction checkpoints, reports, configurations and DGM statement admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-metadata"
                - "memory.md#mem-obj-chat-history"
                - "memory.md#mem-obj-episode-log"
                - "memory.md#mem-obj-report"
                - "memory.md#mem-obj-cfgs"
                - "memory.md#mem-rte-prediction-reuse"
                - "memory.md#mem-rte-dgm-diagnosis"
              note: "Host/harness/logger programs save or replace content, and diagnosis fields are adopted without a human content decision."
          records:
            - "runtime.md#rt-obj-metadata"
            - "memory.md#mem-obj-chat-history"
            - "memory.md#mem-obj-episode-log"
            - "memory.md#mem-obj-report"
            - "memory.md#mem-obj-cfgs"
            - "memory.md#mem-rte-prediction-reuse"
            - "memory.md#mem-rte-dgm-diagnosis"
          note: "Physical I/O and model authorship are not substituted for admission control."
        - scope: "Genesis rollout training and checkpoint production through the runner"
          assessment: "partial"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-policy-runner"
                - "runtime.md#rt-rte-domain-effects"
              note: "Software launches learning and later loads dependency-produced checkpoints without per-checkpoint human approval."
          records:
            - "runtime.md#rt-cmp-policy-runner"
            - "runtime.md#rt-rte-domain-effects"
          note: "The integrated training route is automatic; initialization and any separately supplied/replaced checkpoint admission are not established."
        - scope: "Original bootstrap-file and separately replaced checkpoint admission"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-report"
            - "runtime.md#rt-cmp-policy-runner"
          note: "Copying a file and selecting a checkpoint do not establish who originally approved or replaced its content; no manual finding follows from operator workflow initiation."
        - scope: "Provider-side retained-state writes"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-provider-models"
          note: "Provider inference exposes neither write/admission mechanisms nor human control."
      records:
        - "runtime.md#rt-rte-editor-admission"
        - "memory.md#mem-obj-reward-function"
        - "memory.md#mem-obj-predictions"
        - "runtime.md#rt-obj-metadata"
        - "memory.md#mem-obj-chat-history"
        - "memory.md#mem-obj-episode-log"
        - "memory.md#mem-obj-report"
        - "memory.md#mem-obj-cfgs"
        - "memory.md#mem-rte-prediction-reuse"
        - "memory.md#mem-rte-dgm-diagnosis"
        - "runtime.md#rt-cmp-policy-runner"
        - "runtime.md#rt-rte-domain-effects"
        - "runtime.md#rt-cmp-provider-models"
      note: "Automatic admissions are supported locally. Original bootstrap/checkpoint control and provider writes are unresolved, so neither a manual value nor complete automatic-only coverage is asserted."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Retained executable lineage revisions"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-editor-admission"
                - "runtime.md#rt-obj-model-patch"
                - "runtime.md#rt-bap-code-replay"
              note: "The editor changes inherited code and saves a new diff for later replay, revising existing behavior-bearing material."
          records:
            - "runtime.md#rt-rte-editor-admission"
            - "runtime.md#rt-obj-model-patch"
            - "runtime.md#rt-bap-code-replay"
          note: "The implemented revision route establishes evolution, not actual improvement or semantic correctness."
        - scope: "Parent and editable-selector invalidation"
          assessment: "known"
          findings:
            - value: "invalidate"
              basis: "wired"
              records:
                - "runtime.md#rt-bap-selector-flags"
                - "runtime.md#rt-rte-optional-consumers"
                - "runtime.md#rt-obj-metadata"
              note: "Failure changes validity/reuse flags while archived patches and results remain retained."
          records:
            - "runtime.md#rt-bap-selector-flags"
            - "runtime.md#rt-rte-optional-consumers"
            - "runtime.md#rt-obj-metadata"
          note: "This withdraws current reliance without requiring physical deletion; it is not decay or deduplication."
        - scope: "DGM extraction of the generated diagnosis into retained implementation/problem fields"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
              note: "The full diagnosis is logged, while selected fields form a reduced statement delivered to the later editor."
          records:
            - "memory.md#mem-rte-dgm-diagnosis"
          note: "The supported transformation is selection of existing diagnosis fields; this finding does not classify the semantics of diagnosis generation itself."
        - scope: "DGM diagnosis-generation semantics and ordinary model-mediated archive maintenance"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-dgm-diagnosis"
            - "memory.md#mem-rte-archive-delivery"
          note: "Prompts request improvement and models may reshape or conjecture; accepted records do not establish whether diagnosis content preserves claims or creates new ones. Synthesize is therefore not assigned."
        - scope: "Dependency policy/checkpoint transformations and detailed transfer maintenance"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-policy-runner"
            - "memory.md#mem-obj-report"
          note: "Training changes parameters, but the dependency payload/optimizer and detailed transfer transformations are uninspected; no additional controlled curation operation is established."
        - scope: "Provider-side retention/compaction"
          assessment: "uninspected"
          findings: []
          records:
            - "runtime.md#rt-cmp-provider-models"
          note: "Output-context retry is not evidence of provider compaction or any other maintenance operation."
      records:
        - "runtime.md#rt-rte-editor-admission"
        - "runtime.md#rt-obj-model-patch"
        - "runtime.md#rt-bap-code-replay"
        - "runtime.md#rt-bap-selector-flags"
        - "runtime.md#rt-rte-optional-consumers"
        - "runtime.md#rt-obj-metadata"
        - "memory.md#mem-rte-dgm-diagnosis"
        - "memory.md#mem-rte-archive-delivery"
        - "runtime.md#rt-cmp-policy-runner"
        - "memory.md#mem-obj-report"
        - "runtime.md#rt-cmp-provider-models"
      note: "Evolution, invalidation and field consolidation have separate witnesses. Copy pruning, index/key lookup, raw logging, score acquisition and worktree cleanup are not independently classified as memory curation; unresolved semantic and opaque branches remain included."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Foreground tool reads of surviving archive files"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-archive-delivery"
                - "runtime.md#rt-rte-model-tools"
              note: "The foreground model requests a file/range; the tool fulfills that request with surviving retained content."
          records:
            - "memory.md#mem-rte-archive-delivery"
            - "runtime.md#rt-rte-model-tools"
          note: "Automatic filesystem exposure and requested model-text delivery are separate operations; clipped tool output does not make the requested return push."
        - scope: "Scheduled archive exposure and selected executable-lineage reconstruction"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-archive-delivery"
                - "runtime.md#rt-rte-parent-selection"
                - "runtime.md#rt-bap-code-replay"
              note: "The host automatically copies historical artifacts and supplies selected inherited code to later invocations without a foreground request for those contents."
          records:
            - "memory.md#mem-rte-archive-delivery"
            - "runtime.md#rt-rte-parent-selection"
            - "runtime.md#rt-bap-code-replay"
          note: "The pruned filesystem view is wired; use of its text by a model remains afforded."
        - scope: "Scheduled resume/control/report consumption and prediction/result reuse"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-metadata"
                - "runtime.md#rt-rte-parent-selection"
                - "memory.md#mem-obj-report"
                - "memory.md#mem-rte-prediction-reuse"
                - "memory.md#mem-obj-episode-log"
              note: "Host/harness consumers request retained metadata, reports or result files."
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-prediction-reuse"
                - "memory.md#mem-obj-episode-log"
              note: "Harness reuse automatically inserts available keyed answers/results and bypasses fresh computation without a task-agent request for those prior contents."
          records:
            - "runtime.md#rt-obj-metadata"
            - "runtime.md#rt-rte-parent-selection"
            - "memory.md#mem-obj-report"
            - "memory.md#mem-rte-prediction-reuse"
            - "memory.md#mem-obj-episode-log"
          note: "Reads fulfilling a program request are distinguished from the automatic reuse decision and downstream supply."
        - scope: "Optional ensemble answer requests and wrapper archive supply"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-optional-consumers"
                - "memory.md#mem-obj-predictions"
              note: "The default ensemble fulfills a requested question/split by selecting and returning a saved prediction."
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-optional-consumers"
              note: "The wrapper supplies its copied archive to the inherited selector/ensemble invocation automatically."
          records:
            - "runtime.md#rt-rte-optional-consumers"
            - "memory.md#mem-obj-predictions"
          note: "The score choice and question-ID lookup within an answer request are not counted as extra pushes merely because code returns an answer."
        - scope: "DGM automatic evidence selection and statement delivery"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
              note: "The diagnosis builder reads saved reports/logs."
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
              note: "The host selects failed-case material for a diagnosis call and delivers extracted implementation text to a new editor frame."
          records:
            - "memory.md#mem-rte-dgm-diagnosis"
          note: "Inputs are selected independently of a foreground request for particular retained passages; extraction and model compliance remain distinct."
        - scope: "Genesis checkpoint/configuration read-back"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-policy-runner"
                - "memory.md#mem-obj-cfgs"
              note: "The evaluator requests saved configurations and a chosen checkpoint, then loads the inference policy."
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-domain-effects"
                - "memory.md#mem-obj-reward-function"
              note: "The training-success path automatically supplies the generated reward-code path to the subsequent evaluation workflow."
          records:
            - "runtime.md#rt-cmp-policy-runner"
            - "memory.md#mem-obj-cfgs"
            - "runtime.md#rt-rte-domain-effects"
            - "memory.md#mem-obj-reward-function"
          note: "A requested checkpoint filename alone is not targeted push selection."
        - scope: "Remaining environment-context, transfer and provider retention routes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-episode-log"
            - "memory.md#mem-obj-report"
            - "runtime.md#rt-cmp-provider-models"
          note: "Full environment-context derivation, detailed transfer consumers and provider retention were not inspected; their direction cannot be inferred from a known local route."
      records:
        - "memory.md#mem-rte-archive-delivery"
        - "runtime.md#rt-rte-model-tools"
        - "runtime.md#rt-rte-parent-selection"
        - "runtime.md#rt-bap-code-replay"
        - "runtime.md#rt-obj-metadata"
        - "memory.md#mem-obj-report"
        - "memory.md#mem-rte-prediction-reuse"
        - "memory.md#mem-obj-episode-log"
        - "runtime.md#rt-rte-optional-consumers"
        - "memory.md#mem-obj-predictions"
        - "memory.md#mem-rte-dgm-diagnosis"
        - "runtime.md#rt-cmp-policy-runner"
        - "memory.md#mem-obj-cfgs"
        - "runtime.md#rt-rte-domain-effects"
        - "memory.md#mem-obj-reward-function"
        - "runtime.md#rt-cmp-provider-models"
      note: "Both pull and push exist at different operations, often in one chain. Unresolved environment, transfer and provider alternatives prevent complete direction coverage or a pull-only conclusion."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Scheduled ordinary archive filesystem push and optional-wrapper archive supply"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-archive-delivery"
                - "runtime.md#rt-rte-optional-consumers"
              note: "Trigger: generation/wrapper launch. Inputs: prior-tree availability, current ID, filename/split rules or parent-only mode. Selected part: surviving archive subtree or complete optional archive."
          records:
            - "memory.md#mem-rte-archive-delivery"
            - "runtime.md#rt-rte-optional-consumers"
          note: "Filename pruning and mode availability select broad views, not semantically relevant passages; no archive-wide token budget is established."
        - scope: "Next-parent executable lineage push"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-parent-selection"
              note: "Trigger: bootstrap/resume or generation completion. Inputs: flags, scores, child counts and selected mode. Selected part: candidate lineage under random/latest/score weighting and fallback."
            - value: "identifier"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-metadata"
                - "runtime.md#rt-rte-parent-selection"
                - "runtime.md#rt-bap-code-replay"
              note: "After parent choice, the chosen generation ID matches metadata containing the ordered patch paths, selecting the actual retained code replayed into the next invocation."
          records:
            - "runtime.md#rt-obj-metadata"
            - "runtime.md#rt-rte-parent-selection"
            - "runtime.md#rt-bap-code-replay"
          note: "Candidate priority and the subsequent identity match are separate selectors; a path merely appearing in metadata would not by itself establish the latter."
        - scope: "Automatic completed-answer/result reuse"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-prediction-reuse"
                - "memory.md#mem-obj-predictions"
                - "memory.md#mem-obj-episode-log"
              note: "Trigger: harness resume/repeated invocation. Inputs: current question or instance ID plus completion/file availability. Selected part: matching saved prediction or per-instance JSON."
          records:
            - "memory.md#mem-rte-prediction-reuse"
            - "memory.md#mem-obj-predictions"
            - "memory.md#mem-obj-episode-log"
          note: "The retained match enters the output/skip branch automatically, not a new task-agent request."
        - scope: "DGM failed-case evidence push and reduced-statement delivery"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
              note: "Trigger: optional DGM run. Inputs: random domain and failure/nonperfect outcomes. Selected part: a failed-case evidence bundle, then fixed implementation/problem fields with prefix caps."
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
              note: "Failure IDs or episode identities select the corresponding saved task/log/CSV material used by diagnosis."
          records:
            - "memory.md#mem-rte-dgm-diagnosis"
          note: "The diagnosed proposal is not an inferred-judgment retrieval selector; its new content and extraction are downstream transformations."
        - scope: "Genesis post-training reward-code evaluation handoff"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-domain-effects"
                - "memory.md#mem-obj-reward-function"
              note: "Trigger: training_success. Input: that success flag. Selected part: the generated reward artifact for the completed training trial, forwarded to evaluation."
          records:
            - "runtime.md#rt-rte-domain-effects"
            - "memory.md#mem-obj-reward-function"
          note: "The forwarded path alone is not an identifier-match signal; checkpoint/config requests are pull operations."
        - scope: "Unresolved environment/transfer/provider push alternatives"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-episode-log"
            - "memory.md#mem-obj-report"
            - "runtime.md#rt-cmp-provider-models"
          note: "Direction and selectors are unknown on these included alternatives; inspected pull routes cannot make their signal inapplicable."
      records:
        - "memory.md#mem-rte-archive-delivery"
        - "runtime.md#rt-rte-optional-consumers"
        - "runtime.md#rt-obj-metadata"
        - "runtime.md#rt-rte-parent-selection"
        - "runtime.md#rt-bap-code-replay"
        - "memory.md#mem-rte-prediction-reuse"
        - "memory.md#mem-obj-predictions"
        - "memory.md#mem-obj-episode-log"
        - "memory.md#mem-rte-dgm-diagnosis"
        - "runtime.md#rt-rte-domain-effects"
        - "memory.md#mem-obj-reward-function"
        - "memory.md#mem-obj-report"
        - "runtime.md#rt-cmp-provider-models"
      note: "Coarse availability/performance filtering and actual identity matches are supported locally. Requested file/checkpoint/ensemble lookups are not used as additional push witnesses. Uninspected alternatives prevent complete selector coverage."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "DGM failure traces to logged implementation statement and later coding-agent guidance"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
              note: "Automatic diagnosis uses saved experience, retains the diagnosis/derived fields and supplies extracted implementation guidance to a later editor; a resulting diff can persist into executable lineage."
          records:
            - "memory.md#mem-rte-dgm-diagnosis"
          note: "The qualifying write is behavior-shaping instruction production, not raw-log storage. A malformed retry limits recovery, not the initial successful branch; operation and capacity gain are unobserved."
        - scope: "Genesis rollout-fed retained policy parameters and later inference"
          assessment: "partial"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-policy-runner"
                - "runtime.md#rt-rte-domain-effects"
              note: "The shipped learning call wires experience-driven policy updates to checkpoint loading and action inference."
          records:
            - "runtime.md#rt-cmp-policy-runner"
            - "runtime.md#rt-rte-domain-effects"
          note: "The numerical route qualifies independently of natural-language claim acceptance. Exact optimizer/checkpoint payload and initialization are uninspected."
        - scope: "Ordinary history-informed durable code editing"
          assessment: "partial"
          findings:
            - value: "yes"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-archive-delivery"
                - "runtime.md#rt-rte-editor-admission"
              note: "Tools can expose retained prior experience to an editor that can save behavior-changing code for later replay."
          records:
            - "memory.md#mem-rte-archive-delivery"
            - "runtime.md#rt-rte-editor-admission"
          note: "Evidence-responsive ordinary update determination is afforded, not wired by archive copying; no actual historical read or trace-dependent edit is demonstrated."
        - scope: "Full environment-context adaptation, detailed transfer updates and provider hidden writes"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-episode-log"
            - "memory.md#mem-obj-report"
            - "runtime.md#rt-cmp-provider-models"
          note: "These included alternatives are not sufficiently inspected to determine qualifying durable automatic writes or their later consumers."
      records:
        - "memory.md#mem-rte-dgm-diagnosis"
        - "runtime.md#rt-cmp-policy-runner"
        - "runtime.md#rt-rte-domain-effects"
        - "memory.md#mem-rte-archive-delivery"
        - "runtime.md#rt-rte-editor-admission"
        - "memory.md#mem-obj-episode-log"
        - "memory.md#mem-obj-report"
        - "runtime.md#rt-cmp-provider-models"
      note: "At least DGM and Genesis wire qualifying trace-fed behavior-shaping outputs. Ordinary evidence-shaped editing has only an afforded witness. No bounded-absence record supports a local or system-wide no; raw logs, score reuse and checkpoint selection alone are not learning writes."
    trace_source:
      assessment: "partial"
      units:
        - scope: "DGM trace-fed implementation-guidance write"
          assessment: "partial"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
                - "memory.md#mem-obj-chat-history"
              note: "Selected failed-entry chat records contain recorded conversational inputs/outputs used by diagnosis."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
                - "memory.md#mem-obj-chat-history"
                - "memory.md#mem-obj-episode-log"
              note: "Diagnosis may consume logged tool results and Genesis execution/evaluation text."
            - value: "trajectories"
              basis: "wired"
              records:
                - "memory.md#mem-rte-dgm-diagnosis"
                - "memory.md#mem-obj-episode-log"
              note: "The BALROG branch reads failed-episode step/action/observation/reward sequences alongside chat."
          records:
            - "memory.md#mem-rte-dgm-diagnosis"
            - "memory.md#mem-obj-chat-history"
            - "memory.md#mem-obj-episode-log"
          note: "The input also includes static task/reference material and current code, which add no trace-source value. Exact content/provenance of specialized eval text and complete environment-origin context remain unresolved; no event-streams value is inferred from CSV serialization alone."
        - scope: "Genesis rollout-fed policy write"
          assessment: "partial"
          findings:
            - value: "trajectories"
              basis: "wired"
              records:
                - "runtime.md#rt-cmp-policy-runner"
                - "runtime.md#rt-rte-domain-effects"
              note: "Configured rollout training consumes simulated experience to update the retained policy later loaded for evaluation."
          records:
            - "runtime.md#rt-cmp-policy-runner"
            - "runtime.md#rt-rte-domain-effects"
          note: "The shipped integration supports a trajectory source; dependency internals do not establish all original inputs, auxiliary state or initialization."
        - scope: "Ordinary archive-informed code update affordance"
          assessment: "partial"
          findings:
            - value: "session-logs"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-archive-delivery"
                - "memory.md#mem-obj-chat-history"
              note: "Surviving recorded editor/task conversations are available for a tool-reading editor."
            - value: "tool-traces"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-archive-delivery"
                - "memory.md#mem-obj-chat-history"
                - "memory.md#mem-obj-episode-log"
              note: "Surviving interaction and subprocess/test logs can supply execution feedback to a durable code update."
            - value: "trajectories"
              basis: "afforded"
              records:
                - "memory.md#mem-rte-archive-delivery"
                - "memory.md#mem-obj-episode-log"
              note: "Episode action/observation/outcome sequences can be inspected when retained in the copied view."
          records:
            - "memory.md#mem-rte-archive-delivery"
            - "memory.md#mem-obj-chat-history"
            - "memory.md#mem-obj-episode-log"
          note: "These characterize available source content on the afforded qualifying update route, not a particular observed edit. Filename pruning and mixed payloads prevent an exhaustive trace-origin account."
        - scope: "Other environment/transfer/provider qualifying write inputs"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-episode-log"
            - "memory.md#mem-obj-report"
            - "runtime.md#rt-cmp-provider-models"
          note: "Unresolved trace-learning alternatives have unresolved source content; positives on DGM/Genesis cannot make this unit inapplicable."
      records:
        - "memory.md#mem-rte-dgm-diagnosis"
        - "memory.md#mem-obj-chat-history"
        - "memory.md#mem-obj-episode-log"
        - "runtime.md#rt-cmp-policy-runner"
        - "runtime.md#rt-rte-domain-effects"
        - "memory.md#mem-rte-archive-delivery"
        - "memory.md#mem-obj-report"
        - "runtime.md#rt-cmp-provider-models"
      note: "Original content, not the log adapter or file extension, establishes each value. Mixed static inputs add imported lineage, not event-streams. Dependency/provider and remaining environment/transfer uncertainty prevent complete source coverage."
---

# Hyperagents memory profile

## Comparison rationale

This revision-2 profile classifies accepted records, not source files or an
observed run. All positive findings retain the basis of the actual route.
No observed or causal basis is available. Each axis is partial because its
explicit inventory retains unresolved alternatives rather than promoting a
local witness into complete system coverage.

### Retained carriers and operative parts

[RT-OBJ-model-patch](runtime.md#rt-obj-model-patch) and
[RT-BAP-code-replay](runtime.md#rt-bap-code-replay) establish file retention
and repository reconstruction. Symbolic executable directions have instruction
authority at Python execution; they are not merely advisory model text.
This mapping does not assign every conceivable effect of generated code.
Reward code is a separate executable part, and checkpoint parameters are a
separate parametric part. The checkpoint file establishes files, not a
model-weights storage backend. Its opaque auxiliary payload stays unresolved
under [RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner).

The prediction CSV is not counted as identical to its answer cells. The
broader saved-report object is not identical to its label-agreement,
proof-grade or environment-summary parts. These distinctions preserve the
separate consumers in [MEM-OBJ-predictions](memory.md#mem-obj-predictions),
[MEM-OBJ-report](memory.md#mem-obj-report),
[EPI-OBJ-proof-grades](epistemic.md#epi-obj-proof-grades) and
[EPI-RTE-outcome-summary](epistemic.md#epi-rte-outcome-summary).
Reconciliation supplies no supersessions affecting any value; all citations
therefore retain their declaring identities. Overlap is not duplicate evidence
of a separate mechanism.

### Admission, authority and maintenance

Automatic describes admission without a per-content operator decision, not
whether a model authored the proposal or a human started the workflow.
Original bootstrap approval and separately supplied checkpoint admission remain
unknown even though subsequent software updates are known. Metadata criteria
can validate and veto reuse while the same IDs and paths route execution.
Scores rank candidates and gate continuation without certifying improvement;
starting-node exceptions and fallback remain part of that scope. See
[RT-BAP-selector-flags](runtime.md#rt-bap-selector-flags) and
[RT-RTE-parent-selection](runtime.md#rt-rte-parent-selection).

Evolution revises inherited code. Invalidation withdraws reliance while
preserving archive history. DGM field extraction consolidates the logged
diagnosis into a reduced implementation statement, but its diagnosis-generation
semantics do not establish synthesis. Copy pruning changes another invocation's
view, not the retained host archive. These are distinct operations in
[RT-RTE-editor-admission](runtime.md#rt-rte-editor-admission),
[MEM-RTE-dgm-diagnosis](memory.md#mem-rte-dgm-diagnosis) and
[MEM-RTE-archive-delivery](memory.md#mem-rte-archive-delivery).

### Selection and trace-fed updates

A foreground file request is pull. Automatic archive exposure and selected
lineage replay are push operations at a different stage. The normal copy's
coarse filename filtering is not a relevance selector. The selected-parent
identity match retrieves actual patch parts; prediction reuse similarly
matches current question IDs to retained answers. Conversely, a filename on
a requested checkpoint or the question-ID lookup fulfilling an ensemble
answer request does not independently establish identifier-based push. See
[MEM-RTE-prediction-reuse](memory.md#mem-rte-prediction-reuse) and
[RT-RTE-optional-consumers](runtime.md#rt-rte-optional-consumers).

The DGM write uses retained experience to generate logged guidance consumed
by another editor. Its update consumer gives traces learning authority; its
output supplies instruction authority. Genesis separately wires rollout-fed
numerical adaptation and checkpoint inference. These qualify for trace_learning
without observed improvement, accepted explanatory claims or a theory-builder
finding. Ordinary archive-informed editing remains afforded: copied evidence
is not automatically read by the model. Raw-log retention and score-based
reuse alone establish no additional qualifying update.

Session turns, recorded tool/execution feedback and linked episode experience
support different trace-source findings. Static task/reference inputs do not
become traces by being embedded in a diagnosis prompt. No event-streams value
is inferred solely from episode timestamps, CSV transport or a broad log label.
The DGM retry defect limits recovery, not the supported initial branch.
[MEM-RTE-dgm-diagnosis](memory.md#mem-rte-dgm-diagnosis) and
[RT-CMP-policy-runner](runtime.md#rt-cmp-policy-runner) retain these warrants.

### Coverage limits and source-read log

Unknown initial provenance prevents complete lineage and admission coverage.
Opaque checkpoint fields, provider retention, full environment-context
derivation and detailed transfer consumers prevent complete enumeration of
forms, authorities, transformations, directions and trace origins. Images are
not silently classified by their filenames. A known local route does not turn
these alternatives into absence or inapplicability. Unchanged shipped guidance
and fixed inference weights are excluded as such because the scope requires
through-use retention; possible provider-side writes remain explicitly included
as uninspected in [RT-CMP-provider-models](runtime.md#rt-cmp-provider-models).

No source files were read for this classification. The supplied accepted
members and reconciliation sufficed; no records, quotations, evidence sources
or verification judgments were added.
