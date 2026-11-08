"""Source scope must survive Markdown's structural merging and URL spelling."""

import logging
import re

import pytest
from test_site_links import REVISION, config, render, write

BASE = f"https://github.com/upstream/system/blob/{REVISION}/docs/README.md"


@pytest.mark.parametrize("quoted, expected", [
    (
        f"> [first](a.md)\n> --- {BASE}\n> [second](b.md)\n> --- {BASE}\n",
        ("docs/a.md", "docs/b.md"),
    ),
    (f"> [link](guide.md)\n> ----- {BASE}\n", ("docs/guide.md",)),
    (
        f"> outer source prose\n>\n> > [nested](guide.md)\n>\n> --- {BASE}\n",
        ("docs/guide.md",),
    ),
    (f"> [reference][g]\n> --- {BASE}\n\n[g]: guide.md\n", ("docs/guide.md",)),
])
def test_supported_quote_shapes_keep_exact_source_scope(tmp_path, caplog, quoted, expected):
    cfg = config(tmp_path)
    html = render(cfg, "notes/page.md", "# Page\n\n> [before](missing-before.md)\n\n" + quoted
                  + "\n> [after](missing-after.md)\n\n[authored](missing.md)\n")
    for path in expected:
        assert f'href="https://github.com/upstream/system/blob/{REVISION}/{path}"' in html
    assert 'href="missing-before.md"' in html
    assert 'href="missing-after.md"' in html
    assert 'href="missing.md"' in html
    assert "missing-before.md" in caplog.text and "missing-after.md" in caplog.text
    assert not re.search(r"CP[0-9a-f]{32}(?:BEGIN|END)", html)


@pytest.mark.parametrize("href", [
    "../../../outside.md",
    "%2e%2e/%2e%2e/other/file.md",
    ".%2E/%2E./other.md",
    r"..\..\other.md",
    "..%5c..%5cother.md",
    "%2e%2e%2f%2e%2e/other.md",
    "/guide.md",
])
def test_external_paths_cannot_escape_pin_or_become_site_navigation(tmp_path, href):
    cfg = config(tmp_path)
    html = render(cfg, "notes/page.md", f"# Page\n\n> [quoted]({href})\n> --- {BASE}\n")
    assert 'class="quoted-source-link"' in html
    # Markdown consumes escapes such as \\. before handing us the link target.
    visible_target = href.replace(r"\.", ".")
    assert f"<code>{visible_target}</code>" in html
    assert 'href=' not in html


def test_unknown_source_root_is_literal_but_authored_site_root_is_untouched(tmp_path):
    cfg = config(tmp_path)
    html = render(cfg, "notes/page.md", """# Page

> [quoted](/guide.md)
> --- https://github.com/upstream/system

[authored](/site.md)
""")
    assert "quoted (<code>/guide.md</code>)" in html
    assert 'href="/site.md"' in html
    assert 'href="/guide.md"' not in html


def test_invalid_authored_and_quoted_urls_keep_properdocs_diagnostic(tmp_path, caplog):
    caplog.set_level(logging.INFO, logger="properdocs.structure.pages")
    cfg = config(tmp_path)
    html = render(cfg, "notes/page.md", f"""# Page

[bad](http://[broken)

> [quoted bad](http://[also-broken)
> --- {BASE}
""")
    assert 'href="http://[broken"' in html
    assert 'href="http://[also-broken"' in html
    assert caplog.text.count("contains an invalid link") == 2


@pytest.mark.parametrize("source", [BASE, "https://github.com/upstream/system"])
def test_attribution_annotations_remain_authored_navigation(tmp_path, caplog, source):
    cfg = config(tmp_path)
    write(tmp_path / "src/check.py", "pass\n")
    html = render(cfg, "notes/page.md", f"""# Page

> [quoted](guide.md)
> --- [source]({source}); [verification](missing-verification.md); [code](../../src/check.py)
""")
    if source == BASE:
        assert f'href="https://github.com/upstream/system/blob/{REVISION}/docs/guide.md"' in html
    else:
        assert "quoted (<code>guide.md</code>)" in html
    assert 'href="missing-verification.md"' in html
    assert "missing-verification.md" in caplog.text
    assert 'href="https://github.com/example/project/blob/main/src/check.py"' in html


def test_markers_do_not_leak_from_unclosed_source_fence(tmp_path):
    cfg = config(tmp_path)
    html = render(cfg, "notes/page.md", f"""# Page

> ```
> [example](guide.md)
> --- {BASE}
""")
    assert not re.search(r"CP[0-9a-f]{32}(?:BEGIN|END)", html)
