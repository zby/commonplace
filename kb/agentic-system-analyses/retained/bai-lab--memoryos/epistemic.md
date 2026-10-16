---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "MemoryOS truth-apt content, admission checks and downstream reliance at the frozen revision."
run-id: AAS-2026-10-16-memoryos-bb72a1b70e03-01
reviewed-boundary: "587ed7755c7aed179965792830ff1b5ad9a6fa92"
---

# MemoryOS epistemic report

## Source-and-claim boundary

The question is whether MemoryOS's memory-assisted dialogue and maintenance routes produce warranted content, rather than merely retaining, interpreting and reusing it. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are see [Source register](boundary.md#source-register). All source references below are SRC-1 at that pin. No target execution was performed. Implementation supports possible routes, not their activation or benefit.

The consequential system claim is see [RT-CLM-dialogue-benefit](runtime.md#rt-clm-dialogue-benefit). Prompt demands for factual extraction and evidence-grounded preference inference are assessed separately below; a request for factuality is not a completed factual check.

| Entry point or operation | Source path | Coverage and record |
|---|---|---|
| Python add/get_response, summary, continuity, metadata and profile maintenance | `memoryos-pypi/memoryos.py`, `memoryos-pypi/updater.py`, `memoryos-pypi/utils.py`, `memoryos-pypi/prompts.py` | Direct reads of maintenance admission, updater, utility transformations and prompts; remaining orchestration/retrieval/storage supplied by [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response), [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis). |
| MCP add/retrieve/profile, stdio dispatch | `memoryos-mcp/server_new.py` | Decorator/definition search checked against supplied [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access); bundled helper details rely on that record, not presumed universal equivalence. |
| Playground chat/import/force/clear/state | `memoryos-playground/memdemo/app.py` | Direct route search; supplied [RT-RTE-playground-control](runtime.md#rt-rte-playground-control). |
| Playground personality-analysis display | `memoryos-playground/memdemo/app.py` | Direct read; [EPI-RTE-personality-display](#epi-rte-personality-display) adds a material interpretive operation not separately traced in runtime. |
| ChromaDB keyword/profile transformations and persistent caller | `memoryos-chromadb/utils.py`, `memoryos-chromadb/mid_term.py` | Direct utility read and method search; other insertion, retrieval and persistence findings supplied by [RT-RTE-chroma-dialogue](runtime.md#rt-rte-chroma-dialogue). Deep insertion/merge internals remain unassessed; prevents a variant-complete negative about lineage or acceptance. |
| Evaluation import, generation and offline scoring | `eval/main_loco_parse.py`, `eval/dynamic_update.py`, `eval/evalution_loco.py` | Direct scorer read and updater search; other workflow findings supplied by [RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation). Evaluation storage internals and full prompt bodies remain unassessed; no system-complete absence claim. |
| Docker, demos, model components and remaining documentation | `Dockerfile`, `README.md`, `memoryos-pypi/test.py` | Supplied runtime account and [RT-CMP-openai-client](runtime.md#rt-cmp-openai-client), [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer), [RT-CMP-bgem3-flag-model](runtime.md#rt-cmp-bgem3-flag-model); no additional CLI dispatcher or autonomous hook inferred. |

Missing execution evidence prevents concluding that a particular extraction, admission, consumer influence or improvement occurred. Missing provider internals, resolved model versions and weights prevent identifying parametric propositions or their warrant; truth-apt objects inside those weights are **not determinable**. Available but uninspected variant code is an inspection limit, not an access gap. The excluded paper and unfrozen deployments support no extra claim here. No supplied fact requires supersession; the display operation supplements a valid runtime container.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-dialogue](#epi-obj-dialogue) | User assertions and assistant answers, when proposition-bearing | see record | SRC-1 `memoryos-pypi/updater.py` | Imperatives and social turns need not be truth-apt; assertions lack independent source certification. |
| [EPI-OBJ-summaries](#epi-obj-summaries) | Topic summaries and continuity metadata | see record | SRC-1 `memoryos-pypi/utils.py` | Requested compression does not prove semantic preservation. |
| [EPI-OBJ-user-profile](#epi-obj-user-profile) | Preference/trait levels, contextual explanations | see record | SRC-1 `memoryos-pypi/prompts.py` | A possible inference about a person, not an independently measured trait. |
| [EPI-OBJ-user-knowledge](#epi-obj-user-knowledge) | Extracted personal facts | see record | SRC-1 `memoryos-pypi/utils.py` | No item-level evidence-consuming truth acceptance shown. |
| [EPI-OBJ-assistant-knowledge](#epi-obj-assistant-knowledge) | Claims about assistant actions/capabilities | see record | SRC-1 `memoryos-pypi/prompts.py` | A statement of capability in dialogue does not demonstrate that capability. |
| [RT-OBJ-generation-prompts](runtime.md#rt-obj-generation-prompts) | Instructions primarily; supplied content may assert facts | see record | SRC-1 `memoryos-pypi/prompts.py` | Prompt instruction and its factual payload have different roles. |
| [EPI-OBJ-personality-traits](#epi-obj-personality-traits) | Displayed dimension/level assignments | see record | SRC-1 `memoryos-playground/memdemo/app.py` | Parser can manufacture a positive-looking assignment from a negation. |
| [RT-CMP-openai-client](runtime.md#rt-cmp-openai-client), [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer), [RT-CMP-bgem3-flag-model](runtime.md#rt-cmp-bgem3-flag-model) | Not determinable within opaque distributed-parametric state; vectors used for relevance are not truth verdicts | see records | SRC-1 `memoryos-pypi/utils.py` | Encoding calls are inspected/supplied, weights and provider processing are not. |

## Authority-route ledger

Fields owned by cited records are not restated: `see` delegates those fields to the declaration. This ledger supplies the epistemic classification. Rows sharing an ID separate its consequential functions, not new referents. All `implemented` statuses mean implementation evidence only; no observed-run result is claimed.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) | content transformation | implemented | [EPI-OBJ-dialogue](#epi-obj-dialogue) | truth-apt transformation: acquisition/import | Supplied dialogue enters memory | see record | see record | see record | see record | Source warrant unknown; retains assertions, not established facts | see record | see record | SRC-1 `memoryos-pypi/memoryos.py` | none | none | External/imported assistant text need not originate from this response model. |
| [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) | content transformation | implemented | [EPI-OBJ-summaries](#epi-obj-summaries) | truth-apt transformation: indeterminate | Dialogue to summaries/meta-summary | see record; generation, not an independent verifier | see record | see record | see record | Neither entailment nor semantic preservation established | see record | see record | SRC-1 `memoryos-pypi/updater.py`, `memoryos-pypi/utils.py` | none | none | Reshaping versus conjectural content needs actual input/output and semantic checking. |
| [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) | check/evidence production | implemented | [EPI-OBJ-summaries](#epi-obj-summaries) | no content change | Topic continuity of adjacent pages; JSON syntax of summary | Model true/false judgment over supplied dialogue; JSON parser over syntax | Overflow processing; see record | Boolean continuity; parsed array or empty fallback | Branch selection only | Supports an attributed continuity judgment or parse success, not source truth | Updater can link pages and propagate metadata | see record | SRC-1 `memoryos-pypi/utils.py`, `memoryos-pypi/updater.py` | none | none | Exact true test means `true.` is false; no independent continuity oracle. |
| [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) | retention | implemented | [EPI-OBJ-dialogue](#epi-obj-dialogue), [EPI-OBJ-summaries](#epi-obj-summaries) | no content change | Admission to short/mid-term state | see record | see record | see record | see record | Retention grants availability, not evidence-consuming acceptance | see record | see record | SRC-1 `memoryos-pypi/updater.py` | none | none | No lifecycle integration inferred from grouping or persistence. |
| [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis) | content transformation | implemented | [EPI-OBJ-user-profile](#epi-obj-user-profile) | truth-apt transformation: indeterminate | Dialogue plus old profile to revised trait claims | see record; prompt asks inference from evidence, not a separate test | see record | see record | see record | Candidate interpretations only | see record | see record | SRC-1 `memoryos-pypi/prompts.py`, `memoryos-pypi/utils.py` | none | none | Trait inference can be ampliative, but no actual non-entailed output established; classification stays indeterminate. |
| [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis) | content transformation | implemented | [EPI-OBJ-user-knowledge](#epi-obj-user-knowledge), [EPI-OBJ-assistant-knowledge](#epi-obj-assistant-knowledge) | truth-apt transformation: indeterminate | Dialogue to concise extracted lines | see record | see record | see record | see record | Requested factual extraction, not certified preservation | see record | see record | SRC-1 `memoryos-pypi/utils.py`, `memoryos-pypi/prompts.py` | none | none | Separate user and assistant consumers remain below. |
| [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis) | check/evidence production | implemented | [EPI-OBJ-user-profile](#epi-obj-user-profile), [EPI-OBJ-user-knowledge](#epi-obj-user-knowledge), [EPI-OBJ-assistant-knowledge](#epi-obj-assistant-knowledge) | no content change | Output nonemptiness, sentinel strings, profile length | Deterministic string checks; domain is output shape, not truth | Before writes; see record | Pass or skip | Guards control write eligibility | Only shape/length license; no factual criterion | see record | see record | SRC-1 `memoryos-pypi/memoryos.py` | none | none | Error sentinel is longer than thirty characters and not `none`: it can pass the profile guard. |
| [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis) | disposition/acceptance | implemented | [EPI-OBJ-user-profile](#epi-obj-user-profile), [EPI-OBJ-user-knowledge](#epi-obj-user-knowledge), [EPI-OBJ-assistant-knowledge](#epi-obj-assistant-knowledge) | no content change | Guarded content becomes eligible retained context | see record | see record | see record | see record | Operational admission only; not acceptance of truth under a named evidential criterion | see record | see record | SRC-1 `memoryos-pypi/memoryos.py` | none | none | Marking pages analyzed records processing, not warranted endorsement. |
| [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis) | retention | implemented | [EPI-OBJ-user-profile](#epi-obj-user-profile), [EPI-OBJ-user-knowledge](#epi-obj-user-knowledge), [EPI-OBJ-assistant-knowledge](#epi-obj-assistant-knowledge) | no content change | Profile replacement and fact append | see record | see record | see record | see record | Retained candidate ledger, not established lifecycle integration | see record | see record | SRC-1 `memoryos-pypi/memoryos.py` | none | none | Old profile feeds later inference, enabling persistence of unsupported claims too. |
| [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response) | operational admission/selection/consumption | implemented | [EPI-OBJ-dialogue](#epi-obj-dialogue), [EPI-OBJ-user-profile](#epi-obj-user-profile), [EPI-OBJ-user-knowledge](#epi-obj-user-knowledge) | no content change | Context selection and delivery | Similarity thresholds/ranking; full profile and recent history bypass ranking; see record | see record | see record | see record | Relevance selection grants no truth license | see record | see [RT-BAP-user-context](runtime.md#rt-bap-user-context) | SRC-1 `memoryos-pypi/retriever.py`, `memoryos-pypi/memoryos.py` | [RT-CLM-dialogue-benefit](runtime.md#rt-clm-dialogue-benefit) | none | Access/heat is salience, not endorsement or temporal truth. |
| [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response) | operational admission/selection/consumption | implemented | [EPI-OBJ-assistant-knowledge](#epi-obj-assistant-knowledge) | no content change | Assistant facts selected into system message | see record | see record | see record | see record | No independent warrant from higher-priority placement | see record | see [RT-BAP-assistant-context](runtime.md#rt-bap-assistant-context) | SRC-1 `memoryos-pypi/memoryos.py` | [RT-CLM-dialogue-benefit](runtime.md#rt-clm-dialogue-benefit) | none | Operationally stronger channel need not imply epistemically stronger provenance. |
| [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response) | content transformation | implemented | [EPI-OBJ-dialogue](#epi-obj-dialogue) | truth-apt transformation: indeterminate | Query/context to answer | see record | see record | see record | see record | No external answer oracle in open dialogue | see record | see record | SRC-1 `memoryos-pypi/memoryos.py` | [RT-CLM-dialogue-benefit](runtime.md#rt-clm-dialogue-benefit) | none | Model may reshape, derive, conjecture or produce non-truth-apt text; no output supplied to distinguish. |
| [EPI-RTE-output-cleaning](#epi-rte-output-cleaning) | content transformation | implemented | [EPI-OBJ-dialogue](#epi-obj-dialogue) | truth-apt transformation: non-ampliative reshaping | Tagged response text | see record | see record | see record | see record | Deletion preserves no warranty of whole-response meaning | see record | see record | SRC-1 `memoryos-pypi/utils.py` | none | none | Explicit witness deletes a proposition; no evidence-consuming acceptance occurs. |
| [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access) | operational admission/selection/consumption | implemented | [EPI-OBJ-dialogue](#epi-obj-dialogue), [EPI-OBJ-user-profile](#epi-obj-user-profile), [EPI-OBJ-user-knowledge](#epi-obj-user-knowledge), [EPI-OBJ-assistant-knowledge](#epi-obj-assistant-knowledge) | no content change | Tool result data to host | see record | see record | see record | see record | Host receives candidate context, not adjudicated knowledge | see record | see record | SRC-1 `memoryos-mcp/server_new.py` | none | none | Host's subsequent reliance/channel outside boundary. |
| [RT-RTE-chroma-dialogue](runtime.md#rt-rte-chroma-dialogue) | operational admission/selection/consumption | implemented | [EPI-OBJ-summaries](#epi-obj-summaries), [EPI-OBJ-user-profile](#epi-obj-user-profile) | no content change | Keyword ranking and profile consumption | see record; JSON parsing or raw-text wrapper does not check truth | see record | see record | see record | Availability and relevance only | see record | see record | SRC-1 `memoryos-chromadb/utils.py`, `memoryos-chromadb/retriever.py` | none | none | Same warrant limits do not establish identical variant admission or persistence. |
| [RT-RTE-playground-control](runtime.md#rt-rte-playground-control) | lineage/freshness/recovery | implemented | [EPI-OBJ-dialogue](#epi-obj-dialogue), [EPI-OBJ-user-profile](#epi-obj-user-profile) | no content change | Import, forced analysis and explicit clear | see record | see record | see record | see record | Clear is deletion, not claim-specific retraction or revised warrant | see record | see record | SRC-1 `memoryos-playground/memdemo/app.py` | none | none | Eviction/reset controls future availability, not falsehood classification. |
| [EPI-RTE-personality-display](#epi-rte-personality-display) | content transformation | implemented | [EPI-OBJ-personality-traits](#epi-obj-personality-traits) | truth-apt transformation: ampliative conjecture | Profile prose to displayed level assignment | see record | see record | see record | see record | Concrete negation counterexample defeats entailment | see record | see record | SRC-1 `memoryos-playground/memdemo/app.py` | none | none | Symbolic implementation does not make this a valid deduction. |
| [RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation) | check/evidence production | implemented | [EPI-OBJ-dialogue](#epi-obj-dialogue) | no content change | Benchmark answer lexical overlap with supplied reference | see record; token-set F1 domain only | see record | see record | see record | Licenses lexical overlap, not factual equivalence or causal component effect | see record | see record | SRC-1 `eval/evalution_loco.py` | [RT-CLM-dialogue-benefit](runtime.md#rt-clm-dialogue-benefit) | none | Offline printed aggregates have no inspected admission, rollback or policy-update consumer. |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-dialogue-benefit](runtime.md#rt-clm-dialogue-benefit) | see record | SRC-1 `README.md`; doctrine/design, reported operation | see record | [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response), [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis), [RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation) | see record | see record | Memory-conditioned response and offline F1 machinery are wired | Personalized coherence, numerical gains, BLEU improvement and component causation unverified. |

The extraction prompts request concise factual statements and preference inference from conversation (SRC-1 `memoryos-pypi/prompts.py`; see [EPI-OBJ-user-profile](#epi-obj-user-profile), [EPI-OBJ-assistant-knowledge](#epi-obj-assistant-knowledge)). These are proposal guidance, not an additional public claim that every output has passed a truth test. The guard's permissive error-sentinel case is a concrete counterexample to treating successful admission as successful analysis.

## Bounded conclusion

MemoryOS imports dialogue with unknown source warrant, retains original pages as well as model interpretations, and supplies selected material to subsequent models or an MCP host. Model-generated summaries, extracted facts, profiles and answers have **indeterminate** semantic relations without actual candidates and checking: neither their labels nor prompts establish entailed derivation, novelty or preservation. The deterministic output cleaner proves that intervening deletion occurs; the Playground parser supplies a concrete ampliative edge even without model inference.

Admission criteria in the inspected JSON maintenance route are nonempty/non-sentinel content and a thirty-character profile minimum. Their intended use is persistent dialogue context, not truth certification. Profile replacement and knowledge append are software decisions over model proposals, not per-item human approvals. Their consumer channels and horizons are see [RT-BAP-user-context](runtime.md#rt-bap-user-context), [RT-BAP-assistant-context](runtime.md#rt-bap-assistant-context). User and assistant facts have different downstream authority channels; neither acquires warrant merely by being used. ChromaDB's parsed-or-wrapped profile route has a distinct, weaker shape requirement, not the JSON variant's guard.

Continuity judgments, summary JSON parsing, similarity/heat selection, admission filters and benchmark scoring are real checks, each with a limited target. None of these inspected consumers turns the offline F1 score into content acceptance, source-truth verification or method revision. As a concrete implementation deduction from SRC-1 `eval/evalution_loco.py`, `Alice left` and `Alice Alice left` yield identical token sets and F1 1; `Alice left` and `Alice never left` yield precision 1, recall 2/3 and F1 0.8 despite opposed assertions. Thus the implemented lexical evaluator is not a truth oracle. No claim is made about all possible uninspected variant checks.

No evidence-consuming acceptance of a produced ampliative proposition, nor subsequent lifecycle integration **after such acceptance**, is established by these inspected maintenance paths. Operational organization of candidates is established separately. Deletion, LFU/capacity expiry, raw-text fallback and analyzed markers alter availability or processing; they do not constitute content-directed criticism with blame or evidence of successful correction. The offline evaluator is a counterexample to an unqualified claim that MemoryOS never evaluates anything, while the absence of its consequential update consumer blocks treating it as runtime warrant or an exercised improvement loop.

Trace-fed profile/fact updates can shape future dialogue through retained natural-language state. They do not train the inspected model components. Improved future capacity, exercised self-improvement, reliable model compliance and component benefits remain unsupported without execution and attribution evidence. Preference-model guidance is explicit, and retained profiles feed later updates, but no supplied content-directed criticism establishes a theory-builder cycle. These limits do not negate the independent implemented acquisition, retention, selection and behavioral-authority paths.

## Shared records

### Operative objects

#### EPI-OBJ-dialogue
Label: Dialogue assertions and answers

Source-native identity: QA `user_input` and `agent_response`, later page fields. Natural-language turns inside symbolic dictionaries; short/mid-term JSON substrate in the principal variant. Evidence: SRC-1 `memoryos-pypi/updater.py`; supplied [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) gives admission, persistence and read-back. Distinct from [RT-OBJ-generation-prompts](runtime.md#rt-obj-generation-prompts): accumulated payload, not shipped instructions. No supplied operative-object counterpart after comparison.

> "user_input": qa_pair.get("user_input", ""),
>                 "agent_response": qa_pair.get("agent_response", ""),
> --- `memoryos-pypi/updater.py`

#### EPI-OBJ-summaries
Label: Topic and continuity summaries

Source-native identity: `theme_summary`, page `meta_info`. Natural-language summaries and symbolic keyword lists in mid-term storage. Role: session grouping/selection and continuity context. Evidence: SRC-1 `memoryos-pypi/updater.py`, `memoryos-pypi/utils.py`. Distinct from the raw dialogue object and static [RT-OBJ-generation-prompts](runtime.md#rt-obj-generation-prompts); closest supplied mechanisms are [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), not duplicate object declarations.

> theme_summary = summary_item.get("content", "General summary of recent interactions.")
>                 theme_keywords = summary_item.get("keywords", [])
> --- `memoryos-pypi/updater.py`

#### EPI-OBJ-user-profile
Label: User preference profile

Source-native identity: `updated_user_profile`; natural-language trait assessments stored as user long-term profile text in JSON. Role: background conditioning and input to later profile revision. Evidence: SRC-1 `memoryos-pypi/prompts.py`, `memoryos-pypi/memoryos.py`; closest supplied record [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis) is its producer container, not an object counterpart. Distinct from [RT-OBJ-generation-prompts](runtime.md#rt-obj-generation-prompts), the static consumption instructions.

> 2. If reflected, determine the user's preference level: High / Medium / Low, and briefly explain the reasoning, including time, people, and context if possible.
> 3. If the dimension is not reflected, do not extract or list it.
> --- `memoryos-pypi/prompts.py`

#### EPI-OBJ-user-knowledge
Label: User private knowledge lines

Source-native identity: extracted `private` text admitted by `add_user_knowledge`. Natural-language facts held in symbolic entries with embeddings; long-term JSON in the principal variant. Role: query-selected user background. Evidence SRC-1 `memoryos-pypi/utils.py`, `memoryos-pypi/memoryos.py`; supplied producer [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis) and consumer [RT-BAP-user-context](runtime.md#rt-bap-user-context). No supplied operative-object counterpart after comparison; different consumer from assistant facts.

> if new_user_private_knowledge and new_user_private_knowledge.lower() != "none":
>                     for line in new_user_private_knowledge.split('\n'):
>                          if line.strip() and line.strip().lower() not in ["none", "- none", "- none."]:
>                             self.user_long_term_memory.add_user_knowledge(line.strip())
> --- `memoryos-pypi/memoryos.py`

#### EPI-OBJ-assistant-knowledge
Label: Assistant action and capability lines

Source-native identity: extracted `assistant_knowledge` admitted by `add_assistant_knowledge`. Natural-language claims in embedded symbolic entries, assistant-specific long-term JSON in the principal variant. Role: later system-message persona/knowledge. Evidence SRC-1 `memoryos-pypi/prompts.py`; supplied [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis), [RT-BAP-assistant-context](runtime.md#rt-bap-assistant-context). No supplied operative-object counterpart; source and consumer distinguish it from user facts and static prompts.

> Assistant knowledge: explicit statements about what the assistant did, provided, or demonstrated
> --- `memoryos-pypi/prompts.py`

#### EPI-OBJ-personality-traits
Label: Parsed personality display assignments

Source-native identity: `extracted_traits`, returned as `personality_analysis`. Symbolic category/dimension/level dictionaries carrying proposition-like trait assignments; transient HTTP JSON substrate, not a retained memory write. Evidence SRC-1 `memoryos-playground/memdemo/app.py`. Closest supplied [RT-RTE-playground-control](runtime.md#rt-rte-playground-control) describes the application, not this operative object. Distinct from profile prose because the parser omits qualifications and chooses levels by lexical occurrence.

> extracted_traits[category].append({
>                                     'dimension': dimension,
>                                     'level': level
>                                 })
> --- `memoryos-playground/memdemo/app.py:325-328`

### Routes

#### EPI-RTE-output-cleaning
Label: Completion output cleaning

Part of: [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response)

This part is the response client's deterministic text-deletion stage; the parent remains valid. Endpoints: raw completion → `clean_reasoning_model_output` → cleaned return → parent admission. Owner: `OpenAIClient`. SRC-1 `memoryos-pypi/utils.py` supplies implementation evidence. The same utility also wraps maintenance calls; no claim of identical cleaning in all evaluation helpers follows. The transformation removes tagged spans rather than evaluating their assertions. For concrete input `<think>Alice left.</think>Bob stayed.`, regex deletion yields `Bob stayed.`; whitespace cleanup and strip leave it unchanged. This is non-ampliative deletion, not acceptance, evidence production or guaranteed meaning preservation. No human decision, reference answer or quality oracle participates.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: cleaned completion text.
- Later read-back: parent's admitted cleaned answer can enter later memory contexts; removed span is not admitted by this route.
- Delegated visibility: provider produced raw text; caller and subsequent memory admission receive the cleaned result.
- Selection predicate: regex matches literal lowercase think-tag spans, non-greedily across newlines; excess blank lines and boundary whitespace are removed.
- Invalidation or expiry: inapplicable — no independently retained cleaner state; parent memory expiry controls admitted text.
- Activation or effect: deletion is implementation-deduced for the concrete input; no observed model response supplied.
- Evidence limits: no source-truth check, tag correctness check or semantic-preservation proof; unclosed tags do not match this pattern.

> cleaned_text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL)
> --- `memoryos-pypi/utils.py`

> cleaned_content = clean_reasoning_model_output(raw_content)
>             return cleaned_content
> --- `memoryos-pypi/utils.py`

#### EPI-RTE-personality-display
Label: Playground personality display parsing

Part of: [RT-RTE-playground-control](runtime.md#rt-rte-playground-control)

This part is the application's profile-to-display interpretation, not a replacement for the supplied admin-control container. Endpoints: POST `/personality_analysis` → retained raw profile → `parse_personality_traits` → JSON assignments. Owner: Flask callback and deterministic parser. Evidence SRC-1 `memoryos-playground/memdemo/app.py`, implementation. The model/caller supplies profile prose upstream; code chooses display labels; user requests display but does not approve each label. No truth oracle or improvement trigger. The only callback vetoes are missing session/profile and exceptions, not trait accuracy. No retained update, acceptance or rollback occurs.

Concrete source deduction: input `Extraversion is not High.` yields no regex pair. The fallback scans `High` before `Medium` and `Low`, finds the dimension substring, and emits `Extraversion` / `High` under Psychological Model. The input denies the displayed proposition, so this transformation is demonstrably not entailed reshaping. The classification is ampliative conjecture in the contract's semantic sense, not a claim that this parser intentionally reasons. A positive input such as `Extraversion (High)` can also produce a faithful assignment; the counterexample bounds reliability rather than asserting every assignment is wrong.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: HTTP JSON `personality_analysis` category/dimension/level lists.
- Later read-back: inapplicable — parser result is returned, not written into memory by this endpoint.
- Delegated visibility: browser/caller receives assignments; no provider call from this callback.
- Selection predicate: session exists and profile is not empty/none-like; regex pair matching plus case-insensitive level/dimension substring fallback, suppressing exact-dimension duplicates.
- Invalidation or expiry: inapplicable — result is transient and recomputed on request; source profile can be replaced by other routes.
- Activation or effect: implemented presentation of possibly amplified trait claims; no supplied browser trace demonstrates display or reliance.
- Evidence limits: detects textual patterns, not negation or warranted preference levels; no evidence of subsequent model consumption of the returned assignments.

> personality_analysis = parse_personality_traits(user_profile)
> --- `memoryos-playground/memdemo/app.py`

> for level in ['High', 'Medium', 'Low']:
>             if level.lower() in line.lower():
>                 # Try to extract the dimension name
>                 for category, dimensions in categories.items():
>                     for dimension in dimensions:
>                         if dimension.lower() in line.lower():
> --- `memoryos-playground/memdemo/app.py`
