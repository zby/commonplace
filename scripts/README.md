# scripts/

Ad hoc tooling expected to be reused — committed, but without a `commonplace-*` entry point. The middle tier between a throwaway `python3` heredoc and the installed `commonplace` package. See [ADR-040](../kb/reference/adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md) for the decision and [ADR-014](../kb/reference/adr/014-scripts-as-python-package-one-tree-model.md) for the precedent of a script cluster growing into the package.

## Cleanup norm

If a script's docstring says "one-off" or "temporary," whoever finishes using it deletes it in the same session or commit series. Don't leave it for someone else to notice later.

## Promotion signal

A script graduates to a `commonplace-*` command when it has been invoked, unmodified in its core logic, across multiple unrelated sessions or triage passes — repetition with a stable interface. A script whose interface is still changing hasn't stabilized enough to promote yet, no matter how many times it's been touched. This is a judgment call exercised periodically (e.g., at monthly triage), not a mechanical trigger.

## Isolated installation rehearsal

Start with [the orchestrator instruction](../kb/instructions/test-installed-commonplace.md)
and [the installed-wiki scenarios](../tests/scenarios/installed/README.md).
By default, give the installation agent a disposable source copy, including
selected working-tree changes and INSTALL.md, and point it to that file. The agent builds and
installs from that source, runs init, and completes setup. The supervisor does
not prebuild or preinstall. Select a PyPI release explicitly to test a
published version; development rehearsals require no publication.
The Codex helper supports installation inside its outer sandbox, including
skill-stub creation, and restores the inner Codex sandbox for later stages.
The orchestrator selects stages, prepares prompts and inputs, assigns budgets,
inspects evidence, judges outcomes, and decides whether to continue. It looks
for a CLI counterpart of its own agent runtime and reports a blocker if none
is available with the required isolation. Capture project inventories per
stage, archive the project at the start and end, and check the read-only
installation once at the end. Detailed context accounting is optional.

Two mechanical helpers support it:

- `run_isolated_codex.py`: optional implementation for Codex CLI on Linux;
  enforce a Bubblewrap boundary, launch one supplied prompt with explicit
  access and timeout settings, and retain raw process/session logs. Network
  access is shared with the host. Use only when Codex is the selected runtime.
- `capture_test_state.py`: archive bytes, hash files, and compare inventories
  for any runtime. Differences are data for the orchestrator to assess.

Each helper has `--help`. Neither helper assigns scenario verdicts or advances
the test sequence.

## Synthesis distinction pilot

For the frozen synthesis/review wording pilot, see
[synthesis distinction experiment](../kb/reports/retained/synthesis-distinction-pilot-20261005/protocol/README.md).
`python3 scripts/synthesis_distinction_trial.py verify` verifies the copied
evidence; `packet --help` describes isolated worker-packet preparation.
The helper launches no models and does not alter a live analysis run.
`python3 scripts/run_synthesis_distinction_job.py --help` describes the
isolated single-packet launcher and its predeclared limits; see the
[execution preflight](../kb/reports/retained/synthesis-distinction-pilot-20261005/protocol/execution-preflight.md).

## Agentic analysis rerun statistics

`python3 scripts/agentic_system_rerun_stats.py` is a fast, stdlib-only,
report-only snapshot of `kb/agentic-system-analyses/retained/`. It reads only
named Markdown report members, plus `report-check.md` if an Artifact check
report has been exported under that name. It does not run validation or read
source snapshots, traces, logs, runtime stores, manifests, Git or the workshop
inventory. There is no inventory denominator; no reports is not success.

```bash
# Default: all currently retained sets, including older run dates.
python3 scripts/agentic_system_rerun_stats.py
# Restrict to this rerun cohort by report run-id date, not file mtime.
python3 scripts/agentic_system_rerun_stats.py --since 2026-10-12 --json
# Supplied roots replace the default; repeat --root to include both.
python3 scripts/agentic_system_rerun_stats.py \
  --root kb/agentic-system-analyses/retained \
  --root /path/to/inflight-run/artifact --run-id AAS-2026-10-12-example-token-01
```

