# Test procedure: plugin-based skill delivery

After installing commonplace as a local plugin (`claude plugin install .`), run through these checks to verify skills work with the `commonplace:` namespace prefix.

## Prerequisites

- Plugin installed successfully (`claude plugin install .` or equivalent)
- Old `.claude/skills/` symlinks removed
- Skills live in `skills/` at repo root
- Plugin manifest at `.claude-plugin/plugin.json`

## 1. Skill discovery

Verify all framework skills are discoverable:

```
/commonplace:write
/commonplace:connect
/commonplace:validate
/commonplace:ingest
/commonplace:snapshot-web
/commonplace:convert
/commonplace:revise-iterative
```

**Test:** Type `/commonplace:` and check autocomplete shows all seven skills.

**Also check:** Is `review-related-system` discoverable? It's in `kb/instructions/` (not `skills/`), so it should NOT appear as a plugin skill. It should only work if symlinked separately.

## 2. Write skill — core types

### 2a. Write a note (default type)

```
/commonplace:write note
```

Verify:
- Skill fires and reads WRITING.md
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
- This is raw capture — minimal ceremony

## 3. Write skill — dynamic type discovery

### 3a. Write a local type that exists

```
/commonplace:write adr
```

Verify:
- Skill scans `kb/notes/types/` and finds `adr.md`
- Reads the ADR template
- Routes to `kb/notes/adr/`
- Creates an ADR with correct structure (Context/Decision/Consequences)

### 3b. Write a type that doesn't exist

```
/commonplace:write incident-report
```

Verify:
- Skill errors gracefully
- Error message lists available types (core + any local types found in `kb/*/types/`)
- Does NOT create a file

## 4. Connect skill

```
/commonplace:connect kb/notes/[some-existing-note].md
```

Verify:
- Searches `kb/notes/` for related notes
- Uses descriptions to judge relevance (not just keyword match)
- Proposes connections with relationship semantics (extends, grounds, contradicts, etc.)
- Writes links into the target note and the connected notes

## 5. Validate skill

### 5a. Validate a single note

```
/commonplace:validate kb/notes/[some-existing-note].md
```

Verify:
- Checks frontmatter (type, status, description present)
- Checks link health (relative links resolve)
- Reports PASS/WARN/FAIL

### 5b. Validate all notes

```
/commonplace:validate all
```

Verify:
- Runs across all notes in `kb/notes/`
- Summary shows pass/warn/fail counts

## 6. Ingest skill

```
/commonplace:ingest [some-url]
```

Verify:
- Snapshots the URL into `kb/sources/`
- Writes `.ingest.md` with source-review type frontmatter
- Classifies and analyzes the source

## 7. Snapshot-web skill

```
/commonplace:snapshot-web [some-url]
```

Verify:
- Snapshots the URL into `kb/sources/`
- Creates a markdown file with the page content
- Does NOT run ingestion analysis (that's `/commonplace:ingest`)

## 8. Convert skill

Create a test text file (no frontmatter) in `kb/notes/`, then:

```
/commonplace:convert kb/notes/[test-text-file].md
```

Verify:
- Adds frontmatter (type: note, status: seedling, description)
- Renames file to match the title
- Fixes any backlinks if the filename changed

## 9. Revise-iterative skill

```
/commonplace:revise-iterative kb/notes/[some-note].md
```

Verify:
- Produces numbered revision copies
- Reviews for semantic fidelity between passes
- Does not introduce new content — only improves flow and readability

## 10. Cross-skill workflows

### 10a. Full write-connect-validate cycle

1. `/commonplace:write note` — create a note about a test topic
2. `/commonplace:connect [the-new-note]` — find and link related notes
3. `/commonplace:validate [the-new-note]` — verify structure is clean

All three should work in sequence. The connect step should find the note written in step 1.

### 10b. Ingest-then-write cycle

1. `/commonplace:ingest [some-url]` — ingest an external source
2. `/commonplace:write note` — write a note that references the ingested source
3. `/commonplace:connect [the-new-note]` — should discover connection to the ingest report

## 11. Skills that should NOT work via plugin

### 11a. Review-related-system

```
/commonplace:review-related-system
```

This should either:
- Not be discoverable (if it's not in `skills/`)
- Or be discoverable but work correctly if it IS in `skills/`

Check which case applies and whether it matches the plan.

### 11b. Evaluate-scenarios

```
/commonplace:evaluate-scenarios
```

This was a repo-local skill in `kb/instructions/evaluate-scenarios/`. It should NOT be discoverable via the plugin.

## 12. Internal reference integrity

After running the tests above, verify:
- Skills reference correct paths to WRITING.md, type templates, etc. (these changed when skills moved from `kb/instructions/` to `skills/`)
- Skills that invoke other skills use the `commonplace:` prefix
- No skill references the old `kb/instructions/[skill-name]/` path

## 13. Cleanup

After testing, decide:
- Keep the test notes? (Delete if they clutter the KB)
- Any skills that need path fixes?
- Any issues to log in the workshop?

## Known limitations

- `/connect` won't find connections to skill files — skills are in `skills/`, outside `kb/`. This is a known issue (see plan open questions). For now, link manually when a theory note affects a skill.
- `rg "keyword" kb/` won't search skill content. Use `rg "keyword" skills/ kb/` to search both.
- qmd index doesn't include `skills/` by default. Add a `skills` collection to `~/.config/qmd/commonplace.yml` if needed.
