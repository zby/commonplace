---
description: "Use when the isolated Commonplace rehearsal selects Codex CLI on Linux; configure its filesystem boundary and retain process evidence."
type: types/instruction.md
---

# Launch the rehearsal through Codex CLI on Linux

Run one supplied rehearsal prompt in an isolated Codex CLI process and retain
its execution evidence.

The orchestrator loads this branch from `test-installed-commonplace.md` only
when its selected runtime is Codex CLI on Linux. Keep the parent procedure's
scope, budgets, scenario selection, and assessment in force. This branch
supplies launch mechanics; it does not select stages or assign verdicts.

## Prepare the launcher

Use the source checkout's `scripts/run_isolated_codex.py`. The orchestrator
invokes it; test agents never load it. Use run-directory names `project/`,
`tools/`, `bin/`, `fixtures/`, `inputs/`, and `records/`. Keep prompts and
evaluator evidence outside `project/`. Choose a unique record name on every
call; the helper refuses to overwrite an existing record.

Install with `UV_TOOL_DIR=<run>/tools`, `UV_TOOL_BIN_DIR=<run>/bin`, and
`UV_CACHE_DIR=<run>/cache`. Select `/usr/bin/python3` as the uv installation's
interpreter so it exists inside the sandbox. The snapshot pack needs no
capture-tool installation. Do not expose developer tool environments to
supply missing commands.

## Launch one isolated process

`run_isolated_codex.py` requires Bubblewrap with working user namespaces and a
native Codex distribution. It detects the npm-installed distribution, or takes
`--codex-vendor <directory-containing-bin/codex>`. Verify the CLI supports the
helper's flags; the initial implementation targets version 0.156.1.

After installing Commonplace and creating the project, probe the boundary.
This probe starts `commonplace-validate`; it cannot run before installation:

```bash
python3 scripts/run_isolated_codex.py --run-dir <run> --record preflight --access workspace-write --probe-only
```

Write only your selected stage prompt to `<run>/inputs/0.txt`. Then launch,
substituting your chosen record name, access mode, and remaining time allowance:

```bash
python3 scripts/run_isolated_codex.py --run-dir <run> --record 0-exec --access workspace-write --timeout 900 --prompt-file <run>/inputs/0.txt
```

Use `--access read-only` for answer stages. Access mode and timeout are explicit
inputs; the helper chooses neither from scenario content. Each launch probes
hidden paths, denied tool-directory writes, project write mode, and executable
startup before sending the prompt. Do not bypass a failed probe.

Saved CLI authentication is mounted read-only by default. Select `--auth env`
to use `CODEX_API_KEY` or `OPENAI_API_KEY` from the supervisor environment.
The helper does not copy credentials into records. Classify authentication
failure as a runtime blocker, not a Commonplace failure. A successful
`codex --version` probe does not verify API access. If model discovery or
workspace routing fails before a response, preserve the trace and report a
runtime-connectivity blocker. The launcher shares its caller's network
boundary, including any outer sandbox restrictions.

The process receives separate filesystem and process namespaces containing
system binaries/certificates, Codex, read-only installed tools, and the project.
The original HOME and CODEX_HOME values remain intact, with fresh filesystem
contents apart from selected authentication and this invocation's session logs.
The checkout, personal instructions/configuration/memory/skills, evaluator
files, and prior transcripts are not mounted. Codex starts a fresh
`exec --ignore-user-config` session with memory, plugins, apps, hooks, and
external browser/computer integrations disabled. Project skills and worker
delegation remain available.

The helper writes `prompt.txt`, `isolation.json`, `launch.json`, `trace.jsonl`,
`stderr.txt`, and `execution.json` under `records/<record>/`. Execution metadata
contains the process exit code, timeout and interruption flags, received stop
signal, and elapsed seconds. Send SIGINT or SIGTERM to stop the launcher; it
terminates the child process group and retains partial evidence. SIGKILL
cannot produce final metadata; recover state under the parent procedure. Launch or
probe exceptions produce `error.json`. These are process facts, not stage
verdicts. Interpret error events and missing responses in the raw trace even
when the process exits 0.

The initially empty `records/<record>/sessions/` is mounted at Codex's session
log path. Audit these logs for model identity, loaded instructions, worker
launch settings and parent/child relationships. Workers can see the current
invocation's runtime logs; earlier logs and evaluator files remain unmounted.
Do not use `--ephemeral`, which suppresses these audit records.

Network access is shared with the caller for model API calls. Policy inputs
are local snapshots; no fixture server is needed. This
helper establishes filesystem/session isolation. If the test needs network
isolation or another OS, use a separately verified launcher and record its
boundary; otherwise report that runtime as unsupported.
