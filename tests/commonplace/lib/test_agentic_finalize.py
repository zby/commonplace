from __future__ import annotations

from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from commonplace.lib.agentic_finalize import (
    build_manifest,
    finalize_memory,
    finalize_memory_report,
    reconciliation_rows,
    render_finalization_summary,
)

OVERVIEW = """## Reconciliation

Prose before the table.

| specialist proposal | canonical record | disposition |
|---|---|---|
| MEM-OBJ-1 | OBJ-2 | registered in memory member |
| MEM-RTE-1 | RTE-1 | merged into runtime record; memory annotation |
| MEM-OBJ-2 | OBJ-3 | rejected |

## Bounded synthesis
"""

RUNTIME = """## Shared records

### Routes

#### RTE-1 — Runtime route

Declared by the runtime member.
"""

REPORT = """---
{
  "type": "types/agent-memory-analysis-report.md",
  "finalized-from": null,
  "memory-comparison": {"records": ["MEM-OBJ-1", "MEM-RTE-1"]}
}
---

## Shared records

### Operative objects

#### MEM-OBJ-1 — Kept object

See MEM-RTE-1 and MEM-OBJ-10.

#### MEM-OBJ-2 — Rejected object

Body that goes away.

##### Detail under the rejected object

More of it.

### Routes

#### MEM-RTE-1 — Merged route

Fields.

## Limitations and checks

Fixture.
"""

# MEM-OBJ-10 is not a proposal in the table; a report that uses it is refused.
REPORT_OK = REPORT.replace("See MEM-RTE-1 and MEM-OBJ-10.", "See MEM-RTE-1.")


def run(report: str = REPORT_OK, overview: str = OVERVIEW, runtime: str = RUNTIME):
    return finalize_memory_report(report, overview_body=overview, runtime_body=runtime)


def test_reconciliation_rows_parse_the_specialist_table() -> None:
    assert reconciliation_rows(OVERVIEW) == {
        "MEM-OBJ-1": ("OBJ-2", "registered in memory member"),
        "MEM-RTE-1": ("RTE-1", "merged into runtime record; memory annotation"),
        "MEM-OBJ-2": ("OBJ-3", "rejected"),
    }


def test_reconciliation_needs_a_table() -> None:
    with pytest.raises(ValueError, match="no specialist proposal table"):
        reconciliation_rows("## Reconciliation\n\nprose only\n")


def test_mapping_conversion_removal_and_pin() -> None:
    result = run()

    assert "MEM-" not in result.text
    assert "#### OBJ-2 — Kept object" in result.text
    assert "See RTE-1." in result.text
    assert "#### On RTE-1 — Merged route" in result.text
    assert "Rejected object" not in result.text
    assert "Detail under the rejected object" not in result.text
    assert '"records": ["OBJ-2", "RTE-1"]' in result.text
    assert f'"finalized-from": "{sha256(REPORT_OK.encode()).hexdigest()}"' in result.text
    assert result.text.endswith("\n\n## Amendments\n\nnone\n")
    assert result.mapped == {"MEM-OBJ-1": "OBJ-2", "MEM-RTE-1": "RTE-1"}
    assert result.converted == ("RTE-1",)
    assert result.removed == ("MEM-OBJ-2",)


def test_a_seeded_record_the_specialist_redeclared_becomes_an_annotation() -> None:
    report = REPORT_OK.replace(
        "## Limitations and checks",
        "#### RTE-1 — Seeded route\n\nRe-declared.\n\n## Limitations and checks",
    )

    assert "#### On RTE-1 — Seeded route" in run(report).text


def test_summary_lists_the_mechanical_edits() -> None:
    summary = render_finalization_summary(run())

    assert "2 proposal IDs" in summary
    assert "1 merged headings converted" in summary
    assert "rejected proposals removed (MEM-OBJ-2)" in summary
    assert "memory-report.md" in summary


def test_unmapped_proposal_is_refused() -> None:
    with pytest.raises(ValueError, match="missing from the Reconciliation table: MEM-OBJ-10"):
        run(REPORT)


def test_rejected_proposal_still_referenced_is_returned_to_the_specialist() -> None:
    report = REPORT_OK.replace("Fields.", "Depends on MEM-OBJ-2.")

    with pytest.raises(ValueError, match="return the report to the specialist: MEM-OBJ-2"):
        run(report)


def test_merged_row_needs_a_declaring_member() -> None:
    with pytest.raises(ValueError, match="marked merged but no other member declares RTE-1"):
        run(runtime="## Shared records\n\nnone\n")


def test_row_for_a_record_another_member_declares_must_say_merged() -> None:
    overview = OVERVIEW.replace(
        "merged into runtime record; memory annotation", "registered in memory member"
    )

    with pytest.raises(ValueError, match="not marked merged"):
        run(overview=overview)


