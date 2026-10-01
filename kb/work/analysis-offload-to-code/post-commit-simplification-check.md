# Post-commit simplification check

- **Checked:** 2026-10-01, after reorganization commit `d77388b4`, as commissioned by the operator.
- **Scope:** the shared contracts, four member types, six job instructions, worker rules, orchestrator skill/driver, direct downstream readers and generic type-conformance consumption. The working tree also contains the separate ledger implementation.
- **Purpose:** identify further cuts and missing delivery paths without weakening analysis requirements.

## Findings

### Generic type conformance does not receive the whole contract

The analysis workers receive the new shared files through declared inputs.
Generic type-conformance reviewers receive only the member-type snapshot;
their prompt scope does not allow general traversal of criterion links.
Their freshness baseline also tracks only the target and type text, so a
shared-contract edit does not stale that pair. Giving the reviewer link
access alone would not fix freshness.

The [proposal](../../reference/proposals/shared-analysis-contract-conformance.md)
states the options: factored shared-contract reviews, materialized complete
criteria, or self-contained member types. This is a consumer integration
gap, not a reason to remove the shared requirements. Workflow verification
already receives them; generic member-type conformance is not by itself a
complete check of the inherited contract.

### Exact repeated prose is now limited to the bootstrap rule

After excluding frontmatter, templates, headings and tables, the only
identical substantive paragraph across the workflow's instructions and
contracts is the six jobs' read-first rule. Keep it: the main instruction
must direct the worker to load its dependencies before relying on them.
Repeating the short entry rule serves that delivery path.

No live job, test or constructor still names the removed judging-norms
file. Its remaining mentions are historical workshop records and the map's
description of the removal. No live consumer still treats the overview as
the owner of common record fields or quotation rules.

### Theory requirements are the largest remaining shared reading block

Every record-authoring worker receives the theory account and qualifiers,
even though they apply only to theory routes. Moving them into another
file would save nothing if each job still declares it. A reduction would
require either narrowing which worker supplies these findings or a tracked
conditional-loading contract. That changes responsibility or delivery;
it is not a safe prose-only cut. Retain the present applicability rules.

### Memory findings have several representations

The profile, local declarations/annotations, Write side, Read-back and
Comparison rationale can restate a finding. The profile's local-reference
requirement is deliberate: it validates without the other members.
Removing local annotations would surrender that property and require
whole-set validation at the earlier acceptance boundary.

The present safe rule is already in the contract: narratives trace mechanisms
and reference records; Comparison rationale explains non-obvious mappings
and unions instead of repeating classifications. Enforce that rule in
review before dropping sections or weakening the reference requirement.

### The epistemic ledger remains expensive to author

Its 17 fields separate content change, function, evidence, authority and
later behavioral consequence. The repetition limit already permits `see
<ID>` for a field owned by a declared record. Use that reference form
before deleting fields. Further reduction needs a proposed equivalence
between fields and a representative finding that remains assessable after
the merge; a smaller table alone does not establish it.

## Disposition

No additional safe deletion was established. Keep the compact bootstrap
rules, field vocabularies, templates and evidence distinctions. The next
concrete design issue is generic review delivery and freshness, recorded
in the proposal. Larger output or responsibility changes remain separate
choices. No external-system run or generic conformance assay was performed
in this check; findings come from source inspection and the retained
reorganization tests.
