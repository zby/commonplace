# Delivery probe results: Codex, revision 7

Installation, stopping on missing init, all three index-only reads, and nested
delegation passed. In the initial run, argument forwarding failed: the case agent reported literal
`$ARGUMENTS` instead of `kumquat`. It reached the real skill through the index
without reading a stub, so native stub argument delivery remains untested.

The [2026-10-26 rerun](#case-11-rerun-after-the-argument-routing-amendment)
passed through the amended index route in a fresh CLI session. The original
results below are retained; native stub forwarding remains untested.

- Harness and version: Codex collaboration sub-agents in the current session;
  local executable reports `codex-cli 0.163.0`. Cases were not separate CLI launches.
- Model: GPT-6 family, inherited without overrides; exact serving model ID and
  reasoning setting were not exposed to the runner.
- Operating system: Ubuntu 24.04.5 LTS; Linux 6.8.0-147-generic, x86_64.
- uv and Python versions: uv 0.13.4; installed tool Python 3.12.8.
- Tester and date: Codex agent, 2026-10-24, at the operator's request.
- Probe package revision: 7, copied from checkout
  `105095c2eb9f68c9414aca915a2e7805a69f909a`.
- Protocol: [revision 7](./probe-package/PROTOCOL.md), scoped by the
  [Codex run prompt](./run-prompts.md) to cases 0 and 8–11.

## Controls and reproducibility

`R` below means `/tmp/cp-probe-r7-eebaozh1`. The unchanged package was copied to
`R/package`; separate test-project copies were `R/project` and `R/fresh`.
`UV_TOOL_DIR`, `UV_TOOL_BIN_DIR`, and `UV_CACHE_DIR` were set per command to
`R/tools`, `R/bin`, and `R/cache`. This repeats revision 4's isolated uv layout,
instead of changing the default user tool installation. The installed library
root, `L`, was `R/tools/cp-delivery-probe/share/cp-delivery-probe`.

Each model case received only its scratch project path and the protocol prompt,
using a new collaboration agent with `fork_turns: "none"`. Case 9 used three
distinct agents, concurrently reading the same unchanged project. Follow-up
requests collected retrospective traces only; no case was rerun or corrected.
Case 0 was runner setup, as required by the run prompt, rather than a model case.

Fresh agents did not receive the setup conversation. However, they still received
the Commonplace repository's standing instructions and skill catalog. They were
not launched with the scratch project as their runtime working directory: each
discovered and explicitly read its scratch `AGENTS.md`. This tests fresh task
contexts with an explicit project path, not automatic instruction or native
skill discovery in a new CLI session rooted in that project. Case 8 additionally
read Commonplace's `cp-skill-library` instruction before the scratch instructions.
It ran no Commonplace command. No hooks or MCP servers were added or used for
delivery, and no library bodies were copied into projects.

## Harness facts

- Instruction file: repository `AGENTS.md` supplied in context; scratch
  `AGENTS.md` explicitly read. No Claude-style import route was exercised.
- Shell commands: available; file reads used `cat` through `exec_command`.
- Reads outside the project: succeeded without read approval in the inherited
  workspace-write environment, whose filesystem policy allows reads outside
  the workspace. No restrictive-read-policy claim follows.
- Agent Skills: the parent has a supplied catalog including project skills
  under `.agents/skills/` and system/plugin skills. Init wrote scratch stubs in
  both `.agents/skills/` and `.claude/skills/`; automatic discovery of those
  scratch stubs was not established. Cases 10 and 11 did not read them.
- Project permission settings: init wrote an uncommitted
  `.claude/settings.local.json` with
  `Read(//tmp/cp-probe-r7-eebaozh1/tools/cp-delivery-probe/share/cp-delivery-probe/**)`.
  Whether that Claude rule affects permissions was not tested here.
- Sub-agents: available, including nested delegation to a fresh context.

## Cases

| Case | Result | What happened | Prompts or denials |
|---|---|---|---|
| 0 Install and init | Pass, with setup network approval | Installed 1.0.0 with Python 3.12; init created both templates and eight stubs; check returned ten `ok` lines. | Sandbox DNS failure fetching hatchling; one escalation request, approved retry succeeded. |
| 1a–7 | Skipped by scope | Previous revision's results retained; no new claims about these cases. | None |
| 8 Fresh clone before init | Pass | Agent checked for the missing pointer, stopped, requested `cp-delivery-probe-init`, and reported no tokens. | Expected exit 1 from a file-existence test; no permission prompt. |
| 9 Emulated skill, run 1 | Pass | Explicit AGENTS read → library index → real skill → three relative references; all required V1 tokens. | No failed reads or permission prompts. |
| 9 Emulated skill, run 2 | Pass | Same route and tokens, in a fresh agent. | No failed reads or permission prompts. |
| 9 Emulated skill, run 3 | Pass | Same route and tokens, in a fresh agent. | No failed reads or permission prompts. |
| 10 Sub-agent | Pass through index | Case agent loaded the real skill from the index and launched a fresh nested agent; returned `DELEGATED-STEP-V1` without reading the delegated file itself. | No errors or permission prompts reported. |
| 11 Stub with arguments | Fail on observed route; native stub route untested | Agent bypassed the stub via the index and reported `SHARED-STEP-V1` and `ECHO-V1 $ARGUMENTS`. It did not carry `kumquat` into the real skill. | Initial attempt to execute `delivery-probe-echo kumquat` failed with command not found, exit 127. No failed file reads or permission prompts. |

### Case 0: exact init and check reports

Command: `uv tool install --python 3.12 R/package`, with the isolated uv
environment variables above. The first attempt failed resolving
`https://pypi.org/simple/hatchling/` after three retries with a DNS error.
The runner requested network escalation for that same installation command;
the approved retry built and installed the package. uv warned that `R/bin` was
not on PATH. The runner used absolute executable paths instead of changing
shell configuration. A separate `codex --version` preflight warned that it
could not create PATH aliases because the filesystem was read-only; it still
returned the version.

Init ran as `R/bin/cp-delivery-probe-init --root R/project`:

```text
Initialized delivery-probe project at /tmp/cp-probe-r7-eebaozh1/project
Created:
- AGENTS.md.template
- CLAUDE.md.template
- .claude/skills/delivery-probe-read/SKILL.md
- .claude/skills/delivery-probe-delegate/SKILL.md
- .claude/skills/delivery-probe-echo/SKILL.md
- .claude/skills/delivery-probe-library/SKILL.md
- .agents/skills/delivery-probe-read/SKILL.md
- .agents/skills/delivery-probe-delegate/SKILL.md
- .agents/skills/delivery-probe-echo/SKILL.md
- .agents/skills/delivery-probe-library/SKILL.md
- .cp-delivery-probe/library.md
- .gitignore
Refreshed pointers into the installed library:
- .claude/settings.local.json
```

The same command with `--check` exited zero:

```text
ok: .claude/skills/delivery-probe-read
ok: .claude/skills/delivery-probe-delegate
ok: .claude/skills/delivery-probe-echo
ok: .claude/skills/delivery-probe-library
ok: .agents/skills/delivery-probe-read
ok: .agents/skills/delivery-probe-delegate
ok: .agents/skills/delivery-probe-echo
ok: .agents/skills/delivery-probe-library
ok: .cp-delivery-probe/library.md
ok: .claude/settings.local.json
```

The runner separately confirmed both template files existed beside the adopted
instruction files. It deleted both skill directories for case 9, then reran
init after all three agents finished. Init recreated eight stubs and preserved
the matching templates.

### Case 8: missing-init trace

The agent read the repository's `cp-skill-library/SKILL.md`, searched scratch
filenames with `rg --files`, read scratch `AGENTS.md`, listed hidden files with
`rg --files --hidden -L`, and ran `test -f .cp-delivery-probe/library.md`.
The test exited 1. It stopped and asked the user to run init in `R/fresh`.
There was no session-start import error. It did not search for the library
elsewhere after discovering that the pointer was absent.

### Case 9: index-only traces

All three agents read these six files:

```text
R/project/AGENTS.md
R/project/.cp-delivery-probe/library.md
L/instructions/delivery-probe-read/SKILL.md
L/instructions/shared-step.md
L/types/probe-note.md
L/instructions/delivery-probe-read/references/read-detail.md
```

Runs 1 and 2 started with `rg --files` filtered for delivery/probe names and
`AGENTS.md`. Run 1 used separate `cat` calls for the three references; run 2
read them in one `cat`. Run 3 started with `ls -la`, then combined the AGENTS
read with `rg --files --hidden`; it also used one `cat` for the three references.
Every run returned `SHARED-STEP-V1`, `PROBE-NOTE-TYPE-V1`, and `READ-DETAIL-V1`
with their installed-library paths. No failed reads occurred.

### Case 10: delegation trace

The case agent searched project filenames, read `AGENTS.md`, listed hidden
files, read the library index, and read
`L/instructions/delivery-probe-delegate/SKILL.md`. It did not read a stub.
Its nested launch used `fork_turns: "none"`, task name `read_token`, and this
message, with `L` expanded to the absolute installed path:

> Read L/instructions/delegated-step.md and return the token it names.
> Read-only task; do not change files.

The nested agent returned `DELEGATED-STEP-V1`. The case agent confirmed that
it did not read `delegated-step.md` itself. No emulation was needed.

### Case 11: argument trace

Prompt: “Run the delivery-probe-echo check with the argument kumquat.”

The agent first tried the shell command `delivery-probe-echo kumquat`, which
does not exist. It then searched filenames, read scratch `AGENTS.md`, the
library index, the real echo skill, and the shared step. It did not read the
`.agents/skills/delivery-probe-echo/SKILL.md` stub. Its final answer included:

```text
SHARED-STEP-V1
ECHO-V1 $ARGUMENTS
The argument in the skill file still reads `$ARGUMENTS`.
```

It also gave the real skill's absolute path. No harness substitution was
visible. After the case finished, the runner inspected the stub and real skill.
The stub contains the pass-through paragraph, while the real skill says to
report the placeholder if it remains literal. Neither file was changed.

## Modifications to the package

None. A recursive comparison of the scratch package and workshop original
after the cases found no differences. No bumps, description edits, package
patches, hooks, MCP servers, credentials, or persistent user settings were used.

Execution adaptations were isolated uv directories, absolute paths for the
runner's init commands, and fresh collaboration agents supplied a scratch
project path instead of CLI sessions started there. These are runner choices,
not proven requirements for installing the design. Creating agents required no
administrator intervention. One retrospective trace request was temporarily
rejected because the three active workers occupied the available slots; it
succeeded after a worker finished and did not affect a probe case.

## Consequences for the design

- **Observed:** the revised missing-init instruction caused this agent to stop,
  unlike the recovery outside the intended route in
  [revision 4](./results-codex-r4.md). **Inferred:** the explicit stop rule helps;
  one observation does not establish reliability across harness configurations.
- **Observed:** all three fresh index-only reads resolved the real skill and
  its references. **Inferred:** the generated index can support file-based
  skill execution in this environment without native scratch skill discovery.
- **Observed:** nested fresh-context delegation succeeded through that index.
- **Observed:** echo failed through the index and did not consume the stub's
  forwarding paragraph. **Inferred:** this route needs an argument-binding
  instruction available to index consumers, or another explicit binding
  mechanism. This run does not show whether Codex follows the paragraph when
  it actually loads the stub. Test a session rooted in the scratch project
  before drawing a native-stub conclusion; do not patch the probe to hide this
  result.
- **Not established:** automatic scratch-project discovery, native stub argument
  forwarding, Windows/macOS behavior, restricted outside-project reads, or any
  upgrade behavior beyond the retained revision 4 evidence.

## Cleanup

Ran `cp-delivery-probe-init --root R/project --remove`; it removed all eight
stubs, the routing directory, read rule, ignore block, and templates. Ran
`uv tool uninstall cp-delivery-probe` with the same isolated directories; it
reported both executables uninstalled. Verified the routing directory,
templates, tool environment, and executables were absent. Deleted the entire
scratch root and verified its absence. `R/fresh` had never been initialized.

No real Commonplace installation or command was touched. No persistent shell
settings or credentials were changed. Normal harness conversation records were
left intact. Only this results file and a reply line in
[probe-request.md](./probe-request.md) were written in the repository. The
explicit Codex run prompt authorizes committing those two files despite the
generic probe request's no-commit rule. Validation uses diff and local-link
checks, not a `commonplace-*` command, to preserve the probe boundary.

The initial stage-and-commit command was denied because `.git/index.lock`
could not be created on the sandbox's read-only filesystem. The same operation
was retried with an escalation request and succeeded after approval. Recording
this post-run permission event also requires an escalated Git write. These
repository-write permissions are separate from the probe's library-read results.

## Case 11 rerun after the argument-routing amendment

**Pass through the index, 2026-10-26.** A fresh session returned
`SHARED-STEP-V1` and `ECHO-V1 kumquat`. The real skill still contained literal
`$ARGUMENTS`; the agent applied the request's argument itself.

The user requested this rerun after code revisions. The tested package was
revision 7 as amended on 2026-10-24, copied unchanged from checkout
`58ff93d6ea93e25b0827e28d8bf6593b7b9ea695`. The protocol amendment specifically
requires an index-route case 11 with no stubs to test the new routing instruction.
The fresh-context note in `run-prompts.md` recommends a CLI session rooted in
the project, addressing the initial collaboration run's directory limitation.

### Setup and session

Scratch root `E` was `/tmp/cp-probe-r7-echo-ibly2ph3`. Source and test-project
copies were `E/package` and `E/project`. uv used isolated `UV_TOOL_DIR=E/tools`,
`UV_TOOL_BIN_DIR=E/bin`, and `UV_CACHE_DIR=E/cache`. Installation used
`uv tool install --python 3.12 E/package`; init created eight stubs, both
templates, the routing file, ignore block, and Claude read rule. `--check`
returned ten `ok` lines. Both `.agents/skills/` and `.claude/skills/` were then
removed, leaving the routing file. No package files were modified; a recursive
comparison with the workshop package after the test found no differences.

The generated routing file contained this new instruction:

> If the request carries arguments, use them wherever the skill names its
> argument placeholder; reading the file does not substitute them.

Harness: `codex-cli 0.163.0`; uv: `0.13.4`. The fresh CLI used `gpt-6-astra`
with medium reasoning, explicitly preserving the user's configured model and
effort. It ignored user configuration to avoid loading configured MCP servers,
disabled hooks, retained authentication in its existing location, and used its
own read-only sandbox. No credentials were copied. Its working directory was
`E/project`, with `E/bin` prepended to PATH. The invocation was:

```text
codex exec --ephemeral --ignore-user-config
  -c 'model="gpt-6-astra"' -c 'model_reasoning_effort="medium"'
  -c 'features.hooks=false' --sandbox read-only --skip-git-repo-check
  --json -o E/final.txt
  'Run the delivery-probe-echo check with the argument kumquat.'
```

These lines describe one shell invocation. JSON events and stderr were captured
under `E`; the session received only the protocol prompt, with no setup history.

### Observed trace and result

The successful session made exactly three shell calls, all exiting zero:

1. `cat .cp-delivery-probe/library.md`
2. `cat E/tools/cp-delivery-probe/share/cp-delivery-probe/instructions/delivery-probe-echo/SKILL.md`
3. `cat E/tools/cp-delivery-probe/share/cp-delivery-probe/instructions/shared-step.md`

The second read returned literal `$ARGUMENTS`, establishing that reading the
file did not substitute the argument. The final response was:

```text
SHARED-STEP-V1

ECHO-V1 kumquat

/tmp/cp-probe-r7-echo-ibly2ph3/tools/cp-delivery-probe/share/cp-delivery-probe/instructions/delivery-probe-echo/SKILL.md
```

No failed reads, shell-command guessing, tool approval requests, or MCP calls
appeared in the successful session's event trace. No stub was available to read.
Unlike the initial run, it started directly with the project-relative routing
file instead of discovering and manually reading scratch `AGENTS.md`.

**Inference:** the amended routing instruction supports argument forwarding
through the index in this run. The package and execution context both changed
from the initial run, so this is not a controlled estimate of the instruction's
effect alone. It does not establish native stub behavior or repeated reliability.

### Permissions, cleanup, and recording

The initial installation failed on sandbox DNS resolution of PyPI's hatchling
index; an approved escalation of the same command succeeded. uv warned that
the isolated executable directory was not on PATH; it was prepended for the
probe session. The initial sandboxed CLI launch failed before a model turn:
`failed to initialize in-process app-server client: Read-only file system`.
An approved outer escalation allowed startup; the child still used
`--sandbox read-only`. The CLI version preflight also warned that PATH aliases
could not be created on the read-only filesystem. No persistent setting changed.

After the test, ran init `--remove` in `E/project`, then uninstalled the tool
using the same isolated uv directories. Verified the routing directory, tool
environment, and executables were absent, deleted `E` including raw traces,
and verified its absence. No Commonplace command or installation was touched.

Only this report and a new reply line were edited. Local links and whitespace
were checked without invoking a `commonplace-*` command. Committing the report
requires a separate Git-write escalation because this session's sandbox makes
`.git` read-only; that publication permission is separate from the case result.
