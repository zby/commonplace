from __future__ import annotations

import csv
import io
import json
import shutil
from pathlib import Path

import pytest

from commonplace.lib import agentic_set, library
from scripts import bundle_agentic_landscape as bundle
from tests.commonplace.lib.test_agentic_analysis import (
    MEMBER_TYPES,
    REPO_ROOT,
    RUN_ID,
    digest,
    frontmatter,
    replace_frontmatter,
    valid_run_state,
    write,
)


@pytest.fixture(autouse=True)
def _source_repository_is_the_library(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    """The fixture repository under tmp_path/source carries its own global types."""
    monkeypatch.setenv(library.LIBRARY_ENV, str(tmp_path / "source" / "kb"))


def repin_set(root: Path, review: Path) -> None:
    """Re-pin the overview manifest and the review after a member edit."""
    overview = root / frontmatter(review)["analysis-overview"]
    data = frontmatter(overview)
    data["members"] = [
        {"path": name, "sha256": digest(overview.with_name(name)), "type": MEMBER_TYPES[name]}
        for name in MEMBER_TYPES
    ]
    replace_frontmatter(overview, data)
    replace_frontmatter(
        review, {**frontmatter(review), "analysis-overview-sha256": digest(overview)}
    )


def copy_member(root: Path, original: str, name: str) -> Path:
    """Copy one review and its retained set under another system name."""
    review = root / f"kb/agentic-systems/reviews/{original}.md"
    old_dir = (root / frontmatter(review)["analysis-overview"]).parent
    new_review = write(
        review.with_name(name + ".md"), review.read_text().replace(original, name)
    )
    new_dir = (root / frontmatter(new_review)["analysis-overview"]).parent
    for path in old_dir.iterdir():
        write(new_dir / path.name, path.read_text().replace(original, name))
    repin_set(root, new_review)
    return new_review


@pytest.fixture
def landscape_source(tmp_path: Path) -> Path:
    root = tmp_path / "source"
    valid_run_state(root)
    for path in bundle.METHOD_INPUTS:
        target = root / path
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO_ROOT / path, target)
    members = (
        ("wired-fixture", "code-grounded", "wired", ["files", "sqlite"]),
        ("claimed-fixture", "code-grounded", "claimed", ["vector"]),
        ("unknown-fixture", "code-grounded", None, []),
        ("doc-fixture", "doc-grounded", "claimed", ["sqlite"]),
    )
    for name, tier, basis, values in members:
        review = copy_member(root, "example-system", name)
        overview = root / frontmatter(review)["analysis-overview"]
        memory = overview.with_name("memory.md")
        data = frontmatter(overview)
        data["system"] = name
        data["evidence-tier"] = tier
        replace_frontmatter(overview, data)
        profile = frontmatter(memory)
        profile["memory-comparison"]["axes"]["storage_substrate"].update(
            assessment="known" if basis else "uninspected",
            evidence={v: {"basis": basis, "records": ["OBJ-2"], "note": "Fixture witness."} for v in values},
            values=values,
            records=["OBJ-2"] if basis else [],
        )
        replace_frontmatter(memory, profile)
        if name == "wired-fixture":
            memory.write_text(
                memory.read_text().replace(
                    "Proposed store, from SRC-1.",
                    "The store OBJ-2 keeps session notes in Markdown files and rebuilds a SQLite lookup index from them. This is fixture wiring, not an observed run.",
                )
            )
        repin_set(root, review)
    (root / "kb/agentic-systems/reviews/example-system.md").unlink()
    shutil.rmtree(root / agentic_set.retained_overview_path(RUN_ID).parent)
    shutil.rmtree(root / "kb/reports/state")
    shutil.rmtree(root / "kb/agent-memory-systems")
    shutil.rmtree(root / "related-systems")
    return root


def test_bundle_and_query_use_one_population_without_live_or_legacy_inputs(
    landscape_source, tmp_path
):
    output = tmp_path / "bundle"
    report = bundle.prepare(landscape_source, output)
    assert report["rows"] == 4
    assert report["source_tiers"] == {"code-grounded": 3, "doc-grounded": 1}
    assert not (output / "kb/agent-memory-systems").exists()
    assert not (output / "kb/reports/state").exists()
    assert not (
        landscape_source / "kb/agentic-systems/comparisons/memory-systems.csv"
    ).exists()
    shutil.rmtree(landscape_source)
    assert bundle.verify(output, report["manifest_sha256"]) == report
    rows = list(csv.DictReader(io.StringIO((output / bundle.MATRIX).read_text())))
    eligible = [
        r
        for r in rows
        if r["source_tier"] == "code-grounded"
        and r["storage_substrate_assessment"] == "known"
        and all(e["basis"] in {"wired", "observed", "causally supported"} for e in json.loads(r["storage_substrate_evidence"]).values())
    ]
    matched = [r for r in eligible if "files" in json.loads(r["storage_substrate"])]
    assert len(eligible) == len(matched) == 1
    assert matched[0]["system_name"] == "wired-fixture"
    assert len(json.loads(matched[0]["storage_substrate"])) == 2
    text = (output / matched[0]["overview_file"]).with_name("memory.md").read_text()
    assert "The store OBJ-2 keeps session notes" in text
    assert "not an observed run" in text


