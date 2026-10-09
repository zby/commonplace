"""Retained analysis artifacts, member validation and comparison readers (no runtime)."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

import pytest
import yaml

from commonplace.lib import quote_grounding, systems_matrix, validation
from commonplace.lib.agentic_analysis import analyses
from tests.commonplace.agentic_analysis.fixtures import (
    MEMBER_NAMES,
    REPO_ROOT,
    RETAINED_OVERVIEW,
    RUN_ID,
    SOURCE,
    commit_paths,
    digest,
    frontmatter,
    git_checkout,
    member_fixture,
    repin,
    replace_frontmatter,
    retained_fixture,
    write,
)

pytestmark = pytest.mark.usefixtures("tmp_library")


def test_overview_amendment_index_cannot_hide_an_amendment(tmp_path: Path) -> None:
    run = member_fixture(tmp_path)
    reconciliation = run / "artifact/reconciliation.md"
    reconciliation.write_text(reconciliation.read_text() +
        "\nAmendment: EPI-OBJ-store is superseded by RT-OBJ-store; identity evidence at SRC-1.\n")
    repin(reconciliation.parent)
    failures = validation.validate_note(reconciliation.parent, repo_root=tmp_path).fails
    assert any("amendment index does not match" in failure for failure in failures)


def test_manifest_hash_must_be_a_digest(tmp_path):
    directory = member_fixture(tmp_path) / "artifact"
    manifest = directory / "ARTIFACT.yaml"
    values = yaml.safe_load(manifest.read_text())
    values["members"]["runtime.md"]["sha256"] = "bad"
    manifest.write_text(yaml.safe_dump(values))
    with pytest.raises(ValueError, match="malformed SHA-256"):
        analyses.load_analysis(directory, run=validation.ValidationRun(tmp_path, ()))


@pytest.mark.parametrize("mutation", ["valid", "outside"])
def test_profile_resolves_canonical_record_declarations(tmp_path: Path, mutation: str) -> None:
    directory = member_fixture(tmp_path) / "artifact"
    memory = directory / "memory.md"
    report = directory / "memory-profile.md"
    body = memory.read_text().replace(
        "### Evidenced absences\n\nnone proposed.\n",
        "### Evidenced absences\n\n#### MEM-ABS-missing-route — Inspected absence\n\nSearched.\n",
    )
    memory.write_text(body)
    metadata = frontmatter(report)
    axes = metadata["memory-comparison"]["axes"]
    axes["storage_substrate"] = {
        "assessment": "known", "values": ["files"],
        "evidence": {"files": {"basis": "wired", "records": ["MEM-OBJ-store"], "note": "Fixture witness."}},
        "records": ["MEM-OBJ-store"], "note": "Fixture source writes files.",
    }
    axes["trace_learning"] = {
        "assessment": "absent", "evidence": {}, "values": [],
        "records": ["MEM-ABS-missing-route"], "note": "Fixture source was inspected.",
    }
    expected_error = None
    if mutation == "outside":
        memory.write_text(memory.read_text().replace(
            "#### MEM-OBJ-store — Fixture memory store\n", "",
        ) + "\nMEM-OBJ-store outside the register.\n")
        expected_error = "unresolved record"
    replace_frontmatter(report, metadata)
    repin(directory)
    checked = validation.validate_note(directory, repo_root=tmp_path)
    if expected_error:
        assert any(expected_error in error for error in checked.fails)
    else:
        assert checked.fails == []
        assert any("members, roles and relations satisfied" in message for message in checked.passes)


def test_comparison_tools_use_retained_results_without_local_or_legacy_inputs(tmp_path, monkeypatch):
    import csv
    import io

    from scripts import build_systems_matrix, render_systems_table

    retained_fixture(tmp_path)
    retained = tmp_path / RETAINED_OVERVIEW
    shutil.rmtree(tmp_path / "kb/agentic-system-analyses/state")
    shutil.rmtree(tmp_path / "kb/agent-memory-systems")
    shutil.rmtree(tmp_path / "related-systems")
    write(tmp_path / "kb/agentic-systems/reviews/README.md", "# Ordinary navigation\n")
    inputs = systems_matrix.load_results(tmp_path)
    assert len(inputs.rows) == 1
    assert inputs.rows[0]["storage_substrate"] == ["files", "sqlite"]
    assert inputs.rows[0]["lineage_assessment"] == "uninspected"
    assert inputs.rows[0]["artifact_sha256"] == digest(retained.with_name("ARTIFACT.yaml"))
    for module in (build_systems_matrix, render_systems_table):
        monkeypatch.setattr(module, "REPO_ROOT", tmp_path)
    matrix = tmp_path / "kb/agentic-systems/comparisons/memory-systems.csv"
    table = matrix.with_suffix(".md")
    assert build_systems_matrix.main(["--output", str(matrix)]) == 0
    assert list(csv.DictReader(io.StringIO(matrix.read_text()))) == [
        systems_matrix.csv_row(row) for row in inputs.rows
    ]
    assert '"[""files"",""sqlite""]"' in matrix.read_text()
    assert render_systems_table.main(["--output", str(table)]) == 0
    assert "files [wired], sqlite [wired]" in table.read_text()
    assert "## code-grounded (1)" in table.read_text()
    assert digest(retained.with_name("ARTIFACT.yaml")) in table.read_text()
    assert validation.validate_note(table, repo_root=tmp_path).fails == []


@pytest.mark.parametrize("mutation, error", [
    ("bytes", "SHA-256 mismatch"), ("profile", "memory-comparison"),
    ("source", "directory name does not match"), ("revision", "reviewed-boundary"),
    ("missing", "no discovered file"), ("member", "manifest member memory.md: SHA-256 mismatch"),
])
def test_comparison_reader_rejects_incomplete_or_mismatched_evidence(tmp_path, mutation, error):
    retained_fixture(tmp_path)
    retained = tmp_path / RETAINED_OVERVIEW
    memory = retained.with_name("memory.md")

    def repin_overview() -> None:
        repin(retained.parent)


    if mutation == "bytes":
        retained.write_bytes(retained.read_bytes() + b"drift\n")
    elif mutation == "missing":
        retained.unlink()
    elif mutation == "member":
        memory.write_bytes(memory.read_bytes() + b"drift\n")
    elif mutation == "profile":
        data = frontmatter(memory.with_name("memory-profile.md"))
        data.pop("memory-comparison")
        replace_frontmatter(memory.with_name("memory-profile.md"), data)
        repin_overview()
    else:
        key = "source-identity" if mutation == "source" else "reviewed-boundary"
        value = "https://example.invalid/example-system-other" if mutation == "source" else "other"
        target = memory if mutation == "source" else retained
        replace_frontmatter(target, {**frontmatter(target), key: value})
        repin(retained.parent)
    with pytest.raises((ValueError, OSError), match=error):
        systems_matrix.load_results(tmp_path)


@pytest.mark.parametrize("link, error", [
    ("[memory report](../memory-report-0.md)", "artifact member link: ../memory-report-0.md leaves the artifact directory"),
    ("[runtime member](runtime.md)", None),
])
def test_artifact_member_links_stay_inside_the_artifact_directory(tmp_path: Path, link: str, error: str | None) -> None:
    """A link out of artifact/ resolves in the run directory but breaks once retained."""
    overview = member_fixture(tmp_path) / "artifact/overview.md"
    overview.write_text(overview.read_text() + f"\nRead {link}.\n")
    fails = validation.validate_note(overview, repo_root=tmp_path).fails
    if error is None:
        assert fails == []
    else:
        assert any(error in failure for failure in fails), fails


def test_validate_cli_checks_a_complete_artifact_at_the_skill_path(tmp_path: Path, capsys, monkeypatch) -> None:
    """The skill's step 7 command resolves and validates the artifact from the repository root."""
    from commonplace.cli.validate_notes import main

    member_fixture(tmp_path)
    monkeypatch.chdir(tmp_path)
    target = f"kb/agentic-system-analyses/state/{RUN_ID}/artifact"

    assert main([target, "--json"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert [artifact["path"] for artifact in report["analysed_artifacts"]] == [target]
    assert report["analysed_artifacts"][0]["type"] == analyses.ANALYSIS_TYPE
    assert main([target, "--full"]) == 0


def test_comparison_population_must_select_one_review_per_source(tmp_path):
    retained_fixture(tmp_path)
    current = tmp_path / RETAINED_OVERVIEW.parent
    shutil.copytree(current, current.with_name("twin"))
    with pytest.raises(ValueError, match="multiple current analyses"):
        systems_matrix.load_results(tmp_path)


def test_member_validation_rejects_ranged_prose_anchors(tmp_path: Path) -> None:
    runtime = member_fixture(tmp_path) / "artifact/runtime.md"
    runtime.write_text(runtime.read_text() + "\nEvidence: `src/agent.py:120-140`.\n")
    checked = validation.validate_note(runtime, repo_root=tmp_path)
    assert any(
        "carries a line range" in item and "cite the path without a range, or quote the passage" in item
        for item in checked.fails
    )


def test_real_retained_artifact_keeps_links_and_hashes_when_archived(tmp_path):
    from urllib.parse import urlsplit

    from commonplace.lib.note_parser import find_markdown_links
    real = REPO_ROOT / "kb/agentic-systems/reports/retained-archive/AAS-2026-10-03-dynamic-cheatsheet-02"
    current = tmp_path / "kb/agentic-system-analyses/retained/dynamic-cheatsheet"
    archive = tmp_path / "kb/agentic-system-analyses/retained-archive/AAS-2026-10-03-dynamic-cheatsheet-02"
    shutil.copytree(real, current)
    old = {p.name: digest(p) for p in current.iterdir()}
    archive.parent.mkdir(parents=True)
    current.rename(archive)
    assert {p.name: digest(p) for p in archive.iterdir()} == old
    manifest = yaml.safe_load((archive / "ARTIFACT.yaml").read_text())
    for name, entry in manifest["members"].items():
        assert digest(archive / name) == entry["sha256"]
    for member in archive.glob("*.md"):
        for link in find_markdown_links(member.read_text()):
            parts = urlsplit(link)
            if not parts.scheme and parts.path:
                assert (member.parent / parts.path).is_file(), (member, link)


def test_a_candidate_receives_only_its_own_roles_artifact_findings(tmp_path: Path) -> None:
    run_dir = member_fixture(tmp_path)
    output = run_dir / "artifact"
    epistemic = output / "epistemic.md"
    epistemic.write_text(epistemic.read_text() + "\nEPI-OBJ-dangling is cited here.\n")
    before = {path.name: path.read_bytes() for path in output.iterdir()}
    candidate = write(run_dir / "runtime-report-1.md",
                      (output / "runtime.md").read_text().replace(f"run-id: {RUN_ID}", "run-id: AAS-2026-09-04-other-01"))

    findings = validation.validate_draft_at_slot(output, "runtime.md", candidate, repo_root=tmp_path)

    assert all(finding.role == "runtime" for finding in findings)
    assert [finding.message for finding in findings if not finding.info and not finding.warn] == [(
        f"runtime.md: identity field run-id 'AAS-2026-09-04-other-01' does not match boundary.md; "
        f"expected '{RUN_ID}'"
    )]
    assert any("EPI-OBJ-dangling" in finding.message for finding in
               validation.validate_draft_at_slot(output, "epistemic.md", epistemic, repo_root=tmp_path))
    assert {path.name: path.read_bytes() for path in output.iterdir()} == before


def test_candidate_and_verification_reject_ambiguous_context_references(tmp_path: Path) -> None:
    run_dir = member_fixture(tmp_path)
    output = run_dir / "artifact"
    runtime = output / "runtime.md"
    runtime.write_text(runtime.read_text().replace(
        "## Annotations", "#### RT-OBJ-store — Duplicate object\n\n## Annotations",
    ))
    candidate = write(run_dir / "memory-candidate.md",
                      (output / "memory.md").read_text() + "\nSee RT-OBJ-store.\n")
    verification = write(run_dir / "verification.md",
                         (output / "record-verification.md").read_text() + "\nSee RT-OBJ-store.\n")
    before = {path.name: path.read_bytes() for path in output.iterdir()}

    findings = validation.validate_draft_at_slot(output, "memory.md", candidate, repo_root=tmp_path)
    assert any("memory.md: ambiguous record RT-OBJ-store" in finding.message for finding in findings)
    findings = validation.validate_draft_at_slot(output, "record-verification.md", verification, repo_root=tmp_path)
    assert any("record-verification.md: ambiguous record RT-OBJ-store" in finding.message for finding in findings)
    assert {path.name: path.read_bytes() for path in output.iterdir()} == before


def test_profile_rejects_missing_identity_source_without_requiring_whole_artifact(tmp_path: Path) -> None:
    run_dir = member_fixture(tmp_path)
    output = run_dir / "artifact"
    candidate = write(run_dir / "profile-candidate.md", (output / "memory-profile.md").read_text()
                      .replace("MEM-OBJ-store", "RT-OBJ-store")
                      .replace(SOURCE, "https://example.invalid/unrelated"))
    memory_content = (output / "memory.md").read_text()
    (output / "memory.md").unlink()
    findings = validation.validate_draft_at_slot(output, "memory-profile.md", candidate, repo_root=tmp_path)
    assert [finding.message for finding in findings if not finding.info and not finding.warn] == [(
        "memory-profile.md: cannot check identity fields source-identity; "
        "source member memory.md is absent"
    )]
    # Restore just the identity source. An unrelated absent member is not a
    # candidate failure when no applicable check needs it.
    write(output / "memory.md", memory_content.replace(SOURCE, "https://example.invalid/unrelated"))
    (output / "epistemic.md").unlink()
    findings = validation.validate_draft_at_slot(output, "memory-profile.md", candidate, repo_root=tmp_path)
    assert not [finding for finding in findings if not finding.info and not finding.warn]


def test_a_report_declares_only_its_types_record_prefix(tmp_path: Path) -> None:
    run_dir = member_fixture(tmp_path)
    runtime = run_dir / "artifact/runtime.md"
    assert not validation.validate_note(runtime, repo_root=tmp_path).fails
    runtime.write_text(runtime.read_text().replace("#### RT-OBJ-store —", "#### MEM-OBJ-store —", 1))
    failures = validation.validate_note(runtime, repo_root=tmp_path).fails
    assert any("this report declares only RT- records: MEM-OBJ-store" in failure for failure in failures)


def test_quotations_without_their_frozen_source_are_unverified_not_failed(tmp_path: Path) -> None:
    run_dir = member_fixture(tmp_path)  # its boundary pins a checkout that is not here
    output = run_dir / "artifact"

    checked = validation.validate_note(output, repo_root=tmp_path)

    assert checked.fails == []
    assert any("memory.md:" in info and "quotations unverified, source unavailable" in info
               for info in checked.infos)
    findings = validation.validate_draft_at_slot(output, "memory.md", output / "memory.md", repo_root=tmp_path)
    assert any(finding.info and "quotations unverified" in finding.message for finding in findings)
    assert not [finding for finding in findings if not finding.info and not finding.warn]


@pytest.mark.parametrize("mutation, diagnostic", [
    ("drift", "manifest member runtime.md: SHA-256 mismatch"),
    ("invalid", "member runtime.md"),
    ("identity", "identity field source-identity"),
])
def test_retained_artifact_rejects_member_defects(tmp_path, mutation, diagnostic):
    directory = retained_fixture(tmp_path)
    runtime = directory / "runtime.md"
    if mutation == "drift":
        runtime.write_text(runtime.read_text() + "changed\n")
    elif mutation == "invalid":
        runtime.write_text(runtime.read_text().replace("## Annotations", "## Renamed"))
        repin(directory)
    else:
        memory = directory / "memory.md"
        replace_frontmatter(memory, {**frontmatter(memory), "source-identity": "https://example.invalid/other"})
        repin(directory)
    checked = validation.validate_note(directory, repo_root=tmp_path)
    assert any(diagnostic in item for item in checked.fails), checked.fails


@pytest.mark.parametrize("addition, diagnostic", [
    ("\nBad range: `README.md:999`.\n", "cite the path without a range"),
    ("\n> absent source text\n> --- `README.md` @ `{revision}`\n", "quote does not occur"),
    ("\n> Frozen source\n> --- `README.md` @ `" + "0" * 40 + "`\n", "attribution uses revision"),
    ("\n> --- `README.md` @ `{revision}`\n", "quote body is empty"),
])
def test_artifact_validator_rejects_bad_evidence_without_writes(tmp_path, addition, diagnostic):
    directory = retained_fixture(tmp_path)
    memory = directory / "memory.md"
    revision = frontmatter(directory / "boundary.md")["source"]["revision"]
    memory.write_text(memory.read_text() + addition.format(revision=revision))
    repin(directory)
    before = {path.name: path.read_bytes() for path in directory.iterdir()}
    checked = validation.validate_note(directory, repo_root=tmp_path)
    assert any(diagnostic in item for item in checked.fails), checked.fails
    assert before == {path.name: path.read_bytes() for path in directory.iterdir()}


@pytest.mark.parametrize("citation_kind", ["local", "github"])
def test_artifact_quote_anchors_resolve_from_recorded_commit(tmp_path, citation_kind):
    directory = retained_fixture(tmp_path)
    boundary = directory / "boundary.md"
    metadata = frontmatter(boundary)
    source = metadata["source"]
    revision = source["revision"]
    if citation_kind == "github":
        identity = "https://github.com/example/system"
        # Identity is an artifact relation, not a run-state property.
        for name in ("boundary.md", "memory.md", "memory-profile.md"):
            member = directory / name
            member.write_text(member.read_text().replace(SOURCE, identity))
        attribution = f"[README.md]({identity}/blob/{revision}/README.md)"
    else:
        attribution = f"`README.md` @ `{revision}`"
    runtime = directory / "runtime.md"
    runtime.write_text(runtime.read_text() + f"\n> # Frozen\n> source\n> --- {attribution}\n")
    repin(directory)
    # The source identity change also changes the stable retained directory slug.
    if citation_kind == "github":
        directory = directory.rename(directory.with_name("system"))
    checked = validation.validate_note(directory, repo_root=tmp_path)
    assert checked.fails == []
    assert not any("unverified" in item for item in checked.infos)


@pytest.mark.parametrize("citation, diagnostic", [
    ("EXAMPLE/System/blob/{revision}/README.md", None),
    ("example/system/blob/{revision}/README.md", None),
    ("unrelated/other/blob/{revision}/README.md", "uses repository"),
    ("example/system/blob/main/README.md", "uses revision"),
    ("example/system/blob/{revision}/missing.md", "committed blob"),
])
def test_github_citations_match_frozen_source_objects(tmp_path, citation, diagnostic):
    from commonplace.lib.quote_matching import Citation, parse_github_blob

    root, revision = git_checkout(tmp_path / "source")
    url = "https://github.com/" + citation.format(revision=revision)
    blob = parse_github_blob(url)
    assert blob is not None
    anchor = Citation("", url, blob.revision)
    source = quote_grounding.FrozenGitObjects({
        "identity": "https://github.com/example/system", "revision": revision,
        "path": str(root),
    })
    error = source.attribution_error(anchor)
    if error is None:
        found = source.read(anchor, text=False)
        error = found.error or found.missing
    if diagnostic is None:
        assert error is None
    else:
        assert diagnostic in error


def test_path_only_anchor_to_binary_blob_resolves(tmp_path):
    from commonplace.lib.quote_matching import Citation

    root, _ = git_checkout(tmp_path / "source")
    (root / "paper.pdf").write_bytes(b"%PDF-1.4\n\xff\xfe\x00binary\n")
    revision = commit_paths(root, "Add binary paper", "paper.pdf")
    source = quote_grounding.FrozenGitObjects({
        "identity": "https://github.com/example/system", "revision": revision,
        "path": str(root),
    })
    found = source.read(Citation("", "paper.pdf", revision), text=False)
    assert found.error is None and found.missing is None
    missing = source.read(Citation("", "missing.pdf", revision), text=False)
    assert "does not name a committed blob" in missing.error


@pytest.mark.parametrize("changed", [False, True])
def test_capture_source_is_byte_verified(tmp_path, changed):
    from commonplace.lib.quote_grounding import frozen_source_pin, resolve_citations
    from commonplace.lib.quote_matching import parse_blockquotes

    capture = write(tmp_path / "source.bundle", "# Frozen source\ncaptured source\n")
    checksum = digest(capture)
    source = {
        "kind": "capture", "identity": "document bundle", "revision": "capture-2026-09-04",
        "path": str(capture), "sha256": checksum,
    }
    citation = f"> captured\n> source\n> --- `{capture}` @ `sha256:{checksum}`\n"
    if changed:
        capture.write_text("changed source\n")
    result, = resolve_citations(parse_blockquotes(citation), frozen_source_pin(source), kind="code")
    assert result.status == ("unverified" if changed else "match")
    if changed:
        assert "SHA-256 mismatch" in result.detail


def test_quoted_source_links_and_examples_validate_without_publication(tmp_path):
    directory = retained_fixture(tmp_path)
    boundary = directory / "boundary.md"
    source = frontmatter(boundary)["source"]
    root = Path(source["path"])
    foreign = "https://github.com/other/repo/blob/" + "b" * 40 + "/example.md#L1"
    source_text = (
        "# Frozen source\n"
        "![Diagram](figures/source.png)\n"
        f"[Upstream]({foreign})\n"
        "Use `fictional/file.py:12-20` as an example.\n"
        " * repeated comment\n * repeated comment\n"
    )
    write(root / "README.md", source_text)
    revision = commit_paths(root, "Add source examples", "README.md")
    for member in directory.glob("*.md"):
        member.write_text(member.read_text().replace(source["revision"], revision))
    runtime = directory / "runtime.md"
    for text in [*source_text.splitlines()[1:4], "* repeated comment"]:
        anchor = f"`README.md:6-6` @ `{revision}`" if text == "* repeated comment" else "`README.md`"
        runtime.write_text(runtime.read_text() + f"\n> {text}\n> --- {anchor}\n")
    repin(directory)
    checked = validation.validate_note(directory, repo_root=tmp_path)
    assert not checked.fails and not checked.warns
    assert not any("unverified" in item for item in checked.infos)


def test_changed_checkout_leaves_artifact_quotations_unverified(tmp_path):
    directory = retained_fixture(tmp_path)
    source = frontmatter(directory / "boundary.md")["source"]
    write(Path(source["path"]) / "README.md", "# Changed worktree\n")
    checked = validation.validate_note(directory, repo_root=tmp_path)
    assert any("quotations unverified" in item and "has local changes" in item
               for item in checked.infos)


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope"])
def test_noncomplete_artifact_validates_but_cannot_supply_comparison(tmp_path, disposition):
    retained = retained_fixture(tmp_path)
    directory = retained.rename(tmp_path / "draft-set")
    for name in ("overview.md", "boundary.md"):
        member = directory / name
        replace_frontmatter(member, {**frontmatter(member), "result-disposition": disposition})
    boundary = directory / "boundary.md"
    boundary.write_text(boundary.read_text() + "\n## Not reached\n\nFixture analysis was not reached.\n")
    overview = directory / "overview.md"
    overview.write_text("\n".join(
        line for line in overview.read_text().splitlines()
        if not line.startswith("- [") or line.startswith("- [boundary.md]")
    ) + "\n")
    for name in MEMBER_NAMES:
        if name not in {"boundary.md", "overview.md"}:
            (directory / name).unlink()
    repin(directory)
    assert validation.validate_note(directory, repo_root=tmp_path).fails == []
    shutil.copytree(directory, retained)
    with pytest.raises(ValueError, match="must be complete"):
        systems_matrix.load_results(tmp_path)
