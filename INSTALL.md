# Installing Commonplace into a project

## Prerequisites

- **Python 3.11+** (required)
- **uv** (required, recommended) or pip
- **git** (required)
- **direnv** (optional, recommended on Linux/macOS) — for project-scoped environment variables
- **ripgrep** (required) — used by agent runtimes for fast KB search
- **An agent runtime** — Codex, Claude Code, or another internal LLM/IDE that can load a project control-plane file and expose skill/procedure directories to the agent.

## Start-time contract

Commonplace is usable when the terminal or agent runtime starts inside the project with this state:

- **Project root is the working directory** — relative paths like `kb/notes` resolve to this project.
- **The project venv is the active command environment** — `commonplace-*` commands resolve from the project-local `.venv`, not from a global install or another project.
- **Commands run by bare name** — agents can call `commonplace-validate`, `commonplace-init`, and other Commonplace commands without prepending `.venv/bin/`, `.venv\Scripts\`, `uv run`, or `direnv exec`.
- **The control-plane file is present** — `AGENTS.md` or `CLAUDE.md` contains the project KB goals, routing rules, and command invocation rule.
- **Runtime skills are discoverable by the active agent** — the `cp-skill-*` skill bodies from `kb/commonplace/instructions/` are installed, linked, copied, or registered in whatever skill directory or plugin surface the active agent runtime actually reads.
- **Shipped Commonplace collections are present** — `kb/commonplace/notes/`, `kb/commonplace/reference/`, and `kb/commonplace/instructions/` exist and contain the reusable methodology library.
- **Search works** — `rg` is available for fast KB search.

The concrete shell commands below are examples of ways to satisfy this contract. Linux/macOS usually satisfies it with direnv. Windows usually satisfies it by activating `.venv` in PowerShell or `cmd` before starting the agent runtime. If your company runtime does not automatically read `AGENTS.md` or `CLAUDE.md`, configure it to load the control-plane file as project instructions before starting work.

Acceptance checks:

```bash
pwd
command -v commonplace-validate  # should print a path under $PWD/.venv/bin/
commonplace-init --help
commonplace-validate kb/commonplace/reference/commands.md
rg "^description:" kb/commonplace/notes kb/commonplace/reference kb/commonplace/instructions --glob "*.md"
```

Windows PowerShell equivalents:

```powershell
Get-Location
(Get-Command commonplace-validate).Source  # should print a path under .venv\Scripts
commonplace-init --help
commonplace-validate kb\commonplace\reference\commands.md
rg "^description:" kb\commonplace\notes kb\commonplace\reference kb\commonplace\instructions --glob "*.md"
```

### Check prerequisites

Run these checks before proceeding. If any required tool is missing, ask the user to install it before continuing.

Linux/macOS:

```bash
python3 --version   # must be 3.11+
uv --version        # or: pip --version
git --version
```

Windows PowerShell:

```powershell
py -3 --version     # must be 3.11+
uv --version        # or: py -3 -m pip --version
git --version
```

Optional on Linux/macOS:

```bash
direnv version
```

On Windows, skip `direnv version` unless you have deliberately installed direnv through WSL, Git Bash, or another Unix-like shell. Check ripgrep with:

```powershell
rg --version
```

## 1. Create a project venv and install the package

Commonplace installs into a project-local venv rather than globally, so each project can pin its own version independently.

> **Note:** `llm-commonplace` is not yet published to PyPI. For now, install from a local checkout of this repository. The PyPI-based instructions below are kept as a preview of how it will work once published.

From your project root, install from a local checkout (also works if you're inside the Commonplace repo itself):

Linux/macOS:

```bash
uv venv
uv pip install -e /PATH/TO/commonplace
# or, if you're already in the commonplace directory:
uv pip install -e .
```

Windows PowerShell:

```powershell
uv venv
uv pip install -e C:\path\to\commonplace
# or, if you're already in the commonplace directory:
uv pip install -e .
```

Once the package is published, this will become:

```bash
uv venv
uv pip install llm-commonplace
```

Or without uv:

Linux/macOS:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install llm-commonplace
```

