"""Capture a directory's bytes and compare captures; report facts, not verdicts."""

import argparse
import hashlib
import json
import os
import tarfile
from pathlib import Path


def inventory(root):
    result = {}
    for path in sorted(root.rglob("*")):
        name = str(path.relative_to(root))
        if path.is_symlink():
            result[name] = {"symlink": os.readlink(path)}
        elif path.is_file():
            with path.open("rb") as stream:
                result[name] = {
                    "sha256": hashlib.file_digest(stream, "sha256").hexdigest()
                }
    return result


def capture(root, output, archive=False):
    root, output = root.resolve(), output.resolve()
    if not root.is_dir():
        raise ValueError(f"Not a directory: {root}")
    if output.is_relative_to(root):
        raise ValueError("Capture output must be outside the captured directory")
    output.mkdir(parents=True, exist_ok=False)
    state = inventory(root)
    (output / "inventory.json").write_text(json.dumps(state, indent=2) + "\n")
    if archive:
        with tarfile.open(output / "files.tar.gz", "w:gz") as bundle:
            bundle.add(root, arcname=root.name)
    return state


def compare(before, after):
    return {
        "added": sorted(after.keys() - before.keys()),
        "removed": sorted(before.keys() - after.keys()),
        "modified": sorted(
            k for k in before.keys() & after.keys() if before[k] != after[k]
        ),
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    snapshot = commands.add_parser(
        "capture", help="Save hashes and optionally an archive"
    )
    snapshot.add_argument("root", type=Path)
    snapshot.add_argument("output", type=Path, help="New directory outside root")
    snapshot.add_argument("--archive", action="store_true")
    difference = commands.add_parser(
        "compare", help="Print changed paths; changes still exit 0"
    )
    difference.add_argument("before", type=Path, help="Earlier capture directory")
    difference.add_argument("after", type=Path, help="Later capture directory")
    args = parser.parse_args()
    try:
        if args.command == "capture":
            capture(args.root, args.output, args.archive)
            print(f"Captured: {args.output}")
        else:
            before = json.loads((args.before / "inventory.json").read_text())
            after = json.loads((args.after / "inventory.json").read_text())
            print(json.dumps(compare(before, after), indent=2))
    except (OSError, ValueError) as error:
        parser.exit(1, f"State capture error: {error}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
