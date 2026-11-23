from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib import index_generated
from commonplace.lib.index_generated import collect_tag_space
from commonplace.lib.validation import (
    TAG_README_HARD_BYTES,
    TAG_README_SOFT_BYTES,
    validate_note,
)
from tests.commonplace.validation_helpers import NOTE_TYPE_SPECS, copy_repo_files, write

pytestmark = pytest.mark.usefixtures("tmp_library")


def note(path: Path, tags: list[str]) -> Path:
    name = path.stem.replace("-", " ")
    return write(
        path,
        f"""---
description: {name}
type: types/note.md
tags: [{", ".join(tags)}]
---

# {name}
""",
    )


def tag_readme(
    path: Path,
    tag: str,
    *,
    marks: str = "",
    body: str = "",
) -> Path:
    return write(
        path,
        f"""---
description: "Curated head for {tag}"
type: types/tag-readme.md
{marks}---

# {tag}

Orientation paragraph.
{body}""",
    )


def setup_repo(tmp_path: Path, *, participating: str = "[notes]") -> Path:
    """A repo with a notes collection and a declared tag space; returns kb/tags."""
    copy_repo_files(
        tmp_path,
        "kb/types/tag-readme.md",
        "kb/types/tag-readme.schema.yaml",
        *NOTE_TYPE_SPECS,
    )
    write(tmp_path / "kb" / "notes" / "COLLECTION.md", "# Notes collection\n")
    write(
        tmp_path / "kb" / "tags" / "COLLECTION.md",
        f"---\nparticipating: {participating}\n---\n\n# Tags\n",
    )
    return tmp_path / "kb" / "tags"


@pytest.mark.parametrize("value", ["true", "false"])
def test_head_rejects_retired_complete_field(tmp_path: Path, value: str) -> None:
    tags = setup_repo(tmp_path)
    readme = tag_readme(tags / "topic-README.md", "topic", marks=f"complete: {value}\n")
    assert any("complete" in f for f in validate_note(readme, repo_root=tmp_path).fails)


def test_membership_ignores_undeclared_collections_and_the_proposal_archive(
    tmp_path: Path,
) -> None:
    tags = setup_repo(tmp_path, participating="[notes, reference]")
    write(tmp_path / "kb" / "reference" / "COLLECTION.md", "# Reference collection\n")
    write(tmp_path / "kb" / "work" / "COLLECTION.md", "# Work collection\n")
    note(tmp_path / "kb" / "work" / "draft.md", ["kb-design"])
    note(
        tmp_path / "kb" / "reference" / "proposals" / "archive" / "old.md",
        ["kb-design"],
    )
    note(tmp_path / "kb" / "notes" / "member.replaced.1.md", ["kb-design"])
    note(tmp_path / "kb" / "notes" / "member.md", ["kb-design"])
    readme = tag_readme(tags / "kb-design-README.md", "kb-design")
    assert not validate_note(readme, repo_root=tmp_path).fails
    members = collect_tag_space(tmp_path).notes_by_tag["kb-design"]
    assert [path for path, _, _ in members] == [tmp_path / "kb/notes/member.md"]


def test_head_outside_the_tag_collection_fails(tmp_path: Path) -> None:
    setup_repo(tmp_path)
    stray = tag_readme(tmp_path / "kb" / "notes" / "kb-design-README.md", "kb-design")

    results = validate_note(stray, repo_root=tmp_path)

    assert any(
        "tag head: a head is kb/tags/<tag>-README.md" in f for f in results.fails
    )


def test_validating_tagged_note_does_not_walk_member_collections(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    tags = setup_repo(tmp_path)
    tag_readme(tags / "topic-README.md", "topic")
    tagged = note(tmp_path / "kb/notes/tagged.md", ["topic"])
    note(tmp_path / "kb/notes/unrelated.md", ["topic"])

    def reject_walk(collection: Path) -> None:
        pytest.fail(f"checking a head must not enumerate members of {collection}")

    monkeypatch.setattr(index_generated, "iter_validation_markdown_files", reject_walk)
    results = validate_note(tagged, repo_root=tmp_path)
    assert not results.fails
    assert any("all 1 have heads" in p for p in results.passes)


def test_tagged_note_fails_without_a_head(tmp_path: Path) -> None:
    tags = setup_repo(tmp_path)
    tag_readme(tags / "kb-design-README.md", "kb-design")
    tagged = note(tmp_path / "kb" / "notes" / "tagged.md", ["kb-design", "orphan"])

    results = validate_note(tagged, repo_root=tmp_path)

    assert any(
        "tag `orphan`: no head at kb/tags/orphan-README.md" in f for f in results.fails
    )
    assert not any("kb-design" in f for f in results.fails)


def test_tagged_note_outside_the_tag_space_is_not_checked(tmp_path: Path) -> None:
    setup_repo(tmp_path)
    write(tmp_path / "kb" / "work" / "COLLECTION.md", "# Work collection\n")
    draft = note(tmp_path / "kb" / "work" / "draft.md", ["orphan"])

    results = validate_note(draft, repo_root=tmp_path)

    assert not any("no head" in f for f in results.fails)


def test_archived_proposal_in_a_participating_collection_is_not_checked(
    tmp_path: Path,
) -> None:
    setup_repo(tmp_path, participating="[notes, reference]")
    write(tmp_path / "kb" / "reference" / "COLLECTION.md", "# Reference collection\n")
    archived = note(
        tmp_path / "kb" / "reference" / "proposals" / "archive" / "old.md", ["orphan"]
    )

    results = validate_note(archived, repo_root=tmp_path)

    assert not any("no head" in f for f in results.fails)


def test_undeclared_tag_space_warns_instead_of_failing(tmp_path: Path) -> None:
    copy_repo_files(tmp_path, *NOTE_TYPE_SPECS)
    write(tmp_path / "kb" / "notes" / "COLLECTION.md", "# Notes collection\n")
    tagged = note(tmp_path / "kb" / "notes" / "tagged.md", ["kb-design"])

    results = validate_note(tagged, repo_root=tmp_path)

    assert not any("no head" in f for f in results.fails)
    assert any("tags unchecked" in w and "commonplace-init" in w for w in results.warns)


def test_weight_gates_warn_and_fail(tmp_path: Path) -> None:
    tags = setup_repo(tmp_path)
    filler_soft = "x" * (TAG_README_SOFT_BYTES + 100)
    soft = tag_readme(tags / "soft-README.md", "soft", body=f"\n{filler_soft}\n")
    filler_hard = "x" * (TAG_README_HARD_BYTES + 100)
    hard = tag_readme(tags / "hard-README.md", "hard", body=f"\n{filler_hard}\n")
    small = tag_readme(tags / "small-README.md", "small")

    soft_results = validate_note(soft, repo_root=tmp_path)
    hard_results = validate_note(hard, repo_root=tmp_path)
    small_results = validate_note(small, repo_root=tmp_path)

    assert any("weight gate" in w and "soft limit" in w for w in soft_results.warns)
    assert any("weight gate" in f and "hard limit" in f for f in hard_results.fails)
    assert any("weight gate" in p and "within" in p for p in small_results.passes)
