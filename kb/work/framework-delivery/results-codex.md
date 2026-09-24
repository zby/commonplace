# Delivery probe results: Codex

- Harness and version: codex-cli 0.155.1; fresh `codex exec --ephemeral` sessions and supplementary app-server checks.
- Model: configured `gpt-6-astra`, high reasoning effort.
- Operating system: Linux, Ubuntu 24.04, x86_64.
- uv and Python versions: uv 0.12.17; Python 3.12 and 3.13 selected with `--python` (installed managed versions: 3.12.8 and 3.13.1).
- Tester and date: Codex agent, 2026-09-24.

**Result:** User-level skill symlinks and the command-and-`AGENTS.md` base can read the uv-installed package in place. Ordinary local-marketplace plugin installation copies it. Python-version changes silently break skill discovery until the links are replaced. Relative links work at the filesystem level, but agents repeatedly simplified them incorrectly before recovering.

The [request](./codex-probe-request.md) changed during execution: its original version commissioned a tester-chosen fixture and `codex-probe-results.md`; the revision required the shared package and this filename. The cases below use a copy of the shared package introduced in commit `90e0ef8a`. Earlier tests with a separate fixture are identified as supplemental evidence, not shared-protocol results.

## Harness facts

- **Instruction file:** Codex loaded the test project's `AGENTS.md`. The router case used a separate empty project without that file.
- **Shell commands:** Supported. All four installed console commands were available on `PATH`.
- **Reads outside the project:** Succeeded under the default noninteractive CLI settings and explicit `-s read-only`. A supplementary ephemeral app-server turn also succeeded with verified workspace-write/on-request settings, without requesting approval.
- **Agent Skills directories:** User-level `~/.agents/skills/` was tested here. Project-level symlinks were tested in the [earlier workshop probe](./probe-results.md).
- **Symlinked skill directories:** Discovered and followed. After a Python-version move, dangling links were omitted without discovery errors.
- **Plugins:** A local marketplace accepted the shared fixture's existing `.claude-plugin/plugin.json`; no Codex manifest was needed. Installing the plugin copied its files into Codex's versioned cache.

**Permission distinction:** The parent sandbox could not start snap-packaged uv (`snap-confine` lacked `cap_dac_override`) or initialize Codex CLI (read-only filesystem). Approved outer execution was required for those processes and temporary home-directory writes. These setup approvals were separate from child-agent reads of package data; those reads needed no approval.

Plain `codex exec` reported `approval: never` and `sandbox: read-only`. Even a supplemental `codex -a on-request exec -s workspace-write` run reported approval `never`. The separate app-server test explicitly set `approvalPolicy: "on-request"` and `sandbox: "workspace-write"`, verified the returned settings, and stopped on any server approval request. It completed without one. Thus the on-request finding does not rely on the CLI flag being honored.

## Cases

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

## Modifications to the package

**None beyond the protocol's version bump.** The shared package was copied to `/tmp/cp-delivery-probe-shared-20260924`; its supplied `tools/bump.py 2` changed the package and Claude manifest versions and library tokens. The workshop's source package was not edited. Skills, instructions, CLI code, and build configuration stayed otherwise unchanged.

The Codex marketplace was a separate temporary fixture. Its `plugins/cp-delivery-probe` symlink pointed at the uv-installed plugin directory; its entry used `source: {"source": "local", "path": "./plugins/cp-delivery-probe"}`, with installation/authentication policy and category fields. It did not introduce another source copy of the library.

## Supplemental findings from the original request

Before the shared protocol appeared, a dependency-free local PEP 517/660 fixture named `cp-delivery-probe` tested versions 0.1.0–0.3.0. It used a `.codex-plugin/plugin.json`, three symlinked skills, and one instruction carrying version-specific `AMBER-...` tokens. It was uninstalled before the shared fixture was installed.

