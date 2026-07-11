# Full-pass reports

Output of `kb/instructions/run-full-improvement-pass-on-note.md`. Each invocation writes a pass-scoped directory:

```text
<note-name>/<pass-id>/
  initial/    # reports over the pre-edit note
  closing/    # one closing cycle over the final note
  controls/   # duplicate runs used to measure model variance
  full-pass-report.md
```

Reports here are **gitignored**, but a transformation-closure experiment may retain initial, closing, and control reports through workshop closure because its committed observation records refer to their exact bytes by path and SHA-256. After the workshop extracts its durable conclusions, these pass directories may be deleted. Only this README is tracked.
