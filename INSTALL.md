# Installing Commonplace into a project

Commonplace can be installed into an existing project as a submodule or cloned subdirectory. This creates a two-tree layout: your content lives in `kb/` at the project root, while the framework lives in `commonplace/`. Operational artifacts (`types/`, `WRITING.md`) are copied into your `kb/` for fast access; methodology notes stay in `commonplace/` and are consulted on demand. Only promoted skills, represented as subdirectories under `commonplace/kb/instructions/`, are auto-discovered by agent runtimes. Plain instruction files remain on-demand procedures.

## 1. Add commonplace to your project

```bash
# Option A: git submodule (versioned, reproducible)
git submodule add https://github.com/anthropics/commonplace.git commonplace

# Option B: clone + gitignore (simpler)
git clone https://github.com/anthropics/commonplace.git commonplace
echo "commonplace/" >> .gitignore
```

## 2. Create the kb/ directory structure and copy operational artifacts

```bash
# Create directories
mkdir -p types kb/notes/types kb/sources/types kb/tasks/types kb/tasks/backlog kb/tasks/active kb/work

# Create the improvement log
touch kb/log.md

# Copy operational artifacts
cp commonplace/kb/instructions/WRITING.md kb/instructions/WRITING.md
cp commonplace/types/* types/
cp commonplace/kb/notes/types/* kb/notes/types/
cp commonplace/kb/sources/types/* kb/sources/types/
cp commonplace/kb/tasks/types/* kb/tasks/types/
```

## 3. Configure your agent runtime

### Claude Code: symlink skills into `.claude/skills/`

```bash
# Only promoted skills live in subdirectories; plain .md instructions are not symlinked.
mkdir -p .claude/skills
for skill in commonplace/kb/instructions/*/; do
  name=$(basename "$skill")
  ln -sfn "../../commonplace/kb/instructions/$name" ".claude/skills/$name"
done
```

### Codex: symlink skills into `.agents/skills`

```bash
# Only promoted skills live in subdirectories; plain .md instructions are not symlinked.
mkdir -p .agents/skills
for skill in commonplace/kb/instructions/*/; do
  name=$(basename "$skill")
  ln -sfn "$PWD/commonplace/kb/instructions/$name" ".agents/skills/$name"
done
```

Codex discovers promoted skills from the repository's `.agents/skills/`, but you should still add project routing in `AGENTS.md` so it knows when to read `kb/instructions/WRITING.md`, the relevant `kb/*/types/` file, when to invoke a plain instruction under `commonplace/kb/instructions/`, and when to escalate into `commonplace/kb/` for methodology.

### Optional: install Codex skills globally

If you want the same promoted skills available across projects, you can also symlink them into `$CODEX_HOME/skills` (default `~/.codex/skills`). This is optional; project-local `.agents/skills/` is enough for one repository.

```bash
CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
mkdir -p "$CODEX_HOME/skills"
for skill in commonplace/kb/instructions/*/; do
  name=$(basename "$skill")
  ln -sfn "$PWD/commonplace/kb/instructions/$name" "$CODEX_HOME/skills/$name"
done
```

## 4. Create your project's control-plane file

Copy the template and rename it for your agent runtime:

```bash
# Claude Code
cp commonplace/AGENTS.md.template CLAUDE.md

# Codex
cp commonplace/AGENTS.md.template AGENTS.md
```

The template includes routing, search patterns, escalation boundaries, and conventions — all ready to use. The one section you must fill in is **KB Goals**.

### Fill in the KB Goals section

Open the control-plane file and fill in the five subsections. The HTML comments in the template have examples — remove them when done.

**Purpose** — Name the decisions or actions the KB supports and who uses it. Start from the users, not the domain. "Supports the API team in making design decisions about the payment service" is actionable; "stores knowledge about payments" is not.

**Domain** — Draw a scope boundary specific enough that an agent can decide "does this belong?" without asking. Name adjacent domains and clarify whether they're in or out: "adjacent systems (auth, billing) are in scope only where they interact with payments."

**Include** — What types of knowledge belong: design decisions, failure analysis, integration patterns, operational procedures, etc.

**Exclude** — The most valuable section. Scope creep is the default failure mode — every piece of knowledge looks relevant in isolation. Name specific things that don't belong: "business rules live in the product wiki, not here." The Exclude list is what makes the Include list meaningful.

**Quality bar** — When is a piece of knowledge worth a note vs. a log entry vs. nothing? `WRITING.md` covers universal quality criteria (claim titles, descriptions, composability). This section adds domain-specific standards: "a design decision is worth a note when it affects more than one endpoint; single-endpoint details belong in code comments."

The Goals section is always-loaded — the agent sees it every session and uses it to decide whether knowledge belongs in this KB before deciding where it goes.

## Resulting layout

```
my-project/
  kb/                        Your content
    WRITING.md               Copied from commonplace
    log.md                   Improvement log (append-only)
    notes/
      types/                 Copied from commonplace
    sources/
    tasks/
    work/                    Workshop space — connect reports, ingest staging
  commonplace/               Framework (submodule or clone)
  .claude/skills/            Optional, Claude Code only; symlinked → commonplace/kb/instructions/
  .agents/skills/            Optional, Codex only; symlinked → commonplace/kb/instructions/
  ~/.codex/skills/           Optional, Codex global skills; symlinked → commonplace/kb/instructions/
  CLAUDE.md                  Optional, Claude Code control-plane file
  AGENTS.md                  Optional, Codex control-plane file
```

## Updating

Pull new changes (`git submodule update --remote` or `cd commonplace && git pull`), then re-copy operational artifacts. Commonplace-provided type files are replaced; any custom types you've added are left untouched.

See `kb/notes/commonplace-installation-architecture.md` for the full design rationale.
