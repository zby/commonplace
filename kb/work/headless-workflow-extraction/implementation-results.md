# Independent implementation results

Implemented 2026-10-19 after the operator authorized Sol workers with parent
review. The standalone package is staged at [package/](./package/README.md),
named `treadle-headless` version `0.1.0`, import `treadle_headless`.
It has no runtime dependencies and targets Linux with Python 3.11 or newer.
No code or tests were imported from the headless branch. Treadle and the
Commonplace runtime were not modified.

## Delivered

- Immutable requests and returned results, named text inputs and outputs,
  caller-supplied working directories, and a generic subprocess worker.
- Fresh paths for every physical launch, including retries; explicit delivery
  outcomes and raw execution evidence.
- Exclusive run ownership, atomically committed result records, request and
  content checksums, workdir binding, persistent launch allowances, and explicit
  acknowledgment of uncertain launches before resumption.
- Bounded parallel groups with ordinary Python control flow. No scheduler or
  generic correction protocol was added. The example owns its content check,
  fixed comparison snapshot and bounded correction loop.
- Codex, Claude Code and Pi command factories and a standalone JSONL evidence
  parser. Codex and Pi passed real Sol file-copy/reuse probes; Claude is
  command-tested and parser-tested only.
- A distributable wheel and source archive, with source-archive documentation
  and examples included.

## Review and corrections

One Sol worker implemented the core; another independently built the ordinary
file example and acceptance tests; a third researched and implemented the
adapters, then reviewed the core without write authority. The parent reviewed
the source, directed fixes, added two regression tests, ran real adapter probes,
and verified the built distribution independently.

Review found and fixed:

- Literal braces in generic command arguments being interpreted as template
  syntax, and recursive substitution when a real path contained token text.
- Mutable mappings inside nominally immutable results.
- Saved results with missing, invented or modified output contents being
  accepted on reload.
- A failed result commit leaving reusable, uncommitted controller state.
- Process-start record failures bypassing cleanup, and cleanup failures after
  process start being misclassified as settled launch failures.

The final cleanup-error regression uses a real sleeping subprocess, injects a
cleanup error, verifies that its reservation remains unresolved, and explicitly
cleans up the test worker. Other interruption cases cover a controller killed
while its worker runs, a prelaunch reservation, and exit after result commit.

## Validation

Commands run from the package directory unless stated otherwise:

| Check | Result |
|---|---|
| `uv run pytest -q` | 55 passed |
| `uv run ruff check .` | Passed |
| `uv build --quiet` | Wheel and source archive built |
| Wheel source comparison | All packaged Python modules exactly matched current source bytes |
| Source archive contents | Includes `examples/ordinary_files.py` and `docs/design.md` |
| Installed-wheel test suite | 55 passed outside the repository, using copied tests and examples |
| Installed import check | Imported from temporary environment's `site-packages`; Commonplace was absent |
| `commonplace-validate kb/work/headless-workflow-extraction` | Passed before this result record; revalidated after recording it |
| `git diff --check` | Passed |

The fresh installation used Python 3.13.1 in
`/tmp/treadle-headless-installed-tqktvy03/.venv`. The test command there was
`uv run --no-project --python /tmp/treadle-headless-installed-tqktvy03/.venv/bin/python python -m pytest -q tests`.
There was no package source directory in that test location and no Git
repository. The isolated test files include their own deterministic subprocess
workers; they do not need model credentials.

Wheel: `package/dist/treadle_headless-0.1.0-py3-none-any.whl`.
SHA-256: `3d6c1bfd76f311a3d1f2f77b5f1f6227110ce351eef23cc3f51d5cb68ace0feb`.

Source archive: `package/dist/treadle_headless-0.1.0.tar.gz`.
SHA-256: `ba840b8a9033491e73dfd5809aaa740972340171de49dad06088f23e3f02a8a2`.

Build artifacts are ignored local outputs, reproducible with the package's
build command; their hashes identify this tested build, not all future builds.

The [harness evidence](./package/docs/harness-evidence.md#real-probes-2026-10-19)
records versions, commands, raw local record locations and limitations of the
real Codex/Pi probes. Both requested `gpt-6.1-sol`, delivered the exact input
copy in one launch and reused that launch on the repeated call. Requested
model identity is not substituted for independently observed served identity.

## Remaining limits and handoff

The package does not isolate access, pin code, control ambient dependencies,
make external effects transactional, or automatically recover orphan workers.
Its parallel limit applies per group. Provider quota errors are not universally
classified; structured problem-file usage limits are recognized and not
automatically retried. The adapter stream parser preserves evidence separately
from the generic runtime's result protocol.

The implementation and independent acceptance phases are complete within
these support claims. Public naming, final repository placement and external
publication remain undecided. Commonplace integration remains a separately
commissioned consumer project, not an implicit follow-up in the headless branch.
The workshop stays active while those ownership and adoption decisions remain.
Nothing has been committed or published by this implementation session.
