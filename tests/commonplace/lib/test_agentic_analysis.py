from __future__ import annotations

import json
import re
import shlex
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

pytestmark = pytest.mark.usefixtures("tmp_library")

REPO_ROOT = Path(__file__).resolve().parents[3]
RUN_ID = "AAS-2026-09-04-example-system-01"
SOURCE = "https://example.invalid/example-system"
STATE_DIR = Path("kb/reports/state/agentic-system-analysis")
REVIEW_PATH = "kb/agentic-systems/reviews/example-system.md"
# The fixture set's Reconciliation mapping: the specialist's one proposal.
MAPPING = {"MEM-OBJ-1": "OBJ-2"}
# A placeholder method commit for fixtures that never publish; publication
# fixtures pin the fixture repository's real HEAD.
INPUTS_COMMIT = "f" * 40
MEMBER_TYPES = {
    "runtime.md": "types/agentic-system-runtime-report.md",
    "memory.md": "types/agent-memory-analysis-report.md",
    "epistemic.md": "types/agentic-system-epistemic-report.md",
}


def write(path: Path, content: str) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return path


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def configure_types(tmp_path: Path) -> None:
    shutil.copytree(REPO_ROOT / "kb/types", tmp_path / "kb/types")
    shutil.copytree(
        REPO_ROOT / "kb/agent-memory-systems/types",
        tmp_path / "kb/agent-memory-systems/types",
    )
    shutil.copytree(
        REPO_ROOT / "kb/agentic-systems/types",
        tmp_path / "kb/agentic-systems/types",
    )
    write(tmp_path / "kb/reports/COLLECTION.md", "# Reports\n")
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
    """The specialist's local report: one proposal, one re-declared seed, one quote."""
    handoff = write(
        run_dir / "memory-input.md",
        "# Frozen memory input\n\nOBJ-1 fixture object. RTE-1 fixture route.\n",
    )
    profile = uninspected_profile("The fixture's accumulated project memory and retrieval routes")
    profile["axes"]["storage_substrate"] = {
        "assessment": "known", "values": ["sqlite", "files"],
        "evidence": {v: {"basis": "wired", "records": ["MEM-OBJ-1"], "note": "Fixture witness."}
                     for v in ["sqlite", "files"]},
        "records": ["MEM-OBJ-1"], "note": "Both stores occur within the fixture boundary.",
    }
    values = {
        "type": "types/agent-memory-analysis-report.md",
        "description": "Fixture specialist report bound to the frozen source and shared input",
        "analysis-run": RUN_ID,
        "source-identity": SOURCE,
        "reviewed-boundary": revision,
        "report-status": "complete",
        "canonical-register-sha256": digest(handoff),
        "worker-model": "fixture-model",
        "method-sha256": "a" * 64,
        "finalized-from": None,
        "memory-comparison": profile,
    }
    body = f"""# Fixture memory analysis

## Boundary and evidence

Fixture evidence at `README.md:1`.

## Core ideas

Fixture finding.

> # Frozen source
> --- `README.md` @ `{revision}`

## Shared records

### Components

none proposed.

### Operative objects

#### MEM-OBJ-1 — Fixture memory store

Proposed store, from SRC-1.

### Routes

#### RTE-1 — Fixture route

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

Fixture evidence on RTE-1.

## Comparison rationale

Both stores are MEM-OBJ-1.

## Integration issues

none

## Limitations and checks

Fixture evidence.
"""
    return write(
        run_dir / "memory-report.md",
        "---\n" + yaml.safe_dump(values, sort_keys=False) + "---\n\n" + body,
    )


def finalized_member_text(local: Path, mapping: dict[str, str] = MAPPING) -> str:
    """The coordinator's finalization, written out by hand for the fixture.

    Exact-token mapping of proposal IDs, the re-declared seed turned into an
    annotation heading, ``finalized-from`` set, and an Amendments section.
    """
    text = local.read_text(encoding="utf-8")
    for proposal, canonical in mapping.items():
        text = re.sub(rf"(?<![\w-]){re.escape(proposal)}(?![\w-])", canonical, text)
    text = text.replace("#### RTE-1 — Fixture route", "#### On RTE-1 — Fixture route")
    document, error = validation.parse_document(text)
    assert error is None and document is not None and document.frontmatter is not None
    values = {**document.frontmatter, "finalized-from": digest(local)}
    return (
        "---\n" + yaml.safe_dump(values, sort_keys=False) + "---\n"
        + document.body.rstrip("\n") + "\n\n## Amendments\n\nnone\n"
    )


def runtime_text(revision: str) -> str:
    return f"""---
type: types/agentic-system-runtime-report.md
description: "Runtime baseline of Example System at the fixture boundary"
run-id: {RUN_ID}
reviewed-boundary: {revision}
---

# Example System runtime report

## Runtime account

No dynamic check planned; static evidence at `README.md:1` sufficed.

## Probe evidence

none

## Shared records

### Components

#### CMP-1 — Fixture component

Record. Evidence: SRC-1.

### Operative objects

#### OBJ-1 — Fixture object

Record. Evidence: SRC-1.

### Routes

#### RTE-1 — Fixture route

Record. Evidence: SRC-1.

### Claims

#### CLM-1 — Fixture claim

Record. Evidence: SRC-1.

### Evidenced absences

none found within the fixture boundary.

### Behavioral-authority paths

#### BAP-1 — Fixture authority path

Record. Evidence: SRC-1.

## Annotations

none
"""


def epistemic_text(revision: str) -> str:
    return f"""---
type: types/agentic-system-epistemic-report.md
description: "Epistemic routes of Example System at the fixture boundary"
run-id: {RUN_ID}
reviewed-boundary: {revision}
---

# Example System epistemic report

## Source-and-claim boundary

Boundary from the overview's Source register.

## Epistemic-object inventory

OBJ-1 and OBJ-2 carry no candidate truth-apt content.

## Authority-route ledger

RTE-1: no content change.

## Per-object lifecycle disposition

No candidate lifecycle records: no candidate truth-apt output found within the source boundary.

## System-claim versus route comparison

CLM-1 is compared with RTE-1.

## Bounded conclusion

Conclusion.
"""


