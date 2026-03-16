#!/usr/bin/env python3
"""Snapshot X/Twitter posts, threads, and article posts to kb/sources/.

Usage:
    uv run kb/scripts/x_snapshot.py "https://x.com/<user>/status/<id>"
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib.parse import urlparse

import xdk

DEFAULT_SNAPSHOT_DIR = "kb/sources"
DEFAULT_MAX_POSTS = 200

POST_FIELDS = [
    "id",
    "text",
    "author_id",
    "created_at",
    "conversation_id",
    "in_reply_to_user_id",
    "referenced_tweets",
    "note_tweet",
    "entities",
    "article",
]
USER_FIELDS = ["id", "username", "name"]
EXPANSIONS = ["author_id", "in_reply_to_user_id", "referenced_tweets.id"]


def _slugify(text: str, max_len: int = 70) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:max_len].rstrip("-") or "x-snapshot"


def _canonical_source_url(url: str) -> str:
    parsed = urlparse(url)
    host = parsed.netloc.lower().replace("www.", "")
    path = parsed.path.strip("/")
    segments = [s for s in path.split("/") if s]

    if host in {"x.com", "twitter.com"}:
        status_id, username = _extract_status_info(segments)
        if status_id:
            if username:
                return f"https://x.com/{username}/status/{status_id}"
            return f"https://x.com/i/web/status/{status_id}"

        if len(segments) >= 3 and segments[:2] == ["i", "article"]:
            article_id = segments[2]
            if article_id.isdigit():
                return f"https://x.com/i/article/{article_id}"

    return url


def _extract_status_info(segments: list[str]) -> tuple[str | None, str | None]:
    status_id: str | None = None
    username: str | None = None

    for index, segment in enumerate(segments[:-1]):
        if segment != "status":
            continue
        candidate = segments[index + 1]
        if candidate.isdigit():
            status_id = candidate
            if index > 0 and segments[0] not in {"i", "web", "intent"}:
                username = segments[0]
            break

    return status_id, username


def _extract_status_id(url: str) -> str | None:
    parsed = urlparse(url)
    host = parsed.netloc.lower().replace("www.", "")
    if host not in {"x.com", "twitter.com"}:
        return None

    segments = [s for s in parsed.path.strip("/").split("/") if s]
    status_id, _ = _extract_status_info(segments)
    return status_id


def _is_article_url(url: str) -> bool:
    parsed = urlparse(url)
    host = parsed.netloc.lower().replace("www.", "")
    if host not in {"x.com", "twitter.com"}:
        return False
    segments = [s for s in parsed.path.strip("/").split("/") if s]
    return len(segments) >= 3 and segments[:2] == ["i", "article"] and segments[2].isdigit()


def _extract_users_map(includes: dict[str, Any] | None) -> dict[str, dict[str, Any]]:
    users: dict[str, dict[str, Any]] = {}
    for user in (includes or {}).get("users") or []:
        user_id = str(user.get("id", "")).strip()
        if user_id:
            users[user_id] = user
    return users


def _fetch_post(
    client: xdk.Client,
    post_id: str,
) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    response = client.posts.get_by_id(
        post_id,
        tweet_fields=POST_FIELDS,
        expansions=EXPANSIONS,
        user_fields=USER_FIELDS,
    )
    payload = response.model_dump()
    data = payload.get("data") or {}
    if not data:
        errors = payload.get("errors") or []
        raise RuntimeError(f"Could not fetch post {post_id}. Errors: {errors}")
    return data, _extract_users_map(payload.get("includes"))


def _reply_parent_id(post: dict[str, Any]) -> str | None:
    for ref in post.get("referenced_tweets") or []:
        if ref.get("type") == "replied_to" and ref.get("id"):
            return str(ref["id"])
    return None


def _fetch_ancestors(
    client: xdk.Client,
    start_post: dict[str, Any],
    max_hops: int = 20,
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]]]:
    posts: dict[str, dict[str, Any]] = {}
    users: dict[str, dict[str, Any]] = {}

    current = start_post
    hops = 0
    while hops < max_hops:
        parent_id = _reply_parent_id(current)
        if not parent_id or parent_id in posts:
            break
        try:
            parent, parent_users = _fetch_post(client, parent_id)
        except Exception:
            break
        posts[str(parent.get("id"))] = parent
        users.update(parent_users)
        current = parent
        hops += 1

    return posts, users


def _fetch_thread_recent(
    client: xdk.Client,
    conversation_id: str,
    thread_author_id: str | None,
    max_posts: int,
) -> tuple[dict[str, dict[str, Any]], dict[str, dict[str, Any]], str | None]:
    posts: dict[str, dict[str, Any]] = {}
    users: dict[str, dict[str, Any]] = {}

    query = f"conversation_id:{conversation_id}"
    error: str | None = None

    try:
        for page in client.posts.search_recent(
            query=query,
            max_results=100,
            sort_order="recency",
            tweet_fields=POST_FIELDS,
            expansions=EXPANSIONS,
            user_fields=USER_FIELDS,
        ):
            payload = page.model_dump()
            users.update(_extract_users_map(payload.get("includes")))

            for post in payload.get("data") or []:
                post_id = str(post.get("id", "")).strip()
                if not post_id:
                    continue
                if thread_author_id and str(post.get("author_id")) != thread_author_id:
                    continue
                posts[post_id] = post
                if len(posts) >= max_posts:
                    return posts, users, None
    except Exception as exc:
        error = str(exc)

    return posts, users, error


def _post_sort_key(post: dict[str, Any]) -> tuple[str, int]:
    created_at = str(post.get("created_at", ""))
    post_id = post.get("id")
    try:
        numeric_id = int(post_id) if post_id is not None else 0
    except (TypeError, ValueError):
        numeric_id = 0
    return created_at, numeric_id


def _post_text(post: dict[str, Any]) -> str:
    note_text = (post.get("note_tweet") or {}).get("text")
    if isinstance(note_text, str) and note_text.strip():
        return note_text.strip()
    return str(post.get("text") or "").strip()


def _post_url(post: dict[str, Any], users: dict[str, dict[str, Any]]) -> str:
    post_id = str(post.get("id", "")).strip()
    author_id = str(post.get("author_id", "")).strip()
    username = (users.get(author_id) or {}).get("username")
    if username:
        return f"https://x.com/{username}/status/{post_id}"
    return f"https://x.com/i/web/status/{post_id}"


def _dedup_existing_snapshot(out_dir: Path, source_url: str) -> Path | None:
    marker = f"source: {source_url}"
    for existing in out_dir.glob("*.md"):
        try:
            header = existing.read_text(encoding="utf-8")[:1000]
        except OSError:
            continue
        if marker in header:
            return existing
    return None


def _render_markdown(
    source_url: str,
    timestamp: str,
    kind: str,
    target_post: dict[str, Any],
    posts_sorted: list[dict[str, Any]],
    users: dict[str, dict[str, Any]],
    thread_error: str | None,
) -> str:
    status_id = str(target_post.get("id", ""))
    conversation_id = str(target_post.get("conversation_id") or status_id)
    author_id = str(target_post.get("author_id", ""))
    username = (users.get(author_id) or {}).get("username", "")
    author_label = f"@{username}" if username else author_id or "unknown"

    article = target_post.get("article") or {}
    article_title = str(article.get("title", "")).strip()
    article_text = str(article.get("plain_text", "")).strip()

    lines: list[str] = [
        "---",
        f"source: {source_url}",
        f"captured: {timestamp}",
        "capture: xdk",
        f"type: {kind}",
        f"status_id: {status_id}",
        f"conversation_id: {conversation_id}",
        f"post_count: {len(posts_sorted)}",
        "---",
        "",
    ]

    if article_text:
        title = article_title or f"Article from {author_label}"
        lines.extend(
            [
                f"# {title}",
                "",
                f"Author: {author_label}",
                f"Post: {_post_url(target_post, users)}",
                f"Created: {target_post.get('created_at', '')}",
                "",
                article_text,
                "",
            ]
        )
        return "\n".join(lines)

    heading = f"Thread by {author_label}" if len(posts_sorted) > 1 else f"Post by {author_label}"
    lines.extend([f"# {heading}", "", f"Source post: {_post_url(target_post, users)}", ""])
    if thread_error:
        lines.extend([f"Thread fetch note: {thread_error}", ""])

    for idx, post in enumerate(posts_sorted, start=1):
        post_created = str(post.get("created_at", ""))
        post_link = _post_url(post, users)
        text = _post_text(post)

        lines.append(f"## {idx}. {post_created} {post_link}".rstrip())
        lines.append("")
        lines.append(text or "(no text)")
        urls = (post.get("entities") or {}).get("urls") or []
        expanded = [u.get("expanded_url") for u in urls if u.get("expanded_url")]
        if expanded:
            lines.append("")
            lines.append("Links:")
            for link in expanded:
                lines.append(f"- {link}")
        lines.append("")

    return "\n".join(lines)


def snapshot_x_url(url: str, out_dir: str, max_posts: int) -> str:
    source_url = _canonical_source_url(url.strip())
    status_id = _extract_status_id(source_url)

    if not status_id:
        if _is_article_url(source_url):
            raise RuntimeError(
                "Direct /i/article/<id> URLs are not resolvable via this script. "
                "Paste the source post URL (/status/<id>) instead."
            )
        raise RuntimeError("Unsupported URL. Expected an X/Twitter status URL.")

    token = os.getenv("X_BEARER_TOKEN", "").strip()
    if not token:
        raise RuntimeError("Missing X_BEARER_TOKEN in environment.")

    now = datetime.now(timezone.utc)
    timestamp = now.isoformat()
    dest = Path(out_dir)
    dest.mkdir(parents=True, exist_ok=True)

    existing = _dedup_existing_snapshot(dest, source_url)
    if existing:
        return f"Already snapshotted: {existing}"

    client = xdk.Client(bearer_token=token)

    target_post, users = _fetch_post(client, status_id)
    target_id = str(target_post.get("id"))
    if target_id:
        posts_map: dict[str, dict[str, Any]] = {target_id: target_post}
    else:
        posts_map = {}

    ancestor_posts, ancestor_users = _fetch_ancestors(client, target_post)
    posts_map.update(ancestor_posts)
    users.update(ancestor_users)

    conversation_id = str(target_post.get("conversation_id") or status_id)
    author_id = str(target_post.get("author_id") or "")
    recent_posts, recent_users, thread_error = _fetch_thread_recent(
        client,
        conversation_id=conversation_id,
        thread_author_id=author_id or None,
        max_posts=max_posts,
    )
    posts_map.update(recent_posts)
    users.update(recent_users)

    posts_sorted = sorted(posts_map.values(), key=_post_sort_key)
    if all(str(post.get("id")) != target_id for post in posts_sorted):
        posts_sorted.append(target_post)
        posts_sorted.sort(key=_post_sort_key)

    article_text = str(((target_post.get("article") or {}).get("plain_text") or "")).strip()
    kind = "x-article" if article_text else ("x-thread" if len(posts_sorted) > 1 else "x-post")

    base_title = (
        str(((target_post.get("article") or {}).get("title") or "")).strip()
        or _post_text(target_post)[:70]
        or f"x-status-{status_id}"
    )
    slug = f"{_slugify(base_title)}-{status_id}"

    json_path = dest / f"{slug}.json"
    md_path = dest / f"{slug}.md"

    payload = {
        "source": source_url,
        "captured": timestamp,
        "type": kind,
        "status_id": status_id,
        "conversation_id": conversation_id,
        "target_post": target_post,
        "posts": posts_sorted,
        "users": users,
        "thread_fetch_error": thread_error,
    }
    json_path.write_text(json.dumps(payload, ensure_ascii=True, indent=2), encoding="utf-8")

    md = _render_markdown(
        source_url=source_url,
        timestamp=timestamp,
        kind=kind,
        target_post=target_post,
        posts_sorted=posts_sorted,
        users=users,
        thread_error=thread_error,
    )
    md_path.write_text(md, encoding="utf-8")

    preview = _post_text(target_post).replace("\n", " ").strip()[:200]
    return f"Snapshot saved: {md_path}\nSource: {json_path}\n\nPreview: {preview}..."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Snapshot X/Twitter post/thread/article text into kb/sources/.",
    )
    parser.add_argument(
        "url",
        help="X/Twitter URL from the web UI, e.g. https://x.com/<user>/status/<id>",
    )
    parser.add_argument(
        "--out-dir",
        default=os.getenv("TRIAGE_SNAPSHOT_DIR", DEFAULT_SNAPSHOT_DIR),
        help=f"Snapshot root directory (default: {DEFAULT_SNAPSHOT_DIR})",
    )
    parser.add_argument(
        "--max-posts",
        type=int,
        default=DEFAULT_MAX_POSTS,
        help=f"Max posts to keep when fetching a thread (default: {DEFAULT_MAX_POSTS})",
    )
    return parser.parse_args()


def main() -> int:
    from dotenv import load_dotenv

    load_dotenv()
    args = parse_args()
    try:
        result = snapshot_x_url(args.url, out_dir=args.out_dir, max_posts=args.max_posts)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
