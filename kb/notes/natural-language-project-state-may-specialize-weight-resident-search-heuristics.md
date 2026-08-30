---
description: "Project-specific natural language may specialize general search heuristics already represented in an LLM's weights by supplying the current intent, theory, branch history, and constraints"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, context-engineering, self-improving-systems]
---

# Natural-language project state may specialize weight-resident search heuristics

A pretrained language model may already contain general heuristics for noticing
anomalies, generating alternatives, ranking promising directions, selecting
probes, persisting, and backtracking. It does not already contain the current
state of a particular project.

The conjecture is that retained natural language can specialize those general
heuristics by supplying the project's intent, working theory, prior branches,
failures, commitments, and constraints. The language need not encode a complete
search procedure. The weights may supply the general competence while the
retained project state determines how it applies here.

The relevant evidence is behavioral. Withholding, replacing, or perturbing the
project state should change branch choices and their later consequences. A
plausible explanation that leaves search unchanged does not establish the
conjecture.

## Scope

- This is an empirical conjecture, not a claim that current models already
  allocate open-ended search effectively.
- Specializing search heuristics does not give the resulting choices acceptance
  authority.

---

Relevant Notes:

- [Lightweight search control allocates further search without licensing adoption](./lightweight-search-control-allocates-further-search-without-licensing-adoption.md) — grounds: identifies the limited authority of the specialized heuristics
- [Weight-resident methodologies provide context-efficient behavioral compression](./weight-resident-methodologies-compress-behavior-in-context.md) — grounds: shows how compact language can select a larger behavioral pattern already represented in weights
- [A capable agent needs methodology selection, not just relevant knowledge](./capable-agents-need-methodology-selection.md) — extends: distinguishes selecting a governing method from merely supplying relevant facts
