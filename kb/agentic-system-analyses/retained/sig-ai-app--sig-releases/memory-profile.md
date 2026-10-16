---
type: agentic-system-analyses/types/agentic-system-memory-profile.md
description: "Sig memory profile: claimed private markdown history and approved team context, with opaque skills, selection and admission paths."
run-id: AAS-2026-10-14-sig-releases-50379145ac31-01
source-identity: "https://github.com/sig-ai-app/sig-releases"
reviewed-boundary: "314bbea9d1cef911cea0f201eec66a57c2e59020"
memory-comparison:
  version: 2
  scope: >-
    Accumulated private factual records and personal interpretations, approved
    team knowledge, reusable shared skills, and their admission, maintenance
    and later-consumer paths. Raw capture retention, organizational draft
    retention, access metadata, optional Slack/voice acquisition, conversation
    retention and provider-side retained context remain unresolved included
    alternatives. Excluded are static release documentation, provider model
    weights not shown to change through use, credentials, analytics linkage
    and telemetry, and public support issues: no route from those diagnostic
    objects to durable app behavior-shaping updates is established. This is
    the documentary memory boundary, not the whole runtime's storage.
  axes:
    storage_substrate:
      assessment: partial
      units:
        - scope: "Private factual records and personal-layer notes on the local computer"
          assessment: known
          findings:
            - value: files
              basis: claimed
              records: [memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer]
              note: "The local-memory contract explicitly places these notes in plain markdown files in the selected folder."
          records: [memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer]
          note: "File retention is classified at the documented layer; file-versus-section layout does not change this substrate."
        - scope: "Published team knowledge and reusable skills, including recipient copies"
          assessment: not-determinable
          findings: []
          records: [memory.md#mem-obj-team-knowledge, runtime.md#rt-obj-skills, runtime.md#rt-rte-skill-sync]
          note: "Git synchronization is named, but operative remote storage and skill placement are unspecified; transport alone does not establish repo or files."
        - scope: "Raw captures, drafts, access metadata, integration outputs, transcripts and opaque provider context"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-obj-capture, epistemic.md#epi-obj-org-version, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
          note: "Independent retention and substrate are unresolved for these alternatives; provider internals and optional acquisition paths are unavailable."
      records: [memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer, memory.md#mem-obj-team-knowledge, runtime.md#rt-obj-skills, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share, epistemic.md#epi-obj-capture, epistemic.md#epi-obj-org-version]
      note: "Local files are a supported existence finding, not an inventory of all storage in the partial application loop."
    representational_form:
      assessment: partial
      units:
        - scope: "Private factual and personal content interpreted by users and intended later AI consumers"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer]
              note: "The documented retained parts are textual meeting accounts and interpretations, not demonstrated formal controls."
          records: [memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer]
          note: "This classifies the described content, not undisclosed file metadata or a verified model payload."
        - scope: "Organizational draft and approved team text interpreted by reviewer and later AI"
          assessment: known
          findings:
            - value: natural-language
              basis: claimed
              records: [epistemic.md#epi-obj-org-version, memory.md#mem-obj-team-knowledge]
              note: "Exact-text review concerns a natural-language organizational account; later team context has the same described content form, not necessarily unchanged text."
          records: [epistemic.md#epi-obj-org-version, memory.md#mem-obj-team-knowledge]
          note: "Draft and approved content are separate parts; unknown serialization does not negate their documented textual content."
        - scope: "Capture narrative content, if retained independently"
          assessment: partial
          findings:
            - value: natural-language
              basis: claimed
              records: [epistemic.md#epi-obj-capture]
              note: "The input is a user's raw meeting narrative interpreted by Sig."
          records: [epistemic.md#epi-obj-capture]
          note: "The input's content form is described, but its independent persistence and any retained voice encoding are unresolved."
        - scope: "Skills, symbolic access metadata, integration outputs, transcripts and provider-retained context"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-skills, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share, memory.md#mem-obj-factual-record]
          note: "No workflow bodies or consumed opaque payloads are supplied. Possible symbolic metadata and numerical provider state cannot be classified from labels."
      records: [memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer, memory.md#mem-obj-team-knowledge, epistemic.md#epi-obj-org-version, epistemic.md#epi-obj-capture, runtime.md#rt-obj-skills, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
      note: "Natural-language parts coexist with unresolved operative parts; the provider's model form is not a retained-context form finding."
    lineage:
      assessment: partial
      units:
        - scope: "Capture account supplied by the human user, if independently retained"
          assessment: partial
          findings:
            - value: authored
              basis: claimed
              records: [epistemic.md#epi-obj-capture, runtime.md#rt-rte-capture-share]
              note: "The human supplies their account and personal observations rather than a disclosed extracted execution trace."
          records: [epistemic.md#epi-obj-capture, runtime.md#rt-rte-capture-share]
          note: "Authorship is described; independent input retention and earlier source provenance are not."
        - scope: "Private notes derived by Sig from the supplied account"
          assessment: partial
          findings:
            - value: other-compiled
              basis: claimed
              records: [memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer, epistemic.md#epi-rte-private-synthesis]
              note: "Sig structures the user's narrative into factual and personal parts; no qualifying trace-extraction origin is established."
          records: [memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer, epistemic.md#epi-rte-private-synthesis]
          note: "The subsequent compilation path is described, while initial migration/import provenance and raw-input persistence remain unknown."
        - scope: "Organizational proposal derived from capture/private material"
          assessment: partial
          findings:
            - value: other-compiled
              basis: claimed
              records: [epistemic.md#epi-rte-org-draft, epistemic.md#epi-obj-org-version]
              note: "Sig prepares a clean organizational account for review, a derived candidate rather than a disclosed trace-extracted artifact."
          records: [epistemic.md#epi-rte-org-draft, epistemic.md#epi-obj-org-version]
          note: "The preparation path is described, but exact source subset, semantic changes and draft persistence are unresolved."
        - scope: "Approved organizational content entering teammates' knowledge/context"
          assessment: partial
          findings:
            - value: imported
              basis: claimed
              records: [memory.md#mem-obj-team-knowledge, runtime.md#rt-rte-capture-share]
              note: "Published content from another installation reaches a teammate's Sig through the declared sharing path."
          records: [memory.md#mem-obj-team-knowledge, runtime.md#rt-rte-capture-share]
          note: "Recipient import is described; human inclusion decisions intervene after drafting, so unchanged draft-to-publication content is not assumed."
        - scope: "Reusable workflows received through team synchronization"
          assessment: partial
          findings:
            - value: imported
              basis: claimed
              records: [runtime.md#rt-obj-skills, runtime.md#rt-rte-skill-sync]
              note: "The advertised sharing route distributes another installation's reusable workflow to the team."
          records: [runtime.md#rt-obj-skills, runtime.md#rt-rte-skill-sync]
          note: "The receiving path is described; initial authorship, compilation and possible trace provenance remain unresolved."
        - scope: "Access metadata, optional integration outputs, conversation and provider context provenance"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share, memory.md#mem-obj-factual-record]
          note: "No retained-part derivation or initial-content history establishes controlled lineage for these included alternatives."
      records: [epistemic.md#epi-obj-capture, memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer, memory.md#mem-obj-team-knowledge, epistemic.md#epi-rte-private-synthesis, epistemic.md#epi-rte-org-draft, runtime.md#rt-obj-skills, runtime.md#rt-rte-skill-sync, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
      note: "Authored input, compiled private/proposed output and recipient import are distinct derivation stages; none resolves all initial provenance."
    behavioral_authority:
      assessment: partial
      units:
        - scope: "Private work-history content at its intended later AI-context consumer"
          assessment: partial
          findings:
            - value: knowledge
              basis: claimed
              records: [epistemic.md#epi-rte-context-use, memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer]
              note: "The described force is advisory context for later AI work, not an instruction or enforced control."
          records: [epistemic.md#epi-rte-context-use, memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer]
          note: "Exact selected parts, especially personal-layer provider inclusion, and actual influence are unresolved."
        - scope: "Approved team account at teammate Sig's intended context consumer"
          assessment: partial
          findings:
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-obj-team-knowledge, epistemic.md#epi-rte-context-use]
              note: "Published organizational material is said to supply later teammate context through natural-language interpretation."
          records: [memory.md#mem-obj-team-knowledge, epistemic.md#epi-rte-context-use]
          note: "Context supply is claimed, while selected payload, invocation and activation are not established."
        - scope: "Private notes at the user's direct file-reading consumer"
          assessment: known
          findings:
            - value: knowledge
              basis: claimed
              records: [memory.md#mem-obj-factual-record]
              note: "The local-memory contract explicitly permits opening and reading retained work files as reference."
          records: [memory.md#mem-obj-factual-record]
          note: "This bounded human-reference path does not establish any AI selector or consumer."
        - scope: "Skills, retained capture/draft alternatives, metadata, integration and provider context consumers"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-skills, runtime.md#rt-rte-skill-sync, runtime.md#rt-rte-provider-message, epistemic.md#epi-obj-capture, epistemic.md#epi-obj-org-version, runtime.md#rt-rte-capture-share]
          note: "Workflow bodies and actual downstream effects are unspecified. A review/send policy is not itself an accumulated retained enforcement object."
      records: [epistemic.md#epi-rte-context-use, memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer, memory.md#mem-obj-team-knowledge, runtime.md#rt-obj-skills, runtime.md#rt-rte-skill-sync, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share, epistemic.md#epi-obj-org-version]
      note: "Knowledge is supported at described consumers only. Neither instruction, learning, ranking nor enforcement follows automatically from retention or publication approval."
    write_agency:
      assessment: partial
      units:
        - scope: "Admission of selected organizational text to team publication"
          assessment: known
          findings:
            - value: manual
              basis: claimed
              records: [epistemic.md#epi-rte-share-approval, memory.md#mem-obj-team-knowledge]
              note: "A human reviews exact text, decides inclusion and explicitly authorizes send for that content."
          records: [epistemic.md#epi-rte-share-approval, memory.md#mem-obj-team-knowledge]
          note: "The documentary publication decision is manual; gate enforcement is not inspected."
        - scope: "Local private-note and draft admission, initial imports and capture retention"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-rte-private-synthesis, epistemic.md#epi-rte-org-draft, memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer, epistemic.md#epi-obj-capture]
          note: "Sig proposes structured text and writes files, but per-content local approval is unspecified. Human initiation and physical software writing settle neither automatic nor manual admission."
        - scope: "Skill creation/replacement/publication, recipient admission, integration and provider writes"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-skill-sync, memory.md#mem-obj-team-knowledge, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
          note: "One-click skill sharing does not disclose a content approval decision; recipient, optional integration and provider controls are unknown."
      records: [epistemic.md#epi-rte-share-approval, epistemic.md#epi-rte-private-synthesis, epistemic.md#epi-rte-org-draft, memory.md#mem-obj-team-knowledge, memory.md#mem-obj-factual-record, memory.md#mem-obj-personal-layer, runtime.md#rt-rte-skill-sync, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
      note: "Only organizational publication has an explicit per-content human admission warrant; automatic local admission is not inferred from Sig's authorship."
    curation_operations:
      assessment: not-determinable
      units:
        - scope: "Private synthesis and organizational preparation over potentially retained inputs"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-rte-private-synthesis, epistemic.md#epi-rte-org-draft, epistemic.md#epi-obj-capture]
          note: "No implementation or content instance settles semantic preservation, added claims or retained input. Structuring and the synthesis label do not establish consolidate or synthesize."
        - scope: "Local deletion/editing and team/skill maintenance"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-rte-local-deletion, memory.md#mem-obj-factual-record, memory.md#mem-obj-team-knowledge, runtime.md#rt-rte-skill-sync]
          note: "Local deletion is described, but consumer withdrawal, history retention and maintenance semantics are unknown; editing access alone establishes no evolve route."
        - scope: "Opaque integration, transcript, metadata and provider-state maintenance"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
          note: "No disclosed compaction, checkpoint or optional-integration transformation warrants a controlled operation."
      records: [epistemic.md#epi-rte-private-synthesis, epistemic.md#epi-rte-org-draft, epistemic.md#epi-rte-local-deletion, memory.md#mem-obj-factual-record, memory.md#mem-obj-team-knowledge, runtime.md#rt-rte-skill-sync, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
      note: "Inspected documentation is inconclusive about controlled curation operations; this is not evidenced absence of app maintenance."
    read_back_direction:
      assessment: partial
      units:
        - scope: "User opening and reading accumulated local note files"
          assessment: known
          findings:
            - value: pull
              basis: claimed
              records: [memory.md#mem-obj-factual-record]
              note: "The user requests access by opening the retained files; this is human read-back, not unsolicited model delivery."
          records: [memory.md#mem-obj-factual-record]
          note: "The explicit user file-access path has a described requesting consumer."
        - scope: "Private history and published team knowledge reaching later AI consumers"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-rte-context-use, runtime.md#rt-rte-capture-share, runtime.md#rt-rte-provider-message]
          note: "The documents claim context use but do not distinguish requested retrieval, automatic injection and mere synchronized availability."
        - scope: "Skills and other opaque retained-input alternatives reaching later consumers"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-rte-skill-sync, runtime.md#rt-obj-skills, epistemic.md#epi-obj-capture, epistemic.md#epi-obj-org-version, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
          note: "Invocation triggers, loading channels and independent retention are unresolved; one-click publication is not a read request."
      records: [memory.md#mem-obj-factual-record, epistemic.md#epi-rte-context-use, runtime.md#rt-rte-capture-share, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-skill-sync, runtime.md#rt-obj-skills, epistemic.md#epi-obj-capture, epistemic.md#epi-obj-org-version]
      note: "Human file pull is supported; opaque AI and skill routes prevent a pull-only or complete direction assessment."
    read_back_signal:
      assessment: not-determinable
      units:
        - scope: "Human-requested opening of local note files"
          assessment: inapplicable
          findings: []
          records: [memory.md#mem-obj-factual-record]
          note: "This unit is requested file access, not push; a filename on that request establishes no push selector."
        - scope: "Possible private/team context push, skill delivery and opaque integration/provider alternatives"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-rte-context-use, runtime.md#rt-rte-skill-sync, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
          note: "No actual push operation has a disclosed trigger, selector input and selected retained part; immediate team availability does not establish coarse or identifier selection."
      records: [memory.md#mem-obj-factual-record, epistemic.md#epi-rte-context-use, runtime.md#rt-rte-skill-sync, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
      note: "The known human pull unit cannot make the whole signal axis inapplicable while model routes remain unresolved."
    trace_learning:
      assessment: not-determinable
      units:
        - scope: "Meeting narrative to private notes, organizational material and later AI context"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-obj-capture, epistemic.md#epi-rte-private-synthesis, epistemic.md#epi-rte-org-draft, epistemic.md#epi-rte-context-use, epistemic.md#epi-rte-share-approval]
          note: "Derived retained context is claimed, but automatic private admission and original trace content are unresolved. Manual team publication alone does not warrant a negative for all precursor writes."
        - scope: "Skill updates, optional integration outputs, conversation summaries and provider context writes"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-skills, runtime.md#rt-rte-skill-sync, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
          note: "No recorded automatic trace-fed update and durable later-consumed result can be classified; opaque alternatives remain included rather than absent."
      records: [epistemic.md#epi-obj-capture, epistemic.md#epi-rte-private-synthesis, epistemic.md#epi-rte-org-draft, epistemic.md#epi-rte-context-use, epistemic.md#epi-rte-share-approval, runtime.md#rt-obj-skills, runtime.md#rt-rte-skill-sync, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
      note: "Neither yes nor bounded no is established. The context-payoff claim concerns benefit, not a qualifying automatic trace-fed write."
    trace_source:
      assessment: not-determinable
      units:
        - scope: "Original input to any qualifying private synthesis or organizational update"
          assessment: not-determinable
          findings: []
          records: [epistemic.md#epi-obj-capture, epistemic.md#epi-rte-private-synthesis, epistemic.md#epi-rte-org-draft]
          note: "A retrospective user narrative about a meeting is not by itself a recorded agent-session log or event stream. No qualifying automatic trace-fed write and source content are established."
        - scope: "Original inputs to possible skill, Slack/voice, transcript or provider-context updates"
          assessment: not-determinable
          findings: []
          records: [runtime.md#rt-obj-skills, runtime.md#rt-rte-skill-sync, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
          note: "Integration names and task examples do not establish original trace content or a qualifying write; mixed or opaque inputs remain unresolved."
      records: [epistemic.md#epi-obj-capture, epistemic.md#epi-rte-private-synthesis, epistemic.md#epi-rte-org-draft, runtime.md#rt-obj-skills, runtime.md#rt-rte-skill-sync, runtime.md#rt-rte-provider-message, runtime.md#rt-rte-capture-share]
      note: "Unresolved trace learning prevents inapplicability; no source class is inferred from a conversational UI, voice label or synchronization mechanism."
---

# Sig memory profile

## Comparison rationale

The accepted records describe a memory design, not inspected application wiring.
All positive findings therefore retain a claimed basis. Reading every release
document does not resolve the unavailable application loop. No axis asserts a
complete inventory merely because one local part is classified.

The two duplicate private-object supersessions in the supplied reconciliation
resolve the epistemic factual and personal objects to
[MEM-OBJ-factual-record](memory.md#mem-obj-factual-record) and
[MEM-OBJ-personal-layer](memory.md#mem-obj-personal-layer). Their epistemic
route findings still apply. The organizational proposal
[EPI-OBJ-org-version](epistemic.md#epi-obj-org-version) remains distinct from
[MEM-OBJ-team-knowledge](memory.md#mem-obj-team-knowledge): human selection and
approval intervene. No unchanged-content identity is assumed.

The lineage findings distinguish authoring the input, Sig compiling a derived
private account, preparing a proposal, and importing approved material or skills
at another installation. Other-compiled names a derivation path, not a claim of
faithful compression. The indeterminate semantic relation recorded by
[EPI-RTE-private-synthesis](epistemic.md#epi-rte-private-synthesis) and
[EPI-RTE-org-draft](epistemic.md#epi-rte-org-draft) prevents choosing a curation
operation. The product's word synthesis is not evidence for the controlled
value synthesize.

Direct human reading supports a local pull route. It does not settle whether
later AI context is retrieved on request or automatically injected.
[EPI-RTE-context-use](epistemic.md#epi-rte-context-use) supports claimed knowledge
force at intended later consumers, while retaining unknown selected content and
personal-layer provider inclusion. Synchronization and immediate availability
establish no push selector. Likewise, the explicit human decision in
[EPI-RTE-share-approval](epistemic.md#epi-rte-share-approval) classifies publication
admission, not local private admission, recipient review, or a retained
validation/enforcement object.

Trace learning remains unresolved independently of advertised AI benefit.
Neither user-initiated capture nor Sig's physical file write settles local
admission control. No original recorded trace source and qualifying automatic
update chain are established. The records do not provide bounded absences for
skills, optional integrations, transcripts or provider context. Those branches
cannot be dropped to produce a negative or an inapplicable trace-source axis.

Diagnostic linkage, telemetry and public support intake are excluded from this
memory boundary rather than classified as app context. Their records identify
no admitted repair or later app-change consumer:
[MEM-OBJ-install-id](memory.md#mem-obj-install-id),
[RT-RTE-analytics-egress](runtime.md#rt-rte-analytics-egress) and
[RT-RTE-product-feedback](runtime.md#rt-rte-product-feedback). This exclusion does
not claim they lack storage or diagnostic use.

Source-read log: none. Classification used only the supplied accepted members,
reconciliation and governing contracts; no source ambiguity required a new read.
