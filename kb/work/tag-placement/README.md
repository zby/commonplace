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
  five child–parent relations. These are dependencies of assigned-tag issues,
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
