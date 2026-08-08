from pathlib import Path

import yaml
from mkdocs.config import load_config


ROOT = Path(__file__).resolve().parents[3]


def test_raw_sources_stay_out_while_ingests_are_published() -> None:
    config = load_config(config_file=str(ROOT / "properdocs.yml"))
    excluded = config["exclude_docs"]

    assert excluded.match_file("sources/example.md")
    assert excluded.match_file("sources/example.json")
    assert excluded.match_file("sources/nested/assets/example.png")
    assert not excluded.match_file("sources/example.ingest.md")
    assert not excluded.match_file("sources/nested/example.ingest.md")
    assert not excluded.match_file("sources/README.md")
    assert not excluded.match_file("sources/types/ingest-report.md")


def test_source_redirects_only_cover_published_ingests() -> None:
    config = yaml.safe_load((ROOT / "properdocs.yml").read_text(encoding="utf-8"))

    redirects = next(
        plugin["redirects"]["redirect_maps"]
        for plugin in config["plugins"]
        if isinstance(plugin, dict) and "redirects" in plugin
    )
    source_redirects = {
        old: new
        for old, new in redirects.items()
        if old.startswith("sources/") or new.startswith("sources/")
    }
    assert source_redirects
    assert all(
        old.endswith(".ingest.md") and new.endswith(".ingest.md")
        for old, new in source_redirects.items()
    )
