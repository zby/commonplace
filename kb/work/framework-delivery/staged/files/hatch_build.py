"""Build hook: prepare the Commonplace library that ships in the package.

The library (kb/instructions, kb/notes, kb/reference, kb/types) is read in place
from the installed package, where the rest of the repository does not exist. So
the build stages a copy and rewrites every relative Markdown link that leaves the
shipped trees:

- a link to a tracked ingest (kb/sources/<slug>.ingest.md) becomes the ingest's
  canonical source URL, from its frontmatter `source:`;
- a link to any other repository file becomes its GitHub URL.

A relative link whose target does not exist fails the build. Links inside code
spans and fenced code blocks are examples, not links, and are left alone.

The wheel installs the prepared copy as shared data under share/commonplace/.
The sdist carries the prepared copy in place of the raw trees, so a wheel built
from the sdist needs no other part of the repository.
"""

from __future__ import annotations

import re
import shutil
import tempfile
from pathlib import Path
from urllib.parse import unquote

from hatchling.builders.hooks.plugin.interface import BuildHookInterface

SHIPPED = ("instructions", "notes", "reference", "types")
GITHUB_BLOB = "https://github.com/zby/commonplace/blob/main/"
FENCE = re.compile(r"^[ \t]*(```|~~~)[^\n]*\n.*?^[ \t]*\1[ \t]*$", re.M | re.S)
INLINE_CODE = re.compile(r"(`+)(?!`).*?(?<!`)\1(?!`)", re.S)
LINK = re.compile(r"(\]\()(<[^>]+>|[^)\s]+)((?:\s+\"[^\"]*\")?\))")
SCHEME = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.-]*:")
SOURCE_LINE = re.compile(r"^source:\s*(\S+)\s*$", re.M)
IGNORED = shutil.ignore_patterns("__pycache__", "*.pyc", ".DS_Store")


def _protected_spans(text: str) -> list[tuple[int, int]]:
    spans = [m.span() for m in FENCE.finditer(text)]

    def inside_fence(pos: int) -> bool:
        return any(start <= pos < end for start, end in spans)

    spans += [m.span() for m in INLINE_CODE.finditer(text) if not inside_fence(m.start())]
    return spans


def _ingest_source(ingest: Path) -> str | None:
    text = ingest.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    frontmatter = text.split("---", 2)[1]
    match = SOURCE_LINE.search(frontmatter)
    return match.group(1).strip("\"'") if match else None


def _rewrite(text: str, source_file: Path, repo: Path, shipped: list[Path], errors: list[str]) -> str:
    protected = _protected_spans(text)

    def replace(match: re.Match[str]) -> str:
        if any(start <= match.start() < end for start, end in protected):
            return match.group(0)
        href = match.group(2).strip("<>")
        if not href or href.startswith(("#", "/")) or SCHEME.match(href):
            return match.group(0)
        path, _, fragment = href.partition("#")
        target = (source_file.parent / unquote(path)).resolve()
        if not target.exists():
            errors.append(f"{source_file.relative_to(repo)}: unresolved link {href}")
            return match.group(0)
        if any(target.is_relative_to(tree) for tree in shipped):
            return match.group(0)
        if target.name.endswith(".ingest.md") and target.parent == repo / "kb" / "sources":
            url = _ingest_source(target)
            if url:
                return f"{match.group(1)}{url}{match.group(3)}"
        url = GITHUB_BLOB + target.relative_to(repo).as_posix() + (f"#{fragment}" if fragment else "")
        return f"{match.group(1)}{url}{match.group(3)}"

    return LINK.sub(replace, text)


def prepare_library(repo: Path, out: Path) -> None:
    """Copy the shipped trees to out and rewrite links that leave them; raise on unresolved links."""
    kb = repo / "kb"
    shipped = [(kb / name).resolve() for name in SHIPPED]
    errors: list[str] = []
    for name in SHIPPED:
        shutil.copytree(kb / name, out / name, ignore=IGNORED)
        for copy in sorted((out / name).rglob("*.md")):
            source_file = kb / name / copy.relative_to(out / name)
            text = copy.read_text(encoding="utf-8")
            rewritten = _rewrite(text, source_file.resolve(), repo.resolve(), shipped, errors)
            if rewritten != text:
                copy.write_text(rewritten, encoding="utf-8")
    if errors:
        shown = "\n".join(errors[:40])
        more = f"\n... and {len(errors) - 40} more" if len(errors) > 40 else ""
        raise RuntimeError(f"library links that resolve to nothing:\n{shown}{more}")


class LibraryBuildHook(BuildHookInterface):
    PLUGIN_NAME = "custom"

    def initialize(self, version: str, build_data: dict) -> None:
        out = Path(tempfile.mkdtemp(prefix="commonplace-library-"))
        prepare_library(Path(self.root), out)
        if self.target_name == "wheel":
            build_data.setdefault("shared_data", {}).update(
                {str(out / name): f"share/commonplace/{name}" for name in SHIPPED}
            )
        elif self.target_name == "sdist":
            build_data.setdefault("force_include", {}).update(
                {str(out / name): f"kb/{name}" for name in SHIPPED}
            )
