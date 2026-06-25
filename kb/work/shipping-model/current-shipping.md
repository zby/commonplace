# Current shipping surface

Inventory of what `commonplace-init` produces in a user's project today, as the starting point for the shipping-model workshop. Snapshotted 2026-04-23 from [`src/commonplace/cli/init_project.py`](../../../src/commonplace/cli/init_project.py).

## Scaffold trees

Six trees copied verbatim from `src/commonplace/_data/` to target paths in the user's project:

| Source (scaffold package) | Target (user project) | What's in it |
|---|---|---|
| `kb/instructions` | `kb/instructions` | 27 files with methodology + procedures; cp-skill-* SKILL.md files |
| `kb/notes` | `kb/notes` | 187 files of agent-KB methodology theory |
| `kb/reference` | `kb/reference` | Shipped-system documentation + ADRs |
| `kb/reports/types` | `kb/reports/types` | Type definitions for report artifacts |
| `kb/sources/types` | `kb/sources/types` | Type definitions for source captures |
| `kb/types` | `kb/types` | Top-level type definitions |

All target paths are **identical** to source paths. The user's tree and ours share the namespace.

## Default directories

Created if missing, regardless of scaffold content:

```
kb/types
kb/notes
kb/notes/types
kb/reference
kb/reference/types
kb/sources
kb/sources/types
kb/tasks/backlog
kb/tasks/active
kb/tasks/completed
kb/work
kb/instructions
kb/reports
kb/reports/connect
kb/reports/types
```

Observation: `kb/sources/`, `kb/tasks/`, `kb/work/`, `kb/reports/` (not the types subdir) are created empty — these are user-space from day one. `kb/notes/`, `kb/reference/`, `kb/instructions/` are created then scaffolded — mixed user/shipped.

## Promoted skills (symlinks)

Eight skills are symlinked from `kb/instructions/<name>/` into both `.claude/skills/<name>` and `.agents/skills/<name>`:

- `cp-skill-write`
- `cp-skill-validate`
- `cp-skill-connect`
- `cp-skill-convert`
- `cp-skill-ingest`
- `cp-skill-snapshot-web`
- `cp-skill-revise-iterative`
- `cp-skill-revise-autoreason`

These symlinks resolve to the scaffolded copy of the skill in the user's `kb/instructions/`.

## Templates

Two template files with placeholder substitution (`<your-project>`, `{{project_name}}`, `/PATH/TO/COMMONPLACE/`):

- `AGENTS.md.template` → `AGENTS.md.template` (user renames to `AGENTS.md`)
- `.envrc.template` → `.envrc`

## Hardcoded path references in shipped content

Grep over `kb/instructions/` for `kb/notes|kb/reference|kb/instructions` returns **85 occurrences across 27 files**. Representative call-sites:

| File | Count |
|---|---|
| `REVIEW-SYSTEM.md` | 8 |
| `example-onboard-second-brain.md` | 11 |
| `COLLECTION.md` | 7 |
| `README.md` | 6 |
| `FIX-SYSTEM.md` | 6 |
| `write-instruction.md` | 4 |
| `evaluate-scenarios/SKILL.md` | 4 |
| `cp-skill-connect/SKILL.md` | 4 |
| `cp-skill-convert/SKILL.md` | 4 |

Not yet audited: `kb/notes/` and `kb/reference/` shipped content. Internal links between notes use relative paths (`./` or `../`) and would survive a tree-level move; cross-collection references (e.g. a note citing `kb/reference/adr/...`) are the translation-sensitive population.

## Immediate implications for the namespacing decision

- Of the 85 hardcoded `kb/{notes,reference,instructions}/` references in shipped instructions, only a subset needs translation: references to specific shipped artifacts (e.g. `kb/reference/adr/010-...md`, `kb/instructions/run-review-batches-on-note.md`). Generic references ("a collection such as `kb/notes/`", "read `kb/<collection>/COLLECTION.md`") resolve correctly to the user's own collection and need no change. An audit is needed to split the 85 into these categories.
- The `PROMOTED_SKILLS` list points at `kb/instructions/<name>/` — if shipped instructions move to `kb/cp-instructions/<name>/` or `kb/commonplace/instructions/<name>/`, the symlink target path in `init_project.py:206` needs updating.
- `DEFAULT_DIRS` needs reshaping: create empty user collections at top-level, create the shipped hierarchy separately.
- `AGENTS.md.template` likely references library paths that would need translation. Not audited yet.
