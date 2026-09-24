"""Shared test helpers for validator and full-pass tests."""

from __future__ import annotations

from pathlib import Path

from commonplace.lib.hashing import content_sha256_for_text

REPO_ROOT = Path(__file__).resolve().parents[2]

# The validator resolves global and collection-local type specs from the repo
# root, so fixture repos need the real specs copied in.
NOTE_TYPE_SPECS = (
    "kb/types/note.md",
    "kb/types/note.schema.yaml",
    "kb/types/note-base.schema.yaml",
    "kb/types/type-spec.md",
    "kb/types/type-spec.schema.yaml",
)


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def copy_repo_files(root: Path, *relative_paths: str) -> None:
    """Copy real repo files (type specs, schemas) to the same paths under root."""
    for relative_path in relative_paths:
        write(
            root / relative_path,
            (REPO_ROOT / relative_path).read_text(encoding="utf-8"),
        )


def write_packet(
    root: Path,
    *,
    source_text: str = "source text\n",
    live_source_text: str | None = None,
    disposition: str = "keep",
    target_text: str = "target text\n",
    live_target_text: str | None = None,
    phase: str = "packet",
    final_text: str | None = None,
    closing_status: str | None = None,
    closing_repair_attempted: bool = False,
) -> Path:
    if phase == "complete" and closing_status is None:
        closing_status = "ready"
    closing_status_value = "null" if closing_status is None else closing_status
    repair_attempted_value = str(closing_repair_attempted).lower()

    source = root / "kb/notes/source.md"
    source.parent.mkdir(parents=True, exist_ok=True)
    source.write_text(
        source_text if live_source_text is None else live_source_text,
        encoding="utf-8",
    )

    packet = root / "kb/reports/state/full-pass/source/pass-1"
    packet.mkdir(parents=True)
    (packet / "source.txt").write_text(source_text, encoding="utf-8")

    if final_text is not None:
        (packet / "final.txt").write_text(final_text, encoding="utf-8")
        if closing_status == "hand-back":
            final_fields = f"""final_capture: source.txt
final_sha256: {content_sha256_for_text(source_text)}"""
        else:
            final_fields = f"""final_capture: final.txt
final_sha256: {content_sha256_for_text(final_text)}"""
    else:
        final_fields = """final_capture: null
final_sha256: null"""

    if disposition == "merge":
        target = root / "kb/notes/target.md"
        target.write_text(
            target_text if live_target_text is None else live_target_text,
            encoding="utf-8",
        )
        (packet / "merge-target.txt").write_text(target_text, encoding="utf-8")
        merge_fields = f"""merge_target: kb/notes/target.md
merge_target_capture: merge-target.txt
merge_target_title: Target
merge_target_sha256: {content_sha256_for_text(target_text)}"""
        resolution = "pending"
    else:
        merge_fields = """merge_target: null
merge_target_capture: null
merge_target_title: null
merge_target_sha256: null"""
        resolution = "not-required" if disposition == "keep" else "pending"

    report = packet / "full-pass-report.md"
    report.write_text(
        f"""---
description: Full improvement pass fixture with packet-owned captures for testing
type: kb/reports/types/full-pass-report.md
source: kb/notes/source.md
source_capture: source.txt
source_sha256: {content_sha256_for_text(source_text)}
pass_id: pass-1
phase: {phase}
closing_status: {closing_status_value}
closing_repair_attempted: {repair_attempted_value}
disposition: {disposition}
{merge_fields}
{final_fields}
resolution: {resolution}
resolved_at: null
resolution_authority: null
resolution_summary: null
resolution_rationale: null
resulting_paths: []
---

# Full Improvement Pass: Source

## Resolution

**Status:** {resolution}
**Resolved at:** —
**Authority:** —
**Outcome:** —
**Rationale:** —
**Resulting paths:** —
""",
        encoding="utf-8",
    )
    return report
