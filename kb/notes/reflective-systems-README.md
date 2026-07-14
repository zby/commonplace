---
description: "Curated head for the reflective-systems tag — self-representations that change behavior, from the proof-governed Gödel machine to Commonplace's human-in-the-loop boundary"
type: kb/types/tag-readme.md
index_source: tag
index_key: reflective-systems
complete: true
---

# Reflective systems

A [reflective system](./definitions/reflective-system.md) keeps descriptions of itself that its own processes read and write — edit a description and the system later behaves differently. This repository is one: its notes, skills, and validators describe how it works, the agents working on it consume and update them, and changing them changes what those agents do.

Reflection is structural: a causal path from self-description to behavior, with no promise that changes along it are governed. Closure is the stronger property: reflection only requires that the path exists, while closure requires a governed answer to each decision a change raises — what form the new artifact takes, how it is verified, what gives it force. Indeed, [a methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md).

The two ends of that gap have occupants. Schmidhuber's Gödel machine makes all of its code rewritable, including the routine that searches for code changes, and accepts a rewrite only with a proof that it helps — [a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md), closed to the point of ignoring improvements it cannot prove. [Commonplace classifies as a reflective system](../reference/commonplace-as-a-reflective-system.md) with the same skeleton and a looser gate: tests, validators, and a human maintainer who notices what to change and judges whether it helped; each accepted improvement lands in the self-representation and compounds.

## Other notes

- [Governed adaptation requires search, evaluation, and operative retention](./governed-adaptation-requires-search-evaluation-and-retention.md) — the change-loop functions reflection feeds but does not supply
- [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md) — a system may edit its prose and code freely while its only reach over the model weights is choosing which sealed model runs
- [Human-inclusive boundaries make reflection cheap; autonomy is the discriminating gradient](./human-inclusive-boundaries-make-reflection-cheap.md) — because the human-inclusive boundary makes the bare classification near-trivial, autonomy — how much of the loop runs without a human — is the axis that discriminates
- [Improving an agentic system crosses the prose-symbolic boundary](./improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md) — reliability-improving changes cross between prose and code, so single-form reflective coverage cannot carry them

## Related Tags

- [foundations](./foundations-README.md) — the broader core theory this thread sits inside, including [actionable methodology](./definitions/actionable-methodology.md), the operator relation a governed recommendation presupposes
- [constraining](./constraining-README.md) — closure is a constraining property of methodology-as-input
- [computational-model](./computational-model-README.md) — reflection and intercession as computational concepts generalized to socio-technical boundaries
