# Test procedure: slimmed AGENTS.md + plugin-based skill delivery

This procedure tests the step 13 dogfood: the slimmed AGENTS.md that delegates routing to skills, with skills delivered from `skills/` at repo root.

**Important:** Run this in a fresh session so the old AGENTS.md content is NOT in context. The whole point is testing that the agent can operate with the slimmed control-plane file.

## What changed

- AGENTS.md slimmed: routing table, content workflow, type routing, escalation boundaries, and conventions removed. These are now in `/commonplace:write` skill and `kb/instructions/WRITING.md`.
- KB Goals section added to AGENTS.md.
- Vocabulary paths fixed (`kb/notes/definitions/` not `kb/notes/`).
- WRITING.md references updated to point to `/commonplace:write` instead of "routing table in CLAUDE.md".

## Prerequisites

- Skills live in `skills/` at repo root (7 directories)
- Plugin manifest at `.claude-plugin/plugin.json`
- Codex repo-local marketplace at `.agents/plugins/marketplace.json` points to `./`
- Old `.claude/skills/` symlinks removed (directory exists but empty)
- AGENTS.md is the real file; CLAUDE.md is a symlink to it
- If testing in Codex, restart it after plugin changes and install `commonplace` from `/plugins`

## 1. Skill discovery

Verify all seven framework skills are discoverable with the `commonplace:` prefix:

```
/commonplace:write
/commonplace:connect
/commonplace:validate
/commonplace:ingest
/commonplace:snapshot-web
/commonplace:convert
/commonplace:revise-iterative
```

**Also check:** `review-related-system` and `evaluate-scenarios` should NOT be discoverable (they live in `kb/instructions/`, not `skills/`).

## 2. Write skill — routing without always-loaded routing table

This is the critical test. The old AGENTS.md had a 12-row routing table always in context. Now `/commonplace:write` must handle routing on its own.

### 2a. Write a note (default type)

```
/commonplace:write note
```

Verify:
- Skill reads `kb/instructions/WRITING.md`
- Routes to `kb/notes/`
- Creates a note with correct frontmatter (`type: note`, `status: seedling`, `description:`)
- Title is claim-shaped
- Prompts for `/commonplace:connect` after writing

### 2b. Write an index

```
/commonplace:write index
```

Verify:
- Reads `kb/notes/types/index.md` template
- Routes to `kb/notes/`
- Creates an index with correct frontmatter (`type: index`)

### 2c. Write a text (raw capture)

```
/commonplace:write text
```

Verify:
- Creates a file in `kb/notes/` with NO frontmatter

### 2d. Write an ADR (dynamic type discovery)

```
/commonplace:write adr
```

Verify:
- Skill scans `kb/notes/types/` and finds `adr.md`
- Reads the ADR template
- Routes to `kb/notes/adr/`
- Creates an ADR with correct structure

### 2e. Write a type that doesn't exist

```
/commonplace:write incident-report
```

Verify:
- Errors gracefully
- Lists available types (core + discovered)
- Does NOT create a file

## 3. Validate skill

### 3a. Single note

```
/commonplace:validate kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md
```

Verify: reports PASS/WARN/FAIL.

### 3b. All notes

```
/commonplace:validate all
```

Verify: runs across all notes, shows summary counts.

## 4. Connect skill

```
/commonplace:connect kb/notes/[some-existing-note].md
```

Verify:
- Searches for related notes
- Uses descriptions for relevance (not just keyword match)
- Proposes connections with relationship semantics

## 5. KB Goals scoping test

Ask the agent a scoping question to see if KB Goals work:

> "Should I write a note about Python packaging best practices?"

The agent should recognize this is outside the KB domain (general software engineering, not KB methodology) and either decline or ask how it relates to KB design. This tests that the KB Goals section in the slimmed AGENTS.md is doing its job.

## 6. Escalation to WRITING.md

Ask the agent to write a note without using the skill:

> "Create a note about [topic] in kb/notes/"

The agent should either invoke `/commonplace:write` (because the skills table tells it to) or read `kb/instructions/WRITING.md` before writing. It should NOT try to look up a routing table that no longer exists.

## 7. Review/fix escalation

Ask:

> "Review kb/notes/[some-note].md for quality"

The agent should find its way to `kb/instructions/REVIEW-SYSTEM.md` via the pointer in the skills section of AGENTS.md. It should NOT look for an escalation boundaries section.

## 8. Internal reference integrity

After running the tests above, verify:
- Skills reference correct paths to WRITING.md, type templates
- No skill or instruction references the old "routing table in CLAUDE.md" or "Knowledge System section"
- Skills that invoke other skills use the `commonplace:` prefix (known issue: ~19 occurrences still missing — check if this causes problems in practice)

## 9. Cleanup

After testing:
- Delete any test notes created during the procedure
- Log any issues found in the workshop

## Known issues from prior testing

- **Cross-skill prefix:** ~19 skill invocations use bare names (`/connect`, `/validate`) instead of `/commonplace:connect`. May or may not cause problems — these are in skill prose that the agent reads, not machine-parsed invocations.
- **Broken note links:** Some notes still link to `kb/instructions/connect/SKILL.md` and `kb/instructions/ingest/SKILL.md` (old paths before skills moved). These show up in `/commonplace:validate all` batch warnings.
- **Plugin status:** `arscontexta@agenticnotetaking` shows as disabled in `claude plugin list`, but skills load anyway (likely via direct `skills/` directory discovery, not the plugin system).
