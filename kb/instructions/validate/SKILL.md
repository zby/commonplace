---
name: validate
description: Schema validation for KB notes. Checks against note type — text files (no frontmatter) are always valid; notes and above are checked for description quality, type/trait enums, link health, and areas-topics consistency. Non-blocking — warns but doesn't prevent editing. Triggers on "/validate", "/validate [note]", "/validate all", "/validate recent".
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash
context: fork
model: sonnet
---

## EXECUTE NOW

**Target: $ARGUMENTS**

Parse immediately:
- If target contains a note path or name: validate that specific note
- If target is "all" or "notes": validate all `.md` files in `kb/notes/` (including subdirectories)
- If target is "recent" or "today": validate notes modified today
- If target is empty: ask which note to validate

**Execute these steps:**

### Step 1: Locate Target Notes

**Single note:** Resolve the path. If just a name, search `kb/notes/` for a matching `.md` file.

**Batch ("all"):** Discover all `.md` files in `kb/notes/` recursively.

**Recent:** Find notes modified today:
```bash
find kb/notes/ -name "*.md" -mtime 0
```

### Step 2: Detect Type and Read Each Target Note

For each note, read the full file. First determine the base type:

1. **No frontmatter** (file does not start with `---`) → **text**. Report PASS and skip all further checks. Text files have no structural requirements.
2. **Has frontmatter** → parse YAML. Determine type from `type:` field (default: `note` if absent).

For notes and above, parse:
- All frontmatter fields and their values
- The body content (for link scanning)
- The footer section (for `Topics:` links)

### Step 3: Run Type-Appropriate Checks

Validation checks are cumulative — each type inherits checks from simpler types:

- **text**: no checks (always valid)
- **note**: frontmatter validity, description, enum fields, composability, link health, areas-topics
- **structured-claim**: note checks + Evidence and Reasoning sections present
- **spec**: note checks + Design/Implementation sections present
- **review**: note checks + Findings section present
- **index**: note checks + link density (primarily navigational)
- **adr**: note checks + Context/Decision/Consequences sections present

Run every applicable check. Each check produces PASS, WARN, FAIL, or INFO.

**START NOW.**

---

## Schema Checks

### FAIL-level Checks (required — blocks validation)

#### 1. Frontmatter Valid

Applies to: all types except `text`

| Check | Rule | How to Verify |
|-------|------|---------------|
| Opening delimiter | File starts with `---` on line 1 | Check first line |
| Closing delimiter | A second `---` exists after YAML fields | Scan for closing delimiter |
| Valid YAML | Parses without errors | Check for common YAML errors: unquoted colons in values, mismatched quotes, bad indentation |
| No duplicate keys | Each YAML key appears only once | Scan for repeated field names |

A file with partial/broken frontmatter (has `---` but malformed YAML) is not a seedling — it's a broken note. Report FAIL.

#### 2. Description Exists

Applies to: all types except `text`

| Check | Rule | How to Verify |
|-------|------|---------------|
| `description` field | Must exist in frontmatter | Check for `description:` key |
| Non-empty | Must have a non-empty value | Check that value is not blank, `""`, or `~` |

### WARN-level Checks (quality — does not block)

#### 3. Description Quality

Applies to: all types except `text`

| Check | Rule | How to Verify |
|-------|------|---------------|
| Length | Should be ~50-200 characters | Count characters in description value |
| Discrimination | Must help pick THIS note over similar ones | Compare description against filename/title — if semantically equivalent, WARN. Then ask: if 5 notes matched a search, would this description help choose this one? |
| No trailing period | Convention: descriptions don't end with periods | Check last character |
| Single sentence | Should be one coherent statement | Check for sentence-ending punctuation (`. ! ?`) mid-description |

**The description is a retrieval filter, not a summary.** It answers "why THIS note?" not "what is this note about?" The title already states the claim; the description orients the reader by adding what the title can't carry. In priority order:

1. **Mechanism** — how or why the claim works (strongest discriminator)
2. **Scope** — what boundaries or conditions the claim has
3. **Implication** — what follows from the claim in practice
4. **Context** — where the claim applies or what prompted it

Lead with mechanism or scope — these discriminate best. Add implication if space allows. Within 200 chars you typically fit one or two of these.

**Examples:**

Bad (restates title — no discrimination value):
- Title: `approvals guard against llm mistakes not active attacks`
- Description: "The approval system protects against LLM errors rather than deliberate attacks"

