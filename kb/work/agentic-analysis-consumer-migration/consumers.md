# Consumer migration queue

Inventory inspected on 2026-09-05. These entries distinguish direct review
readers, readers of derived data, evidence-bearing publications, and machinery
that currently requires the legacy output. Recheck each entry's live behavior
when selecting it; a textual reference alone does not prove active use.

Entries without an execution record remain **pending**. The acceptance conditions below supplement the
[workshop's shared conditions](./README.md#execution-and-bookkeeping).

| ID | Consumer and current entry point | Migration boundary and acceptance |
|---|---|---|
| C01 — done | [Matrix builder](../../../scripts/build_systems_matrix.py) and [reader](../../../src/commonplace/lib/systems_matrix.py) read retained main results. | Read main-review results directly. Establish supported fields, system/run identity, evidence tier, population, and input hashes. Derive each classified value from a recorded finding; report missing support. Disposition prior hand-classified and identity-join columns explicitly. |
| C02 — done | [Table renderer](../../../scripts/render_systems_table.py) reads retained main results and links their public evidence. | Render the migrated data and link sufficient tracked main-review evidence. Verify link resolution and population against the originating result set. Depends on C01's data contract. |
| C03 — done | [Matrix analyzer](../../../scripts/analyze_matrix.py) computes statistics directly from retained main results. | Update field assumptions, evidence population, and missing-value handling against C01. Verify a bounded query against the originating main-review findings. |
| C04 — done | [Landscape synthesis skill](../../instructions/synthesize-agent-memory-landscape/SKILL.md) reads full retained main results and bundles a matching derived matrix. | Read main-review files as qualitative evidence and bind quantitative results to that same population. Update the frozen evidence bundle and cited-file identities. Preserve evidence-tier distinctions and exclusion of transfer judgments. Requires the durable-evidence decision and C01 for matrix-based claims. |
| C05 | [Trace-learning survey](../../agent-memory-systems/trace-learning-techniques-in-related-systems.md) cites individual legacy reviews. | Refresh from main-review findings with sufficient lineage, behavior-change, and evidence-status detail. Declare the new snapshot/population and distinguish unavailable evidence from a negative finding. |
| C06 | [Comparative review](../../agent-memory-systems/agentic-memory-systems-comparative-review.md) combines matrix claims and legacy qualitative examples. | Rebuild one coherent snapshot through the migrated synthesis procedure, or explicitly retire it as a current account. Do not update counts while retaining claims from a different population. |
| C07 | [Thalo type comparison](../../agent-memory-systems/thalo-type-comparison.md) uses a legacy review for its external-system account. | Ground the Thalo mechanism in the main review. Disposition the Commonplace mapping as current transfer or a bounded historical comparison under the appropriate contract. |
| C08 — done | [Transfer scan](../../instructions/scan-agentic-system-transfer/SKILL.md) now requires the exact main-review result and its completion state. | Initial and final completion/identity checks, canonical finding references, and no legacy or summary fallback. See [acceptance](./c08-acceptance.md). |
| C09 — done | [External-system placement pass](../../instructions/simplification-passes/place-external-systems.md) reads generated main reviews, with source ingests identified separately. | Check support, evidence status, source revision, and input hashes; withhold unsupported or local-only citations. See [acceptance](./c09-acceptance.md). |
| C10 — done | [Classification audit](../../instructions/refresh-agent-memory-review-taxonomy.md) reads retained main results and diagnoses their classifications. | Require exact evidence and method identities; preserve scope and uncertainty. Route defects through the producing method and source regeneration, without patching generated prose. See [acceptance](./c10-acceptance.md). |
| C11 | [Quote-grounding check](../../instructions/verify-review-quote-grounding.md) reads review quotations and checkout files. | Determine which main-review output actually contains quotations and migrate the relevant check, or retire the unused procedure. Resolve evidence against the frozen commit/capture, not the current worktree; keep quote verification distinct from claim-support judgment. |
| C12 | [Legacy review writer](../../instructions/write-agent-memory-system-review/SKILL.md) reads existing reviews for style and drafts again from frozen sources. | Retire the extra drafting and style-exemplar dependency with C14. Do not rewrite this writer as a legacy-format projection adapter. |
| C13 | Authored evidence links in `kb/notes/`, `kb/articles/`, `kb/sources/`, `kb/reference/`, and per-system analyses; [grounding-alignment gate](../../instructions/review-gates/semantic/grounding-alignment.md) follows linked library evidence. | Work by citing artifact or bounded claim group. Check support before changing a target; retain historical citations when the original observation matters. The generic gate already recognizes both system collections: change it only if the selected evidence location requires it. |
| C14 | Main-review publication and handoff: [analysis checks](../../../src/commonplace/lib/agentic_analysis.py), [publication code](../../../src/commonplace/lib/agentic_publication.py), [validation](../../../src/commonplace/lib/validation.py), result/run-state contracts, and producing skill. | After active consumers are resolved, remove mandatory legacy candidate/output fields, legacy publication gates, and stale-output reporting tied to the old pipeline. Preserve necessary evidence and publication checks on the main outputs; handle validation of retained historical artifacts explicitly. Prove a memory-system run can complete with its main-review outputs alone. |
| C15 | Collection READMEs, generated indexes/table links, and website/search navigation. | Route current discovery to the main reviews and migrated comparison outputs. Keep supported historical references navigable. Verify public evidence from a clean checkout without ignored run files. |

## Inventory boundaries

No additional specialized numerical pipeline was identified beyond the matrix
builder, renderer, and analyzer. Historical relocation/migration scripts, old
proposals, and recorded reports are not automatically active consumers.

Review-to-review links and workshop references also need disposition when their
targets migrate. They are navigation or historical evidence unless inspection
shows a live reading procedure. Source ingests and historical comparisons must
not be rewritten merely to eliminate occurrences of the old collection path.

## Per-consumer record

When starting an entry, add a subsection here with:

- ID, status, intended behavior, and owned files;
- exact main-review inputs and the findings/fields consumed;
- prerequisite or blocker, with its return-to-decision condition;
- bounded verification result and remaining coverage limits;
- final disposition and commit reference when available.

Use these records to choose the next step. Persist detailed change history in
the implementing commits rather than copying their diffs into this queue.

### C08 — Transfer scan

**Status: done.** Selected first because its direct caller already
passes the main review's exact result, and the scan needs no matrix fields or
public retention policy.

Owned files: `kb/instructions/scan-agentic-system-transfer/SKILL.md`, its direct
caller `kb/instructions/analyse-agentic-system/SKILL.md`, and this workshop's
acceptance records. The runtime loads the scan through its skill projection or
the main review's step 9 invocation; the canonical instruction edits change
both paths immediately.

The input is one exact `result.md` plus its sibling completion state, source
identity/revision, result hash, interest brief, and permitted Commonplace scope.
The migrated scan verifies completion before interpretation and again before
returning findings, then reads the result's shared records, lens findings, and
limits. Legacy reviews and compact projections cannot substitute for that file.

The two recent minimal-state runs both fail today's completion checks:

- `AAS-2026-09-04-pond-01`: missing required
  `legacy-review-model-partition`.
- `AAS-2026-09-04-apache-maka-02`: missing that field (required even when null),
  plus a Run identity projection containing a `— complete` suffix where the
  validator requires the exact state path.

These are acceptance inputs for rejection, not successful live pilots. Do not
patch their generated analyses or waive validation to make the trial pass.
The [bounded positive replay and rejection checks](./c08-acceptance.md) accept
the input migration without claiming either production run now validates.
All 699 tests passed; changed skills and the replay scan validated cleanly.
Committed in `c1490415`.

### C01–C03 — Matrix, table, and statistics

**Status: done for the reader migration. Production pilot: one regenerated system.**
C01 established normalized assessments in the exact main result and retention
of those same bytes during publication. C02 then replaced its CSV dependency
with the same direct reader and public evidence links. C03 replaced its CSV
input with that reader and separates stronger implementation/operation evidence
from weaker bases and unknown assessments. Each procedure can run without the
legacy corpus or either of the other comparison outputs.

Owned files: the three scripts and `systems_matrix.py`; main-result type/schema
and validation; publication and completion checks; producer skill; website
retention exception; affected command and collection documentation; tests; and
these acceptance records. No generated system findings or legacy CSV/table
bytes were edited. Prior hand-classified columns and directory-name identity
joins are removed, without a compatibility adapter.

Inputs are selected public main-review projections plus their hash-identified
retained results. Scope, evidence tier, 14 assessed axes, basis, and canonical
record references come directly from the main result. Multiple stores stay
sets. Missing normalization or retained evidence blocks the selected cohort;
no tag omission, legacy prose, or old CSV value fills a gap. A repeated source
identity requires explicit selection of one review.

The [acceptance record](./c01-c03-acceptance.md) covers clean-input builds,
missing and mismatched evidence, unknown/absence distinctions, evidence-tier
filtering, input drift, retention, and publication rollback. The initial live
build rejected Apache Maka for missing retained-result metadata. Implemented
in `c1490415`. The [production pilot](./production-pilot.md) now rebuilds Maka
through the main workflow and verifies the matrix, table and analyzer on its
retained result. The default all-generated build still rejects Pond. The
workshop pair covers Maka alone; public defaults and legacy snapshots remain
unchanged.

The later [producer-check exercise](./producer-check-acceptance.md) found
unsupported task-horizon and inconsistent learning-branch assessments in Maka.
The reader/output mechanics remain accepted, but affected complete learning
claims must be withheld pending source regeneration. The pilot does not certify
every comparison classification.

### C04 — Landscape synthesis

**Status: done for procedure migration and one-system production pilot.**
The skill now requires full retained main results for qualitative claims and
builds its CSV from those same inputs. The reusable bundle command captures
contracts and hashes, rejects drift and mixed populations, and distinguishes
current checks from historical verification. Explicit unknown assessments
withhold unsupported conclusions without blocking unrelated findings.

Owned files: the synthesis skill, `scripts/bundle_agentic_landscape.py`, its
tests, the comparison README, legacy collection navigation and design note,
and the two public-output collection contracts permitting citations to
published exact main results. Invocation through the existing skill projections
loads the changed procedure immediately. No main-review findings were edited.

The [acceptance record](./c04-acceptance.md) and
[bounded fixture synthesis](./c04-trial.md) cover a four-result population,
one eligible quantitative case, three explicit exclusions, canonical-record
support, and rejected stronger claims. The procedure migration passed 722
tests and was committed in `c589b981`. The subsequent
[production pilot](./production-pilot.md) uses main run
`AAS-2026-09-05-apache-maka-01` and its retained result directly for bounded
queries and qualitative findings. It also fixes link validation for results
supplied in the same prospective publication bundle. All 723 tests pass. No
public landscape article or whole-corpus comparison was refreshed. Pilot and
publication fix committed in `f586fb1d`.

**Next:** C11, checking where the main result retains quotations and migrating
or retiring the quote-grounding procedure. Resolve quotations against the
recorded source revision or capture. C05–C07 need enough regenerated evidence
or an explicit historical disposition. Pond remains outside the new comparison
population. Consumer IDs remain an inventory, not a fixed sequence.

C15 received navigation and public-citation contract updates needed by C01–C04. Broader citation
and public-navigation migration remains pending. C12/C14 still require the
legacy publication; this change has not retired duplicate drafting.

### C09 — External-system placement

**Status: done.** Selected after C08 because a tracked public main review can
directly support a bounded placement without solving matrix normalization or
exact-result retention first.

Owned files: `kb/instructions/simplification-passes/place-external-systems.md`,
its `README.md` catalog, and this workshop's acceptance record. The
`revise-an-article-or-note` caller dispatches the named pass as an artifact,
purpose, preserved-claims, and write-scope packet; that interface is unchanged.

The reader now identifies generated main-review metadata and evidence basis,
reads supporting findings directly, and records hashes and source revisions.
An exact result is a checked escalation when a compact review is insufficient.
Unsupported claims are withheld; ignored local evidence cannot silently become
a tracked library citation. Source ingests remain an explicitly separate class.

The [Pond placement trial](./c09-acceptance.md) used only the tracked generated
review. It retained implemented storage/retrieval findings, withheld automatic
injection and demonstrated-improvement claims, and preserved the distinction
between static wiring and observed use. Changed Markdown validated cleanly.
Committed in `c1490415`.

### C10 — Main-review classification audit

**Status: done for procedure migration and a bounded audit.** The existing
instruction path now diagnoses classifications in retained main results.
It checks evidence and method identities before and after interpretation,
distinguishes structural validity from semantic support, and preserves unknown
assessments. Corrections go through the shared method when needed and a new
source-based main-review run; the audit cannot patch generated findings or
refresh surveys.

Owned files: `kb/instructions/refresh-agent-memory-review-taxonomy.md`,
this queue and [acceptance record](./c10-acceptance.md). Repository search found
no automated caller or skill projection. Two mentions in other workshop
inventories are descriptive, not procedure calls. The conditional producing
skill already accepts the required source, target and diagnosis; its interface
is unchanged.

The audit consumed the public Maka review and exact retained result from
`AAS-2026-09-05-apache-maka-01`, including scoped comparison fields, canonical
objects, routes, authority records and limits. No classification defect was
established in that selected result. Missing or mismatched evidence, a legacy
path, input drift and unregenerated Pond were rejected. Two temporary semantic
defects passed structural validation and were identified by reading their
supporting records. An isolated copy worked without legacy files or local run
state. Input and method identities matched at the final recheck.

The changed procedure and workshop records validate cleanly. This Markdown
change exercised the existing reader directly; no code changed or new pytest
run was needed. No production source regeneration or generated-output edit
occurred in C10. Initial acceptance covers Maka alone; the all-generated audit
still blocks on Pond. The subsequent [oh-my-pi report audit](./c10-oh-my-pi-audit.md)
identifies two real classification defects after structural success and one
remaining selection-mapping question. Corrections require a new producer run;
the diagnostic does not invalidate the row automatically in the reader.
The [producer-check update](./producer-check-acceptance.md) adds the focused
integrated check and shared clarifications before that rerun. It preserves the
existing publication interface and passed all 723 tests. Its independent
exercise reproduced oh-my-pi's defects and identified two further learning
assessment gaps in Maka, while preserving valid uncertainty and weaker bases.
Implementation and verification are recorded in this workshop's Git history.
