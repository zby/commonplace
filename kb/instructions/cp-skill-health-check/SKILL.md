---
name: cp-skill-health-check
description: Run a Commonplace health check when agents, skills, or commonplace-* commands do not work correctly. Diagnoses project layout, promoted skill discovery, direnv/PATH state, package commands, and common launch-environment failures.
type: kb/types/instruction.md
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash
context: fork
argument-hint: "[symptom] — optional description of what is broken"
---

## EXECUTE NOW

Use this skill when the user reports that a Commonplace KB is not working correctly: missing skills, `commonplace-*` command failures, validation not found, the agent runtime not seeing the venv, or confusion around direnv. It applies both to installed KBs, where shipped content lives under `kb/commonplace/`, and to the Commonplace source repo, where shipped content lives directly under `kb/`.

Target symptom: `$ARGUMENTS`

This skill diagnoses and reports. Do not edit shell config, rerun `commonplace-init`, install packages, or change symlinks unless the user explicitly asks for repair after seeing the diagnosis.

## Step 1 - Identify the workspace shape

Run:

```bash
pwd
git rev-parse --show-toplevel 2>/dev/null || true
git remote -v 2>/dev/null || true
test -d kb && echo "kb: present" || echo "kb: missing"
test -f AGENTS.md && echo "AGENTS.md: present" || echo "AGENTS.md: missing"
test -f CLAUDE.md && echo "CLAUDE.md: present" || echo "CLAUDE.md: missing"
test -d kb/commonplace && echo "kb/commonplace: present" || echo "kb/commonplace: missing"
test -d src/commonplace && echo "src/commonplace: present" || echo "src/commonplace: missing"
test -d kb/reference && echo "kb/reference: present" || echo "kb/reference: missing"
test -d kb/instructions && echo "kb/instructions: present" || echo "kb/instructions: missing"
test -f .envrc && echo ".envrc: present" || echo ".envrc: missing"
test -d .venv && echo ".venv: present" || echo ".venv: missing"
```

Interpretation:
- Missing `kb/` means the user is probably not in the project root.
- If `kb/commonplace/` exists, classify the workspace as an **installed KB**.
- If any `git remote -v` URL names `github.com:zby/commonplace` or `github.com/zby/commonplace`, classify the workspace as the **Commonplace source repo**. Repositories can have multiple remotes; do not assume the relevant one is named `origin` or that there is only one remote. This is OK; do not warn about the missing shipped library namespace.
- If git metadata is unavailable but `src/commonplace/`, `kb/reference/`, and `kb/instructions/` exist while `kb/commonplace/` is missing, report "source-repo-shaped workspace, git identity unknown" rather than treating it as an installed KB failure.
- Missing `kb/commonplace/` in any other workspace that claims to be installed means `commonplace-init` likely has not run, or the install is from an older layout.
- Missing `AGENTS.md` and `CLAUDE.md` means the agent may not have a loaded control-plane file.
- Missing `.envrc` or `.venv` means command discovery will probably fail unless the package was installed globally.

## Step 2 - Check promoted skill discovery

Run:

```bash
# Use find -L so it follows symlinked skill directories. Promoted skills are
# usually symlinks into kb/instructions/<skill>/, and plain `find` (without -L)
# will not descend into them, returning a misleading empty result.
find -L .claude/skills .agents/skills -maxdepth 2 -name SKILL.md -print 2>/dev/null | sort
for skill in cp-skill-write cp-skill-validate cp-skill-connect cp-skill-convert cp-skill-health-check cp-skill-ingest cp-skill-snapshot-web; do
  for dir in .claude/skills .agents/skills; do
    test -e "$dir/$skill/SKILL.md" && echo "active skill OK: $dir/$skill" || echo "active skill MISSING: $dir/$skill"
  done
done
find .claude/skills .agents/skills -maxdepth 1 -type l ! -exec test -e {} \; -print 2>/dev/null | sort
```

The per-skill `test -e` loop is the authoritative signal for whether each expected skill resolves (`test -e` follows symlinks). Treat the `find -L` listing as a cross-check for unexpected or extra skills, not the primary verdict.

Expected promoted skills include at least:

```text
cp-skill-write
cp-skill-validate
cp-skill-connect
cp-skill-convert
cp-skill-health-check
cp-skill-ingest
cp-skill-snapshot-web
```