def test_linked_ontology_must_be_captured_before_a_bundle_is_published(landscape_source, tmp_path):
    root = landscape_source
    ontology = write(root / "kb/notes/reliability-ontology.md", "# Ontology witness\n")
    review = root / "kb/agentic-systems/reviews/wired-fixture.md"
    runtime = (root / frontmatter(review)["analysis-overview"]).with_name("runtime.md")
    runtime.write_text(runtime.read_text() + "\n[Ontology witness](../../../../notes/reliability-ontology.md)\n")
    repin_set(root, review)
    output = tmp_path / "bundle"
    with pytest.raises(ValueError, match="missing target.*reliability-ontology"):
        bundle.prepare(root, output)
    assert not output.exists()
    accepted = bundle.prepare(root, output, ontology=[ontology])
    assert bundle.verify(output, accepted["manifest_sha256"], source_root=root) == accepted


@pytest.mark.parametrize("changed", ["overview", "member", "matrix", "manifest", "extra"])
def test_verify_rejects_drift_from_the_pinned_bundle(
    landscape_source, tmp_path, changed
):
    output = tmp_path / "bundle"
    report = bundle.prepare(landscape_source, output)
    if changed in {"overview", "member"}:
        review = output / report["reviews"][0]
        path = output / frontmatter(review)["analysis-overview"]
        if changed == "member":
            path = path.with_name("epistemic.md")
    else:
        path = (
            output
            / {
                "matrix": bundle.MATRIX,
                "manifest": bundle.MANIFEST,
                "extra": "unexpected.md",
            }[changed]
        )
    with path.open("ab") as handle:
        handle.write(b"changed\n")
    with pytest.raises(ValueError, match="manifest"):
        bundle.verify(output, report["manifest_sha256"])


def test_valid_manifest_cannot_hide_matrix_result_disagreement(
    landscape_source, tmp_path
):
    output = tmp_path / "bundle"
    bundle.prepare(landscape_source, output)
    (output / bundle.MATRIX).write_text("system_name\nlegacy-only\n")
    manifest = bundle.manifest(bundle.payload(output))
    (output / bundle.MANIFEST).write_bytes(manifest)
    with pytest.raises(ValueError, match="matrix differs from bundled analysis sets"):
        bundle.verify(output, bundle.digest(manifest))


def test_current_check_detects_population_growth_but_explicit_selection_is_stable(
    landscape_source, tmp_path
):
    all_output = tmp_path / "all"
    explicit_output = tmp_path / "explicit"
    report_all = bundle.prepare(landscape_source, all_output)
    report_explicit = bundle.prepare(
        landscape_source,
        explicit_output,
        [Path("kb/agentic-systems/reviews/wired-fixture.md")],
    )
    copy_member(landscape_source, "doc-fixture", "extra-fixture")
    with pytest.raises(ValueError, match="selected population changed"):
        bundle.verify(
            all_output, report_all["manifest_sha256"], source_root=landscape_source
        )
    bundle.verify(
        explicit_output,
        report_explicit["manifest_sha256"],
        source_root=landscape_source,
    )


def test_current_check_detects_source_and_ontology_changes(landscape_source, tmp_path):
    ontology = write(landscape_source / "kb/notes/example.md", "# Example ontology\n")
    output = tmp_path / "bundle"
    report = bundle.prepare(landscape_source, output, ontology=[ontology])
    ontology.write_text("# Revised ontology\n")
    with pytest.raises(ValueError, match="source input changed"):
        bundle.verify(output, report["manifest_sha256"], source_root=landscape_source)
    bundle.verify(output, report["manifest_sha256"])


def test_missing_evidence_leaves_no_bundle_and_existing_bundle_is_preserved(
    landscape_source, tmp_path
):
    output = tmp_path / "bundle"
    report = bundle.prepare(landscape_source, output)
    with pytest.raises(ValueError, match="already exists"):
        bundle.prepare(landscape_source, output)
    assert bundle.verify(output, report["manifest_sha256"]) == report
    review = landscape_source / report["reviews"][0]
    (landscape_source / frontmatter(review)["analysis-overview"]).unlink()
    with pytest.raises(OSError):
        bundle.prepare(landscape_source, tmp_path / "missing")
    assert not (tmp_path / "missing").exists()


def test_additional_inputs_cannot_smuggle_in_legacy_or_transfer_evidence(
    landscape_source, tmp_path
):
    transfer = write(
        landscape_source / "kb/reports/state/agentic-system-transfer/example.md",
        "# Local advice\n",
    )
    with pytest.raises(ValueError, match="additional ontology"):
        bundle.prepare(landscape_source, tmp_path / "bundle", ontology=[transfer])


def test_cli_requires_the_recorded_hash_and_reports_rejection(
    landscape_source, tmp_path, capsys
):
    output = tmp_path / "bundle"
    assert (
        bundle.main(
            ["prepare", "--source-root", str(landscape_source), "--output", str(output)]
        )
        == 0
    )
    report = json.loads(capsys.readouterr().out)
    assert (
        bundle.main(["verify", str(output), "--sha256", report["manifest_sha256"]]) == 0
    )
    assert bundle.main(["verify", str(output), "--sha256", "0" * 64]) == 1
    assert "manifest SHA-256 mismatch" in capsys.readouterr().err
