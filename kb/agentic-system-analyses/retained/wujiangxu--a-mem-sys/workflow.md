---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "A-MEM workflow account tracing related-note ingestion, model-directed evolution and caller retrieval, including bounded rejection and recovery paths."
run-id: AAS-2026-10-16-a-mem-sys-eff95cd80440-01
reviewed-boundary: f303dfc71e07bdc787f4bc135d4cea328ae30e99
---

# A-MEM workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is **add related notes, evolve relationships, then retrieve note data**. It is selected because the shipped `test_memory_evolution` explicitly joins repeated `add_note` calls, ID reads and `search_agentic`; the README also demonstrates addition followed by retrieval. This is a memory-service workflow, not a complete task-solving agent workflow. A Python caller initiates each operation; the internal model makes bounded metadata and relationship decisions. No downstream answer-generation stage is established by this shipped sequence (SRC-1, `tests/test_memory_system.py`, `README.md`; [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval)).

> memory_ids = []
> for content in contents:
>     memory_id = self.memory_system.add_note(content)
>     memory_ids.append(memory_id)
> --- `tests/test_memory_system.py`

> results = self.memory_system.search_agentic("neural networks", k=3)
> self.assertGreater(len(results), 0)
> --- `tests/test_memory_system.py`

These are implementation and test-design witnesses, not observed execution. This member inspected the constructor, prompts, analysis, add, consolidation, neighbor formatting, evolution and agentic-search implementations in `agentic_memory/memory_system.py`; the complete `agentic_memory/retrievers.py`; README usage lines 87–163; and `test_memory_evolution` in `tests/test_memory_system.py`. All belong to registered SRC-1; no new source or observed-run layer is added. Model success, test passage and retrieval benefit remain unobserved.

### Request, handoffs and state changes

