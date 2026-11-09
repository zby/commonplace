---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "EXIA SEED runtime: host hooks, asynchronous consolidation, admission checks, recall and shipped replay routes at c7497ac96da20bd1818096e35a59b6c0237f9730."
run-id: AAS-2026-11-07-exia-seed-804e805b7a8d-01
reviewed-boundary: c7497ac96da20bd1818096e35a59b6c0237f9730
---

# EXIA SEED runtime report

## Runtime account

### Work and ordinary invocation

EXIA SEED is a Hermès memory provider, not the assistant's general action executor. Its consequential work is converting conversation and explicit notes into subject pages, then selecting retained material for later assistant invocations. This account uses SRC-1 implementation and shipped prompt doctrine at the frozen commit. No target was executed. Supplied evidence establishes neither actual activation of recalled instructions nor benefit, latency, deployed grants or model compliance. Host invocation ordering and final context insertion remain external contracts, as recorded in [the boundary](boundary.md#boundary-and-evidence).

Registration constructs `ExiaSeedProvider`. Initialization loads `memory.exia_seed` settings, resolves the memory directory beneath the host home, fixes its language, and records session and `agent_context`. Only `None`, empty and `primary` contexts enable conversation writing. Every initialized context gets a register and query reader sharing one recall cache; primary contexts additionally get the raw writer and, when configured, automatic recall. Tool schemas are available even before initialization. The manifest's hook list is described as informational, not a dispatch filter (SRC-1, `plugin/exia_seed/__init__.py`, `plugin/exia_seed/config.py`, `plugin/exia_seed/plugin.yaml`).

