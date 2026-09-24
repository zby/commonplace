# GBrain delivery methods

Code study of `related-systems/gbrain` at v0.54.1.0 (commit 6040075c6, 2026-09-23). Paths are relative to that clone. **Verified** means read in code or manifests; **inferred** means reasoned from code without running it.

## Summary

GBrain keeps one canonical `skills/` tree in its repository: skill directories plus shared docs (`skills/conventions/`, `skills/_*.md`, `_brain-filing-rules.json`). The CLI is installed from the repository source, so the installed CLI carries that tree. Every delivery channel is a projection of it:

- **Harness plugins (primary).** A generated, committed, version-stamped `plugin/skills/` tree serves as the skills root of both the Claude Code and Codex plugins. The plugin also declares an MCP server started through a shell launcher that runs the separately installed `gbrain` binary.
- **Copies into harness skill directories.** `skillpack scaffold --harness` writes full copies or stubs and records a per-file sha256 ledger for three-way drift checks.
- **Workspace scaffold (OpenClaw).** One-time additive copies into an agent repository, with a two-way update lens.
- **MCP `list_skills`/`get_skill`** (CLI `gbrain skills`/`gbrain skill`), which serve skill bodies at use time.
- **Shared-brain native router (v0.53).** Canonical skills live in the brain's content source, with a single router skill installed per harness. This channel depends on the database.
- Not studied further: the OpenClaw bundle (`openclaw.plugin.json` `skills` and `shared_deps`) and `gbrain bootstrap` hooks and managed blocks (`docs/guides/bootstrap.md:29-36`).

Plugins and the CLI are released in lockstep at build time, but they update through separate channels. I found no runtime check of skew between plugin and CLI.

## 1. Plugins and the generated tree

**Manifests (verified).** `.claude-plugin/plugin.json:21-33` sets `"skills": "./plugin/skills/"` and an MCP server `${CLAUDE_PLUGIN_ROOT}/.agents/gbrain-launcher serve --surface starter --source-guard`. `.claude-plugin/marketplace.json:5-23` lists the full plugin with `source: "./"` (the repository root) and two persona variants under `plugin-variants/`. `.codex-plugin/plugin.json:21-22` names the same skills root and points to `.codex-plugin/mcp.json:4-11`, which uses the same launcher with `cwd: "."` and an allowlist of environment variables. `.agents/plugins/marketplace.json:7` declares a local source `./`.

**Generation (verified).** `scripts/generate-plugin-tree.ts` is a repository-only build script:

- The lane set is the OpenClaw skill list, minus the recorded exclusions, plus the recorded additions (`:17-20`, `:117-120`). Each decision carries a reason in `skills/plugin-lanes.json`.
- Skill directories are copied, then the shared docs are copied beside them (`:190-202`).
- `plugin/README.md` receives `<!-- gbrain-plugin-tree-stamp: <VERSION> -->` (`:204-208`).
- Each persona variant is a self-contained plugin root with its own skills, shared docs, a byte copy of the launcher, and generated manifests at `VERSION` (`:242-297`).

`scripts/check-plugin-tree.sh:36-47` regenerates the tree into a temporary directory and fails CI on any byte difference. `test/codex-plugin-manifest.test.ts:35-41` fails when a manifest version differs from `package.json`. `CLAUDE.md:290` calls the result a "FIVE-file lockstep".

**Publication (verified).** Claude Code users run `/plugin marketplace add garrytan/gbrain`, which reads the default branch (`docs/mcp/CLAUDE_CODE.md:20-24`). For Codex, the release job force-pushes a history-less `codex-plugin` branch containing only `.agents .codex-plugin .claude-plugin plugin plugin-variants LICENSE` (`.github/workflows/release.yml:285-353`). Users add it with `codex plugin marketplace add garrytan/gbrain@codex-plugin` (`docs/mcp/CODEX.md:18-28`).

**Shared docs (verified).** Skills link to shared docs by paths relative to their own location, `../conventions/<x>.md` (34 files). The plugin tree preserves those links because conventions sit beside the skill directories. 37 files also cite repository-rooted paths such as `skills/conventions/quality.md`, which do not resolve inside a plugin (inferred). `scripts/check-skill-refs.mjs:4-10` fails on dangling relative links.

## 2. Harness copies (`skillpack scaffold --harness`)

**What it writes (verified).** `src/core/skillpack/harness-bridge.ts` installs a persona-curated set into a harness skill directory:

