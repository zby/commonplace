from __future__ import annotations

from pathlib import Path

import pytest

from commonplace.lib.agentic_ledger import epistemic_ledger_errors
from commonplace.lib.validation import validate_note
from tests.commonplace.lib.test_agentic_analysis import member_fixture

HEADER = "| route ID | route function | architectural status | gap/limit |\n|---|---|---|---|\n"
ROW = "| `RTE-model-call` | content transformation | implemented | no observed candidate |\n"


def errors(ledger: str) -> list[str]:
    return epistemic_ledger_errors("## Authority-route ledger\n\n" + ledger)


def test_quotations_cannot_silently_interrupt_a_ledger_table() -> None:
    quote = '\n> excerpt\n> --- `src/example.rs:1-1` @ `abc`\n\n'
    assert any("orphan table row" in error for error in errors(HEADER + ROW + quote + ROW))
    assert errors(HEADER + ROW + quote + HEADER + ROW) == []


@pytest.mark.parametrize(("row", "diagnostic"), [
    (ROW.replace("content transformation", "truth-apt transformation"), "invalid route function"),
    (ROW.replace("implemented", "implemented and observed"), "invalid architectural status"),
    (ROW.replace(" | no observed candidate", ""), "cells"),
    (ROW.rstrip('\n|') + '\n', "end with a pipe"),
])
def test_malformed_table_rows_are_refused(row: str, diagnostic: str) -> None:
    assert any(diagnostic in error for error in errors(HEADER + row))


def test_tables_require_matching_separator_and_core_columns() -> None:
    assert errors(HEADER.replace("|---|---|---|---|", "|---|---|") + ROW)
    assert errors(HEADER.replace("route function", "function") + ROW)
    assert errors(HEADER.replace("gap/limit", "route function") + ROW)


def test_literal_pipes_must_be_escaped_even_inside_code() -> None:
    assert errors(HEADER + ROW.replace("no observed candidate", "`left|right`"))
    assert errors(HEADER + ROW.replace("no observed candidate", r"`left\|right`")) == []


def test_controlled_values_accept_code_formatting_and_described_other_functions() -> None:
    assert errors(HEADER + ROW.replace("content transformation", "`other — custom check`")) == []
    assert errors(HEADER + ROW.replace("implemented", "`doctrine only`")) == []
    assert errors(HEADER + ROW.replace("content transformation", "other — "))


COMPACT = "Route ID: RTE-model-call\nRoute function: retention\nArchitectural status: implemented\n"


def test_compact_records_preserve_controlled_fields_without_wide_tables() -> None:
    assert errors(COMPACT + '\n' + COMPACT.replace("RTE-model-call", "RTE-memory-update")) == []
    assert errors(COMPACT.replace("retention", "truth-apt transformation"))
    assert errors(COMPACT.replace("Route function: retention\n", ""))
    assert errors(COMPACT.replace("retention", ""))
    assert errors(COMPACT + "Route function: retention\n")


def test_source_examples_are_not_ledger_records() -> None:
    evidence = '\n```text\n' + HEADER + ROW.replace("implemented", "bogus") + '```\n'
    evidence += '\n> Route ID: RTE-missing\n> Route function: bogus\n'
    assert errors(COMPACT + evidence) == []


def test_empty_ledger_has_an_explicit_disposition() -> None:
    assert errors("no route found within boundary") == []
    assert errors("Ledger.")


@pytest.mark.usefixtures("tmp_library")
def test_standing_validation_rejects_ledger_defects(tmp_path: Path) -> None:
    report = member_fixture(tmp_path) / "set/epistemic.md"
    text = report.read_text()
    start = text.index("## Authority-route ledger")
    end = text.index("## System-claim versus route comparison")
    report.write_text(text[:start] + "## Authority-route ledger\n\n" + HEADER
                      + ROW.replace("content transformation", "truth-apt transformation")
                      + '\n> evidence\n\n' + ROW + '\n' + text[end:])
    failures = validate_note(report, repo_root=tmp_path).fails
    assert any("invalid route function" in error for error in failures)
    assert any("orphan table row" in error for error in failures)


@pytest.mark.usefixtures("tmp_library")
def test_complete_memory_report_cannot_retain_pending_validation(tmp_path: Path) -> None:
    report = member_fixture(tmp_path) / "set/memory.md"
    original = report.read_text()
    report.write_text(original + "\nValidation: pending.\n")
    assert any("memory checks" in error for error in validate_note(report, repo_root=tmp_path).fails)
    report.write_text(original + "\nValidation: passed after repair.\n")
    assert not any("memory checks" in error for error in validate_note(report, repo_root=tmp_path).fails)
    report.write_text(original + "\n```text\nValidation: pending.\n```\n")
    assert not any("memory checks" in error for error in validate_note(report, repo_root=tmp_path).fails)
