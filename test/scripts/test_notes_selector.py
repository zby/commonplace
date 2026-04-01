from __future__ import annotations

from pathlib import Path


SCRIPTS_DIR = Path(__file__).resolve().parents[2] / "scripts"


def test_legacy_notes_selector_stack_was_removed() -> None:
    """The old selector stack was replaced by the gate-based review system."""
    legacy_paths = [
        SCRIPTS_DIR / "review_state.py",
        SCRIPTS_DIR / "selector_engine.py",
        SCRIPTS_DIR / "notes_selector.py",
        SCRIPTS_DIR / "ack_review.py",
    ]

    for path in legacy_paths:
        assert not path.exists(), f"legacy script unexpectedly present: {path.name}"


def test_gate_review_replacements_exist() -> None:
    """Current review workflows use the gate-based scripts instead."""
    replacement_paths = [
        SCRIPTS_DIR / "review_target_selector.py",
        SCRIPTS_DIR / "ack_gate_review.py",
        SCRIPTS_DIR / "resolve_gates.py",
        SCRIPTS_DIR / "warn_selector.py",
        SCRIPTS_DIR / "review_model.py",
        SCRIPTS_DIR / "review_metadata.py",
        SCRIPTS_DIR / "review_db.py",
    ]

    for path in replacement_paths:
        assert path.exists(), f"expected replacement script missing: {path}"
