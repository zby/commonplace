---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Basic Memory epistemic routes: note reliance, schema checks, prescribed research and reflection, and benchmark answer evaluation."
run-id: AAS-2026-10-16-basic-memory-46fe4c6cfdc3-01
reviewed-boundary: a72751c5d626380dedeed30f55f7a80ba3dc710d
---

# Basic Memory epistemic report

## Source-and-claim boundary

The question is what licenses reliance on Basic Memory's retained content, rather than merely making it available. Scope, exclusions and frozen evidence identity are see [boundary](boundary.md#boundary-and-evidence); sources are see its [Source register](boundary.md#source-register). The partial-loop boundary remains. Every new source finding below uses SRC-1, implementation unless labelled doctrine/design. No target execution or independent experiment was performed or supplied.

Writes and retrieved checkpoints establish content admission and supply, not factual endorsement. The schema family adds genuine executable checks and deterministic claims about note structure. The research and reflection skills add model-facing prescriptions for assessing and integrating content; they must not disappear into a system-wide negative about knowledge production. The benchmark package separately generates answers and evaluates them against references. Those checks do not automatically license ordinary note contents.

Claims assessed: [RT-CLM-persistent-notes](runtime.md#rt-clm-persistent-notes), [EPI-CLM-never-forgets](#epi-clm-never-forgets), [EPI-CLM-schema-patterns](#epi-clm-schema-patterns), [EPI-CLM-reflect-knowledge](#epi-clm-reflect-knowledge), and [EPI-CLM-qa-accuracy](#epi-clm-qa-accuracy).

| Entry point or operation | Source path, SRC-1 | Coverage and conclusion limit |
|---|---|---|
| CLI dispatch | `src/basic_memory/cli/main.py` | Direct read confirms schema, hook, tool, import, inspect, doctor, update and maintenance registrations; registration is not inspection of every command body. |
| Registered MCP operations | `src/basic_memory/mcp/tools/__init__.py` | Direct read inventories write/edit/move/delete, reads/search/context/activity, POSIX aliases, project/workspace, diagnostics, schema and ChatGPT search/fetch. Disabled UI import is not an active route. |
| Note mutation and publication | `src/basic_memory/services/note_content_writes.py`, `src/basic_memory/indexing/accepted_note_mutation_runner.py` | Supplied [RT-RTE-note-write](runtime.md#rt-rte-note-write) and [RT-RTE-note-materialization](runtime.md#rt-rte-note-materialization), not independent rereads. Their revision/conflict checks are not semantic acceptance. Full edit/move/delete service internals remain uninspected here. |
| Retrieval and embeddings | `src/basic_memory/mcp/tools/build_context.py`, `src/basic_memory/repository/embedding_provider_factory.py` | Supplied [RT-RTE-context-build](runtime.md#rt-rte-context-build), [RT-CMP-fastembed-provider](runtime.md#rt-cmp-fastembed-provider), [RT-CMP-openai-provider](runtime.md#rt-cmp-openai-provider), [RT-CMP-litellm-provider](runtime.md#rt-cmp-litellm-provider). Optional reranking, full search and cache paths remain unassessed; no relevance-quality or provider-completeness conclusion. |
| Pi capture and hook dispatch | `integrations/pi/extensions/session.ts`, `integrations/pi/extensions/index.ts`, `src/basic_memory/cli/commands/hook.py` | Direct full read of session formatter; supplied [RT-RTE-pi-checkpoint](runtime.md#rt-rte-pi-checkpoint) and [RT-RTE-hook-checkpoint](runtime.md#rt-rte-hook-checkpoint) for callbacks, injection and Python hook path. Hook archive consumption and complete adapter fidelity remain unassessed. |
| Schema validate/infer/diff | `src/basic_memory/picoschema/validator.py`, `src/basic_memory/picoschema/inference.py`, `src/basic_memory/picoschema/diff.py`, `src/basic_memory/api/v2/routers/schema_router.py`, `src/basic_memory/mcp/tools/schema.py`, `src/basic_memory/services/schema_validation_hooks.py` | Direct reads: complete three engines and observer; selected router and tool request/formatting bodies. [EPI-RTE-schema-inference](#epi-rte-schema-inference), [EPI-RTE-schema-validation](#epi-rte-schema-validation), [EPI-RTE-schema-drift](#epi-rte-schema-drift). Full resolver and repository selection correctness uninspected. |
| Withdrawal/errors | `src/basic_memory/mcp/tools/delete_note.py` | Direct selected tool bodies show API delegation and directory partial-failure/error reporting. Not an implemented truth-based retraction policy; full deletion propagation and already-delivered host-context removal uninspected. |
| Memory JSON import | `src/basic_memory/importers/memory_json_importer.py` | Direct complete importer read: external observations/relations become Markdown entities, missing names skipped, exceptions produce failed import result. Downstream base writer and other importers/watch ingestion untraced; no exhaustive import-fidelity or admission conclusion. |
| Research and consolidation | `skills/memory-research/SKILL.md`, `skills/memory-reflect/SKILL.md` | Direct complete doctrine reads, [EPI-RTE-research-note](#epi-rte-research-note), [EPI-RTE-reflect-notes](#epi-rte-reflect-notes). Lifecycle archiving guidance supplied by boundary/runtime. Other curation/defrag/research variants uninspected, preventing complete maintenance-policy coverage. |
| Benchmark QA | `benchmarks/src/basic_memory_benchmarks/scoring/qa.py` | Direct bounded reads cover generation, parsing, context assembly, judging, rejudging and aggregation. [EPI-RTE-qa-answer](#epi-rte-qa-answer), [EPI-RTE-qa-judge](#epi-rte-qa-judge). No benchmark result or causal comparison inspected. Other retrieval/agent-task graders and dataset provenance unassessed. |
| Other first-party hosts and prompts | `integrations/hermes`, `integrations/openclaw`, `integrations/tau`, `plugins/claude-code`, `plugins/codex`, `src/basic_memory/mcp/prompts` | Discovered, implementations not inspected here. Prevents cross-host or system-complete negatives about assessment, adaptation and instruction admission. |

External host model reasoning, provider weights, live cloud infrastructure, actual note corpora and deployed configurations are not captured. They prevent factual-correctness, exercised acceptance, successful continuation and benefit conclusions. Available but uninspected source paths above are inspection limits, not access failures. No supplied runtime finding requires supersession: this report adds schema, skill and QA routes the baseline explicitly left open.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-note-content](#epi-obj-note-content) | Arbitrary caller observations, facts and relations; particular proposition not determinable without a corpus | see record | see record | Content admission is not evidence-consuming factual acceptance. |
| [EPI-OBJ-capture-draft](#epi-obj-capture-draft) | User/assistant utterances and claims about session context | see record | see record | Original utterance truth unknown; extractive text is not a verified lesson. |
| [EPI-OBJ-inference-result](#epi-obj-inference-result) | Counts and proportions over supplied notes; suggested schema is a policy proposal | see record | see record | Corpus/index fidelity not checked by frequency arithmetic. |
| [EPI-OBJ-validation-result](#epi-obj-validation-result) | Structural diagnostics and pass state relative to schema/mode | see record | see record | No factual or source-truth check. |
| [EPI-OBJ-qa-case](#epi-obj-qa-case) | Generated answer and attributed judge correctness | see record | see record | Gold and model reliability not independently validated. |
| [EPI-OBJ-memory-skills](#epi-obj-memory-skills) | Prescriptions; prospective research facts and consolidated claims | see record | see record | Static instructions, not evidence the requested operations occur. |
| [RT-CMP-fastembed-provider](runtime.md#rt-cmp-fastembed-provider), [RT-CMP-openai-provider](runtime.md#rt-cmp-openai-provider), [RT-CMP-litellm-provider](runtime.md#rt-cmp-litellm-provider) | Individuated natural-language truth-apt content not determinable from dense vectors/opaque weights | see records | see records | Inference affects retrieval/advice; does not establish proposition endorsement or training. |

## Authority-route ledger

Fields owned by cited records are given by reference. All architectural statuses below concern source wiring or prescriptions, not exercised operation. A mismatch marker identifies a scope problem, not necessarily a product defect.

Route ID: [RT-RTE-note-write](runtime.md#rt-rte-note-write)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note-content](#epi-obj-note-content)
Content/update relation: no content change
Transition or check target: see route; path/revision/transaction admission, not proposition truth.
Evaluator/condition and domain: see route.
Activation and timing: see route.
Possible or observed result: see route; accepted/refused mutation, operation unobserved.
Implemented force: see route; enforcing mutation gate.
Epistemic authority and scope: no demonstrated factual license; “accepted” denotes storage mutation.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: consumer, channel, force, horizon: mutation service consumes caller request before persistence; see route.
Evidence source ID and local anchor: see route.
Claim IDs or none: [RT-CLM-persistent-notes](runtime.md#rt-clm-persistent-notes)
Mismatch marker or none: storage acceptance is not epistemic acceptance.
Gap/limit: Actual caller authorship/approval and semantic correctness unresolved.

Route ID: [RT-RTE-note-write](runtime.md#rt-rte-note-write), [RT-RTE-note-materialization](runtime.md#rt-rte-note-materialization)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note-content](#epi-obj-note-content)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: see routes; caller-authored Markdown enters accepted state and downstream storage.
Evaluator/condition and domain: see routes.
Activation and timing: see routes.
Possible or observed result: see routes; asynchronous publication may fail/conflict.
Implemented force: see routes.
Epistemic authority and scope: source warrant unknown; storage does not upgrade it.
Operational authority: behavior permitted, blocked, or changed: see routes.
Behavioral-authority path: consumer, channel, force, horizon: see routes; later note/search consumers may receive retained content.
Evidence source ID and local anchor: see routes.
Claim IDs or none: [RT-CLM-persistent-notes](runtime.md#rt-clm-persistent-notes), [EPI-CLM-never-forgets](#epi-clm-never-forgets)
Mismatch marker or none: retention before factual acceptance is not lifecycle integration.
Gap/limit: No run evidence establishes durability or downstream use.

Route ID: [RT-RTE-note-materialization](runtime.md#rt-rte-note-materialization)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note-content](#epi-obj-note-content)
Content/update relation: no content change
Transition or check target: see route; accepted version and storage bytes.
Evaluator/condition and domain: see route; checksums/preflight, not a truth oracle.
Activation and timing: see route.
Possible or observed result: see route; retry, stale retirement, external-change conflict or publication.
Implemented force: see route.
Epistemic authority and scope: version/byte correspondence only, not endorsement.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: consumer, channel, force, horizon: see route.
Evidence source ID and local anchor: see route.
Claim IDs or none: [RT-CLM-persistent-notes](runtime.md#rt-clm-persistent-notes)
Mismatch marker or none: none.
Gap/limit: Local recovery is not demonstrated cross-process or crash correctness.

Route ID: [RT-RTE-context-build](runtime.md#rt-rte-context-build), [RT-RTE-pi-checkpoint](runtime.md#rt-rte-pi-checkpoint)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-note-content](#epi-obj-note-content), [EPI-OBJ-capture-draft](#epi-obj-capture-draft)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see routes; selected graph/excerpts, not accepted conclusions.
Evaluator/condition and domain: see routes; query/timeframe/ranking/size predicates.
Activation and timing: see routes.
Possible or observed result: see routes; bounded context supply.
Implemented force: see routes and [RT-BAP-recall-data](runtime.md#rt-bap-recall-data).
Epistemic authority and scope: unchanged/unknown source warrant; clipping or omission can remove qualifications, so no guarantee of whole-claim preservation.
Operational authority: behavior permitted, blocked, or changed: see routes.
Behavioral-authority path: consumer, channel, force, horizon: see [RT-BAP-recall-data](runtime.md#rt-bap-recall-data); graph-tool caller receives selected context on request, Pi also supplies it automatically.
Evidence source ID and local anchor: see routes.
Claim IDs or none: [EPI-CLM-never-forgets](#epi-clm-never-forgets)
Mismatch marker or none: retrieval rank and continuation do not establish truth.
Gap/limit: Actual model interpretation/compliance unobserved; reshaping classifies extraction, not semantic equivalence of every excerpt.

Route ID: [RT-RTE-pi-checkpoint](runtime.md#rt-rte-pi-checkpoint)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-capture-draft](#epi-obj-capture-draft)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see route and object; user/assistant text becomes role-labelled thread and clipped opening summary.
Evaluator/condition and domain: see route; deterministic text extraction, no truth evaluator.
Activation and timing: see route.
Possible or observed result: see route; extractive checkpoint, not a model-authored lesson.
Implemented force: see route.
Epistemic authority and scope: preserves attribution for included turns, not warrant of their claims.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: consumer, channel, force, horizon: see route and [RT-BAP-recall-data](runtime.md#rt-bap-recall-data).
Evidence source ID and local anchor: SRC-1, `integrations/pi/extensions/session.ts`; see object.
Claim IDs or none: [EPI-CLM-never-forgets](#epi-clm-never-forgets)
Mismatch marker or none: synthetic started/ended timestamps are capture-time metadata, not proof of the session's actual start/end.
Gap/limit: Python hook formatter is a separate route, see [RT-RTE-hook-checkpoint](runtime.md#rt-rte-hook-checkpoint); its detailed semantic preservation remains unassessed.

Route ID: [EPI-RTE-schema-inference](#epi-rte-schema-inference)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-inference-result](#epi-obj-inference-result)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: see record; supplied note category/relation occurrences become counts/proportions.
Evaluator/condition and domain: see record; finite supplied corpus and arithmetic.
Activation and timing: see record.
Possible or observed result: see record; frequency report.
Implemented force: see record.
Epistemic authority and scope: descriptive claims about the supplied note representation only.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-schema-patterns](#epi-clm-schema-patterns)
Mismatch marker or none: frequency is not validity or external truth.
Gap/limit: Premises are indexed note data, not independently warranted external facts.

Route ID: [EPI-RTE-schema-inference](#epi-rte-schema-inference)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-inference-result](#epi-obj-inference-result)
Content/update relation: non-truth-apt policy/content update: suggested required/optional schema rules
Transition or check target: see record; observed frequency maps to a proposed field requirement.
Evaluator/condition and domain: see record; fixed thresholds.
Activation and timing: see record.
Possible or observed result: see record; suggested schema, not installed policy.
Implemented force: advisory only; no automatic schema write in inspected endpoint.
Epistemic authority and scope: no inference that common fields ought to be required universally.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record; caller may separately write schema.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-schema-patterns](#epi-clm-schema-patterns)
Mismatch marker or none: proposal is not operative adaptation of deployed checks until separately adopted.
Gap/limit: Schema adoption and later evaluation unobserved.

Route ID: [EPI-RTE-schema-validation](#epi-rte-schema-validation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-validation-result](#epi-obj-validation-result)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: see record; note structural satisfaction under resolved schema and validation mode.
Evaluator/condition and domain: see record.
Activation and timing: see record; explicitly requested read, not write admission.
Possible or observed result: see record; warnings/errors/pass, or no-schema/no-notes guidance.
Implemented force: report supply and observer callback, not rejection of previously stored note.
Epistemic authority and scope: mode-relative structure only; a warning-mode pass can include a missing required field.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-schema-patterns](#epi-clm-schema-patterns)
Mismatch marker or none: “valid” is not factual acceptance and not necessarily warning-free conformity.
Gap/limit: Injected observer effects and full schema-resolution fidelity uninspected.

Route ID: [EPI-RTE-schema-drift](#epi-rte-schema-drift)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-inference-result](#epi-obj-inference-result)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: see record; declared fields versus finite observed usage.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record; drift diagnostics, no automatic deletion or schema rewrite.
Implemented force: advisory report.
Epistemic authority and scope: configured frequency/cardinality contrasts only.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-schema-patterns](#epi-clm-schema-patterns)
Mismatch marker or none: rare does not mean false or obsolete.
Gap/limit: Zero-note input returns empty drift, not evidence of populated-corpus agreement.

Route ID: [EPI-RTE-research-note](#epi-rte-research-note)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-memory-skills](#epi-obj-memory-skills), [EPI-OBJ-note-content](#epi-obj-note-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see record; researched subject summary and proposed saved entity.
Evaluator/condition and domain: see record; external sources, assistant assessment, user approval.
Activation and timing: see record.
Possible or observed result: see record; approved/modified/rejected proposed note.
Implemented force: prescribed human saving decision, not server-enforced truth acceptance.
Epistemic authority and scope: hedged, dated, source-attributed facts as prescribed; no observed evidence-consuming factual acceptance.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: see record.
Claim IDs or none: none.
Mismatch marker or none: approval to save does not itself prove factual acceptance.
Gap/limit: No specific generated proposition allows choosing reshaping, entailment or ampliative conjecture; host/web evidence and decision trace needed.

Route ID: [EPI-RTE-reflect-notes](#epi-rte-reflect-notes)
Route function: lifecycle integration
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-memory-skills](#epi-obj-memory-skills), [EPI-OBJ-note-content](#epi-obj-note-content)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see record; claimed durable content, its source and temporal scope.
Evaluator/condition and domain: see record; assistant judges durability and explicit source-supported changes.
Activation and timing: see record.
Possible or observed result: see record; consolidated note, uncertainty marker, reflection checkpoint.
Implemented force: model-facing prescription using ordinary editing capabilities.
Epistemic authority and scope: proposed source-linked integration after durability selection; no observed factual acceptance or integration instance.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-reflect-knowledge](#epi-clm-reflect-knowledge)
Mismatch marker or none: scheduled language does not establish an installed autonomous scheduler.
Gap/limit: Actual semantic change and acceptance are not determinable from examples; no independent warrant transfer established.

Route ID: [EPI-RTE-qa-answer](#epi-rte-qa-answer)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-qa-case](#epi-obj-qa-case)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see record; retrieved context to model-generated answer.
Evaluator/condition and domain: see record; answer generation is not its own check.
Activation and timing: see record.
Possible or observed result: see record; answer/abstention/error.
Implemented force: candidate supplied to judge, not ordinary note admission.
Epistemic authority and scope: candidate only; grounding request is not compliance evidence.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-qa-accuracy](#epi-clm-qa-accuracy)
Mismatch marker or none: no concrete output establishes non-entailment, hence not classified as ampliative conjecture.
Gap/limit: Model responses and provider state unobserved.

Route ID: [EPI-RTE-qa-judge](#epi-rte-qa-judge)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-qa-case](#epi-obj-qa-case)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see record; candidate versus gold answer under fixed rubric.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record; boolean/reason or explicit error, aggregate QA accuracy.
Implemented force: enforces result parsing and metric accounting; judge semantics remain model-mediated.
Epistemic authority and scope: attributed benchmark correctness, not general factual truth or ordinary-note endorsement.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: consumer, channel, force, horizon: see record.
Evidence source ID and local anchor: see record.
Claim IDs or none: [EPI-CLM-qa-accuracy](#epi-clm-qa-accuracy)
Mismatch marker or none: rubric permits extra assertions unless contradicting gold; not a complete hallucination audit.
Gap/limit: Gold correctness, judge calibration and causal component effects unestablished.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-persistent-notes](runtime.md#rt-clm-persistent-notes) | see record | see record | see record | [RT-RTE-note-write](runtime.md#rt-rte-note-write), [RT-RTE-context-build](runtime.md#rt-rte-context-build) | None supplied | No benefit comparison | Persistence/read interfaces implemented | Actual shared use and correctness unobserved. |
| [EPI-CLM-never-forgets](#epi-clm-never-forgets) | see record | see record | see record | [RT-RTE-pi-checkpoint](runtime.md#rt-rte-pi-checkpoint), [RT-RTE-context-build](runtime.md#rt-rte-context-build) | None supplied | No continuation experiment | Retention and selected reintroduction afforded | Literal universal recall exceeds bounded extraction, selection and failure handling. |
| [EPI-CLM-schema-patterns](#epi-clm-schema-patterns) | see record | see record | see record | [EPI-RTE-schema-inference](#epi-rte-schema-inference), [EPI-RTE-schema-validation](#epi-rte-schema-validation), [EPI-RTE-schema-drift](#epi-rte-schema-drift) | None supplied | Finite representations and thresholds, not external fact checking | Pattern-derived schema suggestions and mode-relative diagnostics implemented | No automatic warranted schema adoption; no truth guarantee. |
| [EPI-CLM-reflect-knowledge](#epi-clm-reflect-knowledge) | see record | see record | see record | Ordinary mutation capability [RT-RTE-note-write](runtime.md#rt-rte-note-write); integration prescription [EPI-RTE-reflect-notes](#epi-rte-reflect-notes) | None supplied | No durability/quality comparison | Source-linked consolidation is prescribed | Actual semantic acceptance, repeated use and benefit unobserved. |
| [EPI-CLM-qa-accuracy](#epi-clm-qa-accuracy) | see record | see record | see record | [EPI-RTE-qa-answer](#epi-rte-qa-answer), [EPI-RTE-qa-judge](#epi-rte-qa-judge) | None supplied | Accuracy measures whole configured pipeline against gold/judge; no isolated component intervention | Implemented candidate scoring and aggregation | No measured accuracy, mechanism attribution or transfer established. |

## Bounded conclusion

Basic Memory's inspected write/materialization routes retain caller content under operational conflict and version rules. Those rules license mutation and byte publication, not factual reliance. Query, graph and Pi recall routes select retained material for caller/model consumption. Their behavioral force is supply/ranking/reference guidance, not enforced agreement. Imported note assertions have unknown source warrant; extraction and persistence cannot upgrade it. See [RT-RTE-note-write](runtime.md#rt-rte-note-write), [RT-RTE-note-materialization](runtime.md#rt-rte-note-materialization), [RT-RTE-context-build](runtime.md#rt-rte-context-build), and [RT-BAP-recall-data](runtime.md#rt-bap-recall-data).

The schema engines genuinely derive new descriptive propositions about finite supplied note representations. Frequency arithmetic and explicit structural predicates provide narrow warrant from those representations; they do not warrant the world-facing assertions contained in notes. Suggested required fields are policy proposals. A warning-mode “valid” note need not satisfy every required field. Validation results reach the requester and an observer seam, not an inspected core write veto, retraction loop or persisted endorsement. Drift output similarly advises rather than automatically revising knowledge. See [EPI-RTE-schema-inference](#epi-rte-schema-inference), [EPI-RTE-schema-validation](#epi-rte-schema-validation), and [EPI-RTE-schema-drift](#epi-rte-schema-drift).

Research doctrine names multi-source checking, uncertainty, dates and user approval before saving; reflection doctrine names durable-item criteria, source links, temporal revision and preserving disagreements. These are meaningful prescribed acquisition/assessment/integration paths. They establish neither a concrete accepted ampliative claim nor an executed autonomous reflection loop. Source-linked editing may implement the prescription when a host follows it, but generic service admission and human approval to save are not substitutes for a recorded evidence-consuming acceptance against a factual criterion. See [EPI-RTE-research-note](#epi-rte-research-note) and [EPI-RTE-reflect-notes](#epi-rte-reflect-notes).

The benchmark package separately generates and judges truth-apt answers. The criterion is key-gold-fact coverage without contradiction, or appropriate abstention for unanswerable gold. Its intended use is pipeline QA scoring over selected reference-bearing cases. Verdicts control metric accounting and can be rejudged; they do not license all note assertions, update model weights, or prove the proposed memory mechanism caused success. See [EPI-RTE-qa-answer](#epi-rte-qa-answer) and [EPI-RTE-qa-judge](#epi-rte-qa-judge).

No observed operation, accepted conjecture, measured future-capacity improvement or causal benefit is established by this source-only evidence. That does not erase the implemented retention, selection and schema assessment capacities. Pi supplies retained experience to later assistant context, but actual dependence and improvement are unobserved. Embedding adapters establish inference, not parameter training; exact weight identities/provider internals remain unresolved independently of text-memory updates. Research synthesis, reflection, learning, autonomy, theory building and self-improvement cannot be collapsed into one verdict. Uninspected shipped hosts, maintenance skills, evaluators and import/watch paths prevent a system-complete negative about any further epistemic or adaptation route.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-note-content
Label: Note content

Source-native Markdown notes and extracted observations/relations. Form: natural-language assertions, with symbolic metadata, links and mutation identity consumed by fixed rules. Substrate: accepted database content, materialized Markdown and derived indexes; source warrant remains unknown. Material payload part of the supplied write route, not another declaration of that route.
Part of: [RT-RTE-note-write](runtime.md#rt-rte-note-write)
Evidence: see that route's SRC-1 anchors and passages. This object is distinct from the capture draft below: generic caller content need not be a trace or checkpoint. Particular theories, premises or approved claims cannot be individuated without note instances.

#### EPI-OBJ-capture-draft
Label: CaptureDraft

Part of: [RT-RTE-pi-checkpoint](runtime.md#rt-rte-pi-checkpoint)

Payload part of that route. Form: natural-language user/assistant thread plus symbolic YAML session, branch, model and capture metadata. Substrate: TypeScript draft string before CLI write; subsequently a retained Markdown note through the parent route. Direct SRC-1 evidence: `integrations/pi/extensions/session.ts`. Text extraction excludes tool roles and nontext blocks; the full included thread is carried alongside clipped opening fields. This is not a separate summary model. Capture-time `now` is used for both metadata timestamps.

> const thread = params.turns;
> --- `integrations/pi/extensions/session.ts`

> started: now.toISOString(),
> ended: now.toISOString(),
> --- `integrations/pi/extensions/session.ts`

> ...thread.map((turn) => `- **${turn.role}:** ${turn.text}`),
> --- `integrations/pi/extensions/session.ts`

Concrete implementation deduction: with one user turn `Launch is Friday` and one tool-role result `Tests passed`, `extractSessionTurns` drops the tool result; `buildCaptureDraft` emits `- **user:** Launch is Friday` under Thread to date. The launch assertion is acquired, not newly inferred, and test success is not carried by this branch. The inclusion and omission explain why a checkpoint is not a complete evidentiary transcript. See the parent for role-filter quotation and later selection.

#### EPI-OBJ-inference-result
Label: InferenceResult

Form: symbolic per-field counts, proportions, samples, required/optional/excluded lists and a proposed schema dictionary. Substrate: in-process dataclass, returned API report and MCP text/JSON, not automatically persisted schema. Direct SRC-1: `src/basic_memory/picoschema/inference.py`, `src/basic_memory/api/v2/routers/schema_router.py`, `src/basic_memory/mcp/tools/schema.py`. Distinct from supplied graph context: it describes aggregate usage and proposes rules, rather than supplying graph facts. No supplied record counterpart after comparison with [RT-RTE-context-build](runtime.md#rt-rte-context-build).

> suggested_schema: dict[str, Any]  # Ready-to-use Picoschema YAML dict
> suggested_required: list[str]
> suggested_optional: list[str]
> excluded: list[str]  # Below threshold
> --- `src/basic_memory/picoschema/inference.py`

#### EPI-OBJ-validation-result
Label: ValidationResult

Form: symbolic pass/diagnostic lists, field statuses and matched values, with human-readable message strings. Substrate: transient dataclass/API/MCP report; no core persisted validation state established. Direct SRC-1: `src/basic_memory/picoschema/validator.py`, `src/basic_memory/services/schema_validation_hooks.py`. Distinct from mutation acceptance in [RT-RTE-note-write](runtime.md#rt-rte-note-write): this is a read-side structural report, not an accepted revision.

> passed: bool  # True if no errors (warnings are OK)
> --- `src/basic_memory/picoschema/validator.py`

#### EPI-OBJ-qa-case
Label: QACaseResult

Form: natural-language question, expected/generated answer and judge reason plus symbolic correct/error/abstention/model/accounting fields. Substrate: in-process result objects returned by scoring, with stored-case rejudging support. Artifact-file persistence plumbing not inspected. Direct SRC-1: `benchmarks/src/basic_memory_benchmarks/scoring/qa.py`. No supplied counterpart: unlike [RT-RTE-context-build](runtime.md#rt-rte-context-build), this object includes generated answers and reference-based judgments.

> expected_answer=row.expected_answer or "",
> generated_answer=answer_result.text,
> abstained=_is_abstention(answer_result.text),
> correct=correct,
> judge_reason=reason,
> --- `benchmarks/src/basic_memory_benchmarks/scoring/qa.py`

#### EPI-OBJ-memory-skills
Label: Memory Research and Memory Reflect

Form: natural-language procedural guidance, examples and scope conditions. Substrate: static shipped Markdown `skills/memory-research/SKILL.md`, `skills/memory-reflect/SKILL.md` (SRC-1, doctrine/design). They are not retained through target use. Distinct from [RT-BAP-server-instructions](runtime.md#rt-bap-server-instructions): separately loaded workflows for research approval and durable-note consolidation, not the FastMCP instruction string. Delivery/compliance depends on host skill loading. Evidence passages are retained in their routes below.

### Routes

#### EPI-RTE-schema-inference
Label: Schema inference

No supplied counterpart after comparison with [RT-RTE-context-build](runtime.md#rt-rte-context-build): this route computes usage statistics and proposed schema rules. Endpoints: requested note type → router repository selection → NoteData → inference engine → report → caller. Owner: deterministic Python. Context/effects: project note representations are read; result returned without schema persistence. SRC-1, `src/basic_memory/picoschema/inference.py`, `src/basic_memory/api/v2/routers/schema_router.py`, `src/basic_memory/mcp/tools/schema.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts/proportions, samples and suggested schema; empty input yields empty result.
- Later read-back: inapplicable — this endpoint does not persist a new schema; caller adoption is separate.
- Delegated visibility: Caller receives statistics and suggested YAML; no model delegation in the engine.
- Selection predicate: Router selects normalized note type; category/relation presence counts once per note; default required threshold .95, optional .25; majority multiplicity suggests array.
- Invalidation or expiry: inapplicable — report is a request-time snapshot, not retained state.
- Activation or effect: Proposed schema supplied as advisory output; no automatic check-policy change.
- Evidence limits: Repository/resolver fidelity and real input corpus unverified; no generalization beyond supplied representations.

Admission: open read request. Code proposes schema using fixed frequency policy; caller decides whether to save it, through separate write admission. No per-result human approval enforced by inference endpoint; no expected-answer oracle, improvement trigger or rollback required for this read-only proposal. Nothing produced here persists automatically.

> percentage=count / total,
> sample_values=category_samples.get(category, []),
> --- `src/basic_memory/picoschema/inference.py`

> if freq.percentage >= required_threshold:
>     suggested_required.append(freq.name)
> elif freq.percentage >= optional_threshold:
>     suggested_optional.append(freq.name)
> else:
>     excluded.append(freq.name)
> --- `src/basic_memory/picoschema/inference.py`

Concrete implementation deduction, no execution: two NoteData records, one with category `age` and value `old`, one without observations, no relations. Presence count is 1, total 2, proportion .5, multiplicity false. At default thresholds the suggested optional list contains `age` and schema contains `age?: string`. The count/proportion follows from the supplied finite inputs. Requiring `age` in future notes does not follow as a truth claim; the code instead proposes a policy. The value `old` is never checked for factual or numeric correctness.

#### EPI-RTE-schema-validation
Label: Schema validation

Distinct from [RT-RTE-note-write](runtime.md#rt-rte-note-write), not its admission evaluator. Endpoints: explicit MCP/API request → schema resolution and indexed note fields → validator → per-note report → observer → requester. Owner: Python evaluator; an overridable observer is a downstream seam. Target/domain: presence of observation/relation categories and metadata keys, enum membership, under resolved schema's warn/strict mode. SRC-1, `src/basic_memory/picoschema/validator.py`, `src/basic_memory/api/v2/routers/schema_router.py`, `src/basic_memory/services/schema_validation_hooks.py`, `src/basic_memory/mcp/tools/schema.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Report with warnings/errors/pass and counts; tools distinguish no notes from no schema.
- Later read-back: inapplicable — core observer is no-op and validation state is not persisted by this traced path.
- Delegated visibility: Observer receives project/note/schema identities and pass state; requester receives full diagnostics. External observer implementation uninspected.
- Selection predicate: One resolved identifier, requested note type, or schema-covered types; notes without resolved schema skipped.
- Invalidation or expiry: inapplicable — request-time report, not enduring endorsement; schema files are read for current definitions.
- Activation or effect: Pass drives displayed valid label/counts and observer notification; no inspected write veto, note deletion or factual retraction.
- Evidence limits: Mode changes meaning of passed; field presence does not verify assertion truth or entity-target type. Full resolver and repository freshness uninspected.

Open validation operation: user/model caller chooses scope; program judges structural target and can report failure, not veto a previous save. Schema is the structural reference, not an expected factual answer oracle. A custom observer may add effects, but core does not. Required-field absence under warn appends warning and keeps initial passed true; under strict appends error and sets false. Thus one missing required `age` observation yields warning-mode pass and strict-mode failure without changing the note. This implementation deduction falsifies the stronger reading that every “valid” note satisfies every required field.

> case "warn":
>     result.warnings.append(message)
> case "strict":
>     result.errors.append(message)
>     result.passed = False
> --- `src/basic_memory/picoschema/validator.py`

> status = "valid" if r.passed else "INVALID"
> --- `src/basic_memory/mcp/tools/schema.py`

> Validation is the only place that knows whether a note actually satisfies its
> schema: nothing on the write path runs it, and no validation state is stored on
> the entity.
> --- `src/basic_memory/services/schema_validation_hooks.py`

The last passage is an implementation-module contract, not standalone proof about all mutation paths. The inspected validator/router and supplied write route support the bounded separation above.

> await observer.on_notes_validated(
>     project_external_id=project_external_id,
>     outcomes=outcomes,
> )
> return report
> --- `src/basic_memory/api/v2/routers/schema_router.py`

#### EPI-RTE-schema-drift
Label: Schema drift

No supplied counterpart after comparison with [RT-RTE-context-build](runtime.md#rt-rte-context-build). Endpoints: requested type → resolved schema and note representations → usage analysis → diff → report. Owner: deterministic Python. SRC-1, `src/basic_memory/picoschema/diff.py`, `src/basic_memory/api/v2/routers/schema_router.py`, `src/basic_memory/mcp/tools/schema.py`. Target/domain: schema field-name presence and typical multiplicity versus supplied finite note usage, not claim truth.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: New, dropped and cardinality-change diagnostics; missing schema signalled separately.
- Later read-back: inapplicable — report does not persist changes.
- Delegated visibility: Caller receives report text/JSON; no isolated model call in diff engine.
- Selection predicate: Undeclared field at least .25 frequency is new; declared below .10 or missing is dropped; majority multiplicity determines array contrast.
- Invalidation or expiry: inapplicable — snapshot output only.
- Activation or effect: Advisory diagnosis returned; no automatic schema rewrite, deletion or fact withdrawal.
- Evidence limits: Empty input yields empty drift; name-keyed merge can conflate observation and relation names. Threshold conformity is not semantic validity.

Open request, fixed code comparison; caller chooses whether to act. Schema/usage are comparison references, not factual answer oracle. No autonomous improvement trigger, admission or rollback in this read-only operation.

> total = len(notes)
> if total == 0:
>     return SchemaDrift()
> --- `src/basic_memory/picoschema/diff.py`

> all_freq_by_name = {**obs_freq_by_name, **rel_freq_by_name}
> --- `src/basic_memory/picoschema/diff.py`

> if freq.name not in schema_field_names and freq.percentage >= new_field_threshold:
>     result.new_fields.append(freq)
> --- `src/basic_memory/picoschema/diff.py`

#### EPI-RTE-research-note
Label: Research note

Distinct from [RT-RTE-note-write](runtime.md#rt-rte-note-write): upstream source research, summary assessment and saving approval prescribed by a shipped skill. Endpoints: user subject → host web search → assistant source-attributed summary → user yes/no/modify → note write/update. Owner: prescribed assistant plus user; web tool is external and explicitly not included in Basic Memory. SRC-1, `skills/memory-research/SKILL.md`, doctrine/design.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Prescribed structured summary and creation proposal.
- Later read-back: Prescribed saved note may enter ordinary search/context; no executed instance supplied.
- Delegated visibility: Host web provider sees research queries; skill warns against sending private note content. No sub-agent prescribed.
- Selection predicate: Search current multiple sources, existing-note name variants; hedge estimates, prefer primary sources for exact figures.
- Invalidation or expiry: Date/source qualifiers prescribed; update existing note rather than duplicate. Complete rollback protocol not prescribed here.
- Activation or effect: Advisory skill asks user approval before creation; ordinary write service does not enforce that workflow.
- Evidence limits: No specific research proposition, evidence set, acceptance decision or host compliance captured; semantic relation indeterminate.

Open user request. Assistant proposes findings; human decides creation and what to include. This is a saving veto, not necessarily a factual-accuracy criterion. No fixed expected-answer oracle or capacity-improvement trigger. User edits/declines can prevent saving; ordinary mutation checks govern actual I/O. Retained result would be a structured note with sources, not provider parameters.

> Research an external subject, synthesize what you find, and create a structured Basic Memory entity — with the user's approval.
> --- `skills/memory-research/SKILL.md`

> **Store source URLs.** Include the URLs you consulted, either in observations or a Sources section. This enables the user to verify and dig deeper.
> --- `skills/memory-research/SKILL.md`

> **Always web search.** Don't rely on training data alone. Research should reflect current, verifiable information.
> --- `skills/memory-research/SKILL.md`

#### EPI-RTE-reflect-notes
Label: Reflect notes

Distinct from supplied write/checkpoint routes: prescribed durability assessment and source-linked consolidation, not extractive capture. Endpoints: previous reflection checkpoint → changed notes read in full → assistant durability/source assessment → existing-note update or new note → source links and reflection record → next reflection. Owner: prescribed assistant. SRC-1, `skills/memory-reflect/SKILL.md`, doctrine/design.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Prescribed consolidated notes and dated reflection note recording reviewed/updated/created/unsure items.
- Later read-back: Next reflection starts from checkpoint; topic notes remain ordinary searchable content. Actual recurrence unobserved.
- Delegated visibility: Assistant reads changed and durable notes; no isolated model delegation prescribed.
- Selection predicate: Last reflection/date window, skip already reviewed unchanged notes; keep lasting decisions, lessons, preferences, ownership and commitments; skip transient or already recorded details.
- Invalidation or expiry: Close dated old fact range only when source states change/time; otherwise preserve both marked needs confirmation. Keep raw notes. Expected checksum asks reread/reconsider on conflict.
- Activation or effect: Advisory instruction may lead to note edits and source relations through ordinary tools; no inspected automatic scheduler or enforceable semantic gate.
- Evidence limits: Criteria judge durability and source-supported change, not an infallible truth oracle. No concrete accepted integration or model-formulated criticism trace supplied.

Open on-demand/heartbeat prescription, not bounded experiment. Assistant proposes and judges durable items; per-item human approval is not prescribed here. Original notes are evidence, not expected answers. Fixed guidance shapes what is retained; software checksum can reject stale revision, while semantic choice remains model-mediated. Recovery is reread/redecide on conflict; old/raw facts are kept rather than destroyed. Result would be source-linked changed topic notes and a checkpoint, not demonstrated improved capacity.

> Do this only when the source says what changed
> and when; if it only disagrees, record both with "(needs confirmation)".
> --- `skills/memory-reflect/SKILL.md`

> **Link back**: every consolidated fact names its source, e.g.
> `- derived_from [[2026-10-14 Launch Sync]]`, so a reader can check it.
> --- `skills/memory-reflect/SKILL.md`

> Write one note per reflection in `reflections/`, titled with the date and time
> so two runs on one day get separate notes and the newest sorts first. The next
> reflection starts from it:
> --- `skills/memory-reflect/SKILL.md`

The instruction does not individuate a formulated theory being criticized. Conditional theory-builder conditions are therefore not established for an actual theory route here; neither opacity of host reasoning nor this skill name establishes content-directed criticism, learning or autonomy. It prescribes a self-description of reviewed note operations, but no captured bidirectional reflective operation or objective-driven improvement attribution follows.

#### EPI-RTE-qa-answer
Label: QA answer

No supplied counterpart: benchmark-side generation, not runtime context return. Endpoints: selected reference-bearing retrieval rows → date-aware question/context assembly → answer prompt → LLMRunner → candidate answer → judge route. Owner: benchmark code and configured answer model. SRC-1, `benchmarks/src/basic_memory_benchmarks/scoring/qa.py`. Context uses up to ten ranked hits, 12,000 text characters by default with per-hit allocation; empty assembled hits can fall back to stored legacy context. Headers are additional formatting. Models and parameters behind LLMRunner remain uninspected here: no exact immutable weight identity or training behavior established, and endpoint mutability not determined.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Candidate text or error, then case result via scoring driver.
- Later read-back: Stored cases can be rejudged without answer regeneration; artifact persistence implementation uninspected.
- Delegated visibility: Answer model receives question and selected retrieved text, not gold answer in its answer prompt.
- Selection predicate: run_qa selects rows with expected answers; context assembly uses ranked hits and text budgets.
- Invalidation or expiry: Rejudging preserves generated answer; regeneration would be a separate run. No ordinary-note invalidation occurs.
- Activation or effect: Candidate becomes judge input, not an admitted knowledge note or changed model policy.
- Evidence limits: No observed output, gold provenance, runner internals or actual model version inspected. Grounding/abstention instructions do not guarantee compliance.

Mode: bounded dataset evaluation. Code chooses cases; model proposes answer; separate judge evaluates. Gold is a downstream reference oracle, not guidance leaked to answerer by this prompt. No human per-answer gate or capacity-improvement update is wired in inspected scoring. Failure records errors rather than admitting answers as knowledge.

> - Answer concisely using only facts found in the retrieved memories.
> - If the memories do not contain the information needed to answer, reply with
>   exactly: {abstain}
> - Do not use outside knowledge. Do not explain your reasoning.
> --- `benchmarks/src/basic_memory_benchmarks/scoring/qa.py`

> answer_result = answerer.complete(answer_prompt)
> --- `benchmarks/src/basic_memory_benchmarks/scoring/qa.py`

#### EPI-RTE-qa-judge
Label: QA judge

Distinct from answer production above and from supplied runtime routes. Endpoints: question/gold/candidate → fixed rubric prompt → configured judge LLMRunner → boolean parser → QACaseResult → accuracy/category counts; optional rejudge preserves candidate and replaces verdict/reason/model, reports flips. Owner: model judgment plus deterministic parsing/accounting. SRC-1, `benchmarks/src/basic_memory_benchmarks/scoring/qa.py`. Target: benchmark candidate answer's gold coverage/noncontradiction or abstention, not model internals or all possible assertions. Judge provider state/weight fixity and mutable endpoint resolution remain uninspected, independently of supplied embedding component findings.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: correct boolean/reason, or explicit case error when runner/parsing fails; aggregate summary returned.
- Later read-back: Rejudge accepts stored QACaseResult objects, preserves generated answer and can change metric verdict; storage-file wiring uninspected.
- Delegated visibility: Judge sees question, gold and candidate, not the retrieved evidence itself in this prompt.
- Selection predicate: Reference-bearing rows for QA; rejudge skips cases already marked error. Parser requires JSON boolean correct.
- Invalidation or expiry: Rejudging can revise correctness and record flips; it does not correct/retract ordinary notes or change original generated answer.
- Activation or effect: correct values increment overall/category accuracy; no benchmark-to-product automatic installation or retraining path traced.
- Evidence limits: Gold may be incomplete, extra claims are allowed unless contradictory, judge calibration unverified. No run or causal intervention evidence.

Mode: bounded evaluation. Model judges against supplied gold and fixed rubric; program rejects malformed verdicts, human per-case approval is not required. Gold is the expected-answer oracle. Decision criterion/intended use/scope: key-fact coverage without contradiction, or correct abstention, for QA metric accounting on selected cases. This is a recorded scoring decision when executed, not a factual acceptance of the answer for unrestricted use. Rejudge provides review/revision capacity, not evidence of exercised improvement.

> Additional specific facts in the candidate beyond the gold answer are NOT errors;
> do not treat them as hallucination unless they directly contradict the gold.
> --- `benchmarks/src/basic_memory_benchmarks/scoring/qa.py`

> if not isinstance(payload.get("correct"), bool):
>     raise ValueError(f"Judge JSON missing boolean 'correct': {raw[:200]}")
> --- `benchmarks/src/basic_memory_benchmarks/scoring/qa.py`

> correct_count = sum(1 for case in case_results if case.correct)
> --- `benchmarks/src/basic_memory_benchmarks/scoring/qa.py:316-342`

### Claims

#### EPI-CLM-never-forgets
Label: Never forgets

Consequential public recall claim, SRC-1 `README.md`, doctrine/design. Broader than the persistent-notes claim [RT-CLM-persistent-notes](runtime.md#rt-clm-persistent-notes): the latter identifies durable shared storage, this one implies universal assistant recall. Neither is observed operation.

> ### Your AI never forgets again.
> --- `README.md`

#### EPI-CLM-schema-patterns
Label: Schema patterns

Claim: schemas emerge from usage patterns; source-native frequency thresholds define the suggestion mechanism, not independent factual truth. SRC-1, `src/basic_memory/picoschema/inference.py`, doctrine/design. No supplied counterpart; [RT-RTE-context-build](runtime.md#rt-rte-context-build) returns context rather than inferring field rules.

> Write notes freely -> Patterns emerge -> Crystallize into schema
> --- `src/basic_memory/picoschema/inference.py`

#### EPI-CLM-reflect-knowledge
Label: Reflect knowledge

Claim: review recent material and consolidate durable knowledge into notes. SRC-1, `skills/memory-reflect/SKILL.md`, doctrine/design. Distinct from extractive [RT-RTE-pi-checkpoint](runtime.md#rt-rte-pi-checkpoint); claimed assessment and consolidation rather than thread capture.

> Raw notes (meeting notes, daily logs, captures, transcripts)
> record what happened; reflection decides what of it should still be known next
> month, and puts it where someone will look for it.
> --- `skills/memory-reflect/SKILL.md`

#### EPI-CLM-qa-accuracy
Label: QA accuracy

Claim: QA measures whether retrieved context supports answering, separately from retrieval recall/MRR. SRC-1, `benchmarks/src/basic_memory_benchmarks/scoring/qa.py`, doctrine/design. No supplied counterpart after comparison with [RT-RTE-context-build](runtime.md#rt-rte-context-build); benchmark evaluation is a distinct consumer.

> Retrieval metrics (recall/MRR) measure the search layer; QA accuracy measures
> whether an LLM holding only the retrieved memories can actually answer the
> question.
> --- `benchmarks/src/basic_memory_benchmarks/scoring/qa.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