- **Observed: actual `uv tool upgrade` preserved the path on the same Python version.** Both reinstalling a newer version and upgrading from an updated local source worked. Fresh sessions read the newer token without changing links. `uv tool upgrade --python 3.13` moved the package and broke those links, consistent with the shared reinstall case.
- **Observed: the short relative-path sentence did not prevent failure.** A plain skill and one saying “Links are relative to this skill’s directory” both incorrectly read `/home/zby/.agents/library/...` and stopped. A router using the same sentence recovered by resolving its symlink. Adding the wording below made subsequent explicit-skill and router runs read the correct installed file without a failed read:

  > Links are relative to this skill’s directory. First run readlink -f on this SKILL.md path, then resolve relative links against the resulting real directory. Do not lexically collapse .. against the symlink path.

- **Observed: a manifest explains the name prefix.** App-server discovery named standalone links `cp-delivery-probe:cp-delivery-probe-explicit`, etc., even with the registered plugin uninstalled and `pluginId: null`. Temporarily hiding only the enclosing `.codex-plugin/plugin.json` removed the prefixes. Shared-fixture discovery likewise returned `cp-delivery-probe:delivery-probe-read` with its Claude manifest present. This explains the earlier `cp-probe:cp-probe` naming without implying a cached plugin installation.
- **Observed: an in-place API exists for skills.** With user links still dangling, app-server `skills/extraRoots/set` pointing at the installed Python 3.13 `skills` directory made `skills/list` discover those skills directly. This was discovery in that server process, not a test of persistent configuration or model consumption through that route. Schemas came from the installed CLI's `app-server generate-json-schema` command.
- **Observed: a genuinely skill-free command fallback worked after a move.** All remaining discovered skills were verified disabled, and the old probe links dangled. A fresh session followed a project `AGENTS.md` instruction to run the library-root command, found the Python 3.13 library, and returned its token.
- **Observed: the custom editable backend resolved into its source tree.** It used a `.pth` file. The shared fixture separately exercises its normal Hatchling editable build, so this custom-backend result is not the basis for case 7.

## Consequences for the design

- **Observed:** The base command route and user-level symlink route meet the one-tree requirement on the tested Linux setup. The tested local-marketplace plugin route does not; uv upgrades alone left cached plugin content stale.
- **Inferred:** Keep the command-and-`AGENTS.md` base and compute the library location from the installed package. It avoids embedding Python-specific paths in project instructions.
- **Inferred:** A skill setup operation must replace links after an interpreter or install-location change. The shared installer currently needs an explicit remove/install sequence. How to ensure this after uv-only upgrades without hooks remains unresolved; Codex's silent omission cannot serve as a warning.
- **Observed:** The shared skills' relative-link clarification did not prevent wrong first reads. The router's command fallback recovered successfully.
- **Inferred:** Preserve that fallback and make symlink resolution explicit where skills rely on relative links. The tested `readlink -f` wording is Linux-specific evidence, not a portable Windows or macOS recipe.
- **Inferred:** A custom app-server client could discover the package root and register extra skill roots at startup, without hooks or copies. Integration and lifecycle behavior still need a separate decision; the API discovery result alone does not establish a complete client workflow.
- **Inferred:** Expect manifest-derived `plugin:skill` names even for standalone symlinks. Packaging and invocation guidance should not assume the frontmatter name is always the full displayed name.
- **Observed limitation:** Ordinary tested sandboxes allowed package reads, but this does not establish behavior under custom filesystem restrictions. Windows, macOS, router reliability with a large index, same-version plugin refresh, and existing-session refresh were not tested. No universal claim that every possible Codex plugin mechanism copies files is established.

## Cleanup

The original fixture's plugin, marketplace, skill links, tool, and uv build cache were removed. Its temporary project trust entry was removed only after checking that this exact removal restored the recorded Codex configuration SHA-256. Credentials were not copied or moved; no hooks were used; the real `llm-commonplace` installation was not changed.

The shared fixture's two skill links, plugin, marketplace, empty cache directory, tool environment, four console commands, and uv build cache were also removed. Final checks confirmed no probe links, commands, tool environment, or plugin cache remained, and the Codex configuration matched the recorded SHA-256. Temporary source copies, test projects, and raw traces were removed after their findings were recorded here; normal Codex runtime logging was not rewritten or scrubbed.

Only this report and the request's status/reply were changed in the repository. Both files passed `commonplace-validate` with zero failures and warnings. No commit was made.
