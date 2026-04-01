from __future__ import annotations

import importlib.util
import os
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
WORKSHOP_DIR = REPO_ROOT / "kb" / "work" / "review-db-migration" / "draft-scripts"
SCRIPTS_DIR = REPO_ROOT / "scripts"

if str(WORKSHOP_DIR) not in sys.path:
    sys.path.insert(0, str(WORKSHOP_DIR))
if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


select_stale_reviews = load_module(
    "workshop_select_stale_reviews",
    WORKSHOP_DIR / "select_stale_reviews.py",
)
review_db = load_module(
    "workshop_review_db",
    WORKSHOP_DIR / "review_db.py",
)
import_legacy_reviews = load_module(
    "workshop_import_legacy_reviews",
    WORKSHOP_DIR / "import_legacy_reviews.py",
)
render_review = load_module(
    "workshop_render_review",
    WORKSHOP_DIR / "render_review.py",
)
ack_review = load_module(
    "workshop_ack_review",
    WORKSHOP_DIR / "ack_review.py",
)
gate_selector = load_module(
    "current_gate_selector",
    REPO_ROOT / "scripts" / "gate_selector.py",
)
review_metadata = load_module(
    "current_review_metadata",
    REPO_ROOT / "scripts" / "review_metadata.py",
)


def build_fixture_db(tmp_path: Path) -> Path:
    db_path = tmp_path / "review-store-test.sqlite"
    subprocess.run(
        [
            "python3",
            str(WORKSHOP_DIR / "build_test_db.py"),
            "--output",
            str(db_path),
        ],
        cwd=REPO_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return db_path


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
    model_id: str,
    last_full_review_note_sha: str | None = None,
    last_full_review_note_commit: str | None = None,
    last_full_review_at: str | None = None,
    last_acceptance_kind: str = "full-review",
) -> Path:
    body = "**pass** Imported fixture review.\n"
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
    filename = f"{gate_selector.encode_gate_id(gate_id)}.{model_id}.md"
    return write(path / filename, review_metadata.inject_review_metadata(body, metadata))


