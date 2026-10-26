# Probe run prompts (revision 7)

Prompts to paste into a fresh session of each harness, started in this
checkout, to run the delivery probe. Each prompt is self-contained apart from
the files it names. Added 2026-10-24.

## Before starting

Each run installs the probe as a uv tool. Give every run its own uv tool
directory so runs never share an installation: the Codex run of 2026-10-24
did this by setting `UV_TOOL_DIR=<scratch>/tools` and
`UV_TOOL_BIN_DIR=<scratch>/bin` and putting `<scratch>/bin` first on `PATH`
for every session it started. The prompts below require it. Without it, runs
must be sequential: a session's cleanup uninstalls the user-level tool, and
the full protocol (pi) bumps the version, reinstalls and switches to an
editable install in cases 5 and 6, which breaks a run in progress elsewhere.

## Claude Code — delta since revision 4

```
Run the delivery probe, revision 7, in this harness.

Read kb/work/framework-delivery/probe-request.md and
kb/work/framework-delivery/probe-package/PROTOCOL.md first, then
kb/work/framework-delivery/results-claude-code-r4.md for how the last run
was recorded.

Scope: cases 0, 8, 9, 10 and 11 of the protocol. Cases 1 to 7 passed with
revision 4 and do not need repeating. Run each case the required number of
times (case 9 three times) and each in a fresh context that did not do the
setup: start each case as a fresh headless session rooted in the scratch
project (see the note after this prompt), giving it only the prompt the
protocol states.

Setup: make one scratch root outside this repository. Export
UV_TOOL_DIR=<root>/tools and UV_TOOL_BIN_DIR=<root>/bin before every uv
tool command, and put <root>/bin first on PATH for every session you start,
so this run shares nothing with the user-level uv tools or with other probe
runs. Copy probe-package/ to <root>/package and install it with
`uv tool install --python 3.12 <root>/package`, copy test-project/ to
<root>/project and run cp-delivery-probe-init there. Record the init report
and `--check` output for case 0, and record the isolation as an environment
note in the results.

Rules from the request: no hooks, no MCP servers, no copies of library
files into the project, do not touch the llm-commonplace tool or any
commonplace-* command, do not edit the package in the workshop. Record
every modification to the copy, every permission prompt or denial, and
separate observation from inference. A case you cannot run is a result;
record why.

Write results to kb/work/framework-delivery/results-claude-code-r7.md
using probe-package/RESULTS-TEMPLATE.md, then add a line under "Replies" in
probe-request.md. Do not edit anything else in the workshop.

Cleanup: run cp-delivery-probe-init --remove in the scratch project, run
`uv tool uninstall cp-delivery-probe` with the same UV_TOOL_DIR, delete the
scratch root, and confirm in the results file that this was done.

Commit only the results file and the probe-request.md line, with trailers
`Workshop: kb/work/framework-delivery` and `Model: <your model id>`.
```

Fresh contexts, learned 2026-10-24: a sub-agent started from the runner's
session inherits the runner's working directory, so it loads this repository's
`CLAUDE.md` and skills, not the scratch project's import of `library.md` and
its stubs (Claude Code run). Codex collaboration agents likewise kept the
repository's standing instructions and had to read the scratch `AGENTS.md` by
hand, so native stub discovery went untested there. Start each case as a fresh
headless CLI session rooted in the scratch project instead (Claude Code:
`claude -p` in the project; pi: `pi --mode json --no-session --approve` in the
project; Codex: `codex exec` in the project), and say in the results which
route was used. Case 10 then tests the harness's own sub-agent facility.

## Codex — delta since revision 4

Same scope as Claude Code. Codex has no `$ARGUMENTS` substitution, so in
case 11 the agent must carry the argument into the real skill itself; that is
what the case measures there.

