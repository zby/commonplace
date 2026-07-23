# Phase-1 operational-artifact audit

Executed 2026-07-23 against the repository's behavior-determining artifacts: `AGENTS.md` and its generated variants, all collection contracts, `kb/types/`, `kb/instructions/`, and `src/commonplace/`. The inventory is exhaustive at the file-family level; findings are organized by behavior surface rather than repeated for every file with the same consumer and force.

## Audit test

For each surface, the audit asked:

1. What consumes it, through which channel, and with what force?
2. Does it implement search, evaluation, retention, or only evidence bookkeeping?
3. If evaluation is automated, what warrants the oracle and where does that warrant stop?
4. If it retains commitments, are scope and retrieval wires explicit?
5. Does prior retained state directly affect later improvement decisions, rather than merely changing the environment in which they occur?

The detailed coverage record is in [artifact-inventory](./artifact-inventory.md). The three analytic reports are [authority-and-authoring](./authority-and-authoring.md), [review-and-fix-loop](./review-and-fix-loop.md), and [validation-freshness-and-code](./validation-freshness-and-code.md).

## Outcome

The operational layer is structurally stronger than the workshop's trigger finding suggested, but the trigger finding stands: the self-improvement cluster itself has no change-time retrieval wire. Existing validators, review selection, freshness tracking, and mutation commands form useful mechanisms; they do not cause the cluster's operativity, profile, or warrant tests to be consulted when those mechanisms change.

The most important correction is conceptual and operational at once. Semantic review gates are automated **search/problem-noticing**, not reject-capable evaluation. The fix decision evaluates a finding; commit or merge retains an applied change. The previous fix-report contract made a spurious warning impossible to represent, so it has been repaired with a distinct `rejected` disposition. `fail` remains an escalation signal, not an operative blocker.

## Findings and dispositions

| ID | Finding | Disposition |
|---|---|---|
| F1 | No `AGENTS.md`, collection, instruction, type, or code path loads the cluster when behavior-determining organization changes. | **Proposal:** build a bounded change-time digest after the authority-path decision; wire covered changes through `AGENTS.md`, preserve user invocation and link discovery as theory fallback, and declare the digest's coverage. |
| F2 | Review verdicts do not accept or reject operative artifacts. `warn` only generated fix work, while fix reports could not record a false positive. | **Applied:** classify gates as search; add `rejected` beside `fixed` and `deferred`; resolve the workshop ledger item. |
| F3 | Model-based semantic gates lack a labelled-fixture calibration oracle and adoption threshold. | **Existing proposal:** [calibrating semantic gates against labelled fixtures](../../../reference/proposals/calibrating-semantic-gates-against-labelled-fixtures.md). Do not raise their enforcement force before that proposal's acceptance criteria are met. |
| F4 | Review prompt rendering and process scaffolding are outside the review freshness hash. Judgment-bearing criteria are hashed, but a prompt/process change can alter verdicts without invalidating baselines. | **Existing proposal + digest requirement:** the calibration proposal already defines judging configuration broadly. The later digest must require deliberate corpus re-review for judgment-changing prompt/process changes until freshness can represent that dependency. |
| F5 | Deterministic validation has a warranted, narrow oracle domain: schema/shape checks, path and link existence, exact quote matching, and recomputable tag marks. | **No change:** preserve the explicit boundary; do not describe these validators as judging semantic quality. |
| F6 | Freshness tracks review evidence against note and criterion revisions, not theory-to-implementation correspondence or collection-contract dependencies. | **Existing proposals / later phase:** [collection-as-artifact freshness](../../../reference/proposals/collection-as-artifact-freshness.md) and [factored dependency pairs](../../../reference/proposals/factored-dependency-pairs-for-review-freshness.md) cover parts of the substrate. Keep cluster-to-digest lineage under managed staleness until implemented. |
| F7 | Authoring instructions are strong retrieval wires once invoked, but two authority pointers were stale and one skill overclaimed deterministic validation; 14 descriptions exceeded the validator's retrieval-length rule. | **Applied:** repair pointers and semantic/deterministic wording; shorten the 14 descriptions. |
| F8 | Promoted skills contain Bash-shaped command snippets while `AGENTS.md` declares native Windows checkout support. A selected skill can therefore become non-operative on a supported channel. | **Proposal:** [make promoted skill commands channel-portable](../windows-portability-for-promoted-skills.md). |
| F9 | The full improvement pass is a bounded, version-guarded candidate-selection process for note edits. Human disposition and guarded commit preserve the evaluation/retention split, including delete/merge escalation. | **No change:** keep it opt-in and experimental; do not generalize it to behavior-authority changes without a stronger oracle and explicit scope. |
| F10 | The profile's cumulativity exclusion survives contact with the repository. Freshness baselines and generated tag marks directly consume retained prior state; ordinary edits whose only effect is environmental do not. The three uses of “promotion” remain disambiguated by object and channel. | **No change:** park the remaining ontology/closure questions in their owning notes and close the phase-0 ledger. |

## Applied changes

- Added `fixed` / `rejected` / `deferred` fix dispositions and corresponding sweep reporting.
- Corrected promoted-skill authority references to `MANIFEST.promoted_skills` in `src/commonplace/scaffold_manifest.py`.
- Corrected `cp-skill-convert` so deterministic validation is not presented as a semantic title or trait oracle.
- Shortened every instruction description flagged by `commonplace-validate instructions` so the descriptions remain useful retrieval discriminators.

## Evidence boundary

This checkout has no `kb/reports/commonplace-store.sqlite` and no `kb/reports/fixes/` corpus. The audit could therefore inspect mechanisms, contracts, schemas, selectors, and code paths, but could not estimate historical warning rejection rates or model error rates. Those are empirical calibration tasks, not prerequisites for the structural findings above.

## Verification

- `commonplace-validate instructions`: 80 files, no warnings or failures (the 14 pre-audit description warnings are cleared).
- `commonplace-validate types`: clean.
- All eight changed/new workshop records: clean under per-file deterministic validation; local-link resolution also passes.
- Focused pytest suite for validation, scaffolding, and warn selection: 63 passed, 7 failed, 1 skipped. The failures are existing Windows-channel mismatches in path rendering, `direnv` expectations, and scaffold-template idempotency; no executable source changed in this audit. They reinforce F8 but are not attributed to the instruction edits.
- `git diff --check`: clean.

---

Links:

- [Workshop framing](../README.md) — owns: phase sequencing and closure criteria
- [Self-improving systems cluster](../../../notes/self-improving-systems-README.md) — supplies: audit vocabulary
- [Commonplace declared frame](../../../reference/commonplace-declared-frame.md) — bounds: the system under assessment
