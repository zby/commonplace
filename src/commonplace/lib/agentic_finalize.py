"""Mechanical finalization of an analysis set: the manifest.

``output/ARTIFACT.yaml`` pins every member present in ``output/``. It is
derived here from bytes on disk, so it is reproducible.
"""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import yaml

from commonplace.lib.agentic_set import (
    OUTPUT_DIR,
    OVERVIEW_NAME,
    SET_NAMES,
    SET_TYPE,
)
from commonplace.lib.directory_artifact import MANIFEST_NAME


def build_manifest(run_dir: Path) -> str:
    """Write ``output/ARTIFACT.yaml`` pinning the set members present in ``output/``."""
    output = run_dir / OUTPUT_DIR
    members = {}
    for name in SET_NAMES:
        path = output / name
        if path.is_file():
            members[name] = {"sha256": sha256(path.read_bytes()).hexdigest()}
    if OVERVIEW_NAME not in members:
        raise ValueError(f"missing: {output / OVERVIEW_NAME}")
    text = yaml.safe_dump({"type": SET_TYPE, "members": members}, sort_keys=False)
    (output / MANIFEST_NAME).write_text(text, encoding="utf-8")
    return text
