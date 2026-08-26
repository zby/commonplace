---
description: "Naur's theory-building view makes maintainability depend on situated design understanding while bounding what retained rationale alone can transfer"
source: https://ingenieria-de-software-i.github.io/assets/bibliografia/programming-as-theory-building.pdf
captured: "2026-08-24"
capture: pdf-read
genre: conceptual-essay
snapshot_sha256: 4410928aa7247051a6f65f1fb823c0c57aee3d6394455e592afd1262c1975a9c
ingested: "2026-08-24"
type: kb/sources/types/ingest-report.md
domains: [programming-methodology, design-rationale, maintainability, knowledge-transfer]
---

# Ingest: Programming as Theory Building

## Classification

This is a conceptual essay: an invited 1984 keynote published in 1985 that develops a philosophical account from two reported software-maintenance cases rather than a controlled evaluation.
Author: Peter Naur writes from Copenhagen University's computing institute and draws on experience he had directly or received from people with firsthand contact with the systems discussed. That supplies practitioner and theoretical signal about large-program maintenance, not comparative empirical evidence.

## Summary

Naur argues that programming primarily builds a theory held by programmers: a situated capacity to map between real-world affairs and program structure, justify why the program is designed as it is, and respond constructively to novel modification demands. Code, specifications, and documentation are secondary products that cannot by themselves convey the similarity judgments this capacity requires. On this account, a program remains alive while a theory-bearing team controls its changes; transfer requires guided work with people who possess the theory; and reconstructing the original theory from artifacts alone is strictly impossible and may cost more than rewriting. Prescribed methods can supply examples, techniques, and educational prompts, but cannot mechanically determine the right actions or their order. The essay is a primary conceptual source for design-knowledge transfer and future-change-relative maintainability, though its strongest impossibility claims go beyond its anecdotal evidence.

## Quotes

- **Source extract (verbatim):** In terms of Ryle’s notion of theory, what has to be built by the programmer is a theory of how certain affairs of the world will be handled by, or supported by, a computer program.
  - **Source location:** Section 4, “The theory to be built by the programmer”, opening sentence
- **Source extract (verbatim):** By far the largest part of the world aspects and activities will of course lie outside the scope of the program text, being irrelevant in the context. However, the decision that a part of the world is relevant can only be made by someone who understands the whole world. This understanding must be contributed by the programmer.
  - **Source location:** Section 4, “The theory to be built by the programmer”, capability 1 (mapping between world affairs and program text)
- **Source extract (verbatim):** The design of how a modification is best incorporated into an established program depends on the perception of the similarity of the new demand with the operational facilities already built into the program. The kind of similarity that has to be perceived is one between aspects of the world. It only makes sense to the agent who has knowledge of the world, that is to the programmer, and cannot be reduced to any limited set of criteria or rules
  - **Source location:** Section 4, “The theory to be built by the programmer”, capability 3
- **Source extract (verbatim):** The programmer having the theory of the program can explain why each part of the program is what it is, in other words is able to support the actual program text with a justification of some sort.
  - **Source location:** Section 4, “The theory to be built by the programmer”, capability 2 (justification of each part of the program)
- **Source extract (verbatim):** Indeed, the very notion of qualities such as simplicity and good structure can only be understood in terms of the theory of the program, since they characterize the actual program text in relation to such program texts that might have been written to achieve the same execution behaviour, but which exist only as possibilities in the programmer’s understanding.
  - **Source location:** Section 5, “Problems and costs of program modifications”, final sentence
- **Source extract (verbatim):** A main claim of the Theory Building View of programming is that an essential part of any program, the theory of it, is something that could not conceivably be expressed, but is inextricably bound to human beings.
  - **Source location:** Section 6, “Program Life, Death and Revival”, opening sentence
- **Source extract (verbatim):** On the Theory Building View the primary result of the programming activity is the theory held by the programmers. Since this theory by its very nature is part of the mental possession of each programmer, it follows that the notion of the programmer as an easily replaceable component in the program production activity has to be abandoned.
  - **Source location:** Section 8, “Programmers’ Status and the Theory Building View”, first paragraph, closing argument
- **Source extract (verbatim):** What I am concerned with is the activity of matching some significant part and aspect of an activity in the real world to the formal symbol manipulation that can be done by a program running on a computer.
  - **Source location:** Section 2, “Programming and the programmers’ knowledge”, first paragraph (definition of programming)
- **Source extract (verbatim):** It may be noted that this notion of intelligence does not rely on any notion that the intelligent behaviour depends on the person’s following or adhering to rules, prescriptions, or methods. On the contrary, the very act of adhering to rules can be done more or less intelligently; if the exercise of intelligence depended on following rules there would have to be rules above how to follow rules, and about how to follow the rules about following rules, etc. in an infinite regress, which is absurd.
  - **Source location:** Section 3, “Ryle’s notion of theory”, second paragraph on intelligent behaviour (Ryle’s infinite-regress argument)