def overview_text(
    revision: str, members: dict[str, Path], *, inputs_commit: str = INPUTS_COMMIT
) -> str:
    manifest = "\n".join(
        f"  - path: {name}\n    sha256: {digest(path)}\n    type: {MEMBER_TYPES[name]}"
        for name, path in members.items()
    )
    return f"""---
type: types/agentic-system-analysis-overview.md
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
members:
{manifest}
---

# Example System agentic-system analysis

## Run identity

**Run state:** `kb/reports/state/agentic-system-analysis/{RUN_ID}/run-state.md`

**Generated review:** `{REVIEW_PATH}`

## Boundary and evidence

Fixture boundary at `{revision}`.

## Source register

| SRC-1 | git | `{SOURCE}` | `{revision}` | implementation | README.md | `README.md:1` | none |

## Lens scoping

### Memory/context scope

Brief fixture scope.

### Epistemic scope

Brief fixture scope.

## Reconciliation

| specialist proposal | canonical record | disposition |
|---|---|---|
| MEM-OBJ-1 | OBJ-2 | registered |

Finalized from `memory-report.md`; no mechanical edits beyond the mapping.

## Bounded synthesis

Fixture synthesis over OBJ-1, OBJ-2 and RTE-1.

## Limitations

None.

## Verification and blockers

### Semantic verification

Passed.

### Deterministic validation

Passed.

### Blockers

None.
"""


def review_text(revision: str, overview: Path) -> str:
    return f"""---
description: "Generated fixture review of one external agentic system"
type: agentic-systems/types/generated-review.md
generated-by: analyse-agentic-system
analysis-run: {RUN_ID}
source-identity: {SOURCE}
reviewed-revision: {revision}
analysis-overview: {agentic_set.retained_overview_path(RUN_ID).as_posix()}
analysis-overview-sha256: {digest(overview)}
---

# Example System

Evidence basis: `README.md:1` at `{revision}`.
"""


def run_dir_of(tmp_path: Path, run_id: str = RUN_ID) -> Path:
    return tmp_path / STATE_DIR / run_id


def refinalize(run_dir: Path) -> None:
    """Rebuild memory.md from the local report and re-pin the overview manifest."""
    write(run_dir / "memory.md", finalized_member_text(run_dir / "memory-report.md"))
    overview = run_dir / "overview.md"
    values = frontmatter(overview)
    values["members"] = [
        {"path": name, "sha256": digest(run_dir / name), "type": MEMBER_TYPES[name]}
        for name in MEMBER_TYPES
    ]
    replace_frontmatter(overview, values)


def retain_set(tmp_path: Path, run_dir: Path, run_id: str = RUN_ID) -> None:
    for name, retained in agentic_set.retained_set_paths(run_id).items():
        (tmp_path / retained).parent.mkdir(parents=True, exist_ok=True)
        (tmp_path / retained).write_bytes((run_dir / name).read_bytes())


def valid_run_state(tmp_path: Path) -> Path:
    configure_types(tmp_path)
    run_dir = run_dir_of(tmp_path)
    source_root, revision = git_checkout(
        tmp_path / "related-systems/example--system"
    )
    local = memory_report_fixture(run_dir, revision)
    members = {
        "runtime.md": write(run_dir / "runtime.md", runtime_text(revision)),
        "memory.md": write(run_dir / "memory.md", finalized_member_text(local)),
        "epistemic.md": write(run_dir / "epistemic.md", epistemic_text(revision)),
    }
    overview = write(run_dir / "overview.md", overview_text(revision, members))
    retain_set(tmp_path, run_dir)
    generated = write(tmp_path / REVIEW_PATH, review_text(revision, overview))
    run_frontmatter: dict[str, object] = {
        "type": "types/agentic-system-analysis-run-state.md",
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
        "overview": {
            "path": (STATE_DIR / RUN_ID / "overview.md").as_posix(),
            "sha256": digest(overview),
        },
        "generated-review": {
            "path": REVIEW_PATH,
            "sha256": digest(generated),
        },
        "failure": None,
    }
    return write(run_dir / "run-state.md", state_text(run_frontmatter))


def sync_set(tmp_path: Path, values: dict) -> None:
    """Re-derive the member, manifest, retained copies and pins after an edit.

    The local report follows the state's source identity and boundary, as the
    specialist's handoff would; the review's pin follows the overview.
    """
    run_dir = tmp_path / Path(values["overview"]["path"]).parent
    report = run_dir / "memory-report.md"
    report_values = frontmatter(report)
    report_values.update({"source-identity": values["source"]["identity"],
                          "reviewed-boundary": values["source"]["revision"]})
    replace_frontmatter(report, report_values)
    refinalize(run_dir)
    retain_set(tmp_path, run_dir)
    values["overview"]["sha256"] = digest(run_dir / "overview.md")
    generated = tmp_path / values["generated-review"]["path"]
    replace_frontmatter(generated, {
        **frontmatter(generated), "analysis-overview-sha256": digest(run_dir / "overview.md"),
    })
    values["generated-review"]["sha256"] = digest(generated)


def rewrite_boundary(tmp_path: Path, run_dir: Path, old: str, new: str) -> None:
    """Move every set document, the local report and the review to another boundary."""
    for path in (*(run_dir / name for name in ("overview.md", *MEMBER_TYPES)),
                 run_dir / "memory-report.md", tmp_path / REVIEW_PATH):
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
    write(tmp_path / ".gitignore", "kb/reports/state/\nrelated-systems/\n")
    run_git(tmp_path, "init", "--quiet")
    return commit_paths(tmp_path, "Commit the run's inputs", ".")


def pin_inputs_commit(run_dir: Path, commit: str, candidate: Path | None = None) -> None:
    """Record the method commit in the overview and re-pin the candidate review to it."""
    overview = run_dir / "overview.md"
    replace_frontmatter(overview, {**frontmatter(overview), "inputs-commit": commit})
    if candidate is not None:
        replace_frontmatter(
            candidate, {**frontmatter(candidate), "analysis-overview-sha256": digest(overview)}
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
                   "overview": None, "generated-review": None, "failure": None})
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
    state = tmp_path / f"kb/reports/state/agentic-system-analysis/{RUN_ID}/run-state.md"
    values: dict[str, object] = {
        "type": "types/agentic-system-analysis-run-state.md",
        "description": f"Minimal completion state for {RUN_ID}",
        "run-id": RUN_ID,
        "system": "Example System",
        "run-status": "running",
        "result-disposition": None,
        "source": None,
        "overview": None,
        "generated-review": None,
        "failure": None,
    }
    write(state, state_text(values))

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []


def test_failed_state_requires_only_a_reason(tmp_path: Path) -> None:
    configure_types(tmp_path)
    state = tmp_path / f"kb/reports/state/agentic-system-analysis/{RUN_ID}/run-state.md"
    values: dict[str, object] = {
        "type": "types/agentic-system-analysis-run-state.md",
        "description": f"Failed run {RUN_ID}",
        "run-id": RUN_ID,
        "system": "Example System",
        "run-status": "failed",
        "result-disposition": None,
        "source": None,
        "overview": None,
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
            "overview": None,
            "generated-review": None,
            "failure": None,
        }
    )
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("failure" in item for item in results.fails)


