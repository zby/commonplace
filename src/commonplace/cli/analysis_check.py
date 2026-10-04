"""Check an analysis draft with its job's acceptance validator, without replay."""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import UTC, datetime
from pathlib import Path

from commonplace.lib.agentic_workflow import AnalyseAgenticSystem
from commonplace.lib.library import checks_library
from commonplace.lib.quote_matching import parse_blockquotes
from commonplace.workflow.engine import load_definition
from commonplace.workflow.store import RunStore, StateError


def check_draft(run_dir: Path, job_name: str, draft: Path | None = None) -> tuple[Path, list[str]]:
    """Read the run's definition and construct its validator without stepping.

    Checks remain ordinary functions of the output and supplied context. The
    workflow record selects their existing constructors, including subclasses.
    """
    store = RunStore(run_dir)
    record = store.read_json(store.run_file)
    definition = load_definition(record["definition"])(record["params"])
    if not isinstance(definition, AnalyseAgenticSystem):
        raise ValueError("this command checks AnalyseAgenticSystem jobs")  # noqa: TRY004
    job = definition.acceptance_job(run_dir, job_name)
    output = draft or job.output_path(run_dir)
    if not output.is_file():
        raise ValueError(f"{output}: output file is missing; write the assigned draft before checking it")
    refusals = list(job.validator(output)) if job.validator is not None else []
    return output, refusals


@checks_library
def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("run_state", type=Path, help="supplied run-state.md (or its run directory)")
    parser.add_argument("job", help="supplied job name, including its round")
    parser.add_argument("draft", nargs="?", type=Path, help="draft to check; defaults to the job's output")
    args = parser.parse_args(argv)
    run_dir = args.run_state.resolve()
    if run_dir.is_file():
        run_dir = run_dir.parent
    try:
        # Reject path traversal before constructing a job or a scratch path.
        if not args.job or "/" in args.job or "\\" in args.job or args.job in (".", ".."):
            raise ValueError("job must be the supplied analysis job name")
        output, refusals = check_draft(run_dir, args.job, args.draft.resolve() if args.draft else None)
        quotes = parse_blockquotes(output.read_text(encoding="utf-8"))
        counts = Counter(reason.split(": rule ", 1)[-1].split(":", 1)[0] for reason in refusals)
        event = {
            "time": datetime.now(UTC).isoformat(), "job": args.job,
            "draft": str(output), "refusals_by_rule": dict(counts),
            "quotations": {
                "inspected": len(quotes),
                "not_found": sum("quotation not found:" in reason for reason in refusals),
                "ambiguous": sum("quotation ambiguous:" in reason for reason in refusals),
            },
        }
        scratch = run_dir / "jobs" / args.job / "scratch"
        scratch.mkdir(parents=True, exist_ok=True)
        with (scratch / "acceptance-checks.jsonl").open("a", encoding="utf-8") as log:
            log.write(json.dumps(event, ensure_ascii=False) + "\n")
    except (OSError, ValueError, KeyError, StateError) as error:
        print(f"analysis check: {error}", file=sys.stderr)
        return 2
    if refusals:
        print("\n".join(refusals))
        return 1
    print(f"{output.name}: acceptance check passes; this does not establish claim support")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
