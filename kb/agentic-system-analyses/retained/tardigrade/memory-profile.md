---
type: "agentic-system-analyses/types/agentic-system-memory-profile.md"
description: "Tardigrade memory profile: event-derived context, two summary generations, retained provider/file parts, workspaces, recovery state and prescribed trace-fed source revision."
run-id: "AAS-2026-10-15-tardigrade-455e1aaccd4d-01"
source-identity: "https://github.com/clavia-labs/tardigrade"
reviewed-boundary: "1b9f1e5760d1d4d4a63eb1f87af9e5a2341de7e8"
memory-comparison:
  version: 2
  scope: "Included: through-use event/conversation content, current and legacy derived summaries and control state, retained continuation payloads and attachment refs/bytes, effect checkpoints and adopted initial state, current named-text workspace, legacy spills/ref manifests, retained permission and output-rejection decisions, later-consumed installed actor revisions, and prescribed optimization candidate/source/evaluation lineage. Custom backends, opaque payload content, arbitrary caller provenance and uninspected host/maintenance alternatives remain included uncertainties. Excluded: external model weights/provider internals, remote dependency implementations, shipped unchanged static prompts/instructions as memory, ordinary transient work without a later retained consumer, and scratch SQL databases not established as a retained memory corpus. Optimization instructions are evidence of a prescribed memory route, not themselves accumulated memory."
  axes:
    storage_substrate:
      assessment: "partial"
      units:
        - scope: "Current event-backed trajectory, summaries/control state, continuation and content refs, permission/rejection decisions, recorded code outcomes, adopted state and effect checkpoints; configured SQL journal"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-obj-compaction-state"
                - "memory.md#mem-obj-provider-continuation"
                - "memory.md#mem-obj-effect-checkpoint"
              note: "Durable atoms and decoded prompt/checkpoint parts are held in reducer/runtime memory."
            - value: "sqlite"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-journal"
                - "runtime.md#rt-clm-request-before-execution"
                - "memory.md#mem-obj-effect-checkpoint"
              note: "The configured Bun and Cloudflare SQL journal retains events, inputs and checkpoint payloads; embedded content shares this substrate."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-obj-compaction-state"
            - "memory.md#mem-obj-provider-continuation"
            - "memory.md#mem-obj-content-parts"
            - "runtime.md#rt-obj-permission-policy"
            - "epistemic.md#epi-rte-response-check"
            - "runtime.md#rt-rte-code-execution"
            - "memory.md#mem-rte-state-adoption"
            - "memory.md#mem-obj-effect-checkpoint"
            - "runtime.md#rt-obj-journal"
            - "runtime.md#rt-clm-request-before-execution"
          note: "Classification covers the inspected configured journal and materialized projections, not every custom journal."
        - scope: "Legacy event-backed conversation and summary checkpoint in the shipped Bun server"
          assessment: "known"
          findings:
            - value: "sqlite"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-legacy-server"
                - "memory.md#mem-obj-compaction-completed"
                - "memory.md#mem-rte-legacy-compaction"
              note: "The older Bun host stores thread events; CompactionCompleted and its summary/boundary are retained in that event history."
          records:
            - "runtime.md#rt-rte-legacy-server"
            - "memory.md#mem-obj-compaction-completed"
            - "memory.md#mem-rte-legacy-compaction"
          note: "Legacy storage and summary consumption are separately supported; current checkpoint machinery is not substituted for this path."
        - scope: "Current named-text workspace in the shipped example"
          assessment: "known"
          findings:
            - value: "in-memory"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workspace-text"
                - "memory.md#mem-rte-text-workspace"
              note: "memoryWorkspace uses a fresh layer-local Map; journaled read results are a separate object."
          records:
            - "memory.md#mem-obj-workspace-text"
            - "memory.md#mem-rte-text-workspace"
          note: "The example backend is inspected and has only layer-lifetime retention."
        - scope: "Legacy spilled JSON values and ref manifest in the inspected Bun binding"
          assessment: "known"
          findings:
            - value: "kv"
              basis: "wired"
              records:
                - "memory.md#mem-obj-spill-values"
              note: "The retained full values and manifest are addressed through KeyValueStore."
            - value: "sqlite"
              basis: "wired"
              records:
                - "memory.md#mem-obj-spill-values"
                - "runtime.md#rt-rte-legacy-server"
              note: "The inspected Bun SQL storage backs the spill values; scratch SQL is not the spill corpus."
          records:
            - "memory.md#mem-obj-spill-values"
            - "memory.md#mem-rte-spill-readback"
            - "runtime.md#rt-rte-legacy-server"
          note: "The KV interface and its inspected Bun database backing coexist; this does not classify all platform bindings."
        - scope: "Installed actor modules/manifests and prescribed optimization source/evaluation artifacts"
          assessment: "known"
          findings:
            - value: "files"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-actor-artifact"
                - "runtime.md#rt-rte-artifact-admission"
              note: "Build directories and persisted server actor artifacts contain executable modules and manifests."
            - value: "files"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "The procedure requests saved prompt/source versions, diffs, digests, scores and thread identities."
          records:
            - "runtime.md#rt-obj-actor-artifact"
            - "runtime.md#rt-rte-artifact-admission"
            - "runtime.md#rt-rte-optimization-guidance"
          note: "The two evidence layers remain separate; no optimizer artifacts or exercised promotion were supplied."
        - scope: "Attachment byte backends, custom journals/workspaces, remaining legacy backup and Cloudflare spill bindings"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-content-parts"
            - "memory.md#mem-obj-workspace-text"
            - "memory.md#mem-rte-spill-readback"
            - "memory.md#mem-obj-effect-checkpoint"
            - "runtime.md#rt-obj-journal"
          note: "Backend choice and host-specific retention are unresolved; ObjectRef encoding does not establish files, service-object or another substrate."
      records:
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-obj-compaction-state"
        - "memory.md#mem-obj-provider-continuation"
        - "memory.md#mem-obj-content-parts"
        - "runtime.md#rt-obj-permission-policy"
        - "epistemic.md#epi-rte-response-check"
        - "runtime.md#rt-rte-code-execution"
        - "memory.md#mem-rte-state-adoption"
        - "memory.md#mem-obj-effect-checkpoint"
        - "runtime.md#rt-obj-journal"
        - "runtime.md#rt-clm-request-before-execution"
        - "runtime.md#rt-rte-legacy-server"
        - "memory.md#mem-obj-compaction-completed"
        - "memory.md#mem-rte-legacy-compaction"
        - "memory.md#mem-obj-workspace-text"
        - "memory.md#mem-rte-text-workspace"
        - "memory.md#mem-obj-spill-values"
        - "memory.md#mem-rte-spill-readback"
        - "runtime.md#rt-obj-actor-artifact"
        - "runtime.md#rt-rte-artifact-admission"
        - "runtime.md#rt-rte-optimization-guidance"
      note: "Known local memory, SQLite, KV and file witnesses do not enumerate caller-selected backends or uninspected host alternatives."
    representational_form:
      assessment: "partial"
      units:
        - scope: "Conversation text, summary text, ordinary textual tool/resource returns and retained prompt revisions at their model/human consumers"
          assessment: "known"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-obj-compaction-state"
                - "memory.md#mem-obj-compaction-completed"
                - "epistemic.md#epi-obj-resource-body"
              note: "Conversation prose, summary prose and textual source material are interpreted as context, not fixed control fields."
            - value: "natural-language"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
                - "runtime.md#rt-bap-model-instructions"
              note: "Prescribed retained prompt versions are interpreted by the teacher and later inference model."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-obj-compaction-state"
            - "memory.md#mem-obj-compaction-completed"
            - "epistemic.md#epi-obj-resource-body"
            - "runtime.md#rt-rte-optimization-guidance"
            - "runtime.md#rt-bap-model-instructions"
          note: "This unit concerns the textual parts only; arbitrary binary/resource payloads and executable strings are separate."
        - scope: "Event/turn/tool metadata, compaction boundaries, checkpoints, ref manifests, policy/decision fields and executable actor artifacts"
          assessment: "known"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-obj-compaction-state"
                - "memory.md#mem-obj-effect-checkpoint"
                - "memory.md#mem-obj-spill-values"
                - "runtime.md#rt-obj-permission-policy"
                - "runtime.md#rt-obj-actor-artifact"
              note: "These localized fields and code have fixed decoding, selection, replay or execution rules."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-obj-compaction-state"
            - "memory.md#mem-obj-effect-checkpoint"
            - "memory.md#mem-obj-spill-values"
            - "runtime.md#rt-obj-permission-policy"
            - "runtime.md#rt-obj-actor-artifact"
          note: "Text embedded in these containers retains its separate model-interpreted form."
        - scope: "Inspected provider continuation envelope and prompt decoder"
          assessment: "partial"
          findings:
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-provider-continuation"
                - "memory.md#mem-rte-content-replay"
              note: "Provider/protocol/model fields and schema-decoded prompt serialization have fixed matching/decoding rules."
          records:
            - "memory.md#mem-obj-provider-continuation"
            - "memory.md#mem-rte-content-replay"
          note: "Opaque provider reasoning/state may occur inside the consumed payload. The schema and displayed reasoning do not resolve its complete internal form; neither parametric nor wholly natural-language payload is established."
        - scope: "Arbitrary workspace strings, full spill values and attachment bytes"
          assessment: "partial"
          findings:
            - value: "natural-language"
              basis: "wired"
              records:
                - "memory.md#mem-obj-workspace-text"
                - "memory.md#mem-obj-spill-values"
              note: "The records identify textual values among the retained workspace/result parts."
            - value: "symbolic"
              basis: "wired"
              records:
                - "memory.md#mem-obj-spill-values"
                - "memory.md#mem-obj-content-parts"
              note: "Spilled JSON structure and file hash/metadata references are symbolically decoded."
          records:
            - "memory.md#mem-obj-workspace-text"
            - "memory.md#mem-obj-spill-values"
            - "memory.md#mem-obj-content-parts"
          note: "Actual arbitrary strings and opaque bytes are not supplied; other internal forms remain not determinable. A preview cannot classify the full value."
      records:
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-obj-compaction-state"
        - "memory.md#mem-obj-compaction-completed"
        - "epistemic.md#epi-obj-resource-body"
        - "runtime.md#rt-rte-optimization-guidance"
        - "runtime.md#rt-bap-model-instructions"
        - "memory.md#mem-obj-effect-checkpoint"
        - "memory.md#mem-obj-spill-values"
        - "runtime.md#rt-obj-permission-policy"
        - "runtime.md#rt-obj-actor-artifact"
        - "memory.md#mem-obj-provider-continuation"
        - "memory.md#mem-rte-content-replay"
        - "memory.md#mem-obj-workspace-text"
        - "memory.md#mem-obj-content-parts"
      note: "Forms are split by operative part and consumption; opaque continuation/file contents prevent complete enumeration. External model weights are not accumulated memory in this boundary."
    lineage:
      assessment: "partial"
      units:
        - scope: "Current and legacy summaries and event-derived conversation/control projections"
          assessment: "known"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-rte-atom-compaction"
                - "memory.md#mem-rte-legacy-compaction"
                - "memory.md#mem-obj-compaction-state"
                - "memory.md#mem-obj-trajectory"
              note: "Conversation, tool outcomes and prior summaries feed derived retained views and generated summaries."
            - value: "other-compiled"
              basis: "wired"
              records:
                - "memory.md#mem-obj-effect-checkpoint"
                - "runtime.md#rt-clm-request-before-execution"
              note: "Checkpoint codecs compile restoration state into a serialized snapshot, not a model-authored semantic summary."
          records:
            - "memory.md#mem-rte-atom-compaction"
            - "memory.md#mem-rte-legacy-compaction"
            - "memory.md#mem-obj-compaction-state"
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-obj-effect-checkpoint"
            - "runtime.md#rt-clm-request-before-execution"
          note: "These are known derivation paths; they do not authenticate original conversation assertions."
        - scope: "Incoming user/file content and fetched resources admitted into conversation"
          assessment: "known"
          findings:
            - value: "imported"
              basis: "wired"
              records:
                - "memory.md#mem-obj-content-parts"
                - "epistemic.md#epi-rte-resource-import"
                - "memory.md#mem-obj-trajectory"
              note: "Incoming content/refs and HTTP/feed bodies enter from outside the conversation projection."
          records:
            - "memory.md#mem-obj-content-parts"
            - "epistemic.md#epi-rte-resource-import"
            - "memory.md#mem-obj-trajectory"
          note: "Imported lineage describes acquisition; external truth and initial authorship are not established."
        - scope: "Provider continuation emitted by the standard adapter"
          assessment: "partial"
          findings:
            - value: "trace-extracted"
              basis: "wired"
              records:
                - "memory.md#mem-obj-provider-continuation"
                - "memory.md#mem-rte-content-replay"
              note: "A model return supplies the retained continuation for later compatible replay."
          records:
            - "memory.md#mem-obj-provider-continuation"
            - "memory.md#mem-rte-content-replay"
          note: "The extraction path is known, but opaque provider payload origin and its internal derivation are not determined by the replay decoder."
        - scope: "Installed actor artifacts and prescribed trace-fed source revision"
          assessment: "known"
          findings:
            - value: "other-compiled"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-actor-artifact"
                - "runtime.md#rt-rte-artifact-admission"
              note: "Bundling creates actor.mjs and its digest manifest from source."
            - value: "trace-extracted"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "The procedure requests trace/reward-fed prompt or harness revision."
            - value: "authored"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "Teacher/optimizing agent proposes and edits candidate instructions or harness source."
          records:
            - "runtime.md#rt-obj-actor-artifact"
            - "runtime.md#rt-rte-artifact-admission"
            - "runtime.md#rt-rte-optimization-guidance"
          note: "Model/agent authorship here is procedural, not evidence of actual candidate production or human approval."
        - scope: "Arbitrary workspace values, caller-converted initial state, full spill payload origin and preexisting attachment refs"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-workspace-text"
            - "memory.md#mem-rte-text-workspace"
            - "memory.md#mem-rte-state-adoption"
            - "memory.md#mem-obj-spill-values"
            - "memory.md#mem-obj-content-parts"
          note: "Generic callers, stored refs and raw-value spill do not establish whether included initial content was authored, imported or itself trace-derived. State conversion semantics and some spill producers are unspecified."
      records:
        - "memory.md#mem-rte-atom-compaction"
        - "memory.md#mem-rte-legacy-compaction"
        - "memory.md#mem-obj-compaction-state"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-obj-effect-checkpoint"
        - "runtime.md#rt-clm-request-before-execution"
        - "memory.md#mem-obj-content-parts"
        - "epistemic.md#epi-rte-resource-import"
        - "memory.md#mem-obj-provider-continuation"
        - "memory.md#mem-rte-content-replay"
        - "runtime.md#rt-obj-actor-artifact"
        - "runtime.md#rt-rte-artifact-admission"
        - "runtime.md#rt-rte-optimization-guidance"
        - "memory.md#mem-obj-workspace-text"
        - "memory.md#mem-rte-text-workspace"
        - "memory.md#mem-rte-state-adoption"
        - "memory.md#mem-obj-spill-values"
      note: "Known derivations and imported inputs coexist with unresolved initial content and opaque provider provenance; the former do not close the latter."
    behavioral_authority:
      assessment: "partial"
      units:
        - scope: "Conversation/summary/file and compatible continuation content delivered to inference; workspace/spill pages and operator event rows"
          assessment: "known"
          findings:
            - value: "knowledge"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-atom-compaction"
                - "memory.md#mem-rte-legacy-compaction"
                - "memory.md#mem-rte-content-replay"
                - "memory.md#mem-rte-text-workspace"
                - "memory.md#mem-rte-spill-readback"
                - "memory.md#mem-rte-event-inspection"
              note: "These retained parts supply context/reference to the model or operator; delivery establishes neither truth nor compliance."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-atom-compaction"
            - "memory.md#mem-rte-legacy-compaction"
            - "memory.md#mem-rte-content-replay"
            - "memory.md#mem-rte-text-workspace"
            - "memory.md#mem-rte-spill-readback"
            - "memory.md#mem-rte-event-inspection"
          note: "Summary text is user-role context, not automatically a standing system instruction. Opaque payload semantics are considered separately."
        - scope: "Compaction boundaries, recovery positions/seed state, and replayed method results at runtime consumers"
          assessment: "known"
          findings:
            - value: "routing"
              basis: "wired"
              records:
                - "memory.md#mem-obj-compaction-state"
                - "memory.md#mem-obj-effect-checkpoint"
                - "memory.md#mem-rte-state-adoption"
                - "runtime.md#rt-clm-request-before-execution"
              note: "Summary boundaries select later context; checkpoints and initialized states select restoration state and replay windows."
            - value: "validation"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-code-execution"
              note: "Retained method/argument records are criteria for replay equality checks."
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-rte-code-execution"
              note: "Replay divergence fails execution rather than merely advising it."
          records:
            - "memory.md#mem-obj-compaction-state"
            - "memory.md#mem-obj-effect-checkpoint"
            - "memory.md#mem-rte-state-adoption"
            - "runtime.md#rt-clm-request-before-execution"
            - "runtime.md#rt-rte-code-execution"
          note: "Checkpoint data is not itself a schema criterion merely because a decoder validates it; recorded replay arguments really are comparison criteria."
        - scope: "Retained permissions/resolved decisions and current output-rejection state"
          assessment: "known"
          findings:
            - value: "enforcement"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-permission-policy"
                - "runtime.md#rt-rte-governed-tools"
                - "epistemic.md#epi-rte-response-check"
              note: "Allowed/denied decisions gate wrapped tool execution; retained rejection/attempt state can block result admission and terminate correction."
            - value: "routing"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-response-check"
                - "runtime.md#rt-rte-governed-tools"
              note: "Pending decisions and correction limits determine waiting, another inference or failure."
            - value: "instruction"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-response-check"
              note: "Retained validator errors are rendered as corrective system guidance for the next inference."
            - value: "learning"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-response-check"
              note: "Recorded rejection experience feeds automatic construction of durable correction state and its later guidance consumer."
          records:
            - "runtime.md#rt-obj-permission-policy"
            - "runtime.md#rt-rte-governed-tools"
            - "epistemic.md#epi-rte-response-check"
          note: "Only the composed tool gate and conditional output-contract route are covered, not all runtime effects."
        - scope: "Retained conversation and prior summaries at automatic summarization consumers"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "wired"
              records:
                - "memory.md#mem-rte-atom-compaction"
                - "memory.md#mem-rte-legacy-compaction"
              note: "Accumulated session/tool material feeds automatic durable summary updates that supply later model context."
          records:
            - "memory.md#mem-rte-atom-compaction"
            - "memory.md#mem-rte-legacy-compaction"
          note: "Learning authority concerns the trace-fed artifact update, not improved capacity or factual acceptance."
        - scope: "Prescribed optimization feedback, candidate scores, retained prompt versions and promoted executable actor source"
          assessment: "known"
          findings:
            - value: "learning"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "Teacher/optimizer consumes trajectories and score reasons to revise durable prompts or harness code."
            - value: "ranking"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "Development scores and Pareto comparisons determine relative candidate retention/selection."
            - value: "validation"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "Fixed criteria and constraint/regression checks condition candidate acceptance under the procedure."
            - value: "instruction"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
                - "runtime.md#rt-bap-model-instructions"
              note: "Promoted prompt text supplies standing model guidance."
            - value: "routing"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-actor-artifact"
                - "runtime.md#rt-bap-executable-actor"
              note: "Installed executable actor definitions choose runtime composition and service/library paths."
          records:
            - "runtime.md#rt-rte-optimization-guidance"
            - "runtime.md#rt-obj-actor-artifact"
            - "runtime.md#rt-bap-executable-actor"
            - "runtime.md#rt-bap-model-instructions"
          note: "Executable artifact consumption is wired; the optimizer-to-promoted-prompt path and its criteria remain prescribed, not observed."
        - scope: "Semantic force of opaque continuation/file contents and arbitrary adopted/workspace or pushed artifact content"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-obj-provider-continuation"
            - "memory.md#mem-obj-content-parts"
            - "memory.md#mem-rte-state-adoption"
            - "memory.md#mem-obj-workspace-text"
            - "runtime.md#rt-rte-artifact-admission"
          note: "Known delivery and execution channels do not resolve every internal payload role, standing instruction, or arbitrary code effect. No universal authority inventory follows."
      records:
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-atom-compaction"
        - "memory.md#mem-rte-legacy-compaction"
        - "memory.md#mem-rte-content-replay"
        - "memory.md#mem-rte-text-workspace"
        - "memory.md#mem-rte-spill-readback"
        - "memory.md#mem-rte-event-inspection"
        - "memory.md#mem-obj-compaction-state"
        - "memory.md#mem-obj-effect-checkpoint"
        - "memory.md#mem-rte-state-adoption"
        - "runtime.md#rt-clm-request-before-execution"
        - "runtime.md#rt-rte-code-execution"
        - "runtime.md#rt-obj-permission-policy"
        - "runtime.md#rt-rte-governed-tools"
        - "epistemic.md#epi-rte-response-check"
        - "runtime.md#rt-rte-optimization-guidance"
        - "runtime.md#rt-obj-actor-artifact"
        - "runtime.md#rt-bap-executable-actor"
        - "runtime.md#rt-bap-model-instructions"
        - "memory.md#mem-obj-provider-continuation"
        - "memory.md#mem-obj-content-parts"
        - "memory.md#mem-obj-workspace-text"
        - "runtime.md#rt-rte-artifact-admission"
      note: "Knowledge, update-learning, corrective/standing instruction, routing, replay validation/enforcement and prescribed score ranking have separate consumers and evidence layers. Opaque arbitrary parts prevent complete coverage."
    write_agency:
      assessment: "partial"
      units:
        - scope: "Journal/reducer projection, current and legacy summary admission, checkpoint production and inspected final-code spill threshold"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "runtime.md#rt-obj-journal"
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-atom-compaction"
                - "memory.md#mem-rte-legacy-compaction"
                - "memory.md#mem-obj-effect-checkpoint"
                - "memory.md#mem-rte-spill-readback"
              note: "Code or model proposes/adopts retained state without an explicit human decision on each retained item."
          records:
            - "runtime.md#rt-obj-journal"
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-atom-compaction"
            - "memory.md#mem-rte-legacy-compaction"
            - "memory.md#mem-obj-effect-checkpoint"
            - "memory.md#mem-rte-spill-readback"
          note: "Human initiation of a message does not make subsequent journal/summary admission manual; only the inspected spill producer is covered."
        - scope: "Current model-tool workspace write path and output-rejection state admission"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "wired"
              records:
                - "memory.md#mem-rte-text-workspace"
                - "epistemic.md#epi-rte-response-check"
              note: "Model/software tool calls can replace keyed text; validator/reducer code records rejection and correction state without per-content human approval."
          records:
            - "memory.md#mem-rte-text-workspace"
            - "epistemic.md#epi-rte-response-check"
          note: "This is the evidenced software/model path, not a classification of every direct workspace caller."
        - scope: "Prescribed optimizer candidate editing and selection"
          assessment: "known"
          findings:
            - value: "automatic"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "Teacher/optimizing agent proposes and selects revisions within user-authorized scope without a universal per-candidate human approval requirement."
          records:
            - "runtime.md#rt-rte-optimization-guidance"
          note: "User scope and thresholds do not establish manual admission of each revision. Exercise remains unobserved."
        - scope: "Generic direct workspace callers, initial-state conversion/adoption, artifact submission and attachment ingress"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-text-workspace"
            - "memory.md#mem-rte-state-adoption"
            - "runtime.md#rt-rte-artifact-admission"
            - "memory.md#mem-obj-content-parts"
          note: "Code performs structural admission, but the record does not establish whether a human or software decides the submitted content. Generic caller identity cannot support manual or automatic content control for these alternative mechanisms."
        - scope: "Remaining package-spill writers, custom backends and maintenance automation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-spill-readback"
            - "memory.md#mem-obj-workspace-text"
            - "runtime.md#rt-rte-optimization-guidance"
          note: "Not all admission mechanisms are traced; inspected automatic summaries do not classify these alternatives."
      records:
        - "runtime.md#rt-obj-journal"
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-atom-compaction"
        - "memory.md#mem-rte-legacy-compaction"
        - "memory.md#mem-obj-effect-checkpoint"
        - "memory.md#mem-rte-spill-readback"
        - "memory.md#mem-rte-text-workspace"
        - "epistemic.md#epi-rte-response-check"
        - "runtime.md#rt-rte-optimization-guidance"
        - "memory.md#mem-rte-state-adoption"
        - "runtime.md#rt-rte-artifact-admission"
        - "memory.md#mem-obj-content-parts"
        - "memory.md#mem-obj-workspace-text"
      note: "Automatic admission is supported on specific routes. No explicit per-content human admission mechanism is recorded, so manual is not asserted; that is uncertainty, not a system-wide absence."
    curation_operations:
      assessment: "partial"
      units:
        - scope: "Current and legacy conversation summarization and replacement of prior derived summary"
          assessment: "known"
          findings:
            - value: "consolidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-atom-compaction"
                - "memory.md#mem-rte-legacy-compaction"
              note: "Selected retained history plus an earlier summary is compressed into a reduced representation of existing conversation claims."
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-atom-compaction"
                - "memory.md#mem-rte-legacy-compaction"
                - "memory.md#mem-obj-compaction-state"
                - "memory.md#mem-obj-compaction-completed"
              note: "A successful subsequent summary revises the operative retained summary and boundary."
          records:
            - "memory.md#mem-rte-atom-compaction"
            - "memory.md#mem-rte-legacy-compaction"
            - "memory.md#mem-obj-compaction-state"
            - "memory.md#mem-obj-compaction-completed"
          note: "Implementation establishes these transformations despite unverified semantic fidelity. Model novelty/synthesis is not inferred from possible errors."
        - scope: "Current named-text overwrite and legacy repair-history filtering"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "wired"
              records:
                - "memory.md#mem-rte-text-workspace"
              note: "Writing an existing key replaces its retained text."
            - value: "invalidate"
              basis: "wired"
              records:
                - "memory.md#mem-rte-legacy-compaction"
              note: "Repair/completion projection hides designated attempts from subsequent inference/compaction while raw history remains retained."
          records:
            - "memory.md#mem-rte-text-workspace"
            - "memory.md#mem-rte-legacy-compaction"
          note: "These are replacement and withdrawal of current reliance, not an evidenced factual judgment or physical erasure."
        - scope: "Prescribed optimization revision and selected source promotion"
          assessment: "known"
          findings:
            - value: "evolve"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "The procedure revises candidate prompt/harness source against trace feedback."
            - value: "promote"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "Selected candidate source is raised from development candidate to authorized operational source."
          records:
            - "runtime.md#rt-rte-optimization-guidance"
          note: "The procedure requests transformations; generic build/push checks do not prove an optimizer performed them."
        - scope: "Opaque provider payload transformations, caller conversion, untraced spill producers and remaining maintenance automation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-obj-provider-continuation"
            - "memory.md#mem-rte-state-adoption"
            - "memory.md#mem-rte-spill-readback"
            - "runtime.md#rt-rte-optimization-guidance"
          note: "No complete transformation inventory is recorded for these alternatives; no dedup, decay or synthesize conclusion follows from their labels."
      records:
        - "memory.md#mem-rte-atom-compaction"
        - "memory.md#mem-rte-legacy-compaction"
        - "memory.md#mem-obj-compaction-state"
        - "memory.md#mem-obj-compaction-completed"
        - "memory.md#mem-rte-text-workspace"
        - "runtime.md#rt-rte-optimization-guidance"
        - "memory.md#mem-obj-provider-continuation"
        - "memory.md#mem-rte-state-adoption"
        - "memory.md#mem-rte-spill-readback"
      note: "Implemented consolidation, revision and reliance withdrawal coexist with claimed promotion. Raw acquisition, serialization, index/manifest access and byte-integrity checks alone add no curation value."
    read_back_direction:
      assessment: "partial"
      units:
        - scope: "Later inference context and compatible provider/file replay after automatic context selection"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "memory.md#mem-rte-atom-compaction"
                - "memory.md#mem-rte-legacy-compaction"
                - "memory.md#mem-rte-content-replay"
              note: "At a later inference, code supplies summary plus selected suffix; identity-matched continuation and selected attachment bytes are supplied without a fresh retrieval request by that consumer."
          records:
            - "memory.md#mem-rte-atom-compaction"
            - "memory.md#mem-rte-legacy-compaction"
            - "memory.md#mem-rte-content-replay"
          note: "A user message triggers inference but does not request retrieval of each retained context part."
        - scope: "Model-requested current workspace reads and legacy spill reads/grep/SQL; explicit operator event inspection"
          assessment: "known"
          findings:
            - value: "pull"
              basis: "wired"
              records:
                - "memory.md#mem-rte-text-workspace"
                - "memory.md#mem-rte-spill-readback"
                - "memory.md#mem-rte-event-inspection"
              note: "The consumer requests retained keys, refs, substring results or event rows; bounded delivery fulfills that request."
          records:
            - "memory.md#mem-rte-text-workspace"
            - "memory.md#mem-rte-spill-readback"
            - "memory.md#mem-rte-event-inspection"
          note: "Substring/identifier selectors on requested retrieval do not by themselves establish push signals."
        - scope: "Runtime checkpoint/seed and recorded code-result recovery"
          assessment: "known"
          findings:
            - value: "push"
              basis: "wired"
              records:
                - "runtime.md#rt-clm-request-before-execution"
                - "memory.md#mem-obj-effect-checkpoint"
                - "memory.md#mem-rte-state-adoption"
                - "runtime.md#rt-rte-code-execution"
                - "memory.md#mem-rte-spill-readback"
              note: "Restart/resumption automatically supplies checkpoint/seed state and recorded call outcomes to the rebuilt runtime or resumed evaluator."
          records:
            - "runtime.md#rt-clm-request-before-execution"
            - "memory.md#mem-obj-effect-checkpoint"
            - "memory.md#mem-rte-state-adoption"
            - "runtime.md#rt-rte-code-execution"
            - "memory.md#mem-rte-spill-readback"
          note: "The automatic resumption selector is distinct from foreground workspace queries; hydration is not a second independent consumer request."
        - scope: "Prescribed optimization feedback-window consumption"
          assessment: "known"
          findings:
            - value: "push"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "The procedure has a feedback-window selector supply retained prompt versions, trajectories, rewards and reasons to the teacher."
          records:
            - "runtime.md#rt-rte-optimization-guidance"
          note: "Upstream optimizing-agent choices may select the window; teacher receipt remains a prescribed route, not observed delivery."
        - scope: "Custom model/storage callers, advertised logs.events and untraced host/maintenance consumers"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-content-replay"
            - "memory.md#mem-obj-workspace-text"
            - "memory.md#mem-rte-event-inspection"
            - "memory.md#mem-rte-spill-readback"
            - "runtime.md#rt-rte-optimization-guidance"
          note: "Known CLI inspection does not establish advertised model-facing full-log reload. Alternative automatic versus requested consumers are not completely recorded."
      records:
        - "memory.md#mem-rte-atom-compaction"
        - "memory.md#mem-rte-legacy-compaction"
        - "memory.md#mem-rte-content-replay"
        - "memory.md#mem-rte-text-workspace"
        - "memory.md#mem-rte-spill-readback"
        - "memory.md#mem-rte-event-inspection"
        - "runtime.md#rt-clm-request-before-execution"
        - "memory.md#mem-obj-effect-checkpoint"
        - "memory.md#mem-rte-state-adoption"
        - "runtime.md#rt-rte-code-execution"
        - "runtime.md#rt-rte-optimization-guidance"
        - "memory.md#mem-obj-workspace-text"
      note: "Both push and pull are supported. Their inventory is incomplete for custom and advertised-but-unwired alternatives; requested return transport is not counted as another push."
    read_back_signal:
      assessment: "partial"
      units:
        - scope: "Automatic context/summary selection at later inference and summarizer input preparation"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "memory.md#mem-rte-atom-compaction"
                - "memory.md#mem-rte-legacy-compaction"
              note: "Trigger is context preparation; size/window ratios, availability, order and safe boundaries select summary and retained suffix/prefix, not semantic relevance."
          records:
            - "memory.md#mem-rte-atom-compaction"
            - "memory.md#mem-rte-legacy-compaction"
          note: "This coarse signal does not establish judgment-based or lexical retrieval. Model generation of summary text is not the selector of retained context."
        - scope: "Continuation substitution and attachment resolution on a selected inference request"
          assessment: "known"
          findings:
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-obj-provider-continuation"
                - "memory.md#mem-obj-content-parts"
                - "memory.md#mem-rte-content-replay"
              note: "Trigger is request building: provider/protocol/model equality selects compatible retained continuation; object refs select the byte objects delivered with selected user/tool content."
          records:
            - "memory.md#mem-obj-provider-continuation"
            - "memory.md#mem-obj-content-parts"
            - "memory.md#mem-rte-content-replay"
          note: "Actual matching and object resolution affect delivered parts. Merely having a filename or ref in a catalog would not establish this signal."
        - scope: "Runtime recovery and resumed code-result selection"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "wired"
              records:
                - "runtime.md#rt-clm-request-before-execution"
                - "memory.md#mem-obj-effect-checkpoint"
              note: "Restart chooses available checkpoint plus ordered journal suffix by position."
            - value: "identifier"
              basis: "wired"
              records:
                - "memory.md#mem-rte-state-adoption"
                - "runtime.md#rt-rte-code-execution"
                - "memory.md#mem-rte-spill-readback"
              note: "Atom names match registered seed codecs; recorded call ordinal/identity and spill refs select retained outcomes for resumed evaluation."
          records:
            - "runtime.md#rt-clm-request-before-execution"
            - "memory.md#mem-obj-effect-checkpoint"
            - "memory.md#mem-rte-state-adoption"
            - "runtime.md#rt-rte-code-execution"
            - "memory.md#mem-rte-spill-readback"
          note: "Position-based windows and identity-based state/result matching are distinct selectors within automatic recovery."
        - scope: "Prescribed teacher feedback window"
          assessment: "known"
          findings:
            - value: "coarse"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "Trigger is the next optimization round; recent prompt versions and their trajectories/rewards/reasons in a bounded feedback window are supplied to the teacher."
          records:
            - "runtime.md#rt-rte-optimization-guidance"
          note: "The record establishes a prescribed recent-window supply, not embedding or judgment-based trace retrieval."
        - scope: "Requested workspace/event retrieval"
          assessment: "inapplicable"
          findings: []
          records:
            - "memory.md#mem-rte-text-workspace"
            - "memory.md#mem-rte-spill-readback"
            - "memory.md#mem-rte-event-inspection"
          note: "Exact key/ref, substring grep and event filters operate on pull requests. Signal values here classify push selection, not requested queries."
        - scope: "Custom consumers and advertised but unestablished model log reload"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-event-inspection"
            - "memory.md#mem-rte-content-replay"
            - "memory.md#mem-obj-workspace-text"
          note: "The automatic trigger, selector and delivered retained parts are not established; this alternative cannot be made inapplicable by a known pull route."
      records:
        - "memory.md#mem-rte-atom-compaction"
        - "memory.md#mem-rte-legacy-compaction"
        - "memory.md#mem-obj-provider-continuation"
        - "memory.md#mem-obj-content-parts"
        - "memory.md#mem-rte-content-replay"
        - "runtime.md#rt-clm-request-before-execution"
        - "memory.md#mem-obj-effect-checkpoint"
        - "memory.md#mem-rte-state-adoption"
        - "runtime.md#rt-rte-code-execution"
        - "memory.md#mem-rte-spill-readback"
        - "runtime.md#rt-rte-optimization-guidance"
        - "memory.md#mem-rte-text-workspace"
        - "memory.md#mem-rte-event-inspection"
        - "memory.md#mem-obj-workspace-text"
      note: "Known push selectors use coarse windows and actual identity matches. Pull grep does not establish inferred-lexical push. Unresolved consumers prevent a complete selector inventory."
    trace_learning:
      assessment: "partial"
      units:
        - scope: "Automatic current and legacy conversation-summary writes and later inference consumers"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "memory.md#mem-rte-atom-compaction"
                - "memory.md#mem-rte-legacy-compaction"
              note: "Recorded conversational/tool history automatically produces retained summary text; subsequent inference receives it as context."
          records:
            - "memory.md#mem-rte-atom-compaction"
            - "memory.md#mem-rte-legacy-compaction"
          note: "This qualifies independently of whether claims are novel, fidelity is verified or future capacity improves."
        - scope: "Current durable output-rejection state to later corrective inference guidance"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-response-check"
              note: "A rejected model response and validator feedback are retained in rejection state; the next system input is automatically shaped by its errors and attempt limit."
          records:
            - "epistemic.md#epi-rte-response-check"
          note: "This is bounded within the correction route, not an automatic rewrite of the standing actor prompt. No exercised correction or benefit is supplied."
        - scope: "Prescribed NPO/GEPA trace-to-prompt/harness revisions"
          assessment: "known"
          findings:
            - value: "yes"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "Traces, rewards and score reasons feed agent-produced durable prompt/source revisions prescribed for later rounds and deployed operation."
          records:
            - "runtime.md#rt-rte-optimization-guidance"
          note: "The qualifying mechanism is requested in instructions, not an observed or wired optimizer service."
        - scope: "Arbitrary workspace replacement, initial-state conversion, attachment ingress, opaque continuation contents and general pushed actor source"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-text-workspace"
            - "memory.md#mem-rte-state-adoption"
            - "memory.md#mem-obj-content-parts"
            - "memory.md#mem-obj-provider-continuation"
            - "memory.md#mem-rte-content-replay"
            - "runtime.md#rt-rte-artifact-admission"
          note: "The actual trace input and durable behavior-shaping derivation are caller-specific and not supplied. These writes cannot be classified no merely because the generic API does not demand traces."
        - scope: "Remaining package-spill producers and maintenance automation"
          assessment: "uninspected"
          findings: []
          records:
            - "memory.md#mem-rte-spill-readback"
            - "runtime.md#rt-rte-optimization-guidance"
          note: "Raw spill retention alone does not establish trace learning; untraced transformations or maintenance writers prevent a complete negative inventory."
      records:
        - "memory.md#mem-rte-atom-compaction"
        - "memory.md#mem-rte-legacy-compaction"
        - "epistemic.md#epi-rte-response-check"
        - "runtime.md#rt-rte-optimization-guidance"
        - "memory.md#mem-rte-text-workspace"
        - "memory.md#mem-rte-state-adoption"
        - "memory.md#mem-obj-content-parts"
        - "memory.md#mem-obj-provider-continuation"
        - "memory.md#mem-rte-content-replay"
        - "runtime.md#rt-rte-artifact-admission"
        - "memory.md#mem-rte-spill-readback"
      note: "Wired summary and correction routes and claimed optimizer revision support yes locally. No bounded absence records support no for arbitrary alternatives. Raw event retention and unchanged recovery snapshots alone are not qualifying learning writes."
    trace_source:
      assessment: "partial"
      units:
        - scope: "Current conversation-summary generation"
          assessment: "known"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-atom-compaction"
              note: "Original inputs are recorded user/assistant conversational turns, recursively including previous conversation summaries."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-obj-trajectory"
                - "memory.md#mem-rte-atom-compaction"
              note: "Recorded tool calls/results/errors in conversation feed the selected summary prefix."
          records:
            - "memory.md#mem-obj-trajectory"
            - "memory.md#mem-rte-atom-compaction"
          note: "Journal event serialization does not independently add event-streams; current summary receives rendered messages rather than all runtime lifecycle events."
        - scope: "Legacy projected-history summary generation"
          assessment: "partial"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "memory.md#mem-rte-legacy-compaction"
              note: "Selected recorded conversation turns and earlier summary feed the legacy summarizer."
            - value: "tool-traces"
              basis: "wired"
              records:
                - "memory.md#mem-rte-legacy-compaction"
              note: "Selected tool arguments/results and execution/rejection feedback can enter the summary brief."
          records:
            - "memory.md#mem-rte-legacy-compaction"
            - "memory.md#mem-obj-content-parts"
          note: "Attachment bytes can also enter the summary prompt; their original content/provenance is unresolved. The summary therefore has known trace inputs without a complete source inventory."
        - scope: "Current output-rejection to corrective system guidance"
          assessment: "partial"
          findings:
            - value: "session-logs"
              basis: "wired"
              records:
                - "epistemic.md#epi-rte-response-check"
              note: "The recorded rejected model response is the conversational source of the correction episode."
          records:
            - "epistemic.md#epi-rte-response-check"
          note: "The route also consumes validator error feedback. Records establish its generation and retention but do not fully classify that feedback under the controlled original-trace categories; an event envelope alone is not an event-stream source."
        - scope: "Prescribed optimizer feedback and candidate revision"
          assessment: "known"
          findings:
            - value: "trajectories"
              basis: "claimed"
              records:
                - "runtime.md#rt-rte-optimization-guidance"
              note: "The requested feedback contains complete rollouts/trajectories linked to rewards and score reasons."
          records:
            - "runtime.md#rt-rte-optimization-guidance"
          note: "This is a source-native prescription for multi-step experience, not evidence that such trace files or evaluations were produced. No additional source category is inferred from the word trace alone."
        - scope: "Unresolved workspace/adoption/artifact/attachment writers, opaque continuation contents and remaining maintenance producers"
          assessment: "not-determinable"
          findings: []
          records:
            - "memory.md#mem-rte-text-workspace"
            - "memory.md#mem-rte-state-adoption"
            - "runtime.md#rt-rte-artifact-admission"
            - "memory.md#mem-obj-content-parts"
            - "memory.md#mem-obj-provider-continuation"
            - "memory.md#mem-rte-content-replay"
            - "memory.md#mem-rte-spill-readback"
            - "runtime.md#rt-rte-optimization-guidance"
          note: "Qualifying trace-fed updates and their original inputs are not established on these included alternatives. trace_source cannot become inapplicable from another route or from raw-retention-only examples."
      records:
        - "memory.md#mem-obj-trajectory"
        - "memory.md#mem-rte-atom-compaction"
        - "memory.md#mem-rte-legacy-compaction"
        - "memory.md#mem-obj-content-parts"
        - "epistemic.md#epi-rte-response-check"
        - "runtime.md#rt-rte-optimization-guidance"
        - "memory.md#mem-rte-text-workspace"
        - "memory.md#mem-rte-state-adoption"
        - "runtime.md#rt-rte-artifact-admission"
        - "memory.md#mem-obj-provider-continuation"
        - "memory.md#mem-rte-content-replay"
        - "memory.md#mem-rte-spill-readback"
      note: "Session and tool sources for summaries and claimed rollout trajectories are supported. Opaque attachments, validator-feedback categorization and arbitrary alternative writes prevent complete coverage; no event-stream value is inferred from serialization."
