# Front-half draft

Draft prose for the new front half of the lead article. Working notes follow
the draft. Most links are omitted in the prose until the structure is
accepted; the notes list the source for each section.

---

# Conjectural Learning with Fixed Models *(title open — see notes)*

Most learning from mistakes follows one pattern. We act on an idea of how
things work. Something goes wrong. We ask what the idea got wrong, and we
change the idea, not only the one action.

In Popper's account, a research community runs the same loop at a larger
scale. Scientists propose theories, others try to refute them, and the
theories that survive guide the next experiments.

Current work puts language models into this loop. Agent memory systems have a
model write down a lesson after a failed task, and later runs read it.
Automated-science systems have models propose hypotheses, run experiments,
and revise. Whether such a system learns depends on what it keeps and on
whether criticism improves what it can do later.

We call the loop *conjectural learning*. This article says what counts as
learning of this kind, and then states two bets behind Commonplace, a
framework for knowledge bases operated by agents. First, computation can run
the whole loop, with no person proposing, criticizing, or revising theories
inside it. If so, the theories such a system keeps are a learned product, not
hand-built knowledge of the kind Rich Sutton's Bitter Lesson warns against.
Second, the loop is easier when the system writes code as well as prose. Both
bets are untested, and the article ends with what would show them wrong.

## A case

Consider a system that maintains a command-line tool. The project's full
test suite is slow, so the system runs it only on changes that can affect
the released program. A change that edits only files under `docs/` gets a
formatting check instead. The system retains a written account of why, in
two parts:

- **Rule.** A change needs the full test suite when the released program
  depends on a file the change edits.
- **Map.** Files under `docs/` are for human readers; the released program
  depends on none of them.

One day a change edits a page under `docs/help/`. The tool's `help` command
prints these pages, which are bundled into each release, and it expects each
page to start with a title line. The edit removed one. The change passes the
formatting check, and in the next release the `help` command fails. The full
suite includes a test that loads every help page, but by the account nothing
depended on the page, so the suite never ran.

The system investigates and formulates a criticism: `docs/` says where a
file is kept, not whether the program depends on it. It revises the Map:

- **Map, revised.** The released program depends on every file that its
  source code or build configuration references, wherever the file is kept.

The Rule survives.

What the system keeps from the failure matters. A record containing only
“this change, then a failed release” says which change failed. A lesson such
as “run the full suite on changes under `docs/help/`” prevents a repeat. The
criticism says why the decision was wrong. So the revised account also sends
changes to the other help pages through the full suite, and changes to the
README that the packaging step reads, though none of those files has caused a
failure.

This is a hypothetical example of the mechanism, not an experimental result.

## What counts as learning

Two conditions make the case an instance of conjectural learning.

First, a formulated theory guides decisions through what it says. If the Map
had said something different, the system would have run different checks.

Second, criticism of what the theory says improves what the system can do
later. The criticism of the Map changed which checks the system would choose
for files it had not yet seen. That improvement exists before the next such
change arrives; later decisions are evidence of it.

Writing a theory down does not meet these conditions, and neither does
changing one decision or applying a theory to new facts. If the project later
adds a tutorial that the tool also loads, the revised account already says
what to check. It guided a new decision, but no criticism was involved.

The learner is the whole system: its people, models, code, files, and
records. A research community meets both conditions. Its theories decide
which experiments are run, and criticism of them improves its later
predictions and tests. No single member has to hold the whole theory or
supply all the criticism. The members' brains change throughout, and we still
describe what the community learned by its theories. In the same way, the
definition does not depend on whether a model's weights change.

The definition covers less than Popper's schema, which he applied to all
life. An amoeba perishes with its mistaken expectations; scientists “try to
let [their false theories] die in their stead”. Conjectural learning names
only the second kind: theories formulated in language and criticized for
what they say. The definition note covers the boundary cases.

## The first bet: computation can run the whole loop

A research community shows that the loop works when people fill its roles:
proposing theories, deriving their consequences, criticizing them, revising
them, and maintaining the instruments. We call a continuing system that does
this work a *theory builder*, and these roles its internal roles. People who
supply tasks or judge the product are outside it.

The bet is that language models can fill every internal role, given a
sufficiently precise written description of the work. We call that
description a *methodology*.

We hold the models' weights fixed, so any improvement has to be carried by
what the builder keeps outside the models: theories, records, the
methodology, and code. This is a condition of our study, not of conjectural
learning.

We have two reasons for the bet. Models can follow a methodology written in
prose. Agent instructions and skills are already methodologies of this kind,
and models apply them to cases their authors did not list.

The methodology also does not have to be complete at the start. It is itself
a tentative theory. The builder uses it, failures expose its limits, and
criticism revises it, along with the machinery that applies it. People write
the first version, and the builder is meant to revise it.

