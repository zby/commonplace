---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "AI Agents in Depth: imported observations, numerical grounding checks and bounded retry-policy acceptance, distinguished from task correctness and live improvement."
run-id: AAS-2026-10-12-ai-agent-book-d56e8121d636-01
reviewed-boundary: "dbc046eb896ac4e39aa19c7774c8bf49583b89a6"
---

# AI Agents in Depth epistemic report

## Source-and-claim boundary

The question is which selected teaching workflows acquire or produce truth-apt content, what checks license reliance, and which consumers give their results consequential force. The [boundary](boundary.md#boundary-and-evidence) governs the suite's complete artifact, partial loop. Evidence identity and layers are in its [Source register](boundary.md#source-register); all added inspection uses SRC-1 at that same commit. No target execution was performed or adopted as observed evidence.

The assessed families are context-agent observations and replies, mode-dependent delivery, the ablation's numerical assessor and reporting consumer, and retry-policy candidate checking and disposition. Imported PDF assertions, financial results, and model answers are not interchangeable with executable retry rules. Claims found are the teaching purpose [RT-CLM-context-purpose](runtime.md#rt-clm-context-purpose), bounded eligibility [RT-CLM-canary-decision](runtime.md#rt-clm-canary-decision), and the tool's live-rate description [EPI-CLM-current-rates](#epi-clm-current-rates). The assessor's stronger provenance wording is examined under [EPI-CLM-grounding-source](#epi-clm-grounding-source).

| Entry point or operation | Source path | Coverage and records | Limit and conclusion prevented |
| --- | --- | --- | --- |
| CLI single, interactive and ablation dispatch | SRC-1: `chapter1/context/main.py` | Direct read of CLI dispatch, assessor call, warning and summary/table consumers; supplied [RT-RTE-context-task](runtime.md#rt-rte-context-task), [RT-RTE-context-ablation](runtime.md#rt-rte-context-ablation) | No observed invocation or benefit |
| Four registered context tools and loop | SRC-1: `chapter1/context/agent.py` | Supplied complete agent implementation inspection and fixed dispatch; direct read of PDF, conversion, calculator and relevant tool descriptions, plus complete `chapter1/context/calc_sandbox.py`; [EPI-RTE-pdf-import](#epi-rte-pdf-import), [EPI-RTE-currency-conversion](#epi-rte-currency-conversion), [RT-RTE-calculation-path](runtime.md#rt-rte-calculation-path), [RT-RTE-code-execution](runtime.md#rt-rte-code-execution) | Arbitrary interpreter programs not inspected; their semantic warrant cannot be generalized |
| Numerical extraction and grounding verdict | SRC-1: `chapter1/context/grounding.py` | Complete direct read; [EPI-RTE-grounding-check](#epi-rte-grounding-check), [EPI-RTE-grounding-report](#epi-rte-grounding-report) | No reference task rubric; no derivation-provenance oracle |
| Context omission, reset and task continuation | SRC-1: `chapter1/context/agent.py`, `chapter1/context/main.py` | Supplied [RT-RTE-context-ablation](runtime.md#rt-rte-context-ablation), [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history) | Retention does not guarantee delivery or model compliance |
| Candidate demo, campaign and exposed release function | SRC-1: `chapter9/self-modifying-agent/demo.py`, `chapter9/self-modifying-agent/run_experiment_9_6.py`, `chapter9/self-modifying-agent/evolution.py` | Supplied [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate); direct read of generation control, validation and manifest expression in evolution | No deployed successor or live rollback; campaign report writer remains uninspected |
| Container validation and metrics | SRC-1: `chapter9/self-modifying-agent/candidate_sandbox.py`, `chapter9/self-modifying-agent/sandbox_runner.py` | Supplied [RT-RTE-candidate-validation](runtime.md#rt-rte-candidate-validation), [RT-BAP-candidate-policy](runtime.md#rt-bap-candidate-policy) | No inspected execution, Docker image verification or adversarial oracle-integrity proof |
| Provider resolution and model state | SRC-1: `agentbook/providers/resolution.py`, `chapter9/self-modifying-agent/llm_generator.py` | Supplied [RT-CMP-context-model](runtime.md#rt-cmp-context-model), [RT-CMP-coding-model](runtime.md#rt-cmp-coding-model) | Weights and provider internals unavailable; immutable versions and parameter adaptation not established |
| User-memory maintenance and later consumption | SRC-1: `chapter3/user-memory/` | Initial boundary witnesses only; targeted symbol search in `memory_manager.py` and `background_memory_processor.py` is not a full route inspection | Add/update/delete, consolidation, conflict handling, admission and prompt reliance remain unassessed here; prevents a suite-complete negative about acceptance or integration |
| Other chapters, instruction-loading skills, training, retrieval, collaboration and retained validation artifacts | SRC-1: `chapter2/` through `chapter10/`, `skills/`, chapter-local validation paths | Available but uninspected except the selected chapter3 witnesses and chapter9 candidate workflow | No exhaustive architecture, evaluator, learning or knowledge-production conclusion |
| External reproduction repositories, weights, services and agent host | See boundary exclusions and dependencies | Not registered evidence | No end-to-end reproduction, host compliance or service-behavior conclusion |

No additional hooks or dynamic tool registrations are established in the selected context dispatcher. That is a bounded supplied finding, not an absence claim for the suite. Available retained artifacts were not used to infer which routes ran.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
| --- | --- | --- | --- | --- |
| [EPI-OBJ-pdf-result](#epi-obj-pdf-result) | External PDF assertions, as extracted text | see record | SRC-1: `chapter1/context/agent.py` | Author truth and extraction fidelity unchecked |
| [EPI-OBJ-currency-result](#epi-obj-currency-result) | Conversion under fixed rates and rounded numerical result | see record | SRC-1: `chapter1/context/agent.py` | Financial freshness unknown; timestamp is calculation time |
| [EPI-OBJ-final-answer](#epi-obj-final-answer) | Task-dependent assertions when reply has them; a refusal need not | see record | SRC-1: `chapter1/context/agent.py`, `chapter1/context/grounding.py` | Proposition/domain requires a concrete reply; source contains no observed reply adopted here |
| [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history) | Mixed container: tasks, guidance, assistant and tool text | see record | SRC-1: `chapter1/context/agent.py` | Not one homogeneous epistemic object; the three parts above separate material content |
| [RT-OBJ-retry-policy](runtime.md#rt-obj-retry-policy) | Formal retry/circuit policy; comments and impact predictions assert intended behavior | see record | SRC-1: `chapter9/self-modifying-agent/evolution.py` | Policy instructions themselves are behavioral rules, not established claims of improved real-world performance |
| [RT-CMP-context-model](runtime.md#rt-cmp-context-model) | Internal truth-apt units not determinable | see record | SRC-1: `agentbook/providers/resolution.py` | Opaque parameters, mutable routing, no weight-level inspection |
| [RT-CMP-coding-model](runtime.md#rt-cmp-coding-model) | Internal truth-apt units not determinable; external proposal is module text | see record | SRC-1: `chapter9/self-modifying-agent/llm_generator.py` | Proposal request does not establish compliance or weight learning |

## Authority-route ledger

Each row is one function. A repeated route citation separates functions of an existing implementation without reallocating its identity. Fields owned by a shared record say `see`; these are not fresh declarations. All implemented statuses below denote source wiring, not observed operation.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [EPI-RTE-pdf-import](#epi-rte-pdf-import) | content transformation | implemented | see record | truth-apt transformation: acquisition/import | PDF bytes to text observations | see record | see record | see record | see record | Source warrant unknown; records source URL and page, not validation | Makes extracted assertions available for a later completion | see record | SRC-1: `chapter1/context/agent.py` | none | none | Parser success is not endorsement |
| [EPI-RTE-currency-conversion](#epi-rte-currency-conversion) | content transformation | implemented | see record | truth-apt transformation: entailed derivation | Numerical amount under fixed rate table | see record | see record | see record | see record | Conditional arithmetic only, assuming supplied amount and table; no live-rate warrant | Returned result can shape later reply | see record | SRC-1: `chapter1/context/agent.py` | [EPI-CLM-current-rates](#epi-clm-current-rates) | current versus static | Numeric input and rate truth not checked |
| [RT-RTE-calculation-path](runtime.md#rt-rte-calculation-path) | check/evidence production | implemented | see record | no content change | Expression AST admissibility | see record | see record | see record | see record | Syntax whitelist only, not source truth or physical units | Blocks prohibited AST before eval | see record | SRC-1: `chapter1/context/calc_sandbox.py` | none | none | Resource exhaustion and other tool routes outside check |
| [RT-RTE-calculation-path](runtime.md#rt-rte-calculation-path) | content transformation | implemented | see record | truth-apt transformation: entailed derivation | Evaluation of accepted mathematical expression | see record | see record | see record | see record | Result conditional on expression, Python arithmetic and supported names; no warrant for modeling assumptions | Produces tool observation | see record | SRC-1: `chapter1/context/agent.py`, `chapter1/context/calc_sandbox.py` | none | none | Caret rewrite changes Python syntax intentionally; input `2^3` becomes `2**3` and denotes 8, not Python XOR |
| [RT-RTE-code-execution](runtime.md#rt-rte-code-execution) | content transformation | implemented | see record | truth-apt transformation: indeterminate | Arbitrary supplied Python output | see record | see record | see record | see record | Execution success licenses only that code completed on that call, not output truth | Output enters tool history | see record | SRC-1: `chapter1/context/agent.py` | none | none | A specific program is needed to decide acquisition, reshaping, derivation or conjecture; policies may be non-truth-apt |
| [RT-RTE-context-task](runtime.md#rt-rte-context-task) | content transformation | implemented | [EPI-OBJ-final-answer](#epi-obj-final-answer) | truth-apt transformation: indeterminate | Task/context to generated reply | see record | see record | see record | see record | Candidate generation only; no task correctness oracle | May finish the task and return text | see record | SRC-1: `chapter1/context/agent.py` | none | completion is not correctness | Concrete content needed to decide entailment versus non-entailment; terminal refusals need not produce claims |
| [RT-RTE-context-task](runtime.md#rt-rte-context-task) | retention | implemented | [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history) | no content change | Append messages and trajectory | see record | see record | see record | see record | Retention grants no endorsement | Same live agent can expose earlier content to later tasks | see record | SRC-1: `chapter1/context/agent.py`, `chapter1/context/main.py` | none | none | Written single-task JSON has no inspected reload |
| [RT-RTE-context-ablation](runtime.md#rt-rte-context-ablation) | operational admission/selection/consumption | implemented | [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history) | no content change | Stored versus delivered messages/tools/results | see record | see record | see record | see record | Visibility manipulation, not truth checking | Permits/withholds context at provider request | see record | SRC-1: `chapter1/context/agent.py` | [RT-CLM-context-purpose](runtime.md#rt-clm-context-purpose) | none | Hidden provider reasoning is not removed by dropping exposed reasoning text |
| [EPI-RTE-grounding-check](#epi-rte-grounding-check) | check/evidence production | implemented | [EPI-OBJ-final-answer](#epi-obj-final-answer) | truth-apt transformation: entailed derivation | Extracted quantities versus task/tool-message quantities | see record | see record | see record | see record | Reports numeric-match predicate, not correctness or actual derivation lineage | No admission veto in this function | see record | SRC-1: `chapter1/context/grounding.py` | [EPI-CLM-grounding-source](#epi-clm-grounding-source) | source availability overstatement | Ignores sub-floor answer figures; observations trigger abstention; valid arithmetic can yield unmatched numbers |
| [EPI-RTE-grounding-report](#epi-rte-grounding-report) | operational admission/selection/consumption | implemented | see record | no content change | Grounding verdict to report fields | see record | see record | see record | see record | Advisory report only | Warns, labels tables, counts unsupported answers and assigns failure reason | see record | SRC-1: `chapter1/context/main.py` | [RT-CLM-context-purpose](runtime.md#rt-clm-context-purpose), [EPI-CLM-grounding-source](#epi-clm-grounding-source) | report label exceeds predicate | No answer withdrawal, rerun or policy replacement is implemented by this consumer |
| [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate) | behavior/policy adaptation | implemented | [RT-OBJ-retry-policy](runtime.md#rt-obj-retry-policy) | non-truth-apt policy/content update: retry/circuit module proposal | Failure diagnosis and deterministic or model patch | see record | see record | see record | see record | Proposal, not established mechanism or transfer claim | Candidate source executes only during evaluation on inspected paths | see record | SRC-1: `chapter9/self-modifying-agent/evolution.py`, `chapter9/self-modifying-agent/llm_generator.py` | none | none | Diagnosis/predictions assert causal content; synthetic grouping and model proposal alone do not warrant that content |
| [RT-RTE-candidate-validation](runtime.md#rt-rte-candidate-validation) | check/evidence production | implemented | [RT-OBJ-retry-policy](runtime.md#rt-obj-retry-policy) | truth-apt transformation: entailed derivation | Compilation, deny-list, signatures and retry/circuit outcomes on supplied cases | see record | see record | see record | see record | Conditional bounded software checks, given trustworthy runner/image and encoding; not general safety or improved capacity | False checks feed release rejection; metrics do not independently install changes | see record | SRC-1: `chapter9/self-modifying-agent/evolution.py`, `chapter9/self-modifying-agent/sandbox_runner.py` | [RT-CLM-canary-decision](runtime.md#rt-clm-canary-decision) | none | Candidate/evaluator share process; bounded tests do not authenticate causal diagnosis |
| [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate) | disposition/acceptance | implemented | [RT-OBJ-retry-policy](runtime.md#rt-obj-retry-policy) | no content change | Changed candidate plus nonempty all-true supplied checks | see record | see record | see record | see record | Evidence-consuming eligibility against supplied checks, intended use shadow traffic with stable unchanged; no accepted general performance theory | Emits release_to_canary or reject_candidate manifest | see record | SRC-1: `chapter9/self-modifying-agent/evolution.py` | [RT-CLM-canary-decision](runtime.md#rt-clm-canary-decision) | eligibility is not activation | Direct callers can substitute check set; manifest expression does not enforce check-name completeness |
| [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate) | retention | implemented | [RT-OBJ-retry-policy](runtime.md#rt-obj-retry-policy) | no content change | Save candidate source, checks, diagnosis and manifest | see record | see record | see record | see record | Candidate ledger, including rejected proposals; not acceptance by storage | Failed-control results can guide later coding request | see record | SRC-1: `chapter9/self-modifying-agent/demo.py`, `chapter9/self-modifying-agent/run_experiment_9_6.py` | none | none | Retention of accepted and rejected artifacts is not post-acceptance lifecycle integration |
| [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate) | lifecycle integration | no route found within boundary | [RT-OBJ-retry-policy](runtime.md#rt-obj-retry-policy) | no content change | Accepted policy into stable operation | No installed-successor consumer in supplied selected paths | Not observed | No traced live installation | None established | No additional license from manifest | Stable remains unchanged in inspected demo/campaign | No live consumer established; evaluation authority remains separate | SRC-1: `chapter9/self-modifying-agent/demo.py`, `chapter9/self-modifying-agent/evolution.py`, `chapter9/self-modifying-agent/run_experiment_9_6.py` | [RT-CLM-canary-decision](runtime.md#rt-clm-canary-decision) | none | Bounded to selected candidate plane; other suite consumers unassessed |

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| [RT-CLM-context-purpose](runtime.md#rt-clm-context-purpose) | see record | SRC-1: `chapter1/context/agent.py`; doctrine/design | Ablation teaching intent | [RT-RTE-context-ablation](runtime.md#rt-rte-context-ablation), [EPI-RTE-grounding-check](#epi-rte-grounding-check), [EPI-RTE-grounding-report](#epi-rte-grounding-report) | None inspected | Context arms are wired; no retained intervention results inspected; completion and numeric matching do not identify task benefit | Implements a comparison/report mechanism | Importance/effect magnitude not established |
| [EPI-CLM-current-rates](#epi-clm-current-rates) | see record | SRC-1: `chapter1/context/agent.py`; doctrine/design in schema description | Description delivered to model | [EPI-RTE-currency-conversion](#epi-rte-currency-conversion) | None inspected | Constant table and calculation timestamp do not measure current exchange rates | Conditional conversion from shipped constants | Live-rate wording contradicted by implementation |
| [EPI-CLM-grounding-source](#epi-clm-grounding-source) | see record | SRC-1: `chapter1/context/grounding.py`; doctrine/design | Explicitly weaker than correctness, but labels unmatched figures as without evidence | [EPI-RTE-grounding-check](#epi-rte-grounding-check), [EPI-RTE-grounding-report](#epi-rte-grounding-report) | None inspected | Number matching omits arithmetic closure and actual provenance; observation presence forces abstention | A bounded reproducible text predicate | Does not establish that unmatched numbers were fabricated or lacked an evidential derivation |
| [RT-CLM-canary-decision](runtime.md#rt-clm-canary-decision) | see record | SRC-1: `chapter9/self-modifying-agent/evolution.py`; implementation and doctrine/design | Shadow-only eligibility, stable unchanged | [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate), [RT-RTE-candidate-validation](runtime.md#rt-rte-candidate-validation) | None inspected | Fixed cases and expected booleans; direct caller check substitution; no live traffic | Candidate admission against caller-supplied evidence | Not production activation, live rollback or exercised self-improvement |

## Bounded conclusion

**Imported assertions have unknown warrant.** PDF parsing preserves a URL and page association, but neither authenticates the author nor checks extraction against the document. Delivery of that result can affect the completion model without a content acceptance decision. Context retention is separate from delivery, and delivery is separate from compliance. See [EPI-RTE-pdf-import](#epi-rte-pdf-import), [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history) and [RT-RTE-context-ablation](runtime.md#rt-rte-context-ablation).

**Arithmetic produces conditional results, not source truth.** The calculator evaluates accepted syntax; currency conversion derives a rounded result from a fixed table and supplied amount. Neither check warrants the task's assumptions, amount provenance, real-world units or rate freshness. Model-generated replies and arbitrary code outputs remain semantically indeterminate without concrete inputs/outputs; failure to prove entailment is not evidence of ampliative conjecture. See [RT-RTE-calculation-path](runtime.md#rt-rte-calculation-path), [EPI-RTE-currency-conversion](#epi-rte-currency-conversion) and [RT-RTE-code-execution](runtime.md#rt-rte-code-execution).

**The numerical assessor has advisory force, not a truth or provenance veto.** Its target is extracted revenue-scale answer quantities compared with quantities available in task/tool text. It licenses the computed match/abstention classification, not actual derivation history. Its consumer warns and annotates reports; it does not reject the already returned answer or revise the agent. The no-observation arithmetic counterexample in [EPI-RTE-grounding-check](#epi-rte-grounding-check) bounds the stronger evidence wording. No supersession of the supplied runtime is required: its statement that this implementation was uninspected there is valid, and this report supplies the missing local assessment.

**Retry-policy acceptance is narrow but real at the manifest decision.** The intended use and scope are shadow eligibility with stable unchanged. The ordinary validator consumes proposed code and expected software outcomes; release requires a changed candidate and all supplied checks true. A direct manifest caller can bypass the normal check-set construction. Thus acceptance is evidence-consuming in the normal driver, but not a universal release authorization. Candidates, including rejects, are retained. The rejected-control summary can shape a later coding request; that does not install a successor or accept the model's causal explanation. See [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate) and [RT-RTE-candidate-validation](runtime.md#rt-rte-candidate-validation).

The diagnosis and policy module have localized content, and evaluation consumes the formal rule. The runtime separately supports implemented criticism and only afforded content-dependent iteration. Learning benefit, complete reflection, autonomous fulfillment of every theory-builder condition and exercised self-improvement remain independent unestablished properties, not a bundled negative. Missing installed live authority and subsequent causally dependent operation prevent attributing exercised self-improvement over this campaign horizon. The direct policy proposal/evaluation route still exists. See the theory and self-improvement account in [RT-RTE-policy-candidate](runtime.md#rt-rte-policy-candidate).

No accepted ampliative knowledge claim or post-acceptance stable integration is established in these selected routes. This is not a suite-wide absence: user-memory conflict handling, other evaluation/training mechanisms, external-host skills and available retained results remain unassessed. Provider parameter state and immutable answering-model identity also remain uninspected; neither inference calls nor symbolic candidate updates establish parametric learning. See [RT-CMP-context-model](runtime.md#rt-cmp-context-model), [RT-CMP-coding-model](runtime.md#rt-cmp-coding-model) and the coverage limits above.

## Shared records

### Operative objects

#### EPI-OBJ-pdf-result
Label: PDF tool observation

Part of: [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history)

Source-native identity: `parse_pdf` result carried as tool content in history. Representational form: natural-language page text with symbolic URL/page/metadata envelope. Storage substrate: returned Python dictionary, serialized into in-process tool history and optional caller reports. It is the PDF observation part, not the mixed container or model answer. SRC-1: `chapter1/context/agent.py`; see [EPI-RTE-pdf-import](#epi-rte-pdf-import) for supporting implementation passages and delivery limits.

#### EPI-OBJ-currency-result
Label: Currency tool observation

Part of: [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history)

Source-native identity: `convert_currency` result carried as tool content. Representational form: symbolic numeric result dictionary, interpreted as a financial assertion by the completion model. Storage substrate: Python dictionary and serialized in-process tool history. Distinct from PDF assertions and free-form final replies, with an arithmetic consumer before model interpretation. SRC-1: `chapter1/context/agent.py`; evidence in [EPI-RTE-currency-conversion](#epi-rte-currency-conversion).

#### EPI-OBJ-final-answer
Label: Terminal model reply

Part of: [RT-OBJ-conversation-history](runtime.md#rt-obj-conversation-history)

Source-native identity: terminal assistant message content selected as `final_answer`. Representational form: natural language, possibly containing numbers and formatting; storage substrate: live history, returned result and optional JSON report. A material part of the conversation container, not the entire container. Its claims and checks differ from imported observations. SRC-1: `chapter1/context/agent.py`; [RT-RTE-context-task](runtime.md#rt-rte-context-task) supplies termination evidence. The response can be a refusal; nonempty text establishes completion only. [EPI-RTE-grounding-check](#epi-rte-grounding-check) supplies the separate numerical evaluator evidence.

### Routes

#### EPI-RTE-pdf-import
Label: PDF import observation

Part of: [RT-RTE-context-task](runtime.md#rt-rte-context-task)

Endpoints/progression: local path or URL → bytes → `pypdf.PdfReader` → per-page extracted text → tool result → selected later provider request. Owner: `ToolRegistry.parse_pdf` and the context loop. Object: [EPI-OBJ-pdf-result](#epi-obj-pdf-result). URL and page structure preserve an association, not independent source truth. This is the PDF acquisition subroute of the supplied task route; it does not redefine its dispatcher or final-answer semantics. SRC-1: `chapter1/context/agent.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: URL, page count, per-page text and metadata, or an error dictionary.
- Later read-back: Same live agent can deliver retained tool messages on later task calls; reset/replacement discards them.
- Delegated visibility: Provider gets serialized tool content only when context mode permits; there is no separate extraction worker.
- Selection predicate: Model/direct caller supplies path or URL; protocol/path tests choose local file versus HTTP retrieval; page iteration extracts all parsed pages.
- Invalidation or expiry: No source revalidation or endorsement expiry; local history reset governs live retention.
- Activation or effect: Import and provider delivery are wired; changed model behavior unobserved. Consumer: completion model; channel: tool message; force: informational/advisory; horizon: later visible turns/tasks on the live agent.
- Evidence limits: No content evaluator, author-authentication check or extraction-fidelity comparison inspected here; source warrant unknown. Parsing success is not an acceptance decision.

> text = page.extract_text()
> text_content.append({
>     "page": page_num,
>     "text": text
> })
> --- `chapter1/context/agent.py`

#### EPI-RTE-currency-conversion
Label: Currency conversion observation

Part of: [RT-RTE-context-task](runtime.md#rt-rte-context-task)

Endpoints/progression: amount/currency arguments → normalization → fixed-rate lookup → USD intermediate → rounded target amount → tool result → later model request. Owner: `ToolRegistry.convert_currency` and the loop. Object: [EPI-OBJ-currency-result](#epi-obj-currency-result). Evaluator/condition: numeric parsing and membership in shipped table; arithmetic domain is conversion under those constants. This is the conversion subroute, not the whole supplied task loop. SRC-1: `chapter1/context/agent.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Original amount, normalized currencies, rounded converted amount/rate and calculation timestamp, or error.
- Later read-back: Retained tool observation can reach a later task invocation on the same live agent, subject to context mode.
- Delegated visibility: Provider receives serialized conversion result, not a live exchange-rate feed.
- Selection predicate: Dispatcher/direct call chooses conversion; unsupported currency returns error before arithmetic.
- Invalidation or expiry: No rate refresh or financial-validity expiry; history reset/replacement ends live retention.
- Activation or effect: Conditional calculation is wired; actual effect on answers unobserved. Consumer: completion model; channel: tool message; force: informational/advisory; horizon: subsequent visible turns/tasks.
- Evidence limits: Static rate premises lack independently inspected financial warrant. No market source or evidence-consuming rate acceptance exists in this method; timestamp records now, not rate vintage.

Concrete deduction, not execution: numeric input 100 USD to EUR passes both table memberships; USD intermediate is 100/1.0, target is 100×0.92, returned conversion is 92.0. The result is entailed by the implementation and assumed inputs, not by knowledge of present market rates.

> "USD": 1.0,
> "EUR": 0.92,
> --- `chapter1/context/agent.py`

> usd_amount = amount / exchange_rates[from_currency]
> converted_amount = usd_amount * exchange_rates[to_currency]
> --- `chapter1/context/agent.py`

> "converted_amount": round(converted_amount, 2),
> "exchange_rate": round(exchange_rates[to_currency] / exchange_rates[from_currency], 4),
> "timestamp": datetime.now().isoformat()
> --- `chapter1/context/agent.py`

#### EPI-RTE-grounding-check
Label: Numerical grounding check

Part of: [RT-RTE-context-ablation](runtime.md#rt-rte-context-ablation)

Endpoints/progression: sent API message snapshots → tool-message quantities → answer/task quantities → approximate matching → verdict and unsupported list. Owner: ablation driver and `assess_groundedness`. Target: revenue-scale figures extracted from the terminal answer, relative to task and delivered tool-message figures. Evaluator: regex/scaling extraction, floor 100,000, relative tolerance 0.001, and a fixed branch order. It does not compare propositions or reference task answers. Object: [EPI-OBJ-final-answer](#epi-obj-final-answer). This subroute fills the evaluator implementation gap expressly left by the supplied ablation record, without replacing that record. SRC-1: `chapter1/context/grounding.py`, `chapter1/context/main.py`, implementation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Verdict, observation count, extracted answer quantities and unsupported subset.
- Later read-back: inapplicable — current answer assessment does not modify retained agent content or evaluator state for later invocations.
- Delegated visibility: Local program consumes sent-message snapshots, not withheld local tool results; no provider call is made by this assessor.
- Selection predicate: Tool-role message quantities are extracted with floor zero; answer/task use the default floor. A nonempty observations list forces not_assessable after the no-answer branch.
- Invalidation or expiry: Recomputed per returned test; no retained evidence acceptance or withdrawal mechanism.
- Activation or effect: Check wiring is implemented; report consumption is separately [EPI-RTE-grounding-report](#epi-rte-grounding-report). The function itself returns evidence without a behavioral veto.
- Evidence limits: Matching establishes availability of a similar numeral, not actual use or truth; unmatched output can be valid arithmetic. Regex extraction is not semantic parsing, and smaller claims are ignored.

Operating mode: bounded case/mode comparison. Human supplies task/case/mode launch inputs; software computes verdict; no model judges or vetoes it. Answer oracle: none for task correctness; the software predicate is the oracle only for its own defined matching classification. This route does not admit a product or machinery update.

Counterexample to the stronger evidence claim, deduced without executing target code: task `Add 100000 and 200000`, answer `300000`, observations `[]`. Extraction returns task quantities 100000 and 200000, answer quantity 300000. Both relative differences exceed 0.001, so the answer is marked ungrounded, although the asserted sum follows from task evidence. Conversely, copying a task number can pass while asserting the wrong relation. Therefore the result is not a derivation-provenance or correctness oracle.

> QUANTITY_FLOOR = 100_000.0
> --- `chapter1/context/grounding.py`

> DEFAULT_REL_TOL = 1e-3
> --- `chapter1/context/grounding.py`

> known = extract_quantities(task_text) + list(observations)
> unsupported = [q for q in quantities if not matches_any(q, known)]
> --- `chapter1/context/grounding.py`

> elif observations:
>     # With real observations in context there is no honest way to tell a
>     # correct mental calculation from an invented number, so say so instead
>     # of manufacturing a verdict.
>     result["verdict"] = "not_assessable"
> elif not quantities:
>     result["verdict"] = "no_quantities"
> elif not unsupported:
>     result["verdict"] = "grounded"
> else:
>     result["verdict"] = "ungrounded"
> --- `chapter1/context/grounding.py`

> for turn in result["trajectory"].api_turns
> for message in (turn.get("request") or {}).get("messages", [])
> --- `chapter1/context/main.py`

#### EPI-RTE-grounding-report
Label: Grounding report consumption

Part of: [RT-RTE-context-ablation](runtime.md#rt-rte-context-ablation)

Endpoints/progression: grounding dictionary → test result → logger warning, analysis counts/failure reason and displayed table. Owner: `AblationTestSuite`. Target/condition: verdict equal to ungrounded, with table mapping for other verdicts. This is the report-consumption subroute, not the numerical check or candidate release. SRC-1: `chapter1/context/main.py`, implementation. Closest records: parent ablation route and [EPI-RTE-grounding-check](#epi-rte-grounding-check); distinct function and consumer force.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Summary fields, unsupported counts/modes and advisory failure reason; warnings/table output when called.
- Later read-back: inapplicable — inspected consumers do not reload the report into future agent or policy decisions.
- Delegated visibility: Operator sees report labels; the checked answer has already returned from the model.
- Selection predicate: Equality to ungrounded selects warning, counts and unsupported-number failure reason; printed rows use verdict-to-label mapping.
- Invalidation or expiry: Current report generation only; no implemented answer withdrawal or claim endorsement lifecycle.
- Activation or effect: Advisory reporting is wired. Consumer: logger/report builder/operator; channel: test-result fields and displayed table; force: advisory classification; horizon: this comparison report. No enforcing correctness gate or model repair follows.
- Evidence limits: No observed report inspected; report labels cannot enlarge the check's numeric-domain license or establish actual provenance.

Operating mode: bounded ablation reporting; program decides labels, human reads them; no per-content human acceptance, successor selection or task reference oracle.

> if test_result["grounding_verdict"] == "ungrounded":
>     logger.warning(
>         "Answer states %d figure(s) with no observation behind them: %s",
>         len(test_result["unsupported_quantities"]),
>         test_result["unsupported_quantities"],
>     )
> --- `chapter1/context/main.py`

> mode_analysis["failure_reason"] = (
>     "Answered with figures no tool observation supports"
> )
> --- `chapter1/context/main.py`

### Claims

#### EPI-CLM-current-rates
Label: Current exchange rates

Claimed operation: the tool schema says conversion uses current exchange rates. SRC-1: `chapter1/context/agent.py`, doctrine/design delivered to the model. No counterpart among supplied claims: [RT-CLM-context-purpose](runtime.md#rt-clm-context-purpose) concerns ablation intent, and [RT-CLM-canary-decision](runtime.md#rt-clm-canary-decision) concerns candidate eligibility. The runtime prose already notes this mismatch; this declaration isolates the consequential tool claim rather than duplicating a supplied claim record.

> "description": "Convert an amount from one currency to another using current exchange rates",
> --- `chapter1/context/agent.py`

#### EPI-CLM-grounding-source
Label: Grounding source warrant

Claimed warrant: with no observations, figures not supplied by task text are classified as lacking evidence. SRC-1: `chapter1/context/grounding.py`, doctrine/design. Distinct from the supplied teaching-purpose and canary claims; closest is [RT-CLM-context-purpose](runtime.md#rt-clm-context-purpose), which names purpose but not this provenance license. The implemented counterexample is in [EPI-RTE-grounding-check](#epi-rte-grounding-check). The source itself distinguishes grounding from correctness, but that distinction does not remedy the arithmetic-closure gap.

> The model saw no observations yet stated figures the task never
> gave it. Whatever produced them, it was not evidence.
> --- `chapter1/context/grounding.py`
