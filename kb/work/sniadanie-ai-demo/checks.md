# Demo checks

Checked on 2026-11-11, from the repository root, using `commonplace-validate`.

| Input | Exit | Observed result |
|---|---|---|
| Workshop README | 0 | Validation success; no failures or warnings |
| Corrected `demo.md` | 0 | Validation success; no failures or warnings |
| `01-missing-description.md.txt` copied onto `demo.md` | 1 | `validation.schema.frontmatter`: `'description' is a required property` |
| `02-overclaim.md.txt` copied onto `demo.md` | 0 | Validation success; no failures or warnings |
| Corrected `demo.md`, restored after fixture checks | 0 | Validation success; no failures or warnings |
| Workshop index `kb/work/README.md` | 0 | Validation success; no failures or warnings |

The fixture check restored the corrected note in a `finally` block. The faulty states remain text templates, not invalid Markdown artifacts in the collection.

## Bounded execution test: 2026-11-11

Tested the committed demo and templates from `828af3235`; their bytes were unchanged before execution. This was a fixture and single-review test, not a full talk rehearsal. No fixtures, criteria, or runtime configuration were changed.

Elapsed times below are wall-clock command durations measured with Python's monotonic clock, including command startup. Execution began at `2026-11-11T17:11:55.961215+00:00`.

| Input / operation | Exit | Elapsed | Actual result |
|---|---|---|---|
| Corrected `demo.md`, before testing | 0 | 0.210 s | Validation success; no failures or warnings |
| Missing-description template on `demo.md` | 1 | 0.188 s | `validation.schema.frontmatter`: `'description' is a required property` |
| Overclaim template on `demo.md` | 0 | 0.182 s | Validation success; no failures or warnings |
| Review status before launch | 0 | 0.207 s | Selected pair missing; no fresh result reused |
| One title–body alignment review on overclaim state | 0 | 13.043 s | One pair reviewed; semantic outcome `fail`; checkout guard clean |
| Review status immediately after launch, before restoration | 0 | 0.229 s | No stale or missing selected pair |
| Corrected `demo.md`, restored | 0 | 0.185 s | Validation success; no failures or warnings |

The semantic command was exactly:

```bash
commonplace-review run gates kb/work/sniadanie-ai-demo/demo.md --criteria frontmatter/title-body-alignment
```

It used the existing default `sonnet` profile: harness `claude-code`, launch model `sonnet`, effort `medium`. The recorded actual model was `claude-sonnet-5-5`. One launch delivered an accepted review; no retries or configuration changes were needed. Command exit 0 means successful review execution, not semantic approval.

### Actual semantic finding

The reviewer returned `## Result: FAIL`. It identified the universal H1, “Every added wiki note improves every answer,” as unsupported by a body about retaining knowledge separately from loading context. It cited the Scope section's explicit statement that the argument does not establish improved answer quality. It proposed titles about a larger wiki not requiring a larger context per task. This is the intended detection, observed once rather than a reliability estimate.

The central finding is useful and supported. Its wording that the body “denies” or “contradicts” the title is stronger than necessary: disclaiming proof is not itself proving a universal claim false. The unsupported title is sufficient for this gate's failure. No finding was edited or substituted.

### Result and run evidence

- Result: `kb/reports/state/review/results/kb/work/sniadanie-ai-demo/demo.md/frontmatter/title-body-alignment.md`
- Run: `kb/reports/state/review/runs/20261111T171156Z/`
- Captured input, accepted review, profile and launch timestamps: `calls/run.json` inside that run.
- Launch: `c8f2c8cbc01145acb9955709310bc9cf`; completed at `2026-11-11T17:12:09Z`.
- Local raw command output and timings: `/tmp/commonplace-sniadanie-test-owwqb0s_/` (`measurements.json` and labelled `.txt` outputs). These temporary files are not durable evidence.

The result and run files are generated local review state, ignored by Git. The result was fresh for the overclaim state immediately after review. Restoring the corrected H1 makes it stale; it must be presented as the captured review of the staged faulty state, not a verdict on the corrected note. No second semantic review was run.

### Exact restoration and scope

Before any replacement, the original bytes were backed up outside the checkout at `/tmp/commonplace-sniadanie-test-owwqb0s_/demo-original.md`. A `finally` block restored from that backup, with SIGTERM/SIGHUP interruption handlers; byte equality was asserted after restoration. Original and restored SHA-256:

```text
35adb2149973d5989cb366b71467e38219bf7783fcec8b2a09d682c57963353c
```

`demo.md` and both templates also match commit `828af3235`. The review guard reported `clean: true`, with no changed paths. Only this `checks.md` receives durable authored changes; existing unrelated dirty files were left alone. No commits, package installations, delegation, organizer submission, or pytest were performed.

### Remaining delivery risks

- One successful judgment does not guarantee another detection or the same latency. At 13.043 seconds this call fits the planned semantic segment, but network, service availability, and model latency remain live-call risks. Prefer opening this captured result without another call.
- Review outputs are local ignored state, not part of the committed workshop. Confirm they remain available on the presentation machine; the pair result can be overwritten by a later review.
- Full five-minute narration, file switching, projection readability, meetup language, and delivery remain untested. The README's pending semantic-test statement predates this record; it was not edited under this test's write scope.
- Broader connection discovery (`cp-skill-connect`) is a possible later authoring step, not part of this bounded execution test.
