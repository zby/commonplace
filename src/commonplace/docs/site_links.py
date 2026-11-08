"""Project checkout and attributed-source links without changing Markdown bytes.

Source positions delimit quotations before Markdown merges adjacent blocks.
Temporary render-only markers preserve that scope through inline processing;
normal authored blockquotes keep ProperDocs's missing-target diagnostics.
"""

from __future__ import annotations

import posixpath
import re
import uuid
from pathlib import Path
from urllib.parse import quote, unquote, urljoin, urlsplit, urlunsplit
from xml.etree import ElementTree as ET

from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor
from markdown.preprocessors import Preprocessor
from markdown.treeprocessors import Treeprocessor

from commonplace.lib import frontmatter
from commonplace.lib.quote_matching import (
    Citation,
    git_citation_path,
    parse_blockquotes,
    parse_github_blob,
)


def install(page, config, files) -> None:
    """Give each page its own extension; never reuse another page's source pin."""
    if config is None or files is None:
        return
    extensions = config.setdefault("markdown_extensions", [])
    extensions[:] = [item for item in extensions if not isinstance(item, SiteLinks)]
    extensions.append(SiteLinks(page, config, files))


class SiteLinks(Extension):
    def __init__(self, page, config, files):
        super().__init__()
        self.page, self.site_config, self.files = page, config, files
        self.markers: dict[str, tuple[str, str | None]] = {}
        self.ends: set[str] = set()

    def extendMarkdown(self, md):  # Python-Markdown's extension API
        md.preprocessors.register(_QuoteScopes(md, self), "commonplace_quote_scopes", 29)
        # Inline links (20) must exist; ProperDocs's local-link validation (0)
        # must not have run yet. Escape placeholders are decoded explicitly.
        md.treeprocessors.register(_SiteLinks(md, self), "commonplace_source_links", 1)
        md.postprocessors.register(_RemoveMarkers(md, self), "commonplace_remove_markers", 0)


def _http_url(value: object) -> str | None:
    if not isinstance(value, str):
        return None
    try:
        parsed = urlsplit(value)
    except ValueError:
        return None
    return value if parsed.scheme in {"https", "http"} and parsed.netloc else None


def _git_base(citation: Citation, source: dict) -> str | None:
    identity, revision = source.get("identity"), source.get("revision")
    if not isinstance(identity, str) or not re.fullmatch(r"https://github\.com/[^/]+/[^/]+/?", identity):
        return None
    if not isinstance(revision, str) or not re.fullmatch(r"[0-9a-fA-F]{40}", revision):
        return None
    if citation.version is not None and citation.version != revision:
        return None
    try:
        path, repository = git_citation_path(citation)
    except ValueError:
        return None
    if repository and repository.casefold().rstrip("/") != identity.casefold().rstrip("/"):
        return None
    if not path or path.startswith("/") or "\\" in path or any(part in {"", ".", ".."} for part in path.split("/")):
        return None
    return f"{identity.rstrip('/')}/blob/{revision}/{quote(path, safe='/')}"


def _boundary_source(page, docs_dir: Path) -> dict | None:
    member = docs_dir / page.file.src_uri
    # Accepted members declare one frozen source in their sibling boundary.
    # Never guess a repository from a system name or an absolute checkout path.
    if member.is_relative_to(docs_dir / "agentic-system-analyses" / "retained"):
        boundary = member.parent / "boundary.md"
        if boundary.is_file():
            parsed = frontmatter.parse(boundary.read_text(encoding="utf-8"))
            source = parsed.data.get("source") if parsed.ok else None
            if isinstance(source, dict):
                return source
    return None


