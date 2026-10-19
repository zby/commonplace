"""One explicitly requested real model call, followed by a cache-reuse check."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from treadle_headless import Request, Run
from treadle_headless.adapters import codex_worker, parse_evidence, pi_worker


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("harness", choices=("codex", "pi"))
    parser.add_argument("workdir", type=Path)
    parser.add_argument("--model", required=True)
    args = parser.parse_args()
    workdir = args.workdir.resolve()
    workdir.mkdir(parents=True, exist_ok=True)
    if args.harness == "codex":
        worker = codex_worker(args.model, sandbox="workspace-write", effort="low")
    else:
        worker = pi_worker(
            args.model,
            provider="openai",
            tools=("read", "write"),
            project_trust="no-approve",
        )
    request = Request(
        call_id="copy-input",
        task=(
            "Read source.txt from the listed input path. Copy its contents exactly to "
            "answer.txt at the listed output path. Do not add commentary or formatting "
            "to the file. This is the entire task."
        ),
        inputs={"source.txt": "headless-probe-7391\n"},
        required_outputs=("answer.txt",),
        worker=worker,
        timeout_seconds=180,
    )
    with Run(workdir / "records", workdir) as run:
        result = run.call(request)
        if result.status != "delivered":
            print(json.dumps({"status": result.status, "records": str(workdir / "records")}))
            raise SystemExit(1)
        assert result.outputs["answer.txt"] == request.inputs["source.txt"]
        repeated = run.call(request)
        assert repeated.reused and len(repeated.attempts) == len(result.attempts)
        assert repeated.attempts[-1].launch_id == result.attempts[-1].launch_id
    attempt = result.attempts[-1]
    evidence = parse_evidence(
        args.harness,
        (Path(attempt.launch_dir) / "stdout.log").read_text(encoding="utf-8"),
    )
    print(json.dumps({
        "harness": args.harness,
        "requested_model": args.model,
        "status": result.status,
        "attempts": len(result.attempts),
        "reused": repeated.reused,
        "records": str(workdir / "records"),
        "evidence": evidence,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
