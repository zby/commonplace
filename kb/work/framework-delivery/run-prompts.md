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
setup: use a sub-agent per case, giving it only the prompt the protocol
states and the scratch project path.

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

Case 10 asks the probe session to start a sub-agent, so when the case runs
inside a sub-agent it needs nested delegation. If the harness refuses, the
runner records that as the case result and does not read the file itself.

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