- **Source extract (verbatim):** The dependence of a theory on a grasp of certain kinds of similarity between situations and events of the real world gives the reason why the knowledge held by someone who has the theory could not, in principle, be expressed in terms of rules. In fact, the similarities in question are not, and cannot be, expressed in terms of criteria, no more than the similarities of many other kinds of objects, such as human faces, tunes, or tastes of wine, can be thus expressed.
  - **Source location:** Section 3, “Ryle’s notion of theory”, final paragraph
- **Source extract (verbatim):** The point is that the kind of similarity that has to be recognized is accessible to the human beings who possess the theory of the program, although entirely outside the reach of what can be determined by rules, since even the criteria on which to judge it cannot be formulated.
  - **Source location:** Section 5, “Problems and costs of program modifications”, paragraph on the determination of similarity in a modification
- **Source extract (verbatim):** Another related view is that human beings perform best if they act like machines, by following rules, with a consequent stress on formal modes of expression, which make it possible to formulate certain arguments in terms of rules of formal manipulation. Such views agree well with the notion, seemingly common among persons working with computers, that the human mind works like a computer.
  - **Source location:** Section 8, “Programmers’ Status and the Theory Building View”, first paragraph, on the more prevalent view of programming
- **Source extract (verbatim):** get a contract with group A that they will get support in the form of full documentation, including annotated program texts and much additional written design discussion, and also personal advice.
  - **Source location:** Section 2, “Programming and the programmers’ knowledge”, Case 1 (the compiler), description of the support group B received
- **Source extract (verbatim):** In several major cases it turned out that the solutions suggested by group B were found by group A to make no use of the facilities that were not only inherent in the structure of the existing compiler but were discussed at length in its documentation, and to be based instead on additions to that structure in the form of patches that effectively destroyed its power and simplicity. The members of group A were able to spot these cases instantly and could propose simple and effective solutions, framed entirely within the existing structure. This is an example of how the full program text and additional documentation is insufficient in conveying to even the highly motivated group B the deeper insight into the design, that theory which is immediately present to the members of group A.
  - **Source location:** Section 2, “Programming and the programmers’ knowledge”, Case 1 (the compiler), review of group B’s proposed extensions
- **Source extract (verbatim):** For a new programmer to come to possess an existing theory of a program it is insufficient that he or she has the opportunity to become familiar with the program text and other documentation. What is required is that the new programmer has the opportunity to work in close contact with the programmers who already possess the theory, so as to be able to become familiar with the place of the program in the wider context of the relevant real world situations and so as to acquire the knowledge of how the program works and how unusual program reactions and program modifications are handled within the program theory.
  - **Source location:** Section 6, “Program Life, Death and Revival”, second paragraph, on how a new programmer acquires the theory
- **Source extract (verbatim):** The most important educational activity is the student’s doing the relevant things under suitable supervision and guidance.
  - **Source location:** Section 6, “Program Life, Death and Revival”, second paragraph, on the educational parallel
- **Source extract (verbatim):** The relevant experience from the way this kind of system is handled concerns the role and manner of work of the group of installation and fault finding programmers.
  - **Source location:** Section 2, “Programming and the programmers’ knowledge”, Case 2 (the real-time production monitoring system), identification of the group whose work is at issue
- **Source extract (verbatim):** Second, when diagnosing a fault these programmers rely almost exclusively on their ready knowledge of the system and the annotated program text, and are unable to conceive of any kind of additional documentation that would be useful to them.
  - **Source location:** Section 2, “Programming and the programmers’ knowledge”, Case 2, second reported fact
- **Source extract (verbatim):** During the program life a programmer team possessing its theory remains in active control of the program, and in particular retains control over all modifications. The death of a program happens when the programmer team possessing its theory is dissolved. A dead program may continue to be used for execution in a computer and to produce useful results. The actual state of death becomes visible when demands for modifications of the program cannot be intelligently answered.
  - **Source location:** Section 6, “Program Life, Death and Revival”, first paragraph, on program life and the visibility of death
## Connections Found

The essay is a primary conceptual anchor for the KB's distinction between retained state and usable design understanding. Its compiler handoff and fault-diagnosis cases are evidence for [Attempted recovery identifies informational gaps, not provenance or authority](../notes/documentation-generates-the-system-rather-than-describing-it.md): extensive code and documentation did not supply decision-relevant understanding, while that note correctly limits the inference to what the tested source set failed to carry. Naur also supports [Use tests a decomposition locally; retained rationale is what makes transfer testable](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) by showing that visible structure underdetermines why one extension is natural and another is a patch. At the same time, his successful group-to-group guidance is a counterpoint to any document-only account of transfer: live apprenticeship can convey practical capacity even when it does not leave an independently checkable record.

