"""Mechanical finalization of an analysis set: the memory member and the manifest.

The coordinator finalizes the specialist's local ``memory-report.md`` into
``output/memory.md`` by mechanical edits only, then pins every member in
``output/ARTIFACT.yaml``. Both steps are derived here from bytes on disk, so
they are reproducible; every judgment they depend on lives in the overview's
Reconciliation table.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from hashlib import sha256
from pathlib import Path

import yaml

from commonplace.lib.agentic_records import _RECORD_ID, declared_ids, section
from commonplace.lib.agentic_set import (
    LOCAL_REPORT_NAME,
    MANIFEST_NAME,
    OUTPUT_DIR,
    OVERVIEW_NAME,
    SET_NAMES,
    SET_TYPE,
)
from commonplace.lib.note_parser import parse_document

_MEM_TOKEN = re.compile(rf"(?<![\w-])MEM-{_RECORD_ID}(?![\w-])")
_CANONICAL = re.compile(rf"^{_RECORD_ID}$")
_DECLARATION_LINE = re.compile(rf"^####[ \t]+({_RECORD_ID})([ \t]+—[ \t]+\S.*)$")
_FINALIZED_FROM = re.compile(r'(?m)^(\s*"?finalized-from"?\s*:\s*)null(\s*,?\s*)$')
_FENCE = re.compile(r"^\s*(`{3,}|~{3,})")
_TABLE_HEADER = ("specialist proposal", "canonical record", "disposition")
_REJECTED = "rejected"


@dataclass(frozen=True)
class Finalization:
    text: str
    mapped: dict[str, str]
    converted: tuple[str, ...]
    removed: tuple[str, ...]
    source_sha256: str


def reconciliation_rows(overview_body: str) -> dict[str, tuple[str, str]]:
    """The specialist proposal mapping: proposal ID -> (canonical record, disposition)."""
    lines = section(overview_body, "Reconciliation").splitlines()
    rows: dict[str, tuple[str, str]] = {}
    in_table = False
    for line in lines:
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if not line.strip().startswith("|"):
            in_table = False
            continue
        if tuple(cell.lower() for cell in cells) == _TABLE_HEADER:
            in_table = True
            continue
        if not in_table or set("".join(cells)) <= set("-: "):
            continue
        if len(cells) != 3:
            raise ValueError(f"Reconciliation row does not have three cells: {line.strip()}")
        proposal, canonical, disposition = cells
        if not _MEM_TOKEN.fullmatch(proposal):
            raise ValueError(f"Reconciliation row names a non-proposal ID: {proposal}")
        if proposal in rows:
            raise ValueError(f"Reconciliation maps {proposal} twice")
        rows[proposal] = (canonical, disposition)
    if not rows:
        raise ValueError("overview Reconciliation has no specialist proposal table")
    return rows


def _lines_outside_fences(lines: list[str]) -> list[bool]:
    outside, fence = [], None
    for line in lines:
        marker = _FENCE.match(line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            outside.append(False)
        else:
            outside.append(fence is None)
    return outside


def _remove_proposal_sections(text: str, rejected: set[str]) -> tuple[str, list[str]]:
    """Drop each rejected proposal's heading and body, up to the next heading of level 1-4."""
    lines = text.splitlines(keepends=True)
    outside = _lines_outside_fences([line.rstrip("\n") for line in lines])
    kept, removed, skipping = [], [], False
    for line, is_prose in zip(lines, outside):
        heading = re.match(r"^(#{1,4})[ \t]+(\S+)", line) if is_prose else None
        if heading:
            skipping = heading[2] in rejected and len(heading[1]) == 4
            if skipping:
                removed.append(heading[2])
        if not skipping:
            kept.append(line)
    return "".join(kept), removed


def _convert_declarations(text: str, elsewhere: set[str]) -> tuple[str, list[str]]:
    """Rewrite a declaration of a record another member declares to an annotation."""
    lines = text.splitlines(keepends=True)
    outside = _lines_outside_fences([line.rstrip("\n") for line in lines])
    converted = []
    for index, (line, is_prose) in enumerate(zip(lines, outside)):
        match = _DECLARATION_LINE.match(line.rstrip("\n")) if is_prose else None
        if match and match[1] in elsewhere:
            newline = "\n" if line.endswith("\n") else ""
            lines[index] = f"#### On {match[1]}{match[2]}{newline}"
            converted.append(match[1])
    return "".join(lines), converted


