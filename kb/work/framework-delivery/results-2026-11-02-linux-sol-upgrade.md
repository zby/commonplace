# Linux delivery acceptance: upgrades and recovery, 2026-11-02

The isolated published Commonplace 0.3.3 install passed init, pointer checks and
landing validation. The portable Workjig 0.3.0 recovery fixture passed on Linux.
Synthetic upgrade checks established pointer staleness and repair, and a live pi
process retained its old skill description after init while a fresh process
loaded the new description. Fresh Codex Sol sessions read the old V2 library
through stale pointers, then the moved V4 library after repair and a same-root
library-only update. A copied user-level pi extension exposed `subagent`
in the installed project; its model-backed worker acceptance remains blocked.

Setup began on 2026-11-01; the approved model attempt and upgrade checks ran on
2026-11-02. The operator explicitly advanced Linux upgrade work before the
Windows PyPI checkpoint. This result does not establish Windows acceptance.

## Provenance and boundaries

- Host: Linux x86_64, kernel `6.8.0-147-generic`, glibc 2.39; Bash.
- Source HEAD at setup: `c15537e08fefc75ef59dd579848080ed3441c058`;
  initial working tree clean. Release baseline: PyPI `llm-commonplace==0.3.3`,
  release commit `526de4edd`; dependency `workjig==0.3.0`.
- uv 0.13.4; initially uv-managed CPython 3.12.8. Later isolated reinstalls
  selected `/usr/bin/python3`, CPython 3.12.3, so the existing Codex isolation
  helper could start the installed commands without exposing a home-directory
  Python runtime. All pointer checks stayed `ok` across this interpreter change.
- pi 1.3.0; selected model `openai/gpt-6.1-sol`, thinking `low`.
  Codex CLI 0.164.0; selected model `gpt-6.1-sol`, effort `low`.
  No Opus model was launched.
- Synthetic fixture: revision 7, dated 2026-10-24, with the 2026-11-01 worker
  clarification. Only its disposable copy changed. V1/V2/V3/V4 denote fixture
  tokens and package versions, not Commonplace releases.
- Root: `/tmp/cp-delivery-20261101-sol`; synthetic project `project/`;
  published-package project `real-project/`; package copy `package/`;
  evaluator records `records/`. No init ran in the source checkout.

Every uv tool operation used isolated `UV_TOOL_DIR` and `UV_TOOL_BIN_DIR`.
Commands were called by bare name with the intended isolated bin directory
first on PATH. No active Commonplace user tool, shell profile, account, billing
setting, credential or persistent user configuration was changed. `HOME` and
`CODEX_HOME` retained their original values. The pi configuration directory was
the supported `PI_CODING_AGENT_DIR=<root>/pi-user`; its session directory was
also under that disposable directory.

The initial package download failed sandbox DNS resolution. The approved retry
downloaded the probe build dependency and the published release. The first
normal-permission pi model attempt failed with a connection error. The approved
retry reached the provider, which returned a terminal credit error. No success
was inferred from pi's exit status 0 in the first failed attempt.

The full installed-wiki rehearsal was not invoked. Its isolation guidance and
existing Codex launcher were used for these narrower delivery checks.

## Published-package checks

Initial tool operations used:

```bash
delivery_root=/tmp/cp-delivery-20261101-sol
export UV_TOOL_DIR="$delivery_root/tools"
export UV_TOOL_BIN_DIR="$delivery_root/bin"
export UV_CACHE_DIR="$delivery_root/cache"
export TMPDIR="$delivery_root/tmp"
export PATH="$delivery_root/bin:$PATH"
uv tool install --python 3.12 "$delivery_root/package"
uv tool install --python 3.12 llm-commonplace==0.3.3
```

In `real-project/`, `git init`, `commonplace-init --name delivery-acceptance`,
`commonplace-init --check` and `commonplace-validate landings` passed. The two
generated control-plane templates were adopted by renaming them to `AGENTS.md`
and `CLAUDE.md`. Check reported 26 `ok` outputs: 24 skill stubs, the index and
the read-rule settings file. Distribution metadata reported 25 entry points.
The effective library was `<root>/tools/llm-commonplace/share/commonplace`.

