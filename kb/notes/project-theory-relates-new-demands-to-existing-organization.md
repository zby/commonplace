---
description: "For open-ended modification, project-theory possession includes relating a new demand to existing responsibilities before parallel structure becomes the default; an explicit assimilation branch may counter additive coding-agent patches"
type: kb/types/note.md
traits: [title-as-claim]
tags: [foundations, self-improving-systems]
---

# Project-theory possession requires comparing new demands with existing organization

Status: conjecture — the bearer test is derived from Naur; the coding-agent diagnosis and corrective mechanism remain to be tested.

For open-ended software modification, understanding a requested behavior is not enough. A theory-holder must also determine how the demand relates to facilities the program already has, what purpose those facilities serve, and whether their responsibility should be reused, generalized, split, or replaced. Moving directly from a demand to a local implementation makes additive structure the easy default: a new branch, wrapper, type, file, layer, workflow, or exception can satisfy immediate checks while duplicating a responsibility already present elsewhere.

Naur's compiler case is a transfer failure of this kind. The successor group had source code, annotations, design discussion, and advice, yet proposed extensions the original group regarded as patches that damaged the compiler's structure; the original group could frame simpler changes within the existing organization. As [Naur's bearer argument](./naur-equates-machine-execution-with-formulated-criteria.md) shows, the case does not prove that program theory is inexpressible. It supplies a functional test: can the modifier relate a new demand to the existing program rather than merely attach working behavior to it?

## Additive patching is a symptom, not a diagnosis

A new component can be correct. The failure is parallel structure added without establishing why the current organization cannot carry the demand. A theory-bearing process should be able to state which existing responsibility owns the demand and how it should change, why reuse would violate an invariant or conflate distinct responsibilities, or why the current responsibility model itself is wrong.

Repeated additions that cannot answer this question are evidence that project theory is not controlling the modification path. They do not establish why. Missing context, retrieval failure, a locally conditioned proposal, premature stopping after tests pass, failure to generate move, merge, or delete alternatives, or selection that favors a small edit radius can produce the same result.

## A candidate fix is an assimilation branch in modification search

Retained project theory can help only if it changes search before an addition is accepted. The minimum candidate mechanism is:

```text
new demand
  -> retrieve purposes, responsibilities, boundaries, and invariants
  -> locate the closest existing facilities
  -> compare assimilation, revision, and new-responsibility hypotheses
  -> make a provisional change
  -> test local behavior and later structural consequences
  -> retain, consolidate, backtrack, or revise the theory
```

This is search control, not a prohibition on new structure. The process should keep at least two explanations live: the demand belongs to an existing responsibility, so existing machinery should be modified or generalized; or the demand exposes a genuinely distinct responsibility, so new structure is warranted.

The project theory supplies the map and rationale. A structural operator repertoire supplies modification, movement, consolidation, splitting, and deletion candidates. Tests and later demands can defeat the initial choice. A checklist without project-specific state may merely produce a rationale after the same additive decision, while a stored theory that is not retrieved or does not change the candidate set is inert.

## What would support the conjecture

A matched test should use sequences in which an additive patch can pass the first local checks but later requirements expose duplicated ownership or conflicting paths. Compared with the same model and information without an operative theory surface, the theory-guided condition should more often identify the existing responsibility before editing, modify or generalize existing machinery when appropriate, justify genuinely new structure, consolidate mistaken parallel paths, and revise its responsibility model after delayed evidence.

The outcome is not minimality by itself. A correct assimilation may require a broad refactor, and a correct extension may require a new component. The relevant result is lower later recovery cost and fewer unresolved responsibility conflicts, with the chosen structure explained by the program's purposes and organization.

The conjecture loses if explicit theory only adds explanations after unchanged additive choices, if a lightweight assimilation prompt works equally well without retained project state, or if direct structural search performs better at comparable total cost.

## Scope

- Current reports of coding agents adding structure are candidacy evidence, not prevalence evidence that current agents generally lack project theory. Prospective traces and interventions are needed.
- The symptom does not uniquely locate the failure. Acquisition, representation, retrieval, candidate generation, stopping, and selection are separate possible causes.
- Project theory may be implicit or distributed. Natural-language theory is the addressable realization under test, not the only possible carrier.
- The target is open-ended coherent modification. Fully specified changes with complete local oracles may not need this machinery.

## Open Questions

- Which retained content is necessary: responsibility ownership, design rationale, domain mapping, change history, or some combination?
- Can an agent construct and revise that state from the repository, or must an operator bootstrap it?
- How can duplicated responsibility be detected without freezing the current decomposition?
- Does the intervention need a separate structural critic, or can the modifying agent perform both roles reliably?
- What horizon distinguishes coherent assimilation from an initially tidy but later brittle refactor?

---

Relevant Notes:

- [Naur binds program theory to humans by equating machine execution with formulated criteria](./naur-equates-machine-execution-with-formulated-criteria.md) — grounds: supplies the compiler transfer case and the requirement to relate new demands to existing facilities
- [Holding a program theory means sustaining coherent search under delayed feedback](./program-theory-sustains-search-under-delayed-feedback.md) — extends: places assimilation inside fallible search, backtracking, recovery, and theory revision
- [Design rationale must preserve decision premises its interpreter cannot regenerate](./design-rationale-must-preserve-unregenerable-decision-premises.md) — grounds: identifies program-specific premises that source code and general competence may not recover
- [Theory mediation can coordinate heterogeneous factory development](./theory-mediation-can-coordinate-heterogeneous-factory-development.md) — mechanism: supplies the explicit natural-language surface proposed to coordinate changes across machinery
- [Open-ended improvement allocates search before evaluation](./open-ended-improvement-allocates-search-before-evaluation.md) — grounds: explains why assimilation must enter the candidate set before local checks select an additive patch
- [Learning inside a fixed decomposition inherits its mistakes](./learning-inside-a-fixed-decomposition-inherits-its-mistakes.md) — extends: explains why a candidate repertoire limited to local additions cannot repair a mistaken responsibility structure
- [A search controller is tested by what it brings to stronger evaluation](./a-search-controller-is-tested-by-what-it-brings-to-stronger-evaluation.md) — enables: supplies the downstream comparison for the proposed assimilation branch
