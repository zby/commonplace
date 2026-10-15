---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Interview Doc Agent's accumulated dossier, index and user-input memory, with opaque cloud-consumption alternatives."
run-id: AAS-2026-10-14-interview-doc-agent-c7597c33f23d-01
source-identity: "https://github.com/Shilren/interview-doc-agent"
reviewed-boundary: "6ebfe9aba989d7949dadea0fc4af6fb64892c6aa"
memory-comparison:
  version: 2
  scope: "User-admitted raw experience, JD and persistent template replacements; initialized and maintained dossiers, profile and wiki index; generated products and their human consumption; described cloud persistence and opaque later knowledge-source delivery. Excludes unchanged shipped skill/templates/examples, external model weights and ordinary current-conversation state. Includes unresolved profile initialization and cloud intermediary representations where they affect this memory loop."
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Local raw materials, dossiers, profile, wiki index, retained template replacements, JD and generated products"
          assessment: known
          findings:
            - {value: files, basis: claimed, records: [memory.md#mem-obj-materials, memory.md#mem-obj-experience-dossiers, memory.md#mem-obj-personal-profile, memory.md#mem-obj-wiki-index, memory.md#mem-obj-templates, memory.md#mem-obj-jd, memory.md#mem-obj-output], note: "The documented loop retains these objects as local files; Markdown and optional LaTeX describe encoding, not another substrate."}
          records: [memory.md#mem-obj-materials, memory.md#mem-obj-experience-dossiers, memory.md#mem-obj-personal-profile, memory.md#mem-obj-wiki-index, memory.md#mem-obj-templates, memory.md#mem-obj-jd, memory.md#mem-obj-output]
          note: "These records enumerate the local retained-object inventory; successful persistence is unobserved."
        - scope: "Described cloud knowledge pages/Base records and product documents"
          assessment: known
          findings:
            - {value: service-object, basis: claimed, records: [runtime.md#rt-rte-feishu-writeback, memory.md#mem-obj-materials, memory.md#mem-obj-experience-dossiers, memory.md#mem-obj-output], note: "The proposed stores are service-managed pages and records, not evidence of an inspected RDBMS or vector store."}
          records: [runtime.md#rt-rte-feishu-writeback, memory.md#mem-obj-materials, memory.md#mem-obj-experience-dossiers, memory.md#mem-obj-output]
          note: "Classifies the named persistence objects, not the host's internal access structures."
        - scope: "Cloud knowledge-source intermediary retained state/access structures"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-feishu-writeback]
          note: "Host retrieval and transformations are uninspected; the page display cannot resolve internal storage or establish embedding-free delivery."
      records: [memory.md#mem-obj-materials, memory.md#mem-obj-experience-dossiers, memory.md#mem-obj-personal-profile, memory.md#mem-obj-wiki-index, memory.md#mem-obj-templates, memory.md#mem-obj-jd, memory.md#mem-obj-output, runtime.md#rt-rte-feishu-writeback]
      note: "The named local and cloud stores are classified; opaque cloud access structures prevent complete coverage. Repository distribution does not make personal memory a repo substrate."
    representational_form:
      assessment: partial
      units:
        - scope: "Local retained content and access metadata at model/human consumers, plus authored cloud page text"
          assessment: known
          findings:
            - {value: natural-language, basis: claimed, records: [memory.md#mem-obj-materials, memory.md#mem-obj-experience-dossiers, memory.md#mem-obj-personal-profile, memory.md#mem-obj-wiki-index, memory.md#mem-obj-templates, memory.md#mem-obj-jd, memory.md#mem-obj-output], note: "Facts, quantities, paths, labels and style scaffolds receive consequences through model or human interpretation. No fixed-rule path/schema consumer or LaTeX compiler is shipped."}
          records: [memory.md#mem-obj-materials, memory.md#mem-obj-experience-dossiers, memory.md#mem-obj-personal-profile, memory.md#mem-obj-wiki-index, memory.md#mem-obj-templates, memory.md#mem-obj-jd, memory.md#mem-obj-output]
          note: "Textual numbers and Markdown tables do not independently establish symbolic or parametric memory."
        - scope: "Payload/representation selected by the bound cloud knowledge source"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-feishu-writeback]
          note: "Selected page portions and intervening transformations are uninspected; visible source text does not classify the actual host-consumed alternative."
      records: [memory.md#mem-obj-materials, memory.md#mem-obj-experience-dossiers, memory.md#mem-obj-personal-profile, memory.md#mem-obj-wiki-index, memory.md#mem-obj-templates, memory.md#mem-obj-jd, memory.md#mem-obj-output, runtime.md#rt-rte-feishu-writeback]
      note: "Textual paths are known at their described consumers; opaque cloud delivery remains included. External host weights are not accumulated memory of this artifact."
    lineage:
      assessment: partial
      units:
        - scope: "User-provided raw experience, JD and selected/replaced writing templates"
          assessment: known
          findings:
            - {value: imported, basis: claimed, records: [memory.md#mem-obj-materials, memory.md#mem-obj-jd, memory.md#mem-obj-templates], note: "Human-provided external documents enter the retained collection; their truth and original authorship are not certified."}
          records: [memory.md#mem-obj-materials, memory.md#mem-obj-jd, memory.md#mem-obj-templates]
          note: "Classifies admission provenance, not original source authenticity."
        - scope: "Model-organized dossiers, maintained profile project index/wiki table and generated documents"
          assessment: known
          findings:
            - {value: other-compiled, basis: claimed, records: [runtime.md#rt-rte-consolidate-experience, memory.md#mem-obj-wiki-index, memory.md#mem-obj-personal-profile, memory.md#mem-obj-output], note: "The model derives these artifacts from user material and selection/style inputs. No recorded agent-trace origin establishes trace-extracted lineage for the whole route."}
          records: [runtime.md#rt-rte-consolidate-experience, memory.md#mem-obj-wiki-index, memory.md#mem-obj-personal-profile, memory.md#mem-obj-output]
          note: "Known prescribed derivation does not imply faithful extraction or retained claim-level provenance."
        - scope: "Human edits to retained raw records and dossiers"
          assessment: known
          findings:
            - {value: authored, basis: claimed, records: [memory.md#mem-obj-materials, memory.md#mem-obj-experience-dossiers], note: "Users can edit retained source and dossier content; this is a separate human-authored revision path, not model compilation or imported admission."}
          records: [memory.md#mem-obj-materials, memory.md#mem-obj-experience-dossiers]
          note: "Classifies the documented editing alternative, without claiming any real edit occurred."
        - scope: "Initial personal-profile biographical/persona content"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-personal-profile]
          note: "Empty initialization and later placeholder replacement are described, but allocation of populated fields between user and model is unspecified; authored versus compiled/imported origins cannot be enumerated."
        - scope: "Cloud retrieval intermediary derivation"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-feishu-writeback]
          note: "Copying/adaptation is described but service-side transformations and possible derived access material are not inspected."
      records: [memory.md#mem-obj-materials, memory.md#mem-obj-jd, memory.md#mem-obj-templates, runtime.md#rt-rte-consolidate-experience, memory.md#mem-obj-wiki-index, memory.md#mem-obj-personal-profile, memory.md#mem-obj-output, runtime.md#rt-rte-feishu-writeback]
      note: "Imported inputs, compiled derivatives and human-authored edits coexist with unresolved initialization and cloud provenance."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Raw facts at consolidation/detail lookup; dossiers/profile facts at generation; products at human use"
          assessment: known
          findings:
            - {value: knowledge, basis: claimed, records: [memory.md#mem-obj-materials, memory.md#mem-bap-dossier-context, memory.md#mem-obj-output], note: "Retained assertions supply factual/narrative context to the model or advice to the applicant; designation as a source is not factual acceptance."}
          records: [memory.md#mem-obj-materials, memory.md#mem-bap-dossier-context, memory.md#mem-obj-output]
          note: "Names both update and downstream consumers without treating knowledge delivery as compliance."
        - scope: "Retained template replacements at the document-generation model"
          assessment: known
          findings:
            - {value: instruction, basis: claimed, records: [memory.md#mem-bap-template-guidance, memory.md#mem-obj-templates], note: "Selected persistent replacements provide writing-style and structural directions; unchanged shipped examples are excluded from accumulated memory."}
          records: [memory.md#mem-bap-template-guidance, memory.md#mem-obj-templates]
          note: "Instructional force is requested, not independently enforced."
        - scope: "JD requirements and profile persona/project content at relevance selection"
          assessment: known
          findings:
            - {value: ranking, basis: claimed, records: [memory.md#mem-obj-jd, memory.md#mem-obj-personal-profile, runtime.md#rt-rte-generate-document], note: "Content changes relative emphasis, reordering and cutting of experience under model judgment; no numerical scorer is required for ranking authority."}
          records: [memory.md#mem-obj-jd, memory.md#mem-obj-personal-profile, runtime.md#rt-rte-generate-document]
          note: "Relevance priorities do not authenticate accomplishments or supply an answer oracle."
        - scope: "Wiki and profile locator entries at dossier/template lookup"
          assessment: known
          findings:
            - {value: routing, basis: claimed, records: [memory.md#mem-obj-wiki-index, epistemic.md#epi-obj-wiki-index, runtime.md#rt-rte-generate-document], note: "Retained labels and paths guide which dossiers/templates the foreground model reads next."}
          records: [memory.md#mem-obj-wiki-index, epistemic.md#epi-obj-wiki-index, runtime.md#rt-rte-generate-document]
          note: "The broader epistemic index container includes profile locators; locator authority is not factual endorsement."
        - scope: "Actual cloud-selected retained payload at later host consumption"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-feishu-writeback]
          note: "Knowledge-source intent is recorded, but opaque selection/transformation prevents complete classification of the consumed payload and its effects."
      records: [memory.md#mem-obj-materials, memory.md#mem-bap-dossier-context, memory.md#mem-obj-output, memory.md#mem-bap-template-guidance, memory.md#mem-obj-templates, memory.md#mem-obj-jd, memory.md#mem-obj-personal-profile, memory.md#mem-obj-wiki-index, epistemic.md#epi-obj-wiki-index, runtime.md#rt-rte-generate-document, runtime.md#rt-rte-feishu-writeback]
      note: "Knowledge, instruction, ranking and routing have distinct consumers/effects. No blanket enforcement, validation or learning force follows from retention or a host permission check. Cloud consumption is unresolved."
    write_agency:
      assessment: partial
      units:
        - scope: "Human admission/edit/replacement of raw records, dossiers, JD and preferred templates; manual cloud copying"
          assessment: known
          findings:
            - {value: manual, basis: claimed, records: [memory.md#mem-obj-materials, memory.md#mem-obj-experience-dossiers, memory.md#mem-obj-jd, memory.md#mem-obj-templates, runtime.md#rt-rte-feishu-writeback], note: "A human explicitly supplies/edits/replaces this content or chooses text to copy when cloud writing is denied."}
          records: [memory.md#mem-obj-materials, memory.md#mem-obj-jd, memory.md#mem-obj-templates, runtime.md#rt-rte-feishu-writeback]
          note: "Human copying is a separate admission route, not evidence of factual review."
        - scope: "Starter creation, direct dossier/index updates and product admission in local or writable cloud mode"
          assessment: known
          findings:
            - {value: automatic, basis: claimed, records: [runtime.md#rt-rte-initialize-workspace, runtime.md#rt-rte-consolidate-experience, runtime.md#rt-rte-generate-document, runtime.md#rt-rte-feishu-writeback], note: "Model admission is prescribed without a per-content human approval gate. Human initiation and host physical I/O do not make admission manual."}
          records: [runtime.md#rt-rte-initialize-workspace, runtime.md#rt-rte-consolidate-experience, runtime.md#rt-rte-generate-document, runtime.md#rt-rte-feishu-writeback]
          note: "Automatic names documented admission control; no executable or successful write is established."
        - scope: "Initial populated profile fields"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-personal-profile]
          note: "The allocation of real biographical fields between user and model is unspecified; known subsequent index updating does not resolve that admission."
        - scope: "Cloud service-side derived/access-state admission"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-feishu-writeback]
          note: "No inspected selector or transformation implementation establishes control over any intermediary retained state."
      records: [memory.md#mem-obj-materials, memory.md#mem-obj-jd, memory.md#mem-obj-templates, memory.md#mem-obj-personal-profile, runtime.md#rt-rte-initialize-workspace, runtime.md#rt-rte-consolidate-experience, runtime.md#rt-rte-generate-document, runtime.md#rt-rte-feishu-writeback]
      note: "Manual and automatic admission both exist in doctrine; unresolved initial fields and cloud internals prevent a complete agency inventory."
    curation_operations:
      assessment: partial
      units:
        - scope: "Requested raw-material organization and subsequent dossier/index refresh"
          assessment: partial
          findings:
            - {value: consolidate, basis: claimed, records: [runtime.md#rt-rte-consolidate-experience, memory.md#mem-obj-experience-dossiers], note: "The prescribed extraction combines experience into interview-ready summaries and quick metrics while originals remain reachable."}
            - {value: evolve, basis: claimed, records: [runtime.md#rt-rte-consolidate-experience], note: "Changed raw content and a new request lead to revision of corresponding retained dossiers and indexes."}
          records: [runtime.md#rt-rte-consolidate-experience, memory.md#mem-obj-experience-dossiers, epistemic.md#epi-obj-experience-library]
          note: "These are requested transformations, not wired execution. No input/output pair resolves whether why/how explanations add a new claim; synthesis cannot be asserted from an indeterminate semantic edge."
        - scope: "Cloud service-side transformation of retained knowledge"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-feishu-writeback]
          note: "Host transformations are uninspected; local organization does not classify this alternative."
      records: [runtime.md#rt-rte-consolidate-experience, memory.md#mem-obj-experience-dossiers, epistemic.md#epi-obj-experience-library, memory.md#mem-abs-memory-maintenance, runtime.md#rt-rte-feishu-writeback]
      note: "Consolidation and evolution retain claimed warrants. The bounded absence of cleanup/withdrawal/evaluation protocols supplies no dedup, decay, invalidate or promote positive; cloud and semantic transformation coverage remain unresolved."
    read_back_direction:
      assessment: partial
      units:
        - scope: "Local foreground generation/detail reads and requested human consumption of saved products"
          assessment: known
          findings:
            - {value: pull, basis: claimed, records: [runtime.md#rt-rte-generate-document, memory.md#mem-obj-output], note: "The consumer's document/project request causes model-directed reads; the applicant takes the requested saved product. Delivery satisfying that request is not a second push."}
          records: [runtime.md#rt-rte-generate-document, memory.md#mem-obj-output]
          note: "Covers selected dossiers/profile/templates/JD, raw-detail fallback and whole-library alternative in the documented local route."
        - scope: "Bound cloud knowledge-source selection and delivery to a later invocation"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-feishu-writeback]
          note: "The tutorial does not expose whether a consumer pulls pages or the host independently pushes selected content."
      records: [runtime.md#rt-rte-generate-document, memory.md#mem-obj-output, runtime.md#rt-rte-feishu-writeback]
      note: "A known local pull route cannot settle the cloud direction or justify a system-wide pull-only conclusion."
    read_back_signal:
      assessment: uninspected
      units:
        - scope: "Completely described local requested read-back"
          assessment: inapplicable
          findings: []
          records: [runtime.md#rt-rte-generate-document, memory.md#mem-obj-output]
          note: "This branch is pull-only; requested path names and model relevance matching do not establish a push signal."
        - scope: "Cloud knowledge-source selection, if push occurs"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-feishu-writeback]
          note: "Trigger, selector input and delivered retained parts are uninspected. No identifier, lexical, embedding, judgment or coarse push signal can be assigned."
      records: [runtime.md#rt-rte-generate-document, memory.md#mem-obj-output, runtime.md#rt-rte-feishu-writeback]
      note: "There is no supported positive push signal. Unresolved cloud delivery prevents axis-level inapplicability despite the pull-only local unit."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Manual source/JD/template admission, blank initialization and generated products without later agent reuse"
          assessment: known
          findings:
            - {value: "no", basis: claimed, records: [memory.md#mem-abs-memory-maintenance, memory.md#mem-obj-materials, memory.md#mem-obj-jd, memory.md#mem-obj-templates, runtime.md#rt-rte-initialize-workspace, memory.md#mem-obj-output], note: "Manual inputs are not automatic trace-fed writes; blank starters are not trace-derived; products have only a prescribed human consumer and no output-to-agent update route."}
          records: [memory.md#mem-obj-materials, memory.md#mem-obj-jd, memory.md#mem-obj-templates, runtime.md#rt-rte-initialize-workspace, memory.md#mem-obj-output]
          note: "The negative is bounded to these mechanisms and the shipped doctrine, not all downstream host use."
        - scope: "Automatic dossier/index compilation from heterogeneous human experience records"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-materials, runtime.md#rt-rte-consolidate-experience, memory.md#mem-obj-experience-dossiers, memory.md#mem-abs-memory-maintenance]
          note: "A durable derived artifact and later consumer are described, but chats/retrospectives are not identified as qualifying session/tool/event/trajectory traces. Absence of agent-execution compaction or method revision does not rule out other trace-fed context production; qualifying input origin is unresolved."
        - scope: "Cloud intermediary retained transformations"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-feishu-writeback]
          note: "Opaque host transformations expose no trace-fed write inventory or later derived-artifact consumer."
      records: [memory.md#mem-obj-materials, memory.md#mem-obj-jd, memory.md#mem-obj-templates, runtime.md#rt-rte-initialize-workspace, memory.md#mem-obj-output, runtime.md#rt-rte-consolidate-experience, memory.md#mem-obj-experience-dossiers, memory.md#mem-abs-memory-maintenance, runtime.md#rt-rte-feishu-writeback]
      note: "Local negatives do not establish system-wide absence. Records support neither a qualifying positive trace-fed route nor a complete negative across heterogeneous inputs and opaque cloud alternatives."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Manual admission, blank initialization and human-only product routes"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-materials, memory.md#mem-obj-jd, memory.md#mem-obj-templates, runtime.md#rt-rte-initialize-workspace, memory.md#mem-obj-output]
          note: "These bounded mechanisms do not establish qualifying automatic trace learning, so they have no qualifying trace source."
        - scope: "Potential trace inputs among chats and human-work retrospectives compiled into dossiers"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-materials, runtime.md#rt-rte-consolidate-experience]
          note: "Original content/origin does not distinguish conversational agent-session turns, discrete events, tool feedback or linked trajectories. Chat serialization alone cannot establish session-logs; a work record alone cannot establish event-streams."
        - scope: "Potential cloud intermediary trace-fed writes"
          assessment: uninspected
          findings: []
          records: [runtime.md#rt-rte-feishu-writeback]
          note: "No inspected original input to an intermediary qualifying write is supplied."
      records: [memory.md#mem-obj-materials, memory.md#mem-obj-jd, memory.md#mem-obj-templates, runtime.md#rt-rte-initialize-workspace, memory.md#mem-obj-output, runtime.md#rt-rte-consolidate-experience, runtime.md#rt-rte-feishu-writeback]
      note: "No controlled trace-source value is established. Unresolved dossier-input origin and cloud processing prevent system-wide inapplicability."
---

# Interview Doc Agent memory profile

## Comparison rationale

This profile classifies the prescribed memory loop, not an implemented host. All positive findings have a `claimed` basis: the accepted records use doctrine/design evidence, and none establishes wired, observed or causal memory behavior. Coverage assessments are independent of that weak evidence layer. The known local object units classify the complete documented file inventory, while cloud intermediary units retain the recorded inspection gaps.

The local index is model-interpreted lookup content, not a symbolic execution schema or a graph database. Its paths route subsequent reads. JD requirements and persona/project content prioritize experience, so ranking has a different consumer effect from locator routing. Template replacements provide instructions; raw and derived personal assertions provide knowledge. Host permissions are external controls, not accumulated enforcement memory. These distinctions follow [MEM-OBJ-wiki-index](memory.md#mem-obj-wiki-index), [MEM-OBJ-jd](memory.md#mem-obj-jd), [MEM-OBJ-personal-profile](memory.md#mem-obj-personal-profile), [MEM-BAP-template-guidance](memory.md#mem-bap-template-guidance) and [RT-RTE-generate-document](runtime.md#rt-rte-generate-document).

Dossier organization supports claimed consolidation and requested refresh supports claimed evolution. The epistemic account leaves the semantic transformation indeterminate; a why/how field is not sufficient evidence that a new claim was synthesized. Compiled lineage does not establish faithful preservation or trace origin. See [RT-RTE-consolidate-experience](runtime.md#rt-rte-consolidate-experience) and [EPI-OBJ-experience-library](epistemic.md#epi-obj-experience-library).

Read-back direction is assessed at the request/selection/delivery operations. The foreground model's selection serves a document request; automatic file delivery in that chain is not independent push. Cloud knowledge binding does not expose equivalent selection or delivery. Thus local signal inapplicability coexists with an unresolved system signal assessment, supported by [RT-RTE-generate-document](runtime.md#rt-rte-generate-document) and [RT-RTE-feishu-writeback](runtime.md#rt-rte-feishu-writeback).

The absence of shipped agent-execution compaction and performance-fed method revision is bounded in [MEM-ABS-memory-maintenance](memory.md#mem-abs-memory-maintenance). It cannot become a blanket trace-learning negative: the profile definition also allows automatically retained context derived from qualifying traces. [MEM-OBJ-materials](memory.md#mem-obj-materials) names chats and human-work records without enough original-input detail to classify a qualifying trace source. The dossier route has automatic admission and later consumption, but its trace-fed qualification remains unresolved. Conversely, manual admission, blank initialization and products with only human consumption do not independently qualify.

Reconciliation supersedes the epistemic raw-material, JD, template and output object declarations with their corresponding memory declarations. This profile cites those canonical memory records rather than their superseded aliases. The experience-library and epistemic index containers remain unsuperseded because they include profile parts beyond the narrower memory dossier/wiki referents; their citations preserve that scope distinction. No supersession changes a classification value or strengthens its basis.

No frozen-source file was read for this job. Classification uses the supplied accepted records and their annotations only. No records, quotations or new source evidence were added.
