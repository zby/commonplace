# Execution preflight for the synthesis distinction pilot

Prepared on 2026-10-05. No synthesis or review model trial has run. The
preflight checks below do not establish a treatment result.

## Fixed runtime and limits

| Setting | Value |
|---|---|
| Model | `gpt-6-luna` |
| Reasoning effort | `medium` |
| Harness | native Codex CLI 0.160.0, one new ephemeral session per job |
| Filesystem boundary | Bubblewrap exposes the packet at `/work`, makes `inputs/` and `prompt.txt` read-only, and hides the repository and other packets |
| Other context | no inherited session, user config, user rules, plugins, apps, memories or hooks |
| Network | available to Codex for model calls; the worker prompt forbids network use for task evidence |
| Time limit | 1,800 seconds per job, enforced by process termination |
| Token accounting ceiling | 1,000,000 reported input plus output tokens per job, identical for all jobs |
| Run order | the predeclared schedule in [README.md](./README.md) |

The packet is about 343 KB on disk, but only the short `prompt.txt` is sent
at launch. Workers read the required records and inspect relevant source files
through tools. Required instructions and records total about 176 KB; the
optional source tree is about 165 KB. Repeated tool outputs can make cumulative
input tokens much larger than a single reading, so the former 200,000-token
ceiling was too tight. The 1,000,000-token ceiling is an emergency accounting
limit, not an expected usage estimate or a context-window setting.

The launcher records each completed turn's reported token use. The CLI does
not expose a documented cumulative per-job token cutoff to this launcher, so
the ceiling is assessed after the job. An overrun is an incomplete trial and
its actual tokens are reported. The 272,000-token Codex context window is a
separate per-turn limit. The packet asks workers to read long records in
bounded ranges and inspect only source paths needed for a claim; this guidance
is identical in both arms. A time limit is enforced during the job. Keep
either limit fixed across arms and repetitions; changing one starts a new
experiment version.

The model appeared in the account's refreshed Codex catalog with `medium` as
its default effort and a 272,000-token Codex context window. Official
[OpenAI Docs](https://developers.openai.com/api/docs/models/gpt-6-luna)
confirms the model and medium effort. Saved ChatGPT authentication is
configured; `codex doctor` reached the active provider over HTTPS and the
Responses WebSocket outside the outer workspace sandbox. These checks do not
prove an inference will succeed. If the first scheduled call rejects the model,
record an infrastructure failure and stop before running the other arm.

## Packet and result handling

Prepare packets with `scripts/synthesis_distinction_trial.py` as described in
the [experiment plan](./README.md). Run one packet with:

```bash
python3 scripts/run_synthesis_distinction_job.py \
  --packet /tmp/synthesis-distinction/r1-control-write \
  --records /tmp/synthesis-distinction-evidence/r1-control-write
```

The launcher verifies the sibling packet manifest before the call, retains a
raw JSONL trace and stderr outside the worker directory, records the CLI
version and fixed settings, hashes outputs, and rechecks input hashes. Its
`--probe-only` option checks the filesystem boundary without a model call.
The coordinator still checks required sections, citations and blocker syntax
before preparing any dependent call; the launcher does not score content.

Keep temporary packet and evidence directories until scoring is complete.
Retain the final report, scores, manifests, prompts, outputs, raw traces and
launch/result records under
`kb/reports/retained/synthesis-distinction-pilot-20261005/`. This is the
durable report area under the [reports contract](../../reports/COLLECTION.md).
Copy exact files there before clearing temporary directories. The retained
report must name all incomplete calls and infrastructure retries. No result
directory or report has been created yet.

The launcher and its probe were checked without a model call. Its first live
invocation remains the first scheduled control writer in the plan.