Interpretation:
- No `.claude/skills/` or `.agents/skills/` entries: `commonplace-init` likely did not run, or the runtime is looking at a different project root.
- `active skill MISSING` for an expected skill: the runtime skill surface is incomplete. In an installed KB, rerun `commonplace-init` after confirming the project root and package install. In the Commonplace source repo, recreate the local symlink to `kb/instructions/<skill>/`.
- Broken symlink output for an expected active skill: the skill surface points at a missing path; treat it as a runtime-skill problem.
- Broken symlink output for a retired or extra skill not in the expected active set, such as `cp-skill-compile-collections`, is a maintenance observation, not the likely cause of current Commonplace command or health-check failure when all expected active skills are OK.
- Skill exists on disk but the agent cannot invoke it: the runtime may not support that skill directory, may have been started before init, or may need restart.

## Step 3 - Check command environment

Run:

```bash
printf 'SHELL=%s\n' "$SHELL"
printf 'PATH=%s\n' "$PATH"
command -v commonplace-validate || true
command -v commonplace-init || true
command -v pytest || true
command -v python3 || true
command -v uv || true
```

Interpretation:
- `commonplace-validate` missing while `.venv/bin/commonplace-validate` exists usually means `.venv/bin` is not on `PATH`.
- `pytest` resolving outside the project venv is a sign the project environment was not loaded.
- `uv` missing only matters for install/update workflows; installed `commonplace-*` commands should not need `uv run` after environment activation.

## Step 4 - Check direnv specifically

Run:

```bash
command -v direnv || true
direnv status || true
rg -n 'direnv hook (bash|zsh)' "$HOME/.bashrc" "$HOME/.bash_profile" "$HOME/.profile" "$HOME/.zshrc" 2>/dev/null || true
direnv exec . bash -c 'command -v commonplace-validate; command -v pytest; printf "UV_CACHE_DIR=%s\n" "$UV_CACHE_DIR"' || true
```

Interpretation:
- `direnv` missing: install direnv or use explicit `.venv/bin/<command>` paths.
- `.envrc` not allowed: run `direnv allow` from the project root.
- No hook found in shell config: add `eval "$(direnv hook bash)"` to `~/.bashrc` for bash, or `eval "$(direnv hook zsh)"` to `~/.zshrc` for zsh, then start a new interactive shell.
- `direnv exec . bash -c ...` succeeds but direct `command -v commonplace-validate` fails: direnv is configured, but the current agent command environment did not inherit it. Start the agent runtime from a direnv-loaded interactive shell, or launch it with `direnv exec /path/to/project <agent-command>`.
- Do not test `direnv exec` through `bash -lc`; login shell startup may reset `PATH` and hide the environment you are trying to inspect.

## Step 5 - Check package and validator health

Prefer direct commands when available. If direct commands are missing but direnv works, wrap them with `direnv exec . bash -c`.

If the workspace is an installed KB, run one of:

```bash
commonplace-validate kb/commonplace/reference/commands.md
```

or:

```bash
direnv exec . bash -c 'commonplace-validate kb/commonplace/reference/commands.md'
```

If the workspace is the Commonplace source repo, validate:

```bash
direnv exec . bash -c 'commonplace-validate kb/reference/commands.md'
```

Interpretation:
- Command not found: environment activation or package installation problem.
- Import/module error: package install problem; reinstall in the project venv.
- Validation runs: the Python command surface is healthy; focus on skill discovery or agent launch environment.

## Step 6 - Report

Report in this format:

```text
Commonplace health check:
- Project root: OK / problem
- Layout: installed KB / source repo / problem
- Control-plane file: OK / problem
- Library layout: OK / problem
- Runtime skills: OK / problem
- Command PATH: OK / problem
- direnv: OK / problem
- Validator: OK / problem

Likely cause:
<one or two sentences>

Recommended fix:
<concrete next command or user action>

Evidence:
- <short command result>
- <short command result>

Maintenance observations:
- <retired or extra broken symlinks, stale generated indexes, or other non-blocking findings; write "None" if empty>
```

If several independent problems appear, list them in the order that blocks the most downstream checks:

1. Wrong directory / missing project root
2. `commonplace-init` did not run or installed layout is stale
3. Agent runtime does not see promoted skills
4. `.venv/bin` is not on `PATH`
5. direnv hook/allow/launch inheritance problem
6. Package import or command failure

Do not claim the installation is fixed unless you reran the failing check and it passed.
