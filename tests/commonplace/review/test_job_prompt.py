from __future__ import annotations

from pathlib import Path

from commonplace.review.job_prompt import resolve_note_markdown_links


def write(path: Path, text: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def test_resolve_note_markdown_links_sizes_occurrences_and_reports_unavailable_targets(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    note = write(repo / "kb/notes/note.md", "# Note\n")
    shared = write(repo / "kb/notes/shared.md", "shared bytes\n")
    ingest = write(repo / "kb/sources/source.ingest.md", "ingest bytes\n")
    body = """
[first](./shared.md)
[same target](./shared.md#section)
[source (snapshot required)](../sources/source.ingest.md)
[missing](./missing.md)
[external](https://example.com/page.md)
"""

    resolved, unavailable = resolve_note_markdown_links(
        repo_root=repo,
        note_abs=note,
        note_body=body,
    )

    assert [(link.link_text, link.repo_path, link.size_bytes) for link in resolved] == [
        ("first", "kb/notes/shared.md", shared.stat().st_size),
        ("same target", "kb/notes/shared.md", shared.stat().st_size),
        (
            "source (snapshot required)",
            "kb/sources/source.ingest.md",
            ingest.stat().st_size,
        ),
    ]
    assert [
        (target.link_text, target.target_path, target.reason)
        for target in unavailable
    ] == [
        (
            "source (snapshot required)",
            "kb/sources/.snapshots/source.md",
            "required snapshot missing file",
        ),
        ("missing", "kb/notes/missing.md", "missing file"),
    ]


def test_resolve_note_markdown_links_does_not_charge_required_snapshot_in_v1(
    tmp_path: Path,
) -> None:
    repo = tmp_path / "repo"
    note = write(repo / "kb/notes/note.md", "# Note\n")
    ingest = write(repo / "kb/sources/source.ingest.md", "small ingest\n")
    write(repo / "kb/sources/.snapshots/source.md", "a much larger snapshot body\n")

    resolved, unavailable = resolve_note_markdown_links(
        repo_root=repo,
        note_abs=note,
        note_body="[source (snapshot required)](../sources/source.ingest.md)",
    )

    assert [(link.repo_path, link.size_bytes) for link in resolved] == [
        ("kb/sources/source.ingest.md", ingest.stat().st_size)
    ]
    assert unavailable == []
