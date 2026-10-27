from __future__ import annotations

import os
from pathlib import Path

import pytest

# Windows refuses to create symlinks without Developer Mode or elevation.
ERROR_PRIVILEGE_NOT_HELD = 1314


def symlink_or_skip(link: Path, target: Path | str, *, directory: bool = False) -> None:
    """Create a symlink, or skip the test where Windows does not allow it."""
    try:
        link.symlink_to(target, target_is_directory=directory)
    except OSError as error:
        if getattr(error, "winerror", None) == ERROR_PRIVILEGE_NOT_HELD:
            pytest.skip("creating symlinks needs Developer Mode or elevation on Windows")
        raise


def junction(link: Path, target: Path) -> None:
    """Create a Windows directory junction, which needs no privilege."""
    import _winapi

    _winapi.CreateJunction(os.fspath(target), os.fspath(link))
