---
description: "The natural-language part of project state may specialize general search heuristics already represented in an LLM's weights by supplying current intent, theory, branch history, and constraints"
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
retained natural-language state determines how it applies here.

This note isolates one part of project state, not the whole state available to
an agent. Source code, tests, schemas, configuration, execution traces, and other
symbolic artifacts also constrain search. The natural-language contribution
becomes operative when context assembly places it in a prompt; the resulting
semantic operation is instantiated jointly by that prompt and the model's
weights. [Code complements the weight–prompt pair with independently executed
symbolic operations](./code-complements-weight-prompt-with-symbolic-operations.md).

The relevant evidence is behavioral. Withholding, replacing, or perturbing the
natural-language state while holding the model, symbolic project state, tools,
and task fixed should change branch choices and their later consequences. A
plausible explanation that leaves search unchanged does not establish the
conjecture.

## Scope

- This is an empirical conjecture, not a claim that current models already
  allocate open-ended search effectively.
- A retained natural-language artifact is not automatically a prompt. It joins
  the weight–prompt operation only when supplied as model input.
- Showing that code or other project information improves search does not by
  itself establish the distinctive contribution of theory-level organization.
- Specializing search heuristics does not give the resulting choices acceptance
  authority.

---

Relevant Notes:

- [Code complements the weight–prompt pair with independently executed symbolic operations](./code-complements-weight-prompt-with-symbolic-operations.md) — extends: places the prompt-side specialization beside the independently executed symbolic operation class
- [Lightweight search control allocates further search without licensing adoption](./lightweight-search-control-does-not-license-adoption.md) — grounds: identifies the limited authority of the specialized heuristics
- [Weight-resident methodologies provide context-efficient behavioral compression](./weight-resident-methodologies-compress-behavior-in-context.md) — grounds: shows how compact language can select a larger behavioral pattern already represented in weights
- [A capable agent needs methodology selection, not just relevant knowledge](./capable-agents-need-methodology-selection.md) — extends: distinguishes selecting a governing method from merely supplying relevant facts
