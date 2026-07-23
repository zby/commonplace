# Audit: review, fix, and full-pass loops

## Review-system mapping

| Mechanism | Loop role | Reason |
|---|---|---|
| Target selector and criterion resolver | Search preparation | They decide what evidence-producing work to attempt. |
| Model review gates and review jobs | Search / problem-noticing | Verdicts describe possible defects in already-operative notes; no verdict blocks, removes, or rolls back the note. |
| `warn_selector` | Search routing | It turns current warning evidence into a correction queue. |
| Fix / reject / defer decision | Evaluation | It can choose a fix candidate, reject the warning as spurious, or withhold judgment. Rejection is distinct from producing another candidate. |
| Diff review and guarded disposition | Evaluation | It decides whether a proposed edit should become operative. |
| Commit or merge of the edited note | Retention | The selected change enters the repository's behavior-determining state. |
| Review freshness baseline | Evidence bookkeeping | It pins verdict applicability to note and criterion revisions; it does not endorse a note or a verdict. |

This resolves the workshop's `warn` ambiguity without extending the ontology. `warn` is a search output. `fail` is more urgent evidence, but remains an escalation signal because no consumer blocks the incumbent. Calling either one “evaluation” would confuse a verdict-shaped representation with operative selection force.

## Rejection repair

Before this audit, fix reports admitted only `fixed` and `deferred`. A false-positive warning had no honest disposition: it could be applied or postponed, but not rejected. That made the downstream filter weaker than the loop description implied.

`FIX-SYSTEM`, the one-note fix instruction, and the sweep instruction now require three distinct outcomes:

- `fixed`: the finding applies and a minimal edit resolves it;
- `rejected`: the finding is spurious, mistaken, or inapplicable, with evidence and no note edit;
- `deferred`: the finding may apply but needs argument-level or human judgment.

This is a representational repair, not proof that operators will exercise rejection well. The absent fix-report corpus prevents a historical estimate. Future sweeps should report rejection rates and inspect near-zero rejection as a possible rubber-stamping signal.

## Oracle warrant

Semantic gates use model judgment. Their warranted domain is therefore provisional and gate-specific, not inherited from the deterministic validator. The existing [calibration proposal](../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md) correctly requires labelled fixtures, explicit adoption criteria, and judging-configuration versioning before stronger enforcement.

Current force—evidence production and triage—is proportionate to that warrant. Promoting model verdicts to automatic note rejection, demotion, or rewrite acceptance would cross the warrant boundary.

## Freshness boundary

Review freshness hashes criterion and target revisions but intentionally excludes prompt rendering and orchestration scaffolding. That is defensible for refactors that preserve judgment, but unsafe as a blanket assumption: system instructions, formatting, or parser expectations can change model outcomes while stored baselines remain “current.”

Until judging configuration becomes an explicit dependency, judgment-changing prompt/process edits require deliberate re-review. The calibration proposal already names rendered prompts and system instructions as part of the judging configuration; the later change-time digest should route such edits to that requirement.

## Full improvement pass

The full pass composes candidate generation, report validation, explicit disposition, version guards, and guarded mutation. Its delete/merge branches preserve human authority, and its report schema makes candidate commitments inspectable. In loop terms it is a bounded proposal-selection mechanism, not a general self-improvement controller.

No change is recommended. It should remain experimental and opt-in, and its scope should remain note-level until behavior-authority changes have a stronger oracle and explicit retention rules.
