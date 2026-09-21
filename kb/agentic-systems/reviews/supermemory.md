---
type: kb/types/note.md
description: "Supermemory exposes requested and automatic memory delivery around an external graph engine; source visibility stops short of validating inferred facts or measured benefit."
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-21-supermemory-01
source-identity: https://github.com/supermemoryai/supermemory
reviewed-revision: "57b430b5b6a19106a989651f4cde853c05147682"
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-21-supermemory-01/result.md
analysis-result-sha256: aa8a44ae7f070b0e9303af00d8dfcdc4d4944e1f259ce2816770722bafffc0aa
---

# Supermemory

**Evidence basis:** Static code and committed documentation at `57b430b5b6a19106a989651f4cde853c05147682`, inspected on 2026-09-21. The public repository exposes memory clients and integration code; the backend engine, model internals, hosted console and separately linked plugins were not inspected. No system execution or benchmark reproduction was performed.

Supermemory supplies persistent context to agents through requested tools and automatic SDK hooks. Its distinctive boundary is the separation between inspectable acquisition/delivery code and a remote engine documented to extract facts, update a temporal graph, infer new facts and maintain profiles. The host remains responsible for agent scheduling, model decisions and tool approvals. The [exact analysis](../../reports/retained/agentic-system-analysis/AAS-2026-09-21-supermemory-01/result.md) retains the source excerpts, route records and fourteen comparison fields.

## What reaches the agent

| Route | Trigger and retained content | Evidence boundary |
|---|---|---|
| MCP search, profile, context prompt and document reads | Host/model requests memories, profile facts or source content | Client retrieval and formatting are wired; these requested returns are pull. |
| SDK middleware and voice integrations | Model-call/user-turn hooks select a container and optional query, then inject profiles or matches | Automatic supply is wired push; deployed use and actual model reliance were not observed. |
| Conversation writeback | Completed replies, incoming history or voice events, depending on integration | Acquisition is wired; durable fact/profile derivation is documented external behavior. |
| Claude memory commands | Caller requests view/create/edit/delete/rename under a file-shaped interface | The adapter stores and reads complete service documents, not local files. |

The differences are consequential: the Vercel wrapper can save a completed exchange, while some OpenAI wrappers save incoming history before the next response. A uniform “saves every answer” description would be wrong. Default middleware requests static/dynamic profile sections; available topical buckets are not automatically delivered by that path. Source: [Vercel wrapper](https://github.com/supermemoryai/supermemory/blob/57b430b5b6a19106a989651f4cde853c05147682/packages/tools/src/vercel/index.ts), [OpenAI middleware](https://github.com/supermemoryai/supermemory/blob/57b430b5b6a19106a989651f4cde853c05147682/packages/tools/src/openai/middleware.ts), [file adapter](https://github.com/supermemoryai/supermemory/blob/57b430b5b6a19106a989651f4cde853c05147682/packages/tools/src/claude-memory.ts). Exact records: RTE-5, RTE-6, RTE-7, RTE-10, RTE-11, RTE-12.

## Retention and inferred facts

The documented pipeline distinguishes source documents, extracted/inferred facts and profiles. Document status `done` means indexing has finished; default dynamic “dreaming” may still be extracting memories. Older profile content is also periodically aggregated. Together with automatic trace capture and later context delivery, this supports a **claimed** trace-learning chain. It does not establish live weight updates or measured improvement. Source: [processing contract](https://github.com/supermemoryai/supermemory/blob/57b430b5b6a19106a989651f4cde853c05147682/apps/docs/concepts/how-it-works.mdx), [profile aggregation](https://github.com/supermemoryai/supermemory/blob/57b430b5b6a19106a989651f4cde853c05147682/apps/docs/user-profiles/buckets.mdx). Exact records: OBJ-2, OBJ-3, OBJ-4, RTE-8.

The engine explicitly describes inferred facts as guesses. They remain searchable at reduced weight before review. Approval removes that penalty; decline forgets the entry; undo restores its unreviewed state. This is a documented human disposition mechanism, but no independent truth criterion or observed acceptance history was established. Default profile formatting emits strings and may omit inference/provenance metadata that other interfaces expose. Source: [inference review](https://github.com/supermemoryai/supermemory/blob/57b430b5b6a19106a989651f4cde853c05147682/apps/docs/recall/memory-review.mdx), [profile formatter](https://github.com/supermemoryai/supermemory/blob/57b430b5b6a19106a989651f4cde853c05147682/packages/tools/src/shared/prompt-builder.ts). Exact records: OBJ-5, OBJ-9, CLM-3, BAP-5.

## Controls and limits

MCP constructs a fresh server per request, but active-space state persists for an organization/user pair. An explicit tag overrides the default for one call. Document-by-ID reads can access any permitted space, so the active tag is a routing preference rather than a universal security boundary. OAuth verification and API-key authentication also differ: successful API-key lookups may be cached for 60 seconds. Backend authorization remains an external dependency. Source: [space state](https://github.com/supermemoryai/supermemory/blob/57b430b5b6a19106a989651f4cde853c05147682/apps/mcp/src/server/space.ts), [authentication](https://github.com/supermemoryai/supermemory/blob/57b430b5b6a19106a989651f4cde853c05147682/apps/mcp/src/server/auth/index.ts), [document reader](https://github.com/supermemoryai/supermemory/blob/57b430b5b6a19106a989651f4cde853c05147682/apps/mcp/src/server/tools/get-document.ts).

This boundary supports concrete conclusions about client selection, delivery, authoring and failure behavior. It cannot establish complete backend storage/curation semantics, task horizons, extraction fidelity, causal dependence on recall or advertised performance. Editable facts and files also do not establish an outcome-driven theory-repair loop or reflective revision of the system itself. Pinned engine implementation, candidate-linked review records and controlled recall interventions would materially change those assessments.
