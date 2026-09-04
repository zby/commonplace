"""Inventory the dependencies an article body carries outside itself.

Run from the repository root:

    python3 scripts/article_dependency_inventory.py kb/articles/<slug>.md
    python3 scripts/article_dependency_inventory.py kb/articles/<slug>.md --strip-links

The default mode prints a Markdown inventory: the source commit, every
outbound link with its target kind, description, and carrying sentence, every
term the body introduces in italics or bold, and every KB definition-note
title the body uses without linking it. The ``binding`` column is left blank
for the staging procedure to fill. ``--strip-links`` prints the body with the
frontmatter removed and every link replaced by its text, for a links-disabled
reading.
"""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)\s]+)\)")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`]*`")
DESCRIPTION_RE = re.compile(r'^description:\s*"?(.*?)"?\s*$', re.MULTILINE)
TITLE_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
EMPHASIS_RE = re.compile(r"(?<![*\w])(\*\*|\*)(?!\s)([^*\n]{2,80}?)(?<!\s)\1(?![*\w])")
SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?])\s+(?=[A-Z\[*\"])")
DEFINITION_DIRS = (Path("kb/notes/definitions"), Path("kb/reference/definitions"))


def strip_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return text
    end = text.find("\n---\n", 4)
    return text[end + 5 :] if end != -1 else text


def blank_code(text: str) -> str:
    text = FENCE_RE.sub(lambda m: " " * len(m.group(0)), text)
    return INLINE_CODE_RE.sub(lambda m: " " * len(m.group(0)), text)


def flatten(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def sentences(text: str) -> list[str]:
    text = re.sub(r"^\s*[-*]\s+", "\n\n", text, flags=re.MULTILINE)
    paragraphs = [flatten(p) for p in re.split(r"\n\s*\n", text) if p.strip()]
    out: list[str] = []
    for paragraph in paragraphs:
        out.extend(s for s in SENTENCE_SPLIT_RE.split(paragraph) if s)
    return out


def sentence_containing(sents: list[str], needle: str) -> str:
    needle = flatten(needle)
    for sentence in sents:
        if needle in sentence:
            return sentence
    return ""


def target_kind(path: Path | None, raw: str) -> str:
    if raw.startswith(("http://", "https://")):
        return "external"
    if path is None or not path.exists():
        return "missing"
    parts = path.as_posix()
    if parts.startswith(("kb/notes/definitions/", "kb/reference/definitions/")):
        return "definition-note"
    if parts.startswith("kb/sources/"):
        return "source"
    if parts.startswith("kb/articles/"):
        return "article"
    if parts.startswith("kb/notes/"):
        return "note"
    if parts.startswith("kb/reference/"):
        return "reference"
    if parts.startswith("kb/work/"):
        return "workshop"
    return "other"


def read_meta(path: Path) -> tuple[str, str]:
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return "", ""
    title = TITLE_RE.search(strip_frontmatter(text))
    description = DESCRIPTION_RE.search(text)
    return (title.group(1) if title else ""), (description.group(1) if description else "")


def source_commit() -> str:
    try:
        return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()
    except (OSError, subprocess.CalledProcessError):
        return "unknown"


def cell(text: str, limit: int = 220) -> str:
    text = flatten(text).replace("|", "\\|")
    return text if len(text) <= limit else text[: limit - 1] + "…"


def definition_titles() -> list[tuple[str, Path]]:
    found: list[tuple[str, Path]] = []
    for directory in DEFINITION_DIRS:
        if not directory.is_dir():
            continue
        for note in sorted(directory.glob("*.md")):
            title, _ = read_meta(note)
            title = re.sub(r"^(Definition\s*[—:-]\s*)", "", title, flags=re.IGNORECASE).strip()
            if title:
                found.append((title, note))
    return found


def inventory(article: Path) -> str:
    raw = article.read_text(encoding="utf-8")
    body = blank_code(strip_frontmatter(raw))
    sents = sentences(body)
    lines = [
        f"# Dependency inventory: `{article.as_posix()}`",
        "",
        f"Source commit: `{source_commit()}`",
        "",
        "## Outbound links",
        "",
        "| # | link text | target | kind | target title | target description | carrying sentence | binding |",
        "|---|---|---|---|---|---|---|---|",
    ]
    for index, match in enumerate(LINK_RE.finditer(body), start=1):
        text, raw_target = match.group(1), match.group(2)
        target_no_anchor = raw_target.split("#", 1)[0]
        resolved: Path | None = None
        if not raw_target.startswith(("http://", "https://")) and target_no_anchor:
            resolved = (article.parent / target_no_anchor).resolve().relative_to(Path.cwd().resolve()) \
                if (article.parent / target_no_anchor).resolve().is_relative_to(Path.cwd().resolve()) else None
        kind = target_kind(resolved, raw_target)
        title, description = read_meta(resolved) if resolved and resolved.exists() else ("", "")
        shown_target = resolved.as_posix() if resolved else raw_target
        if "#" in raw_target and resolved:
            shown_target += "#" + raw_target.split("#", 1)[1]
        sentence = sentence_containing(sents, match.group(0))
        lines.append(
            f"| {index} | {cell(text)} | `{shown_target}` | {kind} | {cell(title)} | "
            f"{cell(description)} | {cell(sentence, 300)} | |"
        )
    lines += ["", "## Terms introduced in emphasis", "", "| term | carrying sentence | binding |", "|---|---|---|"]
    seen: set[str] = set()
    subtitle = re.search(r"^#\s+.+\n\n\*([^*\n]+)\*\s*$", body, re.MULTILINE)
    if subtitle:
        seen.add(subtitle.group(1).strip().lower())
    for match in EMPHASIS_RE.finditer(body):
        term = match.group(2).strip().rstrip(".")
        key = term.lower()
        if key in seen or key.startswith(("draft", "tl;dr")):
            continue
        seen.add(key)
        lines.append(f"| {cell(term)} | {cell(sentence_containing(sents, match.group(0)), 300)} | |")
    linked_targets = {
        (article.parent / m.group(2).split('#', 1)[0]).resolve() for m in LINK_RE.finditer(body)
        if not m.group(2).startswith(("http://", "https://"))
    }
    lines += ["", "## KB definition terms used without a link", "", "| term | definition note | first sentence | binding |", "|---|---|---|---|"]
    lowered = body.lower()
    for title, note in definition_titles():
        if note.resolve() in linked_targets:
            continue
        pattern = r"\b" + re.escape(title.lower()) + r"\b"
        hit = re.search(pattern, lowered)
        if not hit:
            continue
        sentence = next((s for s in sents if re.search(pattern, s.lower())), "")
        lines.append(f"| {cell(title)} | `{note.as_posix()}` | {cell(sentence, 300)} | |")
    return "\n".join(lines) + "\n"


def stripped(article: Path) -> str:
    body = strip_frontmatter(article.read_text(encoding="utf-8"))
    return LINK_RE.sub(lambda m: m.group(1), body)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("article", type=Path)
    parser.add_argument("--strip-links", action="store_true", help="print the body with links replaced by their text")
    args = parser.parse_args(argv)
    if not args.article.is_file():
        print(f"not a file: {args.article}", file=sys.stderr)
        return 2
    sys.stdout.write(stripped(args.article) if args.strip_links else inventory(args.article))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
