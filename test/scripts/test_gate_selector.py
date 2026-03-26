from __future__ import annotations

import importlib.util
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


frontmatter = load_module("frontmatter", SCRIPTS_DIR / "frontmatter.py")
review_metadata = load_module("review_metadata", SCRIPTS_DIR / "review_metadata.py")
review_state = load_module("review_state", SCRIPTS_DIR / "review_state.py")
gate_core = load_module("gate_core", SCRIPTS_DIR / "gate_core.py")
gate_reviews = load_module("gate_reviews", SCRIPTS_DIR / "gate_reviews.py")
gate_selector = load_module("gate_selector", SCRIPTS_DIR / "gate_selector.py")
ack_gate_review = load_module("ack_gate_review", SCRIPTS_DIR / "ack_gate_review.py")


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def note(path: Path, title: str, body: str) -> Path:
    return write(
        path,
        f"""---
description: Test note description with enough discrimination to be reviewable in batch workflows
type: note
traits: []
status: current
---

# {title}
{body}
""",
    )


def gate(path: Path, gate_id: str, lens: str, watches: str, staleness: str) -> Path:
    return write(
        path,
        f"""---
gate_id: {gate_id}
name: {path.stem.replace("-", " ").title()}
lens: {lens}
watches: {watches}
staleness: {staleness}
---

## Failure mode

Fixture gate.

## Test

Fixture test.
""",
    )


