# Delivery probe results: Codex

## Current run: revision 2

**Result:** The revised package passed the base, linked-skill, router, same-Python upgrade, Python-change repair, and editable-install cases. Command-first skills made no failed path reads in these runs. After a Python change, the lookup commands warned about dangling links and one installer call repaired them without `--remove`. Codex still silently omitted the dangling skills. Local-marketplace plugins still copied the package into a cache.

This rerun supersedes the revision 1 findings about relative-path recovery and the installer's required remove/install sequence. The earlier run is retained below for comparison.

- Harness: codex-cli 0.155.1; fresh `codex exec --ephemeral` sessions, plus app-server discovery, plugin operations, and a permission test.
- Model: configured `gpt-6-astra`, high reasoning effort, for every model case; the app-server permission session also returned `gpt-6-astra`.
- OS: Ubuntu 24.04.5 LTS, Linux, x86_64.
- uv: 0.12.17. Python: 3.12.8 and 3.13.1.
- Tester and date: Codex agent, 2026-09-24, at the operator's request to repeat the probe against the revised supporting code.
- Package: revision 2, introduced by `2c9c67a3`; checkout HEAD at start `bd5756eecc8253a8ce6ad9047a109d6159c42b94`. The working tree was clean.
- Scratch copy: `/tmp/cp-probe-r2-20260924-rifom2c4/package`.

### Harness facts and controls

