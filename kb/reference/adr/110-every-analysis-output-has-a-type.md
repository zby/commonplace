---
description: "Every accepted output of an analysis run is a typed document its worker writes whole — boundary, reports, reconciliation, verifications, synthesis, profile — with the type carrying the shape and the instruction carrying the mission"
type: reference/types/adr.md
status: accepted
---

# 110 — Every analysis output has a type

**Status:** accepted
**Date:** 2026-10-06
**Amends:** [ADR 098](./098-separate-analysis-reconciliation-from-synthesis.md), whose reconciliation member was code-wrapped from a body fragment; [ADR 084](./084-kind-rules-live-in-type-specs-and-operations-in-instructions.md) is applied here to the analysis method, not changed.

## Context

The analysis method's outputs were specified unevenly. The analyst reports
and the profile had type specs with schemas, and their workers wrote them
whole. The reconciler wrote a body fragment that code wrapped in frontmatter.
The three verifications and the synthesis had no type: their sections, the
blocker grammar code routes on, and the description-length rule lived in job
instructions and in hand-written checks. The boundary document's field set,
controlled values and conditional section lived in the boundary job and in
code. An independent checker had to reconstruct the author's task to learn
what an output must be.

The operator asked that the method follow the repository's division: types
say what a conforming artifact is, instructions say how to produce or check
it, and a worker never sees a mechanism the instruction does not mention.

## Decision

Every accepted output of a run is a document under a type spec with a
schema, written whole by its worker, frontmatter included, and checked at
acceptance against that schema plus the run's identity. The types are the
boundary, the runtime, memory and epistemic reports, the reconciliation, the
verification (one type, with `verifies` naming the stage), the synthesis and
the profile. Where two types share field definitions, one schema references
the other's rather than copying them. The manifest names the model and
effort of the run once; it is one model per run.

The type owns the output's shape: fields, sections, controlled values, what
it may and may not contain. The shared record, source and boundary contracts
own the criteria several types share, and each job loads the contracts it
judges against. The job instruction owns the mission: situation, purpose and
end state, boundaries, inputs and the acceptance check. It may remind a
worker of a criterion the contracts carry; it does not define one. Code
enforces what it can read from the typed document and checks run-specific
facts the type cannot state, such as that the frozen source is the one code
froze.

Operativity: workers consume the type through their declared dependencies;
acceptance checks and `commonplace-validate` consume the schema and type
rules with binding force; later jobs read typed documents as text.

Warrant: schemas establish shape and controlled values; acceptance checks
establish identity, reference resolution and quotation occurrence. Nothing
in this decision establishes that content is correct.

## Considered alternatives

**Fragments wrapped by code.** The reconciliation's prior form. It saved the
worker four frontmatter fields and made that output the one document whose
contract was not its type.

**A section in the overview type for verifications.** The overview describes
the verification subsections it carries, so the rule could have lived there.
Verifications are documents in the run directory in their own right and two
of the three verifiers did not load the overview type.

**Per-member model fields.** Considered for recording the worker; rejected as
complication while one model writes a whole run. The manifest carries it.

**Leaving the three shared contracts under `instructions/`.** Kept. The plan
that commissioned this work made layout free; the contracts are type-side by
function and consumed by declared dependency wherever they sit.

## Consequences

An output can be judged from its type and contracts without its instruction;
a withheld-instruction review of an accepted epistemic report recovered or
partly recovered twelve of seventeen operative criteria and missed none that
lived only in an instruction. Instructions shortened by a third to a half,
and the duplicated criteria they carried now have one statement each.

The cost is in reminders: trimming a worker-rules paragraph coincided with a
same-model profile losing supported findings, and the reminder was restored.
Where a reminder is dropped, a model run is the only test of whether the
contract alone carries the behaviour.

This holds for the analysis method's run outputs. Request packets, answers
and change files are code-written or code-checked working files, not typed
documents, and the retained sets published before this date keep their
earlier forms.
