---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "Secure LLM-Wiki workflow: operator-selected source ingestion through batch review, per-claim admission, durable storage and later query delivery."
run-id: AAS-2026-10-19-secure-llm-wiki-df02f419bddb-01
reviewed-boundary: dfbc60e37487b61e9a5cbce1271a13576a776d51
---

# Secure LLM-Wiki workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is **ingest one operator-selected source, admit or quarantine its extracted claims, then consume eligible claims in a later query**. It was selected because it connects the system's central knowledge-production and knowledge-consumption responsibilities through actual persisted state. The later query requires a separate operator invocation; ingestion does not automatically launch a query. This is not a workflow assembled from unrelated capabilities: the query loader reads the pages written by ingestion. The governing records are [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission) and [RT-RTE-context-query](runtime.md#rt-rte-context-query).

The evidence is source implementation and shipped prompt doctrine in SRC-1 at the frozen revision in [the boundary](boundary.md#boundary-and-evidence). This inspection independently checked the driver, reviewer, gate, storage, read hygiene and prompt text (`src/secure_wiki/__main__.py`, `src/secure_wiki/review/adversarial.py`, `src/secure_wiki/gate/write_gate.py`, `src/secure_wiki/store/wiki_store.py`, `src/secure_wiki/read/hygiene.py`, `src/secure_wiki/prompts.py`). These are already registered source paths, not new evidence sources. No target commands, models or tests were executed. The trace establishes wiring, not successful delivery in a real session or security effectiveness.

### 1. Operator request becomes a bounded extraction task

The local operator supplies a file or URL to `ingest`, optionally overriding trust and source identity. Python resolves trust, loads existing active claims and embeddings, reads/transforms the source, and truncates it to 8,000 characters. It computes the source reference and sanitization report. The report's flags are retained for admission; suspicious source text is not withheld from the extraction or review calls. The CLI passes the original truncated source text, not the sanitizer's cleaned version. Thus early detection does not mean early termination of model exposure (SRC-1, `src/secure_wiki/__main__.py`; [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)).

Python delegates extraction to a model as a text computation, not as a worker with filesystem authority. The handoff provides a separate system instruction and nonce-delimited source text. It supplies neither the existing wiki nor an earlier conversation. The extraction return is parsed into pending claims carrying caller-supplied provenance and trust; the model does not choose the next stage or commit location. Empty extraction ends this source without a retained quarantine item. Accepted legacy arrays and linewise parsing do not uniformly verify the nonce, so successful parsing is not proof that every accepted response followed the requested envelope (SRC-1, `src/secure_wiki/extraction/extractor.py`; [RT-RTE-extraction-parsing](runtime.md#rt-rte-extraction-parsing)).

### 2. Proposals cross distinct embedding and review handoffs

The host sends each proposed claim text for embedding, using concurrent futures, then collects available vectors. A failed individual embedding is ignored; embedding setup failure prints a fallback notice. Processing can continue without vectors. The vectors are numerical inputs to a later code check, not votes from another agent. Next Python delegates one security review for all claims extracted from this source. The reviewer receives the proposals, originating source text and existing active trusted claims. Its separate prompt/context excludes the extraction conversation, but intentionally reintroduces source-derived content. Separate contexts are implemented; different model weights are not enforced (SRC-1, `src/secure_wiki/__main__.py`, `src/secure_wiki/review/adversarial.py`; [RT-CMP-review-model](runtime.md#rt-cmp-review-model), [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)).

The review contract asks for manipulation detection, not truth assessment. It returns a nonce-bearing verdict and reasons. A valid `pass` lets claims proceed; it does not commit them. There is no factual answer oracle. Review is performed before the per-claim gate loop, and the same result is reused for every proposal from that source (SRC-1, `src/secure_wiki/__main__.py`):

> review_result=batch_review,
> --- `src/secure_wiki/__main__.py`

Consequently, review is not rerun after an earlier claim from the batch is committed. The per-claim consistency checks can nevertheless see earlier successful claims through the mutable existing-state lists. This is sequential code coordination, not reviewer negotiation or iterative repair of a proposal (SRC-1, `src/secure_wiki/__main__.py`):

> store.save_claim(claim)
> existing.append(claim)
> --- `src/secure_wiki/__main__.py`

### 3. Code owns admission and durable effects

Python evaluates each claim through sanitization, provenance completeness, trust tier, batch review and consistency. The first failing check determines the outcome. Sanitization flags can reject a claim despite a passing review. Missing provenance fields reject without authenticating provenance; any existing active trusted claim is enough to reject an untrusted proposal at the trust check. A passed reviewer cannot override these checks (SRC-1, `src/secure_wiki/gate/write_gate.py`; [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)).

Consistency uses the best available cosine match, with default duplicate and escalation thresholds of .95 and .85. Without a usable new vector or existing vector map, it uses a same-section/different-source trusted-claim heuristic. Neither similarity nor shared section proves contradiction. A conflict outcome requests human review rather than generating a corrected proposition. All checks passing marks the claim active; the CLI writes it to `pages/`, commits that write to the data repository, then saves its embedding if available. The host, not either model, performs these effects. Starting ingestion and selecting source trust are human decisions; ordinary successful claims require no subsequent per-claim human approval (SRC-1, `src/secure_wiki/gate/write_gate.py`, `src/secure_wiki/__main__.py`, `src/secure_wiki/store/wiki_store.py`; [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)).

The ingestion delivery condition is a completed store operation followed by the CLI's outcome/count reporting. This is narrower than a transactional delivery guarantee: files are written before Git succeeds, and embeddings are saved after the claim commit. A failure can leave partially persisted state. Direct `save_claim` calls and manual files are outside the ordinary gate coverage, so the gate is not an unavoidable storage boundary (SRC-1, `src/secure_wiki/store/wiki_store.py`, `src/secure_wiki/__main__.py`; [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)).

### 4. A later question consumes a filtered snapshot

A separate `query` invocation loads eligible pages. The default is active trusted/semi-trusted claims; the CLI can include pending pages, but never untrusted-labelled claims. Quarantine files are not selected. The loader removes body trust-marker tokens and formats claim text with source URI, section, ingestion time and gate history inside a fresh nonce boundary. It does not retrieve by question or consult embeddings. Python composes this context, a hygiene instruction and the query task prompt into the system string (SRC-1, `src/secure_wiki/read/hygiene.py`, `src/secure_wiki/__main__.py`; [RT-RTE-context-query](runtime.md#rt-rte-context-query), [RT-BAP-query-evidence](runtime.md#rt-bap-query-evidence)).

The query model receives that snapshot and the current question. Each question is a new call, without prior questions or answers, and the snapshot is not refreshed during the session. The prompt requests evidence-only answers, source citations and abstention when evidence is insufficient. No code comparator verifies those qualities. A delivered query result means streamed answer text and usage have reached stdout, not that the answer has passed an independent review. Answers do not persist or trigger new claim admission (SRC-1, `src/secure_wiki/__main__.py`, `src/secure_wiki/prompts.py`; [RT-RTE-context-query](runtime.md#rt-rte-context-query)).

### Rejection, retry and recovery

The selected failure branch is a malformed review response. The review function owns bounded recovery: invalid JSON or an incorrect nonce causes another call using the same constructed prompt and nonce, for up to three total calls. A deliberate valid block returns immediately; exhausted parse/nonce retries return a failed review with the final error reason. Provider exceptions and unexpected parsed types are not generally converted into that fail-closed result (SRC-1, `src/secure_wiki/review/adversarial.py`):

> return ReviewResult(passed=False, reasons=[last_error])
> --- `src/secure_wiki/review/adversarial.py`

Claims reaching gate 4 with this result receive review notes and quarantine decisions. Earlier gates can reject first, so not every claim from a blocked batch necessarily records the reviewer as its rejection reason. The CLI stores both quarantine and escalation outcomes in quarantine; escalation increments a distinct count but does not suspend execution for a human response (SRC-1, `src/secure_wiki/gate/write_gate.py`, `src/secure_wiki/__main__.py`):

> else:
>     store.save_quarantined(claim, outcome.detail)
>     escalated += 1
>     print(f"{label} ESCALATE    {outcome.detail}")
> --- `src/secure_wiki/__main__.py`

No automatic proposal rewrite, promotion response or resumable checkpoint completes this rejection path in the inspected driver. Quarantine is a durable terminal branch for this invocation, inspectable later rather than automatically consumed by queries. An operator must arrange any subsequent repair. Existing maintenance affords deletion or reset; Git reversal depends on surviving history. Default reset destroys and recreates that history, so recovery cannot rely on an append-only audit trail. There is no automatic rollback around file/Git/vector failures (SRC-1, `src/secure_wiki/store/wiki_store.py`; [RT-RTE-operator-maintenance](runtime.md#rt-rte-operator-maintenance)).

Overall, Python owns progression, two text-model roles propose and veto within fixed stages, and the operator owns later questions and manual recovery. The source supports this multi-step architecture, not measured reviewer accuracy, model obedience, reliable transaction recovery or improved answers.

## Shared records

### Components

none declared in this member

### Operative objects

none declared in this member

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-ingest-admission](runtime.md#rt-rte-ingest-admission)

Workflow role: source-compilation stage and durable handoff to later invocations. Delegation has no autonomous scheduling: extraction proposes, review can veto, and code applies per-claim checks and writes. A batch review is reused rather than revised as each claim is stored. Embedding failures select an alternate consistency mechanism, not a retry of the whole job. Ordinary commit concludes without per-proposition human approval; escalation concludes in quarantine rather than waiting for an approver. Delivery and recovery boundaries are described in the workflow account above.

#### On [RT-RTE-context-query](runtime.md#rt-rte-context-query)

Workflow role: separately operator-triggered consumption and answer delivery. Eligibility is decided before questions are asked; each question reuses the same snapshot without conversation accumulation. Streamed output is the final product, with no answer-validation, persistence or feedback handoff back to ingestion. Prompt-requested citations and abstention do not create an acceptance oracle.
