from __future__ import annotations

from pathlib import Path

from commonplace.lib.validation import validate_note


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def setup_repo(tmp_path: Path) -> Path:
    # The validator resolves global and collection-local type specs from the
    # repo root, so the fixture repo needs the real specs copied in.
    repo_root = Path(__file__).resolve().parents[3]
    real_types = repo_root / "kb" / "types"
    for name in (
        "note.md",
        "note.schema.yaml",
        "note-base.schema.yaml",
        "type-spec.md",
        "type-spec.schema.yaml",
    ):
        write(
            tmp_path / "kb" / "types" / name,
            (real_types / name).read_text(encoding="utf-8"),
        )
    write(tmp_path / "kb" / "notes" / "COLLECTION.md", "# Notes collection\n")
    return tmp_path / "kb" / "notes"


def ingest(tmp_path: Path, slug: str, *, passage: str, summary: str = "Analysis.") -> Path:
    return write(
        tmp_path / "kb" / "sources" / f"{slug}.ingest.md",
        f"""---
description: a tracked ingest used by the unquoted-sources validation tests
source: https://example.com/{slug}
---

# {slug}

## Summary

{summary}

## Quotes

- **Source extract (verbatim):** {passage}
  - **Source location:** Section 1.
""",
    )


def note(path: Path, body: str) -> Path:
    return write(
        path,
        f"""---
description: "a note used by the unquoted-sources validation tests"
type: kb/types/note.md
---

# A test note

{body}
""",
    )


def _cite(slug: str, *, snapshot_required: bool = False) -> str:
    marker = " (snapshot required)" if snapshot_required else ""
    return f"[{slug}{marker}](../sources/{slug}.ingest.md)"


def test_six_unquoted_tracked_sources_warn(tmp_path: Path) -> None:
    notes = setup_repo(tmp_path)
    slugs = [f"src-{index}" for index in range(1, 7)]
    for slug in slugs:
        ingest(tmp_path, slug, passage="the passage text here")
    path = note(
        notes / "test-note.md",
        "The claim rests on several tracked sources "
        + ", ".join(_cite(slug) for slug in slugs)
        + ".",
    )

    results = validate_note(path, repo_root=tmp_path)

    warns = [warn for warn in results.warns if "unquoted sources" in warn]
    assert len(warns) == 1
    assert "6 distinct tracked sources" in warns[0]
    assert all(f"{slug}.ingest.md" in warns[0] for slug in slugs)


def test_one_verified_quote_brings_the_note_under_the_bound(tmp_path: Path) -> None:
    notes = setup_repo(tmp_path)
    slugs = [f"src-{index}" for index in range(1, 7)]
    for slug in slugs:
        ingest(tmp_path, slug, passage="the passage text here")
    path = note(
        notes / "test-note.md",
        "The first source states, verbatim, "
        f'"the passage text here" ({_cite("src-1")}).\n\n'
        "The rest are cited without a retained quotation: "
        + ", ".join(_cite(slug) for slug in slugs[1:])
        + ".",
    )

    results = validate_note(path, repo_root=tmp_path)

    assert not [warn for warn in results.warns if "unquoted sources" in warn]
    assert any(
        "unquoted sources: 5 of 6 tracked sources need a full read (limit 5)" in line
        for line in results.passes
    )


def test_snapshot_required_source_counts_even_when_quoted(tmp_path: Path) -> None:
    notes = setup_repo(tmp_path)
    slugs = [f"src-{index}" for index in range(1, 7)]
    for slug in slugs:
        ingest(tmp_path, slug, passage="the passage text here")
    path = note(
        notes / "test-note.md",
        "The first source states, verbatim, "
        f'"the passage text here" ({_cite("src-1", snapshot_required=True)}).\n\n'
        "The rest are cited without a retained quotation: "
        + ", ".join(_cite(slug) for slug in slugs[1:])
        + ".",
    )

    results = validate_note(path, repo_root=tmp_path)

    warns = [warn for warn in results.warns if "unquoted sources" in warn]
    assert len(warns) == 1
    assert "6 distinct tracked sources" in warns[0]
    assert "src-1.ingest.md" in warns[0]


def test_note_citing_no_tracked_source_says_nothing(tmp_path: Path) -> None:
    notes = setup_repo(tmp_path)
    note(notes / "other-note.md", "A sibling note.")
    path = note(
        notes / "test-note.md",
        "This note only links a sibling [other note](./other-note.md).",
    )

    results = validate_note(path, repo_root=tmp_path)

    assert not any(
        "unquoted sources" in line
        for line in results.passes + results.warns + results.fails
    )


def test_quote_matching_only_ingest_analysis_does_not_discharge(tmp_path: Path) -> None:
    """Ties to the Quotes-section confinement: analysis prose is not support."""
    notes = setup_repo(tmp_path)
    slugs = [f"src-{index}" for index in range(1, 7)]
    for slug in slugs:
        ingest(tmp_path, slug, passage="an unrelated retained passage")
    ingest(
        tmp_path,
        "src-1",
        passage="an unrelated retained passage",
        summary="The author writes that the passage text here is central.",
    )
    path = note(
        notes / "test-note.md",
        "The first source states, verbatim, "
        f'"the passage text here" ({_cite("src-1")}).\n\n'
        "The rest are cited without a retained quotation: "
        + ", ".join(_cite(slug) for slug in slugs[1:])
        + ".",
    )

    results = validate_note(path, repo_root=tmp_path)

    warns = [warn for warn in results.warns if "unquoted sources" in warn]
    assert len(warns) == 1
    assert "6 distinct tracked sources" in warns[0]
