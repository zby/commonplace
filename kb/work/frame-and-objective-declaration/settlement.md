# Settlement record

Status values: `open`, `agreed`, `ruled` (operator), `moot` (no edit depends on
it), `deferred` (with trigger). Update a row with the date and the basis.
Questions are in the [framing](./README.md#decision-points).

How much this record can carry: positions A, C and D were written into the
workshop by position B's author from comments the operator relayed. B's author
also wrote the concessions and this table. Convergence here means "B accepted
an argument made in a relayed comment". No author of A, C or D has confirmed
their file. Agreement between agents is not evidence under the framing.

| # | Status | Where positions stand | Basis |
|---|---|---|---|
| D1 | moot (proposed 2026-11-20) | A: boundary shift. B, D: not a shift; L17's items are a subset of the frame's computational components. C: no view. | No edit depends on it. |
| D2 | open; B, C, D converge | A: restate in body. B, C: cite at first dependent claim; state locally what was observed. D: the frame note already says cite; no new rule. | |
| D3 | moot (proposed 2026-11-20) | A: human inclusion is the cause. B, D: any boundary owes the same. C: no view. | No edit depends on it. |
| D4 | reframed by operator direction 2026-11-20; the accounting below is no longer a program-wide ruling, see the direction section | Full lifecycle (construction, operation, repair, maintenance) over a stated period; human judgment spent, reported by supplier; reader cost counts in the numerator, not the denominator; model strength reported. A: no view. | C's argument against a boundary-tied denominator; D's argument that "requires" is not observable. |
| D5 + D7 | open, disputed | D: one question; put the objective and its accounting in the frame note, or rename what that note declares. B: one question; the frame note states that horizon and improvement objective are per attribution, and the program objective stays in the instrument note. C: instrument note owns the objective. A: no view. | B's reason: the tag-readme classification is read against ADR 026's criterion, not the program objective. |
| D6 | open; B, C, D converge | No frame-note addition unless the cold-reader check finds an overclaim. Observations owe nothing; effect claims address the rivals that could change the conclusion. A: no view. | |
| D8 | open; B, C, D converge | No writing or review rule unless the check finds repeated overclaims. A: no view. | |

## Operator direction, 2026-11-20

Stated by the operator after reading the software-house investigation. Recorded
as a direction, not yet as a ruling on any row.

> We can measure progress only after we define some application area narrower
> than [knowledge work in general]. We can only measure progress on the margin:
> by showing that in a particular area it has improved and that it is
> improbable that the change made regression in some other areas.

The sentence was cut off after "narrower than"; the bracketed words are the
recorder's reading.

What it changes, as the recorder reads it:

- **D4 is reframed.** There is no program-wide measure whose accounting needs
  one ruling. The objective sentence states a direction. Each progress claim
  declares its own area, the dimension that improved, the reference state, the
  resources counted and the argument against regression elsewhere.
- **D5 gets smaller.** The owner of the objective no longer holds an accounting
  block. It holds the direction and one statement that measurement is marginal
  and area-indexed.
- **The form already exists in the library.**
  [A better-factory claim](../../theory/a-better-factory-claim-compares-operative-states.md)
  compares predecessor and successor by a declared gain plus non-regression on
  prior scope. The direction differs in one respect: non-regression outside the
  area is argued to be improbable, not checked against thresholds. That answers
  the note's open question about open-ended families by giving up the check.
- **What the direction costs** (corrected by the operator, 2026-11-20). The
  recorder first wrote that local gains never support "Commonplace got better".
  The operator's correction: a gain in one area with no regression elsewhere
  does support it. The limit is on the evidence. No regression cannot be shown
  against every possible task; it can only be argued that non-trivial
  regressions are improbable.

The first wording of the claim was:

> Commonplace got better when it improved in a declared area and non-trivial
> regressions elsewhere are improbable.

The recorder first described this as a dominance claim over a partial order.
The operator's second correction, 2026-11-20: a partial order is the wrong
abstraction. What is needed is a partial order that approximates a total
order.

The recorder's reading of that correction:

- **There are two relations, not one.** The total order is "better overall for
  the work Commonplace is for". It is not specified and not directly
  observable. The partial order is what the evidence supports. A marginal
  claim is a conjecture about the total order, made from the partial one.
- **The objective names the total order.** "More useful and better-warranted
  knowledge work per unit of human judgment" is then neither a measure nor a
  mere direction. It says what the comparisons are about.
- **A claim can be wrong.** Under a bare partial order, two states that the
  evidence does not rank are simply unranked. Under this reading one of them
  is better and the evidence has not shown which. A recorded improvement can
  later be refuted by a regression that outweighs it.
- **"Non-trivial" gets its meaning from the gain.** A regression is
  non-trivial when it is large enough to reverse the comparison. The claim
  form is therefore "the gain outweighs the probable losses", not "no losses".
- **The approximation is judged two ways.** Soundness: how often a recorded
  improvement is a real one. Coverage: how many comparisons the evidence can
  make at all. Stricter regression arguments raise the first and lower the
  second.

What the reading assumes, and its limits:

- **Gains and losses in different areas can be weighed, at least coarsely.**
  That is a value judgment. The software-house investigation found that the
  house definition avoids such judgments by leaving them with users. Here they
  stay outside in the same way: the total order is the users' and operator's
  preference between whole states, not something the system defines. Changing
  it is an objective change.
- **Whether one total order exists is itself an assumption.** The library says
  the profile of coverage, dynamics, governance and allocation "does not select
  an order" and that a declared objective is what can. The reading relies on
  the declared objective to do that.
- **The uncertainty still accumulates** over a sequence of changes, unless
  prior scope is re-checked.
- **"Elsewhere" still needs a task population.** The candidate is tasks that
  arise, weighted by how often and how much they matter.

Confirmed by the operator, 2026-11-20: the weighing of gains against losses
stays with the operator and users, and the key property is that the
approximation can be judged.

**Later clarification: “improbable” is not the test.** The operator wants the
reasoning behind an expected-value judgment without a formula. Ask whether
the change is better on balance: weigh the gain against both the likelihood
and the consequence of losses. Do not discard a serious loss just because it
seems unlikely.

The operator's routing example sharpens the distinction. A line in `AGENTS.md`
can help agents that need those instructions. Prompts that do not need them
still load the line. The first reading assumed that a small addition meant a
trivial cost. The operator pointed out that even one line could push a task
past its effective context limit. For that task the loss could be a failed
answer and rework. This is a mechanism to investigate, not a recorded failure.

The practical question is which tasks benefit and how often important tasks
are close enough to that limit for the change to hurt. Neither a probability
nor an exact threshold is required. If the available evidence cannot support
the trade-off, report the local gain and leave the overall judgment open.
Revisit it if the table grows or the mix of tasks changes.

Open under the direction: what counts as an acceptable regression argument.
Candidates are that the change is not on the causal path of other areas,
sampled checks on prior scope, and reversibility.

## Common ground

All positions hold that the confounds A named are real and that the instrument
note should not become a boundary-theory note.

## Not yet done

The open-question cold-reader check on the instrument note. D predicts no
overclaim, citing the disclaimers at L21, L39, L47 and L55. Nobody has run it.