The standing objection is that a scientist's skill is tacit and cannot be
written down. A model brings much unwritten competence from pretraining, and
what is still missing is a problem for the same loop. Whether that is enough
is what the bet risks.

## Why the methodology must be precise

A human scientist learns much of the craft by apprenticeship. A model with
fixed weights has the text it is given and what pretraining left in it. The
methodology carries the rest, and its precision matters for two reasons.

A vague term is read differently from one call to the next. After a failure,
the builder then cannot tell whether the theory was wrong or the model
misread it.

A methodology can also be criticized only where it says something definite
enough to be wrong. The builder can revise a part of its methodology only if
criticism can name that part.

Commonplace is a first version of such a methodology. This is why it spends
effort on definitions of *theory*, *criticism*, *tentative*, *addressable*,
and the internal roles, and why it holds to one term per concept. For a
model, a new word reads as a new thing.

This differs from an expert system, which encoded a domain's conclusions by
hand for a fixed interpreter. The methodology describes how to learn, not
what is true in any domain, and the builder can revise it. The vocabulary of
each new area is the builder's job. If a person has to supply it for every
area, the first bet has failed.

## The second bet: code as well as prose

The second bet is that the loop runs more cheaply and more reliably when the
builder also writes code that operates its knowledge. We do not claim that
prose alone could not carry the loop, only that this way is easier.

Science does the same. Much of its knowledge is kept in mathematical
notation, and a calculation in that notation is carried out by rule, much as
a computer runs code. It gives the same result whoever performs it. People
also rely on procedural memory: a practised skill runs without being reasoned
through on each use.

In the case, applying the revised Map means finding, for every change, the
files that the source code and build configuration reference. A model can do
this by reading the source each time. Code does it the same way each time at
low cost. The pattern is general: exact steps such as traversal, counting,
and state tracking have one correct result, which code delivers without the
variation a model brings to each reading, while judgments about meaning stay
with the model
([scheduler–LLM separation exploits an error-correction asymmetry](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md)).

So the builder writes and maintains code as well as theories. The code stays
open to criticism: whether it runs is a separate question from whether it
captures the intended claim.

## Why this is compatible with the Bitter Lesson

The Bitter Lesson says that general methods which scale with computation
outperform methods built on human knowledge. A builder that keeps written
theories and code looks like the second kind.

The lesson's axis, however, is how content is produced, not the form it is
kept in. The hand-designed features in Sutton's examples were built by people
as the solution, and the method never learned to replace them. A theory that
the builder proposed, criticized, and revised is a product of search and
selection. It happens to be readable. The same holds for code the builder
wrote and tested.

This is where the first bet matters. With people in the internal roles, the
loop scales with staff. With computation in every role, more computation
buys more conjecture and more criticism. Full automation is what makes the
retained theories a learned product.

Automation is necessary for this compatibility, not sufficient. Two
conditions remain open.

The starting methodology must be outgrown. People wrote its first version
and its definitions. The arrangement fits the lesson only if the builder
acquires what each new area requires without people supplying it area by
area.

The search must scale. Assigning credit across a large body of
interdependent text and code is an open problem. Weight training, or a model
that rebuilds the same content when needed, may do the same job at lower
cost. The retained arrangement has to earn its place against those
alternatives.

*(Continues with: what would show the bets wrong — the three adopted
hypotheses and external assessment, short, linking the testing supplement —
and where Commonplace is now: people still fill internal roles; the first
run; the supplements.)*

---

# Working notes

## How the argument is meant to run

Each section should follow from the one before it:

1. **Opening** — the loop is ordinary (everyday, science, current systems);
   the article names it and announces two bets and their consequence.
2. **A case** — one concrete run of the loop, ending with what is worth
   keeping from a failure.
3. **What counts as learning** — the two conditions, read off the case; what
   does not meet them; who the learner is (the whole system, with the
   research community as the instance); what the definition leaves out
   (the amoeba end of Popper's range).
4. **The first bet** — the community shows the loop works with people in the
   roles; the bet puts models in every role, given a methodology; fixed
   weights as the study condition; two reasons; one objection.
5. **Why the methodology must be precise** — follows from "given a
   sufficiently precise description", and from the second reason (the
   builder revises its methodology, so criticism must be able to name a
   part).
6. **The second bet** — code as well as prose, stated briefly.
7. **Bitter Lesson** — the objection both bets invite; the production-method
   reply; why the first bet is what makes the reply available; two open
   conditions.