Good (adds mechanism — reader immediately knows WHY):
- Title: `approvals guard against llm mistakes not active attacks`
- Description: "A determined attacker controls the prompt and can social-engineer approval; approvals catch the common case of tool misuse from hallucination or misunderstanding"

Good (adds scope — reader knows WHEN this applies):
- Title: `oracle strength spectrum`
- Description: "The bitter lesson boundary is a gradient, not a binary — oracle strength (how cheaply and reliably you can verify correctness) determines where on the spectrum a component sits"

#### 4. Type Valid

Applies to: all types except `text`

| Check | Rule | How to Verify |
|-------|------|---------------|
| Non-empty string | If `type:` present, must be a non-empty string | Check value is present and not blank |

The `type` field is a free-form string — convention establishes common values (`note`, `structured-claim`, `spec`, `review`, `index`, `adr`), but there is no closed enum. Directory-scoped `types/` folders document structural expectations for each value.

Skip this check if `type:` is absent (it's optional, defaults to `note`).

#### 5. Traits Valid

Applies to: all types except `text`

| Check | Rule | How to Verify |
|-------|------|---------------|
| Enum values | If `traits:` present, every value must be a valid trait | Compare each against allowed list |

**Valid traits:** `has-comparison`, `has-external-sources`, `has-implementation`

Report each invalid trait individually. Skip if `traits:` is absent.

#### 6. Status Valid

Applies to: all types except `text`

| Check | Rule | How to Verify |
|-------|------|---------------|
| Enum value | If `status:` present, must be one of the valid statuses | Compare against allowed list |

**Valid statuses:** `seedling`, `current`, `speculative`, `outdated`

Skip if `status:` is absent.

#### 7. Composability

Applies to: all types except `text`

| Check | Rule | How to Verify |
|-------|------|---------------|
| Prose fitness | Title works as inline prose: "since [title]..." reads naturally | Read the title as a sentence fragment |
| Not a topic label | Title makes a claim or describes a specific thing, not just a category | Could someone reasonably reference this in a sentence? |
| Specificity | Claim is specific enough to disagree with | Could someone reasonably argue the opposite? |

**Topic labels vs claims:**
- "knowledge management" — topic label, WARNS
- "knowledge management requires curation not accumulation" — claim, PASSES
- "context-loading-strategy" — descriptive name for a specific thing, PASSES

#### 8. Link Health

Applies to: all types except `text`

| Check | Rule | How to Verify |
|-------|------|---------------|
| Markdown link targets | Each `[text](./path.md)` target must resolve to an existing file | Extract all markdown links from body, resolve relative to note's directory, check file exists |
| Skip code blocks | Links inside backtick blocks are examples, not real links | Skip links inside single or triple backtick blocks |
| Skip external URLs | Only check relative links, not `http://` or `https://` | Filter out absolute URLs |

**How to verify:** For each relative markdown link, resolve the path relative to the note's directory and check if the target file exists.

#### 9. Areas-Topics Consistency

Applies to: all types except `text`

| Check | Rule | How to Verify |
|-------|------|---------------|
| Areas without Topics | If `areas:` is set in frontmatter, a `Topics:` footer should exist | Scan for `Topics:` section at end of file |
| Topics without Areas | If `Topics:` footer exists, `areas:` should be set | Check frontmatter for `areas:` field |
| Sync suggestion | If mismatch detected, suggest running sync script | Report: `uv run kb/scripts/sync_topic_links.py <note-path>` |

This check verifies that the two representations stay in sync. `areas:` is the source of truth; `Topics:` footer is generated from it.

#### 10. Type-Specific Structure

Applies to: `structured-claim`, `spec`, `review`, `index`, `adr` only

| Type | Required structure | How to Verify |
|------|--------------------|---------------|
| `structured-claim` | Has Evidence and Reasoning sections; title is an assertion | Grep for `## Evidence` and `## Reasoning` headings |
| `spec` | Has Design and/or Implementation sections | Grep for `## Design` or `## Implementation` headings |
| `review` | Has Findings section; is dated | Grep for `## Findings` heading; check for date in frontmatter or body |
| `index` | Primarily navigational links | Check that link density is high relative to prose |
| `adr` | Has Context, Decision, Consequences sections | Grep for `## Context`, `## Decision`, `## Consequences` headings |

A `note` type has no structural requirements beyond frontmatter — this check only applies to more specific types.

### INFO-level Checks (signals — no action needed)

#### 11. Orphan Check (batch mode only)

Applies to: all types except `text`

| Check | Rule | How to Verify |
|-------|------|---------------|
| Inbound links | Note is referenced by at least one other note | Grep all notes for markdown links pointing to this file |

Only run in batch mode (`/validate all`). A note with no inbound links may be disconnected from the knowledge graph.

#### 12. Bare Note Type

Applies to: `note` only

| Check | Rule | How to Verify |
|-------|------|---------------|
| Unspecified structure | `type: note` with `traits: []` (empty list) | Check both fields |

A bare `note` with no traits is the honest default — but if it persists, it's a signal the note may benefit from type promotion or trait assignment. Report as INFO.

#### 13. Text File Count (batch mode only)

Applies to: batch validation

| Check | Rule | How to Verify |
|-------|------|---------------|
| Text file accumulation | Report total text file count | Count files without frontmatter |

Text files are unstructured captures — a growing count may signal the Collector's Fallacy. Report as INFO with the count and list of filenames.

#### 14. Seedling Status Count (batch mode only)

Applies to: batch validation

| Check | Rule | How to Verify |
|-------|------|---------------|
| Seedling accumulation | Report count of notes with `status: seedling` | Grep for `^status: seedling` in frontmatter |

Notes with `status: seedling` are structurally complete but not yet reviewed. A growing count signals a review backlog. Report as INFO with the count and list of filenames.

## Output Format (Single Note)

### Text file output:

```
=== VALIDATION: thought-about-trust.md ===

Type: text (no frontmatter)
Status: PASS — text files have no structural requirements

===
```

### Structured note output:

```
=== VALIDATION: note-title.md ===

Type: spec

PASS:
- frontmatter: valid delimiters, well-formed YAML
- description: present, 147 chars, adds mechanism beyond title
- type: "spec" — valid
- composability: title works as prose
- structure: Design and Implementation sections present

WARN:
- description: 38 chars — below recommended minimum of 50
- areas-topics: areas: [claw-design] set but no Topics: footer found
  → Run: uv run kb/scripts/sync_topic_links.py kb/notes/note-title.md

FAIL:
- (none)

INFO:
- (none)

Overall: PASS (2 warnings)
===
```

If WARN or FAIL items exist, include:

```
### Suggested Fixes
- **description**: Expand to ~50-200 chars — add mechanism, scope, or implication
- **areas-topics**: Run sync script to generate Topics footer from areas field
```

## Batch Mode

When validating all notes or recent notes:

1. Discover target `.md` files
2. Detect type for each file (text vs structured)
3. Run type-appropriate checks on each note
4. Run orphan check (INFO level) across the full set
5. Run text file count check
6. Produce summary report

**Batch output format:**

```
## Validation Summary

Checked: N files (M structured notes, K text files)
- PASS: M (X%)
- WARN: K (Y%)
- FAIL: J (Z%)

### Text Files (K files, no checks applied)
- thought-about-trust.md
- 2026-02-24-weird-idea.md

### FAIL Items (immediate attention)
| Note | Check | Detail |
|------|-------|--------|
| note-a.md | description | Missing |
| note-b.md | frontmatter | No closing delimiter |

### Top WARN Patterns
- Description quality (short/restates title): N notes
- Areas-Topics mismatch: N notes
- Invalid enum value: N notes

### INFO Signals
- Orphan notes (no inbound links): N notes
- Bare note type: N notes

### Notes Needing Attention
1. note-a.md — 2 FAIL, 1 WARN
2. note-b.md — 1 FAIL, 3 WARN
```

## Severity Levels

| Level | Meaning | Action |
|-------|---------|--------|
| PASS | Meets requirement fully | None needed |
| WARN | Quality issue or soft violation | Consider fixing |
| FAIL | Required field missing or structural error | Should fix |
| INFO | Informational signal | No action needed |

**FAIL does not block editing.** Validation is a quality check, not a gate. Notes can exist with failures — validation just surfaces what needs attention.

## Critical Constraints

**never:**
- modify any files (this skill is read-only)
- auto-fix issues — only report and suggest
- skip checks because the note "looks fine"
- report PASS without actually running the check
- use wiki-link syntax `[[...]]` — this KB uses standard markdown links

**always:**
- detect type before running checks — text files skip everything
- check ALL applicable schema requirements, not a subset
- report specific field values in FAIL/WARN messages (not just "description is weak")
- suggest concrete fixes for every WARN and FAIL
- resolve link paths relative to the note's directory
- handle subdirectories in `kb/notes/` (e.g., `research/`, `related-systems/`)
