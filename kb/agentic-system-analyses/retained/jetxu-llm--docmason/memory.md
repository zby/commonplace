---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "DocMason memory: published document semantics, pending and promoted interaction evidence, continuation state and trace-derived evaluation candidates."
run-id: AAS-2026-10-13-docmason-deba9ae199d5-01
source-identity: https://github.com/JetXu-LLM/DocMason
reviewed-boundary: f3970939593194a158ab7ea1d49995f06cbccc86
---

# DocMason memory report

## Boundary and evidence

DocMason retains document-derived evidence, agent-authored semantics, interaction-derived evidence and governed task state. It supplies selected material to an external host; it does not own that host's model window or parameters. This account uses SRC-1 at the boundary's frozen commit. Direct reads extend the boundary's initial inspection into interaction capture, promotion, maintenance, reader filtering, semantic authoring, overlay freshness, runtime projections and regression admission. They supply implementation and doctrine/design evidence, not observed operation.

Included memory surfaces follow the runtime's ask, sync, evidence-tool, hook, enrichment and evaluation routes. Static canonical instructions and adapters are delivery machinery rather than accumulated experience; their changing projections are described through supplied records. Core replacement preserves private state but is not itself conversation-memory curation. External model weights, provider caches, native host compaction and actual delegation windows remain outside the inspected implementation. No private corpus, published instance, live transcript or evaluation run is supplied; this prevents claims about exercised recall, host adherence or improved capacity.

The table distinguishes direct source inspection from supplied runtime findings. Every path is relative to SRC-1.

