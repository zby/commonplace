# Instructions

`kb/instructions/` is the searchable home for reusable procedures in this repo.

It contains three kinds of artifacts:

- Plain instructions: markdown procedures invoked manually from the KB
- Local skills: instruction subdirectories containing `SKILL.md` that are used inside this repo but are not delivered to projects by `commonplace-init`
- Promoted skills: instruction subdirectories containing `SKILL.md` that `commonplace-init` makes discoverable in installed projects

## Promoted skills run in place

A promoted skill always runs from its own directory in the Commonplace library: `kb/instructions/<name>/` in this checkout, and `instructions/<name>/` under the installed library in a project. The installed library mirrors this repository's `kb/` layout. In a project, `commonplace-init` writes a stub for each promoted skill into:

- `.claude/skills/cp-skill-<name>/`
- `.agents/skills/cp-skill-<name>/`

The stub carries the skill's frontmatter and tells the agent to read the real `SKILL.md` by absolute path and follow it. It holds none of the skill's text. In this checkout, `.claude/skills/` and `.agents/skills/` hold committed relative symlinks to the same directories instead.

Because the agent reads the skill at its real location, relative links resolve the same way in both places. When writing or editing a promoted skill:

- Link to the skill's own files, to other instructions, and to types with ordinary relative links, such as `../re-ingest.md` or `../../types/note.md`
- Name the project's own collections by workspace-root paths, such as `kb/notes/` and `kb/notes/COLLECTION.md`; those are paths in the project, not in the library
- Name a type by its path under a KB root, such as `type: types/note.md`
- Do not branch the text between a source checkout and an installed project; the two layouts agree

## Promotion Convention

To promote an instruction into a runtime skill:

1. Put it in `kb/instructions/<name>/SKILL.md`
2. Add `<name>` to `promoted_skills` in `src/commonplace/scaffold_manifest.py`
3. Keep any auxiliary files in the same directory or link them relatively; the whole library ships, so nothing needs to be copied with the skill
4. Add relative symlinks for it under this repo's `.claude/skills/` and `.agents/skills/`

Not every instruction subdirectory is promoted. Local-only skills stay in `kb/instructions/<name>/SKILL.md` and may be symlinked directly into this repo's `.claude/skills/` and `.agents/skills/` surfaces without being listed in the manifest. The `promoted_skills` list in the scaffold manifest, together with its `router_skill` (`cp-skill-library`), is the source of truth for which skills installed projects receive stubs for.