Codex loaded the test project's `AGENTS.md`, ran shell commands, and read the package outside the project. User-level links under `/home/zby/.agents/skills/` were discovered. The router's separate project contained no `AGENTS.md`. These observations agree with the documented [user skill location and symlink support](https://developers.openai.com/codex/skills#where-codex-loads-local-skills).

Each model case used a fresh session and the protocol's prompt verbatim. Per-process `skills.config` disabled every discovered skill for base cases and unrelated skills for skill/router cases. While the plugin was installed, its cached skills were also disabled in these model cases. No global skill settings were changed. Traces confirmed command-based library reads and reads of the linked skill files; no failed shell command occurred in the model cases. These are individual runs, not reliability estimates.

The first base case left sandbox and approval settings at CLI defaults. Subsequent CLI model cases explicitly used `-s read-only`. A separate ephemeral app-server session set `sandbox: "workspace-write"` and `approvalPolicy: "on-request"`; the server returned those settings. It completed the base prompt without an approval request. No additional read directory was granted. The outer probe runner had unrestricted filesystem access and needed no setup approval; that is separate from the child-session permission results.

### Cases

| Case | Result | What happened | Prompts or denials |
|---|---|---|---|
| 0 Install | Pass | `uv tool install --python 3.12 <copy>` installed 1.0.0 and four commands on PATH. The library root was under the uv tool's Python 3.12 site-packages. | None. |
| 1 Base layer | Pass | With all skills disabled, the agent ran `cp-delivery-probe-instruction retire-widget`, read the returned file, followed `./shared-step.md`, and reported `RETIRE-WIDGET-V1` and `SHARED-STEP-V1`. | None. |
| 2 Read permission | Pass | Explicit read-only skill/router and later base runs read package files. The separate verified workspace-write/on-request base session read the V2 files and reported both tokens without requesting approval. | No read allow-list, approval request, or denial. |
| 3 Skills (link) | Pass | The agent read the linked `delivery-probe-read/SKILL.md`, used both lookup commands, then read the installed files and reported `SHARED-STEP-V1` and `PROBE-NOTE-TYPE-V1`. | No failed reads; no relative-link fallback. |
| 3 Skills (copy) | Not applicable | Linked skills worked, so the protocol's conditional copy retry was not needed. | Not run. |
| 4 Router skill | Pass | Without `AGENTS.md` and without naming the skill, the calibration prompt selected `delivery-probe-library`. It ran `cp-delivery-probe-instruction calibrate-gadget` and reported `CALIBRATE-GADGET-V1`. | No failed reads; no relative-link fallback. |
| 5 Upgrade, same Python | Pass | The supplied `tools/bump.py 2` and a Python 3.12 reinstall kept the library path and links. Fresh base and linked-skill sessions returned their V2 tokens. `install-skills --check` reported both links `ok`. | None. |
| 5 Upgrade, Python change | Pass for warning and repair; automatic discovery still fails until repair | Reinstalling on Python 3.13 moved package data. Fresh `skills/list` omitted both probe skills with `errors: []`. Both lookup commands warned about dangling links; `install-skills --check` exited 1. A fresh base session still read the Python 3.13 V2 files. One `install-skills <dir>` call, without `--remove`, replaced both links. The check then passed, the warning disappeared, and a fresh linked-skill session read V2 from Python 3.13. | Expected diagnostic on stderr; no permission denial. |
| 6 Harness plugin | Fail for serving in place | A local marketplace pointed through a symlink to the installed plugin root. Codex copied seven files into its 1.0.0 cache; all had different inodes from the source and no cached entry was a symlink. After the uv upgrade the cached instruction remained V1 while the installed instruction was V2. Explicit plugin reinstall produced a 2.0.0 cache containing V2. | One initial RPC used a directory where `marketplacePath` required the JSON file and failed with “Is a directory”; corrected before installation. No permission request. |
| 7 Editable install | Pass | After removing the skill links, `uv tool install --python 3.13 --reinstall --editable <copy>` made the library root the copy's `src/cp_delivery_probe/plugin/library`. A fresh base session with all skills disabled read that source tree and returned `RETIRE-WIDGET-V2` and `SHARED-STEP-V2`. | None. |

The normal V1 library root was:

```text
/home/zby/.local/share/uv/tools/cp-delivery-probe/lib/python3.12/site-packages/cp_delivery_probe/plugin/library
```

The Python-change warning was:

```text
warning: installed delivery-probe skills do not match this package (2.0.0); rerun cp-delivery-probe-install-skills <dir>:
  /home/zby/.agents/skills/delivery-probe-library: dangling
  /home/zby/.agents/skills/delivery-probe-read: dangling
```

The repair printed `replaced (dangling) link` for each entry. The successful post-repair skill read used the same package path with `python3.13` in place of `python3.12`.

### Modifications and reproducibility

**No package changes beyond the protocol's version bump.** The copy's supplied bump script changed versions and tokens to 2.0.0/V2. The workshop's package was not edited. Initial SHA-256 values:

| File under `probe-package/` | SHA-256 |
|---|---|
| `src/cp_delivery_probe/cli.py` | `703aa866071c4a4c8efe073496370f97d3048dfaff0f94a56dc24218b34b0895` |
| `src/cp_delivery_probe/plugin/skills/delivery-probe-read/SKILL.md` | `4b9a0c76d84ccc3ac6a35a3aeb4f07d7737d84ac8128e6a7c39d623678848476` |
| `src/cp_delivery_probe/plugin/skills/delivery-probe-library/SKILL.md` | `c4716641d68462f253cd0e7a9614dd34c18352f0025cb4e33e2c3a5cf676f383` |

The separate Codex marketplace was named `cp-delivery-probe-r2-market`. Its `.agents/plugins/marketplace.json` entry used `source: {"source": "local", "path": "./plugins/cp-delivery-probe"}`, `policy: {"installation": "AVAILABLE", "authentication": "ON_USE"}`, and `category: "Productivity"`. `plugins/cp-delivery-probe` was a symlink to the uv-installed plugin root. This replaced the supplied Claude-specific marketplace mechanism for case 6 without modifying the package. App-server request schemas came from the installed CLI's `generate-json-schema` command.

### Consequences for the design

- **Observed:** The command-first revision removed the wrong initial reads seen in revision 1 in these individual runs. Both the explicit skill and the router read the installed library directly.
- **Observed:** The revised commands detect dangling links, and the installer repairs them in one call. This closes the revision 1 remove/install problem.
- **Inferred:** Keep the working design's command route and explicit repair operation. Repair remains an operator/setup action: Codex still silently drops dangling skills, and warnings appear only when a lookup command runs. This probe does not establish automatic repair during upgrades.
- **Observed:** Standalone linked skills still appeared as `cp-delivery-probe:delivery-probe-read` and `cp-delivery-probe:delivery-probe-library`, with `pluginId: null` before plugin installation. The earlier manifest-removal experiment explaining the prefix was not repeated.
- **Observed:** Local-marketplace installation still violated the one-tree requirement. The seven copied files included stale library content after the uv upgrade. A command-first skill could nevertheless reach the new installed library, so a correct token alone would not prove that the plugin was served in place.
- **Limitations:** Linux only; no running-session refresh, full-library router index, copied-skill case, custom filesystem restrictions, same-version plugin refresh, or repeated-trial reliability test. The in-place extra-skill-roots API from the earlier run was not retested.

### Cleanup

The probe's skill links, tool environment, four console commands, package-specific uv build cache, plugin, marketplace, and empty plugin-cache directory were removed. Codex had added a trust entry for the scratch test project; removing only that exact entry restored the initial configuration SHA-256 (`6ef8e1b3f1479d94acedac4b8913f27196aebb982635390ad17f5862c50a1194`). Temporary source copies, projects, schemas, runner scripts, and raw traces were removed after recording the findings. Normal Codex runtime logs were left alone.

No hooks were used. Credentials were not copied or moved. The real `llm-commonplace` installation and its commands were not changed. Repository changes are confined to this report and the request's new reply. Both passed `commonplace-validate` with zero failures and warnings. No commit was made.

## Earlier run: revision 1 (retained)

- Harness and version: codex-cli 0.155.1; fresh `codex exec --ephemeral` sessions and supplementary app-server checks.
- Model: configured `gpt-6-astra`, high reasoning effort.
- Operating system: Linux, Ubuntu 24.04, x86_64.
- uv and Python versions: uv 0.12.17; Python 3.12 and 3.13 selected with `--python` (installed managed versions: 3.12.8 and 3.13.1).
- Tester and date: Codex agent, 2026-09-24.

**Result:** User-level skill symlinks and the command-and-`AGENTS.md` base can read the uv-installed package in place. Ordinary local-marketplace plugin installation copies it. Python-version changes silently break skill discovery until the links are replaced. Relative links work at the filesystem level, but agents repeatedly simplified them incorrectly before recovering.

The [request](./codex-probe-request.md) changed during execution: its original version commissioned a tester-chosen fixture and `codex-probe-results.md`; the revision required the shared package and this filename. The cases below use a copy of the shared package introduced in commit `90e0ef8a`. Earlier tests with a separate fixture are identified as supplemental evidence, not shared-protocol results.

### Harness facts

- **Instruction file:** Codex loaded the test project's `AGENTS.md`. The router case used a separate empty project without that file.
- **Shell commands:** Supported. All four installed console commands were available on `PATH`.
- **Reads outside the project:** Succeeded under the default noninteractive CLI settings and explicit `-s read-only`. A supplementary ephemeral app-server turn also succeeded with verified workspace-write/on-request settings, without requesting approval.
- **Agent Skills directories:** User-level `~/.agents/skills/` was tested here. Project-level symlinks were tested in the [earlier workshop probe](./probe-results.md).
- **Symlinked skill directories:** Discovered and followed. After a Python-version move, dangling links were omitted without discovery errors.
- **Plugins:** A local marketplace accepted the shared fixture's existing `.claude-plugin/plugin.json`; no Codex manifest was needed. Installing the plugin copied its files into Codex's versioned cache.

**Permission distinction:** The parent sandbox could not start snap-packaged uv (`snap-confine` lacked `cap_dac_override`) or initialize Codex CLI (read-only filesystem). Approved outer execution was required for those processes and temporary home-directory writes. These setup approvals were separate from child-agent reads of package data; those reads needed no approval.

Plain `codex exec` reported `approval: never` and `sandbox: read-only`. Even a supplemental `codex -a on-request exec -s workspace-write` run reported approval `never`. The separate app-server test explicitly set `approvalPolicy: "on-request"` and `sandbox: "workspace-write"`, verified the returned settings, and stopped on any server approval request. It completed without one. Thus the on-request finding does not rely on the CLI flag being honored.

### Cases

Each model case used a fresh session. The protocol prompts were used verbatim. These are individual runs, not estimates of reliability across models or repeated trials.

| Case | Result (pass / fail / not applicable) | What happened | Prompts or denials |
|---|---|---|---|
| 0 Install | Pass | Real `uv tool install --python 3.12` installed the copied shared package at version 1.0.0. The library command returned the package-data path below. | Outer setup approval; no package dependency changes. |
| 1 Base layer | Pass | With skills disabled, Codex ran `cp-delivery-probe-instruction retire-widget`, read the returned file, followed its `./shared-step.md` link, and reported `RETIRE-WIDGET-V1` and `SHARED-STEP-V1`. | No child permission request or denial. |
| 2 Read permission | Pass | No additional read permission was necessary in case 1. Explicit read-only skill/router runs also read outside the project. See the supplemental on-request test above. | No child read approvals. No new allow-list required. |
| 3 Skills (link) | Pass, after recovery | The unmodified skill reported `SHARED-STEP-V1` and `PROBE-NOTE-TYPE-V1` from installed package files. Its first attempts incorrectly read `/home/zby/library/...`; it recovered using the literal `/home/zby/.agents/skills/delivery-probe-read/../../library/...` paths, which the OS resolved through the symlink. | Two missing-file errors; no permission denial. |
| 3 Skills (copy) | Not applicable | The link case ultimately passed, so the protocol's conditional copy retry was not needed. | Not run. |
| 4 Router skill | Pass, after recovery | In a project without `AGENTS.md`, the prompt “Calibrate the gadget using the delivery-probe procedure” selected `delivery-probe-library` and returned `CALIBRATE-GADGET-V1`. An initial read under `/home/zby/.agents/library/` failed; the router's built-in `cp-delivery-probe-library` fallback found the correct package file. | One missing-file error; no permission denial. |
| 5 Upgrade, same Python | Pass | Ran the supplied `tools/bump.py 2`, then reinstalled on Python 3.12. The package path and skill links were unchanged. Fresh base and skill cases returned the respective `-V2` tokens from the installed package. | No child permission request. The skill again recovered from incorrect relative-path resolution. |
| 5 Upgrade, Python change | Fail for automatic continuity; pass after repair | Reinstalling on Python 3.13 moved package data. Fresh `skills/list` returned no probe skills and `errors: []`. Merely rerunning `install-skills` failed because the dangling links already existed. Running it with `--remove`, then running it again, replaced them. A fresh skill session then returned `SHARED-STEP-V2` and `PROBE-NOTE-TYPE-V2` from Python 3.13 package files. | Installer: “already exists; remove it first with --remove.” This was not a sandbox denial. |
| 6 Harness plugin | Fail for serving in place | A temporary local marketplace pointed through a symlink to the installed package's plugin root. Codex copied it to `~/.codex/plugins/cache/cp-delivery-probe-market/cp-delivery-probe/1.0.0/`. All cached file inodes differed and no cached entries were symlinks. After the uv upgrade, cached files still held V1 while the package held V2. Explicit plugin reinstall created cache version `2.0.0`. | Outer plugin-management approvals; no command-source trust flow was used. |
| 7 Editable install | Pass | `uv tool install --reinstall --editable --python 3.13` resolved the library into `/tmp/cp-delivery-probe-shared-20260924/src/cp_delivery_probe/plugin/library`. With skill links removed and other skills disabled, a fresh base session used the instruction command and returned `RETIRE-WIDGET-V2` and `SHARED-STEP-V2` from that source tree. | No child permission request or denial. |

The regular shared-package library root was:

```text
/home/zby/.local/share/uv/tools/cp-delivery-probe/lib/python3.12/site-packages/cp_delivery_probe/plugin/library
```

After changing Python, only the interpreter-specific component changed to `python3.13`. `uv tool dir` returned `/home/zby/.local/share/uv/tools`.

For the base cases, per-process `skills.config` disabled the unrelated installed skills. V2 and editable runs also explicitly disabled the probe skill paths. No global skill setting was changed. The V1 base session started before the probe skills were installed and its trace used only the project command route.

### Modifications to the package

**None beyond the protocol's version bump.** The shared package was copied to `/tmp/cp-delivery-probe-shared-20260924`; its supplied `tools/bump.py 2` changed the package and Claude manifest versions and library tokens. The workshop's source package was not edited. Skills, instructions, CLI code, and build configuration stayed otherwise unchanged.

The Codex marketplace was a separate temporary fixture. Its `plugins/cp-delivery-probe` symlink pointed at the uv-installed plugin directory; its entry used `source: {"source": "local", "path": "./plugins/cp-delivery-probe"}`, with installation/authentication policy and category fields. It did not introduce another source copy of the library.

### Supplemental findings from the original request

Before the shared protocol appeared, a dependency-free local PEP 517/660 fixture named `cp-delivery-probe` tested versions 0.1.0–0.3.0. It used a `.codex-plugin/plugin.json`, three symlinked skills, and one instruction carrying version-specific `AMBER-...` tokens. It was uninstalled before the shared fixture was installed.

- **Observed: actual `uv tool upgrade` preserved the path on the same Python version.** Both reinstalling a newer version and upgrading from an updated local source worked. Fresh sessions read the newer token without changing links. `uv tool upgrade --python 3.13` moved the package and broke those links, consistent with the shared reinstall case.
- **Observed: the short relative-path sentence did not prevent failure.** A plain skill and one saying “Links are relative to this skill’s directory” both incorrectly read `/home/zby/.agents/library/...` and stopped. A router using the same sentence recovered by resolving its symlink. Adding the wording below made subsequent explicit-skill and router runs read the correct installed file without a failed read:

  > Links are relative to this skill’s directory. First run readlink -f on this SKILL.md path, then resolve relative links against the resulting real directory. Do not lexically collapse .. against the symlink path.

- **Observed: a manifest explains the name prefix.** App-server discovery named standalone links `cp-delivery-probe:cp-delivery-probe-explicit`, etc., even with the registered plugin uninstalled and `pluginId: null`. Temporarily hiding only the enclosing `.codex-plugin/plugin.json` removed the prefixes. Shared-fixture discovery likewise returned `cp-delivery-probe:delivery-probe-read` with its Claude manifest present. This explains the earlier `cp-probe:cp-probe` naming without implying a cached plugin installation.
- **Observed: an in-place API exists for skills.** With user links still dangling, app-server `skills/extraRoots/set` pointing at the installed Python 3.13 `skills` directory made `skills/list` discover those skills directly. This was discovery in that server process, not a test of persistent configuration or model consumption through that route. Schemas came from the installed CLI's `app-server generate-json-schema` command.
- **Observed: a genuinely skill-free command fallback worked after a move.** All remaining discovered skills were verified disabled, and the old probe links dangled. A fresh session followed a project `AGENTS.md` instruction to run the library-root command, found the Python 3.13 library, and returned its token.
- **Observed: the custom editable backend resolved into its source tree.** It used a `.pth` file. The shared fixture separately exercises its normal Hatchling editable build, so this custom-backend result is not the basis for case 7.

### Consequences for the design

- **Observed:** The base command route and user-level symlink route meet the one-tree requirement on the tested Linux setup. The tested local-marketplace plugin route does not; uv upgrades alone left cached plugin content stale.
- **Inferred:** Keep the command-and-`AGENTS.md` base and compute the library location from the installed package. It avoids embedding Python-specific paths in project instructions.
- **Inferred:** A skill setup operation must replace links after an interpreter or install-location change. The shared installer currently needs an explicit remove/install sequence. How to ensure this after uv-only upgrades without hooks remains unresolved; Codex's silent omission cannot serve as a warning.
- **Observed:** The shared skills' relative-link clarification did not prevent wrong first reads. The router's command fallback recovered successfully.
- **Inferred:** Preserve that fallback and make symlink resolution explicit where skills rely on relative links. The tested `readlink -f` wording is Linux-specific evidence, not a portable Windows or macOS recipe.
- **Inferred:** A custom app-server client could discover the package root and register extra skill roots at startup, without hooks or copies. Integration and lifecycle behavior still need a separate decision; the API discovery result alone does not establish a complete client workflow.
- **Inferred:** Expect manifest-derived `plugin:skill` names even for standalone symlinks. Packaging and invocation guidance should not assume the frontmatter name is always the full displayed name.
- **Observed limitation:** Ordinary tested sandboxes allowed package reads, but this does not establish behavior under custom filesystem restrictions. Windows, macOS, router reliability with a large index, same-version plugin refresh, and existing-session refresh were not tested. No universal claim that every possible Codex plugin mechanism copies files is established.

### Cleanup

The original fixture's plugin, marketplace, skill links, tool, and uv build cache were removed. Its temporary project trust entry was removed only after checking that this exact removal restored the recorded Codex configuration SHA-256. Credentials were not copied or moved; no hooks were used; the real `llm-commonplace` installation was not changed.

The shared fixture's two skill links, plugin, marketplace, empty cache directory, tool environment, four console commands, and uv build cache were also removed. Final checks confirmed no probe links, commands, tool environment, or plugin cache remained, and the Codex configuration matched the recorded SHA-256. Temporary source copies, test projects, and raw traces were removed after their findings were recorded here; normal Codex runtime logging was not rewritten or scrubbed.

Only this report and the request's status/reply were changed in the repository. Both files passed `commonplace-validate` with zero failures and warnings. No commit was made.
