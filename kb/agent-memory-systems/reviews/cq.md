---
description: "cq review: Mozilla AI plugin and MCP store for structured agent knowledge units, review-gated sharing, and agent-led reflection"
type: ../types/agent-memory-system-review.md
source-tier: code-grounded
tags: [trace-derived]
last-checked: "2026-06-04"
---

# cq

cq, by Mozilla AI, is a shared knowledge commons for coding agents. At the reviewed commit it ships a Claude Code plugin, skill and slash commands, a Go CLI/MCP server, Go and Python SDKs, JSON schemas, and an optional FastAPI server. Its durable unit is not a project note or transcript: it is a small structured knowledge unit with domain tags, summary/detail/action prose, optional language/framework/pattern context, confidence evidence, tier, creator, supersession, and flags.

**Repository:** https://github.com/mozilla-ai/cq

**Reviewed commit:** [36ae42ae4b7c30628133455bde128efe91986235](https://github.com/mozilla-ai/cq/commit/36ae42ae4b7c30628133455bde128efe91986235)

**Last checked:** 2026-06-04

## Core Ideas

**The host integration is instruction plus MCP tools.** The Claude plugin manifest registers a skill directory, slash commands, and an MCP server launched by `python3 ${CLAUDE_PLUGIN_ROOT}/scripts/bootstrap.py`; the bootstrapper resolves a usable `cq` binary and execs `cq mcp` ([plugins/cq/.claude-plugin/plugin.json](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/.claude-plugin/plugin.json), [plugins/cq/scripts/bootstrap.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/scripts/bootstrap.py), [cli/cmd/mcp.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/cli/cmd/mcp.go)). The MCP server exposes five tools, `query`, `propose`, `confirm`, `flag`, and `status`, and delegates storage behavior to the Go SDK client ([cli/mcpserver/server.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/cli/mcpserver/server.go)).

**The skill is the strongest behavior surface.** `SKILL.md` tells the agent to query at task starts and before unfamiliar/error-prone work, apply returned `action` guidance only after verification, propose immediately when a non-obvious lesson stabilizes, and confirm or flag guidance before finishing ([plugins/cq/skills/cq/SKILL.md](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/skills/cq/SKILL.md)). That prose is a system-definition artifact: the store holds advice, but the skill gives the advice an operational protocol.

**Knowledge units are compact mixed artifacts.** The schema requires an id, domains, and an `insight` object with `summary`, `detail`, and `action`; it also supports context, evidence/confidence, tier, creator, supersession, and flags ([schema/knowledge_unit.json](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/schema/knowledge_unit.json), [sdk/go/types.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/types.go)). The operative part is prose advice wrapped in symbolic routing and trust metadata.

**Context efficiency comes from tag-first retrieval and bounded results.** Query requires domain tags, optionally filters by language/framework/pattern, defaults to five results, and caps at fifty in both the MCP handler and client layer ([cli/mcpserver/query.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/cli/mcpserver/query.go), [sdk/go/client.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/client.go)). The local store combines normalized domain rows with FTS over summary/detail/action, then ranks by relevance times confidence ([sdk/go/store.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/store.go), [sdk/go/scoring.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/scoring.go)). This keeps retrieved context small, but the system depends on the agent choosing useful tags.

**Local-first storage can drain to a remote review-gated store.** Without `CQ_ADDR`, proposals persist in local SQLite; with a remote configured, `propose` sends the unit to the remote and falls back to local storage on unreachable or auth failures ([sdk/go/client.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/client.go), [sdk/go/options.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/go/options.go)). The MCP command starts a background drain on startup when a remote exists, and the README now documents both self-hosted servers and Mozilla's hosted `cq.exchange` option ([cli/cmd/mcp.go](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/cli/cmd/mcp.go), [README.md](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/README.md)).

**Remote sharing has a pending/approved boundary.** The server migration stores each KU with `status` defaulting to `pending`; review endpoints approve or reject units; normal remote query/get/count paths operate on approved units ([server/backend/alembic/versions/0001_baseline.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/server/backend/alembic/versions/0001_baseline.py), [server/backend/src/cq_server/api/routes/review.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/server/backend/src/cq_server/api/routes/review.py), [server/backend/src/cq_server/repositories/_queries.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/server/backend/src/cq_server/repositories/_queries.py), [server/backend/src/cq_server/repositories/knowledge.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/server/backend/src/cq_server/repositories/knowledge.py)).

**Reflection is agent-led, not a transcript-mining service.** `/cq:reflect` tells the agent to summarize the session, identify generalizable/non-obvious/actionable/novel lessons, run VIBE safety checks, present candidates to the user, query for duplicates, and call `propose` for approved candidates ([plugins/cq/commands/reflect.md](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/commands/reflect.md)). The Python SDK `DefaultReflector` is a stub that returns guidance rather than extracting candidates itself ([sdk/python/src/cq/reflect.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/sdk/python/src/cq/reflect.py)).

## Artifact analysis

- **Storage substrate:** `sqlite` — Local KUs live in SQLite through the Go SDK, remote KUs live behind the FastAPI server's SQL repository, and the plugin/skill/command definitions live as shipped files in the plugin bundle.
- **Representational form:** `prose` `symbolic` — KU `summary`, `detail`, and `action` are prose; domains, context fields, ids, tiers, confidence values, flags, statuses, JSON schemas, MCP tool schemas, SQL indexes, and scoring rules are symbolic. I did not find embedding/vector indexes or model-weight updates in the implemented read path.
- **Lineage:** `authored` `trace-extracted` — KUs can be authored directly by an agent/user through `propose`; `/cq:reflect` and the skill's mid-task propose rule derive candidates from the current agent-visible session. Domain indexes, FTS rows, stats, confidence, flags, and review state are derived from stored KUs and subsequent tool/reviewer actions.
- **Behavioral authority:** `knowledge` `instruction` `enforcement` `routing` `validation` `ranking` `learning` — KUs advise as knowledge; the skill and slash commands instruct the host agent; review status gates remote read-back; domains and MCP/plugin wiring route access; schemas, argument checks, API auth, duplicate/stale flag rules, and review endpoints validate or enforce boundaries; relevance/confidence scoring ranks results; reflection/propose/confirm/flag flows update future guidance.

**Knowledge units.** Storage substrate is local SQLite or remote SQL. Representational form is prose insight fields plus symbolic domains, context, evidence, tier, flags, and review status. Lineage is authored or trace-extracted depending on whether the lesson came from direct curation or agent reflection over session experience. Behavioral authority is advisory knowledge when returned by `query`; it gains force through the separate skill protocol that tells the agent when to use and update it.

**Skill, commands, manifest, and bootstrapper.** Storage substrate is the plugin filesystem bundle. Representational form is prose instructions, markdown command prompts, JSON manifest, and Python/Go launcher behavior. Lineage is authored package content versioned with the repository. Behavioral authority is system-definition: the skill instructs agent conduct, the commands shape reflection/status workflows, the manifest wires MCP into the host, and the bootstrapper selects the executable that handles tool calls.

**Local indexes and scoring.** Storage substrate is SQLite tables: `knowledge_units`, `knowledge_unit_domains`, and `knowledge_units_fts`. Representational form is symbolic SQL rows, FTS terms, normalized domains, and scoring constants. Lineage is derived from inserted or updated KUs. Behavioral authority is routing and ranking because it determines which KUs can reach the agent under a query.

**Remote review state.** Storage substrate is server database columns for `status`, `reviewed_by`, `reviewed_at`, `created_at`, and `tier`. Representational form is symbolic metadata over KU JSON. Lineage is server-created and reviewer-updated. Behavioral authority is gating: pending and rejected units remain retained but are excluded from normal query/get/count surfaces, while approved units become eligible knowledge artifacts for agents.

**Trace-reflection candidates.** Before persistence, storage substrate is the host agent's current session context and the markdown command procedure; cq does not retain raw transcripts in the inspected code path. Representational form is prose candidate reasoning that becomes KU prose plus symbolic metadata after proposal. Lineage is weak unless the agent writes source evidence into the KU. Behavioral authority is candidate knowledge until user approval and `propose`, then the normal KU path.

Promotion path: cq's implemented ladder is session lesson or direct advice -> local/private KU -> remote pending KU -> approved remote KU -> confidence/flag-adjusted result. That mainly changes scope, eligibility, and authority rather than turning prose into a stronger formal representation.

## Comparison with Our System

| Dimension | cq | Commonplace |
|---|---|---|
| Primary purpose | Share compact reusable agent learnings across local, hosted, or self-hosted stores | Maintain a typed methodology KB for agent-operated knowledge bases |
| Canonical artifact | Structured KU with summary/detail/action, domains, context, confidence, tier, flags | Markdown artifact with frontmatter, citations, type contract, links, validation, and review state |
| Storage substrate | Local SQLite plus optional remote SQL API; plugin files for instructions | Git-tracked `kb/` collections plus generated reports/indexes |
| Retrieval | Agent calls `query` with domains/context filters; bounded ranked JSON results | `rg`, indexes, authored links, skills, validation, and review reports |
| Governance | Remote pending/approved/rejected review gate; confidence through confirm/flag | Collection/type contracts, schema validation, git diffs, citations, semantic review gates, replacement archives |
| Trace-derived learning | Agent-led reflection/propose turns session events into KUs | Source-grounded writing and review workflows; trace-derived promotion is an explicit methodology concern |

cq and Commonplace share the belief that retained agent knowledge needs an activation path, but they optimize different artifact sizes. cq makes the path small and tool-shaped: query for a few KUs, verify the `action`, and feed back confirmation or flags. Commonplace uses larger artifacts with stronger authoring contracts, citations, and review state, so it trades cq's low-friction sharing for richer lineage and inspectability.

The key authority split is that cq's stored KUs are mostly knowledge artifacts, while its skill, schemas, scoring, and review status are the system-definition artifacts that make those KUs operational. In Commonplace, many retained artifacts are themselves high-authority system-definition artifacts: instructions, type specs, validators, ADRs, review gates, and collection contracts can directly constrain future work.

### Borrowable Ideas

**Small advice units as an interchange format.** Commonplace should not reduce methodology notes to KUs, but a KU-shaped export could work for portable gotchas found during validation, review, or tool operation. Ready as an integration idea, not a replacement for library artifacts.

**Local capture with shared approval.** cq's local fallback plus remote pending queue is a useful promotion pattern. A Commonplace workshop could allow fast local capture of candidate rules, then require review before those rules enter instructions or validators. Ready as a workflow pattern.

**First-class confirm and flag signals.** Commonplace has review gates, but not a lightweight "this guidance helped/hurt in use" signal. cq's confirm/flag operations suggest a runtime feedback layer for frequently consumed instructions. Needs a concrete consumer before implementation.

**Confidence as social evidence, not truth.** The cq skill warns that confidence reflects confirmations, not freshness. Commonplace should preserve that distinction if it ever adds usage or agreement signals to notes.

**Schema-stable external packaging.** cq's schema package and SDKs make KUs portable across hosts. Commonplace could benefit from a narrow export schema for candidate learnings without exposing the whole KB model. Needs a clear external integration.

**Do not import weak lineage into high-authority artifacts.** cq reflection candidates often lack source offsets or durable raw traces. In Commonplace, a cq-like insight should enter a workshop or source-backed note before it becomes an instruction.

## Write side

**Write agency:** `manual` `automatic` — Manual writes come through human/agent approval of `propose`, `confirm`, `flag`, review decisions, and configuration. Automatic writes include the rule-driven construction of KU ids/default evidence/timestamps, local domain/FTS index upkeep, confidence/flag mutations after tool calls, remote fallback/drain behavior, and agent-led extraction of candidate KUs from session traces through the skill and `/cq:reflect`.

**Curation operations:** `synthesize` `evolve` `invalidate` `promote` — Reflection and mid-task propose synthesize new KUs from session experience; confirm/flag evolves existing confidence and flag metadata; stale/incorrect/duplicate flags invalidate weakly by downweighting and recording a reason; remote review promotes pending units into the approved read-back set.

### Trace-derived learning

**Trace source:** `session-logs` `tool-traces` — The raw signal is the current agent-visible session: user request, attempted actions, tool calls, failures, workarounds, and final solution. The Cursor hook can store a short failed-tool summary, but cq does not own a durable transcript database in this commit.

**Learning scope:** `per-task` `cross-task` — Extraction starts from one task/session, while persisted KUs are intended for reuse across later tasks and, when remote storage is configured, across machines or shared stores.

**Learning timing:** `online` `staged` — The skill prefers immediate mid-task proposals when an insight stabilizes; `/cq:reflect` is a staged session-end backstop; remote review is another staged gate before shared read-back.

**Distilled form:** `prose` `symbolic` — Reflected lessons become prose `summary`, `detail`, and `action` fields wrapped in symbolic domains, context, confidence, tier, flags, ids, and review status. There is no parametric distilled artifact in the inspected implementation.

**Extraction.** Extraction is mostly performed by the host agent following markdown instructions. `/cq:reflect` asks the agent to summarize the session, identify candidates, run VIBE safety checks, present them to the user, query for near-duplicates, and propose approved candidates. The oracle is therefore agent judgment plus user approval, duplicate query, and optional remote human review.

**Scope and timing.** cq does not preserve enough raw trace lineage to regenerate a candidate or audit the exact source slice unless the agent writes that evidence into the KU. The Python `DefaultReflector` confirms this boundary: it accepts session context and returns guidance, not extracted candidates.

**Survey fit.** cq belongs in the trace-to-knowledge-unit family. It strengthens the distinction between raw traces and distilled behavior-shaping artifacts: the raw session is transient, while selected lessons become compact KUs that later advise agents through query.

## Read-back

**Read-back:** `pull` — Stored cq knowledge reaches an agent when the agent, skill-guided workflow, CLI user, or host integration deliberately calls `query`; this commit does not implement stored-KU injection into the model context without such a query.

Because read-back is pull-only, there is no push read-back signal to classify and no push faithfulness test to report. The high-authority skill can tell an agent to query often, including before unfamiliar work and after errors, but that is instruction to pull, not an implemented push path that targets and injects KUs.

**Direction edge cases.** The plugin's checked-in `hooks.json` is empty, and the Cursor hook records failed tool calls into short-lived JSON and prints a stop-time summary rather than querying the KU store ([plugins/cq/hooks/hooks.json](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/hooks/hooks.json), [plugins/cq/hooks/cursor/cq_cursor_hook.py](https://github.com/mozilla-ai/cq/blob/36ae42ae4b7c30628133455bde128efe91986235/plugins/cq/hooks/cursor/cq_cursor_hook.py)). That hook may help reflection, but it does not push retained KUs into the next model call.

**Selection, scope, and complexity.** Pull selection is domain-first with optional languages, frameworks, and pattern filters, then relevance times confidence ranking and a bounded limit. The result is shallow and inspectable: compact JSON KUs rather than large notes or transcript chunks. Precision and recall are not verified from code.

**Authority at consumption.** Query results are advisory knowledge artifacts unless the consuming agent follows the skill and inserts their `action` guidance into its plan. The skill gives returned KUs soft instruction force by telling the agent to verify, apply, confirm, or flag them, but the store itself does not enforce behavior after read-back.

**Other consumers.** Humans can use CLI/status/review routes and the server dashboard/review endpoints. Reviewers consume pending KUs as governance artifacts, while SDK and MCP clients consume KUs as portable structured knowledge.

## Curiosity Pass

**cq is a shared pitfall ledger more than a memory palace.** It does not try to summarize projects, maintain a semantic graph, or recall long conversations. The bet is that many repeated failures can be avoided with compact, tagged, action-oriented lessons.

**The skill carries much of the product behavior.** Without the low-threshold query and immediate propose instructions, the backend is a small tagged advice database. The behavior change depends on the host respecting the skill.

**The README's hosted-service update changes deployment, not the core artifact.** `cq.exchange` makes sharing easier, but the inspected mechanism remains the same KU schema plus review-gated remote store.

**Reflection sounds automatic until you read the command.** `/cq:reflect` is a procedure for the agent to mine its own session; it is not a server-side extractor in this commit.

**Remote and local trust semantics differ.** Remote query returns approved units; local query returns locally inserted units. The same KU shape therefore means different governance depending on tier.

**Tag quality is the retrieval bottleneck.** The system bounds result count and ranks by relevance/confidence, but a poor domain set can miss relevant KUs or retrieve weakly related ones.

## What to Watch

- Whether hooks begin querying the store before a retry or task start; that would change cq from pull-only to a push-capable memory system.
- Whether `reflect` becomes an implemented MCP/server-side extractor with retained source lineage, prompts, model versions, and user decisions.
- Whether remote review gains explicit quality, privacy, generalizability, and anti-poisoning checks beyond pending/approved status.
- Whether public-tier graduation is implemented with source abstraction, human review, provenance, and staleness handling.
- Whether ranking adds freshness, review status, flag details, source diversity, or model-family evidence so confirmation count is not treated as truth.
- Whether local KUs get expiry, review, or stale-warning mechanics before private advice accumulates.

Relevant Notes:

- [Trace-derived learning techniques in related systems](../trace-derived-learning-techniques-in-related-systems.md) - extends: cq turns selected session/tool experience into durable, tagged knowledge units through agent-led reflection and propose flows.
- [Knowledge storage does not imply contextual activation](../../notes/knowledge-storage-does-not-imply-contextual-activation.md) - exemplifies: cq stores KUs, but later behavior changes only when an agent queries and uses returned guidance.
- [Knowledge artifact](../../notes/definitions/knowledge-artifact.md) - defined-in: cq KUs are primarily advisory knowledge artifacts when consumed through query results.
- [System-definition artifact](../../notes/definitions/system-definition-artifact.md) - defined-in: the cq skill, MCP tool definitions, scoring code, review gate, and plugin manifest instruct, route, rank, or gate behavior.
- [Use Trace-Derived Extraction As Meta-Learning](../../notes/agent-memory-requirements/use-trace-derived-extraction.md) - exemplifies: cq's `/cq:reflect` flow extracts candidate reusable lessons from session traces, with user approval before persistence.
