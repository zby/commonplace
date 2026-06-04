"""MkDocs hook: inject local-only site assets into the build.

Rendering-side assets (e.g. the tablesort init script) are not knowledge-base
content, so they live here under mkdocs-assets/ rather than under docs_dir (kb/).
This hook copies them into the built site so extra_javascript / extra_css entries
in mkdocs.yml can reference them by their site-relative path. This rendering setup
is local-only and is not part of the shipped package (yet).
"""

from pathlib import Path

from mkdocs.structure.files import File

ASSETS_DIR = Path(__file__).parent / "mkdocs-assets"

# Paths relative to ASSETS_DIR and to the built site root. Keep in sync with the
# extra_javascript / extra_css entries in mkdocs.yml.
SITE_ASSETS = ["javascripts/tablesort-init.js"]


def on_files(files, config):
    for rel in SITE_ASSETS:
        files.append(
            File(
                rel,
                src_dir=str(ASSETS_DIR),
                dest_dir=config["site_dir"],
                use_directory_urls=config["use_directory_urls"],
            )
        )
    return files
