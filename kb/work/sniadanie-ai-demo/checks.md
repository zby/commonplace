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

The semantic check has **not** been run. Its intended title–body mismatch is prepared, but no model verdict, latency, or detection reliability has been established. A complete timed rehearsal is still required before delivery.
