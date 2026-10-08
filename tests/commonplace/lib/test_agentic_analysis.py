"""Retained analysis sets, member validation and comparison readers (no runtime)."""
from __future__ import annotations

import json
import shutil
import subprocess
from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from commonplace.lib import systems_matrix, validation
from commonplace.lib.agentic_analysis import sets as agentic_set
from commonplace.lib.agentic_analysis.records import amendment_index

pytestmark = pytest.mark.usefixtures("tmp_library")


REPO_ROOT = Path(__file__).resolve().parents[3]


RUN_ID = "AAS-2026-09-04-example-system-01"


RETAINED_OVERVIEW = agentic_set.RETAINED_ROOT / "example-system" / "overview.md"


SOURCE = "https://example.invalid/example-system"


STATE_DIR = Path("kb/agentic-system-analyses/state")


INPUTS_COMMIT = "f" * 40


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def configure_types(tmp_path: Path) -> None:
    for name in (
        "agentic-analysis-boundary.md",
        "agentic-analysis-sources.md",
        "agentic-analysis-records.md",
    ):
        target = tmp_path / "kb/agentic-system-analyses/instructions" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO_ROOT / "kb/agentic-system-analyses/instructions" / name, target)
    shutil.copytree(REPO_ROOT / "kb/types", tmp_path / "kb/types")
    shutil.copytree(
        REPO_ROOT / "kb/agent-memory-systems/types",
        tmp_path / "kb/agent-memory-systems/types",
    )
    shutil.copytree(
        REPO_ROOT / "kb/agentic-system-analyses/types",
        tmp_path / "kb/agentic-system-analyses/types",
    )
    for collection in ("kb/reports", "kb/agentic-systems", "kb/agentic-system-analyses"):
        (tmp_path / collection).mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO_ROOT / collection / "COLLECTION.md", tmp_path / collection / "COLLECTION.md")
    shutil.copytree(
        REPO_ROOT / "kb/instructions/review-gates",
        tmp_path / "kb/instructions/review-gates",
    )


def git_checkout(path: Path) -> tuple[Path, str]:
    path.mkdir(parents=True)
    subprocess.run(["git", "init", "--quiet", str(path)], check=True)
    write(path / "README.md", "# Frozen source\n")
    subprocess.run(["git", "-C", str(path), "add", "README.md"], check=True)
    subprocess.run(
        [
            "git",
            "-C",
            str(path),
            "-c",
            "user.name=Commonplace Test",
            "-c",
            "user.email=test@example.invalid",
            "commit",
            "--quiet",
            "-m",
            "Create source fixture",
        ],
        check=True,
    )
    revision = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()
    return path, revision


def frontmatter(path: Path) -> dict[str, object]:
    content = path.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None and document.frontmatter is not None
    return document.frontmatter


def replace_frontmatter(path: Path, values: dict[str, object]) -> None:
    content = path.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None
    path.write_text(
        "---\n"
        + yaml.safe_dump(values, sort_keys=False)
        + "---\n"
        + document.body,
        encoding="utf-8",
    )


def uninspected_profile(scope: str) -> dict:
    return {
        "scope": scope,
        "axes": {
            axis: {"assessment": "uninspected", "evidence": {}, "values": [],
                   "records": [], "note": "Not inspected in this fixture."}
            for axis in systems_matrix.AXES
        },
    }


def profile_report_fixture(run_dir: Path, revision: str, *, version: int = 1) -> Path:
    """Keep historical-reader fixtures v1; scheduled workflow fixtures use v2."""
    profile = uninspected_profile("The fixture's accumulated project memory and retrieval routes")
    profile["axes"]["storage_substrate"] = {
        "assessment": "known", "values": ["sqlite", "files"],
        "evidence": {v: {"basis": "wired", "records": ["MEM-OBJ-store"], "note": "Fixture witness."}
                     for v in ["sqlite", "files"]},
        "records": ["MEM-OBJ-store"], "note": "Both stores occur within the fixture boundary.",
    }
    if version == 2:
        profile = {
            "version": 2, "scope": profile["scope"],
            "axes": {
                axis: {"assessment": "uninspected", "units": [], "records": [],
                       "note": "Not inspected in this fixture."}
                for axis in systems_matrix.AXES
            },
        }
        profile["axes"]["storage_substrate"] = {
            "assessment": "known",
            "units": [{
                "scope": "The fixture's two inspected stores",
                "assessment": "known",
                "findings": [
                    {"value": value, "basis": "wired", "records": ["MEM-OBJ-store"],
                     "note": "Fixture witness."}
                    for value in ["sqlite", "files"]
                ],
                "records": ["MEM-OBJ-store"],
                "note": "Both stores occur within the fixture boundary.",
            }],
            "records": ["MEM-OBJ-store"],
            "note": "Both stores cover the fixture inventory.",
        }
    else:
        assert version == 1
    values = {
        "type": "agentic-system-analyses/types/agent-memory-profile.md",
        "description": "Comparison of the fixture memory boundary from verified source records",
        "run-id": RUN_ID, "source-identity": SOURCE,
        "reviewed-boundary": revision, "memory-comparison": profile,
    }
    return write(run_dir / "set/memory-profile.md", "---\n" + yaml.safe_dump(values, sort_keys=False) + "---\n\n# Fixture memory profile\n\n## Comparison rationale\n\nBoth stores are MEM-OBJ-store.\n")


