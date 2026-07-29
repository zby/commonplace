# Full mechanism reclassification protocol

**Date:** 2026-07-29

**Status:** pre-registered option-A dispatch record; read-only classification only.

## Purpose

Replace the unreproduced single-pass mechanism disposition ledger with k=3 blind classifications for every row on the current surface. This run supplies maintainer evidence; it does not adopt `explained-by`, `operates-through`, or any other identifier and does not authorize migration.

## Rebaseline

The current surface contains 129 exact source→target tuples:

- 82 active registered `mechanism` edges: all 79 tuples from the prior review remain, plus 3 additions;
- 47 of the 49 exact deferred `grounds` tuples: 2 have disappeared and are attrition, not rows to classify.

The three added active `mechanism` tuples are:

- `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md:57` → `kb/notes/llm-context-is-a-homoiconic-medium.md`;
- `kb/notes/reflection-buys-addressability.md:68` → `kb/notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md`;
- `kb/notes/the-bitter-lesson-selects-production-methods-not-representational.md:70` → `kb/notes/localized-retention-pays-where-change-is-sparse-in-a-matching.md`.

The two disappeared deferred tuples are:

- baseline EX: `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md:78` → `kb/notes/definitions/reflective-system.md`;
- baseline OP: `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md:76` → `kb/notes/a-derived-copy-of-recomputable-truth-must-be-checked-or-absent.md`.

Two surviving tuples moved without semantic attrition:

- active `mechanism`: `kb/notes/retrieval-failure-is-reflection-failure.md` → `kb/notes/stale-indexes-are-worse-than-no-indexes.md`, line 38 → 40;
- deferred `grounds`: `kb/notes/a-consumption-channel-delivers-force-without-the-history-that.md` → `kb/notes/the-four-field-record-exposes-an-efficiency-security-and-sovereignty.md`, line 77 → 59.

Every current source and target resolves. The scanner found no unsupported active syntax or duplicate tuple.

## Blind dispatch

Every row receives three votes from three fresh isolated classifier contexts. The 129 tuples are assigned neutral IDs by sorting the SHA-256 digest of `source-path→target-path`, then distributed round-robin across four batches. This changes only presentation and load distribution; origin and prior disposition remain available to the orchestrator for scoring and hidden from classifiers.

Each classifier reads the full source and target artifacts, or generous excerpts only when an artifact is unusually long. The source footer and its surrounding section must remain visible. Classifiers do not read workshop files, collection contracts, the catalogue, ADRs, prior reviews, other pass outputs, or git history.

The four classes retain the blind-test definitions:

- **EX** — the target is an explanatory account or general principle answering why or how the source claim/phenomenon occurs. Rejecting or revising the target prompts re-reading the source's causal argument, not automatically changing an implementation.
- **OP** — the target is a process, component, control path, artifact, or operational rule through which the source effect is literally produced. A target change prompts an interface, behavior, or operational fit review.
- **EN** — the target is a condition that must be available, true, or completed for the source claim/process to work, rather than the explanation or the operating path itself.
- **OTHER** — none of the above fits; the classifier names the relation in one line.

Before returning a class, each vote records short answers to the five boundary-application tests approved in the [adjudication packet](./mechanism-reversal-adjudication-packet.md): literal use, explanation counterfactual, operation counterfactual, prerequisite, and neither/OTHER.

## Acceptance rule

The dispatch is complete only if every non-attrited row receives exactly three votes and requested/actual model provenance is recorded without inference.

The replacement evidence ledger is usable only if at least 90% of rows have a stable majority of two votes or better. If stability falls below 90%, stop: do not treat any aggregate as an adoption basis and redesign the classification protocol.

Per row:

- **3/3 unanimous:** reproducible candidate disposition;
- **2/3 majority:** contested boundary row; report the majority but require explicit maintainer adjudication before migration;
- **three different votes:** UNSTABLE; no successor candidate;
- **runtime attrition:** exclude from denominators and account for the exact tuple.

EX, OP, EN, and OTHER remain mutually exclusive. EN and OTHER never enter either proposed successor cohort. No result of this run automatically changes an edge: even unanimous EX/OP rows remain candidates until the maintainer decides whether the two-consumer distinction earns registration and settles the identifier spellings.

## Required result

Write `mechanism-full-reclassification-results.md` with:

- rebaseline and runtime attrition;
- all 387 votes, confidence, boundary-test answers, majority, unanimity, origin, and prior disposition where one exists;
- aggregate stability and confusion against the prior review, with new rows reported separately;
- exact unanimous, contested, unstable, EN, and OTHER cohorts;
- strongest evidence for and against retaining an EX/OP split;
- reader and revision consequences without making the maintainer decision;
- requested and actual model provenance;
- changed paths and verification.

Validate the result and run whitespace/diff checks. Do not edit corpus edges, collection contracts, the catalogue, ADRs, durable instructions, or prior workshop results.
