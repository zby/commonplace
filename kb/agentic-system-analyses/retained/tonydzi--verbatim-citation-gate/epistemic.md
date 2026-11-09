---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of verbatim-citation-gate: normalized occurrence, source-relative support, parser admission and benchmark warrant."
run-id: AAS-2026-11-08-verbatim-citation-gate-d205c9f72d5a-01
reviewed-boundary: "2113d603031a554ed901a44648307bd3b711ea10"
---

# verbatim-citation-gate epistemic report

## Source-and-claim boundary

This report asks what the auditor establishes about a supplied citation, and what authority its results actually carry. The [boundary and Source register](boundary.md#source-register) supply SRC-1 and the frozen subsystem boundary. The library, exported alternatives, shipped examples and evaluation machinery are included; production retrieval, citation generation, provider internals and downstream answer admission are excluded. Their absence from the acquired source prevents conclusions about source truth, actual model accuracy, or end-to-end user protection.

The runtime is provisional but its principal dispatch and bypass findings survive direct source inspection. No supersession is needed. [RT-CLM-closed-judge](runtime.md#rt-clm-closed-judge) identifies a real mismatch, retained below. Additional public warrant claims are [EPI-CLM-citation-support](#epi-clm-citation-support) and [EPI-CLM-benchmark-detection](#epi-clm-benchmark-detection). No independently inspected execution or intervention was supplied. Committed benchmark results are an available result artifact, not a trace proving which code produced it.

| Entry point or operation | SRC-1 source path | Coverage and records |
|---|---|---|
| Public API and dispatch | `src/verbatim_citation_gate/__init__.py`, `src/verbatim_citation_gate/judge.py` | Direct complete reads; [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation), [RT-RTE-judge-support](runtime.md#rt-rte-judge-support) |
| Normalize, quote matching, cache | `src/verbatim_citation_gate/gate.py` | Direct complete read; [EPI-RTE-quote-check](#epi-rte-quote-check); cache is bounded memoization, not admission |
| Resolve/span alternative | `src/verbatim_citation_gate/gate.py` | Direct complete read; [RT-RTE-span-gate](runtime.md#rt-rte-span-gate) |
| Prompt and response parser | `src/verbatim_citation_gate/judge.py` | Direct complete read; [RT-OBJ-judge-system](runtime.md#rt-obj-judge-system), [EPI-RTE-verdict-admission](#epi-rte-verdict-admission) |
| Shipped result consumers | `examples/demo.py`, `examples/quickstart.py` | Direct complete reads; [EPI-RTE-example-display](#epi-rte-example-display); constant callbacks and printing, not semantic evaluation |
| Benchmark acquisition, case construction, measurement | `bench/build_corpus.py`, `bench/hard_cases.py`, `bench/bench_gate.py` | Direct complete reads; [EPI-RTE-benchmark-check](#epi-rte-benchmark-check) |
| Benchmark claims and saved output | `bench/README.md`, `bench/results.json` | Direct complete reads; [EPI-CLM-benchmark-detection](#epi-clm-benchmark-detection); no authenticated generating trace |
| Regression tests | `tests/test_gate.py` | Direct bounded symbol/assertion search plus supplied runtime inspection; [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation), [RT-RTE-span-gate](runtime.md#rt-rte-span-gate); no tests executed |
| Packaging/CLI registration | `pyproject.toml` | Direct complete read; no packaged CLI, hook or tool registration here; exports above are callable operations |
| Product/release admission | `GOVERNANCE.md`, `.github/workflows/tests.yml`, `.github/workflows/publish.yml` | Supplied runtime findings only; [RT-RTE-release-admission](runtime.md#rt-rte-release-admission); actual deployed approvals unobserved |
| Saved abstracts | `bench/corpus.json` | Available but uninspected; builder and result summary inspected instead. Prevents corpus-content/provenance audit or independent metric recomputation |
| Presentation and project metadata | `docs/index.html`, `docs/make_demo_gif.py`, `docs/demo.gif`, `FOR-ROBOTS.md`, `AGENTS.md`, `CHANGELOG.md`, `SECURITY.md`, `CITATION.cff` | Not substantively inspected; additional presentation claims and historical evidence not assessed; no repository-complete negative follows |

The inspected paths establish no provider-parameter update. The callback component's parameter storage, exact model version and mutable endpoint remain as limited in [RT-CMP-llm-call](runtime.md#rt-cmp-llm-call); offline example callbacks contain no model. Missing provider evidence is not evidence that an enclosing model cannot learn.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-docs](#epi-obj-docs) | Supplied source assertions, claim, and quoted assertion where the input expresses one | see [EPI-OBJ-docs](#epi-obj-docs) | SRC-1, `src/verbatim_citation_gate/judge.py` | Caller provenance and truth unknown; arbitrary strings need not express propositions |
| [EPI-OBJ-gate-result](#epi-obj-gate-result) | Proposition about normalized occurrence or valid span, not claim truth | see [EPI-OBJ-gate-result](#epi-obj-gate-result) | SRC-1, `src/verbatim_citation_gate/gate.py` | Matching equivalence is narrower than semantic fidelity |
| [EPI-OBJ-verdict](#epi-obj-verdict) | Source-relative support classification; self-estimated confidence is not calibrated warrant | see [EPI-OBJ-verdict](#epi-obj-verdict) | SRC-1, `src/verbatim_citation_gate/judge.py` | Valid vocabulary does not imply sound judgment |
| [EPI-OBJ-reasoning](#epi-obj-reasoning) | Callback explanation, if supplied | see [EPI-OBJ-reasoning](#epi-obj-reasoning) | SRC-1, `src/verbatim_citation_gate/judge.py` | Missing reasoning defaults empty; dispatcher discards it |
| [RT-OBJ-judge-system](runtime.md#rt-obj-judge-system) | Policy rather than an accepted world claim | see [RT-OBJ-judge-system](runtime.md#rt-obj-judge-system) | SRC-1, `src/verbatim_citation_gate/judge.py` | Delivery is not compliance |
| [EPI-RTE-benchmark-check](#epi-rte-benchmark-check) (evaluation material) | Constructed expected labels, per-case comparisons, aggregate rates | see [EPI-RTE-benchmark-check](#epi-rte-benchmark-check) | SRC-1, `bench/bench_gate.py`, `bench/results.json` | Saved results do not authenticate execution or generalization |

## Authority-route ledger

Route ID: [EPI-RTE-quote-check](#epi-rte-quote-check)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-docs](#epi-obj-docs)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Original strings to normalized matching strings
Evaluator/condition and domain: Unicode and typography rules; semantic preservation is not a checked property
Activation and timing: Before occurrence checking, including direct normalize calls
Possible or observed result: Canonicalized strings; see [EPI-RTE-quote-check](#epi-rte-quote-check)
Implemented force: Fixed string transformation
Epistemic authority and scope: Matching equivalence only; original source truth remains unknown
Operational authority: Changes what counts as an occurrence
Behavioral-authority path: quote_gate through normalized strings; enforcing for this predicate; current call
Evidence source ID and local anchor: SRC-1, `src/verbatim_citation_gate/gate.py`
Claim IDs: none
Mismatch marker: Normalized identity is not byte identity.
Gap/limit: Non-ampliative reshaping may fit particular typography repairs, but arbitrary inputs lack a checked interpretation. Entailment and non-entailment are not generally established.

Route ID: [EPI-RTE-quote-check](#epi-rte-quote-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-gate-result](#epi-obj-gate-result)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Occurrence of a contentful normalized quote in attributed/other supplied document
Evaluator/condition and domain: Contiguous substring plus boundary predicate; supplied strings only
Activation and timing: Direct quote_gate, or first stage of audit
Possible or observed result: see [EPI-RTE-quote-check](#epi-rte-quote-check)
Implemented force: Classification return
Epistemic authority and scope: Algorithmic occurrence proposition from supplied strings, not validity of the source or citation sufficiency
Operational authority: Provides found/misattributed/not_found to consumer
Behavioral-authority path: Dispatcher via gate result; enforcing selection only there; one audit
Evidence source ID and local anchor: SRC-1, `src/verbatim_citation_gate/gate.py`
Claim IDs: [EPI-CLM-citation-support](#epi-clm-citation-support)
Mismatch marker: none
Gap/limit: No operation independently observed.

Route ID: [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-gate-result](#epi-obj-gate-result)
Content/update relation: no content change
Transition or check target: Permission to invoke callback
Evaluator/condition and domain: Exact found result and callback presence
Activation and timing: After quote check
Possible or observed result: see [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation)
Implemented force: Deterministic early return
Epistemic authority and scope: No new support warrant; found alone is not acceptance of the claim
Operational authority: see [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation)
Behavioral-authority path: audit_citation via local branch; enforcing callback veto; current audit
Evidence source ID and local anchor: SRC-1, `src/verbatim_citation_gate/judge.py`
Claim IDs: [EPI-CLM-citation-support](#epi-clm-citation-support)
Mismatch marker: Direct judge and deterministic APIs are alternate contracts.
Gap/limit: No operation independently observed.

Route ID: [RT-RTE-span-gate](runtime.md#rt-rte-span-gate)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-gate-result](#epi-obj-gate-result)
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Offset validity, optional chunk containment, optional within-slice quote occurrence
Evaluator/condition and domain: Bounds and content predicates on caller-supplied current strings
Activation and timing: Direct span/resolve operations
Possible or observed result: see [RT-RTE-span-gate](runtime.md#rt-rte-span-gate)
Implemented force: Return/rejection, not answer veto
Epistemic authority and scope: Valid slice or match within slice only
Operational authority: see [RT-RTE-span-gate](runtime.md#rt-rte-span-gate)
Behavioral-authority path: Caller through API return; informational until consumed; one call
Evidence source ID and local anchor: SRC-1, `src/verbatim_citation_gate/gate.py`
Claim IDs: none
Mismatch marker: No-quote branch accepts interior word/number slices.
Gap/limit: No operation independently observed.

Route ID: [RT-RTE-judge-support](runtime.md#rt-rte-judge-support)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-verdict](#epi-obj-verdict) and [EPI-OBJ-reasoning](#epi-obj-reasoning)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Whether quote in full source context establishes supplied claim at requested strength
Evaluator/condition and domain: Caller-selected model under default-refute prompt; source-relative evidential relationship, not real-world truth
Activation and timing: Direct invocation or dispatcher found branch
Possible or observed result: see [RT-RTE-judge-support](runtime.md#rt-rte-judge-support)
Implemented force: Natural-language policy delivered; no semantic code enforcement
Epistemic authority and scope: If compliant, evidence-relative support assessment. Actual soundness and entailment unknown
Operational authority: Proposes a verdict for parser admission
Behavioral-authority path: Callback via system/user strings; requested policy; one judgment
Evidence source ID and local anchor: SRC-1, `src/verbatim_citation_gate/judge.py`
Claim IDs: [EPI-CLM-citation-support](#epi-clm-citation-support)
Mismatch marker: Constant supports callback is permitted and defeats reliable semantic-check inference.
Gap/limit: Implementation requests evaluation; neither universally entailed derivation nor non-entailed conjecture is established for arbitrary model output.

Route ID: [EPI-RTE-verdict-admission](#epi-rte-verdict-admission)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-verdict](#epi-obj-verdict)
Content/update relation: no content change
Transition or check target: Whether a callback label can be returned as a recognized verdict
Evaluator/condition and domain: First parseable JSON object, four labels; not semantic validation
Activation and timing: After callback; direct or dispatched
Possible or observed result: see [EPI-RTE-verdict-admission](#epi-rte-verdict-admission)
Implemented force: Deterministic schema-fragment admission/default refutation
Epistemic authority and scope: Acceptance of output vocabulary, not evidence-consuming acceptance of the underlying claim
Operational authority: Returns allowed verdict; dispatch returns only label, dropping explanation and confidence
Behavioral-authority path: Parser to judge_support to audit caller via Verdict/string; enforcing representation gate; current call
Evidence source ID and local anchor: SRC-1, `src/verbatim_citation_gate/judge.py`
Claim IDs: [RT-CLM-closed-judge](runtime.md#rt-clm-closed-judge)
Mismatch marker: Valid supports without reasoning/confidence passes.
Gap/limit: No operation independently observed.

Route ID: [EPI-RTE-example-display](#epi-rte-example-display)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-verdict](#epi-obj-verdict)
Content/update relation: no content change
Transition or check target: Display of audit result
Evaluator/condition and domain: Loop prints every item; no supports-only delivery filter
Activation and timing: After each example audit
Possible or observed result: see [EPI-RTE-example-display](#epi-rte-example-display)
Implemented force: Display only
Epistemic authority and scope: No added warrant
Operational authority: No answer suppression implemented
Behavioral-authority path: Example loop through stdout; informational; script invocation
Evidence source ID and local anchor: SRC-1, `examples/demo.py`, `examples/quickstart.py`
Claim IDs: [EPI-CLM-citation-support](#epi-clm-citation-support)
Mismatch marker: none
Gap/limit: No operation independently observed.

Route ID: [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: Constructed expected labels and returned gate labels
Content/update relation: truth-apt transformation: entailed derivation
Transition or check target: Agreement with generated expected labels on retained constructed case set
Evaluator/condition and domain: Exact comparison after suite construction/filtering; gate only
Activation and timing: Benchmark invocation, not production audit
Possible or observed result: see [EPI-RTE-benchmark-check](#epi-rte-benchmark-check)
Implemented force: Printed/optional JSON report; no product update branch
Epistemic authority and scope: Suite agreement and arithmetic rates, conditional on labels and corpus; not population recall
Operational authority: Reports results only
Behavioral-authority path: Benchmark driver via counters to stdout; informational; one evaluation
Evidence source ID and local anchor: SRC-1, `bench/bench_gate.py`, `bench/hard_cases.py`
Claim IDs: [EPI-CLM-benchmark-detection](#epi-clm-benchmark-detection)
Mismatch marker: Negative filter shares normalize with evaluated implementation.
Gap/limit: Source defines calculation; saved result lacks generating trace. Human prose reports improvement but no controlled component intervention is supplied.

Retention is not lifecycle integration. The normalization cache in [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation) retains derived strings for speed, not accepted claims; [EPI-RTE-benchmark-check](#epi-rte-benchmark-check) describes corpus retention separately from measurement. Across the directly inspected production modules there is no result write, retained semantic verdict, withdrawal registry or downstream acceptance lifecycle. This is a bounded architectural finding, not a system-wide negative about provider state or excluded hosts. Callback failures yield a current-call label, not revocation of past answers. Product admission remains the separate human/release route [RT-RTE-release-admission](runtime.md#rt-rte-release-admission).

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Source/anchor and evidence layer | Doctrine/design support | Implemented routes | Observed-run support | Causal support/design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-citation-support](#epi-clm-citation-support) | see record | SRC-1, `README.md`, `src/verbatim_citation_gate/__init__.py`; doctrine/design | Default-refute/full-strength rules in [RT-OBJ-judge-system](runtime.md#rt-obj-judge-system) | [EPI-RTE-quote-check](#epi-rte-quote-check), [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation), [RT-RTE-judge-support](runtime.md#rt-rte-judge-support), [EPI-RTE-verdict-admission](#epi-rte-verdict-admission) | None supplied for live-model accuracy or user protection | No judge ablation/comparison; offline stand-ins cannot establish semantic benefit | Non-found deterministically avoids callback on dispatch; full-strength support is requested policy | Normalized occurrence not truth; no downstream answer veto; permitted constant callback can ignore rules |
| [RT-CLM-closed-judge](runtime.md#rt-clm-closed-judge) | see record | SRC-1, `src/verbatim_citation_gate/judge.py`; doctrine/design and implementation | Exception/unparseable/unknown-label rejection | [EPI-RTE-verdict-admission](#epi-rte-verdict-admission), [RT-RTE-judge-support](runtime.md#rt-rte-judge-support) | None supplied | No semantic oracle and incomplete field validation | Narrow fail-closed parse handling | Missing reasoning/confidence need not refute; arbitrary non-string return is outside text contract |
| [EPI-CLM-benchmark-detection](#epi-clm-benchmark-detection) | see record | SRC-1, `bench/README.md`, `bench/results.json`; doctrine/design, reported operation | Explicit stage-two and class-balance exclusions | [EPI-RTE-benchmark-check](#epi-rte-benchmark-check) | Saved aggregate candidate result, no generating trace | Filtered constructed cases, shared normalization, short abstracts, no independent model comparator | Reported suite detection and false-positive tradeoff only | No universal no-fabrication-loss guarantee or demonstrated production recall lift |

## Bounded conclusion

The deterministic routes establish predicates about supplied text and offsets, not source truth. [EPI-RTE-quote-check](#epi-rte-quote-check) derives a normalized-occurrence classification and [RT-RTE-span-gate](runtime.md#rt-rte-span-gate) derives validity of a caller-selected slice. These are entailed implementation-domain results conditional on supplied input strings and the encoded matching rules. A concrete nonexecuted deduction: document `risk > 5%` and quote `risk < 5%` retain distinct operator tokens, so the quote is not found. Conversely, document `25-30 mg` and quote `25 30 mg` both normalize to `25 30 mg`: the internal hyphen follows a digit so it becomes a space, and the match spans the whole string. A found result therefore cannot warrant literal identity or preserved meaning. The same implementation blocks cutting `28` from `28.5`, but that positive boundary protection does not repair all semantic distinctions. See [EPI-RTE-quote-check](#epi-rte-quote-check) and SRC-1, `src/verbatim_citation_gate/gate.py`.

The support route acquires caller claims and source content with unknown source warrant, then requests an evidence-relative judgment. The full original source survives into the callback; normalization is not used to rewrite the model's evidence. The prompt names a substantive criterion and intended use: judge this citation's full-strength support, including population, outcome, direction and certainty, excluding outside knowledge. That is an implemented request for evidence consumption, not demonstrated evidence-consuming acceptance by an actual model. The parser only accepts label vocabulary. Returning `{"verdict":"supports"}` is enough to pass its check; confidence is not a threshold. No accepted ampliative knowledge claim, calibrated confidence or semantic-check reliability follows ([RT-RTE-judge-support](runtime.md#rt-rte-judge-support), [EPI-RTE-verdict-admission](#epi-rte-verdict-admission)). This leaves model-output entailment indeterminate rather than automatically classifying all judgment as conjecture.

Operationally, the dispatcher enforces a pre-model veto but cannot govern callers of the direct judge or downstream user delivery. Its offline result `found` must remain separate from `supports`. The example consumers print results rather than accepting, integrating or withholding answers ([RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation), [EPI-RTE-example-display](#epi-rte-example-display)). No semantic-result persistence or evidence-triggered policy adaptation is present in the inspected production modules; the cache is computational reuse. No exercised learning or improvement is established. Human product maintenance and opaque provider changes remain independent questions, not negatives inferred from that cache finding.

The benchmark evaluates a different target: equality to constructed expected labels. Its documented error tradeoff is relevant to operational use, but its retained rates are neither an authenticated execution trace nor causal evidence for a component improvement. The builder imports, unwraps and persists external abstracts; source truth and acquisition history are not validated. Suite filtering and limited distribution prevent transfer of a reported perfect detection rate to all fabrications, live models or production users ([EPI-RTE-benchmark-check](#epi-rte-benchmark-check), [EPI-CLM-benchmark-detection](#epi-clm-benchmark-detection)). Nothing here gives the mechanism a single epistemic grade.

## Shared records

### Operative objects

#### EPI-OBJ-docs
Label: Supplied citation and document text

Identity: `docs`, `claim`, `quote` and `source` values supplied to library APIs; natural-language strings in caller-owned dictionaries/current-call memory. Document keys and bounds are symbolic selectors, not provenance certificates. Closest supplied records are [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation) and [RT-RTE-judge-support](runtime.md#rt-rte-judge-support), which describe processes, not these input objects. No object counterpart was supplied. The library acquires rather than authors the assertions; normalization provides no endorsement. SRC-1, `src/verbatim_citation_gate/judge.py`; delivery passage in [RT-RTE-judge-support](runtime.md#rt-rte-judge-support).

#### EPI-OBJ-gate-result
Label: GateResult occurrence classification

Identity: `GateResult`, symbolic string labels in current-call Python memory, consumed by dispatch or returned to caller. The closest supplied records [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation) and [RT-RTE-span-gate](runtime.md#rt-rte-span-gate) are producing/consuming routes, not this result object. Both paths can return found, with different predicates; no semantic-support license is implicit. SRC-1, `src/verbatim_citation_gate/gate.py`.

> GateResult = str  # Literal["found", "misattributed", "not_found"]
> --- `src/verbatim_citation_gate/gate.py`

#### EPI-OBJ-verdict
Label: Verdict label and confidence

Identity: symbolic `Verdict.verdict` and numeric `Verdict.confidence` fields in a current-call dataclass. Confidence is a scalar self-report, not distributed-parametric state. Parser and dispatcher consume these fields under fixed rules; dispatch exports only the label. Distinct from the explanation part [EPI-OBJ-reasoning](#epi-obj-reasoning), whose meaning needs interpretation. Closest supplied [RT-RTE-judge-support](runtime.md#rt-rte-judge-support) is the producing route, not a declared result object. Evidence: SRC-1, `src/verbatim_citation_gate/judge.py`; parser and dispatch passages retained in [RT-RTE-judge-support](runtime.md#rt-rte-judge-support) and [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation).

#### EPI-OBJ-reasoning
Label: Verdict reasoning

Identity: natural-language `Verdict.reasoning` string in current-call dataclass memory; available to direct API callers, neither inspected for validity by parser nor delivered by combined dispatcher. Distinct from [EPI-OBJ-verdict](#epi-obj-verdict) by form and consumer. No supplied object counterpart after comparison with [RT-OBJ-judge-system](runtime.md#rt-obj-judge-system), which is the static input instruction rather than returned explanation. Evidence: SRC-1, `src/verbatim_citation_gate/judge.py`; parser's default and constructor retained in [RT-RTE-judge-support](runtime.md#rt-rte-judge-support).

### Routes

#### EPI-RTE-quote-check
Label: Normalize and classify quote occurrence

Part of: [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation)

This declares the material deterministic check inside the combined route, also callable directly as quote_gate/normalize. The parent route owns callback selection, not this check's occurrence warrant. Python owns progression from quote/docs through normalization and boundary checks to GateResult. It changes only working strings/cache, not the source. No human approval or semantic answer oracle is involved: the reference is the supplied document string, interpreted under the encoded predicate. Mode is a caller's open request; no improvement trigger. SRC-1, `src/verbatim_citation_gate/gate.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: normalized text for normalize; found for attributed occurrence, misattributed for another-document occurrence, otherwise not_found for quote_gate.
- Later read-back: bounded normalization memoization of raw strings to derived strings; no retained citation decision or knowledge admission.
- Delegated visibility: inapplicable — deterministic stage invokes no model.
- Selection predicate: nonempty content and a contiguous match whose two normalized boundaries are accepted; cited document first, others only on failure.
- Invalidation or expiry: up to 4096 raw-input cache keys; new text has a different key, no document-version identity is tracked.
- Activation or effect: dispatcher consumes the result to permit/block a callback; direct callers receive only classification.
- Evidence limits: static implementation deduction, no execution. Normalization changes equality and does not prove semantic preservation or source truth.

> text = text.translate(_HOMOGLYPHS)
> text = _SPACE_BEFORE_PERCENT.sub("%", text)
> return " ".join(_keep_quantitative(text).split())
> --- `src/verbatim_citation_gate/gate.py`

> elif (
>     char in _SIGNS
>     and i < last
>     and text[i + 1].isdigit()
>     and (i == 0 or not _is_word_char(text[i - 1]))
> ):
>     out.append("-" if char in "-−" else "+")
> elif char in _OPERATORS:
>     out.append(" " + char + " ")
> else:
>     out.append(" ")
> --- `src/verbatim_citation_gate/gate.py`

> start = haystack.find(needle)
> while start != -1:
>     if _is_boundary(haystack, start) and _is_boundary(haystack, start + len(needle)):
>         return True
>     start = haystack.find(needle, start + 1)
> return False
> --- `src/verbatim_citation_gate/gate.py`

The normalized-proposition derivation follows the inspected predicate, not a new empirical observation. The numeric-boundary and content checks qualify a naive substring account; the hyphen example in the conclusion qualifies the stronger semantic-preservation reading.

#### EPI-RTE-verdict-admission
Label: Parse and admit verdict vocabulary

Part of: [RT-RTE-judge-support](runtime.md#rt-rte-judge-support)

Material disposition stage of the parent support-check route. Python consumes callback text, selects the first parseable object, checks label membership and returns a Verdict. Callback/model proposes; parser decides representational admission and can veto invalid labels; no human approval or independent semantic oracle. It does not test the proposed reasoning against the source. Its criterion and use are vocabulary-safe return in one open judgment request, not epistemic acceptance of a world claim. No product revision, rollback or retained-policy change is admitted. SRC-1, `src/verbatim_citation_gate/judge.py`; load-bearing defaulting/vocabulary passage is supplied by [RT-RTE-judge-support](runtime.md#rt-rte-judge-support).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: parsed Verdict or unrelated/zero-confidence for recognized failure cases.
- Later read-back: inapplicable — no result store or later invocation consumes an accumulated verdict.
- Delegated visibility: inapplicable — parser invokes no second evaluator; direct caller gets structured fields, audit caller only the label.
- Selection predicate: first parseable JSON dictionary; label in supports/partial/unrelated/contradicts; missing reasoning and confidence default rather than reject.
- Invalidation or expiry: inapplicable — no accepted-claim registry to revoke; this is current-call disposition.
- Activation or effect: controls returned label, without semantic evidence checking or confidence threshold.
- Evidence limits: string-returning contract; parse exceptions for arbitrary non-string objects are not promised safe. Valid JSON can still express false support.

> if isinstance(obj, dict):
>     return obj
> pos = text.find("{", pos + 1)
> --- `src/verbatim_citation_gate/judge.py`

A concrete source deduction challenges the blanket fail-closed claim: text `{"verdict":"supports"}` is a parseable dictionary, its label is in _VALID, missing confidence becomes 0.0, and missing reasoning becomes empty; the label remains supports. This shows operational acceptance without any explanatory evidence. It does not establish how often real models emit that case.

#### EPI-RTE-example-display
Label: Display audit labels from offline examples

No supplied record counterpart: [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation) describes the called library route, while this route is its downstream example consumer. Script main loops own progression from fixed citation tuples through audit to print. Constant callbacks ignore evidential inputs and return supports; the demo also increments a call counter. No per-content human veto, real semantic oracle or admission criterion is wired. No package change or answer-release policy is updated. SRC-1, `examples/demo.py`, `examples/quickstart.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: stdout labels and claims; demo also prints quote fragments and call counts.
- Later read-back: inapplicable — examples do not persist decisions for later invocation.
- Delegated visibility: callback receives audit strings but returns its fixed stand-in verdict.
- Selection predicate: all fixed CITATIONS are iterated and printed, not only supports.
- Invalidation or expiry: inapplicable — no acceptance store or retained output lifecycle.
- Activation or effect: implements demonstration display and callback counting, not evidence-sensitive semantic acceptance.
- Evidence limits: scripts not run; constant callbacks cannot demonstrate model judgment or end-to-end user protection.

> def _demo_llm(system: str, user: str) -> str:
>     # Offline stand-in: pretend the model judged the one real, on-point quote as supporting.
>     return '{"reasoning": "demo", "verdict": "supports", "confidence": 0.8}'
> --- `examples/quickstart.py`

> if __name__ == "__main__":
>     for claim, doc_id, quote in CITATIONS:
>         verdict = audit_citation(claim, doc_id, quote, DOCS, llm_call=_demo_llm)
>         print(f"{verdict:>14}  |  {claim}")
> --- `examples/quickstart.py`

#### EPI-RTE-benchmark-check
Label: Construct and measure deterministic gate cases

No supplied route counterpart: [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation) is a product request route; runtime prose describes evaluation but does not declare its benchmark route. Shipped Python builder imports abstracts from a latest-submission feed, unwraps whitespace, filters short entries and writes a doc-ID/text JSON file. This is acquisition with unknown original source warrant; whitespace flattening loses original formatting. The measured driver reloads that corpus, constructs positives and negatives, filters accidental normalized occurrences, evaluates quote_gate, compares exact labels and prints rates or JSON. Fixed corpus/order determines cases, not the date-varying external feed.

Python owns case selection, expectation construction and arithmetic. The expected-answer oracle is the transformation's assigned label (plus source/other-document selection), not independent human annotation or a model. Positive hard cases include ellipsis and bracket insertions; near misses include changed numbers, added negation, removed hedge and synonym substitution. They are test stimuli, not admitted new knowledge. Proposal/admission here concerns test-case population: code proposes cases and can drop expected-not_found cases; no human case-by-case veto appears. Operating mode is a bounded constructed benchmark, not an adaptive production curriculum. There is no automatic product-update consumer or rollback operation. SRC-1, `bench/build_corpus.py`, `bench/bench_gate.py`, `bench/hard_cases.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: builder writes corpus JSON; driver prints per-mode and aggregate report, optionally JSON. Saved results exist but their generating execution is not traced.
- Later read-back: builder's corpus file is loaded by benchmark invocations; no route reads benchmark outcomes to change product policy.
- Delegated visibility: external arXiv request sends fixed categories and query settings; model delegation is inapplicable because only deterministic gate is evaluated.
- Selection predicate: suitable first sentences, stride-selected other documents, applicable transformations; expected-not_found cases with any normalized substring occurrence are dropped before measurement.
- Invalidation or expiry: builder overwrites corpus; result summary contains no frozen code/corpus digest or automatic invalidation.
- Activation or effect: calculates and reports agreement/error rates; no downstream product acceptance threshold is wired.
- Evidence limits: corpus contents not inspected; no target execution, production sampling, model comparison, controlled ablation or authenticated generating trace. Normalization is shared between filtering and tested implementation.

> text = " ".join(summary.split())
> doc_id = raw_id.rsplit("/", 1)[-1]
> if doc_id and len(text) > 400:
>     out.append((doc_id, text))
> --- `bench/build_corpus.py`

> if c["expect"] == "not_found":
>     needle = normalize(c["quote"])
>     if any(needle in h for h in haystacks.values()):
>         dropped += 1
>         continue
> --- `bench/bench_gate.py`

> got = quote_gate(c["quote"], c["doc"], docs)
> slot = per_mode.setdefault(c["mode"], {"n": 0, "ok": 0})
> slot["n"] += 1
> if got == c["expect"]:
>     slot["ok"] += 1
> --- `bench/bench_gate.py`

The filter uses substring occurrence without the production boundary test. It conditions the tested negatives on the same normalizer, so the measured target is surviving cases, not arbitrary false quotations. Saved `bench/results.json` agrees with README headline totals (4592 cases, 1221 bad, 3371 honest, detection 1.0 and false-positive rate 0.1721); existence of that artifact alone does not prove the generating route ran at this revision.

### Claims

#### EPI-CLM-citation-support
Label: Prevent fabricated citations and require full-strength support

Distinct from [RT-CLM-closed-judge](runtime.md#rt-clm-closed-judge), which concerns parser failure policy. This public claim concerns citation protection and evidential sufficiency. SRC-1, `README.md`, `src/verbatim_citation_gate/__init__.py`; doctrine/design, not observed operation.

> **Catch fabricated RAG citations before they reach the user.** A two-stage, framework-agnostic auditor for quote-style citations.
> --- `README.md`

> * **Stage 2 — the skeptical judge** (:func:`judge_support`): a burden-of-proof
>   prompt, wired to *any* model via an ``llm_call`` callable, that only lets a
>   real quote count as ``supports`` when it establishes the claim at full
>   strength.
> --- `src/verbatim_citation_gate/__init__.py`

Prompt criterion, SRC-1, `src/verbatim_citation_gate/judge.py`:

> 1. Judge only the relationship between the quote (read in the context of its source) and the claim. Your own
>    knowledge of the topic is inadmissible: a claim may be true in the real world and still unsupported by this
>    source, and a claim may be dubious yet fully supported by it.
> --- `src/verbatim_citation_gate/judge.py`

> 2. "supports" requires the quote to establish the claim at full strength: same population, same outcome, same
>    direction, and certainty no stronger than the source's own language. If the claim upgrades any of these
>    (correlation to causation, a subgroup to everyone, "may" to "does", hedged to absolute), the verdict is at
>    most "partial".
> --- `src/verbatim_citation_gate/judge.py`

Counterevidence is the permitted constant callback and parser pathway in [EPI-RTE-example-display](#epi-rte-example-display) and [EPI-RTE-verdict-admission](#epi-rte-verdict-admission). The dispatcher does not itself own user delivery, so protection is conditional on external use. README's claim that a judge waves fabrications through and that recall is lifted has no inspected live-model comparison.

#### EPI-CLM-benchmark-detection
Label: Measured detection and normalization improvement

No supplied claim counterpart: [RT-CLM-closed-judge](runtime.md#rt-clm-closed-judge) concerns stage two parsing, whereas this is stage-one evaluation/generalization. SRC-1, `bench/README.md`, `bench/results.json`. These supply author-reported measurements and a saved result artifact, not a reproduced run or identified causal experiment.

> The false-positive rate was **0.4254** when this benchmark was first run. Three
> of the five failing modes were normalization gaps — soft hyphens, line-break
> hyphenation and homoglyphs are the same characters encoded differently — and
> fixing them took the rate to 0.1721 (−25.3 points) **without moving detection**,
> which stayed at 1.0000 on all 1 221 bad citations.
> --- `bench/README.md`

> Anyone dropping this in front of users today should know: it will not lose a
> fabrication, and it will still argue with roughly one in six real quotes —
> specifically, quotes an author shortened with an ellipsis or annotated in
> brackets.
> --- `bench/README.md`

> * **Stage 2, the judge.** These numbers cover the deterministic gate only.
> * **Real-world class balance.** The mix here is constructed, not sampled from
>   production traffic, so the headline rates are per-suite, not per-user. Read
>   the per-mode table, not the average, to predict behaviour on your own inputs.
> --- `bench/README.md`

The scope qualification is substantive counterevidence to an unqualified reading of the preceding no-fabrication-loss claim. The report preserves the narrower measurement claim, without inferring universal recall or a causal component effect. A comparison described in prose without a frozen pre-change run/design cannot identify individual normalization effects.

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
