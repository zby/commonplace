---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Sig memory report: declared local factual and personal notes, approved team knowledge and reusable workflows in release documentation."
run-id: AAS-2026-10-14-sig-releases-50379145ac31-01
source-identity: "https://github.com/sig-ai-app/sig-releases"
reviewed-boundary: "314bbea9d1cef911cea0f201eec66a57c2e59020"
---

# Sig memory report

## Boundary and evidence

This account covers Sig's declared retained work context, not an inspected application implementation. The frozen revision and partial-loop boundary are those of [boundary](boundary.md#boundary-and-evidence). Direct reads covered SRC-1, `README.md`, `RELEASE_NOTES_v0.1.0-beta.md`, `ANALYTICS.md` and all three `.github/ISSUE_TEMPLATE/` YAML files. A Git HEAD and tracked-tree recheck matched the supplied revision and inventory. The evidence layers are doctrine/design and reported operation, not observed runs.

The memory scope follows the supplied runtime's capture, team publication, skills, provider, telemetry and feedback paths. The inventory has no tracked executable CLI dispatch, hooks, registered tools, exposed service/library operations, prompt bodies, evaluators or application drivers to check against those routes. This is a source-availability limit, not evidence that the application lacks such surfaces. Release binaries and external services remain outside the frozen artifact; screenshots remain excluded from visual inspection. Provider state and remote storage implementations are opaque.

