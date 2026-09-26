# Volunteer compute tasks

Turn donated agent compute into useful improvements whose evidence costs much
less to check than to discover. The operator commissioned this workshop on
2026-09-26, requested three choices, later added a fourth, and specified an ordinary repository
checkout with software installed in `.venv`.

The operator's selection criterion is substantial work with cheap verification.
A quotation audit was rejected because judging each alleged mismatch could
cost the maintainer as much as discovering it cost the contributor. These tasks
instead return executable counterexamples or measured improvements. None
guarantees that more compute will find a result.

All tasks must be grounded in committed repository content and runnable
from a fresh checkout. The operator excluded review-state work because the
operational review history is not committed. Do not substitute synthetic review
history for that unavailable evidence.

## Choose one

| Task | Main work | What the maintainer checks |
|---|---|---|
| [Relocation stress search](./relocation-stress-search.md) | Generate and shrink combinations of KB graphs and move sequences | A small graph, a command sequence, and a broken preservation property |
| [Validator defect-detection search](./validator-defect-detection-search.md) | Mutate committed artifacts and generate combinations of explicit structural violations | A small before/after fixture and a required diagnostic the validator misses |
| [Faster collection validation](./faster-collection-validation.md) | Profile, optimize, and compare the validator across corpus shapes | Identical diagnostics, repeatable timings, and a bounded patch |
| [Link recognition differential](./link-recognition-differential.md) | Compare each component's link recognition with the site renderer, then propose one shared recognizer | A small Markdown fixture with disagreeing results; a function checked against the same cases |

Each task can absorb sustained search and experimentation. Choose by interest;
doing more than one is not expected. Search strategy, tools, and allocation of the
contributor's available compute are left to the contributor. The third task
offers a numeric success measure but also requires code review before merging.
The fourth task's second stage likewise ends in a patch that needs code review.

## Shared contributor handoff

Read this page and the chosen task together. Read root `AGENTS.md` for repository
conventions. This commission explicitly replaces its user-level `uv tool`
installation and `uv run` test instructions for this contribution: use the
activated `.venv` and `python -m pytest`. Do not change `AGENTS.md` to make that
exception global. Do not run `commonplace-init` in this checkout.

Use Python 3.11 or newer and Git. In a fresh POSIX shell:

```bash
git clone https://github.com/zby/commonplace.git
cd commonplace
git checkout -b volunteer-compute 8eb5c3a6aea83bcd6c2908b446709b482d5d45a6
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[docs]' pytest ruff
python -c "import sys, commonplace; print(sys.executable); print(commonplace.__file__)"
commonplace-validate --help
```

On Windows, use `py -3 -m venv .venv` and activate with
`.venv\Scripts\Activate.ps1`; the remaining commands are the same. The `docs`
extra supplies dependencies used by the wider test suite. Record Python,
platform, `git rev-parse HEAD`, and `python -m pip freeze` with the result.
Additional search dependencies are permitted inside `.venv`; list them and
their versions. Final reproductions should need only the installed package
and pytest where practical.

The commit above is the common baseline, not a moving branch. Keep these task
instructions separately available: the baseline predates the workshop. If it
cannot be fetched or installed, report that blocker rather than silently
switching revisions. No API credentials, live review service, private snapshots,
or maintainer database are needed.

Run the chosen task's existing tests before searching. Report baseline failures
separately from discoveries. Create all experimental KBs in
temporary directories. Invoke relocation commands from the temporary project
root; they use the working directory to select the project.

## Ownership and result format

Work in your own branch. Add reproducible tests under `tests/commonplace/` and
reusable search or benchmark tooling under `scripts/volunteer_compute/`. Keep
the submission summary under this workshop in a contributor-named subdirectory.
Do not edit the real KB corpus as experimental input. Tasks 1 and 2 initially
own tests, tooling, and reports only; fixes, if supplied, must be separate
patches. Task 3 additionally permits a bounded validator implementation patch.
Task 4 permits a new link-recognition function and one caller adoption, as
separate patches.
The maintainer owns acceptance, integration, and any changes to the contracts.

For a bug finding, supply the baseline SHA, practical consequence, exact
contract passage or existing contract test, minimal fixture, one reproduction
command, expected result, and actual result. The regression assertion should
fail on the baseline for the claimed reason. Include enough before/after state
to inspect the failure without reading the search tool. A small positive
control should distinguish the failure from broken setup.

Deliver at most five distinct defects, ranked by consequence and deduplicated
by cause. Put ambiguous requirements in a separate short list. A test that
merely asserts a contributor's preferred behavior is not a confirmed bug.
Record seeds and search bounds for reproducibility, but do not make rerunning
the entire search a prerequisite for checking a finding. Aim for each final
counterexample to replay in under a minute on an ordinary laptop.

Start with one complete result packet. It should be reviewable on its own;
continue independent search within the chosen scope while awaiting feedback.
Stop at the contributor's stated budget or deadline, after five distinct
findings, or when progress requires a contract decision. Return partial results
and blockers. A search with no counterexample reports its tested domain and
cost, not a claim that the implementation is correct. Report approximate time
and model/token usage if available; private conversation logs are unnecessary.

For a proposed implementation fix, the existing full suite must pass with
`python -m pytest`, together with the relevant new regression tests. A
reproduction-only submission is expected to contain a failing new test; keep
that distinct from the passing baseline suite.

## Maintainer evaluation and closure

Record replay outcome, acceptance decision, and approximate checking time for
each submitted result. A cheap replay does not remove the need to inspect the
contract or review a patch. If adjudication requires reconstructing the search
or reading a long report, narrow the packet before commissioning more work.

The [relocation refactor workshop](../relocation-move-map-engine/README.md) owns
architectural consolidation; this workshop commissions evidence about existing
behavior. Validator defect findings and performance patches remain separate:
the performance comparison preserves baseline output, including known defects;
a correctness fix changes that output under its own regression test.
The [graph-loader workshop](../kb-graph-loader/README.md) explores a broader
architecture; performance work here does not authorize that redesign. It also
owns where a shared positioned link representation lives; task 4 supplies
evidence and a candidate recognizer for that decision.

Close after the contributed results have been accepted, rejected, or deferred
with reasons, useful tests and tooling have been integrated, and any lesson
about verification cost has been retained in the appropriate library artifact.
Remove this workshop and its active-list entry when that work is complete.
