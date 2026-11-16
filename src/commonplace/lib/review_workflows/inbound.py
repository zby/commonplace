"""The inbound contexts of one note: the passages under kb/ that link to it, collected without a model.

The role report (`criteria.ROLE`) judges a note's role in the KB from these
contexts. `collect()` reads every Markdown file under kb/ except the note,
kb/reports/, kb/work/ and hidden directories (such as the ignored source
snapshots), and keeps each file with a local link that resolves to the note.
For each it gives the file's repository path, title and description, and
each passage that holds such a link: the list item, table row, heading or
paragraph around it. Links inside code and quotations do not count, as for
link validation. The text is bounded by the caps below and says when a cap
cut something.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from commonplace.lib import frontmatter
from commonplace.lib.note_parser import (
    extract_title,
    find_markdown_link_offsets,
    strip_frontmatter,
)
from commonplace.lib.project_paths import kb_root
from commonplace.lib.review_workflows import criteria
from commonplace.lib.validation import resolve_local_link_target

INPUT = criteria.SUPPLIED[criteria.ROLE]
"""The input role the role report reads the collected text under: `inbound`."""
ORIGIN = "controller: inbound links collected from kb/"
"""The origin recorded for the collected text, which is no file."""
EXCLUDED = ("reports", "work")
"""Directories directly under kb/ whose files are not inbound contexts: operational outputs and workshops."""
MAX_LINKING_FILES = 30
MAX_PASSAGES_PER_FILE = 5
MAX_PASSAGE_CHARS = 1200
_LIST_ITEM = re.compile(r"\s*(?:[-*+]|\d+[.)])\s")
_HEADING = re.compile(r"#{1,6}\s")


@dataclass(frozen=True)
class Linking:
    path: str                         # repository path of the linking file
    title: str
    description: str
    passages: tuple[str, ...]         # each passage that holds a link to the note, in file order


def _passage(body: str, offset: int) -> str:
    """The list item, table row, heading or paragraph of `body` that holds `offset`."""
    lines = body.splitlines(keepends=True)
    index, seen = 0, 0
    for index, line in enumerate(lines):
        if seen + len(line) > offset:
            break
        seen += len(line)
    line = lines[index]
    if _HEADING.match(line) or line.lstrip().startswith("|"):
        return line.strip()

    def boundary(text: str) -> bool:
        return not text.strip() or bool(_HEADING.match(text))
    start = index
    while start > 0 and not boundary(lines[start - 1]) and not _LIST_ITEM.match(lines[start]):
        start -= 1
    end = index + 1
    while end < len(lines) and not boundary(lines[end]) and not _LIST_ITEM.match(lines[end]):
        end += 1
    return "".join(lines[start:end]).strip()


def _candidates(root: Path, note: Path) -> list[Path]:
    kb = kb_root(root)
    found = []
    for path in sorted(kb.rglob("*.md")):
        parts = path.relative_to(kb).parts
        if parts[0] in EXCLUDED or any(part.startswith(".") for part in parts) or path.resolve() == note:
            continue
        if path.is_file():
            found.append(path)
    return found


def linking(root: Path, note: str) -> list[Linking]:
    """Every file under kb/, outside the exclusions, that links to the repository-relative `note`."""
    root = root.resolve()
    target = (root / note).resolve()
    found = []
    for path in _candidates(root, target):
        text = path.read_text(encoding="utf-8")
        if target.name not in text:                     # a link to the note names its file
            continue
        body = strip_frontmatter(text)
        passages = tuple(dict.fromkeys(
            _passage(body, offset) for offset, link in find_markdown_link_offsets(body)
            if resolve_local_link_target(path, link) == target))
        if passages:
            parsed = frontmatter.parse(text)
            description = parsed.data.get("description") if parsed.ok else None
            found.append(Linking(path.relative_to(root).as_posix(), extract_title(body),
                                 description if isinstance(description, str) else "", passages))
    return found


def _quoted(passage: str) -> str:
    if len(passage) > MAX_PASSAGE_CHARS:
        passage = passage[:MAX_PASSAGE_CHARS].rstrip() + f" [cut at {MAX_PASSAGE_CHARS} characters]"
    return "\n".join(f"> {line}" if line.strip() else ">" for line in passage.splitlines())


def render(note: str, found: list[Linking]) -> str:
    """The inbound contexts as one Markdown text."""
    scope = ("Markdown files under kb/, except kb/reports/, kb/work/, hidden directories and the note itself")
    head = f"# Inbound contexts of `{note}`\n\n"
    if not found:
        return head + f"No file links to this note. Searched: {scope}.\n"
    text = head + f"{len(found)} file(s) link to this note. Searched: {scope}.\n"
    if len(found) > MAX_LINKING_FILES:
        text += (f"\nOnly the first {MAX_LINKING_FILES} files by path are shown; "
                 f"{len(found) - MAX_LINKING_FILES} more were cut.\n")
    for entry in found[:MAX_LINKING_FILES]:
        text += (f"\n## `{entry.path}`\n\n- Title: {entry.title}\n"
                 f"- Description: {entry.description or '(none)'}\n")
        for passage in entry.passages[:MAX_PASSAGES_PER_FILE]:
            text += "\n" + _quoted(passage) + "\n"
        if len(entry.passages) > MAX_PASSAGES_PER_FILE:
            text += (f"\nOnly the first {MAX_PASSAGES_PER_FILE} passages are shown; "
                     f"{len(entry.passages) - MAX_PASSAGES_PER_FILE} more were cut.\n")
    return text


def collect(root: Path, note: str) -> str:
    """The rendered inbound contexts of the repository-relative `note`."""
    return render(note, linking(root, note))


def supplied(root: Path, note: str) -> dict[str, str]:
    """The collected text as one operational input: origin and text."""
    return {"origin": ORIGIN, "text": collect(root, note)}
