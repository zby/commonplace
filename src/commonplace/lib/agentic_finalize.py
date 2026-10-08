"""The analysis set's manifest, from its first write to its finished form.

A working ``output/ARTIFACT.yaml`` names only the type, so the set is
recognized while its members are written. The finished manifest pins every
layout member present in ``output/`` and records the worker that produced
the run. It is derived here from bytes on disk, so it is reproducible.
"""

from __future__ import annotations

import json
from hashlib import sha256
from pathlib import Path

import yaml

from commonplace.lib.agentic_set import OUTPUT_DIR, SET_TYPE, analysis_layout
from commonplace.lib.directory_artifact import MANIFEST_NAME

RUN_METADATA_NAME = "run-metadata.json"
WORKER_FIELDS = ("model", "effort")


def _require_legacy_run(run_dir: Path) -> None:
    """Reject engine or mixed directories before manufacturing a legacy twin."""
    if any((run_dir / name).exists() or (run_dir / name).is_symlink()
           for name in ("run.json", "state")):
        raise ValueError("legacy manifest functions refuse new-engine or mixed run directories")


def start_manifest(run_dir: Path) -> None:
    """Create ``output/`` with a type-only manifest, unless a manifest exists,
    so a replay of a finished run changes nothing."""
    _require_legacy_run(run_dir)
    output = run_dir / OUTPUT_DIR
    output.mkdir(exist_ok=True)
    if not (output / MANIFEST_NAME).exists():
        (output / MANIFEST_NAME).write_text(yaml.safe_dump({"type": SET_TYPE}), encoding="utf-8")


def build_manifest(run_dir: Path) -> str:
    """Write ``output/ARTIFACT.yaml`` pinning the layout members present in
    ``output/`` and naming the worker recorded in the run's metadata.

    One model writes a whole run, so the manifest carries it once, as the
    orchestrator recorded it when the run opened.
    """
    _require_legacy_run(run_dir)
    output = run_dir / OUTPUT_DIR
    layout = analysis_layout()
    members = {}
    for role in layout.roles.values():
        path = output / role.path
        if path.is_file():
            members[role.path] = {"sha256": sha256(path.read_bytes()).hexdigest()}
    for role in layout.required.always:
        if layout.path(role) not in members:
            raise ValueError(f"missing: {output / layout.path(role)}")
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
