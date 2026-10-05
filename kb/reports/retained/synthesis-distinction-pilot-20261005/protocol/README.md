# Test whether synthesis preserves mechanism and assurance distinctions

Commissioned by the operator on 2026-10-05: create an experiment comparing
the existing synthesis and review instructions with two additions together:
preserve evidence distinctions while compressing, and search for qualifying
or contrary evidence during review. Preparation and the eight-call version 2
check completed on 2026-10-05. The combined treatment did not meet the
predeclared promising-signal rule. Exact attempts, [scores](../scores.md)
and costs are in the [retained execution record](../README.md).
This commission creates the experiment, not a production method change or a
new external-system analysis.

The immediate decision is whether the combined treatment is usable enough
to consider in ordinary work or a larger trial. This is now an eight-call
feasibility check, not a reliability estimate. Close the workshop after
reporting the observations and their limits, retaining useful evidence and
extracting any adopted instruction change separately. Do not infer which
addition caused an effect: there are no writer-only or reviewer-only arms.

## Frozen evidence

[frozen-input.json](./frozen-input.json) stores exact UTF-8 contents, original
locations and per-file SHA-256 hashes for 37 files. It is self-contained;
the original ignored worktree is not required to prepare a packet.
The prepared bundle's SHA-256 is
`7f5445a2e6ea2b01a080c10bdd907a51b170d3cdfeee21e54f28714cd8be7582`.

- Original run: `AAS-2026-10-04-dynamic-cheatsheet-01` in
  `.commonplace/worktrees/dynamic-cheatsheet-b0dc01a84b3c`.
- Method commit: `6f497a14e4cee76bac1a8571c23ebfec77784314`.
- Source commit: `5cfe3c37e8e52b1d858d0f3df46e7f17c50991b9`.
- Shared input: boundary, runtime, memory, epistemic and final reconciliation;
  original job instructions, collection, worker rules and three contracts.
- Available source: README, license, benchmark driver and tracked Python,
  text and Markdown under `dynamic_cheatsheet/`, `prompts/`, `text_generation/`,
  obtained from Git objects at the source commit. Data, embeddings, results,
  notebooks, figures and tracked binary files are not copied.
- Coordinator-only history: both original syntheses and reviews, their
  invocation packets, source identity and run metadata. The packet generator
  withholds history except a selected fixed diagnostic draft.

The historical audit is [second-run outcome check](../../../../work/analysis-collection-split/reliability/second-run-outcome-check-audit.md).
Its source interpretation needs a precision correction: the runtime route
record describes prompt-guided selection and useful-content preservation;
it does not itself quote the explicit accuracy instruction. That wording
is in the source prompt. Both conditions receive the same source access.
Score whether the worker uses records alone or inspects the source; do not
silently improve the records for the treatment.

This is an offline wording experiment. Both conditions use the same explicit
transport overrides: local packet paths, read-only copied evidence, output
in one directory, and no live acceptance command or workflow state. Source
access is narrower than the original run. These departures prevent a claim
that this exactly reproduces production workflow reliability. The original
job texts remain frozen, including the correction-round instruction.

## Conditions and schedule

The fixed harness, limits, access checks and result retention are recorded in
[execution preflight](./execution-preflight.md). The schedule below was run
once in version 2, with no correction rounds or added cases.

Version 1 supplied required documents as files. Its first control writer
needed 23 command turns and exceeded the cumulative token ceiling, so it is
retained as resource calibration and excluded from semantic scoring. Version 2
supplies the same required document bytes inline in `prompt.txt` to avoid
repeated file-read turns; source files remain available for targeted checks.
This common delivery change affects both arms. Version 2 restarts the full
eight-call schedule below with fresh sessions. Its model, treatment, evidence,
time limit and 1,000,000-token accounting ceiling are unchanged. If a version
2 job exceeds the ceiling, stop and report it as incomplete; do not silently
raise the ceiling again.

Control uses the frozen job instructions. Treatment inserts
[the writer paragraph](./treatment-synthesize.txt) and
[the reviewer paragraphs](./treatment-verify-synthesis.txt) immediately before
their acceptance-check instruction. There are no other arm-specific edits.
The two job instructions were unchanged between the frozen method and the
checkout used to prepare this experiment.

Use one pipeline per condition. Primary model and effort:
`gpt-6-luna`, medium, matching the historical run. Record the actual resolved
model, harness version, settings, dates, context limits, tools and budgets
before the first call; hold them fixed across conditions. If that model is
unavailable, stop before calls and obtain a revised model choice. A different
model is a separate experiment, not a historical replication.

Use clean sessions with no inherited conversation for every job. Provide only
the generated prompt and its directory.
Run outside this repository's ancestor instruction discovery, using the same
minimal harness instructions for every session. Do not give workers this
README, scoring guide, manifests, other outputs, or the original audit.
Restrict filesystem visibility to the assigned directory where supported;
otherwise retain tool traces and invalidate a trial that reads outside it.
The packet's scope instruction alone is not an isolation guarantee.

