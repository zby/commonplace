---
description: "Proposal: make the runtime report's required route read-back and component fixity fields checkable by giving them a labelled-line form in record bodies and adding a presence rule to set validation"
type: reference/types/design-proposal.md
---

# Required route fields as labelled record lines

The runtime report type requires each route record to state immediate return, later read-back, delegated visibility, selection predicate, invalidation or expiry, and activation or effect, "with an explicit inapplicable or uninspected reason instead of an empty field". It requires component records to state source-native identity, representational form and storage substrate, with parameter change and version pinning separated for parametric components. Nothing checks these. A report can omit them and pass validation. This proposal records how the fields could become checkable and what the check would and would not establish.

## Current state (as of 2026-09-29)

- The requirements are prose in `kb/types/agentic-system-runtime-report.md` under Shared records. The runtime schema checks headings and their order only (`kb/types/agentic-system-runtime-report.schema.yaml`).
- Record bodies are free paragraphs. Shared-record validation checks ID syntax, duplicate declarations and reference resolution (`src/commonplace/lib/agentic_records.py`), not the content of a declaration.
- Authors already use labelled prose such as `Later read-back:` and `Delegated visibility:`. In the one retained set on main (`AAS-2026-09-28-pageindex-01`), all four route records in `runtime.md` carry `Later read-back:`, while none of the seven route records in `memory.md` carry that label. The memory report is authored under a different type with a shorter field list, so this is one observation and not a rate; the set-level counts from the batch 01 rerun are not on main yet.
- The batch 01 rerun trace audit (2026-09-28) records that Basic Memory's specialist report passed validation, then needed two correction turns for missing route read-back fields, heterogeneous objects and irregular kind headings, and that the specialist never opened the runtime type that defines the full field list.
- Route fields that live in a member other than the one that declares the route are written as annotations under `On <ID>` headings, not as declarations.

## The problem

A validator that ignores these fields lets an incomplete record through, and the omission is found only by a reviewer or a later correction turn. Because the fields have no structured form, a JSON schema cannot require them, so any check needs a convention for how a field appears in a record body.

## Options

### A. Labelled lines plus a Python presence rule

Fix a small vocabulary of field labels. A rule beside `record_reference_errors` checks that each declared `RTE-*` record contains every required label with a non-empty value, where an explicit `inapplicable` or `uninspected` with a reason counts as a value. Component records get an analogous label set.

- Smallest change to the current record style, which already uses labelled prose.
- Does not require reformatting existing sets, if the labels match what authors write; that needs measuring across retained sets.
- Does not judge whether a value is right.

### B. Structured sub-blocks per record

Each record carries a small list or table for the required fields, and free prose follows. Easier to parse and harder to omit a field silently, but a larger reformatting of the record grammar and of every existing set.

### C. Leave the fields to an assay

Add a gate criterion that asks whether each route answers every required field. Catches meaning as well as presence, but is an LLM check with cost and variance, and it runs after the fact instead of blocking publication.

### D. A and C together

Code blocks on missing or empty fields; an assay judges whether the answers are adequate. Presence and adequacy are separate questions and the audit observed both failures.

## Forces

- **Presence is not adequacy.** A label with `inapplicable` and a plausible reason passes any code rule, whether or not the reason is true. The audit records that a clean validator does not show that every route field is meaningfully answered.
- **Two authors, two field lists.** The memory report type carries a shorter route field list than the runtime type. A rule that applies to `memory.md` needs to choose which list governs, or exempt records the specialist declares.
- **Where a route is declared decides what is checked.** Declarations carry the full field set; `On <ID>` annotations add to another member's record and should not be held to it.
- **Label drift.** Free prose varies in wording (`Invalidation/expiry` versus `Invalidation or expiry`). The rule works only if the type fixes the labels exactly.
- **No backwards compatibility.** Under the repository rule, existing retained sets that fail the new rule are cleanup, not a reason to add a legacy path; whether to regenerate or fix them is a separate decision.

## Free choices

- The label vocabulary and its exact spelling.
- Whether a missing field is an error or a warning at first.
- Whether an `inapplicable` or `uninspected` value needs a minimum reason length or shape.
- Whether component fixity and theory-route guidance fields join the first version or follow after route fields.

## Operativity and warrant

Consumer: set validation (`commonplace-validate <run>/output --full`) and, through it, publication. Channel: code reading record bodies. Force: a missing or empty required field blocks publication, for the labelled fields only. The check's warrant is presence of text under a label. It stops there: it says nothing about whether the recorded read-back, expiry or activation is true of the system, which stays with the analyst and any review of the report.

## Adoption criteria

- The label vocabulary is chosen and written into the runtime report type in one place.
- A measurement across every retained set on the target branch shows how many existing records would fail a candidate rule, so the operator can decide between fixing records and relaxing the vocabulary.
- Tests cover an omitted field, an empty field, an explicit `inapplicable` with a reason, an annotation heading, and a record in the memory member.
- The specialist instruction links the runtime type's field list, so the rule and its source of truth reach the author at entry.

## Related

- [Runtime report type](../../types/agentic-system-runtime-report.md) — owns the fields this proposal would make checkable.
