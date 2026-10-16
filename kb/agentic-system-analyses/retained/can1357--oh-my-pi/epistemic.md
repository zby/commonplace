---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "oh-my-pi's content, judgment and managed-skill authority routes, with bounded implementation evidence rather than a system-wide warrant verdict"
run-id: AAS-2026-10-14-oh-my-pi-c0ffc54ff768-01
reviewed-boundary: "2431e8a8716a4da73ae327a412f6d54c22f681e5"
---

# oh-my-pi epistemic report

## Source-and-claim boundary

The question is how oh-my-pi acquires or produces truth-apt content, checks it, admits it for reliance and lets it affect later behavior. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identity and layers are see [Source register](boundary.md#source-register). This remains a complete artifact, partial loop analysis, not a system-complete negative. SRC-1 supplies implementation and doctrine/design, not observed runs or causal experiments. External providers, their weights, deployed memory services and user-installed extensions have excluded implementations; target-side integrations remain included.

The supplied runtime is provisional evidence for session, tool, extension and delegation routes. Direct inspection adds automatic capture, managed-skill primitives and read-back, and the exposed eval judgment bridge. The following coverage distinguishes these bases. A directory listed as uninspected is available source, not an access gap.

| Entry point or operation | Source path, SRC-1 | Coverage and records | Remaining limit |
|---|---|---|---|
| CLI command/worker dispatch | `packages/coding-agent/src/cli.ts`; `packages/coding-agent/src/cli-commands.ts` | Direct dispatch range read and registered-command search; supplied [RT-RTE-session-turn](runtime.md#rt-rte-session-turn) | Command bodies are not all inspected. Dispatch includes non-launch operations and eval worker entry points. |
| Main session and context hooks | `packages/coding-agent/src/sdk.ts`; `packages/agent/src/agent-loop.ts` | Supplied [RT-RTE-session-turn](runtime.md#rt-rte-session-turn), [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance) | No delivered provider trace; extension replacements and provider transforms prevent assuming verbatim delivery. |
| Registered tools, approval, Cursor, speculation | `packages/coding-agent/src/tools/index.ts`; `packages/coding-agent/src/cursor.ts`; `packages/coding-agent/src/speculation/host.ts` | Registry searched directly; supplied [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch), [RT-RTE-cursor-exec](runtime.md#rt-rte-cursor-exec), [RT-RTE-speculative-read](runtime.md#rt-rte-speculative-read) | No universal semantic acceptance oracle follows from admission gates. Separate effect paths defeat a universal-wrapper claim. |
| Extension import and hooks | `packages/coding-agent/src/extensibility/extensions/loader.ts`; `packages/coding-agent/src/sdk.ts` | Supplied [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | Arbitrary installed callback semantics and import I/O unassessed. |
| Delegated outputs | `packages/coding-agent/src/task/executor.ts` | Supplied [RT-RTE-task-spawn](runtime.md#rt-rte-task-spawn) | Full structured-output finalization and downstream integration uninspected. Format is not truth. |
| Automatic capture | `packages/coding-agent/src/autolearn/controller.ts`; `packages/coding-agent/src/sdk.ts`; `packages/coding-agent/src/prompts/system/autolearn-nudge-autocontinue.md` | Direct reads, [EPI-RTE-capture-turn](#epi-rte-capture-turn) | Actual captured content, model judgment and benefit unobserved. |
| Managed-skill writes/deletion/read-back | `packages/coding-agent/src/tools/manage-skill.ts`; `packages/coding-agent/src/autolearn/managed-skills.ts`; `packages/coding-agent/src/extensibility/skills.ts` | Direct reads, [EPI-RTE-description-sanitize](#epi-rte-description-sanitize), [EPI-RTE-skill-mutation](#epi-rte-skill-mutation), [EPI-RTE-skill-readback](#epi-rte-skill-readback) | Discovery's upstream capability scan and full prompt delivery are not traced end to end. |
| Eval judge helper | `packages/coding-agent/src/eval/js/tool-bridge.ts`; `packages/coding-agent/src/eval/judgment-bridge.ts`; `packages/coding-agent/src/judgment/index.ts` | Direct reads, [EPI-RTE-eval-judgment](#epi-rte-eval-judgment) | Batch judgments, Python bridge, provider response parsers and every downstream cell consumer uninspected. |
| Memory alternatives, learn/recall and compaction | `packages/coding-agent/src/memory-backend/`; `packages/coding-agent/src/memories/`; `packages/coding-agent/src/hindsight/`; `packages/coding-agent/src/mnemopi/`; `packages/coding-agent/src/sharpshooter/`; `packages/mnemopi/`; `packages/agent/src/compaction/`; `packages/snapcompact/` | Backend startup and capture-tool resolution read in SDK; boundary establishes available alternatives | Missing write-to-recall and summarization traces prevent classification of their content relations, acceptance and source-warrant preservation. No memory member was supplied. |
| Other exposed operations/evaluators | `packages/coding-agent/src/commands/cleanse.ts`; `packages/coding-agent/src/commands/compress.ts`; `packages/coding-agent/src/commands/grievances.ts`; `packages/coding-agent/src/commands/predict.ts`; `packages/coding-agent/src/eval/judgment-batch-bridge.ts`; `packages/metaharness/`; `packages/typescript-edit-benchmark/` | Command/bridge names found in direct searches; bodies uninspected | Cannot rule out other checking, cleanup, ranking or acceptance routes. |
| Other shipped loops | `python/robomp/`; `sdk/`; `packages/collab-web/`; `packages/ai/` | Boundary inventory only | Driver, collaboration and provider-specific route closure unassessed. |

The selected claim is see [EPI-CLM-managed-library](#epi-clm-managed-library). The broader coding-agent characterization is see [RT-CLM-coding-agent](runtime.md#rt-clm-coding-agent). These are design claims, not evidence of accepted knowledge or improved capacity. No supplied execution trace licenses an observed acceptance, actual source truth, calibration or causal-benefit finding. Missing weights prevent determining provider-side parameter updates; see [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model). Missing actual candidates prevent identifying their propositions and entailment relations. No inaccessible checkout file was identified.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) | May contain factual assertions; instructions as such need not be truth-apt | see record | SRC-1, `packages/coding-agent/src/sdk.ts` | Delivery is not compliance or factual endorsement. |
| [RT-OBJ-tool-call](runtime.md#rt-obj-tool-call) | Request itself is not an assertion of successful effect; text arguments may contain claims | see record | SRC-1, `packages/agent/src/agent-loop.ts` | Schema/policy checks concern executable input. |
| [EPI-OBJ-capture-messages](#epi-obj-capture-messages) | Historical requests, model statements and tool reports; individual truths not determinable without instances | see record | SRC-1, `packages/coding-agent/src/sdk.ts` | Copies retain content but remove selected provider metadata. No independent verification. |
| [EPI-OBJ-managed-skill](#epi-obj-managed-skill) | Procedural text can assert facts or conditional effectiveness; imperatives alone are non-truth-apt | see record | SRC-1, `packages/coding-agent/src/autolearn/managed-skills.ts` | No persisted candidate supplied; instructions and factual claims cannot be classified globally as one relation. |
| [EPI-OBJ-managed-description](#epi-obj-managed-description) | Natural-language applicability statement can be truth-apt | see record | SRC-1, `packages/coding-agent/src/autolearn/managed-skills.ts` | Sanitization can alter semantic distinctions. |
| [EPI-OBJ-judgment-answers](#epi-obj-judgment-answers) | Typed model judgments over caller-supplied state/questions | see record | SRC-1, `packages/coding-agent/src/eval/judgment-bridge.ts` | Boolean probability, choice or score is not source truth or a reference outcome. |
| [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model) | Opaque distributed-parametric inference state | see record | SRC-1, `packages/agent/src/agent.ts` | Repository pin does not pin weights; hidden processing cannot establish formulated theories. |
| [EPI-CMP-judge-chain](#epi-cmp-judge-chain) | Opaque model judgments via native, prompted or local inference | see record | SRC-1, `packages/coding-agent/src/judgment/index.ts` | Each alternative has unresolved parameter mutability/version and calibration. |

## Authority-route ledger

Each ledger entry refers to its declaring record for identity and owned findings. These are implementation assessments, not reports of operation.

Route ID: [RT-RTE-session-turn](runtime.md#rt-rte-session-turn)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: supplied requests/history to model response; actual truth-apt propositions unspecified.
Evaluator/condition and domain: inference model in open coding context; no general answer oracle in supplied dispatch.
Activation and timing: see record; each admitted model step.
Possible or observed result: generated answer or tool proposal, not observed here.
Implemented force: see [RT-BAP-prompt-guidance](runtime.md#rt-bap-prompt-guidance).
Epistemic authority and scope: candidate response only; generated prose is not an evidence-consuming acceptance decision.
Operational authority: proposed next step can enter tool admission; response can reach caller.
Behavioral-authority path: model/context channel, guidance, current turn; caller reliance unresolved.
Evidence source ID and local anchor: SRC-1, `packages/agent/src/agent-loop.ts`; see record for passages.
Claim IDs or none: [RT-CLM-coding-agent](runtime.md#rt-clm-coding-agent)
Mismatch marker or none: none
Gap/limit: actual input/output is needed to decide acquisition, reshaping, entailed derivation or non-entailment. Failure to demonstrate entailment is not evidence of ampliative conjecture.

Route ID: [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [RT-OBJ-tool-call](runtime.md#rt-obj-tool-call)
Content/update relation: no content change
Transition or check target: runnable identity, schema and configured authorization of effective arguments.
Evaluator/condition and domain: code schema/policy plus human when approval requires one; domain is dispatch admissibility, not truth of patch/answer.
Activation and timing: see record; before execution, revised inputs checked again.
Possible or observed result: run, block, deny or error; no observed result supplied.
Implemented force: execution veto.
Epistemic authority and scope: grants no general semantic-correctness license.
Operational authority: permits or stops this wrapped executor invocation.
Behavioral-authority path: wrapper/core, validated request and approval channel, enforcing, invocation horizon.
Evidence source ID and local anchor: SRC-1, `packages/coding-agent/src/extensibility/extensions/wrapper.ts`; see record.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: Cursor native effects and extension imports have separate paths; see [RT-RTE-cursor-exec](runtime.md#rt-rte-cursor-exec), [RT-RTE-extension-load](runtime.md#rt-rte-extension-load). Authorization is not acceptance of truth-apt content.

Route ID: [RT-RTE-speculative-read](runtime.md#rt-rte-speculative-read)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: see record for speculative result/evidence.
Content/update relation: no content change
Transition or check target: supported local-read result's resource/evidence and current authorization at commit.
Evaluator/condition and domain: host digest/resource/policy checks, domain supported speculative reads.
Activation and timing: see record; early authorization and later commit validation.
Possible or observed result: reusable result or discard/fresh dispatch.
Implemented force: enforces eligibility to substitute speculative result.
Epistemic authority and scope: bounded identity/freshness of read evidence, not truth of file assertions.
Operational authority: changes whether this read result is delivered as authoritative completion.
Behavioral-authority path: coordinator/dispatch, validation result, enforcing, one read commit.
Evidence source ID and local anchor: SRC-1, `packages/coding-agent/src/speculation/host.ts`; see record.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: scheduler races and actual executions unobserved; no source-endorsement conclusion.

Route ID: [EPI-RTE-capture-turn](#epi-rte-capture-turn)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-capture-messages](#epi-obj-capture-messages), [EPI-OBJ-managed-skill](#epi-obj-managed-skill)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: historical context to proposed durable facts or reusable instructions.
Evaluator/condition and domain: capture model asked whether prior output will help next time; no independent reference answer.
Activation and timing: see record.
Possible or observed result: model may propose capture or do nothing; actual candidate unobserved.
Implemented force: restricted capture-agent tool roster; usefulness guidance is advisory to model.
Epistemic authority and scope: model proposes, not an established evidence-consuming acceptance of a named truth claim.
Operational authority: can request managed-skill/learn mutations but not arbitrary main-session MCP calls through fallback.
Behavioral-authority path: capture model, detached history/nudge, guidance plus restricted executable tool surface, private capture horizon.
Evidence source ID and local anchor: SRC-1, `packages/coding-agent/src/sdk.ts`.
Claim IDs or none: [EPI-CLM-managed-library](#epi-clm-managed-library)
Mismatch marker or none: none
Gap/limit: durable facts may be imported, compressed or newly inferred; proposals alone cannot establish which. Guidance requests selective capture, not measured future usefulness.

Route ID: [EPI-RTE-description-sanitize](#epi-rte-description-sanitize)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-managed-description](#epi-obj-managed-description)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: raw description to prompt-safe single-line text.
Evaluator/condition and domain: deterministic regex edits over Unicode text, not semantic evaluation.
Activation and timing: see record; on managed-description write and read.
Possible or observed result: concrete deduction `a<b` becomes `ab`; implementation evidence, not target execution.
Implemented force: changed description supplied to YAML/discovery.
Epistemic authority and scope: no license that meaning survives; the inequality interpretation can be lost.
Operational authority: controls listing text and can influence later skill selection through model interpretation.
Behavioral-authority path: serializer/loader to later prompt consumers, textual replacement, enforcing transformation and advisory downstream text, persisted-description horizon.
Evidence source ID and local anchor: SRC-1, `packages/coding-agent/src/autolearn/managed-skills.ts`.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: cannot classify every sanitized proposition as non-ampliative reshaping; actual input's meaning matters.

Route ID: [EPI-RTE-skill-mutation](#epi-rte-skill-mutation)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-managed-skill](#epi-obj-managed-skill)
Content/update relation: no content change
Transition or check target: create/update/delete request's allowed name, required fields, size, target-file constraints and authored-name collision.
Evaluator/condition and domain: deterministic tool/schema/filesystem checks; wrapped write policy as supplied runtime.
Activation and timing: see record; before and during mutation.
Possible or observed result: admission, error or authored-name refusal; no observed operation.
Implemented force: errors/refusal block operation.
Epistemic authority and scope: operational disposition only; not semantic acceptance against evidence for reuse or truth.
Operational authority: authorizes mutation of the isolated managed file/directory.
Behavioral-authority path: ManageSkillTool/filesystem primitives, schema and checks, enforcing, mutation horizon.
Evidence source ID and local anchor: SRC-1, `packages/coding-agent/src/tools/manage-skill.ts`.
Claim IDs or none: [EPI-CLM-managed-library](#epi-clm-managed-library)
Mismatch marker or none: none
Gap/limit: path/content safety checks do not judge efficacy. Human veto depends on policy, not on initiating a session.

Route ID: [EPI-RTE-skill-mutation](#epi-rte-skill-mutation)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-managed-skill](#epi-obj-managed-skill)
Content/update relation: no content change
Transition or check target: admitted proposed text to persistent SKILL.md, or deletion of directory.
Evaluator/condition and domain: see record for successful file I/O and refresh.
Activation and timing: after operational checks, same tool invocation.
Possible or observed result: stored/replaced/deleted text, or I/O error.
Implemented force: persistent file mutation and refresh request.
Epistemic authority and scope: retention of a candidate instruction artifact; lifecycle integration after epistemic acceptance is not established.
Operational authority: changes what later discovery can select.
Behavioral-authority path: managed directory and skill discovery, persisted file, permissive availability subject to selection, later sessions.
Evidence source ID and local anchor: SRC-1, `packages/coding-agent/src/autolearn/managed-skills.ts`.
Claim IDs or none: [EPI-CLM-managed-library](#epi-clm-managed-library)
Mismatch marker or none: none
Gap/limit: update truncates before writing; no general transactional rollback shown. Retention and refreshed availability do not establish accepted knowledge.

Route ID: [EPI-RTE-skill-readback](#epi-rte-skill-readback)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-managed-skill](#epi-obj-managed-skill), [EPI-OBJ-managed-description](#epi-obj-managed-description)
Content/update relation: no content change
Transition or check target: eligible managed candidate to loaded skill; selected skill body to invocation message.
Evaluator/condition and domain: deterministic enable/name/include/ignore/collision selection; human or model invocation choice remains separate.
Activation and timing: load/refresh and invocation-message construction.
Possible or observed result: candidate excluded or selected metadata/body prepared for model input.
Implemented force: enforcing discovery filters; natural-language guidance after delivery.
Epistemic authority and scope: no new endorsement of factual/procedural content.
Operational authority: makes retained instructions reachable, suppresses disabled or shadowed managed candidates.
Behavioral-authority path: skill loader and invocation builder, metadata/file text to model, selection then advisory instructions, later invocations/sessions; see record for delivery limit.
Evidence source ID and local anchor: SRC-1, `packages/coding-agent/src/extensibility/skills.ts`.
Claim IDs or none: [EPI-CLM-managed-library](#epi-clm-managed-library)
Mismatch marker or none: none
Gap/limit: deletion withdraws future file availability, not previously delivered copies or prior effects. No observed compliance/benefit.

Route ID: [EPI-RTE-eval-judgment](#epi-rte-eval-judgment)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-judgment-answers](#epi-obj-judgment-answers)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: caller-selected state assessed against caller questions, criteria and instructions; generic helper has no fixed factual domain.
Evaluator/condition and domain: live judge model chain, native/prompted/local alternatives; type validation bounds answer representation, not factual accuracy.
Activation and timing: exposed eval bridge request; see record.
Possible or observed result: typed judgments and backend label to awaiting cell, or error; no observed result.
Implemented force: data return, no universal acceptance veto attached by this helper.
Epistemic authority and scope: model assessment under supplied rubric, not an independent answer oracle or formal proof.
Operational authority: cell receives results and may branch; exact consequential cell consumer must be inspected before attributing a particular disposition.
Behavioral-authority path: eval bridge to waiting cell, typed return channel, advisory as a generic helper, current eval request; caller-specific force unresolved.
Evidence source ID and local anchor: SRC-1, `packages/coding-agent/src/eval/judgment-bridge.ts`.
Claim IDs or none: none
Mismatch marker or none: none
Gap/limit: successful type shaping, caching and retries do not establish calibration, acceptance or source truth. No generic lifecycle integration follows.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-coding-agent](runtime.md#rt-clm-coding-agent) | see record | SRC-1, `README.md`, doctrine/design | see record | [RT-RTE-session-turn](runtime.md#rt-rte-session-turn), [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch) | none supplied | No comparative quality or task-success experiment | Runtime can dispatch inference and effects; not a semantic correctness guarantee | Product superiority is not assessed. |
| [EPI-CLM-managed-library](#epi-clm-managed-library) | see record | SRC-1, `packages/coding-agent/src/prompts/system/autolearn-guidance.md`, doctrine/design | see record | [EPI-RTE-capture-turn](#epi-rte-capture-turn), [EPI-RTE-skill-mutation](#epi-rte-skill-mutation), [EPI-RTE-skill-readback](#epi-rte-skill-readback) | none supplied | Requested reuse/usefulness is not measured future benefit; actual end-to-end delivery not observed | Implemented trace-conditioned capture request, persistent managed instructions and later selection/preparation | No accepted reusable truth claim or improved capacity established. |

## Bounded conclusion

The inspected session admits outside requests/history and tools can report environment information. The supplied route does not determine source warrant for arbitrary returned assertions. A freshness check for a speculative local read licenses reuse of bounded read evidence, not endorsement of what the file says. Model outputs and capture proposals are candidates; their content relations remain indeterminate without propositions and premises. No entailed derivation from warranted premises, or actual non-entailing conjecture, is established by the generic routes alone.

Managed skills provide a concrete trace-fed behavioral path: eligible turn completion can trigger a detached capture model; managed instruction files can persist, be replaced or deleted; discovery selects eligible metadata and an invocation builder loads a selected body. This is retention and operational availability before any demonstrated epistemic acceptance. Deterministic file/schema/collision checks enforce operational admissibility, not truth or procedure efficacy. Description sanitization demonstrably need not preserve every possible meaning. Later instructions have advisory model force; successful delivery, compliance and benefit remain distinct and unobserved.

The eval judge helper checks caller-selected content against caller-selected questions, returning typed model assessments to the cell. This is a material evaluator route omitted from the supplied runtime's detailed account, not evidence of a universal oracle. Cell-specific acceptance or branching must be established separately. Candidate-chain recovery distinguishes credential/account failures, aborts and other failures; it does not criticize a factual hypothesis or establish calibration.

Capture and skill persistence afford behavior-shaping revision, including purely non-truth-apt procedural updates. They do not by themselves establish improved future capacity, exercised self-improvement, reflection or an autonomous theory builder. No formulated theory instance, content-directed criticism, resulting revision and retained criticism-driven next round was supplied or established in these selected paths. This is a local evidential limit, not a negative about all model processing or shipped mechanisms. The opaque weights of both main and judge inference remain independently unresolved.

No system-wide absence of acceptance, knowledge production or lifecycle integration is claimed: memory alternatives, compaction, batch judgment, maintenance commands and other shipped evaluators remain unassessed. The analysis supports heterogeneous implemented content and operational-authority routes, not a single epistemic score or unconditional verdict.

## Shared records

### Components

#### EPI-CMP-judge-chain
Label: Judge chain

Source-native identity: ChainJudge and its native, online TextJudge and LocalTextBackend alternatives. Representational form: symbolic routing/configuration around distributed-parametric inference; model internals are not represented by the descriptor. Storage substrate: process descriptors, provider-side state or local tiny-model worker state. Distinct from [RT-CMP-agent-model](runtime.md#rt-cmp-agent-model): role-specific routing can resolve different models; sharing an endpoint is configuration-dependent, not established identity. SRC-1, `packages/coding-agent/src/judgment/index.ts`, implementation.

For each of native, prompted online and local alternatives: parameter change during operation is uninspected; exact weights/version pin is not established by the inspected client; mutable endpoint/model resolution is possible via the live role chain. No fixed-weight or provider-side learning conclusion follows. Local model artifacts and worker internals were not inspected.

> const model = candidate.model;
> if (model.api === "local-inference") return new TextJudge(new LocalTextBackend(model.id));
> --- `packages/coding-agent/src/judgment/index.ts`

> return new TextJudge(backend);
> --- `packages/coding-agent/src/judgment/index.ts`

### Operative objects

#### EPI-OBJ-capture-messages
Label: Capture messages

Source-native identity: captureMessages passed to captureAgent.initialState. Natural-language conversation plus symbolic message/call metadata; storage substrate is a detached in-process array for a private capture agent. Consumer is capture inference, not the foreground transcript append path. Distinct from [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt): copied message history is a separate input alongside copied system instructions. SRC-1, `packages/coding-agent/src/sdk.ts`, implementation.

> if (message.role === "assistant") {
> 	return { ...message, responseId: undefined, providerPayload: undefined };
> }
> --- `packages/coding-agent/src/sdk.ts`

#### EPI-OBJ-managed-skill
Label: Managed skill

Source-native identity: isolated managed `<name>/SKILL.md`, generated from description/body with YAML frontmatter. Natural-language instruction body plus symbolic YAML fields; storage substrate is the managed-skills directory below agentDir. Consumers are skill discovery and invocation preparation, later model guidance. Different from the transient [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) and from executable extension modules in [RT-RTE-extension-load](runtime.md#rt-rte-extension-load); skill text is not imported module code. No actual authored candidate or initial provenance is supplied. SRC-1, `packages/coding-agent/src/autolearn/managed-skills.ts`, implementation.

> const content = `${toSkillFrontmatter(name, description)}\n${body}\n`;
> --- `packages/coding-agent/src/autolearn/managed-skills.ts`

#### EPI-OBJ-managed-description
Label: Managed description
Part of: [EPI-OBJ-managed-skill](#epi-obj-managed-skill)

Source-native identity: description/frontmatter.description. Natural-language applicability text, stored in YAML and selected into skill metadata. Separate assessment because write/read sanitization changes this part, whereas the body is not passed through that sanitizer. Closest supplied [RT-OBJ-system-prompt](runtime.md#rt-obj-system-prompt) is a downstream input container, not this retained field. SRC-1, `packages/coding-agent/src/autolearn/managed-skills.ts`; `packages/coding-agent/src/extensibility/skills.ts`, implementation.

> description: sanitizeManagedDescription(rawDescription),
> --- `packages/coding-agent/src/extensibility/skills.ts`

#### EPI-OBJ-judgment-answers
Label: Judgment answers

Source-native identity: EvalJudgmentResult.answers and model backend label. Symbolic typed choice/score/bool values encode natural-language question assessments; storage substrate is the returned process object, with separate judgment caching available. Consumer is awaiting eval cell. Distinct from [RT-OBJ-tool-call](runtime.md#rt-obj-tool-call): it is a helper result, not a proposed tool invocation. SRC-1, `packages/coding-agent/src/eval/judgment-bridge.ts`, implementation.

> answers[id] = answer.type === "noul" ? { type: "bool", bool: answer.noul } : answer;
> --- `packages/coding-agent/src/eval/judgment-bridge.ts`

### Routes

#### EPI-RTE-capture-turn
Label: Capture turn

Endpoints/progression: eligible session stop → controller capture callback → detached message/model snapshot → private Agent with live capture tools → model-selected calls or stop → provider-state close. Owner: AutoLearnController/SDK/private Agent. SRC-1, `packages/coding-agent/src/autolearn/controller.ts`, `packages/coding-agent/src/sdk.ts`, implementation. Distinct from [RT-RTE-session-turn](runtime.md#rt-rte-session-turn): private session/cache identity and restricted tool list, not a foreground caller prompt. Overlaps [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch) only when invoking capture tools.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: capture Promise completion or logged error; no private assistant reply appended here to foreground transcript.
- Later read-back: admitted manage_skill/learn writes may persist; managed-skill path traced separately; learn backend internals uninspected.
- Delegated visibility: private agent receives detached history and copied instructions/model; no automatic full capture transcript return to parent is implemented in this runner.
- Selection predicate: top-level installed controller, live enabled setting, tool-count threshold, non-aborted eligible stop, neither plan nor goal diversion, explicit autoContinue; runner additionally needs available capture tools/model.
- Invalidation or expiry: abort forwarded to private Agent; provider state closed and cleared in finally; live tool resolution per capture; queued pending capture can restart after completion.
- Activation or effect: asks private model to capture useful material using only manage_skill/learn; no observed mutation or benefit.
- Evidence limits: no actual capture trace; no truth oracle or measured usefulness criterion; backend-specific learn disposition uninspected.

Computational controller triggers; model proposes content and can choose no write; code constrains executable tools. Human initiation does not constitute per-content acceptance; wrapped write policy can require human approval. Guidance names repeatable procedures/durable facts and tells the model not to treat the synthetic turn as user acceptance. Operating mode is opportunistic capture from open session work, not a bounded evaluation experiment. Rejection/recovery occurs through unavailable tools, dispatch/file errors and abort; closing provider state does not roll back completed writes.

> const autoContinue = cfgAutolearnAutoContinue.get(this.#settings) === true;
> if (!autoContinue) return;
> --- `packages/coding-agent/src/autolearn/controller.ts`

> captureTools: () =>
> 	(["manage_skill", "learn"] as const)
> 		.map(name => session.getToolByName(name))
> 		.filter((tool): tool is AgentTool => tool !== undefined),
> --- `packages/coding-agent/src/sdk.ts`

> await captureAgent.prompt(captureMessage);
> --- `packages/coding-agent/src/sdk.ts`

> Automated capture turn — not a user reply; user has not responded to your previous turn. Do not treat this prompt as their answer, approval to continue, or acceptance of any pending action; only the user can do so.
> --- `packages/coding-agent/src/prompts/system/autolearn-nudge-autocontinue.md`

#### EPI-RTE-description-sanitize
Label: Description sanitize

Endpoints/progression: raw description → sanitizeManagedDescription → YAML serializer on write or selected metadata on read. Owner: managed-skills primitives/skill loader. SRC-1, `packages/coding-agent/src/autolearn/managed-skills.ts`, `packages/coding-agent/src/extensibility/skills.ts`, implementation. No counterpart after comparison with supplied [RT-RTE-session-turn](runtime.md#rt-rte-session-turn): this is persisted-field normalization, not provider-request transformation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: sanitized string.
- Later read-back: serialized description is retained with SKILL.md; discovery re-sanitizes it into metadata.
- Delegated visibility: inapplicable — no child session is created by this string function.
- Selection predicate: description supplied to serializer or loaded managed metadata.
- Invalidation or expiry: empty sanitized description is rejected by writeManagedSkill; no semantic invalidation mechanism in this sanitizer.
- Activation or effect: changes text deterministically, with downstream prompt-selection meaning interpreted by consumers.
- Evidence limits: implementation deduction only; no actual description supplied; prompt-injection safety is not assessed as a universal security guarantee.

Concrete input deduction: for ASCII `a<b`, neither letter is a control/format character; the second replacement removes `<`, leaving `ab`; subsequent tilde/whitespace edits leave it unchanged. If the input denotes a comparison, its relation operator disappears. Thus this implementation does not license universal semantic-preservation classification. It generates no separately checked derived proposition.

> return raw
> 	.replace(/[\p{Cc}\p{Cf}]/gu, " ")
> 	.replace(/[<>`]/g, "")
> 	.replace(/~{2,}/g, "~")
> 	.replace(/\s+/g, " ")
> 	.trim();
> --- `packages/coding-agent/src/autolearn/managed-skills.ts`

#### EPI-RTE-skill-mutation
Label: Skill mutation

Endpoints/progression: manage_skill params → schema/required fields/authored collision → managed primitive name/path/size/file checks → write/update/delete → refreshSkills → result. Owner: ManageSkillTool/managed-skills primitives. This route spans checking, operational disposition and retention but not established epistemic acceptance. Part of the supplied dispatch route as a material tool-specific mutation:
Part of: [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch)

SRC-1, `packages/coding-agent/src/tools/manage-skill.ts`, `packages/coding-agent/src/autolearn/managed-skills.ts`, implementation. Specific checks and persisted object differ from generic wrapper admissibility.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Created/Updated/Deleted text and details, authored-name isError refusal or thrown validation/I/O error.
- Later read-back: retained managed files can enter discovery; updates replace contents and delete removes directory; see separate read-back route.
- Delegated visibility: inapplicable — mutation tool itself creates no child; private capture may invoke it.
- Selection predicate: tool created only when autolearn enabled; valid create/update/delete parameters; allowed normalized name; non-empty sanitized description/body and byte cap; target constraints; create refuses active authored-name collision.
- Invalidation or expiry: update/delete can withdraw or replace file; symlink/hard-link and existence checks reject relevant operations; no claim-truth expiry check.
- Activation or effect: persistent managed-file mutation followed by optional refresh; no observed operation.
- Evidence limits: in-process per-name serialization, not cross-process coordination; no semantic evaluation of body; no general rollback after truncation or completed I/O.

Trigger/proposer: foreground or private capture model requests create/update/delete, shaped by managed-skill guidance and prior context. Tool code decides structural/path admission; generic policy/human veto see supplied dispatch. No expected-answer oracle. Open coding/capture mode, not an improvement experiment. What persists is candidate instruction text and description, not an acceptance record or evidence links required by this writer. User-authored same-name content is given priority. Errors can prevent a write, but deleting a file cannot erase already delivered content.

> readonly approval = "write" as const;
> --- `packages/coding-agent/src/tools/manage-skill.ts`

> if (params.action === "create" && isNameClaimedByAuthoredSkill(sanitizeSkillName(params.name))) {
> --- `packages/coding-agent/src/tools/manage-skill.ts`

> await fs.writeFile(file, content, { flag: "wx" });
> --- `packages/coding-agent/src/autolearn/managed-skills.ts`

> await handle.truncate(0);
> await handle.writeFile(content);
> --- `packages/coding-agent/src/autolearn/managed-skills.ts`

> await fs.rm(dir, { recursive: true });
> --- `packages/coding-agent/src/autolearn/managed-skills.ts`

#### EPI-RTE-skill-readback
Label: Skill readback

Endpoints/progression: discovered managed candidates → name/enable/pattern/authored-priority filters → selected skill metadata → invocation builder reads file/body → prepared invocation message. Owner: skill loader and builder. SRC-1, `packages/coding-agent/src/extensibility/skills.ts`, implementation. Distinct from [RT-RTE-session-turn](runtime.md#rt-rte-session-turn): it selects retained skill material upstream of general session/provider context; no duplicate claim about provider delivery.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: skill list with warnings, or prepared body-containing invocation message/details.
- Later read-back: reads retained managed SKILL.md on invocation; later sessions can discover files through same skill loading mechanism.
- Delegated visibility: uninspected — generic skill builder does not establish every child-session delivery path.
- Selection predicate: managed provider, valid name, not disabled, include/ignore patterns; realpath dedup and enabled authored/custom name priority; selected skill supplied to invocation builder.
- Invalidation or expiry: changed discovery settings/collisions can suppress selection; file deletion removes future read target; selected old text already in context is not recalled by these functions.
- Activation or effect: prepares metadata/body for model guidance; no observed delivery or changed model behavior.
- Evidence limits: upstream capability scan and complete invocation dispatch not inspected; no semantic check or acceptance criterion; no proven universal withdrawal from current contexts.

Code chooses eligible candidates and ordering; invocation caller chooses target skill. No answer oracle or benefit criterion. Authored content can veto managed visibility by name, not by disproving its claims. The requested reusable library is therefore an operationally selected instruction store, not automatically an accepted knowledge graph.

> if (enabledAuthoredNames.has(capSkill.name)) continue; // an enabled authored skill owns this name
> --- `packages/coding-agent/src/extensibility/skills.ts`

> if (skillMap.has(capSkill.name)) continue;
> const rawDescription =
> 	typeof capSkill.frontmatter?.description === "string" ? capSkill.frontmatter.description : "";
> --- `packages/coding-agent/src/extensibility/skills.ts`

> const content = await Bun.file(skill.filePath).text();
> --- `packages/coding-agent/src/extensibility/skills.ts`

> const body = parseFrontmatter(content, { source: skill.filePath, repair: false, level: "off" }).body.trim();
> --- `packages/coding-agent/src/extensibility/skills.ts`

#### EPI-RTE-eval-judgment
Label: Eval judgment

Endpoints/progression: JS eval synthetic judge request → runEvalJudgment validates state/questions → sessionJudge resolves live role chain → judge call → cell answer shaping/backend label → waiting cell. Owner: bridge/ChainJudge. SRC-1, `packages/coding-agent/src/eval/js/tool-bridge.ts`, `packages/coding-agent/src/eval/judgment-bridge.ts`, `packages/coding-agent/src/judgment/index.ts`, implementation. No counterpart after comparison: supplied [RT-RTE-tool-dispatch](runtime.md#rt-rte-tool-dispatch) does not individuate this side-channel evaluator or cell return.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: typed answers/model label to awaiting eval cell; invalid input, no registry/candidates or exhausted failures raise errors.
- Later read-back: native judgment wrapper can reuse model-keyed cached answers for state/questions; cache durability/key internals uninspected, not asserted cross-session knowledge.
- Delegated visibility: inapplicable — judge helper does not return a child coding-session history; it returns question answers.
- Selection predicate: reserved judge bridge name; valid non-empty state and questions; role settings/registry/credential availability; aborted signal stops work; candidate account rejection cooldown can skip models.
- Invalidation or expiry: credential/account errors cause cooldown, abort/timeouts propagate, other failures fall through chain; cache semantic freshness invalidation uninspected.
- Activation or effect: produces model assessments; request-slot release in finally; exact downstream cell branching uninspected.
- Evidence limits: actual state/questions/answers absent; calibration and truth not established; cache/provider question validation internals and bulk route uninspected.

Caller/cell proposes state, questions and rubric; parser decides admissible representation, model evaluates requested domain, chain code selects backend. No human review or independent reference answer is inherent. Operating mode is open caller-defined assessment. A successful answer has advisory data force in this generic route; no implemented mandatory disposition of a product/claim follows without a particular cell consumer. Candidate failure recovery concerns service availability, not falsification or retraction of already returned truth claims.

> if (name === EVAL_JUDGMENT_BRIDGE_NAME) {
> 	return await runEvalJudgment(args, options);
> }
> --- `packages/coding-agent/src/eval/js/tool-bridge.ts`

> return toEvalJudgmentResult(await judge.judge({ state, questions }, { signal }));
> --- `packages/coding-agent/src/eval/judgment-bridge.ts`

> } finally {
> 	evalRequestSlots.release();
> }
> --- `packages/coding-agent/src/eval/judgment-bridge.ts`

> if (isAbortOrTimeout(error)) throw error;
> const rejected = isAccountRejection(error);
> if (rejected) rejections.set(identity, Date.now() + CANDIDATE_REJECTION_COOLDOWN_MS);
> --- `packages/coding-agent/src/judgment/index.ts`

### Claims

#### EPI-CLM-managed-library
Label: Managed library

Claimed operation: build reusable managed skills and surface them in future sessions. SRC-1, `packages/coding-agent/src/prompts/system/autolearn-guidance.md`, doctrine/design. Distinct from [RT-CLM-coding-agent](runtime.md#rt-clm-coding-agent): this concerns retained procedural guidance, not general coding-agent packaging. Reuse/usefulness is requested, not demonstrated.

> `manage_skill`: build reusable managed-skill library.
> Managed skills: `SKILL.md` in isolated `~/.omp/agent/managed-skills`; surfaced in future sessions like other skills.
> --- `packages/coding-agent/src/prompts/system/autolearn-guidance.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