def memory_report_fixture(run_dir: Path, revision: str) -> Path:
    """The specialist's report, which is the memory member unchanged: one
    `MEM-` record, one annotated seed, one quote."""
    values = {
        "type": "agentic-system-analyses/types/agent-memory-analysis-report.md",
        "description": "Fixture specialist report bound to the frozen source and shared input",
        "run-id": RUN_ID,
        "source-identity": SOURCE,
        "reviewed-boundary": revision,
    }
    body = f"""# Fixture memory analysis

## Boundary and evidence

Fixture evidence at `README.md`.

## Core ideas

Fixture finding.

> # Frozen source
> --- `README.md` @ `{revision}`

## Shared records

### Components

none proposed.

### Operative objects

#### MEM-OBJ-store — Fixture memory store

Store the specialist established, from SRC-1.

### Routes

#### On RT-RTE-model-call — Fixture route

Seeded route with the specialist's memory fields.

### Claims

none proposed.

### Evidenced absences

none proposed.

### Behavioral-authority paths

none proposed.

## Write side

Fixture evidence on MEM-OBJ-store.

## Read-back

Fixture evidence on RT-RTE-model-call.

## Integration issues

none

## Limitations and checks

Fixture evidence.
"""
    return write(
        run_dir / "set/memory.md",
        "---\n" + yaml.safe_dump(values, sort_keys=False) + "---\n\n" + body,
    )


def runtime_text(revision: str) -> str:
    return f"""---
type: agentic-system-analyses/types/agentic-system-runtime-report.md
description: "Runtime baseline of Example System at the fixture boundary"
run-id: {RUN_ID}
reviewed-boundary: {revision}
---

# Example System runtime report

## Runtime account

Implementation inspected at `README.md`; operation is unobserved.

## Shared records

### Components

#### RT-CMP-model — Fixture component

Record. Evidence: SRC-1.

### Operative objects

#### RT-OBJ-store — Fixture object

Record. Evidence: SRC-1.

### Routes

#### RT-RTE-model-call — Fixture route

- implementation conclusion status: wired

- Immediate return: The fixture invocation returns the stored object.
- Later read-back: A later invocation reads RT-OBJ-store.
- Delegated visibility: inapplicable — the fixture has no delegated workers.
- Selection predicate: The caller requests the fixture object.
- Invalidation or expiry: inapplicable — the fixture has no expiry mechanism.
- Activation or effect: uninspected — no behavioral execution was observed.
- Evidence limits: Static fixture evidence at SRC-1; operation was not exercised.

Record. Evidence: SRC-1.

### Claims

#### RT-CLM-runtime-claim — Fixture claim

Record. Evidence: SRC-1.

### Evidenced absences

none found within the fixture boundary.

### Behavioral-authority paths

#### RT-BAP-content-authority — Fixture authority path

Record. Evidence: SRC-1.

## Annotations

none
"""


def epistemic_text(revision: str) -> str:
    return f"""---
type: agentic-system-analyses/types/agentic-system-epistemic-report.md
description: "Epistemic routes of Example System at the fixture boundary"
run-id: {RUN_ID}
reviewed-boundary: {revision}
---

# Example System epistemic report

## Source-and-claim boundary

Boundary from the overview's Source register.

## Epistemic-object inventory

RT-OBJ-store and EPI-OBJ-store carry no candidate truth-apt content.

## Authority-route ledger

Route ID: RT-RTE-model-call
Route function: operational admission/selection/consumption
Architectural status: implemented
Content/update relation: no content change.

## System-claim versus route comparison

RT-CLM-runtime-claim is compared with RT-RTE-model-call.

## Bounded conclusion

Conclusion.

## Shared records

### Operative objects

#### EPI-OBJ-store — Fixture checked object

Object the epistemic lens established. Evidence: SRC-1.
"""


