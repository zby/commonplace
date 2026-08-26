from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

import pytest
import yaml

SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.cli import github_snapshot
from commonplace.lib.naming import MAX_INGEST_SNAPSHOT_SLUG_LENGTH


def frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    raw = content.split("---", 2)[1]
    return yaml.safe_load(raw)


@pytest.mark.parametrize(
    ("url", "number", "expected_family", "expected_api_url"),
    [
        (
            "https://github.com/example/project/issues/123",
            123,
            "github-issue",
            "https://api.github.com/repos/example/project/issues/123",
        ),
        (
            "https://github.com/example/project/pull/456",
            456,
            "github-pr",
            "https://api.github.com/repos/example/project/pulls/456",
        ),
    ],
)
def test_github_snapshot_captures_issue_and_pull_request_families(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    url: str,
    number: int,
    expected_family: str,
    expected_api_url: str,
) -> None:
    payload = {
        "title": "Capture title",
        "number": number,
        "state": "open",
        "repository_url": "https://api.github.com/repos/example/project",
        "user": {"login": "alice"},
        "labels": [],
        "body": "Capture body",
    }
    monkeypatch.setattr(github_snapshot, "_gh_api", lambda _url: json.dumps(payload))

    result = github_snapshot.snapshot_github_url(
        url,
        out_dir=str(tmp_path),
    )

    md_path = next(tmp_path.glob("*.md"))
    fm = frontmatter(md_path)

    assert fm["type"] == "kb/sources/types/snapshot.md"
    assert fm["tags"] == [expected_family]
    assert fm["api_url"] == expected_api_url
    assert len(md_path.stem) <= MAX_INGEST_SNAPSHOT_SLUG_LENGTH
    assert len(f"{md_path.stem}.ingest") <= 70
    checksum = hashlib.sha256(md_path.read_bytes()).hexdigest()
    assert f"SHA-256: {checksum}" in result


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
        f"SHA-256: {hashlib.sha256(existing.read_bytes()).hexdigest()}"
    )


def test_github_snapshot_preserves_number_when_title_needs_truncation(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    payload = {
        "title": "A very long issue title " * 20,
        "number": 123,
        "state": "open",
        "repository_url": "https://api.github.com/repos/example/project",
        "user": {"login": "alice"},
        "labels": [],
        "body": "Capture body",
    }
    monkeypatch.setattr(github_snapshot, "_gh_api", lambda _url: json.dumps(payload))

    github_snapshot.snapshot_github_url(
        "https://github.com/example/project/issues/123",
        out_dir=str(tmp_path),
    )

    md_path = next(tmp_path.glob("*.md"))
    assert len(md_path.stem) == MAX_INGEST_SNAPSHOT_SLUG_LENGTH
    assert md_path.stem.endswith("-123")
