---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent report verification of verbatim-citation-gate's citation auditor, shipped consumers and evaluation at the frozen subsystem boundary."
run-id: AAS-2026-11-08-verbatim-citation-gate-d205c9f72d5a-01
reviewed-boundary: "2113d603031a554ed901a44648307bd3b711ea10"
---

# verbatim-citation-gate report verification

## Verification

The runtime, memory, epistemic, workflow and reconciliation members support a bounded implementation account. No material blocker was found. The supplied structural report says `none`; all four correction-answer files are empty, so there are no correction arguments to accept or reject. I independently read the implementation rather than treating the analysts' validation statements or test assertions as verification. No target program, example, test or provider was executed.

The checkout HEAD equals the [boundary](boundary.md)'s reviewed revision, and its working tree is clean. Inspection used SRC-1: all package modules, both example scripts, packaging metadata, corpus builder, benchmark driver and transformations, benchmark README and saved results, the complete test file, governance and both CI workflows. Additional omission inspection used the frozen tracked tree, searches in `docs/index.html` and `docs/make_demo_gif.py`, a full read of the image generator and the API/limits portion of the HTML. These reads supply implementation or doctrine/design evidence, not an authenticated execution or causal experiment. No new source identity or functional boundary was introduced.

### Runtime and alternate paths

