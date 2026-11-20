---
description: "Proposal: check formal links against their source collection’s declared permissions, report contracts the validator cannot read, and leave judgments about meaning to review."
type: reference/types/design-proposal.md
---

# Formal link permission check

A link can resolve to the right file but use a label the writer was not authorised to use. For example, the [reference contract](../COLLECTION.md) permits `derived-from` for a tracked source, not for a theory note. Changing only the destination should change the permission verdict. Looking up the label in the shared catalogue cannot distinguish the two cases.

**Recommendation:** give `commonplace-validate` one permission check across collections, not one global list of permitted labels. Have it read permissions from the contract that writers use. Start with a diagnostic trial; do not make existing projects fail merely because they have not migrated their contracts.

## Current state (as of 2026-11-20)

[ADR 019](../adr/019-collection-owned-link-vocabulary.md) reserves shared label meanings but gives the source collection authority over destinations and local labels. The [collection-contract type](../../types/collection-contract.md#authoring-outbound-link-rules) also distinguishes formal labels from unlabeled external citations. The writing skill can interpret tables, per-destination blocks and prose. The [validator](../validation-contract.md) checks link health; it does not certify that a label is permitted for its destination. Some specialised types have their own linking conventions. None of these facts warrants treating an unrecognised declaration as an empty permission set.

## Candidate: one declaration for writers and the validator

Put the mechanically checkable permissions in the YAML frontmatter of each `COLLECTION.md`. Each entry names a destination and the formal labels permitted there. Keep the reader need beside each permission so writers need no parallel table. Leave search guidance and explanations in prose. The field names and row layout are open; the constraint is that changing a permission in one place changes both what the writer reads and what the validator accepts. `any` includes `external`; a narrower path such as `reports/retained` does not authorise its siblings.

For each formal use, the validator would resolve the artifact’s source collection, its type, and the target destination. It would apply the collection permission plus any explicitly applicable type-specific rule. A specialised type may govern its own link form; it cannot grant external access that the collection has not authorised. If the rules conflict and no precedence has been declared, report the conflict at the declaration rather than guessing at every link.

Recognise uses by **declared position and syntax**, not by searching for a catalogue word. Start with labelled entries in declared footer sections. An unknown label in that position must still be checked. A fenced example, quoted example, prose mention, or ordinary unlabeled citation is not a formal use. A distinct formal surface, such as a named lineage footer whose heading supplies the relation, needs its own recognition rule before the checker can claim to cover it. Malformed entries in a declared formal section must not disappear as prose.

Return distinct findings:

- **Unauthorised use:** identify the source location, label, resolved destination and governing declaration. The writer can change the link; a collection maintainer can instead change the permission if the use should be allowed.
- **Cannot check:** identify the missing or unreadable declaration, unsupported formal surface, ambiguous type rule or unresolved destination. A collection that explicitly declares no formal links is checkable; a collection without a declaration is not. Show unchecked collections and surfaces in the run summary, even if no recognised links were found.

The declaration warrants a verdict about **permission only**. An authorised `derived-from` link may still point to a source from which the claim cannot be reconstructed. Semantic review must judge that claim, a reversed assertion, or a local gloss that changes a reserved meaning. When registering a new shared name, the catalogue maintainer must also check earlier local uses; finding the spelling is mechanical, deciding compatibility is not.

## Alternatives

- **Require a regular Markdown permissions table instead of structured frontmatter.** Writers and the checker could consume the same rows, keeping reader needs visible in rendered contracts. This is preferable if existing path restrictions and type rules can be represented without parsing prose inside cells. It still requires migration: a table that only looks regular is not a reliable declaration.
- **Keep the present formats and use collection-conformance review.** A reviewer can interpret prose and judge whether an assertion fits. This avoids migration and remains useful for meaning, but a clean deterministic run would still say nothing about permission. Inferring a permanent permission map from a model’s reading would introduce a second authority unless a maintainer adopted it as the contract itself.
- **Check every label against the global catalogue.** Cheap to implement, but it would reject legitimate local labels and accept registered labels at forbidden destinations. It tests a different rule.

## Adoption test and requested commitment

Decide first whether to authorise a **report-only trial** on copies of representative contracts. No trial, rewrite of live contracts, or validation failure is authorised by this proposal. Compare the two single-declaration formats on an existing labels table, a prose contract, a restricted subdirectory, and a specialised type. The maintainer’s reading of each original contract supplies the expected permissions; disagreements reveal a contract decision, not a parser bug to hide.

The trial must distinguish an allowed label from the same label at a forbidden destination; accept an authorised local-only label; distinguish `external` from an internal destination; and leave prose, examples and unlabeled citations alone. Include a malformed footer, an unreadable declaration and an unsupported type surface. None may produce a clean bill of health. A permitted but semantically false assertion should pass the permission check: that negative control keeps the checker from claiming review’s job.

Prefer the format that reproduces the agreed verdicts without a second maintained permission list. If neither does, retain semantic review and revise the declaration design. Enable failures only after maintainers can account for every in-scope contract and formal surface as checked or explicitly excluded, and have reviewed the violations in the trial. Existing installations own their contracts; refreshing the library must not silently rewrite them. Making the check blocking, including how an existing project adopts it, is a separate decision.
