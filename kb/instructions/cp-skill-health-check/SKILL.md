---
name: cp-skill-health-check
description: Diagnose Commonplace installation, skill discovery, command PATH, headless harness execution through Workjig, and workflows blocked by sub-agent availability, depth, or isolation.
type: types/instruction.md
user-invocable: true
allowed-tools: Read, Grep, Glob, Bash, Task
argument-hint: "[symptom] — optional description of what is broken"
---

# Commonplace Health Check

## EXECUTE NOW

Identify the installation or runtime constraint blocking a Commonplace operation and report the smallest repair supported by evidence.

Use this skill when a Commonplace KB has missing skills, missing or failing `commonplace-*` commands, commands that work in one shell but not in an IDE or agent runtime, or a workflow blocked on sub-agent creation, isolation, or headless harness execution. It applies both to installed projects, which read the Commonplace library from the installed package through pointers `commonplace-init` writes, and to the Commonplace source repository, whose own `kb/` is the library.

Target symptom: `$ARGUMENTS`

Keep the project and runtime configuration unchanged during diagnosis. Step 7 permits writes to a private diagnostic directory and the harness's normal runtime state. Report the evidence and the smallest repair. Apply a repair only when the user asked for one.

Run in the context being diagnosed; do not delegate the health check itself.
If already invoked in a worker, identify that scope and do not extrapolate its
capabilities to its parent. For a delegation symptom, run Step 3 after the
layout and skill checks; run the package checks only if the evidence also
points to an installation or command failure. For a headless execution symptom,
run Steps 4 and 7 after the layout and skill checks. For a general health
check, run all steps and record any probe you cannot run.

## Step 1 — Locate the project and classify the layout

From the workspace root, inspect:

```bash
pwd
test -f AGENTS.md && echo "AGENTS.md: present" || echo "AGENTS.md: missing"
test -f CLAUDE.md && echo "CLAUDE.md: present" || echo "CLAUDE.md: missing"
test -d .commonplace && echo "layout: installed project" || true
test -f pyproject.toml && test -d src/commonplace && echo "layout: source repo" || true
test -d kb/commonplace && echo "old library copy: kb/commonplace/ present" || true
test -d .agents/skills && echo ".agents/skills: present" || true
test -d .claude/skills && echo ".claude/skills: present" || true
```

Interpretation:

- Installed project: `.commonplace/library.md` exists and names the library root in the installed package. The project holds no library files.
- Source repository: `pyproject.toml`, `src/commonplace/`, and top-level `kb/{theory,reference,instructions}/` exist. Its `kb/` is the library.
- Old library copy: `kb/commonplace/` comes from a release that copied the library into projects. Report it as requiring separate cleanup. `commonplace-init` leaves these files and any review results naming them untouched; inspect local changes and references before removing copies.
- Neither: the wrong directory is open or `commonplace-init` has not run.
- `.venv` is not a Commonplace layout requirement. A project may still own one for unrelated dependencies.

## Step 2 — Check the control plane, library pointers, and skills

Read the active root control-plane file and confirm it routes Commonplace commands by bare name and, in an installed project, points agents to `.commonplace/library.md`. Then check init's pointers into the library and the runtime skills:

```bash
commonplace-init --check
test -f .agents/skills/cp-skill-health-check/SKILL.md && echo ".agents skill: OK" || true
test -f .claude/skills/cp-skill-health-check/SKILL.md && echo ".claude skill: OK" || true
```

Interpretation, for an installed project:

- Every line `ok`: the skill stubs, `.commonplace/library.md`, and the Claude Code read rule match the installed library.
- `stale` or `missing`: the library changed or moved since init last ran, for example after an upgrade that changed the skill set or a switch between editable and normal installs. Rerun `commonplace-init`. Until then, agents may read an outdated copy of the library without any warning.
- `foreign`: a skill directory that `commonplace-init` did not write shadows the library's skill. Remove it after checking it holds nothing the user needs, then rerun `commonplace-init`.
- `collision`: a file in the project's `kb/types/` has the same path as a library global type, so every artifact typed `types/<name>.md` fails validation. It is usually a leftover copy from an older release. Delete it, or move its change into a collection's own `types/` directory.
- Reads of library files denied in Claude Code: the read rule in `.claude/settings.local.json` is missing or names another library root; `commonplace-init --check` reports it.

In the source repository, `.claude/skills/` and `.agents/skills/` hold committed symlinks into `kb/instructions/`; `commonplace-init --check` does not apply. Do not run `commonplace-init` there; follow the source repository's `AGENTS.md` instead.

## Step 3 — Check delegation, agent depth, and isolation

Inspect the current session's exposed tools, runtime instructions, effective
settings when available, and any supplied launch error. Record:

