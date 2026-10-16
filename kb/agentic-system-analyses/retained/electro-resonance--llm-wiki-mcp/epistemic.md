---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "LLM-WIKI-MCP epistemic routes: source acquisition, deterministic and model answers, structural checks, retention and later reliance."
run-id: AAS-2026-10-15-llm-wiki-mcp-5dff0dd0576a-01
reviewed-boundary: "25efb7631082fa3732723fee08e24d39b43311fa"
---

# LLM-WIKI-MCP epistemic report

## Source-and-claim boundary

The question is how the shipped local wiki acquires and transforms truth-apt content, checks candidates, grants reliance and supplies later consumers. The scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see [Source register](boundary.md#source-register). All added inspection uses SRC-1 at the frozen revision, as implementation except for the explicitly attributed doctrine/design claims below. No target, test, example or provider was executed.

The ledger separates imported statements, model answers, deterministic answer assertions, sidecar suggestions, conversation records and structural/runtime measurements. Import preserves available text and some lineage, not an endorsement of source truth. A blank-answer check, a retrievability warning and a successful write have different targets; none is substituted for factual acceptance. The principal counterexample to treating this as merely retrieval is a deterministic fallback that asserts release readiness even with no page evidence. Conversely, the final context-window answer explicitly declines to guess a provider's native capacity. Both matter; neither licenses a system-wide judgment.

Consequential claims are [EPI-CLM-wiki-substrate](#epi-clm-wiki-substrate), [EPI-CLM-provenance-refresh](#epi-clm-provenance-refresh), [EPI-CLM-answer-fallback](#epi-clm-answer-fallback), [EPI-CLM-note-suggestions](#epi-clm-note-suggestions), and see [RT-CLM-context-budget](runtime.md#rt-clm-context-budget) and [RT-CLM-ask-nonmutation](runtime.md#rt-clm-ask-nonmutation).

### Coverage

Direct reads below extend rather than merely repeat the provisional runtime. The registered repository is not limited to the boundary's initial path list.

| Entry point or operation | SRC-1 source path | Coverage and record | Remaining limit / conclusion prevented |
| --- | --- | --- | --- |
| Packaged invocation, interactive ask, Python and MCP | `src/llm_wiki_mcp/cli.py`; `src/llm_wiki_mcp/server.py`; `pyproject.toml` | Supplied dispatch/registration account: [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch). Direct one-shot dispatcher read distinguishes ask, ingest, repair, editor and context commands. Server definition/handler search includes later registry overrides, history, notes, safe self-dispatch and following-page search. | No deployed MCP grants or host continuation; cannot infer host acceptance or planning. |
| Final agentic ask, second synthesis, blank check and fallback | `src/llm_wiki_mcp/context_api.py` | Direct final definitions, second-pass builder, public sanitizer and fallback router/composer: [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask), [EPI-RTE-answer-check](#epi-rte-answer-check), [EPI-RTE-fallback-compose](#epi-rte-fallback-compose). | No generated answers or factual evaluation trace. |
| Plain/store ask and retrieval-only | `src/llm_wiki_mcp/context_api.py`; `src/llm_wiki_mcp/server.py` | Supplied [RT-RTE-plain-ask](runtime.md#rt-rte-plain-ask), [RT-RTE-store-ask](runtime.md#rt-rte-store-ask); direct unified dispatch and final store-search override read. | Provider semantics uninspected; these prompts do not inherit first-agentic-pack guarantees. |
| Page/note search, following-page search, full-page expansion, context pack | `src/llm_wiki_mcp/context_api.py` | Direct final search bodies, context pack and history selection: [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack), [EPI-OBJ-page-notes](#epi-obj-page-notes). | Ranking is lexical, not an assessment of source truth; selected metadata need not all survive prompt trimming. |
| Source extraction and provenance refresh | `src/llm_wiki_mcp/context_api.py`; `src/llm_wiki_mcp/cli.py` | Direct extractor/page writer, hash/status database, final ingestion plan/apply and CLI `ingest_path`: [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write), [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages). | Optional extractor internals not inspected; one-shot CLI overwrites/imports through a different path, not the provenance planner. No general source-fidelity or latest-source guarantee. |
| Direct create/update, transcript/decision writes, schema, table of contents | `src/llm_wiki_mcp/server.py` | Supplied create/update account; direct decision/schema/TOC/dry-run bodies and operation inventory: [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write), [EPI-RTE-structure-check](#epi-rte-structure-check). | Transcript implementation not directly read; represented by supplied local-write account and exposed operation inventory only. No exhaustive semantic assessment of all wrappers. |
| Notes generation, iteration, candidate links | `src/llm_wiki_mcp/context_api.py` | Direct template, term extraction and link scorer: [EPI-RTE-note-template](#epi-rte-note-template). | No human/agent promotion trace; suggestion wording is not a gate on retrieval. |
| Lint, resolve, repair, dry-run write | `src/llm_wiki_mcp/server.py` | Direct check/repair/resolve bodies: [EPI-RTE-structure-check](#epi-rte-structure-check); disposition remains see [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write). | Structural domain only. No semantic repair oracle. |
| Rename/delete and later withdrawal | `src/llm_wiki_mcp/server.py` | Direct bodies: [EPI-RTE-page-withdrawal](#epi-rte-page-withdrawal). | No transitive retraction of old answers/history or semantic consequences established. |
| Ask history, compression, recursive context and recent-history prompt | `src/llm_wiki_mcp/context_api.py` | Direct recorder/compressor/recursive reader and final pack reader: [EPI-RTE-history-reshape](#epi-rte-history-reshape), [EPI-OBJ-ask-turns](#epi-obj-ask-turns). | No deployment history; compression retention and final pack consumption are different paths. |
| Self-context, context-window answer, doc reconciliation, runtime/metrics tools | `src/llm_wiki_mcp/context_api.py` | Direct context-window answer, pack and doc reconciliation; supplied config/model account: [EPI-RTE-diagnostic-check](#epi-rte-diagnostic-check), [RT-BAP-config-control](runtime.md#rt-bap-config-control). | Other metric-helper bodies available but not all inspected; prevents a system-complete negative about every diagnostic's accuracy or use. |
| Docs consolidation/development-history generation | `src/llm_wiki_mcp/context_api.py` | Supplied consolidation: [RT-RTE-docs-consolidate](runtime.md#rt-rte-docs-consolidate); development-history function inventoried only. | Development-history content transformation unassessed; prevents complete enumeration of generated documentation claims. |
| Graph, backlinks, related, exports | `src/llm_wiki_mcp/server.py`; `src/llm_wiki_mcp/context_api.py` | Direct related/backlinks/TOC and search bodies; supplied export/graph dispatch. | Views carry lexical/structural relationships, not demonstrated explanatory relations. Other view bodies not exhaustively inspected. |
| Regression/test evaluation | `src/llm_wiki_mcp/server.py`; `tests/ask_history_context_test.py` | Direct regression suite and harness result consumer; direct mocked-history/sanitizer/context-window tests: [EPI-RTE-regression-check](#epi-rte-regression-check). | Other tests available but uninspected here; no test results or quality/causal comparison supplied. |

These available-but-uninspected operations preclude a system-complete negative about all possible acceptance or evaluation routes. The narrower findings below concern the named active answer/write/read/check implementations. Excluded external weights and provider processing prevent inference about internal reasoning, learned truth, training-time warrant or parameter change; see [RT-CMP-ollama-model](runtime.md#rt-cmp-ollama-model). Missing deployment corpora prevent truth judgments on any actual imported source. Missing provider/run traces prevent observed answer correctness, activation or benefit. Missing interventions/comparisons prevent causal attribution to notes, history, repair or context budgeting.

## Epistemic-object inventory

Fields owned by linked records are `see`; local object labels do not establish additional accepted knowledge.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | Imported or caller-authored statements; source diagnostic placeholders also possible | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see record | Actual source warrant unknown; path/hash identifies a file, not truth. |
| [EPI-OBJ-page-notes](#epi-obj-page-notes) | Topic assertion and candidate-link/term scores | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see record | Template and lexical counts, not model-authored criticism or validated synthesis. |
| [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack) | Selected source statements, operational assertions, questions and prior answers | see | see | Delivery is selected and lossy; not acceptance. |
| [EPI-OBJ-fallback-answer](#epi-obj-fallback-answer) | Release-readiness, inspiration and configuration assertions; extracted lines | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see record | Deterministic branches differ from extractive reshaping. |
| [EPI-OBJ-ask-turns](#epi-obj-ask-turns) | Questions, answers and compressed excerpts; estimates and metadata | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see record | Retained answers can be wrong; source list is tool names on final agentic recording path. |
| [EPI-OBJ-check-results](#epi-obj-check-results) | Broken-link/existence/count/blank predicates, warning lists, test booleans | see | SRC-1 `src/llm_wiki_mcp/server.py`; see record | Domains bounded by executable predicates, not factual-answer validation. |
| [RT-CMP-ollama-model](runtime.md#rt-cmp-ollama-model) | Specific internal truth-apt content not determinable | see | see | Distributed-parametric provider state inaccessible; model identity not weight-pinned. |

## Authority-route ledger

Architectural status below is implementation-grounded, not observed activation. Each row separates one function; shared IDs link phases of one source-native route. `see` delegates owned details to the cited declaration. No row asserts observed epistemic acceptance. All source anchors refer to SRC-1.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) | content transformation | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | truth-apt transformation: acquisition/import | Source/caller content to wiki | File extractor; source warrant unknown | Caller import/write | Extracted/wrapped text, or diagnostic placeholder | Produces page text | No endorsement; plain text retained, rich extraction fidelity unestablished | Supplies later indexed content | see route; later retrieval via files/index, permissive until edited | SRC-1 `src/llm_wiki_mcp/context_api.py`; see object | [EPI-CLM-wiki-substrate](#epi-clm-wiki-substrate) | none | One-shot CLI and provenance ingestion differ. |
| [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) | disposition/acceptance | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Write eligibility, not truth | Existing-path/overwrite, update mode, apply flag | Caller request | Admit/reject file operation | Enforcing local write condition | Operational admission only; no evidence-consuming factual acceptance shown here | Writes/reindexes without per-content approval | see | SRC-1 `src/llm_wiki_mcp/server.py`; see route | none | none | Generic caller authorship unresolved. |
| [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) | retention | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Admitted text to retained file/index | Write and indexing code | Applied mutation | Persisted page/index | Enforcing storage | Retention, not lifecycle integration after acceptance | Makes content eligible for retrieval | see | SRC-1 `src/llm_wiki_mcp/server.py`; see route | [EPI-CLM-wiki-substrate](#epi-clm-wiki-substrate) | none | No populated corpus supplied. |
| [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) | lineage/freshness/recovery | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Source path/mtime/hash change | Provenance predicate, file identity domain | Explicit re-ingest | new/update/skip; reindex/error | Ranking-independent refresh selection | Byte freshness/lineage only, not endorsement | Changed source selected for replacement | see route; planner to writer, enforcing at apply, future retrieval | SRC-1 `src/llm_wiki_mcp/context_api.py`; see object | [EPI-CLM-provenance-refresh](#epi-clm-provenance-refresh) | none | Metadata does not store full prior source bytes; not general rollback. |
| [EPI-RTE-note-template](#epi-rte-note-template) | content transformation | implemented | [EPI-OBJ-page-notes](#epi-obj-page-notes) | truth-apt transformation: indeterminate | Page/old note to topic assertion and link suggestions | Counts/substrings and template | Explicit notes iteration | Term list, topic wording, scored candidates | Produces/overwrites sidecar | Lexical occurrence facts; topic/semantic relation not checked | Later selection can use suggestions before promotion | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | [EPI-CLM-note-suggestions](#epi-clm-note-suggestions) | suggestion-use | Old-note feedback can influence next term set; semantic preservation unproved. |
| [EPI-RTE-note-template](#epi-rte-note-template) | retention | implemented | [EPI-OBJ-page-notes](#epi-obj-page-notes) | no content change | Template result to sidecar file | Nonempty page, then file write | Each successful iteration | Sidecar retained | Enforcing write | No promotion/acceptance decision | Search/combined page can consume it | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | [EPI-CLM-note-suggestions](#epi-clm-note-suggestions) | suggestion-use | "To Review" label is not retrieval exclusion. |
| [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask), [RT-RTE-store-ask](runtime.md#rt-rte-store-ask), [RT-RTE-plain-ask](runtime.md#rt-rte-plain-ask) | operational admission/selection/consumption | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages), [EPI-OBJ-page-notes](#epi-obj-page-notes), [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack) | truth-apt transformation: non-ampliative reshaping | Retained evidence to selected context | Lexical scores/top-k, per-page/history/whole-pack limits | Current request | Ranked snippets/page excerpts/history | Ranking then permissive evidence supply | Relevance heuristic, no source truth license | Code decides what provider/caller receives | see routes and [RT-BAP-answer-guidance](runtime.md#rt-bap-answer-guidance) | SRC-1 `src/llm_wiki_mcp/context_api.py`; see pack | [RT-CLM-context-budget](runtime.md#rt-clm-context-budget) | none | Truncation can remove qualification or lineage; semantic equivalence not guaranteed. |
| [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask), [RT-RTE-store-ask](runtime.md#rt-rte-store-ask), [RT-RTE-plain-ask](runtime.md#rt-rte-plain-ask) | content transformation | implemented | [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack), [RT-CMP-ollama-model](runtime.md#rt-cmp-ollama-model) | truth-apt transformation: indeterminate | Prompt to answer text | External provider generation | Nonbasic, nondry request; different prompt families | Requested answer, failure or blank | Candidate generation; advisory output | No inspected entailment or evidence-consuming answer acceptance | Returns answer; unified routes can retain it | see routes; [RT-BAP-answer-guidance](runtime.md#rt-bap-answer-guidance) | SRC-1 `src/llm_wiki_mcp/context_api.py`; see routes | [EPI-CLM-answer-fallback](#epi-clm-answer-fallback) | none | No concrete generated answer to classify as reshaping/derivation/conjecture. |
| [EPI-RTE-answer-check](#epi-rte-answer-check) | check/evidence production | implemented | [EPI-OBJ-check-results](#epi-obj-check-results) | no content change | Normalized answer availability | Python truthiness, empty-string domain | After synthesis | Blank/nonblank | Predicate feeds continuation | Availability only | Provides branch input | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | [EPI-CLM-answer-fallback](#epi-clm-answer-fallback) | none | A false nonempty answer passes this test. |
| [EPI-RTE-answer-check](#epi-rte-answer-check) | operational admission/selection/consumption | implemented | [EPI-OBJ-fallback-answer](#epi-obj-fallback-answer) | no content change | Continue, retry or return | Blank predicate, basic-question predicate | In current ask | Extra evidence/second request, deterministic answer or ordinary answer | Enforcing branch | No factual acceptance | Blank triggers recovery; nonblank needs no truth check in this path | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | [EPI-CLM-answer-fallback](#epi-clm-answer-fallback) | none | Top-level ok can retain first-call failure. |
| [EPI-RTE-fallback-compose](#epi-rte-fallback-compose) | content transformation | implemented | [EPI-OBJ-fallback-answer](#epi-obj-fallback-answer) | truth-apt transformation: ampliative conjecture | Release-readiness/inspiration branches | Keyword selector and hardcoded prose, no factual evaluator | Recovery asks reaching composer | Specific affirmative conclusion even absent evidence | Advisory answer, then eligible retention | No evidence warrants release readiness from empty input | Can answer and feed future history | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | [EPI-CLM-answer-fallback](#epi-clm-answer-fallback) | unsupported-readiness | Concrete source deduction below; not observed execution. |
| [EPI-RTE-fallback-compose](#epi-rte-fallback-compose) | content transformation | implemented | [EPI-OBJ-fallback-answer](#epi-obj-fallback-answer) | truth-apt transformation: non-ampliative reshaping | Generic page-line fallback | Line cleaning/query scoring | Non-special question with read pages | Selected lines with best-effort framing | Advisory answer | Extracted claims remain dependent on source and lost context | Returns text and references | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | [EPI-CLM-answer-fallback](#epi-clm-answer-fallback) | none | Ranking prose does not prove strongest evidential source. |
| [EPI-RTE-history-reshape](#epi-rte-history-reshape) | retention | implemented | [EPI-OBJ-ask-turns](#epi-obj-ask-turns) | no content change | Completed turn to JSONL | Recorder/config, not factual evaluator | Unified nondry ask or explicit record tool | Stored question/first prompt/final answer | Enforcing append when enabled/succeeds | No accepted-knowledge status | Retains unverified model or fallback assertions | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | none | none | Not all asks record; first prompt can differ from answer-producing prompt. |
| [EPI-RTE-history-reshape](#epi-rte-history-reshape) | content transformation | implemented | [EPI-OBJ-ask-turns](#epi-obj-ask-turns) | truth-apt transformation: non-ampliative reshaping | Older turns to bounded Markdown | Token estimate, whitespace flattening, prefix cuts | Budget exceeded and compression enabled | Short answer excerpts; recent JSONL rewrite | Enforcing replacement | No new corroboration; degraded replay/provenance detail | Alters material reachable by later history readers | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | none | none | Older prompts/full answers removed from live JSONL; not semantic summarization. |
| [EPI-RTE-history-reshape](#epi-rte-history-reshape) | operational admission/selection/consumption | implemented | [EPI-OBJ-ask-turns](#epi-obj-ask-turns) | no content change | History to later context | Recent-history selector; separate recursive reader | Later request | Bounded recent Q/A in final pack; compressed+recent in recursive API | Advisory model context | History explicitly not immutable truth | Prior answers can guide later answers without acceptance | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | none | none | No observed dependence or improvement. |
| [EPI-RTE-structure-check](#epi-rte-structure-check) | check/evidence production | implemented | [EPI-OBJ-check-results](#epi-obj-check-results) | truth-apt transformation: entailed derivation | Link existence, incoming edges, word/paragraph lengths | Graph/file/set/count predicates | Lint/dry-run/repair request | Structural warnings and before/after reports | Advisory; repair consumes before report | Warrant bounded to those measurements of scanned state | Suggests repair actions, no enforced truth gate on create/update | see | SRC-1 `src/llm_wiki_mcp/server.py`; see route | none | none | Valid link can point to false content. |
| [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) | disposition/acceptance | implemented | [EPI-OBJ-check-results](#epi-obj-check-results), [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Repair actions to apply | Caller apply/create-missing flags and resolver | Explicit repair | Rewrite links, link orphans, add scaffold or leave unresolved | Enforcing file edits when enabled | Structural disposition, not factual acceptance/integration | Changes later navigability/retrieval | see; [EPI-RTE-structure-check](#epi-rte-structure-check) supplies check | SRC-1 `src/llm_wiki_mcp/server.py`; see route | none | none | Scaffold does not add independently justified domain knowledge. |
| [EPI-RTE-page-withdrawal](#epi-rte-page-withdrawal) | lineage/freshness/recovery | implemented | [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) | no content change | Rename/delete active page | Caller instruction and existence tests | Explicit mutation | Renamed/relinked or deleted/tombstoned page; reindex | Enforcing local removal/rename | Operational withdrawal, not recorded refutation | Removes active page, changes future retrieval eligibility | see | SRC-1 `src/llm_wiki_mcp/server.py`; see route | none | no-cascade | Old history/answers not retracted by these bodies. |
| [EPI-RTE-diagnostic-check](#epi-rte-diagnostic-check) | check/evidence production | implemented | [EPI-OBJ-check-results](#epi-obj-check-results) | truth-apt transformation: entailed derivation | Expected doc-file existence and command substrings | Filesystem/substring predicates | Reconcile-docs call | Missing/undocumented lists and ok | Advisory returned diagnostics | Only declared file-list/text-presence domain | Caller can inspect; no automatic semantic repair here | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | none | none | Fixed expected filenames can diverge from consolidated layout. |
| [EPI-RTE-diagnostic-check](#epi-rte-diagnostic-check) | content transformation | implemented | [EPI-OBJ-check-results](#epi-obj-check-results) | truth-apt transformation: non-ampliative reshaping | Active settings to context-window answer | Code formatting settings/estimates | Basic context-window request | Named settings plus explicit unknown native limit | Advisory answer | Config describes local budgets, not provider capacity | Returns without model call | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | [RT-CLM-context-budget](runtime.md#rt-clm-context-budget) | none | Not an exact tokenizer/runtime probe. |
| [EPI-RTE-regression-check](#epi-rte-regression-check) | check/evidence production | implemented | [EPI-OBJ-check-results](#epi-obj-check-results) | truth-apt transformation: entailed derivation | Tool surface, fixture mutations/retrieval, history/sanitizer behavior | Fixture assertions and result aggregation | Explicit test/harness invocation | Pass/fail predicates, aggregate exit code | Enforcing harness success/failure, not deployment acceptance | License limited to asserted fixture predicates | Caller receives result/exit; no automatic product promotion shown | see | SRC-1 `src/llm_wiki_mcp/server.py`; see route | none | none | Tests unexecuted; mock output not real model-quality evidence. |
| [RT-RTE-runtime-config](runtime.md#rt-rte-runtime-config) | behavior/policy adaptation | implemented | [RT-CMP-ollama-model](runtime.md#rt-cmp-ollama-model) | non-truth-apt policy/content update: host/model/mode/budget settings | Caller-chosen setting to later controls | Parser/default/minimum rules | Explicit config change | Future dispatch/request selection | Enforcing code selection | No knowledge or provider-capacity acceptance | Can change endpoint, model tag and context policy | see [RT-BAP-config-control](runtime.md#rt-bap-config-control) | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | none | none | Not evidence-responsive autonomous improvement or weight update. |
| [RT-RTE-docs-consolidate](runtime.md#rt-rte-docs-consolidate) | content transformation | implemented | Natural-language documentation; see route | truth-apt transformation: non-ampliative reshaping | Fixed mapped documents to concatenated categories | Static mapping/caller archive flag | Explicit consolidation | Overwritten outputs, optional archives | Enforcing write/move | No checked preservation of all claims/qualifications | Later operators may use generated docs | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; see route | none | none | Not acceptance or demonstrated method improvement. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-CLM-wiki-substrate](#epi-clm-wiki-substrate) | see | SRC-1 `README.md`; doctrine/design | see | [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write), [RT-RTE-store-ask](runtime.md#rt-rte-store-ask) | None supplied | No causal comparison with raw chunks | Markdown is authoritative storage for page retrieval | Storage "source of truth" does not establish factual truth. |
| [EPI-CLM-provenance-refresh](#epi-clm-provenance-refresh) | see | SRC-1 `METHODOLOGY.md`; doctrine/design | see | [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) | None supplied | Source identity/change predicates, not automatic verification | Explicit provenance re-ingestion is wired | Not all import paths use provenance; lineage can be redacted/truncated downstream. |
| [EPI-CLM-answer-fallback](#epi-clm-answer-fallback) | see | SRC-1 `README.md`; doctrine/design | see | [EPI-RTE-answer-check](#epi-rte-answer-check), [EPI-RTE-fallback-compose](#epi-rte-fallback-compose) | None supplied | Blank recovery is implemented; no semantic adequacy check or benefit contrast | Can return answer-first text and evidence lists | Readiness branch overstates evidential basis; generic "states uncertainty" does not make each assertion warranted. |
| [EPI-CLM-note-suggestions](#epi-clm-note-suggestions) | see | SRC-1 `src/llm_wiki_mcp/context_api.py`; emitted design guidance | see | [EPI-RTE-note-template](#epi-rte-note-template), [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask) | None supplied | No promotion trace or retrieval-quality experiment | Candidate wording distinguishes suggestions from canonical edits | Notes already affect ranking/snippets before promotion. |
| [RT-CLM-context-budget](runtime.md#rt-clm-context-budget) | see | see; doctrine/design and implementation distinguished there | see | [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask) | None supplied | Character-based estimate, alternate prompts | First-pack budgeting/inspection is implemented | Second prompt may produce answer while first prompt is recorded; native capacity unknown. |
| [RT-CLM-ask-nonmutation](runtime.md#rt-clm-ask-nonmutation) | see | see | see | [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask), [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch) | None supplied | Scope is ask's code-selected evidence actions | Prompt policy and local ask path differ from general capability surface | History/config writes remain possible; mutation tools are separately callable. |

## Bounded conclusion

**Acquisition and use are implemented; epistemic acceptance is not established for the named answer/write paths.** Page import acquires content rather than producing its warrant. Local metadata permits file-change tracking, and indexed files supply later readers. Plain-text content is copied with wrappers; optional rich extraction, placeholder text, public redaction, snippet selection and truncation limit semantic and lineage preservation. Source warrant remains unknown. See [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write), [EPI-OBJ-wiki-pages](#epi-obj-wiki-pages) and [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack).

**The answer producers differ.** Model generation is requested, but no concrete model answer or entailment check is available. Its content relation remains indeterminate. Generic deterministic fallback selects and reframes page lines; a separate keyword branch produces an affirmative release-readiness conjecture without requiring supporting pages. The final runtime context-window answer, in contrast, returns configured estimates and explicitly withholds a native-capacity claim. These findings coexist; see [EPI-RTE-fallback-compose](#epi-rte-fallback-compose) and [EPI-RTE-diagnostic-check](#epi-rte-diagnostic-check).

**Checks have narrow, consequential domains.** Blankness controls retries/fallback, not truth. Lint and dry-run checks derive structural facts; repair consumes them to alter navigation and scaffolding after caller application. Test code contains fixture oracles and an exit-status consumer, but no passing execution is supplied. No inspected active answer path records an evidence-consuming acceptance decision with a factual criterion, intended use and scope. Accordingly, retention, indexing, relinking and prompt delivery here are not lifecycle integration after such acceptance. This is a scoped finding, not an absence theorem over uninspected diagnostics/tests/document generators. See [EPI-RTE-answer-check](#epi-rte-answer-check), [EPI-RTE-structure-check](#epi-rte-structure-check) and [EPI-RTE-regression-check](#epi-rte-regression-check).

**Unaccepted content has operational influence.** Notes can shape ranking and snippets despite their suggestion label. Unified ask can retain unverified answers; later agentic prompts include bounded recent Q/A as advisory follow-up context. Compression keeps shortened answer excerpts and removes older exact turns from live JSONL. The final pack does not itself read the compressed-history file, whereas the separately exposed recursive-context helper does. Page deletion/reindexing is local withdrawal, not a cascade retracting historic answers. See [EPI-RTE-note-template](#epi-rte-note-template), [EPI-RTE-history-reshape](#epi-rte-history-reshape), [EPI-RTE-page-withdrawal](#epi-rte-page-withdrawal) and [RT-BAP-answer-guidance](runtime.md#rt-bap-answer-guidance).

**Behavioral control and learning are separate.** Explicit settings control later model/host/mode/budget choices; history provides an implemented experience-to-later-context path. Neither supplies evidence of improved capacity, content-directed criticism of a formulated theory, iterative theory revision or exercised self-improvement. No new theory-route claim is made. Provider processing/parameter changes remain uninspected; no negative about all internal learning follows. No run or intervention establishes model compliance, activation of a particular retained claim or benefit attributable to notes/history/context budgets. See [RT-CMP-ollama-model](runtime.md#rt-cmp-ollama-model), [RT-RTE-runtime-config](runtime.md#rt-rte-runtime-config) and [EPI-RTE-history-reshape](#epi-rte-history-reshape).

## Shared records

### Components

none declared in this member

### Operative objects

#### EPI-OBJ-wiki-pages
Label: Wiki pages

Source-native Markdown files under the vault's `wiki/`, interpreted as natural-language content by humans/models and parsed symbolically for frontmatter/links/index fields. Storage is local files plus derived SQLite index. Imported bodies, caller edits, decision-log entries, TOC text and repair scaffolds can all enter this substrate. This is not a duplicate of [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack): files persist outside the selected invocation prompt. Closest write account is [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write); object identity is the resulting page corpus, not that route.

SRC-1 implementation: `src/llm_wiki_mcp/context_api.py`, `src/llm_wiki_mcp/server.py`, `src/llm_wiki_mcp/cli.py`. Provenance stores source path/hash/timestamps and page associations, not a factual endorsement or full prior file snapshot. Text extraction can produce diagnostic content instead of document text.

> body=release_extract_text_from_source_file(p)
> content=f"# {title}\n\nSource file: `{p}`\nSource type: `{p.suffix.lower() or 'file'}`\n\n---\n\n{body}\n"
> wiki_path.write_text(content, encoding="utf-8")
> release_record_ingest_result(vault_path, p, wiki_title=title, wiki_path=str(wiki_path), action="updated_or_new")
> --- `src/llm_wiki_mcp/context_api.py`

> if int(row["mtime_ns"])==rec["mtime_ns"] and row["current_sha256"]==rec["sha256"]:
>     return {"action":"skip","reason":"same datestamp and hash","record":rec,"source_file_id":row["id"],"wiki_title":row["wiki_title"]}
> return {"action":"update","reason":"file changed","record":rec,"source_file_id":row["id"],"wiki_title":row["wiki_title"],"previous_sha256":row["current_sha256"]}
> --- `src/llm_wiki_mcp/context_api.py`

> return f"[No extractable DOCX paragraph text found in {p.name}.]"
> --- `src/llm_wiki_mcp/context_api.py`

The public-object sanitizer can remove the local source locator before delivery; this limits downstream auditability even when retained local provenance is available separately.

> # Keep local raw provenance out of answer prompts. Filename/wiki title remain.
> if str(k).lower() in {"path", "full_path", "wiki_path", "source_path", "db", "vault"}:
>     cleaned[k] = "[local path redacted]"
> --- `src/llm_wiki_mcp/context_api.py`

One-shot CLI import instead constructs a `Source - {stem}` title, copies available raw bytes and writes through create/overwrite, then reindexes. This is a counterexample to attributing the provenance planner to all ingestion.

> page = store.create_page(title, body, tags=["source", "ingested", path.suffix.lower().lstrip('.') or "file"], source=str(path), overwrite=overwrite)
> --- `src/llm_wiki_mcp/cli.py`

#### EPI-OBJ-page-notes
Label: AI sidecar notes

Source-native generated Markdown sidecars under `notes/`. Natural-language topic/suggestion text is interpreted by people/models; extracted terms/scores are symbolic algorithm outputs. Files persist and can be overwritten on iteration. Distinct from the transient [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack); closest supplied route [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) includes their generation but is not an object counterpart. Mechanism/evidence is see [EPI-RTE-note-template](#epi-rte-note-template), SRC-1 `src/llm_wiki_mcp/context_api.py`.

#### EPI-OBJ-fallback-answer
Label: Direct fallback answer

Part of: [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask)

This cross-kind containment identifies a material output part of agentic ask, not the entire execution route. Source-native `answer` string from `release_evidence_extract_answer`/composer. Natural-language assertions exist in process memory and can be returned, displayed and recorded. It is not [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack), which supplies input context; it is not an inspected model response. Evidence is see [EPI-RTE-fallback-compose](#epi-rte-fallback-compose), SRC-1 `src/llm_wiki_mcp/context_api.py`.

#### EPI-OBJ-ask-turns
Label: Ask history

Source-native `ask_history.jsonl` and `ask_history_compressed.md` records. JSON keys/numeric estimates are symbolic; question/prompt/answer text and compressed Markdown are natural-language material. Local filesystem storage is distinct from [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack): selected text enters the pack, but the retained record also contains omitted first-prompt/metadata fields. Overlaps the output described by [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask) and [RT-RTE-plain-ask](runtime.md#rt-rte-plain-ask), and explicit recorder tools can populate it without either ask. Evidence is see [EPI-RTE-history-reshape](#epi-rte-history-reshape), SRC-1 `src/llm_wiki_mcp/context_api.py`.

#### EPI-OBJ-check-results
Label: Check results

Source-native booleans, warning/action lists and counts returned by answer branches, lint/dry-run/repair, doc reconciliation and regression harness. Symbolic dictionaries/booleans in process memory, serialized for callers; no common persistent acceptance register is established. Parts are separated by evaluator/consumer in the ledger. No operative-object counterpart in supplied runtime; [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) and [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask) describe some consuming routes. Evidence is see [EPI-RTE-answer-check](#epi-rte-answer-check), [EPI-RTE-structure-check](#epi-rte-structure-check), [EPI-RTE-diagnostic-check](#epi-rte-diagnostic-check) and [EPI-RTE-regression-check](#epi-rte-regression-check).

### Routes

#### EPI-RTE-answer-check
Label: Answer availability check

Part of: [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask)

The final local ask code owns answer normalization, truthiness check, second synthesis and final fallback selection. State is current answer/evidence/provider status; action effects are additional retrieval/request or deterministic output, not factual candidate acceptance. Check and continuation remain separate ledger functions.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Normalized answer or recovery answer in the enclosing return dictionary; availability predicate is consumed internally.
- Later read-back: Returned answer may enter automatic history and later prompts; the predicate itself is not a retained warrant.
- Delegated visibility: Provider receives a new second-pass prompt; caller receives answer/evidence/status.
- Selection predicate: Basic-question classification bypasses generation; otherwise empty normalized first answer triggers second synthesis and empty continuation triggers fallback.
- Invalidation or expiry: Recomputed for each candidate in the current invocation; no enduring approval.
- Activation or effect: Code branches on blankness; a nonempty false assertion is not rejected by this check.
- Evidence limits: Implementation only; first-call top-level status is not a factual correctness result, nor proof of which prompt produced the returned answer.

Proposer is model or deterministic router, decider is code, caller can select dry-run/synthesis suppression; no human per-answer approval. Open user requests, no reference-answer oracle. Recovery seeks nonempty text, with no inspected content-based rollback/acceptance gate. SRC-1 implementation, `src/llm_wiki_mcp/context_api.py`:

> if not answer and "release_try_second_pass_synthesis" in globals():
>     second = release_try_second_pass_synthesis(vault_path, original, trace, evidence)
>     answer = second.get("answer") or ""
>     llm = {**llm, "second_pass": second.get("llm")}
>     evidence = evidence + release_sanitize_public_obj(second.get("extra_evidence", []))
> --- `src/llm_wiki_mcp/context_api.py:4438-4442`

#### EPI-RTE-fallback-compose
Label: Evidence fallback composition

Part of: [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask)

Code owns the router → evidence extractor → direct-answer composer → supporting-evidence rendering path. It uses current question and available page/search/capability results. Distinct material producer from the containing ask's external model generation; the combined record remains valid and needs no supersession.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Natural-language direct answer plus optional evidence/support/tool sections.
- Later read-back: Enclosing unified ask can record it and later select its answer as follow-up context.
- Delegated visibility: Returned to caller; not a provider critique or validation request.
- Selection predicate: Ordered keyword branches, then best-scored cleaned page lines, then weak-evidence messages.
- Invalidation or expiry: Recomputed per fallback; retained prior answers are not automatically invalidated by later evidence.
- Activation or effect: Recovery can supply a nonempty answer without any model generation or truth check.
- Evidence limits: Concrete deduction below is implementation evidence only; it does not assert that a user observed this answer.

Concrete counterexample, without executing target code: pass question `Is this ready?`, `read_pages=[]`, `search_hits=[]`, `caps=None` to the composer. `low` contains `ready`; `titles` and `docs` are empty; the branch chooses `the available release documentation` and returns `Yes — ... broadly ready for a GitHub release`. The readiness assertion is not entailed by an empty evidence set (a not-ready project satisfies those same inputs). It is an ampliative conjecture, not an extractive summary or acceptance decision. The final nonbasic fallback router reaches the evidence extractor; empty provider output is sufficient to reach recovery. The extractor calls the composer before deciding whether it has pages to list. This route challenges the broader supplied characterization of all deterministic fallback as merely "evidence fallback" without making the runtime container defective.

SRC-1 implementation, `src/llm_wiki_mcp/context_api.py`:

> if any(word in low for word in ["ready", "release", "github"]):
>     docs=[t for t in titles if any(k in t.lower() for k in ["readme", "install", "cli", "mcp", "architecture", "product", "books", "function"])]
>     doc_phrase="the available release documentation" if not docs else ", ".join(f"`{t}`" for t in docs[:5])
>     return (
>         "Yes — based on the wiki evidence, this looks broadly ready for a GitHub release, with the normal caveat that a final clean checkout, "
> --- `src/llm_wiki_mcp/context_api.py`

> lines=["## Direct answer", "", release_compose_best_effort_direct_answer(q, read_pages, search_hits, caps), ""]
> --- `src/llm_wiki_mcp/context_api.py`

The inspiration branch likewise returns source-native lineage prose by keyword without inspecting page content. Generic fallback instead selects lines and adds source-ranking/best-effort framing; it can lose qualifiers through line selection, cleaning and cutting. No evidence-consuming factual acceptance criterion, intended-use license, oracle or promotion decision is implemented in this composer. The caller may reject the displayed product externally, but that decision is not inspected.

#### EPI-RTE-note-template
Label: Sidecar note iteration

Part of: [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write)

Code reads a page and its prior sidecar, counts terms, scores other pages by substring overlap/backlink-title bonus, renders a fixed template and overwrites the sidecar. Natural-language "appears to discuss" and proposed semantic links are distinguished from measured occurrence. This is a part, not a competing identity for the combined write route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Note path, terms and candidate-link dictionaries, or missing-page error.
- Later read-back: Subsequent iteration reads old note; page/note search scores note terms and may select its snippet; combined-page context concatenates page and note.
- Delegated visibility: Calling CLI/MCP/Python consumer receives result; model can receive selected note snippets in later evidence.
- Selection predicate: Existing page; frequency terms from page plus old note; other-page title/first 3000 characters plus backlink-title bonus for candidate links.
- Invalidation or expiry: Rerun replaces note; no semantic invalidation or evidence-based promotion gate shown.
- Activation or effect: Sidecar becomes available to ranking and context independently of canonical-page promotion.
- Evidence limits: No retrieval improvement or accepted semantic relationship is demonstrated; old-note boilerplate can affect extracted terms.

Caller triggers iteration, code proposes and writes without per-content human approval; missing page can block it, caller can withhold invocation. Guidance persists inside generated note; later editors can promote links, but this implementation does not perform an evidence-consuming promotion. No expected-answer oracle or experiment is wired. Topic output relation is indeterminate: occurrence-driven wording may be loose description or unsupported semantic inference; source content/semantic criterion is needed to decide for a concrete page.

SRC-1 implementation and emitted doctrine/design, `src/llm_wiki_mcp/context_api.py`:

> terms = release_extract_terms(page_text + "\n" + old_note, 25)
> links = release_find_candidate_links(vault_path, title, max_links)
> --- `src/llm_wiki_mcp/context_api.py`

> This page appears to discuss: {', '.join(terms[:12]) if terms else 'no clear extracted terms yet'}.
> --- `src/llm_wiki_mcp/context_api.py`

> - Candidate links are suggestions until promoted into the source page or accepted by a human/agent.
> --- `src/llm_wiki_mcp/context_api.py`

> excerpt_source = note if note and any(t in note.lower() for t in terms) else source
> win = release_centered_match_excerpt(excerpt_source, matched or terms, context_chars=context_chars)
> --- `src/llm_wiki_mcp/context_api.py`

The final search loop also adds a score bonus when the query term occurs in a note. This is operational ranking authority, not factual or canonical status.

#### EPI-RTE-history-reshape
Label: Ask history retention

The recorder appends a turn, compresses when configured estimates exceed a threshold, and exposes recent/recursive readers. Code owns each phase. This spans the recorder used by [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask), unified [RT-RTE-plain-ask](runtime.md#rt-rte-plain-ask) and explicit record/compression tools in [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch); not wholly a part of exactly one supplied route. Distinct identity is the history write/reshape/read chain, not a duplicate ask execution.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Record/path, compression metadata or reconstructed context; enclosing ask can return metrics/error even if persistence fails.
- Later read-back: Final pack uses up to eight recent Q/A with per-answer cut and history budget; recursive-context API separately includes compressed Markdown and recent memory.
- Delegated visibility: Callers can inspect history/context; selected history enters subsequent provider prompt. Stored prompts are not copied verbatim by final recent-Q/A renderer.
- Selection predicate: History enabled for append; compression enabled and estimate over max-history threshold for compaction; keep-recent-turns setting splits older/recent.
- Invalidation or expiry: Compaction rewrites live JSONL to recent turns, appends compressed excerpts to existing Markdown; no factual rejection/invalidation based on later answers shown.
- Activation or effect: Retained answers become eligible for later advisory context, not automatically accepted beliefs or revised policies.
- Evidence limits: No observed later dependence or benefit; first prompt can be retained when second synthesis supplies answer; source list on final agentic route is tool names, not passage-level warrant.

Proposer is automatic current-turn recorder or explicit caller-supplied record. Code/config decides append/compaction; caller can disable history/compression or omit explicit invocation. No per-content human approval or factual oracle. Compression guidance is shipped truncation rules, not a model critique; there is no semantic rollback protocol. SRC-1 implementation, `src/llm_wiki_mcp/context_api.py`:

> a = " ".join(str(row.get("answer", "")).split())[:1000]
> src = row.get("sources") or []
> summary_parts.append(f"## Turn: {q[:120]}")
> --- `src/llm_wiki_mcp/context_api.py`

> with live.open("w", encoding="utf-8") as f:
>     for row in recent:
>         f.write(_release_json.dumps(row, ensure_ascii=False) + "\n")
> --- `src/llm_wiki_mcp/context_api.py`

> lines = ["# Recent Ask/Reply History", "", "These are recent local CLI ask turns. Use them for follow-up context, not as immutable truth.", ""]
> --- `src/llm_wiki_mcp/context_api.py`

> if ask.get("recursive_enabled", True):
>     if compressed:
>         parts.append("# Compressed Long-Term Ask Memory\n\n" + compressed)
>     if recent:
>         parts.append("# Recent Ask Memory\n\n" + recent)
> --- `src/llm_wiki_mcp/context_api.py`

Working-context control differs from a separate-agent frame: code copies selected history by value, truncates answers and whole sections, and can reload external history through exposed readers. No sub-agent isolation or frame return is established. Current-call pruning does not remove the page corpus; compaction, separately, changes retained exact-turn availability. Delivery does not establish that the provider treated the historical answer as true.

#### EPI-RTE-structure-check
Label: Structural wiki checks

Code computes graph/file existence and count predicates in lint, word/paragraph/link predicates in dry-run-write, and before/after reports for repair. Closest supplied [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) includes repair admission, not the entire independently callable lint/preview evaluator family. This evaluator record does not replace that write route.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Broken links, orphan/short-page lists, preview warnings/ok or before/after repair report.
- Later read-back: Repair edits can persist and be retrieved; reports have no independent durable acceptance read-back established.
- Delegated visibility: CLI/MCP/Python caller gets report; no model factual evaluation occurs here.
- Selection predicate: Current wiki graph/files, supported preview mode, lexical word counts and paragraph lengths; repair invokes lint before and after apply.
- Invalidation or expiry: Results describe scanned state and are recomputed on later call; no immutable certificate.
- Activation or effect: Repair consumes structural findings to plan changes; callers receive warnings. Direct create/update need not call preview.
- Evidence limits: Domain is retrievability/navigation predicates, not source correctness or semantic adequacy. File scan is not guaranteed atomic against concurrent edits.

Open caller requests; code proposes actions, apply and create-missing flags control admission, caller can veto. No expected factual answer/reference outcome; fixtures are separate test oracles. Recovery is reindex/recheck/edit, not automatic old-content restoration. Checked counts are entailed by scanned strings under these functions; interpretation outside that formal domain is not licensed. SRC-1 implementation, `src/llm_wiki_mcp/server.py`:

> if len(plain_words(body)) < 20:
>     short.append(p.stem)
> return {'broken_links': broken, 'orphans': sorted(orphans), 'very_short_pages': sorted(short), 'page_count': len(existing), 'ok': not broken}
> --- `src/llm_wiki_mcp/server.py`

> if wc<50: warnings.append('doc-too-short: consider adding enough context for retrieval')
> if wc>1800: warnings.append('doc-too-long: consider splitting into linked sub-pages')
> --- `src/llm_wiki_mcp/server.py`

> 'Repair improves navigation; it does not replace human review of source meaning.'
> --- `src/llm_wiki_mcp/server.py`

Concrete deduction: a preview containing fewer than 50 `plain_words` triggers the short-document warning; it does not imply that any proposition in the preview is false. Conversely, arbitrary false prose with enough words and no broken links need not trigger a warning. Thus a structural result can guide maintenance but cannot stand in for factual acceptance.

#### EPI-RTE-page-withdrawal
Label: Page rename deletion

Caller → `rename_page`/`delete_page` → file mutation and reindex → subsequent active-page readers. Code owns changes with process filesystem authority. Closest supplied [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) describes create/update/ingest/notes/repair; rename/delete are distinct exposed operations, not a correction to that account.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Rename metadata/changed pages or deleted/tombstone/backlinks-before-deletion result.
- Later read-back: Later page readers/index consumers see changed active files; tombstone copy can remain in deleted directory. Existing ask-history records are not rewritten by these bodies.
- Delegated visibility: Invoking caller gets result; other consumers depend on subsequent read/cache behavior.
- Selection predicate: Caller-named page, source/target existence, update-links/tombstone flags; rename uses selected literal wiki-link replacements.
- Invalidation or expiry: Reindex called after mutation; no transitive historic-answer/sidecar/provenance retraction shown in these methods, and cached search can retain prior results until its TTL.
- Activation or effect: Removes active page or changes its identity/link targets; old answer assertions can remain retained.
- Evidence limits: Local operational withdrawal is not evidence of epistemic refutation, complete cascade invalidation, atomic rollback or observed fresh results.

Caller proposes and can withhold operation; code rejects missing source/existing rename target. No human per-content acceptance or factual oracle is inserted. Optional tombstone preserves page bytes on delete, not all dependent artifacts; rename writes new file then removes old, without a demonstrated full transaction. SRC-1 implementation, `src/llm_wiki_mcp/server.py`; cache selection corroborated by final search in `src/llm_wiki_mcp/context_api.py`.

> if tombstone:
>     shutil.copyfile(path, deleted_dir/f'{title}.{int(time.time())}.md')
> path.unlink(); self.reindex()
> return {'title': title, 'deleted': True, 'tombstone': tombstone, 'incoming_links_before_delete': backlinks['incoming']}
> --- `src/llm_wiki_mcp/server.py`

> new_path.write_text(make_front_matter(meta)+body, encoding='utf-8')
> old_path.unlink()
> changed=[]
> --- `src/llm_wiki_mcp/server.py`

#### EPI-RTE-diagnostic-check
Label: Runtime document diagnostics

Two separated ledger functions share this diagnostic family: doc reconciliation returns fixed expected-file/command-presence measurements; the final context-window answer renders active settings and uncertainty. No counterpart in supplied runtime beyond adjacent [RT-RTE-runtime-config](runtime.md#rt-rte-runtime-config) and [RT-CLM-context-budget](runtime.md#rt-clm-context-budget): these diagnostics read/report rather than set budgets or build the pack.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Missing/undocumented-doc lists and ok, or context-window answer text naming estimates and unknown native model capacity.
- Later read-back: inapplicable — these diagnostic bodies do not independently retain updated content; enclosing ask may separately record returned text.
- Delegated visibility: Caller receives result; basic context-window ask bypasses model generation.
- Selection predicate: Fixed expected-document names and command substrings for reconciliation; basic intent plus active settings/history for context answer.
- Invalidation or expiry: Recomputed from current filesystem/settings; no continuing certificate of documentation completeness/provider capacity.
- Activation or effect: Diagnostic output advises caller; context answer returns directly. Reconciliation result has no automatic repair/disposition consumer in inspected body.
- Evidence limits: Presence checks do not establish semantic documentation accuracy; settings estimates do not probe native provider token capacity.

Open requests, program predicates not model judgment; caller can act later, no automatic acceptance gate/oracle or retained machinery update in these bodies. SRC-1 implementation, `src/llm_wiki_mcp/context_api.py`:

> missing_docs = [d for d in expected_docs if not (docs / d).exists()]
> commands = list(release_command_tool_map().keys())
> fn_text = function_list.read_text(encoding="utf-8", errors="replace") if function_list.exists() else ""
> undocumented = [c for c in commands if c not in fn_text]
> --- `src/llm_wiki_mcp/context_api.py`

> "I do not know the exact native context-window length of the configured Ollama model from the wiki alone. The ask context is now configurable and less conservative than the earlier release.",
> --- `src/llm_wiki_mcp/context_api.py`

#### EPI-RTE-regression-check
Label: Regression fixture checks

Explicit developer/test invocation → suite using tool client or mocked generation → assertions/results aggregation → printed report and harness exit status. Program owns comparison against fixture expectations. No route counterpart in supplied runtime; [RT-RTE-mcp-dispatch](runtime.md#rt-rte-mcp-dispatch) is exercised by one harness but is not this evaluator.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Regression result booleans/aggregate or assertion failures; async harness returns 0 only if all suite predicates pass.
- Later read-back: inapplicable — inspected harness does not retain a candidate acceptance artifact for later production use.
- Delegated visibility: Human/CI caller can receive printed JSON or test-script output; no provider quality judgment follows.
- Selection predicate: Explicit shipped test cases; expected tool-name set, seeded counts, fixture retrieval/mutation predicates, mocked history/sanitizer/context-window assertions.
- Invalidation or expiry: Test results would apply to that invocation/fixture only; none supplied here.
- Activation or effect: Aggregate controls harness exit code; no automatic deployment/successor-selection consumer shown.
- Evidence limits: Test source is not passing results; mocked answer establishes no actual model quality. Other tests remain uninspected in this member.

Mode is bounded fixture checks, not ordinary open asks. Test authors provide reference expectations; program decides pass/fail, developer chooses invocation and any later response. This constitutes narrow fixture oracles, not an answer oracle for arbitrary user questions. No production update proposal, rollback or promoted successor is implemented by result aggregation. SRC-1 implementation, `src/llm_wiki_mcp/server.py`, `tests/ask_history_context_test.py`:

> results.append({'name':'tools_list_expected_surface','pass':names==expected,'details':{'count':len(names),'names':sorted(names)}})
> --- `src/llm_wiki_mcp/server.py`

> return 0 if suite['all_passed'] else 1
> --- `src/llm_wiki_mcp/server.py:1744-1744`

> return {"ok": True, "answer": "The first answer mentions a working prototype.", "elapsed_seconds": 0.01}
> --- `tests/ask_history_context_test.py`

### Claims

#### EPI-CLM-wiki-substrate
Label: Markdown source of truth

SRC-1 doctrine/design, `README.md`. Claims retained Markdown authority for retrieval and model context. Distinct from [RT-CLM-context-budget](runtime.md#rt-clm-context-budget), which concerns sizing/inspection, not the storage authority claim. No counterpart among supplied runtime claims.

> The core idea is simple: Markdown remains the human-readable source of truth, SQLite provides a fast local index, and an Ollama-compatible local model can answer questions using retrieved wiki context.
> --- `README.md`

#### EPI-CLM-provenance-refresh
Label: Provenance source refresh

SRC-1 doctrine/design, `METHODOLOGY.md`. Claims preserved provenance enables refresh; no supplied claim counterpart. Closest implementation account is [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write), not a separate claim identity.

> 2. Preserve provenance so pages can be refreshed when source files change.
> --- `METHODOLOGY.md`

#### EPI-CLM-answer-fallback
Label: Answer first fallback

SRC-1 doctrine/design, `README.md`. Claims a blank-response fallback gives direct best-effort answer, uncertainty and references. Distinct from the sizing and nonmutation claims [RT-CLM-context-budget](runtime.md#rt-clm-context-budget) and [RT-CLM-ask-nonmutation](runtime.md#rt-clm-ask-nonmutation).

> `/ask` uses the configured Ollama model when available. If model synthesis returns a blank response, the CLI now falls back to an answer-first evidence summary: it gives a direct best-effort answer, states uncertainty, and then lists the wiki pages/tools used. This avoids returning only references when the local model is overloaded or returns an empty response.
> --- `README.md`

#### EPI-CLM-note-suggestions
Label: Candidate link suggestions

SRC-1 emitted doctrine/design in `src/llm_wiki_mcp/context_api.py`. Generated notes distinguish suggested links from canonical or accepted links while requiring their inclusion in search. No supplied claim counterpart; closest route [RT-RTE-knowledge-write](runtime.md#rt-rte-knowledge-write) is their producer. Passage is see [EPI-RTE-note-template](#epi-rte-note-template).

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member; paths are assessed per ledger row and supplied [RT-BAP-answer-guidance](runtime.md#rt-bap-answer-guidance), [RT-BAP-config-control](runtime.md#rt-bap-config-control).