A root is a report directory or its immediate parent. Discovery does not
recurse into run stores or historical attempt directories. Supply in-flight
`artifact/` directories explicitly. Archives are not included by default.
Each directory is one report set; overlapping roots are deduplicated, but
separate copies of the same run stay separate and display their run IDs.
`--run-id` is repeatable. `--since` excludes unidentified sets; excluded counts
are shown. Without filters, older retained runs remain visible, not evidence
that the current workshop rerun has finished.

Recorded failures are verification **Blockers** entries or exported Artifact
check findings, never prose mentions of failure. Verification **Limits** are
warnings, not failures. Blocked dispositions, incomplete sets, accepted sets
with limits, clean accepted sets and out-of-scope stops are separate statuses.
Missing/malformed fields or findings, inconsistent identities, missing members,
and absent recorded passing checks prevent clean acceptance. Failure status
has priority; JSON also exposes overlapping blocked/incomplete/limit counts
and the findings behind them. Clean acceptance means the reports record a
complete overview, all named members with passing snapshot-check rows, and
blocker-free, limit-free verifications. This does not independently establish
publication, runner success, or semantic correctness. In-flight attempts that
never produced reports cannot be detected. Exit status is 2 for root scan
errors, otherwise 0 even when report findings exist. See `--help` for options.

## X likes reading inbox

Run from this checkout:

```bash
uv run python scripts/sync_x_likes.py
```

The default account is `zby`; use `--handle NAME` for another account authorized
by the token. Credentials come from the checkout's `.env`: `X_ACCESS_TOKEN`,
`X_REFRESH_TOKEN`, and `X_CLIENT_ID`. An expired access token is refreshed once
and rotated tokens are saved atomically to `.env`. Native apps use public-client
refresh authentication; web/bot apps require `--confidential-client` and
`X_CLIENT_SECRET`. Tokens and API response bodies are never printed.

The first run reads one page of up to 100 likes. Later runs start at the newest
likes and paginate until a previously seen post or the end of the list. Posts
before that overlap are new to this inbox. The default catch-up cap is ten
pages; use `--max-pages N` to increase it. Reaching the cap without overlap fails
without publishing history or changing cached files. Network errors and partial
API responses also leave the previous cache and history intact. No schedule is
installed; run the command whenever the reading inbox needs refreshing.

Each post becomes `kb/reports/cache/x-likes/<handle>/<post-id>.md`, with author,
source URL, available full post text, expanded links, article title when supplied,
publication time, and first-observed time. Article bodies, threads, and linked
pages are not fetched; use the source ingestion workflow for selected items.
Cache files expire 21 days after first observation, during successful syncs.
A seven-day reading selection means first observed within seven days.

`kb/reports/state/x-likes/<handle>/sync.json` retains seen IDs and first-observed
times, plus the payloads for the active three-week inbox. Those active payloads
allow deleted cache files to be regenerated without API refetches. Expired
payloads are removed, but seen IDs and dates remain to prevent reimporting old
likes. Preserve this state while using the inbox; deleting it deliberately
restarts the 100-like bootstrap. It is local operational state, not disposable
cache. A shared Linux file lock prevents concurrent syncs and token refreshes.
If publishing cache files is interrupted, rerun: committed state rebuilds them.

Limits: X does not supply the time a post was liked, so first observation is
not a historical like timestamp. The initial page is not necessarily one week's
likes. Incremental overlap assumes stable newest-like-first ordering; reordered
likes, unlike/re-like events, or likes removed between runs can be missed. This
is a reading inbox, not an exact mirror or event archive: an unlike does not
remove an already cached post before its retention expires. An API end-of-list
without overlap cannot prove that all intervening likes were available. See the
[X likes endpoint](https://docs.x.com/x-api/users/get-liked-posts) and
[OAuth refresh documentation](https://docs.x.com/fundamentals/authentication/oauth-2-0/authorization-code).
