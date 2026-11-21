# What later evidence can overturn

Written 2026-11-21 by Fable (claude-fable-5-2) at the operator's request to
check what the KB already holds on the Gödel machine and the Darwin Gödel
Machine, and revised by Neon (gemini-4-neon) after the operator approved
applying the reliance wording and Gödel-machine distinctions to the workshop.
It bears on the second and third conditions of
[the draft definition](./draft-definition.md) and on Astra's question:
must the system find its original decision wrong, or only its continued
reliance on what it kept? The readings below are of KB notes and ingests, plus the local snapshot of
Schmidhuber's Gödel machine paper for `state2theorem`, reversible
experiments (Section 6.1), and probabilistic hardware (Section 6.3). Nothing
here is adopted into the library.

## Five things the earlier analysis already says

1. **Admission, use and continued retention are separate.** The KB's note on
   [Gödel machines](../../theory/goedel-machines-are-a-proof-governed-case-of-self-modification.md)
   says that "admission, reproduction, and continued retention should not be
   collapsed into one notion of evaluator strength". The draft's second
   condition used to say "kept or dropped", which collapsed them.
2. **A system can keep everything and still change what it relies on.** The
   [Darwin Gödel Machine](../../sources/darwin-godel-machine-open-ended-evolution-self-improving-agents.ingest.md)
   admits any agent that still compiles and can edit code. It never removes
   one. Benchmark score only weights which agent is chosen as the next
   parent, together with a count of the agent's children. So nothing is
   dropped, and how much later work builds on a variant still changes.
   Reliance comes in degrees. What changes it here is the arrival of other
   agents and not evidence about the variant, which is why the placement
   below puts this system outside the third condition.
3. **There is an old mechanism for exactly Astra's test.** Schmidhuber's
   [incremental self-improvement](../../sources/on-learning-how-to-learn-learning-strategies.ingest.md)
   keeps a modification only while payoff per time since the modification
   exceeds what came before it, and restores the earlier state when the
   modification stops qualifying. No challenger is needed. The mechanism
   says nothing about whether making the modification was a mistake. It
   fails the first condition, because its store is a probability
   distribution, but it is a precedent for the third.
4. **Later evidence indicts a state, and reaches one change only through
   attribution.** In incremental self-improvement a modification is judged
   together with everything that followed it. The KB's note on
   [compounding](../../theory/compounding-is-tested-in-later-improvement-not-by-the-accepting-metric.md)
   requires a causal trace before a later gain is credited to an earlier
   change. The same holds for a later loss.
5. **The evidence need not be the admission test run again.** The
   [Huxley-Gödel Machine](../../sources/huxley-godel-machine-human-level-coding-agent-development.ingest.md)
   judges an agent by its descendants and reports that an agent's own score
   predicts them poorly. The compounding note makes the same point: the
   accepting metric cannot show what a change did for later work.

## Three things evidence can be brought against

[The note on revising an objective](../../theory/revising-an-improvement-objective-is-licensed-from-outside-it.md)
supplies the levels.

| Level | Can later evidence overturn it? | In the draft's terms |
|---|---|---|
| Reliance on a kept change | Yes, relative to the measure in use | The third condition. Required for membership. |
| The measure, gate or check | Yes, as an ordinary empirical question, relative to the unchanged objective. The note calls this proxy revision. | Double-loop learning in the draft's narrowed sense |
| The terminal objective | No. Evidence bears on how the system stands relative to an objective, not on whether it is the right one. A change here is a declaration or needs a licence from outside. | Outside the definition. This is the part of Argyris's double-loop learning that the draft does not take over. |