SET_NAMES = tuple(role.path for role in agentic_set.analysis_layout().roles.values())


def boundary_text(revision: str, *, source: str = SOURCE, path: str = "/fixture/example-system") -> str:
    return f"""---
type: agentic-system-analyses/types/agentic-system-boundary.md
description: "Example System at the frozen fixture boundary, analysed as an enclosing runtime"
run-id: {RUN_ID}
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: {revision}
analysis-cutoff: "2026-09-04"
evidence-tier: code-grounded
source:
  kind: git
  identity: {source}
  revision: {revision}
  path: {path}
  sha256: null
---

# Example System boundary

## Boundary and evidence

Fixture boundary at `{revision}`.

## Source register

| SRC-1 | git | `{source}` | `{revision}` | implementation | README.md | `README.md` | none |
"""


def overview_text(
    revision: str, members: dict[str, Path], *, inputs_commit: str = INPUTS_COMMIT
) -> str:
    return f"""---
type: agentic-system-analyses/types/agentic-system-analysis-overview.md
description: "Complete fixture analysis at one frozen source boundary"
run-id: {RUN_ID}
system: "Example System"
run-date: "2026-09-04"
result-disposition: complete
target-class: enclosing runtime
boundary-kind: whole-system
reviewed-boundary: {revision}
analysis-cutoff: "2026-09-04"
evidence-tier: code-grounded
inputs-commit: {inputs_commit}
---

# Example System agentic-system analysis

## Members

{chr(10).join(f'- [{name}]({name})' for name in SET_NAMES if name != 'overview.md')}

## Amendment index

{amendment_index(members['reconciliation.md'].read_text())}

## Deterministic validation

Passed.
"""


def run_dir_of(tmp_path: Path, run_id: str = RUN_ID) -> Path:
    return tmp_path / STATE_DIR / run_id


def output_path(run_dir: Path, name: str) -> Path:
    if name in (*SET_NAMES, "ARTIFACT.yaml"):
        return run_dir / "set" / name
    return run_dir / name


def repin(directory: Path) -> None:
    manifest = {"type": agentic_set.SET_TYPE, "members": {
        path.name: {"sha256": digest(path)} for path in sorted(directory.glob("*.md"))
    }}
    write(directory / "ARTIFACT.yaml", yaml.safe_dump(manifest, sort_keys=False))


def retain_set(tmp_path: Path, run_dir: Path, run_id: str = RUN_ID) -> None:
    directory = RETAINED_OVERVIEW.parent
    for name in ("ARTIFACT.yaml", *SET_NAMES):
        retained = directory / name
        (tmp_path / retained).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / retained).write_bytes((output_path(run_dir, name)).read_bytes())


def write_set(run_dir: Path, revision: str, *, source_path: Path | None = None) -> Path:
    """Write the members and the overview pinning them."""
    write(run_dir / "set/boundary.md", boundary_text(
        revision, **({"path": source_path.as_posix()} if source_path else {})))
    members = {
        "runtime.md": write(run_dir / "set/runtime.md", runtime_text(revision)),
        "memory.md": memory_report_fixture(run_dir, revision),
        "memory-profile.md": profile_report_fixture(run_dir, revision),
        "epistemic.md": write(run_dir / "set/epistemic.md", epistemic_text(revision)),
        "reconciliation.md": write(run_dir / "set/reconciliation.md", reconciliation_text(revision)),
    }
    write(run_dir / "set/synthesis.md", f'''---
type: agentic-system-analyses/types/agentic-system-synthesis.md
description: "Fixture synthesis retains supported object and route conclusions at the frozen boundary"
run-id: {RUN_ID}
reviewed-boundary: {revision}
---

# Example System synthesis

## Bounded synthesis

Fixture synthesis over RT-OBJ-store, MEM-OBJ-store, EPI-OBJ-store and RT-RTE-model-call.

## Limitations

None.
''')
    for stage, name in (("records", "record-verification.md"),
                        ("profile", "profile-verification.md"),
                        ("synthesis", "synthesis-verification.md")):
        write(run_dir / "set" / name, f'''---
type: agentic-system-analyses/types/agentic-system-verification.md
description: "Independent fixture verification of the accepted {stage} at the frozen boundary"
run-id: {RUN_ID}
reviewed-boundary: {revision}
verifies: {stage}
---

# Example System {stage} verification

## Verification

Passed.

## Blockers

none

## Limits

none
''')
    overview = write(run_dir / "set/overview.md", overview_text(revision, members))
    repin(run_dir / "set")
    return overview


