from __future__ import annotations

from pathlib import Path


REVIEW_LIB_ROOT = Path(__file__).resolve().parents[3] / "src" / "commonplace" / "review"
REVIEW_CLI_ROOT = Path(__file__).resolve().parents[3] / "src" / "commonplace" / "cli" / "review"


def test_legacy_notes_selector_stack_was_removed() -> None:
    """The old selector stack was replaced by the gate-based review system."""
    legacy_paths = [
        REVIEW_LIB_ROOT / "review_state.py",
        REVIEW_LIB_ROOT / "selector_engine.py",
        REVIEW_LIB_ROOT / "notes_selector.py",
        REVIEW_LIB_ROOT / "ack_review.py",
    ]

    for path in legacy_paths:
        assert not path.exists(), f"legacy script unexpectedly present: {path.name}"


def test_gate_review_replacements_exist() -> None:
    """Current review workflows use the gate-based scripts instead."""
    replacement_paths = [
        REVIEW_LIB_ROOT / "review_target_selector.py",
        REVIEW_CLI_ROOT / "ack_gate_review.py",
        REVIEW_LIB_ROOT / "resolve_gates.py",
        REVIEW_LIB_ROOT / "warn_selector.py",
        REVIEW_LIB_ROOT / "review_model.py",
        REVIEW_LIB_ROOT / "review_metadata.py",
        REVIEW_LIB_ROOT / "review_db.py",
    ]

    for path in replacement_paths:
        assert path.exists(), f"expected replacement script missing: {path}"
