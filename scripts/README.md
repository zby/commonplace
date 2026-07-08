# scripts/

Ad hoc tooling expected to be reused — committed, but without a `commonplace-*` entry point. The middle tier between a throwaway `python3` heredoc and the installed `commonplace` package. See [ADR-040](../kb/reference/adr/040-scripts-directory-is-the-accumulation-substrate-for-ad-hoc-tooling.md) for the decision and [ADR-014](../kb/reference/adr/014-scripts-as-python-package-one-tree-model.md) for the precedent of a script cluster growing into the package.

## Cleanup norm

If a script's docstring says "one-off" or "temporary," whoever finishes using it deletes it in the same session or commit series. Don't leave it for someone else to notice later.

## Promotion signal

A script graduates to a `commonplace-*` command when it has been invoked, unmodified in its core logic, across multiple unrelated sessions or triage passes — repetition with a stable interface. A script whose interface is still changing hasn't stabilized enough to promote yet, no matter how many times it's been touched. This is a judgment call exercised periodically (e.g., at monthly triage), not a mechanical trigger.
