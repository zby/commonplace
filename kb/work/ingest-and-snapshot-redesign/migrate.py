"""Resumable ledger and corpus migration for ingest/snapshot P3.

The ledger is generated before any corpus edit.  Later subcommands consume the
same rows and update their status, so a stopped migration can resume without
reconstructing which artifacts were in scope.
"""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit, urlunsplit

import yaml

ROOT = Path(__file__).resolve().parents[3]
SOURCES = ROOT / "kb/sources"
LEDGER = Path(__file__).with_name("migration.tsv")

INGEST_TYPE = "kb/sources/types/ingest-report.md"
SNAPSHOT_TYPES = {"kb/sources/types/snapshot.md", "./types/snapshot.md"}
RETAINED_SOURCE_TYPES = {
    INGEST_TYPE,
    "kb/sources/types/source-review.md",
    "kb/types/note.md",
}
FIXED_RETAINED_PATHS = {
    "kb/sources/.gitignore",
    "kb/sources/COLLECTION.md",
    "kb/sources/README.md",
}
LEDGER_FIELDS = (
    "row_id",
    "kind",
    "source_path",
    "identity",
    "destination",
    "replacement",
    "status",
    "notes",
)

POSITION_INGEST = "kb/sources/position-bias.ingest.md"
POSITION_README = "related-systems/position-bias/README.md"
POSITION_DEST = "kb/sources/.snapshots/position-bias.md"
POSITION_SOURCE = (
    "https://github.com/lechmazur/position_bias/tree/"
    "483150e8e1938c17331f9e82f86e41a653286651"
)
GENTLE_INGEST = "kb/sources/gentle-coding.ingest.md"
GENTLE_PRIMARY = "kb/sources/gentle-coding.md"
CONFERENCE_SOURCE = "https://conf.researchr.org/track/ecsa-2026/asisas-2026"

RAW_PRIMARY_FIELDS = {
    "kb/sources/letta-memgpt-stateful-agents.ingest.md": {
        "captured": "2026-03-05",
        "capture": "manual",
    },
    "kb/sources/voooooogel-multi-agent-future.ingest.md": {
        "captured": "2026-01-27",
        "capture": "manual-paste",
    },
}
SNAPSHOT_AUTHORITY_FIELDS = {
    "source",
    "captured",
    "capture",
    "genre",
    "type",
    "description",
    "tags",
}

_GENRE_LINE_PATTERNS = (
    re.compile(
        r"^(?:Genre|Type):\s+(?:\*\*)?([a-z0-9-]+)(?:\*\*)?\s*"
        r"(?:(?:--|—|–|-)\s*(.*))?$"
    ),
    re.compile(
        r"^- \*\*(?:Genre|Type):\*\*\s+(?:`|\*\*)?([a-z0-9-]+)"
        r"(?:`|\*\*)?\s*(?:(?:--|—|–|-)\s*(.*))?$"
    ),
)

_FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
_INLINE_CODE_RE = re.compile(r"`[^`\n]+`")
_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")


@dataclass(frozen=True)
class Document:
    path: Path
    text: str
    frontmatter: dict[str, object]
    body: str


def rel(path: Path) -> str:
    return path.resolve().relative_to(ROOT).as_posix()


def git_paths(*args: str, scope: str = ".") -> set[str]:
    raw = subprocess.check_output(
        ["git", *args, "-z", "--", scope], cwd=ROOT
    ).decode("utf-8", errors="surrogateescape")
    return {item for item in raw.split("\0") if item}


def read_document(path: Path) -> Document:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return Document(path, text, {}, text)
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        raise ValueError(f"unterminated frontmatter: {rel(path)}")
    data = yaml.safe_load(parts[1]) or {}
    if not isinstance(data, dict):
        raise TypeError(f"non-mapping frontmatter: {rel(path)}")
    return Document(path, text, data, parts[2])


def typed_markdown() -> list[Document]:
    documents: list[Document] = []
    for path in sorted(SOURCES.rglob("*.md")):
        if path.is_symlink() or not path.is_file():
            continue
        documents.append(read_document(path))
    return documents


def tracked_retirement_paths(tracked: set[str], docs: list[Document]) -> set[str]:
    types = {rel(doc.path): doc.frontmatter.get("type") for doc in docs}
    retiring: set[str] = set()
    for path in tracked:
        if path in FIXED_RETAINED_PATHS or path.startswith("kb/sources/types/"):
            continue
        if types.get(path) in RETAINED_SOURCE_TYPES:
            continue
        retiring.add(path)
    return retiring


def resolve_pointer(ingest: Document) -> Path:
    ingest_path = rel(ingest.path)
    if ingest_path == POSITION_INGEST:
        return ROOT / POSITION_DEST
    if ingest_path == GENTLE_INGEST:
        return ROOT / GENTLE_PRIMARY
    raw = ingest.frontmatter.get("source_snapshot")
    if not isinstance(raw, str) or not raw:
        raise ValueError(f"missing source_snapshot: {ingest_path}")
    if raw.startswith("kb/"):
        return ROOT / raw
    return ingest.path.parent / raw


def sutskever_source(path: str) -> str | None:
    match = re.match(
        r"kb/sources/sutskevers-list/chapters/(0[1-9])-.*\.ingest\.md$", path
    )
    if match is None:
        return None
    return f"https://www.manning.com/preview/sutskevers-list/chapter-{int(match.group(1))}"


def source_for_unit(ingest: Document, primary: Path) -> str:
    ingest_path = rel(ingest.path)
    if ingest_path == POSITION_INGEST:
        return POSITION_SOURCE
    if ingest_path == GENTLE_INGEST:
        return "https://github.com/OttoRenner/Gentle-Coding"
    if source := sutskever_source(ingest_path):
        return source
    primary_doc = read_document(primary)
    source = primary_doc.frontmatter.get("source")
    if source in {
        "file:///home/zby/txt/paper/submissions/asisas-2026/paper.md",
    }:
        return CONFERENCE_SOURCE
    if isinstance(source, str) and source.startswith(("http://", "https://")):
        return source
    for line in ingest.body.splitlines():
        if line.startswith("From: "):
            candidate = line.removeprefix("From: ").strip()
            if candidate.startswith(("http://", "https://")):
                return candidate
    raise ValueError(f"no durable HTTP source for {ingest_path} via {rel(primary)}")


def unit_destination(ingest: Document) -> str:
    path = rel(ingest.path)
    if path.startswith("kb/sources/sutskevers-list/chapters/"):
        return f"kb/sources/{ingest.path.name}"
    return path


def asset_destination(path: str) -> str:
    return f"kb/sources/.snapshots/{Path(path).name}"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.p3tmp")
    if temporary.exists():
        raise FileExistsError(f"stale P3 temporary file: {rel(temporary)}")
    temporary.write_bytes(data)
    os.replace(temporary, path)


def scalar_text(value: object) -> str:
    if isinstance(value, (dt.datetime, dt.date)):
        return value.isoformat()
    return str(value)


def quoted_scalar(value: object) -> str:
    text = scalar_text(value)
    return yaml.safe_dump(text, default_style='"').strip()


