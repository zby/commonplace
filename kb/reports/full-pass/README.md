# Full-pass reports

Output of `kb/instructions/run-full-improvement-pass-on-note.md`. Each invocation writes a pass-scoped directory:

```text
<note-name>/<pass-id>/
  source.txt # immutable UTF-8 start-state capture
  initial/    # reports over the pre-edit note
  closing/    # one closing cycle over the final note
  merge-target.txt # only for a merge disposition
  full-pass-report.md
```

Reports here are **gitignored** local artifacts. `full-pass-report.md` is typed by `kb/reports/types/full-pass-report.md` and is authoritative for a pass disposition and its later resolution. The `.txt` captures are immutable guard/diff inputs; the report and captures are one retention unit.

Retain every pending packet. Retain rejected or alternative resolutions while they constrain later work. An accepted packet may be deleted after Git history durably records the operation; captures and report are removed together. Review evidence and freshness remain in the review store, not in these directories. Only this README and the report type contract are tracked.
