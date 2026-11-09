"""Scripted prepared command for scheduler/process permutations, not a workflow.

Every invocation has its own cwd/key and barrier. The full workflow wiring is
covered separately by test_automation's real prepared-command fixtures.
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    parser.add_argument("key")
    for name in ("system", "source-identity", "source", "worker-profile", "source-revision", "timeout", "max-workers", "model"):
        parser.add_argument("--" + name)
    args = parser.parse_args()
    root = Path(os.environ["QUEUE_FIXTURE"])
    result = Path.cwd() / "queue-result.json"
    if args.command in ("integrate", "inspect-integration"):
        data = json.loads(result.read_text())
        key = data["result"]["allocation-key"]
        integration = Path.cwd() / "integration-result.json"
        if args.command == "integrate":
            (root / f"{key}.integration-started").touch()
            while (root / "integration-hold").exists() and not (root / f"{key}.integration-release").exists():
                time.sleep(.02)
            integration.write_text(json.dumps({"state": "integrated", "publication-commit": key,
                                               "merge-commit": "merge-" + key}))
            (root / f"{key}.integration-finished").touch()
        print(integration.read_text() if integration.exists() else json.dumps({"state": "pending"}))
        return
    if args.command == "execute":
        (root / f"{args.key}.started").touch()
        while not (root / f"{args.key}.release").exists():
            time.sleep(.02)
        kind = (root / f"{args.key}.outcome").read_text()
        view = {"run-id": f"run-{args.key}", "state": {"published": "published", "local-complete": "local",
                "stopped": "stopped", "operator-attention": "interrupted"}[kind],
                "unsettled-launches": ["unsettled-fixture"] if kind == "operator-attention" else [],
                "stopped": "fixture stop" if kind == "stopped" else None,
                "advisory-audit": {"state": "skipped"}, "receipt": {"target": args.source_identity}}
        parameters = {"system": args.system, "source-identity": args.source_identity, "source": args.source,
                      "worker-profile": args.worker_profile}
        binding = {"run-id": view["run-id"], "method-commit": "fixture-commit", "parameters": parameters}
        data = {"allocation": binding, "inspection": view,
                "result": {"status": kind, "inspection": view, "allocation-key": args.key}}
        temporary = result.with_suffix(".tmp")
        temporary.write_text(json.dumps(data))
        temporary.replace(result)
        (root / f"{args.key}.finished").touch()
    elif args.command != "inspect-execution":
        raise ValueError(f"unexpected fixture command {args.command}")
    print(result.read_text())


if __name__ == "__main__":
    main()
