---
type: kb/types/note.md
description: Supermemory Vercel wrapper injects retrieved context and uploads conversations,
  with best-effort saving and an uninspected remote learning bridge
generated-by: analyse-agentic-system
analysis-run: AAS-2026-09-25-supermemory-02
source-identity: https://github.com/supermemoryai/supermemory
reviewed-revision: 0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f
analysis-result: kb/reports/retained/agentic-system-analysis/AAS-2026-09-25-supermemory-02/result.md
analysis-result-sha256: 9caa72390cb63c110e48511b87eb83b612cdca25f07400c7d9ea6742e2bcf0e7
---

# Supermemory: the Vercel memory wrapper

This review covers the Vercel AI SDK `withSupermemory` subsystem at the pinned repository commit. It inspects retrieval, prompt injection, caching, generation/stream interception and conversation upload. The remote Supermemory engine, other adapters, host orchestration and model internals are excluded. The findings are code-grounded, with no execution or benchmark evidence.

Before a model call, the wrapper requests profile/search content or reuses a formatted cache entry, then inserts a managed block in system context. Profile, query and full modes choose different content. A new user turn forces retrieval; continuation steps can reuse a matching nonempty cached string. The cache has capacity 100, no configured TTL and no upload-triggered invalidation. Local duplicate filtering compares normalized text, with mode-dependent static/dynamic/search priority; it does not establish semantic equivalence or backend fact revision. [Retrieval path](https://github.com/supermemoryai/supermemory/blob/0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f/packages/tools/src/vercel/middleware.ts#L292-L384), [cache](https://github.com/supermemoryai/supermemory/blob/0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f/packages/tools/src/shared/cache.ts#L8-L73).

By default a retrieval failure clears the managed memory block and continues the base call; callers can choose failure instead. Delimiter escaping protects the block's syntax. Neither the readonly marker nor system placement validates the recalled statements or establishes actual behavioral influence. Query selection is delegated to an uninspected service, so the complete read-back mechanism cannot be classified from local code alone. The profile request uses containerTag and optional query text, not the conversation customId. [Context helper](https://github.com/supermemoryai/supermemory/blob/0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f/packages/tools/src/shared/memory-context.ts#L1-L41), [profile request](https://github.com/supermemoryai/supermemory/blob/0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f/packages/tools/src/shared/memory-client.ts#L28-L71).

After generation, or on normal stream flush, the wrapper can upload original conversation messages and captured assistant text. Saving is not awaited before returning the model result or completing flush, and save errors are logged and suppressed. No separate canceled-stream save path is wired. Thus model completion does not confirm a durable memory write. System messages are omitted; image payloads are supported; structured tool-call/result parts are opt-in, while a generic string-content tool-role message can pass without that option. [Generation and stream paths](https://github.com/supermemoryai/supermemory/blob/0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f/packages/tools/src/vercel/index.ts#L154-L298), [conversion](https://github.com/supermemoryai/supermemory/blob/0e12f0b3a65af1cf7b03f48561f20ddf4369bc3f/packages/tools/src/vercel/middleware.ts#L62-L188).

The strongest supported contribution is a concrete automatic context-delivery and conversation-capture integration. The source does not expose the transformation connecting uploaded traces to later profile facts. Trace learning and its timing/scope/form therefore remain undetermined at this boundary, rather than inferred from product claims. Included image content also prevents a complete natural-language/symbolic representation classification. Conjectural learning, reflection and self-improvement remain uninspected; static prompt/payload tests do not establish answer dependence or capacity gains.

The [exact result](../../reports/retained/agentic-system-analysis/AAS-2026-09-25-supermemory-02/result.md) retains quotes, canonical routes, the full memory comparison and epistemic assessment. Pinned remote-engine evidence, upload-completion traces and controlled host-memory interventions would change separate parts of this assessment.