- Harnesses: `claude-code`, `codex`, `opencode`, `openclaw` (`:69`). Claude Code defaults to user or project `.claude/skills`; Codex and opencode require `--dest`, because GBrain has not verified their default directories (`src/commands/skillpack/harness.ts:184-202`).
- Shared docs travel with the skills. Existing files are never overwritten.
- Before any write, it refuses a SKILL.md without frontmatter, which breaks Codex (`:215-241`), and refuses symlinks or targets outside the destination (`:329-377`).
- Only files the command created are recorded as owned (`:410-455`).

**Superseded path (verified).** Since v0.53, `harness.ts:365-375` first tries `installSharedBrainBridge`. When a shared brain is active, the legacy full and stub copies are refused and a migration plan is returned (`docs/guides/shared-brain-skills.md:248-255`).

## 3. Stub mode

**Stub content (verified).** `renderSkillStub` (`harness-bridge.ts:291-313`) keeps the source frontmatter verbatim, so harness discovery still sees the name, description, and triggers. It replaces the body with about ten lines:

- the marker `<!-- gbrain-skill-stub v1 -->` (`:78`);
- "the full skill body is served by your gbrain brain, so it is always current";
- an instruction to call MCP `get_skill {"name": slug}`;
- if that tool is absent, advice that the MCP surface is too narrow, plus the fallback "Local CLI fallback that always works: `gbrain skill <slug>`".

The file marker, not the ledger, decides whether an installed file is a stub. An install never half-converts a skill between modes (`:225-231`, `:243-248`).

**Stub mode still copies files (verified).** Stub installs still copy shared docs and auxiliary files, because `get_skill` serves only the SKILL.md body (`:200-203`). The response is capped at 256 KiB (`src/core/skill-catalog.ts:65-72`). It carries the body, a subset of frontmatter fields, the skill's usable and unavailable tools, and `client_guidance` (`:506-553`). So stubs keep skill bodies current, but shared docs remain copies that can drift.

**Preflight (verified).** `harness.ts:279-330` refuses stub mode unless `mcp.publish_skills` is on and every slug is servable from the skills directory the server resolves. It warns if the surface is `verbs`, which lacks `get_skill` (`src/mcp/surface.ts:100,123`).

**When the CLI or server is missing.** Verified: the launcher exits 127 and prints the install command (`.agents/gbrain-launcher:45-50`). Inferred: without the server and the binary, the agent has only a pointer and no instructions. `gbrain skill` is an ordinary operation, not a CLI-only command (`src/core/ops/skills-catalog.ts:94`; `src/cli.ts:637-660`), so it goes through engine or remote routing and appears to need a configured brain.

**Cost (inferred, not measured).** A stub costs about 150 tokens resident instead of the full body. Each use adds one tool round-trip. The CLI fallback also pays Bun startup and an engine connection.

## 4. Drift and upgrade

**Ledger format (verified).** `~/.gbrain/skillpack-bridge-state.json`, schema `gbrain-skillpack-bridge-v1` (`bridge-state.ts:29-80`), holds one entry per (harness, dest):

- `scope`, `last_persona`, `last_mode`, `gbrain_version`, `installed_at`, `updated_at`;
- `written: {slug: {mode, files: {relpath: sha256}}}`, where shared docs sit under the reserved key `_shared`.

Loading fails open: a corrupt file loads as empty (`:82-94`).

**Three-way comparison (verified).** `runHarnessReference` (`harness-bridge.ts:604-681`) compares each installed file with the expected content: current source bytes, or the freshly rendered stub for stub files. When they differ, it uses the install-time hash:

- the file equals its install-time hash → `upstream_drift`;
- it has a hash but no longer matches → `local_edit`;
- no hash → `unknown`.

**`--apply-clean-hunks` (verified).** In harness mode (`:711-884`), the command refuses stubs, local edits, and files of unknown provenance. It applies hunks only to files with proven upstream drift, then refreshes the ledger hash. Inferred: a file with proven drift is byte-identical to what GBrain wrote, so applying every hunk equals replacing the file. The hunk machinery changes the outcome only in workspace mode. There, `reference.ts:170-189` states that the comparison is two-way and that applied hunks overwrite the user's intentional edits.

**Removal (verified).** `remove` deletes only files in the ledger whose hash is unchanged and keeps edited files (`:897-1014`).

**How upgrades reach copies (verified).** They do not reach them automatically.