def reconciliation_text(revision: str) -> str:
    return f'''---
type: agentic-system-analyses/types/agentic-system-reconciliation-report.md
description: "Reconciled Example System records at the frozen source boundary"
run-id: {RUN_ID}
reviewed-boundary: {revision}
---

# Example System reconciliation

## Reconciliation

MEM-OBJ-store and EPI-OBJ-store duplicate no runtime record.
'''


def member_fixture(tmp_path: Path) -> Path:
    """A run directory's set without source checkout or run state, for checks of one document."""
    configure_types(tmp_path)
    run_dir = run_dir_of(tmp_path)
    write_set(run_dir, "a" * 40)
    return run_dir


def test_overview_amendment_index_cannot_hide_an_amendment(tmp_path: Path) -> None:
    run = member_fixture(tmp_path)
    reconciliation = run / "set/reconciliation.md"
    reconciliation.write_text(reconciliation.read_text() +
        "\nAmendment: EPI-OBJ-store is superseded by RT-OBJ-store; identity evidence at SRC-1.\n")
    repin(reconciliation.parent)
    failures = validation.validate_note(reconciliation.parent, repo_root=tmp_path).fails
    assert any("amendment index does not match" in failure for failure in failures)


def run_git(root: Path, *args: str) -> str:
    return subprocess.run(
        [
            "git", "-C", str(root),
            "-c", "user.name=Commonplace Test",
            "-c", "user.email=test@example.invalid",
            *args,
        ],
        check=True, capture_output=True, text=True,
    ).stdout.strip()


def commit_paths(root: Path, message: str, *paths: Path | str) -> str:
    """Stage the given paths, commit them, and return the new HEAD."""
    run_git(root, "add", "--", *(str(path) for path in paths))
    run_git(root, "commit", "--quiet", "-m", message)
    return run_git(root, "rev-parse", "HEAD")


def test_manifest_hash_must_be_a_digest(tmp_path):
    directory = member_fixture(tmp_path) / "set"
    manifest = directory / "ARTIFACT.yaml"
    values = yaml.safe_load(manifest.read_text())
    values["members"]["runtime.md"]["sha256"] = "bad"
    manifest.write_text(yaml.safe_dump(values))
    with pytest.raises(ValueError, match="malformed SHA-256"):
        agentic_set.load_member_set(directory, run=validation.ValidationRun(tmp_path, ()))


@pytest.mark.parametrize("mutation", ["valid", "outside"])
def test_profile_resolves_canonical_record_declarations(tmp_path: Path, mutation: str) -> None:
    directory = member_fixture(tmp_path) / "set"
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
    ("[memory report](../memory-report-0.md)", "set member link: ../memory-report-0.md leaves the set directory"),
    ("[runtime member](runtime.md)", None),
])
def test_set_member_links_stay_inside_the_set_directory(tmp_path: Path, link: str, error: str | None) -> None:
    """A link out of set/ resolves in the run directory but breaks once retained."""
    overview = member_fixture(tmp_path) / "set/overview.md"
    overview.write_text(overview.read_text() + f"\nRead {link}.\n")
    fails = validation.validate_note(overview, repo_root=tmp_path).fails
    if error is None:
        assert fails == []
    else:
        assert any(error in failure for failure in fails), fails