def init_repo(path: Path) -> None:
    subprocess.run(["git", "init"], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.name", "Test User"], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "config", "user.email", "test@example.com"], cwd=path, check=True, capture_output=True)


def commit_all(path: Path, message: str) -> str:
    subprocess.run(["git", "add", "."], cwd=path, check=True, capture_output=True)
    subprocess.run(["git", "commit", "-m", message], cwd=path, check=True, capture_output=True)
    result = subprocess.run(["git", "rev-parse", "HEAD"], cwd=path, check=True, capture_output=True, text=True)
    return result.stdout.strip()


def build_repo_fixture(tmp_path: Path) -> tuple[Path, Path]:
    repo = tmp_path / "repo"
    repo.mkdir()
    init_repo(repo)

    notes_dir = repo / "kb" / "notes"
    gates_dir = repo / "kb" / "instructions" / "review-gates"
    reviews_dir = repo / "kb" / "reports" / "reviews"

    stable = make_note(notes_dir / "stable.md", "Stable title", "\nLine 1.\nLine 2.\n")
    changed = make_note(notes_dir / "changed.md", "Changed title", "\nOld line.\n")
    make_gate(gates_dir / "prose" / "source-residue.md", "prose/source-residue", "prose")
    make_gate(gates_dir / "semantic" / "grounding-alignment.md", "semantic/grounding-alignment", "semantic")
    commit = commit_all(repo, "Initial fixture")

    stable_sha = review_metadata.git_blob_sha(stable, write_object=True)
    changed_sha = review_metadata.git_blob_sha(changed, write_object=True)
    prose_sha = review_metadata.git_blob_sha(gates_dir / "prose" / "source-residue.md")
    semantic_sha = review_metadata.git_blob_sha(gates_dir / "semantic" / "grounding-alignment.md")

    stable_review_dir = reviews_dir / "kb__notes__stable"
    changed_review_dir = reviews_dir / "kb__notes__changed"
    make_review(
        stable_review_dir,
        note_path="kb/notes/stable.md",
        gate_id="prose/source-residue",
        note_sha=stable_sha,
        note_commit=commit,
        gate_fingerprint=prose_sha,
        model_id="test-model",
    )
    make_review(
        changed_review_dir,
        note_path="kb/notes/changed.md",
        gate_id="semantic/grounding-alignment",
        note_sha=changed_sha,
        note_commit=commit,
        gate_fingerprint=semantic_sha,
        model_id="test-model",
    )
    commit_all(repo, "Add reviews")

    make_note(notes_dir / "changed.md", "Changed title", "\nNew line.\n")
    commit_all(repo, "Update changed note")

    db_path = repo / "tmp" / "review-store.sqlite"
    review_db.init_db(db_path, REPO_ROOT / "kb" / "work" / "review-db-migration" / "schema.sql")
    return repo, db_path


def test_classify_candidates_uses_latest_acceptance_event(tmp_path: Path) -> None:
    db_path = build_fixture_db(tmp_path)
    candidates = [
        select_stale_reviews.CandidateState(
            note_path="kb/notes/fresh.md",
            gate_id="prose/source-residue",
            model_id="opus-4-6",
            current_note_sha="note-fresh-v1",
            current_gate_sha="gate-prose-source-residue-v1",
        ),
        select_stale_reviews.CandidateState(
            note_path="kb/notes/note-changed.md",
            gate_id="semantic/internal-consistency",
            model_id="opus-4-6",
            current_note_sha="note-note-changed-v2",
            current_gate_sha="gate-semantic-internal-consistency-v1",
        ),
        select_stale_reviews.CandidateState(
            note_path="kb/notes/gate-changed.md",
            gate_id="frontmatter/title-body-alignment",
            model_id="opus-4-6",
            current_note_sha="note-gate-changed-v1",
            current_gate_sha="gate-frontmatter-title-body-alignment-v2",
        ),
        select_stale_reviews.CandidateState(
            note_path="kb/notes/acked.md",
            gate_id="complexity/framework-decoration",
            model_id="opus-4-6",
            current_note_sha="note-acked-v2",
            current_gate_sha="gate-complexity-framework-decoration-v1",
        ),
        select_stale_reviews.CandidateState(
            note_path="kb/notes/model-split.md",
            gate_id="sentence/clause-packing",
            model_id="opus-4-6",
            current_note_sha="note-model-split-v1",
            current_gate_sha="gate-sentence-clause-packing-v1",
        ),
        select_stale_reviews.CandidateState(
            note_path="kb/notes/model-split.md",
            gate_id="sentence/clause-packing",
            model_id="gpt-5.4",
            current_note_sha="note-model-split-v2",
            current_gate_sha="gate-sentence-clause-packing-v1",
        ),
        select_stale_reviews.CandidateState(
            note_path="kb/notes/missing-review.md",
            gate_id="prose/source-residue",
            model_id="opus-4-6",
            current_note_sha="note-missing-review-v1",
            current_gate_sha="gate-prose-source-residue-v1",
        ),
    ]

    stale = select_stale_reviews.classify_candidates(db_path, candidates)
    assert [(item.note_path, item.gate_id, item.model_id, item.reason) for item in stale] == [
        (
            "kb/notes/note-changed.md",
            "semantic/internal-consistency",
            "opus-4-6",
            "note-changed",
        ),
        (
            "kb/notes/gate-changed.md",
            "frontmatter/title-body-alignment",
            "opus-4-6",
            "gate-changed",
        ),
        (
            "kb/notes/missing-review.md",
            "prose/source-residue",
            "opus-4-6",
            "missing-review",
        ),
    ]


def test_model_id_partitions_acceptance_state(tmp_path: Path) -> None:
    db_path = build_fixture_db(tmp_path)
    candidates = [
        select_stale_reviews.CandidateState(
            note_path="kb/notes/model-split.md",
            gate_id="sentence/clause-packing",
            model_id="opus-4-6",
            current_note_sha="note-model-split-v2",
            current_gate_sha="gate-sentence-clause-packing-v1",
        ),
        select_stale_reviews.CandidateState(
            note_path="kb/notes/model-split.md",
            gate_id="sentence/clause-packing",
            model_id="gpt-5.4",
            current_note_sha="note-model-split-v2",
            current_gate_sha="gate-sentence-clause-packing-v1",
        ),
    ]

    stale = select_stale_reviews.classify_candidates(db_path, candidates)
    assert [(item.model_id, item.reason) for item in stale] == [
        ("opus-4-6", "note-changed"),
    ]


def test_legacy_import_and_selector_parity_on_fixture_repo(tmp_path: Path, monkeypatch) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    imported, skipped = import_legacy_reviews.import_review_tree(
        repo,
        db_path,
        repo / "kb" / "reports" / "reviews",
    )
    assert imported == 2
    assert skipped == 0

    monkeypatch.setenv("COMMONPLACE_REVIEW_MODEL", "test-model")
    file_stale = gate_selector.select_stale_gates(
        repo,
        include_all=True,
        note_filter=["kb/notes/stable.md", "kb/notes/changed.md"],
    )
    db_stale = select_stale_reviews.select_stale_gates(
        repo,
        db_path=db_path,
        include_all=True,
        note_filter=["kb/notes/stable.md", "kb/notes/changed.md"],
    )

    assert [(item.note_path, item.gate_id, item.reason) for item in db_stale] == [
        (item.note_path, item.gate_id, item.reason) for item in file_stale
    ]


def test_legacy_import_is_idempotent(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    import_legacy_reviews.import_review_tree(
        repo,
        db_path,
        repo / "kb" / "reports" / "reviews",
    )
    import_legacy_reviews.import_review_tree(
        repo,
        db_path,
        repo / "kb" / "reports" / "reviews",
    )
    with review_db.connect(db_path) as conn:
        gate_reviews_count = conn.execute("select count(*) from gate_reviews").fetchone()[0]
        acceptance_events_count = conn.execute("select count(*) from acceptance_events").fetchone()[0]
    assert gate_reviews_count == 2
    assert acceptance_events_count == 2


def test_ack_appends_acceptance_event_and_render_uses_latest_state(tmp_path: Path, monkeypatch) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    import_legacy_reviews.import_review_tree(
        repo,
        db_path,
        repo / "kb" / "reports" / "reviews",
    )
    monkeypatch.setenv("COMMONPLACE_REVIEW_MODEL", "test-model")
    monkeypatch.setenv("COMMONPLACE_REVIEW_DB", str(db_path))

    ack_review.ack_pairs(
        repo,
        db_path,
        ["kb/notes/changed.md:semantic/grounding-alignment"],
        "test-model",
    )

    db_stale = select_stale_reviews.select_stale_gates(
        repo,
        db_path=db_path,
        include_all=True,
        note_filter=["kb/notes/changed.md"],
    )
    assert [(item.gate_id, item.reason) for item in db_stale] == [
        ("prose/source-residue", "missing-review"),
    ]

    rendered = render_review.render_note_reviews(
        db_path,
        note_path="kb/notes/changed.md",
        model_id="test-model",
    )
    assert "semantic/grounding-alignment" in rendered
    assert "acceptance_kind: trivial-change-ack" in rendered


def test_legacy_import_falls_back_for_body_only_review(tmp_path: Path) -> None:
    repo, db_path = build_repo_fixture(tmp_path)
    body_only = repo / "kb" / "reports" / "reviews" / "kb__notes__stable" / "semantic__grounding-alignment.test-model.md"
    write(body_only, "**pass** Legacy body-only review.\n")

    imported, skipped = import_legacy_reviews.import_review_tree(
        repo,
        db_path,
        repo / "kb" / "reports" / "reviews",
    )

    assert imported == 3
    assert skipped == 0

    with review_db.connect(db_path) as conn:
        rows = conn.execute(
            """
            select note_path, gate_id, model_id, review_kind
            from gate_reviews
            where note_path = 'kb/notes/stable.md'
            order by gate_id
            """
        ).fetchall()
        acceptances = review_db.load_current_acceptances(conn)

    assert [(row["gate_id"], row["review_kind"]) for row in rows] == [
        ("prose/source-residue", "manual-import"),
        ("semantic/grounding-alignment", "manual-import"),
    ]
    acceptance = acceptances[("kb/notes/stable.md", "semantic/grounding-alignment", "test-model")]
    assert acceptance.acceptance_kind == "migration-import"
