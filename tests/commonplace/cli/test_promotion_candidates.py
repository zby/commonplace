from __future__ import annotations

from pathlib import Path

from commonplace.cli import promotion_candidates


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_promotion_candidates_uses_shared_markdown_parsing(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    notes_root = tmp_path / "kb" / "notes"
    reports_root = tmp_path / "kb" / "reports"
    write(notes_root / "COLLECTION.md", "# Notes collection\n")

    write(
        notes_root / "raw-capture.md",
        """# Raw capture

Unstructured note.
""",
    )
    write(
        notes_root / "ignored.md",
        """# Ignored

Only linked from code regions.
""",
    )
    write(
        notes_root / "seedling.md",
        """---
description: Seedling note linking to the raw capture and mentioning another file only inside code
type: kb/types/note.md
traits: []
---

# Seedling note

Real link: [raw](./raw-capture.md)

`[ignored-inline](./ignored.md)`

```md
[ignored-fenced](./ignored.md)
```
""",
    )

    monkeypatch.chdir(tmp_path)

    promotion_candidates.main()

    captured = capsys.readouterr()
    assert "Wrote" in captured.out

    report = (reports_root / "promotion-candidates.md").read_text(encoding="utf-8")
    assert "Unstructured text files: 2" in report
    assert "Seedling -> Current" not in report
    assert "Orphan Seedlings" not in report
    assert "- [Raw capture](../notes/raw-capture.md) - **1 links in**" in report
    assert "Sources: [Seedling note](../notes/seedling.md)" in report
    assert "- [Ignored](../notes/ignored.md) - **0 links in**" in report
    assert "## Invalid frontmatter" in report
    assert "No invalid frontmatter found." in report


def test_promotion_candidates_reports_invalid_frontmatter_separately(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    notes_root = tmp_path / "kb" / "notes"
    write(notes_root / "COLLECTION.md", "# Notes collection\n")
    write(notes_root / "raw.md", "# Raw\n\nUnstructured capture.\n")
    write(
        notes_root / "invalid-yaml.md",
        """---
description: [unterminated
---

# Invalid YAML
""",
    )
    write(
        notes_root / "missing-close.md",
        """---
description: Missing closing delimiter

# Missing close
""",
    )
    monkeypatch.chdir(tmp_path)

    exit_code = promotion_candidates.main()

    captured = capsys.readouterr()
    assert exit_code == 0
    assert "1 unstructured text files, 2 invalid frontmatter files" in captured.out

    report = (tmp_path / "kb" / "reports" / "promotion-candidates.md").read_text(
        encoding="utf-8"
    )
    assert "Unstructured text files: 1" in report
    assert "- [Raw](../notes/raw.md)" in report
    assert "## Invalid frontmatter" in report
    assert "- [Invalid YAML](../notes/invalid-yaml.md)" in report
    assert "- [Missing close](../notes/missing-close.md)" in report
    assert "frontmatter: missing closing delimiter" in report