Terms fixed in this revision, one per concept: *loop* (informal) and
*conjectural learning* (its name); *theory builder* / *builder*; *internal
roles*; *methodology* (replaces "description of the work" after it is
introduced); *code* (not "program", which the case uses for the released
tool); *bet* for the two beliefs (the article reserves *hypotheses* for the
three adopted ones and *conjecture* for theories in general).

Changes made for coherence in the 2026-09-21 revision: the opening now announces both
bets; the case is included in full so the draft reads straight through, and
its closing paragraph is the three-tier contrast; agent memory and
automated-science systems moved from a trailing paragraph into the reasons
for the first bet; theory builder, internal roles, methodology, autonomous,
and reflective are each defined where first needed; Commonplace is introduced
in the opening and identified as a first version of the methodology; a
fixed-weights paragraph was added to the first bet.

## Cut in the length pass (2026-09-21)

The operator asked for a shorter front half. Each cut and a proposed
destination:

- **Two of four reasons for the first bet.** "Much of the methodology of
  criticism has already been written down" (weakest; no note supports it) —
  dropped. "Models already attempt some of the roles" (agent memory and
  automated-science systems) — folded into the opening as one caveat
  sentence.
- **The tacit-skill objection**, cut from a paragraph with two replies to
  three sentences. The fuller version could go to the bootstrap supplement.
- **The terms *autonomous* and *reflective*.** Each was introduced and used
  once. The ideas stay in plain words ("computation fills every internal
  role"; "the builder is meant to revise it"). The closing sections can
  introduce the terms if they use them.
- **The fixed-weights paragraph**, cut to two sentences. Dropped: fixed
  weights "do not show which retained change caused" an improvement. That
  belongs with the testing material in the closing sections.
- **The boundary-cases paragraph** became one sentence pointing to the
  definition note.
- **The amoeba paragraph**, cut to two sentences.
- **The tutorial example** (application is not learning), cut to two
  sentences.
- **The precision section's first two reasons** merged into one (variable
  reading, and telling a wrong theory from a misreading). The expert-system
  paragraph was halved; dropped: "in a formal language" and "a general model
  interprets it".
- **The second bet's list of code kinds** (retrieval, checks, validators,
  schedulers) and the software-house sentence. The supplement link goes in
  "Where to go next".
- **The "order of work" paragraph** in the Bitter Lesson section (computation
  belongs inside the loop from the start). It is advice on running the
  program; its home is the bootstrap note, which already says it.
- **The case's help-command mechanics**, trimmed.

## Sources for each section

- **What counts as learning** —
  [definition](../../notes/definitions/conjectural-learning.md), including its
  "Relation to Popper" table, which already draws the amoeba-to-scientist line
  without naming it. The research-community instance is not yet in any note.
