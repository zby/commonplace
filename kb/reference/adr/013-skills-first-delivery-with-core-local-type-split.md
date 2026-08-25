---
description: Historical decision to move skills to top-level sources, keep KB Goals always-loaded, split types into core and local, and use dynamic type discovery for practitioner-defined types
type: ../types/adr.md
tags: []
status: superseded
---

# 013-skills-first-delivery-with-core-local-type-split

**Status:** superseded by [ADR-014](./014-scripts-as-python-package-one-tree-model.md)
**Date:** 2026-04-08

## Context

Installation copied a ~160-line always-loaded AGENTS.md template carrying the routing table, content workflow, conventions, and search patterns. Embedded KBs paid that context cost on every turn, competing with the project's own CLAUDE.md. The template also hardcoded this KB's types (`adr`, `related-system`, `structured-claim`), so a practitioner building a different KB had to edit the template to remove them. Skills had matured enough to absorb most of the routing table on demand.

## Decision

Skills become the primary delivery mechanism: the always-loaded template shrinks to KB Goals, a KB-exists pointer, a skill reference table, key index paths, and structural search patterns, and everything about how to operate the KB moves into on-demand skills shipped as a plugin from a top-level `skills/` directory. Types split into a small set of core types shipped with the framework (note, text, index, source-review) and local types that stay in this repo as optional examples; framework skills depend only on core types and discover local types dynamically from `kb/*/types/`. KB Goals stay always-loaded because scoping decisions happen before any skill fires. A skill whose dependencies are not yet framework-installable (`review-related-system`) stays repo-local until the review system has a framework surface.

## Consequences

Embedded KBs pay roughly a third of the previous always-loaded context, and practitioners add domain types by dropping templates into `kb/*/types/` without editing framework files. Skills must be well-written because they replace always-loaded instructions, core type templates must stay generic, and dynamic discovery adds complexity to the write skill. Plugin packaging was replaced by direct installation in ADR-014; skills-first delivery and the core/local split carried forward.

---

Relevant Notes:

- [ADR-006: two-tree installation layout](./006-two-tree-installation-layout.md) — foundation: establishes `kb/` as user content and `commonplace/` as framework
- [014-scripts-as-python-package-one-tree-model](./014-scripts-as-python-package-one-tree-model.md) — the later accepted packaging model that refined this delivery approach