def bundle(path: Path, title: str, gate_ids: list[str]) -> Path:
    gate_lines = "\n".join(f"- {gate_id}" for gate_id in gate_ids)
    return write(
        path,
        f"""# {title}

## Purpose

Fixture bundle.

## Gates

{gate_lines}

## Output format

Fixture output.
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


def commit_all(path: Path, message: str) -> str:
    subprocess.run(["git", "add", "."], cwd=path, check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", message],
        cwd=path,
        check=True,
        capture_output=True,
    )
    result = subprocess.run(
        ["git", "rev-parse", "HEAD"],
        cwd=path,
        check=True,
        capture_output=True,
        text=True,
    )
    return result.stdout.strip()


def record_gate(repo_root: Path, note_path: Path, gate_id: str, recorded_commit: str) -> None:
    gate_def = gate_core.load_gate_definition(
        repo_root / "kb" / "instructions" / "review-gates",
        gate_id,
    )
    note_regions = gate_core.load_note_regions(note_path, repo_root)
    watched_hash = gate_core.compute_watched_hash(
        note_regions,
        gate_def.watches if gate_def.staleness.mode == "changed" else gate_core.non_body_watches(gate_def),
    )
    gate_reviews.write_recorded_gate_review(
        repo_root,
        note_path=note_path.relative_to(repo_root).as_posix(),
        gate_id=gate_id,
        model=TEST_MODEL,
        gate_hash=review_metadata.git_blob_sha(gate_def.path),
        recorded_commit=recorded_commit,
        watched_hash=watched_hash,
        review_body=f"## {gate_id}\n\nCLEAN\n",
    )


def build_fixture_repo(tmp_path: Path) -> dict[str, Path | str]:
    init_repo(tmp_path)
    notes_root = tmp_path / "kb" / "notes"
    gates_root = tmp_path / "kb" / "instructions" / "review-gates"
    bundles_root = tmp_path / "kb" / "instructions" / "review-bundles"

    stable = note(notes_root / "stable.md", "Stable title", "\nLine 1.\nLine 2.\n")
    rewrite = note(
        notes_root / "rewrite.md",
        "Rewrite title",
        "\nLine 1.\nLine 2.\nLine 3.\nLine 4.\n",
    )
    unreviewed = note(notes_root / "unreviewed.md", "Unreviewed title", "\nBody.\n")

    gate(
        gates_root / "frontmatter" / "title-composability.md",
        "frontmatter/title-composability",
        "frontmatter",
        "[title]",
        "changed",
    )
    gate(
        gates_root / "frontmatter" / "title-body-alignment.md",
        "frontmatter/title-body-alignment",
        "frontmatter",
        "[title, body]",
        "rewrite(0.5)",
    )
    gate(
        gates_root / "prose" / "source-residue.md",
        "prose/source-residue",
        "prose",
        "[body]",
        "changed",
    )

    bundle(
        bundles_root / "frontmatter-review.md",
        "Frontmatter Review",
        [
            "frontmatter/title-composability",
            "frontmatter/title-body-alignment",
        ],
    )
    bundle(
        bundles_root / "prose-review.md",
        "Prose Review",
        ["prose/source-residue"],
    )

    initial_commit = commit_all(tmp_path, "Initial notes and gate definitions")

    record_gate(tmp_path, stable, "frontmatter/title-composability", initial_commit)
    record_gate(tmp_path, stable, "frontmatter/title-body-alignment", initial_commit)
    record_gate(tmp_path, stable, "prose/source-residue", initial_commit)
    record_gate(tmp_path, rewrite, "frontmatter/title-body-alignment", initial_commit)
    record_gate(tmp_path, rewrite, "frontmatter/title-composability", initial_commit)

    reviews_commit = commit_all(tmp_path, "Store recorded gate reviews")

    return {
        "repo_root": tmp_path,
        "stable": stable,
        "rewrite": rewrite,
        "unreviewed": unreviewed,
        "initial_commit": initial_commit,
        "reviews_commit": reviews_commit,
    }


def test_missing_review_marks_each_gate_stale(tmp_path: Path) -> None:
    fixture = build_fixture_repo(tmp_path)
    stale = gate_selector.select_stale_gates(
        fixture["repo_root"],
        bundle_id="frontmatter-review",
        raw_note_paths=["kb/notes/unreviewed.md"],
    )

    assert [(item.gate_id, item.reason) for item in stale] == [
        ("frontmatter/title-body-alignment", "missing-review"),
        ("frontmatter/title-composability", "missing-review"),
    ]


def test_canonical_gate_review_path_uses_model_key(tmp_path: Path) -> None:
    review_path = gate_reviews.canonical_gate_review_path(
        tmp_path,
        note_path="kb/notes/backlinks.md",
        gate_id="semantic/internal-consistency",
    )

    assert review_path == (
        tmp_path
        / "kb"
        / "reports"
        / "reviews"
        / "kb__notes__backlinks"
        / "semantic__internal-consistency.test-model.md"
    )


def test_gate_file_change_invalidates_existing_acceptance(tmp_path: Path) -> None:
    fixture = build_fixture_repo(tmp_path)
    repo_root = fixture["repo_root"]
    gate_path = repo_root / "kb" / "instructions" / "review-gates" / "frontmatter" / "title-composability.md"
    gate_path.write_text(
        gate_path.read_text(encoding="utf-8") + "\n## Example\n\nChanged gate wording.\n",
        encoding="utf-8",
    )

    stale = gate_selector.select_stale_gates(
        repo_root,
        bundle_id="frontmatter-review",
        raw_note_paths=["kb/notes/stable.md"],
    )

    assert [(item.gate_id, item.reason) for item in stale] == [
        ("frontmatter/title-composability", "gate-changed"),
    ]


def test_watched_hash_change_marks_changed_gate_stale(tmp_path: Path) -> None:
    fixture = build_fixture_repo(tmp_path)
    stable = fixture["stable"]
    note(stable, "Updated title", "\nLine 1.\nLine 2.\n")

    stale = gate_selector.select_stale_gates(
        fixture["repo_root"],
        bundle_id="frontmatter-review",
        raw_note_paths=["kb/notes/stable.md"],
    )

    assert [(item.gate_id, item.reason) for item in stale] == [
        ("frontmatter/title-body-alignment", "watched-changed"),
        ("frontmatter/title-composability", "watched-changed"),
    ]


def test_rewrite_threshold_allows_exact_half_body_change(tmp_path: Path) -> None:
    fixture = build_fixture_repo(tmp_path)
    rewrite = fixture["rewrite"]
    note(
        rewrite,
        "Rewrite title",
        "\nLine 1.\nLine 2.\nNew 3.\nNew 4.\n",
    )

    stale = gate_selector.select_stale_gates(
        fixture["repo_root"],
        bundle_id="frontmatter-review",
        raw_note_paths=["kb/notes/rewrite.md"],
    )

    assert stale == []


def test_rewrite_threshold_marks_major_body_rewrite_stale(tmp_path: Path) -> None:
    fixture = build_fixture_repo(tmp_path)
    rewrite = fixture["rewrite"]
    note(
        rewrite,
        "Rewrite title",
        "\nNew 1.\nNew 2.\nNew 3.\nNew 4.\n",
    )

    stale = gate_selector.select_stale_gates(
        fixture["repo_root"],
        bundle_id="frontmatter-review",
        raw_note_paths=["kb/notes/rewrite.md"],
    )

    assert [(item.gate_id, item.reason) for item in stale] == [
        ("frontmatter/title-body-alignment", "body-rewrite"),
    ]


def test_unchanged_note_outside_git_diff_set_is_fresh(tmp_path: Path) -> None:
    fixture = build_fixture_repo(tmp_path)
    stale = gate_selector.select_stale_gates(
        fixture["repo_root"],
        bundle_id="frontmatter-review",
        raw_note_paths=["kb/notes/stable.md"],
    )

    assert stale == []


def test_finalize_gate_review_round_trip_restores_freshness(tmp_path: Path) -> None:
    fixture = build_fixture_repo(tmp_path)
    repo_root = fixture["repo_root"]
    stable = fixture["stable"]
    note(stable, "Stable title", "\nUpdated line 1.\nUpdated line 2.\n")
    commit_all(repo_root, "Update stable note")

    review_path = gate_reviews.gate_review_path_for(
        "kb/notes/stable.md",
        "prose/source-residue",
        TEST_MODEL,
        repo_root / "kb" / "reports" / "reviews",
    )
    write(
        review_path,
        "## prose/source-residue\n\nCLEAN\n",
    )

    gate_reviews.finalize_gate_review(
        repo_root,
        note_path="kb/notes/stable.md",
        gate_id="prose/source-residue",
    )

    csv_path = repo_root / "kb" / "reports" / "review-csv" / "gate_reviews.csv"
    csv_path.unlink()
    gate_reviews.rebuild_gate_review_index(
        repo_root / "kb" / "reports" / "reviews",
        csv_path,
    )

    stale = gate_selector.select_stale_gates(
        repo_root,
        bundle_id="prose-review",
        raw_note_paths=["kb/notes/stable.md"],
    )

    assert stale == []


def test_ack_gate_review_advances_recorded_baseline_without_rewriting_body(
    tmp_path: Path,
    monkeypatch,
) -> None:
    fixture = build_fixture_repo(tmp_path)
    repo_root = fixture["repo_root"]
    stable = fixture["stable"]
    note(
        stable,
        "Stable title",
        "\nLine 1.\nLine 2.\nTrivial extra sentence.\n",
    )
    new_commit = commit_all(repo_root, "Trivial prose change")

    stale_before = gate_selector.select_stale_gates(
        repo_root,
        bundle_id="prose-review",
        raw_note_paths=["kb/notes/stable.md"],
    )
    assert [(item.gate_id, item.reason) for item in stale_before] == [
        ("prose/source-residue", "watched-changed"),
    ]

    review_path = gate_reviews.gate_review_path_for(
        "kb/notes/stable.md",
        "prose/source-residue",
        TEST_MODEL,
        repo_root / "kb" / "reports" / "reviews",
    )
    original_text = review_path.read_text(encoding="utf-8")
    original_body = gate_reviews.strip_gate_review_metadata(original_text).lstrip("\n")

    monkeypatch.chdir(repo_root)
    old_argv = sys.argv
    sys.argv = [
        "ack_gate_review.py",
        "kb/notes/stable.md",
        "prose/source-residue",
    ]
    try:
        ack_gate_review.main()
    finally:
        sys.argv = old_argv

    updated_text = review_path.read_text(encoding="utf-8")
    updated_metadata = gate_reviews.parse_gate_review_metadata(updated_text)
    assert updated_metadata is not None
    assert updated_metadata.recorded_commit == new_commit
    assert gate_reviews.strip_gate_review_metadata(updated_text).lstrip("\n") == original_body

    stale_after = gate_selector.select_stale_gates(
        repo_root,
        bundle_id="prose-review",
        raw_note_paths=["kb/notes/stable.md"],
    )
    assert stale_after == []


def test_ack_gate_review_can_update_multiple_gates_for_one_note(
    tmp_path: Path,
    monkeypatch,
) -> None:
    fixture = build_fixture_repo(tmp_path)
    repo_root = fixture["repo_root"]
    stable = fixture["stable"]
    note(
        stable,
        "Updated title",
        "\nLine 1.\nLine 2.\n",
    )
    new_commit = commit_all(repo_root, "Trivial frontmatter change")

    stale_before = gate_selector.select_stale_gates(
        repo_root,
        bundle_id="frontmatter-review",
        raw_note_paths=["kb/notes/stable.md"],
    )
    assert [(item.gate_id, item.reason) for item in stale_before] == [
        ("frontmatter/title-body-alignment", "watched-changed"),
        ("frontmatter/title-composability", "watched-changed"),
    ]

    monkeypatch.chdir(repo_root)
    old_argv = sys.argv
    sys.argv = [
        "ack_gate_review.py",
        "kb/notes/stable.md",
        "frontmatter/title-body-alignment",
        "frontmatter/title-composability",
    ]
    try:
        ack_gate_review.main()
    finally:
        sys.argv = old_argv

    for gate_id in [
        "frontmatter/title-body-alignment",
        "frontmatter/title-composability",
    ]:
        review_path = gate_reviews.gate_review_path_for(
            "kb/notes/stable.md",
            gate_id,
            TEST_MODEL,
            repo_root / "kb" / "reports" / "reviews",
        )
        metadata = gate_reviews.parse_gate_review_metadata(
            review_path.read_text(encoding="utf-8")
        )
        assert metadata is not None
        assert metadata.recorded_commit == new_commit


def test_selector_requires_review_model_env(tmp_path: Path, monkeypatch) -> None:
    fixture = build_fixture_repo(tmp_path)
    monkeypatch.delenv("COMMONPLACE_REVIEW_MODEL", raising=False)

    with pytest.raises(ValueError, match="COMMONPLACE_REVIEW_MODEL must be set"):
        gate_selector.select_stale_gates(
            fixture["repo_root"],
            bundle_id="frontmatter-review",
            raw_note_paths=["kb/notes/stable.md"],
        )
