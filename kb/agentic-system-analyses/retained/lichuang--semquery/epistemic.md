---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Semquery epistemic routes: document import, relevance selection, answer generation and the limited license of citation checks."
run-id: AAS-2026-11-09-semquery-b21559990932-01
reviewed-boundary: "0820927160b1400990fa8cc057807c73bbf6d025"
---

# Semquery epistemic report

## Source-and-claim boundary

The question is whether semquery's document-to-answer pipeline establishes truth or source support, rather than merely selecting passages and attaching references. Scope and exclusions are see [boundary](boundary.md#boundary-and-evidence); source identity and evidence layers are see [Source register](boundary.md#source-register). All source anchors below belong to SRC-1 at that frozen commit. No observed execution or causal experiment was supplied. External document truth, downloaded weights, dependency internals and downstream host decisions remain outside inspectable evidence. These gaps prevent certification of extraction fidelity, answer correctness, model compliance, benefit or improvement.

The runtime is a provisional baseline, not an inspection limit. Direct additional reads covered the complete citation parser, prompt builder, synthesizer (including inline test definitions), three reader implementations, and CLI dispatch and consumers. These are implementation evidence; test definitions are not passing test results. The relevant knowledge/warrant claims are [EPI-CLM-cited-answers](#epi-clm-cited-answers) and [RT-CLM-citation-filter](runtime.md#rt-clm-citation-filter). Transaction/freshness qualifications are see [RT-CLM-transaction-scope](runtime.md#rt-clm-transaction-scope) and [RT-RTE-index-admission](runtime.md#rt-rte-index-admission), not truth evaluators.

| Entry point or operation | Source path (SRC-1) | Coverage and records | Limit / conclusion prevented |
|---|---|---|---|
| init, status, removed index command | `crates/semquery/src/main.rs` | Direct dispatch/consumer read; status counts current stored objects; init initializes storage; index exits with migration hint | Operational metadata, not checks of corpus truth |
| add and library indexing | `crates/semquery/src/main.rs`, `crates/semquery-indexer/src/indexer.rs` | Direct CLI; supplied [RT-RTE-index-admission](runtime.md#rt-rte-index-admission); direct reader refinement [EPI-RTE-reader-import](#epi-rte-reader-import) | Indexer internals here rely on supplied runtime; no independent exhaustive extraction audit |
| delete collection/document, missing-file sweep | `crates/semquery/src/main.rs`, `crates/semquery/src/engine.rs`, `crates/semquery-indexer/src/indexer.rs` | Direct CLI delete dispatch; supplied [RT-RTE-index-admission](runtime.md#rt-rte-index-admission) | Removal from retrieval, not retraction after a falsity finding; shared chunks may remain |
| search and search_stream | `crates/semquery/src/main.rs`, `crates/semquery-retrieve/src/retriever.rs`, `crates/semquery-retrieve/src/fusion.rs` | Direct CLI consumer; supplied [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search) | Relevance scores do not certify entailment or truth |
| ask / ask_stream, direct Synthesizer | `crates/semquery-synth/src/synthesizer.rs`, `crates/semquery-synth/src/prompt.rs`, `crates/semquery-synth/src/citation.rs`, `crates/semquery/src/main.rs` | Direct implementation and consumer reads; [EPI-RTE-marker-check](#epi-rte-marker-check), [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation) | No run shows which propositions were generated; no per-proposition acceptance gate |
| GGUF context truncation and generation | `crates/semquery-model/src/gguf.rs` | Supplied [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation), [RT-CMP-gguf-llm](runtime.md#rt-cmp-gguf-llm) | Offered context and model-visible context may differ |
| configuration / injected trait implementations | `crates/semquery/src/engine.rs`, `crates/semquery/src/config.rs`, `crates/semquery-core/src/traits.rs` | Supplied [RT-RTE-config-admission](runtime.md#rt-rte-config-admission) | Custom implementations are opaque alternatives; default-adapter negatives are not universal host claims |

CLI dispatch exposes init/index/add/del/status/search/ask, not a model-driven tool or hook loop. The supplied runtime covers executable trait extension points; injected implementations are not evidence of an additional shipped epistemic evaluator. No system-complete negative about arbitrary injected code is asserted.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-document-source](#epi-obj-document-source) | Imported text may state propositions about the documents' subjects | Source material | SRC-1 `crates/semquery-indexer/src/reader/txt_reader.rs` | Source truth unknown; importing is not production or acceptance |
| [EPI-OBJ-prompt](#epi-obj-prompt) | Selected chunk text plus attribution; query/instructions are not themselves answers | Grounding context | SRC-1 `crates/semquery-synth/src/prompt.rs` | Selection and context truncation can omit qualifications |
| [EPI-OBJ-answer](#epi-obj-answer) | Generated answer text may assert propositions; actual content not determinable without an instance | User answer | SRC-1 `crates/semquery-synth/src/synthesizer.rs` | Generation alone does not establish entailment, non-entailment, truth or acceptance |
| [EPI-OBJ-citation](#epi-obj-citation) | Symbolic association of marker with offered file/range, not a judgment of sentence support | Answer provenance metadata | SRC-1 `crates/semquery-synth/src/citation.rs` | Byte offsets do not establish extraction fidelity or passage support |

Embedding and reranking numerical state are see [RT-CMP-fast-embed](runtime.md#rt-cmp-fast-embed) and [RT-CMP-fast-reranker](runtime.md#rt-cmp-fast-reranker). They supply retrieval representations and relevance judgments, not independently individuated claims about document subjects. Model parameter fixity, mutable resolution and uninspected internals are see those components and [RT-CMP-gguf-llm](runtime.md#rt-cmp-gguf-llm); no learning from weight changes is inferred.

## Authority-route ledger

Route ID: [EPI-RTE-reader-import](#epi-rte-reader-import)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-document-source](#epi-obj-document-source)
Content/update relation: truth-apt transformation: acquisition/import
Transition or check target: Files to extracted DocumentSource; source warrant unknown.
Evaluator/condition and domain: Reader eligibility, UTF-8 decoding, PDF extractor or DOCX XML extraction; these assess readability/extractability, not truth.
Activation and timing: During explicit indexing before chunk admission.
Possible or observed result: Imported text, skipped empty/invalid text, or parse error; implementation only.
Implemented force: Enforcing eligibility for indexing.
Epistemic authority and scope: Evidence of what extractor returned, not endorsement of document claims.
Operational authority: Readable material can enter automatic index admission.
Behavioral-authority path: Indexer receives DocumentSource through FileReader; enforcing eligibility for this indexing pass, with retained outputs reaching later retrieval.
Evidence source ID and local anchor: SRC-1 `crates/semquery-indexer/src/reader/docx_reader.rs`; see route evidence.
Claim IDs or none: [EPI-CLM-cited-answers](#epi-clm-cited-answers).
Mismatch marker or none: Citation ranges cannot alone establish faithful source interpretation.
Gap/limit: PDF dependency internals uninspected; DOCX text assembly can lose boundaries.

Route ID: [RT-RTE-index-admission](runtime.md#rt-rte-index-admission)
Route function: retention
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-document-source](#epi-obj-document-source)
Content/update relation: no content change
Transition or check target: Persistence of extracted/chunked material and retrieval representations, not acceptance of propositions.
Evaluator/condition and domain: see [RT-RTE-index-admission](runtime.md#rt-rte-index-admission).
Activation and timing: After extraction/chunking/embedding; batched transactions.
Possible or observed result: Committed searchable chunks; partial prior commits can survive later failure.
Implemented force: Storage admission, not a truth verdict.
Epistemic authority and scope: No added warrant for source truth.
Operational authority: Later search/ask may use retained chunks without per-claim approval.
Behavioral-authority path: Storage to Retriever to caller or model; permissive corpus availability across invocations, followed by ranking.
Evidence source ID and local anchor: SRC-1 `crates/semquery-indexer/src/indexer.rs`; evidence see [RT-RTE-index-admission](runtime.md#rt-rte-index-admission).
Claim IDs or none: [EPI-CLM-cited-answers](#epi-clm-cited-answers).
Mismatch marker or none: Retention is not lifecycle integration after acceptance.
Gap/limit: No acceptance decision is evidenced by this route. Recovery/freshness are see runtime; neither guarantees truth.

Route ID: [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search)
Route function: operational admission/selection/consumption
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-prompt](#epi-obj-prompt)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Query relevance of retained chunks; ordering and selecting existing texts, not checking their propositions.
Evaluator/condition and domain: Numerical recall, reciprocal-rank fusion, optional cross-encoder; see [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search).
Activation and timing: Each search; ask requests five hits.
Possible or observed result: Ranked hit list or error; no observed accuracy result.
Implemented force: Ranking and omission.
Epistemic authority and scope: Relevance estimate only; no truth, support or completeness license.
Operational authority: Determines which passages may influence this answer.
Behavioral-authority path: Retriever via hit list to Synthesizer or CLI; ranking force for one query.
Evidence source ID and local anchor: SRC-1 `crates/semquery-retrieve/src/retriever.rs`; see runtime route.
Claim IDs or none: [EPI-CLM-cited-answers](#epi-clm-cited-answers).
Mismatch marker or none: Relevant is not warranted.
Gap/limit: Scoring internals and quality unobserved; missing chunks omitted; custom reranking differs.

Route ID: [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-prompt](#epi-obj-prompt)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Hit texts to numbered context blocks, paths/ranges, query and grounding instruction.
Evaluator/condition and domain: Deterministic formatting in build_ask_prompt, not a factual evaluator.
Activation and timing: After nonempty retrieval, before LLM call.
Possible or observed result: Prompt string.
Implemented force: Supplies model input; no acceptance.
Epistemic authority and scope: Preserves offered hit text in prompt construction, not full-document context or actual model visibility.
Operational authority: Model receives selected textual material subject to adapter token budget.
Behavioral-authority path: Synthesizer user-message construction to GGUF; advisory natural-language force, one generation; see [RT-BAP-prompt-influence](runtime.md#rt-bap-prompt-influence).
Evidence source ID and local anchor: SRC-1 `crates/semquery-synth/src/prompt.rs`; see [EPI-OBJ-prompt](#epi-obj-prompt).
Claim IDs or none: [EPI-CLM-cited-answers](#epi-clm-cited-answers).
Mismatch marker or none: none.
Gap/limit: Supplied runtime's GGUF tail truncation is a countercase to all offered context reaching inference.

Route ID: [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation)
Route function: content transformation
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-answer](#epi-obj-answer)
Content/update relation: truth-apt transformation: indeterminate
Transition or check target: Prompt to model-generated text; neither entailment nor non-entailment established for an unsupplied instance.
Evaluator/condition and domain: LLM generation guided by grounding instruction; no independent factual evaluator in inspected synthesis.
Activation and timing: Nonempty hits; direct or streaming completion.
Possible or observed result: Raw answer or error; no-hit empty answer is an implemented counterpath to generation.
Implemented force: Returns generated text without factual admission check.
Epistemic authority and scope: Candidate answer only. It might repeat, infer from, or exceed supplied material; deciding requires an answer and its actual inputs.
Operational authority: CLI displays tokens before marker checking; JSON/API returns raw text with filtered metadata.
Behavioral-authority path: LLM through Token/AnswerComplete or Answer to user/caller; advisory answer content, one call; no inspected answer write-back.
Evidence source ID and local anchor: SRC-1 `crates/semquery-synth/src/synthesizer.rs`, `crates/semquery/src/main.rs`; see [EPI-OBJ-answer](#epi-obj-answer) and runtime route.
Claim IDs or none: [EPI-CLM-cited-answers](#epi-clm-cited-answers).
Mismatch marker or none: Prompt compliance is requested, not enforced.
Gap/limit: No observed answer supports accepted ampliative production or checked derivation from warranted premises.

Route ID: [EPI-RTE-marker-check](#epi-rte-marker-check)
Route function: check/evidence production
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-citation](#epi-obj-citation)
Content/update relation: no content change
Transition or check target: Numeric marker membership in pre-generation offered-hit marker set and uniqueness.
Evaluator/condition and domain: Regex, HashSet membership and deduplication; exact textual marker domain.
Activation and timing: After raw completion, after tokens may already have escaped.
Possible or observed result: Ordered valid-marker vector; not a support score.
Implemented force: Metadata filtering; no block on raw answer.
Epistemic authority and scope: Marker belongs to offered set; not that sentence follows from passage or passage reached inference.
Operational authority: Only retained markers proceed to citation backfill.
Behavioral-authority path: Parser return to Synthesizer citation builder; enforcing metadata selection, one answer.
Evidence source ID and local anchor: SRC-1 `crates/semquery-synth/src/citation.rs`; see route evidence.
Claim IDs or none: [RT-CLM-citation-filter](runtime.md#rt-clm-citation-filter).
Mismatch marker or none: Valid citation syntax is narrower than grounded assertion.
Gap/limit: No proposition-level reference outcome, source truth or entailment evaluator.

Route ID: [EPI-RTE-marker-check](#epi-rte-marker-check)
Route function: disposition/acceptance
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-citation](#epi-obj-citation)
Content/update relation: truth-apt transformation: non-ampliative reshaping
Transition or check target: Valid-marker result to selected hit path/range metadata.
Evaluator/condition and domain: Code parses marker number and indexes hits; see route record. This is metadata disposition, not epistemic acceptance of an answer.
Activation and timing: After marker checking, before Answer return / AnswerComplete.
Possible or observed result: Citation entries for valid offered markers only, alongside unchanged raw answer.
Implemented force: Enforcing citation-vector membership.
Epistemic authority and scope: Attribution to an offered hit; no sentence-support license.
Operational authority: Excluded markers have no Citation entry but may remain displayed in answer text.
Behavioral-authority path: Synthesizer via citations vector to CLI Sources/JSON or library caller; permissive source navigation for returned answer.
Evidence source ID and local anchor: SRC-1 `crates/semquery-synth/src/synthesizer.rs`; see [RT-CLM-citation-filter](runtime.md#rt-clm-citation-filter).
Claim IDs or none: [RT-CLM-citation-filter](runtime.md#rt-clm-citation-filter).
Mismatch marker or none: No accepted proposition is established by metadata admission.
Gap/limit: No separate evidence-consuming acceptance decision for intended answer truth/support was found in inspected synthesis or CLI consumers.

Route ID: [RT-RTE-index-admission](runtime.md#rt-rte-index-admission)
Route function: lineage/freshness/recovery
Architectural status: implemented
Object/candidate ID: [EPI-OBJ-document-source](#epi-obj-document-source)
Content/update relation: no content change
Transition or check target: Changed/missing documents, config drift, explicit deletion; these govern continued availability rather than falsity.
Evaluator/condition and domain: Hash/config comparisons and user/caller deletion; see runtime route.
Activation and timing: Explicit maintenance; search/ask do not enforce reindex first.
Possible or observed result: Skip, replace, sweep or delete indexed material; errors and partial previous commits remain possible.
Implemented force: Enforcing index membership on covered maintenance paths.
Epistemic authority and scope: Freshness/identity bookkeeping, not endorsement or withdrawal of a false claim.
Operational authority: Changes later retrieval corpus, with shared-chunk and canonicalization limits in runtime.
Behavioral-authority path: Indexer/Engine storage mutations to later Retriever reads; enforcing corpus availability across calls.
Evidence source ID and local anchor: SRC-1 `crates/semquery-indexer/src/indexer.rs`, `crates/semquery/src/main.rs`; see runtime route.
Claim IDs or none: [RT-CLM-transaction-scope](runtime.md#rt-clm-transaction-scope).
Mismatch marker or none: No global freshness barrier.
Gap/limit: Not an epistemic rejection loop or acceptance-following integration mechanism.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [EPI-CLM-cited-answers](#epi-clm-cited-answers) | Search/ask with cited answers | SRC-1 `README.md`, doctrine/design | see claim | [RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search), [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation), [EPI-RTE-marker-check](#epi-rte-marker-check) | None supplied | No comparison; generation/metadata wiring does not prove grounded truth | Implemented source-linked answer interface | Broader reading as factual validation unsupported; citation list can be empty |
| [RT-CLM-citation-filter](runtime.md#rt-clm-citation-filter) | Invalid markers silently dropped | SRC-1 `crates/semquery-synth/src/synthesizer.rs`, doctrine/design and implementation | see claim | [EPI-RTE-marker-check](#epi-rte-marker-check) | None supplied | Exact membership domain only; no entailment check | Invalid markers excluded from metadata | Raw text is unchanged; streaming exposes text first |

## Bounded conclusion

Semquery acquires document text and retains retrieval material for later search and question answering; it does not thereby produce or accept the imported claims. Source warrant is unknown. Plain UTF-8 reading preserves the loaded string, whereas PDF extraction depends on uninspected dependency behavior and DOCX assembly has a concrete boundary-loss countercase. The import route therefore cannot certify general semantic preservation ([EPI-RTE-reader-import](#epi-rte-reader-import)).

Retrieval selects and reorders existing chunks. Prompt construction copies selected text into numbered context blocks, but the concrete GGUF adapter can truncate their beginning. Neither relevance ranking nor offered marker membership establishes that a proposition is true, supported, or even drawn from a passage the model actually received ([RT-RTE-hybrid-search](runtime.md#rt-rte-hybrid-search), [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation)).

The answer route implements candidate generation, not observed production of accepted ampliative claims. With no actual answer and actual model input, whether a generated proposition is entailed, ampliative, or merely repeated is not determinable. Citation checking has a precise implemented target and real consumer: exact marker membership controls the returned citation vector. This is operative metadata selection, not evidence-consuming acceptance of an answer against a truth/support criterion. Raw answer text escapes unchanged, and streamed tokens can escape before the check ([EPI-RTE-marker-check](#epi-rte-marker-check), [EPI-OBJ-answer](#epi-obj-answer)).

No lifecycle integration after epistemic acceptance is established in inspected synthesis/CLI or supplied index/search routes. Retained source material is operationally usable without that acceptance. Deletion and hash/config maintenance change availability, not reliance in response to a claim-specific refutation. Configured prompts can shape later behavior through external edits and reload, but [RT-RTE-config-admission](runtime.md#rt-rte-config-admission) establishes no automatic evaluation-fed policy adaptation. These are bounded route findings, not a negative about arbitrary injected components or inaccessible model cognition. No exercised learning, reflection, autonomy or self-improvement follows from citation generation, retention or fixed inference weights; none is inferred from another. Missing run and comparison evidence independently prevents claims of factual success, benefit or causal improvement.

## Shared records

### Operative objects

#### EPI-OBJ-document-source
Label: DocumentSource

Distinct referent relative to supplied runtime routes (which declare no operative objects): extracted text passed from readers into indexing, not the route that later persists it. SRC-1 `crates/semquery-indexer/src/reader/txt_reader.rs`, `crates/semquery-indexer/src/reader/docx_reader.rs`. Natural-language content in Rust String and PathBuf during indexing; inputs reside in files and derived chunks later reside in workspace storage through [RT-RTE-index-admission](runtime.md#rt-rte-index-admission). Actual propositions and source warrant depend on user files, which are not supplied.

> Ok(Some(DocumentSource {
>             path: path.to_path_buf(),
>             content,
>           }))
> --- `crates/semquery-indexer/src/reader/txt_reader.rs`

#### EPI-OBJ-prompt
Label: build_ask_prompt output

Distinct object from the supplied [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation) route: its transient string input to inference. Natural-language chunk texts/instructions with symbolic marker/path/range formatting, stored in a per-call Rust String. No independent prompt archive/read-back route is shown. SRC-1 `crates/semquery-synth/src/prompt.rs`.

> "[{}] {} (bytes {}-{}):\n{}\n\n",
>       marker,
>       hit.file_path.display(),
>       chunk.byte_range.start,
>       chunk.byte_range.end,
>       chunk.text
> --- `crates/semquery-synth/src/prompt.rs`

A concrete formatting deduction: one hit with text `Earth is round.`, path `a.txt`, range `0..15` becomes `[1] a.txt (bytes 0-15):` followed by the same text. This adds an address, not a proof of the sentence. The grounding request is quoted in [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation).

#### EPI-OBJ-answer
Label: Answer.text

Distinct material part from citation metadata below; the supplied [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation) is a process, not a duplicate object. Natural-language raw completion in a Rust String, plus token deltas in channels and CLI buffers; returned/displayed, not retained as future indexed knowledge by inspected synthesis. SRC-1 `crates/semquery-synth/src/synthesizer.rs`, `crates/semquery/src/main.rs`.

> Ok(Answer { text: raw, citations })
> --- `crates/semquery-synth/src/synthesizer.rs`

> AskEvent::Token { delta } => {
>         if !json {
>           print!("{delta}");
> --- `crates/semquery/src/main.rs`

#### EPI-OBJ-citation
Label: Answer.citations

Distinct symbolic metadata part rather than raw answer language or a duplicate of [RT-CLM-citation-filter](runtime.md#rt-clm-citation-filter). Rust Vec of Citation structures carrying markers and source strings; transient result/channel and displayed Sources or JSON, with no inspected future-answer reload. Fixed parser/indexing rules consume markers. SRC-1 `crates/semquery-synth/src/synthesizer.rs`; backfill source includes path and chunk byte range, not a sentence-support judgment.

> Some(Citation {
>           marker,
>           source: format!(
>             "{} (bytes {}-{})",
>             hit.file_path.display(),
>             chunk.byte_range.start,
>             chunk.byte_range.end
>           ),
>         })
> --- `crates/semquery-synth/src/synthesizer.rs:90-119`

### Routes

#### EPI-RTE-reader-import
Label: FileReader extraction
Part of: [RT-RTE-index-admission](runtime.md#rt-rte-index-admission)

Endpoints: filesystem bytes to optional DocumentSource text. Owner: reader implementations selected by registry. This is the extraction stage inside index admission, not a competing index route. SRC-1 `crates/semquery-indexer/src/reader/txt_reader.rs`, `crates/semquery-indexer/src/reader/pdf_reader.rs`, `crates/semquery-indexer/src/reader/docx_reader.rs`. Plain text uses read_to_string; invalid UTF-8/empty content is skipped. PDF uses pdf_extract; DOCX reads word/document.xml and concatenates selected XML text. Software extraction proposes the text; no human review of each extracted proposition, no truth oracle or model factual veto is invoked. Operating mode: explicit document indexing.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Optional extracted DocumentSource or parse/I/O error.
- Later read-back: Extracted material feeds chunk/index persistence for later retrieval through the parent route; no separate reader memory.
- Delegated visibility: inapplicable — no delegated task owner; PDF/XML parsers receive input bytes/text.
- Selection predicate: Dispatched reader extension and readable nonempty text; text reader skips invalid UTF-8.
- Invalidation or expiry: inapplicable — reader holds no durable version; the parent route owns hash/config maintenance.
- Activation or effect: Successful extraction admits candidate content into automatic indexing; no measured fidelity supplied.
- Evidence limits: Source inspection only; dependency internals and user files not supplied. Extraction may remove structure and change interpretation.

> let text = pdf_extract::extract_text_from_mem(&bytes).map_err(|e| ParseError::ExtractFailed {
> --- `crates/semquery-indexer/src/reader/pdf_reader.rs`

> b"w:t" => in_text_node = true,
>         b"w:tab" => text.push('\t'),
>         b"w:br" => text.push('\n'),
>         _ => {}
> --- `crates/semquery-indexer/src/reader/docx_reader.rs`

> text.push_str(&chunk);
> --- `crates/semquery-indexer/src/reader/docx_reader.rs`

Concrete implementation deduction, not target execution: `<w:p><w:r><w:t>not</w:t></w:r></w:p><w:p><w:r><w:t>true</w:t></w:r></w:p>` produces `nottrue`. Start/end paragraph events insert no separator; each text node appends its characters. This falsifies a universal claim that the DOCX extraction preserves word/paragraph boundaries. It does not establish that a particular user's claim changed truth value. Even before chunking, citation addresses are addresses into extracted material, not an independent fidelity check of the original document layout.

#### EPI-RTE-marker-check
Label: parse_citations and citation backfill
Part of: [RT-RTE-answer-generation](runtime.md#rt-rte-answer-generation)

This is the material check/disposition stage of the supplied answer route, not a second whole generation route. Endpoints: raw completion and valid offered marker list to selected markers and Citation metadata. Owner: regex/membership code then Synthesizer. No human per-answer approval; code can veto metadata entries only. No reference-answer oracle; offered marker set is the exact expected membership domain, not expected factual answer. Operating mode: open query answering. Invalid entries are omitted; raw text is neither revised nor rolled back. Guidance comes from the prompt's citation instruction; nothing here persists a revised method or answer for future use. SRC-1 `crates/semquery-synth/src/citation.rs`, `crates/semquery-synth/src/synthesizer.rs`; closest supplied claim is [RT-CLM-citation-filter](runtime.md#rt-clm-citation-filter).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Ordered unique valid marker strings; then metadata entries, with raw Answer text unchanged.
- Later read-back: inapplicable — no inspected persistence/read-back of these results into later answers.
- Delegated visibility: inapplicable — deterministic local checker, no delegated agent.
- Selection predicate: Regex numeric markers, exact membership in valid_markers, first occurrence, then parseable hit number and existing hit.
- Invalidation or expiry: Per-answer marker set derived anew from offered hits; no global citation registry.
- Activation or effect: Enforces citation-vector membership; does not gate displayed raw tokens or answer truth.
- Evidence limits: No observed answer or measured grounding; valid markers can refer to passages removed by GGUF truncation.

> CITATION_RE.get_or_init(|| Regex::new(r"\[(\d+)\]").unwrap())
> --- `crates/semquery-synth/src/citation.rs`

> if !valid.contains(marker) || !seen.insert(marker.to_string()) {
>       continue;
>     }
>     result.push(marker.to_string());
> --- `crates/semquery-synth/src/citation.rs`

Concrete deterministic deduction: for raw `False [1]. Missing [9]. Again [1].` and valid set `[1]`, regex finds three occurrences, membership rejects `[9]`, and seen-set rejects the second `[1]`; returned markers are exactly `[1]`. Synthesizer backfills that hit's metadata but returns the entire original raw text. The word `False` and whether its proposition is supported never enter the membership decision. This is an implementation countercase to reading filtering as factual validation or answer-text cleanup, not an executed run.

### Claims

#### EPI-CLM-cited-answers
Label: Cited answers

Distinct product-level claim from the narrower parser behavior in [RT-CLM-citation-filter](runtime.md#rt-clm-citation-filter). SRC-1 `README.md`, doctrine/design. The README promises indexed collections and cited question answering. It does not explicitly promise a theorem prover or universal truth guarantee; the warranted comparison is with the implemented source-linking path, not an invented stronger promise.

> `semquery` (short for **semantic query**) is a local, offline-ready RAG tool written in Rust. It indexes your personal document collections and lets you search or ask questions with cited answers — everything stays on your machine: indexes, models, and queries.
> --- `README.md`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member
