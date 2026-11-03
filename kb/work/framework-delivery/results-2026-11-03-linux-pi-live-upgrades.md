# Linux pi live-session upgrades — 2026-11-03

## Result and limits

**Passed the bounded synthetic-upgrade checks:** one running pi session reread
updated library content, followed a changed skill body, refreshed its advertised
skill description with the actual TUI `/reload`, and followed repaired pointers
after an installation-mode change. A fresh process also read the repaired
library successfully.

The important distinction is between **file contents** and **loaded skill
metadata**. Re-reading files reached new content without restarting the session.
Init repaired generated pointers and descriptions on disk, but did not refresh
the running session's advertised description. `/reload` did.

This advances the upgrade item in the [acceptance table](./README.md). It does
not certify a real Commonplace release transition, another harness, Windows or
macOS, or automatic recovery without operator direction. Prompts explicitly
requested current file reads; this does not show that an unprompted agent will
notice an upgrade or abandon remembered instructions.

## Setup and protocol deviations

- Linux `6.8.0-147-generic`, pi **1.3.0**, `openai/gpt-6-astra`, thinking `low`.
- Fixture copied from checkout `1ba3da9e2`: revision 7 of the
  [probe protocol](./probe-package/PROTOCOL.md), including its worker-rule
  clarification. No fixture or product source in the checkout was changed.
- Scratch root: `/tmp/cp-delivery-pi-live-20261103.6PnEoE`. Its `project/` was
  copied from the supplied `test-project/`, including its standing instructions.
- Isolated `UV_TOOL_DIR` and `UV_TOOL_BIN_DIR`; package installed with
  `/usr/bin/python3`. This run installed only **cp-delivery-probe**, not a new
  Commonplace release. V1–V4 are synthetic fixture revisions.
- `PI_CODING_AGENT_DIR` selected scratch `pi-user/`. That directory held private
  copies of the existing OpenAI credential record and model catalog, with
  retries disabled. Offline mode prevented automatic catalog updates; model
  requests still used the provider. No active settings or credentials changed.
- The live run used an interactive terminal in a separate tmux 3.4 server,
  `--tui-mode regular`, `--tools read`, `--no-extensions`, `--no-mcp`,
  `--no-prompt-templates`, and explicit one-process project approval.
  No hooks or observer extensions were installed.

Cases 5–6 normally use fresh sessions. This follow-up deliberately kept one
process and conversation alive through the changes to test the remaining
live-session gap. A one-off Python driver sent terminal input and waited for
completed assistant messages in the persisted session. It did not inject
instructions into model responses or implement reload. `/reload` was entered
into the real TUI; RPC was not used to emulate that command.

The live session ID was `01a1a0c5-0fc0-73c1-88ca-63ed311ae8b2`; it contains all
eight model prompts across the upgrade sequence. The final fresh process used
`01a1a0c9-4cd2-7232-afdf-da9a21e4590d` with one prompt. Configuration isolation
was not an OS sandbox or a read-permission test.

## Observations

### 1. Baseline and library-only upgrade

V1 install, init and `--check` passed. Asked to run `delivery-probe-read`, the
agent read the project stub, library pointer, installed skill and its linked
files. It returned `SHARED-STEP-V1`, `PROBE-NOTE-TYPE-V1` and `READ-DETAIL-V1`.

The supplied `tools/bump.py 2` changed package version and library tokens in the
scratch source. A normal reinstall kept the installed library path unchanged.
Without init, `--check` still reported all ten outputs `ok`. The same live
session, asked to rerun the check with current file reads, returned all three
V2 tokens. No reload or restart occurred.

### 2. Changed skill body and metadata

For synthetic V3, the scratch `delivery-probe-read/SKILL.md` changed in two
additional places:

- Its description gained `Metadata revision three.`
- Its body gained step 5: `Also report the body marker
  \`SKILL-BODY-REVISION-THREE\`.`

After bump and reinstall, `--check` exited nonzero and marked both read-skill
stubs and `.cp-delivery-probe/library.md` stale. The library lookup command
emitted a stale-output warning. Init repaired those outputs; the next check was
all `ok`.

Before any reload, a tool-free question asked the model to quote the description
from its current system-context skill list rather than previous file reads. It
reported the original description, without the V3 suffix. A separate rerun of
the skill then read the current files and returned all three V3 tokens plus
`SKILL-BODY-REVISION-THREE`. Thus stale advertised metadata did not prevent
explicit rereading of the new skill body.

### 3. Actual `/reload` with an unseen metadata marker

To distinguish reload from recall of the preceding file reads, a second
metadata-only edit appended `Reload witness cedar-47.` to the description.
The scratch package was reinstalled at the same synthetic version, init reran,
and `--check` passed. The generated stub contained the marker; no model file
read had exposed it.

A second tool-free description question still returned the original description.
Then the TUI received `/reload` and displayed:

> Reloaded keybindings, extensions, skills, prompts, themes, and context files

The identical tool-free question now returned:

> Probe skill for the delivery test. Use only when asked to run the delivery-probe-read check. Metadata revision three. Reload witness cedar-47.

Both description answers used no tools. The new marker was absent from earlier
model-visible prompts and reads. The same session continued afterward. This is
model-backed evidence of refreshed skill metadata, not just a successful reload
notification or an inference from changed files on disk.

### 4. Installation-mode move: stale pointers and repair

The scratch package was reinstalled editable while still V3, then its source
was bumped to V4 without another install. The intended library moved from
`tools/cp-delivery-probe/share/cp-delivery-probe/` to `package/library/`.
The old shared-data files remained a V3 snapshot.

Before init repair, `--check` exited nonzero with all ten outputs stale. Asked
to rerun the skill through the project pointers without repairing anything,
the live session read the old shared-data files and returned V3 tokens.
This is an observed stale-pointer failure, not successful upgrade recovery.
The model did not repair the pointers itself.

After init, all ten outputs checked `ok`. Without another reload or restart,
`/skill:delivery-probe-read` in the same TUI read the updated project pointer
and stub, followed them into `package/library/`, and returned all three V4
tokens. The body marker remained `SKILL-BODY-REVISION-THREE`, as intended.

The TUI then quit normally. A fresh pi JSON/print process, with the same model
and read-only tool selection, invoked `/skill:delivery-probe-read` and read V4
from the editable library. It exited zero.

## Evidence and cleanup

Local raw evidence remains under
`/tmp/cp-delivery-pi-live-20261103.6PnEoE/evidence/`:

- exact per-stage prompts, message entries and terminal captures;
- `reload-screen.txt`, both complete persisted sessions, and fresh-process
  JSON events, stderr and exit code;
- install/init/check logs, including nonzero stale-check exit codes and the
  lookup warning;
- the one-off terminal driver, `verification.json`, final scratch package and
  pre-cleanup project snapshots.

Assertions checked expected tokens, read-only model tool calls, tool-free
metadata answers, the reload notification, clean/stale init outcomes and fresh
process exit. These checks supplement the recorded tool traces; they do not
establish acceptance beyond the scenarios above. Temporary evidence is not a
durable publication dependency; this report retains the observations.

Cleanup ran `cp-delivery-probe-init --remove`, uninstalled the isolated tool,
and removed its scratch project, source, configuration, catalog and credential
copy. Only the evidence directory remains. No active Commonplace installation,
pi settings, account or billing configuration was changed. No production code
was modified; pytest was not run for this probe.