def yaml_field_lines(key: str, value: object) -> list[str]:
    rendered = yaml.safe_dump(
        {key: value},
        allow_unicode=True,
        default_flow_style=False,
        sort_keys=False,
        width=10_000,
    ).rstrip("\n")
    return rendered.splitlines()


def classification_block(body: str) -> tuple[int, int, list[str]]:
    match = re.search(r"(?ms)^## Classification\s*\n(.*?)(?=^## |\Z)", body)
    if match is None:
        raise ValueError("missing Classification section")
    return match.start(1), match.end(1), match.group(1).splitlines(keepends=True)


def parse_genre_line(line: str) -> tuple[str, str] | None:
    content = line.rstrip("\r\n")
    for pattern in _GENRE_LINE_PATTERNS:
        if match := pattern.match(content):
            justification = match.group(2) or ""
            return match.group(1), justification
    return None


def ingest_genre(ingest: Document) -> str:
    ingest_path = rel(ingest.path)
    if ingest_path == GENTLE_INGEST:
        return "code-repository"
    _, _, lines = classification_block(ingest.body)
    found = [parsed for line in lines if (parsed := parse_genre_line(line))]
    if len(found) != 1:
        raise ValueError(
            f"expected one Classification genre display in {ingest_path}; "
            f"found {len(found)}"
        )
    return found[0][0]


def primary_metadata(
    ingest: Document, primary: Path, source: str
) -> tuple[str, str, str, dict[str, object]]:
    ingest_path = rel(ingest.path)
    genre = ingest_genre(ingest)
    if ingest_path == POSITION_INGEST:
        return "2026-04-21", "git-checkout", genre, {}
    if ingest_path in RAW_PRIMARY_FIELDS:
        fixed = RAW_PRIMARY_FIELDS[ingest_path]
        return str(fixed["captured"]), str(fixed["capture"]), genre, {}
    snapshot = read_document(primary)
    captured = snapshot.frontmatter.get("captured")
    capture = snapshot.frontmatter.get("capture")
    if captured is None or not isinstance(capture, str) or not capture:
        raise ValueError(f"incomplete capture metadata: {rel(primary)}")
    adapter = {
        key: value
        for key, value in snapshot.frontmatter.items()
        if key not in SNAPSHOT_AUTHORITY_FIELDS
    }
    collisions = sorted(set(adapter) & set(ingest.frontmatter))
    if collisions:
        raise ValueError(
            f"capture metadata collision in {ingest_path}: {', '.join(collisions)}"
        )
    snapshot_source = snapshot.frontmatter.get("source")
    if (
        isinstance(snapshot_source, str)
        and snapshot_source.startswith(("http://", "https://"))
        and sutskever_source(ingest_path) is None
        and snapshot_source != source
    ):
        raise ValueError(
            f"unexpected source rewrite in {ingest_path}: "
            f"{snapshot_source!r} -> {source!r}"
        )
    return scalar_text(captured), capture, genre, adapter


def primary_from_unit_row(row: dict[str, str]) -> str:
    for part in row["notes"].split("; "):
        if part.startswith("primary="):
            return part.removeprefix("primary=")
    raise ValueError(f"unit row lacks primary path: {row['row_id']}")


def current_primary_path(primary_path: str) -> Path:
    original = ROOT / primary_path
    if original.is_file():
        return original
    local = ROOT / asset_destination(primary_path)
    if local.is_file():
        return local
    raise FileNotFoundError(f"primary unavailable at original or cache path: {primary_path}")


def uppercase_first(text: str) -> str:
    for index, char in enumerate(text):
        if char.isalpha():
            return text[:index] + char.upper() + text[index + 1 :]
    return text


def deduplicate_body(ingest: Document) -> str:
    body = ingest.body
    ingest_path = rel(ingest.path)
    section_at = body.find("\n## ")
    if section_at < 0:
        raise ValueError(f"no body section found: {ingest_path}")
    preamble = body[:section_at]
    rest = body[section_at:]
    removed: Counter[str] = Counter()
    kept_lines: list[str] = []
    skip_blank_after_metadata = False
    for line in preamble.splitlines(keepends=True):
        label = line.split(":", 1)[0]
        if label in {"Source", "Captured", "From"}:
            removed[label] += 1
            skip_blank_after_metadata = True
            continue
        if ingest_path == POSITION_INGEST and label == "Pin":
            removed[label] += 1
            skip_blank_after_metadata = True
            continue
        if skip_blank_after_metadata and not line.strip():
            skip_blank_after_metadata = False
            continue
        kept_lines.append(line)
    expected = {"Source": 1, "Captured": 1, "From": 1}
    if ingest_path == "kb/sources/rlm-depth-one-recursion-2085469602017161229.ingest.md":
        expected = {}
    if ingest_path == POSITION_INGEST:
        expected["Pin"] = 1
    if dict(removed) != expected:
        raise ValueError(
            f"unexpected metadata preamble in {ingest_path}: "
            f"removed={dict(removed)} expected={expected}"
        )
    if skip_blank_after_metadata and rest.startswith("\n"):
        rest = rest[1:]
    body = "".join(kept_lines) + rest

    start, end, lines = classification_block(body)
    domains = ", ".join(str(item) for item in ingest.frontmatter["domains"])
    changed_genre = 0
    changed_domains = 0
    new_lines: list[str] = []
    for line in lines:
        newline = "\n" if line.endswith("\n") else ""
        content = line.rstrip("\r\n")
        content_without_trailing_space = content.rstrip()
        if ingest_path == GENTLE_INGEST and content.startswith(
            "Genre: composite repo capture. "
        ):
            new_lines.append(content.removeprefix("Genre: composite repo capture. ") + newline)
            changed_genre += 1
            continue
        if parsed := parse_genre_line(line):
            _, justification = parsed
            if not justification:
                raise ValueError(f"genre display has no justification: {ingest_path}")
            new_lines.append(uppercase_first(justification.rstrip()) + newline)
            changed_genre += 1
            continue
        if content_without_trailing_space == f"Domains: {domains}":
            changed_domains += 1
            continue
        new_lines.append(line)
    if changed_genre != 1:
        raise ValueError(
            f"expected one genre display removal in {ingest_path}; got {changed_genre}"
        )
    expected_domains = (
        0
        if ingest_path
        == "kb/sources/rlm-depth-one-recursion-2085469602017161229.ingest.md"
        else 1
    )
    if changed_domains != expected_domains:
        raise ValueError(
            f"unexpected domain display removal in {ingest_path}: "
            f"{changed_domains} != {expected_domains}"
        )
    body = body[:start] + "".join(new_lines) + body[end:]

    if ingest_path == GENTLE_INGEST:
        old = "three snapshots captured together as one source"
        new = "three repository documents read together as one source"
        if body.count(old) != 1:
            raise ValueError("Gentle-Coding accepted phrase not found exactly once")
        body = body.replace(old, new, 1)

    revision_prefixes = {
        "kb/sources/intern-s2-mobius-arxiv-v1.ingest.md": (
            "The official repository was inspected at "
            "[commit `2b0037c8603c6638f9173540b13562f0372896d1`]"
            "(https://github.com/internlm/intern-s2-mobius/commit/"
            "2b0037c8603c6638f9173540b13562f0372896d1). "
        ),
        "kb/sources/scienceflow-long-horizon-agent-for-ml-research-and-discovery.ingest.md": (
            "The inspected revision is "
            "[`huawei-noah/noah-research@f16be15660284898354e2a5d0fe195f97e4685c4`]"
            "(https://github.com/huawei-noah/noah-research/commit/"
            "f16be15660284898354e2a5d0fe195f97e4685c4). "
        ),
        "kb/sources/spade-self-play-in-adaptive-synthetic-executable-environments.ingest.md": (
            "The official repository was reviewed at commit "
            "[65421ccb15a6d501ad6217bd969816146da15e11]"
            "(https://github.com/spade-rl/spade/commit/"
            "65421ccb15a6d501ad6217bd969816146da15e11).\n\n"
        ),
    }
    if prefix := revision_prefixes.get(ingest_path):
        if body.count(prefix) != 1:
            raise ValueError(f"code-revision inventory not found exactly once: {ingest_path}")
        body = body.replace(prefix, "", 1)
    return body


