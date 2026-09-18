# scripts/

Ad hoc tooling expected to be reused — committed, but without a `commonplace-*` entry point. The middle tier between a throwaway `python3` heredoc and the installed `commonplace` package. See [ADR-040](../kb/reference/adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md) for the decision and [ADR-014](../kb/reference/adr/014-scripts-as-python-package-one-tree-model.md) for the precedent of a script cluster growing into the package.

## Cleanup norm

If a script's docstring says "one-off" or "temporary," whoever finishes using it deletes it in the same session or commit series. Don't leave it for someone else to notice later.

## Promotion signal

A script graduates to a `commonplace-*` command when it has been invoked, unmodified in its core logic, across multiple unrelated sessions or triage passes — repetition with a stable interface. A script whose interface is still changing hasn't stabilized enough to promote yet, no matter how many times it's been touched. This is a judgment call exercised periodically (e.g., at monthly triage), not a mechanical trigger.

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
