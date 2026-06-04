---
description: "Supermemory review: hosted memory API with MCP/browser/SDK wrappers, conversation trace capture, profile/search read-back, and graph claims"
type: ../types/agent-memory-system-review.md
tags: [trace-derived, push-activation]
status: current
last-checked: "2026-06-02"
---

# supermemory

Supermemory, from `supermemoryai/supermemory`, is an open-source monorepo around a hosted memory and context service. At the reviewed commit, the repo contains the public docs, MCP server, browser extension, memory graph UI package, SDK/tool wrappers, and framework middleware. The core hosted backend that extracts facts, builds graph relationships, embeds/chunks content, and serves `/v3` and `/v4` endpoints is not fully implemented in this checkout, so this review treats those backend behaviors as API-side contracts unless client or wrapper code shows the behavior directly.

**Repository:** https://github.com/supermemoryai/supermemory

**Reviewed commit:** [268499068810586495ba5bd4773f8c5786d9fc97](https://github.com/supermemoryai/supermemory/commit/268499068810586495ba5bd4773f8c5786d9fc97)

**Last checked:** 2026-06-02

## Core Ideas

**The open repo is mostly integration and product surface around a hosted memory API.** The README positions Supermemory as a memory and context layer with documents, memories, user profiles, hybrid search, connectors, and multi-modal extraction, but the checked-in implementation mostly calls hosted endpoints such as `/v3/documents`, `/v4/search`, `/v4/profile`, and `/v4/conversations` from apps and packages ([README.md](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/README.md), [utils/api.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/browser-extension/utils/api.ts), [conversations-client.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/conversations-client.ts)). The reviewable code is therefore strongest as an activation, capture, and adoption layer, not as a complete self-hosted memory engine.

**Memory is exposed as documents, memories, profiles, and search results.** The docs distinguish raw documents from "intelligent knowledge units" called memories, describe update/extend/derive relationships, and expose profile responses split into `static` stable facts and `dynamic` recent context ([how-it-works.mdx](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/docs/concepts/how-it-works.mdx), [graph-memory.mdx](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/docs/concepts/graph-memory.mdx), [api.mdx](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/docs/user-profiles/api.mdx)). The MCP client type also surfaces `DocumentMemoryEntry` fields such as `isStatic`, `isLatest`, `isForgotten`, `forgetAfter`, `version`, `parentMemoryId`, and `rootMemoryId`, which is code evidence that the API exposes memory lifecycle and version state to clients ([client.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/mcp/src/client.ts)).

**Read-back is implemented in several host-native wrappers.** The MCP server registers `memory`, `recall`, profile/resource, project, and memory-graph tools, plus a `context` prompt that returns stable preferences and recent activity with an instruction to save future memory-worthy facts ([server.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/mcp/src/server.ts)). The TypeScript, OpenAI, Vercel AI SDK, Mastra, and Python integrations fetch profile/search context and insert it into system prompts or framework input processors before model calls ([memory-client.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/shared/memory-client.ts), [middleware.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/openai/middleware.ts), [processor.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/mastra/processor.ts), [middleware.py](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/openai-sdk-python/src/supermemory_openai/middleware.py)).

**Trace capture is implemented at the integration edge.** Vercel/OpenAI/Mastra wrappers can save conversation messages after responses through `/v4/conversations`, while the browser extension can capture submitted ChatGPT and Claude prompts when auto-capture is enabled and save them as documents through `/v3/documents` ([middleware.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/vercel/middleware.ts), [middleware.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/openai/middleware.ts), [processor.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/mastra/processor.ts), [chatgpt.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/browser-extension/entrypoints/content/chatgpt.ts), [claude.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/browser-extension/entrypoints/content/claude.ts)). That is enough to classify the open system as trace-derived, but the extraction oracle that converts those traces into profile facts or graph relationships is API-side and not locally auditable.

**Context efficiency comes from mode selection, query scoping, deduplication, caps, and caching, not from a visible token planner.** The shared memory builder supports `profile`, `query`, and `full` modes, extracts the latest user message for query modes, calls `/v4/profile`, deduplicates static, dynamic, and search-result memories, and formats the result into a compact prompt block ([memory-client.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/shared/memory-client.ts), [tools-shared.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/tools-shared.ts), [prompt-builder.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/shared/prompt-builder.ts)). The MCP client truncates returned memory text at 200,000 characters, wrappers provide `limit`, `chunkThreshold`, turn-key caches, and optional retrieval timeout, but I did not find a token-budgeted assembler or progressive disclosure protocol in the open integration code ([client.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/mcp/src/client.ts), [middleware.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/vercel/middleware.ts)).

**Adoption affordance is the dominant design strength.** Supermemory meets agents where they already run: MCP clients, browser ChatGPT/Claude/T3 surfaces, AI SDK tools, OpenAI clients, Mastra processors, Python packages, Raycast, docs, and memory-graph UI. The cost is that many high-value claims depend on the hosted API implementation, so local code review can verify the integration contracts more than the memory engine internals.

## Artifact analysis

- **Storage substrate:** `service-object` — Supermemory's hosted API and data stores, reached through `/v3/documents`, `/v4/search`, `/v4/profile`, `/v4/conversations`, and SDK wrappers; the exact database/vector/graph substrates are not implemented in this checkout
- **Representational form:** `prose` `symbolic` `parametric` — raw text/HTML/Markdown and memory strings, structured conversation messages plus lifecycle/version metadata, and API-side embeddings/search state
- **Lineage:** `authored` `imported` `trace-extracted` — authored wrapper and prompt-policy behavior, imported user/URL/page/connector sources, and prompt/conversation/tool traces captured at integration edges
- **Behavioral authority:** `knowledge` `instruction` `routing` `ranking` `learning` — returned memories advise as knowledge, prompt/tool descriptions instruct, wrappers route memory into host calls, hosted search ranks results, and capture wrappers decide what enters memory

**Hosted documents and memory entries.** Storage substrate: Supermemory's hosted API and data stores, reached through `/v3/documents`, `/v4/search`, `/v4/profile`, `/v4/conversations`, and SDK wrappers; the exact database/vector/graph substrates are not implemented in this checkout. Representational form: mixed raw text/HTML/Markdown, structured conversation messages, metadata, memory strings, lifecycle/version fields, and API-side embeddings/search state. Lineage: imported from user saves, URLs, browser-captured pages, prompt captures, agent conversation traces, and connector sources; API-side chunking, extraction, embedding, update/forget logic, and graph inference are described in docs but not locally auditable. Behavioral authority: knowledge artifact when returned as memories/search results/documents; ranking and filtering authority when the hosted service orders results, marks latest/forgotten state, or builds profile arrays.

**Profile response.** Storage substrate: hosted `/v4/profile` response consumed by MCP, SDKs, middleware, and examples. Representational form: symbolic JSON containing `profile.static`, `profile.dynamic`, and optional `searchResults`, then prose Markdown when formatted for prompts. Lineage: API-side derived view over stored documents/memories and optional query; invalidation is opaque from local code except that new documents/conversations and forget operations can change future responses. Behavioral authority: advisory context when manually fetched; system-definition authority in integrations that insert it into a system prompt or framework input processor before generation.

**Trace capture wrappers.** Storage substrate: integration package code plus hosted documents/conversation records created by API calls. Representational form: symbolic code that converts OpenAI, Vercel, Mastra, browser, and MCP events into prose or structured messages. Lineage: authored wrapper behavior over live user/assistant/tool traces; each saved trace is raw or lightly formatted source material for the hosted memory service. Behavioral authority: capture and scheduling authority over what enters memory; not extraction authority, because the fact/profile generation step happens behind the API boundary.

**Read-back and prompt-injection policies.** Storage substrate: package source, MCP server code, prompt templates, tool descriptions, schemas, cache keys, and configuration options. Representational form: symbolic TypeScript/Python plus prose prompt templates and tool descriptions. Lineage: authored system-definition artifacts; changing mode defaults, query extraction, deduplication, prompt formatting, timeout, cache key, tool description, or `limit` changes what memory can reach future model calls. Behavioral authority: system prompt injection, tool routing, recall formatting, memory-save prompting, and search/result selection.

**Browser extension state and UI hooks.** Storage substrate: browser extension storage, DOM datasets, background script, content scripts, and the hosted API. Representational form: symbolic DOM observers/event handlers plus transient prose snippets appended to input fields. Lineage: user actions, auto-search setting, auto-capture setting, selected page text, ChatGPT/Claude/T3 prompt text, and search results returned by the API. Behavioral authority: event-keyed capture and user-facing insertion into the next prompt field; effective model authority depends on the host UI submitting the modified text.

**MCP session and graph UI surfaces.** Storage substrate: Cloudflare Durable Object storage for MCP client info, cached container tags in the server instance, hosted document/memory data, and the bundled MCP app resource. Representational form: symbolic MCP tools/resources/prompts and graph UI structured content. Lineage: OAuth/API-key authenticated API calls plus fetched documents and memory entries. Behavioral authority: tool/resource/prompt availability for clients, profile/context read-back, and human/agent graph inspection; it does not itself compute graph relationships.

Promotion path: Supermemory's intended path is raw content or conversation trace to processed document, memory entries, graph/lifecycle state, profile summary, search results, and injected context. The open code verifies capture and read-back parts of that path. It does not expose a locally reviewable promotion gate from candidate fact to accepted static/dynamic profile item, nor a rule/validator/instruction promotion ladder comparable to Commonplace.

## Comparison with Our System

| Dimension | Supermemory | Commonplace |
|---|---|---|
| Primary purpose | Hosted memory/context service plus integrations | Git-native methodology KB for agent operation |
| Canonical retained artifact | API-side document, memory entry, profile fact, conversation record | Typed Markdown note, source snapshot, instruction, review, index, report |
| Storage substrate | Hosted API/data stores, browser storage, MCP Durable Objects, package code | Repository files, generated indexes, validation/review reports |
| Write path | API add/search/profile/conversation calls, browser saves, MCP tools, framework output processors | Authored/source-derived artifacts, explicit validation and review |
| Read-back | Pull tools/search plus pre-call system prompt/profile injection | Mostly explicit pull through `rg`, indexes, links, skills, and loaded instructions |
| Governance | API auth, schemas, tool descriptions, forget fields, integration tests/examples; backend governance not visible | Collection contracts, type specs, git diffs, validators, semantic gates, replacement archives |

Supermemory is stronger than Commonplace as an adoption and activation layer. A developer can add memory to an OpenAI, Vercel, Mastra, browser, or MCP workflow without designing storage, extraction, search, or profile assembly. Commonplace is stronger where the question is artifact governance: every durable artifact can be read, diffed, typed, validated, cited, and promoted or retired through repository process.

The main tradeoff is opacity versus ergonomics. Supermemory's hosted API returns useful high-level surfaces like static/dynamic profile and search results, but the reviewed repo does not let us audit the extraction oracle, contradiction handling, embedding model, graph construction, or profile cache. Commonplace exposes the artifact and validator machinery but asks agents to navigate and compose context more deliberately.

**Read-back:** `both` — With engineered push activation. MCP `recall`, API search, and SDK tools are pull surfaces, while OpenAI/Vercel/Mastra/Python middleware and MCP `context` prompt paths can fetch profile/search context before generation and inject it into system or prompt context; the browser extension can also append related memories into the prompt field before submission.

### Borrowable Ideas

**Expose profile and query memory as one read-back call.** Ready as a design target, not as a direct implementation. Commonplace could offer a command that returns stable loaded context plus query-specific evidence in one formatted artifact, while preserving citations and source paths.

**Keep host integrations thin and explicit.** Ready now. Supermemory's wrappers show that storage and extraction can remain behind a stable API while each host decides whether memory is a tool, resource, prompt, input processor, or middleware.

**Deduplicate profile and search memories before prompt injection.** Ready now for generated context bundles. Commonplace could deduplicate loaded notes, rules, and search hits across "always useful" and query-specific sets before presenting them to an agent.

**Borrow the static/dynamic profile split carefully.** Needs a Commonplace use case. The split is useful for persistent preferences versus recent activity, but in Commonplace it should be encoded as artifact type, freshness, lineage, and authority rather than just two arrays.

**Do not borrow API-side opacity for methodology knowledge.** Supermemory's hosted backend is appropriate for product memory, but Commonplace's core methodology artifacts should remain inspectable files with validation and review evidence.

## Trace-derived learning placement

- **Trace source:** `session-logs` `tool-traces` `event-streams` — conversation and prompt messages, tool-call fields where available, and browser/framework/MCP event hooks feed the hosted memory service
- **Learning scope:** `per-project` `cross-task` — container tags, project/default-project state, and custom conversation ids scope memory that can be reused across later calls and tasks
- **Learning timing:** `online` — browser, framework, and MCP capture/retrieval paths run during conversations; backend distillation timing beyond the hosted API is not locally visible
- **Distilled form:** `prose` `symbolic` `parametric` — profile/memory strings, lifecycle/search metadata, and API-side embeddings/search state are the visible distilled surfaces

**Trace source.** Supermemory qualifies as trace-derived from the open integration code. Vercel middleware saves full conversation messages after an assistant response; OpenAI middleware can save chat messages or Responses API input; Mastra output processors save post-generation messages; browser extension content scripts capture submitted prompts from ChatGPT and Claude when auto-capture is enabled; MCP `memory` lets the receiving agent save user facts and forget outdated information ([middleware.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/vercel/middleware.ts), [middleware.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/openai/middleware.ts), [processor.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/mastra/processor.ts), [chatgpt.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/browser-extension/entrypoints/content/chatgpt.ts), [claude.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/browser-extension/entrypoints/content/claude.ts), [server.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/mcp/src/server.ts)).

**Extraction.** The code-grounded extraction boundary is partial. The open wrappers extract prompt or conversation text, preserve message roles/tool-call fields where available, scope it with container tags/custom ids, and send it to hosted endpoints. The hosted API then returns profile static/dynamic facts and search results, and docs describe automatic extraction, updates, extends, derives, and forgetting, but I did not find the backend extractor, judge, contradiction resolver, or graph builder in this checkout ([conversations-client.ts](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/packages/tools/src/conversations-client.ts), [api.mdx](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/docs/user-profiles/api.mdx), [graph-memory.mdx](https://github.com/supermemoryai/supermemory/blob/268499068810586495ba5bd4773f8c5786d9fc97/apps/docs/concepts/graph-memory.mdx)).

**Four fields.** The raw stage is conversation/prompt/document capture: hosted storage, prose or structured-message representation, lineage from user/assistant/tool traces, and knowledge/source authority until processed. The distilled stage is API-returned memories/profile/search: hosted storage, prose memory strings plus symbolic lifecycle/search metadata, lineage from API-side processing, and advisory or prompt-injection authority. The system-definition layer is the wrapper code and tool/prompt descriptions that decide when raw traces are saved and when distilled profile/search output reaches a model.

**Scope and timing.** Scope is by container tag, project/default project, custom conversation id, and sometimes browser/default project state. Timing is mixed: browser prompt capture runs at submission time; framework output processors save after generation; pre-call middleware retrieves before the next model call; MCP `memory` capture is agent/tool initiated during a conversation.

**Survey placement.** Supermemory belongs in the service-owned trace-to-profile/search family. It strengthens the survey distinction between integration-edge trace capture and backend distillation: the open repo makes capture and activation easy to verify, while the most important learning oracle is hidden behind a hosted API boundary.

## Read-back placement

**Read-back:** `both` — Direct search, MCP `recall`, `memory-graph`, documents listing, and SDK tools are pull. Middleware and prompt/resource paths are push from the receiving model's perspective because they assemble retained profile/search memory before generation or insert related memories into the prompt field before submission.

**Read-back signal:** `coarse` `inferred / lexical` `inferred / embedding` — profile/context paths load coarse container profile memory, while query/full/browser paths send prompt text to hosted semantic/hybrid search for instance-targeted recall.

**Read-back timing:** `pre-action` — middleware, MCP prompt/resource paths, and browser prompt insertion assemble retained memory before the receiving model generation or user submission.

**Faithfulness tested:** `no` — wrapper tests and examples cover construction paths, but the review found no local with/without-memory ablation proving downstream behavior changes.

**Targeting and signal.** Push targeting is mixed. `profile` mode and MCP `context` are `coarse`: they load the configured container's static/dynamic profile without deriving relevance from the current instance. `query` and `full` middleware modes, OpenAI Responses wrapping, MCP `recall` when used by a host for another agent, and browser auto-search/prompt insertion are `instance` targeted: the local code extracts the latest user message or prompt text and sends it as `q` to the hosted profile/search API. The instance signal is `inferred`, primarily content-based search; Supermemory docs and MCP search expose semantic/hybrid search, but the hosted `/v4/profile` ranking sub-kind and precision/recall are not locally verifiable from this checkout. Container tag, project, custom id, threshold/limit parameters, cache keys, and client-side deduplication are scoping and complexity controls rather than the relevance signal itself.

**Timing relative to action.** Read-back happens before model generation in middleware and before user prompt submission in the browser extension. Trace saves happen after response or on prompt submission and affect later turns, not the already-completed response.

**Selection, scope, and complexity.** Selection is bounded by mode (`profile`, `query`, `full`), container tag, `limit`, `threshold` in some calls, default chunk threshold, deduplication, turn-key cache, and a coarse 200,000-character cap in the MCP client. Complexity is moderate: wrappers flatten static profile, dynamic profile, and search memories into Markdown/prose prompt blocks rather than loading a graph structure.

**Authority at consumption.** Tool calls and recall output are advisory unless the host prompt uses them. Middleware-injected memory has stronger practical authority because it enters the system prompt or input processor before generation. MCP `context` also instructs the agent to save future memory-worthy facts, giving it instruction authority inside clients that load the prompt.

**Faithfulness.** I found tests and examples for wrapper behavior and memory tool construction, but no local with/without-memory ablation proving injected memories change downstream agent behavior reliably. Effective authority and retrieval quality are runtime properties outside this code read.

**Other consumers.** Human users consume the dashboard, browser extension UI, memory graph UI, Raycast extension, docs, and MCP app resource. Developers consume SDKs and tools. These are adoption and inspection surfaces, separate from whether memory reaches a model automatically.

## Curiosity Pass

**The repo's most reviewable contribution is activation plumbing.** The product language is about memory extraction and graph reasoning, but the code we can inspect most confidently is about moving memory into and out of existing agents.

**The profile API is a strong interface even when the implementation is opaque.** Returning stable facts, recent facts, and optional query results gives callers a compact context contract. For Commonplace, the analogue would need traceable source paths and freshness semantics.

**Browser prompt mutation is powerful but brittle.** The extension stores related memories in `dataset.supermemories` and may append them to the input before submission. That gives strong activation with low integration cost, but it depends on host DOM structure and user-visible prompt text.

**The memory graph UI is an inspection surface, not evidence of local graph construction.** It fetches documents with memory entries and renders relationships; the graph builder itself lives behind the API.

**Forgetting is exposed more concretely than extraction.** The MCP client tries exact forget first, falls back to semantic search above a high threshold, and calls `memories.forget`. That is a useful lifecycle affordance even though delete semantics remain API-side.

## What to Watch

- Whether the hosted extraction, contradiction, update/extend/derive, embedding, and profile-generation code becomes inspectable or self-hostable; that would change confidence in the trace-derived section.
- Whether read-back gains explicit token budgets, source citations, profile freshness metadata, and source-to-memory provenance in the prompt output.
- Whether the browser extension's DOM-based prompt injection moves to official host APIs where available; that would reduce activation brittleness.
- Whether profile/static/dynamic facts expose lineage, confidence, expiry, and review state through SDK/MCP surfaces.
- Whether memory graph APIs expose enough edge provenance to distinguish authored memories, inferred memories, updates, extends, and derives in downstream tools.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Supermemory captures prompt/conversation traces at integration edges and returns hosted profile/search artifacts for later activation.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Supermemory pairs hosted storage with explicit MCP/search pull and several pre-call push activation paths.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: Supermemory requires separating hosted documents, memory entries, profiles, trace wrappers, prompt templates, and UI/MCP surfaces.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: documents, memories, search results, graph views, and profile facts advise as evidence or context until injected with stronger authority.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: middleware, MCP prompts/tools, tool descriptions, query extraction, deduplication, and prompt builders constrain capture and read-back behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies with caveat: the open code captures traces, while extraction into durable profile/search artifacts is API-side.