def rebase_local_links(body: str, old_path: Path, new_path: Path) -> str:
    if old_path == new_path:
        return body
    replacements: list[tuple[int, int, str]] = []
    for match in markdown_matches(body):
        raw = match.group(2).strip()
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue
        decoded = unquote(parsed.path)
        if Path(decoded).is_absolute():
            continue
        target = (old_path.parent / decoded).resolve()
        rebased = os.path.relpath(target, start=new_path.parent.resolve())
        replacement = urlunsplit(("", "", Path(rebased).as_posix(), parsed.query, parsed.fragment))
        replacements.append((match.start(2), match.end(2), replacement))
    for start, end, replacement in reversed(replacements):
        body = body[:start] + replacement + body[end:]
    return body


def migrated_frontmatter(
    ingest: Document,
    *,
    source: str,
    captured: str,
    capture: str,
    genre: str,
    checksum: str,
    adapter: dict[str, object],
) -> str:
    original = ingest.text.split("---\n", 2)[1].splitlines()
    output: list[str] = []
    inserted_primary = False
    index = 0
    while index < len(original):
        line = original[index]
        if line.startswith("source_snapshot:"):
            if inserted_primary:
                raise ValueError(f"duplicate source_snapshot in {rel(ingest.path)}")
            output.extend(
                [
                    f"source: {source}",
                    f"captured: {quoted_scalar(captured)}",
                    f"capture: {capture}",
                    f"genre: {genre}",
                    f"snapshot_sha256: {checksum}",
                ]
            )
            for key, value in adapter.items():
                output.extend(yaml_field_lines(key, value))
            inserted_primary = True
            index += 1
            continue
        if line == "code_revisions:":
            revisions: list[str] = []
            index += 1
            while index < len(original) and original[index].startswith((" ", "\t")):
                item = original[index].strip()
                if not item.startswith("- "):
                    raise ValueError(
                        f"unsupported code_revisions shape in {rel(ingest.path)}"
                    )
                revisions.append(item.removeprefix("- ").strip())
                index += 1
            if not revisions:
                raise ValueError(f"empty code_revisions in {rel(ingest.path)}")
            output.append("secondary_sources:")
            for revision in revisions:
                output.extend(["  - role: implementation", f"    source: {revision}"])
            continue
        output.append(line)
        index += 1
    if not inserted_primary:
        raise ValueError(f"source_snapshot not found in {rel(ingest.path)}")
    return "---\n" + "\n".join(output) + "\n---\n"


def unit_rows(
    ingests: list[Document], tracked: set[str]
) -> tuple[list[dict[str, str]], dict[str, tuple[str, str]]]:
    rows: list[dict[str, str]] = []
    primary_owners: dict[str, tuple[str, str]] = {}
    for ingest in ingests:
        ingest_path = rel(ingest.path)
        primary = resolve_pointer(ingest)
        primary_path = rel(primary)
        if ingest_path != POSITION_INGEST and not primary.is_file():
            raise ValueError(f"primary is unavailable: {ingest_path} -> {primary_path}")
        source = source_for_unit(ingest, primary)
        if primary_path in primary_owners:
            raise ValueError(
                f"primary claimed by multiple ingests: {primary_path}: "
                f"{primary_owners[primary_path][0]}, {ingest_path}"
            )
        primary_owners[primary_path] = (ingest_path, source)
        disposition = "ordinary"
        if ingest_path == POSITION_INGEST:
            disposition = "materialize pinned README before hashing"
        elif ingest_path == GENTLE_INGEST:
            disposition = "three local documents; gentle-coding.md is the sole primary"
        elif ingest_path.startswith("kb/sources/sutskevers-list/chapters/"):
            disposition = "move ignored nested ingest to durable source root"
        rows.append(
            {
                "row_id": f"unit:{ingest_path}",
                "kind": "unit",
                "source_path": ingest_path,
                "identity": source,
                "destination": unit_destination(ingest),
                "replacement": "",
                "status": "pending",
                "notes": (
                    f"primary={primary_path}; "
                    f"ingest={'tracked' if ingest_path in tracked else 'untracked'}; "
                    f"disposition={disposition}"
                ),
            }
        )
    return rows, primary_owners