Windows PowerShell:

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install llm-commonplace
```

## 2. Initialize the project

With uv:

```bash
uv run commonplace-init --name <your-project>
```

Use `uv run` here because the venv may not be on `PATH` yet.

Without uv, activate the venv first, then run the command by bare name:

Linux/macOS:

```bash
. .venv/bin/activate
commonplace-init --name <your-project>
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
commonplace-init --name <your-project>
```

After step 3, `commonplace-*` commands work directly in shells and agent runtimes that have loaded the project environment.

`commonplace-init` creates convenience skill symlinks for the known `.claude/skills/` and `.agents/skills/` layouts. These are not the whole skill contract; other IDEs and agent runtimes may use different locations. If symlink creation is unavailable on Windows, init still creates the canonical `kb/commonplace/instructions/cp-skill-*` directories and reports the optional skill projections as skipped; use the runtime-specific skill installation procedure in step 4.

```powershell
uv run commonplace-init --name <your-project>
```

The `--name` flag sets the project name used in templates. If omitted, it defaults to the directory name.

This creates:

- **User KB directories** — `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/sources/`, `kb/tasks/`, `kb/work/`, `kb/reports/`, `kb/log.md`
- **Commonplace library content** — shipped notes, reference docs, instructions, review gates, and skills under `kb/commonplace/notes/`, `kb/commonplace/reference/`, and `kb/commonplace/instructions/`
- **Type definitions** — shared types under `kb/types/`, plus source/report type scaffolds
- **Canonical skills** — `kb/commonplace/instructions/cp-skill-write/`, plus the matching `cp-skill-validate/`, `cp-skill-connect/`, etc. The `cp-skill-` prefix avoids collisions with your project's own skills and with the `commonplace-*` CLI commands.
- **Known runtime skill projections** — `.claude/skills/cp-skill-*/` and `.agents/skills/cp-skill-*/` symlinks, when the platform permits them
- **`.envrc`** — project-scoped Unix-shell environment (PATH, UV_CACHE_DIR), ready to use with direnv on Linux/macOS
- **`AGENTS.md.template`** — control-plane template with project name filled in

Rerunning `commonplace-init` is safe — it never overwrites existing files, so you can rerun after a package upgrade to pick up new scaffold files. The command now reports which preserved files already match the current scaffold and which ones were left untouched because they differ from what the current run would generate.

## 3. Load the project environment

CLI commands live in `.venv/bin/` on Linux/macOS and `.venv\Scripts\` on Windows. Any loader is acceptable if it satisfies the start-time contract above: Commonplace commands resolve by bare name from the project-local venv.

This matters for agent runtimes: if Codex or Claude Code is started from a desktop launcher, service, wrapper script, or another non-interactive environment, it may not inherit the project `PATH`.

### Linux/macOS with direnv (recommended)

The generated `.envrc` adds `.venv/bin` to `PATH` through direnv, so commands work without manual venv activation. It also sets `UV_CACHE_DIR` to avoid permission issues in sandboxed runtimes like Codex.

direnv only loads `.envrc` automatically when your shell has the direnv hook installed and the project directory is entered from that hooked shell.

Install the shell hook once if it is not already present:

```bash
# bash
echo 'eval "$(direnv hook bash)"' >> ~/.bashrc

# zsh
echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc
```

Restart your shell, enter the project directory, and allow the generated `.envrc`:

```bash
cd /path/to/your-project
direnv allow
```

You should see a `direnv: loading ...` message, and `commonplace-*` commands should resolve from the project venv:

```bash
command -v commonplace-validate
```

When using Codex, start it from that same direnv-loaded interactive shell:

```bash
cd /path/to/your-project
codex
```

If Codex is launched from a non-interactive wrapper, wrap the launch explicitly:

```bash
direnv exec /path/to/your-project codex
```

For one-off commands in an environment where the hook has not loaded, use:

```bash
direnv exec . bash -c 'commonplace-validate kb/commonplace/reference/commands.md'
```

Add the cache and venv directories to `.gitignore`:

```bash
echo -e ".uv-cache/\n.venv/" >> .gitignore
```

### Windows PowerShell

Example: activate the project venv before running Commonplace commands or starting an agent runtime:

```powershell
cd C:\path\to\your-project
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation because script execution is restricted, allow locally signed scripts for your user account, then activate again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

Verify that the start-time contract is satisfied:

```powershell
Get-Command commonplace-validate
```

Start the agent runtime from that same activated terminal. For Codex this is:

```powershell
codex
```

For Claude Code or an internal IDE/LLM, use the runtime's normal launch command from this activated shell, or configure the IDE's integrated terminal/service environment so `.venv\Scripts` is on `PATH`.

For one-off human commands without activating the terminal first, call the venv executable explicitly. Do not put this form in the control-plane file unless the project has deliberately chosen not to satisfy the bare-command contract:

```powershell
.\.venv\Scripts\commonplace-validate.exe kb\commonplace\reference\commands.md
```

Add the cache and venv directories to `.gitignore`:

```powershell
@(".uv-cache/", ".venv/") | Add-Content .gitignore
```

### Windows cmd

Example:

```bat
cd C:\path\to\your-project
.venv\Scripts\activate.bat
where commonplace-validate
codex
```

### Linux/macOS without direnv

Example: add `.venv/bin` to your PATH globally in `~/.bashrc` or `~/.zshrc`:

```bash
export PATH=".venv/bin:$PATH"
```

This uses a relative path, so it resolves to whichever project directory you're in. Restart your shell or `source` the file.

## 4. Install runtime skills

Commonplace's source of truth for shipped skills is:

```text
kb/commonplace/instructions/cp-skill-*/
```

Each active agent runtime must expose those directories through its own skill discovery mechanism. `commonplace-init` creates symlink projections for two common layouts when the platform permits them:

```text
.claude/skills/cp-skill-*/ -> ../../kb/commonplace/instructions/cp-skill-*/
.agents/skills/cp-skill-*/ -> ../../kb/commonplace/instructions/cp-skill-*/
```

If your runtime uses one of those layouts and symlinks are available, no further work is needed. If your runtime uses a different directory, install the same `cp-skill-*` directories there in the way that runtime expects: symlink, junction, copy, plugin registration, IDE-specific import, or whatever internal extension mechanism exposes reusable instructions to the model.

For an agent doing the installation: inspect your own runtime's skill-discovery rules, then project every `kb/commonplace/instructions/cp-skill-*` directory into that surface. Prefer links or runtime registration when available so updates to `kb/commonplace/instructions/` are visible after rerunning `commonplace-init`; copy only when the runtime or platform cannot follow links.

Acceptance check: from inside the agent runtime, confirm that these skills are available by their `cp-skill-*` names:

```text
cp-skill-write
cp-skill-validate
cp-skill-connect
cp-skill-health-check
```

## 5. Set up the control-plane file

The control-plane file (`CLAUDE.md` or `AGENTS.md`) must be loaded by the agent runtime. It tells the agent what the KB is for, where to find things, and which skills are available. Codex and Claude-style runtimes usually load these files automatically from the project root; internal runtimes may need an explicit project-instructions setting, plugin configuration, or prompt import.

**New project** — rename the template:

```bash
mv AGENTS.md.template CLAUDE.md
# or
mv AGENTS.md.template AGENTS.md
```

**Existing project with a CLAUDE.md or AGENTS.md** — append the template to your existing file:

```bash
cat AGENTS.md.template >> CLAUDE.md
```

Then review the merged file and fill in the per-project parts. The template's HTML comments mark every spot, but the load-bearing ones are:

- **`KB Goals and Scope`** — Purpose, Scope (the out-of-scope list is what prevents scope creep), and Quality bar. Without these the agent has no basis for inclusion decisions.
- **Command invocation (in `### Commands`)** — keep the variant that matches the project's start-time contract. The preferred contract is bare-name invocation with the venv command directory on `PATH` (`.venv/bin` through direnv or shell rc on Linux/macOS, `.venv\Scripts` through activation on Windows). If the project deliberately does not put the venv on `PATH`, keep the fallback variant that tells agents to invoke the venv executables directly — `.venv/bin/commonplace-validate` on Linux/macOS or `.venv\Scripts\commonplace-validate.exe` on Windows — otherwise agents will retry failing bare commands.
- **Navigation entry points** — add curated tag READMEs to the list as they emerge; the comment in the template explains when to create one.

## 6. Verify validation and search

Commonplace works with curated indexes and `rg`; no semantic-search daemon is required, and complete generated listings are built only for the published site (never committed).

```bash
commonplace-validate kb/commonplace/reference/commands.md
rg "^description:" kb/commonplace/notes kb/commonplace/reference kb/commonplace/instructions --glob "*.md"
rg "your search terms" kb/ --glob "*.md"
```

A fresh project may have no user notes yet, so `commonplace-validate kb/notes` can report that no notes matched. Run it after the first user note exists.

## 7. Pre-approve Commonplace CLI commands in Claude Code (optional)

If you use Claude Code, you can skip the permission prompt for each `commonplace-*` command by adding prefix-wildcard allow rules to `.claude/settings.local.json` (user-local, gitignored). Add one `Bash(<name>:*)` entry for each `[project.scripts]` entry in `pyproject.toml`, e.g.:

```json
{
  "permissions": {
    "allow": [
      "Bash(commonplace-validate:*)",
      "Bash(commonplace-relocate-note:*)"
    ]
  }
}
```

Prefer `.claude/settings.local.json` over `.claude/settings.json` so the approvals stay local and don't get committed for other contributors.

## Resulting layout

```text
my-project/
  .venv/
  .envrc
  .claude/
    skills/
      cp-skill-write/
      cp-skill-validate/
      cp-skill-connect/
      cp-skill-snapshot-web/
      ...
  kb/
    types/
    notes/
    reference/
    instructions/
    sources/
    tasks/
    work/
    reports/
    commonplace/
      notes/
      reference/
      instructions/
    log.md
  CLAUDE.md
```

## Updating

Until `llm-commonplace` is on PyPI, update by pulling the latest Commonplace checkout — an editable install (`uv pip install -e`) picks up the changes automatically. Once published, you'll be able to upgrade with:

```bash
uv pip install --upgrade llm-commonplace
```

Rerun init to pick up any new scaffold files (existing files are preserved):

```bash
commonplace-init
```
