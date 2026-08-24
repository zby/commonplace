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

from commonplace.cli import x_snapshot


def frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    raw = content.split("---", 2)[1]
    return yaml.safe_load(raw)


class FakeResponse:
    def __init__(self, payload: dict) -> None:
        self.payload = payload

    def model_dump(self) -> dict:
        return self.payload


class FakePosts:
    def __init__(
        self,
        target_post: dict,
        recent_posts: dict[str, dict],
        users: list[dict],
    ) -> None:
        self.target_post = target_post
        self.ancestor_post = {
            "id": "1001",
            "text": "Ancestor post",
            "author_id": "42",
            "created_at": "2026-04-19T09:59:00Z",
            "conversation_id": "1002",
        }
        self.recent_posts = recent_posts
        self.users = users

    def get_by_id(
        self,
        post_id: str,
        *,
        post_fields: list[str],
        expansions: list[str],
        user_fields: list[str],
    ) -> FakeResponse:
        post = (
            self.target_post
            if post_id == self.target_post["id"]
            else self.ancestor_post
        )
        returned_fields = {"id", *post_fields}
        return FakeResponse(
            {
                "data": {
                    key: value for key, value in post.items() if key in returned_fields
                },
                "includes": {"users": self.users},
            }
        )

    def search_recent(
        self,
        *,
        query: str,
        max_results: int,
        sort_order: str,
        post_fields: list[str],
        expansions: list[str],
        user_fields: list[str],
    ) -> list[FakeResponse]:
        returned_fields = {"id", *post_fields}
        return [
            FakeResponse(
                {
                    "data": [
                        {
                            key: value
                            for key, value in post.items()
                            if key in returned_fields
                        }
                        for post in self.recent_posts.values()
                    ],
                    "includes": {"users": self.users},
                }
            )
        ]


class FakeClient:
    def __init__(self, posts: FakePosts) -> None:
        self.posts = posts


@pytest.mark.parametrize(
    ("target_overrides", "recent_posts", "expected_family", "expected_content"),
    [
        ({}, {}, "x-post", ("Full opener text",)),
        (
            {"referenced_posts": [{"type": "replied_to", "id": "1001"}]},
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
            ("Ancestor post", "Full opener text", "Thread reply"),
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
            ("Article body.",),
        ),
    ],
)
def test_x_snapshot_captures_each_content_family(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
    target_overrides: dict,
    recent_posts: dict,
    expected_family: str,
    expected_content: tuple[str, ...],
) -> None:
    target_post = {
        "id": "1002",
        "text": "Truncated opener",
        "note_post": {"text": "Full opener text"},
        "author_id": "42",
        "created_at": "2026-04-19T10:00:00Z",
        "conversation_id": "1002",
    }
    target_post.update(target_overrides)
    users = [{"id": "42", "username": "alice", "name": "Alice"}]

    def fake_client(bearer_token: str) -> FakeClient:
        assert bearer_token == "token"
        return FakeClient(FakePosts(target_post, recent_posts, users))

    monkeypatch.setenv("X_BEARER_TOKEN", "token")
    monkeypatch.setattr(x_snapshot.xdk, "Client", fake_client)

    result = x_snapshot.snapshot_x_url(
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
    rendered = md_path.read_text(encoding="utf-8")
    assert all(content in rendered for content in expected_content)
    checksum = hashlib.sha256(md_path.read_bytes()).hexdigest()
    assert f"SHA-256: {checksum}" in result


def test_x_snapshot_reports_checksum_for_existing_capture(
    tmp_path: Path,
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    existing = tmp_path / "existing.md"
    existing.write_text(
        "---\nsource: https://x.com/alice/status/1002\n---\n",
        encoding="utf-8",
    )
    monkeypatch.setenv("X_BEARER_TOKEN", "token")

    result = x_snapshot.snapshot_x_url(
        "https://x.com/alice/status/1002",
        out_dir=str(tmp_path),
        max_posts=200,
    )

    assert result == (
        f"Already snapshotted: {existing}\n"
        f"SHA-256: {hashlib.sha256(existing.read_bytes()).hexdigest()}"
    )
