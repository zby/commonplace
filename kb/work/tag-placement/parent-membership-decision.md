# Parent membership: first disposition pass

Decision recorded 2026-09-26 while executing the operator's request to work on
the workshop issues. This pass resolves 19 of the original 68 assignment
findings and two suggested additions. It preserves the existing child scopes
and the split-with-overlap rule.

## Decision and reason

The parent heads include the subject areas of their declared children. A
note's substantive fit to a child also qualifies it for that parent. This
does not classify every system discussed by a child as an instance of the
parent's defining concept. A software-factory definition, for example, belongs
in the self-improvement subject area without claiming that every factory
learns or revises itself.

This interpretation follows the existing [tag-README
contract](../../types/tag-readme.md): child-tagged notes keep the parent when
splitting with overlap. Both parent heads already explicitly listed the child
areas and described their topics. Requiring each note to establish a separate
learning or self-change claim would exclude the child definitions and boundary
analyses those same heads retain.

The review used opening excerpts. The self-improving-systems opening referred
to child areas below but did not include their scopes; the learning-theory
opening did not make child inclusion explicit. Thus the review criterion lost
placement information that the full heads and the type contract supplied.
The corrected openings name every declared child and say that substantive fit
to a child also meets the parent condition. The llm-reliability head now names
learning-theory as its parent, matching the existing declaration in the parent
head. This clarifies placement without changing any child inclusion condition
or the definition of a self-improving system.

All 13 original kept-child/rejected-parent cases retain their assignments.
Reading the parent's child list exposed two more cases under llm-reliability,
TP-003 and TP-053, which also retain learning-theory. The original conflict
detector only read explicit “child of” phrases in the frozen openings, so it
missed this relation.

## Two assignment corrections

- **TP-039 / ADD-110:** replace constraining with llm-reliability on the
  [checkpoint note](../../notes/llm-code-boundaries-are-natural-checkpoints.md).
  Its worked example separates an incorrect model argument from correct code
  execution and explains the checks that expose the deviation. Narrowing
  interpretations appears only as a refactoring context. Retain learning-theory
  through llm-reliability, resolving TP-040.
- **TP-045 / ADD-133:** replace constraining with artifact-analysis on the
  [opacity note](../../notes/opacity-is-a-scale-threshold.md). Its contribution
  qualifies the scheme's representational-form axis: practical inspectability
  depends on scale. It does not concern narrowing interpretations. Retain
  learning-theory through artifact-analysis, resolving TP-046. Add a contextual
  entry to the complete artifact-analysis head so it still reaches every member.

The notes' arguments are unchanged. Each resolved issue retains its original
reviewer reason and now has a separate disposition. Stored review results and
the frozen baseline were not rewritten; they remain judgments under the old
criterion, not validations of the clarified heads.

## Affected membership and verification

The head changes preserve the existing direct inclusion routes and add an
explicit route through unchanged child conditions. They therefore do not
invalidate previously accepted assignments. This is a scope-preservation
check, not a new claim that every accepted child assignment is correct.
The 17 notes carrying disputed parent assignments were read in full; their
individual reasons are in the assigned-tag queue. The
[input record](./parent-membership-inputs.md) identifies the versions considered.

The [membership inventory](./parent-membership-gaps.md) enumerates the child
populations governed by the two heads and identifies missing parent tags across
the participating collections. All six children of self-improving-systems
already retain that parent. The learning-theory branch has incomplete parent
assignment; PC-07 tracks that separate cleanup. This is pre-existing metadata
inconsistency exposed by the check, not a reason to reject the subject-area rule.

Validation completed with zero failures and zero warnings for both retagged
notes, the full tag collection, the changed workshop files, and the workshop
index. The added opacity entry initially pushed artifact-analysis over its
8 KB soft limit; shortening three context phrases brought it to 8,146 bytes
while preserving all links and its completeness mark. Disposition counts were
checked against the issue lists. Semantic dispositions are the reasons above
and in the issue list; deterministic validation does not establish tag fit.

## Remaining work

There are 49 original assigned-tag findings and 204 suggested-addition entries
still open. PC-01 through PC-06 have resolved scope decisions; PC-07 remains open
for parent membership gaps. A later review that tests the revised parent
conditions must capture the new openings rather than reuse the frozen criterion.
