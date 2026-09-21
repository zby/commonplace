---
description: "Proposal: distinguish context limits, reconstruction budgets, and the conjectured value of retained theories; trace strategy, effective context, and derived state remain unadopted terms"
type: kb/types/note.md
traits: [has-comparison]
---

# Retained theories compared with retained traces under resource limits

This [theory proposal](./README.md) would add
three terms for resource comparisons: *trace strategy*, *effective context*,
and *derived state*. It separates conditions that require intermediate or
reusable state from the conjecture that retaining theories supplies that
state efficiently. The terms remain unadopted. The
[research arrangement](../commonplace-studies-conjectural-learning-through-retained-theories.md)
already states the retention conjecture without depending on them.

Adoption would be justified if a comparison needs to distinguish these
resource conditions repeatedly and ordinary descriptions no longer suffice.
It would commit the KB to defining the terms, stating how effective context
is assessed, and maintaining their use across comparison notes and articles.
No current experiment requires that import. The proposal does not authorize
changes to experiment protocols.

## What each resource limit establishes

### Unlimited replay can substitute for retained computation

Assume deterministic machinery, access to its initial state, and a complete
record of external inputs and interventions. With unlimited computation and
storage, the system can replay its history to regenerate a retained state.
Under those assumptions, retaining an assembled theory rather than
regenerating it adds no in-principle capability. It can change cost and
stability for consumers. Missing inputs, unrecoverable state, or stochastic
choices invalidate exact replay unless the information needed to reproduce
them is also available.

Replay is not the same as asking a model to synthesize a theory afresh from
outcomes. The replay argument establishes no quality ordering between fresh
synthesis and revising an existing theory. Neither incremental revision nor
reconstruction is defined by a preference for small edits. A local-search
limit in a particular classical algorithm cannot establish a limit for all
criticism-guided revision.

### Some decisions need synthesis across contexts

The proposed **effective context** is the amount of loaded material a model
uses adequately for a specified task and reliability criterion. It need not
equal the nominal context window or remain constant across tasks. A history
larger than that capacity creates no problem when the next decision needs
only a retrievable part.

The proposed **trace strategy** retains records of past work and consults
them when needed. Its simplest form loads a selection of intact records into
one context. That form cannot support a decision when no such selection
contains enough evidence and the decision requires combining more material
than the model can use adequately in one call.

The proposed **derived state** is a result of processing history that stands
in for some of it during later processing. Summaries, aggregates, intermediate
syntheses, and theories can supply it. Multiple passes or computation outside
the model can therefore combine evidence across contexts. Such a strategy
may discard its intermediate results after each decision. Bounded context
under the stated synthesis demand requires some way of carrying results
between steps; it does not require retaining an assembled theory between
decisions. A retrieval index can lower the cost of finding evidence without
itself supplying the required synthesis.

Consulting records when needed also requires detecting that need. A theory
on the decision path may supply the trigger; a retrieval strategy may instead
use learned triggers or routine lookups. Comparisons must allow and price
those mechanisms.

### Some decision budgets require reuse

Suppose the minimum cost of reconstructing information needed for a decision
exceeds its computation budget at the required reliability. The decision
then needs reusable state that avoids that reconstruction, or a change to
the budget or task requirement. Retention alone is insufficient: maintaining,
retrieving, and using that state must also fit the budget.

The limits differ: more computation can be bought, making the computation
budget an economic constraint. For a fixed model, buying more calls does not
enlarge its context window; synthesis across calls must carry intermediate
results. The context limit is architectural under that fixed-model condition.

Growing history does not establish this condition. A bounded lookup or a
fixed recent window may remain adequate. Nor does average cost settle a
strict budget for each decision. Periodically rebuilding at history sizes
1, 2, 4, 8, and so on can bound average work per arriving record when each
rebuild is linear in history size; an individual rebuild can still exceed
the decision budget. Incorporating new evidence between rebuilds also costs
work, or requires accepting delayed use of that evidence.

| Condition | Supported conclusion |
|---|---|
| Deterministic, fully recorded replay with unlimited resources | Retention is unnecessary for reproducing computed state |
| Required synthesis exceeds what one context can support | Information must be combined across processing steps |
| Required reconstruction exceeds the decision budget | Continued performance needs reuse or a changed constraint |
| Any of these conditions | The best retained form remains a separate question |

## Why theories might earn their costs

