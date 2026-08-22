from __future__ import annotations

import json
import sys
from pathlib import Path

import yaml


SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.cli import github_snapshot  # noqa: E402
from commonplace.lib.snapshot import snapshot_sha256  # noqa: E402


def frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    raw = content.split("---", 2)[1]
    return yaml.safe_load(raw)


def test_github_snapshot_stamps_snapshot_issue_family(
    tmp_path: Path, monkeypatch
) -> None:
    payload = {
        "title": "Issue title",
        "number": 123,
        "state": "open",
        "repository_url": "https://api.github.com/repos/example/project",
        "user": {"login": "alice"},
        "labels": [{"name": "bug"}],
        "body": "Issue body",
    }
    monkeypatch.setattr(github_snapshot, "_gh_api", lambda _url: json.dumps(payload))

    result = github_snapshot.snapshot_github_url(
        "https://github.com/example/project/issues/123",
        out_dir=str(tmp_path),
    )

    md_path = next(tmp_path.glob("*.md"))
    fm = frontmatter(md_path)

    assert fm["type"] == "kb/sources/types/snapshot.md"
    assert fm["tags"] == ["github-issue"]
    assert fm["api_url"] == "https://api.github.com/repos/example/project/issues/123"
    assert f"SHA-256: {snapshot_sha256(md_path)}" in result
    assert github_snapshot.DEFAULT_SNAPSHOT_DIR == "kb/sources/.snapshots"


def test_github_snapshot_stamps_snapshot_pr_family(
    tmp_path: Path, monkeypatch
) -> None:
    payload = {
        "title": "PR title",
        "number": 456,
        "state": "open",
        "repository_url": "https://api.github.com/repos/example/project",
        "user": {"login": "alice"},
        "labels": [],
        "body": "PR body",
    }
    monkeypatch.setattr(github_snapshot, "_gh_api", lambda _url: json.dumps(payload))

    github_snapshot.snapshot_github_url(
        "https://github.com/example/project/pull/456",
        out_dir=str(tmp_path),
    )

    md_path = next(tmp_path.glob("*.md"))
    fm = frontmatter(md_path)

    assert fm["type"] == "kb/sources/types/snapshot.md"
    assert fm["tags"] == ["github-pr"]
    assert fm["api_url"] == "https://api.github.com/repos/example/project/pulls/456"


def test_github_snapshot_reports_checksum_for_existing_capture(
    tmp_path: Path, monkeypatch
) -> None:
    existing = tmp_path / "existing.md"
    existing.write_text(
        "---\nsource: https://github.com/example/project/issues/123\n---\n",
        encoding="utf-8",
    )
    monkeypatch.setattr(
        github_snapshot,
        "_gh_api",
        lambda _url: (_ for _ in ()).throw(AssertionError("must not fetch")),
    )

    result = github_snapshot.snapshot_github_url(
        "https://github.com/example/project/issues/123",
        out_dir=str(tmp_path),
    )

    assert result == (
        f"Already snapshotted: {existing}\n"
        f"SHA-256: {snapshot_sha256(existing)}"
    )