def test_complete_state_rejects_changed_overview_bytes(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    overview = state.parent / "overview.md"
    overview.write_text(overview.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("overview: SHA-256 mismatch" in item for item in results.fails)


@pytest.mark.parametrize("member", ["runtime.md", "memory.md", "epistemic.md"])
def test_complete_state_rejects_a_member_that_drifted_from_the_manifest(
    tmp_path: Path, member: str
) -> None:
    state = valid_run_state(tmp_path)
    path = state.parent / member
    path.write_text(path.read_text(encoding="utf-8") + "changed\n", encoding="utf-8")

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any(f"member set: manifest: {member} bytes hash to" in item for item in results.fails)


def test_complete_state_rejects_invalid_overview_with_matching_hash(
    tmp_path: Path,
) -> None:
    state = valid_run_state(tmp_path)
    overview = state.parent / "overview.md"
    overview.write_text(
        overview.read_text(encoding="utf-8").replace("## Limitations\n\nNone.\n\n", ""),
        encoding="utf-8",
    )
    values = frontmatter(state)
    sync_set(tmp_path, values)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("overview validation" in item for item in results.fails)


@pytest.mark.parametrize("member", ["runtime.md", "memory.md", "epistemic.md"])
def test_complete_state_rejects_an_invalid_member_pinned_by_the_manifest(
    tmp_path: Path, member: str
) -> None:
    state = valid_run_state(tmp_path)
    path = state.parent / member
    heading = {"runtime.md": "## Annotations", "memory.md": "## Read-back",
               "epistemic.md": "## Bounded conclusion"}[member]
    path.write_text(path.read_text(encoding="utf-8").replace(heading, "## Renamed"), encoding="utf-8")
    if member == "memory.md":
        # Keep the derivation honest: the local report carries the same edit.
        local = state.parent / "memory-report.md"
        local.write_text(local.read_text(encoding="utf-8").replace(heading, "## Renamed"), encoding="utf-8")
    values = frontmatter(state)
    sync_set(tmp_path, values)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any(f"{member} validation" in item for item in results.fails)


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


def test_blocked_overview_completes_without_members_or_public_review(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    overview = state.parent / "overview.md"
    overview.write_text(
        overview.read_text(encoding="utf-8").replace(
            f"**Generated review:** `{REVIEW_PATH}`",
            "**Generated review:** not applicable",
        ),
        encoding="utf-8",
    )
    replace_frontmatter(overview, {
        **frontmatter(overview), "result-disposition": "blocked", "target-class": None,
        "boundary-kind": None, "reviewed-boundary": None, "analysis-cutoff": None,
        "evidence-tier": None, "members": [],
    })
    for name in MEMBER_TYPES:
        (state.parent / name).unlink()
    values.update(
        {
            "result-disposition": "blocked",
            "source": None,
            "overview": {"path": values["overview"]["path"], "sha256": digest(overview)},  # type: ignore[index]
            "generated-review": None,
        }
    )
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert results.fails == []


@pytest.mark.parametrize("mutation", [
    "stale-finalized-from", "runtime-run-id", "epistemic-boundary", "memory-source",
])
def test_complete_state_verifies_the_set_beyond_each_member(tmp_path: Path, mutation: str) -> None:
    state = valid_run_state(tmp_path)
    run_dir = state.parent
    values = frontmatter(state)
    sync_set(tmp_path, values)
    expected = {
        "stale-finalized-from": "finalized-from does not match memory-report.md bytes",
        "runtime-run-id": "member set: runtime.md: run-id does not match the overview",
        "epistemic-boundary": "member set: epistemic.md: reviewed-boundary does not match the overview",
        "memory-source": "member set: memory.md: source-identity does not match the frozen source",
    }[mutation]
    if mutation == "stale-finalized-from":
        report = run_dir / "memory-report.md"
        report.write_text(report.read_text() + "\nLater specialist edit.\n")
    elif mutation == "runtime-run-id":
        path = run_dir / "runtime.md"
        replace_frontmatter(path, {**frontmatter(path), "run-id": RUN_ID[:-2] + "09"})
    elif mutation == "epistemic-boundary":
        path = run_dir / "epistemic.md"
        replace_frontmatter(path, {**frontmatter(path), "reviewed-boundary": "0" * 40})
    else:
        path = run_dir / "memory.md"
        replace_frontmatter(path, {**frontmatter(path), "source-identity": "https://example.invalid/other"})
    # Re-pin the manifest and copies around the edit without regenerating the member.
    overview = run_dir / "overview.md"
    data = frontmatter(overview)
    data["members"] = [
        {"path": name, "sha256": digest(run_dir / name), "type": MEMBER_TYPES[name]}
        for name in MEMBER_TYPES
    ]
    replace_frontmatter(overview, data)
    retain_set(tmp_path, run_dir)
    values["overview"]["sha256"] = digest(overview)
    generated = tmp_path / REVIEW_PATH
    replace_frontmatter(generated, {**frontmatter(generated), "analysis-overview-sha256": digest(overview)})
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
    old_revision = frontmatter(state.parent / "overview.md")["reviewed-boundary"]
    rewrite_boundary(tmp_path, state.parent, old_revision, "capture-2026-09-04")
    report = state.parent / "memory-report.md"
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


def test_source_anchor_past_blob_end_is_rejected(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    runtime = state.parent / "runtime.md"
    runtime.write_text(
        runtime.read_text(encoding="utf-8") + "\nBad citation: `README.md:99`.\n",
        encoding="utf-8",
    )
    values = frontmatter(state)
    sync_set(tmp_path, values)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("runtime.md source citation" in item and "outside the recorded blob" in item
               for item in results.fails)


@pytest.mark.parametrize("output_role", ["overview", "generated-review"])
@pytest.mark.parametrize(
    ("citation", "expected_error"),
    [
        ("example/system/blob/{revision}/README.md#L1", None),
        ("EXAMPLE/System/blob/{revision}/README.md#L1-L1", None),
        ("example/system/blob/{revision}/README.md", None),
        ("unrelated/other/blob/{revision}/README.md#L1", "uses repository"),
        ("example/system/blob/main/README.md#L999", "uses revision"),
        ("example/system/blob/main/README.md", "uses revision"),
        ("example/system/blob/{short_revision}/README.md#L1", "uses revision"),
        ("example/system/blob/{wrong_revision}/README.md#L1", "uses revision"),
        ("example/system/blob/{revision}/missing.md#L1", "does not resolve to a blob"),
        ("example/system/blob/{revision}/README.md#L999", "outside the recorded blob"),
        ("example/system/blob/{revision}/README.md#L1oops", "invalid GitHub line anchor"),
        ("example/system/blob/{revision}", "incomplete GitHub blob path"),
    ],
)
def test_github_citations_match_the_frozen_source(
    tmp_path: Path, output_role: str, citation: str, expected_error: str | None
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

    output = tmp_path / values[output_role]["path"]
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


@pytest.mark.parametrize("output_role", ["overview", "generated-review"])
@pytest.mark.parametrize("citation_kind", ["local", "github"])
def test_quote_anchors_resolve_from_the_recorded_commit(
    tmp_path: Path, output_role: str, citation_kind: str
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
    output = tmp_path / values[output_role]["path"]
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


def test_quote_anchor_rejects_a_local_revision_mismatch(tmp_path: Path) -> None:
    state = valid_run_state(tmp_path)
    values = frontmatter(state)
    generated = tmp_path / values["generated-review"]["path"]
    with generated.open("a", encoding="utf-8") as handle:
        handle.write(
            "\n> # Frozen source\n"
            f"> --- `README.md` @ `{'0' * 40}`\n"
        )
    sync_set(tmp_path, values)
    replace_frontmatter(state, values)

    results = validation.validate_note(state, repo_root=tmp_path)

    assert any("attribution uses revision" in item for item in results.fails)


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
    assert "**Overview:**" in rendered
    assert "**Members:** runtime.md, memory.md, epistemic.md" in rendered
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
            "overview": None,
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


def test_prepare_checks_handoff_without_publishing(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    assert prepare_publication(spec).prepared
    assert not (tmp_path / spec.generated_destination).exists()
    assert frontmatter(state)["run-status"] == "running"


def test_prepare_validates_each_member_once_through_regular_bundle_validation(tmp_path, monkeypatch):
    state, spec, _ = publication_fixture(tmp_path)
    members = {state.parent / name for name in ("overview.md", *MEMBER_TYPES)}
    validate = validation._validate_parsed_note
    visits = []

    def track(parsed, *, run):
        if parsed.path in members:
            visits.append(parsed.path)
        return validate(parsed, run=run)

    monkeypatch.setattr(validation, "_validate_parsed_note", track)
    assert prepare_publication(spec).prepared
    assert sorted(visits) == sorted(members)


@pytest.mark.parametrize("mutation", ["valid", "annotated-seed", "vocabulary", "empty", "outside", "absence", "dependency"])
def test_standing_memory_report_comparison_validation(tmp_path: Path, mutation: str) -> None:
    state = valid_run_state(tmp_path)
    report = state.parent / "memory-report.md"
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
        report.write_text(report.read_text().replace("#### RTE-1 — Fixture route", "#### On RTE-1 — Fixture route"))
        axes["read_back_direction"] = {
            "assessment": "known", "values": ["pull"],
            "evidence": {"pull": {"basis": "wired", "records": ["RTE-1"], "note": "Seeded route."}},
            "records": ["RTE-1"], "note": "The annotated seed carries the route.",
        }
        axes["read_back_signal"]["assessment"] = "inapplicable"
    elif mutation == "vocabulary":
        axes["storage_substrate"]["values"] = ["invented"]
        expected_error = "off-vocabulary"
    elif mutation == "empty":
        axes["storage_substrate"]["values"] = []
        expected_error = "known assessment needs"
    elif mutation == "outside":
        report.write_text(report.read_text().replace(
            "#### MEM-OBJ-1 — Fixture memory store\n", "",
        ) + "\nMEM-OBJ-1 outside the register.\n")
        expected_error = "unresolved shared or proposed"
    elif mutation == "absence":
        axes["trace_learning"]["records"] = ["MEM-OBJ-1"]
        expected_error = "absence requires"
    elif mutation == "dependency":
        axes["trace_learning"].update({"assessment": "known", "values": ["no"], "evidence": {"no": {"basis": "wired", "records": ["MEM-ABS-1"], "note": "Fixture absence."}}})
        expected_error = "must be inapplicable"
    replace_frontmatter(report, metadata)
    checked = validation.validate_note(report, repo_root=tmp_path)
    if expected_error:
        assert any(expected_error in error for error in checked.fails)
    else:
        assert checked.fails == []
        assert any("shared or proposed references resolve" in message for message in checked.passes)
        document, error = validation.parse_document(report.read_text())
        assert error is None
        with pytest.raises(ValueError, match="unresolved canonical"):
            systems_matrix.validate_comparison(metadata["memory-comparison"], document.body)


@pytest.mark.parametrize("name", [
    "memory-report.md", "memory-input.md", "incumbent-review.md",
    "overview.md", "runtime.md", "memory.md", "epistemic.md",
    "incumbent-overview.md", "incumbent-memory.md",
])
def test_publication_cannot_consume_specialist_evidence_as_candidate(tmp_path: Path, name: str) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    with pytest.raises(ValueError, match="reserved"):
        prepare_publication(PublicationSpec(tmp_path, state, state.parent / name, spec.generated_destination, "absent"))


def test_publication_cli_rejects_retired_legacy_arguments(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    with pytest.raises(SystemExit) as error:
        agentic_analysis_publication.main([
            "prepare", str(state), "--generated-candidate", str(spec.generated_candidate_path),
            "--generated-destination", spec.generated_destination,
            "--legacy-candidate", "retired.md",
        ], cwd=tmp_path)
    assert error.value.code == 2


def test_memory_report_quote_is_checked_at_the_frozen_source(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    report = state.parent / "memory-report.md"
    revision = frontmatter(state)["source"]["revision"]
    report.write_text(report.read_text() + f"\n> absent quotation\n> --- `README.md` @ `{revision}`\n")
    refinalize(state.parent)
    with pytest.raises(ValueError, match="memory.md quote-anchored.*quote does not occur"):
        prepare_publication(spec)


def test_prepare_rejects_an_unresolved_quote_in_a_candidate(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    running_values = frontmatter(state)
    revision = running_values["source"]["revision"]
    with spec.generated_candidate_path.open("a", encoding="utf-8") as handle:
        handle.write(
            "\n> text absent from the source\n"
            f"> --- `README.md` @ `{revision}`\n"
        )

    with pytest.raises(ValueError, match="quote does not occur"):
        prepare_publication(spec)

    assert not (tmp_path / spec.generated_destination).exists()
    assert frontmatter(state)["run-status"] == "running"


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


def test_publish_rejects_a_source_mismatch_before_replacing_an_incumbent(
    tmp_path: Path,
) -> None:
    state, spec, generated_bytes = publication_fixture(tmp_path)
    prepare_publication(spec)
    incumbent = tmp_path / spec.generated_destination
    incumbent.parent.mkdir(parents=True, exist_ok=True)
    incumbent.write_bytes(generated_bytes)
    values = frontmatter(incumbent)
    values["source-identity"] = "https://example.invalid/example-system-other"
    replace_frontmatter(incumbent, values)
    old_bytes = incumbent.read_bytes()
    commit_incumbent(tmp_path, incumbent)

    with pytest.raises(ValueError, match="same source"):
        publish_publication(spec)

    assert incumbent.read_bytes() == old_bytes
    assert frontmatter(state)["run-status"] == "running"


@pytest.mark.parametrize("mutation", ["bytes", "input", "run", "source", "boundary", "blocked"])
def test_publication_requires_exact_completed_memory_handoff(tmp_path: Path, mutation: str) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    report = state.parent / "memory-report.md"
    if mutation == "bytes":
        report.write_text(report.read_text() + "\nChanged.\n")
    elif mutation == "input":
        (state.parent / "memory-input.md").write_text("Changed input.\n")
    else:
        values = frontmatter(report)
        field = {"run": "analysis-run", "source": "source-identity", "boundary": "reviewed-boundary", "blocked": "report-status"}[mutation]
        values[field] = "blocked" if mutation == "blocked" else "different"
        replace_frontmatter(report, values)
        refinalize(state.parent)
    with pytest.raises(ValueError, match="memory"):
        publish_publication(spec)
    assert not (tmp_path / spec.generated_destination).exists()
    assert frontmatter(state)["run-status"] == "running"


def test_publish_replaces_the_bundle_and_completes_run_state(tmp_path: Path) -> None:
    state, spec, generated_bytes = publication_fixture(tmp_path)
    prepare_publication(spec)

    published = publish_publication(spec)

    assert (tmp_path / spec.generated_destination).read_bytes() == generated_bytes
    assert not spec.generated_candidate_path.exists()
    values = frontmatter(state)
    assert values["run-status"] == "complete"
    assert values["overview"]["path"].endswith(f"{RUN_ID}/overview.md")
    assert (tmp_path / published.retained_path).read_bytes() == (state.parent / "overview.md").read_bytes()
    for name, retained in agentic_set.retained_set_paths(RUN_ID).items():
        assert (tmp_path / retained).read_bytes() == (state.parent / name).read_bytes()
    assert published.cleanup_warnings == ()
    assert validation.validate_note(state, repo_root=tmp_path).fails == []


def test_publication_resolves_links_to_results_in_the_same_bundle(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    retained = tmp_path / agentic_set.retained_overview_path(RUN_ID)
    candidate = spec.generated_candidate_path
    content = candidate.read_text() + (
        f"\n[Exact analysis](../../reports/retained/agentic-system-analysis/{RUN_ID}/overview.md)\n"
    )
    candidate.write_text(content)

    assert prepare_publication(spec).prepared
    assert not retained.exists()
    assert not (tmp_path / spec.generated_destination).exists()

    candidate.write_text(content + "\n[Missing](./not-in-the-bundle.md)\n")
    with pytest.raises(ValueError, match="missing target ./not-in-the-bundle.md"):
        prepare_publication(spec)
    assert not retained.exists()

    candidate.write_text(content)
    prepare_publication(spec)
    publish_publication(spec)
    assert retained.read_bytes() == (state.parent / "overview.md").read_bytes()
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
    real_atomic_write = agentic_publication._atomic_write

    def fail_on_state(path: Path, content: bytes) -> None:
        if path == failure_destination:
            raise OSError("injected write failure")
        real_atomic_write(path, content)

    monkeypatch.setattr(agentic_publication, "_atomic_write", fail_on_state)

    try:
        publish_publication(spec)
    except OSError as exc:
        assert "injected write failure" in str(exc)
    else:
        raise AssertionError("publication unexpectedly survived injected failure")

    assert not (tmp_path / spec.generated_destination).exists()
    assert not (tmp_path / agentic_set.retained_overview_path(RUN_ID)).exists()
    assert state.read_bytes() == original_state
    assert spec.generated_candidate_path.exists()



def test_comparison_tools_use_retained_results_without_local_or_legacy_inputs(tmp_path, monkeypatch, capsys):
    import csv
    import io

    from scripts import analyze_matrix, build_systems_matrix, render_systems_table

    state = valid_run_state(tmp_path)
    retained = tmp_path / agentic_set.retained_overview_path(RUN_ID)
    shutil.rmtree(tmp_path / "kb/reports/state")
    shutil.rmtree(tmp_path / "kb/agent-memory-systems")
    shutil.rmtree(tmp_path / "related-systems")
    assert not state.exists()
    write(tmp_path / "kb/agentic-systems/reviews/README.md", "# Ordinary navigation\n")
    inputs = systems_matrix.load_results(tmp_path)
    assert len(inputs.rows) == 1
    assert inputs.rows[0]["storage_substrate"] == '["files","sqlite"]'
    assert inputs.rows[0]["lineage_assessment"] == "uninspected"
    assert inputs.rows[0]["overview_sha256"] == digest(retained)
    for module in (analyze_matrix, build_systems_matrix, render_systems_table):
        monkeypatch.setattr(module, "REPO_ROOT", tmp_path)
    matrix = tmp_path / "kb/agentic-systems/comparisons/memory-systems.csv"
    table = matrix.with_suffix(".md")
    assert build_systems_matrix.main(["--output", str(matrix)]) == 0
    assert list(csv.DictReader(io.StringIO(matrix.read_text()))) == inputs.rows
    assert render_systems_table.main(["--output", str(table)]) == 0
    assert "files [wired], sqlite [wired]" in table.read_text()
    assert "## code-grounded (1)" in table.read_text()
    assert digest(retained) in table.read_text()
    assert validation.validate_note(table, repo_root=tmp_path).fails == []
    assert analyze_matrix.main([]) == 0
    output = capsys.readouterr().out
    line = next(line for line in output.splitlines() if line.startswith("storage_substrate "))
    assert line.split()[:3] == ["storage_substrate", "100%", "1"]
    assert "'uninspected':" in output
    assert "doc-grounded excluded from statistics: 0" in output


@pytest.mark.parametrize("mutation, error", [
    ("bytes", "SHA-256 mismatch"), ("profile", "memory-comparison"),
    ("source", "source identity missing"), ("revision", "identity mismatch"),
    ("missing", "No such file"), ("member", "manifest: memory.md bytes hash to"),
    ("declared-twice", "declared in more than one member"),
])
def test_comparison_reader_rejects_incomplete_or_mismatched_evidence(tmp_path, mutation, error):
    valid_run_state(tmp_path)
    retained = tmp_path / agentic_set.retained_overview_path(RUN_ID)
    memory = retained.with_name("memory.md")
    review = tmp_path / "kb/agentic-systems/reviews/example-system.md"

    def repin_overview() -> None:
        data = frontmatter(retained)
        data["members"] = [
            {"path": name, "sha256": digest(retained.with_name(name)), "type": MEMBER_TYPES[name]}
            for name in MEMBER_TYPES
        ]
        replace_frontmatter(retained, data)
        replace_frontmatter(review, {**frontmatter(review), "analysis-overview-sha256": digest(retained)})

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
    elif mutation == "declared-twice":
        memory.write_text(memory.read_text().replace("#### On RTE-1 — Fixture route", "#### RTE-1 — Fixture route"))
        repin_overview()
    else:
        key = "source-identity" if mutation == "source" else "reviewed-revision"
        value = "https://example.invalid/example-system-other" if mutation == "source" else "other"
        replace_frontmatter(review, {**frontmatter(review), key: value})
    with pytest.raises((ValueError, OSError), match=error):
        systems_matrix.load_results(tmp_path)


def test_comparison_population_must_select_one_review_per_source(tmp_path):
    valid_run_state(tmp_path)
    review = tmp_path / "kb/agentic-systems/reviews/example-system.md"
    second = review.with_name("second.md")
    second.write_bytes(review.read_bytes())
    with pytest.raises(ValueError, match="multiple selected reviews"):
        systems_matrix.load_results(tmp_path)
    assert len(systems_matrix.load_results(tmp_path, [review]).rows) == 1
    inputs = systems_matrix.load_results(tmp_path, [review])
    review.write_bytes(review.read_bytes() + b"changed\n")
    with pytest.raises(ValueError, match="input changed"):
        inputs.recheck(tmp_path)


def test_publication_requires_comparison_fields_and_preserves_retained_bytes(tmp_path):
    state, spec, _ = publication_fixture(tmp_path)
    memory = state.parent / "memory.md"
    old_bytes = {name: (state.parent / name).read_bytes() for name in ("memory.md", "overview.md")}
    data = frontmatter(memory)
    data.pop("memory-comparison")
    replace_frontmatter(memory, data)
    with pytest.raises(ValueError, match="manifest: memory.md bytes hash to"):
        prepare_publication(spec)
    overview = state.parent / "overview.md"
    values = frontmatter(overview)
    values["members"] = [
        {"path": name, "sha256": digest(state.parent / name), "type": MEMBER_TYPES[name]}
        for name in MEMBER_TYPES
    ]
    replace_frontmatter(overview, values)
    with pytest.raises(ValueError, match="memory-comparison"):
        prepare_publication(spec)
    for name, content in old_bytes.items():
        (state.parent / name).write_bytes(content)
    retained = write(tmp_path / agentic_set.retained_overview_path(RUN_ID), "frozen earlier overview\n")
    with pytest.raises(ValueError, match="already exists"):
        prepare_publication(spec)
    assert retained.read_text() == "frozen earlier overview\n"
    assert frontmatter(state)["run-status"] == "running"


@pytest.mark.parametrize("tier,basis,expected_rows,expected_fill", [
    ("code-grounded", "wired", 1, "100%"),
    ("code-grounded", "claimed", 1, "0%"),
    ("code-grounded", "afforded", 1, "0%"),
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
    data["members"] = [
        {"path": name, "sha256": digest(retained.with_name(name)), "type": MEMBER_TYPES[name]}
        for name in MEMBER_TYPES
    ]
    replace_frontmatter(retained, data)
    review = tmp_path / "kb/agentic-systems/reviews/example-system.md"
    replace_frontmatter(review, {**frontmatter(review), "analysis-overview-sha256": digest(retained)})
    monkeypatch.setattr(analyze_matrix, "REPO_ROOT", tmp_path)
    assert analyze_matrix.main([]) == 0
    output = capsys.readouterr().out
    assert f"rows: {expected_rows}  (code-grounded" in output
    line = next(line for line in output.splitlines() if line.startswith("storage_substrate "))
    assert line.split()[1] == expected_fill
    if expected_rows:
        assert f"known:{basis}" in output


def rerun_publication_fixture(tmp_path: Path) -> tuple[PublicationSpec, bytes, bytes]:
    """Create a second run over a real, uncommitted first publication."""
    from commonplace.lib.agentic_publication import inspect_destination

    state, first, _ = publication_fixture(tmp_path)
    publish_publication(first)
    old_review = (tmp_path / first.generated_destination).read_bytes()
    old_set = {name: (state.parent / name).read_bytes() for name in ("overview.md", *MEMBER_TYPES)}
    next_id = RUN_ID[:-2] + "02"
    new_dir = state.parent.with_name(next_id)
    shutil.copytree(state.parent, new_dir)
    for path in new_dir.glob("*.md"):
        path.write_text(path.read_text().replace(RUN_ID, next_id))
    report = new_dir / "memory-report.md"
    replace_frontmatter(report, {**frontmatter(report),
        "canonical-register-sha256": digest(new_dir / "memory-input.md")})
    refinalize(new_dir)
    next_state = new_dir / "run-state.md"
    values = frontmatter(next_state)
    values.update({"run-status": "running", "result-disposition": None,
                   "overview": None, "generated-review": None})
    replace_frontmatter(next_state, values)
    candidate = new_dir / "review-candidate.md"
    candidate.write_text(old_review.decode().replace(RUN_ID, next_id))
    replace_frontmatter(candidate, {**frontmatter(candidate), "analysis-overview-sha256": digest(new_dir / "overview.md")})
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
        "replaceable": True, "exists": False, "expected_incumbent_sha256": "absent",
    }
    secret = "INCUMBENT-PROSE-MUST-NOT-ENTER-COORDINATOR-CONTEXT"
    candidate = spec.generated_candidate_path
    candidate.write_text(candidate.read_text() + "\n" + secret + "\n")
    publish_publication(spec)
    assert main(args, cwd=tmp_path) == 0
    output = capsys.readouterr().out
    assert secret not in output
    assert set(json.loads(output)) == {"replaceable", "exists", "expected_incumbent_sha256"}
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
    ("missing-overview", "cannot read incumbent retained overview"),
    ("overview", "overview hash mismatch"),
    ("member", "manifest: runtime.md bytes hash to"),
    ("source", "same source"),
    ("committed-then-edited", "local changes"),
])
def test_inspection_rejects_unverified_incumbents(tmp_path: Path, mutation: str, error: str) -> None:
    """An incumbent is checked by its bytes and pins; no publication receipt is read."""
    from commonplace.lib.agentic_publication import inspect_destination
    spec, _, _ = rerun_publication_fixture(tmp_path)
    review = tmp_path / spec.generated_destination
    metadata = frontmatter(review)
    retained = tmp_path / metadata["analysis-overview"]
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
    with pytest.raises(ValueError, match=error):
        inspect_destination(repo_root=tmp_path, generated_destination=spec.generated_destination,
                            source_identity=metadata["source-identity"])


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


def test_publish_requires_inspected_digest_even_for_valid_incumbent(tmp_path: Path) -> None:
    from dataclasses import replace
    spec, old_review, _ = rerun_publication_fixture(tmp_path)
    with pytest.raises(ValueError, match="changed since inspection"):
        publish_publication(replace(spec, expected_incumbent_sha256="absent"))
    assert (tmp_path / spec.generated_destination).read_bytes() == old_review


def test_rerun_rollback_preserves_concurrent_incumbent_edit(tmp_path: Path, monkeypatch) -> None:
    from commonplace.lib import agentic_publication as publication
    spec, _, _ = rerun_publication_fixture(tmp_path)
    original_write = publication._atomic_write
    public = tmp_path / spec.generated_destination
    changed = public.read_bytes() + b"\nConcurrent human edit.\n"

    def edit_after_backup(path, content):
        original_write(path, content)
        if path.name == "incumbent-review.md":
            public.write_bytes(changed)

    monkeypatch.setattr(publication, "_atomic_write", edit_after_backup)
    with pytest.raises(ValueError, match="changed before replacement"):
        publish_publication(spec)
    assert public.read_bytes() == changed
    assert frontmatter(spec.run_state_path)["run-status"] == "running"
    assert not (tmp_path / agentic_set.retained_overview_path(RUN_ID[:-2] + "02")).exists()


def test_rerun_failure_restores_uncommitted_publication(tmp_path: Path, monkeypatch) -> None:
    spec, old_review, old_set = rerun_publication_fixture(tmp_path)
    original_write = agentic_publication._atomic_write

    def fail_completion(path, content):
        if path == spec.run_state_path:
            raise OSError("injected completion failure")
        original_write(path, content)

    monkeypatch.setattr(agentic_publication, "_atomic_write", fail_completion)
    with pytest.raises(OSError, match="injected completion failure"):
        publish_publication(spec)
    assert (tmp_path / spec.generated_destination).read_bytes() == old_review
    for name, retained in agentic_set.retained_set_paths(RUN_ID).items():
        assert (tmp_path / retained).read_bytes() == old_set[name]
    assert frontmatter(spec.run_state_path)["run-status"] == "running"
    assert spec.generated_candidate_path.exists()
    assert not (tmp_path / agentic_set.retained_overview_path(RUN_ID[:-2] + "02")).exists()


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
    ("kb/agentic-systems/reviews/sibling.md", True),
    ("kb/reports/retained/agentic-system-analysis/AAS-2026-09-04-sibling-01/overview.md", True),
    ("scratch.txt", True),
])
def test_untracked_files_block_publication_only_under_kb_outside_its_outputs(
    tmp_path: Path, path: str, accepted: bool
) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    write(tmp_path / path, "A sibling run's publication, or a stray file.\n")
    if accepted:
        assert inspect(tmp_path, spec)["replaceable"]
        assert prepare_publication(spec).prepared
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


def test_publication_requires_the_method_unchanged_since_inputs_commit(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    # Unrelated commits after inputs-commit, such as a sibling's publication, are fine.
    note = write(tmp_path / "kb/notes/unrelated.md", "# Unrelated\n")
    commit_paths(tmp_path, "Unrelated change", note)
    assert prepare_publication(spec).prepared
    # A method change since inputs-commit is not.
    method = tmp_path / "kb/types/agentic-system-analysis-overview.md"
    method.write_text(method.read_text() + "\nMethod change.\n")
    commit_paths(tmp_path, "Change the method", method)
    with pytest.raises(ValueError, match="method paths changed since inputs-commit") as error:
        publish_publication(spec)
    assert "kb/types/agentic-system-analysis-overview.md" in str(error.value)
    assert not (tmp_path / spec.generated_destination).exists()
    assert frontmatter(state)["run-status"] == "running"


def test_publication_requires_inputs_commit_to_be_an_ancestor_of_head(tmp_path: Path) -> None:
    state, spec, _ = publication_fixture(tmp_path)
    pin_inputs_commit(state.parent, "0" * 40, spec.generated_candidate_path)
    with pytest.raises(ValueError, match="not an ancestor of HEAD"):
        prepare_publication(spec)
    assert frontmatter(state)["run-status"] == "running"


def test_member_validation_catches_shorthand_in_ordinary_prose(tmp_path: Path) -> None:
    state, _, _ = publication_fixture(tmp_path)
    runtime = state.parent / "runtime.md"
    runtime.write_text(runtime.read_text() + "\nBroken integration: OBJ-1/O2/O3.\n")
    checked = validation.validate_note(runtime, repo_root=tmp_path)
    assert any("expand shorthand" in error for error in checked.fails)


def test_git_source_example_can_initialize_running_state(tmp_path: Path) -> None:
    state, _, _ = publication_fixture(tmp_path)
    values = frontmatter(state)
    actual = values["source"]
    contract = (REPO_ROOT / "kb/types/agentic-system-analysis-run-state.md").read_text()
    example = yaml.safe_load(re.search(r"```yaml\n(source:.*?)```", contract, re.DOTALL)[1])["source"]
    example.update({key: actual[key] for key in ("identity", "revision", "path")})
    replace_frontmatter(state, {**values, "source": example})
    assert validation.validate_note(state, repo_root=tmp_path).fails == []


def test_quoted_code_must_occur_inside_the_cited_range(tmp_path: Path) -> None:
    from commonplace.lib.agentic_analysis import SourceIdentity, _verify_quote_anchors

    root, _ = git_checkout(tmp_path / "source")
    source = write(root / "operation.py", "# Navigation heading\n\ndef apply():\n    rebuild_prompt()\n")
    commit_incumbent(root, source)
    revision = subprocess.check_output(["git", "-C", str(root), "rev-parse", "HEAD"], text=True).strip()
    identity = SourceIdentity("git", "https://github.com/example/system", revision, root, None)
    quote = f"> rebuild_prompt()\n> --- [operation](https://github.com/example/system/blob/{revision}/operation.py#L1)\n"
    _, errors = _verify_quote_anchors(quote, source=identity)
    assert any("cited line range" in error for error in errors)
    _, errors = _verify_quote_anchors(quote.replace("#L1", "#L4"), source=identity)
    assert errors == []
    source.write_text("rebuild_prompt_WRONG()\n")
    _, errors = _verify_quote_anchors(quote.replace("rebuild_prompt()", "rebuild_prompt_WRONG()"), source=identity)
    assert any("quote does not occur" in error for error in errors)


def test_quote_generation_needs_no_report_or_publication(tmp_path, capsys):
    state, spec, _ = publication_fixture(tmp_path)
    for name in ("overview.md", "memory-report.md", *MEMBER_TYPES):
        (state.parent / name).unlink()
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


def test_quote_cli_rejects_mixed_selection_and_single_arguments(tmp_path):
    state, _, _ = publication_fixture(tmp_path)
    selections = write(tmp_path / "selections.json", "[]")
    with pytest.raises(SystemExit):
        quote.main(
            [str(state), "--selections", str(selections), "--source-path", "README.md"],
            cwd=tmp_path,
        )


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
    runtime = state.parent / "runtime.md"
    for text in [*source_text.splitlines()[1:4], "* repeated comment"]:
        payload = generate_quotes(text, source=identity, source_path="README.md")
        if text == "* repeated comment":
            assert [entry["start_line"] for entry in payload["occurrences"]] == [5, 6]
        citation = payload if isinstance(payload, str) else payload["occurrences"][-1]["citation"]
        runtime.write_text(runtime.read_text() + "\n" + citation)
    refinalize(state.parent)
    replace_frontmatter(spec.generated_candidate_path, {
        **frontmatter(spec.generated_candidate_path),
        "analysis-overview-sha256": digest(state.parent / "overview.md"),
    })
    assert prepare_publication(spec).prepared
    published = publish_publication(spec)
    checked = validation.validate_note(state, repo_root=tmp_path)
    assert not checked.warns and not checked.fails
    assert (tmp_path / published.retained_path).read_bytes() == (state.parent / "overview.md").read_bytes()

    # An author-added bad range is still rejected by the same ordinary validator.
    runtime.write_text(runtime.read_text() + "\nAuthor anchor: `README.md:999`.\n")
    values = frontmatter(state)
    sync_set(tmp_path, values)
    replace_frontmatter(state, values)
    checked = validation.validate_note(state, repo_root=tmp_path)
    assert any("outside the recorded blob" in error for error in checked.fails)


@pytest.mark.parametrize("addition,diagnostic", [
    ("\nBad range: `README.md:999`.\n", "outside the recorded blob"),
    ("\n> absent source text\n> --- `README.md` @ `{revision}`\n", "quote does not occur"),
    ("\n> Frozen source\n> --- `README.md` @ `" + "0" * 40 + "`\n", "revision"),
    ("\n> --- `README.md` @ `{revision}`\n", "no quoted text"),
])
def test_publication_validator_rejects_bad_evidence_without_writes(tmp_path, addition, diagnostic):
    state, spec, _ = publication_fixture(tmp_path)
    artifact = state.parent / "memory-report.md"
    revision = frontmatter(state)["source"]["revision"]
    artifact.write_text(artifact.read_text() + addition.format(revision=revision))
    refinalize(state.parent)
    before = {p: p.read_bytes() for p in state.parent.iterdir() if p.is_file()}
    with pytest.raises(ValueError, match=diagnostic):
        prepare_publication(spec)
    assert before == {p: p.read_bytes() for p in state.parent.iterdir() if p.is_file()}
    assert not (tmp_path / spec.generated_destination).exists()


def test_source_failure_stops_dependent_shell_command(tmp_path):
    state, spec, _ = publication_fixture(tmp_path)
    artifact = state.parent / "memory-report.md"
    artifact.write_text(artifact.read_text() + "\nBad range: `README.md:999`.\n")
    refinalize(state.parent)
    marker = tmp_path / "incorrect-success"
    command = shlex.join([
        sys.executable, "-m", "commonplace.cli.agentic_analysis_publication",
        "prepare", str(state), "--generated-candidate", str(spec.generated_candidate_path),
        "--generated-destination", spec.generated_destination,
        "--expected-incumbent-sha256", "absent",
    ])
    later = shlex.join([sys.executable, "-c", "from pathlib import Path; Path('incorrect-success').touch()"])
    result = subprocess.run(["bash", "-c", command + " && " + later], cwd=tmp_path, capture_output=True, text=True, check=False)
    assert result.returncode == 1
    assert "outside the recorded blob" in result.stderr
    assert not marker.exists()
    assert not (tmp_path / spec.generated_destination).exists()


def test_adjacent_attributed_quotes_are_checked_independently(tmp_path):
    from commonplace.lib.agentic_analysis import SourceIdentity, _verify_quote_anchors

    root, revision = git_checkout(tmp_path / "source")
    identity = SourceIdentity("git", "https://github.com/example/system", revision, root, None)
    text = f"""Inline `>` and `> ---` are ordinary prose.
> # Frozen source
> --- `README.md` @ `{revision}`
> Frozen source
> --- `README.md` @ `{revision}`
"""
    checks, errors = _verify_quote_anchors(text, source=identity)
    assert len(checks) == 2
    assert errors == []
    _, errors = _verify_quote_anchors(text.replace("> Frozen source", "> fabricated text"), source=identity)
    assert len(errors) == 1
    assert "quote does not occur" in errors[0]


def test_publication_trial_stops_wrong_specialist_range_then_publishes_unranged(
    tmp_path: Path, monkeypatch,
):
    original_checkout = git_checkout

    def two_line_checkout(path):
        root, _ = original_checkout(path)
        readme = write(root / "README.md", "# Frozen source\nUnrelated second line.\n")
        commit_incumbent(root, readme)
        revision = subprocess.check_output(
            ["git", "-C", str(root), "rev-parse", "HEAD"], text=True,
        ).strip()
        return root, revision

    monkeypatch.setattr(sys.modules[__name__], "git_checkout", two_line_checkout)
    state, spec, _ = publication_fixture(tmp_path)
    report = state.parent / "memory-report.md"
    original = report.read_bytes()
    revision = frontmatter(state)["source"]["revision"]
    with report.open("a") as handle:
        handle.write(f"\n> Frozen source\n> --- `README.md:2` @ `{revision}`\n")
    refinalize(state.parent)
    with pytest.raises(ValueError, match="cited line range"):
        prepare_publication(spec)
    assert not (tmp_path / spec.generated_destination).exists()
    report.write_bytes(original)
    refinalize(state.parent)
    replace_frontmatter(spec.generated_candidate_path, {
        **frontmatter(spec.generated_candidate_path),
        "analysis-overview-sha256": digest(state.parent / "overview.md"),
    })
    published = publish_publication(spec)
    assert (tmp_path / published.retained_path).exists()
    assert frontmatter(state)["run-status"] == "complete"
