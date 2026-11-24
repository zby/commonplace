---
description: "Aamodt and Plaza distinguish what to keep from an episode from how to retrieve it later, a precedent for selective retention in agent memory."
source: https://www.idi.ntnu.no/~agnar/publications/aicom-94.pdf
captured: "2026-11-21"
capture: pdftotext
capture_scope: full-source
genre: scientific-paper
snapshot_sha256: f9b6860587fe06923f2e8b0bdf6611c1e3abe089ba740b38d2faaf1fddd71805
ingested: "2026-11-21"
occasion: "Which parts of deliberative learning, if any, have precedents in case-based reasoning and its retention judgments?"
type: types/ingest-report.md
domains: [case-based reasoning, case retention, failure memory, derivational reuse]
tags: [improvement-loop, learning-theory, self-improving-systems]
learning_claims: true
---

# Ingest: Case-Based Reasoning (Aamodt and Plaza, 1994)

## Classification

A methodological survey published in *AI Communications*. Both authors had built systems in the field: Agnar Aamodt worked on CREEK and Enric Plaza on case-based learning and planning. They compare methods from their own and other research groups.

## Summary

Aamodt and Plaza describe case-based reasoning as a cycle: retrieve a relevant earlier case, reuse its solution or the method that produced it, test and if necessary repair the proposed solution, and retain what might help with a later problem. Their second view separates each task from the methods available to perform it. One system may copy the class of the nearest example; another may use a causal model to explain why a seemingly different case applies. Retention likewise ranges from recording an example to preserving the reason a plan failed or changing which features retrieve an existing case. The [survey](https://www.idi.ntnu.no/~agnar/publications/aicom-94.pdf) illustrates these choices with research systems and fielded applications.

## Contribution assessment (our opinion)

The most useful advance appears to be a common basis for comparing systems, not a new reasoning algorithm. Asking separately what a later problem must retrieve and what it can reuse exposes a dependency: replaying a method requires a different record from copying an answer. The examples make that distinction inspectable across systems. They do not establish which way of organizing experience works best.

## Quotes

No source quotes have been retained yet.

## Connections Found

The survey provides a historical precedent for the judgment in [Use trace extraction as meta-learning](../theory/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) that a new episode need not produce a new memory item. It adds a precise alternative: when an old case was a poor match, the useful change may be to the cue that retrieved it, not to the solution it records. That is a precedent for deciding *what changes* after experience, not proof that the system deliberates about that choice.

## Learning Claims (our opinion)

CHEF tests a proposed recipe in a simulator, explains why a goal was missed, and uses the explanation both to repair the plan and to recognize circumstances that threaten later plans. Against the [theory builder](../theory/definitions/theory-builder.md) criteria, the account identifies localized content (plan steps and causal explanations) and describes its consumption (the repair adds steps to counter the diagnosed cause). The explanation criticizes a particular plan on its content, not just on its score. The failure memory also supplies an iteration mechanism: a later planning episode can anticipate the failure before executing the plan. Thus the criticism persists across problems by design. The account does not show CHEF questioning the simulator that supplied the verdict.

PATDEX illustrates a different change: success or failure adjusts weights linking available features to diagnoses. That can alter later retrieval without a stated criticism of the case or the feature vocabulary. Reweighting cannot itself introduce a missing feature. In both examples the survey identifies a route to improved future action; it does not isolate an improvement on later problems caused by retaining the explanation or updating the weights.

## Extractable Value

1. **Separate four retention judgments.** Section 8 distinguishes what information to keep, in what form, under which retrieval cues, and how it changes existing memory. A failed attempt, for example, may warrant its own failure case or an explanation attached to the problem case. These are precedents for selective retention; they can also be implemented by fixed rules. [quick-win]
2. **Separate provisional use from endorsement.** When real-world feedback is delayed, the authors allow a case to be retrieved before its solution has been evaluated, provided it is marked accordingly. This gives the KB a concrete example of why availability and evidential status need not advance together. [quick-win]

## Limitations (our opinion)

The task hierarchy assigns decisions to a reasoner without requiring it to compare alternative retention policies or give reasons for choosing one. Even the engineering cost estimate compares a fielded decision-support system with earlier manual procedures, not different retention methods on the same cases. Neither the taxonomy nor that comparison shows an advantage for deliberation over a fixed retention rule.

## Recommended Next Action

Add a historical comparison to [Use trace extraction as meta-learning](../theory/agent-memory-requirements/use-trace-extraction-as-meta-learning.md) distinguishing the CBR precedent for choosing what to retain and how to retrieve it from the stronger claim that a learner deliberates about its retention policy.
