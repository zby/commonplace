---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Secure LLM-Wiki: source compilation, security admission and later evidential reliance, distinguished from factual acceptance."
run-id: AAS-2026-10-19-secure-llm-wiki-df02f419bddb-01
reviewed-boundary: dfbc60e37487b61e9a5cbce1271a13576a776d51
---

# Secure LLM-Wiki epistemic report

## Source-and-claim boundary

Question: what warrants the statements that Secure LLM-Wiki stores and presents as evidence, and which checks actually govern their later use? Scope and exclusions are those of the [boundary](boundary.md#boundary-and-evidence); sources are registered only in its [Source register](boundary.md#source-register). SRC-1 supplies implementation and doctrine/design, not observed operation or causal experiments. No target code was executed.

The material routes are source acquisition, extraction/parsing, manipulation review, deterministic checks, disposition, retention, context selection/rendering, answer generation and operator withdrawal/configuration. Source warrant is unknown: a URI label and content hash identify input but do not verify its statements. The model-mediated extraction and answer edges have indeterminate semantic relations without completions; this does not prevent tracing their implemented consumers. There is no supplied generated wiki instance from which to individuate actual retained propositions, accepted factual claims or exercised reliance.

Consequential claims are [RT-CLM-security-boundary](runtime.md#rt-clm-security-boundary), [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) and [EPI-CLM-quality-evidence](#epi-clm-quality-evidence). A security-oriented reference artifact need not be a truth-certification product. Nevertheless, presenting admitted statements as high-quality evidence makes the distinction between security admission and factual warrant consequential.

### Coverage

Direct reads below are of SRC-1 at the reviewed commit. Supplied runtime findings remain separately identified; a path appearing in the runtime is not claimed as a direct read here.

| Entry point or operation | Source path | Coverage and records | Limit and conclusion prevented |
|---|---|---|---|
| Installed CLI and module dispatch; init/list/context/query/clear/ingest | `pyproject.toml`; `src/secure_wiki/__main__.py` | Packaging via runtime; dispatch, source reading, pipeline, query/context/list/clear directly read; [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance), [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), [RT-RTE-context-query](runtime.md#rt-rte-context-query) | Folder scheduling and interactive trust setup supplied by runtime; no session evidence. |
| Extraction and JSON compatibility routes | `src/secure_wiki/extraction/extractor.py`; `src/secure_wiki/prompts.py` | Direct, including all prompt builders; [RT-RTE-extraction-parsing](runtime.md#rt-rte-extraction-parsing) | No completion demonstrates faithful extraction, entailment or conjecture. |
| Sanitizer, trust registry, provenance, review and consistency | `src/secure_wiki/ingestion/sanitizer.py`; `src/secure_wiki/trust/tiering.py`; `src/secure_wiki/models.py`; `src/secure_wiki/review/adversarial.py`; `src/secure_wiki/gate/write_gate.py` | Direct; [EPI-RTE-security-checks](#epi-rte-security-checks), [EPI-RTE-gate-disposition](#epi-rte-gate-disposition) | No live reviewer or vector evidence; detection quality and factual reliability unmeasured. |
| Write/reload/quarantine/delete/reset, including direct store API | `src/secure_wiki/store/wiki_store.py`; `src/secure_wiki/store/embedding_store.py` | Direct, complete modules; [EPI-RTE-store-retention](#epi-rte-store-retention) | Filesystem/Git operation not observed; manual edits have no authenticated lineage here. |
| Actual loader versus alternate builders | `src/secure_wiki/read/hygiene.py`; `src/secure_wiki/prompts.py` | Direct; [EPI-RTE-text-render](#epi-rte-text-render), [RT-RTE-context-query](runtime.md#rt-rte-context-query) | Natural-language non-instructionality remains a model request. |
| Model adapters and external parametric state | `src/secure_wiki/llm_client.py` | Supplied runtime inspection; [RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model), [RT-CMP-review-model](runtime.md#rt-cmp-review-model), [RT-CMP-embed-model](runtime.md#rt-cmp-embed-model) | External weights, training, exact deployed versions and service behavior uninspected; no model-internal epistemic conclusion. |
| Public purpose and evidence framing | `README.md`; `src/secure_wiki/prompts.py` | Direct; the three claim records above | Doctrine does not establish operation. |
| Regression evaluators and future maintenance | `tests/test_injection_corpus.py`; `tests/test_read_hygiene.py`; `docs/roadmap.md` | Supplied boundary/runtime findings, not direct reads; [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), [RT-RTE-context-query](runtime.md#rt-rte-context-query), [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance) | Mocked reviewer verdict is a test-only reference; no live factual or manipulation evaluation. Future promotion is not an implemented route. |

The shipped parser dispatches the six listed operations, not a registered model-tool or hook loop. No new CLI operation omitted by runtime was found in direct dispatch inspection (SRC-1, `src/secure_wiki/__main__.py`). Direct storage, pending inclusion and strict alternate prompt builders are included rather than silently treated as normal ingestion. This coverage supports bounded conclusions about the shipped application routes, not external consumers of printed context, arbitrary local edits or opaque provider internals.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-source-text](#epi-obj-source-text) | see record | see record | SRC-1, `src/secure_wiki/__main__.py` | see record |
| [EPI-OBJ-claim-text](#epi-obj-claim-text) | see record | see record | SRC-1, `src/secure_wiki/models.py` | see record |
| [EPI-OBJ-claim-metadata](#epi-obj-claim-metadata) | see record | see record | SRC-1, `src/secure_wiki/models.py` | see record |
| [EPI-OBJ-review-result](#epi-obj-review-result) | see record | see record | SRC-1, `src/secure_wiki/review/adversarial.py` | see record |
| [EPI-OBJ-claim-embeddings](#epi-obj-claim-embeddings) | see record | see record | SRC-1, `src/secure_wiki/store/embedding_store.py` | see record |
| [EPI-OBJ-query-answer](#epi-obj-query-answer) | see record | see record | SRC-1, `src/secure_wiki/__main__.py` | see record |
| [RT-OBJ-system-prompts](runtime.md#rt-obj-system-prompts) | Task/security policy, not accumulated factual knowledge | see record | SRC-1, `src/secure_wiki/prompts.py` | see record |
| [RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model), [RT-CMP-review-model](runtime.md#rt-cmp-review-model), [RT-CMP-embed-model](runtime.md#rt-cmp-embed-model) | Not determinable from external weights | see records | SRC-1, `src/secure_wiki/llm_client.py` | see records |

## Authority-route ledger

Each row separates a function, even where the same supplied container record supports several functions. `see` delegates the owned detail, not the architectural status or content-edge classification. All implemented rows are source-level capacities; none is reported as exercised.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) | content transformation | implemented | [EPI-OBJ-source-text](#epi-obj-source-text) | truth-apt transformation: acquisition/import | see object | see object | see route | see route | see route | Source warrant unknown | see route | see route | SRC-1, `src/secure_wiki/__main__.py` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | none | Import is not production |
| [RT-RTE-extraction-parsing](runtime.md#rt-rte-extraction-parsing) | content transformation | implemented | [EPI-OBJ-claim-text](#epi-obj-claim-text) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | Candidate statements only | see route | see route | SRC-1, `src/secure_wiki/extraction/extractor.py` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | Atomicity requested, not verified | Completions needed to distinguish reshaping, derivation and non-entailment |
| [RT-RTE-extraction-parsing](runtime.md#rt-rte-extraction-parsing) | check/evidence production | implemented | [EPI-OBJ-claim-metadata](#epi-obj-claim-metadata) | no content change | Envelope correspondence/parse shape | see route | see route | see route | see route | No factual license from nonce echo | see route | see route | SRC-1, `src/secure_wiki/extraction/extractor.py` | [RT-CLM-security-boundary](runtime.md#rt-clm-security-boundary) | Uniform nonce verification unsupported | Legacy and linewise outputs remain admissible to later checks |
| [EPI-RTE-security-checks](#epi-rte-security-checks) | check/evidence production | implemented | [EPI-OBJ-source-text](#epi-obj-source-text), [EPI-OBJ-review-result](#epi-obj-review-result), [EPI-OBJ-claim-metadata](#epi-obj-claim-metadata) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/secure_wiki/gate/write_gate.py` | [RT-CLM-security-boundary](runtime.md#rt-clm-security-boundary) | Security/metadata checks are not truth checks | see record |
| [EPI-RTE-security-checks](#epi-rte-security-checks) | check/evidence production | implemented | [EPI-OBJ-claim-embeddings](#epi-obj-claim-embeddings) | no content change | see record: similarity target | see record: numerical domain | see record | see record | see record | see record | see record | see record | SRC-1, `src/secure_wiki/store/embedding_store.py` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | Similarity is not contradiction | see record |
| [EPI-RTE-gate-disposition](#epi-rte-gate-disposition) | disposition/acceptance | implemented | [EPI-OBJ-claim-text](#epi-obj-claim-text), [EPI-OBJ-claim-metadata](#epi-obj-claim-metadata) | non-truth-apt policy/content update: active status and gate history | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/secure_wiki/gate/write_gate.py` | [EPI-CLM-quality-evidence](#epi-clm-quality-evidence) | Operational admission, not factual acceptance | see record |
| [EPI-RTE-store-retention](#epi-rte-store-retention) | retention | implemented | [EPI-OBJ-claim-text](#epi-obj-claim-text), [EPI-OBJ-claim-metadata](#epi-obj-claim-metadata), [EPI-OBJ-claim-embeddings](#epi-obj-claim-embeddings) | no content change | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/secure_wiki/store/wiki_store.py` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | Retention is not acceptance | see record |
| [RT-RTE-context-query](runtime.md#rt-rte-context-query) | operational admission/selection/consumption | implemented | [EPI-OBJ-claim-metadata](#epi-obj-claim-metadata), [EPI-OBJ-claim-text](#epi-obj-claim-text) | no content change | see route | see route | see route | see route | see route | Requested evidence, not certified truth | see route | see [RT-BAP-query-evidence](runtime.md#rt-bap-query-evidence) | SRC-1, `src/secure_wiki/read/hygiene.py` | [EPI-CLM-quality-evidence](#epi-clm-quality-evidence) | Pending option versus default active selection | Loaded labels, not admission attestations |
| [EPI-RTE-text-render](#epi-rte-text-render) | content transformation | implemented | [EPI-OBJ-claim-text](#epi-obj-claim-text) | truth-apt transformation: indeterminate | see record | see record | see record | see record | see record | see record | see record | see record | SRC-1, `src/secure_wiki/prompts.py` | [EPI-CLM-quality-evidence](#epi-clm-quality-evidence) | Token removal can change semantic content | see concrete deduction in record |
| [RT-RTE-context-query](runtime.md#rt-rte-context-query) | content transformation | implemented | [EPI-OBJ-query-answer](#epi-obj-query-answer) | truth-apt transformation: indeterminate | see route | see route | see route | see route | see route | Citation/abstention requested, no answer check | see route | see [RT-BAP-prompt-policy](runtime.md#rt-bap-prompt-policy) | SRC-1, `src/secure_wiki/__main__.py` | [EPI-CLM-quality-evidence](#epi-clm-quality-evidence) | No generated answer available | No basis to classify actual synthesis as entailed or ampliative |
| [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance) | lineage/freshness/recovery | implemented | [EPI-OBJ-claim-text](#epi-obj-claim-text), [EPI-OBJ-claim-metadata](#epi-obj-claim-metadata) | non-truth-apt policy/content update: operator deletion/reset/configuration | see route | see route | see route | see route | see route | Withdrawal/configuration, not falsification judgment | see route | see route | SRC-1, `src/secure_wiki/__main__.py` | [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | Reset may erase history; open query keeps snapshot | No automatic semantic supersession |

No lifecycle-integration route after factual acceptance was found in the inspected driver, gate, store, models, hygiene and prompt builders (SRC-1, paths in coverage). The `supersedes` field and status enum are serializable metadata, not a driver-operated revision link or evidence-consuming acceptance decision. This bounded absence does not deny operational integration: saved statements and vectors do change later input selection and comparison. Nor does it turn security admission into product failure.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-security-boundary](runtime.md#rt-clm-security-boundary) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-extraction-parsing](runtime.md#rt-rte-extraction-parsing), [EPI-RTE-security-checks](#epi-rte-security-checks), [EPI-RTE-gate-disposition](#epi-rte-gate-disposition), [RT-RTE-context-query](runtime.md#rt-rte-context-query) | None registered | No causal experiment; defaults/separate contexts do not enforce independent weights | Multiple barriers are wired | Nonce compatibility paths, direct writes, pending inclusion and model compliance bound universal language; none demonstrates a live exploit |
| [EPI-CLM-compiled-knowledge](#epi-clm-compiled-knowledge) | see record | SRC-1, `README.md`; doctrine/design | see record | [RT-RTE-extraction-parsing](runtime.md#rt-rte-extraction-parsing), [EPI-RTE-store-retention](#epi-rte-store-retention), [RT-RTE-context-query](runtime.md#rt-rte-context-query) | None registered | No comparison to RAG, no knowledge-quality or causal benefit measurement | Persistent source-derived candidates can replace raw documents as query input | Linking/curation rhetoric exceeds evidence of semantic integration or factual acceptance |
| [EPI-CLM-quality-evidence](#epi-clm-quality-evidence) | see record | SRC-1, `src/secure_wiki/prompts.py`; doctrine/design | see record | [EPI-RTE-gate-disposition](#epi-rte-gate-disposition), [EPI-RTE-text-render](#epi-rte-text-render), [RT-RTE-context-query](runtime.md#rt-rte-context-query) | None registered | Security reviewer expressly excludes truth; no answer oracle | Evidence-labelled delivery is wired | No demonstrated license for general factual reliability or obeyed citation/abstention |

## Bounded conclusion

- **Acquisition and production differ.** The application imports source text, preserves a URI and hash of transformed/truncated input, and requests atomic statements. It does not establish source truth or proposition-level support. Extraction and query generation are implemented model calls; without outputs their semantic relations remain indeterminate, not proven entailment or conjecture ([EPI-OBJ-source-text](#epi-obj-source-text), [RT-RTE-extraction-parsing](runtime.md#rt-rte-extraction-parsing), [EPI-OBJ-query-answer](#epi-obj-query-answer)).
- **Checks have real but narrow force.** Pattern flags, metadata completeness, trust labels, review verdict and similarity/section rules change dispositions. The reviewer targets manipulation, not factual accuracy. Cosine thresholds license numeric similarity classifications under supplied vectors, not contradiction or source truth. All-gates success licenses CLI storage and active status; no evidence-consuming decision against a factual criterion for an intended truth-dependent use was found in these checks ([EPI-RTE-security-checks](#epi-rte-security-checks), [EPI-RTE-gate-disposition](#epi-rte-gate-disposition)).
- **Retention supports later reliance without establishing acceptance.** Page text, symbolic labels/history and separate numerical vectors are retained. Trusted active text informs later security review; vectors influence later admission; selected trusted/semi-trusted pages feed query context. Context instructions call these evidence and request citations/abstention. Delivery is wired, obedience and benefit unobserved. Quarantine instead reaches listing/manual handling, not the ordinary query loader ([EPI-RTE-store-retention](#epi-rte-store-retention), [RT-BAP-query-evidence](runtime.md#rt-bap-query-evidence)).
- **Consumer-visible content is not necessarily the stored proposition.** Trust-marker stripping is deterministic but not universally meaning-preserving. Pending inclusion and direct storage show that later eligibility is a metadata decision, not proof that every delivered proposition passed ordinary ingestion. Deletion changes later loads but does not retract already-loaded session evidence ([EPI-RTE-text-render](#epi-rte-text-render), [RT-RTE-context-query](runtime.md#rt-rte-context-query), [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance)).
- **Other properties remain independent.** Retained source-derived context can influence later calls; that alone establishes neither improved future capacity nor reflection or theory criticism. The inspected routes do not expose a model-weight update or an evaluation-fed rewrite of the shipped policy. Operator configuration changes future behavior but is not an automatic evidence-responsive adaptation. External parametric internals remain uninspected. No actual formulated explanatory theory or criticized revision is supplied from which to assess a theory-building episode; security review is not substituted for that evidence ([RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model), [RT-CMP-review-model](runtime.md#rt-cmp-review-model), [RT-CMP-embed-model](runtime.md#rt-cmp-embed-model), [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance)).

## Shared records

### Operative objects

#### EPI-OBJ-source-text
Label: Source text

Part of: [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

This object is the input material of that broader route, not another invocation route. Source-native identity: `_read_source` result `source_text`. Natural-language text in process memory, potentially containing truth-apt statements and directives; no actual proposition instance is supplied. Claimed role: evidence for extraction and security review. SRC-1, `src/secure_wiki/__main__.py`: HTTP HTML loses skipped elements, PDFs are converted by pypdf, local non-PDF files are read directly, and all are truncated to 8,000 characters. Source URI is retained; source warrant is unknown, and completeness/qualification preservation is not guaranteed. Hashes cover this resulting string after whitespace normalization, not the full original. Sanitizer cleaned text is not the CLI's extraction/review input, as shown by [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission). No counterpart object in the supplied runtime; this is its source-input part.

> return text[:_MAX_CHARS], f"file://{path.resolve()}"
> --- `src/secure_wiki/__main__.py`

#### EPI-OBJ-claim-text
Label: Claim text

Part of: [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

Source-native identity: `Claim.text`; natural-language candidate statement, in process memory then YAML-frontmatter Markdown in pages or quarantine. This is the retained content part of the supplied route, not its admission procedure. Claimed role: atomic verifiable source statement; actual faithfulness, truth and atomicity are not checked by construction. No concrete retained instance is supplied. The parser copies `item["text"]` and caller provenance/trust without a proposition-to-source alignment. See the passage in [RT-RTE-extraction-parsing](runtime.md#rt-rte-extraction-parsing); SRC-1, `src/secure_wiki/extraction/extractor.py`. Text feeds embeddings, review, listings and selected context. Serialization/reload evidence is in [EPI-RTE-store-retention](#epi-rte-store-retention). Distinct from symbolic claim metadata and numerical embeddings.

#### EPI-OBJ-claim-metadata
Label: Claim metadata

Part of: [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

Source-native identities: `SourceRef`, `Claim.trust_level`, `status`, `gates_passed`, UUID, timestamp, `supersedes`, `review_notes`. Symbolic units in dataclass memory and serialized YAML. Review notes are natural-language diagnostic text retained alongside them; they are not the factual claim or policy consumed by the query prompt. This object is the control/lineage part of the supplied ingestion route. Claimed roles: source attribution, lifecycle status and gate trace. Metadata can state truth-apt provenance assertions, but its completeness does not authenticate those assertions. Trust is URI-rule/operator assignment; ordinary extraction copies one source reference, not an implemented multi-source weakest-trust derivation. `weakest` is an available helper. Read selection trusts deserialized labels; the CLI never independently proves them. SRC-1, `src/secure_wiki/models.py`, `src/secure_wiki/trust/tiering.py`, `src/secure_wiki/read/hygiene.py`.

> status: ClaimStatus = ClaimStatus.PENDING
> gates_passed: list[str] = field(default_factory=list)
> supersedes: Optional[str] = None
> review_notes: Optional[str] = None
> --- `src/secure_wiki/models.py`

#### EPI-OBJ-review-result
Label: Review result

Part of: [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

Source-native identity: `ReviewResult(passed, reasons)`, a transient symbolic Boolean plus natural-language reasons in process memory. Proposed manipulation findings may be truth-apt over the reviewed batch, but no actual review result is supplied. Claimed role: security veto, explicitly not factual verification. This is the decision-evidence part of the supplied route, distinct from claim text. Passing results need not retain reasons; failing reasons can become `review_notes` through gate 4. No full review conversation is persisted. SRC-1, `src/secure_wiki/review/adversarial.py`, `src/secure_wiki/gate/write_gate.py`.

> passed = parsed.get("verdict") == "pass"
> reasons = parsed.get("reasons", [])
> return ReviewResult(passed=passed, reasons=reasons)
> --- `src/secure_wiki/review/adversarial.py`

The governing review-domain passage is already retained in [RT-OBJ-system-prompts](runtime.md#rt-obj-system-prompts).

#### EPI-OBJ-claim-embeddings
Label: Claim embeddings

Part of: [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

Source-native identity: `new_embeddings` and `EmbeddingStore` values keyed by claim UUID. Dense numerical, distributed representations in memory and `embeddings/<claim_id>.json`, distinct from the external parameter component [RT-CMP-embed-model](runtime.md#rt-cmp-embed-model). They do not individuate a truth-apt proposition independently of text; claimed role is duplicate/conflict comparison. No stored model/version marker or input-text hash accompanies the vectors; lineage compatibility after model changes is unknown. All readable JSON vectors are loaded, and gate comparison does not join status/trust/text before selecting the highest similarity. SRC-1, `src/secure_wiki/store/embedding_store.py`, `src/secure_wiki/gate/write_gate.py`.

> path.write_text(json.dumps({"claim_id": claim_id, "embedding": embedding}), encoding="utf-8")
> --- `src/secure_wiki/store/embedding_store.py`

#### EPI-OBJ-query-answer
Label: Query answer

Part of: [RT-RTE-context-query](runtime.md#rt-rte-context-query)

Source-native identity: text chunks from `client.stream(system, question)`. Natural-language answer in provider response/process/stdout, not retained wiki state. Claimed role: answer grounded only in selected context, with URI citations and abstention on insufficient evidence. It may contain truth-apt statements, but none is supplied. This is the output material part of the supplied query route, not a duplicate route or retained claim. The query consumer prints chunks without an independent factual, entailment or citation check. SRC-1, `src/secure_wiki/__main__.py`, `src/secure_wiki/prompts.py`; task passage in [RT-OBJ-system-prompts](runtime.md#rt-obj-system-prompts).

> else:
>     print(chunk, end="", flush=True)
> --- `src/secure_wiki/__main__.py`

### Routes

#### EPI-RTE-security-checks
Label: Security checks

Part of: [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

Endpoints: raw source/proposed claims/labels/existing state → flags, review Boolean/reasons, comparison scores and branch conditions. This is the checking part, distinct from disposition and persistence. Python sequences checks; the review model interprets source-derived text in a fresh context. Evidence: SRC-1, `src/secure_wiki/ingestion/sanitizer.py`, `src/secure_wiki/review/adversarial.py`, `src/secure_wiki/gate/write_gate.py`, `src/secure_wiki/store/embedding_store.py`, `src/secure_wiki/prompts.py`.

Separate targets/domains and consumers:

1. Sanitizer tests the input string against enumerated Unicode/control/hidden-text/base64/instruction patterns. Flags are diagnostics for gate 1. The cleaned string has no CLI model-input force; detection does not establish absence of other manipulation.
2. Provenance completeness tests truthiness of id/URI/hash, not authenticity, source accuracy or support for the particular proposition. URI rules and operator override assign trust rather than measure truth.
3. Review evaluates manipulation in proposed text, originating truncated source and existing active trusted text. The builder strips marker tokens from proposed/existing bodies and omits their trust labels. Despite the prompt's low-trust-overwrite criterion, the reviewer does not receive each proposed claim's trust enum. The model returns a batch veto, not per-proposition factual support. Exact `pass` plus nonce correspondence is parsed; malformed JSON/nonce mismatch retries three total calls, then returns a failed result. Model correctness is not verified by nonce correspondence.
4. Consistency evaluates cosine similarity over supplied vectors. Numeric scores at default .95/.85 thresholds classify duplicate/escalation branches; they do not determine logical contradiction, shared referent or equivalence. Zero magnitudes yield zero similarity; unequal dimensions are not rejected (`zip` truncates the dot product while magnitudes use complete vectors). Without vectors the target is matching section and differing source ID among existing trusted claims. That is a symbolic heuristic, not semantic falsification.

The batch reviewer can veto all proposals from a source. Python checks can veto individual claims; operator starts ingestion and assigns source trust, not per-claim factual approval. Answer oracle: none for truth or manipulation; the model's judgment is not an independent reference outcome. Operating mode: open source ingestion, not bounded experiment/curriculum. These checks produce operative results only through [EPI-RTE-gate-disposition](#epi-rte-gate-disposition).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: flags, `ReviewResult`, and internal gate comparison/metadata conditions.
- Later read-back: failed review reasons and passed-gate labels may persist with claim metadata; existing active trusted text and retained vectors are inputs to future checks, not retained full evaluator conversations.
- Delegated visibility: reviewer sees source and marker-stripped proposed/existing text in separate nonce blocks; embedding provider sees claim text; no provider gets storage-write authority.
- Selection predicate: sanitizer scans source; reviewer gets the whole source batch and active trusted existing text; consistency compares all supplied vector IDs or the same-section/different-source fallback.
- Invalidation or expiry: per-call review/flags have no timer; later ingestions recompute them. Persisted vectors lack model-version invalidation.
- Activation or effect: check results are consumed by gate branches; actual detection accuracy or changed model behavior is unobserved.
- Evidence limits: no source truth check, live review trace, independent reference outcome or measured embedding validity. Direct gate callers can supply `ReviewResult` or omit source context through fallback, as traced in the parent runtime account.

> if sanitize_report.flags:
>     return GateOutcome(
>         decision=GateDecision.QUARANTINE,
>         claim=claim,
>         detail=f"sanitizing: {', '.join(sanitize_report.flags)}",
>     )
> --- `src/secure_wiki/gate/write_gate.py`

> if c.source.section == claim.source.section and c.source.id != claim.source.id
> --- `src/secure_wiki/gate/write_gate.py`

> dot = sum(x * y for x, y in zip(a, b))
> mag_a = sum(x * x for x in a) ** 0.5
> mag_b = sum(x * x for x in b) ** 0.5
> --- `src/secure_wiki/store/embedding_store.py`

Countercase to similarity-as-contradiction: identical nonzero vectors have cosine 1 and take the duplicate branch; no claim negation is examined. Likewise two unrelated propositions in the same default section can trigger fallback escalation. These deductions use implementation only, not target execution.

#### EPI-RTE-gate-disposition
Label: Gate disposition

Part of: [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

Endpoints: check conditions and proposed claim → `GateOutcome` and status/history mutation → driver save selection. This is the disposition part of the supplied route, not another checker or persistence path. Python owns decisions; extraction proposes, reviewer can veto, software can quarantine/escalate; the operator is not asked to approve individual claim content. Trigger: ingestion of source-derived knowledge proposals. Guidance: five gate rules plus extraction/security prompts, not an independent factual answer oracle. Mode: open operator-selected source compilation. Criterion for operational admission: no sanitize flags; populated provenance; not untrusted in the presence of active trusted claims; passed review; no threshold/fallback conflict. Intended use: active retained candidates, eligible for later reads under their labels. Scope: these code rules with supplied state, not general truth or reliable manipulation detection. The recorded gate history is evidence of branch passage, not an evidence-consuming factual acceptance decision.

SRC-1, `src/secure_wiki/gate/write_gate.py`, `src/secure_wiki/__main__.py`. The active/commit passage is retained in [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission). Ordinary driver consequences are enforcing: commit saves to pages; quarantine and escalation both save as quarantined. “Human review required” has no subsequent approval consumer in this dispatch. Rejection exists, but a later human acceptance or promotion route is not wired here. Withdrawal/recovery uses operator deletion/reset or manual Git reversal where history survives, not automatic semantic correction.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: commit, quarantine or escalate with claim and detail; successful gate sets active status.
- Later read-back: passed labels, status and failure notes persist through the store; later selection consumes current metadata rather than a cryptographic gate attestation.
- Delegated visibility: inapplicable — disposition itself is Python; model review is the separate checking function.
- Selection predicate: ordered fail-fast branches; all five successful checks required for ordinary CLI commit.
- Invalidation or expiry: no expiry/reverification of active decisions; explicit operator removal or local editing can change state.
- Activation or effect: driver consumes the decision to select pages versus quarantine and update in-process existing claims/vectors. Query eligibility is another decision.
- Evidence limits: no factual acceptance criterion, observed successful admission or demonstrated downstream correctness; direct `save_claim` is not governed by this mechanism.

> else:
>     store.save_quarantined(claim, outcome.detail)
>     escalated += 1
>     print(f"{label} ESCALATE    {outcome.detail}")
> --- `src/secure_wiki/__main__.py`

#### EPI-RTE-store-retention
Label: Store retention

Endpoints: supplied claim/vector → Markdown/YAML and embedding JSON → later reload. Distinct lower-level persistence function spanning [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) and [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance), not a duplicate of either route: it is also callable without their CLI decisions. Python storage methods write under the local user's authority. Serialization preserves the claim dictionary and duplicates text in the body; deserialization reads frontmatter only, so editing only the Markdown body does not revise the loaded claim. No factual checking occurs during save or reload. Successful saves synchronously commit claim files to Git; file writes precede Git, and embeddings are saved separately after a successful CLI claim save. Failure may leave partial state. SRC-1, `src/secure_wiki/store/wiki_store.py`, `src/secure_wiki/store/embedding_store.py`, `src/secure_wiki/__main__.py`.

Admission at this API boundary is caller invocation, not gate approval; the gate parent describes the normal CLI approval. Supplied status may remain pending in pages. Local edits/storage bypass do not establish a remote attack surface. Stored source text is not independently preserved as a source snapshot by these methods; retained URI/hash is weaker than proposition-support evidence. Quarantined claims and reasons persist for operator listing, not query consumption. Retention is not lifecycle integration after factual acceptance.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: claim path or vector save completion; Git failures raise after file writes.
- Later read-back: pages feed future ingestion and context; active trusted text feeds review; vectors feed consistency; quarantine feeds listing/manual handling, not ordinary query context. Reload reconstructs from YAML, not the prose body.
- Delegated visibility: inapplicable — file serialization/reload invokes no model; later consumers are separate routes.
- Selection predicate: caller selects claim/path by UUID; directory reload skips unreadable/deserialization failures and optionally filters status; vector reload accepts readable JSON without reconciling claim labels or model versions.
- Invalidation or expiry: no age expiry; deletion/reset removes current files; history survives only where operator reset/deletion policy preserves it. No atomic rollback spans file, Git and vector writes.
- Activation or effect: later commands can deliver saved material to reviewer/gate/query consumers. Actual use, benefit and factual reliability are unobserved.
- Evidence limits: no frozen instance or history; a saved file alone would not establish that the gate produced it. No source-support verification or evidence-consuming factual acceptance in this lower-level API.

> raw = yaml.safe_load(parts[1])
> return Claim.from_dict(raw)
> --- `src/secure_wiki/store/wiki_store.py`

> claim.status = ClaimStatus.QUARANTINED
> path = self.quarantine / f"{claim.claim_id}.md"
> path.write_text(_serialize(claim, gate_detail), encoding="utf-8")
> --- `src/secure_wiki/store/wiki_store.py`

#### EPI-RTE-text-render
Label: Text rendering

Endpoints: stored/proposed claim text → marker-stripped prompt text → security reviewer or context/query model. Distinct cross-stage content transformation overlapping [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) and [RT-RTE-context-query](runtime.md#rt-rte-context-query); not identical to either container. Python applies `_safe_claim_text` in review/alternate context builders and `strip_trust_markers` in the actual loader. Natural-language text is transformed under fixed symbolic regex rules; no model judges semantic fidelity. SRC-1, `src/secure_wiki/prompts.py`, `src/secure_wiki/read/hygiene.py`.

Concrete source-only deduction: input `The token [T] denotes trusted.` passes the regex substitution with exactly `[T]` removed, yielding `The token  denotes trusted.` after edge whitespace stripping. `_format_claims` then prefixes the assigned trust symbol and appends URI/section/time/gates; it does not restore the mentioned token. `build_review_prompt` also strips that token from proposed/existing text. This is not universally non-ampliative reshaping: the term about which the sentence makes a claim has been removed. Remaining semantic classifications depend on actual input and interpretation. No target execution or claim of an observed instance is involved. A contrasting plain sentence containing none of `[T]`, `[S]`, `[U]` keeps its text, aside from edge whitespace. Thus the route is not uniformly meaning-changing either.

Consumer/force/horizon: review-model user block for each batch, or query-model system context for a session; code enforces literal token removal, while intended instruction resistance and evidential interpretation are advisory model instructions. The actual loader includes source URI and gate fields but does not display a separate pending-status warning in `_format_claims`. Strict alternate context builders exclude pending; actual loader admits them if requested. Marker removal cannot authenticate URI text or prevent every multiline semantic impersonation.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: rendered marker-stripped text in prompt/context strings.
- Later read-back: inapplicable — this transformation does not write the rendered text back to the store; later invocations render again from surviving stored claims.
- Delegated visibility: reviewer/query model receives transformed bodies rather than the exact stored text; source block in review still contains original truncated input.
- Selection predicate: literal regex matches `[T]`, `[S]`, `[U]` anywhere in claim text; loader trust/status filtering and alternate builder predicates precede contextual delivery.
- Invalidation or expiry: fresh rendering at each prompt/context build; query sessions retain the startup snapshot until exit, not until subsequent store deletion.
- Activation or effect: consumers receive transformed text; interpretation, faithful factual reliance and instruction resistance are unobserved.
- Evidence limits: deterministic token deletion is established; general semantic preservation, reliable injection prevention and any actual answer quality are not.

> _TRUST_MARKER_RE = re.compile(r"\[[TSU]\]")  # strip forged [T]/[S]/[U] tokens
> --- `src/secure_wiki/prompts.py`

> def strip_trust_markers(text: str) -> str:
>     """Public API: remove forged [T]/[S]/[U] tokens from source-derived text."""
>     return _TRUST_MARKER_RE.sub("", text).strip()
> --- `src/secure_wiki/prompts.py`

> lines.append(f"[{sym}] {strip_trust_markers(claim.text)}")
> lines.append(f"    source:    {claim.source.uri}")
> --- `src/secure_wiki/read/hygiene.py`

### Claims

#### EPI-CLM-compiled-knowledge
Label: Compiled knowledge

Claimed operation: persistent linked knowledge compilation and curation rather than repeatedly consulting raw documents. Distinct from the trust-boundary guarantee in [RT-CLM-security-boundary](runtime.md#rt-clm-security-boundary): this claim concerns the knowledge lifecycle and product. SRC-1, `README.md`, doctrine/design.

- claim conclusion status: claimed
- operation conclusion status: uninspected

> Instead of re-scanning raw documents on every query (classic RAG), an LLM maintains a persistent,
> linked Markdown wiki: knowledge is compiled once and then curated. The security challenge is the
> hard part — a crafted source must never reach the wiki persistently and poison later sessions.
> --- `README.md`

Support: persisted claims replace raw sources as query input. Limit: inspected storage maintains per-claim records, source references and optional supersession fields, not an automatic linked explanatory synthesis or demonstrated factual knowledge production. Candidate compilation and retention do not entail acceptance/integration.

#### EPI-CLM-quality-evidence
Label: High-quality evidence

Claimed warrant: selected wiki context should be treated as high-quality evidence, not instructions, and used exclusively with URI citations/abstention. SRC-1, `src/secure_wiki/prompts.py`, doctrine/design. Distinct from [RT-CLM-security-boundary](runtime.md#rt-clm-security-boundary), which concerns crossing a security boundary, and from [RT-OBJ-system-prompts](runtime.md#rt-obj-system-prompts), the actual policy artifact carrying this claim. The load-bearing passages are retained in [RT-BAP-query-evidence](runtime.md#rt-bap-query-evidence) and [RT-OBJ-system-prompts](runtime.md#rt-obj-system-prompts).

- claim conclusion status: claimed
- operation conclusion status: uninspected

Support: trust/status filtering and evidence-labelled delivery are implemented. Limit: security review explicitly does not judge truth; source trust and gate passage do not establish factual verification or source entailment. Citation and abstention are requests without an independent downstream check.