- `gbrain upgrade` runs an advisory sweep over the workspace scaffold only. It prints drifted and new skills and writes nothing (`src/commands/upgrade.ts:800-910`).
- Harness copies appear under `skillpack status` (`harness.ts:703-745`).
- Plugins need `codex plugin marketplace upgrade` or a Claude plugin update. `docs/mcp/CODEX.md:83-86` calls upgrading a process with "two halves": the plugin and the binary.

**Skew detection (verified absent).** No code in `src/` reads the plugin-tree stamp or a plugin cache. The launcher runs whichever `gbrain` it finds. The only stamp check covers the bootstrap runbook (`src/commands/doctor/bootstrap-checks.ts:469-480`). Claude plugin users track the default branch, while CLI users track the `latest-stable` tag, so the two can diverge (inferred).

## 5. Runtime installation

**Install (verified).** `bun install -g github:garrytan/gbrain#latest-stable`: Bun runs the TypeScript source directly (`package.json` bin `src/cli.ts`, engines `bun >=1.3.11`). Release CI force-moves the `latest-stable` tag only after the release publishes (`release.yml:175-191`). Other install methods are compiled binaries (darwin-arm64 and linux-x64 only, with self-update checked against build provenance, `upgrade.ts:80-84`), `bun link`, and ClawHub (`upgrade.ts:932-960`).

**Locating skills (verified).** `findGbrainRoot` walks up from the module's path to find `openclaw.plugin.json` and `src/cli.ts` (`src/core/skillpack/bundle.ts:50-82`). The installed source tree is therefore the skills source. Inferred: compiled binaries cannot scaffold, because I found no embedded copy of the skills tree.

**Windows (verified).** The launcher is `/bin/sh` and Unix-only (`.agents/gbrain-launcher:1-4`), the plugin description says "Unix (macOS/Linux) only", and no Windows binary is published. Only the postinstall script handles Windows paths (`scripts/postinstall.ts:10-19`). The plugin lane does not work on Windows.

## Carry-over table

| Method | Carries over to Commonplace as | Needs | Blocker / GBrain-specific dependency |
|---|---|---|---|
| Generated, committed plugin tree + byte-diff CI gate + version stamp | A Python generator that emits one plugin tree (skills plus library) from `kb/`, with a pytest that regenerates and diffs it and a stamp at the package version | Decide whether the committed tree lives in the main repo (Claude, default branch) or a release branch (Codex slim dist) | None. Pure file generation |
| Marketplace manifests (Claude `source: "./"`, Codex orphan branch) | The same two manifests; the release workflow force-pushes a dist branch | GitHub release CI; a tag playing the role of `latest-stable` | None. GBrain's MCP entry is optional; drop it |
| MCP launcher inside the plugin | Not needed: Commonplace has no MCP server. The resolution order (environment override → sanctioned install directory → PATH → fail with install hint) is reusable for any plugin hook that calls `commonplace-*` | uv's bin directory as the sanctioned location | `/bin/sh` launcher is Unix-only. Commonplace requires Windows, so hooks must avoid sh |
| Harness copies + sha256 ledger + three-way lens | A user-level ledger (JSON) keyed by (harness, dest) with install-time hashes; `local_edit` / `upstream_drift` / `unknown` classification | A ledger location per OS user, matching ADR 064 | None. Pure file operations |
| `--apply-clean-hunks` | Replace a file whose hash shows it unedited; report edited files. The hunk applier can be dropped (see §4) | — | None |
| Stub mode | Stub SKILL.md whose body says to run `commonplace-skill <name>` (prints current text from package data) | A skill-printing command; Bash permission for it | GBrain's primary path needs MCP `get_skill` + publish gate + DB config. CLI-only stubs avoid that. Stubs still leave shared docs as copies |
| MCP `list_skills`/`get_skill` | No direct equivalent | An MCP server | Requires GBrain's server, surface, and publish gate; the survey records poor adherence and schema cost for MCP instructions |
| Shared-brain native router | No equivalent | — | Database-bound: brain identity, source policy, and membership |
| Upgrade reach | `commonplace-*` upgrade advisory: after `uv tool upgrade`, report drifted copies; `status` lists harness copies | Hook or command that runs the lens | GBrain itself does not auto-refresh; copying it gives advisory drift only |
| Plugin/CLI skew | GBrain has none. Commonplace can add a check that compares the plugin tree stamp with `commonplace` version from a SessionStart hook or skill preamble | Stamp file readable from the plugin root | Departure from GBrain (improvement), justified by the proposal's divergence requirement |
