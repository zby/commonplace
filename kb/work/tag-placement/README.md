# Tag placement and parent–child relations

## Commission

Opened on 2026-09-26 at the operator's request after the tag placement review.
Resolve the review's possible mismatches and parent–child conflicts so that
note assignments, tag-head inclusion rules, and the hierarchy convention agree.
This is a new workshop following the closed tag workshop. Opening it records
the work; it does not accept the reviewers' proposed removals or additions.

## Work inventory

- [Assigned-tag issues](./assigned-tag-issues.md): 67 possible mismatches and
  one uncertain assignment, with stable issue IDs and retained reviewer reasons.
- [Parent–child relations](./parent-child-relations.md): 13 conflicts across
  five child–parent relations in the initial review. Disposition added two cases
  under a sixth relation and a missing-parent inventory. These are dependencies of assigned-tag issues,
  not 13 additional assignment findings.
- [Suggested additions](./suggested-additions.md): suggestions for 206 notes,
  retained for disposition separately from the assigned-tag verdicts.
- [Placement baseline](./placement-baseline.md): the 29 frozen tag-head
  openings used in the review. These preserve what each finding was judged
  against; the live heads govern future assignments.

The review covered all 848 existing assignments on 388 selected artifacts
under `kb/notes/`: 780 keep, 67 mismatch proposals, and one uncertain judgment.
There were 327 PASS notes, 60 FAIL notes, and one WARN note. A PASS does not
establish that every useful tag is present. The 27 typed artifacts with no tags
and artifacts in other collections were outside the sweep. Expanding that
audit is a separate scope decision, not a hidden closure requirement.

## Progress — 2026-09-26

The [first disposition pass](./parent-membership-decision.md) resolved 19
assignment findings: 17 parent assignments retained, two incorrect constraining
tags replaced. Two addition entries were accepted as those replacements.
Parent openings now explicitly include substantive fit to their declared
children. PC-01 through PC-06 are resolved; PC-07 tracks
[129 missing parent assignments](./parent-membership-gaps.md) exposed by the
membership check. The initial semantic sweep did not cover those absences.

The operator then included responses within deploy-time-learning. The
[scope decision](./deploy-time-scope-decision.md) retains all eleven assignments
flagged under its old phenomenon-only rule and aligns neighboring heads.
The operator also accepted substantive use of one artifact-analysis field.
The [single-field scope decision](./artifact-analysis-scope-decision.md) retains
three flagged assignments and removes one unsupported tag. That removal also
closes PG-035, leaving 128 entries in the parent-gap inventory.
The operator renamed methodology to method-guided-action, keeping the narrower
question of how methods guide decisions and allowing overlap with learning-theory.
The [disposition](./methodology-scope-decision.md) retains the literature-reuse
assignment and accepts all six related additions, superseding the initial
rejection of the theory–methodology execution note.

The operator then split Commonplace-specific architecture from the general
subject. The [architecture decision](./architecture-placement-decision.md)
retains all three flagged assignments under the general head, adds the new
commonplace-architecture child to six qualifying members, and records PC-08
as resolved with every child member retaining its parent. Three related
addition entries are accepted; the always-loaded-context survey also has the
agent-memory parent. Thirty-eight original assignment findings were resolved at that point.

The [computational-model disposition](./computational-model-placement-decision.md)
removes twelve assignments that do not meet the execution-focused head. It
accepts nine addition entries and closes one duplicate removal recommendation.
Child-fit checks also restore eleven learning-theory parents from PC-07, leaving
117 inventory entries open. Fifty original assignment findings were resolved at that point.

The [context-engineering disposition](./context-engineering-placement-decision.md)
removes nine context-engineering assignments and one associated llm-reliability
assignment, accepts five addition entries, and resolves two more parent gaps.
Sixty original findings were resolved at that point, with 115 parent-gap entries open.

The [remaining-placement disposition](./remaining-placement-decision.md)
retains the discovery assignment on epiplexity and removes seven unsupported
assignments. It accepts four additions, closes two duplicate removals, and
resolves three parent gaps. All 68 original assignment findings now have
dispositions: 36 retained and 32 corrected.

The [learning-tag boundary and application](./learning-tag-boundary-decision.md)
clarifies improvement-loop versus continual-learning without merging them.
It accepts twenty addition entries, adds both tags where both mechanisms
are developed, and resolves seven more parent gaps.

The [first evaluation-additions pass](./evaluation-additions-01.md) accepts ten
entries on assessment warrant, human judgment, memory effects, and text testing.
It also resolves two parent gaps.

The [second evaluation-additions pass](./evaluation-additions-02.md) accepts ten
entries on check targets, causal tests, compounding, benchmark limits, and
output diagnosis. It also resolves three parent gaps.

