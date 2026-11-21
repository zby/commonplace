# Defining the learning process

Posed 2026-11-21 by the operator. Written by an agent (claude-fable-5-2) from
one day's conversation with the operator. Quoted statements are the
operator's. Everything else is the agent's wording and awaits adoption. The
directory name comes from the workshop's first goal, which was to choose a
name. Earlier states of this framing are in the Git history.

## Goal

Set by the operator: define the learning process we are working on. The
definition has to say what the process is, cover all the learning that
happens in Commonplace, and separate the process from the claim that a
particular change was learned.

## Result so far

[The draft definition](./draft-definition.md) defines **deliberative
learning** by three conditions:

1. **Legible store.** What is learned is kept as changes to a store that can
   be read.
2. **Judgment in the loop.** Each change is kept or dropped by an on-balance
   judgment, made as a step of the learning loop and not bound to one measure
   fixed beforehand.
3. **Open to criticism.** The judgment is held as a conjecture and can later
   be found wrong.

The term has no success condition. "Learned" is a separate claim about one
retained change, with the verdicts learned, not learned and open.

No library file has been changed.

## Why the question was open

Commit `21021fcc9` (2026-09-25) retired the term "conjectural learning" and
moved its consumers to the redefined
[theory builder](../../theory/definitions/theory-builder.md). The reason
given was that the new definition "has no success condition: whether a
builder learns is the hypothesis under test." That left the system with a
name and the process without one.

The process could not be called learning while nobody could say what
"improved" would be checked against. The
[on-balance note](../../theory/on-balance-judgments-can-guide-improvement-without-a-global-measure.md)
and [the definition workshop](../bounding-omitted-effects/README.md) supplied
that: a step is an improvement on balance when every reasonable measure
favours the successor. The operator's response to the objection that a name
ending in "learning" asserts what the program is testing: "Didn't we just
solve this problem?"

## Rulings, in the order they were made

All on 2026-11-21.

| Question | Ruling | The operator's words |
|---|---|---|
| May the name say "learning"? | Yes. The name is a process name with no success condition, as "reinforcement learning" is. | Ruled with the first name choice. |
| First name | Conjectural learning, later replaced. | "make it 'conjectural learning'" |
| What "conjectural" refers to | The judgments of improvement, so that the term covers every kind of retained change. | "the other is about on balance judgements being conjectures. I think we want the second one - so that all learning that happens in Commonplace was under one umbrella" |
| What distinguishes the process from model training | Legible storage makes it possible. The on-balance judgment inside the loop is the core. | "the difference from people judging models is that this is outside of the learning loop - in our case the on-balance judgement is inside. On balance judgement seems the core here" and "The legible store is what makes the on-balance judgement possible" |
| Final name | Deliberative learning. "On balance" stays as the qualifier of the verdict. | "on-balance would fit - but on-balance is kind of not scientific", then "revise the draft to deliberative learning, keep on-balance" |
| Basis of the word | Deliberation as the weighing of reasons, not the deliberative agent of agent architectures. | "we don't need deliberative agent definition for us" |
| What distinguishes Commonplace | Language models make the judgments. | "we use LLMs to make these judgements" |
| The autonomous judge | A language model. Nothing is said about size. | "a judgement machine that understands language (and code)"; "say language model and that is enough" |
| Role of the sources | Background. The definition stands without them. | "it is good to have this as some kind of background - but I think we can define deliberative learning precisely enough for our uses" |
| Reversibility | Not a condition. The third condition concerns the judgment. | "we do delete stuff - so it is not that everything is reversible" |
| Deterministic checks | They meet the second condition. | "on-balance judgement can contain a simple deterministic judgement as a degenerate case" |
| Which loop | A claim names a system and its store. The conditions are checked on the outermost loop the system runs itself. | "I fully agree with your assessment" |
| Workshop goal | Changed from choosing a name to defining the process. | "it is about defining the learning process we are working on" |

Three parts of the draft are the agent's and go beyond the rulings:

- **The rider on deterministic checks.** The claim that one measure is enough
  for a question must itself stay open. Without it, a symbolic system bound
  to one formula would meet the definition.
