---
description: "Curated head for the reflective-systems tag — self-representations that change behavior, from the proof-governed Gödel machine to Commonplace's human-in-the-loop boundary"
type: kb/types/tag-readme.md
index_source: tag
index_key: reflective-systems
complete: true
---

# Reflective systems

A [reflective system](./definitions/reflective-system.md) maintains descriptions of itself that are causally connected in both directions: the descriptions are kept current as the system changes, and editing them changes what the system later does. This repository is one: its notes, skills, and validators describe how it works, and the agents working on it read them, act on them, and update them when the system changes.

Reflection is structural: a causal path from self-description to behavior, with no promise that changes along it are governed. Closure is the stronger property: reflection only requires that the path exists, while closure requires a governed answer to each decision a change raises — what form the new artifact takes, how it is verified, what gives it force — and [a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md).

The two ends of that gap have occupants. Schmidhuber's Gödel machine makes all of its code rewritable, including the routine that searches for code changes, and accepts a rewrite only with a proof that it helps — [a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md), closed to the point of ignoring improvements it cannot prove. [Commonplace classifies as a reflective system](../reference/commonplace-as-a-reflective-system.md) with the same skeleton and a looser gate: tests, validators, and a human maintainer who notices what to change and judges whether it helped; each accepted improvement lands in the self-representation and compounds.

## Other notes

- [Actionable theory](./definitions/actionable-theory.md) — the prior question: when can written theory guide an operator's actions at all
- [Governed adaptation requires search, evaluation, and operative retention](./governed-adaptation-requires-search-evaluation-and-retention.md) — the change-loop functions reflection feeds but does not supply
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — a system may edit its prose and code freely while its only reach over the model weights is choosing which sealed model runs

## Related Tags

- [foundations](./foundations-README.md) — the broader core theory this thread sits inside
- [constraining](./constraining-README.md) — closure is a constraining property of methodology-as-input
- [computational-model](./computational-model-README.md) — reflection and intercession as computational concepts generalized to socio-technical boundaries
