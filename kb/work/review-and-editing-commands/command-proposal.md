# Command proposal: two commands split by authority over the note

Proposed by an agent (claude-fable-5-2) on 2026-11-19, in answer to the [workshop framing](./README.md). The operator adopted it on 2026-11-19 as the starting design. Nothing here is implemented.

## The rule

Split the commands by one question: may this invocation write the note?

- `commonplace-review` never writes a note. It writes review results and run records only.
- `commonplace-revise` is the only command that writes a note.
- Within `commonplace-revise`, an invocation that starts with a note path may write that note. Of the invocations that start with a verb, only `apply` and `publish` write a note.

An operator who knows only the first two lines predicts safely. `commonplace-review` cannot change a note under any flag. The third line refines the prediction for `commonplace-revise`; guessing wrong there means expecting an edit that does not happen.

Both commands take the main operation with the note first and follow-up actions with a verb first. A first argument that is a registered verb is read as the verb. A file named like a verb is written with a path prefix, such as `./status`.

## Proposed commands

### Main operations

| Proposed | Today | Writes |
|---|---|---|
| `commonplace-revise NOTE` | none; a bare `run revise NOTE` is a command error | whatever the default procedure writes; at the start, the full pass |
| `commonplace-revise NOTE --full` | `commonplace-review run revise NOTE --full` | findings, then the note, or a held candidate |
| `commonplace-revise NOTE --quick` | `run revise NOTE --assess` | the note, or a held candidate |
| `commonplace-revise NOTE --pass NAME` | `run revise NOTE --pass NAME` | the note, or a held candidate |
| `commonplace-revise NOTE --finding RESULT` | `run revise NOTE --finding RESULT` | the note, or a held candidate |
| `commonplace-revise NOTE --plan FILE` | `run revise NOTE --plan FILE` | the note, or a held candidate |
| `commonplace-review NOTES... [--criteria C...]` | `commonplace-review run gates NOTES... (--criteria C... \| --all-gates)` | findings |

The bare `commonplace-revise NOTE` runs the default procedure, which is the full pass at the start. `--full` stays and always means the full pass. A caller that needs the full pass, such as an instruction or a saved command, names `--full`; the bare form is for an operator who wants the current default. `--assess` becomes `--quick`, the name the operating guide already gives that procedure.

The bare `commonplace-review NOTES...` reviews against every gate. `--all-gates` goes away. `status` already uses that default. `--criterion-file`, `--fixture`, `--grouping`, `--profile`, `--input`, `--force` and `--resume` keep their meaning.

### Follow-up actions under `commonplace-revise`

| Proposed | Today | Writes |
|---|---|---|
| `apply FILE [FILE ...]` | `run revise NOTE --answers FILE [--answers FILE ...]` | the note, and a copy of each answers file |
| `publish RUN [--revised FILE]` | `commonplace-review publish RUN [--revised FILE]` | the note |
| `triage NOTE` | `run revise NOTE --triage` | pending answers files |
| `answers create --from QUESTION [--to PATH]` | the same | a pending answers file |
| `answers create --run RUN` | `record RUN` | pending answers files |
| `answers record FILE` | the same | a decision record |
| `decisions [--note PATH] [--class NAME] [--json]` | `commonplace-review decisions` | nothing |
| `rewrite NOTE --commission FILE` | `run rewrite NOTE --commission FILE` | a held candidate |
| `try OPERATION NOTE` | `run edit OPERATION NOTE` | a candidate kept in the run |

### Follow-up actions under `commonplace-review`

`status`, `show`, `fixture create`, `retry` and `acknowledge` keep their names and contracts. `publish`, `record`, `answers` and `decisions` leave this command.

## The follow-up verbs

The framing names three actions that two uses of `record` blur today. The proposal gives each one verb:

| Action | Verb | Effect |
|---|---|---|
| prepare pending answers | `answers create` | writes a file for the operator to decide; launches nothing |
| save decisions that nothing will consume | `answers record` | keeps the decided file in the run; launches nothing |
| give effect to approved items | `apply` | starts a run that edits the note |

`record RUN` becomes a second source for `answers create`. Both write pending answers files over a question; they differ only in where the question comes from. After that change `record` has one meaning.