- whether a harness worker-launch tool is available and permitted;
- the current agent depth, the maximum permitted depth, and their counting
  convention, when exposed;
- how many additional nested worker levels those values permit;
- whether launch supports a fresh context without the parent's conversation;
- available concurrent worker capacity, separately from nesting depth.

Report unexposed values as `unknown`. A configuration file is evidence of
configured intent, not proof that the running session loaded it. Neither an
installed agent CLI nor a skill's `allowed-tools` declaration proves that a
worker-launch tool is available. Do not infer depth from agent names, the
number of visible chats, or the number of free worker slots.

For a failing workflow, read its operative instructions and map the nesting
needed from the failing caller: who launches whom, and at which stage. Count
a skill's `context: fork` only if this runtime actually executes it in a
child context. Sequential sibling workers reuse a level; do not add their
count to the required depth. For ingest, the agent executing `cp-skill-ingest`
must be able to launch a fresh drafting worker; if ingest itself runs in a
child of the user-facing agent, drafting needs a further level. Compare the
required nesting with the remaining depth at that caller, not merely at the
health-check agent. If the caller's depth or runtime behavior is unavailable,
report that comparison as unresolved.

When a delegation symptom remains unresolved and a harness launch tool is
available and permitted, make at most one diagnostic worker launch from the
current context. Use a fresh-context option if supported. Give it only:

```text
This is a Commonplace worker-launch diagnostic. Reply with
COMMONPLACE_WORKER_OK and any agent-depth or nesting-limit values explicitly
exposed in your runtime instructions; report unknown otherwise. Do not read
files, use tools, invoke skills, spawn workers, or modify anything.
```

Collect the response and release the worker through the harness when
supported. Preserve any launch failure verbatim. Success establishes only
that one child could run from this context at this time; it does not establish
the maximum depth or prove conversation isolation. Establish isolation from
the launch API's documented contract and the actual launch arguments; otherwise
report it as unknown. Do not probe recursively. Use the native launch tool for
this step and Workjig for Step 7. If probing is unavailable or prohibited,
report the evidence gap and continue diagnosis.

Classify the evidence as missing launch capability, delegation prohibited,
depth exhausted, concurrent capacity exhausted, isolation unavailable, another
launch failure, or unresolved. A missing tool alone does not establish why it
is missing. Recommend a shallower entry point, enabling supported delegation,
or waiting for an owned worker slot only when the evidence supports that
repair. Report the specific workflow stage affected. A diagnosis does not
authorize changing runtime settings or bypassing the workflow's isolation rule.

## Step 4 — Check the uv tool installation and command ownership

On Linux/macOS:

```bash
command -v uv || true
uv tool list || true
uv tool dir --bin || true
command -v commonplace-init || true
command -v commonplace-validate || true
which -a commonplace-validate 2>/dev/null || true
```

On native Windows PowerShell:

```powershell
Get-Command uv -ErrorAction SilentlyContinue
uv tool list
uv tool dir --bin
Get-Command commonplace-init -All -ErrorAction SilentlyContinue
Get-Command commonplace-validate -All -ErrorAction SilentlyContinue
uv tool dir
```

If the bare name resolves to a `.cmd` file, or in Git Bash to an extensionless script, read that one file: `Get-Content (Get-Command commonplace-validate).Source` in PowerShell, or `cat "$(command -v commonplace-validate)"` in Git Bash.

Classify the result:

- **uv missing:** the installation prerequisite is absent.
- **`llm-commonplace` absent from `uv tool list`:** the user-level tool is not installed.
- **Command exists inside `uv tool dir --bin` but bare-name lookup fails:** the tool executable directory is missing from this process's `PATH`.
- **Bare name resolves to a supported Windows shim:** the file is a single line that runs `<uv tool dir>\llm-commonplace\Scripts\python.exe -c` on the same command's entry point, as written by the shim snippet in `INSTALL.md` (`/c/...` path form in the Git Bash script). Count it as the uv tool, not a conflict: Windows installs require these shims ahead of `uv tool dir --bin`. If that `python.exe` is missing, the tool environment is damaged; reinstall it and rerun the snippet. `commonplace-init` makes the same distinction.
- **Bare name resolves outside `uv tool dir --bin` otherwise:** another install, a project venv, or a shim for another interpreter or command shadows the user-level tool. Report every candidate from `which -a` or `Get-Command -All`.
- **Only some declared `commonplace-*` commands exist:** the tool installation is incomplete or stale after an entry-point metadata change; reinstall it.
- **A fresh terminal resolves the command but the IDE or agent does not:** the launch class did not inherit the updated user environment. Treat this as runtime environment propagation, not package absence.

Do not use `uv tool install --force` as the default repair for an executable conflict. First identify which installation owns the conflicting name and remove or reorder the stale owner.

