"""Boundary invocation and frozen-source checks for analysis consumers."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from commonplace.artifactrun.sources import frozen_source_refusals
from commonplace.lib.note_parser import parse_document


def boundary_refusals(
    candidate: Path | bytes, *, repo_root: Path, run_id: str, identity: str,
    frozen: dict[str, Any] | None = None, capture_directory: Path | None = None,
) -> list[str]:
    """Invocation-only checks against run parameters and pinned source bytes."""
    try:
        text = candidate.decode("utf-8") if isinstance(candidate, bytes) else candidate.read_text(encoding="utf-8")
        document, error = parse_document(text)
    except UnicodeError:
        return []  # The content validator reports unreadable candidate bytes.
    if document is None or error:
        return []
    fields = dict(document.frontmatter or {})
    refusals = []
    if fields.get("run-id") != run_id:
        refusals.append(f"member identity: run-id {fields.get('run-id')!r} does not match {run_id!r}")
    source = fields.get("source")
    # A non-complete disposition does not authorize discarding code's source pin.
    if frozen is not None and (
        source != frozen or fields.get("reviewed-boundary") != frozen["revision"]
    ):
        if frozen.get("kind") == "capture":
            refusals.append(
                "source must preserve the incumbent boundary's frozen capture and "
                f"reviewed-boundary its label `{frozen['revision']}`: {json.dumps(frozen)}"
            )
        else:
            refusals.append(
                "source must be exactly the checkout code froze, and reviewed-boundary "
                f"its commit `{frozen['revision']}`: {json.dumps(frozen)}"
            )
    if isinstance(source, dict):
        # Authorize the declared source before inspecting its bytes or running Git.
        # Other member errors (run-id or reviewed-boundary) do not make a source
        # that matches the pin unsafe to inspect for independent diagnostics.
        authorized = frozen is None or source == frozen
        if frozen is None and capture_directory is not None:
            if source.get("kind") != "capture":
                refusals.append("a non-Git acquisition requires a capture, not a worker-acquired Git checkout")
                authorized = False
            else:
                path = Path(str(source.get("path") or ""))
                if not path.is_absolute() or ".." in path.parts or not path.is_relative_to(capture_directory):
                    refusals.append(f"capture source.path must be in the supplied capture-directory: {capture_directory}")
                    authorized = False
                if fields.get("reviewed-boundary") != source.get("revision"):
                    refusals.append("reviewed-boundary must be the frozen capture's label")
        if source.get("identity") != identity:
            refusals.append(f"source.identity must be `{identity}`, the run's source identity")
            authorized = False
        if authorized:
            refusals += frozen_source_refusals(source)
    return refusals
