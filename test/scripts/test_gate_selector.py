from __future__ import annotations

import importlib.util
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest


SCRIPTS_DIR = Path(__file__).resolve().parents[2] / "scripts"
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

TEST_MODEL = "test-model"
os.environ["COMMONPLACE_REVIEW_MODEL"] = TEST_MODEL


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


gate_selector = load_module("gate_selector", SCRIPTS_DIR / "gate_selector.py")
resolve_gates = load_module("resolve_gates", SCRIPTS_DIR / "resolve_gates.py")
review_metadata = load_module("review_metadata", SCRIPTS_DIR / "review_metadata.py")


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_note(path: Path, title: str, body: str) -> Path:
    return write(
        path,
        f"""---
description: Test note
type: note
traits: []
status: current
---

# {title}
{body}
""",
    )


def make_gate(path: Path, gate_id: str, lens: str) -> Path:
    return write(
        path,
        f"""---
gate_id: {gate_id}
name: {path.stem.replace("-", " ").title()}
lens: {lens}
watches: [body]
staleness: changed
---

## Failure mode

Fixture gate.

## Test

Fixture test.
""",
    )


def make_review(
    path: Path,
    *,
    note_path: str,
    gate_id: str,
    note_sha: str,
    note_commit: str | None,
    gate_fingerprint: str,
    with_metadata: bool = True,
    last_full_review_note_sha: str | None = None,
    last_full_review_note_commit: str | None = None,
    last_full_review_at: str | None = None,
    last_acceptance_kind: str = "full-review",
) -> Path:
    body = "## Review\n\nCLEAN\n"
    if not with_metadata:
        return write(path, body)

    metadata = review_metadata.ReviewMetadata(
        note_path=note_path,
        gate_id=gate_id,
        gate_fingerprint=gate_fingerprint,
        last_full_review_note_sha=last_full_review_note_sha or note_sha,
        last_full_review_note_commit=last_full_review_note_commit or note_commit,
        last_full_review_at=last_full_review_at or "2026-03-31T00:00:00+00:00",
        last_accepted_note_sha=note_sha,
        last_accepted_note_commit=note_commit,
        last_accepted_at="2026-03-31T00:00:00+00:00",
        last_acceptance_kind=last_acceptance_kind,
        review_type="gate-review",
    )
    return write(path, review_metadata.inject_review_metadata(body, metadata))


def init_repo(path: Path) -> None:
    subprocess.run(["git", "init"], cwd=path, check=True, capture_output=True)
    subprocess.run(
        ["git", "config", "user.name", "Test User"],
        cwd=path,
        check=True,
        capture_output=True,
    )
    subprocess.run(
        ["git", "config", "user.email", "test@example.com"],
        cwd=path,
        check=True,
        capture_output=True,
    )


