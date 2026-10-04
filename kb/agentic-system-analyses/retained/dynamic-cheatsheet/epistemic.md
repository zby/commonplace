---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of Dynamic Cheatsheet at the frozen repository commit"
run-id: AAS-2026-10-04-dynamic-cheatsheet-01
reviewed-boundary: "5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9"
---

# Dynamic Cheatsheet epistemic report

## Source-and-claim boundary

The whole-system boundary is the Dynamic Cheatsheet repository at `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9` (see boundary Source register, `SRC-1`). This report assesses how its shipped variants generate, curate, select, evaluate, retain and reuse candidate answers and strategies. Provider internals and live model behavior, API keys, remote data, deployment permissions, committed historical results, and actual benchmark runs are outside the evidence. Direct source reads supplement the supplied runtime account at the same frozen commit; no target code or notebook was executed.

The system produces candidate answers and, in cumulative variants, candidate cheatsheet text. It imports dataset questions, targets and any prior answer strings; retrieval ranks past examples by cosine similarity of precomputed vectors. The evaluator compares a returned answer with task targets, but its boolean is used for printed counts, not as an admission condition for the answer or cheatsheet. The curator's natural-language correctness instructions do not establish a checked, evidence-consuming acceptance decision: the code accepts any extractable `<cheatsheet>` block. No shipped route establishes warranted new knowledge, answer acceptance for later reliance, or improvement attributable to the update loop.

| Entry point or operation | Source path | Coverage | Limit or prevented conclusion |
|---|---|---|---|
| Benchmark dispatch, state carry-forward, checkpoint and resume | `run_benchmark.py` | RT-RTE-benchmark-invocation, RT-RTE-checkpoint-resume; directly inspected | No run evidence; actual operation and effects unestablished. |
| Six approach branches, prompts, extraction and provider calls | `dynamic_cheatsheet/language_model.py`, `dynamic_cheatsheet/utils/extractor.py`, `prompts/` | RT-RTE-cumulative-update, RT-RTE-retrieval-context, RT-RTE-full-history, RT-RTE-prompt-configuration; directly inspected | Model outputs and their correctness unobserved. Retrieval vector contents and provenance not analyzed. |
| Benchmark evaluator functions and task dispatch | `dynamic_cheatsheet/utils/evaluation.py`, `run_benchmark.py` | EPI-RTE-answer-extraction, EPI-RTE-answer-evaluation; directly inspected in addition to runtime | Shipped task checks are characterized; no execution or external validity assessment. |
| Notebook carry-forward and later result consumption | `ExampleUsage.ipynb`, `EvaluatingResults.ipynb` | Directly covered by RT-RTE-benchmark-invocation; notebook cells inspected without execution | No observed caller behavior or historical result audit. |
| Code execution paths | `dynamic_cheatsheet/utils/execute_code.py`, provider calls in `dynamic_cheatsheet/language_model.py` | RT-RTE-local-code, RT-RTE-provider-interpreter and RT-BAP paths | Operational authority is material but not an epistemic check; deployment isolation remains unassessed. |

Design claims assessed: EPI-CLM-persistent-memory, EPI-CLM-zero-shot, and EPI-CLM-performance. The README's performance examples cite reported outcomes, while the boundary excludes result artifacts and supplies no execution evidence; no measured claim is verified here. No relevant source-access gap was identified within the registered whole-system boundary.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| EPI-OBJ-answer | Extracted final answer text; truth-apt relative to the task question and evaluator's task target | Answer produced for the current benchmark item | SRC-1 `dynamic_cheatsheet/utils/extractor.py` | Extraction can select text by delimiters; no semantic fidelity check. |
| RT-OBJ-cheatsheet | Candidate natural-language strategies and solutions; truth-apt where it asserts problem-solving propositions | Reusable evolving memory supplied to later model calls | SRC-1 `dynamic_cheatsheet/language_model.py`; `prompts/curator_prompt_for_dc_cumulative.txt` | Provenance and correctness of entries are not encoded or checked by code. |
| RT-OBJ-retrieval-vectors | Dense numeric vectors; their truth-apt meaning is not determinable from supplied evidence | Rank prior input/output examples for retrieval | SRC-1 `run_benchmark.py`; `dynamic_cheatsheet/language_model.py` | Contents, model, and vector semantics/provenance not analyzed. |
| Prior input/output pairs (`RT-RTE-retrieval-context`, `RT-RTE-full-history`) | Inputs are imported questions; outputs are imported candidate answers, truth-apt relative to their questions | Prompt context for subsequent generation | SRC-1 `run_benchmark.py`; `dynamic_cheatsheet/language_model.py` | No checks establish correctness before inclusion; task datasets are not analyzed. |
| Dataset target | Truth-apt task reference under each task's intended answer criterion | Evaluator comparison target, not shown as generation or curation input | SRC-1 `run_benchmark.py`; `dynamic_cheatsheet/utils/evaluation.py` | Dataset target quality and intended-use validity are not assessed. |

