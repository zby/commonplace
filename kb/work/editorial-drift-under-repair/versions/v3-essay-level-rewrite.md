---
description: "Naur argues program theory cannot be expressed in rules, then concludes it is bound to humans; the step needs the unargued premise that every non-human candidate follows formulable rules, which a trained interpreter contests"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, context-engineering]
---

# Naur binds program theory to humans through the premise that machines only follow rules

Peter Naur's essay *Programming as Theory Building* makes two claims that are usually read as one. The first is that the theory of a program — the capacity to map it onto the world, justify its parts, and extend it coherently — cannot be expressed in rules. The second is that the theory is therefore "inextricably bound to human beings." The first is argued. The second follows from it only through a premise the essay uses everywhere and argues nowhere: that the alternative to a human theory-holder is a follower of formulable rules. An interpreter whose judgments are not given by rules anyone formulated falls outside that dichotomy, so the essay's argument does not reach it. What the essay does establish about such an interpreter is a set of conditions, not a verdict.

## The inexpressibility argument targets formulable rules

Naur takes his notion of theory from Ryle. A person who has a theory can do certain things and also explain, justify, and answer questions about them. Intelligence in this sense cannot consist in following rules: adhering to a rule is itself done well or badly, so intelligence-as-rule-following needs rules for following rules, and so on in a regress Naur calls absurd. What stops the regress is a grasp of similarity between situations, and similarity of the relevant kind "cannot be expressed in terms of criteria, no more than the similarities of … human faces, tunes, or tastes of wine."

Applied to programs, this gives the three capabilities of a theory-holder — mapping between world and program text, justifying each part, and incorporating a new demand by perceiving its similarity to existing facilities — and the claim that the third "cannot be reduced to any limited set of criteria or rules." The argument's target is precise: criteria that can be formulated. Naur says so directly when he calls the similarity judgment "entirely outside the reach of what can be determined by rules, since even the criteria on which to judge it cannot be formulated." Text that must decide a case by itself is a set of formulated criteria, so the argument bounds it. It says nothing about a recognizer whose criteria were never formulated — the faces, tunes, and wine examples are exactly things such recognizers judge.

## The step to human beings rests on an exhaustive dichotomy

The human-binding conclusion is stated as a main claim, not a hedge: the theory "could not conceivably be expressed, but is inextricably bound to human beings," and "by its very nature is part of the mental possession of each programmer." The "but" carries an inference from *not expressible* to *human*. It is valid only if the candidates for holding a theory are exhausted by two kinds: human insight and formulable rules.

That is how the essay partitions the field. Programming is defined as matching real-world activity "to the formal symbol manipulation that can be done by a program running on a computer." The similarity judgment is "accessible to the human beings who possess the theory" and "outside the reach of what can be determined by rules." The opposing view Naur rejects is that "human beings perform best if they act like machines, by following rules," a view he pairs with the notion "that the human mind works like a computer." Throughout, *machine* and *rule-follower* name the same pole, and the human stands at the other. Given that partition, "not rules" entails "human," and the conclusion follows.

The partition was a fair description of the computers Naur knew, and he never argues for it because nothing in 1985 contested it. It is a premise all the same, and a premise with a different modal status from the regress argument: the regress is a conceptual result about rules, while the partition is a claim about which kinds of interpreter exist.

## A trained interpreter falls outside the partition

An LLM is a machine, but its similarity judgments are not determined by criteria anyone formulated. They were acquired from examples — the route Naur himself gives for how theory is acquired, by "doing the relevant things under suitable supervision and guidance." So an LLM does not sit at either pole of Naur's partition: not a human, and not "what can be determined by rules" in the sense his argument uses. The inexpressibility argument therefore does not apply to it, and the human-binding conclusion does not follow for it. This is a claim about the argument's reach, not about the interpreter's competence. It says the essay did not pose the question whether such an interpreter holds a program's theory; it does not answer that question.

Nor does it help to note that an LLM is a computable procedure. Naur's argument is about expressibility — criteria that can be *formulated* — not about computability, and his own examples of the inexpressible are all judgments that trained recognizers perform. An argument that some capacity cannot be computed at all would have a different shape and would reach text and interpreter together; the essay makes no such argument.

## What the essay still establishes as conditions

Dropping the partition leaves the rest of the essay intact, and the rest is demanding. Naur's evidence is that competent humans with full artifacts failed: in his compiler case, a motivated group with the full program text, annotated sources, and written design discussion proposed extensions that the original authors instantly recognized as patches destroying the structure, and only personal advice from the authors repaired them. His conclusion is that for a newcomer "it is insufficient that he or she has the opportunity to become familiar with the program text and other documentation"; what is required is close work with those who hold the theory. So a competent interpreter plus text is not thereby a theory-holder, and any composite that claims to be one owes three things:

- **Program-specific acquisition.** General competence over language and the world is not the theory of this program. The composite must acquire the particular theory, and Naur's cases show that reading the artifacts as they were written did not achieve that even for humans.
- **Retained premises the interpreter cannot regenerate.** What the compiler authors supplied in person was which existing facilities a new demand resembled and why the structure was as it was. Those are decision premises, and the recovery test in [design rationale must preserve decision premises its interpreter cannot regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md) asks which of them the text must carry because the interpreter cannot recover them from the implementation and general knowledge. Naur's cases do not test this route: his programmers were "unable to conceive of any kind of additional documentation that would be useful," which reports what was tried, not what retained rationale selected at decision time would do.
- **Dispositional reliability.** Naur ties a program's life to a team that *remains* in control and can answer the next demand. A composite that produces one coherent extension has not shown it holds the theory; it must exercise the capacity across later occasions.

These are the conditions under which [theory-mediated self-improvement needs both interpretation and retention from one substrate](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) proposes its division of labour: the interpreter supplies the case-by-case judgment, the retained text supplies the premises. Whether any current LLM-plus-artifact system meets them is an empirical question this note leaves open. What it closes is the claim that Naur's argument settles it in advance.

---

Relevant Notes:

- [Programming as Theory Building](../sources/programming-as-theory-building.ingest.md) — abstracted-from: supplies the Ryle regress, the inexpressibility-as-criteria argument, the human-binding claim, the machine-as-rule-follower framing, and the compiler-transfer case; the partition diagnosis is this note's reading
- [Attempted recovery identifies informational gaps, not provenance or authority](./documentation-generates-the-system-rather-than-describing-it.md) — grounds: why Naur's failed transfers show that content was missing from the supplied artifacts, not that program theory is inexpressible in principle
