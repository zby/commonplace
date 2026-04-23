from __future__ import annotations

import re
import sys
from pathlib import Path


SRC_ROOT = Path(__file__).resolve().parents[5] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.lib.extraction import link_audit  # noqa: E402


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def test_finds_all_links_when_no_pattern(tmp_path: Path) -> None:
    write(tmp_path / "a.md", "see [foo](./foo.md) and [bar](https://example.com)")

    found = link_audit.find_links(roots=[tmp_path])

    assert {f.url for f in found} == {"./foo.md", "https://example.com"}


def test_filters_by_substring_pattern(tmp_path: Path) -> None:
    write(tmp_path / "a.md", "[x](../sources/x.md) [y](../notes/y.md)")

    found = link_audit.find_links(roots=[tmp_path], url_pattern="../sources/")

    assert len(found) == 1
    assert found[0].url == "../sources/x.md"


def test_filters_by_regex_pattern(tmp_path: Path) -> None:
    write(tmp_path / "a.md", "[x](https://x.com) [y](http://y.org) [z](file://z)")

    found = link_audit.find_links(
        roots=[tmp_path], url_pattern=re.compile(r"^https?://")
    )

    assert len(found) == 2


def test_skips_backtick_matches_by_default(tmp_path: Path) -> None:
    write(
        tmp_path / "a.md",
        "real [link](./real.md) and `[fake](./fake.md)` example",
    )

    found = link_audit.find_links(roots=[tmp_path])

    assert len(found) == 1
    assert found[0].url == "./real.md"


def test_includes_backtick_matches_when_requested(tmp_path: Path) -> None:
    write(
        tmp_path / "a.md",
        "real [link](./real.md) and `[fake](./fake.md)` example",
    )

    found = link_audit.find_links(roots=[tmp_path], include_backtick_matches=True)

    assert {f.url for f in found} == {"./real.md", "./fake.md"}


def test_line_numbers_are_1_based(tmp_path: Path) -> None:
    write(tmp_path / "a.md", "line 1\nline 2 with [link](./foo.md)\n")

    found = link_audit.find_links(roots=[tmp_path])

    assert len(found) == 1
    assert found[0].line == 2


def test_captures_text_and_url(tmp_path: Path) -> None:
    write(tmp_path / "a.md", "[the title](https://example.com/path)")

    found = link_audit.find_links(roots=[tmp_path])

    assert found[0].text == "the title"
    assert found[0].url == "https://example.com/path"


def test_recurses_subdirectories(tmp_path: Path) -> None:
    write(tmp_path / "deep" / "nested.md", "[x](./x.md)")
    write(tmp_path / "shallow.md", "[y](./y.md)")

    found = link_audit.find_links(roots=[tmp_path])

    assert len(found) == 2


def test_skips_symlinks(tmp_path: Path) -> None:
    real = write(tmp_path / "real.md", "[real](./r.md)")
    link = tmp_path / "link.md"
    link.symlink_to(real)

    found = link_audit.find_links(roots=[tmp_path])

    assert len(found) == 1
    assert found[0].file == real
