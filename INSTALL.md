# Installing Commonplace into a project

## Prerequisites

Add `.venv/bin` to your PATH so that project-local Python commands are available without activating the venv. Add this to your `~/.bashrc` or `~/.zshrc`:

```bash
export PATH=".venv/bin:$PATH"
```

Restart your shell or `source` the file. This is a one-time setup — it works for any project with a local `.venv/`.

## Codex: uv cache configuration

Codex often runs inside a sandbox where the default uv cache location is not writable. Set `UV_CACHE_DIR` to a writable directory inside the project so `uv run`, `uv pip`, and related commands work without escalation.

Preferred: set it in Codex config so it is injected into the shell Codex runs.

Add this to `~/.codex/config.toml`:

```toml
[shell_environment_policy]
inherit = "all"

[shell_environment_policy.set]
UV_CACHE_DIR = ".uv-cache"
```

If you already configure Codex globally in `~/.codex/config.toml` for things like `model`, this is the most direct place to add the cache override as well.

Fallback: add it to the shell startup file used by the shell Codex launches (`~/.bashrc` for `bash`, `~/.zshrc` for `zsh`):

```bash
export UV_CACHE_DIR="${UV_CACHE_DIR:-.uv-cache}"
```

Then restart Codex or start a new shell so the variable is present in the shell Codex runs.

For the current shell only, you can also set it manually:

```bash
export UV_CACHE_DIR=.uv-cache
```

If you use a repo-local cache, add it to your gitignore:

```bash
echo ".uv-cache/" >> .gitignore
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
