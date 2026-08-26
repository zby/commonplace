---
description: "Naur's rule-inexpressibility argument does not establish that program theory is human-only; that conclusion needs a separate premise excluding every eligible nonhuman theory-holder"
type: kb/types/note.md
traits: [title-as-claim, has-external-sources]
tags: [foundations, context-engineering]
---

# Naur's rule-inexpressibility argument does not by itself bind program theory to humans

Peter Naur's essay *Programming as Theory Building* makes two claims that are often treated as one. First, a program's theory — the capacity to relate the program to the world, justify its parts, and extend it coherently — cannot be expressed as rules. Second, that theory is “inextricably bound to human beings.” Yet rule-inexpressibility does not entail human exclusivity. The latter conclusion requires a separate premise that excludes every eligible nonhuman theory-holder. Naur may find such a premise in his person-bound descriptions of theory or in his opposition between human judgment and rule-following machines. Either route, however, must be defended independently of the rule-inexpressibility claim.

This distinction separates a logical question from an empirical one. Logically, what additional premise connects rule-inexpressibility to human possession? Empirically, can a nonhuman interpreter acquire and exercise the theory of a particular program? Current LLMs make the empirical question salient, but their training history neither supplies the missing logical premise nor shows that they possess a theory.

## The regress targets rule-complete accounts of intelligence

Naur draws his notion of theory from the philosopher Gilbert Ryle. To possess a theory, on this account, is not merely to perform competently. It is also to explain, justify, and answer questions about one's performance. Such intelligence cannot consist solely in following rules. Following a rule can itself be done well or badly, so an intelligence-as-rule-following account requires further rules for following the first rules, then still further rules, and so on. Naur calls this regress absurd. He says it stops with a grasp of similarity between situations, and that similarity of the relevant kind “cannot be expressed in terms of criteria, no more than the similarities of … human faces, tunes, or tastes of wine.”

Applied to programs, this account gives a theory-holder three capabilities: mapping between the world and the program text, justifying each part, and incorporating a new demand by perceiving its similarity to existing facilities. Naur claims that the last capability “cannot be reduced to any limited set of criteria or rules.” He later calls the similarity judgment “entirely outside the reach of what can be determined by rules, since even the criteria on which to judge it cannot be formulated.”

Even if this inexpressibility claim succeeds, it rules out only a rule-complete account of the judgment. It does not identify the species of every possible bearer of the capacity. That further classification needs another premise.

## Human exclusivity needs an additional premise

Naur nevertheless states the human-binding conclusion as a main claim: program theory “could not conceivably be expressed, but is inextricably bound to human beings,” and “by its very nature is part of the mental possession of each programmer.” Moving from *not expressible as rules* to *human-only* therefore requires an exclusionary premise: no eligible nonhuman can exercise the relevant capacity.

At least for machines, one possible bridge comes from the boundary the essay draws between human judgment and rule-following execution. Naur defines programming against “the formal symbol manipulation that can be done by a program running on a computer.” He contrasts similarity judgments accessible to human theory-holders with what rules can determine, and he rejects the view that humans act like machines by following rules. In these passages, machine execution occupies the rule-following pole.

The essay also makes broader person-bound claims: relevance must be contributed by a programmer who understands the world, and theory is a programmer's mental possession. Those claims may provide additional exclusions. But accepting them would supply the human premise rather than derive it from the regress. This note therefore need not identify the machine-as-rule-follower dichotomy as Naur's only bridge. Its narrower point is that rule-inexpressibility alone does not establish human exclusivity.

## A trained interpreter exposes the question but does not settle it

A learned interpreter is not presented as a designer-written list of semantic criteria. That difference makes Naur's human-versus-rules partition worth reopening. But learning does not by itself place a present-day LLM outside the rule-determined pole. Acquisition history and resulting form are different properties: a decision tree can be induced from examples yet remain an explicit finite rule set.

Any assessment must therefore distinguish at least three levels:

- **Human-readable criteria.** Can a person state a compact semantic rubric that reproduces the judgments?
- **Finite formal implementation.** Do model state and an inference procedure formally determine the system's outputs?
- **Computability.** Does an effective procedure exist for producing those outputs?

Naur writes about criteria that cannot be formulated and judgments outside what rules can determine, but the essay does not say which description level matters for a learned implementation. On a broad reading of *rules*, a formally implemented model remains on the machine pole even when nobody can extract a compact semantic rubric from its parameters. On a narrower reading tied to expressible semantic criteria, the implementation may fail to express the criterion that makes a particular judgment apt. Even then, that failure does not show that the system possesses a program's theory.

A current LLM is therefore a challenge case, not a counterexample that settles the argument. Showing that it holds a theory requires evidence of the capacities Naur names, not merely the fact that it learned from examples.

## The transfer cases still impose three tests

Naur's compiler case shows a bounded transfer failure. A motivated successor group had the full program text, annotated sources, and extensive written design discussion, yet proposed extensions that the original group regarded as structure-destroying patches. The original group could instead propose simple changes framed within the existing structure. The case shows that the supplied artifact package did not convey enough program-specific understanding to this successor group. It does not test every possible rationale package, training route, or interpreter.

Read alongside Naur's account of theory possession, the case suggests three necessary tests for any claim that an interpreter-plus-artifact composite holds a program's theory. These tests are not sufficient conditions:

- **Program-specific acquisition.** General competence in language and the world is not the theory of a particular program. The composite must acquire that program's mapping, justification, and modification judgments. The tested artifacts did not enable the successor group to do so.
- **Provision of premises the interpreter cannot regenerate.** If coherent modification depends on a decision premise that the interpreter cannot recover from the implementation and general knowledge, the artifact package or another component must supply it. The recovery test in [design rationale must preserve decision premises its interpreter cannot regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md) identifies such premises. Naur's case establishes the failure of one supplied package, not of every retained-rationale design.
- **Dispositional reliability.** Naur ties a program's life to a team that remains in control and can answer later demands. One coherent extension may be lucky or memorized; theory possession requires a reliable capacity across occasions.

Whether a current LLM-plus-artifact system passes these tests is an empirical question. The logical conclusion is narrower: Naur's rule-inexpressibility argument cannot settle human exclusivity without an independently warranted premise that excludes every eligible nonhuman theory-holder.

---

Relevant Notes:

- [Programming as Theory Building](../sources/programming-as-theory-building.ingest.md) — abstracted-from: supplies the Ryle regress, the inexpressibility and human-binding claims, the human/machine passages, and the bounded compiler-transfer case; the additional-premise diagnosis is this note's reading
- [Attempted recovery identifies informational gaps, not provenance or authority](./documentation-generates-the-system-rather-than-describing-it.md) — grounds: why Naur's failed transfers show that content was missing from the supplied artifacts, not that program theory is inexpressible in principle
- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](./theory-mediated-self-improvement-needs-interpretation-and-retention.md) — extends: proposes the interpreter/retention division whose Naur premise must be read with this note's narrower logical result