`apply` drops the NOTE argument. Each answers file names its question, and the question, an edit result or a review result, names its note. `answers_plan()` in `revise.py` already checks today's NOTE argument against that field, so the argument carries no information. Files that name different notes are refused. Naming the file stays the operator's approval, as [ADR 138](../../reference/adr/138-a-stop-ends-the-run-and-naming-its-output-is-the-approval.md) decided.

`triage` is a verb because it never writes the note. As a flag on the note-first form it would be the one flag that removes edit authority.

## Worked example: a full pass through a stop

The operator runs `commonplace-revise kb/theory/foo.md`.

1. The run reviews the note against every review operation that declares a depth, and the type and collection reviews. Fresh results are reused. New results go to the shared store.
2. An assessor reads the findings and writes a plan. Assume four passes; the last is `plain-wording`, a per-item pass.
3. The run applies the first three passes and publishes their text to the note. `git diff` shows the change.
4. `plain-wording` proposes changes. The run stops.

The report states, in this order:

- **Done:** the reviews run and reused; the three passes applied; the note written, with the path of the diff.
- **Decision left:** approve, reject or defer each proposal in `<run>/artifact/plain-wording-answers.md`.
- **Command:** `commonplace-revise apply <run>/artifact/plain-wording-answers.md`.

The operator decides the items. On the operator's word for that file, the agent runs the `apply` command. It applies the approved items and publishes. If the operator approves nothing, `commonplace-revise answers record FILE` keeps the rejections and the note stays as it is.

The other stops name their commands the same way:

| Stop | Decision left | Command |
|---|---|---|
| per-item proposals | decide each proposal | `apply FILE` |
| triage findings | decide each finding | `apply FILE FILE ...` |
| held candidate, after a new validation warning or a rewrite | accept the exact candidate, or supply a revised text | `publish RUN [--revised FILE]` |
| plan stop on a depth 1 proposal | decide the proposal; nothing consumes the answer | `answers record FILE`, then a new run with `--plan FILE` if work follows |
| plan entry not run | none | `commonplace-revise NOTE --plan <run>/artifact/continue/<id>.yaml` |

## Migration

**Callers.** 68 tracked files outside `kb/reports/` and `kb/work/` name `commonplace-review`. Change them in the commit that changes the parser. No old form stays accepted: no consumer needs one, and an accepted old form would keep two names per operation.

**No findings-only invocation gains edit authority.** `commonplace-review` loses every path that writes a note, so an old invocation typed into the new command cannot edit. Every verb that leaves `commonplace-review` stays a refused word there: `run`, `publish`, `record`, `answers` and `decisions`. Its error prints the proposed form of the old invocation, such as `commonplace-revise publish RUN` for `commonplace-review publish RUN`. This is a hint, not an accepted alias.

**Saved continuation records.** Continuation records and `held.json` files under `kb/reports/state/` embed old commands. Do not rewrite them: `made-for` is already never updated, and the files are records of what the run reported. The saved commands begin with `commonplace-review run revise`, `commonplace-review publish` or `commonplace-review answers record`. Each fails with the hint above, so the operator can finish an earlier run without reconstructing the command. Mark the hints `# BACKCOMPAT` and remove it when `decisions` lists no pending item from a run made before the change.

**Decisions.** The change reverses one part of [ADR 135](../../reference/adr/135-improvement-procedures-are-three-plans-on-one-runner.md)'s command contract: a bare invocation runs the default procedure instead of ending in an error. It needs a new ADR. The runner, the plans, the run directories and the publication rules do not change.

## Decided and left open

- **Bare `commonplace-revise NOTE` defaults to the full pass.** The operator accepted this on 2026-11-19 as a start. It is the costliest invocation: it launches every review and may write the note. The operator expects the full pass to grow and the default to become a faster procedure later. Every procedure, the full pass included, keeps its own flag, so changing the default changes one line of the parser and breaks no caller that named its procedure.
- **`try` and `rewrite` sit under `commonplace-revise`** though neither writes the note. Adopted with the rest.
- **Coordination, open.** The [review workflow workshop](../review-on-workjig/README.md) is still listed as active. Agree the parser change with it before implementation.
