---
description: "How to investigate a rule when local checks pass but outcomes deteriorate, without mistaking an integration defect for a bad requirement."
type: types/note.md
traits: [title-as-claim]
tags: [learning-theory, constraining, llm-reliability]
---

# Operational signals that a component is a relaxing candidate

A component may do exactly what its specification requires and still restrict useful behavior: [meeting a requirement does not establish that it serves the objective](./exact-implementation-does-not-validate-a-requirement.md). The signals below suggest where to investigate. They do not by themselves tell us to replace the component.

## Signals that a requirement may not fit its use

**Brittleness under paraphrase or reordering.** If the component breaks when inputs are rephrased, reordered, or padded with irrelevant content, it's relying on surface patterns rather than capturing the underlying structure. Metamorphic tests can detect this systematically. Rabanser et al.'s [agent reliability study](https://arxiv.org/pdf/2602.16666) operationalises a related signal as R_prompt — prompt robustness — and finds it is the key differentiator among robustness sub-dimensions: models handle genuine faults gracefully yet remain vulnerable to surface-level instruction rephrasings. [Ma et al.'s PromptSE framework](../sources/prompt-stability-code-llms-emotion-personality-variations.ingest.md) tests prompt sensitivity with semantically equivalent emotion/personality variants of HumanEval tasks across 14 models (14,760 variants). This measures sensitivity to surface form under fixed functional requirements; it does not determine whether the cause is a badly-fitting theory or limited model capacity. In the pinned [Mazur position-bias benchmark](../sources/position-bias.ingest.md), 27 judge models evaluated 193 sibling-edit story pairs in both display orders, and the median model changed its canonical winner in 44.8% of decisive swapped-order pairs. This measures the signal on the evaluator, not the task-solver. None of these sources connect the brittleness signal to the fixed-artifact distinction, but we interpret the findings as evidence that paraphrase brittleness is a measurable and prevalent signal — exactly what you'd expect if many agent components encode theories about input format rather than specifications of meaning.

**Isolation-vs-integration gap.** If unit tests pass but integration fails, trace the value across the interface. A correct result ignored by its consumer points to a handoff defect, not necessarily a bad rule. Passing the tested cases does not exclude an implementation bug on other inputs.

**Process constraints rather than outcome constraints.** If a rule requires a particular sequence, ask whether that sequence is itself obligatory or merely the current way to obtain a result. Only in the latter case is an alternative sequence that works evidence for relaxing the rule.

**Hard to specify failure conditions.** Name an outcome that would count against the rule. If none is identifiable, its benefit will be hard to assess even if every step is easy to verify.

**High sensitivity to distribution shift.** If the component works on training/development data but degrades on slightly different inputs, it has overfit to a particular theory of what inputs look like.

**Composition failure** (late-stage). After checking implementation, interfaces and operating conditions, compare alternative requirements on the same task. If relaxing the rule improves the outcome, that is evidence against enforcing it in those conditions.

## Using the signals

These signals guide investigation; they are not a score for correctness or a measure of how expensive the local check is.

When signals fire:
- Keep the component in a **replaceable slot** — clean interface, swappable implementation.
- Invest in **integration tests** over unit tests for this component.
- Maintain **alternative candidates** (different decompositions, learned replacements) so relaxing is cheap when the time comes.

When signals don't fire:
- No signal is not evidence that stricter rules would improve outcomes. Add tests for known local requirements; assess any proposed restriction on the cases it would exclude.

## Open questions

- Can these signals be measured automatically, or do they require human judgment? Brittleness and distribution sensitivity seem measurable; "hard to specify failure" seems inherently subjective.
- Is there a feedback loop? Investing in integration tests for suspected vision-features might *itself* reveal whether the theory is wrong, accelerating the relaxing decision.

---

Relevant Notes:

- [Exact implementation does not validate a requirement against its objective](./exact-implementation-does-not-validate-a-requirement.md) — grounds: local conformance and fitness for purpose need different checks.
- [oracle-strength-spectrum](./oracle-strength-spectrum.md) — extends: signals shift confidence about where a component sits on the oracle strength gradient
- [spec-mining-as-codification](./spec-mining-as-codification.md) — complement: spec mining is the action when signals don't fire (codify harder); relaxing signals detect when to reverse it
- [codification-and-relaxing-navigate-the-bitter-lesson-boundary](./codification-and-relaxing-navigate-the-bitter-lesson-boundary.md) — operationalizes: these signals are the detection mechanism for the codify/relax cycle
- [Code and prompts can share a unified interface so programmers choose between them as systems evolve](./a-unified-interface-lets-programmers-choose-prompts-or-code.md) — enables: a unified interface keeps acting on relaxing signals local to the binding, swapping a brittle coded rule back to a prompt without changing callers
- [error-correction-works-above-chance-oracles-with-decorrelated-checks](./error-correction-works-above-chance-oracles-with-decorrelated-checks.md) — enables: metamorphic checks are the operational mechanism for measuring the paraphrase brittleness signal automatically
- [changing-requirements-conflate-genuine-change-with-disambiguation-failure](./changing-requirements-conflate-genuine-change-with-disambiguation.md) — exemplifies: disambiguation failure surfacing late is an instance of Signal 4 (hard to specify failure conditions)
- [memory-management-policy-is-learnable-but-oracle-dependent](./memory-management-policy-is-learnable-but-oracle-dependent.md) — exemplifies: AgeMem confirms memory composition policy exhibits Signal 3 and Signal 4 in a concrete system
- [Rabanser et al. reliability study](https://arxiv.org/pdf/2602.16666) — evidence (interpreted): R_prompt metric shows paraphrase brittleness is the key differentiator among robustness sub-dimensions; we interpret this as support for the paraphrase brittleness signal, though the source doesn't connect to the fixed-artifact distinction
- [Mazur position-bias benchmark](../sources/position-bias.ingest.md) — **evidence**: judge-layer measurement of the brittleness signal; the median of 27 judge models changed its canonical winner in 44.8% of decisive swapped-order pairs, while Mistral Large 3 showed an opposite-direction second-position bias — model heterogeneity that this note treats as relevant to decorrelation (repository snapshot; decisive-pair statistic; sibling-edit surface)
