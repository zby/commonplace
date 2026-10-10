# Focused synthesis-verifier calibration protocol

## Intent and evaluation boundary

Measure whether each registered worker profile rejects unsupported synthesis
claims without rejecting supported controls. The result feeds decisions about
verifier instructions and further calibration, not publication acceptance.

Use four faulty/control pairs: source support, quotation entailment, inventory
coverage, and carriage of a limit's prevented conclusion. All evidence is
synthetic and supplied in the packet. The eight excerpts are not complete
analysis-set members. The prompt states this deviation and excludes structural
complaints from the task. The production synthesis mission and three supporting
contracts are copied unchanged from one Git commit. This is a focused assay,
not an execution of the full production hand-out or complete contract closure.

Before an evidential run, an independent reviewer must check the answer key
against these packets and the pinned materiality contract. Freeze any revisions
before launching; changing the key after seeing responses creates a new
exploratory analysis, not a correction to the predeclared score. The reviewer
must not later serve as a blind verifier for these same cases.

## Profile matrix

Use the profiles from the committed `worker-profiles.yaml`, not invented model
names or substituted settings. At workshop creation the matrix is:

| Profile | Harness | Launch model | Effort |
|---|---|---|---|
| opus | claude-code | opus | medium |
| sonnet | claude-code | sonnet | medium |
| haiku | claude-code | haiku | medium |
| codex-sol | codex | gpt-6.1-sol | medium |
| codex-luna | codex | gpt-6-luna | medium |
| pi-sol | pi | gpt-6.1-sol | medium |
| pi-luna | pi | gpt-6-luna | medium |
| pi-luna-low | pi | gpt-6-luna | low |

This table is descriptive, not a second launch authority. The helper resolves
and pins the actual file from the selected method commit. Compare profiles
separately; harness differences can affect outcomes on the same launch model.
Record a resolved model version when exposed, or explicitly `unknown`. Aliases
alone do not establish immutable model identity. An unavailable profile stays
unrun with the exact failure; do not replace it with another harness or model.

The operator selected `pi-luna-low` for the initial pilot: one trial per case,
eight calls. Keep `pi-luna` as the medium-effort comparison, not a substitute.
A full eight-profile matrix would require 64 calls; do not launch it without a
separate decision. This is not a failure-rate estimate. Repeats and model
comparisons need a separately fixed sampling protocol after feasibility.

## Preparation

Select one coherent committed method revision for all profiles. Do not snapshot
uncommitted implementation files. The helper pins its own bytes, the protocol,
fixtures, answer key, profile file and each copied method file by SHA-256. It
refuses to reuse an existing run directory.

From the repository root:

```bash
uv run python scripts/analysis_workflow_calibration.py prepare \
  --revision <commit> --profile pi-luna-low \
  --output /tmp/analysis-calibration-pi-luna-low-01
uv run python scripts/analysis_workflow_calibration.py verify \
  /tmp/analysis-calibration-pi-luna-low-01
```

The output directory must be outside the checkout. `private/` contains the
answer key and experiment provenance. Each `packets/cNN/` directory contains
only that case's prompt, evidence and method files. Do not hand the whole run
directory to a verifier. Case IDs omit faulty/control labels, but adjacent IDs
and the authored simplicity mean the set is not adversarially blinded against
a model that guesses the experiment design.

## Launch and isolation

Launch is a separate authorized operation, not something the helper performs.
Each case needs a fresh context with no parent conversation, no prior case,
no repository discovery or automatic repository instructions. Expose only its
packet directory to the worker and permit writing only `response.md`. The
answer key, siblings, repository and outer run directory must be inaccessible.
Network and extra tools are unnecessary and should be disabled. A prompt that
says not to read those files is not an enforced filesystem boundary.

For Pi delegation, the repository's coordinator diagnostic remains required
before any worker run. Tool availability alone does not establish the packet-only
filesystem boundary. If the selected launcher cannot enforce isolation or exact
profile settings, stop that profile and record the exact limitation. Do not
launch an agent CLI as a substitute for unavailable delegation authority.

Dispatch the same prompt and case bytes to every profile. Shuffle launch order
and record it in the retained execution record. Keep raw outputs and actual
launch evidence, including harness, launch model, effort, resolved model or
`unknown`, isolation mechanism, failures, elapsed time and token/cost figures
when exposed. Report missing cost data as unknown. Never retry a failed call
silently; a retry is a separately identified trial.

## Authorized exploratory relaxation

For the first `pi-luna-low` pilot, the operator authorized relaxing filesystem
isolation on 2026-10-10. Use fresh Pi worker conversations with explicit packet-only
read instructions and output-only write scope, but do not claim an enforced
sandbox. Repository instructions may load. This run is exploratory; the stronger
isolation requirement still governs an evidential calibration.

The new profile is not yet committed. For this pilot only, `--profiles-file` may
name the current worker-profile file; retain its exact bytes and digest alongside
the committed method snapshot and report the different provenance explicitly.
Do not include concurrent uncommitted method edits. The helper supports this
explicit override; it never silently falls back to working-tree profiles.

## Annotation and scoring

An annotator reads raw responses and the answer key after execution. The helper
does not infer semantic validity from keywords or from the presence of a list.
Use a JSON object keyed by all eight case IDs. Completed entries look like:

```json
{
  "c01": {
    "status": "completed",
    "blocker": true,
    "reason": "The response identifies the unsupported invocation claim in RT-01.",
    "launch": {
      "harness": "pi",
      "launch-model": "gpt-6-luna",
      "effort": "low",
      "resolved-model": "unknown",
      "isolation-evidence": "Describe the enforced boundary and retained launch log."
    }
  }
}
```

`blocker: true` on a faulty case means the response raises the targeted semantic
defect as a material blocker, with the defective claim and evidence identified.
An unrelated blocker, a generic complaint, or a limit that permits the faulty
claim does not count as detection. On a supported control it means the response
raises an unwarranted semantic blocker. Discuss unrelated defects separately;
do not silently score them as the targeted defect. Disagreement about whether
a response counts is `unscorable` until independently adjudicated.

Every case has a status and reason. A launch/tool failure is `failed`, not a
semantic miss. A `problem`, malformed verdict, or undecidable annotation is
`unscorable`; retain the raw response and explain why. Completed cases require
nonempty raw response files and matching launch-profile fields. Those equality
checks validate recorded metadata, not whether the actual launcher honored it.

```bash
uv run python scripts/analysis_workflow_calibration.py score \
  /tmp/analysis-calibration-pi-luna-low-01 \
  --annotations /tmp/pi-luna-low-annotations.json > /tmp/pi-luna-low-score.json
```

Report detected defects out of four faulty cases, false blockers out of four
controls, and counts of failed/unscorable calls separately. Do not exclude
failures and present the remainder as an unconditional success rate. Include
pair-level outcomes, annotation rationale and response hashes. Preserve raw
responses; hashes without bytes do not support later review.

## Interpretation and return to decision

A miss warrants inspection of the contract, assembled input and response, not
an automatic prompt addition. Repeated failure alone cannot distinguish a
specification gap from interpreter noncompliance. A false blocker may indicate
an overly strict materiality interpretation. Perfect scores here show only
success on eight simple authored cases, not full workflow reliability or
independent source inspection.

After feasibility, return to the operator with runnable/unavailable profiles,
per-case judgments, costs and isolation limitations. Decide then whether to
expand cases, repeat trials, change missions, or build tool-mocked worker assays.
Do not edit production instructions or handlers as part of scoring this pilot.
