# Installing Commonplace into a project

Commonplace can be installed into an existing project as a submodule or cloned subdirectory. This creates a two-tree layout: your content lives in `kb/` at the project root, while the framework lives in `commonplace/`. Operational artifacts (`types/`, `WRITING.md`) are copied into your `kb/` for fast access; methodology notes stay in `commonplace/` and are consulted on demand.

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
cp commonplace/kb/WRITING.md kb/WRITING.md
cp commonplace/types/* types/
cp commonplace/kb/notes/types/* kb/notes/types/
cp commonplace/kb/sources/types/* kb/sources/types/
cp commonplace/kb/tasks/types/* kb/tasks/types/
```

## 3. Symlink skills into `.claude/skills/`

```bash
mkdir -p .claude/skills
for skill in commonplace/skills/*/; do
  name=$(basename "$skill")
  ln -sfn "../../commonplace/skills/$name" ".claude/skills/$name"
done
```

## 4. Add a Knowledge System section to your project's `CLAUDE.md`

Include a routing table and search patterns. See `kb/notes/commonplace-installation-architecture.md` for the full fragment design.

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
  .claude/skills/            Symlinked → commonplace/skills/
  CLAUDE.md                  Routing table + commonplace reference
```

## Updating

Pull new changes (`git submodule update --remote` or `cd commonplace && git pull`), then re-copy operational artifacts. Commonplace-provided type files are replaced; any custom types you've added are left untouched.

See `kb/notes/commonplace-installation-architecture.md` for the full design rationale.
