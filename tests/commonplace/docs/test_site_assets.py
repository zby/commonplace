from pathlib import Path

import yaml

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