## Step 5 — Check legacy project-environment residue

Inspect only; do not delete. Do not print or read `.envrc` into the conversation: it may hold secrets. Compare it with the file older Commonplace releases generated and report only the classification.

The exact `.envrc` generated by older Commonplace releases contained only:

```bash
export PATH="$PWD/.venv/bin:$PATH"
export UV_CACHE_DIR="$PWD/.uv-cache"
```

POSIX shell:

```bash
if [ ! -f .envrc ]; then
  echo ".envrc: absent"
elif printf '%s\n' 'export PATH="$PWD/.venv/bin:$PATH"' 'export UV_CACHE_DIR="$PWD/.uv-cache"' | cmp -s - .envrc; then
  echo ".envrc: exact legacy Commonplace file"
else
  echo ".envrc: present, differs from the legacy file"
fi
test -d .venv && echo ".venv exists; determine its owner before cleanup" || true
```

On native Windows PowerShell:

```powershell
$Legacy = 'export PATH="$PWD/.venv/bin:$PATH"' + "`n" + 'export UV_CACHE_DIR="$PWD/.uv-cache"' + "`n"
if (-not (Test-Path .envrc -PathType Leaf)) {
  '.envrc: absent'
} elseif (((Get-Content .envrc -Raw) -replace "`r`n", "`n") -ceq $Legacy) {
  '.envrc: exact legacy Commonplace file'
} else {
  '.envrc: present, differs from the legacy file'
}
if (Test-Path .venv -PathType Container) { '.venv exists; determine its owner before cleanup' }
```

The exact legacy file is obsolete after the user-level tool works in fresh processes. A differing `.envrc` needs manual review by the operator; tell them it exists and differs, and leave the reading to them. A `.venv` may hold the project's own dependencies; never classify it as removable merely because Commonplace no longer needs it.

## Step 6 — Check package and validator health

If this is an installed project:

```bash
commonplace-validate landings
```

If this is the Commonplace source repository:

```bash
commonplace-validate kb/reference/commands.md
uv run pytest -q
```

Interpretation:

- Command not found: return to step 4.
- Import or dependency error: reinstall the uv tool. For an editable source install, metadata and dependency changes require `uv tool install --reinstall --python ">=3.11" --editable .` even though ordinary source edits do not.
- Validator runs: the command package is healthy; this does not establish worker availability, nesting depth, or isolation support.
- `uv run pytest` fails before tests start: the source project's dependency environment is unhealthy. `pytest` is a development dependency, not part of the Commonplace command tool.

## Step 7 — Check headless harness execution through Workjig

Use the failing workflow's controller launch directory, environment and
worker working directory. Recover its effective worker profile, including
the model, effort, extra flags and environment overrides. For a general check
without a failing workflow, use a configured Commonplace worker profile for
the active harness and state which profile and directory you checked. If no
applicable profile or environment is available, report the missing input.
Keep the workflow's effective sandbox, permissions and approval settings.

Use the installed Commonplace tool's Python. It is under
`$(uv tool dir)/llm-commonplace/bin/python` on Linux/macOS and under
`(uv tool dir)\llm-commonplace\Scripts\python.exe` on native Windows; use
the interpreter verified in Step 4 if it differs. Import Workjig from that
environment. Construct the worker as the workflow does. The standard
constructor is `HARNESSES[profile.harness].worker(profile)` from
`commonplace.headless.harness`, with `Profile.from_yaml_entry(entry)` for
a YAML profile. Use the worker as constructed, including any adjustments
the workflow applies. Report an import or profile error at this stage.

Resolve `worker.argv[0]` from the controller directory using the inherited
environment overlaid with `worker.env`. Use the installed Workjig resolver
(`workjig.platform.resolve_command` where present) so the result follows
Workjig's executable lookup. Follow symlinks and inspect any launcher or
shim for the executable it forwards to. Use observed process image metadata
when a wrapper selects its target dynamically. Record the chosen PATH entry
and the final executable's canonical path. Obtain the active session's
executable path from runtime metadata or a process verified to belong to
that session. Compare canonical paths and SHA-256 digests, and record available
version metadata for both sides. A digest match at different paths establishes
identical contents at different locations. A version match alone leaves
identity unresolved. If either final executable cannot be established, report
the comparison as `unknown`. Configuration and shell command lookup cannot
identify the active session's binary on their own.

The live probe uses the configured provider and can consume credentials and
quota. Run it only when the user has authorized a real harness call, including
an explicit request to test live Workjig execution. Otherwise report the
static findings and mark the live probe `not run`. Use a new private
diagnostic directory where the configured harness may already write.
If it is inside the project, verify that Git ignores it. Keep its records
and logs local. Use only generated input and direct the worker to read and
write only the paths Workjig lists in its invocation. If those paths fall
outside the existing permissions, report the boundary. Do not widen it.

Run this probe with the constructed `worker`, the workflow's
`worker_cwd` and the fresh `diagnostic_dir` as absolute paths:

```python
from uuid import uuid4

