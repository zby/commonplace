from __future__ import annotations

from pathlib import Path
from types import SimpleNamespace

import pytest
from properdocs.config import load_config
from properdocs.structure.files import File, Files, InclusionLevel
from properdocs.structure.pages import Page

from commonplace.docs import properdocs_hooks

# Imported at collection: the fixture module reads the real library's layout when first imported.
from tests.commonplace.agentic_analysis.fixtures import retained_fixture


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def tag_space(root: Path) -> Path:
    tags = root / "kb" / "tags"
    write(tags / "COLLECTION.md", "# Tags\n")
    return tags


def head(tags: Path, tag: str) -> Path:
    return write(
        tags / f"{tag}-README.md",
        f"""---
description: "Curated head for {tag}"
type: types/tag-readme.md
---

# {tag}
""",
    )


def test_on_page_markdown_renders_user_verification_and_specialized_status(tmp_path: Path) -> None:
    note = write(tmp_path / "kb" / "reference" / "adr" / "044-example.md", "# Example\n")
    page = SimpleNamespace(
        meta={
            "type": "reference/types/adr.md",
            "status": "accepted",
            "user-verified": True,
        },
        file=SimpleNamespace(abs_src_path=str(note)),
    )

    result = properdocs_hooks.on_page_markdown("# Example\n\nBody\n", page)

    assert "**Status:** accepted" in result
    assert "**User verified:** yes" in result


def test_on_files_detaches_tag_members_in_both_site_formats(tmp_path: Path) -> None:
    notes = tmp_path / "kb" / "notes"
    reference = tmp_path / "kb" / "reference"
    write(notes / "COLLECTION.md", "# Notes collection\n")
    write(reference / "COLLECTION.md", "# Reference collection\n")
    tags = tag_space(tmp_path)
    readme = head(tags, "kb-design")
    write(
        notes / "tagged.md",
        """---
description: Tagged note
type: types/note.md
tags: [kb-design]
---

# Tagged note
""",
    )
    write(
        reference / "doc.md",
        """---
description: Reference doc
type: types/note.md
tags: [kb-design]
---

# Reference doc
""",
    )
    write(
        notes / "curated.md",
        """---
description: Already curated note
type: types/note.md
tags: [kb-design]
---

# Curated note
""",
    )
    from properdocs_site_assets import on_env

    readme.write_text(readme.read_text() + "\n[Curated note](../notes/curated.md)\n")
    head(notes, "stray")
    empty = head(tags, "empty")
    docs = tmp_path / "kb"
    cfg = write(tmp_path / "properdocs.yml", "site_name: Test\ndocs_dir: kb\nplugins: []\n"
                "theme: {name: null, custom_dir: .}\nuse_directory_urls: false\nsite_url: https://example.org/project/\n")
    config = load_config(config_file=str(cfg))
    config.plugins._current_plugin = None
    files = Files([File(p.relative_to(docs).as_posix(), str(docs), config.site_dir, False)
                   for p in docs.rglob("*.md")])
    properdocs_hooks.on_files(files, config)
    on_env(None, config, files)
    site = Path(config.site_dir) / "tags"
    guide = (site / readme.name).read_text()
    assert "[All 3 tagged artifacts](./kb-design-members.md) — 2 notes, 1 reference" in guide
    assert "tagged.md" not in guide and guide.startswith(readme.read_text())
    assert "members.md" not in readme.read_text()
    assert "members.md" not in (site.parent / "notes/stray-README.md").read_text()
    assert not (site / "stray-members.md").exists()
    listing = (site / "kb-design-members.md").read_text()
    assert "[Back to the kb-design guide](./kb-design-README.md)" in listing
    assert "[notes](#notes)" in listing
    notes_group, reference_group = listing.split("## notes\n")[1].split("## reference\n")
    assert "curated.md" in notes_group and "tagged.md" in notes_group
    assert "doc.md" in reference_group
    assert "[All 0 tagged artifacts](./empty-members.md)" in (site / empty.name).read_text()
    assert "No tagged artifacts." in (site / "empty-members.md").read_text()
    for uri, href in ((readme.name, "kb-design-members.html"), ("kb-design-members.md", readme.stem + ".html")):
        page = Page(None, files.get_file_from_path("tags/" + uri), config)
        page.read_source(config)
        page.markdown = properdocs_hooks.on_page_markdown(page.markdown, page, config, files=files)
        page.render(config, files)
        assert f'href="{href}"' in page.content


