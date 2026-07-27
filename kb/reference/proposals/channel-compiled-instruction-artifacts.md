---
description: "Proposal: resolve execution channel at install time so an agent reads one literal procedure, extending build-time generation from paths to shell and command form"
type: ../types/design-proposal.md
tags: [architecture]
---

# Channel-compiled instruction artifacts

Commonplace already decided that skills are generated at build time rather than parameterised at runtime, and `commonplace-init` already resolves paths that way. Execution channel — which shell, which command spelling, which virtual-environment layout — escaped that decision. It is carried instead as branches the reading agent resolves on every use: a native-Windows section in the control plane, a bare-name-then-`.exe` fallback rule, and Bash-shaped snippets inside promoted skills that a PowerShell agent must translate before it can act.

That is runtime parameterisation wearing natural-language clothing. The [adopted claim](../../notes/generate-instructions-at-build-time.md) rejects it in placeholder form for exactly the reasons that apply here — interpretation overhead on every use across every substitution site, with occasional silent misreads — and states the canonical form of a skill as standalone, with the templating step producing that form rather than leaking into the runtime artifact. A natural-language branch is a substitution site whose resolver is the LLM.

## Current state (as of 2026-07-25)

- `commonplace-init` is the single build/install step. It copies scaffold trees verbatim and resolves a small set of placeholders (project name, absolute project root). [Instruction generation](../instruction-generation.md) states the intended property directly: "There are no runtime variables in the generated artifacts."
- Promoted skills are projected into `.claude/skills/` and `.agents/skills/` as real copied directories, after ADR 037 retired symlinks and Windows junctions. The instructions collection contract already calls these "compiled copies" — today that compilation is identity plus path substitution.
- Non-promoted instructions are copied into `kb/commonplace/instructions/` and read in place. No projection, no substitution.
- Eleven promoted skills carry 28 shell fences, every one labelled `bash` or `sh` and none `powershell`. Two contain constructs that cannot run under PowerShell: a `test -d … && echo … || echo …` block with `2>/dev/null` in the health-check skill, and `xargs -r` in the connect skill, whose own instructions flag the `-r` guard as load-bearing.
- The control plane spends roughly a screenful of always-loaded context on channel-conditional procedure — Windows venv setup, the `.exe` fallback, `Test-Path` diagnosis, a pytest cache caveat — of which at most one branch is ever true on a given machine.
- The Commonplace source checkout is deliberately not initialised, so no compile step currently covers the repository the maintainer operates.
- Provenance: phase-1 audit finding F8 and its workshop proposal on promoted-skill portability, which treats the symptom (make every snippet run everywhere) rather than the mechanism (resolve the channel once, emit one form).

## Problem

An instruction that must serve two channels either fails on one of them or carries both. Both outcomes are defects, and they trade against each other:

- **Carrying one channel** leaves the other non-operative. The consumer and force exist, but the channel is unavailable across part of the declared frame, so the intended behavior does not occur there. The sharpest instance is the diagnostic skill named as the recovery path for a broken environment being itself the most channel-bound artifact in the set.
- **Carrying both** makes every reader pay for a branch that is false for them, and makes the agent the resolver. A wrong resolution is worse than a missing command: an absent binary fails loudly, while an improvised translation of a guarded pipeline can drop the guard and return a plausible wrong answer.

The channel is known at install time. Nothing about it requires the reading agent's runtime state, which is the standing test for what should be frontloaded.

## Forces

- **Context cost.** Unresolved branches consume always-loaded and per-skill budget for text that is inert on the machine reading it.
- **Silent mistranslation.** Agent-side translation of shell idioms can fail without failing loudly.
- **Derived-copy hazard.** A compiled artifact is a derived copy; the KB's standing rule is that such a copy must be checked or absent. Deepening compilation deepens the drift surface that `commonplace-init` already reports rather than clobbers.
- **Review target ambiguity.** Gates and freshness currently hash source text. If the compiled form is what agents execute, reviewing only the source leaves the executed artifact unreviewed — the same dependency gap the audit recorded as F4 and F6.
- **Search surface.** The instructions tree is the searchable source; multiplying compiled copies multiplies lexical matches. Already true for skills, and worse if the whole tree compiles.
- **Authoring and review cost.** A channel-branching source is harder to write, review, and keep symmetric than a single literal form — the cost moves rather than vanishing.
- **Uncompiled source checkout.** The repository where this methodology is authored gets no compile step by current design, so any benefit skips its own maintainer unless that changes.
- **Boundary of "channel".** Shell, path convention, tool availability, and environment-activation style are separable facts that may or may not deserve a single name.

