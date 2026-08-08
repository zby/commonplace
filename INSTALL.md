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

Then add a routing block to your project's `CLAUDE.md` or `AGENTS.md`. The vendored repo ships it as `AGENTS.md.reader-fragment`, so appending is one command (creates the file if the project has none):

```bash
cat commonplace/AGENTS.md.reader-fragment >> CLAUDE.md    # or >> AGENTS.md
```

Or paste it directly:

```markdown
## Knowledge base (vendored, read-only)

`commonplace/kb/` is a vendored knowledge base on agent context engineering,
memory, and deploy-time learning. For design decisions in those areas, consult
it before deciding: start at `commonplace/kb/notes/tags-README.md`. Paths named
inside it are relative to `commonplace/`. It is read-only in this project — to
contest a claim, open an issue at https://github.com/zby/commonplace/issues.
```

Either way, if you vendored under a directory name other than `commonplace/`, adjust the paths in the block to match.

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

- **uv** — installs Commonplace and selects or provisions a compatible Python 3.11+ interpreter
- **git**
- **ripgrep** (`rg`) — agent runtimes use it for fast KB search
- **An agent runtime** — Codex, Claude Code, or another LLM/IDE that can load a project control-plane file (`AGENTS.md`/`CLAUDE.md`) and expose skill directories to the agent

Normal KB maintenance is expected to happen under version control. The shipped procedures and examples use Git, so it is included in the out-of-the-box prerequisites above. A project may substitute another VCS if it adapts Git-specific procedures; the `commonplace-*` commands do not use Git history as correctness state.

### Check prerequisites

If any required tool is missing, install it before continuing.

Linux/macOS:

```bash
uv --version
git --version
rg --version
```

Windows PowerShell:

```powershell
uv --version
git --version
rg --version
```

## 2. Install Commonplace as a user-level tool

Install Commonplace as a user-level uv tool. uv creates an isolated environment for the package and places every declared `commonplace-*` executable in its tool executable directory:

```text
uv tool install --python ">=3.11" llm-commonplace
uv tool update-shell
```

The second command durably adds uv's tool executable directory to the user environment; it is not reissued on every shell restart. Close the installer shell and fully restart every shell, IDE, desktop agent, or service process that must use the commands. A process that was already running keeps its old environment.

This establishes one active Commonplace command version per OS user. All projects for that user resolve the same tool. Project dependencies remain independent and do not share Commonplace's isolated tool environment.

For Commonplace development, install an editable checkout instead, from that checkout's root:

```text
uv tool install --python ">=3.11" --editable .
uv tool update-shell
```

Ordinary Python and scaffold-source edits are visible without reinstalling. After changing dependencies, entry points, build metadata, or which files the package includes, force a metadata refresh without changing command ownership:

```text
uv tool install --reinstall --python ">=3.11" --editable .
```

Switching the user-level tool to an editable checkout changes the commands seen by every project for that user.

To install optional snapshot dependencies with the published tool, request the extra during installation:

```text
uv tool install --reinstall --python ">=3.11" "llm-commonplace[snapshot]"
```

### Check the commands run

Run these checks in a newly started process, not the installer process:

```bash
uv tool dir --bin
command -v commonplace-validate
commonplace-init --help
```

```powershell
uv tool dir --bin
(Get-Command commonplace-validate).Source
commonplace-init --help
```

The resolved command should be inside the directory printed by `uv tool dir --bin`. Repeat the check inside each IDE or agent runtime you intend to support; an integrated terminal result does not prove that a separately launched desktop agent inherited the same environment.

## 3. Create the project with commonplace-init

Run `commonplace-init` from the project root by bare name:

```bash
commonplace-init --name my-project
```

```powershell
commonplace-init --name my-project
```

The `--name` flag sets the project name used in templates; if omitted it defaults to the directory name.

This creates:

- **User KB directories** — `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/sources/`, `kb/tasks/`, `kb/work/`, `kb/reports/`, `kb/log.md`
- **Commonplace library content** — shipped notes, reference docs, instructions, review gates, and skills under `kb/commonplace/notes/`, `kb/commonplace/reference/`, and `kb/commonplace/instructions/`
- **Type definitions** — shared types under `kb/types/`, plus source/report type scaffolds
- **Canonical skills** — `kb/commonplace/instructions/cp-skill-write/`, plus the matching `cp-skill-validate/`, `cp-skill-connect/`, etc. The `cp-skill-` prefix avoids collisions with your project's own skills and with the `commonplace-*` CLI commands.
- **Known runtime skill projections** — `.agents/skills/cp-skill-*/` and `.claude/skills/cp-skill-*/` copies of the canonical skill directories for two common layouts (step 5 covers other runtimes). These are regular directories, not symlinks or junctions, so they work the same on every platform — including Windows without admin rights or Developer Mode.
- **`AGENTS.md.template`** — control-plane template with the project name filled in

