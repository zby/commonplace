from __future__ import annotations

from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parents[3] / "src" / "commonplace" / "review"


def test_legacy_notes_selector_stack_was_removed() -> None:
    """The old selector stack was replaced by the gate-based review system."""
    legacy_paths = [
        PACKAGE_ROOT / "review_state.py",
        PACKAGE_ROOT / "selector_engine.py",
        PACKAGE_ROOT / "notes_selector.py",
        PACKAGE_ROOT / "ack_review.py",
    ]

    for path in legacy_paths:
        assert not path.exists(), f"legacy script unexpectedly present: {path.name}"


def test_gate_review_replacements_exist() -> None:
    """Current review workflows use the gate-based scripts instead."""
    replacement_paths = [
        PACKAGE_ROOT / "review_target_selector.py",
        PACKAGE_ROOT / "ack_gate_review.py",
        PACKAGE_ROOT / "resolve_gates.py",
        PACKAGE_ROOT / "warn_selector.py",
        PACKAGE_ROOT / "review_model.py",
        PACKAGE_ROOT / "review_metadata.py",
        PACKAGE_ROOT / "review_db.py",
    ]

    for path in replacement_paths:
        assert path.exists(), f"expected replacement script missing: {path}"