| Entry or operation | Source path and inspection basis | Coverage and limit |
|---|---|---|
| Public retrieve/trace and `_ask`/`_hook` dispatch | Direct CLI retrieval options in `src/docmason/cli.py`; supplied dispatch account in runtime | [RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools), [RT-RTE-canonical-ask](runtime.md#rt-rte-canonical-ask), [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks). No separate registered model-tool registry is established by these entries. |
| Physical document staging; sample corpus driver | Supplied runtime/boundary; direct preservation and conservative synthesis in `src/docmason/knowledge.py` | [MEM-OBJ-source-evidence](#mem-obj-source-evidence), [MEM-OBJ-knowledge-text](#mem-obj-knowledge-text), [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish). Individual Office/PDF extraction branches and binary sample contents not audited; extraction fidelity remains unresolved. |
| Host semantic authoring and additive overlays | Direct `skills/canonical/knowledge-construction/SKILL.md`, `src/docmason/semantic_overlays.py`, `src/docmason/hybrid.py`; supplied hybrid route | [MEM-OBJ-knowledge-text](#mem-obj-knowledge-text), [MEM-OBJ-semantic-overlay](#mem-obj-semantic-overlay), [RT-RTE-hybrid-refresh](runtime.md#rt-rte-hybrid-refresh). Authoring requested, not observed. |
| Validation-derived retrieval/trace indexes and source deletion filtering | Direct `src/docmason/knowledge.py`, `src/docmason/retrieval.py` | [MEM-OBJ-reader-index](#mem-obj-reader-index), [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish), [RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools). Cache-key internals and all incremental combinations not audited. |
| Native capture and alternative provider reconciliation | Direct shared reconciliation, entry persistence, cursor-tail compaction and provider dispatch in `src/docmason/interaction.py`; ask self-capture handling in `src/docmason/ask.py` | [MEM-OBJ-native-ledger](#mem-obj-native-ledger), [MEM-OBJ-interaction-entry](#mem-obj-interaction-entry), [MEM-RTE-native-capture](#mem-rte-native-capture). Individual provider parsers, attachment decoding and connector generation internals remain uninspected; completeness of native capture cannot be concluded. |
| Pending interaction overlay and published interaction read-back | Direct `src/docmason/interaction.py`, `src/docmason/routing.py`, `src/docmason/retrieval.py` | [MEM-OBJ-interaction-policy](#mem-obj-interaction-policy), [MEM-RTE-interaction-promotion](#mem-rte-interaction-promotion), [RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools). Pending evidence has a route before publication, but not for every query domain. |
| Duplicate repair, orphan pruning, source-reference repair and suppression | Direct `src/docmason/interaction.py`, `src/docmason/ask.py`; supplied publication pruning | [MEM-RTE-interaction-promotion](#mem-rte-interaction-promotion), [MEM-RTE-native-capture](#mem-rte-native-capture), [RT-OBJ-publish-pointer](runtime.md#rt-obj-publish-pointer). Suppression is not universal withdrawal of published content. |
| Later-turn work brief and advisory context | Direct `src/docmason/work_experience.py`, `src/docmason/hooks.py`; supplied ask/hook records | Annotations on [RT-OBJ-canonical-turn](runtime.md#rt-obj-canonical-turn) and [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks). No deployed host window management is inspected. |
| Runtime review, projections and candidate extraction | Direct `src/docmason/projections.py`, `src/docmason/review.py`, `skills/canonical/runtime-log-review/SKILL.md` | [MEM-OBJ-benchmark-candidates](#mem-obj-benchmark-candidates), [MEM-RTE-review-projection](#mem-rte-review-projection). Projection scheduler recovery and answer-history consumers not fully traced; no complete projection freshness guarantee. |
| Candidate promotion, baselines and later suite consumption | Direct candidate-promotion branch in `src/docmason/operator_eval.py`; supplied evaluator wiring | [RT-RTE-operator-eval](runtime.md#rt-rte-operator-eval), [MEM-OBJ-benchmark-candidates](#mem-obj-benchmark-candidates). No live judge, successful replay or production improvement evidence. |
| Adapter projection and core update | Supplied runtime only | [RT-RTE-adapter-sync](runtime.md#rt-rte-adapter-sync), [RT-RTE-core-update](runtime.md#rt-rte-core-update). Actual host reload and released bundle provenance remain unobserved. |

## Core ideas

1. **Published evidence is a layered file surface, not just summaries.** Extracted text, structure and renders remain reachable beside bilingual semantics, citations, overlays and derived channel descriptors. Validation constructs reader indexes from accepted contexts; retrieval selects a small subset for host inspection. Physical evidence and derived assertions have different lineage and consumers ([MEM-OBJ-source-evidence](#mem-obj-source-evidence), [MEM-OBJ-knowledge-text](#mem-obj-knowledge-text), [MEM-OBJ-reader-index](#mem-obj-reader-index)).
2. **Conversation capture and knowledge publication are separate admissions.** Reconciliation writes entries and pending reader artifacts without waiting for publication. Sync groups eligible entries, preserves turn evidence, creates conservative semantics when enabled, validates and publishes. Canonical ask self-capture and degraded operator evidence have suppression paths. Neither native capture nor the word `promoted` establishes canonical answer ownership ([MEM-RTE-native-capture](#mem-rte-native-capture), [MEM-RTE-interaction-promotion](#mem-rte-interaction-promotion)).
3. **Memory labels change deterministic reader behavior, but are not truth certificates.** Query domain, source scope, participation mode, lexical overlap and memory rank priors decide inclusion and ranking. `confirmed` can be a structured fallback rather than corroboration. Pending and promoted material retain interaction provenance; publication does not turn it into source-authored fact ([MEM-OBJ-interaction-policy](#mem-obj-interaction-policy)).
4. **Trace-derived candidates change a later evaluator only after a separate request.** Review filters and groups runtime evidence into candidate cases. Explicit promotion appends regression cases; later suite execution consumes them. This is a retained trace-to-evaluation path, not automatic prompt or code revision, and not demonstrated learning ([MEM-RTE-review-projection](#mem-rte-review-projection), [RT-RTE-operator-eval](runtime.md#rt-rte-operator-eval)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-source-evidence
Label: Staged and published source evidence

Part of: [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish)

This object is the retained evidence product inside the supplied build/publication route, not a duplicate of its progression or of the publish pointer. Source manifests and evidence-unit IDs are symbolic lineage/access metadata; extracted text is natural-language content, and renders/media are inspectable source representations interpreted by the host. They live in staged source directories and the selected published tree. Their lineage is document discovery and deterministic parsing/rendering, including derived email attachment sources in the supplied boundary. Initial corpus choice belongs to the operator or shipped sample driver; byte copying is not per-assertion approval. Exact private-document authorship and user installation control are unavailable.

Later retrieve/trace operations select index records and referenced text, structure or render assets. The host interprets evidence; Python interprets identifiers and paths. These are knowledge inputs, not executable instructions with enforced authority over the host. SRC-1, `src/docmason/knowledge.py`, `src/docmason/retrieval.py`, `skills/canonical/knowledge-construction/SKILL.md`.

> - rendered assets referenced by the evidence manifest
> --- `skills/canonical/knowledge-construction/SKILL.md`

The supplied [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish) establishes staging and publication admission. Content fidelity and every parser-specific representation remain uninspected here.

#### MEM-OBJ-knowledge-text
Label: Bilingual source and interaction semantics

Part of: [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish)

The operative content is titles, bilingual summaries, key-point/claim statements, gaps and ambiguities in `knowledge.json` and `summary.md`, stored beside each staged/published source or interaction memory. These natural-language units receive their meaning through host interpretation. Citation IDs and support bindings are symbolic reader metadata covered separately by [MEM-OBJ-reader-index](#mem-obj-reader-index). This is the semantic product of the supplied publication route, not its state machine.

Lineage has two producers: conservative Python synthesis from bounded evidence snippets, and host-agent authoring requested by the canonical construction skill. Python's `autonomous` branch invokes a deterministic function, not a model call. In the interaction branch, the first extracted turn snippet shapes the summary/key point; a separate generated statement preserves interaction provenance. Neither producer is evidence that every original reason survives the summary. Host authoring may retain gaps and uncertainty, but actual compliance is unobserved. SRC-1, `src/docmason/knowledge.py`, `skills/canonical/knowledge-construction/SKILL.md`.

> def write_conservative_semantic_outputs(
>     source_dir: Path,
>     *,
>     active_source_ids: set[str],
> ) -> dict[str, Any]:
>     """Write a minimal but publishable knowledge object directly from staged evidence."""
> --- `src/docmason/knowledge.py`

> Write `knowledge.json` with the required bilingual fields and only cite real evidence-unit IDs from the matching source.
> --- `skills/canonical/knowledge-construction/SKILL.md`

Software admits or rejects through pending-synthesis checks and validation; the host proposes semantic enrichment and the main agent is prescribed to settle publication. Starting sync is not per-line human approval. Later index building reads these texts and retrieval delivers selected summaries to the host. Preservation across rebuilds copies prior authored files; preserved text alone is not evidence of re-grounding against changed input. See [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish).

#### MEM-OBJ-semantic-overlay
Label: Additive unit semantic overlay

Part of: [RT-RTE-hybrid-refresh](runtime.md#rt-rte-hybrid-refresh)

This is the persisted enrichment product inside the supplied hybrid route. Unit files under `semantic_overlay/` contain natural-language labels, annotations, relation descriptions and uncertainty notes, alongside symbolic artifact/unit IDs, covered/blocked slots, consumed-input references and source/unit fingerprints. Storage is staged/published JSON, not model weights. Authorship is requested of the host; the helper can normalize defaults and physically write files, while validation checks shape and references. The write helper is not itself the complete publication gate. SRC-1, `src/docmason/semantic_overlays.py`, `src/docmason/hybrid.py`, `src/docmason/knowledge.py`.

> def overlay_is_fresh(
>     payload: dict[str, Any],
>     *,
>     source_fingerprint: str,
>     unit_evidence_fingerprint: str,
> ) -> bool:
>     """Return whether one overlay still matches the current deterministic substrate."""
>     return (
>         payload.get("source_fingerprint") == source_fingerprint
>         and payload.get("unit_evidence_fingerprint") == unit_evidence_fingerprint
>     )
> --- `src/docmason/hybrid.py`

Coverage evaluation gives stale overlays no covered-slot credit. Separately, the inspected generic overlay loader loads files by unit ID, and retrieval converts their strings into search text. Do not infer a universal read-time stale-content exclusion from the coverage checker. Preserving overlay directories on rebuild and subsequent settlement require the integration qualification below. Reasons/uncertainty can persist, but retrieved label projections need not deliver all consumed-input detail to the host.

#### MEM-OBJ-reader-index
Label: Retrieval and provenance reader indexes

These symbolic JSON artifacts hold source/unit/artifact records, graph edges, provenance lookups and citation/consumer mappings, plus copied natural-language search strings. Storage is target-local retrieval/trace directories; the pending interaction overlay supplies analogous runtime-local artifacts. Fixed Python rules consume identifiers, metadata and scores; the host interprets selected text. Numeric scores here are localized symbolic ranking values, not distributed-parametric learned representations. SRC-1, `src/docmason/retrieval.py`, `src/docmason/knowledge.py`, `src/docmason/affordances.py`, `src/docmason/interaction.py`.

Distinct from [RT-OBJ-publish-pointer](runtime.md#rt-obj-publish-pointer): the pointer selects a root; indexes select evidence within it. Distinct from [RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools): these are retained reader inputs, not the reader invocation. The published lineage is validated source contexts to records; incremental builds reuse unaffected records and filter inactive IDs. Pending artifacts instead derive directly from eligible interaction entries. Baseline `derived_affordances.json` provides channel/access descriptions; requested host enrichment is explicitly derived, not source-authored fact.

> if not pending_synthesis and not blocking_errors:
>     retrieval_manifest = build_retrieval_artifacts(
> --- `src/docmason/knowledge.py`

Index generation admits through software checks, not direct human selection of every record. Public readers and answer tracing reload these artifacts; retrieval sessions/trace records retain selections for later canonical closure and review. These artifacts mediate access and support diagnostics, not factual correctness. Cache and incremental correctness are not exhaustively audited.

#### MEM-OBJ-native-ledger
Label: Native turn ledger and transcript cursor

The ledger is persisted JSON under `runtime/state/native-ledger/`; transcript mirrors/cursors are interaction-ingest capture state. Ledger user/assistant excerpts are natural-language trace content; identity, closure, reconciliation, audit and promotion fields are symbolic bookkeeping. Cursors retain offsets/checksums and a provider-specific tail for incremental parser recovery. These are raw or normalized trace records rather than learned semantic advice. SRC-1, `src/docmason/interaction.py`, `src/docmason/project.py`.

Distinct from [RT-OBJ-canonical-turn](runtime.md#rt-obj-canonical-turn): native turns can exist without canonical ownership. Distinct from [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks): the ledger is retained capture, not the optional advisory delivery path. Direct reconciliation upserts ledger turns and interaction entries; review later reads native ledgers. The cursor's tail compaction keeps the last resumable native turn, not a model-generated summary of the host's window.

> """Keep only the records required to resume the last native turn."""
> --- `src/docmason/interaction.py`

This quote concerns `_compact_transcript_tail`, not context eviction by the enclosing model runtime. Original provider processing and completeness of captured tool/assistant content remain uninspected.

#### MEM-OBJ-interaction-entry
Label: Captured and promoted interaction content

The entry's natural-language payload is user text, an assistant excerpt and referenced attachments under runtime interaction-ingest storage. Promotion produces extracted turn text/structure/assets and context in per-memory directories under staging/current interaction storage. The operative text is distinguished from the selection metadata in [MEM-OBJ-interaction-policy](#mem-obj-interaction-policy). SRC-1, `src/docmason/interaction.py`.

No supplied object has this referent: [RT-OBJ-canonical-turn](runtime.md#rt-obj-canonical-turn) expressly denotes control binding rather than conversation-memory content. [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish) overlaps the promotion endpoint, not the whole pending-to-promoted object lifecycle.

> "user_text": user_text,
> "assistant_excerpt": assistant_excerpt[:500],
> "attachment_ids": [
> --- `src/docmason/interaction.py`

Promotion groups pending entries by conversation and derives a memory ID from their entry IDs. It preserves each unit's user text plus the bounded assistant excerpt, attachment copies and linkage. Suggested summaries take at most the first five entries and truncate each user fragment to 220 characters; conservative semantics additionally select snippets. Thus durable evidence is richer than the displayed summary but not the full assistant transcript. Stored identifiers allow later tracing; they do not establish delivery of omitted reasons.

> for entry in entries[:5]:
>     if not isinstance(entry, dict):
>         continue
>     user_text = " ".join(str(entry.get("user_text", "")).split())
>     if user_text:
>         fragments.append(user_text[:220])
> --- `src/docmason/interaction.py`

Pending readers can consume derived entry records before sync; published readers load admitted memory contexts after semantic files exist. These are interaction-derived knowledge/context inputs, not source-authored corpus authority. Trace-fed transformation is wired; exercised learning or improved future capacity is uninspected.

#### MEM-OBJ-interaction-policy
Label: Interaction selection and support metadata

Symbolic fields in entries, source manifests, interaction contexts and reader records encode `memory_kind`, `durability`, `uncertainty`, `answer_use_policy`, rank prior, family/trust tier and pending status. They share file storage with [MEM-OBJ-interaction-entry](#mem-obj-interaction-entry) but have a distinct fixed-rule consumer: query participation/ranking. No supplied object separately denotes these fields. SRC-1, `src/docmason/routing.py`, `src/docmason/interaction.py`, `src/docmason/retrieval.py`.

Entry semantics honor structured hints when supplied to the inference helper; native entry persistence uses continuation type and tool audit instead. Constraint updates become constraints; command activity can become operator intent; the residual default is working note. Group promotion selects priority metadata and aggregates uncertainty. These are implemented transformations with software admission, not proof that a human confirmed the content.

> elif memory_kind == "working-note":
>     uncertainty = "inferred"
> else:
>     uncertainty = "confirmed"
> --- `src/docmason/routing.py`

At retrieval, external-factual queries exclude interaction records; workspace-corpus minimal mode excludes them too. Other modes apply lexical thresholds and rank bonuses. `contextual-only` affects thresholds/bonuses in this inspected selector rather than serving as a blanket ban on all support use. Downstream trace/admissibility semantics need their own assessment.

> if question_domain == "external-factual":
>     return False, 0.0
> if question_domain == "workspace-corpus" and mode == "minimal":
>     return False, 0.0
> --- `src/docmason/retrieval.py`

Durability labels alone establish no implemented time-to-live or automatic expiration. Promotion preserves interaction family/trust tier rather than upgrading the material to authored-document status.

#### MEM-OBJ-benchmark-candidates
Label: Derived runtime review and benchmark candidates

Symbolic review/candidate JSON under runtime log review storage retains questions, case IDs, linked sessions/traces, expected-state suggestions, reasons, priorities, feedback matches and support summaries. The question/reason text remains natural-language material for operators; fixed promotion/evaluation consumers interpret case fields. Lineage is captured conversations and tool traces, filtered/grouped into review projections, then optionally explicit regression admission. SRC-1, `src/docmason/projections.py`, `src/docmason/review.py`, `src/docmason/operator_eval.py`, `skills/canonical/runtime-log-review/SKILL.md`.

Distinct from [RT-RTE-operator-eval](runtime.md#rt-rte-operator-eval): these are its retained candidate inputs, whose automatic production precedes the operator's promotion request. No counterpart object is declared in runtime.

> write_json(paths.benchmark_candidates_path, build_benchmark_candidates(paths, summary=summary))
> --- `src/docmason/projections.py`

Candidates preserve reasons and raw-artifact links for deeper inspection. Their later consumer is the review host and explicit candidate-promotion code; promoted cases feed later suites. Candidate suggestions are not accepted product changes or proof of content-directed theory criticism.

### Routes

#### MEM-RTE-native-capture
Label: Native transcript capture and suppression

Native provider reconciliation, reached by ask preparation or command-context reconciliation, parses available turns, derives audits/classifications, stores attachments, persists entries and upserts the ledger, then refreshes pending reader artifacts and queues projections. Producer/admission owner is Python; raw user and host output supply content, but generic capture does not establish human approval of derived entry semantics. This route is distinct from [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks), which supplies optional event/advisory plumbing, and from [RT-RTE-canonical-ask](runtime.md#rt-rte-canonical-ask), whose preparation can invoke this capture.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Reconciliation status, ledger identity, captured interaction IDs and pending-overlay state.
- Later read-back: Later current-target retrieve/trace calls can merge pending entry artifacts; review consumes native ledger and log projections; sync consumes eligible entries.
- Delegated visibility: uninspected — actual host parsing and delegated context delivery are external; captured entries contain only bounded excerpts and attachment references.
- Selection predicate: Native turns with valid IDs and user text or attachments; degraded operator evidence is not promotable. Ask suppresses its latest captured entry as canonical self-capture unless the reusable canonical-turn branch returns first.
- Invalidation or expiry: Reconciliation upserts existing entries; suppression sets audit-only status and refreshes the overlay. Already-promoted entries are skipped by suppression; no general TTL is established.
- Activation or effect: Makes derived pending evidence available to later readers and queues review projections; changed host behavior is unobserved.
- Evidence limits: Capture is not canonical ownership, factual validation, guaranteed complete transcript retention or observed recall.

SRC-1, `src/docmason/interaction.py`, `src/docmason/ask.py`, `src/docmason/commands.py`. Structured fallback guidance shapes derived metadata, not a retained learned rule. Software can exclude degraded evidence and self-capture; user initiation is not per-entry approval. There is no independent expected-answer oracle; mode is capture during open requests/operator activity. Recovery includes stable-ID upsert and cursor replay, not a demonstrated crash-safe transaction across every artifact.

> promotable = not (
>     isinstance(operator_evidence, dict)
>     and operator_evidence.get("status") == "degraded"
> )
> --- `src/docmason/interaction.py`

> reason="canonical-ask-self-capture",
> --- `src/docmason/ask.py`

#### MEM-RTE-interaction-promotion
Label: Interaction evidence promotion and maintenance

Part of: [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish)

This route is the interaction-specific transformation inside the supplied sync container. Python repairs duplicates/orphans, groups pending entries, writes merged evidence/context/work items, reuses matching complete digests or preserves previous semantics, and retains prior published groups with surviving backing entries. Conservative semantic authoring or host completion then supplies semantic files; validation/publication controls reader admission. Successful publication marks entries promoted and rebuilds the pending overlay. SRC-1, `src/docmason/interaction.py`, `src/docmason/knowledge.py`, `skills/canonical/knowledge-construction/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Interaction manifest/counts and pending semantic work; successful publication reports promoted-entry counts.
- Later read-back: Validation builds published reader records from loadable interaction contexts; later retrieve/trace operations reload those records and referenced evidence. Subsequent sync can copy surviving prior memories.
- Delegated visibility: Bounded construction instructions expose assigned memory manifests, context, extracted evidence and attachments; actual delegated window enforcement is uninspected.
- Selection predicate: Pending-promotion flag, conversation grouping, stable input digest and contract completeness; active source IDs prune related-source links. Publication requires valid/warnings in the supplied sync route.
- Invalidation or expiry: Missing backing entries can orphan-prune a memory; duplicate repair merges entries; changed digest forces evidence rebuilding; deleted source references are repaired. Any surviving entry can retain a prior published memory; suppression does not withdraw already-promoted content.
- Activation or effect: Published interaction records become selectable later; promotion removes corresponding pending overlay participation. Host behavioral effects remain unobserved.
- Evidence limits: Publication checks structure/bindings, not truth of captured statements or complete retention of reasons. Not a universal withdrawal or rollback facility.

Software proposes grouping and conservative content; the host can propose semantic text. Software validation can block, and disabled conservative authoring can leave pending work. The supplied sync approval route governs execution, not human approval of every memory assertion. Mode is maintenance of accumulated interaction evidence; no independent answer oracle. Guidance preserves provenance/uncertainty. Raw turns become bounded evidence units, suggested summaries and semantic outputs, then later reader inputs: this is a trace-fed retained transformation, not merely a log append. No model parameter update or improved capacity is established.

> if not any(
>     _interaction_entry_path(paths, interaction_id).exists()
>     for interaction_id in interaction_ids
> ):
>     import shutil
>
>     shutil.rmtree(memory_dir)
> --- `src/docmason/interaction.py`

The orphan check is deliberately only an existence test. It does not prove that removed or edited individual turns disappear from a surviving merged memory. Maintenance can prune the current tree before a new publication; it is not solely immutable-snapshot replacement.

#### MEM-RTE-review-projection
Label: Runtime review projection and candidate selection

Changes in canonical/captured/tool state queue projection refresh; rebuilding copies live conversation views, removes dead projection mirrors, derives review summaries, candidates and answer history. Explicit runtime-log-review refresh/read delivers those outputs to the main host. This is distinct from [RT-RTE-operator-eval](runtime.md#rt-rte-operator-eval): it selects candidate inputs, while that route admits selected cases and consumes suites. SRC-1, `src/docmason/projections.py`, `src/docmason/review.py`, `src/docmason/commands.py`, `skills/canonical/runtime-log-review/SKILL.md`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Review summary, candidate suggestions and request-level audit linkage; background refresh writes projections.
- Later read-back: Later operator review reads derived summaries and follows referenced raw logs; explicit promote-candidate loads selected candidates and appends regression cases for later suite runs.
- Delegated visibility: Review skill requests a concise main-agent summary and referenced case IDs; actual host-side delegation is uninspected.
- Selection predicate: Grouped runtime records and feedback; render-needed/unresolved outcomes, ambiguity, unexplained mixed support or explicit feedback can admit candidates. Recency/priority ordering is capped by RECENT_LIMIT; synthetic traffic is distinguished from real canonical activity.
- Invalidation or expiry: Derived views can be regenerated; removed live conversation files remove projection mirrors. Independent retention/cleanup of raw logs, promoted cases and answer history is not fully traced.
- Activation or effect: Changes later review inputs and, following explicit promotion, future evaluator cases; does not itself mutate production prompts, skills or overlays.
- Evidence limits: Suggestions, scores and retained reasons do not establish factual criticism, successful learning or exercised self-improvement. Worker scheduling/freshness and actual replay are unobserved.

Software proposes/filter-ranks candidates from traces; an operator request selects promotion IDs, but generic request files do not establish human authorship or per-content approval. Missing IDs are rejected; duplicate case IDs are skipped by the supplied evaluation route. Replay uses suite expectations and optional references/judge inputs, not a new oracle created by candidate mining. Operating modes are descriptive review followed optionally by bounded regression evaluation. Recovery is regeneration and explicit case/baseline maintenance; transactional rollback across all evaluator writes is uninspected.

> Keep the workflow descriptive and review-oriented. Do not mutate prompts, skills, overlays, or benchmarks from inside this workflow.
> --- `skills/canonical/runtime-log-review/SKILL.md`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-OBJ-canonical-turn](runtime.md#rt-obj-canonical-turn)

Memory-specific read-back includes explicitly anchored later-turn work briefs, decision gates and accepted scopes, not merely the ordinary current-run control state. `normalize_work_brief` merges host-authored deltas into the prior brief; continuation resolution requires exact `revision_of` or open gate identity rather than adjacency. Natural-language brief content is interpreted by the host; Python owns symbolic identities/legality. User decision resolution is separate from semantic authorship. SRC-1, `src/docmason/work_experience.py`, `src/docmason/ask.py`.

> Content strategy remains agent-owned.  The deterministic runtime validates and
> merges the explicit projection; it must not replace professional framing with a
> keyword router.
> --- `src/docmason/work_experience.py`

Persistence reaches later linked turns on the same task; cross-task reuse of every brief is not established. Raw task evidence and retained gates are not automatically source facts.

#### On [RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools)

Reader input is published source/unit/artifact records plus graph edges and optional pending overlay, not the complete stored corpus. Domain/memory-profile/source-scope checks gate pending merging on current-target queries; workspace minimal mode excludes interaction candidates. Unbound direct retrieval with no domain can admit pending material, so a claim that every memory read requires published KB admission would be false. SRC-1, `src/docmason/retrieval.py`.

> if question_domain == "composition":
>     return True
> if question_domain == "workspace-corpus":
>     if not isinstance(memory_profile, dict):
>         return True
>     return str(memory_profile.get("mode") or "minimal") != "minimal"
> return question_domain is None
> --- `src/docmason/retrieval.py`

Selection uses query, explicit/inherited source IDs, lexical-plus-graph ranking, document type and channel evidence requirements. Public CLI defaults are five source bundles and one graph hop, not a model-token budget. `--include-renders` returns references, not proof of visual inspection. Compact projection retains title/summary, family/trust/uncertainty/policy, score, matched IDs and render/focus references while dropping nested units/artifacts. The host can inspect external full files selectively; delivered IDs are reload handles, not by-reference objects in its window. SRC-1, `src/docmason/cli.py`, `src/docmason/commands.py`.

Requested tool delivery is pull read-back. Logging a session/trace retains raw selection/support outcomes; later finalization and review are separate consumers. Public source/session/answer tracing has alternative identifier/file-based entry points; this is provenance lookup, not necessarily content-targeted recall. Exact activation and host use are unobserved.

#### On [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks)

Prompt submission can automatically select the latest linked canonical turn, open gate options and accepted scope IDs, then deliver an advisory text reminder through host additional context. Trigger/selector are event and bound state, not an independent model memory-search call. No numeric token budget is established in the inspected reminder constructor. This is push read-back of changed task state. SRC-1, `src/docmason/hooks.py`.

> "DocMason continuation state (advisory; ignore for unrelated requests): "
> f"the latest linked canonical turn is `{turn_id}`. Use this exact id as "
> "`revision_of` only when the user explicitly revises that work."
> --- `src/docmason/hooks.py`

The later consumer is the host's next prompt invocation. Delivery is wired; optional activation and behavioral effect are unobserved. Stop reminders concern bounded same-turn recovery, not unrestricted unsolicited knowledge injection.

#### On [RT-RTE-hybrid-refresh](runtime.md#rt-rte-hybrid-refresh)

Authored work packets constrain the context/writes to assigned sources, units, focus renders and queued hard artifacts. Guidance says to retain uncertainty and consumed inputs and not rewrite deterministic sidecars. Main-agent integration remains separate. This resembles an isolated work frame only if the external host actually supplies a separate window; source instructions establish selected work scope, not frame isolation or automatic eviction. SRC-1, `skills/canonical/knowledge-construction/SKILL.md` and the supplied route's passages.

Overlay freshness is established for coverage credit, not every reader path. Rebuild preservation and generic loading require the integration issue retained below.

#### On [RT-RTE-operator-eval](runtime.md#rt-rte-operator-eval)

Retained candidate drafts contain candidate evidence, proposed case and operator notes. Promotion appends cases to regression suite JSON; subsequent suite execution reads current corpus, cases and selected baselines. Reasons survive in draft/candidate material; automatic use of every reason in later evaluation policy is not established. SRC-1, `src/docmason/operator_eval.py`, with suite consumption supplied by the runtime record.

> "candidate": candidate,
> "proposed_case": _draft_case_from_candidate(paths, candidate),
> "operator_notes": request.get("operator_notes"),
> --- `src/docmason/operator_eval.py`

This is trace-derived evaluator-state adoption after explicit selection. It does not demonstrate that production behavior changed, that capacity improved, or that a reflective theory-building loop criticized and revised its method text.

## Write side

Document acquisition is operator corpus placement or the included sample driver. Python builds physical artifacts and source metadata; conservative semantic synthesis and host-authored enrichment are separate producers. Generic caller identity does not resolve initial human control of every document. Later software transforms evidence into summaries, citation bindings, affordances and indexes; known transformations remain supported despite unresolved initial provenance ([MEM-OBJ-source-evidence](#mem-obj-source-evidence), [MEM-OBJ-knowledge-text](#mem-obj-knowledge-text), [MEM-OBJ-reader-index](#mem-obj-reader-index)).

Validation blocks pending synthesis or blocking errors; valid/warnings admit publication through the supplied sync route. Main-agent sign-off is authored policy; the executable admission branch belongs to Python. Preservation copies prior semantic files/overlays, and structural repair can normalize metadata; this is not evidence that a host freshly reconsidered their meaning. Published current-root pruning removes old physical roots, while the ledger is logical history rather than complete old corpus rollback ([RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish), [RT-OBJ-publish-pointer](runtime.md#rt-obj-publish-pointer)).

Native traces follow a different admission: raw/normalized ledger and bounded entry payload become pending reader records, then optionally grouped evidence and published semantics. Degraded operator capture and canonical ask self-capture can remain audit-only. Suppression skips promoted entries; orphan cleanup requires no surviving backing entry, so partial deletion does not establish unit-level withdrawal. The promotion builder also repairs related-source links and can copy prior groups. There is no basis to promise a universal forget operation ([MEM-RTE-native-capture](#mem-rte-native-capture), [MEM-RTE-interaction-promotion](#mem-rte-interaction-promotion)).

Runtime projection is another automatic trace-fed transformation. It retains review reasons and candidate evidence, but later regression adoption requires selected IDs in an explicit evaluation request. Review guidance itself forbids production mutations. Raw logs alone are not learned behavior; this trace-to-candidate-to-suite path reaches a real later consumer without establishing improved capacity or automatic self-revision ([MEM-RTE-review-projection](#mem-rte-review-projection), [RT-RTE-operator-eval](runtime.md#rt-rte-operator-eval)).

## Read-back

The main knowledge route is requested retrieval/trace followed by host inspection and interpretation. Published records mediate selection rather than pushing the whole KB. Pending interaction read-back is an alternate conditional merge; it is not universally subordinated to publication. Both paths expose provenance/trust/uncertainty metadata and bounded text. That metadata changes deterministic ranking/participation, while the host retains responsibility for treating text as evidence rather than obeying it as instruction ([RT-RTE-evidence-tools](runtime.md#rt-rte-evidence-tools), [MEM-OBJ-interaction-policy](#mem-obj-interaction-policy)).

Later linked ask invocations reload explicit task state; optional prompt hooks independently push selected continuation reminders. Task identity is meaningful targeting for that state route, whereas a direct trace identifier simply requests a particular persisted record. Review and evaluation have separate later consumers and selection policies, not a generic host-wide memory store ([RT-OBJ-canonical-turn](runtime.md#rt-obj-canonical-turn), [RT-RTE-host-hooks](runtime.md#rt-rte-host-hooks), [MEM-RTE-review-projection](#mem-rte-review-projection)).

Working-context control is mainly authored selective inspection and compact tool output. Code omits heavy nested evidence from compact projections but keeps IDs/references for later file reads. It does not evict previously delivered content from the host window. Read-only side research is prescribed in [RT-BAP-canonical-skills](runtime.md#rt-bap-canonical-skills); actual separate frames, their input/tail retention and return isolation remain uninspected. The frame analogy fits bounded work packets only at the level of scoped inputs/returns; it cannot establish host isolation. The heap analogy also stops at file handles: text already delivered remains by value, and an ID becomes useful only through a new read. Transcript cursor-tail compaction is parser checkpointing, not model-window summarization ([MEM-OBJ-native-ledger](#mem-obj-native-ledger)). No total token budget, native model compaction policy or provider-cache recall guarantee is established.

## Integration issues

- **No supplied fact is replaced.** Added interaction-specific records refine the supplied runtime rather than negate its stated provisional limits. The new promotion route is explicitly part of [RT-RTE-sync-publish](runtime.md#rt-rte-sync-publish); source evidence, semantic text and overlays are declared as products of their supplied route containers. No possible duplicate of an existing operative-object referent remains after comparison. [MEM-RTE-review-projection](#mem-rte-review-projection) supplies inputs to, but is not identical to, [RT-RTE-operator-eval](runtime.md#rt-rte-operator-eval).
- **Freshness credit is not universal stale-content exclusion.** SRC-1 `src/docmason/hybrid.py` withholds coverage credit for mismatched fingerprints; `src/docmason/knowledge.py` preserves overlay directories across rebuilds; `src/docmason/semantic_overlays.py` loads files by unit ID and `src/docmason/retrieval.py` projects their strings. These support a narrower freshness claim than universal stale-content quarantine. Whether every intervening settlement path removes or excludes stale text remains unresolved; prevent a system-wide freshness guarantee for [MEM-OBJ-semantic-overlay](#mem-obj-semantic-overlay) and [RT-RTE-hybrid-refresh](runtime.md#rt-rte-hybrid-refresh).
- **Withdrawal is partial.** SRC-1 `src/docmason/interaction.py` suppression skips promoted entries and orphan pruning retains groups with any surviving entry. Partial backing-entry edits/deletion do not by themselves prove unit-level withdrawal from published memory. Current-tree maintenance can prune outside a new publication. These limits concern [MEM-RTE-interaction-promotion](#mem-rte-interaction-promotion), [MEM-OBJ-interaction-entry](#mem-obj-interaction-entry) and the supplied [RT-OBJ-publish-pointer](runtime.md#rt-obj-publish-pointer); the pointer record does not imply an immutable selected tree.
- **Support labels require consumer-specific interpretation.** SRC-1 `src/docmason/routing.py` can default uncertainty to confirmed, and `src/docmason/retrieval.py` uses contextual-only in thresholds/bonuses. Neither is universal corroboration or a complete support-use prohibition. This report establishes selection, not every downstream trace/admissibility interpretation. Retain that scope for [MEM-OBJ-interaction-policy](#mem-obj-interaction-policy) and [RT-CLM-commit-gate](runtime.md#rt-clm-commit-gate).
- **Opaque or uninspected alternatives remain local.** Provider parser completeness, all attachment/connector variants, projection scheduling/freshness, answer-history reuse, cache invalidation combinations and every parser-specific source representation are not fully audited. Available source is not an access gap. These omissions prevent exhaustive capture, freshness, fidelity and all-consumer guarantees without negating the wired paths above. Actual host context isolation/compaction and benefit remain external/unobserved.

## Limitations and checks

The frozen checkout's HEAD was rechecked as f3970939593194a158ab7ea1d49995f06cbccc86 with no working-tree changes reported. Source identity and repeated run fields equal the supplied boundary/run. Evidence is implementation plus doctrine/design from SRC-1; no target program, test, example, model, hook or service was executed. Newly inspected paths are named in the coverage table; supplied runtime findings are explicitly distinguished.

Negative searches are not promoted to evidenced absences. Small structured labels, durable files and later reader wiring establish retained transformation and afforded behavior-shaping inputs, not improved future capacity. Host adherence, actual activation, successful memory use, causal benefit, autonomous criticism and exercised self-improvement remain unobserved or uninspected at their respective boundaries.

Validation: the required `commonplace-run validate-output` check passed after expanding one ambiguous excerpt attribution. It checks output form, identity, record relations and quotation occurrence, not claim support or acceptance.