The installed Commonplace and Workjig modules resolved under that isolated
tool's `site-packages`; both reported the expected versions. Neither had an
editable `direct_url.json`. This was a published-package install with no local
source overlay. It did not test an upgrade between two real releases.

## Harness facts

pi loaded the synthetic project's `AGENTS.md` pointer and discovered its four
native `.agents/skills/` stubs. RPC `get_commands` returned
`skill:delivery-probe-read` with project scope and the expected stub path.
`--approve` was a process-local project trust choice. It was not a filesystem
sandbox or evidence about Claude's read-rule effect. pi sessions used
`--no-mcp --no-prompt-templates --no-themes --offline`; `--offline` disables
startup network work, not model calls. Upgrade catalog checks used only the
RPC protocol and made no model calls.

The live catalog process used `--mode rpc --no-session --no-extensions` and
`--tools read`. One PID, `/proc` start value and session ID were retained across
library and metadata changes. This was an actual ongoing process, not a fresh
process reopening a saved chat. Its session ID was
`01a19b94-2553-7643-8a28-21d4edda8e4e`.

The model-backed pi attempt returned `You have no credits remaining`. It made
no tool calls and returned no delivery tokens. Existing pi authentication had
no `openai-codex` provider configured. No credential was copied to add one.

For Codex, the existing isolation helper mounted saved login state read-only,
hid the checkout, personal config, memories, skills and evaluator records, and
made the project/tool directories read-only. Its complete isolation probe
passed. The first sandbox request failed workspace-routing connectivity; its
process timeout was 120 seconds. The approved saved-login retry succeeded.
Its retained turn context confirms `gpt-6.1-sol`, effort `low`, scratch-project
working directory, approval policy `never` and a read-only sandbox. It completed
in 17.02 seconds. The model read the index/stub, the real old-root skill and its
three linked files, and returned `SHARED-STEP-V2`, `PROBE-NOTE-TYPE-V2` and
`READ-DETAIL-V2`. All three shell read commands succeeded. It ran no init or
probe command and observed no warning. This is a successful stale-pointer read,
not evidence that a file-only session notices an installation move. That first
helper exposed the original tool/bin roots; the final case adds explicit
read-only mounts of the moved roots and places their bin first on PATH.

## Cases

| Selected case | Result | Observation |
|---|---|---|
| Probe install/init | Pass | Initial V1 install; ten `ok` outputs; adopted project instruction files retained. |
| Library-only V1 to V2 | Deterministic pass; pi model read blocked | `python3 tools/bump.py 2`, reinstall at the same root, then ten `ok` without init. |
| Library-only V3 to V4 | Pass in the combined fresh Codex case | After V3 pointer repair, V4 reinstall at that same moved root needed no init; check stayed ten `ok` and Sol read all three V4 tokens. |
| Changed skill metadata | Pass for detection/repair | Appending ` Metadata marker META-V2.` to the read skill description made exactly its two stubs and the index stale. Check exited 1; the library command warned about all three; one init restored ten `ok`. |
| Already-running pi catalog | Pass with a session limit | The same RPC process kept the original skill description before and after metadata repair. A fresh process returned the description containing `META-V2`. No `/reload` was tested. |
| Moved installation | Scoped pass for detection, repair and fresh-session read | A separate tool/bin root held V3 while the old root retained V2. With the new bin first on PATH, all ten outputs were stale and the library command warned. Init repaired them; the combined final fresh session read V4 from the moved root. Both library paths remained readable before cleanup. |
| Fresh Codex stale-pointer read | Pass as an observation of the limit | Saved-login Sol followed the unrefreshed project pointers and returned all three V2 tokens from the old root without a warning. |
| pi user-level extension copy | Startup prerequisite passed; worker acceptance blocked | The copied extension registered an active `subagent` tool in `real-project/`. No worker obtained a model response. |
| Workjig recovery fixture | Linux pass | Both interrupted-marker cases preserved bytes and were rejected by `Run`; fresh records were accepted. |

