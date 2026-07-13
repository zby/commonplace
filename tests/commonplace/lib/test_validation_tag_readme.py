from __future__ import annotations

from pathlib import Path

from commonplace.lib.validation import (
    TAG_README_HARD_BYTES,
    TAG_README_SOFT_BYTES,
    validate_note,
)


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def note(path: Path, tags: list[str]) -> Path:
    name = path.stem.replace("-", " ")
    return write(
        path,
        f"""---
description: {name}
type: kb/types/note.md
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
type: kb/types/tag-readme.md
index_source: tag
index_key: {tag}
{marks}---

# {tag}

Orientation paragraph.
{body}""",
    )


def setup_repo(tmp_path: Path) -> Path:
    # The validator resolves the global type from kb/types/ in the repo root,
    # so the fixture repo needs the real specs copied in.
    real_types = Path(__file__).resolve().parents[3] / "kb" / "types"
    for name in (
        "tag-readme.md",
        "tag-readme.schema.yaml",
        "note.md",
        "note.schema.yaml",
        "note-base.schema.yaml",
        "type-spec.md",
        "type-spec.schema.yaml",
    ):
        write(tmp_path / "kb" / "types" / name, (real_types / name).read_text(encoding="utf-8"))
    write(tmp_path / "kb" / "notes" / "COLLECTION.md", "# Notes collection\n")
    return tmp_path / "kb" / "notes"


def test_complete_mark_fails_on_missing_member(tmp_path: Path) -> None:
    notes = setup_repo(tmp_path)
    note(notes / "linked-note.md", ["kb-design"])
    note(notes / "missing-note.md", ["kb-design"])
    readme = tag_readme(
        notes / "kb-design-README.md",
        "kb-design",
        marks="complete: true\n",
        body="\n## Picks\n\n- [linked note](./linked-note.md) — placed\n",
    )

    results = validate_note(readme, repo_root=tmp_path)

    assert any("complete mark: missing entry" in f and "missing-note.md" in f for f in results.fails)
    assert any("maintain-curated-indexes" in f for f in results.fails)


def test_complete_mark_passes_when_all_members_linked(tmp_path: Path) -> None:
    notes = setup_repo(tmp_path)
    note(notes / "linked-note.md", ["kb-design"])
    readme = tag_readme(
        notes / "kb-design-README.md",
        "kb-design",
        marks="complete: true\n",
        body="\n## Picks\n\n- [linked note](./linked-note.md) — placed\n",
    )

    results = validate_note(readme, repo_root=tmp_path)

    assert not results.fails
    assert any("complete mark: all 1 members linked" in p for p in results.passes)


def test_complete_mark_normalizes_edge_case_local_urls(tmp_path: Path) -> None:
    notes = setup_repo(tmp_path)
    note(notes / "linked note.md", ["kb-design"])
    readme = tag_readme(
        notes / "kb-design-README.md",
        "kb-design",
        marks="complete: true\n",
        body=(
            "\n## Picks\n\n"
            "- [linked note](./linked%20note.md?view=brief#details) — placed\n"
        ),
    )

    results = validate_note(readme, repo_root=tmp_path)

    assert not results.fails
    assert any("complete mark: all 1 members linked" in p for p in results.passes)


def test_weight_gates_warn_and_fail(tmp_path: Path) -> None:
    notes = setup_repo(tmp_path)
    filler_soft = "x" * (TAG_README_SOFT_BYTES + 100)
    soft = tag_readme(notes / "soft-README.md", "soft", body=f"\n{filler_soft}\n")
    filler_hard = "x" * (TAG_README_HARD_BYTES + 100)
    hard = tag_readme(notes / "hard-README.md", "hard", body=f"\n{filler_hard}\n")
    small = tag_readme(notes / "small-README.md", "small")

    soft_results = validate_note(soft, repo_root=tmp_path)
    hard_results = validate_note(hard, repo_root=tmp_path)
    small_results = validate_note(small, repo_root=tmp_path)

    assert any("weight gate" in w and "soft limit" in w for w in soft_results.warns)
    assert any("weight gate" in f and "hard limit" in f for f in hard_results.fails)
    assert any("weight gate" in p and "within" in p for p in small_results.passes)


def test_covered_by_fails_on_uncovered_note(tmp_path: Path) -> None:
    notes = setup_repo(tmp_path)
    note(notes / "covered-note.md", ["parent", "child-a"])
    note(notes / "uncovered-note.md", ["parent"])
    readme = tag_readme(
        notes / "parent-README.md",
        "parent",
        marks="covered_by: [child-a]\n",
    )

    results = validate_note(readme, repo_root=tmp_path)

    assert any("covered_by" in f and "uncovered-note.md" in f for f in results.fails)


def test_covered_by_passes_and_warns_on_fanout(tmp_path: Path) -> None:
    notes = setup_repo(tmp_path)
    note(notes / "covered-note.md", ["parent", "child-1"])
    children = ", ".join(f"child-{i}" for i in range(1, 9))
    readme = tag_readme(
        notes / "parent-README.md",
        "parent",
        marks=f"covered_by: [{children}]\n",
    )

    results = validate_note(readme, repo_root=tmp_path)

    assert not results.fails
    assert any("covered_by fan-out: 8 children" in w for w in results.warns)
    assert any("covered_by: all tagged notes" in p for p in results.passes)
