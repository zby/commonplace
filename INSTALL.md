# Installing Commonplace into a project

Two installs, by what you want from it:

- **Reader install** — vendor the Commonplace knowledge base inside an existing project as a read-only reference: your agents consult the research when they face context, memory, or learning design decisions. A vendored copy (submodule, clone, or plain download) and one routing paragraph; no Python — the KB is plain markdown, so it works in a project written in any language. See [Reader install](#reader-install-the-kb-as-a-vendored-reference).
- **Full install** — run your own knowledge base with the Commonplace type system, skills, and commands. The package carries the Commonplace library — notes, reference docs, instructions, global types, review gates, and skills — but not this repo's external-system reviews (`kb/agent-memory-systems/`, `kb/agentic-systems/`) or source corpus. Projects read the library in place from the installed package; it is not copied into them. The numbered steps below: check prerequisites, install the package so `commonplace-*` commands run, set up the project with `commonplace-init`, set up the control-plane files, check the skills for every agent that will work on the project, and start the runtime. Most steps end with a check you can run before moving on.

## Reader install: the KB as a vendored reference

Vendor this repository **inside** your project root — placement is load-bearing, not cosmetic: agent harnesses scope file access to the project root, so a sibling directory costs a permission prompt in every session, while a subdirectory is readable with none.

As a submodule (pins a commit; every teammate and CI gets the same version, and updates are deliberate, reviewable bumps):

```bash
git submodule add https://github.com/zby/commonplace commonplace
```

Or as a gitignored clone (zero ceremony; each machine clones its own):

```bash
git clone https://github.com/zby/commonplace
echo '/commonplace/' >> .gitignore
```

Git itself is optional — the KB is plain files, so [downloading the repo as an archive](https://github.com/zby/commonplace/archive/refs/heads/main.zip) and extracting it into `commonplace/` works too; you just update by re-downloading.

Then add a routing block to your project's `CLAUDE.md` or `AGENTS.md`. The vendored repo ships it as `AGENTS.md.reader-fragment`, so appending is one command (creates the file if the project has none):

```bash
cat commonplace/AGENTS.md.reader-fragment >> CLAUDE.md    # or >> AGENTS.md
```

Or paste it directly:

```markdown
## Knowledge base (vendored, read-only)

`commonplace/kb/` is a vendored knowledge base on agent context engineering,
memory, and deploy-time learning. For design decisions in those areas, consult
it before deciding: start at `commonplace/kb/tags/README.md`. Paths named
inside it are relative to `commonplace/`. It is read-only in this project — to
contest a claim, open an issue at https://github.com/zby/commonplace/issues.
```

Either way, if you vendored under a directory name other than `commonplace/`, adjust the paths in the block to match.

That's the whole install. Reading needs no Python, no venv, and no skills — the `commonplace-*` commands and `cp-skill-*` skills exist to maintain a KB, not to consume one. The one tool the KB's navigation leans on is ripgrep (`rg`), which most agent runtimes bundle. The vendored repo's own `AGENTS.md` tells agents that wander into it to treat it as read-only.

### Check the reader install

```bash
rg "^description:" commonplace/kb/notes/ --glob "*.md" | head
```

Then ask your agent a design question in the KB's domain — "should our agent memory get vector retrieval, or navigation structure first?" — and check the answer cites notes from `commonplace/kb/`.

### Updating the vendored KB

```bash
git -C commonplace pull                        # gitignored clone
git submodule update --remote commonplace      # submodule
```

### Keeping it small (optional)

If repository weight matters, a blobless, kb-only checkout works — root files such as `AGENTS.md` remain present:

```bash
git clone --filter=blob:none --sparse https://github.com/zby/commonplace
git -C commonplace sparse-checkout set kb
```

## 1. Prerequisites

### Required

- **uv** — installs Commonplace and selects or provisions a compatible Python 3.11+ interpreter
- **git**
- **ripgrep** (`rg`) — agent runtimes use it for fast KB search
- **curl** — downloads PDFs for `cp-skill-snapshot-web`
- **Trafilatura 2.2+** — extracts ordinary web pages as clean Markdown; install
  its CLI with `uv tool install "trafilatura>=2.2"`
- **Poppler** — supplies `pdfinfo` and `pdftotext` for PDF snapshots (the
  package is commonly named `poppler-utils` on Debian/Ubuntu and `poppler` on
  Homebrew; WinGet identifies it as `oschwartz10612.Poppler`)
- **An agent runtime** — Codex, Claude Code, or another LLM/IDE that can load a project control-plane file (`AGENTS.md`/`CLAUDE.md`) and read files outside the project, where the installed library lives. A runtime that discovers skills in a project directory gets the `cp-skill-*` skills natively; any other runtime uses the skill index that `commonplace-init` writes.

Normal KB maintenance is expected to happen under version control. The shipped procedures and examples use Git, so it is included in the out-of-the-box prerequisites above. A project may substitute another VCS if it adapts Git-specific procedures; the `commonplace-*` commands do not use Git history as correctness state.

### Check prerequisites

If any required tool is missing, install it before continuing.

Linux/macOS:

```bash
uv --version
git --version
rg --version
curl --version
trafilatura --version
pdfinfo -v
pdftotext -v
```

Windows PowerShell:

```powershell
uv --version
git --version
rg --version
curl --version
trafilatura --version
pdfinfo -v
pdftotext -v
```

## 2. Install Commonplace as a user-level tool

Install Commonplace as a user-level uv tool. uv creates an isolated environment for the package and places every declared `commonplace-*` executable in its tool executable directory:

```text
uv tool install --python ">=3.11" llm-commonplace
uv tool update-shell
```

The second command durably adds uv's tool executable directory to the user environment; it is not reissued on every shell restart. Close the installer shell and fully restart every shell, IDE, desktop agent, or service process that must use the commands. A process that was already running keeps its old environment.

This establishes one active Commonplace command version per OS user. All projects for that user resolve the same tool. Project dependencies remain independent and do not share Commonplace's isolated tool environment.

For Commonplace development, install an editable checkout instead, from that checkout's root:

```text
uv tool install --python ">=3.11" --editable .
uv tool update-shell
```

An editable install reads the library from the checkout's `kb/`, so ordinary Python, scaffold-source, and library edits are visible without reinstalling. After changing dependencies, entry points, build metadata, or which files the package includes, force a metadata refresh without changing command ownership:

```text
uv tool install --reinstall --python ">=3.11" --editable .
```

Switching the user-level tool to an editable checkout changes the commands, and the library, seen by every project for that user. It also moves the library root, so rerun `commonplace-init` in each project right after the switch (see [Updating](#updating)).

The base tool installation includes the dependencies used by X/Twitter
snapshotting; no installation extra is required.

### Check the commands run

Run these checks in a newly started process, not the installer process:

```bash
uv tool dir --bin
command -v commonplace-validate
commonplace-init --help
```

```powershell
uv tool dir --bin
(Get-Command commonplace-validate).Source
commonplace-init --help
```

The resolved command should be inside the directory printed by `uv tool dir --bin`. Repeat the check inside each IDE or agent runtime you intend to support; an integrated terminal result does not prove that a separately launched desktop agent inherited the same environment.

## 3. Set up the project with commonplace-init

Run `commonplace-init` from the project root by bare name:

```bash
commonplace-init --name my-project
```

```powershell
commonplace-init --name my-project
```

The `--name` flag sets the project name used in templates; if omitted it defaults to the directory name.

The Commonplace library — framework notes, reference, instructions, review gates, global types, and skills — stays in the installed package. `commonplace-init` does not copy it into the project. It writes the project's own KB and a few machine-specific files that point into the library.

On a new project it creates the project's own files once:

- **User KB directories and collection heads** — `kb/notes/`, `kb/reference/`, `kb/instructions/`, `kb/tags/`, `kb/sources/`, `kb/tasks/`, `kb/work/`, `kb/reports/`, `kb/log.md`; notes, reference, instructions, tags, sources, work, and reports each receive a starter `COLLECTION.md` contract and `README.md` landing. Source snapshots are ignored locally; reports also receive `cache/`, `state/`, and `retained/` policy areas with their own ignore and validation boundaries.
- **`AGENTS.md.template` and `CLAUDE.md.template`** — control-plane templates with the project name filled in (step 4).

On every run it also writes its pointers into the library for this machine:

- **Skill stubs** — a stub `SKILL.md` for each `cp-skill-*` skill, and for the router skill `cp-skill-library`, in `.claude/skills/` (Claude Code) and `.agents/skills/` (Codex and others). A stub carries the real skill's name and description and tells the agent to read the real `SKILL.md` in the installed library and follow it. The `cp-skill-` prefix avoids collisions with your project's own skills and with the `commonplace-*` CLI commands.
- **`.commonplace/library.md`** — the library root on this machine, the library's entry points, and an index of its skills with each `SKILL.md` path. Agents in a runtime without a skills mechanism use this index in place of the stubs.
- **A read rule for Claude Code** — a `Read(//<library root>/**)` allow rule in `.claude/settings.local.json`, so Claude Code reads the library without permission prompts. Codex needs no rule.
- **`.gitignore` entries** — for the stubs, `.commonplace/`, and `.claude/settings.local.json`. These outputs name paths on this machine, so they are never committed.

Rerunning `commonplace-init` is safe. It never overwrites the project's own files: it reports which of them already match the current scaffold and which were left untouched because they differ. It rewrites only its own outputs — the stubs, `.commonplace/library.md`, and the read rule — and removes stubs for skills the package no longer has. It leaves alone any skill directory it did not write, and reports it. It does not create or inspect `.envrc`.

If the project holds a copy of the library from an older release, init migrates it; see [Migrating from a copied library](#migrating-from-a-copied-library).

### Check the setup, validation, and search

Commonplace works with curated indexes and `rg`; no semantic-search daemon is required.

```bash
commonplace-init --check
commonplace-validate landings
rg "your search terms" kb/ --glob "*.md"
```

`commonplace-init --check` writes nothing. It reports each stub, `.commonplace/library.md`, and the read rule as `ok`, `missing`, `stale`, `extra` (a stub for a skill the package no longer has), or `foreign` (a skill directory with a `cp-skill-*` name that init did not write), and exits non-zero if any entry is not `ok`. A fresh scaffold should pass `commonplace-validate landings`: every collection directly under `kb/` has a `README.md`, with no sibling `index.md` collision. A fresh project has no user notes yet, so `commonplace-validate kb/notes` may report that no notes matched — run it after the first user note exists.

To search the library as well as the project, add the library root that `.commonplace/library.md` names to the `rg` paths.

## 4. Set up the control-plane files

The control-plane file tells the agent what the KB is for, where to find things, and which skills are available. Codex- and Claude-style runtimes load it automatically from the project root; internal runtimes may need an explicit project-instructions setting, plugin config, or prompt import.

**New project** — rename both templates:

```bash
mv AGENTS.md.template AGENTS.md
mv CLAUDE.md.template CLAUDE.md
```

`AGENTS.md` carries the project's instructions and tells agents to read `.commonplace/library.md` for the Commonplace library. `CLAUDE.md` imports `AGENTS.md` and `.commonplace/library.md`, so Claude Code has the library paths in context from the start of a session. Neither file names a path on this machine, so both are committed.

**Existing project that already has an `AGENTS.md` or `CLAUDE.md`** — append the template to the file that holds the project's instructions:

```bash
cat AGENTS.md.template >> AGENTS.md
```

Then make sure `CLAUDE.md`, if Claude Code will work on the project, imports both files. It needs these two lines; drop `@AGENTS.md` if the template went into `CLAUDE.md` itself:

```text
@AGENTS.md
@.commonplace/library.md
```

Then review the merged file and fill in the per-project parts. The template's HTML comments mark every spot; the load-bearing ones are:

- **`KB Goals and Scope`** — Purpose, Scope (the out-of-scope list is what prevents scope creep), and Quality bar. Without these the agent has no basis for inclusion decisions.
- **`The Commonplace library`** — keep it as shipped. It tells agents to read `.commonplace/library.md`, and to stop and ask for `commonplace-init` when that file is missing instead of looking for the library elsewhere.
- **Command invocation (in `### Commands`)** — keep the unconditional bare-name rule. Commonplace commands come from the user-level uv tool, not the project's dependency environment.
- **Navigation entry points** — add tag heads (`kb/tags/<tag>-README.md`) to the list as they emerge; the template comment explains when a tag needs one.
- **Version-control conventions** — keep the framework expectation that the KB is versioned, and add any project-specific commit, branch, or review rules. The template deliberately assigns no portable Commonplace semantics to those objects.

A runtime that loads neither `AGENTS.md` nor `CLAUDE.md` needs the same pointer in whatever it does load: "read `.commonplace/library.md` in the current project; if it is missing, stop and ask for `commonplace-init`". The pointer names no machine path and no particular project, so it can be set once per user.

## 5. Check the skills for every agent that will work on the project

**For most agent setups, nothing needs to be installed here.** `commonplace-init` already wrote the skill stubs into `.claude/skills/` (Claude Code) and `.agents/skills/` (Codex and others). Confirm they are current:

```bash
commonplace-init --check
```

A stub is a small `SKILL.md`, the same on every platform; no link support is needed. When the agent invokes a skill, the stub sends it to the real `SKILL.md` in the installed library, and the agent follows that file in place, resolving its relative links from the real location. Each skill use therefore costs one extra read.

An agent whose runtime reads neither of those two skill directories, or has no skills mechanism at all, uses the skill index in `.commonplace/library.md`: when a task matches a skill's description there, the agent reads that `SKILL.md` and follows it. It loses what only a native skill gets from the harness — a forked context, model choice, tool limits, and invocation by name.

The Commonplace source checkout does not run `commonplace-init`. It is where the library is authored, and its committed `.claude/skills/` and `.agents/skills/` symlinks cover all its skills.

## 6. Start the runtime

Fully restart the agent runtime after `uv tool update-shell`, then confirm inside the agent that `commonplace-validate --help` resolves. Shell activation is not part of the contract. If the command works in a new terminal but not in the agent, diagnose how that runtime receives the user environment rather than reinstalling the package repeatedly.

From inside the running runtime, confirm the skills resolve by their `cp-skill-*` names:

```text
cp-skill-write
cp-skill-validate
cp-skill-connect
cp-skill-health-check
cp-skill-library
```

If they don't, run `commonplace-init --check`, and `cp-skill-health-check` once it is visible.

## Pre-approve Commonplace commands in Claude Code (optional)

Reading the library needs only the read rule, which `commonplace-init` writes. Agents also run `commonplace-*` commands in ordinary work. If you use Claude Code, skip the per-command permission prompt by adding prefix-wildcard allow rules to `.claude/settings.local.json` (user-local, gitignored). Add one `Bash(<name>:*)` entry per `[project.scripts]` entry in `pyproject.toml`:

```json
{
  "permissions": {
    "allow": [
      "Bash(commonplace-validate:*)",
      "Bash(commonplace-relocate-note:*)"
    ]
  }
}
```

Init keeps your entries when it updates its read rule in the same file. Prefer `.claude/settings.local.json` over `.claude/settings.json` so the approvals stay local and aren't committed for other contributors.

## Troubleshooting command discovery

Use `uv tool list` to confirm installation and `uv tool dir --bin` to identify the expected executable directory. On Linux/macOS, `command -v` or `which -a` shows what wins on `PATH`; on PowerShell use `Get-Command -All`.

- **Tool missing:** install it with the step 2 command.
- **Executable exists in uv's tool directory but bare name is missing:** run `uv tool update-shell`, then fully restart the consuming process. In CI, append the configured tool bin directory to `$GITHUB_PATH` instead of editing a profile.
- **Bare name resolves elsewhere:** an older project venv or another install is shadowing the uv tool. Remove or reorder that `PATH` entry. Do not make `uv tool install --force` the default repair; uv's conflict is evidence that command ownership needs to be resolved.
- **Only one IDE or agent fails:** that launch class did not inherit the updated user environment. Fix its supported environment configuration or exclude it from the support claim.
- **Import fails after an editable metadata change:** rerun the editable install with `--reinstall` so uv refreshes the existing tool environment.
- **A command warns that the project's Commonplace files are out of date:** a stub, `.commonplace/library.md`, or the read rule no longer matches the installed library. Rerun `commonplace-init` in the project.
- **A command reports that the Commonplace library is not available:** the installation has no library under its shared data. Reinstall the tool with the step 2 command.

`cp-skill-health-check` performs the same classification, runs `commonplace-init --check`, and flags a library copy left by an older release.

### Migrating an older project-local installation

Install and verify the user-level tool first. Then inspect any project `.envrc` that adds `.venv/bin` or `.venv\Scripts` to `PATH`. The exact two-line `.envrc` generated by older Commonplace releases can be removed after the fresh-process checks pass. An edited `.envrc` must be reviewed manually. Remove a project `.venv` only if you have confirmed it was used solely for Commonplace; it may still own the project's unrelated dependencies.

### Migrating from a copied library

Earlier Commonplace releases copied the library into the project: the collections under `kb/commonplace/`, the global types under `kb/types/`, the source and report types under `kb/sources/types/` and `kb/reports/types/`, and the skills as full directories under `.claude/skills/` and `.agents/skills/`. To migrate, install the new tool and rerun `commonplace-init` in the project.

Init compares every file of those old copies with the installed library's version:

- A file that matches is removed. A skill directory emptied this way receives a stub.
- A file that differs is left in place and listed under "Kept library copies that differ from the installed library". It may carry a local change. The old copies record no version, so it may also be an unmodified file from an older release. Decide which, then delete it or move the change into the project's own collections. A skill directory that still holds such a file is not replaced by a stub until you remove it; init lists it as skipped.
- A file under `kb/types/`, `kb/sources/types/`, or `kb/reports/types/` that has no counterpart in the library is treated as the project's own and left alone. A type spec left under `kb/types/` is no longer eligible in any collection; move it into the `types/` directory of the collection that uses it.

Init also retires, once, the review baselines whose criteria were files in the old copy, because those criteria now have library identities (`commonplace:instructions/review-gates/...`, `commonplace:types/...`). Review history is kept; the affected pairs are reviewed again as missing baselines.

If the project committed its old skill copies, version control keeps tracking those directories after init turns them into stubs, and the stubs hold paths specific to one machine. Init lists every skill directory it converted this way with the command to untrack it (`git rm -r --cached <paths>`); run it and commit. Init does not run git itself. A skill directory that is a symlink is never migrated, overwritten, or deleted; init lists it as skipped.

Init also rewrites the project's type values in the form this release uses, and lists every file it changed:

- **Type values.** Every type value is the type spec's path under a KB root, with `.md`: `types/<name>.md` for a global type, found under the library root, and `<collection>/types/<name>.md` for a collection-local type, found under the project's `kb/`. A frontmatter `type:` or `requires_type:` value in an older form becomes the new one: a bare global name such as `note`, or a pointer at an old copy of a global type as `kb/types/<name>.md`, `kb/sources/types/<name>.md`, `kb/reports/types/<name>.md`, or a relative path to the same file, becomes `types/<name>.md`; a file-relative or `kb/`-prefixed local value becomes `<collection>/types/<name>.md`. Frozen evidence copies under `kb/reports/state/` keep their recorded pointers to `kb/types/`; live reports there are rewritten. Replaceable output under `kb/reports/cache/` is not rewritten. JSON-style frontmatter is handled the same way. Project-shared types are no longer supported: a differing copy of a library type that init kept under `kb/types/` collides with the library file of the same path, and validation names both files. Delete the copy, or move its change into a type in one of the project's own collections.
- **Schema references.** A schema under the project's `kb/` that refers to a global schema by relative path, as the older report and source types do, now refers to it as `commonplace:types/<name>.schema.yaml`, resolved in the installed library.

- **Snapshots.** A local capture under `.snapshots/` whose frontmatter still names the old snapshot type path is rewritten to `type: types/snapshot.md`; nothing else in it changes. An ingest that pinned the capture's old bytes in `snapshot_sha256` or `original_snapshot_sha256` gets the new checksum; commit those ingests. The rewrite is the same on every machine, so another clone reaches the same bytes when it reruns init after pulling the re-pinned ingests.

Relative links from project notes into `kb/commonplace/` stop resolving. Point them at the published Commonplace documentation or remove them. When the migration is done, `commonplace-init --check` reports every entry `ok` and `commonplace-validate` passes on the project's collections.

## Resulting layout

```text
my-project/
  .agents/
    skills/
      cp-skill-write/SKILL.md          stub, uncommitted
      cp-skill-validate/SKILL.md
      ...
      cp-skill-library/SKILL.md
  .claude/
    settings.local.json                read rule for the library, uncommitted
    skills/
      cp-skill-write/SKILL.md          stub, uncommitted
      ...
  .commonplace/
    library.md                         library root, entry points, skill index; uncommitted
  kb/
    notes/
    reference/
    instructions/
    sources/
    tasks/
    work/
    reports/
    log.md
  AGENTS.md
  CLAUDE.md
```

The project contains its own collections and their collection-local types, the two control-plane files, and init's uncommitted outputs. It contains no library files, no global types, and no skill bodies. Each person who clones the project runs `commonplace-init` once in their clone, because the uncommitted outputs name paths on their machine.

## Updating

Upgrade the published user-level tool:

```bash
uv tool upgrade llm-commonplace
```

The library changes in place: the next agent read and the next command use the new skills, instructions, gates, and types. Nothing needs to be copied. If the upgrade added, removed, or renamed a skill or changed a skill's description, `commonplace-*` commands warn in each project until you rerun init there:

```bash
commonplace-init
```

For an editable source install, pull the checkout. Ordinary code and library changes are immediately visible; rerun `uv tool install --reinstall --python ">=3.11" --editable .` when installation metadata or dependencies changed.

To switch between an editable checkout and the published package, make the ownership change explicit:

```bash
uv tool uninstall llm-commonplace
uv tool install --python ">=3.11" llm-commonplace       # published
# or, from the checkout:
uv tool install --python ">=3.11" --editable .          # editable
```

The switch moves the library root, so rerun `commonplace-init` in every project immediately afterwards. Until then the stubs and `.commonplace/library.md` may still point at the old root, and an agent can read the old library without any warning; the warning appears only when a `commonplace-*` command or `commonplace-init --check` runs.
