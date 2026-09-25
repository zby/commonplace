"""Print the source directory of the installed Commonplace package."""

from __future__ import annotations

import argparse
from collections.abc import Sequence
from pathlib import Path

import commonplace
from commonplace.lib.library import checks_library


def source_path() -> Path:
    """Return the directory containing the executing Commonplace package."""
    package_file = commonplace.__file__
    if package_file is None:
        raise RuntimeError("cannot locate the installed commonplace package source")
    return Path(package_file).resolve().parent


@checks_library
def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args(argv)
    print(source_path())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
