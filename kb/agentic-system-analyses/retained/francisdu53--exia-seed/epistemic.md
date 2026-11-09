---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "EXIA SEED epistemic routes: conversational acquisition, lexical vetoes, temporal checks, summaries, withdrawal and benchmark judging."
run-id: AAS-2026-11-07-exia-seed-804e805b7a8d-01
reviewed-boundary: c7497ac96da20bd1818096e35a59b6c0237f9730
---

# EXIA SEED epistemic report

## Source-and-claim boundary

The question is what licenses reliance on retained conversational content, as distinct from making it available to a later assistant. Scope and exclusions are those of [the boundary](boundary.md#boundary-and-evidence); evidence identities come from its [Source register](boundary.md#source-register). SRC-1 supplies implementation, doctrine/design and reported operation, not an observed run or causal experiment. No target execution was performed.

EXIA SEED imports speakers' statements and notes, asks a model to turn them into subject facts, applies lexical and temporal vetoes, stores the survivors and retrieves selected material. These checks supply limited operational admission, not a source-truth oracle. The public documentation itself acknowledges this distinction. Claims are [RT-CLM-citation-control](runtime.md#rt-clm-citation-control), [EPI-CLM-cited-memory](#epi-clm-cited-memory) and [EPI-CLM-summary-grounding](#epi-clm-summary-grounding).

The supplied runtime is provisional but its principal route findings remain usable. Added direct inspection finds a consequential withdrawal qualification: graph reconstruction removes withdrawn raw references, but still appends the fact text. This is not a correction of the runtime's explicitly narrower statement that withdrawal does not erase prior page prose; it extends that finding through a downstream consumer ([EPI-RTE-withdrawal-read](#epi-rte-withdrawal-read)). No supersession is needed.

### Coverage

“Supplied” means the runtime record, including its retained passages, supplies evidence; it does not mean this analyst reread the complete file. “Direct” names this analyst's additional reads/searches in SRC-1. An available uninspected branch is not absent.

| Entry point or operation | Source path | Coverage and records | Limit and prevented conclusion |
|---|---|---|---|
| Registration, hook dispatch, search/read/note tools, native-memory callback | `plugin/exia_seed/plugin.yaml`, `plugin/exia_seed/__init__.py`, `plugin/exia_seed/langues/en.py` | Direct manifest, tool dispatch/native callback and English schema/prompt reads; supplied initialization, capture and prefetch: [RT-RTE-conversation-ingest](runtime.md#rt-rte-conversation-ingest), [RT-RTE-register-admission](runtime.md#rt-rte-register-admission), [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery) | Hermès source is excluded; host dispatch order, actual context placement and compliance remain unknown. |
| Automatic subprocess, nightly and manual forced consolidation | `plugin/exia_seed/outils/consolider.py`, `plugin/exia_seed_consolider.sh`, `plugin/exia_seed/consolidation.py` | Direct CLI-entry search and consolidation source/check/write/withdrawal bodies; supplied caller trace: [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation), [EPI-RTE-fragment-check](#epi-rte-fragment-check), [EPI-RTE-time-check](#epi-rte-time-check) | No service calls or deployment traces; only wired routes are established. |
| Page addition, deduplication and persistence | `plugin/exia_seed/pages.py`, `plugin/exia_seed/consolidation.py` | Direct add/write and consolidation bodies: [EPI-OBJ-fragments](#epi-obj-fragments), [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation) | Normalized-text deduplication is not contradiction resolution. |
| Summary generation, checking and write-mode refresh | `plugin/exia_seed/fiches.py`, `plugin/exia_seed/outils/fiches.py` | Direct entire summary implementation and CLI-option search; supplied maintenance caller: [EPI-RTE-summary-proposal](#epi-rte-summary-proposal), [EPI-RTE-summary-check](#epi-rte-summary-check), [EPI-RTE-summary-write](#epi-rte-summary-write) | Model compliance with “general, not detail” remains unknown; old summaries survive failure. |
| Concept tagging, timestamp backfill, graph rebuild | `plugin/exia_seed/outils/concepts.py`, `plugin/exia_seed/outils/ancrer.py`, `plugin/exia_seed/outils/graphe.py`, `plugin/exia_seed/graphe.py` | Direct entry-point search, concept model-result/write body, graph page-reader and edge-construction bodies; supplied maintenance: [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance), [EPI-RTE-withdrawal-read](#epi-rte-withdrawal-read) | Full engine internals and learned lexical-field body not traced here; no system-complete semantic-quality or ranking-equivalence claim. |
| Recall, search, read-page, neighboring trails and cache reload | `plugin/exia_seed/rappel.py`, `plugin/exia_seed/requete.py` | Supplied [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery), [RT-BAP-recalled-content](runtime.md#rt-bap-recalled-content); direct graph input extraction | Distinct future/expiry filters and graph-timestamp cache invalidation remain consequential; no universal currentness or privacy guarantee. |
| LoCoMo preparation, response modes and judgment | `banc/locomo/preparer.py`, `banc/locomo/repondre.py`, `banc/locomo/juger.py` | Supplied replay; direct entire judge: [RT-RTE-benchmark-replay](runtime.md#rt-rte-benchmark-replay) | Reference answers license benchmark labels only; generated memories and datasets not frozen. |
| LongMemEval judge | `banc/longmemeval/juger_lme.py` | Direct entire body: [EPI-RTE-lme-judging](#epi-rte-lme-judging) | Semantic judgment is delegated to a mutable external model; no actual scores established. |
| Nexa copies and model/prompt comparison | `banc/nexa/reconsolider.py`, `banc/modeles/consolider.py` | Supplied [RT-RTE-benchmark-replay](runtime.md#rt-rte-benchmark-replay) | Private panels, generated runs and separate plugin copy unavailable; component causal effects and deployed improvements not established. |
| Other benchmark baselines, acceptance diagnostics, French prompt variants, tests and engineering documents | `banc/`, `tests/`, `plugin/exia_seed/langues/fr.py`, `docs/` | Included by boundary but not exhaustively inspected here; public claims read directly in `README.md` | This is not a system-complete negative about all evaluators, all language behavior or all maintenance paths. |

Missing host evidence prevents concluding that delivered instructions were obeyed. Missing model internals prevents claims about internal verification or parameter adaptation. Missing retained outputs with production provenance prevents identifying which proposed semantic transformations actually occurred. Missing experimental runs and comparisons prevents independent acceptance of reported benefits. These limits do not erase the inspected admission and delivery capacities.

## Epistemic-object inventory

| Object ID | Candidate truth-apt content or none | Claimed role | Evidence source ID and local anchor | Gap/limit |
|---|---|---|---|---|
| [EPI-OBJ-sources](#epi-obj-sources) | see record | see record | SRC-1 `plugin/exia_seed/consolidation.py` | see record |
| [EPI-OBJ-fragments](#epi-obj-fragments) | see record | see record | SRC-1 `plugin/exia_seed/pages.py` | see record |
| [EPI-OBJ-summaries](#epi-obj-summaries) | see record | see record | SRC-1 `plugin/exia_seed/fiches.py` | see record |
| [EPI-OBJ-keywords](#epi-obj-keywords) | none; symbolic selection words | see record | SRC-1 `plugin/exia_seed/fiches.py` | see record |
| [EPI-OBJ-concepts](#epi-obj-concepts) | see record | see record | SRC-1 `plugin/exia_seed/graphe.py` | see record |
| [EPI-OBJ-evaluations](#epi-obj-evaluations) | see record | see record | SRC-1 `banc/locomo/juger.py`, `banc/longmemeval/juger_lme.py` | see record |

External parametric components are separately characterized by [RT-CMP-consolidation-model](runtime.md#rt-cmp-consolidation-model) and [RT-CMP-benchmark-model](runtime.md#rt-cmp-benchmark-model). Their weights are not page memory; configured names do not pin exact weights or exclude endpoint changes. No parameter-update operation is shown by the inspected adapters; provider internals remain uninspected.

## Authority-route ledger

Each ledger row is a function, not a new declaration of the route it cites. Where one container performs several functions, rows separate those functions. “See record” delegates the remaining identity/evidence fields to the cited record; local classifications and bounded licenses below are this report's assessments.

| Route ID | Route function | Architectural status | Object/candidate ID | Content/update relation | Transition or check target | Evaluator/condition and domain | Activation and timing | Possible or observed result | Implemented force | Epistemic authority and scope | Operational authority: behavior permitted, blocked, or changed | Behavioral-authority path: consumer, channel, force, horizon | Evidence source ID and local anchor | Claim IDs or none | Mismatch marker or none | Gap/limit |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| [RT-RTE-conversation-ingest](runtime.md#rt-rte-conversation-ingest); [RT-RTE-register-admission](runtime.md#rt-rte-register-admission) | content transformation | implemented | [EPI-OBJ-sources](#epi-obj-sources) | truth-apt transformation: acquisition/import | Captured text/notes | see records | see records | Source text and speaker metadata retained | Source availability | Source truth unknown; masking/omission changes available evidence | see records | Consolidator; numbered lines; permissive input; later batch | SRC-1 `plugin/exia_seed/consolidation.py` | none | none | A note is not thereby human-confirmed. |
| [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation) | content transformation | implemented | [EPI-OBJ-fragments](#epi-obj-fragments) | truth-apt transformation: indeterminate | Statements to self-contained page proposals | Model request; open conversational domain | see record | Candidate facts, aliases, concepts and confidence | Proposal only until code veto | No semantic preservation or entailment established for arbitrary output | see record | Checker; JSON; candidate; current consolidation | SRC-1 `plugin/exia_seed/langues/en.py` | [RT-CLM-citation-control](runtime.md#rt-clm-citation-control) | none | Retelling, inference and error remain possible; provenance-linked outputs needed to classify actual edges. |
| [EPI-RTE-fragment-check](#epi-rte-fragment-check) | check/evidence production | implemented | [EPI-OBJ-fragments](#epi-obj-fragments) | no content change | see record | see record | see record | see record | Boolean and reason | Lexical admissibility only | Supplies veto input | see record | SRC-1 `plugin/exia_seed/consolidation.py` | [RT-CLM-citation-control](runtime.md#rt-clm-citation-control) | Lexical support is not entailment | see record |
| [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation) | disposition/acceptance | implemented | [EPI-OBJ-fragments](#epi-obj-fragments) | no content change | Fragment admission for page use | Code consumes lexical result; no per-fragment human approval | After parsing/check | Reject or proceed | Enforcing veto | Operational acceptance against named lexical criteria, not acceptance of ampliative truth | Rejected fragment skipped; input can still be marked processed | Page writer; checker Boolean; enforcing; this pass and later retrieval | SRC-1 `plugin/exia_seed/consolidation.py` | [RT-CLM-citation-control](runtime.md#rt-clm-citation-control) | none | JSON recovery does not strengthen checks; rejected fragments need not be retried. |
| [EPI-RTE-time-check](#epi-rte-time-check) | check/evidence production | implemented | [EPI-OBJ-fragments](#epi-obj-fragments) | truth-apt transformation: entailed derivation | see record | see record | see record | see record | Result/date-removal reason | Entailment only in the explicit calendar predicate, not event truth | see record | see record | SRC-1 `plugin/exia_seed/temps.py` | [RT-CLM-citation-control](runtime.md#rt-clm-citation-control) | Same-day shortcut, permissive weekday handling | see record |
| [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation) | retention | implemented | [EPI-OBJ-fragments](#epi-obj-fragments) | truth-apt transformation: non-ampliative reshaping | Admitted text/metadata to pages | Code; alias routing, normalized duplicate test | After checks | Page files and progress journals | Durable availability | Retention adds no truth warrant | Existing duplicate omitted; new fact appended | Page reader; Markdown; permissive; future invocations | SRC-1 `plugin/exia_seed/pages.py` | [EPI-CLM-cited-memory](#epi-clm-cited-memory) | none | Contradictory statements can coexist; failures are not atomic rollback. |
| [EPI-RTE-summary-proposal](#epi-rte-summary-proposal) | content transformation | implemented | [EPI-OBJ-summaries](#epi-obj-summaries) | truth-apt transformation: indeterminate | see record | see record | see record | see record | Proposal | Requested compression does not establish faithful reshaping | see record | see record | SRC-1 `plugin/exia_seed/fiches.py` | [EPI-CLM-summary-grounding](#epi-clm-summary-grounding) | Bounded excerpt versus “entire page” | see record |
| [EPI-RTE-summary-check](#epi-rte-summary-check) | check/evidence production | implemented | [EPI-OBJ-summaries](#epi-obj-summaries) | no content change | see record | see record | see record | see record | Lexical veto input | Name/number/path/length conditions only | see record | see record | SRC-1 `plugin/exia_seed/fiches.py` | [EPI-CLM-summary-grounding](#epi-clm-summary-grounding) | No general truth or permanence check | see record |
| [EPI-RTE-summary-write](#epi-rte-summary-write) | disposition/acceptance | implemented | [EPI-OBJ-summaries](#epi-obj-summaries) | no content change | see record | see record | see record | see record | Enforcing check/write switch | Operational admission for topic identification, not truth acceptance | see record | see record | SRC-1 `plugin/exia_seed/fiches.py` | [EPI-CLM-summary-grounding](#epi-clm-summary-grounding) | none | see record |
| [EPI-RTE-summary-write](#epi-rte-summary-write) | retention | implemented | [EPI-OBJ-summaries](#epi-obj-summaries) | no content change | Checked summary to header | see record | see record | see record | Retained metadata | No additional warrant | see record | see record | SRC-1 `plugin/exia_seed/fiches.py` | none | none | No epistemic acceptance implied by persistence. |
| [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance) | operational admission/selection/consumption | implemented | [EPI-OBJ-concepts](#epi-obj-concepts) | non-truth-apt policy/content update: concept labels and retrieval vocabulary | Fact-to-concept assignment | Model/seed proposes; code known-concept and count filter | Explicit write mode | Tags/thesaurus; timestamps and graph on separate commands | Enforcing structural admission; downstream ranking | Concept association does not verify the tagged proposition | see record | Graph/retriever; tags and symbolic weights; ranking; later reconstruction | SRC-1 `plugin/exia_seed/outils/concepts.py` | none | none | Seed origin and semantic appropriateness unresolved. |
| [EPI-RTE-withdrawal-read](#epi-rte-withdrawal-read) | lineage/freshness/recovery | implemented | [EPI-OBJ-fragments](#epi-obj-fragments) | no content change | see record | see record | see record | see record | Removes selected provenance edges, not text | No automatic withdrawal of epistemic reliance | see record | see record | SRC-1 `plugin/exia_seed/graphe.py` | none | Withdrawal is not global retraction | see record |
| [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery) | operational admission/selection/consumption | implemented | [EPI-OBJ-fragments](#epi-obj-fragments); [EPI-OBJ-summaries](#epi-obj-summaries) | no content change | Retained material selected for host | see record | see record | see record | Ranking/delivery | Relevance and temporal eligibility, not truth certification | see record | see [RT-BAP-recalled-content](runtime.md#rt-bap-recalled-content) | SRC-1 `plugin/exia_seed/rappel.py` | [EPI-CLM-cited-memory](#epi-clm-cited-memory) | Data label does not eliminate procedural content | No observed compliance; privacy metadata is not authorization. |
| [RT-RTE-benchmark-replay](runtime.md#rt-rte-benchmark-replay) | check/evidence production | implemented | [EPI-OBJ-evaluations](#epi-obj-evaluations) | no content change | LoCoMo generated answers | Model with gold for categories 1–4; separate regex for category 5 | Benchmark judging stage | Majority label or abstention label | Writes judgments/reports, not production veto | Agreement with generous benchmark rubric or regex only | No live page or model promotion | Report writer; JSONL labels; evaluative; benchmark run | SRC-1 `banc/locomo/juger.py` | none | none | Gold not independently verified; model labels may be UNKNOWN. |
| [EPI-RTE-lme-judging](#epi-rte-lme-judging) | check/evidence production | implemented | [EPI-OBJ-evaluations](#epi-obj-evaluations) | no content change | see record | see record | see record | see record | Benchmark labels | see record | see record | see record | SRC-1 `banc/longmemeval/juger_lme.py` | none | Parser accepts substring “yes” | No live promotion consumer. |

No separate lifecycle-integration route after evidence-consuming acceptance of an ampliative claim was established in the directly inspected consolidation, summary and maintenance bodies. Their organization and retrieval changes follow lexical admission. This bounded finding does not claim that all uninspected diagnostics lack acceptance decisions.

## System-claim versus route comparison

| Claim ID | Claimed operation or warrant | Claim source ID/anchor and evidence layer | Doctrine/design support | Implemented route IDs | Observed-run support | Causal support and design limits | Supported conclusion | Mismatch/unknown |
|---|---|---|---|---|---|---|---|---|
| [RT-CLM-citation-control](runtime.md#rt-clm-citation-control) | see record | SRC-1 `plugin/exia_seed/consolidation.py`; implementation and doctrine | see record | [EPI-RTE-fragment-check](#epi-rte-fragment-check), [EPI-RTE-time-check](#epi-rte-time-check), [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation) | None supplied | No causal comparison; symbolic counterexample needs no execution | Bounded lexical/date veto, not confirmation or truth proof | Invalid mixed references and semantically opposite statements can survive. |
| [EPI-CLM-cited-memory](#epi-clm-cited-memory) | see record | SRC-1 `README.md`; doctrine/design and reported operation | see record | [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation), [EPI-RTE-fragment-check](#epi-rte-fragment-check), [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery) | No provenance-linked production trace supplied | Reported recall/benchmark results are not independently reproduced or causally identified | Inspectable cited memory and ranking architecture; explicit acknowledged lexical blind spot | Universal citation exactness is too strong for mixed references; reproducibility conditional on state/config/time. |
| [EPI-CLM-summary-grounding](#epi-clm-summary-grounding) | see record | SRC-1 `plugin/exia_seed/fiches.py`; doctrine/design | see record | [EPI-RTE-summary-proposal](#epi-rte-summary-proposal), [EPI-RTE-summary-check](#epi-rte-summary-check), [EPI-RTE-summary-write](#epi-rte-summary-write) | None supplied | No semantic-equivalence or transfer comparison | Bounded excerpts generate summaries; whole-page lexical checker can veto specified tokens | “Entire page” input and “nothing new” semantic conclusion are not enforced. |

## Bounded conclusion

- **Acquisition and retention:** [RT-RTE-conversation-ingest](runtime.md#rt-rte-conversation-ingest), [RT-RTE-register-admission](runtime.md#rt-rte-register-admission) and [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation) establish a route from conversation/notes to durable, source-addressed subject pages. Speaker assertion is acquired testimony; its source truth is unknown. Masking, omission and model rewriting mean complete preservation of source warrant is not established. Register entries are treated as non-agent even when an agent proposed them.
- **Candidate production and narrow warrant:** the fragment and summary models are requested to preserve facts, but actual semantic relations are indeterminate without linked outputs. Neither model fluency nor `conf` labels establish entailment. [EPI-RTE-fragment-check](#epi-rte-fragment-check) can admit a proposition contradicted by its cited sentence. [EPI-RTE-time-check](#epi-rte-time-check) derives calendar eligibility under explicit rules; its license stops at that predicate. It does not establish that the event occurred, that an intention remains endorsed or that a same-day candidate was actually mentioned.
- **Admission versus truth acceptance:** software consumes checker results to skip fragments or persist survivors. Summary rejection preserves old values; dry-run mode withholds writes. These are material criteria for operational use, with no mandatory human per-content approval and no source-truth oracle. They do not establish produced accepted ampliative knowledge. Input progress can advance despite rejection, so rejection is consequential loss of automatic reconsideration, not just an advisory warning ([RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation), [EPI-RTE-summary-write](#epi-rte-summary-write)).
- **Later authority:** [RT-BAP-recalled-content](runtime.md#rt-bap-recalled-content) is the live delivery path: later host models get selected facts, summaries and procedural rules through tool JSON or natural-language recall. Force is interpretive/advisory, not an executable obligation; horizon extends across sessions sharing the root. Concepts and graph weights rank candidates rather than prove their truth. Withdrawal can remove raw references while retaining searchable fact text ([EPI-RTE-withdrawal-read](#epi-rte-withdrawal-read)). Date filtering and cache invalidation are consumer-specific, not universal warrant renewal.
- **Evaluation is a separate route:** [RT-RTE-benchmark-replay](runtime.md#rt-rte-benchmark-replay) and [EPI-RTE-lme-judging](#epi-rte-lme-judging) wire reference-answer judgments into reports, not live memory acceptance or deployment. Their license concerns generated-answer agreement under named rubrics. Answer success would not identify which producing component caused it or establish explanation, transfer or replay safety.
- **Behavioral change remains separately bounded:** lasting user corrections can be retained as procedural content and prioritized for delivery; the source prompt explicitly requests this ([RT-BAP-recalled-content](runtime.md#rt-bap-recalled-content)). That supports an instruction-update capacity, not observed improved action. No supplied evidence closes exercised self-improvement's later behavioral-dependence link, and no causal improvement comparison establishes learning. This does not imply absent capacity or absent reflection in opaque model processing. No formulated-theory criticism/iteration route was established in the directly inspected production bodies; benchmark scoring alone is not such criticism.

## Shared records

### Operative objects

#### EPI-OBJ-sources
Label: Numbered sources

Raw speaker sentences and register text are natural-language content on Markdown/JSONL-backed input paths. Source references, agent flags and timestamps are symbolic metadata consumed by the consolidator. Claimed role: evidence for page proposals. Truth-apt statements include prices, events, preferences and decisions; retention requests themselves can be non-truth-apt policy. Distinct from the supplied route containers: this is their input object, not the capture or admission mechanism. Closest records: [RT-RTE-conversation-ingest](runtime.md#rt-rte-conversation-ingest), [RT-RTE-register-admission](runtime.md#rt-rte-register-admission). No object counterpart is declared in the supplied runtime.

SRC-1 implementation, `plugin/exia_seed/consolidation.py`: raw lines receive speaker classification and numbered references; all register notes receive `False` agent flags. This encodes eligibility, not human confirmation.

> for e in notes:
>             ref = f"registre:{e['id']}"
>             sources[ref] = (e["texte"], False)
> --- `plugin/exia_seed/consolidation.py`

#### EPI-OBJ-fragments
Label: Page fragments

Natural-language `fait` sentences with symbolic HTML-comment metadata reside in subject Markdown pages. Fields include source references, confidence, utterance/event/deadline time, privacy, protection, lot and concepts. Claimed role: self-contained durable facts and conduct rules. Model confidence is not calibrated evidence in the inspected admission body. Distinct object, not a duplicate of [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation); no supplied object counterpart. SRC-1 implementation: `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/pages.py`.

> meta = {"conf": frag.get("conf"), "src": ",".join(frag["src"]), "dit_le": moment,
>                     "event_time": quand, "echeance": echeance,
>                     "speaker": frag.get("speaker"),
>                     "privacy": frag.get("privacy") if frag.get("privacy") in ("personnel", "confidentiel") else None,
>                     "protected": "true" if frag.get("protected") else None, "lot": lot_id}
> --- `plugin/exia_seed/consolidation.py`

> if section not in self.sections or not fait or self.contient(section, fait):
>             return False
> --- `plugin/exia_seed/pages.py`

No provenance-linked instance was supplied that would establish an actually produced accepted ampliative claim. The object schema permits assertion and confidence but does not establish their warrant.

#### EPI-OBJ-summaries
Label: Identity summaries

Summary prose is natural-language truth-apt topic identification in YAML page headers, also rendered as a blockquote. Summary text is distinct from symbolic keywords and fragment bodies: its checks and old-value fallback differ. Closest supplied record is [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance), a route rather than an object; no object counterpart. SRC-1 implementation `plugin/exia_seed/fiches.py`, `plugin/exia_seed/pages.py`. Later delivery is supplied by [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery).

> nouv["summary"], nouv["summary_date"] = fiche, date
>             if mots is not None:
>                 nouv["keywords"] = list(mots)
> --- `plugin/exia_seed/fiches.py`

#### EPI-OBJ-keywords
Label: Distinctive keywords

Symbolic single-word selectors in the page YAML `keywords` list. These are not truth-apt topic descriptions. Their model proposal, name/alias membership filter and eventual later recall selection differ from the summary sentence's lexical grounding check. Distinct from [EPI-OBJ-summaries](#epi-obj-summaries); closest supplied route is [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance), with no supplied object counterpart. SRC-1 implementation `plugin/exia_seed/fiches.py`; subsequent delivery is [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery). Membership in a name/alias list does not establish the prompt's requested near-unique association in the user's life.

> if w and " " not in w and w in permis and w not in garde and w not in exclus:
>             garde.append(w)
>     return garde[:4]
> --- `plugin/exia_seed/fiches.py`

#### EPI-OBJ-concepts
Label: Concept vocabulary and graph evidence

Concept names, bilingual lexical fields, fact tags, alias matches, raw-line proximity, edge weights and proof excerpts are symbolic retrieval state on pages and graph/thesaurus JSON. A cited excerpt retains natural-language content but a graph `preuve` means the implemented association condition, not proof of the excerpt's truth or a causal relation between subjects. Distinct from fragment assertions and from [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance), their maintenance route; no supplied object counterpart. SRC-1 implementation `plugin/exia_seed/graphe.py`, `plugin/exia_seed/outils/concepts.py`.

> preuves[cle].append(_preuve("meme_ligne" if d == 0 else "voisine", force, a_, b_, d))
> --- `plugin/exia_seed/graphe.py`

> cs = [c for c in dict.fromkeys(th["faits"].get(texte, [])) if c in th["concepts"]][:3]
> --- `plugin/exia_seed/outils/concepts.py`

These numerical weights are localized symbolic calculations, not evidence of mutable learned model parameters.

#### EPI-OBJ-evaluations
Label: Benchmark answers and judgments

Question/gold/generated-answer prose is truth-apt within the benchmark task; labels, categories, votes and persisted JSONL judgment rows are symbolic results consumed by reporting code. Claimed role: answer-quality measurement, not live memory endorsement. Distinct from [RT-RTE-benchmark-replay](runtime.md#rt-rte-benchmark-replay), the construction/evaluation route; no supplied object counterpart. SRC-1 implementation `banc/locomo/juger.py`, `banc/longmemeval/juger_lme.py`.

> return {"label": Counter(labels).most_common(1)[0][0], "passes": labels, "regle": False}
> --- `banc/locomo/juger.py`

Reference truth and model judgment accuracy are not independently established by the fixture field name `gold`.

### Routes

#### EPI-RTE-fragment-check
Label: Fragment lexical check
Part of: [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation)

This is its check subroute, not the enclosing generation/disposition/writer. Endpoint: candidate fragment plus source map to Boolean/reason and normalized source-list field. Owner: deterministic consolidator. Target/domain: nonempty fact, known section and node slug, at least one valid non-agent reference, numeric/proper-name containment and five-character-root overlap. Model proposes; software evaluates; no human per-content review or expected-answer oracle. Open conversational operation, not a curriculum. SRC-1 implementation `plugin/exia_seed/consolidation.py`; closest supplied claim [RT-CLM-citation-control](runtime.md#rt-clm-citation-control).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: Boolean/reason; passing normalizes refs to a string list.
- Later read-back: inapplicable — the check itself retains nothing; enclosing writer later stores admitted prose/metadata.
- Delegated visibility: source text only for references present in the selected map; no external truth lookup.
- Selection predicate: valid source collection followed by non-agent, number, proper-name and overlap tests.
- Invalidation or expiry: inapplicable — per-fragment current-pass result, not an expiring retained result.
- Activation or effect: caller skips on false, proceeds toward page addition on true.
- Evidence limits: static deduction establishes possible acceptance, not a real generated candidate or frequency of false acceptance.

> minimum = 1 if len(mots_fait) <= 3 else 2
>         if len(communs) < minimum or (mots_fait and len(communs) / len(mots_fait) < 0.4):
>             return False, f"trop peu de mots en commun avec les sources ({len(communs)}/{len(mots_fait)})"
> --- `plugin/exia_seed/consolidation.py`

Concrete implementation deduction, not execution: with English mask, source `registre:case` mapped to `("i do not like hiking", False)`, and candidate `fait="i like hiking"`, `section="semantic"`, `noeud="hiking"`, `src=["registre:case"]`, the source is valid and non-agent. Neither text contributes numbers or capitalized proper nouns. English stopwords remove `i do not`; both content-word sets become `like, hiking`, so two common roots exceed minimum one and the ratio is one. The contradictory positive preference passes. This establishes non-entailment for this constructed candidate, not that the model actually produced it. The gate itself does not make the route ampliative; it admits semantically unsupported candidates.

> each few more most other some such no nor not only own same so than too very s t can will just don should now
> --- `plugin/exia_seed/langues/en.py`

> return [x for x in re.findall(r"[a-zà-ÿ0-9]+", texte.lower())
>             if (x.isdigit() or len(x) >= 3) and x not in m.mots_vides]
> --- `plugin/exia_seed/consolidation.py`

Invalid references in a mixed list are ignored while gathering cited text but remain in the normalized reference list; mixed agent/user text also does not establish confirmation of a particular claim. Evidence and countervailing rejection branch are retained in [RT-CLM-citation-control](runtime.md#rt-clm-citation-control). The strong alternative “it accepts anything” is false: numeric/name/overlap vetoes have enforcing consumers.

#### EPI-RTE-time-check
Label: Calendar validation and suffixes
Part of: [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation)

Subroute endpoints: cited text and source-derived utterance anchor plus model event/deadline proposals to retained date, stripped date/time and removal reasons; the caller appends suffixes. Code owns this route. It checks date parseability and calendar predicates, not whether the cited proposition is true. Proposer is model; evaluator/veto is software, no mandatory human decision or expected-answer oracle. SRC-1 implementation `plugin/exia_seed/temps.py`, `plugin/exia_seed/consolidation.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: verified ISO value or None, plus removal reason; suffix renderer formats accepted values.
- Later read-back: resulting event/deadline metadata reaches later temporal filtering through page retention.
- Delegated visibility: valid cited lines with timestamp prefixes removed, and earliest available cited utterance anchor.
- Selection predicate: parsed dates; anchor equality, day/month numeric mention, permitted weekday relation or relative-date/week rules; hour numeric checks.
- Invalidation or expiry: ungrounded date is dropped; ungrounded time can be dropped while retaining date; this is not whole-fact rejection.
- Activation or effect: caller retains fact, strips invalid metadata and adds permitted calendar suffix.
- Evidence limits: predicate satisfaction supplies no event-truth or endorsement warrant; source dates and encoding remain premises.

> if d == ancre:                                   # ce qui arrive ou est arrivé le jour même
>         return True
> --- `plugin/exia_seed/temps.py`

> if heure and not _heure_justifiee(heure, cite, m):
>         return d.isoformat(), f"heure non justifiée par les sources : {heure}"
> --- `plugin/exia_seed/temps.py`

Concrete trace: anchor 2026-11-07 and English cited text `appointment tomorrow`, with proposed date 2026-11-08, satisfy the `tomorrow` offset of one. `verifier` returns that date; `suffixe` renders the ISO date with weekday because the original fact lacks explicit day/month/year numbers. The derived calendar relation is entailed under that rule and anchor, not a new empirical discovery. Conversely an arbitrary parsed date equal to the anchor passes the same-day shortcut even without a date phrase. English bare weekdays permit both next and previous occurrence at the checking stage; tense consistency is requested of the model but not determined by this predicate.

> if d == prochain(ancre, i):
>                 return True
>             if (m.jour_nu_passe or re.search(m.motif_jour_passe.format(jour=nom), bas)) and d == precedent(ancre, i):
>                 return True
> --- `plugin/exia_seed/temps.py`

#### EPI-RTE-summary-proposal
Label: Summary proposal generation

Distinct material transformation spanning summary generation in [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation) and [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance); not part of exactly one supplied route. Model receives topic/aliases, old summary/keywords and ordered fact excerpts, returns JSON summary/keyword proposals. Target is topic identity, purpose and location. Prompt requests unchanged summary if still right and no invented detail, not proof. Model proposes; subsequent software checker decides admission; caller chooses write mode. No answer oracle. SRC-1 implementation and doctrine `plugin/exia_seed/fiches.py`, `plugin/exia_seed/langues/en.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: parsed per-node summary and optional word list to checking code.
- Later read-back: inapplicable — proposal generation alone retains nothing; summary-write route supplies retention.
- Delegated visibility: ten pages per call, at most 3,000 budgeted fact characters per page, ordered semantic/procedural/prospective/episodic, plus headers and old summary.
- Selection predicate: touched pages in consolidation; stale/missing summaries or all-page override in maintenance.
- Invalidation or expiry: inapplicable — current model proposal, not independently retained until admission.
- Activation or effect: supplies candidates for checker; unsupported tokens can be vetoed downstream.
- Evidence limits: no generated outputs supplied; faithful compression versus new inference versus semantic error is not determinable.

> CARACTERES_PAR_PAGE = 3000      # les faits d'une page, au plus (le général se voit dans les premiers)
> --- `plugin/exia_seed/fiches.py`

> for s, t in _faits(p):
>         if len(t) + 3 > reste:
>             break
>         lignes.append(f"- [{s}] {t}"); reste -= len(t) + 3
> --- `plugin/exia_seed/fiches.py`

The break is not a skip: an oversized earlier fact can prevent all later facts reaching this call. A whole page object is the input to the function, but not necessarily the content sent to the model. This is a source-supported countercase to the “entire page” wording.

#### EPI-RTE-summary-check
Label: Summary lexical controls

Distinct check subroute spanning the same two supplied containers as [EPI-RTE-summary-proposal](#epi-rte-summary-proposal). Endpoint: proposed summary/page to Boolean and reason; proposed keywords to filtered list. Code owns the check. Domain: nonempty summary, maximum 320 characters, recognized proper names (with known-name exceptions and normalized prefix/subword matching), numbers and paths in full page text; keywords must be single words from node/aliases, at most four and not known user/agent names. No human or reference-answer oracle; open maintenance/consolidation proposal mode. SRC-1 implementation `plugin/exia_seed/fiches.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: pass/fail/reason; separately filtered keywords.
- Later read-back: inapplicable — check output is not retained on its own.
- Delegated visibility: checker reads full page facts and aliases, not only model excerpt.
- Selection predicate: checks every nonempty parsed summary; filters keyword candidates without rejecting the summary.
- Invalidation or expiry: inapplicable — current-pass check.
- Activation or effect: false blocks replacement; invalid keyword is removed; caller may write survivors.
- Evidence limits: lexical tests do not check relational truth, permanence, completeness, semantic equivalence or actual keyword distinctiveness.

> for c in _RE_CHEMIN.findall(fiche):
>         if c.rstrip(".,;)") not in texte:
>             return False, f"chemin absent de la page : {c}"
>     return True, ""
> --- `plugin/exia_seed/fiches.py`

> if w and " " not in w and w in permis and w not in garde and w not in exclus:
>             garde.append(w)
>     return garde[:4]
> --- `plugin/exia_seed/fiches.py`

Countercase to “no veto”: absent path and oversized summary have enforcing rejection. Countercase to semantic grounding: the checker tests no negation/entailment relationship; a common-word sentence changing a preference is not rejected merely for that change.

#### EPI-RTE-summary-write
Label: Summary disposition and retention

Distinct consumer/write subroute shared by both consolidation and maintenance containers, not a duplicate of the preceding proposal/check endpoints. Code consumes the checker result and `ecrire` switch; the operator can request dry-run proposals but writing does not require per-sentence approval. Proposed change: summary and optional keyword replacement. Rejection leaves old metadata; empty/unparseable outputs do not replace it; call failure proceeds to other lots. No automatic semantic rollback, winner installation or expected-answer oracle. Shipped prompts guide proposal; page YAML persists admitted output. SRC-1 implementation `plugin/exia_seed/fiches.py`; external delivery is [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: proposal/written/unchanged/refused/absent report fields.
- Later read-back: page summary/keywords reach index/graph/cache and later topic recall subject to cache invalidation.
- Delegated visibility: downstream receives admitted header values, not the generator's entire prompt or rejection rationale.
- Selection predicate: nonempty parsed summary passing controler; write switch controls persistence.
- Invalidation or expiry: old summary retained on failure; refresh compares summary date with page update date.
- Activation or effect: write mode updates header and page file; dry run records proposals only; delivery is wired, compliance not observed.
- Evidence limits: passing controls grants topic-use availability, not evidence-consuming acceptance of novel world claims; maintenance alone does not refresh the graph cache.

> ok, raison = controler(fiche, p, connus)
>             if not ok:
>                 rapport["refusees"].append((n, raison, fiche)); continue
> --- `plugin/exia_seed/fiches.py`

> if ecrire:
>                 _poser(p, fiche, date, mots)
>                 p.ecrire()
> --- `plugin/exia_seed/fiches.py`

#### EPI-RTE-withdrawal-read
Label: Withdrawn provenance at graph read

Distinct downstream consumer of withdrawals, overlapping [RT-RTE-conversation-ingest](runtime.md#rt-rte-conversation-ingest) (which records omissions) and [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery) (which consumes reconstructed facts). Not exactly contained in either. Endpoint: pages plus raw withdrawal journal to graph/cache facts and edge evidence. Owner: graph page reader. User requests withdrawal through capture; code interprets line ranges. This route is not an evidence-based contradiction/falsehood judgment and has no answer oracle. SRC-1 implementation `plugin/exia_seed/graphe.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: nodes/facts with withdrawn raw references omitted from refs.
- Later read-back: reconstructed facts reach later retrieval; removal from refs does not remove page text.
- Delegated visibility: later retrieval still has the fact prose and metadata, even when some/all raw refs disappear.
- Selection predicate: omit raw refs found in withdrawal journal; append each page fact regardless of resulting refs.
- Invalidation or expiry: graph/cache rebuild governs when reconstructed state reaches consumers; no page retraction follows merely from refs becoming empty.
- Activation or effect: proximity evidence can change; naming/concept evidence and textual retrieval can remain.
- Evidence limits: static route only; no affected production page supplied; does not establish an actual privacy incident or all host erasure behavior.

> if l not in retraits.get(r.group(1), set()):
>                             refs.add((r.group(1), l))
> --- `plugin/exia_seed/graphe.py`

> faits.append({"noeud": n, "fichier": p.chemin.name, "section": section, "texte": texte,
>                               "norm": _norm(texte), "refs": refs, "dit_le": d.group(1) if d else None,
>                               "meta": champs})
> --- `plugin/exia_seed/graphe.py`

Countervailing scope: consolidation's `_lignes_de` does exclude withdrawn raw lines from new model input. Thus withdrawal has implemented force, but that force must not be promoted into global recall/retraction authority.

#### EPI-RTE-lme-judging
Label: LongMemEval answer judging
Part of: [RT-RTE-benchmark-replay](runtime.md#rt-rte-benchmark-replay)

Material specialization of the broader benchmark family [RT-RTE-benchmark-replay](runtime.md#rt-rte-benchmark-replay), whose explicit judgment description is LoCoMo. Distinct evaluator prompts/parser/endpoints, not a duplicate of LoCoMo judgment. Endpoint: dataset question/type/gold plus generated answer to model text, label and judgment JSONL. Code selects type-specific rubric, external model judges, code parses. Reference oracle is dataset gold/explanation/rubric, not model judgment alone; neither human review nor a production installation veto is wired here. Operator selects benchmark run; fixed prompt mode rather than an open production request. SRC-1 implementation/doctrine `banc/longmemeval/juger_lme.py`.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: label and up to twenty characters of judge response; main writes judgments and prints counts.
- Later read-back: retained benchmark judgments support reporting, not production memory or policy read-back.
- Delegated visibility: judge gets question, reference and generated response, not a full producing trajectory.
- Selection predicate: abstention overrides type; otherwise type template with standard fallback; one model pass.
- Invalidation or expiry: uninspected — this judge body does not establish report-cache retirement policy.
- Activation or effect: substring yes makes CORRECT; otherwise WRONG; consumers are benchmark outputs/counts.
- Evidence limits: no actual labels supplied; judge reliability, dataset truth, reproduction and causal attribution remain unestablished.

> return {"label": "CORRECT" if "yes" in (rep or "").lower() else "WRONG", "brut": (rep or "")[:20]}
> --- `banc/longmemeval/juger_lme.py`

License differs by type: temporal judging tolerates off-by-one duration errors; knowledge-update judging permits old material alongside the required update; preference judging uses a rubric; abstention judging asks whether the answer identifies insufficiency. Such answer-level correctness is not proof that stored facts were correct or that a memory component caused success.

> "question asks for the number of days/weeks/months, etc., and the model makes off-by-one errors (e.g., predicting "
>         "19 days when the answer is 18), the model's response is still correct. " + _FIN,
> --- `banc/longmemeval/juger_lme.py`

### Claims

#### EPI-CLM-cited-memory
Label: Cited auditable memory

SRC-1 doctrine/design `README.md` claims sentence memories citing exact conversation lines, recomputable retrieval and identical search replay. Reported operation there includes deployment counts, recall examples and benchmark comparisons. Distinct from [RT-CLM-citation-control](runtime.md#rt-clm-citation-control), which concerns the guard: this claim concerns the resulting memory and retrieval service. The implementation supports inspectable cited state, not universal exactness of every retained citation or truth of every statement.

> No embedding model. No vector database. Every memory is a sentence in a markdown page that cites the exact line of
> conversation it comes from; every retrieval score can be recomputed by hand, and every search replays identically.
> --- `README.md`

The strongest alternative interpretation—documentation claiming infallible truth checking—is contradicted by its explicit admission:

> It is a lexical check: a false statement built from the source's own words can still pass — a
>   known blind spot (`docs/04` §5.3).
> --- `README.md`

This report does not independently affirm byte-for-byte replay, performance figures or published effect estimates. No run trace or causal comparison is registered; currentness and temporal selection also depend on invocation time and cache state, not just query text.

#### EPI-CLM-summary-grounding
Label: Whole-page grounded identity summary

SRC-1 doctrine/design `plugin/exia_seed/fiches.py` describes summaries as written from the entire page and controlled like facts. Distinct from [RT-CLM-citation-control](runtime.md#rt-clm-citation-control): target is identity-summary content and input coverage, not fragment citation. The summary generator receives bounded ordered excerpts; the checker sees full-page lexical material. Thus whole-page lexical checking and whole-page model input must be distinguished.

> rediger(pages, appel_llm, date)    une phrase par page, écrite DEPUIS LA PAGE ENTIÈRE (la page fait foi,
>                                        pas le lot du jour), contrôlée comme un fait, posée dans l'en-tête :
> --- `plugin/exia_seed/fiches.py`

> Une fiche n'apporte rien que la page n'ait déjà : noms propres, nombres, chemins vérifiés.
> --- `plugin/exia_seed/fiches.py`

The second passage describes the check's intended semantic consequence, but only the listed lexical dimensions are implemented. Missing relational verification prevents treating summary admission as evidence of semantic equivalence or production of accepted new knowledge.
