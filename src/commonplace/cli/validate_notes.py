"""Deterministic validator for KB notes."""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any

from jsonschema.exceptions import ValidationError

from commonplace.lib.note_parser import ParsedDocument, parse_document
from commonplace.lib.type_resolver import TypeProfile, resolve_type, validate_instance


REPO_ROOT = Path.cwd().resolve()
NOTES_ROOT = REPO_ROOT / "kb" / "notes"
VALID_TRAITS = {
    "definition",
    "has-comparison",
    "has-external-sources",
    "has-implementation",
    "title-as-claim",
}


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
    profile: TypeProfile
    document: ParsedDocument


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
    document, parse_error = parse_document(content)
    if parse_error:
        return None, parse_error
    assert document is not None

    note_type = "text" if document.frontmatter is None else str(document.frontmatter.get("type", "note") or "note")
    profile = resolve_type(path, document.frontmatter, repo_root=REPO_ROOT)
    return ParsedNote(
        path=path,
        content=content,
        note_type=note_type,
        profile=profile,
        document=document,
    ), None


def validate_description(results: CheckResults, description: Any) -> None:
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


def validate_type_traits_status(
    results: CheckResults,
    frontmatter: dict[str, Any],
    note_type: str,
    profile: TypeProfile,
) -> None:
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
        if status not in profile.allowed_status:
            results.warns.append(f'status: "{status}" is not one of {sorted(profile.allowed_status)}')
        else:
            results.passes.append(f'status: "{status}" — valid')

    if note_type == "note" and frontmatter.get("traits") == []:
        results.infos.append("bare note type: type=note with empty traits")


def validate_links_from_document(results: CheckResults, path: Path, links: tuple[str, ...]) -> None:
    missing: list[str] = []
    for link in links:
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


def validate_structure(
    results: CheckResults, note_type: str, document: ParsedDocument, profile: TypeProfile
) -> None:
    if profile.required_headings:
        missing = [heading for heading in profile.required_headings if heading not in document.headings]
        if missing:
            results.warns.append(f"structure: missing headings {', '.join(missing)}")
        else:
            results.passes.append(f"structure: required {note_type} headings present")

    if profile.any_headings:
        if all(heading not in document.headings for heading in profile.any_headings):
            results.warns.append(f"structure: {note_type} should contain {' or '.join(profile.any_headings)}")
        else:
            results.passes.append(f"structure: {note_type} has required heading")

    extra_required_fields = [field for field in profile.required_fields if field != "description"]
    frontmatter = document.frontmatter or {}
    missing_fields = [field for field in extra_required_fields if frontmatter.get(field) in (None, "", [])]
    if missing_fields:
        results.warns.append(f"frontmatter: missing required fields {', '.join(missing_fields)}")
    elif extra_required_fields:
        results.passes.append(f"frontmatter: required {note_type} fields present")

    if profile.requires_date:
        has_date = any(key in frontmatter for key in ("date", "last-checked")) or bool(document.body_dates)
        if not has_date:
            results.warns.append("structure: review should include a date in frontmatter or body")
        else:
            results.passes.append("structure: review has date")

    if profile.min_links is not None:
        if len(document.links) < profile.min_links:
            results.warns.append(f"structure: index should be primarily navigational (found {len(document.links)} links)")
        else:
            results.passes.append("structure: index has navigational link density")


def _missing_required_property(error: ValidationError) -> str | None:
    match = re.search(r"'([^']+)' is a required property", error.message)
    return match.group(1) if match else None


