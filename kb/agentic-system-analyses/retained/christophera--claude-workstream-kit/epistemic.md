---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Claude Workstream Kit: which retained claims, measurements and evidence checks license later work, and where their authority stops."
run-id: AAS-2026-10-15-claude-workstream-kit-103204afa1ab-01
reviewed-boundary: "15705c38a4fffb206b868b3e6bc5ffb4fd8b9d64"
---

# Claude Workstream Kit epistemic report

## Source-and-claim boundary

The question is how work-state claims acquire warrant before they guide another session, become instructions, or authorize closure. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and layers are see [Source register](boundary.md#source-register). All source findings below use SRC-1 at the frozen commit. Direct inspection establishes code behavior or model-facing instructions, not model compliance. No target was executed.

The kit is deliberately an operational work-state system, not an all-purpose truth adjudicator. Its checks are heterogeneous: parser predicates establish facts about text; model verification compares task claims with artifacts; users approve substantive changes and closure. Their licenses must not be merged. Consequential claims are [EPI-CLM-grounded-claims](#epi-clm-grounded-claims), [EPI-CLM-gate-validation](#epi-clm-gate-validation), and [RT-CLM-rewrite-preservation](runtime.md#rt-clm-rewrite-preservation).

| Entry point or operation | Source path in SRC-1 | Coverage and records; limit |
|---|---|---|
| Registered hooks | `.claude/settings.json` | Direct full read: SessionStart and Stop registrations only; supplied [RT-RTE-session-reload](runtime.md#rt-rte-session-reload), [RT-RTE-stop-gloss](runtime.md#rt-rte-stop-gloss) supply hook findings. No registered tool server appears in these settings; no conclusion about external host tools. |
| Record CLI | `.claude/scripts/workstream-record.py` | Direct dispatch inspection: record/default-root, cites, refs, paths, decay, git, fires, bare-ids, self-check. Direct Learning-field and self-check implementation; [EPI-RTE-marker-measure](#epi-rte-marker-measure). Other handlers only function/search coverage here, supplemented by supplied hook/rewrite findings. Their exact matching completeness is unassessed, preventing a system-complete negative about omitted checking routes. |
| Rewrite CLI | `.claude/scripts/workstream-rewrite.py`, `.claude/scripts/workstream_state.py` | Direct dispatch, finish, Learning transformation/check, sentence/marker/fingerprint code and rotation admission tail; [EPI-RTE-learning-condense](#epi-rte-learning-condense), [RT-RTE-rewrite-state](runtime.md#rt-rte-rewrite-state). Detailed records/decisions and rotation dependency-sweep internals use supplied runtime findings, not a fresh full audit. |
| Compatibility entry | `.claude/scripts/condense-completed-records.py` | Direct full read: forwards to run_condense, including write flag. Same underlying route, not another evaluator. |
| Work, create, close and delegates | `.claude/skills/workstream-work/SKILL.md`, `.claude/skills/workstream-create/SKILL.md`, `.claude/skills/workstream-close/SKILL.md`, `.claude/agents/verifier.md` | Verifier directly read; other skill and agent findings supplied by [RT-RTE-work-goal](runtime.md#rt-rte-work-goal), [RT-RTE-agent-packet](runtime.md#rt-rte-agent-packet), [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle). |
| Capture, review, extract | `.claude/skills/workstream-capture/SKILL.md`, `.claude/skills/workstream-review/SKILL.md`, `.claude/skills/workstream-extract/SKILL.md` | Direct full reads; [EPI-RTE-capture-synthesis](#epi-rte-capture-synthesis), [EPI-RTE-still-true](#epi-rte-still-true), [EPI-RTE-disposition-check](#epi-rte-disposition-check). Linked failure histories not independently inspected: historical causal explanations remain attributed. |
| Status and cross-project intake | `.claude/skills/workstream-status/SKILL.md`, `.claude/skills/handoff/SKILL.md` | Direct full reads; [EPI-RTE-status-statement](#epi-rte-status-statement), [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle). |
| Installer, upgrade and context telemetry | `install.sh`, `.claude/skills/workstream-upgrade/SKILL.md`, `.claude/scripts/status-line.sh` | Supplied [RT-RTE-install-upgrade](runtime.md#rt-rte-install-upgrade) and runtime context account only; exact deployment drift predicates not re-audited. Copying instructions is operational admission, not acceptance of their truth. Telemetry is a budget signal, not a semantic check. |
| Model-calling evaluator | `tests/va3-acceptance.sh` | Direct full read; [RT-RTE-acceptance-driver](runtime.md#rt-rte-acceptance-driver). Other offline suites remain available but uninspected here: no claim of comprehensive test coverage or successful tests. |
| Public design claims | `docs/design.md`, `README.md` | Direct bounded search passages; claim records below. Statements about earlier runs are reported operation, not supplied traces. |

Missing live consumer artifacts prevent individuating an actual accepted Learning or synthesis and checking its truth. Missing host implementation and traces prevent establishing actual goal arming, delegation isolation, user-gate compliance or downstream activation. Missing interventions prevent attributing safety, learning benefit or improvement to the kit. Exact provider state is see [RT-CMP-claude](runtime.md#rt-cmp-claude): parameter updates, exact model version and endpoint resolution are uninspected. These limits do not negate the inspected deterministic routes or the declared evidence protocols.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-workstream-claims](#epi-obj-workstream-claims) | Dated findings, explanations, completion and disposition claims | Durable premises for review and future work | SRC-1, `.claude/skills/workstream-review/SKILL.md` | Natural-language claims, not automatically accepted knowledge; actual instance truth not determinable. |
| [EPI-OBJ-workstream-markers](#epi-obj-workstream-markers) | Markers encode assertions of state; parser predicates about their occurrence are truth-apt separately | Count, signal and rewrite selection | SRC-1, `.claude/scripts/workstream_state.py` | Symbolic marker occurrence does not prove the asserted disposition. |
| [EPI-OBJ-workstream-guidance](#epi-obj-workstream-guidance) | Plans/criteria are primarily normative; their premises and claims of satisfaction are truth-apt | Scope, ordering and user gates | SRC-1, `.claude/skills/workstream-review/SKILL.md` | Approval changes permission, not source truth. |
| [RT-OBJ-active](runtime.md#rt-obj-active) | see record | see record | SRC-1, `.claude/hooks/session-start.sh` | Pointer/prose mixture; cannot establish armed-goal state. |
| [EPI-OBJ-record-learnings](#epi-obj-record-learnings) | Counts and classifications of Learning blocks under the parser grammar | Input to drain selection and status | SRC-1, `.claude/scripts/workstream-record.py` | Target is file form, not truth of entries or correctness of their claimed destinations. |
| [RT-CMP-claude](runtime.md#rt-cmp-claude) | Particular generated propositions not determinable from inaccessible weights | see record | SRC-1, `.claude/agents/verifier.md` | Model instructions and outputs must not be confused with parameter change or an oracle. |

## Authority-route ledger

Fields owned by supplied or declared records are linked rather than reproduced. Architectural status below is local to this ledger. A prompt-only semantic route is doctrine only: executable delivery does not establish execution of the requested evaluation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs | Mismatch marker | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-capture-synthesis](#epi-rte-capture-synthesis) | content transformation | doctrine only | [EPI-OBJ-workstream-claims](#epi-obj-workstream-claims) | truth-apt transformation: indeterminate | Session findings to durable synthesis | see record | see record | see record | Requested writing | Candidate only; no general acceptance | Routine capture can persist without per-claim user approval | see record | SRC-1, `.claude/skills/workstream-capture/SKILL.md` | none | none | Could copy, reshape, derive or conjecture; actual inputs/output needed to classify. |
| [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle) | retention | doctrine only | [EPI-OBJ-workstream-claims](#epi-obj-workstream-claims) | no content change | Current notes to committed checkpoint | see record | see record | see record | Model policy | Retention does not confer acceptance | Future work may use candidate notes | [RT-BAP-resume-state](runtime.md#rt-bap-resume-state) | SRC-1, `.claude/skills/workstream-capture/SKILL.md` | none | none | Git retention depends on compliance and publication. |
| [EPI-RTE-marker-measure](#epi-rte-marker-measure) | check/evidence production | implemented | [EPI-OBJ-record-learnings](#epi-obj-record-learnings) | truth-apt transformation: entailed derivation | Learning blocks and dated markers | see record | see record | see record | Code classification, advisory to semantic decisions | Counts under named grammar only | Supplies drain/status inputs, never approves content | see record | SRC-1, `.claude/scripts/workstream-record.py` | [EPI-CLM-grounded-claims](#epi-clm-grounded-claims) | none | Syntactically terminal can be factually false. |
| [EPI-RTE-still-true](#epi-rte-still-true) | check/evidence production | doctrine only | [EPI-OBJ-workstream-claims](#epi-obj-workstream-claims) | no content change | Premises versus current artifacts and commitments | see record | see record | see record | Requested comparative inspection | Local evidence, not document authority alone | Findings propose reliance changes | see record | SRC-1, `.claude/skills/workstream-review/SKILL.md` | [EPI-CLM-grounded-claims](#epi-clm-grounded-claims) | none | Missing consumer artifacts and runs. |
| [EPI-RTE-still-true](#epi-rte-still-true) | disposition/acceptance | doctrine only | [EPI-OBJ-workstream-claims](#epi-obj-workstream-claims) | non-truth-apt policy/content update: mark supersession or revise scope | Stale findings to changed reliance | see record | see record | see record | Model policy; substantive restructure user gate | Evidence can withdraw current reliance; approval is not infallibility | Mark stale in place; revise tasks after required approval | see record | SRC-1, `.claude/skills/workstream-review/SKILL.md` | none | none | Not a universally enforced content admission gate. |
| [EPI-RTE-disposition-check](#epi-rte-disposition-check) | check/evidence production | doctrine only | [EPI-OBJ-workstream-claims](#epi-obj-workstream-claims) | no content change | Claimed disposition versus governed destination | see record | see record | see record | Requested artifact check | Verifies routing/implementation, not every generalization's truth | Missing application requires edit or re-routing | see record | SRC-1, `.claude/skills/workstream-extract/SKILL.md` | [EPI-CLM-grounded-claims](#epi-clm-grounded-claims) | none | Marker counting is explicitly insufficient. |
| [EPI-RTE-disposition-check](#epi-rte-disposition-check) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-workstream-claims](#epi-obj-workstream-claims) | non-truth-apt policy/content update: apply, hand off or drop | Resolved entries to governed files or declined matter | see record | see record | see record | Requested edits plus separate handoff gate | Routing licenses intended operational use, not general truth | Guidance may change future work; dropping with rationale is allowed | see record | SRC-1, `.claude/skills/workstream-extract/SKILL.md` | none | none | Not automatically lifecycle integration of accepted ampliative knowledge. |
| [EPI-RTE-learning-condense](#epi-rte-learning-condense) | content transformation | implemented | [EPI-OBJ-workstream-claims](#epi-obj-workstream-claims) | truth-apt transformation: indeterminate | Terminal Learning to selected sentences | see record | see record | see record | Deterministic selection | Literal retention checks do not prove preserved meaning | Shorter text can replace later-read state | see record | SRC-1, `.claude/scripts/workstream-rewrite.py` | [RT-CLM-rewrite-preservation](runtime.md#rt-clm-rewrite-preservation) | Semantic preservation unestablished | Concrete trace below shows omission. |
| [EPI-RTE-learning-condense](#epi-rte-learning-condense) | check/evidence production | implemented | [EPI-OBJ-workstream-claims](#epi-obj-workstream-claims) | no content change | Statement/target/disposition strings, count and fingerprint | see record | see record | see record | Local refusal before own write | Checked syntactic relation only | Blocks this CLI path when predicate fails | see record | SRC-1, `.claude/scripts/workstream-rewrite.py` | [RT-CLM-rewrite-preservation](runtime.md#rt-clm-rewrite-preservation) | Rotation exception, see runtime | Manual edits bypass checks. |
| [RT-RTE-rewrite-state](runtime.md#rt-rte-rewrite-state) | lineage/freshness/recovery | implemented | [RT-OBJ-workstream](runtime.md#rt-obj-workstream) | truth-apt transformation: indeterminate | Rotation and records/decisions reduction | see record | see record | see record | Code refuses selected defects; --write replaces text | Reference/structure checks, not semantic endorsement | Alters visible state; stale-claim override permits continuation | [RT-BAP-resume-state](runtime.md#rt-bap-resume-state) | SRC-1, `.claude/scripts/workstream-rewrite.py` | [RT-CLM-rewrite-preservation](runtime.md#rt-clm-rewrite-preservation) | General preservation claim too broad | Historical recovery requires prior commit/tag, not just a successful transform. |
| [RT-RTE-agent-packet](runtime.md#rt-rte-agent-packet) | check/evidence production | doctrine only | [EPI-OBJ-workstream-claims](#epi-obj-workstream-claims) | no content change | Worker claims against packet/spec and outputs | see record | see record | see record | Verifier advisory PASS/FAIL | Task-specific command/spec domain | Foreground must verify findings | see record | SRC-1, `.claude/agents/verifier.md` | [EPI-CLM-grounded-claims](#epi-clm-grounded-claims) | none | Fresh context does not establish evaluator independence or correctness. |
| [RT-RTE-agent-packet](runtime.md#rt-rte-agent-packet) | disposition/acceptance | doctrine only | [EPI-OBJ-workstream-guidance](#epi-obj-workstream-guidance) | no content change | Task product for intended packet use | see record | see record | see record | Foreground admission; user veto at gates | Evidence-consuming task acceptance, conditional on compliance | Accept, retry, block or stop before next packet | see record | SRC-1, `.claude/skills/workstream-work/SKILL.md` | [EPI-CLM-grounded-claims](#epi-clm-grounded-claims) | none | Product completion is not acceptance of a new general explanation. |
| [EPI-RTE-status-statement](#epi-rte-status-statement) | content transformation | doctrine only | [EPI-OBJ-record-learnings](#epi-obj-record-learnings) | truth-apt transformation: indeterminate | Records to cross-workstream statement | see record | see record | see record | Advisory chat | Attributed premises, no independently derived priority | Informs user selection; no state mutation requested | see record | SRC-1, `.claude/skills/workstream-status/SKILL.md` | none | none | Some joins follow recorded edges; semantic inference needs actual output. |
| [EPI-RTE-status-statement](#epi-rte-status-statement) | check/evidence production | doctrine only | [EPI-OBJ-workstream-claims](#epi-obj-workstream-claims) | no content change | Statement counts, citations and surrounding context | see record | see record | see record | Requested correction/drop before delivery | Occurrence and scoped interpretation, not external premise verification | Mismatched citations corrected or dropped | see record | SRC-1, `.claude/skills/workstream-status/SKILL.md` | none | none | Self-check fixtures calibrate patterns, not every real file or conclusion. |
| [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle) | disposition/acceptance | doctrine only | [EPI-OBJ-workstream-guidance](#epi-obj-workstream-guidance) | no content change | Closure criteria with current evidence | see record | see record | see record | Required user approval by policy | Deliverable/exit scope only | Permits status done, archive and deletion, not arbitrary publication | see record | SRC-1, `.claude/skills/workstream-close/SKILL.md` | [EPI-CLM-gate-validation](#epi-clm-gate-validation) | none | Preapproved unattended path differs from an interactive gate. |
| [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-workstream-claims](#epi-obj-workstream-claims) | truth-apt transformation: acquisition/import | Handoff claims to receiving backlog | see record | see record | see record | Receiver verification requested | Source warrant unknown until local check; provenance requested | Receiver may act, route or decline, then delete processed inbox | see record | SRC-1, `.claude/skills/handoff/SKILL.md` | none | none | Filing is not acceptance; sender approval is destination/visibility authority. |
| [RT-RTE-session-reload](runtime.md#rt-rte-session-reload) | operational admission/selection/consumption | implemented | [RT-OBJ-active](runtime.md#rt-obj-active) | no content change | Retained pointer and signals to host context | see record | see record | see record | Code selection and stdout; model guidance thereafter | No semantic warrant from freshness | Can change what later model inspects | [RT-BAP-resume-state](runtime.md#rt-bap-resume-state) | SRC-1, `.claude/hooks/session-start.sh` | none | none | Full workstream is separately read, not injected wholesale. |
| [RT-RTE-stop-gloss](runtime.md#rt-rte-stop-gloss) | check/evidence production | implemented | [EPI-OBJ-workstream-markers](#epi-obj-workstream-markers) | no content change | Final answer bare-reference form | see record | see record | see record | Best-effort one-turn repair request | Gloss shape, not reference truth or task completion | Host can request another turn | see record | SRC-1, `.claude/hooks/bare-id-guard.py` | none | none | Fail-open and repeated-stop paths prevent universal enforcement. |
| [RT-RTE-acceptance-driver](runtime.md#rt-rte-acceptance-driver) | check/evidence production | implemented | [EPI-OBJ-workstream-guidance](#epi-obj-workstream-guidance) | no content change | Greeting fixture and lifecycle artifacts | see record | see record | see record | Shell verdict; no automatic production update | Fixed scenario only | Reports PASS/FAIL/HELD to maintainer | see record | SRC-1, `tests/va3-acceptance.sh` | [EPI-CLM-gate-validation](#epi-clm-gate-validation) | Outcome cannot identify mechanism | Unexecuted; pattern checks and conditional held classification are not universal safety tests. |

The concrete Learning deduction is see [EPI-RTE-learning-condense](#epi-rte-learning-condense). No row establishes lifecycle integration after acceptance of a produced ampliative claim. Extraction and retention have operational authority, but actual candidate generation, evidence-consuming semantic acceptance and downstream integration are not shown as a connected observed episode.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-grounded-claims](#epi-clm-grounded-claims) | see record | SRC-1, `docs/design.md`; doctrine/design | Artifact checks, user gates and fresh verifier requested | [EPI-RTE-marker-measure](#epi-rte-marker-measure), [RT-RTE-acceptance-driver](runtime.md#rt-rte-acceptance-driver); semantic checks remain doctrine | None supplied | No comparison identifying safety effects; marker evidence is weaker than truth | Coherent grounding protocol with executable file measures | Grounding not universally enforced; ordinary capture can retain unchecked candidates. |
| [EPI-CLM-gate-validation](#epi-clm-gate-validation) | see record | SRC-1, `docs/design.md`; reported operation | Skills reserve gates to users | [RT-RTE-acceptance-driver](runtime.md#rt-rte-acceptance-driver) | Reported earlier tests only | Fixed scenario and prompt-supplied approvals; no attribution to text alone | Driver can test selected lifecycle outcomes | No independently supplied all-constraints trace; native goal not exercised by driver. |
| [RT-CLM-rewrite-preservation](runtime.md#rt-clm-rewrite-preservation) | see record | SRC-1, `.claude/skills/workstream-extract/SKILL.md`; doctrine/design | Extraction orders checking before trimming | [RT-RTE-rewrite-state](runtime.md#rt-rte-rewrite-state), [EPI-RTE-learning-condense](#epi-rte-learning-condense) | None supplied | Local predicates only | Checked syntactic retention on standard path | Rotation intentionally changes headings/checkboxes; Git backup is caller-dependent. |

## Bounded conclusion

**Retained operational claims can guide later sessions before semantic acceptance.** Capture asks the model to persist findings and synthesis, and reload/work routes deliver or request that state. Workstream claims, symbolic disposition markers and plans have different authority paths. Neither persistence nor an APPLIED marker establishes truth or application to another file. The supplied runtime and direct marker implementation support that separation.

**The kit's strongest semantic checks are evidence-consuming protocols, not a single enforcing evaluator.** Review compares dated claims with current artifacts, marks supersession and asks user approval for substantive restructuring. Extract verifies actual governed destinations, permits dropping with rationale and distinguishes deferral from disposition. Work acceptance compares products to packet criteria; closure additionally needs user approval against exit criteria. Each can change operational reliance in its local scope. Those protocols are doctrine only as semantic behavior in this evidence set; their wording alone is not a run.

**Executable evidence is narrow but real.** A dated marker can entail a parser classification; fingerprint and sentence-presence predicates can block a script write. Their checked domain is text form. Condensation's checked deletion may remove a qualification, and rotation has separate checks and explicit stale-claim override. These checks cannot license preserved meaning, external premise truth or reliable behavior. No warranted general explanatory conclusion follows from a preserved heading or a passing smoke test.

**Imports and summaries retain uncertain warrant locally.** Handoff carries source context and requests receiver verification before a claim becomes a task description; filing and deletion do not equal acceptance. Status limits sources, labels unverified premises inline and requests citation checking. Its chat informs user decisions but is not automatically retained or accepted. Capture's synthesis relation is indeterminate without actual inputs and output: the instruction's transfer test does not prove novelty, non-entailment, correctness or acceptance.

No actual accepted ampliative claim, associated test result and post-acceptance integration episode is established. This is not a claim that the model cannot conjecture. No source-supported parameter-learning route is established within the inspected kit, while provider behavior remains uninspected. Retained state and applied guidance can alter future action without a parameter update; improved capacity, exercised self-improvement and causal benefit remain independently unestablished. The design's grounding and autonomous-safety claims have protocol and fixture support, not a system-wide warrant or demonstrated causal effect. Uninspected record handlers and offline suites prevent a system-complete negative about other checking routes.

## Shared records

### Operative objects

#### EPI-OBJ-workstream-claims
Label: Workstream claims and findings

Part of: [RT-OBJ-workstream](runtime.md#rt-obj-workstream)

Source-native identity: Decisions, Learnings, Open Questions and completion/disposition prose inside workstream.md. Representational form: natural language. Storage substrate: consumer Markdown and intended Git history. This part differs from symbolic markers and normative task guidance in what must be checked: current artifacts and source evidence, not regex occurrence. SRC-1, `.claude/skills/workstream-review/SKILL.md`.

> Move 1 asks what is new and unrecorded. This asks what is recorded and no longer true — the pass nothing else runs, because staleness has no event: nothing changes at the moment a Decision becomes false, so the detector has to be comparative, and wider than this file.
> --- `.claude/skills/workstream-review/SKILL.md`

#### EPI-OBJ-workstream-markers
Label: Workstream disposition markers

Part of: [RT-OBJ-workstream](runtime.md#rt-obj-workstream)

Source-native identity: dated terminal/deferred markers in Learning blocks, distinct from their semantic assertions. Representational form: symbolic for the parser consumer. Storage substrate: the same Markdown bytes and intended Git history. Consumers select/count/trim via finite patterns; they do not inspect the claimed destination. SRC-1, `.claude/scripts/workstream_state.py`.

> if marker_counts(body, TERMINAL_RE):
>         return 'terminal'
> --- `.claude/scripts/workstream_state.py`

#### EPI-OBJ-workstream-guidance
Label: Workstream plan and criteria

Part of: [RT-OBJ-workstream](runtime.md#rt-obj-workstream)

Source-native identity: backlog wording, critical-path guidance and Deletion Criteria. Representational form: natural-language policies interpreted by model/user, distinct from fixed-rule marker consumption. Storage substrate: consumer Markdown/Git. Facts invoked as premises remain truth-apt; choosing scope or approving a restructuring is normative. SRC-1, `.claude/skills/workstream-review/SKILL.md`.

> Do not restructure on an assumption you have not surfaced; an option set the user reframes in free text is the signal the framing, not the options, was wrong.
> --- `.claude/skills/workstream-review/SKILL.md`

#### EPI-OBJ-record-learnings
Label: Record Learnings field

Distinct identity: derived JSON fields, not the retained source [RT-OBJ-workstream](runtime.md#rt-obj-workstream) or [RT-OBJ-active](runtime.md#rt-obj-active). Source-native identity: count, terminal, deferred and undispositioned in record.learnings. Form: symbolic JSON. Substrate: process memory/stdout, no automatic retention established. SRC-1, `.claude/scripts/workstream-record.py`.

> return {"count": count, "terminal": terminal, "deferred": deferred,
>             "undispositioned": undispositioned}
> --- `.claude/scripts/workstream-record.py`

### Routes

#### EPI-RTE-capture-synthesis
Label: Capture synthesis proposal

Part of: [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle)

Endpoints/progression: session findings and durable files → foreground model synthesis → Decision/Learning extension or supersession. Owner: foreground model following capture policy. Routine capture admits notes without per-claim user approval; existing substantive/user gates still apply. Trigger: session boundary. Intended use is future work; no universal evidence-consuming semantic acceptance criterion is supplied for new synthesis. Recovery uses scoped commits and supersession. The source does not individuate a produced theory; conditions of consumption, criticism and iteration for an actual theory instance remain uninspected, not inferred from the word synthesis. SRC-1, `.claude/skills/workstream-capture/SKILL.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested routed findings and synthesis-level pattern.
- Later read-back: committed Decisions/Learnings are requested inputs to later work/review.
- Delegated visibility: uninspected — no live packet or host propagation supplied for this sweep.
- Selection predicate: findings not yet durable; synthesis asks what changes another piece of work.
- Invalidation or expiry: extend/supersede existing entries; later review may mark stale claims.
- Activation or effect: requested retained content can guide later model planning through file context; activation unobserved.
- Evidence limits: no actual input/output pair establishes entailed derivation or ampliative conjecture; generic model generation is insufficient.

> Synthesis is a different question from detection, not a harder pass at it; the test is whether anything in the sweep's output would change how a DIFFERENT piece of work is done -- if nothing would, the step is still owed.
> --- `.claude/skills/workstream-capture/SKILL.md`

#### EPI-RTE-marker-measure
Label: Learning marker measurement

Distinct identity: deterministic record-field production, not the write route [RT-RTE-rewrite-state](runtime.md#rt-rte-rewrite-state) or the host delivery route [RT-RTE-session-reload](runtime.md#rt-rte-session-reload). Endpoints: folded workstream Learning blocks → learnings_field/disposition → JSON classifications and counts. Owner: Python predicates. Target/domain: entries in the Learnings section and dated sentence/clause-start markers, not destination truth. There is no semantic answer oracle. Self-check compares predicates against hand-coded positives/negatives; it does not evaluate work completion. SRC-1, `.claude/scripts/workstream-record.py`, `.claude/scripts/workstream_state.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: count, terminal number and deferred/undispositioned entries.
- Later read-back: inapplicable — this measurement does not persist changed state; later runs recompute from files.
- Delegated visibility: inapplicable — the inspected functions invoke no delegate.
- Selection predicate: Learning-shaped item block starting within the Learnings section; marker grammar prioritizes terminal over deferred.
- Invalidation or expiry: recomputed on next read; changed bytes may change classification.
- Activation or effect: classifications feed status and drain signals by code/prompt paths; actual behavior change unobserved.
- Evidence limits: predicate truth is not the truth of the marked claim or disposition.

> if kind == 'item' and LEARNING_RE.match(raw[0]) and start in learnings_lines:
>             count += 1
>             d = disposition(text)
> --- `.claude/scripts/workstream-record.py`

#### EPI-RTE-still-true
Label: Still-true comparison and withdrawal

Part of: [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle)

Endpoints: dated claims/plans → comparison with current repo, sibling workstreams and named commitments → stale finding, in-place supersession, approved substantive restructure. Foreground model proposes and investigates; user decides substantive restructure, while mechanical repairs proceed. Target is current applicability/truth of recorded premises, distinct from whether a premise still matters. Reference documents provide comparison material, not an oracle. Trigger: drift, staleness or request. Guidance persists as dated state/commits; rollback relies on history, not a software veto. SRC-1, `.claude/skills/workstream-review/SKILL.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: drift/stale findings and requested user decisions.
- Later read-back: supersession marks and changed backlog/ACTIVE.md are committed for later model use.
- Delegated visibility: optional set-level adversarial subagent receives the set without workstream priors; host isolation uninspected.
- Selection predicate: dated Decisions/completed tasks, criteria, duplicate facts and framing assumptions; widen beyond the single file.
- Invalidation or expiry: mark superseded text when found, re-derive order and recheck at later drift.
- Activation or effect: model policy requests changed reliance and revised task selection; substantive changes need user approval.
- Evidence limits: current truth and revised reliance are not observed; no particular retained theory instance demonstrates conditions 1–4.

> Read state against the project's DESIGNATED-AUTHORITY documents — the ADR, the design note, the spec — in both directions — a criterion and an ADR can contradict each other with neither referencing the other, and authority is not accuracy.
> --- `.claude/skills/workstream-review/SKILL.md`

> Mark every stale hit in place at the moment you find it (`~~superseded by ...~~`, or a dated note saying what overtook it) rather than collecting them for a later pass.
> --- `.claude/skills/workstream-review/SKILL.md`

#### EPI-RTE-disposition-check
Label: Extraction destination verification

Part of: [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle)

Endpoints: resolved Learning/OQ and claimed disposition → inspect governed file/commit/destination → apply, hand off or drop with rationale. Foreground model checks and edits; handoff separately requires user destination/visibility confirmation. Trigger: drain symptoms, review or closure. Check target is whether the substance actually reached its governed destination; acceptance of a general proposition's truth is a different question. A future task is not an implemented result. Rejection is available through drop/reroute; commits preserve changes and rationale. SRC-1, `.claude/skills/workstream-extract/SKILL.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: requested extraction/disposition account and edits.
- Later read-back: named permanent files and disposition markers guide future work and review.
- Delegated visibility: cross-project handoffs must supply self-contained context; actual receipt unobserved.
- Selection predicate: every resolved Learning and settled OQ; still-live entries remain; sweep already-applied entries too.
- Invalidation or expiry: verify destinations each pass; installed/generated copies remain provisional until governing source changed.
- Activation or effect: requested governed-file edits can change later guidance; retained marker alone cannot establish activation.
- Evidence limits: destination verification is not universal evidence for the explanatory content of a Learning; no observed accepted ampliative claim is supplied.

> A file this project does not GOVERN — an installed copy, a generated file, a vendored template: provisional until the change reaches whatever governs the file; verify it there.
> --- `.claude/skills/workstream-extract/SKILL.md`

> Only after Move 1, and the order is load-bearing: trimming before extracting destroys the insight you were about to route, and the trim looks successful either way.
> --- `.claude/skills/workstream-extract/SKILL.md`

#### EPI-RTE-learning-condense
Label: Terminal Learning sentence condensation

Part of: [RT-RTE-rewrite-state](runtime.md#rt-rte-rewrite-state)

Endpoints: CLI learnings request → terminal-marker selection → sentence selection → learning_loss, count and finish fingerprint checks → dry report or file replacement. Owner: Python code, with caller supplying --write. Trigger/proposal: extract recommends trimming terminal entries; caller chooses applicability, no per-content human check enforced. Oracle is literal presence/count/structure, not source truth or semantic preservation. Refusal precedes this CLI's write; direct file writes bypass it; recovery needs prior Git retention. SRC-1, `.claude/scripts/workstream-rewrite.py`, `.claude/scripts/workstream_state.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: entry/byte report, refusal, NO CHANGE or WRITTEN.
- Later read-back: with --write, selected sentences replace source prose for later hook/model invocations.
- Delegated visibility: inapplicable — inspected dispatch/transform/write path invokes no delegate.
- Selection predicate: terminal Learning, recognized prefix, multiple sentences, no later addendum; retain first statement, provenance plus following statement when applicable, target sentences and latest terminal-marker sentence.
- Invalidation or expiry: later writes replace text; count or preservation mismatch refuses before finish/write.
- Activation or effect: executable text reduction and local write veto; semantic effect on later consumers unobserved.
- Evidence limits: literal statement/target/disposition checks do not protect every qualification or mechanism sentence.

Concrete deduction, not target execution: inside an otherwise conforming `## Learnings` section, take `- L1 (2026-01-01): The probe works. Only on Linux. Extra explanation is long enough to remove. APPLIED 2026-01-02.` The sentence splitter separates at punctuation plus whitespace. APPLIED at a sentence start with a date makes disposition terminal. With no provenance, integration-target sentence or addendum, condense_learning keeps sentence zero and the disposition, yielding joined text `- L1 (2026-01-01): The probe works. APPLIED 2026-01-02.` learning_loss finds its required statement and last marker intact; Learning count and heading/checkbox fingerprint are unchanged. The qualifier is dropped. This demonstrates a permitted loss of scope, not an actual deployed false statement. For arbitrary entries the relation remains indeterminate; it is not certified non-ampliative reshaping.

> keep = set(range(2 if PROVENANCE_RE.match(sentences[0]) else 1))
>     keep.update(i for i, x in enumerate(sentences) if TARGET_RE.search(x))
>     keep = {i for i in keep if sentences[i] != disp and not ADDENDUM_RE.match(sentences[i])}
>     condensed = ' '.join([sentences[i] for i in sorted(keep)] + [disp])
> --- `.claude/scripts/workstream-rewrite.py`

> if fingerprint(new_lines) != fingerprint(old_lines):
>         sys.stderr.write("%s: structure changed (headings or checkbox IDs/states); refusing to write\n" % PROG)
>         return 1
> --- `.claude/scripts/workstream-rewrite.py`

#### EPI-RTE-status-statement
Label: Status synthesis and citation check

Distinct identity: on-demand cross-workstream chat production/checking, not [RT-RTE-session-reload](runtime.md#rt-rte-session-reload)'s hook output or [RT-RTE-state-lifecycle](runtime.md#rt-rte-state-lifecycle)'s retained updates. Endpoints: bounded records/files → foreground statement → count/calibration checks → scout citation occurrences/context → correction/drop → user. Owner: foreground interprets; scout reports occurrences, not a verdict. Criteria: count agreement, calibrated patterns and matching cited text, with unverified premise labels. Scope excludes external premise verification and priority among independent chains. Operating mode: requested read-only project status. No automated product admission or rollback is present; report correction precedes delivery. SRC-1, `.claude/skills/workstream-status/SKILL.md`.

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: roster, chains, gates, disagreements and coverage gaps in chat.
- Later read-back: inapplicable — status requests no file writes; optional user copying is separate.
- Delegated visibility: statement and records to fresh scout for cited claim text and surrounding context.
- Selection predicate: all workstreams including paused, ACTIVE, archive/inbox, Git reads and PROJECT-declared context; bounded exception for empty PROJECT descriptions.
- Invalidation or expiry: rerun measures for current status; do not recall old hook output.
- Activation or effect: advisory user selection; actionable findings name the owning skill rather than applying changes.
- Evidence limits: matching citation occurrence does not establish every inference; actual statement/output not supplied.

> **A premise the statement repeats is marked where it appears** — `asserted by <file>, unverified here`, inline, never disclaimed twenty lines later. The skill does not verify it; that would make a read-only skill a verifying one.
> --- `.claude/skills/workstream-status/SKILL.md`

> A citation that comes back as anything but MATCH is corrected or dropped before delivery; reading a cited line against a claim is the check a grep cannot make.
> --- `.claude/skills/workstream-status/SKILL.md`

### Claims

#### EPI-CLM-grounded-claims
Label: Grounded claims and safe goal work

Distinct identity: semantic grounding/safety rationale, not [RT-CLM-rewrite-preservation](runtime.md#rt-clm-rewrite-preservation)'s rewrite predicate. Claimed operation: cited completion evidence plus durable, mechanically checkable state supports safe goal-driven autonomy. SRC-1, `docs/design.md`, doctrine/design. Local measurements and requested artifact checks support a scoped protocol; no causal or deployed-safety guarantee follows.

> The kit replaces that with *grounded claims*: a checkbox closes only with cited evidence (a commit, a command's output, a count), which the user can check at the gate.
> --- `docs/design.md`

> Durable, mechanically-checkable state is what makes goal-driven autonomy safe.
> --- `docs/design.md`

#### EPI-CLM-gate-validation
Label: Text-only gate validation report

Distinct identity: attributed lifecycle test outcome, not [RT-CLM-rewrite-preservation](runtime.md#rt-clm-rewrite-preservation). Claimed operation: prior autonomous acceptance sessions honored all user-authority constraints from skill text alone. SRC-1, `docs/design.md`, reported operation. The inspectable driver is [RT-RTE-acceptance-driver](runtime.md#rt-rte-acceptance-driver), not those runs' evidence. Prompt preapproval and artifact assertions cannot independently isolate skill text as the cause.

> This was validated directly: in the kit's acceptance tests, fully autonomous sessions ran the create/work/close lifecycle and honored every user-authority constraint — no auto-starting work after creation, no auto-passing checkpoint gates, no self-certified closure — from the skill text alone.
> --- `docs/design.md`

> # fixture's own Learnings and applies them to its installed skill copies. Read
> # Session C's output and the fixture's Learnings (in its git log, since the
> # closure archives the workstream file) before deleting the fixture -- both
> # findings from the first two runs were visible only there, while the summary
> # said ALL CHECKS PASS.
> --- `tests/va3-acceptance.sh`

The driver's own comment supplies a countercase to equating its green summary with defect-free guidance. It is reported operation only. Reading saved fixture evidence and separately updating the kit could support a later improvement route; this boundary supplies no resulting update and exercised downstream causal chain.
