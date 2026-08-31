---
description: "Naur argues program theory cannot be expressed as criteria, then concludes it is human-only; the bridge is that machine execution meant formulated criteria — true of the programs of his day, and separated since by trained recognizers"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, context-engineering]
---

# Naur binds program theory to humans by equating machine execution with formulated criteria

Peter Naur's essay *Programming as Theory Building* makes two claims that are usually read as one. The first is that a program's theory — the capacity to map it onto the world, justify its parts, and extend it coherently — cannot be expressed as criteria or rules. The second is that the theory is "inextricably bound to human beings." The essay's bridge between them is an equation: what a program running on a computer does is execute formulated criteria, so a judgment whose criteria cannot be formulated is a judgment no program can make. For the programs Naur's essay is about, the equation was accurate — making a machine judge meant writing the criteria. Trained recognizers have since separated formal execution from formulated criteria, and the examples Naur chose for the inexpressible — faces, tunes, tastes of wine — are the ones they separated them on. What survives is not the human binding but a set of tests that any interpreter-plus-artifact composite has to pass.

## The inexpressibility argument targets formulable criteria

Naur takes his notion of theory from the philosopher Gilbert Ryle. Having a theory is being able to do certain things and also to explain, justify, and answer questions about them. Intelligence of this kind cannot consist in following rules: adhering to a rule is itself done well or badly, so intelligence-as-rule-following would need rules for following rules, in a regress Naur calls absurd. What ends the regress is a grasp of similarity between situations, and similarity of the relevant kind "cannot be expressed in terms of criteria, no more than the similarities of … human faces, tunes, or tastes of wine."

Applied to programs, this yields the theory-holder's three capabilities — mapping between the world and the program text, justifying each part, and incorporating a new demand by perceiving its similarity to existing facilities — and the claim that the third "cannot be reduced to any limited set of criteria or rules." The target is precise: criteria that can be formulated. Naur says so when he calls the judgment "entirely outside the reach of what can be determined by rules, since even the criteria on which to judge it cannot be formulated." Text that must decide a case by itself is formulated criteria, and the argument bounds it.

## The bridge to human beings is an equation that held for the programs of its time

The human binding is stated as "a main claim": the theory "could not conceivably be expressed, *but* is inextricably bound to human beings," and "by its very nature is part of the mental possession of each programmer." The "but" moves from *not expressible* to *human*. What licenses the move is the way the essay places computers. Programming is defined as matching real-world activity "to the formal symbol manipulation that can be done by a program running on a computer." The similarity judgment is "accessible to the human beings who possess the theory" and "outside the reach of what can be determined by rules." The view Naur rejects is that "human beings perform best if they act like machines, by following rules," paired with the notion "that the human mind works like a computer." In these passages a program on a computer, rule-determination, and formulable criteria occupy one pole, and human judgment the other.

So the inference runs: the criteria cannot be formulated; what a program does is execute formulated criteria; therefore no program can make the judgment; therefore it is human. The second premise is the bridge. The essay does not argue it and did not need to: for the programming it describes, a machine judged only by criteria a programmer had written, so machine execution and formulated criteria were one thing and the premise was a description, not a conjecture. Read in full, the essay's other person-bound statements — theory as mental possession, relevance as something the programmer must contribute — assert the binding without giving a second reason for it. The equation is the only reason the essay offers, and it was a good one when it was written.

## Trained recognizers separate execution from formulated criteria

A face recognizer is formal symbol manipulation by a program running on a computer — its execution is as formal as anything Naur describes — and it performs a similarity judgment for which nobody can state the criteria. It is not a counterexample to Naur's first claim; the criteria are as unformulable as he said. It is a counterexample to the bridge: formal execution no longer requires formulated criteria, so a judgment can be beyond formulable criteria and still within the reach of a program. The same holds for tune and taste recognition, and for the case that matters here, judging whether a new demand in natural language resembles a facility a program already has — the judgment a language model makes over retained text.

Learning is not the discriminator. A decision tree can be induced from examples and remain an explicit finite rule set, so "learned" does not by itself place a system outside Naur's rule-determined pole. The discriminator is whether the resulting judgment has a formulable rubric. A decision tree has one; a face recognizer's parameters do not yield one. Naur's argument bounds the first kind and never reaches the second, because when it was written programs were the first kind.

None of this shows that any program holds a program's theory. Breaking the bridge removes a reason to think the question is closed; it does not answer it.

## The transfer cases still impose three tests

Naur's compiler case is a bounded transfer failure. A motivated successor group had the full program text, annotated sources, extensive written design discussion, and personal advice, and still proposed extensions the original group recognized as patches destroying the structure; the original group could propose simple changes framed within it. The case shows that the supplied package did not convey enough program-specific understanding to that group. It does not test other rationale packages or other interpreters.

Read with Naur's account of theory possession, the case gives three necessary tests for any claim that an interpreter-plus-artifact composite holds a program's theory:

- **Program-specific acquisition.** General competence over language and the world is not the theory of this program. The composite must acquire this program's mapping, justification, and modification judgments; the tested artifacts did not enable the successor group to do so.
- **Provision of premises the interpreter cannot regenerate.** If coherent modification depends on a decision premise the interpreter cannot recover from the implementation and general knowledge, some component must supply it. The recovery test in [design rationale must preserve decision premises its interpreter cannot regenerate](../../../../notes/design-rationale-must-preserve-unregenerable-decision-premises.md) identifies such premises. Naur's case establishes the failure of one supplied package, not of retained rationale as a route.
- **Dispositional reliability.** Naur ties a program's life to a team that remains in control of it and can answer later demands, and dates its death to the moment modification demands cannot be intelligently answered. One coherent extension may be lucky or memorized; possession is a capacity across occasions.

Whether a current LLM-plus-artifact system passes these tests is an empirical question. What the essay cannot do is settle it in advance, because the premise that would settle it — that a program executes only formulated criteria — stopped being true of programs after it was written.

---

Relevant Notes:

- [Programming as Theory Building](../../../../sources/programming-as-theory-building.ingest.md) — abstracted-from: supplies the Ryle regress, the inexpressibility and human-binding claims, the program-as-formal-symbol-manipulation and rule-following passages, the program-life passage, and the compiler case; the identification of the bridge as an equation is this note's reading
- [Attempted recovery identifies informational gaps, not provenance or authority](../../../../notes/documentation-generates-the-system-rather-than-describing-it.md) — grounds: why Naur's failed transfers show that content was missing from the supplied artifacts, not that program theory is inexpressible in principle
- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../../../../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) — extends: the interpreter/retention division of labour that the three tests condition
