from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest
import yaml


SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

pytest.importorskip("xdk")

from commonplace.cli import x_snapshot  # noqa: E402


def frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    raw = content.split("---", 2)[1]
    return yaml.safe_load(raw)


class FakeClient:
    def __init__(self, bearer_token: str) -> None:
        self.bearer_token = bearer_token


@pytest.mark.parametrize(
    ("target_overrides", "recent_posts", "expected_family"),
    [
        ({}, {}, "x-post"),
        (
            {},
            {
                "1003": {
                    "id": "1003",
                    "text": "Thread reply",
                    "author_id": "42",
                    "created_at": "2026-04-19T10:01:00Z",
                    "conversation_id": "1002",
                }
            },
            "x-thread",
        ),
        (
            {"article": {"title": "Article title", "plain_text": "Article body."}},
            {
                "1003": {
                    "id": "1003",
                    "text": "Thread reply",
                    "author_id": "42",
                    "created_at": "2026-04-19T10:01:00Z",
                    "conversation_id": "1002",
                }
            },
            "x-article",
        ),
    ],
)
def test_x_snapshot_stamps_family_tag_into_frontmatter_and_sidecar(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target_overrides: dict,
    recent_posts: dict,
    expected_family: str,
) -> None:
    target_post = {
        "id": "1002",
        "text": "Thread opener",
        "author_id": "42",
        "created_at": "2026-04-19T10:00:00Z",
        "conversation_id": "1002",
    }
    target_post.update(target_overrides)
    users = {"42": {"id": "42", "username": "alice", "name": "Alice"}}
    monkeypatch.setenv("X_BEARER_TOKEN", "token")
    monkeypatch.setattr(x_snapshot.xdk, "Client", FakeClient)
    monkeypatch.setattr(x_snapshot, "_fetch_post", lambda _client, _post_id: (target_post, users))
    monkeypatch.setattr(x_snapshot, "_fetch_ancestors", lambda _client, _post: ({}, {}))
    monkeypatch.setattr(
        x_snapshot,
        "_fetch_thread_recent",
        lambda _client, **_kwargs: (recent_posts, users, None),
    )

    x_snapshot.snapshot_x_url(
        f"https://x.com/alice/status/{target_post['id']}",
        out_dir=str(tmp_path),
        max_posts=200,
    )

    md_path = next(tmp_path.glob("*.md"))
    json_path = next(tmp_path.glob("*.json"))
    fm = frontmatter(md_path)
    sidecar = json.loads(json_path.read_text(encoding="utf-8"))

    assert fm["type"] == "kb/sources/types/snapshot.md"
    assert fm["tags"] == [expected_family]
    assert sidecar["family"] == expected_family
    assert "type" not in sidecar
