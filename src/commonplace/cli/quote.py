"""Generate citations for selected text in a frozen agentic-analysis source.

The agent chooses an occurrence and inserts its citation unchanged. This
command writes no artifacts and performs no document validation. Publication
uses the regular validator to check the assembled analysis bundle.
One occurrence prints only the Markdown citation. Two to ten occurrences print
JSON candidates with selection metadata. More than ten asks for a longer quote.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from commonplace.lib.agentic_analysis import parse_agentic_analysis_run_state
from commonplace.lib.library import checks_library
from commonplace.lib.note_parser import parse_document
from commonplace.lib.quote_generation import generate_quotes


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
    args = parser.parse_args(argv)
    repo_root = (cwd or Path.cwd()).resolve()
    try:
        path = (repo_root / args.run_state).resolve()
        document, error = parse_document(path.read_text(encoding="utf-8"))
        if error or document is None:
            raise ValueError(f"cannot parse run state: {error}")
        state = parse_agentic_analysis_run_state(path, document, repo_root=repo_root)
        if state.status != "running" or state.source is None:
            raise ValueError(
                "quotation generation requires a running run with a frozen source"
            )
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
    if isinstance(payload, str):
        sys.stdout.write(payload)
    else:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
