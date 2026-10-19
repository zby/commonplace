---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of From Agent Memory to Portable Skills: documented NAMS distillation, gates, review, delivery and bounded repair in the frozen article."
run-id: AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01
reviewed-boundary: "neo4j-article-2026-10-18-99f91d4da959"
---

# From Agent Memory to Portable Skills runtime report

## Runtime account

### Boundary and ordinary invocation

This is a doc-grounded account of NAMS's skill-building subsystem, not an audit of an enclosing agent runtime. SRC-1, `article.html`, is the frozen article registered in [the boundary](boundary.md#source-register). Its substantive body and HTML captions were inspected, including the pipeline, fallback, governance and delivery descriptions. No implementation, actual job, generated package, human review artifact or consumer execution is supplied. Availability is reported by the article; operation, activation and benefit are not observed here. Linked AIP evaluation results are not NAMS execution evidence.

The ordinary documented invocation starts when a caller submits a workspace scope through HTTP, MCP or the dashboard. The article does not identify that caller as necessarily human or give authentication, authorization, request schemas, task identifiers or the exact polling response. A trigger enqueues a Redis-stream run. The distiller then owns progression: resolve the conversations, take a workspace lock, wait for extraction to settle, consolidate recurring actions, derive graph topology, call synthesis, apply gates, and persist a pending skill in Neo4j. The result is a graph-backed artifact-building job, not execution of the generated procedure. [RT-RTE-skill-distillation](#rt-rte-skill-distillation) gives the admission and return details.

The input context comprises decisions and their reasoning/action/result, recorded tool calls and statuses, touched entities, and surrounding messages, observations and reflections. Deterministic stages use recorded relationships and outcomes to form clusters and topology. The only model stage is a Python grounded-synthesis call to [RT-CMP-llm](#rt-cmp-llm): up to 400 interleaved, PII-redacted snippets become claims and step annotations carrying source references. The model does not select the topology according to the article. Source-less claims are dropped at synthesis, references are checked by the worker against the subgraph, and gates can withhold the skill before persistence. These are declared control responsibilities, not independently verified invariants (SRC-1, `article.html`, “Inside the Distillation Pipeline”).

The persisted product has distinct operative parts: [RT-OBJ-procedure-graph](#rt-obj-procedure-graph) contains symbolic topology and bindings; [RT-OBJ-skill-package](#rt-obj-skill-package) contains the natural-language procedure, claims and annotations as exported Markdown. A scope with fewer than three recorded steps falls back to prose. It would therefore be wrong to describe every admitted skill as a typed execution graph. A script-backed step is derived from a recorded tool call, not evidence that the distiller executes that call or grants the consumer access to the named tool (SRC-1, `article.html`, “AIP Procedure Graphs in NAMS”).

Persistence is not publication. A human reviewer reads steps and evidence and approves or rejects; subsequently a published package can reach Claude Code, MCP clients or REST consumers via [RT-RTE-review-delivery](#rt-rte-review-delivery). Those hosts own later action selection, tools, permissions, context loading and execution. The document does not specify an interpreter that enforces the graph in every host. [RT-BAP-skill-consumption](#rt-bap-skill-consumption) bounds the downstream authority claim.

### Maintenance and forcing routes

The smallest useful forcing set in this document is three cases, each of which qualifies a tempting universal claim:

1. **Thin scope:** fewer than three recorded steps produces prose rather than a skeletal graph. This challenges a universal graph/schema assurance, not the existence of a graph path. The article states that the procedure graph is validated before persistence, but does not show the fallback's data shape, validators or how prose claims are represented. [RT-CLM-admission-controls](#rt-clm-admission-controls) therefore does not extend graph validation into a proved property of every package.
2. **Citation-preserving contradiction:** a step's tool status can contradict its recorded expected status even while all grounding edges remain. The governance check compares these statuses, rather than treating edge presence as sufficient validity. [RT-RTE-drift-check](#rt-rte-drift-check) distinguishes flagging from execution failure diagnosis.
3. **Salvageable versus unsalvageable drift:** repair follows merged sources, drops deleted ones and patches one step; no surviving grounding causes refusal and a full re-distill flag. It is not a universal automatic repair path. [RT-RTE-step-repair](#rt-rte-step-repair) records versioning and the unresolved release semantics.

The initial pipeline also withholds a scope containing separable procedures and suggests splitting it. Grounding must clear 0.9 and recurring-pattern coverage must clear 0.6. The capture does not define their calculations or show a borderline input. These are documented acceptance criteria, not evidence of semantic correctness (SRC-1, `article.html`, “Inside the Distillation Pipeline”).

### Guarantees, capability and isolation

[RT-CLM-admission-controls](#rt-clm-admission-controls) separates the owners and enforcement points for scope grounding, stable snapshot, gates and human review. Material alternate entry paths named by the source are HTTP, MCP and dashboard; material output paths are Claude Code, MCP and REST; material generation variants are graph and prose; and maintenance has its own patch path. The article groups initial triggers into one pipeline, but provides no caller code to establish path equivalence. It does not expose whether a direct synthesis call, raw artifact read, manual graph edit or alternate writer could circumvent publication controls. These are unresolved reachability questions, not demonstrated bypasses or evidenced absences.

The subsystem's described capability is to synthesize, validate, store, review, flag and repair skills. The workspace lock is concurrency control, not a sandbox or permission grant. The per-request scope is described as the evidence boundary; no ACL, tenant-isolation or deployed grant set is inspectable. Redis delivery, Neo4j locking/transactions, extraction completion and Python service integrity are external contracts needed to realize the stated controls. Their failure behavior, crash recovery, retry/idempotency, lock timeout, ordering and durability guarantees are not documented. These limits prevent claims of production isolation or exactly-once admission (SRC-1, `article.html`, “Distilling a Skill from Memory,” “Bounded, Node-Level Repair,” “Inside the Distillation Pipeline”).

The explicit model-context control is scoped selection and a bounded, redacted snippet supply. What is omitted preferentially when more than 400 snippets exist is not described; no complete-context or optimal-selection claim follows. A separately called synthesis service resembles an isolated work frame only in that selected input is sent and claims/annotations return. It supplies no evidence of a general sub-agent stack, foreground-window trimming, host compaction, or a reload pointer for omitted snippets. Published-skill loading is a later external-context supply path, but the consumer's reload/eviction policy is opaque (SRC-1, `article.html`, synthesis and delivery paragraphs).

There is no observed NAMS latency or success-rate comparison. The article's reported AIP SkillsBench contrast concerns another evaluation, not an intervention isolating NAMS distillation, gates or governance. No runtime-benefit claim is assigned to those components here (SRC-1, `article.html`, “What AIP Proposes”).

## Shared records

### Components

#### RT-CMP-llm
Label: Grounded-synthesis LLM

Source-native identity: the unnamed LLM called through the Python grounded-synthesis endpoint. Its operative model state is distributed-parametric; the provider's storage and serving substrate are uninspected. It receives natural-language source snippets and returns claims and annotations. The endpoint's wrapper and the worker, not a model assertion, are assigned source-dropping and reference-checking duties. Evidence: SRC-1, `article.html`, “Inside the Distillation Pipeline.”

Parameter changes during operation: uninspected; the capture describes inference and no inspectable parameter lifecycle. Exact model/version pin: uninspected; no model identifier is supplied. Whether the endpoint can resolve to another model: uninspected; endpoint configuration and provider internals are outside the capture. These unknowns do not imply absence of learning through retained skills.

> For synthesis, the distiller calls out to a Python grounded-synthesis endpoint, and the LLM&rsquo;s role there is deliberately narrow.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

### Operative objects

#### RT-OBJ-procedure-graph
Label: Procedure graph structure and bindings

Source-native identity: the skill/step topology with typed I/O, dependencies, branch types and tool-call bindings. Its structural part is symbolic: types and schema checks are assigned fixed validation roles. Storage is the skill subgraph in Neo4j, linked back to memory by GROUNDED_IN edges. Its natural-language annotations are treated separately in [RT-OBJ-skill-package](#rt-obj-skill-package); a shared container does not give those annotations symbolic semantics. Deterministic topology derives from recorded traces; recorded tool names, inputs, outputs and expected status supply script-backed bindings. The article names sequence, one-of, parallel and retry relationships but supplies no executor semantics or graph instance. Evidence: SRC-1, `article.html`, “What Distillation Produces,” “What AIP Proposes,” “AIP Procedure Graphs in NAMS.”

> The topology is derived deterministically from the traces, not written by a model.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

#### RT-OBJ-skill-package
Label: SKILL.md procedure and annotations

Source-native identity: the packaged SKILL.md, including provenance frontmatter, procedure body and reference material; model-authored claims and step annotations provide names, descriptions and completion criteria. Natural-language content operates through human review and host-model interpretation. Metadata and source IDs also have symbolic uses in validation; that does not make the procedure text a deterministic program. The packaged artifact is stored in Neo4j alongside the skill graph. The article does not supply bytes of an exported package or demonstrate specification conformance. The graph-form output and thin-scope prose fallback must remain distinct possibilities. Evidence: SRC-1, `article.html`, “What Distillation Produces,” “AIP Procedure Graphs in NAMS,” “Inside the Distillation Pipeline.”

> Frontmatter contains provenance metadata, the body leads with the procedure, and reference material is included.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

### Routes

#### RT-RTE-skill-distillation
Label: Scoped memory to pending skill

Endpoints and progression: HTTP/MCP/dashboard trigger → Redis-stream run → scope resolution → workspace snapshot lock and extraction-settlement wait → outcome-separated, frequency-weighted pattern consolidation → deterministic topology → Python synthesis → gates → Neo4j skill and package pending review. The caller supplies scope; the distiller owns progression; the model proposes claims and annotations only. Input guidance is the selected conversations' decisions, tool calls, entities and messages, not an independently supplied expected answer. Cluster outcomes distinguish effective patterns from anti-patterns. Operating mode is open scope-requested artifact construction, not a documented curriculum or controlled experiment. Triggering the job is not per-content approval. Computational gates can reject before persistence; a human can later veto publication through [RT-RTE-review-delivery](#rt-rte-review-delivery). Source: SRC-1, `article.html`, pipeline and scope sections.

- Immediate return: A graph-backed pollable job is described; the initial HTTP/MCP/UI response schema, run ID and error envelope are uninspected. The terminal accepted result is a pending skill, not an executed task.
- Later read-back: Persisted skill graph and package support later human review and published-agent consumption. Raw input-memory retention is an upstream responsibility, not established by this write route.
- Delegated visibility: Synthesis receives up to 400 interleaved, PII-redacted source snippets; claims and annotations carrying source IDs return to the worker. Complete snapshot visibility at the model is not established.
- Selection predicate: Requested scope resolves to conversations; recurring actions are clustered by frequency and tool outcome. Detailed scope schema, snippet ranking and truncation policy are uninspected.
- Invalidation or expiry: Later drift checking and patch supersession are described; no initial skill TTL or automatic withdrawal policy is given.
- Activation or effect: Claimed admission of a pending skill subgraph and packaged artifact; no publication or consumer behavior is established by persistence alone.
- Evidence limits: SRC-1 is design/report only; caller schemas, implementation branches, lock release, service failures and executed gate results are not inspectable.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Proposal/admission/recovery: deterministic code proposes topology, the LLM proposes textual content, and software applies grounding/coverage/coherence/spec/PII checks. A multi-procedure scope is withheld with a split suggestion. Failed scopes are not shipped according to the document; retry, transaction rollback and crash recovery are unspecified. Persisted content retains source grounding and provenance; it does not retain an inspectable complete synthesis transcript in this evidence. Tool outcomes are evidence inputs, not an answer oracle giving an expected synthesized skill. No separate expected-answer provider is identified.

> It sees up to 400 interleaved, PII-redacted source snippets and returns the skill&rsquo;s claims and step annotations (names, descriptions, completion criteria), each carrying source references.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

> Claims without sources are dropped before they leave the synthesis service, and the worker re-checks every reference against the actual subgraph: the graph, not the model, is the authority on what exists.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

The prose-fallback countercase is explicit:

> a scope with fewer than three recorded steps degrades gracefully to prose instead of shipping a skeletal&nbsp;graph.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

#### RT-RTE-review-delivery
Label: Human review to published delivery

Endpoints and owner: pending skill → human reviewer reading steps and linked evidence → approval or rejection → published package available to Claude Code, NAMS MCP clients or REST consumers. The reviewer decides publication; the article does not identify roles, identities, permission checks or the publication transaction. The host agent owns subsequent task execution. Operating mode is human content review, not automatic promotion. Guidance comprises step tool binding, input/output contract, completion condition and grounding. No expected-answer oracle or review rubric is supplied beyond this evidence-based inspection. Source: SRC-1, `article.html`, “Nothing Ships Unreviewed,” review caption and delivery section.

- Immediate return: Review accepts or rejects a pending skill; subsequent consumers receive a published SKILL.md package by the documented delivery interfaces. Exact response bodies are uninspected.
- Later read-back: A later agent can load the retained published procedure across sessions and host frameworks; actual repeated use is not shown.
- Delegated visibility: The reviewer sees steps and supporting memory. The consumer receives a packaged procedure and reference material; complete graph/memory delivery and tool access are not established.
- Selection predicate: Published state is the stated delivery condition. Consumer-side task matching, version resolution and automatic skill selection are uninspected; agent-driven selection is described as an exploration area.
- Invalidation or expiry: Drift flags and patch supersession exist in the account, but effects on already-loaded packages and revocation are unspecified.
- Activation or effect: Approval is claimed to permit publication and delivery; loading, compliant execution and task success remain separate and unobserved.
- Evidence limits: No review record, publication code, export example or host trace is supplied. The article does not establish exclusion of direct reads of pending data or mandatory re-review of repaired patches.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Admission and recovery: the human can reject the generated instruction product. Editing, override, rollback to prior versions, re-review after repair and rejection persistence are not detailed. The retained product is the skill/package, not an inspectable review rationale. Human approval in this route prevents attributing fully autonomous publication to the documented loop.

> A distilled skill lands pending human review. A reviewer reads the steps, follows the evidence back to the work behind them, and approves or&nbsp;rejects.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

> a published skill can be loaded into Claude Code as a skill, fetched by MCP clients through the NAMS MCP server, or consumed over REST by any other agent framework.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

#### RT-RTE-drift-check
Label: Tool-status contradiction check

Endpoints and owner: recorded step expected status and current grounded ToolCall status → NAMS skill-drift comparison → contradicted flag. The check's computational decision concerns a status mismatch, not a model-written diagnosis. Its invocation schedule, principal and automatic handoff to repair are unspecified. Operating mode is governance against live backing memory. The step's expectStatus supplies the reference outcome and the current ToolCall node supplies the comparison value; neither is an independent task-success oracle. A mismatch targets reliance on that step despite surviving citations. Source: SRC-1, `article.html`, “Keeping Skills Honest: Governance and Drift.”

- Immediate return: A contradicted step is flagged; exact API return and persistence of the flag are uninspected.
- Later read-back: Governance UI is described as showing issues; how flags influence later delivery or consumers is not specified.
- Delegated visibility: The comparison uses expected and current status on grounded nodes; evidence of a delegated model call or additional diagnosis context is not supplied.
- Selection predicate: Steps grounded in ToolCall nodes are compared against their recorded expected status. Coverage of description-only steps and other contradiction classes is unresolved.
- Invalidation or expiry: Flagging challenges validity; automatic revocation, expiry and cache invalidation are uninspected.
- Activation or effect: Claimed contradiction detection, not demonstrated repair, disabling or changed downstream execution.
- Evidence limits: No graph instance, comparison code, schedule or run trace is supplied. A status mismatch is not sufficient to locate the cause in the procedure rather than changed tools, data or policy.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> A step that used to succeed but whose tool now fails is flagged as contradicted, even though every grounding edge is still&nbsp;present.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

#### RT-RTE-step-repair
Label: Bounded grounding repair

Endpoints and owner: a drifting step → repairStep acquires workspace lock → follow merged sources to survivors, drop deleted sources → revalidate graph → patch version superseding prior version. Other steps remain untouched according to the document. If no grounding survives, repair declines and flags full re-distillation. The repair mechanism proposes and admits a bounded grounding change under validation; a human reviewer is said to see a one-step diff, but mandatory reviewer approval of patch publication is not stated. Trigger is single-step drift; whether a person or scheduler calls repairStep is unresolved. Source: SRC-1, `article.html`, “Bounded, Node-Level Repair.”

- Immediate return: A superseding patch version, or decline with a full re-distill flag; API response shape and job/asynchronous behavior are uninspected.
- Later read-back: The patch is intended to replace the prior skill version for later review/use. Consumer version pinning, installed-package updates and actual read-back are not shown.
- Delegated visibility: Repair traverses grounding for one step; the reviewer sees a one-step diff. A model repair context or remote worker protocol is not described.
- Selection predicate: The drifting step and surviving grounding sources are selected; all other steps are stated to remain unchanged.
- Invalidation or expiry: Patch supersedes the prior version; deletion, retention horizon, revocation and rollback selection are unspecified.
- Activation or effect: Claimed re-grounding and graph revalidation, not demonstrated restoration of tool success or downstream behavior.
- Evidence limits: No repair implementation, patch artifact, re-review policy or executed salvage/decline case is supplied. Reachability of both branches and atomicity are not code-verified.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

Admission, guidance and recovery: source-survivor relationships and graph validation constrain the proposed change; absence of grounding permits computational rejection. Full re-distillation is the stated escalation, not an automatic completed recovery. Supersession retains a version relation but does not prove an operational rollback facility. No expected repaired text or task-level answer oracle is supplied. Operating mode is bounded maintenance, not open-ended skill optimization.

> A repairStep takes the workspace lock, re-grounds only that step by following merged sources to their survivors (and dropping deleted ones), re-validates the graph, and cuts a patch version that supersedes the prior&#8202;&mdash;&#8202;every other step untouched, so a reviewer sees a one-step&nbsp;diff.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

> If no surviving grounding exists, repair declines and flags a full re-distill&#8202;&mdash;&#8202;it fixes salvageable drift, never papers over the unsalvageable.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

Theory assessment boundary: these routes manipulate prescriptive procedures and their evidence links. No actual procedure unit is supplied from which to establish explanatory content or a formulated theory. Consequently, theory-builder conditions 1–4 remain separately uninspected here: (1) no generated whole theory unit; (2) no content-dependent consumer decision trace; (3) no formulated blame allocation and resulting revision of a theory; (4) no retained criticism shown shaping a next theory round. Status comparison and source-survivor repair do not by themselves establish those conditions, nor do they establish their absence inside opaque processing. Node-level addressability of steps is claimed, but addressability of assumptions or scope conditions in an actual theory is unresolved. Persistence is claimed for skills across sessions and versions; actual later capacity improvement (learning) is uninspected. The governance pathway represents some backing-memory/tool-status changes and can revise a skill's grounding; it does not establish full self-representation of the distiller or criticism of its own method. A reflective or autonomous theory builder and exercised self-improvement are not established. The evidence supports a described instruction-product maintenance path, not observed improvement of the subsystem's own organization.

### Claims

#### RT-CLM-admission-controls
Label: Documented admission controls and their coverage

Claimed operation: source-bounded, validated, reviewed skills rather than unrestricted model-authored procedures. Source: SRC-1, `article.html`, scope, synthesis, gates, review and repair sections. Each assurance below has separate declared and observed status; no implementation has been inspected.

| Assurance | Owner and enforcement point | Guarantee strength | Covered path and external contract | Alternate-path limit |
|---|---|---|---|---|
| Scoped evidence only | Scope resolver, synthesis source filtering and worker reference re-check | protocol | Initial distillation; conversation membership and graph identities must be correct | Request shapes, scope expansion rules and direct synthesis reachability are uninspected; reference existence is not entailment |
| Settled input snapshot | Distiller's per-workspace lock and extraction-settlement wait | protocol | Initial snapshot; requires extraction completion signal and effective shared locking | Repair takes a lock too, but transaction boundaries, unrelated writers and crash behavior are not described |
| Withhold low-quality or mixed scopes | Pre-persistence grounding, coverage, coherence, spec/PII gates | protocol | Initial pipeline; thresholds clear 0.9 grounding and 0.6 coverage; separable procedures cause split suggestion | Score definitions and prose-fallback validation are not exposed; repair explicitly mentions graph revalidation, not every initial gate |
| No unreviewed initial skill publication | Pending-review state and human approval/rejection | policy | Initial distilled skill before published delivery; requires review-state enforcement in readers/writers | No endpoint code, patch publication state or raw-read policy; cannot prove all delivery paths enforce it |
| Do not repair unsupported grounding | repairStep refusal when no survivor exists | protocol | Single-step repair; requires correct source-survivor traversal and graph validation | Cannot conclude repair resolves a tool-status contradiction or applies to every drift class |

- design conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

The term protocol here denotes the described ordered controls, not demonstrated runtime invariance. The article's stronger categorical wording is retained as a claim, with enforcement coverage bounded above.

> The grounding score must clear 0.9 and coverage of recurring patterns must clear 0.6; a scope that contains two or more separable procedures is withheld with a split suggestion rather than shipped as one blended skill; exemplars are PII-redacted; and the procedure graph is schema-validated before anything persists.
> --- `/media/zby/2b5e98b6-baf0-4e97-90d2-03321ea23372/outputs/commonplace-worktrees/batch-22-nams-retry-1/kb/agentic-system-analyses/state/AAS-2026-10-18-from-agent-memory-to-portable-skills-4a509c7732b1-01/sources/article.html`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-skill-consumption
Label: Published procedure as later agent guidance

Consumer: a later Claude Code agent, MCP client or other REST-consuming agent framework. Channel: published SKILL.md package, whose procedure, annotations and references derive from scoped retained memory. Force: natural-language task guidance interpreted by a host/model; no mandatory compliance, direct tool grant or uniform graph executor is established. Horizon: later invocations and sessions, as claimed by the article's new-agent loop. Distiller-side validation is a different consumer and has a different force: checking structure and references before admission. Sources: SRC-1, `article.html`, “How a Published Skill Reaches Your Agents,” with the delivery passage retained in [RT-RTE-review-delivery](#rt-rte-review-delivery).

Delivery can make the product behavior-shaping, but no supplied consumer trace shows it changing a decision or improving success. HTTP/MCP delivery does not extend the distiller's workspace lock, gates or review authority into host permissions. The article does not demonstrate a loop in which this subsystem consumes and revises its own distillation method; its published artifact is for external agents.

## Annotations

none
