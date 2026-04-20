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
status: seedling
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
    assert "Text files: 2 | Seedlings: 1" in report
    assert "- [Raw capture](../notes/raw-capture.md) - **1 links in**" in report
    assert "Sources: [Seedling note](../notes/seedling.md)" in report
    assert "- [Ignored](../notes/ignored.md) - **0 links in**" in report