Other protocol cases were not rerun. This is not a fresh baseline certification
of all file/index/argument routes, all upgrade forms, or every worker requirement.

### Exact synthetic mutations

The disposable package was installed normally, not editable. Its upgrade
commands, after selecting system Python, were:

```bash
uv tool install --offline --reinstall --python /usr/bin/python3 "$delivery_root/package"
uv tool install --offline --reinstall --python /usr/bin/python3 llm-commonplace==0.3.3
python3 tools/bump.py 2
uv tool install --offline --reinstall --python /usr/bin/python3 "$delivery_root/package"
cp-delivery-probe-init --check
```

The bump command ran from `package/`; project commands ran from `project/`.
The metadata append was the only manual skill edit. Reinstall, check,
`cp-delivery-probe-library`, init and check followed in that order.
`python3 tools/bump.py 3` then produced the next synthetic version. A new
installation used `UV_TOOL_DIR=<root>/tools-moved`,
`UV_TOOL_BIN_DIR=<root>/bin-moved`, that bin first on PATH, and:

```bash
uv tool install --offline --python /usr/bin/python3 "$delivery_root/package"
cp-delivery-probe-init --check
cp-delivery-probe-library
```

After the fresh stale-pointer read, a complete pre-repair project snapshot was
retained. Init against the moved V3 installation repaired all ten outputs;
check passed and the library command returned the new root without a warning.
The next bounded setup ran `python3 tools/bump.py 4`, reinstalled with
`uv tool install --offline --reinstall --python /usr/bin/python3 "$delivery_root/package"`
at that same moved root and checked ten `ok` outputs **without another init**.
The final fresh Sol session read the updated project index/stub, the real
moved-root skill and its three linked files. It returned `SHARED-STEP-V4`,
`PROBE-NOTE-TYPE-V4` and `READ-DETAIL-V4`; all three shell read commands passed,
with no init, repair, warning or missing file. It completed in 18.42 seconds.
The retained turn context again confirms Sol, low effort and a read-only
scratch-project session. This establishes the combined repaired-root and
library-update outcome. There is no independent model read between V3 repair
and V4 update, or model-backed already-running-session read after either change.

Both fresh Codex sessions received this prompt:

> Run the delivery-probe-read check. Use current on-disk files for this check,
> and report the paths you actually read and their tokens. Use only this
> installed project and its pointers. Do not use any Commonplace source
> checkout. Do not run init or repair the project. Report any warning or
> missing file exactly.

The first used `scripts/run_isolated_codex.py` with
`--model gpt-6.1-sol --effort low --auth saved --access read-only --timeout 120`.
The final one-off wrapper reused its `sandbox`, `probe`, `codex_args` and
`run_bounded` functions, adding only read-only mounts of `tools-moved` and
`bin-moved`, and the moved bin first on PATH. Its additional boundary check
verified both moved roots were immutable and that the effective probe command
returned the moved library. Exact launches, prompts and session records are
retained with the evidence.

The protocol copy and Commonplace 0.3.3 share the relevant mechanisms: absolute
stub pointers, the generated skill index, description-based staleness, the
`Read(//…/**)` rule, and command-time warnings. Current Commonplace also has its
own scaffold and manifest, source/worktree routing and Windows junction
handling. The fixture has four skills; the real package has twelve. Fixture
results do not certify those other surfaces or a real release directory move.

### Installed-project pi copy

The extension tree `.pi/extensions/subagent/` and worker
`.pi/agents/commonplace-worker.md` were copied from source HEAD into
`<root>/pi-user/extensions/subagent/` and `<root>/pi-user/agents/`. All 14
extension files matched their source SHA-256 values. The worker copy was
unchanged. The project had no checkout `.pi` directory.

This uses the supported disposable pi configuration-directory override to test
the user-level layout prescribed by INSTALL.md; it does not change `~/.pi`.
An additional observation-only extension recorded the runtime's registered and
active tools during `session_start`. It did not implement delegation. In the
published-package project's fresh startup, `subagent` was active and no
extension load failure occurred. No prompt was supplied, so no API call ran.

