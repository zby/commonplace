---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "How Labyrinth Exploration checks research candidates, grants reliance and exposes unchecked project state"
run-id: AAS-2026-11-23-labyrinth-exploration-4000731242d4-01
reviewed-boundary: "019a93da59313e697dc6f28bcfe1588a376c7565"
---

# Labyrinth Exploration epistemic report

## Source-and-claim boundary

Does this research skill turn conjectures, imported findings and computed outputs into checked claims that guide future work? The boundary is the shipped skill, engine, example and evaluation tooling, not the surrounding model host or a particular research deployment. See the [Source register](boundary.md#source-register). Claims: see [RT-CLM-map-progress](runtime.md#rt-clm-map-progress), [EPI-CLM-independent-evidence](#epi-clm-independent-evidence), [EPI-CLM-resolved-frontier](#epi-clm-resolved-frontier) and [EPI-CLM-traceable-notes](#epi-clm-traceable-notes). The README and tutorial assertions are separate: [EPI-CLM-tier-facts](#epi-clm-tier-facts), [EPI-CLM-session-change](#epi-clm-session-change), [EPI-CLM-checked-before-use](#epi-clm-checked-before-use), [EPI-CLM-conjecture-test-check](#epi-clm-conjecture-test-check).

No model transcripts, example referee reports, observed CLI/browser/test runs or controlled comparisons are supplied. The SRC-1 example artifacts show stored candidate/status instances, not their actual production or acceptance. Campaign anecdotes are reported operation, not linked review traces or component comparisons. Host delivery/grants, project-specific proof tools, literature access, cluster runs and publication checks are unobserved; this prevents judging actual independence, scientific correctness of private files, coverage at scale and hosting status. See [RT-CMP-host-models](runtime.md#rt-cmp-host-models): no in-skill parameter update; exact versions, endpoint mutability, provider state/encoding and any truth-apt content in it are not determinable. Explanatory and presentation assets, license and historical releases are excluded per boundary.

| Operation | SRC-1 source path | Coverage and limit |
| --- | --- | --- |
| Explicit/implicit skill; host tools and hooks | `agents/openai.yaml`, `references/codex.md`, `SKILL.md` | Direct metadata/dispatch instructions and frozen tree inspection: host shell, web, agents/follow-up by availability; no shipped hook or tool registration found in the entry configuration/tree (no MCP required). See [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration); no host registry or hook behavior inferred. |
| Conjecture, literature/side projects, review, withdrawal, copy rebuild | `references/loop.md`, `templates/briefs/referee.md`, `templates/briefs/writer.md`, `references/campaigns.md` | Direct; see [EPI-RTE-referee-check](#epi-rte-referee-check), [EPI-RTE-verdict-dispose](#epi-rte-verdict-dispose), [EPI-RTE-writer-check](#epi-rte-writer-check). Side projects read-only import by doctrine; formalization is an optional rigor anchor, not a shipped prover. |
| Unknowns readout; review of external submissions | `examples/prompts.md` | Direct design: report unknown bands, doors and clearly marked hunches without a required map edit; separately, save imported reports and seek independent review without requiring a new attack. See [EPI-RTE-verdict-dispose](#epi-rte-verdict-dispose). No observed host run. |
| Compute and saturation | `references/compute.md`, `SKILL.md`, `references/saturation.md` | Direct compute/skill instructions and supplied runtime escalation trace; see [EPI-RTE-compute-check](#epi-rte-compute-check), [EPI-RTE-resume-select](#epi-rte-resume-select). No access to deployed jobs. |
| CLI help/unknown, event, check, build, status, project blueprint | `templates/lab.py` | Direct dispatcher: help prints doc/0; unknown prints doc/2, neither loads project. See [EPI-RTE-event-keep](#epi-rte-event-keep), [EPI-RTE-schema-check](#epi-rte-schema-check), [EPI-RTE-frontier-project](#epi-rte-frontier-project), [EPI-RTE-status-project](#epi-rte-status-project), [EPI-RTE-blueprint-label](#epi-rte-blueprint-label). |
| Browser view and optional outputs | `templates/dashboard.html`, `templates/lab.py` | Direct board and table filters/consumers; graph/scatter/history wiring located, individual view math not fully audited (no browser-complete classification verdict). See [EPI-RTE-browser-select](#epi-rte-browser-select), [EPI-RTE-table-project](#epi-rte-table-project). |
| Initial and exhaustive example | `examples/triangle-counts/make_example.py`, `examples/triangle-counts/exhaustive_n8.py`, `docs/tutorial.md` | Direct producers and selected tutorial/fixture anchors; see [EPI-RTE-example-compute](#epi-rte-example-compute), [EPI-RTE-example-write](#epi-rte-example-write). No supplied memberwise comparator output. |
| Package/CI, native discovery and live recipes | `tests/test_lab.py`, `tests/test_skill.py`, `tests/test_codex.py`, `tools/codex_smoke.py`, `.github/workflows/tests.yml`, `docs/codex-testing.md` | Direct assertion/discovery trace, including [EPI-RTE-json-assertions](#epi-rte-json-assertions) for standalone dashboard JSON; live artifact comparison is prescribed separately in `docs/codex-testing.md`. Supplied runtime CI/maintenance account [RT-RTE-maintainer-update](runtime.md#rt-rte-maintainer-update). No deployed release or isolated live recipe results. |

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-claims](#epi-obj-claims) | Proofs, computed results and precisely scoped predictions | see [EPI-OBJ-claims](#epi-obj-claims) | SRC-1 `references/loop.md` | A label supplies no proof. |
| [EPI-OBJ-reports](#epi-obj-reports) | Candidate claims, literature leads and itemized criticisms | see [EPI-OBJ-reports](#epi-obj-reports) | SRC-1 `references/campaigns.md` | No example referee report is bundled. |
| [EPI-OBJ-source-family](#epi-obj-source-family) | Imported statements and findings about named example families | see [EPI-OBJ-source-family](#epi-obj-source-family) | SRC-1 `references/loop.md` | Retention does not record admission; no actual literature nodes or check trace supplied for this route. |
| [EPI-OBJ-review](#epi-obj-review) | Claims about check provenance and eligibility | see [EPI-OBJ-review](#epi-obj-review) | SRC-1 `SKILL.md` | Review label can be supplied directly. |
| [EPI-OBJ-frontier](#epi-obj-frontier) | Existence or impossibility at a size/value and conditional claims | see [EPI-OBJ-frontier](#epi-obj-frontier) | SRC-1 `templates/lab.py` | A reason string need not resolve to a proof or witness. |
| [EPI-OBJ-sota](#epi-obj-sota) | Current and previous scoped best-results statements | see [EPI-OBJ-sota](#epi-obj-sota) | SRC-1 `templates/lab.py` | History is not state restoration. |
| [EPI-OBJ-events](#epi-obj-events) | Assertions about project actions/outcomes | see [EPI-OBJ-events](#epi-obj-events) | SRC-1 `templates/lab.py` | Append does not authenticate provenance. |
| [EPI-OBJ-views](#epi-obj-views) | Claims about recorded data, including counts and sorted/filtered displays | see [EPI-OBJ-views](#epi-obj-views) | SRC-1 `templates/lab.py` | View can be stale, selective or contradictory. |
| [EPI-OBJ-status](#epi-obj-status) | Frontier totals, selected graph entries and recent event statements | see [EPI-OBJ-status](#epi-obj-status) | SRC-1 `templates/lab.py` | Selected excerpt, not the full board or review log. |
| [EPI-OBJ-book-status](#epi-obj-book-status) | The status report with a different heading | see [EPI-OBJ-book-status](#epi-obj-book-status) | SRC-1 `templates/lab.py` | No shipped universal document consumer. |
| [EPI-OBJ-sota-tex](#epi-obj-sota-tex) | Current results, statuses and proof/citation references; no earlier rows | see [EPI-OBJ-sota-tex](#epi-obj-sota-tex) | SRC-1 `templates/lab.py` | Optional TeX result/class overrides; no check of their semantic equivalence. |
| [EPI-OBJ-sota-md](#epi-obj-sota-md) | Current results, statuses, references, update date and earlier result text | see [EPI-OBJ-sota-md](#epi-obj-sota-md) | SRC-1 `templates/lab.py` | History is copied text, not rollback. |
| [EPI-OBJ-dashboard-data](#epi-obj-dashboard-data) | Serialized graph, parseable events, frontier projection, scatter/history, SoTA and summary | see [EPI-OBJ-dashboard-data](#epi-obj-dashboard-data) | SRC-1 `templates/lab.py` | Shipped example assertions consume selected fields; no research-session reader is established. |
| [MEM-OBJ-dashboard-snapshot](memory.md#mem-obj-dashboard-snapshot) | Frozen build payload available to browser rendering | see [MEM-OBJ-dashboard-snapshot](memory.md#mem-obj-dashboard-snapshot) | SRC-1 `templates/dashboard.html` | Board and SoTA show selected material; no live reload of sources. |
| [EPI-OBJ-briefs](#epi-obj-briefs) | Premises, failed routes, lessons and directives | see [EPI-OBJ-briefs](#epi-obj-briefs) | SRC-1 `SKILL.md` | Actual delivered context and reliance are unobserved. |

## Authority-route ledger

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority | Behavioral-authority path | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-literature-import](#epi-rte-literature-import) | content transformation | doctrine only | [EPI-OBJ-reports](#epi-obj-reports) | truth-apt transformation: acquisition/import | Outside statements and research leads | Literature agent reports exact statements/numbers and possible ideas | During exploration | Candidate source claim or flagged unchecked lead | Policy only | Unknown on entry; paraphrase may lose scope until checked | Forward a lead without treating it as established | Attacker via lead/brief, advisory for exploration | SRC-1 `references/loop.md`, `references/codex.md` | none | none | No retrieved original or delivered lead supplied. |
| [EPI-RTE-source-check](#epi-rte-source-check) | check/evidence production | doctrine only | [EPI-OBJ-reports](#epi-obj-reports) → [EPI-OBJ-source-family](#epi-obj-source-family) | no content change | Imported statement and proposed scope of use | Coordinator consults original, comparing wording and quantifiers, including connectedness and size bounds | Before reliance, when original accessible | Matching scoped statement, mismatch, or check outstanding | Coordinator policy | Evidence about what source states and whether its scope fits, not independent proof of the source | Return narrowed/supported statement or grounds to withhold | Coordinator via original and lead, advisory evidence for the intended use | SRC-1 `references/loop.md` | none | none | No actual source access or completed check supplied. |
| [EPI-RTE-source-retain](#epi-rte-source-retain) | retention | doctrine only | [EPI-OBJ-reports](#epi-obj-reports) → [EPI-OBJ-source-family](#epi-obj-source-family) | no content change | Useful source or family finding | Coordinator selects useful results for graph and marks unverified claims; storage does not require recorded clearance | During exploration; independent of admission | Project source/family node or lead left outside graph | Coordinator policy | Stored wording and attribution alone confer no warrant | Later map and graph consumers can retrieve candidate, and board shows families | Later coordinator or reader via graph and projection, advisory across sessions | SRC-1 `references/loop.md` | none | none | No evidence that check state is automatically propagated or enforced. |
| [EPI-RTE-source-rely](#epi-rte-source-rely) | disposition/acceptance | doctrine only | [EPI-OBJ-reports](#epi-obj-reports) → [EPI-OBJ-source-family](#epi-obj-source-family) | no content change | Use an imported assertion as a research premise | Coordinator requires original-source check with matching quantifiers; missing check leaves the intended reliance pending | Before using as a premise, not before all search or exploratory forwarding | Use within source scope, narrow, withhold or keep pending | Coordinator policy | At most the original source's warrant within checked scope; no automatic validation of attribution or transfer | Can use as a scoped input to proof or computation; unchecked leads may still guide exploration as such | Coordinator via source comparison and pending status, procedural before intended use | SRC-1 `references/loop.md`, `references/codex.md` | none | none | No per-claim executable gate or supplied acceptance decision. |
| [EPI-RTE-predict-test](#epi-rte-predict-test) | content transformation | doctrine only | [EPI-OBJ-claims](#epi-obj-claims) | truth-apt transformation: ampliative conjecture | From earlier-size data to a prediction about the next size | Coordinator/attack role; earlier sizes alone do not entail next-size occurrence | Before test | Testable claim, or a non-claim hunch retained separately | Instruction | None from novelty or fit | Proposed claim sets test target | Attacker via brief and graph, advisory per iteration | SRC-1 `references/loop.md` | [RT-CLM-map-progress](runtime.md#rt-clm-map-progress) | none | No general claim about arbitrary model outputs; not determinable without their text and premises |
| [EPI-RTE-referee-check](#epi-rte-referee-check) | check/evidence production | doctrine only | [EPI-OBJ-reports](#epi-obj-reports) | no content change | Quantifiers/hypotheses/steps of named proof or per-member counts at specified sizes | Independent agent or co-author; own reasoning/code, exact reference or disclosed sample; coordinator separately spot checks | On candidate before established use; early theorem review possible | ESTABLISHED, ESTABLISHED WITH CORRECTIONS, GAP, FALSE with reasons and replacements | Evidence to coordinator, not canonical write | Named item and checked domain; sample agreement only over compared cases | Enables coordinator to correct, withhold or seek more evidence | Coordinator via verdict and spot check, advisory evidence with policy consequences | SRC-1 `templates/briefs/referee.md` | [EPI-CLM-independent-evidence](#epi-clm-independent-evidence) | none | No implementation of independent reasoning supplied |
| [EPI-RTE-verdict-dispose](#epi-rte-verdict-dispose) | disposition/acceptance | doctrine only | [EPI-OBJ-review](#epi-obj-review) | no content change | License to cite result as established | Coordinator consumes independent verdict, applies corrections, adds own spot check; proof/certificate tier criterion is separate | After review before established use | Accept corrected result, withhold GAP, reject FALSE or leave pending | Coordinator policy, bypassable | Corrected statement in checked scope only; citation remains subject to [EPI-RTE-tier-citation](#epi-rte-tier-citation) | Canonical result eligibility, not blanket factual citation; pending data can persist | Coordinator through verdict/notes policy, permissive or withholding across sessions | SRC-1 `SKILL.md` | [EPI-CLM-independent-evidence](#epi-clm-independent-evidence) | none | Illustrative writer does not consume these checks |
| [EPI-RTE-tier-citation](#epi-rte-tier-citation) | operational admission/selection/consumption | doctrine only | [EPI-OBJ-claims](#epi-obj-claims) and [EPI-OBJ-review](#epi-obj-review) | no content change | Use of a result or lead in notes, proofs or research planning | Coordinator or writer applies tier and review state under the schema's citation rule; not a proof evaluator | At citation or use, independently of insertion | Fact, qualified result, finite fact, evidence, conjecture or direction | Coordinator policy, not enforced by engine | T1 literature/standard fact within source scope; T2 local result with non-peer-review caveat and review state; T3 certified finite fact only at stated sizes, disclosing pending same-size replay where applicable; T4 evidence only; T5 conjecture; T6 direction only, never a proof premise | Cite in allowed form and scope, qualify or withhold; a positive verdict does not raise the tier | Coordinator and writers via tier/review metadata and schema, procedural at each citation; readers receive resulting scope and caveats | SRC-1 `references/schema.md`, `SKILL.md` | [EPI-CLM-tier-facts](#epi-clm-tier-facts) | scope mismatch | README groups T1–T3 as facts; passing metadata checks does not authorize the citation. |
| [EPI-RTE-canonical-integrate](#epi-rte-canonical-integrate) | lifecycle integration | doctrine only | [EPI-OBJ-claims](#epi-obj-claims) | no content change | Connect accepted evidence/result into proof, graph and best-result state | Coordinator edits; writer drafts on a copy, no status upgrades | After acceptance; re-anchor competing edits, revert unsupported drift | Corrected proof and links, replaced best row retained in previous; updated documents | Coordinator policy | Preserves intended accepted scope only if edits match verdict | Next sessions and briefs can cite integrated result | Coordinator and readers via canonical map/write-ups, advisory across sessions | SRC-1 `references/campaigns.md` | [EPI-CLM-independent-evidence](#epi-clm-independent-evidence) | none | No transaction; independent project writes can drift |
| [EPI-RTE-refutation-record](#epi-rte-refutation-record) | retention | doctrine only | [EPI-OBJ-claims](#epi-obj-claims) | no content change | Counterexample, rejected formulation and lesson | Coordinator links refuting evidence; GAP does not itself prove falsity | After refutation | Dead end and lesson, with successor considered separately | Policy | Counterexample disproves a universal only within its admissible scope | Retains evidence without licensing the rejected statement | Later attackers via board and brief, advisory across sessions | SRC-1 `references/loop.md` | [EPI-CLM-independent-evidence](#epi-clm-independent-evidence) | none | No automatic invalidation of all dependent artifacts |
| [EPI-RTE-resume-select](#epi-rte-resume-select) | behavior/policy adaptation | doctrine only | [EPI-OBJ-briefs](#epi-obj-briefs) | non-truth-apt policy/content update: choose next experiment and allocation | Question selection and escalation | Coordinator ranks by cheap map-changing steps; stall triggers different method/scale | Start, stall or recovery after restart | New question, agent roles or compute plan; inspect live status before replacement | Policy | Live job state and saved report serve different purposes; neither is review | Changes next tasks and selected worker context | Coordinator and delegated agents via status/map/journal and explicit brief, advisory over sessions | SRC-1 `SKILL.md` | [RT-CLM-map-progress](runtime.md#rt-clm-map-progress) | none | No trace of task choice or improved capacity |
| [EPI-RTE-writer-check](#epi-rte-writer-check) | check/evidence production | doctrine only | [EPI-OBJ-claims](#epi-obj-claims) | no content change | Proposed edits and derived documents, not theorem truth | Writer compiles copy; coordinator compares draft to verdict, tests uniqueness and references | Before canonical insertion; one block at a time | Errors/ambiguity block or require re-anchor; compile success not semantic approval | Procedural; proposed exact-token guard | Document/anchor consistency and human/model fidelity check, not independent proof | Copy discarded; unsupported text reverted; change canonical source only after review | Coordinator via build diagnostics and verdict, policy per draft | SRC-1 `references/campaigns.md` | [EPI-CLM-independent-evidence](#epi-clm-independent-evidence) | none | No shipped document-builder for arbitrary project proofs |
| [EPI-RTE-compute-check](#epi-rte-compute-check) | check/evidence production | doctrine only | [EPI-OBJ-frontier](#epi-obj-frontier) | no content change | Coverage and numeric agreement of computations | Project check script accounts for chunks and totals; independent earlier-size implementation checks code; missing chunks resubmitted | Before scale increase and on collection | Coverage or missing work; pending same-size replay | Policy | Coverage is not semantic correctness; earlier agreement does not establish current instance | Coordinator may retry or withhold; archive cleanup requires checking membership first | Coordinator via project checks, policy per run | SRC-1 `references/compute.md` | [EPI-CLM-independent-evidence](#epi-clm-independent-evidence) | none | No project verifier or remote environment pinned |
| [EPI-RTE-example-compute](#epi-rte-example-compute) | check/evidence production | implemented | [EPI-OBJ-frontier](#epi-obj-frontier) | truth-apt transformation: entailed derivation | Triangle counts among labeled simple undirected graphs | Enumerate edge masks and subsets, add induced neighbor edges to base triangles; initial generator exhausts n=3–7, samples base graphs at n=8 plus named witnesses | Example generation or later exhaustive run | Exact sets on exhaustive domain; sampled presence only; true top-band bound from missing edge | Computed sets feed projection or optional writer | Conditional on faithful encoding and arithmetic; no inference that a sampled omission is impossible | Prints sets/counts and supplies next stage, no verdict gate | Example writers via computed values, enforcing in that run | SRC-1 `examples/triangle-counts/exhaustive_n8.py` | none | none | Neither run nor independent referee observed; initial generator shares one-vertex reasoning |
| [EPI-RTE-example-write](#epi-rte-example-write) | operational admission/selection/consumption | implemented | [EPI-OBJ-review](#epi-obj-review) | no content change | Permission to persist example update | Caller chooses --write; code only guards existing exhaustive k.n8 before writes, not reviewer verdict or agreement with statement | After enumeration, then sequential writes | Computed values plus fixed review/answer text; previous result saved | Enforcing on script path only | No license for referee claim or fixed sentence from persistence | Rewrites frontier, graph and table; skips later retry once exhaustive tag present | Engine reads JSON on later calls, enforcing selection by file contents | SRC-1 `examples/triangle-counts/exhaustive_n8.py` | none | scope mismatch | Partial update needs manual reconciliation; fixed provenance is illustrative |
| [EPI-RTE-event-keep](#epi-rte-event-keep) | retention | implemented | [EPI-OBJ-events](#epi-obj-events) | no content change | Admit event log record | Caller supplies summary and references; engine enforces option shape/recognized type only | Event dispatch without log reload | Append timestamped object or reject argument/type | Enforcing on CLI, not direct file edits | A record of what caller asserted; no reference warrant | Events visible to engine and recovery readers | Build/status via JSONL, coordinator via log, until edited | SRC-1 `templates/lab.py` | none | none | No automatic links from verdict events to node acceptance |
| [EPI-RTE-event-reload](#epi-rte-event-reload) | lineage/freshness/recovery | implemented | [EPI-OBJ-events](#epi-obj-events) | no content change | Decodable object lines | JSON loader discards blanks, invalid JSON and non-objects | Check, build or status calls the loader; event dispatch does not | Diagnostics list only when caller supplies it; otherwise silent skip | Enforcing selection on read; no deletion | Current projection can omit source lines | Check can fail while view silently omits malformed records | Check and build/status via surviving objects, current read only | SRC-1 `templates/lab.py` | none | none | A parseable object can still misstate an outcome |
| [EPI-RTE-blueprint-label](#epi-rte-blueprint-label) | content transformation | implemented | [EPI-OBJ-claims](#epi-obj-claims) | truth-apt transformation: acquisition/import | Imported project statement and use links | N imported as project code when present; map provenance to tier, fill defaults and apply overrides | Check/status/build before checks | Statements, dependencies and default or overridden metadata | Enforcing merged representation | Unknown original warrant; default established/T2 does not preserve any known check provenance | Adds nodes to inputs of checker and projection | Engine via project Python and JSON overrides on each load | SRC-1 `templates/lab.py` | none | scope mismatch | No supplied project module; its particular statements and side effects not determinable |
| [EPI-RTE-schema-check](#epi-rte-schema-check) | check/evidence production | implemented | [EPI-OBJ-review](#epi-obj-review) | no content change | Selected shape/metadata of merged nodes, event references, tier/review/test and SoTA fields | check() checks enumerations, named review where claimed, references on links/events and selected field presence; test required only for open curated conjectures | Explicit check, parseable input | Diagnostic list or ok | Returns evidence to dispatcher; no writes | Only checked predicates; no requirement that established nodes have verdicts, no cross-check of SoTA against frontier | Nonempty diagnostics can stop an explicitly chained close | CLI via list and subsequent exit status, current call | SRC-1 `templates/lab.py` | [EPI-CLM-conjecture-test-check](#epi-clm-conjecture-test-check) | scope mismatch | No full schema or scientific check; malformed inputs can raise |
| [EPI-RTE-conflict-check](#epi-rte-conflict-check) | check/evidence production | implemented | [EPI-OBJ-frontier](#epi-obj-frontier) | truth-apt transformation: entailed derivation | Intersection of asserted realized and impossible claims | Snap intersection to lo/step grid; no upper hi clamp in conflict function | Explicit check | At least one grid-aligned overlap diagnostic per conflicting realized claim | Evidence to check dispatcher | In-row overlap demonstrates contradictory statuses if fixed meaning; outside row may also be reported | Diagnostic can prevent chained build; neither side repaired | CLI check via diagnostics, current call | SRC-1 `templates/lab.py` | [EPI-CLM-resolved-frontier](#epi-clm-resolved-frontier) | scope mismatch | Not a scientific evaluator; lower/grid bound is not full range |
| [EPI-RTE-check-exit](#epi-rte-check-exit) | operational admission/selection/consumption | implemented | [EPI-OBJ-views](#epi-obj-views) | no content change | Whether to continue a checked close | Shell observes CLI success/failure only if caller chains commands | After check returns diagnostics | Exit 1 for nonempty list, 0 otherwise; standalone build bypasses | Enforcing only for chained shell invocation | No result acceptance or snapshot guarantee | Can block next command; no withdrawal of older views | Caller/shell via status code, one invocation | SRC-1 `templates/lab.py` | [EPI-CLM-resolved-frontier](#epi-clm-resolved-frontier) | none | Files can change between commands |
| [EPI-RTE-frontier-project](#epi-rte-frontier-project) | content transformation | implemented | [EPI-OBJ-status](#epi-obj-status) and [MEM-OBJ-dashboard-snapshot](memory.md#mem-obj-dashboard-snapshot) | truth-apt transformation: entailed derivation | Displayed resolution of loaded frontier row | Grid clip, precedence and counting in frontier(); merge runs and keep first reason or bin dense rows for display | Build or status; positive step/required row keys | Counts/fraction and best known from winning labels | Enforces display selection | Warrant is about representation of supplied labels, not truth of those labels | Lower priority labels disappear from rendered classification; no canonical repair | Coordinator and browser via report/dashboard, advisory until refreshed | SRC-1 `templates/lab.py` | [EPI-CLM-resolved-frontier](#epi-clm-resolved-frontier) | scope mismatch | A conflicting realized claim wins over impossible; reasons can be compressed |
| [EPI-RTE-status-project](#epi-rte-status-project) | content transformation | implemented | [EPI-OBJ-status](#epi-obj-status) | truth-apt transformation: non-ampliative reshaping | Frontier table, listed node kinds, under-review subset and recent event summaries | status_md lists by kind (including answered questions under Open doors), selects literal under-review state, takes last 25 log entries in load order | status prints, build writes | A selective excerpt independent of checker | Enforcing in view | Absence from under-review list does not demonstrate independent review | Status is prescribed as next-session entry, not authoritative provenance | Coordinator via stdout or generated Markdown, advisory | SRC-1 `templates/lab.py` | [EPI-CLM-resolved-frontier](#epi-clm-resolved-frontier) | none | Status is not a full review or event ledger |
| [EPI-RTE-browser-select](#epi-rte-browser-select) | operational admission/selection/consumption | implemented | [MEM-OBJ-dashboard-snapshot](memory.md#mem-obj-dashboard-snapshot) | no content change | Which statements and statuses show in browser | Embedded DATA; board filters kind/status, SoTA groups rows and infers color from kind/status | On HTML page load; later tab switches expose already-populated board/SoTA | Answered door excluded from open list; missing recognized status can fall to proved color | Enforcing rendering selection only | A visual category is not proof | Routes readers toward displayed evidence; existing HTML may lag source | Browser reads retained HTML DATA; rendered board/SoTA advise readers for this page instance | SRC-1 `templates/dashboard.html` | [EPI-CLM-resolved-frontier](#epi-clm-resolved-frontier) | scope mismatch | No back-write or evidence-gated display |
| [EPI-RTE-table-project](#epi-rte-table-project) | content transformation | implemented | [EPI-OBJ-sota](#epi-obj-sota) → [EPI-OBJ-sota-tex](#epi-obj-sota-tex); [EPI-OBJ-sota-md](#epi-obj-sota-md) | truth-apt transformation: indeterminate | Dated best rows and prior results | sota_build groups and formats known groups; optional LaTeX/Markdown paths off by default | Build, with table present and outputs configured | Projection; Markdown preserves selected text, LaTeX fidelity of optional overrides is unknown | Enforcing formatting | No adjudication of proof/reference validity or ranking of results | Generated tables can carry unchecked states into notes/book | Readers via generated table, advisory until rebuilt | SRC-1 `templates/lab.py` | [EPI-CLM-resolved-frontier](#epi-clm-resolved-frontier) | none | Operator must bring frontier/table into agreement |
| [EPI-RTE-book-status](#epi-rte-book-status) | content transformation | implemented | [EPI-OBJ-book-status](#epi-obj-book-status) | truth-apt transformation: non-ampliative reshaping | Book status copy | Build with BOOK_STATUS configured, after writing STATUS.md | During build | Status body with a replacement heading written to configured path | Enforces file projection only | No stronger warrant than selected input fields | Project document build or reader via configured Markdown file; advisory until regenerated and reread | Project document build or reader via configured Markdown file; advisory until regenerated and reread | SRC-1 `templates/lab.py` | none | none | No included project document consumer or actual inclusion supplied. |
| [EPI-RTE-sota-tex](#epi-rte-sota-tex) | content transformation | implemented | [EPI-OBJ-sota-tex](#epi-obj-sota-tex) | truth-apt transformation: indeterminate | SoTA LaTeX output | sota.json present and SOTA_TEX configured; rows belong to configured groups | During build | Current results and references only; can use cls_tex and result_tex overrides | Enforces file projection only | No stronger warrant than selected input fields | Notes/book reader via configured LaTeX inclusion, if wired by the project; advisory until regenerated and rebuilt | Notes/book reader via configured LaTeX inclusion, if wired by the project; advisory until regenerated and rebuilt | SRC-1 `templates/lab.py` | none | none | No history column or check of TeX override fidelity; no observed document inclusion. |
| [EPI-RTE-sota-md](#epi-rte-sota-md) | content transformation | implemented | [EPI-OBJ-sota-md](#epi-obj-sota-md) | truth-apt transformation: non-ampliative reshaping | SoTA Markdown output | sota.json present and SOTA_MD configured; rows belong to configured groups | During build | Current rows, references, dates and previous results in a Markdown table | Enforces file projection only | No stronger warrant than selected input fields | Markdown reader via generated table; advisory until regenerated and reopened | Markdown reader via generated table; advisory until regenerated and reopened | SRC-1 `templates/lab.py` | none | none | Copies statuses and history text without evaluating either. |
| [EPI-RTE-dashboard-json](#epi-rte-dashboard-json) | retention | implemented | [EPI-OBJ-dashboard-data](#epi-obj-dashboard-data) | no content change | Persist build data for file readers | Build serializes projection directly to data.json | Before HTML handling | JSON file replaced | Enforces serialization only | No stronger warrant than selected input fields | Supplies saved projection to shipped example assertions | Example tests reopen the JSON after build; see [EPI-RTE-json-assertions](#epi-rte-json-assertions); browser reads HTML instead | SRC-1 `templates/lab.py`, `tests/test_lab.py` | none | none | Research-session read-back uninspected. |
| [EPI-RTE-snapshot-write](#epi-rte-snapshot-write) | retention | implemented | [MEM-OBJ-dashboard-snapshot](memory.md#mem-obj-dashboard-snapshot) | no content change | Persist build data in HTML | Template presence controls writing; marker controls inlining | After writing dashboard JSON | HTML with embedded DATA if marker matches | Enforces file projection only | No stronger warrant than selected input fields | Later browser can render this saved snapshot | Browser via embedded DATA on a subsequent page load; advisory to reader | SRC-1 `templates/lab.py` | none | none | No check prerequisite; skipped write can leave old HTML, and markerless HTML need not contain new data. |
| [EPI-RTE-json-assertions](#epi-rte-json-assertions) | check/evidence production | implemented | [EPI-OBJ-dashboard-data](#epi-obj-dashboard-data) | no content change | Selected fields of the freshly built example projection before and after the size-eight update | Unit tests decode the standalone file and compare frontier/counts and selected node/summary fields to expected values | After build in the shipped example tests | Assertion success or failure | Enforcing pass/fail within the suite, advisory for maintenance decisions | Fixture-specific projection agreement only, not scientific or browser validation | Can fail the software test; no research admission effect | Test runner via decoded JSON and assertions for one test; results inform maintainer | SRC-1 `tests/test_lab.py` | none | none | No executed result supplied; live graph/frontier/table agreement is a separate prescribed check. |
| [EPI-RTE-software-check](#epi-rte-software-check) | check/evidence production | implemented | [EPI-OBJ-views](#epi-obj-views) | no content change | Shipped software behavior and discovery shape, not project research | Test fixtures compare classifier to brute reference and tutorial to expected outputs; discovery tests metadata and skills/list match | Maintainer or CI test run; optional native smoke | Assertions or smoke report/exit | Testing, not release gate proven | Only asserted cases on actual successful run; none supplied | Can inform human release judgment; no scientific admission effect | Maintainer via test output, advisory per change | SRC-1 `tools/codex_smoke.py` | none | none | Live workflow recipes are not run evidence |

**Checked-input deductions (implementation, not target runs).** In SRC-1 `templates/lab.py`, take a row with lo=0, hi=4, step=2, realized entries 2 and 6, and impossible singleton intervals at 2 and 6. `frontier_conflicts` finds grid-aligned overlaps at both 2 and 6 because it does not use hi. `classify` clips 6, gives 2 to realized by priority, then counts one realized and two unknown: resolution 1/3, even if no successful check preceded build. The only license is about labels and arithmetic. The runtime's admissible-overlap example holds, but it is not a complete characterization of the check. Also, a well-formed SoTA row with a valid group but unrecognized status and no kind passes the inspected field checks: `kindOf` in SRC-1 `templates/dashboard.html` assigns the proved color while leaving the literal status visible. Neither projection changes the source.

At size eight, the initial script's phrase “not realized” means absent from its sampled and named-witness set, not impossibility. In the later script, a base triangle on vertices 0, 1, 2 has t=1; joining the eighth vertex to 0 and 1 adds one triangle because their edge is counted by the subset mask. Exhausting masks and subsets covers every labeled simple graph in this domain. The complement is numerical evidence for missing counts, conditional on the encoding and implementation. The later writer does not compare the set to a stored prediction: the fixed answer text and named referee are separate from that deduction. The expected missing-count list in SRC-1 `tests/test_lab.py` is a test oracle for that software case, not an independent review transcript. See [RT-RTE-example-update](runtime.md#rt-rte-example-update), [EPI-RTE-example-compute](#epi-rte-example-compute) and [EPI-RTE-example-write](#epi-rte-example-write) (SRC-1 `examples/triangle-counts/make_example.py`, `examples/triangle-counts/exhaustive_n8.py`).

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-map-progress](runtime.md#rt-clm-map-progress) | Map changes count as progress | SRC-1 `SKILL.md` design | see [EPI-RTE-refutation-record](#epi-rte-refutation-record) | [EPI-RTE-example-compute](#epi-rte-example-compute) | None supplied | No comparison | Protocol retains failed routes as inputs to later choice | No outcome guarantee |
| [EPI-CLM-independent-evidence](#epi-clm-independent-evidence) | Map with independent review | SRC-1 `agents/openai.yaml` design | see [EPI-RTE-referee-check](#epi-rte-referee-check) and [EPI-RTE-verdict-dispose](#epi-rte-verdict-dispose) | [EPI-RTE-example-write](#epi-rte-example-write) bypasses; [EPI-RTE-schema-check](#epi-rte-schema-check) checks labels only | None supplied; SRC-1 `references/campaigns.md` reports corrections | No independent variation of review or verification scope | Specified coordinator policy, not enforced invariant | Fixture status can falsely imply performed review if read at face value |
| [EPI-CLM-resolved-frontier](#epi-clm-resolved-frontier) | Compute resolved fraction and report realized/impossible overlap | SRC-1 `SKILL.md` design | see [EPI-RTE-conflict-check](#epi-rte-conflict-check) | [EPI-RTE-conflict-check](#epi-rte-conflict-check) and [EPI-RTE-frontier-project](#epi-rte-frontier-project) | None supplied | Deterministic input deduction, not scientific validation | Implemented summaries of input claims; explicit check detects described in-row conflict | No guarantee build was checked or fraction reflects known truth; check may also report overlap beyond hi |
| [EPI-CLM-traceable-notes](#epi-clm-traceable-notes) | Trace each claim in notes to its work and check | SRC-1 `SKILL.md` design | see [EPI-RTE-canonical-integrate](#epi-rte-canonical-integrate) | [EPI-RTE-event-keep](#epi-rte-event-keep) and [EPI-RTE-schema-check](#epi-rte-schema-check) do not verify evidence paths or proof lineage | None supplied | No sampled project note lineage | Procedural links via saved evidence and corrected documents are supported by design | Direct edits and example metadata can omit actual supporting artifacts |
| [EPI-CLM-session-change](#epi-clm-session-change) | Each session starts from the map and changes it | SRC-1 `README.md` doctrine/design | [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration) prescribes change for research iterations; SRC-1 `examples/prompts.md` also prescribes a readout with no required edit | No end-of-session mutation gate on inspected paths; status reads and prints | None supplied | No session series or counterfactual | An iteration can change the map, including by recording refutations; not every entry point requires mutation | Universal claim unsupported; the unknowns readout need not write and build can refresh a projection without changing the research claims |
| [EPI-CLM-checked-before-use](#epi-clm-checked-before-use) | Nothing used before checked; agent/external-model results independently refereed before notes | SRC-1 `README.md` doctrine/design; `references/campaigns.md` reported operation | [EPI-RTE-verdict-dispose](#epi-rte-verdict-dispose) covers established use, not all uses; unchecked leads may guide exploration, useful results can be retained as candidates, and campaign data/events can be committed under review | [EPI-RTE-example-write](#epi-rte-example-write) can write established/refereed labels without reading a verdict; [EPI-RTE-schema-check](#epi-rte-schema-check) does not enforce review before use | None supplied; campaign account reports no false theorem entered one programme's notes and recounts a false-as-stated lemma caught before the final report | No linked independent verdicts, complete outcome audit, comparison or isolated referee effect | Coordinator protocol for established agent/external results, including corrections and spot check; separate scoped original-source check for imported premises | Headline overstates scope; pending data and advisory leads are usable without clearance; fixture metadata is illustrative, not observed checking |
| [EPI-CLM-conjecture-test-check](#epi-clm-conjecture-test-check) | check confirms every conjecture has a test | SRC-1 `docs/tutorial.md` doctrine/design | A stated test is part of formulating a conjecture; SRC-1 `references/schema.md` narrows the engine contract to open curated conjectures | [EPI-RTE-schema-check](#epi-rte-schema-check) requires a truthy test only for open curated conjectures | None supplied | Source deduction only, not a quality assessment of test texts | An open curated T5 node without test is diagnosed; a well-formed modified curated or open blueprint T5 node without test is not diagnosed by that predicate | Universal scope overstates the check; it does not judge suitability of the test |
| [EPI-CLM-tier-facts](#epi-clm-tier-facts) | README caption groups T1–T3 as citable facts; T4 as evidence and T5–T6 as speculation | SRC-1 `README.md` doctrine/design | [EPI-RTE-tier-citation](#epi-rte-tier-citation): schema distinguishes caveated T2 and bounded T3; `SKILL.md` excludes hunches from proofs and separates review from tier | [EPI-RTE-schema-check](#epi-rte-schema-check) checks labels and selected field constraints, not proof, validation provenance or citation use; [EPI-RTE-example-write](#epi-rte-example-write) sets illustrative labels without a verdict | None supplied | No comparison or proof-use audit | Citation policy is narrower than the caption: T1 literature/standard fact within source scope; T2 local result with non-peer-review caveat and review state; T3 certified finite fact only at stated sizes, disclosing pending same-size replay where applicable; T4 evidence only; T5 conjecture; T6 direction only, never a proof premise | Positive review can affect admission as established but does not upgrade a tier or grant unqualified factual use. |

## Bounded conclusion

- **Acquisition and candidate production.** Imported leads have unknown warrant on arrival ([EPI-RTE-literature-import](#epi-rte-literature-import)). A coordinator is instructed to mark unchecked leads and can retain useful findings as source/family nodes ([EPI-RTE-source-retain](#epi-rte-source-retain)). Before reliance as a premise, compare the exact claim and its quantifiers with the original ([EPI-RTE-source-check](#epi-rte-source-check)); narrow the intended use to that scope or leave an unavailable check pending ([EPI-RTE-source-rely](#epi-rte-source-rely)). This can preserve source warrant if performed, not establish a new result or independently verify the original proof. No such check or grant of reliance is observed; blueprint warrant is separately unknown. Verbatim reports preserve candidate wording, not the truth of assertions. An earlier-size pattern can motivate a genuinely ampliative conjecture, not entail the next-size prediction ([EPI-RTE-predict-test](#epi-rte-predict-test)); opaque outputs without supplied inputs and text are not determinable.
- **Checking and admission.** [EPI-RTE-referee-check](#epi-rte-referee-check) and [EPI-RTE-verdict-dispose](#epi-rte-verdict-dispose) specify an evidence-consuming decision for intended use as an established result: analyze proof steps or independently recompute the scoped result, apply corrections and add a spot check. Sample agreement and earlier-size validation license less than independent same-size verification. GAP withholds establishment, FALSE can lead to counterexample/lesson retention, and [EPI-RTE-canonical-integrate](#epi-rte-canonical-integrate) ties eligible results into later notes/map/briefs. None establishes that a particular candidate was accepted. The executable example separately derives a finite result, then can place a label and fixed claim without such acceptance. Even after favorable review, citation follows a separate policy: T1 literature/standard fact within source scope; T2 local result with non-peer-review caveat and review state; T3 certified finite fact only at stated sizes, disclosing pending same-size replay where applicable; T4 evidence only; T5 conjecture; T6 direction only, never a proof premise. A stored `established` label and a clean metadata check establish neither that the checks occurred nor that a particular citation was warranted. See [EPI-RTE-tier-citation](#epi-rte-tier-citation).
- **Operative software results.** A check can stop a caller's chained build, not ban a standalone build or withdraw stale projections ([EPI-RTE-check-exit](#epi-rte-check-exit)). The projections derive summaries from recorded input, filter and regroup it, and enable later advisory use, not scientific warrant. Unchecked labels, unresolved conflicts and stale projections can influence which proofs or experiments readers choose. On resumption, the coordinator gets the selected status excerpt; the browser reads the retained HTML snapshot on page load, not `dashboard/data.json`. Shipped example tests reopen the standalone JSON after build and check selected projections against fixed expectations; this is implemented read-back for software evaluation, separate from prescribed live artifact comparison and uninspected research-session JSON use. Configured book status copies that excerpt with a new heading. Optional SoTA Markdown carries earlier rows, while LaTeX omits them and can substitute project-supplied TeX text. These outputs carry advisory claims to different readers, not acceptance. An old result in `previous` and archived evidence support human diagnosis, not an atomic rollback.
- **Limits of the public claims.** The readout shows why map change is not required for every session; the tutorial's checker checks test presence only for open curated conjectures. The reported campaign correction and claimed clean notes do not establish reliable review, component benefit or compliance outside that account. The README's check-before-use heading does not describe pending data, exploratory leads or the shipped fixture write. See [EPI-CLM-session-change](#epi-clm-session-change), [EPI-CLM-checked-before-use](#epi-clm-checked-before-use), [EPI-CLM-conjecture-test-check](#epi-clm-conjecture-test-check).
- **Later decisions.** [EPI-RTE-resume-select](#epi-rte-resume-select) changes task selection, budget or tool use by procedure, even without a new accepted claim. See [RT-RTE-review-integration](runtime.md#rt-rte-review-integration) for the conjecture theory conditions and [RT-RTE-maintainer-update](runtime.md#rt-rte-maintainer-update) for human changes to shipped guidance. Neither persistence nor a reported correction establishes improved future capacity. Reflection on the live method, autonomous criticism across the whole loop and exercised self-improvement are independently unestablished: no trace connects changes in the method to represented operational evidence and onward to dependent later operation. Revising mathematical claims is not itself revision of the installed method.

## Shared records

### Operative objects

#### EPI-OBJ-claims
Label: Claims

Proofs, computed results and precisely scoped predictions. Natural-language statements and proofs in notes and graph text on disk; questions without assertions and expressly non-claim hunches guide investigation instead. SRC-1 `references/loop.md`. A label supplies no proof. No runtime operative-object counterpart; see related route [RT-RTE-review-integration](runtime.md#rt-rte-review-integration).

#### EPI-OBJ-reports
Label: Reports

Candidate claims, literature leads and itemized criticisms. Natural-language reports and correction requests, with code/data in per-agent filesystem directories; a saved report and the corresponding verdict are distinct inputs. SRC-1 `references/campaigns.md`. No example referee report is bundled. No runtime operative-object counterpart; see related route [RT-RTE-review-integration](runtime.md#rt-rte-review-integration).

#### EPI-OBJ-review
Label: Review

Claims about check provenance and eligibility. Symbolic review state and tier used by code plus names and verdict prose, in graph JSON; distinct from the checked text and the actual check. SRC-1 `SKILL.md`. Review label can be supplied directly. No runtime operative-object counterpart; see related route [RT-RTE-review-integration](runtime.md#rt-rte-review-integration).

#### EPI-OBJ-frontier
Label: Frontier

Existence or impossibility at a size/value and conditional claims. Symbolic status and interval fields with prose reasons in frontier JSON; scatter JSON adds numerical observations, not weights or embeddings. SRC-1 `templates/lab.py`. A reason string need not resolve to a proof or witness. No runtime operative-object counterpart; see related route [RT-RTE-build-views](runtime.md#rt-rte-build-views).

#### EPI-OBJ-sota
Label: Sota

Current and previous scoped best-results statements. Natural-language result and provenance strings with symbolic row/group identifiers in sota JSON. SRC-1 `templates/lab.py`. History is not state restoration. No runtime operative-object counterpart; see related route [RT-RTE-build-views](runtime.md#rt-rte-build-views).

#### EPI-OBJ-events
Label: Events

Assertions about project actions/outcomes. Natural-language summaries and evidence strings with symbolic type, timestamp and identifiers in JSONL. SRC-1 `templates/lab.py`. Append does not authenticate provenance. No runtime operative-object counterpart; see related route [RT-RTE-event-append](runtime.md#rt-rte-event-append).

#### EPI-OBJ-views
Label: Views

Claims about recorded data, including counts and sorted/filtered displays. Symbolic aggregates and projected strings in status Markdown, dashboard JSON/HTML and optional tables. SRC-1 `templates/lab.py`. View can be stale, selective or contradictory. No runtime operative-object counterpart; see related route [RT-RTE-build-views](runtime.md#rt-rte-build-views).

#### EPI-OBJ-briefs
Label: Briefs

Premises, failed routes, lessons and directives. Natural-language brief, journal, plan and project-memory files with path references; selected inputs conveyed through host. SRC-1 `SKILL.md`. Actual delivered context and reliance are unobserved. No runtime operative-object counterpart; see related route [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration).

#### EPI-OBJ-status
Label: Status report

Part of: [EPI-OBJ-views](#epi-obj-views)

Frontier totals, selected graph entries and recent event statements. Symbolic fields and natural-language text, represented as `status` stdout and build's `STATUS.md`. Consumer: Coordinator on resumption; fresh CLI invocation recomputes from source. Selected excerpt, not the full board or review log. SRC-1 `templates/lab.py`; configuration contract in SRC-1 `references/schema.md`. Distinct from canonical inputs and from the browser-consumed embedded payload [MEM-OBJ-dashboard-snapshot](memory.md#mem-obj-dashboard-snapshot); see [RT-RTE-build-views](runtime.md#rt-rte-build-views) for CLI ownership.

#### EPI-OBJ-book-status
Label: Book status export

Part of: [EPI-OBJ-views](#epi-obj-views)

The status report with a different heading. Symbolic fields and natural-language text, represented as Markdown at configured `BOOK_STATUS` path. Consumer: Book/document reader or build if project includes the path. No shipped universal document consumer. SRC-1 `templates/lab.py`; configuration contract in SRC-1 `references/schema.md`. Distinct from canonical inputs and from the browser-consumed embedded payload [MEM-OBJ-dashboard-snapshot](memory.md#mem-obj-dashboard-snapshot); see [RT-RTE-build-views](runtime.md#rt-rte-build-views) for CLI ownership.

#### EPI-OBJ-sota-tex
Label: LaTeX SoTA export

Part of: [EPI-OBJ-views](#epi-obj-views)

Current results, statuses and proof/citation references; no earlier rows. Symbolic fields and natural-language text, represented as LaTeX longtable at configured `SOTA_TEX` path. Consumer: Notes/book through project inclusion. Optional TeX result/class overrides; no check of their semantic equivalence. SRC-1 `templates/lab.py`; configuration contract in SRC-1 `references/schema.md`. Distinct from canonical inputs and from the browser-consumed embedded payload [MEM-OBJ-dashboard-snapshot](memory.md#mem-obj-dashboard-snapshot); see [RT-RTE-build-views](runtime.md#rt-rte-build-views) for CLI ownership.

#### EPI-OBJ-sota-md
Label: Markdown SoTA export

Part of: [EPI-OBJ-views](#epi-obj-views)

Current results, statuses, references, update date and earlier result text. Symbolic fields and natural-language text, represented as Markdown at configured `SOTA_MD` path. Consumer: Markdown table readers or a project document. History is copied text, not rollback. SRC-1 `templates/lab.py`; configuration contract in SRC-1 `references/schema.md`. Distinct from canonical inputs and from the browser-consumed embedded payload [MEM-OBJ-dashboard-snapshot](memory.md#mem-obj-dashboard-snapshot); see [RT-RTE-build-views](runtime.md#rt-rte-build-views) for CLI ownership.

#### EPI-OBJ-dashboard-data
Label: Dashboard JSON export

Part of: [MEM-OBJ-dashboard-snapshot](memory.md#mem-obj-dashboard-snapshot)

Serialized graph, parseable events, frontier projection, scatter/history, SoTA and summary. Symbolic fields and natural-language text, represented as `dashboard/data.json` on disk. Consumer: Shipped example tests reopen and decode this file after build and assert selected frontier, node and summary fields (SRC-1 `tests/test_lab.py`; see [EPI-RTE-json-assertions](#epi-rte-json-assertions)). The live artifact comparison is prescribed separately (SRC-1 `docs/codex-testing.md`). No research-session JSON consumer is established. SRC-1 `templates/lab.py`; configuration contract in SRC-1 `references/schema.md`. This standalone representation also falls within the broader local views inventory, [EPI-OBJ-views](#epi-obj-views), but is not the embedded HTML representation of its memory parent. See [RT-RTE-build-views](runtime.md#rt-rte-build-views) for CLI ownership.

#### EPI-OBJ-source-family
Label: Source and family nodes

Part of: [MEM-OBJ-knowledge-nodes](memory.md#mem-obj-knowledge-nodes)

Imported research results selected for durable storage as `source` or `family` entries in the project graph. The symbolic node kind and ID carry natural-language statements with source scope; these are not the initial agent leads or the proof-tier review labels. The engine merges curated nodes for builds; the dashboard's board selects family entries and the graph can display nodes. SRC-1 `references/loop.md`, `templates/lab.py`, `templates/dashboard.html`. Distinct from report text in [EPI-OBJ-reports](#epi-obj-reports); no runtime object counterpart, see [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration) for the enclosing loop.

### Routes

#### EPI-RTE-literature-import
Label: literature import

Part of: [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration)

Literature agents bring in external statements, numbers and leads. The coordinator can forward a lead as unverified before checking. Warrant at acquisition is unknown; the source comparison, retention and intended use are separate transitions: [EPI-RTE-source-check](#epi-rte-source-check), [EPI-RTE-source-retain](#epi-rte-source-retain), [EPI-RTE-source-rely](#epi-rte-source-rely). SRC-1 `references/loop.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Imported candidate wording or an unverified lead.
- Later read-back: inapplicable — this is intake; later graph retention is traced in [EPI-RTE-source-retain](#epi-rte-source-retain).
- Delegated visibility: Attackers via lead/brief, advisory for task
- Selection predicate: Literature search directed by community-specific prompts; report exact statements, numbers and usable ideas.
- Invalidation or expiry: inapplicable — no separate expiry or persistent rejection mechanism on this transition
- Activation or effect: Attackers via lead/brief, advisory for task. Policy only.
- Evidence limits: No supplied literature retrieval trace.

>   claims as such. Store the useful results as `source` and `family` nodes. Check every
>   claim you will use at the source, quantifiers included ("connected", "for all sizes",
>   "for n ≤ N").
> --- `references/loop.md`

#### EPI-RTE-source-check
Label: Check claims at the source

Part of: [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration)

Imported statement and proposed scope of use. Coordinator consults original, comparing wording and quantifiers, including connectedness and size bounds. Evidence about what source states and whether its scope fits, not independent proof of the source. SRC-1 `references/loop.md`. Distinct from [EPI-RTE-literature-import](#epi-rte-literature-import) and from the independent referee's judgment on a new result in [EPI-RTE-referee-check](#epi-rte-referee-check). The original is a reference for the imported proposition, not an oracle for the new research claim.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Matching scoped statement, mismatch, or check outstanding.
- Later read-back: inapplicable — this decision does not itself persist a separate check result; graph retention is traced separately.
- Delegated visibility: Unchecked leads may be forwarded as such; the check does not grant workers write authority.
- Selection predicate: Coordinator consults original, comparing wording and quantifiers, including connectedness and size bounds. Before reliance, when original accessible.
- Invalidation or expiry: Withhold or narrow reliance on a missing check or scope mismatch; correct reliance if source is misread.
- Activation or effect: Return narrowed/supported statement or grounds to withhold. Coordinator via original and lead, advisory evidence for the intended use.
- Evidence limits: No actual source access or completed check supplied.

>   claims as such. Store the useful results as `source` and `family` nodes. Check every
>   claim you will use at the source, quantifiers included ("connected", "for all sizes",
>   "for n ≤ N").
> --- `references/loop.md`

#### EPI-RTE-source-retain
Label: Retain useful source results

Part of: [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration)

Useful source or family finding. Coordinator selects useful results for graph and marks unverified claims; storage does not require recorded clearance. Stored wording and attribution alone confer no warrant. SRC-1 `references/loop.md`. Distinct from [EPI-RTE-literature-import](#epi-rte-literature-import) and from the independent referee's judgment on a new result in [EPI-RTE-referee-check](#epi-rte-referee-check). A marked candidate can remain in the map without acceptance.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Project source/family node or lead left outside graph.
- Later read-back: Later coordinator can reuse retained project graph entries; browser users can consult merged nodes and see family cards after a build.
- Delegated visibility: A later brief may select graph material; graph retention is not automatic delivery.
- Selection predicate: Coordinator selects useful results for graph and marks unverified claims; storage does not require recorded clearance. During exploration; independent of admission.
- Invalidation or expiry: Coordinator may correct labels or graph text and rebuild; no automated expiry specified.
- Activation or effect: Later map and graph consumers can retrieve candidate, and board shows families. Later coordinator or reader via graph and projection, advisory across sessions.
- Evidence limits: No evidence that check state is automatically propagated or enforced.

>   claims as such. Store the useful results as `source` and `family` nodes. Check every
> --- `references/loop.md`

#### EPI-RTE-source-rely
Label: Grant scoped reliance on imported claims

Part of: [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration)

Use an imported assertion as a research premise. Coordinator requires original-source check with matching quantifiers; missing check leaves the intended reliance pending. At most the original source's warrant within checked scope; no automatic validation of attribution or transfer. SRC-1 `references/loop.md`, `references/codex.md`. Distinct from [EPI-RTE-literature-import](#epi-rte-literature-import) and from the independent referee's judgment on a new result in [EPI-RTE-referee-check](#epi-rte-referee-check). No general answer oracle; the original text is the reference for attribution and scope. The coordinator can withhold or narrow; humans may provide sources without thereby clearing a claim. If access or the needed check is missing, record it as outstanding, not clearance. A mismatch does not require deleting a flagged lead.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Use within source scope, narrow, withhold or keep pending.
- Later read-back: inapplicable — this decision does not itself persist a separate check result; graph retention is traced separately.
- Delegated visibility: Unchecked leads may be forwarded as such; the check does not grant workers write authority.
- Selection predicate: Coordinator requires original-source check with matching quantifiers; missing check leaves the intended reliance pending. Before using as a premise, not before all search or exploratory forwarding.
- Invalidation or expiry: Withhold or narrow reliance on a missing check or scope mismatch; correct reliance if source is misread.
- Activation or effect: Can use as a scoped input to proof or computation; unchecked leads may still guide exploration as such. Coordinator via source comparison and pending status, procedural before intended use.
- Evidence limits: No per-claim executable gate or supplied acceptance decision.

> commit when that is within scope. Report frontier changes and any outstanding review,
> source, compute or hosting steps separately.
> --- `references/codex.md`

#### EPI-RTE-predict-test
Label: predict test

Part of: [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration)

From earlier-size data to a prediction about the next size. Coordinator/attack role; earlier sizes alone do not entail next-size occurrence. Before test. Proposed claim sets test target. Scope: None from novelty or fit. SRC-1 `references/loop.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Testable claim, or a non-claim hunch retained separately.
- Later read-back: inapplicable — the transition itself supplies no retained state to a later invocation; any separate retention is traced apart
- Delegated visibility: Attacker via brief and graph, advisory per iteration
- Selection predicate: Coordinator/attack role; earlier sizes alone do not entail next-size occurrence.
- Invalidation or expiry: inapplicable — no separate expiry or persistent rejection mechanism on this transition
- Activation or effect: Attacker via brief and graph, advisory per iteration. Instruction.
- Evidence limits: No general claim about arbitrary model outputs; not determinable without their text and premises.

> - Prefer predictions for the next size, where they can fail.
> --- `references/loop.md`

#### EPI-RTE-referee-check
Label: referee check

Part of: [RT-RTE-review-integration](runtime.md#rt-rte-review-integration)

Quantifiers/hypotheses/steps of named proof or per-member counts at specified sizes. Independent agent or co-author; own reasoning/code, exact reference or disclosed sample; coordinator separately spot checks. On candidate before established use; early theorem review possible. Enables coordinator to correct, withhold or seek more evidence. Scope: Named item and checked domain; sample agreement only over compared cases. SRC-1 `templates/briefs/referee.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: ESTABLISHED, ESTABLISHED WITH CORRECTIONS, GAP, FALSE with reasons and replacements.
- Later read-back: inapplicable — the transition itself supplies no retained state to a later invocation; any separate retention is traced apart
- Delegated visibility: Coordinator via verdict and spot check, advisory evidence with policy consequences
- Selection predicate: Independent agent or co-author; own reasoning/code, exact reference or disclosed sample; coordinator separately spot checks.
- Invalidation or expiry: inapplicable — no separate expiry or persistent rejection mechanism on this transition
- Activation or effect: Coordinator via verdict and spot check, advisory evidence with policy consequences. Evidence to coordinator, not canonical write.
- Evidence limits: No implementation of independent reasoning supplied.

> 3. `<a computation>`: reimplement it independently and recompute the counts **member by
>    member** for `<sizes>`. If the largest size is too expensive, compare a random sample of at
>    least `<k>` members with the agent's per-member output, and say so.
> --- `templates/briefs/referee.md`

#### EPI-RTE-verdict-dispose
Label: verdict dispose

Part of: [RT-RTE-review-integration](runtime.md#rt-rte-review-integration)

License to cite result as established. Coordinator consumes independent verdict, applies corrections, adds own spot check; proof/certificate tier criterion is separate. After review before established use. Canonical result eligibility; pending data can persist. Scope: Only corrected statement within proof or numerical scope; validated prior-size code does not imply new-size replay. This permits established entry under the review policy; tier independently governs how the result can be cited. A positive verdict changes review state, not tier, and neither it nor `established` metadata licenses unqualified factual use. See [EPI-RTE-tier-citation](#epi-rte-tier-citation). SRC-1 `SKILL.md`, `references/schema.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Accept corrected result, withhold GAP, reject FALSE or leave pending.
- Later read-back: inapplicable — the transition itself supplies no retained state to a later invocation; any separate retention is traced apart
- Delegated visibility: inapplicable — coordinator or project-file consumers own this transition, see related runtime route
- Selection predicate: Coordinator consumes independent verdict, applies corrections, adds own spot check; proof/certificate tier criterion is separate.
- Invalidation or expiry: Withhold pending, correct or withdraw on contrary evidence; retain reasons.
- Activation or effect: Coordinator through verdict/notes policy, permissive or withholding across sessions. Coordinator policy, bypassable.
- Evidence limits: Illustrative writer does not consume these checks.

> - **Referee before consuming.** Results from agents or external models enter the notes,
>   the state-of-the-art table or the graph as established only after an independent
>   referee and your own spot check. Apply the referee's corrections; noting them is not
>   enough.
> --- `SKILL.md`

#### EPI-RTE-tier-citation
Label: Tier-based citation

Part of: [RT-RTE-review-integration](runtime.md#rt-rte-review-integration)

Distinct from [EPI-RTE-verdict-dispose](#epi-rte-verdict-dispose): the coordinator or writer applies citation rules when using material in notes or proofs, not when judging a candidate or marking it established. T1 literature/standard fact within source scope; T2 local result with non-peer-review caveat and review state; T3 certified finite fact only at stated sizes, disclosing pending same-size replay where applicable; T4 evidence only; T5 conjecture; T6 direction only, never a proof premise. Review can require corrections or withhold established entry; it does not promote the tier. Reclassify when the underlying basis changes (for example, publication for a programme result moving to T1), not merely after a referee pass. SRC-1 `references/schema.md`, `SKILL.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Scoped citation or statement identified as evidence or conjecture; a hunch can guide investigation but not appear in a proof.
- Later read-back: Later readers can see the resulting wording and caveats if recorded in notes; no separately persisted citation decision is specified.
- Delegated visibility: Writers receive corrected results and are expected to preserve their tier and limits; delivery and compliance are unobserved.
- Selection predicate: A use in notes or proof must fit the tier, scientific scope, and applicable review discipline; exploration may use weaker material as such.
- Invalidation or expiry: Correct or withhold use beyond that scope; reevaluate when the evidential basis changes.
- Activation or effect: Policy guides coordinator and writer at citation time. The checker does not inspect proofs or enforce caveats, finite domain or exclusion of hunches from proofs.
- Evidence limits: Design only. No observed citation or checker result supplied.

> | T1 | proved in the literature (published, peer reviewed) or standard | fact |
> | T2 | proved here, not peer reviewed | result, with the caveat and the review state |
> | T3 | exhaustive computation with certified code, validated against an independent implementation | fact for the stated sizes |
> | T4 | computational evidence | evidence only |
> | T5 | conjecture with a stated test | conjecture |
> | T6 | hunch, explicitly not a claim | a direction only |
> --- `references/schema.md`

> Referees change the review state, not the tier. A result of the programme becomes T1 only
> once it is published.
> --- `references/schema.md`

> - **Tier discipline.** Nothing below T3 is cited as a fact. A T6 hunch never appears in a
>   theorem's proof. Write "conjecture" and "evidence" in prose.
> --- `SKILL.md`

#### EPI-RTE-canonical-integrate
Label: canonical integrate

Part of: [RT-RTE-review-integration](runtime.md#rt-rte-review-integration)

Connect accepted evidence/result into proof, graph and best-result state. Coordinator edits; writer drafts on a copy, no status upgrades. After acceptance; re-anchor competing edits, revert unsupported drift. Next sessions and briefs can cite integrated result. Scope: Preserves intended accepted scope only if edits match verdict. SRC-1 `references/campaigns.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Corrected proof and links, replaced best row retained in previous; updated documents.
- Later read-back: Coordinator and readers via canonical map/write-ups, advisory across sessions.
- Delegated visibility: inapplicable — coordinator or project-file consumers own this transition, see related runtime route
- Selection predicate: Coordinator edits; writer drafts on a copy, no status upgrades.
- Invalidation or expiry: Revert drift and rebuild; retain prior best row, not a rollback snapshot.
- Activation or effect: Coordinator and readers via canonical map/write-ups, advisory across sessions. Coordinator policy.
- Evidence limits: No transaction; independent project writes can drift.

> 1. **Read every draft against the referee's verdicts.** Writers drift. One weakened a
>    conjecture from "and" to "or" with no support, and the change was reverted. Check that
>    every label and cross-reference exists and points where the text says.
> --- `references/campaigns.md`

#### EPI-RTE-refutation-record
Label: refutation record

Part of: [RT-RTE-review-integration](runtime.md#rt-rte-review-integration)

Counterexample, rejected formulation and lesson. Coordinator links refuting evidence; GAP does not itself prove falsity. After refutation. Retains evidence without licensing the rejected statement. Scope: Counterexample disproves a universal only within its admissible scope. SRC-1 `references/loop.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Dead end and lesson, with successor considered separately.
- Later read-back: Later attackers via board and brief, advisory across sessions.
- Delegated visibility: inapplicable — coordinator or project-file consumers own this transition, see related runtime route
- Selection predicate: Coordinator links refuting evidence; GAP does not itself prove falsity.
- Invalidation or expiry: Withdraw reliance, not the lesson or counterexample.
- Activation or effect: Later attackers via board and brief, advisory across sessions. Policy.
- Evidence limits: No automatic invalidation of all dependent artifacts.

> - **Refuted:** add a `deadend` node with the counterexample and a `lesson`, and link it
>   (`refutes`) from what refutes it. Then write the modified statement and test it.
> --- `references/loop.md`

#### EPI-RTE-resume-select
Label: resume select

Part of: [RT-RTE-research-iteration](runtime.md#rt-rte-research-iteration)

Question selection and escalation. Coordinator ranks by cheap map-changing steps; stall triggers different method/scale. Start, stall or recovery after restart. Changes next tasks and selected worker context. Scope: Live job state and saved report serve different purposes; neither is review. SRC-1 `SKILL.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: New question, agent roles or compute plan; inspect live status before replacement.
- Later read-back: Coordinator and delegated agents via status/map/journal and explicit brief, advisory over sessions.
- Delegated visibility: Coordinator and delegated agents via status/map/journal and explicit brief, advisory over sessions
- Selection predicate: Coordinator ranks by cheap map-changing steps; stall triggers different method/scale.
- Invalidation or expiry: inapplicable — no separate expiry or persistent rejection mechanism on this transition
- Activation or effect: Coordinator and delegated agents via status/map/journal and explicit brief, advisory over sessions. Policy.
- Evidence limits: No trace of task choice or improved capacity.

>    doors or conjectures. Prefer items where a single computation or proof step would move
>    the map.
> --- `SKILL.md`

#### EPI-RTE-writer-check
Label: writer check

Part of: [RT-RTE-review-integration](runtime.md#rt-rte-review-integration)

Proposed edits and derived documents, not theorem truth. Writer compiles copy; coordinator compares draft to verdict, tests uniqueness and references. Before canonical insertion; one block at a time. Copy discarded; unsupported text reverted; change canonical source only after review. Scope: Document/anchor consistency and human/model fidelity check, not independent proof. SRC-1 `references/campaigns.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Errors/ambiguity block or require re-anchor; compile success not semantic approval.
- Later read-back: inapplicable — the transition itself supplies no retained state to a later invocation; any separate retention is traced apart
- Delegated visibility: Coordinator via build diagnostics and verdict, policy per draft
- Selection predicate: Writer compiles copy; coordinator compares draft to verdict, tests uniqueness and references.
- Invalidation or expiry: Discard test copy and re-anchor or revert unsupported edits.
- Activation or effect: Coordinator via build diagnostics and verdict, policy per draft. Procedural; proposed exact-token guard.
- Evidence limits: No shipped document-builder for arbitrary project proofs.

> - **Test on a copy** of the notes: insert, apply the edits, build twice. Require zero
>   errors, zero undefined references and zero overfull boxes, then delete the copy.
> --- `references/campaigns.md`

#### EPI-RTE-compute-check
Label: compute check

Part of: [RT-RTE-review-integration](runtime.md#rt-rte-review-integration)

Coverage and numeric agreement of computations. Project check script accounts for chunks and totals; independent earlier-size implementation checks code; missing chunks resubmitted. Before scale increase and on collection. Coordinator may retry or withhold; archive cleanup requires checking membership first. Scope: Coverage is not semantic correctness; earlier agreement does not establish current instance. SRC-1 `references/compute.md`.

- doctrine conclusion status: claimed
- operation conclusion status: uninspected
- Immediate return: Coverage or missing work; pending same-size replay.
- Later read-back: inapplicable — the transition itself supplies no retained state to a later invocation; any separate retention is traced apart
- Delegated visibility: Coordinator via project checks, policy per run
- Selection predicate: Project check script accounts for chunks and totals; independent earlier-size implementation checks code; missing chunks resubmitted.
- Invalidation or expiry: inapplicable — no separate expiry or persistent rejection mechanism on this transition
- Activation or effect: Coordinator via project checks, policy per run. Policy.
- Evidence limits: No project verifier or remote environment pinned.

> - **Write a check script** that verifies that every chunk is present, that the counts add
> --- `references/compute.md`

#### EPI-RTE-example-compute
Label: example compute

Part of: [RT-RTE-example-update](runtime.md#rt-rte-example-update)

Triangle counts among labeled simple undirected graphs. Enumerate edge masks and subsets, add induced neighbor edges to base triangles; initial generator exhausts n=3–7, samples base graphs at n=8 plus named witnesses. Example generation or later exhaustive run. Prints sets/counts and supplies next stage, no verdict gate. Scope: Conditional on faithful encoding and arithmetic; no inference that a sampled omission is impossible. SRC-1 `examples/triangle-counts/exhaustive_n8.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Exact sets on exhaustive domain; sampled presence only; true top-band bound from missing edge.
- Later read-back: inapplicable — the transition itself supplies no retained state to a later invocation; any separate retention is traced apart
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: Enumerate edge masks and subsets, add induced neighbor edges to base triangles; initial generator exhausts n=3–7, samples base graphs at n=8 plus named witnesses.
- Invalidation or expiry: inapplicable — no separate expiry or persistent rejection mechanism on this transition
- Activation or effect: Example writers via computed values, enforcing in that run. Computed sets feed projection or optional writer.
- Evidence limits: Neither run nor independent referee observed; initial generator shares one-vertex reasoning.

>     for S in range(1 << m):
>         mk = sum(1 << idx[(a, b)] for a, b in E if S >> a & 1 and S >> b & 1)
>         found[np.unique(t + popcount(g & np.uint32(mk)))] = True
> --- `examples/triangle-counts/exhaustive_n8.py`

#### EPI-RTE-example-write
Label: example write

Part of: [RT-RTE-example-update](runtime.md#rt-rte-example-update)

Permission to persist example update. Caller chooses --write; code only guards existing exhaustive k.n8 before writes, not reviewer verdict or agreement with statement. After enumeration, then sequential writes. Rewrites frontier, graph and table; skips later retry once exhaustive tag present. Scope: No license for referee claim or fixed sentence from persistence. SRC-1 `examples/triangle-counts/exhaustive_n8.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Computed values plus fixed review/answer text; previous result saved.
- Later read-back: Engine reads JSON on later calls, enforcing selection by file contents.
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: Caller chooses --write; code only guards existing exhaustive k.n8 before writes, not reviewer verdict or agreement with statement.
- Invalidation or expiry: Manual repair or restoration; the existing kind can block retry after partial write.
- Activation or effect: Engine reads JSON on later calls, enforcing selection by file contents. Enforcing on script path only.
- Evidence limits: Partial update needs manual reconciliation; fixed provenance is illustrative.

>     if any(n["id"] == "k.n8" and n.get("kind") == "exhaustive" for n in K["nodes"]):
>         print("already recorded: k.n8 is an exhaustive result; nothing changed")
>         return
> --- `examples/triangle-counts/exhaustive_n8.py`

#### EPI-RTE-event-keep
Label: event keep

Same transition as [RT-RTE-event-append](runtime.md#rt-rte-event-append), not a subroute: both describe the CLI's type-gated append. This retained ID records its epistemic role as trace retention, not a second admission mechanism.

Admit event log record. Caller supplies summary and references; engine enforces option shape/recognized type only. event dispatch. Events visible to engine and recovery readers. Scope: A record of what caller asserted; no reference warrant. SRC-1 `templates/lab.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Append timestamped object or reject argument/type.
- Later read-back: Build/status via JSONL, coordinator via log, until edited.
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: Caller supplies summary and references; engine enforces option shape/recognized type only.
- Invalidation or expiry: No expiry; the caller may edit the file separately.
- Activation or effect: Build/status via JSONL, coordinator via log, until edited. Enforcing on CLI, not direct file edits.
- Evidence limits: No automatic links from verdict events to node acceptance.

>     with open(LAB / "events.jsonl", "a") as fh:
>         fh.write(json.dumps(ev, ensure_ascii=False) + "\n")
> --- `templates/lab.py`

#### EPI-RTE-event-reload
Label: event reload

Part of: [RT-RTE-build-views](runtime.md#rt-rte-build-views)

This is the read stage under check, build or status, not part of [RT-RTE-event-append](runtime.md#rt-rte-event-append). Event dispatch writes without loading the log; a later read neither calls append nor requires a prior CLI append (the file can be edited directly).

Decodable object lines. JSON loader discards blanks, invalid JSON and non-objects. Every log load. Check can fail while view silently omits malformed records. Scope: Current projection can omit source lines. SRC-1 `templates/lab.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Diagnostics list only when caller supplies it; otherwise silent skip.
- Later read-back: Check and build/status via surviving objects, current read only.
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: JSON loader discards blanks, invalid JSON and non-objects.
- Invalidation or expiry: Read-time exclusion only, not deletion.
- Activation or effect: Check and build/status via surviving objects, current read only. Enforcing selection on read; no deletion.
- Evidence limits: A parseable object can still misstate an outcome.

>     """The event log; a malformed line is skipped (and reported to `problems` when given)."""
> --- `templates/lab.py`

#### EPI-RTE-blueprint-label
Label: blueprint label

Part of: [RT-RTE-blueprint-import](runtime.md#rt-rte-blueprint-import)

Imported project statement and use links. N imported as project code when present; map provenance to tier, fill defaults and apply overrides. Check/status/build before checks. Adds nodes to inputs of checker and projection. Scope: Unknown original warrant; default established/T2 does not preserve any known check provenance. SRC-1 `templates/lab.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Statements, dependencies and default or overridden metadata.
- Later read-back: Engine via project Python and JSON overrides on each load.
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: N imported as project code when present; map provenance to tier, fill defaults and apply overrides.
- Invalidation or expiry: Remove/revert module or overrides and reload.
- Activation or effect: Engine via project Python and JSON overrides on each load. Enforcing merged representation.
- Evidence limits: No supplied project module; its particular statements and side effects not determinable.

>             "status": o.get("status", "open" if kind == "conjecture" else "established"),
> --- `templates/lab.py`

#### EPI-RTE-schema-check
Label: schema check

Part of: [RT-RTE-build-views](runtime.md#rt-rte-build-views)

Selected shape/metadata of merged nodes, event references, tier/review/test and SoTA fields. check() checks enumerations, named review where claimed, references on links/events and selected field presence. The test predicate applies only to open curated conjectures and checks presence/truthiness, not quality. Explicit check, parseable input. Nonempty diagnostics can stop an explicitly chained close. Scope: Only checked predicates; no requirement that established nodes have verdicts, no cross-check of SoTA against frontier. For example, a well-formed curated T2 theorem marked established with no review field does not trigger the review predicate, and a refereed object with an allowed state and a nonempty `by` need not supply a real report or a verdict to pass it. The checker requires a recognized tier for scientific node kinds, a T6 tier for hunches and excludes T5/T6 for theorems, but does not check proofs, peer review, certified code or the way a result is cited. SRC-1 `templates/lab.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Diagnostic list or ok.
- Later read-back: inapplicable — the transition itself supplies no retained state to a later invocation; any separate retention is traced apart
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: check() checks enumerations, named review where claimed, references on links/events and selected field presence.
- Invalidation or expiry: inapplicable — no separate expiry or persistent rejection mechanism on this transition
- Activation or effect: CLI via list and subsequent exit status, current call. Returns evidence to dispatcher; no writes.
- Evidence limits: No full schema or scientific check; malformed inputs can raise.

>         if kind == "conjecture" and n.get("status") == "open" and not n.get("test") and n.get("source") == "labyrinth":
>             problems.append(f"{nid}: open conjecture without a stated test")
> --- `templates/lab.py`

>             elif rv["state"] in ("refereed", "human-checked") and not rv.get("by"):
>                 problems.append(f"{nid}: a refereed result names its referees (review.by)")
> --- `templates/lab.py`

#### EPI-RTE-conflict-check
Label: conflict check

Part of: [RT-RTE-build-views](runtime.md#rt-rte-build-views)

Intersection of asserted realized and impossible claims. Snap intersection to lo/step grid; no upper hi clamp in conflict function. Explicit check. Diagnostic can prevent chained build; neither side repaired. Scope: In-row overlap demonstrates contradictory statuses if fixed meaning; outside row may also be reported. SRC-1 `templates/lab.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: At least one grid-aligned overlap diagnostic per conflicting realized claim.
- Later read-back: inapplicable — the transition itself supplies no retained state to a later invocation; any separate retention is traced apart
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: Snap intersection to lo/step grid; no upper hi clamp in conflict function.
- Invalidation or expiry: inapplicable — no separate expiry or persistent rejection mechanism on this transition
- Activation or effect: CLI check via diagnostics, current call. Evidence to check dispatcher.
- Evidence limits: Not a scientific evaluator; lower/grid bound is not full range.

>                 x0, x1 = max(a, imp[k][0]), min(b, imp[k][1])
>                 first = lo + max(0, math.ceil((x0 - lo) / step)) * step   # first admissible value >= x0
>                 if first <= x1:
> --- `templates/lab.py`

#### EPI-RTE-check-exit
Label: check exit

Part of: [RT-RTE-build-views](runtime.md#rt-rte-build-views)

Whether to continue a checked close. Shell observes CLI success/failure only if caller chains commands. After check returns diagnostics. Can block next command; no withdrawal of older views. Scope: No result acceptance or snapshot guarantee. SRC-1 `templates/lab.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Exit 1 for nonempty list, 0 otherwise; standalone build bypasses.
- Later read-back: inapplicable — the transition itself supplies no retained state to a later invocation; any separate retention is traced apart
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: Shell observes CLI success/failure only if caller chains commands.
- Invalidation or expiry: inapplicable — no separate expiry or persistent rejection mechanism on this transition
- Activation or effect: Caller/shell via status code, one invocation. Enforcing only for chained shell invocation.
- Evidence limits: Files can change between commands.

>     elif cmd == "check":
>         p = check()
>         print("\n".join(p) if p else "ok")
>         return 1 if p else 0
> --- `templates/lab.py`

#### EPI-RTE-frontier-project
Label: frontier project

Part of: [RT-RTE-build-views](runtime.md#rt-rte-build-views)

Displayed resolution of loaded frontier row. Grid clip, precedence and counting in frontier(); merge runs and keep first reason or bin dense rows for display. Build or status; positive step/required row keys. Lower priority labels disappear from rendered classification; no canonical repair. Scope: Warrant is about representation of supplied labels, not truth of those labels. SRC-1 `templates/lab.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Counts/fraction and best known from winning labels.
- Later read-back: Coordinator and browser via report/dashboard, advisory until refreshed.
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: Grid clip, precedence and counting in frontier(); merge runs and keep first reason or bin dense rows for display.
- Invalidation or expiry: Rebuild to reflect changed inputs; a missing template can leave old HTML untouched.
- Activation or effect: Coordinator and browser via report/dashboard, advisory until refreshed. Enforces display selection.
- Evidence limits: A conflicting realized claim wins over impossible; reasons can be compressed.

>             "counts": dict(cnt), "resolved_fraction": (cnt["realized"] + cnt["impossible"]) / total if total else 1.0,
> --- `templates/lab.py`

#### EPI-RTE-status-project
Label: status project

Part of: [RT-RTE-build-views](runtime.md#rt-rte-build-views)

Frontier table, listed node kinds, review subset and recent event summaries. status_md lists by kind (including answered questions under Open doors), selects literal under-review state and takes last 25 log entries in load order. status prints, build writes. Status is prescribed as next-session entry, not authoritative provenance. Scope: Absence from under-review list does not demonstrate independent review. SRC-1 `templates/lab.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: A selective excerpt independent of checker.
- Later read-back: Coordinator via stdout or generated Markdown, advisory.
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: Listed node kinds regardless of status, literal under-review state for the review subset, and last 25 events in load order.
- Invalidation or expiry: Recompute on each status/build invocation; stored output can lag.
- Activation or effect: Coordinator via stdout or generated Markdown, advisory. Enforcing in view.
- Evidence limits: Status is not a full review or event ledger.

>     for e in events[-25:]:
> --- `templates/lab.py`

#### EPI-RTE-browser-select
Label: browser select

Part of: [MEM-RTE-snapshot-browse](memory.md#mem-rte-snapshot-browse)

Board and SoTA are populated from [MEM-OBJ-dashboard-snapshot](memory.md#mem-obj-dashboard-snapshot) during page initialization, downstream of [RT-RTE-build-views](runtime.md#rt-rte-build-views). Their tab controls show or hide already populated panels; they do not reload the snapshot or canonical files.

Which statements and statuses show in browser. Embedded DATA; board filters kind/status, SoTA groups rows and infers color from kind/status. On opening retained HTML; subsequent tab selection changes visibility only. Routes readers toward displayed evidence; existing HTML may lag source. Scope: A visual category is not proof. SRC-1 `templates/dashboard.html`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Answered door excluded from open list; missing recognized status can fall to proved color.
- Later read-back: A later browser page load consumes the build's embedded nodes and SoTA; toggling those panels within the loaded page does not read another retained snapshot.
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: Embedded DATA; board filters kind/status, SoTA groups rows and infers color from kind/status.
- Invalidation or expiry: Reopen a rebuilt snapshot; old page or exports need manual replacement.
- Activation or effect: Reader/coordinator via dashboard, advisory until rebuilt/reopened. Enforcing rendering selection only.
- Evidence limits: No back-write or evidence-gated display. Selective rendering is not complete exposure: the graph drops links to missing targets, and the timeline expects string timestamps, which JSONL object parsing does not ensure.

>   function drawBoard() {
>     const N = DATA.nodes;
> --- `templates/dashboard.html`

>   function drawSota() {
>     const SO = DATA.sota; if (!SO) return;
> --- `templates/dashboard.html`

>       : /partial|lower bound/.test(e.status) ? "partial" : /exhaustive|certified/.test(e.status) ? "exhaustive" : /computed/.test(e.status) ? "computed" : "proved";
> --- `templates/dashboard.html`

#### EPI-RTE-table-project
Label: table project

Part of: [RT-RTE-build-views](runtime.md#rt-rte-build-views)

Dated best rows and prior results. sota_build groups and formats known groups; optional LaTeX/Markdown paths off by default. Build, with table present and outputs configured. Generated tables can carry unchecked states into notes/book. The distinct export branches are [EPI-RTE-sota-md](#epi-rte-sota-md) and [EPI-RTE-sota-tex](#epi-rte-sota-tex). Scope: No adjudication of proof/reference validity or ranking of results. SRC-1 `templates/lab.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Projection; Markdown includes previous text; LaTeX layout lacks previous column.
- Later read-back: Readers via generated table, advisory until rebuilt.
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: sota_build groups and formats known groups; optional LaTeX/Markdown paths off by default.
- Invalidation or expiry: Rebuild after edits; no removal on disabled outputs.
- Activation or effect: Readers via generated table, advisory until rebuilt. Enforcing formatting.
- Evidence limits: Operator must bring frontier/table into agreement.

>                 prev = "; ".join(f"{p.get('date', '?')}: {p.get('was', '?')}" for p in e.get("previous", [])) or "–"
> --- `templates/lab.py`

#### EPI-RTE-software-check
Label: software check

Part of: [RT-RTE-maintainer-update](runtime.md#rt-rte-maintainer-update)

Shipped software behavior and discovery shape, not project research. Test fixtures compare classifier to brute reference and tutorial to expected outputs; discovery tests metadata and skills/list match. Maintainer or CI test run; optional native smoke. Can inform human release judgment; no scientific admission effect. Scope: Only asserted cases on actual successful run; none supplied. SRC-1 `tools/codex_smoke.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Assertions or smoke report/exit.
- Later read-back: inapplicable — the transition itself supplies no retained state to a later invocation; any separate retention is traced apart
- Delegated visibility: inapplicable — no software delegation on this route
- Selection predicate: Test fixtures compare classifier to brute reference and tutorial to expected outputs; discovery tests metadata and skills/list match.
- Invalidation or expiry: inapplicable — no separate expiry or persistent rejection mechanism on this transition
- Activation or effect: Maintainer via test output, advisory per change. Testing, not release gate proven.
- Evidence limits: Live workflow recipes are not run evidence.

>             result = server.request(2, "skills/list", {
>                 "cwds": [str(project)], "forceReload": True})
> --- `tools/codex_smoke.py`

#### EPI-RTE-book-status
Label: Book status copy

Part of: [RT-RTE-build-views](runtime.md#rt-rte-build-views)

CLI-owned build step. Build with BOOK_STATUS configured, after writing STATUS.md. Status body with a replacement heading written to configured path. Output: [EPI-OBJ-book-status](#epi-obj-book-status). SRC-1 `templates/lab.py`. This destination is distinct from the coordinator-facing status output.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Status body with a replacement heading written to configured path.
- Later read-back: Project document build or reader via configured Markdown file; advisory until regenerated and reread.
- Delegated visibility: inapplicable — the CLI dispatches no delegate.
- Selection predicate: Build with BOOK_STATUS configured, after writing STATUS.md.
- Invalidation or expiry: Rebuild and reread; disabling an output or skipping a write does not remove existing copies.
- Activation or effect: Project document build or reader via configured Markdown file; advisory until regenerated and reread. No scientific acceptance or observed reliance.
- Evidence limits: No included project document consumer or actual inclusion supplied.

>     if BOOK_STATUS:
>         Path(BOOK_STATUS).write_text("# Labyrinth status (generated)\n\n" + md.split("\n", 1)[1])
> --- `templates/lab.py`

#### EPI-RTE-sota-tex
Label: SoTA LaTeX output

Part of: [EPI-RTE-table-project](#epi-rte-table-project)

CLI-owned build step. sota.json present and SOTA_TEX configured; rows belong to configured groups. Current results and references only; can use cls_tex and result_tex overrides. Output: [EPI-OBJ-sota-tex](#epi-obj-sota-tex). SRC-1 `templates/lab.py`. This branch has a separate destination, payload and consumer from the other export.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current results and references only; can use cls_tex and result_tex overrides.
- Later read-back: Notes/book reader via configured LaTeX inclusion, if wired by the project; advisory until regenerated and rebuilt.
- Delegated visibility: inapplicable — the CLI dispatches no delegate.
- Selection predicate: sota.json present and SOTA_TEX configured; rows belong to configured groups.
- Invalidation or expiry: Rebuild and reread; disabling an output or skipping a write does not remove existing copies.
- Activation or effect: Notes/book reader via configured LaTeX inclusion, if wired by the project; advisory until regenerated and rebuilt. No scientific acceptance or observed reliance.
- Evidence limits: No history column or check of TeX override fidelity; no observed document inclusion.

>                 res = e.get("result_tex", tex_escape(e.get("result", "")))
>                 T.append(f"{cls} & {res} & {tex_escape(e.get('status', ''))} & {where}\\\\")
> --- `templates/lab.py`

#### EPI-RTE-sota-md
Label: SoTA Markdown output

Part of: [EPI-RTE-table-project](#epi-rte-table-project)

CLI-owned build step. sota.json present and SOTA_MD configured; rows belong to configured groups. Current rows, references, dates and previous results in a Markdown table. Output: [EPI-OBJ-sota-md](#epi-obj-sota-md). SRC-1 `templates/lab.py`. This branch has a separate destination, payload and consumer from the other export.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Current rows, references, dates and previous results in a Markdown table.
- Later read-back: Markdown reader via generated table; advisory until regenerated and reopened.
- Delegated visibility: inapplicable — the CLI dispatches no delegate.
- Selection predicate: sota.json present and SOTA_MD configured; rows belong to configured groups.
- Invalidation or expiry: Rebuild and reread; disabling an output or skipping a write does not remove existing copies.
- Activation or effect: Markdown reader via generated table; advisory until regenerated and reopened. No scientific acceptance or observed reliance.
- Evidence limits: Copies statuses and history text without evaluating either.

>         Path(SOTA_MD).write_text("\n".join(M))
> --- `templates/lab.py`

#### EPI-RTE-dashboard-json
Label: Write dashboard JSON

Part of: [RT-RTE-build-views](runtime.md#rt-rte-build-views)

Build serializes the projection to [EPI-OBJ-dashboard-data](#epi-obj-dashboard-data) before handling the HTML template. This JSON file is not the embedded HTML consumed by the browser. SRC-1 `templates/lab.py`, `templates/dashboard.html`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Writes dashboard/data.json; build later returns the data object to CLI dispatch.
- Later read-back: A subsequent file read in each shipped example test decodes the generated JSON and uses selected fields for assertions (SRC-1 `tests/test_lab.py`; [EPI-RTE-json-assertions](#epi-rte-json-assertions)). The browser uses embedded HTML instead; research-session JSON readers are uninspected.
- Delegated visibility: inapplicable — the CLI dispatches no delegate.
- Selection predicate: Build reaches the JSON write; neither a successful check nor an HTML template is required.
- Invalidation or expiry: A later build replaces the file; publication or file cleanup is not managed by this write.
- Activation or effect: Supplies the artifact checked by the example suite after build; test source establishes the consumer, not its execution or research reliance.
- Evidence limits: No observed test result or research-session JSON read. The live artifact comparison in SRC-1 `docs/codex-testing.md` is a prescription, not an executed result.

>     blob = json.dumps(data, ensure_ascii=False)
>     (LAB / "dashboard" / "data.json").write_text(blob)
> --- `templates/lab.py`

#### EPI-RTE-json-assertions
Label: Assert dashboard JSON

Part of: [EPI-RTE-software-check](#epi-rte-software-check)

Separate shipped consumer from the browser. Example tests load the standalone JSON written by [EPI-RTE-dashboard-json](#epi-rte-dashboard-json), then check initial resolved fractions and size-eight counts, and after the update check resolution, the exhaustive T3 node, the answered door and the open-question count. Assertions compare selected projected values to expected fixture values. The live test plan instead asks an evaluator to check agreement with graph, frontier and table, and inspect HTML separately (SRC-1 `tests/test_lab.py`, `docs/codex-testing.md`). Neither consumer is a referee for private research.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Assertion pass or failure to the suite.
- Later read-back: The test reads the file produced by the preceding build invocation; the assertions do not retain a research claim for a subsequent session.
- Delegated visibility: inapplicable — unit-test code reads the artifact directly.
- Selection predicate: The example tests reach the JSON read after build; they select specific fixture fields, not every payload field.
- Invalidation or expiry: Results apply to the built fixture in that test invocation, not to later source changes.
- Activation or effect: The test runner can fail the suite on a mismatch; evidence for maintainers, not a gate on use of research claims.
- Evidence limits: Static test implementation only. No run or successful browser render supplied.

>         data = json.loads((self.tmp / "labyrinth" / "dashboard" / "data.json").read_text())
>         res = {m["size"]: m["resolved_fraction"] for m in data["frontier"]}
> --- `tests/test_lab.py`

>         data = json.loads((self.tmp / "labyrinth" / "dashboard" / "data.json").read_text())
>         self.assertEqual({m["size"]: m["resolved_fraction"] for m in data["frontier"]}[8], 1.0)
>         nodes = {n["id"]: n for n in data["nodes"]}
>         self.assertEqual((nodes["k.n8"]["kind"], nodes["k.n8"]["tier"]), ("exhaustive", "T3"))
>         self.assertEqual(nodes["q.unknown8"]["status"], "answered")
>         self.assertEqual(data["summary"]["questions_open"], 0)
> --- `tests/test_lab.py`

>   embedded data, and `dashboard/data.json` agrees with the graph, frontier and table.
> --- `docs/codex-testing.md`

#### EPI-RTE-snapshot-write
Label: Write embedded HTML snapshot

Part of: [RT-RTE-build-views](runtime.md#rt-rte-build-views)

CLI-owned build step after [EPI-RTE-dashboard-json](#epi-rte-dashboard-json). The template must exist for an HTML write and have the marker for data insertion. Output: [MEM-OBJ-dashboard-snapshot](memory.md#mem-obj-dashboard-snapshot). Downstream read: [MEM-RTE-snapshot-browse](memory.md#mem-rte-snapshot-browse). SRC-1 `templates/lab.py`. This write is distinct from downstream browsing.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: HTML containing the build data if the template has the marker.
- Later read-back: A subsequent browser load reads the retained HTML's embedded DATA.
- Delegated visibility: inapplicable — the CLI dispatches no delegate.
- Selection predicate: Template presence gates the HTML write; the marker gates replacement.
- Invalidation or expiry: Rebuild and reread; disabling an output or skipping a write does not remove existing copies.
- Activation or effect: Exposes the embedded projection to the next browser page instance. No scientific acceptance or observed reliance.
- Evidence limits: No check prerequisite; old HTML can persist if template is absent, or a markerless template can produce HTML without the new payload.

>         (LAB / "dashboard" / "index.html").write_text(page.replace(key, key.replace("/*LABYRINTH_DATA*/null", safe), 1))
> --- `templates/lab.py`

### Claims

#### EPI-CLM-independent-evidence
Label: Independently reviewed evidence

Independently reviewed evidence is a public or procedural claim, not the same proposition as the research objective [RT-CLM-map-progress](runtime.md#rt-clm-map-progress). SRC-1 `agents/openai.yaml`, doctrine/design.

>   short_description: "Map research frontiers with independently reviewed evidence"
> --- `agents/openai.yaml`

#### EPI-CLM-resolved-frontier
Label: Resolved fraction and conflicting claims

Resolved fraction and conflicting claims is a public or procedural claim, not the same proposition as the research objective [RT-CLM-map-progress](runtime.md#rt-clm-map-progress). SRC-1 `SKILL.md`, doctrine/design.

>    unknown. The engine computes the resolved fraction per size, which makes "how much is
>    left" concrete. It also reports a value claimed both realized and impossible, since one of
>    the two claims is wrong.
> --- `SKILL.md`

#### EPI-CLM-traceable-notes
Label: Claims traceable to work and check

Claims traceable to work and check is a public or procedural claim, not the same proposition as the research objective [RT-CLM-map-progress](runtime.md#rt-clm-map-progress). SRC-1 `SKILL.md`, doctrine/design.

>    it checks. Every claim in the notes can then be traced to the work and to its check.
> --- `SKILL.md`

#### EPI-CLM-session-change
Label: Every session changes the map

A universal session assertion, distinct from the objective [RT-CLM-map-progress](runtime.md#rt-clm-map-progress). The unknowns readout requires reporting, not a map edit (SRC-1 `examples/prompts.md`). SRC-1 `README.md` doctrine/design.

> Every session starts from that map and leaves it changed. A refutation counts as progress:
> it turns a hoped-for corridor into a wall and usually reveals a new door.
> --- `README.md`

#### EPI-CLM-checked-before-use
Label: Nothing used before checking

The README headline and note-entry sentence are stronger than the metadata tagline in [EPI-CLM-independent-evidence](#epi-clm-independent-evidence). SRC-1 `SKILL.md` governs admission as established; SRC-1 `references/campaigns.md` permits data and events before verdict and reports a campaign outcome, not an independently inspected run. SRC-1 `README.md` doctrine/design; `references/campaigns.md` reported operation.

> - **Nothing is used before it is checked.** Results from agents or external models pass an
>   independent referee, with its own code, before they enter the notes.
> --- `README.md`

>    running. In one campaign such a referee caught a lemma false as stated before the attack
>    agent's final report.
> --- `references/campaigns.md`

> session's usage limit. The notes grew from 285 to 397 pages, and no false theorem entered
> them.
> --- `references/campaigns.md`

#### EPI-CLM-conjecture-test-check
Label: Checker requires every conjecture to have a test

A claim about checker coverage, distinct from the resolved-frontier claim [EPI-CLM-resolved-frontier](#epi-clm-resolved-frontier) and the research objective [RT-CLM-map-progress](runtime.md#rt-clm-map-progress). SRC-1 `docs/tutorial.md` doctrine/design.

> **`lab.py check`** validates all of this. It confirms that:
> - every link resolves;
> - every conjecture has a test;
> --- `docs/tutorial.md`


#### EPI-CLM-tier-facts
Label: Tiers citable as facts

The tier caption describes permissible citation, not admission after a referee check. SRC-1 `README.md` doctrine/design. The schema qualifies T2 as a non-peer-reviewed result with review state and restricts T3 to stated sizes; see [EPI-RTE-tier-citation](#epi-rte-tier-citation). Distinct from [EPI-CLM-independent-evidence](#epi-clm-independent-evidence).

>   <img src="assets/tiers.svg" width="88%" alt="Tiers T1 to T6: T1 to T3 may be cited as facts, T4 is evidence, T5 and T6 are speculation. T2 and T3 results also carry a review state.">
> --- `README.md`
