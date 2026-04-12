---
description: Self-hosted skill registry with partial local-first editing resilience, dual version tracks, live MCP tool exposure, and agent-submitted per-version ratings
type: agent-memory-system-review
traits: [has-comparison, has-implementation, has-external-sources]
tags: [related-systems]
status: current
last-checked: "2026-04-04"
---

# SkillNote

SkillNote is Luna Prompts' self-hosted registry for `SKILL.md` artifacts. It combines a Next.js web app, a FastAPI backend, a FastMCP server, PostgreSQL, and a Node CLI so teams can author skills in a browser, expose them live over MCP, and optionally install published bundles into agent-specific directories. The interesting part is not "skills in a database" by itself, but the way SkillNote turns one artifact type into three primary operational surfaces at once: editable registry content, installable release bundles, and MCP tools with built-in feedback capture.

**Repository:** https://github.com/luna-prompts/skillnote

## Core Ideas

**Registry over file format.** SkillNote keeps the `SKILL.md` format as the interchange artifact, but the working system is registry-first rather than repo-first. Editable skills live in PostgreSQL rows (`skills` plus `skill_content_versions`), while the frontend regenerates and parses frontmatter through `src/lib/markdown-utils.ts`. This means the system treats `SKILL.md` as a portable packaging format, not as the primary storage substrate.

**Two version tracks for one skill.** The backend maintains two distinct server-side histories. Every backend-persisted edit creates an integer `SkillContentVersion` snapshot (`backend/app/api/skills.py`, `backend/app/db/models/skill_content_version.py`) so the UI can restore prior draft states. Publishing is separate: semver-tagged `SkillVersion` rows point to checksummed ZIP bundles in local storage (`backend/app/api/publish.py`, `backend/app/db/models/skill_version.py`). This is a real architectural distinction, not just naming. Authoring history and distributable releases are different objects, even though local shadow edits can temporarily exist outside both tracks during outages.

**MCP is a live projection of the registry.** The MCP server does not serve static files from disk. It queries the skills table on every `list_tools` / `get_tool` call, converts each row into a tool (`name = slug`, `description = description`, body = stored markdown), and can filter visibility by `collections` (`backend/mcp_server.py`). Skill create/update/delete events call `pg_notify('skillnote_skills_changed', ...)`, and the MCP server listens with PostgreSQL `LISTEN` and pushes `notifications/tools/list_changed` to connected clients. The "live registry" claim is mechanically real.

**Feedback is part of the tool surface, not a separate dashboard feature.** SkillNote appends a `complete_skill` tool alongside skill tools when enabled. The MCP server records both `skill_call_events` and `skill_ratings`, and the analytics API reads directly from those tables. This gives the system a genuine runtime feedback-capture loop: the agent can call a skill, then submit a rating and optional outcome tied to the skill slug and current version. The feedback remains self-reported, but it is implemented as part of the runtime contract rather than as an out-of-band survey.

**The frontend uses a local shadow store to survive backend failure.** `src/lib/skills-store.ts` renders from localStorage first, merges API state in the background, and falls back to local-only create/update when the backend is unreachable. This gives the UI immediate startup and some offline resilience. But the implementation matters: delete still requires the API, and local-only changes are preserved rather than replayed through a sync queue later. The mechanism is useful, but it is weaker than a full offline-first replication model.

**Distribution is bundle-based, not git-based.** The CLI downloads published ZIP bundles, verifies checksums, installs files into agent adapter directories, and records installed versions in `.skillnote/manifest.json` (`cli/src/commands/add.ts`, `cli/src/manifest/index.ts`). This is closer to a package manager than to "git pull a shared skills repo." The upside is reproducible install state and explicit release channels; the downside is that collaborative diffing and branching happen outside the distribution path.

## Comparison with Our System

| Dimension | SkillNote | Commonplace |
|---|---|---|
| Primary artifact | `SKILL.md` skills as the whole product surface | Mixed knowledge artifacts: notes, instructions, sources, ADRs, tasks |
| Persistent substrate | PostgreSQL rows + localStorage shadow state + ZIP bundle storage | Markdown files in git, with derived indexes and scripts |
| Discovery model | UI search, collections, MCP `tools/list`, description-based tool routing | Descriptions, links, indexes, search, and traversal as reasoning |
| Version model | App-managed content snapshots plus semver release bundles | Git-native history over authored files |
| Learning loop | Agent-submitted call telemetry and ratings; humans improve skills manually | Human-authored note changes, validation, reviews, and explicit knowledge curation |
| Distribution | Live MCP registry or CLI bundle install | Repo checkout, direct file access, local skills, and KB navigation |

SkillNote is stronger where Commonplace is still thin: centralized distribution, shared hosting, live MCP projection, and usage telemetry for skills as reusable operational artifacts. Commonplace is stronger where SkillNote is intentionally narrow: inspectable reasoning, compositional links, explanatory reach, and heterogeneous knowledge forms beyond one `SKILL.md` schema.

The biggest architectural split is the storage choice. SkillNote makes the opposite bet from [files-not-database](../../notes/files-not-database.md): it centralizes skills in a database-backed application and treats file export as a secondary interface. That gives it better coordination and a better UX for a team-facing registry, but it loses the default diffability and direct browseability that file-first systems get for free.

