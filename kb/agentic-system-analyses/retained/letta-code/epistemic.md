---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Letta Code epistemic routes: retained claims, memory admission, compaction, human reflection selection and bounded mod evaluation."
run-id: AAS-2026-10-12-letta-code-be76afeab9b7-01
reviewed-boundary: "271f119dcf37d58649a18e6c733386b3c710a456"
---

# Letta Code epistemic report

## Source-and-claim boundary

The question is how Letta Code makes conversational content available for later reliance, which checks license that reliance, and whether its learning claims have evidence-consuming successors. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identities and evidence layers are see [Source register](boundary.md#source-register). All added source inspection below is SRC-1 at the frozen revision, implementation unless identified as doctrine/design. There are no observed runs or causal experiments. The runtime is a supplied provisional trace, not an inspection ceiling.

Truth-apt objects include conversational assertions, remembered facts and claimed procedures, summaries of past events, and propositions about a candidate mod's behavior. A permission grant licenses an action, not an answer's truth. Git merge success licenses a state transition, not the semantics of the merged facts. The public learning claim is [EPI-CLM-long-horizons](#epi-clm-long-horizons). No single truth criterion follows from that claim.

| Entry point or operation | Source path and inspection basis | Covering records or remaining limit |
|---|---|---|
| CLI dispatch, memory maintenance, servers and exports | Direct full read: SRC-1 `src/cli/subcommands/router.ts`; direct restore range and action search: `src/cli/subcommands/memory.ts`; supplied startup trace | [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn); [EPI-RTE-memory-restore](#epi-rte-memory-restore). Pull/export/backup are inventoried, not traced end to end; no complete lineage guarantee. |
| Provider turns, client tools, Task, schedules, hosted service | Supplied runtime: SRC-1 `src/headless.ts`, `src/tools/manager.ts`, `src/agent/subagents/manager.ts`, `src/cron/scheduler.ts`, `src/backend/backend.ts` | [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn), [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task), [RT-RTE-scheduled-prompt](runtime.md#rt-rte-scheduled-prompt). Tool-result warrant depends on tool and environment; external server/provider implementation unavailable. |
| Registered Memory tool and result shaping | Direct ranges: SRC-1 `src/tools/impl/memory.ts`; registry filter search in `src/tools/manager.ts` | [EPI-RTE-memory-fetch](#epi-rte-memory-fetch). Remaining built-in tools and arbitrary MCP/SDK tool evaluators unassessed; no system-complete negative about checking. |
| Hooks and mod policy | Direct sequential-hook range: SRC-1 `src/hooks/executor.ts`; direct consumer range: `src/tools/manager.ts`; supplied mod trace | [EPI-RTE-hook-policy](#epi-rte-hook-policy), [RT-RTE-extension-load](runtime.md#rt-rte-extension-load). Installed hook content unavailable; parallel/post-tool feedback and shipped example hooks not traced to all consumers. |
| Memory commit validation and publication audit | Direct full function: SRC-1 `src/memory-frontmatter.ts`; hook range `src/agent/memory-git-hooks.ts`; audit range `src/agent/memory-constraints-audit.ts` | [EPI-RTE-frontmatter-check](#epi-rte-frontmatter-check), [EPI-RTE-commit-admission](#epi-rte-commit-admission). Constraint validator implementation and every synchronization caller not fully inspected; no universal validation guarantee. |
| Reflection, rejection, merge and arena | Direct full doctrine: SRC-1 `src/agent/subagents/builtin/reflection-v2.md`; direct finalization ranges: `src/agent/memory-worktree.ts`; arena definitions, display and choice ranges: `src/cli/helpers/reflection-arena.ts`; supplied launcher trace | [EPI-RTE-reflection-guidance](#epi-rte-reflection-guidance), [EPI-RTE-reflection-merge](#epi-rte-reflection-merge), [EPI-RTE-arena-choice](#epi-rte-arena-choice). Transcript slicing, automatic selection and primary-agent conflict resolution not fully traced; no claim of comprehensive evidence presentation or semantic acceptance. |
| Local compaction and prompt consumption | Direct ranges: SRC-1 `src/backend/local/compaction.ts`, `src/backend/local/local-backend.ts`, `src/backend/local/system-prompt-compilation.ts`; supplied store trace | [EPI-RTE-summary-generation](#epi-rte-summary-generation), [EPI-RTE-summary-retention](#epi-rte-summary-retention), [EPI-RTE-memory-projection](#epi-rte-memory-projection). Provider semantics opaque; summary fidelity unestablished. |
| Recall | Direct full descriptor: SRC-1 `src/agent/subagents/builtin/recall.md`; supplied Task mechanism | Recall forks parent history and injects search guidance rather than using the descriptor's body. Search instructions/consumer transformations remain uninspected; no retrieval-completeness or returned-answer warrant claim. |
| Mod-learning builder | Direct ranges/search: SRC-1 `src/mods/learning-harness.ts`; wrapper search `scripts/mod-learning/learn-mod.ts` | [EPI-RTE-mod-evaluation](#epi-rte-mod-evaluation), [EPI-RTE-mod-selection](#epi-rte-mod-selection). Assertion executor internals, scenario environments and baseline contrasts not fully inspected; no causal component effect. |
| Settings, release update, extensions | Supplied runtime: SRC-1 `src/skills/builtin/self-configuration/scripts/update-agent-settings.ts`, `src/updater/auto-update.ts`, `src/mods/mod-engine.ts` | [RT-RTE-settings-patch](runtime.md#rt-rte-settings-patch), [RT-RTE-package-update](runtime.md#rt-rte-package-update), [RT-BAP-mod-capabilities](runtime.md#rt-bap-mod-capabilities). These change organization but do not themselves evaluate truth or improvement. |
| Other exposed or developer improvement routes | Inventoried by boundary: channels/listener bridges, shared memory, skills installs, trajectory review, doctor/dreaming, `.github/`, developer automation | Not traced here beyond supplied routes and dispatch. Available but uninspected implementation prevents system-complete negatives about acceptance, criticism or improvement. Dynamic content, hosted dreaming and providers are separately unavailable, preventing deployed-loop and parametric-learning conclusions. |

No inaccessible repository path is inferred from an uninspected row. Absence of retained live memories prevents individuation of actual propositions, candidate provenance and actual accepted ampliative claims. Absence of run evidence prevents activation/compliance conclusions; absence of interventions/comparisons prevents improvement attribution. Distributed-parametric model identity and mutability are see [RT-CMP-turn-model](runtime.md#rt-cmp-turn-model) and [RT-CMP-summary-model](runtime.md#rt-cmp-summary-model), not a claim that the repository freezes their weights.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [RT-OBJ-local-transcript](runtime.md#rt-obj-local-transcript) | Conversation assertions and tool reports, alongside symbolic envelopes | see record | SRC-1 `src/backend/local/local-store.ts` | Container includes claims with heterogeneous sources; persistence does not authenticate them. |
| [EPI-OBJ-compaction-summary](#epi-obj-compaction-summary) | Statements about requests, prior actions and prior events | see record | SRC-1 `src/backend/local/compaction.ts` | No live instance supplied; truth, semantic preservation and entailment indeterminate. |
| [EPI-OBJ-memory-prose](#epi-obj-memory-prose) | Facts, preferences, corrections and procedure assumptions; some instructions are non-truth-apt | see record | SRC-1 `src/agent/subagents/builtin/reflection-v2.md` | File-level validation does not establish body truth; core and deferred delivery differ. |
| [EPI-OBJ-arena-choice](#epi-obj-arena-choice) | Selection/notes may state judgments; choice value alone states a preference | see record | SRC-1 `src/cli/helpers/reflection-arena.ts` | Recorded preference is not a named evidence-consuming factual criterion. |
| [EPI-OBJ-mod-report](#epi-obj-mod-report) | Assertions that outputs/traces met configured markers and checks | see record | SRC-1 `src/mods/learning-harness.ts` | Validity bounded to reported inputs and configured scenario predicates. |
| [RT-OBJ-tool-context](runtime.md#rt-obj-tool-context) | None in registry/scope references; descriptions/results separately interpreted | see record | SRC-1 `src/tools/manager.ts` | Capability/admission state is not factual warrant. |
| [RT-CMP-turn-model](runtime.md#rt-cmp-turn-model), [RT-CMP-summary-model](runtime.md#rt-cmp-summary-model) | Distributed knowledge cannot be individuated from inspected caller | see records | SRC-1 `src/backend/dev/pi-stream-adapter.ts`, `src/backend/local/compaction.ts` | Internal content/updates and exact weight identity not determinable; other retained text remains independently assessable. |

## Authority-route ledger

Fields owned by declaring records use `see` below. The architectural status is this report's independent assessment. No record here establishes observed operation.

Route ID: [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-local-transcript](runtime.md#rt-obj-local-transcript)
Content/update relation: truth-apt transformation: acquisition/import for incoming user/tool claims; source warrant unknown. Model-produced propositions: truth-apt transformation: indeterminate; no candidate instance establishes entailment or non-entailment.
Transition or check target: see route; no answer oracle.
Evaluator/condition and domain: see route; permissions check action admission, not answer truth.
Activation and timing: see route.
Possible or observed result: see route.
Implemented force: see route.
Epistemic authority and scope: input supplies attributed claims and model candidates, not universal factual endorsement.
Operational authority: behavior permitted, blocked, or changed: see route.
Behavioral-authority path: see [RT-BAP-provider-context](runtime.md#rt-bap-provider-context).
Evidence source ID and local anchor: SRC-1 `src/headless.ts`.
Claim IDs: [RT-CLM-approval-policy](runtime.md#rt-clm-approval-policy).
Mismatch marker: none; consent is not an answer oracle.
Gap/limit: source warrant and observed correctness require tool/environment evidence, not stop reasons.

Route ID: [EPI-RTE-summary-generation](#epi-rte-summary-generation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-compaction-summary](#epi-obj-compaction-summary)
Content/update relation: truth-apt transformation: indeterminate; summarization is requested, but model semantics and omitted propositions are not checked. Non-ampliative reshaping versus derivation/conjecture remains unresolved.
Transition or check target: see record.
Evaluator/condition and domain: see record; overflow/length checks are not fidelity checks.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: generated account of past context, with unestablished fidelity.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record and [RT-BAP-provider-context](runtime.md#rt-bap-provider-context).
Evidence source ID and local anchor: SRC-1 `src/backend/local/compaction.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: no concrete summary, reference comparison or run.

Route ID: [EPI-RTE-summary-retention](#epi-rte-summary-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-compaction-summary](#epi-obj-compaction-summary)
Content/update relation: no content change; summary is packaged with a context-loss notice.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: retention grants no additional factual warrant.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `src/backend/local/local-backend.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: no separate lifecycle integration after factual acceptance established in this path.

Route ID: [EPI-RTE-frontmatter-check](#epi-rte-frontmatter-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-prose](#epi-obj-memory-prose)
Content/update relation: truth-apt transformation: entailed derivation; error list follows from exact file text under the function's scalar syntax rules, not from body truth.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: diagnostic list, consumed separately by [EPI-RTE-commit-admission](#epi-rte-commit-admission).
Epistemic authority and scope: conformance to this validator's bounded rules only.
Operational authority: behavior permitted, blocked, or changed: see record; no admission by this function alone.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `src/memory-frontmatter.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: parser is not a semantic evaluator or general YAML validator.

Route ID: [EPI-RTE-commit-admission](#epi-rte-commit-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-prose](#epi-obj-memory-prose)
Content/update relation: no content change.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: operational admission against format/layout constraints, not acceptance of truth-apt body claims for an intended knowledge use.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `src/agent/memory-git-hooks.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: hook bypass, restore and other callers prevent extending this gate to every state replacement.

Route ID: [EPI-RTE-reflection-guidance](#epi-rte-reflection-guidance)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-memory-prose](#epi-obj-memory-prose)
Content/update relation: truth-apt transformation: indeterminate for claimed facts/procedures; non-truth-apt policy/content update: behavioral instructions when the child writes them. Actual output not captured.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: advisory guidance to spawned model; spawning is implemented separately in [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task).
Epistemic authority and scope: requested comparison to conversational evidence, not evidenced model acceptance.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `src/agent/subagents/builtin/reflection-v2.md` (doctrine/design).
Claim IDs: [EPI-CLM-long-horizons](#epi-clm-long-horizons).
Mismatch marker: actual compliance unknown.
Gap/limit: requested generalization alone is not a witnessed ampliative claim or formulated criticism.

Route ID: [EPI-RTE-reflection-merge](#epi-rte-reflection-merge)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-prose](#epi-obj-memory-prose)
Content/update relation: no content change in the selected Git merge branch; conflict-resolution alternatives unassessed.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: branch ancestry/merge success, not propositional warrant; this is operational integration before any established factual acceptance, not lifecycle integration in the technical sense.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see [EPI-RTE-memory-projection](#epi-rte-memory-projection).
Evidence source ID and local anchor: SRC-1 `src/agent/memory-worktree.ts`.
Claim IDs: [EPI-CLM-long-horizons](#epi-clm-long-horizons).
Mismatch marker: merge status must not be read as knowledge acceptance.
Gap/limit: no merged candidate/run supplied.

Route ID: [EPI-RTE-arena-choice](#epi-rte-arena-choice)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-arena-choice](#epi-obj-arena-choice), [EPI-OBJ-memory-prose](#epi-obj-memory-prose)
Content/update relation: no content change.
Transition or check target: see record.
Evaluator/condition and domain: see record; a choice selects a branch, with no enforced factual criterion.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: recorded comparative preference; factual scope/criterion not required.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `src/cli/helpers/reflection-arena.ts`.
Claim IDs: none.
Mismatch marker: counters a blanket claim that memory has no human-selection route.
Gap/limit: chooser identity and actual evidence reviewed unobserved.

Route ID: [EPI-RTE-memory-projection](#epi-rte-memory-projection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-prose](#epi-obj-memory-prose)
Content/update relation: truth-apt transformation: non-ampliative reshaping; committed text is selected, stripped of metadata and wrapped, not independently endorsed.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: source warrant unknown; local path/revision locates text but does not authenticate truth.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see [RT-BAP-provider-context](runtime.md#rt-bap-provider-context).
Evidence source ID and local anchor: SRC-1 `src/backend/local/system-prompt-compilation.ts`.
Claim IDs: [EPI-CLM-long-horizons](#epi-clm-long-horizons).
Mismatch marker: none.
Gap/limit: core text and deferred directory pointers are not equivalent evidence delivery.

Route ID: [EPI-RTE-memory-fetch](#epi-rte-memory-fetch)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-prose](#epi-obj-memory-prose)
Content/update relation: truth-apt transformation: non-ampliative reshaping; selection, wrappers and truncation degrade completeness, not an inference of falsehood.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: attributed file extract, source warrant unknown.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `src/tools/impl/memory.ts`.
Claim IDs: none.
Mismatch marker: none.
Gap/limit: on-demand reads use filesystem contents; committed prompt lineage cannot be assigned to all tool extracts.

Route ID: [EPI-RTE-memory-restore](#epi-rte-memory-restore)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-prose](#epi-obj-memory-prose)
Content/update relation: truth-apt transformation: acquisition/import; backup source warrant unknown.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: none added by existence/directory/force checks.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `src/cli/subcommands/memory.ts`.
Claim IDs: none.
Mismatch marker: restore is a non-commit replacement path.
Gap/limit: subsequent compiler/backend state reconciliation not traced.

Route ID: [EPI-RTE-hook-policy](#epi-rte-hook-policy)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: see [RT-OBJ-tool-context](runtime.md#rt-obj-tool-context); configured hook outputs are transient.
Content/update relation: non-truth-apt policy/content update: rewritten tool arguments and blocking decisions.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: no generic factual license; configured hook criterion opaque.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `src/hooks/executor.ts`, `src/tools/manager.ts`.
Claim IDs: [RT-CLM-approval-policy](runtime.md#rt-clm-approval-policy).
Mismatch marker: none.
Gap/limit: operational rejection/rewrite can occur without a truth-apt route.

Route ID: [EPI-RTE-mod-evaluation](#epi-rte-mod-evaluation)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-mod-report](#epi-obj-mod-report)
Content/update relation: truth-apt transformation: entailed derivation for marker verdicts given captured text/exit/timeout and configured predicates; actual behavior beyond those inputs not entailed.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: verdict/report; separate selection consumer below.
Epistemic authority and scope: scenario marker conformance, not arbitrary answer correctness or mechanism explanation.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record.
Evidence source ID and local anchor: SRC-1 `src/mods/learning-harness.ts`.
Claim IDs: [EPI-CLM-long-horizons](#epi-clm-long-horizons).
Mismatch marker: counters a blanket claim that Code never checks improvement candidates.
Gap/limit: assertion-only alternatives and environment validity incompletely inspected.

Route ID: [EPI-RTE-mod-selection](#epi-rte-mod-selection)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-mod-report](#epi-obj-mod-report); executable candidate is distinct from report.
Content/update relation: non-truth-apt policy/content update: successor mod file selected/copied; feedback supplied to later proposal rounds.
Transition or check target: see record.
Evaluator/condition and domain: see record.
Activation and timing: see record.
Possible or observed result: see record.
Implemented force: see record.
Epistemic authority and scope: acceptance for configured scenario conformance, not accepted explanatory theory or universal transfer.
Operational authority: behavior permitted, blocked, or changed: see record.
Behavioral-authority path: see record and [RT-BAP-mod-capabilities](runtime.md#rt-bap-mod-capabilities) for separately loaded code.
Evidence source ID and local anchor: SRC-1 `src/mods/learning-harness.ts`.
Claim IDs: [EPI-CLM-long-horizons](#epi-clm-long-horizons).
Mismatch marker: promotion is not evidence of live activation or benefit.
Gap/limit: no observed candidate, loaded successor, contrast or causal outcome.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-long-horizons](#epi-clm-long-horizons) | see record | SRC-1 `README.md`, doctrine/design | Reflection asks for corrections, reusable patterns and skill updates | [EPI-RTE-reflection-merge](#epi-rte-reflection-merge), [EPI-RTE-memory-projection](#epi-rte-memory-projection), [EPI-RTE-mod-evaluation](#epi-rte-mod-evaluation), [EPI-RTE-mod-selection](#epi-rte-mod-selection); configuration/load paths see [RT-RTE-settings-patch](runtime.md#rt-rte-settings-patch), [RT-RTE-extension-load](runtime.md#rt-rte-extension-load) | None supplied | No intervention/comparison or later activated outcome; mutable text is not evidence of improved capacity | Persistent, behavior-shaping text and executable change paths exist; mod builder has evaluation-responsive selection | Exercised long-horizon learning and successful improvement unsupported here; architectural contributions are not withdrawn |
| [RT-CLM-approval-policy](runtime.md#rt-clm-approval-policy) | see record | SRC-1 `src/permissions/checker.ts`, implementation | see record | [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn), [EPI-RTE-hook-policy](#epi-rte-hook-policy) | see record | Consent/admission criteria do not test truth | Action authority, not answer warrant | No mismatch with scoped policy claim; broad epistemic interpretation would be wrong |
| [RT-CLM-effect-checkpoint](runtime.md#rt-clm-effect-checkpoint) | see record | SRC-1 `src/websocket/listener/recovered-approval-checkpoint.ts`, implementation | see record | [RT-RTE-listener-approval](runtime.md#rt-rte-listener-approval) | see record | Recorded exact result versus unknown outcome preserves recovery uncertainty; result correctness depends on executor | Conservative outcome bookkeeping | Neither exactly-once effects nor factual correctness follows |

## Bounded conclusion

Letta Code can retain conversational assertions and model-produced accounts, then place selected text in subsequent provider context. This grants operational relevance through model interpretation, not an independently verified truth status. Imported user/tool/file assertions retain attribution only as far as the corresponding containers and paths preserve it; their original warrant is unknown. Memory fetch can omit content with explicit truncation notices; prompt projection selectively exposes committed core bodies and deferred pointers. These are bounded reshaping routes, not new knowledge by themselves. See [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn), [EPI-RTE-memory-fetch](#epi-rte-memory-fetch), [EPI-RTE-memory-projection](#epi-rte-memory-projection).

The frontmatter evaluator derives bounded conformance results from exact input text. Its hook consumer blocks malformed commits, but leaves body truth outside the checked domain. A validly formatted false proposition therefore passes this particular check. Backup restore is a separately enforced replacement path; merge success and recompile eligibility are similarly operational predicates. No evidence-consuming acceptance of a factual memory claim for a named intended use is established by these inspected predicates. This conclusion is local, not a claim that no shipped or dynamic evaluator can perform such acceptance. See [EPI-RTE-frontmatter-check](#epi-rte-frontmatter-check), [EPI-RTE-commit-admission](#epi-rte-commit-admission), [EPI-RTE-memory-restore](#epi-rte-memory-restore), [EPI-RTE-reflection-merge](#epi-rte-reflection-merge).

Reflection instructions request evidence comparison, contradiction resolution, withdrawal of wrong content and generalization into reusable procedures. The background execution and merge path are wired, but those requested semantic operations remain doctrine without a supplied candidate/trace demonstrating them. Compaction independently generates summaries whose fidelity and entailment remain indeterminate; successful model return leads to retention without an inspected reference comparison. Arena selection is a genuine optional human-facing branch choice with discarding and logs, not a universally absent evaluator. Its preference result still lacks an enforced factual criterion/scope. See [EPI-RTE-reflection-guidance](#epi-rte-reflection-guidance), [EPI-RTE-summary-generation](#epi-rte-summary-generation), [EPI-RTE-summary-retention](#epi-rte-summary-retention), [EPI-RTE-arena-choice](#epi-rte-arena-choice).

The mod-learning plane supplies the clearest inspected evidence-consuming successor selection: configured marker predicates assess output/trace text, passing candidates can be promoted, and prior evaluation histories reach later proposal rounds. Acceptance is for scenario conformance of executable candidates, not acceptance of a formulated ampliative theory. Direct hook policies also revise/block behavior without factual warrant. Neither route requires a universal knowledge ontology. See [EPI-RTE-mod-evaluation](#epi-rte-mod-evaluation), [EPI-RTE-mod-selection](#epi-rte-mod-selection), [EPI-RTE-hook-policy](#epi-rte-hook-policy).

For the public long-horizon claim, the objective of improved future behavior is distinguishable from merely changing files, but lacks a supplied operational metric/contrast. The bounded mod pathway wires evaluation to selection and optional persistent code copying; its later load is a separate supported capability, not observed activation. Subsequent operation causally depending on that change is unestablished. For memory reflection, trace-informed semantic selection is requested and persistent context consumption is wired; actual evidence-to-update dependence and later behavior are unobserved. Thus neither exercised self-improvement nor successful learning is established over sessions. Reflection's requested self-representation and the capacity to deliver its updates remain positive contributions; reliable content-directed criticism, autonomous completion of every semantic operation, and theory-builder iteration are independently unresolved without candidate content and consumed criticisms. Opaque model processing supplies neither positive nor negative evidence for those properties. See [EPI-CLM-long-horizons](#epi-clm-long-horizons) and the independently scoped routes above. Unassessed relevant paths in the coverage table prevent any unqualified system-wide negative.

## Shared records

### Operative objects

#### EPI-OBJ-compaction-summary
Label: Compaction summary prose

Part of: [RT-OBJ-local-transcript](runtime.md#rt-obj-local-transcript)

Source-native identity: `summary` and `metadata.compaction.summary`. Natural-language encoding, consumed as the account of earlier conversation; storage is local transcript/session state rather than model weights. Distinct material part because summarization and clipping differ from raw message persistence. SRC-1 `src/backend/local/compaction.ts`, `src/backend/local/local-backend.ts`; generation and retention passages are in their separate routes below.

#### EPI-OBJ-memory-prose
Label: Core and deferred memory prose

Source-native identity: committed core Markdown bodies, `MEMORY.md` indexes and deferred files under `$MEMORY_DIR`. Natural-language facts and procedures; path/frontmatter/layout are symbolic selectors. Storage: Git-backed files and working checkout. Core bodies are inlined; deferred directory pointers require a later request. No counterpart in supplied runtime objects: [RT-OBJ-local-transcript](runtime.md#rt-obj-local-transcript) is conversation history, not the MemFS file repository; [RT-BAP-provider-context](runtime.md#rt-bap-provider-context) is a consumer path, not this content. SRC-1 `src/backend/local/system-prompt-compilation.ts`; minimum passages in projection/fetch routes below. Core and deferred contents share mutable text storage but retain their distinct delivery and warrant limits there.

#### EPI-OBJ-arena-choice
Label: Reflection arena choice record

Source-native identity: `completedRun.choice` and `choices.jsonl`. Symbolic chosen/discarded labels, timestamps and integration result, optional natural-language notes; stored in run JSON and appended choice log on local disk. Distinct from [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task): the choice is a comparative disposition after two candidate tasks, not their execution record. SRC-1 `src/cli/helpers/reflection-arena.ts`; operative passage in arena route below.

#### EPI-OBJ-mod-report
Label: Mod learning evaluation report

Source-native identity: `ModLearningEvaluationResult`, `ModLearningReport`, history/report JSON and Markdown. Symbolic checks, pass/score fields and paths plus natural-language result/diagnostic text. Local files retain the record for later proposal/selection; no counterpart in [RT-RTE-extension-load](runtime.md#rt-rte-extension-load), which admits executable modules rather than judging candidates against scenario outputs. SRC-1 `src/mods/learning-harness.ts`; minimum passages in evaluation and selection routes below.

### Routes

#### EPI-RTE-summary-generation
Label: Local summary generation and clipping

Part of: [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn)

Endpoints: selected transcript → summarizer/provider → trimmed/clipped text. Owner: local compaction helper; model owns semantic output, host owns overflow retries and output clipping. Context: summarization instructions and formatted transcript; state/effect: returned candidate summary, not yet retained. Distinct material subroute of conversation context management, using [RT-CMP-summary-model](runtime.md#rt-cmp-summary-model) rather than assuming the foreground inference identity. SRC-1 `src/backend/local/compaction.ts`.

- Immediate return: summary text or exception; shorter input variants may be tried after context overflow.
- Later read-back: inapplicable — this producer returns text; the separate retention consumer stores it.
- Delegated visibility: summary model receives a formatted transcript with tool-return truncation and possible shorter fallback variants.
- Selection predicate: caller-selected compaction transcript and settings; non-overflow provider errors propagate.
- Invalidation or expiry: the summary may be clipped to configured characters before return; no semantic withdrawal predicate here.
- Activation or effect: returned summary reaches the compaction caller; reliable summarization unobserved.
- Evidence limits: no candidate instance or reference comparison; model internals inaccessible.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete deterministic output trace: for `result.text = "abcdef"`, `clipChars = 3`, trimming changes nothing and the branch returns `abc... [summary truncated to fit]`. This is non-ampliative clipping of text, not proof that the full model output was semantically preserving. No target execution is used. The entire semantic transformation remains indeterminate.

> let summary = result.text.trim();
> const clipChars = input.clipChars === undefined ? 50000 : input.clipChars;
> if (clipChars !== null && summary.length > clipChars) {
>   summary = `${summary.slice(0, clipChars)}${SUMMARY_TRUNCATION_SUFFIX}`;
> }
> return summary;
> --- `src/backend/local/compaction.ts`

> const SUMMARY_TRUNCATION_SUFFIX = "... [summary truncated to fit]";
> --- `src/backend/local/compaction.ts`

#### EPI-RTE-summary-retention
Label: Summary retention in compaction state

Part of: [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn)

Endpoints: successful summary → `compactConversationAll` → compacted history → later provider context. Owner: local backend/store. State: packed summary, remaining messages, stats. The admission domain is completed summarizer/caller plan, not fidelity; model proposes text, software decides retention, errors veto continuation. No human content approval or answer oracle is required; operating mode is ordinary context maintenance triggered manually/automatically. Recovery depends on store state, not a warranted-summary rollback criterion. Distinct from generation and the container [RT-OBJ-local-transcript](runtime.md#rt-obj-local-transcript). SRC-1 `src/backend/local/local-backend.ts`.

- Immediate return: counts, summary and stats after store compaction.
- Later read-back: retained summary and remaining messages enter subsequent conversation invocations through history loading.
- Delegated visibility: provider receives the packaged summary in place of hidden prior messages; not all original evidence is delivered.
- Selection predicate: compaction mode/plan and successfully returned summary.
- Invalidation or expiry: later compaction or conversation maintenance can supersede current context; original fidelity check is not established.
- Activation or effect: store compaction is invoked, changing available history; actual model behavior unobserved.
- Evidence limits: persistence baseline is supplied runtime; no run or factual acceptance trace.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const storeResult = this.store.compactConversationAll({
>   conversationId,
>   agentId,
>   summary,
>   packedSummary: packageLocalSummaryMessage(summary, stats, settings.mode),
>   stats,
>   remainingMessages: plan.messagesToKeep,
> });
> --- `src/backend/local/local-backend.ts:825-832`

#### EPI-RTE-frontmatter-check
Label: Memory frontmatter conformance check

Endpoints: path/text/previous accepted text/layout → deterministic validator → errors. Owner: `validateMemoryFileFrontmatter`; no content changes. Target/domain: required scalar fields, allowed/duplicate/empty fields, index frontmatter exclusion, legacy read-only fields. Model/user may supply proposed file text; caller supplies trusted previous text/layout, and the program evaluates. No factual answer oracle; mode is file conformance, not experiment. No counterpart in runtime's generic [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn): this is the specific content gate used by Git readers/hooks. SRC-1 `src/memory-frontmatter.ts`.

- Immediate return: deterministic string array of errors, possibly empty.
- Later read-back: inapplicable — function does not retain a result.
- Delegated visibility: installed hook embeds this function and supplies Git-selected contents.
- Selection predicate: caller chooses format, paths and trusted previous content; v2 index files have a special rule.
- Invalidation or expiry: result describes supplied inputs only; changed inputs require another call.
- Activation or effect: result is evidence consumed by a separate commit gate; no direct write/commit.
- Evidence limits: semantic truth, full YAML validity, path/ref authorization and deletion/rename protection are outside this function's domain.
- implementation conclusion status: wired
- operation conclusion status: uninspected

Concrete implementation deduction: `path = "facts.md"`, `format = "memfs-v2"`, `previousContent = null`, and text `---\nname: facts\ndescription: claims\n---\n2 + 2 = 5\n` yield `[]`: the closing marker is present, two permitted nonempty fields occur once, required keys are present, and no branch checks body truth. The false body proposition is a counterexample to treating this check as factual acceptance. The result is a justified conformance finding relative to inspected code, not a target run.

> const allowed = v2
>   ? ["name", "description"]
>   : ["description", "read_only", "limit"];
> for (const line of lines.slice(1, closing)) {
> --- `src/memory-frontmatter.ts`

> for (const key of v2 ? ["name", "description"] : ["description"]) {
>   if (!seen.has(key)) errors.push(`${path}: missing required field '${key}'`);
> }
> --- `src/memory-frontmatter.ts`

#### EPI-RTE-commit-admission
Label: Installed memory commit admission

Endpoints: staged tree → embedded validator/error aggregation → hook exit → Git commit admission. Owner: generated pre-commit hook and Git invocation. Context: trusted layout policy; state: index plus HEAD for legacy previous content. Program decides; file author proposes; failing hook vetoes ordinary commit. Human authorship of a file is not separate content approval. Trigger: commit, proposed change: staged memory/skills; criteria: syntax/layout plus invoked constraint validator; persistence: admitted commit. Rejection is operational, not factual acceptance. Direct bypasses and non-commit replacements are not covered; repair/recommit is available, no truth-based rollback. No counterpart to [RT-CLM-approval-policy](runtime.md#rt-clm-approval-policy), which concerns client tools. SRC-1 `src/agent/memory-git-hooks.ts`, `src/agent/memory-constraints-audit.ts`.

- Immediate return: zero exit or failure diagnostics.
- Later read-back: admitted commit becomes eligible for prompt projection; result itself is not retained here.
- Delegated visibility: validator receives complete staged v2 projected Markdown, excluding skills; legacy paths are narrower and changed-only.
- Selection predicate: layout policy and staged/HEAD root marker; projected ancestor indexes govern v2 path inclusion.
- Invalidation or expiry: each commit reruns selected checks; Git invocation/hook bypass and replacement paths are separate.
- Activation or effect: errors prevent ordinary hook-covered commit; constraint audit can separately flag committed HEAD invalid for publication.
- Evidence limits: full constraint implementation/publication consumers not inspected; passing does not certify claims.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> validate_memory_files "memfs-v2"
>
> if [ -n "$errors" ]; then
>   echo "Memory validation failed:"
>   echo -e "$errors"
>   exit 1
> fi
> validate_memory_constraints
> exit 0
> --- `src/agent/memory-git-hooks.ts`

> const validation = validateMemoryConstraintsHead(memoryDir);
> if (validation.valid) return null;
> return {
>   status: "invalid",
>   summary: `Committed memory fails validation:\n${validation.output}`,
>   memoryDir,
>   localOnly,
> };
> --- `src/agent/memory-constraints-audit.ts`

#### EPI-RTE-reflection-guidance
Label: Transcript reflection guidance

Part of: [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task)

Endpoints: recent conversation payload and current memory → instructed child review → requested memory/skill edits and commit/report. Model is requested to investigate, select lasting candidates, compare existing content, correct/remove contradictions, review and persist. Owner: shipped reflection instruction at the child semantic boundary; host launch/merge is separately implemented. Natural-language guidance includes mistakes, user corrections, facts and reusable procedures; intended persistence is edited facts and skills, not raw event logs. Ordinary open transcript review, not a controlled curriculum. Model proposes and judges content; hook/Git can veto commits, user not required to approve each candidate; no independent expected-answer oracle. Source is doctrine/design only for semantic compliance. SRC-1 `src/agent/subagents/builtin/reflection-v2.md`.

- Immediate return: requested final report of actual edits, skipped candidates, commit and issues.
- Later read-back: requested committed memory can reach later parent prompts/skill requests; compliance unobserved.
- Delegated visibility: payload path, root memory and selected deferred/skill files; instruction calls for bounded transcript reads and on-demand adjacent content.
- Selection predicate: lasting/not duplicated/generalizable filters; facts versus reusable multistep workflow placement.
- Invalidation or expiry: instructed stale-entry correction, deletion of wrong/forgotten content and archiving of retired context; actual withdrawals unobserved.
- Activation or effect: semantic operations are requested, not evidenced; generic child execution wiring is supplied separately.
- Evidence limits: no transcript/output/candidate instance; no factual acceptance trace, improved capacity or criticism result established.
- doctrine conclusion status: claimed
- operation conclusion status: uninspected

> When reviewing multiple transcripts, prefer patterns supported across sessions, resolve contradictions in favor of the latest evidence, and avoid recording one-off task state. Follow the phases below in order.
> --- `src/agent/subagents/builtin/reflection-v2.md`

> **Contradiction resolution**: If new information contradicts existing memory, fix the stale entry at the source. Do not append the new version alongside the old.
> --- `src/agent/subagents/builtin/reflection-v2.md`

> **Archiving retired context**: Use the root file `ARCHIVE.md` when content should no longer be load-bearing but may still be useful as historical context — shrink or remove the active source, then append a concise dated entry to `ARCHIVE.md`. Delete (don't archive) content the user asked to forget, sensitive or wrong content, or junk with no future-reference value.
> --- `src/agent/subagents/builtin/reflection-v2.md`

#### EPI-RTE-reflection-merge
Label: Reflection branch merge and cleanup

Part of: [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task)

Endpoints: committed worker branch → finalizer → Git merge/ancestry result → parent main or failure/cleanup. Owner: worktree finalizer, not the model's claimed report. State: parent/child heads, commit count, options and cleanliness. Model proposes files; program admits operationally with configured merge/previous-integration checks. Trigger is worker completion; successful merge retains edits; rejection/abort and cleanup permit transcript retry rather than accepting failed work. Guidance shapes the child separately. No per-content human decision or answer oracle; mode is background maintenance integration. This subroute adds specific branch disposition to the generic task, not a new task identity. SRC-1 `src/agent/memory-worktree.ts`.

- Immediate return: merged, no-changes or failure/conflict status, summary and heads.
- Later read-back: merged parent HEAD is eligible for later prompt compilation; failure result supports retry, not factual reliance.
- Delegated visibility: parent receives branch contents through Git; finalizer inspects refs/status, not the truth of every fact.
- Selection predicate: finalization options, worker success/commits/cleanliness; requireAlreadyMerged branch tests ancestry, ordinary branch attempts merge.
- Invalidation or expiry: failed merges abort and clean worktree/branch; this does not semantically retract facts from a previously accepted claim.
- Activation or effect: parent Git state can change; subsequent context mechanism separately wired.
- Evidence limits: primary-agent integration and synchronization alternatives not fully traced; no observed integration or warrant criterion.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const mergeResult = await tryRunGit(worktree.parentMemoryDir, [
>   "merge",
>   worktree.branchName,
>   "-m",
>   mergeMessage,
> ]);
> if (!mergeResult) {
>   await tryRunGit(worktree.parentMemoryDir, ["merge", "--abort"]);
>   await cleanupWorktreeAndBranch(
>     worktree.parentMemoryDir,
>     worktree.worktreeDir,
>     worktree.branchName,
>     { force: true },
>   );
> --- `src/agent/memory-worktree.ts`

#### EPI-RTE-arena-choice
Label: Reflection arena comparative choice

Endpoints: two background worktree candidates → blind labeled reports and payload/run paths → chosen label/tie → selected finalizer, discarded candidates and choice log. Owner: arena finalization software; human-facing UI asks which reflection should merge, caller supplies the recorded response. Distinct from [RT-RTE-subagent-task](runtime.md#rt-rte-subagent-task), since task success is not this comparative choice. Trigger: awaiting choice; model proposes alternatives, chooser selects/vetoes through tie, software rejects wrong run status/unknown label and can fail integration. Guidance is the merge question and optional notes, not an enforced factual standard. Possible rollback: nonselected branches discarded; selected integration follows merge failure/retry protocol. Mode: bounded two-candidate comparison; oracle: inapplicable — preference is not an expected answer. SRC-1 `src/cli/helpers/reflection-arena.ts`.

- Immediate return: completed run and formatted outcome including integration/discards.
- Later read-back: choice JSON and log retained; selected merged memory can reach later prompts, while the log's training consumer is external/uninspected.
- Delegated visibility: reports can be truncated, model names hidden before choice, payload and complete run paths displayed; no guarantee the chooser inspects actual diff or transcript.
- Selection predicate: awaiting-choice status and chosen label; tie finalizes both without merge.
- Invalidation or expiry: nonselected candidates finalized with shouldMerge false; choice record retains disposition.
- Activation or effect: choice changes which branch is offered for integration; logs/upload are not evidence of later training or benefit.
- Evidence limits: actual chooser identity, criteria, content inspection and correctness unobserved.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "Models are hidden until you choose.",
> "",
> reports,
> "",
> "Use the reflection arena choice prompt below to select a winner and optionally add notes.",
> --- `src/cli/helpers/reflection-arena.ts`

> for (const candidate of run.candidates) {
>   if (options.choice !== "tie" && candidate.label === options.choice) {
>     continue;
>   }
>   discarded.push(candidate.label);
>   await finalizeReflectionMemoryWorktree(candidate.worktree, {
>     shouldMerge: false,
>     knownNoChanges: candidateIsConfirmedNoOp(candidate),
>   });
> }
> --- `src/cli/helpers/reflection-arena.ts`

> await saveReflectionArenaRun(completedRun);
> await appendChoiceRecord(completedRun);
> void uploadChoiceRecordToHf({
>   run: completedRun,
>   memoryBaseCommit,
>   memoryCandidateCommit,
> })
> --- `src/cli/helpers/reflection-arena.ts`

#### EPI-RTE-memory-projection
Label: Committed memory prompt projection

Part of: [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn)

Endpoints: committed MemFS tree → collected selected bodies/indexes → wrapped coreMemory → provider context. Owner: local compiler/backend; effects through [RT-BAP-provider-context](runtime.md#rt-bap-provider-context), advisory/model-interpreted, current/later turns. Target is path/layout selection, not truth. Distinct subroute of supplied compiled-prompt consumption. SRC-1 `src/backend/local/system-prompt-compilation.ts`.

- Immediate return: compiled content, coreMemory, hash, timestamp and MemFS revision.
- Later read-back: changed committed memory revises subsequent compiled/context-update delivery; supplied runtime describes cache and mid-conversation consumer.
- Delegated visibility: v2 core file bodies and root index inlined; immediate deferred directories represented by pointers, not all deferred contents.
- Selection predicate: committed HEAD Markdown paths, layout and core/index classification; unreadable blobs skipped best effort.
- Invalidation or expiry: source raw-system hash and committed revision invalidate compiler cache per supplied runtime; no factual stale-content detector established.
- Activation or effect: eligible text is delivered for model interpretation; compliance or improved behavior unobserved.
- Evidence limits: missing original proposition provenance and no run; hosted compilation unavailable.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const raw = gitOutput(memoryDir, ["show", `HEAD:${relativePath}`]);
> const { frontmatter, body } = parseFrontmatter(raw);
> files.push({
>   relativePath,
>   label: labelFromPath(relativePath),
>   value: body,
> --- `src/backend/local/system-prompt-compilation.ts`

> for (const file of rootFiles) {
>   const lines = [`<${file.label}>`];
>   const description = file.description.trim();
>   if (description) lines.push(`<description>${description}</description>`);
>   const value = file.value.trimEnd();
>   if (value) lines.push(value);
>   lines.push(`</${file.label}>`);
>   blocks.push(lines.join("\n"));
> }
> --- `src/backend/local/system-prompt-compilation.ts`

#### EPI-RTE-memory-fetch
Label: Deferred memory fetch and clamping

Endpoints: model-requested path → path/realpath/file checks → filesystem file or directory index/listing → tool result → next provider continuation. Owner: Memory tool and generic result transport; action effects are read-only. Distinct subroute of [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn), targeting a file repository rather than arbitrary tool results. Candidate selector is a requested relative path, not an autonomous semantic retrieval classifier. SRC-1 `src/tools/impl/memory.ts`.

- Immediate return: XML-wrapped content/listing with possible truncation notices, or thrown error.
- Later read-back: changed retained file content is read on later requests; generic conversation result retention also permits later history consumption.
- Delegated visibility: selected file text or directory index/listing; length/line budgets can omit evidence.
- Selection predicate: v2 root exists; nonhidden relative path, no traversal/outside-realpath/skills/root-core request; directory or file branch.
- Invalidation or expiry: each request reads filesystem; projection revision is not used as a truth or commitment check here.
- Activation or effect: extracted text returned as tool content; no semantic endorsement or observed reliance.
- Evidence limits: layout registration and file-type tail checks not fully inspected; returned content can differ from committed prompt.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> function renderFile(relPath: string, fullPath: string): string {
>   const content = readFileSync(fullPath, "utf8").trimEnd();
>   const open = `<memory_content path="${escapeXmlText(relPath).replace(/"/g, "&quot;")}"${descriptionAttr(readDescription(fullPath))}>`;
>   const close = "</memory_content>";
>   return `${open}\n${clampContent(content, fullPath, LIMITS.READ_OUTPUT_CHARS - open.length - close.length - 2)}\n${close}`;
> }
> --- `src/tools/impl/memory.ts`

#### EPI-RTE-memory-restore
Label: Destructive backup restore

Endpoints: caller backup path/force → existence/type checks → remove current root/copy backup → JSON success. Owner: memory CLI. Source text and Git metadata imported together; proposer is caller/backup supplier, program rejects missing force/source/non-directory, no per-proposition review. Trigger is explicit restore; guidance is destructive-write confirmation; persisted result is copied directory. Previous content is deleted, no automatic transactional rollback established. Distinct from hook-covered writes and [RT-RTE-settings-patch](runtime.md#rt-rte-settings-patch), which changes server settings. Answer oracle inapplicable; operating mode is recovery, not evaluation. SRC-1 `src/cli/subcommands/memory.ts`.

- Immediate return: restoredFrom JSON or diagnostic/nonzero exit.
- Later read-back: restored root files/HEAD become inputs to subsequent compiler/tool reads.
- Delegated visibility: later consumers receive copied content, not an authenticated explanation of every proposition's lineage.
- Selection predicate: source supplied, force flag true, path exists and is directory.
- Invalidation or expiry: current directory removed/replaced; further edits/restores can replace it again.
- Activation or effect: filesystem replacement wired; successful restore and downstream reconciliation unobserved.
- Evidence limits: no content validation call in inspected restore branch; other backup/path contracts not fully traced.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const root = getMemoryRoot(agentId);
> rmSync(root, { recursive: true, force: true });
> cpSync(backupPath, root, { recursive: true });
> console.log(JSON.stringify({ restoredFrom: backupPath }, null, 2));
> return 0;
> --- `src/cli/subcommands/memory.ts`

#### EPI-RTE-hook-policy
Label: Pre-tool hook blocking and rewrites

Part of: [RT-RTE-foreground-turn](runtime.md#rt-rte-foreground-turn)

Endpoints: proposed tool args → hook subprocess result → sequential block/updatedInput aggregation → tool manager error or argument merge before execution. Owner: hook executor and tool manager. Caller config supplies policy; model proposes action; configured program can veto/rewrite, no mandatory human content judgment. Dynamic criterion may be factual or purely policy, uninspected; no generic answer oracle. Mode is ordinary operational admission; guidance/proposal criterion is hook-specific. Persisted hook code can affect later invocations, but transient result alone is not retained learning. No universal rollback of hook subprocess effects. Distinct admission part, not supersession of [RT-CLM-approval-policy](runtime.md#rt-clm-approval-policy). SRC-1 `src/hooks/executor.ts`, `src/tools/manager.ts`.

- Immediate return: blocked/error/feedback/updatedInput; tool consumer returns error or executes revised arguments.
- Later read-back: inapplicable — this result is current-call state; configured persistent hook source is a separate external input.
- Delegated visibility: hook receives execution metadata/input; tool executor receives merged updated arguments.
- Selection predicate: configured event hooks; first accepted updatedInput and BLOCK exit govern sequential result.
- Invalidation or expiry: invocation ends; subsequent calls rerun policy.
- Activation or effect: block prevents tool execution; rewrite changes actual tool args before invocation.
- Evidence limits: installed policy and its factual domain unknown; no run; other caller/hook modes not exhaustively covered.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if (preHookResult.blocked) {
>   const feedback = preHookResult.feedback.join("\n") || "Blocked by hook";
>   return {
>     toolReturn: `Error: Tool execution blocked by hook. ${scrubAmbientSecrets(feedback)}`,
>     status: "error",
>   };
> }
>
> // Apply rewritten tool input from PreToolUse hooks (e.g. rtk command rewrite)
> if (preHookResult.updatedInput) {
>   args = {
>     ...(args as Record<string, unknown>),
>     ...preHookResult.updatedInput,
>   };
> }
> --- `src/tools/manager.ts`

#### EPI-RTE-mod-evaluation
Label: Mod candidate scenario evaluation

Endpoints: candidate/env → evaluator command/assertions → output/trace/exit/timeout → check report. Owner: learning harness/evaluator implementation. Target: candidate behavior under configured scenarios. Inspected marker domain checks required/forbidden markers in result/trace plus exit and timeout; assertions include load, message injection and argument rewrite/preservation, but their executors remain partially uninspected. Program computes verdict, scenario author supplies reference markers/expectArgs; model supplies candidate. Mode is bounded candidate experiments, unlike ordinary user turns. No human runtime approval required by this evaluator; test specifications are reference expectations, not universal truth oracles. Distinct from [RT-RTE-extension-load](runtime.md#rt-rte-extension-load): loading alone does not assess scenario conformance. SRC-1 `src/mods/learning-harness.ts`.

- Immediate return: resultText, check arrays and passed verdict; evaluator caller also obtains command result and score.
- Later read-back: reports/history retained for candidate comparison and next proposal; not evidence of generalization beyond configured domains.
- Delegated visibility: evaluator uses captured stdout/stderr and selected parsed result text; assertion routes use specified event arguments.
- Selection predicate: candidate exists; configured evaluator/spec decides checks.
- Invalidation or expiry: verdict applies to candidate and scenario invocation; changed candidate/env requires reassessment.
- Activation or effect: result is consumed by separate selection/promotion; actual runs not supplied here.
- Evidence limits: test-source predicates and wiring, not passing tests; environment validity, assertion executor internals and causal design incompletely inspected.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> const passed =
>   params.exitCode === 0 &&
>   !params.timedOut &&
>   allPresent(requiredResultMarkers) &&
>   allPresent(requiredTraceMarkers) &&
>   allAbsent(forbiddenResultMarkers) &&
>   allAbsent(forbiddenTraceMarkers);
> --- `src/mods/learning-harness.ts`

#### EPI-RTE-mod-selection
Label: Mod learning successor selection and promotion

Endpoints: candidate reports → comparison/history → next proposal round or selected report → optional copied successor file. Owner: learning harness; model proposes code, program chooses and vetoes promotion unless selected report passed. Trigger: configured learning run/candidate count; guidance: independent objective/requirements/scenarios and previous attempt history. Criterion: pass before score, earliest among passes; score orders failures, ties prefer later failures. What persists: executable candidates, reports and history; selected code optionally copied to caller path. Rollback is not automatic; rejected candidates may remain evidence but are not promoted by this branch. Operating mode: bounded optimization rounds, potentially stopping at perfect report. Oracle scope is see evaluation route. Distinct from [RT-RTE-extension-load](runtime.md#rt-rte-extension-load), a later load consumer. SRC-1 `src/mods/learning-harness.ts`.

- Immediate return: selected report, attempt history and optional promoted path.
- Later read-back: later proposal rounds receive prior attempts/history paths; copied code can be loaded in future runtime via a separately configured mod source.
- Delegated visibility: candidate generator is passed previousAttempts and previousAttemptDirs plus history/proposer-guide paths; actual reading/use unobserved.
- Selection predicate: comparison favors passing candidate; promotion additionally requires configured path; perfect report can terminate rounds.
- Invalidation or expiry: subsequent runs may replace promoted file; registry unload/reload belongs to mod runtime, not this copy operation.
- Activation or effect: evaluation-responsive iteration and persistent copying wired; live registration requires separately loading selected code.
- Evidence limits: no live successor or causal comparison; score/selection does not establish explanatory criticism or improved future capacity.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> options: { ...normalizedOptions, promoteToPath: undefined },
> previousAttempts: attempts,
> previousAttemptDirs: reports.map((attempt) => attempt.runDir),
> proposerGuidePath,
> --- `src/mods/learning-harness.ts`

> const selectedReport = selectBestReport(reports);
> const selectedCandidateIndex = selectedReport.candidateIndex ?? 1;
> let promotedToPath: string | null = null;
> if (selectedReport.passed && normalizedOptions.promoteToPath) {
> --- `src/mods/learning-harness.ts`

> promotedToPath = path.resolve(repoRoot, normalizedOptions.promoteToPath);
> await mkdir(path.dirname(promotedToPath), { recursive: true });
> await copyFile(selectedReport.candidatePath, promotedToPath);
> --- `src/mods/learning-harness.ts`

> if (candidate.passed !== incumbent.passed) {
>   return candidate.passed ? 1 : -1;
> }
> if (candidate.passed && incumbent.passed) {
>   return (incumbent.candidateIndex ?? 0) - (candidate.candidateIndex ?? 0);
> }
> --- `src/mods/learning-harness.ts`

### Claims

#### EPI-CLM-long-horizons
Label: Long-horizon learning through self-rewriting

Claimed operation: agents learn/evolve over long horizons by rewriting memory, skills, prompts and harness mods. Public source: SRC-1 `README.md`, doctrine/design. No counterpart among supplied runtime claims: approval, isolation, checkpointing and server-auth policy do not assert learning quality. Independent improvement/activation limitations are in the comparison and bounded conclusion, not an inferred absence of mutable architecture.

> Letta Code is a stateful agent harness for creating agents that are more like people than tools. Letta Code agents have memory, identity, and a sense of experience over time. They learn and evolve over long horizons through rewriting their own memory, skills, prompts, and even the harness itself (through mods).
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; provider and executable-mod paths are see [RT-BAP-provider-context](runtime.md#rt-bap-provider-context) and [RT-BAP-mod-capabilities](runtime.md#rt-bap-mod-capabilities). Route-specific symbolic enforcement and horizons are stated in the route records above.
