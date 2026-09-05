---
description: "Conjecture that an automated software house can sustain open-ended coherent software change with LLMs available by 2026-09-02 and held fixed; system boundary, program-theory bearer, and witness conditions"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/code-complements-weight-prompt-with-symbolic-operations.md
  - kb/notes/definitions/representational-form.md
  - kb/notes/definitions/software-house.md
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/naur-equates-machine-execution-with-formulated-criteria.md
  - kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md
  - kb/notes/program-theory-sustains-search-under-delayed-feedback.md
  - kb/sources/goedel-machines-schmidhuber.ingest.md
  - kb/sources/programming-as-theory-building.ingest.md
---
# The Automated Software House Conjecture

*Open-ended software development with fixed LLMs*

> **Draft.** This article may change. Comments and counterexamples are welcome
> on [the repository's GitHub Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** We use *software house* for the complete persistent system that
keeps changing a piece of software for its users, not only for a company. The
conjecture is that, within at least one declared product scope, such a house
can handle relevant requests not listed in advance with no human in an
internal production role, using only LLMs and other learned components
available by 2026-09-02 and held fixed during the run. The house may start
with human-written project theory, tools, tests, and production machinery.
The claim is that the resulting system can carry the complete production
function, including the program-specific understanding needed for coherent
change. It does not require the house to have discovered its starting theory
or outgrown its human-built seed. Companion articles ask [how a software
house should be trained](./the-software-house-as-the-unit-of-training.md)
and [how the first automated one might be
built](./bootstrapping-the-first-automated-software-house.md).

## Claim

**The automated software house conjecture.** At least one automated [software
house](../notes/definitions/software-house.md) capable of open-ended coherent
software change is practically reachable using only LLMs and other learned
components available by 2026-09-02 and held fixed during the run.

*Practically reachable* means that the house succeeds within a product scope,
request-generating process, operating horizon, and budget of compute, time,
and cost declared before the run. *Open-ended* means that the declared
process can produce relevant requests and consequences that were not listed
one by one in advance. It does not mean that one house must handle every
possible software product or request.

The house may begin from a state constructed by people. That state may
include the product, project-specific purposes and rationale, tools, tests,
evaluators, workflows, context assembly, safety boundaries, and other
production machinery. The conjecture asks whether this complete system can
then do the work without a human inside it. How the starting state was
created is not part of the claim.

## The boundary

An *internal production role* is work the house depends on to develop and
evolve the software, whoever performs it. Internal roles include interpreting
project knowledge, making implementation decisions, diagnosing failures,
comparing candidates, revising project state or production machinery, and
choosing which revision takes effect.

Users remain outside the house when they provide product requirements, domain
facts, preferences, observed outcomes, or acceptance judgments about visible
behaviour. A user crosses into an internal role when asked to diagnose an
implementation failure, choose among internal designs, supply a missing
project-specific design decision, or select the retained successor. The role,
not the person's identity, decides which side of the boundary an act falls
on.

An automated software house has no human in an internal production role over
its declared scope and horizon. User participation is compatible with
automation; hidden human production work is not.

## Why the claim is not trivial

Open-ended change brings questions that available checks do not settle. Say a
product built for one customer per deployment must now serve many tenants.
The tenant identifier can enter the data model in several ways. More than one
choice may pass the current tests, while only some preserve the assumptions
on which later changes depend.

Choosing and revising such designs needs what the computer scientist Peter
Naur called a program theory: the capacity to relate the software to the
activity it supports, explain why it is organized as it is, and relate a new
demand to that organization. We use coherent modification across later
demands as the main behavioural test. [Holding a program theory means
sustaining coherent search under delayed
feedback](../notes/program-theory-sustains-search-under-delayed-feedback.md):
the first choice may be tentative, but the process must use project-specific
understanding to guide search, interpret failure, backtrack, and recover when
later consequences arrive.

[Naur's compiler case](../sources/programming-as-theory-building.ingest.md)
reports that full code, annotations, extensive design discussion, and personal
advice did not give one successor team enough program-specific
understanding. The case therefore rules out only a simple answer in which more
documentation of the same kind automatically transfers that understanding. It
tested [one historically bounded document package and way of using
it](../notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md).
It did not test linked rationale, machine-maintained indexes, semantic
retrieval, dependency-aware context assembly, or automatic loading of the
relevant material at the decision point.

One route from Naur's argument to a human-only conclusion depends on treating
machine execution as execution of explicitly formulated criteria.
An LLM is still formal computation, but it can interpret a paragraph about
why retry logic belongs in the caller without that judgment first being
reduced to a complete rule. [Formal execution and explicitly formulated
criteria are not the same
thing](../notes/naur-equates-machine-execution-with-formulated-criteria.md).
A successful house would show that a computational composite can carry the
program-theory function defined here. It would reject that route to a
human-only conclusion, but would not settle Naur's separate claim that the
relevant judgment cannot be reduced to a finite set of formulated criteria.

## A possible bearer of the program theory

The conjectured house combines three kinds of component:

- Fixed LLMs supply general linguistic, programming, and reasoning capacity.
  They interpret the current request and the project state and produce
  candidate judgments and changes.
- Natural-language project state supplies persistent purposes, commitments,
  explanations, evidence, and prior decisions. For example: "installs must
  remain a single file, so the store is SQLite; do not add a server
  dependency."
- Symbolic software supplies exact behaviour and continuity. This includes
  the product, tools, schemas, tests, context assembly, schedulers,
  validators, rollback, and retention rules.

None of these holds the theory alone. A note nobody loads has no effect. A
fixed LLM without enough project state reconstructs or guesses instead of
carrying understanding from one change to the next. Software executes a
decision without supplying all the judgment that selected it. The house as a
whole has to carry the program-theory function.

The theory need not be stored as one explicit artifact. The house may use a
separately retained rationale, reconstruct working understanding from
records, or combine both. What matters is causal use: the project-specific
state must change proposal, evaluation, diagnosis, or recovery, including
where the relevant implication is not stated verbatim.

## What remains fixed

For a witness run, every eligible model version and every other learned
component is declared and pinned before testing. This includes model weights,
adapters, embedding models, learned routers, learned critics, and similar
components. A provider endpoint that may change silently is not enough unless
its model lineage can be audited for the run.

The product and the house's natural-language and symbolic state may change.
The house may edit project rationale, code, tests, tools, evaluators,
workflows, context assembly, or its own production machinery. Derived indexes
may be regenerated mechanically from that mutable canonical state under
algorithms pinned before the run; they are not an independent learned update.

The operational loop can therefore have this shape:

```text
request + operating evidence + current product and project state
  -> fixed learned components + current production machinery
  -> changed product and, where needed, changed project state or machinery
  -> later request
```

This is not a claim that the house learned to construct its starting state.
Human-written starting theory and machinery are allowed. Once the witness run
starts, however, every internal decision and successor state must come from
the house's current state, its fixed learned components, and the permitted
external inputs. A human rescue in an internal role ends that witness run.

This is the transition closure of the declared starting state: later states
must be reachable through the current house and permitted inputs. The
observation says where successors may come from; it does not require the
house to outgrow or rediscover its starting design.

Pinning is an experimental condition, not a recommendation for a mature
software house. It isolates whether the system around current models can
carry the complete software-house function without help from a newer or
newly trained model.

## What a witness must show

One working house must show the following conjunction.

1. **Holding and application.** Across novel changes, the house uses
   project-specific understanding to guide proposal, evaluation, diagnosis,
   or recovery, including cases whose correct handling is not stated verbatim
   in its retained state. With everything else held equal, withholding or
   replacing the relevant state changes what the house does next in a
   predicted way.
2. **Coherent revision.** When a later request or operating consequence
   exposes an inadequacy in the current product understanding, the house
   revises the product, retained project state, production machinery, or a
   combination, and the successor supports coherent later modification.
   The starting understanding may have been supplied by people.
3. **Automated continuation.** The house sustains those capacities across the
   declared scope and horizon with no human in an internal production role.
   Requirements, facts, visible outcomes, and product-level acceptance may
   continue to come from users.
4. **Practical reliability.** The declared evaluation must show useful
   success within the resource budget and continued adequacy across the
   horizon. One lucky path establishes only possibility, not practical
   reachability.

These obligations do not fix which form carries the theory or which mutable
surface changes. Storing or citing a rationale is insufficient if it does not
govern a later decision. A gate that can reject is insufficient if the
accepted successor is not adequate. Passing tests on one requested change is
insufficient if the house cannot preserve coherence across later demands.

Initial acquisition of project theory is not an obligation. Neither is
computational production of the starting tools, evaluators, or workflows.
Those are stronger training and bootstrapping questions.

## Formal contrast and existing constructions

The fully formal contrast is AI researcher Jürgen Schmidhuber's [Gödel
machine](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md),
a proof-governed construction that can rewrite its own code. It is not a
software house: it has no users, and the only software it changes is itself.
An embedded prover admits a rewrite only after proving, from the current
axioms and formal utility function, that switching pays. Its starting
formalization is supplied in advance, which the conjecture stated here
allows. The price is that it "must ignore those self-improvements whose
effectiveness it cannot prove"
([Schmidhuber](../sources/goedel-machines-schmidhuber.ingest.md), §2.4,
verbatim).

At the level of state-transition provenance, both systems obey the same descent
constraint: every next state must arise through the current state's machinery
and permitted inputs. Their system boundaries and successor relations still
differ. The Gödel machine admits only a
proof-licensed successor. The house may make a fallible change, observe later
consequences, and recover. A novel demand can affect the Gödel machine's
rewrite only insofar as its formalization gives that demand
utility-relevant meaning. The house instead relies on model interpretation,
available checks, and later exposure.

Reviewed records describe separate parts of the possible house: persistent
project records, code and tool revision, reject-capable gates, rollback, and
long-running human-agent production. Their code-inspected rows can support
implementation claims; papers and practitioner or product reports support only
what those sources describe. No row supplies the missing conjunction: a complete
user-facing software-house boundary, fixed learned components, a demonstrated
program-theory function across novel changes, and continuation with no human in
an internal role. Evidence for separate components does not show that they
compose.

## Boundaries and epistemic status

The conjecture is existential. It says only that at least one eligible
construction works for some declared product scope, request process, horizon,
and budget. It does not claim a universal software house.

The witness rules out two post-hoc escapes. The learned components are pinned
before testing, so a newer model or newly trained auxiliary component cannot
supply the missing capacity. The scope, request process, horizon, resource
budget, and success threshold are also declared before testing, so they
cannot be narrowed after a failure.

The request process must be able to expose relevant novelty rather than replay
a fixed benchmark list. Its admissible histories, the history realized in one
run, and the probability or selection procedure over histories are distinct.
The admissible set and selection procedure are fixed before the run. Repeated
runs or another justified estimate must show that adequate operation receives
usable probability and persists across the declared horizon.

The cutoff applies only to a run intended to establish the claim. Ordinary
development may use newer models. In a witness run, however, a newer model
must not supply trial-specific theory, diagnose internal failures, compare
candidates, select successors, or fill any other internal role.

The need for a program theory is a theoretical argument, not a proved
theorem. That current LLMs can participate in a system carrying that function,
and that such a system is practically reachable, remain conjectures. A
working house establishes the claim only over its declared regime. Failure of
one architecture eliminates that path, not every possible construction.

This article does not claim that explicit project theory is the best carrier,
that updates outside model weights are generally better than weight updates,
or that weights should stay fixed in a mature system. It also does not claim
that the house acquired its starting understanding or learned to build its
own production machinery. It asks only whether a computational software
house can carry the complete production function with current learned
components pinned. The [training
article](./the-software-house-as-the-unit-of-training.md) asks how such a
house should improve once it exists; the [bootstrap
article](./bootstrapping-the-first-automated-software-house.md) asks how to
reach it from a house that still has people in internal roles.
