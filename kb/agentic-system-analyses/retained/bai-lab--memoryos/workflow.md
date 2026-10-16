---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "MemoryOS workflow account of a JSON-backed dialogue turn, its retrieval handoffs, synchronous memory admission and failure delivery."
run-id: AAS-2026-10-16-memoryos-bb72a1b70e03-01
reviewed-boundary: "587ed7755c7aed179965792830ff1b5ad9a6fa92"
---

# MemoryOS workflow report

## Workflow account

### Selection and evidence

The representative workflow is one call to the Python JSON implementation's `Memoryos.get_response`: retrieve context, request an answer, admit the exchange and return its text. It is selected because it joins the shipped response and maintenance paths without inventing an autonomous agent loop. The caller supplies the problem; Python controls all handoffs. The completion model contributes text, not a plan of executable tasks. The workflow ends at the library return, not at verified user satisfaction or an observed browser delivery. Its main route is [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response), with conditional continuations through [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission) and [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis).

Evidence is implementation in SRC-1 at the frozen revision. Direct inspection for this member covers `memoryos-pypi/memoryos.py` from the heat-triggered analysis method through the response method, all of `memoryos-pypi/retriever.py`, and `OpenAIClient` initialization and synchronous completion in `memoryos-pypi/utils.py`. The runtime member supplies the associated storage, migration and prompt evidence. This adds workflow-focused inspection within the registered source, not a new source. No target execution or supplied run trace establishes successful completion, personalization or durable recovery.

### Request, fan-out and join

1. **Caller to orchestrator.** An already constructed `Memoryos` receives the query, relationship setting and optional conversation metadata. Its configured identities and memory instances determine accessible state; these are not newly authenticated identities on each call. The caller invokes the operation, but does not approve each retrieved item or resulting write. Construction and reload are established in [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response), SRC-1: `memoryos-pypi/memoryos.py`.
2. **Orchestrator to retriever.** The orchestrator passes the query and user ID to `retrieve_context`. The retriever submits three fixed tasks: mid-term pages, user knowledge and assistant knowledge. Each has the query and its corresponding memory object. These are local worker threads, not independently prompted agents. They cannot decide to launch another task or deliver an alternative final answer. Page selection uses session/page thresholds and a capacity-seven heap; knowledge tasks use threshold/top-k arguments. Recent short-term dialogue and the full profile are obtained separately and bypass this query-ranking step. See [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response), SRC-1: `memoryos-pypi/retriever.py` and `memoryos-pypi/memoryos.py`.
3. **Retriever back to orchestrator.** Results are associated with their task indices and joined into three named lists. An exception from a task yields an empty list for that task, not rejection of the whole response request. Thus the join can proceed with incomplete recalled context. Successful retrieval also can change access/heat state; it is not an isolated, read-only worker stage ([RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response)).

The join's recovery owner is the retriever, and its recovery action is substitution rather than retry:

> results[task_idx] = future.result()
>                 except Exception as e:
>                     print(f"Error in retrieval task {task_idx}: {e}")
>                     results[task_idx] = []
> --- `memoryos-pypi/retriever.py`

### Context handoff and answer proposal