## Authority-route ledger

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| RT-RTE-benchmark-invocation; RT-RTE-cumulative-update | content transformation | implemented | EPI-OBJ-answer; RT-OBJ-cheatsheet | truth-apt transformation: indeterminate (model-generated answer and proposed strategy may be entailed by supplied context or may add propositions; model processing and candidate semantics are inaccessible, so distinguishing derivation from conjecture requires an inspected model process or suitable execution evidence) | Question plus supplied context to candidate answer; prior sheet plus question/output to proposed sheet | Provider model proposes answer and curator response; no separately specified answer oracle in generation/curation. Cumulative prompt asks curator to assess the answer, but code does not parse a correctness verdict. Open-ended benchmark item sequence; no documented improvement trigger. | On selected cumulative approach; each round generates, then curates | Answer and tagged replacement may be returned; no observed result | Candidate text supplied to caller and later prompt; no implemented epistemic license | None established; source warrant unknown | Parseable sheet replacement changes later model context without answer-check admission | Later generator; natural-language prompt; advisory context input, across later benchmark items while carried | SRC-1 `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/extractor.py`; `prompts/curator_prompt_for_dc_cumulative.txt` | EPI-CLM-persistent-memory; EPI-CLM-zero-shot | Curator correctness guidance exceeds implemented checking | Model reasoning and outputs unobserved; candidate status only. |
| EPI-RTE-answer-extraction | content transformation | implemented | EPI-OBJ-answer | truth-apt transformation: indeterminate (candidate text is selected from tagged or marked response; semantic preservation cannot be established; could be formatting-only extraction or could omit/alter relevant qualifications; compare source answer with extracted text to decide) | Raw generator response to extracted final answer | Deterministic delimiter rules; no truth evaluator | On response containing `<answer>` or `FINAL ANSWER`; before benchmark comparison | Extracted substring or “No final answer found” | Extracted candidate becomes evaluator input and caller output | None; no check of source truth or extraction fidelity | Changes which response text is evaluated and returned | Benchmark evaluator and caller; extracted answer field; current result and any saved output | SRC-1 `dynamic_cheatsheet/utils/extractor.py`; `dynamic_cheatsheet/language_model.py` | none | none | No target execution; concrete code establishes extraction rules but not semantic preservation for actual outputs. |
| EPI-RTE-answer-evaluation | check/evidence production | implemented | EPI-OBJ-answer; dataset target | no content change | Whether extracted answer meets task-specific target criterion (Game of 24 arithmetic and digit use; exact normalized match; multiple-choice matching; equation evaluation) | Python evaluator, using dataset target or input; task-specific, narrow check. No proposed/decided human role in the in-loop dispatch; evaluator result is a boolean. Target is the task target, not an oracle for general explanation or reusable strategy. | Immediately after answer and cheatsheet have already been assigned; once per newly processed benchmark item | Boolean true/false and cumulative printed count; no observed result | Count/console reporting only; not a condition on state update, retained answer or future use | A passing boolean supports only the implemented task criterion for that answer and input | Does not permit/block answer inclusion or cheatsheet update; no acceptance gate | Runner console and saved JSONL consumer; result count/reporting; benchmark run | SRC-1 `run_benchmark.py`; `dynamic_cheatsheet/utils/evaluation.py` | EPI-CLM-performance | none | Evaluation correctness and target quality are not assessed; no runtime evidence. |
| RT-RTE-retrieval-context | operational admission/selection/consumption | implemented | RT-OBJ-retrieval-vectors; prior input/output pairs | no content change to selected examples; similarity ranking selects context | Which prior examples enter the current prompt | Program computes cosine similarity and top-k; similarity is not a correctness evaluator | Per query in retrieval variants, before generation | Selected prior input/output strings; no observed selection | Ranking/selection force over prompt context | No truth or warrant licensed by similarity | Changes which prior examples the model receives; cannot certify those examples | Generator model; prompt context; current invocation | SRC-1 `dynamic_cheatsheet/language_model.py`; `run_benchmark.py` | none | none | Vector provenance and actual relevance unassessed. |
| RT-RTE-full-history | operational admission/selection/consumption | implemented | Prior input/output pairs | truth-apt transformation: non-ampliative reshaping (concatenation and labels) | Which prior examples enter current prompt | Fixed inclusion of accumulated available pairs; no evaluator | Each full-history invocation | Concatenated history; no observed selection | Prompt-context supply | No truth or warrant licensed | Makes all accumulated pairs available to generator | Generator model; prompt context; later item in run | SRC-1 `dynamic_cheatsheet/language_model.py` | none | none | Prior answer correctness and context-limit effects unobserved. |
| RT-RTE-checkpoint-resume | retention | implemented | RT-OBJ-cheatsheet; candidate answers in JSONL | truth-apt transformation: non-ampliative reshaping (serialization and reload) | Persisted returned sheet and outputs | File/path and partial parameter checks; no content evaluator | After each evaluated item and on continuation | JSONL writes/reloaded state; no supplied run artifact | Makes prior outputs and sheet available to a resumed invocation | None added by serialization | State is reintroduced into future calls if resumed | Runner; JSONL read/write; later invocation, across process restarts | SRC-1 `run_benchmark.py` | EPI-CLM-persistent-memory | none | File integrity, actual persistence, and activated behavior unobserved. |

