# Naming the learning method

Posed 2026-11-21 by the operator. The framing below was written by an agent
(claude-fable-5-2) from one conversation with the operator. The goal and the
operator's statements are the operator's. The options and the recommendation
are the agent's and await adoption.

## Goal

Decide what Commonplace calls the method by which a theory builder acquires
its theories. The operator's premise is that an on-balance judgment supplies
the improvement function previously missing from the account of learning.
When one version helps on many more tasks than it harms, a range of precise
weights can favor it. If the judgment holds across the weights plausible for
that work, we can recognize improvement without selecting an exact weight.
This gives us grounds to call the process learning. The name remains open.

The [definition workshop](../bounding-omitted-effects/README.md) has since
made that premise precise. Its result is carried into the decision points
[below](#state-after-the-definition-workshop-2026-11-21).

The operator's framing, in three statements from the conversation:

- "We have retired conjectural learning. What is its replacement? I think we
  need a name for the new training paradigm."
- "What is being learned is kind of what symbolic AI did, but we have a new
  method of doing it."
- On the objection that a name ending in "learning" asserts what the program
  is testing: "Didn't we just solve this problem?" The reference is to
  [on-balance judgments can guide improvement without a global measure](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md).

## Why the question is open now

**What the September retirement did.** Commit `21021fcc9` (2026-09-25) deleted
`kb/notes/definitions/conjectural-learning.md` and moved its consumers to the
redefined [theory builder](../../theory/definitions/theory-builder.md). The
workshop that did it, `theory-builder-from-popper`, gave this reason: the new
definition "has no success condition: whether a builder learns is the
hypothesis under test." Its framing is readable with
`git show 301114320^:kb/work/theory-builder-from-popper/README.md`.

**What the retirement left without a name.** The system has a registered name.
The method does not. The lead article calls the paradigm "theory building" in
one section. That term is in no vocabulary table and has no entry in the
[collision ledger](../../reference/vocabulary-collision-ledger.md).

**What changed.** The retired definition tied the term to improved capacity
for future action, in the sense of
[Simon's criterion](../../theory/learning-is-not-only-about-generality.md). At
the time, nobody could say what "improved" would be checked against without a
ranking of versions. The on-balance note gives that question a form: a named
gain in a declared area, and a judgment that losses elsewhere do not outweigh
it. The operator's position is that this removes the reason for keeping
"learning" out of the name.

## Three parts that the conversation separated

| Part | Current name | Status |
|---|---|---|
| What is learned: explicit theories that can be criticized | none needed | The operator holds that symbolic AI held knowledge in this form. |
| The system | theory builder | Registered in `AGENTS.md`. |
| The method by which theories are acquired | none | This workshop. |

The agent first placed the novelty in how theories are used: an LLM interprets
natural-language theories where symbolic AI needed a formal interpreter. The
operator corrected this. The novelty to be named is in how theories are
acquired.

## Decision points

- **N1 — Is "learning" acceptable in the name?** Two separate objections were
  mixed in the conversation and need separate answers.
  - *The definition objection.* A definition with a success condition makes
    membership depend on an outcome. A method name need not do that:
    reinforcement learning names a method, and a run that learns nothing is
    still reinforcement learning. The retired definition already had the
    distinction: "Exercising the process without improvement is an attempt to
    learn."
  - *The assessment objection.* "It learned" needed something to be checked
  against. The operator takes the on-balance note to answer this objection.
- **N2 — What would warrant saying that a particular theory builder learned?**
  Compare the builder's capacity for future work before and after it acquired
  a theory. For Commonplace, ask whether it can now produce more useful and
  better-warranted knowledge work for the human judgment spent. Give reasons
  for the judgment, including whose work improved and which losses could
  outweigh the gain. This comparison can remain open when the evidence is
  insufficient. The note's ADR 085 example illustrates why adopting a change
  alone cannot establish improvement.
- **N3 — Which name?** Candidates so far:
  - **Conjectural learning, restored.** It named this method. Eight redirects
    in `properdocs.yml` and the archived agentic-system reviews still carry
    the retired meaning.
  - **LLM-run conjecture and criticism.** Popper's name for the method, with a
    qualifier. It asserts no learning. It is accurate only for the autonomous
    end state; during the bootstrap people perform part of the method.
  - **Theory building.** Already used for the paradigm in the lead article. It
    is also Naur's term, for a theory that stays unformulated and with people.
  - **A new term.**

  Rejected in conversation, with reasons that were recalled and not checked:
  "theory-based learning", "Popperian learning", "critical learning",
  "theory revision", "neurosymbolic".
- **N4 — Does the success condition return to a definition?** If the method
  name asserts nothing, the theory-builder definition stays as it is and
  "learns" remains a separate claim. If the condition returns, say where: in a
  restored definition, or as a qualifier beside "reflective" and "autonomous".
- **N5 — The symbolic AI precedent.** The claim that symbolic AI learned the
  same kind of thing by other methods is the operator's. The agent's examples
  (hand-written rules, search in a formal hypothesis space, inductive logic
  programming) came from memory. The
  [precedents note](../../theory/theory-building-has-distinct-precedents.md)
  does not cover symbolic AI. If the name or its definition relies on the
  contrast, it needs sources.
- **N6 — Who performs the method.** In the bootstrap, people perform some of
  the conjecture and criticism. Decide whether the name covers the
  human-staffed case or only the automated one.

## State after the definition workshop, 2026-11-21

Written by the same agent after the operator settled the definition in
[the definition workshop](../bounding-omitted-effects/README.md). The first
paragraph reports that workshop. The consequences drawn for N1–N4 are the
agent's and await the operator.

**What was settled there.** A step is an improvement on balance when, for
every reasonable measure, the successor scores higher than the predecessor.
No measure is chosen. The verdict is improvement, not an improvement, or open
when reasonable measures disagree.

**Consequences for the decision points.**

- **N1, the assessment objection: answered.** "The builder learned" now has a
  stated meaning. A retained change is learning when every reasonable measure
  of the builder's capacity for future work favours the builder that has it.
  The objection that nothing could check the claim no longer holds. The
  definition objection was already answered by treating the name as a method
  name.
- **N2: the usual verdict for a new change is "open now, settled later".** The
  [refactoring case](../bounding-omitted-effects/further-cases.md#case-a--a-refactoring-the-whole-gain-lies-in-future-work)
  has the shape of a learning claim: the gain lies in work not yet done, so
  the evidence arrives in later episodes. A builder can therefore be running
  the method correctly while most of its recent changes are not yet shown to
  be learning.
- **N4: keep the success condition out of the method name and state it as a
  separate predicate.** The method name says what the builder does. "Learned"
  is the on-balance definition applied to one retained change, with its three
  verdicts. This keeps the September decision that membership does not
  establish learning, and still lets the name say "learning", as
  "reinforcement learning" does.
- **N3: one new argument for "conjectural".** The
  [irreversible-step case](../bounding-omitted-effects/further-cases.md#case-d--a-step-that-cannot-be-undone)
  found that a reversible step can be taken while its verdict is open. A
  tentative theory is such a step: it is held as revisable and can be dropped
  when criticism counts against it. "Conjectural" is Popper's word for exactly
  that status. So the word names the property that lets the method act before
  improvement is shown.

**The agent's recommendation.** Restore "conjectural learning" as the name of
the method, defined with no success condition. Define "learned" separately by
the on-balance definition. Leave the theory-builder definition as it is.

**Still for the operator.** The ruling on N1 and N3. N5, the symbolic AI
contrast, still has no source. N6, whether the name covers the human-staffed
bootstrap, is untouched.

## Operator rulings, 2026-11-21

**N3, the name: conjectural learning.** The operator first wrote "I think we
can use conjecture learning", then confirmed: "make it 'conjectural
learning'". The retired name is restored.

**N1.** Ruled with N3: the name contains "learning".

**N5, the comparison with symbolic AI.** The operator: the definition from the
definition workshop "would work for symbolic AI as a definition, but it might
be unworkable in practice."

The agent's reading of that statement, which the operator accepted as "part
of the answer":

- The definition of improvement does not mention the method. A step improves
  when every reasonable measure favours the successor. That applies to a
  symbolic system's retained rules as well as to a theory builder's theories.
  So what is learned, and what counts as having learned it, can be the same in
  both.
- Applying the definition takes judgment: which measures are reasonable for
  the purpose, and whether the plausible values fall on one side of the
  break-even point. A symbolic system could not make that judgment itself. It
  needed an evaluation function written down in advance, which is one measure
  chosen beforehand.
- So the new method differs in who can apply the success condition. The
  conjecture here is that an LLM can make on-balance judgments. That is the
  hypothesis of the
  [Python change judgment probe](../../reports/retained/python-change-judgment-probe-2026-11-20/README.md),
  and it is not established.

The operator then added a second difficulty, lower down. A symbolic system
would have trouble even evaluating the individual cases for a new Python
release. It could run tests, but it would need an enormous test array. People
use on-balance judgment inside individual cases too. The volume would
probably be prohibitive for a symbolic system, though the operator leaves open
whether it could be organized.

So judgment enters at two levels: choosing which measures are reasonable, and
scoring a single case under a measure.

This changes what N5 needs. The definition no longer has to claim that
symbolic AI learned the same things by other means. It needs one narrower
claim: that symbolic learning systems required a formally specified
evaluation. That claim still comes from memory and still needs a source.

**Draft.** [The draft definition](./draft-definition.md) defines conjectural
learning as a method with no success condition, and "learned" as the
on-balance predicate with three verdicts. It includes the comparison with
symbolic AI. No library file changes until the operator has read it.

## Evaluation boundary

While N1–N4 are open, do not edit these to adopt a name:

- `kb/theory/definitions/theory-builder.md` and its checks;
- `kb/theory/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md`;
- the articles under `kb/articles/`, including the lead article's "if a fully
  automated theory builder learns" framing;
- the vocabulary table in `AGENTS.md` and the collision ledger;
- the redirects in `properdocs.yml`.

Agreement between agents is not evidence here. The agent that wrote this
framing argued against "learning" in the name, then for it, within one
conversation. N2 should be read by an agent or person who did not take part.

## What closes the workshop

- The operator rules on N1 and N3.
- N2 has an answer that an independent reader accepts or a recorded
  disagreement.
- The chosen name is registered: a definition under `kb/theory/definitions/`,
  the `AGENTS.md` vocabulary table, and a collision-ledger entry where the
  term collides.
- The consumers are listed and either edited or deferred with a reason.
- If "conjectural learning" is restored, the record says that the September
  retirement is reversed and why, and the redirects are checked.

Then delete this directory and remove its entry from `kb/work/README.md`.

## Bookkeeping

Commits carry `Workshop: kb/work/learning-method-name`. Positions from other
agents go in `positions/`, one file each, marked with who wrote them and
whether the author confirmed the file.
