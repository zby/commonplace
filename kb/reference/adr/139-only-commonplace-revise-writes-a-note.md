---
description: "commonplace-review never writes a note and commonplace-revise is the only review command that does; a bare commonplace-revise NOTE runs the default procedure, and apply, triage and answers create --run replace --answers, --triage and record"
type: reference/types/adr.md
status: accepted
---

# 139 — Only commonplace-revise writes a note

**Status:** accepted; the operator adopted the design on 2026-11-19 and it was implemented the same day.
**Date:** 2026-11-19
**Amends:** [ADR 135](./135-improvement-procedures-are-three-plans-on-one-runner.md), whose rule that a run names its procedure this replaces: a bare run takes the default procedure. It renames the commands that [ADR 127](./127-review-runs-as-workflows-over-result-files.md), [ADR 130](./130-the-operator-decision-record-is-a-query-over-the-state-tree.md) and ADRs 132 to [138](./138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md) name; their decisions stand. The table below translates their command names.

## Context

One command, `commonplace-review`, ran every workflow of the review and editing system. Three forces act on its interface.

An operator must be able to predict from an invocation whether it may change a note. Under one command the answer depended on a subcommand and its flags: `run gates` only wrote findings, `run revise --triage` only wrote answers files, and `run revise --full` reviewed and then wrote the note. A first-time operator could not tell these apart by name.

The full editorial pass is the main operation for improving a note. It needed the longest invocation, and a bare `run revise NOTE` was a command error.

Three actions shared one word. `record RUN` prepared pending answers files, `answers record FILE` kept decided ones, and `run revise NOTE --answers FILE` gave effect to them.

## Decision

**The commands split by authority over the note.** `commonplace-review` never writes a note. It writes review results and run records. `commonplace-revise` is the only command that writes a note. Of its invocations, the note-first form, `apply` and `publish` may write the note; `triage`, `answers`, `decisions`, `rewrite` and `try` never do.

**Each command takes its main operation note-first and its follow-up actions verb-first.** `commonplace-review NOTES...` reviews; `commonplace-revise NOTE` revises. A first argument that is a registered verb is read as the verb, so a file named like a verb is given with a path prefix.

**A bare invocation runs the default.** `commonplace-revise NOTE` runs the default procedure, which is the full one. `--full` stays and always means the full procedure, so a caller that needs it names it and survives a change of the default. `commonplace-review NOTES...` without `--criteria` covers every bundle plus `type` and `collection`, the default `status` already had.

**Each follow-up action has one verb.** `answers create` prepares pending answers, from a question (`--from`) or from a revise run's findings (`--run`). `answers record` keeps decided answers that nothing consumes. `apply` gives effect to approved items. `apply` takes no note: each answers file names its question, the question names its note, and files that name different notes are refused. Naming the file is still the operator's approval, as ADR 138 decided.

**The system is named the review and editing system.**

| Before | Now |
|---|---|
| `commonplace-review run gates NOTES (--criteria C \| --all-gates)` | `commonplace-review NOTES [--criteria C]` |
| `commonplace-review run revise NOTE --full` | `commonplace-revise NOTE [--full]` |
| `run revise NOTE --assess` | `commonplace-revise NOTE --quick` |
| `run revise NOTE --pass`, `--finding`, `--plan` | `commonplace-revise NOTE` with the same flag |
| `run revise NOTE --answers FILE ...` | `commonplace-revise apply FILE ...` |
| `run revise NOTE --triage` | `commonplace-revise triage NOTE` |
| `record RUN` | `commonplace-revise answers create --run RUN` |
| `commonplace-review publish`, `answers`, `decisions` | the same verb under `commonplace-revise` |
| `run rewrite NOTE --commission FILE` | `commonplace-revise rewrite NOTE --commission FILE` |
| `run edit OPERATION NOTE` | `commonplace-revise try OPERATION NOTE` |

`status`, `show`, `fixture create`, `retry` and `acknowledge` stay under `commonplace-review` unchanged. The report's mode `assess` is now `quick`.

## Considered alternatives

**Keep one command and rename only the flags.** Rejected. The prediction the operator needs would still depend on a subcommand and its flags. With two commands, the first word answers it.

**Require a procedure choice on every run.** This was ADR 135's rule: a run never chooses work implicitly. The operator chose a default instead, so that the main operation is the shortest invocation. The default is the costliest procedure: it launches every review and may write the note. The operator expects the default to become a faster procedure once the full one has grown.

**Keep `triage` as a flag of the note-first form.** Rejected. It would be the one flag that removes authority to write the note.

**Put `try` under `commonplace-review`, since it never writes the note.** Not adopted. An edit operation would then run under the review command. A wrong prediction about a `commonplace-revise` action errs on the safe side: the operator expects an edit that does not happen.

**Accept the old invocations, or refuse them with a hint naming the new form.** Rejected by the operator: no compatibility for now.

## Consequences

An old invocation typed into `commonplace-review` cannot edit a note, because that command has no path that writes one. It fails: `run` and the moved verbs are read as note paths that do not exist.

Continuation records and `held.json` files written before this decision name the old commands. They are not rewritten, and the commands they give no longer run. An operator finishing such a run translates the command with the table above.

`apply` trusts the question's `note` field to name the note. `answers_plan()` checked the old NOTE argument against that same field, so no check was lost.

Operativity: the parsers in `src/commonplace/cli/review_workflows.py` enforce the split in Python, and the library builds every continuation and held-candidate command in the new form. Session agents reach the commands through the [review and editing system guide](../README-REVIEW-SYSTEM.md), the [command reference](../commands.md) and the instructions those link, with the force of instructions.

Limits: the rule that only `commonplace-revise` writes a note covers the review and editing commands. Relocation, conversion and other commands that write notes are outside it. No test asserts that `commonplace-review` cannot reach the publication code; the split holds by the dispatch in one module.
