"""Print the source directory of the installed Commonplace package."""

from __future__ import annotations

from pathlib import Path

import commonplace


def source_path() -> Path:
    """Return the directory containing the executing Commonplace package."""
    package_file = commonplace.__file__
    if package_file is None:
        raise RuntimeError("cannot locate the installed commonplace package source")
    return Path(package_file).resolve().parent


def main() -> int:
    print(source_path())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
