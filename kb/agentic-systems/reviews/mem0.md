---
{
  "type": "types/note.md",
  "description": "Mem0 at its additive Python source revision: extraction, host recall, mutable deployment boundaries and limits of memory-based learning claims.",
  "generated-by": "analyse-agentic-system",
  "analysis-run": "AAS-2026-09-27-mem0-03",
  "source-identity": "https://github.com/mem0ai/mem0",
  "reviewed-revision": "94c3fe9f238f3dbf29c9ce98643bd71eb13077cd",
  "analysis-result": "kb/reports/retained/agentic-system-analysis/AAS-2026-09-27-mem0-03/result.md",
  "analysis-result-sha256": "c018cb9aad519e006e5ccb4ed7e9f457372bed5dc0c1e993046668982b7aaefa"
}
---

# Mem0: additive memory and host context supply

Evidence basis: source code and shipped documentation at `94c3fe9f238f3dbf29c9ce98643bd71eb13077cd`, inspected on 2026-09-27; no live operation or causal experiment.

Mem0 supplies memory acquisition, persistence and retrieval to applications and agent hosts. The caller or host still owns task planning, tool execution and final answers. This account covers the Python OSS library, self-hosted service and representative shared plugin implementation. Hosted internals, TypeScript and other host-specific alternatives remain opaque or partly uninspected. The [exact result](../../reports/retained/agentic-system-analysis/AAS-2026-09-27-mem0-03/result.md) retains the source register, canonical routes, generated quotations and complete comparison fields.

## How retained material reaches later work

The normal Python write path is additive at this revision. It retrieves ten recent scoped messages and ten relevant stored facts, supplies them alongside new messages to an extraction LLM, and stores generated texts under new UUIDs. Existing memory helps deduplication and context; explicit update and delete are separate caller operations. The implementation therefore does not support reading the older add docstring as an automatic ADD/UPDATE/DELETE loop. Provider failure raises an error, while parse failure can become empty extraction with messages still saved. Vector insertion, history and entity maintenance have separate failure paths. See exact-result RTE-5, RTE-6 and CLM-3; [Python memory implementation](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/mem0/memory/main.py).

Facts live with embeddings and scope metadata. A separate vector collection records entities and linked memory IDs that affect later ranking. SQLite retains a rolling raw-message window and mutation history. That entity collection supports a bounded access-metadata deduplication finding, not a dedicated graph-memory characterization of the inspected Python engine. Explicit updates revise text; deletion withdraws current entries while history remains. The ten-message window forgets older raw context without defining the lifetime of derived facts. See OBJ-3, OBJ-4, OBJ-5 and ABS-1 in the exact result.

The shared plugin stages host events locally, then submits selected conversations and tool evidence for hosted extraction. It persists pending jobs and polls completion before treating extraction as finished. On a qualifying first prompt it selects repository/personal memory and emits bounded hook context automatically. An MCP tool provides a separate route for the coding agent to request earlier-work recall. These support push and pull respectively; a response to an explicit query is not counted again as push. Hosted matching and extraction internals remain uninspected. See RTE-8, RTE-9 and RTE-10; [shared hook](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/integrations/agent-plugin-core/python/hook_runner.py) and [MCP tool](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/integrations/agent-plugin-core/python/mcp_server.py).

Automatic reuse also happens inside OSS extraction: retained facts and raw history enter a later extraction call without the LLM requesting them individually. This is the strongest wired trace-learning witness in the comparison profile. Procedural mode additionally generates and stores a summary for task continuation, but no dedicated continuation assembler was established. Subagent helpers can copy cached context; cached text may be longer than what the main hook actually delivered after truncation. The separately inspected proxy passes arguments incompatible with the current API and is not counted as functioning recall. See RTE-5, RTE-11 and RTE-12.

## Control and deployment boundaries

The self-hosted service authenticates requests and reserves configuration, reset, bulk deletion and unrestricted listing for admin paths. These controls do not by themselves establish tenant ownership: read-by-ID dispatches the requested ID after authentication, and callers provide memory identity filters. Direct library use bypasses HTTP guards; AUTH_DISABLED permits a configured bypass. Deployed grants and isolation were not inspected. See RTE-1 and BAP-2; [server endpoints](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/server/main.py) and [authentication](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/server/auth.py).

Configuration replacement is not atomic across the current dictionary, new Memory instance and persisted overrides. The dictionary changes before construction, and persistence errors are logged. The instruction-generation endpoint returns proposed priorities and a test sentence without installing or testing them. Library provider registration permits in-process extensions; the server's bundled-provider allowlist narrows only its own path. The supplied Compose command installs unversioned `mem0ai`, so a deployment may execute different library bytes from this source pin. See RTE-2, RTE-3 and RTE-4; [state management](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/server/server_state.py) and [Compose recipe](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/server/docker-compose.yaml).

Model names and provider URLs are configurable. The inspected defaults name `gpt-5-mini`, `text-embedding-3-small` and the spaCy package `en_core_web_sm`; these do not pin exact deployed model weights. Optional reranking scores relevance, not truth. Provider internals remain uninspected. See CMP-1, CMP-2, CMP-3 and CMP-4.

## What the evidence supports

Mem0 wires durable trace-derived text into later extraction and affords or wires host recall at the specific routes above. The comparison's trace-learning classification records that mechanism; it does not establish improved future capacity attributable to criticism. The README's benchmark numbers explicitly concern the managed platform, whose proprietary optimizations are outside this implementation boundary. No reproduced result or causal attribution is claimed. See CLM-1 and the [pinned README](https://github.com/mem0ai/mem0/blob/94c3fe9f238f3dbf29c9ce98643bd71eb13077cd/README.md).

Localized guidance and retained content are present, and named routes consume them. A working process of formulated criticism, resulting revision or changed reliance, and criticism-led iteration is not established. Theory-builder membership, reflective criticism, autonomous theory building and exercised self-improvement therefore remain uninspected as separate findings. Manual edits, a similarity score, storage success and delivered context cannot fill those missing links.

## Scope

This is a source-grounded whole-system account at Mem0's memory-service responsibility horizon, with explicit partial coverage. It establishes possible execution paths, not successful deployment, faithful activation, latency, recall benefit or complete behavior of every adapter. Candidate/source pairs and controlled recalled-content interventions would strengthen fidelity and benefit claims. A pinned deployment and inspected hosted backend would resolve different limits. The exact result preserves those distinctions instead of treating uninspected alternatives as absent.
