# Run-summary prompt for a confidential consuming project

> **Status:** Draft, 2026-09-19. It becomes the pinned prompt when a run's
> declaration records this file's commit hash. After that it is not edited
> for that run; a changed prompt is a new pin and is reported as one.

The [protocol](./commonplace-evidence-protocol.md#confidential-consuming-projects)
says what this prompt is for and what may be done to its output. The
summarizer runs inside the enterprise, on a model the enterprise permits to
read the records. The declaration names the exact model version and
settings, with sampling made as deterministic as the model allows.

## Input

One run's raw records: the task statement, the operator exchange, the agent
transcript, validator output, and the judge's decision and reasons.

## Prompt

```text
You are writing a summary of one recorded run for publication. The records
are confidential. The summary is the only text about this run that will be
published, and nobody will edit it except to remove confidential details.

Rules:
- Report only what the records show. If the records do not show something,
  write "not recorded". Do not infer motives or causes the records do not
  state.
- Do not include names of people, organizations, products, systems,
  customers, or projects, and do not include file paths, URLs, identifiers,
  figures, or quotations from the task's subject matter. Describe the
  subject matter only by its general kind, for example "internal process
  documentation".
- You may name framework commands, skills, and files, since the framework
  is public.
- Use plain declarative sentences. No evaluation of whether the framework
  is good or bad.

Write these sections, each in at most five sentences:

1. Task kind: what the agent was asked to produce, in general terms.
2. Course of the run: the main steps the agent took, in order.
3. Operator exchange: each question the agent put to the operator, stated
   generally, marked as about the subject matter or about the framework,
   with the operator's kind of answer.
4. Stopping points: each point where the run could not continue without a
   person, and what was missing.
5. Framework artifacts consulted: which framework instructions, skills, or
   commands the agent read or ran before its main decisions.
6. Outcome: the judge's decision and the general kind of each stated
   reason.
7. Anything in the records that contradicts another part of the records.
```

## Output handling

The enterprise reviews the output for confidential details before release.
The reviewer may only delete text, replacing it with `[redacted: kind]`. The
published record gives the number of redactions per summary.
