"""Repo-invariant checks on this repository's published redirect map.

Unlike the other tests in this directory, these read the real `properdocs.yml`
rather than a fixture: the invariants are about this repository's config drifting
out of step with its tree, which no fixture can observe. A broken redirect has no
local symptom — the generated page redirects to a URL that 404s — so nothing
reports it until a reader follows the link.
"""

from __future__ import annotations

from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[3]
CONFIG = REPO_ROOT / "properdocs.yml"


def _config() -> tuple[Path, dict[str, str]]:
    config = yaml.safe_load(CONFIG.read_text(encoding="utf-8"))
    docs_dir = REPO_ROOT / config["docs_dir"]
    redirects = [
        plugin["redirects"]
        for plugin in config["plugins"]
        if isinstance(plugin, dict) and "redirects" in plugin
    ]
    assert len(redirects) == 1, "expected exactly one redirects plugin entry"
    return docs_dir, redirects[0]["redirect_maps"]


def test_every_redirect_target_resolves() -> None:
    docs_dir, redirect_maps = _config()
    broken = sorted(
        f"{old} -> {new}" for old, new in redirect_maps.items() if not (docs_dir / new).exists()
    )
    assert not broken, "redirect targets do not exist:\n  " + "\n  ".join(broken)


def test_no_redirect_shadows_a_live_page() -> None:
    docs_dir, redirect_maps = _config()
    shadowed = sorted(old for old in redirect_maps if (docs_dir / old).exists())
    assert not shadowed, (
        "redirect keys name pages that still exist, so the entries are dead config:\n  "
        + "\n  ".join(shadowed)
    )


def test_redirect_map_is_flat() -> None:
    docs_dir, redirect_maps = _config()
    chained = sorted(
        f"{old} -> {new} (itself a redirect key)"
        for old, new in redirect_maps.items()
        if new in redirect_maps
    )
    assert not chained, (
        "redirects must point at a live page, not at another redirect — the plugin emits one "
        "hop per entry, so a chain lands on a page that only redirects again:\n  "
        + "\n  ".join(chained)
    )