## Option space

Sketched to bound the design, not to choose. Options are not mutually exclusive.

- **A — Portability convention only.** Keep both channels in the source and require every snippet to run everywhere or label its channel. Cheapest; retains the interpretation step and the context cost; this is roughly the existing workshop proposal.
- **B — Compile promoted skills.** Extend the existing projection from identity-plus-paths to channel resolution. Smallest change that reaches the artifacts agents execute most.
- **C — Compile the instructions tree.** Same treatment for non-promoted instructions, which today have no projection at all.
- **D — Compile the control plane.** Emit a channel-resolved `AGENTS.md`, removing the always-loaded branch that benefits nobody on a resolved machine.
- **E — Resolve later than install.** Compile at session start or on demand rather than at init, so the artifact tracks the machine currently running it rather than the machine that installed it.

Cross-cutting: whether the source carries explicit per-channel branches, or stays channel-neutral while the compiler selects idioms from a table it owns.

## Free choices

Marked as undecided, with the consideration each turns on:

- **What a channel is** — one named profile, or a set of independent capability facts. Turns on whether the axes actually co-vary in practice.
- **When compilation runs** — install, session start, or explicit refresh. Turns on how often the channel changes relative to the artifacts.
- **What compiles** — skills, all instructions, the control plane, or a declared subset. Turns on where the interpretation cost actually lands.
- **Whether compiled output is committed or ignored** — turns on whether a reader without a build step must still find a working procedure.
- **How the source checkout participates** — it is currently outside the compile step by explicit rule; changing that is a separate decision with its own cost.
- **What the review target is** — source, compiled form, or both. Turns on the freshness questions already open in F4 and F6.
- **What the compiler owns** — only substitution of declared placeholders, or a maintained mapping of channel idioms. The second is a much larger commitment.

## Operativity

- Options B, C, D consume an existing channel: `commonplace-init` writes files that harness skill loaders and agents already read, with the force those artifacts already carry. No new consumer is required — the compile step and its outputs exist.
- Option E has **no consumer yet**: nothing runs at session start today, so a hook or equivalent must be built before the option is available at all.
- Option A changes no mechanism; its force is authoring convention plus whatever check backs it.
- If any option adds a portability check, its warrant is narrow: a detector for known channel-specific idioms where a portable equivalent exists. It cannot prove general shell portability, and should report rather than infer semantic equivalence. Warrant stops at the idiom list it carries.

## Adoption criteria

- A worked case: one artifact compiled for a real channel, with the before/after context cost and the resolved-branch count stated rather than estimated.
- A stated answer for the derived-copy question — what checks the compiled form against its source, or why an unchecked copy is acceptable here.
- A stated review target, consistent with whatever freshness can currently represent.
- Evidence that the interpretation cost being removed is real: at minimum, the observed failure class (two skills that cannot run on a declared-supported channel), and preferably an instance of an agent mistranslating rather than failing.

## Out of scope

Historical command examples outside instructions and promoted skills; mechanical translation between shell languages; and any change to which channels Commonplace declares support for. This proposal is about resolving the declared set at build time, not revising it.

---

Relevant Notes:

- [Generate KB skills at build time, don't parameterise them](../../notes/generate-instructions-at-build-time.md) — rationale: the adopted claim this extends from paths to execution channel, including the standalone-canonical-form rule
- [Frontloading spares execution context](../../notes/frontloading-spares-execution-context.md) — rationale: the test for what belongs at build time, and the validity-window obligation a compiled artifact inherits
- [Indirection is costly in LLM instructions](../../notes/indirection-is-costly-in-llm-instructions.md) — rationale: why an unresolved branch costs on every read
- [Operative change](../../notes/definitions/operative-change.md) — rationale: the consumer/channel/force test the Operativity section applies
- [A derived copy of recomputable truth must be checked or absent](../../notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md) — rationale: the constraint a compiled artifact must satisfy
- [Instruction generation](../instruction-generation.md) — current-state: the shipped build step this proposal extends
