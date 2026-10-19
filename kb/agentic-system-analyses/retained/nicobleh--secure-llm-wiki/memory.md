---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "Secure LLM-Wiki memory: extracted claim text, admission metadata, vectors, policy configuration and Git history across ingestion and later queries."
run-id: AAS-2026-10-19-secure-llm-wiki-df02f419bddb-01
source-identity: https://github.com/nicobleh/secure-llm-wiki
reviewed-boundary: dfbc60e37487b61e9a5cbce1271a13576a776d51
---

# Secure LLM-Wiki memory report

## Boundary and evidence

The memory boundary includes the whole shipped CLI knowledge lifecycle: initialization, source acquisition and extraction, admission and quarantine, future-ingestion comparisons, context/query/list read-back, configuration and deletion/reset. It includes direct storage and prompt-builder APIs as alternative capabilities, not presumed deployed consumers. The frozen source is SRC-1 at `dfbc60e37487b61e9a5cbce1271a13576a776d51`, as declared in [the boundary](boundary.md#source-register). Direct reads confirmed the provisional runtime account's principal memory routes. No correction to its factual account is required.

Evidence is source implementation and attributed doctrine/design, not observed operation. Direct inspection covered `src/secure_wiki/__main__.py`, `models.py`, `prompts.py`, `llm_client.py`, `extraction/extractor.py`, `review/adversarial.py`, `gate/write_gate.py`, `trust/tiering.py`, both store modules, `read/hygiene.py`, `tests/test_injection_corpus.py` and `docs/roadmap.md` under SRC-1. Paths abbreviated in this paragraph are relative to `src/secure_wiki/` except the explicit test/docs paths. The runtime supplies the parser/security countercases and model component classifications cited below. No new source identity or evidence layer is introduced.

Generated wiki state, operator edits, provider-side memory/weights, external documents before acquisition, actual vectors and execution traces are not supplied. These gaps prevent conclusions about actual retained content, fidelity, effective trust, model obedience and benefits. Provider-internal retention is opaque, not asserted absent. Corpus payload efficacy is not assessed; the evaluator's source was inspected without executing it or reading every fixture. Tests elsewhere remain supplied boundary/runtime findings rather than this member's direct test inspection.

### Coverage inventory

All source paths below are SRC-1 implementation unless marked doctrine. The compact inventory separates direct inspection from reliance on supplied records.

| Entry point / operation | Source path | Coverage, alternatives and limits |
|---|---|---|
| Installed CLI and dispatch | `src/secure_wiki/__main__.py`; packaging supplied by runtime | Direct dispatch read: init/ingest/list/context/query/clear. [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance), [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), [RT-RTE-context-query](runtime.md#rt-rte-context-query). No model-tool dispatcher or hook registration in this driver; no external host integration inferred. |
| URL/local/PDF/folder acquisition, extraction | `src/secure_wiki/__main__.py`, `src/secure_wiki/extraction/extractor.py`, `src/secure_wiki/prompts.py` | Direct: first 8,000 transformed characters; original truncated text, not sanitizer cleaned output, goes to models. [RT-RTE-extraction-parsing](runtime.md#rt-rte-extraction-parsing), [MEM-OBJ-claim-text](#mem-obj-claim-text). Full original documents and extraction rationale are not retained by this path. |
| Batch review, five gates, quarantine | `src/secure_wiki/review/adversarial.py`, `src/secure_wiki/gate/write_gate.py`, `src/secure_wiki/__main__.py` | Direct: software admission; direct gate can receive caller verdict or review without source. [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), [MEM-OBJ-gate-records](#mem-obj-gate-records). Escalation saves quarantine, not an approval queue. |
| Save, deserialize, manual edits and direct storage | `src/secure_wiki/store/wiki_store.py`, `src/secure_wiki/models.py` | Direct: frontmatter is reload authority; Markdown body is display duplication. [MEM-OBJ-claim-metadata](#mem-obj-claim-metadata), [MEM-OBJ-claim-text](#mem-obj-claim-text). Generic caller identity leaves human control of direct writes unresolved. |
| Embedding save/load/delete and later comparison | `src/secure_wiki/store/embedding_store.py`, `src/secure_wiki/gate/write_gate.py`, `src/secure_wiki/__main__.py` | Direct: all readable vectors reloaded, no claim-status join or model marker. [MEM-OBJ-claim-embeddings](#mem-obj-claim-embeddings). Unknown deployed vector lineage prevents compatibility conclusions. |
| Context/query and strict alternative builders | `src/secure_wiki/read/hygiene.py`, `src/secure_wiki/prompts.py`, `src/secure_wiki/__main__.py`, `src/secure_wiki/llm_client.py` | Direct: all eligible text, no question-specific retrieval or context truncation. Actual loader permits pending option; builders do not. [RT-RTE-context-query](runtime.md#rt-rte-context-query), [RT-BAP-query-evidence](runtime.md#rt-bap-query-evidence). External builder caller unspecified. |
| List including quarantine | `src/secure_wiki/__main__.py`, `src/secure_wiki/store/wiki_store.py` | Direct: human display of preview, trust, short ID, URI; not model context or full review reasons. [MEM-OBJ-gate-records](#mem-obj-gate-records). |
| Init, rule edits, trust override, similarity policy | `src/secure_wiki/trust/tiering.py`, `src/secure_wiki/store/wiki_store.py`, `src/secure_wiki/__main__.py` | Direct: [MEM-OBJ-trust-rules](#mem-obj-trust-rules), [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance). Effective deployed root/rules unknown; changes do not retroactively re-tier claims. |
| Clear/reset, history and withdrawal | `src/secure_wiki/__main__.py`, `src/secure_wiki/store/wiki_store.py`, `src/secure_wiki/store/embedding_store.py` | Direct: deletion and CLI vector cleanup separate; default reset erases history. [MEM-OBJ-wiki-history](#mem-obj-wiki-history). Open query snapshots survive filesystem withdrawal. |
| Evaluator and planned feedback/promotion | `tests/test_injection_corpus.py`, `docs/roadmap.md` | Direct implementation/test text and doctrine respectively. [MEM-ABS-query-feedback](#mem-abs-query-feedback). No run evidence; mocked verdict is not a security measurement or retained learning input. |
| External model state | `src/secure_wiki/llm_client.py` | Direct adapters; supplied [RT-CMP-extraction-model](runtime.md#rt-cmp-extraction-model), [RT-CMP-review-model](runtime.md#rt-cmp-review-model), [RT-CMP-embed-model](runtime.md#rt-cmp-embed-model). Weight updates/provider retention uninspected; no application training call. |

## Core ideas

1. **Compilation, not conversational recollection.** Extraction transforms a bounded source excerpt into claim text. Later queries reload that text, not raw documents or old dialogue. The query loop neither accumulates turns nor writes its answers back. The retained result can shape later answers, but delivery alone establishes neither faithful extraction nor improved capacity ([MEM-OBJ-claim-text](#mem-obj-claim-text), [MEM-ABS-query-feedback](#mem-abs-query-feedback)).
2. **Content and eligibility are different retained parts.** Natural-language statements are interpreted by models; symbolic status/trust fields decide code eligibility. The same active untrusted claim can affect some future admission checks while being ineligible for query context. Frontmatter, not a human-visible Markdown body, is the actual reload source ([MEM-OBJ-claim-metadata](#mem-obj-claim-metadata)).
3. **Two different reuse selectors.** Query selects by stored status/trust and sends every eligible claim. Future ingestion supplies active trusted claim text to review and separately supplies all readable stored vectors to similarity scoring. Embeddings are admission memory, not a semantic query index in this implementation ([MEM-OBJ-claim-embeddings](#mem-obj-claim-embeddings)).
4. **Rejection reasons survive less far than claims.** Failed review notes and gate histories persist, while gate detail also appears in the Markdown body and Git message. Ordinary loaders ignore the body, context omits review notes, and query use does not revise admission policy. Retaining diagnostic traces is not a trace-fed automatic improvement loop ([MEM-OBJ-gate-records](#mem-obj-gate-records), [MEM-OBJ-wiki-history](#mem-obj-wiki-history)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-claim-text
Label: Claim text

Part of: [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

This is the natural-language retained output part of that broader route, not a duplicate route or static prompt. Source-native identity: `Claim.text`. Storage substrate: `pages/<claim_id>.md` or `quarantine/<claim_id>.md`, duplicated in YAML frontmatter and Markdown body. Reload obtains `text` from frontmatter; the body is not a second admission source. Evidence: SRC-1, `src/secure_wiki/models.py`, `src/secure_wiki/store/wiki_store.py`.

> body = claim.text
> if gate_detail:
>     body += f"\n\n> Gate decision: {gate_detail}"
> return f"---\n{frontmatter}---\n\n{body}\n"
> --- `src/secure_wiki/store/wiki_store.py`

> raw = yaml.safe_load(parts[1])
> return Claim.from_dict(raw)
> --- `src/secure_wiki/store/wiki_store.py`

Lineage: model extraction of at most 8,000 post-acquisition characters; parser copies `item["text"]`, caller supplies source/trust. No source excerpt, full raw completion, extraction explanation or conversation is stored alongside it by the CLI. Hash is a digest of normalized truncated source text, not a recoverable copy. Successful semantic extraction is requested, not observed. SRC-1, `src/secure_wiki/__main__.py`, `src/secure_wiki/extraction/extractor.py`; closest parser account: [RT-RTE-extraction-parsing](runtime.md#rt-rte-extraction-parsing).

Write agency: model authors proposals, operator chooses source and possibly trust, Python gates and saves without per-proposition human approval. Direct `save_claim` can write caller text or replace a same-ID page without gate checks; whether a direct caller is human, software or model-controlled is unresolved. Manual filesystem edits can alter the YAML text. Body-only edits change the display but not reload. Admission is therefore an ordinary CLI mechanism, not a store invariant.

Consumers: later review sees active trusted text; consistency fallback uses metadata instead of interpreting text; context/query sees text selected by status/trust and stripped of `[T]`/`[S]`/`[U]`; list previews it. Query's authority is evidence for an answer, not permission to execute directives. The natural-language consumer's compliance remains unobserved. Quarantine text is separately retained and listable but excluded from normal page read-back. No age expiry or automatic semantic revision is wired in these inspected paths.

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-claim-metadata
Label: Claim eligibility and provenance

Part of: [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

This is a separate symbolic output part of ingestion, alongside [MEM-OBJ-claim-text](#mem-obj-claim-text). Source-native identity: `Claim` fields `claim_id`, `source`, `trust_level`, `status`, `ingested_at`, `supersedes`; gate diagnostics are separately classified below. Storage is YAML frontmatter in claim Markdown files; fixed enum/predicate rules, not model interpretation, govern read eligibility. Evidence: SRC-1, `src/secure_wiki/models.py`, `src/secure_wiki/read/hygiene.py`.

> claims = [
>     c for c in all_claims
>     if c.status in statuses
>     and _trust_rank(c.trust_level) <= min_rank
>     and c.trust_level != TrustLevel.UNTRUSTED  # hard floor — never load untrusted
> ]
> --- `src/secure_wiki/read/hygiene.py`

Lineage and admission: UUID/time defaults, caller source/section/hash and trust, then gate-produced active status or storage-produced quarantined status. Source URI/ID/hash completeness is checked, not authenticity; trust derives from domain rules or operator override rather than proposition verification. The untrusted-plus-any-active-trusted gate blocks globally, not just subject-specific overwrite. An untrusted claim may otherwise become active but still cannot enter shipped query context. See [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission).

The loader's caller may include pending records in pages; quarantine directory placement remains a separate exclusion. Current frontmatter is authoritative on reload, with no re-admission, hash recheck against the original source, or signature check in `_deserialize`. Badly deserialized files are silently skipped. Stored `supersedes` and `SUPERSEDED` describe schema possibilities, not an automatic replacement writer: the inspected extractor/gate/driver never assign a successor pointer or set an old claim superseded. Direct edits can change eligibility, but their approval process is outside the known caller contract. A declared enum alone is not a maintained lifecycle.

Later consumers: trust/status control context and existing-trusted review selection; section and source ID control non-vector consistency; ID links JSON vectors and deletion; URI/section/time/gates are copied into CLI context for interpretation, but hash, ID, status and supersedes are not rendered by `_format_claims`. Neither a source label nor a hash proves retained text follows from that source. No retrospective re-tiering follows a trust-rule edit (SRC-1, `src/secure_wiki/__main__.py`, `src/secure_wiki/read/hygiene.py`, `src/secure_wiki/gate/write_gate.py`, `src/secure_wiki/store/wiki_store.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-gate-records
Label: Gate records and review notes

Part of: [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

Source-native identity: `gates_passed`, `review_notes` and serialized `gate_detail`. This output part is not a new review route. Separate operative forms share a diagnostic lineage: gate-name lists are symbolic progress records; failed review reasons and outcome detail are natural-language diagnostic text. Storage: YAML frontmatter contains gate names/review notes; Markdown body contains optional gate detail; quarantine Git commit message contains a shortened reason. Evidence: SRC-1, `src/secure_wiki/gate/write_gate.py`, `src/secure_wiki/store/wiki_store.py`, `src/secure_wiki/models.py`.

> if not review.passed:
>     claim.review_notes = "; ".join(review.reasons)
>     return GateOutcome(
>         decision=GateDecision.QUARANTINE,
>         claim=claim,
>         detail=f"adversarial_review: {claim.review_notes}",
>     )
> --- `src/secure_wiki/gate/write_gate.py`

Lineage and admission: Python appends passed-gate names in order; a failed review copies model reasons only if gate 4 is reached. The CLI computes review before the gate, but an earlier sanitize/provenance/trust rejection returns without copying that review's reasons. Successful reviewer reasons are not saved as `review_notes`. Quarantine/escalation detail is saved without human approval; direct callers can supply arbitrary detail or notes. These are selective outcome traces, not a full review transcript or proof of the claim's truth.

Consumers: deserialization reconstructs notes and gates, but the ordinary review builder receives only claim text; context renders gate names, not `review_notes`, `gate_detail` or source content hash. `list --quarantine` displays text preview/trust/URI, not the detailed reason. Humans can inspect files/history to see reasons; no shipped consumer automatically revises trust or prompts using them. Therefore reasons have a human inspection affordance, while gate names cross to query as evidence metadata. Existing gate names are not checked as an admission credential by the context loader (SRC-1, `src/secure_wiki/prompts.py`, `src/secure_wiki/read/hygiene.py`, `src/secure_wiki/__main__.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-claim-embeddings
Label: Claim embeddings

Part of: [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

Source-native identity: `EmbeddingStore`, `embeddings/<claim_id>.json`, fields `claim_id` and `embedding`. This retained output is distinct from [RT-CMP-embed-model](runtime.md#rt-cmp-embed-model), the external model that produces it. Dense vectors have distributed numerical representation; JSON encoding, claim keys and filesystem location are symbolic substrate/indexing, not model parameters. Evidence: SRC-1, `src/secure_wiki/store/embedding_store.py`, `src/secure_wiki/__main__.py`.

> path.write_text(json.dumps({"claim_id": claim_id, "embedding": embedding}), encoding="utf-8")
> --- `src/secure_wiki/store/embedding_store.py`

Lineage: current extracted claim text goes to the embedding provider before admission. The CLI saves a vector only after the corresponding claim commit; partial failures can leave incomplete coverage. A direct `save` accepts caller-supplied numerical payload with no model/version/text-hash marker or validation. Existing instance provenance is unknown. The payload is not a readable claim summary: code consumes coordinates via cosine similarity; it does not reconstruct text.

Later consumer: next ingestion loads every readable JSON entry and Gate 5 selects the maximum cosine score. No trust/status join or vector dimension/version reconciliation precedes scoring; direct or stale vectors may therefore affect future admission even without a currently eligible page. A vector is not used by query to retrieve top-k facts. Its code-level force is duplicate quarantine at the configured upper threshold or escalation at the lower one, subject to earlier gate passage. Without usable new vector/nonempty vector map, the route switches to the section heuristic, not a new embedding derivation. Semantic correctness/compatibility is unobserved.

Withdrawal: CLI clear deletes vectors for returned claim IDs; CLI reset deletes all. Direct store deletion does not coordinate this automatically. A successful page commit can precede failed vector save; a direct page edit can leave an old vector. No atomic artifact pair or regeneration-on-read is established. The module's untracked comment is not enforcement, because store init/bulk deletion can stage broadly; see [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance) and [MEM-OBJ-wiki-history](#mem-obj-wiki-history).

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-trust-rules
Label: Trust rules and similarity configuration

Part of: [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance)

Source-native identity: `trust_rules.yaml` `rules` and `similarity` sections, `TrustRegistry`. This is a policy-state part of maintenance, not a duplicate route or a learned claim. Symbolic domain strings, enum values and numeric thresholds are stored in YAML; built-ins are static Python data; cached parsed rules are process memory. Comments/explanatory strings are human-readable documentation, not model policy updates. Evidence: SRC-1, `src/secure_wiki/trust/tiering.py`, `src/secure_wiki/store/wiki_store.py`.

> for rule in self._rules:
>     if rule.matches(uri):
>         return rule.level
> return TrustLevel.UNTRUSTED
> --- `src/secure_wiki/trust/tiering.py`

Initialization is software-authored template plus built-in domain defaults. Subsequent file editing is documented operator control, without per-edit approval checks; `TrustRegistry.add_rule` affords caller-driven in-memory prepending but does not save YAML. Generic API caller identity does not establish human content approval. Rules match host equality/subdomain suffix, first match wins; user rules precede built-ins. Numeric threshold conversion supplies no semantic validation of configured threshold choices. Operator override can replace assigned trust for ingestion.

Future-ingestion consumers: assigned trust is copied into claims, and thresholds determine gate decisions. Query trusts stored claim tiers rather than rerunning domain assignment. Default rule path is package-relative while store root defaults cwd-relative, unless environment configuration aligns them. Registry caches after first load; similarity config is loaded for ingestion. Reset preserves rules; changed rules do not automatically repair prior labels or vectors. No extraction/review/query model rewrites this file in the inspected driver. Thus this is editable retained policy with code authority, not inferred automatic policy learning.

- implementation conclusion status: wired
- operation conclusion status: uninspected

#### MEM-OBJ-wiki-history
Label: Wiki Git history

Source-native identity: separate data-root Git repository and its add/quarantine/delete/reset commits. Storage: local `.git` objects plus working files. Symbolic snapshots/diffs and natural-language commit messages form an operation trace, not derived guidance. This spans admission and maintenance, so is not part of exactly one supplied record. Closest overlaps are [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) and [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance); neither declares a standalone history object.

Evidence: SRC-1, `src/secure_wiki/store/wiki_store.py`.

> keep_history=False (default): delete and re-init the git repo so no
> claim content survives in the history.
> keep_history=True: commit a removal on top of the existing history.
> --- `src/secure_wiki/store/wiki_store.py`

Lineage/write control: software writes the file then stages and commits it; message references URI, shortened ID/trust or quarantine reason. Human starts ingestion but does not approve each commit. Direct storage calls also commit. Physical success depends on Git/filesystem and is not transactional with claim/vector writes. Broad `git add .` at init and `git add -A` during bulk deletion can stage co-located files, so embeddings are not guaranteed untracked merely by their module comment.

Later consumers: operator Git inspection/reversal is an afforded forensic/recovery path, not a deployed automatic memory route. CLI query/ingest reload the working files, not Git history; no model receives diffs/commit messages through those paths. Ordinary deletion can retain prior snapshots; default reset destroys the repository while preserving rules, whereas keep-history commits removals. No append-only audit or automated rollback is established. This object's rationale coverage is limited to serialized diagnostics and messages, not original source/model dialogue.

- implementation conclusion status: wired
- operation conclusion status: uninspected

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

#### MEM-ABS-query-feedback
Label: Query feedback update

Within SRC-1 at the reviewed revision, the shipped query path has no answer/feedback-to-store update. Search inspected `src/secure_wiki/` for `feedback`, `review_notes`, `supersedes`, `SUPERSEDED`, `save_claim`, `load_claims` and `load_all`, then directly traced the complete query/dispatch, storage and gate implementations. The positive evidence is the query loop's fresh stream call and stdout-only handling; no save operation follows before the next question or exit. Evidence: SRC-1, `src/secure_wiki/__main__.py`; [RT-RTE-context-query](runtime.md#rt-rte-context-query) supplies the corresponding route. This is a bounded implementation absence, not a statement about external provider retention, undocumented user scripts or inaccessible model learning.

> stream = client.stream(system, question)
> --- `src/secure_wiki/__main__.py`

Doctrine explicitly distinguishes future feedback from current behavior (SRC-1, `docs/roadmap.md`):

> **Current state:** Query answers are shown but user reactions are not captured.
> --- `docs/roadmap.md`

No automated trace-fed rewrite of claim eligibility/policy from query outcomes can be attributed to this inspected path. The source compilation chain does produce derived claims for later consumers; that positive mechanism is not negated by this absence. Model-internal adaptation remains uninspected. Tests supply fixed expected decisions, not a retained runtime evaluation-feedback stream: the corpus creates a fixed proposed claim and mocks review according to the manifest (SRC-1, `tests/test_injection_corpus.py`; supplied quotation in [the runtime account](runtime.md#authority-change-admission-and-remaining-limits)).

- implementation conclusion status: absent
- external-provider conclusion status: uninspected

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

Memory read-back trigger is a later operator ingestion request, not unsolicited memory push. Startup loads active page claims and all readable vector JSON; the batch reviewer receives only active trusted claim text, with markers stripped, alongside new source/proposals. It receives neither prior reviewer reasons nor stored provenance metadata for those existing statements through `build_review_prompt`. Gate 3 uses active trusted existence; Gate 5's vector path uses the whole supplied vector map independently of trust/status. Without vectors, the fallback selects active trusted claims by same section and different source ID. No top-k review budget or model-input trimming is implemented; the 8,000-character cap applies to the newly acquired source, not accumulated existing claims. Evidence: SRC-1, `src/secure_wiki/__main__.py`, `src/secure_wiki/prompts.py`, `src/secure_wiki/gate/write_gate.py`.

> existing_block = "\n".join(
>     f"- {_safe_claim_text(c.text)}" for c in (existing_high_trust or [])
> )
> --- `src/secure_wiki/prompts.py`

Persisted parts and their actual consumers are separated in [MEM-OBJ-claim-text](#mem-obj-claim-text), [MEM-OBJ-claim-metadata](#mem-obj-claim-metadata), [MEM-OBJ-gate-records](#mem-obj-gate-records) and [MEM-OBJ-claim-embeddings](#mem-obj-claim-embeddings). Review/gates automatically admit new knowledge; starting ingestion or selecting source trust is not approval of each derived proposition. Rejection retains selected diagnostics and rejected text in quarantine; it does not automatically replace established content. No trace-derived method change follows from stored diagnostics in the inspected loop.

#### On [RT-RTE-context-query](runtime.md#rt-rte-context-query)

Read-back is operator-requested at context/query startup. Code selects page records by stored trust/status, sorts through the store's filename iteration, strips trust-marker tokens from text and renders URI/section/ingested time/gate names. The selector does not receive the question; all eligible records enter a nonce-delimited block. There is no explicit token/character budget, top-k selector, recency decay or source revalidation at this read boundary. Provider limits can still constrain actual calls; successful handling of oversized stores is unobserved. Evidence: SRC-1, `src/secure_wiki/read/hygiene.py`, `src/secure_wiki/__main__.py`.

> lines.append(f"[{sym}] {strip_trust_markers(claim.text)}")
> lines.append(f"    source:    {claim.source.uri}")
> lines.append(f"    section:   {claim.source.section}")
> lines.append(f"    ingested:  {claim.ingested_at}")
> lines.append(f"    gates:     {', '.join(claim.gates_passed)}")
> --- `src/secure_wiki/read/hygiene.py`

Working-context control is isolation and initial filtering, not compression of accumulated dialogue: extraction and review each get fresh calls; query reuses a fixed loaded system context plus only the current question. Earlier answers/turns remain outside the next call and are not persisted by this route. The isolated-call frame analogy fits selected inputs plus returned text, but there is no heap-like reference from the model window to omitted source/history; no retrieval tool follows such a pointer. A new host invocation can reload surviving pages; it cannot recover discarded raw model dialogue through the wiki store. No compaction summary/checkpoint alternative is produced by these adapters. SRC-1, `src/secure_wiki/llm_client.py`, `src/secure_wiki/__main__.py`.

The strict prompt-builder APIs are afforded alternate renderers for caller-supplied claims, not evidence that an unknown external agent loads the store. The actual CLI uses `load_for_context`, with optional pending inclusion. A manual deletion, re-tiering or reset cannot retract context already loaded into an open query session. Delivery to the model is wired; subsequent use, obedience and benefits are unobserved.

#### On [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance)

Retained policy has software/template initialization and documented operator edits, with code-level authority on future ingestion as [MEM-OBJ-trust-rules](#mem-obj-trust-rules) details. Clear uses human confirmation, then separate page and vector deletions. Direct store APIs do not enforce that confirmation or companion-vector cleanup. Deleted working-state content stops reaching new page loads, but retained Git history may survive; an open query snapshot does not refresh. Default reset removes history as well as working content while retaining rules. Evidence: SRC-1, `src/secure_wiki/__main__.py`, `src/secure_wiki/store/wiki_store.py`, `src/secure_wiki/store/embedding_store.py`.

#### On [RT-BAP-query-evidence](runtime.md#rt-bap-query-evidence)

The behavioral authority belongs to selected text plus its displayed provenance/trust/gates, not to every serialized field. The consumer receives no raw source excerpt, hash verification, reviewer explanation or vector through `_format_claims`. Despite its placement inside a system string, the declared force is evidence, not instructions; enforcement beyond marker removal/status filtering depends on model compliance. Missing rationale and unverifiable source lineage limit confidence, not delivery. Evidence: SRC-1, `src/secure_wiki/read/hygiene.py`, `src/secure_wiki/prompts.py`; the governing instruction quotation is retained in the supplied record.

## Write side

The raw-to-derived chain is acquired/transformed/truncated source → extraction completion → pending claim text with caller metadata → reviewed/gated page or quarantined file → later review/query consumer. The first source hash describes only the normalized processed excerpt. The sanitizer's cleaned-text output does not become the extraction source. Empty extraction returns before saving quarantine, including nonce-rejected envelopes; compatibility parser outputs may proceed with warnings. These limits are directly confirmed by SRC-1, `src/secure_wiki/__main__.py`, `src/secure_wiki/extraction/extractor.py`, and [RT-RTE-extraction-parsing](runtime.md#rt-rte-extraction-parsing).

The ordinary acquisition/admission mechanism is automatic after the operator chooses source/trust. Extraction authors proposed statements, batch review can veto, fixed gates decide, and storage performs I/O. Human trust selection is not per-statement truth review. Direct gate invocation may supply its verdict; direct storage does not run the gate. Manual frontmatter edits can change content/eligibility without re-admission. Generic direct API authorship and approval remain unknown rather than labelled human by assumption. See [MEM-OBJ-claim-text](#mem-obj-claim-text), [MEM-OBJ-claim-metadata](#mem-obj-claim-metadata).

Transformation is compilation of document statements, not automatic rewriting of prompts/rules from experience. The model is asked for atomic statements, not evidence of formulated theory criticism. Embeddings derive from text and influence future admission, not provider weights or query retrieval. External model fixity/version limits are preserved in the supplied model component records. The diagnostic chain retains selected gate outcomes and failed reasons, but no later automatic consumer derives new policy from them ([MEM-OBJ-gate-records](#mem-obj-gate-records), [MEM-ABS-query-feedback](#mem-abs-query-feedback)).

Maintenance is operator-side configuration or file editing and explicit clear/reset. Trust rules are not retroactive; no shipped promotion command or automatic supersession/decay completes the quarantine lifecycle. The roadmap admits manual promotion, while the schema's successor fields remain only storage possibilities in inspected writers (SRC-1, `docs/roadmap.md`, `src/secure_wiki/models.py`, `src/secure_wiki/__main__.py`). Rejection preserves proposed text, selected diagnostics and history; withdrawal affects future reload but not an already loaded session. File/Git/vector changes are separate, so partial failure can leave mixed state. Recovery is retry/manual inspection/Git reversal where history survives, not automatic semantic rollback.

## Read-back

There are three concrete retained-state consumer chains, plus human inspection affordances:

- **Future ingestion:** requested startup load → active trusted text for batch review and metadata for gate rules, plus separately loaded vectors → model review/code admission of new proposals. Claims admitted earlier in a folder also update in-process lists for later sources. Within-command ordinary state and cross-command retained read-back are distinct horizons of the same checks. No evidence proves prior reasons are reused ([RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission), [MEM-OBJ-claim-embeddings](#mem-obj-claim-embeddings)).
- **Context/query:** requested load → status/trust filter → every eligible claim, metadata rendering and nonce wrapping → printed context or query model system string. Selection precedes the question; no automatic push, semantic retrieval or model-controlled reload is wired. Answers are immediate output, not retained memory. The strict builders have a different status policy but no identified external consumer wiring ([RT-RTE-context-query](runtime.md#rt-rte-context-query)).
- **Policy reuse:** later configuration load/client creation → rules/thresholds/model settings → future admission decisions. Persisted YAML policy is distinct from static prompts and external model weights; no automatic update from query traces is established ([MEM-OBJ-trust-rules](#mem-obj-trust-rules), [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance)).
- **Inspection/recovery:** list reads current active/quarantine records into previews; direct file/Git inspection can expose full diagnostics/history to an operator. These affordances do not establish automated adoption, promotion or a model consumer of history ([MEM-OBJ-gate-records](#mem-obj-gate-records), [MEM-OBJ-wiki-history](#mem-obj-wiki-history)).

## Integration issues

- **Corrections to supplied facts:** none. Direct source reads corroborate the supplied distinctions between strict builders and pending-capable CLI loader, direct storage and gated admission, vector similarity and conflict proof, normal Git recording and durable audit guarantees.
- **Potential duplicate records:** none identified. The four claim-output objects explicitly declare containment in [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission); policy state is part of [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance). [MEM-OBJ-wiki-history](#mem-obj-wiki-history) spans both routes and is a distinct artifact, not their replacement. [MEM-ABS-query-feedback](#mem-abs-query-feedback) makes a searched bounded absence explicit rather than replacing the query route. Model objects and static prompts are annotated/discussed by citation, not redeclared.
- **Effective state and local authorship remain unknown:** no instance files or direct-call principal are supplied. [MEM-OBJ-claim-text](#mem-obj-claim-text), [MEM-OBJ-claim-metadata](#mem-obj-claim-metadata), [MEM-OBJ-trust-rules](#mem-obj-trust-rules). This prevents assigning human approval to arbitrary API writes or certifying provenance/trust of a deployed store.
- **Vector compatibility and stale-state effects remain unresolved operationally:** no model/version marker or claim join accompanies reload. Code permits mismatches; their occurrence/effect is unobserved. [MEM-OBJ-claim-embeddings](#mem-obj-claim-embeddings). This prevents asserting a complete semantic consistency index or reproducibility after model changes.
- **Rationale does not traverse the ordinary model read-back:** failed notes survive storage but are omitted from review/query rendering; body-only diagnostics are not deserialized. [MEM-OBJ-gate-records](#mem-obj-gate-records). Reconciliation must not infer rationale-informed learning from trace retention.
- **Deployment/provider behavior remains outside evidence:** source wiring establishes delivery, not activation, truth, injection resistance or benefit. [RT-BAP-query-evidence](runtime.md#rt-bap-query-evidence), [RT-CMP-review-model](runtime.md#rt-cmp-review-model). No supplied observation resolves these limits.

## Limitations and checks

Rechecked source HEAD against the boundary revision and confirmed a clean target checkout. Read only the registered source and supplied method/inputs; no target execution, tests, services, fixtures or external sources were introduced. The type/record contracts and worker rules supplied here govern the candidate; no method changes were made. Consequential counterchecks included body-versus-frontmatter reload, pending inclusion versus strict builders, direct write bypass versus normal gate, vector-only admission effects versus query retrieval, and preserved versus wiped history.

No live source, extraction/review output or provider trace proves faithful compilation, attack resistance, truth or improved future capacity. No observed consumer behavior establishes activation or benefit. Absence of a local query feedback writer is bounded to inspected code, not to opaque provider state. Validation is a deterministic form/quotation/identity check, not semantic acceptance or a security experiment.

Validation: the required `commonplace-run validate-output` check passed for this invocation.
