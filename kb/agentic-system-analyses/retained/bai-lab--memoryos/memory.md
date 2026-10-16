---
type: agentic-system-analyses/types/agentic-system-memory-report.md
description: "MemoryOS retained dialogue, derived profiles and knowledge, context selection and withdrawal across JSON, ChromaDB, MCP, Playground and evaluation."
run-id: AAS-2026-10-16-memoryos-bb72a1b70e03-01
source-identity: "https://github.com/BAI-LAB/MemoryOS"
reviewed-boundary: "587ed7755c7aed179965792830ff1b5ad9a6fa92"
---

# MemoryOS memory report

## Boundary and evidence

This member covers the whole-system memory boundary in [boundary](boundary.md#boundary-and-evidence): JSON library admission, overflow migration, heat analysis, retrieval and response; bundled MCP tools; Playground import, inspection and clear; ChromaDB collections and metadata; and the separate evaluation pipeline. All evidence is SRC-1 at the frozen commit. HEAD and clean Git status were rechecked. No target program, test, provider or example was executed. Implementation wiring does not establish activated personalization, improved capacity, successful deployment or durable crash recovery.

Direct reads added the Python updater, short-/mid-/long-term storage, retriever, profile-analysis and response-assembly bodies, utility transformation functions and all Python prompts; ChromaDB insertion/search, provider backup/vector operations, retriever and long-term operations; Playground state/personality display; and evaluation orchestration, migration, retrieval and mid-/long-term storage. Supplied runtime records support the wrappers and other orchestration facts explicitly cited below; they are not treated as independent run evidence.

| Entry point or operation | Source paths (SRC-1) | Coverage and limits |
|---|---|---|
| JSON add, reload and generation | `memoryos-pypi/short_term.py`, `memoryos-pypi/memoryos.py`, `memoryos-pypi/retriever.py` | Direct storage/assembly reads; [MEM-OBJ-short-term](#mem-obj-short-term); [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response). |
| Overflow, continuity, summary, merge and LFU | `memoryos-pypi/updater.py`, `memoryos-pypi/mid_term.py`, `memoryos-pypi/utils.py` | Direct reads; [MEM-OBJ-mid-term](#mem-obj-mid-term), [MEM-OBJ-memory-access](#mem-obj-memory-access). |
| Heat/forced extraction, profile replacement and knowledge append | `memoryos-pypi/memoryos.py`, `memoryos-pypi/long_term.py`, `memoryos-pypi/prompts.py` | Direct reads; [MEM-OBJ-user-profiles](#mem-obj-user-profiles), [MEM-OBJ-user-knowledge](#mem-obj-user-knowledge), [MEM-OBJ-assistant-knowledge](#mem-obj-assistant-knowledge); supplied force-method finding in [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis). |
| Alternative updater and direct storage writes | `memoryos-pypi/updater.py`, `memoryos-pypi/long_term.py` | Direct reads; [MEM-RTE-direct-update](#mem-rte-direct-update). Capability only: no shipped caller of that updater method established here. |
| MCP registered add/retrieve/profile tools | `memoryos-mcp/server_new.py`, `memoryos-mcp/memoryos/retriever.py` | Supplied [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access), including bundled comparison. Host selection of tools is afforded; host prompt consumption remains outside evidence. |
| Playground chat/import/force/clear, state and personality views | `memoryos-playground/memdemo/app.py`, `memoryos-playground/memoryos.py` | Direct display reads plus supplied [RT-RTE-playground-control](runtime.md#rt-rte-playground-control); [MEM-RTE-profile-display](#mem-rte-profile-display). Display is not profile approval or replacement. |
| ChromaDB admission, reload, selection, capacity/delete and close | `memoryos-chromadb/mid_term.py`, `memoryos-chromadb/storage_provider.py`, `memoryos-chromadb/retriever.py`, `memoryos-chromadb/long_term.py`, `memoryos-chromadb/memoryos.py` | Direct scoped reads plus supplied [RT-RTE-chroma-dialogue](runtime.md#rt-rte-chroma-dialogue); [MEM-OBJ-chroma-storage](#mem-obj-chroma-storage). New-session alias overwrite, backup-fed extraction/enrichment and merge-created backups directly rechecked; dependency duplicate-ID behavior and crash consistency uninspected. |
| Evaluation import, derivation, question answering and scoring | `eval/main_loco_parse.py`, `eval/dynamic_update.py`, `eval/mid_term_memory.py`, `eval/long_term_memory.py`, `eval/retrieval_and_answer.py`, `eval/evalution_loco.py` | Direct main/storage/retrieval reads plus supplied scorer account in [RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation); [MEM-OBJ-evaluation-memory](#mem-obj-evaluation-memory), [MEM-OBJ-loco-results](#mem-obj-loco-results). Dataset validity and full evaluation prompt internals uninspected. |
| Shipped drivers, packaging and fixed-call boundary | `memoryos-pypi/test.py`, `memoryos-chromadb/comprehensive_test.py`, `Dockerfile`, `memoryos-mcp/server_new.py` | Runtime account supplies Python demo, fixed-call dispatch and Docker findings; boundary includes remaining demonstration drivers. No additional CLI/hook memory consumer established by these supplied findings; demonstration assertions are not executed results. |

External provider weights, dependency internals, unavailable local embedding cache and enclosing MCP host remain excluded as in boundary. The paper and performance reproduction are not added to scope. Available but uninspected HTML, remaining demonstration code and evaluation utilities cannot support completeness or benchmark-effect conclusions.

## Core ideas

MemoryOS retains original exchange text as well as derived representations. Mid-term summaries gate which sessions can yield pages; they do not generally replace all original dialogue. ChromaDB new-session insertion preserves vector-page text subject to dependency success but overwrites its JSON page backup before reload; backup-fed extraction and chain enrichment therefore lack those original pages ([MEM-OBJ-chroma-storage](#mem-obj-chroma-storage)). Continuity metadata is another model-produced summary delivered alongside recalled text. Profile analysis then produces a separately retained interpretation, recursively informed by the previous profile. Knowledge extraction produces short statements with embedding-based read-back. These distinct products and consumers are recorded below, rather than equating a hierarchy label with a single memory form.

Context reconstruction is code-owned and query-triggered. The JSON response path injects all recent history and the full profile, ranks older pages and knowledge, and uses different message positions for user and assistant context. Capacity bounds items, not input tokens. Access also changes future maintenance: visits raise heat and LFU survival, and heat chooses pages for extraction. Thus selection metadata has consequences without itself being factual memory ([MEM-OBJ-memory-access](#mem-obj-memory-access); [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response)).

Admission does not authenticate dialogue truth. Imports and direct adds can supply assistant text that the response model did not produce; ordinary model failures can also become stored dialogue. Derived statements can subsequently condition a system message. That is a live authority channel, not verified instruction isolation, factual validation or observed benefit ([RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), [RT-RTE-playground-control](runtime.md#rt-rte-playground-control), [RT-BAP-assistant-context](runtime.md#rt-bap-assistant-context)).

## Shared records

### Components

none declared in this member

### Operative objects

#### MEM-OBJ-short-term
Label: Recent QA deque

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

This object is the retained-input part of that admission route, not another route declaration. Source-native identity: `ShortTermMemory.memory`. Natural-language user/assistant text sits in symbolic QA dictionaries with timestamps; substrate is a bounded process deque serialized as a JSON list. The caller supplies the exchange or the generated-response path supplies it. Initial file content has caller/filesystem provenance, not established human authorship. All entries are later formatted into response history without query ranking; oldest entries become migration input. Capacity truncation also applies on reload. Direct append can evict without migration. Save errors are caught and malformed JSON resets this store, so neither local return nor reconstruction certifies complete retained history (SRC-1: `memoryos-pypi/short_term.py`, `memoryos-pypi/memoryos.py`).

> self.memory = deque(data, maxlen=self.max_capacity)
> --- `memoryos-pypi/short_term.py`

#### MEM-OBJ-mid-term
Label: Sessions, original pages and derived summaries

Part of: [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Source-native identities: `MidTermMemory.sessions`, session `summary`/`summary_keywords`, page `user_input`/`agent_response`/`meta_info`. Substrate: JSON session dictionaries reloaded into process memory. Pages preserve original text and timestamps; summaries, keywords and chain overviews are model-derived natural language. IDs and links are symbolic navigation metadata. Numerical embeddings are separated in [MEM-OBJ-memory-access](#mem-obj-memory-access). These are retained outputs of the supplied admission route, not duplicates of its progression.

The updater uses dialogue to judge continuity, generates a new overview, propagates it through reachable stored links, then supplies the same pages to every theme. Session merging appends pages but leaves the established session summary/embedding unchanged. Thus a summary can remain an old selection gate for new pages; theme production does not establish a topic partition. Retrieval returns selected raw pages with their overviews, not summary-only compaction. The original text can support later analysis, but derived profiles/facts do not carry a durable page-ID provenance relation (SRC-1: `memoryos-pypi/updater.py`, `memoryos-pypi/mid_term.py`, `memoryos-pypi/memoryos.py`, `memoryos-pypi/long_term.py`).

> target_session["details"].append(processed_page)
>                 processed_new_pages.append(processed_page)
> --- `memoryos-pypi/mid_term.py`

> current_batch_pages = []
>         temp_last_page_in_batch = self.last_evicted_page_for_continuity # Carry over from previous batch if any
> --- `memoryos-pypi/updater.py`

The continuity pointer starts process-local; linked pages persist, but initialization does not reconstruct that pointer. LFU removes sessions rather than retiring their already extracted facts/profile implications. The JSON eviction body has placeholder link cleanup, so link existence does not certify resolvable original evidence (SRC-1: `memoryos-pypi/mid_term.py`).

#### MEM-OBJ-memory-access
Label: Embeddings and maintenance-control metadata

Source-native identities: `summary_embedding`, `page_embedding`, `knowledge_embedding`, `access_frequency`, `H_segment`, `analyzed`, and the derived `heap`. This spans admission, response and profile-analysis state rather than being part of exactly one supplied route; closest counterparts are [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response) and [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis). It is their retained selector/control material, not a replacement route.

Dense embeddings are distributed numerical representations generated by encoders; counters, flags and links are symbolic. JSON stores vectors, sessions, counts and flags; FAISS indices and the negative-heat heap are rebuilt in process. Encoder weights and their mutability are separately described by [RT-CMP-sentence-transformer](runtime.md#rt-cmp-sentence-transformer) and [RT-CMP-bgem3-flag-model](runtime.md#rt-cmp-bgem3-flag-model). Adding vectors is not training those weights. Imported vector provenance is not verified by load.

The actual consumers are fixed code: cosine/inner-product thresholds and ranking select pages/facts; access frequency selects LFU loss; heat selects one session for analysis; analyzed flags suppress repeat extraction. In JSON search, query keywords are empty and recency multiplication is commented out. Heat still uses recency, visits and interaction count. Calling this a recency-ranked JSON retriever would confuse those consumers (SRC-1: `memoryos-pypi/mid_term.py`, `memoryos-pypi/long_term.py`, `memoryos-pypi/retriever.py`).

> query_keywords = set()  # Keywords extraction removed, relying on semantic similarity
> --- `memoryos-pypi/mid_term.py`

> self.access_frequency[session_id] = session["access_count_lfu"]
>                     session["H_segment"] = compute_segment_heat(session)
>                     self.rebuild_heap() # Heat changed
> --- `memoryos-pypi/mid_term.py`

#### MEM-OBJ-user-profiles
Label: Integrated user profiles

Part of: [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis)

Source-native identity: `LongTermMemory.user_profiles[user_id]`, with `data` and `last_updated`. Substrate: user long-term JSON. Content is model-interpreted natural-language preferences and traits, optionally containing reasons, inside a symbolic identity/time envelope. Old profile plus timestamped dialogue produces a proposed complete replacement; the orchestrator applies its thirty-character/non-none guard and writes `merge=False`. Direct storage writes have a different guard surface ([MEM-RTE-direct-update](#mem-rte-direct-update)).

Later consumers are the next profile-analysis call and the entire user-background portion of response generation, without relevance filtering; MCP/Playground also expose it. The prompt requests reasoning and preservation of prior insights, not guaranteed preservation. The stored string may contain reasons, and later profile/generation consumers receive the string, but no structured evidence references or independent reasoning validator are added. A rejected proposal leaves the old profile in place while the route can still mark pages analyzed (SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-pypi/long_term.py`, `memoryos-pypi/prompts.py`).

> 5. Include brief reasoning for each dimension when possible
> 6. Maintain existing insights from the old profile while incorporating new observations
> --- `memoryos-pypi/prompts.py`

#### MEM-OBJ-user-knowledge
Label: Extracted user facts

Part of: [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis)

Source-native identity: `LongTermMemory.knowledge_base`. Substrate: bounded deque serialized in the user's long-term JSON. Natural-language statements come from model extraction of dialogue, split by lines, or direct caller writes. Symbolic entries retain `knowledge`, recording timestamp and a numerical embedding, not original page IDs. The embedding selects statements for a later user-background context; it is not a warrant for their truth. Empty/none-like strings are filtered; finite capacity removes the oldest statements, with no contradiction-driven withdrawal in the inspected append/search methods. Profile replacement does not replace this deque (SRC-1: `memoryos-pypi/long_term.py`, `memoryos-pypi/memoryos.py`, `memoryos-pypi/utils.py`).

> entry = {
>             "knowledge": knowledge_text,
>             "timestamp": get_timestamp(),
>             "knowledge_embedding": vec
>         }
> --- `memoryos-pypi/long_term.py`

#### MEM-OBJ-assistant-knowledge
Label: Extracted assistant statements

Part of: [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis)

Source-native identity: dedicated assistant `LongTermMemory.assistant_knowledge`. Same natural-language/symbolic/numerical envelope and deque/JSON substrate as user knowledge, but different identity scope and downstream authority. The profile-analysis route sends extracted assistant lines to the assistant store. Dialogue includes generated or imported assistant text, so provenance is mixed. The extraction prompt requests demonstrated actions/capabilities; it cannot establish that an utterance proved such a capability. Selected statements enter system-message role/trait conditioning via [RT-BAP-assistant-context](runtime.md#rt-bap-assistant-context). The store and this BAP have distinct identities: retained content versus its authority path. Assistant-ID scoping can span users when the same assistant ID is used; this is not user-exclusive factual memory (SRC-1: `memoryos-pypi/long_term.py`, `memoryos-pypi/memoryos.py`, `memoryos-pypi/prompts.py`; storage identity supplied by [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response)).

> 2. Assistant knowledge: explicit statements about what the assistant did, provided, or demonstrated
> --- `memoryos-pypi/prompts.py`

#### MEM-OBJ-chroma-storage
Label: ChromaDB collections and JSON backups

Part of: [RT-RTE-chroma-dialogue](runtime.md#rt-rte-chroma-dialogue)

Source-native identity: `ChromaStorageProvider` collections and `metadata`. This is the route's retained state, not a second ChromaDB route. Substrates differ: persistent vector collections hold embeddings plus string-converted metadata; separately saved JSON metadata holds short-term entries, profiles, session metadata, counts and heap state. Session `pages_backup` survives only when a producer leaves it in the shared dictionary; ordinary successful new-session insertion overwrites it before any file save or reload. Content is original/derived natural language, symbolic bookkeeping and dense numerical selection material; it is not an opaque vector-only memory. Provider-held dependency index details remain uninspected.

The provider constructs backup pages containing raw dialogue, timestamps, links, overviews and flags, without embeddings; its session backup omits `summary_embedding`. This construction is not the final retained state on the new-session path. `MidTermMemory.sessions` aliases the provider's actual `mid_term_sessions` dictionary. After the provider installs its backup and submits vectors, `add_session` replaces that same dictionary slot with `session_obj`, which has neither `pages_backup` nor `page_count`. Both first insertion and the no-suitable-session branch follow this path. `save` updates access/heap state only, and `close` serializes the overwritten dictionary rather than restoring pages (SRC-1: `memoryos-chromadb/mid_term.py`, `memoryos-chromadb/storage_provider.py`, `memoryos-chromadb/memoryos.py`; agrees with corrected [RT-RTE-chroma-dialogue](runtime.md#rt-rte-chroma-dialogue)).

> self.sessions: dict = self.storage.get_mid_term_sessions()
> --- `memoryos-chromadb/mid_term.py`

> def get_mid_term_sessions(self) -> dict:
>         return self.metadata.get("mid_term_sessions", {})
> --- `memoryos-chromadb/storage_provider.py`

> self.metadata["mid_term_sessions"][session_id] = session_backup
> --- `memoryos-chromadb/storage_provider.py`

> # Add to storage
>         self.storage.add_mid_term_session(session_obj, processed_details)
>         
>         # Update local data structures
>         self.sessions[session_id] = session_obj
> --- `memoryos-chromadb/mid_term.py`

Surviving vector-page metadata contains original user/assistant text and timestamps, not the backup's links, overviews or analyzed flags. Its search returns raw text and relevance. Heat analysis reads only backup pages, so a newly inserted session supplies no unanalyzed pages and skips profile/knowledge extraction even if hot or forced. Response generation can still recall vector text, but backup lookup supplies no chain overview for those pages. Thus raw dialogue persistence in vectors does not establish a raw-to-profile/fact trace-fed update for that session. Direct profile/knowledge writes remain separate capabilities. When backup dialogue is available, the long-term updater sees serialized old profile plus dialogue and admits truthy parsed/wrapped profile output. Facts use separate user/assistant collections and timestamp-based capacity deletion (SRC-1: `memoryos-chromadb/storage_provider.py`, `memoryos-chromadb/memoryos.py`, `memoryos-chromadb/long_term.py`).

> def get_pages_from_json_backup(self, session_id: str) -> List[dict]:
>         return self.metadata.get("mid_term_sessions", {}).get(session_id, {}).get("pages_backup", [])
> --- `memoryos-chromadb/storage_provider.py`

> full_page_info = self.storage_provider.get_page_full_info(page_id, session_id)
>                 if full_page_info:
>                     meta_info = full_page_info.get('meta_info', '')
> --- `memoryos-chromadb/memoryos.py`

> unanalyzed_pages = [
>                 page for page in self.mid_term_memory.storage.get_pages_from_json_backup(sid)
>                 if not page.get("analyzed")
>             ]
> --- `memoryos-chromadb/memoryos.py`

Merge retrieves only surviving backup pages, combines them with new pages and calls the provider without the final local-slot overwrite. It can therefore leave a backup for newly merged pages, including their dialogue, links, overviews and flags; it cannot recover initial pages already lost from the backup. These surviving pages can later supply heat analysis and prompt enrichment. The provider replaces the backup before collection `add`, not an inspected upsert contract. Existing backup pages lack embeddings and are filtered from vector addition; old vectors must remain independently usable. Dependency duplicate-ID behavior limits verified merge/reload equivalence and atomic withdrawal, but is not the cause of the deterministic new-session backup loss (SRC-1: `memoryos-chromadb/mid_term.py`, `memoryos-chromadb/storage_provider.py`).

> pages_with_embeddings = [p for p in pages if "page_embedding" in p and p["page_embedding"]]
> --- `memoryos-chromadb/storage_provider.py`

> self.mid_term_collection.add(embeddings=page_embeddings, metadatas=page_metadatas, ids=page_ids)
> --- `memoryos-chromadb/storage_provider.py`

#### MEM-OBJ-evaluation-memory
Label: Evaluation-specific retained memories

Part of: [RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation)

Source-native identities: evaluation `ShortTermMemory`, `MidTermMemory.sessions`, `LongTermMemory.user_profiles`, `knowledge_base`, `assistant_knowledge`. Substrate: sample-specific short/mid/long JSON files under `mem_tmp_loco_final`, loaded before import. Natural-language dialogue/profile/facts and symbolic IDs/links/counters coexist with numerical embeddings. This is the alternate route's memory state, distinct from product JSON stores.

The dataset processor maps speakers to QA sides and appends image captions to text; incomplete pairs can be popped without migration. Capacity one followed by immediate migration normally leaves no recent tail for questions. Summary input uses user text only, although retained pages contain both sides. Each theme again receives all pages. Evaluation profile derivation first analyzes pages, then merges old/new profiles through another model call; user facts append by line and assistant knowledge can append as one block. Long-term lists have no product knowledge-capacity deque bound. These differences prevent treating the benchmark driver as a run of the product algorithm (SRC-1: `eval/main_loco_parse.py`, `eval/dynamic_update.py`, `eval/long_term_memory.py`).

> self.knowledge_base = []
>         self.assistant_knowledge = []
> --- `eval/long_term_memory.py`

The query consumer selects top-five session candidates using embedding plus keyword overlap, recomputes page embeddings from user text, timestamp and assistant text, and retains the best ten pages in the driver-configured queue. Its apparent time-decay multiplier is fixed to one. Search updates visits/access/heat in memory but does not call save or rebuild the heap there. Later question generation gets full profile and all assistant knowledge, not just query-selected assistant facts. User facts are query-ranked. Question answers are not admitted as dialogue by the main question loop (SRC-1: `eval/mid_term_memory.py`, `eval/retrieval_and_answer.py`, `eval/main_loco_parse.py`).

> lambda_t=1
> --- `eval/mid_term_memory.py`

#### MEM-OBJ-loco-results
Label: Retained benchmark answers and references

Part of: [RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation)

Source-native identity: `results` serialized as `all_loco_results.json`. Substrate: rewritten JSON result file. Natural-language question, system answer and reference answer are stored in symbolic sample/speaker/category/evidence/timestamp envelopes. Generated prompt strings are returned by generation but not included in these saved records. Reference answers come from `answer` or `adversarial_answer`; supplied dataset validity is unverified. The later consumer is the offline token-set F1 scorer, not memory admission, profile revision or model replacement. These are evaluation traces, not demonstrated derived behavioral memory (SRC-1: `eval/main_loco_parse.py`; scorer evidence in [RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation)).

> "system_answer": system_answer,
>                 "original_answer": original_answer,
> --- `eval/main_loco_parse.py`

### Routes

#### MEM-RTE-direct-update
Label: Direct profile and knowledge updates

Distinct from the orchestrated [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis): source-native `Updater.update_long_term_from_analysis` accepts a caller-provided result dictionary; `LongTermMemory.update_user_profile` and add methods expose still lower-level writes. No shipped invocation of this alternative updater method was established by this inspection. This is storage/admission capability, not a proven later consumer route with a hypothetical caller. Owner is calling software; caller content authorship and human approval are unresolved (SRC-1: `memoryos-pypi/updater.py`, `memoryos-pypi/long_term.py`).

- Immediate return: no result payload; mutation and save attempts.
- Later read-back: the normal response and analysis consumers can read the modified stores; use of this particular entry is uninspected.
- Delegated visibility: updater gets the result dictionary; storage gets text. No extra model call in this updater method.
- Selection predicate: nonempty/non-none profile and line-filtered knowledge; direct profile setter lacks the orchestrator's thirty-character guard.
- Invalidation or expiry: updater replaces profile; direct setter can concatenate with merge enabled; knowledge capacities apply.
- Activation or effect: changes later eligible content when invoked; no demonstrated invocation or changed answer.
- Evidence limits: exposed methods establish capacity, not a deployed consumer or human-curated revision process.
- implementation conclusion status: afforded
- operation conclusion status: uninspected

Admission: caller proposes supplied profile/facts, code applies guards and writes; no per-item human veto or reference-answer oracle is implemented here. Operating mode is caller-invoked update rather than benchmark experiment. The updater's `long_term_memory` is normally the user store, so its assistant lines go there, unlike the main orchestrator's dedicated assistant store. Guidance must have been supplied upstream; this method imposes no analysis prompt and persists no proposal rationale beyond supplied text. Rejection is structural/empty filtering; rollback is not provided by these methods, and save exceptions can leave in-memory changes (SRC-1: `memoryos-pypi/updater.py`, `memoryos-pypi/long_term.py`).

> self.long_term_memory.add_assistant_knowledge(line.strip())
> --- `memoryos-pypi/updater.py`

#### MEM-RTE-profile-display
Label: Playground retained-profile inspection

Part of: [RT-RTE-playground-control](runtime.md#rt-rte-playground-control)

Endpoints: session-selected Flask instance → `/memory_state` or `/personality_analysis` → browser JSON display. Owner: Flask callbacks. This separately traces the container route's read-only inspection part, not another administrative admission route. Source: SRC-1, `memoryos-playground/memdemo/app.py`.

- Immediate return: raw state JSON, or parsed category/dimension/level JSON, or HTTP error.
- Later read-back: requests consume retained recent history, profile and knowledge; personality display reads the existing profile rather than running fresh analysis.
- Delegated visibility: browser receives raw memories or a lossy trait display; display does not establish browser approval or model consumption.
- Selection predicate: session lookup; state view takes first five session entries then sorts that subset by heat; personality view applies regex, category substring matches and High/Medium/Low line scans.
- Invalidation or expiry: inapplicable — these callbacks do not persist a new display artifact or change source profile; subsequent writes/clear change later responses.
- Activation or effect: code formats inspectable state; no observed browser behavior or subsequent operator revision.
- Evidence limits: category/level output omits profile reasoning/context and need not cover all original traits; it is not the authoritative retained profile.
- implementation conclusion status: wired
- operation conclusion status: uninspected

> personality_analysis = parse_personality_traits(user_profile)
> --- `memoryos-playground/memdemo/app.py`

### Claims

none declared in this member

### Evidenced absences

none declared in this member

### Behavioral-authority paths

none declared in this member

## Annotations

#### On [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Write-side lineage is original exchange → retained page plus overview/summary → later response recall or heat analysis. This is not wholesale replacement of raw traces by summaries. Admission is software/model controlled; caller authorship is unresolved. Each theme receives the complete batch, including fallback insertion when no summaries parse; continuity is model judgment with an exact `true` check. Popping saves the shortened short-term file before the downstream transformation succeeds. Therefore failed migration can lose retrievable input, and a general fallback is recovery of topic organization, not transactional recovery of the popped pair (SRC-1: `memoryos-pypi/updater.py`, `memoryos-pypi/utils.py`, `memoryos-pypi/short_term.py`).

#### On [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis)

Trace-fed derivation has durable behavior-shaping products: integrated profile, user statements and assistant statements. Reasons are requested for profile dimensions but not persisted as independent extraction decisions or criticism records. Old profile is an update input; future generation reads the complete stored profile. Extracted facts retain recording time rather than an enforced original-page link. On the normal path, skipped profile/empty knowledge still lead to analyzed flags and heat reset after tasks return. Thus the analyzed marker means processing, not successful validated knowledge acquisition (SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-pypi/prompts.py`, `memoryos-pypi/long_term.py`).

#### On [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response)

Read-back is request-driven: current query → fixed semantic selectors → selected historical pages and knowledge → formatted model messages. Recent deque and profile bypass ranking. Default retrieval bounds are seven pages, five candidate sessions and twenty entries per knowledge category, not a total token budget. Heat can increase during retrieval before the generated exchange triggers maintenance. There is no isolated model-agent frame here: threads receive fixed retrieval work, not delegated conversational histories. Old context remains externally reachable, but it is copied by value into the next prompt rather than linked by followable model-window pointers (SRC-1: `memoryos-pypi/retriever.py`, `memoryos-pypi/mid_term.py`, `memoryos-pypi/memoryos.py`).

#### On [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access)

MCP supplies an alternative requested read-back channel: host query selects lists, but full recent history/profile and optional complete knowledge access bypass that list budget. This is not independent unsolicited memory injection. The actual authority at the final model is uninspected because the server returns data, not final host messages. Successful retrieval alone does not ensure subsequent host dialogue is retained; the host must call add. These findings rely on the supplied server/retriever evidence in this record, not an observed MCP session (SRC-1: `memoryos-mcp/server_new.py`).

#### On [RT-RTE-chroma-dialogue](runtime.md#rt-rte-chroma-dialogue)

Separate metadata and vector persistence mean withdrawal must reach both stores. Session deletion removes backup/access entries before attempting vector deletion, which catches exceptions; an inconsistent residue is possible, although session query filters also require backup presence. Knowledge-capacity deletion acts on vector IDs. Profile and short-term durability follow close/exit metadata save, not collection persistence alone. Session keyword extraction distinguishes selection from the JSON variant. Backup enrichment is attempted, not ensured: successful new-session insertion overwrites backup pages through the aliased dictionary, blocking both chain enrichment and heat-fed extraction for those pages before any reload. A later merge can retain a backup of newly merged pages but does not recover original backup contents. Vector-selected original text remains independently available subject to dependency success; repeated-ID merge behavior is a separate dependency question ([MEM-OBJ-chroma-storage](#mem-obj-chroma-storage); SRC-1: `memoryos-chromadb/storage_provider.py`, `memoryos-chromadb/mid_term.py`).

#### On [RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation)

Memory-fed answer generation is wired, but scorer output does not flow back into admission. All assistant statements are delivered to the benchmark system prompt, whereas user knowledge is query-ranked. Existing sample files are reloaded before new import; no clean-start reset is performed by this driver. Evaluation mid-term search changes access statistics in process but, unlike product JSON search, returns without saving/rebuilding its heap at that point. Persistence or maintenance effects of later retrieval visits must not be imported from the product path (SRC-1: `eval/main_loco_parse.py`, `eval/mid_term_memory.py`, `eval/retrieval_and_answer.py`; scorer passage supplied in this record).

## Write side

**Acquisition and admission.** Direct add, generated responses, MCP add and Playground import are different origins, not different factuality approvals. Top-level product add has no content-quality veto; migration drops incomplete popped pairs, while MCP/import perform nonempty-side checks before add. Initiating a workflow does not establish human approval of extracted content. Low-level stores and the alternative updater can write without the normal heat or profile-length gates ([RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access), [RT-RTE-playground-control](runtime.md#rt-rte-playground-control), [MEM-RTE-direct-update](#mem-rte-direct-update)).

**Automatic transformation.** JSON overflow changes storage and adds summaries/continuity without generally deleting migrated raw dialogue. ChromaDB overflow can retain original text in vector metadata while losing the corresponding JSON backup at new-session insertion. Its heat extractor then has no pages to transform, and response enrichment has no chain overview to deliver. Later merge-created backups can feed those consumers for newly merged pages, not recover the lost initial backup ([MEM-OBJ-chroma-storage](#mem-obj-chroma-storage), [RT-RTE-chroma-dialogue](runtime.md#rt-rte-chroma-dialogue)). Heat-selected unanalyzed pages supply profile/fact extraction; the existing profile supplies retained interpretation to the next update. Code admits model proposals under string/parse/length checks, not reference-answer assessment. Requested profile reasons may survive in the profile text and be read again; no durable record proves why each individual fact was accepted. This is trace-fed retained-content change, not evidence of improved capacity or weight learning ([MEM-OBJ-mid-term](#mem-obj-mid-term), [MEM-OBJ-user-profiles](#mem-obj-user-profiles), [MEM-OBJ-user-knowledge](#mem-obj-user-knowledge), [MEM-OBJ-assistant-knowledge](#mem-obj-assistant-knowledge)).

**Maintenance and withdrawal.** Capacity loss, session LFU, profile replacement and explicit Playground clear differ from semantic retraction. LFU page loss does not automatically retract already extracted profile/facts. Clearing both user and assistant directories is destructive rather than versioned rollback, and can affect any other caller using the same stored assistant identity; cross-instance synchronization is unestablished. JSON saves and ChromaDB metadata/vector writes are not one transaction. The analyzed flag can suppress further extraction even when an individual proposal was skipped, and force selects one hottest session rather than guaranteeing every eligible page is processed ([MEM-OBJ-memory-access](#mem-obj-memory-access), [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis), [RT-RTE-playground-control](runtime.md#rt-rte-playground-control), [RT-RTE-chroma-dialogue](runtime.md#rt-rte-chroma-dialogue)).

**Evaluation.** Imported dataset conversation, derived sample memory, generated answer records and scorer results are distinct. No source-grounded feedback route from F1 into memory rejection, method revision or successor selection is established by the driver/scorer. Dataset reference answers serve the offline evaluator rather than product admission ([MEM-OBJ-evaluation-memory](#mem-obj-evaluation-memory), [MEM-OBJ-loco-results](#mem-obj-loco-results), [RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation)).

## Read-back

Product JSON/ChromaDB response calls automatically reconstruct context only after the foreground request. The selector's inputs are query, embeddings and variant-specific thresholds/keywords; selected raw pages and statements are delivered alongside unranked recent history/profile. JSON overviews accompany recalled pages; ChromaDB attempts overview enrichment only from surviving backups. Ordinary new-session overwrite prevents that enrichment for initial pages even when vector text is recalled, while later merged pages can have surviving backup overviews ([MEM-OBJ-chroma-storage](#mem-obj-chroma-storage)). Storage persists across calls and reloads subject to the variant's save horizon. No unsolicited context push is established: automatic delivery is a stage of a requested generation route. Externalized state resembles a retrievable heap only in the limited sense of material kept out of the current window and later copied back; count bounds do not express model-window liveness or a token bound ([RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response), [RT-RTE-chroma-dialogue](runtime.md#rt-rte-chroma-dialogue), [MEM-OBJ-memory-access](#mem-obj-memory-access)).

The response model sees user profile/facts/history as user-message context, but assistant facts as system-message trait/knowledge context. These are natural-language influences, not executable instructions with locally enforced compliance. Profile reasons, if present, are delivered with the profile; JSON page overviews accompany original recalled text. Neither exposure establishes that the model used reasons or changed behavior ([RT-BAP-user-context](runtime.md#rt-bap-user-context), [RT-BAP-assistant-context](runtime.md#rt-bap-assistant-context), [MEM-OBJ-user-profiles](#mem-obj-user-profiles)).

MCP returns retained data to a host with unresolved downstream channel and actual activation. Playground returns raw state or a lossy trait rendering to the browser. Evaluation question generation reads sample memory with separate selection/all-assistant rules; the scorer later reads saved answers/references. Direct storage getter availability alone adds no unnamed deployed consumer ([RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access), [MEM-RTE-profile-display](#mem-rte-profile-display), [MEM-OBJ-evaluation-memory](#mem-obj-evaluation-memory), [MEM-OBJ-loco-results](#mem-obj-loco-results), [MEM-RTE-direct-update](#mem-rte-direct-update)).

## Integration issues

1. **No correction to the supplied runtime is needed; the previous memory backup finding is corrected below.** The following refinements must remain scoped: product JSON query keywords/recency differ from maintenance heat; evaluation returns after access mutation without the product save/rebuild behavior. SRC-1 `memoryos-pypi/mid_term.py` and `eval/mid_term_memory.py` support the distinction. Do not generalize product persistence claims in [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response) to [RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation); see [MEM-OBJ-memory-access](#mem-obj-memory-access), [MEM-OBJ-evaluation-memory](#mem-obj-evaluation-memory).
2. **ChromaDB retained-state correction and separate dependency limit.** [MEM-OBJ-chroma-storage](#mem-obj-chroma-storage) corrects this member's previous positive backup finding: SRC-1 `memoryos-chromadb/mid_term.py` aliases provider sessions and overwrites the backup after new-session insertion. `memoryos-chromadb/storage_provider.py` and `memoryos-chromadb/memoryos.py` show that initial pages then cannot feed heat analysis or chain enrichment, regardless of metadata-save success. Vector text can still feed response generation. Later merge-created backups can retain newly merged pages but do not reconstruct the lost initial pages. This now agrees with the supplied corrected [RT-RTE-chroma-dialogue](runtime.md#rt-rte-chroma-dialogue); neither record is a duplicate of the other (retained object versus route). Stable-ID collection `add` behavior remains uninspected and prevents verified merge idempotence/reload equivalence, but does not qualify the source-established overwrite or justify an intact-backup lineage claim. No target execution was authorized.
3. **Alternative admission scope is not a duplicate.** [MEM-RTE-direct-update](#mem-rte-direct-update) has no established shipped caller and writes assistant lines to its bound user long-term object. It must not inherit the invocation/assistant-store conclusions of [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis). SRC-1 `memoryos-pypi/updater.py` supports this capability and its distinct guards; hypothetical invocation does not establish later consumption of those particular writes.
4. **Display inspection is a contained route, not another analysis writer.** [MEM-RTE-profile-display](#mem-rte-profile-display) is part of [RT-RTE-playground-control](runtime.md#rt-rte-playground-control). SRC-1 `memoryos-playground/memdemo/app.py` shows regex/substrings, not a fresh model call or retained profile revision. Do not infer profile reasoning coverage from the browser's category/level payload.
5. **Unresolved provenance and operation limits remain local.** Loaded JSON/vector origins, actual end-user/human approval, provider responses, MCP host use, complete profile reason preservation and cross-instance clear effects are not observed. These prevent authenticated lineage, exercised revision/activation and durability conclusions, not the implemented transformation account. Records concerned: [MEM-OBJ-short-term](#mem-obj-short-term), [MEM-OBJ-user-profiles](#mem-obj-user-profiles), [MEM-OBJ-chroma-storage](#mem-obj-chroma-storage), [RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access), [RT-RTE-playground-control](runtime.md#rt-rte-playground-control).

All new declarations were compared with supplied runtime records. Object declarations identify retained parts or distinct cross-route selector state; route declarations identify a contained display operation or distinct alternative admission capability. No candidate replacement/possible duplicate remains undeclared here; annotations retain existing referents rather than redeclaring them. Future peer overlap cannot be checked without those members and must be reconciled then.

## Limitations and checks

The source identity and HEAD matched the frozen revision and the source checkout was clean. Scope and method were rechecked against the supplied boundary, runtime, memory type, worker rules and records contract. This is source analysis, not observation or an experiment. Remaining available-but-uninspected surfaces and excluded dependencies are named in the coverage table; they prevent exhaustive deployment/driver and quality claims, not the bounded positive findings above. Model instruction compliance, activation of reasons and personalization benefit remain unobserved.

Validation: the invocation-specific deterministic validator passed. This establishes structural and quotation checks, not analytical correctness or acceptance.
