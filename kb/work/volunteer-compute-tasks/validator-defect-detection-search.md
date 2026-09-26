# Validator defect-detection search

Find explicit structural violations that Commonplace's validator fails to
report. Use committed artifacts and contracts as inputs, introduce controlled
defects in temporary copies, and return small cases whose expected result is
easy to establish. This tests whether routine validation actually catches the
mistakes it promises to catch. Follow the [shared handoff](./README.md).

## Inputs and baseline

Read the [validation contract](../../reference/validation-contract.md),
[validator implementation](../../../src/commonplace/lib/validation.py),
[CLI tests](../../../tests/commonplace/cli/test_validate_notes.py),
[type-resolution tests](../../../tests/commonplace/lib/test_type_resolver.py),
and [tag validation tests](../../../tests/commonplace/lib/test_validation_tag_readme.py).
Use type specs, schemas, collection contracts, and representative artifacts
from the pinned checkout. No review database or ignored source snapshot is an
input to this task.

```bash
python -m pytest tests/commonplace/cli/test_validate_notes.py tests/commonplace/lib/test_type_resolver.py tests/commonplace/lib/test_validation_tag_readme.py
```

## Search commission

Build a table of testable rules from the committed deterministic contracts.
For each rule, identify its authority, applicable artifact types, validation
scope, expected severity, and documented exceptions. Restrict the table to
rules enforced by schemas or deterministic code; prose requirements assigned
to semantic review are outside the task.

Generate temporary fixtures from committed examples and create controlled
mutations. Candidate families include:

- Removing schema-required fields or headings, or changing a field to a value
  its schema prohibits, while preserving valid frontmatter and type identity.
- Breaking a supported local link or a type-spec schema reference.
- Making a declared tag completeness claim false by removing required coverage.
- Introducing an explicitly forbidden archive link or invalid redirect map.
- Combining violations across artifacts and types to expose checks that are
  skipped, incorrectly dispatched, or suppressed by another diagnostic.

Establish each rule in isolation before testing combinations. Validate the
original and mutated fixtures with the same command. Record the actual
diagnostics, not only the exit code: link warnings intentionally exit zero.
Removing all frontmatter produces bare text, which deliberately opts out of
most structural checks; that alone is not a bypass. Likewise, an explicit-file
run and a collection run need not check the same scope.

Explore multiple artifact shapes, local and global types, collection scopes,
and combinations of mutations. Choose search methods and bounds from the
available compute. Shrink both the fixture and mutation set for every finding.
Use a simple independent check of the violated property where possible; do not
derive expected behavior by calling the production check under investigation.

Exclude quotation support, semantic correctness, new policy proposals, and
rules requiring absent private state. Keep unclear contracts in a short
separate list. A crash on otherwise supported input may be reported, but a
cleanly rejected malformed document is not an undetected violation.

## Acceptance

Each finding contains an exact rule citation at the pinned revision, a small
original fixture, the controlled change, one replay command, and the missing or
incorrect diagnostic. The original must satisfy the rule under test. Restoring
the changed input must restore that property. Preserve the failure when
removing unrelated files and defects.

Return deterministic regression tests and at most five distinct failure causes.
We should be able to inspect the changed field, link, or membership and see why
the expected diagnostic follows without reviewing the generator. The reusable
generator and rule table are supporting material, not substitutes for findings.

If no defect survives minimization and contract checking, report the tested
rules and bounds honestly. A high detection rate over planted defects does not
establish accuracy on ordinary KB edits. The useful retained outputs are
confirmed validation gaps and compact regression fixtures that protect future
validator changes.
