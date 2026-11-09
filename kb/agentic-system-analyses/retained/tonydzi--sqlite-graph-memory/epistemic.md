---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "sqlite-graph-memory epistemic routes: imported snippets, transcript-derived state, retrieval authority and bounded evaluator licenses."
run-id: AAS-2026-11-08-sqlite-graph-memory-ca3785ec5c2e-01
reviewed-boundary: f05db2778159d50a0ad8a35be4f2be3a6aea94b1
---

# sqlite-graph-memory epistemic report

## Source-and-claim boundary

The question is what content this shipped memory layer acquires, transforms, checks and licenses for later reliance. The functional scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); evidence identities are in its [Source register](boundary.md#source-register), SRC-1. The private home pipeline, external agent reasoning and editing, model weights and host compliance are not inside the frozen executable account. No target execution was performed. Implementation establishes capacity and wiring, not activation or benefit.

The ordinary retrieval path is not an answer author. It imports note text, selects indexed snippets and returns context. Its numerical relevance scores are not truth evaluations. The shipped benchmark adds an answer selector, abstention and reference-based checking; these must not be projected onto MCP. Temporal closure instructions request a stronger reliance discipline than the retriever enforces. Relevant claims are [EPI-CLM-search-layer](#epi-clm-search-layer), [EPI-CLM-measurement-scope](#epi-clm-measurement-scope), [RT-CLM-temporal-scope](runtime.md#rt-clm-temporal-scope) and [RT-CLM-scoped-return](runtime.md#rt-clm-scoped-return).

### Coverage

Direct reads below supply implementation unless explicitly marked doctrine. Supplied runtime findings remain distinguishable from direct inspection. All paths are SRC-1 at the reviewed commit; the source register is not copied here.

| Entry point or operation | Source path | Coverage / records or limit |
|---|---|---|
| CLI registration; MCP tool registry and dispatch, including direct-test wrapper | `pyproject.toml`; `src/sqlite_graph_memory/mcp_server.py` | Direct, complete reads; [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall), [RT-CLM-scoped-return](runtime.md#rt-clm-scoped-return). Only recall is advertised; error handling checks successful transport, not source truth. |
| Index admission, refresh, dropped files, clipping | `src/sqlite_graph_memory/index_notes.py` | Direct, complete; [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), [EPI-OBJ-note-snippets](#epi-obj-note-snippets). |
| Dense, graph, entity, supersession, PPR call sites, A/B, formatted delivery | `src/sqlite_graph_memory/brain_ask.py` | Direct, complete; [RT-RTE-recall-options](runtime.md#rt-rte-recall-options), [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery). PPR internals and backend internals are supplied runtime findings, not independently reread. |
| Encoder and reranker versions, mutability | `src/sqlite_graph_memory/onnx_backend.py`; `src/sqlite_graph_memory/ppr.py` | Supplied [RT-CMP-e5-model](runtime.md#rt-cmp-e5-model), [RT-CMP-rerank-model](runtime.md#rt-cmp-rerank-model), [RT-RTE-recall-options](runtime.md#rt-rte-recall-options). Exact weights and model internals unavailable; prevents semantic guarantees from numerical scores. |
| Stop registration, capture and ledger inspection | `examples/claude-code-stop-hook.json`; `src/sqlite_graph_memory/turnstate_hook.py`; `src/sqlite_graph_memory/turnstate_show.py` | Direct, complete; [RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture), [EPI-OBJ-turns](#epi-obj-turns). Viewer is a consequential human-facing consumer, not automatic recall integration. |
| Gold construction; scoring, persistence, mutant withdrawal | `eval/build_gold.py`; `eval/run_eval.py` | Direct, complete; [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths), [EPI-OBJ-evaluation-records](#epi-obj-evaluation-records). `run_ablation.py` composition supplied by runtime, not independently reread. |
| Benchmark answer and abstention | `bench/adapters/sgm.py`; `bench/adapters/_extract.py`; `bench/vault/tool-lanternfish.md` | Direct, complete; [EPI-RTE-extract-answer](#epi-rte-extract-answer), [EPI-RTE-answer-abstain](#epi-rte-answer-abstain). Concrete static deduction below, not execution. |
| Benchmark scoring, result gate, rerun comparison and CI consumer | `bench/bench_core.py`; `bench/validate.py`; `bench/run.py`; `.github/workflows/bench.yml` | Direct, complete; [EPI-RTE-bench-score](#epi-rte-bench-score), [EPI-RTE-bench-gate](#epi-rte-bench-gate). Result artifacts, generator, questions and leaderboard implementation not assessed for observed outcomes or causal gains. Other-system adapters are not characterized. |
| Diagnostic checks and verdicts | `src/sqlite_graph_memory/vault_stats.py`; `src/sqlite_graph_memory/doctor.py` | Direct, complete; [EPI-RTE-diagnostic-checks](#epi-rte-diagnostic-checks). These were not assessed in detail by runtime; they add bounded truth-apt graph/environment reports, not note validation. |
| Temporal writer/reader rules and public claims | `BITEMPORAL.md`; `README.md` | Direct, complete, doctrine/design and attributed reported operation; [RT-BAP-temporal-instructions](runtime.md#rt-bap-temporal-instructions), claim records below. |
| Product change and publishing | `AGENTS.md`; `.github/workflows/tests.yml`; `.github/workflows/publish.yml`; `docs/RELEASING.md` | Supplied [RT-RTE-change-admission](runtime.md#rt-rte-change-admission). Repository protection, actual maintainer decisions and deployed successor use uninspected. |
| Remaining included support, tests, paper, alternate agent guides, temporal design note | Paths inventoried in boundary | Available but not independently inspected here. No claim of a system-complete absence of knowledge production, a complete doctrine census, passing tests or private-system performance follows. The negative conclusions below concern the enumerated executable routes only. |

Missing host traces prevent determining whether context changed an agent's decisions or ledger text reached an agent. Missing authenticated execution and comparison evidence prevent assigning observed operation or causal benefit to the reconstructed routes. Uninspected benchmark result conditions prevent adopting the README's numbers as verified outcomes. Missing note-author evidence prevents assigning imported propositions a source warrant; missing provider internals prevents individuating truth-apt propositions in distributed numerical state. None of these limitations erases the inspected architectural capacities.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-note-snippets](#epi-obj-note-snippets) | Imported note assertions, potentially knowledge or instructions; stored substrings, not guaranteed whole assertions | see record | SRC-1, `src/sqlite_graph_memory/index_notes.py` | External authorship and truth unknown; frontmatter and later qualifications can be omitted. |
| [EPI-OBJ-recall-state](#epi-obj-recall-state) | Scores/edges express selection relations; no individuated world-knowledge proposition in vectors | see record | SRC-1, `src/sqlite_graph_memory/brain_ask.py` | Numerical state is not a truth certificate. Current graph and old snippets can have different freshness. |
| [EPI-OBJ-turns](#epi-obj-turns) | Text of asks, assistant statements and proposed decisions; structured claims that tools/files/commands appeared | see record | SRC-1, `src/sqlite_graph_memory/turnstate_hook.py` | Tool invocation is not successful effect; asserted decisions are not validated commitments or facts. |
| [EPI-OBJ-evaluation-records](#epi-obj-evaluation-records) | Reference-note labels; extracted answers and citations; metric propositions about supplied outputs | see record | SRC-1, `bench/bench_core.py` | Label fidelity and execution provenance bound all conclusions. |
| [EPI-OBJ-diagnostic-report](#epi-obj-diagnostic-report) | Graph counts/date classifications and environment/file-presence observations | see record | SRC-1, `src/sqlite_graph_memory/vault_stats.py` | Health thresholds are policy judgments, not evidence that a note is true or a deployment works. |

## Authority-route ledger

Each ledger row is a consequential function, not an entire API. Repeated implementations are split by function. Fields owned by an existing record are cited rather than copied. All implementation rows have unobserved activation; none grants warrant beyond the indicated target domain.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-index-admission](runtime.md#rt-rte-index-admission) | content transformation | implemented | [EPI-OBJ-note-snippets](#epi-obj-note-snippets) | truth-apt transformation: acquisition/import | see route | see route | see route | see route | see route | Source warrant unknown, not established by indexing | see route | see route | SRC-1, `src/sqlite_graph_memory/index_notes.py` | [EPI-CLM-search-layer](#epi-clm-search-layer) | none | Import precedes substring reshaping; no semantic review. |
| [RT-RTE-index-admission](runtime.md#rt-rte-index-admission) | retention | implemented | [EPI-OBJ-note-snippets](#epi-obj-note-snippets) | truth-apt transformation: non-ampliative reshaping | Indexed snippets/vectors | see route | see route | see route | see route | Retains selected text, not accepted claims | see route | see route | SRC-1, `src/sqlite_graph_memory/index_notes.py` | none | none | Clipping preserves characters, not necessarily assertion scope. |
| [RT-RTE-index-admission](runtime.md#rt-rte-index-admission) | lineage/freshness/recovery | implemented | [EPI-OBJ-note-snippets](#epi-obj-note-snippets) | no content change | File change/removal and artifact reuse | see route | see route | see route | see route | Freshness only under file fingerprint assumptions | see route | see route | SRC-1, `src/sqlite_graph_memory/index_notes.py` | none | none | Removal/rebuild is not epistemic rejection or rollback of an accepted theory. |
| [RT-RTE-recall-options](runtime.md#rt-rte-recall-options) | operational admission/selection/consumption | implemented | [EPI-OBJ-recall-state](#epi-obj-recall-state) | no content change | Candidate membership/order | see route | see route | see route | see route | Relevance/graph proximity only; no statement truth license | see route | see route | SRC-1, `src/sqlite_graph_memory/brain_ask.py` | [RT-CLM-temporal-scope](runtime.md#rt-clm-temporal-scope) | Temporal rule not enforced | Supersession access is not withdrawal of stale assertions. |
| [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall) | operational admission/selection/consumption | implemented | [EPI-OBJ-note-snippets](#epi-obj-note-snippets) | truth-apt transformation: non-ampliative reshaping | Bundle delivery | see route | see route | see route | see route | Advisory imported excerpts, no acceptance | see route | see [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery) | SRC-1, `src/sqlite_graph_memory/mcp_server.py` | [EPI-CLM-search-layer](#epi-clm-search-layer) | none | Child exit success is transport success, not knowledge warrant. |
| [RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture) | content transformation | implemented | [EPI-OBJ-turns](#epi-obj-turns) | truth-apt transformation: acquisition/import | Transcript events | see route | see route | see route | see route | Original statements acquired with unknown source warrant | see route | see route | SRC-1, `src/sqlite_graph_memory/turnstate_hook.py` | none | none | Structural event parsing can warrant only bounded claims about supplied events. |
| [RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture) | retention | implemented | [EPI-OBJ-turns](#epi-obj-turns) | truth-apt transformation: non-ampliative reshaping | Selected/clipped ledger fields | see route | see route | see route | see route | Retained candidate/history, not acceptance | see route | see route | SRC-1, `src/sqlite_graph_memory/turnstate_hook.py` | none | none | No checks of assistant claim truth or tool success. |
| [RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture) | operational admission/selection/consumption | implemented | [EPI-OBJ-turns](#epi-obj-turns) | truth-apt transformation: non-ampliative reshaping | Viewer-selected rows | see route | see route | see route | see route | Human-readable operational history | see route | see route | SRC-1, `src/sqlite_graph_memory/turnstate_show.py` | none | none | Viewer drops evidence pointer/offset fields and clips further; automatic model consumption unestablished. |
| [EPI-RTE-extract-answer](#epi-rte-extract-answer) | content transformation | implemented | [EPI-OBJ-evaluation-records](#epi-obj-evaluation-records) | truth-apt transformation: non-ampliative reshaping | see route | see route | see route | see route | see route | Attribution to synthetic text only | see route | see route | SRC-1, `bench/adapters/_extract.py` | [EPI-CLM-measurement-scope](#epi-clm-measurement-scope) | Not production answering | Lexical overlap is not entailment checking. |
| [EPI-RTE-answer-abstain](#epi-rte-answer-abstain) | disposition/acceptance | implemented | [EPI-OBJ-evaluation-records](#epi-obj-evaluation-records) | no content change | see route | see route | see route | see route | see route | Operational answer admission only | see route | see route | SRC-1, `bench/adapters/sgm.py` | none | none | No evidence-consuming acceptance of a new ampliative claim. |
| [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths) | check/evidence production | implemented | [EPI-OBJ-evaluation-records](#epi-obj-evaluation-records) | truth-apt transformation: entailed derivation | Ranks versus reference sets | see route | see route | see route | see route | Metrics conditional on gold and selected composition | see route | see route | SRC-1, `eval/run_eval.py` | [EPI-CLM-measurement-scope](#epi-clm-measurement-scope) | Shared functions, different policy composition | Gold generation derives labels from notes/links, not independent truth judgments. |
| [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths) | retention | implemented | [EPI-OBJ-evaluation-records](#epi-obj-evaluation-records) | no content change | Evaluation history | see route | see route | see route | see route | Retention of measurement evidence, not production acceptance | see route | see route | SRC-1, `eval/run_eval.py` | none | none | Mutant mode explicitly withholds score persistence. |
| [EPI-RTE-bench-score](#epi-rte-bench-score) | check/evidence production | implemented | [EPI-OBJ-evaluation-records](#epi-obj-evaluation-records) | truth-apt transformation: entailed derivation | see route | see route | see route | see route | see route | Fixed scorer's bounded verdicts about outputs/text | see route | see route | SRC-1, `bench/bench_core.py` | [EPI-CLM-measurement-scope](#epi-clm-measurement-scope) | none | Truth of vault assertions and semantic answer entailment not checked. |
| [EPI-RTE-bench-gate](#epi-rte-bench-gate) | disposition/acceptance | implemented | [EPI-OBJ-evaluation-records](#epi-obj-evaluation-records) | no content change | see route | see route | see route | see route | see route | Acceptance of result consistency for reporting, not truth of answers | see route | see route | SRC-1, `bench/validate.py` | [EPI-CLM-measurement-scope](#epi-clm-measurement-scope) | none | Rerun equality does not establish that a pipeline explanation is correct. |
| [EPI-RTE-diagnostic-checks](#epi-rte-diagnostic-checks) | check/evidence production | implemented | [EPI-OBJ-diagnostic-report](#epi-obj-diagnostic-report) | truth-apt transformation: entailed derivation | Graph counts/dates | see route | see route | see route | see route | Parsed graph and age arithmetic under supplied date and filesystem | see route | see route | SRC-1, `src/sqlite_graph_memory/vault_stats.py` | none | none | No semantic truth/freshness test. |
| [EPI-RTE-diagnostic-checks](#epi-rte-diagnostic-checks) | check/evidence production | implemented | [EPI-OBJ-diagnostic-report](#epi-obj-diagnostic-report) | truth-apt transformation: entailed derivation | Environment/import/file-presence predicates | see route | see route | see route | see route | Narrow checked predicates, not verified deployment readiness | see route | see route | SRC-1, `src/sqlite_graph_memory/doctor.py` | none | none | A cache directory can exist without valid model bytes. |
| [EPI-RTE-diagnostic-checks](#epi-rte-diagnostic-checks) | disposition/acceptance | implemented | [EPI-OBJ-diagnostic-report](#epi-obj-diagnostic-report) | non-truth-apt policy/content update: threshold verdict | Health classifications/exit status | see route | see route | see route | see route | No additional truth license beyond checks | see route | see route | SRC-1, `src/sqlite_graph_memory/vault_stats.py` | none | none | Thresholds advise repair, do not remove/approve notes. |
| [RT-RTE-change-admission](runtime.md#rt-rte-change-admission) | disposition/acceptance | implemented | [EPI-OBJ-evaluation-records](#epi-obj-evaluation-records) | non-truth-apt policy/content update: product release choice | see route | see route | see route | see route | see route | Build checks and prescribed regression criterion are distinct | see route | see route | SRC-1, `.github/workflows/publish.yml` | none | Documented measurement veto not publisher invariant | Actual human veto and upgrade use uninspected. |
| [RT-BAP-temporal-instructions](runtime.md#rt-bap-temporal-instructions) | disposition/acceptance | doctrine only | [EPI-OBJ-note-snippets](#epi-obj-note-snippets) | non-truth-apt policy/content update: close mistaken/expired records | Temporal reliance and human deletion veto | see path | see path | Requested closing, history citation and replacement | Natural-language prescription only | Temporal discipline requested, not factual correctness | see path | see path | SRC-1, `BITEMPORAL.md` | [RT-CLM-temporal-scope](runtime.md#rt-clm-temporal-scope) | Host installation/compliance unobserved | No package writer executes the block. |

No lifecycle-integration row is inferred from storage, link expansion or telemetry: within these inspected executable routes, no evidence-consuming acceptance of new ampliative knowledge precedes such integration. This is a bounded route conclusion, not a claim that an external author cannot maintain accepted knowledge.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-search-layer](#epi-clm-search-layer) | see claim | SRC-1, `README.md`, doctrine/design | see claim | [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall) | Not assessed | No host-use comparison | Context recall is wired; source truth and agent compliance are not thereby warranted | Read-only describes note recall, not ledger/telemetry writes. |
| [EPI-CLM-measurement-scope](#epi-clm-measurement-scope) | see claim | SRC-1, `README.md`, doctrine/design and reported operation | see claim | [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths), [EPI-RTE-bench-score](#epi-rte-bench-score), [EPI-RTE-bench-gate](#epi-rte-bench-gate) | Private numbers attributed only; public result conditions unassessed | Link-derived gold favors walking links; default MCP and benchmark differ | Metrics/checks have operative reporting force, with local reference-dependent license | “What you measure is what runs” holds for shared functions, not all composed policies or answer consumers. |
| [RT-CLM-temporal-scope](runtime.md#rt-clm-temporal-scope) | see claim | SRC-1, `BITEMPORAL.md`, doctrine/design | see claim | [RT-RTE-recall-options](runtime.md#rt-rte-recall-options) | None supplied for host adherence | Following replacement is not open-record filtering or historical query semantics | Portable temporal discipline is prescribed; limited replacement access is implemented | Closed content can still rank and be delivered as unqualified text. |
| [RT-CLM-scoped-return](runtime.md#rt-clm-scoped-return) | see claim | SRC-1, `src/sqlite_graph_memory/mcp_server.py`, implementation | see claim | [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall) | None supplied | Child success and scoped output do not check statements | Transport contamination protection, not truth validation | No warrant upgrade from error containment. |

## Bounded conclusion

The package grants **selection authority**, not a general epistemic endorsement. Indexed note assertions enter with unknown source warrant; character-preserving clipping and frontmatter removal can degrade contextual warrant. The host sees a bounded excerpt, not all caveats, evidence or temporal metadata. Dense, cross-encoder and graph scores license ranking under their algorithms, not reliance on a proposition's truth ([EPI-OBJ-note-snippets](#epi-obj-note-snippets), [EPI-OBJ-recall-state](#epi-obj-recall-state), [RT-BAP-context-delivery](runtime.md#rt-bap-context-delivery)). Model parameters are not updated in the supplied inspected inference paths; exact versions and internal factual representations remain unresolved independently of text retention ([RT-CMP-e5-model](runtime.md#rt-cmp-e5-model), [RT-CMP-rerank-model](runtime.md#rt-cmp-rerank-model)).

Transcript capture acquires statements and derives a lossy operational ledger. Its later viewer establishes read-back to a person, not automatic answer correction or learning. Selection of a decision-looking line is neither criticism of its content nor validation of the represented action. The parser's invocation records license at most claims about transcript structure, not successful file modification ([RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture), [EPI-OBJ-turns](#epi-obj-turns)).

The evaluators do produce checkable, bounded propositions: set/rank metrics relative to generated labels; literal citation occurrence and gold-answer matches; numerical consistency of result files; graph/environment predicates. Their warranted premises are the supplied labels, bytes and fixed formal rules, not externally certified world facts. Benchmark answer retention/admission is a score-threshold and nonempty-sentence rule, not acceptance of an ampliative conjecture. Benchmark validation accepts result consistency for reporting; CI status can block continuation under configured workflows, but repository-wide merge enforcement is external. Diagnostics classify and advise through stdout and exit codes, without revising memory ([RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths), [EPI-RTE-answer-abstain](#epi-rte-answer-abstain), [EPI-RTE-bench-score](#epi-rte-bench-score), [EPI-RTE-bench-gate](#epi-rte-bench-gate), [EPI-RTE-diagnostic-checks](#epi-rte-diagnostic-checks)).

Among the inspected executable routes there is no established produced, accepted ampliative knowledge or post-acceptance lifecycle integration. The contrary candidate—the benchmark's apparent answering—is extractive reshaping plus operational admission, while score arithmetic is entailed derivation in a bounded symbolic domain. Portable instructions can direct external closure and changed reliance, but publication does not establish execution. No independent conclusion about learning, reflection, autonomous theory building or self-improvement follows from persistence or measurement wiring. Product-regression doctrine and release machinery exist; actual evidence-responsive successor adoption and later causal effects remain uninspected ([EPI-RTE-extract-answer](#epi-rte-extract-answer), [RT-BAP-temporal-instructions](runtime.md#rt-bap-temporal-instructions), [RT-RTE-change-admission](runtime.md#rt-rte-change-admission)).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-note-snippets
Label: Indexed note snippets

Natural-language note bodies and stored snippets are acquired from caller-selected Markdown files. Paths, dates and titles are symbolic metadata; dense arrays are the separate numerical part. Text and metadata persist in `_brain_e5_meta.pkl`, vectors in `_brain_e5.npy`, with a JSON manifest. No runtime object counterpart is declared; closest supplied route is [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), which owns the admission process, not this stored object. SRC-1, `src/sqlite_graph_memory/index_notes.py`.

> body = t[m.end():] if m else t
> --- `src/sqlite_graph_memory/index_notes.py`

> meta.append({'path': str(p), 'title': title,
>              'snippet': c[:SNIPPET_CHARS], 'date': date})
> --- `src/sqlite_graph_memory/index_notes.py`

Clipping is selection of existing characters, not evidence of semantic preservation of an entire assertion. A qualification after character 600 cannot reach recall through that chunk's snippet. The next chunk starts at 1000 under the fixed 1200/200 settings, so delivery is not a guarantee that all omitted material appears in another result. Source-note truth and original evidence lineage are external; path and date establish traceability, not endorsement. Refresh/removal and fast-path hazards are owned by the supplied route.

#### EPI-OBJ-recall-state
Label: Recall candidates and scores

Dense index/query vectors are distributed-parametric numerical arrays; ranked indices, graph target matches, flags and formatted headings are symbolic. Source-native numerical components are already [RT-CMP-e5-model](runtime.md#rt-cmp-e5-model) and [RT-CMP-rerank-model](runtime.md#rt-cmp-rerank-model); this object instead identifies their output/candidate state, not another model. Closest route is [RT-RTE-recall-options](runtime.md#rt-rte-recall-options). Vectors persist in NumPy; per-query lists live in memory and selected text is mirrored to an answer file. SRC-1, `src/sqlite_graph_memory/brain_ask.py`.

> return emb @ qv
> --- `src/sqlite_graph_memory/brain_ask.py`

> pairs = [(query, meta[i]['title'] + '. ' + meta[i]['snippet']) for i in cand]
> sc = ce.predict(pairs) if len(pairs) else []
> --- `src/sqlite_graph_memory/brain_ask.py`

No individuated truth-apt world proposition is determinable from the numerical vectors within accessible evidence. Link proximity and pair scores have fixed ranking consumers; neither is an answer oracle. A countercase to temporal exclusion is that the gated branch adds replacements to `base_order` without removing the superseded seed; see the supplied route's passage. Current-file graph reads and old stored snippets do not form one guaranteed-current assertion set.

#### EPI-OBJ-turns
Label: TurnState rows

Natural-language ask/summary/decision text and symbolic session, tool, command, file and evidence-pointer fields persist in SQLite `turns`. No runtime object counterpart; closest process is [RT-RTE-turnstate-capture](runtime.md#rt-rte-turnstate-capture). SRC-1, `src/sqlite_graph_memory/turnstate_hook.py`, `src/sqlite_graph_memory/turnstate_show.py`.

> summary = "\n".join(summary_parts).strip()
> for ln in summary.splitlines():
>     ln = ln.strip(" -*#>").strip()
>     if 8 <= len(ln) <= 180 and DECISION_RX.search(ln):
>         decisions.append(ln)
> --- `src/sqlite_graph_memory/turnstate_hook.py`

Concrete static deduction: an assistant text block `Next step: verify cache.` is appended to `summary_parts`, joined unchanged, then passes length and case-insensitive `next step` matching and becomes a decision string. A `Write` tool-use input with `file_path` is added to `files` without checking any tool-result success. Thus “decision” and “files” are parser classifications of supplied events, not certified commitments or successful writes. This follows implementation, with no fixture or target execution.

> if name in FILE_TOOLS:
>     fp = inp.get("file_path") or inp.get("notebook_path")
>     if fp:
>         files.append(fp)
> --- `src/sqlite_graph_memory/turnstate_hook.py`

The viewer selects no evidence/byte-offset columns and prints only a 200-character summary. The original ledger pointer still permits external investigation if the transcript survives; automatic evidential checking is not implemented by this viewer.

#### EPI-OBJ-evaluation-records
Label: Gold, answers and metric records

Mixed natural-language questions/answers/quotes and symbolic note IDs, reference sets, rankings, metrics and run metadata. Gold and score JSONL, benchmark JSON results and optional SQLite `gold_eval` retain them; evaluation call state is in memory. No supplied operative-object counterpart; the closest container process is [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths). SRC-1, `eval/build_gold.py`, `eval/run_eval.py`, `bench/run.py`, `bench/bench_core.py`.

> elif cls == 'temporal':
>     g, dropped = [n['sup']], 0
> else:
>     g, dropped = [n['stem']], 0
> --- `eval/build_gold.py`

Gold labels are constructed expectations, not newly established claims that a linked note really answers the query. Bridge gold is a capped sorted subset of parsed links. Ambiguous stems are excluded by `main`; this is a countercase to treating every note as an eligible independent label.

> stems = all_stems - ambiguous
> --- `eval/build_gold.py`

> if os.environ.get('EVAL_MUTANT') == '1':
>     # A mutant run must never enter the history it would later be compared against: a
>     # leftover env var is enough to make every future diff meaningless.
>     print('nothing written: EVAL_MUTANT=1 runs are never persisted')
>     return 0
> --- `eval/run_eval.py`

This withdrawal concerns intentionally corrupted measurement output, not truth assessment of notes. The record does not adopt any retained result as verified execution or causal evidence.

#### EPI-OBJ-diagnostic-report
Label: Graph and environment health reports

Symbolic counts, dates, paths, verdict strings and exit statuses, rendered as natural-language lines or JSON to stdout. No persistent repair state is written by the inspected checks. Distinct from [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths): targets filesystem/installation health, not retrieval outputs against gold. No supplied object counterpart. SRC-1, `src/sqlite_graph_memory/vault_stats.py`, `src/sqlite_graph_memory/doctor.py`.

> orphan_pct = round(100.0 * len(orphans) / n, 1)
> degree = round(len(edges) / n, 2)
> main, n_comp = largest_component(pages, edges)
> main_pct = round(100.0 * main / n, 1)
> --- `src/sqlite_graph_memory/vault_stats.py`

The report can entail graph-count propositions under its parsing domain. Age is measured from metadata, not from fact-checking content; unknown dates are not counted as stale. Doctor's file-presence observations have still narrower meaning than its user-facing “all good” language.

### Routes

#### EPI-RTE-extract-answer
Label: Benchmark sentence extraction
Part of: [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths)

This material subroute is distinct from the container's overall retrieval/metric loop: `Adapter.ask` supplies ranked note IDs and raw notes to `best_sentence`, which chooses a normalized sentence from the first three notes. Python owns the lexical policy; no human or generative model edits a sentence here. Output is natural-language candidate text with symbolic note identity, in memory until `bench/run.py` persists the result. SRC-1, `bench/adapters/sgm.py`, `bench/adapters/_extract.py`, `bench/bench_core.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `(note id, sentence, overlap)` to the adapter.
- Later read-back: Benchmark result JSON retains returned answer/citation for scoring and reporting; no production recall consumer of this answer is established.
- Delegated visibility: inapplicable — deterministic helper, not a delegated agent.
- Selection predicate: Positive maximum overlap of non-stopword token sets over sentences from first three ranked notes; strict greater-than retains earlier ties.
- Invalidation or expiry: Invocation-local candidate; rerunning can replace the caller's result file, not a knowledge store.
- Activation or effect: Selected text feeds abstention and citation construction; actual run activation uninspected.
- Evidence limits: Normalized substring selection does not evaluate contextual answer correctness or semantic entailment.

> for nid in ranked_ids[:depth]:
>     for s in sentences(read_note(nid)):
>         ov = len(qt & tokens(s))
>         if ov > best[2]:
>             best = (nid, s, ov)
> --- `bench/adapters/_extract.py`

> text = WIKI_RX.sub(lambda m: m.group(2) or m.group(1), text or '')
> return re.sub(r'\s+', ' ', text).strip()
> --- `bench/bench_core.py`

Concrete input traced through inspected code: with only `tool-lanternfish` ranked, question `What language is Lanternfish written in?`, and its frozen raw note, frontmatter and heading are removed; punctuation-space splitting produces `Lanternfish is written in Elixir.` Tokens `lanternfish` and `written` overlap the question, whereas the maintenance sentence shares only `lanternfish`. The first sentence wins, becomes the answer and the same citation quote if the separate score gate permits it. This is non-ampliative selection, not generation of the Elixir claim or proof that the claim is true. No code was executed.

> Lanternfish is written in Elixir. Lanternfish is maintained by the [[team-willowherb|Willowherb]] team.
> --- `bench/vault/tool-lanternfish.md`

#### EPI-RTE-answer-abstain
Label: Benchmark answer admission
Part of: [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths)

Distinct material disposition after [EPI-RTE-extract-answer](#epi-rte-extract-answer). The adapter proposes the selected sentence; Python decides and vetoes output if the top reranker score is below 0.0 or there is no sentence. The cross-encoder is [RT-CMP-rerank-model](runtime.md#rt-cmp-rerank-model), not a separate truth oracle. Open benchmark questions use a fixed policy; humans choose the run/configuration, not per-answer admission. No proposal guidance beyond extractor and threshold; no accepted knowledge revision or rollback is involved. SRC-1, `bench/adapters/sgm.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answer/citation object or null answer and empty citations, plus retrieved IDs and top score.
- Later read-back: Caller stores per-question result for later benchmark scoring/validation; not later production knowledge integration.
- Delegated visibility: inapplicable — no reasoning-agent delegation; local model supplies a relevance score.
- Selection predicate: Top reranker score at least ABSTAIN_BELOW and nonempty extracted sentence.
- Invalidation or expiry: Recomputed per question; no stored acceptance state is maintained by the adapter.
- Activation or effect: Enforcing answer suppression at adapter return, not a gate in MCP recall.
- Evidence limits: Top-ranked note's score can admit a sentence from another of the first three notes; there is no sentence-specific truth check.

> if top < ABSTAIN_BELOW or not sent:
>     return {'retrieved': ids, 'answer': None, 'citations': [], 'top_score': round(top, 3)}
> return {'retrieved': ids, 'answer': sent, 'citations': [{'note': nid, 'quote': sent}],
>         'top_score': round(top, 3)}
> --- `bench/adapters/sgm.py`

Operational admission is permissive/enforcing for this benchmark response only. Its criterion does not consume evidence sufficient to accept a produced ampliative claim; the text was imported/extracted in the first place.

#### EPI-RTE-bench-score
Label: Benchmark reference checking
Part of: [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths)

Distinct material checker: `score_one` and aggregate functions evaluate per-question outputs against caller-supplied question answers/support IDs and normalized vault text. `bench/run.py` calls `score`, displays the metrics and persists them. Fixed Python owns comparison; question records provide the answer oracle. This is bounded evaluation, not per-note admission or a human approval workflow. SRC-1, `bench/bench_core.py`, `bench/run.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Recall, lexical answer hit, citation occurrence/support/answer-hit and abstention verdicts aggregated overall/by class.
- Later read-back: Metrics and per-question results persist in benchmark JSON; `check_result` rederives them for validation.
- Delegated visibility: inapplicable — deterministic scorer receives returned outputs, gold and normalized vault.
- Selection predicate: Fixed support sets, first k deduplicated retrieved IDs, bounded deduplicated citations; lexical word-boundary answer matching.
- Invalidation or expiry: Dependent on current questions, vault and outputs; no general validity beyond those inputs.
- Activation or effect: Produces displayed/persisted metrics used by the separate result gate; no automatic production-policy change.
- Evidence limits: Formal consistency/lexical matches do not certify source truth, answer entailment, completeness or real execution.

> ok = bool(quote) and nid in vault and quote in vault[nid]
> faithful.append(ok)
> if (ok and answerable and len(quote) >= MIN_QUOTE and nid in support
>         and contains_answer(quote, q['answers'])):
>     verbatim_hit = True
> --- `bench/bench_core.py`

A countercase to broad “faithful” semantics is a literal quote used with a wrong or contradictory answer: `citation_faithful` tests quote occurrence irrespective of that answer. `answer_ok` separately tests presence of a gold string, not negation or entailment. License is therefore exactly the implemented predicates. No causal result is inferred from this arithmetic.

#### EPI-RTE-bench-gate
Label: Benchmark result acceptance

Distinct from [RT-RTE-evaluation-paths](runtime.md#rt-rte-evaluation-paths)'s evaluation execution: this route admits/rejects a result *claim for reporting*, consuming scorer results, hashes and result structure, and optionally independent rerun outputs. It overlaps the checker [EPI-RTE-bench-score](#epi-rte-bench-score) but owns disposition, not metric production. Result submitter proposes; Python checks can veto; configured CI consumes nonzero status. Human merge powers/branch protections are external. Trigger is explicit CLI/CI invocation, not an adaptive recall loop. SRC-1, `bench/bench_core.py`, `bench/validate.py`, `.github/workflows/bench.yml`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Printed validation/reproduction findings and success/failure exit status.
- Later read-back: Committed result files remain; configured reproduction preserves rerun artifacts for diffing. Gate itself does not rewrite results or a production model.
- Delegated visibility: Reproduction subprocess runs the benchmark and returns a new result file; no delegated agent evaluation.
- Selection predicate: Shape/coverage/hash consistency, recomputed metric equality, generated vault/leaderboard consistency in ordinary full validation; optional rerun metric tolerance plus zero changed per-question keys.
- Invalidation or expiry: Changed vault/question hashes or mismatched results trigger rejection; correction/rerun is caller-owned, no automatic rollback of deployed code.
- Activation or effect: Nonzero command status fails its CI step; `reproduce` job depends on `validate`. Merge enforcement depends on external repository settings.
- Evidence limits: No gate or CI execution observed; self-awarded provenance is limited by configured list membership, and content consistency alone cannot authenticate execution.

> need(res.get('vault_sha256') == vault_sha, 'vault_sha256 does not match bench/vault (stale result or edited vault)')
> need(res.get('questions_sha256') == questions_sha, 'questions_sha256 does not match bench/questions.jsonl')
> --- `bench/bench_core.py`

> if worst > tol or changed > MAX_CHANGED:
>     print('FAIL the committed outputs for %s do not reproduce' % system); return 1
> print('ok   %s reproduces' % system)
> return 0
> --- `bench/validate.py`

> What it cannot catch: per-question outputs that were themselves made up. That is why a
> result says whether CI reproduced it (`reproduce.in_ci`), and the board shows it.
> --- `bench/validate.py`

> reproduce:
>   runs-on: ubuntu-latest
>   needs: validate
> --- `.github/workflows/bench.yml`

Acceptance criterion and use are bounded: consistent report relative to the frozen benchmark inputs, or reproduction agreement in the selected rerun mode. Neither accepts an external factual theory. A passing rerun supports repeatability of compared outputs under its environment, not component-level causal benefit or general transfer.

#### EPI-RTE-diagnostic-checks
Label: Health checks and verdict consumers

No supplied counterpart after comparison: runtime explicitly leaves `sgm-stats`/`sgm-doctor` detail unassessed. These operator-invoked deterministic routes assess graph structure/date metadata and machine import/cache/index presence, not retrieval against gold. Python owns checks and threshold verdicts; callers choose thresholds/date and whether to act on advice. There is no per-content human approval, reference answer oracle, successor selection or automatic repair. Check and disposition functions are separated in the ledger. SRC-1, `src/sqlite_graph_memory/vault_stats.py`, `src/sqlite_graph_memory/doctor.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Stats text/JSON and exit 0/1/2; doctor lines/fixes and exit 1 for failures, otherwise 0.
- Later read-back: inapplicable — these entry points do not persist their reports; external cron/log capture is outside inspected code.
- Delegated visibility: inapplicable — no agent delegation; doctor imports installed packages as checks.
- Selection predicate: Shared note enumeration/link parsing, resolved edges, concept classification and metadata date cutoff; environment/module availability, cache-directory existence, pairwise index-file presence and version predicates.
- Invalidation or expiry: Reports are snapshots; rerun after filesystem/environment/date changes. No note content is invalidated.
- Activation or effect: Code emits warning/failure and exit status; these can advise a person or be consumed by a watchdog. Actual repairs or watchdog behavior uninspected.
- Evidence limits: Threshold verdicts do not warrant truth of note assertions, model integrity or successful end-to-end recall; doctor does not deserialize/check index contents.

> stale = sorted(s for s, d in dated if d < cutoff)
> if concepts:
>     stale_pct = round(100.0 * len(stale) / len(concepts), 1)
>     stale_v = 'warn' if stale_pct > th['stale_warn'] else 'ok'
> --- `src/sqlite_graph_memory/vault_stats.py`

> worst = max(RANK[m['verdict']] for m in metrics)
> return {'notes_dir': str(notes_dir), 'pages': n, 'metrics': metrics,
>         'verdict': ['ok', 'warn', 'fail'][worst], 'exit_code': worst}
> --- `src/sqlite_graph_memory/vault_stats.py`

> if not any((d / folder).exists() for d in _hf_cache_dirs()):
>     missing.append(name)
> --- `src/sqlite_graph_memory/doctor.py`

> text, fails = render(run_checks())
> print(text)
> return 1 if fails else 0
> --- `src/sqlite_graph_memory/doctor.py`

The contrasting cases bound authority: an undated concept is excluded from the stale numerator but included in its denominator; an existing model-cache folder passes its presence check without proving complete weights; two existing index files pass presence checking without proving compatible rows. These are limits on target/domain, not absent evaluators.

### Claims

#### EPI-CLM-search-layer
Label: Read-only associative recall

Source-native claim is context retrieval over notes, rather than independent answer production. Closest supplied claim [RT-CLM-scoped-return](runtime.md#rt-clm-scoped-return) concerns transport isolation; this is the distinct functional/warrant boundary. SRC-1, `README.md`, doctrine/design; implemented comparison uses [RT-RTE-mcp-recall](runtime.md#rt-rte-mcp-recall).

> It fits [Andrej Karpathy's LLM Wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) (April 2026), where an agent maintains an interlinked markdown wiki and a search tool over the pages is the first helper he suggests adding: sgm is that search layer, read-only, and it follows your `[[wikilinks]]` as a graph. Independent project, not affiliated with or endorsed by him.
> --- `README.md`

Read-only concerns source notes on recall, not all package side effects. The index and ledger retain content and telemetry. No claim that graph association validates note truth is established by this search-layer statement.

#### EPI-CLM-measurement-scope
Label: Measurement and reproducible evidence

Claims concern what evaluation can establish, what shared functions reproduce, and private reported performance. Distinct from [RT-CLM-temporal-scope](runtime.md#rt-clm-temporal-scope), whose target is temporal reliance. SRC-1, `README.md`, doctrine/design and reported operation. No new execution evidence is asserted here.

> `run_eval.py` imports `brain_ask.py` and calls the same functions the agent calls —
> `load_index`, `retrieve_candidates`, `expand_1hop`, `rerank_candidates` — so what you measure
> is what runs. An eval that re-implements the pipeline measures the re-implementation.
> --- `README.md`

> Wikilink gold is weak supervision: a linked neighbour is not always the note that answers the
> question. `bridge` is built *from* links, so any method that walks links is flattered there —
> it measures "can the pipeline follow a connection", not "is this the right connection".
> --- `README.md`

> Be clear about what that reproduces: the bridge
> numbers above came from the maintainer's home vault and home pipeline on 2026-09-16, and they
> have not been re-run from the published package.
> --- `README.md`

Shared functions support algorithm reuse, not equivalent composition. A countercase is the supplied runtime's entity-policy divergence and the benchmark's mandatory reranking/extractive answering. Private figures are attributed operation, not authenticated observed/causal evidence for this package. The README itself explicitly restricts the license of its gold and private figures; the report retains those restrictions rather than treating evaluation as universally invalid.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
