"""Reusable retained-set and member fixtures, without workflow execution."""
from __future__ import annotations

import json
import shutil
import subprocess
from copy import deepcopy
from hashlib import sha256
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

from commonplace.lib import systems_matrix, validation
from commonplace.lib.agentic_analysis import sets as agentic_set
from commonplace.lib.agentic_analysis.records import amendment_index

REPO_ROOT = Path(__file__).resolve().parents[3]


RUN_ID = "AAS-2026-09-04-example-system-01"


RETAINED_OVERVIEW = agentic_set.RETAINED_ROOT / "example-system" / "overview.md"


SOURCE = "https://example.invalid/example-system"


STATE_DIR = Path("kb/agentic-system-analyses/state")


INPUTS_COMMIT = "f" * 40


def comparison_schema():
    schema = json.loads((Path(__file__).resolve().parents[3] /
                         "kb/agentic-system-analyses/types/agent-memory-profile.schema.yaml").read_text())
    comparison = deepcopy(schema["allOf"][1]["properties"]["frontmatter"]["properties"]["memory-comparison"])
    comparison["$defs"] = schema["$defs"]
    Draft202012Validator.check_schema(comparison)
    return Draft202012Validator(comparison)


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


def retained_fixture(tmp_path: Path) -> Path:
    """A source-backed retained set, constructed without running or publishing."""
    configure_types(tmp_path)
    source, revision = git_checkout(tmp_path / "related-systems/example--system")
    run_dir = run_dir_of(tmp_path)
    write_set(run_dir, revision, source_path=source)
    retain_set(tmp_path, run_dir)
    return tmp_path / RETAINED_OVERVIEW.parent
