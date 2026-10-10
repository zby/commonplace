"""The tag space (ADR 089): declaration, heads, membership scope, drift guard."""

from __future__ import annotations

import re
from pathlib import Path

from commonplace.lib import index_generated
from commonplace.lib.project_paths import is_proposal_archive, is_replaced_archive
from tests.commonplace.validation_helpers import REPO_ROOT, write


def test_participating_declaration_is_read_and_checked(tmp_path: Path) -> None:
    write(tmp_path / "kb" / "notes" / "COLLECTION.md", "# Notes\n")
    write(
        tmp_path / "kb" / "tags" / "COLLECTION.md",
        "---\nparticipating: [notes, missing, tags]\n---\n\n# Tags\n",
    )

    participating, error = index_generated.read_participating(tmp_path)

    assert participating == ((tmp_path / "kb" / "notes").resolve(),)
    assert error is not None
    assert "`missing` is not a collection" in error
    assert "`tags` holds the heads" in error


def test_heads_are_identified_by_filename_only(tmp_path: Path) -> None:
    tags = tmp_path / "kb" / "tags"
    write(tags / "COLLECTION.md", "---\nparticipating: []\n---\n")
    write(tags / "README.md", "# Tags\n")
    write(tags / "x-README.md", "---\ndescription: x\ntype: types/tag-readme.md\n---\n\n# x\n")
    write(tags / "notes.md", "# not a head\n")

    heads = index_generated.collect_heads(tmp_path)

    assert set(heads) == {"x"}
    assert index_generated.tag_for_head(tags / "README.md") is None
    assert index_generated.tag_for_head(tags / "-README.md") is None


# ---------------------------------------------------------------------------
# Drift guard over this checkout: every collection that tags anything is either
# declared participating or deliberately outside the tag space. A new
# collection that starts tagging without a declaration fails here rather than
# silently falsifying a mark.

OUTSIDE_TAG_SPACE = frozenset({"work", "sources", "reports", "types", "articles", "tags"})
TAGS_LINE = re.compile(r"^tags: \[[^\]]+\]", re.MULTILINE)


def _collections_that_tag(kb: Path) -> set[str]:
    found: set[str] = set()
    for collection in sorted(kb.iterdir()):
        if not (collection / "COLLECTION.md").is_file():
            continue
        for path in collection.rglob("*.md"):
            if is_replaced_archive(path) or is_proposal_archive(path):
                continue
            if "types" in path.relative_to(collection).parts:
                continue
            if TAGS_LINE.search(path.read_text(encoding="utf-8", errors="ignore")):
                found.add(collection.name)
                break
    return found


def test_checkout_declares_every_tagging_collection() -> None:
    participating, error = index_generated.read_participating(REPO_ROOT)
    assert error is None, error
    declared = {path.name for path in participating}

    undeclared = _collections_that_tag(REPO_ROOT / "kb") - declared - OUTSIDE_TAG_SPACE

    assert undeclared == set(), (
        f"collections tagging artifacts with no participation decision: {sorted(undeclared)}"
    )
