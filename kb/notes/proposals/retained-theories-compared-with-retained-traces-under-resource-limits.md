---
description: "Proposal: a framework for comparing retained theories with retained traces, separating what bounded context and decision budgets make necessary from the conjecture that theories are an efficient compression; unadopted vocabulary"
type: kb/types/note.md
traits: [has-comparison]
---

# Retained theories compared with retained traces under resource limits

This is a [theory proposal](./README.md): finished, unadopted, and not a
premise for other notes.

**What adoption would add.** Three terms and one decomposition. The terms
are the *trace strategy* (retain the traces of past work and consult them
when needed), *effective context* (the amount of loaded material a model
uses well), and *derived state* (results of processing history that stand
in for it in later processing). The decomposition separates, by resource
limit, what is necessary from what is conjectured: with no limits retained
theories add no reach; bounded context makes derived state necessary for
some decisions; a bounded decision budget makes retaining it necessary for
some; and whether theories are an efficient compression of experience is
the conjecture a comparison tests.

**Adopted so far (2026-09-19), in plain words and without these terms.** The
[lead article](../../articles/learning-by-theory-refinement-with-fixed-models.md)
now says that the paradigm claims nothing about what can be learned in
principle, names the two needs that limits on context and computation
create, states the compression conjecture, and keeps the records as
evidence behind the theory; the
[learning by theory refinement](../definitions/learning-by-theory-refinement.md)
definition says the same about records. The
[testing supplement](../../articles/testing-the-theory-refinement-program.md)
now specifies the raw-record treatment and names records with a maintained
index as a further arm. The
[theory builder](../definitions/theory-builder.md) definition admits a
builder that regenerates its theories.

**What adoption would still change.** The three terms would get
definitions, the articles would state the decomposition with them, and the
retained-form comparison would be split into the arms below, with the two
quantities from steps 3 and 4 as independent variables.

## Trigger and cost

Import when the first retained-form comparison is designed, or when a note
or article cannot state which claim follows from which limit without the
terms. Until then
the program's conjecture can be stated in plain words without these terms:
retained theories are an efficient way to compress experience for later
decisions.

The cost is three terms to define and keep consistent, and a second axis
(resource limits) in how the program states its claims. The distinctions
under Open questions that are marked undeveloped would add more, and are
deliberately left undeveloped until experimental work shows which of them
a result depends on.

## The rival strategy

The **trace strategy** retains the traces of past work (observations, tool
output, reasoning, outcomes) and consults them when needed. The model
builds whatever explanation it needs while reasoning and discards it. What
survives to the next decision is the traces, plus whatever retrieval
machinery finds them.

The program already names this rival. The
[lead article](../../articles/learning-by-theory-refinement-with-fixed-models.md)
sets the paradigm against "retaining raw records or summaries of experience
without an explanation", and the retained-form comparison in the
[testing supplement](../../articles/testing-the-theory-refinement-program.md)
has a raw-record treatment. Two things are missing: a statement of what the
paradigm claims against the rival and what it concedes, and a rival arm as
strong as the strategy in practice.

## The argument

The argument separates what follows from each resource limit. Determinism
can be granted as an idealization, because deterministic models are
possible. Unlimited context cannot be granted: for a fixed model, effective
context is a constant that no budget buys more of. So part of the position
is a claim about reach, not only about efficiency.

**Step 1. With no limits, retention adds no reach.** Assume deterministic
models. Then every retained state of a builder is a function of its
machinery and its external inputs. A builder could regenerate all past
calculations at each step. The only state that cannot be recomputed is what
came from outside: observations, outcomes, and acceptance judgments.
Traces, summaries, and theories are all caches of a derivation from those
inputs. So with no limit on context or computation, a builder that refines
retained theories can reach nothing that a regenerating builder cannot.

The same holds for the update operation, separately from retention. With
unlimited resources, deriving a theory from all the evidence at once is at
least as good as refining it step by step, because step-by-step refinement
depends on the order of its history and prefers small changes. FORTE, the
classical system, can stop at a local maximum.

**Step 2. Keeping all traces preserves past calculations.** If the model
could load every past calculation, it would not need to regenerate those
calculations, and the cache would discard none of their recorded detail.
This is possible while the traces fit in the model's **effective context**:
the amount of loaded material the model actually uses well, which is
smaller than the nominal window. It does not settle which strategy is
better. Reading and interpreting the traces still costs computation, while
a retained theory may save repeated synthesis or carry a mistaken
abstraction forward.

**Step 3. Decisions requiring synthesis across contexts need derived
state.** A large history alone does not require such synthesis: a decision
might depend on one retrievable record. But when a decision requires
combining evidence that cannot fit in one effective context, the builder
needs some means of carrying intermediate results across processing steps.

