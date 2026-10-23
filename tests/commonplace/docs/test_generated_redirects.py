"""Virtual pages must exist before redirect plugins snapshot the file list."""
from pathlib import Path
from types import SimpleNamespace

import pytest
from properdocs.plugins import PluginCollection
from properdocs.structure.files import File, Files, InclusionLevel

from commonplace.docs import properdocs_hooks


def site(tmp_path: Path):
    docs = tmp_path / "kb"
    docs.mkdir()
    for name in ("COLLECTION.md", "README.md", "claim.md"):
        (docs / "theory").mkdir(exist_ok=True)
        (docs / "theory" / name).write_text("# Claim\n", encoding="utf-8")

    class Config(dict):
        site_dir = str(tmp_path / "site")
        use_directory_urls = False
        plugins = PluginCollection()

    config = Config(docs_dir=str(docs), site_dir=str(tmp_path / "site"), use_directory_urls=False)
    files = Files([
        File(f"theory/{name}", str(docs), config.site_dir, False, inclusion=InclusionLevel.INCLUDED)
        for name in ("COLLECTION.md", "README.md", "claim.md")
    ])
    return config, files


def test_directory_generator_precedes_default_priority_consumers(tmp_path: Path) -> None:
    config, files = site(tmp_path)
    observed = []

    def consumer(files, config):
        observed.append(files.get_file_from_path("theory/dir-index.md"))

    # Site plugins are registered before hooks. Priority must reverse that
    # order for consumers which cache the file list for a later event.
    config.plugins["consumer"] = SimpleNamespace(on_files=consumer)
    config.plugins["hooks"] = properdocs_hooks
    config.plugins.run_event("files", files, config=config)

    assert len(observed) == 1
    assert observed[0] is not None
    assert observed[0].url == "theory/dir-index.html"


def test_redirect_plugin_writes_old_virtual_index_address(tmp_path: Path) -> None:
    redirect_module = pytest.importorskip("mkdocs_redirects.plugin")
    config, files = site(tmp_path)
    redirects = redirect_module.RedirectPlugin()
    errors, _ = redirects.load_config({
        "redirect_maps": {"notes/dir-index.md": "theory/dir-index.md"},
    })
    assert not errors
    config.plugins["redirects"] = redirects
    config.plugins["hooks"] = properdocs_hooks
    config.plugins.run_event("files", files, config=config)
    config.plugins.run_event("post_build", config=config)

    output = Path(config.site_dir) / "notes/dir-index.html"
    assert output.is_file()
    assert 'href="../theory/dir-index.html"' in output.read_text(encoding="utf-8")