A theory can retain an explanation synthesized from many episodes. Later
work may use its consequences without repeating that synthesis. A criticism
can identify what to reconsider; [addressability](../definitions/addressable-theory.md)
can make particular assumptions or parts available for inspection. Neither
property guarantees a correct diagnosis, a small edit, or preservation of
untested behavior.

The conjecture is that, for some demands, explanatory content preserves more
of what later decisions need per unit of total cost than competing retained
forms. [Structured shifts](../retained-theories-may-improve-sample-efficiency.md)
may favor reusable explanations when relevant relations survive while other
features change. Mistaken abstractions can instead cause negative transfer.
An aggregate may preserve the information needed for a task exactly; derived
state need not be lossy or smaller than its inputs. No general superiority
follows from calling theories compression.

Records remain evidence from which a theory can be challenged or rebuilt;
[retaining episode evidence](../retaining-episode-evidence-keeps-a-distilled-rule-open-to.md)
serves that purpose. Retaining more records and more theory also adds
retrieval, interpretation, maintenance, and consistency costs.

## Separate the two reconstruction comparisons

The storage container does not decide whether a system performs
[conjectural learning](../definitions/conjectural-learning.md).
Indexed traces can expose theories and their criticisms as retained,
addressable knowledge. A theory can also be reconstructed from criticism
without retaining the assembled theory. Either can qualify when criticism
improves capacity for future action.

Two retention comparisons therefore ask different questions:

- **Assembled theory and testing record versus retained criticisms.** This
  asks what keeping the assembled theory buys over reconstructing it from
  work already done. The reconstruction may itself be conjectural learning.
- **Assembled theory and testing record versus inputs and outcomes only.**
  This asks what retaining the work of conjecture and criticism buys over
  doing that work again. The records in the second arrangement do not
  contain formulated criticisms; its active machinery may still formulate
  and use them. A storage contrast cannot establish their internal absence.

Full reasoning traces may contain theories and criticism. Treating all
traces as raw observations would change what the comparison varies. Generic
or learned retrieval, reconstruction, and direct use can be combined in any
arrangement if their roles and costs are declared. The useful contrast is
the work retained and consumed, not whether it sits in a file called a
theory. Supplying the same model weights also does not hold processing fixed
when the inputs change.

Records with a maintained retrieval index are a stronger rival than records
with generic retrieval alone. After the first comparison, a further arm
should test that rival while declaring which content the records retain and
counting index construction and maintenance. This is a deferred comparison,
not an addition to the currently commissioned protocol.

Comparisons should count initial construction, retrieval, reconstruction,
testing, and maintenance, and report cost at comparable quality or quality
under matched budgets. Content interventions can strengthen attribution to
what a theory says. A result establishes only
[the contrast actually run](../an-experiment-identifies-only-the-contrast-it-actually-runs.md),
not a universal boundary between learning and nonlearning arrangements.

## Open questions

- Can effective context be measured reliably enough for this vocabulary to
  improve comparisons over direct descriptions of tasks and supplied text?
- Which decisions require combining evidence across contexts rather than
  retrieving a small sufficient subset?
- When is retaining an assembled theory cheaper than reconstructing it from
  criticism at comparable quality, including maintenance and stale-theory
  failures?
- Can retained criticisms be kept usefully distinct from a compressed or
  partially assembled theory in an actual implementation?
- Which costs or failures should cause a system to revise, reconstruct, or
  combine the two? Neither strategy is a membership condition of learning.
- When does a learned index itself expose an addressable theory, rather than
  only route access to records? Retention or editability alone does not decide.
- How should replay be compared when stochastic choices cannot be reproduced
  and reconstruction yields a distribution of states rather than the same state?
- When a prior theory is supplied, what evidence distinguishes revision that
  uses it from independent reconstruction? Output alone may not distinguish
  them; a decision-point citation and an intervention removing the prior
  theory are candidate checks.

---

Relevant Notes:

- [Conjectural learning](../definitions/conjectural-learning.md) — defined-in: learning attribution is distinct from the retained-state arrangement
- [Addressable theory](../definitions/addressable-theory.md) — defined-in: the optional structural property supporting targeted criticism
- [Commonplace studies conjectural learning through retained theories](../commonplace-studies-conjectural-learning-through-retained-theories.md) — see-also: the independently stated efficiency conjecture
- [Retaining episode evidence keeps a distilled rule open to re-examination](../retaining-episode-evidence-keeps-a-distilled-rule-open-to.md) — grounds: records remain evidence behind retained abstractions
