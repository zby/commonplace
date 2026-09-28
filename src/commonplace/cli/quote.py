"""Generate citations for selected text in a frozen agentic-analysis source.

The agent chooses an occurrence and inserts its citation unchanged. This
command writes no artifacts and performs no document validation. Publication
uses the regular validator to check the assembled analysis set.
One occurrence prints only the Markdown citation. Two to ten occurrences print
JSON candidates with selection metadata. More than ten asks for a longer quote.
With --selections, a JSON list of {key, source_path, text} objects is resolved
in one call and a JSON object keyed by selection is printed; exit status 2
means at least one key needs a choice among candidates or failed.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from commonplace.lib.agentic_analysis import load_run_state
from commonplace.lib.library import checks_library
from commonplace.lib.quote_generation import generate_quote_batch, generate_quotes


@checks_library
def main(argv: list[str] | None = None, *, cwd: Path | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "run_state",
        type=Path,
        help="Running analysis run-state.md with its frozen source",
    )
    parser.add_argument(
        "--source-path", help="Full commit-relative Git path; omit for a capture"
    )
    parser.add_argument(
        "--text-file", default="-", help="UTF-8 text to locate; default: read stdin"
    )
    parser.add_argument(
        "--selections",
        help=(
            "JSON file holding a list of {key, source_path, text} selections to "
            "resolve together; replaces --source-path and --text-file"
        ),
    )
    args = parser.parse_args(argv)
    if args.selections and (args.source_path or args.text_file != "-"):
        parser.error("--selections replaces --source-path and --text-file")
    repo_root = (cwd or Path.cwd()).resolve()
    try:
        state = load_run_state((repo_root / args.run_state).resolve(), repo_root=repo_root)
        if state.status != "running" or state.source is None:
            raise ValueError(
                "quotation generation requires a running run with a frozen source"
            )
        if args.selections:
            selections = json.loads(
                (repo_root / args.selections).read_text(encoding="utf-8")
            )
            results = generate_quote_batch(selections, source=state.source)
        else:
            text = (
                sys.stdin.read()
                if args.text_file == "-"
                else (repo_root / args.text_file).read_text(encoding="utf-8")
            )
            payload = generate_quotes(
                text, source=state.source, source_path=args.source_path
            )
    except (OSError, ValueError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    if args.selections:
        print(json.dumps(results, ensure_ascii=False, indent=2))
        unresolved = [k for k, v in results.items() if v["status"] != "citation"]
        if unresolved:
            print(
                f"{len(unresolved)} of {len(results)} selections need attention: "
                + ", ".join(f"{k} ({results[k]['status']})" for k in unresolved),
                file=sys.stderr,
            )
            return 2
        return 0
    if isinstance(payload, str):
        sys.stdout.write(payload)
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