---

# Tardigrade memory profile

## Comparison rationale

This profile classifies accepted records, not new source inspection. All positive
implementation findings are **wired**, not observed activation or benefit.
The optimizer findings remain **claimed** because the shipped procedure, not an
executed optimizer, is the evidence. Every axis is partial: positive witnesses
coexist with the named opaque/custom or uninspected alternatives. The scope is
accumulated memory and later consumers, not every storage or permission feature
of the runtime.

### Canonical identities and parts

Reconciliation supersedes the epistemic workspace object/route with
[MEM-OBJ-workspace-text](memory.md#mem-obj-workspace-text) and
[MEM-RTE-text-workspace](memory.md#mem-rte-text-workspace), and the epistemic
current-summary route with
[MEM-RTE-atom-compaction](memory.md#mem-rte-atom-compaction). All classifications
use those canonical destinations. No value changes merely because an alias is
superseded. The summary text part
[EPI-OBJ-summary-text](epistemic.md#epi-obj-summary-text) remains distinct from
[MEM-OBJ-compaction-state](memory.md#mem-obj-compaction-state), which also owns
selector/control fields. Likewise, continuation and effect-checkpoint parts do
not replace their journal container. Current code-mode recovery is not the
legacy spill implementation; see
[RT-RTE-code-execution](runtime.md#rt-rte-code-execution) and
[MEM-RTE-spill-readback](memory.md#mem-rte-spill-readback).

### Consequential mappings

Automatic summaries qualify for trace learning because the trace-to-retained-
summary-to-later-inference chain is recorded, even within a run. Consolidation
classifies the implemented compression purpose; unverified faithfulness neither
proves synthesis nor defeats that classification. Prior experience supplies
learning authority at the summarizer, while summary text supplies knowledge at
later inference. The summary's user-role delivery does not alone make it standing
instruction. See [MEM-RTE-atom-compaction](memory.md#mem-rte-atom-compaction) and
[MEM-RTE-legacy-compaction](memory.md#mem-rte-legacy-compaction).

Retained rejection errors form a separate automatic, within-turn guidance route:
[EPI-RTE-response-check](epistemic.md#epi-rte-response-check). This route qualifies
through retained rejection state and its later corrective system consumer, not
through an inferred standing actor rewrite. Its validator-feedback source is
left partially classified rather than called an environmental event merely
because it is logged. The default Bun example has no output contract, so this
conditional route is not asserted active in every invocation.

Read-back units distinguish requested workspace/event retrieval from automatic
context, identity-matched continuation/file delivery and recovery selection.
Substring grep on a requested spill query is pull, not inferred-lexical push.
Coarse size/availability windows coexist with identity matching of actual
retained parts. Compaction's model-generated text does not establish a
judgment-based retrieval selector. See
[MEM-RTE-content-replay](memory.md#mem-rte-content-replay),
[MEM-RTE-text-workspace](memory.md#mem-rte-text-workspace),
[MEM-RTE-event-inspection](memory.md#mem-rte-event-inspection) and
[RT-CLM-request-before-execution](runtime.md#rt-clm-request-before-execution).

The prescribed optimization loop adds trace-fed authored revisions, candidate
score ranking, criteria-based validation and promotion only at its claimed
layer. Its installed executable artifact route is independently wired; that
witness does not upgrade procedural selection or prove a teacher generated or
installed anything. User authorization of scope is not per-candidate manual
admission. Generic workspace, artifact and state-adoption callers retain
unresolved content control. See
[RT-RTE-optimization-guidance](runtime.md#rt-rte-optimization-guidance),
[RT-RTE-artifact-admission](runtime.md#rt-rte-artifact-admission) and
[MEM-RTE-state-adoption](memory.md#mem-rte-state-adoption).

### Coverage limits and read log

The opaque continuation's local serialization/storage is classified without
pretending its display reasoning describes every consumed part. File refs are
symbolic; their bytes and custom backend substrates remain unresolved. Raw spill
retention and checkpoint encoding do not alone establish trace learning. Repair
projection withdraws current reliance while keeping raw history, without proving
rejected assertions false. These limits follow
[MEM-OBJ-provider-continuation](memory.md#mem-obj-provider-continuation),
[MEM-OBJ-content-parts](memory.md#mem-obj-content-parts),
[MEM-OBJ-effect-checkpoint](memory.md#mem-obj-effect-checkpoint) and
[MEM-RTE-legacy-compaction](memory.md#mem-rte-legacy-compaction).

No source files were read for this classification; only the supplied members and
governing contracts were read. No new evidence, quotations, records or target
execution were added. Missing execution evidence prevents observed/causal bases,
not the recorded wired classifications. No bounded absence record warrants a
system-wide trace-learning no, and unresolved alternatives cannot be converted
to inapplicability. The advertised model log reload, custom backends, attachment
provenance, remaining spill producers and maintenance automation prevent stronger
coverage assessments; known routes do not erase those gaps.
