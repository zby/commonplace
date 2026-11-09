---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "EXIA SEED memory: raw conversation and register admission, subject-page derivation, graph selection and unequal read-back controls."
run-id: AAS-2026-11-07-exia-seed-804e805b7a8d-01
source-identity: https://github.com/francisdu53/exia-seed
reviewed-boundary: c7497ac96da20bd1818096e35a59b6c0237f9730
---

# EXIA SEED memory report

## Boundary and evidence

EXIA SEED retains conversation and explicit notes, derives cited subject pages and retrieval structure, and delivers selected prose to a later Hermès invocation. The frozen boundary is SRC-1 at c7497ac96da20bd1818096e35a59b6c0237f9730, as defined in [boundary](boundary.md#boundary-and-evidence). Memory scope includes the provider hooks and tools, consolidation, pages, summaries, thesaurus, graph/cache, maintenance and shipped evaluation consumers. It excludes the enclosing host's own compaction algorithm, model/provider internals and unfrozen deployment state. Those exclusions prevent conclusions about actual host context placement, provider-side retention, model compliance and exercised benefit.

I directly inspected SRC-1 `plugin/exia_seed/pages.py`, `plugin/exia_seed/registre.py`, `plugin/exia_seed/graphe.py`, `plugin/exia_seed/fiches.py`, `plugin/exia_seed/creux.py`; provider initialization, dispatch, ingestion and recall ranges in `plugin/exia_seed/__init__.py`; admission, withdrawal, page writing, index and audit ranges in `plugin/exia_seed/consolidation.py`; raw writing/closure in `plugin/exia_seed/ingestion.py`; cache construction and automatic selection in `plugin/exia_seed/rappel.py`; and query display, logging and read/trail ranges in `plugin/exia_seed/requete.py`. These are implementation evidence, with comments treated as design statements rather than observations. Supplied runtime records provide the remaining maintenance, language-prompt, model-client and benchmark findings; those are distinguished below from direct reads. HEAD was rechecked against the frozen revision. No target, test or example was executed.

| Entry point or operation | SRC-1 paths | Coverage and conclusion limits |
|---|---|---|
| Primary turn and retention-command admission | `plugin/exia_seed/__init__.py`, `plugin/exia_seed/ingestion.py`, `plugin/exia_seed/consolidation.py` | Direct reads; [RT-RTE-conversation-ingest](runtime.md#rt-rte-conversation-ingest), [MEM-OBJ-raw](#mem-obj-raw). Host completeness remains external. |
| Explicit note and native-memory mirror | `plugin/exia_seed/__init__.py`, `plugin/exia_seed/registre.py` | Direct reads; [RT-RTE-register-admission](runtime.md#rt-rte-register-admission), [MEM-OBJ-registre](#mem-obj-registre). Tool identity does not establish human authorship or approval. |
| Automatic subprocess, forced/manual CLI, direct consolidation API | `plugin/exia_seed/__init__.py`, `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/outils/consolider.py`, `plugin/exia_seed_consolider.sh` | Provider/core read directly; CLI and shell coverage supplied by [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation). Same proposed-content gate; not an atomic transaction. |
| Fact, metadata, summary and keyword admission | `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/pages.py`, `plugin/exia_seed/fiches.py` | Direct reads; [MEM-OBJ-page-facts](#mem-obj-page-facts), [MEM-OBJ-page-metadata](#mem-obj-page-metadata), [MEM-OBJ-summary](#mem-obj-summary), [MEM-OBJ-keywords](#mem-obj-keywords). Separate checks; a summary is not a verbatim page. |
| Concept enrichment and graph rebuild | `plugin/exia_seed/graphe.py`, `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/creux.py` | Direct reads; [MEM-OBJ-thesaurus](#mem-obj-thesaurus), [MEM-OBJ-graphe](#mem-obj-graphe). No model call in graph construction; original concept semantics remain model/caller supplied. |
| Prefetch, phase-1 logging, phase-2 delivery | `plugin/exia_seed/__init__.py`, `plugin/exia_seed/rappel.py` | Direct reads of caller, cache and final selection; supplied runtime covers cascade overview. [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery), [MEM-CMP-memoire](#mem-cmp-memoire). No final-host-token guarantee or observed activation. |
| Explicit search and page/trail reads | `plugin/exia_seed/requete.py` | Direct display/read/trail inspection plus supplied search findings in [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery). Search scoring body not independently retraced in full; no exhaustive ranking-equivalence claim. |
| Compression/reset/session end | `plugin/exia_seed/__init__.py`, `plugin/exia_seed/ingestion.py` | Direct reads; compression writes only a marker, reset/end close raw. Host's replacement summary and eviction decisions remain uninspected, not attributed to EXIA SEED. |
| Summary/concept/timestamp/graph maintenance | `plugin/exia_seed/outils/fiches.py`, `plugin/exia_seed/outils/concepts.py`, `plugin/exia_seed/outils/ancrer.py`, `plugin/exia_seed/outils/graphe.py` | Tool coverage supplied by [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance); shared summary/graph implementation read directly. No per-content human approval inferred from write flags. |
| Replay, fusion, response, judging, caches and baseline alternatives | `banc/locomo/preparer.py`, `banc/locomo/repondre.py`, `banc/locomo/juger.py`, `banc/locomo/modele.py`, `banc/longmemeval/lancer.sh`, `banc/nexa/reconsolider.py`, `banc/modeles/consolider.py` | Supplied [RT-RTE-benchmark-replay](runtime.md#rt-rte-benchmark-replay) and runtime account. Full transcription/all-fact/index-selected response alternatives retained; baseline embeddings, remaining fusion/diagnostic details not independently inspected. Their exact provenance, parameters and selection behavior remain unresolved, preventing exhaustive benchmark-memory equivalence or reproduced scores. |
| Audit and provenance retention | `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/registre.py`, `plugin/exia_seed/rappel.py`, `plugin/exia_seed/requete.py` | Direct reads; [MEM-OBJ-journals](#mem-obj-journals). Logs are not automatically promoted into improved rules by these inspected readers. |

## Core ideas

1. **Compilation at write time, selection at read time.** A model proposes short facts and concept associations from budget-selected sources; code admits fragments and derives graph evidence. Later recall uses lexical matching, graph propagation and fixed scoring, not a fresh retrieval-time model interpretation. The resulting prose can carry both factual knowledge and conduct rules. See [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation), [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery) and [MEM-OBJ-graphe](#mem-obj-graphe).
2. **Source trust is path-dependent.** Raw assistant-only citations are rejected, but register entries are presented as non-agent sources even when supplied by an agent tool or native-memory mirror. Mixed citations can pass lexical checks without proving user confirmation. Secret guards and privacy labels do not establish a downstream authorization boundary. See [RT-CLM-citation-control](runtime.md#rt-clm-citation-control) and [RT-RTE-register-admission](runtime.md#rt-rte-register-admission).
3. **Retention is richer than delivery.** Pages retain source references, timestamps and policy metadata. Automatic recall delivers fact text and display dates; tools deliver selected prose and sometimes speaker labels, not all original evidence or privacy fields. Graph proof snippets can guide associative trails without giving the final model a complete warrant. See [MEM-OBJ-page-metadata](#mem-obj-page-metadata), [MEM-OBJ-graphe](#mem-obj-graphe) and the read-back account.
4. **Context control is asymmetric.** Auxiliary calls receive explicit source/page excerpts rather than the foreground context. Phase 2 injects selected subjects and facts; phase 1 only logs them. The compression hook does not itself summarize or restore the foreground history. Cache invalidation and temporal filters vary across read routes. These limits are local mechanisms, not evidence of failed or successful host behavior ([RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery)).

## Shared records

### Components

#### MEM-CMP-memoire
Label: Memoire retrieval cache

Source-native identity: `Memoire` and its owning `Rappeleur` in SRC-1 `plugin/exia_seed/rappel.py`. Storage is process memory, including SQLite FTS5 `:memory:`, Python dictionaries and a sparse numerical propagation engine. This is symbolic retrieval state: named nodes, explicit edge weights and localized consumer rules, not learned dense embeddings or provider parameters. The sparse engine's arrays encode individual graph edges; numerical storage alone does not make them distributed-parametric memory. The external consolidation model remains [RT-CMP-consolidation-model](runtime.md#rt-cmp-consolidation-model), not this component.

Lineage: cache construction reads pages/thesaurus through `_graphe._lire`, loads the saved graph, derives aliases, concept lexical fields, IDF and FTS rows, then maps summaries and neighbor evidence. Consumers are automatic recall and `Lecteur`; cache exists across invocations in the process, while durable source objects survive process restart. Graph edge-file mtime is the invalidation signal, not page-file mtime. This component is the reader implementing [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery), not a duplicate route or model.

> self.fts = sqlite3.connect(":memory:", check_same_thread=False)
> --- `plugin/exia_seed/rappel.py`

> f = self.racine / "graphe" / "aretes.json"
> return f.stat().st_mtime_ns if f.exists() else None
> --- `plugin/exia_seed/rappel.py`

The cache gives ranking/selection authority to code. Returned prose has only the interpretive authority described by [RT-BAP-recalled-content](runtime.md#rt-bap-recalled-content). Operation, activation and benefit remain unobserved.

### Operative objects

The runtime declares no operative objects. The objects below distinguish products and control state of its routes, rather than re-declaring those routes or the external model components.

#### MEM-OBJ-raw
Label: Raw conversation batches

Source-native identity: `raw/*_open.md` and closed `raw/*.md`, authored by `Brut`. Substrate is append-written Markdown, renamed on closure, with YAML identity/time fields and speaker-prefixed natural-language conversation. Text and fixed-parsed headers are separate operative parts: source text goes to consolidation; session/day/token/hash state governs acquisition and eligibility, not factual authority. These are transformed raw traces, not a full host transcript: recognizable secrets are masked, notices/voice/envelopes can be transformed, tool turns are not automatically included. Authorship is mixed user/assistant/host notice; software admits ordinary primary turns without per-content approval. Human retention commands can veto current capture or withdraw the previous turn through a journal. SRC-1 `plugin/exia_seed/ingestion.py`, `plugin/exia_seed/__init__.py`; closest supplied route is [RT-RTE-conversation-ingest](runtime.md#rt-rte-conversation-ingest), whose stored input this object identifies.

> lignes.append(f"[{heure} {qui}] {texte_utilisateur}")
> --- `plugin/exia_seed/ingestion.py`

Later consumer: consolidation reads only conversation lines of pending closed lots and excludes withdrawn lines. Raw files remain available as provenance; no inspected automatic recall route sends whole raw files to the foreground model. Closure hashes record integrity lineage, not truth. Withdrawal preserves raw bytes and is not retroactive page erasure. The exact retention of host messages outside this hook remains external.

#### MEM-OBJ-registre
Label: Explicit-note register

Source-native identity: `registre.md`, with separate `registre.integre.jsonl`. Append-only Markdown contains natural-language notes and symbolic IDs/date/source/node/privacy fields. The integration JSONL is access/progress metadata, not note semantics. SRC-1 `plugin/exia_seed/registre.py`, `plugin/exia_seed/__init__.py`. This is the retained source of [RT-RTE-register-admission](runtime.md#rt-rte-register-admission), distinct from raw capture.

> return [e for e in self.entrees() if e["id"] not in faits]
> --- `plugin/exia_seed/registre.py`

Tool callers and native-memory callbacks supply content; the register normalizes/escapes it and physically appends. Guarded provider calls reject recognized secrets. Direct library `noter` does not establish that guard. Caller identity leaves human versus computational admission unresolved per entry; no separate approval interaction is required. Consolidation consumes pending entry text and privacy, treats it as non-agent, and does not forward the full register record. Node hints retained in the register are not appended to its source text in the inspected consolidation loop. Integrated IDs cease pending delivery even when no accepted fact cites them. A native `remove` mirrors a descriptive note, not deletion of this object or earlier page knowledge ([RT-RTE-register-admission](runtime.md#rt-rte-register-admission)).

#### MEM-OBJ-page-facts
Label: Subject-page fact prose

Source-native identity: four-section fact lines in `pages/*.md`, represented by `Page.sections`. Natural-language facts persist in Markdown, separate from the parsed comments assessed below. They derive from model proposals over raw/register sources and code date rendering. The immediate admission mechanism is lexical/source/shape checking, alias routing and normalized same-section duplicate detection; the model authors the phrase, code decides/writes, no per-fragment human gate is called. Existing facts are appended to rather than semantically replaced by the inspected `Page.ajouter`. SRC-1 `plugin/exia_seed/pages.py`, `plugin/exia_seed/consolidation.py`; retained output of [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation), not a new admission route.

> self.sections[section].append(f"- {fait.strip()} <!-- {champs} -->" if champs else f"- {fait.strip()}")
> --- `plugin/exia_seed/pages.py`

Later consumers: summary generation, graph/cache reconstruction, recall/search/read, and benchmark answer routes. Facts can express rules of conduct; their authority at the foreground model is natural-language guidance, not executable policy. Source citations can retain evidential lineage but no independent reasoning/rationale field is required. A fact may itself include a reason; the format does not guarantee one. No observed improved capacity or exercised self-improvement follows from this retention. Actual content-directed theory criticism cannot be inferred from the `procedural` or `etat_agent` label alone ([RT-BAP-recalled-content](runtime.md#rt-bap-recalled-content)).

#### MEM-OBJ-page-metadata
Label: Subject-page identity and fact controls

Source-native identity: page YAML excluding summary/keywords, and trailing fact HTML comments. Fixed-parsed symbolic fields persist beside prose: node/type/aliases, creation/update dates, source/model lineage and strength; fact confidence, source references, utterance/event/deadline times, speaker, privacy, protected flag, batch and concepts. These are not an opaque payload represented only by display text: parsers read the actual serialized fields. SRC-1 `plugin/exia_seed/pages.py`, `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/graphe.py`.

> champs = dict(x.split(":", 1) for x in meta.split() if ":" in x)   # lu par le rappel
> --- `plugin/exia_seed/graphe.py`

Code derives utterance time from cited source anchors, verifies proposed event/deadline dates and limits concepts to known/newly defined values. Other fields, such as confidence or protected, remain proposed metadata rather than independently calibrated warrant. Aliases are merged; page type is normalized on creation. Consumers use dates for selection, confidence/protected for tie-breaking, aliases/concepts for retrieval and source references for graph proofs. Privacy retained here is not a tested authorization predicate in the supplied read routes. Foreground display omits much of this metadata, including full source references; content and access metadata therefore must not be conflated ([RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery)). This is distinct from fact prose because consumers enforce different fixed rules on it; it is not a second declaration of that prose.

#### MEM-OBJ-summary
Label: Subject identity summary

Source-native identity: YAML `summary` and its rendered page blockquote; `summary_date` tracks refresh. Natural-language summary is stored in the page header and copied/truncated into `INDEX.md`; it is a model-derived second representation, not the raw trace or a proof-bearing fact. SRC-1 `plugin/exia_seed/fiches.py`, `plugin/exia_seed/pages.py`, `plugin/exia_seed/consolidation.py`. This is the separately checked product of summary generation in [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation) and [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance).

> CARACTERES_PAR_PAGE = 3000      # les faits d'une page, au plus (le général se voit dans les premiers)
> --- `plugin/exia_seed/fiches.py`

> ordre = ("semantic", "procedural", "prospective", "episodic")
> --- `plugin/exia_seed/fiches.py`

The model sees existing summary/keywords plus prioritized page-fact excerpts, stopping at the first fact exceeding the remaining character budget. Thus comments saying “entire page” do not establish full-page exposure. The checker uses full page text/aliases and known names for selected name/number/path constraints, with a 320-character limit; it does not establish entailment. Software vetoes rejected summaries and leaves older values; callers can preview or enable writes without approving each phrase. Later `souvenirs` and `lire` deliver the summary as subject identity. It has no required per-summary source references or derivation reasons, and is not independently filtered against the query's historical time. This distinct admission/read path warrants separation from fact prose.

#### MEM-OBJ-keywords
Label: Distinctive subject keywords

Source-native identity: YAML `keywords`, written alongside summaries and loaded as graph node `mots`. Substrate is page YAML; form is a symbolic list of at most four normalized single words, not summary prose or a dense representation. The model proposes; `mots_valides` admits only words in node name/aliases, excluding configured user/agent names and duplicates. SRC-1 `plugin/exia_seed/fiches.py`, `plugin/exia_seed/rappel.py`. A rejected keyword need not reject its summary, while an older response without a keyword field can retain previous keywords.

> return garde[:4]
> --- `plugin/exia_seed/fiches.py`

Later consumer is cache alias activation: non-distinctive alias words receive lower weight, with special handling for short distinctive words and situation-driven node types. These are learned-by-content editing of retrieval inputs, not weight training of [RT-CMP-consolidation-model](runtime.md#rt-cmp-consolidation-model). Retained keywords carry no required justification. Same writers as [MEM-OBJ-summary](#mem-obj-summary), but different gate and consumer; no supplied object counterpart.

#### MEM-OBJ-thesaurus
Label: Concept thesaurus

Source-native identity: `thesaurus.json`, mapping concept slugs to language lexical fields and an optional fact-text-to-concepts table. Form is symbolic structured text on disk. Initial contents can be pre-existing/caller-supplied; the inspected consolidator's known subsequent transformation adds new model-defined concepts only when used by admitted fragments. It does not establish the provenance or human approval of an arbitrary starting file. Fact associations use at most three recognized concepts. SRC-1 `plugin/exia_seed/graphe.py`, `plugin/exia_seed/consolidation.py`.

> utilises = sorted({c for f in faits for c in f["concepts"]})
> --- `plugin/exia_seed/graphe.py`

Later graph/cache consumers expand fields with words from associated fact prose. `_champs_appris` selects up to four rare words per fact, then up to forty frequent-within-concept words, excluding ubiquitous words. This is a deterministic trace-derived vocabulary route through admitted facts, not merely retaining query logs and not demonstrated learning benefit. It changes selection inputs on later reads, without changing provider parameters. Supplied [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance) supplies alternate concept-tagging admission; its checks differ from fact citation checks. This object is distinct from graph weights and page facts, though the same admission route produces their inputs.

#### MEM-OBJ-graphe
Label: Associative graph and evidence

Source-native identity: `graphe/noeuds.json`, `graphe/aretes.json` and `graphe/rapport.json`. Disk JSON carries symbolic named nodes, weighted edges and truncated supporting snippets; fixed reconstruction/propagation rules consume them. Weights are deterministic counts/saturation/degree normalization from cited-line proximity, named aliases and concept association, not opaque learned neural parameters. SRC-1 `plugin/exia_seed/graphe.py`, `plugin/exia_seed/creux.py`. This is the retained selector structure behind [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery), not a new external model.

> PREUVES_LISTEES = 20            # par arête ; le compte total est toujours donné
> --- `plugin/exia_seed/graphe.py`

> ps = sorted(preuves[(a, b)], key=lambda p: (-p["force"], p["type"], p["page"], p["fait"]))
> --- `plugin/exia_seed/graphe.py`

Derivation recalculates from page facts and thesaurus, excludes configured implicit names from named-link evidence and honors withdrawals when forming raw-line references. It does not drop fact prose whose source line is withdrawn. Consumers use weights for propagation and proof snippets for associative query trails. Stored evidence includes only bounded snippets/line references, not all reasons or full original sources. Trails attempt to recover full neighboring facts through prefix matching. Graph reporting and edge-count limits can leave an older graph in place; page writes alone do not ensure a current reader cache. Reconstruction is software admission under consolidation or an operator-selected maintenance invocation, not human approval of each edge.

#### MEM-OBJ-journals
Label: Progress and audit journals

Source-native identity: raw state/last-turn/withdrawal/closure/consolidation journals, register integration JSONL, page hash chain, memory Git history, `log.md`, telemetry and recall/query JSONL. These are filesystem text/JSON/history, grouped here as access/provenance state, not a second semantic fact store. JSON IDs/hashes/timestamps drive eligibility or inspection; rejection prose and truncated query/fact displays are natural-language audit parts. SRC-1 `plugin/exia_seed/ingestion.py`, `plugin/exia_seed/registre.py`, `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/rappel.py`, `plugin/exia_seed/requete.py`.

> entree = {"ts": maintenant.isoformat(timespec="seconds"), "message": message[:300],
>           **{k: v for k, v in r.items() if k not in ("bloc", "_choisis")}}
> --- `plugin/exia_seed/rappel.py`

The producer is code, not a separate approval role. Last-turn and withdrawal records affect subsequent source admission; progress records prevent reconsidering processed inputs; hashes/Git afford provenance/history. Reject logs retain reasons but are not read by the inspected consolidation source builder, recall cache or tool reader as revision guidance. Recall journals omit the full delivered block and internal selection indices; they are neither complete context checkpoints nor automatic trace-learning inputs. Git failure does not undo admission. Benchmark request/answer caches are a separate supplied mechanism in [RT-RTE-benchmark-replay](runtime.md#rt-rte-benchmark-replay), not evidence that production reads these audit logs into its behavior.

### Routes

none declared in this member

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-conversation-ingest](runtime.md#rt-rte-conversation-ingest)

Memory-specific lineage: [MEM-OBJ-raw](#mem-obj-raw) is the raw source, not derived knowledge. The last-turn journal survives batch closure and lets a recognized retrospective command identify earlier lines. `_lignes_de` excludes those lines before model delivery; graph reconstruction excludes their raw-reference links, but still appends each page fact. Thus withdrawal has source-admission and graph-evidence effects, not a proven semantic erasure cascade. SRC-1 `plugin/exia_seed/ingestion.py`, `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/graphe.py`.

> if l not in retraits.get(r.group(1), set()):
>     refs.add((r.group(1), l))
> --- `plugin/exia_seed/graphe.py`

#### On [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation)

Trace-fed write chain: raw conversation/explicit note → separate auxiliary model proposal → lexical admission and timestamp transformation → [MEM-OBJ-page-facts](#mem-obj-page-facts)/[MEM-OBJ-page-metadata](#mem-obj-page-metadata) → summary, concepts, graph → later foreground delivery. Original inputs include user and agent text, but agent-only raw support is vetoed; register text has potentially mixed origin. Reasons may survive in fact prose and source links, not in a guaranteed rationale field. The auxiliary model receives a catalogue and selected source text, not a full foreground conversation frame. No per-content human gate is introduced by calling the CLI. Source budget is not a hard total-message cap: first raw lot can exceed it, notes/catalogues are added outside that remaining-lot check. SRC-1 `plugin/exia_seed/consolidation.py`.

> if lots and cout > budget:
>     break                                  # le reste au prochain passage
> --- `plugin/exia_seed/consolidation.py`

#### On [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery)

Read-back draws durable content into later invocations; the short-lived `_amorce` additionally retains previous successful recall entry activations in process memory, for configured minutes. It is symbolic topic priming, not a stored conversation summary or provider weight update. Generic recall's selected facts feed phase-2 subject selection; subject summaries and file pointers are then added. Final prose lacks full source comments and their reasons. SRC-1 `plugin/exia_seed/__init__.py`, `plugin/exia_seed/rappel.py`, `plugin/exia_seed/requete.py`.

> self._amorce = (instant, dict(res.get("entrees") or {}))
> --- `plugin/exia_seed/__init__.py`

## Write side

Admission mechanisms differ. Ordinary primary turns are automatically retained after masking and retention-command handling; explicit notes/native mirrors are admitted through separate provider guards in all initialized contexts. Direct register/library and benchmark raw-file writes must not inherit hook guards they do not call. The model authors proposed derived facts; code applies a lexical veto, chooses the actual page through alias resolution, appends and serializes. Existing subject pages are not full inputs to fact extraction: the consolidator supplies names/aliases and a concept catalogue, so old fact content is not automatically available for semantic contradiction resolution. This bounds any reading of consolidation as comprehensive truth maintenance. Sources and minimum passages are in [RT-RTE-register-admission](runtime.md#rt-rte-register-admission), [RT-CLM-citation-control](runtime.md#rt-clm-citation-control) and the annotations above (SRC-1 `plugin/exia_seed/consolidation.py`).

Summary and keywords are a second admission mechanism. Summaries use name/number/path/length checks against page text; keywords use node/alias membership. Both can be rewritten automatically after fact admission or by write-enabled maintenance, without per-phrase human review. Timestamp, concept and graph maintenance have their own fixed filters and caller flags; the supplied [RT-RTE-state-maintenance](runtime.md#rt-rte-state-maintenance) records their alternate write surfaces. Unknown initial thesaurus/page provenance does not erase these known transformations. Physical writes, authorship and admission are separate roles ([MEM-OBJ-summary](#mem-obj-summary), [MEM-OBJ-keywords](#mem-obj-keywords), [MEM-OBJ-thesaurus](#mem-obj-thesaurus)).

A parsed response advances all selected sources even when some/all fragments fail. The rejection reason remains audit material rather than a wired critic-to-revision prompt. An unreadable JSON response leaves inputs pending; a rejected summary preserves its predecessor; graph/Git failures do not roll back accepted page prose. Retrospective raw withdrawal leaves raw bytes and does not remove already derived facts. Native-memory removal is another positive note. These are distinct rejection/recovery paths, not one forgetting guarantee ([RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation), [RT-RTE-register-admission](runtime.md#rt-rte-register-admission), [MEM-OBJ-journals](#mem-obj-journals)).

This establishes automatic trace-fed transformation into later behavior-shaping content. It does not establish improved capacity. User behavioral corrections may become procedural facts, but neither model compliance nor successful reflective theory building follows from page labels. The retained-input/derived-output/later-consumer chain is inspectable; actual deployment and causal improvement remain unobserved ([RT-BAP-recalled-content](runtime.md#rt-bap-recalled-content)).

## Read-back

**Automatic supply.** The host calls `prefetch` with the current query. Code removes envelope material, consults cached aliases/lexical/concept/graph inputs and optional recent priming, ranks eligible facts and applies thresholds, per-node limits and an estimated token ceiling. It omits future utterances and expired prospective facts. Phase 1 runs/journals selection but returns empty; phase 2 builds a smaller subject/fact view, prioritizes procedural facts among selected facts and adds summary and path pointers. This is query-triggered automatic supply without a foreground tool request, not evidence of unsolicited retrieval independent of host invocation. Summaries added after generic selection make its budget non-universal. The later host model receives prose, not executable constraints ([RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery), [RT-BAP-recalled-content](runtime.md#rt-bap-recalled-content); SRC-1 `plugin/exia_seed/__init__.py`, `plugin/exia_seed/rappel.py`).

**Requested search/read.** The foreground model chooses a short query or subject via explicit tools. Symbolic search/ranking or subject resolution chooses retained page facts and trails; subject identifiers alone do not prove relevance selection. `lire` uses a nominal 1,200-token page/trail budget, but admits a first fact without a hard total serialized-output check, and returns summary/metadata overhead separately. `_fait` returns prose, display date and eligible speaker label; it does not forward full source/protected/privacy/confidence comments. Normal page sections exclude future utterances; read-page neighbor proof recovery and newest-neighbor fallback do not. Automatic expiry therefore is not a universal retention or read policy. Direct file reading is an afforded human/host usage surface, not proven deployed host tool wiring; it can expose metadata absent from tool JSON (SRC-1 `plugin/exia_seed/requete.py`, `plugin/exia_seed/pages.py`; [RT-RTE-memory-delivery](runtime.md#rt-rte-memory-delivery)).

**Working-context isolation and restoration.** The consolidation and summary calls receive bounded explicit messages, keeping unrelated foreground history out. Only admitted content and returned text escape; the page store remains outside the model window and is later brought back by prefetch/tools. This resembles a separate work frame with selected inputs and returned products, but not a reference-counted heap: a file pointer in prose does not automatically reload its referent, and the foreground model gets material by value. These are auxiliary calls, not evidence of a general-purpose autonomous sub-agent runtime. The compression hook writes a nonconversation marker and returns empty; no EXIA SEED replacement checkpoint or verbatim-tail policy is established by it. Host compaction and any alternate host checkpoint forms remain outside the frozen implementation. Session end/reset close the batch, preserving sources rather than popping/erasing them. SRC-1 `plugin/exia_seed/__init__.py`, `plugin/exia_seed/ingestion.py`.

> self._brut.marquer(f"compression de l'historique — {len(messages or [])} messages")
> --- `plugin/exia_seed/__init__.py`

**Evaluation consumers.** Supplied [RT-RTE-benchmark-replay](runtime.md#rt-rte-benchmark-replay) establishes chronological construction and later benchmark answers using generated contexts, index-selected pages, all facts or full transcription, with persisted model-call caches. These alternatives must not be collapsed into the live tool/prefetch policy. Reference answers reach the judge, not the production consolidation gate. Private data, full datasets, embedding-baseline internals and the separate plugin copy used by model comparisons prevent exhaustive route equivalence, independent scores or inference that a judged winner was deployed (SRC-1 paths in the coverage table; supplied implementation findings only).

## Integration issues

- No correction to a supplied runtime fact is required by these direct reads. Added precision: summary producer comments claiming whole-page input are bounded by the actual 3,000-character fact excerpt, whose order favors semantic/procedural facts. The checker still consults full page text. This confirms rather than contradicts the runtime's bounded-summary warning; see [MEM-OBJ-summary](#mem-obj-summary) and [RT-RTE-page-consolidation](runtime.md#rt-rte-page-consolidation).
- Withdrawal has two distinct effects: filtering future consolidation input and removing graph raw-reference evidence. It does not remove page prose in `_lire`, so it cannot establish forgetting of already derived knowledge. Preserve this limit when connecting [MEM-OBJ-raw](#mem-obj-raw), [MEM-OBJ-graphe](#mem-obj-graphe) and [RT-RTE-conversation-ingest](runtime.md#rt-rte-conversation-ingest). Existing summary/cache values can outlive such changes until independently refreshed/rebuilt.
- No possible duplicate declaration is identified after comparison: runtime has no object declarations; the memory component is a retrieval cache, not either external model. Route-specific memory findings annotate supplied routes instead of allocating replacements. Page fact prose, parsed controls, summary and keywords are intentionally separate parts with distinct checks/consumers.
- Unresolved initialization: actual pre-existing pages/thesaurus and per-entry caller agency are not frozen. Known consolidation/maintenance transformations remain established, but one cannot attribute all starting content to human approval or all of it to model generation ([MEM-OBJ-registre](#mem-obj-registre), [MEM-OBJ-thesaurus](#mem-obj-thesaurus)).
- Unresolved benchmark detail: full fusion, embedding-baseline and diagnostic implementations were not independently inspected by this memory account. Supplied runtime establishes material replay/response alternatives but not every baseline part's lineage or selector; no exhaustive benchmark-memory or causal-component claim is made ([RT-RTE-benchmark-replay](runtime.md#rt-rte-benchmark-replay)).
- Unresolved deployment: host compaction, final context placement and actual consumption of conduct rules are external/unobserved. Page delivery does not settle activation, learning, exercised self-improvement or benefit ([RT-BAP-recalled-content](runtime.md#rt-bap-recalled-content)).

## Limitations and checks

The frozen source supplies implementation and design statements, not a supplied execution trace or causal experiment. HEAD matched c7497ac96da20bd1818096e35a59b6c0237f9730. The input contracts and this invocation were read completely, with oversized inputs read in separate bounded ranges. Added source inspection stayed within SRC-1 and the selected functional boundary; no source IDs, target execution or external corpus were added. Available but uninspected benchmark/host details are local limits, not evidenced absences. No prohibited prior analysis was consulted.

Deterministic validation: passed for this memory candidate against the supplied artifact. This checks structure, references and quotation occurrence, not semantic support, exercised operation or job acceptance.
