---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent report verification of Cortexes capture, vault maintenance, retrieval and evaluation at the frozen commit."
run-id: AAS-2026-11-08-cortexes-af94078f2405-01
reviewed-boundary: "2b8e79f0099203e0453147b708346349952bb963"
---

# Cortexes report verification

## Verification

The reports support a bounded account of the shipped vault loop. No material blocker was established. One local omission in the helper's write-side inventory remains below. This judgment concerns source support, not observed operation or retrieval quality.

### Evidence and record review

I read every supplied report, the reconciliation, the empty correction-answer files and the structural check, which reports `none`. There are no structural failures to route and no correction claims to accept on trust. I checked every declaration and annotation for its referent, source support, evidence strength and relation to the other reports. I did not repeat deterministic quotation-occurrence or reference-resolution validation as semantic verification.

SRC-1's checkout HEAD equals the reviewed commit and its working tree is clean. I enumerated the frozen tracked tree and independently read the command wrappers, all shipped skills, hook manifest, lifecycle scripts, deck and deck-core modules, takeoff helper, CLI dispatcher, config, store, fusion, reranker, parser, BM25, graph, Raw projection, map/span/page modules, plan lifecycle, queue/reclaim modules and evaluator runner/adapters/metrics/corpus. Additional targeted reads covered classifier/control and final-redaction branches, Raw identity/marker normalization, maintenance-session detection, static synonyms and tokenization. All are implementation or doctrine/design evidence under the existing source register in [boundary](boundary.md#source-register); none is run or causal evidence. No target program or test was executed.

