from pathlib import Path
from types import SimpleNamespace

import yaml
from properdocs.structure.files import File, Files, InclusionLevel

import properdocs_site_assets

ROOT = Path(__file__).resolve().parents[3]


def _local_entries(entries: list[str]) -> set[str]:
    return {entry for entry in entries if not entry.startswith(("http://", "https://"))}


def test_site_asset_hook_matches_properdocs_config() -> None:
    config = yaml.safe_load((ROOT / "properdocs.yml").read_text(encoding="utf-8"))
    configured_assets = _local_entries(config.get("extra_css", [])) | _local_entries(
        config.get("extra_javascript", [])
    )

    assert set(properdocs_site_assets.SITE_ASSETS) == configured_assets
    for asset in properdocs_site_assets.SITE_ASSETS:
        assert (properdocs_site_assets.ASSETS_DIR / asset).is_file()


def test_workshop_status_precedes_html_content_only_in_work_tree() -> None:
    body = "<h1>A design question</h1>"
    for uri in ("work/README.md", "work/example/nested/question.md", "work/example/dir-index.md"):
        result = properdocs_site_assets.on_page_content(body, SimpleNamespace(file=SimpleNamespace(src_uri=uri)))
        assert result.index("Workshop material.") < result.index(body)
        assert "not, by itself, an adopted Commonplace decision" in result
    for uri in ("workflow-state/README.md", "theory/work/question.md", "index.md"):
        assert properdocs_site_assets.on_page_content(body, SimpleNamespace(file=SimpleNamespace(src_uri=uri))) == body


def test_markdown_companions_follow_published_files(tmp_path: Path) -> None:
    site = tmp_path / "site"
    config = {"site_dir": str(site), "site_url": "https://example.org/project/"}
    source = b"---\r\ntags: []\r\n---\r\n# Home\r\n[Listing](topics/dir-index.md)\r\n"
    (tmp_path / "index.md").write_bytes(source)
    listing = "# Topics\n"
    virtual = File("topics/dir-index.md", None, str(site), False)
    virtual.content_string = listing
    files = Files([
        File("index.md", str(tmp_path), str(site), False),
        virtual,
        File("private.md", str(tmp_path), str(site), False, inclusion=InclusionLevel.EXCLUDED),
        File("draft.md", str(tmp_path), str(site), False, inclusion=InclusionLevel.DRAFT),
    ])

    properdocs_site_assets.on_env(None, config, files)

    assert (site / "index.md").read_bytes() == source
    assert (site / "topics/dir-index.md").read_text() == listing
    assert not (site / "private.md").exists()
    assert not (site / "draft.md").exists()
    assert (site / "llms.txt").read_text() == "[Commonplace](https://example.org/project/index.md)\n"
