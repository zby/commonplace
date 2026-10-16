---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Tendril memory comparison: retained capability descriptions, invocation conditions and executable source, with unresolved SDK memory alternatives."
run-id: AAS-2026-10-15-tendril-f560fb299a37-01
source-identity: "https://github.com/serverless-dna/tendril"
reviewed-boundary: "e671a4143d28de68289efd81580002041bb4cb6a"
memory-comparison:
  version: 2
  scope: "Capability selection text, symbolic index metadata and TypeScript source accumulated or replaced through registration, human editing or afforded generated-program writes; their listing, execution and human-inspection routes. Includes unresolved preexisting-content provenance, generated workspace-memory alternatives and SDK-owned retained summaries/checkpoints if any. Excludes shipped static instructions and their display copy, runtime configuration/credentials, ordinary current-run conversation/display state, transient stdout and temporary scripts, provider weights, and developer scaffolding. Arbitrary application files have no established shipped later-consumer route; their possible memory mechanisms remain unresolved rather than classified from the workspace grant alone."
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Capability selection text, index metadata and executable source on disk"
          assessment: known
          findings:
            - value: files
              basis: wired
              records: [memory.md#mem-obj-selection-text, memory.md#mem-obj-index-metadata, memory.md#mem-obj-tool-source]
              note: "JSON index and UTF-8 TypeScript files survive process restart and are reloaded by their respective consumers; JSON encoding does not establish a database substrate."
          records: [memory.md#mem-obj-selection-text, memory.md#mem-obj-index-metadata, memory.md#mem-obj-tool-source]
          note: "All three operative registry parts have explicit filesystem storage."
        - scope: "SDK retained context/checkpoint alternatives and possible generated workspace-memory payloads"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-prompt-stream, runtime.md#rt-rte-program-mutation, memory.md#mem-obj-tool-source]
          note: "Dependency internals and actual generated payloads/readers are unavailable in the accepted account. A workspace write grant does not enumerate a memory substrate or establish a later consumer."
      records: [memory.md#mem-obj-selection-text, memory.md#mem-obj-index-metadata, memory.md#mem-obj-tool-source, runtime.md#rt-rte-prompt-stream, runtime.md#rt-rte-program-mutation]
      note: "File-backed capability memory is established; opaque alternatives prevent complete inventory coverage."
    representational_form:
      assessment: partial
      units:
        - scope: "Capability description and invocation conditions interpreted by model/human"
          assessment: known
          findings:
            - value: natural-language
              basis: wired
              records: [epistemic.md#epi-obj-capability, epistemic.md#epi-obj-triggers-suppression, memory.md#mem-bap-selection-guidance]
              note: "Descriptions and conversational conditions receive their consequences through interpretation, even when serialized in JSON."
          records: [epistemic.md#epi-obj-capability, epistemic.md#epi-obj-triggers-suppression, memory.md#mem-bap-selection-guidance]
          note: "This unit covers the text consumer, not the surrounding containers or source body."
        - scope: "Index access/bookkeeping fields and TypeScript execution path"
          assessment: known
          findings:
            - value: symbolic
              basis: wired
              records: [memory.md#mem-obj-index-metadata, memory.md#mem-obj-tool-source, runtime.md#rt-rte-capability-execution]
              note: "Names and metadata have fixed parsing rules; Deno consumes TypeScript as executable symbolic content."
          records: [memory.md#mem-obj-index-metadata, memory.md#mem-obj-tool-source, runtime.md#rt-rte-capability-execution]
          note: "Classifies the operative executable path, not any unsupplied comments or human-readable propositions embedded in actual programs."
        - scope: "Actual code's optional text parts, generated application-memory payloads and SDK retained context alternatives"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-tool-source, runtime.md#rt-rte-program-mutation, runtime.md#rt-rte-prompt-stream]
          note: "No corpus or inspected dependency mechanism establishes additional operative forms. External model weights are not treated as use-accumulated memory here."
      records: [epistemic.md#epi-obj-capability, epistemic.md#epi-obj-triggers-suppression, memory.md#mem-obj-index-metadata, memory.md#mem-obj-tool-source, runtime.md#rt-rte-prompt-stream, runtime.md#rt-rte-program-mutation]
      note: "Natural-language and symbolic paths coexist; neither resolves opaque payloads."
    lineage:
      assessment: partial
      units:
        - scope: "Model registration and human-edited capability text/source"
          assessment: known
          findings:
            - value: authored
              basis: wired
              records: [runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-editor-mutation]
              note: "The model supplies new definition/code; the editor supplies human-chosen replacement bytes. This classifies these derivation paths, not all initial contents."
          records: [runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-editor-mutation]
          note: "Both inspected authoring paths are explicit; no actual authored corpus is supplied."
        - scope: "Registration-generated index bookkeeping"
          assessment: known
          findings:
            - value: other-compiled
              basis: wired
              records: [memory.md#mem-obj-index-metadata, runtime.md#rt-rte-capability-admission]
              note: "Node derives path/date/attribution/version from registration inputs and constants, rather than extracting them from a retained trace."
          records: [memory.md#mem-obj-index-metadata, runtime.md#rt-rte-capability-admission]
          note: "Covers metadata construction only; hardcoded model attribution does not attest later bytes."
        - scope: "Preexisting corpus and program-written replacement provenance"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-selection-text, memory.md#mem-obj-index-metadata, memory.md#mem-obj-tool-source, runtime.md#rt-rte-program-mutation]
          note: "Preserving existing files and allowing arbitrary writes establish neither import nor trace extraction for their actual contents. Initial origin and program derivation inputs are missing."
        - scope: "SDK-owned retained context derivation"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-prompt-stream]
          note: "No accepted record identifies an SDK summary/checkpoint producer or its inputs."
      records: [runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-editor-mutation, memory.md#mem-obj-index-metadata, memory.md#mem-obj-tool-source, runtime.md#rt-rte-program-mutation, runtime.md#rt-rte-prompt-stream]
      note: "Known authoring and metadata derivation do not resolve initial provenance or opaque alternatives."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Capability description consumed by foreground model for tool fit"
          assessment: known
          findings:
            - value: knowledge
              basis: wired
              records: [epistemic.md#epi-obj-capability, memory.md#mem-bap-selection-guidance]
              note: "The description supplies reference about what a retained capability does; delivery is not endorsement or compliance."
          records: [epistemic.md#epi-obj-capability, memory.md#mem-bap-selection-guidance]
          note: "The classified force is advisory reference at the model consumer, not factual acceptance."
        - scope: "Retained triggers/suppression interpreted as invocation policy by foreground model"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [epistemic.md#epi-obj-triggers-suppression, memory.md#mem-bap-selection-guidance]
              note: "Standing conditions direct when to invoke or avoid a capability; no deterministic suppression veto consumes them."
            - value: routing
              basis: wired
              records: [memory.md#mem-rte-capability-list, memory.md#mem-bap-selection-guidance]
              note: "The model interprets retained conditions against the task to choose the capability operation. This is model-mediated selection, not a fixed dispatch matcher."
          records: [epistemic.md#epi-obj-triggers-suppression, memory.md#mem-bap-selection-guidance, memory.md#mem-rte-capability-list]
          note: "Instruction and operation selection coexist at this consumer; no recorded relative-priority ranking is inferred merely from listing."
        - scope: "Retained TypeScript consumed as a program by Deno"
          assessment: known
          findings:
            - value: instruction
              basis: wired
              records: [memory.md#mem-obj-tool-source, runtime.md#rt-bap-capability-source]
              note: "Executable symbolic directions determine later subprocess behavior. This is not the model's static system instruction and does not itself establish a retained permission control."
          records: [memory.md#mem-obj-tool-source, runtime.md#rt-bap-capability-source]
          note: "Deno consumes the current source, not description text; actual program-specific checks and destinations remain outside this unit."
        - scope: "Failure feedback at the requested corrective-update consumer"
          assessment: known
          findings:
            - value: learning
              basis: claimed
              records: [epistemic.md#epi-rte-failure-repair, runtime.md#rt-rte-capability-admission]
              note: "The repair instruction asks the model to use failure feedback to revise durable behavior-shaping code for later execution. This requested update path is not upgraded by the wired write API."
          records: [epistemic.md#epi-rte-failure-repair, runtime.md#rt-rte-capability-admission]
          note: "Coverage is of the declared repair policy; compliance, actual feedback use and improved capacity remain unobserved."
        - scope: "Actual program-specific authority, generated application memory and SDK retained context consumers"
          assessment: uninspected
          findings: []
          records: [memory.md#mem-obj-tool-source, runtime.md#rt-rte-program-mutation, runtime.md#rt-rte-prompt-stream]
          note: "Arbitrary code could supply additional checks or memory consumers; opaque SDK alternatives are not classified from the inspected display."
      records: [epistemic.md#epi-obj-capability, epistemic.md#epi-obj-triggers-suppression, memory.md#mem-bap-selection-guidance, runtime.md#rt-bap-capability-source, epistemic.md#epi-rte-failure-repair, runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-prompt-stream, runtime.md#rt-rte-program-mutation]
      note: "Forces stay local to consumers and evidence layers. Index bookkeeping displayed to humans does not become a runtime validation or enforcement policy."
    write_agency:
      assessment: partial
      units:
        - scope: "Model registration admission"
          assessment: known
          findings:
            - value: automatic
              basis: wired
              records: [runtime.md#rt-rte-capability-admission]
              note: "Schema/name-valid model proposals are saved without a per-content human decision; starting chat does not make admission manual."
          records: [runtime.md#rt-rte-capability-admission]
          note: "Node I/O and model authorship are distinct from the automatic admission policy."
        - scope: "Generated program writes under workspace grant"
          assessment: known
          findings:
            - value: automatic
              basis: afforded
              records: [runtime.md#rt-rte-program-mutation]
              note: "Executing code can decide and perform registry writes without another approval; no supplied program demonstrates such a write."
          records: [runtime.md#rt-rte-program-mutation]
          note: "Afforded permission capacity remains separate from wired registration."
        - scope: "Human editor replacement"
          assessment: known
          findings:
            - value: manual
              basis: wired
              records: [runtime.md#rt-rte-editor-mutation]
              note: "A human supplies changed bytes and explicitly confirms Save. The backend's physical write does not make admission automatic."
          records: [runtime.md#rt-rte-editor-mutation]
          note: "The confirmation applies to the shipped editor action, not arbitrary backend callers."
        - scope: "Admission of preexisting content and unspecified direct backend writers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-index-metadata, memory.md#mem-obj-tool-source, runtime.md#rt-rte-editor-mutation]
          note: "Workspace initialization preserves old files; their control is not recorded. Generic backend identity does not establish a human content decision."
        - scope: "SDK retained context/checkpoint admission"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-prompt-stream]
          note: "Dependency-owned writes and any checkpoint replacement control are uninspected."
      records: [runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-program-mutation, runtime.md#rt-rte-editor-mutation, memory.md#mem-obj-index-metadata, runtime.md#rt-rte-prompt-stream]
      note: "Automatic wired registration, automatic afforded program mutation and manual wired editing are distinct mechanisms; unknown initialization remains included."
    curation_operations:
      assessment: partial
      units:
        - scope: "Same-name registry replacement and editor revision of existing capability content"
          assessment: known
          findings:
            - value: evolve
              basis: wired
              records: [runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-editor-mutation]
              note: "Implemented replacement revises an existing entry/source; no retained prior revision or semantic improvement is required for this mapping."
          records: [runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-editor-mutation]
          note: "Covers overwrite of existing content, not first-time acquisition or primary-key checking by itself."
        - scope: "Requested failure-guided repair of retained code"
          assessment: known
          findings:
            - value: evolve
              basis: claimed
              records: [epistemic.md#epi-rte-failure-repair]
              note: "The policy requests corrective replacement; it does not establish an implemented repair controller or an exercised revision."
          records: [epistemic.md#epi-rte-failure-repair]
          note: "The claimed semantic repair path remains distinct from the wired overwrite operation."
        - scope: "Generated workspace transformations and actual retained code contents"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-program-mutation, memory.md#mem-obj-tool-source]
          note: "Permission to write/remove bytes establishes no particular consolidation, deduplication, synthesis or withdrawal policy. No actual generated transformation is supplied."
        - scope: "SDK summary/compaction and checkpoint transformations"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-prompt-stream]
          note: "The constructor's lack of a Tendril summarizer does not establish absence inside the SDK."
      records: [runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-editor-mutation, epistemic.md#epi-rte-failure-repair, runtime.md#rt-rte-program-mutation, runtime.md#rt-rte-prompt-stream]
      note: "Replacement supports evolution. Listing projection does not write a reduced retained representation; temporary-script cleanup does not curate durable memory."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Model-requested index listing and named source execution"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-rte-capability-list, runtime.md#rt-rte-capability-execution]
              note: "The model requests the index or named capability; Node fulfills that request and Deno consumes the loaded source. Requested delivery is not another push."
          records: [memory.md#mem-rte-capability-list, runtime.md#rt-rte-capability-execution]
          note: "Listing is exhaustive; execution is name-addressed. Neither route independently pushes selected memory."
        - scope: "Human capability browsing and file inspection"
          assessment: known
          findings:
            - value: pull
              basis: wired
              records: [memory.md#mem-rte-capability-browser, runtime.md#rt-rte-editor-mutation]
              note: "Opening/refreshing the browser requests the index; expanding a card or selecting a file requests its bytes. Source cache reuse does not create a separate unsolicited selector."
          records: [memory.md#mem-rte-capability-browser, runtime.md#rt-rte-editor-mutation]
          note: "Human inspection is a later-consumer path, not model context injection."
        - scope: "SDK retained context delivery and possible generated application-memory consumers"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-prompt-stream, runtime.md#rt-rte-program-mutation]
          note: "No accepted record determines whether these alternatives retain material and later pull or push it. A hypothetical generated reader is not a wired consumer."
      records: [memory.md#mem-rte-capability-list, runtime.md#rt-rte-capability-execution, memory.md#mem-rte-capability-browser, runtime.md#rt-rte-editor-mutation, runtime.md#rt-rte-prompt-stream, runtime.md#rt-rte-program-mutation]
      note: "Known request-driven routes do not establish a completely pull-only system boundary while opaque alternatives remain."
    read_back_signal:
      assessment: uninspected
      units:
        - scope: "Inspected capability listing, source execution and human inspection routes"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-rte-capability-list, runtime.md#rt-rte-capability-execution, memory.md#mem-rte-capability-browser]
          note: "These routes fulfill requests, so no push selector exists to classify here. The requested name is an address, not identifier-based push."
        - scope: "SDK retained-context and generated workspace-memory push alternatives"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-prompt-stream, runtime.md#rt-rte-program-mutation]
          note: "Trigger, selector input, selected retained part and even push existence are uninspected. No coarse or inferred signal can be assigned from a tool catalog alone."
      records: [memory.md#mem-rte-capability-list, runtime.md#rt-rte-capability-execution, memory.md#mem-rte-capability-browser, runtime.md#rt-rte-prompt-stream, runtime.md#rt-rte-program-mutation]
      note: "There is no supported positive push signal, but unresolved alternatives prevent axis-wide inapplicability or absence."
    trace_learning:
      assessment: partial
      units:
        - scope: "Requested failure-feedback to model repair to retained replacement to later Deno execution"
          assessment: known
          findings:
            - value: "yes"
              basis: claimed
              records: [epistemic.md#epi-rte-failure-repair, runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-capability-execution]
              note: "Failure feedback is to guide automatic model repair, saved without human approval and available for later execution. This satisfies the route definition at the claimed layer, not observed learning or improvement."
          records: [epistemic.md#epi-rte-failure-repair, runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-capability-execution]
          note: "The repair policy names the trace-fed update; wired persistence alone does not upgrade its claimed compliance."
        - scope: "General registration inputs and generated-program workspace updates beyond the repair policy"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-program-mutation, memory.md#mem-obj-tool-source]
          note: "No actual inputs or program instances determine which further writes are trace-fed durable behavior-shaping updates. Lack of a supplied episode does not warrant a local no."
        - scope: "SDK retained summaries/checkpoints and their later consumers"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-prompt-stream]
          note: "A qualifying continuation summary cannot be ruled out by inspecting only Tendril's constructor; dependency production and read-back are uninspected."
      records: [epistemic.md#epi-rte-failure-repair, runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-capability-execution, runtime.md#rt-rte-program-mutation, runtime.md#rt-rte-prompt-stream]
      note: "A claimed positive coexists with unresolved alternatives. No observed or causally supported learning, improved capacity or system-wide negative follows."
    trace_source:
      assessment: partial
      units:
        - scope: "Failure-feedback input to the requested repair write"
          assessment: known
          findings:
            - value: tool-traces
              basis: claimed
              records: [epistemic.md#epi-rte-failure-repair, epistemic.md#epi-rte-result-disposition]
              note: "The qualifying feedback is a tool execution failure/error supplied to the model, not a trajectory or environmental event stream merely because process events produced it."
          records: [epistemic.md#epi-rte-failure-repair, epistemic.md#epi-rte-result-disposition]
          note: "Classifies the explicitly requested failure input only; exact SDK packaging and any additional retained conversational inputs are not specified."
        - scope: "Additional context inputs to repair and other possible qualifying registration/program writes"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-program-mutation, runtime.md#rt-rte-prompt-stream]
          note: "Task/context can be mixed, but no accepted input instance establishes additional original trace classes consumed by a qualifying write. User text alone does not establish extraction from recorded session logs."
        - scope: "SDK-owned trace-fed retained context alternatives"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-prompt-stream]
          note: "No inspected summary/checkpoint producer identifies its original trace inputs."
      records: [epistemic.md#epi-rte-failure-repair, epistemic.md#epi-rte-result-disposition, runtime.md#rt-rte-capability-admission, runtime.md#rt-rte-program-mutation, runtime.md#rt-rte-prompt-stream]
      note: "The claimed repair source is tool execution feedback; opaque or mixed alternatives prevent complete source coverage."
---

# Tendril memory profile

## Comparison rationale

The durable library has two consumption paths. The model reads descriptions and invocation conditions; Deno reads executable source. JSON serialization does not turn interpreted conditions into symbolic enforcement. Conversely, executable TypeScript has instruction authority at its executor without being natural-language host guidance. The catalog is not an execution whitelist. See [MEM-BAP-selection-guidance](memory.md#mem-bap-selection-guidance), [MEM-OBJ-index-metadata](memory.md#mem-obj-index-metadata) and [RT-BAP-capability-source](runtime.md#rt-bap-capability-source).

The routing finding is model-mediated operation selection from retained conditions. It does not assert a deterministic trigger matcher, a relevance ranker or compliance in a supplied run. Full index delivery and requested named loading are pull operations. An identifier used to fulfill that request does not establish push selection. The separate human browser is also request-driven; its source cache can be stale. See [MEM-RTE-capability-list](memory.md#mem-rte-capability-list), [MEM-BAP-selection-guidance](memory.md#mem-bap-selection-guidance), [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution) and [MEM-RTE-capability-browser](memory.md#mem-rte-capability-browser).

Three admission mechanisms retain distinct warrants: wired automatic registration, afforded automatic program writes and wired manual editing. The container's affordance does not downgrade the editor or upgrade arbitrary program writes. Unknown preexisting-content control remains unresolved. Same-name replacement supports evolution, not versioned rollback, semantic improvement, consolidation or synthesis by implication. See [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission), [RT-RTE-program-mutation](runtime.md#rt-rte-program-mutation), [RT-RTE-editor-mutation](runtime.md#rt-rte-editor-mutation) and [MEM-OBJ-index-metadata](memory.md#mem-obj-index-metadata).

The repair instruction supports claimed trace learning: tool failure is to shape automatically admitted durable replacement code consumed on later execution. Its update consumer has claimed learning authority; the resulting code has separate wired instruction authority at Deno. No successful repair, exercised learning or improved capacity is inferred. Other registration inputs and SDK behavior remain unresolved, rather than being assigned a negative from missing execution evidence. See [EPI-RTE-failure-repair](epistemic.md#epi-rte-failure-repair), [EPI-RTE-result-disposition](epistemic.md#epi-rte-result-disposition), [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) and [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution).

Reconciliation supersedes the epistemic tool-code object with [MEM-OBJ-tool-source](memory.md#mem-obj-tool-source), and the epistemic summary-projection route with [MEM-RTE-capability-list](memory.md#mem-rte-capability-list). All classifications use those canonical destinations. The selection-text container remains valid alongside the epistemic description and policy parts. The program/editor admission parts remain distinct within the valid workspace-mutation container; no unresolved cross-report conflict affects these mappings.

SDK-owned memory alternatives remain included but uninspected. Ordinary SDK turn accumulation, desktop display state, transient tool output and temporary scripts are not classified as accumulated memory merely because they occupy process memory. The accepted records do not establish a durable SDK summary or its absence. Arbitrary workspace write authority likewise does not establish a particular application-memory schema or later consumer. These limits prevent complete axis coverage without suppressing the positive capability-library findings. See [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream), [MEM-OBJ-agent-display](memory.md#mem-obj-agent-display), [RT-RTE-program-mutation](runtime.md#rt-rte-program-mutation) and [MEM-OBJ-tool-source](memory.md#mem-obj-tool-source).

Source-read log: none. Classification used the supplied accepted members and reconciliation only; no source ambiguity required an additional frozen-source read.
