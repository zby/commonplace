---
description: "Proposal: normalize autonomy and revision findings for cross-system comparison after source-based reviews establish useful distinctions"
type: ../types/design-proposal.md
---

# Normalized autonomy and revision comparison fields

## Problem

The [nearest-constructions supplement](../../articles/nearest-existing-constructions-to-a-witness-house.md)
compares systems against the automated software house conjecture's witness
conditions. Its judgments depend on component fixity, permitted revisions,
admission mechanisms, decision roles, operating modes and answer-oracle
access. Those findings need source evidence before they can support grades.

The main analysis requires these facts as prose on canonical records. It does
not normalize them for cross-system comparison. An author can audit a table
against those records, but the matrix machinery cannot rebuild that table.
The open question is whether stable comparison fields would save enough work
to justify another classification contract.

## Current state (as of 2026-09-05)

- The [producing skill](../../instructions/analyse-agentic-system/SKILL.md)
  and [result type](../../types/agentic-system-analysis-result.md) require
  evidenced prose for components used by inspected runtime routes and
  materially distinct revision mechanisms. Routine writes sharing a mechanism
  are grouped; memory revisions reuse the specialist's findings.
- Decision roles and answer-oracle access are separate questions. A human or
  computational process may propose, decide or veto. An answer oracle supplies
  an expected answer or reference outcome; model judgment alone does not
  establish one. A system may have both open-request and bounded experimental
  modes with different oracle access.
- Only memory findings have normalized comparison fields. Their vocabulary
  lives in `src/commonplace/lib/systems_matrix.py`; standing validation and
  publication check classifications and record references. Structural checks
  do not establish the truth of a classification.
- Retained results are byte-frozen and their public reviews pin SHA-256
  hashes. Requiring new evidence means regenerating results under new run IDs,
  not patching old outputs. No legacy fallback or compatibility path is part
  of this proposal.
- Normalization is deferred until several source-based reviews establish
  which distinctions are useful and consistently supported. The prose
  requirements do not add normalized fields or table-generation support.

## Option space

### Separate comparison fields

A distinct family could describe whole-runtime properties with its own scope,
vocabulary and validation. It would leave memory classifications tied to
memory mechanisms. This is the smaller change if only one additional family
is needed, but adds another contract to maintain.

If adopted, the new contract would apply to every result selected for those
comparisons. Missing required fields would fail selection and require a new
analysis; historical results would receive no compatibility exception.

### Shared comparison registry

A common registry could declare vocabularies, multiplicity, dependencies and
evidence requirements for several comparison families. One validator and
rendering path would consume it. This might reduce duplication if several
families prove necessary, but generalizing before the second family's
requirements are known adds work without demonstrated benefit.

### Continue comparing prose

Authors could keep deriving comparisons from cited canonical records. This
preserves flexibility while the distinctions settle and remains auditable
through those records. It leaves table construction manual. Normalization is
unnecessary if that cost stays small or the comparison questions change often.

Adding whole-runtime properties to the memory axes is not a candidate: their
scope differs. No normalized design is selected here.

### Candidate distinctions

The following delimit the questions, not a settled set of axes or tokens:

- **Component fixity:** parameter changes and identity pinning, assessed
  separately for each material distributed-parametric component role.
- **Revision mechanism:** what can change, what triggers a candidate, what
  admits or rejects it, and what permits rollback or recovery.
- **Decision roles:** who proposes, decides and can veto, with computational
  and human contributions represented without forcing a single owner.
- **Answer-oracle access:** supplied expected answers or reference outcomes,
  their providers, and the decisions they govern.
- **Operating modes:** open requests, bounded experiments or curricula, and
  the improvement triggers and oracle access specific to each mode.

Some findings may need per-component or per-route records rather than one
system-level value. Unknowns, multiple modes and different evidence strengths
must survive any normalization. Fixed model weights do not preclude learning
through retained knowledge, instructions or changed production machinery.

## Forces

- **Evidence before vocabulary.** Several regenerated reviews must show which
  distinctions change a comparison and can be supported without exhaustive
  provider inspection or a catalogue of routine writes.
- **Descriptive facts before grades.** Witness conditions belong to the
  consuming comparison. Normalized system findings must remain useful without
  adopting that article's threshold for autonomy.
- **Maintenance cost.** A second family adds vocabulary, validation and display
  obligations. A shared registry reduces some duplication but adds its own
  design and migration work.
- **One current contract.** New mandatory fields may exclude existing results
  until regeneration. Frozen historical evidence stays intact; preserving its
  eligibility is not a reason to add compatibility behavior.

## Operativity and warrant

Possible consumers are the matrix builder, table renderer, analyzer and
nearest-constructions supplement. A normalized family would be consumed as
retained evidence through validation and table generation; those readers would
need implementation before adoption. Until then, authors read canonical prose
records directly. No new machine consumer exists for these proposed fields.

A validator could check vocabulary, scope references and permitted evidence
statuses. It could not certify source support, actual autonomy or improvement.
Those judgments still require inspection of the producing run's evidence.

## Adoption criteria

Revisit normalization after several regenerated reviews expose recurring,
useful distinctions and their difficult cases. Adopt only when a named
comparison needs a reproducible table, its vocabulary and scope rules have
been reviewed against those records, and a reader implementation can reject
missing or unsupported inputs. Choose a separate family or a shared registry
from those requirements. Until then, retain the evidenced prose requirements.
