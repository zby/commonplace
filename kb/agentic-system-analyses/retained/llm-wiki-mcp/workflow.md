---
type: agentic-system-analyses/types/agentic-system-workflow-report.md
description: "LLM-WIKI-MCP workflow account: interactive agentic ask from question through evidence selection, synthesis recovery, recording and visible delivery."
run-id: AAS-2026-10-15-llm-wiki-mcp-5dff0dd0576a-01
reviewed-boundary: "25efb7631082fa3732723fee08e24d39b43311fa"
---

# LLM-WIKI-MCP workflow report

## Workflow account

### Selection and evidence boundary

The representative workflow is an interactive `/ask` of a subject question with the configured mode set to `agentic`. It is selected because the shipped caller connects retrieval, prompt construction, a model request, blank-answer recovery, retained conversation recording and visible delivery. It is a multi-step, code-coordinated workflow, not a team of delegated agents. Its existing referent is [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask); workflow-specific findings annotate that record rather than declaring it again.

The frozen source and exclusions are those in [boundary](boundary.md#boundary-and-evidence). This account uses SRC-1 implementation, not an observed execution. No target code, tests, examples or services were run. Inspection checked the final ask/dispatcher definitions in `src/llm_wiki_mcp/context_api.py`, their second-pass helpers and fallback router, and the interactive ask branch in `src/llm_wiki_mcp/cli.py`. This adds focused implementation coverage of the second-pass handoff and visible-delivery condition within the already registered source. It establishes wiring, not successful answering, persistence or user receipt in a deployment.

### Request and local evidence handoffs

The user supplies the question and the shell supplies the resolved vault, configured mode, a tool-call setting of 14 and `dry_run=False`. An empty question is rejected locally with usage text. For a nonempty question the shell calls the unified dispatcher. The dispatcher selects plain mode only when requested; otherwise it calls the final agentic helper. One-shot CLI `ask` is a different workflow and must not inherit this account's history or prompt guarantees: see [RT-RTE-store-ask](runtime.md#rt-rte-store-ask). SRC-1: `src/llm_wiki_mcp/cli.py`, `src/llm_wiki_mcp/context_api.py`.

Within agentic ask, code resolves intent, repairs query text and initializes per-call state, trace and evidence. For ordinary subject questions it starts with page/note search, capabilities and ask history, then admits additional planner entries. Each selected helper receives the vault, repaired question, arguments and local state. Its result becomes evidence; trace entries record tool names and result types, not a transcript of a model choosing actions. Search can set a focus page; selected search titles lead to fuller page reads. Code, not a model or a human reviewer, decides these transitions. These mechanics and their minimum source passages are supplied by [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask). SRC-1: `src/llm_wiki_mcp/context_api.py`.

Evidence collection is not equivalent to provider visibility. The first context-pack builder selects recognized evidence types, incorporates selected recent question/answer history, caps source material and trims the whole prompt. Some collected results do not reach the prompt in full. The model receives copied text, not a worker frame with independent access to the vault. The operative object and context controls are [RT-OBJ-context-pack](runtime.md#rt-obj-context-pack) and [RT-CLM-context-budget](runtime.md#rt-clm-context-budget). Their budget is an estimated-text bound for the first agentic pack, not proof that all supporting sources fit the provider window. SRC-1: `src/llm_wiki_mcp/context_api.py`.

### Synthesis, verification and recovery

For the selected subject-question path, the local helper submits the assembled prompt to the configured model adapter. The endpoint receives shipped guidance and selected evidence and returns answer text; it is not delegated planning, permission checking or subsequent tool execution. Model identity and endpoint mutability remain those of [RT-CMP-ollama-model](runtime.md#rt-cmp-ollama-model). The prompt's force is described by [RT-BAP-answer-guidance](runtime.md#rt-bap-answer-guidance). SRC-1: `src/llm_wiki_mcp/context_api.py`.

The consequential check is whether normalized answer text is empty. A nonempty answer proceeds without a factual verifier, reference answer or citation-validation gate in this inspected path. This is an availability check, not an answer-quality acceptance test. A blank answer triggers a second synthesis helper, which selects up to six titles from first-pass search evidence, requests page reads and candidate links, and searches again with the original question. Local exceptions in these extra reads become error evidence or are suppressed; they do not constitute review decisions. SRC-1: `src/llm_wiki_mcp/context_api.py`; see the recovery annotation below.

The second prompt contains the original question, a truncated first trace, individually truncated first-pass evidence and expanded evidence. It is built separately rather than passed through the first pack's total-budget routine. The helper normalizes the second answer and can itself invoke deterministic fallback. Therefore an answer returned by the second helper is not necessarily a model-produced synthesis. If no answer returns to the main helper, that helper invokes fallback again. Fallback can extract from evidence or ultimately return generic system-description text; nonemptiness does not establish that the subject question was answered. SRC-1: `src/llm_wiki_mcp/context_api.py`.

No human is asked to accept each candidate answer. The user initiates the open request; code owns retry and fallback; the model supplies proposed prose. Operational self-questions are a separate branch that bypasses synthesis, and dry run returns evidence and the first prompt without an answer or turn recording. These are bounded alternatives, not missing stages in the selected subject-question workflow. [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask).

### Retention and delivery

After answer sanitization, code attempts to record the original question, first prompt, final answer, tool names and metadata. A recording exception becomes metrics error data and does not suppress the returned answer. This is automatic retention, not per-turn human approval. Retained question/answer records can feed a later agentic context pack, but that later delivery is not demonstrated model reliance or improved capacity. The recorder's admission and later-read path are already established in [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask). SRC-1: `src/llm_wiki_mcp/context_api.py`.

The API returns an answer dictionary. The interactive caller treats a truthy `answer` as printable delivery and then invokes its visible-turn recording helper; it does not gate display on the result's `ok` field. Thus provider failure status, fallback delivery and recording success are separate outcomes. The shell returns to user input rather than scheduling another autonomous task. SRC-1: `src/llm_wiki_mcp/cli.py`.

The returned `llm_prompt` and recorded prompt remain the first prompt even if the second helper produced the answer. Extra evidence and nested second-pass model metadata are returned, but the first prompt alone cannot reconstruct the second request. Neither a nonempty displayed answer nor the exposed first context pack establishes correct synthesis, complete provenance of the final answer, or durable recording. [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask), [RT-CLM-context-budget](runtime.md#rt-clm-context-budget).

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

#### On [RT-RTE-agentic-ask](runtime.md#rt-rte-agentic-ask)

Workflow handoff and delivery condition: the interactive caller delegates orchestration to the unified helper with a question and configured mode. It displays an answer on truthiness, independently of provider status. SRC-1 implementation: `src/llm_wiki_mcp/cli.py`.

> mode = release_current_ask_mode(str(vault))
> payload = release_ask(str(vault), question_text, mode=mode, max_tool_calls=14, dry_run=False)
> --- `src/llm_wiki_mcp/cli.py`

> if payload.get("answer"):
>     print("Answer:")
>     screen_print(payload["answer"])
>     _record_visible_cli_ask_turn(vault, question_text, payload, session_ask_turns)
> --- `src/llm_wiki_mcp/cli.py`

Recovery owner and acceptance limit: code supplies expanded evidence and a second prompt to the same adapter role, then tests normalized answer availability. There is no semantic comparison with an expected answer in this helper. Its fallback may supply the returned answer even when generation is blank. SRC-1 implementation: `src/llm_wiki_mcp/context_api.py`.

> extra=release_collect_second_pass_evidence(vault_path, question, evidence, limit=6)
> prompt=release_build_second_pass_prompt(vault_path, question, trace, evidence, extra)
> llm=release_ollama_generate(vault_path,prompt) if "release_ollama_generate" in globals() else {"ok":False,"error":"missing ollama","answer":""}
> answer=release_normalise_answer_text((llm.get("answer") or "").strip()) if "release_normalise_answer_text" in globals() else (llm.get("answer") or "").strip()
> if not answer:
>     answer=release_fallback_answer_router(question, trace, (evidence or [])+extra, llm.get("error") or "empty LLM response after second pass")
> return {"answer":answer,"llm":llm,"extra_evidence":extra,"prompt":prompt}
> --- `src/llm_wiki_mcp/context_api.py`

Fallback's terminal generic text is a delivery backstop, not evidence that the requested subject was resolved. SRC-1 implementation: `src/llm_wiki_mcp/context_api.py`.

> return release_sanitize_public_text(
>     "I can answer, but the LLM did not return a final synthesis. Based on the available runtime evidence, this is an LLM Wiki MCP: a local Markdown wiki system with search, page reads, Ollama-backed asking, MCP tools, provenance-aware ingest, notes, graphs and maintenance commands."
> )
> --- `src/llm_wiki_mcp/context_api.py`

Recovery visibility limit: the main helper incorporates the second result's answer, nested model result and extra evidence, but does not replace its first `prompt`. This agrees with the supplied route's provenance limitation. SRC-1: `src/llm_wiki_mcp/context_api.py`; minimum passage is already retained in the cited runtime record.