```
Run the delivery probe, revision 7, in this harness.

Read kb/work/framework-delivery/probe-request.md and
kb/work/framework-delivery/probe-package/PROTOCOL.md first, then
kb/work/framework-delivery/results-codex-r4.md for how the last run was
recorded.

Scope: cases 0, 8, 9, 10 and 11 of the protocol. Cases 1 to 7 passed with
revision 4 and do not need repeating. Run each case the required number of
times (case 9 three times) and each in a fresh context that did not do the
setup: use a sub-agent per case if this harness has them, giving it only the
prompt the protocol states and the scratch project path. If it has none,
record that, run each case in your own context, and say so per case.

Setup: make one scratch root outside this repository. Export
UV_TOOL_DIR=<root>/tools and UV_TOOL_BIN_DIR=<root>/bin before every uv
tool command, and put <root>/bin first on PATH for every session you start,
so this run shares nothing with the user-level uv tools or with other probe
runs. Copy probe-package/ to <root>/package and install it with
`uv tool install --python 3.12 <root>/package`, copy test-project/ to
<root>/project and run cp-delivery-probe-init there. Record the init report
and `--check` output for case 0, and record the isolation as an environment
note in the results. The stubs
Codex reads are under .agents/skills/.

Rules from the request: no hooks, no MCP servers, no copies of library
files into the project, do not touch the llm-commonplace tool or any
commonplace-* command, do not edit the package in the workshop. Record
every modification to the copy, every permission prompt or denial, and
separate observation from inference. A case you cannot run is a result;
record why.

Write results to kb/work/framework-delivery/results-codex-r7.md using
probe-package/RESULTS-TEMPLATE.md, then add a line under "Replies" in
probe-request.md. Do not edit anything else in the workshop.

Cleanup: run cp-delivery-probe-init --remove in the scratch project, run
`uv tool uninstall cp-delivery-probe` with the same UV_TOOL_DIR, delete the
scratch root, and confirm in the results file that this was done.

Commit only the results file and the probe-request.md line, with trailers
`Workshop: kb/work/framework-delivery` and `Model: <your model id>`.
```

## pi — full protocol

pi never ran the probe and is now a sanctioned worker harness (ADR 118), so
it runs every case. Whether pi loads `AGENTS.md`, lists project skill
directories, or can start a sub-agent is unrecorded; cases 1c, 7 and 10 settle
that.

```
Run the delivery probe, revision 7, in this harness. This harness has not
run the probe before, so run the full protocol.

Read kb/work/framework-delivery/probe-request.md and
kb/work/framework-delivery/probe-package/PROTOCOL.md first, then
kb/work/framework-delivery/results-claude-code-r4.md for how a run is
recorded.

Scope: every case, 0 to 11, including the three runs of case 3 and of
case 9 and the upgrade cases 5 and 6. First record the harness facts the
results template asks for: which instruction file this harness loads
(AGENTS.md, CLAUDE.md, another, or none), which skill directories it reads,
whether it can start a sub-agent, and whether it can read files outside the
project. If it loads neither AGENTS.md nor CLAUDE.md, follow case 1c and
the pointer line in the probe request. Run each case in a fresh context
that did not do the setup; if this harness cannot start one, run it in your
own context and say so per case.

Setup: make one scratch root outside this repository. Export
UV_TOOL_DIR=<root>/tools and UV_TOOL_BIN_DIR=<root>/bin before every uv
tool command, and put <root>/bin first on PATH for every session you start,
so this run shares nothing with the user-level uv tools or with other probe
runs. Copy probe-package/ to <root>/package and install it with
`uv tool install --python 3.12 <root>/package`, copy test-project/ to
<root>/project and run cp-delivery-probe-init there. Record the init report
and `--check` output for case 0, and record the isolation as an environment
note in the results.

Rules from the request: no hooks, no MCP servers, no copies of library
files into the project, do not touch the llm-commonplace tool or any
commonplace-* command, do not edit the package in the workshop. Record
every modification to the copy, every permission prompt or denial, and
separate observation from inference. A case you cannot run is a result;
record why.

Write results to kb/work/framework-delivery/results-pi-r7.md using
probe-package/RESULTS-TEMPLATE.md, then add a line under "Replies" in
probe-request.md. Do not edit anything else in the workshop.

Cleanup: run cp-delivery-probe-init --remove in each scratch project, run
`uv tool uninstall cp-delivery-probe` with the same UV_TOOL_DIR, delete the
scratch root, and confirm in the results file that this was done.

Commit only the results file and the probe-request.md line, with trailers
`Workshop: kb/work/framework-delivery` and `Model: <your model id>`.
```

