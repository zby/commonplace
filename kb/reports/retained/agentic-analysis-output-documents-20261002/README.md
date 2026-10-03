---
type: types/note.md
description: "Closure evidence for replacing the monolithic agentic analysis: fixture sizes, fresh publication trials, reader checks, and limits of the adopted set contract."
---

# Agentic analysis output documents: closure, 2026-10-02

The operator commissioned closure of the output-documents workshop on
2026-10-02. The replacement of the monolithic result is implemented and has
bounded producer and consumer acceptance. This report retains the evidence
needed to assess that conclusion after the workshop is deleted. It supports
future review of the output design; it does not establish improved analysis
quality or full-corpus refresh completion.

## Adopted design

The [analysis set contract](../../../agentic-system-analyses/types/agentic-system-analysis-set.md)
owns directory membership and shared consistency checks. Each member has its
own type. The current complete set contains overview, runtime, memory,
epistemic and reconciliation reports. Blocked and out-of-scope sets contain
only the overview. Reviews and run state pin `ARTIFACT.yaml`; it pins the
reports. Publication and comparison readers use the shared artifact checker.
[ADR 095](../../../reference/adr/095-directory-artifacts-add-shared-set-validation.md)
records the directory model and the separation of shared checks from checks
requiring a frozen source or local run state.

The original candidate had four reports. The fifth separates reconciliation
from synthesis, implemented in `0ad34f5d`. The later collection ownership
migration is documented in its
[retained acceptance record](../../../agentic-systems/reports/retained/layout-migration-2026-10-01/README.md).
The retired result type and compatibility readers were removed. Historical
results remain frozen in the collection archive; they are not current
comparison inputs.

Types specify document contents; instructions specify production and judging.
The workshop's cleanup reduced the five governing files from 15,701 to
12,701 whitespace-separated words before the subsequent independent review.
The review brought the total to 12,795. These are dated measurements of that
method, not word counts of today's reorganized job instructions.

## Retained trials

Four exact records are retained under `captures/`. Their original locations,
source commits and SHA-256 values are in
[capture provenance](./capture-provenance.json). Their relative links belong
to their original checkout context and are preserved as capture data, not
live navigation. The validation-ignore marker applies only to these captures.

- [Cleanup regression](./captures/cleanup-rerun-20260927.md): three frozen
  source analyses validated, published and passed independent handoff and
  bounded consumers. It found omitted profile values despite surviving prose
  and changes in functional scope. Structural success did not establish
  semantic completeness or comparable breadth.
- [Fixture split](./captures/fixture-split-20260928.md): two existing results
  split with zero duplicate declarations, zero unresolved references and
  unchanged quote unions. The dropped memory sections survived verbatim in
  the memory reports. Measured set sizes were 19,505 and 15,100 words,
  respectively 87% and 84% of the original retained result plus local report.
  The largest members were 67% and 51% of the old result. Smaller projections
  after reducing amendment copies were estimates, not another measured trial.
- [Fresh batch acceptance](./captures/batch-01-rerun-2026-09-28.md): three
  whole-system sets published, passed independent handoff and full-set
  validation, and supplied the same selected population to matrix, table and
  statistics. The memory member remained largest even for Agent-S; this
  trial did not demonstrate a runtime-dominated output. Body totals were
  16,622, 14,098 and 17,979 words. Specialist correction turns were 1, 2 and 2.
- [Batch trace audit](./captures/batch-01-rerun-trace-audit-2026-09-28.md):
  confirmed zero failed analysis validations or prepares, while retaining
  recovered command errors, truncated reads and incomplete instruction
  delivery. Final passes do not establish error-free execution.

The last two records came from branch `refresh-batch-01-rerun` at
`c854800b`; its two batch commits remain absent from main at closure.
Retaining the records neither merges their sets nor advances the main
inventory. The corpus-refresh workshop owns that integration decision.

## Closure checks

The inspected method and evidence commit is
`1bdd2929650bad5a5ecb9d0fb6b2f23b6f87c00a`. Closure checks used the committed
review and retained set for `AAS-2026-10-01-instinctual-memory-07`, excluding
concurrent uncommitted review replacements. The review pins manifest SHA-256
`e409b30ce075f68a71fbdf29719dd9d2816e639d687a8d0bfc0fc7a164bade8e`.

The selected existing test modules passed: **211 tests**. They cover directory
membership and hashes, set identity, cross-member references, analysis
publication, comparison readers, member contracts and site publication.
Missing members, changed bytes, differing run/source identities and unresolved
references have rejection cases. No new tests or analysis runs were added.
Explicit full validation of the retained five-report set passed without
warnings.

A temporary export of the committed `kb/` and `scripts/` trees supplied the
same selected review to `build_systems_matrix.py`, `render_systems_table.py`
and `analyze_matrix.py`. All exited zero, producing one code-grounded row and
no doc-grounded rows. The profile had ten known axes; all listed value bases
were wired. This is a one-row reader trial, not a corpus distribution.

The recorded reader trial produced this bounded numerical summary:
`write_agency` retains both automatic and manual values, and
`read_back_direction` retains both pull and push values. Each is counted once
within one selected row, rather than as another system. The former cites
MEM-RTE-1, RTE-3, RTE-4, RTE-5, RTE-8 and RTE-9; the latter cites RTE-1,
RTE-2, RTE-5 and RTE-8. These are profile classifications, not measured
behavioral benefit. The evidence-bearing set and review were later retired during
[analysis-offload closure](../analysis-offload-closure-20261002.md); this
compressed reader observation remains, and Git retains the original records. The
[comparison procedure](../../../agentic-systems/comparisons/README.md) and
[landscape synthesis skill](../../../agentic-systems/instructions/synthesize-agent-memory-landscape/SKILL.md)
both require manifest-pinned evidence of this form. The retired trial set is
no longer selected as a live input.

The [transfer scan](../../../instructions/scan-agentic-system-transfer/SKILL.md)
checks complete run state, complete substantive disposition, manifest identity
and hashes before and after reading. Its completion and source assumptions
were inspected; closure did not commission a new Commonplace transfer scan.

## Limits and disposition

The adopted contract checks declared membership, hashes, identities,
declarations and references. It does not prove semantic support, complete
profile classification or absence of duplicated prose. Exact derivation of
the finalized specialist body and a set-wide quote minimum were deliberately
dropped during implementation. The original proposal's stronger checks are
not implied by this closure.

The fixtures support preserved evidence and reduced duplicated text on two
historical cases. Fresh trials establish operation of the split output and
its consumers. There is no matched estimate of quality improvement, time
savings or general context benefit. Coordination still requires semantic
reconciliation and corrections; the trace audit bounds the acceptance claim.

The output-documents workshop is closed. Its draft contracts and superseded
handoffs are deleted; Git retains their history. Corpus regeneration,
historical consumer migrations and ongoing analysis-method repair remain
with their existing workshops. The unmerged batch is not a blocker for the
implemented output contract. No workshop redirect is added.
