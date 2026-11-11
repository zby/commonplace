"""Open, publish and close the drafting handoff of one ingest.

The drafting worker writes a candidate in an ignored working directory under
kb/reports/state/ingest/; the ingest in kb/sources/ is not touched until the
candidate is accepted.

``prepare`` guards the target and writes the handoff record. ``publish`` checks
the candidate again and, when it is clean, copies it to the ingest path.
``close`` ends the run without publishing. Check a candidate with
``commonplace-validate <candidate> --handoff <record>``.

The working directory stays after the run: its record lists every handoff check
and how the run ended. ``prune`` deletes the directories of published runs.

Run from the repository root. Exits 0 on success and 1 when a guard refuses or
the candidate has failures.
"""

from __future__ import annotations

import argparse
import sys
from collections.abc import Sequence
from pathlib import Path

from commonplace.lib.ingest_handoff import (
    HandoffError,
    close_handoff,
    load_record,
    prepare_handoff,
    print_handoff_result,
    prune_published,
    publish_handoff,
)
from commonplace.lib.ingest_handoff import (
    shown_path as _shown,
)
from commonplace.lib.library import checks_library


def _prepare(args: argparse.Namespace, repo_root: Path) -> int:
    record = prepare_handoff(
        args.ingest,
        repo_root=repo_root,
        occasion=args.occasion,
        code_grounded=args.code_grounded,
        created_snapshot=args.created_snapshot,
    )
    print(f"handoff_record: {_shown(record.path, repo_root)}")
    print(f"candidate_path: {_shown(record.candidate, repo_root)}")
    print(f"retained_quotes_path: {_shown(record.retained_quotes_path, repo_root)}")
    print(f"output_path: {_shown(record.ingest, repo_root)}")
    print(f"snapshot_sha256: {record.snapshot_sha256}")
    print(f"incumbent: {'none (new output)' if record.incumbent_sha256 is None else 'exists; it stays unchanged until publish'}")
    return 0


def _publish(args: argparse.Namespace, repo_root: Path) -> int:
    record = load_record(args.record, repo_root=repo_root)
    result = publish_handoff(record, repo_root=repo_root)
    if result.failures:
        print_handoff_result(record, result, repo_root=repo_root)
        print("Not published; the ingest path is unchanged.")
        return 1
    print(f"Published: {_shown(record.ingest, repo_root)}")
    for warning in result.warnings:
        print(f"warning: {warning}")
    return 0


def _close(args: argparse.Namespace, repo_root: Path) -> int:
    record = load_record(args.record, repo_root=repo_root)
    close_handoff(record)
    print(f"Handoff closed without publishing; {_shown(record.ingest, repo_root)} is unchanged.")
    return 0


def _prune(args: argparse.Namespace, repo_root: Path) -> int:
    removed = prune_published(repo_root=repo_root, older_than_days=args.days)
    for directory in removed:
        print(f"removed: {_shown(directory, repo_root)}")
    print(f"{len(removed)} published run(s) removed.")
    return 0


@checks_library
def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    commands = parser.add_subparsers(dest="command", required=True)

    prepare = commands.add_parser("prepare", help="guard the target and open its working directory")
    prepare.add_argument("ingest", type=Path, help="the .ingest.md output path")
    prepare.add_argument("--occasion", metavar="TEXT", help="the supplied occasion, verbatim")
    prepare.add_argument("--code-grounded", action="store_true", help="the run has code-grounding context")
    prepare.add_argument("--created-snapshot", action="store_true", help="this run captured the snapshot")
    prepare.set_defaults(run=_prepare)

    publish = commands.add_parser("publish", help="publish a clean candidate and end the run")
    publish.add_argument("record", type=Path, help="the handoff record")
    publish.set_defaults(run=_publish)

    close = commands.add_parser("close", help="end the run without publishing")
    close.add_argument("record", type=Path, help="the handoff record")
    close.set_defaults(run=_close)

    prune = commands.add_parser("prune", help="delete the working directories of published runs")
    prune.add_argument(
        "--days", type=int, default=30, metavar="N",
        help="delete runs published at least N days ago (default 30; 0 deletes all published runs)",
    )
    prune.set_defaults(run=_prune)

    args = parser.parse_args(argv)
    try:
        return args.run(args, Path.cwd().resolve())
    except HandoffError as error:
        print(f"commonplace-ingest-handoff: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
