# Instructions

`kb/instructions/` is the searchable home for reusable procedures in this repo.

It contains three kinds of artifacts:

- Plain instructions: markdown procedures invoked manually from the KB
- Local skills: instruction subdirectories containing `SKILL.md` that are used inside this repo but are not installed by `commonplace-init`
- Promoted skills: instruction subdirectories containing `SKILL.md` that `commonplace-init` copies into runtime skill directories

## Warning: Promoted Skills Run From A Different Path

Promoted skills are **not executed from `kb/instructions/`**. `commonplace-init` copies selected instruction directories into:

- `.claude/skills/cp-skill-<name>/`
- `.agents/skills/cp-skill-<name>/`

The copies keep the same file contents, but the runtime path is different. That means promoted skills must not rely on their own on-disk location being `kb/instructions/<name>/`.

When writing or editing a promoted skill:

- Prefer stable workspace-root paths in prose and commands, such as `kb/notes/`, `kb/notes/COLLECTION.md`, and `kb/types/`
- Do not assume markdown-relative links inside the skill will resolve from the runtime copy
- Treat `kb/instructions/` as the searchable source surface, and the runtime skill directories as compiled copies

## Promotion Convention

To promote an instruction into a runtime skill:

1. Put it in `kb/instructions/<name>/SKILL.md`
2. Add `<name>` to `MANIFEST.promoted_skills` in `src/commonplace/scaffold_manifest.py`
3. Keep any auxiliary files in the same directory so `commonplace-init` copies them with the skill

Not every instruction subdirectory is promoted. Local-only skills stay in `kb/instructions/<name>/SKILL.md` and may be symlinked directly into this repo's `.claude/skills/` and `.agents/skills/` surfaces without adding them to `PROMOTED_SKILLS`. The explicit `MANIFEST.promoted_skills` list consumed by `commonplace-init` is the source of truth for what gets copied into runtime skill surfaces.
