---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "AriGraph epistemic routes: observation and paragraph acquisition, model fact maintenance, decision authority and bounded evaluation at the frozen commit."
run-id: AAS-2026-10-12-arigraph-fd0f6f1c1383-01
reviewed-boundary: e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2
---

# AriGraph epistemic report

## Source-and-claim boundary

The question is how AriGraph turns observations or paragraphs into material that later decisions rely on, and what its checks license. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see [Source register](boundary.md#source-register). SRC-1 is the frozen repository. Direct source inspection supports implementation deductions, not fresh target execution. Supplied runtime records remain provisional but their selected forcing cases survive the direct reads below.

The principal public performance claim is see [RT-CLM-memory-performance](runtime.md#rt-clm-memory-performance). Extraction and replacement instructions make narrower source-fidelity and conservative-maintenance claims, see [EPI-CLM-concrete-extraction](#epi-clm-concrete-extraction) and [EPI-CLM-conservative-replacement](#epi-clm-conservative-replacement). The README's title uses “Learning Knowledge Graph World Models”; the exposed routes support experience-fed memory construction, not by that label alone validated explanatory models or improved capacity.

Coverage separates direct reads from supplied findings. No new source is introduced. An available but uninspected task or log is not an access gap.

| Entry point or operation | Source path | Coverage and record citations | Limit and conclusion prevented |
|---|---|---|---|
| Game invocation, planner/action, exploration, navigation | `pipeline_arigraph.py`; `agents/parent_agent.py`; `prompts/system_prompts.py` | Direct complete reads; see [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle), [RT-RTE-graph-navigation](runtime.md#rt-rte-graph-navigation) | No fresh trace; current-default activation, reliable compliance and benefit unestablished. |
| Fact extraction, replacement, add/delete, clear and retrieve | `graphs/contriever_graph.py`; `graphs/parent_graph.py`; `prompts/prompts.py` | Direct complete reads; see [RT-RTE-game-memory](runtime.md#rt-rte-game-memory), [EPI-RTE-triplet-parsing](#epi-rte-triplet-parsing), [EPI-RTE-removal-parsing](#epi-rte-removal-parsing) | Warrant of external inputs and opaque model interpretations unresolved. |
| QA ingest, answer, metrics and local-model variant | `musique_test_big.py`; `graphs/contriever_graph.py` | Direct complete reads; see [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle), [EPI-RTE-answer-metrics](#epi-rte-answer-metrics); local-agent detail supplied by [RT-CMP-llama-agent](runtime.md#rt-cmp-llama-agent) | HotpotQA shape mismatch and graph-model selection defect bound reproduction claims. Dataset correctness unassessed. |
| Hypergraph exposed interface, deletion and event ranking | `graphs/hypergraph.py`; `prompts/prompts.py` | Direct complete reads; see [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update) | Interface implementation is not evidence of a shipped downstream consumer or deployment. |
| Intended removal evaluator | `pipeline_graph_evaluation.py`; `graphs/lazy_graph.py` | Evaluator directly read; LazyGraph finding supplied by [RT-RTE-graph-evaluation](runtime.md#rt-rte-graph-evaluation) | Undefined initial state and uncalled scoring defeat an operational-validation inference. |
| Embedding fact traversal and fixed-reference diagnostic | `utils/retriever_search_drafts.py` | Direct complete read; see [EPI-RTE-reference-match](#epi-rte-reference-match), [RT-RTE-game-memory](runtime.md#rt-rte-game-memory) | Similarity thresholds and reference membership do not certify truth. |
| Observation cleanup, normalization, episode ranking and auxiliary navigation | `utils/utils.py` | Direct bounded reads of lines 1–110, 129–193, 235–304; see [EPI-RTE-observation-cleanup](#epi-rte-observation-cleanup), [EPI-RTE-triplet-parsing](#epi-rte-triplet-parsing) | Remaining reward, exit and thesis helpers are covered only by supplied runtime findings; no exhaustive helper correctness claim. Auxiliary navigation has an uninitialized `curr_loc` read; no root invocation found in the scoped search. |
| Environment feedback and reference facts | `utils/textworld_adapter.py` | Direct lines 1–100; see [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle), [RT-RTE-graph-evaluation](runtime.md#rt-rte-graph-evaluation) | External TextWorld/task semantics not executed or independently checked; rest of rendering helper uninspected. |
| Summary/full-history/smart-RAG alternatives and human driver | `pipeline_summary.py`; `pipeline_fullhist.py`; `pipeline_smartrag.py`; `interactive_human_games.py` | Supplied findings plus direct scoped dispatch/update searches; see [RT-RTE-summary-cycle](runtime.md#rt-rte-summary-cycle), [RT-RTE-full-history](runtime.md#rt-rte-full-history), [RT-RTE-smart-rag](runtime.md#rt-rte-smart-rag), [RT-RTE-human-play](runtime.md#rt-rte-human-play) | No independently observed baseline fidelity, human policy or benefit. |
| Model/checkpoint and embedding interiors | `utils/contriever.py`; `src/contriever.py`; `agents/llama_agent.py` | Supplied [RT-CMP-retriever](runtime.md#rt-cmp-retriever), [RT-CMP-gpt-agent](runtime.md#rt-cmp-gpt-agent), [RT-CMP-llama-agent](runtime.md#rt-cmp-llama-agent) | Exact upstream weights and provider internals unavailable; no parametric knowledge acquisition or training-quality conclusion. |
| Authored reflexion instruction | `prompts/prompts.py` | Direct definition and scoped search corroborate [RT-ABS-reflex-invocation](runtime.md#rt-abs-reflex-invocation) | No named invocation; does not rule out opaque model reasoning. |
| Results, tasks, assets and training support | `logs/`; `qa_data/`; `envs/`; `img/`; `src/utils.py`; `src/dist_utils.py` | Coverage and exclusions see boundary; performance claim see [RT-CLM-memory-performance](runtime.md#rt-clm-memory-performance) | Not directly reassessed here; prevents aggregate efficacy, fixture fidelity and all-repository evaluation negatives. |

Dispatch search at the frozen revision covered root Python files, `agents/`, `graphs/`, `prompts/`, `utils/` and `src/contriever.py`, using `argparse`, `click`, `register`, `hook`, `tools=`, `tool_calls`, `reflex_prompt`, score calls and mutation/load terms. It found script entry points and TextWorld registration rather than an application tool registry in these paths. The source exposes callable graph/helper operations beyond the main driver; the fixed-reference diagnostic is therefore assessed separately. This is not a claim that all source-support or excluded bytecode paths lack evaluators. No runtime supersession is needed: the supplied combined routes remain valid containers for the parts declared here.

Missing fresh execution evidence prevents current-default operation claims. Missing intervention/comparison evidence prevents causal attribution of performance to extraction, replacement, episodes or embeddings individually. External-input truth, exact model versions and model interpretation fidelity remain unknown. Accessible logs can support only their attributed sequences, see the runtime's game and QA records; no new log sampling was performed here.

## Epistemic-object inventory

Each row identifies one material part; generic identity/form/substrate belong to the cited declaration. Natural-language propositions inside symbolic triplets must not be confused with numerical embeddings used to rank them.

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-observation-text](#epi-obj-observation-text) | Statements about visible game state or paragraph subject matter | see record | SRC-1, `pipeline_arigraph.py` | Source warrant unknown; game cleanup can discard text. |
| [EPI-OBJ-triplets](#epi-obj-triplets) | Subject–relation–object propositions about an environment or QA subject | see record | SRC-1, `graphs/contriever_graph.py` | Semantic fidelity and certainty are not locally adjudicated. |
| [EPI-OBJ-episodic-text](#epi-obj-episodic-text) | Retained observation/paragraph statements | see record | SRC-1, `graphs/contriever_graph.py` | Raw relative to graph extraction, not raw relative to all game preprocessing. |
| [EPI-OBJ-outdated-triplets](#epi-obj-outdated-triplets) | A model assertion that an old fact is outdated/redundant | see record | SRC-1, `utils/utils.py` | Parsed deletion target omits replacement side and rationale. |
| [EPI-OBJ-answer](#epi-obj-answer) | QA answer and accompanying explanation | see record | SRC-1, `musique_test_big.py` | No checked entailment from retrieved evidence. |
| [EPI-OBJ-answer-metrics](#epi-obj-answer-metrics) | Token overlap and exact normalized answer equality | see record | SRC-1, `musique_test_big.py` | Lexical evaluator, not explanation or source-truth oracle. |
| [RT-OBJ-plan](runtime.md#rt-obj-plan) | Goals are not truth-apt; reasons/progress can be | see record | SRC-1, `pipeline_arigraph.py` | Truth-apt subcontent not individually recorded or checked. |
| [EPI-OBJ-thesises](#epi-obj-thesises) | Thesis sentences and retained event text | see record | SRC-1, `graphs/hypergraph.py` | No root consumer established; linked event/claim text differs from embeddings. |
| [EPI-OBJ-summary](#epi-obj-summary) | Model summary of states/outcomes plus strategic claims | see record | SRC-1, `pipeline_summary.py` | Fidelity and entailment indeterminate. |
| [RT-CMP-retriever](runtime.md#rt-cmp-retriever) | None individuated in weights/embeddings | see record | SRC-1, `utils/contriever.py` | Numerical similarity is not a fact-truth estimate established by this evidence. |
| [RT-CMP-gpt-agent](runtime.md#rt-cmp-gpt-agent), [RT-CMP-llama-agent](runtime.md#rt-cmp-llama-agent) | Parametric truth-apt contents not determinable | see records | SRC-1, `agents/parent_agent.py` | Opaque model knowledge cannot be inventoried from returned text or identifiers. |
| [RT-OBJ-system-prompts](runtime.md#rt-obj-system-prompts) | Rules/goals primarily policy; factual examples are illustrative | see record | SRC-1, `prompts/prompts.py` | Static instructions do not establish experience-derived tested theory. |

## Authority-route ledger

Fields owned by canonical records say `see`. Splits below assess functions separately without redeclaring the same runtime container. Results are possible implementation results unless an explicitly cited record supplies bounded observed support. Epistemic authority is never inferred from delivery or storage alone.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-observation-cleanup](#epi-rte-observation-cleanup) | content transformation | implemented | [EPI-OBJ-observation-text](#epi-obj-observation-text) | truth-apt transformation: acquisition/import | Environment feedback to extraction input | see route | see route | see route | Text supplied downstream | Input source warrant unknown; omission demonstrated | Limits what extraction sees | see route | SRC-1, `utils/utils.py` | none | none | Acquisition includes lossy preprocessing. |
| [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle) | content transformation | implemented | [EPI-OBJ-observation-text](#epi-obj-observation-text) | truth-apt transformation: acquisition/import | Dataset paragraph to memory input | see route | see route | see route | Paragraph ingestion | Source warrant unknown; text retained | Paragraphs enter per-task graph | see [RT-BAP-memory-decisions](runtime.md#rt-bap-memory-decisions) | SRC-1, `musique_test_big.py` | none | none | Dataset integrity unassessed. |
| [RT-RTE-game-memory](runtime.md#rt-rte-game-memory), [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle) | content transformation | implemented | [EPI-OBJ-triplets](#epi-obj-triplets) | truth-apt transformation: indeterminate | Input text to extracted propositions | Model interpretation, domain game/paragraph content; see routes | see routes | see routes | Parsed candidates can enter memory | Candidate extraction only; neither entailment nor non-entailment established generally | Creates facts later selected for decisions | see [RT-BAP-memory-decisions](runtime.md#rt-bap-memory-decisions) | SRC-1, `prompts/prompts.py` | [EPI-CLM-concrete-extraction](#epi-clm-concrete-extraction) | Fidelity not enforced | Per-output provenance/semantic comparison needed to distinguish faithful compression from conjecture. |
| [EPI-RTE-triplet-parsing](#epi-rte-triplet-parsing) | content transformation | implemented | [EPI-OBJ-triplets](#epi-obj-triplets) | truth-apt transformation: non-ampliative reshaping | Text fragments to normalized triplet candidates | see route | see route | see route | Syntactic filtering and normalized identity | No truth license; case/alias assumptions bound preservation | Malformed/empty fragments omitted; normalized duplicates suppressed | see route | SRC-1, `utils/utils.py` | none | none | Real entity distinctions can be collapsed by normalization. |
| [RT-RTE-game-memory](runtime.md#rt-rte-game-memory) | check/evidence production | implemented | [EPI-OBJ-outdated-triplets](#epi-obj-outdated-triplets) | no content change | Old candidates versus new facts: same-aspect redundancy/conflict | Model under conservative instruction; see route | see route | Replacement proposal | Advisory proposal until code consumes it | Model comparison, not independent truth check | Supplies removal candidates | see route | SRC-1, `prompts/prompts.py` | [EPI-CLM-conservative-replacement](#epi-clm-conservative-replacement) | Narrow candidate pool | Directional/other excluded strings are not judged by this request. |
| [EPI-RTE-removal-parsing](#epi-rte-removal-parsing) | disposition/acceptance | implemented | [EPI-OBJ-outdated-triplets](#epi-obj-outdated-triplets) | no content change | Proposal to deletion of matching old item | see route | see route | see route | Enforcing state deletion except guards | No evidence-consuming acceptance of replacement truth | Removes matching unprotected facts, potentially without installed replacement | see route | SRC-1, `utils/utils.py` | [EPI-CLM-conservative-replacement](#epi-clm-conservative-replacement) | Replacement link discarded | Protected locations survive even a valid deletion proposal. |
| [RT-RTE-game-memory](runtime.md#rt-rte-game-memory), [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle) | retention | implemented | [EPI-OBJ-triplets](#epi-obj-triplets), [EPI-OBJ-episodic-text](#epi-obj-episodic-text) | no content change | Candidate/text to local stores | see routes | see routes | see routes | Admission without semantic acceptance | Retention grants availability, not warrant | Candidates remain retrievable until delete/reset | see routes | SRC-1, `graphs/contriever_graph.py` | none | none | Episodic text is not withdrawn with old triplet deletion. |
| [RT-RTE-game-memory](runtime.md#rt-rte-game-memory), [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle) | operational admission/selection/consumption | implemented | [EPI-OBJ-triplets](#epi-obj-triplets), [EPI-OBJ-episodic-text](#epi-obj-episodic-text) | no content change | Memory to context selection | see routes | see routes | see routes | Ranking then model-context delivery | Similarity/overlap supplies relevance only | Selected old facts/text become decision inputs | see [RT-BAP-memory-decisions](runtime.md#rt-bap-memory-decisions) | SRC-1, `utils/retriever_search_drafts.py` | none | none | Omitted/new/recent filters change delivered subset; receipt is not activation. |
| [RT-RTE-game-memory](runtime.md#rt-rte-game-memory) | content transformation | implemented | [EPI-OBJ-triplets](#epi-obj-triplets) | truth-apt transformation: indeterminate | Changed location plus last action to reciprocal spatial claims | Fixed substring mapping; see route | see route | Two location edges | Direct addition and later path use | Conditional spatial inference only; environment motion semantics unverified | Enables route construction without semantic check | see [RT-RTE-graph-navigation](runtime.md#rt-rte-graph-navigation) | SRC-1, `graphs/contriever_graph.py` | none | none | Teleports/ambiguous commands can defeat direction interpretation; no warranted-premise derivation claimed. |
| [RT-RTE-graph-navigation](runtime.md#rt-rte-graph-navigation) | operational admission/selection/consumption | implemented | [EPI-OBJ-triplets](#epi-obj-triplets) | no content change | Graph path to environment commands | see route | see route | see route | Enforcing command dispatch | Reachability computation is bounded by graph encoding, not world truth | Multiple commands before next planner check | see [RT-BAP-action-dispatch](runtime.md#rt-bap-action-dispatch) | SRC-1, `graphs/parent_graph.py` | none | none | Feedback does not retrospectively validate all graph edges. |
| [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle) | behavior/policy adaptation | implemented | [RT-OBJ-plan](runtime.md#rt-obj-plan) | non-truth-apt policy/content update: revised goals and priorities, with indeterminate factual reasons | New context to plan/action/exploration | see route | see route | see route | Whole-plan replacement, parser/dispatcher consumption | No independent acceptance of progress or reason claims | New guidance influences later requests; action parsing alone gates fallback | see [RT-BAP-plan-decisions](runtime.md#rt-bap-plan-decisions), [RT-BAP-action-dispatch](runtime.md#rt-bap-action-dispatch) | SRC-1, `pipeline_arigraph.py` | none | Prompt policy not invariant | Independent learning/reflection/benefit not inferred. |
| [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle) | content transformation | implemented | [EPI-OBJ-answer](#epi-obj-answer) | truth-apt transformation: indeterminate | Retrieved text/facts plus question to answer | see route | see route | see route | Answer returned and logged | Candidate answer; prompt asks abstention on doubt | Answer proceeds to metrics without truth gate | see route | SRC-1, `musique_test_big.py` | none | none | Needs per-answer premise/entailment analysis; fluency not warrant. |
| [EPI-RTE-answer-metrics](#epi-rte-answer-metrics) | check/evidence production | implemented | [EPI-OBJ-answer](#epi-obj-answer), [EPI-OBJ-answer-metrics](#epi-obj-answer-metrics) | truth-apt transformation: entailed derivation | Normalized answer tokens versus dataset answer | see route | see route | see route | Diagnostic recording only | Lexical equality/overlap within normalization domain | Does not admit/reject/revise memory or next answer | see route | SRC-1, `musique_test_big.py` | [RT-CLM-memory-performance](runtime.md#rt-clm-memory-performance) | Metric is not explanation check | Derived count is warranted by code/input tokens, not truth of dataset answer. |
| [RT-RTE-graph-evaluation](runtime.md#rt-rte-graph-evaluation) | check/evidence production | doctrine only | [EPI-OBJ-outdated-triplets](#epi-obj-outdated-triplets) | no content change | Predicted removed facts versus environment-fact differences | see route | see route | Intended precision/recall | No working score consumer established | Intended diagnostic, not product acceptance | No production update/gate | see route | SRC-1, `pipeline_graph_evaluation.py` | [EPI-CLM-conservative-replacement](#epi-clm-conservative-replacement) | Executable defects | “Doctrine only” applies to functioning end-to-end scored validation; code fragments are present. |
| [EPI-RTE-reference-match](#epi-rte-reference-match) | check/evidence production | implemented | [EPI-OBJ-triplets](#epi-obj-triplets) | truth-apt transformation: entailed derivation | Exact membership in fixed cooking list | see route | see route | see route | Print diagnostic only | Set/list membership, not general extraction fidelity | No gate or later behavioral consumer | see route | SRC-1, `utils/retriever_search_drafts.py` | none | none | No shipped invocation established by scoped search. |
| [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update) | content transformation | implemented | [EPI-OBJ-thesises](#epi-obj-thesises) | truth-apt transformation: indeterminate | Text to thesis candidates | see route | see route | see route | Candidate production | Model fidelity unknown | Makes candidate theses available to update | see route | SRC-1, `graphs/hypergraph.py` | [EPI-CLM-concrete-extraction](#epi-clm-concrete-extraction) | Unformatted template | Literal placeholder plus appended input; not demonstrated compliance. |
| [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update) | check/evidence production | implemented | [EPI-OBJ-thesises](#epi-obj-thesises) | no content change | Existing versus new same-property claims | see route | see route | see route | Advisory model removal proposal | No independent truth evaluator | Supplies names to deletion | see route | SRC-1, `prompts/prompts.py` | [EPI-CLM-conservative-replacement](#epi-clm-conservative-replacement) | none | Requirement for a replacement is prompt policy. |
| [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update) | disposition/acceptance | implemented | [EPI-OBJ-thesises](#epi-obj-thesises) | no content change | Parsed names to removal | see route | see route | see route | Enforcing deletion/link cleanup | No epistemic acceptance of new thesis | Existing names removed without location guard | see route | SRC-1, `graphs/hypergraph.py` | [EPI-CLM-conservative-replacement](#epi-clm-conservative-replacement) | Replacement side ignored | No transaction/rollback or replacement existence check. |
| [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update) | retention | implemented | [EPI-OBJ-thesises](#epi-obj-thesises) | no content change | Candidates/events to dictionaries and links | see route | see route | see route | Local retention | Linked storage is not accepted-claim lifecycle integration | Later calls can retrieve theses/events | see route | SRC-1, `graphs/hypergraph.py` | none | none | Only API-level horizon established. |
| [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update) | operational admission/selection/consumption | implemented | [EPI-OBJ-thesises](#epi-obj-thesises) | no content change | Thesis/event scores to returned text | see route | see route | see route | Ranking and return | Relevance ordering only | Caller can receive subset | see route | SRC-1, `graphs/hypergraph.py` | none | Ascending event order | No planner/action consumer established. |
| [RT-RTE-summary-cycle](runtime.md#rt-rte-summary-cycle) | content transformation | implemented | [EPI-OBJ-summary](#epi-obj-summary) | truth-apt transformation: indeterminate | Observation/history/old summary to new account | see route | see route | see route | Whole-response assignment | Accuracy requested, not checked | New text is immediate decision context | see route | SRC-1, `pipeline_summary.py` | none | none | Summarization name alone cannot prove non-ampliative preservation. |
| [RT-RTE-summary-cycle](runtime.md#rt-rte-summary-cycle) | retention | implemented | [EPI-OBJ-summary](#epi-obj-summary) | no content change | Summary response to later summary/decision calls | see route | see route | see route | Ungated retention/use | No acceptance criterion implemented | Previous account shapes next update | see route | SRC-1, `pipeline_summary.py` | none | none | No semantic rollback. |
| [RT-RTE-full-history](runtime.md#rt-rte-full-history), [RT-RTE-smart-rag](runtime.md#rt-rte-smart-rag) | operational admission/selection/consumption | implemented | [EPI-OBJ-observation-text](#epi-obj-observation-text) | no content change | Retained observations/actions to decision context | see routes | see routes | see routes | Full delivery or ranked selection | History/relevance, not truth certification | Information and importance affect later decision inputs | see routes | SRC-1, `pipeline_smartrag.py` | none | none | Importance is an unvalidated policy score, not truth-apt world knowledge. |
| [RT-RTE-game-memory](runtime.md#rt-rte-game-memory), [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle) | lifecycle integration | no route found within boundary | [EPI-OBJ-triplets](#epi-obj-triplets) | no content change | Accepted proposition to evidence-linked organization/use | No prior evidence-consuming acceptance found in inspected updates | see routes for storage timing | No accepted-claim integration established | Storage/retrieval only | No added license | None distinct from pre-acceptance retention/use | see routes for actual memory use | SRC-1, `graphs/contriever_graph.py` | none | none | Bounded to these updates, not all possible external callers or model interiors. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-memory-performance](runtime.md#rt-clm-memory-performance) | see record | SRC-1, `README.md`; doctrine/design and reported operation | see record | see [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle), [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle) | Bounded supplied sequences, see routes; not aggregate replication | No independent intervention assessed; component effects not isolated | Memory-to-decision architecture wired; reported scores remain attributed | QA branch/configuration defects and uninspected aggregate evidence prevent reproduction and causal endorsement. |
| [EPI-CLM-concrete-extraction](#epi-clm-concrete-extraction) | see record | SRC-1, `prompts/prompts.py`; doctrine/design | see record | see [RT-RTE-game-memory](runtime.md#rt-rte-game-memory), [EPI-RTE-triplet-parsing](#epi-rte-triplet-parsing), [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update) | Supplied game/QA candidate sequences, not general fidelity checks | No source-fidelity intervention or semantic validator | Requests concrete facts and modal hypotheses; creates structured candidates | Parser accepts syntax, not source support or calibrated uncertainty. |
| [EPI-CLM-conservative-replacement](#epi-clm-conservative-replacement) | see record | SRC-1, `prompts/prompts.py`; doctrine/design | see record | see [RT-RTE-game-memory](runtime.md#rt-rte-game-memory), [EPI-RTE-removal-parsing](#epi-rte-removal-parsing), [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update) | Actual correctness of replacement unobserved in handed samples | Intended evaluator defective, see [RT-RTE-graph-evaluation](runtime.md#rt-rte-graph-evaluation); not a negative about all logs | Model judgment has operational withdrawal force, with exact-match and game-location guards | Replacement linkage/semantic criterion not enforced; QA does not invoke removal. |

## Bounded conclusion

AriGraph acquires external game/paragraph statements with **unknown source warrant**. Game preprocessing can omit text before memory receives it; QA directly supplies paragraph text. Its semantic store holds normalized extracted candidates, and its episodic store preserves the supplied text and fact associations. That is retention and later operational reliance, not by itself an evidence-consuming acceptance decision. See [EPI-RTE-observation-cleanup](#epi-rte-observation-cleanup), [RT-RTE-game-memory](runtime.md#rt-rte-game-memory), [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle).

The extraction prompts request faithful concrete facts and marked hypotheses. Model extraction, summary generation, spatial inference and answering remain **indeterminate transformations** at the semantic edge: no general checked entailment or positive demonstration of non-entailment is available for their outputs. Parsing/normalization are inspectable reshaping; they do not repair model meaning. Numerical similarity ranks relevance, not truth. Exact premises suffice to deduce the metrics computed on token lists and the fixed-reference membership count, but those deductions warrant only lexical results within the specified domain. See [EPI-RTE-triplet-parsing](#epi-rte-triplet-parsing), [EPI-RTE-answer-metrics](#epi-rte-answer-metrics), [EPI-RTE-reference-match](#epi-rte-reference-match).

The game maintenance model evaluates redundancy/conflict against selected old/new candidates. Its decision has **operational withdrawal authority** through the parser and graph deletion method. The criterion is requested same-aspect replacement with retention under uncertainty, intended for current game facts; no independent check establishes that the judgment is correct or that the named replacement exists. Exact old-item membership and location protection are enforcing guards, not semantic acceptance. QA's no-removal path is a counterexample to universal stale-fact reconciliation. Deleting a semantic fact does not delete all episodic text containing it. Hypergraph uses another removal path without the location guard and removes thesis links; its deployment and downstream decision consumer remain unestablished. See [EPI-RTE-removal-parsing](#epi-rte-removal-parsing), [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update).

Selected memory reaches later model user messages as informational context within one game attempt or QA task. Plans change priorities in retrieval/exploration/action requests, and graph paths directly dispatch multiple environment commands. These are consequential behavioral-authority paths, not evidence that models relied on each fact, that any explanation is warranted, or that retained changes improved capacity. Parse fallback blocks some malformed actions but not well-formed off-list commands. Environment score/completion assesses task outcomes, not correctness of every producing component or general transfer. See [RT-BAP-memory-decisions](runtime.md#rt-bap-memory-decisions), [RT-BAP-plan-decisions](runtime.md#rt-bap-plan-decisions), [RT-BAP-action-dispatch](runtime.md#rt-bap-action-dispatch).

QA metrics compare answers after generation to a local reference. Their only implemented consequence is diagnostic accumulation/logging; they do not reject memory, revise a plan or train a model. The fact-replacement evaluation script does not establish a working scored validation route. The separately exposed fixed-reference diagnostic prints membership, likewise without a later consequential consumer. Neither licenses a system-complete claim that no evaluation exists: task contents, remaining logs and external model interiors were not exhaustively assessed. See [EPI-RTE-answer-metrics](#epi-rte-answer-metrics), [RT-RTE-graph-evaluation](runtime.md#rt-rte-graph-evaluation), [EPI-RTE-reference-match](#epi-rte-reference-match).

No accepted ampliative claim or post-acceptance lifecycle integration is established by the inspected memory updates. Experience-fed writes and model-revised plans do establish a behavior-shaping pathway, independently of the unused named reflexion prompt. Learning benefit, content-directed theory criticism, reflective theory building and exercised self-improvement require separate evidence and are not inferred from memory replacement, static prompts or performance labels. Exact parametric contents, upstream weight identity and provider-internal updates are not determinable; wrapper inference paths alone do not settle those questions. See [RT-ABS-reflex-invocation](runtime.md#rt-abs-reflex-invocation), [RT-CMP-gpt-agent](runtime.md#rt-cmp-gpt-agent), [RT-CMP-retriever](runtime.md#rt-cmp-retriever), [RT-CMP-llama-agent](runtime.md#rt-cmp-llama-agent).

## Shared records

### Operative objects

#### EPI-OBJ-observation-text
Label: Observation and paragraph text

Part of: [RT-RTE-game-memory](runtime.md#rt-rte-game-memory)

This is the text-input part of that route, not its graph-update process. Source-native identity: `observation` passed to extraction; QA supplies `paragraph_text` to the same extraction API. Form: natural-language statements, alongside driver-added task/step text in the game. Substrate: Python strings. It overlaps the text inputs in [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle), not the answer or graph itself. Lineage and warrant: environment/fixture or dataset supplied, then game cleanup/annotation; truth of these inputs is not independently checked. SRC-1, `pipeline_arigraph.py`, `musique_test_big.py`.

> observation = observation.split("$$$")[-1]
> observation = observation_processing(observation)
> --- `pipeline_arigraph.py`

> triplets, episodic = graph.update_without_retrieve(text["paragraph_text"], [], log)
> --- `musique_test_big.py`

#### EPI-OBJ-triplets
Label: Triplets retained as semantic facts

Part of: [RT-RTE-game-memory](runtime.md#rt-rte-game-memory)

This is the retained semantic-content part of the route; supplied QA route shares the graph class but is a different caller. Source-native identity: `self.triplets`, with each normalized subject/object and label. Form: symbolic list/dictionary structure holding natural-language proposition labels; downstream models interpret serialized facts. Substrate: local Python list plus numerical embedding caches, which are not the proposition content. Lineage: model extraction and deterministic spatial additions. No independent acceptance event is stored. Distinct from [EPI-OBJ-episodic-text](#epi-obj-episodic-text): deletion/retrieval operate differently. SRC-1, `graphs/contriever_graph.py`.

> if triplet not in self.triplets:
>     self.triplets.append(triplet)
>     self.triplets_emb[self.str(triplet)] = self.get_embedding_local(self.str(triplet))
> --- `graphs/contriever_graph.py`

#### EPI-OBJ-episodic-text
Label: Episodic observation text

Part of: [RT-RTE-game-memory](runtime.md#rt-rte-game-memory)

Source-native identity: keys in `self.obs_episodic`, values carrying extracted-fact strings and observation embedding. Form: natural-language observation content, symbolic fact associations and separate dense numerical rank inputs. Substrate: Python dictionary and tensors; snapshots are local lists. This text-content part differs from graph facts because fact deletion does not withdraw the dictionary key or earlier text. Same class stores QA paragraphs, see [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle). Source warrant is unknown. SRC-1, `graphs/contriever_graph.py`.

> obs_embedding = self.retriever.embed(observation)
> obs_value = [new_triplets_str, obs_embedding]
> self.obs_episodic[observation] = obs_value
> --- `graphs/contriever_graph.py:77-79`

#### EPI-OBJ-outdated-triplets
Label: Parsed outdated triplets

Part of: [RT-RTE-game-memory](runtime.md#rt-rte-game-memory)

Source-native identity: `predicted_outdated`, derived from model-returned replacement text. Form: symbolic triplet targets naming natural-language facts, not retained justification or new fact identity. Substrate: temporary Python list and textual logs of original response. This is a material proposal part of the supplied update container, distinct from accepted replacements, which are not recorded as such. SRC-1, `graphs/contriever_graph.py`, `utils/utils.py`; passage see [EPI-RTE-removal-parsing](#epi-rte-removal-parsing).

#### EPI-OBJ-answer
Label: QA answer text

Part of: [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle)

Source-native identity: `answer` returned by `get_answer`. Form: natural-language explanation plus direct answer; no locally verified proof structure. Substrate: Python string and textual log. Lineage: question, retrieved facts/text and opaque model knowledge. Distinct from metrics and from the supplied route that generates/scores it. SRC-1, `musique_test_big.py`.

> answer = get_answer(agent_qa, question, subgraph, episodic)
> log("AGENT ANSWER: " + str(answer))
> log("TRUE ANSWER: " + str(task["answer"]))
> --- `musique_test_big.py`

#### EPI-OBJ-answer-metrics
Label: Answer metrics accumulators

Part of: [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle)

Source-native identity: `trueP`, `pred_len`, `true_len`, `EM`, aggregate `prec`, `rec`, `f1`, `em`. Form: symbolic numerical counts/ratios/equality decisions. Substrate: Python lists and computed scalars, rendered to logs. The metric object is distinct from answer text and dataset oracle. It carries lexical comparison results, not semantic acceptance. SRC-1, `musique_test_big.py`; passage see [EPI-RTE-answer-metrics](#epi-rte-answer-metrics).

#### EPI-OBJ-thesises
Label: Hypergraph theses and events

Part of: [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update)

Source-native identity: `self.thesises`, `self.events`, linked `self.entities`. Form: natural-language thesis/event names, symbolic hash-indexed parent/child links, and distinct numerical embeddings. Substrate: Python dictionaries/object fields. This is the retained content part of the supplied route, not a duplicate route or an established planner consumer. Event text is retained alongside generated claims; thesis deletion changes links but retains event objects. SRC-1, `graphs/hypergraph.py`.

> if event_id not in self.events:
>     self.events[event_id] = Event(event, event_emb, thesises_ids)
> else:
>     self.events[event_id].add_children(thesises_ids)
> --- `graphs/hypergraph.py`

#### EPI-OBJ-summary
Label: Summary baseline text

Part of: [RT-RTE-summary-cycle](runtime.md#rt-rte-summary-cycle)

Source-native identity: `summary`, model-replaced situation account. Form: natural-language compressed statements and strategic guidance; substrate: Python string/logs. Lineage: prior summary, observations/history and model output; preserved meaning unresolved. Different checks/consumers from semantic triplets. Supplied route supplies direct assignment and return passages; this object is its text part, not a second summary process. SRC-1, `pipeline_summary.py`, `prompts/system_prompts.py`; evidence see supplied route.

### Routes

#### EPI-RTE-observation-cleanup
Label: Game observation cleanup

Part of: [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle)

Endpoints: environment feedback → delimiter stripping → `observation_processing` → step/task annotation → extraction/decision context. Owner: game driver and deterministic helper. SRC-1, `pipeline_arigraph.py`, `utils/utils.py`. Distinct part of the supplied container, not its entire environment/decision cycle. Concrete source deduction, without target execution: `Room contains apple > take apple` becomes `Room contains apple ` because `>.*$` under DOTALL removes the suffix. A statement after that marker also disappears; hence cleanup does not establish full source-content preservation. Renaming `Recipe #1` to `Recipe` also collapses identity under a task-local alias assumption.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Cleaned natural-language string, then driver annotations.
- Later read-back: Cleaned text is retained in graph episodes/recent history for later model invocations, not the removed suffix.
- Delegated visibility: inapplicable — local synchronous preprocessing.
- Selection predicate: Suffix after last `$$$`; regex suffix removal from `>`; literal spelling substitutions.
- Invalidation or expiry: Original omitted text is not restored by this function; attempt history/reset bounds later use.
- Activation or effect: Changes the available text delivered to extraction and decisions; individual behavioral effect unobserved.
- Evidence limits: Deterministic deduction establishes text loss, not that omitted text is materially true or false in an observed task.

> pattern = r">.*$"
> cleaned_text = re.sub(pattern, "", text, flags=re.DOTALL)
> --- `utils/utils.py`

#### EPI-RTE-triplet-parsing
Label: Triplet parsing and normalization

Part of: [RT-RTE-game-memory](runtime.md#rt-rte-game-memory)

Endpoints: extraction response → `process_triplets` → `clear_triplet` → duplicate-aware `add_triplets`. Owner: helper and graph code. QA invokes the same functions. SRC-1, `utils/utils.py`, `graphs/contriever_graph.py`. This is the syntactic transformation/admission part, not a semantic evaluator. Concrete deduction: `Apple, is in, I; bad` yields one structured candidate `['Apple', 'I', {'label': 'is in'}]`; `bad` fails the three-comma-field requirement. `clear_triplet` maps exact `I` to `inventory` and lowercases names, yielding `['apple', 'inventory', {'label': 'is in'}]`. A lowercase `i` is not that exact alias before lowercasing. No execution was used. Normalized identity assumes case is immaterial and aliases refer to the same entity; otherwise fidelity can degrade.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed list, then normalized candidates and local insertions.
- Later read-back: Inserted fact strings become later retrieval candidates and model context.
- Delegated visibility: inapplicable — local parsing and graph mutation.
- Selection predicate: Exactly three comma-separated fields, nonempty trimmed values; `free` relation skipped before normalization; normalized duplicate membership checked.
- Invalidation or expiry: Malformed fragments omitted; stored fact survives until matching deletion or reset.
- Activation or effect: Enforces shape/identity admission and determines later candidate population, not factual truth.
- Evidence limits: Commas/colons inside content can change parsing; semantic interpretation and source fidelity are not checked.

Proposer: extraction model; computational decider: parser/adder; human: initial prompts/configuration only. Veto: malformed/empty fragments and exact duplicate/`free` checks. Oracle: none. Mode: bounded attempt/task. Trigger/change: each supplied text; guidance requests concrete structured knowledge and marked hypotheses. Admission is immediate; no semantic rollback, reset is recovery. What persists: normalized facts, not rationale or evidence-consuming acceptance.

> if len(triplet.split(",")) != 3:
>     continue
> --- `utils/utils.py:26-40`

> if triplet[0] == "I":
>     triplet = ("inventory", triplet[1], triplet[2])
> if triplet[1] == "I":
>     triplet = (triplet[0], "inventory", triplet[2])
> --- `utils/utils.py`

#### EPI-RTE-removal-parsing
Label: Replacement proposal to deletion

Part of: [RT-RTE-game-memory](runtime.md#rt-rte-game-memory)

Endpoints: model replacement response → `parse_triplets_removing` → exact old-target list → `delete_triplets`. Owner: helper and ContrieverGraph. SRC-1, `utils/utils.py`, `graphs/contriever_graph.py`. This is disposition of proposed removal targets, distinct from the model comparison and new-fact insertion phases of the supplied route.

Concrete implementation deduction: `[[apple, is in, room -> nonsense]]` passes the arrow/two-side and left-three-field tests and returns the old `apple`/`room`/`is in` target. The parser never validates `nonsense` or checks it against incoming candidates. If that old triplet exists and both endpoints are not protected locations, the deletion method removes it. This counterexample defeats a local invariant that a justified new replacement must be installed before withdrawal. No target execution is needed.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Parsed old-target list; deletion mutates triplets/cache without a returned acceptance record.
- Later read-back: Remaining facts reach later retrieval; withdrawn facts no longer do through the semantic store, while associated episodic text can survive.
- Delegated visibility: inapplicable — local model response consumption.
- Selection predicate: Arrow pair and three left-side fields; exact existing triplet membership; skip when both endpoints belong to supplied locations.
- Invalidation or expiry: Removes matched facts and their fact embeddings; reset clears local stores; no transactional restoration.
- Activation or effect: Software-enforced withdrawal changes the later candidate pool; correctness/benefit unobserved.
- Evidence limits: Replacement meaning and existence unverified; protected or nonmatching targets survive; original text logged is not an acceptance rationale consumed later.

Proposer: maintenance model. Decider/veto: code membership and location guard, no per-item human approval. Oracle: none. Operating mode: within-game maintenance. Trigger: new facts; guidance: conservative same-aspect duplication/conflict, retaining uncertainty. Proposed change: replace old facts; operative result: delete named old targets and separately add extraction outputs. Recovery: attempt reset only, not semantic rollback. Persistence: altered fact pool, not validated old→new lineage.

> splitted_pair = pair.split("->")
> if len(splitted_pair) != 2:
>     continue
> first_triplet = splitted_pair[0].split(",")
> --- `utils/utils.py`

> if triplet[0] in locations and triplet[1] in locations:
>     continue
> if triplet in self.triplets:
>     self.triplets.remove(triplet)
>     self.triplets_emb.pop(self.str(triplet))
> --- `graphs/contriever_graph.py`

#### EPI-RTE-answer-metrics
Label: QA answer lexical scoring

Part of: [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle)

Endpoints: answer/reference → direct-answer suffix → lowercasing/punctuation trimming/token lists → set-valued matching-word count and list equality → aggregate ratios/logging. Owner: QA driver. SRC-1, `musique_test_big.py`. This evaluator part differs from answer generation and paragraph admission in the supplied route. Target/domain: lexical correspondence of direct answer to dataset reference under these exact normalization rules, not reasoning validity or premise truth.

Concrete deduction: reference `a a` and candidate direct answer `a a` yield equality true and `true_P = 1` while both token lengths are 2. Thus even exact normalized equality does not entail an overlap ratio of one for repeated tokens. This bounds the interpretation of the script's precision/recall/F1 labels. Missing `Direct answer:` leaves the whole response as the candidate suffix. Empty totals can produce invalid numerical ratios; no guard is implemented.

- implementation conclusion status: wired
- operation conclusion status: observed
- Immediate return: No returned score object; appends counts/equality and logs running aggregates.
- Later read-back: inapplicable — accumulators feed aggregate diagnostics, not later answer/memory requests.
- Delegated visibility: inapplicable — local scoring, not worker feedback.
- Selection predicate: Last direct-answer delimiter, exact normalized token membership/equality; no semantic-equivalence evaluator.
- Invalidation or expiry: Lists initialized per run; no revision/removal of prior metric entries.
- Activation or effect: Metrics affect running diagnostic output only; no successor-selection or memory gate.
- Evidence limits: Observed status is limited to the attributed QA sequence quoted in the supplied route; fresh operation/configuration and aggregate correctness uninspected.

Proposer: answer model; metric evaluator: code; oracle: local `task['answer']`, consumed only after generation, not given to the answer producer. Human contribution: dataset/configuration, not per-answer adjudication. Mode: bounded evaluation batch. No metric-fed improvement trigger, revision admission, rejection or rollback is wired. Explanation and evidence-truth targets remain outside the lexical check's license.

> true_P = len({word for word in answer if word in true_answer})
> trueP.append(true_P), pred_len.append(len(answer)), true_len.append(len(true_answer))
> EM.append(answer == true_answer)
> --- `musique_test_big.py`

#### EPI-RTE-reference-match
Label: Fixed cooking reference diagnostic

Source-native identity: callable `eval_triplets` in `utils/retriever_search_drafts.py`. No counterpart after comparison with supplied [RT-RTE-graph-evaluation](runtime.md#rt-rte-graph-evaluation): this counts fixed-string membership, whereas that route intends before/after environment removal scoring. Endpoints: caller triplet strings → hardcoded `reference_full` membership list → printed count. Owner: helper function; context/state: cooking reference list and supplied candidate list. SRC-1, `utils/retriever_search_drafts.py`.

- implementation conclusion status: afforded
- operation conclusion status: uninspected
- Immediate return: Printed `Found` count; no returned evaluation or mutated graph.
- Later read-back: inapplicable — no installed result or later consumer identified in scoped callers.
- Delegated visibility: inapplicable — local helper diagnostic.
- Selection predicate: Exact string membership for each reference entry; list contains repeated reference strings, so count is entry-weighted rather than unique-fact coverage.
- Invalidation or expiry: Temporary list/count discarded after call; fixed references remain source constants.
- Activation or effect: Diagnostic printing only; no consequential admission or behavioral gate found.
- Evidence limits: No root/helper call found by scoped `eval_triplets` search; neither actual execution nor completeness/truth of the reference list independently assessed.

Target: membership of reference strings in the caller's triplet list. Evaluator: Python membership; oracle: author-supplied cooking string list. Proposer: external caller supplies candidates; human authored references. Mode: standalone diagnostic, not a feedback optimization loop. Trigger: explicit call; no installed change, rejection or rollback. A concrete deduction: passing an empty list yields all zeros and printed zero coverage, without establishing why facts were absent or whether extraction failed.

> is_found = [int(r in triplets) for r in reference_full]
> print(f"Found {sum(is_found)}/{len(is_found)} from reference_full")
> --- `utils/retriever_search_drafts.py`

### Claims

#### EPI-CLM-concrete-extraction
Label: Concrete knowledge and hypothesis marking

Claimed operation: extraction organizes concrete knowledge from input into triplets or thesis sentences, marking assumptions as hypotheses. Source: SRC-1, `prompts/prompts.py`, doctrine/design. Distinct from [RT-CLM-memory-performance](runtime.md#rt-clm-memory-performance): a content-production policy, not a comparative outcome claim. No equivalent supplied claim record after comparison.

> Length of your triplet should not be more than 7 words. You should extract only concrete knowledges, any assumptions must be described as hypothesis.
> --- `prompts/prompts.py`

#### EPI-CLM-conservative-replacement
Label: Conservative same-aspect replacement

Claimed operation: preserve distinct/complementary facts and uncertain old facts; replace only redundant/conflicting same-aspect facts. Hypergraph additionally requests an identifiable newer replacement. Source: SRC-1, `prompts/prompts.py`, doctrine/design. Distinct from [RT-CLM-memory-performance](runtime.md#rt-clm-memory-performance); related implementation container is [RT-RTE-game-memory](runtime.md#rt-rte-game-memory), not another claim declaration.

> If there is uncertainty about whether a triplet should be replaced, prioritize retaining the existing triplet over replacing it.
> --- `prompts/prompts.py`

> For every thesis you want to replace you must find replacement from new thesises. If there is no clear replacement, you must not replace existing thesis.
> --- `prompts/prompts.py`
