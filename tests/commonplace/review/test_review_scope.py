from pathlib import Path

import pytest

from commonplace.cli.review.ack_trivial_note_changes import main as ack_main
from commonplace.cli.review.review_target_selector import main as selector_main
from commonplace.review.review_target_selector import (
    _select_notes,
    select_stale_criteria,
)
from tests.commonplace.review.test_review_target_selector import (
    make_gate,
    make_note,
    write,
)


def test_verified_review_uses_only_explicit_arbitrary_roots(tmp_path: Path):
    root = tmp_path / "kb/teams/claims"
    write(root / "COLLECTION.md", "---\ntype: types/collection-contract.md\n---\n# Contract\n")
    verified = make_note(root / "verified.md", "Verified", "Body", user_verified=True)
    make_note(root / "unverified.md", "Unverified", "Body")
    make_note(root / "nested/deep.md", "Deep", "Body", user_verified=True)
    make_note(tmp_path / "kb/inbox/unselected.md", "Outside", "Body", user_verified=True)
    gate = tmp_path / "kb/instructions/review-gates/prose/source-residue.md"
    make_gate(gate, "prose/source-residue", "prose")
    records = select_stale_criteria(
        tmp_path, model=None, criterion_ids=["prose/source-residue"],
        note_filter=[str(root)], user_verified_only=True, freshness_baselines={},
    )
    assert [record.note_path for record in records] == ["kb/teams/claims/verified.md"]
    assert _select_notes(tmp_path, note_filter=[str(root)], user_verified_only=False) == [
        root / "unverified.md", verified,
    ]
    assert not (tmp_path / "kb/reports").exists()


def test_verified_flag_cannot_select_or_ack_an_implicit_global_scope(tmp_path: Path):
    make_note(tmp_path / "kb/notes/verified.md", "Verified", "Body", user_verified=True)
    with pytest.raises(ValueError, match="only filters explicit scope"):
        select_stale_criteria(
            tmp_path, model=None, criterion_ids=[], user_verified_only=True,
        )
    assert not (tmp_path / "kb/reports").exists()


def test_review_ignored_directory_requires_explicit_file(tmp_path: Path):
    root = tmp_path / "kb/captures"
    write(root / ".commonplace-validation-ignore", "")
    capture = make_note(root / "packet/capture.md", "Capture", "Body")
    with pytest.raises(ValueError, match="select files explicitly"):
        _select_notes(tmp_path, note_filter=[str(capture.parent)], user_verified_only=False)
    assert _select_notes(tmp_path, note_filter=[str(capture)], user_verified_only=False) == [capture]


@pytest.mark.parametrize("command", [selector_main, ack_main])
def test_review_commands_reject_verified_sweep_without_targets(tmp_path: Path, command):
    with pytest.raises(SystemExit) as exc:
        command([
            "--all-gates", "--user-verified", "--model-partition", "test-model",
        ], cwd=tmp_path)
    assert exc.value.code == 2
    assert not (tmp_path / "kb/reports").exists()
