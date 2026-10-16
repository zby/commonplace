---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Archie epistemic routes: operational profile authority versus planned documentation warrant."
run-id: AAS-2026-10-15-archie-1ab3d8b8ff03-01
reviewed-boundary: 76caf94548cf76f2399d9a7446da15e0daa22685
---

# Archie epistemic report

## Source-and-claim boundary

The question is whether Archie's agent-launch profiles acquire, produce, check or accept truth-apt content, and how their results affect later behavior. Scope and exclusions are as in [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register). This is a runtime-client subsystem, not the external agent loop or the whole desktop distribution. The assistant plan is design context, not an implemented evaluator.

Direct inspection used SRC-1 at the frozen revision: the complete profile module, shell command loader, Python CLI, assistant epic and agent-backed work item, plus the profile-reference section. The searches below covered operation names, hooks, tools, acceptance, rejection, rollback, provenance and confidence in those files. Deployment, shell initialization and override behavior are supplied runtime findings, not fresh source reads. No source was executed. There are no supplied traces, candidate answers, evaluation results or causal comparisons.

| Entry point or operation | Source path | Coverage and records | Limit / conclusion prevented |
| --- | --- | --- | --- |
| Seven profiles, four aliases, direct helper call | `deployment-packages/local/lib/zsh/commands-agents.sh` | Direct complete read; [RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch), [RT-RTE-default-update](runtime.md#rt-rte-default-update) | External CLI semantics and model outputs uninspected |
| Shell load and deployment | `deployment-packages/local/lib/zsh/commands.sh`, `deployment-packages/home/.zshrc`, `scripts/install.sh` | Loader read directly; remaining chain supplied by [RT-RTE-shell-load](runtime.md#rt-rte-shell-load) | No installed-environment evidence |
| Direct invocation and overrides | `deployment-packages/home/.zshrc` | Supplied [RT-RTE-direct-handoff](runtime.md#rt-rte-direct-handoff) | Prevents universal profile-gate claims |
| Python CLI dispatch | `src/archie/cli.py` | Direct complete read; registers applet, downgrade, GUI and system groups, not an agent operation | Desktop implementations excluded; no whole-system negative follows |
| Documented profile guarantees | `deployment-packages/local/lib/zsh/README.md` | Direct profile-section read; [EPI-CLM-profile-contract](#epi-clm-profile-contract) | Documentation differs from executable selectors |
| Documentation guidance, provenance, confidence and fallback | `docs/epics/assistant.md`, `docs/work-items/assistant-03-agent-backed-documentation-guide.md` | Direct complete reads; [RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide) | Planned; no candidate, check algorithm or consumer implementation |
| External tools, hooks, model evaluation and context management | External `omp` and providers | Opaque dependencies; [RT-CMP-model-services](runtime.md#rt-cmp-model-services) | No external implementation or traces; cannot judge their epistemic routes |

There is no knowledge-production guarantee in the inspected launcher. The consequential claims are the operational profile contract and the planned documentation guide cited above. Missing external runtime/provider sources prevent attribution of any internal acquisition, inference, evaluation, acceptance or tool restriction to Archie. Missing executions prevent claims of exercised authority or benefit. Missing candidate content prevents classification of any actual answer as imported, entailed or conjectural; answer content is **not determinable**. Excluded contributor workflows and unrelated desktop maintenance cannot support conclusions about this subsystem's knowledge production.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [RT-OBJ-model-roles](runtime.md#rt-obj-model-roles) | None established; symbolic role configuration, not a proposition accepted as true | see cited record | SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh` | Getter origin and durable backend opaque; existing fields are not evidence claims merely because they persist |
| [RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch) | No truth-apt candidate in preset model/effort flags; forwarded caller input may contain one | see cited record | SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh` | Flags are symbolic controls. No actual caller payload or downstream answer is supplied |
| [RT-CMP-model-services](runtime.md#rt-cmp-model-services) | Not determinable within accessible service state | see cited record | SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh` | Service computation may produce truth-apt content, but no model state or output is inspected; per-selector mutability and version limits remain in cited record |
| [RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide) | Intended documentation/architecture explanations; no candidate instance supplied | see cited record | SRC-1, `docs/work-items/assistant-03-agent-backed-documentation-guide.md` | Design-only context and provenance requirements; no operative answer object or evidence attachment |

## Authority-route ledger

Rows separate the functions performed by existing records; they do not allocate duplicate route identities. Fields owned by those records are incorporated by citation. Architectural statuses and content relations below are this report's assessment.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-default-update](runtime.md#rt-rte-default-update) | content transformation | implemented | [RT-OBJ-model-roles](runtime.md#rt-obj-model-roles) | non-truth-apt policy/content update: replace default selector | Current JSON to updated configuration | Symbolic jq assignment; ordinary JSON object domain | see route | see route | see route | No factual warrant conferred | see route | see [RT-BAP-role-arguments](runtime.md#rt-bap-role-arguments) | SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh` | [EPI-CLM-profile-contract](#epi-clm-profile-contract) | Conditional preservation, not universal durability | Direct helper calls also afforded; no target execution |
| [RT-RTE-default-update](runtime.md#rt-rte-default-update) | retention | implemented | [RT-OBJ-model-roles](runtime.md#rt-obj-model-roles) | no content change | Transformed value to config setter | Setter return status; backend opaque | see route | see route | see route | Retention is not acceptance of a proposition | see route | see [RT-BAP-role-arguments](runtime.md#rt-bap-role-arguments) | SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh` | [EPI-CLM-profile-contract](#epi-clm-profile-contract) | Persistence requested, not observed | No read-back verification, lock, history or compensating restore in helper |
| [RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch) | operational admission/selection/consumption | implemented | [RT-OBJ-model-roles](runtime.md#rt-obj-model-roles) | no content change | Helper completion to process launch | Nonzero helper return stops profile; shell status domain, not answer truth or provider readiness | see route | see route | see route | None for generated claims | see route | see [RT-BAP-role-arguments](runtime.md#rt-bap-role-arguments) | SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh` | [EPI-CLM-profile-contract](#epi-clm-profile-contract) | Gate is operational, not epistemic acceptance | Pipeline status need not expose every getter failure; no schema/read-back check |
| [RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch) | behavior/policy adaptation | implemented | [RT-OBJ-model-roles](runtime.md#rt-obj-model-roles) | non-truth-apt policy/content update: fixed role selection | Invoked function to runtime role request | Caller chooses preset; no evidence-responsive ranking or answer oracle | see route | see route | see route | Model names confer no answer warrant | see route | see [RT-BAP-role-arguments](runtime.md#rt-bap-role-arguments) | SRC-1, `deployment-packages/local/lib/zsh/commands-agents.sh` | none | none | Appended arguments and external parser bound effective selection; not evaluation-driven adaptation |
| [RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide) | other — intended documentation guidance and provenance presentation | doctrine only | see claim | truth-apt transformation: indeterminate | Intended documentation/context to explanation | No named answer evaluator or acceptance criterion implemented in inspected subsystem | Planned, optional mode | Intended constrained guidance; no observed answer | No implemented assistant force found in inspected profile/dispatch paths | No established license for factual reliance | None established for assistant restrictions | Intended assistant-to-user guidance, advisory; implementation and horizon undecided | SRC-1, `docs/work-items/assistant-03-agent-backed-documentation-guide.md` | [RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide) | Plan must not be transferred to launcher | No candidate to distinguish import, reshaping, derivation or conjecture |

For the deterministic transformation, consider the hypothetical ordinary object `{"default":"old","plan":"keep"}` and helper argument `openai-codex/gpt-6-luna:medium`. The inspected `.default = $default` expression yields `{"default":"openai-codex/gpt-6-luna:medium","plan":"keep"}` modulo JSON serialization. The whole resulting value goes to the setter. This is an implementation-layer deduction, not a target execution or an entailed new factual proposition. It supports preservation of non-default keys in the transform's domain, not source truth, durable atomicity or protection from concurrent whole-object writes. The minimum implementation passage is supplied by [RT-RTE-default-update](runtime.md#rt-rte-default-update).

The strongest countercase to a purely passive-launcher account is that it changes configuration before launch and later helper invocations request that value again. Hence operational retention and authority are real implemented requests, even though factual acceptance is not established. Conversely, setter success followed by launch failure does not restore the previous selector. Direct invocation bypasses the profile gate. These cases, supported by the same helper and [RT-RTE-direct-handoff](runtime.md#rt-rte-direct-handoff), prevent treating status gating as an answer validator or a universal runtime safety policy.

No wrapper answer check, rejection, withdrawal, cleanup of accepted claims or post-acceptance lifecycle integration was found in the complete profile module. This is a bounded inspection finding, not an absence finding about external `omp`. The only inspected failure disposition is shell return-status handling, whose target is command continuation rather than a truth-apt candidate. The planned provenance requirement is not itself an evaluator:

> - Define how the assistant should present provenance, confidence, and fallback
>   behavior when the agent response goes beyond the local docs.
> --- `docs/work-items/assistant-03-agent-backed-documentation-guide.md`

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-profile-contract](#epi-clm-profile-contract) | see claim | SRC-1, `deployment-packages/local/lib/zsh/README.md`; doctrine/design | see claim | [RT-RTE-default-update](runtime.md#rt-rte-default-update), [RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch) | None supplied | No comparison; external storage and parser required | Source supports conditional JSON preservation and forwarding, not unconditional durable preservation | Some documented GPT selectors differ from code; failures/concurrency bound preservation |
| [RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide) | see claim | SRC-1, `docs/epics/assistant.md`, `docs/work-items/assistant-03-agent-backed-documentation-guide.md`; doctrine/design | see claim; provenance/confidence/fallback remain tasks to define | No implemented assistant route established; profile launch is not the planned guide | None supplied | No comparison, acceptance procedure or implemented restriction in inspected mechanism | A planned constrained documentation mode, not exercised factual evaluation | No implementation/operation support for assistant warrant; plan is explicitly future-facing, not a failed deployed guarantee |

## Bounded conclusion

Archie implements operational model-role selection and a configuration retention request, not an inspected truth-apt acceptance pipeline. The fixed default update, helper-status gate and CLI presets affect the external runtime through symbolic arguments and config-setting calls; their scope, consumer and horizons are in [RT-BAP-role-arguments](runtime.md#rt-bap-role-arguments). They confer no evidence-based authority on any answer. Their actual activation remains unobserved.

No truth-apt acquisition with preserved source warrant, accepted ampliative claim, checked entailment or post-acceptance integration is established in the selected shell mechanism. External caller input, model state and generated answers remain uninspected, not presumed non-truth-apt. Thus neither a system-wide negative nor a positive knowledge-production conclusion follows. The concrete JSON deduction concerns control configuration only.

The assistant's documentation corpus, contextual guidance, provenance and confidence presentation remain planned. Without an answer instance and evidence-consuming decision against a criterion for an intended use and scope, there is no basis to classify its future outputs as accepted knowledge. Presentation of provenance would not by itself establish source truth or acceptance. The plan and source-level configuration effects therefore retain separate statuses.

The profile path changes behavior requests without evaluated content: it is fixed caller-selected adaptation, not evidence of learning, reflection, autonomous theory building or self-improvement. External model processing and any parameter changes are independently uninspected as recorded in [RT-CMP-model-services](runtime.md#rt-cmp-model-services); symbolic selector changes do not establish weight updates. Missing executions also prevent benefit or causal attribution. None of these limits erases the implemented configuration path or implies a single epistemic verdict for Archie and its dependencies.

## Shared records

### Claims

#### EPI-CLM-profile-contract
Label: Persistent profile configuration contract

The profile reference claims that functions persist their default, preserve non-default roles and forward appended arguments. This is an operational contract, not a knowledge-production claim. SRC-1, `deployment-packages/local/lib/zsh/README.md`, doctrine/design:

> Persistent `omp:*` profile functions set their own default model role before starting `omp`; they preserve configured non-default roles and forward appended arguments. Shorthand aliases delegate to the corresponding profile function.
> --- `deployment-packages/local/lib/zsh/README.md`

The closest supplied claim, [RT-CLM-assistant-guide](runtime.md#rt-clm-assistant-guide), concerns a distinct planned assistant mode. This claim instead concerns the deployed shell-profile contract implemented by [RT-RTE-default-update](runtime.md#rt-rte-default-update) and [RT-RTE-profile-launch](runtime.md#rt-rte-profile-launch); those routes supply the implementation quotations. No duplicate claim counterpart was found in the supplied runtime declarations. The universal preservation reading is limited to ordinary input shape, external storage success and absence of conflicting concurrent writes. This record does not assert an actual persisted instance or a new epistemic evaluator.
