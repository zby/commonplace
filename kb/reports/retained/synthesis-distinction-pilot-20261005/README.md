# Synthesis distinction pilot: execution and result

The [eight-call feasibility check](./protocol/README.md)
ran on 2026-10-05 with one frozen Dynamic Cheatsheet case. The combined
instruction treatment did **not** meet the predeclared promising-signal rule:
its writer omitted the targeted retrieval-synthesis distinction, and its
reviewer accepted the known overclaim in a fixed draft. The control did the
same. In a second fixed draft, the treatment reviewer accepted a supported
qualification while the control reviewer falsely blocked it. These are one
response per condition and case, not estimates of reliability or causal
effects. No production instruction was changed.

[Scores and source adjudication](./scores.md) give the individual judgments,
coverage losses, other objections and costs. The exact packets, prompts,
outputs, traces, settings and usage records are retained under
[`attempts/v2/`](./attempts/v2/). Each job's `result.json` includes output
SHA-256 and confirms that packet inputs were unchanged. The 37-file frozen
bundle and treatment text are pinned by the experiment plan; version 2 used
the same evidence, model and treatment for both arms.

## Execution history

The first launch of the version 1 control writer failed at provider routing
inside the outer workspace network sandbox, before inference. Its [raw
record](./attempts/control-writer-network-failure/) is retained as an
infrastructure failure. A retry produced a draft in 182.7 seconds but
exceeded the predeclared 1,000,000-token accounting ceiling: 1,283,864
reported tokens, including 1,191,936 cached input tokens. The [version 1
record](./attempts/control-writer-v1/) is cost calibration only; that draft
was not semantically scored. Its trace contains 23 completed command
executions and repeated reads after truncated output.

Version 2 sent the same required documents inline in each initial prompt and
kept source files accessible for targeted checks. This common delivery change
started a new version. All eight scheduled jobs completed with no timeout or
budget overrun, in 332.32 seconds of aggregate model runtime and 1,950,094
reported input-plus-output tokens. That total counts cached input; it is
neither a context-window size nor a billable-token estimate. All required
output sections and blocker syntax passed the coordinator's mechanical check.
The large difference between version 1 and version 2 control-writer usage is
an operational observation, not a controlled cost-effect estimate.

The pilot is a development case built around a known failure. It tested a
combined writer and reviewer treatment, with no isolated component arms,
correction rounds, repetitions or held-out cases. The original and qualified
fixed drafts test local target claims, not the entire document as a gold
standard. The result supports a decision to refrain from adopting this
combined treatment on this evidence; it does not establish that the wording
never helps or that the control method is reliable.
