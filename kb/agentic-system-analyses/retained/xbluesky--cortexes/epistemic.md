---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Cortexes epistemic routes: candidate extraction, human-directed revision, derived search state and bounded retrieval evaluation."
run-id: AAS-2026-11-08-cortexes-af94078f2405-01
reviewed-boundary: "2b8e79f0099203e0453147b708346349952bb963"
---

# Cortexes epistemic report

## Source-and-claim boundary

Question: what content can Cortexes acquire, check, admit and make consequential in later work, and what warrant do those operations confer? The whole-system functional boundary and exclusions are those of [boundary](boundary.md#boundary-and-evidence); evidence identities remain in its [Source register](boundary.md#source-register). All new inspection below is SRC-1 at the frozen commit, not an additional source. No target execution was performed.

Cortexes records and curates user-session material. Its “knowledge” vocabulary does not by itself promise autonomous scientific discovery. Public claims assessed are [RT-CLM-vault-purpose](runtime.md#rt-clm-vault-purpose) and [EPI-CLM-vault-index](#epi-clm-vault-index). Host/provider implementations, private vaults, real-session traces and evaluation results are unavailable: respectively these prevent claims about internal model reasoning/parameter changes, actual retained propositions, exercised acceptance/adherence, and measured retrieval benefit. No causal comparison was supplied. Candidate content can be identified by its prescribed role without inventing particular vault claims.

Coverage distinguishes direct reads in this job from supplied runtime evidence. Entry points missing from runtime's route inventory receive new records rather than being excluded.

| Entry point or operation | Source path (SRC-1) | Coverage and records |
|---|---|---|
| Hook registration, SessionStart/End, deck | `hooks/hooks.json` | Direct registration read; executable path detail supplied by [RT-RTE-session-start](runtime.md#rt-rte-session-start), [RT-RTE-session-capture](runtime.md#rt-rte-session-capture). |
| Genesis and direct evolve | `commands/genesis.md`, `skills/cortex-evolve/SKILL.md` | Evolve directly read; genesis supplied by [RT-RTE-direct-save](runtime.md#rt-rte-direct-save). |
| Distill, broadcast and rejection/abort | `skills/cortex-distill/SKILL.md`, `skills/cortex-broadcast/SKILL.md` | Complete direct skill reads; [RT-RTE-distill-review](runtime.md#rt-rte-distill-review), [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit). |
| Query and optional rerank/graph | `skills/cortex-query/SKILL.md`, `cortex-vec/src/cortex_vec/fusion.py` | Supplied [RT-RTE-vault-search](runtime.md#rt-rte-vault-search); no independent reranker accuracy assessment. |
| Takeoff resume/clear | `skills/cortex-takeoff/SKILL.md`, `hooks/scripts/takeoff.sh` | Supplied [RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff); no baton instance or downstream dependence. |
| Every Python CLI command | `cortex-vec/src/cortex_vec/cli.py` | Complete direct dispatcher read: status, rebuild, upsert, delete, search, eval, queues, reclaim, raw-state/view/map/span and distill-plan. |
| Status, summary generation, stale cleanup, delete | `cortex-vec/src/cortex_vec/store.py` | Direct function reads; [EPI-RTE-summary-build](#epi-rte-summary-build), [EPI-RTE-index-withdraw](#epi-rte-index-withdraw); rebuild/search detail supplied by [RT-RTE-direct-save](runtime.md#rt-rte-direct-save), [RT-RTE-vault-search](runtime.md#rt-rte-vault-search). |
| Retrieval evaluation and proposed query corpus | `cortex-vec/src/cortex_vec/eval/run.py`, `cortex-vec/src/cortex_vec/eval/corpus.py`, `cortex-vec/src/cortex_vec/eval/score.py`, `cortex-vec/src/cortex_vec/eval/adapters.py` | Complete direct reads; [EPI-RTE-eval-score](#epi-rte-eval-score), [EPI-RTE-query-propose](#epi-rte-query-propose). |
| Reclaim superseded | `cortex-vec/src/cortex_vec/reclaim.py` | Direct body, repo, predicate, scan, deletion and dispatch reads; [EPI-RTE-prefix-check](#epi-rte-prefix-check), [EPI-RTE-prefix-remove](#epi-rte-prefix-remove). |
| Raw filtering, navigation and ledger | `hooks/scripts/filter-transcript.py`, `cortex-vec/src/cortex_vec/distill_plan.py`, `cortex-vec/src/cortex_vec/raw_span.py` | Supplied runtime passages; exact command/TOML reducers and every projection branch not directly audited here. Prevents a universal semantic-preservation verdict. |
| Development audits/tests and remaining documentation | `docs/index-audit.md`, `tests/`, `cortex-vec/tests/` | Not inspected as runtime evidence; no passing tests, audit conclusions or deployment quality inferred. README opening directly read for claim comparison. |

This is coverage of material route families, not exhaustive branch verification. Uninspected reducers prevent a system-complete negative about every transformation; they do not undo witnessed acquisition, indexing or human-admission pathways.

## Epistemic-object inventory

Each row's claimed role, form and consumers are owned by its cited declaration.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-raw](#epi-obj-raw) | Session utterances, findings and decisions; some blocks are commands/logs rather than assertions | see declaration | SRC-1, `skills/cortex-distill/SKILL.md` | Recording an assertion does not authenticate it. |
| [EPI-OBJ-notes](#epi-obj-notes) | Technical explanations, mechanisms, decisions and project descriptions | see declaration | SRC-1, `skills/cortex-evolve/SKILL.md` | No actual vault supplied; specific proposition truth not determinable. |
| [EPI-OBJ-summary](#epi-obj-summary) | Model-requested summary of technical page; fallback title/tags | see declaration | SRC-1, `cortex-vec/src/cortex_vec/store.py` | Semantic fidelity not checked. |
| [EPI-OBJ-query-gold](#epi-obj-query-gold) | Query string is not an assertion; gold membership asserts intended relevance | see declaration | SRC-1, `cortex-vec/src/cortex_vec/eval/corpus.py` | Label authorship and confirmation unresolved per instance. |
| [EPI-OBJ-scorecard](#epi-obj-scorecard) | Bounded claims about retrieval against supplied gold | see declaration | SRC-1, `cortex-vec/src/cortex_vec/eval/score.py` | No measured instance supplied. |
| [RT-RTE-distill-review](runtime.md#rt-rte-distill-review) | Coverage intervals/terminal markers are process-state assertions, not note truth | see route | SRC-1, `cortex-vec/src/cortex_vec/distill_plan.py` | Coverage is emitted text, not cognition. |
| [RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff) | Continuation claims and task directives, mixed | see route | SRC-1, `skills/cortex-takeoff/SKILL.md` | No independent check of baton claims. |
| [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code), [RT-CMP-summary-model](runtime.md#rt-cmp-summary-model), [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model), [RT-CMP-rerank-model](runtime.md#rt-cmp-rerank-model), [RT-CMP-sonnet](runtime.md#rt-cmp-sonnet) | Distributed-parametric state: individuated stored propositions not determinable | see components | SRC-1, `cortex-vec/src/cortex_vec/store.py` | No weight inspection; request/candidate production is not provider learning evidence. |

## Authority-route ledger

Fields owned by the cited records say “see”; architectural status is assessed here. Related functions are deliberately separate even when one implementation handles them.

Route ID: [RT-RTE-session-capture](runtime.md#rt-rte-session-capture)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-raw](#epi-obj-raw)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Host transcript to Raw
Evaluator/condition and domain: see route; filter/classifier select preservation format, not truth
Activation and timing: see route
Possible or observed result: Filtered record or failure stub
Implemented force: Automatic capture
Epistemic authority and scope: Source warrant unknown; reduction can omit context
Operational authority: Makes Raw available for review/archive
Behavioral-authority path: see route; later model, Raw pages, advisory, later sessions
Evidence source ID and local anchor: SRC-1, `hooks/scripts/filter-transcript.py`
Claim IDs: [RT-CLM-vault-purpose](runtime.md#rt-clm-vault-purpose)
Mismatch marker: Full-report language does not establish full preservation
Gap/limit: No observed operation supplied.

Route ID: [RT-RTE-distill-review](runtime.md#rt-rte-distill-review)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-raw](#epi-obj-raw)
Content/update relation: no content change
Transition or check target: Budget, source identity, emitted coverage and evidence ranges
Evaluator/condition and domain: Program over ledger and source bytes; not factual evaluation
Activation and timing: Before pages/seal/complete; see route
Possible or observed result: Pages or rejection; negative seal requires coverage
Implemented force: Enforcing for these API calls only
Epistemic authority and scope: Coverage and source-consistency evidence, not truth of Raw
Operational authority: Blocks premature negative sealing; no gate on direct tools
Behavioral-authority path: see route; foreground via page API, enforcing, active plan
Evidence source ID and local anchor: SRC-1, `cortex-vec/src/cortex_vec/distill_plan.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [RT-RTE-distill-review](runtime.md#rt-rte-distill-review)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-notes](#epi-obj-notes)
Content/update relation: no content change
Transition or check target: Candidate insight verdict, placement and draft
Evaluator/condition and domain: Model proposes concrete-referent/mechanism/rationale evidence; human can override; see route
Activation and timing: After excerpts, before prescribed write
Possible or observed result: new, pending-merge, skip-routine, no-insight; draft confirmation
Implemented force: Interpreted human-approval policy
Epistemic authority and scope: Acceptance for useful vault retention is prescribed; no named factual-validity test or actual acceptance trace
Operational authority: Authorizes note write or defers/rejects it
Behavioral-authority path: see route and [RT-BAP-plugin-guidance](runtime.md#rt-bap-plugin-guidance)
Evidence source ID and local anchor: SRC-1, `skills/cortex-distill/SKILL.md`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [RT-RTE-distill-review](runtime.md#rt-rte-distill-review)
Route function: content transformation
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-notes](#epi-obj-notes)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Read passages to refined draft
Evaluator/condition and domain: Foreground model; human requested to confirm draft
Activation and timing: After new choice
Possible or observed result: Refined page candidate
Implemented force: Advisory proposal
Epistemic authority and scope: Could reshape acquired claims, derive or conjecture; paired inputs/outputs needed to classify
Operational authority: Supplies draft for human decision
Behavioral-authority path: see route
Evidence source ID and local anchor: SRC-1, `skills/cortex-distill/SKILL.md`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [RT-RTE-direct-save](runtime.md#rt-rte-direct-save)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-notes](#epi-obj-notes)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Caller page to derived indexes; source page creation is prescribed
Evaluator/condition and domain: User initiation/model authorship in evolve; CLI automatically indexes path
Activation and timing: Save/upsert or rebuild
Possible or observed result: Persisted page by policy, entries by code
Implemented force: Executable index admission, not truth approval
Epistemic authority and scope: Source warrant unknown; evolve bypasses distill dedup/final draft confirmation
Operational authority: Makes page searchable
Behavioral-authority path: see route; later search/model, index then Read, ranking/advisory, cross-session
Evidence source ID and local anchor: SRC-1, `cortex-vec/src/cortex_vec/store.py`
Claim IDs: [EPI-CLM-vault-index](#epi-clm-vault-index)
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [RT-RTE-distill-review](runtime.md#rt-rte-distill-review)
Route function: lifecycle integration
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-notes](#epi-obj-notes)
Content/update relation: no content change
Transition or check target: Confirmed new draft to indexed and linked vault
Evaluator/condition and domain: Human-confirmed retention decision; no independent correctness criterion
Activation and timing: After prescribed draft confirmation
Possible or observed result: Page index row, upsert, Raw target marker and log
Implemented force: Prompt-followed organizational integration
Epistemic authority and scope: Integrates accepted-for-retention content, not demonstrated accepted ampliative knowledge
Operational authority: Links accepted page to source record and later retrieval
Behavioral-authority path: see route
Evidence source ID and local anchor: SRC-1, `skills/cortex-distill/SKILL.md`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit)
Route function: check/evidence production
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-notes](#epi-obj-notes)
Content/update relation: no content change
Transition or check target: Raw assertion versus page assertion
Evaluator/condition and domain: Model compares content; human judges proposals; no expected answer oracle
Activation and timing: After full target Read
Possible or observed result: Contradiction proposal or section change
Implemented force: Advisory
Epistemic authority and scope: Potential disagreement evidence, not adjudicated truth
Operational authority: Exposes conflict for approval
Behavioral-authority path: see route
Evidence source ID and local anchor: SRC-1, `skills/cortex-broadcast/SKILL.md`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit)
Route function: disposition/acceptance
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-notes](#epi-obj-notes)
Content/update relation: no content change
Transition or check target: Exact before/after or conflict flag
Evaluator/condition and domain: Human yes/no/free-form response; criterion is requested page revision
Activation and timing: Per proposal, before targeted Edit
Possible or observed result: Approve, discard, revise, abort
Implemented force: Interpreted conversational gate
Epistemic authority and scope: Acceptance of edit does not establish new claim warrant
Operational authority: Permits/rejects page modification; earlier commits survive abort
Behavioral-authority path: see route
Evidence source ID and local anchor: SRC-1, `skills/cortex-broadcast/SKILL.md`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit)
Route function: lifecycle integration
Architectural status: doctrine only
Object/candidate ID: [EPI-OBJ-notes](#epi-obj-notes)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Approved page changes and source links
Evaluator/condition and domain: Foreground follows user-approved changes
Activation and timing: After per-page approval
Possible or observed result: Rewritten passage or inline conflict link, upsert and commit
Implemented force: Prompt-followed durable revision
Epistemic authority and scope: Per-instance interpretation needs actual input/output; conflict flag does not withdraw old claim automatically
Operational authority: Later search can return amended page
Behavioral-authority path: see route
Evidence source ID and local anchor: SRC-1, `skills/cortex-broadcast/SKILL.md`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [RT-RTE-vault-search](runtime.md#rt-rte-vault-search)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-notes](#epi-obj-notes)
Content/update relation: no content change
Transition or check target: Candidates for later answer context
Evaluator/condition and domain: Fusion/optional reranker select relevance; human chooses full page by policy
Activation and timing: On query
Possible or observed result: Hits then chosen full text
Implemented force: Ranking in code; advisory content
Epistemic authority and scope: No factual license from cosine, RRF or model relevance score
Operational authority: Ranks material for foreground interpretation
Behavioral-authority path: see route
Evidence source ID and local anchor: SRC-1, `cortex-vec/src/cortex_vec/fusion.py`
Claim IDs: [RT-CLM-vault-purpose](runtime.md#rt-clm-vault-purpose)
Mismatch marker: Distill/broadcast every-hit cosine wording fails on supported zero-backfill fallback
Gap/limit: No observed operation supplied.

Route ID: [RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff)
Route function: operational admission/selection/consumption
Architectural status: doctrine only
Object/candidate ID: [RT-BAP-baton-context](runtime.md#rt-bap-baton-context)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Baton to continuation context
Evaluator/condition and domain: Selected topic; no content-validity check
Activation and timing: On resume
Possible or observed result: Full-body adoption requested
Implemented force: Advisory work guidance
Epistemic authority and scope: Baton claims retain unknown source warrant
Operational authority: Steers next work without another truth check
Behavioral-authority path: see [RT-BAP-baton-context](runtime.md#rt-bap-baton-context)
Evidence source ID and local anchor: SRC-1, `skills/cortex-takeoff/SKILL.md`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [EPI-RTE-summary-build](#epi-rte-summary-build)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-summary](#epi-obj-summary)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Title/tags/body prefix to summary
Evaluator/condition and domain: OpenAI request; no fidelity evaluator
Activation and timing: see declaration
Possible or observed result: Model output or title/tags fallback
Implemented force: Automatic derived-state write
Epistemic authority and scope: No summary truth endorsement
Operational authority: Changes vector retrieval representation
Behavioral-authority path: see declaration; consumer/channel/force/horizon are route-specific
Evidence source ID and local anchor: SRC-1, `cortex-vec/src/cortex_vec/store.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [EPI-RTE-eval-score](#epi-rte-eval-score)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-scorecard](#epi-obj-scorecard)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Ranked paths versus gold at K
Evaluator/condition and domain: Deterministic metrics in path-membership domain
Activation and timing: see declaration
Possible or observed result: Per-query metrics and aggregate report
Implemented force: Reporting only
Epistemic authority and scope: Arithmetic relative to supplied labels, not label truth
Operational authority: Emits scorecard; no automatic production selector
Behavioral-authority path: see declaration; consumer/channel/force/horizon are route-specific
Evidence source ID and local anchor: SRC-1, `cortex-vec/src/cortex_vec/eval/score.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [EPI-RTE-query-propose](#epi-rte-query-propose)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-query-gold](#epi-obj-query-gold)
Content/update relation: non-truth-apt policy/content update: proposed search queries with assigned relevance labels
Transition or check target: Notes to candidate query corpus
Evaluator/condition and domain: Model proposes query, code assigns source path as gold
Activation and timing: see declaration
Possible or observed result: AUTO-PROPOSED JSONL
Implemented force: Automatic file write; review advisory
Epistemic authority and scope: Gold is a proposed relevance judgment, not verified truth
Operational authority: Supplies later eval input if caller runs it
Behavioral-authority path: see declaration; consumer/channel/force/horizon are route-specific
Evidence source ID and local anchor: SRC-1, `cortex-vec/src/cortex_vec/eval/run.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [EPI-RTE-prefix-check](#epi-rte-prefix-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-raw](#epi-obj-raw)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Conversation-line prefix and repo equality
Evaluator/condition and domain: Deterministic equality over normalized line arrays
Activation and timing: see declaration
Possible or observed result: Superseded/refused lists
Implemented force: Classification only
Epistemic authority and scope: Body inclusion only; no claim that unique header metadata survives
Operational authority: Supplies removal candidates
Behavioral-authority path: see declaration; consumer/channel/force/horizon are route-specific
Evidence source ID and local anchor: SRC-1, `cortex-vec/src/cortex_vec/reclaim.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [EPI-RTE-prefix-remove](#epi-rte-prefix-remove)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-raw](#epi-obj-raw)
Content/update relation: no content change
Transition or check target: Superseded file to deletion
Evaluator/condition and domain: --apply or hook caller consumes scan; no per-file human veto required
Activation and timing: see declaration
Possible or observed result: git rm or unlink; refusal retains cross-repo pair
Implemented force: Enforcing I/O
Epistemic authority and scope: Redundancy disposition, not factual rejection
Operational authority: Withdraws Raw file; history only where tracked
Behavioral-authority path: see declaration; consumer/channel/force/horizon are route-specific
Evidence source ID and local anchor: SRC-1, `cortex-vec/src/cortex_vec/reclaim.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

Route ID: [EPI-RTE-index-withdraw](#epi-rte-index-withdraw)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-notes](#epi-obj-notes)
Content/update relation: no content change
Transition or check target: Path and variants to index removal
Evaluator/condition and domain: Exact ID/prefix match in collection
Activation and timing: see declaration
Possible or observed result: Delete entries; conditional BM25 removal
Implemented force: Enforcing I/O
Epistemic authority and scope: No epistemic retraction; source Markdown remains
Operational authority: Removes indexed access but does not block direct Read
Behavioral-authority path: see declaration; consumer/channel/force/horizon are route-specific
Evidence source ID and local anchor: SRC-1, `cortex-vec/src/cortex_vec/store.py`
Claim IDs: none
Mismatch marker: none
Gap/limit: No observed operation supplied.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-vault-purpose](runtime.md#rt-clm-vault-purpose) | see record | SRC-1, `skills/using-cortex/SKILL.md`, doctrine/design | see record | [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), [RT-RTE-vault-search](runtime.md#rt-rte-vault-search) | None supplied | No outcome comparison | Retain/retrieve plumbing and prescribed curation exist | “Knowledge” does not certify claims. |
| [EPI-CLM-vault-index](#epi-clm-vault-index) | see record | SRC-1, `README.md`, doctrine/design | see record | [RT-RTE-direct-save](runtime.md#rt-rte-direct-save), [EPI-RTE-summary-build](#epi-rte-summary-build), [EPI-RTE-index-withdraw](#epi-rte-index-withdraw) | None supplied | No rebuild or fidelity experiment | Vault is authoritative storage relative to derived index | Generated summary is not pure copying; delete may leave BM25 stale. |

The every-hit comparable-cosine design statement is contrasted in [RT-RTE-vault-search](runtime.md#rt-rte-vault-search): supported no-vector/failed-backfill paths can return zero without measurement. This is a local score-interpretation defect, not evidence that every search result is irrelevant.

## Bounded conclusion

- Raw acquires assertions from sessions, with unknown truth warrant and potentially reduced context ([RT-RTE-session-capture](runtime.md#rt-rte-session-capture)). The classifier checks preservation strategy, not source truth. Prefix cleanup proves only body inclusion under its narrow equality domain ([EPI-RTE-prefix-check](#epi-rte-prefix-check)); deletion does not prove the remaining record preserves every header fact.
- Distill prescribes evidence-consuming human decisions about whether material is concrete/useful, where to retain it and whether a draft is acceptable. The mechanical ledger checks coverage/source identity, not those human decisions or factual correctness ([RT-RTE-distill-review](runtime.md#rt-rte-distill-review)). This is a useful retention criterion for a personal vault, not established acceptance of newly produced ampliative claims.
- Broadcast explicitly affords content-directed disagreement and rejection, unlike mere storage. Its human can preserve a conflict flag or replace a challenged claim; later page indexing makes that decision consequential. No actual criticism/revision episode, truth judgment or retained benefit is evidenced ([RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit)). Generic procedures do not establish particular theories or theory-builder conditions 1–4; each remains uninspected for actual vault theories. Exact-section edit affordances are not proof of fine-grained theory addressability.
- Evolve can save without the distill approval sequence; summary generation automatically admits an unchecked representation into retrieval. Summary semantics and draft transformations are indeterminate, not automatically conjecture or faithful compression ([RT-RTE-direct-save](runtime.md#rt-rte-direct-save), [EPI-RTE-summary-build](#epi-rte-summary-build)). No warranted novel domain conclusion is demonstrated.
- The evaluator derives correct-by-definition membership metrics from ranked lists and gold labels; its license ends at that domain. Gold proposal warns about review but does not enforce it; current adapter/index mismatch can confound comparisons. No scorecard consumer automatically promotes an adapter or revises policy ([EPI-RTE-eval-score](#epi-rte-eval-score), [EPI-RTE-query-propose](#epi-rte-query-propose)). This is implemented evaluation capacity, not observed quality or component causality.
- Retrieval and baton resume can shape later host behavior through ranking and interpreted context without a factual recheck ([RT-RTE-vault-search](runtime.md#rt-rte-vault-search), [RT-BAP-baton-context](runtime.md#rt-bap-baton-context)). Delivery and continuation are not acceptance or verified compliance. Withdrawal is local: index delete is not truth retraction, and stale BM25 can survive an early return ([EPI-RTE-index-withdraw](#epi-rte-index-withdraw)).
- Provider parameters are not shown to update through these calls; their exact versions/internal state are opaque, separately per [RT-CMP-sonnet](runtime.md#rt-cmp-sonnet), [RT-CMP-summary-model](runtime.md#rt-cmp-summary-model), [RT-CMP-embedding-model](runtime.md#rt-cmp-embedding-model), [RT-CMP-rerank-model](runtime.md#rt-cmp-rerank-model), [RT-CMP-claude-code](runtime.md#rt-cmp-claude-code). Retained page/baton adaptation is distinct from parameter learning. Improved future capacity, reflection's two causal directions and exercised self-improvement are not established by retention, indexing or generic conversational edits. Human vetoes remain integral to prescribed distill/broadcast, so these routes do not establish autonomous theory building. No unqualified system-wide epistemic verdict follows.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-raw
Label: Raw session record

SRC-1, `skills/cortex-distill/SKILL.md`. Mixed natural-language assertions and symbolic transcript/tool fragments; Markdown in the vault Raw tree. This is the retained output and later review input of [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) and [RT-RTE-distill-review](runtime.md#rt-rte-distill-review), not a duplicate route. No supplied object counterpart.

#### EPI-OBJ-notes
Label: Notes and Projects pages

SRC-1, `skills/cortex-evolve/SKILL.md`. Natural-language technical/project content plus symbolic YAML and links, Markdown files under vault Notes/Projects. Retained/input object shared by [RT-RTE-direct-save](runtime.md#rt-rte-direct-save), [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit) and [RT-RTE-vault-search](runtime.md#rt-rte-vault-search). Those are routes, not object counterparts.

#### EPI-OBJ-summary
Label: Generated bilingual summary

SRC-1, `cortex-vec/src/cortex_vec/store.py`. Natural-language model output stored as Chroma summary documents and embedded numerical representations. Distinct from source body: prefix-limited and unchecked. The direct-save route contains this index-generation object; provider component is [RT-CMP-summary-model](runtime.md#rt-cmp-summary-model).
Part of: [RT-RTE-direct-save](runtime.md#rt-rte-direct-save)

#### EPI-OBJ-query-gold
Label: Queries and gold paths

SRC-1, `cortex-vec/src/cortex_vec/eval/corpus.py`. JSONL query text and symbolic nonempty gold path list on caller-specified disk path. Gold denotes intended relevant pages. Separate evaluation input, no supplied counterpart; closest [RT-RTE-vault-search](runtime.md#rt-rte-vault-search) produces rankings rather than labels.

#### EPI-OBJ-scorecard
Label: Retrieval scorecard

SRC-1, `cortex-vec/src/cortex_vec/eval/run.py`. Symbolic per-query metrics as stdout JSON and natural-language/tabular Markdown aggregates to stderr or --out file. Derived assertions about ranked paths versus labels, not note truth. No supplied counterpart; [RT-RTE-vault-search](runtime.md#rt-rte-vault-search) supplies a production ranking mechanism, not the evaluator.

### Routes

#### EPI-RTE-summary-build
Label: Bilingual summary generation

SRC-1, `cortex-vec/src/cortex_vec/store.py`. Upsert/rebuild page fields → OpenAI → summary document. Store code owns the request and persistence; title/tags/body[:3000] shape a retrieval representation. This is a material generation part of the supplied direct-save container, not another save route.
Part of: [RT-RTE-direct-save](runtime.md#rt-rte-direct-save)

- Immediate return: Summary text on success; title/tags on exception.
- Later read-back: Summary documents are embedded and consumed by later vector search.
- Delegated visibility: Provider sees bounded document fields, not the whole session.
- Selection predicate: Each upsert/rebuild page, no independent fidelity gate.
- Invalidation or expiry: Replaced by upsert/rebuild or index deletion.
- Activation or effect: Changes search representation, not demonstrated correctness.
- Evidence limits: No paired generated summary/source, provider internals or retrieval effect supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> return resp.choices[0].message.content.strip()
> --- `cortex-vec/src/cortex_vec/store.py`

> except Exception:
>         return f"{title}. Tags: {tags}"
> --- `cortex-vec/src/cortex_vec/store.py`

#### EPI-RTE-eval-score
Label: Retrieval scoring and report

SRC-1, `cortex-vec/src/cortex_vec/eval/run.py`. Caller eval run → corpus validation → named adapters → deterministic metrics → JSON/report. Runner owns progression; labels are a caller-supplied answer oracle for relevance at K, not a factual truth oracle. This evaluator has no supplied runtime counterpart; closest [RT-RTE-vault-search](runtime.md#rt-rte-vault-search) supplies ranking rather than evaluating it. Mode: bounded caller corpus. Computation rejects malformed/missing fields or empty/non-list gold; missing gold paths only warn. Human label authorship is not established by loading a path. No evaluator result is wired here to promote a production adapter or change policy.

- Immediate return: Per-query scores plus aggregates and optional scorecard file.
- Later read-back: Report can persist for human inspection; no implemented production score consumer found in inspected runner/dispatcher.
- Delegated visibility: inapplicable — adapters are program calls, not isolated host agents; provider-backed search remains external.
- Selection predicate: Caller-selected adapters/K/query file; unknown adapter names warn and skip.
- Invalidation or expiry: Regenerate report; no automatic label or index freshness guarantee.
- Activation or effect: Measures path agreement and latency, not source truth, explanation or successful answer generation.
- Evidence limits: No evaluation run supplied. Grep/BM25 build from current docs, vector/hybrid init are no-ops using existing production indexes: unequal freshness prevents clean component attribution.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> sc = score.score_query(ranked, set(q["gold"]), k)
> --- `cortex-vec/src/cortex_vec/eval/run.py`

> precision = hits / k if k else 0.0
>     recall = hits / len(gold) if gold else 0.0
> --- `cortex-vec/src/cortex_vec/eval/score.py`

#### EPI-RTE-query-propose
Label: Candidate query corpus proposal

SRC-1, `cortex-vec/src/cortex_vec/eval/run.py`. Caller eval propose → current Notes/Projects docs → model queries → JSONL with source page as gold. Runner writes candidates automatically; user review is requested, not attested or enforced. This is a distinct evaluator-input generator, not [RT-RTE-direct-save](runtime.md#rt-rte-direct-save)'s vault page admission. Open generation over a bounded loaded corpus; no external relevance oracle. Rejection occurs on provider exception per document; users can edit labels or discard file. No rollback of an overwritten query file is implemented here.

- Immediate return: Proposed query count and JSONL at --queries.
- Later read-back: A later eval run loads this file and consumes gold without a confirmation field.
- Delegated visibility: OpenAI receives title/summary; provider response is query text.
- Selection predicate: One query per loaded doc with successful response; code assigns gold to that doc.
- Invalidation or expiry: Caller may edit/regenerate; output write replaces existing file.
- Activation or effect: Creates possible reference judgments for later metrics, not verified relevance.
- Evidence limits: No proposed corpus instance or user confirmation supplied.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> "gold": [d["id"]],
>             "type": "single-note",
>             "note": "AUTO-PROPOSED — review query + gold before use",
> --- `cortex-vec/src/cortex_vec/eval/run.py`

#### EPI-RTE-prefix-check
Label: Raw prefix and repo comparison

SRC-1, `cortex-vec/src/cortex_vec/reclaim.py`. Queue → _body and _repo → scan superseded/refused lists. Code owns comparison; optional keep chooses survivor, otherwise pairwise queue scan. This is the deterministic checking subfunction of cleanup mentioned inside [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), also independently exposed by CLI, not a duplicate whole capture route. Mode: bounded file comparison; answer reference is actual survivor body. It tests equality/prefix, not inferred semantic equivalence. No human content judgment is part of scan.

- Immediate return: Candidate paths and cross-repo refusal messages.
- Later read-back: inapplicable — scan is current-call state; removal decisions consume it immediately.
- Delegated visibility: inapplicable — local file comparison launches no model agent.
- Selection predicate: Nonempty body prefix with equal repo; equal bodies keep later path.
- Invalidation or expiry: Recomputed on scan; filesystem mutations between check and deletion are not locked here.
- Activation or effect: Establishes that candidate conversation-line sequence is covered by survivor.
- Evidence limits: Frontmatter and pre-turn headers are omitted from comparison; missing repo matches another missing repo; no semantic or metadata-loss guarantee.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> bool(candidate)
>         and len(candidate) <= len(survivor)
>         and survivor[: len(candidate)] == candidate
> --- `cortex-vec/src/cortex_vec/reclaim.py`

> lines.append(line.rstrip("\n"))
> --- `cortex-vec/src/cortex_vec/reclaim.py`

#### EPI-RTE-prefix-remove
Label: Apply superseded Raw removal

SRC-1, `cortex-vec/src/cortex_vec/reclaim.py`. Scan result → apply_reclaim → git rm, fallback unlink → actual removed list. Code owns removal, caller selects --apply or SessionEnd cleanup. Distinct disposition from prefix check; broader capture counterpart [RT-RTE-session-capture](runtime.md#rt-rte-session-capture) only mentions this adjunct. Non-apply dispatch lists candidates without removing. Cross-repo refusal leaves candidate. Per-file human approval is not required. Recovery via Git only for tracked history; no guaranteed untracked recovery.

- Immediate return: Paths actually gone; refusals on stderr.
- Later read-back: Future queue no longer sees removed file; source surviving Raw remains loadable.
- Delegated visibility: inapplicable — deletion is local software, not agent delegation.
- Selection predicate: --apply consumes scan superseded list; hook invocation is an alternate automatic caller.
- Invalidation or expiry: Removed files cease active existence; historical Git recovery depends on previous tracking.
- Activation or effect: Physically withdraws selected Raw records, not epistemic refutation.
- Evidence limits: No successful removal or recovery observed; check/removal not a transactional snapshot.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> if vault is not None and _git_rm(vault, path):
>             removed.append(path)
>             continue
>         try:
>             path.unlink()
> --- `cortex-vec/src/cortex_vec/reclaim.py`

#### EPI-RTE-index-withdraw
Label: Path-level index withdrawal

SRC-1, `cortex-vec/src/cortex_vec/store.py`. CLI delete path → remove Chroma base/repo/summary ID variants → BM25 delete when vector entries existed. Store owns effects. Cleanup helper also runs before upsert. Distinct exposed withdrawal omitted from [RT-RTE-direct-save](runtime.md#rt-rte-direct-save)'s indexing account; does not replace that route. Caller chooses path; software admits deletion with no truth criterion or human confirmation. Mode: caller-directed maintenance. It can be reversed by upsert/rebuild if source persists; no automatic rollback.

- Immediate return: Deleted count or not-indexed diagnostic.
- Later read-back: Later vector search lacks removed entries; source Markdown remains directly readable. BM25 can remain if no Chroma stale entries trigger early return.
- Delegated visibility: inapplicable — local deletion does not delegate a model call.
- Selection predicate: ID equals rel_path or starts with rel_path plus ::; no content-level refutation.
- Invalidation or expiry: Upsert/rebuild can reintroduce source; no tombstone preventing that.
- Activation or effect: Changes indexed access, not epistemic reliance everywhere.
- Evidence limits: Vector-empty early return skips BM25 cleanup; no cross-store transaction or universal withdrawal.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> stale = [i for i in all_ids if i == rel_path or i.startswith(f"{rel_path}::")]
> --- `cortex-vec/src/cortex_vec/store.py`

> if not stale:
>         # Idempotent: the goal state (not indexed) already holds.
>         print(f"cortex-vec: {rel_path} not indexed; nothing to delete",
>               file=sys.stderr)
>         _emit(args, [], {"deleted": 0, "path": rel_path})
>         return
> --- `cortex-vec/src/cortex_vec/store.py`

Deterministic deduction, not target execution: in [EPI-RTE-prefix-check](#epi-rte-prefix-check), a candidate file with pre-turn metadata followed by `### User\nA\n` yields the line array `["### User", "A"]`. A survivor whose first conversation lines are `### User\nA\n### Claude\nB\n` satisfies _covers. With matching repo, scan can select the candidate for removal even if its pre-turn metadata differs. This establishes body preservation only. Likewise, [EPI-RTE-eval-score](#epi-rte-eval-score) takes ranked `["Notes/A.md", "Notes/B.md"]`, gold `{"Notes/B.md"}`, K=2 to P=0.5, R=1, reciprocal rank=0.5 and hit=true by inspected arithmetic. Those numbers do not establish that B is genuinely relevant.

Additional load-bearing support (SRC-1, doctrine/design for skills; implementation for Python):

> If the Raw contains a claim that directly contradicts a claim in the page:
>
> 1. Locate the conflicting claim in the page.
> 2. Propose inline flag at that location:
> --- `skills/cortex-broadcast/SKILL.md`

> Free-form (e.g., "the new info is correct, delete the old claim")
>      → rewrite the old claim with new info; no `⚠️` flag
> --- `skills/cortex-broadcast/SKILL.md`

> 3. Add `repos:` to frontmatter if repo-specific
> 4. Present draft to user for confirmation
> 5. Write to vault using Obsidian Flavored Markdown (wikilinks, frontmatter, callouts)
> --- `skills/cortex-distill/SKILL.md`

> "content": _SUMMARY_PROMPT.format(title=title, tags=tags, body=body[:3000]),
> --- `cortex-vec/src/cortex_vec/store.py`

> if cand_repo != keep_repo:
>                 result.refused.append(
>                     CrossRepoPair(p, keep_path, cand_repo, keep_repo)
>                 )
>                 continue
> --- `cortex-vec/src/cortex_vec/reclaim.py`

Additional evaluator support (SRC-1):

> for idx, p in enumerate(top_k):
>         if p in gold:
>             reciprocal_rank = 1.0 / (idx + 1)
>             break
> --- `cortex-vec/src/cortex_vec/eval/score.py`

> if missing:
>         print(f"WARNING: gold paths missing from vault: {missing}", file=sys.stderr)
> --- `cortex-vec/src/cortex_vec/eval/run.py`

> class HybridAdapter:
>     """Full production fusion.search (vector + BM25, RRF)."""
>     name = "hybrid"
>
>     def init(self, docs):
>         pass
> --- `cortex-vec/src/cortex_vec/eval/adapters.py`

> if not isinstance(row["gold"], list) or not row["gold"]:
>                 raise ValueError(f"line {lineno}: 'gold' must be a non-empty list")
> --- `cortex-vec/src/cortex_vec/eval/corpus.py`

### Claims

#### EPI-CLM-vault-index
Label: Vault truth source and derived index

SRC-1, `README.md`, doctrine/design. The vault is designated authoritative storage and the vector index rebuildable, not an infallible truth oracle. Closest supplied [RT-CLM-vault-purpose](runtime.md#rt-clm-vault-purpose) names the user's knowledge base; this claim is distinct in asserting the vault/index authority relationship.

> **Design philosophy:** the vault is the source of truth (plain markdown +
> git); the vector store is just a rebuildable derived index.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