Run order, fixed before outputs are seen:

1. Control first-round writer, then treatment first-round writer.
2. Treatment reviewer of its writer's draft, then control reviewer of its
   writer's draft.
3. Fixed original draft: control reviewer, then treatment reviewer.
4. Fixed qualified draft: treatment reviewer, then control reviewer.

This is eight calls: two writers and six reviewers. There is no correction
round in this check. A blocker is an observed review result, not a trigger
for more calls. `bounded-absence` and `implicit-overclaim` remain prepared
but are outside this check. They and further repetitions require a new,
separately justified plan after scoring these results. Use the same per-job
token and time limits; budget exhaustion is an incomplete trial, never a
semantic pass. Do not continue sampling until the desired result appears.
Preserve failures and infrastructure retries separately.

## Prepare and execute the main comparison

The helper prepares packets; it launches no workers and judges no claims.
From this checkout:

```bash
python3 scripts/synthesis_distinction_trial.py verify
python3 scripts/synthesis_distinction_trial.py packet --delivery inline --arm control --job synthesize --out /tmp/synthesis-distinction-v2/r1-control-write
```

Launch a clean worker with that directory as its working directory and
`prompt.txt` as its complete task message. Retain its raw trace and response
outside the worker directory. The worker writes `output.md` or `problem.md`.
Prepare its independent reviewer after the writer completes:

```bash
python3 scripts/synthesis_distinction_trial.py packet --delivery inline --arm control --job verify-synthesis --synthesis /tmp/synthesis-distinction-v2/r1-control-write/output.md --out /tmp/synthesis-distinction-v2/r1-control-review
```

Follow the fixed order above for treatment and control. Do not pass a previous
synthesis to a first-round writer. Reviewers receive the candidate and shared
evidence, not the writer's scratch work or prompt. The packet generator can
prepare a correction round, but this pilot does not use that capability.

Before a dependent call, check the required sections, Description length,
member references and blocker syntax. Record format failures separately and
stop that pipeline if the result cannot be consumed. Do not supply unplanned
repair coaching or count this manual check as the production checker. A
`problem.md`, unreadable output or infrastructure failure is reported as such.
Do not mutate the original run, publish, stage or commit from trial workers.

Each packet has a sibling coordinator manifest with input/prompt hashes and
condition metadata. Copy these, traces and outputs to the chosen result
location before clearing temporary directories. Hash final outputs and check
input hashes again after each call. The chosen result location and retention
rule are in [execution preflight](./execution-preflight.md).

## Fixed-draft review diagnostic

Use frozen `synthesis-1.md`, which contains the target defect after the
earlier unrelated blocker was addressed. Generate the `original` and
`qualified` candidates by changing only the target sentence; the generator
retains the rest byte-for-byte. The original case is byte-identical. This
auxiliary comparison checks whether review catches the known overclaim and
avoids rejecting a supported qualification. It does not estimate the
combined pipeline effect.

```bash
python3 scripts/synthesis_distinction_trial.py packet --delivery inline --arm treatment --job verify-synthesis --case original --out /tmp/synthesis-distinction-v2/r1-treatment-case1
```

Repeat for `qualified` and both arms in the fixed order above. Use opaque
worker directory names for cases. Workers
see only `inputs/synthesis.md`, without case labels or expected judgments.
These are local sentence controls, not whole-document gold standards:
reviewers may legitimately identify other defects. The scoring guide keeps
target verdicts separate from other findings.

## Score and interpret

Use [the coordinator-only scoring guide](./scoring.md). Blind human scoring
to condition where practical; a model grader must run in a fresh context and
have its decisive evidence checked by the operator. Score before inspecting
the manifest's condition. Review tables may reveal the treatment, so report
that blinding is imperfect. Never let the synthesizer grade its own result.

Report each output and judgment, all incomplete trials, false objections,
coverage losses, non-target findings, time and tokens. One pipeline per arm
and one run of each fixed case can expose a mechanism or obvious failure;
they cannot estimate reliability or justify a broad adoption claim. A
favorable result may warrant provisional use in a reversible setting or a
separately justified larger trial. The prompts were designed around this
failure, so it is a development case, not held-out evidence.

Useful methodological precedents: [prompt variation](../../../../notes/prompt-ablation-converts-human-insight-to-deployable-framing.md)
and [claims limited to the contrast actually run](../../../../notes/an-experiment-identifies-only-the-contrast-it-actually-runs.md).

## Preparation verification

On 2026-10-05 the 37 frozen-file hashes passed verification. Packet smoke
checks confirmed that control and treatment differ only in the job instruction,
copied records and source bytes match the bundle, historical reviews stay out
of first-round packets, all four diagnostic replacements are exact, correction
inputs are wired correctly, manifests match, and invalid or duplicate packet
requests are refused. Ruff and relevant Commonplace Markdown validation passed.
These checks exercise preparation only; they provide no evidence that the
treatment improves synthesis or review.
