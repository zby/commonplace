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
