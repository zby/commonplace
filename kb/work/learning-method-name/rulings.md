# Rulings and how the definition was reached

Moved out of [the workshop README](./README.md) on 2026-11-21 so that the
README states only the current position. Written by an agent
(claude-fable-5-2) from one day's conversation with the operator. Quoted
statements are the operator's.

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
| The noun for the system | Deliberative learner, contrasted with the deliberative agent. Whether a deliberative learner is a deliberative agent stays open. | "it is possible that we'll discover something in that old tradition that is closer to us" |
| Is a fixed measure excluded? | No. A judgment by one fixed measure is a special case of condition 2. This reverses the agent's rider on deterministic checks and its reading that being bound to one measure separates Commonplace from symbolic AI. | "Exclusion of fixed measure should not be part of the definition ... our definition should be more general - the fixed measure would be a special case ... there is a kind of continuity - small changes should not get us out from the definition" |
| Names for the two kinds | Single-loop and double-loop deliberative learning, after Argyris. The agent checked the Argyris ingest: his double-loop questions "underlying objectives and policies", so the KB's use, which requires only that measures can be questioned, is narrower. | "maybe we should use double loop deliberation?" |
| Workshop goal | Changed from choosing a name to defining the process. | "it is about defining the learning process we are working on" |

Three parts of the draft are the agent's and go beyond the rulings:

- **The rider on deterministic checks, since reversed by the ruling on
  fixed measures.** The claim that one measure is enough
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
Commonplace from symbolic AI. The agent concluded that being bound to one
measure does. The later ruling on fixed measures removed that from the
definition: it is now a property of a learner, and what separates
Commonplace is the conjecture about a language model's judgment.