def commit_all(path: Path, message: str, date: str | None = None) -> str:
    subprocess.run(["git", "add", "."], cwd=path, check=True, capture_output=True)
    env = os.environ.copy()
    if date:
        env["GIT_COMMITTER_DATE"] = date
        env["GIT_AUTHOR_DATE"] = date
    subprocess.run(
        ["git", "commit", "-m", message],
        cwd=path,
        check=True,
        capture_output=True,
        env=env,
    )
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=path,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def build_fixture(tmp_path: Path) -> dict[str, Path | str]:
    init_repo(tmp_path)
    notes_dir = tmp_path / "kb" / "notes"
    gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
    reviews_dir = tmp_path / "kb" / "reports" / "reviews"

    stable = make_note(notes_dir / "stable.md", "Stable title", "\nLine 1.\nLine 2.\n")
    unreviewed = make_note(notes_dir / "unreviewed.md", "Unreviewed title", "\nBody.\n")

    g1 = make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")
    g2 = make_gate(
        gates_dir / "prose" / "confidence-miscalibration.md",
        "prose/confidence-miscalibration",
        "prose",
    )
    g3 = make_gate(
        gates_dir / "semantic" / "grounding-alignment.md",
        "semantic/grounding-alignment",
        "semantic",
    )
    commit = commit_all(tmp_path, "Initial fixture", date="2020-01-01T00:00:00+00:00")

    stable_sha = review_metadata.git_blob_sha(stable, write_object=True)
    g1_sha = review_metadata.git_blob_sha(g1, write_object=True)
    g2_sha = review_metadata.git_blob_sha(g2, write_object=True)
    g3_sha = review_metadata.git_blob_sha(g3, write_object=True)

    r1 = make_review(
        reviews_dir / "kb__notes__stable" / "prose__source-residue.test-model.md",
        note_path="kb/notes/stable.md",
        gate_id="prose/source-residue",
        note_sha=stable_sha,
        note_commit=commit,
        gate_fingerprint=g1_sha,
    )
    r2 = make_review(
        reviews_dir / "kb__notes__stable" / "prose__confidence-miscalibration.test-model.md",
        note_path="kb/notes/stable.md",
        gate_id="prose/confidence-miscalibration",
        note_sha=stable_sha,
        note_commit=commit,
        gate_fingerprint=g2_sha,
    )
    r3 = make_review(
        reviews_dir / "kb__notes__stable" / "semantic__grounding-alignment.test-model.md",
        note_path="kb/notes/stable.md",
        gate_id="semantic/grounding-alignment",
        note_sha=stable_sha,
        note_commit=commit,
        gate_fingerprint=g3_sha,
    )

    return {
        "stable": stable,
        "unreviewed": unreviewed,
        "gate_prose_sr": g1,
        "gate_prose_cm": g2,
        "gate_semantic_ga": g3,
        "review_sr": r1,
        "review_cm": r2,
        "review_ga": r3,
        "commit": commit,
    }


