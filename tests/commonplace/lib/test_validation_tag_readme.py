from __future__ import annotations

from pathlib import Path

import pytest

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


def test_complete_mark_fails_on_missing_member(tmp_path: Path) -> None:
    tags = setup_repo(tmp_path)
    notes = tmp_path / "kb" / "notes"
    note(notes / "linked-note.md", ["kb-design"])
    note(notes / "missing-note.md", ["kb-design"])
    readme = tag_readme(
        tags / "kb-design-README.md",
        "kb-design",
        marks="complete: true\n",
        body="\n## Picks\n\n- [linked note](../notes/linked-note.md) — placed\n",
    )

    results = validate_note(readme, repo_root=tmp_path)

    assert any("complete mark: missing entry" in f and "missing-note.md" in f for f in results.fails)
    assert any("maintain-curated-indexes" in f for f in results.fails)


@pytest.mark.parametrize(
    ("filename", "link"),
    [
        ("linked-note.md", "../notes/linked-note.md"),
        # Percent-encoding, query, and fragment are normalized away.
        ("linked note.md", "../notes/linked%20note.md?view=brief#details"),
    ],
)
def test_complete_mark_passes_when_all_members_linked(
    tmp_path: Path, filename: str, link: str
) -> None:
    tags = setup_repo(tmp_path)
    note(tmp_path / "kb" / "notes" / filename, ["kb-design"])
    readme = tag_readme(
        tags / "kb-design-README.md",
        "kb-design",
        marks="complete: true\n",
        body=f"\n## Picks\n\n- [linked note]({link}) — placed\n",
    )

    results = validate_note(readme, repo_root=tmp_path)

    assert not results.fails
    assert any("complete mark: all 1 members linked" in p for p in results.passes)


def test_complete_mark_ranges_over_every_participating_collection(tmp_path: Path) -> None:
    tags = setup_repo(tmp_path, participating="[notes, reference]")
    write(tmp_path / "kb" / "reference" / "COLLECTION.md", "# Reference collection\n")
    note(tmp_path / "kb" / "notes" / "in-notes.md", ["kb-design"])
    note(tmp_path / "kb" / "reference" / "in-reference.md", ["kb-design"])
    readme = tag_readme(
        tags / "kb-design-README.md",
        "kb-design",
        marks="complete: true\n",
        body="\n- [in notes](../notes/in-notes.md) — placed\n",
    )

    results = validate_note(readme, repo_root=tmp_path)

    assert any("missing entry for kb/reference/in-reference.md" in f for f in results.fails)


def test_membership_ignores_undeclared_collections_and_the_proposal_archive(
    tmp_path: Path,
) -> None:
    tags = setup_repo(tmp_path, participating="[notes, reference]")
    write(tmp_path / "kb" / "reference" / "COLLECTION.md", "# Reference collection\n")
    write(tmp_path / "kb" / "work" / "COLLECTION.md", "# Work collection\n")
    note(tmp_path / "kb" / "work" / "draft.md", ["kb-design"])
    note(tmp_path / "kb" / "reference" / "proposals" / "archive" / "old.md", ["kb-design"])
    note(tmp_path / "kb" / "notes" / "member.md", ["kb-design"])
    readme = tag_readme(
        tags / "kb-design-README.md",
        "kb-design",
        marks="complete: true\n",
        body="\n- [member](../notes/member.md) — placed\n",
    )

    results = validate_note(readme, repo_root=tmp_path)

    assert not results.fails
    assert any("complete mark: all 1 members linked" in p for p in results.passes)


def test_head_outside_the_tag_collection_fails(tmp_path: Path) -> None:
    setup_repo(tmp_path)
    stray = tag_readme(tmp_path / "kb" / "notes" / "kb-design-README.md", "kb-design")

    results = validate_note(stray, repo_root=tmp_path)

    assert any("tag head: a head is kb/tags/<tag>-README.md" in f for f in results.fails)


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


def test_covered_by_fails_on_uncovered_note(tmp_path: Path) -> None:
    tags = setup_repo(tmp_path)
    notes = tmp_path / "kb" / "notes"
    note(notes / "covered-note.md", ["parent", "child-a"])
    note(notes / "uncovered-note.md", ["parent"])
    tag_readme(tags / "child-a-README.md", "child-a")
    readme = tag_readme(
        tags / "parent-README.md",
        "parent",
        marks="covered_by: [child-a]\n",
    )

    results = validate_note(readme, repo_root=tmp_path)

    assert any("covered_by" in f and "uncovered-note.md" in f for f in results.fails)


def test_covered_by_requires_a_head_per_child(tmp_path: Path) -> None:
    tags = setup_repo(tmp_path)
    note(tmp_path / "kb" / "notes" / "covered-note.md", ["parent", "child-a"])
    readme = tag_readme(
        tags / "parent-README.md",
        "parent",
        marks="covered_by: [child-a]\n",
    )

    results = validate_note(readme, repo_root=tmp_path)

    assert any("child `child-a` has no head" in f for f in results.fails)


def test_covered_by_passes_and_warns_on_fanout(tmp_path: Path) -> None:
    tags = setup_repo(tmp_path)
    note(tmp_path / "kb" / "notes" / "covered-note.md", ["parent", "child-1"])
    children = [f"child-{i}" for i in range(1, 9)]
    for child in children:
        tag_readme(tags / f"{child}-README.md", child)
    readme = tag_readme(
        tags / "parent-README.md",
        "parent",
        marks=f"covered_by: [{', '.join(children)}]\n",
    )

    results = validate_note(readme, repo_root=tmp_path)

    assert not results.fails
    assert any("covered_by fan-out: 8 children" in w for w in results.warns)
    assert any("covered_by: all tagged notes" in p for p in results.passes)
