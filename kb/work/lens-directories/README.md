# Per-lens directories for analysis summaries and tables

Posed by the operator on 2026-10-22, while retiring Agent Memory Systems from
the site's main menu.

## Goal

Give each analysis lens its own directory for cross-system summaries and
tables. Each directory links into the per-system members already published
under `kb/agentic-system-analyses/retained/<system>/` (for the memory lens,
`memory.md` and `memory-profile.md`); it does not copy, move or re-derive them.
Readers then navigate by lens rather than through the frozen
[Agent Memory Systems](../../agent-memory-systems/README.md) collection, which
stays buildable but leaves the main menu.

## Operator decisions

- **Per-lens directories hold summaries and tables.** Per-system analysis
  parts stay where publication puts them; the lens directories link to them.
  This is not a change to the analysis set layout, `ARTIFACT.yaml` or
  `integrate`.
- **Agent Memory Systems leaves the main menu** but its collection stays. Its
  links keep resolving.
- **The menu change belongs here**, because the memory lens directory is its
  replacement.

## Starting evidence (2026-10-22)

- The lenses are the analyst members of a set: `runtime`, `memory`,
  `epistemic`, `workflow`. Only memory has structured comparison fields
  (`memory-profile.md`, under the
  [memory profile contract](../../agentic-system-analyses/types/agentic-system-memory-profile.md)).
  The other lenses have prose reports only.
- The memory lens already has table machinery in
  [`kb/agentic-systems/comparisons/`](../../agentic-systems/comparisons/README.md):
  `scripts/build_systems_matrix.py`, `render_systems_table.py` and
  `analyze_matrix.py` read the retained sets directly. The
  [landscape synthesis skill](../../agentic-systems/instructions/synthesize-agent-memory-landscape/SKILL.md)
  writes the cross-system summary. The comparison population there is
  currently empty until regeneration.
- Coverage: 152 of the 159 historical Agent Memory Systems reviews have a
  retained analysis, matched by repository name; all 191 retained sets carry
  `memory.md` and `memory-profile.md`. Not covered: `ace`, `sift-kg`,
  `clawvault`, `operational-ontology-framework`, `agentic-harness-engineering`
  (unresolved in [agentic-system-completion](../agentic-system-completion/README.md)),
  `Awesome-Agent-Memory` (out of scope) and `scroll`; five of eight lightweight
  reviews also lack one.
- The site menu is built by `on_config` in
  `src/commonplace/docs/properdocs_hooks.py` from every `kb/<dir>/README.md`.
  Its `UNPUBLISHED_COLLECTIONS` exclusion also suppresses generated directory
  listings, so hiding a collection from the menu alone needs a menu-only
  exclusion. `kb/index.md` line 34 also links Agent Memory Systems from Home.

## Decisions (operator, 2026-10-22)

- **Placement: `kb/agentic-systems/comparisons/<lens>/`.** Both collection
  contracts already route comparative work there: "Comparative writing belongs
  in `kb/agentic-systems/`" and "`comparisons/` holds cross-system analyses and
  generated tables". Per-system members stay in `kb/agentic-system-analyses/`.
  The memory table scripts' outputs move from `comparisons/` to
  `comparisons/memory/`.
- **Per-system lists are generated at build time** by the docs hook, as
  `current-analyses.md` is, from `current_analyses(root)`, linking each
  system's `<lens>.md` (and `memory-profile.md` for memory). Nothing is
  committed when an analysis lands. Each lens directory keeps an authored
  `README.md` explaining the lens and linking its list, tables and summaries.
- **Lenses without structured fields** (runtime, epistemic, workflow) start
  with the lens README and the generated list only. A table waits for
  comparison fields that emerge from prose across runs; a summary waits for a
  commission.
- **Staleness by kind.** Generated lists cannot go stale. Memory tables stay
  command-generated and committed; their rows already carry artifact hashes,
  and the lens page states the selected population and generation date or
  commit. A build-time population check is deferred until a stale table
  causes harm. Landscape syntheses are commit-bound snapshots; the lens
  README lists each with its date and system count.
- **Order, revised.** The generated list is lens-generic, so all four lens
  directories landed together (2026-10-22): each has an authored README and a
  build-time `systems.md`; memory also links profiles and holds the relocated
  table outputs.

- **Menu: one "Agentic Systems" dropdown** replaces the separate "Agentic
  System Analyses" and "Agentic Systems" entries: Analyses (the generated
  current-analyses list), one entry per lens, and Authored accounts (the
  `kb/agentic-systems/` landing). A lens joins the dropdown only when its
  directory lands; memory comes first. "Agent Memory Systems" leaves the menu.

## Open questions

- Comparison fields for runtime, epistemic and workflow. Their members carry
  structured body content — shared records of six kinds, and the epistemic
  object inventory and authority-route ledger with controlled route-function
  and architectural-status values — but no frontmatter comparison block like
  `memory-comparison`. A table needs either an extractor over those records
  or a profile step per lens; either is a method change.

## Boundaries

- Do not edit retained analysis sets or the publication method; per-lens
  comparison fields for runtime, epistemic or workflow would be a separate
  method change.
- A landscape synthesis run needs its own commission.
- Historical Agent Memory Systems content stays as it is.

## What closes this workshop

The memory lens directory exists and replaces Agent Memory Systems in the
main menu; the placement and generation choices are recorded where the
collection contracts or an ADR will find them; each other lens either has a
directory or a recorded reason it waits. Then remove this directory and its
Active Workshops entry.