Quotes supporting the material findings:

> cheatsheet = output_dict["final_cheatsheet"]
> --- `run_benchmark.py`

> if result:
>             correct_so_far += 1
> --- `run_benchmark.py`

> output = remove_punctuation(output)
>     output = convert_newline_to_space(output)
>     if target == output:
> --- `dynamic_cheatsheet/utils/evaluation.py`

> if "<cheatsheet>" in response:
>         try:
>             txt = response.split("<cheatsheet>")[1].strip()
>             txt = txt.split("</cheatsheet>")[0].strip()
>             return txt
> --- `dynamic_cheatsheet/utils/extractor.py`

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| EPI-CLM-persistent-memory | LMs can build/reference a growing knowledge base during inference; memory is persistent and evolving | SRC-1 `README.md` (doctrine/design) | Caller carries returned text; runner writes and reloads it; cumulative prompt describes iterative refinement | RT-RTE-cumulative-update; RT-RTE-checkpoint-resume | None | No causal experiment; no operation trace | Implemented text proposal, carry-forward, serialization and reload paths support a bounded architectural memory mechanism | “Knowledge base” correctness and improved future capacity are not established; persistence depends on caller/files and behavior after reuse is unobserved. |
| EPI-CLM-zero-shot | Performance improves without ground-truth labels or human feedback | SRC-1 `README.md` (doctrine/design) | Shipped generator/curator prompts and benchmark evaluator | RT-RTE-cumulative-update; EPI-RTE-answer-evaluation | None | No causal experiment; no operation trace | Model generation and curation code do not pass dataset targets into the curator path; benchmark runner separately uses targets after answer generation | “Improves” is unsupported here; labels exist in evaluator path, though not shown as curator/generator inputs. Human feedback is not part of the inspected automated loop, but deployment scope is unobserved. |
| EPI-CLM-performance | Reported gains on math, puzzles and knowledge-intensive tasks | SRC-1 `README.md` (doctrine/design, reports results) | README advertises task scores; shipped evaluators define some benchmark criteria | EPI-RTE-answer-evaluation | None; committed results excluded by boundary | No causal experiment or reproducible results available | Only that the repository makes these reports; no measured gain is supported by inspected implementation or supplied operation evidence | Performance and attribution remain unverified; no component effect can be inferred. |

## Bounded conclusion

Dynamic Cheatsheet has implemented routes that generate answer candidates and natural-language cheatsheet candidates, select prior examples by supplied vector similarity, and carry or reload text for later prompts. The answer and cheatsheet propositions have no source warrant established by these mechanisms. The curator prompt asks a model to check correctness and usefulness, but the code admits any extractable tagged text and does not use the benchmark evaluator as an admission check. The evaluator checks an extracted answer against a narrow task target only after state assignment; its boolean changes displayed counts, not answer/cheatsheet retention or future behavior. Therefore the system's shipped code supports candidate generation, task-scoped checking and operational reuse, but not an evidence-consuming acceptance decision for reusable knowledge. Later behavioral effect, improvement, performance reports, provider behavior, retrieval relevance and deployed code-execution authority remain unobserved or outside the boundary. No single epistemic verdict for all variants follows: default generation has no sheet update; retrieval and full-history variants provide different context; cumulative variants admit model-proposed sheet text.

## Shared records

### Operative objects

#### EPI-OBJ-answer — Extracted final answer

