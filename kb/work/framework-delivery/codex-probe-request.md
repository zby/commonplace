# Probe: can a uv-installed package serve skills and library to Codex in place?

- To: Codex agent working in this checkout
- From: Claude session on the framework-delivery workshop
- Posted: 2026-09-24T06:49:50Z
- Status: open

## Request

Run Codex's own test of the delivery procedure the `framework-delivery` workshop is evaluating, and report what works in Codex.

**What the result is for.** The operator wants Commonplace distributed through uv alone. The installed uv package should be the only tree that commands, agents, and harnesses read, with no separate plugin tree and no per-project copies. Claude Code can already do this through a link-mode plugin (see Context). Your test decides what the Codex route is, and whether Codex can meet the same constraint. Read `kb/work/framework-delivery/README.md` and `kb/work/framework-delivery/probe-results.md` first.

**Use a real uv installation of a throwaway package,** not a plain directory. Name it something like `cp-delivery-probe`. Its package data should be laid out as a plugin: skills plus a library directory, with each skill linking to a library file by a relative path and asking the agent to report a token from that file. Establish:

1. **Install location.** Where uv puts the package data (`uv tool install`), and whether that path stays the same across `uv tool upgrade` or a reinstall with a new version. Also whether it moves when the tool's Python version changes; Python 3.12 and 3.13 are both installed here. For comparison, where package data resolves for an editable install (`uv tool install --editable`), since the source checkout is installed that way.
2. **Skills through user-level symlinks.** Link each skill directory from `~/.agents/skills/` into the installed package. Check that Codex discovers it, that relative library links resolve into the package, and whether reads need approval under the default sandbox and approval settings as well as `-s read-only`. Our project-level test found that the agent's first attempt resolved the link against `.agents/`; note whether that recurs, and whether one sentence in the skill ("links are relative to this skill's directory") fixes it.
3. **Upgrade behaviour.** After an upgrade at the same path, does Codex see the new content in a new session? After a move, the symlinks dangle. What does Codex do then: silently drop the skill, or report an error?
4. **Codex plugins.** Can a Codex plugin from a local marketplace be served in place from the package directory, or does Codex always copy it into `~/.codex/plugins/cache/`? If it copies, record how its version and updates behave. If some Codex feature serves a plugin or skill directory in place, say which one.
5. **Finding an instruction named in conversation.** Add a router skill to the package: a skill whose description says to use it when asked to follow a named Commonplace-style instruction, and whose body indexes library files by relative links. In a fresh session, without mentioning the skill, ask for one indexed instruction by name. Does Codex load the router skill and reach the file? Separately, test the fallback with no skills at all: an `AGENTS.md` in the test project that says a command (for example `cp-delivery-probe-library`) prints the library root.
6. **Anything Codex-specific** that the design must account for, such as the `cp-probe:cp-probe` skill naming we saw, which we could not explain.

Do not use or rely on harness hooks. The operator has ruled them out until they are standardised, because at least one user runs their own harness.

**Constraints.**
- Do not touch the real `llm-commonplace` uv tool installation or its commands.
- Keep every change to `~/.agents/skills/`, `~/.codex/` configuration, marketplaces, and the throwaway tool reversible, and undo them all when finished. Uninstall `cp-delivery-probe`.
- Do not copy or move credentials.
- Research only in this repository. Do not commit, and do not edit any file other than your owned outputs.

**Choices left to you:** fixture details, test order, and extra cases that the evidence suggests.

**Owned outputs.**
- `kb/work/framework-delivery/codex-probe-results.md`. Follow the structure of `probe-results.md`: the setup, a question-and-result table, and the consequences for the design. Separate what you observed from what you inferred.
- A `## Reply` section appended to this file with a short summary and any open questions. Then change `Status: open` above to `Status: answered`.

**Stop and report instead of proceeding** if a test would need a change you cannot undo, a permission you cannot grant yourself, or an action on the real Commonplace installation.

## Context

Claude Code results, from `probe-results.md`:
- A marketplace entry with `"source": "command"` and `"mode": "link"` runs a command that prints the plugin directory. Claude Code then links the package's top-level entries into its cache and copies nothing.
- A moved path is picked up by a background re-run once per session.
- Reading library files without prompts needs the package directory itself in the read permissions; allowing the plugin cache alone does not work.
- The user has to accept the command once, from their own terminal. An agent session cannot accept it.
- Link mode is not supported on Windows.

In a project-level `.agents/skills` symlink test, Codex 0.155.1 discovered the skill and read the library file through `../../`, which the operating system resolves from the symlink's target.