class TestMissingReview:
    def test_missing_review_marks_stale(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = gate_selector.select_stale_gates(
            tmp_path,
            bundle="prose",
            note_filter=["kb/notes/unreviewed.md"],
        )
        assert [(s.gate_id, s.reason) for s in stale] == [
            ("prose/confidence-miscalibration", "missing-review"),
            ("prose/source-residue", "missing-review"),
        ]

    def test_review_without_metadata_counts_as_missing(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        write(
            fixture["review_sr"],
            "## Review\n\nLegacy review body only.\n",
        )
        stale = gate_selector.select_stale_gates(
            tmp_path,
            bundle="prose",
            note_filter=["kb/notes/stable.md"],
        )
        assert [(s.gate_id, s.reason) for s in stale] == [
            ("prose/source-residue", "missing-review"),
        ]

    def test_all_gates_finds_missing_across_bundles(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = gate_selector.select_stale_gates(
            tmp_path,
            include_all=True,
            note_filter=["kb/notes/unreviewed.md"],
        )
        gate_ids = [s.gate_id for s in stale]
        assert "prose/source-residue" in gate_ids
        assert "semantic/grounding-alignment" in gate_ids


class TestFreshReview:
    def test_review_with_matching_metadata_is_fresh(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = gate_selector.select_stale_gates(
            tmp_path,
            bundle="prose",
            note_filter=["kb/notes/stable.md"],
        )
        assert stale == []


class TestGateChanged:
    def test_gate_fingerprint_change_marks_stale(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        make_gate(
            fixture["gate_prose_sr"],
            "prose/source-residue",
            "prose",
        )
        fixture["gate_prose_sr"].write_text(
            fixture["gate_prose_sr"].read_text(encoding="utf-8") + "\nExtra line.\n",
            encoding="utf-8",
        )

        stale = gate_selector.select_stale_gates(
            tmp_path,
            bundle="prose",
            note_filter=["kb/notes/stable.md"],
        )
        assert [(s.gate_id, s.reason) for s in stale] == [
            ("prose/source-residue", "gate-changed"),
        ]


class TestNoteChanged:
    def test_note_sha_change_marks_stale(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        make_note(fixture["stable"], "Stable title", "\nUpdated line.\n")

        stale = gate_selector.select_stale_gates(
            tmp_path,
            bundle="prose",
            note_filter=["kb/notes/stable.md"],
        )
        assert [(s.gate_id, s.reason) for s in stale] == [
            ("prose/confidence-miscalibration", "note-changed"),
            ("prose/source-residue", "note-changed"),
        ]


class TestAckMetadata:
    def test_ack_updates_existing_review_metadata(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        original_text = fixture["review_sr"].read_text(encoding="utf-8")
        original_metadata = review_metadata.parse_review_metadata(original_text)
        assert original_metadata is not None
        make_note(fixture["stable"], "Stable title", "\nUpdated line.\n")

        stale_before = gate_selector.select_stale_gates(
            tmp_path,
            bundle="prose",
            note_filter=["kb/notes/stable.md"],
        )
        assert len(stale_before) == 2

        gate_selector.ack_pairs(
            tmp_path,
            [
                "kb/notes/stable.md:prose/source-residue",
                "kb/notes/stable.md:prose/confidence-miscalibration",
            ],
            TEST_MODEL,
        )

        stale_after = gate_selector.select_stale_gates(
            tmp_path,
            bundle="prose",
            note_filter=["kb/notes/stable.md"],
        )
        assert stale_after == []

        updated_text = fixture["review_sr"].read_text(encoding="utf-8")
        updated_metadata = review_metadata.parse_review_metadata(updated_text)
        assert updated_metadata is not None
        assert updated_metadata.last_full_review_note_sha == original_metadata.last_full_review_note_sha
        assert updated_metadata.last_acceptance_kind == "trivial-change-ack"
        assert updated_metadata.last_accepted_note_sha == review_metadata.git_blob_sha(fixture["stable"])
        assert "## Review" in updated_text

    def test_ack_creates_metadata_only_review_when_missing(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale_before = gate_selector.select_stale_gates(
            tmp_path,
            bundle="prose",
            note_filter=["kb/notes/unreviewed.md"],
        )
        assert len(stale_before) == 2

        gate_selector.ack_pairs(
            tmp_path,
            [
                "kb/notes/unreviewed.md:prose/confidence-miscalibration",
                "kb/notes/unreviewed.md:prose/source-residue",
            ],
            TEST_MODEL,
        )

        stale_after = gate_selector.select_stale_gates(
            tmp_path,
            bundle="prose",
            note_filter=["kb/notes/unreviewed.md"],
        )
        assert stale_after == []

        created = (
            tmp_path
            / "kb"
            / "reports"
            / "reviews"
            / "kb__notes__unreviewed"
            / "prose__source-residue.test-model.md"
        )
        metadata = review_metadata.parse_review_metadata(created.read_text(encoding="utf-8"))
        assert metadata is not None
        assert metadata.last_full_review_note_sha is None
        assert metadata.last_acceptance_kind == "trivial-change-ack"


class TestDiffGeneration:
    def test_note_changed_includes_diff_in_json_mode(self, tmp_path: Path) -> None:
        init_repo(tmp_path)
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        reviews_dir = tmp_path / "kb" / "reports" / "reviews"

        note_path = make_note(notes_dir / "target.md", "Target", "\nOriginal line.\n")
        gate_path = make_gate(gates_dir / "prose" / "test-gate.md", "prose/test-gate", "prose")
        commit = commit_all(tmp_path, "Initial", date="2020-01-01T00:00:00+00:00")

        review_path = make_review(
            reviews_dir / "kb__notes__target" / "prose__test-gate.test-model.md",
            note_path="kb/notes/target.md",
            gate_id="prose/test-gate",
            note_sha=review_metadata.git_blob_sha(note_path, write_object=True),
            note_commit=commit,
            gate_fingerprint=review_metadata.git_blob_sha(gate_path, write_object=True),
        )
        assert review_path.exists()

        make_note(note_path, "Target", "\nUpdated line.\n")

        stale = gate_selector.select_stale_gates(
            tmp_path,
            bundle="prose",
            note_filter=["kb/notes/target.md"],
            include_diff=True,
        )
        assert len(stale) == 1
        assert stale[0].reason == "note-changed"
        assert stale[0].diff is not None
        assert "Updated line" in stale[0].diff


class TestModelInPath:
    def test_review_path_includes_model(self, tmp_path: Path) -> None:
        path = gate_selector.review_path_for(
            "kb/notes/backlinks.md",
            "semantic/internal-consistency",
            "test-model",
        )
        assert path == Path(
            "kb/reports/reviews/kb__notes__backlinks/semantic__internal-consistency.test-model.md"
        )

    def test_model_encoding_normalizes_special_chars(self, tmp_path: Path) -> None:
        path = gate_selector.review_path_for(
            "kb/notes/backlinks.md",
            "prose/source-residue",
            "opus 4.6",
        )
        assert "opus-4-6" in str(path)


class TestJsonIncludesReviewPath:
    def test_review_path_in_json_output(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = gate_selector.select_stale_gates(
            tmp_path,
            bundle="prose",
            note_filter=["kb/notes/unreviewed.md"],
        )
        json_str = gate_selector.render_json(stale, TEST_MODEL)
        items = json.loads(json_str)
        assert len(items) == 2
        for item in items:
            assert "review_path" in item
            assert item["review_path"].startswith("kb/reports/reviews/")
            assert TEST_MODEL in item["review_path"]


class TestModelRequired:
    def test_selector_requires_review_model_env(self, tmp_path: Path, monkeypatch) -> None:
        build_fixture(tmp_path)
        monkeypatch.delenv("COMMONPLACE_REVIEW_MODEL", raising=False)

        with pytest.raises(ValueError, match="COMMONPLACE_REVIEW_MODEL is not set"):
            gate_selector.select_stale_gates(
                tmp_path,
                bundle="prose",
                note_filter=["kb/notes/stable.md"],
            )


class TestResolveGates:
    def test_individual_gate_resolves(self, tmp_path: Path) -> None:
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        ids = resolve_gates.resolve_to_gate_ids(["prose/source-residue"], gates_dir)
        assert ids == ["prose/source-residue"]

    def test_bundle_expands_to_all_gates(self, tmp_path: Path) -> None:
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        make_gate(gates_dir / "prose" / "a-gate.md", "prose/a-gate", "prose")
        make_gate(gates_dir / "prose" / "b-gate.md", "prose/b-gate", "prose")

        ids = resolve_gates.resolve_to_gate_ids(["prose"], gates_dir)
        assert ids == ["prose/a-gate", "prose/b-gate"]

    def test_mixed_bundles_and_ids(self, tmp_path: Path) -> None:
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        make_gate(gates_dir / "prose" / "a-gate.md", "prose/a-gate", "prose")
        make_gate(gates_dir / "semantic" / "b-gate.md", "semantic/b-gate", "semantic")

        ids = resolve_gates.resolve_to_gate_ids(["semantic/b-gate", "prose"], gates_dir)
        assert ids == ["semantic/b-gate", "prose/a-gate"]

    def test_review_path_includes_model(self, tmp_path: Path) -> None:
        path = resolve_gates.review_path_for(
            "kb/notes/backlinks.md",
            "prose/source-residue",
            "test-model",
        )
        assert path == "kb/reports/reviews/kb__notes__backlinks/prose__source-residue.test-model.md"

    def test_missing_gate_exits(self, tmp_path: Path) -> None:
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        gates_dir.mkdir(parents=True, exist_ok=True)

        with pytest.raises(SystemExit):
            resolve_gates.resolve_to_gate_ids(["prose/nonexistent"], gates_dir)
