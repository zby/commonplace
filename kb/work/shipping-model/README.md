# Workshop: Shipping Model

## Question

How should commonplace ship its content to users so that their working collections (`kb/notes/`, `kb/reference/`, `kb/instructions/`) stay theirs, while our shipped library (methodology notes, reference, instructions, skills) sits alongside as a read-only dependency?

## Why this workshop exists

Today `commonplace-init` copies our entire `kb/notes/`, `kb/reference/`, and `kb/instructions/` into the user's project at the same paths (see [`SCAFFOLD_TREES`](../../../src/commonplace/cli/init_project.py)). The user's own content and our shipped content land in the same directories, with no provenance marker and no isolation. Practical consequences:

- A user who wants to author a note in their own register has nowhere to put it that isn't already ours.
- Our 187 shipped notes become "the user's notes" by default — indistinguishable from anything they add.
- Future `commonplace-init` runs overwrite or collide with user-authored files in ambiguous ways.
- Users can accidentally edit shipped notes, breaking the ability to re-sync.

The core design move under consideration is to namespace shipped content under `kb/commonplace/` so the user gets their own empty `kb/notes/`, `kb/reference/`, `kb/instructions/` alongside a read-only `kb/commonplace/{notes,reference,instructions}/`.

This interacts with several systems and cannot be done as a one-line path change:

- Skills (`cp-skill-write`, `cp-skill-connect`, `cp-skill-validate`, etc.) currently hardcode `kb/notes/`, `kb/reference/`, `kb/instructions/` — ~85 references across 27 files.
- `COLLECTION.md` exists per-collection and sets the register. Shipped collections and user collections would each need their own.
- The commonplace repo itself authors the library — our `kb/notes/` is the source of truth. If users receive it as `kb/commonplace/notes/`, source-path and ship-path diverge, and shipped instructions embedded with source paths would break in the user's tree.

## Grounding from the conversation that triggered this

- Current scaffolding ships `kb/instructions`, `kb/notes`, `kb/reference`, `kb/reports/types`, `kb/sources/types`, and `kb/types` verbatim to identical user paths ([`SCAFFOLD_TREES` in `init_project.py:33-40`](../../../src/commonplace/cli/init_project.py)).
- Users typically do **not** need to run `cp-skill-write` / `cp-skill-revise-*` / `cp-skill-validate` on shipped content — those documents were validated and revised at ship time. But skills still need to **read** shipped content as link-target candidates and to load the register conventions in `COLLECTION.md`.
- Users will rarely want to link to our notes from their own notes — most users' KBs will be about different domains. Isolation is the dominant need, not cross-linking.
- Extensibility of types is solved by copy-paste: users who want a shipped type in their own collection copy it from `kb/commonplace/notes/types/` into their own `kb/notes/types/`. No config complexity.
- Dogfooding means **we stay in the user's working position**: we author in `kb/notes/`, just like a user does. We do not move our authoring into `kb/commonplace/`, because that is the consumer position, not the author position. Ship time translates our source paths into the shipped namespace.

## Current grounding (library)

- [kb/reference/README.md](../../reference/README.md) — current shipped-system documentation surface
- [kb/reference/adr/](../../reference/adr/) — prior architecture decisions
- [Agent-operated KB maximizes contextual competence through discoverable, composable, trusted knowledge](../../notes/an-agentic-kb-maximizes-contextual-competence-through-discoverable-composable-trusted-knowledge.md) — why the library/user boundary matters for trust
- [Distillation status determines directory placement](../../notes/distillation-status-determines-directory-placement.md) — existing theory for why structural placement carries meaning
- [A functioning KB needs a workshop layer, not just a library](../../notes/a-functioning-kb-needs-a-workshop-layer-not-just-a-library.md) — framing for why this is a workshop

## What this workshop needs to resolve

1. **Namespace layout.** Is the target `kb/commonplace/{notes,reference,instructions}/`? Or a different shape — `kb/cp/`, file-level `cp-` prefix, flat `kb/commonplace-library/`?
2. **Read-only convention.** How do we signal that shipped content is read-only? Marker file (`.commonplace`), frontmatter field, directory-level README? Does `commonplace-init` refuse to run over a modified shipped tree?
3. **Path translation at ship time.** Our source is `kb/notes/...`; users receive `kb/commonplace/notes/...`. What translates in-between?
   - Hardcoded paths in our 27 instruction files referencing `kb/notes/...`, `kb/reference/...`, `kb/instructions/...`.
   - Cross-links between shipped notes (these stay relative — within the shipped tree — so they probably survive).
   - Examples: skill SKILL.md files reference `kb/notes/COLLECTION.md`; these need to point to `kb/commonplace/notes/COLLECTION.md` after ship.
