# Test procedure: Codex plugin install + commonplace skill behavior

This procedure tests commonplace after installation into Codex through a local marketplace and the interactive `/plugins` flow.

**Important:** Run this in a fresh Codex session after restarting Codex. The point is to verify the installed plugin and the slimmed `AGENTS.md`, not accidental carry-over from an older session.

## Prerequisites

- The repo-local marketplace file exists at `.agents/plugins/marketplace.json`
- Codex has been restarted after the latest plugin or skill changes
- The `commonplace` plugin is installed from `/plugins`
- `AGENTS.md` is the active control-plane file
- The framework skills live in `skills/` at repo root

## How to invoke skills in Codex

Use Codex's current explicit plugin or skill surface rather than Claude-style slash commands. The exact UI may evolve, but the test should always target the `commonplace` plugin's bundled skills:

- `write`
- `connect`
- `validate`
- `snapshot-web`
- `ingest`
- `convert`
- `revise-iterative`

If Codex exposes multiple explicit invocation surfaces such as `/skills`, `@`, or `$`, use whichever is current and stable in that build.

## 1. Plugin visibility

Open `/plugins` and verify:

- `Local Commonplace Plugins` appears
- `commonplace` is listed inside it
- `commonplace` shows as installed

If the plugin is missing, restart Codex and check `.agents/plugins/marketplace.json` plus `.codex-plugin/plugin.json`.

## 2. Skill visibility

Use Codex's explicit skill or plugin invocation surface and verify all seven framework skills are available from the installed `commonplace` plugin:

- `write`
- `connect`
- `validate`
- `snapshot-web`
- `ingest`
- `convert`
- `revise-iterative`

Also verify that repo-local instructions that are not shipped as plugin skills are not surfaced as plugin skills:

- `review-related-system`
- `evaluate-scenarios`

## 3. Write skill

This is the critical test. `AGENTS.md` no longer carries the routing table, so the `write` skill must own routing behavior.

### 3a. Write a note

Invoke the `write` skill with `note`.

Verify:

- The skill reads `kb/instructions/WRITING.md`
- It routes to `kb/notes/`
- It creates a note with valid frontmatter
- The title is claim-shaped when the content warrants it
- It suggests follow-up connection work after writing

### 3b. Write an index

Invoke the `write` skill with `index`.

Verify:

- It reads `kb/notes/types/index.md`
- It routes to `kb/notes/`
- It creates an `index` note with the expected frontmatter

### 3c. Write a text

Invoke the `write` skill with `text`.

Verify:

- It creates a file in `kb/notes/`
- The file has no frontmatter

### 3d. Write an ADR

Invoke the `write` skill with `adr`.

Verify:

- It scans `kb/notes/types/` and finds `adr.md`
- It routes to `kb/notes/adr/`
- It creates an ADR with the expected structure

### 3e. Request a missing type

Invoke the `write` skill with `incident-report`.

Verify:

- It errors cleanly
- It lists available types
- It does not create a file

## 4. Validate skill

### 4a. Single note

Invoke the `validate` skill on `kb/notes/context-efficiency-is-the-central-design-concern-in-agent-systems.md`.

Verify:

- It reports PASS, WARN, or FAIL
- It checks structure rather than attempting semantic editorial review

### 4b. Batch validation

Invoke the `validate` skill on `all`.

Verify:

- It scans the whole KB
- It reports summary counts
- Any warnings point at real path or structure issues

## 5. Connect skill

Invoke the `connect` skill on an existing note path.

Verify:

- It searches for related notes
- It uses descriptions and note content, not just literal keyword overlap
- It proposes relationship semantics rather than generic "relatedness"
- It writes a workshop report instead of mutating KB notes directly

## 6. KB Goals scoping

Ask Codex:

> Should I write a note about Python packaging best practices?

Verify:

- It recognizes that this is outside the KB's scope unless tied back to KB methodology
- It declines or asks for the KB-methodology angle

## 7. Escalation to writing guidance

Ask Codex:

> Create a note about [topic] in kb/notes/

Verify:

- It routes through the `write` skill or clearly follows `kb/instructions/WRITING.md`
- It does not look for the removed routing table

## 8. Review/fix escalation

Ask Codex:

> Review kb/notes/[some-note].md for quality

Verify:

- It follows the pointer to `kb/instructions/REVIEW-SYSTEM.md`
- It does not invent an obsolete escalation section from `AGENTS.md`

## 9. Runtime-neutral wording audit

Spot-check the installed guidance and skill text:

- `AGENTS.md`
- `AGENTS.md.template`
- `kb/instructions/WRITING.md`
- `skills/write/SKILL.md`
- `skills/connect/SKILL.md`
- `skills/convert/SKILL.md`
- `skills/ingest/SKILL.md`

Verify:

- They refer to commonplace skills by skill name, not Claude-only slash syntax
- They do not instruct Codex users to run `/commonplace:...`
- Cross-skill guidance still makes sense in Codex

## 10. Cleanup

- Delete test notes created during the run
- Keep any useful workshop artifacts if they help fix bugs
- Log issues in `kb/work/installation-simplification/`

## Residual risks

- Codex explicit invocation UX may change faster than the skill files do; prefer stable behavioral assertions over exact UI click-paths.
- Some workshop notes in `kb/work/installation-simplification/` still use Claude-oriented examples; they are planning artifacts, not runtime instructions.
