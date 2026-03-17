#!/usr/bin/env python3
"""Deterministic validator for KB notes.

Usage:
  uv run kb/instructions/validate/validate_notes.py <note-path-or-name>
  uv run kb/instructions/validate/validate_notes.py all
  uv run kb/instructions/validate/validate_notes.py recent
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

import yaml


REPO_ROOT = Path(__file__).resolve().parents[3]
NOTES_ROOT = REPO_ROOT / "kb" / "notes"
VALID_TRAITS = {"has-comparison", "has-external-sources", "has-implementation"}
VALID_STATUS = {"seedling", "current", "speculative", "outdated"}
TYPE_HEADINGS = {
    "structured-claim": ("## Evidence", "## Reasoning"),
    "spec": ("## Design", "## Implementation"),
    "review": ("## Findings",),
    "adr": ("## Context", "## Decision", "## Consequences"),
}
CLAIMISH_MARKERS = (
    " is ",
    " are ",
    " should ",
    " makes ",
    " make ",
    " requires ",
    " require ",
    " enables ",
    " enable ",
    " means ",
    " predicts ",
    " separates ",
    " prevent",
    " maps ",
    " shows ",
    " closes ",
    " keeps ",
    " turns ",
    " needs ",
    " occupies ",
    " maximizes ",
)


class DuplicateKeyLoader(yaml.SafeLoader):
    """YAML loader that rejects duplicate keys."""


def _construct_mapping(loader: DuplicateKeyLoader, node: yaml.nodes.MappingNode, deep: bool = False) -> dict[str, Any]:
    mapping: dict[str, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise yaml.YAMLError(f"duplicate key: {key}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


DuplicateKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


@dataclass
class CheckResults:
    note_type: str
    passes: list[str] = field(default_factory=list)
    warns: list[str] = field(default_factory=list)
    fails: list[str] = field(default_factory=list)
    infos: list[str] = field(default_factory=list)


@dataclass
class ParsedNote:
    path: Path
    content: str
    note_type: str
    frontmatter: dict[str, Any] | None
    body: str
    title: str


def strip_frontmatter(content: str) -> str:
    return re.sub(r"^---\n.*?\n---\n?", "", content, count=1, flags=re.DOTALL)


def parse_frontmatter(content: str) -> tuple[dict[str, Any] | None, str | None]:
    if not content.startswith("---\n"):
        return None, None

    match = re.match(r"^---\n(.*?)\n---\n?", content, flags=re.DOTALL)
    if not match:
        return None, "frontmatter: missing closing delimiter"

    raw = match.group(1)
    try:
        data = yaml.load(raw, Loader=DuplicateKeyLoader)
    except yaml.YAMLError as exc:
        return None, f"frontmatter: invalid YAML ({exc})"

    if data is None:
        data = {}
    if not isinstance(data, dict):
        return None, "frontmatter: top-level YAML must be a mapping"
    return data, None


def extract_title(content: str) -> str:
    body = strip_frontmatter(content)
    match = re.search(r"^#\s+(.+)$", body, flags=re.MULTILINE)
    return match.group(1).strip() if match else "Untitled"


def tokenize(text: str) -> set[str]:
    return {token for token in re.findall(r"[a-z0-9]+", text.casefold()) if len(token) > 2}


def remove_code_regions(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"`[^`\n]+`", "", text)
    return text


def find_markdown_links(text: str) -> list[str]:
    cleaned = remove_code_regions(text)
    return re.findall(r"\[[^\]]+\]\(([^)]+)\)", cleaned)


def is_nested_git_repo_content(path: Path) -> bool:
    current = path.parent
    while current != NOTES_ROOT and NOTES_ROOT in current.parents:
        if (current / ".git").exists():
            return True
        current = current.parent
    return False


def list_kb_note_paths() -> list[Path]:
    return sorted(path for path in NOTES_ROOT.rglob("*.md") if not is_nested_git_repo_content(path))


def resolve_targets(arg: str) -> list[Path]:
    if arg in {"all", "notes"}:
        return list_kb_note_paths()

    if arg in {"recent", "today"}:
        today = datetime.now().date()
        return sorted(
            path
            for path in list_kb_note_paths()
            if datetime.fromtimestamp(path.stat().st_mtime).date() == today
        )

    candidate = Path(arg)
    if candidate.is_file():
        return [candidate.resolve()]

    repo_candidate = (REPO_ROOT / arg).resolve()
    if repo_candidate.is_file():
        return [repo_candidate]

    name = arg if arg.endswith(".md") else f"{arg}.md"

    matches = sorted(path for path in NOTES_ROOT.rglob(name))
    if not matches:
        matches = sorted(path for path in NOTES_ROOT.rglob("*.md") if path.stem == arg)

    if not matches:
        raise FileNotFoundError(f"No matching note found for: {arg}")
    if len(matches) > 1:
        raise FileNotFoundError(
            "Multiple matching notes found:\n" + "\n".join(str(path.relative_to(REPO_ROOT)) for path in matches)
        )
    return matches


def parse_note(path: Path) -> tuple[ParsedNote | None, str | None]:
    content = path.read_text(encoding="utf-8")
    fm, fm_error = parse_frontmatter(content)
    if fm_error:
        return None, fm_error
    note_type = "text" if fm is None else str(fm.get("type", "note") or "note")
    title = extract_title(content)
    body = strip_frontmatter(content)
    return ParsedNote(path=path, content=content, note_type=note_type, frontmatter=fm, body=body, title=title), None


def sentence_count(description: str) -> int:
    return len(re.findall(r"[.!?](?:\s|$)", description))


def validate_description(results: CheckResults, description: Any, title: str) -> None:
    if description in (None, "", "~"):
        results.fails.append("description: missing or empty")
        return

    if not isinstance(description, str):
        results.fails.append("description: must be a string")
        return

    desc = description.strip()
    if not desc:
        results.fails.append("description: missing or empty")
        return

    results.passes.append(f"description: present, {len(desc)} chars")

    if len(desc) < 50:
        results.warns.append(f"description: {len(desc)} chars — below recommended minimum of 50")
    elif len(desc) > 200:
        results.warns.append(f"description: {len(desc)} chars — above recommended maximum of 200")

    if desc.endswith((".", "!", "?")):
        results.warns.append("description: should not end with terminal punctuation")

    if sentence_count(desc) > 1:
        results.warns.append("description: appears to contain multiple sentences")

    title_tokens = tokenize(title)
    desc_tokens = tokenize(desc)
    if title_tokens and desc_tokens:
        overlap = len(title_tokens & desc_tokens) / max(1, len(title_tokens | desc_tokens))
        if overlap > 0.7:
            results.warns.append("description: may restate the title rather than discriminate this note")


def validate_type_traits_status(results: CheckResults, frontmatter: dict[str, Any], note_type: str) -> None:
    if "type" in frontmatter:
        if not isinstance(frontmatter["type"], str) or not frontmatter["type"].strip():
            results.fails.append("type: must be a non-empty string")
        else:
            results.passes.append(f'type: "{frontmatter["type"]}" — valid')

    traits = frontmatter.get("traits")
    if traits is not None:
        if not isinstance(traits, list):
            results.fails.append("traits: must be a list")
        else:
            invalid = [trait for trait in traits if trait not in VALID_TRAITS]
            if invalid:
                for trait in invalid:
                    results.warns.append(f'traits: invalid trait "{trait}"')
            else:
                results.passes.append("traits: valid")

    status = frontmatter.get("status")
    if status is not None:
        if status not in VALID_STATUS:
            results.warns.append(f'status: "{status}" is not one of {sorted(VALID_STATUS)}')
        else:
            results.passes.append(f'status: "{status}" — valid')

    if note_type == "note" and frontmatter.get("traits") == []:
        results.infos.append("bare note type: type=note with empty traits")


def validate_composability(results: CheckResults, title: str) -> None:
    lowered = title.casefold()
    if any(marker in lowered for marker in CLAIMISH_MARKERS):
        results.passes.append("composability: title reads like a claim")
        return

    word_count = len(re.findall(r"\b\w+\b", title))
    if word_count <= 3:
        results.warns.append("composability: title may be a topic label rather than a claim or specific artifact")
    else:
        results.infos.append("composability: title is topical/descriptive rather than explicitly claim-shaped")


def validate_links(results: CheckResults, path: Path, body: str) -> None:
    missing: list[str] = []
    for link in find_markdown_links(body):
        if re.match(r"^[a-z]+://", link):
            continue
        if not link.endswith(".md"):
            continue
        target = (path.parent / link).resolve()
        if not target.exists():
            missing.append(link)

    if missing:
        for link in missing:
            results.warns.append(f"link health: missing target {link}")
    else:
        results.passes.append("link health: all relative markdown links resolve")


def validate_structure(results: CheckResults, note_type: str, body: str, frontmatter: dict[str, Any]) -> None:
    if note_type in TYPE_HEADINGS:
        missing = [heading for heading in TYPE_HEADINGS[note_type] if heading not in body]
        if note_type == "spec":
            if all(heading not in body for heading in TYPE_HEADINGS[note_type]):
                results.warns.append("structure: spec should contain ## Design or ## Implementation")
            else:
                results.passes.append("structure: spec has required heading")
            return
        if missing:
            results.warns.append(f"structure: missing headings {', '.join(missing)}")
        else:
            results.passes.append(f"structure: required {note_type} headings present")

    if note_type == "review":
        has_date = any(key in frontmatter for key in ("date", "last-checked")) or bool(
            re.search(r"\b\d{4}-\d{2}-\d{2}\b", body)
        )
        if not has_date:
            results.warns.append("structure: review should include a date in frontmatter or body")

    if note_type == "index":
        links = find_markdown_links(body)
        if len(links) < 3:
            results.warns.append("structure: index should be primarily navigational (few links found)")
        else:
            results.passes.append("structure: index has navigational link density")


def validate_note(path: Path) -> CheckResults:
    parsed, parse_error = parse_note(path)
    if parse_error:
        return CheckResults(note_type="unknown", fails=[parse_error])

    assert parsed is not None

    if parsed.frontmatter is None:
        return CheckResults(note_type="text", passes=["text file: no frontmatter, no structural requirements"])

    results = CheckResults(note_type=parsed.note_type)
    results.passes.append("frontmatter: valid delimiters, well-formed YAML")
    validate_description(results, parsed.frontmatter.get("description"), parsed.title)
    validate_type_traits_status(results, parsed.frontmatter, parsed.note_type)
    validate_composability(results, parsed.title)
    validate_links(results, parsed.path, parsed.body)
    validate_structure(results, parsed.note_type, parsed.body, parsed.frontmatter)
    return results


def orphan_info(all_paths: list[Path]) -> dict[Path, bool]:
    inbound: dict[Path, bool] = {path: False for path in all_paths}
    texts = {path: path.read_text(encoding="utf-8") for path in all_paths}
    for target in all_paths:
        filename = target.name
        for source, text in texts.items():
            if source == target:
                continue
            if filename in text:
                inbound[target] = True
                break
    return inbound


def format_block(path: Path, results: CheckResults) -> str:
    lines = [f"=== VALIDATION: {path.name} ===", "", f"Type: {results.note_type}", ""]

    for label, items in (
        ("PASS", results.passes),
        ("WARN", results.warns),
        ("FAIL", results.fails),
        ("INFO", results.infos),
    ):
        lines.append(f"{label}:")
        if items:
            lines.extend(f"- {item}" for item in items)
        else:
            lines.append("- (none)")
        lines.append("")

    if results.fails:
        overall = f"FAIL ({len(results.fails)} fails"
        if results.warns:
            overall += f", {len(results.warns)} warnings"
        overall += ")"
    else:
        overall = "PASS"
        if results.warns:
            overall += f" ({len(results.warns)} warnings)"
        else:
            overall += " (clean)"

    lines.append(f"Overall: {overall}")
    lines.append("===")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="note path, note name, all, or recent")
    args = parser.parse_args()

    try:
        paths = resolve_targets(args.target)
    except FileNotFoundError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    if not paths:
        print("No notes matched target.", file=sys.stderr)
        return 1

    inbound = orphan_info(paths) if args.target in {"all", "notes"} else {}

    had_failures = False
    text_count = 0
    seedling_paths: list[Path] = []

    for path in paths:
        results = validate_note(path)
        if results.note_type == "text":
            text_count += 1
        else:
            parsed, error = parse_note(path)
            if parsed and not error and parsed.frontmatter and parsed.frontmatter.get("status") == "seedling":
                seedling_paths.append(path)
        if args.target in {"all", "notes"} and path in inbound and not inbound[path] and results.note_type != "text":
            results.infos.append("orphan check: no inbound links found in kb/notes")
        print(format_block(path, results))
        if results.fails:
            had_failures = True

    if args.target in {"all", "notes"}:
        print("\n=== BATCH INFO ===\n")
        print(f"Text files: {text_count}")
        if text_count:
            for path in paths:
                parsed, error = parse_note(path)
                if parsed and not error and parsed.note_type == "text":
                    print(f"- {path.relative_to(REPO_ROOT)}")
        print(f"Seedling notes: {len(seedling_paths)}")
        if seedling_paths:
            for path in seedling_paths:
                print(f"- {path.relative_to(REPO_ROOT)}")
        print("\n===")

    return 1 if had_failures else 0


if __name__ == "__main__":
    sys.exit(main())
