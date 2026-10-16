---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Dynamic Cheatsheet's candidate generation, model-requested verification, unchecked reference admission and bounded benchmark evaluators."
run-id: AAS-2026-10-12-dynamic-cheatsheet-ca0a0b29d273-01
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
---

# Dynamic Cheatsheet epistemic report

## Source-and-claim boundary

The question is whether inference-time reference updates acquire or produce warranted content, rather than merely change later model context. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); evidence identities and layers are see its [Source register](boundary.md#source-register). The shipped driver, library, prompts, provider client and notebook consumers belong to the boundary. Provider internals, remote dataset bytes and the uncaptured paper do not supply evidence here.

All direct reads below use SRC-1 at the frozen revision. Supplied runtime records remain provisional but their core routes agree with the inspected source. No supersession is needed. Direct reads support implementation or doctrine/design, not observed activation. No model, benchmark or target code was executed.

| Entry point or operation | Source path | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| CLI dispatch, initialization, dataset import, checkpoint, resume and online scoring | `run_benchmark.py` | Direct full read; see [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation), [RT-RTE-answer-scoring](runtime.md#rt-rte-answer-scoring) | Initial file authorship, target truth and exact dataset/embedding provenance unresolved; no imported-warrant claim |
| Six advanced generation branches; local/native execution dispatch | `dynamic_cheatsheet/language_model.py` | Direct full read; see [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation), [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), [EPI-RTE-answer-generation](#epi-rte-answer-generation) | Actual candidate content and compliance not inspected |
| Delimiter extraction, including unused solution-evaluation extraction | `dynamic_cheatsheet/utils/extractor.py` | Direct full read; see [EPI-RTE-reference-admission](#epi-rte-reference-admission) | Extracting a section is not evaluating its assertions; no consumer of extract_solution in inspected driver/library |
| All three shipped model prompts | `prompts/generator_prompt.txt`, `prompts/curator_prompt_for_dc_cumulative.txt`, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt` | Direct full reads; see [EPI-CLM-verified-solutions](#epi-clm-verified-solutions) and runtime curation/context records | Requested correctness, usage counts and provenance references not enforced |
| Local code extraction, print adjustment, subprocess, output and cleanup | `dynamic_cheatsheet/utils/execute_code.py` | Direct full read; see [RT-RTE-local-execution](runtime.md#rt-rte-local-execution) | Actual execution/result fidelity and semantic problem encoding unobserved |
| Active task scorers and exposed auxiliary puzzle/checkmate/soft-match scorers | `dynamic_cheatsheet/utils/evaluation.py` | Direct full read; see [RT-RTE-answer-scoring](runtime.md#rt-rte-answer-scoring), [EPI-RTE-choice-scoring](#epi-rte-choice-scoring) | Auxiliary evaluators not dispatched by shipped benchmark; no complete evaluator-validity conclusion |
| Retained-output scoring and repeated-problem example | `EvaluatingResults.ipynb`, `ExampleUsage.ipynb` | Direct source-cell reads; see runtime scoring/checkpoint records | Saved outputs not inspected; source comments do not establish success |
| Client generate/chat/history, Tavily, native search, citation logging, provider text projection and native code | `text_generation/simple_unified_client.py` | Direct reads of methods from _web_search through generate_from_messages, citation extraction, all provider generation methods, native code methods and chat/history methods; see [EPI-RTE-search-acquisition](#epi-rte-search-acquisition), [EPI-RTE-chat-history](#epi-rte-chat-history) | Tool configuration helpers and initialization rely on supplied runtime/findings and source search rather than a complete direct audit; remote tool internals remain opaque |
| Auxiliary sonnet evaluation | `dynamic_cheatsheet/utils/sonnet_eval.py` | Direct entry-point/doctrine read, lines 1–85; evaluation.py comments out its import | Rhyme/syllable helper internals unassessed; prevents system-complete negative about all evaluation routes |
| Knowledge-production and improvement claims | `README.md` | Direct overview, features, performance and usage reads; see [RT-CLM-adaptive-memory](runtime.md#rt-clm-adaptive-memory), [EPI-CLM-zero-shot](#epi-clm-zero-shot) | Full result payloads, comparisons and experimental controls uninspected; benefit and component attribution not established |
| Task/embedding/result payloads | `data/`, `embeddings/`, `results/` | Supplied boundary inventory only | No content-level provenance, leakage, transfer or observed acceptance conclusion |

This coverage does not authorize a system-complete absence verdict. The bounded negative is that the inspected driver/library update and reload paths do not use the benchmark score to veto reference admission. The separate public client search routes are included below rather than mistaken for an excluded host.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-final-output](#epi-obj-final-output) | see record | see record | SRC-1, `dynamic_cheatsheet/language_model.py` | Particular answers, explanations and code truth unassessed |
| [EPI-OBJ-final-answer](#epi-obj-final-answer) | see record | see record | SRC-1, `dynamic_cheatsheet/utils/extractor.py` | Extraction can change selected answer without checking it |
| [EPI-OBJ-final-cheatsheet](#epi-obj-final-cheatsheet) | see record | see record | SRC-1, `dynamic_cheatsheet/language_model.py` | Strategies can mix propositions and non-truth-apt instructions; no instance classification |
| [EPI-OBJ-target](#epi-obj-target) | see record | see record | SRC-1, `run_benchmark.py` | Imported target warrant unknown |
| [EPI-OBJ-curator-prompt](#epi-obj-curator-prompt) | see record | see record | SRC-1, `prompts/curator_prompt_for_dc_cumulative.txt` | Instructions and warrant claims are requested, not enforced |
| [EPI-OBJ-synthesis-prompt](#epi-obj-synthesis-prompt) | see record | see record | SRC-1, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt` | Effectiveness judgment and preservation unobserved |
| [RT-OBJ-generator-prompt](runtime.md#rt-obj-generator-prompt) | Instructions, chiefly not truth-apt claims | see record | SRC-1, `prompts/generator_prompt.txt` | Requested verification not evidence of verification |
| [RT-CMP-language-model](runtime.md#rt-cmp-language-model) | not determinable from accessible weights | see record | SRC-1, `dynamic_cheatsheet/language_model.py` | Latent propositions cannot be individuated; no weight-training conclusion beyond inspected calls |
| [RT-CMP-input-embeddings](runtime.md#rt-cmp-input-embeddings) | Similarity representation, not explicit truth claims | see record | SRC-1, `run_benchmark.py` | Ranking warrant is numerical similarity, not solution correctness |
| [EPI-OBJ-search-results](#epi-obj-search-results) | see record | see record | SRC-1, `text_generation/simple_unified_client.py` | Source content and reliability unknown; URLs are not endorsement |
| [EPI-OBJ-messages](#epi-obj-messages) | see record | see record | SRC-1, `text_generation/simple_unified_client.py` | Chat state is separate from externally managed LanguageModel history |

Local code output is a material evidential part of final_output, not a separate retained tool artifact: see [RT-RTE-local-execution](runtime.md#rt-rte-local-execution). It includes stdout or failure text. Provider-native result text has the separate opaque projection boundary in [RT-RTE-native-execution](runtime.md#rt-rte-native-execution).

## Authority-route ledger

Rows separate checking, admission, retention and later consumption even where one supplied route record spans them. Fields owned by those records are referenced rather than redeclared. Relation judgments are local assessments of the cited implementation. Model-generated semantics remain indeterminate: a call can copy, derive or invent, and the accessible call site cannot choose among those cases.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [EPI-RTE-answer-generation](#epi-rte-answer-generation) | content transformation | implemented | [EPI-OBJ-final-output](#epi-obj-final-output) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | Candidate answer, no independent truth license | see record | see record | SRC-1, `dynamic_cheatsheet/language_model.py` | [RT-CLM-adaptive-memory](runtime.md#rt-clm-adaptive-memory) | none | Copy, derivation or conjecture not distinguishable without content |
| [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation), [RT-RTE-context-selection](runtime.md#rt-rte-context-selection) | content transformation | implemented | [EPI-OBJ-final-cheatsheet](#epi-obj-final-cheatsheet) | truth-apt transformation: indeterminate | Curator successor proposal; see records | see records | see records | see records | see records | No established entailed derivation or accepted ampliative claim | see records | see [RT-BAP-curator-guidance](runtime.md#rt-bap-curator-guidance) | SRC-1, `dynamic_cheatsheet/language_model.py` | [EPI-CLM-verified-solutions](#epi-clm-verified-solutions) | Requested verification exceeds observed warrant | Content-level evidence would distinguish reshaping, derivation and non-entailing generalization |
| [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation) | check/evidence production | doctrine only | [EPI-OBJ-final-output](#epi-obj-final-output) | no content change | Solution correctness before updating | see record | see record | see record | Model-facing request only | Requested accuracy/effectiveness assessment, not independently established acceptance | see record | see [RT-BAP-curator-guidance](runtime.md#rt-bap-curator-guidance) | SRC-1, `prompts/curator_prompt_for_dc_cumulative.txt` | [EPI-CLM-verified-solutions](#epi-clm-verified-solutions) | No recorded evidence-consuming semantic decision inspected | Sending a check instruction is implemented; performance of the check is doctrine only |
| [EPI-RTE-reference-admission](#epi-rte-reference-admission) | disposition/acceptance | implemented | [EPI-OBJ-final-cheatsheet](#epi-obj-final-cheatsheet) | no content change | see record | see record | see record | see record | see record | Delimiter admission only; not epistemic acceptance | see record | see record | SRC-1, `dynamic_cheatsheet/utils/extractor.py` | [EPI-CLM-verified-solutions](#epi-clm-verified-solutions) | Semantic warrant is not an admission condition | Empty or unclosed tagged text can replace prior reference |
| [RT-RTE-context-selection](runtime.md#rt-rte-context-selection) | content transformation | implemented | [EPI-OBJ-final-output](#epi-obj-final-output) | truth-apt transformation: non-ampliative reshaping | Pair selection and labelled assembly, not model synthesis | see record | see record | see record | see record | Preserves selected strings, not their correctness | see record | see [RT-BAP-cheatsheet-context](runtime.md#rt-bap-cheatsheet-context) | SRC-1, `dynamic_cheatsheet/language_model.py` | none | none | Selection omits other pairs; labels and similarity do not license truth |
| [RT-RTE-context-selection](runtime.md#rt-rte-context-selection) | operational admission/selection/consumption | implemented | [EPI-OBJ-final-cheatsheet](#epi-obj-final-cheatsheet) | no content change | see record | see record | see record | see record | see record | Relevance ranking only, not correctness ranking | see record | see [RT-BAP-cheatsheet-context](runtime.md#rt-bap-cheatsheet-context) | SRC-1, `dynamic_cheatsheet/language_model.py` | none | none | Direct retrieval and full-history bypass curator checks |
| [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation) | retention | implemented | [EPI-OBJ-final-cheatsheet](#epi-obj-final-cheatsheet), [EPI-OBJ-final-output](#epi-obj-final-output) | no content change | see record | see record | see record | see record | see record | Retention licenses no truth claim | see record | see record | SRC-1, `run_benchmark.py` | [RT-CLM-adaptive-memory](runtime.md#rt-clm-adaptive-memory) | none | Save after scoring still saves candidates regardless of score |
| [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation) | lineage/freshness/recovery | implemented | [EPI-OBJ-final-cheatsheet](#epi-obj-final-cheatsheet) | no content change | see record | see record | see record | see record | see record | Argument equality is not endorsement or exact replay | see record | see record | SRC-1, `run_benchmark.py` | none | none | Changed prompt bytes, curator configuration and data order not fully guarded |
| [RT-BAP-cheatsheet-context](runtime.md#rt-bap-cheatsheet-context) | operational admission/selection/consumption | implemented | [EPI-OBJ-final-cheatsheet](#epi-obj-final-cheatsheet) | no content change | Reference delivery to solving | see record | see record | see record | see record | Advisory reference use, not enforced truth | see record | see record | SRC-1, `prompts/generator_prompt.txt` | [RT-CLM-adaptive-memory](runtime.md#rt-clm-adaptive-memory) | none | Model reliance and benefit unobserved |
| [RT-RTE-local-execution](runtime.md#rt-rte-local-execution) | check/evidence production | implemented | [EPI-OBJ-final-output](#epi-obj-final-output) | truth-apt transformation: indeterminate | Model-selected Python, not automatically a complete solution test | see record | see record | see record | see record | Bounded computational outcome evidence if exercised; no problem-encoding or transfer license | see record | see record | SRC-1, `dynamic_cheatsheet/utils/execute_code.py` | none | none | stdout can mask nonempty stderr when stdout exists; self-reported output is not a proof |
| [RT-RTE-native-execution](runtime.md#rt-rte-native-execution) | check/evidence production | implemented | [EPI-OBJ-final-output](#epi-obj-final-output) | truth-apt transformation: indeterminate | Provider tool-enabled answer, inner test domain uninspected | see record | see record | see record | see record | Opaque tool result, no independently inspected correctness acceptance | see record | see record | SRC-1, `text_generation/simple_unified_client.py` | none | none | Text projection does not retain a complete execution/evidence envelope |
| [RT-RTE-answer-scoring](runtime.md#rt-rte-answer-scoring) | check/evidence production | implemented | [EPI-OBJ-final-answer](#epi-obj-final-answer), [EPI-OBJ-target](#epi-obj-target) | no content change | Game of 24: expression value and number multiset | see record | see record | see record | see record | Numeric tolerance plus token-use predicate, not process correctness | see record | see record | SRC-1, `dynamic_cheatsheet/utils/evaluation.py` | [EPI-CLM-zero-shot](#epi-clm-zero-shot) | none | Operator grammar not restricted before eval; no reference-update veto |
| [RT-RTE-answer-scoring](runtime.md#rt-rte-answer-scoring) | check/evidence production | implemented | [EPI-OBJ-final-answer](#epi-obj-final-answer), [EPI-OBJ-target](#epi-obj-target) | no content change | AIME: normalized target string | see record | see record | see record | see record | Target-string match only; target truth and derivation not checked | see record | see record | SRC-1, `dynamic_cheatsheet/utils/evaluation.py` | [EPI-CLM-zero-shot](#epi-clm-zero-shot) | none | Online normalization differs from notebook; no curator veto |
| [RT-RTE-answer-scoring](runtime.md#rt-rte-answer-scoring) | check/evidence production | implemented | [EPI-OBJ-final-answer](#epi-obj-final-answer), [EPI-OBJ-target](#epi-obj-target) | no content change | Equation balancing: numeral format and value tolerance | see record | see record | see record | see record | Expression/target-value agreement within tolerance; no explanation license | see record | see record | SRC-1, `dynamic_cheatsheet/utils/evaluation.py` | [EPI-CLM-zero-shot](#epi-clm-zero-shot) | none | Format predicate precedes eval; no curator veto |
| [EPI-RTE-choice-scoring](#epi-rte-choice-scoring) | check/evidence production | implemented | [EPI-OBJ-final-answer](#epi-obj-final-answer) | no content change | see record | see record | see record | see record | see record | Answer-format/substring predicate, not semantic entailment | see record | see record | SRC-1, `dynamic_cheatsheet/utils/evaluation.py` | [EPI-CLM-zero-shot](#epi-clm-zero-shot) | Predicate can accept a negated target text | Concrete counterexample in record; accuracy cannot validate curation |
| [EPI-RTE-search-acquisition](#epi-rte-search-acquisition) | content transformation | implemented | [EPI-OBJ-search-results](#epi-obj-search-results) | truth-apt transformation: acquisition/import | Tavily snippet import; see record | see record | see record | see record | see record | External warrant unknown; title/URL/snippet retained as text | see record | see record | SRC-1, `text_generation/simple_unified_client.py` | none | none | Query results are context, not source endorsement |
| [EPI-RTE-search-acquisition](#epi-rte-search-acquisition) | content transformation | implemented | [EPI-OBJ-search-results](#epi-obj-search-results) | truth-apt transformation: indeterminate | Native searched generation and text projection; see record | see record | see record | see record | see record | External source warrant unknown; structured citation lineage degraded on text projection | see record | see record | SRC-1, `text_generation/simple_unified_client.py` | none | none | Native imported inputs, derivations and conjectures not individually distinguishable |
| [EPI-RTE-chat-history](#epi-rte-chat-history) | retention | implemented | [EPI-OBJ-messages](#epi-obj-messages) | no content change | see record | see record | see record | see record | see record | Conversation retention is not acceptance | see record | see record | SRC-1, `text_generation/simple_unified_client.py` | none | none | No semantic invalidation; reset/set replaces state |
| [EPI-RTE-chat-history](#epi-rte-chat-history) | operational admission/selection/consumption | implemented | [EPI-OBJ-messages](#epi-obj-messages) | no content change | see record | see record | see record | see record | see record | Prior turns are contextual material only | see record | see record | SRC-1, `text_generation/simple_unified_client.py` | none | none | Not used by benchmark generate_from_messages |

Implementation evidence for the local-output license limit:

> captured_output = stdout.decode().strip()
> error_output = stderr.decode().strip()
>
> if captured_output == "":
>     if error_output != "":
>         captured_output = f"Error in execution: {error_output}"
> --- `dynamic_cheatsheet/utils/execute_code.py`

Lifecycle integration: no route found within boundary of the inspected driver/library reference updates and reloads **after evidence-consuming acceptance**. Organizing candidate text is requested and context installation is implemented, but neither establishes prior acceptance. This is not a negative about inaccessible provider reasoning or the unassessed sonnet helpers. Non-truth-apt behavioral heuristics can travel alongside propositions through the same advisory context path; their effects are likewise unobserved.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-adaptive-memory](runtime.md#rt-clm-adaptive-memory) | see record | SRC-1, `README.md`; doctrine/design and reported operation | see record | [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation), [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation) | see record | see record | Installed reference can reach later calls without an explicit local weight update | Reduced mistakes, generalization and improved capacity remain unestablished |
| [EPI-CLM-verified-solutions](#epi-clm-verified-solutions) | see record | SRC-1, `prompts/curator_prompt_for_dc_cumulative.txt`; doctrine/design | see record | [EPI-RTE-reference-admission](#epi-rte-reference-admission), [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation) | none inspected | No specific solution check/acceptance trace; benchmark scorer runs downstream | Verification is a model-facing responsibility; reference admission is syntactic | “Verified” cannot be assigned to every retained item |
| [EPI-CLM-zero-shot](#epi-clm-zero-shot) | see record | SRC-1, `README.md`; doctrine/design and reported operation | see record | [RT-RTE-answer-scoring](runtime.md#rt-rte-answer-scoring), [EPI-RTE-choice-scoring](#epi-rte-choice-scoring), [EPI-RTE-reference-admission](#epi-rte-reference-admission) | Full results not inspected | No frozen intervention/comparison assessed; no curator, tool or retrieval component attribution | Driver keeps labels out of curator/generator update context, while using them for measurement | Label-free updating is not label-free evaluation; improvement figures not independently warranted here |

## Bounded conclusion

Dynamic Cheatsheet implements answer-fed model curation and immediate installation of extracted reference text. The old reference and generated solution reach the update consumer; the replacement reaches subsequent solving through a user-message reference channel. See [RT-BAP-curator-guidance](runtime.md#rt-bap-curator-guidance), [RT-BAP-cheatsheet-context](runtime.md#rt-bap-cheatsheet-context) and [EPI-RTE-reference-admission](#epi-rte-reference-admission). This is operational authority without established epistemic acceptance. A tagged candidate, even empty or unclosed, can supersede prior text before scoring. Missing opening tags retain the old text or retrieved fallback; that is formatting rejection, not correctness rejection.

Direct retrieval and full-history modes reuse prior full responses without model curation. Cosine selection licenses similarity priority, not truth. Curator synthesis may preserve propositions, deduce new ones or conjecture broader strategies; no particular transformation is established from the call sites. A deterministic extraction does establish a non-ampliative substring operation, as the concrete trace in [EPI-RTE-reference-admission](#epi-rte-reference-admission) shows. No checked derivation from warranted premises or produced accepted ampliative claim is established in the inspected reference loop.

Imported task targets and caller initialization text have unresolved source warrant. Optional client search acquires externally supplied snippets with visible URLs, while native provider text projection can omit structured citation metadata. See [EPI-RTE-search-acquisition](#epi-rte-search-acquisition). Import, retrieval and fluent synthesis do not add warrant. Disk checkpoints preserve candidates and reconnect them to later calls without reevaluation; argument checks support a limited continuation protocol, not freshness endorsement or exact replay.

Local execution can produce computational evidence and error feedback, but its code is model-selected and transformed before execution. Its license does not extend to correctness of problem encoding, explanation, transfer or reference admission. Native tools have an independently opaque evaluator boundary. Task scorers check narrow predicates and print counts, not proposed reference content. The multiple-choice counterexample in [EPI-RTE-choice-scoring](#epi-rte-choice-scoring) limits even the semantic reading of a score. None of these results is a wired curator correctness veto in the inspected driver.

The claimed future-capacity pathway has reference updating, persistence and a live advisory consumption channel. Exercised learning and successful self-improvement remain unestablished without content-dependent outcome and attribution evidence; reported performance does not identify a curator or memory component effect. Reflection and autonomous theory-building are separately unresolved: requested localized strategies and iteration wiring do not demonstrate content-directed criticism, criticism-result reuse or method-text revision. See [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation) and [RT-RTE-context-selection](runtime.md#rt-rte-context-selection). Provider weights remain uninspected; no remote parametric-state verdict follows from the absence of a local training call. These are independent route limits, not one epistemic score.

## Shared records

### Operative objects

#### EPI-OBJ-curator-prompt
Label: Cumulative curator template

Source-native identity: curator_prompt_for_dc_cumulative template. Representational form: natural-language instructions with literal placeholders substituted by the wrapper. Storage substrate: shipped text, loaded string and model user message. Claimed role: correctness assessment, reusable-strategy selection, refinement, preservation and usage counts. Candidate truth-apt content: claims about verified/effective solutions and any instantiated prior-reference/answer propositions; most static content is policy rather than a factual candidate. No supplied object counterpart: [RT-OBJ-generator-prompt](runtime.md#rt-obj-generator-prompt) is the solving template, while [RT-BAP-curator-guidance](runtime.md#rt-bap-curator-guidance) is this template's authority path, not the text object. SRC-1, `prompts/curator_prompt_for_dc_cumulative.txt`; doctrine/design. Its warranty claim is see [EPI-CLM-verified-solutions](#epi-clm-verified-solutions); correctness request evidence is see [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation).

> Each entry must include a usage count: Increase the count every time a strategy is successfully used in problem-solving.
> --- `prompts/curator_prompt_for_dc_cumulative.txt`

#### EPI-OBJ-synthesis-prompt
Label: Retrieval synthesis template

Source-native identity: curator_prompt_for_dc_retrieval_synthesis template. Representational form: natural-language update instructions with substituted selected pairs, prior reference and next question. Storage substrate: shipped text and model user message. Claimed role: task-suited synthesis, effectiveness assessment, removal of weak strategies, generalization and preservation. Candidate truth-apt content: instantiated strategy/example assertions; optimization instructions are not themselves factual candidates. Distinct from [EPI-OBJ-curator-prompt](#epi-obj-curator-prompt), this runs before generation and receives selected earlier pairs/next question rather than the just-produced answer. No supplied object counterpart; evidence for the consumer route and replacement request is see [RT-RTE-context-selection](runtime.md#rt-rte-context-selection). SRC-1, `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`; doctrine/design.

> - Introduce new meta-strategies based on recent problem-solving experiences.
> --- `prompts/curator_prompt_for_dc_retrieval_synthesis.txt`

#### EPI-OBJ-final-output
Label: Full generator output

Part of: [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict)

Source-native identity: final_output, containing natural-language answers/explanations and possible Python/output text. Representational form: natural-language interpretation, with symbolic Python executed on the local tool path. Storage substrate: returned string, driver corpus and JSONL. Claimed role: answer and source material for curator/retrieval. Candidate truth-apt content: problem answers, intermediate assertions and possible general rules; individual truth not assessed. This is a material field of the supplied result container, not a new identity for that container. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`; implementation.

> generator_outputs_so_far.append(output_dict["final_output"])
> --- `run_benchmark.py`

#### EPI-OBJ-final-answer
Label: Extracted final answer

Part of: [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict)

Source-native identity: final_answer/generator_answer. Representational form: model answer text, subsequently consumed by fixed string or arithmetic scoring rules. Storage substrate: returned dictionary and JSONL. Claimed role: scored task response. Candidate truth-apt content: the proposed answer over the current benchmark item, distinct from the full response. SRC-1, `dynamic_cheatsheet/utils/extractor.py`; implementation. The extractor selects the last answer opening tag; notebook source instead selects the first, so contradictory multiple tags can change the measured answer without changing the saved response.

> txt = response.split("<answer>")[-1].strip()
> txt = txt.split("</answer>")[0].strip()
> return txt
> --- `dynamic_cheatsheet/utils/extractor.py`

#### EPI-OBJ-final-cheatsheet
Label: Live returned reference

Part of: [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict)

Source-native identity: final_cheatsheet. Representational form: natural-language guidance and examples, potentially containing executable code or proposition-like strategies. Storage substrate: Python string, later prompts, JSONL. Claimed role: reusable reference. Candidate truth-apt content: conditional strategies, computational examples, claims of effectiveness and usage counts when produced as requested; non-truth-apt instructions may coexist. No actual candidate instance is assessed. SRC-1, `dynamic_cheatsheet/language_model.py`, `run_benchmark.py`; implementation. Container field is distinct from its producer and consumers; these are see [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation) and [RT-BAP-cheatsheet-context](runtime.md#rt-bap-cheatsheet-context).

> cheatsheet = output_dict["final_cheatsheet"]
> --- `run_benchmark.py`

#### EPI-OBJ-target
Label: Dataset target

Part of: [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict)

Source-native identity: target/original_target. Representational form: target answer text interpreted by symbolic scoring rules. Storage substrate: dataset item and saved JSONL. Claimed role: reference outcome for measurement, not curator guidance. Candidate truth-apt content: expected benchmark answer; truth/provenance of the dataset item uninspected. SRC-1, `run_benchmark.py`; implementation. This is the target part of the supplied mixed result/checkpoint object, distinct from model responses.

> original_target = dataset[idx]["target"]
> --- `run_benchmark.py`

#### EPI-OBJ-search-results
Label: Search results context

Source-native identity: search_context and provider-native searched response text. Representational form: natural-language snippets with symbolic URL labels in Tavily assembly; opaque native search text. Storage substrate: string prepended to a client user message or returned provider text. Claimed role: optional external context. Candidate truth-apt content: imported snippet assertions; source warrant unknown. Compared with [RT-OBJ-generator-prompt](runtime.md#rt-obj-generator-prompt), this is newly acquired external content, not a static generator template; no supplied object counterpart. SRC-1, `text_generation/simple_unified_client.py`; implementation. Structured provider citations are not returned as an evidence object by these text-returning methods.

> prompt = f"Web Search Results:\n{search_context}\n\nUser Query: {prompt}"
> --- `text_generation/simple_unified_client.py`

#### EPI-OBJ-messages
Label: Client chat messages

Source-native identity: UnifiedLLMClient.messages. Representational form: symbolic role/content envelopes around natural-language turns. Storage substrate: in-memory list with shallow get/set copies. Claimed role: conversation context. Candidate truth-apt content: prior user and assistant assertions, not automatically endorsed. Compared with [RT-OBJ-output-dict](runtime.md#rt-obj-output-dict), this is a distinct client-owned history, not benchmark disk state or external generate_from_messages history. SRC-1, `text_generation/simple_unified_client.py`; implementation.

> self.messages.append({"role": "user", "content": message})
> self.messages.append({"role": "assistant", "content": full_response})
> --- `text_generation/simple_unified_client.py`

### Routes

#### EPI-RTE-answer-generation
Label: Model answer generation

This is the common model-answer stage across default and all five context approaches. It overlaps the generator stages of [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation) and [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), but neither supplied route alone contains the all-mode producer. It does not duplicate either complete update/selection route.

Endpoints/progression: caller question and assembled reference → template → provider model → full answer text → extract_answer. Owner: wrapper for dispatch and extraction; configured remote model for proposed content. Context/state/action effects: candidate text becomes current answer and, in selected approaches, curator/history input. SRC-1, `dynamic_cheatsheet/language_model.py`; implementation. Semantic relation is indeterminate: no candidate content has been inspected to establish copying, entailment or non-entailment. The model's internal evidence and parameter truth-apt contents remain opaque.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Full response string and extracted answer in the advanced result.
- Later read-back: Driver appends full output for future retrieval/history; cumulative rounds may add extracted prior answers.
- Delegated visibility: Generator sees current question/reference; no target or online score from driver.
- Selection predicate: Approach selects reference context; extractor selects answer text, not correctness.
- Invalidation or expiry: New answer per call; previous outputs remain in caller corpus/checkpoint.
- Activation or effect: Provider dispatch and answer delivery implemented; content-dependent reliance unobserved.
- Evidence limits: No inspected generated instance, provider weights or answer-producing trace.

Behavioral-authority path: curator consumes full answer through its natural-language input, advisory evidence for a successor proposal; driver scorer consumes extracted answer through a fixed task predicate, determining immediate counts. Scheduling is computational in bounded benchmark or open caller modes. No answer oracle is supplied to the model producer. The static generator prompt requests checking assumptions, not an independently recorded acceptance decision.

> output = self.client.generate_from_messages(
>     messages=history,
>     temperature=temperature,
>     max_completion_tokens=max_tokens,
>     **self.extra_api_params,
> )
> --- `dynamic_cheatsheet/language_model.py`

#### EPI-RTE-reference-admission
Label: Delimiter reference admission

Distinct identity: the syntactic extraction/install stage spans [RT-RTE-cumulative-curation](runtime.md#rt-rte-cumulative-curation) and synthesis in [RT-RTE-context-selection](runtime.md#rt-rte-context-selection), not either entire proposal/selection loop. The concrete evaluator target is tag presence and substring extraction, not proposition truth. Endpoints/progression: curator response and fallback reference → extract_cheatsheet → live replacement string → later generator/driver. Owner: extractor and wrapper. SRC-1, `dynamic_cheatsheet/utils/extractor.py`, `dynamic_cheatsheet/language_model.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: First opening-tag segment, trimmed and stopped at the first closing tag, or fallback text.
- Later read-back: Installed text reaches next cumulative round and caller carry-forward; synthesis supplies it immediately to the next generator.
- Delegated visibility: Generator receives extracted text, not necessarily curator reasoning outside tags.
- Selection predicate: Opening cheatsheet tag and successful string operations; no semantic predicate.
- Invalidation or expiry: Replacement discards omitted live content; absent tag retains old cumulative reference or assembled retrieval fallback in synthesis.
- Activation or effect: Syntactic reference replacement enforced; correctness and model reliance unobserved.
- Evidence limits: No independent evidence-consuming acceptance criterion for truth, usefulness or transfer on inspected admission path.

Trigger/proposed change: every cumulative generated response or incoming synthesis query leads to a whole-reference proposal. Model proposes; software decides the substring; no human per-item approval or oracle on this path. Rejection ability is formatting fallback, not an accuracy veto. Recovery is caller/manual reconstruction from saved steps, not automatic rollback. Guidance requests accurate reusable strategies and copying useful prior content; only extracted text persists. Consumer/channel/force/horizon: downstream generator's user-message reference region, permissive installation plus advisory use, next round/query and resumed runs if saved. This is operational disposition, not epistemic acceptance or lifecycle integration.

Concrete implementation deduction without execution: response `prefix <cheatsheet>2+2=5`, old reference `2+2=4` → strip unchanged → opening-tag segment `2+2=5` → no closing tag means split leaves the same segment → returns `2+2=5`. Thus even an unclosed false candidate replaces a true fallback. Conversely a response with no opening tag returns fallback. This counterexample falsifies a universal semantic/closed-tag admission guarantee, not model compliance in any particular run.

> if "<cheatsheet>" in response:
>     try:
>         txt = response.split("<cheatsheet>")[1].strip()
>         txt = txt.split("</cheatsheet>")[0].strip()
>         return txt
>     except:
>         return old_cheatsheet
> else:
>     return old_cheatsheet
> --- `dynamic_cheatsheet/utils/extractor.py`

#### EPI-RTE-choice-scoring
Label: Multiple choice scoring

Part of: [RT-RTE-answer-scoring](runtime.md#rt-rte-answer-scoring)

Endpoints/progression: question/answer/target → eval_for_multiple_choice → boolean → benchmark or notebook accuracy count. Owner: deterministic evaluator and count consumer. Domain: GPQA/MMLU answer formats, target letters and target-option substrings. Context/state/action effects: count/print only, not live reference revision. SRC-1, `dynamic_cheatsheet/utils/evaluation.py`, `run_benchmark.py`, `EvaluatingResults.ipynb`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean match result.
- Later read-back: inapplicable — score is not saved as reference/update state; saved answer/target can be scored afresh.
- Delegated visibility: Scorer sees target; curator and generator do not receive this result.
- Selection predicate: Exact equality or accepted letter format or occurrence of target option text in normalized answer.
- Invalidation or expiry: Counters scoped to evaluation pass/new continuation examples.
- Activation or effect: Boolean controls reported count; no score-driven reference veto.
- Evidence limits: Predicate is not semantic entailment; target truth and measurement activation unobserved.

Dataset expected answer is the oracle for this bounded scoring mode. Software decides; no content approval by humans or models. Behavioral-authority path: scorer result → driver/notebook boolean counter branch → printed accuracy, enforcing the count for that pass only. No future proposal improvement trigger.

Concrete source deduction: question `Options:\n(A) red\n(B) blue`, target `(A)`, final answer `not red` → clean_target `a`, clean_answer `not red` → no exact/letter-format match → extract_option_text finds `red` → substring branch returns True. Therefore acceptance by this predicate does not establish endorsement of the target proposition. No target execution is needed for this deduction.

> if target_text and target_text in clean_answer:
>     return True
> --- `dynamic_cheatsheet/utils/evaluation.py`

#### EPI-RTE-search-acquisition
Label: Optional search acquisition

No supplied route counterpart after comparison with [RT-RTE-context-selection](runtime.md#rt-rte-context-selection): that selects earlier benchmark outputs, whereas this imports externally supplied search content. Endpoints/progression: client generate/chat with Tavily enabled → query → formatted title/URL/content snippets → prepended user prompt → provider. The separate native alternatives request server-side search through Claude/xAI/Gemini tools or an OpenAI search-capable model; they are not Tavily evaluation. Owner: client for request/formatting, external service for search and model for interpretation. SRC-1, `text_generation/simple_unified_client.py`; implementation. Benchmark generate_from_messages supplies false for the explicit native-search switch and does not call Tavily; OpenAI search-model behavior is an opaque exception to any universal no-search claim.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Tavily snippets are prepended to generation context; provider methods return generated text, not search-verification decisions.
- Later read-back: Chat can retain generated response; raw Tavily context is not stored in chat.messages by chat's two append operations. The original user message is retained instead.
- Delegated visibility: Tavily titles, URLs and snippet content reach the model; native provider metadata is projected into returned text rather than preserved as a structured evidence envelope.
- Selection predicate: Tavily enabled/requested with initialized client; query supplied or original prompt, max_results default five; native switch/provider branch selects a different external search operation.
- Invalidation or expiry: Fresh optional search per generate call; no source endorsement or freshness check in inspected formatting/projection methods.
- Activation or effect: Query dispatch and snippet context injection implemented; native tool declaration/text extraction implemented, external searching and actual reliance unobserved.
- Evidence limits: Native search internals, source truth, source selection and live compatibility uninspected; no inspected search result or generated claim.

Content relation: acquisition/import for external snippets, source warrant unknown. Tavily keeps title/URL/content as text; no authenticity or entailment check. Native answer generation is indeterminate, independently of its imported inputs. Native citation lineage is degraded at the structured-return boundary: OpenAI logs distinct URLs/titles but returns message.content; Claude takes text blocks, xAI takes output_text and Gemini returns text/candidate text. Text can still contain citations, so this does not establish that every citation is lost.

Decision/authority: software injects successful nonempty Tavily text (including the literal no-results text); service selects results; caller chooses search flags, not per-claim approval. No answer oracle, semantic veto or rollback on these inspected paths. Consumer/channel/force/horizon: model receives a user-message search prefix, advisory context for current generation; chat can carry the answer into later turns. Citation logger has logging force only, not a claim-certification or admission consumer. Operational mode is caller-open generation/chat, not a benchmark correctness curriculum.

> search_context = self._web_search(query)
> if search_context and not search_context.startswith("Web search failed"):
>     prompt = f"Web Search Results:\n{search_context}\n\nUser Query: {prompt}"
> --- `text_generation/simple_unified_client.py`

> if message.content:
>     return message.content
> --- `text_generation/simple_unified_client.py`

> logger.info("Web Search URLs Visited:")
> --- `text_generation/simple_unified_client.py`

#### EPI-RTE-chat-history
Label: Client chat history

Distinct identity compared with [RT-RTE-checkpoint-continuation](runtime.md#rt-rte-checkpoint-continuation): this client-owned in-memory conversation is neither JSONL reload nor the LanguageModel external message path. Endpoints/progression: chat → generate with previous self.messages → response → append original user message and assistant response → next generate/chat reads messages. Owner: client plus caller reset/set controls. Context/state/action effects: earlier turns reach later provider decisions. SRC-1, `text_generation/simple_unified_client.py`; implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Full response string, streaming chunks joined before retention when necessary.
- Later read-back: Later generate/chat extends its prompt with stored messages; benchmark generate_from_messages does not read this history.
- Delegated visibility: Later provider receives prior roles/content and current user message; Tavily prefix is not in the original message appended by chat.
- Selection predicate: All stored messages included by generate, without correctness ranking.
- Invalidation or expiry: reset_history clears messages; set_history replaces them with caller-supplied shallow copy; no semantic expiry on chat append.
- Activation or effect: Append and later delivery implemented; behavioral dependence and benefit unobserved.
- Evidence limits: No inspected conversation trace, semantic approval, disk persistence or outcome-driven invalidation on these methods.

Admission/control: caller proposes set/reset/history inputs, model proposes response; software appends both without content checks. Caller identity does not establish human authorship/approval. No expected-answer oracle or improvement trigger. Mode: open conversation. Retention is not acceptance; replacement/clear is caller-controlled, not correctness rollback. Consumer/channel/force/horizon: provider model, role/content history in the next generate/chat request, advisory prior context, client lifetime across turns. No guidance-method revision is implemented here.

> messages.extend(self.messages)
> messages.append({"role": "user", "content": prompt})
> --- `text_generation/simple_unified_client.py`

> self.messages = messages.copy()
> --- `text_generation/simple_unified_client.py`

### Claims

#### EPI-CLM-verified-solutions
Label: Verified reusable solutions

Claimed operation: curator consolidates verified solutions and only retains tested/effective strategies. SRC-1, `prompts/curator_prompt_for_dc_cumulative.txt`; doctrine/design. Compared with [RT-CLM-adaptive-memory](runtime.md#rt-clm-adaptive-memory), this is a distinct retention-warrant requirement, not a performance claim. Its model-requested check has no inspected instance-level acceptance trace. Usage counts and Q references are requested text, not software-computed success/provenance records.

> The cheatsheet's purpose is to consolidate verified solutions, reusable strategies, and critical insights into a single, well-structured resource.
> --- `prompts/curator_prompt_for_dc_cumulative.txt`

> - Only include solutions and strategies that have been tested and proven effective.
> --- `prompts/curator_prompt_for_dc_cumulative.txt`

#### EPI-CLM-zero-shot
Label: Label free performance improvement

Claimed operation: improvement without ground-truth labels or human feedback, accompanied by specific benchmark improvement reports. SRC-1, `README.md`; doctrine/design and reported operation. Distinct from [RT-CLM-adaptive-memory](runtime.md#rt-clm-adaptive-memory): this adds the label/feedback condition and empirical benefit claims. Source supports label-free curator updating, not absence of ground-truth evaluation or causal benefit. Full result traces and comparisons remain uninspected.

> * **Zero-Shot Learning**: Improves performance without ground-truth labels or human feedback
> --- `README.md`

> * **Puzzles**: GPT-4o's success rate on Game of 24 increased from approximately 10% to 99% after discovering and reusing Python-based solutions
> --- `README.md`

### Behavioral-authority paths

none declared in this member