def test_on_files_publishes_source_index_with_only_published_pages(tmp_path: Path) -> None:
    class Config(dict):
        def __init__(self, docs_dir: Path, site_dir: Path) -> None:
            super().__init__(docs_dir=str(docs_dir))
            self.site_dir = str(site_dir)
            self.use_directory_urls = True
            self.plugins = SimpleNamespace(_current_plugin="test")

    docs_dir = tmp_path / "kb"
    sources = docs_dir / "sources"
    readme = write(sources / "README.md", "# Sources\n")
    collection = write(sources / "COLLECTION.md", "# Sources collection\n")
    ingest = write(sources / "published.ingest.md", "# Published ingest\n")
    snapshot = write(sources / "excluded.md", "# Excluded snapshot\n")
    config = Config(docs_dir, tmp_path / "site")

    def source_file(path: Path, inclusion: InclusionLevel) -> File:
        return File(
            path.relative_to(docs_dir).as_posix(),
            str(docs_dir),
            config.site_dir,
            config.use_directory_urls,
            inclusion=inclusion,
        )

    files = Files(
        [
            source_file(readme, InclusionLevel.INCLUDED),
            source_file(collection, InclusionLevel.INCLUDED),
            source_file(ingest, InclusionLevel.INCLUDED),
            source_file(snapshot, InclusionLevel.EXCLUDED),
        ]
    )

    properdocs_hooks.on_files(files, config)
    generated = files.get_file_from_path("sources/dir-index.md")
    rendered_readme = files.get_file_from_path("sources/README.md").content_string

    assert generated is not None
    assert generated.inclusion is InclusionLevel.INCLUDED
    assert "Published ingest" in generated.content_string
    assert "Excluded snapshot" not in generated.content_string
    assert "[Complete file listing](./dir-index.md)" in rendered_readme


def test_on_page_markdown_keeps_headless_tags_as_text(tmp_path: Path) -> None:
    notes = tmp_path / "kb" / "notes"
    write(notes / "COLLECTION.md", "# Notes collection\n")
    head(tag_space(tmp_path), "learning-theory")
    note = write(notes / "example.md", "# Example\n")
    page = SimpleNamespace(
        meta={
            "type": "types/note.md",
            "tags": ["context-engineering", "learning-theory"],
        },
        file=SimpleNamespace(abs_src_path=str(note)),
    )
    properdocs_hooks.on_config({"docs_dir": str(tmp_path / "kb")})

    result = properdocs_hooks.on_page_markdown(
        "# Example\n\nBody\n", page, config={"docs_dir": str(tmp_path / "kb")}
    )

    assert "**Tags:** context-engineering, [learning-theory](../tags/learning-theory-README.md)" in result


def test_on_page_markdown_keeps_backslashes_in_badge_values(tmp_path: Path) -> None:
    note = write(tmp_path / "kb" / "notes" / "example.md", "# Example\n")
    page = SimpleNamespace(meta={"status": r"draft \1 C:\local"}, file=SimpleNamespace(abs_src_path=str(note)))

    result = properdocs_hooks.on_page_markdown("# Example\n\nBody\n", page)

    assert "# Example\n\n**Status:** draft \\1 C:\\local\n" in result


def test_site_current_list_matches_comparison_population(tmp_path: Path, tmp_library) -> None:
    from commonplace.lib.systems_matrix import load_results
    retained_fixture(tmp_path)
    docs_dir = tmp_path / "kb"
    readme = write(docs_dir / "agentic-system-analyses/README.md", "# Analyses\n")
    class Config(dict):
        site_dir = str(tmp_path / "site")
        use_directory_urls = False
        plugins = SimpleNamespace(_current_plugin="test")
    config = Config(docs_dir=str(docs_dir))
    files = Files([File("agentic-system-analyses/README.md", str(docs_dir), config.site_dir,
                       False, inclusion=InclusionLevel.INCLUDED)])
    properdocs_hooks.on_files(files, config)
    listing = files.get_file_from_path("agentic-system-analyses/current-analyses.md")
    assert listing is not None
    row = load_results(tmp_path).rows[0]
    assert row["analysis_run"] in listing.content_string
    assert "[Example System](retained/example-system/overview.md)" in listing.content_string
    assert not (readme.parent / "current-analyses.md").exists()
    assert "current-analyses.md" in files.get_file_from_path("agentic-system-analyses/README.md").content_string


