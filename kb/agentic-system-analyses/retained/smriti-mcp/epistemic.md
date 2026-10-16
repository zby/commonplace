---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Smriti MCP epistemic routes: caller-authored claims, unchecked provenance, retrieval authority and deterministic maintenance."
run-id: AAS-2026-10-14-smriti-mcp-14f6928f9817-01
reviewed-boundary: "8264bf9103477d9521e57b27c81dcc2e943a3230"
---

# Smriti MCP epistemic report

## Source-and-claim boundary

Question: how do retained facts, observations and consolidated notes gain warrant or consequential use? Scope and exclusions: see [boundary](boundary.md#boundary-and-evidence); evidence identities: see its [Source register](boundary.md#source-register). This is the shipped artifact, not its enclosing model/host. SRC-1 supplies implementation and doctrine/design, not an observed execution or causal comparison. No production memory or supplied model trace individuates an actual accepted proposition. Truth and authorship of generic supplied prose are not determinable; storage of such prose is inspectable.

Direct source reads checked the complete CLI, server, store, frontmatter parser and repair utility against the provisional runtime routes. No extra hook or tool dispatch appears in those files: registered wrappers delegate to the inspected store. Tests and broader documentation coverage remain supplied boundary/runtime findings, not independently executed evidence. Missing host processing prevents judging actual prompt use or model reliability; missing acceptance records prevents attributing evidenced acceptance to a particular note; missing comparative runs prevents retrieval-quality and learning-benefit claims. Dependency internals and external model parameters remain outside the boundary. No owned distributed-parametric component is established by these routes; see [RT-CMP-memory-store](runtime.md#rt-cmp-memory-store).

| Entry point or operation | Source path (SRC-1) | Coverage and records |
|---|---|---|
| CLI server/default/options, fix-frontmatter, rebuild; repair module main | `src/smriti_mcp/cli.py`, `src/smriti_mcp/fix_frontmatter.py` | Direct full reads; [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance), [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite) |
| All registered tools and input models | `src/smriti_mcp/server.py` | Direct full read; [RT-BAP-tool-guidance](runtime.md#rt-bap-tool-guidance), [EPI-RTE-shape-check](#epi-rte-shape-check) |
| create/append/update/remember, archive/delete/supersede | `src/smriti_mcp/store.py` | Direct full read; [RT-RTE-memory-write](runtime.md#rt-rte-memory-write), [EPI-RTE-write-admission](#epi-rte-write-admission), [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition) |
| get/list/search/recall, mark_accessed, index build/load | `src/smriti_mcp/store.py`, `src/smriti_mcp/frontmatter.py` | Direct full reads; [EPI-RTE-content-retention](#epi-rte-content-retention), [EPI-RTE-recall-selection](#epi-rte-recall-selection), [EPI-RTE-access-reinforcement](#epi-rte-access-reinforcement) |
| record/load traces, suggest/consolidate | `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py` | Direct reads; [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation), [EPI-RTE-trace-review](#epi-rte-trace-review) |
| health, frontmatter repair, link normalization/insertion, rebuild | `src/smriti_mcp/store.py`, `src/smriti_mcp/fix_frontmatter.py` | Direct reads; [EPI-RTE-maintenance-check](#epi-rte-maintenance-check), [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite) |
| Library examples and shipped tests | `README.md`, `tests/` | Supplied boundary/runtime coverage; README precise-metadata passage directly read. No test execution or production evaluator evidence. |

Consequential claims: [EPI-CLM-consolidation-provenance](#epi-clm-consolidation-provenance), [EPI-CLM-summary-omission](#epi-clm-summary-omission), [EPI-CLM-recall-bundle](#epi-clm-recall-bundle). They concern preservation, provenance and selection, not an explicit guarantee of factual truth. File-safety claims remain [RT-CLM-file-controls](runtime.md#rt-clm-file-controls); they are not semantic warrant.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-memory-body](#epi-obj-memory-body) | Supplied facts, decisions and observations; actual propositions not supplied | see record | SRC-1, `src/smriti_mcp/store.py` | Actual truth, source warrant and generic authorship unknown |
| [EPI-OBJ-memory-meta](#epi-obj-memory-meta) | Descriptions and asserted source/confidence/verification labels; counters and routing fields also present | see record | SRC-1, `src/smriti_mcp/store.py` | Separate symbolic ranking consumption from prose interpretation |
| [EPI-OBJ-trace-event](#epi-obj-trace-event) | Raw supplied observations; generated operation reports | see record | SRC-1, `src/smriti_mcp/store.py` | A trace label or ID is not authentication or evidence of factual support |
| [RT-OBJ-server-instructions](runtime.md#rt-obj-server-instructions) | None required: prescriptive storage guidance | see record | SRC-1, `src/smriti_mcp/server.py` | Host interpretation unobserved |

## Authority-route ledger

The linked records own their targets, evaluators, timing, results, force, scope, channels and read-back fields. All rows below are implementation assessments, not evidence of activation. Checking and admission are split; retention is not treated as lifecycle integration after acceptance.

Route ID: [EPI-RTE-shape-check](#epi-rte-shape-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-body](#epi-obj-memory-body)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-shape-check](#epi-rte-shape-check).
Evaluator/condition and domain: see [EPI-RTE-shape-check](#epi-rte-shape-check).
Activation and timing: see [EPI-RTE-shape-check](#epi-rte-shape-check).
Possible or observed result: see [EPI-RTE-shape-check](#epi-rte-shape-check).
Implemented force: see [EPI-RTE-shape-check](#epi-rte-shape-check).
Epistemic authority and scope: see [EPI-RTE-shape-check](#epi-rte-shape-check).
Operational authority: see [EPI-RTE-shape-check](#epi-rte-shape-check).
Behavioral-authority path: see [EPI-RTE-shape-check](#epi-rte-shape-check).
Evidence source ID and local anchor: SRC-1, `src/smriti_mcp/store.py`.
Claim IDs: none
Mismatch marker: none.
Gap/limit: Input shape/path checks; not proposition truth; exercised operation unobserved.

Route ID: [EPI-RTE-write-admission](#epi-rte-write-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-body](#epi-obj-memory-body)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: see [EPI-RTE-write-admission](#epi-rte-write-admission).
Evaluator/condition and domain: see [EPI-RTE-write-admission](#epi-rte-write-admission).
Activation and timing: see [EPI-RTE-write-admission](#epi-rte-write-admission).
Possible or observed result: see [EPI-RTE-write-admission](#epi-rte-write-admission).
Implemented force: see [EPI-RTE-write-admission](#epi-rte-write-admission).
Epistemic authority and scope: see [EPI-RTE-write-admission](#epi-rte-write-admission).
Operational authority: see [EPI-RTE-write-admission](#epi-rte-write-admission).
Behavioral-authority path: see [EPI-RTE-write-admission](#epi-rte-write-admission).
Evidence source ID and local anchor: SRC-1, `src/smriti_mcp/store.py`.
Claim IDs: none
Mismatch marker: none.
Gap/limit: Operational admission, not evidence-consuming acceptance; exercised operation unobserved.

Route ID: [EPI-RTE-content-retention](#epi-rte-content-retention)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-body](#epi-obj-memory-body)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: see [EPI-RTE-content-retention](#epi-rte-content-retention).
Evaluator/condition and domain: see [EPI-RTE-content-retention](#epi-rte-content-retention).
Activation and timing: see [EPI-RTE-content-retention](#epi-rte-content-retention).
Possible or observed result: see [EPI-RTE-content-retention](#epi-rte-content-retention).
Implemented force: see [EPI-RTE-content-retention](#epi-rte-content-retention).
Epistemic authority and scope: see [EPI-RTE-content-retention](#epi-rte-content-retention).
Operational authority: see [EPI-RTE-content-retention](#epi-rte-content-retention).
Behavioral-authority path: see [EPI-RTE-content-retention](#epi-rte-content-retention).
Evidence source ID and local anchor: SRC-1, `src/smriti_mcp/store.py`.
Claim IDs: [EPI-CLM-consolidation-provenance](#epi-clm-consolidation-provenance)
Mismatch marker: none.
Gap/limit: Unknown source warrant; retained supplied text; exercised operation unobserved.

Route ID: [EPI-RTE-recall-selection](#epi-rte-recall-selection)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-meta](#epi-obj-memory-meta)
Content/update relation: no content change
Transition or check target: see [EPI-RTE-recall-selection](#epi-rte-recall-selection).
Evaluator/condition and domain: see [EPI-RTE-recall-selection](#epi-rte-recall-selection).
Activation and timing: see [EPI-RTE-recall-selection](#epi-rte-recall-selection).
Possible or observed result: see [EPI-RTE-recall-selection](#epi-rte-recall-selection).
Implemented force: see [EPI-RTE-recall-selection](#epi-rte-recall-selection).
Epistemic authority and scope: see [EPI-RTE-recall-selection](#epi-rte-recall-selection).
Operational authority: see [EPI-RTE-recall-selection](#epi-rte-recall-selection).
Behavioral-authority path: see [EPI-RTE-recall-selection](#epi-rte-recall-selection).
Evidence source ID and local anchor: SRC-1, `src/smriti_mcp/store.py`.
Claim IDs: [EPI-CLM-recall-bundle](#epi-clm-recall-bundle)
Mismatch marker: none.
Gap/limit: Ranks and delivers; confidence is supplied, not checked; exercised operation unobserved.

Route ID: [EPI-RTE-access-reinforcement](#epi-rte-access-reinforcement)
Route function: behavior/policy adaptation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-meta](#epi-obj-memory-meta)
Content/update relation: non-truth-apt policy/content update: access-based salience and counters
Transition or check target: see [EPI-RTE-access-reinforcement](#epi-rte-access-reinforcement).
Evaluator/condition and domain: see [EPI-RTE-access-reinforcement](#epi-rte-access-reinforcement).
Activation and timing: see [EPI-RTE-access-reinforcement](#epi-rte-access-reinforcement).
Possible or observed result: see [EPI-RTE-access-reinforcement](#epi-rte-access-reinforcement).
Implemented force: see [EPI-RTE-access-reinforcement](#epi-rte-access-reinforcement).
Epistemic authority and scope: see [EPI-RTE-access-reinforcement](#epi-rte-access-reinforcement).
Operational authority: see [EPI-RTE-access-reinforcement](#epi-rte-access-reinforcement).
Behavioral-authority path: see [EPI-RTE-access-reinforcement](#epi-rte-access-reinforcement).
Evidence source ID and local anchor: SRC-1, `src/smriti_mcp/store.py`.
Claim IDs: none
Mismatch marker: none.
Gap/limit: Repeated selection can strengthen later ranking without correctness evidence; exercised operation unobserved.

Route ID: [EPI-RTE-trace-review](#epi-rte-trace-review)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-trace-event](#epi-obj-trace-event)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: see [EPI-RTE-trace-review](#epi-rte-trace-review).
Evaluator/condition and domain: see [EPI-RTE-trace-review](#epi-rte-trace-review).
Activation and timing: see [EPI-RTE-trace-review](#epi-rte-trace-review).
Possible or observed result: see [EPI-RTE-trace-review](#epi-rte-trace-review).
Implemented force: see [EPI-RTE-trace-review](#epi-rte-trace-review).
Epistemic authority and scope: see [EPI-RTE-trace-review](#epi-rte-trace-review).
Operational authority: see [EPI-RTE-trace-review](#epi-rte-trace-review).
Behavioral-authority path: see [EPI-RTE-trace-review](#epi-rte-trace-review).
Evidence source ID and local anchor: SRC-1, `src/smriti_mcp/store.py`.
Claim IDs: none
Mismatch marker: none.
Gap/limit: Grouping raw events; advisory recommendations; exercised operation unobserved.

Route ID: [EPI-RTE-maintenance-check](#epi-rte-maintenance-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-meta](#epi-obj-memory-meta)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: see [EPI-RTE-maintenance-check](#epi-rte-maintenance-check).
Evaluator/condition and domain: see [EPI-RTE-maintenance-check](#epi-rte-maintenance-check).
Activation and timing: see [EPI-RTE-maintenance-check](#epi-rte-maintenance-check).
Possible or observed result: see [EPI-RTE-maintenance-check](#epi-rte-maintenance-check).
Implemented force: see [EPI-RTE-maintenance-check](#epi-rte-maintenance-check).
Epistemic authority and scope: see [EPI-RTE-maintenance-check](#epi-rte-maintenance-check).
Operational authority: see [EPI-RTE-maintenance-check](#epi-rte-maintenance-check).
Behavioral-authority path: see [EPI-RTE-maintenance-check](#epi-rte-maintenance-check).
Evidence source ID and local anchor: SRC-1, `src/smriti_mcp/store.py`.
Claim IDs: none
Mismatch marker: none.
Gap/limit: Code-relative health diagnostics, not note-truth tests; exercised operation unobserved.

Route ID: [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-meta](#epi-obj-memory-meta)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: see [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite).
Evaluator/condition and domain: see [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite).
Activation and timing: see [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite).
Possible or observed result: see [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite).
Implemented force: see [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite).
Epistemic authority and scope: see [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite).
Operational authority: see [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite).
Behavioral-authority path: see [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite).
Evidence source ID and local anchor: SRC-1, `src/smriti_mcp/store.py`.
Claim IDs: [EPI-CLM-summary-omission](#epi-clm-summary-omission)
Mismatch marker: summary-omission contradiction.
Gap/limit: Truncation and inferred metadata can change meaning; linking also changes retrieval graph; exercised operation unobserved.

Route ID: [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-memory-meta](#epi-obj-memory-meta)
Content/update relation: non-truth-apt policy/content update: lifecycle status and supersession relations
Transition or check target: see [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition).
Evaluator/condition and domain: see [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition).
Activation and timing: see [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition).
Possible or observed result: see [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition).
Implemented force: see [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition).
Epistemic authority and scope: see [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition).
Operational authority: see [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition).
Behavioral-authority path: see [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition).
Evidence source ID and local anchor: SRC-1, `src/smriti_mcp/store.py`.
Claim IDs: none
Mismatch marker: none.
Gap/limit: Caller-directed withdrawal from default recall, not truth adjudication; exercised operation unobserved.

Lifecycle integration after evidence-consuming acceptance: no route found within boundary. This is a scoped result over the directly read CLI/server/store/repair paths, not a denial that an external caller could verify a claim before submitting it. Source strings can connect notes to alleged evidence without an implemented evidence-support check.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-consolidation-provenance](#epi-clm-consolidation-provenance) | see record | SRC-1, `src/smriti_mcp/server.py`; doctrine/design | Agent supplies reviewed prose | [EPI-RTE-content-retention](#epi-rte-content-retention), [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation) | None supplied | No comparison; identifiers not checked against support | Provenance labels are recorded on create/update, not factual validation | Append omits newly prepared metadata; review is requested, not enforced |
| [EPI-CLM-summary-omission](#epi-clm-summary-omission) | see record | SRC-1, `README.md`, `src/smriti_mcp/server.py`; doctrine/design | Explicit no-derived-description wording | [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite), [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) | None supplied | Source-level counterpath only | Auto/create reaches create_memory's body-prefix fallback | Contradicted for missing descriptions on creation; not a supplied runtime defect |
| [EPI-CLM-recall-bundle](#epi-clm-recall-bundle) | see record | SRC-1, `src/smriti_mcp/server.py`; doctrine/design | Lexical/metadata/link selection | [EPI-RTE-recall-selection](#epi-rte-recall-selection), [EPI-RTE-access-reinforcement](#epi-rte-access-reinforcement) | None supplied | No relevance or task-outcome evaluation | Deterministic requested selection given files/time; not a truth oracle | Approximate budget and changed access state prevent strict size or invariant-output inference |

## Bounded conclusion

Smriti acquires caller-authored content and stores it for later requested use; the system does not establish that source warrant exists. Provenance/confidence/verification fields are asserted metadata, not evidence-consuming acceptance decisions. Retention, recommendation, status changes and later retrieval therefore do not license the truth of imported claims. See [EPI-RTE-write-admission](#epi-rte-write-admission) and [EPI-RTE-content-retention](#epi-rte-content-retention).

Selection grants operational, not epistemic, priority: lexical matches, supplied confidence, backlinks, lifecycle and expiry affect delivery; accesses can reinforce future rank. A recalled bundle exposes short descriptions and at most two body snippets, plus status/confidence/source-agent, but not the complete sources or last_verified_at evidence chain. Full get remains reachable. The external host decides whether to interpret the output as advice or instruction; actual behavioral compliance is unobserved. See [EPI-RTE-recall-selection](#epi-rte-recall-selection) and [EPI-RTE-access-reinforcement](#epi-rte-access-reinforcement).

Health diagnostics derive limited file/graph properties under fixed thresholds; they do not criticize a memory's factual explanation. Repair defaults, truncated descriptions and wikilink insertion can influence later retrieval without evaluating semantic correctness. A concrete counterexample below shows why “summary” cannot imply semantic preservation. Supersession changes default reliance selection but permits explicit historical retrieval; it is not evidence of refutation. See [EPI-RTE-maintenance-check](#epi-rte-maintenance-check), [EPI-RTE-maintenance-rewrite](#epi-rte-maintenance-rewrite) and [EPI-RTE-lifecycle-disposition](#epi-rte-lifecycle-disposition).

Trace grouping preserves candidate observations for external review. No produced accepted ampliative claim, internally checked theory, or acceptance-linked lifecycle integration is established in these inspected routes. Generic imported prose may contain theories, but no supplied content/run supports assessing their consumption, content-directed criticism or iterative revision. Access-based adaptation is independently implemented; improved capacity, autonomous semantic review, reflection and self-improvement do not follow from it. No causal benefit is established without later-consumer or comparison evidence. These are independent limits, not a single system-wide epistemic verdict.

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-memory-body
Label: MemoryDocument body

Source-native identity: `MemoryDocument.body`, supplied content retained in note Markdown; natural-language content on local filesystem, interpreted by an external human/model after retrieval. Symbolic string operations store and excerpt it without semantic adjudication. SRC-1, `src/smriti_mcp/frontmatter.py`, `src/smriti_mcp/store.py`. No counterpart among supplied runtime objects: this is not the static server guidance. Closest route is [RT-RTE-memory-write](runtime.md#rt-rte-memory-write).

> body: str = ""
> --- `src/smriti_mcp/frontmatter.py`

> if content is not None:
>     doc.body = content
> --- `src/smriti_mcp/store.py`

#### EPI-OBJ-memory-meta
Label: MemoryDocument metadata

Source-native identity: `MemoryDocument.meta`, YAML in local Markdown and derived dictionaries/indexes. Mixed parts: natural-language description/source assertions for external interpretation; symbolic status, confidence labels, numeric salience/access fields, scope and associations consumed by fixed Python rules. No distributed-parametric representation. Split from body because update, ranking and read-back differ. No counterpart in supplied operative objects; overlaps the state traversed by [RT-RTE-context-recall](runtime.md#rt-rte-context-recall), not a duplicate of that route. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`.

> confidence = str(note.get("confidence") or "").lower()
> score += {"high": 1.0, "medium": 0.5, "low": -0.5}.get(confidence, 0.0)
> --- `src/smriti_mcp/store.py`

#### EPI-OBJ-trace-event
Label: Trace event

Source-native identity: `event` in record_trace; natural-language `content` and symbolic event metadata persisted as NDJSON. Raw observations and generated operation reports have different origins: generic caller for record_trace/remember, code-produced consolidation report for consolidate_memory. Hash IDs identify events, not authenticated factual warrant. No counterpart in supplied objects; closest container route is [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation). SRC-1, `src/smriti_mcp/store.py`.

> handle.write(json.dumps(event, ensure_ascii=False, sort_keys=True) + "\n")
> --- `src/smriti_mcp/store.py`

### Routes

#### EPI-RTE-shape-check
Label: Write shape checking

Part of: [RT-RTE-memory-write](runtime.md#rt-rte-memory-write)

The checking part, not the parent's admission/I/O: MCP Pydantic schemas → store metadata cleaners and ID resolver → usable input or exception. Caller proposes; Python decides shape/path admissibility, not truth. No answer oracle, experiment or per-content human approval. Direct library calls bypass MCP models but retain store checks. SRC-1, `src/smriti_mcp/server.py`, `src/smriti_mcp/store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cleaned metadata or exception to calling write operation.
- Later read-back: inapplicable — this check does not itself persist content.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: Nonempty title/category, supported field shapes, valid root-contained note ID and branch-specific target existence.
- Invalidation or expiry: inapplicable — request-local evaluation.
- Activation or effect: Enforcing on relevant API writes; no license that a fact or source reference is true.
- Evidence limits: Dependency internals uninspected; arbitrary direct file editors bypass API checks; trace paths use different rules.

> if not title:
>     raise ValueError("Memory metadata requires title.")
> if not category:
>     raise ValueError("Memory metadata requires category.")
> --- `src/smriti_mcp/store.py`

#### EPI-RTE-write-admission
Label: Memory write admission

Part of: [RT-RTE-memory-write](runtime.md#rt-rte-memory-write)

Operational disposition after shape checking: request and candidate metadata → caller-explicit operation or auto branch → selected note write. Caller supplies proposed content; Python decides auto create/append; caller can withhold or explicitly choose update/append/create. Human versus model authorship unknown. Open requested mode; no expected-answer oracle or truth criterion. Guidance is shipped storage guidance. Rollback is caller restoration, not composite transaction. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`. The parent's exact-title/score passage supplies the automatic predicate.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Selected action, ID and reason/candidate metadata for remember; errors can reject operation.
- Later read-back: Admitted content feeds the separate retention route and later get/search/recall.
- Delegated visibility: inapplicable — no launched worker.
- Selection predicate: Explicit modes/IDs or auto equal normalized title and score at least 6; conflicting creation can fail.
- Invalidation or expiry: Caller replacement, append, archive, supersession or deletion; no factual revalidation gate.
- Activation or effect: Permissive operational admission of supplied prose into durable files, not acceptance against evidence for an intended truth use.
- Evidence limits: Search similarity cannot detect all semantic contradictions or duplicates. Explicit modes bypass auto disposition; no actual accepted claim supplied.

> elif best and self._remember_should_append(best, clean_meta):
>     action = "append"
>     reason = "Existing memory had a strong title or metadata match."
> --- `src/smriti_mcp/store.py`

#### EPI-RTE-content-retention
Label: Supplied content retention

Distinct cross-route function spanning [RT-RTE-memory-write](runtime.md#rt-rte-memory-write) and [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation), not wholly part of either: supplied note/trace → serialization/filesystem → future reload. Python owns I/O, caller owns prose and declared support. Acquires content with unknown source warrant; whitespace/serialization is not semantic verification. Consolidate create/update attach trace-reference strings without loading those traces; append does not attach the prepared metadata. Trace IDs replace the supplied sources list when present. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/frontmatter.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: ID/path or update status; trace returns event/ID/path.
- Later read-back: Note get, scans/search/recall; traces through load/group suggestions. Saved indexes have a separate refresh horizon.
- Delegated visibility: inapplicable — local files shared only through external filesystem access or calls.
- Selection predicate: Supplied content and target, subject to write admission; trace IDs need not be verified supporting events.
- Invalidation or expiry: Note mutations/deletion; trace history is not automatically consumed or removed by consolidation; expiry only affects ranking.
- Activation or effect: Retention permits subsequent requested delivery; no epistemic acceptance or demonstrated later use.
- Evidence limits: No source-authenticated corpus or run; note plus event writes are not atomic. External source warrant unknown, not established preserved by keeping an identifier.

> if trace_ids:
>     clean_meta["sources"] = [f"trace:{trace_id}" for trace_id in trace_ids]
> --- `src/smriti_mcp/store.py`

Append's counterpath is quoted in [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation).

#### EPI-RTE-recall-selection
Label: Recall priority and delivery

Part of: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

Requested selection/delivery part: caller query/filters → lexical/metadata graph rules → ranked response. The caller proposes task and can veto consumption; Python selects without answer oracle, human adjudication or correctness outcome. Implemented force is ranking and filtering at tool response, not enforcement of external belief. Candidate facts may receive operational priority without epistemic endorsement. SRC-1, `src/smriti_mcp/store.py`. The parent supplies lexical/expiry/budget evidence; [EPI-OBJ-memory-meta](#epi-obj-memory-meta) supplies confidence consumption evidence.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Search optionally returns full Markdown; recall returns title/ID, description, status/confidence/source-agent and at most two body snippets; list/index browsing differs; get returns full serialized note.
- Later read-back: Selection reloads current files; optional access writes feed future ranking through the separate reinforcement route. Cached index text can outlive note edits until refresh.
- Delegated visibility: inapplicable — return to requester only.
- Selection predicate: Exact filters then weighted lexical/body/description matches, affinity and optional one-hop links; top limit and approximate budget. Recall excludes archived/superseded by default, not under all explicit filters.
- Invalidation or expiry: File changes affect scans; expiry subtracts score, not a general read ban.
- Activation or effect: Ranking force at the response consumer this call; advisory content for external host across later calls, whose actual interpretation is unobserved. No epistemic license beyond reported stored content.
- Evidence limits: Snippets can omit qualifications elsewhere; sources, observed_at and last_verified_at are not rendered by _recall_summary. Full note retrieval remains available; delivery is not compliance.

> for snippet in snippets[:2]:
>     lines.append(f"  {snippet}")
> return "\n".join(lines)
> --- `src/smriti_mcp/store.py`

#### EPI-RTE-access-reinforcement
Label: Access reinforcement

Part of: [RT-RTE-context-recall](runtime.md#rt-rte-context-recall)

Recall with mark_accessed or direct mark_accessed → metadata update → later affinity ranking. This is behavior-shaping retention of use counts, not content validation. Caller requests or accepts the default; code decides increment. No answer oracle or evaluation of future usefulness. Owner and consumer are MemoryStore; natural-language host reliance is a separate path. SRC-1, `src/smriti_mcp/store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Access count/status for direct call; recall incorporates access side effects before returning bundle.
- Later read-back: Future scans read salience/access_count; affinity uses salience times 2 and capped count contribution.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: Explicit ID or each actually included recall item when mark_accessed is enabled.
- Invalidation or expiry: Later accesses increment again; caller can patch metadata/delete note; capped salience is not confidence calibration.
- Activation or effect: Ranking force on later search/recall, persisted across sessions sharing files. No truth-apt content change or established capacity improvement.
- Evidence limits: No objective-linked feedback or later retrieval evaluation; popularity reinforcement can coexist with false claims.

> doc.meta["salience"] = min(1.0, (salience if salience is not None else 0.5) + 0.02)
> --- `src/smriti_mcp/store.py`

#### EPI-RTE-trace-review
Label: Trace review suggestions

Part of: [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation)

Load traces → normalize/group → search related notes → recommend review/update/create to caller. Python decides grouping; caller decides final prose and write. No truth oracle or tested semantic entailment. Operating mode is requested review, with repetitions or salience as triggers for recommendations rather than improvement evidence. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/server.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Raw event groups, related-memory metadata, recommendation and trace_count; no internally synthesized factual summary.
- Later read-back: Suggestions themselves are not persisted; caller-selected prose and IDs can enter separate consolidation/retention.
- Delegated visibility: inapplicable — no delegated review worker.
- Selection predicate: Scope/since/agent filters; first three normalized content terms group; related matches suggest update, repeated or salience at least 0.7 suggest create.
- Invalidation or expiry: New traces or filter changes recompute groups; malformed JSON is skipped. Consolidation does not automatically clear traces.
- Activation or effect: Advisory recommendation to caller for the review invocation, not evidence-consuming acceptance or automatic synthesis.
- Evidence limits: Grouping does not establish common factual referent, novelty or contradiction handling; source content origin unknown for generic observations.

> key = " ".join(terms[:3]) if terms else str(trace.get("type") or "trace")
> --- `src/smriti_mcp/store.py`

#### EPI-RTE-maintenance-check
Label: Health diagnostics

Part of: [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance)

Store scan/index → health rule evaluation → returned report. Target/domain: duplicate normalized titles, inactivity of active notes, body word count, alias-resolvable links among scanned notes. These are code-relative structural properties, not factual claims in notes. Caller requests; program evaluates; no answer oracle beyond those predicates. Computed counts and diagnostics are entailed by the inspected representation/rules, not independently warranted assertions about external reality. SRC-1, `src/smriti_mcp/store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts and IDs/details for duplicates, stale, oversized and unresolved links.
- Later read-back: inapplicable — health results are not saved or consumed by an automatic corrective branch.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: Scanned parseable titled nonreserved notes; active inactivity at least 180 days, body above 2500 words, same lowercased title, unresolved alias target.
- Invalidation or expiry: Recompute upon request; changed notes/time can change diagnoses.
- Activation or effect: Advisory report to requesting caller for current review; no enforced rejection, archive or deletion. Epistemic license only for the named representation-level diagnostics.
- Evidence limits: A stale note can be true and a recently accessed note false; no deployed diagnostic output supplied.

> if int(note.get("word_count") or 0) > 2500:
>     oversized.append({"id": note_id, "word_count": note.get("word_count")})
> --- `src/smriti_mcp/store.py`

#### EPI-RTE-maintenance-rewrite
Label: Deterministic text and metadata reshaping

Part of: [RT-RTE-store-maintenance](runtime.md#rt-rte-store-maintenance)

The maintenance transformation part: selected files → inferred defaults, link normalization/insertion and index formatting → rewritten notes/derived indexes. Caller invokes and can select dry-run or skip phases; code proposes/adopts edits without per-edit human approval. No truth oracle. Defaults come from title/body/path, not evidence-consuming semantic acceptance. Direct create additionally uses the same kind of truncating description transformation, a counterpath to the omission claim rather than another maintenance invocation. SRC-1, `src/smriti_mcp/store.py`, `src/smriti_mcp/fix_frontmatter.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Change counts/details/index paths; CLI prints summary and some error conditions cause nonzero exit.
- Later read-back: Repaired titles/categories/descriptions affect scans/rank/index; inserted wikilinks feed links/backlinks and optional recall expansion. Markdown index can be loaded later.
- Delegated visibility: inapplicable — local batch rules only.
- Selection predicate: Repair's nonhidden nonreserved Markdown; existing heading or filename title, metadata/type/path category, first body line description; unique title/alias whole-phrase linking, protected code/links and self-target exclusion.
- Invalidation or expiry: Rebuild overwrites derived indexes; caller can restore/edit notes, but no batch rollback. Dry-run does not simulate all metadata edits.
- Activation or effect: Enforcing local file changes upon invocation; later ranking and graph selection can change. Description truncation has indeterminate semantic preservation; indexes reorder/format, and links add symbolic associations rather than warranted facts.
- Evidence limits: No corpus/run demonstrates semantic fidelity; hidden path exclusions can suppress repair. Truncated/inferred metadata cannot be promoted to accepted knowledge.

Concrete deduction, no execution: take a body consisting of 151 letter A characters followed by the exact string ` is safe only when isolated.`. The first 160 characters are the A prefix followed by ` is safe `; whitespace collapsing does not alter this input. create_memory with no description assigns that prefix as both description fields, so the displayed assertion omits its necessary condition. This falsifies universal semantic-preservation and omitted-description claims; it does not prove every truncation is ampliative. The overall transformation remains indeterminate without actual content and intended interpretation. Normalization/indexing also contain non-ampliative reshaping cases: an unambiguous title `Cache` in `Use Cache.` becomes `Use [[Cache]].`, retaining display text while adding a graph edge consumed by optional recall traversal. An alias match adds canonical target with original display text; ambiguity exclusion does not test referent identity in natural language.

> collapsed = re.sub(r"\s+", " ", content).strip()
> return collapsed[:160] if collapsed else "Durable memory."
> --- `src/smriti_mcp/store.py`

> if not meta.get("description") and not meta.get("short_description"):
>     summary = self._short_description_from_content(content)
>     meta["description"] = summary
>     meta["short_description"] = summary
> --- `src/smriti_mcp/store.py`

> if display == title:
>     return f"[[{title}]]"
> return f"[[{title}|{display}]]"
> --- `src/smriti_mcp/store.py`

Repair has an independent fallback:

> first_line = body.strip().splitlines()[0].strip()
> meta["description"] = first_line[:160]
> --- `src/smriti_mcp/fix_frontmatter.py`

#### EPI-RTE-lifecycle-disposition
Label: Lifecycle withdrawal and replacement

Part of: [RT-RTE-memory-write](runtime.md#rt-rte-memory-write)

Caller command → status/delete or old/new note rewrite → later selector. Caller proposes/decides withdrawal; program enforces mutations, not factual refutation or evidence-consuming acceptance of replacement. Open requests; no answer oracle. Optional reason is caller prose; no criticism structure is required or checked. Recovery is external restoration/edits; supersession's two saves are sequential. SRC-1, `src/smriti_mcp/store.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Archived/updated/deleted/superseded IDs and status.
- Later read-back: Archive/supersession metadata enters later filters/penalties; both superseded/new notes remain; delete removes a note from subsequent scans.
- Delegated visibility: inapplicable — no delegation.
- Selection predicate: Caller-selected IDs with existing target; no requirement for contradictory evidence or verified replacement.
- Invalidation or expiry: Re-edit/replacement/deletion; not a target-managed undo facility.
- Activation or effect: Default recall exclusion of archived/superseded; ranking penalties in search absent explicit status control; get and overrides can still expose historical content. Force is selective operational withdrawal across later calls, not universal revocation or epistemic disproof.
- Evidence limits: No supplied reason/claim/run; no automated contradiction-resolution conclusion follows from supersedes metadata.

> old_doc.meta["status"] = "superseded"
> old_doc.meta["superseded_by"] = new_id
> --- `src/smriti_mcp/store.py`

### Claims

#### EPI-CLM-consolidation-provenance
Label: Agent supplied consolidation and provenance

Claim: consolidation stores reviewed agent-supplied prose and records provenance without internally summarizing. SRC-1, `src/smriti_mcp/server.py`, doctrine/design. Distinct from [RT-CLM-file-controls](runtime.md#rt-clm-file-controls); closest supplied mechanism is [RT-RTE-trace-consolidation](runtime.md#rt-rte-trace-consolidation). This claim's no-internal-summary part is supported; review is advisory and provenance is branch-bounded, not support checking.

> "Create, append, or update a durable memory from agent-supplied consolidated content. "
> "Use after reviewing traces; Smriti records provenance but does not summarize content itself."
> --- `src/smriti_mcp/server.py`

#### EPI-CLM-summary-omission
Label: Missing summary remains omitted

Claim: remember leaves an omitted short_description omitted rather than deriving a partial body summary. SRC-1, `README.md`, doctrine/design; also `src/smriti_mcp/server.py` RememberMetaInput field doctrine. No supplied claim counterpart; differs from file-controls claim and qualifies a write-route behavior without superseding the runtime's valid container record. Auto/create reaches create_memory fallback, contradicting this universal omission claim. Update/append have different preservation behavior.

> `remember` treats supplied `meta` as authoritative. If `short_description` is omitted,
> Smriti leaves it omitted instead of deriving a partial summary from the body. In `auto`
> --- `README.md`

#### EPI-CLM-recall-bundle
Label: Deterministic task recall

Claim: return a compact deterministic bundle using lexical and metadata/link cues. SRC-1, `src/smriti_mcp/server.py`, doctrine/design. No supplied claim counterpart; closest route is [RT-RTE-context-recall](runtime.md#rt-rte-context-recall). This is a selector claim, not an express truth/relevance guarantee or proof of task improvement.

> "Return a compact, deterministic recall bundle for an agent task using lexical match, "
> "metadata, salience, access history, status, and optional wikilink traversal."
> --- `src/smriti_mcp/server.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; each declared route describes its own consumer, channel, force and horizon. Static host guidance remains [RT-BAP-tool-guidance](runtime.md#rt-bap-tool-guidance).
