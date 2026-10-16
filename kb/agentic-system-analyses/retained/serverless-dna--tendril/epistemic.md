---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Tendril epistemic routes: capability claims, live-data acquisition, execution checks and later reliance."
run-id: AAS-2026-10-15-tendril-f560fb299a37-01
reviewed-boundary: "e671a4143d28de68289efd81580002041bb4cb6a"
---

# Tendril epistemic report

## Source-and-claim boundary

This assesses whether Tendril's retained tools and execution feedback warrant later reliance, including the claims that sessions become smarter and tools should supply live information. Functional scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity is see its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed runs or causal experiments. The shipped desktop, sidecar and writable workspace are included. External SDK internals, model services/weights, Deno internals and arbitrary fetched packages are outside the frozen implementation boundary.

The material routes are model production of capability descriptions and programs, disk admission and replacement, model selection from summaries, program execution and result delivery, requested repair, and alternate human/program writes. Transport is assessed only where omission or status labels could change reliance. Developer CI is distinguished from candidate-tool evaluation. No supplied candidate corpus individuates actual generated propositions; executable content and results may be truth-apt, policy-only or mixed. That uncertainty does not prevent assessing their operational force.

Knowledge/warrant claims are see [EPI-CLM-session-smarter](#epi-clm-session-smarter), [EPI-CLM-live-data](#epi-clm-live-data), and [RT-CLM-action-sequence](runtime.md#rt-clm-action-sequence). README examples are doctrine, not traces. Its historical `searchCapabilities`/`loadTool` examples do not match the frozen three-callback API; current registration and execution follow the implementation, not those examples.

### Material entry-point coverage

Paths below are SRC-1 commit-relative anchors. Direct reads were made for the paths explicitly marked direct; supplied coverage is not presented as an independent read. No new source identity is introduced.

| Entry point or operation | Source path | Coverage records or bounded exclusion |
|---|---|---|
| Sidecar positional workspace argument; startup and user text extraction | `tendril-agent/src/index.ts` | Direct; [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream), [EPI-RTE-model-production](#epi-rte-model-production). Only last message/first usable text block is forwarded. |
| JSON-RPC initialize, new_session, prompt, cancellation and unknown-method rejection | `tendril-agent/src/transport/protocol.ts` | Direct; [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream). No extra evaluator or maintenance dispatch is registered here. |
| Agent construction, provider alternatives, tools/hooks | `tendril-agent/src/agent.ts` | Direct; [RT-CMP-bedrock-model](runtime.md#rt-cmp-bedrock-model), [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model), [RT-CMP-anthropic-model](runtime.md#rt-cmp-anthropic-model), [RT-CMP-ollama-model](runtime.md#rt-cmp-ollama-model), [EPI-RTE-model-production](#epi-rte-model-production). Constructor supplies three callbacks, no evaluator hook. SDK-internal hooks remain uninspected. |
| listCapabilities, registerCapability, execute | `tendril-agent/src/loop/tools.ts`; `tendril-agent/src/loop/registry.ts` | Direct complete files; [EPI-RTE-summary-projection](#epi-rte-summary-projection), [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission), [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution). |
| Live information and failure repair instructions | `tendril-agent/src/loop/prompt.ts` | Direct; [EPI-CLM-live-data](#epi-clm-live-data), [EPI-RTE-failure-repair](#epi-rte-failure-repair). |
| Deno result/error, timeout, cancellation, output cap and finally cleanup | `tendril-agent/src/loop/sandbox.ts` | Direct; [EPI-RTE-execution-check](#epi-rte-execution-check), [EPI-RTE-result-disposition](#epi-rte-result-disposition). |
| Tool-result and completion presentation | `tendril-agent/src/transport/stream.ts`; `tendril-agent/src/index.ts` | Direct; [EPI-RTE-display-result](#epi-rte-display-result), [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream). |
| All exposed Tauri command registrations | `tendril-ui/src-tauri/src/lib.rs` | Direct. send/cancel/connect/restart; workspace init; config read/write; file list/read/write/reveal; capability/source/prompt reads. Relevant routes covered below; directory sorting and reveal helpers do not endorse claims. |
| Workspace editor, capability browser, source and prompt display | `tendril-ui/src-tauri/src/files.rs`; `tendril-ui/src-tauri/src/capabilities.rs`; `tendril-ui/src/components/CapabilityBrowser.tsx`; `tendril-ui/src/components/FileExplorer.tsx` | First three direct complete reads; editor save-handler direct bounded read. [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation), [EPI-OBJ-capability](#epi-obj-capability), [EPI-OBJ-tool-code](#epi-obj-tool-code). Browser source editor is read-only; file editor is a distinct write route. |
| Workspace init, config validation/restart, process recovery, desktop result consumer | `tendril-ui/src-tauri/src/workspace.rs`; `tendril-ui/src-tauri/src/config.rs`; `tendril-ui/src-tauri/src/acp.rs`; `tendril-agent/src/config.ts`; `tendril-ui/src/context/AgentContext.tsx` | Supplied findings only: [RT-RTE-settings-restart](runtime.md#rt-rte-settings-restart), [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation), [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream). Not an independent audit of every config-validation branch. |
| Product-development quality gate | `.github/workflows/quality-gate.yml`; `Makefile`; `tendril-agent/tests/registry.test.ts`; `tendril-agent/tests/sandbox.test.ts` | Workflow and tests direct complete reads; Makefile quality targets direct. [EPI-RTE-development-check](#epi-rte-development-check). Other test bodies remain uninspected except supplied integration findings; no inference of full test adequacy or passing results. |
| Public self-extension account | `README.md` | Direct complete read; [EPI-CLM-session-smarter](#epi-clm-session-smarter). Historical specs/docs not comprehensively inspected: prevents an exhaustive inventory of historical warrant claims, not analysis of the registered runtime callbacks. |

No workspace, provider trace, persisted capability instance or measured comparison was supplied. These respectively prevent identifying actual program propositions, observed criticism/acceptance, and longitudinal/causal improvement. External model opacity prevents conclusions about internal parametric learning, not the visible file-mediated authority path. Available uninspected documentation and dependency internals are not evidence of absence. No system-complete negative about every possible evaluator embedded in generated programs follows: arbitrary code could implement tests, proofs, measurements or human consultation.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) | Mainly non-truth-apt instructions; no task-specific accepted claim | see record | SRC-1, `tendril-agent/src/loop/prompt.ts` | Delivery is not compliance; display copy is not active instruction. |
| [EPI-OBJ-capability](#epi-obj-capability) | Natural-language claim about what a tool does | see record | SRC-1, `tendril-agent/src/loop/registry.ts` | Description is not checked against code or outcomes. |
| [EPI-OBJ-triggers-suppression](#epi-obj-triggers-suppression) | Primarily invocation policy, not factual endorsement | see record | SRC-1, `tendril-agent/src/loop/tools.ts` | Model interprets conditions; no fixed semantic veto. |
| [EPI-OBJ-tool-code](#epi-obj-tool-code) | Not determinable for actual generated content; program may encode assertions, derivations or only actions | see record | SRC-1, `tendril-agent/src/loop/sandbox.ts` | No supplied corpus; code execution alone does not establish theory production. |
| [EPI-OBJ-tool-output](#epi-obj-tool-output) | Not determinable without a result instance; may report external facts or measurements | see record | SRC-1, `tendril-agent/src/loop/sandbox.ts` | stdout is arbitrary program-controlled text. Source warrant unknown. |
| [EPI-OBJ-agent-text](#epi-obj-agent-text) | Not determinable without model output; potential task-answer propositions | see record | SRC-1, `tendril-agent/src/transport/stream.ts` | Fluent text and delivery supply no acceptance decision. |
| [RT-CMP-bedrock-model](runtime.md#rt-cmp-bedrock-model), [RT-CMP-openai-model](runtime.md#rt-cmp-openai-model), [RT-CMP-anthropic-model](runtime.md#rt-cmp-anthropic-model), [RT-CMP-ollama-model](runtime.md#rt-cmp-ollama-model) | Distributed-parametric alternatives; truth-apt units not individuated from available sources | see records | SRC-1, `tendril-agent/src/agent.ts` | Exact weights unpinned, mutable endpoint resolution possible, provider-internal updates uninspected; no Tendril weight-update API wired. |

## Authority-route ledger

Each row isolates a consequential function. Shared-record-owned fields are referred to rather than recopied. Architectural status belongs to this overlay; implementation and operation statuses remain separate in the declaring records. Imported source warrant is unknown unless an actual tool result supplies provenance and a check.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-model-production](#epi-rte-model-production) | content transformation | implemented | [EPI-OBJ-capability](#epi-obj-capability), [EPI-OBJ-tool-code](#epi-obj-tool-code), [EPI-OBJ-agent-text](#epi-obj-agent-text) | truth-apt transformation: indeterminate | User/tool context to proposed descriptions, code or answers | see record | see record | see record | Model proposal/text; callback execution separate | Candidate production only; no warranted ampliative or entailed claim established | Can request writes/execution without per-candidate human approval | see record | SRC-1, `tendril-agent/src/agent.ts` | [EPI-CLM-session-smarter](#epi-clm-session-smarter) | none | No actual inputs/outputs or internal model reasoning. |
| [EPI-RTE-summary-projection](#epi-rte-summary-projection) | content transformation | implemented | [EPI-OBJ-capability](#epi-obj-capability), [EPI-OBJ-triggers-suppression](#epi-obj-triggers-suppression) | truth-apt transformation: non-ampliative reshaping | Stored index to selection summary | see record | see record | see record | No truth check | Preserves description text; omits attribution/date/version and code | Makes summaries available for selection | see record | SRC-1, `tendril-agent/src/loop/registry.ts` | [RT-CLM-action-sequence](runtime.md#rt-clm-action-sequence) | none | Metadata may not describe current file. |
| [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) | check/evidence production | implemented | [EPI-OBJ-capability](#epi-obj-capability), [EPI-OBJ-tool-code](#epi-obj-tool-code) | no content change | Registration shape/name | see record | see record | see record | Syntactic rejection, not semantic evaluation | Name/shape license only | Malformed name blocks registration; SDK schema contract applies | see record | SRC-1, `tendril-agent/src/loop/tools.ts`; `tendril-agent/src/loop/registry.ts` | none | none | Does not test description, code type correctness or outcome. |
| [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) | disposition/acceptance | implemented | [EPI-OBJ-tool-code](#epi-obj-tool-code), [EPI-OBJ-capability](#epi-obj-capability) | non-truth-apt policy/content update: admit or replace executable program and selection metadata | Proposed definition/code to writable store | see record | see record | see record | Automatic operational admission | Not evidence-consuming epistemic acceptance | Registration permits later loading and summary delivery | see record | SRC-1, `tendril-agent/src/loop/registry.ts` | [EPI-CLM-session-smarter](#epi-clm-session-smarter) | admission-not-acceptance | No content approval, semantic veto or prior-version rollback. |
| [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission) | retention | implemented | [EPI-OBJ-tool-code](#epi-obj-tool-code), [EPI-OBJ-capability](#epi-obj-capability) | no content change | Admitted bytes to later disk reads | see record | see record | see record | Persistent availability until replacement | Retention does not license truth | Later selection/execution can use current files | see record | SRC-1, `tendril-agent/src/loop/registry.ts` | [EPI-CLM-session-smarter](#epi-clm-session-smarter) | none | Index saved before source; no atomic content/evidence lineage. |
| [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution) | operational admission/selection/consumption | implemented | [EPI-OBJ-tool-code](#epi-obj-tool-code), [EPI-OBJ-triggers-suppression](#epi-obj-triggers-suppression) | no content change | Selected name/args to Deno execution | see record | see record | see record | Executable source within configured grants | No endorsement of description or results | Can read/write workspace and fetch network data | see [RT-BAP-capability-source](runtime.md#rt-bap-capability-source) | SRC-1, `tendril-agent/src/loop/tools.ts`; `tendril-agent/src/loop/sandbox.ts` | [RT-CLM-action-sequence](runtime.md#rt-clm-action-sequence), [EPI-CLM-live-data](#epi-clm-live-data) | index-membership-not-required | Valid-named file can run without index entry. |
| [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution) | content transformation | implemented | [EPI-OBJ-tool-output](#epi-obj-tool-output) | truth-apt transformation: acquisition/import | External/local observations to tool data | Program-specific; generic callback does not authenticate source | On code choosing fetch/read; not observed | Potential external facts; unknown warrant | Program result enters tool channel | Acquisition capacity, not certified live truth | Model may answer or act on returned data | see record | SRC-1, `tendril-agent/src/loop/prompt.ts`; `tendril-agent/src/loop/sandbox.ts` | [EPI-CLM-live-data](#epi-clm-live-data) | freshness-not-endorsement | Actual code may cache, omit provenance or fabricate; no supplied acquired instance. |
| [EPI-RTE-execution-check](#epi-rte-execution-check) | check/evidence production | implemented | [EPI-OBJ-tool-code](#epi-obj-tool-code), [EPI-OBJ-tool-output](#epi-obj-tool-output) | no content change | Subprocess liveness, resource envelope, termination status | see record | see record | see record | Produces runtime signals | Exit status licenses only a process-status inference within Node/Deno contract | Signals feed resolution/rejection and possible repair | see record | SRC-1, `tendril-agent/src/loop/sandbox.ts` | [EPI-CLM-live-data](#epi-clm-live-data) | exit-not-answer-oracle | No reference outcome or factual test. |
| [EPI-RTE-result-disposition](#epi-rte-result-disposition) | disposition/acceptance | implemented | [EPI-OBJ-tool-output](#epi-obj-tool-output) | truth-apt transformation: non-ampliative reshaping | Runtime signals to resolved text or error | see record | see record | see record | Resolves/rejects callback; can kill process | No epistemic acceptance of stdout | Successful stdout becomes available; failures withhold normal return | see record | SRC-1, `tendril-agent/src/loop/sandbox.ts` | none | none | Successful stderr omitted; previous effects not rolled back. |
| [EPI-RTE-display-result](#epi-rte-display-result) | operational admission/selection/consumption | implemented | [EPI-OBJ-tool-output](#epi-obj-tool-output), [EPI-OBJ-agent-text](#epi-obj-agent-text) | no content change | Model text and tool result to desktop presentation | see record | see record | see record | Presentation only | `completed` and `end_turn` are not validity certificates | UI receives result/text/completion | see record | SRC-1, `tendril-agent/src/transport/stream.ts`; `tendril-agent/src/index.ts` | none | completion-not-acceptance | SDK result visibility to model is external contract, not established by UI label. |
| [EPI-RTE-failure-repair](#epi-rte-failure-repair) | behavior/policy adaptation | doctrine only | [EPI-OBJ-tool-code](#epi-obj-tool-code) | non-truth-apt policy/content update: requested program repair | Failure to corrective replacement and retry | see record | see record | see record | Advisory request; writing/execution affordance implemented separately | No checked diagnosis or accepted explanation | If followed, new source changes later execution | see record | SRC-1, `tendril-agent/src/loop/prompt.ts` | [EPI-CLM-session-smarter](#epi-clm-session-smarter) | requested-not-observed | Request is delivered by implemented prompt; compliance and evaluation quality unobserved. |
| [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation) | disposition/acceptance | implemented | [EPI-OBJ-tool-code](#epi-obj-tool-code), [EPI-OBJ-capability](#epi-obj-capability) | non-truth-apt policy/content update: human-editor replacement | Human-chosen content to file write | see record | see record | see record | UI confirmation plus backend path gate | Confirmation is not evidence-consuming truth acceptance | Human may replace code/index; future loads use changed bytes | see record | SRC-1, `tendril-ui/src/components/FileExplorer.tsx`; `tendril-ui/src-tauri/src/files.rs` | none | none | Generic backend has no confirmation or semantic gate. |
| [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation) | behavior/policy adaptation | implemented | [EPI-OBJ-tool-code](#epi-obj-tool-code), [EPI-OBJ-capability](#epi-obj-capability) | non-truth-apt policy/content update: executable workspace mutation | Running program to later source/index | see record | see record | see record | Workspace write grant | No required evaluation of mutation | Can bypass registration bookkeeping and change future behavior | see [RT-BAP-capability-source](runtime.md#rt-bap-capability-source) | SRC-1, `tendril-agent/src/loop/sandbox.ts` | [EPI-CLM-session-smarter](#epi-clm-session-smarter) | none | Capacity only; particular write and benefit unobserved. |
| [RT-RTE-settings-restart](runtime.md#rt-rte-settings-restart) | behavior/policy adaptation | implemented | Provider and sandbox configuration; see record | non-truth-apt policy/content update: human settings change | Saved config to reconstructed agent | see record | see record | see record | Schema admission and restart | No task-answer warrant | Changes model/permissions/timeouts; rebuilds process | see record | SRC-1, `tendril-ui/src/App.tsx`; `tendril-agent/src/config.ts` | none | none | Supplied findings; not evidence-responsive autonomous improvement. |
| [EPI-RTE-development-check](#epi-rte-development-check) | check/evidence production | implemented | Product source/tests, not newly generated capabilities | no content change | Repository checks and selected fixture expectations | see record | see record | see record | CI dependency and local quality targets | Bounded implementation-property tests, not factual tool-answer license | CI build-check waits for check job; local release depends on check | see record | SRC-1, `.github/workflows/quality-gate.yml`; `Makefile` | none | developer-gate-not-runtime-gate | No passing result; no installed runtime capability gate. |

No lifecycle-integration route after evidence-consuming acceptance was found in the inspected constructor, three callbacks, registry and sandbox. They do connect retained files to operational use, but do not record an accepted truth claim, evidence, criterion, intended use and scope. This is a bounded finding about these implementations, not a prohibition on a generated capability implementing its own evaluation/integration procedure.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-session-smarter](#epi-clm-session-smarter) | see record | SRC-1, `README.md`, doctrine/design | Persistent reuse and autonomous construction declared | [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission), [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution), [EPI-RTE-failure-repair](#epi-rte-failure-repair) | None supplied | No intervention, baseline, corpus or later-use trace; replacement can degrade or break a tool | Available executable repertoire can change across sessions | Neither monotonic improvement nor every-session improvement established. |
| [EPI-CLM-live-data](#epi-clm-live-data) | see record | SRC-1, `tendril-agent/src/loop/prompt.ts`, doctrine/design | Prefers live tool information and requests repair | [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution), [EPI-RTE-execution-check](#epi-rte-execution-check), [EPI-RTE-result-disposition](#epi-rte-result-disposition) | None supplied | No correctness/freshness comparison; exit status is not an answer oracle | Acquisition and runtime-feedback paths exist | Actual content provenance, freshness and truth unknown. |
| [RT-CLM-action-sequence](runtime.md#rt-clm-action-sequence) | see record | SRC-1, `tendril-agent/src/loop/prompt.ts`, doctrine/design | Explicit list/match/create/execute policy | [EPI-RTE-summary-projection](#epi-rte-summary-projection), [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission), [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution) | None supplied | No compliance or independent benefit comparison | Model receives policy and necessary tools | Sequencing/matching not enforced; source without index can execute. |

## Bounded conclusion

Tendril retains descriptions, invocation policy and executable TypeScript. Listing reshapes index metadata for model selection; execution reads current source by name and gives it consequential workspace/network authority. These are operational reliance paths, not evidence-consuming acceptance of the description or program's claims. Registration's syntactic check, source-file availability and process exit each license a different narrow conclusion. None licenses factual correctness of stdout. See [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission), [EPI-RTE-summary-projection](#epi-rte-summary-projection), [EPI-RTE-execution-check](#epi-rte-execution-check) and [RT-BAP-capability-source](runtime.md#rt-bap-capability-source).

The system can acquire local/remote facts through programs. Warrant is unknown at that generic edge: code controls what is fetched, transformed and printed, and the wrapper retains no obligatory source-evidence binding. Deterministic summary projection preserves selected wording while dropping attribution fields; stdout trimming can remove whitespace, and successful stderr is omitted. Neither is a new entailed proposition or factual check. The concrete implementation deductions and counter-cases are see [EPI-RTE-summary-projection](#epi-rte-summary-projection) and [EPI-RTE-result-disposition](#epi-rte-result-disposition). No actual model-produced accepted ampliative claim, checked entailed derivation from warranted premises, or post-acceptance integration is established by the supplied evidence.

Failures can produce operative process errors and kill the current process. They do not withdraw a capability, restore its previous version or undo completed side effects. Repair is requested, not independently observed. Human edits and executable workspace writes can change the same future behavior without an epistemic acceptance decision. The browser permits inspection, but there is no required human review before model registration/execution. See [EPI-RTE-failure-repair](#epi-rte-failure-repair), [EPI-RTE-result-disposition](#epi-rte-result-disposition), and [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation).

The smarter-session claim exceeds demonstrated warrant. Retained executable changes can shape future behavior without changing model weights. That supports a self-extension architecture; it does not establish learning as improved future capacity. A potential failure-responsive repair pathway has a live authority channel, but no trace establishes evidence shaping a particular update or subsequent operation causally depending on it. Exercised self-improvement and its success therefore remain unestablished over the cross-session horizon. Reflection, formulated-theory criticism and autonomous theory-building are separately unestablished, not disproved: no supplied generated contents identify a theory, a content-directed criticism, or a retained criticism shaping another round. Autonomous callback writes do not establish all those internal roles. Provider-internal learning and reasoning remain uninspected, independently of these file-mediated findings.

## Shared records

### Operative objects

#### EPI-OBJ-capability
Label: capability

Part of: [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission)

The natural-language `capability` field states what the tool does. It is stored inside symbolic JSON in workspace `tools/index.json`, then delivered as a textual description to the model and human browser. This object is the description part of the admission route, not a duplicate of its write mechanism or [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt). SRC-1, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/registry.ts`, `tendril-ui/src/components/CapabilityBrowser.tsx`.

> capability: z.string().describe('One-sentence description of what the tool does'),
> --- `tendril-agent/src/loop/tools.ts`

#### EPI-OBJ-triggers-suppression
Label: triggers and suppression

Part of: [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission)

Natural-language invocation policy stored in the same index and projected to model-visible summaries. The arrays are symbolic containers; their conditions have model/human-interpreted force, not executable trigger matching. Unlike [EPI-OBJ-capability](#epi-obj-capability), these primarily direct selection rather than describe tool behavior. Parent is the route that admits this operative part. SRC-1, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/prompt.ts`.

> triggers: z.array(z.string()).describe('2-5 conversational signals for invocation'),
>         suppression: z.array(z.string()).describe('Conditions that prevent invocation'),
> --- `tendril-agent/src/loop/tools.ts`

#### EPI-OBJ-tool-code
Label: code

Symbolic TypeScript retained as workspace `tools/{name}.ts`; Node later loads it and Deno executes it in a temporary script. This is the operative source object connecting [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission), [RT-RTE-workspace-mutation](runtime.md#rt-rte-workspace-mutation) and [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution), not a duplicate route. It spans these routes, so it is not a part of exactly one. Comments or strings inside actual code might carry natural-language propositions; no actual corpus is supplied. Model attribution in an index does not certify that later bytes are still model-produced. Evidence and behavioral channel are see [RT-BAP-capability-source](runtime.md#rt-bap-capability-source). SRC-1, `tendril-agent/src/loop/registry.ts`, `tendril-agent/src/loop/sandbox.ts`.

#### EPI-OBJ-tool-output
Label: stdout

Part of: [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution)

Program-controlled stdout is a transient UTF-8 string held in Node process memory and returned through the tool callback. It may encode natural-language facts, symbolic JSON or non-truth-apt output; no particular result is supplied. stderr and process status are distinct check signals, not the same truth-apt candidate. Evidence is see [EPI-RTE-result-disposition](#epi-rte-result-disposition). SRC-1, `tendril-agent/src/loop/sandbox.ts`.

#### EPI-OBJ-agent-text
Label: agent_message_chunk

Part of: [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream)

Natural-language text deltas produced by the model, transformed into symbolic session updates and displayed in the desktop's in-memory transcript. This is the answer-content part, not the protocol or the retained capability source. Truth-apt propositions cannot be individuated without an output instance. SRC-1, `tendril-agent/src/transport/stream.ts`; desktop storage is see [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream).

> sessionUpdate: 'agent_message_chunk',
>     text,
>     content: { type: 'text', text },
> --- `tendril-agent/src/transport/stream.ts`

### Routes

#### EPI-RTE-model-production
Label: Model candidate production

Part of: [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: model text deltas or tool requests through the SDK stream.
- Later read-back: inapplicable — this generation part does not itself retain content; registration is separately declared.
- Delegated visibility: configured provider/SDK receives shipped instruction, extracted user text and SDK-managed tool context; exact serialization and history are uninspected.
- Selection predicate: model chooses text/tool calls under the system prompt; no reference answer or candidate comparator is supplied by the constructor.
- Invalidation or expiry: current stream finishes or is canceled; no semantic retraction channel is defined here.
- Activation or effect: generated registration requests can propose code/metadata; generated text reaches presentation; actual generated content and activation unobserved.
- Evidence limits: implementation wires inference; no corpus or model trace establishes semantic preservation, entailment or non-entailment for a particular output.

This isolates candidate production within the supplied transport/iteration container. Human supplies an open request; model proposes, SDK orchestrates, callbacks decide mechanical admission. There is no per-candidate human veto in the inspected constructor/callback wiring. The content/update relation remains indeterminate, rather than inferring conjecture merely from lack of an entailment proof. Natural-language model output has advisory/instructional force at selection and can request executable writes; the actual execution grant belongs to callbacks and Deno. SRC-1, `tendril-agent/src/agent.ts`, `tendril-agent/src/index.ts`, `tendril-agent/src/loop/tools.ts`.

> for await (const event of agent.stream(userText)) {
> --- `tendril-agent/src/index.ts`

The exact callback set and instruction delivery are already evidenced in [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) and [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream).

#### EPI-RTE-summary-projection
Label: Capability summary projection

Part of: [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: JSON-formatted list of projected selection fields, or an empty-registry instruction from the tool wrapper.
- Later read-back: list reloads current index at each request; retained descriptions/policies can reach later model invocations across sessions.
- Delegated visibility: model receives name, capability, triggers and suppression, not source or created/created_by/version/tool_path.
- Selection predicate: list returns all index entries; the model makes semantic selection, not this projection code.
- Invalidation or expiry: overwrite changes next read; malformed/missing index can become empty under loadIndex; no expiry.
- Activation or effect: summary data becomes available for foreground model selection; actual selection or compliance unobserved.
- Evidence limits: projection preserves chosen field values, not their truth or binding to current source; no observed invocation supplied.

This is the read-back transformation part of the admission container, not a duplicate of registration. Concrete deduction from SRC-1, `tendril-agent/src/loop/registry.ts`: an entry with name `fetch_url`, capability `Fetches a URL and returns text content`, its two policy arrays and created_by `model` becomes a four-field summary. The capability sentence and arrays remain unchanged; created_by is absent. No new proposition follows; attribution context is degraded even though wording is preserved. The test source uses the same sample description and asserts the omitted fields; it is corroborating intended behavior, not a passing result (`tendril-agent/tests/registry.test.ts`).

> return index.capabilities.map(({ name, capability, triggers, suppression }) => ({
>       name,
>       capability,
>       triggers,
>       suppression,
>     }));
> --- `tendril-agent/src/loop/registry.ts`

There is no evidence-consuming acceptance of the description. Model decides applicability from summaries; human need not approve the chosen tool. This operates on open requests, without an answer oracle. The malformed-index fallback can hide entries while leaving executable source intact; the source-only load counter-case is see [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution).

#### EPI-RTE-execution-check
Label: Subprocess execution check

Part of: [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: close/error events, output-byte count, timer or abort signal feed settlement logic.
- Later read-back: inapplicable — these transient signals are not persisted as an evaluation ledger by this checker.
- Delegated visibility: Node receives stdout/stderr and process events; no independent critic is called.
- Selection predicate: every executeDeno invocation installs process event handlers, timeout and optional cancellation listener.
- Invalidation or expiry: handlers settle one promise; timeout cleared on close/error and cancel listener removed on close.
- Activation or effect: signals determine normal result, rejection or kill; actual runtime checks unobserved.
- Evidence limits: Deno/OS event semantics are external contracts; no trace or deployment test supplied.

The target is process completion and resource-envelope compliance, not correctness of user-domain claims. Node code evaluates exit status, elapsed deadline and combined output bytes. Model-selected program and args are the tested candidate; humans supply tasks but no expected-answer oracle. The distinct result consumer is [EPI-RTE-result-disposition](#epi-rte-result-disposition). SRC-1, `tendril-agent/src/loop/sandbox.ts`.

> proc.stdout.on('data', (d: Buffer) => {
>         outputBytes += d.length;
>         if (outputBytes > MAX_OUTPUT_BYTES) {
> --- `tendril-agent/src/loop/sandbox.ts`

> const timeout = setTimeout(() => {
>         proc.kill('SIGKILL');
>         if (!settled) { settled = true; reject(new Error(`Execution timeout after ${timeoutMs}ms`)); }
>       }, timeoutMs);
> --- `tendril-agent/src/loop/sandbox.ts`

Both stdout and stderr handlers count against the same output cap; the quoted handler is the stdout branch.

#### EPI-RTE-result-disposition
Label: Execution result disposition

Part of: [RT-RTE-capability-execution](runtime.md#rt-rte-capability-execution)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: zero exit resolves trimmed stdout or `(no output)`; nonzero/spawn/timeout/output-limit/cancellation rejects with an error.
- Later read-back: inapplicable — this disposition does not itself persist output or change stored source.
- Delegated visibility: resolved text/error goes to the SDK tool channel; exact SDK packaging is uninspected. Successful stderr is not returned by this wrapper.
- Selection predicate: zero exit and no earlier settlement admits normal output; contrary process signals select rejection.
- Invalidation or expiry: promise settles once; finally attempts temp-file deletion. No automatic stored-tool withdrawal or old-source restoration.
- Activation or effect: normal output may be consumed by model; errors may prompt repair. Killing a process does not undo prior workspace writes/network effects.
- Evidence limits: no observed output, correction or rollback trace; exit status does not certify factual accuracy.

This is disposition within the execution container, distinct from checking. It is operational result admission, not epistemic acceptance. Node decides via a process criterion; there is no human or semantic veto on zero-exit content. In the open-request mode no expected answer is supplied. SRC-1, `tendril-agent/src/loop/sandbox.ts`.

> if (exitCode === 0) resolve(stdout.trim() || '(no output)');
>         else reject(new Error(stderr.trim() || `Exit code ${exitCode}`));
> --- `tendril-agent/src/loop/sandbox.ts`

> await fs.unlink(tmpFile);
> --- `tendril-agent/src/loop/sandbox.ts`

Concrete source deductions, not executions: stdout `  false\n` with exit zero becomes `false`, regardless of whether the proposition is false; empty/whitespace stdout becomes `(no output)`; stdout `42` and stderr `warning` with exit zero return only `42`. The trimming is non-ampliative reshaping; the placeholder is a program status string. None checks truth. A program that prints an incorrect answer and exits zero is a source-supported counter-case to a generic correctness oracle. Finally cleanup targets the temp script, not the retained capability or its side effects.

#### EPI-RTE-display-result
Label: Stream result presentation

Part of: [RT-RTE-prompt-stream](runtime.md#rt-rte-prompt-stream)

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: session updates carrying text, tool output, errors and completion for desktop display.
- Later read-back: inapplicable — this adapter does not persist an accepted-claim ledger or replay transcript.
- Delegated visibility: desktop receives selected result content/result/text, serializing nonstring output; model-facing SDK handling is a separate uninspected dependency.
- Selection predicate: recognized model text delta/toolResultEvent; duplicate afterToolCallEvent and unknown events ignored.
- Invalidation or expiry: turn completion stops streaming; no truth-based retraction or withdrawal of earlier text.
- Activation or effect: UI labels a returned tool event completed; entry point emits end_turn even after catching an error. Actual display operation unobserved.
- Evidence limits: completion status cannot establish callback success semantics, factual correctness or model acceptance.

This separates the presentation part of the supplied stream route. Its consumer is the desktop via session/update, its force is presentation, and its horizon is the current in-memory transcript. SRC-1, `tendril-agent/src/transport/stream.ts`, `tendril-agent/src/index.ts`. Errors and terminal completion are not mutually exclusive; this is not an outcome oracle.

> const rawOutput = result.content ?? result.result ?? result.text ?? '';
> --- `tendril-agent/src/transport/stream.ts`

> status: 'completed',
>     rawOutput: typeof rawOutput === 'string' ? rawOutput : JSON.stringify(rawOutput),
> --- `tendril-agent/src/transport/stream.ts`

#### EPI-RTE-failure-repair
Label: Failure repair instruction

Part of: [RT-RTE-capability-admission](runtime.md#rt-rte-capability-admission)

- implementation conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: inapplicable — the repair rule is instruction, not a separate automatic repair callback.
- Later read-back: if followed, replacement source is reloaded on later execute calls; no separate retained diagnosis or evidence ledger is required.
- Delegated visibility: foreground model receives repair instruction through the system prompt and may receive SDK tool errors; no separate critic is wired in the inspected constructor.
- Selection predicate: instruction says repair on failure; compliance and diagnosis are model-dependent.
- Invalidation or expiry: same-name registration overwrites source/definition; no versioned rollback. Shipped instruction reconstructed at restart.
- Activation or effect: a requested repair can change future executable behavior via registration, but no repaired candidate or subsequent use was supplied.
- Evidence limits: instruction delivery is wired; the repair route itself is doctrine-only, not observed criticism, successful learning or causal improvement.

This is the repair-request part of the registration container; [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance) owns delivery of the general policy. Model proposes/decides revised code, Node admits schema/name-valid writes, human has no per-repair approval step. Expected-answer oracle absent in the inspected generic callback; a particular generated tool might implement one. Operating mode is open user requests; failure is the improvement trigger, intended objective is successful task execution, and source/metadata persist across sessions. No actual formulated theory or content-directed criticism is available to assess conditions 1–4. SRC-1, `tendril-agent/src/loop/prompt.ts`, `tendril-agent/src/loop/tools.ts`, `tendril-agent/src/loop/registry.ts`.

> - On failure: fix the code and retry. Do not fall back to memory.
> --- `tendril-agent/src/loop/prompt.ts`

#### EPI-RTE-development-check
Label: Development quality gate

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: format/type/lint/test commands can return success/failure; no execution result supplied.
- Later read-back: inapplicable — this gate does not admit workspace capability contents or install evaluation memories in the agent.
- Delegated visibility: CI/local developer receives command results; no result channel from this gate to runtime tool registration is wired in inspected source.
- Selection predicate: workflow push/PR triggers repository quality job; local make check invokes prerequisites. CI build-check requires check job; local make release depends on check and ui-build.
- Invalidation or expiry: rerun evaluates changed repository; no runtime tool withdrawal or rollback follows from this gate.
- Activation or effect: a failed check blocks the workflow's dependent build-check; local commands propagate prerequisite failure. Actual passing/blocking outcome unobserved.
- Evidence limits: selected tests are fixture assertions, not general proof; sandbox tests can skip without Deno. Other test bodies and release workflow not comprehensively assessed.

No counterpart after comparison with supplied runtime routes: this is the product-development check, not capability admission. Targets are repository formatting/type/lint checks and fixture assertions about implementation behavior. Evaluators are deterministic compiler/linter/test tools plus source-authored expectations; expected outputs are developer supplied, not user-task answer oracles. SRC-1, `Makefile`, `.github/workflows/quality-gate.yml`, `tendril-agent/tests/registry.test.ts`, `tendril-agent/tests/sandbox.test.ts`.

> check: fmt lint test
> --- `Makefile`

> needs: check
> --- `.github/workflows/quality-gate.yml`

> expect(result).toBe('hello world');
> --- `tendril-agent/tests/sandbox.test.ts`

The literal-output test checks that one simple program returns the expected text, not that arbitrary generated programs answer correctly. It is evaluator source, not an observed passing result. This is a counter-case to an unqualified claim that Tendril has no checks at all, while leaving the missing runtime semantic admission gate intact.

### Claims

#### EPI-CLM-session-smarter
Label: Smarter sessions

README claims autonomous cross-session construction/reuse and improvement with every session. This distinct claim concerns longitudinal benefit, unlike the action-sequencing claim [RT-CLM-action-sequence](runtime.md#rt-clm-action-sequence). SRC-1, `README.md`, doctrine/design.

> The registry grows with use. Every session is smarter than the last.
> --- `README.md`

Persistence/reload is implemented, but the strong improvement claim has no supplied execution or comparison support. Same-name replacement, corrupt-index fallback and permissive workspace mutation are relevant counter-routes; growth is not invariant and does not establish improved task capacity.

#### EPI-CLM-live-data
Label: Live data preference

The shipped instruction demands tool-acquired live information rather than memory where possible. It is a consequential reliance policy, not an explicit infallibility claim. Distinct from [RT-CLM-action-sequence](runtime.md#rt-clm-action-sequence): it addresses answer sourcing, not tool-call order. SRC-1, `tendril-agent/src/loop/prompt.ts`, doctrine/design.

> - Never answer from memory when a tool can get live data.
> --- `tendril-agent/src/loop/prompt.ts`

> - Return ONLY the data the user needs — filter and reshape before logging.
> --- `tendril-agent/src/loop/prompt.ts`

Fetching and reshaping are possible under the execution grant. Neither instruction guarantees freshness, semantic preservation, source reliability or retained evidence provenance; those depend on actual code and observations.
