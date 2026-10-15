---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Claude Code dynamic workflows: documented claim checking, structural validation, operational reliance and replay, without implementation or run evidence."
run-id: AAS-2026-10-14-workflows-f9c2f80a3a94-01
reviewed-boundary: workflows-2026-10-14
---

# Claude Code dynamic workflows epistemic report

## Source-and-claim boundary

The question is how this workflow subsystem acquires or produces truth-apt content, checks it, grants reliance and carries it into later behavior. The frozen scope and exclusions are those of [boundary.md](boundary.md#boundary-and-evidence); the only source is SRC-1 in its [Source register](boundary.md#source-register). I directly read the entire 506-line capture, including the example script. Supplied runtime findings organize the account but do not establish implementation.

All positive routes below have architectural status `doctrine only`. The executable-looking example is documentation, not inspected runtime implementation. No target execution or supplied run establishes activation. Enclosing permission machinery, worker tool implementations, linked specifications and actual bundled, saved or plugin scripts are excluded. Their missing evidence prevents conclusions about enforcement, exact evaluator thresholds, tool correctness and complete runtime coverage respectively. Provider parameters and immutable model revisions are uninspected; see [RT-CMP-claude-model](runtime.md#rt-cmp-claude-model). No fixed-weight, parameter-learning or provider-wide negative follows.

The consequential quality claim is [RT-CLM-research-report](runtime.md#rt-clm-research-report), including the assertion of greater trustworthiness than a single pass. [RT-CLM-runtime-limits](runtime.md#rt-clm-runtime-limits) concerns operational ceilings, not factual warrant. Research check failures, unverified claims, fan-out nulls and replay without factual refresh are countercases to interpreting successful completion or a cited report as universal acceptance.

| Entry point or operation | Source path / local anchor | Coverage and evidence basis | Limit and conclusion prevented |
| --- | --- | --- | --- |
| Explicit requests, ultracode, named commands, headless and SDK launch | SRC-1, capture, `Have Claude write a workflow`; `Approve the plan before it runs` | Direct read and supplied [RT-RTE-workflow-launch](runtime.md#rt-rte-workflow-launch) | Hook/classifier/host internals excluded; launch authorization is not truth checking |
| Bundled `/deep-research`, WebSearch, fetching, voting and report | SRC-1, capture, `Bundled workflows`; `Read the report` | Direct read; [EPI-RTE-research-acquisition](#epi-rte-research-acquisition), [EPI-RTE-research-check](#epi-rte-research-check), [EPI-RTE-report-disposition](#epi-rte-report-disposition) | Actual bundled body excluded; cannot establish criteria, independence or correctness |
| `agent()`, `pipeline()`, `parallel()`, structured output | SRC-1, capture, `What the saved script looks like` | Direct read and supplied [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration); [EPI-RTE-schema-check](#epi-rte-schema-check) | No implementation or outcomes; schema domain only |
| Example return filtering and terminal consumption | SRC-1, capture, `What the saved script looks like`; `How a workflow runs` | Direct read; [EPI-RTE-result-filter](#epi-rte-result-filter) | No actual audit; completeness of discovery and findings unestablished |
| Checker/fixer, intermittent tests, adversarial audit, ranking/deduplication and migration examples | SRC-1, capture, `Example workflow prompts` | Direct read; [EPI-RTE-checker-loop](#epi-rte-checker-loop) | Requests, not supplied scripts or runs; exact check-to-edit and ranking paths unresolved |
| Save/edit/reload, plugin loading, args, metadata/syntax and symlink checks | SRC-1, capture, `Save the workflow for reuse`; `Edit a saved script` | Direct read and supplied [RT-RTE-script-admission](runtime.md#rt-rte-script-admission) | Loader/plugin implementations and authoring reference excluded; no semantic script acceptance inferred |
| Results, replay, restart, null/error, usage waits, pause/stop | SRC-1, capture, `Manage runs` | Direct read and supplied [RT-RTE-run-replay](runtime.md#rt-rte-run-replay), [RT-RTE-agent-recovery](runtime.md#rt-rte-agent-recovery) | No storage/matching implementation; no freshness or exactly-once guarantee |
| UI, cache, caps, size advice, models, disable settings | SRC-1, capture, `Watch the run`; `Prompt caching in a fan-out`; `Behavior and limits`; `Cost`; `Turn workflows off` | Direct read and supplied [RT-CLM-runtime-limits](runtime.md#rt-clm-runtime-limits), [RT-CMP-claude-model](runtime.md#rt-cmp-claude-model) | Visibility and liveness controls do not establish epistemic evaluation; cache is not shared findings |

This is complete coverage of the captured page, not a system-complete negative about Claude Code. No frozen CLI dispatch, registered tool implementation or executable hook is available to inspect. The documented Workflow approval alternatives were checked against the runtime account; no necessary supersession was found.

## Epistemic-object inventory

Fields owned by supplied objects remain in those records rather than being copied here. Objects below distinguish factual candidates, structural constraints and operational control.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-workflow-script](runtime.md#rt-obj-workflow-script) | None necessarily in control flow; embedded tasks can request factual judgments | see cited record | SRC-1, `What the saved script looks like`; `Edit a saved script` | Literal code and interpreted task text have different consumers; no actual generated script inspected |
| [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results) | Worker prose/JSON may assert files, defects or research facts | see cited record | SRC-1, `How a workflow runs`; `Which agents run again` | Candidate truth and lineage unresolved; saved/completed is not accepted |
| [EPI-OBJ-research-claims](#epi-obj-research-claims) | Claims about the invoked question, with cited external sources | see cited record | SRC-1, `Bundled workflows`; `Read the report` | No instance, provenance trace, independent reference answer or exact acceptance rule |
| [EPI-OBJ-output-schema](#epi-obj-output-schema) | Shape constraint, not itself factual findings | see cited record | SRC-1, `What the saved script looks like` | Constraints validate encodings, not truth of enclosed assertions |
| [RT-CMP-claude-model](runtime.md#rt-cmp-claude-model) | Accessible parametric truth-apt unit: not determinable | see cited record | SRC-1, `Cost` | Opaque numerical state, substitution and version uninspected |

## Authority-route ledger

`see` denotes fields owned by a linked declaration. All results are possible declared results, not observed ones. Current-run delivery is distinguished from retained read-back.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-research-acquisition](#epi-rte-research-acquisition) | content transformation | doctrine only | [EPI-OBJ-research-claims](#epi-obj-research-claims) | truth-apt transformation: acquisition/import | External search/fetched content enters research | WebSearch and readers; public-source domain | see record | Retrieved source content | Uninspected; declared delivery | Source warrant unknown; import is not original production | Makes evidence available for checking | Research workers, search/fetch results, advisory input, current run | SRC-1, `Bundled workflows` | [RT-CLM-research-report](runtime.md#rt-clm-research-report) | none | No actual sources or traces |
| [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration) | content transformation | doctrine only | [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results) | truth-apt transformation: indeterminate | Worker interpretation/synthesis | Model and tools; task-dependent domain | see record | Prose/JSON candidate | Uninspected; declared result delivery | Candidate generation only; no general entailment or non-entailment established | Returned value can guide branches and later worker prompts | see [RT-BAP-agent-prompts](runtime.md#rt-bap-agent-prompts) and [RT-BAP-script-control](runtime.md#rt-bap-script-control) | SRC-1, `What the saved script looks like` | none | none | Need actual input/output pairs to distinguish reshaping, derivation and conjecture |
| [EPI-RTE-schema-check](#epi-rte-schema-check) | check/evidence production | doctrine only | [EPI-OBJ-output-schema](#epi-obj-output-schema) | no content change | Schema contradiction and returned JSON shape | Program validator; supported schema/encoding domain | see record | Validation failure or conforming output | Uninspected; declared check | Structural license only, not file-list completeness or factual validity | Produces structural decision input | Validator, error/result channel, checking, launch/output attempts | SRC-1, `What the saved script looks like` | none | none | Validator implementation and schema dialect uninspected |
| [EPI-RTE-schema-disposition](#epi-rte-schema-disposition) | disposition/acceptance | doctrine only | [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results) | no content change | Launch/result admission after structural check | Runtime consumes validation; JSON shape domain | see record | No worker launch, retry, accepted shape or call error | Uninspected; declared enforcing gate | Accepts shape for structured return only | Blocks contradictory call; retries invalid output, fails on exhausted attempts | Runtime, schema error/conformance, enforcing, one call | SRC-1, `What the saved script looks like` | none | none | Not acceptance of ampliative factual content |
| [EPI-RTE-research-check](#epi-rte-research-check) | check/evidence production | doctrine only | [EPI-OBJ-research-claims](#epi-obj-research-claims) | no content change | Claim support against sources | Verifier agents and votes; invoked research domain | see record | Survived/failed cross-check or unable to check | Uninspected; declared evidence-producing role | Bounded source checking intended; no calibrated warrant shown | Supplies disposition input | Report process, verification/vote results, evaluative, current run | SRC-1, `Bundled workflows`; `Read the report` | [RT-CLM-research-report](runtime.md#rt-clm-research-report) | none | Independence, thresholds and source interpretation uninspected |
| [EPI-RTE-report-disposition](#epi-rte-report-disposition) | disposition/acceptance | doctrine only | [EPI-OBJ-research-claims](#epi-obj-research-claims) | no content change | Whether/how a claim enters report | Bundled process consumes cross-check outcomes; question scope | see record | Filter failed claims; keep uncheckable claims labelled unverified | Uninspected; declared selection | Intended report criterion is surviving cross-check; actual evidence-consuming acceptance unobserved | Removes failed candidates, qualifies uncheckable ones | Report assembler then session reader, cited report, selection/advisory, terminal report | SRC-1, `Read the report` | [RT-CLM-research-report](runtime.md#rt-clm-research-report) | none | Report inclusion is not uniform verification |
| [EPI-RTE-result-filter](#epi-rte-result-filter) | content transformation | doctrine only | [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results) | truth-apt transformation: non-ampliative reshaping | Example result list | JavaScript truthiness; array-value domain | see record | Truthy results retained; null slots dropped | Uninspected runtime; explicit example rule | No new warrant for surviving findings | Changes which findings foreground receives | Script return, filtered list, selection, one run | SRC-1, `What the saved script looks like` | none | none | Loss of failed slots can hide incomplete audit; no implementation deduction claimed |
| [EPI-RTE-checker-loop](#epi-rte-checker-loop) | behavior/policy adaptation | doctrine only | [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results) | non-truth-apt policy/content update: requested edits guided by checker errors | Project code against type-checker criterion | Requested `npx tsc --noEmit`; TypeScript diagnostics domain | see record | Fix/recheck; pass or stop without progress | Uninspected; requested feedback loop | Type-check result licenses only configured checker success, not general correctness | Requested continuation, edits or stop | Workers, diagnostics and task prompts, model-mediated, rounds of one task | SRC-1, `Keep fixing until a check passes` | none | none | No script, checker config or observed changes |
| [RT-RTE-workflow-launch](runtime.md#rt-rte-workflow-launch) | operational admission/selection/consumption | doctrine only | [RT-OBJ-workflow-script](runtime.md#rt-obj-workflow-script) | no content change | Launch permission, not claim truth | see record | see record | Approve/cancel/deny | Uninspected; declared permission gate | No factual authority conferred | Allows or blocks background run | see record | SRC-1, `Approve the plan before it runs` | none | none | Human review is mode-dependent, not universal |
| [RT-RTE-script-admission](runtime.md#rt-rte-script-admission) | retention | doctrine only | [RT-OBJ-workflow-script](runtime.md#rt-obj-workflow-script) | no content change | Reusable orchestration copy | see record | see record | Saved/edited workflow | Uninspected; declared save/load | No acceptance of task theory inferred | Reusable script can control future work | see [RT-BAP-script-control](runtime.md#rt-bap-script-control) | SRC-1, `Save the workflow for reuse`; `Edit a saved script` | none | none | Structural loader and save-path checks do not prove semantic quality |
| [RT-RTE-run-replay](runtime.md#rt-rte-run-replay) | retention | doctrine only | [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results) | no content change | Completed result tracking | see record | see record | Session-associated saved values | Uninspected; declared persistence | Completion is not factual acceptance | Enables later reuse | see record | SRC-1, `How a workflow runs`; `Resume after you leave the session` | none | none | No lifecycle integration demonstrated |
| [RT-RTE-run-replay](runtime.md#rt-rte-run-replay) | lineage/freshness/recovery | doctrine only | [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results) | no content change | Ordered prefix reuse and suffix invalidation | see record | see record | Cached prefix, recomputed suffix or missing-result error | Uninspected; declared recovery rule | Prompt compatibility, not source freshness or truth | Cached results can drive later calls without another worker check | see record | SRC-1, `Which agents run again` | none | none | Changes to external files, sources or model/options are not specified as invalidators |
| [RT-RTE-agent-recovery](runtime.md#rt-rte-agent-recovery) | operational admission/selection/consumption | doctrine only | [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results) | no content change | Liveness, not content validity | see record | see record | Retry, null or direct-await error | Uninspected; declared control | No epistemic endorsement from continuation | Repeat work, continue fan-out or terminate | see record | SRC-1, `When an agent stalls and restarts` | none | none | Edits survive while transcript is lost; no withdrawal/rollback of effects |

Schema checking and disposition are separate functions of the same documented call. Research checking and reporting likewise remain separate. Retention and replay do not establish lifecycle integration: there is no supplied accepted claim linked into a knowledge organization after an evidence-consuming acceptance event. That is an evidence limit, not a claim that configurable workflows cannot implement integration.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-research-report](runtime.md#rt-clm-research-report) | see record | SRC-1, `Bundled workflows`; `Read the report`; `When to use a workflow`, doctrine/design | Declares acquisition, checking, voting, filtering and unverified labels; see [EPI-RTE-research-check](#epi-rte-research-check), [EPI-RTE-report-disposition](#epi-rte-report-disposition) | None inspected | None supplied | No single-pass comparison or verifier intervention; correlated agents and incorrect sources remain possible | A declared quality pattern, not demonstrated superior trustworthiness or accepted factual production | Thresholds, independence and actual source warrant unknown |
| [RT-CLM-runtime-limits](runtime.md#rt-clm-runtime-limits) | see record | SRC-1, `Behavior and limits`; `Set a size guideline`, doctrine/design | see record; scheduling gates differ from advisory authoring input | None inspected | None supplied | No causal cost measurement; caps do not evaluate content or bound per-agent spend | Declared resource constraints, not epistemic coverage guarantees | Fan-out errors/null filtering defeat inferring a complete factual audit from a final list |

## Bounded conclusion

The captured documentation declares acquisition of external research content, model-mediated candidate outputs and a consequential check-to-report route. Imported source warrant is unknown. The bundle promises cross-checking and voting, exclusion of failed claims, and explicit unverified labels for claims that cannot be checked. Its intended acceptance criterion is surviving cross-checking for inclusion in the invoked question's report. Neither precise criteria nor an actual evidence-consuming acceptance event is supplied. Citations, votes and a returned report establish no independent answer oracle or produced accepted ampliative claim.

Worker transformations remain indeterminate without concrete task inputs and outputs: factual invention, entailed derivation and faithful reshaping cannot be discriminated. No warranted-premise derivation is established. The example's truthiness filtering is explicit non-ampliative list reshaping in documentation, not inspected deterministic implementation. It can remove null failures without establishing that every requested file was audited.

Structural validation has a narrower license. It concerns schema contradictions and output conformance. Runtime disposition can prevent launch, retry, or fail a call based on these checks. Shape conformance does not establish discovery completeness, defect correctness or research truth. Launch permission, save-path checks, metadata rules and syntax checks similarly confer operational authority within their own domains, not epistemic authority over returned claims.

Saved orchestration and completed results have declared future consumers. Replay can supply earlier values to script control without another worker invocation. Its compatibility check concerns prompt/start order and prior failure; it is not a documented factual freshness evaluator. Stalled retries lose the prior transcript while leaving file effects intact. Report filtering withdraws a candidate from the report, not previously performed edits. Retention, reuse and continued execution therefore remain distinct from acceptance, lifecycle integration and rollback.

The checker/fixer prompt requests direct behavior adaptation from diagnostics, bounded to configured type-checking and task rounds. Audit verification, ranked/deduplicated summaries and intermittent-test discovery are also requested patterns, not traced instances. Inspectable code edits and rerunnable scripts alone establish neither improved future capacity, formulated theory criticism nor exercised self-improvement. Model parameters, reflection and autonomy remain independently unestablished at this boundary. Missing implementation, execution and comparative causal evidence prevents stronger claims, while leaving the source's distinct declared mechanisms intact.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-research-claims
Label: Research claims

Part of: [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results)

Source-native identity: individual research claims handled by `/deep-research`, including candidates surviving checks and claims listed as unverified. Representational form: natural-language propositions and source citations, with vote/check representation uninspected. Storage substrate: worker results and terminal report in the session; encoding and retention format uninspected. This material part differs from generic agent results by its research check and report-selection consumers. No concrete claim instance is supplied.

Evidence: SRC-1, `Read the report`, doctrine/design:

> When the run finishes, the report appears in your session. It cites the sources each claim came from, with claims that didn't survive cross-checking already filtered out.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### EPI-OBJ-output-schema
Label: Output schema

Source-native identity: `schema` option to `agent()`. Representational form: symbolic JSON-shape constraints interpreted by a validator. Storage substrate: option in workflow code and runtime call state; internals uninspected. Distinct from [RT-OBJ-workflow-script](runtime.md#rt-obj-workflow-script): this is the call's shape specification, which may be embedded in or constructed by a script, not the whole script. Distinct from [RT-OBJ-agent-results](runtime.md#rt-obj-agent-results): it constrains the result rather than containing its factual assertions.

Evidence: SRC-1, `What the saved script looks like`, doctrine/design:

> If you pass a `schema` on an `agent()` call, that subagent returns JSON matching the shape instead of prose. Claude Code checks the schema before starting the subagent: when it can prove the schema contradicts itself, the call fails with an error naming the contradiction, and the subagent never starts. One contradiction it can prove is a `required` key that `additionalProperties: false` rules out.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

### Routes

#### EPI-RTE-research-acquisition
Label: Research acquisition

Documented question input → web searches across angles → fetched sources → checking and synthesis workers. Owner: bundled workflow and model-backed workers, exact split uninspected. This specializes [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration) but is not identical to its general worker-call contract; acquisition has an external-content boundary and does not confer original production warrant. Imported lineage is advertised through report citations; actual source truth and preservation are unknown.

- Immediate return: search/fetched content available to the research process; exact intermediates uninspected.
- Later read-back: uninspected — no acquisition-specific retained-source reload contract in the capture.
- Delegated visibility: readers/verifiers receive source material by the declared research process; exact payloads uninspected.
- Selection predicate: invoked question and several search angles; actual query and source ranking policy uninspected.
- Invalidation or expiry: uninspected — no source freshness or invalidation contract for this bundle.
- Activation or effect: claimed evidence acquisition for checking and synthesis; not observed.
- Evidence limits: bundle body, actual searches, source content and run traces excluded or unsupplied.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Evidence: SRC-1, `Run the workflow`, doctrine/design:

> Run `/deep-research` with a question you want investigated. It fans out web searches across several angles, fetches and cross-checks the sources it finds, and synthesizes a cited report.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### EPI-RTE-research-check
Label: Research check

Source-linked claims → verifier agents/source cross-checking and voting → check outcomes consumed by [EPI-RTE-report-disposition](#epi-rte-report-disposition). Owner: bundled process; human supplies question, not each verdict. Distinct from the broader [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration); closest claim is [RT-CLM-research-report](runtime.md#rt-clm-research-report). Target is each research claim in the question domain. Evaluator is model-backed verification against sources; exact votes, independence, thresholds and expected-answer reference are uninspected. Model judgment is not an answer oracle. Operating mode: open invoked research questions, not a supplied controlled experiment. Who proposes particular claims and can veto internal judgments is uninspected; downstream filtering is separately declared.

- Immediate return: declared cross-check/vote outcome; inability to check is distinct from refutation.
- Later read-back: uninspected — persistent verification records and later checking consumers unspecified.
- Delegated visibility: verifier agents check claims against sources; precise claim/source framing uninspected.
- Selection predicate: each claim under the bundled report process, detailed selection uninspected.
- Invalidation or expiry: uninspected — no verifier-result expiry or correction policy supplied.
- Activation or effect: claimed production of judgments for report filtering/qualification; unobserved.
- Evidence limits: source supplies contract, not verifier prompts, evidence traces, calibration or comparative causal results.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Evidence: SRC-1, `Bundled workflows`, doctrine/design:

> | `/deep-research <question>` | Fans out web searches on a question across several angles, fetches and cross-checks the sources it finds, votes on each claim, and returns a cited report with claims that didn't survive cross-checking filtered out. Requires the [WebSearch tool](/docs/en/tools-reference#websearch-tool-behavior) to be available |
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### EPI-RTE-report-disposition
Label: Report disposition

Cross-check outcomes → report filtering and unverified labelling → cited report in foreground session. Owner: bundled report process, detailed model/code split uninspected. Distinct identity from [EPI-RTE-research-check](#epi-rte-research-check): this consumes evaluation to change inclusion/reliance; [RT-CLM-research-report](runtime.md#rt-clm-research-report) supplies the nearest broader claim. Proposal: candidate research claim. Intended criterion: survive cross-check for the invoked report; failed claims rejected, uncheckable ones reported as unverified. Admission consumer/threshold is uninspected; human may judge final report but no per-claim human gate is declared. No independent answer oracle supplied. Open-question mode. Guidance is the bundled cross-check/vote contract; report persists in session, while revision/rollback of earlier published claims is uninspected.

- Immediate return: cited report with failed claims removed and uncheckable claims marked unverified.
- Later read-back: uninspected — report-specific later reliance or reload not traced by this page.
- Delegated visibility: final foreground reader receives selected claims and citations, not every intermediate candidate.
- Selection predicate: cross-check survival versus failure versus inability to check; exact threshold uninspected.
- Invalidation or expiry: uninspected — no post-report correction or withdrawal protocol supplied.
- Activation or effect: claimed selection and qualification of final content; exercised reliance unobserved.
- Evidence limits: no report instance, exact acceptance algorithm or evidence-consuming decision trace; intended inclusion is not observed factual acceptance.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Evidence: SRC-1, `Read the report`, [EPI-OBJ-research-claims](#epi-obj-research-claims), and this countercase, doctrine/design:

> When the verifier agents can't check a claim, such as after a rate limit or API error, the report lists that claim as unverified instead of counting it as refuted.
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### EPI-RTE-schema-check
Label: Schema check

Part of: [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration)

Schema specification → contradiction check before launch; worker JSON → validation during output attempts. Owner: Claude Code validator, implementation uninspected. Target/domain: supported schema contradictions and JSON conformance, not semantic truth. Errors and conformance feed [EPI-RTE-schema-disposition](#epi-rte-schema-disposition); no independent factual answer oracle. Evidence is SRC-1, `What the saved script looks like`, at [EPI-OBJ-output-schema](#epi-obj-output-schema), and the validation-retry passage below. This is the checking part of the supplied container, not a replacement.

- Immediate return: contradiction or output-validation result; exact successful-result encoding uninspected.
- Later read-back: inapplicable — no retained-check reload in this described checking function.
- Delegated visibility: subagent gets schema-constrained task; validator gets schema and output, exact retry framing uninspected.
- Selection predicate: `schema` supplied on a call; check only contradictions it can prove.
- Invalidation or expiry: inapplicable — each described call/output attempt is checked against its supplied schema.
- Activation or effect: claimed structural evaluation, separate from its consequential disposition.
- Evidence limits: dialect, validator coverage and implementation uninspected; cannot license factual correctness.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

#### EPI-RTE-schema-disposition
Label: Schema disposition

Part of: [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration)

Schema-check outcome → no launch on contradiction, constrained output attempts, returned structured result or error after retries. Owner: runtime consumes validator outcomes. Computational gate, not human content review; schema author supplies criterion, while per-call proposer identity can vary. Veto: runtime fails contradictory or persistently invalid calls. Open-task mode. No factual oracle. Proposed admission is encoded output for use by caller; rejection/recovery is error or retries, not rollback of prior tool effects. Guidance: supplied schema. No durable revision or accepted knowledge is established.

- Immediate return: shaped worker result or call error including last validation failure.
- Later read-back: inapplicable — this function describes admission, not persisted-result reload.
- Delegated visibility: caller receives returned value or failure; complete failed-attempt contents uninspected.
- Selection predicate: schema conformance; contradiction blocks launch and retry exhaustion fails output.
- Invalidation or expiry: inapplicable — applies to the current constrained call.
- Activation or effect: claimed blocking/retry/failure or successful shape admission; unobserved.
- Evidence limits: no actual call trace or retry internals; successful conformance is not factual acceptance.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Evidence: SRC-1, `What the saved script looks like`, doctrine/design, with [EPI-OBJ-output-schema](#epi-obj-output-schema):

> If the subagent's output still fails validation after five attempts, the call fails with an error that includes the last validation failure. To change the attempt count, set [`MAX_STRUCTURED_OUTPUT_RETRIES`](/docs/en/env-vars).
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### EPI-RTE-result-filter
Label: Result filter

Part of: [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration)

Example pipeline array → `audits.filter(Boolean)` → terminal return. Owner: documented script author/rule. Target: truthy array elements, not finding correctness. For a hypothetical array containing two finding strings separated by null, the displayed rule would retain the strings and remove null; this illustrates the source's declared rule, not a deduction from inspected runtime implementation. It neither synthesizes a new proposition nor evaluates surviving findings. Selection is computational; no human veto or factual answer oracle is part of the filter. Open audit example, not experimental comparison.

- Immediate return: truthy audit values only.
- Later read-back: inapplicable — filter acts on current-run array; replay is separate.
- Delegated visibility: foreground receives filtered return, not omitted failure slots through this channel.
- Selection predicate: JavaScript truthiness, not source warrant or task success.
- Invalidation or expiry: inapplicable — per-return list transformation, no retained filter verdict.
- Activation or effect: example selection of terminal results; not observed execution.
- Evidence limits: documented example only; no actual audit output, complete discovery or runtime implementation.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Evidence: SRC-1, `What the saved script looks like`, doctrine/design:

> An `agent()` call resolves to `null` if you stop it mid-run or it hits an unrecoverable API error. `pipeline()` keeps each `null` in the results array, which is why the example ends with `.filter(Boolean)` to drop those entries, including the slot of [an agent that stalled on every attempt](#when-an-agent-stalls-and-restarts).
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

#### EPI-RTE-checker-loop
Label: Checker loop

Requested checker → reported diagnostics → worker fixes → repeated checker until pass/no-progress stop. Owner: user requests process; Claude proposes script; computational worker/checker division and human veto during edits uninspected. Compared with [RT-RTE-agent-orchestration](runtime.md#rt-rte-agent-orchestration), distinct requested feedback route, not the generic API. Target/domain: project under selected TypeScript checker/configuration. Program diagnostics are the intended reference outcome for type-check success, not an oracle for runtime correctness. Proposed changes: external project fixes. Trigger: checker failure; admission and rollback details uninspected. Guidance: user prompt and diagnostics, with no supplied persistent rationale or formulated theory route. Mode: open user task, no comparative experiment.

- Immediate return: requested checker diagnostics/pass and eventual stop; actual return shape uninspected.
- Later read-back: uninspected — persistent fixes could affect later calls, but actual artifact/reload contract not supplied.
- Delegated visibility: requested fixer receives reported errors; exact passing of results uninspected.
- Selection predicate: failed diagnostics drive fixes; pass or two no-progress rounds stop.
- Invalidation or expiry: uninspected — no cache or diagnostic freshness policy supplied.
- Activation or effect: requests evidence-responsive task edits and repeated checking; no execution or changed artifact observed.
- Evidence limits: illustrative prompt only; no generated script, checker configuration, trace or causal benefit evidence.
- doctrine conclusion status: claimed
- implementation conclusion status: uninspected
- operation conclusion status: uninspected

Evidence: SRC-1, `Keep fixing until a check passes`, doctrine/design:

> use a workflow to run npx tsc --noEmit and keep fixing the reported errors until the type check passes or two rounds in a row make no progress
> --- `/home/zby/llm/commonplace/.commonplace/worktrees/claude-code-dynamic-workflows-f9c2f80a3a94/kb/agentic-system-analyses/state/AAS-2026-10-14-workflows-f9c2f80a3a94-01/sources/workflows-2026-10-14.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
