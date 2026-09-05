---
description: "Supplement to the automated software house conjecture: fixed computational semantics allow mutable update policies; transition closure constrains how the house may change but does not establish that it sustains adequacy"
type: kb/articles/types/article.md
status: draft
byline: Zbigniew Lukasiak
source_notes:
  - kb/notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md
  - kb/notes/warranted-autonomy-is-bounded-by-oracle-domain.md
  - kb/notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md
---
# Transition closure and practical reachability

> **Draft supplement.** This develops the transition-closure and Gödel-machine
> arguments in [The Automated Software House
> Conjecture](./automated-software-houses-with-fixed-llms.md). It may change.
> Comments and counterexamples are welcome on [the repository's GitHub
> Discussions page](https://github.com/zby/commonplace/discussions).

**TL;DR.** Every change in an automated software house must arise through its
current machinery and permitted external inputs, including changes to that
machinery. This requirement constrains how the house develops; it does not
establish that the house stays adequate as it changes. Practical operability
requires evidence of sustained adequacy within declared resource limits.

A software house is the complete persistent system that develops and maintains
software for users. The conjecture asks for a **witness house**: a concrete
example meeting four conditions together. It must apply program theory,
revise coherently, continue without internal human production decisions, and
perform reliably within a declared scope, horizon, and budget. Program theory
means understanding the software's purpose, organization, and how to handle new
requests. Coherent revision means responding to a failed assumption in ways
that support later modification. Below, an *adequate state* is one from which
the house can perform that work; reliability concerns sustaining such states
across runs and later requests.

Eligible constructions use only distributed-parametric models available by the
conjecture's chosen cutoff, 2026-09-02, and keep them fixed during a **witness
run**, an attempt to demonstrate the four conditions. People may build the
seed. During the run, users may supply requirements, domain facts, observed
outcomes, and judgments about visible behaviour. Human implementation,
diagnosis, design selection, or admission of revisions would instead perform
an internal production role and end the run.

## The observation

Represent the mutable state of the house by `s`: its product, notes, tools,
evaluators, context assembly, and update machinery. Include every internal
history-dependent variable that can affect an update; persistent tool or
environment state must either belong to `s` or be declared external. Learned
components remain fixed parameters: model weights, adapters, embedding models,
parametric routers, and parametric critics. Indexes regenerated from mutable records
under pinned algorithms belong to `s`; their embedding models remain fixed.
These are different [representational
forms](../notes/definitions/representational-form.md) within one system.

Write `R(s, x)` for the possible successor states on input `x`, under the
system's fixed computational semantics and distributed-parametric models. Inputs can
include user requests, tool results, and operating consequences. Sampling
rules may assign probabilities to successors. If omitted internal history can
affect an update, augment `s`; a list of artifact types alone does not establish
that the representation is sufficient.

Define reachability through **admissible paths**. Start at the seed `s0`, take
an input sequence allowed by the declared input process, and at each step
choose a successor permitted by `R(s, x)`. A state is reachable exactly when
it occurs at a finite prefix of such a path. The input process may condition
later inputs on the observed run; its rules must still be declared in advance.
Each extension must satisfy both the transition relation and those rules.
This is the sense of **transition closure** used here.

Closing a set of house states under each individually permitted input is not
enough. If a protocol permits request B only after request A, that construction
could wrongly admit a path starting with B. One can recover an ordinary
state-set closure by adding the input process's relevant history or state to
the representation. The path definition keeps the restriction explicit.

The overall relation `R` stays fixed, but the update policy encoded in `s` may
change. Rewriting an evaluator changes what it accepts under the same rules
for executing code. The rewrite is itself an `R` transition from the preceding
state. Closure therefore permits self-modification without requiring the seed
to specify every later decision.

## Consequences for the conjecture

### A possible path need not be practical

If an update process can emit and retain arbitrary state, adequate successor
states may be possible yet extremely unlikely. The quantity the conjecture
needs is **continuation reliability**: starting from an adequate house, the
chance of sustaining adequate performance across later requests over the
declared horizon within the resource budget. A house that stays adequate for
a few requests and then drifts differs from one that sustains adequacy across
the horizon, even if both pass an early evaluation.

The conjecture allows a human-built seed, so it does not ask how likely an
autonomous process is to reach an adequate house from a non-adequate seed.
That **hitting probability** is the [bootstrap
article's](./bootstrapping-the-first-automated-software-house.md) measure, and
seed-construction effort is reported separately for the same reason.

### The existential claim and nondeterminism are separate

The conjecture says at least one eligible construction and declared regime
works. That construction may be deterministic, nondeterministic, or
probabilistic. Its transition model does not settle whether success requires
one possible path, all paths, almost-sure success, or a probability threshold.
The **witness protocol**, the evaluation plan fixed before testing, must specify
that separately. One lucky run cannot establish practical reliability.

### The declared input process is part of the claim

Distinguish the set of admissible request and consequence histories, the
history realized in one run, and the distribution or procedure selecting
histories. With `R` fixed, allowing more histories can enlarge the reachable
set without making adequate successors more probable. The selection procedure
may direct more runs toward failure. Practical operability depends on that
process, not an informal claim that the house receives richer requests.

### Permitted self-modification can suppress adequate successors

The policies reachable from the seed may exclude adequate states or make them
negligibly likely. An evaluator can govern a rewrite of itself, but the current
machinery must be capable of producing that rewrite. Coherent revision tests
whether new evidence leads to a suitable policy and continued operation
without internal human decisions. An evaluator-editing operation alone does
not establish that capacity. The supporting note on [methodology governing its
own extension](../notes/a-methodology-governs-its-own-extension-only-as-far-as-it-settles.md)
examines this limit on internally settled revisions.

A human correction during the run breaks the autonomous lineage even if the
machinery could have produced the same result. The actual path matters. This
requirement applies generally to autonomous systems; fixing distributed-parametric models
is an additional restriction of the software-house conjecture.

## The Gödel-machine comparison

A Gödel machine admits a rewrite only after proving, under its current axioms
and utility function, that switching to the proposed program has higher utility
than continuing the current search. Its code, including the proof searcher and
utility representation, may be rewritten only when the predecessor
formalization licenses the change. This is a [proof-governed case of
self-modification](../notes/goedel-machines-are-a-proof-governed-case-of-self-modification.md),
not a separate requirement of transition closure. The retained [Schmidhuber
source analysis](../sources/goedel-machines-schmidhuber.ingest.md) locates the
proof condition in §3.2 and the treatment of rewritable utility in the FAQ.

The same source describes `state2theorem`, which records observed state in a
time-labelled theorem (§3.2, printed pp. 10–11). This lets environmental
observations enter the proof process; it does not remove the proof requirement.

| | Gödel machine | Conjectured house |
|---|---|---|
| Rewrite condition | Proof under current axioms and utility | A fallible process produces and, where applicable, admits a successor from evidence |
| External input | Observations enter through formalized operations; rewrites still require proof | Current interpretive capabilities use requests, tool results, and consequences to challenge program theory |
| Warrant | Conditional proof relative to the encoded formalization | Empirical warrant bounded by evaluators and later exposure |
| Characteristic failure | A useful change remains unavailable because the required proof is not found or expressible | Harmful successors receive enough probability to undermine continued adequacy |

Deductive closure concerns the theorems derivable from the Gödel machine's
axioms. Transition closure concerns reachable machine states. Neither alone
establishes reliable software-house operation. For the conjectured house,
[the domain covered by available checks](../notes/warranted-autonomy-is-bounded-by-oracle-domain.md)
limits what successful evaluation warrants; permitted self-modification does
not remove that limit.

## What this changes in the witness protocol

Use the main article's [protocol declaration](./automated-software-houses-with-fixed-llms.md#boundaries-evidence-and-uncertainty):
starting system, boundary and workload, resources, and evaluation. The path
account explains why the allowed histories and their selection procedure must
both be fixed, and why sustained adequacy needs its own measure, separate from
the bootstrap article's question of reaching an adequate house.

The [training](./the-software-house-as-the-unit-of-training.md) and
[bootstrap](./bootstrapping-the-first-automated-software-house.md) articles ask
how the house might acquire understanding and machinery absent from the seed.
The [construction comparison](./nearest-existing-constructions-to-a-reachability-witness.md)
assesses the available evidence for the four conditions together.

## Open questions

- What evidence would establish useful continuation reliability for a given
  product and risk level?
- How should a witness protocol preserve relevant novelty while preventing
  post-hoc removal of failed requests?
- Which environmental state must be represented internally, and which inputs
  need separately reported provenance and authority?
