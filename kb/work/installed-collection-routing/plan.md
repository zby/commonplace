# Plan: Use Top-Level Collection Convention for Installed Commonplace

## Problem

Installed Commonplace projects currently put shipped library content under `kb/commonplace/`, with collection-shaped children such as `kb/commonplace/notes/` and `kb/commonplace/reference/`. That shape is awkward for agents because it requires them to know that the parent is not a collection while the grandchildren are.

Parsing a registry from `AGENTS.md` would solve this for one harness shape, but agent startup files vary: Claude has `CLAUDE.md`, other agents use `AGENTS.md`, and some use other startup surfaces. Making a startup file the structural source of truth would create synchronization and portability problems.

## Fundamental Requirements

- Agents must reliably find relevant KB material with minimal reasoning.
- Python tooling and agents must agree on what a collection is.
- The installed KB must be understandable by inspection, without hidden installer history.
- User-authored content and shipped Commonplace content must not be confused.
- Users should not be encouraged to edit shipped Commonplace library content.
- Shipped Commonplace content should remain useful as examples and reference material.
- Installed reference docs must be good documentation of Commonplace itself.
- Installed skills/instructions must be operational from the installed project.
- Collection contracts should stay close to the artifacts they govern.
- Cross-links inside shipped content should keep working after installation.
- The system should avoid duplicate sources of truth.
- The design should work across LLM harnesses with different startup-file conventions.
- The installer may perform deterministic mechanical transformations.
- The ongoing operating model should be simpler than the install process.

## Derived Core Requirements

- Collection discovery should use a filesystem convention, not a harness-specific startup config.
- A collection root is a direct child of `kb/` containing `COLLECTION.md`.
- For any collection path `kb/foo/`, the contract is `kb/foo/COLLECTION.md`.
- The collection id is the directory name, such as `notes`, `reference`, or `cmpl-reference`.
- Python tooling and agents should use the same collection convention.
- Shipped and user collections must occupy distinct top-level paths.
- Installed shipped collections should be visibly read-only/library-shaped, likely through a `cmpl-*` prefix.
- Agent routing should have a canonical KB-owned home, but should not be structural authority.
- Any installed-link remapping should happen at install time, not during agent operation.
- Startup-file routing can be frontloaded later by individual agents or harness integrations.

## Direction

Use top-level installed library collections:

```text
kb/
  notes/
  reference/
  instructions/
  sources/
  reports/
  work/
  cmpl-notes/
  cmpl-reference/
  cmpl-instructions/
```

Do not install `kb/commonplace/` as a wrapper collection or namespace. Do not create `kb/commonplace/COLLECTION.md`.

Treat `cmpl-*` collections as read-only shipped Commonplace library material:

- `kb/cmpl-reference/` is installed product documentation for Commonplace.
- `kb/cmpl-instructions/` contains operational instructions and promoted skill bodies.
- `kb/cmpl-notes/` contains methodology examples/theory that reference docs and skills may cite.

Do not install `kb/agent-memory-systems/` by default. It can remain in this repo as a development corpus/showcase unless a later optional install mode is designed.

Add canonical routing guidance inside the KB, likely `kb/README.md`, instead of making `AGENTS.md` or `CLAUDE.md` the source of truth. Agent startup files may later summarize or point to `kb/README.md`, but that is a frontloading optimization.

## Packaging Alternatives

The unresolved design choice is where to pay the complexity cost: in the source repo layout, in the installer, or in a hybrid split. All alternatives should preserve the same installed-facing convention: shipped Commonplace collections appear as top-level `cmpl-*` collections.

### Alternative A: Keep Source Layout, Rewrite on Install

Source repo stays as it is today:

| Source collection | Installed target |
|---|---|
| `kb/notes/` | `kb/cmpl-notes/` |
| `kb/reference/` | `kb/cmpl-reference/` |
| `kb/instructions/` | `kb/cmpl-instructions/` |

The installer rewrites deterministic path surfaces during the copy:

- Markdown links between shipped collections, such as `../reference/foo.md` to `../cmpl-reference/foo.md`.
- Markdown links from shipped instructions to shipped notes/reference.
- Any frontmatter path fields that point at moved shipped collection-local type docs, if present.

Benefits:

- This repo continues to look like a working Commonplace KB with familiar `kb/notes`, `kb/reference`, and `kb/instructions` paths.
- Most existing docs and tools remain oriented around the current source layout.

Costs:

- The installer owns link rewriting and must be tested carefully.
- Installed docs are produced artifacts, not verbatim copies.
- Every new path-bearing surface needs a decision: rewrite, leave alone, or avoid.

### Alternative B: Rename Source Collections to `cmpl-*`

Source repo adopts the installed shipped-library layout:

```text
kb/cmpl-notes/
kb/cmpl-reference/
kb/cmpl-instructions/
```

The installer copies these collections mostly verbatim.

Benefits:

- Install is simpler and safer because shipped links already point at installed paths.
- Source and installed shipped library have the same layout.
- Path bugs become visible during normal development rather than only after install.

Costs:

- This repo stops looking like a consuming project's user-owned KB.
- Many existing docs, links, indexes, tests, and instructions need a larger migration.
- We may need user-collection templates or fixtures to keep examples of `kb/notes`, `kb/reference`, and `kb/instructions` visible.

### Alternative C: Hybrid Rename Only Installed Documentation