- **The first bet** — the adopted Sufficiency hypothesis in the
  [testing supplement](../../articles/testing-the-conjectural-learning-program.md#the-hypotheses);
  [theory builder](../../notes/definitions/theory-builder.md),
  [reflective](../../notes/definitions/reflective-theory-builder.md), and
  [autonomous](../../notes/definitions/autonomous-theory-builder.md) builder
  definitions; the fixed-weights paragraph restates the current lead's "The
  arrangement Commonplace studies". The two reasons and the tacit-skill
  reply are new in this draft.
- **Why the methodology must be precise** — new in this draft. The
  per-area-vocabulary failure condition is from
  [the bootstrap note](../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md).
- **The second bet** —
  [a fixed-model house must retain missing procedures for theory use](../../notes/a-fixed-model-house-must-retain-missing-procedures-for-theory-use.md);
  [codification](../../notes/definitions/codification.md);
  [scheduler–LLM separation exploits an error-correction asymmetry](../../notes/scheduler-llm-separation-exploits-an-error-correction-asymmetry.md),
  added at the operator's direction as additional support. It supplies the
  reason code is cheaper and more reliable for exact steps, a "humans exhibit
  the same pattern" section (pen and paper) that backs the notation analogy,
  and the point that the symbolic layer is itself a learning target. When the
  article is promoted, add this note to `source_notes`.
- **Bitter Lesson** —
  [production methods, not representational forms](../../notes/the-bitter-lesson-selects-production-methods-not-representational.md);
  [the bootstrap note](../../notes/a-bootstrap-fits-the-bitter-lesson-only-if-learning-outgrows-it.md);
  [unearned reach](../../notes/bitter-lesson-selects-against-unearned-reach-not-against-structure.md).

## Where the draft goes beyond the notes

The article is distilled from the notes, so each of these needs a decision:
fold it into a note first, or keep it as the article's own argument.

1. **A research community as an instance of the definition**, and the amoeba
   contrast by name. Proposed home: a short paragraph in the definition note's
   "Relation to Popper" section. The amoeba sentence needs `cp-skill-ground`.
2. **"Code as well as prose" is a comparative bet, stated briefly (operator,
   2026-09-21).** The operator's direction: it is one of the program's bets
   that adding code will help, the lead should not justify it at length, and
   the claim needed is only that the loop is easier with code, not that prose
   alone would fail. Two earlier drafts overclaimed ("prose is not enough",
   "prose alone will not carry the loop"). The comparative form agrees with
   the missing-procedures note, which says code "can make specified steps
   cheaper and more reliable" and that "there is no general threshold at
   which every growing theory must become code". An earlier draft also argued
   from fixed weights (a pinned model cannot consolidate a skill through
   practice, so code is where a skill can live); that argument is in the note
   and was cut from the lead.
3. **Two analogies carry the second bet: mathematical notation in science,
   and procedural memory in people.** The notation point is the operator's:
   science also relies on a formal carrier, which people execute by rule much
   as a computer does. The scheduler–LLM separation note makes the nearby
   point that people reach for pen and paper because mental operations lack
   reliable intermediate state; no note makes the claim about mathematical
   notation in science specifically. Popper 1968 §6 treats informal argument
   as preceding formalization, which is compatible. The
   missing-procedures note warns that
   [human analogies suggest functions, not component boundaries](../../notes/human-analogies-suggest-functions-not-component-boundaries.md).
   The draft uses both analogies for the function only (a step that runs
   without fresh judgment) and does not claim a separate component.
4. **The two reasons for the first bet and the tacit-skill objection.** Not
   in any note. Candidate home: the research companion, or the bootstrap
   article. The opening mentions agent memory and automated-science systems
   without classifying them; naming particular systems still needs a check
   against the KB's reviews and ingests.
5. **Precision as a condition of criticizing the methodology.** Not in any
   note in this form. It is addressability applied to the methodology. It may
   fit the addressable-theory definition or the companion.
6. **"Scales with staff" versus "scales with computation".** The bootstrap
   note implies it (failure condition: "human global judgment and maintenance
   grow with the corpus") but does not say it this way.
7. **"The same holds for code the builder wrote and tested"** (Bitter Lesson
   section). The production-methods note's learned-localized quadrant covers
   code search (FunSearch, AlphaDev), so this is supported, but the sentence
   is new.

## A candidate argument left out

A methodology written in prose may get better as base models improve, with no
rewriting, while hand-built scaffolding goes stale. No note supports this. The
nearest,
[scaling absorbs scaffolding at fixed difficulty, not at the frontier](../../notes/scaling-absorbs-scaffolding-at-fixed-difficulty-not-at-the-frontier.md),
is about a different question. Left out until someone argues it in a note.

## Current sections this front half displaces

| Current section | Proposed fate |
|---|---|
| Opening paragraphs | Replaced. |
| A case | Kept. Its contrast paragraph and its "other referenced files" sentence merge into the three-tier paragraph; the closing paragraph shrinks to the "hypothetical example" sentence, and its capacity-before-evidence point moves into "What counts as learning". The part-versus-whole revision sentence is dropped from the lead (it belongs with the addressability conjecture). |
| Conjecture, criticism, and improved capacity | Replaced by "What counts as learning". The `P1 → TT → EE → P2` schema, survival without text change, persistence, and visibility stay in the definition note. |
| The arrangement Commonplace studies | Absorbed: fixed weights and the whole-system unit into "The first bet"; interpreted methodology and codification into the two bets; recursive self-improvement and the Schmidhuber positioning are not in the front half and need a home (the companion note already has them). |
| Three conjectures about the mechanism | Open. They are the program's mechanism questions, but they are not on the new argument's main line. Candidates: a short passage in the closing "what would show the bets wrong", or the testing supplement. The three-tier paragraph in the case is the small version of the efficiency question. |
| Retention has costs | Its Bitter Lesson paragraph is absorbed. The cost accounting could shrink to a few sentences beside the Comparison hypothesis or move to the companion note. |
| Requirements and responsibility | Move out of the lead. The theory-builder definition is now two sentences in "The first bet"; lineage belongs in a supplement; the requirement-versus-description point could go to the testing supplement. |
| Reflection and autonomy | Absorbed into "The first bet" (one sentence each). |
| What would test it; Assessment from outside the builder | Kept, shortened, as the closing "what would show the bets wrong". Each bet should be tied to what refutes it: Sufficiency for the first bet; the matched-builders test in the missing-procedures note for the second, which has no adopted hypothesis. |
| The first arrangement; Open questions; Where to go next | Kept, shortened. |

## Title

"Conjectural Learning with Fixed Models" names the study condition. The
front half now gives fixed weights one paragraph, in the first bet, so the
title is supported but does not name the thesis. Options: keep it, or retitle
around the bet. A retitle is a relocation and goes in its own commit.
