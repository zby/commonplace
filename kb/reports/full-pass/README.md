# Full-pass reports

Output of `kb/instructions/run-full-improvement-pass-on-note.md`. Each invocation writes a pass-scoped directory:

```text
<note-name>/<pass-id>/
  initial/    # reports over the pre-edit note
  closing/    # one closing cycle over the final note
  full-pass-report.md
```

Reports here are **gitignored** inspection artifacts. Retain a pass directory while its packet or residual findings are still in use; delete it when those outputs have been consumed. Review freshness and acceptance live in the review store, not in these directories. Only this README is tracked.