**Derived state** represents results of processing history that stand in
for that history in later processing: a summary, an intermediate synthesis,
an aggregate computed by code, a theory. Sequential processing,
hierarchical summaries, reconstruction over multiple passes, and retained
theories can all supply it. Computation outside the model can also combine
evidence and supply the result; the model need not perform every step.

The pure trace strategy considered here appends records and loads a
selection of intact traces into one context. Its limit applies to decisions
for which no such selection supplies enough evidence. A strategy that
carries intermediate results across steps or computes an aggregate outside
the model uses derived state, even if it discards that state after the
decision. This distinguishes operations, not mutually exclusive systems:
retrieval and synthesis can be parts of the same strategy.

Bounded context together with this demand for synthesis establishes the
need for intermediate results. It does not select their form or make
regeneration impossible. With unlimited computation, a builder can rebuild
its derived state at every decision, over as many passes as it needs.

**Step 4. Retention is necessary when reconstruction exceeds the decision
budget.** With unlimited computation, retaining derived state instead of
rebuilding it is memoization. Under a fixed budget per decision, suppose
the minimum cost of reconstructing the information needed for a decision
from records eventually exceeds that budget. Continued performance then
requires reusable state that avoids that reconstruction. Retention is
necessary under this condition, but not sufficient: maintaining and using
the retained state must also fit the budget.

A growing history does not by itself establish the condition. Relevant
evidence must require increasingly costly reconstruction; a bounded lookup
or a fixed recent window may otherwise suffice indefinitely. The comparison
must hold the decision's required reliability fixed, since an approximation
may reduce reconstruction cost while failing that requirement. Within a
finite assessed horizon, whether reconstruction exceeds the budget is a
question to measure, not a guaranteed crossover.

The two limits differ in kind. More computation can be bought, so the
budget limit is economic. More context cannot be bought for a fixed model,
so the context limit in step 3 is architectural, and the condition in this
step is the weaker of the two.

This does not force purely incremental updating. For example, rebuilding
at history sizes 1, 2, 4, 8, and so on gives bounded average reconstruction
cost per arriving record if each rebuild costs linearly in history size.
It does not bound the cost of each rebuild or guarantee a strict budget
per decision. Using such a schedule also requires a way to incorporate new
evidence between rebuilds, or a justification for delaying its use. The
costs of that work must be counted alongside reconstruction.

| Limits and task conditions | What follows |
|---|---|
| No resource limits | Retained theories add no reach |
| Bounded context; a decision requires combining evidence that cannot fit in one context | Intermediate derived state is necessary; with unlimited computation it can be reconstructed for each decision |
| Bounded budget per decision; minimum reconstruction cost exceeds it | Continued performance requires reusable derived state; retaining it is insufficient unless maintenance and use also fit the budget |
| Any of the above | Whether retaining and refining theories serves later decisions better than other strategies is the conjecture under test |

**The form is the conjecture.** Derived state is not necessarily lossy
compression. An aggregate can preserve everything needed for a particular
decision exactly, and an intermediate representation can be larger than
its input. A compact representation may discard information; its adequacy
depends on which later decisions it must support.

