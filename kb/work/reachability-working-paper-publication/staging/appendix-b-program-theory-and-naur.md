# Appendix B — Program theory and Naur

```text
Versioned argument snapshot for: The Reachability Conjecture
Paper version: pending
Mode: paper adaptation (compressed)
Frozen source tag: pending
Source paths: kb/notes/naur-equates-machine-execution-with-formulated-criteria.md;
  kb/notes/naurs-compiler-case-tests-one-historically-bounded-documentation-and-consumption-system.md;
  kb/notes/program-theory-sustains-search-under-delayed-feedback.md;
  kb/sources/programming-as-theory-building.ingest.md
Live successors: the same paths on the main branch
Status: staging — not published
```

The paper's possibility claim rests on two readings of Peter Naur's essay
*Programming as Theory Building* (Naur 1985; see References for the edition and
locations). This appendix states them and no more. The full arguments are in
the live notes.

## B.1 Formal execution is not the same as formulated criteria

Naur makes two claims that are usually read as one. First, a program's theory,
the capacity to map the program onto the world, justify its parts, and extend
it coherently, cannot be expressed as criteria or rules. Second, that theory is
"inextricably bound to human beings". The essay's bridge from the first to the
second is an equation: what a program running on a computer does is execute
formulated criteria, so a judgment whose criteria cannot be formulated is a
judgment no program can make.

The first claim is precise about its target. Naur takes his notion of theory
from Ryle: having a theory is being able to do certain things and to explain,
justify, and answer questions about them. Rule-following cannot be the whole of
it, because following a rule is itself done well or badly, and rules for
following rules regress. What ends the regress is a grasp of similarity between
situations, and that similarity "cannot be expressed in terms of criteria, no
more than the similarities of ... human faces, tunes, or tastes of wine". The
theory-holder's third capability, taking in a new demand by seeing its
similarity to what the program already does, "cannot be reduced to any limited
set of criteria or rules".

The bridge held for the programs the essay describes. A machine judged only by
criteria a programmer had written, so machine execution and formulated criteria
were one thing, and the premise was a description rather than a conjecture.
Trained recognizers have since separated them. A face recognizer is formal
symbol manipulation by a program running on a computer, and it performs a
similarity judgment for which nobody can state the criteria. It does not touch
Naur's first claim; the criteria are as unformulable as he said. It breaks the
bridge: formal execution no longer requires formulated criteria, so a judgment
can be beyond formulable criteria and still within reach of a program. Two of
Naur's three examples of the inexpressible, faces and tunes, are the ones the
separation was demonstrated on.

Learning is not what does the work. A decision tree induced from examples is
still an explicit finite rule set and sits on Naur's rule-determined side. What
matters is whether the resulting judgment has a formulable rubric. An objector
who says the recognizer's parameters are the formulated criteria, only not
readable, proves too much: on that reading the recognizer has expressed face
similarity in criteria and Naur's first claim is false; on the other reading the
bridge is false. Either way the human binding fails.

What the paper takes from this: a successful house would falsify Naur's
conclusion that only people can hold a program theory, while leaving his first
claim intact. The LLM interprets a paragraph of rationale without that judgment
first being written out as a complete rule. Nothing here shows that any current
system holds a program's theory; it removes the reason to think the question
was closed in advance.

## B.2 What the compiler case rules out and what it leaves open

Naur reports a strong transfer failure. A motivated successor group received the
full program text, annotated sources, extensive written design discussion, and
personal advice from the original group, and still proposed extensions that the
original group recognized as patches destroying the compiler's structure, while
the original group could propose simple changes framed within it. The supplied
package did not convey enough program-specific understanding to that group.

The case rules out one answer: more prose of the same kind does not by itself
transfer a program theory. It does not rule out other packages or other
readers. The package and its use belonged to the documentation and
knowledge-consumption practice of its time. People had to organize, find,
select, and bring to bear the relevant material through their own reading. The
case did not test rationale linked to the decisions it affects, records with
explicit scope and status, machine-maintained indexes, retrieval by meaning,
context assembled by following dependencies, or a note surfaced at the point of
decision.

Those mechanisms create an empirical possibility, not a rebuttal. None of them
holds a program theory by itself. Whether a newer way of representing and
consuming project knowledge transfers more of the required capacity, to people
or to a house built from an LLM, is an open question, and the paper's witness
protocol (Appendix C) is the shape of an answer to it. The right comparison
varies representation and consumption together while holding source evidence
and demands fixed: ordinary documentation, structured rationale with indexing
and context assembly, and raw records from which the reader reconstructs an
understanding are three different transfer paths. Naur's case establishes the
failure of the first.

## B.3 Holding a theory is a capacity shown over many changes

Naur's hardest test of holding a theory is coherent modification: change the
program for a new demand without destroying the structure and purpose that make
it work. He ties a program's life to a team that remains in control of it and
can answer later demands, and dates its death to the moment demands can no
longer be answered intelligently. One coherent change may be lucky or copied;
holding a theory is a capacity across occasions.

Meeting the test does not need a theory strong enough to deduce the right change
in one step. A working program theory may be partial, imprecise, and fallible.
It counts because it keeps the search for a change coherent: it shapes which
changes are considered, what must be preserved, how failures are read, when to
backtrack, and what to revise. Searching, failing, and backtracking are not
signs that the theory was missing. The consequences of a choice may not arrive
until later demands do, so the test is over a path, not a first proposal.

Three tests follow for any claim that a house holds a program's theory, and
Appendix C is built on them:

- **Program-specific acquisition.** General competence over language and the
  world is not the theory of this program. The house must acquire this
  program's mapping, justification, and modification judgments. (C.4, items 2
  and 3)
- **Premises the reader cannot regenerate.** If a coherent change depends on a
  decision premise that cannot be recovered from the implementation and general
  knowledge, some retained component must supply it, and withholding it must
  change what the house does. (C.4, item 4; C.5)
- **Reliability across occasions.** Holding is shown over novel demands,
  delayed contradiction, and recovery, not by one accepted edit. (C.4, items 5
  and 8; C.7)

A record that the house cited a piece of retained theory at a decision is a
trace of what it claims to have used. Withholding or replacing that theory is
the stronger evidence that its use was load-bearing.