## Borrowable Ideas

**`complete_skill` as a first-class feedback closure.** Ready to borrow when we expose skills over MCP. The important idea is not "collect ratings" in the abstract, but making the post-use feedback action part of the runtime surface so the agent can close the loop in the same protocol it used to load the skill.

**Push invalidation for live tool catalogs.** Ready to borrow when we serve dynamic skills. `pg_notify` plus `notifications/tools/list_changed` is a crisp pattern for keeping MCP clients current without reconnects or polling.

**Separate edit history from distributable releases.** Needs a use case first. The split between `SkillContentVersion` and semver ZIP bundles is sensible when a skill is both collaboratively edited and externally installed. We do not yet have that distribution problem in commonplace, but if we start shipping skills as products, this boundary is worth reusing.

**Collection-scoped MCP URLs.** Ready to borrow when we need role- or team-specific skill subsets. The filtering mechanism is simple, legible, and already aligns with how many harnesses think about capability subsets.

**Checksum-verified bundle installs with a local manifest.** Needs a use case first. The CLI's manifest and checksum verification are useful if skills become installable dependencies rather than just repo files. That is a real packaging pattern, but it is premature for our current file-first workflow.

## Curiosity Pass

**The feedback loop is real, but it stops at telemetry.** SkillNote's strongest marketing claim is the "built-in feedback loop," and the tool/runtime plumbing for that claim is genuine. But even if it worked perfectly, the system would still only produce ratings, outcomes, and call counts. It does not synthesize revised skills, mine failure patterns into new rules, or promote agent traces into richer knowledge automatically. The ceiling is "help humans see what to improve," not "learns to improve itself."

**The offline-first story is only partially implemented.** `skills-store.ts` gives the UI a local shadow store and preserves local-only entries during API sync, which is enough to avoid a blank screen and enough to keep editing during outages. But there is no durable replay queue that later publishes those local-only creates/updates back to PostgreSQL, and delete remains online-only. So the mechanism achieves frontend resilience, not full eventual-consistency offline sync.

**The install model is narrower than the README suggests.** The README advertises paths like `~/.claude/skills/` and `~/.codex/skills/`, but the actual adapters mostly install into project-local directories such as `.claude/skills/`, `.cursor/skills/`, and `.codex/skills/`. OpenClaw is even stranger: it detects `~/.openclaw` in the home directory but installs into `projectDir/skills/`. That does not invalidate the bundle-install story, but it means the repo currently implements a project-scoped installation strategy more than a universal user-scoped one.

**The simplest alternative is still a git repo of skills.** The extra machinery only earns its keep if you value live MCP projection, centralized editing, ratings, analytics, and package-like distribution. If all you need is shared skills with diffs and branching, a normal repo is cheaper. SkillNote is therefore best understood as a coordination product over skills, not merely as a storage format for them.

## What to Watch

- Whether the localStorage shadow store becomes a real replay/sync subsystem rather than a frontend fallback that preserves unsynced local edits indefinitely
- Whether `complete_skill` stays as telemetry or becomes the input to a more structured refinement loop (holdouts, replay, or skill mutation)
- Whether the install adapters converge on a coherent project-scope vs user-scope model across Claude Code, Codex, Cursor, OpenClaw, and OpenHands
- Whether collections remain lightweight filters or grow into actual policy boundaries with authentication and access control
- Whether the currently open API surface described in `CLAUDE.md` grows into a real multi-user governance model, which matters if the product wants to be more than a single-team self-hosted tool

---

Relevant Notes:

- [skills-are-instructions-plus-routing-and-execution-policy](../../notes/skills-are-instructions-plus-routing-and-execution-policy.md) — grounds: SkillNote packages skills precisely as routed, invocable execution artifacts
- [skills-derive-from-methodology-through-distillation](../../notes/skills-derive-from-methodology-through-distillation.md) — contrasts: SkillNote stores and distributes skills but says little about how their content should be derived or maintained theoretically
- [instruction-specificity-should-match-loading-frequency](../../notes/instruction-specificity-should-match-loading-frequency.md) — analogizes: SkillNote has a looser metadata/body split between tool descriptions and stored skill markdown than the harness pattern described there
- [mcp-bundles-stateless-tools-with-stateful-runtime](../../notes/mcp-bundles-stateless-tools-with-stateful-runtime.md) — contextualizes: SkillNote is a concrete example of accepting the stateful-runtime cost in exchange for a live shared tool registry
- [files-not-database](../../notes/files-not-database.md) — trades off against: SkillNote chooses coordination and UX through a database-backed registry where commonplace argues files should stay primary until capabilities justify more structure
- [deploy-time-learning-is-the-missing-middle](../../notes/deploy-time-learning-is-the-missing-middle.md) — partially exemplifies: ratings and skill revisions operate on durable symbolic artifacts even though the learning loop remains human-mediated
- [getsentry/skills](./getsentry-skills.md) — compares: getsentry/skills is strongest on skill creation and synthesis discipline, while SkillNote is strongest on hosting, distribution, and feedback plumbing
- [Agent Skills for Context Engineering](./agent-skills-for-context-engineering.md) — compares: both take skills seriously as agent-facing artifacts, but one is a teaching/reference library and the other is a registry product
