---
description: "A decision-specific rule for fixing what verified doctrine, task intent, and authorized evidence cannot safely determine while leaving bounded choices to execution"
type: kb/types/note.md
traits:
  - title-as-claim
tags: []
---

# An author should fix what the executor can't determine, not what it will

For each choice in an authored execution, the author should fix what a
competent, authorized executor cannot safely determine from verified inherited
doctrine, the task commission, and authorized decision-relevant evidence. The
author should leave a situational choice open when task intent and live or
actively produced evidence can distinguish among its permitted alternatives.
A harmless choice whose alternatives are all acceptable and decoupled may also
remain open; coordination can instead require one common selection. This
boundary is bidirectional and specific to the choice. The author may uniquely
know intent, binding constraints, acceptance conditions, privileged facts,
external commitments, and cross-task coupling. Execution may instead reveal
current state, tool results, local failures, and evidence produced during the
work. A premature choice can therefore be wrong because upstream lacked
relevant evidence, become wrong when state later drifts, or be overturned by
evidence the work itself produces. Neither actor has to know more overall;
[intent-framed delegation is a control regime, not a short
prompt](./intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md)
owns the underlying information relation.

## Determinability, not what versus how

“Specify what, not how” puts the boundary in the wrong place. An outcome,
decomposition, opening question, or abstraction frame can constrain later
means without naming a method. A method can also encode a binding constraint,
shared convention, or coordination dependency that execution cannot recover.
To fix a choice is to select or constrain it upstream, regardless of whether
the choice is described as *what* or *how*. Leaving a choice open still
requires enough purpose, bounds, and acceptance conditions for the executor to
recognize permitted adaptation. Otherwise the author has omitted part of the
commission and the executor must project an interpretation into the gap.
[Agentic systems interpret underspecified
instructions](./agentic-systems-interpret-underspecified-instructions.md)
explains why added framing and constraints narrow this interpretation space.
Here, an executor can *determine* a choice only when it can select safely from
authorized evidence, preserve the fixed intent and bounds, and recognize when
it cannot make a safe selection.

Determination is not limited to recovering a preselected answer. Verified
doctrine may settle an inherited default, or it may supply interpretive rules
from which the executor derives a new means using task intent and execution
evidence. An unstated choice is safe only when it is inherited, deliberately
delegated, or irrelevant to acceptance and coupling. When none applies, the
omission is a gap rather than discretion.

## Actor, time, and evidence are separate axes

Delegation changes who holds the judgment. Deferral changes when the judgment
is exercised. A different actor can receive a choice and exercise judgment
immediately, while the same actor can retain a choice and decide it later.
Delegation also requires both competence and authority for the particular
choice. When the delegated choice is consequential, it needs the governed
handoff described by [intent-framed delegation is a control regime, not a
short prompt](./intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md),
not merely an instruction that leaves the choice open.

Later timing supplies an information advantage only when a named observation
has some possible result that would change selection, timing, modification, or
abandonment for this choice. Evidence may arrive through later live-state
observation or be produced by an earlier step or bounded probe. Activity
produces decision-relevant evidence only when one of its possible outputs can
change the follow-on choice. [Productive deferral requires option, evidence,
and convergence](./productive-deferral-requires-option-evidence-and-convergence.md)
owns this discriminating-evidence test. Waiting without such an observation
does not improve the decision.

Evidence production does not itself determine the actor or the time of
choice. An author can run a probe and retain the later judgment. Another actor
can exercise judgment immediately from evidence already available. The three
axes must therefore be allocated independently for the choice at issue.

## Arbitrary choices and coupling

A choice is genuinely arbitrary here when no authorized, decision-relevant
evidence selects among its permitted alternatives. Waiting cannot resolve such
a choice. If its alternatives are decoupled and all acceptable, it need not be
fixed. If consistency or hidden cross-task coupling requires several executors
to use one convention, a coordination-bearing actor must establish or expose
one shared selection rather than leave independent local projections. This is
a target-side inference combining the hidden-coupling boundary in [intent-
framed delegation](./intent-framed-delegation-is-a-control-regime-not-a-short-prompt.md),
the no-discriminating-evidence test in [productive
deferral](./productive-deferral-requires-option-evidence-and-convergence.md),
and the plural projections described by [agentic systems interpret
underspecified instructions](./agentic-systems-interpret-underspecified-instructions.md).
For interdependent choices, [solving low-degree-of-freedom subproblems first
can preserve the options of more flexible
ones](./solve-low-degree-of-freedom-subproblems-first-to-avoid-blocking.md);
that scoped ordering mechanism does not decide the whole author–executor
boundary. When alternatives change feasibility, acceptance, or another task's
options, the choice is not genuinely arbitrary. The author must then expose
any hidden coupling and apply the central determinability rule to the
resulting choice.

## Search cost and frontloading

Leaving a choice open makes the consuming executor select among the permitted
interpretations. Fixing a value that is already known and remains valid for
that call can spare discovery, derivation, indirection, or interpretation
work. [Frontloading spares execution
context](./frontloading-spares-execution-context.md) owns that benefit. The
comparison is local and qualitative: frontload a known value when the avoided
work matters, but do not freeze a situational value that discriminating
execution evidence could overturn.

## Scope

Leaving a choice open presumes a chooser competent and authorized for that
particular choice. This note supplies no universal competence test or numeric
measure of information advantage. If the available executor is not competent,
that blocks delegation; it does not by itself show that an early guess will
produce a safe choice. When all choice-relevant inputs are available upstream,
remain valid for the consuming call, and no discriminating execution
observation is expected, resolving even method detail upstream is permissible.
It is not required when the alternatives are all acceptable and no
coordination benefit calls for a common selection. An author may rely on
standing doctrine only when the executor's actual consumption path supplies it
with binding force; otherwise the task commission must carry the needed rule.

Operationalized into:

- [Write an instruction](../instructions/write-instruction.md) — makes stable-input and execution-evidence classification part of instruction authoring
- [cp-skill-write-multistage](../instructions/cp-skill-write-multistage/SKILL.md) — fixes cross-stage invariants and lets workers choose source investigation, claim disposition form, and prose within them