def finalize_memory_report(
    report_text: str, *, overview_body: str, runtime_body: str
) -> Finalization:
    """Apply the Reconciliation table to the specialist's local report.

    Refuses instead of guessing: an unmapped proposal, a rejected proposal
    that other findings still reference, a merged row whose target no other
    member declares, and a row whose target another member declares but which
    is not marked merged.
    """
    rows = reconciliation_rows(overview_body)
    tokens = set(_MEM_TOKEN.findall(report_text))
    unmapped = sorted(tokens - rows.keys())
    if unmapped:
        raise ValueError("proposals missing from the Reconciliation table: " + ", ".join(unmapped))

    rejected = {p for p, (_, disposition) in rows.items() if disposition.lower() == _REJECTED}
    text, removed = _remove_proposal_sections(report_text, rejected)
    still_referenced = sorted(rejected & set(_MEM_TOKEN.findall(text)))
    if still_referenced:
        raise ValueError(
            "rejected proposals are still referenced by other findings; return the report "
            "to the specialist: " + ", ".join(still_referenced)
        )

    mapped = {}
    for proposal, (canonical, disposition) in rows.items():
        if proposal in rejected or proposal not in tokens:
            continue
        if not _CANONICAL.match(canonical):
            raise ValueError(f"{proposal}: canonical record is not a record ID: {canonical!r}")
        mapped[proposal] = canonical
    text = _MEM_TOKEN.sub(lambda match: mapped[match[0]], text)

    elsewhere = set(declared_ids(runtime_body))
    for proposal, canonical in mapped.items():
        merged = "merged" in rows[proposal][1].lower()
        if merged and canonical not in elsewhere:
            raise ValueError(f"{proposal}: marked merged but no other member declares {canonical}")
        if not merged and canonical in elsewhere:
            raise ValueError(
                f"{proposal}: {canonical} is declared by another member but the row is not marked merged"
            )
    text, converted = _convert_declarations(text, elsewhere)

    if re.search(r"(?m)^## Amendments[ \t]*$", text):
        raise ValueError("the local report already has an Amendments section")
    source_sha256 = sha256(report_text.encode("utf-8")).hexdigest()
    text, count = _FINALIZED_FROM.subn(
        lambda match: f'{match[1]}"{source_sha256}"{match[2]}', text, count=1
    )
    if count != 1:
        raise ValueError("the local report's frontmatter has no `finalized-from: null` to set")
    text = text.rstrip("\n") + "\n\n## Amendments\n\nnone\n"
    return Finalization(text, mapped, tuple(converted), tuple(removed), source_sha256)


def render_finalization_summary(result: Finalization) -> str:
    """The mechanical edits, for the overview Reconciliation's list of them."""
    parts = [f"exact-token mapping of {len(result.mapped)} proposal IDs"]
    if result.converted:
        parts.append(
            f"{len(result.converted)} merged headings converted to `On <ID>` annotations ("
            + ", ".join(result.converted) + ")"
        )
    if result.removed:
        parts.append("rejected proposals removed (" + ", ".join(result.removed) + ")")
    parts.append("`finalized-from` set and an `## Amendments` section appended")
    return (
        f"Local report `{LOCAL_REPORT_NAME}` SHA-256 `{result.source_sha256}`. "
        "Finalization made only: " + "; ".join(parts) + "."
    )


def finalize_memory(run_dir: Path) -> Finalization:
    """Read the run directory, write ``output/memory.md``, return what changed."""
    output = run_dir / OUTPUT_DIR
    report = run_dir / LOCAL_REPORT_NAME
    overview = output / OVERVIEW_NAME
    runtime = output / "runtime.md"
    for path in (report, overview, runtime):
        if not path.is_file():
            raise ValueError(f"missing: {path}")
    bodies = {}
    for path in (overview, runtime):
        document, error = parse_document(path.read_text(encoding="utf-8"))
        if error is not None or document is None:
            raise ValueError(f"cannot parse {path.name}: {error}")
        bodies[path.name] = document.body
    result = finalize_memory_report(
        report.read_text(encoding="utf-8"),
        overview_body=bodies[OVERVIEW_NAME],
        runtime_body=bodies["runtime.md"],
    )
    (output / "memory.md").write_text(result.text, encoding="utf-8")
    return result


def build_manifest(run_dir: Path) -> str:
    """Write ``output/ARTIFACT.yaml`` pinning the set members present in ``output/``."""
    output = run_dir / OUTPUT_DIR
    members = {}
    for name in SET_NAMES:
        path = output / name
        if path.is_file():
            members[name] = {"sha256": sha256(path.read_bytes()).hexdigest()}
    if OVERVIEW_NAME not in members:
        raise ValueError(f"missing: {output / OVERVIEW_NAME}")
    text = yaml.safe_dump({"type": SET_TYPE, "members": members}, sort_keys=False)
    (output / MANIFEST_NAME).write_text(text, encoding="utf-8")
    return text
