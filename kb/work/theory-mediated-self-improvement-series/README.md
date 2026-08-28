# Workshop: theory-mediated self-improvement article series

**Posed by:** the operator, 2026-08-27, as author of the article series.

## Goal

The workshop's product is the article series. Its main article states the
research program; the other articles argue the program's parts. Reconstruct
the series around that program without treating four review-defeated drafts
as foundations.

The program asks whether a mixed system of retained natural-language theory,
language-model interpretation, symbolic procedures and code, and operational
evidence can progressively close the set of programming decisions that a
person must still supply — for software construction and for its own
theory-mediated improvement.

Progress has a practical lower bound. A programming tool moves in the desired
direction when, for a nontrivial task class, it increases the accepted
outcomes obtainable from a fixed amount of total human programming effort,
counting configuration, review, recovery, and repair. A bounded mechanism
still counts: a formatter can remove formatting work even though formatting
alone can never cover the programmer's role. Its ceiling limits that
mechanism, not the progress already made. Better performance inside a fixed
envelope — better results, more inputs, fewer failures, fewer resources —
improves capability or yield; only envelope expansion reduces the kinds of
decisions that remain human.

Transfer is adversely selective. Each mechanism takes the decisions it can
warrant — represented inputs, a settled criterion, a result an independent
oracle can check — and leaves a residue that is harder to warrant per
decision
([warranted transfer leaves people the hardest-to-warrant decisions](../../notes/warranted-transfer-leaves-people-the-hardest-to-warrant-decisions.md)).
Envelopes therefore do not stack toward closure. The work must classify the
residual human decisions on a named path by the reason each stayed human —
unrepresented premise, unsettled criterion, no independent check, horizon
cut, priced out — and show which part of the mixed architecture is the
candidate mechanism for each class and what that part cannot reach. This is
why the architecture is mixed: retained theory supplies representation and
settlement, the interpreter applies settlements across unformalized cases,
oracles supply verification, and the symbolic runtime supplies horizon.

Two strong milestones follow, and they meet at the evaluator. Scoped
computational closure holds when, for a declared path and horizon, every
required decision is represented and executable inside the automatic system
with no hidden cut. The remote-programmer benchmark holds when the system
performs at least as well as a competent remote programmer given the same
brief, repository, digital tools, permissions, and feedback; its client cut is
a declared export of demand choice and acceptance, not closure over them.
Both milestones are decided by whether the system can warrant its own hardest
decisions. Neither is a prerequisite for present usefulness or a final upper
limit. The workshop must map no-op loops, narrow optimizers, weak evaluators,
and exported human decisions rather than letting them satisfy a milestone by
definition. The present Commonplace arrangement is a human-inclusive
bootstrap: evidence about an allocation, not the endpoint.

The theory this program builds is retained natural-language theory of the
kind the program studies, and it is consumed by the system it describes.
Classifying a path's residual human decisions by reason, and routing each
class to the architecture part that can move it, is a theory-building
function of the wiki: it helps operators decide where their own automation
should go next and what it cannot yet reach. Applied to Commonplace's own
transfer decisions, it supplies the mediation trace the earlier drafts
lacked — the same theory guides a change, the change's warrant record tests
the theory, and a misclassified row revises it. This is a tool-usefulness
claim and a traceability claim; it is not a closure claim, and it is earned
by a recorded use, not by stating it.

Read the same way, the research program is a build plan. The classification
orders what to build next — for an LLM wiki first, and, because the theory is
stated over decisions rather than over any one task, for an LLM coding agent
or an LLM agent generally. Whether following the plan yields the most
powerful system of its kind is the conjecture the program tests; power is an
outcome to measure, not a consequence of the plan's shape.

The strong milestones are not the only payoff. Commonplace already serves its
operators as a theory-building tool. The same substrate can grow to cover
other LLM-wiki functions, and each warranted transfer can make the tool more
useful before the closed-system goal is reached — or less useful, if it leaves
people only the decisions they are worst placed to make.

### Outputs

- **Theory** — claims with reach, in `kb/notes/` (the self-improving-systems
  cluster).
- **Instrument** — one procedure in `kb/instructions/` that classifies a
  path's residual human decisions and routes each class to a mechanism,
  resting on the notes; repo-local first, promoted to a `cp-skill-*` after a
  first use outside this checkout.
- **Articles** — the outward distillation, paper-from-notes, led by the
  research-program article.

## Author direction fixed by the operator

- Naur supplies the starting requirement: coherent construction and
  modification require a program-specific theory. The accepted Naur article
  reopens computational possession of that theory without claiming that any
  current composite has passed Naur's tests.
- The target is not natural-language theory plus model weights alone. Exact or
  long-horizon operations may require symbolic code because a scheduler can
  execute an implemented transition faithfully where prompt execution remains
  exposed to underspecification, indeterminism, and bias.
- Code exactness is not correctness. The theory, language model, symbolic
  runtime, and evidence oracles must remain in one revisable arrangement.
- Commonplace is already useful as a human–agent theory-building tool. That
  practical role does not establish independent computational theory
  possession or computational closure.
