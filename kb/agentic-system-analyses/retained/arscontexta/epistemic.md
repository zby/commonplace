---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Ars Contexta epistemic routes: source acquisition, note criticism, quality gates and retained instruction authority at the frozen revision."
run-id: AAS-2026-10-12-arscontexta-f9e5f2f34166-01
reviewed-boundary: "2acfd5cc4473c4d06c46be63df748e77e00e2746"
---

# Ars Contexta epistemic report

## Source-and-claim boundary

The question is how Ars Contexta imports or formulates claims, evaluates them, changes reliance and carries them into later work. Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence). Evidence identity and layers: see the [Source register](boundary.md#source-register). SRC-1 is the sole source. Most semantic routes are model-facing procedures, not executable semantic evaluators. Executable hook checks have narrower domains. No target execution was performed.

The whole-system source boundary is broader than this report's direct inspection. Supplied runtime findings are cited as such, not treated as fresh source reads. Added direct reads cover the paths below at the frozen commit. Relevant available but uninspected branches prevent a system-complete negative about semantic checking or acceptance. No supplied installed vault, transcript, provider trace or causal comparison establishes route activation, accepted claim instances, improved capacity or transfer. Provider weights and exact version remain uninspected: see [RT-CMP-session-model](runtime.md#rt-cmp-session-model). Research/search services are outside the frozen implementation; their correctness and source entailment cannot be attributed to Ars Contexta.

| Entry point or operation | SRC-1 source path | Coverage and records / limit |
|---|---|---|
| Plugin hook dispatch | `hooks/hooks.json`, `hooks/scripts/write-validate.sh` | Direct full reads; [RT-RTE-write-hooks](runtime.md#rt-rte-write-hooks), [EPI-RTE-hook-shape](#epi-rte-hook-shape). Write-only dispatch; no registered pre-write semantic veto. |
| Setup, copied/inherited skills, upgrade | `skills/setup/SKILL.md`, `platforms/claude-code/generator.md`, `skills/upgrade/SKILL.md` | Supplied runtime findings: [RT-RTE-setup-generation](runtime.md#rt-rte-setup-generation), [RT-RTE-skill-upgrade](runtime.md#rt-rte-skill-upgrade), [RT-CLM-generation-paths](runtime.md#rt-clm-generation-paths). No generated deployment evidence. |
| Seed, pipeline, serial/parallel ralph | `skill-sources/seed/SKILL.md`, `skill-sources/pipeline/SKILL.md`, `skill-sources/ralph/SKILL.md` | Supplied runtime findings: [RT-RTE-source-processing](runtime.md#rt-rte-source-processing), [RT-RTE-parallel-claims](runtime.md#rt-rte-parallel-claims), [RT-CLM-completion-gate](runtime.md#rt-clm-completion-gate). Direct edits and missing handoffs are material bypasses. |
| Reduce extraction/admission/provenance | `skill-sources/reduce/SKILL.md` | Direct selected sections: classification, approval, note format, provenance; scoped search of gates and extraction modes. [EPI-RTE-reduce-content](#epi-rte-reduce-content), [EPI-RTE-reduce-admission](#epi-rte-reduce-admission). Configurable strict mode is a countercase to universal permissiveness. |
| Learn research filing | `skill-sources/learn/SKILL.md` | Direct steps 1–6; [EPI-RTE-learn-import](#epi-rte-learn-import). Tool returns and provider interpretation unavailable; acquisition is distinct from target-side synthesis. |
| Reflect connection/synthesis/tensions | `skill-sources/reflect/SKILL.md` | Direct articulation, synthesis opportunity, quality gates and conflicting-note sections; scoped search elsewhere. [EPI-RTE-reflect-check](#epi-rte-reflect-check), [EPI-RTE-reflect-use](#epi-rte-reflect-use). Retrieval internals uninspected. |
| Reweave criticism and replacement | `skill-sources/reweave/SKILL.md` | Direct claim evaluation, connection evaluation, admission and challenge logging; [EPI-RTE-reweave-check](#epi-rte-reweave-check), [EPI-RTE-reweave-revision](#epi-rte-reweave-revision). Enrichment-triggered continuation not fully inspected. |
| Verify and validate | `skill-sources/verify/SKILL.md`, `skill-sources/validate/SKILL.md` | Direct cold-read/schema/review and final chaining; validate metadata, checks and handoff. [EPI-RTE-verify-check](#epi-rte-verify-check), [EPI-RTE-verify-disposition](#epi-rte-verify-disposition). These do not test source truth. |
| Kernel validator | `reference/validate-kernel.sh` | Direct initial primitives and final summary; middle primitives uninspected. [EPI-RTE-kernel-check](#epi-rte-kernel-check). No full-kernel accuracy claim. |
| Remember | `skill-sources/remember/SKILL.md` | Direct explicit specification and session-mining steps; contextual confirmation from supplied runtime. [EPI-RTE-remember-policy](#epi-rte-remember-policy). Session transcript availability not established. |
| Ask | `skills/ask/SKILL.md` | Direct local methodology, answer synthesis and confidence policy; [EPI-RTE-ask-consumption](#epi-rte-ask-consumption). Earlier retrieval routing only searched, not fully traced. |
| Rethink, architect, reseed | `skill-sources/rethink/SKILL.md`, `skills/architect/SKILL.md`, `skills/reseed/SKILL.md` | Supplied [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution); direct scoped searches corroborate triage, rejection and evidence rules. Rethink's public scientific-method claim retained separately. |
| Session reload, Git retention, Stop capture | `hooks/scripts/session-orient.sh`, `hooks/scripts/auto-commit.sh`, `platforms/claude-code/hooks/session-capture.sh.template` | Supplied [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation), [RT-RTE-write-hooks](runtime.md#rt-rte-write-hooks). Full-body versus header-only loading must remain separate. |
| Health, recommend, graph, next, tasks, stats, refactor | `skills/health/SKILL.md`, `skills/recommend/SKILL.md`, `skill-sources/graph/SKILL.md`, `skill-sources/next/SKILL.md`, `skill-sources/tasks/SKILL.md`, `skill-sources/stats/SKILL.md`, `skill-sources/refactor/SKILL.md` | Health/recommend scoped searches only; remaining operations not directly assessed. Prevents exhaustive evaluator/cleanup/selection enumeration. |
| Other generation, guidance and corpus consumers | `generators/`, `platforms/shared/`, `presets/`, `methodology/`, `reference/`, `agents/knowledge-guide.md`, `skills/add-domain/SKILL.md`, `skills/reseed/SKILL.md` | Initial coverage in boundary/runtime, not comprehensive specialist reads. Corpus research warrant and every generated alternate cannot be established. Source-native reports remain attributed reported operation, not observed experiments. |

Consequential claims: [EPI-CLM-write-enforcement](#epi-clm-write-enforcement), [EPI-CLM-research-backing](#epi-clm-research-backing), [EPI-CLM-scientific-method](#epi-clm-scientific-method), [EPI-CLM-hypothesis-test](#epi-clm-hypothesis-test), and supplied [RT-CLM-completion-gate](runtime.md#rt-clm-completion-gate). No unqualified whole-system absence is inferred from this coverage.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-research-inbox](#epi-obj-research-inbox) | see record | see record | SRC-1 `skill-sources/learn/SKILL.md` | Imported service output and model synthesis have different warrant. |
| [EPI-OBJ-claim-notes](#epi-obj-claim-notes) | see record | see record | SRC-1 `skill-sources/reduce/SKILL.md` | OPEN/CLOSED is readiness classification, not evidence of accepted truth. |
| [EPI-OBJ-topic-maps](#epi-obj-topic-maps) | see record | see record | SRC-1 `skill-sources/reflect/SKILL.md` | Navigational grouping and opening synthesis are distinct operative parts within this container. |
| [EPI-OBJ-methodology-notes](#epi-obj-methodology-notes) | see record | see record | SRC-1 `skill-sources/remember/SKILL.md` | Directive authority does not establish its causal rationale. |
| [RT-OBJ-queue](runtime.md#rt-obj-queue) | none for phase/status fields; see record | see record | SRC-1 `skill-sources/ralph/SKILL.md` | Operational continuation does not establish claim acceptance. |
| [RT-OBJ-claude-md](runtime.md#rt-obj-claude-md) | see record; instructional container may include truth-apt rationale | see record | SRC-1 `skills/setup/SKILL.md` | No installed instance or invariant semantic preservation. |
| [RT-CMP-session-model](runtime.md#rt-cmp-session-model) | not determinable at accessible weight granularity | see record | SRC-1 `skill-sources/ralph/SKILL.md` | No accessible proposition inventory, parameter provenance or target-side training evidence. |

## Authority-route ledger

The table splits checks from disposition and retention from integration. Fields owned by declaring records are referenced with `see`. Architectural status describes the route, not successful compliance. Doctrine-only model procedures may request tool execution without implementing the semantic operation. Multiple rows for a container do not supersede its valid identity.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-learn-import](#epi-rte-learn-import) | content transformation | doctrine only | [EPI-OBJ-research-inbox](#epi-obj-research-inbox) | truth-apt transformation: acquisition/import | see [EPI-RTE-learn-import](#epi-rte-learn-import) | see [EPI-RTE-learn-import](#epi-rte-learn-import) | see [EPI-RTE-learn-import](#epi-rte-learn-import) | see [EPI-RTE-learn-import](#epi-rte-learn-import) | see [EPI-RTE-learn-import](#epi-rte-learn-import) | No newly established warrant for external assertions | Allows later extraction | Model, inbox file, permissive, later processing | SRC-1 `skill-sources/learn/SKILL.md` | none | none | Provider and target-side themed synthesis remain semantically indeterminate |
| [EPI-RTE-reduce-content](#epi-rte-reduce-content) | content transformation | doctrine only | [EPI-OBJ-claim-notes](#epi-obj-claim-notes) | truth-apt transformation: indeterminate | see [EPI-RTE-reduce-content](#epi-rte-reduce-content) | see [EPI-RTE-reduce-content](#epi-rte-reduce-content) | see [EPI-RTE-reduce-content](#epi-rte-reduce-content) | see [EPI-RTE-reduce-content](#epi-rte-reduce-content) | see [EPI-RTE-reduce-content](#epi-rte-reduce-content) | Attribution chain, not validation of premises | Candidate for approval and later linking | Human/model, findings/task files, advisory, current batch | SRC-1 `skill-sources/reduce/SKILL.md` | none | none | Acquisition edge distinguishable; body expansion may reshape, derive or conjecture |
| [EPI-RTE-reduce-admission](#epi-rte-reduce-admission) | disposition/acceptance | doctrine only | [EPI-OBJ-claim-notes](#epi-obj-claim-notes) | no content change | see [EPI-RTE-reduce-admission](#epi-rte-reduce-admission) | see [EPI-RTE-reduce-admission](#epi-rte-reduce-admission) | see [EPI-RTE-reduce-admission](#epi-rte-reduce-admission) | see [EPI-RTE-reduce-admission](#epi-rte-reduce-admission) | see [EPI-RTE-reduce-admission](#epi-rte-reduce-admission) | Approval for inclusion/use as notes; no evidenced semantic acceptance instance | Permits creation | Human to model, approval conversation, permissive, batch | SRC-1 `skill-sources/reduce/SKILL.md` | none | none | Pipeline dontAsk conflict remains in supplied runtime |
| [EPI-RTE-reflect-check](#epi-rte-reflect-check) | check/evidence production | doctrine only | [EPI-OBJ-topic-maps](#epi-obj-topic-maps) | no content change | see [EPI-RTE-reflect-check](#epi-rte-reflect-check) | see [EPI-RTE-reflect-check](#epi-rte-reflect-check) | see [EPI-RTE-reflect-check](#epi-rte-reflect-check) | see [EPI-RTE-reflect-check](#epi-rte-reflect-check) | see [EPI-RTE-reflect-check](#epi-rte-reflect-check) | Claimed meaningful relationship, not truth of linked premises | Informs connection editing | Model, skill report, advisory, current connection round | SRC-1 `skill-sources/reflect/SKILL.md` | none | none | No independent reference link set |
| [EPI-RTE-reflect-use](#epi-rte-reflect-use) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-topic-maps](#epi-obj-topic-maps) | truth-apt transformation: indeterminate | see [EPI-RTE-reflect-use](#epi-rte-reflect-use) | see [EPI-RTE-reflect-use](#epi-rte-reflect-use) | see [EPI-RTE-reflect-use](#epi-rte-reflect-use) | see [EPI-RTE-reflect-use](#epi-rte-reflect-use) | see [EPI-RTE-reflect-use](#epi-rte-reflect-use) | Navigational admission; ampliative acceptance not demonstrated | Later traversal paths and framing changed | Later models, map prose/wiki links, advisory/ranking, later work | SRC-1 `skill-sources/reflect/SKILL.md` | none | none | Not lifecycle integration under an evidenced prior acceptance |
| [EPI-RTE-reweave-check](#epi-rte-reweave-check) | check/evidence production | doctrine only | [EPI-OBJ-claim-notes](#epi-obj-claim-notes) | no content change | see [EPI-RTE-reweave-check](#epi-rte-reweave-check) | see [EPI-RTE-reweave-check](#epi-rte-reweave-check) | see [EPI-RTE-reweave-check](#epi-rte-reweave-check) | see [EPI-RTE-reweave-check](#epi-rte-reweave-check) | see [EPI-RTE-reweave-check](#epi-rte-reweave-check) | Relative consistency with vault evidence, whose warrant is unresolved | Informs revision proposal | Model/human, proposal/task section, advisory, revision round | SRC-1 `skill-sources/reweave/SKILL.md` | [EPI-CLM-hypothesis-test](#epi-clm-hypothesis-test) | none | Current vault content is not an independent empirical test |
| [EPI-RTE-reweave-revision](#epi-rte-reweave-revision) | content transformation | doctrine only | [EPI-OBJ-claim-notes](#epi-obj-claim-notes) | truth-apt transformation: indeterminate | see [EPI-RTE-reweave-revision](#epi-rte-reweave-revision) | see [EPI-RTE-reweave-revision](#epi-rte-reweave-revision) | see [EPI-RTE-reweave-revision](#epi-rte-reweave-revision) | see [EPI-RTE-reweave-revision](#epi-rte-reweave-revision) | see [EPI-RTE-reweave-revision](#epi-rte-reweave-revision) | Evidence-linked changed reliance is specified, not observed | Permits replacing note text and downstream use | Later model, note plus links, advisory, future retrieval | SRC-1 `skill-sources/reweave/SKILL.md` | [EPI-CLM-hypothesis-test](#epi-clm-hypothesis-test) | none | No distinct evidence-consuming acceptance instance; revision may change meaning |
| [EPI-RTE-verify-check](#epi-rte-verify-check) | check/evidence production | doctrine only | [EPI-OBJ-claim-notes](#epi-obj-claim-notes) | no content change | see [EPI-RTE-verify-check](#epi-rte-verify-check) | see [EPI-RTE-verify-check](#epi-rte-verify-check) | see [EPI-RTE-verify-check](#epi-rte-verify-check) | see [EPI-RTE-verify-check](#epi-rte-verify-check) | see [EPI-RTE-verify-check](#epi-rte-verify-check) | License concerns findability and shape, not assertion truth | Feeds completion decision or correction | Model lead, verification report/handoff, advisory, batch | SRC-1 `skill-sources/verify/SKILL.md` | none | none | Unavailable retrieval is deferred; no host trace |
| [EPI-RTE-verify-disposition](#epi-rte-verify-disposition) | disposition/acceptance | doctrine only | [EPI-OBJ-claim-notes](#epi-obj-claim-notes) | no content change | see [EPI-RTE-verify-disposition](#epi-rte-verify-disposition) | see [EPI-RTE-verify-disposition](#epi-rte-verify-disposition) | see [EPI-RTE-verify-disposition](#epi-rte-verify-disposition) | see [EPI-RTE-verify-disposition](#epi-rte-verify-disposition) | see [EPI-RTE-verify-disposition](#epi-rte-verify-disposition) | Readiness for vault processing, not truth acceptance | Allows completion/archive or demands fixes | Lead, handoff/queue, permissive, batch | SRC-1 `skill-sources/verify/SKILL.md` | none | see supplied completion claim | Done alone insufficient |
| [EPI-RTE-hook-shape](#epi-rte-hook-shape) | check/evidence production | implemented | [EPI-OBJ-claim-notes](#epi-obj-claim-notes) | truth-apt transformation: entailed derivation | see [EPI-RTE-hook-shape](#epi-rte-hook-shape) | see [EPI-RTE-hook-shape](#epi-rte-hook-shape) | see [EPI-RTE-hook-shape](#epi-rte-hook-shape) | see [EPI-RTE-hook-shape](#epi-rte-hook-shape) | see [EPI-RTE-hook-shape](#epi-rte-hook-shape) | Predicate result only within scanned text domain | Does not undo or block note | Host/model, warning JSON, advisory, current tool return | SRC-1 `hooks/scripts/write-validate.sh` | [EPI-CLM-write-enforcement](#epi-clm-write-enforcement) | Overbroad every-write enforcement claim | Malformed YAML and false propositions can pass |
| [EPI-RTE-kernel-check](#epi-rte-kernel-check) | check/evidence production | implemented | [EPI-OBJ-claim-notes](#epi-obj-claim-notes) | truth-apt transformation: entailed derivation | see [EPI-RTE-kernel-check](#epi-rte-kernel-check) | see [EPI-RTE-kernel-check](#epi-rte-kernel-check) | see [EPI-RTE-kernel-check](#epi-rte-kernel-check) | see [EPI-RTE-kernel-check](#epi-rte-kernel-check) | see [EPI-RTE-kernel-check](#epi-rte-kernel-check) | Only inspected predicates, not successful knowledge system | May inform repair; no checked admission consumer | Caller, stdout/exit, advisory, current validation | SRC-1 `reference/validate-kernel.sh` | none | none | Middle primitives uninspected; PASS labels overstate first-line test |
| [EPI-RTE-remember-policy](#epi-rte-remember-policy) | behavior/policy adaptation | doctrine only | [EPI-OBJ-methodology-notes](#epi-obj-methodology-notes) | non-truth-apt policy/content update: behavior directive from friction | see [EPI-RTE-remember-policy](#epi-rte-remember-policy) | see [EPI-RTE-remember-policy](#epi-rte-remember-policy) | see [EPI-RTE-remember-policy](#epi-rte-remember-policy) | see [EPI-RTE-remember-policy](#epi-rte-remember-policy) | see [EPI-RTE-remember-policy](#epi-rte-remember-policy) | Normative authority for intended behavior, not causal truth | Changes future instructions/drift reference | Model/meta-skills, full methodology reads, advisory, future sessions | SRC-1 `skill-sources/remember/SKILL.md` | none | none | Hook supplies headers only; mining requires unavailable transcript-rich Markdown |
| [EPI-RTE-ask-consumption](#epi-rte-ask-consumption) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-methodology-notes](#epi-obj-methodology-notes) | truth-apt transformation: indeterminate | see [EPI-RTE-ask-consumption](#epi-rte-ask-consumption) | see [EPI-RTE-ask-consumption](#epi-rte-ask-consumption) | see [EPI-RTE-ask-consumption](#epi-rte-ask-consumption) | see [EPI-RTE-ask-consumption](#epi-rte-ask-consumption) | see [EPI-RTE-ask-consumption](#epi-rte-ask-consumption) | Attributed support; absent confidence treated established without demonstrated evaluation | Changes guidance provided to user | Model/user, synthesized answer, advisory, current question | SRC-1 `skills/ask/SKILL.md` | [EPI-CLM-research-backing](#epi-clm-research-backing) | Confidence is not warrant | Research corpus validity and answer entailment unresolved |
| [RT-RTE-write-hooks](runtime.md#rt-rte-write-hooks) | retention | implemented | see record | no content change | see record | see record | see record | see record | see record | Git persistence grants no semantic endorsement | see record | see record | SRC-1 `hooks/scripts/auto-commit.sh` | none | none | Committed invalid content remains possible. |
| [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation) | operational admission/selection/consumption | implemented | see record | truth-apt transformation: non-ampliative reshaping | see record | see record | see record | see record | see record | Header excerpt selection does not license omitted body | see record | see record | SRC-1 `hooks/scripts/session-orient.sh` | none | none | Delivery, not activation. |
| [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution) | behavior/policy adaptation | doctrine only | see record | non-truth-apt policy/content update: approved operating assumptions | see record | see record | see record | see record | see record | Proposed evidence-responsive method change, not warranted benefit | see record | see record | SRC-1 `skill-sources/rethink/SKILL.md` | [EPI-CLM-scientific-method](#epi-clm-scientific-method) | none | Human veto and missing outcome comparison remain independent. |
| [RT-RTE-setup-generation](runtime.md#rt-rte-setup-generation) | content transformation | doctrine only | see record | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Research-guided configuration proposal, not source truth or verified derivation | see record | see record | SRC-1 `skills/setup/SKILL.md` | [EPI-CLM-research-backing](#epi-clm-research-backing) | see generation-path claim | LLM vocabulary transformation is not guaranteed semantics-preserving. |
| [RT-RTE-skill-upgrade](runtime.md#rt-rte-skill-upgrade) | behavior/policy adaptation | doctrine only | see record | non-truth-apt policy/content update: selected successor skills | see record | see record | see record | see record | see record | Approved deployment of instruction successor, not evidence of improved capability | see record | see record | SRC-1 `skills/upgrade/SKILL.md` | none | see generation-path claim | Manual rollback is not automatic withdrawal. |

No lifecycle-integration row is established by an evidenced accepted claim instance in these inspected routes. Linking and use are present as specified operations; they are not relabelled acceptance. This is a limit, not a system-complete absence.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-write-enforcement](#epi-clm-write-enforcement) | see record | SRC-1 `README.md`; doctrine/design | Hook warning design | [EPI-RTE-hook-shape](#epi-rte-hook-shape), [RT-RTE-write-hooks](runtime.md#rt-rte-write-hooks) | none supplied | Post-effect, Write-only, path-limited, zero exit | Limited advisory shape checking is implemented | Every-write enforcing guarantee unsupported |
| [EPI-CLM-research-backing](#epi-clm-research-backing) | see record | SRC-1 `README.md`, `skills/ask/SKILL.md`; doctrine/design | Setup/ask/architect prescribe research citation | see [RT-RTE-setup-generation](runtime.md#rt-rte-setup-generation); semantic routes doctrine only | none supplied | No independent evaluation of corpus or choice-to-evidence chain | Research-guided proposal and attributed answers are specified | Citation/metadata does not establish source warrant or causal mechanism |
| [EPI-CLM-scientific-method](#epi-clm-scientific-method) | see record | SRC-1 `skill-sources/rethink/SKILL.md`; doctrine/design | Evidence, quoted assumptions, human selection and retention | see [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution); semantic route doctrine only | none supplied | No exercised intervention/comparison or subsequent benefit | Explicit criticism/adaptation design | Scientific-method analogy does not establish causal testing |
| [EPI-CLM-hypothesis-test](#epi-clm-hypothesis-test) | see record | SRC-1 `skill-sources/reweave/SKILL.md`; doctrine/design | New evidence can qualify or replace old claim and log challenge | [EPI-RTE-reweave-check](#epi-rte-reweave-check), [EPI-RTE-reweave-revision](#epi-rte-reweave-revision), doctrine only | none supplied | Vault evidence may itself be conjectural/imported; no independent oracle | Content-directed criticism is specified, not merely backlinking | Every reweave need not test truth; may only clarify/link |
| [RT-CLM-completion-gate](runtime.md#rt-clm-completion-gate) | see record | SRC-1 `skill-sources/verify/SKILL.md`, `skill-sources/ralph/SKILL.md`; doctrine/design | see record | [EPI-RTE-verify-disposition](#epi-rte-verify-disposition), doctrine only | none supplied | see record | Queue completion cannot substitute for evaluated readiness | Instruction-level bypass, not observed failure |
| [RT-CLM-generation-paths](runtime.md#rt-clm-generation-paths) | see record | SRC-1 `skills/setup/SKILL.md`, `platforms/claude-code/generator.md`; doctrine/design | see record | see record | none supplied | see record | Installed skill freshness/authority requires deployment evidence | Copied versus inherited contradiction retained |

## Bounded conclusion

Ars Contexta specifies acquisition of external research and source-to-note processing, preserving a source footer and query lineage. That lineage supports attribution, not external truth. Learn uses `exa_prompt` while reduce's preservation guidance names `research_prompt`; automatic uniform query-field preservation across this interface is not established. Model-written themed findings, note reasoning, scope revisions and map syntheses are truth-apt transformations whose preservation/entailment remains indeterminate without concrete produced artifacts and inputs. The synthesis-opportunity branch explicitly proposes an uncaptured higher-order argument; it is candidate generation, not accepted new knowledge. No warranted-premise semantic deduction is established. The deterministic deductions here concern bounded text predicates, not claims in the notes.

Admission is heterogeneous. Reduce prescribes user approval for extracted files; that decision concerns inclusion and readiness under extraction criteria. Reflect uses model articulation and traversal utility, removes failed links and flags contradictions without automatic resolution. Reweave compares old claims with newer vault evidence and records changed positions; interactive changes need approval, handoff changes do not. These routes can change retained reliance but provide no observed evidence-consuming acceptance of an ampliative claim for a named use and scope. Their semantic criteria must not be replaced by the narrower verify readiness criterion.

Verify's criterion is cold-read prediction score at least three plus no FAIL-level structural/graph issue, for use as a process-ready note. Its requested operational force is holding at verify on failure and allowing completion on success. RALPH's missing-handoff continuation weakens that gate. Standalone validate is non-blocking. Neither tests the factual assertions against the external world. The hook's implemented force is weaker still: it warns after a Write and exits zero. Git retention can preserve such a candidate without admission, endorsement or lifecycle integration.

Remember may directly turn friction into authoritative directives; contextual interpretation requires confirmation, whereas mining specifies model classification before writing. The intended consumer is future sessions and meta-skills reading methodology; the automatic hook exposes only headers. Ask rereads accumulated local methodology for later questions; its full-body local-methodology precedence gives these directives further answer authority. This is retained-input read-back, not an established persistent answer writer. This policy path exists independently of a truth-acceptance route or improved-capacity evidence. Rethink/architect specify a criticism-and-approved-revision loop for the operating system; supplied runtime establishes separate claimed theory-builder conditions and a dormant improvement-directed pathway, not exercised self-improvement. Reweave independently specifies addressable claim criticism and retained revision. Neither opacity of the model nor missing runs proves these capacities absent.

Execution, benefit and causal transfer remain unobserved. The relevant uninspected operations and corpus consumers in the coverage table prevent a system-complete negative about other checks or acceptance. No single system-wide epistemic verdict follows.

## Shared records

### Operative objects

#### EPI-OBJ-research-inbox
Label: Research inbox findings

Source-native identity: learn's `YYYY-MM-DD-[slugified-topic].md` inbox file. Natural-language findings and source URLs plus symbolic provenance fields; filesystem Markdown substrate. Candidate truth-apt content: tool-reported propositions and model-themed findings. Role: input for reduce and research-direction discovery. No counterpart after comparison with [RT-OBJ-queue](runtime.md#rt-obj-queue) and [RT-OBJ-claude-md](runtime.md#rt-obj-claude-md): source content is neither task state nor operating instruction container. SRC-1 `skill-sources/learn/SKILL.md`; doctrine/design.

> [Synthesized findings organized by theme, not by source. Each finding
> should be a clear proposition the reduce phase can extract as an atomic insight.]
> --- `skill-sources/learn/SKILL.md`

#### EPI-OBJ-claim-notes
Label: Atomic claim notes

Source-native identity: reduce's proposition-titled notes in the configured notes directory. Natural-language assertions, reasons and uncertainty consumed semantically; symbolic frontmatter and wiki pointers consumed for routing/checks; filesystem Markdown substrate. Role: retained candidate claims used by reflect/reweave/verify. Distinct from [RT-OBJ-queue](runtime.md#rt-obj-queue): the queue references work, not the full claim note. Also distinct from [RT-OBJ-claude-md](runtime.md#rt-obj-claude-md), which governs work. SRC-1 `skill-sources/reduce/SKILL.md`; doctrine/design. OPEN/CLOSED classifies processing readiness rather than witnessed truth acceptance.

> - **CLOSED** — standalone claim, design decision, ready for processing as-is
> - **OPEN** — needs more investigation, testable hypothesis, requires evidence
> --- `skill-sources/reduce/SKILL.md`

#### EPI-OBJ-topic-maps
Label: Topic maps and opening synthesis

Source-native identity: reflect's configured topic-map files. Natural-language opening arguments and relationship context coexist with symbolic wiki-link navigation; substrate: filesystem Markdown. Truth-apt part: relationship explanations and opening synthesis, not membership alone. Role: later traversal and framing. Distinct from [RT-OBJ-queue](runtime.md#rt-obj-queue) and [RT-OBJ-claude-md](runtime.md#rt-obj-claude-md): domain navigation rather than task progress or operating instructions. SRC-1 `skill-sources/reflect/SKILL.md`; doctrine/design.

> [Opening synthesis: Claims about the topic. Not "this {vocabulary.topic_map} collects {vocabulary.note_plural}" but "the core insight is Y because Z." This IS thinking, not meta-description.]
> --- `skill-sources/reflect/SKILL.md`

#### EPI-OBJ-methodology-notes
Label: Canonical methodology directives

Source-native identity: `ops/methodology/` notes and `ops/methodology.md` navigation. Natural-language DO/DON'T/scope and causal rationale; symbolic source/category/status fields; filesystem Markdown substrate. Normative directive is not itself a truth claim; its friction account and why-this-matters rationale can be truth-apt. Role: canonical intended behavior and drift reference. Distinct from [RT-OBJ-claude-md](runtime.md#rt-obj-claude-md): these separately maintained notes can contradict or supersede earlier derivation rationale and feed meta-skills. Relevant consumer counterpart: [RT-BAP-context-instructions](runtime.md#rt-bap-context-instructions), not duplicate object identity. SRC-1 `skill-sources/remember/SKILL.md`; doctrine/design.

> **Rule Zero:** This methodology note becomes part of the system's canonical specification. ops/methodology/ is not a log of what happened — it is the authoritative declaration of how the system should behave. Write this note as a directive: what the agent SHOULD do, not what went wrong. Future sessions, /rethink drift checks, and meta-skills will consult this note as ground truth for system behavior.
> --- `skill-sources/remember/SKILL.md`

### Routes

#### EPI-RTE-learn-import
Label: Learn research acquisition

No counterpart after comparison with the supplied runtime routes; this entry point and consumer are distinct from runtime setup/source-processing containers.

Research tools → inbox → later reduce; the invoking model selects depth and handles failed/empty results through a tool cascade. Source success is not a factual answer oracle. Open research mode; model files and formats results without a separate human approval dialog in the inspected steps. Proposed updates include findings and goals directions; all-tool failure stops research. Source URLs/query metadata persist; no tested rollback. Acquisition and target-side synthesis are distinct edges: only the former is classified import. SRC-1 `skill-sources/learn/SKILL.md`; doctrine/design.

- Immediate return: Filed findings and source/tool metadata; goals directions when applicable.
- Later read-back: Later reduce reads the inbox file; goals may seed another research invocation.
- Delegated visibility: uninspected — no delegated execution supplied.
- Selection predicate: Selected query/depth, configured tool priority, successful/nonempty return.
- Invalidation or expiry: Later edits or processing change the file; no evidence-based expiration specified.
- Activation or effect: Requested tool calls and writes; no executed service result or later compliance.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> 4. **File to inbox** — with full provenance metadata
> 5. **Chain to processing** — next step based on pipeline chaining mode
> 6. **Update goals.md** — append new research directions discovered
> --- `skill-sources/learn/SKILL.md`

#### EPI-RTE-reduce-content
Label: Reduce source to note

Part of: [RT-RTE-source-processing](runtime.md#rt-rte-source-processing)

Model reads source and writes approved claim title/body with reasoning, uncertainty, counterargument and attribution. Source → proposed extraction → note is not demonstrated non-ampliative compression. No accepted ampliative instance or checked semantic derivation follows. This part transforms content; the separate admission part controls writing. SRC-1 `skill-sources/reduce/SKILL.md`; doctrine/design.

- Immediate return: Candidate titles, findings report, task/note text.
- Later read-back: Notes and archived source support later reflect/reweave and retrieval.
- Delegated visibility: uninspected — no worker output supplied.
- Selection predicate: Domain relevance, extraction categories, near-duplicate enrichment and configurable gate.
- Invalidation or expiry: Reweave/enrichment can revise; no universal expiry specified.
- Activation or effect: Requested semantic extraction and file creation after approval.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> Acknowledge uncertainty where appropriate.
> Consider the strongest counterargument.
> Show the path to the conclusion, not just the conclusion.
> --- `skill-sources/reduce/SKILL.md`

#### EPI-RTE-reduce-admission
Label: Reduce extraction approval

Part of: [RT-RTE-source-processing](runtime.md#rt-rte-source-processing)

Model proposes extraction; human approves or declines files. Guidance: relevant-source comprehensive extraction and content-quality checks; strict configuration is a narrower alternate. No expected truth answer is provided. Open processing mode. Approved notes persist; declined proposals need not be written. This is inclusion authority, not observed semantic acceptance. Queue mode does not remove approval per supplied runtime; dontAsk conflict remains. SRC-1 `skill-sources/reduce/SKILL.md`; doctrine/design.

- Immediate return: Approved/declined candidate selection before creation.
- Later read-back: Approved notes can enter later processing; rejected proposal retention unspecified.
- Delegated visibility: uninspected — host/worker admission dialogue unavailable.
- Selection predicate: Human response to findings; relevance and note-quality criteria.
- Invalidation or expiry: Later evidence/revision may replace retained text; approval has no stated expiry.
- Activation or effect: Requested permission to write; no observed approval.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> **Wait for user approval before creating files.** Never auto-extract.
> --- `skill-sources/reduce/SKILL.md`

#### EPI-RTE-reflect-check
Label: Reflect relationship evaluation

Part of: [RT-RTE-source-processing](runtime.md#rt-rte-source-processing)

Model proposes relationships and decides which pass substantive articulation and agent traversal utility. Domain: semantic relationship and usefulness, with file existence as auxiliary check. No independent reference answer. Open connection work. This evaluation informs a separate edit/disposition route. Reject unarticulated links; unresolved contradictions are flagged, not resolved. SRC-1 `skill-sources/reflect/SKILL.md`; doctrine/design.

- Immediate return: Articulation/utility/coherence decisions and tension flags.
- Later read-back: Connection reports may inform reweave; actual later report consumption unobserved.
- Delegated visibility: uninspected — no model evaluation trace.
- Selection predicate: Candidate neighbors and existing topic maps; config quick mode can skip synthesis detection.
- Invalidation or expiry: Subsequent reflect/reweave may reconsider links.
- Activation or effect: Requested evaluation, not demonstrated correctness.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> If you cannot fill in [specific reason] with something substantive, the connection fails.
> --- `skill-sources/reflect/SKILL.md`

#### EPI-RTE-reflect-use
Label: Reflect connection and map use

Part of: [RT-RTE-source-processing](runtime.md#rt-rte-source-processing)

Model consumes connection checks to add/remove links and revise map openings. Guidance includes prose, bidirectional and coherence gates. No separate human per-link veto in this worker path. Candidate links may be rejected/removed. Contradicting notes retain both positions for judgment. New standalone synthesis is flagged, not written here; map-opening synthesis can nonetheless change. This is graph use before an evidenced truth-acceptance decision, not lifecycle integration. SRC-1 `skill-sources/reflect/SKILL.md`; doctrine/design.

- Immediate return: Edited links/maps; synthesis opportunity report.
- Later read-back: Later vault traversal sees revised edges and opening synthesis.
- Delegated visibility: uninspected — no worker returns supplied.
- Selection predicate: Passed articulation/utility, map coherence and existing targets.
- Invalidation or expiry: Failed links removed; later contradictory evidence can alter map.
- Activation or effect: Requested editing and navigation change; no observed next-round use.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> 1. Document the tension in both {vocabulary.note_plural}
> 2. Add to {vocabulary.topic_map} Tensions section
> 3. Do not auto-resolve — flag for judgment
> --- `skill-sources/reflect/SKILL.md`

#### EPI-RTE-reweave-check
Label: Reweave claim criticism

Part of: [RT-RTE-source-processing](runtime.md#rt-rte-source-processing)

Model judges old claim against newer notes/evidence, distinguishing supported, vague, broad, partially wrong and contradicted. No independent empirical oracle; newer vault claims may be unwarranted. Open revision mode. This part produces criticism; separate revision changes the retained candidate. Human approval applies in interactive mode, not handoff. See the separate revision record for theory account. SRC-1 `skill-sources/reweave/SKILL.md`; doctrine/design.

- Immediate return: Finding and proposed revision/tension.
- Later read-back: Criticism may be logged in task section and used in later revisions.
- Delegated visibility: uninspected — no worker criticism supplied.
- Selection predicate: Target older note plus relevant newer notes/backlinks.
- Invalidation or expiry: Newer evidence or revision can supersede judgment.
- Activation or effect: Requested content-directed criticism; no actual criticized instance supplied.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> | Claim is partially wrong | Revise with nuance |
> | Claim is contradicted | Flag tension, propose revision |
> --- `skill-sources/reweave/SKILL.md`

#### EPI-RTE-reweave-revision
Label: Reweave evidence linked revision

Part of: [RT-RTE-source-processing](runtime.md#rt-rte-source-processing)

Model proposes/executes successor note; human decides interactive mode; handoff authorizes direct application. Guidance: claim assessment and articulated links, with explicit challenge history. Rejection is possible interactively; no atomic rollback is established. Revised claim and evidence links persist. No uniform truth-acceptance criterion is named beyond comparison with current vault evidence. SRC-1 `skill-sources/reweave/SKILL.md`; doctrine/design.

- Immediate return: Revised note, links and logged original/evidence/revised position.
- Later read-back: Later reflect/reweave and retrieval use the revised note.
- Delegated visibility: uninspected — no revision execution supplied.
- Selection predicate: Criticism identifies changed claim, framing, scope or links; execution mode controls approval.
- Invalidation or expiry: Later reweave/enrichment replaces the live note; history logging is requested.
- Activation or effect: Requested successor writing; no exercised influence or benefit.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> **For pipeline execution (--handoff mode):** Apply changes directly. The pipeline needs to proceed without waiting for approval.
> 
> **For interactive execution (no --handoff):** Present the reweave proposal first, then apply after approval.
> --- `skill-sources/reweave/SKILL.md`

Theory account: target is the old note's explicit claim and its scope. Newer evidence can criticize and revise it rather than merely add retrieval links. Retained material includes original claim, new evidence and revised position in the task section, plus the live revised note. Addressability is at note/claim granularity, with title and scope separately editable; finer premise separation uninspected. Persistence is specified across later vault operations, not an observed horizon.

theory-builder conditions 1–4:
- condition 1 conclusion status: claimed
  A proposition-titled note supplies localized theory content.
- condition 2 conclusion status: claimed
  Evaluation and revision are instructed to depend on what that claim says.
- condition 3 conclusion status: claimed
  Contradicting evidence can challenge the original claim and change its scope or position; no performed blame assignment supplied.
- condition 4 conclusion status: claimed
  Revised claim and challenge history are retained for later vault work; actual next-round influence unobserved.

learning: uninspected — no future-capacity improvement or attribution evidence. Reflection: uninspected for this route — ordinary user-domain note criticism does not itself establish a self-representation of the operating system. Reflective theory builder: uninspected for this same reason; do not confuse it with supplied rethink findings. Autonomous theory builder: not established across this route's modes because interactive approval is an internal admission operation; handoff permits computational application but no complete operation trace is supplied. Self-improvement is not attributed to domain-note revision alone.

> **Always log challenges:** When a claim is challenged or revised, this is a significant event. Note it in the task file Reweave section with the original claim, the new evidence, and the revised position.
> --- `skill-sources/reweave/SKILL.md`

#### EPI-RTE-verify-check
Label: Verify usability and schema

Part of: [RT-RTE-source-processing](runtime.md#rt-rte-source-processing)

Model predicts note from title/description before reading full body, scores agreement, checks template/schema, links and map membership; optional qmd rank tests retrieval. Prediction/body contrast is a reference for descriptive fidelity, not source truth. Model may propose/apply description repair. Open note-quality checking; external search failure permits deferred retrieval. Standalone validate is a distinct non-blocking schema procedure with Read/Grep/Glob metadata, not a guaranteed repair tool. SRC-1 `skill-sources/verify/SKILL.md`; doctrine/design.

- Immediate return: Prediction/score, retrieval rank or deferred status, PASS/WARN/FAIL.
- Later read-back: Quality/task reports can guide future repairs; actual later consumption unavailable.
- Delegated visibility: uninspected — no cold-read trace or search result supplied.
- Selection predicate: Configured checks and specified note/all/recent selection.
- Invalidation or expiry: Edits invalidate old quality results; no automatic expiry implementation.
- Activation or effect: Requested diagnosis/description improvement, not semantic warrant.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> This step tests whether the title + description alone enable an agent to predict the note's content. The cold-read constraint is the entire point — reading the note first contaminates the prediction.
> --- `skill-sources/verify/SKILL.md`

#### EPI-RTE-verify-disposition
Label: Verify completion disposition

Part of: [RT-RTE-source-processing](runtime.md#rt-rte-source-processing)

Model consumes verification results: recite score below three or FAIL holds task at verify; manual/suggested/automatic modes differ in done signaling. Permissive completion intended for ready notes, not accepted truth. RALPH missing-handoff branch may instead mark done. Human timing choice in manual mode is not per-claim truth approval. Recovery: fix and rerun; no rollback of original note write. SRC-1 `skill-sources/verify/SKILL.md`; doctrine/design.

- Immediate return: Completion summary or failure/fix instruction and retained verify phase.
- Later read-back: Persisted queue permits later repair invocation; done notes remain usable.
- Delegated visibility: uninspected — no lead response to verification supplied.
- Selection predicate: Verification threshold, FAIL issues and chaining mode; driver may bypass.
- Invalidation or expiry: Rerun after fixes; done state may be archived.
- Activation or effect: Requested readiness gate with conflicting continuation policy.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> If verification FAILS (recite score < 3 or any FAIL-level issue), do NOT mark done. Instead:
> - Output what failed and what needs fixing
> - Keep task at `current_phase: "verify"` for re-run after fixes
> --- `skill-sources/verify/SKILL.md`

#### EPI-RTE-hook-shape
Label: Post Write shape predicates

Part of: [RT-RTE-write-hooks](runtime.md#rt-rte-write-hooks)

Host dispatches Write callback; guarded shell derives warning strings from line-presence tests. Concrete static input trace, not executed: for an existing detected-vault file /v/notes/x.md beginning with --- then description: and topics: within twenty lines, even with an arbitrary false proposition below, each inspected predicate passes and no warning is emitted. Missing topics: appends Missing topics field. to warning JSON, then exits zero. Entailed result is about scanned text only; it cannot infer valid YAML, actual schema adherence or truth. Model/human can react, but no blocking or rollback consumer exists in this hook. SRC-1 `hooks/scripts/write-validate.sh`; implementation.

- Immediate return: Warning additionalContext JSON or no output; exit zero.
- Later read-back: inapplicable — warning output is not a retained revision; file retention belongs to the separate Git route.
- Delegated visibility: uninspected — host worker event propagation outside source.
- Selection predicate: Detected vault, existing file, extracted file path, notes/thinking path and Write event.
- Invalidation or expiry: inapplicable — no retained result invalidation policy in this callback.
- Activation or effect: Implemented post-effect advisory warning; operation unobserved.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if ! head -20 "$FILE" | grep -q "^topics:"; then
>       WARNS="${WARNS}Missing topics field. "
>     fi
> --- `hooks/scripts/write-validate.sh`

#### EPI-RTE-kernel-check
Label: Kernel structural evaluation

No counterpart after comparison with the supplied runtime routes; kernel CLI predicate evaluation is not the source-processing semantic evaluator.

Explicit caller supplies vault path; shell computes sampled presence/count predicates, emits summary and exits zero for warnings-only, one for FAIL. Concrete static deduction: a single eligible Markdown file whose first line is --- but has no closing delimiter contributes one to yaml_count, and zero missing yields the primitive-one PASS message. Therefore its all-with-YAML label warrants first-line presence only. No target execution. Caller interpretation is the available force; no inspected downstream admission consumer. Structural diagnosis has no semantic oracle; failure can motivate repair but does not undo content. SRC-1 `reference/validate-kernel.sh`; implementation.

- Immediate return: PASS/WARN/FAIL messages and summary exit status.
- Later read-back: inapplicable — script writes no retained evidence or corrected artifact.
- Delegated visibility: inapplicable — no delegation in this shell implementation.
- Selection predicate: Caller path and inspected file/directory/pattern tests; links deduplicated and sampled to first 100.
- Invalidation or expiry: inapplicable — each invocation recomputes; no stored result lifecycle.
- Activation or effect: Implemented predicate evaluation; no executed validator result.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> link_candidates=$(echo "$link_candidates" | sort -u | head -100)
> --- `reference/validate-kernel.sh`

#### EPI-RTE-remember-policy
Label: Remember friction to specification

No counterpart after comparison with the supplied runtime routes; this entry point and consumer are distinct from runtime setup/source-processing containers.

Explicit correction or session-mined pattern → model deduplication/classification → methodology directive or pending observation → future meta-skill consumption. This is distinct from the approval-based architecture route [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution): local directive admission does not require a system-wide proposal. Contextual mode requires user confirmation per [RT-BAP-context-instructions](runtime.md#rt-bap-context-instructions); mining classifies actionable guidance versus unresolved observation. No expected outcome oracle or tested improvement. Contradiction creates observation rather than automatically settling evidence. Model writes and sets mined markers; no tested rollback. Guidance and rationale persist; causality of rationale remains indeterminate. SRC-1 `skill-sources/remember/SKILL.md`; doctrine/design.

- Immediate return: Methodology notes/MOC updates or observations and mining markers.
- Later read-back: Future ask/rethink/meta-skills read full methodology; SessionStart supplies only recent headers, see [RT-RTE-session-orientation](runtime.md#rt-rte-session-orientation).
- Delegated visibility: uninspected — no delegated trace or transcript-rich session instance supplied.
- Selection predicate: Explicit friction, confirmed contextual interpretation or unmined Markdown session patterns; deduplication against prior notes.
- Invalidation or expiry: Later remember may extend; contradictions can trigger rethink. No automatic policy withdrawal established.
- Activation or effect: Requested durable directive update; consumer activation and capacity improvement unobserved.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> **For methodology findings:** Follow the same creation process as explicit mode (Step 3 in Explicit Mode section), with `source: session-mining` and add `session_source: [session filename]`.
> --- `skill-sources/remember/SKILL.md`

#### EPI-RTE-ask-consumption
Label: Ask scope dependent reliance

No counterpart after comparison with the supplied runtime routes; this entry point and consumer are distinct from runtime setup/source-processing containers.

User question → model reads bundled/local guidance → synthesized answer. Local methodology receives precedence for how-MY-system-works questions; research receives precedence for general comparison. The model drafts/decides answer and flags conflict rather than resolving by independent test. No expected factual answer oracle. Open questions; advice has no automatic file effect in these inspected sections. Distinct from [RT-BAP-context-instructions](runtime.md#rt-bap-context-instructions): full-body interpretive answer consumption, not host injection. Certainty metadata influences reporting without evidence-consuming acceptance being established. SRC-1 `skills/ask/SKILL.md`; doctrine/design.

- Immediate return: Cited answer with practical implications and tensions.
- Later read-back: Previous derivation and accumulated local methodology notes are reread for a later user question and inform requested answer synthesis; see [MEM-RTE-local-guidance](memory.md#mem-rte-local-guidance). No persistent answer writer is established by the inspected answer section.
- Delegated visibility: uninspected — no delegated answer trace.
- Selection predicate: User question scope and bundled claims; Step 5 loads all local methodology files, then relevance determines answer use; confidence and archived status labels influence reporting. No explicit active-only filter is established for the local-methodology read loop.
- Invalidation or expiry: Edits or supersession can change live retained guidance, but the local-methodology read loop has no explicit active-only filter; no retained answer invalidation route is specified.
- Activation or effect: Requested scope-sensitive answer framing, not observed truth or downstream user action.
- Evidence limits: Source procedure/code only; no supplied route execution or causal comparison.
- implementation conclusion status: claimed
- operation conclusion status: uninspected

> Read `ops/methodology/` for system-specific self-knowledge. Methodology notes may be more current than the derivation document — they capture ongoing operational learnings that the original derivation did not anticipate.
> --- `skills/ask/SKILL.md`

> - Methodology notes about system behavior are more authoritative for "how does MY system work" questions than the general research graph
> --- `skills/ask/SKILL.md`

Additional load-bearing interface and evaluation passages:

> exa_prompt: "[full query/instruction string sent to the research tool]"
> --- `skill-sources/learn/SKILL.md`

> When the source file contains provenance metadata (source_type, research_prompt, research_server, generated), preserve the chain:
> --- `skill-sources/reduce/SKILL.md`

> - Each created {vocabulary.note}'s Source footer links to the source file
> - The source file's YAML contains the research prompt
> - The chain: research query -> inbox file -> /{vocabulary.reduce} -> {vocabulary.notes}
> --- `skill-sources/reduce/SKILL.md`

> - Two {vocabulary.note_plural} make complementary arguments that combine into something neither says alone
> --- `skill-sources/reflect/SKILL.md`

> 2. Do NOT create the synthesis {vocabulary.note} during reflect — flag it for future work
> --- `skill-sources/reflect/SKILL.md`

> description: Schema validation for notes. Checks against domain-specific templates. Validates required fields, enum values, description quality, and link health. Non-blocking — warns but doesn't prevent capture. Triggers on "/validate", "/validate [note]", "check schema", "validate note", "validate all".
> --- `skill-sources/validate/SKILL.md`

### Claims

#### EPI-CLM-write-enforcement
Label: Every write structure enforcement

Claimed operation: hooks enforce structure on every write. SRC-1 `README.md`; doctrine/design. No counterpart after comparison with [RT-CLM-completion-gate](runtime.md#rt-clm-completion-gate): this is filesystem callback force, not phase success. Implementation countercase: [EPI-RTE-hook-shape](#epi-rte-hook-shape) and [RT-RTE-write-hooks](runtime.md#rt-rte-write-hooks).

> - **Automation** -- hooks that enforce structure on every write, detect maintenance
>   needs, capture session state, and auto-commit.
> --- `README.md`

#### EPI-CLM-research-backing
Label: Research traced choices and answers

Claimed warrant: every generated choice traces to research and ask answers should be evidence-based by using specific claims. SRC-1 `README.md`, `skills/ask/SKILL.md`; doctrine/design. Distinct from [RT-CLM-generation-paths](runtime.md#rt-clm-generation-paths): evidential justification rather than copied/inherited update mechanism. This supports intended citation discipline, not corpus validation.

> **The key differentiator:** derivation, not templating. Every choice traces to
> specific research claims. The engine reasons from principles about what your
> domain needs and why.
> --- `README.md`

> **Ground answers in specific claims, not general knowledge.** The knowledge base exists so answers are evidence-based. If you answer from general knowledge without consulting the graph, you are bypassing the tool.
> --- `skills/ask/SKILL.md`

> - No confidence field — standard established claim
> --- `skills/ask/SKILL.md`

#### EPI-CLM-scientific-method
Label: Rethink scientific method

Claimed operation: rethink applies scientific-method hypothesis/implementation/observation/revision to generated systems. SRC-1 `skill-sources/rethink/SKILL.md`; doctrine/design. Closest supplied [RT-RTE-architecture-evolution](runtime.md#rt-rte-architecture-evolution) records the associated route, not this public claim; no duplicate claim counterpart. Evidence-responsive criticism is specified; causal intervention/comparison is not established.

> This is the scientific method applied to knowledge systems: hypothesize, implement, observe, revise.
> --- `skill-sources/rethink/SKILL.md`

#### EPI-CLM-hypothesis-test
Label: Every reweave a test

Claimed operation: each note is a hypothesis and each reweave a test. SRC-1 `skill-sources/reweave/SKILL.md`; doctrine/design. Closest supplied [RT-RTE-source-processing](runtime.md#rt-rte-source-processing) is a route container; no counterpart claim. This differs from rethink's self-method criticism: user-domain claims may be revised against other vault content without testing the operating system.

> Reweaving is how knowledge stays alive. Not just connecting, but questioning, sharpening, splitting, rewriting. Every {vocabulary.note} is a hypothesis. Every reweave is a test.
> --- `skill-sources/reweave/SKILL.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; new routes state their paths, and generated instruction loading is owned by [RT-BAP-context-instructions](runtime.md#rt-bap-context-instructions).
