---
description: "Curated head for the reflective-systems tag — the lens the agent-memory-system reviews are conducted through: a low-bar definition, three independent gradings over it (coverage, closure, autonomy), and what they let you ask of a system that claims to improve itself"
type: kb/types/tag-readme.md
index_source: tag
index_key: reflective-systems
complete: true
---

# Reflective systems

A [reflective system](./definitions/reflective-system.md) keeps descriptions of itself that its own processes read and write — edit a description and the system later behaves differently. This repository is one: its notes, skills, and validators describe how it works, the agents working on it consume and update them, and changing them changes what those agents do.

## What the frame is for

Three jobs, all of them already running in this repository.

**Reviewing systems that claim to learn.** The [agent-memory-system-review](../agent-memory-systems/types/agent-memory-system-review.md) type is built out of this vocabulary. It instructs every reviewer to record a system's representational forms, its behavioral authority as *consumer, channel, and force*, and whether its artifacts are knowledge or system-definition — then to find its **promotion path**, whether a candidate can move from prose advice to symbolic validator to enforced gate, which the spec calls "often the most design-relevant question." Those are this cluster's terms, and the [comparison matrix](../agent-memory-systems/systems-table.md) is generated from them. Without the frame the reviews collapse into feature lists.

**Diagnosing a learning system that does not learn.** The decomposition says where to look: a reviewed note no prompt-assembly step loads has no *consumer*; an approved patch never merged has no *channel*; a generated validator nothing invokes has no *force*. In each the work happened and the loop stayed open. It also predicts what a better evaluator cannot buy you — search reach and evaluation strength are independent limits, and no verifier can select a candidate the generator never reached.

**Reading a "self-improving system" claim without being taken in.** Under a human-inclusive boundary reflection is nearly free, so *the system modifies itself* discriminates almost nothing — every maintained codebase qualifies. The questions that discriminate are which functions run without a human, and what oracle bounds them; autonomy in evaluation extends exactly as far as verification reaches, and no further.

## The wire, where the representation is prose

Where the self-representation is a body of retained artifacts rather than code an interpreter reads, the causal path runs through search — so [retrieval failure is reflection failure](./retrieval-failure-is-reflection-failure.md). A represented constraint no process can find is inert, and an index that claims completeness it does not have cuts the path exactly where a consumer was relying on it.

## The base and its gradings

The definition sets a deliberately low bar, and its exclusions carry the weight: reflection is *not* autonomy, *not* verification, and *not* closure. Each of those three exclusions is picked up by a note that turns it into a grading over the same base. The gradings answer different questions and move independently — a system can widen one without touching the others.

- **Coverage — what is represented.** [Reflective coverage is graded across representational forms](./reflective-coverage-is-graded-across-representational-forms.md): a claim must name the form (prose, symbolic, distributed-parametric) and the operation depth. A system may edit its prose and code freely while its only reach over the model weights is choosing which sealed model runs.
- **Closure — what the methodology settles.** [A methodology governs its own extension only as far as it settles the meta-decisions it raises](./a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md): reflection only requires that a causal path exists; closure requires a governed answer to each decision a change raises — what form the artifact takes, how it is verified, what gives it force.
- **Autonomy — who performs the functions.** [Human-inclusive boundaries make reflection cheap](./human-inclusive-boundaries-make-reflection-cheap.md): because a standing maintainer inside the boundary makes the bare classification near-trivial, autonomy is the axis that actually discriminates.

All three grade over one decomposition: [governed adaptation requires search, evaluation, and operative retention](./governed-adaptation-requires-search-evaluation-and-retention.md) — the change-loop functions reflection feeds but does not supply.

## Occupants

Schmidhuber's Gödel machine makes all of its code rewritable, including the routine that searches for code changes, and accepts a rewrite only with a proof that it helps — [a proof-governed case of reflective self-modification](./goedel-machines-are-a-proof-governed-case-of-self-modification.md), closed to the point of ignoring improvements it cannot prove. It sits at the far corner of all three gradings at once.

[Commonplace classifies as a reflective system](../reference/commonplace-as-a-reflective-system.md) with the same skeleton and a looser gate: tests, validators, and a human maintainer who notices what to change and judges whether it helped. It grades unevenly — modification depth on prose and code, selection depth on the model; closure on some axes and not others; humans at search and the judgment-heavy evaluation.

## Consequence for agentic systems

[Improving an agentic system crosses the prose-symbolic boundary](./improving-an-agentic-system-crosses-the-prose-symbolic-boundary.md): the changes that improve reliability move behavior between prose and code rather than staying in either, so coverage of a single form cannot carry them.

## Related Tags

- [foundations](./foundations-README.md) — the broader core theory this thread sits inside, including [actionable methodology](./definitions/actionable-methodology.md), the operator relation a governed recommendation presupposes
- [constraining](./constraining-README.md) — closure is a constraining property of methodology-as-input
- [computational-model](./computational-model-README.md) — reflection and intercession as computational concepts generalized to socio-technical boundaries
