from __future__ import annotations

import csv
import io
import json
import shutil
from pathlib import Path

import pytest

from commonplace.lib import systems_matrix
from scripts import bundle_agentic_landscape as bundle
from tests.commonplace.lib.test_agentic_analysis import (
    REPO_ROOT,
    RUN_ID,
    digest,
    frontmatter,
    replace_frontmatter,
    valid_run_state,
    write,
)


def copy_member(root: Path, original: str, name: str) -> Path:
    review = root / f"kb/agentic-systems/reviews/{original}.md"
    result = root / frontmatter(review)["analysis-result"]
    new_review = write(
        review.with_name(name + ".md"), review.read_text().replace(original, name)
    )
    new_result = write(
        root / frontmatter(new_review)["analysis-result"],
        result.read_text().replace(original, name),
    )
    replace_frontmatter(
        new_review,
        {**frontmatter(new_review), "analysis-result-sha256": digest(new_result)},
    )
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
        result = root / frontmatter(review)["analysis-result"]
        data = frontmatter(result)
        data["system"] = name
        data["evidence-tier"] = tier
        data["memory-comparison"]["axes"]["storage_substrate"].update(
            assessment="known" if basis else "uninspected",
            basis=basis,
            values=values,
            records=["OBJ-1"] if basis else [],
        )
        replace_frontmatter(result, data)
        if name == "wired-fixture":
            result.write_text(
                result.read_text().replace(
                    "OBJ-1 fixture object.",
                    "OBJ-1 stores session notes in Markdown files and rebuilds a SQLite lookup index from them. This is fixture wiring, not an observed run.",
                )
            )
        replace_frontmatter(
            review, {**frontmatter(review), "analysis-result-sha256": digest(result)}
        )
    (root / "kb/agentic-systems/reviews/example-system.md").unlink()
    (root / systems_matrix.retained_result_path(RUN_ID)).unlink()
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
        and r["storage_substrate_basis"] in {"wired", "observed", "causally supported"}
    ]
    matched = [r for r in eligible if "files" in json.loads(r["storage_substrate"])]
    assert len(eligible) == len(matched) == 1
    assert matched[0]["system_name"] == "wired-fixture"
    assert len(json.loads(matched[0]["storage_substrate"])) == 2
    text = (output / matched[0]["result_file"]).read_text()
    assert "OBJ-1 stores session notes" in text
    assert "not an observed run" in text


@pytest.mark.parametrize("changed", ["result", "matrix", "manifest", "extra"])
def test_verify_rejects_drift_from_the_pinned_bundle(
    landscape_source, tmp_path, changed
):
    output = tmp_path / "bundle"
    report = bundle.prepare(landscape_source, output)
    if changed == "result":
        review = output / report["reviews"][0]
        path = output / frontmatter(review)["analysis-result"]
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
    with pytest.raises(ValueError, match="matrix differs from bundled main results"):
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
    (landscape_source / frontmatter(review)["analysis-result"]).unlink()
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
