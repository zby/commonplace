"""Two producers, one checked combination, and a bounded correction.

Run again with the same records after --stop-after-producers to resume using
delivered producer results. The working directory needs left-source.txt and
right-source.txt; no Git repository or Commonplace installation is needed.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from treadle_headless import CommandWorker, Request, Run

WORKER = Path(__file__).with_name("ordinary_worker.py")


def worker(operation: str, log_file: Path, delay: float = 0.0) -> CommandWorker:
    return CommandWorker(
        argv=(
            sys.executable,
            str(WORKER),
            "{prompt}",
            "{input_dir}",
            "{output_dir}",
            "{problem_file}",
            operation,
            "--delay",
            str(delay),
        ),
        env={"ORDINARY_WORKER_LOG": str(log_file)},
    )


def delivered(result: object, label: str) -> None:
    if result.status != "delivered":
        raise RuntimeError(f"{label}: {result.status}")


def workflow(
    record_dir: Path,
    workdir: Path,
    *,
    left_delay: float = 0.0,
    right_delay: float = 0.0,
    max_corrections: int = 1,
    stop_after_producers: bool = False,
) -> dict[str, object]:
    if max_corrections < 0:
        raise ValueError("max_corrections must be nonnegative")
    left_source = (workdir / "left-source.txt").read_text(encoding="utf-8")
    right_source = (workdir / "right-source.txt").read_text(encoding="utf-8")
    log_file = workdir / "invocations.log"

    with Run(record_dir, workdir) as run:
        requests = (
            Request(
                call_id="left",
                task="Produce the left ordinary file from source.txt.",
                inputs={"source.txt": left_source},
                required_outputs=("left.txt",),
                worker=worker("left", log_file, left_delay),
            ),
            Request(
                call_id="right",
                task="Produce the right ordinary file from source.txt.",
                inputs={"source.txt": right_source},
                required_outputs=("right.txt",),
                worker=worker("right", log_file, right_delay),
            ),
        )
        left, right = run.parallel(requests, max_workers=2)
        delivered(left, "left producer")
        delivered(right, "right producer")
        producer_reused = {"left": left.reused, "right": right.reused}
        if stop_after_producers:
            return {"status": "stopped", "producer_reused": producer_reused}

        # Freeze both siblings before interpreting any combined candidate.
        snapshot = {"left.txt": left.outputs["left.txt"], "right.txt": right.outputs["right.txt"]}
        expected = snapshot["left.txt"] + snapshot["right.txt"]
        candidate = ""
        feedback = ""
        for correction in range(max_corrections + 1):
            inputs = dict(snapshot)
            if correction:
                inputs.update({"candidate.txt": candidate, "feedback.txt": feedback})
            result = run.call(
                Request(
                    call_id=f"combine:{correction}",
                    task=(
                        "Combine both ordinary files and answer the caller's feedback "
                        "if supplied."
                    ),
                    inputs=inputs,
                    required_outputs=("combined.txt",),
                    worker=worker("combine" if correction == 0 else "correct", log_file),
                )
            )
            delivered(result, f"combine round {correction}")
            candidate = result.outputs["combined.txt"]
            if candidate == expected:
                return {
                    "status": "accepted",
                    "candidate": candidate,
                    "corrections_used": correction,
                    "producer_reused": producer_reused,
                    "combine_reused": result.reused,
                }
            feedback = "combined.txt does not match the frozen left and right contents"
        return {
            "status": "rejected",
            "candidate": candidate,
            "corrections_used": max_corrections,
            "producer_reused": producer_reused,
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record_dir", type=Path)
    parser.add_argument("workdir", type=Path)
    parser.add_argument("--left-delay", type=float, default=0.0)
    parser.add_argument("--right-delay", type=float, default=0.0)
    parser.add_argument("--max-corrections", type=int, default=1)
    parser.add_argument("--stop-after-producers", action="store_true")
    args = parser.parse_args()
    print(
        json.dumps(
            workflow(
                args.record_dir,
                args.workdir,
                left_delay=args.left_delay,
                right_delay=args.right_delay,
                max_corrections=args.max_corrections,
                stop_after_producers=args.stop_after_producers,
            ),
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
