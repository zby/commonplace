---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Omni-Memory epistemic routes: candidate admission, source integrity, verified-tier reliance and withdrawal at the frozen revision."
run-id: AAS-2026-11-08-omni-memory-09378abbfe6b-01
reviewed-boundary: "20f9f9ffd7ece0c6514542677ba6a549841f5536"
---

# Omni-Memory epistemic report

## Source-and-claim boundary

Question: what licenses reliance on retained project claims, and which consumers give that license consequences? The selected whole-system scope and exclusions are those in [Boundary and evidence](boundary.md#boundary-and-evidence); source identity and evidence layers are in its [Source register](boundary.md#source-register). All new inspections below use SRC-1 at the same revision; checkout HEAD matched the pin. Implementation and doctrine/design establish routes, not exercised behavior. No execution evidence or causal comparison was supplied.

Assessed families: acquisition/extraction, noise admission, file-identity checks, trust-tier promotion/withdrawal, relevance feedback, duplication/conflict handling, quarantine/restoration, and delivery. Public/design warrant claims: [RT-CLM-verified-context](runtime.md#rt-clm-verified-context), [EPI-CLM-earned-verified](#epi-clm-earned-verified), [EPI-CLM-hygiene-truth](#epi-clm-hygiene-truth). No single system-wide negative follows from this coverage.

| Entry point or operation | Source path (SRC-1) | Coverage and records | Limit / conclusion prevented |
|---|---|---|---|
| Frozen CLI dispatch and options | `omni_memory/cli.py` | Direct read of main/dispatch, hook dispatcher, recall, check, used, gc, doctor ranges; [RT-RTE-local-edits](runtime.md#rt-rte-local-edits) | Setup/status/config/gain internals not fully read directly; no exhaustive command-correctness conclusion |
| Plugin hooks | `hooks/hooks.json`, `omni_memory/cli.py` | Direct event wiring and hook read; [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission), [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery) | Actual host delivery not observed; no registered model-tool API appears in this inspected hook/CLI surface |
| Capture and model build/artifacts | `omni_memory/session_memory.py`, `omni_memory/cleanup.py`; supplied runtime: `omni_memory/llm.py`, `omni_memory/context.py`, `omni_memory/artifacts.py` | Direct capture/prompts/heuristics/batch/filter reads; [RT-RTE-build-artifacts](runtime.md#rt-rte-build-artifacts), [EPI-RTE-candidate-filter](#epi-rte-candidate-filter), [EPI-RTE-filter-admission](#epi-rte-filter-admission) | No provider outputs tied to routes; semantic fidelity and accepted novel claims not established |
| Remember/global, edit, merge, reanchor, resolve, forget | `omni_memory/store.py`, `omni_memory/serve.py`, `omni_memory/cli.py` | Direct store and dashboard mutation reads; supplied [RT-RTE-local-edits](runtime.md#rt-rte-local-edits); [EPI-RTE-merge-disposition](#epi-rte-merge-disposition) | Caller identity does not authenticate human review; reanchor clears flags without semantic test |
| Refresh / doctor / source integrity / graduation | `omni_memory/branch.py`, `omni_memory/staleness.py`, `omni_memory/cli.py` | Direct full_refresh, signature gate, recompute/reconcile/graduation/demotion, doctor entry; [EPI-RTE-integrity-check](#epi-rte-integrity-check), [EPI-RTE-tier-graduation](#epi-rte-tier-graduation), [EPI-RTE-tier-withdrawal](#epi-rte-tier-withdrawal) | Graph propagation helpers and Git adapter internals not fully audited; no graph/source-enumeration completeness proof |
| Citation feedback and point of use | `omni_memory/cli.py`, `omni_memory/session_memory.py`; supplied `omni_memory/witness.py` | Direct citation parsing, bump_uses and callers; supplied [RT-RTE-use-check](runtime.md#rt-rte-use-check) | No semantic success result consumed; later agent response to warning unknown |
| Inject / recall / AGENTS / digest / OpenCode | Direct `omni_memory/rank.py`, `omni_memory/store.py`, `omni_memory/cli.py`; supplied `omni_memory/inject.py`, `omni_memory/agentsmd.py`, `omni_memory/install.py` | [EPI-RTE-query-ranking](#epi-rte-query-ranking), supplied [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-BAP-agent-context](runtime.md#rt-bap-agent-context) | Different projections do not preserve identical caveats; full digest/graph/dashboard display transformations not directly inspected here |
| Branch merge / duplication / conflict | `omni_memory/store.py`, supplied `omni_memory/branch.py` | Direct overlap/reconcile/resolve/history reads; [EPI-RTE-merge-reconcile](#epi-rte-merge-reconcile), [EPI-RTE-merge-disposition](#epi-rte-merge-disposition) | Text overlap is not logical equivalence; no complete contradiction detector |
| gc / check / restore / purge | `omni_memory/eviction.py`, `omni_memory/store.py`, `omni_memory/cli.py` | Direct full sweep and score, store quarantine/restore/purgeable; [EPI-RTE-eviction-check](#epi-rte-eviction-check), [EPI-RTE-quarantine-disposition](#epi-rte-quarantine-disposition) | Heuristic withdrawal not epistemic refutation |
| Team / snapshot | Supplied `omni_memory/team.py`, `omni_memory/store.py`, `omni_memory/cli.py` | [RT-RTE-shared-import](runtime.md#rt-rte-shared-import); direct clamp_evidence | Import trust choice and Git author labels do not authenticate source truth |
| Health/system maps, savings, collector, browser, tests | `omni_memory/healthmap.py`, `omni_memory/systemmap.py`, `omni_memory/savings.py`, `omni_memory/collector.py`, `omni_memory/static/index.html`, `tests/` | Available but not deeply inspected in this member; boundary/runtime cover existence and roles | No system-complete negative about evaluators, map fidelity, savings or diagnostic correctness; test definitions would not supply executed outcomes |

Missing run-linked transcripts, DB transitions and genuine context deliveries prevent conclusions that these routes operated. Missing downstream agent decisions prevent activation claims. Missing controlled interventions prevent benefit/component attribution. Provider internals and exact weights remain inaccessible in this boundary: see separately [RT-CMP-agent-cli](runtime.md#rt-cmp-agent-cli), [RT-CMP-gemini](runtime.md#rt-cmp-gemini), [RT-CMP-openai](runtime.md#rt-cmp-openai), [RT-CMP-anthropic](runtime.md#rt-cmp-anthropic). No local parameter-update route is established by those adapters; no inference about remote weight updates follows.

## Epistemic-object inventory

Fields owned by records say see rather than recopy their descriptions.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-candidates](#epi-obj-candidates) | Project propositions or task/policy text; scope per item | see [EPI-OBJ-candidates](#epi-obj-candidates) | SRC-1 `omni_memory/session_memory.py` | A kind/evidence label cannot individuate a true proposition |
| [EPI-OBJ-memory](#epi-obj-memory) | Retained textual project assertions; also todos and policies | see [EPI-OBJ-memory](#epi-obj-memory) | SRC-1 `omni_memory/store.py` | No supplied live DB or accepted candidate instance |
| [EPI-OBJ-evidence](#epi-obj-evidence) | File identity/change claims; tiers and counters are symbolic metadata | see [EPI-OBJ-evidence](#epi-obj-evidence) | SRC-1 `omni_memory/staleness.py` | Source identity does not establish text follows from sources |
| [EPI-OBJ-artifacts](#epi-obj-artifacts) | Generated repository explanations and maps | see [EPI-OBJ-artifacts](#epi-obj-artifacts) | SRC-1 `omni_memory/artifacts.py` via [RT-RTE-build-artifacts](runtime.md#rt-rte-build-artifacts) | Content-specific relation not determinable without input/output pairs |
| [RT-OBJ-inject-cache](runtime.md#rt-obj-inject-cache) | None; delivery control | see [RT-OBJ-inject-cache](runtime.md#rt-obj-inject-cache) | SRC-1 `omni_memory/cli.py` | Delivery frequency is not endorsement |
| [RT-CMP-agent-cli](runtime.md#rt-cmp-agent-cli), [RT-CMP-gemini](runtime.md#rt-cmp-gemini), [RT-CMP-openai](runtime.md#rt-cmp-openai), [RT-CMP-anthropic](runtime.md#rt-cmp-anthropic) | Distributed model state not inspectable as localized claims | see component records | SRC-1 `omni_memory/llm.py` | Hidden processing, exact version and parameter mutation not determinable |

## Authority-route ledger

All observed-run results are uninspected. Status below is architectural. Each function remains separate even where a shared route implements more than one function. Generic route details remain owned by the cited declarations.

Route ID: [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidates](#epi-obj-candidates)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Raw transcript → model candidate text
Evaluator/condition and domain: Model extracts under EXTRACTION_PROMPT; optional fallback heuristic has a separate transformation below
Activation and timing: Capture/precompact/session-end or explicit capture
Possible or observed result: Candidate array; no observed operation supplied.
Implemented force: candidate generation only
Epistemic authority and scope: JSON import acquires caller content; original warrant unknown; heuristic preserves selected wording but drops role context
Operational authority: Proposals proceed to filtering, not truth acceptance
Behavioral-authority path: model/heuristic → remember_many; permissive candidate supply; same invocation
Evidence source ID and local anchor: SRC-1 `omni_memory/session_memory.py`; see [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission).
Claim IDs: none
Mismatch marker: none
Gap/limit: Model reshaping/entailed derivation/ampliative conjecture not decidable from instructions alone; need item-level inputs and outputs

Route ID: [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidates](#epi-obj-candidates)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Caller JSON → Python candidate list
Evaluator/condition and domain: JSON parser plus accepted envelopes; no truth evaluator
Activation and timing: Explicit capture or other JSON ingestion before remember_many
Possible or observed result: Imported assertions; implementation only
Implemented force: Candidate supply; admission separate
Epistemic authority and scope: Original source warrant unknown; import does not produce a newly accepted claim
Operational authority: Supplies items to batch filter
Behavioral-authority path: caller → parser → remember_many; permissive; current invocation then retained rows if admitted
Evidence source ID and local anchor: SRC-1 `omni_memory/session_memory.py`; see [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission).
Claim IDs: none
Mismatch marker: none
Gap/limit: Syntax and shape are not truth checks

Route ID: [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidates](#epi-obj-candidates)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Transcript lines → selected de-framed line text and category
Evaluator/condition and domain: Deterministic regex / length rules; not semantic validation
Activation and timing: Fallback heuristic or document scan
Possible or observed result: Up to 40 candidate lines; implementation deduction below, not target execution
Implemented force: Candidate generation and selection
Epistemic authority and scope: Selected wording retained, role framing removed; speaker attribution is degraded
Operational authority: Selected candidates proceed to stricter doc/heuristic filtering
Behavioral-authority path: _heuristic_extract → cleanup → remember_many; permissive; same call
Evidence source ID and local anchor: SRC-1 `omni_memory/session_memory.py`; see [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission).
Claim IDs: none
Mismatch marker: none
Gap/limit: No new semantic proposition derived by the regex; dropping role context does not establish warranted project assertion

Concrete source deduction: the single input line `assistant: GET /orders returns orders.` is stripped to `GET /orders returns orders.`, passes the 12–240 character window, matches the first HTTP-method/path pattern and becomes an endpoint candidate with no file anchors. This is the extractor's result before cleanup, not a claim that it would be accepted or true. An assistant's assertion becomes de-framed project-memory text; preserving words does not preserve attribution.

> line = _ROLE_PREFIX.sub("", line.strip("-* \t")).strip()
> --- `omni_memory/session_memory.py`

> if len(line) < 12 or len(line) > 240:
>             continue
>         for pat, kind in _PATTERNS:
>             if re.search(pat, line, re.I):
>                 out.append({"kind": kind, "text": line,
>                             "files": _real_files(root, line) if root else []})
>                 break
>     return out[:40]
> --- `omni_memory/session_memory.py`


Route ID: [RT-RTE-build-artifacts](runtime.md#rt-rte-build-artifacts)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-artifacts](#epi-obj-artifacts)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Repository context → model facts/docs
Evaluator/condition and domain: Prompted model; artifact length check only
Activation and timing: Explicit build, with independent AI/docs generation switches
Possible or observed result: Facts/docs; no observed operation supplied.
Implemented force: candidate generation, length admission for docs
Epistemic authority and scope: No semantic warrant established
Operational authority: Stores facts or writes docs for later readers
Behavioral-authority path: build model → store/artifact writer → context/dashboard; permissive; later reads
Evidence source ID and local anchor: SRC-1 `omni_memory/artifacts.py`; see [RT-RTE-build-artifacts](runtime.md#rt-rte-build-artifacts).
Claim IDs: none
Mismatch marker: none
Gap/limit: Truncated context and opaque outputs; not enough to call every result a novel conjecture

Route ID: [EPI-RTE-candidate-filter](#epi-rte-candidate-filter)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidates](#epi-obj-candidates)
Content/update relation: no content change
Transition or check target: Candidate storage-worthiness, not propositional truth
Evaluator/condition and domain: Python length, structure, chatter and anchor rules; doc/heuristic stricter
Activation and timing: remember_many before storage
Possible or observed result: keep/drop Boolean; no observed operation supplied.
Implemented force: enforcing at batch gate
Epistemic authority and scope: Only conformity to heuristic shape rules
Operational authority: Blocked candidates do not enter batch storage
Behavioral-authority path: remember_many → filter_items → kept list; enforcing; admission invocation
Evidence source ID and local anchor: SRC-1 `omni_memory/cleanup.py`; see [EPI-RTE-candidate-filter](#epi-rte-candidate-filter).
Claim IDs: none
Mismatch marker: none
Gap/limit: Manual remember and dashboard bypass this batch gate

Route ID: [EPI-RTE-filter-admission](#epi-rte-filter-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-candidates](#epi-obj-candidates)
Content/update relation: no content change
Transition or check target: Whether a batch candidate proceeds to remember
Evaluator/condition and domain: filter result and source-sensitive ceiling; no semantic oracle
Activation and timing: After candidate check
Possible or observed result: Dropped count or admitted row; no observed operation supplied.
Implemented force: enforcing admission
Epistemic authority and scope: Storage eligibility, not evidence-consuming acceptance of meaning
Operational authority: Admitted text becomes eligible memory
Behavioral-authority path: capture/build → remember_many → SQLite; permissive; later sessions
Evidence source ID and local anchor: SRC-1 `omni_memory/session_memory.py`; see [EPI-RTE-filter-admission](#epi-rte-filter-admission).
Claim IDs: none
Mismatch marker: none
Gap/limit: Admission criterion is not truth acceptance

Route ID: [EPI-RTE-staleness-check](#epi-rte-staleness-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-evidence](#epi-obj-evidence)
Content/update relation: no content change
Transition or check target: Whether anchored files or mapped symbols changed since the memory's commit
Evaluator/condition and domain: Git diff plus available code-graph symbol/dependent mapping; file fallback
Activation and timing: recompute during check or refresh orchestration
Possible or observed result: is_stale Boolean and touched anchors; implementation only
Implemented force: Supplies separate flag update
Epistemic authority and scope: Possible source-relevant change, not factual falsity
Operational authority: Selects stale/clear metadata update
Behavioral-authority path: recompute predicates → set_stale; enforcing locally; maintenance call
Evidence source ID and local anchor: SRC-1 `omni_memory/staleness.py`; see [EPI-RTE-staleness-check](#epi-rte-staleness-check).
Claim IDs: none
Mismatch marker: none
Gap/limit: Graph helpers not fully audited; unknown/missing commit/files may skip evaluation

Route ID: [EPI-RTE-staleness-flag](#epi-rte-staleness-flag)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-evidence](#epi-obj-evidence)
Content/update relation: non-truth-apt policy/content update: staleness metadata
Transition or check target: Mark or clear possible staleness without rewriting memory
Evaluator/condition and domain: is_stale and prior flag; Python decides
Activation and timing: After recompute predicate
Possible or observed result: SQLite stale flag, timestamp and touched files; implementation only
Implemented force: Persisted warning/retention input
Epistemic authority and scope: Alert to recheck, not acceptance/rejection of sentence truth
Operational authority: Warnings on marked reads; uncited stale age contributes to eviction
Behavioral-authority path: SQLite stale → rendering and eviction; advisory to host, retention scoring; subsequent invocations
Evidence source ID and local anchor: SRC-1 `omni_memory/staleness.py`; see [EPI-RTE-staleness-flag](#epi-rte-staleness-flag).
Claim IDs: none
Mismatch marker: none
Gap/limit: Not every projection reproduces warnings; drift demotion is separate

Route ID: [EPI-RTE-integrity-check](#epi-rte-integrity-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-evidence](#epi-obj-evidence)
Content/update relation: no content change
Transition or check target: Identity/existence of recorded source-file bytes
Evaluator/condition and domain: Git digest comparison; worst recorded anchor wins
Activation and timing: reconcile / graduation during full_refresh; doctor also reconciles
Possible or observed result: FRESH / DRIFTED / ORPHANED; legacy uncheckable; no observed operation supplied.
Implemented force: measurement; disposition separate
Epistemic authority and scope: Identity of compared sources only, conditional on declared anchor map
Operational authority: Supplies demotion and promotion predicates; source-loss stale flag input
Behavioral-authority path: reconcile/graduate → verdict → metadata consumers; enforcing locally; refresh horizon
Evidence source ID and local anchor: SRC-1 `omni_memory/staleness.py`; see [EPI-RTE-integrity-check](#epi-rte-integrity-check).
Claim IDs: [EPI-CLM-earned-verified](#epi-clm-earned-verified)
Mismatch marker: warrant narrower than claim
Gap/limit: Not semantic entailment; incomplete source maps remain possible

Route ID: [EPI-RTE-tier-graduation](#epi-rte-tier-graduation)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-evidence](#epi-obj-evidence)
Content/update relation: non-truth-apt policy/content update: evidence tier
Transition or check target: Promote active stated memory with positive uses and matching nonempty blob map
Evaluator/condition and domain: Code decides on citation counter plus FRESH; no outcome-success evaluator
Activation and timing: full_refresh after reconcile; skip on unchanged refresh signature possible
Possible or observed result: evidence becomes verified; no observed operation supplied.
Implemented force: ranking/retention metadata write
Epistemic authority and scope: Evidence of citation and unchanged mapped bytes, not confirmed proposition
Operational authority: Eligible query ranking boost and eviction shield
Behavioral-authority path: SQLite evidence → rank.score_one / eviction.evict_score; ranking; until changed
Evidence source ID and local anchor: SRC-1 `omni_memory/staleness.py`; see [EPI-RTE-tier-graduation](#epi-rte-tier-graduation).
Claim IDs: [EPI-CLM-earned-verified](#epi-clm-earned-verified)
Mismatch marker: citation is not outcome success
Gap/limit: AI capture/build/doc ceiling inferred prevents direct graduation from those initial tiers

Route ID: [EPI-RTE-tier-withdrawal](#epi-rte-tier-withdrawal)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-evidence](#epi-obj-evidence)
Content/update relation: non-truth-apt policy/content update: evidence tier and stale flag
Transition or check target: Revoke verified on mapped-source drift or loss
Evaluator/condition and domain: reconcile digest verdict; legacy handling differs
Activation and timing: Refresh or doctor reconcile
Possible or observed result: verified → stated; orphan flagged stale; drift counted; no observed operation supplied.
Implemented force: enforcing metadata update
Epistemic authority and scope: Withdraws old source-identity assurance, not disproof
Operational authority: Removes tier boost/shield on later score calculation
Behavioral-authority path: reconcile → SQLite → rank/eviction; enforcing locally; later reads
Evidence source ID and local anchor: SRC-1 `omni_memory/staleness.py`; see [EPI-RTE-tier-withdrawal](#epi-rte-tier-withdrawal).
Claim IDs: [EPI-CLM-earned-verified](#epi-clm-earned-verified)
Mismatch marker: none
Gap/limit: Content remains; source drift is not necessarily factual error

Route ID: [EPI-RTE-query-ranking](#epi-rte-query-ranking)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: no content change
Transition or check target: Which scoped active memories surface for a query
Evaluator/condition and domain: Code lexical/file/graph scoring with uses and evidence multipliers
Activation and timing: Store query path; ordinary empty-query browse differs
Possible or observed result: Sorted matching rows; zero-match omitted; no observed operation supplied.
Implemented force: ranking
Epistemic authority and scope: Relevance signal only; not truth validation
Operational authority: Changes memory order/delivery to model
Behavioral-authority path: Store.memories → rank → inject/recall; ranking; each query
Evidence source ID and local anchor: SRC-1 `omni_memory/rank.py`; see [EPI-RTE-query-ranking](#epi-rte-query-ranking).
Claim IDs: [EPI-CLM-earned-verified](#epi-clm-earned-verified)
Mismatch marker: none
Gap/limit: No-query/no-context path sorts by updated; boost is not universal

Route ID: [EPI-RTE-merge-reconcile](#epi-rte-merge-reconcile)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: no content change
Transition or check target: Text overlap / shared-symbol claim-kind collision
Evaluator/condition and domain: Token-set Jaccard; anchor-relaxed threshold; kind/symbol rules
Activation and timing: Add or merged-branch reconciliation
Possible or observed result: Similarity or conflict classification; no observed operation supplied.
Implemented force: heuristic result; disposition separate
Epistemic authority and scope: Text overlap and co-anchoring only
Operational authority: Feeds supersession / conflict recording
Behavioral-authority path: Store._similar → duplicate/reconcile callers; enforcing local predicates; mutation invocation
Evidence source ID and local anchor: SRC-1 `omni_memory/store.py`; see [EPI-RTE-merge-reconcile](#epi-rte-merge-reconcile).
Claim IDs: none
Mismatch marker: none
Gap/limit: Negation can preserve high token overlap; distinct claims can share a symbol

Route ID: [EPI-RTE-merge-disposition](#epi-rte-merge-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: no content change
Transition or check target: Retire overlap losers; mark collisions; caller resolves keep/both
Evaluator/condition and domain: Code applies citation/tier/tie rules; caller decides explicit resolution
Activation and timing: Add, branch merge, CLI/dashboard resolve or merge
Possible or observed result: Superseded/active rows and conflict flags; dashboard merge unions files; no observed operation supplied.
Implemented force: enforcing retrieval membership
Epistemic authority and scope: No checked logical contradiction or truth winner
Operational authority: Changes active retrieval set; conflict warns instead of blocking
Behavioral-authority path: Store statuses/conflicts → active-row selectors and marker; enforcing membership/advisory conflict; later sessions
Evidence source ID and local anchor: SRC-1 `omni_memory/store.py`; see [EPI-RTE-merge-disposition](#epi-rte-merge-disposition).
Claim IDs: none
Mismatch marker: none
Gap/limit: Not post-acceptance lifecycle integration; source-file union does not prove support

Route ID: [EPI-RTE-eviction-check](#epi-rte-eviction-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: no content change
Transition or check target: Retention eligibility, not falsehood
Evaluator/condition and domain: Branch state, staleness, age, kind, confidence, citations, tier; protected exemption; retro-noise filter
Activation and timing: gc and check; dry_run computes without mutation
Possible or observed result: Score threshold / noise / purgeable lists; no observed operation supplied.
Implemented force: selection recommendation consumed by sweep
Epistemic authority and scope: Heuristic retention priority only
Operational authority: Selects withdrawal candidates
Behavioral-authority path: evict_score/is_noise → sweep → quarantine; enforcing unless dry run; maintenance invocation
Evidence source ID and local anchor: SRC-1 `omni_memory/eviction.py`; see [EPI-RTE-eviction-check](#epi-rte-eviction-check).
Claim IDs: [EPI-CLM-hygiene-truth](#epi-clm-hygiene-truth)
Mismatch marker: use is not demonstrated truth
Gap/limit: Uses shield and verified tier can protect false but cited text

Route ID: [EPI-RTE-quarantine-disposition](#epi-rte-quarantine-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: no content change
Transition or check target: Active retrieval membership / deletion
Evaluator/condition and domain: sweep result; explicit purge; caller restore/forget
Activation and timing: check/gc maintenance or explicit edits
Possible or observed result: abandoned rows, optional deletion, restore active with noise_exempt; no observed operation supplied.
Implemented force: enforcing membership
Epistemic authority and scope: No semantic rejection or acceptance established
Operational authority: Quarantined excluded from default active retrieval; restored reeligible
Behavioral-authority path: SQLite status → Store.memories → context; enforcing; cross-session
Evidence source ID and local anchor: SRC-1 `omni_memory/eviction.py`; see [EPI-RTE-quarantine-disposition](#epi-rte-quarantine-disposition).
Claim IDs: [EPI-CLM-hygiene-truth](#epi-clm-hygiene-truth)
Mismatch marker: none
Gap/limit: Restore waives retro-noise, not score eviction; purge removes history rows

Route ID: [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: no content change
Transition or check target: Admitted rows → SQLite
Evaluator/condition and domain: Store writes after caller-specific gates
Activation and timing: Following admission
Possible or observed result: Persisted memory plus anchors; no observed operation supplied.
Implemented force: durable retention
Epistemic authority and scope: Retention does not accept a proposition
Operational authority: Makes active rows reachable in later calls
Behavioral-authority path: SQLite → Store.memories → context; permissive; cross-session
Evidence source ID and local anchor: SRC-1 `omni_memory/store.py`; see [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission).
Claim IDs: none
Mismatch marker: none
Gap/limit: No post-acceptance lifecycle integration established merely by storage

Route ID: [RT-RTE-shared-import](runtime.md#rt-rte-shared-import)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: External shard/snapshot → local memory
Evaluator/condition and domain: Shape/ID/noise validation and tier clamping; explicit trust exception
Activation and timing: Sync/start/snapshot import
Possible or observed result: Local rows; no observed operation supplied.
Implemented force: admission and retention
Epistemic authority and scope: External source warrant unknown; tier ceilings reduce label authority but do not validate meaning
Operational authority: Makes imported content eligible for delivery
Behavioral-authority path: JSON → importer → SQLite → context; permissive; later sessions
Evidence source ID and local anchor: SRC-1 `omni_memory/store.py`; see [RT-RTE-shared-import](runtime.md#rt-rte-shared-import).
Claim IDs: none
Mismatch marker: none
Gap/limit: Automatic import does not establish human review; later graduation can promote stated imported rows

Route ID: [RT-RTE-use-check](runtime.md#rt-rte-use-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-evidence](#epi-obj-evidence)
Content/update relation: no content change
Transition or check target: Pinned mapped sources versus current file digests
Evaluator/condition and domain: Witness comparison; bound>0 needed for valid coverage
Activation and timing: used command or retrospective capture citation scan
Possible or observed result: Clean/changed/missing-source diagnostics; no observed operation supplied.
Implemented force: advisory to host; durable warning events possible
Epistemic authority and scope: Source movement only, not claim truth or action success
Operational authority: Warns revalidate/re-source; no action lock
Behavioral-authority path: witness → stdout/stderr/events → host; advisory; current use/later session
Evidence source ID and local anchor: SRC-1 `omni_memory/witness.py`; see [RT-RTE-use-check](runtime.md#rt-rte-use-check).
Claim IDs: [RT-CLM-verified-context](runtime.md#rt-clm-verified-context)
Mismatch marker: verification is source-bounded
Gap/limit: See route limits, including observation-bound versus pin-time binding

Route ID: [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory](#epi-obj-memory)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Selected rows → narrower rendered context
Evaluator/condition and domain: Scope/ranking/budget/clipping rules; AGENTS projection differs
Activation and timing: Start/pull/auto prompt/OpenCode compaction
Possible or observed result: Instructions and selected textual claims; no observed operation supplied.
Implemented force: advisory content; software selects projection
Epistemic authority and scope: No semantic license beyond underlying sources; clipping and caveat omission can degrade warrant visibility
Operational authority: Host may rely on text without another enforced check
Behavioral-authority path: See [RT-BAP-agent-context](runtime.md#rt-bap-agent-context)
Evidence source ID and local anchor: SRC-1 `omni_memory/inject.py`; see [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery).
Claim IDs: [RT-CLM-verified-context](runtime.md#rt-clm-verified-context)
Mismatch marker: verified heading is not per-row proof
Gap/limit: Reshaping is projection only; does not certify preservation of complete propositions or causal chains

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-verified-context](runtime.md#rt-clm-verified-context) | see claim | SRC-1 `omni_memory/skills/omni-memory/SKILL.md`; doctrine/design | see claim | [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery), [RT-RTE-use-check](runtime.md#rt-rte-use-check) | none supplied | Host compliance external; no intervention | Instructions and source warnings wired | Not semantic verification or enforced host obedience |
| [EPI-CLM-earned-verified](#epi-clm-earned-verified) | see claim | SRC-1 `omni_memory/staleness.py`; doctrine/design embedded in code | see claim | [EPI-RTE-integrity-check](#epi-rte-integrity-check), [EPI-RTE-tier-graduation](#epi-rte-tier-graduation), [EPI-RTE-tier-withdrawal](#epi-rte-tier-withdrawal), [EPI-RTE-query-ranking](#epi-rte-query-ranking) | none supplied | Citation and identity can hold for false text | Narrow file-identity/citation qualification with consequential metadata | “held up” and “outcome + reality” exceed predicate |
| [EPI-CLM-hygiene-truth](#epi-clm-hygiene-truth) | see claim | SRC-1 `omni_memory/eviction.py`; doctrine/design | see claim | [EPI-RTE-eviction-check](#epi-rte-eviction-check), [EPI-RTE-quarantine-disposition](#epi-rte-quarantine-disposition) | none supplied | No action outcome reference or component comparison | Reversible heuristic retrieval withdrawal | Citation is not demonstrable truth; quarantine is not refutation |

## Bounded conclusion

Omni-Memory acquires caller and shared assertions with unknown original warrant, retains them with code anchors, and supplies selected projections to later agents. Batch filtering is a storage-worthiness gate; direct manual/dashboard and explicit trusted import follow different admission rules. Model extraction/build requests project claims, but neither those instructions nor a storage write establish an evidence-consuming acceptance decision for an ampliative proposition. Semantic transformation remains indeterminate without content-specific pairs; JSON acquisition and code-controlled selection can be identified independently. See [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission), [RT-RTE-shared-import](runtime.md#rt-rte-shared-import), [RT-RTE-build-artifacts](runtime.md#rt-rte-build-artifacts), [EPI-RTE-filter-admission](#epi-rte-filter-admission).

The strongest inspected deterministic check concerns source-file identity. Its target is not the truth of the memory sentence. Tier promotion consumes a nonempty matching blob map and a positive citation count for active stated rows; withdrawal consumes drift/loss. The implementation can therefore rank and protect content without demonstrating its truth. AI-session/AI-build/doc inputs are capped at inferred here; that is a real countercase to a claim that all captured content can immediately graduate by citation. Explicit/manual and trusted import routes are countercases to a universal earned-tier rule. See [EPI-RTE-integrity-check](#epi-rte-integrity-check), [EPI-RTE-tier-graduation](#epi-rte-tier-graduation), [EPI-RTE-tier-withdrawal](#epi-rte-tier-withdrawal), [RT-RTE-local-edits](runtime.md#rt-rte-local-edits).

Citations change uses and later ranking/retention even without semantic success. Reconciliation heuristics alter active membership and conflict flags; callers can resolve, merge, restore or reanchor without a truth test. Quarantine and purge are retention decisions, not falsification. These routes are operational adaptation of memory selection, not evidence of improved future capacity. See [EPI-RTE-query-ranking](#epi-rte-query-ranking), [EPI-RTE-merge-disposition](#epi-rte-merge-disposition), [EPI-RTE-quarantine-disposition](#epi-rte-quarantine-disposition).

No inspected route here establishes post-acceptance lifecycle integration of a newly warranted claim. That bounded finding is not a system-complete absence: map/diagnostic/browser internals and provider processing have the explicit coverage limits above. Context delivery and point-of-use warnings have advisory force through [RT-BAP-agent-context](runtime.md#rt-bap-agent-context); metadata/status decisions enforce local ranking and membership but not external agent obedience. No demonstrated benefit, learning, exercised self-improvement or method-directed theory criticism follows from these source-only findings. Static guidance persists while claims/counters change; independent learning, reflection, autonomy and theory-builder conclusions must not be collapsed into one verdict.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-candidates
Label: Extracted memory candidates

SRC-1 `omni_memory/session_memory.py`. Natural-language text plus symbolic kind/files/symbols/evidence fields in transient Python JSON-compatible arrays. Inputs are caller JSON, model output or heuristic-selected text; source warrant unknown. No supplied runtime operative-object counterpart: [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission) and [RT-RTE-build-artifacts](runtime.md#rt-rte-build-artifacts) describe routes, not this candidate object. Not all items are truth-apt: todos are prospective tasks. Project fact/flow/decision assertions are truth-apt over the project/revision they describe.

> array; each item: {{"kind": one of {_KINDS_LINE}, "text": one concise sentence,
> "files": [paths], "symbols": [names], "evidence": "stated"|"inferred"}}.
> --- `omni_memory/session_memory.py`

#### EPI-OBJ-memory
Label: Retained memory text

SRC-1 `omni_memory/store.py`, `omni_memory/session_memory.py`. Natural-language memory.text in SQLite, indexed by symbolic IDs/status/branch/anchors. Distinct from [RT-OBJ-inject-cache](runtime.md#rt-obj-inject-cache) (delivery digest/counter) and from metadata part below. Closest route containers: [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission), [RT-RTE-local-edits](runtime.md#rt-rte-local-edits), [RT-RTE-shared-import](runtime.md#rt-rte-shared-import); no object counterpart supplied. In-memory text can be replaced by caller updates; retained text reaches later retrieval/projections without mandatory truth acceptance.

> m = Memory(text=text.strip(), kind=kind if kind in KINDS else "fact",
>                branch=branch, files=files or [], symbols=symbols or [],
>                commit_range=commit, source=source, evidence=evidence,
>                blob_shas=shas, observed=observed, unbound=unbound,
>                author=gitmeta.git_user(root))
> --- `omni_memory/session_memory.py`

#### EPI-OBJ-evidence
Label: Evidence and source-integrity metadata

Part of: [EPI-OBJ-memory](#epi-obj-memory)

The retained memory record contains this symbolic operative part; the parent above denotes the retained memory text with its row, not merely an isolated string. SRC-1 `omni_memory/store.py`, `omni_memory/staleness.py`. SQLite evidence tier, blob map, observation flags, citation counts and staleness flags are consumed by fixed code rules separately from natural-language text. Witness and read-ledger tables support the source-check paths in [RT-RTE-use-check](runtime.md#rt-rte-use-check). No supplied object counterpart; not a duplicate of the injection cache.

> evidence: str = "stated"
> --- `omni_memory/store.py`

#### EPI-OBJ-artifacts
Label: Generated API map and linkup

SRC-1 `omni_memory/artifacts.py`; evidence/passage supplied by [RT-RTE-build-artifacts](runtime.md#rt-rte-build-artifacts). Natural-language Markdown documents with diagram/code notation, stored as .omni-memory/api-map.md and linkup.md. Human/dashboard readers interpret explanations; no formal proof checker established. Distinct from retained SQLite rows: generated files have independent length-based replacement and no inspected version rollback. No supplied object counterpart.

### Routes

#### EPI-RTE-candidate-filter
Label: Candidate noise check

Part of: [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission)

SRC-1 `omni_memory/cleanup.py`. remember_many → cleanup.filter_items → Boolean keep/drop; Python owns check, candidates remain transient.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Kept list and dropped count.
- Later read-back: inapplicable — transient check alone retains nothing
- Delegated visibility: inapplicable — no delegation in deterministic filter
- Selection predicate: All batch items; structural/length/chatter checks for all, concrete-anchor check additionally for doc/heuristic.
- Invalidation or expiry: inapplicable — check result exists for current call only
- Activation or effect: Controls which candidates pass to batch admission.
- Evidence limits: This is storage-worthiness, not evidence about truth.

> if t.endswith("?"):                       # questions aren't durable facts
>         return True
> --- `omni_memory/cleanup.py`

> if source not in _STRICT_SOURCES:
>         return False                          # trust AI/manual/session prose
> --- `omni_memory/cleanup.py`

#### EPI-RTE-filter-admission
Label: Filtered candidate disposition

Part of: [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission)

SRC-1 `omni_memory/session_memory.py`. Kept candidates → remember → add_memory; code owns batch admission and evidence ceiling.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Accepted/dropped counts or failure.
- Later read-back: Admitted rows reach later retrieval through [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)
- Delegated visibility: Optional model proposes upstream; filter and writer are local.
- Selection predicate: Filter pass then source-tier clamp; inferred for ai-build/ai-session/doc ceilings, stated for other non-human labels.
- Invalidation or expiry: Later edit/forget/maintenance can change or retire rows.
- Activation or effect: Permits storage; does not establish changed host behavior.
- Evidence limits: Direct remember/dashboard admission differs; no semantic oracle.

Decision roles and admission: code applies the predicates above; caller/model proposes upstream text, and caller can later edit/forget/restore where applicable. No authenticated human per-item veto is mandatory. Open-ended memory operation, not a bounded experiment/curriculum. No semantic answer oracle; hash equality is a reference only for file identity. Static extraction/usage guidance shapes proposals, not a learned method revision. What persists is memory text and metadata, not validated criticism or provider reasoning. Rejection/recovery limits are stated above.

> items, dropped = cleanup.filter_items(items, source=source)
>     n = 0
>     for it in items:
> --- `omni_memory/session_memory.py`

> ceiling = "inferred" if source in ("ai-build", "ai-session", "doc") else "stated"
>     return ev if _EVIDENCE_RANK[ev] <= _EVIDENCE_RANK[ceiling] else ceiling
> --- `omni_memory/store.py`

#### EPI-RTE-staleness-check
Label: Changed anchor check

SRC-1 `omni_memory/staleness.py`. Endpoints: commit/file/symbol anchors and code graph → changed-file/affected-symbol intersections → is_stale. Code owns evaluation. No supplied counterpart after comparison with [RT-RTE-use-check](runtime.md#rt-rte-use-check): this checks commit-relative source changes rather than retrieval pins.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Changed-anchor predicate and touched anchors, internally.
- Later read-back: inapplicable — the check itself is transient; separate flag update persists results
- Delegated visibility: inapplicable — deterministic local source check
- Selection predicate: Active memories with files and commit anchor; graph-resolved symbol IDs when available, file-level fallback otherwise.
- Invalidation or expiry: inapplicable — predicate recomputed against current source state
- Activation or effect: Supplies staleness flag decisions, not semantic disproof.
- Evidence limits: Full graph propagation and Git error behavior not audited here; code changes need not invalidate historical decisions.

> is_stale = bool(mem_ids & affected_cache[anchor])
>             touched = sorted(mem_ids & affected_cache[anchor])
> --- `omni_memory/staleness.py`

> hit = files & changed_files
>             is_stale = bool(hit)
>             touched = sorted(hit)
> --- `omni_memory/staleness.py`

#### EPI-RTE-staleness-flag
Label: Staleness flag update

SRC-1 `omni_memory/staleness.py`. Endpoints: changed-anchor verdict → SQLite stale metadata → later context/eviction. Code owns flag setting/clearing; no supplied counterpart after comparison with [RT-RTE-use-check](runtime.md#rt-rte-use-check), which emits retrieval-time warnings instead.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: checked/stale/cleared counters.
- Later read-back: Persisted stale flag and timestamp feed warnings and uncited stale-age eviction scoring.
- Delegated visibility: External host receives warnings only where the selected projection emits them.
- Selection predicate: is_stale sets flag; previously stale but now unaffected clears it.
- Invalidation or expiry: Next recompute can clear flags; explicit reanchor also clears them.
- Activation or effect: Warning authority and retention priority change; text itself stays unchanged.
- Evidence limits: No observed response to warnings; not semantic acceptance or rejection.

Decision roles: code evaluates and changes flags; caller launches check or refresh, not per-item approval. No answer oracle for sentence truth; open-ended maintenance. Caller may reanchor/edit/forget later; static guidance says reverify stale claims, but no completed revalidation is established.

> if is_stale:
>             store.set_stale(r["id"], True, None if was_stale else now, touched)
>             stale += 1
>         elif was_stale:
>             store.set_stale(r["id"], False, None, [])
>             cleared += 1
> --- `omni_memory/staleness.py`

#### EPI-RTE-integrity-check
Label: Source integrity check

SRC-1 `omni_memory/staleness.py`. Recorded blob map → current Git hashes → verdict; reconcile/graduate own checks. Compared with [RT-RTE-use-check](runtime.md#rt-rte-use-check): same class of hash comparison but capture-anchored integrity instead of retrieval-time witness; no duplicate route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counters/verdicts; doctor prints coverage.
- Later read-back: Stored flags/tiers can affect subsequent retrieval; verdict itself recomputed.
- Delegated visibility: inapplicable — local Git/SQLite check, no model delegation
- Selection predicate: Active rows with declared anchors; nonempty recorded map checked file by file.
- Invalidation or expiry: Recomputed on refresh/doctor; no-source legacy rows uncheckable or name-resolved.
- Activation or effect: Feeds separate promotion/demotion; no semantic inference.
- Evidence limits: Scope is only mapped files; completeness and fidelity of chosen anchors unproved.

> for path, sha in shas.items():
>         cur = current.get(path) if current is not None else gitmeta.blob_sha(root, path)
>         if not cur:
>             return "ORPHANED"                     # object missing at HEAD → deleted
>         if cur != sha:
>             worst = "DRIFTED"
>     return worst
> --- `omni_memory/staleness.py`

#### EPI-RTE-tier-graduation
Label: Verified-tier promotion

SRC-1 `omni_memory/staleness.py`. Active stated rows + positive uses + nonempty FRESH blob map → SQLite verified; full_refresh owns transition. No supplied counterpart: related to but distinct from [RT-RTE-use-check](runtime.md#rt-rte-use-check).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Promotion count.
- Later read-back: Tier consumed by query rank and eviction; no-query browse can bypass tier weighting.
- Delegated visibility: inapplicable — local transition, no delegation
- Selection predicate: status active, evidence stated, uses>0, shas nonempty, all compared hashes match.
- Invalidation or expiry: reconcile can demote on drift/loss; callers can edit tiers.
- Activation or effect: Grants rank/eviction authority to same text, not semantic acceptance.
- Evidence limits: Refresh signature can defer check; initial inferred AI/doc rows do not satisfy stated predicate.

Decision roles and admission: code applies the predicates above; caller/model proposes upstream text, and caller can later edit/forget/restore where applicable. No authenticated human per-item veto is mandatory. Open-ended memory operation, not a bounded experiment/curriculum. No semantic answer oracle; hash equality is a reference only for file identity. Static extraction/usage guidance shapes proposals, not a learned method revision. What persists is memory text and metadata, not validated criticism or provider reasoning. Rejection/recovery limits are stated above.

> "SELECT id, blob_shas, source FROM memory WHERE status='active' "
>         "AND evidence='stated' AND COALESCE(uses,0) > 0"
> --- `omni_memory/staleness.py`

> if _integrity_verdict(root, shas, current) == "FRESH":
>             store.db.execute("UPDATE memory SET evidence='verified' WHERE id=?", (r["id"],))
>             n += 1
> --- `omni_memory/staleness.py`

#### EPI-RTE-tier-withdrawal
Label: Verified-tier withdrawal

SRC-1 `omni_memory/staleness.py`. Reconcile verdict → _demote / stale flag → SQLite. Distinct from [RT-RTE-use-check](runtime.md#rt-rte-use-check) warnings: this mutates persisted qualification.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Reconcile counters.
- Later read-back: Changed tier/flag consumed by later ranking, maintenance and projections.
- Delegated visibility: inapplicable — no delegation
- Selection predicate: Verified rows with nonempty recorded blob map and drift/loss; orphan stale handling broader.
- Invalidation or expiry: Later matching stated+cited row may graduate again; caller can intervene.
- Activation or effect: Removes metadata authority without rewriting text.
- Evidence limits: Drift does not disprove a claim; AGENTS projection need not surface per-row flags.

Decision roles and admission: code applies the predicates above; caller/model proposes upstream text, and caller can later edit/forget/restore where applicable. No authenticated human per-item veto is mandatory. Open-ended memory operation, not a bounded experiment/curriculum. No semantic answer oracle; hash equality is a reference only for file identity. Static extraction/usage guidance shapes proposals, not a learned method revision. What persists is memory text and metadata, not validated criticism or provider reasoning. Rejection/recovery limits are stated above.

> elif verdict == "DRIFTED":
>                 drifted += 1                      # counted; recompute owns staleness
>                 _demote(store, r)
> --- `omni_memory/staleness.py`

> if row["evidence"] != "verified":
>         return
>     store.db.execute(
>         "UPDATE memory SET evidence='stated' WHERE id=? AND evidence='verified'",
>         (row["id"],))
> --- `omni_memory/staleness.py`

#### EPI-RTE-query-ranking
Label: Citation and tier ranking

Part of: [RT-RTE-context-delivery](runtime.md#rt-rte-context-delivery)

SRC-1 `omni_memory/rank.py`. Scoped rows → rank.score_one → sorted hits → Store.memories; Python owns relevance decision.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ranked matching list.
- Later read-back: Uses/evidence persist and influence later query invocations; ranking results need not persist.
- Delegated visibility: External host sees only downstream selected projection, not all rows.
- Selection predicate: Positive lexical/file/graph score; uses/log feedback and verified ×1.2 or inferred ×0.8; empty query handled separately.
- Invalidation or expiry: Recomputed each query as rows/config/state change.
- Activation or effect: Ranking changes which text can reach host; actual compliance unobserved.
- Evidence limits: Score is relevance/priority; no reference answer or correctness assessment.

Decision roles and admission: code applies the predicates above; caller/model proposes upstream text, and caller can later edit/forget/restore where applicable. No authenticated human per-item veto is mandatory. Open-ended memory operation, not a bounded experiment/curriculum. No semantic answer oracle; hash equality is a reference only for file identity. Static extraction/usage guidance shapes proposals, not a learned method revision. What persists is memory text and metadata, not validated criticism or provider reasoning. Rejection/recovery limits are stated above.

> score *= 1.0 + _USE_W * math.log(1 + (m.get("uses") or 0))  # citation feedback
> --- `omni_memory/rank.py`

> score *= {"verified": 1.2, "inferred": 0.8}.get(m.get("evidence"), 1.0)
> --- `omni_memory/rank.py`

#### EPI-RTE-merge-reconcile
Label: Duplicate and conflict check

SRC-1 `omni_memory/store.py`. New/merged row and peers → text overlap/symbol-kind check → duplicate/conflict result. Distinct from supplied [RT-RTE-local-edits](runtime.md#rt-rte-local-edits) caller route and [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission) ingestion route; this shared check serves both and branch movement.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Similarity/conflict classification internal to callers.
- Later read-back: inapplicable — check itself does not retain outcome; disposition does
- Delegated visibility: inapplicable — code comparison, no delegated model
- Selection predicate: Same branch/kind active peers for new-row dedup; incoming branch rows against base on merge.
- Invalidation or expiry: inapplicable — predicates evaluated against current peer texts
- Activation or effect: Supplies membership mutation and conflict-recording decisions.
- Evidence limits: No logical equivalence or contradiction checker; heuristics admit false positives.

Decision roles and admission: code applies the predicates above; caller/model proposes upstream text, and caller can later edit/forget/restore where applicable. No authenticated human per-item veto is mandatory. Open-ended memory operation, not a bounded experiment/curriculum. No semantic answer oracle; hash equality is a reference only for file identity. Static extraction/usage guidance shapes proposals, not a learned method revision. What persists is memory text and metadata, not validated criticism or provider reasoning. Rejection/recovery limits are stated above.

> jacc = len(ta & tb) / len(ta | tb)
>     return jacc >= thresh
> --- `omni_memory/store.py`

> if shared_sym and m["kind"] in _CONFLICT_KINDS:
>                 anchor = ", ".join(sorted(m_syms & r_syms))
>                 self.record_conflict(m["id"], r["id"], anchor)
>                 return "conflict"
> --- `omni_memory/store.py`

#### EPI-RTE-merge-disposition
Label: Supersession and conflict disposition

SRC-1 `omni_memory/store.py`. Similarity/collision result or caller decision → superseded rows/conflicts/merged files; store owns mutations. Overlaps supplied [RT-RTE-local-edits](runtime.md#rt-rte-local-edits) and [RT-RTE-capture-admission](runtime.md#rt-rte-capture-admission) but distinct shared submechanism, not wholly part of one.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Mutation counts or status; resolve reports result.
- Later read-back: Statuses constrain active reads, conflicts mark ranked injection; history follows supersedes chain.
- Delegated visibility: inapplicable — no model call; local caller may itself be an agent
- Selection predicate: Duplicate thresholds; tier/uses guards on relaxed insertion; merge reconciliation prefers citation/tier strength; caller keep/both.
- Invalidation or expiry: Caller can later edit or retain both; no automatic semantic rollback established.
- Activation or effect: Enforces membership; conflict flag advisory. Dashboard merge unions files then forgets drops without synthesizing text.
- Evidence limits: Protected insertion peers exempt, not a universal proof of protection across every route.

Decision roles and admission: code applies the predicates above; caller/model proposes upstream text, and caller can later edit/forget/restore where applicable. No authenticated human per-item veto is mandatory. Open-ended memory operation, not a bounded experiment/curriculum. No semantic answer oracle; hash equality is a reference only for file identity. Static extraction/usage guidance shapes proposals, not a learned method revision. What persists is memory text and metadata, not validated criticism or provider reasoning. Rejection/recovery limits are stated above.

> if relaxed and not strict:
>                 if r["uses"] > 0 or _EVIDENCE_RANK.get(r["evidence"], 1) > m_rank:
>                     continue
>             self.db.execute("UPDATE memory SET status='superseded',updated=? WHERE id=?",
>                             (time.time(), r["id"]))
>             m.supersedes_id = r["id"]
> --- `omni_memory/store.py`

> self.update_memory(keep_id, files=files)
>         n = 0
>         for did in drop_ids:
>             if did != keep_id and self.forget(did):
>                 n += 1
>         return n
> --- `omni_memory/store.py`

#### EPI-RTE-eviction-check
Label: Hygiene score and noise check

SRC-1 `omni_memory/eviction.py`. Active row metadata / branch state → evict_score and retro-noise → sweep lists; code owns evaluation. Distinct from [RT-RTE-local-edits](runtime.md#rt-rte-local-edits) umbrella maintenance callers.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Candidate/noise/purgeable lists.
- Later read-back: inapplicable — score computation itself retains nothing
- Delegated visibility: inapplicable — no delegation
- Selection predicate: Threshold meta default 0.5; protected returns 0; source/tier/uses/kind/staleness/branch factors; noise requires uncited nonprotected nonexempt.
- Invalidation or expiry: inapplicable — ephemeral recomputation on maintenance
- Activation or effect: Supplies quarantine/deletion decisions; dry run does not apply them.
- Evidence limits: Uses is not outcome success; confidence is stored input, not measured truth probability.

Decision roles and admission: code applies the predicates above; caller/model proposes upstream text, and caller can later edit/forget/restore where applicable. No authenticated human per-item veto is mandatory. Open-ended memory operation, not a bounded experiment/curriculum. No semantic answer oracle; hash equality is a reference only for file identity. Static extraction/usage guidance shapes proposals, not a learned method revision. What persists is memory text and metadata, not validated criticism or provider reasoning. Rejection/recovery limits are stated above.

> if evidence == "inferred":
>         score += 0.15
>     elif evidence == "verified":
>         score -= 0.30
> --- `omni_memory/eviction.py`

> if uses > 0:  # citation shield — proven-useful memory resists eviction
>         score -= min(0.5, 0.15 * math.log(1 + uses))
> --- `omni_memory/eviction.py`

#### EPI-RTE-quarantine-disposition
Label: Quarantine purge and restoration

SRC-1 `omni_memory/eviction.py`. sweep/caller → quarantine/forget/restore/delete → SQLite status or deletion; code/caller own changes. Distinct from broad [RT-RTE-local-edits](runtime.md#rt-rte-local-edits) route; material maintenance subroute with separate evaluator.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts/IDs; restore can return failure.
- Later read-back: Abandoned excluded by default active selector; restored rows reappear; deleted rows unavailable.
- Delegated visibility: inapplicable — no delegation
- Selection predicate: Non-dry-run candidates/noise; purge explicit and grace-aged uncited quarantine; caller chooses restoration.
- Invalidation or expiry: Restore marks noise_exempt; purge irreversible at this API.
- Activation or effect: Changes future retrieval membership.
- Evidence limits: No outcome-based semantic acceptance/rejection; ordinary false text may survive.

Decision roles and admission: code applies the predicates above; caller/model proposes upstream text, and caller can later edit/forget/restore where applicable. No authenticated human per-item veto is mandatory. Open-ended memory operation, not a bounded experiment/curriculum. No semantic answer oracle; hash equality is a reference only for file identity. Static extraction/usage guidance shapes proposals, not a learned method revision. What persists is memory text and metadata, not validated criticism or provider reasoning. Rejection/recovery limits are stated above.

> if not dry_run:
>         for c in candidates:
>             store.quarantine(c["id"], f"{c['reason']} (score {c['score']})")
>         for c in noise:
>             store.quarantine(c["id"], "extraction noise (conversational/thread)")
> --- `omni_memory/eviction.py`

> "UPDATE memory SET status='active', quarantined_at=NULL, "
>             "quarantine_reason=NULL, noise_exempt=1 WHERE id=? AND status='abandoned'",
> --- `omni_memory/store.py`

### Claims

#### EPI-CLM-earned-verified
Label: Earned verified tier

SRC-1 `omni_memory/staleness.py`. Doctrine/design in graduation comments claims citation plus re-fetchable unchanged anchors warrants verified and means a cited memory held up. Closest supplied [RT-CLM-verified-context](runtime.md#rt-clm-verified-context) concerns enforced usage; this is the distinct warrant attributed to tier qualification. Implementation supports predicates and their consequences, not outcome success.

> blob sha still matches HEAD) AND the agent has cited it (uses>0). Content can
>     never self-declare `verified`; it must be earned by outcome + reality.
> --- `omni_memory/staleness.py`

> locally. And `uses > 0` means you cited it and it held up. Excluding shared memory
> --- `omni_memory/staleness.py`


#### EPI-CLM-hygiene-truth
Label: Citation shield as truth

SRC-1 `omni_memory/eviction.py`. Doctrine/design interprets continued citation as demonstrated truth and calls quarantine false/dead-memory hygiene. Distinct from [RT-CLM-verified-context](runtime.md#rt-clm-verified-context) (use instructions) and [EPI-CLM-earned-verified](#epi-clm-earned-verified) (tier promotion): this claim licenses retention protection. The score consumes citations, not tests of the cited assertion.

> The citation shield means a memory the agent keeps using never gets evicted,
> even on a dead branch — because it's demonstrably still true.
> --- `omni_memory/eviction.py`


### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