def test_validate_cli_checks_a_complete_set_at_the_skill_path(tmp_path: Path, capsys, monkeypatch) -> None:
    """The skill's step 7 command resolves and validates the set from the repository root."""
    from commonplace.cli.validate_notes import main

    member_fixture(tmp_path)
    monkeypatch.chdir(tmp_path)
    target = f"kb/agentic-system-analyses/state/{RUN_ID}/set"

    assert main([target, "--json"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert [artifact["path"] for artifact in report["analysed_artifacts"]] == [target]
    assert report["analysed_artifacts"][0]["type"] == agentic_set.SET_TYPE
    assert main([target, "--full"]) == 0


def test_comparison_population_must_select_one_review_per_source(tmp_path):
    retained_fixture(tmp_path)
    current = tmp_path / RETAINED_OVERVIEW.parent
    shutil.copytree(current, current.with_name("twin"))
    with pytest.raises(ValueError, match="multiple current analyses"):
        systems_matrix.load_results(tmp_path)


def test_member_validation_rejects_ranged_prose_anchors(tmp_path: Path) -> None:
    runtime = member_fixture(tmp_path) / "set/runtime.md"
    runtime.write_text(runtime.read_text() + "\nEvidence: `src/agent.py:120-140`.\n")
    checked = validation.validate_note(runtime, repo_root=tmp_path)
    assert any(
        "carries a line range" in item and "cite the path without a range, or quote the passage" in item
        for item in checked.fails
    )


def test_real_retained_set_keeps_links_and_hashes_when_archived(tmp_path):
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


def test_a_candidate_receives_only_its_own_roles_set_findings(tmp_path: Path) -> None:
    run_dir = member_fixture(tmp_path)
    output = run_dir / "set"
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
    output = run_dir / "set"
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


def test_profile_rejects_missing_identity_source_without_requiring_whole_set(tmp_path: Path) -> None:
    run_dir = member_fixture(tmp_path)
    output = run_dir / "set"
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
    runtime = run_dir / "set/runtime.md"
    assert not validation.validate_note(runtime, repo_root=tmp_path).fails
    runtime.write_text(runtime.read_text().replace("#### RT-OBJ-store —", "#### MEM-OBJ-store —", 1))
    failures = validation.validate_note(runtime, repo_root=tmp_path).fails
    assert any("this report declares only RT- records: MEM-OBJ-store" in failure for failure in failures)


def test_quotations_without_their_frozen_source_are_unverified_not_failed(tmp_path: Path) -> None:
    run_dir = member_fixture(tmp_path)  # its boundary pins a checkout that is not here
    output = run_dir / "set"

    checked = validation.validate_note(output, repo_root=tmp_path)

    assert checked.fails == []
    assert any("memory.md:" in info and "quotations unverified, source unavailable" in info
               for info in checked.infos)
    findings = validation.validate_draft_at_slot(output, "memory.md", output / "memory.md", repo_root=tmp_path)
    assert any(finding.info and "quotations unverified" in finding.message for finding in findings)
    assert not [finding for finding in findings if not finding.info and not finding.warn]



def retained_fixture(tmp_path: Path) -> Path:
    """A source-backed retained set, constructed without running or publishing."""
    configure_types(tmp_path)
    source, revision = git_checkout(tmp_path / "related-systems/example--system")
    run_dir = run_dir_of(tmp_path)
    write_set(run_dir, revision, source_path=source)
    retain_set(tmp_path, run_dir)
    return tmp_path / RETAINED_OVERVIEW.parent


@pytest.mark.parametrize("mutation, diagnostic", [
    ("drift", "manifest member runtime.md: SHA-256 mismatch"),
    ("invalid", "member runtime.md"),
    ("identity", "identity field source-identity"),
])
def test_retained_set_rejects_member_defects(tmp_path, mutation, diagnostic):
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
def test_set_validator_rejects_bad_evidence_without_writes(tmp_path, addition, diagnostic):
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
def test_set_quote_anchors_resolve_from_recorded_commit(tmp_path, citation_kind):
    directory = retained_fixture(tmp_path)
    boundary = directory / "boundary.md"
    metadata = frontmatter(boundary)
    source = metadata["source"]
    revision = source["revision"]
    if citation_kind == "github":
        identity = "https://github.com/example/system"
        # Identity is a set relation, not a run-state property.
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
    source = validation._FrozenGitObjects({
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
    source = validation._FrozenGitObjects({
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


def test_changed_checkout_leaves_set_quotations_unverified(tmp_path):
    directory = retained_fixture(tmp_path)
    source = frontmatter(directory / "boundary.md")["source"]
    write(Path(source["path"]) / "README.md", "# Changed worktree\n")
    checked = validation.validate_note(directory, repo_root=tmp_path)
    assert any("quotations unverified" in item and "has local changes" in item
               for item in checked.infos)


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope"])
def test_noncomplete_set_validates_but_cannot_supply_comparison(tmp_path, disposition):
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
    for name in SET_NAMES:
        if name not in {"boundary.md", "overview.md"}:
            (directory / name).unlink()
    repin(directory)
    assert validation.validate_note(directory, repo_root=tmp_path).fails == []
    shutil.copytree(directory, retained)
    with pytest.raises(ValueError, match="must be complete"):
        systems_matrix.load_results(tmp_path)
