#!/usr/bin/env python3
"""Snapshot GitHub issue/PR content into kb/sources/.

Usage:
    uv run kb/scripts/github_snapshot.py "https://github.com/owner/repo/issues/123"
    uv run kb/scripts/github_snapshot.py "https://api.github.com/repos/owner/repo/issues/123"
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

DEFAULT_SNAPSHOT_DIR = "kb/sources"


def _slugify(text: str, max_len: int = 70) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:max_len].rstrip("-") or "github-snapshot"


def _is_github_issue_api_path(path: str) -> bool:
    return bool(re.match(r"^/repos/[^/]+/[^/]+/(issues|pulls)/[0-9]+$", path))


def _to_api_url(url: str) -> tuple[str, str]:
    parsed = urlparse(url.strip())
    host = parsed.netloc.lower().replace("www.", "")
    path = parsed.path.rstrip("/")

    if host == "api.github.com" and _is_github_issue_api_path(path):
        api_url = f"https://api.github.com{path}"
        return api_url, api_url

    if host == "github.com":
        match = re.match(r"^/([^/]+)/([^/]+)/(issues|pull)/([0-9]+)$", path)
        if match:
            owner, repo, kind, number = match.groups()
            api_kind = "issues" if kind == "issues" else "pulls"
            api_url = f"https://api.github.com/repos/{owner}/{repo}/{api_kind}/{number}"
            canonical_source = f"https://github.com/{owner}/{repo}/{kind}/{number}"
            return api_url, canonical_source

    raise ValueError(
        "Unsupported URL. Expected GitHub issue/PR URL or API URL for issue/pull."
    )


def _gh_api(url: str, timeout: int = 30) -> str:
    result = subprocess.run(
        ["gh", "api", url],
        capture_output=True,
        text=True,
        timeout=timeout,
    )
    if result.returncode != 0:
        stderr = result.stderr.strip() or "(no stderr)"
        raise RuntimeError(f"gh api failed for {url}: {stderr}")
    return result.stdout


def _render_markdown(data: dict) -> str:
    title = str(data.get("title") or "Untitled")
    number = data.get("number")
    state = str(data.get("state") or "")
    user = ""
    if isinstance(data.get("user"), dict):
        user = str(data["user"].get("login") or "")

    labels: list[str] = []
    if isinstance(data.get("labels"), list):
        for label in data["labels"]:
            if isinstance(label, dict) and label.get("name"):
                labels.append(str(label["name"]))

    lines = [f"# {title}" + (f" (#{number})" if number else ""), ""]

    meta = []
    if state:
        meta.append(f"**State:** {state}")
    if user:
        meta.append(f"**Author:** {user}")
    if labels:
        meta.append(f"**Labels:** {', '.join(labels)}")
    if meta:
        lines.append(" | ".join(meta))
        lines.append("")

    body = str(data.get("body") or "").strip()
    if body:
        lines.append(body[:10000])
    else:
        lines.append("(no body)")
    lines.append("")
    return "\n".join(lines)


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


def snapshot_github_url(url: str, out_dir: str) -> str:
    api_url, source_url = _to_api_url(url)

    now = datetime.now(timezone.utc)
    timestamp = now.isoformat()
    dest = Path(out_dir)
    dest.mkdir(parents=True, exist_ok=True)

    existing = _dedup_existing_snapshot(dest, source_url)
    if existing:
        return f"Already snapshotted: {existing}"

    raw = _gh_api(api_url)
    data = json.loads(raw)

    title = str(data.get("title") or "")
    number = str(data.get("number") or "")
    repo = str(data.get("repository_url") or "").rstrip("/").split("/")[-2:]
    repo_slug = "-".join(repo) if len(repo) == 2 else ""
    slug_bits = [repo_slug, number, _slugify(title, max_len=45)]
    slug = "-".join(bit for bit in slug_bits if bit).strip("-") or "github-snapshot"

    source_path = dest / f"{slug}.json"
    md_path = dest / f"{slug}.md"

    source_path.write_text(json.dumps(data, ensure_ascii=True, indent=2), encoding="utf-8")

    md_body = _render_markdown(data)
    md = (
        f"---\n"
        f"source: {source_url}\n"
        f"api_url: {api_url}\n"
        f"captured: {timestamp}\n"
        f"capture: gh-api\n"
        f"type: github-issue\n"
        f"---\n\n"
        f"{md_body}"
    )
    md_path.write_text(md, encoding="utf-8")

    preview = md_body.replace("\n", " ").strip()[:200]
    return f"Snapshot saved: {md_path}\nSource: {source_path}\n\nPreview: {preview}..."


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Snapshot a GitHub issue/PR URL into kb/sources/.",
    )
    parser.add_argument(
        "url",
        help=(
            "GitHub issue/PR URL from browser or API URL. "
            "Example: https://github.com/owner/repo/issues/123"
        ),
    )
    parser.add_argument(
        "--out-dir",
        default=os.getenv("TRIAGE_SNAPSHOT_DIR", DEFAULT_SNAPSHOT_DIR),
        help=f"Snapshot root directory (default: {DEFAULT_SNAPSHOT_DIR})",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        result = snapshot_github_url(args.url, out_dir=args.out_dir)
    except Exception as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1

    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
