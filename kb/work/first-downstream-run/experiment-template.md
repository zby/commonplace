# Experiment template: operator work on one KB-building task

A template for a small experiment that anyone using Commonplace can run.

**The question.** Does a revised release of the framework let an agent
build an accepted knowledge base with less help from a person than an
earlier release, on the same task, at comparable cost?

**Why this one.** Early use showed that the framework is complex and asks
the operator to learn a great deal. Current work moves decisions from the
operator to the agent. This experiment measures that on one real task. It
needs no production traffic and no long observation period.

Copy this template, fill in Part 1 before any run, then run the experiment
and fill in Parts 2 and 3.

## Part 1. Declaration (fill in before the first run)

| Field | Your entry |
|---|---|
| Project, by its general kind | |
| Task: what the agent must produce, from which inputs | |
| Who chose the task, and when | |
| Release A: the earlier framework version (commit) | |
| Release B: the revised framework version (commit) | |
| Agent tool, model version, and settings (same for A and B) | |
| Operating system (same for A and B) | |
| Who plays the operator, and the subject-matter brief they answer from | |
| What counts as an intervention, if different from the default below | |
| Acceptance criteria for the finished knowledge base | |
| Who judges, and whether they know which release produced each result | |
| Runs per release | |
| Ceilings per run on time and tokens | |
| Date of this declaration | |

Three choices keep the comparison fair:

- **Choose the task after release B is fixed**, and do not use a task whose
  failure led to the fixes in B. Otherwise B was built for the test.
- **Keep everything except the release the same** in both conditions.
- **Run each release several times.** The same agent on the same task
  varies from run to run, and one run per release cannot separate the
  release's effect from that variation.

**The operator script (default).** The operator hands over the task. They
answer questions about the task's subject matter from the brief. To every
question about the framework they reply "use your judgment". If a run
cannot continue without more than that, they record a stop, give the least
help that lets it continue, and note what they gave.

**Interventions (default).** Count separately: framework questions the
agent asked, and stops.

## Part 2. Record of each run

| Run | Release | Framework questions | Stops | Accepted? | Criterion failed, if rejected | Validator failures at end | Time | Tokens |
|---|---|---|---|---|---|---|---|---|
| | | | | | | | | |

Count these by rule from the run's records. For each stop, note in a line
what the agent could not decide without a person. If the agent tool records
which framework instructions the agent read before its main decisions, keep
that list too.

## Part 3. Result

| Release | Runs | Accepted | Framework questions (median, range) | Stops (median, range) | Time (median) | Tokens (median) |
|---|---|---|---|---|---|---|
| A | | | | | | |
| B | | | | | | |

**What a result supports.** Fewer interventions under B with no loss of
acceptance supports the claim for this task, model, and operating system.
It does not show which fix made the difference; that takes a run with one
fix removed. It does not show that the finished knowledge base helps the
people or agents who later use it, which is a separate experiment.

**Next steps.** If B is no better, the list of stops is the most useful
output, because it says what the agent still could not decide alone. A
second task of a different kind is the natural next step either way.

## Publishing

Publish whatever your organization allows. The tables above contain no
subject matter, so they are usually the easiest part to release. Task
inputs, knowledge-base contents, transcripts, and the judge's reasons can
stay private.

If you want to publish an account of each run without its records, one
option is an automatic summary.

To use this option, run the prompt below, inside your organization, on
each run's records, with one model version and the same settings
throughout. Fixing the prompt and model before the runs means
every run is described by the same procedure. If you use it, state the
model version and this file's commit.

```text
You are writing a summary of one recorded run for publication. The records
are confidential. Report only what the records show; where they do not show
something, write "not recorded". Do not include names of people,
organizations, products, systems, customers, or projects, and do not
include file paths, URLs, identifiers, figures, or quotations from the
task's subject matter. Describe the subject matter only by its general
kind. You may name framework commands, skills, and files, since the
framework is public. Use plain declarative sentences and do not evaluate
the framework.

Write these sections, each in at most five sentences:
1. Task kind: what the agent was asked to produce, in general terms.
2. Course of the run: the main steps the agent took, in order.
3. Operator exchange: each question the agent put to the operator, stated
   generally, marked as about the subject matter or about the framework.
4. Stops: each point where the run could not continue without a person,
   and what was missing.
5. Framework material consulted before the main decisions.
6. Outcome: the judge's decision and the general kind of each reason.
7. Anything in the records that contradicts another part of the records.
```