def test_on_config_groups_agentic_systems_and_hides_unlisted_collections(tmp_path: Path) -> None:
    docs_dir = tmp_path / "kb"
    for collection in ("agent-memory-systems", "agentic-system-analyses", "agentic-systems", "notes", "types"):
        write(docs_dir / collection / "README.md", f"# {collection}\n")
    for path in ("topics/README.md", "comparisons/README.md", "methods.md",
                 "comparisons/memory/README.md"):
        write(docs_dir / "agentic-systems" / path, "# Research\n")

    nav = properdocs_hooks.on_config({"docs_dir": str(docs_dir)})["nav"]

    assert {"Agentic Systems": [
        {"Overview": "agentic-systems/README.md"},
        {"Research Topics": "agentic-systems/topics/README.md"},
        {"Comparisons": "agentic-systems/comparisons/README.md"},
        {"Systems Directory": "agentic-system-analyses/current-analyses.md"},
        {"Methods & Data": "agentic-systems/methods.md"},
    ]} in nav
    labels = [next(iter(entry)) for entry in nav]
    assert "Agent Memory Systems" not in labels
    assert "Agentic System Analyses" not in labels
    assert "Types" not in labels
    assert "Recent Changes" not in labels
    assert labels.count("Agentic Systems") == 1
    assert {"Notes": "notes/README.md"} in nav
    assert labels.index("Agentic Systems") < labels.index("Notes")
    # Every public destination is authored or is the existing generated directory.
    for entry in next(entry["Agentic Systems"] for entry in nav if "Agentic Systems" in entry):
        target = next(iter(entry.values()))
        assert target.endswith("current-analyses.md") or (docs_dir / target).is_file()


def test_lens_listing_links_each_current_member(tmp_path: Path, tmp_library) -> None:
    retained_fixture(tmp_path)
    docs_dir = tmp_path / "kb"
    write(docs_dir / "agentic-system-analyses/README.md", "# Analyses\n")
    readme = write(docs_dir / "agentic-systems/comparisons/memory/README.md", "# Memory lens\n")
    class Config(dict):
        site_dir = str(tmp_path / "site")
        use_directory_urls = False
        plugins = SimpleNamespace(_current_plugin="test")
    config = Config(docs_dir=str(docs_dir))
    uri = readme.relative_to(docs_dir).as_posix()
    files = Files([File(uri, str(docs_dir), config.site_dir, False)])
    properdocs_hooks.on_files(files, config)

    listing = files.get_file_from_path("agentic-systems/comparisons/memory/systems.md").content_string
    member = "../../../agentic-system-analyses/retained/example-system/"
    assert f"]({member}memory.md)" in listing
    assert f"[profile]({member}memory-profile.md)" in listing
    assert files.get_file_from_path("agentic-systems/comparisons/runtime/systems.md") is None
    assert "[Current analyses](./systems.md)" in files.get_file_from_path(uri).content_string


@pytest.mark.parametrize("collection", ["reports", "work", "agentic-systems"])
def test_on_files_leaves_marked_subtrees_off_the_site(tmp_path: Path, collection: str) -> None:
    docs_dir = tmp_path / "kb"
    trial = docs_dir / collection / "retained/trial"
    report = write(trial / "README.md", "# Trial\n")
    capture = write(trial / "captures/nested/out.md", "# Captured content\n")
    asset = write(trial / "captures/nested/raw.txt", "Raw capture\n")
    write(trial / "captures/.commonplace-validation-ignore", "")
    note = write(docs_dir / "notes/n.md", "# N\n")
    write(docs_dir / collection / "COLLECTION.md", "# Collection\n")
    copied = docs_dir / "workflow-state/data/current/bundle/kb/notes"
    write(copied / "COLLECTION.md", "# Copied notes\n")
    write(copied / "README.md", "# Copied notes\n")
    class Config(dict):
        site_dir = str(tmp_path / "site")
        use_directory_urls = False
        plugins = SimpleNamespace(_current_plugin="test")
    config = Config(docs_dir=str(docs_dir))
    files = Files([File(p.relative_to(docs_dir).as_posix(), str(docs_dir), config.site_dir, False,
                        inclusion=InclusionLevel.INCLUDED) for p in (report, capture, asset, note)])
    virtual_uri = f"{collection}/retained/trial/captures/generated.md"
    files.append(File.generated(config, virtual_uri, content="# Generated capture\n",
                                inclusion=InclusionLevel.INCLUDED))

    properdocs_hooks.on_files(files, config)

    inclusion = {f.src_uri: f.inclusion for f in files}
    assert inclusion[f"{collection}/retained/trial/README.md"] is InclusionLevel.INCLUDED
    assert inclusion[f"{collection}/retained/trial/captures/nested/out.md"] is InclusionLevel.EXCLUDED
    assert inclusion[f"{collection}/retained/trial/captures/nested/raw.txt"] is InclusionLevel.EXCLUDED
    assert inclusion[virtual_uri] is InclusionLevel.EXCLUDED
    assert inclusion["notes/n.md"] is InclusionLevel.INCLUDED
    for file in files:
        if file.src_uri.endswith("dir-index.md") and file.inclusion is InclusionLevel.INCLUDED:
            assert "Captured content" not in file.content_string
            assert "/captures/" not in file.src_uri
    if collection == "reports":
        assert not [uri for uri in inclusion if uri.startswith("reports/") and uri.endswith("dir-index.md")]
