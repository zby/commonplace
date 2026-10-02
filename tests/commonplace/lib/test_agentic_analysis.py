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
    quote,
)
from commonplace.lib import agentic_publication, agentic_set, systems_matrix, validation
from commonplace.lib.agentic_analysis import (
    parse_agentic_analysis_run_state,
    render_agentic_analysis_handoff,
)
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
SOURCE = "https://example.invalid/example-system"
STATE_DIR = Path("kb/agentic-systems/reports/state")
REVIEW_PATH = "kb/agentic-systems/reviews/example-system.md"
# A placeholder method commit for fixtures that never publish; publication
# fixtures pin the fixture repository's real HEAD.
INPUTS_COMMIT = "f" * 40
MEMBER_TYPES = {
    "runtime.md": "agentic-systems/types/agentic-system-runtime-report.md",
    "memory.md": "agentic-systems/types/agent-memory-analysis-report.md",
    "epistemic.md": "agentic-systems/types/agentic-system-epistemic-report.md",
    "reconciliation.md": "agentic-systems/types/agentic-system-reconciliation-report.md",
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
        target = tmp_path / "kb/agentic-systems/instructions" / name
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(REPO_ROOT / "kb/agentic-systems/instructions" / name, target)
    shutil.copytree(REPO_ROOT / "kb/types", tmp_path / "kb/types")
    shutil.copytree(
        REPO_ROOT / "kb/agent-memory-systems/types",
        tmp_path / "kb/agent-memory-systems/types",
    )
    shutil.copytree(
        REPO_ROOT / "kb/agentic-systems/types",
        tmp_path / "kb/agentic-systems/types",
    )
    for collection in ("kb/reports", "kb/agentic-systems"):
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


def body_of(path: Path) -> str:
    document, error = validation.parse_document(path.read_text(encoding="utf-8"))
    assert error is None and document is not None
    return document.body


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


def memory_report_fixture(run_dir: Path, revision: str) -> Path:
    """The specialist's report, which is the memory member unchanged: one
    `MEM-` record, one annotated seed, one quote."""
    profile = uninspected_profile("The fixture's accumulated project memory and retrieval routes")
    profile["axes"]["storage_substrate"] = {
        "assessment": "known", "values": ["sqlite", "files"],
        "evidence": {v: {"basis": "wired", "records": ["MEM-OBJ-1"], "note": "Fixture witness."}
                     for v in ["sqlite", "files"]},
        "records": ["MEM-OBJ-1"], "note": "Both stores occur within the fixture boundary.",
    }
    values = {
        "type": "agentic-systems/types/agent-memory-analysis-report.md",
        "description": "Fixture specialist report bound to the frozen source and shared input",
        "run-id": RUN_ID,
        "source-identity": SOURCE,
        "reviewed-boundary": revision,
        "report-status": "complete",
        "memory-comparison": profile,
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

#### MEM-OBJ-1 — Fixture memory store

Store the specialist established, from SRC-1.

### Routes

#### On RT-RTE-1 — Fixture route

Seeded route with the specialist's memory fields.

### Claims

none proposed.

### Evidenced absences

none proposed.

### Behavioral-authority paths

none proposed.

## Write side

Fixture evidence on MEM-OBJ-1.

## Read-back

Fixture evidence on RT-RTE-1.

## Comparison rationale

Both stores are MEM-OBJ-1.

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
type: agentic-systems/types/agentic-system-runtime-report.md
description: "Runtime baseline of Example System at the fixture boundary"
run-id: {RUN_ID}
reviewed-boundary: {revision}
---

# Example System runtime report

## Runtime account

Implementation inspected at `README.md`; operation is unobserved.

## Shared records

### Components

#### RT-CMP-1 — Fixture component

Record. Evidence: SRC-1.

### Operative objects

#### RT-OBJ-1 — Fixture object

Record. Evidence: SRC-1.

### Routes

#### RT-RTE-1 — Fixture route

- implementation conclusion status: wired

- Immediate return: The fixture invocation returns the stored object.
- Later read-back: A later invocation reads RT-OBJ-1.
- Delegated visibility: inapplicable — the fixture has no delegated workers.
- Selection predicate: The caller requests the fixture object.
- Invalidation or expiry: inapplicable — the fixture has no expiry mechanism.
- Activation or effect: uninspected — no behavioral execution was observed.
- Evidence limits: Static fixture evidence at SRC-1; operation was not exercised.

Record. Evidence: SRC-1.

### Claims

#### RT-CLM-1 — Fixture claim

Record. Evidence: SRC-1.

### Evidenced absences

none found within the fixture boundary.

### Behavioral-authority paths

#### RT-BAP-1 — Fixture authority path

Record. Evidence: SRC-1.

## Annotations

none
"""


def epistemic_text(revision: str) -> str:
    return f"""---
type: agentic-systems/types/agentic-system-epistemic-report.md
description: "Epistemic routes of Example System at the fixture boundary"
run-id: {RUN_ID}
reviewed-boundary: {revision}
---

# Example System epistemic report

## Source-and-claim boundary

Boundary from the overview's Source register.

## Epistemic-object inventory

RT-OBJ-1 and EPI-OBJ-1 carry no candidate truth-apt content.

## Authority-route ledger

Route ID: RT-RTE-1
Route function: operational admission/selection/consumption
Architectural status: implemented
Content/update relation: no content change.

## System-claim versus route comparison

RT-CLM-1 is compared with RT-RTE-1.

## Bounded conclusion

Conclusion.

## Shared records

### Operative objects

#### EPI-OBJ-1 — Fixture checked object

Object the epistemic lens established. Evidence: SRC-1.
"""


def overview_text(
    revision: str, members: dict[str, Path], *, inputs_commit: str = INPUTS_COMMIT
) -> str:
    return f"""---
type: agentic-systems/types/agentic-system-analysis-overview.md
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

Fixture synthesis over RT-OBJ-1, MEM-OBJ-1, EPI-OBJ-1 and RT-RTE-1.

## Limitations

None.

## Verification and blockers

### Record verification

Passed.

### Synthesis verification

Passed.

### Deterministic validation

Passed.

### Blockers

none
"""


def review_text(revision: str, overview: Path) -> str:
    return f"""---
description: "Generated fixture review of one external agentic system"
type: agentic-systems/types/generated-review.md
generated-by: analyse-agentic-system
analysis-run: {RUN_ID}
source-identity: {SOURCE}
reviewed-revision: {revision}
analysis-artifact: {agentic_set.retained_artifact_path(RUN_ID).as_posix()}
analysis-artifact-sha256: {digest(overview.with_name("ARTIFACT.yaml"))}
---

# Example System

Evidence basis: `README.md` at `{revision}`.
"""


def run_dir_of(tmp_path: Path, run_id: str = RUN_ID) -> Path:
    return tmp_path / STATE_DIR / run_id


def output_path(run_dir: Path, name: str) -> Path:
    if name in (*agentic_set.SET_NAMES, "ARTIFACT.yaml"):
        return run_dir / "output" / name
    return run_dir / name


def repin(directory: Path) -> None:
    manifest = {"type": agentic_set.SET_TYPE, "members": {
        path.name: {"sha256": digest(path)} for path in sorted(directory.glob("*.md"))
    }}
    write(directory / "ARTIFACT.yaml", yaml.safe_dump(manifest, sort_keys=False))


def retain_set(tmp_path: Path, run_dir: Path, run_id: str = RUN_ID) -> None:
    for name, retained in agentic_set.retained_set_paths(run_id).items():
        (tmp_path / retained).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / retained).write_bytes((output_path(run_dir, name)).read_bytes())


def write_set(run_dir: Path, revision: str) -> Path:
    """Write the members and the overview pinning them."""
    members = {
        "runtime.md": write(run_dir / "output/runtime.md", runtime_text(revision)),
        "memory.md": memory_report_fixture(run_dir, revision),
        "epistemic.md": write(run_dir / "output/epistemic.md", epistemic_text(revision)),
        "reconciliation.md": write(run_dir / "output/reconciliation.md", reconciliation_text(revision)),
    }
    overview = write(run_dir / "output/overview.md", overview_text(revision, members))
    repin(run_dir / "output")
    return overview


def reconciliation_text(revision: str) -> str:
    return f'''---
type: agentic-systems/types/agentic-system-reconciliation-report.md
description: "Reconciled Example System records at the frozen source boundary"
run-id: {RUN_ID}
reviewed-boundary: {revision}
---

# Example System reconciliation

## Reconciliation

MEM-OBJ-1 and EPI-OBJ-1 duplicate no runtime record.
'''


def member_fixture(tmp_path: Path) -> Path:
    """A run directory's set without source checkout or run state, for checks of one document."""
    configure_types(tmp_path)
    run_dir = run_dir_of(tmp_path)
    write_set(run_dir, "a" * 40)
    return run_dir


def test_member_set_readers_preserve_runtime_ids(tmp_path: Path) -> None:
    prefix = "RT-"
    directory = member_fixture(tmp_path) / "output"
    member_set = agentic_set.load_member_set(
        directory, run=validation.ValidationRun(tmp_path, ()),
    )
    assert f"#### {prefix}RTE-1 — Fixture route" in member_set.members["runtime.md"].body
    profile = systems_matrix.memory_member_comparison(
        member_set.members["memory.md"].frontmatter,
        member_set.members["memory.md"].body,
    )
    assert f"#### On {prefix}RTE-1 — Fixture route" in member_set.members["memory.md"].body
    assert profile["axes"]["storage_substrate"]["records"] == ["MEM-OBJ-1"]


def test_overview_amendment_index_cannot_hide_an_amendment(tmp_path: Path) -> None:
    run = member_fixture(tmp_path)
    reconciliation = run / "output/reconciliation.md"
    reconciliation.write_text(reconciliation.read_text() +
        "\nAmendment: EPI-OBJ-1 is superseded by RT-OBJ-1; identity evidence at SRC-1.\n")
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
        "type": "agentic-systems/types/agentic-system-analysis-run-state.md",
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
    repin(run_dir / "output")
    retain_set(tmp_path, run_dir)
    values["artifact"]["sha256"] = digest(run_dir / "output/ARTIFACT.yaml")
    generated = tmp_path / values["generated-review"]["path"]
    replace_frontmatter(generated, {
        **frontmatter(generated), "analysis-artifact-sha256": digest(run_dir / "output/ARTIFACT.yaml"),
    })
    values["generated-review"]["sha256"] = digest(generated)


def rewrite_boundary(tmp_path: Path, run_dir: Path, old: str, new: str) -> None:
    """Move every set document and the review to another boundary."""
    for path in (*(output_path(run_dir, name) for name in ("overview.md", *MEMBER_TYPES)),
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
    write(tmp_path / ".gitignore", "kb/agentic-systems/reports/state/\nrelated-systems/\n")
    run_git(tmp_path, "init", "--quiet")
    return commit_paths(tmp_path, "Commit the run's inputs", ".")


def pin_inputs_commit(run_dir: Path, commit: str, candidate: Path | None = None) -> None:
    """Record the method commit in the overview and re-pin the candidate review to it."""
    overview = run_dir / "output/overview.md"
    replace_frontmatter(overview, {**frontmatter(overview), "inputs-commit": commit})
    repin(overview.parent)
    if candidate is not None:
        replace_frontmatter(
            candidate, {**frontmatter(candidate), "analysis-artifact-sha256": digest(overview.with_name("ARTIFACT.yaml"))}
        )


def publication_fixture(tmp_path: Path) -> tuple[Path, PublicationSpec, bytes]:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    destination = values["generated-review"]["path"]
    public = tmp_path / destination
    candidate = state.parent / "generated-review.candidate.md"
    candidate.write_bytes(public.read_bytes())
    public.unlink()
    shutil.rmtree(tmp_path / agentic_set.retained_overview_path(RUN_ID).parent)
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
        "expected kb/agentic-systems/reviews/<name>.md" in item
        for item in results.fails
    )


def test_running_state_needs_no_recovery_records(tmp_path: Path) -> None:
    configure_types(tmp_path)
    state = tmp_path / f"kb/agentic-systems/reports/state/{RUN_ID}/run-state.md"
    values: dict[str, object] = {
        "type": "agentic-systems/types/agentic-system-analysis-run-state.md",
        "description": f"Minimal completion state for {RUN_ID}",
        "run-id": RUN_ID,
        "system": "Example System",
        "run-status": "running",
        "result-disposition": None,
        "source": None,
        "artifact": None,
        "generated-review": None,
        "failure": None,
    }
    write(state, state_text(values))

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []


def test_failed_state_requires_only_a_reason(tmp_path: Path) -> None:
    configure_types(tmp_path)
    state = tmp_path / f"kb/agentic-systems/reports/state/{RUN_ID}/run-state.md"
    values: dict[str, object] = {
        "type": "agentic-systems/types/agentic-system-analysis-run-state.md",
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


def test_complete_state_rejects_changed_overview_bytes(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    overview = state.parent / "output/overview.md"
    overview.write_text(overview.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("overview.md: SHA-256 mismatch" in item for item in results.fails)


def test_complete_state_rejects_a_member_that_drifted_from_the_manifest(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    path = state.parent / "output/runtime.md"
    path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("manifest member runtime.md: SHA-256 mismatch" in item for item in results.fails)


def test_complete_state_rejects_invalid_overview_with_matching_hash(
    tmp_path: Path,
) -> None:
    state = valid_run_state(tmp_path)
    overview = state.parent / "output/overview.md"
    overview.write_text(
        overview.read_text(encoding="utf-8").replace("## Limitations\n\nNone.\n\n", ""),
        encoding="utf-8",
    )
    values = frontmatter(state)
    sync_set(tmp_path, values)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("member overview.md" in item for item in results.fails)


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

    assert any("source-identity" in item for item in results.fails)


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope"])
def test_blocked_overview_completes_without_members_or_public_review(tmp_path: Path, disposition: str) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    overview = state.parent / "output/overview.md"
    replace_frontmatter(overview, {
        **frontmatter(overview), "result-disposition": disposition, "target-class": None,
        "boundary-kind": None, "reviewed-boundary": None, "analysis-cutoff": None,
        "evidence-tier": None,
    })
    for name in MEMBER_TYPES:
        (output_path(state.parent, name)).unlink()
    overview.write_text(re.sub(r"(?m)^Amended or superseded records:.*\n", "",
        re.sub(r"(?:MEM-)?(?:OBJ|RTE|CMP|CLM|ABS|BAP)-\d+", "not evaluated", overview.read_text())))
    repin(overview.parent)
    values.update(
        {
            "result-disposition": disposition,
            "source": None,
            "artifact": {"path": values["artifact"]["path"], "sha256": digest(overview.with_name("ARTIFACT.yaml"))},  # type: ignore[index]
            "generated-review": None,
        }
    )
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []


@pytest.mark.parametrize("value", [12345, "bad", None])
def test_manifest_hash_must_be_a_digest(tmp_path, value):
    directory = member_fixture(tmp_path) / "output"
    manifest = directory / "ARTIFACT.yaml"
    values = yaml.safe_load(manifest.read_text())
    values["members"]["runtime.md"]["sha256"] = value
    manifest.write_text(yaml.safe_dump(values))
    with pytest.raises(ValueError, match="malformed SHA-256"):
        agentic_set.load_member_set(directory, run=validation.ValidationRun(tmp_path, ()))


def test_member_pass_needs_every_member_named(tmp_path: Path) -> None:
    """A complete state over a memberless overview never reports members present."""
    state = valid_run_state(tmp_path)
    overview = state.parent / "output/overview.md"
    replace_frontmatter(overview, {
        **frontmatter(overview), "result-disposition": "blocked",
    })
    values = frontmatter(state)
    repin(overview.parent)
    values["artifact"]["sha256"] = digest(overview.with_name("ARTIFACT.yaml"))  # type: ignore[index]
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert not any("manifest members present" in item for item in results.passes)
    assert any("properties" in item for item in results.fails), results.fails


@pytest.mark.parametrize("mutation", ["memory-source-identity", "runtime-run-id"])
def test_complete_state_verifies_the_set_beyond_each_member(tmp_path: Path, mutation: str) -> None:
    state = valid_run_state(tmp_path)
    run_dir = state.parent
    values = frontmatter(state)
    sync_set(tmp_path, values)
    expected = {
        "memory-source-identity": "memory.md: source-identity does not match the frozen source",
        "runtime-run-id": "runtime.md: run-id does not match the overview",
    }[mutation]
    if mutation == "memory-source-identity":
        path = run_dir / "output/memory.md"
        replace_frontmatter(path, {**frontmatter(path), "source-identity": "https://example.invalid/other"})
    else:
        path = run_dir / "output/runtime.md"
        replace_frontmatter(path, {**frontmatter(path), "run-id": RUN_ID[:-2] + "09"})
    # Re-pin the manifest and copies around the edit without regenerating the member.
    overview = run_dir / "output/overview.md"
    repin(overview.parent)
    retain_set(tmp_path, run_dir)
    values["artifact"]["sha256"] = digest(overview.with_name("ARTIFACT.yaml"))
    generated = tmp_path / REVIEW_PATH
    replace_frontmatter(generated, {**frontmatter(generated), "analysis-artifact-sha256": digest(overview.with_name("ARTIFACT.yaml"))})
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
        ("example/system/blob/{short_revision}/README.md", "uses revision"),
        ("example/system/blob/{wrong_revision}/README.md", "uses revision"),
        ("example/system/blob/{revision}/missing.md", "does not resolve to a blob"),
        ("example/system/blob/{revision}/README.md#L1", "cite the path without a range"),
        ("example/system/blob/{revision}/README.md#L1-L1", "cite the path without a range"),
        ("example/system/blob/{revision}/README.md#L1oops", "invalid GitHub line anchor"),
        ("example/system/blob/{revision}", "incomplete GitHub blob path"),
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
    target = citation.format(
        revision=revision,
        short_revision=revision[:8],
        wrong_revision="0" * len(revision),
    )
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


def test_operator_handoff_is_rendered_from_complete_state(tmp_path: Path) -> None:
    state_path = valid_run_state(tmp_path)
    content = state_path.read_text(encoding="utf-8")
    document, error = validation.parse_document(content)
    assert error is None and document is not None
    state = parse_agentic_analysis_run_state(
        state_path,
        document,
        repo_root=tmp_path,
    )

    rendered = render_agentic_analysis_handoff(state)

    assert RUN_ID in rendered
    assert "**Artifact:**" in rendered
    assert "**Members:** overview.md, runtime.md, memory.md, epistemic.md, reconciliation.md (pinned" in rendered
    assert "**Frozen source:**" in rendered
    assert (
        "**Generated system review:** "
        "kb/agentic-systems/reviews/example-system.md"
    ) in rendered
    assert "**Run status:** complete" in rendered


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


@pytest.mark.parametrize("mutation", ["valid", "annotated-seed", "empty", "outside"])
def test_standing_memory_report_comparison_validation(tmp_path: Path, mutation: str) -> None:
    report = member_fixture(tmp_path) / "output/memory.md"
    body = report.read_text().replace(
        "### Evidenced absences\n\nnone proposed.\n",
        "### Evidenced absences\n\n#### MEM-ABS-1 — Inspected absence\n\nSearched.\n",
    )
    report.write_text(body)
    metadata = frontmatter(report)
    axes = metadata["memory-comparison"]["axes"]
    axes["storage_substrate"] = {
        "assessment": "known", "values": ["files"],
        "evidence": {"files": {"basis": "wired", "records": ["MEM-OBJ-1"], "note": "Fixture witness."}},
        "records": ["MEM-OBJ-1"], "note": "Fixture source writes files.",
    }
    axes["trace_learning"] = {
        "assessment": "absent", "evidence": {}, "values": [],
        "records": ["MEM-ABS-1"], "note": "Fixture source was inspected.",
    }
    expected_error = None
    if mutation == "annotated-seed":
        axes["read_back_direction"] = {
            "assessment": "known", "values": ["pull"],
            "evidence": {"pull": {"basis": "wired", "records": ["RT-RTE-1"], "note": "Seeded route."}},
            "records": ["RT-RTE-1"], "note": "The annotated seed carries the route.",
        }
        axes["read_back_signal"]["assessment"] = "inapplicable"
    elif mutation == "empty":
        axes["storage_substrate"]["values"] = []
        expected_error = "known assessment needs"
    elif mutation == "outside":
        report.write_text(report.read_text().replace(
            "#### MEM-OBJ-1 — Fixture memory store\n", "",
        ) + "\nMEM-OBJ-1 outside the register.\n")
        expected_error = "storage_substrate: unresolved records"
    replace_frontmatter(report, metadata)
    checked = validation.validate_note(report, repo_root=tmp_path)
    if expected_error:
        assert any(expected_error in error for error in checked.fails)
    else:
        assert checked.fails == []
        assert any("declared or annotated references resolve" in message for message in checked.passes)


def test_publication_cannot_consume_specialist_evidence_as_candidate(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    for name in (
        "incumbent-review.md",
        "overview.md", "runtime.md", "memory.md", "epistemic.md",
        "incumbent-overview.md", "incumbent-memory.md",
    ):
        candidate = PublicationSpec(tmp_path, state, output_path(state.parent, name), spec.generated_destination, "absent")
        with pytest.raises(ValueError, match="reserved"):
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


@pytest.mark.parametrize("mutation", ["bytes", "run", "source", "boundary", "blocked"])
def test_publication_requires_an_exact_complete_memory_member(tmp_path: Path, mutation: str) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    report = state.parent / "output/memory.md"
    if mutation == "bytes":
        report.write_text(report.read_text() + "\nChanged.\n")
    else:
        values = frontmatter(report)
        field = {"run": "run-id", "source": "source-identity", "boundary": "reviewed-boundary", "blocked": "report-status"}[mutation]
        values[field] = "blocked" if mutation == "blocked" else "different"
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
    assert not spec.generated_candidate_path.exists()
    values = frontmatter(state)
    assert values["run-status"] == "complete"
    assert values["artifact"]["path"].endswith(f"{RUN_ID}/output/ARTIFACT.yaml")
    assert (tmp_path / published.retained_path).read_bytes() == (state.parent / "output/ARTIFACT.yaml").read_bytes()
    for name, retained in agentic_set.retained_set_paths(RUN_ID).items():
        assert (tmp_path / retained).read_bytes() == (output_path(state.parent, name)).read_bytes()
    assert published.cleanup_warnings == ()
    assert validation.validate_note(state, repo_root=tmp_path).fails == []


def test_publication_resolves_links_to_results_in_the_same_set(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    retained = tmp_path / agentic_set.retained_overview_path(RUN_ID)
    candidate = spec.generated_candidate_path
    content = candidate.read_text() + (
        f"\n[Exact analysis](../reports/retained/{RUN_ID}/overview.md)\n"
    )
    candidate.write_text(content)

    prepare_publication(spec)
    assert not retained.exists()
    assert not (tmp_path / spec.generated_destination).exists()

    candidate.write_text(content + "\n[Missing](./not-in-the-set.md)\n")
    with pytest.raises(ValueError, match="missing target ./not-in-the-set.md"):
        prepare_publication(spec)
    assert not retained.exists()

    candidate.write_text(content)
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
    assert not (tmp_path / agentic_set.retained_overview_path(RUN_ID)).parent.exists()
    assert state.read_bytes() == original_state
    assert spec.generated_candidate_path.exists()

    # A retry with the same run ID succeeds once the failure is gone.
    monkeypatch.setattr(agentic_publication, "atomic_write", real_atomic_write)
    publish_publication(spec)
    assert frontmatter(state)["run-status"] == "complete"



def test_published_set_feeds_the_comparison_matrix(tmp_path, monkeypatch):
    """A set published through the workflow loads and builds the matrix without edits."""
    import csv
    import io

    from scripts import build_systems_matrix

    state, spec, _ = publication_fixture(tmp_path)
    prepare_publication(spec)
    published = publish_publication(spec)
    assert validation.validate_note(state, repo_root=tmp_path).fails == []

    inputs = systems_matrix.load_results(tmp_path)
    assert [row["analysis_run"] for row in inputs.rows] == [RUN_ID]
    assert inputs.rows[0]["artifact_sha256"] == digest(tmp_path / published.retained_path)
    assert inputs.rows[0]["storage_substrate"] == ["files", "sqlite"]
    monkeypatch.setattr(build_systems_matrix, "REPO_ROOT", tmp_path)
    matrix = tmp_path / "kb/agentic-systems/comparisons/memory-systems.csv"
    assert build_systems_matrix.main(["--output", str(matrix)]) == 0
    assert list(csv.DictReader(io.StringIO(matrix.read_text()))) == [
        systems_matrix.csv_row(row) for row in inputs.rows
    ]


def test_comparison_tools_use_retained_results_without_local_or_legacy_inputs(tmp_path, monkeypatch):
    import csv
    import io

    from scripts import build_systems_matrix, render_systems_table

    state = valid_run_state(tmp_path)
    retained = tmp_path / agentic_set.retained_overview_path(RUN_ID)
    shutil.rmtree(tmp_path / "kb/agentic-systems/reports/state")
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
    ("source", "source-identity does not match"), ("revision", "identity mismatch"),
    ("missing", "no discovered file"), ("member", "manifest member memory.md: SHA-256 mismatch"),
])
def test_comparison_reader_rejects_incomplete_or_mismatched_evidence(tmp_path, mutation, error):
    valid_run_state(tmp_path)
    retained = tmp_path / agentic_set.retained_overview_path(RUN_ID)
    memory = retained.with_name("memory.md")
    review = tmp_path / "kb/agentic-systems/reviews/example-system.md"

    def repin_overview() -> None:
        repin(retained.parent)
        replace_frontmatter(review, {**frontmatter(review), "analysis-artifact-sha256": digest(retained.with_name("ARTIFACT.yaml"))})

    if mutation == "bytes":
        retained.write_bytes(retained.read_bytes() + b"drift\n")
    elif mutation == "missing":
        retained.unlink()
    elif mutation == "member":
        memory.write_bytes(memory.read_bytes() + b"drift\n")
    elif mutation == "profile":
        data = frontmatter(memory)
        data.pop("memory-comparison")
        replace_frontmatter(memory, data)
        repin_overview()
    else:
        key = "source-identity" if mutation == "source" else "reviewed-revision"
        value = "https://example.invalid/example-system-other" if mutation == "source" else "other"
        replace_frontmatter(review, {**frontmatter(review), key: value})
    with pytest.raises((ValueError, OSError), match=error):
        systems_matrix.load_results(tmp_path)


@pytest.mark.parametrize("mutation, error", [
    ("none", None),
    ("finalized-from", "finalized-from"),
])
def test_memory_member_contract(tmp_path: Path, mutation: str, error: str | None) -> None:
    """The member is the specialist's report; it has no finalization field."""
    memory = member_fixture(tmp_path) / "output/memory.md"
    if mutation == "finalized-from":
        replace_frontmatter(memory, {**frontmatter(memory), "finalized-from": "a" * 64})
    fails = validation.validate_note(memory, repo_root=tmp_path).fails
    if error is None:
        assert fails == []
    else:
        assert any(error in failure for failure in fails), fails


@pytest.mark.parametrize("declared, amendment, error", [
    ("RT-CMP-1", None, "duplicate set declaration: RT-CMP-1"),
    ("MEM-CMP-1", "MEM-CMP-1 is superseded by RT-CMP-1", None),
    ("MEM-CMP-1", "MEM-CMP-1 is superseded by RT-CMP-9", "reconciliation.md: unresolved record RT-CMP-9"),
])
def test_a_duplicate_record_is_superseded_in_the_reconciliation(
    tmp_path: Path, declared: str, amendment: str | None, error: str | None
) -> None:
    """A lens record for a thing the runtime pass declared stays declared
    under its own ID; the reconciliation member supersedes it."""
    run_dir = member_fixture(tmp_path)
    memory = run_dir / "output/memory.md"
    memory.write_text(memory.read_text().replace(
        "### Components\n\nnone proposed.\n",
        f"### Components\n\n#### {declared} — Memory view of the component\n\nFrom SRC-1.\n",
    ))
    overview = run_dir / "output/overview.md"
    if amendment is not None:
        reconciliation = run_dir / "output/reconciliation.md"
        reconciliation.write_text(reconciliation.read_text() +
            f"\nAmendment: {amendment}; both trace `README.md` at SRC-1.\n")
        overview.write_text(overview.read_text().replace(
            amendment_index(""), amendment_index(reconciliation.read_text()),
        ))
    repin(overview.parent)

    fails = validation.ValidationRun(tmp_path, ()).validate(overview.parent).fails

    if error is None:
        assert fails == []
    else:
        assert any(error in failure for failure in fails), fails


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
    target = f"kb/agentic-systems/reports/state/{RUN_ID}/output"

    assert main([target, "--json"]) == 0
    report = json.loads(capsys.readouterr().out)
    assert [artifact["path"] for artifact in report["analysed_artifacts"]] == [target]
    assert report["analysed_artifacts"][0]["type"] == agentic_set.SET_TYPE
    assert main([target, "--full"]) == 0


def test_comparison_reader_loads_what_publication_accepts(tmp_path):
    """Run-state and comparison readers reject the same duplicate set declaration."""
    state = valid_run_state(tmp_path)
    run_dir = state.parent
    memory = run_dir / "output/memory.md"
    # The memory member re-declares a record the runtime member declares.
    text = memory.read_text()
    assert "#### On RT-RTE-1 — Fixture route" in text
    route = (run_dir / "output/runtime.md").read_text().split(
        "#### RT-RTE-1 — Fixture route\n\n", 1
    )[1].split("\n### Claims", 1)[0]
    memory.write_text(text.replace(
        "#### On RT-RTE-1 — Fixture route", "#### RT-RTE-1 — Fixture route"
    ).replace("Seeded route with the specialist's memory fields.", route))
    overview = run_dir / "output/overview.md"
    repin(overview.parent)
    retain_set(tmp_path, run_dir)
    review = tmp_path / REVIEW_PATH
    replace_frontmatter(review, {**frontmatter(review), "analysis-artifact-sha256": digest(overview.with_name("ARTIFACT.yaml"))})
    values = frontmatter(state)
    values["artifact"]["sha256"] = digest(overview.with_name("ARTIFACT.yaml"))
    values["generated-review"]["sha256"] = digest(review)
    replace_frontmatter(state, values)
    assert any("duplicate set declaration: RT-RTE-1" in error
               for error in validation.validate_note(state, repo_root=tmp_path).fails)
    with pytest.raises(ValueError, match="duplicate set declaration: RT-RTE-1"):
        systems_matrix.load_results(tmp_path)


def test_comparison_population_must_select_one_review_per_source(tmp_path):
    valid_run_state(tmp_path)
    review = tmp_path / "kb/agentic-systems/reviews/example-system.md"
    second = review.with_name("second.md")
    second.write_bytes(review.read_bytes())
    with pytest.raises(ValueError, match="multiple selected reviews"):
        systems_matrix.load_results(tmp_path)
    assert len(systems_matrix.load_results(tmp_path, [review]).rows) == 1


def test_publication_requires_comparison_fields_and_preserves_retained_bytes(tmp_path):
    state, spec, _ = publication_fixture(tmp_path)
    memory = state.parent / "output/memory.md"
    old_bytes = {name: (output_path(state.parent, name)).read_bytes() for name in ("memory.md", "overview.md")}
    data = frontmatter(memory)
    data.pop("memory-comparison")
    replace_frontmatter(memory, data)
    with pytest.raises(ValueError, match="manifest member memory.md: SHA-256 mismatch"):
        prepare_publication(spec)
    overview = state.parent / "output/overview.md"
    repin(overview.parent)
    with pytest.raises(ValueError, match="memory-comparison"):
        prepare_publication(spec)
    for name, content in old_bytes.items():
        (output_path(state.parent, name)).write_bytes(content)
    repin(state.parent / "output")
    retained = write(tmp_path / agentic_set.retained_overview_path(RUN_ID), "frozen earlier overview\n")
    with pytest.raises(ValueError, match="already exists"):
        prepare_publication(spec)
    assert retained.read_text() == "frozen earlier overview\n"
    assert frontmatter(state)["run-status"] == "running"


@pytest.mark.parametrize("tier,basis,expected_rows,expected_fill", [
    ("code-grounded", "wired", 1, "100%"),
    ("code-grounded", "claimed", 1, "0%"),
    ("doc-grounded", "wired", 0, "0%"),
])
def test_statistics_keep_evidence_tiers_and_weaker_bases_separate(tmp_path, monkeypatch, capsys, tier, basis, expected_rows, expected_fill):
    from scripts import analyze_matrix

    valid_run_state(tmp_path)
    retained = tmp_path / agentic_set.retained_overview_path(RUN_ID)
    memory = retained.with_name("memory.md")
    profile = frontmatter(memory)
    for support in profile["memory-comparison"]["axes"]["storage_substrate"]["evidence"].values():
        support["basis"] = basis
    replace_frontmatter(memory, profile)
    data = frontmatter(retained)
    data["evidence-tier"] = tier
    replace_frontmatter(retained, data)
    repin(retained.parent)
    review = tmp_path / "kb/agentic-systems/reviews/example-system.md"
    replace_frontmatter(review, {**frontmatter(review), "analysis-artifact-sha256": digest(retained.with_name("ARTIFACT.yaml"))})
    monkeypatch.setattr(analyze_matrix, "REPO_ROOT", tmp_path)
    assert analyze_matrix.main([]) == 0
    output = capsys.readouterr().out
    assert f"code-grounded rows: {expected_rows}" in output
    complete = 1 if expected_fill == "100%" else 0
    assert f"complete storage_substrate: {complete} of {expected_rows} rows" in output
    if expected_rows:
        assert f"known:{basis}" in output


def rerun_publication_fixture(tmp_path: Path) -> tuple[PublicationSpec, bytes, bytes]:
    """Create a second run over a real, uncommitted first publication."""
    from commonplace.lib.agentic_publication import inspect_destination

    state, first, _ = publication_fixture(tmp_path)
    publish_publication(first)
    old_review = (tmp_path / first.generated_destination).read_bytes()
    old_set = {name: (output_path(state.parent, name)).read_bytes() for name in ("ARTIFACT.yaml", "overview.md", *MEMBER_TYPES)}
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
    candidate = new_dir / "review-candidate.md"
    candidate.write_text(old_review.decode().replace(RUN_ID, next_id))
    replace_frontmatter(candidate, {**frontmatter(candidate), "analysis-artifact-sha256": digest(new_dir / "output/ARTIFACT.yaml")})
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
    assert (spec.run_state_path.parent / "incumbent-review.md").read_bytes() == old_review
    for name, content in old_set.items():
        assert (spec.run_state_path.parent / f"incumbent-{name}").read_bytes() == content
    assert validation.validate_note(spec.run_state_path, repo_root=tmp_path).fails == []


@pytest.mark.parametrize("mutation, error", [
    ("missing-overview", "cannot read incumbent retained manifest"),
    ("overview", "manifest hash mismatch"),
    ("member", "manifest member runtime.md: SHA-256 mismatch"),
    ("source", "same source"),
    ("committed-then-staged", "local changes"),
])
def test_inspection_rejects_unverified_incumbents(tmp_path: Path, mutation: str, error: str) -> None:
    """An incumbent is checked by its bytes and pins; no publication receipt is read."""
    from commonplace.lib.agentic_publication import inspect_destination
    spec, _, _ = rerun_publication_fixture(tmp_path)
    review = tmp_path / spec.generated_destination
    metadata = frontmatter(review)
    retained = tmp_path / metadata["analysis-artifact"]
    if mutation == "missing-overview":
        retained.unlink()
    elif mutation == "overview":
        retained.write_text(retained.read_text() + "\nAltered evidence.\n")
    elif mutation == "member":
        member = retained.with_name("runtime.md")
        member.write_text(member.read_text() + "\nAltered evidence.\n")
    elif mutation == "source":
        replace_frontmatter(review, {**metadata, "source-identity": "other"})
    else:
        commit_paths(tmp_path, "Record the first publication", review, retained.parent)
        review.write_text(review.read_text() + "\nHuman correction.\n")
        run_git(tmp_path, "add", "--", str(review))
    before = review.read_bytes()
    with pytest.raises(ValueError, match=error):
        inspect_destination(repo_root=tmp_path, generated_destination=spec.generated_destination,
                            source_identity=metadata["source-identity"])
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
    with pytest.raises(ValueError, match="changed since inspection"):
        publish_publication(spec)
    assert path.read_bytes() == changed
    assert frontmatter(spec.run_state_path)["run-status"] == "running"


def test_rerun_rollback_preserves_concurrent_incumbent_edit(tmp_path: Path, monkeypatch) -> None:
    from commonplace.lib import agentic_publication as publication
    spec, _, _ = rerun_publication_fixture(tmp_path)
    original_write = publication.atomic_write
    public = tmp_path / spec.generated_destination
    changed = public.read_bytes() + b"\nConcurrent human edit.\n"

    def edit_after_backup(path, content):
        original_write(path, content)
        if path.name == "incumbent-review.md":
            public.write_bytes(changed)

    monkeypatch.setattr(publication, "atomic_write", edit_after_backup)
    with pytest.raises(ValueError, match="changed before replacement"):
        publish_publication(spec)
    assert public.read_bytes() == changed
    assert frontmatter(spec.run_state_path)["run-status"] == "running"
    assert not (tmp_path / agentic_set.retained_overview_path(RUN_ID[:-2] + "02")).exists()


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
    for name, retained in agentic_set.retained_set_paths(RUN_ID).items():
        assert (tmp_path / retained).read_bytes() == old_set[name]
    assert frontmatter(spec.run_state_path)["run-status"] == "running"
    assert spec.generated_candidate_path.exists()
    assert not (tmp_path / agentic_set.retained_overview_path(RUN_ID[:-2] + "02")).parent.exists()


def test_rerun_never_overwrites_a_conflicting_recovery_copy(tmp_path: Path) -> None:
    spec, old_review, _ = rerun_publication_fixture(tmp_path)
    backup = spec.run_state_path.parent / "incumbent-review.md"
    backup.write_bytes(b"Other recovery evidence.\n")
    with pytest.raises(ValueError, match="recovery copy already contains different bytes"):
        publish_publication(spec)
    assert backup.read_bytes() == b"Other recovery evidence.\n"
    assert (tmp_path / spec.generated_destination).read_bytes() == old_review


@pytest.mark.parametrize("path, accepted", [
    ("kb/notes/draft.md", False),
    ("kb/notes/zażółć gęślą.md", False),
    ("kb/agentic-systems/reviews/sibling.md", True),
    ("kb/agentic-systems/reports/retained/AAS-2026-09-04-sibling-01/overview.md", True),
    ("scratch.txt", True),
])
def test_untracked_files_block_publication_only_under_kb_outside_its_outputs(
    tmp_path: Path, path: str, accepted: bool
) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    write(tmp_path / path, "A sibling run's publication, or a stray file.\n")
    if accepted:
        inspect(tmp_path, spec)
        prepare_publication(spec)
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
    sibling = write(tmp_path / "kb/agentic-systems/reviews/sibling.md", "# Sibling\n")
    commit_paths(tmp_path, "Record the sibling's earlier review", sibling)
    sibling.write_text("# Sibling, replaced by a later run\n")
    inspect(tmp_path, spec)
    publish_publication(spec)
    assert frontmatter(state)["run-status"] == "complete"


@pytest.mark.parametrize("method_path", [
    "kb/agentic-systems/COLLECTION.md",
    "kb/agentic-systems/instructions/agentic-analysis-boundary.md",
    "kb/agentic-systems/instructions/agentic-analysis-sources.md",
    "kb/agentic-systems/instructions/agentic-analysis-records.md",
    "kb/agentic-systems/types/agentic-system-analysis-overview.md",
    "kb/agentic-systems/types/agentic-system-analysis-set.md",
    "kb/agentic-systems/types/agentic-system-analysis-set.schema.yaml",
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


def test_member_validation_accepts_s3_title_and_prose_references(tmp_path: Path) -> None:
    runtime = member_fixture(tmp_path) / "output/runtime.md"
    runtime.write_text(runtime.read_text().replace(
        "#### RT-RTE-1 — Fixture route",
        "#### RT-RTE-1 — S3 invocation\n\nRT-RTE-1 reads the bucket.",
    ))
    checked = validation.validate_note(runtime, repo_root=tmp_path)
    assert checked.fails == []


@pytest.mark.parametrize("anchor", [
    "`src/agent.py:120-140`",
    "`README.md:1`",
    "[run](https://github.com/example/system/blob/" + "a" * 40 + "/run.py#L3-L9)",
])
def test_member_validation_rejects_ranged_prose_anchors(tmp_path: Path, anchor: str) -> None:
    runtime = member_fixture(tmp_path) / "output/runtime.md"
    runtime.write_text(runtime.read_text() + f"\nEvidence: {anchor}.\n")
    checked = validation.validate_note(runtime, repo_root=tmp_path)
    assert any(
        "carries a line range" in item and "cite the path without a range, or quote the passage" in item
        for item in checked.fails
    )


def test_member_validation_keeps_ranges_in_quote_attributions(tmp_path: Path) -> None:
    runtime = member_fixture(tmp_path) / "output/runtime.md"
    revision = frontmatter(runtime)["reviewed-boundary"]
    runtime.write_text(
        runtime.read_text()
        + f"\n> Frozen source\n> --- `README.md:1-1` @ `{revision}`\n"
        + f"\n> See `other.py:4-8`\n> --- https://github.com/example/system/blob/{revision}/README.md#L1\n"
        + "\n```text\nexample `fenced.py:1-2`\n```\n"
    )
    checked = validation.validate_note(runtime, repo_root=tmp_path)
    assert checked.fails == []


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


def test_git_source_example_can_initialize_running_state(tmp_path: Path) -> None:
    state, _, _ = publication_fixture(tmp_path)
    values = frontmatter(state)
    actual = values["source"]
    contract = (REPO_ROOT / "kb/agentic-systems/types/agentic-system-analysis-run-state.md").read_text()
    example = yaml.safe_load(re.search(r"```yaml\n(source:.*?)```", contract, re.DOTALL)[1])["source"]
    example.update({key: actual[key] for key in ("identity", "revision", "path")})
    replace_frontmatter(state, {**values, "source": example})
    assert validation.validate_note(state, repo_root=tmp_path).fails == []


def test_quoted_code_must_occur_inside_the_cited_range(tmp_path: Path) -> None:
    from commonplace.lib.agentic_analysis import SourceIdentity, verify_quote_anchors

    root, _ = git_checkout(tmp_path / "source")
    source = write(root / "operation.py", "# Navigation heading\n\ndef apply():\n    rebuild_prompt()\n")
    commit_incumbent(root, source)
    revision = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    identity = SourceIdentity("git", "https://github.com/example/system", revision, root, None)
    quote = f"> rebuild_prompt()\n> --- [operation](https://github.com/example/system/blob/{revision}/operation.py#L1)\n"
    _, errors = verify_quote_anchors(quote, source=identity)
    assert any("cited line range" in error for error in errors)
    _, errors = verify_quote_anchors(quote.replace("#L1", "#L4"), source=identity)
    assert errors == []
    source.write_text("rebuild_prompt_WRONG()\n")
    _, errors = verify_quote_anchors(quote.replace("rebuild_prompt()", "rebuild_prompt_WRONG()"), source=identity)
    assert any("quote does not occur" in error for error in errors)


def test_quote_generation_needs_no_report_or_publication(tmp_path, capsys):
    state, spec, _ = publication_fixture(tmp_path)
    for name in ("overview.md", *MEMBER_TYPES):
        (output_path(state.parent, name)).unlink()
    spec.generated_candidate_path.unlink()
    text = write(tmp_path / "selection.txt", "Frozen source")
    before = {p: p.read_bytes() for p in state.parent.iterdir() if p.is_file()}
    assert quote.main([
        str(state), "--source-path", "README.md", "--text-file", str(text),
    ], cwd=tmp_path) == 0
    output = capsys.readouterr().out
    revision = frontmatter(state)["source"]["revision"]
    assert output == f"> Frozen source\n> --- `README.md:1-1` @ `{revision}`\n"
    assert before == {p: p.read_bytes() for p in state.parent.iterdir() if p.is_file()}
    assert frontmatter(state)["run-status"] == "running"
    assert not (tmp_path / spec.generated_destination).exists()


@pytest.mark.parametrize("count", [10, 11])
def test_quote_cli_emits_candidates_or_requests_longer_selection(tmp_path, capsys, count):
    state, _, _ = publication_fixture(tmp_path)
    snapshot = write(tmp_path / "capture.md", "repeated phrase\n" * count)
    values = frontmatter(state)
    values["source"] = {
        "kind": "capture", "identity": "https://example.com/source",
        "revision": "capture", "path": str(snapshot), "sha256": digest(snapshot),
    }
    replace_frontmatter(state, values)
    selection = write(tmp_path / "selection.txt", "repeated phrase")
    status = quote.main([str(state), "--text-file", str(selection)], cwd=tmp_path)
    output = capsys.readouterr()
    if count == 10:
        assert status == 0 and not output.err
        assert len(json.loads(output.out)["occurrences"]) == 10
    else:
        assert status == 1 and not output.out
        assert "more than 10 occurrences; choose a longer quote" in output.err


def test_quote_cli_resolves_a_selection_list_in_one_call(tmp_path, capsys):
    state, _, _ = publication_fixture(tmp_path)
    root = Path(frontmatter(state)["source"]["path"])
    revision = frontmatter(state)["source"]["revision"]
    selections = write(tmp_path / "selections.json", json.dumps([
        {"key": "readme", "source_path": "README.md", "text": "Frozen source"},
        {"key": "absent", "source_path": "README.md", "text": "not in source"},
        {"key": "nofile", "source_path": "missing.md", "text": "Frozen source"},
    ]))
    status = quote.main([str(state), "--selections", str(selections)], cwd=tmp_path)
    output = capsys.readouterr()
    assert status == 2
    results = json.loads(output.out)
    assert results["readme"] == {
        "status": "citation",
        "citation": f"> Frozen source\n> --- `README.md:1-1` @ `{revision}`\n",
    }
    assert results["absent"]["status"] == "error"
    assert results["nofile"]["status"] == "error"
    assert "2 of 3 selections need attention: absent (error), nofile (error)" in output.err
    assert root.exists()

    single = write(tmp_path / "single.json", json.dumps(
        [{"key": "readme", "source_path": "README.md", "text": "Frozen source"}]
    ))
    assert quote.main([str(state), "--selections", str(single)], cwd=tmp_path) == 0
    output = capsys.readouterr()
    assert not output.err
    assert json.loads(output.out)["readme"]["status"] == "citation"


def test_quote_cli_rejects_mixed_selection_and_single_arguments(tmp_path, capsys):
    with pytest.raises(SystemExit):
        quote.main(
            ["run-state.md", "--selections", "selections.json", "--source-path", "README.md"],
            cwd=tmp_path,
        )
    assert "--selections replaces --source-path" in capsys.readouterr().err


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
    from commonplace.lib.quote_generation import generate_quotes

    source = frontmatter(state)["source"]
    identity = SourceIdentity("git", source["identity"], source["revision"], Path(source["path"]), None)
    # The worktree must not supply either the selected text or its locations.
    write(identity.path / "README.md", "uncommitted replacement\n")
    runtime = state.parent / "output/runtime.md"
    for text in [*source_text.splitlines()[1:4], "* repeated comment"]:
        payload = generate_quotes(text, source=identity, source_path="README.md")
        if text == "* repeated comment":
            assert [entry["start_line"] for entry in payload["occurrences"]] == [5, 6]
        citation = payload if isinstance(payload, str) else payload["occurrences"][-1]["citation"]
        runtime.write_text(runtime.read_text() + "\n" + citation)
    repin(state.parent / "output")
    replace_frontmatter(spec.generated_candidate_path, {
        **frontmatter(spec.generated_candidate_path),
        "analysis-artifact-sha256": digest(state.parent / "output/ARTIFACT.yaml"),
    })
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


def test_adjacent_attributed_quotes_are_checked_independently(tmp_path):
    from commonplace.lib.agentic_analysis import SourceIdentity, verify_quote_anchors

    root, revision = git_checkout(tmp_path / "source")
    identity = SourceIdentity("git", "https://github.com/example/system", revision, root, None)
    text = f"""Inline `>` and `> ---` are ordinary prose.
> # Frozen source
> --- `README.md` @ `{revision}`
> Frozen source
> --- `README.md` @ `{revision}`
"""
    checks, errors = verify_quote_anchors(text, source=identity)
    assert len(checks) == 2
    assert errors == []
    _, errors = verify_quote_anchors(text.replace("> Frozen source", "> fabricated text"), source=identity)
    assert len(errors) == 1
    assert "quote does not occur" in errors[0]


def test_run_directory_traversal_reuses_member_checks(tmp_path, monkeypatch):
    from collections import Counter

    from commonplace.lib.project_paths import list_directory_validation_paths

    state = valid_run_state(tmp_path)
    calls = Counter()
    original = validation._validate_parsed_note
    def checked(parsed, *, run):
        calls[parsed.path] += 1
        return original(parsed, run=run)
    monkeypatch.setattr(validation, "_validate_parsed_note", checked)
    paths = tuple(list_directory_validation_paths(state.parent))
    outcome = validation.ValidationRun(tmp_path, paths).evaluate()
    assert not [error for result in outcome.results.values() for error in result.fails]
    assert state.parent / "output" in outcome.results
    for name in agentic_set.SET_NAMES:
        member = state.parent / "output" / name
        assert member not in outcome.results
        assert calls[member] == 1


@pytest.mark.parametrize("disposition", ["blocked", "out-of-scope"])
def test_noncomplete_artifact_cannot_publish_or_supply_comparison(tmp_path, disposition):
    state, spec, _ = publication_fixture(tmp_path)
    directory = state.parent / "output"
    overview = directory / "overview.md"
    values = frontmatter(overview)
    values["result-disposition"] = disposition
    replace_frontmatter(overview, values)
    overview.write_text(re.sub(r"(?m)^Amended or superseded records:.*\n", "",
        re.sub(r"(?:MEM-)?(?:OBJ|RTE|CMP|CLM|ABS|BAP)-\d+", "not evaluated", overview.read_text())))
    for name in MEMBER_TYPES:
        (directory / name).unlink()
    repin(directory)
    assert not validation.ValidationRun(tmp_path, ()).validate(directory).fails
    with pytest.raises(ValueError, match="requires a complete"):
        prepare_publication(spec)
    retained = tmp_path / agentic_set.retained_artifact_path(RUN_ID).parent
    shutil.copytree(directory, retained)
    review = tmp_path / REVIEW_PATH
    write(review, review_text(values["reviewed-boundary"], overview))
    with pytest.raises(ValueError, match="not a complete"):
        systems_matrix.load_results(tmp_path)


def test_quote_accepts_an_absolute_run_state_path_from_another_directory(
    tmp_path: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    from commonplace.cli.quote import main as quote_main

    state = valid_run_state(tmp_path)
    elsewhere = tmp_path / "elsewhere"
    elsewhere.mkdir()
    selection = write(elsewhere / "selection.txt", "# Frozen source\n")

    status = quote_main(
        [str(state.resolve()), "--text-file", "selection.txt"], cwd=elsewhere
    )

    # The location check passes; this fixture's state is complete, so the
    # command stops at the next check instead.
    assert status == 1
    assert selection.exists()
    error = capsys.readouterr().err
    assert "run-state path" not in error
    assert "requires a running run" in error


def test_run_state_repo_root_is_the_repository(tmp_path: Path) -> None:
    from commonplace.lib.agentic_analysis import run_state_repo_root

    state = tmp_path / STATE_DIR / RUN_ID / "run-state.md"

    assert run_state_repo_root(state) == tmp_path
    assert run_state_repo_root(tmp_path / "elsewhere" / "run-state.md") is None
