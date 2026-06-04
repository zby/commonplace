---
description: "Stash review: Go MCP memory server with pgvector episodes, consolidated facts, relationships, goals, failures, hypotheses, and agent-mediated recall"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-02"
---

# Stash

Stash, from alash3al, is a self-hosted Go memory server for MCP-compatible agents. At the reviewed commit it stores raw episode memories in PostgreSQL with pgvector embeddings, consolidates those episodes into facts, relationships, causal links, contradictions, patterns, goal annotations, failure patterns, and hypothesis updates, and exposes the system through CLI and MCP SSE/stdio tools. Its cloud service is described as a separate codebase, so this review covers only the open-source repository.

**Repository:** https://github.com/alash3al/stash

**Reviewed commit:** [93601c1f4e0fb42df99d2de33567095020fb6d7e](https://github.com/alash3al/stash/commit/93601c1f4e0fb42df99d2de33567095020fb6d7e)

**Last checked:** 2026-06-02

## Core Ideas

**The write unit is an embedded episode.** `Remember()` validates content and namespace path, resolves the namespace, embeds the content, and inserts an `episodes` row with `content`, `embedding`, `embedding_model`, and `occurred_at` ([internal/brain/episode.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/episode.go), [internal/db/migrations/00004_create_episodes.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00004_create_episodes.sql)). Episodes are append-style raw observations with soft delete and hard purge APIs, not edited notes.

**Consolidation turns episodes into several higher-order artifacts.** `ConsolidateByID()` reads per-namespace checkpoints and runs staged extraction from episodes to facts, facts to relationships, facts to causal links, goal progress annotations, failure pattern detection, facts/relationships to patterns, hypothesis evidence scanning, and confidence decay ([internal/brain/consolidate.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/consolidate.go)). Checkpoints only advance after successful stage processing, so the pipeline is incremental rather than reprocessing the full database each run.

**The fact layer is structured enough to govern freshness.** Consolidated facts carry prose content, embeddings, confidence, optional `entity` / `property` / `value`, validity windows, source episode links, and soft delete state ([internal/models/models.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/models/models.go), [internal/db/migrations/00005_create_facts.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00005_create_facts.sql), [internal/db/migrations/00006_create_fact_sources.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00006_create_fact_sources.sql)). Contradiction detection compares new and existing facts with the same entity/property, records unresolved contradictions, and can auto-supersede old facts on high-confidence replacement classifications ([internal/brain/contradiction.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/contradiction.go)).

**Recall is fact-first semantic search with bounded fallback to episodes.** `Recall()` embeds the query, resolves namespace paths including descendants, searches consolidated facts up to the requested limit, then fills remaining slots from episode search, sorts by score, and caps the returned list to `limit` with a hard maximum of 100 ([internal/brain/recall.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/recall.go), [internal/queries/recall.sql.tmpl](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/queries/recall.sql.tmpl)). Context efficiency is therefore retrieval-time selection: namespaces, vector similarity, fact-before-episode ordering, pagination limits, and separate query tools for facts, relationships, causal chains, goals, failures, and hypotheses. There is no token budget, progressive disclosure tree, or prompt-size measurement in the reviewed code.

**MCP tool descriptions carry an opinionated operating protocol.** The server description tells the agent to initialize first, recall before answering history-sensitive questions, store durable signal proactively, consolidate periodically, and use different tools for raw search, verified facts, relationships, goals, failures, and context ([cmd/cli/mcp.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/cmd/cli/mcp.go), [cmd/cli/mcp_prompts.tmpl](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/cmd/cli/mcp_prompts.tmpl)). This is an adoption affordance and a system-definition layer: the tool surface teaches agents how to use the memory store without changing the host agent's code.

**Working context, goals, failures, and hypotheses are separate memory channels.** Stash distinguishes short-lived context rows from durable episodes/facts, durable goals from ordinary memories, failures from generic notes, and hypotheses from confirmed facts ([internal/brain/context.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/context.go), [internal/brain/goal.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/goal.go), [internal/brain/failure.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/failure.go), [internal/brain/hypothesis.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/hypothesis.go)). The split is useful because each channel has different authority: context resumes active work, goals track intended outcomes, failures carry anti-repeat lessons, and hypotheses stay uncertain until tested or confirmed.

## Artifact analysis

- **Storage substrate:** `rdbms` — PostgreSQL `episodes` rows with pgvector embeddings and namespace foreign keys
- **Representational form:** `prose` `symbolic` `parametric` — Prose observations and facts, symbolic timestamps/namespaces/status fields/prompts/tool schemas, and distributed-parametric embeddings
- **Lineage:** `authored` `trace-extracted` — authored system-definition artifacts and explicit context/goals/failures sit beside agent-mediated session observations and LLM-derived consolidation outputs
- **Behavioral authority:** `knowledge` `instruction` `routing` `validation` `ranking` `learning` — recalled rows advise as knowledge; MCP prompts instruct; namespaces/tool channels route; confidence/contradiction/status logic validates; embeddings and fact-first recall rank; consolidation learns derived records

**Episode rows.** Storage substrate: PostgreSQL `episodes` rows with pgvector embeddings and namespace foreign keys. Representational form: prose observation plus symbolic timestamps, namespace ids, embedding model metadata, and distributed-parametric vectors. Lineage: agent- or caller-submitted observations from a session, project, user preference, decision, failure, or summary; Stash records the submitted text and timestamp, but not the full surrounding transcript, exact source span, or acceptance review. Behavioral authority: knowledge artifacts when recalled as evidence or context; ranking artifacts through embedding similarity.

**Consolidated facts and fact sources.** Storage substrate: PostgreSQL `facts` and `fact_sources`, with embeddings, confidence, optional structured fields, validity windows, and source episode links. Representational form: prose fact, symbolic entity/property/value metadata, confidence, validity, source ids, and distributed-parametric vectors. Lineage: LLM-derived from clustered episodes through `ReasonStructured()`, deduplicated by vector similarity, and linked back to source episode ids. Behavioral authority: knowledge artifacts when queried or recalled; system-definition authority appears in validity windows, confidence decay, contradiction resolution, and the fact-before-episode recall policy.

**Relationships, causal links, contradictions, patterns, goals, failures, and hypotheses.** Storage substrate: PostgreSQL tables for each retained object. Representational form: mostly symbolic records with prose payloads, confidence/status fields, source fact ids, and lifecycle state. Lineage: authored directly through tools in some cases, or derived during consolidation from facts, relationships, failures, goals, and hypotheses. Behavioral authority: advisory knowledge when listed or searched; stronger workflow authority when a goal's status, a failure's lesson, a contradiction's resolution, or a hypothesis transition changes what a future agent should attempt.

**Working context rows.** Storage substrate: PostgreSQL `contexts`, one row per namespace with focus text and expiry. Representational form: prose focus plus symbolic TTL. Lineage: explicitly set by the agent or caller for a resumable work stream, not derived by consolidation. Behavioral authority: temporary handoff context when an agent explicitly calls `get_context`; it is not durable knowledge and expires by design.

**Consolidation checkpoints, prompts, thresholds, and reasoner interfaces.** Storage substrate: repository source, embedded SQL templates, prompt/tool-description templates, environment configuration, and `consolidation_progress` rows. Representational form: symbolic code, SQL, thresholds, model configuration, and prose prompts. Lineage: authored system-definition artifacts. Behavioral authority: extraction, batching, ranking, scheduling, validation, and governance authority over which raw observations become higher-order memory and which stages are considered current.

**MCP and CLI tools.** Storage substrate: Go command source and embedded MCP prompt templates. Representational form: symbolic tool schemas plus prose usage contracts. Lineage: authored integration layer over the brain package. Behavioral authority: system-definition artifact for host agents: it tells them when to initialize, recall, remember, consolidate, and separate raw memory from facts, context, goals, failures, and hypotheses. Effective compliance is not proven by code; a host agent can still ignore tool descriptions.

Promotion path: Stash has a real promotion path from agent-selected session observation to episode, episode cluster to fact, fact to relationship/causal link/pattern/goal annotation/failure pattern/hypothesis update, and hypothesis confirmation to fact. It does not have a reviewed promotion gate that turns derived facts into high-authority instructions, validators, skills, or repository artifacts.

## Comparison with Our System

| Dimension | Stash | Commonplace |
|---|---|---|
| Primary purpose | Runtime MCP memory service for agents | Git-native methodology KB for agent-operated knowledge bases |
| Canonical artifact | Episode rows and consolidated database records | Typed Markdown notes, reviews, instructions, ADRs, sources, indexes |
| Storage substrate | PostgreSQL, pgvector, migrations, embedded prompts, MCP/CLI code | Repository files plus generated indexes, validation outputs, and review reports |
| Write path | Agent/caller tool calls plus background/manual consolidation | Authored artifacts, source snapshots, explicit review and validation |
| Retrieval | Semantic recall, fact listing, relationship/causal/goal/failure/hypothesis tools | `rg`, frontmatter descriptions, indexes, links, skills, validation/review runs |
| Governance | Namespaces, soft deletes, fact confidence, source ids, contradiction handling, status transitions, decay | Collection contracts, type specs, git diffs, validators, semantic gates, archives |
| Activation | MCP/CLI pull tools plus tool-description protocol | Mostly explicit pull through local search, indexes, links, and loaded instructions |

Stash is stronger as a runtime memory appliance. It packages database migrations, pgvector indexes, embedding cache, a Docker Compose setup, MCP SSE/stdio serving, and a domain-specific tool surface. Commonplace is stronger as a durable authored knowledge system: every artifact is inspectable as a file, citations are explicit, type contracts are local, and promotion into instruction or validation authority is reviewable through git.

The largest design difference is admission and authority. Stash makes it cheap for an agent to remember and consolidate session observations, but the accepting agent decides what to store and the LLM reasoner decides what to extract. Commonplace is slower and heavier because durable methodology claims are authored, cited, validated, and reviewed before gaining authority.

**Read-back:** `pull` — Agents or users call MCP/CLI tools such as `recall`, `query_facts`, `query_relationships`, `get_context`, `list_goals`, `list_failures`, and `list_hypotheses`; the MCP prompt strongly instructs agents to call those tools before history-sensitive answers, but I did not find a code-grounded relevance-gated pre-action injection path for stored memory content, so `push-activation` is not warranted

### Borrowable Ideas

**Separate raw episodes from consolidated facts.** Ready now as vocabulary. Commonplace already separates sources, notes, and generated indexes, but Stash's episode/fact split is a clean reminder that raw traces and distilled claims need different trust labels and read paths.

**Use namespace-scoped working context as an expiring handoff.** Needs a concrete workflow. A Commonplace workshop could have short-lived focus records that expire independently of durable notes, preventing "current task" text from being mistaken for retained methodology.

**Keep failure lessons as first-class anti-repeat artifacts.** Ready for workshop use. Stash's failure record requires what failed, why, and the lesson. Commonplace review or migration work could use that shape before deciding whether a lesson deserves promotion into an instruction.

**Preserve source ids for derived facts, but add stronger lineage.** Ready as a constraint. Stash links facts to source episode ids; Commonplace should keep exact source snapshots, quote anchors, review run ids, or trace spans when any derived note could affect future behavior.

**Do not borrow automatic consolidation as direct instruction promotion.** Ready as a caution. Stash's consolidation is useful for advisory memory, but Commonplace should not let clustered session traces become instructions, validators, or routing rules without review.

**Make tool descriptions teach memory hygiene.** Ready now. Stash's MCP prompt is unusually explicit about when to recall, remember, consolidate, and avoid noise. Commonplace skills and commands should carry similarly operational descriptions, while still relying on validation for high-authority artifacts.

## Trace-derived learning placement

- **Trace source:** `session-logs` — agent-mediated session observations, summaries, decisions, corrections, failures, and completed-work notes submitted through `remember`
- **Learning scope:** `per-project` `cross-task` — namespace paths scope recall and consolidation, while user preferences, goals, failures, and project facts can carry across future tasks
- **Learning timing:** `online` `staged` — capture happens at agent/caller tool-call time, while consolidation runs manually or periodically through checkpointed stages
- **Distilled form:** `prose` `symbolic` `parametric` — facts and summaries remain prose, relationships/status fields/prompts are symbolic, and embeddings support retrieval and deduplication

**Trace source.** Stash qualifies as trace-derived under the current rule, but the trace capture is agent-mediated rather than passive. The raw trace entering the system is whatever an agent or caller submits through `remember`: user preferences, project facts, decisions, corrections, completed work, session summaries, failures, and similar observations. The MCP prompt explicitly instructs agents to store durable signal proactively and at session end; the code then stores those submissions as episode rows ([cmd/cli/mcp_prompts.tmpl](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/cmd/cli/mcp_prompts.tmpl), [cmd/cli/mcp.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/cmd/cli/mcp.go)).

**Extraction.** Consolidation clusters new episodes by embedding similarity, asks the reasoner for structured facts, embeds fact summaries, deduplicates by vector similarity, records fact sources, detects contradictions, extracts relationships and causal links, annotates active goals from new facts, detects repeated failures and failure patterns, extracts patterns from facts and relationships, and updates or confirms/rejects hypotheses from evidence ([internal/brain/consolidate.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/consolidate.go), [internal/reasoner/reasoner.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/reasoner/reasoner.go), [internal/brain/consolidate_failure.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/consolidate_failure.go), [internal/brain/consolidate_goal.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/consolidate_goal.go), [internal/brain/consolidate_hypothesis.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/brain/consolidate_hypothesis.go)). The oracle is mostly the configured LLM reasoner plus thresholds for deduplication, contradiction auto-supersession, hypothesis confirmation/rejection, and confidence decay; there is no human review gate before derived facts become queryable.

**Four fields.** The raw stage is episode records: PostgreSQL plus pgvector, prose plus embeddings, agent-submitted trace lineage, and advisory knowledge authority when recalled. The distilled stage is facts, relationships, causal links, contradictions, patterns, goal notes, failure pattern facts, and hypothesis status: PostgreSQL symbolic/prose records with embeddings where relevant, LLM-derived lineage from episodes/facts/failures, and advisory or workflow authority depending on the consumer.

**Scope and timing.** Scope is namespace-based, with namespace paths including descendants for read operations. Capture is per agent/caller tool call. Consolidation can be manual through the `consolidate` tool or CLI, or periodic when the MCP server is started with `--with-consolidation`; each stage processes only records beyond its checkpoint ([cmd/cli/mcp.go](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/cmd/cli/mcp.go), [internal/db/migrations/00010_create_consolidation_progress.sql](https://github.com/alash3al/stash/blob/93601c1f4e0fb42df99d2de33567095020fb6d7e/internal/db/migrations/00010_create_consolidation_progress.sql)).

**Survey placement.** Stash belongs in the service-owned trace backend family, with an agent-mediated capture boundary. On the artifact/weights axis it is symbolic-artifact learning with vector retrieval support, not model-weight learning. It strengthens the survey's distinction between raw trace retention and distilled behavior-shaping artifacts: Stash has separate rows for episodes, facts, context, failures, goals, hypotheses, and consolidation progress, but the path from distilled artifact to future behavior still depends on agents calling pull tools.

## Curiosity Pass

**The README's "patterns become wisdom" story is implemented as database records, not a governed knowledge ladder.** Patterns, contradictions, goals, failures, and hypotheses exist in code, but they remain service records unless a host agent reads and applies them.

**The MCP prompt is almost as important as the database.** Stash does not only expose `remember` and `recall`; it ships an operating contract telling the agent when memory is mandatory. That prompt is a behavior-shaping artifact even though it is not remembered user knowledge.

**Fact-first recall is a useful maturity marker.** The system prefers consolidated facts and only spends remaining slots on raw episodes. That reduces context noise when consolidation is healthy, but stale or low-quality consolidation can hide useful raw traces behind confident summaries.

**Agent-mediated capture is both safer and weaker than automatic transcript capture.** Stash avoids silently logging everything, but it relies on the agent to notice durable signal and call `remember`. The code cannot prove that important session traces will actually be captured.

**The context table is deliberately not memory.** Expiring working focus is a good separate channel. It prevents a resumable task note from becoming a permanent fact, but only if agents follow the tool descriptions.

## What to Watch

- Whether Stash adds host integrations that automatically call recall before model invocation with a relevance signal and token budget; that would reopen the `push-activation` decision.
- Whether consolidated facts gain review state, source quote spans, or acceptance decisions; without them, derived facts are useful but weakly governed.
- Whether pattern, goal, failure, and hypothesis outputs become prompt-ready bundles rather than separate pull tools; that would raise their behavioral authority.
- Whether benchmarks measure downstream with/without-memory behavior, not only storage, recall, or consolidation correctness.
- Whether namespaces gain migration, merge, or alias workflows; namespace drift is the obvious failure mode for long-running memory stores.
- Whether the cloud product's separate implementation feeds design changes back into this repository, since the README explicitly says the feature sets differ.

## Bottom Line

Stash is a real MCP memory server with agent-mediated trace capture, PostgreSQL/pgvector storage, staged LLM consolidation, semantic recall, and a strong tool-description protocol. Its best lesson for Commonplace is the separation between raw episodes, consolidated facts, short-lived context, failures, goals, and hypotheses. Its main boundary is activation and governance: stored memory changes behavior only when an agent pulls and trusts it, and derived facts do not pass through the kind of citation and review ladder Commonplace needs for methodology artifacts.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - places: Stash turns agent-selected session observations into episodes, facts, relationships, patterns, and workflow state.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: Stash stores and consolidates memory, but stored content reaches behavior through explicit tool use.
- [Axes of artifact analysis](../../notes/axes-of-artifact-analysis.md) - applies: episodes, facts, vectors, relationships, goals, failures, hypotheses, context rows, and MCP prompts have different substrate/form/lineage/authority profiles.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - classifies: episodes, recalled facts, relationships, causal chains, and patterns mostly advise as evidence or context.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - classifies: MCP tool descriptions, consolidation code, prompts, thresholds, SQL templates, and status transitions constrain future behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies with caveat: Stash derives durable artifacts from agent-submitted traces, but capture itself is not automatic transcript logging.