An ordinary primary conversation follows [RT-RTE-conversation-ingest](#rt-rte-conversation-ingest), then [RT-RTE-page-consolidation](#rt-rte-page-consolidation), then [RT-RTE-memory-delivery](#rt-rte-memory-delivery). The host supplies user and assistant text after a turn. EXIA SEED replaces a voice marker with spoken content when available, masks recognizable secrets, recognizes retention commands and appends timestamped speaker lines. A day change, volume threshold, session end or reset closes the current batch. Closure renames the file, records its digest and previous digest, and leaves it eligible for consolidation. Automatic consolidation starts on a separate host-context thread, which launches the shipped Python consolidation CLI in a subprocess. The host thread does not run the model client itself. If already busy, it does not queue another thread; remaining work waits for a later invocation. The nightly shell driver calls the same CLI with `--forcer`, which closes the current day's open batch too (SRC-1, `plugin/exia_seed/__init__.py`, `plugin/exia_seed/ingestion.py`, `plugin/exia_seed/outils/consolider.py`, `plugin/exia_seed_consolider.sh`).

The consolidator takes a nonblocking file lock, loads pending raw batches and register entries, builds numbered sources and an existing-node/concept catalogue, and calls its injected model function. Code, not the model, owns progression and physical writes. The model proposes self-contained facts, target nodes, sections, metadata and new concepts. Code parses or salvages complete JSON fragments, checks each fact, resolves aliases, writes pages, optionally generates identity summaries, advances input journals, regenerates the index and graph, chains page hashes and attempts a Git commit. The callable supplied by the production CLI uses the host auxiliary client with explicit configured provider and selected model. It supplies messages, reasoning effort and timeout, but no EXIA SEED shell/tool executor to that model call (SRC-1, `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/outils/consolider.py`). Model fixity is recorded in [RT-CMP-consolidation-model](#rt-cmp-consolidation-model).

A later user message can cause automatic recall or the host model can request explicit search/read. Retrieval is code-directed lexical/graph computation rather than a retrieval-time LLM call. The cache reconstructs when `graphe/aretes.json` modification time changes; page-only changes do not independently invalidate that cache. Automatic phase 1 computes and journals but returns an empty string; phase 2 returns subjects, summaries and selected facts for host insertion. Explicit tools work in both phases and all initialized contexts. EXIA SEED does not itself decide the assistant's next action or enforce its compliance with recalled procedural rules (SRC-1, `plugin/exia_seed/__init__.py`, `plugin/exia_seed/rappel.py`, `plugin/exia_seed/requete.py`; [RT-BAP-recalled-content](#rt-bap-recalled-content)).

### Selected challenges and guarantee boundaries

Four forcing cases prevent treating local controls as system-wide guarantees.

1. **Non-primary contexts can still retain notes.** `sync_turn` is gated by `_actif`, but the register is deliberately initialized for every context; `memoire_noter` and native-memory mirroring do not require `_actif`. Consolidation marks register sources as non-agent regardless of the tool caller. Thus primary-only raw ingestion is wired; primary-only knowledge admission is not the implemented contract ([RT-RTE-register-admission](#rt-rte-register-admission)). This is not evidence of an unauthenticated remote caller: host authentication and dispatch are outside the source boundary.
2. **Phase 1 is not a global no-read guarantee.** `system_prompt_block` is empty and phase-1 `prefetch` returns empty, but explicit search/read tools remain available. Phase 2 follows `_souvenirs`, not the generic recall block. It adds summaries and subject pointers after generic selection, without reapplying the generic 1,200-token ceiling. The generic estimated-token budget is therefore not a universal final-context cap. Host direct file access, if granted, is another consumption path whose actual grant is unobserved (SRC-1, `plugin/exia_seed/__init__.py`, `plugin/exia_seed/rappel.py`, `plugin/exia_seed/requete.py`).
3. **Citation checking is a lexical gate, not proof or confirmation verification.** Invalid references are ignored while collecting valid cited text; a mixed reference list can pass if valid text suffices. Mixed agent/user citations pass the agent-only check without proving that the user confirmed that particular assistant claim. Salvaged complete fragments pass the same checker as ordinary JSON, while unrecovered trailing material is lost. This bounds the stronger introductory claim that every invented source is rejected (SRC-1, `plugin/exia_seed/consolidation.py`; [RT-CLM-citation-control](#rt-clm-citation-control)).
4. **Temporal and privacy controls differ by consumer.** Automatic recall removes future-dated facts and expired prospective facts. Explicit search filters future facts but not expired prospective ones. Read-page sections filter future facts, but the linked-page trail extraction and newest-neighbor fallback do not apply that date predicate. These branches are reachable from an ordinary `memoire_lire` request when neighboring evidence or fallback facts exist; no actual affected memory is supplied. Privacy labels guide the consolidation model and remain page metadata, but the inspected recall/search/read paths do not use them as an authorization predicate or consistently return them to the host. This prevents attributing a software-enforced confidential-output boundary to the plugin (SRC-1, `plugin/exia_seed/langues/en.py`, `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/requete.py`, `plugin/exia_seed/rappel.py`).

| Guarantee and owner | Enforcement and strength | Covered and alternate paths; required external contract | Separate conclusions |
|---|---|---|---|
| Primary-only conversation capture; provider | `_actif` plus raw-writer check in `sync_turn`; invariant for that hook | Does not cover register notes or host filesystem edits. Requires accurate host `agent_context`. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Single consolidation writer; consolidator | `flock(LOCK_EX | LOCK_NB)` around `_consolider`; invariant among cooperating lock users | CLI and benchmark `consolider()` use it; concept, timestamp and graph maintenance use the same lock. Summary maintenance does not acquire it. Arbitrary host edits are not covered. Requires OS advisory-lock semantics and common root. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Nonblocking conversation on memory failure; provider | Exception catches, asynchronous process launch, timeout and bounded shutdown join; best effort | Raw-hook and read-tool failures mostly degrade to logs/empty or error responses. Synchronous phase-2 recall still executes inline; host's advertised wait limit is not implemented as a plugin timer. Imports/schema rendering/thread startup and native-hook preconditions are not all inside the same catch. Not an all-method no-exception proof. | implementation conclusion status: wired; operation conclusion status: uninspected |
| No secrets retained; secret layer and hook callers | Regex masking in raw writer; rejection at note tool and native hook; best effort | Recognized patterns only. `Registre.noter` itself does not filter; replay writes raw directly. Numbers such as IBAN/telephone are intentionally allowed. Requires host callers to use guarded paths, not direct filesystem writes. | implementation conclusion status: wired; operation conclusion status: uninspected |
| Confidential content stays in conversation; host-model instruction | Tool schema description and consolidation privacy prompt; policy | Retrieval is not an exfiltration gate, and the auxiliary model receives source text. Host tools, model behavior and provider data handling must supply any actual confinement. | policy conclusion status: claimed; operation conclusion status: uninspected |

The failure policy is not transactionality. Invalid JSON leaves inputs pending, but an otherwise valid response advances all selected batches and notes even when particular fragments were rejected or no page cites a note. Summary failure leaves older summaries; graph failure leaves written pages and continues. A Git error is reported, not used to roll back page admission. A crash between page writes and progress journals can leave partial state; source-level deduplication and pending-input retry are not an atomic commit protocol (SRC-1, `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/registre.py`).

### Alternate admission, maintenance and evaluation

Explicit note/native-memory entry is a second admission mechanism, not merely raw conversation with another label. Operator maintenance can alter timestamps, concept assignments, summaries and graph state independently of fresh conversation. These paths and their rejection/recovery differences are retained in [RT-RTE-state-maintenance](#rt-rte-state-maintenance). They admit retained knowledge and retrieval capabilities; the inspected production loop does not choose or install new plugin source. Source/config deployment remains an operator/host responsibility, not an autonomous production-machinery updater established here (SRC-1, `plugin/exia_seed/outils/ancrer.py`, `plugin/exia_seed/outils/concepts.py`, `plugin/exia_seed/outils/fiches.py`, `plugin/exia_seed/outils/graphe.py`).

The shipped benchmark drivers also construct and later consume state. LoCoMo preparation writes raw session files directly, in chronological order, then consolidates; its two-person mode sets no agent while LongMemEval sets user/assistant roles. These drivers bypass live raw secret masking and retention-command handling, not the fragment checker. Preparation can replace the production selection rule with a historical selective rule. Responses may consume precomputed retrieval contexts, a model-selected subset of index pages, all retained facts or the full transcription. The answer judge uses reference answers for categories 1–4 and a separate abstention rule for category 5. These are bounded evaluation modes, not the open assistant's answer oracle or a deployed promotion gate ([RT-RTE-benchmark-replay](#rt-rte-benchmark-replay)).

Nexa reconsolidation replays copied history day by day through the same consolidator with a benchmark model client and stops after repeated nonprogress. The model-comparison driver instead imports a separate `/banc/plugin` copy; its production/adapted-prompt behavior cannot be inferred as execution of the frozen plugin. It writes copied memories and reports, not live installation. LongMemEval's launcher mounts plugin code read-only and benchmark state writable in disposable containers, running as root; only factice mode disables network. That is benchmark packaging, not evidence of production process isolation (SRC-1, `banc/nexa/reconsolider.py`, `banc/modeles/consolider.py`, `banc/longmemeval/lancer.sh`).

Added inspection under SRC-1 comprises the complete provider, config, ingestion, register, secrets, consolidation, recall, query, summary and four maintenance-tool bodies; English consolidation/tool/summary prompt ranges; graph page-reader range; LoCoMo preparation/response/judge/model client; LongMemEval launcher; Nexa and model comparison consolidation drivers. These provide implementation and doctrine, not observed-run or causal-experiment evidence. French prompt variants, remaining benchmark baselines and diagnostics, complete graph/engine internals and host runtime were not exhaustively traced. Their uninspected details prevent claims of exhaustive algorithm equivalence, model/provider performance or universal deployment guarantees. Memory revisions and detailed retained-object assessment are left to the memory analyst.

## Shared records

### Components

#### RT-CMP-consolidation-model
Label: Configured consolidation model

The distributed-parametric component is the external model selected by `appel_llm_hermes`; its numerical weights live at the provider, not in the Markdown memory. Production resolves provider and default model from Hermès configuration on calls, with an optional configured consolidation-model override. This callable also generates page identity summaries. No parameter-update operation is implemented by this adapter; provider internals, training and exact weights remain uninspected. Neither exact weight version nor immutable endpoint is pinned. A configured name or default can resolve differently across calls or deployments. Host fallback behavior cannot be independently established (SRC-1, `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/outils/consolider.py`, `plugin/exia_seed/config.py`).

> rep = call_llm(task="exia_seed_consolidation",
>                        provider=modele_cfg.get("provider") or None,
>                        model=modele or modele_cfg.get("default") or None,
>                        messages=messages, reasoning_config=parse_reasoning_effort(effort), timeout=timeout)
> --- `plugin/exia_seed/consolidation.py`

#### RT-CMP-benchmark-model
Label: LoCoMo benchmark model client

The live benchmark client sends messages to OpenAI chat completions, returning text plus usage and retaining output in JSONL cache files. The model and judge are distributed-parametric services with provider-side weight storage. Parameters are not updated by this client, exact weights are not pinned and mutable model names can resolve to changed service versions. The `FACTICE` alternative is a symbolic regex-driven stub, not a parametric model. Benchmark model internals and actual service execution are uninspected (SRC-1, `banc/locomo/modele.py`).

> if FACTICE:
>         texte, usage = _factice(messages, role), {"prompt_tokens": sum(len(m["content"]) for m in messages) // 4,
>                                                   "completion_tokens": 20}
>     else:
>         texte, usage = _api(messages, modele, max_tokens, json_seul)
> --- `banc/locomo/modele.py`

### Operative objects

none declared in this member

### Routes

#### RT-RTE-conversation-ingest
Label: Primary conversation capture and batch closure

The host owns the next conversational turn. EXIA SEED's symbolic hook policy records primary-session identity and speaker labels, transforms voice/envelope content and secret patterns, then appends natural-language lines to raw Markdown under a file lock. State/progress and withdrawal identities are JSON/JSONL. Retention commands can omit the current turn and record withdrawal of the previous one; withdrawal does not erase the immutable raw file. Threshold/day/session triggers close and sign batches. This route admits source material automatically, not subject-page knowledge. The user can request omission through recognized text; software recognizes it, and no per-content approval is requested for ordinary turns. There is no answer oracle (SRC-1, `plugin/exia_seed/__init__.py`, `plugin/exia_seed/ingestion.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: `sync_turn` returns no content to the host; counters/logs record failures.
- Later read-back: closed batches reach the consolidator; selected facts can later reach recall and tools through page admission.
- Delegated visibility: raw capture excludes ordinary tool messages; consolidation gets selected conversation lines, not the whole foreground context.
- Selection predicate: primary-context gate, retention-command detection, envelope/voice handling and recognizable-secret masking; only pending closed batches are later eligible.
- Invalidation or expiry: withdrawal journal excludes referenced raw lines from later consolidation; it is not automatic erasure of previously consolidated prose.
- Activation or effect: appends source files, renames closed batch and updates hash/progress records; downstream behavioral activation is unobserved.
- Evidence limits: source hook behavior only; host completeness, correct speaker identity, actual capture and filesystem durability are not observed.

> if not (self._actif and self._brut):
>             self._compteurs["tours_ignores"] += 1
>             return
> --- `plugin/exia_seed/__init__.py`

> texte_utilisateur, n1 = masquer(texte_utilisateur)
>         texte_agent, n2 = masquer(texte_agent)
> --- `plugin/exia_seed/ingestion.py`

#### RT-RTE-register-admission
Label: Explicit and native-memory notes

Tool calls can propose notes on user request or the host agent's initiative; native-memory callbacks mirror supplied content, prefixing removals rather than deleting the EXIA note. The provider rejects recognized secrets before appending through `Registre.noter`. The register escapes structural Markdown/comment delimiters, normalizes privacy and node hints, generates an ID and appends under a lock. All initialized agent contexts can use it. Consolidation treats these sources as non-agent, so the raw agent-only exclusion does not imply human confirmation of every note. Code admits the entry and model/code later select page content; a user starting a workflow is not per-entry human approval. Open operation has no reference-answer oracle (SRC-1, `plugin/exia_seed/__init__.py`, `plugin/exia_seed/registre.py`, `plugin/exia_seed/consolidation.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: note tool returns JSON success plus ID or an error; native callback returns no note content.
- Later read-back: pending register text is sent to consolidation and may enter later page consumers.
- Delegated visibility: notes are shared through the common memory root, not restricted to primary-context capture.
- Selection predicate: nonempty note and provider-level secret rejection; consolidation uses IDs absent from the integration journal.
- Invalidation or expiry: integration journal removes entries from pending selection; native `remove` adds a descriptive note rather than retracting prior pages.
- Activation or effect: appends retained source text; actual use of resulting facts is unobserved.
- Evidence limits: host tool principal/authentication and human review are not established; direct `Registre.noter` does not itself enforce the secret filter.

> for e in notes:
>             ref = f"registre:{e['id']}"
>             sources[ref] = (e["texte"], False)
> --- `plugin/exia_seed/consolidation.py`

#### RT-RTE-page-consolidation
Label: Model proposals admitted into subject pages

Trigger: pending closed batches or notes, via automatic subprocess, nightly forced closure, manual CLI or direct consolidator callers. The file lock serializes cooperating consolidators. Sources are budget-selected raw lines plus pending notes; the first raw lot can exceed the remaining budget, and notes are all appended. Existing page names/aliases and concept vocabulary are included, not full raw history. The selected model proposes facts and concepts; deterministic code decides admission and page routing. English prompt guidance asks for exact citations, exhaustive concrete facts, dates, privacy and behavioral corrections; it does not establish compliance. No expected-answer oracle checks these proposals. Citation and date checks reject or strip particular material; no human approval gate is called. Summary generation is an additional model pass over bounded page excerpts, not proof that every page fact reaches it (SRC-1, `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/langues/en.py`, `plugin/exia_seed/fiches.py`).

The admitted change is retained page prose and metadata, summaries/keywords and used new concepts; graph/index/provenance follow. It changes later available knowledge/instructions rather than provider weights. Invalid JSON remains pending; accepted/rejected fragments in a parsed response still lead to progress advancement. Summary exceptions leave previous summaries, graph exceptions do not undo pages, Git records history best-effort. There is no automatic rollback selection; histories afford operator recovery but do not prove successful recovery. The optional adapted prompt and model configuration are operator-supplied variation, not an automatic successor-selection loop.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: report dict from `consolider`; CLI prints only anomalous statuses unless verbose, then returns zero on its normal completion path.
- Later read-back: subject pages, concepts and summaries reach graph/cache reconstruction and later recall/search/read.
- Delegated visibility: the model gets selected source lines, catalogues and prompts in separate client messages; it receives no foreground tool history or general execution authority from this code.
- Selection predicate: pending journals and budget; fact checker; alias resolution; only used new concepts persist.
- Invalidation or expiry: processed input journals stop automatic reconsideration even for rejected fragments; no automatic semantic invalidation or rollback of older contradictory facts is shown by this admission body.
- Activation or effect: writes pages and derived state; potential later instruction authority is recorded in RT-BAP-recalled-content, not observed compliance.
- Evidence limits: model output correctness, successful service calls, all-or-nothing crash recovery and benefit remain unobserved.

> ok, raison = self._controler(frag, sources)
>             if not ok:
>                 rejetes.append((frag.get("fait", "")[:120], raison))
>                 continue
> --- `plugin/exia_seed/consolidation.py`

> for e in notes:
>             self.registre.marquer_integre(e["id"], cites.get(e["id"], ""), lot_id)
> --- `plugin/exia_seed/consolidation.py`

> if len(t) + 3 > reste:
>             break
> --- `plugin/exia_seed/fiches.py`

#### RT-RTE-memory-delivery
Label: Automatic recall and explicit query consumption

Host query or tool call triggers a symbolic retrieval policy. The common cache loads pages, concept fields, edge proofs, aliases and SQLite in-memory FTS; FCM propagation and lexical coverage rank facts. Code owns candidate selection; the foreground model owns whether to call tools and what to do with results. Automatic recall suppresses future facts and expired intentions, uses a per-node cap and estimated token budget, then phase-2 `souvenirs` selects subject summaries and prioritizes procedural facts within each subject. Explicit search uses a broader BM25 pool, concept credit and trails; read resolves a subject then returns sections and neighbor trails. Neither query API is a general action executor. No answer oracle is used (SRC-1, `plugin/exia_seed/rappel.py`, `plugin/exia_seed/requete.py`, `plugin/exia_seed/__init__.py`).

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: automatic phase 1 returns empty; phase 2 returns a natural-language block; tools return JSON facts/sections/trails or errors.
- Later read-back: durable pages and summaries are consumed on later invocations; in-process previous-topic priming may influence subsequent recall for configured minutes.
- Delegated visibility: any initialized context receives explicit read tools; automatic recall is primary-context only; actual host context placement remains external.
- Selection predicate: automatic alias/lexical/graph activation, thresholds and budgets; explicit search/read have distinct lexical/subject and trail policies, not identical exclusion coverage.
- Invalidation or expiry: cache uses edge-file modification time, priming expires by time; expired intentions are filtered only on automatic recall. Future-date exclusion is not applied to every read trail/fallback.
- Activation or effect: returns selected knowledge and potential conduct rules, while logging query/recall metadata; model compliance and useful action are unobserved.
- Evidence limits: estimated token ceilings do not establish a final host-token bound; summaries added in phase 2 and explicit read branches have different budgets. Actual deployed phase is not supplied.

> if int(self._reglages.get("phase") or 1) >= 2:
>             return self._souvenirs(r, query, texte)
> --- `plugin/exia_seed/__init__.py`

> if self._memoire is None or etat != self._empreinte:
>                 self._memoire = Memoire(self.racine, self.implicites)
>                 self._empreinte = etat
> --- `plugin/exia_seed/rappel.py`

> if m.fiches.get(n):                                                 # docs/12 : ce que c'est, avant les détails
>             lignes.append(f"  {m.fiches[n]}")
> --- `plugin/exia_seed/rappel.py`

#### RT-RTE-state-maintenance
Label: Operator-selected memory maintenance

CLI callers select a root or configured home and opt into mutations. `concepts.py --ecrire` supplies seed assignments or asks a model for concept tags, checks known concepts and count, writes metadata/thesaurus and commits; it holds the consolidation lock. `ancrer.py --ecrire` deterministically derives missing utterance timestamps from cited raw/register sources under that lock. `graphe.py --calculer` rebuilds graph state under the same lock. `fiches.py` proposes summaries by default and writes accepted summaries/keywords with `--ecrire`; its body does not take the consolidation lock or rebuild graph/index. Thus summary maintenance is a material alternate writer and can leave an already loaded cache stale until a graph change. The caller authorizes the operation, not each model-produced phrase. Summary controls can veto names/numbers/paths/length; concept tagging uses shape/known-concept filtering rather than the fact citation checker. No reference-answer oracle is supplied. Human review of dry-run proposals is afforded, not mandatory before write mode (SRC-1, `plugin/exia_seed/outils/concepts.py`, `plugin/exia_seed/outils/ancrer.py`, `plugin/exia_seed/outils/graphe.py`, `plugin/exia_seed/outils/fiches.py`, `plugin/exia_seed/fiches.py`).

Guidance persists as shipped prompts and code; changes persist as page metadata, thesaurus or graph files. These commands do not automatically improve their own prompts or install a successor executable. Timestamp backfill leaves existing timestamps; concepts leave already tagged facts; summary refresh selects stale/missing summaries unless `--toutes`. Recovery is operator rerun/history, not a demonstrated rollback protocol. These are open maintenance requests, not bounded answer-scored experiments.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: maintenance reports/proposals and optional output JSON; accepted write mode mutates files.
- Later read-back: changed metadata affects later page/graph/cache consumers, subject to graph-timestamp invalidation.
- Delegated visibility: model tagging/summary calls receive selected facts or bounded page excerpts, not an entire host session.
- Selection predicate: explicit write/calculation flags, missing concepts/timestamps, stale summaries or all-page override.
- Invalidation or expiry: no automatic expiry of admitted tags/summaries; unchanged or rejected summaries retain old values.
- Activation or effect: changes retrieval-relevant retained content; no supplied later behavior demonstrates activation or benefit.
- Evidence limits: manual code/config edits and actual operator deployment are not observed; Git availability does not prove recovery.

> if ecrire:
>                 _poser(p, fiche, date, mots)
>                 p.ecrire()
> --- `plugin/exia_seed/fiches.py`

#### RT-RTE-benchmark-replay
Label: Constructed-memory evaluation and prompt variants

The operator supplies datasets, run selection, model and variant; preparation writes session files and progress-chain entries directly, then invokes consolidation. Variant code can wrap the language mask to replay the historical selective rule; it does not modify the shared mask or production installation. Responses consume generated contexts or other selected modes, then judging compares answers with dataset gold. The model proposes benchmark answers and judge labels; code parses labels, votes across passes and writes reports. Category 5 uses a regex abstention decision. No software admission of measured winners into live plugin code/config is wired in the inspected driver bodies. Expected answers are the dataset's `gold`, delivered to the judge, not the production consolidation model. This is a bounded evaluation mode distinct from open user operation (SRC-1, `banc/locomo/preparer.py`, `banc/locomo/repondre.py`, `banc/locomo/juger.py`, `banc/locomo/modele.py`).

Rejection ability includes obsolete-variant errors and budget stops; retry reads progress and call caches. The local spending check happens before calls outside the network operation and is not a reserved concurrent-spend ceiling. Call cache keys include messages/model/generation controls; `passe` deliberately differentiates judge passes. No observed score or causal improvement is established. Copied-history Nexa replay and separate-plugin model comparison are related shipped modes, with the source-copy limits described above.

- implementation conclusion status: wired
- operation conclusion status: uninspected
- Immediate return: persisted memory, response/judgment JSONL and printed status/spending reports.
- Later read-back: sessions see earlier consolidated nodes/concepts; later benchmark response/judge stages consume generated memories and answers; call caches survive relaunch.
- Delegated visibility: independent conversations/questions can run on thread pools; each model request receives its explicit messages, and outputs return through cached text/results rather than full worker context.
- Selection predicate: run IDs, chronological sessions, role mode, prompt variant, response engine/scale and evaluation category.
- Invalidation or expiry: prepared sessions skip completed inputs; call cache keyed by request content/controls; copied runs separate experimental variants.
- Activation or effect: creates and evaluates test memories, not demonstrated deployment of winning changes.
- Evidence limits: datasets, generated runs, actual provider calls and separate production-plugin copy are not frozen evidence; no reproducible score or component causal effect is asserted.

> return _CACHE[cle]["texte"]
> --- `banc/locomo/modele.py`

> question=q["question"], gold_answer=q["gold"], generated_answer=reponse)}],
>         "juge", max_tokens=200, json_seul=True, passe=passe)
> --- `banc/locomo/juger.py`

### Claims

#### RT-CLM-citation-control
Label: Citation control versus semantic support

The source introduces a deterministic guard as rejecting fragments citing an unsupplied source, invented numbers/names, insufficient word overlap or only agent speech. Actual code rejects absence of any valid source, not every invalid member of a mixed list. It checks numbers, selected capitalized words and five-character-root overlap, not entailment, user confirmation semantics or all metadata. This establishes a software veto on defined lexical failures, not truth or faithful confirmation. SRC-1 implementation and doctrine: `plugin/exia_seed/consolidation.py`, `plugin/exia_seed/langues/en.py`.

> if cle in sources:
>                     textes.append(_temps.sans_horodatage(sources[cle][0]))
>                     que_agent = que_agent and sources[cle][1]
>         if not textes:
>             return False, "aucune source valide citée"
> --- `plugin/exia_seed/consolidation.py`

> if que_agent:
>             return False, "repose seulement sur des paroles de l'agent"
> --- `plugin/exia_seed/consolidation.py`

### Evidenced absences

none declared in this member

### Behavioral-authority paths

#### RT-BAP-recalled-content
Label: Retained facts and conduct rules reaching a host model

Consumer: the Hermès foreground model, or an explicitly querying agent context. Channel: tool JSON or phase-2 natural-language recall block; summaries and procedural facts are included by selection code. Force: model-interpreted knowledge and behavioral guidance, not an executable privilege check. Horizon: later turns/sessions using the same retained root, with cache reconstruction controlled by graph timestamp. This path is wired as delivery, but actual context placement, compliance and changed behavior remain unobserved. It can carry user corrections of assistant behavior; merely retaining such a correction does not establish successful learning or exercised self-improvement. No content-directed theory-criticism loop is claimed by this runtime account (SRC-1, `plugin/exia_seed/__init__.py`, `plugin/exia_seed/rappel.py`, `plugin/exia_seed/requete.py`, `plugin/exia_seed/langues/en.py`).

> 7. An ordinary event does NOT create an "evenement" node: attach it to the entity concerned, section "episodic". "etat_agent" = a lasting correction of the assistant's behaviour by the user.
> --- `plugin/exia_seed/langues/en.py`

> fs = sorted(groupes[n], key=lambda t: (m.faits[t[1]]["section"] != "procedural", -t[0], t[1]))[:max(1, faits_par_sujet)]
> --- `plugin/exia_seed/rappel.py`

## Annotations

none
