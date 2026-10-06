from __future__ import annotations

import json
import re
import shutil
import subprocess
import sys
from hashlib import sha256
from pathlib import Path

import pytest
import yaml

from commonplace.cli import (
    agentic_analysis_handoff,
    agentic_analysis_publication,
)
from commonplace.lib import agentic_publication, agentic_set, systems_matrix, validation
from commonplace.lib.agentic_publication import (
    PublicationSpec,
    prepare_publication,
    publish_publication,
)
from commonplace.lib.agentic_records import amendment_index

pytestmark = pytest.mark.usefixtures("tmp_library")


@pytest.fixture(autouse=True)
def running_package_is_the_fixture_repository(tmp_path, monkeypatch):
    """Fixture runs pin inputs-commit in their own repository, not this checkout."""
    monkeypatch.setattr(agentic_publication, "running_package_root", lambda: tmp_path)

REPO_ROOT = Path(__file__).resolve().parents[3]
RUN_ID = "AAS-2026-09-04-example-system-01"
RETAINED_OVERVIEW = agentic_set.RETAINED_ROOT / "example-system" / "overview.md"
SOURCE = "https://example.invalid/example-system"
STATE_DIR = Path("kb/agentic-system-analyses/state")
REVIEW_PATH = "kb/agentic-system-analyses/retained/example-system/overview.md"
# A placeholder method commit for fixtures that never publish; publication
# fixtures pin the fixture repository's real HEAD.
INPUTS_COMMIT = "f" * 40
MEMBER_TYPES = {
    "memory-profile.md": "agentic-system-analyses/types/agent-memory-profile.md",
    "runtime.md": "agentic-system-analyses/types/agentic-system-runtime-report.md",
    "memory.md": "agentic-system-analyses/types/agent-memory-analysis-report.md",
    "epistemic.md": "agentic-system-analyses/types/agentic-system-epistemic-report.md",
    "reconciliation.md": "agentic-system-analyses/types/agentic-system-reconciliation-report.md",
}


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


def state_text(frontmatter: dict[str, object]) -> str:
    return (
        "---\n"
        + yaml.safe_dump(frontmatter, sort_keys=False)
        + "---\n\n"
        + f"# Agentic-system analysis run — {RUN_ID}\n\n"
        + "## Run\n\nFixture run.\n\n"
        + "## Outcome\n\nFixture outcome.\n"
    )


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
    return write(run_dir / "output/memory-profile.md", "---\n" + yaml.safe_dump(values, sort_keys=False) + "---\n\n# Fixture memory profile\n\n## Comparison rationale\n\nBoth stores are MEM-OBJ-store.\n")


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
        run_dir / "output/memory.md",
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


def boundary_text(revision: str, *, source: str = SOURCE) -> str:
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
  path: /fixture/example-system
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

## Boundary and evidence

Fixture boundary at `{revision}`.

## Source register

| SRC-1 | git | `{SOURCE}` | `{revision}` | implementation | README.md | `README.md` | none |

{amendment_index(members['reconciliation.md'].read_text())}

## Bounded synthesis

Fixture synthesis over RT-OBJ-store, MEM-OBJ-store, EPI-OBJ-store and RT-RTE-model-call.

## Limitations

None.

## Verification and blockers

### Record verification

Passed.

### Profile verification

Profile passes.

### Synthesis verification

Passed.

### Deterministic validation

Passed.

### Blockers

