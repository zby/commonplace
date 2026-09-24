# Probe request: does the uv-only delivery design work in your harness?

- To: agents in harnesses other than Codex, including Gemini CLI, OpenCode, Cursor, Goose, GitHub Copilot, Claude Code (a full rerun of the shared protocol), and enterprise or in-house harnesses
- From: Claude session on the framework-delivery workshop, at the operator's direction
- Posted: 2026-09-24
- Status: open

## Request

Run the shared delivery probe in your harness and record what works, what fails, and what you had to change.

**What the result is for.** Commonplace is a framework for agent-operated knowledge bases. It is moving to a single distribution channel: a Python package installed with `uv tool install`. The installed package is meant to be the only copy of everything agents read — skills, instructions, type specs — with no per-project copies and no separately published plugin. Codex has already run this probe. Your run tells the operator whether the design works in your harness, and what it would need there. The findings decide the design; they are not a ranking of harnesses.

**The design under test,** in three layers. Each must work without the ones above it:

1. **Base layer, for any harness.** The project's instruction file (`AGENTS.md` here) names two commands. One prints the library root; the other prints the path of a named instruction. The agent runs a command and reads the file it prints. This needs only a shell and file reads.
2. **Skills layer, where the harness supports Agent Skills.** Setup links (or, failing that, copies) the skills into the harness's user-level skill directory. The skills find library files through the same commands. A router skill indexes the library, so an agent asked for an instruction by name can find it.
3. **Harness-specific extras, optional.** An example is a plugin mechanism that serves the package in place without copying.

**What to run.** Use the probe package in this workshop, revision 3: [probe-package/PROTOCOL.md](./probe-package/PROTOCOL.md). Copy `probe-package/` to a scratch location, work on the copy, and run cases 0–7 as far as your harness allows. The package is a throwaway called `cp-delivery-probe`. Its commands, skills, and library files are placeholders that carry tokens such as `RETIRE-WIDGET-V1`, so a correct read is easy to check.

**Start from the same code, and record every change.** You may modify your copy when your harness needs it: a different instruction file name, another skill directory, a manifest format, a path convention. Each modification is a finding. Record what you changed, why your harness needed it, and the diff or an exact description.

**Rules.** These bind even if your harness does not load this repository's instructions:

- **No harness hooks** (session-start or any other). The operator has ruled them out until they are standardised.
- **No MCP servers** for delivering instructions.
- **Do not touch a real Commonplace installation** (the `llm-commonplace` uv tool or `commonplace-*` commands), and do not copy or move credentials.
- **Make every change reversible, and undo it when you finish.** That covers skill directories, harness configuration, plugins or extensions, permission settings, and the `cp-delivery-probe` tool.
- **Record observation separately from inference.** Name the harness version and model for each run. One run is one observation, not a reliability estimate.
- **Do not commit.** Write only your owned outputs, listed below.

**Harness facts we most need,** for the enterprise harness in particular. Record them in the results template's "Harness facts" section even where a case cannot run:

- Which instruction file does it load: `AGENTS.md`, another name, or none?
- Can the agent run shell commands?
- Can the agent read files outside the project directory? Under what setting, and can a user-level setting grant it once for all projects?
- Does it support Agent Skills? From which directories? Does it follow symlinked skill directories?
- Does it have a plugin or extension mechanism? Does that mechanism copy files, or can it serve a directory in place?
- Does it provide any configurable skill or instruction search path?

**Choices left to you:** the scratch locations, the order of cases, and extra cases your evidence suggests. For example, if your harness has its own way to register skill directories, test it.

**Owned outputs.**

- `results-<harness>.md` in this workshop, from [probe-package/RESULTS-TEMPLATE.md](./probe-package/RESULTS-TEMPLATE.md). If a file for your harness already exists, add a suffix.
- **If you cannot write to this repository** (for example, an agent inside an enterprise environment), return the filled-in template to the operator instead. Replace internal names, hosts, paths, and anything confidential with neutral labels such as `enterprise-A`. The design needs the behaviour, not the identity.

**Stop and report instead of proceeding** if a case would need a change you cannot undo, a permission you cannot grant yourself, installing software your environment's policy does not allow, or an action on a real Commonplace installation. Record the blocked case and the reason. A blocked case is a result.

## Context

The details are in [results-codex.md](./results-codex.md), [probe-results.md](./probe-results.md), and the protocol's "Known results" section. In brief:

- **Claude Code** serves the package in place through a link-mode plugin, whose marketplace entry runs a command that prints the plugin directory. The user must accept that command once, in their own terminal. Reading without prompts needs the package directory itself in the read permissions. Link mode is not supported on Windows.
- **Codex:**
  - The base layer and user-level skill symlinks worked, with no read approvals.
  - Agents misresolved relative links through the symlinks; revision 2 therefore uses the commands first.
  - A change of the uv tool's Python version moved the install path, and Codex silently dropped the dangling skills. Revision 2's commands warn about that, and `install-skills` repairs it.
  - Revision 3 therefore installs the tree as shared data under the tool environment's `share/` directory, whose path does not include the Python version. Codex has not yet run revision 3.
  - Codex copied local-marketplace plugins into its cache.
- **Not yet tested anywhere:** Windows and macOS, a router skill over a large library, and whether a session that is already running picks up an upgrade.
