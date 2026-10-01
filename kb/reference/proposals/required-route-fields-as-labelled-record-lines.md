---
description: "Proposal: make common route fields checkable across runtime and memory declarations through one shared contract, labelled record lines, and deterministic presence validation"
type: reference/types/design-proposal.md
---

# Required route fields as labelled record lines

The runtime report type requires each route record to state immediate return, later read-back, delegated visibility, selection predicate, invalidation or expiry, and activation or effect, "with an explicit inapplicable or uninspected reason instead of an empty field". A report can omit these fields and pass validation. This proposal would make their presence checkable under one contract shared by runtime and memory declarations. Component fixity and conditional theory-route fields remain outside the proposed first version; their applicability rules need to be settled before adding checks.

## Current state (as of 2026-09-29)

- The requirements are prose in `kb/types/agentic-system-runtime-report.md` under Shared records. The runtime schema checks headings and their order only (`kb/types/agentic-system-runtime-report.schema.yaml`).
- Record bodies are free paragraphs. Shared-record validation checks ID syntax, duplicate declarations and reference resolution (`src/commonplace/lib/agentic_records.py`), not the content of a declaration.
- Authors already use labelled prose such as `Later read-back:` and `Delegated visibility:`. In the one retained set on main (`AAS-2026-09-28-pageindex-01`), all four route records in `runtime.md` carry `Later read-back:`, while none of the seven route records in `memory.md` carry that label. The memory report is authored under a different type with a shorter field list, so this is one observation and not a rate; the set-level counts from the batch 01 rerun are not on main yet.
- Label counts do not establish missing answers. PageIndex memory record RTE-5 says “Later read-back is RTE-8 and RTE-9” without the colon label. Runtime records put multiple labels in a paragraph and vary labels such as `Expiry`, `Invalidation`, and `Invalidation/expiry`. Even records with the answers would need reformatting for one exact label per line.
- The batch 01 rerun trace audit (2026-09-28) records that Basic Memory's specialist report passed validation, then needed two correction turns for missing route read-back fields, heterogeneous objects and irregular kind headings, and that the specialist never opened the runtime type that defines the full field list.
- Route fields that live in a member other than the one that declares the route are written as annotations under `On <ID>` headings, not as declarations.

## The problem

A validator that ignores these fields lets an incomplete record through, and the omission is found only by a reviewer or a later correction turn. The fields have no agreed syntax that the current schema checks. A deterministic presence check needs a convention for how a field appears in a record body. It also needs a shared contract: moving a declaration between runtime and memory members should not change its common requirements.

## Options

### A. Labelled lines plus a Python presence rule

Define the common route-field contract once in the analysis overview type, alongside the shared record grammar, and have both member types reference it. The contract would cover immediate return, later read-back, delegated visibility, selection predicate, invalidation or expiry, activation or effect, and evidence limits. Lens-specific requirements remain in their member types.

Require one bullet line per field, with an exact label and a non-empty value. Each required label occurs exactly once within the declaration. An `inapplicable` or `uninspected` value must include a non-empty reason after a fixed separator; no minimum reason length is proposed. Free prose and evidence passages can follow the field list.

A Python rule would check canonical `RTE-*` declarations in either member and local `MEM-RTE-*` proposals. It would ignore quoted source material and fenced excerpts, stop at record and section boundaries, and exclude `On <ID>` annotations. An annotation cannot satisfy a missing common field in a declaration.

This keeps the existing Markdown record grammar, but requires reformatting even where paragraphs already contain all the answers. It checks presence and uniqueness, not whether an answer or reason is adequate.

### B. Structured sub-blocks per record

Give each record a distinct structured block, such as a table, for the required fields. This would use the same shared contract as A but add a container grammar. A's bullet lines already separate the fields; a stronger container needs a further consumer requirement to justify its additional structure.

### C. Leave the fields to an assay

Add a gate criterion that asks whether each route answers every required field. Can assess meaning as well as presence, but has LLM cost and variance. It would block publication only if the publication procedure required a passing result.

### D. A and C together

Code rejects missing, empty or duplicate fields; a dedicated assay judges whether the answers are adequate. Presence and adequacy are separate questions, but the observed omissions do not by themselves establish the need for a new assay beyond existing substantive review.

The recommended candidate is A first, with errors once the shared contract and retained records are updated. Substantive review remains necessary; a dedicated assay is a separate adoption choice. This is a proposed selection, not an adopted contract.

## Forces

- **Presence is not adequacy.** A label with `inapplicable` and a plausible reason passes any code rule, whether or not the reason is true. The audit records that a clean validator does not show that every route field is meaningfully answered.
- **Two authors, one common contract.** The memory report type currently carries a shorter route field list. Both authors need the same common contract at entry; exempting memory declarations would leave the omission path open.
- **Declaration ownership.** Declarations carry the common field set regardless of member; `On <ID>` annotations add lens-specific fields and should not be held to it.
- **Label drift.** Free prose varies in wording (`Invalidation/expiry` versus `Invalidation or expiry`). The rule works only if the type fixes the labels exactly.
- **No backwards compatibility.** Under the repository rule, existing retained sets that fail the new rule are cleanup, not a reason to add a legacy path; whether to regenerate or fix them is a separate decision.

## Free choices

- The label vocabulary and its exact spelling.
- The separator between an explicit `inapplicable` or `uninspected` value and its reason.
- Whether retained records should be reformatted, substantively repaired, or regenerated, based on the measurement below.
- Whether evidence from substantive review warrants a dedicated adequacy assay later.
- The applicability rules needed before proposing component fixity or theory-route checks.

## Operativity and warrant

Consumer: set validation (`commonplace-validate <run>/output --full`) and, through it, publication. Channel: code reading record bodies. Under A or B, the proposed rule would produce an error for missing, empty or duplicate required fields; publication would require validation to pass. The same check would run during local specialist validation so omissions can be corrected before integration. The check's warrant is presence of text under a label. It stops there: it says nothing about whether the recorded read-back, expiry or activation is true of the system, which stays with the analyst and any review of the report.

Under C or D, the additional consumer would be the review pipeline applying the criterion to the report. Its warrant would be model judgment against the shared contract and available evidence, subject to variance and missed errors. Making that result binding on publication would require an explicit procedure change.

## Adoption criteria

- The common field contract and exact line grammar are defined once in the analysis overview type and referenced by both member types. Local memory proposals and finalized declarations have the same common requirements.
- A measurement across every retained set on the target branch distinguishes records that need only reformatting from records that lack answers or need further inspection. Label counts alone do not measure analytical completeness. Records needing both are identified separately so the cleanup estimate includes both costs.
- Existing records are brought into conformance before the rule becomes a required publication check. Missing answers are investigated or explicitly bounded, not replaced with invented findings to satisfy the parser.
- Tests cover omitted, empty and duplicate fields; explicit `inapplicable` and `uninspected` values with and without reasons; labels inside source quotations and fenced excerpts; record boundaries; annotation headings; local memory proposals; and canonical declarations in either member.
- The coordinator and specialist entry instructions point to the shared contract, and local validation catches the same field omissions as set validation.

## Related

- [Runtime report type](../../agentic-systems/types/agentic-system-runtime-report.md) — currently states the route fields this proposal would make checkable.
- [Memory report type](../../agentic-systems/types/agent-memory-analysis-report.md) — currently supplies a shorter route field list; would reference the common contract.
- [Analysis overview type](../../agentic-systems/types/agentic-system-analysis-overview.md) — owns the shared record grammar and would own the common route-field contract.
