"""Mechanical finalization of an analysis set: the manifest.

``output/ARTIFACT.yaml`` pins every member present in ``output/`` and records
the worker that produced the run. It is derived here from bytes on disk, so
it is reproducible.
"""

from __future__ import annotations

import json
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

RUN_METADATA_NAME = "run-metadata.json"
WORKER_FIELDS = ("model", "effort")


def build_manifest(run_dir: Path) -> str:
    """Write ``output/ARTIFACT.yaml`` pinning the set members present in
    ``output/`` and naming the worker recorded in the run's metadata.

    One model writes a whole run, so the manifest carries it once, as the
    orchestrator recorded it when the run opened.
    """
    output = run_dir / OUTPUT_DIR
    members = {}
    for name in SET_NAMES:
        path = output / name
        if path.is_file():
            members[name] = {"sha256": sha256(path.read_bytes()).hexdigest()}
    if OVERVIEW_NAME not in members:
        raise ValueError(f"missing: {output / OVERVIEW_NAME}")
    manifest = {"type": SET_TYPE, "members": members}
    metadata_path = run_dir / RUN_METADATA_NAME
    if metadata_path.is_file():
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        worker = {field: metadata[field] for field in WORKER_FIELDS if metadata.get(field)}
        if worker:
            manifest["worker"] = worker
    text = yaml.safe_dump(manifest, sort_keys=False)
    (output / MANIFEST_NAME).write_text(text, encoding="utf-8")
    return text
