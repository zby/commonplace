# Installation simplification: skills-only delivery

## Problem

Current installation (INSTALL.md) requires:
1. Add commonplace as submodule/clone
2. Create kb/ structure and copy operational artifacts (types, WRITING.md)
3. Symlink skills into .claude/skills/ or .agents/skills/
4. Copy and customize a ~160-line AGENTS.md template as CLAUDE.md

Step 4 is the friction point. The AGENTS.md template carries routing logic, escalation boundaries, search patterns, conventions, and KB Goals — all always-loaded into the agent's context. Now that skills are mature, most of the routing table either already delegates to skills or could.

## Usage modes

### Mode A: Standalone KB
A new repo created just for notes. CLAUDE.md can be fully dedicated to the KB. This is how this repo works today (minus the dual framework/content identity).

### Mode B: Embedded KB in a code repo
The KB lives inside an existing code repo, used for software documentation, design decisions, etc. In this scenario:
- The user's CLAUDE.md is primarily about their code project, not the KB
- The KB should not be always-loaded — users also use the LLM for coding
- The KB needs to activate on-demand, which is exactly what skills do

This makes the always-loaded routing table actively harmful — it burns context budget and confuses the agent when the user is doing non-KB work.

### Key insight: paths already work
Skills and scripts reference `kb/notes/`, `kb/sources/`, etc. relative to the project root. When commonplace is a submodule, our methodology notes live at `commonplace/kb/notes/` — no collision with the user's `kb/notes/`. No restructuring needed. The current `kb/instructions/` dual role (framework skills + this repo's procedures) is fine because only promoted skills (subdirectories) get symlinked; plain .md instructions stay local.

## Design direction: skills as the primary delivery mechanism

People are already accustomed to installing skills. If we can make skills the **only** thing that needs installing (beyond the submodule itself), installation becomes:

1. Add commonplace as submodule/clone
2. Create kb/ directories
3. Symlink skills
4. Write KB Goals in `kb/GOALS.md`
5. Done — no CLAUDE.md changes needed

This works identically for both standalone and embedded modes.

## What currently lives in always-loaded context

Analyzing AGENTS.md.template section by section:

### 1. KB Goals (~30 lines when filled in)
**Purpose, Domain, Include/Exclude, Quality bar.**
Cross-cutting scoping. Applies to every operation. Cannot become a skill — needs to be available before any skill fires.

But: does it need to be in CLAUDE.md? Could it live in a `kb/GOALS.md` file that skills read when they need it? Skills already read WRITING.md, type templates, etc. on demand.

### 2. Routing Table (~15 lines)
Maps intent → directory + type template. Two rows already say "use skill X". The rest could be absorbed by skills:

| Row | Can become skill? | How? |
|---|---|---|
| Design note | Yes | `/write` skill — routes to kb/notes/, reads WRITING.md |
| Structured argument | Yes | `/write structured-claim` — reads the type template |
| Architecture decision | Yes | `/write adr` — routes to kb/notes/adr/ |
| Review/sweep | Yes | Promote REVIEW-SYSTEM.md to a `/review` skill |
| Fix review warnings | Yes | Promote FIX-SYSTEM.md to a `/fix` skill |
| Log entry | No skill needed | Just "append to kb/log.md" — too simple for a skill |
| Snapshot | Already a skill | `/snapshot-web` |
| Ingest | Already a skill | `/ingest` |
| Task | Maybe | `/task` skill or just directory convention |
| Procedure | No skill needed | Just "write in kb/instructions/" |
| Area index | Yes | `/write index` or part of `/write` |

### 3. Content Workflow (5 steps)
Search first → read WRITING.md → read type → write → connect.
This is orchestration. A `/write` skill could embed this entire workflow.

### 4. Escalation Boundaries (6 rules)
"When X, load Y." Each rule could live in the relevant skill's own instructions. The skill fires → it loads its own guidance → no need for always-loaded escalation rules.

### 5. Conventions (~10 lines)
Links, filenames, frontmatter format. Cross-cutting.
Could live in WRITING.md (which skills already load) or a dedicated conventions file that skills reference.

