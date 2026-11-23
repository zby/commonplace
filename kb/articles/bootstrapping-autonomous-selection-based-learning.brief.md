---
type: types/write-brief.md
description: "Commission for the bootstrap supplement: explain how Commonplace bootstraps autonomous selection-based learning in a reflective self-improver by moving update decisions from its operator to computation"
---

# Brief: Bootstrapping autonomous selection-based learning

## Intent

Explain to an external technical reader how Commonplace intends to reach the
lead article's autonomous selection-based learning: start human-assisted and
reflective, retain selected updates, let the system build its own software,
transfer update decisions to computation one kind at a time, and judge
progress by a removal test with stated failure conditions.

## Must keep

- Anchor on selection-based learning as defined in
  `kb/theory/definitions/selection-based-learning.md` and on the lead article
  `continual-learning-with-fixed-model-weights-llm-selected-updates.md`.
- Early in the body, state plainly that the full machinery being built is a
  reflective self-improving system, using the lead article's phrase
  "reflective self-improvement by selection" and linking the reflective-system
  and self-improving-system definitions. Relate the names once: selection-based
  learning names the process; the reflective self-improver is the whole system
  that runs it on its own method, with selection inside the boundary.
  "Autonomous" means computation, not the operator, supplies the search and
  selection decisions. Keep one term per concept afterwards.
- The lead article's boundary: outside input (tasks, bug reports,
  objections) does not make the loop human-assisted; a person making an
  internal update decision does.
- Keep the removal test (decisions moved) separate from whether selected
  updates improve later work; point to the testing article for the latter.

## Must exclude

- "Reflective self-improver" in the title; the title stays "Bootstrapping
  Autonomous Selection-Based Learning with Commonplace".
- The theory-builder framing (theory builder, stating and criticizing
  theories, Popper's cycle) as the thing being built. Sibling articles and
  source notes still use it; do not reintroduce it from them.

## Reserved decisions

- Renaming the file to match the new title; the user decides when to run
  `commonplace-relocate-note`.
