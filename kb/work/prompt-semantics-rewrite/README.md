# Prompt semantics rewrite: integration and remaining repairs

## Commission and current state

The operator commissioned the coherence audit and central rewrite on 2026-11-03, then requested integration of the parallel revisions on 2026-11-04. The purpose is to make the KB consistent with two accounts of prompting: programming in a model-defined language and executing English instructions through a fallible interpreter. Opacity remains relative to the inspection question, tools and budget.

The central rewrite is implemented. The latest integration review covers the 22 commits after `693ab4306` through `6ecdced41`, together with the generator/artifact correction to `automated-tests-for-text.md`, subsequently committed in `b69e7b478`. The parallel work largely supports the rewrite. It also repairs much of the dependent material that this session had planned to tackle next. Do not repeat those migrations.

Repair commits are not the same as reviewed closure. Several revised passages retain categorical claims that conflict with the central account. [The integration review](./integration-review-2026-11-04.md) records their exact scope and proposed repairs. The workshop remains open for those items and final acceptance checks.

## Settled direction

- A specified model package can define precise prompt-language semantics, including specified variation. Adoption fixes the governing reference; it does not establish adequacy to English requirements or affordable inspection.
- English can state a requirement and separately predict model-defined behavior. Conformance and predictive fidelity reverse the direction of assessment; neither follows from selecting an account. The fixed behavior-prediction burden remains, while English adjudication can add work.
- A caller, reviewer or stated conventions must settle the applicable English reading where a conformance judgment needs one. Explicitly permitted alternatives differ from an unsettled permission boundary. Graded satisfaction, disputed interpretation and missing evidence need different responses; no fuzzy-set machinery is adopted.
- Near-decomposability remains a candidate mechanism for affordable local inspection. Locating an intervention point does not establish that a repair preserves required invariants, and weak interactions can still break them.
- The technical spec-to-program use of projection has been replaced by [program refinement](../../theory/definitions/program-refinement.md). Unchecked generated artifacts are candidates. The relation is conditional on applicable interpretations and must preserve the specification's guarantees, including required termination. Composition does not automatically preserve refinement.
- Reference adoption, inspection cost, execution cost and the quality of correctness checks remain separate. Code extraction can improve some of them in a specified case; it is not the definition of codification.

The temporary instruction to retain projection pending parallel work has been superseded in the practices note and its brief. Do not restore it. Projection retains unrelated ordinary and technical senses elsewhere; see the [inventory](./projection-inventory.md).

## Disposition

The identifiers refer to the dated [coherence audit](../../reports/retained/prompt-semantics-coherence-audit-2026-11-03.md). That report remains a historical record; this table tracks current work.

| Item | Current disposition | Evidence / remaining work |
|---|---|---|
| F1 central argument | Rebuilt; latest additions compatible with our work | `aef13b709`, `d3a6459b0`, `e76d0972e`, `6ecdced41`; two accounts, English adjudication, disputed membership |
| F2 navigation | Main thesis repaired | Computational-model head uses the revised account; final gloss check remains |
| F3 testing | Practices rewrite and R1 correction implemented | `b4858b39b`, `a0f274dc7`, `693ab4306`, `263966e5c`; R1 now distinguishes a candidate implementation from its permitted behaviors. Generator/artifact correction in `automated-tests-for-text.md` and R1 committed in `b69e7b478` |
| F4 scoping | R2 corrected: frame means one invocation’s complete input; direct exclusion and checked selection rules | `7093080cd`, `5b53e7b18`; completed disposition in review R2 |
| F5 opacity and near-decomposition | Definition/necessity rollback and invariant distinction implemented | `a14b910e9`, `9d91230e1`, `f377f14ca`; broader invariant theory is parked separately |
| F6 partial evaluation | R3 corrected: candidate specialization and preservation obligations replace shared-medium identity | `acc843c5d`; review R3 |
| F7 verifiability | R4 corrected: examples compare requirements, retry costs and checking limits without ranking artifact kinds | `35daecae2`; review R4 |
| F8 extraction dependents | Repairs applied; several implications still need qualification | `fa55d03b0`, `406e44952`, `6ecdced41`; review R5 |
| Program-refinement terminology and backlinks | Migration applied; preserve latest interpretation and guarantee qualifications | `263966e5c`, `9d800927d`, `6c4fc3ea1`, `16c834161`, `3aed3acae`, `408b509a1`, `6ecdced41` |
| Earlier Tier 1 claim review | Four repairs applied | `fa55d03b0`, `d2751437d`, `4176fa06b`, `4b35dc051`; do not treat these commits as clearance of all surrounding prose |

