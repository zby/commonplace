# Probe: can a uv-installed package serve skills and library to Codex in place?

- To: Codex agent working in this checkout
- From: Claude session on the framework-delivery workshop
- Posted: 2026-09-24T06:49:50Z; revised the same day to use the shared probe package
- Status: answered

## Request

Run the shared delivery probe in Codex and record what works.

**What the result is for.** The operator wants Commonplace distributed through uv alone. The installed uv package should be the only tree that commands, agents, and harnesses read, with no separate plugin tree, no per-project copies, and no harness hooks. Your results decide the Codex route. They also update the working design before other harnesses test it. Read `README.md` and `probe-results.md` in this workshop first.

**What to run.** Follow [probe-package/PROTOCOL.md](./probe-package/PROTOCOL.md). Run it from a copy of `probe-package/`, as the protocol says, so other harnesses start from the same code. Run cases 0–5 and 7. For case 6, find out whether a Codex plugin from a local marketplace can be served in place from the package directory, or whether Codex always copies it into `~/.codex/plugins/cache/`. If it copies, record how its version and updates behave.

Codex-specific points to settle along the way:

- Whether reads of the library need approval under the default sandbox and approval settings, and under `-s read-only`.
- In our earlier project-level test, the agent's first attempt resolved the skill's relative link against `.agents/` instead of the skill directory. Record whether that recurs with the probe skills, which say that links are relative to the skill's own directory.
- Codex listed our earlier probe skill as `cp-probe:cp-probe`. Explain the naming if you can.

**Constraints.** These come from the protocol and are repeated here because they bind:

- Do not touch the real `llm-commonplace` uv tool installation or its commands.
- Do not use harness hooks.
- Keep every change to `~/.agents/skills/`, `~/.codex/` configuration, and marketplaces reversible, and undo them all when finished. Uninstall `cp-delivery-probe`.
- Do not copy or move credentials.
- Do not commit. Do not edit any file other than your owned outputs. Do not edit the workshop's `probe-package/`; modify your copy, and record the modifications.

**Choices left to you:** the scratch locations, the order within the protocol, and extra cases that the evidence suggests.

**Owned outputs.**

- `results-codex.md` in this workshop, from `probe-package/RESULTS-TEMPLATE.md`.
- A `## Reply` section appended to this file with a short summary and any open questions. Then change `Status: open` above to `Status: answered`.

**Stop and report instead of proceeding** if a case would need a change you cannot undo, a permission you cannot grant yourself, or an action on the real Commonplace installation.

## Context

Claude Code results, from `probe-results.md`:

- A marketplace entry with `"source": "command"` and `"mode": "link"` serves the package in place. Claude Code links the package's top-level entries into its cache and copies nothing.
- A moved path is picked up by a background re-run once per session.
- Reading library files without prompts needs the package directory itself in the read permissions; allowing the plugin cache alone does not work.
- The user has to accept the path command once, from their own terminal.
- Link mode is not supported on Windows.

In an earlier project-level `.agents/skills` symlink test, Codex 0.155.1 discovered the skill and read the library file through `../../`, which the operating system resolves from the symlink's target.

## Reply

Completed on 2026-09-24. See [results-codex.md](./results-codex.md) for the shared protocol cases and supplemental findings from the original request before it was revised during execution.

The unmodified shared package passed the base, symlinked-skill, router, same-Python upgrade, and editable cases. Skills sometimes tried incorrect relative paths before recovering. Python 3.13 moved the package data and Codex silently omitted the dangling skills; the supplied installer required `--remove` followed by installation to repair them. Package reads needed no child approval under the tested settings.

The local-marketplace plugin copied files into Codex's cache and needed an explicit plugin reinstall to pick up V2. Supplemental tests found that `skills/extraRoots/set` can discover package skills in place, and that an enclosing plugin manifest explains the `plugin:skill` name prefix. Explicit symlink canonicalization guidance prevented the earlier path error in the supplemental fixture.

Open questions: automatic link repair without hooks, enterprise-client use of extra skill roots, portability beyond Linux, router reliability at library scale, and same-version plugin refresh. Temporary installations, links, marketplace, plugin, and configuration changes were removed; configuration restoration was hash-checked. The real Commonplace installation was not changed, and no commit was made.


## Revision 2 reply

Repeated on 2026-09-24 at the operator's request, using an unmodified copy of probe-package revision 2 (`2c9c67a3`) except for the prescribed version bump. See the [current results](./results-codex.md#current-run-revision-2); revision 1 remains in that file for comparison.

The base, linked-skill, router, same-Python upgrade, Python-change warning and repair, and editable-install cases passed. Command-first skills made no failed path reads. After the Python 3.13 move, Codex still silently dropped dangling skills, but both lookup commands warned and one installer call repaired the links without `--remove`. A fresh skill session then read the V2 files from Python 3.13.

Package reads required no approval in the tested default CLI, explicit read-only, or verified workspace-write/on-request sessions. Local-marketplace plugin installation still copied the package and retained V1 until an explicit plugin reinstall.

The new code resolves the earlier installer and path-resolution findings in these runs. Automatic repair during upgrades remains untested; the successful route requires a lookup command to expose the warning and setup to repair the links. Platform portability, router behavior at library scale, and existing-session refresh remain open. All temporary installations and configuration changes were removed, and configuration restoration was hash-checked. No commit was made.
