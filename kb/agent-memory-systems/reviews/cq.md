---
description: Local-first agent knowledge commons with SQLite local/team stores, approval-gated team sharing, and a plugin-packaged query/propose/confirm loop; strongest reviewed shared-learning reference so far
type: kb/agent-memory-systems/types/agent-memory-system-review.md
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-03-24"
---

# cq

`cq` is Mozilla.ai's exploratory "shared agent knowledge commons": a Claude plugin and OpenCode MCP integration that lets agents query prior learnings, propose new knowledge units, confirm guidance that worked, and flag stale or incorrect guidance. The implemented system is narrower than the proposal language. What exists today is a local SQLite store, an optional team SQLite store behind a FastAPI service, a review dashboard, and an MCP server that merges local and team results with graceful degradation. The global commons, identity layer, guardrails, and richer trust model are still design material rather than working mechanisms.

**Repository:** https://github.com/mozilla-ai/cq

## Core Ideas

**Plugin-packaged knowledge sharing loop.** The real product surface is not just the database or the API; it is the bundle of plugin manifest, skill, slash commands, and MCP server. The `cq` skill teaches agents a concrete behavior loop: query before unfamiliar work, propose after discovering something non-obvious, confirm when guidance proved correct, and flag bad guidance. This is a clean example of shipping a knowledge architecture as agent-facing packaging rather than as a standalone backend alone.

**Local-first storage with offline-to-team promotion.** The MCP server owns a local SQLite database at `~/.cq/local.db`. When `CQ_TEAM_ADDR` is configured and reachable, `propose` sends new knowledge directly to the team API; when it is unreachable, the server falls back to local storage. On next startup, `_drain_local_to_team()` retries those locally stored proposals and deletes them after successful promotion. This is the repo's strongest implemented mechanism: shared knowledge without making network availability a hard dependency.

**Knowledge units are compact operational triples, not notes.** The unit shape is fixed by Pydantic models: `summary`, `detail`, `action`, plus domain tags, lightweight context (`languages`, `frameworks`, `pattern`), and simple evidence metadata. This is optimized for quick retrieval and reuse of operational tips. It is not trying to be a compositional knowledge medium; there are no links, no indexes, no progression from sketch to mature argument, and no place for long-form reasoning to accumulate.

**Team sharing is gated by human review.** Team proposals enter the shared store as `pending`, and agent-facing `get()`/`query()` only expose `approved` units. The repo ships JWT auth, review queue endpoints, and a React dashboard for approving and rejecting candidates. That makes `cq` more governance-heavy than most memory tools: it does not assume that successful proposal is enough for shared availability.

**Retrieval is intentionally simple.** Relevance is `Jaccard(domain overlap) * 0.7 + language match * 0.15 + framework match * 0.15`, then multiplied by confidence. Local search supplements domain matching with SQLite FTS over `summary`, `detail`, and `action`; the team store currently filters by approved domain matches and scores in memory. Confirmation and flagging adjust confidence linearly. This is a pragmatic operational baseline, not a sophisticated retrieval or trust model.

## Comparison with Our System

| Dimension | cq | Commonplace |
|---|---|---|
| Primary purpose | Share short operational learnings across agents and teams | Build a navigable, inspectable knowledge base for agents and humans |
| Persistent substrate | SQLite local store + SQLite team store + MCP/API/plugin packaging | Markdown files in git with frontmatter, links, and curated indexes |
| Knowledge unit | Structured tip: summary/detail/action + tags/context/confidence | Typed note with prose body, links, status, and optional stronger forms |
| Sharing model | Local capture, team sync, human approval for shared availability | Repo-native sharing through files, review, links, and explicit curation |
| Retrieval | Domain-tag query with simple scoring; local FTS; merged local/team results | Search, descriptions, indexes, and semantic link traversal |
| Governance | Review queue and approval gate for team tier | Structural validation, semantic review, and human editorial judgment |
| Learning strength | Strong on cross-agent operational tip reuse | Strong on inspectability, explanatory structure, and composability |

`cq` is stronger where Commonplace is still thin: quick cross-agent sharing of compact operational knowledge with a real confirm/flag loop and a concrete path from private discovery to team-available guidance. Commonplace is stronger where `cq` stays deliberately narrow: note quality, explanatory reach, explicit relationships, and durable knowledge structure beyond isolated tips.

The systems also make opposite substrate bets. `cq` optimizes for low-friction agent consumption through opaque records and simple scores. We optimize for inspectable artifacts that remain legible to humans and support traversal as reasoning. That means `cq` can more easily automate a shared operational commons, while Commonplace can support richer synthesis once knowledge matters for more than "what action should I take next?"

