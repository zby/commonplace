---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Halo epistemic routes: trace-relative computation, model diagnosis, operational completion and externally evaluated harness changes."
run-id: AAS-2026-10-14-halo-c4ed89d7f99f-01
reviewed-boundary: b7f8509745d67b499b4e80efe20ea37c03426a74
---

# Halo epistemic report

## Source-and-claim boundary

The question is how Halo turns captured executions into findings that can affect later harness behavior, and what checks license that reliance. Scope, external exclusions and source identity: see [boundary](boundary.md#boundary-and-evidence) and its [Source register](boundary.md#source-register). SRC-1 supplies implementation, doctrine/design and reported operation, not an inspected intervention comparison. The external coding actor, harness deployment and provider internals remain outside the frozen partial loop.

Knowledge and improvement claims: see [EPI-CLM-halo-loop](#epi-clm-halo-loop), [EPI-CLM-benchmark-improvement](#epi-clm-benchmark-improvement) and [RT-CLM-trace-only](runtime.md#rt-clm-trace-only). The first two are newly read source claims; the last has a source-supported capability counterexample in [RT-RTE-repository-inspection](runtime.md#rt-rte-repository-inspection). No supersession is needed: the runtime already retains that mismatch.

### Coverage

“Direct” means source text inspected for this member. “Supplied” means the runtime record supplies the mechanism and load-bearing passage. Neither means observed execution.

| Entry point or operation | Source path | Coverage and record, or remaining limit |
| --- | --- | --- |
| CLI dispatch and exposed tool factory | `pyproject.toml`, `halo_cli/main.py`, `engine/tools/subagent_tool_factory.py` | Direct registration/dispatch reads; [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis), [RT-RTE-subagent-call](runtime.md#rt-rte-subagent-call). Registered trace overview/query/count/view/search, context lookup, synthesis, optional Python, code/Git and child invocation were checked against runtime. |
| Hooks and alternate engine surfaces | `engine/`, `halo_cli/` | Scoped `hook` search found a Git-environment comment, not another analysis hook dispatcher. Supplied API convergence in [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis); this is not a claim about dependency callbacks or desktop-wide hooks. |
| Raw views, count and rendered synthesis input | `engine/traces/trace_store.py`, `engine/tools/synthesis_tool.py` | Direct consequential methods; [EPI-RTE-trace-projection](#epi-rte-trace-projection), [EPI-RTE-count-traces](#epi-rte-count-traces), [RT-RTE-trace-synthesis](runtime.md#rt-rte-trace-synthesis). Full query/filter/index validation not audited; exact counts remain conditional on their inputs and predicates. |
| Sidecar reuse/rebuild | `engine/traces/trace_index_builder.py` | Direct admission, fingerprint and parsing ranges; [EPI-RTE-index-reuse](#epi-rte-index-reuse). Full accumulator semantics uninspected. |
| Completion | `engine/tools/final_answer_tool.py` | Direct entire tool; [EPI-RTE-answer-finalization](#epi-rte-answer-finalization). Bridge fallback and consequential completion consumer supplied by [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis). |
| Context recovery and compaction | `engine/agents/agent_context.py`, `engine/tools/agent_context_tools.py`, `engine/agents/prompt_templates.py` | Direct atomic compaction admission, original-item lookup and prompts; terminal trigger and retry cleanup supplied by [RT-RTE-checkpoint-emission](runtime.md#rt-rte-checkpoint-emission) and [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis). |
| Optional repository and executable analysis | `engine/code/`, `engine/git/`, `engine/sandbox/` | Supplied [RT-RTE-repository-inspection](runtime.md#rt-rte-repository-inspection), [RT-RTE-sandbox-python](runtime.md#rt-rte-sandbox-python); direct registration check. Arbitrary model-supplied program content not individuated: its truth-apt results are not determinable in advance. |
| Desktop export, storage, report and handoff | `app/src/server/halo/exporter.ts`, `app/src/server/halo/storage.ts`, `app/src/server/halo/report.ts`, `app/src/desktop/commands.ts` | Direct export mapper; supplied [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis), [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff). Provider-specific import mappings and common upsert paths not independently audited here; no end-to-end fidelity verdict. |
| Verification and remeasurement procedure | `skills/claude/SKILL.md`, `README.md` | Direct claim and verification ranges; [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff), new claim records below. Procedure is not an executed acceptance decision. |
| AppWorld evaluation | `demo/appworld/src/appworld/evaluator.py` | Direct task evaluator and TestTracker success; [EPI-RTE-task-evaluation](#epi-rte-task-evaluation). Task-specific evaluation modules, bundled task data and full metric aggregation not inspected; benchmark completeness and reproducibility unestablished. |
| Engine smoke evaluators | `tests/e2e/test_engine_e2e.py` | Searched assertions: final flags, tool invocation, deltas and sandbox exit/output. Available definitions, not test results; no diagnosis-truth conclusion follows. Other suites and CI definitions uninspected. |
| Halo production-machinery update | `app/src/server/halo/engine.ts` | Supplied [RT-RTE-engine-install](runtime.md#rt-rte-engine-install); importability gate is distinct from diagnostic truth. |
| Source-native run artifacts and demo trace producers | `halo-telemetry-run-legacy.jsonl`, `demo/` | Artifacts/producers not traced to individual findings here; no observed acquisition, diagnosis, acceptance or benchmark causality is asserted. |

Relevant uninspected import mapping, task modules, tests and trace artifacts prevent a system-complete negative about every possible evaluator or accepted claim. Missing execution evidence prevents assertions that an implemented route operated. Missing paired interventions prevents attribution of benchmark gains to Halo, its decomposition, or a particular diagnosis. Missing provider internals prevents a parameter-learning conclusion beyond the inspected inference callers.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-span-record](#epi-obj-span-record) | Captured events, status and payload assertions | see record | SRC-1, `engine/traces/trace_store.py` | Capture truth, omitted events and import fidelity not authenticated |
| [EPI-OBJ-trace-count](#epi-obj-trace-count) | Number of indexed traces satisfying selected filters | see record | SRC-1, `engine/traces/trace_store.py` | Conditional on index and predicate semantics, not a task-success count |
| [EPI-OBJ-diagnostic-answer](#epi-obj-diagnostic-answer) | Findings about selected traces/code; possible causal hypotheses | see record | SRC-1, `engine/tools/final_answer_tool.py` | No concrete answer inspected; semantic relation remains indeterminate |
| [EPI-OBJ-synthesis-summary](#epi-obj-synthesis-summary) | Model-authored statements about rendered traces | see record | SRC-1, `engine/tools/synthesis_tool.py` | Summary and compaction are distinct consumers; this object is synthesis only |
| [EPI-OBJ-compaction-summary](#epi-obj-compaction-summary) | Claimed preservation of item facts | see record | SRC-1, `engine/agents/agent_context.py` | Successful inference does not check fidelity |
| [EPI-OBJ-test-tracker](#epi-obj-test-tracker) | Task-specific pass/fail and success proposition | see record | SRC-1, `demo/appworld/src/appworld/evaluator.py` | Does not individuate or validate Halo's causal explanations |
| [RT-CMP-root-agent](runtime.md#rt-cmp-root-agent), [RT-CMP-subagent](runtime.md#rt-cmp-subagent), [RT-CMP-synthesis-model](runtime.md#rt-cmp-synthesis-model), [RT-CMP-compaction-model](runtime.md#rt-cmp-compaction-model) | Not determinable from accessible parameters | see records | SRC-1, `engine/engine_config.py`; supplied records | Remote numerical state is not a localized inspectable proposition; inference wiring is assessable independently |

## Authority-route ledger

These are route/property assessments, not observed candidate states. Fields owned by the declaring records are cited rather than recopied. Relation classifications refer to the named edge only. In particular, an unchanged answer admitted for display has no content change even if its earlier generation was indeterminate.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-trace-projection](#epi-rte-trace-projection) | content transformation | implemented | [EPI-OBJ-span-record](#epi-obj-span-record) | truth-apt transformation: non-ampliative reshaping | Selected raw evidence to bounded view | see record | Requested tool call | Payload removal, prefix markers or metadata rendering | Enforcing selection of model-visible evidence | Preserves displayed fields, not full evidence or source truth | Narrows evidence available to inference | Calling model; tool text; informational; current invocation | SRC-1, `engine/traces/trace_store.py` | none | none | Oversized render can say spans: 0 without explaining omission |
| [EPI-RTE-count-traces](#epi-rte-count-traces) | content transformation | implemented | [EPI-OBJ-trace-count](#epi-obj-trace-count) | truth-apt transformation: entailed derivation | Cardinality of selected index rows | see record | Model-selected count call | Integer total | Informational | Cardinality under actual filter/index premises only | Supplies numerical evidence to later reasoning | Calling model; typed tool result; advisory; current analysis | SRC-1, `engine/traces/trace_store.py` | none | none | No independently warranted premises for real-world success frequency |
| [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis), [RT-RTE-subagent-call](runtime.md#rt-rte-subagent-call) | content transformation | implemented | [EPI-OBJ-diagnostic-answer](#epi-obj-diagnostic-answer) | truth-apt transformation: indeterminate | Evidence and question to diagnosis | see records | Open request and delegated calls | Candidate findings and possible hypotheses | Model-directed investigation | Candidate generation only; entailment and non-entailment not established for an unseen answer | Chooses subsequent tools or returns answer | Parent/root model; transcript/tool result; advisory; analysis episode | SRC-1, `engine/tools/subagent_tool_factory.py` | [EPI-CLM-halo-loop](#epi-clm-halo-loop) | none | Intention to generalize is not tested generalization |
| [RT-RTE-trace-synthesis](runtime.md#rt-rte-trace-synthesis) | content transformation | implemented | [EPI-OBJ-synthesis-summary](#epi-obj-synthesis-summary) | truth-apt transformation: indeterminate | Rendered traces to plain text | see record | Selected IDs/focus | Model summary | Returned without semantic gate | No acceptance or complete raw-trace warrant | Supplies compressed evidence to caller | Calling model; tool summary; advisory; analysis episode | SRC-1, `engine/tools/synthesis_tool.py` | none | none | Could reshape, derive or conjecture; actual content needed to decide |
| [EPI-RTE-answer-finalization](#epi-rte-answer-finalization) | disposition/acceptance | implemented | [EPI-OBJ-diagnostic-answer](#epi-obj-diagnostic-answer) | no content change | Terminal answer submission, not truth | see record | Root final_answer | Acknowledgement and termination | Permissive/enforcing protocol completion | No epistemic acceptance criterion | Stops root loop, exposes final answer | SDK/mapper; structured tool channel; enforcing; run termination | SRC-1, `engine/tools/final_answer_tool.py` | [EPI-CLM-halo-loop](#epi-clm-halo-loop) | none | Disposition here is operational, not evidence-consuming acceptance |
| [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis) | disposition/acceptance | implemented | [EPI-OBJ-diagnostic-answer](#epi-obj-diagnostic-answer) | no content change | Bridge answer eligible for completed state | see record | Terminal bridge selection | Final answer or last-assistant fallback | Software completion admission | Non-empty text licenses completion, not correctness | Completed answer can be retained and reported | Queue; bridge event; permissive; run/turn lifetime | SRC-1, `app/scripts/halo-local-runner.py` | none | none | Counterexample to treating completed as a truth check |
| [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis) | retention | implemented | [EPI-OBJ-diagnostic-answer](#epi-obj-diagnostic-answer) | no content change | Answer to durable turn/report | see record | Queue persistence | Retained conversation and report | Retention without per-answer human approval | No added warrant | Enables report and follow-up input | Storage/report builder; saved role/content; informational; later sessions | SRC-1, `app/src/server/halo/storage.ts` | none | none | Retention is not lifecycle integration after acceptance |
| [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis) | operational admission/selection/consumption | implemented | [EPI-OBJ-diagnostic-answer](#epi-obj-diagnostic-answer) | no content change | Earlier turns to follow-up context | see record | Later question | Prior user and non-empty assistant turns | Software context admission | Conversation continuity only | Earlier candidate findings can influence later analysis | Follow-up model; message history; advisory; later run turns | SRC-1, `app/src/server/halo/storage.ts` | none | none | Tool/child evidence is not replayed with the answer |
| [RT-RTE-checkpoint-emission](runtime.md#rt-rte-checkpoint-emission) | content transformation | implemented | [EPI-OBJ-compaction-summary](#epi-obj-compaction-summary) | truth-apt transformation: indeterminate | Original item to compressed rendering | see record | Successful root with checkpoint flag | Summaries or unchanged failed units | Context replacement on successful calls | Preservation requested, not checked | Changes potential replay context | Host checkpoint consumer; rendered messages; permissive; later resume if supplied | SRC-1, `engine/agents/agent_context.py` | none | none | Ordinary CLI/desktop does not activate this path; no inspected resume |
| [EPI-RTE-index-reuse](#epi-rte-index-reuse) | lineage/freshness/recovery | implemented | [EPI-OBJ-span-record](#epi-obj-span-record) | no content change | Index eligibility relative to source stat/schema | see record | Before analysis | Reuse or rebuild | Enforcing cache selection | Stat agreement, not source endorsement or content identity | Chooses offsets/metadata later queries use | TraceStore; sidecar rows; enforcing selection; run startup | SRC-1, `engine/traces/trace_index_builder.py` | none | none | Same-size, same-mtime content change can evade this predicate |
| [EPI-RTE-task-evaluation](#epi-rte-task-evaluation) | check/evidence production | implemented | [EPI-OBJ-test-tracker](#epi-obj-test-tracker) | truth-apt transformation: entailed derivation | Task output databases/answer against task-specific criteria | see record | Explicit evaluate_task | Pass/fail records and saved report | Reports evidence, does not automatically admit a patch | Criterion satisfaction in that task, conditional on evaluator/data fidelity | Provides outcome input to manual improvement loop | Evaluation/report reader; report and return; advisory; experiment | SRC-1, `demo/appworld/src/appworld/evaluator.py` | [EPI-CLM-benchmark-improvement](#epi-clm-benchmark-improvement) | none | Does not test the proposed failure mechanism or isolate Halo effect |
| [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff) | operational admission/selection/consumption | implemented | [EPI-OBJ-diagnostic-answer](#epi-obj-diagnostic-answer) | no content change | Report offered to coding actor | see record | User confirms tool request | Path-bearing instruction | Advisory/directive, user-gated initiation | No truth license from launch confirmation | Invites external code edits | External coding actor; report path and request; advisory; later coding session | SRC-1, `app/src/desktop/commands.ts` | [EPI-CLM-halo-loop](#epi-clm-halo-loop) | none | Actual read/edit/deployment unobserved and outside boundary |
| [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff) | disposition/acceptance | doctrine only | [EPI-OBJ-diagnostic-answer](#epi-obj-diagnostic-answer) | no content change | Verified hypothesis/edit against eval delta and error frequency | see record | Prescribed verify/edit/remeasure cycle | Ship or return to diagnosis | Procedural policy only | Bounded outcome comparison if performed; not mechanism truth | Coding actor is told to ship or revise | Coding actor; skill text; advisory; improvement rounds | SRC-1, `skills/claude/SKILL.md` | [EPI-CLM-benchmark-improvement](#epi-clm-benchmark-improvement) | none | No inspected evidence-consuming acceptance instance or integration follows |
| [RT-RTE-engine-install](runtime.md#rt-rte-engine-install) | operational admission/selection/consumption | implemented | none: machinery update | non-truth-apt policy/content update: executable engine/dependencies | Install/import success | see record | Host setup/update | Installed/error state | Admits machinery by command/import success | Importability only | Later bridge runs changed checkout | Host queue; install path; enforcing; subsequent analyses | SRC-1, `app/src/server/halo/engine.ts` | none | none | Not trace-responsive policy adaptation or evidence of better diagnosis |

Retry cleanup removes incomplete tool tails but cannot retract emitted output: see [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis). That is protocol recovery, not withdrawal of a refuted proposition. Original-item lookup returns the calling context's stored item including original content: SRC-1, `engine/tools/agent_context_tools.py`. It restores access, not warrant. Code/Git and Python routes remain separate evidence-producing possibilities: see [RT-RTE-repository-inspection](runtime.md#rt-rte-repository-inspection) and [RT-RTE-sandbox-python](runtime.md#rt-rte-sandbox-python). A successful Python exit licenses execution completion only; the program and premises determine any further truth claim.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-halo-loop](#epi-clm-halo-loop) | see record | SRC-1, `README.md`; doctrine/design | Trace diagnosis, report, external coding and redeployment loop | [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis), [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff) | None inspected | No closed-loop execution or comparison | Diagnosis and handoff are wired; external improvement is a methodology | “Recursively self-improving” cannot establish autonomous or exercised Halo self-improvement |
| [EPI-CLM-benchmark-improvement](#epi-clm-benchmark-improvement) | see record | SRC-1, `README.md`; reported operation | Skill prescribes independent verification and remeasurement | [EPI-RTE-task-evaluation](#epi-rte-task-evaluation), [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff) | No underlying paired runs inspected | Reported dev/test_normal comparison does not isolate the engine, a component or mechanism | Source reports gains and trace verification; evaluator wiring could measure task outcomes | Reported verification is not independently retained acceptance evidence in this report |
| [RT-CLM-trace-only](runtime.md#rt-clm-trace-only) | see record | SRC-1, `skills/claude/SKILL.md`; doctrine/design | Verify before acting remains sound procedural intent | [RT-RTE-repository-inspection](runtime.md#rt-rte-repository-inspection) | None inspected | Optional grants contradict blanket inability to inspect code | Trace-only applies to an ungranted configuration, not all shipped engine invocations | Capability mismatch already recorded by runtime |
| [RT-CLM-delegation-policy](runtime.md#rt-clm-delegation-policy) | see record | SRC-1, `engine/agents/prompt_templates.py`; doctrine/design | Delegate exploration and synthesize findings | [RT-RTE-subagent-call](runtime.md#rt-rte-subagent-call) | None inspected | No comparison isolating decomposition benefit | Fresh-context delegation is available | Root leaf tools remain; instruction is not enforced isolation of investigation |

## Bounded conclusion

Halo has implemented routes for importing trace evidence, exposing bounded views, computing trace-relative aggregates, generating model findings, and retaining and reusing answers. Import/source warrant is unknown: the visible desktop export retains IDs and status but remaps attributes; neither that mapping nor the trace producer authenticates the asserted events. Bounded views deliberately degrade completeness. Synthesis can lose even the explanation for omitted spans. See [EPI-RTE-trace-projection](#epi-rte-trace-projection) and [EPI-OBJ-span-record](#epi-obj-span-record).

A count is a limited entailed derivation from selected index rows, not proof of task success or an explanation of failures. Model diagnosis, synthesis and compaction are separate truth-apt generation edges whose actual preservation, entailment or ampliation cannot be classified without content. Novelty is not inferred from a model call. Final-answer acknowledgement, desktop non-empty completion and successful summary calls grant operational use, not evidence-consuming epistemic acceptance. See [EPI-RTE-count-traces](#epi-rte-count-traces), [EPI-RTE-answer-finalization](#epi-rte-answer-finalization), [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis), [RT-RTE-checkpoint-emission](runtime.md#rt-rte-checkpoint-emission).

The consequential reliance paths differ. Follow-ups admit earlier findings through role/content history without the underlying tool context. Handoff invites a separate coding actor to act on a retained report after user confirmation. The skill explicitly inserts repo verification before editing and comparative evaluation before shipping. These are meaningful proposed checks, not an observed accepted ampliative claim or lifecycle integration after acceptance. AppWorld's evaluator is a real programmatic counterexample to “only models ever evaluate anything”: its target is task-output criterion satisfaction, not Halo's causal account. Outcome success cannot establish why an edit worked or that it transfers. See [EPI-RTE-task-evaluation](#epi-rte-task-evaluation) and [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff).

The runtime's independently bounded theory-builder conditions, learning, reflection and autonomy assessments remain in [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff); nothing here upgrades them from method prescription to operation. Localized method text and available external editing do not demonstrate retained criticism shaping a next round. Model-parameter updates are not established by any inspected inference caller; provider internals remain uninspected, and this does not negate other retained-context learning paths. Engine installation changes machinery without trace-responsive evaluation. The self-improvement boundary is Halo, horizon subsequent diagnosis sessions, objective improved trace-grounded diagnosis: no inspected route establishes an evidence-shaped organizational update followed by causally dependent later operation. Reported external harness gains therefore remain independent of an exercised Halo self-improvement claim. No system-wide epistemic score or universal negative follows.

## Shared records

### Operative objects

#### EPI-OBJ-span-record
Label: SpanRecord evidence views

Source-native identity: `SpanRecord` and its bounded tool projections. Symbolic event metadata and natural-language payloads are stored in JSONL, loaded into Python records and returned as tool data. Distinct from runtime's model components; no supplied operative-object counterpart. Closest route: [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis). This object describes the acquired evidence, not the diagnosis machinery. SRC-1, `engine/traces/trace_store.py`, `app/src/server/halo/exporter.ts`. Export preserves span/trace IDs and status while adding normalized aliases; conflicting source aliases can be overwritten by later literal keys. That limits lineage fidelity, not necessarily event truth.

> "input.value": row.input ?? row.input_messages,
> "llm.model_name": row.llm_model_name,
> "llm.provider": row.llm_provider,
> "openinference.span.kind": row.observation_kind,
> "output.value": row.output ?? row.output_messages,
> --- `app/src/server/halo/exporter.ts`

#### EPI-OBJ-trace-count
Label: TraceCountResult total

Source-native identity: `TraceCountResult.total`. Symbolic integer in Python and serialized tool output; transient current-run evidence, not an accepted persistent theory. No supplied operative-object counterpart; closest route [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis). Evidence and exact derivation are in [EPI-RTE-count-traces](#epi-rte-count-traces).

#### EPI-OBJ-diagnostic-answer
Label: FinalAnswerArguments answer

Source-native identity: `FinalAnswerArguments.answer` and downstream selected answer text. Natural language carried by structured tool arguments, output messages and desktop turn/report storage. No supplied operative-object counterpart; closest routes [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis), [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis). The text may assert facts about behavior or code, but no particular answer or proposition was inspected. Evidence: SRC-1, `engine/tools/final_answer_tool.py`, plus those supplied records' persistence passages.

> answer: str
> --- `engine/tools/final_answer_tool.py:15-15`

#### EPI-OBJ-synthesis-summary
Label: SynthesizeTracesResult summary

Source-native identity: `SynthesizeTracesResult.summary`. Natural-language text held in a Python result and current-run tool history. No supplied operative-object counterpart; closest route [RT-RTE-trace-synthesis](runtime.md#rt-rte-trace-synthesis). Distinct from the remote model component and from compaction summaries: it describes selected trace renderings to the calling agent. Evidence: SRC-1, `engine/tools/synthesis_tool.py`.

> summary = (response.choices[0].message.content or "").strip()
> return SynthesizeTracesResult(summary=summary)
> --- `engine/tools/synthesis_tool.py`

#### EPI-OBJ-compaction-summary
Label: AgentContextItem compaction summary

Source-native identity: `AgentContextItem.compaction_summary`. Natural-language text in context objects, optionally rendered into a checkpoint; original fields remain locally reachable. No supplied operative-object counterpart; closest route [RT-RTE-checkpoint-emission](runtime.md#rt-rte-checkpoint-emission), whose replacement quote supplies evidence. This differs from synthesis by input, trigger and later replay consumer. SRC-1, `engine/agents/agent_context.py`. Atomic admission tests exception-free summarizer returns, not proposition preservation.

> if isinstance(result, Exception):
>     # Compaction is an optimization — a failed summarization call
>     # (after its own retries) must never take down the run, and must
>     # not partially compact a tool turn. Leave the whole unit
>     # uncompacted; the next turn's pass retries it.
> --- `engine/agents/agent_context.py`

The comment's next-turn wording does not supersede the runner's terminal-only trigger. The model instruction is a preservation request, not a checked invariant:

> You summarize a single conversation item for storage. Preserve tool names,
> argument shapes, and key result facts that future reasoning might need.
> Return a short plain-text summary — no JSON wrapping, no surrounding prose.
> --- `engine/agents/prompt_templates.py`

#### EPI-OBJ-test-tracker
Label: TestTracker evaluation results

Source-native identity: AppWorld `TestTracker` passes/failures, `success` and report. Symbolic criteria/results plus natural-language report, in Python and optionally disk Markdown. No supplied operative-object counterpart; closest [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff) prescribes outcome measurement but does not declare this evaluator object. SRC-1, `demo/appworld/src/appworld/evaluator.py`; route passage below supplies invocation evidence.

> @property
> def success(self) -> bool:
>     return self.pass_count == self.num_tests
> --- `demo/appworld/src/appworld/evaluator.py`

### Routes

#### EPI-RTE-trace-projection
Label: Bounded trace projection

Part of: [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis)

The container's diagnostic route includes tool-driven evidence access; this part owns deterministic projection only. Code transforms selected parsed spans into bounded records or rendered metadata for the calling model/synthesis. SRC-1, `engine/traces/trace_store.py`. The view's lossy projection changes available evidence, not acceptance. For concrete input `abcdef` with cap 3, the string branch returns `abc... [HALO truncated: original 6 chars]`. This source deduction requires no target execution. It retains the prefix and explicitly removes `def`; it cannot support an inference about omitted content. `render_trace` further selects metadata, excluding payload assertions regardless of cap.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Bounded span fields, omission marker or metadata text.
- Later read-back: inapplicable — this projection does not persist changed material; downstream context/report routes own retention.
- Delegated visibility: Calling agent receives its requested view; synthesis receives rendered metadata rather than full raw payloads.
- Selection predicate: Trace/span IDs, attribute caps, noisy-key predicate, total response budget and rendering field whitelist.
- Invalidation or expiry: Fresh projection from current store per request; no epistemic withdrawal state.
- Activation or effect: Code limits model-visible evidence; model reliance and output effects unobserved.
- Evidence limits: No authenticated source truth or completeness follows; oversized omission is consequential to synthesis.

> return f"{value[:cap_chars]}... [HALO truncated: original {len(value)} chars]"
> --- `engine/traces/trace_store.py`

> view = self.view_trace(trace_id)
> lines: list[str] = [f"trace_id: {trace_id}", f"spans: {len(view.spans)}"]
> --- `engine/traces/trace_store.py`

The oversized empty-span witness is supplied by [RT-RTE-trace-synthesis](runtime.md#rt-rte-trace-synthesis). Together these passages establish that an oversized view renders `spans: 0`, not the original span count or its omission explanation.

#### EPI-RTE-count-traces
Label: Indexed trace count

Part of: [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis)

This is the deterministic count-tool part, not the container's model inference. The calling model proposes filters; code chooses matching rows and returns their length. The target/domain is indexed rows satisfying the implemented predicate, not successful real-world tasks. Open diagnostic mode; no expected-answer oracle. The model can revise filters or disregard the count; no human approval or acceptance gate intervenes. SRC-1, `engine/traces/trace_store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: TraceCountResult with integer total.
- Later read-back: inapplicable — count tool does not write retained material; ordinary current-run delivery alone is not read-back.
- Delegated visibility: Root and children have this leaf tool; result is visible only in the requesting context unless relayed.
- Selection predicate: Caller filters passed to _apply_filters.
- Invalidation or expiry: Recomputed on request over the loaded index.
- Activation or effect: Supplies a numerical proposition for interpretation, not automatic candidate acceptance.
- Evidence limits: Full filter and accumulator semantics not audited here; premises conditional. A count of two selected rows yields total 2 by len, not a new empirical generalization.

> return TraceCountResult(total=len(self._apply_filters(filters)))
> --- `engine/traces/trace_store.py`

#### EPI-RTE-answer-finalization
Label: Root answer acknowledgement

Part of: [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis)

This part is the terminal tool's acknowledgement, not answer generation. Root model proposes final text; software accepts the structured submission and SDK stop policy terminates. Target/domain is protocol completion, with no evidence-consuming truth test or answer oracle. Open diagnostic mode. Human can cancel/reject outside this acknowledgement but does not approve each answer before emission. The tool deliberately discards arguments; correction or rollback of a proposition is not implemented by this function. SRC-1, `engine/tools/final_answer_tool.py`; downstream mapping/stop and fallback are supplied by [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis) and [RT-RTE-desktop-analysis](runtime.md#rt-rte-desktop-analysis).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: FinalAnswerResult acknowledgement.
- Later read-back: inapplicable — acknowledgement does not persist or replay content; desktop route owns that path.
- Delegated visibility: Root-only tool; children return plain messages.
- Selection predicate: Root final_answer dispatch with structured answer argument.
- Invalidation or expiry: Stops current root run; no truth-retraction or expiry rule.
- Activation or effect: Ends analysis and exposes answer to downstream consumers.
- Evidence limits: Final flag and acknowledgement establish no correctness, completeness or acceptance against an epistemic criterion.

> del tool_context, arguments
> return FinalAnswerResult()
> --- `engine/tools/final_answer_tool.py`

#### EPI-RTE-index-reuse
Label: Sidecar freshness admission

Part of: [RT-RTE-trace-diagnosis](runtime.md#rt-rte-trace-diagnosis)

Startup code admits a derived index or rebuilds it. The target is source/index stat-and-schema compatibility, not the truth of trace claims. Software decides; no content proposal or human per-index approval. This is recovery/selection of derived data, not knowledge acceptance. SRC-1, `engine/traces/trace_index_builder.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Reused or rebuilt index path.
- Later read-back: Subsequent runs can select the sidecar if source size, mtime and schema still agree.
- Delegated visibility: Root/children query the common store built from admitted rows, not freshness metadata as an epistemic endorsement.
- Selection predicate: Both files exist and metadata schema_version, source_size and source_mtime_ns match current inputs.
- Invalidation or expiry: Predicate mismatch triggers rebuild; source mutation preserving size/mtime is not detected by this predicate. Invalid metadata parsing can raise rather than silently rebuild.
- Activation or effect: Selects offsets and derived metadata for subsequent evidence queries; actual execution unobserved.
- Evidence limits: Not a cryptographic content check, capture authentication or approval; complete accumulator and concurrent mutation behavior uninspected.

> if index_path.exists() and meta_path.exists():
>     existing = TraceIndexMeta.model_validate_json(meta_path.read_text())
>     if (
>         existing.schema_version == config.schema_version
>         and existing.source_size == current_size
>         and existing.source_mtime_ns == current_mtime_ns
>     ):
>         return index_path
> --- `engine/traces/trace_index_builder.py`

#### EPI-RTE-task-evaluation
Label: AppWorld task evaluation

No supplied route counterpart after comparison: [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff) prescribes remeasurement, while this distinct shipped program evaluates task outputs and returns a tracker. It is not a material part of that desktop handoff. The evaluator loads a named task, its start state and saved task-output databases, then calls the task ground-truth evaluation module with public/private data and expected answer. Target/domain: task-specific assertions over those outputs. Reference provider: bundled task ground truth; encoding fidelity and task-specific evaluator completeness remain uninspected. Caller chooses task/experiment, code invokes evaluation, task module judges criteria; no universal Halo diagnosis oracle. This supports bounded experiments, not automatic patch admission. SRC-1, `demo/appworld/src/appworld/evaluator.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: TestTracker of passes/failures; optional saved report and version file.
- Later read-back: Saved report is available to an experimenter; no inspected automatic patch-selection consumer reads it. The skill prescribes evaluation comparison separately.
- Delegated visibility: Evaluation module receives reference data, main_user, model collection pair and ground_truth_answer, not a Halo diagnosis transcript.
- Selection predicate: Named task/experiment and task ground-truth evaluation module; db_version mismatch rejects evaluation startup.
- Invalidation or expiry: Re-evaluation reads selected outputs; saved reports can be rewritten. No harness-patch rollback is implemented by this evaluator.
- Activation or effect: Produces criterion-relative outcome evidence. A shipping decision remains a separate prescribed external operation, not force implemented here.
- Evidence limits: Specific task modules and metric aggregation not inspected; success cannot validate diagnosis mechanism, counterfactual benefit or transfer.

> evaluation_module.evaluate(
>     test=test_tracker,
>     public_data=ground_truth.public_data,
>     private_data=ground_truth.private_data,
>     main_user=main_user,
>     models=models,
>     ground_truth_answer=ground_truth.answer,
> )
> --- `demo/appworld/src/appworld/evaluator.py`

### Claims

#### EPI-CLM-halo-loop
Label: Recursive harness improvement methodology

Claimed operation: trace analysis produces common-failure findings for external coding and repeated deployment. SRC-1, `README.md`, doctrine/design. Distinct from [RT-CLM-trace-only](runtime.md#rt-clm-trace-only) and [RT-CLM-delegation-policy](runtime.md#rt-clm-delegation-policy): those concern tool grants/policy, not the advertised improvement loop. Closest implemented route: [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff).

> HALO is a methodology for building recursively self-improving agent harnesses using [RLMs](https://github.com/alexzhang13/rlm). This repository contains:
> --- `README.md`

> 3. The engine decomposes the traces to understand common failure modes across harness executions and produces a report with its findings.
> 4. This report is fed into a coding agent like Cursor or Claude Code to generate and apply a set of changes to your harness.
> 5. The harness is then re-deployed, more traces are gathered, and the cycle repeats.
> --- `README.md`

#### EPI-CLM-benchmark-improvement
Label: Reported benchmark and verification gains

Claimed operation/warrant: harness-only improvements, source-trace verification and held-out split comparison. SRC-1, `README.md`, reported operation; statements are attributed, not independently observed. No supplied claim counterpart; closest [RT-RTE-report-handoff](runtime.md#rt-rte-report-handoff) describes the prescribed procedure rather than these result claims.

> HALO is consistently capable of driving improvements on benchmarks, solely by optimizing the harness.
> --- `README.md`

> The feedback from HALO Engine surfaced failures in the harnesses such as hallucinated tool calls, redundant arguments in tools, refusal loops, and semantic correctness issues. Each issue mapped cleanly to a direct prompt edit. HALO’s claims were independently verified from the source trace files with the findings holding up under scrutiny.
> --- `README.md`

> The peak improvements over baseline were substantial for both models. For Gemini 3 Flash, dev SGC went from 36.8% to 52.6% (+15.8 points) and test_normal SGC went from 37.5% to 48.2% (+10.7 points). For Sonnet 4.6, dev SGC went from 73.7% to 89.5% (+15.8 points) and test_normal SGC went from 62.5% to 73.2% (+10.7 points).
> --- `README.md`