def _quote_context(citation: Citation, page, source: dict | None) -> tuple[bool, str | None]:
    """Return (external quotation, reliable source-file URL or None).

    A pin gives source identity, not a claim that linked destinations exist.
    Bare repository identities, PDF captures and malformed pins are not bases.
    """
    if citation.error or not citation.source:
        return False, None
    if url := _http_url(citation.source):
        try:
            blob = parse_github_blob(url)
        except ValueError:
            blob = None
        if urlsplit(url).hostname == "github.com":
            if blob and re.fullmatch(r"[0-9a-fA-F]{40}", blob.revision):
                return True, _git_base(citation, {"identity": blob.repository, "revision": blob.revision})
            return True, None
        return True, None if urlsplit(url).path.lower().endswith(".pdf") else url

    meta = page.meta or {}
    if meta.get("type") == "types/ingest-report.md" and _http_url(meta.get("source")):
        # Only the name-paired, hash-bound primary capture supplies this base.
        name = Path(page.file.src_uri).name.removesuffix(".ingest.md") + ".md"
        snapshot = f"kb/sources/.snapshots/{name}"
        checksum = meta.get("snapshot_sha256")
        paired = citation.source == snapshot and isinstance(checksum, str) and citation.version == f"sha256:{checksum}"
        url = meta["source"]
        if not paired or urlsplit(url).hostname == "github.com" or urlsplit(url).path.lower().endswith(".pdf"):
            return True, None
        return True, url
    if source is not None:
        return True, _git_base(citation, source) if source.get("kind") == "git" else None
    return False, None


class _QuoteScopes(Preprocessor):
    def __init__(self, md, context):
        super().__init__(md)
        self.context = context

    def run(self, lines):
        context = self.context
        context.markers.clear()
        context.ends.clear()
        source = _boundary_source(context.page, Path(context.site_config["docs_dir"]).resolve())
        before = {}
        nonce = uuid.uuid4().hex
        for index, citation in enumerate(parse_blockquotes("\n".join(lines))):
            # Markdown links, including reference-style links, require '['.
            # Leave link-free quotations' paragraph structure entirely alone.
            if "[" not in citation.quote:
                continue
            external, base = _quote_context(citation, context.page, source)
            if not external:
                continue
            end = citation.line - 1  # Attribution's one-based original source line.
            start = end - len(citation.quote.split("\n"))
            begin_marker, end_marker = f"CP{nonce}BEGIN{index}", f"CP{nonce}END{index}"
            context.markers[begin_marker] = (end_marker, base)
            context.ends.add(end_marker)
            # Separate marker paragraphs keep lists, nested quotes and adjacent
            # citations structurally distinct without editing their source bytes.
            before[start] = [">", "> " + begin_marker, ">"]
            # Attribution annotations are authored navigation, not source
            # content. Close the scope before, not after, the attribution line.
            before[end] = [">", "> " + end_marker, ">"]
        result = []
        for index, line in enumerate(lines):
            result.extend(before.get(index, ()))
            result.append(line)
        return result


class _RemoveMarkers(Postprocessor):
    def __init__(self, md, context):
        super().__init__(md)
        self.context = context

    def run(self, text):
        # Malformed source HTML/fences may swallow a marker before tree parsing.
        # Never leak implementation tokens into the site, even in that case.
        for marker in (*self.context.markers, *self.context.ends):
            text = text.replace(marker, "")
        return text


def _source_url(base: str, href: str) -> str | None:
    # Browsers treat backslashes as separators and percent-encoded dot segments
    # as traversal. Reject those ambiguous spellings rather than merely testing
    # the raw urljoin result's prefix. Ordinary ../ paths are normalized below.
    path = urlsplit(href).path
    decoded = unquote(path)
    if "\\" in path or "\\" in decoded:
        return None
    if any("%" in part and unquote(part) in {".", ".."} for part in path.split("/")):
        return None
    if decoded.count("/") != path.count("/"):
        return None  # An encoded separator changes the path's segment boundaries.
    result = urljoin(base, href)
    if urlsplit(base).hostname == "github.com":
        # Do not let relative links climb out of the recorded Git revision.
        prefix = base.split("/blob/", 1)[0] + "/blob/" + base.split("/blob/", 1)[1].split("/", 1)[0] + "/"
        if not result.startswith(prefix):
            return None
    return result