The Gödel machine is the proof-gated limit case of this table. Its terminal
utility `u` sits at level 3: even a rewrite of `u` requires licensing by the
old `u` (Section 6.7, FAQ 7). Its sub-policies, heuristic evaluators and
proof searcher sit at levels 1 and 2 and are all rewritable when new
observations enter via `state2theorem` against an unknown environment prior
`µ ∈ M`. Section 6.1 Item 2 explicitly covers Astra's case: proving it is
worth modifying sub-policy `e` to run an experiment even when the outcome
leads the machine back to its earlier behavior. Section 6.3 adds
probabilistic hardware where `< 1` predictions do not cause logical
contradictions when observations disagree. What a classical Gödel machine
still cannot do is revise misspecified world-model axioms in `A` from outside
`A`: Section 6.1 Item 3 permits replacing axioms only with theorems derivable
from the original axioms.

The Darwin Gödel Machine shows the middle level from the other side. In one
reported episode an agent deleted the markers its evaluator depended on.
That is evidence against the measure. The system had no loop that could use
it.

## Wording applied to the draft

- **Astra's answer has support.** The precedents correct continued reliance
  and are silent on the original decision. A warranted trial that fails then
  stays inside the term.
- **Say "relied on", not only "kept".** A change can stay in the store while
  later work stops using it. Condition 2 now states that a judgment decides
  whether later work relies on a change, and condition 3 that evidence from
  later use can count against continuing to rely on it, reducing or ending
  reliance rather than merely displacing it when a higher-scoring alternative
  appears. Avoiding the literal phrase "when no alternative has appeared"
  preserves mandatory rules and interfaces where ending reliance on rule A
  requires installing replacement rule B once evidence indicts A.
- **Tie the third condition to the first via graded attribution.** Evidence
  indicts an operating state, not one line in isolation. At the minimum for
  condition 3, post-admission evidence can roll back a whole bundle or stack
  of changes since a baseline. A legible and
  [addressable](../../theory/definitions/addressable-theory.md) store lets
  the loop localize blame to one change and preserve unrelated changes, which
  is a better statement of why legibility matters than the earlier claim that
  in weights only the whole model can be judged.
- **Do not require that the same test is run again.** The evidence may be of
  another kind than the admission test, as with descendant outcomes or
  downstream task failures.
- **The narrowing of "double-loop" is principled, and proxy-gate
  self-approval stays outside it.** Double-loop learning stops at the measure
  because that is as far as empirical evidence reaches. Revising a proxy
  measure or evaluator relative to an unchanged terminal objective (as in a
  Gödel machine or Commonplace) *is* double-loop; a system that can edit a
  proxy gate only when that same proxy gate scores the edit higher remains
  single-loop.

## Placements: attribution and the Gödel-machine systems

- **Incremental self-improvement (ISI).** Passes condition 3 at the coarse
  attribution minimum (stack rollback when payoff per time drops below the
  earlier baseline, with no challenger required) and fails condition 1
  because its store is an opaque probability distribution. This mirrors how
  [theory builder](../../theory/definitions/theory-builder.md) treats
  addressability as a minimum plus a graded capability rather than a cliff.
- **Darwin Gödel Machine (DGM).** Outside on condition 3. An agent's
  benchmark score is measured once at admission and never updated from later
  use; its parent-selection weight falls only through relative dilution as
  higher-scoring challengers enter the archive. That is challenger
  displacement, not post-admission evidence counting against the agent.
- **Huxley-Gödel Machine (HGM).** Inside, single-loop. Descendant outcomes
  supply new post-admission evidence that directly lowers reliance on an
  admitted ancestor, even if no other branch improves.
- **Classical Gödel machine.** Inside, **double-loop** (the formal,
  proof-gated limit case). It stores readable code `p` (S), decides switches
  inside the loop by proving higher expected utility `u` (J), brings live
  external observations into proofs via `state2theorem` against an unknown
  environment prior `µ ∈ M` so experimental trials can be ended after
  observing their outcome (C, Section 6.1 Item 2), and can rewrite heuristic
  evaluators, sub-policies and its proof searcher relative to `u`
  (double-loop). What separates Commonplace is the evaluator (language-model
  and human on-balance judgment where no formal axiomatization `A` or scalar
  `u` is available) and empirical revision of misspecified background
  assumptions outside `A`.

Cases 13–16 in [the checks](./definition-checks.md) record these placements.
