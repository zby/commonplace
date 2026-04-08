# Installing Commonplace into a project

Commonplace can be installed into an existing project as a submodule or cloned subdirectory. This creates a two-tree layout: your content lives in `kb/` at the project root, while the framework lives in `commonplace/`. Operational artifacts (`types/`, `WRITING.md`) are copied into your `kb/` for fast access; methodology notes and promoted skills stay in `commonplace/` and are consulted on demand.

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
mkdir -p types kb/notes/types kb/sources/types kb/tasks/backlog kb/tasks/active kb/work kb/instructions

# Create the improvement log
touch kb/log.md

# Copy operational artifacts
cp commonplace/kb/instructions/WRITING.md kb/instructions/WRITING.md
cp commonplace/types/* types/
cp commonplace/kb/notes/types/index.md kb/notes/types/
cp commonplace/kb/notes/types/index.yaml kb/notes/types/
cp commonplace/kb/sources/types/source-review.md kb/sources/types/
cp commonplace/kb/sources/types/source-review.yaml kb/sources/types/
```

## 3. Configure your agent runtime

### Claude Code: install the plugin

```bash
claude plugin install ./commonplace
```

### Codex: register the plugin in a repo-local marketplace, then install it in `/plugins`

Create `.agents/plugins/marketplace.json` in the host project root:

```json
{
  "name": "local-commonplace",
  "interface": {
    "displayName": "Local Commonplace Plugins"
  },
  "plugins": [
    {
      "name": "commonplace",
      "source": {
        "source": "local",
        "path": "./commonplace"
      },
      "policy": {
        "installation": "AVAILABLE",
        "authentication": "ON_INSTALL"
      },
      "category": "Productivity"
    }
  ]
}
```

Then restart Codex, open it, run `/plugins`, choose `Local Commonplace Plugins`, and install `commonplace`.

This repo also ships its own repo-local Codex marketplace file at `.agents/plugins/marketplace.json` for dogfooding inside the `commonplace/` repo itself. That entry points to `./` because the repo root is the plugin directory.

If you change `.codex-plugin/plugin.json`, `skills/`, or the marketplace file, restart Codex again before reinstalling or retesting.

### Codex fallback: symlink framework skills manually

```bash
mkdir -p .agents/skills
for skill in commonplace/skills/*/; do
  name=$(basename "$skill")
  ln -sfn "$PWD/commonplace/skills/$name" ".agents/skills/$name"
done
```

### Claude Code fallback: symlink framework skills manually

```bash
mkdir -p .claude/skills
for skill in commonplace/skills/*/; do
  name=$(basename "$skill")
  ln -sfn "../../commonplace/skills/$name" ".claude/skills/$name"
done
```

### Optional: repo-local uv cache with `.envrc`

This repo includes a checked-in `.envrc` that sets `UV_CACHE_DIR` to `$PWD/tmp/uv-cache`. If you already use `direnv`, run `direnv allow` once after entering the repo so `uv run ...` uses the repo-local cache automatically instead of the default global cache path. If you do not use `direnv`, you can ignore this and set `UV_CACHE_DIR` some other way.

### Optional: set up qmd semantic search

If you use qmd, copy the sample config and then edit the paths manually:

```bash
cp commonplace/scripts/qmd-collections.yml ~/.config/qmd/my-project.yml
```

Open `~/.config/qmd/my-project.yml` and replace `/PATH/TO/COMMONPLACE/` with the absolute path to your project root, not the `commonplace/` subdirectory. The collections should point at your project's `kb/notes`, `kb/sources`, `kb/tasks`, and `kb/instructions`.

Then build the index:

```bash
qmd --index my-project update && qmd --index my-project embed
```

### Optional: install Codex skills globally

If you want the same promoted skills available across projects, you can also symlink them into `$CODEX_HOME/skills` (default `~/.codex/skills`). This is optional; project-local `.agents/skills/` is enough for one repository.

```bash
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$CODEX_HOME/skills"
for skill in commonplace/skills/*/; do
  name=$(basename "$skill")
  ln -sfn "$PWD/commonplace/skills/$name" "$CODEX_HOME/skills/$name"
done
```

## 4. Create your project's control-plane file

Copy the template and rename it for your agent runtime:

```bash
# Claude Code
cp commonplace/AGENTS.md.template CLAUDE.md

# Codex
cp commonplace/AGENTS.md.template AGENTS.md
```

The template includes KB discovery, structural search patterns, and the framework skill list. The one section you must fill in is **KB Goals**.

### Fill in the KB Goals section

Open the control-plane file and fill in the five subsections. The HTML comments in the template have examples — remove them when done.

**Purpose** — Name the decisions or actions the KB supports and who uses it. Start from the users, not the domain. "Supports the API team in making design decisions about the payment service" is actionable; "stores knowledge about payments" is not.

**Domain** — Draw a scope boundary specific enough that an agent can decide "does this belong?" without asking. Name adjacent domains and clarify whether they're in or out: "adjacent systems (auth, billing) are in scope only where they interact with payments."

**Include** — What types of knowledge belong: design decisions, failure analysis, integration patterns, operational procedures, etc.

**Exclude** — The most valuable section. Scope creep is the default failure mode — every piece of knowledge looks relevant in isolation. Name specific things that don't belong: "business rules live in the product wiki, not here." The Exclude list is what makes the Include list meaningful.

**Quality bar** — When is a piece of knowledge worth a note vs. a log entry vs. nothing? `WRITING.md` covers universal quality criteria (claim titles, descriptions, composability). This section adds domain-specific standards: "a design decision is worth a note when it affects more than one endpoint; single-endpoint details belong in code comments."

The Goals section is always-loaded — the agent sees it every session and uses it to decide whether knowledge belongs in this KB before deciding where it goes.

## Resulting layout

```
my-project/
  kb/                        Your content
    instructions/
      WRITING.md             Copied from commonplace
    log.md                   Improvement log (append-only)
    notes/
      types/                 Copied from commonplace
    sources/
    tasks/
    work/                    Workshop space — connect reports, ingest staging
  commonplace/               Framework (submodule or clone)
    skills/                  Framework skills
    kb/notes/                Methodology notes
  .claude/skills/            Optional fallback, Claude Code only; symlinked → commonplace/skills/
  .agents/plugins/
    marketplace.json         Codex local marketplace entry pointing to commonplace/
  .agents/skills/            Optional fallback, Codex only; symlinked → commonplace/skills/
  ~/.codex/skills/           Optional, Codex global skills; symlinked → commonplace/skills/
  CLAUDE.md                  Claude Code control-plane file
  AGENTS.md                  Codex control-plane file
```

## Updating

Pull new changes (`git submodule update --remote` or `cd commonplace && git pull`), then re-copy operational artifacts. Commonplace-provided type files are replaced; any custom types you've added are left untouched.

See `kb/notes/adr/006-two-tree-installation-layout.md` for the full design rationale.