def _literal_link(element, href: str) -> None:
    element.tag = "span"
    element.attrib.pop("href", None)
    element.set("class", "quoted-source-link")
    if len(element):
        element[-1].tail = (element[-1].tail or "") + " ("
    else:
        element.text = (element.text or "") + " ("
    code = ET.SubElement(element, "code")
    code.text, code.tail = href, ")"


class _SiteLinks(Treeprocessor):
    def __init__(self, md, context):
        super().__init__(md)
        self.context = context

    def run(self, root):
        context = self.context
        docs_dir = Path(context.site_config["docs_dir"]).resolve()
        repository_root = docs_dir.parent
        source_path = docs_dir / context.page.file.src_uri
        base = _http_url(context.site_config.get("extra", {}).get("repository_files_url"))
        handled = set()
        unescape = self.md.treeprocessors["unescape"].unescape
        for block in root.iter("blockquote"):
            active, quote_base = False, None
            children = list(block)
            markers = [(child.text or "").strip() if child.tag == "p" and not len(child) else None
                       for child in children]
            positions = {marker: index for index, marker in enumerate(markers) if marker}
            for index, child in enumerate(children):
                marker = markers[index]
                if marker in context.markers:
                    end_marker, quote_base = context.markers[marker]
                    # If malformed source markup swallowed a delimiter, do not
                    # let an unterminated source scope consume authored prose.
                    active = positions.get(end_marker, -1) > index
                    block.remove(child)
                    continue
                if marker in context.ends:
                    active, quote_base = False, None
                    block.remove(child)
                    continue
                if not active:
                    continue
                for link in child.iter("a"):
                    href = unescape(link.get("href", ""))
                    try:
                        parsed = urlsplit(href)
                    except ValueError:
                        # Preserve ProperDocs's invalid-URL diagnostic.
                        continue
                    if parsed.scheme or parsed.netloc:
                        continue
                    handled.add(link)
                    # A source-root spelling is not this website's root. Its
                    # meaning is uncertain (host root vs repository root).
                    resolved = _source_url(quote_base, href) if quote_base and not href.startswith("/") else None
                    if resolved:
                        link.set("href", resolved)
                    else:
                        _literal_link(link, href)

        if not base:
            return
        for link in root.iter("a"):
            if link in handled:
                continue
            href = unescape(link.get("href", ""))
            try:
                parsed = urlsplit(href)
            except ValueError:
                continue  # ProperDocs reports invalid authored links itself.
            if parsed.scheme or parsed.netloc or not parsed.path or href.startswith(("/", "\\")):
                continue
            try:
                target = (source_path.parent / unquote(parsed.path)).resolve()
            except (OSError, ValueError):
                continue  # Invalid filesystem spellings are not repository files.
            if not target.is_relative_to(repository_root):
                continue
            if target.is_relative_to(docs_dir):
                uri = target.relative_to(docs_dir).as_posix()
                published = context.files.get_file_from_path(uri)
                if published is not None and not published.inclusion.is_excluded():
                    path = posixpath.relpath(uri, posixpath.dirname(context.page.file.src_uri))
                    link.set("href", urlunsplit(("", "", path, parsed.query, parsed.fragment)))
                    continue
            if not target.exists():
                continue
            url_base = urlunsplit((*urlsplit(base)[:3], "", "")).rstrip("/") + "/"
            if target.is_dir() and urlsplit(url_base).hostname == "github.com":
                url_base = url_base.replace("/blob/", "/tree/", 1)
            url = url_base + quote(target.relative_to(repository_root).as_posix(), safe="/")
            link.set("href", urlunsplit((*urlsplit(url)[:3], parsed.query, parsed.fragment)))
