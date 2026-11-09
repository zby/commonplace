---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of verbatim-citation-gate: normalized quote checks, offset checks, callback judgment and release admission."
run-id: AAS-2026-11-08-verbatim-citation-gate-d205c9f72d5a-01
reviewed-boundary: "2113d603031a554ed901a44648307bd3b711ea10"
---

# verbatim-citation-gate runtime report

## Runtime account

This is a returning citation auditor, not a scheduler or enclosing agent. The caller owns the supplied claim, quote, document identity, document dictionary and optional callback. The library owns deterministic matching, prompt construction and result parsing. It returns a string or structured result; it does not itself suppress a user-facing answer. All implementation findings below use SRC-1 at the frozen revision. No target code, tests, examples or providers were executed. Operation and benefit remain uninspected, rather than absent.

### Ordinary invocation and effect boundary

The shipped quickstart iterates a static citation batch and invokes `audit_citation` with a document dictionary and offline callback; it prints each returned verdict (SRC-1, `examples/quickstart.py`). The substantive progression is [RT-RTE-audit-citation](#rt-rte-audit-citation): normalize the quote, search the attributed document first, search other supplied documents on failure, and either return the deterministic result or ask the callback to judge support. The callback receives a fixed system instruction plus the original claim, original quote and **entire original cited document**, not normalized text or a selected neighboring passage. There is no library context trimming, retrieval, conversation history, tool loop or per-task worker context in this path. The next step after the return belongs to the caller (SRC-1, `src/verbatim_citation_gate/judge.py`).

There is no persistent citation identifier or internal job identity: document keys identify caller-supplied values. Matching uses symbolic string rules; semantic support uses natural-language instructions interpreted by a caller-selected model. A bounded process-local normalization cache accelerates repeated strings; it is not a knowledge admission mechanism. The callback is synchronous, with no library timeout, retry or cancellation control. It can perform arbitrary caller-defined work: the small callback interface is not a sandbox or permission grant. The package declares no provider dependency, transport or model pin (SRC-1, `src/verbatim_citation_gate/gate.py`, `src/verbatim_citation_gate/judge.py`, `pyproject.toml`).

### Guarantees and forcing routes

1. **Rejected quote does not call the judge through the dispatcher.** Owner: `audit_citation`; enforcement: return before callback invocation; strength: invariant for this control path. This is not a guarantee that every fabricated or insufficient citation will be rejected: matching means normalized occurrence, not truth or sufficient evidence. Direct `judge_support` is publicly exported and does not run this control, as traced in [RT-RTE-judge-support](#rt-rte-judge-support). Direct deterministic functions also bypass semantic judgment. The external contract is that consumers use the intended entry point and distinguish `found` from `supports`. Implementation conclusion status: wired. Operation conclusion status: uninspected.

2. **Contiguity and boundary checking concern normalized text.** Owner: `quote_gate` through `_contains`; strength: invariant for that predicate, not literal byte equality. Unicode normalization, case folding, format-character removal, hyphen repair and selected homoglyph folding deliberately alter matching identity. Numeric punctuation, signs and operators receive special handling. Partial words and numeric fragments are rejected at match boundaries, but no minimum evidence length or claim relevance rule is applied. Whole-word one-word quotes can pass. The alternate span route has a materially different acceptance predicate (SRC-1, `src/verbatim_citation_gate/gate.py`; [RT-RTE-span-gate](#rt-rte-span-gate)). Implementation conclusion status: wired. Operation conclusion status: uninspected.

3. **Offset and chunk validation are optional-path guarantees.** Owner: `resolve_span`; enforcement: reject invalid half-open Python character indices and reject spans outside an explicitly supplied valid chunk. Strength: invariant for this entry point with ordinary documented inputs. Neither `quote_gate` nor `audit_citation` accepts or enforces a chunk bound. With no optional quote, `span_gate` accepts any valid span with content, even one cutting through a word or number; with a quote it checks boundaries relative to the sliced span, not the full document. These are reachable documented branches, not hypothetical bypasses of a mandatory chunk policy. Implementation conclusion status: wired. Operation conclusion status: uninspected.

4. **The judge's default-refute policy is not a deterministic semantic guarantee.** Owner of instruction: library; owner of judgment: callback/model. Strength: policy. The parser converts recognized textual failure cases and caught callback exceptions to `unrelated`, but does not validate whether the reasoning is sound. A valid `supports` label is accepted even with missing reasoning or confidence. The source's blanket missing-field language therefore exceeds the implemented check. It also takes the first parseable JSON object rather than enforcing JSON-only output. These paths are reachable under the documented string-returning callback contract; an adversarial or constant callback can return `supports`. Non-string callback returns violate that contract and may raise during parsing, which occurs outside the callback exception handler. No provider compliance, timeout or isolation guarantee is established (SRC-1, `src/verbatim_citation_gate/judge.py`). Implementation conclusion status: wired. Operation conclusion status: uninspected.

The smallest forcing set inspected covers rejection before callback, offline `found`, direct judge invocation, and optional-quote/chunk span behavior. Tests contain fake callbacks for dispatch, garbage, exceptions and unknown verdicts, plus offset and numeric regressions. They are executable specifications, not observed run evidence here (SRC-1, `tests/test_gate.py`).

### Product changes and evaluation machinery

[RT-RTE-release-admission](#rt-rte-release-admission) separates declared human merge/release authority from automated artifact publication. CI defines tests on push, PR, manual dispatch and schedule, plus wheel/sdist installation checks. The publishing workflow builds on release publication or manual dispatch and conditionally publishes when `PYPI_READY` is true. It depends on its build job, not on the separate tests workflow. Repository protection, actual environment approval, publisher registration and release execution are unobserved; workflow text does not establish those deployed controls (SRC-1, `.github/workflows/tests.yml`, `.github/workflows/publish.yml`, `GOVERNANCE.md`). No product self-modification is performed by the citation dispatcher.

Evaluation is shipped machinery rather than a production retriever. `bench/build_corpus.py` fetches latest submissions for three fixed arXiv categories, unwraps summaries, filters short texts, combines document IDs and overwrites `bench/corpus.json`. Fixed query order does not freeze the external feed across dates. `bench/bench_gate.py` loads that file, constructs labeled cases, drops constructed negative cases whose normalized quote occurs anywhere in the corpus, runs `quote_gate` and prints aggregate results or JSON. The expected answer is supplied by case construction, not by an independent model oracle. Case filtering uses normalized substring presence without the gate's boundary predicate. This matters when interpreting benchmark population and detection claims. The benchmark explicitly excludes stage two and production class balance; its README's numbers are attributed reported results, not independently reproduced observations (SRC-1, `bench/build_corpus.py`, `bench/bench_gate.py`, `bench/README.md`).

Added substantive inspection beyond boundary's initial scope: complete test file, corpus builder and benchmark driver; CI test and publication workflows; governance. These provide implementation or declared policy evidence, not live deployment evidence. Benchmark transformation definitions in `bench/hard_cases.py`, raw corpus/results, hosted documentation and production traces were not substantively inspected here; no exhaustive benchmark validity or production accuracy conclusion follows.

## Shared records

### Components

#### RT-CMP-llm-call
Label: Caller-supplied model callback

Source-native identity: `LLMCall`; an in-process callable accepting system/user strings and returning text. The interface and message strings are symbolic and natural-language material respectively; the model reached through it is a distributed-parametric component whose weights and storage substrate are outside this source. The library neither changes model parameters nor pins an exact model version. A caller-controlled mutable endpoint can resolve to another model; no stability check prevents this. Provider state, training and actual endpoint behavior remain uninspected. The shipped demos use constant string callbacks rather than a distributed-parametric model (SRC-1, `src/verbatim_citation_gate/judge.py`, `examples/quickstart.py`).

> LLMCall = Callable[[str, str], str]
> --- `src/verbatim_citation_gate/judge.py`

### Operative objects

#### RT-OBJ-judge-system
Label: Skeptical judge system instruction

Source-native identity: `JUDGE_SYSTEM`, a natural-language Python string stored in the package module and passed to the callback. It requests evidence-relative judgment, weaker verdicts on uncertainty and a JSON response. It is static shipped instruction, not an artifact revised from audit outcomes. The callback/model is its intended interpreting consumer; instruction delivery alone does not establish compliance (SRC-1, `src/verbatim_citation_gate/judge.py`).

> You are a citation auditor. Your default verdict is that a citation does NOT support its
> claim; the quote must earn the verdict "supports".
> --- `src/verbatim_citation_gate/judge.py`

> 6. When torn between two verdicts, choose the one less favorable to the claim.
> --- `src/verbatim_citation_gate/judge.py`

### Routes

#### RT-RTE-audit-citation
Label: Combined citation audit

Caller-triggered open requests enter `audit_citation`; Python dispatch owns progression and the deterministic veto. `quote_gate` first searches the attributed document then others; only `found` with a supplied callback proceeds to [RT-RTE-judge-support](#rt-rte-judge-support). No human per-citation approval or expected-answer oracle is wired. This is citation classification, not admission of a product change. Claim and quote content do not mutate the package or documents (SRC-1, `src/verbatim_citation_gate/gate.py`, `src/verbatim_citation_gate/judge.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `not_found` or `misattributed` on gate rejection; `found` without a callback; otherwise the semantic verdict string, discarding structured reasoning and confidence.
- Later read-back: inapplicable — dispatcher stores no audit result for a later invocation.
- Delegated visibility: callback receives system instruction, original claim, quote and full cited source only on the model-enabled found path.
- Selection predicate: nonempty normalized content with contiguous whole-word/whole-number occurrence in the cited text; other-document hits are misattributed rather than found.
- Invalidation or expiry: normalization cache is bounded to 4096 raw input strings; changed document strings obtain different cache keys, not stale document-ID results.
- Activation or effect: implemented return can inform caller acceptance; no downstream user-delivery veto is implemented by the library.
- Evidence limits: no live model, supplied execution trace or downstream application acceptance was observed.

> gate = quote_gate(quote, doc_id, docs)
> if gate != "found":
>     return gate  # never reaches the judge — fabrications cost 0 tokens
> if llm_call is None:
>     return "found"
> return judge_support(claim, quote, docs[doc_id], llm_call).verdict
> --- `src/verbatim_citation_gate/judge.py`

> if isinstance(cited, str) and _contains(_normalized(cited), q):
>     return "found"
> --- `src/verbatim_citation_gate/gate.py`

> @lru_cache(maxsize=4096)
> def _normalized(text: str) -> str:
> --- `src/verbatim_citation_gate/gate.py`

#### RT-RTE-judge-support
Label: Direct or dispatched support judgment

The direct exported API accepts claim, quote, source and callback without checking quote existence. Python constructs the messages and invokes the callback once. The model proposes the verdict; parser vocabulary acceptance decides what is returned, without a human veto or independent semantic oracle. Operating mode is an open single request; no improvement trigger or retained revision is wired. Its natural-language guidance is [RT-OBJ-judge-system](#rt-obj-judge-system), interpreted through [RT-CMP-llm-call](#rt-cmp-llm-call). The route classifies a claim-source relationship, not a formulated-theory revision (SRC-1, `src/verbatim_citation_gate/__init__.py`, `src/verbatim_citation_gate/judge.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `Verdict(reasoning, verdict, confidence)`; callback exceptions or recognized parse failures become `unrelated` with zero confidence.
- Later read-back: inapplicable — no library persistence or accumulation of judgments.
- Delegated visibility: supplied claim, quote and entire source text plus the fixed system instruction cross the callback boundary; provider-side retention is uninspected.
- Selection predicate: direct calls always attempt the callback; parser chooses first parseable JSON object and accepts only four verdict labels.
- Invalidation or expiry: inapplicable — no cached semantic verdict or revision lifecycle.
- Activation or effect: returns the callback's accepted classification; adherence to the evidence policy is requested, not deterministically enforced.
- Evidence limits: callback contract requires text; non-string parser failures are not covered by the callback exception handler. Model accuracy and prompt-injection resistance are unobserved.

> user = f"CLAIM: {claim}\n\nQUOTE: {quote}\n\nSOURCE:\n{source}"
> try:
>     raw = llm_call(JUDGE_SYSTEM, user)
> except Exception:  # noqa: BLE001 — any judge failure is a closed gate, not a crash
>     return Verdict("judge call raised", "unrelated", 0.0)
> return _parse_verdict(raw)
> --- `src/verbatim_citation_gate/judge.py`

> verdict = data.get("verdict")
> if verdict not in _VALID:
>     return Verdict("judge verdict out of vocabulary", "unrelated", 0.0)
> try:
>     confidence = float(data.get("confidence", 0.0))
> except (ValueError, TypeError):
>     confidence = 0.0
> return Verdict(str(data.get("reasoning", "")), verdict, confidence)
> --- `src/verbatim_citation_gate/judge.py`

Confidence is converted, not clamped to the advertised range; missing fields are defaulted rather than always rejected. No confidence threshold controls the dispatcher's returned verdict.

#### RT-RTE-span-gate
Label: Character-span validation

Caller-selected document and offsets enter `resolve_span`, optionally with chunk bounds; `span_gate` consumes the slice and optionally checks a quote against it. The code owns selection and rejection. This is a deterministic alternative to textual attribution checks, not a combined offset-plus-model pipeline. Indices are Python Unicode string positions, not byte offsets. No human decision or semantic oracle is involved (SRC-1, `src/verbatim_citation_gate/gate.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: resolver returns `(slice, None)` or `(None, reason)`; gate maps invalid/content-free/mismatching input to `not_found`, otherwise `found`.
- Later read-back: inapplicable — no retained offset or document write.
- Delegated visibility: inapplicable — no callback or worker invoked.
- Selection predicate: known string document, valid nonempty integer bounds excluding booleans, optional containing valid tuple chunk; optional quote must occur with boundaries in the normalized slice.
- Invalidation or expiry: caller must supply offsets for its current document version; no version identity is recorded or checked.
- Activation or effect: returns validation classification only; no support judgment, source mutation or cross-document misattribution diagnosis.
- Evidence limits: no execution observed; full-document match boundaries are not checked when accepting an extracted span without a quote.

> if start < chunk_start or end > chunk_end:
>     return None, "crosses_chunk"
> --- `src/verbatim_citation_gate/gate.py`

> if quote is None:
>     return "found"
> --- `src/verbatim_citation_gate/gate.py`

> if _has_content(normalized_quote) and _contains(_normalized(resolved), normalized_quote):
>     return "found"
> --- `src/verbatim_citation_gate/gate.py`

#### RT-RTE-release-admission
Label: Product merge and package publication

Product proposals enter through contributors and maintainer review under declared governance. The named maintainer has final merge/release authority and can reject proposals. Changes may alter code, instructions or capabilities; CI and publication consume the resulting repository/artifacts, not citation audit history. This is a human-governed development path, not an autonomous runtime improvement loop. Guidance includes preserving the fail-closed invariant and MIT-compatible contributions. Merged files and release artifacts persist for later installations. Rollback automation is not specified in the inspected publication workflow; a recovery action would require external repository/release administration. Actual PR review and deployment permissions remain uninspected (SRC-1, `GOVERNANCE.md`, `.github/workflows/tests.yml`, `.github/workflows/publish.yml`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: workflow builds distributions and validates metadata; conditional publish job uploads artifacts via the PyPI action.
- Later read-back: package installation consumes retained release artifacts; no trace-fed product update is wired here.
- Delegated visibility: GitHub build and publish jobs exchange `dist` artifacts; publish job requests OIDC identity permission.
- Selection predicate: release publication or manual dispatch starts the build; publish requires successful build and `vars.PYPI_READY == 'true'`.
- Invalidation or expiry: release version derives from the module; deployed rollback and artifact revocation are uninspected.
- Activation or effect: artifact publication is wired conditionally, not evidence of actual publication or downstream installation.
- Evidence limits: governance is policy evidence; branch protection, environment approval and external publisher setup are not established. Separate test workflow success is not a dependency declared by the publication workflow.

> - **Maintainer:** Anton Dziatkovskii ([@tonydzi](https://github.com/tonydzi)), Palo Alto AI Research Lab.
>   Final say on merges, releases, and the fail-closed invariant.
> --- `GOVERNANCE.md`

> if: ${{ vars.PYPI_READY == 'true' }}
> --- `.github/workflows/publish.yml`

The test suite supplies assertions as an answer oracle for bounded regression cases; artifact checks validate packaging rather than semantic judge accuracy. Humans own proposal admission; software executes the declared build and conditional upload. No source passage establishes automatic rollback or a complete autonomous proposal-to-merge path.

### Claims

#### RT-CLM-closed-judge
Label: Fail-closed judge claim and implementation limit

The module claims missing fields fail closed. Implemented vocabulary checking and callback exception handling support narrower guarantees; defaults permit a valid verdict without reasoning or confidence. This claim must not be read as full schema validation, semantic verification or proof that every callback failure returns safely. Evidence: SRC-1, `src/verbatim_citation_gate/judge.py`, with the operative parsing passage retained in [RT-RTE-judge-support](#rt-rte-judge-support).

> Any parse failure — no JSON, missing fields, an out-of-vocabulary verdict —
> is treated as *not support*, never retried into optimism.
> --- `src/verbatim_citation_gate/judge.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-judge-instruction
Label: System instruction to callback judgment

Consumer: caller-selected model behind `llm_call`. Channel: first positional system string, alongside a separately constructed user string. Force: requested policy rather than code-level semantic constraint; a compliant callback may use it to select a verdict, while arbitrary callbacks can ignore it. Horizon: one judgment invocation; provider-side persistence is uninspected. The package's returned classification can influence caller decisions, but its activation in an enclosing application is not observed. Evidence: SRC-1, `src/verbatim_citation_gate/judge.py`; minimum instruction and delivery passages are retained in [RT-OBJ-judge-system](#rt-obj-judge-system) and [RT-RTE-judge-support](#rt-rte-judge-support).

## Annotations

none