This establishes loading from the copied user-level layout. It does not pass
case 10, prove a fresh worker context, or establish worker lifecycle, capacity,
nesting, tool limits or inherited resources in an installed project.

## Portable Workjig recovery fixture

The [fixture](./workjig-030-recovery-fixture.py) uses only the installed Workjig
public API and Python's standard library. It requires version 0.3.0, rejects an
import outside the installed distribution or an editable distribution, and
prints interpreter/module provenance with its result. It launches no workers
and removes its temporary records after a successful run.

The fixture checks empty and `b"interrupted"` pre-existing `.lock` bytes. Each
case repeats `Run` rejection and `hold` acquisition twice, then checks rejection
once more. It verifies unchanged bytes, no `run.json`, and released ownership.
It separately verifies a fresh `Run`, repeated fresh `hold` followed by `Run`,
and shared lock exclusion. **`hold` preserves evidence; `Run` rejects the
interrupted state.** `hold` does not validate or reject that state itself.

Linux invocation, from the scratch published-package project:

```text
/tmp/cp-delivery-20261101-sol/tools/llm-commonplace/bin/python /home/zby/llm/commonplace/kb/work/framework-delivery/workjig-030-recovery-fixture.py
```

The first run passed over Python 3.12.8. After adding the explicit installed-origin
guards, the focused rerun passed over Python 3.12.3. Both used the isolated
published Workjig 0.3.0 distribution. This is direct dependency acceptance,
separate from Commonplace's software suite.

For the next Windows run, copy the fixture to that machine and run it with the
interpreter of the installed 0.3.3 tool, without a source overlay:

```powershell
& (Join-Path (uv tool dir) 'llm-commonplace\Scripts\python.exe') '<copied-fixture-path>'
```

Retain the JSON output and verify its Windows interpreter/module paths. A
nonzero exit or missing prerequisite remains a failure or blocker. No Windows
result is claimed here; the fixture removes the previously missing-fixture
prerequisite for that check.

## Evidence, validation and cleanup

Raw command outputs, exact RPC inputs/events, provider failures, copy hashes,
package provenance and launcher records are retained under
`/tmp/cp-delivery-20261101-sol-evidence/records/`. The same evidence directory
also retains the one-off drivers, synthetic package, pre-cleanup projects,
copied pi extension/worker and tested fixture. They are not product additions.
The parent approved retention before cleanup. The pre-cleanup archive is:

```text
/tmp/cp-delivery-20261101-sol-evidence.tar.gz
SHA-256: 2ab382f183e8ae0efe3f9764dbceea0c93e87b32c2e1f13a6e80f2622f9e97f8
```

The archive is 229,912 bytes and has 354 members. Inspection covered 240 files;
no credential-named file or active secret environment value was included.
Installed tools, uv cache/build temporaries and pi's generated empty
`auth.json` were omitted. Saved Codex credentials were only mounted read-only
in the temporary namespace and were never copied. The raw evidence directory
is mode 0700 and the archive is mode 0600.

Cleanup completed after both model scenarios exited. `cp-delivery-probe-init
--remove` ran in both scratch projects. The probe was uninstalled from both
isolated tool roots and Commonplace only from its isolated root. Each isolated
`uv tool list` then reported `No tools installed`. The scratch root was removed;
the archive and raw evidence directory remain. The active command still resolves
to `/home/zby/.local/bin/commonplace-init`. The full cleanup record is
`/tmp/cp-delivery-20261101-sol-evidence/cleanup.json`, written after sealing the
pre-cleanup archive and retained separately from it.

The report passed `commonplace-validate` with no failures or warnings, and
`git diff --check` passed. The parent separately ran the required general and
tooling suites: 104 tests passed with `-m ''` under Linux Python 3.13.1, and
fixture Ruff passed. The fixture's focused installed-dependency runs under
Python 3.12.8 and 3.12.3 are separate evidence. No additional model calls,
product repair, support-scope change or release was made.