Move or author installed product documentation as `kb/cmpl-reference/`, but keep methodology notes and instructions in the current source locations. Installer rewriting then applies only to the collections that are remapped.

One variant: `cmpl-reference` is copied without rewriting, while shipped notes remain sourced from `kb/notes/` and are rewritten to `kb/cmpl-notes/` at install time.

Benefits:

- Commonplace product documentation can be developed against its installed path.
- The highest user-facing documentation surface avoids install-time path distortion.
- The migration can be staged instead of all-at-once.

Costs:

- Mixed source conventions are harder to explain.
- Cross-links between `cmpl-reference` and unprefixed source collections still need careful treatment.
- Agents working in this repo may need more routing guidance during the transition.

### Alternative D: Do Not Install `cmpl-notes` by Default

Install only operational product surfaces:

| Source collection | Installed target |
|---|---|
| `kb/reference/` | `kb/cmpl-reference/` |
| `kb/instructions/` | `kb/cmpl-instructions/` |

Under this option, reference docs and skills must either avoid depending on shipped notes or cite only the subset promoted into reference/instructions.

Benefits:

- Smaller installed KB.
- Clearer distinction between product documentation/skills and methodology corpus.
- Less link rewriting if reference/instructions are made self-contained.

Costs:

- Shipped notes stop being available as examples inside installed projects.
- Reference docs may become less explanatory unless they inline or duplicate some methodology.
- Skills that rely on notes for rationale or definitions need to be audited.

## Current Lean

Do not choose the packaging alternative until we audit links and operational dependencies. The next step is to measure how much shipped reference and instruction content depends on `kb/notes/`, and how much rewriting would be required under Alternative A.

If the dependency surface is small, Alternative D or a hybrid may be best. If the dependency surface is broad, either Alternative A with a tested installer rewriter or Alternative B with a source-layout migration becomes more defensible.

## Canonical Routing Artifact

Create or update `kb/README.md` in installed projects with a concise routing table:

| Need | Start here |
|---|---|
| Write project theory/claims | `kb/notes/` |
| Write project documentation | `kb/reference/` |
| Write project procedures | `kb/instructions/` |
| Read Commonplace documentation | `kb/cmpl-reference/` |
| Use Commonplace operational skills | `kb/cmpl-instructions/` |
| Inspect Commonplace methodology examples | `kb/cmpl-notes/` |
| Store external source snapshots | `kb/sources/` |
| Read generated reports | `kb/reports/` |
| Work on temporary drafts/plans | `kb/work/` |

The table is for agent orientation. It is not a Python config file and should not be parsed as structural authority.

## Implementation Steps

1. Audit shipped cross-collection dependencies.
   - Count links from `kb/reference/` and `kb/instructions/` into `kb/notes/`.
   - Count links among `kb/notes/`, `kb/reference/`, and `kb/instructions/`.
   - Identify non-link path surfaces such as frontmatter type paths and prose paths that are operational rather than illustrative.
2. Choose a packaging alternative.
   - Use Alternative A if preserving the current source layout is more valuable than install simplicity.
   - Use Alternative B if install parity and path correctness during development matter more.
   - Use Alternative C if product docs should move first but a full migration is too large.
   - Use Alternative D if reference docs and skills can be made self-contained without shipped notes.
3. Update `commonplace-init` according to the chosen alternative.
   - Stop copying shipped content into `kb/commonplace/*`.
   - Stop installing `kb/agent-memory-systems/` by default.
   - Generate or preserve a project `kb/README.md` with routing guidance.
   - Add link rewriting only if the chosen alternative needs it.
4. Update Python path expectations.
   - Keep `project_paths.collection_dirs(root)` based on top-level `kb/*/COLLECTION.md`.
   - Ensure `collection_for_path` does not need special cases for `kb/commonplace/`.
   - Audit index refresh, validation, relocation, and review commands for assumptions about fixed collection names.
5. Update skills and reference docs.
   - Replace installed-path references to `kb/commonplace/*` with the chosen installed path convention.
   - Keep examples clear about user collections versus shipped collections.
   - Make read-only behavior explicit in shipped `cmpl-*` `COLLECTION.md` files or top-level routing docs.
6. Update tests.
   - Init scaffolding produces the chosen `cmpl-*` installed collections.
   - No `kb/commonplace/` wrapper is created.
   - `kb/agent-memory-systems/` is not installed by default.
   - Cross-links inside installed shipped content resolve.
   - Collection discovery sees `cmpl-*` as ordinary top-level collections.
7. Validate.
   - Run focused init, path, validation, and index tests.
   - Run `commonplace-refresh-indexes` after any source collection rename.
   - Run `commonplace-validate` on affected durable collections after docs are updated.

## Open Questions

- Should this repo eventually rename its own shipped-library authoring collections to `kb/cmpl-*`, or is installer rewriting cleaner?
- Is `cmpl-*` the right prefix, or should it be more explicit, such as `commonplace-*`?
- Should `kb/cmpl-notes/` be installed by default, or only when reference docs/skills actually cite it?
- Should `kb/README.md` be generated only on init, or should there be a command to refresh it?
- Which exact path surfaces beyond Markdown links need rewriting?

## Closure Criteria

- Installed collections follow the simple direct-child convention.
- Agents can inspect `kb/` and understand which roots are user-owned and which are shipped Commonplace library roots.
- Python and agents use the same collection rule without a registry.
- Installed Commonplace reference docs and skills are operational from their installed paths.
- Startup-file routing is optional frontloading, not required for correctness.