def asset_rows(
    *,
    retiring: set[str],
    untracked_snapshots: set[str],
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    for path in sorted(retiring | untracked_snapshots):
        state = "tracked-retirement" if path in retiring else "untracked-local-snapshot"
        rows.append(
            {
                "row_id": f"asset:{path}",
                "kind": "asset",
                "source_path": path,
                "identity": sha256(ROOT / path),
                "destination": asset_destination(path),
                "replacement": "",
                "status": "pending",
                "notes": state,
            }
        )
    rows.append(
        {
            "row_id": f"asset:{POSITION_DEST}",
            "kind": "asset",
            "source_path": POSITION_README,
            "identity": sha256(ROOT / POSITION_README),
            "destination": POSITION_DEST,
            "replacement": "",
            "status": "pending",
            "notes": "materialize with capture frontmatter from pinned clean checkout",
        }
    )
    destinations: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        destinations[row["destination"]].append(row)
    collisions = {key: value for key, value in destinations.items() if len(value) > 1}
    if collisions:
        details = "; ".join(
            f"{dest}: {[row['source_path'] for row in colliding]}"
            for dest, colliding in collisions.items()
        )
        raise ValueError(f"asset destination collision: {details}")
    return rows


def _blank(match: re.Match[str]) -> str:
    return "".join("\n" if char == "\n" else " " for char in match.group(0))


def markdown_matches(text: str) -> list[re.Match[str]]:
    cleaned = _FENCE_RE.sub(_blank, text)
    spans = tuple(match.span() for match in _INLINE_CODE_RE.finditer(cleaned))
    return [
        match
        for match in _LINK_RE.finditer(cleaned)
        if not any(start <= match.start() and match.end() <= end for start, end in spans)
    ]


def resolve_link(author: Path, raw_target: str) -> str | None:
    parsed = urlsplit(raw_target.strip())
    if parsed.scheme or parsed.netloc:
        return None
    link_path = unquote(parsed.path)
    if not link_path or Path(link_path).is_absolute():
        return None
    try:
        return rel(author.parent / link_path)
    except ValueError:
        return None


def durable_authors(
    *,
    docs: list[Document],
    tracked_all: set[str],
    retiring_targets: set[str],
) -> list[Path]:
    authors: set[Path] = set()
    for path in tracked_all:
        if not path.endswith(".md") or path in retiring_targets:
            continue
        if path.startswith(("kb/work/", "kb/reports/")):
            continue
        authors.add(ROOT / path)
    # Reconcile legitimate untracked durable artifacts without sweeping ignored
    # source bodies or in-flight workshops into the link-author universe.
    for doc in docs:
        path = rel(doc.path)
        if doc.frontmatter.get("type") == INGEST_TYPE:
            authors.add(doc.path)
    for path in (ROOT / "kb/notes").rglob("*.md"):
        path_string = rel(path)
        if path_string in tracked_all:
            continue
        ignored = subprocess.run(
            ["git", "check-ignore", "-q", "--", path_string],
            cwd=ROOT,
            check=False,
        ).returncode == 0
        if not ignored:
            authors.add(path)
    return sorted(authors)


def external_source_for_target(
    target: str,
    *,
    primary_owners: dict[str, tuple[str, str]],
) -> str:
    if target in primary_owners:
        return primary_owners[target][1]
    if target == "kb/sources/gentle-coding-proof-of-concept.md":
        return "https://github.com/OttoRenner/Gentle-Coding/blob/main/Proof-of-Concept.md"
    if target == "kb/sources/gentle-coding-research.md":
        return "https://github.com/OttoRenner/Gentle-Coding/blob/main/RESEARCH.md"
    doc = read_document(ROOT / target)
    source = doc.frontmatter.get("source")
    if isinstance(source, str) and source.startswith(("http://", "https://")):
        return source
    raise ValueError(f"no external replacement source for linked target: {target}")


def link_rows(
    *,
    docs: list[Document],
    tracked_all: set[str],
    retiring_targets: set[str],
    primary_owners: dict[str, tuple[str, str]],
) -> list[dict[str, str]]:
    rows: list[dict[str, str]] = []
    authors = durable_authors(
        docs=docs,
        tracked_all=tracked_all,
        retiring_targets=retiring_targets,
    )
    ingest_paths = {
        rel(doc.path): doc for doc in docs if doc.frontmatter.get("type") == INGEST_TYPE
    }
    for author in authors:
        text = author.read_text(encoding="utf-8")
        occurrence_by_line: Counter[int] = Counter()
        for match in markdown_matches(text):
            target = resolve_link(author, match.group(2))
            if target not in retiring_targets:
                continue
            line = text.count("\n", 0, match.start()) + 1
            occurrence_by_line[line] += 1
            ordinal = occurrence_by_line[line]
            author_path = rel(author)
            replacement = external_source_for_target(
                target, primary_owners=primary_owners
            )
            raw_fragment = urlsplit(match.group(2).strip()).fragment
            if raw_fragment:
                parsed_replacement = urlsplit(replacement)
                replacement = urlunsplit(
                    (
                        parsed_replacement.scheme,
                        parsed_replacement.netloc,
                        parsed_replacement.path,
                        parsed_replacement.query,
                        raw_fragment,
                    )
                )
            note = f"target={target}; text={match.group(1)}"
            if author_path in ingest_paths:
                first_section = text.find("\n## ")
                line_start = text.rfind("\n", 0, match.start()) + 1
                display_line = text[line_start : text.find("\n", match.end())]
                if (
                    first_section < 0 or match.start() < first_section
                ) and display_line.startswith("Source:"):
                    replacement = "REMOVE_METADATA_DISPLAY"
                    note += "; primary ingest preamble"
            rows.append(
                {
                    "row_id": f"link:{author_path}:{line}:{ordinal}",
                    "kind": "link",
                    "source_path": author_path,
                    "identity": (
                        f"line={line};ordinal={ordinal};raw={match.group(2)};resolved={target}"
                    ),
                    "destination": target,
                    "replacement": replacement,
                    "status": "pending",
                    "notes": note,
                }
            )
    return rows


def discover_rows() -> tuple[list[dict[str, str]], dict[str, int]]:
    tracked = git_paths("ls-files", scope="kb/sources")
    tracked_all = git_paths("ls-files")
    docs = typed_markdown()
    ingests = [doc for doc in docs if doc.frontmatter.get("type") == INGEST_TYPE]
    snapshots = [doc for doc in docs if doc.frontmatter.get("type") in SNAPSHOT_TYPES]
    retiring = tracked_retirement_paths(tracked, docs)
    untracked_snapshots = {rel(doc.path) for doc in snapshots if rel(doc.path) not in tracked}

    units, primary_owners = unit_rows(ingests, tracked)
    assets = asset_rows(retiring=retiring, untracked_snapshots=untracked_snapshots)
    retiring_targets = retiring | untracked_snapshots
    links = link_rows(
        docs=docs,
        tracked_all=tracked_all,
        retiring_targets=retiring_targets,
        primary_owners=primary_owners,
    )
    rows = units + assets + links
    ids = [row["row_id"] for row in rows]
    if len(ids) != len(set(ids)):
        duplicate_ids = sorted(key for key, count in Counter(ids).items() if count > 1)
        raise ValueError(f"duplicate ledger row ids: {duplicate_ids}")
    counts = {
        "tracked_source_files": len(tracked),
        "ingests": len(ingests),
        "tracked_ingests": sum(rel(doc.path) in tracked for doc in ingests),
        "untracked_ingests": sum(rel(doc.path) not in tracked for doc in ingests),
        "tracked_typed_snapshots": sum(rel(doc.path) in tracked for doc in snapshots),
        "untracked_typed_snapshots": len(untracked_snapshots),
        "tracked_retiring_markdown": sum(path.endswith(".md") for path in retiring),
        "tracked_retiring_companions": sum(not path.endswith(".md") for path in retiring),
        "unit_rows": len(units),
        "asset_rows": len(assets),
        "link_rows": len(links),
        "link_authors": len({row["source_path"] for row in links}),
        "link_targets": len({row["destination"] for row in links}),
        "total_rows": len(rows),
    }
    return rows, counts


def write_ledger(rows: list[dict[str, str]], *, refresh: bool = False) -> None:
    if LEDGER.exists() and not refresh:
        raise FileExistsError(f"refusing to overwrite existing ledger: {LEDGER}")
    if refresh:
        current = read_ledger()
        nonpending = [row["row_id"] for row in current if row["status"] != "pending"]
        if nonpending:
            raise ValueError(
                "refusing to refresh a started ledger; non-pending rows: "
                f"{nonpending[:10]}"
            )
    target = LEDGER.with_suffix(".tsv.tmp")
    with target.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=LEDGER_FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    target.replace(LEDGER)


def read_ledger() -> list[dict[str, str]]:
    with LEDGER.open(encoding="utf-8", newline="") as stream:
        return list(csv.DictReader(stream, delimiter="\t"))


def save_ledger(rows: list[dict[str, str]]) -> None:
    target = LEDGER.with_suffix(".tsv.tmp")
    with target.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(stream, fieldnames=LEDGER_FIELDS, delimiter="\t")
        writer.writeheader()
        writer.writerows(rows)
    os.replace(target, LEDGER)


def append_note(row: dict[str, str], note: str) -> None:
    if "\t" in note or "\n" in note:
        raise ValueError(f"ledger note must be one TSV-safe line: {note!r}")
    if note and note not in row["notes"]:
        row["notes"] = f"{row['notes']}; {note}" if row["notes"] else note


def row_map(rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
    mapped = {row["row_id"]: row for row in rows}
    if len(mapped) != len(rows):
        raise ValueError("ledger has duplicate row ids")
    return mapped


def position_materialization_bytes(row: dict[str, str]) -> bytes:
    checkout = ROOT / "related-systems/position-bias"
    head = subprocess.check_output(
        ["git", "-C", str(checkout), "rev-parse", "HEAD"], text=True
    ).strip()
    expected_head = "483150e8e1938c17331f9e82f86e41a653286651"
    if head != expected_head:
        raise ValueError(f"position-bias checkout HEAD {head} != {expected_head}")
    dirty = subprocess.check_output(
        ["git", "-C", str(checkout), "status", "--porcelain"], text=True
    )
    if dirty:
        raise ValueError("position-bias checkout is dirty; refusing materialization")
    readme = (checkout / "README.md").read_bytes()
    if hashlib.sha256(readme).hexdigest() != row["identity"]:
        raise ValueError("position-bias README changed since ledger construction")
    header = (
        "---\n"
        f"source: {POSITION_SOURCE}\n"
        'captured: "2026-04-21"\n'
        "capture: git-checkout\n"
        "genre: code-repository\n"
        "type: kb/sources/types/snapshot.md\n"
        "---\n\n"
    ).encode()
    return header + readme


def materialize_position(rows: list[dict[str, str]]) -> None:
    row_id = f"asset:{POSITION_DEST}"
    row = row_map(rows)[row_id]
    destination = ROOT / POSITION_DEST
    expected = position_materialization_bytes(row)
    if destination.exists():
        if destination.read_bytes() != expected:
            raise ValueError(
                f"different bytes already occupy materialization: {POSITION_DEST}"
            )
    else:
        atomic_write(destination, expected)
    checksum = hashlib.sha256(expected).hexdigest()
    row["status"] = "complete"
    append_note(row, f"materialized_sha256={checksum}")
    save_ledger(rows)


def validate_migrated_ingest(
    document: Document,
    *,
    source: str,
    checksum: str,
    original_headings: tuple[str, ...] | None = None,
) -> None:
    frontmatter = document.frontmatter
    required = {
        "description",
        "source",
        "captured",
        "capture",
        "genre",
        "snapshot_sha256",
        "ingested",
        "type",
        "domains",
    }
    missing = sorted(required - set(frontmatter))
    if missing:
        raise ValueError(f"migrated ingest missing fields: {rel(document.path)}: {missing}")
    if frontmatter["source"] != source or frontmatter["snapshot_sha256"] != checksum:
        raise ValueError(f"migrated ingest identity mismatch: {rel(document.path)}")
    if "source_snapshot" in frontmatter or "code_revisions" in frontmatter:
        raise ValueError(f"retired field remains: {rel(document.path)}")
    if not re.fullmatch(r"[0-9a-f]{64}", str(frontmatter["snapshot_sha256"])):
        raise ValueError(f"invalid checksum shape: {rel(document.path)}")
    if frontmatter.get("secondary_sources"):
        for item in frontmatter["secondary_sources"]:  # type: ignore[index]
            if set(item) != {"role", "source"} or item["role"] != "implementation":
                raise ValueError(f"invalid secondary in {rel(document.path)}: {item}")
    headings = tuple(
        match.group(0).strip()
        for match in re.finditer(r"(?m)^#{1,6}\s+.+$", _FENCE_RE.sub("", document.body))
    )
    if original_headings is not None and headings != original_headings:
        raise ValueError(f"body headings changed in {rel(document.path)}")


def heading_tuple(body: str) -> tuple[str, ...]:
    return tuple(
        match.group(0).strip()
        for match in re.finditer(r"(?m)^#{1,6}\s+.+$", _FENCE_RE.sub("", body))
    )


def migrate_units(rows: list[dict[str, str]]) -> None:
    for row in (item for item in rows if item["kind"] == "unit"):
        if row["status"] == "complete":
            continue
        source_path = ROOT / row["source_path"]
        destination = ROOT / row["destination"]
        current = source_path if source_path.is_file() else destination
        if not current.is_file():
            raise FileNotFoundError(f"unit path is unavailable: {row['row_id']}")
        primary_identity = primary_from_unit_row(row)
        primary = current_primary_path(primary_identity)
        checksum = sha256(primary)
        current_doc = read_document(current)

        # Recover cleanly when a crash happened after the artifact write and
        # before the ledger status update.
        if "source_snapshot" not in current_doc.frontmatter:
            validate_migrated_ingest(
                current_doc,
                source=row["identity"],
                checksum=checksum,
            )
            row["status"] = "complete"
            append_note(row, f"snapshot_sha256={checksum}")
            append_note(row, "status recovered from migrated artifact")
            save_ledger(rows)
            continue

        original_file_hash = hashlib.sha256(current_doc.text.encode()).hexdigest()
        original_body_hash = hashlib.sha256(current_doc.body.encode()).hexdigest()
        original_headings = heading_tuple(current_doc.body)
        captured, capture, genre, adapter = primary_metadata(
            current_doc, primary, row["identity"]
        )
        if row["source_path"] == GENTLE_INGEST and checksum != (
            "5c99601b818bcc5461e7c7c2fe4d8776773cca417aee8775d197d0739b65bb56"
        ):
            raise ValueError("Gentle-Coding primary checksum does not match accepted P1 value")
        new_frontmatter = migrated_frontmatter(
            current_doc,
            source=row["identity"],
            captured=captured,
            capture=capture,
            genre=genre,
            checksum=checksum,
            adapter=adapter,
        )
        new_body = deduplicate_body(current_doc)
        new_body = rebase_local_links(new_body, current, destination)
        new_text = new_frontmatter + new_body
        candidate_path = destination.with_name(f".{destination.name}.candidate")
        candidate = read_document_from_text(candidate_path, new_text)
        validate_migrated_ingest(
            candidate,
            source=row["identity"],
            checksum=checksum,
            original_headings=original_headings,
        )
        if destination.exists() and destination != current:
            if destination.read_text(encoding="utf-8") != new_text:
                raise ValueError(f"different unit already exists: {rel(destination)}")
        else:
            atomic_write(destination, new_text.encode())
        if source_path != destination and source_path.exists():
            source_path.unlink()
        row["status"] = "complete"
        append_note(row, f"before_file_sha256={original_file_hash}")
        append_note(row, f"before_body_sha256={original_body_hash}")
        append_note(row, f"snapshot_sha256={checksum}")
        if row["source_path"] in RAW_PRIMARY_FIELDS:
            append_note(
                row,
                f"raw-source disposition={capture} inferred from retained capture form",
            )
        if row["identity"] == CONFERENCE_SOURCE:
            append_note(row, "file URL replaced by official ASISAS track URL")
        save_ledger(rows)


def normalize_migrated_metadata_gaps(rows: list[dict[str, str]]) -> None:
    for row in (item for item in rows if item["kind"] == "unit"):
        path = ROOT / row["destination"]
        document = read_document(path)
        first_section = document.body.find("\n## ")
        if first_section < 0:
            raise ValueError(f"migrated ingest lacks a section: {row['destination']}")
        prefix = document.body[: first_section + 1]
        count = prefix.count("\n\n\n")
        if count > 1:
            raise ValueError(
                f"ambiguous metadata-gap normalization: {row['destination']} ({count})"
            )
        if count == 0:
            continue
        changed = document.text.replace("\n\n\n", "\n\n", 1)
        atomic_write(path, changed.encode())
        append_note(row, "removed metadata-block blank-line residue")
        save_ledger(rows)


def normalize_migrated_classification_gaps(rows: list[dict[str, str]]) -> None:
    for row in (item for item in rows if item["kind"] == "unit"):
        path = ROOT / row["destination"]
        document = read_document(path)
        start, end, _ = classification_block(document.body)
        block = document.body[start:end]
        count = block.count("\n\n\n")
        if count > 1:
            raise ValueError(
                f"ambiguous classification-gap normalization: "
                f"{row['destination']} ({count})"
            )
        if count == 0:
            continue
        new_block = block.replace("\n\n\n", "\n\n", 1)
        new_body = document.body[:start] + new_block + document.body[end:]
        frontmatter_text = document.text[: -len(document.body)]
        atomic_write(path, (frontmatter_text + new_body).encode())
        append_note(row, "removed domains-line blank-line residue")
        save_ledger(rows)


def read_document_from_text(path: Path, text: str) -> Document:
    if not text.startswith("---\n"):
        return Document(path, text, {}, text)
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        raise ValueError(f"unterminated generated frontmatter: {path}")
    data = yaml.safe_load(parts[1]) or {}
    if not isinstance(data, dict):
        raise TypeError(f"non-mapping generated frontmatter: {path}")
    return Document(path, text, data, parts[2])


def dry_run(rows: list[dict[str, str]]) -> dict[str, int]:
    mapped = row_map(rows)
    position_bytes = position_materialization_bytes(mapped[f"asset:{POSITION_DEST}"])
    position_checksum = hashlib.sha256(position_bytes).hexdigest()
    genres: Counter[str] = Counter()
    adapter_fields = 0
    moved_units = 0
    code_grounded = 0
    for row in (item for item in rows if item["kind"] == "unit"):
        source_path = ROOT / row["source_path"]
        destination = ROOT / row["destination"]
        if not source_path.is_file():
            raise FileNotFoundError(f"dry-run unit source unavailable: {row['row_id']}")
        ingest = read_document(source_path)
        primary_identity = primary_from_unit_row(row)
        if row["source_path"] == POSITION_INGEST:
            primary = ROOT / POSITION_DEST
            checksum = position_checksum
        else:
            primary = ROOT / primary_identity
            checksum = sha256(primary)
        captured, capture, genre, adapter = primary_metadata(
            ingest, primary, row["identity"]
        )
        genres[genre] += 1
        adapter_fields += len(adapter)
        code_grounded += int("code_revisions" in ingest.frontmatter)
        moved_units += int(source_path != destination)
        frontmatter = migrated_frontmatter(
            ingest,
            source=row["identity"],
            captured=captured,
            capture=capture,
            genre=genre,
            checksum=checksum,
            adapter=adapter,
        )
        body = rebase_local_links(deduplicate_body(ingest), source_path, destination)
        candidate = read_document_from_text(
            destination.with_name(f".{destination.name}.candidate"), frontmatter + body
        )
        validate_migrated_ingest(
            candidate,
            source=row["identity"],
            checksum=checksum,
            original_headings=heading_tuple(ingest.body),
        )
        if destination.exists() and destination != source_path:
            raise ValueError(f"dry-run destination already exists: {rel(destination)}")
    for row in (item for item in rows if item["kind"] == "asset"):
        destination = ROOT / row["destination"]
        if row["destination"] == POSITION_DEST:
            continue
        source = ROOT / row["source_path"]
        if not source.is_file():
            raise FileNotFoundError(f"dry-run asset source unavailable: {row['row_id']}")
        if sha256(source) != row["identity"]:
            raise ValueError(f"dry-run asset hash changed: {row['row_id']}")
        if destination.exists():
            raise ValueError(f"dry-run asset destination already exists: {rel(destination)}")
    for row in (item for item in rows if item["kind"] == "link"):
        if row["replacement"] != "REMOVE_METADATA_DISPLAY" and not row[
            "replacement"
        ].startswith(("http://", "https://")):
            raise ValueError(f"invalid link disposition: {row['row_id']}")
    return {
        "units": sum(row["kind"] == "unit" for row in rows),
        "moved_units": moved_units,
        "code_grounded_units": code_grounded,
        "adapter_fields_copied": adapter_fields,
        "genres": len(genres),
        "position_snapshot_bytes": len(position_bytes),
        "assets": sum(row["kind"] == "asset" for row in rows),
        "links": sum(row["kind"] == "link" for row in rows),
    }


def link_identity(row: dict[str, str]) -> tuple[str, str]:
    match = re.fullmatch(
        r"line=\d+;ordinal=\d+;raw=(.*);resolved=(.+)", row["identity"]
    )
    if match is None:
        raise ValueError(f"invalid link identity: {row['row_id']}: {row['identity']}")
    return match.group(1), match.group(2)


def current_author_path(
    author: str, unit_destinations: dict[str, str]
) -> Path:
    original = ROOT / author
    if original.is_file():
        return original
    if author in unit_destinations:
        destination = ROOT / unit_destinations[author]
        if destination.is_file():
            return destination
    raise FileNotFoundError(f"link author unavailable: {author}")


def migrate_links(rows: list[dict[str, str]]) -> None:
    incomplete_units = [
        row["row_id"]
        for row in rows
        if row["kind"] == "unit" and row["status"] != "complete"
    ]
    if incomplete_units:
        raise ValueError(f"link migration requires complete units: {incomplete_units[:10]}")
    unit_destinations = {
        row["source_path"]: row["destination"]
        for row in rows
        if row["kind"] == "unit"
    }
    groups: dict[str, list[dict[str, str]]] = defaultdict(list)
    for row in rows:
        if row["kind"] == "link" and row["status"] != "complete":
            groups[row["source_path"]].append(row)
    for author, pending_rows in sorted(groups.items()):
        path = current_author_path(author, unit_destinations)
        text = path.read_text(encoding="utf-8")
        expected: Counter[tuple[str, str]] = Counter()
        replacement_by_key: dict[tuple[str, str], str] = {}
        sentinel_rows: list[dict[str, str]] = []
        for row in pending_rows:
            raw, target = link_identity(row)
            if row["replacement"] == "REMOVE_METADATA_DISPLAY":
                sentinel_rows.append(row)
                continue
            key = (target, urlsplit(raw).fragment)
            expected[key] += 1
            prior = replacement_by_key.setdefault(key, row["replacement"])
            if prior != row["replacement"]:
                raise ValueError(f"ambiguous link replacements for {author}: {key}")

        occurrences: list[tuple[re.Match[str], tuple[str, str]]] = []
        actual: Counter[tuple[str, str]] = Counter()
        for match in markdown_matches(text):
            resolved = resolve_link(path, match.group(2))
            if resolved is None:
                continue
            key = (resolved, urlsplit(match.group(2).strip()).fragment)
            if key in expected:
                occurrences.append((match, key))
                actual[key] += 1
        if actual != expected:
            # Crash recovery: every pending local link may already have been
            # replaced in the author, while the ledger write did not land.
            recovered = True
            for row in pending_rows:
                if row["replacement"] == "REMOVE_METADATA_DISPLAY":
                    continue
                display = row["notes"].split("; text=", 1)[-1].split("; ", 1)[0]
                token = f"[{display}]({row['replacement']})"
                if text.count(token) < 1:
                    recovered = False
                    break
            if not recovered:
                raise ValueError(
                    f"link occurrence mismatch in {author}: "
                    f"expected={dict(expected)} actual={dict(actual)}"
                )
            for row in pending_rows:
                row["status"] = "complete"
                append_note(row, "status recovered from rewritten author")
            save_ledger(rows)
            continue

        replacements: list[tuple[int, int, str]] = []
        for match, key in occurrences:
            replacements.append((match.start(2), match.end(2), replacement_by_key[key]))
        for start, end, replacement in reversed(replacements):
            text = text[:start] + replacement + text[end:]
        if replacements:
            atomic_write(path, text.encode())
        for row in pending_rows:
            row["status"] = "complete"
            if row in sentinel_rows:
                append_note(row, "metadata display removed during unit migration")
            else:
                append_note(row, "local citation replaced semantically")
        save_ledger(rows)


def verify_all_unit_checksums(rows: list[dict[str, str]]) -> None:
    for row in (item for item in rows if item["kind"] == "unit"):
        if row["status"] != "complete":
            raise ValueError(f"unit is not complete: {row['row_id']}")
        path = ROOT / row["destination"]
        ingest = read_document(path)
        primary = current_primary_path(primary_from_unit_row(row))
        checksum = sha256(primary)
        validate_migrated_ingest(ingest, source=row["identity"], checksum=checksum)


def migrate_assets(rows: list[dict[str, str]]) -> None:
    incomplete_links = [
        row["row_id"]
        for row in rows
        if row["kind"] == "link" and row["status"] != "complete"
    ]
    if incomplete_links:
        raise ValueError(f"asset migration requires complete links: {incomplete_links[:10]}")
    verify_all_unit_checksums(rows)
    primary_by_path = {
        primary_from_unit_row(row): row
        for row in rows
        if row["kind"] == "unit"
    }
    for row in (item for item in rows if item["kind"] == "asset"):
        if row["status"] == "complete":
            continue
        source = ROOT / row["source_path"]
        destination = ROOT / row["destination"]
        expected_hash = row["identity"]
        if source.is_file():
            if sha256(source) != expected_hash:
                raise ValueError(f"asset source hash changed: {row['row_id']}")
            if row["source_path"] in primary_by_path:
                ingest_row = primary_by_path[row["source_path"]]
                ingest = read_document(ROOT / ingest_row["destination"])
                if ingest.frontmatter["snapshot_sha256"] != expected_hash:
                    raise ValueError(
                        f"primary asset is not durably hashed: {row['source_path']}"
                    )
            destination.parent.mkdir(parents=True, exist_ok=True)
            if destination.exists():
                if destination.read_bytes() != source.read_bytes():
                    raise ValueError(
                        f"different bytes occupy asset destination: {row['destination']}"
                    )
                if source != destination:
                    source.unlink()
            else:
                source.rename(destination)
        elif destination.is_file():
            if sha256(destination) != expected_hash:
                raise ValueError(f"moved asset hash mismatch: {row['row_id']}")
        else:
            raise FileNotFoundError(
                f"asset absent from source and destination: {row['row_id']}"
            )
        if sha256(destination) != expected_hash:
            raise ValueError(f"asset bytes changed during move: {row['row_id']}")
        row["status"] = "complete"
        append_note(row, f"moved_sha256={expected_hash}")
        save_ledger(rows)


def normalize_link_targets(text: str) -> str:
    replacements = [
        (match.start(2), match.end(2), "<LINK-TARGET>")
        for match in markdown_matches(text)
    ]
    for start, end, replacement in reversed(replacements):
        text = text[:start] + replacement + text[end:]
    return text


def section_text(body: str, heading: str) -> str:
    pattern = re.compile(
        rf"(?ms)^## {re.escape(heading)}\s*\n(.*?)(?=^## |\Z)"
    )
    match = pattern.search(body)
    if match is None:
        raise ValueError(f"missing section during body audit: {heading}")
    return match.group(1)


def audit_tracked_analytical_sections(rows: list[dict[str, str]]) -> int:
    headings = (
        "Summary",
        "Connections Found",
        "Extractable Value",
        "Limitations (our opinion)",
        "Recommended Next Action",
    )
    audited = 0
    for row in (item for item in rows if item["kind"] == "unit"):
        original = subprocess.run(
            ["git", "show", f"HEAD:{row['source_path']}"],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        if original.returncode != 0:
            continue
        original_doc = read_document_from_text(ROOT / row["source_path"], original.stdout)
        migrated_doc = read_document(ROOT / row["destination"])
        for heading in headings:
            before = normalize_link_targets(section_text(original_doc.body, heading))
            after = normalize_link_targets(section_text(migrated_doc.body, heading))
            if before != after:
                raise ValueError(
                    f"analytical section changed beyond link targets: "
                    f"{row['source_path']} :: {heading}"
                )
        audited += 1
    return audited


def audit_final(rows: list[dict[str, str]]) -> dict[str, int]:
    statuses = Counter(row["status"] for row in rows)
    if statuses != {"complete": len(rows)}:
        raise ValueError(f"nonterminal ledger rows remain: {dict(statuses)}")
    units = [row for row in rows if row["kind"] == "unit"]
    assets = [row for row in rows if row["kind"] == "asset"]
    links = [row for row in rows if row["kind"] == "link"]
    current_docs = typed_markdown()
    current_ingests = {
        rel(doc.path): doc
        for doc in current_docs
        if doc.frontmatter.get("type") == INGEST_TYPE
    }
    expected_ingests = {row["destination"] for row in units}
    if set(current_ingests) != expected_ingests:
        raise ValueError(
            "final unit parity failed: "
            f"missing={sorted(expected_ingests - set(current_ingests))[:10]} "
            f"extra={sorted(set(current_ingests) - expected_ingests)[:10]}"
        )

    expected_local = {row["destination"] for row in assets}
    actual_local = {
        rel(path)
        for path in (SOURCES / ".snapshots").iterdir()
        if path.is_file()
    }
    if actual_local != expected_local:
        raise ValueError(
            "final asset parity failed: "
            f"missing={sorted(expected_local - actual_local)[:10]} "
            f"extra={sorted(actual_local - expected_local)[:10]}"
        )
    position_row = row_map(rows)[f"asset:{POSITION_DEST}"]
    position_hash = hashlib.sha256(position_materialization_bytes(position_row)).hexdigest()
    for row in assets:
        destination = ROOT / row["destination"]
        expected_hash = (
            position_hash if row["destination"] == POSITION_DEST else row["identity"]
        )
        if sha256(destination) != expected_hash:
            raise ValueError(f"final asset checksum mismatch: {row['row_id']}")
        if row["source_path"].startswith("kb/sources/") and (
            ROOT / row["source_path"]
        ).exists():
            raise ValueError(f"retiring asset still exists: {row['source_path']}")

    checksums: dict[str, str] = {}
    for row in units:
        ingest = current_ingests[row["destination"]]
        primary_destination = asset_destination(primary_from_unit_row(row))
        primary = ROOT / primary_destination
        checksum = sha256(primary)
        validate_migrated_ingest(
            ingest,
            source=row["identity"],
            checksum=checksum,
        )
        prior = checksums.setdefault(checksum, row["destination"])
        if prior != row["destination"]:
            raise ValueError(
                f"duplicate primary checksum: {checksum}: {prior}, {row['destination']}"
            )

    local_paths = "\n".join(sorted(expected_local)) + "\n"
    ignored = subprocess.run(
        ["git", "check-ignore", "--stdin"],
        cwd=ROOT,
        input=local_paths,
        text=True,
        capture_output=True,
        check=False,
    )
    ignored_paths = set(ignored.stdout.splitlines())
    if ignored_paths != expected_local:
        raise ValueError(
            f"local cache ignore parity failed: {len(ignored_paths)} != {len(expected_local)}"
        )
    tracked_local = git_paths("ls-files", scope="kb/sources/.snapshots")
    if tracked_local:
        raise ValueError(f"local cache contains tracked files: {sorted(tracked_local)[:10]}")

    tracked_all = git_paths("ls-files")
    retiring_targets = {
        row["source_path"]
        for row in assets
        if row["source_path"].startswith("kb/sources/")
    }
    authors = durable_authors(
        docs=current_docs,
        tracked_all=tracked_all,
        retiring_targets=retiring_targets,
    )
    remaining_retiring_links: list[tuple[str, str]] = []
    local_cache_links: list[tuple[str, str]] = []
    for author in authors:
        if not author.is_file():
            continue
        text = author.read_text(encoding="utf-8")
        for match in markdown_matches(text):
            target = resolve_link(author, match.group(2))
            if target in retiring_targets:
                remaining_retiring_links.append((rel(author), match.group(2)))
            if target is not None and target.startswith("kb/sources/.snapshots/"):
                local_cache_links.append((rel(author), match.group(2)))
    if remaining_retiring_links or local_cache_links:
        raise ValueError(
            f"durable local-source links remain: retiring={remaining_retiring_links[:10]} "
            f"cache={local_cache_links[:10]}"
        )
    analytical_audits = audit_tracked_analytical_sections(rows)
    return {
        "terminal_rows": len(rows),
        "unit_parity": len(expected_ingests),
        "asset_parity": len(expected_local),
        "link_rows_terminal": len(links),
        "remaining_retiring_links": 0,
        "remaining_local_cache_links": 0,
        "primary_checksums_verified": len(checksums),
        "ignored_local_files": len(ignored_paths),
        "tracked_analytical_bodies_audited": analytical_audits,
    }


def verify_ledger(expected: list[dict[str, str]]) -> None:
    actual = read_ledger()
    expected_by_id = {row["row_id"]: row for row in expected}
    actual_by_id = {row["row_id"]: row for row in actual}
    if len(actual) != len(actual_by_id):
        raise ValueError("ledger has duplicate row ids")
    missing = sorted(expected_by_id.keys() - actual_by_id.keys())
    extra = sorted(actual_by_id.keys() - expected_by_id.keys())
    changed = sorted(
        row_id
        for row_id in expected_by_id.keys() & actual_by_id.keys()
        if any(
            expected_by_id[row_id][field] != actual_by_id[row_id][field]
            for field in LEDGER_FIELDS
            if field != "status"
        )
    )
    if missing or extra or changed:
        raise ValueError(
            f"ledger parity failed: missing={missing[:10]} extra={extra[:10]} "
            f"changed={changed[:10]}"
        )


def print_counts(counts: dict[str, int]) -> None:
    for key, value in counts.items():
        print(f"{key}\t{value}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "command",
        choices=(
            "inventory",
            "refresh-inventory",
            "verify-ledger",
            "dry-run",
            "apply-units",
            "apply-links",
            "apply-assets",
            "apply-all",
            "audit-final",
        ),
    )
    args = parser.parse_args()
    if args.command in {"inventory", "refresh-inventory", "verify-ledger", "dry-run"}:
        discovered, counts = discover_rows()
    else:
        discovered, counts = [], {}
    if args.command == "inventory":
        write_ledger(discovered)
        print(f"wrote\t{LEDGER.relative_to(ROOT)}")
    elif args.command == "refresh-inventory":
        write_ledger(discovered, refresh=True)
        print(f"refreshed\t{LEDGER.relative_to(ROOT)}")
    elif args.command == "dry-run":
        verify_ledger(discovered)
        audit = dry_run(read_ledger())
        print("dry_run\tPASS")
        print_counts(audit)
    elif args.command == "verify-ledger":
        verify_ledger(discovered)
        print("ledger_parity\tPASS")
    else:
        rows = read_ledger()
        if args.command in {"apply-units", "apply-all"}:
            materialize_position(rows)
            migrate_units(rows)
            normalize_migrated_metadata_gaps(rows)
            normalize_migrated_classification_gaps(rows)
            print("units\tCOMPLETE")
        if args.command in {"apply-links", "apply-all"}:
            migrate_links(rows)
            print("links\tCOMPLETE")
        if args.command in {"apply-assets", "apply-all"}:
            migrate_assets(rows)
            print("assets\tCOMPLETE")
        if args.command == "audit-final":
            audit = audit_final(rows)
            print("final_audit\tPASS")
            print_counts(audit)
        status_counts = Counter(row["status"] for row in rows)
        print(f"ledger_status\t{dict(status_counts)}")
    if counts:
        print_counts(counts)
    return 0


if __name__ == "__main__":
    sys.exit(main())
