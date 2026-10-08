"""Check the epistemic ledger's observable syntax and controlled values."""

from __future__ import annotations

import re

from commonplace.lib.note_parser import blank_fenced_code_blocks, section

ROUTE_FUNCTIONS = frozenset({
    "content transformation", "check/evidence production", "disposition/acceptance",
    "retention", "lifecycle integration", "operational admission/selection/consumption",
    "behavior/policy adaptation", "lineage/freshness/recovery",
})
ARCHITECTURAL_STATUSES = frozenset({
    "implemented", "observed, implementation uninspected", "doctrine only",
    "no route found within boundary", "not determinable",
})
_COMPACT_START = re.compile(r"(?im)^Route ID:[ \t]*(\S[^\n]*)$")


def _plain(value: str) -> str:
    return value.strip().strip("`").strip()


def _values(function: str, status: str, where: str) -> list[str]:
    errors = []
    if function not in ROUTE_FUNCTIONS and not (
        function.startswith("other — ") and function.removeprefix("other — ").strip()
    ):
        errors.append(
            f"{where}: invalid route function {function!r}; use one of "
            + ", ".join(sorted(ROUTE_FUNCTIONS)) + ", or 'other — description'"
        )
    if status not in ARCHITECTURAL_STATUSES:
        errors.append(
            f"{where}: invalid architectural status {status!r}; use one of "
            + ", ".join(sorted(ARCHITECTURAL_STATUSES))
        )
    return errors


def epistemic_ledger_errors(body: str) -> list[str]:
    """Check tables, including rows orphaned by quotes, and labeled records.

    This checks structure and two controlled fields, not the truth of a row
    or whether the ledger covers every material function.
    """
    ledger = blank_fenced_code_blocks(section(body, "Authority-route ledger"))
    errors: list[str] = []
    lines = ledger.splitlines()
    header: list[str] | None = None
    rows = 0
    for number, line in enumerate(lines, 1):
        stripped = line.strip()
        if not stripped.startswith("|"):
            header = None
            continue
        cells = [_plain(cell) for cell in re.split(r"(?<!\\)\|", stripped[1:-1])]
        where = f"epistemic ledger line {number}"
        if not stripped.endswith("|"):
            errors.append(f"{where}: table row must end with a pipe")
            continue
        if cells[0].casefold() == "route id":
            candidate = [cell.casefold() for cell in cells]
            if not all(field in candidate for field in (
                "route function", "architectural status",
            )) or len(set(candidate)) != len(candidate):
                errors.append(f"{where}: header needs unique route-function and status columns")
                header = None
                continue
            separator = lines[number].strip() if number < len(lines) else ""
            if (not re.fullmatch(r"\|(?:\s*:?-{3,}:?\s*\|)+", separator)
                    or len(re.split(r"(?<!\\)\|", separator[1:-1])) != len(candidate)):
                errors.append(f"{where}: table header needs a Markdown separator")
                header = None
            else:
                header = candidate
            continue
        if all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells):
            continue
        if header is None:
            errors.append(f"{where}: orphan table row; repeat header and separator after a break")
            continue
        if len(cells) != len(header):
            errors.append(f"{where}: row has {len(cells)} cells, expected {len(header)}")
            continue
        rows += 1
        errors.extend(_values(
            cells[header.index("route function")],
            cells[header.index("architectural status")], where,
        ))

    # Quoted source text is not a compact ledger record.
    prose = "\n".join(line for line in lines if not line.lstrip().startswith(">"))
    starts = list(_COMPACT_START.finditer(prose))
    for index, start in enumerate(starts):
        end = starts[index + 1].start() if index + 1 < len(starts) else len(prose)
        record = prose[start.end():end]
        where = f"epistemic ledger record {_plain(start[1])}"
        fields = []
        complete = True
        for label in ("Route function", "Architectural status"):
            values = re.findall(rf"(?im)^{label}:[ \t]*(.*?)$", record)
            if len(values) != 1:
                errors.append(f"{where}: needs exactly one {label} field")
                complete = False
            fields.append(_plain(values[0]) if len(values) == 1 else "")
        if complete:
            errors.extend(_values(*fields, where))
    if not rows and not starts and not errors and ledger.strip() != "no route found within boundary":
        errors.append("epistemic ledger: use a table, labeled records, or 'no route found within boundary'")
    return errors
