"""Gate type requirements name types the way notes do: by their path under a KB root."""

from __future__ import annotations

from pathlib import Path

from commonplace.review.resolve_criteria import applicable_criterion_ids_for_note

REPO_ROOT = Path(__file__).resolve().parents[3]
GATES = REPO_ROOT / "kb" / "instructions" / "review-gates"


def test_definition_gate_applies_to_a_definition_note(tmp_path: Path) -> None:
    note = tmp_path / "term.md"
    note.write_text(
        "---\ndescription: A definition note for the requirement check\ntype: types/definition.md\n---\n\n# Term\n",
        encoding="utf-8",
    )
    gate = "semantic/explication-quality"

    assert applicable_criterion_ids_for_note(note, [gate], GATES) == [gate]
