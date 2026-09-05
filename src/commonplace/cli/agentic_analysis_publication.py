"""Prepare or publish one agentic-analysis projection bundle."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from commonplace.lib.agentic_publication import (
    PublicationSpec,
    PublicationUncertainError,
    prepare_publication,
    publish_publication,
)


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="operation", required=True)
    for operation in ("prepare", "publish"):
        command = subparsers.add_parser(operation)
        command.add_argument("run_state", help="Path to the running run-state.md")
        command.add_argument("--generated-candidate", required=True)
        command.add_argument("--generated-destination", required=True)
        command.add_argument("--legacy-candidate")
        command.add_argument("--legacy-destination")
        command.add_argument("--legacy-model-partition")
    return parser


def _spec(args: argparse.Namespace, *, repo_root: Path) -> PublicationSpec:
    return PublicationSpec(
        repo_root=repo_root,
        run_state_path=Path(args.run_state),
        generated_candidate_path=Path(args.generated_candidate),
        generated_destination=args.generated_destination,
        legacy_candidate_path=(
            Path(args.legacy_candidate) if args.legacy_candidate else None
        ),
        legacy_destination=args.legacy_destination,
        legacy_model_partition=args.legacy_model_partition,
    )


def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = _parser()
    args = parser.parse_args(argv)
    repo_root = (cwd or Path.cwd()).resolve()
    try:
        spec = _spec(args, repo_root=repo_root)
        if args.operation == "prepare":
            prepared = prepare_publication(spec)
            batch = prepared.review_batch
            payload: dict[str, object] = {
                "prepared": True,
                "semantic_review_required": batch is not None,
            }
            if batch is not None:
                payload.update(
                    {
                        "review_job_id": batch.review_job_id,
                        "prompt_path": batch.prompt_path,
                        "job_output_path": batch.job_output_path,
                    }
                )
        else:
            published = publish_publication(spec)
            payload = {
                "published": True,
                "generated_path": published.generated_path,
                "retained_path": published.retained_path,
                "legacy_path": published.legacy_path,
                "cleanup_warnings": list(published.cleanup_warnings),
            }
    except PublicationUncertainError as exc:
        print(
            f"public state is uncertain; mark this run failed and use a new run ID: {exc}",
            file=sys.stderr,
        )
        return 2
    except (OSError, RuntimeError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    print(json.dumps(payload, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