Rerunning `commonplace-init` is safe — it never overwrites existing files, so you can rerun after a package upgrade to pick up new scaffold files. It reports which preserved files already match the current scaffold and which were left untouched because they differ from what the current run would generate. It does not create or inspect `.envrc`.

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
- **Command invocation (in `### Commands`)** — keep the unconditional bare-name rule. Commonplace commands come from the user-level uv tool, not the project's dependency environment.
- **Navigation entry points** — add curated tag READMEs to the list as they emerge; the template comment explains when to create one.
- **Version-control conventions** — keep the framework expectation that the KB is versioned, and add any project-specific commit, branch, or review rules. The template deliberately assigns no portable Commonplace semantics to those objects.

## 5. Install skills for every agent that will work on the project

**For most agent setups, nothing needs to be done here.** `commonplace-init` already projected the skills into the two common layouts — `.agents/skills/cp-skill-*/` (Codex and others) and `.claude/skills/cp-skill-*/` (Claude Code) — by copying each `cp-skill-*` directory from its source under `kb/commonplace/instructions/`. The copies are regular directories, so no platform-specific link support is needed. If every agent that will work on the project reads one of those two directories, skip to step 6.

You only need to do something here if an agent uses a **different** skill-discovery convention. In that case, expose the same source directories where that runtime expects them:

```text
kb/commonplace/instructions/cp-skill-*/
```

Inspect your runtime's skill-discovery rules and project every `cp-skill-*` directory into that surface — copy, plugin registration, or IDE-specific import. The canonical content stays under `kb/commonplace/instructions/`; rerunning `commonplace-init` after an upgrade reports projected copies that drifted from that source without overwriting them.

## 6. Start the runtime

Fully restart the agent runtime after `uv tool update-shell`, then confirm inside the agent that `commonplace-validate --help` resolves. Shell activation is not part of the contract. If the command works in a new terminal but not in the agent, diagnose how that runtime receives the user environment rather than reinstalling the package repeatedly.

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

## Troubleshooting command discovery

Use `uv tool list` to confirm installation and `uv tool dir --bin` to identify the expected executable directory. On Linux/macOS, `command -v` or `which -a` shows what wins on `PATH`; on PowerShell use `Get-Command -All`.

- **Tool missing:** install it with the step 2 command.
- **Executable exists in uv's tool directory but bare name is missing:** run `uv tool update-shell`, then fully restart the consuming process. In CI, append the configured tool bin directory to `$GITHUB_PATH` instead of editing a profile.
- **Bare name resolves elsewhere:** an older project venv or another install is shadowing the uv tool. Remove or reorder that `PATH` entry. Do not make `uv tool install --force` the default repair; uv's conflict is evidence that command ownership needs to be resolved.
- **Only one IDE or agent fails:** that launch class did not inherit the updated user environment. Fix its supported environment configuration or exclude it from the support claim.
- **Import fails after an editable metadata change:** rerun the editable install with `--reinstall` so uv refreshes the existing tool environment.

`cp-skill-health-check` performs the same classification and also checks the installed KB and skill projections.

### Migrating an older project-local installation

Install and verify the user-level tool first. Then inspect any project `.envrc` that adds `.venv/bin` or `.venv\Scripts` to `PATH`. The exact two-line `.envrc` generated by older Commonplace releases can be removed after the fresh-process checks pass. An edited `.envrc` must be reviewed manually. Remove a project `.venv` only if you have confirmed it was used solely for Commonplace; it may still own the project's unrelated dependencies.

## Resulting layout

```text
my-project/
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

Upgrade the published user-level tool:

```bash
uv tool upgrade llm-commonplace
```

For an editable source install, pull the checkout. Ordinary code changes are immediately visible; rerun `uv tool install --reinstall --python ">=3.11" --editable .` when installation metadata or dependencies changed.

To switch between an editable checkout and the published package, make the ownership change explicit:

```bash
uv tool uninstall llm-commonplace
uv tool install --python ">=3.11" llm-commonplace       # published
# or, from the checkout:
uv tool install --python ">=3.11" --editable .          # editable
```

Rerun init to pick up any new scaffold files (existing files are preserved):

```bash
commonplace-init
```
