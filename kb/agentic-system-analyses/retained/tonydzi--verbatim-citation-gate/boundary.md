---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "The verbatim-citation-gate citation-auditing library and its shipped consumers at commit 2113d603031a554ed901a44648307bd3b711ea10."
run-id: AAS-2026-11-08-verbatim-citation-gate-d205c9f72d5a-01
result-disposition: complete
target-class: extension or tool mechanism
boundary-kind: subsystem-only
reviewed-boundary: 2113d603031a554ed901a44648307bd3b711ea10
analysis-cutoff: "2026-11-08"
evidence-tier: code-grounded
source:
  identity: https://github.com/tonydzi/verbatim-citation-gate
  kind: git
  path: /home/zby/llm/commonplace/.commonplace/worktrees/verbatim-citation-gate-1aab9156abd4/related-systems/tonydzi--verbatim-citation-gate
  revision: 2113d603031a554ed901a44648307bd3b711ea10
  sha256: null
---

# verbatim-citation-gate boundary

## Boundary and evidence

The target is the shipped citation-auditing library, including its deterministic quote and character-span checks, optional model-backed support judgment, exported interfaces, shipped example callers and evaluation material. It is an **extension or tool mechanism**, not an enclosing agent runtime. Its intended use is auditing a supplied claim, quote and document attribution before a consuming application treats that citation as support. The boundary is **subsystem-only**: the library supplies an auditing computation within a larger retrieval or agent application, rather than that application's complete operational loop (SRC-1, `src/verbatim_citation_gate/__init__.py`, `src/verbatim_citation_gate/judge.py`, `examples/quickstart.py`).

The combined mechanism is in scope because its support judgment depends on a model call supplied through a callback. The deterministic gate remains usable without that callback. The shipped dispatcher establishes both paths (SRC-1, `src/verbatim_citation_gate/judge.py`):

> gate = quote_gate(quote, doc_id, docs)
> if gate != "found":
>     return gate  # never reaches the judge — fabrications cost 0 tokens
> if llm_call is None:
>     return "found"
> return judge_support(claim, quote, docs[doc_id], llm_call).verdict
> --- `src/verbatim_citation_gate/judge.py`

The model boundary is explicit: the library constructs prompts and invokes the supplied callback; it does not select or implement a provider transport (SRC-1, `src/verbatim_citation_gate/judge.py`):

> user = f"CLAIM: {claim}\n\nQUOTE: {quote}\n\nSOURCE:\n{source}"
> try:
>     raw = llm_call(JUDGE_SYSTEM, user)
> except Exception:  # noqa: BLE001 — any judge failure is a closed gate, not a crash
>     return Verdict("judge call raised", "unrelated", 0.0)
> return _parse_verdict(raw)
> --- `src/verbatim_citation_gate/judge.py`

Functional inclusions are normalization and matching, attribution checks across supplied documents, offset and chunk validation, the judge prompt and response parsing, and the audit dispatcher. The public exports include direct gate and judge entry points as well as the combined dispatcher; the boundary does not assume callers must use the combined path (SRC-1, `src/verbatim_citation_gate/gate.py`, `src/verbatim_citation_gate/__init__.py`, `src/verbatim_citation_gate/judge.py`).

The shipped callers are not excluded hosts. Both example scripts supply fixed document dictionaries and citation batches, call the combined auditor and print verdicts. Their model callbacks are offline stand-ins, not evidence of live-model judgment quality. The demo explicitly identifies its callback (SRC-1, `examples/demo.py`, `examples/quickstart.py`):

> """Stand-in for your model. Counts calls so the demo cannot overstate itself."""
> --- `examples/demo.py`

The test suite and benchmark remain within the target's evidence scope. Initial bounded searches traced the test callbacks and audit assertions, benchmark corpus acquisition and persistence, and benchmark case construction and reporting. The benchmark's own scope statement excludes stage-two measurement (SRC-1, `tests/test_gate.py`, `bench/build_corpus.py`, `bench/bench_gate.py`, `bench/hard_cases.py`, `bench/README.md`):

> * **Stage 2, the judge.** These numbers cover the deterministic gate only.
> --- `bench/README.md`

External dependencies and exclusions:

- The package declares no runtime dependencies; Python's standard library implements the gate and parser. Model-provider clients are caller-supplied, not packaged transports (SRC-1, `pyproject.toml`, `src/verbatim_citation_gate/judge.py`). Provider internals are outside this source, preventing conclusions about provider reliability, model selection or actual model accuracy.
- Retrieval, document acquisition for a production application, citation generation, downstream acceptance policy and user delivery are outside the library boundary. The dispatcher accepts supplied inputs and returns a verdict; the examples print it (SRC-1, `src/verbatim_citation_gate/judge.py`, `examples/demo.py`, `examples/quickstart.py`). This prevents attributing an enclosing application's enforcement or end-to-end citation correctness to the library.
- The benchmark corpus builder is shipped evaluation infrastructure, not an excluded production retriever (SRC-1, `bench/build_corpus.py`). Its external arXiv service is not separately acquired; later analysis may inspect only the committed corpus and source, not infer current service contents.
- Linked ecosystem repositories, issues, hosted pages and provider documentation have not been acquired. Their contents supply no evidence here. In particular, repository claims about extraction from production do not establish the wider fleet's operation (SRC-1, `README.md`).

The frozen evidence is the entire registered repository at **2113d603031a554ed901a44648307bd3b711ea10**, with applicability cutoff **2026-11-08**. The acquisition object is preserved unchanged above, and the checkout's HEAD was verified against it. Overall evidence is **code-grounded**, based on source inspection, not target execution. No tests, examples, benchmark or model calls were executed. This prevents a claim of independently observed runtime behavior or reproduced benchmark performance.

Initial inspection covered the complete tracked tree, all package Python modules, packaging metadata, README and both example scripts, plus the benchmark README and bounded symbol/call-site searches over tests, benchmark programs and the demo-image generator. The committed corpus and result files, remaining documentation, CI/release configuration and governance files have not yet been substantively inspected. They are available evidence within SRC-1, not access gaps or deliberate exclusions. No whole-repository operational-coverage claim is made.

## Source register

| Source ID | Kind | Identity/location | Revision or capture | Evidence layer | Inspected scope | Citation anchors | Access gaps and conclusion prevented |
|---|---|---|---|---|---|---|---|
| SRC-1 | git | `https://github.com/tonydzi/verbatim-citation-gate` | 2113d603031a554ed901a44648307bd3b711ea10 | implementation; doctrine/design | Access root: `/home/zby/llm/commonplace/.commonplace/worktrees/verbatim-citation-gate-1aab9156abd4/related-systems/tonydzi--verbatim-citation-gate`. Implementation: `src/verbatim_citation_gate/__init__.py`, `src/verbatim_citation_gate/gate.py`, `src/verbatim_citation_gate/judge.py`, `examples/demo.py`, `examples/quickstart.py`, `pyproject.toml`; bounded searches of `tests/test_gate.py`, `bench/build_corpus.py`, `bench/bench_gate.py`, `bench/hard_cases.py`, `docs/make_demo_gif.py`. Doctrine/design: `README.md`, `bench/README.md`. | Implementation: [public exports](https://github.com/tonydzi/verbatim-citation-gate/blob/2113d603031a554ed901a44648307bd3b711ea10/src/verbatim_citation_gate/__init__.py), [gate](https://github.com/tonydzi/verbatim-citation-gate/blob/2113d603031a554ed901a44648307bd3b711ea10/src/verbatim_citation_gate/gate.py), [judge and dispatcher](https://github.com/tonydzi/verbatim-citation-gate/blob/2113d603031a554ed901a44648307bd3b711ea10/src/verbatim_citation_gate/judge.py), [example caller](https://github.com/tonydzi/verbatim-citation-gate/blob/2113d603031a554ed901a44648307bd3b711ea10/examples/demo.py). Doctrine/design: [README](https://github.com/tonydzi/verbatim-citation-gate/blob/2113d603031a554ed901a44648307bd3b711ea10/README.md), [benchmark scope](https://github.com/tonydzi/verbatim-citation-gate/blob/2113d603031a554ed901a44648307bd3b711ea10/bench/README.md). | No checkout access gap identified. No independently observed run or causal experiment: source and author-supplied evaluation material do not establish reproduced results, production class balance or live-model support accuracy. External hosts and linked repositories are not captured, preventing conclusions about their operation. |
