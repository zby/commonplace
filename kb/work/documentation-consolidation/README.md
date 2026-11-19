# Documentation consolidation

Posed by the operator on 2026-11-18 and refocused on 2026-11-19.

## Motivation

Documentation grows, goes out of date, and misleads. Agents rarely read free-standing reference files, and humans find long reference manuals inconvenient when deciding what to do. Adding or reorganizing prose files does not fix that.

Every document needs a clear answer to two questions:

1. **What exact task does this document serve, and for whom?** If no concrete task needs it, retire it after rehoming anything unique.
2. **Where does that task activate?** Move rules, procedures, and tool references onto the **activation path** — the surface already loaded at the point of use (just as `cp-skill-write` names `commonplace-validate` at its validation step).

## Activation paths and document roles

- **Agent activation path.** Rules, procedures, and tool invocations belong where the triggering task loads them: a skill body, a collection contract, a type spec, `AGENTS.md` (only for cross-task rules with no single trigger), `--help`, a validator message, a test, or a comment beside the constrained code. A pointer in `AGENTS.md` that says "for task X, read Y" is a skill in the wrong place.
- **Human overview.** Assume the human can use an agent, and that the agent knows how to retrieve current operational details (via skills, `--help`, and live code). Aim human-directed docs at stable, higher-level concepts that let a person choose a request or decide whether to run a workflow — what it does, what it may publish, what it costs, and when it needs a decision — rather than volatile flags, inventories, or implementation detail.
- **Reference and architecture.** Kept only where code, `--help`, and ADRs do not cheaply supply the answer (cross-component invariants, composed current state across amended ADRs, or declared project frames). Prose copies of behaviour drift and should be cut once their unique detail sits on an activation path or in `--help`.

Use the [reference collection's economy tests](../../reference/COLLECTION.md#text-contract-and-fidelity) and the [seven-case documentation study](../../theory/evidence/seven-documentation-cases-left-routing-and-synthesis.md) as the baseline. Coordinate with [ADR routing](../adr-routing/README.md) where the needed context is a binding ADR; do not build a parallel ADR index here.

## Current order of work

1. **Review, revise, and command activation paths (completed in working tree).** Moved the operational surface of `README-REVIEW-SYSTEM.md` into `cp-skill-review` (read-only) and `cp-skill-revise` (may write the note), extracted Pi reviewer setup into `kb/instructions/run-review-from-pi.md`, removed the review-guide pointers from `AGENTS.md` and `AGENTS.md.template`, and shrank `README-REVIEW-SYSTEM.md` to a high-level human overview. Moved `commands.md`'s unique details into live `--help`, shrank `commands.md` to a checked command catalogue, and wired it into `AGENTS.md.template` beside `AGENTS.md`.
2. **Check remaining documentation by task and activation path.** Using the [reference analysis](./reference-analysis.md) as input, inspect each remaining document, decide what task actually needs it, move its live rules and command mentions onto the relevant activation path (or `--help`), fix stale statements, and retire documents that serve no live task.
3. **Human entry points.** Decide how the [Getting started draft](./getting-started.md) (commissioned by [getting-started.brief.md](./getting-started.brief.md)) fits with [kb/reference/README.md](../../reference/README.md).
4. **Skill pruning (later).** Once activation paths settle, review existing skills and remove any that add trigger noise without earning a dedicated activation path.

## Files in this workshop

- [reference-analysis.md](./reference-analysis.md) — empirical audit of the 30 top-level `kb/reference/` documents (duplication, unique content, stale statements, live consumers), retained as input for step 2.
- [getting-started.md](./getting-started.md) and [getting-started.brief.md](./getting-started.brief.md) — draft human entry point and its write brief trial.

## What closes this workshop

- Every retained reference document has an explicit task it serves, and stale copies are removed or moved onto their activation paths.
- Agent tasks reach their needed rules and commands along their natural activation paths without being told a reference file's name; human overviews stay short and decision-oriented.
- Any skill removals decided in step 4 are applied or split out, and untested cases are recorded. Opening this workshop does not authorize an unchecked repository-wide deletion sweep.