4. **Skill root resolution.** Skills that currently read `kb/notes/` need to know about both roots in a user's install: user's own `kb/notes/` (write targets, authored content) and `kb/commonplace/notes/` (read-only library). Options:
   - Hardcoded second root in each skill
   - Config file (`kb/.commonplace-roots`) naming the commonplace location
   - Environment variable resolved at skill execution
   - Always look for `kb/commonplace/` if it exists; else assume single-root
5. **COLLECTION.md duplication.** Shipped collections each have their own `COLLECTION.md` (register, title conventions, linking rules). User collections need their own too. Does `commonplace-init` scaffold a starter `COLLECTION.md` into the user's empty `kb/notes/`, or does the user author their own?
6. **The cp-skill-write question.** When a user runs `cp-skill-write` from a user's own `kb/notes/`, which `COLLECTION.md` does it read — the user's, or the shipped one? Both? How does it pick a register?
7. **Types scaffolding.** Shipped types live under `kb/commonplace/notes/types/`. User's `kb/notes/types/` starts empty. User copies types they want. Does `cp-skill-write` enumerate types from both, or only from the user's collection? (Affects whether users must copy types before using them, or can reference shipped types directly.)
8. **Source-vs-ship divergence cost.** If our repo keeps `kb/notes/` but ships as `kb/commonplace/notes/`, paths diverge. This means: (a) we cannot test shipped instructions in our own repo without a translation step, (b) documentation written in our repo can't be read verbatim as documentation in a user's install. What mitigates this? A `commonplace-ship-preview` command? Running the scaffolding on ourselves in a temporary directory?

## Locked decisions (2026-04-23)

- **Namespacing shape: Option E** — `kb/commonplace/{notes,reference,instructions,agent-memory-systems}/`. Reversed from the initial D lean after the path audit showed E has strictly lower translation cost (sibling-relative links are invariant under E). See [design-space.md §Axis 1](./design-space.md) and [path-audit-option-e.md](./path-audit-option-e.md).
- **Types placement**: shared `kb/types/` stays at top level (unwrapped). Preserves 270 B1 absolute-path pointers unchanged.
- **Collection-local types (B2)**: 28 frontmatter pointers migrate to file-relative (`./types/foo.md` or `../types/foo.md`). Type resolver extended to accept file-relative paths (~1–2h, precedent exists for `$ref`).
- **Bundle scope**: ship `notes/`, `reference/`, `instructions/`, `agent-memory-systems/` under `kb/commonplace/`, plus shared `kb/types/`. Omit `kb/sources/` (copyright + size), `kb/work/` (workshop), `kb/tasks/` content, `kb/log.md` content. Scaffold user-space dirs empty. ~440 files, ~4.5M.
- **Source-link migration**: 283 `../sources/...` links convert to external URLs (primary citation) plus optional supplementary ingest link. Derived principle worth extracting as a library note.
- **Read-only convention**: `.commonplace` marker file at `kb/commonplace/` root + `commonplace-init` drift check.
- **Skill root resolution**: presence-check on `kb/commonplace/`. If present, library root; skills read both user and library. If absent, single-root mode.
- **User COLLECTION.md scaffolding**: minimal template per collection with explicit register prompts and placeholder sections.

## Deliverables

- A recommended layout and a migration plan from current state → new state
- Updated scaffolding (`SCAFFOLD_TREES`, `DEFAULT_DIRS`) with path-rewriting where needed
- A specification for how skills resolve "library root" vs. "user root"
- Updated `COLLECTION.md` for the commonplace library collections (register unchanged, just acknowledge the new path)
- A scaffolded starter `COLLECTION.md` template for each user collection
- An ADR in `kb/reference/adr/` capturing the decision
- If the design stabilizes, one or more promoted notes: a claim about the user/library boundary, a descriptive reference on the shipped layout

## Starter artifacts

- [design-space.md](./design-space.md) — the axes: namespacing shape, read-only marker, path translation mechanism, skill root resolution
- [current-shipping.md](./current-shipping.md) — concrete inventory of what ships today (scaffold trees, promoted skills, templates, hardcoded path references)

## Open questions

- Does the `kb/commonplace/` layout extend to `kb/sources/` and `kb/reports/` as well, or are those purely user-space from day one? (We ship `kb/sources/types/` and `kb/reports/types/` but not sources/reports themselves — suggesting these are user-space by design.)
- Is there value in versioning the commonplace library in the user's tree (`kb/commonplace/` as a git submodule, or with a version tag in a metadata file)? Enables clean re-sync.
- Should the `cp-skill-*` family itself live under `kb/commonplace/instructions/` as shipped instructions, or remain promoted into `.claude/skills/` / `.agents/skills/` from wherever they live?
- Do we want to preserve the ability for a user to add a note to our shipped library (PR flow)? If yes, the user's tree needs a way to mark "this note is a candidate upstream contribution" — separate from their own KB additions.
