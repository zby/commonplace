"""Report-only stats: no runner, validators, source snapshots or runtime stores."""

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

from tests.commonplace.link_helpers import symlink_or_skip

SCRIPT = Path(__file__).resolve().parents[3] / "scripts/agentic_system_rerun_stats.py"
spec = importlib.util.spec_from_file_location("rerun_stats", SCRIPT)
stats = importlib.util.module_from_spec(spec)
spec.loader.exec_module(stats)
RUN = "AAS-2026-10-12-example-token-01"


def report(run_id=RUN, disposition=None, body=""):
    fields = f"run-id: {run_id}\n"
    if disposition:
        fields += f"result-disposition: {disposition}\n"
    return f"---\n{fields}---\n\n# Report\n\n{body}"


def make_set(path, run_id=RUN, disposition="complete"):
    path.mkdir(parents=True)
    members = stats.MEMBERS if disposition == "complete" else ("boundary", "overview")
    for name in members:
        body = "Failure handling is a property of the target, not a rerun verdict.\n"
        if name in stats.VERIFIERS:
            body += "\n## Verification\n\nEarlier failures repaired.\n\n## Blockers\n\nnone\n\n## Limits\n\nnone\n"
        if name == "overview":
            body += "\n## Deterministic validation\n\n" + "\n".join(
                f"- `{member}.md`: deterministic snapshot checks passed." for member in members
            ) + "\n"
        (path / f"{name}.md").write_text(report(run_id, disposition if name in ("overview", "boundary") else None, body))
    return path


def test_clean_accepted_and_no_lexical_prose_verdict(tmp_path):
    path = make_set(tmp_path / "example")
    result = stats.collect([tmp_path], [], None)
    assert result["statuses"]["clean-accepted"] == 1
    assert result["reports_read"] == 12
    assert result["recorded_failure_findings"] == 0
    assert result["sets"][0]["directory"] == str(path)


def test_blockers_limits_and_artifact_check_are_distinct(tmp_path):
    path = make_set(tmp_path / "example")
    verification = path / "report-verification.md"
    verification.write_text(verification.read_text().replace("## Blockers\n\nnone", "## Blockers\n\n- runtime: unsupported claim\n  evidence here").replace("## Limits\n\nnone", "## Limits\n\n- Local inventory gap"))
    (path / "report-check.md").write_text("# Artifact check\n\n- memory.md: bad relation\n")
    result = stats.collect([path], [], None)
    assert result["statuses"]["recorded-failure"] == 1
    assert result["recorded_failure_findings"] == 2
    assert result["recorded_limit_findings"] == 1
    assert not result["sets"][0]["incomplete"]


def test_limits_are_warning_not_failure(tmp_path):
    path = make_set(tmp_path / "example")
    verification = path / "profile-verification.md"
    verification.write_text(verification.read_text().replace("## Limits\n\nnone", "## Limits\n\n- Coarse unit limits comparison"))
    result = stats.collect([path], [], None)
    assert result["statuses"]["accepted-with-limits"] == 1
    assert result["sets_with_recorded_failures"] == 0
    assert result["sets_with_limits"] == 1


@pytest.mark.parametrize("disposition,status", [("blocked", "blocked"), ("out-of-scope", "out-of-scope")])
def test_early_stop_does_not_require_later_stages(tmp_path, disposition, status):
    path = make_set(tmp_path / "example", disposition=disposition)
    result = stats.collect([path], [], None)
    assert result["statuses"][status] == 1
    assert result["incomplete_sets"] == 0
    assert result["sets_with_recorded_failures"] == 0


@pytest.mark.parametrize("change", ["missing-member", "missing-check", "malformed-blockers", "duplicate-blockers", "conflicting-run", "invalid-disposition", "unreadable"])
def test_incomplete_never_counts_as_clean(tmp_path, change):
    path = make_set(tmp_path / "example")
    if change == "missing-member":
        (path / "workflow.md").unlink()
    elif change == "missing-check":
        overview = path / "overview.md"
        overview.write_text(overview.read_text().replace("- `workflow.md`: deterministic snapshot checks passed.", ""))
    elif change == "conflicting-run":
        (path / "workflow.md").write_text(report("AAS-2026-10-11-example-token-01"))
    elif change == "invalid-disposition":
        (path / "boundary.md").write_text(report(disposition="unknown"))
    elif change == "unreadable":
        (path / "workflow.md").write_bytes(b"\xff")
    else:
        verification = path / "report-verification.md"
        verification.write_text(verification.read_text().replace("## Blockers\n\nnone", "## Blockers\n\nNo blockers" if change == "malformed-blockers" else "## Blockers\n\nnone\n\n## Blockers\n\nnone"))
    result = stats.collect([path], [], None)
    assert result["statuses"]["incomplete"] == 1
    assert result["statuses"]["clean-accepted"] == 0
    assert result["sets"][0]["issues"] or result["sets"][0]["missing_reports"]