The [third evaluation-additions pass](./evaluation-additions-03.md) accepts ten
entries on oracle quality, adoption evidence, and experimental interpretation.
It adds four neighboring assignments and seven required parents, resolving
three entries in the original parent-gap inventory.

The [fourth evaluation-additions pass](./evaluation-additions-04.md) accepts the
six remaining evaluation suggestions, covering automation, claim support, and
transfer tests. It adds three neighboring assignments and six required parents,
resolving three original parent gaps. No evaluation suggestions remain open
in this queue; this does not establish exhaustive evaluation-tag coverage.

The [first context-additions pass](./context-additions-01.md) accepts twenty
entries on routing, prompt assembly, bounded-call budgets, and content retention
for later loading. It adds three companion assignments and five required
parents, resolving four original parent gaps.

The [context and document additions pass](./context-document-additions-02.md)
accepts thirty entries: all sixteen remaining context-engineering suggestions
and fourteen document-system entries. It implements the companion suggestions
and seven other required parents, resolving four original parent gaps. No
context-engineering suggestion remains open in this queue.

The [mechanism additions pass](./mechanism-additions-01.md) accepts thirty entries on
artifact classification, constraining, execution, reliability, and document
types. It adds thirteen required parent assignments and resolves six original
parent gaps. The artifact-analysis head retains complete coverage with shorter
navigation text and an unchanged inclusion rule.

The [review and evidence additions pass](./evidence-additions-01.md) accepts twenty-three
entries and closes one duplicate removal already implemented through TP-012.
It covers semantic review, observability, claim support, failure modes, curation,
and learning, and resolves nine original parent gaps. Four complete heads gain
member links without changing their inclusion rules.

The [theory and discovery additions pass](./theory-discovery-additions-01.md) accepts all fourteen
remaining suggestions, adds eight required parents, and resolves six original
parent gaps. Four complete heads gain member links; the theory-builder head
uses shorter navigation text, with all inclusion rules unchanged. The addition
queue is now fully disposed: 202 accepted entries and four duplicate closures.
This completes the retained suggestions, not an exhaustive missing-tag audit.

Remaining: the 65 parent-gap entries
tracked by PC-07. The [input record](./parent-membership-inputs.md) preserves versions
used for the first pass. Existing review results and the placement baseline
remain frozen.

## Evaluation boundary

Determine placement from what the note substantively addresses and the tag
head's inclusion condition. A secondary argument or worked boundary case can
qualify. A term's incidental occurrence or a footer link alone cannot. The
review findings are hypotheses to adjudicate, not instructions to retag.

The [tag-README contract](../../types/tag-readme.md) says child-tagged notes
keep the parent when a tag is split with overlap. Thirteen findings accept a
child while rejecting that parent. Before acting on one of those findings,
resolve whether the parent wording is too narrow, the declared relation needs
revision, or the reviewer misapplied the rules. Record the decision against
the relation and link it from each affected assignment. Do not infer from
these findings that parent tags should simply be removed.

A change to a head or hierarchy can affect assignments the review accepted.
Before closing such a decision, identify its affected membership and recheck
it under the revised rule, including accepted assignments. Concrete wording,
grouping, and the order of independent cases remain choices for the working
session; this framing does not preselect their outcomes.

## Bookkeeping and evidence

Each issue starts open. Record a disposition, its reason, the live note and
head versions considered, and any resulting artifact or commit. Dispositions
may retain an assignment, change an assignment, revise a head or relation,
reject a suggested addition, or explicitly defer a case. A deferral names its
reason and a return condition or destination; it must not silently disappear.
Keep issue IDs stable. Cross-reference a shared decision instead of treating
dependent findings as independent votes.

Reviewer reasons and addition suggestions are copied into the work lists so
the workshop remains usable from a clean checkout. The baseline is historical
input, not a second editable tag registry. Read the live note and head before
disposition; the initial review's freshness does not persist through edits.

The local [review report](../../reports/cache/tag-placement/2026-09-26.md) and
[run record](../../reports/state/tag-placement/2026-09-26/README.md) provide
optional access to full outputs and captured inputs in this checkout. Their
absence in another checkout does not erase the retained issue list. The run
used `gpt-6-sol` fresh workers, jobs 8790–8809, and refresh job 8810 after a note
changed. Its criterion was
`commonplace:instructions/review-gates/frontmatter/tag-placement-20260926.md`,
with head openings captured after commit `fe905c66`. Final verification found
zero stale pairs and unchanged placement openings. These are single-reviewer
judgments, not independently confirmed tagging errors.

## Closure

Close when every assigned-tag issue, relation issue, and suggested-addition
entry has a recorded disposition; accepted changes are implemented; and any
explicitly deferred work has a named continuing home. Validate changed
artifacts and check the affected assignments against the resulting heads.
Preserve any needed decisions or methodological findings in the appropriate
library artifacts, with change history and sweep counts in commits. Then
delete this workshop and remove its active-list entry.
