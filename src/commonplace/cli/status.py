"""Show a compact read-only Commonplace project situation report."""

from __future__ import annotations

import argparse
import json
from dataclasses import asdict
from pathlib import Path

from commonplace.lib.library import checks_library
from commonplace.lib.project_status import ProjectStatus, load_project_status


def format_status(status: ProjectStatus) -> str:
    git = status.git
    git_summary = (
        f"{git.head} ({git.changed_paths} changed paths)"
        if git.available
        else f"unavailable ({git.error})"
    )
    lines = [
        f"COMMONPLACE STATUS {status.status.upper()}",
        f"Root: {status.repo_root}",
        (
            f"Versions: project {status.project_version or 'unknown'}; "
            f"command {status.command_version or 'unknown'}"
        ),
        f"Git: {git_summary}",
        (
            f"Notes validation ({status.notes_validation.scope}): "
            f"{status.notes_validation.status}; "
            f"{status.notes_validation.failures} failures, "
            f"{status.notes_validation.warnings} warnings across "
            f"{status.notes_validation.subjects} subjects"
        ),
        (
            "Lifecycle: "
            f"{status.lifecycle.status}; {status.lifecycle.failures} failures, "
            f"{status.lifecycle.warnings} warnings across "
            f"{status.lifecycle.subjects} subjects"
        ),
    ]
    review = status.review
    if review is not None:
        review_summary = (
            (
                f"{review.results} results: {review.fresh} fresh, {review.stale} stale, "
                f"{review.orphaned} orphaned; current {review.warn} warn, {review.fail} fail"
            )
            if review.error is None
            else f"unreadable ({review.error})"
        )
        lines.append(f"Review: {review_summary}")
    if status.actions:
        lines.extend(("", "NEXT ACTIONS:"))
        lines.extend(
            f"- {item.action_id} | {item.reason} | {item.command}"
            for item in status.actions
        )
    else:
        lines.extend(("", "Next actions: none from the bounded status inputs"))
    return "\n".join(lines)


def format_status_json(status: ProjectStatus) -> str:
    payload = asdict(status)
    payload["schema"] = "commonplace.status.v2"
    payload["status"] = status.status
    return json.dumps(payload, indent=2, sort_keys=True)


@checks_library
def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument("--json", action="store_true", help="Print structured status.")
    parser.add_argument(
        "--collection", required=True,
        help="Collection name or path to validate; other status components keep their own scope.",
    )
    # TODO: reconsider review-by-default after the review system is stable and
    # regularly used as an operational surface rather than accumulated state.
    parser.add_argument(
        "--review",
        action="store_true",
        help="Include counts over the stored review results.",
    )
    args = parser.parse_args(argv)

    try:
        status = load_project_status(
            repo_root=cwd if cwd is not None else Path.cwd(),
            collection=args.collection,
            include_review=args.review,
        )
    except (FileNotFoundError, ValueError) as exc:
        parser.error(str(exc))
    print(format_status_json(status) if args.json else format_status(status))
    return 1 if status.status == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
