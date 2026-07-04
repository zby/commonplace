from __future__ import annotations

import re
import sys
from pathlib import Path

import pytest


SRC_ROOT = Path(__file__).resolve().parents[5] / "src"
if str(SRC_ROOT) not in sys.path:
    sys.path.insert(0, str(SRC_ROOT))

from commonplace.lib.extraction import link_audit  # noqa: E402


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


@pytest.mark.parametrize(
    ("content", "options", "expected_urls"),
    [
        (
            "see [foo](./foo.md) and [bar](https://example.com)",
            {},
            ("./foo.md", "https://example.com"),
        ),
        (
            "[x](../sources/x.md) [y](../notes/y.md)",
            {"url_pattern": "../sources/"},
            ("../sources/x.md",),
        ),
        (
            "[x](https://x.com) [y](http://y.org) [z](file://z)",
            {"url_pattern": re.compile(r"^https?://")},
            ("https://x.com", "http://y.org"),
        ),
        (
            "real [link](./real.md) and `[fake](./fake.md)` example",
            {},
            ("./real.md",),
        ),
        (
            "real [link](./real.md) and `[fake](./fake.md)` example",
            {"include_backtick_matches": True},
            ("./real.md", "./fake.md"),
        ),
    ],
)
def test_find_links_filters_and_backtick_handling(
    tmp_path: Path,
    content: str,
    options: dict,
    expected_urls: tuple[str, ...],
) -> None:
    write(tmp_path / "a.md", content)

    found = link_audit.find_links(roots=[tmp_path], **options)

    assert tuple(item.url for item in found) == expected_urls


def test_occurrences_include_file_line_text_and_url(tmp_path: Path) -> None:
    path = write(tmp_path / "a.md", "line 1\nline 2 with [the title](https://example.com/path)\n")

    found = link_audit.find_links(roots=[tmp_path])

    assert [(item.file, item.line, item.text, item.url) for item in found] == [
        (path, 2, "the title", "https://example.com/path")
    ]


def test_recurses_subdirectories(tmp_path: Path) -> None:
    write(tmp_path / "deep" / "nested.md", "[x](./x.md)")
    write(tmp_path / "shallow.md", "[y](./y.md)")

    found = link_audit.find_links(roots=[tmp_path])

    assert len(found) == 2


def test_skips_symlinks(tmp_path: Path) -> None:
    real = write(tmp_path / "real.md", "[real](./r.md)")
    link = tmp_path / "link.md"
    try:
        link.symlink_to(real)
    except OSError:
        pytest.skip("cannot create symlinks on this platform")

    found = link_audit.find_links(roots=[tmp_path])

    assert len(found) == 1
    assert found[0].file == real
