from __future__ import annotations

import threading
import time
from pathlib import Path

import pytest

from commonplace.cli.review import review_sweep
from commonplace.review.review_target_selector import StaleGate
from commonplace.review.run_review_bundle import UsageExhausted


def make_fake_repo(tmp_path: Path) -> Path:
    repo = tmp_path / "repo"
    prose_dir = repo / "kb" / "instructions" / "review-gates" / "prose"
    prose_dir.mkdir(parents=True, exist_ok=True)
    (prose_dir / "source-residue.md").write_text("---\ntype: gate\n---\n\n# Source residue\n", encoding="utf-8")
    return repo


def test_review_sweep_aborts_immediately_on_usage_exhaustion(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    repo = make_fake_repo(tmp_path)
    monkeypatch.chdir(repo)
    monkeypatch.setenv("REVIEW_SWEEP_JOBS", "1")

    def fake_select_stale_gates(repo_root, *, model, gate_ids, note_filter=None, current_only=False, include_diff=False):
        return [
            StaleGate("kb/notes/first.md", "prose/source-residue", "missing-review"),
            StaleGate("kb/notes/second.md", "prose/source-residue", "missing-review"),
        ]

    calls: list[str] = []

    def fake_run_bundle(*, repo_root, db_path, note_path, gate_or_bundle, runner, model, dry_run):
        calls.append(note_path)
        raise UsageExhausted()

    monkeypatch.setattr(review_sweep, "select_stale_gates", fake_select_stale_gates)
    monkeypatch.setattr(review_sweep, "run_bundle", fake_run_bundle)

    exit_code = review_sweep.main(["--model", "test-model", "prose", "kb/notes"])
    stderr = capsys.readouterr().err

    assert exit_code == 1
    assert calls == ["kb/notes/first.md"]
    assert "aborting sweep immediately" in stderr


def test_review_sweep_passes_current_flag_to_selector(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = make_fake_repo(tmp_path)
    monkeypatch.chdir(repo)

    captured_kwargs: dict[str, object] = {}

    def fake_select_stale_gates(repo_root, **kwargs):
        captured_kwargs.update(kwargs)
        return []

    def fake_run_bundle(**kwargs):
        raise AssertionError("run_bundle should not be called when selector returns no stale pairs")

    monkeypatch.setattr(review_sweep, "select_stale_gates", fake_select_stale_gates)
    monkeypatch.setattr(review_sweep, "run_bundle", fake_run_bundle)

    exit_code = review_sweep.main(["--model", "test-model", "--current", "prose"])

    assert exit_code == 0
    assert captured_kwargs["current_only"] is True
    assert captured_kwargs["note_filter"] is None
    assert captured_kwargs["model"] == "test-model"
    assert captured_kwargs["gate_ids"] == ["prose/source-residue"]


def test_review_sweep_runs_up_to_four_reviews_in_parallel_by_default(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = make_fake_repo(tmp_path)
    monkeypatch.chdir(repo)

    def fake_select_stale_gates(repo_root, **kwargs):
        return [
            StaleGate(f"kb/notes/note-{idx}.md", "prose/source-residue", "missing-review")
            for idx in range(5)
        ]

    current_in_flight = 0
    max_in_flight = 0
    lock = threading.Lock()

    def fake_run_bundle(*, repo_root, db_path, note_path, gate_or_bundle, runner, model, dry_run):
        nonlocal current_in_flight, max_in_flight
        with lock:
            current_in_flight += 1
            if current_in_flight > max_in_flight:
                max_in_flight = current_in_flight
        time.sleep(0.1)
        with lock:
            current_in_flight -= 1
        return 0

    monkeypatch.setattr(review_sweep, "select_stale_gates", fake_select_stale_gates)
    monkeypatch.setattr(review_sweep, "run_bundle", fake_run_bundle)

    exit_code = review_sweep.main(["--model", "test-model", "prose", "kb/notes"])

    assert exit_code == 0
    assert max_in_flight >= 4


def test_review_sweep_passes_runner_to_run_review_bundle(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    repo = make_fake_repo(tmp_path)
    monkeypatch.chdir(repo)
    monkeypatch.setenv("REVIEW_SWEEP_JOBS", "1")

    def fake_select_stale_gates(repo_root, **kwargs):
        return [StaleGate("kb/notes/first.md", "prose/source-residue", "missing-review")]

    captured: dict[str, object] = {}

    def fake_run_bundle(**kwargs):
        captured.update(kwargs)
        return 0

    monkeypatch.setattr(review_sweep, "select_stale_gates", fake_select_stale_gates)
    monkeypatch.setattr(review_sweep, "run_bundle", fake_run_bundle)

    exit_code = review_sweep.main(["--model", "test-model", "--runner", "codex", "--current", "prose"])

    assert exit_code == 0
    assert captured["runner"] == "codex"
    assert captured["model"] == "test-model"
    assert captured["note_path"] == "kb/notes/first.md"
    assert captured["gate_or_bundle"] == ["prose/source-residue"]
    assert captured["dry_run"] is False
