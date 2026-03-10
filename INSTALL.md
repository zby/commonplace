# Installing Commonplace into a project

Commonplace can be installed into an existing project as a submodule or cloned subdirectory. This creates a two-tree layout: your content lives in `kb/` at the project root, while the framework lives in `commonplace/`. Operational artifacts (`types/`, `WRITING.md`) are copied into your `kb/` for fast access; methodology notes stay in `commonplace/` and are consulted on demand. Only promoted skills, represented as subdirectories under `commonplace/kb/instructions/`, are auto-discovered by agent runtimes. Plain instruction files remain on-demand procedures.

## 1. Add commonplace to your project

```bash
# Option A: git submodule (versioned, reproducible)
git submodule add https://github.com/anthropics/commonplace.git commonplace

# Option B: clone + gitignore (simpler)
git clone https://github.com/anthropics/commonplace.git commonplace
echo "commonplace/" >> .gitignore
```

## 2. Create the kb/ directory structure and copy operational artifacts

```bash
# Create directories
mkdir -p types kb/notes/types kb/sources/types kb/tasks/types kb/tasks/backlog kb/tasks/active kb/work

# Create the improvement log
touch kb/log.md

# Copy operational artifacts
cp commonplace/kb/instructions/WRITING.md kb/instructions/WRITING.md
cp commonplace/types/* types/
cp commonplace/kb/notes/types/* kb/notes/types/
cp commonplace/kb/sources/types/* kb/sources/types/
cp commonplace/kb/tasks/types/* kb/tasks/types/
```

## 3. Configure your agent runtime

### Claude Code: symlink skills into `.claude/skills/`

```bash
# Only promoted skills live in subdirectories; plain .md instructions are not symlinked.
mkdir -p .claude/skills
for skill in commonplace/kb/instructions/*/; do
  name=$(basename "$skill")
  ln -sfn "../../commonplace/kb/instructions/$name" ".claude/skills/$name"
done
```

### Codex: symlink skills into `.agents/skills`

```bash
# Only promoted skills live in subdirectories; plain .md instructions are not symlinked.
mkdir -p .agents/skills
for skill in commonplace/kb/instructions/*/; do
  name=$(basename "$skill")
  ln -sfn "$PWD/commonplace/kb/instructions/$name" ".agents/skills/$name"
done
```

Codex discovers promoted skills from the repository's `.agents/skills/`, but you should still add project routing in `AGENTS.md` so it knows when to read `kb/instructions/WRITING.md`, the relevant `kb/*/types/` file, when to invoke a plain instruction under `commonplace/kb/instructions/`, and when to escalate into `commonplace/kb/` for methodology.

### Optional: install Codex skills globally

If you want the same promoted skills available across projects, you can also symlink them into `$CODEX_HOME/skills` (default `~/.codex/skills`). This is optional; project-local `.agents/skills/` is enough for one repository.

```bash
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$CODEX_HOME/skills"
for skill in commonplace/kb/instructions/*/; do
  name=$(basename "$skill")
  ln -sfn "$PWD/commonplace/kb/instructions/$name" "$CODEX_HOME/skills/$name"
done
```

## 4. Add a Knowledge System section to your project's control-plane file

Add the same Knowledge System section to the file your agent runtime loads by default:

- Claude Code: `CLAUDE.md`
- Codex: `AGENTS.md`

Include a routing table, core search patterns, and escalation boundaries. See `kb/notes/commonplace-installation-architecture.md` for the full fragment design.

## Resulting layout

```
my-project/
  kb/                        Your content
    WRITING.md               Copied from commonplace
    log.md                   Improvement log (append-only)
    notes/
      types/                 Copied from commonplace
    sources/
    tasks/
    work/                    Workshop space — connect reports, ingest staging
  commonplace/               Framework (submodule or clone)
  .claude/skills/            Optional, Claude Code only; symlinked → commonplace/kb/instructions/
  .agents/skills/            Optional, Codex only; symlinked → commonplace/kb/instructions/
  ~/.codex/skills/           Optional, Codex global skills; symlinked → commonplace/kb/instructions/
  CLAUDE.md                  Optional, Claude Code control-plane file
  AGENTS.md                  Optional, Codex control-plane file
```

## Updating

Pull new changes (`git submodule update --remote` or `cd commonplace && git pull`), then re-copy operational artifacts. Commonplace-provided type files are replaced; any custom types you've added are left untouched.

See `kb/notes/commonplace-installation-architecture.md` for the full design rationale.