### 6. Search Patterns (~10 lines)
Agents know how to grep. Droppable.

### 7. Type Routing (~5 lines)
text vs note vs specialized. Part of the `/write` skill's logic.

## Key design question: where do KB Goals live?

Options:

**A. In CLAUDE.md (current approach)**
- Pro: Always available, agent sees it every turn
- Con: Burns context when doing non-KB work, doesn't work for embedded KBs

**B. In kb/GOALS.md, read by skills on demand**
- Pro: Zero always-loaded cost, works for embedded KBs
- Con: Skills need to read it; goals aren't available for "should I even create a note?" decisions unless a skill is already running

**C. Hybrid — one line in CLAUDE.md pointing to kb/GOALS.md**
- Pro: Minimal context cost, agent knows the KB exists
- Con: Still requires touching CLAUDE.md

Option B seems strongest. The concern about "should I even create a note?" decisions is mitigated by the user explicitly invoking a skill — if they type `/write`, they've already decided to create a note.

## New skill needed: `/write`

The biggest gap. Subsumes the routing table, content workflow, and type routing. Would need to:
1. Accept optional type argument (note, structured-claim, adr, index)
2. Read kb/GOALS.md for scoping (if it exists)
3. Route to the correct directory
4. Read the relevant type template
5. Follow the WRITING.md checklist
6. Prompt for connection after writing (or auto-invoke /connect)

### One skill or several?
One `/write` skill is simpler to install; several (`/write-note`, `/write-adr`) are easier to discover. Leaning toward one with arguments.

## Simplified installation for both modes

```bash
# 1. Add framework
git submodule add <url> commonplace

# 2. Create content directories
mkdir -p kb/notes/types kb/sources/types kb/tasks/{backlog,active} kb/work
cp commonplace/kb/instructions/WRITING.md kb/instructions/WRITING.md
cp commonplace/types/* types/
cp commonplace/kb/notes/types/* kb/notes/types/
cp commonplace/kb/sources/types/* kb/sources/types/

# 3. Symlink skills
mkdir -p .claude/skills
for skill in commonplace/kb/instructions/*/; do
  ln -sfn "../../commonplace/kb/instructions/$(basename "$skill")" ".claude/skills/$(basename "$skill")"
done

# 4. Write goals (interactive or manual)
# /kb-init could do this interactively
```

No AGENTS.md template to copy. No CLAUDE.md to edit. Works for both standalone and embedded.

## This repo: dogfooding the installed version

This repo can use the exact same skills-only approach. The notes in `kb/notes/` are our methodology content (the "user" KB for this project). The skills in `kb/instructions/` are already symlinked into `.claude/skills/`. The current AGENTS.md content that's beyond what skills provide:
- KB Goals → move to `kb/GOALS.md`
- Conventions → fold into WRITING.md
- Vocabulary → already in `kb/notes/definitions/`, referenced by WRITING.md
- Development section → stays in CLAUDE.md (it's about this repo's code, not the KB)
- Git section → stays in CLAUDE.md

So CLAUDE.md for this repo shrinks to just Development + Git conventions. Everything KB-related moves into skills and `kb/GOALS.md`.

## Open questions

- How do we handle the "log entry" case? Too simple for a skill but currently relies on routing table knowledge. Document it in WRITING.md?
- Do we need a `/kb-init` skill that creates the directory structure and goals file interactively?
- Review and Fix systems — promote to full skills, or leave as on-demand instructions?
- Should this repo's CLAUDE.md keep the Vocabulary section, or is `kb/notes/definitions/` + WRITING.md's glossing rule enough?
- How does the agent discover KB skills exist in the embedded case? Skill trigger descriptions need to be clear enough that `/write` shows up when the user asks "how do I add a design note?"

## Next steps

1. Prototype `/write` skill
2. Move conventions into WRITING.md
3. Design kb/GOALS.md format
4. Test: can a brand-new KB work with ONLY skills and no CLAUDE.md KB content?
5. Dogfood: strip this repo's CLAUDE.md to Development + Git, move KB content to skills
6. Update INSTALL.md for the simplified flow
