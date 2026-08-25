"""Prompt-target preparation for review jobs."""

from __future__ import annotations

import re
import stat
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import find_markdown_links_with_text
from commonplace.review.protocol.prompt import (
    NoteReviewTarget,
    ResolvedMarkdownLink,
    UnavailableMarkdownTarget,
)

URL_SCHEME_RE = re.compile(r"^[a-z]+://", re.IGNORECASE)
SNAPSHOT_REQUIRED_MARKER = "(snapshot required)"


def _display_target_path(candidate: Path, repo_root: Path, raw_target: str) -> str:
    try:
        return candidate.relative_to(repo_root).as_posix()
    except ValueError:
        return raw_target


def _target_size(candidate: Path) -> tuple[int | None, str | None]:
    try:
        target_stat = candidate.stat()
    except FileNotFoundError:
        return None, "missing file"
    except OSError:
        return None, "unreadable file"
    if not stat.S_ISREG(target_stat.st_mode):
        return None, "not a regular file"
    return target_stat.st_size, None


def _required_snapshot_path(repo_path: str) -> str | None:
    ingest_path = Path(repo_path)
    suffix = ".ingest.md"
    if not repo_path.startswith("kb/sources/") or not ingest_path.name.endswith(suffix):
        return None
    slug = ingest_path.name.removesuffix(suffix)
    return (ingest_path.parent / ".snapshots" / f"{slug}.md").as_posix()


def resolve_note_markdown_links(
    *,
    repo_root: Path,
    note_abs: Path,
    note_body: str,
) -> tuple[list[ResolvedMarkdownLink], list[UnavailableMarkdownTarget]]:
    """Resolve and size local Markdown targets without making availability a judgment.

    Resolved link occurrences remain separate so telemetry can compare occurrence
    count with distinct artifacts. Whole-file cost is deduplicated later by
    ``repo_path``. A required snapshot is only reported when unavailable; V1
    still prices the directly resolved ingest, as documented by the proposal.
    """
    resolved: list[ResolvedMarkdownLink] = []
    unavailable: list[UnavailableMarkdownTarget] = []

    repo_root_resolved = repo_root.resolve()
    for link_text, raw_target in find_markdown_links_with_text(note_body):
        if URL_SCHEME_RE.match(raw_target) or raw_target.startswith("#"):
            continue

        bare_target = raw_target.split("#", 1)[0]
        if not bare_target or not bare_target.endswith(".md"):
            continue

        try:
            candidate = (note_abs.parent / bare_target).resolve()
        except (OSError, RuntimeError):
            unavailable.append(
                UnavailableMarkdownTarget(
                    link_text=link_text,
                    raw_target=raw_target,
                    target_path=bare_target,
                    reason="unresolvable path",
                )
            )
            continue
        try:
            repo_rel = candidate.relative_to(repo_root_resolved).as_posix()
        except ValueError:
            unavailable.append(
                UnavailableMarkdownTarget(
                    link_text=link_text,
                    raw_target=raw_target,
                    target_path=raw_target,
                    reason="outside repository",
                )
            )
            continue

        size_bytes, reason = _target_size(candidate)
        if reason is not None:
            unavailable.append(
                UnavailableMarkdownTarget(
                    link_text=link_text,
                    raw_target=raw_target,
                    target_path=_display_target_path(candidate, repo_root_resolved, raw_target),
                    reason=reason,
                )
            )
            continue
        assert size_bytes is not None

        resolved.append(
            ResolvedMarkdownLink(
                link_text=link_text,
                raw_target=raw_target,
                repo_path=repo_rel,
                size_bytes=size_bytes,
            )
        )

        if SNAPSHOT_REQUIRED_MARKER not in link_text:
            continue
        snapshot_repo_path = _required_snapshot_path(repo_rel)
        if snapshot_repo_path is None:
            continue
        snapshot_abs = repo_root_resolved / snapshot_repo_path
        _, snapshot_reason = _target_size(snapshot_abs)
        if snapshot_reason is not None:
            unavailable.append(
                UnavailableMarkdownTarget(
                    link_text=link_text,
                    raw_target=raw_target,
                    target_path=snapshot_repo_path,
                    reason=f"required snapshot {snapshot_reason}",
                )
            )

    return resolved, unavailable


def prepare_note_target(
    *,
    repo_root: Path,
    note_path: str,
    criterion_paths: tuple[str, ...],
    note_text: str | None = None,
) -> NoteReviewTarget:
    note_abs = repo_root / note_path
    if note_text is None:
        note_text = note_abs.read_text(encoding="utf-8")
    note_body = frontmatter.strip(note_text).lstrip("\n")
    resolved_links, unavailable_targets = resolve_note_markdown_links(
        repo_root=repo_root,
        note_abs=note_abs,
        note_body=note_body,
    )
    return NoteReviewTarget(
        note_path=note_path,
        criterion_paths=criterion_paths,
        note_text=note_text,
        resolved_links=resolved_links,
        unavailable_targets=unavailable_targets,
    )