- **The distinction between "on balance" and "deliberation".** "On balance"
  qualifies the verdict. "Deliberation" names the process that reaches it.
  *Deliberare* is derived from *libra*, a pair of scales, so the two words
  share an image. The operator asked for the etymology to be checked and
  used.
- **What "learning" adds to deliberation.** The sources on deliberation do
  not cover keeping the outcome or correcting it from later evidence. Those
  are the first and third conditions.

## The comparison with symbolic AI

The operator's account, now background in the draft:

- "What is being learned is kind of what symbolic AI did, but we have a new
  method of doing it."
- The on-balance definition of improvement "would work for symbolic AI as a
  definition, but it might be unworkable in practice."
- A symbolic system would have trouble even with single cases. For a new
  Python release it could run tests, but it would need an enormous test
  array. People judge on balance inside single cases too.

The agent recalled three claims about symbolic learners from memory. The
[Minton ingest](../../sources/minton-utility-of-ebl-aaai88.ingest.md)
corrected two. PRODIGY did not keep every learned rule, and its utility
estimate was revised from use. What was fixed was the measure: one formula in
one unit. So a judgment inside the loop does not by itself separate
Commonplace from symbolic AI. Being bound to one measure does.

## Sources

Four ingests were made on 2026-11-21. None has retained quotes.

| Ingest | What the draft takes from it |
|---|---|
| [Practical Reason](../../sources/sep-practical-reason.ingest.md), Stanford Encyclopedia of Philosophy | Deliberation by one agent. Judging without a single measure is a recognized position and not the majority formal view. |
| [Fishkin and Mansbridge, 2017](../../sources/fishkin-mansbridge-deliberative-democracy-intro.ingest.md) | Deliberation by a group. |
| [Wooldridge and Jennings, 1995](../../sources/wooldridge-jennings-intelligent-agents.ingest.md) | The deliberative agent, as a use the term is not taken from. |
| [Minton, 1988](../../sources/minton-utility-of-ebl-aaai88.ingest.md) | PRODIGY, the closest symbolic precedent. From a scanned copy of the conference version. |

Noted and not ingested: Zollo and Winter, *Deliberate Learning and the
Evolution of Dynamic Capabilities* (2002), which separates learning by
accumulated experience from learning by articulated and codified knowledge.

## Open

- **Where "learned" lives.** It is a section of the draft. It could be a
  section of the on-balance note.
- **Independent reading.** One agent wrote this framing and the draft, and
  changed its position on the name several times in one conversation.
  Agreement between agents is not evidence. The definition of "learned"
  should be read by an agent or person who did not take part.
- **Quotes.** The four ingests have none retained.
- **The conjecture itself.** That a language model can make on-balance
  judgments well enough is not established. The
  [Python change judgment probe](../../reports/retained/python-change-judgment-probe-2026-11-20/README.md)
  was designed to test it.

## Evaluation boundary

Until the operator adopts the draft, do not edit these to introduce the term:

- `kb/theory/definitions/theory-builder.md` and its checks;
- `kb/theory/commonplace-builds-a-theory-builder-and-tests-whether-it-learns.md`;
- the articles under `kb/articles/`, including the lead article's "distinct
  learning paradigm" section;
- the vocabulary table in `AGENTS.md` and the
  [collision ledger](../../reference/vocabulary-collision-ledger.md), which
  has no entry for "deliberative".

The September retirement of "conjectural learning" stands, so the redirects
in `properdocs.yml` need no change.

## What closes the workshop

- The operator adopts the draft, or a revision of it.
- The definition of "learned" has an independent reader's acceptance or a
  recorded disagreement.
- The definition is in the library under `kb/theory/definitions/`, and the
  term is in the `AGENTS.md` vocabulary table.
- The collision ledger has an entry for "deliberative" that separates this
  sense from the group sense and from the agent-architecture sense.
- The consumers in the evaluation boundary are listed and either edited or
  deferred with a reason.

Then delete this directory and remove its entry from `kb/work/README.md`.

## Bookkeeping

Commits carry `Workshop: kb/work/learning-method-name`. Positions from other
agents go in `positions/`, one file each, marked with who wrote them and
whether the author confirmed the file.
