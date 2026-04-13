# kb/work/

`kb/work/` is the catch-all workshop layer: temporary work state, drafts, investigations, scratch notes, pasted traces, migration plans, and other material that exists to move active work forward.

It is not a clean register collection and does not require library-style metadata. Plain markdown without frontmatter is normal here. Imported, copied, or transitional files with incomplete or incompatible frontmatter are also normal. Do not "fix" workshop files just to make them look like notes; add structure only when it helps the work continue or makes later extraction easier.

Substantial work should usually live in a named subdirectory with a short `README.md`, `framing.md`, or `plan.md` that says what the work is and what would close it. Small one-off files can live directly under `kb/work/` until they disappear or grow into a workshop.

Linking from workshop files is permissive: use whatever relationship label makes the work state clear (`draws-on`, `tests`, `depends-on`, `produces`, `supersedes`, or a local phrase). Workshop links are working notes, not durable graph contracts.

If a conclusion should remain useful after the workshop closes, extract it into the right durable collection: `kb/notes/` for transferable claims, `kb/reference/` for shipped-system descriptions, `kb/instructions/` for reusable procedures, or an ADR for architectural decisions.