from workjig import Request, Run

nonce = uuid4().hex
request = Request(
    call_id="harness-health",
    task=(
        "Read health-input.txt at the path under Inputs. Copy its entire "
        "contents exactly to health-output.txt at the path under Required "
        "outputs. Add no text or newline. Read no other files, write no "
        "other files, and launch no workers."
    ),
    inputs={"health-input.txt": nonce},
    required_outputs=("health-output.txt",),
    worker=worker,
    timeout_seconds=180,
    max_launches=1,
)
records_dir = diagnostic_dir / "calls"
with Run(records_dir, worker_cwd, retain_logs=True) as records:
    result = records.call(request)

launch_ids = tuple(launch.launch_id for launch in result.launches)
exact = result.outputs.get("health-output.txt") == nonce
print(result.status.value, exact, result.reused)
for launch in result.launches:
    print(launch.launch_id, launch.status.value, launch.returncode, launch.launch_dir)

if result.status.value == "delivered" and exact and not result.reused and len(launch_ids) == 1:
    with Run(records_dir, worker_cwd, retain_logs=True) as records:
        replay = records.call(request)
    print("reuse verified", (
        replay.status.value == "delivered"
        and replay.reused
        and replay.outputs.get("health-output.txt") == nonce
        and tuple(launch.launch_id for launch in replay.launches) == launch_ids
    ))
```

Pass the probe only on exact delivery on one physical launch and verified
reuse after reopening the records. The same request with the same one-launch
limit must not start another worker. Keep the logs on failure and do not
retry. Use the launch status and logs to distinguish executable lookup,
process start, sandbox or authentication failure, timeout, output mismatch
and terminal protocol failure where the evidence permits. Report only
redacted error evidence and the local record path. A native worker launch
in Step 3 supplies no evidence of Workjig delivery.

## Repair commands

Published install:

```bash
uv tool install --python ">=3.11" llm-commonplace
uv tool update-shell
```

Editable source install, run from the Commonplace checkout:

```bash
uv tool install --python ">=3.11" --editable .
uv tool update-shell
```

After `uv tool update-shell`, fully restart the shell, IDE, desktop agent, or service being tested. The shell update is durable and is not rerun at every shell start. In CI, configure a job-local uv tool executable directory and append it to `$GITHUB_PATH`; do not mutate a shell profile.

One uv tool installation supplies one active Commonplace version per OS user. Switching between published and editable sources changes the command implementation for every project under that user.

## Step 8 — Report

Use this format:

```text
Commonplace health check:
- Project root: OK / problem
- Layout: installed project / source repo / problem
- Library pointers: OK / stale / missing / not applicable
- Control-plane file: OK / problem
- Runtime skills: OK / problem
- Diagnostic context: failing caller / other context / unknown
- Worker launch: available / unavailable / prohibited / unknown
- Agent depth: current / maximum / counting convention, or unknown
- Remaining nesting levels: number / unknown
- Workflow nesting required: number and caller / unresolved / not applicable
- Fresh-context isolation: supported / unavailable / unknown
- Concurrent worker capacity: available / exhausted / unknown
- Launch probe: succeeded / failed / not run; reason and scope
- uv tool installation: OK / problem / not checked
- Runtime PATH: OK / problem / not checked
- Command ownership: uv tool / conflict / missing / not checked
- Validator: OK / problem / not checked
- Workjig harness: delivered and reused / failed / not run; profile, launch context and record path
- Harness executable: PATH entry, final binary and active session binary with known paths, digests and versions; match / identical contents at different paths / different / unknown

Likely cause:
<one or two sentences>

Recommended fix:
<concrete next command or user action>

Evidence:
- <short command result>
- <short command result>

Maintenance observations:
- <legacy .envrc, unrelated .venv requiring owner review, an old library copy under kb/commonplace/, or "None">
```

List independent problems in this blocking order:

1. Wrong directory or missing initialized layout.
2. Stale or missing library pointers, or a missing runtime skill.
3. Required worker launch, nesting depth, capacity, or isolation is unavailable.
4. uv or the `llm-commonplace` tool is missing.
5. uv's tool executable directory is absent from the consuming process's `PATH`.
6. Another executable shadows the uv tool.
7. Package import, dependency, or validator failure.
8. Workjig executable mismatch or headless launch, delivery, or reuse failure.

Do not claim the problem is fixed unless the failing check passes in the same
launch class and, for delegation failures, at the same caller depth that
originally failed. Distinguish observed results, configured limits, and unknowns.