| Operation or included part | Direct source anchor, SRC-1 | Coverage and prevented conclusion |
|---|---|---|
| Narrative acquisition and local synthesis | `README.md`; `RELEASE_NOTES_v0.1.0-beta.md` | [RT-RTE-capture-share](runtime.md#rt-rte-capture-share); [MEM-OBJ-factual-record](#mem-obj-factual-record), [MEM-OBJ-personal-layer](#mem-obj-personal-layer). Raw input retention, model calls and per-local-write approval unspecified. |
| Organizational draft, admission and git synchronization | `README.md` | [RT-RTE-capture-share](runtime.md#rt-rte-capture-share); [MEM-OBJ-team-knowledge](#mem-obj-team-knowledge). Remote format, merge/conflict, recipient checks and withdrawal unspecified. |
| Private history and teammate context read-back | `README.md` | Annotation on [RT-RTE-capture-share](runtime.md#rt-rte-capture-share). Claimed consumers; selection, payload and budget unspecified. |
| Reusable skill admission, sync and invocation | `README.md`; `ANALYTICS.md` | [RT-OBJ-skills](runtime.md#rt-obj-skills), [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync). No bodies, loader, executor or rationale reader. |
| Chat/provider context and response | `README.md`; `ANALYTICS.md` | [RT-RTE-provider-message](runtime.md#rt-rte-provider-message). No transcript reload, context-filtering or provider-memory contract. |
| Local access, deletion and uninstall retention | `README.md`; `RELEASE_NOTES_v0.1.0-beta.md` | Local files explicitly readable and deletable; propagation of edits/deletion, caches and remote retraction unresolved. |
| Slack, voice and optional team connection | `README.md`; `ANALYTICS.md` | Connections off by default; Slack sync counts mentioned. Acquisition, selection, durable results and later consumers unspecified; cannot classify an integration-specific memory route. |
| End-of-day label, people/projects/weeks/thoughts | `README.md` | Product vocabulary, not disclosed schemas or separate maintenance routes. Cannot infer a nightly consolidation job or structured entity store. |
| Analytics, install linkage, explicit feedback | `ANALYTICS.md` | [RT-RTE-analytics-egress](runtime.md#rt-rte-analytics-egress); [MEM-OBJ-install-id](#mem-obj-install-id). Metadata distinct from knowledge; no automatic app read-back established. |
| Public issue intake and evaluation | `.github/ISSUE_TEMPLATE/bug_report.yml`; `.github/ISSUE_TEMPLATE/feedback.yml`; `.github/ISSUE_TEMPLATE/config.yml` | [RT-RTE-product-feedback](runtime.md#rt-rte-product-feedback). Reporter review only; no evaluator, repair-admission or app-consumer loop supplied. |

## Core ideas

Sig declares a split between factual work records, private interpretations and deliberately published organizational material. Synthesis changes the representation of a user's narrative; team publication adds a separate human admission decision. Starting capture does not establish approval of each private write. These distinctions are retained in [RT-RTE-capture-share](runtime.md#rt-rte-capture-share) and its annotation below.

Local markdown gives the user an inspectable and deletable retention surface. That does not establish that external edits are indexed or adopted by Sig. Git-backed team delivery is claimed to make knowledge available to a teammate's Sig, not to guarantee faithful selection, compliance or improved answers. Source trust is bounded by user narrative and review; the label “facts” supplies no truth-checking procedure (SRC-1, `README.md`).

No context budget, selector, compaction, task-frame isolation, summary checkpoint or reload protocol is disclosed in the inspected documents. The stack-frame lens has no evidenced mechanism to apply to here. The documented store is external to a model window, but the documents do not show when any stored value is copied into that window. This prevents a working-context control classification beyond the claimed supply of retained context (SRC-1, `README.md`; [RT-RTE-provider-message](runtime.md#rt-rte-provider-message)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-factual-record
Label: Factual record

This is the factual part of the private structured note, distinct from its personal interpretation and from approved team text. It is a retained output of [RT-RTE-capture-share](runtime.md#rt-rte-capture-share), not a duplicate route or a reusable [RT-OBJ-skills](runtime.md#rt-obj-skills) workflow. No supplied operative-object record denotes this part. SRC-1, `README.md` and `RELEASE_NOTES_v0.1.0-beta.md` describe local plain markdown; its operative content is natural language interpreted by the user and, as advertised, later AI. File structure and any symbolic metadata are uninspected.

> **Your memory stays on your computer.** People, projects, weeks, thoughts — Sig writes them as plain markdown files in the folder you choose during setup. There is no Sig server holding your content. Open the folder, read the files, copy them, or delete them anytime.
> --- `README.md`

Lineage is user meeting narrative → Sig structuring → factual note. Initial migration/import provenance and persistence of raw narrative are unspecified. The user supplies input and chooses the storage directory; Sig authors the structure and is the declared physical writer. Per-note local approval and validation are unspecified. The user can inspect or delete files. Private history is advertised as later AI context, but the consumer payload and authoritative force are not shown. Storage survives uninstall; reindexing, correction propagation and expiry are uninspected. Documentation supports a claimed material artifact, not a verified schema or factual accuracy.

#### MEM-OBJ-personal-layer
Label: Personal layer

The personal layer is the retained user's interpretation, separate in meaning and sharing policy from [MEM-OBJ-factual-record](#mem-obj-factual-record). It is another output of [RT-RTE-capture-share](runtime.md#rt-rte-capture-share), with no supplied operative-object counterpart. SRC-1, `README.md` supplies the distinction:

> **Your thinking, not just the facts** — Sig saves two things: the factual record, and your personal layer — your read on what it means, your honest take. The personal layer stays on your machine and is never shared
> --- `README.md`

Encoding is natural-language interpretation; substrate is declared local markdown under the general local-memory contract quoted above. Separate files versus sections are unspecified. Lineage is the user's take as structured by Sig, not an inspected derivation of beliefs from objective evidence. The local admission mechanism and write-agency limits match the factual record. The stated team-exclusion policy is distinct from unknown provider-message inclusion: [RT-CLM-private-sharing](runtime.md#rt-clm-private-sharing) already bounds that ambiguity. Intended later private-context use does not establish instruction priority or whether any specific invocation receives this part. Reasons may occur in a user's interpretation, but their retention as explicit rationale and later use are uninspected.

#### MEM-OBJ-team-knowledge
Label: Team knowledge

This object is approved organizational content in the central team knowledge base. It differs from local private notes and reusable [RT-OBJ-skills](runtime.md#rt-obj-skills). Its production/delivery route is already [RT-RTE-capture-share](runtime.md#rt-rte-capture-share); no supplied object denotes the published material. SRC-1, `README.md` supplies the synchronization and consumer claim in that route's retained quotation.

Lineage is capture → private synthesis → clean organizational proposal → user-selected approved text → team publication. Natural-language organizational content is established by the exact-text review contract; remote serialization, repository layout, access metadata, server location and version retention are unspecified. Git is a synchronization mechanism, not an established content schema. The user has the declared publication veto; Sig proposes the version and git performs background transport. Recipient admission/review is unspecified. Later consumers are the team and teammates' Sig installations. Delivery as context is claimed, but model-visible selection and behavioral authority are uninspected. The transformation can omit private material, so the published object cannot be assumed to preserve the capture or its reasons completely. Remote correction, rejection after publication and withdrawal are unspecified.

#### MEM-OBJ-install-id
Label: Install ID

This is access/linkage metadata, not retained knowledge or a skill. It is associated with [RT-RTE-analytics-egress](runtime.md#rt-rte-analytics-egress), but no supplied object denotes it. SRC-1, `ANALYTICS.md` states:

> Every install generates a random anonymous ID on first launch. The analytics backend uses it to group one install's events. It is not joined to any external identity system. You can find it under **Settings → Advanced → Diagnostic** and reset it by deleting the ID files (the next launch generates a new one; events before and after the reset will not be linked).
> --- `ANALYTICS.md`

Representation is a symbolic grouping token; exact encoding and file locations are unspecified. Local ID files are the stated substrate; backend storage is opaque. Software generates the initial and replacement IDs, with no per-ID human approval stated. A user can trigger replacement by deletion. The actual named consumer is the analytics backend's grouping operation, not the foreground AI. This metadata has linkage authority only; it supplies no content-learning evidence. Reset is claimed to break linkage, not delete earlier events. Implementation and operation remain uninspected.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-capture-share](runtime.md#rt-rte-capture-share)

Memory outputs are the separately classified [MEM-OBJ-factual-record](#mem-obj-factual-record), [MEM-OBJ-personal-layer](#mem-obj-personal-layer) and [MEM-OBJ-team-knowledge](#mem-obj-team-knowledge). The raw narrative is an input; its independent persistence is unresolved. The structured note is derived material, but no synthesis prompt or evaluator shows factual fidelity. No rationale-retention requirement or later rationale reader is disclosed (SRC-1, `README.md`).

Read-back has two claimed consumer surfaces: local history used by AI and team material arriving at a teammate's Sig. The first is advertised across accumulating weeks; the second is described as immediate after synchronization. The selector's trigger and inputs, selected portions, relevance criterion, token budget and final model-delivery channel are unspecified. User selection of share content is a publication decision, not evidence of request-targeted retrieval. The model receives no established instruction authority from this documentation alone. The route's existing quotation supplies the load-bearing delivery claim (SRC-1, `README.md`).

Local deletion is a declared user control, and uninstall is expressly not withdrawal of retained notes:

> Drag Sig from Applications to the Trash (macOS), or remove the package via your package manager (Linux). Your captures stay on your computer as plain markdown in the folder you picked during setup. Delete that folder if you want them gone.
> --- `RELEASE_NOTES_v0.1.0-beta.md`

This establishes a documentary local-retention horizon across app uninstall, not remote deletion, context-cache invalidation or successful future read-back. Whether manual edits alter later AI inputs is unresolved.

#### On [RT-OBJ-skills](runtime.md#rt-obj-skills)

The retained workflow may shape later task behavior, but its actual body and encoding are unavailable. A source-native workflow label does not establish natural-language instructions, symbolic code or a mixed artifact. Storage, initial author, derivation from task traces, retained reasons and actual execution authority are uninspected. The closest source support is the skill-sharing quotation in the supplied record (SRC-1, `README.md`). Analytics explicitly mentions skill runs and outputs, but not their adoption as memory (SRC-1, `ANALYTICS.md`).

#### On [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync)

The retained input is the chosen reusable workflow; intended later consumers are teammates' installations performing recurring user tasks. Source says one-click sharing and hidden git sync, not an automatic invocation trigger. Recipient selection, budget, loading channel and conflict/revocation policy are unresolved. Publication availability is not proof of activation. There is no evidence of a raw-task-trace → revised skill → later task-consumer chain, or of retained reasons being read during execution (SRC-1, `README.md`; `ANALYTICS.md`).

#### On [RT-RTE-provider-message](runtime.md#rt-rte-provider-message)

The direct provider channel is documented, but its context assembly is not. The retained private/team/skill subset, transcript storage, summary checkpoints, provider-side state and content exclusion rules are uninspected. Thus the advertised history payoff cannot establish that a particular provider request contains either all history or the personal layer. Current message delivery alone is not retained-memory read-back (SRC-1, `README.md`; `ANALYTICS.md`).

#### On [RT-RTE-analytics-egress](runtime.md#rt-rte-analytics-egress)

Declared payloads include counts, skill success/duration, sanitized errors, connection state and explicitly submitted comment text. These are traces or feedback, not a disclosed derived knowledge artifact delivered back to Sig. [MEM-OBJ-install-id](#mem-obj-install-id) supplies linkage metadata. The document says diagnostics inform crash investigation and prioritization, but specifies no retained repair, accepted change or later app consumer (SRC-1, `ANALYTICS.md`). Analytics rejection by allowlist is a claimed pre-egress filter, not a knowledge-correctness check. Backend retention and event withdrawal remain unresolved.

## Write side

Acquisition is user narrative, with optional voice and Slack connections mentioned but not traced to durable notes. Sig's synthesis and organizational drafting are claimed transformations, not observed curation. The user authors the narrative; Sig supplies structured text; physical markdown writing and a separately approved publication are distinct. The supplied route records establish these admission boundaries without assuming that a human-initiated workflow approves every local output (SRC-1, `README.md`; [RT-RTE-capture-share](runtime.md#rt-rte-capture-share)).

The documentary raw-to-derived-to-later-consumer chain is meeting narrative → private factual/personal notes → intended later private AI context, plus organizational drafting → human-approved team text → teammate context. The original narrative, alternative summaries/checkpoints and rationale linkage are unresolved. No transcript-driven compaction or automated skill revision is disclosed in the inspected texts. This prevents establishing automatic learning from retained execution traces, without denying the claimed narrative-fed synthesis (SRC-1, `README.md`; [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync)).

Rejection is specifically the user's ability not to send a proposed organizational share. Local deletion and uninstall retention are quoted above. External editing is possible as file access, but a reload/adoption path is not specified. No remote retraction, stale-material suppression, automatic maintenance or correctness evaluation is established. The separate feedback and analytics paths may retain human reports or diagnostics; they do not establish revision of the memory corpus, skills or production app ([RT-RTE-product-feedback](runtime.md#rt-rte-product-feedback), [RT-RTE-analytics-egress](runtime.md#rt-rte-analytics-egress); SRC-1, `.github/ISSUE_TEMPLATE/bug_report.yml`, `.github/ISSUE_TEMPLATE/feedback.yml`, `ANALYTICS.md`).

## Read-back

The strongest documented read-back is published knowledge reaching a teammate's Sig as context. Automatic git synchronization is the delivery mechanism, but the source does not specify whether context injection is pushed immediately, selected upon a later request, or merely made available for retrieval. Synchronization therefore does not establish an unsolicited model-input push selector ([RT-RTE-capture-share](runtime.md#rt-rte-capture-share); SRC-1, `README.md`).

Private work history is advertised to make later AI conversations more informed, but the exact consumer request, selector and budget are unspecified. The user can independently read stored files; that direct human access does not supply the missing model route. Skills have a claimed team distribution route and recurring-task purpose, without a disclosed activation mechanism. Analytics has a named grouping consumer and diagnostic purpose, not an app-context route. These differences prevent treating every retained item as model memory ([MEM-OBJ-install-id](#mem-obj-install-id), [RT-RTE-provider-message](runtime.md#rt-rte-provider-message), [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync); SRC-1, `README.md`, `ANALYTICS.md`).

## Integration issues

No correction to a supplied fact is required. No new declaration duplicates a supplied operative object: three declarations identify distinct capture/publication outputs, and the fourth is analytics linkage metadata. Their closest route/object comparisons are stated in each declaration.

Unresolved questions for integration remain:

- Raw narrative retention, note schema, local-write approval, synthesis fidelity and preserved reasons are unknown. They prevent treating derived notes as validated facts or a complete trace archive ([MEM-OBJ-factual-record](#mem-obj-factual-record), [MEM-OBJ-personal-layer](#mem-obj-personal-layer); SRC-1, `README.md`).
- Team content's remote encoding, recipient checks, conflict handling and withdrawal are unknown. They prevent a consistency, trust or universal approval-enforcement conclusion ([MEM-OBJ-team-knowledge](#mem-obj-team-knowledge), [RT-RTE-capture-share](runtime.md#rt-rte-capture-share); SRC-1, `README.md`).
- Actual retained-context selection, payload, budgets and private-layer provider inclusion are unknown. They prevent read-back wiring, personal-layer network confinement and behavioral activation conclusions ([RT-RTE-provider-message](runtime.md#rt-rte-provider-message), [RT-CLM-private-sharing](runtime.md#rt-clm-private-sharing); SRC-1, `README.md`).
- Skill encoding, admission, execution authority, provenance and reason consumption are unknown. They prevent classifying skills as executable extensions or trace-learned instructions ([RT-OBJ-skills](runtime.md#rt-obj-skills), [RT-RTE-skill-sync](runtime.md#rt-rte-skill-sync); SRC-1, `README.md`).
- Optional integration acquisition, end-of-day processing and context compaction/isolation are not disclosed. They prevent a complete application-loop inventory, not completion of this release-document account ([RT-RTE-capture-share](runtime.md#rt-rte-capture-share); SRC-1, `README.md`, `ANALYTICS.md`).
- Local deletion propagation, analytics retention and feedback-to-change consumers are unknown. They prevent claiming complete withdrawal or automatic improvement ([MEM-OBJ-install-id](#mem-obj-install-id), [RT-RTE-analytics-egress](runtime.md#rt-rte-analytics-egress), [RT-RTE-product-feedback](runtime.md#rt-rte-product-feedback); SRC-1, `ANALYTICS.md`, `RELEASE_NOTES_v0.1.0-beta.md`, `.github/ISSUE_TEMPLATE/feedback.yml`).

## Limitations and checks

The source and report identity were rechecked against the supplied boundary and runtime; method inputs were read completely. No target code or service was executed. The README's broad “nothing leaves” language was checked against provider traffic and the analytics comment exception retained in runtime: approval is scoped to team publication, not all egress. Readable/deletable markdown was also checked against uninstall retention; neither implies remote retraction. These countercases constrain privacy and maintenance conclusions without changing the supplied facts.

No execution traces, experiments, model-visible payloads or evaluator results establish activation, fidelity or benefit. The central limitation is unavailable application implementation, not unobserved behavior in otherwise inspected code. Deterministic validation is run with the invocation's prepared command; a pass checks form and quotation occurrence, not semantic acceptance.

Validation: passed `commonplace-run validate-output` for this invocation.
