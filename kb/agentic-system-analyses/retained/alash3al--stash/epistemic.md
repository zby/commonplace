---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Stash epistemic routes: extraction, hypothesis assessment, admission and the limits of withdrawal at the frozen revision."
run-id: AAS-2026-10-15-stash-7ac5612837a0-01
reviewed-boundary: d34ed430c4348ef741ef95146b488aea8616f4fb
---

# Stash epistemic report

## Source-and-claim boundary

This report asks what licenses reliance on Stash's retained content, and what its checks actually change. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); the evidence identity is see [Source register](boundary.md#source-register), SRC-1. The target is the self-hosted memory system, including its shipped callers and maintenance. External clients' final answers, provider internals and the separate cloud implementation are excluded. All findings below are implementation or doctrine/design at the frozen commit, not observed execution or causal experiments.

The supplied runtime is a baseline, not an inspection limit. Direct reads added all reasoner methods, the secondary consolidation stages, hypothesis transitions, contradiction handling, causal operations, decay, fact getters and selectors, episode deletion, models and selected MCP handlers and protocol passages. Registry searches covered the frozen CLI dispatch and MCP registrations. The coverage table distinguishes those reads from inherited runtime findings. Source-native quality claims are see [EPI-CLM-fact-warrant](#epi-clm-fact-warrant), [EPI-CLM-memory-learning](#epi-clm-memory-learning), [EPI-CLM-hypothesis-verification](#epi-clm-hypothesis-verification) and [RT-CLM-session-protocol](runtime.md#rt-clm-session-protocol).

| Entry point or operation | SRC-1 source path | Coverage and records | Limit / conclusion prevented |
|---|---|---|---|
| CLI dispatch, Before initialization and tool registration | `cmd/cli/main.go`, `cmd/cli/mcp.go` | Direct registry search; bootstrap/hooks inherited from [RT-RTE-remember-write](runtime.md#rt-rte-remember-write) | Not a deployment or caller-adherence audit |
| Remember, recall, context and service triggers | `internal/brain/episode.go`, `internal/queries/recall.sql.tmpl`, `internal/brain/context.go`, `cmd/cli/consolidate.go`, `cmd/cli/serve_all.go` | Episode and recall SQL directly read; other paths supplied by [RT-RTE-remember-write](runtime.md#rt-rte-remember-write), [RT-RTE-recall-read](runtime.md#rt-rte-recall-read), [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff), [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run) | No successful write, restart or delivery trace |
| Fact synthesis and grounding | `internal/reasoner/openai.go`, `internal/brain/consolidate.go` | Direct read; [EPI-RTE-fact-synthesis](#epi-rte-fact-synthesis) | No semantic-preservation evaluation |
| Relationships, patterns and causal links | `internal/reasoner/openai.go`, `internal/brain/consolidate.go`, `internal/brain/causal.go`, `internal/brain/fact.go` | Direct reads; [EPI-RTE-relationship-extraction](#epi-rte-relationship-extraction), [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction), [EPI-RTE-causal-links](#epi-rte-causal-links) | No intervention/comparison validating causation; QueryPatterns API inspected, no registered MCP pattern query found in registry search |
| Contradiction classification, supersession, resolution | `internal/brain/contradiction.go`, `internal/reasoner/openai.go`, `cmd/cli/mcp.go` | Direct reads; [EPI-RTE-contradiction-review](#epi-rte-contradiction-review) | No evidence of reliable temporal classification |
| Hypothesis create/test/confirm/reject/refine/delete and maintenance | `cmd/cli/hypothesis.go`, `cmd/cli/mcp.go`, `internal/brain/hypothesis.go`, `internal/brain/consolidate_hypothesis.go`, `internal/reasoner/openai.go` | Direct reads; [EPI-RTE-hypothesis-assessment](#epi-rte-hypothesis-assessment), [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control) | No actual hypothesis instance or plan execution supplied |
| Goals and failures | `internal/brain/consolidate_goal.go`, `internal/brain/consolidate_failure.go`, `internal/brain/goal.go`, `internal/brain/failure.go`, `internal/reasoner/openai.go` | Direct stage/model reads, goal progress/completion/update/delete and failure CRUD; [EPI-RTE-goal-assessment](#epi-rte-goal-assessment), [EPI-RTE-failure-review](#epi-rte-failure-review) | Goal creation/list handlers and remaining MCP CRUD adapters searched, not fully read; prevents a system-complete negative about all admission behavior |
| Decay, deletion and later selectors | `internal/brain/decay.go`, `internal/brain/episode.go`, `internal/brain/fact.go`, `internal/queries/consolidate.sql.tmpl`, `internal/queries/recall.sql.tmpl` | Direct reads; [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal) | Migration cascades not audited; no guarantee of complete derivative withdrawal |
| Product release and opaque model state | `.github/workflows/release.yml`, `internal/embedder/cache.go`, `internal/bootstrap/bootstrap.go` | Supplied [RT-RTE-release-build](runtime.md#rt-rte-release-build), [RT-CMP-openai-reasoner](runtime.md#rt-cmp-openai-reasoner), [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder) | No provider parameter history, immutable deployed model identity or learning experiment |
| Product and agent warrant language | `README.md`, `cmd/cli/mcp_prompts.tmpl` | README and selected protocol/confirmation passages directly read; claim records below | Remaining HTML/tool prose not exhaustively read: no exhaustive public-claim inventory |

Missing run traces prevent claims that these routes operated or changed an agent's behavior. Missing truth-labelled evaluations prevent precision, faithfulness and calibration conclusions. Missing controlled interventions prevent learning benefit, causal link correctness and component-effect attribution. Uninspected available handlers limit exhaustive negatives; they are not access gaps. No supplied fact needs supersession: the new parts refine the runtime container rather than contradict its qualified findings.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-episode](#epi-obj-episode) | Caller assertions about events; author/warrant unknown | see record | SRC-1 `internal/brain/episode.go` | Not necessarily observations by a human |
| [EPI-OBJ-fact](#epi-obj-fact) | Summaries and structured assertions | see record | SRC-1 `internal/models/models.go` | Multiple producers; label not acceptance |
| [EPI-OBJ-relationship](#epi-obj-relationship) | Entity relation propositions | see record | SRC-1 `internal/brain/consolidate.go` | Entity occurrence does not validate relation |
| [EPI-OBJ-pattern](#epi-obj-pattern) | Cross-source pattern assertions | see record | SRC-1 `internal/brain/consolidate.go` | Coherence not independent truth evidence |
| [EPI-OBJ-causal-link](#epi-obj-causal-link) | Directed cause-effect assertion | see record | SRC-1 `internal/brain/causal.go` | Graph reachability not demonstrated causation |
| [EPI-OBJ-hypothesis](#epi-obj-hypothesis) | Belief content; plan is procedural content | see record | SRC-1 `internal/brain/hypothesis.go` | Plan omitted from automatic evaluator |
| [EPI-OBJ-contradiction](#epi-obj-contradiction) | Conflict/replacement classification over values | see record | SRC-1 `internal/brain/contradiction.go` | Explanation discarded on automatic persistence |
| [EPI-OBJ-goal](#epi-obj-goal) | Goal itself is an intention; progress notes/status make achievement claims | see record | SRC-1 `internal/brain/consolidate_goal.go` | No completion measurement |
| [EPI-OBJ-failure](#epi-obj-failure) | Failure/reason assertions plus prescriptive lesson | see record | SRC-1 `internal/brain/failure.go` | Caller attribution unverified |
| [RT-OBJ-server-description](runtime.md#rt-obj-server-description) | Protocol mostly non-truth-apt; warrant assertions in claim records | see record | SRC-1 `cmd/cli/mcp_prompts.tmpl` | Advisory to external client |
| [RT-CMP-openai-reasoner](runtime.md#rt-cmp-openai-reasoner), [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder) | Not determinable as individuated propositions in provider weights; vectors are numerical selectors | see records | SRC-1 `internal/reasoner/openai.go`, `internal/embedder/cache.go` | Distributed-parametric state; no weight/update access |
| [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff) | Focus can carry assertions/instructions | see record | SRC-1 `internal/brain/context.go` | Supplied runtime evidence, no separate object declaration |

## Authority-route ledger

Each function is separate even where the same implementation record owns its fields. In the compact entries, the grouped labels delegate each named field to the cited route. `see` delegates those fields to the linked canonical record; it does not turn storage into acceptance. No lifecycle integration of an accepted ampliative claim is established by the inspected witnesses. Hypothesis promotion has an operational integration path, assessed separately from its evidence-consuming decision.

Route ID: [RT-RTE-remember-write](runtime.md#rt-rte-remember-write)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-episode](#epi-obj-episode)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [RT-RTE-remember-write](runtime.md#rt-rte-remember-write).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [RT-RTE-remember-write](runtime.md#rt-rte-remember-write)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-episode](#epi-obj-episode)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [RT-RTE-remember-write](runtime.md#rt-rte-remember-write).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [RT-RTE-recall-read](runtime.md#rt-rte-recall-read)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fact](#epi-obj-fact), [EPI-OBJ-episode](#epi-obj-episode)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [RT-RTE-recall-read](runtime.md#rt-rte-recall-read).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff)
Route function: retention
Architectural status: implemented
Object/candidate ID: focus
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: focus
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [RT-RTE-context-handoff](runtime.md#rt-rte-context-handoff).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-fact-synthesis](#epi-rte-fact-synthesis)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fact](#epi-obj-fact)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-fact-synthesis](#epi-rte-fact-synthesis).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-fact-synthesis](#epi-rte-fact-synthesis)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fact](#epi-obj-fact)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-fact-synthesis](#epi-rte-fact-synthesis).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-fact-synthesis](#epi-rte-fact-synthesis)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fact](#epi-obj-fact)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-fact-synthesis](#epi-rte-fact-synthesis).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-fact-synthesis](#epi-rte-fact-synthesis)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fact](#epi-obj-fact)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-fact-synthesis](#epi-rte-fact-synthesis).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-relationship-extraction](#epi-rte-relationship-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-relationship](#epi-obj-relationship)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-relationship-extraction](#epi-rte-relationship-extraction).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-relationship-extraction](#epi-rte-relationship-extraction)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-relationship](#epi-obj-relationship)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-relationship-extraction](#epi-rte-relationship-extraction).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-relationship-extraction](#epi-rte-relationship-extraction)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-relationship](#epi-obj-relationship)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-relationship-extraction](#epi-rte-relationship-extraction).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-relationship-extraction](#epi-rte-relationship-extraction)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-relationship](#epi-obj-relationship)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-relationship-extraction](#epi-rte-relationship-extraction).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-pattern](#epi-obj-pattern)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-pattern](#epi-obj-pattern)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-pattern](#epi-obj-pattern)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-pattern](#epi-obj-pattern)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-pattern-extraction](#epi-rte-pattern-extraction).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-causal-links](#epi-rte-causal-links)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-causal-link](#epi-obj-causal-link)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-causal-links](#epi-rte-causal-links).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-causal-links](#epi-rte-causal-links)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-causal-link](#epi-obj-causal-link)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-causal-links](#epi-rte-causal-links).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-causal-links](#epi-rte-causal-links)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-causal-link](#epi-obj-causal-link)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-causal-links](#epi-rte-causal-links).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-causal-links](#epi-rte-causal-links)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-causal-link](#epi-obj-causal-link)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-causal-links](#epi-rte-causal-links).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-causal-links](#epi-rte-causal-links)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-causal-link](#epi-obj-causal-link)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-causal-links](#epi-rte-causal-links).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-causal-links](#epi-rte-causal-links)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-causal-link](#epi-obj-causal-link)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-causal-links](#epi-rte-causal-links).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-contradiction-review](#epi-rte-contradiction-review)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-contradiction](#epi-obj-contradiction)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-contradiction-review](#epi-rte-contradiction-review).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-contradiction-review](#epi-rte-contradiction-review)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-contradiction](#epi-obj-contradiction)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-contradiction-review](#epi-rte-contradiction-review).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-contradiction-review](#epi-rte-contradiction-review)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-contradiction](#epi-obj-contradiction)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-contradiction-review](#epi-rte-contradiction-review).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-contradiction-review](#epi-rte-contradiction-review)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-contradiction](#epi-obj-contradiction)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-contradiction-review](#epi-rte-contradiction-review).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-hypothesis-assessment](#epi-rte-hypothesis-assessment)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-hypothesis](#epi-obj-hypothesis)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-hypothesis-assessment](#epi-rte-hypothesis-assessment).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-hypothesis-assessment](#epi-rte-hypothesis-assessment)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-hypothesis](#epi-obj-hypothesis)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-hypothesis-assessment](#epi-rte-hypothesis-assessment).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-hypothesis-assessment](#epi-rte-hypothesis-assessment)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-hypothesis](#epi-obj-hypothesis)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-hypothesis-assessment](#epi-rte-hypothesis-assessment).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-hypothesis-assessment](#epi-rte-hypothesis-assessment)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-hypothesis](#epi-obj-hypothesis)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-hypothesis-assessment](#epi-rte-hypothesis-assessment).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-hypothesis](#epi-obj-hypothesis)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-hypothesis](#epi-obj-hypothesis)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-hypothesis](#epi-obj-hypothesis)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-hypothesis](#epi-obj-hypothesis)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-hypothesis](#epi-obj-hypothesis)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-goal-assessment](#epi-rte-goal-assessment)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-goal](#epi-obj-goal)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-goal-assessment](#epi-rte-goal-assessment).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-goal-assessment](#epi-rte-goal-assessment)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-goal](#epi-obj-goal)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-goal-assessment](#epi-rte-goal-assessment).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-goal-assessment](#epi-rte-goal-assessment)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-goal](#epi-obj-goal)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-goal-assessment](#epi-rte-goal-assessment).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-goal-assessment](#epi-rte-goal-assessment)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-goal](#epi-obj-goal)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-goal-assessment](#epi-rte-goal-assessment).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-failure-review](#epi-rte-failure-review)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-failure](#epi-obj-failure)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-failure-review](#epi-rte-failure-review).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-failure-review](#epi-rte-failure-review)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-failure](#epi-obj-failure)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-failure-review](#epi-rte-failure-review).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-failure-review](#epi-rte-failure-review)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-failure](#epi-obj-failure)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-failure-review](#epi-rte-failure-review).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-failure-review](#epi-rte-failure-review)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-failure](#epi-obj-failure)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-failure-review](#epi-rte-failure-review).
Claim IDs or none: none. Mismatch marker or none: none.

Route ID: [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fact](#epi-obj-fact)
Content/update relation: non-truth-apt policy/content update: age/score-based validity and deletion metadata
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal).
Claim IDs or none: none. Mismatch marker or none: expiry does not exclude recall.

Route ID: [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-fact](#epi-obj-fact)
Content/update relation: no content change
Transition or check target; evaluator/condition and domain; activation and timing; possible or observed result; implemented force; epistemic authority and scope; operational authority; behavioral-authority path; evidence source ID and local anchor; gap/limit: see [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal).
Claim IDs or none: none. Mismatch marker or none: none.


The contradiction-review, goal-assessment and failure-review records span maintenance and independent caller operations; their ledger fields delegate branch-specific owners, triggers and force to those records, not uniformly to the runtime consolidation container. Contradiction checking is model-driven maintenance, whereas manual resolution is caller-driven disposition. Goal checking/annotation is maintenance, whereas completion/status changes are caller-driven disposition. Failure checking/derivation is maintenance, whereas initial failure retention is caller-driven admission. None of these entire referents is contained in consolidation.

The indeterminate transformation rows concern model-produced semantic assertions, not every edge in their containers. For causal-links, the acquisition row is the caller-asserted path and consumption row is list/trace. For hypothesis-control, acquisition is creation or caller replacement and reshaping is unchanged-content confirmation. Direct causal assertion and hypothesis creation are acquisition/import with unknown source warrant; hypothesis confirmation preserves the same content and is non-ampliative reshaping into a new storage role. Goal/failure prescriptions are non-truth-apt content; progress and failure assessments are truth-apt. JSON fence stripping in extractJSON is deterministic formatting: input fenced JSON is trimmed, prefix/suffix fences removed, then decoded; it changes syntax, not evidential status (SRC-1 `internal/reasoner/openai.go`). Numerical confidence/validity updates change reliance metadata, not an assertion's truth. All transformations remain separate from subsequent checks and disposition.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source / evidence layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-fact-warrant](#epi-clm-fact-warrant) | see record | SRC-1 `cmd/cli/mcp_prompts.tmpl`; doctrine/design | see record | [EPI-RTE-fact-synthesis](#epi-rte-fact-synthesis), [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control), [EPI-RTE-failure-review](#epi-rte-failure-review), [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal) | None supplied | Structural checks and direct promotion cannot establish truth | Structured retained beliefs exist architecturally | Verified/distilled truth language exceeds demonstrated warrant |
| [EPI-CLM-hypothesis-verification](#epi-clm-hypothesis-verification) | see record | SRC-1 `README.md`, `cmd/cli/mcp_prompts.tmpl`; doctrine/design | see record | [EPI-RTE-hypothesis-assessment](#epi-rte-hypothesis-assessment), [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control) | None supplied | Model consumes fact text; stored plan not executed by test command or scan | Evidence-sensitive status change and promotion implemented | Verification is not an empirical testing guarantee |
| [EPI-CLM-memory-learning](#epi-clm-memory-learning) | see record | SRC-1 `README.md`; doctrine/design | see record | [RT-RTE-remember-write](runtime.md#rt-rte-remember-write), [RT-RTE-recall-read](runtime.md#rt-rte-recall-read), secondary routes above | None supplied | No quality comparison or client activation trace | Retention, retrieval and model-driven curation implemented | Improved future capacity unestablished |
| [RT-CLM-session-protocol](runtime.md#rt-clm-session-protocol) | see record | SRC-1 `cmd/cli/mcp_prompts.tmpl`; doctrine/design | see record | [RT-BAP-agent-protocol](runtime.md#rt-bap-agent-protocol) | None supplied | External client owns compliance | Advisory protocol delivered | Mandatory wording is not enforced call order or warranted answers |

## Bounded conclusion

Stash imports caller assertions with unknown warrant and stores them for later retrieval; it does not establish their original observational authority. Its structured-fact route requests reshaping, checks JSON and copying, then admits candidates as facts. The deterministic countercase in [EPI-RTE-fact-synthesis](#epi-rte-fact-synthesis) shows why the anti-copy gate cannot warrant entailment. Entity membership, source-ID counts, model coherence and confidence arithmetic provide narrower structural licenses. No supplied output establishes whether a particular model-produced edge is faithful reshaping, entailed derivation or ampliative conjecture. No accepted produced ampliative instance is evidenced.

There is genuine evidence-consuming evaluation in [EPI-RTE-hypothesis-assessment](#epi-rte-hypothesis-assessment): a model compares open beliefs with new retained fact text and code changes status/confidence or rejects. Its implemented acceptance criterion is model support above configured threshold for promotion of a testing hypothesis into retained fact use. That local license is bounded by the supplied text batch and a model judgement, not the stored verification plan or an independent empirical criterion. Support reasoning is not retained as a full acceptance record. Direct [EPI-RTE-hypothesis-control](#epi-rte-hypothesis-control) confirmation is a separate, evidence-free operational promotion from testing status. CLI exposes a direct test-status command; MCP exposes create/confirm/reject but no direct transition to testing, so an MCP confirmation depends on that status being obtained elsewhere. Neither fact naming nor the resulting confirmed_fact_id establishes evidence-consuming lifecycle integration of accepted ampliative knowledge.

[EPI-RTE-contradiction-review](#epi-rte-contradiction-review) marks an old fact ended and can hide a resolved conflict from unresolved listings; [EPI-RTE-memory-withdrawal](#epi-rte-memory-withdrawal) demonstrates that ending validity is not general withdrawal from recall or maintenance. QueryFacts supplies validity metadata, whereas recall omits it. Model goal suggestions are advisory notes rather than automatic completion; failure repetition episodes lack embeddings and bypass ordinary semantic recall, while failure pattern facts enter it directly. These distinct consequences prevent treating all maintenance outputs as equally available or equally authoritative.

Opaque model weights are separately assessed by [RT-CMP-openai-reasoner](runtime.md#rt-cmp-openai-reasoner) and [RT-CMP-openai-embedder](runtime.md#rt-cmp-openai-embedder). No training/update operation is identified in those adapters; mutable provider versions remain uninspected. Persistence and automatic content revision do not establish improved future capacity. Failure/goal/hypothesis routes afford structured review and change local state; reflection, learning benefit, autonomous theory building and exercised self-improvement are not inferred as a bundle. Formulated runtime theories and their criticism history cannot be established from source-native labels without instances; partial theory-condition findings are retained below. Protocol-mediated `/self` use can influence an external agent only if it recalls and obeys the text; that client's activation and capacity are outside inspected evidence. No run or causal evidence supports improved answers, reliable verification, or a system-wide epistemic score.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-episode
Label: Episode text

Source-native identity: `Episode.Content`. Caller natural-language assertions in PostgreSQL; dense Embedding is a separate numerical selection representation, and IDs/timestamps/deletion flags are symbolic metadata. Remember retains text without semantic acceptance; recall and synthesis later consume it. Distinct from [RT-OBJ-server-description](runtime.md#rt-obj-server-description) (static protocol) and from the runtime routes that carry these payloads; no counterpart object is declared in supplied runtime. Evidence: SRC-1 `internal/brain/episode.go` (implementation).

> // Remember stores a new episode in the given namespace.
> --- `internal/brain/episode.go`

#### EPI-OBJ-fact
Label: Fact content and metadata

Source-native identity: `Fact`. Content and entity/property/value text express candidate propositions; symbolic confidence/validity/source IDs control selected consumers, and dense vectors select by similarity. Stored in PostgreSQL. Producers are structured synthesis, confirmed hypothesis copying and failure patterns; these differ in checks. Their separate routes own admission and lineage findings. Distinct from [RT-OBJ-server-description](runtime.md#rt-obj-server-description) (static protocol) and from the runtime routes that carry these payloads; no counterpart object is declared in supplied runtime. Evidence: SRC-1 `internal/models/models.go` (implementation).

> // Fact is a belief derived from episodes.
> --- `internal/models/models.go`

#### EPI-OBJ-relationship
Label: Relationship triple

Source-native identity: `Relationship`. Symbolically delimited from_entity/relation_type/to_entity carries a proposition interpreted by models or humans; source_fact_id/confidence are metadata in PostgreSQL. Query and pattern consumers differ from the generating reasoner. Distinct from [RT-OBJ-server-description](runtime.md#rt-obj-server-description) (static protocol) and from the runtime routes that carry these payloads; no counterpart object is declared in supplied runtime. Evidence: SRC-1 `internal/models/models.go` (implementation).

> // Relationship is an extracted entity edge.
> --- `internal/models/models.go`

#### EPI-OBJ-pattern
Label: Pattern statement

Source-native identity: `Pattern`. Natural-language Content in PostgreSQL plus symbolic source lists/coherence/confidence. QueryPatterns can return it; no inspected ordinary recall selector retrieves patterns. Distinct from [RT-OBJ-server-description](runtime.md#rt-obj-server-description) (static protocol) and from the runtime routes that carry these payloads; no counterpart object is declared in supplied runtime. Evidence: SRC-1 `internal/models/models.go` (implementation).

> // Pattern is an abstraction over facts and relationships.
> --- `internal/models/models.go`

#### EPI-OBJ-causal-link
Label: Causal link

Source-native identity: `CausalLink`. Symbolic directed fact IDs, method and confidence in PostgreSQL encode a cause-effect assertion whose truth is not guaranteed by graph traversal. List/trace consume fixed structure, clients interpret causal meaning. Distinct from [RT-OBJ-server-description](runtime.md#rt-obj-server-description) (static protocol) and from the runtime routes that carry these payloads; no counterpart object is declared in supplied runtime. Evidence: SRC-1 `internal/models/models.go` (implementation).

> // CausalLink records a cause-effect relationship between two facts.
> --- `internal/models/models.go`

#### EPI-OBJ-hypothesis
Label: Hypothesis content and verification plan

Source-native identity: `Hypothesis`. Natural-language content/verification_plan/rejection_reason in PostgreSQL; symbolic status/confidence/source IDs/confirmed_fact_id control API transitions. The automatic evaluator consumes content but not the plan. Distinct from [RT-OBJ-server-description](runtime.md#rt-obj-server-description) (static protocol) and from the runtime routes that carry these payloads; no counterpart object is declared in supplied runtime. Evidence: SRC-1 `internal/models/models.go` (implementation).

> // Hypothesis is a belief held with uncertainty plus a plan to verify it.
> --- `internal/models/models.go`

#### EPI-OBJ-contradiction
Label: Contradiction record

Source-native identity: `Contradiction`. Structured entity/property/old/new values plus symbolic fact IDs/confidence/resolved flag, stored in PostgreSQL. Resolution text can carry rationale. Model explanation is not copied into these writes. Distinct from [RT-OBJ-server-description](runtime.md#rt-obj-server-description) (static protocol) and from the runtime routes that carry these payloads; no counterpart object is declared in supplied runtime. Evidence: SRC-1 `internal/models/models.go` (implementation).

> // Contradiction records a conflict between two facts about the same entity and property.
> --- `internal/models/models.go`

#### EPI-OBJ-goal
Label: Goal and assessment notes

Source-native identity: `Goal`. Natural-language intended outcome and notes in PostgreSQL; symbolic status, parent, priority and dates. Goal content is not an assertion that it is achieved; status and notes can assert progress/completion. Distinct from [RT-OBJ-server-description](runtime.md#rt-obj-server-description) (static protocol) and from the runtime routes that carry these payloads; no counterpart object is declared in supplied runtime. Evidence: SRC-1 `internal/models/models.go` (implementation).

> // Goal is an intended outcome that persists across sessions.
> --- `internal/models/models.go`

#### EPI-OBJ-failure
Label: Failure and lesson

Source-native identity: `Failure`. Natural-language content/reason/lesson in PostgreSQL; symbolic goal/namespace IDs. Caller cause attribution and prescription are not independently validated; later model review consumes them. Distinct from [RT-OBJ-server-description](runtime.md#rt-obj-server-description) (static protocol) and from the runtime routes that carry these payloads; no counterpart object is declared in supplied runtime. Evidence: SRC-1 `internal/models/models.go` (implementation).

> // Failure records what didn't work, why, and what to do instead.
> --- `internal/models/models.go`

### Routes

#### EPI-RTE-fact-synthesis
Label: Structured fact synthesis

Part of: [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run)

Cluster texts → ReasonStructured → JSON and anti-copy checks → embedding/dedup → fact SQL and source associations. Brain owns progression; model proposes content; code can veto malformed/copying/duplicate results. Open maintenance requests, no reference-answer oracle or human per-content approval. Guidance is extraction-only plus synthesis without echoing. The intended relation is reshaping, but actual semantic preservation is indeterminate without outputs and source comparisons. Source warrant is unknown; removing first-person markers can erase who asserted a proposition. Confidence is a count/structured-fields heuristic, not truth calibration. With one observation and structured fields the inspected arithmetic yields about 0.533, independent of the statement's truth.

Concrete deterministic countercase: source text `Alice uses Python`; proposed summary `Bob owns elephants`. Token sets are {alice, uses, python} and {bob, owns, elephants}; containment is false and overlap is zero, so validateFactGrounding returns nil. This is implementation deduction, not a model run. Conversely the unchanged true source sentence is rejected as a verbatim copy. The check distinguishes copying, not entailment. Parse/retry checks therefore license a structurally usable candidate, not a verified fact. Nonempty admitted content persists before epistemic acceptance; best-effort source links may fail independently. Later recall supplies fact content/confidence but not the provenance chain. Recovery is retry/checkpoint/dedup, not atomic rollback of the whole maintenance pass.

Evidence: SRC-1 `internal/reasoner/openai.go` (implementation); additional named paths are in this report's coverage table.

- Immediate return: Fact insertion/counters or stage errors; empty summaries and duplicates skipped.
- Later read-back: Facts reach recall, QueryFacts and later maintenance; source links are attempted.
- Delegated visibility: External tool caller receives maintenance results; later memory caller receives selected text.
- Selection predicate: Checkpointed episode batch, vector clustering, nonempty summary, anti-copy gate, vector dedup.
- Invalidation or expiry: Fact validity/deletion controls are separate; failed source-link inserts are ignored.
- Activation or effect: Persisted fact gains eligibility for later fact consumers, not an established truth license.
- Evidence limits: No candidate/run supplied; faithful reshaping, warrant preservation and quality unestablished.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if strings.Contains(textLower, summaryLower) {
> 			return fmt.Errorf("summary is a verbatim copy of source text")
> 		}
> --- `internal/reasoner/openai.go`

> confidence := calculateConfidence(len(cluster), sf.Entity != "" && sf.Property != "")
> --- `internal/brain/consolidate.go`

> _, _ = b.pool.Exec(ctx,
> 				"INSERT INTO fact_sources (fact_id, episode_id) VALUES ($1, $2) ON CONFLICT DO NOTHING",
> 				factID, eid,
> 			)
> --- `internal/brain/consolidate.go`

#### EPI-RTE-relationship-extraction
Label: Entity relationship extraction

Part of: [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run)

Fact content → model relationship candidates → JSON/entity-substring validation → nonempty/dedup checks → relationships table. Brain and adapter own progression; model proposes relation_type and confidence. Entity names must occur case-insensitively in the fact; confidence is clamped to [0.7,1]. A fabricated relation between two mentioned entities passes this structural target; the program does not assess whether the relation is stated. Extraction-only doctrine requests non-ampliative reshaping; semantic relation is indeterminate without candidate text. Open maintenance mode, no answer oracle or human veto. Stored edge retains source_fact_id and is delivered by QueryRelationships/MCP; it also feeds patterns. Database failure rejects a write; checkpoint/retry is recovery, with no semantic rollback. This part is distinct from the enclosing consolidation route.

Evidence: SRC-1 `internal/reasoner/openai.go` (implementation); additional named paths are in this report's coverage table.

- Immediate return: Edges/counters or stage errors.
- Later read-back: QueryRelationships returns edges; patterns consume them.
- Delegated visibility: MCP JSON to requesting client.
- Selection predicate: New facts, endpoint occurrence, nonempty triple and per-source dedup.
- Invalidation or expiry: Deleted edges excluded from query; no automatic semantic retraction shown.
- Activation or effect: Edges become queryable and pattern inputs; no demonstrated correctness.
- Evidence limits: No outputs or relationship truth labels.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if !stringsContains(factContent, jr.From) || !stringsContains(factContent, jr.To) {
> 				groundingFailed = true
> 				break
> 			}
> --- `internal/reasoner/openai.go`

#### EPI-RTE-pattern-extraction
Label: Pattern candidate extraction

Part of: [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run)

New fact and relationship text/IDs/confidences → model pattern → JSON/ID membership and minimum-count checks → SQL pattern. Brain owns storage, model proposes and rates coherence. No oracle or per-content human veto; maintenance mode. Content relation is indeterminate: extraction/no-generalization doctrine does not establish entailment, nor does failure to prove entailment establish conjecture. Code accepts at least two total IDs, unlike the prompt requiring two fact IDs OR two relation IDs; IDs are not deduplicated by filterIDs, so repeated references can satisfy the count. This licenses reference membership/count, not independent evidence or truth. Stored confidence is minimum selected source confidence times coherence; if either source list is empty the persistence code replaces both lists with all input sources, broadening lineage without a new evidential decision. QueryPatterns is a Brain API consumer, not an inspected registered MCP tool; relationships/facts alone are served by ordinary recall. Writes/checkpoints have retry recovery, not epistemic acceptance.

Evidence: SRC-1 `internal/reasoner/openai.go` (implementation); additional named paths are in this report's coverage table.

- Immediate return: Pattern rows/counters or errors.
- Later read-back: QueryPatterns API returns retained pattern content and source IDs.
- Delegated visibility: API callers; no MCP pattern-query registration in searched registry.
- Selection predicate: New facts; enough facts/relationships; nonempty output and valid IDs.
- Invalidation or expiry: Deletion filtering at QueryPatterns; derivative validity propagation not established.
- Activation or effect: Pattern retention and API eligibility, not accepted ampliative knowledge.
- Evidence limits: No distinct-source guarantee, actual patterns, evaluation or demonstrated downstream use.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if len(validFacts)+len(validRels) < 2 {
> 				continue
> 			}
> --- `internal/reasoner/openai.go`

> if len(sourceFactIDs) == 0 || len(sourceRelIDs) == 0 {
> --- `internal/brain/consolidate.go`

#### EPI-RTE-causal-links
Label: Causal link extraction and assertion

Distinct identity: unlike [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run), this record includes exposed caller operations and their own consumers, not solely a part of the maintenance invocation. It is not a replacement for that container.

Automatic input facts → model directed IDs → JSON/membership/non-self-loop checks → extracted causal link. Model judges DIRECT causation from fact text, without intervention or measured contrast; code licenses IDs, not a causal effect. Content relation is indeterminate; causal wording may be explicitly present or inferred, and no instance resolves it. Brain owns inserts. An alternate CLI/MCP caller directly asserts a link with method asserted; this imports a claim with unknown source warrant, bypassing the model and automatic membership-list validator. Human authorship unresolved. Both are open requests/maintenance, no answer oracle. ListCausalLinks and TraceCausalChain return edges; recursive traversal derives graph reachability, not transitive causal warrant. Bounded depth controls continuation, not causal validity. Delete soft-deletes links; DB errors reject inserts. No autonomous test-selection loop follows from these operations.

Evidence: SRC-1 `internal/brain/causal.go` (implementation); additional named paths are in this report's coverage table.

- Immediate return: Link rows/counts, chain rows or errors.
- Later read-back: List/trace read retained nondeleted edges.
- Delegated visibility: MCP serializes link/chain objects to caller.
- Selection predicate: Automatic IDs from model input and no self-loop; manual two differing IDs; trace start/direction/depth.
- Invalidation or expiry: DeleteCausalLink soft-deletes; all traversed edges filter deleted_at.
- Activation or effect: Graph assertions become available for external interpretation; traversal is enforcing graph selection only.
- Evidence limits: No causal experiment, factual provenance check or external agent effect.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> // CreateCausalLink manually asserts a cause-effect relationship between two facts.
> --- `internal/brain/causal.go`

#### EPI-RTE-contradiction-review
Label: Structured contradiction review

Distinct identity: this route spans automatic detection within [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run) and independent caller resolution/listing in SRC-1 `internal/brain/contradiction.go` and `cmd/cli/mcp.go`. Only the detection branch is contained in maintenance. The whole referent is neither a part nor a replacement of that runtime container; no supplied runtime record separately declares the caller-resolution branch.

New structured fact → existing active same entity/property values → model replacement/contradiction/compatible judgement → confidence threshold branch. Model sees entity/property and old/new values, not original episode chronology or full evidence. Target is compatibility/replacement of these values, not an independently verified world state. Adapter checks class and clamps confidence. At replacement confidence >=0.9, Brain sets old valid_until and inserts a resolved superseded record; other conflicts are retained unresolved. Model Explanation is returned by adapter but not persisted in the contradiction table writes. There is no answer oracle or per-content human veto in automatic maintenance. Manual CLI/MCP resolution merely marks the contradiction resolved with text; it does not update either fact. Resolve is caller-chosen, authorship unresolved, no evidence criterion enforced. Listing selects only unresolved conflicts, so resolving hides them from that listing. A successful supersession changes eligibility in the active-fact contradiction detector but NOT ordinary recall or QueryFacts, which omit a valid_until filter. No route here licenses new value truth. Nontransactional updates can leave partial state; logged counters can overstate successful supersession.

Evidence: SRC-1 `internal/brain/contradiction.go` (implementation); additional named paths are in this report's coverage table.

- Immediate return: Detected/resolved counters or DB error; manual resolution acknowledgment.
- Later read-back: Unresolved list returns pending conflicts; active detector omits ended facts.
- Delegated visibility: MCP list/resolution to requesting client.
- Selection predicate: Same entity/property namespace; different values; replacement threshold 0.9.
- Invalidation or expiry: Resolved conflicts leave unresolved listing; old fact remains eligible in recall/query.
- Activation or effect: Metadata changes future comparison and conflict visibility; not full withdrawal of reliance.
- Evidence limits: Value-only model judgement; no operation trace or reliable temporal warrant.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "UPDATE facts SET valid_until = $2, updated_at = $3 WHERE id = $1",
> --- `internal/brain/contradiction.go`

> UPDATE contradictions SET resolved = TRUE, resolution = $2, resolved_at = $3 WHERE id = $1
> --- `internal/brain/contradiction.go`

#### EPI-RTE-hypothesis-assessment
Label: Hypothesis evidence assessment

Part of: [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run)

Open proposed/testing hypotheses plus up to 30 new fact texts → model supports/weakens/contradicts verdict and reasoning → adapter ID/verdict/range validation → Brain threshold decisions. The prompt input includes hypothesis content/status/confidence but omits verification_plan and source_fact_ids; fact input includes IDs/text, not underlying episode evidence. The model is an evidence-consuming evaluator over recent retained texts, not an answer oracle or executor of the stored verification plan. Guidance requests supporting/contradicting evidence; open maintenance mode. The criterion for operational promotion is supports with configured auto-confirm threshold: proposed becomes testing; an already testing hypothesis is confirmed into a fact. Contradicts over the reject threshold rejects with reasoning; lower support/weakening updates confidence. The threshold acceptance is for use as a retained fact, scoped to model judgement over this batch, not an independently checked empirical conclusion. Relation of verdict/reasoning to premises is indeterminate without candidate outputs.

Supporting reasoning and the evidence batch's particular fact IDs are not persisted by the support branch; confirmation copies preexisting hypothesis confidence, not verdict confidence or new_confidence. Contradiction reasoning is retained as rejection_reason. Thus evidence evaluation has implemented force but confirmation does not retain a complete acceptance rationale. Checkpoint advancement even after some result failures can prevent reconsideration of that same batch. Decisions change future status-filtered selection and fact eligibility. Counterexample to a blanket no-evaluation finding: this stage actually consumes evidence and can reject, unlike direct confirmation.

Evidence: SRC-1 `internal/brain/consolidate_hypothesis.go` (implementation); additional named paths are in this report's coverage table.

- Immediate return: Auto-confirm/reject/update counters or stage errors.
- Later read-back: Status/confidence/rejection reason feed later list/scans; confirmed facts reach recall.
- Delegated visibility: Maintenance results then requested hypothesis/fact reads.
- Selection predicate: Open hypotheses; new fact checkpoint; model ID membership; configurable thresholds.
- Invalidation or expiry: Rejected/confirmed no longer selected as open; batch checkpoint advances after result loop.
- Activation or effect: Enforcing status/promotion/confidence decisions in Brain; advisory delivered content for external client.
- Evidence limits: No plan execution, empirical oracle, stored supporting rationale or demonstrated benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> case r.Verdict == "supports" && r.Confidence >= b.config.HypothesisAutoConfirmThreshold:
> --- `internal/brain/consolidate_hypothesis.go`

> hypLines = append(hypLines, fmt.Sprintf("[Hypothesis %d] (status: %s, confidence: %.2f) %s", h.ID, h.Status, h.Confidence, h.Content))
> --- `internal/reasoner/openai.go`

> _, _, confirmErr := b.ConfirmHypothesis(ctx, r.HypothesisID)
> --- `internal/brain/consolidate_hypothesis.go`

> reason := r.Reasoning
> --- `internal/brain/consolidate_hypothesis.go`

Theory account: conditional on the supplied belief being a formulated theory, content and criticism are individually identifiable by hypothesis ID; no actual instance was supplied. The evidence scan consumes the statement, can retain contradicting reasoning as rejection_reason and changes reliance/status. Next scans consume changed statuses/confidence; rejected items leave open selection. Supporting reasoning is not kept, verification-plan content is not consumed and no explicit blame assignment among theory/test/data/auxiliary assumptions is required. Thus theory-builder conditions 1–4 are independent: condition 1 conclusion status: afforded (whole belief storage, actual formulated theory uninspected); condition 2 conclusion status: wired (statement-dependent scan); condition 3 conclusion status: uninspected (no criticism instance demonstrating content, result and blame); condition 4 conclusion status: wired (status/confidence affect next selection, but criticism-specific iteration remains uninspected). Addressability: whole statement/plan independently accessible; assumptions/scope/parts not structured. Persistence: database across sessions; later hypothesis/fact readers. Learning conclusion status: uninspected — no improvement comparison. Reflection conclusion status: uninspected — no self-representation instance and both causal directions. Autonomous theory builder conclusion status: uninspected — caller supplies beliefs and controls external testing; internal evidence assessment alone is insufficient. Reflective theory builder conclusion status: uninspected — no retained criticism of operative method text. These are conditional capacity observations, not a positive or negative system-wide theory-builder verdict.

#### EPI-RTE-hypothesis-control
Label: Caller hypothesis lifecycle control

Distinct identity: unlike [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run), this record includes exposed caller operations and their own consumers, not solely a part of the maintenance invocation. It is not a replacement for that container.

CLI caller → create/test/confirm/reject/refine/delete; MCP caller → create/confirm/reject, with list for read-back. The frozen MCP registry exposes no direct test/status-to-testing tool. An MCP confirmation therefore requires testing status obtained through the CLI test command or automatic evidence scan, not a complete direct MCP lifecycle. The automatic proposed-to-testing transition belongs to [EPI-RTE-hypothesis-assessment](#epi-rte-hypothesis-assessment), not this caller-control route (SRC-1 `cmd/cli/main.go`, `cmd/cli/hypothesis.go`, `cmd/cli/mcp.go`, `internal/brain/consolidate_hypothesis.go`). Creation imports content/plan/confidence and source IDs (warrant unknown). Caller chooses changes; original human versus model author unresolved. Brain rejects empty content/invalid transitions/DB failures but requests no evidential payload for confirm. CLI test only changes status/tested_at; it runs no test. Confirm from testing embeds unchanged content and transactionally creates a fact and confirmed_fact_id; this is non-ampliative promotion, not an evidence-consuming acceptance decision. Guidance tells clients to check sufficient evidence, but confirm handler takes only ID. It copies hypothesis confidence and does not insert fact_sources or invoke the structured-fact anti-copy/contradiction validator. Rejection can retain caller reason and is terminal in transition map. Refine intends testing → proposed reset and replacement of text/plan/confidence, but passes time.Now().UTC as a function value rather than calling it: source establishes intended SQL wiring, not a successful refinement. It does not retain a versioned criticism history. No answer oracle; open requests; confirmation transaction has rollback on failure, no exposed undo of completed promotion. Deleting a hypothesis does not explicitly withdraw its confirmed fact in this method.

Evidence: SRC-1 `internal/brain/hypothesis.go` (implementation); additional named paths are in this report's coverage table.

- Immediate return: Updated hypothesis/fact JSON or error.
- Later read-back: Hypothesis lists/get and confirmed fact recall.
- Delegated visibility: CLI/MCP requester; confirmation returns both hypothesis and fact.
- Selection predicate: Brain transition map: proposed to testing/rejected; testing to confirmed/rejected/proposed; terminal thereafter. Direct caller transition to testing is CLI-only; MCP confirm requires preexisting testing status.
- Invalidation or expiry: Delete soft-deletes hypothesis only; rejected reason remains stored; refinement intended reset is not proven runnable.
- Activation or effect: Caller-driven retention/status/fact eligibility through the registered interface-specific operations; MCP cannot directly mark testing. Advisory evidence criterion is not enforced.
- Evidence limits: Confirm has no evidence argument; MCP-only direct lifecycle is incomplete without a testing transition elsewhere; no observed refinement or accepted produced ampliative instance.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> current.NamespaceID, current.Content, pgvector.NewVector(vec), b.embedder.Model(), current.Confidence, now,
> --- `internal/brain/hypothesis.go`

> h, err := bc.Brain.UpdateHypothesisStatus(ctx, id, "testing")
> --- `cmd/cli/hypothesis.go`

> Name:   "test",
> Usage:  "Mark a hypothesis as testing",
> Action: hypothesisTestCmd,
> --- `cmd/cli/main.go`

> now := time.Now().UTC
> 	var h models.Hypothesis
> --- `internal/brain/hypothesis.go`

> h, f, err := bc.Brain.ConfirmHypothesis(ctx, int64(id))
> --- `cmd/cli/mcp.go`

#### EPI-RTE-goal-assessment
Label: Goal progress assessment and annotation

Distinct identity: this route spans automatic annotation within [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run) and independent caller completion/status operations in SRC-1 `internal/brain/goal.go` and `cmd/cli/mcp.go`. Only the annotation branch is contained in maintenance. The whole referent is neither a part nor a replacement of that runtime container; no supplied runtime record separately declares these caller goal decisions.

Active goals and new fact text → model progress/suggested_complete/contradicted judgement → adapter IDs/verdict/range checks → appended goal note. Model checks textual evidence of progress; no measured outcome or answer oracle. Brain owns notes, model proposes; maintenance is open, with no human veto before note storage. Generated notes have indeterminate semantic relation to evidence. Suggested completion is advisory: this stage never invokes CompleteGoal. Separate caller CompleteGoal marks active goal completed and, if all nondeleted active/completed siblings are complete, recursively marks parents complete. Abandoned siblings are excluded from that denominator. Completion metadata is caller assertion plus a fixed aggregation policy, not a physical success measurement. Caller can update/abandon/delete active goals; human authorship unresolved. Notes/status persist to goal readers; stage checkpoint can advance after annotation errors. This is distinct from directly changing agent executable policy.

Evidence: SRC-1 `internal/brain/consolidate_goal.go` (implementation); additional named paths are in this report's coverage table.

- Immediate return: Annotation/suggestion counters or errors; caller completion returns goal.
- Later read-back: Goal list/get returns retained notes/status; parent completion affects later goal selection.
- Delegated visibility: Goal read callers receive text/status; no unsolicited foreground delivery.
- Selection predicate: Active goals/new fact batch; valid model goal IDs; caller complete requires active status.
- Invalidation or expiry: Abandon/delete change later selection; notes appended rather than criticism supersession.
- Activation or effect: Model notes advisory; caller status update and ancestor aggregation enforcing inside goal state.
- Evidence limits: No goal outcome measurement, fully inspected goal-creation adapter or run benefit.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> note = fmt.Sprintf("\n[SUGGESTED COMPLETE] %s (confidence: %.2f)", a.Note, a.Confidence)
> --- `internal/brain/consolidate_goal.go`

> g, err := bc.Brain.CompleteGoal(ctx, int64(id), notes)
> --- `cmd/cli/mcp.go`

#### EPI-RTE-failure-review
Label: Failure repetition and pattern review

Distinct identity: this route spans automatic failure review within [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run) and independent caller admission/listing/deletion in SRC-1 `internal/brain/failure.go` and `cmd/cli/mcp.go`. Only the automatic review branch is contained in maintenance. The whole referent is neither a part nor a replacement of that runtime container; no supplied runtime record separately declares initial caller failure admission.

Caller records failure content/reason/lesson after nonempty checks; ListFailures later supplies these assertions. Source warrant is unknown and lesson prescription does not itself assert a truth. During maintenance new failures plus new episode texts go to model repetition/pattern judgement. Adapter checks repetition failure-ID membership/nonempty evidence or nonempty pattern_fact, clamps confidence, retries JSON/reference failures. Brain stores repetitions as REPEAT FAILURE episodes with NULL embedding; these cannot enter ordinary semantic recall, whose episode selector requires embedding. They remain eligible for episode fetch/consolidation, which has no embedding filter. Pattern facts are embedded and directly inserted with model confidence, bypassing structured-fact anti-copy/dedup/source-link/contradiction path. Content relation is indeterminate without model instances; higher-order guidance requests general claims but does not prove any occurred or were non-entailed. No answer oracle or human veto; open maintenance mode; code rejects DB/embedding failures. Checkpoints advance after results even with write errors and can consume new failures without model review when no new episode text exists. Rationale/data can thus persist and feed later synthesis without a complete preserved evidence chain or an independently warranted causal explanation.

Evidence: SRC-1 `internal/brain/consolidate_failure.go` (implementation); additional named paths are in this report's coverage table.

- Immediate return: Failure row or repetition/pattern counts/errors.
- Later read-back: Failure list; repetition episodes through fetch; embedded pattern facts through recall.
- Delegated visibility: MCP failure readers and later fact consumers, not unsolicited foreground updates.
- Selection predicate: Nonempty caller content/reason/lesson; new failure/episode batches; adapter ID checks.
- Invalidation or expiry: Failure delete soft-deletes; output episodes/facts are separate and not explicitly retracted.
- Activation or effect: Automatically retained evaluative assertions influence later maintenance inputs; downstream behavior unobserved.
- Evidence limits: No observed recurring failure instance, generalization validity or capacity improvement.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> VALUES ($1, $2, NULL, '', $3)
> --- `internal/brain/consolidate_failure.go`

> f, err := bc.Brain.CreateFailure(ctx, nsIDs[0], content, reason, lesson, goalID)
> --- `cmd/cli/mcp.go`

> nsID, r.PatternFact, pgvector.NewVector(vec), b.embedder.Model(), r.Confidence, time.Now().UTC(),
> --- `internal/brain/consolidate_failure.go`

#### EPI-RTE-memory-withdrawal
Label: Decay deletion and consumer selection

Distinct identity: unlike [RT-RTE-consolidation-run](runtime.md#rt-rte-consolidation-run), this record includes exposed caller operations and their own consumers, not solely a part of the maintenance invocation. It is not a replacement for that container.

Stale active facts → SQL confidence multiplication → below-threshold valid_until stamp. The evaluator targets age/score under configured rules, not truth. This is a non-truth-apt reliance-metadata update; Brain owns it without model/human judgement or answer oracle. Countercase to the source comment claiming soft-deletion: expiry SQL only sets valid_until, not deleted_at. Ordinary recall, QueryFacts and maintenance fetch_facts filter deleted_at but not valid_until; recall also omits validity metadata from its projection. Ended content therefore remains deliverable as ordinary fact text, and fetch can feed it to later model assessments. QueryFacts does return validity metadata, leaving interpretation to the client. Contradiction detector and further decay use valid_until IS NULL and thus do exclude it.

Caller ForgetEpisode embeds a query and soft-deletes only the nearest episode, without similarity threshold or explicit content-confirmation step. PurgeEpisode physically deletes an ID; PurgeFact is a Brain API operation, not located as a shipped CLI fact-purge command. Deleting/forgetting an input does not in inspected Brain code re-evaluate derived claims. Migration cascade details were not audited: no full derivative-cleanup negative follows. Invalidated episode text is filtered out of recall and maintenance; GetEpisode by ID can still fetch a soft-deleted row. No general complete withdrawal guarantee follows.

Evidence: SRC-1 `internal/brain/decay.go` (implementation); additional named paths are in this report's coverage table.

- Immediate return: Decay/expiry counts or delete acknowledgment/error.
- Later read-back: Updated metadata consumed by next decay/detector; recall still returns ended facts.
- Delegated visibility: Caller-triggered read/delete; no push revocation to external agent contexts.
- Selection predicate: Configured window/factor/threshold; forget nearest embedded episode in namespaces; purge by ID.
- Invalidation or expiry: Fact expiry is validity metadata only; episode soft deletion excludes ordinary search but not ID getter.
- Activation or effect: Enforcing selector changes only where consumers consult changed metadata; no retroactive client-context withdrawal.
- Evidence limits: No migration cascade audit, executed expiry or downstream correction trace.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> UPDATE facts SET valid_until = now(), updated_at = now()
> --- `internal/brain/decay.go`

> FROM facts
> WHERE deleted_at IS NULL
>     AND embedding IS NOT NULL
> --- `internal/queries/recall.sql.tmpl`

> FROM facts
> WHERE namespace_id = {{.Bind .Args.namespace_id}}
>     AND deleted_at IS NULL
>     AND id > {{.Bind .Args.after_id}}
> --- `internal/queries/consolidate.sql.tmpl`

> "UPDATE episodes SET deleted_at = now() WHERE id = $1", id,
> --- `internal/brain/episode.go`

### Claims

#### EPI-CLM-fact-warrant
Label: Consolidated fact warrant

Distinct from [RT-CLM-session-protocol](runtime.md#rt-clm-session-protocol), which governs requested call order. Claimed operation: query_facts returns verified/distilled truths, not merely admitted candidates. Source: SRC-1 `cmd/cli/mcp_prompts.tmpl` (doctrine/design). Comparison is with synthesis and alternate fact admission, not external provider truth.

> - Verified facts (requires consolidation) → query_facts
> --- `cmd/cli/mcp_prompts.tmpl`

> Lists consolidated facts for a namespace. Higher quality than raw recall — these are distilled truths extracted from episodes.
> --- `cmd/cli/mcp_prompts.tmpl`

#### EPI-CLM-memory-learning
Label: Learning across sessions

Distinct from [RT-CLM-session-protocol](runtime.md#rt-clm-session-protocol): this is a product benefit assertion. Claimed operation: persistent memory enables remembering, consolidation and learning across sessions. SRC-1 `README.md` (doctrine/design). Retention/retrieval are implemented; improvement evidence is not supplied.

> Stash gives your agent persistent memory — it remembers, recalls, consolidates, and learns across sessions.
> --- `README.md`

#### EPI-CLM-hypothesis-verification
Label: Hypothesis verification and promotion

Distinct from [RT-CLM-session-protocol](runtime.md#rt-clm-session-protocol): this is a content warrant/lifecycle claim. SRC-1 `README.md`, `cmd/cli/mcp_prompts.tmpl` (doctrine/design). Claimed operation: hypothesis verification and confirming truth before fact promotion. Model evidence scan and direct ID confirmation differ in evidence requirements.

> A 9-stage consolidation pipeline turns raw observations into structured knowledge — facts, relationships, causal links, patterns, contradictions, goal tracking, failure patterns, and hypothesis verification.
> --- `README.md`

> Confirms a hypothesis as true and automatically creates a Fact from it.
> --- `cmd/cli/mcp_prompts.tmpl`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; actual consumer/channel/force/horizon fields are retained in each route, with static prompt paths supplied by [RT-BAP-extraction-policy](runtime.md#rt-bap-extraction-policy) and [RT-BAP-agent-protocol](runtime.md#rt-bap-agent-protocol).
