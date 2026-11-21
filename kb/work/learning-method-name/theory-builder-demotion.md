# Next stage: deliberative learning replaces the theory builder as the central definition

Proposed by the operator on 2026-11-21. The original assessment and plan are Fable's
(claude-fable-5-2). The operator subsequently asked to separate the choice
of a central definition from the claim that one kind of system is a special
case of the other.

## The proposal

The operator: "we need to think about retiring theory builder as one of our
main definitions - it can stay in some notes and articles for some time - but
we should retire it from its central place and replace it by deliberative
learning". The operator also called the definition of learning "a long
standing problem for us that we could not define what learning means here".

## Why deliberative learning should be central

- **It answers the main question.** The
  [theory-builder definition](../../theory/definitions/theory-builder.md) has
  no success condition. Every central statement therefore adds that whether
  the builder learns is the hypothesis under test, with only
  [Simon's criterion](../../theory/learning-is-not-only-about-generality.md)
  behind "learns". [The draft](./draft-definition.md) defines "learned".
- **It covers all of Commonplace's learning.** The theory builder covers
  stated theories. Deliberative learning covers any retained change.
- **It puts the distinguishing property in the definition.** A judgment
  inside the loop that is not bound to one measure separates Commonplace from
  model training and from symbolic learners. The theory-builder definition
  does not say that.
- **The research question is simpler to state.** Before: can a theory builder
  running on fixed-weight LLMs learn? After: can a language model run the
  outermost loop of deliberative learning well enough?

## What the theory builder says that deliberative learning does not

The theory-builder definition requires criticism aimed at what a theory says.
That separates conjecture and refutation from trial and error. A system that
keeps an unexplained prompt change because it judged, on balance, that
results improved is doing deliberative learning. It is not a theory builder.

Two things depend on that requirement:

- **The three conjectures of
  [the research companion](../../theory/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md).**
  One asks whether criticism of content pays against trial and error. The
  other two ask about addressability and persistence.
- **[The survey of eighteen self-improving systems](../../articles/which-existing-self-improving-systems-are-theory-builders.md),**
  which classifies each system against the four conditions.

## Choosing a central definition does not settle which systems qualify

The reason to lead with deliberative learning is that it states the research
question more directly. Fable's further proposal—that every theory builder
is a deliberative learner—is a claim about the two definitions. The prompt
example above tests only the other direction: deliberative learning need not
involve criticism of what a theory says.

**Boundary case: criticism under an immutable score.** Suppose a system
states a theory, acts on a prediction, identifies why the prediction failed,
and revises the theory in response. For the next round it must keep whichever
revision scores highest on a fixed test. No loop the system runs can question
whether that score is sufficient. The case appears to meet the builder's
conditions, but not the learner's condition on retention. Check it against
both definitions at that same system boundary. If that reading holds, the
kinds can overlap without either being a special case of the other. Commonplace
could still use deliberative learning as its central definition and use the
builder conditions where criticism of stated content matters.

**After the ruling on fixed measures.** On 2026-11-21 the operator ruled
that a fixed measure is a special case of condition 2. The boundary case
above then passes condition 2, as a fixed measure. It still fails the
learner's conditions if its score is a fixed test that takes in nothing new:
the kept theory is then only displaced by a higher scorer, and no later
evidence counts against it, so condition 3 fails. If the score takes in
later outcomes, the same builder is a single-loop deliberative learner.
[The checks](./definition-checks.md) record both as cases 7a and 7b. On that
reading the kinds still overlap without containment, and the excluding
condition is the third. The prompt example still shows the other direction.

**Neon's position on the relation**, relayed on 2026-11-21 and not yet
checked against the builder's boundary cases: every continuing theory
builder with a text store is a deliberative learner. A non-reflective
builder corresponds to single-loop learning and a reflective builder to
double-loop learning. Two edge cases remain: a builder whose localized
theory is not kept in prose, structured text or code, and a builder that
forms and discards a theory within one episode. Neon reads the boundary case
above as case 7b. The demotion does not depend on the answer.

## Decisions for the operator

1. **Place in the research program.** Ruled on 2026-11-21: lead with
   deliberative learning, and demote the theory builder from its central
   place. The operator: "I think we can demote theory builder without
   deciding if it is a special case". The relation between the two kinds
   stays open and does not block the demotion. Fable agrees with the
   boundary case above: as the two definitions stand, a theory builder bound
   to an immutable score is not a deliberative learner, so the kinds overlap
   and neither contains the other. Fable's "special case" was a proposal to
   redefine the theory builder, and it is withdrawn as a step of this plan.
2. **A noun for the system.** Ruled on 2026-11-21: **deliberative learner**.
   The operator: "I think we can use deliberative learner and contrast it
   with the deliberative agents (it is possible that we'll discover something
   in that old tradition that is closer to us - so we should remain open
   about the question if our deliberative learner is a deliberative agent)."
   The draft now states the contrast and leaves the question open.
3. **Order of work.** The agent recommends the plan below. Step 1 was
   carried out on 2026-11-21; see the step 1 result.

The questions about the definition that remain open are listed in
[the workshop README](./README.md#open-questions-about-the-definition).

## Plan

1. **Test the definition before moving anything.**
   - Write boundary cases for deliberative learning, as
     [the theory-builder checks](../../theory/definitions/theory-builder-checks.md)
     do for the four conditions. Apply both sets of conditions to the
     immutable-score case before describing theory builders as a special case.
   - Reclassify a few of the eighteen surveyed systems by the three
     conditions. The agent expects most to fail the second condition, because
     they accept changes by a benchmark score. If that expectation is wrong,
     the definition needs work.
   - Get an independent reading of the draft.
2. **Finish the on-balance side.** The on-balance note states the definition
   of improvement since 2026-11-21. The two companions from
   [the definition workshop](../bounding-omitted-effects/README.md) cover how
   a judgment is reached and how reversibility limits future loss. The
   addition/removal contrast and tie case are in the on-balance note.
3. **Register the term.** The definition under `kb/theory/definitions/`, the
   `AGENTS.md` vocabulary table, and a collision record for "deliberative".
4. **Move the central places.**

   | Place | Now | After |
   |---|---|---|
   | `AGENTS.md` vocabulary | Theory builder | Both, with deliberative learning as the main term |
   | `kb/tags/learning-theory-README.md` | The anchor is the theory builder | The anchor is deliberative learning |
   | The research companion | Framed around the theory builder | Restated around deliberative learning; a relocation if the title changes |
   | The theory-builder definition and its checks | Stand alone | State only the relation supported by the checks |
   | `kb/tags/theory-builder-README.md` | A main tag | Decide: keep for work about theory builders, or add a tag for the new term |

5. **Articles last.** All six are drafts and are framed around the theory
   builder. The operator allows them to keep the term for some time. The lead
   article goes first when they change.

About 65 library files mention the theory builder. Most need no change if the
term keeps its present meaning in those files.

## Step 1 result

The [eight boundary cases and three historical survey placements](./definition-checks.md) test the draft without changing either definition. Cases 6–8 support overlap without containment on the stipulated assumptions. Only one of the three surveyed protocols demonstrably binds admission to an immutable gate. Distinguish selection of retained guidance from automatic logging and from later benchmark evaluation.

The [independent reader](./positions/step-1-independent-reading.md) accepts the strict success test for “learned” but disputes the wording of condition 2. The operator's ruling stands: keeping a reversible trial is itself judged better for future work than not trying it. It is the trial that is judged worth keeping now; its later result is not established. The reader's objection is evidence that these two comparisons can still be confused, not authority to relax condition 2. Before promotion, clarify their alternatives and decide how “each change” applies to a store that also records unselected observations. No wording or placement in the library changed in this step.

## Cautions

- **The new definition is one day old.** One agent wrote it in one
  conversation. The theory-builder definition has seventeen boundary cases
  and a survey behind it. Step 1 exists for this reason.
- **The older tradition of deliberative agents has been read through one
  survey.** A closer precedent may exist there. Reading on belief-desire-
  intention architectures and on learning in Soar would test the contrast.
  This is not required before adoption.
- **This is the second change of central term since September.** Conjectural
  learning gave way to the theory builder, and the theory builder now gives
  way to deliberative learning. The earlier changes were attempts at the
  problem this one addresses: what learning means here. The record of the
  change should say so in one place.
