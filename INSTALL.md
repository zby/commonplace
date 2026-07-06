# Installing Commonplace into a project

Two installs, by what you want from it:

- **Reader install** — vendor the Commonplace knowledge base inside an existing project as a read-only reference: your agents consult the research when they face context, memory, or learning design decisions. A vendored copy (submodule, clone, or plain download) and one routing paragraph; no Python — the KB is plain markdown, so it works in a project written in any language. See [Reader install](#reader-install-the-kb-as-a-vendored-reference).
- **Full install** — run your own knowledge base with the Commonplace type system, skills, and commands. The package carries the methodology — notes, reference docs, instructions, types, and skills — but not this repo's external-system reviews (`kb/agent-memory-systems/`, `kb/agentic-systems/`) or source snapshots. The numbered steps below: check prerequisites, install the library so `commonplace-*` commands run, create the project with `commonplace-init`, set up the control-plane file, install the skills for every agent that will work on the project, and start the runtime. Most steps end with a check you can run before moving on.

## Reader install: the KB as a vendored reference

Vendor this repository **inside** your project root — placement is load-bearing, not cosmetic: agent harnesses scope file access to the project root, so a sibling directory costs a permission prompt in every session, while a subdirectory is readable with none.

As a submodule (pins a commit; every teammate and CI gets the same version, and updates are deliberate, reviewable bumps):

```bash
git submodule add https://github.com/zby/commonplace commonplace
```

Or as a gitignored clone (zero ceremony; each machine clones its own):

```bash
git clone https://github.com/zby/commonplace
echo '/commonplace/' >> .gitignore
```

Git itself is optional — the KB is plain files, so [downloading the repo as an archive](https://github.com/zby/commonplace/archive/refs/heads/main.zip) and extracting it into `commonplace/` works too; you just update by re-downloading.

Then paste a routing block into your project's `CLAUDE.md` or `AGENTS.md` (create the file if the project has none):

```markdown
## Knowledge base (vendored, read-only)

`commonplace/kb/` is a vendored knowledge base on agent context engineering,
memory, and deploy-time learning. For design decisions in those areas, consult
it before deciding: start at `commonplace/kb/notes/tags-README.md`. Paths named
inside it are relative to `commonplace/`. It is read-only in this project — to
contest a claim, open an issue at https://github.com/zby/commonplace/issues.
```

That's the whole install. Reading needs no Python, no venv, and no skills — the `commonplace-*` commands and `cp-skill-*` skills exist to maintain a KB, not to consume one. The one tool the KB's navigation leans on is ripgrep (`rg`), which most agent runtimes bundle. The vendored repo's own `AGENTS.md` tells agents that wander into it to treat it as read-only.

### Check the reader install

```bash
rg "^description:" commonplace/kb/notes/ --glob "*.md" | head
```

Then ask your agent a design question in the KB's domain — "should our agent memory get vector retrieval, or navigation structure first?" — and check the answer cites notes from `commonplace/kb/`.

### Updating the vendored KB

```bash
git -C commonplace pull                        # gitignored clone
git submodule update --remote commonplace      # submodule
```

### Keeping it small (optional)

If repository weight matters, a blobless, kb-only checkout works — root files such as `AGENTS.md` remain present:

```bash
git clone --filter=blob:none --sparse https://github.com/zby/commonplace
git -C commonplace sparse-checkout set kb
```

## 1. Prerequisites

### Required

- **Python 3.11+**
- **uv** (recommended) or **pip**
- **git**
- **ripgrep** (`rg`) — agent runtimes use it for fast KB search
- **An agent runtime** — Codex, Claude Code, or another LLM/IDE that can load a project control-plane file (`AGENTS.md`/`CLAUDE.md`) and expose skill directories to the agent

### Optional

- **direnv** (Linux/macOS) — optional convenience: auto-activates the project venv on `cd` and keeps uv's cache inside the project. Not needed for a working install; see the [direnv appendix](#appendix-direnv-linuxmacos). The main steps below use plain venv activation.

### Check prerequisites

If any required tool is missing, install it before continuing.

Linux/macOS:

```bash
python3 --version   # must be 3.11+
uv --version        # or: pip --version
git --version
rg --version
direnv version      # optional
```

Windows PowerShell:

```powershell
py -3 --version     # must be 3.11+
uv --version        # or: py -3 -m pip --version
git --version
rg --version
```

## 2. Install the library and make the commands work

The requirement is simply that the `commonplace-*` commands are installed and resolvable in the environment that runs your agent runtime — the shell you launch a command-line runtime (Codex, Claude Code) from, or whatever environment an IDE like Cursor opens the project in. A **project-local venv** is the recommended way to satisfy that, because each project can pin its own version independently; a global or shared install works too, as long as the commands end up on `PATH` where the agent actually runs. The rest of this guide uses a project-local venv. From your project root — create the directory and `cd` into it first if this is a new project:

Linux/macOS:

```bash
uv venv
uv pip install llm-commonplace
```

Windows PowerShell:

```powershell
uv venv
uv pip install llm-commonplace
```

Without uv:

```bash
# Linux/macOS
python3 -m venv .venv
. .venv/bin/activate
pip install llm-commonplace
```

```powershell
# Windows PowerShell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install llm-commonplace
```

For Commonplace development or local contribution work, install from a checkout instead:

```bash
uv pip install -e /PATH/TO/commonplace
```

### Make `commonplace-*` resolve by bare name

The install puts the `commonplace-*` executables in `.venv/bin/` (Linux/macOS) or `.venv\Scripts\` (Windows), but they are not on your `PATH` yet, so bare-name calls fail. Activate the venv so agents and shells can call `commonplace-validate`, `commonplace-init`, and the rest by bare name. Activation must be redone in each new shell:

```bash
. .venv/bin/activate                 # Linux/macOS
```

```powershell
.\.venv\Scripts\Activate.ps1         # Windows PowerShell
```

```bat
.venv\Scripts\activate.bat           :: Windows cmd
```

If PowerShell blocks activation because script execution is restricted, allow locally signed scripts for your user account, then activate again:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
.\.venv\Scripts\Activate.ps1
```

On Linux/macOS, to skip the per-shell `activate` step (and keep uv's cache inside the project for sandboxed runtimes), set up direnv — see the [direnv appendix](#appendix-direnv-linuxmacos).

### Check the commands run

With the venv activated, confirm the entry points resolve:

```bash
command -v commonplace-validate   # Linux/macOS — should print a path under .venv/bin
commonplace-init --help
```

```powershell
(Get-Command commonplace-validate).Source   # Windows — should print a path under .venv\Scripts
commonplace-init --help
```

## 3. Create the project with commonplace-init

Run `commonplace-init` from the project root. With the venv activated (step 2), call it by bare name:

```bash
commonplace-init --name <your-project>          # Linux/macOS
```

```powershell
commonplace-init --name <your-project>          # Windows PowerShell
```

The `--name` flag sets the project name used in templates; if omitted it defaults to the directory name.

This creates:

- **User KB directories** — `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/sources/`, `kb/tasks/`, `kb/work/`, `kb/reports/`, `kb/log.md`
- **Commonplace library content** — shipped notes, reference docs, instructions, review gates, and skills under `kb/commonplace/notes/`, `kb/commonplace/reference/`, and `kb/commonplace/instructions/`
- **Type definitions** — shared types under `kb/types/`, plus source/report type scaffolds
- **Canonical skills** — `kb/commonplace/instructions/cp-skill-write/`, plus the matching `cp-skill-validate/`, `cp-skill-connect/`, etc. The `cp-skill-` prefix avoids collisions with your project's own skills and with the `commonplace-*` CLI commands.
- **Known runtime skill projections** — `.agents/skills/cp-skill-*/` and `.claude/skills/cp-skill-*/` copies of the canonical skill directories for two common layouts (step 5 covers other runtimes). These are regular directories, not symlinks or junctions, so they work the same on every platform — including Windows without admin rights or Developer Mode.
- **`.envrc`** — project-scoped environment (`PATH`, `UV_CACHE_DIR`) for the optional direnv setup (see the [direnv appendix](#appendix-direnv-linuxmacos)); harmless if you don't use direnv
- **`AGENTS.md.template`** — control-plane template with the project name filled in

Rerunning `commonplace-init` is safe — it never overwrites existing files, so you can rerun after a package upgrade to pick up new scaffold files. It reports which preserved files already match the current scaffold and which were left untouched because they differ from what the current run would generate.

### Check validation and search

Commonplace works with curated indexes and `rg`; no semantic-search daemon is required.

```bash
commonplace-validate kb/commonplace/reference/commands.md
rg "^description:" kb/commonplace/notes kb/commonplace/reference kb/commonplace/instructions --glob "*.md"
rg "your search terms" kb/ --glob "*.md"
```

A fresh project has no user notes yet, so `commonplace-validate kb/notes` may report that no notes matched — run it after the first user note exists.

## 4. Set up the control-plane file

The control-plane file (`CLAUDE.md` or `AGENTS.md`) tells the agent what the KB is for, where to find things, and which skills are available. Codex- and Claude-style runtimes load it automatically from the project root; internal runtimes may need an explicit project-instructions setting, plugin config, or prompt import.

**New project** — rename the template:

```bash
mv AGENTS.md.template CLAUDE.md
# or
mv AGENTS.md.template AGENTS.md
```

**Existing project that already has a CLAUDE.md or AGENTS.md** — append the template:

```bash
cat AGENTS.md.template >> CLAUDE.md
```

Then review the merged file and fill in the per-project parts. The template's HTML comments mark every spot; the load-bearing ones are:

- **`KB Goals and Scope`** — Purpose, Scope (the out-of-scope list is what prevents scope creep), and Quality bar. Without these the agent has no basis for inclusion decisions.
- **Command invocation (in `### Commands`)** — keep the bare-name variant, which matches the activated venv from step 2 (or the auto-activation in the direnv appendix). If the project deliberately does **not** put the venv on `PATH`, keep the fallback variant telling agents to call the venv executables directly — `.venv/bin/commonplace-validate` or `.venv\Scripts\commonplace-validate.exe` — otherwise agents will retry failing bare commands.
- **Navigation entry points** — add curated tag READMEs to the list as they emerge; the template comment explains when to create one.

## 5. Install skills for every agent that will work on the project

**For most agent setups, nothing needs to be done here.** `commonplace-init` already projected the skills into the two common layouts — `.agents/skills/cp-skill-*/` (Codex and others) and `.claude/skills/cp-skill-*/` (Claude Code) — by copying each `cp-skill-*` directory from its source under `kb/commonplace/instructions/`. The copies are regular directories, so no platform-specific link support is needed. If every agent that will work on the project reads one of those two directories, skip to step 6.

You only need to do something here if an agent uses a **different** skill-discovery convention. In that case, expose the same source directories where that runtime expects them:

```text
kb/commonplace/instructions/cp-skill-*/
```

Inspect your runtime's skill-discovery rules and project every `cp-skill-*` directory into that surface — copy, plugin registration, or IDE-specific import. The canonical content stays under `kb/commonplace/instructions/`; rerunning `commonplace-init` after an upgrade reports projected copies that drifted from that source without overwriting them.

## 6. Start the runtime

Start your agent runtime from a shell where the venv is activated (step 2) so it inherits the environment. On Windows, activate in that shell first, or configure the IDE's integrated terminal/service so `.venv\Scripts` is on `PATH`.

From inside the running runtime, confirm the skills resolve by their `cp-skill-*` names:

```text
cp-skill-write
cp-skill-validate
cp-skill-connect
cp-skill-health-check
```

If they don't, run `cp-skill-health-check` (once it is visible) or re-check the projection for your runtime (step 5).

## Pre-approve Commonplace commands in Claude Code (optional)

If you use Claude Code, skip the per-command permission prompt by adding prefix-wildcard allow rules to `.claude/settings.local.json` (user-local, gitignored). Add one `Bash(<name>:*)` entry per `[project.scripts]` entry in `pyproject.toml`:

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

Prefer `.claude/settings.local.json` over `.claude/settings.json` so the approvals stay local and aren't committed for other contributors.

## Appendix: direnv (Linux/macOS)

direnv is an optional convenience on top of the plain venv activation in step 2. It does two things:

- **Auto-activation** — adds `.venv/bin` to `PATH` whenever you `cd` into the project, so `commonplace-*` commands resolve by bare name without running `. .venv/bin/activate` in every new shell.
- **In-project uv cache** — sets `UV_CACHE_DIR` to `.uv-cache/` inside the project, so sandboxed runtimes like Codex don't need privilege escalation to write to a cache outside the project tree.

`commonplace-init` already generated the `.envrc` with both settings, so setup is just installing the hook and allowing the file.

1. Install the direnv shell hook once (skip if already present), then restart your shell:

   ```bash
   echo 'eval "$(direnv hook bash)"' >> ~/.bashrc   # bash
   echo 'eval "$(direnv hook zsh)"' >> ~/.zshrc      # zsh
   ```

2. Allow the generated `.envrc` from the project root:

   ```bash
   cd /path/to/your-project
   direnv allow
   ```

   You should see a `direnv: loading ...` message, and commands resolve by bare name:

   ```bash
   command -v commonplace-validate
   ```

direnv populates `.uv-cache/` inside the project (you'll likely want to keep it out of version control). Launch agent runtimes from this direnv-loaded shell so they inherit the environment. If a runtime is started from a non-interactive wrapper that has not run the hook, wrap the launch explicitly:

```bash
direnv exec /path/to/your-project codex
```

direnv here is written for Linux/macOS. It may work on Windows through WSL or Git Bash, but that path is untested.

## Resulting layout

```text
my-project/
  .venv/
  .envrc
  .agents/
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

Upgrade the project-local package from PyPI:

```bash
uv pip install --upgrade llm-commonplace
```

If the project uses a source checkout or editable install for Commonplace development, pull that checkout before upgrading or reinstalling the editable package.

Rerun init to pick up any new scaffold files (existing files are preserved):

```bash
commonplace-init
```
