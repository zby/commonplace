"""Boundary invocation checks shared by the legacy and new analysis consumers."""

from __future__ import annotations

import json
import re
import subprocess
from hashlib import sha256
from pathlib import Path
from typing import Any

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
        if frozen is None and capture_directory is not None:
            if source.get("kind") != "capture":
                refusals.append("a non-Git acquisition requires a capture, not a worker-acquired Git checkout")
            else:
                if not Path(str(source.get("path") or "")).is_relative_to(capture_directory):
                    refusals.append(f"capture source.path must be in the supplied capture-directory: {capture_directory}")
                if fields.get("reviewed-boundary") != source.get("revision"):
                    refusals.append("reviewed-boundary must be the frozen capture's label")
        if source.get("identity") != identity:
            refusals.append(f"source.identity must be `{identity}`, the run's source identity")
        refusals += frozen_source_refusals(source)
    return refusals


def frozen_source_refusals(source: dict[str, Any]) -> list[str]:
    """Verify a clean Git checkout's commit or a capture file's exact digest."""
    path = Path(str(source.get("path") or ""))
    if not path.is_absolute():
        return ["source.path must be the absolute path of the frozen source"]
    if path.is_symlink() or path.resolve() != path:
        return ["source.path must be canonical and not redirected through a symlink"]
    if source.get("kind") == "capture":
        if not path.is_file():
            return [f"source.path {path} is not a file"]
        digest = sha256(path.read_bytes()).hexdigest()
        if source.get("sha256") != digest:
            return [f"source.sha256 must be the SHA-256 of the capture file: expected {digest}"]
        return []
    revision = str(source.get("revision") or "")
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        return ["source.revision must be a full 40-hex commit"]

    def git(*args: str) -> str | None:
        result = subprocess.run(
            ["git", "-C", str(path), *args], capture_output=True, text=True, check=False, timeout=30,
        )
        return result.stdout if result.returncode == 0 else None

    head = git("rev-parse", "HEAD") if path.is_dir() else None
    if head is None:
        return [f"source.path {path} is not a Git checkout"]
    root = git("rev-parse", "--show-toplevel")
    if root is None or Path(root.strip()).resolve() != path:
        return ["source.path must be the Git checkout root"]
    if head.strip() != revision:
        return [f"the checkout at {path} is not at source.revision"]
    status = git("status", "--porcelain")
    if status is None or status:
        return [
            (
                f"the checkout at {path} does not hold exactly the commit's files; "
                "a clone made without checkout lists them all as deleted"
            )
        ]
    return []