1. **Caller establishes the instance and submits content.** Construction selects an inference backend and embedding model, initializes the object map and attempts a Chroma reset. It is not a resume operation. The caller owns which experiences to submit and when to search; the service does not schedule those requests ([RT-RTE-note-admission](runtime.md#rt-rte-note-admission); SRC-1, `agentic_memory/memory_system.py`). The representative test submits three related neural-network strings rather than delegating a user task to an autonomous worker.

2. **Python delegates semantic analysis to the configured model.** For missing keywords/tags or default context, `analyze_content` supplies current content and static natural-language instructions requesting keywords, a contextual sentence and categorical tags. The adapter receives a JSON-schema request. Python parses the returned JSON and fills only missing/default fields. Complete caller metadata bypasses this handoff, not subsequent relationship processing. The model proposes field values; code admits them without a separate content reviewer or expected-answer oracle. Generic caller identity does not establish human authorship or approval ([RT-RTE-note-admission](runtime.md#rt-rte-note-admission); SRC-1, `agentic_memory/memory_system.py`).

3. **On later additions, Python selects retained context and delegates evolution.** The first note skips evolution because the object map is empty. For a populated map, `find_related_memories(note.content, k=5)` asks Chroma for neighbors and formats their IDs, timestamps, content, context, keywords and tags. The evolution model receives that text plus the new note's content, context and keywords. This is a separately assembled request, not transfer of a conversation or an independent worker's persistent context. Unselected notes stay outside this request and remain searchable. The model decides `should_evolve` and requested actions; Python retains next-step ownership ([RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution), [RT-BAP-neighbor-context](runtime.md#rt-bap-neighbor-context); SRC-1, `agentic_memory/memory_system.py`).

4. **Python applies bounded actions, then stores the new note.** `strengthen` extends the new note's links and replaces its tags. `update_neighbor` replaces selected existing neighbors' tags/context in the object map. It does not immediately write those neighbors to Chroma. The add continuation inserts the new note into the map, then sends its content and metadata to the retriever. The retriever incorporates nondefault context, keywords and tags into the embedding document and serializes metadata for Chroma. Thus model output crosses into retained state through fixed Python operations, not model-issued tools or executable code ([RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution), [RT-RTE-note-admission](runtime.md#rt-rte-note-admission); SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`).

5. **A positive evolution decision may trigger consolidation before the add returns.** The counter increments on positive decisions; a threshold multiple calls `consolidate_memories`. That routine constructs a get-or-create retriever and adds every mapped note. Despite the reset comment, it performs no explicit reset, delete or upsert. It therefore cannot be treated as demonstrated synchronization or recovery of already-indexed neighbors. The add returns the note ID only after its downstream storage and any triggered consolidation complete ([RT-RTE-note-admission](runtime.md#rt-rte-note-admission); SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`).

6. **The caller explicitly requests delivery.** In the selected workflow, `search_agentic` queries Chroma, converts metadata into result dictionaries, optionally appends linked live-map neighbors, and truncates to `k`. If direct hits fill that budget, appended neighbors are cut. Direct-hit fields come from the index metadata, so evolved live-map fields need not appear in this result. Delivery means return of this list to Python, not a verified answer, adoption of its contents by another model, or durable recovery in a later session ([RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval), [RT-BAP-caller-results](runtime.md#rt-bap-caller-results); SRC-1, `agentic_memory/memory_system.py`).

### Verification, rejection and recovery

**Local admission is structural and bounded, not an independent quality gate.** Requested JSON schemas and `json.loads` mediate both model handoffs. Evolution dispatch recognizes only `strengthen` and `update_neighbor`; unknown action strings have no branch. Neighbor writes skip IDs not in the map. However, suggested links are extended without an equivalent existence check. The prompt asks for one neighborhood entry per neighbor, while code tolerates shorter arrays rather than checking equality. It updates at most the smaller of the neighbor count and tag-array length, and changes context only where the context array has an entry (SRC-1, `agentic_memory/memory_system.py`; [RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution)).

> for i in range(min(len(memory_ids), len(new_tags_neighborhood))):
>     memory_id = memory_ids[i]
> --- `agentic_memory/memory_system.py`

> if i < len(new_context_neighborhood):
>     neighbor_memory.context = new_context_neighborhood[i]
> --- `agentic_memory/memory_system.py`

**Declining evolution does not reject ingestion.** An empty map, missing neighbor context, a negative model decision or a handled evolution exception returns control to `add_note`, which continues to store the note. A malformed response can therefore yield successful-looking ID delivery without successful relationship evolution. The handler has no retry or compensating rollback; if earlier actions mutated state before failure, returning `False` does not undo them (SRC-1, `agentic_memory/memory_system.py`; [RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution)).

> except (json.JSONDecodeError, KeyError, Exception) as e:
>     logger.error(f"Error in memory evolution: {str(e)}")
>     return False, note
> --- `agentic_memory/memory_system.py`

Analysis exceptions instead supply empty keywords/tags and `General`; adapter-specific empty responses can produce different degraded values. There is no structured degraded-result flag. Storage failures are not enclosed in a route-wide transaction: map insertion and earlier neighbor changes may survive failure to return an ID. The caller receives an exception where one escapes and must decide what to do; no automatic recovery owner beyond the bounded handlers is established ([RT-RTE-note-admission](runtime.md#rt-rte-note-admission); SRC-1, `agentic_memory/memory_system.py`, `agentic_memory/retrievers.py`).

Search failure has a different terminal form: empty results. That return does not distinguish a retrieval exception from a valid no-result path (SRC-1, `agentic_memory/memory_system.py`).

> except Exception as e:
>     logger.error(f"Error in search_agentic: {str(e)}")
>     return []
> --- `agentic_memory/memory_system.py`

The shipped test checks non-null metadata and nonempty search output, not relationship correctness, relevance against a reference answer, synchronization, rollback or cross-session restoration. Those assertions describe intended verification only; they were not executed here. Consequently the workflow is wired through to API return, but neither reliable end-to-end operation nor improved agent performance is established (SRC-1, `tests/test_memory_system.py`).

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

#### On [RT-RTE-note-admission](runtime.md#rt-rte-note-admission)

Workflow role: repeated ingestion is the caller-controlled entry stage. ID return is the stage's completion signal, not proof that evolution succeeded. A triggered consolidation lies before that return and can prevent it. No separate final reviewer accepts the combined workflow result.

#### On [RT-RTE-neighbor-evolution](runtime.md#rt-rte-neighbor-evolution)

Workflow role: this is an optional internal handoff during each later add, not a separately scheduled worker. A decline or handled failure rejoins the storage continuation rather than terminating ingestion. Partial action effects can survive a failure, so this join point is not rollback.

#### On [RT-RTE-memory-retrieval](runtime.md#rt-rte-memory-retrieval)

Workflow role: caller-requested retrieval is the outward delivery stage. An empty list is not a distinct failure diagnosis. Neither this return nor the shipped test's acceptance criteria establishes that an enclosing agent used the returned notes to complete a task.
