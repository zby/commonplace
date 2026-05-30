---
description: "Mozilla.ai shared agent knowledge commons with SQLite local/private stores, MCP query/propose/confirm/flag tools, review gates, and prompt-mediated session reflection"
type: ../types/agent-memory-system-review.md
tags: [trace-derived]
status: current
last-checked: "2026-05-16"
---

# cq

`cq` is Mozilla.ai's shared agent knowledge commons: a Claude Code plugin, Go CLI/MCP server, Go and Python SDKs, optional FastAPI server, and review dashboard for compact operational learnings that agents can query before acting. The implemented core is local-first and deliberately small: agents query by domain tags, propose structured knowledge units, confirm guidance that worked, and flag guidance that is wrong or stale. The global commons, decentralized identity layer, guardrail integrations, and privacy-preserving proofs in the architecture document are mostly roadmap-level design at this commit, while the local/private SQLite stores, MCP tools, plugin packaging, sync path, and private review queue are real.

**Repository:** https://github.com/mozilla-ai/cq

**Reviewed revision:** [7fc95f53c4705cbe0e8eb96a4eb620512f266169](https://github.com/mozilla-ai/cq/commit/7fc95f53c4705cbe0e8eb96a4eb620512f266169)

## Core Ideas

**The durable unit is a compact structured lesson.** A knowledge unit is a JSON object with `id`, `domains`, `insight.summary`, `insight.detail`, `insight.action`, optional language/framework/pattern context, evidence fields, tier, flags, and supersession pointer ([`schema/knowledge_unit.json`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/schema/knowledge_unit.json)). The operative part is mixed: prose advice in the insight fields plus symbolic tags, confidence, tier, and flag state. When a future agent reads a result as background guidance, the unit is a knowledge artifact. When the plugin skill tells the agent to query before acting, confirm useful results, and propose new gotchas mid-task, the same unit participates in a system-definition path because the loaded skill gives it behavioral force ([`plugins/cq/skills/cq/SKILL.md`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/plugins/cq/skills/cq/SKILL.md)).

**Local SQLite is the default source of truth, with remote as an optional private tier.** The Go SDK opens a local SQLite database at the XDG data path (`~/.local/share/cq/local.db` by default), creates `knowledge_units`, a domain index, an FTS5 virtual table, and writer metadata, and applies WAL/busy-timeout pragmas ([`sdk/go/options.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/sdk/go/options.go), [`sdk/go/store.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/sdk/go/store.go)). If `CQ_ADDR` is configured, `propose` tries the remote API first; on transport, 5xx, 401, or 403 failure it stores the unit locally as `local` and returns a fallback error so the caller can report partial success ([`sdk/go/client.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/sdk/go/client.go)). The MCP command starts a background `Drain` on launch, pushing local units to the remote and deleting them locally after successful push ([`cli/cmd/mcp.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/cli/cmd/mcp.go), [`cli/cmd/drain.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/cli/cmd/drain.go)).

**The agent-facing surface is MCP plus prompt packaging, not a custom agent runtime.** The MCP server exposes exactly five tools: `query`, `propose`, `confirm`, `flag`, and `status` ([`cli/mcpserver/server.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/cli/mcpserver/server.go), [`cli/mcpserver/query.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/cli/mcpserver/query.go), [`cli/mcpserver/propose.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/cli/mcpserver/propose.go)). The Claude plugin manifest wires a Python bootstrap script that ensures a cached `cq` binary exists, then `exec`s `cq mcp` over stdio ([`plugins/cq/.claude-plugin/plugin.json`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/plugins/cq/.claude-plugin/plugin.json), [`plugins/cq/scripts/bootstrap.py`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/plugins/cq/scripts/bootstrap.py)). Non-Claude hosts are installer targets rather than separate implementations; for example, the OpenCode adapter copies skills/commands and writes MCP config pointing at the shared binary ([`scripts/install/src/cq_install/hosts/opencode.py`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/scripts/install/src/cq_install/hosts/opencode.py)).

**Retrieval is tag-first with confidence-weighted ranking.** Local query requires domains, searches both the normalized domain table and FTS phrases over summary/detail/action, then ranks by relevance times confidence ([`sdk/go/store.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/sdk/go/store.go)). Relevance is a weighted score: domain Jaccard plus language/framework/pattern matches, using constants from the shared schema package ([`sdk/go/scoring.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/sdk/go/scoring.go), [`schema/scoring.values.json`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/schema/scoring.values.json)). Remote query returns only approved private units, then the SDK merges local and remote results with local results winning ID conflicts ([`sdk/go/client.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/sdk/go/client.go), [`server/backend/src/cq_server/repositories/_queries.py`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/server/backend/src/cq_server/repositories/_queries.py)).

**The private/team tier has a real approval gate.** The FastAPI server runs Alembic migrations into a SQLite schema whose `knowledge_units.status` defaults to `pending`; approved units are the only ones exposed by normal query/get paths ([`server/backend/alembic/versions/0001_baseline.py`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/server/backend/alembic/versions/0001_baseline.py), [`server/backend/src/cq_server/repositories/knowledge.py`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/server/backend/src/cq_server/repositories/knowledge.py)). Review endpoints expose pending queue, approve/reject decisions, filtered listing, and review stats, and the React SPA routes users to review, dashboard, and API-key pages ([`server/backend/src/cq_server/api/routes/review.py`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/server/backend/src/cq_server/api/routes/review.py), [`server/backend/src/cq_server/services/reviews.py`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/server/backend/src/cq_server/services/reviews.py), [`server/frontend/src/App.tsx`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/server/frontend/src/App.tsx)). This gives shared knowledge stronger authority than local hints: a private unit becomes query-visible only after a human reviewer approves it.

**The trust story is partly implemented and partly aspirational.** Confirmation and flagging are implemented as simple confidence updates: confirmation adds 0.1, flags subtract 0.15, and duplicate flags require a target in the SDK path ([`sdk/go/scoring.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/sdk/go/scoring.go), [`sdk/go/client.go`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/sdk/go/client.go)). The architecture document describes KERI identity, anti-poisoning, PII filtering, retrieval-time warnings, global graduation, and zero-knowledge privacy as system layers, but the inspected propose/query paths do not call a guardrail engine or identity system ([`docs/architecture.md`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/docs/architecture.md)). For this revision, the real trust mechanisms are human review, tags, confidence arithmetic, flags, API-key auth, and the local/private tier split.

## Comparison with Our System

| Dimension | cq | Commonplace |
|---|---|---|
| Primary purpose | Share compact operational gotchas across agents and teams | Maintain a typed, navigable methodology KB for agents and humans |
| Storage substrate | SQLite local store plus optional FastAPI SQLite private store | Markdown files in git, generated indexes, validation artifacts |
| Retained unit | JSON knowledge unit: summary/detail/action, tags, confidence, flags | Typed notes, reviews, instructions, ADRs, indexes, workshop docs |
| Agent activation | Loaded skill instructs query/propose/confirm/flag at task points | AGENTS instructions, skills, indexes, links, validation, review bundles |
| Sharing boundary | Local capture, drain to private server, human approval before query visibility | Git/review workflow and curated/indexed file publication |
| Retrieval | Domain tags, optional context filters, local FTS, confidence-weighted ranking | `rg`, frontmatter descriptions, directory indexes, authored links |
| Governance | Review queue, API keys, confidence boosts/penalties, flags | Structural validation, semantic review, link contracts, editorial review |
| Artifact authority | Advice becomes action-shaping through the skill protocol | Authority split across knowledge artifacts and system-definition artifacts |

cq is stronger than commonplace at lightweight cross-agent operational memory. Its capture path is cheap, its plugin surface is practical, and its local-first fallback avoids losing a useful gotcha just because the remote service is down. Commonplace has no similarly productized shared pitfall store.

Commonplace is stronger at explanation, lineage, and durable knowledge structure. A cq knowledge unit can tell an agent what to do, but it does not preserve source excerpts, derivation rationale, related claims, supersession history beyond a single pointer, or enough context for deep review. That is a good trade for short "avoid this mistake" advice. It is a weak substrate for methodological knowledge that needs synthesis, argument, and cross-note navigation.

The cleanest vocabulary split is behavioral authority. A cq unit stored in SQLite is a knowledge artifact by default: evidence or advice a future agent may consider. The cq skill, command prompts, and MCP tool policy are system-definition artifacts: they instruct when to query, when to trust cautiously, when to confirm, when to flag, and when to propose. cq's strongest design move is packaging those two surfaces together without pretending the database alone changes behavior.

## Borrowable Ideas

**Local-first capture with drain-on-reconnect.** Ready to borrow if commonplace ever gets a shared operational-memory service. cq's remote fallback and startup drain keep capture available under bad network/auth conditions without silently dropping candidate knowledge.

**Approval gates at the sharing boundary.** Ready to borrow as a principle. cq lets local capture be cheap but requires review before private/team query visibility. That is a better default than either blocking capture on review or sharing every candidate immediately.

**A compact action-shaped unit for repeated pitfalls.** Useful, but only for a narrower artifact family than commonplace notes. A `summary/detail/action` unit could live in a workshop or operations layer for common tool/API gotchas, while richer methodology claims should still become normal notes.

**Confidence as a weak social signal.** Worth borrowing only if we keep it explicitly weak. Confirmation and flag counts can rank hints, but they should not replace source evidence, timestamps, or review. cq's own skill says confidence is not a freshness guarantee.

**Ship the behavior policy with the tool.** Ready to borrow for future MCP wrappers around `commonplace-*` commands. cq does not just expose `query`; it installs skill text that tells the agent when to query, how to present results, and how to update the commons afterward. The prompt policy is part of the product.

**Do not borrow shallow units as a universal memory substrate.** cq is intentionally optimized for operational lessons. For commonplace, short action units should feed notes, instructions, skills, validators, or scripts only when the lesson proves durable enough to deserve stronger authority.

## Trace-derived learning placement

**Trace source.** cq qualifies narrowly because `/cq:reflect` is an implemented plugin command that asks the agent to mine the current session conversation for shareable learnings, including errors, tool failures, workarounds, configuration decisions, and dead ends ([`plugins/cq/commands/reflect.md`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/plugins/cq/commands/reflect.md)). The ordinary `propose` and `confirm` loop is manual social curation; it is not by itself trace-derived learning.

**Extraction.** Extraction is prompt-mediated and human-gated. The command instructs the agent to summarize the session, identify generalizable/non-obvious/actionable/novel candidates, run a VIBE safety check, present candidates for approval/edit/skip, then call `propose` for approved candidates. There is no dedicated `reflect` MCP tool and no server-side transcript miner; the oracle is the acting agent plus the user approval step.

**Storage substrate.** The source trace is the active agent session context, not a retained raw transcript inside cq. Distilled candidates become normal knowledge units in the local SQLite store or private remote store through the same `propose` path as manual submissions.

**Representational form.** The raw trace is mixed conversation/tool context. The distilled artifact is prose plus symbolic metadata: summary/detail/action, domains, optional language/framework/pattern, confidence, tier, and flags. No inspected path updates embeddings, ranker weights, or model parameters.

**Lineage.** Lineage is weak. The proposed unit can include timestamp/source detail in prose if the agent writes it, but the schema does not record session ID, source transcript pointer, extraction prompt version, approval edits, or raw evidence snippets. The Cursor hook records a last tool failure in temporary per-session JSON and prints a summary on stop, but it does not write knowledge units itself ([`plugins/cq/hooks/cursor/cq_cursor_hook.py`](https://github.com/mozilla-ai/cq/blob/7fc95f53c4705cbe0e8eb96a4eb620512f266169/plugins/cq/hooks/cursor/cq_cursor_hook.py)).

**Behavioral authority.** The session trace is source evidence. The proposed knowledge unit is a knowledge artifact while stored and retrieved as advice. It gains system-definition influence only because the installed skill instructs future agents to query before acting and to use `insight.action` as a starting point while verifying it.

**Scope and timing.** Scope is per agent session at extraction time, then local or private/team after proposal and review. Timing is staged and user-triggered: `/cq:reflect` runs at session end as a backstop, while the primary skill protocol prefers immediate `propose` during work.

**Survey placement.** On the [trace-derived survey](../trace-derived-learning-techniques-in-related-systems.md), cq belongs in the lightest readable-artifact branch: session conversation can become short operational advice through an agent/user review prompt. It strengthens the survey distinction between trace-derived learning and manual curation because both paths converge on the same knowledge-unit schema, but only the reflect command consumes a trace.

## Curiosity Pass

**The strongest product idea is not retrieval.** Tag plus FTS search is ordinary. The distinctive property is the social loop: query before acting, propose immediately after non-obvious learning, confirm useful guidance, flag bad guidance, and review before team visibility. cq is a behavior protocol wrapped around a small database.

**The docs are more ambitious than the running trust stack.** The architecture diagrams are useful for intent, but KERI identity, anti-poisoning, global graduation, guardrail checks, vendor-bias signals, and privacy proofs should not be treated as implemented mechanisms at this revision. The review should track the code path, not the diagram.

**The private review queue improves legitimacy, not depth.** Reviewers can approve, reject, and filter units, but the reviewed artifact is still a short tip. The system cannot support source-grounded adjudication unless the unit itself carries better evidence and lineage.

**Reflection is real but deliberately soft.** `/cq:reflect` is a prompt workflow over session context, not an automatic miner. That is probably the right 0.x stance: it lowers capture loss without granting unreviewed session summaries automatic team authority.

**The local/private/public vocabulary is slightly ahead of deployment.** The code has tier values for `local`, `private`, and `public`, and status text explains public as an open commons, but the implemented remote server is private/team-scoped. Public commons behavior remains future work.

## What to Watch

- Whether proposed guardrails become actual calls in the `propose`, review, and query paths rather than architecture-document layers.
- Whether knowledge units gain source evidence, extraction provenance, review comments, staleness policy, and richer supersession beyond the current fields.
- Whether `/cq:reflect` becomes a real trace-ingestion tool or remains an agent prompt that calls ordinary `propose`.
- Whether private/team SQLite grows into the documented hosted production shape, including multi-tenant posture and stronger RBAC.
- Whether confidence scoring remains simple arithmetic or starts incorporating reviewer decisions, independent confirmations, model-family diversity, and retrieval outcomes.

---

Relevant Notes:

- [Agent memory needs discoverable, composable, trusted knowledge under bounded context](../../notes/agent-memory-needs-discoverable-composable-trusted-knowledge-under.md) - supports: cq optimizes the "trusted enough to avoid repeating a mistake" slice of agent memory, but with shallow composability.
- [Activate behavior-changing memory](../../notes/agent-memory-requirements/activate-behavior-changing-memory.md) - exemplifies: cq matters because the skill loads the query/update protocol before the next agent acts.
- [Make authority explicit](../../notes/agent-memory-requirements/make-authority-explicit.md) - exemplifies: cq separates local advice, private approved guidance, and prompt-level instructions, even though its unit schema stays compact.
- [Use trace-derived extraction as meta-learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - qualifies narrowly: `/cq:reflect` turns session context into candidate knowledge units, with user approval and weak lineage.
- [The boundary of automation is the boundary of verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) - grounds: cq's review gate is necessary because proposed shared guidance is not automatically verifiable.
- [Gnosis](./gnosis.md) - compares-with: both use compact repo/tooling memory for coding agents, but cq is shared-service oriented while Gnosis is repo-local why-memory.
