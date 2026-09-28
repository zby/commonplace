# Directory artifacts: validating a set of documents as one artifact

## Commission

Posed by the operator on 2026-09-28. Commonplace validates one Markdown
document at a time: a `type:` line names a type spec, the spec's schema
states the document's structure, and type rules in the validator add what
a schema cannot express. The agentic-system analysis output is becoming a
set of four typed documents in one run directory, whose integrity (a
manifest of member hashes, identity agreement, identifiers declared once
across members, a profile citing records another member declares) is a
property of the set, not of any member. During the transition the
operator directed that these checks become a validator type rule on the
set's entry document and that a run directory validate as one artifact,
then judged that extending validation from single notes to directories
is an architectural change to the validator's model and must be planned
before it is implemented. This workshop owns that planning.

A candidate implementation exists in git history as commit `6d8d9fd0`
("Check the analysis set through a type rule on the overview"), made
under the mid-flight direction and reverted pending this workshop. It is
evidence of what the change touches, not a decision: a set rule in
`validation.py`, directory-to-overview resolution in `project_paths.py`,
a sweep that yields the overview for such a directory, and consumers
(publication, the comparison loader) calling validate instead of
re-checking.

## Question

How should the validator model an artifact composed of several typed
documents in one directory, so that validating the directory gives the
same guarantees as validating a note, without a general manifest
framework the repository does not yet need?

Decision points:

1. **Where the manifest lives.** A field in an entry document's
   frontmatter (the overview's `members`, as designed), or a directory-level
   manifest file. The entry-document form keeps one `type:` line per
   artifact and reuses the existing type-rule mechanism; the file form
   separates set identity from any member's content.
2. **Which mechanism carries the set check.** A type rule on the entry
   document's type, which any validation of that document triggers; or a
   new artifact kind the validator recognizes by directory shape. The
   type-spec contract already states that schemas cannot dereference and
   that such checks live outside the schema.
3. **How a directory is recognized and reported.** By the presence of an
   entry document whose type declares a manifest; what
   `commonplace-validate <dir>` and a collection sweep do with it; how
   diagnostics are attributed to members.
4. **What the schema layer can absorb.** Manifest shape, member type
   enum, disposition-conditional cardinality are schema-expressible and
   already in the overview schema. Everything that opens another file is
   not.
5. **What depends on it.** Publication, the comparison loader, the
   handoff, run-state verification, the site build, and the landscape
   bundle each either call validate or re-check; the transition plan's
   revised layering lists the intended split, with source-bound checks
   confined to run-state verification.

## Boundary and inputs

The analysis set is the only instance today and the evaluation boundary:
the design must serve it and must not be sized for instances that do not
exist. Inputs: the [transition plan](../agentic-analysis-output-documents/transition-plan.md)
and its revised-layering section; the
[consumer inventory](../agentic-analysis-output-documents/consumer-inventory-20260928.md);
the member type specs under `kb/types/`; the
[type-spec contract](../../types/type-spec.md) and the
[validation contract](../../reference/validation-contract.md); commit
`6d8d9fd0` and its tests. The operator has also asked for a review of the
analysis code's size and its redundant checks, which this workshop may
inform but does not own.

Coupling: the [output-documents workshop](../agentic-analysis-output-documents/README.md)
owns the set design and the producer transition, whose remaining commits
proceed on the approved plan with set checks in run-state verification.
The refresh batch in `kb/work/agentic-memory-refresh/batch-01-handoff.md`
waits on that transition, not on this workshop.

## Closure

Close when an ADR records the directory-artifact model the validator
adopts, its implementation has landed with tests, the analysis set
validates through it from a clean checkout, and the redundant checks it
replaces in run-state verification, publication and the comparison loader
have been removed. If the decision is to keep set checks outside the
validator, record that and close without implementation.
