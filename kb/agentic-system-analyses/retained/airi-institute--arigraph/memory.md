---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "AriGraph memory: attempt-local facts, unretracted episodes, retrieval metadata and alternative game and QA retention paths."
run-id: AAS-2026-10-12-arigraph-fd0f6f1c1383-01
source-identity: https://github.com/AIRI-Institute/AriGraph
reviewed-boundary: e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2
---

# AriGraph memory report

## Boundary and evidence

This report covers the memory state and later consumers inside the supplied whole-system [boundary](boundary.md#boundary-and-evidence). SRC-1 is the repository at the exact revision above. Memory scope includes the main game graph, QA admission and retrieval, graph navigation/exploration, recent history and plans, alternative full-history/summary/smart-RAG drivers, Hypergraph, the auxiliary ObservedGraph API, logging and the replacement evaluator. It excludes external provider internals, externally resolved weights, the paper/site, bytecode-only implementations and task-rule verification. Those exclusions prevent provider-storage, checkpoint-provenance, historical-variant and exhaustive task-fidelity conclusions.

Direct reads here cover `graphs/contriever_graph.py`, `graphs/parent_graph.py`, `graphs/hypergraph.py`, `graphs/lazy_graph.py`, `utils/retriever_search_drafts.py`, `utils/contriever.py`, `utils/observedgpaph.py`, `prompts/prompts.py`, `musique_test_big.py` and `pipeline_graph_evaluation.py`; bounded ranges cover game decision/update dispatch, alternative driver retention/consumption, and parsing, logging, observation cleanup and episode ranking in `utils/utils.py`. All are SRC-1 implementation except prompt instructions, which are doctrine/design. Runtime findings supply model fixity, human-driver progression, authored system prompts and bounded recorded-operation evidence; they are distinguished below. No target execution or new causal experiment was performed.

A root tree inventory and repository-wide Python search checked constructors, snapshot/cached-state accessors, serialization calls, `reflex_prompt`, CLI-parser and tool-registration terms. Together with the root driver traces, these establish script entry points rather than a discovered CLI dispatch or registered provider-tool memory surface. The search is bounded source inspection, not proof about undocumented deployments or bytecode. Available task datasets, remaining logs, diagram assets and support training utilities were not inspected here; they do not supply conclusions about aggregate accuracy, diagram semantics or external checkpoint history.

| Entry point / operation | SRC-1 path and inspection basis | Covering records / limit |
|---|---|---|
| Main game admission, replacement, retention | Direct: `graphs/contriever_graph.py`, `utils/utils.py`, `prompts/prompts.py`; driver ranges in `pipeline_arigraph.py` | [RT-RTE-game-memory](runtime.md#rt-rte-game-memory), [MEM-OBJ-triplets](#mem-obj-triplets), [MEM-OBJ-obs-episodic](#mem-obj-obs-episodic), [MEM-OBJ-graph-embeddings](#mem-obj-graph-embeddings) |
| Semantic and episodic read-back | Direct: `utils/retriever_search_drafts.py`, `utils/contriever.py`, `utils/utils.py`, `graphs/contriever_graph.py` | Annotations on [RT-RTE-game-memory](runtime.md#rt-rte-game-memory) and [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle) |
| QA additive admission, reset, answer and metrics | Direct: `musique_test_big.py`, `graphs/contriever_graph.py` | [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle); dataset contents not reassessed, preventing dataset-integrity conclusions |
| Navigation and exploration | Direct: `graphs/parent_graph.py`, game dispatch/exploration ranges | [RT-RTE-graph-navigation](runtime.md#rt-rte-graph-navigation), [MEM-OBJ-triplets](#mem-obj-triplets) |
| Recent history and feedback plan | Direct driver ranges; supplied runtime plan record | [MEM-OBJ-history](#mem-obj-history), annotation on [RT-OBJ-plan](runtime.md#rt-obj-plan) |
| Episode snapshots and score histories; direct state accessors | Direct: `graphs/contriever_graph.py`; repository-wide Python identifier search | [MEM-OBJ-episodic-snapshots](#mem-obj-episodic-snapshots), [MEM-ABS-state-readers](#mem-abs-state-readers); no shipped snapshot replay consumer found |
| Full history | Direct retention/consumer ranges: `pipeline_fullhist.py` | [RT-RTE-full-history](runtime.md#rt-rte-full-history), [MEM-OBJ-observations](#mem-obj-observations) |
| Summary compression | Direct retention/consumer ranges: `pipeline_summary.py`; system-prompt intent supplied by runtime | [RT-RTE-summary-cycle](runtime.md#rt-rte-summary-cycle), [MEM-OBJ-summary](#mem-obj-summary) |
| Smart-RAG raw history and access metadata | Direct retention/ranking ranges: `pipeline_smartrag.py` | [RT-RTE-smart-rag](runtime.md#rt-rte-smart-rag), [MEM-OBJ-rag-observations](#mem-obj-rag-observations), [MEM-OBJ-rag-metadata](#mem-obj-rag-metadata) |
| Hypergraph admission, thesis/event deletion and read API | Direct: `graphs/hypergraph.py`, thesis-search helper, prompts | [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update), [MEM-OBJ-hypergraph-content](#mem-obj-hypergraph-content), [MEM-OBJ-hypergraph-index](#mem-obj-hypergraph-index); shipped planner delivery unestablished |
| Auxiliary observation graph mutation/display | Direct: `utils/observedgpaph.py`; repository-wide constructor search | [MEM-OBJ-observed-graph](#mem-obj-observed-graph), [MEM-RTE-observed-update](#mem-rte-observed-update); no shipped root consumer found |
| Evaluation and cleanup | Direct evaluator/LazyGraph; clear/delete methods | [RT-RTE-graph-evaluation](runtime.md#rt-rte-graph-evaluation); diagnostics do not admit revisions into production |
| Human play and unused reflexion | Supplied runtime findings plus named-prompt/constructor search | [RT-RTE-human-play](runtime.md#rt-rte-human-play), [RT-ABS-reflex-invocation](runtime.md#rt-abs-reflex-invocation); helpers are not invoked by the human loop |
| File logging and JSON capability | Direct `utils/utils.py`; call search | [MEM-OBJ-logs](#mem-obj-logs), [MEM-ABS-state-readers](#mem-abs-state-readers); file writes are not restart graph persistence |
| Remote/local generation and retriever model | Supplied runtime component findings; local adapter and Retriever directly read | [RT-CMP-gpt-agent](runtime.md#rt-cmp-gpt-agent), [RT-CMP-llama-agent](runtime.md#rt-cmp-llama-agent), [RT-CMP-retriever](runtime.md#rt-cmp-retriever); provider retention and exact upstream weights unresolved |

## Core ideas

1. **Facts and episodes have different withdrawal rules.** Game maintenance removes selected triplets and their fact embeddings, but leaves the originating observation text and its extracted-fact list available for episodic retrieval. A fact deleted as outdated can therefore survive in a later model's episode context. This is historical evidence, not a globally synchronized truth view: [MEM-OBJ-triplets](#mem-obj-triplets), [MEM-OBJ-obs-episodic](#mem-obj-obs-episodic).
2. **Selection is a chain, not one similarity lookup.** Model-generated entities/depths drive recursive fact search; episodic ranking combines fact overlap with plan/question embedding similarity. Game overlap uses the *previous* selected subgraph; QA uses the newly retrieved subgraph. Semantic top six is per expanded query, not a global six-fact limit. Episode top-k and recent-text filtering are separate operations: annotations on [RT-RTE-game-memory](runtime.md#rt-rte-game-memory) and [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle).
3. **Retention mostly ends at an attempt or QA task.** Process-local stores and snapshots are distinct from textual files. The scripts construct/reset memory rather than loading graph checkpoints. Summary and smart-RAG also retain derived behavior-shaping state within attempts, but neither establishes improved performance: [MEM-OBJ-summary](#mem-obj-summary), [MEM-OBJ-rag-metadata](#mem-obj-rag-metadata), [MEM-ABS-state-readers](#mem-abs-state-readers).
4. **Admission policy is model guidance with narrow software checks.** Maintainers author prompts; computational callers admit parsed facts, summary text and importance values without per-item human approval. Hypothesis wording and conservative replacement are requested, not independently verified. Actual decision consumers receive fact/episode strings as informational context; navigation instead consumes matching spatial labels through fixed software rules. See [RT-BAP-memory-decisions](runtime.md#rt-bap-memory-decisions) and [RT-RTE-graph-navigation](runtime.md#rt-rte-graph-navigation).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-triplets
Label: ContrieverGraph triplets

Source-native identity: `self.triplets`, normalized subject/object/label triples in a Python list. Form: symbolic endpoints/structure and spatial labels for fixed graph consumers; natural-language fact labels when serialized for models. Substrate: process memory. Lineage: model extraction from cleaned game observations or QA paragraphs, plus deterministic forward/reverse location edges derived from movement. Compared with [RT-RTE-game-memory](runtime.md#rt-rte-game-memory) and [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle), this is their shared retained fact object, not a duplicate route; no supplied operative-object counterpart exists. Navigation is a separate consumer of this same object.

Admission: code normalizes/deduplicates, ignores a raw `free` label, then appends; the model supplies content, not human approval. Game deletion ignores nonexistent entries and protects pairs of known locations; QA admission does not delete. Later consumers are extraction-example construction via earlier retrieval, replacement candidate selection, semantic retrieval, exploration and path computation. Facts supply interpreted knowledge to models and fixed relation inputs to navigation. No model explanation, validity interval, source-document ID or contradiction rationale is stored in this list. Reset clears it. SRC-1, `graphs/contriever_graph.py`, `graphs/parent_graph.py`, `utils/utils.py`.

> if triplet not in self.triplets:
>     self.triplets.append(triplet)
>     self.triplets_emb[self.str(triplet)] = self.get_embedding_local(self.str(triplet))
> --- `graphs/contriever_graph.py`

> if triplet in self.triplets:
>     self.triplets.remove(triplet)
>     self.triplets_emb.pop(self.str(triplet))
> --- `graphs/contriever_graph.py`

#### MEM-OBJ-obs-episodic
Label: obs_episodic observation content and extraction lineage

Source-native identity: dictionary keys are complete observation/paragraph strings; each value's first element is the converted extraction list. Form: natural-language episode text and fact displays, with symbolic exact-string dictionary identity and list membership used for ranking. Substrate: Python dictionary/list memory. Numerical value elements are separately covered by [MEM-OBJ-graph-embeddings](#mem-obj-graph-embeddings). No supplied object counterpart; this is the episode content shared by [RT-RTE-game-memory](runtime.md#rt-rte-game-memory) and [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle).

Lineage: game text has step prefixes and first-observation task instructions, but admission precedes appending explicit inventory to planner text; QA uses paragraph text. The extracted list precedes deterministic movement additions and can include strings not finally admitted, including an ignored `free` fact. It is a lossy extraction association, not a validated provenance graph. Assignment overwrites an identical observation key rather than creating a distinct repeated-occurrence event. Graph deletion does not rewrite these lists or episode text. Raw here means retained input to extraction, not untouched environment output. Admission is driver/model/software-controlled. Selected dictionary keys reach planner/action or answer models as historical text, without an explicit stale-fact marker. SRC-1, `graphs/contriever_graph.py`, `pipeline_arigraph.py`, `musique_test_big.py`.

> obs_embedding = self.retriever.embed(observation)
> obs_value = [new_triplets_str, obs_embedding]
> self.obs_episodic[observation] = obs_value
> return new_triplets_raw, obs_value
> --- `graphs/contriever_graph.py`

#### MEM-OBJ-graph-embeddings
Label: Graph embeddings and episode vectors

Source-native identity: `triplets_emb`, `items_emb`, and second elements of `obs_episodic` values. Form: distributed-parametric dense representations; symbolic dictionary keys identify associated text. Substrate: NumPy arrays for fact/entity caches, PyTorch tensors for episode embeddings. Lineage: inference by [RT-CMP-retriever](runtime.md#rt-cmp-retriever) over normalized facts/entities or observation text. No new weight training occurs in these paths; upstream exact model/tokenizer revision is unpinned. This object is derived state, not the retriever component or readable fact content. It overlaps the game/QA route containers but no supplied object record.

Software creates caches on admission. Fact deletion pops its fact vector, but leaves entity vectors; clear removes all these stores. Semantic graph search actually re-embeds supplied fact strings through `Retriever.search`, rather than using `triplets_emb`; episode ranking uses stored episode vectors. The exposed `find_current_items` accessor can return selected entity vectors, but no shipped Python caller was found. Dense vectors have selection authority, not model-facing instructional force; their text keys are display/source associations, not an interpretable explanation of similarity. SRC-1, `graphs/contriever_graph.py`, `utils/contriever.py`, `utils/utils.py`.

> key_embeds = self.embed(key_strings)
> query_embeds = self.embed(query_strings)
> result = self.search_in_embeds(
>     key_embeds, query_embeds, topk, similarity_threshold, return_embeds, return_scores
> )
> --- `utils/contriever.py`

#### MEM-OBJ-episodic-snapshots
Label: obs_episodic_list and top_episodic_dict_list

Source-native identity: successive deep copies of the episode dictionary and stored ranking dictionaries. Form: copies of natural-language content, symbolic association keys and dense tensors; separate numeric ranking values are access metadata, not episode assertions. Substrate: process-local Python lists. Lineage: each game update after episode insertion. QA's additive method does not append these histories. No supplied object counterpart; the write is already quoted by [RT-RTE-game-memory](runtime.md#rt-rte-game-memory).

These accumulate automatically, but a repository-wide Python identifier search found no later consumer of either list outside their initialization/reset/appends. They are alternative retained snapshots, not demonstrated checkpoints for replay, rollback or decision delivery. Known main read-back uses the current dictionary, not these lists. Reset clears both. SRC-1, `graphs/contriever_graph.py`; [MEM-ABS-state-readers](#mem-abs-state-readers).

#### MEM-OBJ-history
Label: Main game bounded recent observations and actions

Part of: [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle)

This object is retained state within the supplied route, not another cycle. Source-native identity: `observations` and `history` lists in the main driver. Form: natural-language observations/actions plus symbolic list order/slicing. Substrate: attempt-local process memory. Code appends the inventory-augmented current observation and chosen action, then retains the default last five entries. `history` is joined into planner/action requests. `observations` supplies the episode exclusion list, a separate selection consumer. These traces can expose earlier behavior but are not distilled guidance. Admission is automatic append, not per-content human approval. Attempt reset clears both; no semantic revision or rollback. SRC-1, `pipeline_arigraph.py`; [RT-RTE-game-cycle](runtime.md#rt-rte-game-cycle) supplies the append/slice quote.

#### MEM-OBJ-observations
Label: Full-history observations

Part of: [RT-RTE-full-history](runtime.md#rt-rte-full-history)

Source-native identity: the full-history driver's `observations` list, its retained trace state. Form: natural-language observation/action entries and symbolic ordering. Substrate: attempt-local Python list. Lineage: cleaned, step-prefixed, inventory-augmented observation plus chosen action appended before environment execution. Admission is deterministic driver append. Later planner/action invocations interpolate the entire list; no ranked selection, compression or semantic veto. This is distinct from main-driver bounded history and smart-RAG tuples. Reset discards it; provider context handling is external and does not establish that every character is effectively used. SRC-1, `pipeline_fullhist.py`; [RT-RTE-full-history](runtime.md#rt-rte-full-history) supplies the append quote.

#### MEM-OBJ-summary
Label: Summary baseline summary

Part of: [RT-RTE-summary-cycle](runtime.md#rt-rte-summary-cycle)

Source-native identity: `summary` string, seeded as `Yet nothing`. It is the route's retained derived content, not another update route. Form: natural-language compressed memory. Substrate: Python string and textual log copy. Lineage: previous summary, bounded observation/action history, goal and current inventory-augmented observation. Each model response wholly replaces the summary and reaches current planner/action and the next summarizer. Authorship is computational; code admits returned text without a semantic check or human approval. Maintainers author the guidance, not each summary. The contract does not require retaining the summarizer's reasons; generated reasons may appear in text, but no separate rationale store or reader is wired. Fidelity, uptake and improvement are unobserved. SRC-1, `pipeline_summary.py`; [RT-RTE-summary-cycle](runtime.md#rt-rte-summary-cycle) supplies generation/assignment passages.

> summary = "Yet nothing"
> --- `pipeline_summary.py`

#### MEM-OBJ-rag-observations
Label: Smart-RAG observation and action content

Part of: [RT-RTE-smart-rag](runtime.md#rt-rte-smart-rag)

Source-native identity: tuple fields zero and four in the smart-RAG `observations` list. Form: natural-language cleaned/step-prefixed/inventory-augmented observation and action text. Substrate: attempt-local list/tuple memory. Lineage: driver trace appended after choosing an action and rating importance, before executing the action. Consequently each entry pairs a pre-action observation with the proposed action, not a validated action outcome. Software admits it; no content gate or subsequent revision. Retrieval returns formatted text/action pairs to planner/action. Metadata fields have different consumers and are declared separately below. SRC-1, `pipeline_smartrag.py`.

> score = get_score(observation, plan0)
> observations.append((observation, step, score, current_emb, action))
> --- `pipeline_smartrag.py`

#### MEM-OBJ-rag-metadata
Label: Smart-RAG step importance and embedding metadata

Part of: [RT-RTE-smart-rag](runtime.md#rt-rte-smart-rag)

Source-native identity: tuple fields one through three, `step`, `score`, `current_emb`. Form: symbolic step/integer importance and distributed-parametric dense embedding. Substrate: Python numeric fields and NumPy arrays. Lineage: step from driver; importance from model text's first digit sequence; embedding from observation plus the *old* plan. Importance is subsequently requested with the newly generated plan. Code does not enforce the requested 1–10 range. This is retained access metadata, not a replacement observation or a human verdict.

Later software combines min-max-normalized recency decay, importance and cosine similarity to choose text/action entries. The numerical values influence selection but are not delivered as factual memory assertions. No importance explanation persists in the tuple; only the parsed integer is logged. No metadata revision or metric-fed optimization is wired. Source passage for ranking is in [RT-RTE-smart-rag](runtime.md#rt-rte-smart-rag); SRC-1, `pipeline_smartrag.py`.

> score, cost = agent_score.generate(prompt, t = 0.4)
> score = int(re.findall(r"\d+", score)[0])
> log("Score: " + str(score))
> return score
> --- `pipeline_smartrag.py`

#### MEM-OBJ-hypergraph-content
Label: Hypergraph thesis entity and event names

Part of: [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update)

Source-native identity: names in `Hyperedge`, `Entity`, `Event`, with dictionaries `thesises`, `entities`, `events`. Form: natural-language thesis/event content and entity labels, normalized to lowercase/stripped strings. Substrate: process-local class instances/dictionaries. Lineage: extracted thesis sentences/entities and input observation as event. Model proposes content/removals; code applies parsed removals then adds names. No item-level human review or semantic oracle. The supplied route container is the closest record, not an object duplicate.

The read API returns selected thesis names and event texts. Deleting a thesis removes its object and incidence links but does not remove its parent event text or now-orphaned entity objects. Thus original observation content remains potentially returnable, as in the triplet episode store. Replacement rationale is logged rather than retained in thesis objects. No shipped root driver establishes later planner/action consumption. SRC-1, `graphs/hypergraph.py`.

> for parent in self.thesises[thesis_id].parents:
>     self.events[parent].delete_child(thesis_id)
> for child in self.thesises[thesis_id].children:
>     self.entities[child].delete_parent(thesis_id)
> self.thesises.pop(thesis_id)
> --- `graphs/hypergraph.py`

#### MEM-OBJ-hypergraph-index
Label: Hypergraph hash incidence and embeddings

Part of: [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update)

Source-native identity: `hash(name)` dictionary IDs, thesis `parents`/`children`, entity `parents`, event `children`, and each object's embedding. Form: symbolic incidence structure plus distributed-parametric dense vectors, separately consumed by BFS, overlap and embedding search. Substrate: Python hashes/lists, NumPy vectors in process memory. Lineage: code links normalized extracted names/events and embeds them. Hash IDs are process-native identities, not document IDs or portable checkpoint addresses. Computational admission merges links for existing names. Deletion changes links but leaves event/entity vectors and texts.

The API's thesis BFS and retrieval expansion use entity associations; event overlap uses child IDs and similarity uses stored event vectors. Other stored thesis/entity embeddings are not used by the inspected name-search helper, which re-embeds names. Event sorting is ascending before the history exclusion/prefix limit, so maximum-score-first delivery cannot be inferred from a relevance label. SRC-1, `graphs/hypergraph.py`, `utils/retriever_search_drafts.py`; [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update).

> ids = np.argsort(scores)
> return np.array([event.name for event in self.events.values()])[ids]
> --- `graphs/hypergraph.py`

#### MEM-OBJ-observed-graph
Label: ObservedGraph graph

Source-native identity: `ObservedGraph.graph`, a NetworkX MultiDiGraph. Form: symbolic entity/label edges for fixed mutation rules and human-readable display. Substrate: process memory. Lineage: caller-supplied full graph filtered by observation/action substring tests, or a caller-supplied replacement state. It is distinct from AriGraph model extraction, Hypergraph, and evaluator LazyGraph; no supplied object counterpart. The caller's full-graph provenance and human/computational identity are unresolved for this library surface. Known subsequent mutations remain inspectable despite that initialization uncertainty. SRC-1, `utils/observedgpaph.py`; [MEM-RTE-observed-update](#mem-rte-observed-update).

> self.graph = nx.MultiDiGraph()  # Using MultiDiGraph to handle multiple edges between two nodes
> --- `utils/observedgpaph.py`

#### MEM-OBJ-logs
Label: Logger text and JSON files

Source-native identity: Logger destination files, default `log.txt` and the exposed `history.json` write capability. Form: natural-language trace/decision displays and symbolic metrics; JSON is an optional serialized caller object, not a known graph-checkpoint format. Substrate: filesystem. Text calls append; JSON writes replace the file. Software performs I/O; originating drivers/models supply text, while authorship/control of arbitrary JSON payloads is caller-dependent. No inspected shipped Python call to `to_json` was found. Main runtime routes write observations, extracted/removal text, selected memory, plans/actions and costs; files can preserve more explanation than the live fact objects, but the running drivers do not reload those explanations. Source-supplied log samples are bounded evidence of attributed operation in runtime, not independent replay. SRC-1, `utils/utils.py`; closest counterparts are terminal outputs of the supplied game/QA/baseline routes, not a supplied file object.

> with open(self.path + "/" + filename, "a") as file:
>     file.write(text + "\n")
> --- `utils/utils.py`

> with open(self.path + "/" + filename, "w") as file:
>     json.dump(obj, file)
> --- `utils/utils.py`

### Routes

#### MEM-RTE-observed-update
Label: Auxiliary observed graph mutation and display

Endpoints/progression: caller supplies observation/action/full graph or entity/new state → fixed substring/edge rules → mutate `ObservedGraph.graph` → optional print. Owner: local API methods; unspecified external caller controls invocation. This is not a duplicate of [RT-RTE-game-memory](runtime.md#rt-rte-game-memory) or [RT-RTE-graph-evaluation](runtime.md#rt-rte-graph-evaluation): it uses neither model extraction nor the evaluator's LazyGraph. SRC-1, `utils/observedgpaph.py`.

- Immediate return: mutation methods have no explicit content return; `print_observed_graph` prints edge tuples.
- Later read-back: uninspected — graph state is accessible and displayable, but no shipped later model/agent invocation is wired to it.
- Delegated visibility: inapplicable — local synchronous library methods, not delegated workers.
- Selection predicate: observation endpoint substrings or self-state label match; action path tests source substring in observation and action; movement tests both endpoints in combined observations and direction label.
- Invalidation or expiry: selected endpoint pairs lose all prior parallel edges before observation/movement addition; action mutation removes matches; state replacement rewrites self-edges; caller controls lifetime.
- Activation or effect: fixed code changes local graph; display capability exists, without established behavioral consumption.
- Evidence limits: caller provenance, deployed use, reset horizon and environment-fact authenticity uninspected; root/Python constructor search found only the class definition.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Trigger/proposal/admission: explicit method call with supplied content; code selects/removes/adds edges deterministically. Human approval remains unresolved for the generic caller, not implicitly absent. No independent semantic veto, answer oracle, rollback or improvement loop is specified. Operating mode is caller-defined. Guidance is encoded substring/direction logic rather than a model prompt. Retained result is graph edges, not reasons for the mutation.

> def replace_state_change_edges(self, entity, new_state):
>     """Replace edges for entities that have changed state (e.g., unlocked)."""
>     for edge in list(self.graph.edges(entity, data=True)):
>         if edge[1] == 'itself':  # Check if the edge describes the state of the entity
>             self.graph.remove_edge(edge[0], edge[1])
>             self.graph.add_edge(edge[0], edge[1], label=new_state)
> --- `utils/observedgpaph.py`

### Claims

none declared in this member

### Evidenced absences

#### MEM-ABS-state-readers
Label: No shipped snapshot replay or cache-accessor callers

- implementation conclusion status: absent

Searched boundary: all Python source under SRC-1 at e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2, with root driver reads and identifier search for `obs_episodic_list`, `top_episodic_dict_list`, `get_triplets_by_ids`, `find_current_items`, `filter_associated`, `.to_json(` and `delete_all(`. Matches are snapshot initialization/reset/appends and method definitions, not shipped read/replay calls. This is distinct from [RT-ABS-reflex-invocation](runtime.md#rt-abs-reflex-invocation), which concerns a named prompt. SRC-1, `graphs/contriever_graph.py`, `graphs/parent_graph.py`, `utils/utils.py`.

The result prevents assigning snapshot replay/rollback, JSON graph checkpointing or cached-fact accessor delivery to the inspected scripts. It does not remove their library affordances or establish absence of external callers. Retained snapshot writes are witnessed by [RT-RTE-game-memory](runtime.md#rt-rte-game-memory); direct capability:

> def get_triplets_by_ids(self, best_ids):
>     return [self.triplets[i] for i in best_ids]
> --- `graphs/contriever_graph.py`

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-game-memory](runtime.md#rt-rte-game-memory)

Read-back detail: this is a driver request, not unsolicited memory delivery. Entity queries/depths select semantic fact strings by queue expansion: each popped query retrieves top six scored strings, rejects scores below 0.75 and enqueues unseen endpoints below depth. Union can exceed six facts; no global fact/token budget is implemented in the inspected helper. Returned facts exclude current extraction strings. Embedding input uses tokenizer truncation, whose effective checkpoint limit is external; semantic similarity scores are not truth confidence. SRC-1, `utils/retriever_search_drafts.py`, `utils/contriever.py`, `graphs/contriever_graph.py`.

> res = retriever.search(triplets, q, topk=topk, return_scores=True)
> for s, score in zip(res['strings'], res['scores']):
>     if score < post_retrieve_threshold: continue
>     v1, e, v2 = edge(s)
> --- `utils/retriever_search_drafts.py`

> inputs = tokenizer(list_of_strings, padding=True, truncation=True, return_tensors="pt").to(embedder.device)
> --- `utils/contriever.py`

Episode selection uses previous returned fact strings and old plan embedding against already stored episodes, before retaining the current observation. Match fraction times log extraction length is normalized and added to normalized embedding similarity; descending sum selects top-k (default two), then exact-text recent exclusion runs without backfill. Crucially the exclusion list holds inventory-augmented observations while episode keys were admitted before inventory append. The intended recent-episode exclusion is therefore not guaranteed by the shipped driver, even though the filter itself is wired. This qualifies the supplied route, not its identity. Source: SRC-1, `graphs/contriever_graph.py`, `pipeline_arigraph.py`, `utils/utils.py`.

> top_episodic = [item for item in top_episodic if item not in observations]
> --- `graphs/contriever_graph.py`

> subgraph, top_episodic = graph.update(observation, observations, plan=plan0, prev_subgraph=subgraph, locations=list(locations), curr_location=observation_processing(env.curr_location).lower(), previous_location=previous_location, action=action, log=log, items1 = items, topk_episodic=topk_episodic)
> observation += f"\nInventory: {inventory}"
> --- `pipeline_arigraph.py`

Selected facts and raw episode keys reach planner/action user messages. At the update consumer, previous facts provide extraction examples and old associated facts supply removal candidates. At downstream models they are informational inputs, not verified assertions; the inspected deletion parser only keeps the left side of `->`, so the proposed replacement relation and reasons do not gate retention. Parsed removals need not be checked against the candidate list or an admitted replacement. Graph truth, uptake and causal improvement remain unestablished. The retained reasons boundary is live fact/episode stores versus separately written model output logs.

#### On [RT-RTE-qa-cycle](runtime.md#rt-rte-qa-cycle)

Memory-specific distinction: `update_without_retrieve` uses extraction with empty examples, admits normalized facts and stores paragraph keys/extraction lists/vectors. The replacement request is commented out. `graph.clear()` removes task state, not model weights/provider state. Requested read-back uses question-derived entities and question embedding; unlike the game method, overlap uses the freshly retrieved subgraph and there is no recent-text exclusion. `retrieve_facts` is accepted but unused by the inspected method. Default two episode keys and unioned semantic fact strings reach answer model user context; paragraph/source IDs and retrieval scores do not. Dataset answers score output afterward and neither curate stored facts nor become a successor-admission gate. SRC-1, `graphs/contriever_graph.py`, `musique_test_big.py`; generation/metrics quotations are supplied by the route and [RT-BAP-memory-decisions](runtime.md#rt-bap-memory-decisions).

> top_episodic_dict = find_top_episodic_emb(associated_subgraph, deepcopy(self.obs_episodic), obs_plan_embeddings, self.retriever)
> top_episodic = top_k_obs(top_episodic_dict, k=topk_episodic)
> --- `graphs/contriever_graph.py`

#### On [RT-OBJ-plan](runtime.md#rt-obj-plan)

Memory-specific lineage/authority: planner response retains requested subgoals/reasons as a whole string, though compliance is not locally validated. That string reaches later entity/exploration/planning/action requests and its dense encoding influences episode selection. This is plan read-back alongside memory, not a static prompt. No independent criticism ledger or reason-aware selector is supplied; reasons are available to interpreting models insofar as present in the string. Subgraph/episode deletion does not rewrite the plan. SRC-1, `pipeline_arigraph.py`, `graphs/contriever_graph.py`; [RT-BAP-plan-decisions](runtime.md#rt-bap-plan-decisions) supplies the later-consumer witness.

#### On [RT-RTE-summary-cycle](runtime.md#rt-rte-summary-cycle)

Compression chain: cleaned current observation/inventory and last-five observation/action history + old summary → model-derived replacement → current planner/action and next summarizer. It is trace-fed memory transformation, not raw log retention, despite no demonstrated improved capacity. Full replacement can lose earlier content; no token ceiling or fidelity check is locally enforced in the read ranges. Reasons for compression/omission are not separately retained or read. Reset seed is exactly `Yet nothing`, consistent with the supplied runtime account. SRC-1, `pipeline_summary.py`; [MEM-OBJ-summary](#mem-obj-summary) gives the checked literal.

#### On [RT-RTE-smart-rag](runtime.md#rt-rte-smart-rag)

Selected parts are text/action, not importance rationale or dense vectors. Admission timing mixes old-plan embedding with new-plan importance; later old entries are not re-rated when priorities change. Top-n ranked entries are unioned/deduplicated with the recent-expression results. Since the recent expression begins at `i=0`, `observations[-0]` includes the oldest entry and the remaining negative indexes cover recent entries; it is not an exact last-n window. No global token budget or retention eviction is wired. SRC-1, `pipeline_smartrag.py`; the route supplies ranking passage and the metadata/object records distinguish stored numerical authority from delivered knowledge.

#### On [RT-RTE-hypergraph-update](runtime.md#rt-rte-hypergraph-update)

Event text is retained even when its thesis child links are removed. Semantic name selection re-embeds theses with top five/0.75/depth expansion. Event selection uses new thesis names' hash overlap and plan similarity, then ascending score order, excludes history/current observation, and takes the prefix top-k. This differs from game descending episode ranking. API returns texts but lacks a shipped later planner consumer; no actual read-back deployment is inferred. `clear(thesises,event)` normalizes input and cannot be treated as the QA zero-argument reset. Source-native `thesises` does not itself establish formulated explanatory theories or retained content-directed criticism. SRC-1, `graphs/hypergraph.py`, `utils/retriever_search_drafts.py`; distinct operative content/index records above refine the supplied combined route.

## Write side

### Acquisition and automatic transformation

Game observations are cleaned and augmented with step/task instructions before graph extraction; inventory is separately appended afterward. Maintainer-authored extraction instructions ask for short concrete facts, hypothesis wording and entity containment, but code only parses syntax and normalizes. Fragments without exactly three comma-separated fields or nonempty units are dropped. [MEM-OBJ-triplets](#mem-obj-triplets) therefore contains model-derived claims, not a certified semantic graph. QA paragraphs enter the same extraction machinery without replacement. Direct `add_triplets`/`delete_triplets` calls remain mutable library affordances; the inherited `delete_all` clears the list but is not a synchronized ContrieverGraph cache/episode reset. No shipped caller uses it: [MEM-ABS-state-readers](#mem-abs-state-readers). SRC-1, `utils/utils.py`, `graphs/contriever_graph.py`, `graphs/parent_graph.py`.

> def process_triplets(raw_triplets):
>     raw_triplets = raw_triplets.split(";")
>     triplets = []
>     for triplet in raw_triplets:
>         if len(triplet.split(",")) != 3:
>             continue
> --- `utils/utils.py`

### Curation, rejection and withdrawal

Game replacement first selects endpoint-associated old facts and filters strings containing direction and selected relation words. A model then applies the conservative same-aspect instructions. Code parses left-side triplets, removes matching unprotected entries and independently adds extracted new ones. It does not retain or validate the replacement mapping as a transaction. Hypothesis, truth and semantic redundancy gates remain requested behavior, not enforced guarantees. Model-returned stale-fact removal is computational admission, not human editing. SRC-1, `graphs/contriever_graph.py`, `utils/utils.py`, `prompts/prompts.py`; [RT-RTE-game-memory](runtime.md#rt-rte-game-memory) supplies removal and narrow guard witnesses.

> Generate only replacing, no descriptions are needed.
> Existing triplets: {ex_triplets}.
> New triplets: {new_triplets}.
> --- `prompts/prompts.py`

Withdrawal acts on live triples/fact vectors, not episode input text, stored episode extraction lists, prior plans or snapshots. Hypergraph removes thesis objects/incidence but preserves parent event text. Neither path has transactional rollback or a semantic-error recovery checkpoint. Reset/new attempt provides a different horizon, not repair of an erroneous revision. See [MEM-OBJ-obs-episodic](#mem-obj-obs-episodic), [MEM-OBJ-hypergraph-content](#mem-obj-hypergraph-content), [MEM-OBJ-episodic-snapshots](#mem-obj-episodic-snapshots).

### Trace-fed alternatives and evaluation

Full history retains raw observation/action pairs; summary transforms such traces plus earlier summary into later-consumed text; smart-RAG derives integer importance and embeddings which select retained traces. Main graph extraction similarly turns observation evidence into retained facts and episodes. These are automatic trace-fed writes with behavior-shaping later consumers. They establish retained experience influencing update/selection contexts, not beneficial learning, exercised self-improvement or a theory-builder classification. Explanation for replacement/compression/rating is not separately retained in their live stores; logs can retain returned text, but no shipped reason read-back route is shown. Plan strings can carry subgoal reasons to later models, a separate positive path rather than a general claim that reasons are absent. SRC-1, `pipeline_fullhist.py`, `pipeline_summary.py`, `pipeline_smartrag.py`, `pipeline_arigraph.py`; object records and runtime routes supply the respective witnesses.

QA reference-answer metrics and intended TextWorld replacement metrics terminate in diagnostics. They do not admit a corrected fact/prompt/model into later production. Source defects in the replacement evaluator and LazyGraph prevent treating that code as operational validation, as retained in [RT-RTE-graph-evaluation](runtime.md#rt-rte-graph-evaluation). The unused reflexion prompt cannot supply a missing trace-to-general-rule path: [RT-ABS-reflex-invocation](runtime.md#rt-abs-reflex-invocation). Provider-internal memory/weight updates remain opaque; local model adapters do not establish them or their absence.

## Read-back

The main graph and QA routes are explicit requests from shipped drivers, with automatic selectors inside the requested operation. They are not unsolicited pushes. Game delivery is selected old fact displays and episode input text → planner/action requests; QA delivery is selected fact displays and paragraph texts → answer request. Selection authority belongs to code and embeddings, while content's behavioral force at those models is interpretive information. Static authored prompts are guidance, not experiential read-back. [RT-BAP-memory-decisions](runtime.md#rt-bap-memory-decisions) describes the authority boundary; annotations above specify what survives selection.

Navigation/exploration read live triples through location/edge rules rather than model fact interpretation. The navigation consumer can expand one action into many environment commands. Intermediate hidden observations are logged but not separately admitted; only final feedback reaches the next outer update. Thus neither the graph nor bounded history is a complete raw environment-action trace: [RT-RTE-graph-navigation](runtime.md#rt-rte-graph-navigation), SRC-1, `pipeline_arigraph.py`, `graphs/parent_graph.py`.

Alternative drivers deliver entire history, replaced summary or selected smart-RAG text/action pairs to their own planner/action roles. They are separately invoked scripts, not automatic interchangeable backends. Current plans also reach later requests. All established horizons are within an attempt/task, not cross-session graph reuse. Library accessors, Hypergraph and ObservedGraph supply capabilities without established shipped downstream behavioral consumers; logs/snapshots supply retention without established replay. The readable facts/events are not explanations of their dense representations, and numerical access metadata is not itself delivered instruction.

## Integration issues

1. **Recent-episode exclusion qualification.** [RT-RTE-game-memory](runtime.md#rt-rte-game-memory) describes recent-observation exclusion. The filter is implemented, but [MEM-OBJ-history](#mem-obj-history) holds inventory-augmented strings while [MEM-OBJ-obs-episodic](#mem-obj-obs-episodic) keys were stored before that augmentation. The exact-string exclusion need not suppress recent episodes. Evidence and quote are in the route annotation; consequence: distinguish the selector's condition from successful recent-window removal.
2. **Stale episode delivery is separate from fact withdrawal.** [MEM-OBJ-triplets](#mem-obj-triplets) and [MEM-OBJ-obs-episodic](#mem-obj-obs-episodic) have different deletion horizons. Hypergraph has an analogous difference between removed theses and surviving events: [MEM-OBJ-hypergraph-content](#mem-obj-hypergraph-content). Consequence: do not promote game fact replacement to universal memory invalidation or truth at every consumer.
3. **No duplicate declarations identified.** New objects are retained parts omitted as standalone objects by runtime, with explicit containment for single-route parts and distinct-identity comparison for shared parts. [MEM-RTE-observed-update](#mem-rte-observed-update) is a separate auxiliary API rather than a duplicate main/evaluator route; [MEM-ABS-state-readers](#mem-abs-state-readers) concerns snapshot/cache/serialization callers rather than the supplied named-reflexion absence.
4. **Unresolved operative limits.** Exact provider retention/updates and upstream weight versions remain unresolved in [RT-CMP-gpt-agent](runtime.md#rt-cmp-gpt-agent), [RT-CMP-llama-agent](runtime.md#rt-cmp-llama-agent), [RT-CMP-retriever](runtime.md#rt-cmp-retriever). External deployment and later consumers of Hypergraph, ObservedGraph, snapshots and JSON payloads remain uninspected; generic auxiliary caller admission cannot be assigned a human/computational principal. Available methods are not deployed wiring. These limits prevent cross-session, global semantic-validity and external-caller authority conclusions.
5. **Effective budgets and benefit remain limited.** Per-query top-k/depth and episode counts are code-visible, but provider context truncation/compliance and causally attributable memory benefit are not. [RT-CLM-memory-performance](runtime.md#rt-clm-memory-performance) remains attributed reporting, not a demonstrated consequence of these individual stores or selectors.

## Limitations and checks

HEAD was rechecked as e884b76d7fa5185a3a8a55e5a67393b5a43f5ef2 and source `git status --short` was empty. Run identity, source identity and reviewed boundary match supplied inputs. Analysis followed the supplied memory job, member type, worker rules and record contract; no other analysis, worker launch, target execution or source mutation was used. Direct source searches and reads challenge universal replacement, restart persistence, cached-retrieval and recent-exclusion interpretations; the qualified findings above retain the positive implemented paths.

No fresh operation/experiment establishes truth, successful model uptake, live auxiliary deployment, improved future capacity or component-level causal benefit. Recorded operation remains scoped to runtime's supplied log samples. Exact token budgets, external provider state and generic auxiliary caller control remain unresolved rather than asserted absent.

Deterministic validation: the supplied `validate-output` command passed with “Member content check passes; invocation residue not checked.” This establishes structural and quotation checks, not job acceptance, claim support or deployment evidence.
