# Installing Commonplace into a project

## Prerequisites

Add `.venv/bin` to your PATH so that project-local Python commands are available without activating the venv. Add this to your `~/.bashrc` or `~/.zshrc`:

```bash
export PATH=".venv/bin:$PATH"
```

Restart your shell or `source` the file. This is a one-time setup — it works for any project with a local `.venv/`.

## Project-local uv cache

Codex often runs inside a sandbox where the default uv cache location is not writable. The cleanest fix is to set `UV_CACHE_DIR` per project so both your normal shell and the shell Codex runs use the same writable cache.

Preferred: use `direnv`.

Create a project-local `.envrc`:

```bash
export UV_CACHE_DIR="$PWD/tmp/uv-cache"
```

Then allow it once:

```bash
direnv allow
```

This keeps the setting project-scoped instead of changing every shell on your machine.

If you use a project-local cache, add it to your gitignore if it is not already ignored:

```bash
echo "tmp/uv-cache/" >> .gitignore
```

Fallback for Codex-only behavior: set it in `~/.codex/config.toml` so Codex injects it into the shell it launches:

```toml
[shell_environment_policy]
inherit = "all"

[shell_environment_policy.set]
UV_CACHE_DIR = ".uv-cache"
```

Last-resort fallback: export it from your shell startup file (`~/.bashrc` or `~/.zshrc`), but that is global rather than project-specific:

```bash
export UV_CACHE_DIR="${UV_CACHE_DIR:-.uv-cache}"
```

## 1. Create a project venv and install the package

From your project root:

```bash
uv venv
uv pip install llm-commonplace
```

Or without uv:

```bash
python3 -m venv .venv
pip install llm-commonplace
```

Or from a local checkout:

```bash
uv venv
uv pip install -e /PATH/TO/commonplace
```

## 2. Initialize the local KB layout

```bash
commonplace-init
```

That creates the standard local tree and seeds it with instructions, review gates, type definitions, and a starter `AGENTS.md.template`:

- `kb/notes/`
- `kb/sources/`
- `kb/tasks/`
- `kb/work/`
- `kb/reports/`
- `kb/instructions/` (seeded with writing conventions, review system, gates, fix instructions)
- `types/` (seeded with note and text type definitions)
- `kb/log.md`
- `AGENTS.md.template`

Rerunning `commonplace-init` is safe — it never overwrites existing files.

## 3. Create your control-plane file

Copy the seeded template and rename it for your runtime:

```bash
cp AGENTS.md.template CLAUDE.md
# or
cp AGENTS.md.template AGENTS.md
```

Then fill in the `KB Goals` section for your project.

Skills (write, validate, snapshot, connect, etc.) are installed automatically by `commonplace-init` into `.claude/skills/` with a `commonplace-` prefix. No separate plugin install is needed.

## Resulting layout

```text
my-project/
  .venv/
  .claude/
    skills/
      commonplace-write/
      commonplace-validate/
      commonplace-connect/
      commonplace-snapshot-web/
      ...
  kb/
    notes/
    sources/
    tasks/
    work/
    reports/
    instructions/
    log.md
  types/
  CLAUDE.md
```

## Optional: qmd semantic search

Copy the sample config:

```bash
commonplace-init-qmd  # not yet implemented — copy manually for now
cp /PATH/TO/commonplace/src/commonplace/assets/qmd-collections.yml ~/.config/qmd/my-project.yml
```

Edit `~/.config/qmd/my-project.yml` and replace `/PATH/TO/COMMONPLACE/` with the absolute path to your project root.

Then build the index:

```bash
qmd --index my-project update && qmd --index my-project embed
```

## Updating

Update the package in your project venv:

```bash
uv pip install --upgrade llm-commonplace
```

Rerun init to pick up any new scaffold files (existing files are preserved):

```bash
commonplace-init
```