Our conjecture is that theories are an efficient compression
technique: for the context they occupy and the maintenance they cost, they
preserve more of what later decisions need than the other forms do. We
therefore provisionally choose to retain and refine
[tentative theories](../definitions/theory-refinement.md#tentative-theory)
as the form of derived state, one strategy for reusing synthesis across
decisions. This is a working choice to test, not a rejection of the
alternatives. Retrieval can supply evidence for refinement; summaries can
help navigate history; regeneration can replace an inadequate theory. A
builder may combine these techniques.

The position has three parts. Some decisions require intermediate
synthesis across contexts. Some decision budgets require reusing its
results because reconstruction would exceed the budget. Our conjecture
concerns when retaining and refining theories serves those decisions well.
Neither history growth alone nor the need for derived state establishes
an advantage for theories.

## Why choose learning by theory refinement provisionally

**Retained theories can save repeated synthesis.** An explanation derived
from many episodes can be retained and consulted without repeating its
whole derivation. When new evidence exposes an error, theory refinement
can revise that explanation while seeking to preserve useful prior
knowledge. This may cost less than reconstructing it, but bounded context
does not establish that comparison. Periodic reconstruction or a combined
strategy may perform better.

An [addressable theory](../definitions/theory-refinement.md#what-the-operation-requires-of-a-theory)
has consequences that evidence can contradict, parts available as candidate
repair locations, and parts editable separately. These properties make it
possible to target a revision and inspect what changed. They do not
guarantee that the diagnosis is right or that an edit preserves untested
behavior. Nor are they exclusive to theories: summaries can contain
correctable claims, and indexes can have entries that retrieval failures
motivate us to revise. The comparison must establish what explanatory
content and its explicit maintenance add to those alternatives.

**Explanations may serve future cases that differ from past ones.** Lossy
compression is good or bad relative to the decisions it must later serve.
An explanation can have consequences for cases never observed. Popper makes
the point about theories in general: a theory's consequences bear on
situations of which "many of these situations have never been thought of"
([Popper 1966](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md), verbatim). This is
[explanatory-reach](../first-principles-reasoning-selects-for-explanatory-reach-over.md),
and it motivates testing theories against descriptive summaries rather
than assuming that every compression serves later decisions equally well.
It also agrees with the payoff conjecture in
[learning by theory refinement may improve sample efficiency under structured shifts](../learning-by-theory-refinement-may-improve-sample-efficiency.md):
the advantage may be largest when later work differs from earlier work
in structured ways. A mistaken explanation may instead make those decisions
worse.

## Retrieval as a rival and a complement

Retrieval selects traces for a query while keeping each selected item
intact. It can compete with retained theories or support their construction,
application, and revision. Two possible sources of advantage for retained
theories deserve testing.

- **Need detection.** Consulting traces "when needed" requires some means
  of detecting the need. A theory on the decision path may supply it, as
  in the lead article's snippet case where a syntax check passes. A
  retrieval strategy can also include routine lookups or learned triggers;
  comparisons should not deny it those mechanisms.
- **Repeated synthesis over a large history.** If a decision needs more
  evidence than fits in one context, retrieval may require several passes
  and intermediate synthesis, which is derived state in the sense of
  step 3. A retained theory may save that work on later decisions. The
  advantage depends on reuse, retrieval quality, maintenance costs, and
  the errors introduced by compression.

These considerations motivate varying history length relative to effective
context, together with the budget and the decisions' demands on history.
They do not establish a sharp crossover: theories may save work before
traces exceed context, and selective retrieval may remain effective well
past that point.

Retrieval also needs machinery. An index encodes choices about how traces
can be found; a theory may guide when to consult them and which ones bear
on a decision. Whether a learned index itself counts as a theory depends
on its content and how it is used, not merely on its being retained or
editable. Comparisons should state which mechanisms each arm shares and
which contribution they isolate.

## A trace records a process; a theory is a product

Popper separates "the world of thought-processes, and the world of the
products of thought-processes", and adds: "While the former may stand in
causal relationships, the latter stand in logical relationships"
([Popper 1966](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md), verbatim). Applying this to the comparison is our
reading, not his. A reasoning trace records a process: what was considered,
in what order, and what happened next. A theory is a product: it has
consequences, and it can be incompatible with a case or with another theory
whether or not anyone has noticed. The first requirement of an addressable
theory, consequences a case can contradict, is a requirement on a product.
A trace that contains a past theory holds the product inside a process
record, and using it as a theory means extracting it first. The first-class
claim below is then the claim that keeping the product extracted, with an
identity and versions, serves later criticism better than extracting it on
each use.

Popper's account does not decide between the strategies. His objective
knowledge is whatever can be "contained in a book; or stored in a library"
([Popper 1966](../../sources/popper-a-realist-view-of-logic-physics-and-history-1966.ingest.md), verbatim), which covers records as well as theories,
and he does not consider bounded context, retrieval, or cost. His account
of consuming theories includes "criticising them, changing them, and often
even demolishing them, in order to replace them by better ones" (same
source, verbatim). Replacement stands beside revision there, which agrees
with treating refinement as a provisional choice that regeneration can
supplement.

Every retained theory is tentative in Popper's sense, however well it has
done; that status does not come from the compression being lossy. What the
lossy compression adds is a reason to keep the records, as the evidence
from which the theory can be criticized and derived again.

## When the traces contain past theories

Retained reasoning may include past theories and how they failed. A builder
can extract an existing theory and correct it against evidence while
seeking to preserve useful prior knowledge. That is theory refinement,
whatever the storage format. A prior theory merely appearing in the input
is insufficient: the builder may ignore it, quote it, or independently
reconstruct a replacement. The criterion concerns the operation performed
on the theory, not its presence in a record.

Against a trace strategy that performs refinement, the comparison concerns
whether keeping the theory as a first-class addressable object pays more
than extracting it again when needed. Trace storage does not preclude
identity, versions, or separately editable claims, so each treatment must
state which of those facilities it supplies. Addressability comes in
degrees. Against a strategy that reconstructs independently, the comparison
also varies the update operation.

A clean arm that retains observations and outcomes only is still useful.
It tests reconstruction from evidence without retained reasoning. This arm
can still synthesize theories during execution, so it does not isolate
whether synthesis helps at all.

## Costs and concessions

- Neither context fit nor history length alone establishes which strategy
  performs better. Retrieval and reconstruction remain viable alternatives
  and possible components of a builder that refines theories.
- A retained theory can carry a mistaken abstraction forward, and can omit
  a detail a later case needed.
- Theories cost maintenance. A comparison has to count construction,
  validation, retrieval, and revision for every arm.
- That theories are an efficient compression technique is a conjecture. No
  comparison has been run.

## What a comparison would need to vary

The arms below separate two claims. The *machinery claim* is that
consulting traces needs retained machinery, such as an index, to find the
right traces at the right time. The *first-class claim* is that a theory
kept as an addressable object serves later decisions better than one
extracted again when needed.

The testing supplement's single raw-record treatment tests the machinery
claim and the first-class claim at once. Candidate arms that separate
them:

| Arm | What it isolates |
|---|---|
| Observations and outcomes only | Reconstruction without retained reasoning |
| Full traces with generic retrieval | The trace strategy without a learned index |
| Full traces with a learned or curated index | The machinery claim |
| First-class theories, with traces kept as evidence | The first-class claim |

Two quantities become independent variables, following steps 3 and 4: how
much evidence a decision must combine relative to effective context, and
what reconstruction costs relative to the decision budget. History length
matters only through them. The existing descriptive-summary and
wrong-theory arms stay. If the full set is too costly, the articles should say which arm is deferred
and what that leaves untested.

## Open questions

- How is effective context measured for a given model and task, well
  enough to place the threshold and vary history length against it?
- Is a learned index an addressable theory? If a case can contradict it and
  its entries can be blamed and edited separately, the third and fourth
  arms differ in degree, not in kind.
- Which decisions in practice depend on a synthesis wider than effective
  context? If they are rare, the limit in step 3 is seldom binding. The
  comparison then turns mainly on reconstruction costs and the form
  conjecture.
- When a prior theory is in the input, how does an assessor tell that the
  builder refined it and did not reconstruct independently? The criterion
  is the operation performed, which the output alone may not show.
  Candidates are a
  [citation at the decision point](../citing-retained-theory-at-the-decision-point-is-a-mediation-trace.md)
  and a matched run with the prior theory removed from the input.
- When should the builder refine a retained theory, reconstruct it from
  evidence, or combine the two? Which observable costs or failures should
  trigger a change of strategy?
- Does dropping the determinism idealization change step 1? Without it,
  regeneration yields a distribution over theories, which bears on
  stability for consumers but not obviously on reach.
- Do the adopted hypotheses need rewording now that the
  [theory builder](../definitions/theory-builder.md) definition admits a
  builder that regenerates its theories, or only the treatment tables?
- Undeveloped: derived state does two jobs. A summary, aggregate, or theory
  substitutes for the history, and the reader does not load the source. An
  index routes into the history, and the reader loads only the part it
  needs. An index alone does not supply the synthesis in step 3, but it
  lowers reconstruction cost in step 4, and a growing store of theories
  needs one too.
- Undeveloped: three further points about compression. A theory with its
  retained traces resembles a two-part code, in which the theory covers the
  regularities and the traces hold the exceptions. Description length is
  relative to the decoder, here the fixed model, which supplies background
  knowledge. And a theory may grow with the number of regularities while
  traces and summaries of events grow with the number of cases.

---

Relevant Notes:

- [Learning by theory refinement](../definitions/learning-by-theory-refinement.md) — defined-in: the paradigm whose advantage over retained traces this framework would test
- [Theory refinement](../definitions/theory-refinement.md) — defined-in: the operation, the addressable theory, and the tentative-theory status the argument uses
- [Theory builder](../definitions/theory-builder.md) — defined-in: the persistent system whose retained state the comparison varies
- [First-principles reasoning selects for explanatory-reach over adaptive fit](../first-principles-reasoning-selects-for-explanatory-reach-over.md) — grounds: why an explanation may serve cases that differ from past ones
- [Learning by learning by theory refinement may improve sample efficiency under structured shifts](../learning-by-theory-refinement-may-improve-sample-efficiency.md) — extends: the payoff conjecture this framework leaves to the comparison
- [Retaining episode evidence keeps a distilled rule open to re-examination](../retaining-the-episode-keeps-a-distilled-rule-re-derivable.md) — grounds: why the traces stay as evidence behind the theory