For [Brainstorming: maintainability oracles for agentic development](../notes/brainstorming-maintainability-oracles-for-agentic-development.md), Naur supplies a technical basis for treating maintainability as relational: two behaviorally correct changes differ according to how they connect new world demands to the program's existing design theory. [Why LLMs can't make your code simpler](why-llms-cant-make-your-code-simpler.ingest.md) is the closest source comparison because it applies that account to LLM-generated code; Naur provides the primary formulation and also makes clear that the theory-building view includes method, education, team continuity, and modification judgment, not just simplicity.

## Extractable Value

1. **Program theory has three assessable capabilities** -- A maintainer who possesses it can map both ways between world affairs and artifact structure, justify design choices, and incorporate a novel demand by recognizing relevant similarities. This gives agent-operated KBs a richer evaluation target than factual recall: whether supplied context supports explanation, justification, and coherent change. [deep-dive]
2. **Artifact retention and guided participation are complementary transfer channels** -- Retained rationale makes premises and rejected alternatives durable and testable; close work with a current theory-holder can teach situated judgments that the artifact does not exhaust. The distinction bounds documentation claims without treating incomplete externalization as useless. [quick-win]
3. **Behavioral correctness does not discriminate coherent modification from patching** -- Multiple edits can satisfy the same requested behavior while differing in how naturally they extend the existing design. A maintainability oracle therefore needs evidence about design forces and anticipated changes, not only tests or structural metrics. [experiment]
4. **Execution continuity is weaker than maintenance continuity** -- Naur's life/death distinction identifies a system that still runs but can no longer answer new demands intelligently. Adapted cautiously, this is a useful diagnostic for an agent-operated KB whose artifacts remain readable while the rationale needed for coherent revision has been lost. [deep-dive]
5. **Methods should be evaluated as theory-building supports, not complete generators** -- Examples, notations, checks, and work rules may improve an agent's repertoire without fixing the correct sequence for every case. Commonplace can test instructions by whether agents explain and adapt their choices in new cases, rather than inferring success from procedural conformance alone. [experiment]

## Limitations (our opinion)

The essay generalizes from two reported cases without controlled comparisons of documentation quality, team continuity, task difficulty, modification outcomes, or cost. Those cases show that the supplied artifacts were insufficient for those successor programmers; they do not establish that every possible artifact set must fail. Poor selection, organization, practice, or access could explain some of the gap. The narrower inference in [Attempted recovery identifies informational gaps, not provenance or authority](../notes/documentation-generates-the-system-rather-than-describing-it.md) is better supported than Naur's claim of in-principle inexpressibility.

The central construct is also difficult to vary: the theory is recognized through the ability to explain, justify, and modify well, while failures can be attributed to not possessing it. The essay supplies no independent measure that separates theory possession from experience, domain familiarity, or documentation usability. Its claim that revival is strictly impossible further conflates recreating the original programmers' mental possession with building a different but sufficiently compatible understanding; no revival-versus-rewrite comparison tests the recommendation to start over. Likewise, the critique of universal methods does not show that explicit procedures are ineffective within bounded tasks. It shows at most that rules and documents are not a complete mechanical substitute for situated judgment.

## Recommended Next Action

Revise [Use tests a decomposition locally; retained rationale is what makes transfer testable](../notes/use-tests-a-decomposition-locally-rationale-makes-transfer-testable.md) to distinguish durable, independently testable rationale from guided theory acquisition through work with a current theory-holder, preserving the note's documentary claim while no longer treating writing as the only way understanding can cross between people.

---

Abstracted into:

- [Theory-mediated self-improvement needs both interpretation and retention from one substrate](../notes/theory-mediated-self-improvement-needs-interpretation-and-retention.md) — shifts Naur's human theory-holder into an LLM-plus-artifact system boundary while preserving the theory-building claim
- [Design rationale must preserve decision premises its interpreter cannot regenerate](../notes/design-rationale-must-preserve-unregenerable-decision-premises.md) — turns the three theory-holder capabilities into a one-way retention test: preserve the decision premises a fresh interpreter cannot faithfully recover from implementation, history, and general knowledge
- [A specific intent may out-yield local rationales, but contingent facts stay separate](../notes/specific-intent-may-out-yield-local-rationales-facts-stay-separate.md) — uses the justification capability and the counterfactual-design-space passage to conjecture an intent's per-token yield and to bound it with contingent fact
- [Naur binds program theory to humans by equating machine execution with formulated criteria](../notes/naur-equates-machine-execution-with-formulated-criteria.md) — separates the essay's argued inexpressibility claim from its human-binding conclusion, identifies the bridge as the equation of machine execution with formulated criteria (accurate for the programs of its time), and turns the transfer cases into tests on a text-plus-interpreter composite
