# Work

Experimental workshop space. Purpose-driven working artifacts that haven't codified into notes yet.

Each workshop is a directory exploring a specific workflow end-to-end: from question through sourcing and extraction to finished notes. The goal is to discover what patterns actually emerge from use, rather than designing structure upfront.

## Active Workshops

- [gate-refactor/](./gate-refactor/) — moving review storage and selector state from monolithic review bundles to gate-native definitions, memberships, and per-gate acceptances
- [gate-selector-flexibility/](./gate-selector-flexibility/) — redesigning `gate_selector.py` so selection can vary by inventory, gate scope, ranking, and output shape without reopening the simplified mtime-based review architecture
- [ingestion-and-deep-search/](./ingestion-and-deep-search/) — rethinking how sources get analysed and how analysis instructions flow from the caller
- [connect-refactoring/](./connect-refactoring/) — splitting /connect into discovery-only + directed reading for file mutations
- [validation/](./validation/) — making validation a reliable part of the workflow: when, what, and how to validate (hooks, skill upgrades, periodic revalidation)
- [trace-derived-systems-review/](./trace-derived-systems-review/) — review queue and execution packets for the next wave of trace-derived learning systems surfaced from web search
- [tool-loop-control/](./tool-loop-control/) — rewriting the framework-loop note so it starts from why the standard tool loop exists and where convenience should end
- [skills-vs-instructions/](./skills-vs-instructions/) — when should a procedure be a skill vs an instruction file with CLAUDE.md routing? Testing five hypotheses against platform docs, practitioner experience, and KB theory
- [db-layer/](./db-layer/) — brainstorming whether and how to add a database layer over the filesystem as review/revision scripts accumulate query complexity
- [type-system-rationalization/](./type-system-rationalization/) — reconciling frontmatter types, directory-scoped `types/` templates, and path-based exemptions into one coherent design
- [review-db-migration/](./review-db-migration/) — moving gate reviews out of gitignored markdown files into a local SQLite review store with explicit acceptance state and import/export tooling