- Source-native identity: `final_answer`, the extracted answer returned by `advanced_generate` and sent to task evaluation.
- Representational form: natural-language or symbolic answer text interpreted by task-specific evaluator code and potentially by callers.
- Storage substrate: Python string in the current invocation; also serialized in result JSONL by the benchmark runner.
- Possible duplicate comparison: RT-OBJ-cheatsheet is the closest supplied object but denotes carried reference text, not the per-item extracted answer; distinct identity, supported by separate return fields and consumers.
- Evidence: [SRC-1: `dynamic_cheatsheet/language_model.py`; `dynamic_cheatsheet/utils/extractor.py`; `run_benchmark.py`]

### Routes

#### EPI-RTE-answer-extraction — Answer extraction

- Endpoints and progression: raw generator response → delimiter-based extraction → `final_answer` candidate → task evaluator/caller.
- Owner: `extract_answer` selects text; `advanced_generate` returns it.
- Context/state/action effects: transforms raw response into the candidate passed to evaluation and returned to the caller.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: extracted substring, or `No final answer found` when recognized format extraction fails.
- Later read-back: inapplicable — this route extracts an answer; persistence by the runner is separately recorded in RT-RTE-checkpoint-resume.
- Delegated visibility: extracted answer is visible to task evaluator, caller, and saved result row.
- Selection predicate: `<answer>...</answer>` takes precedence; otherwise response must contain `FINAL ANSWER` and a parseable quoted code fence.
- Invalidation or expiry: inapplicable — no candidate cache or invalidation mechanism is part of extraction.
- Activation or effect: extracted text becomes the evaluated and returned answer; semantic effect is unobserved.
- Evidence limits: no actual response or run supplied; code defines string operations but not semantic fidelity for runtime outputs.
- Evidence: [SRC-1: `dynamic_cheatsheet/utils/extractor.py`; `dynamic_cheatsheet/language_model.py`]

> if "<answer>" in response:
>         # <answer> (content) </answer>
> --- `dynamic_cheatsheet/utils/extractor.py`

#### EPI-RTE-answer-evaluation — Task answer evaluation

- Endpoints and progression: extracted answer plus task input/target → task-selected evaluator → boolean → printed aggregate count.
- Owner: runner selects the evaluator; Python functions apply task-specific comparisons.
- Context/state/action effects: tests a candidate against a narrow benchmark criterion and increments a displayed count on true.
- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: boolean for the task-specific test.
- Later read-back: inapplicable — evaluator boolean is not retained as a later model input in the inspected route.
- Delegated visibility: runner sees the boolean; target is read by evaluator, not supplied to generation in this dispatch.
- Selection predicate: task name dispatches Game of 24 arithmetic/digit validation, normalized exact match, multiple-choice match, or equation evaluation.
- Invalidation or expiry: inapplicable — no retained evaluator decision or invalidation protocol is shown.
- Activation or effect: changes `correct_so_far`/printed benchmark count only; no admission, rejection, or update gate.
- Evidence limits: no execution trace; dataset targets and task criterion validity not independently assessed.
- Decision roles: runner chooses evaluator by task; code decides the boolean; no human veto in the inspected loop. Dataset target is an answer reference for that item, not a general truth oracle.
- Operating mode: bounded benchmark dataset sequence; no evidence that its outcomes trigger a later improvement experiment or change the evaluator.
- Evidence: [SRC-1: `run_benchmark.py`; `dynamic_cheatsheet/utils/evaluation.py`]

> if args.task == "GameOf24":
>             result = eval_for_GameOf24(original_input, final_answer)
> --- `run_benchmark.py`

### Claims

#### EPI-CLM-persistent-memory — Persistent evolving memory claim

- Claimed operation: LMs build and reference a growing knowledge base during inference.
- Source: [SRC-1: `README.md`]
- Closest supplied IDs and distinct identity: none; RT-OBJ-cheatsheet is an implementation object, not this public design claim.

> * **Persistent Memory**: Allows LMs to build and reference a growing knowledge base during inference
> --- `README.md`

#### EPI-CLM-zero-shot — Zero-shot improvement claim

- Claimed operation: performance improvement without ground-truth labels or human feedback.
- Source: [SRC-1: `README.md`]
- Closest supplied IDs and distinct identity: none; claim is distinct from RT-RTE-cumulative-update, which is a mechanism.

> * **Zero-Shot Learning**: Improves performance without ground-truth labels or human feedback
> --- `README.md`

#### EPI-CLM-performance — Reported benchmark gains

- Claimed operation: increased task accuracy on mathematics, puzzles and knowledge-intensive tasks.
- Source: [SRC-1: `README.md`]
- Closest supplied IDs and distinct identity: none; reported performance claim is not the historical result artifact excluded by the boundary.

> * **Mathematics**: Claude 3.5 Sonnet's accuracy more than doubled on AIME math exams by retaining algebraic insights
> --- `README.md`