def _schema_error_message(error: ValidationError, profile: TypeProfile, document: ParsedDocument) -> tuple[str, str] | None:
    path = tuple(str(part) for part in error.absolute_path)

    if error.validator == "required" and path == ("frontmatter",):
        missing = _missing_required_property(error)
        if missing == "description":
            return "fail", "description: missing or empty"
        if missing == "type":
            return "fail", "type: must be a non-empty string"
        if missing is not None:
            return "warn", f"frontmatter: missing required fields {missing}"

    if path == ("frontmatter", "description"):
        if error.validator == "type":
            return "fail", "description: must be a string"
        if error.validator == "minLength":
            return "fail", "description: missing or empty"

    if path == ("frontmatter", "type"):
        if error.validator in {"type", "const"}:
            return "fail", "type: must be a non-empty string"

    if path == ("frontmatter", "status") and error.validator == "enum":
        status = None if document.frontmatter is None else document.frontmatter.get("status")
        return "warn", f'status: "{status}" is not one of {sorted(profile.allowed_status)}'

    if error.validator == "format" and len(path) == 2 and path[0] == "frontmatter":
        return "warn", f"frontmatter: {path[1]} must be a valid {error.validator_value}"

    if error.validator in {"contains", "anyOf", "minItems", "enum", "required"}:
        return None

    location = ".".join(path) if path else "document"
    return "warn", f"{location}: {error.message}"


def apply_schema_validation(results: CheckResults, parsed: ParsedNote) -> None:
    messages = {
        ("pass", item) for item in results.passes
    } | {
        ("warn", item) for item in results.warns
    } | {
        ("fail", item) for item in results.fails
    }

    for error in validate_instance(parsed.profile, parsed.document.to_validation_object()):
        translated = _schema_error_message(error, parsed.profile, parsed.document)
        if translated is None:
            continue
        severity, message = translated
        key = (severity, message)
        if key in messages:
            continue
        if severity == "fail":
            results.fails.append(message)
        else:
            results.warns.append(message)
        messages.add(key)


def validate_note(path: Path) -> CheckResults:
    parsed, parse_error = parse_note(path)
    if parse_error:
        return CheckResults(note_type="unknown", fails=[parse_error])

    assert parsed is not None

    if parsed.document.frontmatter is None:
        return CheckResults(note_type="text", passes=["text file: no frontmatter, no structural requirements"])

    results = CheckResults(note_type=parsed.note_type)
    results.passes.append("frontmatter: valid delimiters, well-formed YAML")
    validate_description(results, parsed.document.frontmatter.get("description"))
    validate_type_traits_status(results, parsed.document.frontmatter, parsed.note_type, parsed.profile)
    validate_links_from_document(results, parsed.path, parsed.document.links)
    validate_structure(results, parsed.note_type, parsed.document, parsed.profile)
    apply_schema_validation(results, parsed)
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


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("target", help="note path, note name, all, or recent")
    args = parser.parse_args(argv)

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
    warning_count = 0
    failure_count = 0
    warning_items: list[tuple[Path, str]] = []
    failure_items: list[tuple[Path, str]] = []

    for path in paths:
        results = validate_note(path)
        if results.note_type == "text":
            text_count += 1
        if args.target in {"all", "notes"} and path in inbound and not inbound[path] and results.note_type != "text":
            results.infos.append("orphan check: no inbound links found in kb/notes")
        print(format_block(path, results))
        if results.warns:
            warning_count += 1
            warning_items.extend((path, warning) for warning in results.warns)
        if results.fails:
            had_failures = True
            failure_count += 1
            failure_items.extend((path, failure) for failure in results.fails)

    if args.target in {"all", "notes"}:
        print("\n=== BATCH INFO ===\n")
        print(f"Files analysed: {len(paths)}")
        print(f"Text files: {text_count}")
        print(f"Notes with warnings: {warning_count}")
        print(f"Failing notes: {failure_count}")
        print("\nWarnings:")
        if warning_items:
            for path, warning in warning_items:
                print(f"- {path.relative_to(REPO_ROOT)}: {warning}")
        else:
            print("- (none)")
        print("\nFailures:")
        if failure_items:
            for path, failure in failure_items:
                print(f"- {path.relative_to(REPO_ROOT)}: {failure}")
        else:
            print("- (none)")
        print("\n===")

    return 1 if had_failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