## Borrowable Ideas

**Offline-first shared sync with retry-on-startup.** Ready to borrow now. The fallback from team proposal to local storage, followed by deterministic drain on reconnect, is a strong pattern for any shared agent service. It keeps capture cheap without pretending the network is reliable.

**Approval gates only at the sharing boundary, not at capture time.** Ready to borrow now as a principle. `cq` preserves an ungated capture path in local-only or fallback mode while requiring review before team-wide reuse. If we build any shared workshop or operations memory, this split is better than forcing every candidate through the same gate immediately.

**Package the behavior loop with the integration, not just the transport.** Ready to borrow now. The plugin bundles skill text, slash commands, and MCP configuration so the usage protocol ships alongside the tools. This is stronger than exposing an API and hoping the agent learns the right loop from examples.

**Compact action-oriented unit shape for operational learnings.** Needs a use case first. The `summary/detail/action` triplet is too thin for library knowledge, but it is a good fit for short-lived operational warnings or environment gotchas where the main question is "what should I do differently?"

## Curiosity Pass

**The docs overstate how much of the trust stack is real.** Architecture docs describe guardrails, PII filtering, prompt-injection checks, DIDs, KERI, anti-poisoning, global commons flows, and privacy-preserving proofs. The implemented `propose` path in `cq_mcp/server.py` creates a knowledge unit and either posts it to team or writes it locally; no guardrail or trust-layer code runs in that path. The shared-learning loop is real. The stronger governance language is mostly design intent.

**`reflect` is mostly workflow prose, not server capability.** The slash command `/cq:reflect` contains a rich human-agent procedure for mining session learnings, but the MCP `reflect` tool itself returns an empty candidate list with `status: "stub"`. Even if the surrounding workflow works in practice, the mechanism currently lives in prompt instructions and agent reasoning, not in the server.

**The hook story is ahead of the actual hook file.** `docs/architecture.md` describes a post-error auto-query hook, but `plugins/cq/hooks/hooks.json` only runs `uv sync` on `SessionStart`. That does not make the system useless, but it does matter for claims about automatic behavior. The installed behavior today is "ensure the server environment exists," not "auto-query cq when errors occur."

**The review gate is real, but the knowledge model stays shallow.** Human approval helps with legitimacy, not deep verification. Reviewers can judge whether a unit looks plausible and generalisable, but the schema gives them only a compact operational tip, not the fuller context needed for explanatory review. That means the team tier can become trustworthy enough for "remember this pitfall," but it is unlikely to grow into a richer knowledge base without a second, more expressive artifact form.

**Retrieval simplicity is both a feature and a ceiling.** The simpler alternative to vector search is exactly what `cq` ships: domain tags, light context boosts, and FTS on the local side. That is a defensible choice for a small operational commons. But even if it works perfectly, it can only retrieve what its tags and short fields can express. It cannot recover the richer, cross-note reasoning patterns that our KB's links and longer prose bodies make possible.

## What to Watch

- Whether the stubbed `reflect` tool becomes a real mining subsystem rather than a prompt-level workflow carried by the slash command
- Whether the documented guardrails layer (`any-guardrail`, PII filtering, prompt-injection checks) actually enters the `propose` and promotion paths
- Whether the team store grows beyond one approved/pending/rejected queue into stronger deduplication, synthesis, or staleness handling
- Whether the promised global commons and identity layer ever materialize, or whether `cq` remains primarily a local-plus-team operational memory tool

---

Relevant Notes:

- [deploy-time-learning-the-missing-middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — exemplifies: `cq` improves deployed agent behavior through durable symbolic artifacts rather than weight updates
- [files-not-database](../../notes/files-not-database.md) — contrasts: `cq` chooses SQLite records and API surfaces where Commonplace chooses inspectable files
- [the-boundary-of-automation-is-the-boundary-of-verification](../../notes/the-boundary-of-automation-is-the-boundary-of-verification.md) — grounds: the team review gate exists because shared knowledge quality cannot be cheaply verified automatically
- [instruction-specificity-should-match-loading-frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) — exemplifies: the plugin bundles manifest, skill, commands, and MCP server so usage instructions load at the right boundary
- [getsentry/skills](./getsentry-skills.md) — compares: both use agent-facing packaging around operational behavior, but `getsentry/skills` codifies skill creation while `cq` codifies knowledge sharing
- [crewai-memory](./crewai-memory.md) — compares: both are service-style memory systems with opaque stores and retrieval infrastructure, but `cq` adds explicit human review for team-visible knowledge
