---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Memory and context in verbatim-citation-gate: process-local normalization reuse, full-source judge input and retained benchmark corpus."
run-id: AAS-2026-11-08-verbatim-citation-gate-d205c9f72d5a-01
source-identity: https://github.com/tonydzi/verbatim-citation-gate
reviewed-boundary: 2113d603031a554ed901a44648307bd3b711ea10
---

# verbatim-citation-gate memory report

## Boundary and evidence

The memory boundary follows the subsystem in [boundary](boundary.md): public deterministic and model-callback APIs, shipped example consumers and evaluation infrastructure. It includes process-local derived text, model-visible source selection, benchmark persistence and retained evaluation output. It excludes enclosing production retrieval, application acceptance and inaccessible provider state. Those exclusions prevent conclusions about production document provenance, conversation memory and actual model retention.

All direct evidence is SRC-1 at the reviewed commit. HEAD was rechecked as 2113d603031a554ed901a44648307bd3b711ea10. Direct reads covered all three package modules, both example callers, packaging metadata, the corpus builder, benchmark driver, hard-case transformations, benchmark README and results JSON. The corpus was sampled at its first seven document entries, not audited in full. The runtime supplied the release-policy account; it was not independently reinspected here. No target program was executed.

| Entry point or memory operation | Source path (SRC-1) | Coverage and limits |
|---|---|---|
| Public API dispatch; no packaged CLI entry point | `src/verbatim_citation_gate/__init__.py`, `pyproject.toml` | Exports match supplied runtime routes; no separate registered tool, hook or service operation in these interfaces. This does not survey external host registration. |
| Normalization and repeated matching | `src/verbatim_citation_gate/gate.py` | [MEM-OBJ-normalized](#mem-obj-normalized), [MEM-RTE-normalization-reuse](#mem-rte-normalization-reuse); direct read, including public uncached `normalize`. |
| Optional offset/chunk extraction | `src/verbatim_citation_gate/gate.py` | [RT-RTE-span-gate](runtime.md#rt-rte-span-gate); direct read confirms current-input selection, not persistent chunk memory. |
| Combined audit and direct judge | `src/verbatim_citation_gate/judge.py` | [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation), [RT-RTE-judge-support](runtime.md#rt-rte-judge-support); direct read and annotations below. |
| Shipped consumers | `examples/demo.py`, `examples/quickstart.py` | Direct read: static dictionaries and printed verdicts; no audit-result reload. Demo counter is current-process accounting, not behavior-shaping memory. |
| Corpus acquisition, replacement and later loading | `bench/build_corpus.py`, `bench/bench_gate.py`, `bench/corpus.json` | [MEM-OBJ-corpus](#mem-obj-corpus), [MEM-RTE-corpus-reload](#mem-rte-corpus-reload); corpus sample does not establish authenticity of every abstract. |
| Case curation and report retention | `bench/hard_cases.py`, `bench/bench_gate.py`, `bench/results.json`, `bench/README.md` | [MEM-OBJ-results](#mem-obj-results); direct reads. Printed reports and manually redirected files do not establish automatic runtime instruction updates. |
| Release/install of static instructions and code | `GOVERNANCE.md`, `.github/workflows/publish.yml` | Supplied [RT-RTE-release-admission](runtime.md#rt-rte-release-admission), not newly read. No audit-outcome-to-release transformation established. |
| Provider history, weights, callback side effects | `src/verbatim_citation_gate/judge.py` | [RT-CMP-llm-call](runtime.md#rt-cmp-llm-call); callback implementation beyond shipped stand-ins is unavailable. Persistence, truncation and actual endpoint identity remain unresolved. |

## Core ideas

The main retained runtime artifact is a bounded memoization cache, not a semantic memory store. It retains raw string keys and normalized string values for later deterministic comparisons. It neither retains support decisions nor supplies derived memories to the model ([MEM-OBJ-normalized](#mem-obj-normalized)).

The judge receives the entire original cited document. The deterministic gate controls whether this call occurs, but does not extract a smaller evidence window. Direct judge calls bypass that selection. No library token budget or compaction is applied to these messages; provider-side handling remains unknown ([RT-RTE-judge-support](runtime.md#rt-rte-judge-support)).

Evaluation has a separate durable path: acquired abstracts are transformed and written to a JSON corpus, then loaded in another benchmark invocation. Reports can be retained for human inspection, but no automatic report-to-rule revision or learned capability update is shown ([MEM-RTE-corpus-reload](#mem-rte-corpus-reload), [MEM-OBJ-results](#mem-obj-results)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-normalized
Label: Normalized text cache

Source-native identity: `_normalized`, the cached wrapper of `normalize`. Storage is Python process memory maintained by `functools.lru_cache`, bounded to 4096 raw input strings, not 4096 tokens or documents. Raw string keys preserve inputs; values are derived strings with typography, case and punctuation transformations. At the comparison consumer, strings have symbolic form: fixed substring and boundary predicates decide results, without interpreting their meaning. They are not model summaries or opaque embeddings. The retained derivation does not carry an explanation per value; the static normalization code supplies the transformation rules. Cache access metadata is an implementation detail of the standard-library decorator, not source evidence or citation confidence (SRC-1, `src/verbatim_citation_gate/gate.py`).

Closest supplied record: [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation) mentions this cache but declares an invocation route, not its retained object. This object also serves span validation, so it is not exclusively part of the audit route.

> @lru_cache(maxsize=4096)
> def _normalized(text: str) -> str:
>     """Normalize repeated text once, retaining up to 4,096 raw inputs."""
>     return normalize(text)
> --- `src/verbatim_citation_gate/gate.py`

#### MEM-OBJ-corpus
Label: Benchmark corpus

Source-native identity: `bench/corpus.json`, a filesystem JSON mapping of document IDs to abstract text. IDs and JSON structure have symbolic form; abstracts are natural-language source content, consumed symbolically by the benchmark's text operations. They are not retained agent traces. Builder lineage is external arXiv summaries, whitespace unwrapping, final-component ID extraction, minimum-length filtering and assignment into a dictionary. Same-ID assignment replaces the previous value across category results. The frozen file's complete provenance and acquisition time are not authenticated by the implementation alone (SRC-1, `bench/build_corpus.py`, `bench/corpus.json`).

Closest supplied record: [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation) takes generic caller documents, not this persisted evaluation artifact. Runtime discusses corpus building in prose but declares no corresponding object. No duplicate object identified.

> text = " ".join(summary.split())
> doc_id = raw_id.rsplit("/", 1)[-1]
> if doc_id and len(text) > 400:
>     out.append((doc_id, text))
> --- `bench/build_corpus.py`

#### MEM-OBJ-results
Label: Benchmark results report

Source-native identity: `bench/results.json`, retained filesystem JSON with per-mode counts, aggregate rates and a failure sample. Counts, expected labels and returned labels are symbolic evaluation data; truncated quote strings are readable display excerpts, not complete source evidence or opaque hidden payloads. The driver's report construction retains at most 40 failures and limits each quote to 110 characters. It does not retain every case, full source, successful-case trace or a complete reason for each rejection. The README offers shell redirection to retain the printed JSON; the driver itself prints, rather than writing this path. The committed file is author-supplied evaluation material, not independently authenticated execution evidence (SRC-1, `bench/bench_gate.py`, `bench/results.json`, `bench/README.md`).

Closest supplied record: [RT-RTE-release-admission](runtime.md#rt-rte-release-admission) concerns release artifacts, not benchmark output; no supplied object counterpart exists. A human can inspect the report, but no inspected executable consumer reloads it into gate policy or the judge prompt.

> elif len(failures) < 40:
>     failures.append({**c, "got": got, "quote": c["quote"][:110]})
> --- `bench/bench_gate.py`

> python bench/bench_gate.py --json > bench/results.json
> --- `bench/README.md`

### Routes

#### MEM-RTE-normalization-reuse
Label: Reuse normalized input

Code in quote and span checking requests normalization; cache machinery selects by the exact raw string. A cache miss computes a transformed value and admits it automatically without human approval. Physical retention is decorator-owned; input authorship remains caller-controlled. The later deterministic matcher consumes the derived value under the same fixed rules. Public `normalize` is an alternative uncached entry point. This is memoization, not content-directed criticism or admission of new knowledge (SRC-1, `src/verbatim_citation_gate/gate.py`). Closest supplied routes are [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation) and [RT-RTE-span-gate](runtime.md#rt-rte-span-gate); this shared helper's retained reuse crosses both rather than duplicating either full invocation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: normalized string, computed or reused.
- Later read-back: a subsequent normalization request for the same raw string can reuse its retained value within this Python process.
- Delegated visibility: inapplicable — cached values are not delivered to a model or worker by this route.
- Selection predicate: exact raw string cache key, not query similarity, document ID or a relevance score.
- Invalidation or expiry: LRU capacity 4096 and process lifetime; changed strings are new keys, with no document-ID version invalidation needed.
- Activation or effect: supplies the string used by deterministic comparison; no demonstrated performance benefit or changed decision quality is inferred.
- Evidence limits: no target execution; provider memory and durable storage are outside this cache.

The cache definition is quoted in [MEM-OBJ-normalized](#mem-obj-normalized). The matcher consumer is explicit:

> if isinstance(cited, str) and _contains(_normalized(cited), q):
>     return "found"
> --- `src/verbatim_citation_gate/gate.py`

#### MEM-RTE-corpus-reload
Label: Build and reload corpus

A script operator starts acquisition; code selects summaries, filters and overwrites the corpus without per-document human approval. The operator's human identity is unresolved by script invocation alone. Another operator-triggered benchmark loads that file, constructs synthetic expected-answer cases, removes accidentally real negatives and invokes `quote_gate`. Case code supplies the answer oracle; it is not independent external semantic validation. Operating mode is a bounded constructed benchmark, not autonomous product revision. No automatic improvement trigger, product admission, rollback or content veto is implemented here. Existing corpus replacement is whole-file; the builder specifies no archival recovery (SRC-1, `bench/build_corpus.py`, `bench/bench_gate.py`). Closest supplied record is [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation), which audits individual current requests rather than acquiring and reloading a durable corpus.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: builder writes JSON and prints counts; benchmark prints text or JSON aggregate results.
- Later read-back: benchmark reads the retained corpus file on each invocation, then passes its document dictionary to deterministic gate calls.
- Delegated visibility: inapplicable — this benchmark does not invoke the support-judge callback.
- Selection predicate: three fixed categories, latest submissions, up to 100 feed entries each; retain nonempty IDs with unwrapped summaries longer than 400 characters. Benchmark uses sentence-length filtering and fixed-stride alternate documents; synthetic negative cases are dropped when normalized text appears anywhere in the corpus.
- Invalidation or expiry: builder overwrites the corpus; no TTL or acquisition timestamp is enforced. Latest-submission queries mean fixed query order does not freeze future input.
- Activation or effect: corpus and case-generation rules determine the tested population and returned report; they do not update runtime gate rules.
- Evidence limits: committed corpus/results establish retained artifacts, not independently reproduced execution or live-feed authenticity; stage-two quality is not tested.

> OUT.write_text(json.dumps(docs, ensure_ascii=False, indent=1), encoding="utf-8")
> --- `bench/build_corpus.py`

> docs = json.loads(CORPUS.read_text(encoding="utf-8"))
> cases, dropped = drop_accidental_truths(build_cases(docs), docs)
> --- `bench/bench_gate.py`

> if c["expect"] == "not_found":
>     needle = normalize(c["quote"])
>     if any(needle in h for h in haystacks.values()):
>         dropped += 1
>         continue
> --- `bench/bench_gate.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-judge-support](runtime.md#rt-rte-judge-support)

Read-back scope: supplied current claim, quote and source are not necessarily accumulated-through-use memory. Caller provenance is unresolved. The code constructs a user string with the entire source, alongside static `JUDGE_SYSTEM`; neither normalization-cache output nor a selected evidence summary replaces it. Selection is caller-supplied source for the direct API, and `docs[doc_id]` after `found` for the combined API. There is no library context/token cap, old-turn eviction, compaction, sub-agent isolation or reload pointer in these inspected modules. Provider-side truncation, storage and conversation reuse are uninspected. The supplied record's message-construction quotation supplies the decisive passage (SRC-1, `src/verbatim_citation_gate/judge.py`). A Python function frame is not evidence of a separate model conversation frame: only two strings cross the callback interface.

#### On [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation)

The direct judge returns reasoning, label and confidence, but this dispatcher keeps only `.verdict`. Thus a later application using the ordinary dispatcher does not receive the generated reason through this return channel. Neither return form is persisted by this module. A source caller can retain it externally, but the shipped examples only print classifications; no later audit consumes those outputs (SRC-1, `src/verbatim_citation_gate/judge.py`, `examples/demo.py`, `examples/quickstart.py`). The supplied dispatcher quotation establishes the omission; it prevents treating returned labels as a retained rationale-backed knowledge store.

## Write side

Admission is surface-specific. Cache admission is automatic on normalization requests, with deterministic text transformation rather than model authorship. Caller document selection and content editing are outside the generic API; accepting a dictionary does not establish human approval or provenance verification. Offset extraction changes neither that dictionary nor retained source content ([MEM-RTE-normalization-reuse](#mem-rte-normalization-reuse), [RT-RTE-span-gate](runtime.md#rt-rte-span-gate)).

Corpus curation is software-controlled after script invocation: whitespace unwrapping and length filtering, not semantic vetting. Bad-length/missing-ID entries are omitted; replacements overwrite by key and then by file. Synthetic case rejection affects the benchmark population, not the corpus or installed policy ([MEM-RTE-corpus-reload](#mem-rte-corpus-reload)). Reports retain aggregate outcomes and a lossy sample, not a derived reusable instruction. No trace-to-derived-behavior-to-later-agent chain is established by storing those reports. Human development may use results, but the supplied release route does not wire that causal chain ([MEM-OBJ-results](#mem-obj-results), [RT-RTE-release-admission](runtime.md#rt-rte-release-admission)).

## Read-back

Two implemented later-use paths are supported: exact-key process-local normalization reuse and filesystem corpus reload. Both are requested reads, not unsolicited contextual injection. Cache capacity is entry-count based; corpus reload loads the whole JSON file and then constructs cases. Neither selects model-visible memories. The judge's full-source message is current-request context delivery, not evidence that earlier judgments influence subsequent invocations. Static instruction delivery remains the policy path described in [RT-BAP-judge-instruction](runtime.md#rt-bap-judge-instruction); it is not learned memory.

No source trust score is acquired from a quote match. The deterministic gate establishes normalized occurrence among supplied strings; the judge instruction asks the model to exclude outside knowledge. The supplied record establishes requested policy, not prompt-injection resistance or source authenticity ([RT-OBJ-judge-system](runtime.md#rt-obj-judge-system), [RT-RTE-audit-citation](runtime.md#rt-rte-audit-citation)).

## Integration issues

- No correction to a supplied runtime fact is required. New cache-object and helper-route records expand its memoization account without replacing the combined audit or span routes; their cross-route identity is explained in [MEM-OBJ-normalized](#mem-obj-normalized) and [MEM-RTE-normalization-reuse](#mem-rte-normalization-reuse).
- Corpus and report records have no supplied object counterparts. They separate retained evaluation inputs from lossy output reports, rather than treating all evaluation material as runtime knowledge ([MEM-OBJ-corpus](#mem-obj-corpus), [MEM-OBJ-results](#mem-obj-results)).
- Callback retention, context limits and actual model identity remain unresolved, preventing system-wide memory or isolation guarantees; the supplied callback contract and message construction do not decide them ([RT-CMP-llm-call](runtime.md#rt-cmp-llm-call), [RT-RTE-judge-support](runtime.md#rt-rte-judge-support)).
- Exact acquisition provenance of the committed corpus and causal provenance of the committed results remain unresolved. Inspected generation code and attributed README instructions support capability and intended lineage, not independently reproduced results or a demonstrated learning loop ([MEM-RTE-corpus-reload](#mem-rte-corpus-reload), [MEM-OBJ-results](#mem-obj-results)).

## Limitations and checks

Source identity was rechecked against the boundary's full commit. Method identity is the supplied invocation, member type, worker rules and record contract; no method changes were made. Searches for persistence and context operations were bounded to included package, examples, benchmark code and packaging metadata, followed by direct source reads. Corpus content sampling is not a whole-corpus authenticity review. Evaluation and release conclusions retain their different evidence layers. No claim of exercised memory, improved capacity or causal benefit follows from implementation alone.

Validation: passed with the required role-specific commonplace-validate command; this establishes structural and quotation checks, not semantic acceptance.