## Current library homes

- [Main prompting argument](../../theory/prompting-changes-failure-diagnosis-with-the-semantic-reference.md): reference choice and failure diagnosis.
- [English approximation](../../theory/english-can-approximate-a-model-defined-prompt-language.md): localized predictions, their assessment criteria and the proposed description-length residual mapping.
- [Unsettled instruction composition](../../theory/clear-instructions-can-compose-into-an-unsettled-contract.md): applicability, precedence and exceptions under English requirements.
- [Near-decomposability](../../theory/near-decomposability-may-make-local-inspection-affordable.md): candidate inspection mechanism and invariant-preservation limits.
- [Programming practices](../../theory/underspecification-and-indeterminism-complicate-programming-for.md): checks matched to requirement adequacy, conformance, prediction and variation. Its title changed; its historical filename has not yet been relocated.
- [Program refinement](../../theory/definitions/program-refinement.md): candidate versus checked refinement under applicable interpretations and preserved guarantees.

## Next work and acceptance

R1 is corrected: generation fixes a candidate implementation without establishing that its permitted behaviors preserve the specification's guarantees. The compatible generator/artifact correction is committed in `b69e7b478`. R2 is corrected: frame construction selects inputs without guaranteeing all causal isolation or scope within those inputs, and code selection does not imply zero error cost. R3 now separates precise semantics, affordable proof and behavioral evidence. Its shared-medium identity claim has been replaced with a candidate-specialization account, including separate checks for template expansion and model behavior. R4 replaces the artifact ladder with concrete checking arrangements and task-relative placement advice. Next address R5 one note at a time; final navigation review must also repair remaining backlinks that describe a universal verifiability ladder.

Before closure, inspect the revised passages and relevant navigation against these conceptual cases:

- The same prompt under English requirements and under an adopted deterministic package: diagnosis changes; task adequacy and inspection questions remain.
- A stochastic reference with precise semantics: specified variation is not unsettled permission.
- A permitted choice, a disputed interpretation and missing evidence: avoid diagnosing all three as either interpreter failure or ordinary selection from a settled set.
- A generated function with multiple inputs or nondeterministic behavior: one retained artifact does not imply a singleton behavior set.
- Readable code, opaque conventional code and a locally understandable prompt: form alone does not rank inspection cost.
- A successful generated artifact and a generator that sometimes fails: keep their testing obligations separate, including with deterministic generation.
- An isolated model input with information arriving through summaries, tools or shared state: distinguish direct exclusion from complete noninterference.
- A local intervention that changes a small quantity but breaks a required invariant: weak interaction alone does not justify ignoring the effect.

These are review cases, not a commissioned empirical trial. The workshop closes after the remaining claims are resolved or explicitly deferred to a durable owner, and final navigation and acceptance checks are complete. Extract any useful remaining working material, then delete the workshop and its index entry.

## Boundaries

The [addressability/near-decomposability unification candidate](../../reference/vocabulary-unification-ledger.md#addressability-and-near-decomposability) remains open; this rewrite does not decide it. The [invariants-under-composition workshop](../invariants-under-composition/README.md) is parked and must not be developed without the operator's request. The [ideal-interpreter workshop](../ideal-interpreter/README.md) is separate: the present argument needs no ideal interpreter.

Do not infer that most users hold either prompting account, that English resemblance is the only route to useful predictions, or that prompt abstractions are empirically worse than conventional code without a specified comparison. Preserve source quotations and dated findings as records of their inspected versions. This integration review checks internal consistency; it does not reverify the external literature or certify every backlink.