- Any programming-tool change that produces more accepted work from the same
  total human programming effort, or the same work from less effort, is
  practical progress toward the broad direction. It need not demonstrate a
  complete route to the strong benchmark.
- Each mechanism has an automation envelope. Reaching its ceiling leaves the
  other residual programming decisions visible; it does not retroactively make
  the bounded transfer unreal. Envelopes do not stack toward closure: the
  residue is adversely selected, and the next transfer is decided at the
  evaluator.
- The program's theory is also the KB's instrument and a build plan. Both
  readings are earned by recorded use; neither is a closure or power claim.
- Better performance inside a fixed envelope also counts, through outcome
  quality, reliability, coverage, latency, or resource efficiency. It is not
  the same change as transferring another kind of responsibility.
- Competent remote-programmer performance is a strong capability benchmark,
  not the definition of all useful progress or the final limit of the system.
- The substrate may support other LLM-wiki operations such as grounding,
  routing, retrieval, synthesis, criticism, revision, validation, and
  publication. This list is a working scope, not a completeness claim.
- Commonplace is evidence about a bootstrap allocation, not evidence that the
  endpoint has been reached.
- Tool usefulness, computational autonomy, warrant, and system power are
  separate dimensions. The Bitter Lesson motivates a possible power gain; it
  does not make power a consequence of autonomy.

## Evaluation boundary

The target claim is always relative to a named revision path, objective,
system boundary, and horizon. The automatic side may include model calls,
retained prose, code, schedulers, validators, tests, state, and evidence
interfaces. The environment may supply observations and tasks. Closure means
that no indispensable decision on the named path crosses an unrepresented
human cut; it does not mean independence from infrastructure, observations, or
a previously supplied objective.

The practical tool claim is evaluated at the human–agent boundary instead.
Does the arrangement help its operators form, criticize, retain, retrieve,
apply, and revise theories or perform another declared wiki function? Hold the
task class and acceptance threshold fixed, and count configuration, review,
recovery, and repair rather than hiding them outside the effort measure. A
change is forward when it increases accepted outcomes for the same total human
programming effort or reduces that effort for the same outcomes without an
unacceptable loss of warrant. Client direction and feedback are held apart
from programming decisions when the remote-programmer benchmark is used.

This comparison is a partial order, not proof that every improving method can
reach the benchmark. A formatter may eliminate one residual responsibility
and then stop. Further progress requires another mechanism or a composition
whose automation envelope covers more of the remaining work.

The workshop does not assume that every transition to the strong benchmark is
possible. Demonstrating or defeating those transitions is the experiment.

## Source handling

Only the two closing-ready articles have been copied as prose baselines under
[accepted](./accepted/README.md). Acceptance is local to their completed
passes, not a promise that they will remain unchanged.

The four other article bodies are inert source captures under
[rejected-drafts](./rejected-drafts/README.md). Rejection applies to each draft
as a publishable argument, not automatically to every claim it contains. No
agent should revise one of those files into a successor article. A claim can
leave quarantine only through an explicit entry in the
[incumbent ledger](./incumbent-ledger.md).

The earlier
[theory-mediated methodology workshop](../theory-mediated-methodology-article/README.md)
records how the drafts accumulated. It is historical input, not the place to
continue the series. It remains until its live decisions have been checked
against this workshop and then closes under the workshop contract.

## Working artifacts

- [Shared model](./shared-model.md) — the current architecture, bootstrap
  relation, practical payoff, closure condition, and progress dimensions.
- [Closure–capability map](./closure-capability-map.md) — comparison coordinates,
  degenerate closure patterns, provisional system regions, and a candidate
  adequacy gate.
- [Article roles](./article-roles.md) — argumentative jobs and their dependency
  order; these do not promise that every rejected title survives.
- [Incumbent ledger](./incumbent-ledger.md) — source identities, review
  constraints, and claim-by-claim transfer decisions.
- [Accepted baselines](./accepted/README.md) — the only inherited prose that
  may seed a successor directly.
- [Rejected draft captures](./rejected-drafts/README.md) — read-only evidence
  for claim recovery.

## What closes this workshop

The workshop closes when:

1. the shared model states the target architecture, present bootstrap,
   practical tool payoff, and progress comparison precisely enough for the
   articles to use;
2. the closure–capability map has been exercised on a few contrasting
   systems: their human cut classified by reason, with the degenerate
   patterns checked against the verification row;
3. every material claim in the four rejected drafts has a recorded
   disposition;
4. accepted successor articles have been reconstructed and reconciled without
   depending on a quarantined draft;
5. the four latest full-pass findings and all affected article links have been
   resolved;
6. the earlier workshop has been consumed; and
7. the durable articles and any supporting notes validate under their target
   contracts;
8. the classify-and-route instrument exists and has been applied once to a
   Commonplace path, with the classification, the chosen transfer, and its
   outcome recorded; and
9. the bootstrap article cites that record as its mediation trace.

At closure, durable results move to the library and this directory is deleted.
