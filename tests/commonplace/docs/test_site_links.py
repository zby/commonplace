"""Website link projection must precede ProperDocs's link validation.

Render through the real Page pipeline: testing a URL helper alone would miss
wrong processor priority, per-page context leakage, and suppressed diagnostics.
"""

from pathlib import Path

import pytest
from properdocs.config import load_config
from properdocs.structure.files import File, Files, InclusionLevel
from properdocs.structure.pages import Page

from commonplace.docs import properdocs_hooks

REVISION = "a" * 40


def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def config(root):
    write(root / "properdocs.yml", """site_name: Test
use_directory_urls: false
theme:
  name: null
  custom_dir: .
plugins: []
extra:
  repository_files_url: https://github.com/example/project/blob/main/
""")
    (root / "docs").mkdir()
    return load_config(config_file=str(root / "properdocs.yml"))


def render(cfg, uri, text, *, excluded=(), generated=()):
    docs = Path(cfg["docs_dir"])
    source = write(docs / uri, text)
    files = Files([
        File(path.relative_to(docs).as_posix(), str(docs), cfg["site_dir"], False,
             inclusion=InclusionLevel.EXCLUDED if path.relative_to(docs).as_posix() in excluded
             else InclusionLevel.INCLUDED)
        for path in docs.rglob("*") if path.is_file()
    ])
    cfg.plugins._current_plugin = None
    for name in generated:
        files.append(File.generated(cfg, name, content="# Generated\n"))
    page = Page(None, files.get_file_from_path(uri), cfg)
    page.read_source(cfg)
    page.markdown = properdocs_hooks.on_page_markdown(page.markdown, page, cfg, files=files)
    page.render(cfg, files)
    assert source.read_text(encoding="utf-8") == text
    return page.content


def test_checkout_links_project_to_repository_but_missing_links_still_warn(tmp_path, caplog):
    cfg = config(tmp_path)
    write(tmp_path / "src/a file.py", "pass\n")
    write(tmp_path / "docs/notes/other.md", "# Other\n")
    write(tmp_path / "docs/notes/evidence/raw.md", "# Captured\n")
    html = render(cfg, "notes/readme.md", """# Readme

[code](../../src/a%20file.py?raw=1#L1)
[page](other.md)
[canonical page](../../docs/notes/other.md)
[generated page](../../docs/notes/generated.md)
[evidence directory](evidence/)
[evidence](evidence/raw.md)
[missing](missing.md)

> [authored quote](also-missing.md)

`[example](../../src/a%20file.py)`

```markdown
[example](../../src/a%20file.py)
```
""", excluded=("notes/evidence/raw.md",), generated=("notes/generated.md",))
    assert 'href="https://github.com/example/project/blob/main/src/a%20file.py?raw=1#L1"' in html
    assert html.count('href="other.html"') == 2
    assert 'href="generated.html"' in html
    assert 'href="https://github.com/example/project/tree/main/docs/notes/evidence"' in html
    assert 'href="https://github.com/example/project/blob/main/docs/notes/evidence/raw.md"' in html
    assert 'href="missing.md"' in html and 'href="also-missing.md"' in html
    assert "missing.md" in caplog.text and "also-missing.md" in caplog.text
    assert "not found among documentation files" in caplog.text
    assert "[example](../../src/a%20file.py)" in html


def test_repository_links_do_not_follow_symlinks_outside_checkout(tmp_path):
    cfg = config(tmp_path)
    outside = write(tmp_path.parent / (tmp_path.name + "-outside.txt"), "outside\n")
    try:
        (tmp_path / "docs/escape.txt").symlink_to(outside)
    except (OSError, NotImplementedError) as exc:
        pytest.skip(f"Symlink creation unavailable: {exc}")
    html = render(cfg, "notes/page.md", "# Page\n\n[outside](../escape.txt)\n")
    assert 'href="../escape.txt"' in html
    assert "https://github.com/example/project" not in html