def test_inflight_reports_without_overview_are_not_accepted(tmp_path):
    path = make_set(tmp_path / "artifact")
    (path / "overview.md").unlink()
    result = stats.collect([path], [], None)
    assert result["statuses"]["incomplete"] == 1
    assert "overview.md" in result["sets"][0]["missing_reports"]


def test_filter_historical_reports_and_deduplicate_overlapping_roots(tmp_path):
    old = make_set(tmp_path / "old", run_id="AAS-2026-10-01-example-token-01")
    current = make_set(tmp_path / "current")
    assert stats.collect([tmp_path, current], [], "2026-10-12")["report_sets"] == 1
    result = stats.collect([tmp_path], [RUN], None)
    assert result["excluded_sets"] == 1
    assert result["sets"][0]["run_id"] == RUN
    assert stats.collect([old], [], "2026-10-12")["report_sets"] == 0


def test_only_named_report_artifacts_are_read(tmp_path, monkeypatch):
    path = make_set(tmp_path / "example")
    for name in ("trace.json", "runtime-store.json", "ARTIFACT.yaml", "README.md"):
        (path / name).write_text("FAIL! These files must not be read")
    make_set(path / "snapshots" / "nested")
    original = Path.read_text
    reads = []

    def guarded_read(file, *args, **kwargs):
        reads.append(file)
        assert file.parent == path
        assert file.name in stats.FILENAMES
        return original(file, *args, **kwargs)

    monkeypatch.setattr(Path, "read_text", guarded_read)
    result = stats.collect([tmp_path], [], None)
    assert result["reports_read"] == 12
    assert len(reads) == 12


def test_report_symlink_is_not_followed(tmp_path):
    path = make_set(tmp_path / "example")
    (path / "workflow.md").unlink()
    outside = tmp_path / "source.txt"
    outside.write_text("source snapshot must not be read")
    symlink_or_skip(path / "workflow.md", outside)
    assert stats.collect([path], [], None)["incomplete_sets"] == 1


@pytest.mark.parametrize("body,status", [("# Artifact check\n\nnone\n", "clean-accepted"), ("# Artifact check\n\nNo failures\n", "incomplete")])
def test_artifact_check_requires_structured_findings(tmp_path, body, status):
    path = make_set(tmp_path / "example")
    (path / "report-check.md").write_text(body)
    result = stats.collect([path], [], None)
    assert result["statuses"][status] == 1
    assert result["recorded_failure_findings"] == 0


def test_same_run_in_two_report_roots_stays_explicit(tmp_path):
    accepted = make_set(tmp_path / "accepted" / "example")
    inflight = make_set(tmp_path / "inflight" / "artifact")
    (inflight / "overview.md").unlink()
    result = stats.collect([accepted, inflight], [], None)
    assert result["report_sets"] == 2
    assert result["statuses"]["clean-accepted"] == 1
    assert result["statuses"]["incomplete"] == 1
    assert [item["run_id"] for item in result["sets"]] == [RUN, RUN]


def test_unidentified_reports_are_explicit_or_filter_excluded(tmp_path):
    path = tmp_path / "artifact"
    path.mkdir()
    (path / "runtime.md").write_text("# Unfinished report\n")
    result = stats.collect([path], [], None)
    assert result["statuses"]["incomplete"] == 1
    assert result["sets"][0]["run_id"] is None
    filtered = stats.collect([path], [], "2026-10-12")
    assert filtered["excluded_sets"] == 1
    assert filtered["report_sets"] == 0


def test_empty_and_missing_roots_are_not_success(tmp_path):
    result = stats.collect([tmp_path], [], None)
    assert result["report_sets"] == 0
    assert result["statuses"]["clean-accepted"] == 0
    assert "Missing reports are not success" in result["caveat"]
    assert stats.collect([tmp_path / "missing"], [], None)["errors"]


def test_cli_json_help_and_errors(tmp_path):
    make_set(tmp_path / "example")
    output = subprocess.run([sys.executable, str(SCRIPT), "--root", str(tmp_path), "--json"], capture_output=True, text=True, check=True)
    assert json.loads(output.stdout)["statuses"]["clean-accepted"] == 1
    help_output = subprocess.run([sys.executable, str(SCRIPT), "--help"], capture_output=True, text=True, check=True)
    assert "--since" in help_output.stdout
    assert "run stores" in help_output.stdout
    missing = subprocess.run([sys.executable, str(SCRIPT), "--root", str(tmp_path / "absent"), "--json"], capture_output=True, text=True, check=False)
    assert missing.returncode == 2
    assert json.loads(missing.stdout)["errors"]
