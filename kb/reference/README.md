# Reference

Current-state documentation for the commonplace system.

Use this collection when the question is not "is this generally true?" but "how does commonplace work today?" It holds subsystem descriptions, current architecture notes, and architecture decision records for the live repo.

## Start here

- [architecture.md](./architecture.md) — current repo layout, installed-project boundary, and where the operational surface lives now
- [type-system.md](./type-system.md) — current document taxonomy, base types, and the old-to-new type migration summary
- [ADR 006: two-tree installation layout](./adr/006-two-tree-installation-layout.md) — the installed-project boundary and why commonplace ships the way it does

## Collection boundary

- Use `kb/notes/` for transferable claims and theory.
- Use `kb/reference/` for current-state descriptions and decision history.
- Use `kb/instructions/` for imperative procedures and operator guidance.

If a reference note names a general principle, it should link back to the theory note in `kb/notes/` that argues for it. If a theory note depends on a concrete commonplace implementation, it should link here.