## Windows — install check for the published 0.3.0 (any harness)

Not a probe run: this checks the published package on a Windows machine,
the open half of next step 1, and settles the protocol's case 2 question
about the `Read(//C:/…/**)` rule when the session is Claude Code. Added
2026-10-26. Paste into a session on the Windows machine; the session
needs uv, git and Python 3.12 available and PowerShell as its shell.

```
Verify that the published Commonplace 0.3.0 installs and initialises on
this Windows machine. Use PowerShell for every command and record exact
outputs, not summaries. Change nothing outside the scratch root below.

Setup: $root = "$env:TEMP\cp-030"; create it. Isolate the run from any
user-level uv tools: $env:UV_TOOL_DIR = "$root\tools";
$env:UV_TOOL_BIN_DIR = "$root\bin"; $env:PATH = "$root\bin;$env:PATH".
Record: Windows version, PowerShell version ($PSVersionTable), uv --version,
and the Python uv selects.

1. uv tool install --python 3.12 llm-commonplace==0.3.0
   Record how many executables uv reports. If uv refuses the package as
   newer than an exclude-newer cutoff, record that and retry with
   --exclude-newer-package llm-commonplace=2026-11-01T00:00:00Z
   --exclude-newer-package workjig=2026-11-01T00:00:00Z.
2. (Get-Command commonplace-init).Source and uv tool dir --bin: the first
   must be inside the second, and both under $root. Also record
   (Get-Command commonplace-init -All).Source to show nothing else shadows it.
3. New-Item -ItemType Directory "$root\project"; cd there; git init;
   commonplace-init --name win-check. Record the full report.
4. commonplace-init --check. Record every line and $LASTEXITCODE; 26 "ok"
   lines and exit 0 is the pass.
5. Record these file facts verbatim: the "allow" entry in
   .claude\settings.local.json; the absolute path line in
   .claude\skills\cp-skill-write\SKILL.md; one path from
   .commonplace\library.md. Note whether each path uses forward slashes and
   carries the drive letter. Check the first three bytes of
   settings.local.json and library.md for a byte-order mark
   ([System.IO.File]::ReadAllBytes(...)[0..2]); none is expected.
6. commonplace-validate kb/notes, then kb/reference, kb/instructions and
   kb/tags. Record each summary line.
7. Run commonplace-init again. Every file should be reported as preserved.
8. Only if this machine has Claude Code: from the project directory start
   one fresh headless session, claude -p "Read the file that
   .claude/skills/cp-skill-write/SKILL.md tells you to read and report its
   first heading and the absolute path you read" --permission-mode default,
   and record whether the read succeeded without a permission prompt or
   denial. This settles whether Claude Code on Windows honours the rule
   form init writes. If Claude Code is absent, say so.
9. Cleanup: uv tool uninstall llm-commonplace with the same environment
   variables, then remove $root. Confirm (Get-Command commonplace-init
   -ErrorAction SilentlyContinue) returns nothing.

Report: if this session runs inside a clone of the Commonplace repository,
write kb/work/framework-delivery/results-windows-install-030.md with the
sections Environment, Steps 1–9 (each with its recorded output), Findings,
Cleanup, and commit only that file with trailers
"Workshop: kb/work/framework-delivery" and "Model: <your model id>".
Otherwise return the same report as text for the operator to file.
```
