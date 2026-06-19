---
description: "Stash review: MCP-served Postgres/pgvector memory with episodes, consolidated facts, graph-like relations, goals, failures, hypotheses, and decay"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
status: current
last-checked: "2026-06-05"
---

# Stash

Stash, from `alash3al/stash`, is a self-hosted Go MCP server that gives compatible agents a persistent memory service backed by PostgreSQL and pgvector. It stores raw episodes, embeds them for semantic recall, consolidates them into structured facts and relationship-like records, tracks temporary working context, goals, failures, contradictions, causal links, hypotheses, and confidence decay, and exposes the whole surface through MCP-over-SSE plus health and metrics endpoints.

**Repository:** https://github.com/alash3al/stash

**Reviewed commit:** [93601c1f4e0fb42df99d2de33567095020fb6d7e](https://github.com/alash3al/stash/commit/93601c1f4e0fb42df99d2de33567095020fb6d7e)

**Last checked:** 2026-06-05

## Core Ideas

**Stash is a tool-mediated memory substrate, not an autonomous agent loop.** The README frames it as persistent memory for any MCP-compatible agent, and Docker Compose starts Postgres plus an MCP SSE server on port 8080 with optional background consolidation ([README.md](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/README.md), [docker-compose.yml](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/docker-compose.yml)). The code wires MCP tools for initialization, remembering, recall, namespace management, consolidation, context, facts, relationships, contradictions, causal chains, hypotheses, goals, and failures; host agents decide when to call them ([cmd/cli/mcp.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/cmd/cli/mcp.go)).

**The standing store splits raw observations from distilled knowledge.** `Remember` inserts an episode with content, namespace, timestamp, embedding, and embedding model, while `Recall` searches both consolidated facts and raw episodes by query embedding and returns a merged ranked result set ([internal/brain/episode.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/episode.go), [internal/brain/recall.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/recall.go), [internal/queries/recall.sql.tmpl](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/queries/recall.sql.tmpl)). Consolidation then clusters similar episodes, asks a reasoner for a structured fact, embeds it, records source episode ids, and skips near-duplicate facts ([internal/brain/consolidate.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/consolidate.go)).

**The consolidation pipeline is broad and checkpointed.** `ConsolidateByID` runs stages for episodes-to-facts, facts-to-relationships, causal links, goal progress, failure pattern detection, facts/relationships-to-patterns, hypothesis evidence scanning, and confidence decay, then persists per-namespace checkpoints so later runs process only new ids ([internal/brain/consolidate.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/consolidate.go), [internal/db/migrations/00010_create_consolidation_progress.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00010_create_consolidation_progress.sql), [internal/db/migrations/00020_add_consolidation_checkpoints.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00020_add_consolidation_checkpoints.sql)). The README calls this a nine-stage pipeline, but the inspected code comments enumerate eight main stages plus inserted sub-stages and newer goal/failure/hypothesis checkpoints.

**Context efficiency is mostly namespace scoping plus embedding-ranked pull.** Namespaces are hierarchical, `/` can resolve all namespaces, and recall limits are capped at 100 results; fact and episode SQL orders by vector distance and the returned result set is sorted by score ([internal/brain/brain.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/brain.go), [internal/brain/recall.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/recall.go)). There is no token budget, progressive disclosure bundle, reranker, or context-packing layer inside Stash; the MCP descriptions tell the host agent when and how to retrieve, but returned JSON can still be large or semantically complex if the caller asks broadly.

**The MCP prompt gives memory operational force.** The embedded server description instructs compatible agents to initialize first, recall before answering questions with history, proactively remember durable signal, consolidate periodically, and report memory failures rather than pretending ([cmd/cli/mcp_prompts.tmpl](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/cmd/cli/mcp_prompts.tmpl)). That prompt is an authored system-definition artifact; it can influence a compliant host agent, but it is not code that automatically injects stored memories into every model call.

**The quality model is a mix of LLM extraction rules and symbolic guards.** The OpenAI reasoner uses a strict extraction system prompt, retries invalid JSON, validates some grounding and id references, and clamps confidence values ([internal/reasoner/openai.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/reasoner/openai.go)). Postgres schemas add confidence ranges, status enums, soft-delete timestamps, validity intervals, source links, and uniqueness constraints for causal links ([internal/db/migrations/00005_create_facts.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00005_create_facts.sql), [internal/db/migrations/00014_create_contradictions.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00014_create_contradictions.sql), [internal/db/migrations/00016_create_causal_links.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00016_create_causal_links.sql), [internal/db/migrations/00017_create_hypotheses.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00017_create_hypotheses.sql)).

## Artifact analysis

- **Storage substrate:** `rdbms` `vector` — The durable store is PostgreSQL tables for namespaces, episodes, facts, sources, relationships, patterns, contexts, contradictions, causal links, hypotheses, goals, failures, settings, checkpoints, and embedding cache, with pgvector columns and vector indexes for embedding search and duplicate checks ([internal/db/migrations](https://github.com/alash3al/stash/tree/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations), [internal/bootstrap/bootstrap.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/bootstrap/bootstrap.go)).
- **Representational form:** `prose` `symbolic` `parametric` — Episodes, facts, contexts, goals, failures, hypotheses, patterns, and contradiction notes are prose-like text; namespaces, schemas, ids, confidence values, status enums, source links, checkpoints, MCP tool schemas, and prompt templates are symbolic; embeddings and vector distances are parametric retrieval state.
- **Lineage:** `authored` `imported` — Namespaces, episodes, contexts, goals, failures, hypotheses, causal links, and the MCP/server prompts are authored by users, agents, or developers through the tool surface; facts, relationships, patterns, contradictions, goal notes, failure-pattern facts, hypothesis status/confidence changes, causal links, embeddings, and checkpoints are derived from those stored entries. I did not find durable extraction from session logs, tool traces, event streams, or trajectories, so this review does not mark Stash as trace-derived.
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — Retrieved episodes, facts, contexts, goals, failures, hypotheses, relationships, and causal links advise host agents as knowledge; MCP descriptions and the server prompt instruct host behavior; namespaces, tool parameters, checkpoints, contexts, and causal-chain traversal route lookup and maintenance; schema checks, status transitions, contradiction records, validity intervals, and health/ready endpoints validate state; vector scoring, confidence, priorities, and decay rank attention; consolidation outputs become learning input for future host-agent behavior.

**Episodes and facts.** Episodes are raw, timestamped, embedded observations; facts are higher-quality consolidated records with confidence, optional structured entity/property/value fields, validity intervals, embeddings, and source episode links ([internal/db/migrations/00004_create_episodes.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00004_create_episodes.sql), [internal/db/migrations/00005_create_facts.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00005_create_facts.sql), [internal/db/migrations/00006_create_fact_sources.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00006_create_fact_sources.sql), [internal/db/migrations/00013_add_fact_structured_fields.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00013_add_fact_structured_fields.sql)). The source links are important: they make a derived fact auditable back to the stored episodes, but not back to any external transcript unless the host stored that transcript content as an episode.

**Graph and reasoning records.** Relationships, patterns, causal links, contradictions, hypotheses, goals, and failures are stored as separate tables rather than a single graph database. They still create graph-like navigational surfaces: entity edges, cause/effect chains, fact-sourced patterns, unresolved contradictions, goal trees, and hypothesis-to-fact promotion ([internal/brain/causal.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/causal.go), [internal/brain/goal.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/goal.go), [internal/brain/hypothesis.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/hypothesis.go)).

**Working context.** Context rows are one per namespace, contain a focus string plus expiration time, and are set/read/cleared by explicit tools ([internal/brain/context.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/context.go), [internal/db/migrations/00009_create_contexts.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00009_create_contexts.sql)). This is a useful short-handoff artifact, but it is not a generalized activation engine: callers must know the exact namespace and invoke `get_context`.

**MCP contract and prompts.** The tool schemas and prompt template are high-authority operational artifacts because they tell a host agent when it should write, read, consolidate, and admit failure. Their effect depends on the host respecting MCP descriptions and using tool outputs faithfully; the Stash server itself does not verify downstream uptake.

**Promotion path.** Stash promotes raw episodes into embedded facts, facts into relationships/causal links/patterns, hypotheses into confirmed facts, and old facts into superseded or expired state. This is stronger than a passive vector store because the memory surface changes authority and shape over time, but the promotion oracle is mostly an LLM reasoner plus local symbolic checks rather than human review.

## Comparison with Our System

Stash and Commonplace both treat retained material as something that can guide later agents, but they choose different authority centers. Stash is a runtime memory service: host agents write observations, then Stash derives searchable, structured, and decayed records in Postgres. Commonplace is a repo-native knowledge base: agents write typed Markdown artifacts under collection contracts, validate them, review them, cite sources, and keep their authority visible in git.

The biggest alignment is the raw-to-distilled distinction. Stash's episodes-to-facts pipeline resembles Commonplace's source/workshop-to-note promotion, except Stash runs it as an LLM-backed service operation and stores the result in tables. Commonplace keeps the promotion path inspectable as files, diffs, schemas, and review artifacts; Stash keeps it operationally convenient and available over MCP.

The biggest divergence is read-back. Commonplace relies on lexical search, indexes, authored links, and explicit loading by the working agent. Stash also remains pull-driven, but it adds a prompt contract telling host agents to recall before historically sensitive answers and to remember durable signal proactively. That is a pragmatic adoption affordance, though it still trusts the host agent to comply.

Stash is stronger than Commonplace at lightweight runtime continuity: a compatible agent can store a preference, recall it by semantic similarity, and consolidate later without editing a repo. Commonplace is stronger at durable methodology claims, provenance, reviewability, source citation, and preventing derived conclusions from quietly acquiring more authority than their evidence supports.

### Borrowable Ideas

**Session-start memory protocol as tool text.** Commonplace skills could include a concise "read before answering history-sensitive questions" decision tree for local search and relevant indexes. Ready now as instruction wording, provided it stays tied to explicit evidence paths.

**Short-lived namespace context.** A one-row-per-workshop or one-row-per-review "current focus" handoff could reduce noisy session summaries. Needs a concrete workflow first because Commonplace already has `kb/work/` for visible in-flight state.

**Checkpointed promotion runs.** Stash's per-namespace consolidation checkpoints are a good model for large review or source-processing jobs that should only process new records. Ready for generated review machinery, not for ordinary notes.

**Contradiction records with supersession intervals.** Commonplace could borrow explicit contradiction/supersession metadata for reviews or claims that become stale, rather than only archiving whole files. Needs a claim-level artifact surface before implementation.

**Do not borrow opaque LLM promotion as authority.** Stash's automatic facts and patterns are useful, but Commonplace should keep source citations, human-readable drafts, validation, and semantic review before derived claims become library notes.

## Write side

**Write agency:** `manual` `automatic` — Agents and users manually create namespaces, remember episodes, set contexts, create goals, failures, hypotheses, and asserted causal links; automatic paths embed remembered text, cache embeddings, run background or manual consolidation, derive facts/relationships/causal links/patterns, update goals and hypotheses, supersede contradicted facts, decay confidence, expire weak facts, and persist checkpoints.

**Curation operations:** `consolidate` `dedup` `evolve` `synthesize` `invalidate` `decay` `promote` — Consolidation reduces similar episodes into facts; vector duplicate checks skip already-known facts; goal notes, hypothesis confidence/status, and fact confidence/validity evolve in light of new evidence; pattern, causal, failure-pattern, and hypothesis evidence passes can create new inferred records across stored entries; contradiction replacement and low-confidence expiry invalidate old facts; decay down-weights stale facts; confirmed hypotheses become facts and raw episodes become higher-authority structured facts.

Stash has non-trivial automatic maintenance, but I did not include a trace-derived learning subsection because the inspected code does not automatically derive durable artifacts from session logs, tool traces, event streams, repeated trajectories, or rollouts. The raw inputs are episodes deliberately written through `remember`, failures/goals/hypotheses written through explicit tools, and derived database records produced from those entries.

## Read-back

**Read-back:** `pull` — Stored memory reaches a host agent when the agent, user, or host deliberately calls MCP tools such as `recall`, `query_facts`, `query_relationships`, `get_context`, `list_goals`, `list_failures`, `list_hypotheses`, `list_contradictions`, or `trace_causal_chain`; I did not find server code that automatically injects stored memory into future model invocations.

The closest edge case is the MCP server description: it instructs agents to initialize first, recall at session start when history may matter, recall before historically sensitive answers, and write useful durable information without waiting for the user to say "remember this" ([cmd/cli/mcp_prompts.tmpl](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/cmd/cli/mcp_prompts.tmpl)). That is a pushy instruction surface, but the memory content still arrives only after a tool call, so the Stash-side read-back mechanism is pull.

Selection is controlled by namespace paths and descendants, vector similarity, facts-first search, result limits, pagination, exact context namespace, causal-chain depth, status filters, and consolidation state. Effective faithfulness is not tested by Stash itself: the code tests mechanics and validates some extraction outputs, but I did not find a with/without memory ablation, perturbation test, or post-answer audit proving that retrieved memories changed host-agent behavior.

Other consumers include human users reading MCP/CLI JSON, the background consolidation loop, health/metrics observers, and host agents that interpret the MCP prompt and tool descriptions as operating instructions.

## Curiosity Pass

**The README's "amnesia fixed" framing depends on host compliance.** Stash gives a rich memory surface, but forgetting is still possible if the host agent ignores the MCP descriptions, fails to recall before answering, or stores vague/noisy episodes.

**The system has more truth-maintenance machinery than most MCP memory servers.** Contradiction records, `valid_until`, confidence decay, hypothesis status transitions, and soft deletes make Stash more than a vector recall wrapper, even though the evidence oracle remains mostly LLM-mediated.

**The "knowledge graph" is table-shaped.** Relationships and causal links are stored in relational tables with ids and constraints, not a graph substrate. That is probably the right engineering choice for a small self-hosted service, but reviews should not overstate it as a full graph memory engine.

**The trace-learning boundary is subtle.** The MCP prompt encourages end-of-session summaries and proactive memory writes, which can approximate trace distillation if a host agent writes summaries of its own work. The repository does not implement automatic capture from transcripts or tool traces, so the trace-derived tag would overclaim.

**Context expiration is stored but not enforced on read.** `SetContext` writes an `expires_at`, but `GetContext` returns the row it finds without checking expiry in the inspected code ([internal/brain/context.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/context.go)). Host instructions say stale context should be cleared, so expiry currently looks advisory rather than enforced.

## What to Watch

- Whether Stash adds automatic transcript, tool-call, or event-stream capture; that would change the trace-derived verdict and require a raw-trace/distilled-artifact split.
- Whether read-back becomes host-integrated push, such as session-start memory injection or situation-triggered recall middleware, rather than MCP tool pull.
- Whether derived facts and patterns gain stronger provenance displays, review state, or human approval before they influence future answers.
- Whether context expiry is enforced in `GetContext` or cleanup paths; that would make working context less likely to leak stale handoffs.
- Whether consolidation outputs get tokenizer-aware limits or bundle shaping before returning to agents; broad recall and graph queries can otherwise dilute context.

Relevant Notes:

- [Knowledge storage does not imply contextual activation](../../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - distinguishes: Stash stores durable memory, but the inspected read-back path is explicit MCP-tool pull.
- [Axes of artifact analysis](../../../notes/axes-of-artifact-analysis.md) - applies: Stash's episodes, facts, vectors, checkpoints, prompts, and derived records carry different forms and authorities.
- [Knowledge artifact](../../../notes/definitions/knowledge-artifact.md) - classifies: retrieved memories, facts, contexts, failures, goals, hypotheses, and graph-like records mostly advise host agents as evidence or context.
- [System-definition artifact](../../../notes/definitions/system-definition-artifact.md) - classifies: MCP tool schemas, prompt templates, namespaces, status rules, and validation checks instruct or constrain behavior.
- [Storage substrate](../../../notes/definitions/storage-substrate.md) - relates: Stash uses a relational/vector database rather than files or a repo-native library as the durable substrate.
- [Lineage](../../../notes/definitions/lineage.md) - frames: Stash's fact-source rows and consolidation checkpoints preserve derivation from stored episodes, but not from external transcripts unless the host wrote them into Stash.