def test_headings_inside_fences_are_left_alone() -> None:
    report = REPORT_OK.replace(
        "Fields.", "```\n#### RTE-1 — Example heading\nkept text\n```\n"
    )

    text = run(report).text

    assert "```\n#### RTE-1 — Example heading\nkept text\n```" in text
    assert "#### On RTE-1 — Merged route" in text


@pytest.mark.parametrize(
    ("edit", "message"),
    [
        (lambda t: t.replace('"finalized-from": null,', ""), "no `finalized-from: null`"),
        (lambda t: t + "\n## Amendments\n\nnone\n", "already has an Amendments section"),
    ],
)
def test_report_shapes_that_are_not_mechanical_are_refused(edit, message: str) -> None:
    with pytest.raises(ValueError, match=message):
        run(edit(REPORT_OK))


def test_finalize_memory_writes_the_member_from_a_run_directory(tmp_path: Path) -> None:
    run_dir = tmp_path / "AAS-2026-09-04-example-system-01"
    (run_dir / "output").mkdir(parents=True)
    (run_dir / "memory-report.md").write_text(REPORT_OK, encoding="utf-8")
    for name, body in (("overview.md", OVERVIEW), ("runtime.md", RUNTIME)):
        (run_dir / "output" / name).write_text(f"---\ntype: t\n---\n\n{body}", encoding="utf-8")

    first = finalize_memory(run_dir)
    written = (run_dir / "output" / "memory.md").read_text(encoding="utf-8")
    second = finalize_memory(run_dir)

    assert written == first.text == second.text


def test_finalize_memory_names_a_missing_input(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="missing:"):
        finalize_memory(tmp_path)


def test_manifest_pins_the_members_present(tmp_path: Path) -> None:
    output = tmp_path / "output"
    output.mkdir()
    (output / "overview.md").write_text("overview", encoding="utf-8")
    (output / "runtime.md").write_text("runtime", encoding="utf-8")
    (output / "notes.md").write_text("not a member", encoding="utf-8")

    text = build_manifest(tmp_path)

    manifest = yaml.safe_load((output / "ARTIFACT.yaml").read_text(encoding="utf-8"))
    assert manifest == yaml.safe_load(text)
    assert manifest["type"] == "reports/types/agentic-system-analysis-set.md"
    assert list(manifest["members"]) == ["overview.md", "runtime.md"]
    assert manifest["members"]["runtime.md"] == {"sha256": sha256(b"runtime").hexdigest()}


def test_manifest_follows_a_member_edit(tmp_path: Path) -> None:
    output = tmp_path / "output"
    output.mkdir()
    (output / "overview.md").write_text("one", encoding="utf-8")
    before = build_manifest(tmp_path)
    (output / "overview.md").write_text("two", encoding="utf-8")

    assert build_manifest(tmp_path) != before


def test_manifest_needs_an_overview(tmp_path: Path) -> None:
    (tmp_path / "output").mkdir()

    with pytest.raises(ValueError, match="missing:"):
        build_manifest(tmp_path)


class _State:
    def __init__(self, run_dir: Path, status: str = "running") -> None:
        self.run_dir = run_dir
        self.status = status


def _cli(monkeypatch, tmp_path: Path, state: _State, *argv: str) -> int:
    from commonplace.cli import agentic_analysis_finalize

    monkeypatch.chdir(tmp_path)
    monkeypatch.setattr(agentic_analysis_finalize, "load_run_state", lambda *a, **k: state)
    return agentic_analysis_finalize.main([*argv, "run-state.md"])


@pytest.mark.usefixtures("tmp_library")
def test_command_finalizes_and_pins_a_running_run(tmp_path: Path, monkeypatch, capsys) -> None:
    run_dir = tmp_path / "run"
    (run_dir / "output").mkdir(parents=True)
    (run_dir / "memory-report.md").write_text(REPORT_OK, encoding="utf-8")
    for name, body in (("overview.md", OVERVIEW), ("runtime.md", RUNTIME)):
        (run_dir / "output" / name).write_text(f"---\ntype: t\n---\n\n{body}", encoding="utf-8")

    assert _cli(monkeypatch, tmp_path, _State(run_dir), "memory") == 0
    assert "Finalization made only" in capsys.readouterr().out
    assert _cli(monkeypatch, tmp_path, _State(run_dir), "manifest") == 0
    assert "memory.md" in yaml.safe_load((run_dir / "output" / "ARTIFACT.yaml").read_text())["members"]


@pytest.mark.usefixtures("tmp_library")
def test_command_refuses_a_run_that_is_not_running(tmp_path: Path, monkeypatch, capsys) -> None:
    assert _cli(monkeypatch, tmp_path, _State(tmp_path, "complete"), "memory") == 1
    assert "not running" in capsys.readouterr().err
