---
description: "cq review: Mozilla AI plugin, MCP server, SQLite/remote knowledge units, review-gated sharing, and agent-led session reflection"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-06-01"
---

# cq

cq is Mozilla AI's shared agent knowledge commons: a plugin, CLI/MCP server, SDKs, schema package, and optional FastAPI server for storing small "knowledge units" that agents query before acting, propose after discovering a reusable pitfall, and confirm or flag after use. The implemented system is not a general note vault. Its retained artifact is a structured knowledge unit with domain tags, a summary/detail/action triplet, context metadata, confidence signals, tier, and flags.

**Repository:** https://github.com/mozilla-ai/cq

**Reviewed commit:** [36ae42ae4b7c30628133455bde128efe91986235](https://github.com/mozilla-ai/cq/commit/36ae42ae4b7c30628133455bde128efe91986235)

**Last checked:** 2026-06-01

## Core Ideas

**The agent integration is instruction plus MCP tools.** The Claude plugin manifest registers the cq skill, slash commands, and an MCP server launched through `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/bootstrap.py`; the bootstrapper ensures a minimum `cq` binary is available and then execs `cq mcp` ([plugins/cq/.claude-plugin/plugin.json](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/.claude-plugin/plugin.json), [plugins/cq/scripts/bootstrap.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/scripts/bootstrap.py), [plugins/cq/scripts/cq_binary.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/scripts/cq_binary.py)). The MCP server exposes `query`, `propose`, `confirm`, `flag`, and `status`, delegating all storage behavior to the Go SDK client ([cli/mcpserver/server.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/cli/mcpserver/server.go)).

**The skill is the highest-authority local behavior surface.** The skill tells the agent to query before unfamiliar work, apply and verify returned guidance, propose immediately when a non-obvious insight stabilizes, and confirm or flag before finishing ([plugins/cq/skills/cq/SKILL.md](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/skills/cq/SKILL.md)). That prose is a system-definition artifact: it does not merely describe cq, it instructs the consuming agent when to call each tool.

**Knowledge units are deliberately small mixed artifacts.** The schema requires an id, domains, and an `insight` object, with optional language/framework/pattern context, confidence evidence, tier, creator, supersession, and flags ([schema/knowledge_unit.json](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/schema/knowledge_unit.json), [sdk/go/types.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/types.go)). The operative part is prose advice wrapped in symbolic routing and trust metadata. It is meant to change later agent behavior through the `action` field, not through a large recalled transcript.

**Context efficiency comes from tag-first retrieval and bounded result sets.** Query requires at least one domain tag, optionally filters by language/framework/pattern, defaults to five results, and caps at fifty in both MCP and client layers ([cli/mcpserver/query.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/cli/mcpserver/query.go), [sdk/go/client.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/client.go)). The local store combines a normalized domain table with FTS over summary/detail/action, then ranks by relevance times confidence ([sdk/go/store.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/store.go), [sdk/go/scoring.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/scoring.go), [schema/scoring.values.json](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/schema/scoring.values.json)). This keeps volume low, but relevance depends on the agent choosing useful tags.

**Local-first storage can drain to a remote review-gated store.** Without `CQ_ADDR`, proposed units persist in a local SQLite database at the XDG data path, normally `~/.local/share/cq/local.db`; with a remote configured, `propose` sends units to the remote and falls back to local storage on unreachable or auth failures ([sdk/go/options.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/options.go), [sdk/go/client.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/client.go), [sdk/go/remote.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/remote.go)). The MCP command starts a background drain when a remote is present ([cli/cmd/mcp.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/cli/cmd/mcp.go)).

**Remote sharing has a pending/approved boundary.** The server stores proposed KUs with status defaulting to `pending`, exposes review endpoints to approve or reject them, and only returns approved units from `query`, `get`, domain counts, and tier counts ([server/backend/alembic/versions/0001_baseline.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/server/backend/alembic/versions/0001_baseline.py), [server/backend/src/cq_server/repositories/_queries.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/server/backend/src/cq_server/repositories/_queries.py), [server/backend/src/cq_server/api/routes/review.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/server/backend/src/cq_server/api/routes/review.py)). This gives remote KUs stronger governance than local KUs, though the review criteria themselves are outside the query path.

**Session reflection is agent-led, not a server-side transcript miner.** `/cq:reflect` instructs the agent to summarize the current session, identify candidate KUs from errors, tool failures, workarounds, and dead ends, run a VIBE safety check, present candidates to the user, query for duplicates, and call `propose` for approved candidates ([plugins/cq/commands/reflect.md](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/commands/reflect.md)). The Python SDK has a `Reflector` protocol and a default stub that returns guidance rather than performing extraction itself ([sdk/python/src/cq/reflect.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/python/src/cq/reflect.py)).

**Hooks are present but not yet the main read-back mechanism.** The checked-in Claude plugin hook config is empty, while the Cursor hook records failed tool calls into short-lived per-session JSON and prints a failure summary at stop ([plugins/cq/hooks/hooks.json](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/hooks/hooks.json), [plugins/cq/hooks/cursor/cq_cursor_hook.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/hooks/cursor/cq_cursor_hook.py)). That hook may prompt later reflection, but it does not query stored knowledge units or push KUs into the next action.

## Artifact analysis

**Knowledge units.** Storage substrate is local SQLite in the Go SDK and server-side SQL through the FastAPI backend, with remote node discovery and API-key auth when configured. Representational form is mixed: prose `summary`, `detail`, and `action` plus symbolic domains, context, tier, confidence, flags, status, and ids. Lineage is authored or trace-derived depending on whether a human/agent proposed it directly or generated it through `/cq:reflect`; stored lineage is limited to timestamps, creator on the remote, confidence/flag history, and review status, not source transcript offsets. Behavioral authority is advisory knowledge-artifact authority when returned by `query`; it becomes stronger only because the cq skill instructs the agent to verify, apply, confirm, or flag it.

**Skill, slash commands, plugin manifest, and bootstrapper.** Storage substrate is the plugin filesystem bundle. Representational form is prose plus JSON manifest and Python launcher code. Lineage is authored package content, versioned with the repository and release bundle. Behavioral authority is system-definition: the skill instructs when to query/propose/confirm/flag, slash commands shape retrospective review, the manifest wires MCP tools into the host, and the bootstrapper controls which executable actually handles tool calls.

**Local indexes and scoring.** Storage substrate is SQLite tables: the JSON blob table, domain index table, and FTS5 virtual table. Representational form is symbolic/procedural: SQL rows, normalized domains, FTS terms, and scoring constants. Lineage is derived from inserted KUs and regenerated on insert/update; changing KU domains or insight text invalidates the relevant derived rows. Behavioral authority is ranking and routing authority, because it determines which KUs can reach the agent's context under a query.

**Remote review state.** Storage substrate is the server database columns `status`, `reviewed_by`, `reviewed_at`, `created_at`, and `tier`. Representational form is symbolic metadata over the KU JSON. Lineage is server-created and reviewer-updated. Behavioral authority is gating authority: pending and rejected units are retained but excluded from normal query read-back, while approved units become eligible knowledge artifacts for agents.

**Trace-reflection candidates.** Storage substrate before approval is the host agent's current session context and the markdown slash-command flow; cq does not persist raw transcripts in the checked-in implementation. Representational form is prose reasoning by the agent, then mixed KU fields after approval. Lineage is weak unless the agent writes source details into the KU itself. Behavioral authority is candidate knowledge-artifact authority until a user approves and the agent calls `propose`; after storage, it follows the normal KU path.

There is a promotion path, but it mostly changes authority and scope rather than representational form: session experience or local authored advice becomes a KU, a remote KU enters `pending`, a reviewer approves it, and later confirmations/flags adjust confidence. The long-term README and architecture docs discuss broader local/private/public graduation and commons governance, but the code-grounded remote path in this commit is pending-to-approved within the configured remote store ([README.md](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/README.md), [docs/architecture.md](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/docs/architecture.md)).

## Comparison with Our System

| Dimension | cq | Commonplace |
|---|---|---|
| Primary purpose | Share small reusable agent learnings across agents and stores | Maintain a typed methodology KB for agent-operated knowledge bases |
| Canonical artifact | Structured KU with summary/detail/action, tags, context, confidence, tier, flags | Markdown artifacts with frontmatter, type specs, links, indexes, and review state |
| Storage substrate | Local SQLite plus optional remote SQL API; plugin files for instructions | Git-tracked `kb/` collections and generated reports/indexes |
| Retrieval | Agent calls `query` with domain/context tags; ranked bounded JSON results | `rg`, indexes, authored links, skills, validation and review reports |
| Governance | Remote pending/approved/rejected review gate; confidence by confirm/flag | Type contracts, collection rules, validation, semantic review gates, replacement archives |
| Trace-derived learning | Agent-led reflection/propose turns session events into KUs | Source-grounded writing and review workflows; trace-derived promotion is explicit methodology |

cq and Commonplace share the belief that retained agent knowledge needs an activation path. cq makes that path small and tool-shaped: query for a few KUs before acting, act on the `action` field if verified, and update confidence afterward. Commonplace uses larger artifacts and stronger authoring contracts, so it trades cq's low-friction sharing for richer lineage, reviewability, and semantic structure.

The strongest divergence is artifact granularity. A cq KU is intentionally atomic and portable. It can move between local, private, and eventually public stores because it carries a compact schema and little local context. A Commonplace note or review is heavier: it often carries argument structure, citations, outbound links, and collection-specific obligations. That makes it less portable but more reviewable.

The authority split is also different. cq's stored KUs are mostly knowledge artifacts: evidence, hints, or advice returned through a tool. The skill and server policies are the system-definition artifacts that give those KUs operational force. In Commonplace, many retained artifacts are themselves system-definition artifacts: instructions, type specs, validators, ADRs, review gates, and collection contracts can directly constrain future work.

Read-back: pull — stored cq knowledge reaches an agent when the agent or skill-guided workflow deliberately calls `query`; this commit does not implement relevance-gated KU injection into the agent context.

### Borrowable Ideas

**Keep the advice unit small when cross-project portability matters.** Commonplace should not shrink methodology notes into cq-style KUs, but a KU-shaped export could work for operational gotchas discovered during review or validation. Ready as an integration/export idea; not a replacement for library artifacts.

**Separate local capture from shared approval.** cq's local-first fallback plus remote pending queue is a useful promotion pattern. A Commonplace workshop could allow fast local capture of candidate rules, then require review before those rules enter instructions or validation. Ready as a workflow pattern.

**Make confirmation and flagging first-class feedback.** Commonplace has review gates, but not a simple "this remembered guidance helped/hurt in use" signal. cq's `confirm`/`flag` operations suggest a lightweight runtime feedback layer for high-traffic instructions. Needs a concrete consumer before implementation.

**Expose confidence as social evidence, not truth.** The cq skill explicitly warns that confidence counts confirmations, not freshness. Commonplace could use the same distinction if it ever records usage or agreement signals on notes. Ready as wording for any future confidence metadata.

**Use a schema-stable interchange layer.** cq's schema package and Go/Python SDKs make KUs portable across hosts. Commonplace could benefit from a narrow interchange schema for exporting candidate learnings to other agent tools without exposing the whole KB model. Needs a clear external integration.

**Do not import weak lineage into high-authority artifacts.** cq reflection candidates often lack source offsets or durable raw traces. In Commonplace, a cq-like insight should enter a workshop or source-backed note first, not jump straight into an instruction file.

## Trace-derived learning placement

**Trace source.** cq qualifies for trace-derived learning through its implemented agent instructions and `/cq:reflect` command. The raw signal is the current agent session: user requests, assistant reasoning as available to the host, tool calls, errors, failed attempts, workarounds, and final solutions. The Cursor hook can add a short failed-tool summary, but the central trace source is still the agent-visible session context, not a cq-owned transcript database.

**Extraction.** Extraction is agent-led. During normal work, the skill tells the agent to propose immediately when a non-obvious lesson stabilizes. During `/cq:reflect`, the command tells the agent to summarize the session, identify generalizable/non-obvious/actionable/novel candidates, run VIBE safety checks, present candidates to the user, query for near-duplicates, and call `propose` only for approved candidates. The oracle is therefore a mix of agent judgment, user approval, duplicate query, and later remote human review when a remote store is used.

**Scope and timing.** Scope is per-session at extraction time and per-store after persistence: local to one machine/agent environment, private to a configured remote namespace, and public only as a planned or future commons tier. Timing is online mid-task for direct proposes and retrospective at session end for `/cq:reflect`; remote review is staged after proposal.

**Survey placement.** On the [trace-derived learning survey](../trace-derived-learning-techniques-in-related-systems.md), cq belongs in the trace-to-knowledge-unit family rather than trace-to-profile or trace-to-policy. It strengthens the survey distinction between raw traces and durable behavior-shaping artifacts: cq does not keep a transcript memory, but it can turn selected session lessons into compact KUs that later advise agents through query.

**Limits.** The durable artifact does not preserve enough lineage to regenerate the extraction or audit the exact trace slice unless the agent includes that evidence in `detail`. The Python reflector protocol is only a stub in this commit, so there is no implemented server-side extractor, model judge, or transcript store to review for extraction quality.

## Curiosity Pass

**cq is a shared pitfall ledger more than a memory palace.** It does not try to summarize a project, maintain a graph, or build long-context recall. The design bet is that many costly repeated failures can be avoided by a few compact, tagged, action-oriented KUs.

**The skill does much of the product's work.** Without the skill's low threshold for querying and immediate propose discipline, the backend is just a small tagged advice database. The behavior change depends on agents following instruction text.

**`/cq:reflect` is less automatic than the README wording can imply.** The command does not call a server-side reflection tool in this commit. It gives the agent a procedure for mining its visible session and then uses the normal `propose` path.

**The remote read path is stricter than the local path.** Remote query only returns approved units, while local units are queryable after insertion. That asymmetry is sensible, but it means "cq knowledge" has different trust semantics depending on tier.

**Context efficiency depends on tag quality.** The retrieval system bounds result count and ranks by relevance times confidence, but an agent that chooses poor domain tags can miss relevant KUs or retrieve weakly related ones. Precision/recall is not verified from code.

**The hook surface is still early.** Cursor failure capture is useful evidence for reflection, but the checked-in hook does not yet close the loop by querying cq immediately after an error or injecting matching KUs before a retry.

## What to Watch

- Whether `reflect` becomes an actual MCP/server-side extraction tool, and whether it preserves source session lineage, extraction prompts, model versions, and user decisions.
- Whether hooks start performing relevance-gated pre-action or post-error KU retrieval; that would change the read-back classification from pull-only to engineered push activation.
- Whether remote review gains explicit quality, privacy, and generalizability checks beyond pending/approved status.
- Whether public-tier graduation is implemented in code with abstraction, HITL review, provenance, and anti-poisoning controls.
- Whether query ranking adds freshness, review status, flag detail, source diversity, or model-family evidence to avoid treating confirmation count as truth.
- Whether local KUs get a review or expiry mechanism before they accumulate into stale private advice.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: cq turns selected session/tool experience into durable, tagged knowledge units through agent-led reflection and propose flows.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: cq stores KUs, but later behavior changes only when an agent queries and uses returned guidance.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: cq KUs are primarily advisory knowledge artifacts when consumed through query results.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: the cq skill, MCP tool definitions, scoring code, review gate, and plugin manifest instruct, route, rank, or gate behavior.
- [Use trace-derived extraction](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: cq's `/cq:reflect` flow extracts candidate reusable lessons from session traces, with user approval before persistence.
