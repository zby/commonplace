# Installing Commonplace into a project

## 1. Install the Python package

```bash
uv pip install llm-commonplace
# or
pip install llm-commonplace
```

Or from a local checkout:

```bash
uv pip install -e /PATH/TO/commonplace
```

## 2. Initialize the local KB layout

From the project root:

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

## 4. Install the plugin (optional)

The Commonplace plugin provides skills (write, validate, snapshot, review, etc.) to your agent runtime.

### Claude Code

```bash
claude plugin install /PATH/TO/commonplace
```

### Codex

Create a host-project marketplace entry in `.agents/plugins/marketplace.json` that points at the plugin source, then restart Codex and install `commonplace` from `/plugins`.

> **Note:** Plugin distribution without a local checkout is not yet supported. For now, plugin installation still requires a path to a Commonplace checkout or a locally available plugin directory.

## Resulting layout

```text
my-project/
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

Update the package:

```bash
uv pip install --upgrade llm-commonplace
# or
pip install --upgrade llm-commonplace
```

Rerun init to pick up any new scaffold files (existing files are preserved):

```bash
commonplace-init
```