The orchestrator renders retrieved pages as historical dialogue with timestamps and chain metadata. It combines recent dialogue, recalled pages, user profile, user facts and the query into the user message. Retrieved assistant knowledge, the relationship setting and conversation metadata enter the system message. The provider therefore receives selected and formatted text, not unrestricted access to the persistent stores. No sub-agent frame is returned: Python builds one two-message request for the completion model. These handoffs and their different authority channels are established by [RT-BAP-user-context](runtime.md#rt-bap-user-context) and [RT-BAP-assistant-context](runtime.md#rt-bap-assistant-context), SRC-1: `memoryos-pypi/memoryos.py` and `memoryos-pypi/prompts.py`.

The orchestrator requests a completion with temperature 0.7 and a 1500-token cap. The wrapper extracts the first choice's text, strips it and cleans reasoning tags before returning it. There is no model-selected next-step dispatcher in this route. The shipped prompt requests English, a maximum of thirty words and temporal relevance, but the inspected response method has no acceptance test enforcing those requests. A token cap is not a thirty-word validator. Neither the caller's query nor a retrieved passage is an expected-answer oracle. See [RT-OBJ-generation-prompts](runtime.md#rt-obj-generation-prompts) and [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response), SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-pypi/utils.py`.

### Admission before delivery

The completion is not returned immediately to the caller. `get_response` first passes the original query and returned text to `add_memory`. If short-term storage is full, the updater migrates old dialogue before the new pair is appended. The migration uses continuity/summary model outputs and storage rules; it is not an answer-review stage. It may fall back on a general summary when parsing fails. The new exchange is then appended and saved, followed by the heat-triggered analysis check. This progression and its nontransactional limits are established in [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission), SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-pypi/updater.py`, `memoryos-pypi/utils.py`.

When the hottest session meets the heat threshold and contains unanalyzed pages, the orchestrator fans out two more fixed tasks. One receives the existing profile and dialogue and proposes a replacement profile; the other receives dialogue and proposes user/assistant knowledge. Python joins the tasks and decides admission. The profile must be nonempty, not `none` and at least thirty stripped characters. Knowledge is split into lines and empty/none-like lines are filtered. These are structural/content-length guards, not evidence checks against reality. The source prompt guides preservation of existing insights and grounded extraction; the persisted results are the proposed profile/facts and analysis metadata, not a verdict on answer correctness ([RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis), SRC-1: `memoryos-pypi/memoryos.py`, `memoryos-pypi/prompts.py`).

No human veto appears in this per-turn admission route. A skipped short profile does not cause regeneration or reject the already generated response. If both analysis futures return, processing proceeds to marking session pages analyzed and resetting heat contributors even when the profile guard skipped replacement. If a future raises, the method logs and returns before those admission/marking steps; it supplies no automatic retry. Writes later in the method can also fail after earlier changes. There is no transaction restoring the whole turn. These workflow consequences follow from SRC-1: `memoryos-pypi/memoryos.py` and [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis).

### Failure path and terminal result

The source-supported failure path is a completion-provider exception. The wrapper catches it and returns the ordinary string `Error: Could not get response from LLM.` The response method does not inspect a success flag or reject that sentinel: it admits the query/sentinel pair through the same `add_memory` call and then returns it. The verbatim exception and return passages are retained in [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response), SRC-1: `memoryos-pypi/utils.py` and `memoryos-pypi/memoryos.py`. Consequently the local workflow can deliver an error as answer text and make it eligible for subsequent recall. This is implemented control flow, not an observed failure incident.

The orchestrator owns the final delivery decision: reaching `return response_content` after synchronous admission constitutes library delivery. It does not certify complete retrieval, a successful provider request, prompt compliance or durable saves. Conversely, an uncaught prompt/admission exception can prevent delivery after provider generation; earlier retrieval or storage effects need not be undone. Save handlers' best-effort behavior and the nontransactional migration prevent interpreting an API return as a durable-commit certificate ([RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response), [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)).

This terminal boundary is route-specific. MCP retrieval hands memory data to an external host rather than generating and admitting its final answer; the evaluation driver writes benchmark answers and uses an offline scorer rather than the dialogue loop's admission path. Those are not missing stages to splice into this workflow ([RT-RTE-mcp-access](runtime.md#rt-rte-mcp-access), [RT-RTE-locomo-evaluation](runtime.md#rt-rte-locomo-evaluation)). No supplied execution evidence closes the gap from these wired handoffs to successful delivery or benefit.

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

#### On [RT-RTE-dialogue-response](runtime.md#rt-rte-dialogue-response)

Workflow role: representative request-to-return route. The retrieval join substitutes empty lists on worker failure; it is not a verification gate. Final completion text, including the provider-error sentinel, passes into synchronous admission before delivery. Delivery means API return, not acceptance by a truth/style oracle or durable-commit acknowledgement. Python owns progression and the caller owns invocation; the model owns only the text proposal within this handoff.

#### On [RT-RTE-memory-admission](runtime.md#rt-rte-memory-admission)

Workflow role: required post-generation continuation before the response return. Overflow migration and subsequent maintenance increase the work that can occur between proposal and delivery. Their failures can leave partial effects; neither the pre-append ordering nor the save attempts provide whole-turn rollback. This continuation is not independent verification of the proposed answer.

#### On [RT-RTE-profile-analysis](runtime.md#rt-rte-profile-analysis)

Workflow role: conditional synchronous branch of response admission. The orchestrator joins profile and knowledge proposals, applies structural guards, then marks pages analyzed and resets heat. Rejection of an insufficient profile does not reject the dialogue turn. A raised analysis future exits the branch without an automatic retry; this is distinct from a caught provider error returned as text. No per-item human approval or reference-answer adjudication governs this branch.