def test_pinned_quote_links_use_attributed_file_not_analysis_page(tmp_path, caplog):
    cfg = config(tmp_path)
    directory = Path(cfg["docs_dir"]) / "agentic-system-analyses/retained/example"
    write(directory / "boundary.md", f"""---
source:
  kind: git
  identity: https://github.com/upstream/system
  revision: {REVISION}
---
# Boundary
""")
    text = r"""# Analysis

> [first](guide.md)
> --- `docs/README.md`

> [**second**](../src/engine.py?view=1#L2)
> --- `docs/README.md`

> [unsafe](../../../outside.md)
> --- `docs/README.md`

> 3. **Read** the relevant pages.
> 4. **Synthesize** using [page](concepts/page.md).
> --- `skills/wiki/SKILL.md`

> Link template: \`*Source: [raw/filename.md](raw/filename.md)*\`
> --- `docs/README.md`

[author link](missing.md)
"""
    html = render(cfg, "agentic-system-analyses/retained/example/memory.md", text)
    assert f'href="https://github.com/upstream/system/blob/{REVISION}/docs/guide.md"' in html
    assert f'href="https://github.com/upstream/system/blob/{REVISION}/src/engine.py?view=1#L2"' in html
    assert 'unsafe (<code>../../../outside.md</code>)' in html
    assert 'href="../../../outside.md"' not in html
    assert f'href="https://github.com/upstream/system/blob/{REVISION}/skills/wiki/concepts/page.md"' in html
    assert f'href="https://github.com/upstream/system/blob/{REVISION}/docs/raw/filename.md"' in html
    assert "guide.md'" not in caplog.text
    assert "missing.md" in caplog.text

    # The config is reused by ProperDocs, but its source pin must not leak.
    html = render(cfg, "notes/next.md", "# Next\n\n> [local](guide.md)\n")
    assert 'href="guide.md"' in html
    assert "upstream/system" not in html


def test_capture_without_reliable_source_file_keeps_link_literal(tmp_path, caplog):
    cfg = config(tmp_path)
    directory = Path(cfg["docs_dir"]) / "agentic-system-analyses/retained/paper"
    write(directory / "boundary.md", """---
source:
  kind: capture
  identity: https://arxiv.org/abs/1234.56789
  path: /local/paper.txt
---
# Boundary
""")
    html = render(cfg, "agentic-system-analyses/retained/paper/memory.md", """# Paper

> [a **formatted** label](wiki/pattern-name.md?q=1&mode=2#part).
> --- `/local/paper.txt`

> [not attributed](missing.md)
""")
    assert 'a <strong>formatted</strong> label (<code>wiki/pattern-name.md?q=1&amp;mode=2#part</code>)' in html
    assert 'href="wiki/' not in html
    assert "wiki/pattern-name" not in caplog.text
    assert 'href="missing.md"' in html and "missing.md" in caplog.text


def test_web_ingest_quotes_resolve_only_with_paired_capture_identity(tmp_path):
    cfg = config(tmp_path)
    checksum = "b" * 64
    html = render(cfg, "sources/paper.ingest.md", f"""---
type: types/ingest-report.md
source: https://example.org/papers/paper/index.html
snapshot_sha256: {checksum}
---
# Paper

> [feature](features/index.html?featureId=3) and [section](#section).
> --- `kb/sources/.snapshots/paper.md` @ `sha256:{checksum}`

> [uncertain](other.html)
> --- `kb/sources/.snapshots/another.md` @ `sha256:{checksum}`
""")
    assert 'href="https://example.org/papers/paper/features/index.html?featureId=3"' in html
    assert 'href="https://example.org/papers/paper/index.html#section"' in html
    assert 'uncertain (<code>other.html</code>)' in html
    assert 'href="other.html"' not in html


def test_repository_projection_is_explicit_and_does_not_require_git(tmp_path, caplog):
    cfg = config(tmp_path)
    cfg["extra"] = {}
    write(tmp_path / "src/code.py", "pass\n")
    html = render(cfg, "notes/test.md", "# Test\n\n[code](../../src/code.py)\n")
    assert 'href="../../src/code.py"' in html
    assert "not found among documentation files" in caplog.text
