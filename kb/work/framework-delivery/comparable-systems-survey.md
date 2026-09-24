# Comparable systems survey

Collected 2026-09-23 by four research agents: two web surveys and two code inspections of local clones under `related-systems/`, updated the same day. Claims marked *unverified* come from search summaries or inference. File paths are relative to each clone.

## Harness mechanisms

| Harness | Loose skills | Plugins | No-copy route |
|---|---|---|---|
| Claude Code | `~/.claude/skills`, project `.claude/skills`, managed dir, `.claude/skills` inside `--add-dir` dirs; symlinked skill dirs supported; no setting for extra dirs | Marketplace plugins copied to `~/.claude/plugins/cache` per version. `command` source in link mode (v2.1.229+) runs a command that prints a plugin dir and uses it in place, re-run once per session; not on Windows. Local-directory marketplaces and `--plugin-dir` load in place. Components outside the plugin root are rejected, symlinks included | Link-mode plugin; symlink |
| Codex | `.agents/skills` up to repo root, `~/.agents/skills`, `/etc/codex/skills`; `[[skills.config]]` only enables/disables; follows symlinks | Copied to `~/.codex/plugins/cache`, including local plugins; issue #18863: cache install drops symlinks | Symlink only |
| OpenCode | `skills` array in `opencode.json` takes absolute paths and HTTP catalogs (v2 docs) | — | Config path |
| Gemini CLI | `~/.gemini/skills`, `~/.agents/skills`, workspace dirs; `/skills link` symlinks | Extensions installed to `~/.gemini/extensions`; `extensions link` symlinks a dev dir | Symlink |
| Goose, Cursor | Fixed dirs; no configurable path found | — | Symlink at best |

Requests for configurable skill paths were closed without visible maintainer rationale: Claude Code #22902, #77766 (stale); Codex #13074 (not planned). Codex #22869 appeared open. The Agent Skills spec (agentskills.io) does not mandate locations and lists user-configured paths as optional; it does not address packaging or versioning.

Sources: code.claude.com/docs/en/skills, /plugins-reference, /plugin-marketplaces; learn.chatgpt.com/docs/build-skills; opencode.ai/v2/docs/skills/; geminicli.com/docs/cli/skills/; agentskills.io/client-implementation/adding-skills-support.

## Systems inspected in local clones

| System | Ships | Channel | Copied vs in place | Drift handling |
|---|---|---|---|---|
| **GBrain** | Bun CLI + MCP server, ~80 skills, shared convention docs | Claude and Codex plugins over a generated, version-stamped `plugin/skills` tree (`scripts/generate-plugin-tree.ts`); `skillpack scaffold` into harness skill dirs; stub mode | Plugin: in place, skills reach `../conventions/*.md` relatively. Scaffold: copies, additive, "local edits win". Stubs: frontmatter-only SKILL.md telling the agent to call `gbrain skill <slug>` or MCP `get_skill` — "always current" (`src/core/skillpack/harness-bridge.ts:76-78,291-312`) | sha256 per file at install (`bridge-state.ts:10-16`) → three-way: local edit vs upstream change; `skillpack reference --apply-clean-hunks` merges clean upstream hunks. MCP launcher via `${CLAUDE_PLUGIN_ROOT}` is Unix-only |
| Ars Contexta | ~249-note methodology library, meta-skills, skill templates, hooks | Claude Code plugin only | Library read in place via `${CLAUDE_PLUGIN_ROOT}/...`; working skills generated into project `.claude/skills` by `/setup` | `generated_from` version stamp; `/upgrade` uses `git status` and an LLM judgment per skill; keep/merge/replace with archive; rejects hashing deliberately |
| nvk/llm-wiki | One skill with ~22 references, commands, Python CLI, hooks | Claude and Codex plugins; OpenCode fetches a raw GitHub URL each session | In place from plugin cache; relative reference links; `${CLAUDE_PLUGIN_ROOT}/bin/llm-wiki` | Harness plugin update; README documents manual cache repair; replaced a symlink with a copy because the Codex cache broke it |
| Basic Memory | Python CLI + MCP server; Claude and Codex plugins; shared skills | `bm install claude-code/codex` wraps the harness plugin install; skills also shipped as **wheel package data** (`pyproject.toml` force-include → `basic_memory/data/...`), located with `importlib.metadata.distribution().locate_file`, and copied to user-level Tau/Pi dirs | Hooks run `uv run --script` and import the installed package | Install plan compares previous bytes, refuses changes made after preview (`cli/commands/install.py`); schemas seeded once, customizations win |
| claude-obsidian | Python core, 17 skills, hooks, templates | Claude Code plugin; `setup-multi-agent.sh` symlinks each skill into other harnesses' dirs | Symlinks to one canonical tree; skills resolve their own install root | Never replaces existing files (`CONFLICT`); `--check` verifies link targets |
| OKF Harness | npm packages, one skill with references | Claude and Codex marketplaces; `npx @okf-harness/setup` | User-level host skill + per-workspace rendered skills | Frontmatter markers: installed / version-drifted / unmanaged-conflict; workspace pins exact runtime version |
| hyalo | Rust CLI, skills, rule, managed CLAUDE.md/AGENTS.md section | `hyalo init` writes templates embedded in the binary; Codex plugin | Copies; removes project copies when the Codex plugin is used | `hyalo:managed` marker; refuses to overwrite unmarked files or write through symlinks |
| ai-modules | Skills, agents, commands, hooks for six harnesses | Claude and Codex plugins; `deployment.sh` copies | Copies ("every deployed artifact is a copy") | Log of deployed paths for uninstall; no edit detection |
| memwiki, ai-memex-cli | npm CLIs with embedded instruction text / skill templates | init copies into project | Copies | Blind overwrite |

## Systems found on the web only

- **beads:** a SessionStart hook runs `bd prime`, which prints instructions from the installed binary; MCP only as fallback, citing 10–50k tokens of MCP schemas versus 1–2k for `bd prime`.
- **spec-kit:** `uv tool` CLI plus `specify init` copies templates; CLI and project files upgrade separately; managed files overwritten only if unchanged since install.
- **antfu/skills-npm:** skills inside npm packages, symlinked from `node_modules`; names "skills and tools update separately" as the problem.
- **pixi-skills** (pavel.pink, 2026-02-09): skills in conda packages pinned to the library version, symlinked into the project.
- **Vercel `npx skills`:** one canonical `.agents/skills`, other harness dirs symlinked to it; copies where symlinks fail.
- **gentle-ai #4646:** proposes release-time content-hash manifests and a `skills verify` command after stale copies broke command references.

## MCP as a channel

Not the common answer for instructions. Recorded drawbacks: context cost of tool schemas (Task Master ~21k tokens), server instructions capped or dropped by some clients, and poor adherence (Serena's docs report Claude Code largely ignoring its instructions). The trend runs toward skills or CLI plus hooks for knowledge, MCP for tool access. GBrain's `get_skill` is the exception worth examining.

## Language-native distribution

Several systems ship agent content inside their language package: Basic Memory (wheel package data), OKF Harness and memwiki (npm), hyalo (compiled into the Rust binary), skills-npm (npm), pixi-skills (conda). None makes a harness read skills from the package location directly; all copy, symlink, or print from it.
