---
name: cp-skill-write
description: Write a KB artifact using the default note workflow or a discovered type template. Routes by type, reads WRITING.md, searches first, and validates after writing. Use with an optional type and optional topic.
user-invocable: true
allowed-tools: Read, Write, Grep, Glob, Bash, Skill
context: fork
model: opus
argument-hint: "[type] [topic] — optional type followed by an optional topic or title hint"
---

## EXECUTE NOW

**Target: $ARGUMENTS**

Parse arguments immediately:

- No arguments: write a default `note`
- One argument:
  - if it matches a known type, write that type
  - otherwise treat it as the topic and write a default `note`
- Multiple arguments:
  - if the first token matches a known type, use it as the type and treat the rest as the topic
  - otherwise treat the whole string as the topic and write a default `note`

Known built-in types:

- `note`
- `text`
- `index`
- `source-review`

If a non-built-in type is requested, scan `kb/*/types/` for `{type}.template.md`. If no matching template exists, stop and report the available types.

## Procedure

1. Search first.
Search `kb/notes/`, `kb/sources/`, and relevant indexes before writing. Read the closest matches so the new artifact does not duplicate existing work and can connect cleanly.

2. Load writing guidance.
Read `kb/instructions/WRITING.md` before drafting any frontmatter-based artifact.

3. Resolve the target type and destination.

- `note`:
  - destination: `kb/notes/`
  - template source: `kb/instructions/WRITING.md`
- `text`:
  - destination: `kb/notes/`
  - no frontmatter template
- `index`:
  - destination: `kb/notes/`
  - template source: `kb/notes/types/index.template.md`
  - instructions source: `kb/notes/types/index.instructions.md`
- `source-review`:
  - destination: `kb/sources/`
  - template source: `kb/sources/types/source-review.template.md`
  - instructions source: `kb/sources/types/source-review.instructions.md`
- any other discovered type:
  - read its template from `kb/*/types/{type}.template.md`
  - if present, also read `kb/*/types/{type}.instructions.md`
  - infer the target collection from the template path and the companion instructions

4. Draft the artifact.

- For `text`, write a raw markdown file with no frontmatter.
- For any typed artifact, follow the resolved template and the WRITING checklist.
- Use a lowercase hyphenated filename derived from the `# Title` heading.
- Set traits only when the content clearly warrants them:
  - `title-as-claim`
  - `definition`
  - `has-comparison`
  - `has-external-sources`
  - `has-implementation`

5. Save the file.
Create the file in the routed destination directory. If a topic was provided but no final title is obvious, choose the narrowest title that reflects the actual claim or subject of the draft.

6. Validate immediately.
Run the `cp-skill-validate` skill on the new file after writing. If validation finds structural issues, fix them before stopping.

7. Finish by prompting for connection work.
Tell the user where the file was written and suggest running the `cp-skill-connect` skill on the new file as the next step.

## Critical Constraints

**Always:**

- search before writing
- read `kb/instructions/WRITING.md` before drafting typed artifacts
- use the discovered type template when writing a specialized artifact
- validate the new file before stopping

**Never:**

- invent a specialized type when no template exists
- skip validation for typed artifacts
- force a claim title when the note is clearly exploratory or definitional
