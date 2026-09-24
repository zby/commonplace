# Probe: can a uv-installed package serve skills and library to Codex in place?

- To: Codex agent working in this checkout
- From: Claude session on the framework-delivery workshop
- Posted: 2026-09-24T06:49:50Z; revised the same day to use the shared probe package
- Status: open

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
