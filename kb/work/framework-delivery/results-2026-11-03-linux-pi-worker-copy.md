# Linux pi installed worker copy — 2026-11-03

## Result and scope

**Passed:** the installed-project worker-copy check, using pi's harness-provided
`subagent` extension copied unchanged to a disposable user-level directory.
The parent followed the installed probe skill through a project stub, delegated
one file read to a fresh worker, and reported `DELEGATED-STEP-V1`. The parent
did not read the target itself.

This establishes the worker-copy item in the [acceptance table](./README.md)
for this Linux configuration. It does not establish Windows/macOS workers,
live-session upgrades, `/reload`, continuation, nesting, or full execution of
Commonplace's delegating skills. The target was the synthetic probe library,
not a production Commonplace skill's complete workload.

## Environment and setup

- Linux `6.8.0-147-generic`; pi **1.3.0**.
- Parent and worker: `openai/gpt-6-astra`, thinking `low`, existing OpenAI OAuth
  credentials. No account, billing, or active configuration changes. This is
  a different route from the previously blocked Sol check; it does not show
  that the old no-credit route recovered.
- Isolated uv tool directories held PyPI **llm-commonplace 0.3.3**, resolving
  Workjig **0.3.1**, and **cp-delivery-probe 1.0.0** built from a scratch copy
  of the workshop's revision-7 package.
- Copy source: checkout commit `e8087b7f11023dc39427348ec75160907a3b05ea`.
  All 14 files under `.pi/extensions/subagent/` and
  `.pi/agents/commonplace-worker.md` were byte-verified against their user-level
  copies. No extension or worker-definition changes were required.
- Scratch root: `/tmp/cp-delivery-pi-worker-20261103.jCvQce`.
  Project: its `project/` directory, outside the source checkout.
  `PI_CODING_AGENT_DIR` selected its `pi-user/` directory, with the extension
  under `extensions/subagent/` and definition under `agents/`.
- The project was initialized with the isolated `commonplace-init --name
  pi-worker-probe`; control-plane templates were renamed into place.
  `cp-delivery-probe-init` installed the synthetic library pointer and stubs.
  Both init checks passed. The project had no `.pi/extensions/` directory.

The [probe protocol](./probe-package/PROTOCOL.md), case 10, supplied the test.
Harness-specific setup used a private copy of the existing OpenAI credential
record and model catalog, offline catalog mode, disabled retries, and JSON
one-shot parent sessions. The parent had only `read` and `subagent`; MCP was
disabled. The worker definition retained its normal tool selection, but its
handoff prohibited writes and further delegation. No delivery hooks or
shell-emulated worker were added. The copied extension itself launched the
worker through its normal harness implementation.

These are process/configuration isolation measures, not an OS sandbox or a
file-permission acceptance test. The actual user installation and settings
were not modified.

## Attempts and observed sequence

### Attempt 1 — setup omission, no worker launched

The scratch project initially lacked the probe protocol's standing instruction
pointing to `.cp-delivery-probe/library.md`. The parent looked for the synthetic
skill in the real Commonplace library and stopped without delegation. Its
restricted tool selection offered no search/listing fallback. No token was
returned. Preserve this as a failed setup attempt, not a worker failure or pass.

The correction appended the supplied `probe-package/test-project/AGENTS.md`
text verbatim to the scratch project's generated `AGENTS.md`. Neither package,
installed skill, extension, nor worker definition was changed. The parent prompt
and tool selection stayed the same; the retry started a fresh parent session.

### Attempt 2 — passed

1. The parent read `.cp-delivery-probe/library.md`.
2. It tried a nonexistent `.pi/skills/delivery-probe-delegate/SKILL.md`, then
   successfully read `.agents/skills/delivery-probe-delegate/SKILL.md` and its
   installed target. This was a stub-following check, not proof of native
   skill-menu discovery.
3. It called `subagent` once with `agent: commonplace-worker`,
   `agentScope: user`, and the scratch project as `cwd`. No `sessionFile`,
   model override, or nested-worker budget was supplied.
4. The worker read the project probe pointer and the installed
   `share/cp-delivery-probe/instructions/delegated-step.md`. Its only tool calls
   were these two reads. It returned exactly `DELEGATED-STEP-V1`.
5. The parent reported the token and identified the worker session. Both
   processes exited zero; the worker ended with `stopReason: stop`.

## Fresh-context and mutation checks

Parent session: `01a1a0bc-0898-7143-8ae8-09037854c2da`.
Worker session: `01a1a0bc-52f9-7628-8235-f981a02184db`.

The retained execution record identifies `agentSource: user`, the copied
user-level definition, the correct project directory, and the parent session.
It records inherited `openai/gpt-6-astra` / `low` and zero nested depth/slots.
The launch arguments contain no session-resume option.

The worker transcript contains one user message: the bounded task and absolute
installed-file path. A parent-only marker, `PARENT-ONLY-73d6a91c`, is absent from
that transcript. The parent prompt did not supply the expected file token.
The parent tool trace contains no read of `delegated-step.md`. Together these
checks establish a fresh conversation handoff, not absence of shared standing
project instructions or an inaccessible filesystem.

All **988** pre-run hashed project, installed-library, extension and definition
files were unchanged after the successful model-backed run. No production code
was changed; no pytest run was needed for this acceptance probe.

## Evidence and cleanup

Local raw evidence remains at
`/tmp/cp-delivery-pi-worker-20261103.jCvQce/evidence/`:

- `attempt-1-parent-events.jsonl` and associated stderr/exit code;
- `parent-prompt.txt`, `parent-events.jsonl`, stderr and exit code;
- `sessions/`: both parent sessions, the worker session, and extension audit
  records including `execution.json`;
- `subagent-result.json`, `verification.json`, `copy-manifest.json`, and
  `pre-run-files.json`;
- init/check logs, project snapshot, probe removal and tool-uninstall logs.

These temporary logs are not durable publication dependencies; this report
retains the acceptance observations. Original session paths in execution
records no longer exist; their copies are under `evidence/sessions/`.

Cleanup ran `cp-delivery-probe-init --remove`, uninstalled both isolated uv
tools, and removed the scratch project, package copy, configuration, model
catalog and credential copy. Only the local evidence directory remains.
