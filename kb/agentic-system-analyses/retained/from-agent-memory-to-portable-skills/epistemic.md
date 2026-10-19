---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of From Agent Memory to Portable Skills: what source grounding, gates, review and repair license in the frozen NAMS article."
run-id: AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01
reviewed-boundary: "neo4j-article-2026-10-18-99f91d4da959"
---

# From Agent Memory to Portable Skills epistemic report

## Source-and-claim boundary

The question is whether the described NAMS skill builder produces warranted procedural knowledge, rather than merely retained instructions with provenance. This is the subsystem-only, document-grounded boundary in [boundary](boundary.md#boundary-and-evidence); source identity and layers are in its [Source register](boundary.md#source-register). SRC-1 supplies doctrine/design and attributed operation, not inspected implementation or execution. The article body and captions at `article.html` were read directly; the supplied runtime is corroborating analysis, not additional execution evidence.

The material claims are [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls), [EPI-CLM-actionable-knowledge](#epi-clm-actionable-knowledge), and [EPI-CLM-graph-validity](#epi-clm-graph-validity). The assessed routes cover initial generation, gates, pending retention, human review, delivery, contradiction flags and repair. Upstream extraction and downstream host execution remain excluded as in the boundary. No system-complete negative about NAMS follows.

| Entry point or operation | Source path | Coverage | Inspection basis and limit |
|---|---|---|---|
| HTTP, MCP, dashboard triggers; scope and snapshot | SRC-1, `article.html`, “Distilling a Skill” and pipeline | [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation) | Direct document read plus supplied runtime; no frozen dispatch, hooks or registered-tool implementation exists to inspect. Path equivalence and bypass exclusion cannot be proved. |
| Consolidation, topology, thin-scope prose | SRC-1, `article.html`, “AIP Procedure Graphs” and pipeline | [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph), [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation) | Direct read; deterministic is a design attribution, not an inspected semantic transformation. |
| Synthesis and source checks | SRC-1, `article.html`, pipeline | [EPI-RTE-source-check](#epi-rte-source-check), [EPI-OBJ-claims](#epi-obj-claims) | Direct read; no prompt, model output or entailment test supplied. |
| Quality checks and withholding before persistence | SRC-1, `article.html`, pipeline | [EPI-RTE-quality-check](#epi-rte-quality-check), [EPI-RTE-pending-admission](#epi-rte-pending-admission) | Direct read; metric definitions, failure artifacts and prose validation unresolved. |
| Review, publication, Claude Code/MCP/REST delivery | SRC-1, `article.html`, review and delivery | [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery), [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) | Direct read; no review rubric, accepted instance or consumer trace. |
| Drift query and governance UI | SRC-1, `article.html`, governance | [RT-RTE-drift-check](runtime.md#rt-rte-drift-check) | Direct read; status contrast is specified, but schedule, withdrawal and downstream enforcement are not. |
| repairStep, merged/deleted sources, refusal, supersession | SRC-1, `article.html`, repair | [RT-RTE-step-repair](runtime.md#rt-rte-step-repair) | Direct read; patch release and re-review policy unresolved. |
| AIP comparison and future selection/editing | SRC-1, `article.html`, “What AIP Proposes” and “Try It Today” | [EPI-CLM-graph-validity](#epi-clm-graph-validity) | Direct read; linked paper is excluded. Planned selection/editing is not a current route. |

Missing implementation prevents enforcement guarantees and a concrete input-to-output code deduction. Missing memory/skill instances prevent individuating actual propositions or deciding whether synthesis preserves, entails or extends them. Missing review decisions prevent establishing acceptance of any actual ampliative claim. Missing host traces prevent activation and transfer conclusions. Missing experimental artifacts prevent causal attribution to NAMS or its components. These are separate limits, not evidence that the described routes do not exist.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-scoped-memory](#epi-obj-scoped-memory) | Reports of decisions, calls, results and entities; actual propositions not determinable | see record | SRC-1, `article.html`, pipeline | Historical report accuracy and extraction fidelity untested. |
| [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph) | Trace-derived ordering and bindings can assert what happened; branch instructions are policy | see record | SRC-1, `article.html`, “AIP Procedure Graphs” | No graph instance, formal semantics or checked entailment. |
| [EPI-OBJ-claims](#epi-obj-claims) | Model-written claims; particular truth-apt units not determinable | see record | SRC-1, `article.html`, synthesis paragraph | No generated claim supplied. Source references alone do not establish support. |
| [EPI-OBJ-step-annotations](#epi-obj-step-annotations) | Names, descriptions and completion criteria; prescriptions need not be truth-apt | see record | SRC-1, `article.html`, synthesis paragraph | Cannot separate factual descriptions from policy choices in absent output. |
| [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package) | Mixed claims, instructions and provenance | see record | SRC-1, `article.html`, “What Distillation Produces” | Container is not an additional epistemically accepted object. |
| [RT-CMP-llm](runtime.md#rt-cmp-llm) | Particular distributed-parametric content not determinable | see record | SRC-1, `article.html`, synthesis paragraph | Parameters, training provenance, version and endpoint mutability uninspected. |

## Authority-route ledger

Each row is a consequential function, not a second declaration of its cited route. Repeated route citations split functions inside a valid supplied container. All statuses concern this frozen document; reported availability does not raise them to implemented or observed. “Unknown source warrant” means fidelity or truth of imported reports was not established, not that provenance is absent.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation) | content transformation | doctrine only | [EPI-OBJ-scoped-memory](#epi-obj-scoped-memory) | truth-apt transformation: acquisition/import | Scoped conversations to selected snippets | Scope resolver and snapshot protocol; conversation membership and settled extraction | Before synthesis; no activation observed | Claimed bounded, redacted input | None verified | Unknown source warrant; provenance is retained in design | Limits what synthesis receives | Synthesis endpoint; snippets; input restriction; one synthesis call | SRC-1, `article.html`, pipeline | [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls) | none | 400-snippet cap may omit relevant evidence; selection details unknown. |
| [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation) | content transformation | doctrine only | [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph) | truth-apt transformation: indeterminate | Traces to clusters, ordering and branches | Deterministic outcome clustering/topology derivation, described but not inspected | Before synthesis | Claimed patterns, anti-patterns and graph, or prose fallback | None verified | Recorded succession does not establish necessary dependencies or transfer | Selects reusable procedure structure | Synthesis/validators; graph; constraining; current and retained product | SRC-1, `article.html`, graph and consolidate stages | [EPI-CLM-graph-validity](#epi-clm-graph-validity) | deterministic is not entailed | Could reshape observations or infer a new general procedure; code and example needed to decide. |
| [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation) | content transformation | doctrine only | [EPI-OBJ-claims](#epi-obj-claims), [EPI-OBJ-step-annotations](#epi-obj-step-annotations) | truth-apt transformation: indeterminate | Snippets to claims and annotations | LLM, scoped snippet context; content semantics opaque | Single synthesis stage | Claimed source-bearing text | None verified | Candidate generation only | Proposes instructions and completion criteria for gates/reviewer | Worker and reviewer; returned text; proposal; pending product | SRC-1, `article.html`, synthesis paragraph | [EPI-CLM-actionable-knowledge](#epi-clm-actionable-knowledge) | cited does not mean entailed | Reshaping, derivation and ampliative conjecture remain alternatives; non-entailment is not evidenced. Policy text may instead be non-truth-apt. |
| [EPI-RTE-source-check](#epi-rte-source-check) | check/evidence production | doctrine only | [EPI-OBJ-claims](#epi-obj-claims) | no content change | Presence of sources and reference existence in actual subgraph | Service source filter and worker lookup; existence domain | Before return and after synthesis | Missing source or reference discrepancy | None verified; described software gate | At most source presence/existence, not truth or entailment | Supplies a failure signal to disposition | Service/worker; check outcome; constraining in design; current candidate | SRC-1, `article.html`, synthesis paragraph | [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls) | none | Disposition of an invalid worker reference is not specified. |
| [EPI-RTE-source-check](#epi-rte-source-check) | disposition/acceptance | doctrine only | [EPI-OBJ-claims](#epi-obj-claims) | no content change | Unsourced claim to dropped candidate | Synthesis service; absence of source | Before leaving service | Claimed claim removal | None verified; described enforcing filter | Rejection for missing provenance, not positive epistemic acceptance | Blocks unsourced claim return | Worker; filtered response; enforcing in design; this synthesis | SRC-1, `article.html`, synthesis paragraph | [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls) | none | Does not test cited source truth. |
| [EPI-RTE-quality-check](#epi-rte-quality-check) | check/evidence production | doctrine only | [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package), [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph) | no content change | Grounding, recurring-pattern coverage, coherence, schema/spec, PII, separable procedures | Software checks; grounding >0.9 and coverage >0.6 as described; other definitions opaque | Before persistence | Claimed pass/fail or split suggestion | None verified | Schema validity is limited to encoded shape; other semantic license not determinable without metric definitions | Supplies initial admission result | Distiller; gate outcomes; constraining in design; initial candidate | SRC-1, `article.html`, gates paragraph | [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls) | none | These checks do not document task replay, causal testing or transfer evaluation. |
| [EPI-RTE-pending-admission](#epi-rte-pending-admission) | disposition/acceptance | doctrine only | [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package) | no content change | Checked candidate to withheld scope or pending skill | Distiller consumes initial gates; software veto | After gates, before write | Claimed withholding or permission to persist | None verified; described enforcing gate | Operational admission for review, not accepted knowledge for arbitrary tasks | Blocks failed scope; permits pending write | Neo4j writer; gate result; permissive/enforcing in design; initial persistence | SRC-1, `article.html`, gates and persist stages | [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls) | none | No rollback/failure transaction details. |
| [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation) | retention | doctrine only | [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package), [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph) | no content change | Candidate to pending subgraph/package | Neo4j persistence after gates | Before human review | Claimed retained content and grounding links | None verified | Evidence-linked retention is not acceptance or post-acceptance integration | Makes pending content available to reviewer | Reviewer; stored graph/package; evidential/advisory; later review | SRC-1, `article.html`, persist stage | [EPI-CLM-actionable-knowledge](#epi-clm-actionable-knowledge) | none | GROUNDED_IN edges are created before human approval. |
| [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery) | disposition/acceptance | doctrine only | [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package) | no content change | Pending skill to approved or rejected | Human follows steps and evidence; exact acceptance rubric not supplied | After pending persistence | Claimed approval/rejection | None verified; described human veto | Evidence-consuming review is described; no actual claim acceptance against a named substantive criterion established | Approval permits publication, rejection blocks it in design | Publisher; review state; permissive/enforcing in design; initial publication | SRC-1, `article.html`, review | [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls) | publication is not universal truth warrant | Human judgment may add substantive evaluation, so source checks are not necessarily the only review; depth remains unknown. |
| [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery) | operational admission/selection/consumption | doctrine only | [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package) | no content change | Published package to later host | Host interpretation; published state is documented condition | Later sessions/invocations | Claimed loading/fetching | None verified | Delivery carries no new truth warrant | Gives a host instructions; no tool permissions or compliance guarantee | see [RT-BAP-skill-consumption](runtime.md#rt-bap-skill-consumption) | SRC-1, `article.html`, delivery | [EPI-CLM-actionable-knowledge](#epi-clm-actionable-knowledge) | none | No executed consumer decision or observed benefit. |
| [RT-RTE-drift-check](runtime.md#rt-rte-drift-check) | check/evidence production | doctrine only | [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph) | no content change | Step expectStatus versus current grounded ToolCall status | Program comparison in named status domain | Governance schedule unspecified | Claimed contradicted flag | None verified; described flag only | Narrow counterevidence to expected status; not a causal diagnosis or general invalidity proof | Makes issue visible; automatic blocking not established | Governance UI/reviewer; flag; advisory; later governance | SRC-1, `article.html`, contradiction drift | [EPI-CLM-graph-validity](#epi-clm-graph-validity) | none | Existing edges can coexist with contradiction. No documented revocation consumer. |
| [RT-RTE-step-repair](runtime.md#rt-rte-step-repair) | lineage/freshness/recovery | doctrine only | [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph) | truth-apt transformation: indeterminate | One step re-grounded to survivors; deleted sources dropped | Source traversal and graph revalidation | On single-step drift; trigger owner unspecified | Claimed bounded patch | None verified | Restored lineage does not establish source truth or restored tool success | Changes one step's grounding and supersedes version | Reviewer/later resolver; patch and diff; proposed replacement; later use | SRC-1, `article.html`, repair | [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls) | none | Could preserve meaning or change support; no patch instance or semantic check. |
| [RT-RTE-step-repair](runtime.md#rt-rte-step-repair) | disposition/acceptance | doctrine only | [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph) | no content change | Salvageable patch versus no surviving grounding | Repair mechanism; surviving sources and graph revalidation | During repair | Claimed supersession or refusal/full re-distill flag | None verified; described refusal | Lineage/structural admission only; no established semantic acceptance | Refuses unsupported repair; permits patch path | Reviewer/version store; patch or escalation flag; permissive/enforcing in design; subsequent version | SRC-1, `article.html`, repair | [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls) | none | Initial gates, patch human approval, withdrawal and loaded-copy invalidation unresolved. |

No separate lifecycle-integration route is established by the document: pending evidence linkage precedes review, and publication is operational availability. This does not exclude unreported post-acceptance integration. No direct adaptation of the distiller's own policy or model parameters is established; skill repair changes an external instruction product. The status is bounded by SRC-1's article contents, not a negative finding about opaque services.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls) | see record | SRC-1, `article.html`, pipeline/review; doctrine/design | see record; checks and disposition separated above | None inspected; described [EPI-RTE-source-check](#epi-rte-source-check), [EPI-RTE-quality-check](#epi-rte-quality-check), [EPI-RTE-pending-admission](#epi-rte-pending-admission), [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery) | None supplied | No path equivalence, gate accuracy or review-effect experiment | Explicit source, structure, quality and human publication controls are declared | Source existence is narrower than claim justification; patch review coverage unknown. |
| [EPI-CLM-actionable-knowledge](#epi-clm-actionable-knowledge) | see record | SRC-1, `article.html`, introduction and product; doctrine/design | Source-grounded artifacts plus later loading described | None inspected; described [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation), [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery) | None supplied | No replay or transfer test; no actual accepted claim | Candidate procedural instruction construction, evidence-linked retention and reviewable delivery | Actual production of warranted ampliative knowledge or improved capacity is not established. |
| [EPI-CLM-graph-validity](#epi-clm-graph-validity) | see record | SRC-1, `article.html`, governance and AIP; doctrine/design and reported operation | Status check, bounded repair and schema validation described | None inspected; described [RT-RTE-drift-check](runtime.md#rt-rte-drift-check), [RT-RTE-step-repair](runtime.md#rt-rte-step-repair) | Article reports another study, not supplied NAMS runs | AIP numbers are secondhand; treatment/setup unavailable; no isolated NAMS component effect | Addressable graph representation permits declared local checks and repair | Whole-skill validity, explanation, transfer and automatic withdrawal exceed the specified check domain. |

## Bounded conclusion

NAMS is described as acquiring workspace reports with source identities, reshaping or inferring a procedure, generating model-written claims/annotations, and retaining a pending evidence-linked skill. Source warrant is unknown: provenance is described, but upstream factual accuracy and extraction fidelity are not checked here. Without actual inputs/outputs or implementation, no new proposition can be classified as a checked entailed derivation or a demonstrated ampliative conjecture. Determinism of topology generation does not settle either classification. See [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation) and the distinct parts [EPI-OBJ-claims](#epi-obj-claims) and [EPI-OBJ-step-annotations](#epi-obj-step-annotations).

The declared gates license narrower actions than “knowledge” can suggest. Source checks license provenance presence/existence; grounding and coverage thresholds license passage under unspecified metrics; schema checks license structural conformance; PII checks target disclosure, not truth. These feed an enforcing-in-design pre-persistence gate for a review candidate, not a demonstrated acceptance decision for a true general procedure. Human evidence inspection can approve publication or reject it, but its substantive acceptance criterion and any actual accepted claim are unavailable. Evidence links made while pending are not post-acceptance lifecycle integration. See [EPI-RTE-source-check](#epi-rte-source-check), [EPI-RTE-quality-check](#epi-rte-quality-check), [EPI-RTE-pending-admission](#epi-rte-pending-admission) and [RT-RTE-review-delivery](runtime.md#rt-rte-review-delivery).

The status-drift route has a genuine distinct target: an expected/current ToolCall status discrepancy, even when citations survive. Its recorded flag does not establish withdrawal or repair consumption. Repair can refuse a step with no surviving grounding, or produce a bounded superseding patch; neither lineage repair nor schema revalidation establishes restoration of task success. Tool changes, data changes and policy changes remain competing explanations for a failure. See [RT-RTE-drift-check](runtime.md#rt-rte-drift-check) and [RT-RTE-step-repair](runtime.md#rt-rte-step-repair).

The later behavioral channel is a published package interpreted by a host, not a demonstrated universal graph executor. It can guide later action across sessions, but delivery, activation and benefit remain distinct; no supplied trace closes the latter two. Trace-fed persistence supports a declared instruction-maintenance mechanism, not demonstrated future-capacity improvement. Parameter learning is independently uninspected in [RT-CMP-llm](runtime.md#rt-cmp-llm). Step addressability does not establish a formulated explanatory theory: each theory-builder condition remains independently unestablished on the supplied artifact-free evidence, as qualified in [RT-RTE-step-repair](runtime.md#rt-rte-step-repair). The represented aspects are backing memory/status, not a demonstrated self-representation of this builder's method; reflection of the builder is unresolved. Human publication veto limits autonomous release, while other internal roles are computational in doctrine. No live self-update of the distiller's own behavior-determining organization is traced, and no exercised self-improvement or successful improvement is established. These conclusions are independent, not one system-wide score.

## Shared records

### Operative objects

#### EPI-OBJ-scoped-memory
Label: Scoped memory inputs

Source-native identity: scoped decisions (:AgentStep), :ToolCall records, touched entities, messages, observations and reflections. Symbolic node identities and status fields are consumed by scope/topology/check programs; natural-language reasoning and messages are consumed by synthesis and reviewers. Substrate: input workspace graph in Neo4j; selected redacted snippets cross to synthesis. This is an input object, distinct from the output [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph) and [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package); no input counterpart was declared in the supplied runtime. SRC-1, `article.html`, pipeline. Particular factual content, historical authenticity and ontology extraction fidelity are not inspectable.

> Its raw inputs come from all three memory types: recorded decisions (:AgentStep nodes with reasoning, action, and result), the tool calls each decision made (:ToolCall nodes with tool name, input, output, and recorded status), the entities those conversations touched, and the surrounding messages, observations, and reflections.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

#### EPI-OBJ-claims
Label: Skill claims

Part of: [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package)

Source-native identity: the skill's model-returned claims with source references. Natural-language candidate assertions with symbolic source IDs; retained within Neo4j skill/package content in the design. Distinct from step names and completion criteria because assertions require truth support, whereas prescriptions can alter behavior without asserting a truth. Particular propositions and their preservation/entailment are not determinable. SRC-1, `article.html`, synthesis paragraph; minimum passage is supplied by [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation). The supplied container remains valid; no supersession is needed.

#### EPI-OBJ-step-annotations
Label: Step annotations

Part of: [RT-OBJ-skill-package](runtime.md#rt-obj-skill-package)

Source-native identity: names, descriptions and completion criteria returned by synthesis. Natural-language text interpreted by human reviewers and host models; stored with the skill/package in Neo4j as described. Different consumer role from factual claims: it can name steps or prescribe what counts as done. A factual description might be truth-apt, but the capture supplies no annotation instance to classify. SRC-1, `article.html`, synthesis paragraph; passage in [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation). Symbolic topology remains [RT-OBJ-procedure-graph](runtime.md#rt-obj-procedure-graph), not authored by this text route in doctrine.

### Routes

#### EPI-RTE-source-check
Label: Synthesis source checking

Part of: [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)

Endpoints: model-returned claims/references → synthesis-service source presence filtering → worker subgraph reference check. Owner: service and worker, not the model as authority on node existence. These are computational checks; the service can veto return of a source-less claim. No answer oracle for the correct procedure is supplied. Operating mode is open scoped synthesis, triggered by a scope job, not an experiment. Source existence and presence are the check domain; source truth or semantic entailment is not specified. Guidance is scoped snippets and source IDs; what survives is returned source-bearing claims. This part separates check/filter duties from the parent's generation and retention. SRC-1, `article.html`, synthesis paragraph; passage and scope limits in [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation).

- Immediate return: Claimed filtered claims and checked references; invalid-reference worker return shape uninspected.
- Later read-back: Surviving claims can enter the retained package for later review/consumption; check transcript retention is uninspected.
- Delegated visibility: Service sees up to 400 interleaved PII-redacted snippets; worker checks against actual subgraph.
- Selection predicate: Source presence at service; reference existence in scoped graph at worker.
- Invalidation or expiry: uninspected — no check-result lifetime or rollback protocol supplied.
- Activation or effect: Claimed source-less claim removal before return; no exercised filter result supplied.
- Evidence limits: Doctrine/design only; no code, claim, lookup trace, semantic test or result artifact.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

#### EPI-RTE-quality-check
Label: Initial quality checks

Part of: [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)

Endpoints: synthesized package/graph → software grounding, coverage, coherence, spec lint and PII checks → gate result/split suggestion. Owner: distiller's gate stage. Model and deterministic stages propose content; this computational check supplies the criterion result, while disposition is [EPI-RTE-pending-admission](#epi-rte-pending-admission). Grounding must clear 0.9, recurring-pattern coverage 0.6; separable procedures are identified for splitting; graph schema is checked before persistence. Domains differ: reference/coverage measures, procedure coherence, data shape and privacy. Formulas and semantic evaluation procedures are opaque. No independent expected procedure oracle or replay test is provided. Operating mode is initial construction; improvement trigger is requested distillation. SRC-1, `article.html`, gates paragraph; minimum passage in [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls).

- Immediate return: Claimed gate result or split suggestion; exact schema uninspected.
- Later read-back: uninspected — exported grounding/coverage scores are described, but complete check-result or rationale retention is not shown.
- Delegated visibility: uninspected — gate inputs beyond the candidate, scoped graph and recurring patterns are not specified.
- Selection predicate: Initial synthesized scope; grounding, coverage, coherence, spec and PII criteria.
- Invalidation or expiry: uninspected — no result expiry or recheck schedule for these initial gates supplied.
- Activation or effect: Claimed results feed pending-admission decision; no executed checks supplied.
- Evidence limits: Threshold definitions, checker code, boundary cases, false positives/negatives and fallback checks unknown.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

#### EPI-RTE-pending-admission
Label: Pending skill admission

Part of: [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation)

Endpoints: candidate and gate results → withholding, split suggestion or permission to persist pending human review. Owner: software distiller; computational veto precedes human publication review. Trigger and proposed change: a scope job proposes a new skill graph/package. Guidance: initial gate criteria, scoped evidence and synthesized procedure. Intended use is admission to review, not an independently warranted solution to future tasks. No expected-answer oracle is supplied. Rejected scopes are withheld; split is suggested rather than automatically demonstrated. Rollback, retry and partial-write recovery are unspecified. Persisted material is the skill and packaged artifact, not a demonstrated acceptance rationale. SRC-1, `article.html`, gates and persist stages. Minimum passages are in [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls) and below.

- Immediate return: Permission for pending write, or withheld scope/split suggestion as described.
- Later read-back: Pending content reaches human review; published content can later reach hosts via the parent and review route.
- Delegated visibility: Reviewer is described as receiving steps and supporting memory; exact failed-gate visibility uninspected.
- Selection predicate: Initial gate pass versus failure; separable procedures cause withholding and split suggestion.
- Invalidation or expiry: uninspected — initial pending-state expiry, rollback and rejected-candidate retention are not documented.
- Activation or effect: Claimed block on failed scopes before persistence; no admitted or rejected instance supplied.
- Evidence limits: No transaction code, executed gate consumer, bypass audit or published-state enforcement trace.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> <li><strong>Gates</strong>&#8202;&mdash;&#8202;grounding, coverage, coherence, spec lint, and PII checks; a scope that fails is withheld, not&nbsp;shipped</li>
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

> <li><strong>Persist</strong>&#8202;&mdash;&#8202;write the skill subgraph and the packaged artifact into Neo4j, pending human&nbsp;review</li>
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

### Claims

#### EPI-CLM-actionable-knowledge
Label: Distillation produces usable knowledge

Claimed operation: distillation converts workspace experience into portable, provenance-grounded instructions a new agent can load and run; evidence next to the procedure is described as justifying claims. SRC-1, `article.html`, introduction and “What Distillation Produces.” This is the product/warrant claim, distinct from the admission-control mechanisms in [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls). A source-bearing procedure can be useful without proving its truth, mechanism or transfer; an actual evidence-consuming acceptance decision is not supplied.

> Skill distillation produces knowledge your agents can act on, an artifact they load at runtime, and a governance loop that keeps both&nbsp;honest.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

> What separates it from a hand-written skill is the evidence shipped next to the procedure: steps grounded in actual tool calls observed from reasoning memory, grounding and coverage scores, and claims linked to the sources that justify them. The skill persists as a subgraph in Neo4j with GROUNDED_IN edges pointing back into the memory that justifies each&nbsp;claim.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

#### EPI-CLM-graph-validity
Label: Graph-governed validity and improvement

Claimed operation: keeping grounding and skills together makes validity queryable; schema-bound graph edits support measurable skill improvement. SRC-1, `article.html`, governance and “What AIP Proposes.” This warrant/benefit claim is distinct from [RT-CLM-admission-controls](runtime.md#rt-clm-admission-controls), though its local controls overlap. The operative contradiction check is limited to expected/current tool statuses; its source passage is in [RT-RTE-drift-check](runtime.md#rt-rte-drift-check). Salvageable/no-survivor repair countercases are in [RT-RTE-step-repair](runtime.md#rt-rte-step-repair). These qualify a broad validity reading rather than proving it false. The prose fallback in [RT-RTE-skill-distillation](runtime.md#rt-rte-skill-distillation) also prevents universal graph guarantees.

> A grounded skill is only as good as the memory under it and memory changes over time. Entities merge, policies are updated, and tool behavior shifts. Because a skill and its grounding are graph data side by side, &ldquo;is this skill still valid?&rdquo; is a graph&nbsp;query.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

> <p>The AIP paper frames this as a <strong>validity-gated action space:</strong> because each node is typed and schema-bound, edits are constrained and checkable&#8202;&mdash;&#8202;a foundation for structured, measurable skill improvement instead of open-ended prose rewriting.</p>
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

> <p>This graph structure measurably helps. In the AIP authors&rsquo; own evaluation on SkillsBench, structured skills beat freeform prose by <strong>+14.1 percentage points in pass rate</strong> (53.3% &rarr; 67.4%) and ran <strong>~13% faster</strong> (585s &rarr; 510s). (Source: AIP, arXiv 2606.04781)</p>
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

This is an attributed AIP contrast, not a supplied causal experiment on the NAMS builder, gates, review or repair. It cannot identify their contribution, and outcome differences alone would not establish explanatory warrant for generated claims.
