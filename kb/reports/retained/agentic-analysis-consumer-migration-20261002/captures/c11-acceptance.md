# C11 acceptance: quote resolution in main-review publication

Accepted on 2026-09-05 for the migration and retirement described below.

## Disposition

Quote resolution is now a deterministic check on the files produced by the
main review. During prospective publication, the run-state verifier reads the
exact result and every generated candidate using their intended public paths.
It finds blockquotes whose final line is a `> ---` attribution and requires the
normalized quote text to occur in the frozen source.

For a Git source, the attribution is either a full-commit GitHub blob URL for
the registered repository or `` `commit-relative/path` @ `full-commit` ``. The
verifier reads that blob with `git --no-replace-objects ... cat-file blob`; it
does not read the worktree or infer evidence from current HEAD. For an
immutable capture, it reads the SHA-256-identified capture as UTF-8 and checks
the quote against those bytes. A repository, revision, path, encoding, or quote
mismatch fails the bundle before publication writes.

The removed `verify-review-quote-grounding` instruction instead read a live
checkout and treated a mismatched citation revision as a warning. It had no
automated caller, freshness baseline, or projected skill. Its function is now
covered at the boundary that holds the frozen source and all candidate bytes,
so the instruction was deleted and its public path redirects to
`analyse-agentic-system`.

## Scope separation

This check establishes only that quoted text occurs in the recorded source.
Standing note validation still checks quote-anchor shape because the external
source is not retained with the library artifact. Semantic verification and
the grounding-alignment gates separately decide whether the quotation supports
the surrounding claim. Neither success is represented as the other.

The generated Apache Maka and oh-my-pi main outputs inspected during selection
contain no quote-anchored blocks, so no production result needed rewriting.
The unmarked Semantic Engine review and legacy review corpus include historical
examples. C11 did not rewrite or retroactively attest them.

## Verification

Focused tests exercised:

- exact-result and compact-review quote blocks;
- local-path and GitHub-blob attributions;
- successful resolution from the recorded commit after the worktree changed;
- rejection of text found only in the changed worktree;
- rejection of a local attribution with the wrong revision;
- successful resolution against an immutable capture; and
- rejection of an unresolved generated candidate by publication `prepare`
  before any public destination is written.

The focused module passed 74 tests. The full suite passed all 730 tests, and
Ruff passed for the repository. The changed instruction and type collections,
legacy review type, ADR, workshop files, and redirect map validated cleanly.
`git diff --check` also passed.

## Remaining migration

C11 is complete without a secondary review or legacy projection. The
trace-learning survey, C05, cannot yet be refreshed from sound current inputs:
the recent producer audit requires regenerated Maka and oh-my-pi learning
findings, and Pond still lacks the retained-result publication contract. That
evidence work is the return condition for C05. C12/C14 remain coupled to the
retirement of mandatory legacy candidate generation after active consumers are
resolved.
