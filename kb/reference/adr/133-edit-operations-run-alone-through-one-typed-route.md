---
description: "Register edit operations and edit results as types; run one operation alone through a code route that retains its observation; revise runs every pass through it; per-item operations run twice"
type: reference/types/adr.md
status: accepted
---

# 133 — Edit operations run alone through one typed route

**Status:** accepted; implemented under the operator's commission for the edit-operation group.
**Date:** 2026-11-15
**Extends:** [ADR 132](./132-review-atoms-retain-observations-behind-current-results.md), from review operations to edit operations. Its observation, acceptance and fixture boundaries apply unchanged.

## Context

The operator wants every improvement operation to be an atom: a typed instruction file, file inputs, a typed stored result, runnable and testable alone. ADR 132 made review operations atoms. Edit operations were not. The simplification passes shared a shape by habit, the ten fix strategies were sections of one codebook, and only the revise workflow could run a pass. A pass could not be run alone on one note, repeated on the same input or rerun from retained inputs.

An edit differs from a review in one way that matters for storage. A review result is a statement about a note that may since have changed, so it needs freshness. An edit result is a candidate made from one exact input text. It either names that text's hash or is about another text.

## Decision

**Register two shared types.** The [edit-operation type](../../types/edit-operation.md) declares `effort`, `decision` (`none` or `per-item`), and the best-effort `depth` and `responds-to`. Its schema requires `## Steps`, `## Report` and `## Preserve`. The field is named `depth`, not `level`, because `level` already names a review finding's severity. The [edit-result type](../../types/edit-result.md) records one run with outcome `changed`, `unchanged`, `proposed` or `problem`. The worker supplies content: the outcome, the change lines, the proposals, the removed links and the report. Code supplies provenance: the operation and its hash, the input hash, the candidate hash, the model, the run and the launch. The candidate text is a file in the observation, not a field. An edit result has no freshness state and no current-result file.

**Acceptance is deterministic and shared.** Code checks the outcome the operation's `decision` allows, the schema, and the bounds: title, H1, type, brief declaration, `user-verified` removal and no new validation failure, as before, plus two new checks. Every link target of the input stays unless the result names its removal. Every quoted span stays: a Markdown blockquote, or a quotation the validator pairs with a `verbatim` citation. A `proposed` result's quotes must each occur exactly once in the input, by the shared prose quote matcher. An operation's own `## Preserve` section binds the worker only. A rejected answer goes back to the worker; a worker problem becomes a `problem` result; controller failures stop.

**One code route.** `commonplace-review run edit OPERATION NOTE [--input ROLE=PATH] [--text PATH]` runs one operation on one note and writes nothing to the checkout. It reuses the review observation machinery: each execution's exact text, operation, prompt, supplied inputs and contract are captured under the run's `artifact/edits/`, and `run edit --fixture` reruns one execution. Every worker receives [execute a revision pass](../../instructions/simplification-passes/execute-a-revision-pass.md) as its `execution` input, which carries the shared contract. The revise workflow's pass launch moved onto this route, so one writer produces every pass candidate. Revise keeps its own composition: plan, order, strike stops and publication. Which passes stop for strikes now follows each operation's `decision` instead of a list in code.

**A per-item operation runs twice.** The first run returns `proposed`. The operator strikes entries. The second run receives the answered list as its `answers` input and returns `changed`. Code refuses a candidate that changed a struck entry's passage. The answered list was at first the revise workflow's strike-list format; [ADR 134](./134-stops-record-the-operators-answers-in-one-typed-file.md) replaced it with the shared answers type.

**Convert the material in one change.** Readability-and-flow, narrow-overclaims and opening-and-title declare `decision: none`; plain-wording and abstractions declare `per-item`; audit-a-prior-pass and place-external-systems name the extra files they read as input roles. The ten fix strategies are one operation, "fix a finding by a named strategy", which takes the finding as its `finding` input; fix reports keep citing a strategy by its anchor. Split-out-a-treatment stays an instruction because it writes a second file. The full pass's body edits and copyedit stay steps of the full pass.

## Considered alternatives

**Session-run edit operations, as the improvement-procedure proposal designed.** Rejected for testability. Running an operation alone, repeating it on one input and rerunning it from a fixture all need the exact inputs retained, which code already does for reviews. A session agent can still call the command.

**Keep revise's own pass launch beside the new route.** Rejected. Two writers would maintain two acceptance paths for the same candidate, which ADR 132 rejected for review results.

**Wait for the answers type before admitting per-item operations.** Rejected. The revise strike-list format already carries the operator's strikes with reasons, so per-item operations can run alone now. The shared answers type and its validator are the next change.

**A check that only approved entries changed the text.** Not adopted. A check that every changed region lies inside an approved quote would refuse abstractions, which replace a term throughout. Code checks only that struck passages are unchanged.

**Split the fix strategies into ten operations.** Deferred. Each strategy is a pattern and a typical fix with no steps or preserve rules of its own. A strategy becomes its own operation when its record shows it needs separate calibration.

## Consequences

The operative consumers are the review CLI (`run edit`, `run edit --fixture`, `show`), the revise workflow, `commonplace-validate` for edit-operation instances, and the worker, which receives the operation, the execution instruction and the result contract as inputs. Python enforces the outcome rules, the bounds, the struck-entry check and retention; the type specs and the execution instruction bind worker content.

Every pass candidate in revise now carries a typed result and a retained observation, and the run directory grows by those copies. The strike-list entries changed form, so an operator now strikes entries that show `quote`, `change` and `reason`. The new link and quoted-span bounds may refuse sound edits; the first live runs will show whether they do.

Limits: no edit operation has run live on this route. Whether the wrapped fix-strategy operation gives results that can be told apart by strategy is untested. The `depth` values were set for revise's order and are not shown to be a general order of concerns. Code does not detect a change outside an answered list. This decision does not arrange operations into procedures, define stops or replace the full pass's edits.
