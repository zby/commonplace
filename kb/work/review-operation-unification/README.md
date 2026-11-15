# Unify the review operations

Posed by the operator on 2026-11-14. This is the first, deliberately bounded application of the [live-operation-to-controlled-testing workshop](../stochastic-operation-testing/README.md). The operator authorized implementation on 2026-11-15 with “ok - commit - then go on”. The first slice includes fixtures; paid evaluation remains separately authorized. See [implementation status](./implementation.md) for verification and the completed cutover.

## Goal and scope

Give review operations shared execution, provenance, freshness and fixture support so each can be run and tested alone. Start with this subset to keep the work simple; a general operation framework is not a prerequisite.

The [improvement-procedure proposal](../../reference/proposals/one-improvement-procedure-over-atomic-instructions.md) supplies the intended atom contract: a typed instruction, file inputs, a typed result identified by target and operation, and standalone execution on a note or across a collection. Sharing machinery does not require sharing judgments or forcing reports into pass/warn/fail.

**In scope:** the review families below, their input/output contracts, common bookkeeping and controlled reconstruction. **Out of scope:** edits, stops, improvement variants, full-pass/revise redesign, authority grades, general improvement-run types and dynamic coordinator dispatch. Existing consumers must keep working. Calibrating individual judgments belongs to their evaluation work, not this design investigation.

## Document ownership

| File | Owns |
|---|---|
| [Execution design](./execution-design.md) | Selected common behavior: Workjig, provenance, run-local inputs, freshness and fixtures |
| [Plan](./plan.md) | Evidence investigation, remaining decisions, operator checkpoints and execution limits |
| [Command sketch](./operation-command-sketch.md) | Design sketch; the CLI and reference now own the implemented interface |
| [Decisions](./decisions.md) | Family/form recommendations and consumer evidence; operator authorized design continuation after the atoms-only correction |
| [Execution contract](./execution-contract.md) | Authorized record ownership, first implementation slice, cutover and acceptance tests |
| [Implementation status](./implementation.md) | Acceptance evidence, implementation limits and completed cutover |

## Current candidate pool

Baseline inspected on 2026-11-14. The [overlap map](../decision-lifecycle-evidence/review-operation-overlaps.md) is a starting hypothesis about duplication, not proof that operations can be merged.

| Family | Current execution and result |
|---|---|
| 40 catalog gates in seven bundles | Typed [review-gate](../../types/review-gate.md) criteria; batch execution; Python-checked verdict result files |
| Type and collection conformance | Wrappers apply the applicable contracts; same batch and result machinery |
| [Compression bundle](../../instructions/compression-bundle/README.md) | Four checks plus synthesis; standalone instruction and full-pass method; deliberately outside the gate catalog |
| [Critique](../../instructions/critique-note.md) | Standalone report instruction **and** a report-kind `critique` lens through the review command and shared result store |
| [Composition friction](../../instructions/composition-friction-gate.md), [premise decomposition](../../instructions/premise-decomposition-gate.md) | Standalone report instructions and full-pass methods |
| [Connect](../../instructions/cp-skill-connect/SKILL.md) | Discovery skill with a typed connect report; also used by the full pass |
| [Higher-order check](../higher-order-check-evaluation/README.md) | Experimental criterion wordings executed as gates; result needs include proposal kind and force |

That baseline's shared result format was checked by Python, not a registered type. The implementation now uses [review-result](../../types/review-result.md); old current results and packets are archived, and historical runs remain citable in place. Typed criteria do not establish typed-result conformance. Likewise, an existing report type does not establish that its operation already meets the shared execution contract.

## Binding premises and compatibility

- **Reviews first.** Do not redesign a consuming improvement procedure to make an operation fit. Record incompatibilities and return them to the operator.
- **Stability is assumed reachable.** The operator permits designs to rest on review verdicts becoming stable. Present instability identifies calibration work; it does not reopen that premise. Stability does not establish correctness.
- [ADR 127](../../reference/adr/127-review-runs-as-workflows-over-result-files.md) supplies the existing file-backed runtime. [ADR 131](../../reference/adr/131-conformance-reviews-leave-titles-and-descriptions-to-their-gates.md) reserves title and description properties for their gates. [ADR 082](../../reference/adr/082-grounding-is-bounded-on-the-artifact-by-unquoted-sources.md) keeps concept-attribution and misleading-link-text distinct.
- The shared store currently replaces the result for a note/criterion pair. Experimental observations must survive that replacement; distinct criterion ids separate wordings but not repeated trials of one wording.
- The [review system](../../reference/README-REVIEW-SYSTEM.md) requires independent operation evaluation before composition is trusted. A form change alone establishes no review-quality improvement.

## Coordination

The parent testing workshop owns general methods and trial evidence. [Review on Workjig](../review-on-workjig/README.md) supplies the existing engine work; coordinate authorized changes rather than create a parallel runtime. [Decision lifecycle and evidence](../decision-lifecycle-evidence/README.md) holds the overlap map, retention decisions and improvement-run drafts. [Higher-order check evaluation](../higher-order-check-evaluation/README.md) owns that check's wording and calibration; consume its result requirements here. The [gate calibration proposal](../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) is a methodological input, not a requirement to calibrate every gate in this workshop.

## Completion

The design phase ends with operator dispositions for family membership/forms, shared execution and result requirements, the first implementation slice, and its acceptance tests. Unresolved semantic overlaps may stay separate with a stated reason.

The workshop closes after separately authorized implementation establishes the admitted review subset and its required types, or the operator explicitly declines the proposed changes. Preserve existing consumers, extract adopted decisions into the appropriate ADR/types/reference and update the improvement proposal's atom table where needed. Then remove the workshop and its active-list entry. Neither closure nor implementation requires extending the mechanism to edits or stops.