The five model-component records in [runtime](runtime.md#components) correctly separate provider parameters from local document embeddings, configured names from immutable weight revisions, and distinct call roles from a shared default model name. The records do not claim that opaque provider internals were inspected. Both claim records retain source-native purpose/design statements rather than promoting them to demonstrated benefits: [RT-CLM-vault-purpose](runtime.md#rt-clm-vault-purpose) and [EPI-CLM-vault-index](epistemic.md#epi-clm-vault-index).

All memory object records were compared with their actual producers and consumers. The distinctions between filtered Raw, canonical pages, vector documents/embeddings, lexical tokens/display metadata, process-local graph topology, markers/logs, temporary plan state and batons survive that comparison ([memory objects](memory.md#operative-objects)). In particular, `store.py` passes a body prefix to summary generation and later extracts a display line from the winning vector document; BM25 and graph do not consume that generated summary as their display input. Their storage and authority findings are supported, without requiring faithful model summaries or an atomic cross-store transaction. The epistemic object declarations identify the same Raw/pages and distinct summary/evaluator objects, with the duplicate identities retained in reconciliation.

### Consequential route checks

- **Capture and context delivery.** The manifest connects the lifecycle scripts. Start emits topic metadata and baton previews, while deck substitution removes only the menu from compatible hook-context rows and forwards on failure. End detaches capture after eligibility checks. In `filter-transcript.py`, Task passthrough and recognized tool filters precede generic classification; classifier failures preserve content, and whole-body redaction occurs later with a fail-preserving exception branch. These facts support [RT-RTE-session-start](runtime.md#rt-rte-session-start) and [RT-RTE-session-capture](runtime.md#rt-rte-session-capture), not a universal privacy or preservation guarantee. The reports correctly distinguish possible source-level fallback behavior from an observed leak.
- **Review and delivery.** I traced map/span output accounting into plan charges, reviewed intervals, evidence admission, negative sealing, source normalization and completion. The ledger checks its own API state, not cognition, human approval, successful note writes or Git commits. Reset and direct-tool alternatives are retained. The human verdict/draft policies and broadcast's target/change decisions are explicit in the skills. Inline dispatch, zero-page finalization, pending-target override and partial abort recovery support [RT-RTE-distill-review](runtime.md#rt-rte-distill-review), [RT-RTE-broadcast-edit](runtime.md#rt-rte-broadcast-edit) and the [workflow account](workflow.md#workflow-account). The account does not turn instruction following into observed completion.
- **Search and withdrawal.** I followed CLI-produced filters through vector, BM25 and graph consumers, then diversification, cosine backfill and reranking. For the filter shapes the shipped CLI produces, the reports' scoped selector account holds. Graph filters returned nodes rather than intermediate traversal, and reranking indexes only existing candidates. Supported no-vector and failed-backfill branches preserve the reported zero-score ambiguity. Rebuild's directory scan is not upsert's admission boundary. Delete's vector-empty early return skips lexical removal. These support [RT-RTE-vault-search](runtime.md#rt-rte-vault-search), [MEM-OBJ-vectorstore](memory.md#mem-obj-vectorstore) and [MEM-RTE-index-delete](memory.md#mem-rte-index-delete), including their qualifications.
- **Cleanup, alternate projection and continuation.** Reclaim compares nonempty body sequences from a turn header, retains blank lines within them, checks repo equality and removes selected candidates through Git or unlink. It does not preserve unique header metadata by proof. Raw-view's explicit-level branch bypasses automatic budget selection without creating a durable checkpoint. Takeoff prepare and clear have the stated preflight/ownership checks, but path lookup and separate host Write prevent a universal filesystem enforcement claim. The corresponding [MEM-RTE-reclaim-raw](memory.md#mem-rte-reclaim-raw), [MEM-RTE-raw-view](memory.md#mem-rte-raw-view) and [RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff) findings remain supported.
- **Epistemic force and evaluation.** The [authority ledger](epistemic.md#authority-route-ledger) separates checks, dispositions, retention and integration. Human useful-retention decisions are not presented as factual validation. Evaluator arithmetic consumes supplied gold; proposal assigns the source page as gold and writes without enforcing review. Adapters have unequal freshness assumptions. These support [EPI-RTE-eval-score](epistemic.md#epi-rte-eval-score) and [EPI-RTE-query-propose](epistemic.md#epi-rte-query-propose), not observed retrieval benefit or causal attribution. I considered whether the proposal row's non-truth-apt policy/update classification conceals acquired warrant: it describes assigned benchmark targets, while the inventory explicitly preserves their relevance-judgment meaning and uncertain validity. It does not claim verified labels or accepted novel knowledge; no material classification defect was established. Generic editing and retention likewise do not establish the independently discussed learning, theory-building or exercised self-improvement properties.

### Relations and reconciliation

I checked all explicit `Part of:` relations: reclaim is an adjunct within capture; summary generation and its output are contained in the broader direct-save/indexing route. These are functional containment claims, not assertions that an object is itself a route. The three supersessions in [reconciliation](reconciliation.md#duplicate-identities) preserve matching Raw, canonical-page and explicit-withdrawal referents without changing findings. Cleanup checking/removal and evaluation/proposal remain distinct functions under valid broader containers; summary is not superseded by the entire vector store. No split requires replacing a still-valid container.

The memory integration issues are disposed of without selecting stronger statuses: conditional withdrawal and broader upsert qualify, rather than contradict, runtime's account. The every-hit-cosine mismatch is between shipped prose and implementation, not between analysts. Function-specific `implemented` versus `doctrine only` ledger statuses do not contradict a mixed route's `wired` implementation status. No unresolved cross-report conflict was identified that needs both positions retained as a disputed conclusion. The reconciliation does not itself adjudicate truth or revise analyst records.

### Omission search and stopping decision

The frozen tree and producer/consumer dependencies selected three omission questions: could command/helper paths bypass the ordinary admission procedure; could non-vector or graph paths change the retrieval account; and could evaluator or maintenance callers silently promote content or remove future review eligibility? Wrapper, helper, upsert/delete, fusion/graph, evaluator and `meta_session.py` inspection answered these questions within the account's scope. Maintenance detection tests for a recognized structured Skill invocation, not proof that the entire session contained only maintenance; the reports do not claim such purity. Static synonym expansion adds configured lexical candidates, not learned source knowledge. The takeoff helper's additional configuration write is retained as the local limit below.

I also checked map continuation decoding and progress accounting. Map progress records a maximum reached index, not an authenticated history of contiguous traversal; the sequential returned-cursor procedure and semantic/ambiguous-range gate remain supported. The reports' ledger findings are acceptable as API accounting within the prescribed procedure, not as an adversarial attestation of every map card's delivery. Their existing direct-tool/reset and cognition qualifications prevent treating this as host-enforced complete reading.

Further optional omission expansion stopped because these selected questions have supported dispositions and no identified material challenge remains undisposed. Individual command/TOML reducers, private content and host/provider internals are not exhaustively verified. The reports already withhold universal preservation, deployment isolation, model compliance, complete provenance, performance and benefit conclusions; those acknowledged uncertainties are not new defects or evidence of absence.

## Blockers

none

## Limits

- [RT-RTE-takeoff-handoff](runtime.md#rt-rte-takeoff-handoff) and [MEM-OBJ-takeoff](memory.md#mem-obj-takeoff) omit an additional write-side mechanism: prepare can append `.takeoff/` to the vault's `.gitignore` and commit that rule before checking ignored status. SRC-1, `hooks/scripts/takeoff.sh`, implementation. The curated baton and its separate host Write remain correctly characterized; the omission only prevents treating their write-side inventory as a complete account of helper configuration/Git effects. It does not establish that baton content is committed or that ignored-path preflight universally enforces host writes.

  > if ! grep -qxF '.takeoff/' "$gitignore" 2>/dev/null; then
  >       printf '.takeoff/\n' >>"$gitignore"
  > --- `hooks/scripts/takeoff.sh`

  > git -C "$vault" commit -q -m "cortex: gitignore .takeoff/ (takeoff batons)" -- .gitignore
  > --- `hooks/scripts/takeoff.sh`
