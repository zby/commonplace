"""The role report's inbound contexts, collected from files without a model."""
from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib.review_workflows import inbound

NOTE = "kb/theory/alpha.md"


def write(root: Path, rel: str, body: str, description: str = "A linking note") -> None:
    path = root / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(f"---\ndescription: {description}\n---\n\n{body}", encoding="utf-8")


@pytest.fixture
def root(tmp_path):
    write(tmp_path, NOTE, "# Alpha\n\nSee [itself](./alpha.md).\n")
    return tmp_path


def test_finds_each_passage_that_links_to_the_note(root):
    write(root, "kb/theory/beta.md", (
        "# Beta\n\nA paragraph before.\n\nIt rests on [alpha](./alpha.md#claim)\nand continues here.\n\n"
        "- [Alpha](./alpha.md) — grounds: the term\n  wraps onto a second line.\n- An unrelated item.\n\n"
        "| Note | Use |\n|---|---|\n| [alpha](alpha.md) | the pair |\n| other | none |\n\n"
        "## About [alpha](./alpha.md)\n\n```\n[in code](./alpha.md)\n```\n"))
    write(root, "kb/tags/theory-README.md", "# Theory\n\n- [Alpha](../theory/alpha.md) — a tag entry\n")
    [tag, beta] = inbound.linking(root, NOTE)
    assert (beta.path, beta.title, beta.description) == ("kb/theory/beta.md", "Beta", "A linking note")
    assert beta.passages == ("It rests on [alpha](./alpha.md#claim)\nand continues here.",
                             "- [Alpha](./alpha.md) — grounds: the term\n  wraps onto a second line.",
                             "| [alpha](alpha.md) | the pair |",
                             "## About [alpha](./alpha.md)")
    assert tag.path == "kb/tags/theory-README.md"
    text = inbound.collect(root, NOTE)
    assert "2 file(s) link to this note" in text and "An unrelated item" not in text and "in code" not in text
    assert "> - [Alpha](./alpha.md) — grounds: the term\n>   wraps onto a second line." in text


def test_excludes_reports_work_hidden_directories_and_the_note_itself(root):
    for rel in ("kb/reports/state/x.md", "kb/work/draft/x.md", "kb/sources/.snapshots/x.md"):
        write(root, rel, "# X\n\n[Alpha](../../theory/alpha.md) and [alpha](../../../theory/alpha.md)\n")
    write(root, "kb/theory/gamma.md", "# Gamma\n\n[Another](./alpha-two.md) names a similar file.\n")
    assert inbound.linking(root, NOTE) == []


def test_no_inbound_links_says_so(root):
    text = inbound.collect(root, NOTE)
    assert text.startswith(f"# Inbound contexts of `{NOTE}`") and "No file links to this note" in text


def test_caps_cut_files_passages_and_long_passages_and_say_so(root, monkeypatch):
    monkeypatch.setattr(inbound, "MAX_LINKING_FILES", 2)
    monkeypatch.setattr(inbound, "MAX_PASSAGES_PER_FILE", 1)
    monkeypatch.setattr(inbound, "MAX_PASSAGE_CHARS", 40)
    for name in ("a", "b", "c"):
        write(root, f"kb/theory/{name}.md", f"# {name}\n\n[Alpha](./alpha.md) {'word ' * 20}\n\n"
                                            "Second [link](./alpha.md).\n")
    text = inbound.collect(root, NOTE)
    assert "3 file(s) link to this note" in text and "1 more were cut" in text
    assert "kb/theory/b.md" in text and "kb/theory/c.md" not in text
    assert text.count("[cut at 40 characters]") == 2 and "Second" not in text
    assert text.count("Only the first 1 passages are shown; 1 more were cut.") == 2