none
"""


def review_text(revision: str, overview: Path) -> str:
    return overview.read_text()


def run_dir_of(tmp_path: Path, run_id: str = RUN_ID) -> Path:
    return tmp_path / STATE_DIR / run_id


def output_path(run_dir: Path, name: str) -> Path:
    if name in (*SET_NAMES, "ARTIFACT.yaml"):
        return run_dir / "output" / name
    return run_dir / name


def repin(directory: Path) -> None:
    manifest = {"type": agentic_set.SET_TYPE, "members": {
        path.name: {"sha256": digest(path)} for path in sorted(directory.glob("*.md"))
    }}
    write(directory / "ARTIFACT.yaml", yaml.safe_dump(manifest, sort_keys=False))


def retained_fixture_paths(run_id: str) -> dict[str, Path]:
    directory = RETAINED_OVERVIEW.parent
    return {name: directory / name for name in ("ARTIFACT.yaml", *SET_NAMES)}


def retain_set(tmp_path: Path, run_dir: Path, run_id: str = RUN_ID) -> None:
    directory = RETAINED_OVERVIEW.parent
    for name in ("ARTIFACT.yaml", *SET_NAMES):
        retained = directory / name
        (tmp_path / retained).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / retained).write_bytes((output_path(run_dir, name)).read_bytes())


def write_set(run_dir: Path, revision: str) -> Path:
    """Write the members and the overview pinning them."""
    write(run_dir / "output/boundary.md", boundary_text(revision))
    members = {
        "runtime.md": write(run_dir / "output/runtime.md", runtime_text(revision)),
        "memory.md": memory_report_fixture(run_dir, revision),
        "memory-profile.md": profile_report_fixture(run_dir, revision),
        "epistemic.md": write(run_dir / "output/epistemic.md", epistemic_text(revision)),
        "reconciliation.md": write(run_dir / "output/reconciliation.md", reconciliation_text(revision)),
    }
    overview = write(run_dir / "output/overview.md", overview_text(revision, members))
    repin(run_dir / "output")
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
    reconciliation = run / "output/reconciliation.md"
    reconciliation.write_text(reconciliation.read_text() +
        "\nAmendment: EPI-OBJ-store is superseded by RT-OBJ-store; identity evidence at SRC-1.\n")
    repin(reconciliation.parent)
    failures = validation.validate_note(reconciliation.parent, repo_root=tmp_path).fails
    assert any("amendment index does not match" in failure for failure in failures)


def valid_run_state(tmp_path: Path) -> Path:
    configure_types(tmp_path)
    run_dir = run_dir_of(tmp_path)
    source_root, revision = git_checkout(
        tmp_path / "related-systems/example--system"
    )
    overview = write_set(run_dir, revision)
    retain_set(tmp_path, run_dir)
    generated = write(tmp_path / REVIEW_PATH, review_text(revision, overview))
    run_frontmatter: dict[str, object] = {
        "type": "agentic-system-analyses/types/agentic-system-analysis-run-state.md",
        "description": f"Minimal completion state for {RUN_ID}",
        "run-id": RUN_ID,
        "system": "Example System",
        "run-status": "complete",
        "result-disposition": "complete",
        "source": {
            "kind": "git",
            "identity": SOURCE,
            "revision": revision,
            "path": source_root.as_posix(),
            "sha256": None,
        },
        "artifact": {
            "path": (STATE_DIR / RUN_ID / "output/ARTIFACT.yaml").as_posix(),
            "sha256": digest(overview.with_name("ARTIFACT.yaml")),
        },
        "generated-review": {
            "path": REVIEW_PATH,
            "sha256": digest(generated),
        },
        "failure": None,
    }
    return write(run_dir / "run-state.md", state_text(run_frontmatter))


def sync_set(tmp_path: Path, values: dict) -> None:
    """Re-derive the manifest, retained copies and pins after an edit.

    The memory member follows the state's source identity and boundary, as the
    specialist's report would; the review's pin follows the overview.
    """
    run_dir = tmp_path / Path(values["artifact"]["path"]).parent.parent
    report = run_dir / "output/memory.md"
    report_values = frontmatter(report)
    report_values.update({"source-identity": values["source"]["identity"],
                          "reviewed-boundary": values["source"]["revision"]})
    replace_frontmatter(report, report_values)
    boundary = run_dir / "output/boundary.md"
    boundary_values = frontmatter(boundary)
    boundary_values["reviewed-boundary"] = values["source"]["revision"]
    boundary_values["source"] = {**boundary_values["source"], "identity": values["source"]["identity"],
                                 "revision": values["source"]["revision"]}
    replace_frontmatter(boundary, boundary_values)
    profile = run_dir / "output/memory-profile.md"
    replace_frontmatter(profile, {**frontmatter(profile),
                                 "source-identity": values["source"]["identity"],
                                 "reviewed-boundary": values["source"]["revision"]})
    generated = tmp_path / values["generated-review"]["path"]
    if generated.exists():
        (run_dir / "output/overview.md").write_bytes(generated.read_bytes())
    expected = agentic_set.RETAINED_ROOT / agentic_set.source_slug(values["source"]["identity"], values["system"]) / "overview.md"
    if generated != tmp_path / expected:
        generated.parent.rename((tmp_path / expected).parent)
        generated = tmp_path / expected
        values["generated-review"]["path"] = expected.as_posix()
    repin(run_dir / "output")
    for name in ("ARTIFACT.yaml", *SET_NAMES):
        (generated.parent / name).write_bytes((run_dir / "output" / name).read_bytes())
    values["artifact"]["sha256"] = digest(run_dir / "output/ARTIFACT.yaml")
    values["generated-review"]["sha256"] = digest(generated)


def rewrite_boundary(tmp_path: Path, run_dir: Path, old: str, new: str) -> None:
    """Move every set document and the review to another boundary."""
    for path in (*(output_path(run_dir, name) for name in ("boundary.md", "overview.md", *MEMBER_TYPES)),
                 tmp_path / REVIEW_PATH):
        path.write_text(path.read_text(encoding="utf-8").replace(old, new), encoding="utf-8")


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


def commit_inputs(tmp_path: Path) -> str:
    """Make the fixture tree a repository whose initial commit holds the run's inputs.

    The run directory and the source checkout are ignored, as in the real
    repository, so the run's own files never dirty the tree.
    """
    write(tmp_path / ".gitignore", "kb/agentic-system-analyses/state/\nrelated-systems/\n")
    run_git(tmp_path, "init", "--quiet")
    return commit_paths(tmp_path, "Commit the run's inputs", ".")


def pin_inputs_commit(run_dir: Path, commit: str, candidate: Path | None = None) -> None:
    """Record the method commit in the overview and re-pin the candidate review to it."""
    overview = run_dir / "output/overview.md"
    replace_frontmatter(overview, {**frontmatter(overview), "inputs-commit": commit})
    repin(overview.parent)


def publication_fixture(tmp_path: Path) -> tuple[Path, PublicationSpec, bytes]:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    destination = values["generated-review"]["path"]
    public = tmp_path / destination
    candidate = state.parent / "output/overview.md"
    candidate.write_bytes(public.read_bytes())
    public.unlink()
    shutil.rmtree(tmp_path / RETAINED_OVERVIEW.parent)
    head = commit_inputs(tmp_path)
    pin_inputs_commit(state.parent, head, candidate)
    values.update({"run-status": "running", "result-disposition": None,
                   "artifact": None, "generated-review": None, "failure": None})
    replace_frontmatter(state, values)
    spec = PublicationSpec(tmp_path, state, candidate, destination, "absent")
    return state, spec, candidate.read_bytes()


def inspect(tmp_path: Path, spec: PublicationSpec) -> dict[str, object]:
    from commonplace.lib.agentic_publication import inspect_destination

    return inspect_destination(
        repo_root=tmp_path, generated_destination=spec.generated_destination,
        source_identity=SOURCE,
    )


def test_complete_run_state_verifies_source_and_outputs(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
    assert results.note_type == "agentic-system-analysis-run-state"
    assert any("run state: complete" in item for item in results.passes)
    assert any("README.md" in item and "resolve" in item for item in results.passes)


def test_generated_review_must_live_in_reviews_directory(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    values["generated-review"]["path"] = (  # type: ignore[index]
        "kb/agentic-systems/example-system.md"
    )
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any(
        "expected kb/agentic-system-analyses/retained/<slug>/overview.md" in item
        for item in results.fails
    )


def test_failed_state_requires_only_a_reason(tmp_path: Path) -> None:
    configure_types(tmp_path)
    state = tmp_path / f"kb/agentic-system-analyses/state/{RUN_ID}/run-state.md"
    values: dict[str, object] = {
        "type": "agentic-system-analyses/types/agentic-system-analysis-run-state.md",
        "description": f"Failed run {RUN_ID}",
        "run-id": RUN_ID,
        "system": "Example System",
        "run-status": "failed",
        "result-disposition": None,
        "source": None,
        "artifact": None,
        "generated-review": None,
        "failure": "Generated review candidate failed validation; rerun required.",
    }
    write(state, state_text(values))

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []


def test_failed_state_without_reason_is_rejected(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    values.update(
        {
            "run-status": "failed",
            "result-disposition": None,
            "source": None,
            "artifact": None,
            "generated-review": None,
            "failure": None,
        }
    )
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("failure" in item for item in results.fails)


def test_complete_state_rejects_a_member_that_drifted_from_the_manifest(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    path = state.parent / "output/runtime.md"
    path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("manifest member runtime.md: SHA-256 mismatch" in item for item in results.fails)


def test_complete_state_rejects_an_invalid_member_pinned_by_the_manifest(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    path = state.parent / "output/runtime.md"
    path.write_text(
        path.read_text(encoding="utf-8").replace("## Annotations", "## Renamed"), encoding="utf-8"
    )
    values = frontmatter(state)
    sync_set(tmp_path, values)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("member runtime.md" in item for item in results.fails)


def test_complete_state_rejects_generated_review_from_another_source(
    tmp_path: Path,
) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    generated = tmp_path / values["generated-review"]["path"]  # type: ignore[index]
    content = generated.read_text(encoding="utf-8").replace(
        "https://example.invalid/example-system",
        "https://example.invalid/another-system",
    )
    generated.write_text(content, encoding="utf-8")
    values["generated-review"]["sha256"] = digest(generated)  # type: ignore[index]
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("exact" in item or "SHA-256" in item for item in results.fails)


def test_manifest_hash_must_be_a_digest(tmp_path):
    directory = member_fixture(tmp_path) / "output"
    manifest = directory / "ARTIFACT.yaml"
    values = yaml.safe_load(manifest.read_text())
    values["members"]["runtime.md"]["sha256"] = "bad"
    manifest.write_text(yaml.safe_dump(values))
    with pytest.raises(ValueError, match="malformed SHA-256"):
        agentic_set.load_member_set(directory, run=validation.ValidationRun(tmp_path, ()))


def test_complete_state_verifies_the_set_beyond_each_member(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    run_dir = state.parent
    values = frontmatter(state)
    sync_set(tmp_path, values)
    expected = "memory-profile.md: identity field source-identity 'https://example.invalid/example-system' does not match memory.md"
    path = run_dir / "output/memory.md"
    replace_frontmatter(path, {**frontmatter(path), "source-identity": "https://example.invalid/other"})
    # Re-pin the manifest and copies around the edit without regenerating the member.
    overview = run_dir / "output/overview.md"
    repin(overview.parent)
    retain_set(tmp_path, run_dir)
    values["artifact"]["sha256"] = digest(overview.with_name("ARTIFACT.yaml"))
    generated = tmp_path / REVIEW_PATH
    values["generated-review"]["sha256"] = digest(generated)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any(expected in item for item in results.fails), results.fails


def test_capture_source_is_byte_verified(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    capture = write(tmp_path / "source.bundle", "# Frozen source\ncaptured source\n")
    values = frontmatter(state)
    values["source"] = {
        "kind": "capture",
        "identity": "document bundle",
        "revision": "capture-2026-09-04",
        "path": capture.as_posix(),
        "sha256": digest(capture),
    }
    old_revision = frontmatter(state.parent / "output/overview.md")["reviewed-boundary"]
    rewrite_boundary(tmp_path, state.parent, old_revision, "capture-2026-09-04")
    report = state.parent / "output/memory.md"
    report.write_text(report.read_text().replace(
        "`README.md` @ `capture-2026-09-04`",
        f"`{capture.as_posix()}` @ `sha256:{digest(capture)}`",
    ))
    generated = tmp_path / values["generated-review"]["path"]  # type: ignore[index]
    generated.write_text(
        generated.read_text(encoding="utf-8").replace(
            f"source-identity: {SOURCE}",
            "source-identity: document bundle",
        )
        + "\n> captured\n> source\n"
        + f"> --- `{capture.as_posix()}` @ `sha256:{digest(capture)}`\n",
        encoding="utf-8",
    )
    sync_set(tmp_path, values)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
    assert any("frozen capture" in item for item in results.passes)


@pytest.mark.parametrize(
    ("citation", "expected_error"),
    [
        ("EXAMPLE/System/blob/{revision}/README.md", None),
        ("example/system/blob/{revision}/README.md", None),
        ("unrelated/other/blob/{revision}/README.md", "uses repository"),
        ("example/system/blob/main/README.md", "uses revision"),
        ("example/system/blob/{revision}/missing.md", "does not resolve to a blob"),
        ("example/system/blob/{revision}/README.md#L1", "cite the path without a range"),
    ],
)
def test_github_citations_match_the_frozen_source(
    tmp_path: Path, citation: str, expected_error: str | None
) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    source_identity = "https://github.com/example/system"
    values["source"]["identity"] = source_identity
    revision = values["source"]["revision"]
    generated = tmp_path / values["generated-review"]["path"]
    generated_values = frontmatter(generated)
    generated_values["source-identity"] = source_identity
    replace_frontmatter(generated, generated_values)

    output = tmp_path / values["generated-review"]["path"]
    target = citation.format(revision=revision)
    with output.open("a", encoding="utf-8") as handle:
        handle.write(f"\nSource evidence: [source](https://github.com/{target}).\n")
    sync_set(tmp_path, values)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    if expected_error is None:
        assert results.fails == []
        assert any("resolve" in item and "GitHub" in item for item in results.passes)
    else:
        assert any(expected_error in item for item in results.fails)


@pytest.mark.parametrize("citation_kind", ["local", "github"])
def test_quote_anchors_resolve_from_the_recorded_commit(
    tmp_path: Path, citation_kind: str
) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    revision = values["source"]["revision"]
    if citation_kind == "github":
        source_identity = "https://github.com/example/system"
        values["source"]["identity"] = source_identity
        generated = tmp_path / values["generated-review"]["path"]
        replace_frontmatter(
            generated,
            {**frontmatter(generated), "source-identity": source_identity},
        )
        attribution = (
            "[README.md](https://github.com/example/system/blob/"
            f"{revision}/README.md)"
        )
    else:
        attribution = f"`README.md` @ `{revision}`"

    source_root = Path(values["source"]["path"])
    write(source_root / "README.md", "# Changed worktree\n")
    output = tmp_path / values["generated-review"]["path"]
    with output.open("a", encoding="utf-8") as handle:
        handle.write(
            "\n> # Frozen\n> source\n"
            f"> --- {attribution}\n"
        )
    sync_set(tmp_path, values)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []
    assert any("quote resolves" in item for item in results.passes)


def test_quote_anchor_rejects_text_found_only_in_the_worktree(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    revision = values["source"]["revision"]
    source_root = Path(values["source"]["path"])
    write(source_root / "README.md", "# Changed worktree\n")
    generated = tmp_path / values["generated-review"]["path"]
    with generated.open("a", encoding="utf-8") as handle:
        handle.write(
            "\n> # Changed worktree\n"
            f"> --- `README.md` @ `{revision}`\n"
        )
    sync_set(tmp_path, values)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("quote does not occur" in item for item in results.fails)


def test_handoff_command_refuses_a_running_run(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    values.update(
        {
            "run-status": "running",
            "result-disposition": None,
            "source": None,
            "artifact": None,
            "generated-review": None,
        }
    )
    replace_frontmatter(state, values)
    monkeypatch.chdir(tmp_path)

    exit_code = agentic_analysis_handoff.main(
        [state.relative_to(tmp_path).as_posix()]
    )

    assert exit_code == 1
    assert "complete run state" in capsys.readouterr().err


def test_handoff_command_renders_a_valid_run(
    tmp_path: Path,
    monkeypatch,
    capsys,
) -> None:
    state = valid_run_state(tmp_path)
    monkeypatch.chdir(tmp_path)

    exit_code = agentic_analysis_handoff.main(
        [state.relative_to(tmp_path).as_posix()]
    )

    assert exit_code == 0
    assert f"# Agentic-system analysis handoff — {RUN_ID}" in capsys.readouterr().out


@pytest.mark.parametrize("mutation", ["valid", "outside"])
def test_profile_resolves_canonical_record_declarations(tmp_path: Path, mutation: str) -> None:
    directory = member_fixture(tmp_path) / "output"
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


def test_publication_cannot_consume_specialist_evidence_as_candidate(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    for name in (
        "incumbent-review.md",
        "runtime.md", "memory.md", "epistemic.md",
        "incumbent-overview.md", "incumbent-memory.md",
    ):
        candidate = PublicationSpec(tmp_path, state, output_path(state.parent, name), spec.generated_destination, "absent")
        with pytest.raises(ValueError, match="accepted output/overview.md"):
            prepare_publication(candidate)


def commit_incumbent(tmp_path: Path, path: Path) -> None:
    commit_paths(tmp_path, "Record incumbent", path)


@pytest.mark.parametrize("staged", [True, False])
def test_prepare_rejects_a_locally_deleted_review(
    tmp_path: Path, staged: bool
) -> None:
    state, spec, generated_bytes = publication_fixture(tmp_path)
    destination = spec.generated_destination
    assert destination is not None
    incumbent = tmp_path / destination
    incumbent.parent.mkdir(parents=True, exist_ok=True)
    incumbent.write_bytes(generated_bytes)
    commit_incumbent(tmp_path, incumbent)
    incumbent.unlink()
    if staged:
        subprocess.run(["git", "-C", str(tmp_path), "add", destination], check=True)

    with pytest.raises(ValueError, match="clean worktree") as error:
        prepare_publication(spec)

    assert destination in str(error.value)
    assert not incumbent.exists()
    assert frontmatter(state)["run-status"] == "running"


@pytest.mark.parametrize("mutation", ["bytes", "run", "source", "boundary"])
def test_publication_requires_an_exact_memory_member(tmp_path: Path, mutation: str) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    report = state.parent / "output/memory.md"
    if mutation == "bytes":
        report.write_text(report.read_text() + "\nChanged.\n")
    else:
        values = frontmatter(report)
        field = {"run": "run-id", "source": "source-identity", "boundary": "reviewed-boundary"}[mutation]
        values[field] = "different"
        replace_frontmatter(report, values)
        repin(state.parent / "output")
    with pytest.raises(ValueError, match="memory"):
        publish_publication(spec)
    assert not (tmp_path / spec.generated_destination).exists()
    assert frontmatter(state)["run-status"] == "running"


def test_publish_replaces_the_set_and_completes_run_state(tmp_path: Path) -> None:
    state, spec, generated_bytes = publication_fixture(tmp_path)
    prepare_publication(spec)

    published = publish_publication(spec)

    assert (tmp_path / spec.generated_destination).read_bytes() == generated_bytes
    assert spec.generated_candidate_path.exists()
    values = frontmatter(state)
    assert values["run-status"] == "complete"
    assert values["artifact"]["path"].endswith(f"{RUN_ID}/output/ARTIFACT.yaml")
    assert (tmp_path / published.retained_path).read_bytes() == (state.parent / "output/ARTIFACT.yaml").read_bytes()
    for name, retained in retained_fixture_paths(RUN_ID).items():
        assert (tmp_path / retained).read_bytes() == (output_path(state.parent, name)).read_bytes()
    assert published.cleanup_warnings == ()
    assert validation.validate_note(state, repo_root=tmp_path).fails == []
    # The published set loads as comparison evidence without edits.
    rows = systems_matrix.load_results(tmp_path).rows
    assert [row["analysis_run"] for row in rows] == [RUN_ID]
    assert rows[0]["artifact_sha256"] == digest(tmp_path / published.retained_path)


def test_publication_resolves_links_to_results_in_the_same_set(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    retained = tmp_path / RETAINED_OVERVIEW
    candidate = spec.generated_candidate_path
    content = candidate.read_text() + (
        "\n[Exact analysis](overview.md)\n"
    )
    candidate.write_text(content)
    repin(candidate.parent)

    prepare_publication(spec)
    assert not retained.exists()
    assert not (tmp_path / spec.generated_destination).exists()

    candidate.write_text(content + "\n[Missing](./not-in-the-set.md)\n")
    repin(candidate.parent)
    with pytest.raises(ValueError, match="missing target ./not-in-the-set.md"):
        prepare_publication(spec)
    assert not retained.exists()

    candidate.write_text(content)
    repin(candidate.parent)
    prepare_publication(spec)
    publish_publication(spec)
    assert retained.read_bytes() == (state.parent / "output/overview.md").read_bytes()
    assert (tmp_path / spec.generated_destination).read_text() == content
    checks = validation.validate_note(state, repo_root=tmp_path)
    assert checks.fails == []
    assert checks.warns == []


def test_publish_rolls_back_an_ordinary_multi_file_write_failure(
    tmp_path: Path,
    monkeypatch,
) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    prepare_publication(spec)
    original_state = state.read_bytes()
    failure_destination = state
    real_atomic_write = agentic_publication.atomic_write

    def fail_on_state(path: Path, content: bytes) -> None:
        if path == failure_destination:
            raise OSError("injected write failure")
        real_atomic_write(path, content)

    monkeypatch.setattr(agentic_publication, "atomic_write", fail_on_state)

    try:
        publish_publication(spec)
    except OSError as exc:
        assert "injected write failure" in str(exc)
    else:
        raise AssertionError("publication unexpectedly survived injected failure")

    assert not (tmp_path / spec.generated_destination).exists()
    assert not (tmp_path / RETAINED_OVERVIEW).parent.exists()
    assert state.read_bytes() == original_state
    assert spec.generated_candidate_path.exists()

    # A retry with the same run ID succeeds once the failure is gone.
    monkeypatch.setattr(agentic_publication, "atomic_write", real_atomic_write)
    publish_publication(spec)
    assert frontmatter(state)["run-status"] == "complete"


def test_comparison_tools_use_retained_results_without_local_or_legacy_inputs(tmp_path, monkeypatch):
    import csv
    import io

    from scripts import build_systems_matrix, render_systems_table

    state = valid_run_state(tmp_path)
    retained = tmp_path / RETAINED_OVERVIEW
    shutil.rmtree(tmp_path / "kb/agentic-system-analyses/state")
    shutil.rmtree(tmp_path / "kb/agent-memory-systems")
    shutil.rmtree(tmp_path / "related-systems")
    assert not state.exists()
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
    valid_run_state(tmp_path)
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
    """A link out of output/ resolves in the run directory but breaks once retained."""
    overview = member_fixture(tmp_path) / "output/overview.md"
    overview.write_text(overview.read_text().replace(
        "Fixture synthesis over", f"Read {link}. Fixture synthesis over"
    ))
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
    target = f"kb/agentic-system-analyses/state/{RUN_ID}/output"

    assert main([target, "--json"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert [artifact["path"] for artifact in report["analysed_artifacts"]] == [target]
    assert report["analysed_artifacts"][0]["type"] == agentic_set.SET_TYPE
    assert main([target, "--full"]) == 0


def test_comparison_population_must_select_one_review_per_source(tmp_path):
    valid_run_state(tmp_path)
    current = tmp_path / RETAINED_OVERVIEW.parent
    shutil.copytree(current, current.with_name("twin"))
    with pytest.raises(ValueError, match="multiple current analyses"):
        systems_matrix.load_results(tmp_path)


def test_publication_requires_comparison_fields_and_preserves_retained_bytes(tmp_path):
    state, spec, _ = publication_fixture(tmp_path)
    memory = state.parent / "output/memory-profile.md"
    old_bytes = {name: (output_path(state.parent, name)).read_bytes() for name in ("memory-profile.md", "overview.md")}
    data = frontmatter(memory)
    data.pop("memory-comparison")
    replace_frontmatter(memory, data)
    with pytest.raises(ValueError, match="manifest member memory-profile.md: SHA-256 mismatch"):
        prepare_publication(spec)
    overview = state.parent / "output/overview.md"
    repin(overview.parent)
    with pytest.raises(ValueError, match="memory-comparison"):
        prepare_publication(spec)
    for name, content in old_bytes.items():
        (output_path(state.parent, name)).write_bytes(content)
    repin(state.parent / "output")
    retained = write(tmp_path / RETAINED_OVERVIEW, "frozen earlier overview\n")
    with pytest.raises(ValueError, match="ARTIFACT.yaml"):
        prepare_publication(spec)
    assert retained.read_text() == "frozen earlier overview\n"
    assert frontmatter(state)["run-status"] == "running"


def rerun_publication_fixture(tmp_path: Path) -> tuple[PublicationSpec, bytes, bytes]:
    """Create a second run over a real, uncommitted first publication."""
    from commonplace.lib.agentic_publication import inspect_destination

    state, first, _ = publication_fixture(tmp_path)
    publish_publication(first)
    old_review = (tmp_path / first.generated_destination).read_bytes()
    old_set = {name: (output_path(state.parent, name)).read_bytes() for name in ("ARTIFACT.yaml", *SET_NAMES)}
    next_id = RUN_ID[:-2] + "02"
    new_dir = state.parent.with_name(next_id)
    shutil.copytree(state.parent, new_dir)
    for path in new_dir.rglob("*.md"):
        path.write_text(path.read_text().replace(RUN_ID, next_id))
    repin(new_dir / "output")
    next_state = new_dir / "run-state.md"
    values = frontmatter(next_state)
    values.update({"run-status": "running", "result-disposition": None,
                   "artifact": None, "generated-review": None})
    replace_frontmatter(next_state, values)
    candidate = new_dir / "output/overview.md"
    candidate.write_text(old_review.decode().replace(RUN_ID, next_id))
    repin(new_dir / "output")
    inspection = inspect_destination(
        repo_root=tmp_path, generated_destination=first.generated_destination,
        source_identity=values["source"]["identity"],
    )
    return PublicationSpec(tmp_path, next_state, candidate, first.generated_destination,
                           inspection["expected_incumbent_sha256"]), old_review, old_set


def test_inspect_destination_cli_never_returns_prior_prose(tmp_path: Path, capsys) -> None:
    from commonplace.cli.agentic_analysis_publication import main
    state, spec, _ = publication_fixture(tmp_path)
    source = frontmatter(state)["source"]["identity"]
    args = ["inspect-destination", "--generated-destination", spec.generated_destination,
            "--source-identity", source]
    assert main(args, cwd=tmp_path) == 0
    assert json.loads(capsys.readouterr().out) == {
        "exists": False, "expected_incumbent_sha256": "absent",
    }
    secret = "INCUMBENT-PROSE-MUST-NOT-ENTER-COORDINATOR-CONTEXT"
    candidate = spec.generated_candidate_path
    candidate.write_text(candidate.read_text() + "\n" + secret + "\n")
    repin(candidate.parent)
    publish_publication(spec)
    assert main(args, cwd=tmp_path) == 0
    output = capsys.readouterr().out
    assert secret not in output
    assert set(json.loads(output)) == {"exists", "expected_incumbent_sha256"}
    assert json.loads(output)["expected_incumbent_sha256"] == digest(tmp_path / spec.generated_destination)


@pytest.mark.parametrize("tracked", [False, True])
def test_rerun_replaces_unchanged_publication_and_keeps_recovery_copies(tmp_path: Path, tracked: bool) -> None:
    spec, old_review, old_set = rerun_publication_fixture(tmp_path)
    if tracked:
        commit_incumbent(tmp_path, tmp_path / spec.generated_destination)
    prepare_publication(spec)
    publish_publication(spec)
    archive = tmp_path / agentic_set.ARCHIVE_ROOT / RUN_ID
    assert (archive / "overview.md").read_bytes() == old_review
    for name, content in old_set.items():
        assert (archive / name).read_bytes() == content
    assert validation.validate_note(spec.run_state_path, repo_root=tmp_path).fails == []


@pytest.mark.parametrize("mutation, error", [
    ("missing-overview", "ARTIFACT.yaml"),
    ("overview", "invalid ARTIFACT.yaml"),
    ("member", "manifest member runtime.md: SHA-256 mismatch"),
    ("source", "directory name does not match"),
    ("committed-then-staged", "local changes"),
])
def test_inspection_rejects_unverified_incumbents(tmp_path: Path, mutation: str, error: str) -> None:
    """An incumbent is checked by its bytes and pins; no publication receipt is read."""
    from commonplace.lib.agentic_publication import inspect_destination
    spec, _, _ = rerun_publication_fixture(tmp_path)
    review = tmp_path / spec.generated_destination
    retained = review.with_name("ARTIFACT.yaml")
    if mutation == "missing-overview":
        retained.unlink()
    elif mutation == "overview":
        retained.write_text(retained.read_text() + "\nAltered evidence.\n")
    elif mutation == "member":
        member = retained.with_name("runtime.md")
        member.write_text(member.read_text() + "\nAltered evidence.\n")
    elif mutation == "source":
        memory = retained.with_name("memory.md")
        replace_frontmatter(memory, {**frontmatter(memory), "source-identity": "https://example.invalid/other"})
        repin(retained.parent)
    else:
        commit_paths(tmp_path, "Record the first publication", review, retained.parent)
        review.write_text(review.read_text() + "\nHuman correction.\n")
        run_git(tmp_path, "add", "--", str(review))
    before = review.read_bytes()
    with pytest.raises(ValueError, match=error):
        inspect_destination(repo_root=tmp_path, generated_destination=spec.generated_destination,
                            source_identity=SOURCE)
    if mutation == "source":
        with pytest.raises(ValueError, match=error):
            publish_publication(spec)
    assert review.read_bytes() == before


def test_publish_rejects_destination_change_after_prepare(tmp_path: Path) -> None:
    spec, _, _ = rerun_publication_fixture(tmp_path)
    prepare_publication(spec)
    path = tmp_path / spec.generated_destination
    path.write_text(path.read_text() + "\nConcurrent edit.\n")
    changed = path.read_bytes()
    with pytest.raises(ValueError, match="SHA-256 mismatch"):
        publish_publication(spec)
    assert path.read_bytes() == changed
    assert frontmatter(spec.run_state_path)["run-status"] == "running"


def test_rerun_rollback_preserves_concurrent_incumbent_edit(tmp_path: Path, monkeypatch) -> None:
    spec, _, _ = rerun_publication_fixture(tmp_path)
    original_check = agentic_publication._check_set
    public = tmp_path / spec.generated_destination
    changed = public.read_bytes() + b"\nConcurrent human edit.\n"
    def edit_after_validation(spec):
        checked = original_check(spec)
        public.write_bytes(changed)
        return checked
    monkeypatch.setattr(agentic_publication, "_check_set", edit_after_validation)
    with pytest.raises(ValueError, match="changed during validation"):
        publish_publication(spec)
    assert public.read_bytes() == changed
    assert frontmatter(spec.run_state_path)["run-status"] == "running"
    assert not (tmp_path / agentic_set.ARCHIVE_ROOT / RUN_ID).exists()


def test_rerun_failure_restores_uncommitted_publication(tmp_path: Path, monkeypatch) -> None:
    spec, old_review, old_set = rerun_publication_fixture(tmp_path)
    original_write = agentic_publication.atomic_write

    def fail_completion(path, content):
        if path == spec.run_state_path:
            raise OSError("injected completion failure")
        original_write(path, content)

    monkeypatch.setattr(agentic_publication, "atomic_write", fail_completion)
    with pytest.raises(OSError, match="injected completion failure"):
        publish_publication(spec)
    assert (tmp_path / spec.generated_destination).read_bytes() == old_review
    for name, retained in retained_fixture_paths(RUN_ID).items():
        assert (tmp_path / retained).read_bytes() == old_set[name]
    assert frontmatter(spec.run_state_path)["run-status"] == "running"
    assert spec.generated_candidate_path.exists()
    assert not (tmp_path / agentic_set.ARCHIVE_ROOT / RUN_ID).exists()


def test_rerun_never_overwrites_a_conflicting_recovery_copy(tmp_path: Path) -> None:
    spec, old_review, _ = rerun_publication_fixture(tmp_path)
    backup = tmp_path / agentic_set.ARCHIVE_ROOT / RUN_ID / "overview.md"
    write(backup, "Other recovery evidence.\n")
    with pytest.raises(ValueError, match="archive destination already exists"):
        publish_publication(spec)
    assert backup.read_bytes() == b"Other recovery evidence.\n"
    assert (tmp_path / spec.generated_destination).read_bytes() == old_review


@pytest.mark.parametrize("path, accepted", [
    ("kb/notes/draft.md", False),
    ("kb/notes/zażółć gęślą.md", False),
    ("kb/agentic-systems/reviews/sibling.md", False),
    ("kb/agentic-system-analyses/retained/AAS-2026-09-04-sibling-01/overview.md", True),
    ("scratch.txt", True),
])
def test_untracked_files_block_publication_only_under_kb_outside_its_outputs(
    tmp_path: Path, path: str, accepted: bool
) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    write(tmp_path / path, "A sibling run's publication, or a stray file.\n")
    if accepted:
        agentic_publication.require_publishable_worktree(tmp_path)
        return
    with pytest.raises(ValueError, match="clean worktree") as error:
        inspect(tmp_path, spec)
    assert path in str(error.value)
    with pytest.raises(ValueError, match=re.escape(path)):
        prepare_publication(spec)
    assert frontmatter(state)["run-status"] == "running"


@pytest.mark.parametrize("staged", [False, True])
def test_a_modified_tracked_file_anywhere_blocks_publication(tmp_path: Path, staged: bool) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    tracked = tmp_path / ".gitignore"
    tracked.write_text(tracked.read_text() + "tmp/\n")
    if staged:
        run_git(tmp_path, "add", "--", ".gitignore")
    for operation in (lambda: inspect(tmp_path, spec), lambda: publish_publication(spec)):
        with pytest.raises(ValueError, match="local changes") as error:
            operation()
        assert ".gitignore" in str(error.value)
    assert not (tmp_path / spec.generated_destination).exists()
    assert frontmatter(state)["run-status"] == "running"


def test_a_modified_tracked_review_does_not_block_a_sibling_publication(tmp_path: Path) -> None:
    """A sibling run that replaced a committed review leaves it modified, not staged."""
    state, spec, _ = publication_fixture(tmp_path)
    sibling = write(tmp_path / "kb/agentic-system-analyses/retained-archive/sibling/overview.md", "# Sibling\n")
    commit_paths(tmp_path, "Record the sibling's earlier review", sibling)
    sibling.write_text("# Sibling, replaced by a later run\n")
    inspect(tmp_path, spec)
    publish_publication(spec)
    assert frontmatter(state)["run-status"] == "complete"


@pytest.mark.parametrize("method_path", [
    "kb/agentic-system-analyses/instructions/agentic-analysis-records.md",
    "kb/agentic-system-analyses/types/agentic-system-analysis-set.schema.yaml",
])
def test_publication_requires_the_method_unchanged_since_inputs_commit(tmp_path: Path, method_path: str) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    # Unrelated commits after inputs-commit, such as a sibling's publication, are fine.
    note = write(tmp_path / "kb/notes/unrelated.md", "# Unrelated\n")
    commit_paths(tmp_path, "Unrelated change", note)
    prepare_publication(spec)
    # A method change since inputs-commit is not.
    method = tmp_path / method_path
    method.write_text(method.read_text() + "\nMethod change.\n")
    commit_paths(tmp_path, "Change the method", method)
    with pytest.raises(ValueError, match="method paths changed since inputs-commit") as error:
        publish_publication(spec)
    assert method_path in str(error.value)
    assert not (tmp_path / spec.generated_destination).exists()
    assert frontmatter(state)["run-status"] == "running"


def test_publication_requires_the_running_package_to_match_inputs_commit(
    tmp_path: Path, monkeypatch
) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    package = write(tmp_path / "src/commonplace/__init__.py", "")
    commit_paths(tmp_path, "Add package source", package)
    pin_inputs_commit(state.parent, run_git(tmp_path, "rev-parse", "HEAD").strip(),
                      spec.generated_candidate_path)
    prepare_publication(spec)
    # A running package edited after inputs-commit, even uncommitted in another
    # checkout, is not the pinned method.
    other = tmp_path.parent / (tmp_path.name + "-running")
    subprocess.run(["git", "clone", "--quiet", str(tmp_path), str(other)], check=True)
    (other / "src/commonplace/__init__.py").write_text("# drifted\n")
    monkeypatch.setattr(agentic_publication, "running_package_root", lambda: other)
    with pytest.raises(ValueError, match="running commonplace source .* differs") as error:
        prepare_publication(spec)
    assert "src/commonplace/__init__.py" in str(error.value)
    monkeypatch.setattr(agentic_publication, "running_package_root", lambda: tmp_path / "kb")
    with pytest.raises(ValueError, match="not a source checkout"):
        prepare_publication(spec)
    assert frontmatter(state)["run-status"] == "running"


def test_publication_requires_inputs_commit_to_be_an_ancestor_of_head(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    pin_inputs_commit(state.parent, "0" * 40, spec.generated_candidate_path)
    with pytest.raises(ValueError, match="not an ancestor of HEAD"):
        prepare_publication(spec)
    assert frontmatter(state)["run-status"] == "running"


def test_member_validation_rejects_ranged_prose_anchors(tmp_path: Path) -> None:
    runtime = member_fixture(tmp_path) / "output/runtime.md"
    runtime.write_text(runtime.read_text() + "\nEvidence: `src/agent.py:120-140`.\n")
    checked = validation.validate_note(runtime, repo_root=tmp_path)
    assert any(
        "carries a line range" in item and "cite the path without a range, or quote the passage" in item
        for item in checked.fails
    )


def test_path_only_anchor_to_a_binary_blob_resolves(tmp_path: Path) -> None:
    from commonplace.lib.agentic_analysis import _verify_source_anchors

    root, _ = git_checkout(tmp_path / "source")
    (root / "paper.pdf").write_bytes(b"%PDF-1.4\n\xff\xfe\x00binary\n")
    revision = commit_paths(root, "Add binary paper", "paper.pdf")
    identity = "https://github.com/example/system"
    content = f"See [paper]({identity}/blob/{revision}/paper.pdf).\n"
    passes, failures = _verify_source_anchors(
        content, source_root=root, source_identity=identity, source_revision=revision
    )
    assert failures == []
    assert any("paper.pdf resolves at the recorded commit" in item for item in passes)
    _, failures = _verify_source_anchors(
        content.replace("paper.pdf", "missing.pdf"),
        source_root=root, source_identity=identity, source_revision=revision,
    )
    assert any("does not resolve to a blob" in item for item in failures)


def test_generated_source_links_publish_through_regular_validator(tmp_path, monkeypatch):
    original_checkout = git_checkout
    foreign = "https://github.com/other/repo/blob/" + "b" * 40 + "/example.md#L1"
    source_text = (
        "# Frozen source\n"
        "![Diagram](figures/source.png)\n"
        f"[Upstream]({foreign})\n"
        "Use `fictional/file.py:12-20` as an example.\n"
        " * repeated comment\n * repeated comment\n"
    )

    def source_with_examples(path):
        root, _ = original_checkout(path)
        readme = write(root / "README.md", source_text)
        commit_incumbent(root, readme)
        revision = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
        return root, revision

    monkeypatch.setattr(sys.modules[__name__], "git_checkout", source_with_examples)
    state, spec, _ = publication_fixture(tmp_path)
    from commonplace.lib.agentic_analysis import SourceIdentity

    source = frontmatter(state)["source"]
    identity = SourceIdentity("git", source["identity"], source["revision"], Path(source["path"]), None)
    # The worktree must not supply either the selected text or its locations.
    write(identity.path / "README.md", "uncommitted replacement\n")
    runtime = state.parent / "output/runtime.md"
    for text in [*source_text.splitlines()[1:4], "* repeated comment"]:
        if text == "* repeated comment":
            citation = f"> {text}\n> --- `README.md:6-6` @ `{identity.revision}`\n"
        else:
            citation = f"> {text}\n> --- `README.md`\n"
        runtime.write_text(runtime.read_text() + "\n" + citation)
    repin(state.parent / "output")
    prepare_publication(spec)
    published = publish_publication(spec)
    checked = validation.validate_note(state, repo_root=tmp_path)
    assert not checked.warns and not checked.fails
    assert (tmp_path / published.retained_path).read_bytes() == (state.parent / "output/ARTIFACT.yaml").read_bytes()


@pytest.mark.parametrize("addition,diagnostic", [
    ("\nBad range: `README.md:999`.\n", "cite the path without a range"),
    ("\n> absent source text\n> --- `README.md` @ `{revision}`\n", "quote does not occur"),
    ("\n> Frozen source\n> --- `README.md` @ `" + "0" * 40 + "`\n", "attribution uses revision"),
    ("\n> --- `README.md` @ `{revision}`\n", "no quoted text"),
])
def test_publication_validator_rejects_bad_evidence_without_writes(tmp_path, addition, diagnostic):
    state, spec, _ = publication_fixture(tmp_path)
    artifact = state.parent / "output/memory.md"
    revision = frontmatter(state)["source"]["revision"]
    artifact.write_text(artifact.read_text() + addition.format(revision=revision))
    repin(state.parent / "output")
    before = {p: p.read_bytes() for p in state.parent.iterdir() if p.is_file()}
    with pytest.raises(ValueError, match=diagnostic):
        prepare_publication(spec)
    assert before == {p: p.read_bytes() for p in state.parent.iterdir() if p.is_file()}
    assert not (tmp_path / spec.generated_destination).exists()


def test_source_failure_makes_prepare_exit_nonzero(tmp_path, capsys):
    state, spec, _ = publication_fixture(tmp_path)
    artifact = state.parent / "output/memory.md"
    artifact.write_text(artifact.read_text() + "\nBad range: `README.md:999`.\n")
    repin(state.parent / "output")
    status = agentic_analysis_publication.main([
        "prepare", str(state), "--generated-candidate", str(spec.generated_candidate_path),
        "--generated-destination", spec.generated_destination,
        "--expected-incumbent-sha256", "absent",
    ], cwd=tmp_path)
    assert status == 1
    assert "cite the path without a range" in capsys.readouterr().err
    assert not (tmp_path / spec.generated_destination).exists()


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope"])
def test_noncomplete_artifact_cannot_publish_or_supply_comparison(tmp_path, disposition):
    state, spec, _ = publication_fixture(tmp_path)
    directory = state.parent / "output"
    overview = directory / "overview.md"
    values = frontmatter(overview)
    values["result-disposition"] = disposition
    replace_frontmatter(overview, values)
    boundary = directory / "boundary.md"
    replace_frontmatter(boundary, {**frontmatter(boundary), "result-disposition": disposition})
    boundary.write_text(boundary.read_text() + "\n## Not reached\n\nFixture analysis was not reached.\n")
    overview.write_text(re.sub(r"(?m)^Amended or superseded records:.*\n", "",
        re.sub(r"(?:RT|MEM|EPI)-(?:OBJ|RTE|CMP|CLM|ABS|BAP)-[a-z][a-z0-9]*(?:-[a-z][a-z0-9]*){0,2}", "not evaluated", overview.read_text())))
    for name in MEMBER_TYPES:
        (directory / name).unlink()
    repin(directory)
    assert not validation.ValidationRun(tmp_path, ()).validate(directory).fails
    with pytest.raises(ValueError, match="requires a complete"):
        prepare_publication(spec)
    retained = tmp_path / RETAINED_OVERVIEW.parent
    shutil.copytree(directory, retained)
    review = tmp_path / REVIEW_PATH
    write(review, review_text(values["reviewed-boundary"], overview))
    with pytest.raises(ValueError, match="must be complete"):
        systems_matrix.load_results(tmp_path)


def test_run_state_repo_root_is_the_repository(tmp_path: Path) -> None:
    from commonplace.lib.agentic_analysis import run_state_repo_root

    state = tmp_path / STATE_DIR / RUN_ID / "run-state.md"

    assert run_state_repo_root(state) == tmp_path
    assert run_state_repo_root(tmp_path / "elsewhere" / "run-state.md") is None


@pytest.mark.parametrize("fault", ["before-move", "after-move", "copy"])
def test_archive_replacement_restores_exact_incumbent_on_failure(tmp_path, monkeypatch, fault):
    spec, _, old_set = rerun_publication_fixture(tmp_path)
    current = (tmp_path / spec.generated_destination).parent
    archive = tmp_path / agentic_set.ARCHIVE_ROOT / RUN_ID
    old_state = spec.run_state_path.read_bytes()
    rename, mkdir, atomic = Path.rename, Path.mkdir, agentic_publication.atomic_write
    def injected_rename(path, target):
        if fault == "before-move" and path == current:
            raise OSError("injected archive failure")
        return rename(path, target)
    def injected_mkdir(path, *args, **kwargs):
        if fault == "after-move" and path == current and archive.exists():
            raise OSError("injected archive failure")
        return mkdir(path, *args, **kwargs)
    def injected_write(path, content):
        if fault == "copy" and path.parent == current:
            raise OSError("injected archive failure")
        return atomic(path, content)
    monkeypatch.setattr(Path, "rename", injected_rename)
    monkeypatch.setattr(Path, "mkdir", injected_mkdir)
    monkeypatch.setattr(agentic_publication, "atomic_write", injected_write)
    with pytest.raises(OSError, match="injected archive failure"):
        publish_publication(spec)
    assert {p.name: p.read_bytes() for p in current.iterdir()} == old_set
    assert not archive.exists()
    assert spec.run_state_path.read_bytes() == old_state


def test_publication_refuses_a_wrong_source_slug(tmp_path):
    from dataclasses import replace
    _, spec, _ = publication_fixture(tmp_path)
    wrong = replace(spec, generated_destination="kb/agentic-system-analyses/retained/other/overview.md")
    with pytest.raises(ValueError, match="directory name does not match"):
        publish_publication(wrong)


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


def test_replacement_recognition_distinguishes_incumbent_from_interruption(tmp_path):
    from commonplace.lib.agentic_workflow import AnalyseAgenticSystem
    from commonplace.workflow import Recognition
    spec, _, _ = rerun_publication_fixture(tmp_path)
    definition = AnalyseAgenticSystem({"system": "Example System", "source-identity": SOURCE, "model": "fixture-model"})
    definition.run_id = spec.run_state_path.parent.name
    assert definition.recognize_publication(spec) is Recognition.ABSENT
    current = (tmp_path / spec.generated_destination).parent
    archive = tmp_path / agentic_set.ARCHIVE_ROOT / RUN_ID
    archive.parent.mkdir(parents=True)
    current.rename(archive)
    assert definition.recognize_publication(spec) is Recognition.UNKNOWN
    archive.rename(current)
    (current / "runtime.md").unlink()
    assert definition.recognize_publication(spec) is Recognition.UNKNOWN


def test_a_candidate_receives_only_its_own_roles_set_findings(tmp_path: Path) -> None:
    from commonplace.lib.agentic_workflow import set_role_refusals

    run_dir = member_fixture(tmp_path)
    output = run_dir / "output"
    epistemic = output / "epistemic.md"
    epistemic.write_text(epistemic.read_text() + "\nEPI-OBJ-dangling is cited here.\n")
    before = {path.name: path.read_bytes() for path in output.iterdir()}
    candidate = write(run_dir / "runtime-report-1.md",
                      (output / "runtime.md").read_text().replace(f"run-id: {RUN_ID}", "run-id: AAS-2026-09-04-other-01"))

    refusals = set_role_refusals(candidate, run_dir=run_dir, repo_root=tmp_path, role="runtime")

    assert refusals == [(
        f"[set] runtime.md: identity field run-id 'AAS-2026-09-04-other-01' does not match boundary.md; "
        f"expected '{RUN_ID}'"
    )]
    assert any("EPI-OBJ-dangling" in refusal for refusal in
               set_role_refusals(epistemic, run_dir=run_dir, repo_root=tmp_path, role="epistemic"))
    assert {path.name: path.read_bytes() for path in output.iterdir()} == before


def test_a_report_declares_only_its_types_record_prefix(tmp_path: Path) -> None:
    run_dir = member_fixture(tmp_path)
    runtime = run_dir / "output/runtime.md"
    assert not validation.validate_note(runtime, repo_root=tmp_path).fails
    runtime.write_text(runtime.read_text().replace("#### RT-OBJ-store —", "#### MEM-OBJ-store —", 1))
    failures = validation.validate_note(runtime, repo_root=tmp_path).fails
    assert any("this report declares only RT- records: MEM-OBJ-store" in failure for failure in failures)
