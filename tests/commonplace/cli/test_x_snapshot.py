from __future__ import annotations

import json
import sys
from pathlib import Path
from types import SimpleNamespace

import pytest
import yaml


SRC_ROOT = Path(__file__).resolve().parents[4] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.cli import x_snapshot  # noqa: E402


def frontmatter(path: Path) -> dict:
    content = path.read_text(encoding="utf-8")
    raw = content.split("---", 2)[1]
    return yaml.safe_load(raw)


class FakeClient:
    def __init__(self, bearer_token: str) -> None:
        self.bearer_token = bearer_token


class FakeResponse:
    def __init__(self, payload: dict) -> None:
        self.payload = payload

    def model_dump(self) -> dict:
        return self.payload


def test_fetch_post_uses_xdk_0_10_post_vocabulary() -> None:
    target_post = {
        "id": "1002",
        "text": "Truncated text",
        "author_id": "42",
        "referenced_posts": [{"type": "replied_to", "id": "1001"}],
        "note_post": {"text": "Full post text"},
    }

    class LookupPosts:
        def get_by_id(
            self,
            post_id: str,
            *,
            post_fields: list[str],
            expansions: list[str],
            user_fields: list[str],
        ) -> FakeResponse:
            assert post_id == "1002"
            assert "referenced_posts" in post_fields
            assert "note_post" in post_fields
            assert "referenced_tweets" not in post_fields
            assert expansions == [
                "author_id",
                "in_reply_to_user_id",
                "referenced_posts",
            ]
            assert user_fields == x_snapshot.USER_FIELDS
            return FakeResponse(
                {
                    "data": target_post,
                    "includes": {
                        "users": [{"id": "42", "username": "alice", "name": "Alice"}]
                    },
                }
            )

    client = SimpleNamespace(posts=LookupPosts())
    post, users = x_snapshot._fetch_post(client, "1002")

    assert users["42"]["username"] == "alice"
    assert x_snapshot._reply_parent_id(post) == "1001"
    assert x_snapshot._post_text(post) == "Full post text"


def test_fetch_thread_recent_uses_xdk_0_10_post_fields() -> None:
    class RecentPosts:
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
            assert query == "conversation_id:1002"
            assert max_results == 100
            assert sort_order == "recency"
            assert "referenced_posts" in post_fields
            assert "note_post" in post_fields
            assert expansions == [
                "author_id",
                "in_reply_to_user_id",
                "referenced_posts",
            ]
            assert user_fields == x_snapshot.USER_FIELDS
            return [
                FakeResponse(
                    {
                        "data": [{"id": "1003", "author_id": "42"}],
                        "includes": {
                            "users": [
                                {"id": "42", "username": "alice", "name": "Alice"}
                            ]
                        },
                    }
                )
            ]

    client = SimpleNamespace(posts=RecentPosts())
    posts, users, error = x_snapshot._fetch_thread_recent(
        client,
        conversation_id="1002",
        thread_author_id="42",
        max_posts=200,
    )

    assert error is None
    assert list(posts) == ["1003"]
    assert users["42"]["username"] == "alice"


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
    monkeypatch.setattr(
        x_snapshot, "_fetch_post", lambda _client, _post_id: (target_post, users)
    )
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