I traced [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation), [RT-RTE-judge-support](runtime.md#rt-rte-judge-support) and [RT-RTE-span-gate](runtime.md#rt-rte-span-gate) through their actual branches in SRC-1, `src/verbatim_citation_gate/gate.py`, `src/verbatim_citation_gate/judge.py` and the exports in `src/verbatim_citation_gate/__init__.py`. The dispatcher veto is supported only for a non-`found` gate result on that entry point. Direct judgment bypasses the occurrence check, direct deterministic APIs bypass semantic judgment, and the no-callback dispatcher returns `found`, not `supports`. The reports preserve all three qualifications.

The span route's chunk control is optional and confined to that route. Its no-quote branch accepts a contentful valid slice without full-document boundary checking; the quote branch checks within the slice. Both branches are reachable with documented string and integer inputs. Thus these are supported alternate predicates, not a conjectured bypass based on invalid types. Normalization, content filtering and word/number boundaries support the encoded occurrence predicate, not literal identity or semantic preservation. The operator and range examples in [EPI-RTE-quote-check](epistemic.md#epi-rte-quote-check) follow the inspected normalization order and quantitative rules.

The callback receives the original whole cited source with the claim and quote. Neither cache output nor a selected evidence summary replaces it. [RT-CMP-llm-call](runtime.md#rt-cmp-llm-call), [RT-OBJ-judge-system](runtime.md#rt-obj-judge-system) and [RT-BAP-judge-instruction](runtime.md#rt-bap-judge-instruction) correctly separate the unpinned external model boundary, delivered instruction and requested force. They do not establish model compliance, provider retention, timeout control or semantic reliability.

The parser admits a recognized `supports` label with missing reasoning and confidence. It scans for the first parseable object, defaults fields and applies no confidence threshold. This is reachable under the text-returning callback contract. It supports the mismatch in [RT-CLM-closed-judge](runtime.md#rt-clm-closed-judge) and the separate representation-disposition account in [EPI-RTE-verdict-admission](epistemic.md#epi-rte-verdict-admission). The reports also correctly distinguish caught callback exceptions from non-string failures during subsequent parsing; they do not turn an out-of-contract input into a demonstrated supported-input failure.

[RT-RTE-release-admission](runtime.md#rt-rte-release-admission) agrees with SRC-1, `GOVERNANCE.md`, `.github/workflows/tests.yml` and `.github/workflows/publish.yml`: human authority is declared policy, publication depends on its build and readiness condition, and the separate test workflow is not a publication dependency. Deployed protections and actual release execution remain unestablished.

### Memory, epistemic authority and delivery

[MEM-OBJ-normalized](memory.md#mem-obj-normalized) and [MEM-RTE-normalization-reuse](memory.md#mem-rte-normalization-reuse) correctly identify exact raw-string keys, derived symbolic values, a 4096-entry process-local bound and later deterministic consumers. Changed text selects another key. No semantic judgment is retained by this cache. [MEM-OBJ-corpus](memory.md#mem-obj-corpus) and [MEM-RTE-corpus-reload](memory.md#mem-rte-corpus-reload) distinguish external acquisition, software filtering, whole-file replacement and subsequent requested loading. Script invocation does not establish per-content human approval. [MEM-OBJ-results](memory.md#mem-obj-results) correctly separates retained aggregate data and truncated failure display from a complete execution trace or behavior-shaping update. The write-side and read-back conclusions are supported within their stated scope.

The operative distinctions in [EPI-OBJ-docs](epistemic.md#epi-obj-docs), [EPI-OBJ-gate-result](epistemic.md#epi-obj-gate-result), [EPI-OBJ-verdict](epistemic.md#epi-obj-verdict) and [EPI-OBJ-reasoning](epistemic.md#epi-obj-reasoning) match their consumers. Input assertions have unknown source warrant; occurrence labels assert an implementation-domain result; support labels and confidence receive fixed parser treatment; explanation content is not checked and is discarded by the dispatcher. No evidence-consuming acceptance of an underlying world claim or lifecycle integration is inferred from returning a vocabulary-valid label. The epistemic ledger's indeterminate normalization and model-output relations are appropriately distinct from its entailed algorithmic predicate and arithmetic findings.

I traced case generation, accidental-truth filtering, comparison and report construction for [EPI-RTE-benchmark-check](epistemic.md#epi-rte-benchmark-check). Filtering shares the normalizer and uses substring occurrence without the production boundary predicate. Saved totals agree with the reported figures, but neither those figures nor source-defined calculations authenticate a generating execution at this revision. [EPI-CLM-benchmark-detection](epistemic.md#epi-clm-benchmark-detection) preserves the stage-one, constructed-distribution and causal-attribution restrictions. [EPI-CLM-citation-support](epistemic.md#epi-clm-citation-support) is likewise compared with actual dispatcher and callback authority rather than accepted as guaranteed user protection.

Both shipped example loops print results from constant stand-ins. [WF-RTE-demo-batch](workflow.md#wf-rte-demo-batch) correctly traces the four-item batch, conditional handoff, per-item termination, continuation and stdout delivery. [EPI-RTE-example-display](epistemic.md#epi-rte-example-display) covers both callers' display rather than enforced answer admission. Notes and counters do not become judge context; counter-derived cost text is not provider usage measurement. Failure returns do not constitute citation repair. These conclusions preserve the distinction between implemented wiring and observed successful operation.

### Relations, omission search and stopping decision

I checked every declared record's referent, supporting anchor, evidence strength and consumer against the account above, including the memory/workflow annotations and epistemic ledger. There are no declared evidenced-absence records whose searched boundary needs adjudication. The bounded negative statements remain confined to inspected modules or explicitly selected routes, not opaque providers or excluded applications.

The two `Part of:` relations are semantically supported: the occurrence-check stage is contained in the combined audit, and parser admission is contained in support judgment. Direct reuse of those stages does not invalidate their containment on the parent paths. The [reconciliation](reconciliation.md#reconciliation) correctly retains valid containers, distinguishes result objects from producing routes and explains the overlapping cache, benchmark and example accounts. No supersession is proposed, no missing operative part changes a central conclusion, and no unresolved disagreement between reports was identified. The parser mismatch is a shared source-doctrine discrepancy, not an inter-report conflict.

Omission questions were selected from the frozen tree and producer/consumer dependencies: whether another exported path evades a claimed mandatory control; whether a shipped caller enforces answer delivery or retains judgments; whether evaluation output feeds a later policy update; and whether CI supplies a stronger admission guarantee. Export inspection, both callers, benchmark write/read consumers and publication dependencies give supported dispositions, as described above. Presentation-path inspection did not require changing the bounded auditor or selected-workflow conclusions. This is not a complete audit of presentation claims, every corpus item, historical development or external applications. Such comparisons are not emitted by these reports.

Further optional omission expansion stopped because the identified alternatives have dispositions, the consequential implementation claims remain supported at their declared breadth, and no known material contradiction remains unaddressed. Missing live-model, provider, provenance and causal evidence is already attached to the affected conclusions; it does not justify either an observed-benefit claim or a system-wide absence claim. These faithfully scoped uncertainties require no additional verifier limit.

## Blockers

none

## Limits

none
