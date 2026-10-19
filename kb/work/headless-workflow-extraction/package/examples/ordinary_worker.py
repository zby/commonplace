"""Deterministic subprocess used by the ordinary-file workflow example.

The command receives the same launch paths a real headless adapter receives.
Its deliberately wrong first combine result demonstrates that delivery and
caller acceptance are separate decisions.
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("prompt", type=Path)
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("problem_file", type=Path)
    parser.add_argument("operation", choices=("left", "right", "combine", "correct"))
    parser.add_argument("--delay", type=float, default=0.0)
    args = parser.parse_args()

    # Read the actual rendered prompt even though this deterministic worker
    # receives its operation as an explicit command argument.
    if not args.prompt.read_text(encoding="utf-8").strip():
        raise ValueError("empty task prompt")
    time.sleep(args.delay)

    if args.operation in ("left", "right"):
        source = (args.input_dir / "source.txt").read_text(encoding="utf-8").strip()
        content = f"{args.operation.upper()}:{source}\n"
        output_name = f"{args.operation}.txt"
    else:
        left = (args.input_dir / "left.txt").read_text(encoding="utf-8")
        right = (args.input_dir / "right.txt").read_text(encoding="utf-8")
        if args.operation == "combine":
            content = left + "RIGHT:unchecked\n"
        else:
            previous = (args.input_dir / "candidate.txt").read_text(encoding="utf-8")
            feedback = (args.input_dir / "feedback.txt").read_text(encoding="utf-8")
            if "does not match" not in feedback or not previous:
                raise ValueError("correction request lacks candidate and findings")
            content = left + right
        output_name = "combined.txt"

    args.output_dir.mkdir(parents=True, exist_ok=True)
    (args.output_dir / output_name).write_text(content, encoding="utf-8")
    log_file = Path(os.environ["ORDINARY_WORKER_LOG"])
    line = (
        json.dumps(
            {
                "operation": args.operation,
                "prompt": str(args.prompt),
                "output": str(args.output_dir / output_name),
            }
        )
        + "\n"
    )
    fd = os.open(log_file, os.O_CREAT | os.O_APPEND | os.O_WRONLY, 0o600)
    try:
        os.write(fd, line.encode("utf-8"))
    finally:
        os.close(fd)


if __name__ == "__main__":
    main()
