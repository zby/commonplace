"""ProperDocs hooks: publish local site assets and Markdown companions.

Rendering-side assets (e.g. the tablesort init script) are not knowledge-base
content, so they live here under properdocs-assets/ rather than under docs_dir (kb/).
This hook copies them into the built site so extra_javascript / extra_css entries
in properdocs.yml can reference them by their site-relative path. This rendering setup
is local-only and is not part of the shipped package (yet).
"""

from pathlib import Path

from properdocs.structure.files import File

ASSETS_DIR = Path(__file__).parent / "properdocs-assets"

# Paths relative to ASSETS_DIR and to the built site root. Keep in sync with the
# extra_javascript / extra_css entries in properdocs.yml.
SITE_ASSETS = [
    "javascripts/tablesort-init.js",
    "javascripts/giscus-comments.js",
    "stylesheets/content.css",
    "stylesheets/giscus.css",
    "stylesheets/link-markers.css",
]


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


def on_page_content(html, page, **kwargs):
    """Keep workshop status in the readable HTML body, not the source companion."""
    if page.file.src_uri.startswith("work/"):
        return (
            "<p><strong>Workshop material.</strong> This page records an investigation. "
            "A proposal here is not, by itself, an adopted Commonplace decision.</p>\n" + html
        )
    return html


def on_env(env, config, files):
    """Publish source bytes after page generation and publication filtering."""
    site = Path(config["site_dir"])
    for page in files.documentation_pages():
        target = site / page.src_uri
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(page.content_bytes)

    landing = config["site_url"].rstrip("/") + "/index.md"
    (site / "llms.txt").write_text(f"[Commonplace]({landing})\n", encoding="utf-8")
    return env
