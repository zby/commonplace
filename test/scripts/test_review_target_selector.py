from __future__ import annotations

import importlib.util
import json
import os
import sqlite3
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


review_target_selector = load_module(
    "review_target_selector",
    SCRIPTS_DIR / "review_target_selector.py",
)
resolve_gates = load_module("resolve_gates", SCRIPTS_DIR / "resolve_gates.py")
review_db = load_module("review_db_review_target_selector_test", SCRIPTS_DIR / "review_db.py")
review_metadata = load_module("review_metadata", SCRIPTS_DIR / "review_metadata.py")


def db_path_for(repo_root: Path) -> Path:
    return repo_root / "kb" / "reports" / "review-store.sqlite"


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def make_note(path: Path, title: str, body: str, *, status: str = "current") -> Path:
    return write(
        path,
        f"""---
description: Test note
type: note
traits: []
status: {status}
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

    review_db.ensure_db(tmp_path, db_path_for(tmp_path))
    reviewed_at = "2026-03-31T00:00:00+00:00"
    with review_db.connect(db_path_for(tmp_path)) as conn:
        for gate_id, gate_sha in [
            ("prose/source-residue", g1_sha),
            ("prose/confidence-miscalibration", g2_sha),
            ("semantic/grounding-alignment", g3_sha),
        ]:
            review_id = review_db.insert_gate_review(
                conn,
                note_path="kb/notes/stable.md",
                gate_id=gate_id,
                model_id=TEST_MODEL,
                decision="pass",
                rationale_markdown="Looks good.\n\n## Result: PASS\n",
                evidence_json=None,
                gate_sha=gate_sha,
                reviewed_note_sha=stable_sha,
                reviewed_note_commit=commit,
                reviewed_at=reviewed_at,
                review_kind="full-review",
            )
            review_db.append_acceptance_event(
                conn,
                note_path="kb/notes/stable.md",
                gate_id=gate_id,
                model_id=TEST_MODEL,
                accepted_review_id=review_id,
                accepted_note_sha=stable_sha,
                accepted_note_commit=commit,
                accepted_gate_sha=gate_sha,
                accepted_at=reviewed_at,
                acceptance_kind="full-review",
            )
        conn.commit()

    return {
        "stable": stable,
        "unreviewed": unreviewed,
        "gate_prose_sr": g1,
        "gate_prose_cm": g2,
        "gate_semantic_ga": g3,
        "commit": commit,
    }


class TestMissingReview:
    def test_missing_review_marks_stale(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_gates(
            tmp_path,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/unreviewed.md"],
        )
        assert [(s.gate_id, s.reason) for s in stale] == [
            ("prose/confidence-miscalibration", "missing-review"),
            ("prose/source-residue", "missing-review"),
        ]

    def test_all_gates_finds_missing_across_bundles(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_gates(
            tmp_path,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue", "semantic/grounding-alignment"],
            note_filter=["kb/notes/unreviewed.md"],
        )
        gate_ids = [s.gate_id for s in stale]
        assert "prose/source-residue" in gate_ids
        assert "semantic/grounding-alignment" in gate_ids

    def test_current_filter_limits_selection_to_current_notes(self, tmp_path: Path) -> None:
        init_repo(tmp_path)
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        make_note(notes_dir / "current-top.md", "Current top", "\nBody.\n", status="current")
        make_note(notes_dir / "archived.md", "Archived", "\nBody.\n", status="archived")
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            gate_ids=["prose/source-residue"],
            current_only=True,
        )

        assert [record.note_path for record in stale] == [
            "kb/notes/current-top.md",
        ]


class TestFreshReview:
    def test_review_with_matching_metadata_is_fresh(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_gates(
            tmp_path,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
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

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
        )
        assert [(s.gate_id, s.reason) for s in stale] == [
            ("prose/source-residue", "gate-changed"),
        ]


class TestNoteChanged:
    def test_note_sha_change_marks_stale(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        make_note(fixture["stable"], "Stable title", "\nUpdated line.\n")

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
        )
        assert [(s.gate_id, s.reason) for s in stale] == [
            ("prose/confidence-miscalibration", "note-changed"),
            ("prose/source-residue", "note-changed"),
        ]


class TestAckMetadata:
    def test_ack_appends_acceptance_event_without_creating_new_gate_reviews(self, tmp_path: Path) -> None:
        fixture = build_fixture(tmp_path)
        make_note(fixture["stable"], "Stable title", "\nUpdated line.\n")

        with sqlite3.connect(db_path_for(tmp_path)) as conn:
            gate_review_count_before = conn.execute("SELECT count(*) FROM gate_reviews").fetchone()[0]

        stale_before = review_target_selector.select_stale_gates(
            tmp_path,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
        )
        assert len(stale_before) == 2

        review_target_selector.ack_pairs(
            tmp_path,
            [
                "kb/notes/stable.md:prose/source-residue",
                "kb/notes/stable.md:prose/confidence-miscalibration",
            ],
            TEST_MODEL,
        )

        stale_after = review_target_selector.select_stale_gates(
            tmp_path,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/stable.md"],
        )
        assert stale_after == []

        with sqlite3.connect(db_path_for(tmp_path)) as conn:
            conn.row_factory = sqlite3.Row
            gate_review_count_after = conn.execute("SELECT count(*) FROM gate_reviews").fetchone()[0]
            row = conn.execute(
                """
                SELECT accepted_review_id, accepted_note_sha, acceptance_kind
                FROM current_gate_acceptances
                WHERE note_path = ? AND gate_id = ? AND model_id = ?
                """,
                ("kb/notes/stable.md", "prose/source-residue", TEST_MODEL),
            ).fetchone()
        assert row is not None
        assert gate_review_count_after == gate_review_count_before
        assert row["accepted_review_id"] is None
        assert row["acceptance_kind"] == "trivial-change-ack"
        assert row["accepted_note_sha"] == review_metadata.git_blob_sha(fixture["stable"])

    def test_ack_does_not_create_review_file_when_missing(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale_before = review_target_selector.select_stale_gates(
            tmp_path,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/unreviewed.md"],
        )
        assert len(stale_before) == 2

        review_target_selector.ack_pairs(
            tmp_path,
            [
                "kb/notes/unreviewed.md:prose/confidence-miscalibration",
                "kb/notes/unreviewed.md:prose/source-residue",
            ],
            TEST_MODEL,
        )

        stale_after = review_target_selector.select_stale_gates(
            tmp_path,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/unreviewed.md"],
        )
        assert stale_after == []

        with sqlite3.connect(db_path_for(tmp_path)) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                """
                SELECT accepted_review_id, acceptance_kind
                FROM current_gate_acceptances
                WHERE note_path = ? AND gate_id = ? AND model_id = ?
                """,
                ("kb/notes/unreviewed.md", "prose/source-residue", TEST_MODEL),
            ).fetchone()
        assert row is not None
        assert row["accepted_review_id"] is None
        assert row["acceptance_kind"] == "trivial-change-ack"


class TestDiffGeneration:
    def test_note_changed_includes_diff_in_json_mode(self, tmp_path: Path) -> None:
        init_repo(tmp_path)
        notes_dir = tmp_path / "kb" / "notes"
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"

        note_path = make_note(notes_dir / "target.md", "Target", "\nOriginal line.\n")
        gate_path = make_gate(gates_dir / "prose" / "test-gate.md", "prose/test-gate", "prose")
        commit = commit_all(tmp_path, "Initial", date="2020-01-01T00:00:00+00:00")

        review_db.ensure_db(tmp_path, db_path_for(tmp_path))
        note_sha = review_metadata.git_blob_sha(note_path, write_object=True)
        gate_sha = review_metadata.git_blob_sha(gate_path, write_object=True)
        with review_db.connect(db_path_for(tmp_path)) as conn:
            review_id = review_db.insert_gate_review(
                conn,
                note_path="kb/notes/target.md",
                gate_id="prose/test-gate",
                model_id=TEST_MODEL,
                decision="pass",
                rationale_markdown="Looks good.\n\n## Result: PASS\n",
                evidence_json=None,
                gate_sha=gate_sha,
                reviewed_note_sha=note_sha,
                reviewed_note_commit=commit,
                reviewed_at="2026-03-31T00:00:00+00:00",
                review_kind="full-review",
            )
            review_db.append_acceptance_event(
                conn,
                note_path="kb/notes/target.md",
                gate_id="prose/test-gate",
                model_id=TEST_MODEL,
                accepted_review_id=review_id,
                accepted_note_sha=note_sha,
                accepted_note_commit=commit,
                accepted_gate_sha=gate_sha,
                accepted_at="2026-03-31T00:00:00+00:00",
                acceptance_kind="full-review",
            )
            conn.commit()

        make_note(note_path, "Target", "\nUpdated line.\n")

        stale = review_target_selector.select_stale_gates(
            tmp_path,
            gate_ids=["prose/test-gate"],
            note_filter=["kb/notes/target.md"],
            include_diff=True,
        )
        assert len(stale) == 1
        assert stale[0].reason == "note-changed"
        assert stale[0].diff is not None
        assert "Updated line" in stale[0].diff


class TestJsonOutput:
    def test_json_output_omits_review_path(self, tmp_path: Path) -> None:
        build_fixture(tmp_path)
        stale = review_target_selector.select_stale_gates(
            tmp_path,
            gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
            note_filter=["kb/notes/unreviewed.md"],
        )
        json_str = review_target_selector.render_json(stale)
        items = json.loads(json_str)
        assert len(items) == 2
        for item in items:
            assert "review_path" not in item


class TestModelRequired:
    def test_selector_requires_review_model_env(self, tmp_path: Path, monkeypatch) -> None:
        build_fixture(tmp_path)
        monkeypatch.delenv("COMMONPLACE_REVIEW_MODEL", raising=False)

        with pytest.raises(ValueError, match="COMMONPLACE_REVIEW_MODEL is not set"):
            review_target_selector.select_stale_gates(
                tmp_path,
                gate_ids=["prose/confidence-miscalibration", "prose/source-residue"],
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

    def test_cli_output_includes_gate_header_without_path(self, tmp_path: Path) -> None:
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")

        result = subprocess.run(
            [sys.executable, str(SCRIPTS_DIR / "resolve_gates.py"), "prose/source-residue"],
            cwd=tmp_path,
            check=True,
            capture_output=True,
            text=True,
        )

        assert "=== gate: prose/source-residue ===" in result.stdout
        assert "path:" not in result.stdout

    def test_missing_gate_exits(self, tmp_path: Path) -> None:
        gates_dir = tmp_path / "kb" / "instructions" / "review-gates"
        gates_dir.mkdir(parents=True, exist_ok=True)

        with pytest.raises(SystemExit):
            resolve_gates.resolve_to_gate_ids(["prose/nonexistent"], gates_dir)
