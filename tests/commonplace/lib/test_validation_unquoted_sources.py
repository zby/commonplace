from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib.validation import validate_note
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, copy_repo_files, write

pytestmark = pytest.mark.usefixtures("tmp_library")

SLUGS = [f"src-{index}" for index in range(1, 7)]
QUOTED_PASSAGE = "the passage text here"


def setup_repo(tmp_path: Path, *, passage: str = QUOTED_PASSAGE) -> None:
    """Build a repo whose six tracked ingests each retain `passage`."""
    copy_repo_files(
        tmp_path,
        *NOTE_TYPE_SPECS,
        "kb/articles/types/article.md",
        "kb/articles/types/article.schema.yaml",
    )
    write(tmp_path / "kb" / "notes" / "COLLECTION.md", "# Notes collection\n")
    write(tmp_path / "kb" / "articles" / "COLLECTION.md", "# Articles collection\n")
    for slug in SLUGS:
        ingest(tmp_path, slug, passage=passage)


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


def note(
    tmp_path: Path,
    body: str,
    *,
    collection: str = "notes",
    type_path: str = "types/note.md",
) -> Path:
    return write(
        tmp_path / "kb" / collection / "test-note.md",
        f"""---
description: "a note used by the unquoted-sources validation tests"
type: {type_path}
---

# A test note

{body}
""",
    )


def _cite(slug: str, *, snapshot_required: bool = False) -> str:
    marker = " (snapshot required)" if snapshot_required else ""
    return f"[{slug}{marker}](../sources/{slug}.ingest.md)"


def first_quoted_body(*, snapshot_required: bool = False) -> str:
    """Quote src-1 verbatim and cite the other five without a quotation."""
    return (
        "The first source states, verbatim, "
        f'"{QUOTED_PASSAGE}" ({_cite("src-1", snapshot_required=snapshot_required)}).\n\n'
        "The rest are cited without a retained quotation: "
        + ", ".join(_cite(slug) for slug in SLUGS[1:])
        + "."
    )


def unquoted_fails(path: Path, repo_root: Path) -> list[str]:
    results = validate_note(path, repo_root=repo_root)
    return [fail for fail in results.fails if "unquoted sources" in fail]


@pytest.mark.parametrize(
    ("collection", "type_path"),
    [
        ("notes", "types/note.md"),
        ("articles", "articles/types/article.md"),
    ],
)
def test_six_unquoted_tracked_sources_fail(
    tmp_path: Path, collection: str, type_path: str
) -> None:
    setup_repo(tmp_path)
    path = note(
        tmp_path,
        "The claim rests on several tracked sources "
        + ", ".join(_cite(slug) for slug in SLUGS)
        + ".",
        collection=collection,
        type_path=type_path,
    )

    fails = unquoted_fails(path, tmp_path)

    assert len(fails) == 1
    assert "6 distinct tracked sources" in fails[0]
    assert all(f"{slug}.ingest.md" in fails[0] for slug in SLUGS)


def test_one_verified_quote_brings_the_note_under_the_bound(tmp_path: Path) -> None:
    setup_repo(tmp_path)
    path = note(tmp_path, first_quoted_body())

    results = validate_note(path, repo_root=tmp_path)

    assert not [fail for fail in results.fails if "unquoted sources" in fail]
    assert any(
        "unquoted sources: 5 of 6 tracked sources need a full read (limit 5)" in line
        for line in results.passes
    )


def test_snapshot_required_source_counts_even_when_quoted(tmp_path: Path) -> None:
    setup_repo(tmp_path)
    path = note(tmp_path, first_quoted_body(snapshot_required=True))

    fails = unquoted_fails(path, tmp_path)

    assert len(fails) == 1
    assert "6 distinct tracked sources" in fails[0]
    assert "src-1.ingest.md" in fails[0]


def test_note_citing_no_tracked_source_says_nothing(tmp_path: Path) -> None:
    setup_repo(tmp_path)
    write(tmp_path / "kb" / "notes" / "other-note.md", "A sibling note.\n")
    path = note(
        tmp_path,
        "This note only links a sibling [other note](./other-note.md).",
    )

    results = validate_note(path, repo_root=tmp_path)

    assert not any(
        "unquoted sources" in line
        for line in results.passes + results.warns + results.fails
    )


def test_quote_matching_only_ingest_analysis_does_not_discharge(tmp_path: Path) -> None:
    """Ties to the Quotes-section confinement: analysis prose is not support."""
    setup_repo(tmp_path, passage="an unrelated retained passage")
    ingest(
        tmp_path,
        "src-1",
        passage="an unrelated retained passage",
        summary=f"The author writes that {QUOTED_PASSAGE} is central.",
    )
    path = note(tmp_path, first_quoted_body())

    fails = unquoted_fails(path, tmp_path)

    assert len(fails) == 1
    assert "6 distinct tracked sources" in fails[0]
