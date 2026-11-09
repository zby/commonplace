---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Workflow account of verbatim-citation-gate: shipped batch demonstration from supplied citations through rejection or callback judgment to printed verdicts."
run-id: AAS-2026-11-08-verbatim-citation-gate-d205c9f72d5a-01
reviewed-boundary: "2113d603031a554ed901a44648307bd3b711ea10"
---

# verbatim-citation-gate workflow report

## Workflow account

The representative workflow is the batch audit in `examples/demo.py`: supplied citations pass through deterministic attribution checking, optionally through a judgment callback, and then into printed results. It was selected because it connects the two-stage library to a shipped caller and includes both nonexistent quotations and a real quotation attributed to the wrong document. This is a multi-step tool workflow, not a demonstrated autonomous agent workflow. Its callback is an offline stand-in, not a live model. The account establishes implementation wiring in SRC-1 at the frozen revision, not successful execution, semantic accuracy or downstream enforcement. The surrounding application's retrieval, citation generation and user-answer acceptance remain outside the [boundary](boundary.md).

### Request and handoff ownership

The demo supplies two fixed documents and four citation tuples containing claim, document key, quote and explanatory note. A human or enclosing application does not generate fresh citations inside this path. The script owns batch ordering, calls the auditor synchronously and prints the result; the auditor owns checking and conditional delegation. [WF-RTE-demo-batch](#wf-rte-demo-batch) describes this caller-level route, while [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation) supplies the internal dispatch evidence (SRC-1, `examples/demo.py`, `src/verbatim_citation_gate/judge.py`).

The handoff into the library supplies the original claim, quote, document identity, whole document dictionary and callback. Neither the demo's explanatory note nor its call counter becomes judgment context. The deterministic gate searches the cited document first; a match there proceeds even if another document also contains the quote. Only after that fails does another-document occurrence produce `misattributed`. No matching supplied document produces `not_found`. The predicate is normalized contiguous occurrence with word/number boundaries, not literal byte identity and not a semantic support test (SRC-1, `src/verbatim_citation_gate/gate.py`; [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation)).

### Verification and conditional judgment

The fabricated weight-loss quote and the assembled low-risk-subgroup quote in the demo reach deterministic rejection, while the heart-attack quote attributed to the veltranib document matches the other supplied document. Those are source-traced branch expectations, not observed results. The decisive veto is library code: any result other than `found` immediately returns without invoking the callback. The successful existence check instead delegates to [RT-RTE-judge-support](runtime.md#rt-rte-judge-support). Without a supplied callback, the same dispatcher would return `found`, which must not be confused with semantic `supports` (SRC-1, `examples/demo.py`, `src/verbatim_citation_gate/judge.py`).

On delegation, the callback gets the fixed skeptical system instruction plus the original claim, original quote and full original cited document. It does not receive the normalized match, other documents, batch history, note or counter. The requested judgment evaluates whether this source supports the claim at its stated strength; the instruction is policy, not an enforced semantic oracle. Callback/model judgment proposes the label, and the parser controls acceptance into the four-label vocabulary. No human per-item approval or independent expected answer is wired into this demonstration (SRC-1, `src/verbatim_citation_gate/judge.py`; [RT-OBJ-judge-system](runtime.md#rt-obj-judge-system), [RT-BAP-judge-instruction](runtime.md#rt-bap-judge-instruction)).

The demo callback ignores both input strings and always returns a `supports` object. Its incremented counter witnesses the intended callback boundary in code, not model reasoning quality. Thus the final real quotation demonstrates wiring to a stand-in, not evidence that the skeptical policy works. There is no worker scheduling, separate agent context or model-led next-step choice in the inspected demo loop (SRC-1, `examples/demo.py`):

> def llm_call(system: str, user: str) -> str:
>     """Stand-in for your model. Counts calls so the demo cannot overstate itself."""
>     global CALLS
>     CALLS += 1
>     return '{"reasoning": "the quote states it directly", "verdict": "supports", "confidence": 0.9}'
> --- `examples/demo.py`

### Rejection, recovery and delivery

Deterministic rejection terminates only that citation's audit; the demo prints its result and moves to the next tuple. It neither corrects the citation nor resubmits it. On the model-enabled path, caught callback exceptions, unparseable text and invalid verdict labels become `unrelated`; there is no retry into a more favorable answer. Recovery is therefore a conservative return, not repair. Parser acceptance does not establish sound reasoning: valid labels can survive missing reasoning/confidence, and non-string callback outputs violate the callback contract and can escape the callback exception handler. These qualifications follow [RT-RTE-judge-support](runtime.md#rt-rte-judge-support) and [RT-CLM-closed-judge](runtime.md#rt-clm-closed-judge) (SRC-1, `src/verbatim_citation_gate/judge.py`).

The combined auditor discards reasoning and confidence and returns only the verdict string. The demo delivers by printing claim, shortened quote, verdict, explanatory note and call-count-derived cost label, then a batch summary. It does not remove rejected citations from a generated answer or persist a repaired artifact. Its `0 tokens` text means no demo callback invocation for that item; this is not provider usage accounting. Any correction, changed acceptance rule or actual user-answer suppression belongs to a caller beyond this example (SRC-1, `examples/demo.py`, `src/verbatim_citation_gate/judge.py`).

Inspection for this account covered the complete `examples/demo.py`, `examples/quickstart.py` and `src/verbatim_citation_gate/judge.py`, plus `_contains` and `quote_gate` in `src/verbatim_citation_gate/gate.py`. These supply implementation evidence within SRC-1, extending the initial example inspection into a caller-level workflow trace. No source ID, functional boundary or revision was added. No target code was executed; actual callback counts, delivery and live-model behavior remain unobserved.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

#### WF-RTE-demo-batch
Label: Demo batch audit and printed delivery

Source-native identity: the main loop in `examples/demo.py`. Endpoints are static `CITATIONS`/`DOCS` and stdout. Python serial iteration owns progression; each item calls the auditor, receives its verdict and prints before proceeding. This route is distinct from [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation): it is the shipped caller wrapping repeated auditor invocations with instrumentation and presentation, not a second declaration of internal audit dispatch. The loop's note is for presentation, not an answer oracle used to select the verdict. There is no human per-item veto, improvement trigger or product-change admission in this fixed demonstration (SRC-1, `examples/demo.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: printed per-citation fields followed by batch totals; the nested auditor returns a verdict string.
- Later read-back: inapplicable — this caller writes no retained result for a later invocation.
- Delegated visibility: each nested audit receives claim, document ID, quote, DOCS and callback; only a successful deterministic match exposes claim, quote and cited source to the callback. Notes and counts stay local.
- Selection predicate: all four static citation tuples in list order; conditional callback dispatch belongs to the cited runtime route.
- Invalidation or expiry: inapplicable — fixed inputs and process-local instrumentation have no persisted result lifecycle.
- Activation or effect: prints classification and a cost label derived from counter change; does not enforce answer admission or revise citations.
- Evidence limits: offline constant callback; no observed execution, provider-token measurement or demonstrated semantic verification.

> if __name__ == "__main__":
>     for claim, doc_id, quote, note in CITATIONS:
>         before = CALLS
>         verdict = audit_citation(claim, doc_id, quote, DOCS, llm_call=llm_call)
>         cost = "1 model call" if CALLS > before else "0 tokens"
> --- `examples/demo.py`

> print(f"  -> {verdict:<14} {note}  ({cost})")
> --- `examples/demo.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation)

Workflow role: per-item verification handoff inside the demo batch. Deterministic veto terminates that item without correction; a model-enabled `found` proceeds to callback judgment. Completion returns a label to the caller, not an accepted user-facing answer. The demo continues to the next item rather than using the failure to revise its proposal.

#### On [RT-RTE-judge-support](runtime.md#rt-rte-judge-support)

Workflow role: conditional single-callback judgment with conservative error return, not a delegated agent tasked with repairing evidence. The enclosing dispatcher exposes only its verdict, so the demo's delivered output cannot explain the judgment using this route's reasoning or confidence fields.
